"""Unit tests for src/tools/create_research_file_tool.py.

Tests the two code paths:
  1. **Preferred path**: uses deduplicated_research.md + appends tagged sections.
  2. **Fallback path**: assembles from Tavily results + scraped directories with XML tags.

No LLM calls — the tool only performs file I/O and calls pure helpers.
Tavily handler helpers (``extract_tavily_chunks``, ``group_tavily_by_query``)
are tested in test_tavily_handler.py.
"""

from pathlib import Path

import pytest

from src.config.constants import (
    DEDUPLICATED_RESEARCH_FILE,
    LOCAL_FILES_FROM_RESEARCH_FOLDER,
    RESEARCH_MD_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,
)
from src.tools.create_research_file_tool import create_research_file_tool


def _setup_dir(tmp_path: Path) -> Path:
    """Create a minimal research folder with required article_guideline.md."""
    (tmp_path / "article_guideline.md").write_text("# Topic\n\nGuidelines.", encoding="utf-8")
    return tmp_path


def _setup_source_dirs(research_dir: Path) -> Path:
    """Populate all source directories including local files."""
    output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
    output_dir.mkdir(exist_ok=True)

    # Create a minimal tavily_results.md
    tavily_md = (
        "### Source [1]: https://a.com\n\n"
        "Query: What is RAG?\n\n"
        "Answer: RAG retrieves context.\n\n-----\n"
    )
    (output_dir / TAVILY_RESULTS_FILE).write_text(tavily_md, encoding="utf-8")

    # Create scraped source directories with content
    for folder_name in [
        URLS_FROM_RESEARCH_FOLDER,
        URLS_FROM_GUIDELINES_CODE_FOLDER,
        URLS_FROM_GUIDELINES_FOLDER,
        URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
        LOCAL_FILES_FROM_RESEARCH_FOLDER,
    ]:
        d = output_dir / folder_name
        d.mkdir()
        (d / "sample.md").write_text(f"# {folder_name}\n\nContent.", encoding="utf-8")

    return output_dir


class TestCreateResearchFileToolDedup:
    """Tests the preferred path using deduplicated_research.md."""

    def test_uses_dedup_file_when_present(self, tmp_path):
        research_dir = _setup_dir(tmp_path)
        output_dir = _setup_source_dirs(research_dir)
        (output_dir / DEDUPLICATED_RESEARCH_FILE).write_text(
            "# Dedup content\n\nClean output.", encoding="utf-8"
        )

        result = create_research_file_tool(str(research_dir))

        assert result["status"] == "success"
        md_path = research_dir / RESEARCH_MD_FILE
        assert md_path.exists()
        content = md_path.read_text(encoding="utf-8")
        assert "Dedup content" in content
        assert "deduplication enabled" in content.lower()

    def test_dedup_path_appends_tagged_sections(self, tmp_path):
        """When dedup file exists, tagged golden-source reference sections are appended."""
        research_dir = _setup_dir(tmp_path)
        output_dir = _setup_source_dirs(research_dir)
        (output_dir / DEDUPLICATED_RESEARCH_FILE).write_text(
            "# Dedup content\n\nClean output.", encoding="utf-8"
        )

        result = create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "<golden_source" in content
        assert "<research_source" in content
        assert "Golden Source Reference" in content

    def test_dedup_path_includes_local_files_count(self, tmp_path):
        research_dir = _setup_dir(tmp_path)
        output_dir = _setup_source_dirs(research_dir)
        (output_dir / DEDUPLICATED_RESEARCH_FILE).write_text("dedup", encoding="utf-8")

        result = create_research_file_tool(str(research_dir))

        assert "local_files_count" in result
        assert result["local_files_count"] == 1


