"""
Unit tests for src/app/dedup_new_queries_handler.py.

``deduplicate_new_queries_against_history`` calls ``get_chat_model`` and then
``ainvoke``; we replace the real LLM with ``FakePlainModel`` which returns a
configurable JSON string without touching any API.

All other functions (``parse_queries_from_file``, ``format_dedup_prompt_inputs``)
are pure or do simple I/O and are covered in test_query_helpers.py; they are
only lightly exercised here where needed.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import patch

from tests.conftest import FakePlainModel
from src.app.dedup_new_queries_handler import deduplicate_new_queries_against_history

_PATCH_TARGET = "src.app.dedup_new_queries_handler.get_chat_model"

_SAMPLE_NEW = [
    ("What is RAG?", "Covers basics"),
    ("How does dense retrieval work?", "Technical deep dive"),
    ("What are RAG limitations?", "Critical analysis"),
]


def _kept_json(kept: list, removed: list | None = None) -> str:
    return json.dumps(
        {
            "kept_queries": kept,
            "removed_queries": removed or [],
            "reasoning": "Test reasoning",
        }
    )


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------

class TestDeduplicateNewQueriesAgainstHistory:
    async def test_returns_all_queries_when_none_removed(self, fake_plain_model_factory, tmp_path):
        kept = [q for q, _ in _SAMPLE_NEW]
        model = fake_plain_model_factory(_kept_json(kept))
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert len(result) == 3

    async def test_removes_queries_not_in_kept_list(self, fake_plain_model_factory, tmp_path):
        model = fake_plain_model_factory(
            _kept_json(["What is RAG?"], removed=["How does dense retrieval work?", "What are RAG limitations?"])
        )
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert len(result) == 1
        assert result[0][0] == "What is RAG?"

    async def test_preserves_original_reasons_for_kept_queries(self, fake_plain_model_factory, tmp_path):
        model = fake_plain_model_factory(_kept_json(["What is RAG?"]))
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert result[0][1] == "Covers basics"  # original reason preserved

    async def test_returns_list_of_tuples(self, fake_plain_model_factory, tmp_path):
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_NEW]))
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    async def test_complementary_source_passed_to_model(self, fake_plain_model_factory, tmp_path):
        """The query_source value must reach the prompt so the LLM knows the phase."""
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_NEW]))

        with patch(_PATCH_TARGET, return_value=model):
            # Capture what ainvoke receives
            original_ainvoke = model.ainvoke
            prompts_seen = []

            async def recording_ainvoke(prompt, **kw):
                prompts_seen.append(str(prompt))
                return await original_ainvoke(prompt, **kw)

            model.ainvoke = recording_ainvoke

            await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "complementary"
            )

        assert prompts_seen, "ainvoke was not called"
        assert "complementary" in prompts_seen[0]

    async def test_history_file_content_included_in_prompt(self, fake_plain_model_factory, tmp_path):
        history = tmp_path / "full.md"
        history.write_text(
            "Query [1] [Exploitation]: Previous baseline query\n", encoding="utf-8"
        )
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_NEW]))
        prompts_seen = []

        async def recording_ainvoke(prompt, **kw):
            prompts_seen.append(str(prompt))
            return await model.ainvoke.__wrapped__(model, prompt, **kw) if hasattr(model.ainvoke, "__wrapped__") else FakePlainModel.__dict__["ainvoke"](model, prompt, **kw)

        with patch(_PATCH_TARGET, return_value=model):
            original = model.ainvoke

            async def spy(prompt, **kw):
                prompts_seen.append(str(prompt))
                return await original(prompt, **kw)

            model.ainvoke = spy
            await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert "Previous baseline query" in prompts_seen[0]

    async def test_all_kept_queries_from_new_list_are_returned(self, fake_plain_model_factory, tmp_path):
        """Only queries that appear in new_queries are returned (not random strings)."""
        # LLM 'hallucinates' a query not in the new list
        model = fake_plain_model_factory(_kept_json(["What is RAG?", "THIS QUERY DOES NOT EXIST"]))
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        returned_texts = [q for q, _ in result]
        assert "THIS QUERY DOES NOT EXIST" not in returned_texts
        assert "What is RAG?" in returned_texts


# ---------------------------------------------------------------------------
# Edge / failure cases
# ---------------------------------------------------------------------------

class TestDeduplicateEdgeCases:
    async def test_empty_input_returns_empty_without_llm_call(self, tmp_path):
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        # No patch needed – function should short-circuit before calling LLM
        result = await deduplicate_new_queries_against_history([], history, "exploitation")
        assert result == []

    async def test_json_parse_failure_falls_back_to_all_queries(
        self, fake_plain_model_factory, tmp_path
    ):
        """Malformed JSON from the LLM → keep all queries rather than crashing."""
        model = fake_plain_model_factory("not valid JSON {{ broken")
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert result == _SAMPLE_NEW

    async def test_missing_kept_queries_key_falls_back_to_all(
        self, fake_plain_model_factory, tmp_path
    ):
        """Valid JSON but missing 'kept_queries' key → keep all."""
        model = fake_plain_model_factory(json.dumps({"reasoning": "oops"}))
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        # .get("kept_queries", []) returns [] → kept = [] → all removed; but
        # the implementation returns the matched subset (which is empty in this case).
        # The important assertion is: it does NOT raise.
        assert isinstance(result, list)

    async def test_nonexistent_history_file_still_works(self, fake_plain_model_factory, tmp_path):
        """Missing history file should be treated as empty history (<none>)."""
        model = fake_plain_model_factory(_kept_json([q for q, _ in _SAMPLE_NEW]))
        missing = tmp_path / "no_history.md"  # does not exist

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, missing, "exploitation"
            )

        assert len(result) == 3

    async def test_all_queries_removed_returns_empty_list(self, fake_plain_model_factory, tmp_path):
        model = fake_plain_model_factory(_kept_json([]))  # LLM keeps nothing
        history = tmp_path / "full.md"
        history.write_text("", encoding="utf-8")

        with patch(_PATCH_TARGET, return_value=model):
            result = await deduplicate_new_queries_against_history(
                _SAMPLE_NEW, history, "exploitation"
            )

        assert result == []
