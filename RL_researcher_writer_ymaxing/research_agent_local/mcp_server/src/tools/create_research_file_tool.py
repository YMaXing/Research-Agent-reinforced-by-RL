"""Research file creation tool implementation."""

import logging
from pathlib import Path
from typing import Any, Dict

from ..app.tavily_handler import extract_tavily_chunks, group_tavily_by_query
from ..config.constants import (
    DEDUPLICATED_RESEARCH_FILE,
    LOCAL_FILES_FROM_RESEARCH_FOLDER,
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


def _wrap_xml(tag: str, attrs: str, content: str) -> str:
    """Wrap *content* in an XML element for downstream LLM provenance detection."""
    return f"<{tag} {attrs}>\n{content}\n</{tag}>"


def _build_tagged_sections(research_output_dir: Path) -> str:
    """
    Build all research sections with XML tags indicating golden vs research provenance.

    Golden sources (from article guidelines — only these are tagged ``<golden_source>``):
      - urls_from_guidelines (additional scraped pages from guideline links)
      - urls_from_guidelines_code (code repos referenced in guidelines)
      - urls_from_guidelines_youtube_videos (YouTube videos referenced in guidelines)
      - local_files_from_research (local files referenced in guidelines)

    Research sources (from Tavily exploration / exploitation — ``<research_source>``):
      - Tavily results
      - urls_from_research (scraped research URLs — may include code repos,
        YouTube videos, and web pages discovered through Tavily, NOT golden)
    """
    selected_results_file = research_output_dir / TAVILY_RESULTS_SELECTED_FILE
    original_results_file = research_output_dir / TAVILY_RESULTS_FILE

    urls_from_research_dir = research_output_dir / URLS_FROM_RESEARCH_FOLDER
    code_sources_dir = research_output_dir / URLS_FROM_GUIDELINES_CODE_FOLDER
    additional_sources_dir = research_output_dir / URLS_FROM_GUIDELINES_FOLDER
    youtube_transcripts_dir = research_output_dir / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
    local_files_dir = research_output_dir / LOCAL_FILES_FROM_RESEARCH_FOLDER

    # --- Tavily research results (non-golden) — one block per phase ---
    if selected_results_file.exists():
        results_md = read_file_safe(selected_results_file)
    else:
        results_md = read_file_safe(original_results_file)
    chunks = extract_tavily_chunks(results_md)

    exploitation_ids: list[int] = []
    exploration_ids: list[int] = []
    for src_id, chunk in chunks.items():
        first_line = chunk.split("\n", 1)[0] if chunk else ""
        if first_line.startswith("Phase:") and "[EXPLORATION]" in first_line:
            exploration_ids.append(src_id)
        else:
            exploitation_ids.append(src_id)

    tavily_parts: list[str] = []
    for phase_label, ids in [("exploitation", exploitation_ids), ("exploration", exploration_ids)]:
        if ids:
            grouped = group_tavily_by_query(chunks, ids)
            tavily_parts.append(_wrap_xml(
                "research_source", f'type="tavily_results" phase="{phase_label}"',
                build_research_results_section(grouped),
            ))
    if not tavily_parts:
        tavily_parts.append(_wrap_xml(
            "research_source", 'type="tavily_results" phase="exploitation"',
            "## Research Results\n\n_No accepted research results found._\n",
        ))
    research_results_section = "\n\n".join(tavily_parts)

    # --- Scraped research URLs (non-golden) — one block per file with phase attribute ---
    scraped_parts: list[str] = []
    if urls_from_research_dir.exists():
        for f in sorted(urls_from_research_dir.glob("*.md")):
            content = read_file_safe(f)
            if content:
                first_line = content.split("\n", 1)[0]
                phase = (
                    "exploration"
                    if first_line.startswith("Phase:") and "[EXPLORATION]" in first_line
                    else "exploitation"
                )
                scraped_parts.append(_wrap_xml(
                    "research_source",
                    f'type="scraped_from_research" phase="{phase}" file="{f.name}"',
                    content,
                ))
    sources_scraped_section = (
        "\n\n".join(scraped_parts)
        if scraped_parts
        else _wrap_xml(
            "research_source", 'type="scraped_from_research"',
            "## Sources Scraped From Research Results\n\n_No scraped sources found for research results._\n",
        )
    )

    # --- Code sources from guidelines (golden) ---
    code_sources = collect_directory_markdowns_with_titles(code_sources_dir)
    code_sources_section = _wrap_xml(
        "golden_source", 'type="guideline_code"',
        build_sources_section(
            "## Code Sources (from Article Guidelines)", code_sources,
            "No guideline code sources found.",
        ),
    )

    # --- YouTube transcripts from guidelines (golden) ---
    youtube_sources = collect_directory_markdowns_with_titles(youtube_transcripts_dir)
    youtube_transcripts_section = _wrap_xml(
        "golden_source", 'type="guideline_youtube"',
        build_sources_section(
            "## YouTube Video Transcripts (from Article Guidelines)", youtube_sources,
            "No guideline YouTube video transcripts found.",
        ),
    )

    # --- Additional scraped guideline URLs (golden) ---
    additional_sources = collect_directory_markdowns(additional_sources_dir)
    additional_sources_section = _wrap_xml(
        "golden_source", 'type="guideline_urls"',
        build_sources_section(
            "## Additional Sources Scraped (from Article Guidelines)", additional_sources,
            "No additional guideline sources scraped.",
        ),
    )

    # --- Local files (golden) ---
    local_files = collect_directory_markdowns_with_titles(local_files_dir)
    local_files_section = _wrap_xml(
        "golden_source", 'type="local_files"',
        build_sources_section(
            "## Local File Sources (from Article Guidelines)", local_files,
            "No local file sources found.",
        ),
    )

    final_md = combine_research_sections(
        research_results_section,
        sources_scraped_section,
        code_sources_section,
        youtube_transcripts_section,
        additional_sources_section,
        local_files_section,
    )

    counts = {
        "research_results_count": len(chunks),
        "scraped_sources_count": len(scraped_parts),
        "code_sources_count": len(code_sources),
        "youtube_transcripts_count": len(youtube_sources),
        "additional_sources_count": len(additional_sources),
        "local_files_count": len(local_files),
    }
    return final_md, counts


def create_research_file_tool(research_directory: str) -> Dict[str, Any]:
    """
    Generate comprehensive research.md file.

    When ``deduplicated_research.md`` exists the tool uses it as the primary
    body but **appends** the full tagged-section assembly so that downstream
    LLM judges can identify which content originates from golden sources vs
    Tavily research sources (via ``<golden_source>`` / ``<research_source>``
    XML tags).

    Falls back to the tagged multi-section assembly alone when no
    deduplicated file is present.
    """
    logger.debug(f"Creating research files for directory: {research_directory}")

    article_dir = Path(research_directory)
    research_output_dir = article_dir / RESEARCH_OUTPUT_FOLDER

    validate_research_folder(article_dir)

    dedup_path = research_output_dir / DEDUPLICATED_RESEARCH_FILE

    # Always build the tagged reference sections
    tagged_md, counts = _build_tagged_sections(research_output_dir)

    # === PREFERRED PATH: Dedup content + tagged golden-source appendix ===
    if dedup_path.exists():
        dedup_content = read_file_safe(dedup_path)
        final_md = (
            f"# Comprehensive Research Report\n\n"
            f"{dedup_content}\n\n"
            f"---\n\n"
            f"## Golden Source Reference\n\n"
            f"The sections below preserve the original source provenance via XML tags "
            f"(`<golden_source>` for guideline-referenced material, `<research_source>` "
            f"for Tavily / exploration results) so that downstream evaluation can assess "
            f"golden-source priority.\n\n"
            f"{tagged_md}\n\n"
            f"---\n\n"
            f"*Generated with content deduplication enabled.*"
        )

        md_output_path = article_dir / RESEARCH_MD_FILE
        md_output_path.write_text(final_md, encoding="utf-8")

        return {
            "status": "success",
            "markdown_file": str(md_output_path.resolve()),
            **counts,
            "message": (
                f"✅ Generated research markdown from deduplicated content "
                f"with golden-source reference appendix:\n  - {md_output_path.relative_to(article_dir)}"
            ),
        }

    # === FALLBACK: Tagged multi-section assembly (no deduplication) ===
    logger.info("⚠️  No deduplicated_research.md found — falling back to original multi-section assembly.")

    md_output_path = article_dir / RESEARCH_MD_FILE
    md_output_path.write_text(tagged_md, encoding="utf-8")

    return {
        "status": "success",
        "markdown_file": str(md_output_path.resolve()),
        **counts,
        "message": f"✅ Generated research markdown file:\n  - {md_output_path.relative_to(article_dir)}",
    }