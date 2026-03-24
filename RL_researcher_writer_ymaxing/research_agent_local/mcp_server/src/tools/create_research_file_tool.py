"""Research file creation tool implementation."""

import logging
from pathlib import Path
from typing import Any, Dict

from ..app.tavily_handler import extract_tavily_chunks, group_tavily_by_query
from ..config.constants import (
    DEDUPLICATED_RESEARCH_FILE,
    RESEARCH_MD_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    TAVILY_RESULTS_SELECTED_FILE,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,
)
from ..utils.file_utils import (
    collect_directory_markdowns,
    collect_directory_markdowns_with_titles,
    read_file_safe,
    validate_research_folder,
)
from ..utils.markdown_utils import build_research_results_section, build_sources_section, combine_research_sections

logger = logging.getLogger(__name__)


def create_research_file_tool(research_directory: str) -> Dict[str, Any]:
    """
    Generate comprehensive research.md file.
    Prefers the deduplicated_research.md (if it exists) for maximum cleanliness.
    Falls back to original multi-section logic otherwise.
    """
    logger.debug(f"Creating research files for directory: {research_directory}")

    article_dir = Path(research_directory)
    research_output_dir = article_dir / RESEARCH_OUTPUT_FOLDER

    validate_research_folder(article_dir)

    dedup_path = research_output_dir / DEDUPLICATED_RESEARCH_FILE

    # === PREFERRED PATH: Use deduplicated content (new workflow) ===
    if dedup_path.exists():
        final_md = read_file_safe(dedup_path)
        # Optional nice wrapper
        final_md = f"# Comprehensive Research Report\n\n{final_md}\n\n---\n\n*Generated with content deduplication enabled.*"

        md_output_path = article_dir / RESEARCH_MD_FILE
        md_output_path.write_text(final_md, encoding="utf-8")

        return {
            "status": "success",
            "markdown_file": str(md_output_path.resolve()),
            "message": f"✅ Generated research markdown from deduplicated content:\n  - {md_output_path.relative_to(article_dir)}",
        }

    # === FALLBACK: Original logic (no deduplication yet) ===
    logger.info("⚠️  No deduplicated_research.md found — falling back to original multi-section assembly.")

    # (All your original code stays exactly the same from here down)
    selected_results_file = research_output_dir / TAVILY_RESULTS_SELECTED_FILE
    original_results_file = research_output_dir / TAVILY_RESULTS_FILE

    urls_from_research_dir = research_output_dir / URLS_FROM_RESEARCH_FOLDER
    code_sources_dir = research_output_dir / URLS_FROM_GUIDELINES_CODE_FOLDER
    additional_sources_dir = research_output_dir / URLS_FROM_GUIDELINES_FOLDER
    youtube_transcripts_dir = research_output_dir / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER

    if selected_results_file.exists():
        results_md = read_file_safe(selected_results_file)
        chunks = extract_tavily_chunks(results_md)
    else:
        results_md = read_file_safe(original_results_file)
        chunks = extract_tavily_chunks(results_md)

    grouped = group_tavily_by_query(chunks, list(chunks.keys()))
    research_results_section = build_research_results_section(grouped)

    scraped_sources = collect_directory_markdowns_with_titles(urls_from_research_dir)
    sources_scraped_section = build_sources_section(
        "## Sources Scraped From Research Results", scraped_sources, "No scraped sources found for research results."
    )

    code_sources = collect_directory_markdowns_with_titles(code_sources_dir)
    code_sources_section = build_sources_section("## Code Sources", code_sources, "No code sources found.")

    youtube_sources = collect_directory_markdowns_with_titles(youtube_transcripts_dir)
    youtube_transcripts_section = build_sources_section(
        "## YouTube Video Transcripts", youtube_sources, "No YouTube video transcripts found."
    )

    additional_sources = collect_directory_markdowns(additional_sources_dir)
    additional_sources_section = build_sources_section(
        "## Additional Sources Scraped", additional_sources, "No additional sources scraped."
    )

    final_md = combine_research_sections(
        research_results_section,
        sources_scraped_section,
        code_sources_section,
        youtube_transcripts_section,
        additional_sources_section,
    )

    md_output_path = article_dir / RESEARCH_MD_FILE
    md_output_path.write_text(final_md, encoding="utf-8")

    return {
        "status": "success",
        "markdown_file": str(md_output_path.resolve()),
        "research_results_count": len(grouped),
        "scraped_sources_count": len(scraped_sources),
        "code_sources_count": len(code_sources),
        "youtube_transcripts_count": len(youtube_sources),
        "additional_sources_count": len(additional_sources),
        "message": f"✅ Generated research markdown file:\n  - {md_output_path.relative_to(article_dir)}",
    }