"""
Unit tests for src/app/generate_queries_handler.py.

Both public async functions are tested with a fake LLM so no real API calls
are made.

Strategy
--------
``get_chat_model`` is patched at the point it is *looked up* in the handler
module (``src.app.generate_queries_handler.get_chat_model``).  Depending on
the call, the patch returns either:

* ``FakeStructuredModel`` – simulates a model wrapped with
  ``with_structured_output(GeneratedQueries)``, returning a ``GeneratedQueries``
  object from ``ainvoke``.

* ``RecordingModel`` – like ``FakeStructuredModel`` but stores the prompt
  string, enabling assertions on prompt content (e.g. depth ratio values).
"""

import pytest
from unittest.mock import patch, AsyncMock

from tests.conftest import FAKE_QUERIES_5, FakeStructuredModel, RecordingModel
from src.app.generate_queries_handler import (
    generate_complementary_queries_with_reasons,
    generate_queries_with_reasons,
)
from src.models.query_models import GeneratedQueries

_PATCH_TARGET = "src.app.generate_queries_handler.get_chat_model"


# ---------------------------------------------------------------------------
# generate_queries_with_reasons
# ---------------------------------------------------------------------------

class TestGenerateQueriesWithReasons:
    async def test_returns_list_of_tuples(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model):
            result = await generate_queries_with_reasons("guidelines", "past", "full", "scraped", n_queries=5)

        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    async def test_returns_exactly_n_queries(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model):
            result = await generate_queries_with_reasons("guidelines", "past", "full", "scraped", n_queries=5)

        assert len(result) == 5

    async def test_result_trimmed_when_model_returns_too_many(self):
        """If model returns more than n_queries, output is capped at n_queries."""
        # Fake model returns 5 queries; ask for 3 → truncated to 3
        model = FakeStructuredModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=model):
            result = await generate_queries_with_reasons("g", "p", "f", "s", n_queries=3)

        assert len(result) == 3

    async def test_query_and_reason_values_match_model_output(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model):
            result = await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        assert result[0][0] == "What is RAG?"
        assert result[0][1] == "Covers retrieval basics"
        assert result[4][0] == "What are production RAG challenges?"

    async def test_raises_runtime_error_when_too_few_queries(self, fake_structured_model_few):
        """If model returns fewer queries than n_queries, RuntimeError is raised."""
        with patch(_PATCH_TARGET, return_value=fake_structured_model_few):
            with pytest.raises(RuntimeError, match="only"):
                await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

    async def test_get_chat_model_called_once(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model) as mock_get:
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        mock_get.assert_called_once()

    async def test_get_chat_model_receives_schema(self, fake_structured_model):
        """The handler must pass GeneratedQueries as the schema argument."""
        with patch(_PATCH_TARGET, return_value=fake_structured_model) as mock_get:
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        call_args = mock_get.call_args
        # Second positional argument should be GeneratedQueries
        assert call_args[0][1] is GeneratedQueries

    async def test_prompt_contains_guidelines(self):
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_queries_with_reasons(
                "Article guidelines text", "past", "full", "scraped", n_queries=5
            )

        assert "Article guidelines text" in recording.last_prompt

    async def test_prompt_contains_n_queries(self):
        queries_7 = FAKE_QUERIES_5 + [
            ("Extra query 6", "Reason 6"),
            ("Extra query 7", "Reason 7"),
        ]
        recording = RecordingModel(queries_7)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=7)

        assert "7" in recording.last_prompt

    async def test_none_guidelines_replaced_with_none_placeholder(self):
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_queries_with_reasons("", "p", "f", "s", n_queries=5)

        # Empty / falsy guideline string should be replaced with "<none>"
        assert "<none>" in recording.last_prompt

    async def test_reraises_on_unexpected_response_type(self):
        """A model returning a non-GeneratedQueries value should propagate RuntimeError."""

        class WrongTypeModel:
            async def ainvoke(self, *a, **kw):
                return "just a string"  # wrong type

        with patch(_PATCH_TARGET, return_value=WrongTypeModel()):
            with pytest.raises(RuntimeError, match="unexpected type"):
                await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

    async def test_prompt_contains_exploitation_boundary_rule(self):
        """The exploitation prompt must state that depth/breadth queries belong to the complementary phase."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        assert "Exploitation queries fill direct coverage gaps only" in recording.last_prompt

    async def test_prompt_does_not_contain_depth_breadth_definition(self):
        """The exploitation prompt must NOT contain the inward/outward framing (that belongs to the complementary prompt)."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        assert "inward" not in recording.last_prompt
        assert "outward" not in recording.last_prompt


# ---------------------------------------------------------------------------
# generate_complementary_queries_with_reasons
# ---------------------------------------------------------------------------

class TestGenerateComplementaryQueriesWithReasons:
    async def test_returns_list_of_tuples(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model):
            result = await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5, depth_vs_breadth_ratio=0.5
            )

        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    async def test_returns_exactly_n_queries(self, fake_structured_model):
        with patch(_PATCH_TARGET, return_value=fake_structured_model):
            result = await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
            )

        assert len(result) == 5

    async def test_prompt_contains_depth_percentage_for_08_ratio(self):
        """ratio=0.8 → depth_pct=80, breadth_pct=20 → both appear in prompt."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5, depth_vs_breadth_ratio=0.8
            )

        assert "80" in recording.last_prompt
        assert "20" in recording.last_prompt

    async def test_prompt_contains_depth_percentage_for_03_ratio(self):
        """ratio=0.3 → depth_pct=30, breadth_pct=70."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5, depth_vs_breadth_ratio=0.3
            )

        assert "30" in recording.last_prompt
        assert "70" in recording.last_prompt

    async def test_default_ratio_is_50_50(self):
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
                # depth_vs_breadth_ratio defaults to 0.5
            )

        assert "50" in recording.last_prompt

    async def test_raises_when_too_few_queries(self, fake_structured_model_few):
        with patch(_PATCH_TARGET, return_value=fake_structured_model_few):
            with pytest.raises(RuntimeError):
                await generate_complementary_queries_with_reasons(
                    "g", "p", "f", "s", n_queries=5
                )

    async def test_prompt_contains_guidelines(self):
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "My guidelines", "p", "f", "s", n_queries=5
            )

        assert "My guidelines" in recording.last_prompt

    async def test_result_trimmed_to_n_queries(self):
        model = FakeStructuredModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=model):
            result = await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=2
            )

        assert len(result) == 2

    async def test_prompt_contains_inward_outward_framing(self):
        """The complementary prompt must contain the canonical inward/outward depth-breadth framing."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
            )

        assert "inward \u2014 intensify understanding of the core topic" in recording.last_prompt
        assert "outward \u2014 connect to adjacent areas outside the core topic" in recording.last_prompt

    async def test_prompt_contains_motivation_depth_bullet(self):
        """The motivation bullet (first depth item) must be present in the complementary prompt."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
            )

        assert "motivation for the topic" in recording.last_prompt

    async def test_prompt_contains_alternative_implementation_perspectives_bullet(self):
        """'alternative implementation perspectives' must appear verbatim, not the vaguer 'alternative perspectives'."""
        recording = RecordingModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=recording):
            await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
            )

        assert "alternative implementation perspectives" in recording.last_prompt
