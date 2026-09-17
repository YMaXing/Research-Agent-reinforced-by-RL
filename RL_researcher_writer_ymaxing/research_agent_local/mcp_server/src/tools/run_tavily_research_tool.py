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
from ..app.guideline_extractions_handler import load_reference_url_blocklist

from ..config.constants import (
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
)
from ..utils.file_utils import validate_research_folder
from ..utils.url_utils import normalize_url_for_match

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
    blocklist: set[str] | None = None,
) -> int:
    """
    Process search results and append them to the results file.

    Args:
        results_path: Path to the results file
        queries: List of search queries
        search_results: List of search results from run_tavily_search
        phase: Phase label to tag each source ("[EXPLOITATION]" or "[EXPLORATION]")
        blocklist: Optional set of normalised reference-only URLs to skip. Any
            citation whose URL normalises into this set is dropped so that
            locally-supplied sources are never recorded as research sources.

    Returns:
        Total number of sources added
    """
    next_global_id = compute_next_source_id(results_path)
    total_sources = 0
    dropped = 0

    for query, (_, answer_by_source, citations) in zip(queries, search_results):
        if blocklist and citations:
            kept: Dict[int, str] = {}
            for local_id, url in citations.items():
                if normalize_url_for_match(url) in blocklist:
                    dropped += 1
                    continue
                kept[local_id] = url
            citations = kept
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
            logger.info(f"Appended results for query: '{query}' (added {len(citations)} source section(s)).")

    if dropped:
        logger.info(
            f"Skipped {dropped} reference-only source(s) matching the local-file blocklist."
        )

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
    logger.info(f"Running Tavily research for directory: {research_directory}")

    # Load reference-only URL blocklist (local files whose URLs are for reference
    # only) so they are never recorded as research sources in this phase.
    blocklist = load_reference_url_blocklist(research_directory)

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
    logger.info(f"Executing {len(queries)} Tavily queries (phase={phase})...")
    tasks = [run_tavily_search(query) for query in queries]
    raw_results = await asyncio.gather(*tasks, return_exceptions=True)
    logger.info("All Tavily queries finished. Appending results.")

    # Filter out failed queries so the rest of the batch still saves.
    search_results: list = []
    good_queries: list = []
    for query, result in zip(queries, raw_results):
        if isinstance(result, BaseException):
            logger.error(
                f"❌ Tavily query failed (skipped): {query!r} — {result}"
            )
        else:
            good_queries.append(query)
            search_results.append(result)

    if not search_results:
        return {
            "status": "error",
            "message": (
                f"All {len(queries)} Tavily queries failed for research folder "
                f"'{research_directory}'. Last error: {raw_results[-1]}"
            ),
            "queries_processed": 0,
            "sources_added": 0,
            "queries": queries,
        }

    # Process and append search results to file
    total_sources = append_search_results_to_file(
        results_path, good_queries, search_results, phase=phase, blocklist=blocklist
    )

    failed_count = len(queries) - len(good_queries)
    processed_queries_count = len(good_queries)
    status = "partial" if failed_count else "success"
    return {
        "status": status,
        "queries_processed": processed_queries_count,
        "queries_failed": failed_count,
        "sources_added": total_sources,
        "output_path": str(results_path.resolve()),
        "message": (
            f"Completed Tavily research for '{research_directory}'. "
            f"Processed {processed_queries_count}/{len(queries)} queries"
            + (f" ({failed_count} failed — see server logs)" if failed_count else "")
            + f" and added {total_sources} source sections to {TAVILY_RESULTS_FILE}."
        ),
    }
