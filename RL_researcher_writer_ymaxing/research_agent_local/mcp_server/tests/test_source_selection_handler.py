"""Unit tests for src/app/source_selection_handler.py.

Pure-function tests for ``parse_tavily_results``, ``build_sources_data_text``,
``parse_results_selected``, and ``load_scraped_guideline_context`` require no
LLM mocking.

``select_sources`` and ``select_top_sources`` call ``get_chat_model`` which is
patched with fake models that return deterministic Pydantic objects.
"""

from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

from src.app.source_selection_handler import (
    build_sources_data_text,
    load_scraped_guideline_context,
    parse_results_selected,
    parse_tavily_results,
    select_sources,
    select_top_sources,
)
from src.config.constants import RESEARCH_OUTPUT_FOLDER, URLS_FROM_GUIDELINES_FOLDER
from src.models.query_models import SourceSelection, TopSourceSelection

_PATCH_TARGET = "src.app.source_selection_handler.get_chat_model"


# ---------------------------------------------------------------------------
# Sample markdown blocks reused across tests
# ---------------------------------------------------------------------------

_SAMPLE_RESULTS_MD = """\
Phase: [EXPLOITATION]

### Source [1]: https://a.com

Query: What is RAG?

Answer: RAG retrieves context.

-----

Phase: [EXPLORATION]

### Source [2]: https://b.com

Query: How does dense retrieval work?

Answer: Dense retrieval uses embeddings.

-----
"""


# ---------------------------------------------------------------------------
# parse_tavily_results
# ---------------------------------------------------------------------------


class TestParseTavilyResults:
    def test_parses_sources(self):
        parsed = parse_tavily_results(_SAMPLE_RESULTS_MD)
        assert len(parsed) == 2
        assert parsed[1]["url"] == "https://a.com"
        assert parsed[2]["url"] == "https://b.com"

    def test_phase_captured(self):
        parsed = parse_tavily_results(_SAMPLE_RESULTS_MD)
        assert parsed[1]["phase"] == "[EXPLOITATION]"
        assert parsed[2]["phase"] == "[EXPLORATION]"

    def test_query_and_answer(self):
        parsed = parse_tavily_results(_SAMPLE_RESULTS_MD)
        assert "RAG" in parsed[1]["query"]
        assert "retrieves" in parsed[1]["answer"]

    def test_empty_input(self):
        assert parse_tavily_results("") == {}


# ---------------------------------------------------------------------------
# build_sources_data_text
# ---------------------------------------------------------------------------


class TestBuildSourcesDataText:
    def test_contains_all_sources(self):
        parsed = parse_tavily_results(_SAMPLE_RESULTS_MD)
        text = build_sources_data_text(parsed)
        assert "Source ID 1" in text
        assert "Source ID 2" in text
        assert "https://a.com" in text

    def test_empty_parsed(self):
        assert build_sources_data_text({}) == ""


# ---------------------------------------------------------------------------
# parse_results_selected
# ---------------------------------------------------------------------------


class TestParseResultsSelected:
    def test_parses_same_format(self):
        sources = parse_results_selected(_SAMPLE_RESULTS_MD)
        assert len(sources) == 2
        assert sources[0]["url"] == "https://a.com"

    def test_returns_list_of_dicts(self):
        sources = parse_results_selected(_SAMPLE_RESULTS_MD)
        for src in sources:
            assert "url" in src
            assert "query" in src
            assert "answer" in src
            assert "phase" in src

    def test_empty(self):
        assert parse_results_selected("") == []


# ---------------------------------------------------------------------------
# load_scraped_guideline_context
# ---------------------------------------------------------------------------


class TestLoadScrapedGuidelineContext:
    def test_loads_markdown_files(self, tmp_path):
        research_dir = tmp_path
        guide_dir = research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
        guide_dir.mkdir(parents=True)
        (guide_dir / "a.md").write_text("Alpha content", encoding="utf-8")
        (guide_dir / "b.md").write_text("Beta content", encoding="utf-8")

        ctx = load_scraped_guideline_context(str(research_dir))
        assert "Alpha content" in ctx
        assert "Beta content" in ctx

    def test_returns_empty_for_missing_dir(self, tmp_path):
        ctx = load_scraped_guideline_context(str(tmp_path))
        assert ctx == ""


