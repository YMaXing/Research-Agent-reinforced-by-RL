"""
Unit tests for src/utils/file_utils.py.

Uses ``tmp_path`` (pytest built-in) for all filesystem operations.
No LLM calls involved.
"""

import pytest
from pathlib import Path

from src.utils.file_utils import (
    collect_directory_markdowns,
    collect_directory_markdowns_with_titles,
    read_file_safe,
    validate_guidelines_file,
    validate_research_folder,
)


# ---------------------------------------------------------------------------
# read_file_safe
# ---------------------------------------------------------------------------

class TestReadFileSafe:
    def test_reads_existing_utf8_file(self, tmp_path: Path):
        f = tmp_path / "test.md"
        f.write_text("Hello world", encoding="utf-8")
        assert read_file_safe(f) == "Hello world"

    def test_returns_empty_string_for_nonexistent_file(self, tmp_path: Path):
        result = read_file_safe(tmp_path / "missing.md")
        assert result == ""

    def test_reads_file_with_unicode_content(self, tmp_path: Path):
        f = tmp_path / "unicode.md"
        f.write_text("Résumé and naïve 🚀", encoding="utf-8")
        content = read_file_safe(f)
        assert "Résumé" in content
        assert "🚀" in content

    def test_reads_multiline_file(self, tmp_path: Path):
        f = tmp_path / "multi.md"
        f.write_text("Line 1\nLine 2\nLine 3", encoding="utf-8")
        content = read_file_safe(f)
        assert "Line 1" in content
        assert "Line 3" in content

    def test_returns_empty_string_for_empty_file(self, tmp_path: Path):
        f = tmp_path / "empty.md"
        f.write_text("", encoding="utf-8")
        assert read_file_safe(f) == ""

    def test_returns_string_type(self, tmp_path: Path):
        f = tmp_path / "test.md"
        f.write_text("content", encoding="utf-8")
        assert isinstance(read_file_safe(f), str)


# ---------------------------------------------------------------------------
# validate_research_folder
# ---------------------------------------------------------------------------

class TestValidateResearchFolder:
    def test_valid_directory_does_not_raise(self, tmp_path: Path):
        validate_research_folder(tmp_path)  # should not raise

    def test_nonexistent_path_raises_value_error(self, tmp_path: Path):
        with pytest.raises(ValueError, match="does not exist"):
            validate_research_folder(tmp_path / "nonexistent_folder")

    def test_file_path_raises_value_error(self, tmp_path: Path):
        f = tmp_path / "file.txt"
        f.write_text("I am a file", encoding="utf-8")
        with pytest.raises(ValueError, match="not a directory"):
            validate_research_folder(f)

    def test_nested_valid_directory_does_not_raise(self, tmp_path: Path):
        nested = tmp_path / "a" / "b" / "c"
        nested.mkdir(parents=True)
        validate_research_folder(nested)  # should not raise


# ---------------------------------------------------------------------------
# validate_guidelines_file
# ---------------------------------------------------------------------------

class TestValidateGuidelinesFile:
    def test_valid_file_does_not_raise(self, tmp_path: Path):
        f = tmp_path / "guideline.md"
        f.write_text("# Guidelines\n\nContent here.", encoding="utf-8")
        validate_guidelines_file(f)  # should not raise

    def test_nonexistent_file_raises_value_error(self, tmp_path: Path):
        with pytest.raises(ValueError, match="does not exist"):
            validate_guidelines_file(tmp_path / "missing.md")

    def test_directory_path_raises_value_error(self, tmp_path: Path):
        with pytest.raises(ValueError, match="not a file"):
            validate_guidelines_file(tmp_path)


# ---------------------------------------------------------------------------
# collect_directory_markdowns
# ---------------------------------------------------------------------------

