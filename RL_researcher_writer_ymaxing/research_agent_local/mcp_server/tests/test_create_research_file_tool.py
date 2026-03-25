"""Unit tests for src/tools/create_research_file_tool.py.

Tests the two code paths:
  1. **Preferred path**: uses deduplicated_research.md when it exists.
  2. **Fallback path**: assembles from Tavily results + scraped directories.

No LLM calls — the tool only performs file I/O and calls pure helpers.
Tavily handler helpers (``extract_tavily_chunks``, ``group_tavily_by_query``)
are tested in test_tavily_handler.py.
"""

from pathlib import Path

import pytest

from src.config.constants import (
    DEDUPLICATED_RESEARCH_FILE,
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


class TestCreateResearchFileToolDedup:
    """Tests the preferred path using deduplicated_research.md."""

    def test_uses_dedup_file_when_present(self, tmp_path):
        research_dir = _setup_dir(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        output_dir.mkdir()
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


class TestCreateResearchFileToolFallback:
    """Tests the fallback multi-section assembly path."""

    def _setup_fallback(self, tmp_path: Path) -> Path:
        research_dir = _setup_dir(tmp_path)
        output_dir = research_dir / RESEARCH_OUTPUT_FOLDER
        output_dir.mkdir()

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
        ]:
            d = output_dir / folder_name
            d.mkdir()
            (d / "sample.md").write_text(f"# {folder_name}\n\nContent.", encoding="utf-8")

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

    def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            create_research_file_tool("/nonexistent/path")
