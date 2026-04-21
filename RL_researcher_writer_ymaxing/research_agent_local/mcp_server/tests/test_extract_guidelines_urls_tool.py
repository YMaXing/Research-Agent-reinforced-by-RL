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
        assert "exploitation_github_urls" in data
        assert "exploitation_youtube_videos_urls" in data
        assert "exploitation_other_urls" in data
        assert "url_titles" in data

    def test_golden_and_exploitation_sections_separated(self, tmp_path):
        text = (
            "## Golden Sources\n"
            "1. [Gold YT](https://youtube.com/watch?v=gold)\n"
            "2. [Gold GH](https://github.com/gold/repo)\n"
            "## Article Code\n"
            "1. [Notebook](https://github.com/code/notebook)\n"
            "## Other Sources\n"
            "1. [Other web](https://other.example.com/article)\n"
            "2. [Other ArXiv](https://arxiv.org/abs/9999.00001)\n"
            "3. [Other GH](https://github.com/other/repo)\n"
            "4. [Other YT](https://youtube.com/watch?v=other)\n"
        )
        research_dir = _setup_dir(tmp_path, text)
        result = extract_guidelines_urls_tool(str(research_dir))

        assert result["status"] == "success"

        # Golden counts
        assert result["youtube_sources_count"] == 1       # Golden YT only
        assert result["github_sources_count"] == 2        # Gold GH + Notebook
        assert result["web_sources_count"] == 0           # No golden web URLs

        # Exploitation counts
        assert result["exploitation_youtube_sources_count"] == 1
        assert result["exploitation_github_sources_count"] == 1
        assert result["exploitation_web_sources_count"] == 2   # other.example.com + arxiv

        output_path = research_dir / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE
        data = json.loads(output_path.read_text(encoding="utf-8"))

        assert "https://youtube.com/watch?v=gold" in data["youtube_videos_urls"]
        assert "https://github.com/gold/repo" in data["github_urls"]
        assert "https://github.com/code/notebook" in data["github_urls"]

        assert "https://other.example.com/article" in data["exploitation_other_urls"]
        assert "https://arxiv.org/abs/9999.00001" in data["exploitation_other_urls"]
        assert "https://github.com/other/repo" in data["exploitation_github_urls"]
        assert "https://youtube.com/watch?v=other" in data["exploitation_youtube_videos_urls"]

        # url_titles captures link text from all markdown links
        assert "url_titles" in data
        assert data["url_titles"].get("https://youtube.com/watch?v=gold") == "Gold YT"
        assert data["url_titles"].get("https://github.com/gold/repo") == "Gold GH"
        assert data["url_titles"].get("https://github.com/other/repo") == "Other GH"
        assert data["url_titles"].get("https://youtube.com/watch?v=other") == "Other YT"

    def test_no_urls_no_files(self, tmp_path):
        research_dir = _setup_dir(tmp_path, "Just plain text, nothing to extract.")
        result = extract_guidelines_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["github_sources_count"] == 0
        assert result["youtube_sources_count"] == 0
        assert result["web_sources_count"] == 0
        assert result["exploitation_github_sources_count"] == 0
        assert result["exploitation_youtube_sources_count"] == 0
        assert result["exploitation_web_sources_count"] == 0

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
