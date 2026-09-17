"""Unit tests for src/app/guideline_extractions_handler.py.

Both ``extract_urls`` and ``extract_local_paths`` are pure functions —
no LLM mocking or file I/O is required.
``extract_urls_by_section`` is also pure and tested here.
"""

import pytest

from src.app.guideline_extractions_handler import (
    extract_local_file_reference_urls,
    extract_local_paths,
    extract_urls,
    extract_urls_by_section,
    load_reference_url_blocklist,
)
from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)


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

    def test_ignores_image_url_wrapped_in_backticks(self):
        text = "Include the diagram: `https://example.com/assets/diagram.png`"
        assert extract_urls(text) == []

    def test_backtick_wrapped_non_image_url_is_captured_cleanly(self):
        text = "See `https://example.com/docs/guide` for details."
        urls = extract_urls(text)
        assert urls == ["https://example.com/docs/guide"]


# ---------------------------------------------------------------------------
# extract_local_paths
# ---------------------------------------------------------------------------


class TestExtractLocalPaths:
    def test_extracts_quoted_python_file(self):
        text = 'Reference the file below for details.\n"src/main.py"'
        paths = extract_local_paths(text)
        assert "src/main.py" in paths

    def test_extracts_quoted_notebook(self):
        text = 'Open the file below to see the results.\n"analysis.ipynb"'
        paths = extract_local_paths(text)
        assert "analysis.ipynb" in paths

    def test_extracts_quoted_markdown_file(self):
        text = 'See the file below for instructions.\n"docs/guide.md"'
        paths = extract_local_paths(text)
        assert "docs/guide.md" in paths

    def test_ignores_quoted_urls(self):
        text = 'See "https://example.com/file.py" for info.'
        paths = extract_local_paths(text)
        assert len(paths) == 0

    def test_extracts_standalone_filename(self):
        text = 'Check the file below for the entry point.\n"main.py"'
        paths = extract_local_paths(text)
        assert "main.py" in paths

    def test_ignores_unsupported_extensions(self):
        text = 'Open "data.csv" and "image.png" for data.'
        paths = extract_local_paths(text)
        assert len(paths) == 0

    def test_no_duplicates(self):
        text = '"code.py"\nSome text in between.\n"code.py"'
        paths = extract_local_paths(text)
        assert paths.count("code.py") == 1

    def test_returns_empty_for_no_paths(self):
        text = "Just some text with no file references."
        assert extract_local_paths(text) == []

    def test_multiple_different_files(self):
        text = '"a.py"\n"b.ipynb"\n"c.md"'
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

    def test_notebooks_section_is_golden(self):
        text = (
            "## Notebooks\n"
            "1. [Notebook](https://github.com/owner/repo3)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://github.com/owner/repo3" in result["golden"]
        assert result["exploitation"] == []

    def test_documentation_section_is_exploitation(self):
        text = (
            "## Documentation\n"
            "1. [Docs](https://docs.example.com/guide)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://docs.example.com/guide" in result["exploitation"]
        assert result["golden"] == []

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

    def test_urls_before_any_section_are_exploitation(self):
        text = (
            "Intro text with https://intro.example.com\n"
            "## Other Sources\n"
            "1. [Other](https://other.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://intro.example.com" in result["exploitation"]
        assert "https://other.example.com" in result["exploitation"]

    def test_unknown_section_defaults_to_exploitation(self):
        text = (
            "## References\n"
            "1. [Ref](https://ref.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert "https://ref.example.com" in result["exploitation"]
        assert result["golden"] == []

    def test_empty_text_returns_empty_lists(self):
        result = extract_urls_by_section("")
        assert result["golden"] == []
        assert result["exploitation"] == []

    def test_other_sources_case_insensitive(self):
        text = "## OTHER SOURCES\n1. [X](https://x.example.com)\n"
        result = extract_urls_by_section(text)
        assert "https://x.example.com" in result["exploitation"]

    def test_duplicate_url_within_same_section_is_deduplicated(self):
        text = (
            "## Golden Sources\n"
            "1. [Gold](https://golden.example.com)\n"
            "2. [Gold again](https://golden.example.com)\n"
        )
        result = extract_urls_by_section(text)
        assert result["golden"].count("https://golden.example.com") == 1

    def test_url_cited_in_body_and_listed_as_golden_is_golden_only(self):
        text = (
            "## Section 2 - Theory\n"
            "Quoting [source](https://youtube.com/watch?v=abc) here.\n"
            "## Golden Sources\n"
            "1. [Same source](https://youtube.com/watch?v=abc)\n"
        )
        result = extract_urls_by_section(text)
        assert result["golden"] == ["https://youtube.com/watch?v=abc"]
        assert result["exploitation"] == []


# ---------------------------------------------------------------------------
# extract_local_file_reference_urls
# ---------------------------------------------------------------------------


class TestExtractLocalFileReferenceUrls:
    def test_pairs_commented_url_with_local_file(self):
        text = (
            "## Golden Sources\n\n"
            "<!-- [Evolving Dark Sector](https://arxiv.org/abs/2205.12293) -->\n"
            '"Evolving Dark Sector and the Dark Dimension Scenario.md"\n'
        )
        urls = extract_local_file_reference_urls(text)
        assert urls == ["https://arxiv.org/abs/2205.12293"]

    def test_multiple_sections_collected(self):
        text = (
            "## Golden Sources\n\n"
            "<!-- [A](https://arxiv.org/abs/2205.12293) -->\n"
            '"A.md"\n\n'
            "## Other Sources\n\n"
            "<!-- [B](https://link.aps.org/doi/10.1103/9lf2-33zf) -->\n"
            '"B.md"\n'
        )
        urls = extract_local_file_reference_urls(text)
        assert "https://arxiv.org/abs/2205.12293" in urls
        assert "https://link.aps.org/doi/10.1103/9lf2-33zf" in urls

    def test_deduplicates_repeated_urls(self):
        text = (
            "<!-- [A](https://arxiv.org/abs/2205.12293) -->\n"
            '"A.md"\n\n'
            "<!-- [B](https://arxiv.org/abs/2205.12293) -->\n"
            '"B.md"\n'
        )
        urls = extract_local_file_reference_urls(text)
        assert urls == ["https://arxiv.org/abs/2205.12293"]

    def test_commented_url_without_local_file_is_ignored(self):
        text = (
            "<!-- [A](https://arxiv.org/abs/2205.12293) -->\n"
            "Some prose that is not a local file.\n"
        )
        assert extract_local_file_reference_urls(text) == []

    def test_uncommented_url_is_not_captured(self):
        text = (
            "[A](https://arxiv.org/abs/2205.12293)\n"
            '"A.md"\n'
        )
        assert extract_local_file_reference_urls(text) == []

    def test_returns_empty_for_no_matches(self):
        assert extract_local_file_reference_urls("just text") == []


# ---------------------------------------------------------------------------
# load_reference_url_blocklist
# ---------------------------------------------------------------------------


class TestLoadReferenceUrlBlocklist:
    def _make_dir(self, tmp_path):
        (tmp_path / RESEARCH_OUTPUT_FOLDER).mkdir()
        return tmp_path

    def test_reads_normalised_urls_from_json(self, tmp_path):
        self._make_dir(tmp_path)
        gf = tmp_path / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE
        gf.write_text(
            '{"local_file_reference_urls": ["https://arxiv.org/abs/2205.12293"]}',
            encoding="utf-8",
        )
        blocklist = load_reference_url_blocklist(str(tmp_path))
        assert "arxiv.org/abs/2205.12293" in blocklist

    def test_falls_back_to_guideline_when_key_missing(self, tmp_path):
        self._make_dir(tmp_path)
        gf = tmp_path / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE
        gf.write_text("{}", encoding="utf-8")
        (tmp_path / ARTICLE_GUIDELINE_FILE).write_text(
            "<!-- [A](https://arxiv.org/pdf/2205.12293v2) -->\n" '"A.md"\n',
            encoding="utf-8",
        )
        blocklist = load_reference_url_blocklist(str(tmp_path))
        # /pdf/…v2 must normalise to the same key as /abs/… (no version).
        assert "arxiv.org/abs/2205.12293" in blocklist

    def test_returns_empty_when_nothing_available(self, tmp_path):
        self._make_dir(tmp_path)
        assert load_reference_url_blocklist(str(tmp_path)) == set()
