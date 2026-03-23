"""
Unit tests for deterministic helper functions used in query generation and
deduplication.  No LLM calls are made – all functions under test are either
pure or perform simple file I/O.

Covered functions
-----------------
From ``src/tools/generate_next_queries_tool.py``:
    write_queries_to_file
    format_queries_for_display

From ``src/app/generate_queries_handler.py``:
    compute_next_query_id
    append_generated_queries_with_reasons

From ``src/app/dedup_new_queries_handler.py``:
    parse_queries_from_file
    format_dedup_prompt_inputs
"""

import pytest
from pathlib import Path
from typing import List, Tuple

# We import directly from the module files to bypass src/tools/__init__.py,
# which would attempt to import all tool modules (heavy transitive deps).
from src.app.dedup_new_queries_handler import (
    format_dedup_prompt_inputs,
    parse_queries_from_file,
)
from src.app.generate_queries_handler import (
    append_generated_queries_with_reasons,
    compute_next_query_id,
)
from src.tools.generate_next_queries_tool import (
    format_queries_for_display,
    write_queries_to_file,
)

# Shared sample data
_SAMPLE: List[Tuple[str, str]] = [
    ("What is RAG?", "Covers the basics of retrieval-augmented generation."),
    ("How does dense retrieval work?", "Explains the vector similarity mechanism."),
]


# ---------------------------------------------------------------------------
# write_queries_to_file
# ---------------------------------------------------------------------------

class TestWriteQueriesToFile:
    def test_file_is_created(self, tmp_path: Path):
        p = tmp_path / "next_queries.md"
        write_queries_to_file(p, _SAMPLE)
        assert p.exists()

    def test_file_has_section_header(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, _SAMPLE)
        assert "Candidate Web-Search Queries" in p.read_text(encoding="utf-8")

    def test_all_query_texts_present(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, _SAMPLE)
        content = p.read_text(encoding="utf-8")
        for query, _ in _SAMPLE:
            assert query in content

    def test_all_reasons_present(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, _SAMPLE)
        content = p.read_text(encoding="utf-8")
        for _, reason in _SAMPLE:
            assert reason in content

    def test_queries_are_numbered_starting_at_one(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, _SAMPLE)
        content = p.read_text(encoding="utf-8")
        assert "1." in content
        assert "2." in content

    def test_empty_list_writes_header_only(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, [])
        content = p.read_text(encoding="utf-8")
        assert "Candidate Web-Search Queries" in content

    def test_overwrites_existing_content(self, tmp_path: Path):
        p = tmp_path / "q.md"
        p.write_text("old content that should vanish", encoding="utf-8")
        write_queries_to_file(p, [("New query", "New reason")])
        content = p.read_text(encoding="utf-8")
        assert "old content" not in content
        assert "New query" in content

    def test_reasons_prefixed_with_reason_label(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, [("Q?", "My reason")])
        content = p.read_text(encoding="utf-8")
        assert "Reason: My reason" in content

    def test_file_written_with_utf8(self, tmp_path: Path):
        p = tmp_path / "q.md"
        write_queries_to_file(p, [("Naïve question?", "Résumé reason")])
        # If encoding is wrong this read would fail or produce garbage
        content = p.read_text(encoding="utf-8")
        assert "Naïve" in content


# ---------------------------------------------------------------------------
# format_queries_for_display
# ---------------------------------------------------------------------------

class TestFormatQueriesForDisplay:
    def test_empty_list_returns_empty_string(self):
        assert format_queries_for_display([]) == ""

    def test_single_query_formatted_correctly(self):
        result = format_queries_for_display([("My Q?", "My reason")])
        assert "1. My Q?" in result
        assert "Reason: My reason" in result

    def test_multiple_queries_all_numbered(self):
        result = format_queries_for_display(_SAMPLE)
        assert "1. What is RAG?" in result
        assert "2. How does dense retrieval work?" in result

    def test_queries_separated_by_double_newline(self):
        result = format_queries_for_display(_SAMPLE)
        assert "\n\n" in result

    def test_returns_string(self):
        assert isinstance(format_queries_for_display(_SAMPLE), str)

    def test_five_queries_numbered_1_to_5(self):
        queries = [(f"Q{i}", f"R{i}") for i in range(1, 6)]
        result = format_queries_for_display(queries)
        for i in range(1, 6):
            assert f"{i}. Q{i}" in result


