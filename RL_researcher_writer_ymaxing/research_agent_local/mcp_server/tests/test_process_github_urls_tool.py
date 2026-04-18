"""Unit tests for src/tools/process_github_urls_tool.py.

The tool reads github_urls from guidelines_filenames.json, calls
``process_github_url`` for each (mocked), and returns a summary dict.
``settings.github_token`` is also patched to avoid loading real env vars.
"""

import json
from pathlib import Path
from unittest.mock import AsyncMock, patch, PropertyMock

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
)
from src.tools.process_github_urls_tool import process_github_urls_tool

_PATCH_HANDLER = "src.tools.process_github_urls_tool.process_github_url"
_PATCH_SETTINGS = "src.tools.process_github_urls_tool.settings"


def _setup_dir(tmp_path: Path, github_urls: list, url_titles: dict | None = None) -> Path:
    """Create research folder with article_guideline.md and guidelines JSON."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Topic", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    data = {"github_urls": github_urls, "youtube_videos_urls": [], "other_urls": [], "local_file_paths": [], "url_titles": url_titles or {}}
    (output / GUIDELINES_FILENAMES_FILE).write_text(json.dumps(data), encoding="utf-8")
    return tmp_path


class TestProcessGithubUrlsTool:
    async def test_success_processes_urls(self, tmp_path):
        research_dir = _setup_dir(tmp_path, ["https://github.com/a/b", "https://github.com/c/d"])

        mock_settings = type("S", (), {"github_token": type("T", (), {"get_secret_value": lambda self: "tok"})()})()
        with (
            patch(_PATCH_HANDLER, new_callable=AsyncMock, return_value=True) as mock_handler,
            patch(_PATCH_SETTINGS, mock_settings),
        ):
            result = await process_github_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["urls_processed"] == 2
        assert result["urls_total"] == 2
        assert mock_handler.await_count == 2

    async def test_empty_urls_returns_zero(self, tmp_path):
        research_dir = _setup_dir(tmp_path, [])

        mock_settings = type("S", (), {"github_token": type("T", (), {"get_secret_value": lambda self: None})()})()
        with patch(_PATCH_SETTINGS, mock_settings):
            result = await process_github_urls_tool(str(research_dir))

        assert result["urls_processed"] == 0
        assert result["urls_total"] == 0

    async def test_partial_failure(self, tmp_path):
        research_dir = _setup_dir(tmp_path, ["https://github.com/a/b", "https://github.com/c/d"])

        call_count = 0

        async def _side_effect(url, dest, token, title=""):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise RuntimeError("network error")
            return True

        mock_settings = type("S", (), {"github_token": type("T", (), {"get_secret_value": lambda self: "tok"})()})()
        with (
            patch(_PATCH_HANDLER, side_effect=_side_effect),
            patch(_PATCH_SETTINGS, mock_settings),
        ):
            result = await process_github_urls_tool(str(research_dir))

        assert result["urls_processed"] == 1
        assert result["urls_total"] == 2

    async def test_creates_output_directory(self, tmp_path):
        research_dir = _setup_dir(tmp_path, ["https://github.com/a/b"])

        mock_settings = type("S", (), {"github_token": type("T", (), {"get_secret_value": lambda self: "tok"})()})()
        with (
            patch(_PATCH_HANDLER, new_callable=AsyncMock, return_value=True),
            patch(_PATCH_SETTINGS, mock_settings),
        ):
            await process_github_urls_tool(str(research_dir))

        assert (research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_CODE_FOLDER).is_dir()

    async def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            await process_github_urls_tool("/nonexistent/path")

    async def test_title_forwarded_to_handler(self, tmp_path):
        url = "https://github.com/a/b"
        research_dir = _setup_dir(tmp_path, [url], url_titles={url: "My Awesome Library"})
        mock_settings = type("S", (), {"github_token": type("T", (), {"get_secret_value": lambda self: "tok"})()})()  # noqa: E501
        with (
            patch(_PATCH_HANDLER, new_callable=AsyncMock, return_value=True) as mock_handler,
            patch(_PATCH_SETTINGS, mock_settings),
        ):
            await process_github_urls_tool(str(research_dir))
        _, kwargs = mock_handler.call_args
        assert kwargs.get("title") == "My Awesome Library"
