"""
Phase 2a — RL Training Data Generator (Writing Generation)

Generates article.md for each episode directory that has research.md (from Phase 1).
Calls the Brown writing workflow directly with a persistent SQLite checkpointer
for maximum mid-workflow resumability.

Resumability layers:
  1. article.md exists → skip episode (zero cost)
  2. SQLite checkpointer + deterministic thread_id → LangGraph @task memoization
     (if process crashes mid-workflow, expensive LLM tasks already completed are
     replayed from cache instead of re-invoked)
  3. Per-episode retry with exponential backoff (3 attempts)
  4. Intermediate article_NNN.md files serve as progress indicators

Usage (from writing_workflow/):
  uv run python rl_writing_generator.py                               # all episodes
  uv run python rl_writing_generator.py --dry-run                    # plan only
  uv run python rl_writing_generator.py --articles 02_workflows_vs_agents
  uv run python rl_writing_generator.py --presets 0 1
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import time
import uuid
from pathlib import Path
from typing import Sequence

from langchain_core.runnables import RunnableConfig

from brown.memory import build_sqlite_checkpointer
from brown.utils.rate_limiter import set_llm_concurrency
from brown.workflows import build_generate_article_workflow

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_writing_generator")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_THIS_DIR = Path(__file__).resolve().parent

# Episode dirs produced by Phase 1
EPISODES_DIR = _THIS_DIR.parent / "rl_training_data" / "episodes"

# Train articles (L2, L3, L5, L6, L8, L9, L11) — must match Phase 1
# L11 is listed before L8 because L8 (08_react_practice) frequently triggers
# LLM 429 rate-limit errors; processing L11 first keeps the pipeline moving.
# L9 (09_RAG) is listed before L6 (06_tools) for the same reason.
TRAIN_ARTICLES: list[str] = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "11_multimodal",
    "08_react_practice",
    "09_RAG",
    "06_tools",
]

N_PRESETS = 6  # preset IDs 0-5
MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 60  # seconds; attempt N waits N * 60s
DEFAULT_CONCURRENCY = 4  # concurrent episodes; Tier 2: 1K RPM / 5M TPM
DEFAULT_LLM_CONCURRENCY = 2  # concurrent LLM API calls; each call can be 100K-500K tokens


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _episode_dir_name(article: str, preset_id: int) -> str:
    """Match the naming convention from Phase 1."""
    return f"{article}__preset{preset_id}"


def _thread_id_for_episode(episode_name: str) -> str:
    """Deterministic thread ID so LangGraph can resume from checkpointed tasks."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"rl-writing/{episode_name}"))


def _checkpoint_db_path(episode_dir: Path) -> Path:
    """Per-episode SQLite DB for LangGraph checkpointing."""
    return episode_dir / ".writing_checkpoints.sqlite"


def _detect_progress(episode_dir: Path) -> str:
    """Inspect intermediate article_NNN.md files to report progress."""
    drafts = sorted(episode_dir.glob("article_[0-9][0-9][0-9].md"))
    if not drafts:
        return "no drafts yet"
    latest = drafts[-1].stem  # e.g. "article_002"
    return f"{len(drafts)} draft(s), latest: {latest}"


# ---------------------------------------------------------------------------
# Core runner
# ---------------------------------------------------------------------------


async def run_episode(episode_dir: Path, episode_name: str) -> bool:
    """Run the writing workflow for a single episode.

    Returns True on success, False on failure.
    """
    article_path = episode_dir / "article.md"
    if article_path.exists():
        logger.info(f"  article.md already exists, skipping: {episode_name}")
        return True

    research_path = episode_dir / "research.md"
    if not research_path.exists():
        logger.warning(f"  No research.md found, skipping: {episode_name}")
        return False

    thread_id = _thread_id_for_episode(episode_name)
    checkpoint_path = _checkpoint_db_path(episode_dir)

    logger.info(f"  Thread ID:      {thread_id}")
    logger.info(f"  Checkpoint DB:  {checkpoint_path}")

    progress = _detect_progress(episode_dir)
    if progress != "no drafts yet":
        logger.info(f"  Resuming from:  {progress}")

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            async with build_sqlite_checkpointer(uri=checkpoint_path) as checkpointer:
                workflow = build_generate_article_workflow(checkpointer=checkpointer)
                config = RunnableConfig(
                    configurable={"thread_id": thread_id},
                )
                await workflow.ainvoke({"dir_path": episode_dir}, config)

            if article_path.exists():
                logger.info(f"  SUCCESS: article.md generated for {episode_name}")
                return True
            else:
                logger.error(f"  Workflow completed but article.md not found: {episode_name}")
                return False

        except Exception:
            logger.exception(f"  Attempt {attempt}/{MAX_RETRIES} failed for {episode_name}")
            if attempt < MAX_RETRIES:
                wait = RETRY_BACKOFF_BASE * attempt
                logger.info(f"  Retrying in {wait}s …")
                await asyncio.sleep(wait)

    logger.error(f"  FAILED after {MAX_RETRIES} attempts: {episode_name}")
    return False


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


