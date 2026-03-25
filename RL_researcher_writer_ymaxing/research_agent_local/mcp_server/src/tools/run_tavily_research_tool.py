"""Tavily research tool implementation."""

import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, List, Literal, Tuple

from ..app.tavily_handler import (
    run_tavily_search,
    compute_next_source_id,
    append_tavily_results,
)

from ..config.constants import (
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
)
from ..utils.file_utils import validate_research_folder

logger = logging.getLogger(__name__)

_PHASE_LABELS: Dict[str, str] = {
    "exploitation": "[EXPLOITATION]",
    "complementary": "[EXPLORATION]",
}


def append_search_results_to_file(
    results_path: Path,
    queries: List[str],
    search_results: List[Tuple],
    phase: str = "[EXPLOITATION]",
) -> int:
    """
    Process search results and append them to the results file.

    Args:
        results_path: Path to the results file
        queries: List of search queries
        search_results: List of search results from run_tavily_search
        phase: Phase label to tag each source ("[EXPLOITATION]" or "[EXPLORATION]")

    Returns:
        Total number of sources added
    """
    next_global_id = compute_next_source_id(results_path)
    total_sources = 0

    for query, (_, answer_by_source, citations) in zip(queries, search_results):
        if citations:
            next_global_id = append_tavily_results(
                results_path,
                query,
                answer_by_source,
                citations,
                next_global_id,
                phase=phase,
            )
            total_sources += len(citations)
            logger.debug(f"Appended results for query: '{query}' (added {len(citations)} source section(s)).")

    return total_sources


async def run_tavily_research_tool(
    research_directory: str,
    queries: List[str],
    query_source: Literal["exploitation", "complementary"] = "exploitation",
) -> Dict[str, Any]:
    """
    Run Tavily research queries for the research folder.

    Executes the provided queries using Tavily and appends
    the results to tavily_results.md in the research directory. Each query
    result includes the answer and source citations tagged with the research phase
    ("[EXPLOITATION]" for core queries, "[EXPLORATION]" for complementary queries).

    Args:
        research_directory: Path to the research directory where results will be saved
        queries: List of web-search queries to execute
        query_source: Origin of queries - "exploitation" (default) or "complementary".
            Controls the Phase tag written to tavily_results.md.

    Returns:
        Dict with status, processing results, and file paths
    """
    logger.debug(f"Running Tavily research for directory: {research_directory}")

    # Convert to Path object
    research_path = Path(research_directory)
    research_path = research_path / RESEARCH_OUTPUT_FOLDER

    # Validate folders and files
    validate_research_folder(research_path)

    if not queries:
        return {
            "status": "success",
            "message": f"No queries provided for research folder '{research_directory}' - nothing to do.",
            "queries_processed": 0,
            "sources_added": 0,
            "queries": queries,
        }

    results_path = research_path / TAVILY_RESULTS_FILE

    # Ensure output file exists
    results_path.touch(exist_ok=True)

    phase = _PHASE_LABELS.get(query_source, "Exploitation")
    logger.debug(f"Executing {len(queries)} Tavily queries (phase={phase})...")
    tasks = [run_tavily_search(query) for query in queries]
    search_results = await asyncio.gather(*tasks)
    logger.debug("All Tavily queries finished. Appending results.")

    # Process and append search results to file
    total_sources = append_search_results_to_file(results_path, queries, search_results, phase=phase)

    processed_queries_count = len(queries)
    return {
        "status": "success",
        "queries_processed": processed_queries_count,
        "sources_added": total_sources,
        "output_path": str(results_path.resolve()),
        "message": (
            f"Successfully completed Tavily research round for research folder '{research_directory}'. "
            f"Processed {processed_queries_count} queries and added {total_sources} "
            f"source sections to {TAVILY_RESULTS_FILE}"
        ),
    }
