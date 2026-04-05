"""
Unit tests for src/utils/markdown_utils.py.

All functions are pure (no I/O, no LLM) so no mocking is required.
"""

import pytest

from src.utils.markdown_utils import (
    build_research_results_section,
    build_sources_section,
    combine_research_sections,
    get_first_line_title,
    markdown_collapsible,
)


# ---------------------------------------------------------------------------
# markdown_collapsible
# ---------------------------------------------------------------------------

class TestMarkdownCollapsible:
    def test_contains_details_tag(self):
        result = markdown_collapsible("My Title", "Some body")
        assert "<details>" in result
        assert "</details>" in result

    def test_contains_summary_tag_with_title(self):
        result = markdown_collapsible("My Title", "Some body")
        assert "<summary>My Title</summary>" in result

    def test_contains_body_text(self):
        result = markdown_collapsible("T", "Hello world")
        assert "Hello world" in result

    def test_body_whitespace_is_stripped(self):
        result = markdown_collapsible("T", "   padded   ")
        assert "padded" in result
        # Leading/trailing whitespace on the raw body string should be removed
        assert "   padded   " not in result

    def test_empty_body_still_renders(self):
        result = markdown_collapsible("Title", "")
        assert "<summary>Title</summary>" in result
        assert "<details>" in result

    def test_multiline_body_preserved(self):
        body = "Line 1\nLine 2\nLine 3"
        result = markdown_collapsible("T", body)
        assert "Line 1" in result
        assert "Line 3" in result


# ---------------------------------------------------------------------------
# get_first_line_title
# ---------------------------------------------------------------------------

class TestGetFirstLineTitle:
    def test_strips_single_hash(self):
        assert get_first_line_title("# My Title\n\nSome content") == "My Title"

    def test_strips_double_hash(self):
        assert get_first_line_title("## Section\nContent") == "Section"

    def test_strips_triple_hash(self):
        assert get_first_line_title("### Sub\nContent") == "Sub"

    def test_returns_plain_first_line_without_hash(self):
        assert get_first_line_title("Plain Title\n\nContent") == "Plain Title"

    def test_empty_string_returns_untitled(self):
        assert get_first_line_title("") == "Untitled"

    def test_whitespace_only_returns_untitled(self):
        assert get_first_line_title("   \n   \n  ") == "Untitled"

    def test_leading_empty_lines_skipped(self):
        assert get_first_line_title("\n\n# Actual Title") == "Actual Title"

    def test_hash_only_returns_untitled(self):
        # A line with only '#' and nothing else → empty after lstrip → "Untitled"
        assert get_first_line_title("#\n") == "Untitled"

    def test_title_with_trailing_whitespace_stripped(self):
        result = get_first_line_title("# Title With Spaces   ")
        assert result == "Title With Spaces"


# ---------------------------------------------------------------------------
# build_research_results_section
# ---------------------------------------------------------------------------

class TestBuildResearchResultsSection:
    def test_contains_section_header(self):
        result = build_research_results_section({})
        assert "## Research Results" in result

    def test_empty_input_shows_no_results_message(self):
        result = build_research_results_section({})
        assert "_No accepted research results found._" in result

    def test_single_query_appears_in_output(self):
        result = build_research_results_section({"What is RAG?": ["Result block"]})
        assert "What is RAG?" in result
        assert "Result block" in result

    def test_multiple_result_blocks_per_query(self):
        result = build_research_results_section({"Q": ["Block A", "Block B"]})
        assert "Block A" in result
        assert "Block B" in result

    def test_multiple_queries_all_present(self):
        grouped = {"Q1": ["R1"], "Q2": ["R2"], "Q3": ["R3"]}
        result = build_research_results_section(grouped)
        for key in grouped:
            assert key in result

    def test_result_is_string(self):
        result = build_research_results_section({"Q": ["R"]})
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# build_sources_section
# ---------------------------------------------------------------------------

class TestBuildSourcesSection:
    def test_section_title_present(self):
        result = build_sources_section("## Code Sources", [], "No code")
        assert "## Code Sources" in result

    def test_empty_sources_shows_empty_message(self):
        result = build_sources_section("## My Sources", [], "Nothing here")
        assert "_Nothing here_" in result

    def test_single_source_title_and_body_present(self):
        result = build_sources_section(
            "## Sources", [("Source One", "Content one")], "empty"
        )
        assert "Source One" in result
        assert "Content one" in result

    def test_multiple_sources_all_present(self):
        sources = [("S1", "C1"), ("S2", "C2"), ("S3", "C3")]
        result = build_sources_section("## S", sources, "none")
        for title, body in sources:
            assert title in result
            assert body in result

    def test_returns_string(self):
        result = build_sources_section("## T", [("A", "B")], "x")
        assert isinstance(result, str)


# ---------------------------------------------------------------------------
# combine_research_sections
# ---------------------------------------------------------------------------

class TestCombineResearchSections:
    def test_contains_research_title(self):
        result = combine_research_sections("S1", "S2", "S3", "S4", "S5")
        assert "# Research" in result

    def test_all_sections_present(self):
        sections = ("Research Results", "Sources", "Code", "YouTube", "Additional")
        result = combine_research_sections(*sections)
        for section in sections:
            assert section in result

    def test_sections_joined_by_double_newline(self):
        result = combine_research_sections("A", "B", "C", "D", "E")
        assert "\n\n" in result

    def test_returns_string(self):
        result = combine_research_sections("a", "b", "c", "d", "e")
        assert isinstance(result, str)

    def test_local_files_section_included_when_provided(self):
        result = combine_research_sections("S1", "S2", "S3", "S4", "S5", local_files_section="Local Files Content")
        assert "Local Files Content" in result

    def test_local_files_section_omitted_when_empty(self):
        result = combine_research_sections("S1", "S2", "S3", "S4", "S5", local_files_section="")
        assert result == combine_research_sections("S1", "S2", "S3", "S4", "S5")

    def test_default_local_files_section_is_empty(self):
        """Calling without local_files_section should behave like the original 5-section version."""
        result = combine_research_sections("A", "B", "C", "D", "E")
        # Should have exactly 6 parts joined (title + 5 sections)
        assert result.count("\n\n") == 5
