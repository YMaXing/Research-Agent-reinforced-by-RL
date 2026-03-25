"""Unit tests for src/app/guideline_extractions_handler.py.

Both ``extract_urls`` and ``extract_local_paths`` are pure functions —
no LLM mocking or file I/O is required.
"""

import pytest

from src.app.guideline_extractions_handler import extract_local_paths, extract_urls


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
