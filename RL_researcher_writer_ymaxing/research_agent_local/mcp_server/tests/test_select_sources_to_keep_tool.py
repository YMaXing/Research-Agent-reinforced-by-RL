"""Unit tests for src/tools/select_research_sources_to_keep_tool.py.

``extract_selected_blocks_content`` is a pure regex helper tested directly.
``select_research_sources_to_keep_tool`` is async; the LLM-backed
``select_sources`` handler is mocked.
"""

from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    TAVILY_RESULTS_SELECTED_FILE,
    TAVILY_SOURCES_SELECTED_FILE,
)
from src.tools.select_research_sources_to_keep_tool import (
    extract_selected_blocks_content,
    select_research_sources_to_keep_tool,
)

_PATCH_SELECT = "src.tools.select_research_sources_to_keep_tool.select_sources"

# Sample markdown closely matching the actual tavily_results.md format.
_SAMPLE_MD = (
    "### Source [1]: First\n"
    "Content of source 1.\n\n"
    "### Source [2]: Second\n"
    "Content of source 2.\n\n"
    "### Source [3]: Third\n"
    "Content of source 3.\n"
)

_SAMPLE_MD_WITH_PHASE = (
    "Phase: [EXPLOITATION]\n\n"
    "### Source [1]: First\n"
    "Content of source 1.\n\n"
    "Phase: [EXPLORATION]\n\n"
    "### Source [2]: Second\n"
    "Content of source 2.\n"
)


def _setup_dir(tmp_path: Path, md_content: str = _SAMPLE_MD) -> Path:
    """Create a valid research directory with tavily_results.md."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Guidelines", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    (output / TAVILY_RESULTS_FILE).write_text(md_content, encoding="utf-8")
    return tmp_path


# ---------------------------------------------------------------------------
# extract_selected_blocks_content
# ---------------------------------------------------------------------------


class TestExtractSelectedBlocksContent:
    def test_selects_subset(self):
        result = extract_selected_blocks_content([1, 3], _SAMPLE_MD)
        assert "Source [1]" in result
        assert "Source [3]" in result
        assert "Source [2]" not in result

    def test_selects_all(self):
        result = extract_selected_blocks_content([1, 2, 3], _SAMPLE_MD)
        assert "Source [1]" in result
        assert "Source [2]" in result
        assert "Source [3]" in result

    def test_empty_ids_returns_empty(self):
        result = extract_selected_blocks_content([], _SAMPLE_MD)
        assert result == ""

    def test_non_matching_ids_returns_empty(self):
        result = extract_selected_blocks_content([99], _SAMPLE_MD)
        assert result == ""

    def test_phase_prefix_format(self):
        result = extract_selected_blocks_content([2], _SAMPLE_MD_WITH_PHASE)
        assert "Source [2]" in result
        assert "Source [1]" not in result


# ---------------------------------------------------------------------------
# select_research_sources_to_keep_tool (async)
# ---------------------------------------------------------------------------


class TestSelectResearchSourcesToKeepTool:
    async def test_success_writes_files(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        with patch(_PATCH_SELECT, new_callable=AsyncMock, return_value=[1, 3]):
            result = await select_research_sources_to_keep_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["sources_selected_count"] == 2
        assert result["selected_source_ids"] == [1, 3]

        output = research_dir / RESEARCH_OUTPUT_FOLDER
        # IDs file written
        ids_content = (output / TAVILY_SOURCES_SELECTED_FILE).read_text(encoding="utf-8")
        assert "1" in ids_content and "3" in ids_content

        # Filtered results written
        selected_content = (output / TAVILY_RESULTS_SELECTED_FILE).read_text(encoding="utf-8")
        assert "Source [1]" in selected_content
        assert "Source [2]" not in selected_content

    async def test_no_sources_selected(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        with patch(_PATCH_SELECT, new_callable=AsyncMock, return_value=[]):
            result = await select_research_sources_to_keep_tool(str(research_dir))

        assert result["sources_selected_count"] == 0

        output = research_dir / RESEARCH_OUTPUT_FOLDER
        selected_content = (output / TAVILY_RESULTS_SELECTED_FILE).read_text(encoding="utf-8")
        assert selected_content == ""

    async def test_raises_when_results_missing(self, tmp_path):
        (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("x", encoding="utf-8")
        (tmp_path / RESEARCH_OUTPUT_FOLDER).mkdir()
        # No tavily_results.md

        with pytest.raises(FileNotFoundError):
            await select_research_sources_to_keep_tool(str(tmp_path))

    async def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            await select_research_sources_to_keep_tool("/nonexistent/path")
