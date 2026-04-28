"""
One-shot script — run the two replacement Tavily queries for lesson 06_tools.

Queries 8 and 9 in the original run produced zero results because they were
400-500 char compound essay questions.  This script re-runs Tavily with two
short, focused replacements and appends the results to tavily_results.md.

Usage (from research_agent_local/):
    uv run --project mcp_server python training/run_tavily_06_tools_replacement.py
    uv run --project mcp_server python training/run_tavily_06_tools_replacement.py --dry-run
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Ensure the mcp_server package is importable (mirrors repair_missing_tavily_queries.py)
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_MCP_SERVER_DIR = _THIS_DIR.parent / "mcp_server"
if str(_MCP_SERVER_DIR) not in sys.path:
    sys.path.insert(0, str(_MCP_SERVER_DIR))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(_MCP_SERVER_DIR / ".env", override=False)

from src.tools.run_tavily_research_tool import run_tavily_research_tool  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
_RESEARCH_DIR = str(_THIS_DIR.parent.parent / "rl_training_data" / "bases" / "06_tools")

_REPLACEMENT_QUERIES = [
    "OpenAI function calling vs Anthropic tool use API format comparison",
]


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main(dry_run: bool) -> None:
    if dry_run:
        logger.info("DRY RUN — no API calls will be made.")
        logger.info("Research directory: %s", _RESEARCH_DIR)
        for i, q in enumerate(_REPLACEMENT_QUERIES, 1):
            logger.info("  Query %d (%d chars): %s", i, len(q), q)
        return

    logger.info("Running %d replacement Tavily queries for 06_tools…", len(_REPLACEMENT_QUERIES))
    result = await run_tavily_research_tool(
        _RESEARCH_DIR,
        _REPLACEMENT_QUERIES,
        query_source="exploitation",
    )
    logger.info("Result: %s", result)
    if result["status"] in ("success", "partial"):
        logger.info(
            "✅ Appended %d source section(s) to tavily_results.md  "
            "(queries processed: %d / %d).",
            result["sources_added"],
            result["queries_processed"],
            len(_REPLACEMENT_QUERIES),
        )
    else:
        logger.error("❌ All queries failed — check logs above for details.")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print plan without executing")
    args = parser.parse_args()
    asyncio.run(main(dry_run=args.dry_run))
