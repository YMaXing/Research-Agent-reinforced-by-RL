"""
Phase 1 — RL Training Data Generator (Research Generation)

Generates research.md files for all 6 exploration presets across 5 train articles.
Calls MCP server tool functions directly (no LLM orchestrator) for deterministic control.

Architecture:
  1. Build a shared "exploitation base" per article (steps 1-3: extract URLs, scrape
     golden/exploitation sources, run 3 exploitation rounds).
  2. Copy each base to 6 episode directories (one per preset).
  3. Run the preset-specific exploration phase (step 4) on each episode.
  4. Run post-exploration steps 5-7 (filter, scrape top sources, create research.md).

Usage (from research_agent_local/):
  uv run --project mcp_server python rl_data_generator.py           # default
  uv run --project mcp_server python rl_data_generator.py --dry-run # plan only
  uv run --project mcp_server python rl_data_generator.py --articles 02_workflows_vs_agents --presets 0
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import re
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Literal, Sequence

# ---------------------------------------------------------------------------
# Ensure the mcp_server package is importable and .env is loaded from the
# correct absolute path (settings uses env_file=".env" relative to CWD).
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent.parent
_MCP_SERVER_DIR = _THIS_DIR / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv  # noqa: E402  (dotenv is a dep of mcp-server)
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

# Tool functions (business logic, no MCP/router dependency) -----------------
from src.tools import (  # noqa: E402
    extract_guidelines_urls_tool,
    process_local_files_tool,
    scrape_and_clean_other_urls_tool,
    scrape_exploitation_guideline_urls_tool,
    process_github_urls_tool,
    transcribe_youtube_videos_tool,
    generate_next_queries_tool,
    generate_next_complementary_queries_tool,
    deduplicate_new_queries_tool,
    run_tavily_research_tool,
    select_research_sources_to_keep_tool,
    select_research_sources_to_scrape_tool,
    scrape_research_urls_tool,
    create_research_file_tool,
)
from src.app.dedup_new_queries_handler import parse_queries_from_file  # noqa: E402
from src.config.constants import (  # noqa: E402
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    NEXT_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
)
from src.config.settings import settings  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_data_generator")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Source articles live in the writing_workflow eval dataset
_EVAL_DATASET_DIR = (
    _THIS_DIR.parent
    / "writing_workflow"
    / "inputs"
    / "evals"
    / "dataset"
    / "data"
)

# Train articles (L2, L3, L5, L8, L11)
TRAIN_ARTICLES: list[str] = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "08_react_practice",
    "11_multimodal",
]

# Output root — sibling to research_agent_local/
_OUTPUT_ROOT = _THIS_DIR.parent / "rl_training_data"
BASES_DIR = _OUTPUT_ROOT / "bases"
EPISODES_DIR = _OUTPUT_ROOT / "episodes"

# Exploitation rounds (matches current prompt: 3 fixed rounds)
N_EXPLOITATION_ROUNDS = 3
N_EXPLOITATION_QUERIES_PER_ROUND = 5  # generate_next_queries_tool default


# ---------------------------------------------------------------------------
# Preset definitions
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class ExplorationPreset:
    """One bandit arm — defines the exploration strategy for a single episode."""
    id: int
    n_rounds: int
    focus_sequence: tuple[Literal["balanced", "depth", "breadth"], ...] = field(default=())
    label: str = ""

    def __post_init__(self) -> None:
        if self.n_rounds != len(self.focus_sequence):
            raise ValueError(
                f"Preset {self.id}: n_rounds={self.n_rounds} but "
                f"focus_sequence has {len(self.focus_sequence)} entries"
            )


PRESETS: tuple[ExplorationPreset, ...] = (
    ExplorationPreset(id=0, n_rounds=0, focus_sequence=(),
                      label="baseline_no_exploration"),
    ExplorationPreset(id=1, n_rounds=1, focus_sequence=("balanced",),
                      label="single_balanced"),
    ExplorationPreset(id=2, n_rounds=2, focus_sequence=("balanced", "depth"),
                      label="balanced_then_depth"),
    ExplorationPreset(id=3, n_rounds=2, focus_sequence=("depth", "breadth"),
                      label="depth_then_breadth"),
    ExplorationPreset(id=4, n_rounds=3, focus_sequence=("balanced", "depth", "breadth"),
                      label="full_progressive"),
    ExplorationPreset(id=5, n_rounds=3, focus_sequence=("depth", "breadth", "depth"),
                      label="depth_sandwich"),
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _episode_dir_name(article: str, preset: ExplorationPreset) -> str:
    return f"{article}__preset{preset.id}"


def _copy_base_to_episode(base_dir: Path, episode_dir: Path) -> None:
    """Deep-copy an exploitation base to an episode directory.

    Skips the copy if the episode dir already exists so that exploration
    sentinels written by a previous (interrupted) run are preserved.
    """
    if episode_dir.exists():
        logger.info(f"  Episode dir already exists, skipping base copy: {episode_dir.name}")
        return
    shutil.copytree(base_dir, episode_dir)
    logger.info(f"  Copied base → {episode_dir.name}")


def _extract_query_strings(research_dir: str) -> list[str]:
    """Read next_queries.md and return just the query strings."""
    nq_path = Path(research_dir) / RESEARCH_OUTPUT_FOLDER / NEXT_QUERIES_FILE
    pairs = parse_queries_from_file(nq_path)
    return [q for q, _reason in pairs]


# ---------------------------------------------------------------------------
# Pre-seeded content
# ---------------------------------------------------------------------------
# Place manually-copied sources inside the article's eval dataset folder:
#
#   writing_workflow/inputs/evals/dataset/data/<article>/pre_seeded/
#       urls_from_guidelines/          ← for golden sources (other_urls)
#       urls_from_guidelines_exploitation/  ← for exploitation sources
#
# Each .md file must start with the standard header:
#   # Title
#   **Source URL:** <https://...>
#
# The pipeline copies the file to .research/<subfolder>/ and removes the URL
# from guidelines_filenames.json so Firecrawl never attempts to scrape it.

_SOURCE_URL_RE = re.compile(r'\*\*Source URL:\*\*\s*<?([^>\s]+)>?', re.MULTILINE)

_PRE_SEEDED_FOLDER = "pre_seeded"

# Maps pre_seeded subfolder name → key(s) inside guidelines_filenames.json to purge
_PRE_SEEDED_SUBFOLDER_KEYS: dict[str, list[str]] = {
    URLS_FROM_GUIDELINES_FOLDER: ["other_urls"],
    URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER: ["exploitation_other_urls"],
}


def _apply_pre_seeded_content(article: str, base_dir: Path) -> None:
    """
    Copy manually-provided .md files into the base's .research subfolders and
    remove their URLs from guidelines_filenames.json so Firecrawl skips them.

    Call this AFTER step 1 (extract_guidelines_urls_tool) so that
    guidelines_filenames.json already exists.
    """
    pre_seeded_root = _EVAL_DATASET_DIR / article / _PRE_SEEDED_FOLDER
    if not pre_seeded_root.exists():
        return  # nothing to pre-seed for this article

    gf_path = base_dir / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE
    if not gf_path.exists():
        logger.warning(f"  Pre-seed: {GUIDELINES_FILENAMES_FILE} not found for {article}, skipping")
        return

    gf_data: dict = json.loads(gf_path.read_text(encoding="utf-8"))
    urls_purged: list[str] = []

    for sub_name, json_keys in _PRE_SEEDED_SUBFOLDER_KEYS.items():
        src_sub = pre_seeded_root / sub_name
        if not src_sub.exists():
            continue
        dst_sub = base_dir / RESEARCH_OUTPUT_FOLDER / sub_name
        dst_sub.mkdir(parents=True, exist_ok=True)

        for md_file in sorted(src_sub.glob("*.md")):
            content = md_file.read_text(encoding="utf-8")
            # Extract the source URL so we can remove it from the scrape queue
            m = _SOURCE_URL_RE.search(content)
            if m:
                url = m.group(1).rstrip("/")
                for key in json_keys:
                    gf_data[key] = [
                        u for u in gf_data.get(key, []) if u.rstrip("/") != url
                    ]
                urls_purged.append(url)
            dst = dst_sub / md_file.name
            shutil.copy2(md_file, dst)
            logger.info(f"  Pre-seed: copied {md_file.name} → {sub_name}/")

    if urls_purged:
        gf_path.write_text(json.dumps(gf_data, indent=2, ensure_ascii=False), encoding="utf-8")
        logger.info(f"  Pre-seed: removed {len(urls_purged)} URL(s) from {GUIDELINES_FILENAMES_FILE}")


def _create_migration_sentinels(base_dir: Path) -> None:
    """Retroactively create step and round sentinels for bases built before
    sentinel support was introduced."""
    research_dir = base_dir / RESEARCH_OUTPUT_FOLDER
    if not research_dir.exists():
        return

    # Step 1 sentinel — guidelines_filenames.json exists
    if (research_dir / GUIDELINES_FILENAMES_FILE).exists():
        s = research_dir / "_step1.done"
        if not s.exists():
            s.touch()
            logger.info(f"  Migration: created step1 sentinel for {base_dir.name}")

    # Step 2 sentinel — at least one .md file scraped in either golden folder
    _golden = research_dir / URLS_FROM_GUIDELINES_FOLDER
    _exploit = research_dir / URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER
    _step2_done = (
        (_golden.exists() and any(_golden.glob("*.md")))
        or (_exploit.exists() and any(_exploit.glob("*.md")))
    )
    if _step2_done:
        s = research_dir / "_step2.done"
        if not s.exists():
            s.touch()
            logger.info(f"  Migration: created step2 sentinel for {base_dir.name}")

    # Exploitation-round sentinels — infer from query count in full_queries.md
    full_q = research_dir / "full_queries.md"
    if not full_q.exists():
        return
    try:
        content = full_q.read_text(encoding="utf-8")
    except Exception:
        return
    n_queries = content.count("[Exploitation]")
    # Each round produces up to N_EXPLOITATION_QUERIES_PER_ROUND queries before
    # dedup; use floor(count / 4) as a conservative lower-bound for done rounds.
    n_done = min(n_queries // 4, N_EXPLOITATION_ROUNDS)
    for i in range(1, n_done + 1):
        sentinel = research_dir / f"_exploit_round_{i}.done"
        if not sentinel.exists():
            sentinel.touch()
            logger.info(
                f"  Migration: created exploitation round-{i} sentinel for {base_dir.name}"
            )


# ---------------------------------------------------------------------------
# Pipeline stages
# ---------------------------------------------------------------------------

async def run_step1_setup(research_dir: str) -> None:
    """Step 1 — extract guideline URLs."""
    logger.info("  Step 1: Extracting guideline URLs …")
    result = extract_guidelines_urls_tool(research_dir)
    logger.info(f"    → {result.get('message', 'done')[:120]}")


async def run_step2_golden_sources(research_dir: str) -> None:
    """Step 2 — scrape golden + exploitation sources (parallel sub-steps)."""
    logger.info("  Step 2: Scraping golden & exploitation sources (parallel) …")
    results = await asyncio.gather(
        # 2.1 local files (sync — run in thread to avoid blocking the loop)
        asyncio.to_thread(process_local_files_tool, research_dir),
        # 2.2 golden other URLs
        scrape_and_clean_other_urls_tool(research_dir),
        # 2.3 golden GitHub URLs
        process_github_urls_tool(research_dir),
        # 2.4 golden YouTube URLs
        transcribe_youtube_videos_tool(research_dir),
        # 2.5 exploitation guideline URLs
        scrape_exploitation_guideline_urls_tool(research_dir),
        return_exceptions=True,
    )
    for i, r in enumerate(results):
        step_label = ["2.1 local", "2.2 other", "2.3 github", "2.4 youtube", "2.5 exploitation"][i]
        if isinstance(r, BaseException):
            logger.error(f"    ✗ Step {step_label} failed: {r}")
        else:
            logger.info(f"    ✓ Step {step_label}: {str(r.get('message', ''))[:100]}")


async def run_step3_exploitation(research_dir: str) -> None:
    """Step 3 — 3 rounds of exploitation queries + Tavily search."""
    logger.info("  Step 3: Exploitation phase (3 rounds) …")
    _rdir = Path(research_dir) / RESEARCH_OUTPUT_FOLDER
    for round_idx in range(1, N_EXPLOITATION_ROUNDS + 1):
        sentinel = _rdir / f"_exploit_round_{round_idx}.done"
        if sentinel.exists():
            logger.info(f"    Round {round_idx}/{N_EXPLOITATION_ROUNDS} already done, skipping …")
            continue

        logger.info(f"    Round {round_idx}/{N_EXPLOITATION_ROUNDS}")

        # 3.1 generate queries — retry up to 3 times on transient None / LLM errors
        query_gen_ok = False
        for attempt in range(1, 4):
            try:
                await generate_next_queries_tool(
                    research_dir, n_queries=N_EXPLOITATION_QUERIES_PER_ROUND
                )
                query_gen_ok = True
                break
            except Exception as exc:
                if attempt < 3:
                    logger.warning(
                        f"      generate_next_queries_tool attempt {attempt}/3 failed: "
                        f"{exc!r} — retrying in 5 s …"
                    )
                    await asyncio.sleep(5)
                else:
                    logger.error(
                        f"      generate_next_queries_tool failed after 3 attempts: "
                        f"{exc!r} — round {round_idx} will retry on next run"
                    )

        if not query_gen_ok:
            continue  # leave sentinel unwritten so this round reruns next time

        # 3.2 deduplicate
        await deduplicate_new_queries_tool(research_dir, query_source="exploitation")

        # 3.3 run Tavily
        queries = _extract_query_strings(research_dir)
        if queries:
            await run_tavily_research_tool(research_dir, queries, query_source="exploitation")
            logger.info(f"      → {len(queries)} queries executed")
        else:
            logger.warning("      → No queries after dedup, skipping Tavily")

        sentinel.touch()
        logger.info(f"    Round {round_idx} sentinel written.")


async def run_step4_exploration(research_dir: str, preset: ExplorationPreset) -> None:
    """Step 4 — exploration phase per preset."""
    if preset.n_rounds == 0:
        logger.info("  Step 4: Exploration skipped (preset 0)")
        return

    logger.info(f"  Step 4: Exploration ({preset.n_rounds} rounds, {preset.label}) …")
    _rdir = Path(research_dir) / RESEARCH_OUTPUT_FOLDER
    for round_idx, focus in enumerate(preset.focus_sequence, 1):
        sentinel = _rdir / f"_explore_round_{round_idx}.done"
        if sentinel.exists():
            logger.info(f"    Exploration round {round_idx}/{preset.n_rounds} already done, skipping …")
            continue

        logger.info(f"    Exploration round {round_idx}/{preset.n_rounds} (focus={focus})")

        # 4.1 generate complementary queries — retry up to 3 times on transient errors
        query_gen_ok = False
        for attempt in range(1, 4):
            try:
                await generate_next_complementary_queries_tool(
                    research_dir,
                    n_queries=settings.n_exploration_queries_per_round,
                    focus=focus,
                )
                query_gen_ok = True
                break
            except Exception as exc:
                if attempt < 3:
                    logger.warning(
                        f"      generate_next_complementary_queries_tool attempt {attempt}/3 "
                        f"failed: {exc!r} — retrying in 5 s …"
                    )
                    await asyncio.sleep(5)
                else:
                    logger.error(
                        f"      generate_next_complementary_queries_tool failed after 3 attempts: "
                        f"{exc!r} — round {round_idx} will retry on next run"
                    )

        if not query_gen_ok:
            continue  # leave sentinel unwritten so this round reruns next time

        # 4.2 deduplicate
        await deduplicate_new_queries_tool(research_dir, query_source="complementary")

        # 4.3 run Tavily
        queries = _extract_query_strings(research_dir)
        if queries:
            await run_tavily_research_tool(research_dir, queries, query_source="complementary")
            logger.info(f"      → {len(queries)} queries executed")
        else:
            logger.warning("      → No queries after dedup, skipping Tavily")

        sentinel.touch()
        logger.info(f"    Exploration round {round_idx} sentinel written.")


async def run_steps5_to_7(research_dir: str) -> None:
    """Steps 5-7: filter sources, select & scrape top sources, create research.md."""
    _rdir = Path(research_dir) / RESEARCH_OUTPUT_FOLDER

    # Step 5 — filter Tavily results by quality
    if (_rdir / "_step5.done").exists():
        logger.info("  Step 5 already done, skipping …")
    else:
        logger.info("  Step 5: Filtering Tavily results …")
        await select_research_sources_to_keep_tool(research_dir)
        (_rdir / "_step5.done").touch()

    # Step 6 — select and scrape top sources
    if (_rdir / "_step6.done").exists():
        logger.info("  Step 6 already done, skipping …")
    else:
        logger.info("  Step 6: Selecting & scraping top research sources …")
        await select_research_sources_to_scrape_tool(
            research_dir, max_sources=settings.maximum_sources_to_scrape
        )
        await scrape_research_urls_tool(research_dir, concurrency_limit=2)
        (_rdir / "_step6.done").touch()

    # Step 7 — create final research.md (sentinel is research.md itself)
    if (Path(research_dir) / "research.md").exists():
        logger.info("  Step 7 already done (research.md exists), skipping …")
    else:
        logger.info("  Step 7: Creating research.md …")
        result = create_research_file_tool(research_dir)
        logger.info(f"    → {result.get('message', 'done')[:120]}")


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

async def build_exploitation_base(article: str) -> Path:
    """
    Build the shared exploitation base for one article.

    Returns the path to the base directory (ready to be copied per preset).
    """
    src_guideline = _EVAL_DATASET_DIR / article / ARTICLE_GUIDELINE_FILE
    if not src_guideline.exists():
        raise FileNotFoundError(f"Guideline not found: {src_guideline}")

    base_dir = BASES_DIR / article
    base_dir.mkdir(parents=True, exist_ok=True)

    # Copy article_guideline.md into the base directory
    dst_guideline = base_dir / ARTICLE_GUIDELINE_FILE
    if not dst_guideline.exists():
        shutil.copy2(src_guideline, dst_guideline)

    research_dir = str(base_dir)

    logger.info(f"Building exploitation base: {article}")
    t0 = time.monotonic()
    _rdir = base_dir / RESEARCH_OUTPUT_FOLDER
    _rdir.mkdir(parents=True, exist_ok=True)

    if (_rdir / "_step1.done").exists():
        logger.info("  Step 1 already done, skipping …")
    else:
        await run_step1_setup(research_dir)
        _apply_pre_seeded_content(article, base_dir)
        (_rdir / "_step1.done").touch()

    if (_rdir / "_step2.done").exists():
        logger.info("  Step 2 already done, skipping …")
    else:
        await run_step2_golden_sources(research_dir)
        (_rdir / "_step2.done").touch()

    await run_step3_exploitation(research_dir)

    elapsed = time.monotonic() - t0
    logger.info(f"  Base complete for {article} in {elapsed:.0f}s")
    return base_dir


async def run_episode(article: str, preset: ExplorationPreset) -> Path:
    """
    Run one episode: copy exploitation base → exploration → post-processing.

    Returns path to the episode directory containing the final research.md.
    """
    ep_name = _episode_dir_name(article, preset)
    episode_dir = EPISODES_DIR / ep_name
    base_dir = BASES_DIR / article

    if not base_dir.exists():
        raise FileNotFoundError(f"Exploitation base missing: {base_dir}")

    logger.info(f"Episode: {ep_name}")
    t0 = time.monotonic()

    # Copy the shared exploitation base
    _copy_base_to_episode(base_dir, episode_dir)

    research_dir = str(episode_dir)

    # Run exploration
    await run_step4_exploration(research_dir, preset)

    # Run post-exploration steps
    await run_steps5_to_7(research_dir)

    elapsed = time.monotonic() - t0
    logger.info(f"  Episode {ep_name} complete in {elapsed:.0f}s")
    return episode_dir


async def run_pipeline(
    articles: Sequence[str] | None = None,
    preset_ids: Sequence[int] | None = None,
    dry_run: bool = False,
) -> None:
    """
    Run the full Phase 1 data generation pipeline.

    Args:
        articles: Which articles to process (default: all 5 train articles)
        preset_ids: Which presets to run (default: all 6)
        dry_run: If True, only print the plan without executing
    """
    arts = list(articles or TRAIN_ARTICLES)
    pids = set(preset_ids or [p.id for p in PRESETS])
    selected_presets = [p for p in PRESETS if p.id in pids]

    total_episodes = len(arts) * len(selected_presets)

    logger.info("=" * 70)
    logger.info("Phase 1: RL Research Data Generation")
    logger.info(f"  Articles:  {arts}")
    logger.info(f"  Presets:   {[p.id for p in selected_presets]}")
    logger.info(f"  Episodes:  {total_episodes}")
    logger.info(f"  Output:    {_OUTPUT_ROOT}")
    logger.info("=" * 70)

    if dry_run:
        logger.info("DRY RUN — plan only, no execution.")
        for art in arts:
            logger.info(f"\n  Base: {art}")
            for preset in selected_presets:
                logger.info(f"    Episode: {_episode_dir_name(art, preset)}  "
                            f"(rounds={preset.n_rounds}, focus={preset.focus_sequence})")
        return

    _OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    BASES_DIR.mkdir(parents=True, exist_ok=True)
    EPISODES_DIR.mkdir(parents=True, exist_ok=True)

    pipeline_t0 = time.monotonic()

    # Stage 1 — build exploitation bases (sequential per article)
    for art in arts:
        base_dir = BASES_DIR / art
        # Migrate bases built before sentinel support was introduced
        _create_migration_sentinels(base_dir)
        _all_rounds_done = all(
            (base_dir / RESEARCH_OUTPUT_FOLDER / f"_exploit_round_{i}.done").exists()
            for i in range(1, N_EXPLOITATION_ROUNDS + 1)
        )
        if _all_rounds_done:
            logger.info(f"Exploitation base already complete for {art}, skipping …")
        else:
            await build_exploitation_base(art)

    # Stage 2 — run episodes (sequential to stay within API limits)
    completed = 0
    for art in arts:
        for preset in selected_presets:
            ep_name = _episode_dir_name(art, preset)
            ep_dir = EPISODES_DIR / ep_name
            research_md = ep_dir / "research.md"
            if research_md.exists():
                logger.info(f"Episode {ep_name} already complete, skipping …")
                completed += 1
                continue
            await run_episode(art, preset)
            completed += 1
            logger.info(f"Progress: {completed}/{total_episodes} episodes done")

    pipeline_elapsed = time.monotonic() - pipeline_t0
    logger.info("=" * 70)
    logger.info(f"Pipeline complete — {total_episodes} episodes in {pipeline_elapsed:.0f}s")
    logger.info(f"Output: {_OUTPUT_ROOT}")
    logger.info("=" * 70)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 1: Generate research.md files for RL training data",
    )
    parser.add_argument(
        "--articles", nargs="+", default=None,
        help=f"Article folder names to process (default: all 5 train articles)",
    )
    parser.add_argument(
        "--presets", nargs="+", type=int, default=None,
        help="Preset IDs to run (0-5, default: all 6)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show execution plan without running",
    )
    args = parser.parse_args()

    asyncio.run(run_pipeline(
        articles=args.articles,
        preset_ids=args.presets,
        dry_run=args.dry_run,
    ))


if __name__ == "__main__":
    main()
