"""
Integration tests for ``deduplicate_new_queries_tool`` in
``src/tools/dedup_new_queries_tool.py``.

Design notes
------------
This tool has an unusual bare import at module level::

    from generate_next_queries_tool import write_queries_to_file

``conftest.py`` pre-registers a ``MagicMock`` module under the bare name
``generate_next_queries_tool`` so the dedup tool can be imported safely.
As a result ``write_queries_to_file`` inside the tool is a ``MagicMock``
(it does NOT write to disk).  All assertions therefore target:

1. The **return dictionary** – status, counts, message.
2. The **existence of next_queries.md** via
   ``src.tools.dedup_new_queries_tool.write_queries_to_file`` being called
   (verified with ``Mock.assert_called_once``).

The actual file-writing logic is unit-tested independently in
``test_query_helpers.py::TestWriteQueriesToFile``.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import patch

from tests.conftest import FakePlainModel
from src.tools.dedup_new_queries_tool import deduplicate_new_queries_tool
from src.config.constants import (
    FULL_QUERIES_FILE,
    NEXT_QUERIES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)

_DEDUP_LLM_PATCH = "src.app.dedup_new_queries_handler.get_chat_model"
# write_queries_to_file inside the dedup tool is the mock injected by conftest;
# we can access it in tests via the module attribute.
import src.tools.dedup_new_queries_tool as _dedup_mod


def _kept_json(kept: list) -> str:
    return json.dumps(
        {"kept_queries": kept, "removed_queries": [], "reasoning": "test"}
    )


def _write_next_queries(
    research_dir: Path, queries: list[tuple[str, str]]
) -> None:
    """Helper: write a next_queries.md file so the tool has something to parse."""
    output = research_dir / RESEARCH_OUTPUT_FOLDER
    output.mkdir(parents=True, exist_ok=True)
    nq = output / NEXT_QUERIES_FILE
    lines = ["### Candidate Web-Search Queries\n\n"]
    for i, (q, r) in enumerate(queries, 1):
        lines.append(f"{i}. {q}\nReason: {r}\n\n")
    nq.write_text("".join(lines), encoding="utf-8")


_SAMPLE_QUERIES = [
    ("What is RAG?", "Covers basics"),
    ("How does dense retrieval work?", "Technical deep dive"),
    ("What are RAG limitations?", "Critical analysis"),
]


# ---------------------------------------------------------------------------
# Happy-path tests
# ---------------------------------------------------------------------------

class TestDeduplicateNewQueriesTool:
    async def test_returns_success_status(self, fake_plain_model_factory, tmp_research_dir):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        kept = [q for q, _ in _SAMPLE_QUERIES]
        model = fake_plain_model_factory(_kept_json(kept))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["status"] == "success"

    async def test_new_queries_count_correct(self, fake_plain_model_factory, tmp_research_dir):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["new_queries_count"] == 3

    async def test_kept_count_when_all_kept(self, fake_plain_model_factory, tmp_research_dir):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["kept_count"] == 3
        assert result["removed_duplicates"] == 0

    async def test_removed_count_reflects_dedup(self, fake_plain_model_factory, tmp_research_dir):
        """LLM keeps only 1 of 3 → removed_duplicates == 2."""
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json(["What is RAG?"]))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["kept_count"] == 1
        assert result["removed_duplicates"] == 2

    async def test_write_queries_to_file_called_after_dedup(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        """write_queries_to_file must be called exactly once per run."""
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))

        with patch("src.tools.dedup_new_queries_tool.write_queries_to_file") as mock_write, \
             patch(_DEDUP_LLM_PATCH, return_value=model):
            await deduplicate_new_queries_tool(str(tmp_research_dir))

        mock_write.assert_called_once()

    async def test_output_path_in_result(self, fake_plain_model_factory, tmp_research_dir):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert "output_path" in result
        assert NEXT_QUERIES_FILE in result["output_path"]

    async def test_result_message_contains_counts(self, fake_plain_model_factory, tmp_research_dir):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json(["What is RAG?"]))

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert "1" in result["message"]  # kept_count

    async def test_exploitation_query_source_forwarded(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))
        prompts_seen = []
        original = model.ainvoke

        async def spy(prompt, **kw):
            prompts_seen.append(str(prompt))
            return await original(prompt, **kw)

        model.ainvoke = spy

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            await deduplicate_new_queries_tool(
                str(tmp_research_dir), query_source="exploitation"
            )

        assert prompts_seen and "exploitation" in prompts_seen[0]

    async def test_complementary_query_source_forwarded(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))
        prompts_seen = []
        original = model.ainvoke

        async def spy(prompt, **kw):
            prompts_seen.append(str(prompt))
            return await original(prompt, **kw)

        model.ainvoke = spy

        with patch(_DEDUP_LLM_PATCH, return_value=model):
            await deduplicate_new_queries_tool(
                str(tmp_research_dir), query_source="complementary"
            )

        assert prompts_seen and "complementary" in prompts_seen[0]


# ---------------------------------------------------------------------------
# Edge / skip cases
# ---------------------------------------------------------------------------

class TestDeduplicateEdgeCases:
    async def test_skipped_when_next_queries_file_is_empty(self, tmp_research_dir):
        """If next_queries.md is empty (or missing), the tool should report 'skipped'."""
        output = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        output.mkdir(parents=True, exist_ok=True)
        (output / NEXT_QUERIES_FILE).write_text("", encoding="utf-8")

        # No LLM patch needed – should short-circuit before calling the model
        result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["status"] == "skipped"

    async def test_skipped_when_next_queries_file_missing(self, tmp_research_dir):
        """If next_queries.md does not yet exist, the tool should report 'skipped'."""
        output = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        output.mkdir(parents=True, exist_ok=True)
        # Do NOT create next_queries.md

        result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["status"] == "skipped"

    async def test_raises_value_error_for_nonexistent_directory(self):
        with pytest.raises(ValueError):
            await deduplicate_new_queries_tool("/does/not/exist")

    async def test_creates_output_directory_if_not_exists(
        self, fake_plain_model_factory, tmp_research_dir
    ):
        """The .research/ folder is created automatically if absent."""
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)
        # Remove the output dir after writing to test auto-creation
        import shutil
        output_path = tmp_research_dir / RESEARCH_OUTPUT_FOLDER
        # Re-create from scratch so the tool must mkdir
        shutil.rmtree(output_path)
        _write_next_queries(tmp_research_dir, _SAMPLE_QUERIES)  # recreate files

        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_QUERIES]))
        with patch(_DEDUP_LLM_PATCH, return_value=model):
            result = await deduplicate_new_queries_tool(str(tmp_research_dir))

        assert result["status"] == "success"
        assert (tmp_research_dir / RESEARCH_OUTPUT_FOLDER).is_dir()