class TestCreateResearchFileToolFallback:
    """Tests the fallback multi-section assembly path."""

    def _setup_fallback(self, tmp_path: Path) -> Path:
        research_dir = _setup_dir(tmp_path)
        _setup_source_dirs(research_dir)
        return research_dir

    def test_fallback_produces_research_md(self, tmp_path):
        research_dir = self._setup_fallback(tmp_path)
        result = create_research_file_tool(str(research_dir))

        assert result["status"] == "success"
        md_path = research_dir / RESEARCH_MD_FILE
        assert md_path.exists()
        content = md_path.read_text(encoding="utf-8")
        assert len(content) > 0

    def test_fallback_result_has_counts(self, tmp_path):
        research_dir = self._setup_fallback(tmp_path)
        result = create_research_file_tool(str(research_dir))

        assert "research_results_count" in result
        assert "scraped_sources_count" in result
        assert "code_sources_count" in result
        assert "youtube_transcripts_count" in result
        assert "additional_sources_count" in result
        assert "local_files_count" in result

    def test_fallback_includes_xml_tags(self, tmp_path):
        """Fallback output should include golden_source and research_source XML tags."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "<golden_source" in content
        assert "</golden_source>" in content
        assert "<research_source" in content
        assert "</research_source>" in content

    def test_fallback_marks_guideline_code_as_golden(self, tmp_path):
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert '<golden_source type="guideline_code">' in content

    def test_fallback_marks_guideline_youtube_as_golden(self, tmp_path):
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert '<golden_source type="guideline_youtube">' in content

    def test_fallback_marks_local_files_as_golden(self, tmp_path):
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert '<golden_source type="local_files">' in content

    def test_fallback_marks_tavily_as_research(self, tmp_path):
        """Tavily blocks carry type='tavily_results' with a phase attribute."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert 'type="tavily_results"' in content
        assert 'phase=' in content

    def test_fallback_marks_scraped_research_as_research(self, tmp_path):
        """Scraped research blocks carry type='scraped_from_research' with phase and file attributes."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert 'type="scraped_from_research"' in content
        assert 'phase=' in content
        assert 'file=' in content

    def test_fallback_tavily_defaults_to_exploitation_phase(self, tmp_path):
        """Tavily results with no Phase prefix are wrapped with phase='exploitation'."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert 'type="tavily_results" phase="exploitation"' in content

    def test_fallback_scraped_exploration_file_gets_exploration_phase(self, tmp_path):
        """A scraped file with a Phase: [EXPLORATION] header gets phase='exploration'."""
        research_dir = self._setup_fallback(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        exploration_file = output_dir / URLS_FROM_RESEARCH_FOLDER / "exploration_source.md"
        exploration_file.write_text(
            "Phase: [EXPLORATION]\n\n# Exploration Source\n\nContent.", encoding="utf-8"
        )

        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert 'type="scraped_from_research" phase="exploration" file="exploration_source.md"' in content

    def test_fallback_scraped_per_file_wrapping(self, tmp_path):
        """Each scraped file gets its own <research_source> wrapper with a file attribute."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert 'file="sample.md"' in content

    def test_scraped_file_with_h1_uses_h1_as_collapsible_title(self, tmp_path):
        """A scraped file with an H1 heading should use the H1 text as the collapsible title."""
        research_dir = self._setup_fallback(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        h1_file = output_dir / URLS_FROM_RESEARCH_FOLDER / "my-source.md"
        h1_file.write_text(
            "**Source URL:** https://example.com\n\n# Real Page Title\n\nBody content.",
            encoding="utf-8",
        )

        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "<summary>Real Page Title</summary>" in content

    def test_scraped_file_with_only_h2_falls_back_to_filename_stem(self, tmp_path):
        """A scraped file with no H1 (only H2/H3) should fall back to the filename stem,
        not pick up a subheading as the collapsible title."""
        research_dir = self._setup_fallback(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        h2_only_file = output_dir / URLS_FROM_RESEARCH_FOLDER / "subheading-only.md"
        h2_only_file.write_text(
            "**Source URL:** https://example.com\n\n## Summary\n\nBody content.",
            encoding="utf-8",
        )

        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "<summary>subheading-only</summary>" in content
        assert "<summary>Summary</summary>" not in content

    def test_scraped_file_with_heading_in_code_fence_uses_fallback_title(self, tmp_path):
        """A scraped file whose only heading is inside a code fence should use the
        filename stem as the collapsible title, not the fenced heading."""
        research_dir = self._setup_fallback(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        fenced_file = output_dir / URLS_FROM_RESEARCH_FOLDER / "arxiv-article.md"
        fenced_file.write_text(
            "Phase: [EXPLOITATION]\n\n"
            "```markdown\n## 1 Introduction\nFenced content\n```\n",
            encoding="utf-8",
        )

        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        # The title should be the filename stem, not '1 Introduction'
        assert "<summary>arxiv-article</summary>" in content
        assert "<summary>1 Introduction</summary>" not in content

    def test_scraped_file_with_unclosed_code_fence_closes_before_details(self, tmp_path):
        """A scraped file with an unclosed code fence must have it closed before
        </details> so that subsequent sections are not swallowed."""
        research_dir = self._setup_fallback(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        unclosed_file = output_dir / URLS_FROM_RESEARCH_FOLDER / "unclosed.md"
        unclosed_file.write_text(
            "# Real Heading\n\n```markdown\n## Section\nContent without closing fence",
            encoding="utf-8",
        )

        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        # The closing ``` must appear before </details> for this block
        unclosed_block_start = content.index('file="unclosed.md"')
        block_slice = content[unclosed_block_start:]
        fence_close_pos = block_slice.index("```\n\n</details>")
        details_pos = block_slice.index("</details>")
        assert fence_close_pos < details_pos

    def test_fallback_includes_local_files_section(self, tmp_path):
        """Local files should appear in the fallback output."""
        research_dir = self._setup_fallback(tmp_path)
        result = create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "## Local File Sources (from Article Guidelines)" in content
        assert result["local_files_count"] == 1

    def test_fallback_section_titles_indicate_guideline_provenance(self, tmp_path):
        """Section titles for golden sources should clarify they come from article guidelines."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        assert "## Code Sources (from Article Guidelines)" in content
        assert "## YouTube Video Transcripts (from Article Guidelines)" in content
        assert "## Additional Sources Scraped (from Article Guidelines)" in content

    def test_research_sources_not_marked_golden(self, tmp_path):
        """Tavily results and scraped research URLs must NOT be tagged as golden."""
        research_dir = self._setup_fallback(tmp_path)
        create_research_file_tool(str(research_dir))

        content = (research_dir / RESEARCH_MD_FILE).read_text(encoding="utf-8")
        # Tavily and scraped-from-research should be <research_source>, not <golden_source>
        assert 'type="tavily_results"' in content
        assert 'type="scraped_from_research"' in content
        # These types must not appear as golden
        assert '<golden_source type="tavily_results">' not in content
        assert '<golden_source type="scraped_from_research">' not in content

    def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            create_research_file_tool("/nonexistent/path")
