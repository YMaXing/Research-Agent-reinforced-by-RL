"""Deduplicate new queries against full history – designed for 3 fixed exploitation rounds + RL complementary rounds."""


import logging
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple, Literal

from ..app.dedup_new_queries_handler import (
    DeduplicationResult,
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
    REJECTED_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)

logger = logging.getLogger(__name__)


def _append_rejected_queries(
    rejected_path: Path,
    rejected: List[Tuple[str, str]],
    reasoning: str,
    query_source: str,
) -> None:
    """Append a section for this dedup round's rejected queries to rejected_queries.md."""
    timestamp = datetime.now().isoformat(timespec="seconds")
    lines = [f"\n## [{query_source.capitalize()}] — {timestamp}\n\n"]
    if reasoning:
        lines.append(f"Dedup reasoning: {reasoning}\n\n")
    for i, (query, original_reason) in enumerate(rejected, 1):
        lines.append(f"{i}. {query}\n   Original reason: {original_reason}\n\n")
    lines.append("-----\n")
    with rejected_path.open("a", encoding="utf-8") as f:
        f.write("".join(lines))

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

    dedup_result = await deduplicate_new_queries_against_history(new_queries, full_queries_path, query_source)

    # Write clean file for Tavily (overwrite)
    write_queries_to_file(next_queries_path, dedup_result.kept)

    # Append all generated queries with reasons to full_queries.md
    append_generated_queries_with_reasons(
            full_queries_path,
            dedup_result.kept,
            starting_id=compute_next_query_id(full_queries_path),
            query_source=query_source,
    )

    # Persist rejected queries for inspection
    if dedup_result.rejected:
        _append_rejected_queries(
            output_path / REJECTED_QUERIES_FILE,
            dedup_result.rejected,
            dedup_result.reasoning,
            query_source,
        )

    removed_count = len(new_queries) - len(dedup_result.kept)

    message = (
        f"✅ Deduplicated {query_source} queries against full history.\n"
        f"Kept: {len(dedup_result.kept)} | Removed: {removed_count}\n"
        f"Ready for Tavily: {next_queries_path.relative_to(research_path)}"
    )

    return {
        "status": "success",
        "new_queries_count": len(new_queries),
        "kept_count": len(dedup_result.kept),
        "removed_duplicates": removed_count,
        "output_path": str(next_queries_path.resolve()),
        "message": message,
    }