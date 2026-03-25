"""Unit tests for src/tools/process_local_files_tool.py.

Tests file-copying logic, .ipynb → .md conversion (with mocked converter),
filename sanitisation, warning/error handling, and the ``build_result_message``
helper.  No LLM calls.
"""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    LOCAL_FILES_FROM_RESEARCH_FOLDER,
    RESEARCH_OUTPUT_FOLDER,
)
from src.tools.process_local_files_tool import build_result_message, process_local_files_tool


def _setup_dir(tmp_path: Path, local_file_paths: list, create_files: dict | None = None) -> Path:
    """Create research folder with guidelines JSON and optional source files."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Topic", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    data = {"github_urls": [], "youtube_videos_urls": [], "other_urls": [], "local_file_paths": local_file_paths}
    (output / GUIDELINES_FILENAMES_FILE).write_text(json.dumps(data), encoding="utf-8")

    if create_files:
        for rel_path, content in create_files.items():
            p = tmp_path / rel_path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding="utf-8")

    return tmp_path


# ---------------------------------------------------------------------------
# build_result_message (pure function)
# ---------------------------------------------------------------------------


class TestBuildResultMessage:
    def test_basic_message(self, tmp_path):
        msg = build_result_message("test_dir", 2, ["a", "b"], tmp_path / "out", [], [])
        assert "2/2" in msg
        assert "test_dir" in msg

    def test_includes_warnings(self, tmp_path):
        msg = build_result_message("d", 1, ["a", "b"], tmp_path / "out", ["file not found"], [])
        assert "Warnings" in msg
        assert "Missing" in msg

    def test_includes_errors(self, tmp_path):
        msg = build_result_message("d", 0, ["a"], tmp_path / "out", [], ["copy failed"])
        assert "Errors" in msg

    def test_truncates_long_warnings(self, tmp_path):
        warnings = [f"warn_{i}" for i in range(5)]
        msg = build_result_message("d", 0, ["a"] * 5, tmp_path / "out", warnings, [])
        assert "more missing" in msg


# ---------------------------------------------------------------------------
# process_local_files_tool
# ---------------------------------------------------------------------------


class TestProcessLocalFilesTool:
    def test_copies_existing_files(self, tmp_path):
        research_dir = _setup_dir(
            tmp_path,
            local_file_paths=["data.md"],
            create_files={"data.md": "# Data\n\nContent."},
        )

        result = process_local_files_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["files_processed"] == 1
        dest = research_dir / RESEARCH_OUTPUT_FOLDER / LOCAL_FILES_FROM_RESEARCH_FOLDER
        assert (dest / "data.md").exists()

    def test_sanitises_path_separators_in_filename(self, tmp_path):
        research_dir = _setup_dir(
            tmp_path,
            local_file_paths=["sub/dir/file.md"],
            create_files={"sub/dir/file.md": "content"},
        )

        result = process_local_files_tool(str(research_dir))
        assert result["files_processed"] == 1
        dest = research_dir / RESEARCH_OUTPUT_FOLDER / LOCAL_FILES_FROM_RESEARCH_FOLDER
        assert (dest / "sub_dir_file.md").exists()

    def test_notebook_converted_to_markdown(self, tmp_path):
        research_dir = _setup_dir(
            tmp_path,
            local_file_paths=["analysis.ipynb"],
            create_files={"analysis.ipynb": "{}"},  # placeholder
        )

        with patch(
            "src.tools.process_local_files_tool.NotebookToMarkdownConverter"
        ) as MockConverter:
            instance = MockConverter.return_value
            instance.convert_notebook_to_string.return_value = "# Notebook as MD"
            result = process_local_files_tool(str(research_dir))

        assert result["files_processed"] == 1
        dest = research_dir / RESEARCH_OUTPUT_FOLDER / LOCAL_FILES_FROM_RESEARCH_FOLDER
        assert (dest / "analysis.md").exists()
        assert (dest / "analysis.md").read_text(encoding="utf-8") == "# Notebook as MD"

    def test_missing_file_produces_warning(self, tmp_path):
        research_dir = _setup_dir(tmp_path, local_file_paths=["nonexistent.py"])

        result = process_local_files_tool(str(research_dir))

        assert result["files_processed"] == 0
        assert len(result["warnings"]) == 1

    def test_empty_local_files_list(self, tmp_path):
        research_dir = _setup_dir(tmp_path, local_file_paths=[])

        result = process_local_files_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["files_processed"] == 0
        assert result["files_total"] == 0

    def test_raises_for_missing_folder(self):
        with pytest.raises(ValueError):
            process_local_files_tool("/nonexistent/path")
