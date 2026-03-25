"""Unit tests for src/tools/extract_guidelines_urls_tool.py.

The tool reads article_guideline.md, calls handler functions to extract URLs
and local paths, writes results to a JSON file, and returns a summary dict.
No LLM calls — purely file I/O + regex logic (handler functions are tested
separately in test_guideline_extractions_handler.py).
"""

import json
from pathlib import Path

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)
from src.tools.extract_guidelines_urls_tool import extract_guidelines_urls_tool


def _setup_dir(tmp_path: Path, guideline_text: str) -> Path:
    """Create a research folder with an article_guideline.md file."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text(guideline_text, encoding="utf-8")
    return tmp_path


class TestExtractGuidelinesUrlsTool:
    def test_success_with_mixed_urls(self, tmp_path):
        text = (
            "GitHub: https://github.com/owner/repo\n"
            "YouTube: https://youtube.com/watch?v=abc\n"
            "Web: https://docs.example.com/page\n"
            'Local: "src/main.py"\n'
        )
        research_dir = _setup_dir(tmp_path, text)
        result = extract_guidelines_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["github_sources_count"] == 1
        assert result["youtube_sources_count"] == 1
        assert result["web_sources_count"] == 1
        assert result["local_files_count"] >= 1

        # Check that output file was created
        output_path = research_dir / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE
        assert output_path.exists()

        data = json.loads(output_path.read_text(encoding="utf-8"))
        assert "github_urls" in data
        assert "youtube_videos_urls" in data
        assert "other_urls" in data
        assert "local_file_paths" in data

    def test_no_urls_no_files(self, tmp_path):
        research_dir = _setup_dir(tmp_path, "Just plain text, nothing to extract.")
        result = extract_guidelines_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["github_sources_count"] == 0
        assert result["youtube_sources_count"] == 0
        assert result["web_sources_count"] == 0

    def test_creates_research_output_folder(self, tmp_path):
        research_dir = _setup_dir(tmp_path, "https://example.com")
        extract_guidelines_urls_tool(str(research_dir))
        assert (research_dir / RESEARCH_OUTPUT_FOLDER).is_dir()

    def test_raises_for_missing_research_folder(self):
        with pytest.raises(ValueError):
            extract_guidelines_urls_tool("/nonexistent/path")

    def test_raises_for_missing_guideline_file(self, tmp_path):
        # Folder exists but no article_guideline.md
        with pytest.raises(ValueError):
            extract_guidelines_urls_tool(str(tmp_path))
