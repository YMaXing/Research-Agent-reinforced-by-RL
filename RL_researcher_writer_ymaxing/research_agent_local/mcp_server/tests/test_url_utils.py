"""Unit tests for src/utils/url_utils.py.

``normalize_url_for_match`` is a pure function — no I/O or mocking required.
"""

from src.utils.url_utils import normalize_url_for_match


class TestNormalizeUrlForMatch:
    def test_empty_and_none_like(self):
        assert normalize_url_for_match("") == ""
        assert normalize_url_for_match("   ") == ""

    def test_strips_scheme_and_www(self):
        assert normalize_url_for_match("https://www.example.com/page") == "example.com/page"
        assert normalize_url_for_match("http://example.com/page") == "example.com/page"

    def test_http_and_https_match(self):
        assert normalize_url_for_match("http://example.com/x") == normalize_url_for_match(
            "https://example.com/x"
        )

    def test_trailing_slash_and_fragment_ignored(self):
        a = normalize_url_for_match("https://example.com/path/")
        b = normalize_url_for_match("https://example.com/path#section")
        assert a == b == "example.com/path"

    def test_arxiv_abs_and_pdf_match(self):
        abs_url = normalize_url_for_match("https://arxiv.org/abs/2205.12293")
        pdf_url = normalize_url_for_match("https://arxiv.org/pdf/2205.12293")
        assert abs_url == pdf_url == "arxiv.org/abs/2205.12293"

    def test_arxiv_version_suffix_ignored(self):
        assert (
            normalize_url_for_match("https://arxiv.org/pdf/2205.12293v2")
            == "arxiv.org/abs/2205.12293"
        )

    def test_arxiv_pdf_extension_ignored(self):
        assert (
            normalize_url_for_match("https://arxiv.org/pdf/2505.10410.pdf")
            == "arxiv.org/abs/2505.10410"
        )

    def test_non_arxiv_pdf_suffix_stripped(self):
        assert normalize_url_for_match("https://example.com/paper.pdf") == "example.com/paper"

    def test_query_string_preserved(self):
        assert (
            normalize_url_for_match("https://youtube.com/watch?v=abc123")
            == "youtube.com/watch?v=abc123"
        )

    def test_angle_brackets_stripped(self):
        assert (
            normalize_url_for_match("<https://arxiv.org/abs/2205.12293>")
            == "arxiv.org/abs/2205.12293"
        )