# ---------------------------------------------------------------------------
# compute_next_query_id
# ---------------------------------------------------------------------------

class TestComputeNextQueryId:
    def test_returns_1_for_nonexistent_file(self, tmp_path: Path):
        assert compute_next_query_id(tmp_path / "missing.md") == 1

    def test_returns_1_for_empty_file(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("", encoding="utf-8")
        assert compute_next_query_id(f) == 1

    def test_returns_1_for_file_with_no_query_ids(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("Some text without any query IDs\n", encoding="utf-8")
        assert compute_next_query_id(f) == 1

    def test_reads_legacy_format(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("Query [5]: What is RAG?\n\nReason: test\n\n-----\n\n", encoding="utf-8")
        assert compute_next_query_id(f) == 6

    def test_reads_exploitation_tag_format(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("Query [12] [Exploitation]: Some query\n\nReason: test\n", encoding="utf-8")
        assert compute_next_query_id(f) == 13

    def test_reads_exploration_tag_format(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("Query [7] [Exploration]: Another query\n\n", encoding="utf-8")
        assert compute_next_query_id(f) == 8

    def test_returns_max_id_plus_one(self, tmp_path: Path):
        f = tmp_path / "q.md"
        content = (
            "Query [3] [Exploitation]: Third\n\n"
            "Query [1] [Exploitation]: First\n\n"
            "Query [7] [Exploration]:  Seventh\n\n"
        )
        f.write_text(content, encoding="utf-8")
        assert compute_next_query_id(f) == 8

    def test_id_not_at_line_start_still_found(self, tmp_path: Path):
        # Robustness: .search() is used, so id can appear anywhere on the line
        f = tmp_path / "q.md"
        f.write_text("  Query [9] [Exploitation]: Indented\n", encoding="utf-8")
        assert compute_next_query_id(f) == 10


# ---------------------------------------------------------------------------
# append_generated_queries_with_reasons
# ---------------------------------------------------------------------------

class TestAppendGeneratedQueriesWithReasons:
    def test_creates_file_if_not_exists(self, tmp_path: Path):
        f = tmp_path / "full.md"
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="exploitation")
        assert f.exists()

    def test_exploitation_tag_present(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="exploitation")
        assert "[Exploitation]" in f.read_text(encoding="utf-8")

    def test_exploration_tag_for_complementary(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="complementary")
        assert "[Exploration]" in f.read_text(encoding="utf-8")

    def test_ids_start_at_given_starting_id(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=10, query_source="exploitation")
        content = f.read_text(encoding="utf-8")
        assert "Query [10]" in content
        assert "Query [11]" in content

    def test_ids_are_sequential(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        queries = [(f"Q{i}", f"R{i}") for i in range(3)]
        append_generated_queries_with_reasons(f, queries, starting_id=1, query_source="exploitation")
        content = f.read_text(encoding="utf-8")
        assert "Query [1]" in content
        assert "Query [2]" in content
        assert "Query [3]" in content

    def test_returns_next_available_id(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        next_id = append_generated_queries_with_reasons(
            f, _SAMPLE, starting_id=5, query_source="exploitation"
        )
        # 2 queries starting at 5 → next id = 7
        assert next_id == 7

    def test_appends_does_not_overwrite_existing(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("Existing content\n\n", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="exploitation")
        content = f.read_text(encoding="utf-8")
        assert "Existing content" in content

    def test_all_query_texts_written(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="exploitation")
        content = f.read_text(encoding="utf-8")
        for query, reason in _SAMPLE:
            assert query in content
            assert reason in content

    def test_separator_between_entries(self, tmp_path: Path):
        f = tmp_path / "full.md"
        f.write_text("", encoding="utf-8")
        append_generated_queries_with_reasons(f, _SAMPLE, starting_id=1, query_source="exploitation")
        assert "-----" in f.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# parse_queries_from_file
# ---------------------------------------------------------------------------

class TestParseQueriesFromFile:
    def test_returns_empty_list_for_nonexistent_file(self, tmp_path: Path):
        result = parse_queries_from_file(tmp_path / "missing.md")
        assert result == []

    def test_returns_empty_list_for_empty_file(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("", encoding="utf-8")
        assert parse_queries_from_file(f) == []

    def test_parses_basic_numbered_format(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text(
            "1. What is RAG?\nReason: Fills a gap.\n\n"
            "2. How does it work?\nReason: Technical details.\n",
            encoding="utf-8",
        )
        queries = parse_queries_from_file(f)
        assert len(queries) == 2
        assert queries[0] == ("What is RAG?", "Fills a gap.")
        assert queries[1] == ("How does it work?", "Technical details.")

    def test_returns_list_of_tuples(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("1. Q?\nReason: R\n", encoding="utf-8")
        result = parse_queries_from_file(f)
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    def test_ignores_non_query_header_lines(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text(
            "### Candidate Queries\n\n1. My query?\nReason: Because.\n",
            encoding="utf-8",
        )
        queries = parse_queries_from_file(f)
        assert len(queries) == 1
        assert queries[0][0] == "My query?"

    def test_parses_multi_line_reason(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text(
            "1. My query?\nReason: First part.\nSecond part of reason.\n",
            encoding="utf-8",
        )
        queries = parse_queries_from_file(f)
        assert len(queries) == 1
        assert "First part." in queries[0][1]
        assert "Second part of reason." in queries[0][1]

    def test_five_queries_parsed(self, tmp_path: Path):
        lines = "\n\n".join(
            f"{i}. Question {i}?\nReason: Reason {i}." for i in range(1, 6)
        )
        f = tmp_path / "q.md"
        f.write_text(lines, encoding="utf-8")
        queries = parse_queries_from_file(f)
        assert len(queries) == 5

    def test_query_text_stripped_of_dot_prefix(self, tmp_path: Path):
        f = tmp_path / "q.md"
        f.write_text("1. The actual question?\nReason: Why.\n", encoding="utf-8")
        queries = parse_queries_from_file(f)
        # Should NOT include the "1. " prefix
        assert queries[0][0] == "The actual question?"


# ---------------------------------------------------------------------------
# format_dedup_prompt_inputs
# ---------------------------------------------------------------------------

class TestFormatDedupPromptInputs:
    def test_includes_query_source_exploitation(self):
        result = format_dedup_prompt_inputs([("Q1", "R1")], "history content", "exploitation")
        assert "exploitation" in result

    def test_includes_query_source_complementary(self):
        result = format_dedup_prompt_inputs([("Q1", "R1")], "history", "complementary")
        assert "complementary" in result

    def test_includes_history_text(self):
        result = format_dedup_prompt_inputs([("Q1", "R1")], "my historical context", "exploitation")
        assert "my historical context" in result

    def test_includes_new_query_text(self):
        result = format_dedup_prompt_inputs([("What is RAG?", "Basics")], "history", "exploitation")
        assert "What is RAG?" in result

    def test_includes_new_query_reason(self):
        result = format_dedup_prompt_inputs([("Q?", "Cover the gap")], "history", "exploitation")
        assert "Cover the gap" in result

    def test_empty_history_replaced_with_placeholder(self):
        result = format_dedup_prompt_inputs([("Q", "R")], "", "exploitation")
        assert "<none>" in result

    def test_none_history_replaced_with_placeholder(self):
        # ``read_file_safe`` can return "" but the handler might receive None in edge cases
        result = format_dedup_prompt_inputs([("Q", "R")], None, "exploitation")  # type: ignore[arg-type]
        assert "<none>" in result

    def test_multiple_queries_all_present(self):
        queries = [("Q1", "R1"), ("Q2", "R2"), ("Q3", "R3")]
        result = format_dedup_prompt_inputs(queries, "history", "exploitation")
        for q, _ in queries:
            assert q in result

    def test_returns_string(self):
        result = format_dedup_prompt_inputs([("Q", "R")], "h", "exploitation")
        assert isinstance(result, str)
