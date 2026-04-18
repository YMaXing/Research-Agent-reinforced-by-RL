"""Markdown processing utilities."""

from typing import Dict, List, Tuple


def markdown_collapsible(title: str, body: str) -> str:
    """Return a Markdown collapsible block using <details> / <summary>."""
    stripped_body = body.strip()
    # Balance any unclosed code fence so </details> is not swallowed into a <pre> block.
    if stripped_body.count("```") % 2 != 0:
        stripped_body += "\n```"
    return f"<details>\n<summary>{title}</summary>\n\n{stripped_body}\n\n</details>\n"


def get_first_line_title(markdown: str) -> str:
    """
    Get the title from markdown content.

    Prefers the first markdown heading (any level, outside code blocks).
    Falls back to the first non-empty line with leading '#' stripped.
    If neither is found, returns 'Untitled'.
    """
    in_code_block = False
    first_non_empty: str | None = None
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if not in_code_block and stripped:
            if first_non_empty is None:
                first_non_empty = stripped.lstrip("#").strip()
            if stripped.startswith("#"):
                return stripped.lstrip("#").strip() or "Untitled"
    return first_non_empty or "Untitled"


def build_research_results_section(grouped_queries: Dict[str, List[str]]) -> str:
    """
    Build the Research Results section from grouped tavily query results.

    Args:
        grouped_queries: Dict mapping query strings to lists of result blocks

    Returns:
        Formatted markdown string for the research results section
    """
    research_results_blocks: List[str] = []
    for query, blocks in grouped_queries.items():
        body = "\n\n-----\n\n".join(blocks)
        research_results_blocks.append(markdown_collapsible(query, body))

    if research_results_blocks:
        return "## Research Results\n\n" + "\n".join(research_results_blocks)
    else:
        return "## Research Results\n\n_No accepted research results found._\n"


def build_sources_section(section_title: str, sources: List[Tuple[str, str]], empty_message: str) -> str:
    """
    Build a sources section from a list of title-body pairs.

    Args:
        section_title: Title for the section (e.g., "## Code Sources")
        sources: List of (title, body) tuples for each source
        empty_message: Message to show when no sources are found

    Returns:
        Formatted markdown string for the sources section
    """
    if sources:
        blocks = [markdown_collapsible(title, body) for title, body in sources]
        return f"{section_title}\n\n" + "\n".join(blocks)
    else:
        return f"{section_title}\n\n_{empty_message}_\n"


def combine_research_sections(
    research_results_section: str,
    sources_scraped_section: str,
    code_sources_section: str,
    youtube_transcripts_section: str,
    additional_sources_section: str,
    local_files_section: str = "",
    exploitation_guideline_section: str = "",
) -> str:
    """
    Combine all research sections into a single markdown document.

    Args:
        research_results_section: Research results section markdown
        sources_scraped_section: Sources scraped section markdown
        code_sources_section: Code sources section markdown
        youtube_transcripts_section: YouTube transcripts section markdown
        additional_sources_section: Additional sources section markdown
        local_files_section: Local files section markdown (optional)
        exploitation_guideline_section: Exploitation guideline sources section markdown (optional)

    Returns:
        Complete markdown document as a single string
    """
    sections = [
        "# Research",  # Title of the document
        research_results_section,
        sources_scraped_section,
        code_sources_section,
        youtube_transcripts_section,
        additional_sources_section,
    ]
    if exploitation_guideline_section:
        sections.append(exploitation_guideline_section)
    if local_files_section:
        sections.append(local_files_section)
    return "\n\n".join(sections)
