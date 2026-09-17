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

from tests.conftest import FAKE_QUERIES_5, FakeAIMessage, FakePlainModel, FakeStructuredModel, RecordingModel
from src.app.generate_queries_handler import (
    _shorten_query_if_needed,
    generate_complementary_queries_with_reasons,
    generate_queries_with_reasons,
)
from src.models.query_models import GeneratedQueries, _MAX_QUERY_CHARS

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


# ---------------------------------------------------------------------------
# _shorten_query_if_needed (unit tests)
# ---------------------------------------------------------------------------

_LONG_QUERY = "A" * (_MAX_QUERY_CHARS + 50)       # 250 chars — over the limit
_SHORT_ANSWER = "What is the best tool description practice?"  # 43 chars


class TestShortenQueryIfNeeded:
    """Direct unit tests for the _shorten_query_if_needed helper."""

    async def test_short_query_returned_unchanged(self):
        """A query at or below _MAX_QUERY_CHARS must be returned as-is with no LLM call."""
        short = "x" * _MAX_QUERY_CHARS
        with patch(_PATCH_TARGET) as mock_get:
            result = await _shorten_query_if_needed(short)
        mock_get.assert_not_called()
        assert result == short

    async def test_long_query_shortened_on_first_attempt(self):
        """LLM returns a short-enough reply on the first attempt."""
        plain_model = FakePlainModel(_SHORT_ANSWER)
        with patch(_PATCH_TARGET, return_value=plain_model):
            result = await _shorten_query_if_needed(_LONG_QUERY)
        assert result == _SHORT_ANSWER
        assert len(result) <= _MAX_QUERY_CHARS

    async def test_long_query_requiring_two_attempts(self):
        """LLM returns an over-long reply on attempt 1, then a valid reply on attempt 2."""
        still_long = "B" * (_MAX_QUERY_CHARS + 10)
        replies = iter([still_long, _SHORT_ANSWER])

        class TwoStepModel:
            async def ainvoke(self, *a, **kw):
                return FakeAIMessage(next(replies))

        with patch(_PATCH_TARGET, return_value=TwoStepModel()):
            result = await _shorten_query_if_needed(_LONG_QUERY)
        assert result == _SHORT_ANSWER

    async def test_hard_fallback_after_max_attempts(self):
        """If the LLM never shortens enough, result is hard-cut to <= _MAX_QUERY_CHARS."""
        always_long = FakePlainModel("Z" * (_MAX_QUERY_CHARS + 100))
        with patch(_PATCH_TARGET, return_value=always_long):
            result = await _shorten_query_if_needed(_LONG_QUERY)
        assert len(result) <= _MAX_QUERY_CHARS

    async def test_hard_fallback_ends_with_question_mark(self):
        """The hard-cut fallback always appends a '?' at the end."""
        always_long = FakePlainModel("word " * (_MAX_QUERY_CHARS // 5 + 10))
        with patch(_PATCH_TARGET, return_value=always_long):
            result = await _shorten_query_if_needed(_LONG_QUERY)
        assert result.endswith("?")

    async def test_hard_fallback_cuts_at_word_boundary(self):
        """Hard-cut should not split in the middle of a word."""
        # Build a string of 5-char words followed by spaces so a mid-word cut is possible
        repeated = ("hello " * 50)[:(_MAX_QUERY_CHARS + 50)]
        always_long = FakePlainModel(repeated)
        with patch(_PATCH_TARGET, return_value=always_long):
            result = await _shorten_query_if_needed(_LONG_QUERY)
        # Remove the trailing '?' before checking — the word before it must be complete
        body = result.rstrip("?")
        assert not body.endswith("hell") and not body.endswith("hel")  # no mid-word split


# ---------------------------------------------------------------------------
# Shorten integration: long query from model is shortened before return
# ---------------------------------------------------------------------------

class TestShortenIntegration:
    """Integration tests verifying _shorten_query_if_needed is wired into the
    generation functions and that its output reaches the caller.

    Pydantic enforces ``max_length=200`` at construction time, so we use
    ``QueryAndReason.model_construct`` (which bypasses validation) inside a
    custom fake model to simulate a structured-output parser that returns an
    over-length query before the shorten step runs.
    """

    def _make_overlong_model(self, long_q: str) -> FakeStructuredModel:
        """Return a fake model whose first query is intentionally over the char limit.

        ``model_construct`` bypasses Pydantic field validation, mirroring how a
        LangChain JSON parser might produce a raw object before schema checks.
        """
        from src.models.query_models import QueryAndReason, GeneratedQueries

        first = QueryAndReason.model_construct(question=long_q, reason="reason1")
        rest = [QueryAndReason(question=q, reason=r) for q, r in FAKE_QUERIES_5[1:]]

        class _Model:
            async def ainvoke(self, *a, **kw):
                return GeneratedQueries.model_construct(queries=[first] + rest)

        return _Model()

    async def test_long_query_from_model_is_shortened_exploitation(self):
        """generate_queries_with_reasons must shorten any query that exceeds _MAX_QUERY_CHARS."""
        long_q = "How does this work exactly? " * 12  # well over 200 chars
        overlong_model = self._make_overlong_model(long_q)
        plain_model = FakePlainModel(_SHORT_ANSWER)

        # First get_chat_model call → overlong model; second (shorten) → plain model
        with patch(_PATCH_TARGET, side_effect=[overlong_model, plain_model]):
            result = await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)

        assert result[0][0] == _SHORT_ANSWER
        assert len(result[0][0]) <= _MAX_QUERY_CHARS

    async def test_short_queries_not_shortened_exploitation(self):
        """When all generated queries are short, get_chat_model is called exactly once."""
        structured_model = FakeStructuredModel(FAKE_QUERIES_5)
        with patch(_PATCH_TARGET, return_value=structured_model) as mock_get:
            await generate_queries_with_reasons("g", "p", "f", "s", n_queries=5)
        mock_get.assert_called_once()

    async def test_long_query_from_model_is_shortened_complementary(self):
        """generate_complementary_queries_with_reasons must also shorten overlong queries."""
        long_q = "Explain in detail the motivation and mechanics of tool calling? " * 5
        overlong_model = self._make_overlong_model(long_q)
        plain_model = FakePlainModel(_SHORT_ANSWER)

        with patch(_PATCH_TARGET, side_effect=[overlong_model, plain_model]):
            result = await generate_complementary_queries_with_reasons(
                "g", "p", "f", "s", n_queries=5
            )

        assert result[0][0] == _SHORT_ANSWER
        assert len(result[0][0]) <= _MAX_QUERY_CHARS