async def _bounded_run(
    sem: asyncio.Semaphore,
    ep_dir: Path,
    ep_name: str,
) -> tuple[str, bool]:
    """Run a single episode under the concurrency semaphore."""
    async with sem:
        ok = await run_episode(ep_dir, ep_name)
        return ep_name, ok


async def run_pipeline(
    articles: Sequence[str] | None = None,
    preset_ids: Sequence[int] | None = None,
    dry_run: bool = False,
    max_concurrent: int = DEFAULT_CONCURRENCY,
) -> None:
    """Run the writing pipeline across all requested episodes.

    Args:
        articles: Article folder names (default: all 5 train articles).
        preset_ids: Preset IDs 0-5 (default: all 6).
        dry_run: Print plan without executing.
    """
    arts = list(articles or TRAIN_ARTICLES)
    pids = sorted(set(preset_ids if preset_ids is not None else range(N_PRESETS)))

    # Build ordered episode list
    episodes: list[tuple[str, Path]] = []
    for art in arts:
        for pid in pids:
            ep_name = _episode_dir_name(art, pid)
            ep_dir = EPISODES_DIR / ep_name
            episodes.append((ep_name, ep_dir))

    # Categorise
    ready = [(n, d) for n, d in episodes if d.exists() and (d / "research.md").exists() and not (d / "article.md").exists()]
    done = [(n, d) for n, d in episodes if d.exists() and (d / "article.md").exists()]
    missing = [(n, d) for n, d in episodes if not d.exists() or not (d / "research.md").exists()]

    logger.info("=" * 70)
    logger.info("Phase 2a: RL Writing Data Generation")
    logger.info(f"  Articles:           {arts}")
    logger.info(f"  Presets:            {pids}")
    logger.info(f"  Total episodes:     {len(episodes)}")
    logger.info(f"  Already complete:   {len(done)}")
    logger.info(f"  Ready to generate:  {len(ready)}")
    logger.info(f"  Missing research:   {len(missing)}")
    logger.info(f"  Max concurrent:     {max_concurrent}")
    logger.info(f"  Episodes dir:       {EPISODES_DIR}")
    logger.info("=" * 70)

    if dry_run:
        logger.info("DRY RUN — plan only, no execution.")
        for name, ep_dir in ready:
            progress = _detect_progress(ep_dir)
            logger.info(f"  READY:   {name}  ({progress})")
        for name, _ in done:
            logger.info(f"  DONE:    {name}")
        for name, _ in missing:
            logger.info(f"  NO-RES:  {name}")
        return

    if not ready:
        logger.info("Nothing to do — all episodes complete or missing research.md")
        return

    pipeline_t0 = time.monotonic()
    sem = asyncio.Semaphore(max_concurrent)
    tasks = [_bounded_run(sem, ep_dir, ep_name) for ep_name, ep_dir in ready]

    logger.info(f"Launching {len(tasks)} episode(s) with max_concurrent={max_concurrent} …")
    results: list[tuple[str, bool]] = await asyncio.gather(*tasks)

    succeeded = sum(1 for _, ok in results if ok)
    failed = sum(1 for _, ok in results if not ok)
    elapsed = time.monotonic() - pipeline_t0
    logger.info("=" * 70)
    logger.info(f"Pipeline complete — {succeeded} succeeded, {failed} failed in {elapsed:.0f}s")
    if failed:
        for ep_name, ok in results:
            if not ok:
                logger.warning(f"  FAILED: {ep_name}")
    logger.info("=" * 70)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Phase 2a: Generate article.md files from research.md for RL training data",
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        default=None,
        help="Article folder names to process (default: all 5 train articles)",
    )
    parser.add_argument(
        "--presets",
        nargs="+",
        type=int,
        default=None,
        help="Preset IDs to run (0-5, default: all 6)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show execution plan without running",
    )
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        metavar="N",
        help=f"Max concurrent episodes (default: {DEFAULT_CONCURRENCY}; raise carefully — Gemini RPM limits apply)",
    )
    parser.add_argument(
        "--llm-concurrency",
        type=int,
        default=DEFAULT_LLM_CONCURRENCY,
        metavar="N",
        dest="llm_concurrency",
        help=(
            f"Max concurrent LLM API calls across all episodes (default: {DEFAULT_LLM_CONCURRENCY}). "
            "Each article call consumes 100K-500K input tokens. Lower this if you see 429 quota errors."
        ),
    )
    args = parser.parse_args()

    set_llm_concurrency(args.llm_concurrency)

    asyncio.run(
        run_pipeline(
            articles=args.articles,
            preset_ids=args.presets,
            dry_run=args.dry_run,
            max_concurrent=args.concurrency,
        )
    )


if __name__ == "__main__":
    main()
