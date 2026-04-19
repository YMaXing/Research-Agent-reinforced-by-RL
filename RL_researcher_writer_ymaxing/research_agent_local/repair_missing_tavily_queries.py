"""
Repair script — re-run Tavily for queries that failed due to LLM context overflow.

A query is considered "missing" when it appears in full_queries.md but has no
corresponding source entry in tavily_results.md (because the LLM returned an
empty structured response and the run_tavily_search call returned ({}, {})).

For each such query the script:
  1. Re-runs run_tavily_search (now with include_raw_content=False, so prompts
     are safe).
  2. Appends the new source entries to tavily_results.md  (with correct Phase
     and globally-unique Source IDs).
  3. Appends the same entries to tavily_results_selected.md  (since the
     selection step already ran; the entries would have been accepted had they
     existed, so we include them directly).
  4. Regenerates research.md via create_research_file_tool so the new sources
     appear in the correct <details> block.

Usage (from research_agent_local/):
  uv run --project mcp_server python repair_missing_tavily_queries.py
  uv run --project mcp_server python repair_missing_tavily_queries.py --dry-run
  uv run --project mcp_server python repair_missing_tavily_queries.py --episodes 03_context_engineering__preset3
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

# ---------------------------------------------------------------------------
# Ensure the mcp_server package is importable
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _THIS_DIR / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv  # noqa: E402
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

from src.app.tavily_handler import (  # noqa: E402
    run_tavily_search,
    compute_next_source_id,
    append_tavily_results,
)
from src.config.constants import (  # noqa: E402
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    TAVILY_RESULTS_SELECTED_FILE,
)
from src.tools.create_research_file_tool import create_research_file_tool  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("repair_missing_tavily")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_EPISODES_DIR = (
    _THIS_DIR.parent / "rl_training_data" / "episodes"
)

_PHASE_TAG: dict[str, str] = {
    "Exploitation": "[EXPLOITATION]",
    "Exploration":  "[EXPLORATION]",
}

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------
@dataclass
class MissingQuery:
    text: str
    phase: str          # "[EXPLOITATION]" or "[EXPLORATION]"
    episode_dir: Path   # path to the episode root (not .research/)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_full_queries(fq_path: Path) -> list[tuple[str, str]]:
    """Return [(query_text, phase_tag), ...] from full_queries.md."""
    text = fq_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r"^Query \[\d+\] \[(Exploitation|Exploration)\]: (.+)$",
        re.MULTILINE,
    )
    return [
        (m.group(2).strip(), _PHASE_TAG[m.group(1)])
        for m in pattern.finditer(text)
    ]


def _present_queries(tr_path: Path) -> set[str]:
    """Return the set of query texts that already have results in tavily_results.md."""
    text = tr_path.read_text(encoding="utf-8")
    return set(re.findall(r"^Query: (.+)$", text, re.MULTILINE))


def find_missing_queries(episodes_dir: Path, filter_episodes: list[str] | None = None) -> list[MissingQuery]:
    """Scan all episode dirs and return queries with no Tavily results."""
    missing: list[MissingQuery] = []
    for ep in sorted(episodes_dir.iterdir()):
        if not ep.is_dir():
            continue
        if filter_episodes and ep.name not in filter_episodes:
            continue

        fq = ep / RESEARCH_OUTPUT_FOLDER / "full_queries.md"
        tr = ep / RESEARCH_OUTPUT_FOLDER / TAVILY_RESULTS_FILE
        if not fq.exists() or not tr.exists():
            continue

        all_queries = _parse_full_queries(fq)
        present   = _present_queries(tr)
        for query_text, phase_tag in all_queries:
            if query_text not in present:
                missing.append(MissingQuery(
                    text=query_text,
                    phase=phase_tag,
                    episode_dir=ep,
                ))
    return missing


# ---------------------------------------------------------------------------
# Core repair logic
# ---------------------------------------------------------------------------

async def repair_query(mq: MissingQuery, dry_run: bool) -> bool:
    """
    Re-run Tavily for a single missing query and patch the episode files.
    Returns True if at least one source was appended.
    """
    research_dir = mq.episode_dir / RESEARCH_OUTPUT_FOLDER
    tr_path      = research_dir / TAVILY_RESULTS_FILE
    sel_path     = research_dir / TAVILY_RESULTS_SELECTED_FILE

    logger.info(f"[{mq.episode_dir.name}] Repairing query ({mq.phase}):")
    logger.info(f"  '{mq.text}'")

    if dry_run:
        logger.info("  [DRY-RUN] Would run Tavily and patch files.")
        return False

    # 1. Run Tavily search
    _, answer_by_source, citations = await run_tavily_search(mq.text)

    if not citations:
        logger.warning(
            f"  ⚠️  Tavily returned no sources for this query again. "
            "Skipping file updates."
        )
        return False

    logger.info(f"  ✅ Got {len(citations)} source(s).")

    # 2. Append to tavily_results.md
    next_id = compute_next_source_id(tr_path)
    append_tavily_results(
        tr_path,
        query=mq.text,
        answer_by_source=answer_by_source,
        citations=citations,
        starting_id=next_id,
        phase=mq.phase,
    )
    logger.info(f"  Appended {len(citations)} source(s) to {tr_path.name} (IDs {next_id}–{next_id + len(citations) - 1}).")

    # 3. Append to tavily_results_selected.md (selection step already ran)
    if sel_path.exists():
        sel_next_id = compute_next_source_id(sel_path)
        append_tavily_results(
            sel_path,
            query=mq.text,
            answer_by_source=answer_by_source,
            citations=citations,
            starting_id=sel_next_id,
            phase=mq.phase,
        )
        logger.info(f"  Appended {len(citations)} source(s) to {sel_path.name} (IDs {sel_next_id}–{sel_next_id + len(citations) - 1}).")
    else:
        logger.warning(f"  {sel_path.name} does not exist — skipping selected-file update.")

    return True


async def repair_episode(ep_dir: Path, missing: list[MissingQuery], dry_run: bool) -> None:
    """Repair all missing queries for one episode, then regenerate research.md."""
    any_patched = False
    for mq in missing:
        patched = await repair_query(mq, dry_run)
        any_patched = any_patched or patched

    if any_patched:
        # 4. Regenerate research.md
        logger.info(f"[{ep_dir.name}] Regenerating research.md …")
        result = create_research_file_tool(str(ep_dir))
        if result.get("status") == "success":
            logger.info(f"[{ep_dir.name}] ✅ research.md regenerated.")
        else:
            logger.error(f"[{ep_dir.name}] ❌ research.md regeneration failed: {result}")
    elif not dry_run:
        logger.info(f"[{ep_dir.name}] No sources were added — research.md not touched.")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

async def main(dry_run: bool, filter_episodes: list[str] | None) -> None:
    missing = find_missing_queries(_EPISODES_DIR, filter_episodes)

    if not missing:
        logger.info("✅ No missing queries found across all episodes.")
        return

    # Group by episode for a tidy summary and to batch research.md regeneration
    by_episode: dict[Path, list[MissingQuery]] = {}
    for mq in missing:
        by_episode.setdefault(mq.episode_dir, []).append(mq)

    logger.info(f"Found {len(missing)} missing query/episode pair(s) across {len(by_episode)} episode(s):")
    for ep, queries in by_episode.items():
        for q in queries:
            logger.info(f"  [{ep.name}] {q.phase}  '{q.text[:80]}...'")

    if dry_run:
        logger.info("\n[DRY-RUN] No files will be modified.")

    for ep_dir, queries in by_episode.items():
        await repair_episode(ep_dir, queries, dry_run)

    logger.info("\n✅ Repair run complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Repair missing Tavily query results.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print what would be done without writing any files.",
    )
    parser.add_argument(
        "--episodes", nargs="+", metavar="EPISODE",
        help="Restrict repair to specific episode directory names (e.g. 03_context_engineering__preset3).",
    )
    args = parser.parse_args()
    asyncio.run(main(dry_run=args.dry_run, filter_episodes=args.episodes))
