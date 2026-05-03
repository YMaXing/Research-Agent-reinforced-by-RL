"""
One-shot propagation script for shared missing queries across lesson 6 episodes.

Runs Tavily ONCE per query (using direct fallback — no LLM structuring, since
the queries are too long for the structuring LLM), then appends the results to
every episode that is still missing that query.

Usage (from research_agent_local/):
  uv run --project mcp_server python training/propagate_shared_queries.py
  uv run --project mcp_server python training/propagate_shared_queries.py --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure the mcp_server package is importable
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _THIS_DIR.parent / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv  # noqa: E402
load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

from src.app.tavily_handler import (  # noqa: E402
    compute_next_source_id,
    append_tavily_results,
)
from src.app.generate_queries_handler import _shorten_query_if_needed  # noqa: E402
from src.config.constants import (  # noqa: E402
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    TAVILY_RESULTS_SELECTED_FILE,
)
from src.tools.create_research_file_tool import create_research_file_tool  # noqa: E402
from src.utils.llm_utils import get_tavily_tool  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("propagate_shared_queries")

# ---------------------------------------------------------------------------
# Episode prefix to process
# ---------------------------------------------------------------------------
_EPISODES_DIR = _THIS_DIR.parent.parent / "rl_training_data" / "episodes"
EPISODE_PREFIX = "06_"

# ---------------------------------------------------------------------------
# The two shared missing queries and their phase tag
# ---------------------------------------------------------------------------
SHARED_QUERIES: list[tuple[str, str]] = [
    (
        'Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?',
        "[EXPLOITATION]",
    ),
    (
        "Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?",
        "[EXPLOITATION]",
    ),
]


# ---------------------------------------------------------------------------
# Tavily direct (no LLM structuring)
# ---------------------------------------------------------------------------
async def _fetch_tavily_direct(query: str) -> tuple[dict[int, str], dict[int, str]]:
    """Call Tavily once without LLM structuring. Returns (answer_by_source, citations).

    Uses _shorten_query_if_needed to paraphrase long queries to ≤ _MAX_QUERY_CHARS
    (the same mechanism used during query generation) before calling Tavily.
    The original full query text is used for file storage by the caller.
    """
    search_query = await _shorten_query_if_needed(query)
    if search_query != query:
        logger.info("   Query shortened from %d to %d chars for Tavily API.", len(query), len(search_query))
        logger.info("   Shortened: '%s'", search_query)
    tavily_tool = get_tavily_tool("tavily")
    results = await tavily_tool.ainvoke({"query": search_query})
    if isinstance(results, dict):
        results = results.get("results", [])
    if not isinstance(results, list):
        logger.warning("Unexpected Tavily result type: %s", type(results))
        return {}, {}

    answer_by_source: dict[int, str] = {}
    citations: dict[int, str] = {}
    for i, result in enumerate(results, 1):
        if not isinstance(result, dict):
            continue
        url = result.get("url", "")
        if not url:
            continue
        content = (
            result.get("content") or (result.get("raw_content") or "")[:4000]
        ).strip()
        if not content:
            content = f"(No content extracted for {url})"
        citations[i] = url
        answer_by_source[i] = content

    return answer_by_source, citations


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _present_queries(tr_path: Path) -> set[str]:
    return set(re.findall(r"^Query: (.+)$", tr_path.read_text(encoding="utf-8"), re.MULTILINE))


def _get_episode_dirs() -> list[Path]:
    return sorted(
        ep for ep in _EPISODES_DIR.iterdir()
        if ep.is_dir()
        and ep.name.startswith(EPISODE_PREFIX)
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main(dry_run: bool) -> None:
    episodes = _get_episode_dirs()
    logger.info("Found %d episode dirs with prefix '%s'", len(episodes), EPISODE_PREFIX)

    # Step 1 — fetch Tavily results once per query
    fetched: dict[str, tuple[dict[int, str], dict[int, str]]] = {}
    for query_text, phase in SHARED_QUERIES:
        logger.info("🔍 Fetching Tavily for query (phase=%s):", phase)
        logger.info("   '%s'", query_text[:120] + ("…" if len(query_text) > 120 else ""))
        if dry_run:
            logger.info("   [DRY-RUN] skipping API call.")
            fetched[query_text] = ({1: "(dry-run content)"}, {1: "https://example.com"})
            continue
        answer_by_source, citations = await _fetch_tavily_direct(query_text)
        if not citations:
            logger.error("   ❌ No results returned — skipping this query.")
            fetched[query_text] = ({}, {})
        else:
            logger.info("   ✅ Got %d source(s).", len(citations))
            fetched[query_text] = (answer_by_source, citations)

    # Step 2 — propagate to each episode
    for ep in episodes:
        research_dir = ep / RESEARCH_OUTPUT_FOLDER
        tr_path  = research_dir / TAVILY_RESULTS_FILE
        sel_path = research_dir / TAVILY_RESULTS_SELECTED_FILE

        if not tr_path.exists():
            logger.warning("[%s] tavily_results.md missing — skipping.", ep.name)
            continue

        present = _present_queries(tr_path)
        any_patched = False

        for query_text, phase in SHARED_QUERIES:
            if query_text in present:
                logger.info("[%s] Already present: '%s…' — skipping.", ep.name, query_text[:60])
                continue

            answer_by_source, citations = fetched.get(query_text, ({}, {}))
            if not citations:
                logger.warning("[%s] No Tavily results for query — cannot patch.", ep.name)
                continue

            if dry_run:
                logger.info("[%s] [DRY-RUN] Would append %d source(s) for: '%s…'", ep.name, len(citations), query_text[:60])
                continue

            # Append to tavily_results.md
            next_id = compute_next_source_id(tr_path)
            append_tavily_results(
                tr_path,
                query=query_text,
                answer_by_source=answer_by_source,
                citations=citations,
                starting_id=next_id,
                phase=phase,
            )
            logger.info("[%s] Appended %d source(s) to tavily_results.md (IDs %d–%d).",
                        ep.name, len(citations), next_id, next_id + len(citations) - 1)

            # Append to tavily_results_selected.md if it has prior sources
            sel_has_content = sel_path.exists() and compute_next_source_id(sel_path) > 1
            if sel_has_content:
                sel_next_id = compute_next_source_id(sel_path)
                append_tavily_results(
                    sel_path,
                    query=query_text,
                    answer_by_source=answer_by_source,
                    citations=citations,
                    starting_id=sel_next_id,
                    phase=phase,
                )
                logger.info("[%s] Appended %d source(s) to tavily_results_selected.md (IDs %d–%d).",
                            ep.name, len(citations), sel_next_id, sel_next_id + len(citations) - 1)
            else:
                logger.warning("[%s] tavily_results_selected.md has no prior sources — skipping selected-file update.", ep.name)

            any_patched = True

        if any_patched and not dry_run:
            logger.info("[%s] Regenerating research.md …", ep.name)
            result = create_research_file_tool(str(ep))
            if result.get("status") == "success":
                logger.info("[%s] ✅ research.md regenerated.", ep.name)
            else:
                logger.error("[%s] ❌ research.md regeneration failed: %s", ep.name, result)

    logger.info("✅ Propagation complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Detect only, no file writes.")
    args = parser.parse_args()
    asyncio.run(main(dry_run=args.dry_run))
