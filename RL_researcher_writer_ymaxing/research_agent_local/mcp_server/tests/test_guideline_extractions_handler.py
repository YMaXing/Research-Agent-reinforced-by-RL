"""Unit tests for src/app/guideline_extractions_handler.py.

Both ``extract_urls`` and ``extract_local_paths`` are pure functions —
no LLM mocking or file I/O is required.
``extract_urls_by_section`` is also pure and tested here.
"""

import pytest

from src.app.guideline_extractions_handler import extract_local_paths, extract_urls, extract_urls_by_section


# ---------------------------------------------------------------------------
# extract_urls
# ---------------------------------------------------------------------------


class TestExtractUrls:
    def test_extracts_http_and_https(self):
        text = "Visit http://example.com and https://secure.example.com/page"
        urls = extract_urls(text)
        assert "http://example.com" in urls
        assert "https://secure.example.com/page" in urls

    def test_extracts_github_urls(self):
        text = "See https://github.com/owner/repo for the code."
        urls = extract_urls(text)
        assert "https://github.com/owner/repo" in urls

    def test_extracts_youtube_urls(self):
        text = "Watch https://youtube.com/watch?v=abc123 for a demo."
        urls = extract_urls(text)
        assert "https://youtube.com/watch?v=abc123" in urls

    def test_returns_empty_for_no_urls(self):
        assert extract_urls("No links here") == []

    def test_handles_urls_in_markdown_links(self):
        text = "Check [this link](https://docs.example.com/guide) for docs."
        urls = extract_urls(text)
        assert any("docs.example.com/guide" in u for u in urls)

    def test_multiple_urls_same_line(self):
        text = "https://a.com and https://b.com"
        urls = extract_urls(text)
        assert len(urls) == 2

    def test_ignores_non_url_text(self):
        text = "some text without protocols ftp://hidden"
        urls = extract_urls(text)
        assert all(u.startswith("http") for u in urls)


# ---------------------------------------------------------------------------
# extract_local_paths
# ---------------------------------------------------------------------------


class TestExtractLocalPaths:
    def test_extracts_quoted_python_file(self):
        text = 'Reference the file "src/main.py" for details.'
        paths = extract_local_paths(text)
        assert "src/main.py" in paths

    def test_extracts_quoted_notebook(self):
        text = 'Open "analysis.ipynb" to see the results.'
        paths = extract_local_paths(text)
        assert "analysis.ipynb" in paths

    def test_extracts_quoted_markdown_file(self):
        text = 'See "docs/guide.md" for instructions.'
        paths = extract_local_paths(text)
        assert "docs/guide.md" in paths

    def test_ignores_quoted_urls(self):
        text = 'See "https://example.com/file.py" for info.'
        paths = extract_local_paths(text)
        assert len(paths) == 0

    def test_extracts_standalone_filename(self):
        text = "Check the file main.py for the entry point."
        paths = extract_local_paths(text)
        assert "main.py" in paths

    def test_ignores_unsupported_extensions(self):
        text = 'Open "data.csv" and "image.png" for data.'
        paths = extract_local_paths(text)
        assert len(paths) == 0

    def test_no_duplicates(self):
        text = '"code.py" is important. Also see "code.py" again.'
        paths = extract_local_paths(text)
        assert paths.count("code.py") == 1

    def test_returns_empty_for_no_paths(self):
        text = "Just some text with no file references."
        assert extract_local_paths(text) == []

    def test_multiple_different_files(self):
        text = '"a.py" and "b.ipynb" and "c.md"'
        paths = extract_local_paths(text)
        assert "a.py" in paths
        assert "b.ipynb" in paths
        assert "c.md" in paths


# ---------------------------------------------------------------------------
# extract_urls_by_section
# ---------------------------------------------------------------------------


class TestExtractUrlsBySection:
    def test_other_sources_are_exploitation(self):
        text = (
            "## Other Sources\n"
            "1. [IBM](https://www.ibm.com/article)\n"
            "2. [ArXiv](https://arxiv.org/abs/1234)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://www.ibm.com/article" in result["exploitation"]
        assert "https://arxiv.org/abs/1234" in result["exploitation"]
        assert result["golden"] == []

    def test_golden_sources_are_golden(self):
        text = (
            "## Golden Sources\n"
            "1. [YouTube](https://youtube.com/watch?v=abc)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://youtube.com/watch?v=abc" in result["golden"]
        assert result["exploitation"] == []

    def test_article_code_is_golden(self):
        text = (
            "## Article Code\n"
            "1. [Notebook](https://github.com/owner/repo)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://github.com/owner/repo" in result["golden"]
        assert result["exploitation"] == []

    def test_lesson_code_is_golden(self):
        text = (
            "## Lesson Code\n"
            "1. [Notebook](https://github.com/owner/repo2)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://github.com/owner/repo2" in result["golden"]
        assert result["exploitation"] == []

    def test_mixed_sections(self):
        text = (
            "## Golden Sources\n"
            "1. [Gold](https://golden.example.com)\n"
            "## Other Sources\n"
            "1. [Other](https://other.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://golden.example.com" in result["golden"]
        assert "https://other.example.com" in result["exploitation"]

    def test_urls_before_any_section_are_golden(self):
        text = (
            "Intro text with https://intro.example.com\n"
            "## Other Sources\n"
            "1. [Other](https://other.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://intro.example.com" in result["golden"]
        assert "https://other.example.com" in result["exploitation"]

    def test_unknown_section_defaults_to_golden(self):
        text = (
            "## References\n"
            "1. [Ref](https://ref.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://ref.example.com" in result["golden"]

    def test_empty_text_returns_empty_lists(self):
        result = extract_urls_by_section("")
        assert result["golden"] == []
        assert result["exploitation"] == []

    def test_other_sources_case_insensitive(self):
        text = "## OTHER SOURCES\n1. [X](https://x.example.com)\n"
        result = extract_urls_by_section(text)
        assert "https://x.example.com" in result["exploitation"]
