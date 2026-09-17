"""
Phase 2b -- RL Training Data Generator (Grading)

Grades each article.md on 9 dimensions using:
  - FollowsGTMetric  (6 dims): core_content, flow, structure,
                                depth_enhancement, breadth_enhancement, core_preservation
  - UserIntentMetric (3 dims): guideline_adherence, research_anchoring, golden_source_priority

All 9 scores are stored in scores.json as raw floats (Option 4).
Reward combination formula is deferred to Phase 3 (GRPO training).

Resumability:
  - scores.json exists -> skip episode (zero cost, single sentinel)

Both metrics run concurrently per episode (asyncio.gather) since they are independent.
Episodes are processed sequentially to respect Gemini rate limits.

Grading judge model defaults to Gemini 2.5 Pro; pass --grading-model claude to use
Claude Sonnet instead (requires ANTHROPIC_API_KEY + langchain-anthropic installed).

Usage (from writing_workflow/):
  uv run python rl_pipeline/rl_grading_generator.py                               # all episodes
  uv run python rl_pipeline/rl_grading_generator.py --dry-run                    # plan only
  uv run python rl_pipeline/rl_grading_generator.py --articles 02_workflows_vs_agents
  uv run python rl_pipeline/rl_grading_generator.py --presets 0 1
  uv run python rl_pipeline/rl_grading_generator.py --test                       # held-out test episodes
  uv run python rl_pipeline/rl_grading_generator.py --grading-model claude       # judge with Claude Sonnet
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import time
from pathlib import Path
from typing import Sequence

from brown.evals.metrics import FollowsGTMetric, UserIntentMetric
from brown.models import ModelConfig, SupportedModels

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_grading_generator")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_THIS_DIR = Path(__file__).resolve().parent

# Episode dirs produced by Phase 1 / Phase 2a
EPISODES_DIR = _THIS_DIR.parent.parent / "rl_training_data" / "episodes"

# Held-out test episodes dir
TEST_EPISODES_DIR = _THIS_DIR.parent.parent / "rl_training_data" / "test_episodes"

# Eval dataset with ground-truth articles and guidelines
EVAL_DATA_DIR = _THIS_DIR.parent / "inputs" / "evals" / "dataset" / "data"

# Train articles (L2, L3, L5, L6, L8, L9, L11) -- must match Phase 1 / Phase 2a
# Variant articles (var_demanding, var_minimal, var_standard) for L8 and L9
TRAIN_ARTICLES: list[str] = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "08_react_practice__var_demanding",
    "08_react_practice__var_minimal",
    "08_react_practice__var_standard",
    "09_RAG",
    "09_RAG__var_demanding",
    "09_RAG__var_minimal",
    "09_RAG__var_standard",
    "11_multimodal",
]

# Held-out test articles -- must match Phase 1 / Phase 2a
TEST_ARTICLES: list[str] = ["04_structured_outputs", "07_reasoning_planning"]

N_PRESETS = 4  # preset IDs 0-3 (skip / light / standard / deep)
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 30  # seconds; attempt N waits N * 30s

DEFAULT_CONCURRENCY = 2  # concurrent episodes; Tier 2: 1K RPM / 5M TPM

# Small stagger between episode launches to soften the initial burst.
# With DEFAULT_CONCURRENCY=2 each episode fires 2 concurrent Pro calls
# (4 simultaneous at peak), well within Tier 2 limits.
INTER_EPISODE_DELAY_SECS: float = 5.0

# Grading model: Gemini 2.5 Pro (LLM-as-judge) by default.
# Gemini occasionally makes blatant scoring mistakes that have historically
# needed manual correction (see grok_planner_test_results/run13_rl_grok_pipeline_analysis.md,
# Part 4); Claude Sonnet is offered as an alternative judge via --grading-model claude.
GRADING_MODEL = SupportedModels.GOOGLE_GEMINI_25_PRO

# CLI-facing short names -> SupportedModels enum value.
_MODEL_CHOICES: dict[str, SupportedModels] = {
    "gemini": SupportedModels.GOOGLE_GEMINI_25_PRO,
    "claude": SupportedModels.ANTHROPIC_CLAUDE_SONNET,
}

# Shared model config: lower thinking budget vs the per-metric default (4096)
# to reduce cost and latency; Pro reasons reliably at 1024 for binary scoring.
# thinking_budget/include_thoughts are Gemini-only params and are silently
# stripped for non-Google models by brown.models.get_model (GOOGLE_ONLY_PARAMS).
_GRADING_CONFIG = ModelConfig(temperature=0.0, thinking_budget=1024, include_thoughts=False, max_retries=3)

# ---------------------------------------------------------------------------
# Metric instances (shared across episodes; each ascore() creates its own client)
#
# Built via _build_metrics() so the judge model can be swapped at runtime
# (--grading-model) without touching call sites -- _grade_episode() always
# reads the current _follows_gt_metric/_user_intent_metric module globals.
# ---------------------------------------------------------------------------


def _build_metrics(model: SupportedModels) -> tuple[FollowsGTMetric, UserIntentMetric]:
    follows_gt_metric = FollowsGTMetric(
        model=model,
        name="ground_truth",
        track=True,
        project_name="rl-grading",
        model_config=_GRADING_CONFIG,
    )
    user_intent_metric = UserIntentMetric(
        model=model,
        name="user_intent",
        track=True,
        project_name="rl-grading",
        model_config=_GRADING_CONFIG,
    )
    return follows_gt_metric, user_intent_metric


def configure_grading_model(model: SupportedModels) -> None:
    """Rebuild the module-level grading metrics against *model*.

    Must be called (if at all) before any episode is graded -- e.g. from
    main() right after parsing --grading-model, before run_pipeline() starts.
    """
    global GRADING_MODEL, _follows_gt_metric, _user_intent_metric
    GRADING_MODEL = model
    _follows_gt_metric, _user_intent_metric = _build_metrics(model)


_follows_gt_metric, _user_intent_metric = _build_metrics(GRADING_MODEL)


# ---------------------------------------------------------------------------
# Core grading logic
# ---------------------------------------------------------------------------


def _build_exploration_sources(research_dir: Path) -> str | None:
    """Build a formatted exploration-sources string from tavily_results_selected.md.

    Scans tavily_results_selected.md for blocks tagged 'Phase: [EXPLORATION]'.
    This captures all exploration-phase Tavily results — both snippet-only entries
    and those selected for full scraping — making url_phases.json unnecessary here.

    Returns None when no exploration blocks exist or the file is missing.
    """
    tavily_file = research_dir / "tavily_results_selected.md"

    if not tavily_file.exists():
        return None

    tavily_content = tavily_file.read_text(encoding="utf-8")

    entries: list[str] = []
    for block in tavily_content.split("-----"):
        if "[EXPLORATION]" not in block:
            continue

        url_match = re.search(r"### Source \[\d+\]: (\S+)", block)
        url = url_match.group(1).strip() if url_match else ""
        query_match = re.search(r"Query: (.+?)(?=\n|$)", block)
        query = query_match.group(1).strip() if query_match else ""
        answer_match = re.search(r"Answer: (.+?)(?=\n-----|\Z)", block, re.DOTALL)
        if answer_match:
            answer = answer_match.group(1).strip()
            sentences = re.split(r"(?<=[.!?])\s+", answer)
            summary = " ".join(sentences[:2])
            if len(summary) > 300:
                summary = summary[:300] + "..."
        else:
            summary = ""
        entries.append(f"- {url}\n  Query: {query}\n  Summary: {summary}")

    if not entries:
        return None

    header = (
        "The following sources were retrieved during the exploration phase "
        "(gap-driven research beyond the article guideline scope). "
        "Depth and breadth additions score 1 only if traceable to one or more of these sources."
    )
    return header + "\n\n" + "\n".join(entries)


async def _grade_episode(episode_dir: Path, article_name: str) -> tuple[dict[str, float], dict[str, str]]:
    """Run FollowsGTMetric and UserIntentMetric concurrently; return merged scores and reasons."""
    gt_article_name = _strip_replicate_suffix(article_name)
    article_md = (episode_dir / "article.md").read_text(encoding="utf-8")
    gt_md = (EVAL_DATA_DIR / gt_article_name / "article_ground_truth.md").read_text(encoding="utf-8")
    guideline_md = (EVAL_DATA_DIR / gt_article_name / "article_guideline.md").read_text(encoding="utf-8")
    research_md = (episode_dir / "research.md").read_text(encoding="utf-8")
    exploration_sources = _build_exploration_sources(episode_dir / ".research")

    gt_results, ui_results = await asyncio.gather(
        _follows_gt_metric.ascore(output=article_md, expected_output=gt_md, exploration_sources=exploration_sources),
        _user_intent_metric.ascore(
            input=guideline_md,
            context={"research": research_md},
            output=article_md,
        ),
    )

    scores: dict[str, float] = {}
    reasons: dict[str, str] = {}
    for sr in gt_results + ui_results:
        scores[sr.name] = round(sr.value, 6)
        reasons[sr.name] = sr.reason or ""

    return scores, reasons


async def run_episode(episode_dir: Path, article_name: str, episode_name: str) -> bool:
    """Grade one episode; writes scores.json on success. Returns True on success."""
    scores_path = episode_dir / "scores.json"

    if scores_path.exists():
        logger.info(f"[SKIP]  {episode_name} -- scores.json already exists")
        return True

    if not (episode_dir / "article.md").exists():
        logger.warning(f"[SKIP]  {episode_name} -- article.md missing (run Phase 2a first)")
        return False

    if not (episode_dir / "research.md").exists():
        logger.warning(f"[SKIP]  {episode_name} -- research.md missing (run Phase 1 first)")
        return False

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            logger.info(f"[START] {episode_name} (attempt {attempt}/{MAX_RETRIES})")
            t0 = time.monotonic()

            scores, reasons = await _grade_episode(episode_dir, article_name)

            elapsed = time.monotonic() - t0
            reasoning_path = episode_dir / "reasoning.json"
            reasoning_path.write_text(json.dumps(reasons, indent=2), encoding="utf-8")
            scores_path.write_text(json.dumps(scores, indent=2), encoding="utf-8")
            logger.info(f"[DONE]  {episode_name}  ({elapsed:.1f}s)\n        {json.dumps(scores, separators=(',', ':'))}")
            return True

        except Exception as exc:
            logger.warning(f"[FAIL]  {episode_name} attempt {attempt}: {exc}")
            # Context-window overflows (e.g. Claude's 200K token limit) are deterministic --
            # retrying with the exact same prompt will fail identically every time, so don't
            # waste the backoff windows on it.
            if "prompt is too long" in str(exc) or "context_length" in str(exc).lower():
                logger.error(f"[ERROR] {episode_name} -- prompt exceeds model context window, not retrying")
                break
            if attempt < MAX_RETRIES:
                wait = attempt * RETRY_BACKOFF_BASE
                logger.info(f"        retrying in {wait}s ...")
                await asyncio.sleep(wait)

    logger.error(f"[ERROR] {episode_name} failed after {MAX_RETRIES} attempts -- scores.json NOT written")
    return False


# ---------------------------------------------------------------------------
# Pipeline orchestration
# ---------------------------------------------------------------------------


def _episode_dir_name(article: str, preset_id: int) -> str:
    """Match the naming convention from Phase 1."""
    return f"{article}__preset{preset_id}"


def _strip_replicate_suffix(article: str) -> str:
    """Map a noise-experiment replicate name back to its base article for GT lookup.

    e.g. '09_RAG__var_standard__replicate2' -> '09_RAG__var_standard' (which does
    have an EVAL_DATA_DIR entry), while the episode dir itself keeps the full
    replicate name so it never collides with the real production episode dir.
    """
    return re.sub(r"__replicate\d+$", "", article)


async def run_pipeline(
    articles: Sequence[str],
    presets: Sequence[int],
    dry_run: bool = False,
    max_concurrent: int = DEFAULT_CONCURRENCY,
    test_mode: bool = False,
    episodes_dir_override: Path | None = None,
) -> None:
    """Iterate over all (article, preset) combinations and grade each episode."""
    episodes_dir = episodes_dir_override or (TEST_EPISODES_DIR if test_mode else EPISODES_DIR)

    ready: list[tuple[Path, str, str]] = []  # (ep_dir, article_name, ep_name) -- has article.md, no scores.json
    done: list[str] = []  # already have scores.json
    missing_article: list[str] = []  # article.md absent
    missing_research: list[str] = []  # research.md absent

    for article in articles:
        for preset_id in presets:
            ep_name = _episode_dir_name(article, preset_id)
            ep_dir = episodes_dir / ep_name

            if not ep_dir.exists():
                missing_research.append(ep_name)
                continue

            if (ep_dir / "scores.json").exists():
                done.append(ep_name)
                continue

            if not (ep_dir / "research.md").exists():
                missing_research.append(ep_name)
                continue

            if not (ep_dir / "article.md").exists():
                missing_article.append(ep_name)
                continue

            ready.append((ep_dir, article, ep_name))

    # Report plan
    logger.info("=" * 60)
    logger.info("Phase 2b grading plan")
    logger.info(f"  Mode            : {'test (held-out)' if test_mode else 'train'}")
    logger.info(f"  To grade    : {len(ready)}")
    logger.info(f"  Already done: {len(done)}")
    logger.info(f"  Missing article.md : {len(missing_article)}")
    logger.info(f"  Missing research.md: {len(missing_research)}")
    logger.info(f"  Max concurrent  : {max_concurrent}")
    logger.info(f"  Episodes dir    : {episodes_dir}")
    if missing_article:
        logger.info(f"  [no article.md] {missing_article}")
    if missing_research:
        logger.info(f"  [no research.md] {missing_research}")
    logger.info("=" * 60)

    if dry_run:
        logger.info("DRY RUN -- no grading performed")
        for ep_dir, article_name, ep_name in ready:
            logger.info(f"  would grade: {ep_name}")
        return

    sem = asyncio.Semaphore(max_concurrent)

    async def _bounded_grade(ep_dir: Path, article_name: str, ep_name: str) -> tuple[str, bool]:
        async with sem:
            ok = await run_episode(ep_dir, article_name, ep_name)
            return ep_name, ok

    grading_tasks = [_bounded_grade(ep_dir, article_name, ep_name) for ep_dir, article_name, ep_name in ready]
    logger.info(f"Launching {len(grading_tasks)} episode(s) with max_concurrent={max_concurrent} ...")
    results: list[tuple[str, bool]] = await asyncio.gather(*grading_tasks)

    succeeded = sum(1 for _, ok in results if ok)
    failed = sum(1 for _, ok in results if not ok)

    logger.info("=" * 60)
    logger.info(f"Grading complete: {succeeded} succeeded, {failed} failed, {len(done)} already done")
    if failed:
        for ep_name, ok in results:
            if not ok:
                logger.warning(f"  FAILED: {ep_name}")
    logger.info("=" * 60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 2b: grade article.md episodes and write scores.json")
    parser.add_argument(
        "--articles",
        nargs="+",
        default=None,
        metavar="ARTICLE",
        help="Article names to process (default: all train articles, or test articles with --test)",
    )
    parser.add_argument(
        "--presets",
        nargs="+",
        type=int,
        default=list(range(N_PRESETS)),
        metavar="N",
        help="Preset IDs to process (0, 1, 2, 3 — default: all 4)",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Use held-out test articles and test_episodes/ output directory",
    )
    parser.add_argument(
        "--episodes-dir",
        type=Path,
        default=None,
        dest="episodes_dir",
        help="Override the episodes root directory (default: rl_training_data/episodes or "
        "test_episodes/ with --test). Used for noise-measurement replicate experiments.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be graded without running any LLM calls",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        metavar="N",
        help=f"Max concurrent episodes (default: {DEFAULT_CONCURRENCY}; raise carefully — Gemini RPM limits apply)",
    )
    parser.add_argument(
        "--grading-model",
        choices=sorted(_MODEL_CHOICES),
        default="gemini",
        dest="grading_model",
        help="LLM-as-judge model to use for grading (default: gemini = Gemini 2.5 Pro). "
        "'claude' uses Claude Sonnet (requires ANTHROPIC_API_KEY and langchain-anthropic installed).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    configure_grading_model(_MODEL_CHOICES[args.grading_model])
    default_articles = TEST_ARTICLES if args.test else TRAIN_ARTICLES
    asyncio.run(
        run_pipeline(
            articles=args.articles if args.articles is not None else default_articles,
            presets=args.presets,
            dry_run=args.dry_run,
            max_concurrent=args.concurrency,
            test_mode=args.test,
            episodes_dir_override=args.episodes_dir,
        )
    )


if __name__ == "__main__":
    main()
