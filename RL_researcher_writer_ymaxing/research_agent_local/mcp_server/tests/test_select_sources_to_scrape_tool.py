"""Unit tests for src/tools/select_research_sources_to_scrape_tool.py.

The async tool calls ``select_top_sources`` and ``load_scraped_guideline_context``
(both mocked).  Deterministic I/O assertions only.
"""

import json
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_SELECTED_FILE,
    URL_PHASES_FILE,
    URLS_TO_SCRAPE_FROM_RESEARCH_FILE,
)
from src.tools.select_research_sources_to_scrape_tool import (
    select_research_sources_to_scrape_tool,
)

_PATCH_SELECT_TOP = "src.tools.select_research_sources_to_scrape_tool.select_top_sources"
_PATCH_LOAD_CTX = "src.tools.select_research_sources_to_scrape_tool.load_scraped_guideline_context"


def _setup_dir(tmp_path: Path) -> Path:
    """Create research dir with required files for the tool."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Guidelines", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    (output / TAVILY_RESULTS_SELECTED_FILE).write_text(
        "### Source [1]: Example\nSome content.\n", encoding="utf-8"
    )
    return tmp_path


class TestSelectResearchSourcesToScrapeTool:
    async def test_success_writes_urls_and_phases(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        fake_selection = {
            "selected_urls": ["https://a.com", "https://b.com"],
            "url_to_phase": {"https://a.com": "[EXPLOITATION]", "https://b.com": "[EXPLORATION]"},
            "reasoning": "Both are authoritative.",
        }

        with (
            patch(_PATCH_LOAD_CTX, return_value="prior context"),
            patch(_PATCH_SELECT_TOP, new_callable=AsyncMock, return_value=fake_selection),
        ):
            result = await select_research_sources_to_scrape_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["urls_selected_count"] == 2
        assert result["selected_urls"] == ["https://a.com", "https://b.com"]

        output = research_dir / RESEARCH_OUTPUT_FOLDER

        # Verify URL file contents
        urls = (output / URLS_TO_SCRAPE_FROM_RESEARCH_FILE).read_text(encoding="utf-8").strip().splitlines()
        assert urls == ["https://a.com", "https://b.com"]

        # Verify phase JSON
        phases = json.loads((output / URL_PHASES_FILE).read_text(encoding="utf-8"))
        assert phases["https://a.com"] == "[EXPLOITATION]"

    async def test_empty_selection(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        fake_selection = {
            "selected_urls": [],
            "url_to_phase": {},
            "reasoning": "None relevant.",
        }

        with (
            patch(_PATCH_LOAD_CTX, return_value=""),
            patch(_PATCH_SELECT_TOP, new_callable=AsyncMock, return_value=fake_selection),
        ):
            result = await select_research_sources_to_scrape_tool(str(research_dir))

        assert result["urls_selected_count"] == 0

    async def test_max_sources_passed_to_handler(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        fake_selection = {
            "selected_urls": ["https://a.com"],
            "url_to_phase": {"https://a.com": "[EXPLOITATION]"},
            "reasoning": "Top pick.",
        }

        with (
            patch(_PATCH_LOAD_CTX, return_value=""),
            patch(_PATCH_SELECT_TOP, new_callable=AsyncMock, return_value=fake_selection) as mock_select,
        ):
            await select_research_sources_to_scrape_tool(str(research_dir), max_sources=3)

        # Verify max_sources was forwarded
        mock_select.assert_awaited_once()
        _, kwargs = mock_select.call_args
        # max_sources is a positional arg (4th param)
        args = mock_select.call_args.args
        assert args[3] == 3  # max_sources

    async def test_raises_when_selected_file_missing(self, tmp_path):
        (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("x", encoding="utf-8")
        (tmp_path / RESEARCH_OUTPUT_FOLDER).mkdir()
        # No tavily_results_selected.md

        with pytest.raises(FileNotFoundError):
            await select_research_sources_to_scrape_tool(str(tmp_path))

    async def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            await select_research_sources_to_scrape_tool("/nonexistent/path")