class TestCollectDirectoryMarkdowns:
    def test_empty_directory_returns_empty_list(self, tmp_path: Path):
        assert collect_directory_markdowns(tmp_path) == []

    def test_nonexistent_directory_returns_empty_list(self, tmp_path: Path):
        assert collect_directory_markdowns(tmp_path / "nonexistent") == []

    def test_collects_md_files_and_ignores_others(self, tmp_path: Path):
        (tmp_path / "page.md").write_text("# Page\nContent", encoding="utf-8")
        (tmp_path / "notes.md").write_text("# Notes\nContent", encoding="utf-8")
        (tmp_path / "data.txt").write_text("Not markdown")
        (tmp_path / "config.json").write_text("{}")
        results = collect_directory_markdowns(tmp_path)
        assert len(results) == 2

    def test_returns_list_of_title_content_tuples(self, tmp_path: Path):
        (tmp_path / "doc.md").write_text("Content here", encoding="utf-8")
        results = collect_directory_markdowns(tmp_path)
        assert len(results) == 1
        title, content = results[0]
        assert isinstance(title, str)
        assert isinstance(content, str)

    def test_title_is_filename_stem(self, tmp_path: Path):
        (tmp_path / "my_document.md").write_text("Content", encoding="utf-8")
        results = collect_directory_markdowns(tmp_path)
        assert results[0][0] == "my_document"

    def test_content_matches_file_content(self, tmp_path: Path):
        (tmp_path / "page.md").write_text("Hello RAG world", encoding="utf-8")
        results = collect_directory_markdowns(tmp_path)
        assert "Hello RAG world" in results[0][1]

    def test_empty_md_files_are_excluded(self, tmp_path: Path):
        (tmp_path / "empty.md").write_text("", encoding="utf-8")
        (tmp_path / "nonempty.md").write_text("Something", encoding="utf-8")
        results = collect_directory_markdowns(tmp_path)
        assert len(results) == 1

    def test_files_sorted_alphabetically(self, tmp_path: Path):
        (tmp_path / "zebra.md").write_text("Z", encoding="utf-8")
        (tmp_path / "alpha.md").write_text("A", encoding="utf-8")
        (tmp_path / "middle.md").write_text("M", encoding="utf-8")
        results = collect_directory_markdowns(tmp_path)
        titles = [t for t, _ in results]
        assert titles == ["alpha", "middle", "zebra"]


# ---------------------------------------------------------------------------
# collect_directory_markdowns_with_titles
# ---------------------------------------------------------------------------

class TestCollectDirectoryMarkdownsWithTitles:
    def test_nonexistent_directory_returns_empty_list(self, tmp_path: Path):
        assert collect_directory_markdowns_with_titles(tmp_path / "nope") == []

    def test_extracts_title_from_markdown_header(self, tmp_path: Path):
        (tmp_path / "doc.md").write_text("# My RAG Article\nContent", encoding="utf-8")
        results = collect_directory_markdowns_with_titles(tmp_path)
        assert len(results) == 1
        assert results[0][0] == "My RAG Article"

    def test_title_without_hash_uses_first_line(self, tmp_path: Path):
        (tmp_path / "doc.md").write_text("Plain Title\nContent", encoding="utf-8")
        results = collect_directory_markdowns_with_titles(tmp_path)
        assert results[0][0] == "Plain Title"

    def test_content_includes_full_file_text(self, tmp_path: Path):
        text = "# Title\nLine one\nLine two"
        (tmp_path / "doc.md").write_text(text, encoding="utf-8")
        results = collect_directory_markdowns_with_titles(tmp_path)
        assert "Line one" in results[0][1]
        assert "Line two" in results[0][1]

    def test_multiple_files_all_collected(self, tmp_path: Path):
        (tmp_path / "a.md").write_text("# Alpha\nContent", encoding="utf-8")
        (tmp_path / "b.md").write_text("# Beta\nContent", encoding="utf-8")
        results = collect_directory_markdowns_with_titles(tmp_path)
        titles = [t for t, _ in results]
        assert "Alpha" in titles
        assert "Beta" in titles
