"""Deduplicate new queries against full history – designed for 3 fixed exploitation rounds + RL complementary rounds."""


import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple, Literal

from ..app.dedup_new_queries_handler import (
    deduplicate_new_queries_against_history,
    parse_queries_from_file,
)
from ..app.generate_queries_handler import(
    append_generated_queries_with_reasons,
    compute_next_query_id,
)

from .generate_next_queries_tool import write_queries_to_file
from ..utils.file_utils import validate_research_folder
from ..config.settings import settings
from ..config.constants import (
    FULL_QUERIES_FILE,
    NEXT_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)

logger = logging.getLogger(__name__)

async def deduplicate_new_queries_tool(
    research_directory: str,
    query_source: Literal["exploitation", "complementary"] = "exploitation",
) -> Dict[str, Any]:
    """
    Runs after every query generation round (exploitation or complementary).
    Deduplicates the new batch against FULL_QUERIES_FILE history.
    Writes clean next_queries.md for run_tavily_research.

    Args:
        research_directory: Path to the research directory containing the output subdirectory with next_queries.md and full_queries.md
        query_source: Origin of the current query batch, one of "exploitation" or "complementary" (default: "exploitation")

    Returns:
        Dict[str, Any]: Dictionary containing:
            - status: Operation status ("success" or "skipped")
            - new_queries_count: Total number of queries in the incoming batch
            - kept_count: Number of queries retained after deduplication
            - removed_duplicates: Number of queries dropped as duplicates
            - output_path: Path to the rewritten next_queries.md file
            - message: Human-readable summary of the operation
    """
    research_path = Path(research_directory)
    output_path = research_path / RESEARCH_OUTPUT_FOLDER

    validate_research_folder(research_path)
    output_path.mkdir(parents=True, exist_ok=True)

    next_queries_path = output_path / NEXT_QUERIES_FILE

    full_queries_path = output_path / FULL_QUERIES_FILE

    new_queries = parse_queries_from_file(next_queries_path)

    if not new_queries:
        return {"status": "skipped", "message": "No new queries found."}

    deduplicated = await deduplicate_new_queries_against_history(new_queries, full_queries_path, query_source)

    # Write clean file for Tavily (overwrite)
    write_queries_to_file(next_queries_path, deduplicated)

    # Append all generated queries with reasons to full_queries.md
    append_generated_queries_with_reasons(
            full_queries_path,
            deduplicated,
            starting_id=compute_next_query_id(full_queries_path),
            query_source=query_source,
    )

    removed_count = len(new_queries) - len(deduplicated)

    message = (
        f"✅ Deduplicated {query_source} queries against full history.\n"
        f"Kept: {len(deduplicated)} | Removed: {removed_count}\n"
        f"Ready for Tavily: {next_queries_path.relative_to(research_path)}"
    )

    return {
        "status": "success",
        "new_queries_count": len(new_queries),
        "kept_count": len(deduplicated),
        "removed_duplicates": removed_count,
        "output_path": str(next_queries_path.resolve()),
        "message": message,
    }