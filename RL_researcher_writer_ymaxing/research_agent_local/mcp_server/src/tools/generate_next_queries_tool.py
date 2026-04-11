"""Query generation tool implementation."""

import logging
from pathlib import Path
from typing import Any, Dict, List, Tuple, Literal

from ..app.generate_queries_handler import (
    generate_complementary_queries_with_reasons,
    generate_queries_with_reasons,
)
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    LOCAL_FILES_FROM_RESEARCH_FOLDER,
    MARKDOWN_EXTENSION,
    NEXT_QUERIES_FILE,
    FULL_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    URLS_FROM_GUIDELINES_FOLDER,
)
from ..utils.file_utils import read_file_safe, validate_research_folder

logger = logging.getLogger(__name__)


def write_queries_to_file(next_q_path: Path, queries_and_reasons: List[Tuple[str, str]]) -> None:
    """
    Write the generated queries and reasons to a markdown file.

    Args:
        next_q_path: Path to the output file
        queries_and_reasons: List of tuples containing (query, reason) pairs
    """
    with next_q_path.open("w", encoding="utf-8") as f:
        f.write("### Candidate Web-Search Queries\n\n")
        for idx, (query, reason) in enumerate(queries_and_reasons, 1):
            f.write(f"{idx}. {query}\n")
            f.write(f"Reason: {reason}\n\n")


def format_queries_for_display(queries_and_reasons: List[Tuple[str, str]]) -> str:
    """
    Format the queries and reasons for display in the response message.

    Args:
        queries_and_reasons: List of tuples containing (query, reason) pairs

    Returns:
        Formatted string with all queries and reasons
    """
    formatted_queries = []
    for idx, (query, reason) in enumerate(queries_and_reasons, 1):
        formatted_queries.append(f"{idx}. {query}\nReason: {reason}")

    return "\n\n".join(formatted_queries)


async def generate_next_queries_tool(research_directory: str, n_queries: int = 5) -> Dict[str, Any]:
    """
    Generate candidate web-search queries for the next research round.

    Analyzes the article guidelines, already-scraped content, and existing Tavily
    results to identify knowledge gaps and propose new web-search questions.
    Each query includes a rationale explaining why it's important for the article.
    Results are saved to next_queries.md in the research directory.

    Args:
        research_directory: Path to the research directory containing article data
        n_queries: Number of queries to generate (default: 5)

    Returns:
        Dict with status, generated queries, and output file path
    """
    logger.debug(f"Generating candidate web-search queries for {research_directory}")

    # Convert to Path object
    research_path = Path(research_directory)
    research_output_path = research_path / RESEARCH_OUTPUT_FOLDER

    # Validate folders and files
    validate_research_folder(research_path)

    # Create RESEARCH_OUTPUT_FOLDER directory if it doesn't exist
    research_output_path.mkdir(parents=True, exist_ok=True)

    # Gather context from the research folder
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    results_path = research_output_path / TAVILY_RESULTS_FILE
    urls_from_guidelines_dir = research_output_path / URLS_FROM_GUIDELINES_FOLDER
    full_queries_path = research_output_path / FULL_QUERIES_FILE

    article_guidelines = read_file_safe(guidelines_path)
    past_research = read_file_safe(results_path)
    full_queries = read_file_safe(full_queries_path)

    scraped_ctx_parts: List[str] = []
    if urls_from_guidelines_dir.exists():
        for md_file in sorted(urls_from_guidelines_dir.glob(f"*{MARKDOWN_EXTENSION}")):
            scraped_ctx_parts.append(md_file.read_text(encoding="utf-8"))

    local_files_dir = research_output_path / LOCAL_FILES_FROM_RESEARCH_FOLDER
    if local_files_dir.exists():
        for md_file in sorted(local_files_dir.glob(f"*{MARKDOWN_EXTENSION}")):
            scraped_ctx_parts.append(md_file.read_text(encoding="utf-8"))

    scraped_ctx_str = "\n\n".join(scraped_ctx_parts)

    if not article_guidelines:
        logger.warning(f"⚠️  Article guidelines not found at {guidelines_path}. Proceeding anyway.")

    queries_and_reasons = await generate_queries_with_reasons(
        article_guidelines, past_research, full_queries, scraped_ctx_str, n_queries=n_queries
    )

    # Write to next_queries.md (overwrite)
    next_q_path = research_output_path / NEXT_QUERIES_FILE

    # Write queries to file
    write_queries_to_file(next_q_path, queries_and_reasons)

    # Create the formatted queries string for display
    queries_string = format_queries_for_display(queries_and_reasons)

    return {
        "status": "success",
        "queries_count": len(queries_and_reasons),
        "queries": queries_and_reasons,
        "output_path": str(next_q_path.resolve()),
        "message": (
            f"Successfully generated {len(queries_and_reasons)} candidate queries for research folder "
            f"'{research_directory}'. Queries and reasons saved to: "
            f"{next_q_path.relative_to(research_path)}\n\nGenerated Queries:\n\n{queries_string}"
        ),
    }


