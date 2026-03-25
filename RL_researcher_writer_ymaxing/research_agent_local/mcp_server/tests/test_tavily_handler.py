"""Unit tests for src/app/tavily_handler.py.

Pure-function tests (no LLM/API calls) for:
  - ``compute_next_source_id``
  - ``append_tavily_results``
  - ``extract_tavily_chunks``
  - ``group_tavily_by_query``

``run_tavily_search`` involves a real LLM + Tavily and is tested at the tool
layer with full mocking; here we only test the deterministic helpers.
"""

import pytest
from pathlib import Path

from src.app.tavily_handler import (
    append_tavily_results,
    compute_next_source_id,
    extract_tavily_chunks,
    group_tavily_by_query,
)


# ---------------------------------------------------------------------------
# compute_next_source_id
# ---------------------------------------------------------------------------


class TestComputeNextSourceId:
    def test_returns_1_for_missing_file(self, tmp_path):
        assert compute_next_source_id(tmp_path / "missing.md") == 1

    def test_returns_1_for_empty_file(self, tmp_path):
        f = tmp_path / "empty.md"
        f.write_text("", encoding="utf-8")
        assert compute_next_source_id(f) == 1

    def test_returns_next_after_existing_ids(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text(
            "### Source [1]: https://a.com\nstuff\n\n"
            "### Source [3]: https://b.com\nmore\n",
            encoding="utf-8",
        )
        assert compute_next_source_id(f) == 4

    def test_handles_single_source(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text("### Source [5]: https://x.com\n", encoding="utf-8")
        assert compute_next_source_id(f) == 6


# ---------------------------------------------------------------------------
# append_tavily_results
# ---------------------------------------------------------------------------


class TestAppendTavilyResults:
    def test_appends_single_source(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text("", encoding="utf-8")

        next_id = append_tavily_results(
            f,
            query="What is RAG?",
            answer_by_source={1: "RAG is retrieval-augmented generation."},
            citations={1: "https://rag.example.com"},
            starting_id=1,
            phase="[EXPLOITATION]",
        )

        content = f.read_text(encoding="utf-8")
        assert "### Source [1]: https://rag.example.com" in content
        assert "Query: What is RAG?" in content
        assert "Phase: [EXPLOITATION]" in content
        assert next_id == 2

    def test_appends_multiple_sources(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text("", encoding="utf-8")

        next_id = append_tavily_results(
            f,
            query="test",
            answer_by_source={1: "answer A", 2: "answer B"},
            citations={1: "https://a.com", 2: "https://b.com"},
            starting_id=10,
        )

        content = f.read_text(encoding="utf-8")
        assert "### Source [10]:" in content
        assert "### Source [11]:" in content
        assert next_id == 12

    def test_skips_empty_answers(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text("", encoding="utf-8")

        next_id = append_tavily_results(
            f,
            query="test",
            answer_by_source={1: "", 2: "real answer"},
            citations={1: "https://a.com", 2: "https://b.com"},
            starting_id=1,
        )

        content = f.read_text(encoding="utf-8")
        assert "### Source [1]:" in content
        assert "real answer" in content
        # empty answer skipped, so next_id only incremented once
        assert next_id == 2

    def test_exploration_phase_tag(self, tmp_path):
        f = tmp_path / "results.md"
        f.write_text("", encoding="utf-8")

        append_tavily_results(
            f,
            query="q",
            answer_by_source={1: "a"},
            citations={1: "https://x.com"},
            starting_id=1,
            phase="[EXPLORATION]",
        )
        content = f.read_text(encoding="utf-8")
        assert "Phase: [EXPLORATION]" in content


# ---------------------------------------------------------------------------
# extract_tavily_chunks
# ---------------------------------------------------------------------------

_SAMPLE_MD = """\
Phase: [EXPLOITATION]

### Source [1]: https://a.com

Query: What is RAG?

Answer: RAG uses retrieval.

-----

Phase: [EXPLORATION]

### Source [2]: https://b.com

Query: How does dense retrieval work?

Answer: Dense retrieval uses embeddings.

-----
"""


class TestExtractTavilyChunks:
    def test_extracts_correct_number(self):
        chunks = extract_tavily_chunks(_SAMPLE_MD)
        assert len(chunks) == 2
        assert 1 in chunks
        assert 2 in chunks

    def test_chunk_content(self):
        chunks = extract_tavily_chunks(_SAMPLE_MD)
        assert "https://a.com" in chunks[1]
        assert "dense retrieval" in chunks[2]

    def test_empty_input(self):
        assert extract_tavily_chunks("") == {}

    def test_no_phase_prefix(self):
        md = (
            "### Source [1]: https://a.com\n\n"
            "Query: q\n\n"
            "Answer: a\n\n-----\n"
        )
        chunks = extract_tavily_chunks(md)
        assert 1 in chunks


# ---------------------------------------------------------------------------
# group_tavily_by_query
# ---------------------------------------------------------------------------


class TestGroupTavilyByQuery:
    def test_groups_by_query_string(self):
        chunks = extract_tavily_chunks(_SAMPLE_MD)
        grouped = group_tavily_by_query(chunks, [1, 2])
        assert len(grouped) == 2
        assert "What is RAG?" in grouped

    def test_selected_ids_filter(self):
        chunks = extract_tavily_chunks(_SAMPLE_MD)
        grouped = group_tavily_by_query(chunks, [1])
        assert len(grouped) == 1

    def test_missing_id_ignored(self):
        chunks = extract_tavily_chunks(_SAMPLE_MD)
        grouped = group_tavily_by_query(chunks, [999])
        assert len(grouped) == 0
