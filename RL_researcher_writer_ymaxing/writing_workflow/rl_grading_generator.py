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

Usage (from writing_workflow/):
  uv run python rl_grading_generator.py                               # all episodes
  uv run python rl_grading_generator.py --dry-run                    # plan only
  uv run python rl_grading_generator.py --articles 02_workflows_vs_agents
  uv run python rl_grading_generator.py --presets 0 1
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
EPISODES_DIR = _THIS_DIR.parent / "rl_training_data" / "episodes"

# Eval dataset with ground-truth articles and guidelines
EVAL_DATA_DIR = _THIS_DIR / "inputs" / "evals" / "dataset" / "data"

# Train articles (L2, L3, L5, L8, L11) -- must match Phase 1 / Phase 2a
TRAIN_ARTICLES: list[str] = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "08_react_practice",
    "11_multimodal",
]

N_PRESETS = 6  # preset IDs 0-5
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 30  # seconds; attempt N waits N * 30s

# Minimum pause between episodes (seconds).
# Each episode fires 2 concurrent Pro calls.  The UserIntentMetric prompt
# includes the full research.md (~130K-300K tokens), so back-to-back
# episodes can sustain high TPM.  20s provides a reasonable cooldown;
# increase to 30s if quota errors are observed.
INTER_EPISODE_DELAY_SECS: float = 20.0

# Grading model: Gemini 2.5 Pro (LLM-as-judge)
GRADING_MODEL = SupportedModels.GOOGLE_GEMINI_25_PRO

# Shared model config: lower thinking budget vs the per-metric default (4096)
# to reduce cost and latency; Pro reasons reliably at 1024 for binary scoring.
_GRADING_CONFIG = ModelConfig(temperature=0.0, thinking_budget=1024, include_thoughts=False, max_retries=3)

# ---------------------------------------------------------------------------
# Metric instances (shared across episodes; each ascore() creates its own client)
# ---------------------------------------------------------------------------

_follows_gt_metric = FollowsGTMetric(
    model=GRADING_MODEL,
    name="ground_truth",
    track=True,
    project_name="rl-grading",
    model_config=_GRADING_CONFIG,
)
_user_intent_metric = UserIntentMetric(
    model=GRADING_MODEL,
    name="user_intent",
    track=True,
    project_name="rl-grading",
    model_config=_GRADING_CONFIG,
)


# ---------------------------------------------------------------------------
# Core grading logic
# ---------------------------------------------------------------------------


def _build_exploration_sources(research_dir: Path) -> str | None:
    """Build a formatted exploration-sources string from url_phases.json.

    Reads url_phases.json to identify which URLs were retrieved during the exploration
    phase, then extracts their query and answer summary from tavily_results_selected.md.
    Returns None when no exploration URLs exist or when required files are missing.
    """
    url_phases_file = research_dir / "url_phases.json"
    tavily_file = research_dir / "tavily_results_selected.md"

    if not url_phases_file.exists() or not tavily_file.exists():
        return None

    url_phases: dict[str, str] = json.loads(url_phases_file.read_text(encoding="utf-8"))
    exploration_urls = {url for url, phase in url_phases.items() if "[EXPLORATION]" in phase}
    if not exploration_urls:
        return None

    tavily_content = tavily_file.read_text(encoding="utf-8")
    entries: list[str] = []
    for block in tavily_content.split("-----"):
        url_match = re.search(r"### Source \[\d+\]: (\S+)", block)
        if not url_match:
            continue
        url = url_match.group(1).strip()
        if url not in exploration_urls:
            continue
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
    article_md = (episode_dir / "article.md").read_text(encoding="utf-8")
    gt_md = (EVAL_DATA_DIR / article_name / "article_ground_truth.md").read_text(encoding="utf-8")
    guideline_md = (EVAL_DATA_DIR / article_name / "article_guideline.md").read_text(encoding="utf-8")
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


async def run_pipeline(
    articles: Sequence[str],
    presets: Sequence[int],
    dry_run: bool = False,
) -> None:
    """Iterate over all (article, preset) combinations and grade each episode."""
    ready: list[tuple[Path, str, str]] = []  # (ep_dir, article_name, ep_name) -- has article.md, no scores.json
    done: list[str] = []  # already have scores.json
    missing_article: list[str] = []  # article.md absent
    missing_research: list[str] = []  # research.md absent

    for article in articles:
        for preset_id in presets:
            ep_name = _episode_dir_name(article, preset_id)
            ep_dir = EPISODES_DIR / ep_name

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
    logger.info(f"  To grade    : {len(ready)}")
    logger.info(f"  Already done: {len(done)}")
    logger.info(f"  Missing article.md : {len(missing_article)}")
    logger.info(f"  Missing research.md: {len(missing_research)}")
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

    succeeded = 0
    failed = 0
    for i, (ep_dir, article_name, ep_name) in enumerate(ready):
        if i > 0:
            logger.info(f"Waiting {INTER_EPISODE_DELAY_SECS:.0f}s before next episode (TPM cooldown) ...")
            await asyncio.sleep(INTER_EPISODE_DELAY_SECS)
        ok = await run_episode(ep_dir, article_name, ep_name)
        if ok:
            succeeded += 1
        else:
            failed += 1

    logger.info("=" * 60)
    logger.info(f"Grading complete: {succeeded} succeeded, {failed} failed, {len(done)} already done")
    logger.info("=" * 60)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Phase 2b: grade article.md episodes and write scores.json")
    parser.add_argument(
        "--articles",
        nargs="+",
        default=TRAIN_ARTICLES,
        metavar="ARTICLE",
        help="Article names to process (default: all train articles)",
    )
    parser.add_argument(
        "--presets",
        nargs="+",
        type=int,
        default=list(range(N_PRESETS)),
        metavar="N",
        help="Preset IDs to process (default: 0-5)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be graded without running any LLM calls",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    asyncio.run(
        run_pipeline(
            articles=args.articles,
            presets=args.presets,
            dry_run=args.dry_run,
        )
    )


if __name__ == "__main__":
    main()