async def generate_next_complementary_queries_tool(research_directory: str,
                                                   n_queries: int = 5,
                                                   depth_vs_breadth_ratio: float = 0.5,
                                                   focus: Literal["balanced", "depth", "breadth"] = "balanced") -> Dict[str, Any]:
        """
        Generate complementary candidate web-search queries to explore uncovered but closely relevant aspects.

        Analyzes the article guidelines, already-scraped content, and existing Tavily results 
        to dive deeper into the content already covered in past research, and/or explore other uncovered aspects 
        that are closely related to past research and may expand the research scope, then propose new web-search questions.
        Each query includes a rationale explaining why it's important and what additional value it brings for the article.
        Results are saved to next_queries.md in the research directory.

        Args:
            research_directory: Path to the research directory containing article data
            n_queries: Number of queries to generate (default: 4)
            focus: Query focus mode — "depth" (all depth), "breadth" (all breadth), or "balanced" (50/50)

        Returns:
            Dict[str, Any]: Dictionary containing:
                - status: Operation status ("success")
                - queries_generated: List of generated query dictionaries with 'query' and 'rationale' keys
                - queries_count: Number of queries generated
                - output_path: Path to the generated next_queries.md file
                - message: Human-readable success message with generation results
        """
        logger.debug(f"Generating complementary queries for {research_directory} (focus={focus})")

        # Convert to Path object
        research_path = Path(research_directory)
        research_output_path = research_path / RESEARCH_OUTPUT_FOLDER

        # Validate folders and files
        validate_research_folder(research_path)

        # Create RESEARCH_OUTPUT_FOLDER directory if it doesn't exist
        research_output_path.mkdir(parents=True, exist_ok=True)

        # Gather context from the research folder
        guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
        results_path = research_output_path / TAVILY_RESULTS_FILE
        urls_from_guidelines_dir = research_output_path / URLS_FROM_GUIDELINES_FOLDER
        full_queries_path = research_output_path / FULL_QUERIES_FILE

        article_guidelines = read_file_safe(guidelines_path)
        past_research = read_file_safe(results_path)
        full_queries = read_file_safe(full_queries_path)

        scraped_ctx_parts: List[str] = []
        if urls_from_guidelines_dir.exists():
            for md_file in sorted(urls_from_guidelines_dir.glob(f"*{MARKDOWN_EXTENSION}")):
                scraped_ctx_parts.append(md_file.read_text(encoding="utf-8"))

        local_files_dir = research_output_path / LOCAL_FILES_FROM_RESEARCH_FOLDER
        if local_files_dir.exists():
            for md_file in sorted(local_files_dir.glob(f"*{MARKDOWN_EXTENSION}")):
                scraped_ctx_parts.append(md_file.read_text(encoding="utf-8"))

        scraped_ctx_str = "\n\n".join(scraped_ctx_parts)

        if not article_guidelines:
            logger.warning(f"⚠️  Article guidelines not found at {guidelines_path}. Proceeding anyway.")

        # === Resolve effective ratio based on focus knob ===
        if focus == "depth":
            effective_ratio = 0.80
        elif focus == "breadth":
            effective_ratio = 0.20
        else:  # balanced — honour provided ratio, clamped to [0, 1]
            effective_ratio = max(0.0, min(1.0, depth_vs_breadth_ratio))
        
        queries_and_reasons = await generate_complementary_queries_with_reasons(
            article_guidelines, past_research, full_queries, scraped_ctx_str, n_queries=n_queries, depth_vs_breadth_ratio=effective_ratio
        )

        # Write to next_queries.md (overwrite)
        next_q_path = research_output_path / NEXT_QUERIES_FILE
        
        # Write queries to file
        write_queries_to_file(next_q_path, queries_and_reasons)

        # Create the formatted queries string for display
        queries_string = format_queries_for_display(queries_and_reasons)

        return {
            "status": "success",
            "queries_count": len(queries_and_reasons),
            "queries": queries_and_reasons,
            "output_path": str(next_q_path.resolve()),
            "message": (
                f"Successfully generated {len(queries_and_reasons)} complementary candidate queries for research folder "
                f"'{research_directory}'. Queries and reasons saved to: "
                f"{next_q_path.relative_to(research_path)}\n\nGenerated Queries:\n\n{queries_string}"
            ),
        }