# ---------------------------------------------------------------------------
# select_sources (async, fake LLM)
# ---------------------------------------------------------------------------


class _FakeSourceSelectionModel:
    """Fake model returning a ``SourceSelection`` Pydantic object."""

    def __init__(self, selection: SourceSelection) -> None:
        self._selection = selection

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> SourceSelection:
        return self._selection


class TestSelectSources:
    async def test_specific_selection(self):
        selection = SourceSelection(selection_type="specific", source_ids=[1])
        model = _FakeSourceSelectionModel(selection)
        with patch(_PATCH_TARGET, return_value=model):
            result = await select_sources("guidelines", _SAMPLE_RESULTS_MD)
        assert result == [1]

    async def test_all_selection(self):
        selection = SourceSelection(selection_type="all", source_ids=[])
        model = _FakeSourceSelectionModel(selection)
        with patch(_PATCH_TARGET, return_value=model):
            result = await select_sources("guidelines", _SAMPLE_RESULTS_MD)
        assert sorted(result) == [1, 2]

    async def test_none_selection(self):
        selection = SourceSelection(selection_type="none", source_ids=[])
        model = _FakeSourceSelectionModel(selection)
        with patch(_PATCH_TARGET, return_value=model):
            result = await select_sources("guidelines", _SAMPLE_RESULTS_MD)
        assert result == []

    async def test_empty_results_returns_empty(self):
        # No mocking needed — function short-circuits on empty input
        result = await select_sources("guidelines", "")
        assert result == []

    async def test_llm_failure_fallback_to_all(self):
        """When the LLM raises an exception, all sources are returned."""

        class _ExplodingModel:
            async def ainvoke(self, *a, **kw):
                raise RuntimeError("boom")

        with patch(_PATCH_TARGET, return_value=_ExplodingModel()):
            result = await select_sources("g", _SAMPLE_RESULTS_MD)
        assert sorted(result) == [1, 2]


# ---------------------------------------------------------------------------
# select_top_sources (async, fake LLM)
# ---------------------------------------------------------------------------


class _FakeTopSourceSelectionModel:
    """Fake model returning a ``TopSourceSelection`` Pydantic object."""

    def __init__(self, response: TopSourceSelection) -> None:
        self._response = response

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> TopSourceSelection:
        return self._response


class TestSelectTopSources:
    async def test_returns_selected_urls(self):
        response = TopSourceSelection(
            selected_urls=["https://a.com", "https://b.com"],
            reasoning="Most relevant",
        )
        model = _FakeTopSourceSelectionModel(response)
        with patch(_PATCH_TARGET, return_value=model):
            result = await select_top_sources("guidelines", "", _SAMPLE_RESULTS_MD, max_sources=5)
        assert result["selected_urls"] == ["https://a.com", "https://b.com"]
        assert result["reasoning"] == "Most relevant"

    async def test_respects_max_sources(self):
        response = TopSourceSelection(
            selected_urls=["https://a.com", "https://b.com", "https://c.com"],
            reasoning="top 3",
        )
        model = _FakeTopSourceSelectionModel(response)
        with patch(_PATCH_TARGET, return_value=model):
            result = await select_top_sources("g", "", _SAMPLE_RESULTS_MD, max_sources=2)
        assert len(result["selected_urls"]) == 2

    async def test_empty_results_returns_empty(self):
        result = await select_top_sources("g", "", "", max_sources=5)
        assert result["selected_urls"] == []

    async def test_llm_failure_fallback(self):
        class _ExplodingModel:
            async def ainvoke(self, *a, **kw):
                raise RuntimeError("boom")

        with patch(_PATCH_TARGET, return_value=_ExplodingModel()):
            result = await select_top_sources("g", "", _SAMPLE_RESULTS_MD, max_sources=5)
        # Fallback returns first N source URLs from the file
        assert len(result["selected_urls"]) > 0
        assert "failed" in result["reasoning"].lower() or "falling back" in result["reasoning"].lower()
