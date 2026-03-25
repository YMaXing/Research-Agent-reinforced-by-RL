"""Unit tests for src/tools/run_tavily_research_tool.py.

``append_search_results_to_file`` is a pure helper tested directly.
``run_tavily_research_tool`` is async and calls ``run_tavily_search`` (mocked)
+ file I/O.  No real Tavily or LLM calls.
"""

from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

from src.config.constants import (
    ARTICLE_GUIDELINE_FILE,
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
)
from src.tools.run_tavily_research_tool import (
    append_search_results_to_file,
    run_tavily_research_tool,
)

_PATCH_SEARCH = "src.tools.run_tavily_research_tool.run_tavily_search"


def _setup_dir(tmp_path: Path) -> Path:
    """Create a research folder with the RESEARCH_OUTPUT_FOLDER sub-directory.

    The tool validates that ``research_path / RESEARCH_OUTPUT_FOLDER`` exists,
    so we must create the output sub-folder up front.
    """
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("# Topic", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    return tmp_path


# ---------------------------------------------------------------------------
# append_search_results_to_file (pure helper)
# ---------------------------------------------------------------------------


class TestAppendSearchResultsToFile:
    def test_appends_results(self, tmp_path):
        results_path = tmp_path / "results.md"
        results_path.write_text("", encoding="utf-8")

        queries = ["What is RAG?"]
        # run_tavily_search returns (full_answer, answer_by_source, citations)
        search_results = [
            ("full answer", {1: "RAG is retrieval."}, {1: "https://rag.com"})
        ]

        total = append_search_results_to_file(results_path, queries, search_results, phase="[EXPLOITATION]")

        assert total == 1
        content = results_path.read_text(encoding="utf-8")
        assert "### Source [1]:" in content

    def test_skips_empty_citations(self, tmp_path):
        results_path = tmp_path / "results.md"
        results_path.write_text("", encoding="utf-8")

        queries = ["q1"]
        search_results = [("", {}, {})]  # no citations

        total = append_search_results_to_file(results_path, queries, search_results)
        assert total == 0

    def test_multiple_queries(self, tmp_path):
        results_path = tmp_path / "results.md"
        results_path.write_text("", encoding="utf-8")

        queries = ["q1", "q2"]
        search_results = [
            ("a1", {1: "ans1"}, {1: "https://a.com"}),
            ("a2", {1: "ans2", 2: "ans3"}, {1: "https://b.com", 2: "https://c.com"}),
        ]

        total = append_search_results_to_file(results_path, queries, search_results)
        assert total == 3  # 1 + 2

    def test_exploration_phase_tag(self, tmp_path):
        results_path = tmp_path / "results.md"
        results_path.write_text("", encoding="utf-8")

        queries = ["q"]
        search_results = [("a", {1: "x"}, {1: "https://x.com"})]

        append_search_results_to_file(results_path, queries, search_results, phase="[EXPLORATION]")
        content = results_path.read_text(encoding="utf-8")
        assert "[EXPLORATION]" in content


# ---------------------------------------------------------------------------
# run_tavily_research_tool (async, mock tavily search)
# ---------------------------------------------------------------------------


class TestRunTavilyResearchTool:
    async def test_success_returns_counts(self, tmp_path):
        research_dir = _setup_dir(tmp_path)
        fake_result = ("full", {1: "answer"}, {1: "https://a.com"})

        with patch(_PATCH_SEARCH, new_callable=AsyncMock, return_value=fake_result):
            result = await run_tavily_research_tool(str(research_dir), ["What is RAG?"])

        assert result["status"] == "success"
        assert result["queries_processed"] == 1
        assert result["sources_added"] == 1

        # Verify file was created
        results_path = research_dir / RESEARCH_OUTPUT_FOLDER / TAVILY_RESULTS_FILE
        assert results_path.exists()

    async def test_empty_queries(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        result = await run_tavily_research_tool(str(research_dir), [])

        assert result["status"] == "success"
        assert result["queries_processed"] == 0

    async def test_complementary_phase(self, tmp_path):
        research_dir = _setup_dir(tmp_path)
        fake_result = ("full", {1: "answer"}, {1: "https://a.com"})

        with patch(_PATCH_SEARCH, new_callable=AsyncMock, return_value=fake_result):
            result = await run_tavily_research_tool(str(research_dir), ["q1"], query_source="complementary")

        assert result["status"] == "success"
        content = (research_dir / RESEARCH_OUTPUT_FOLDER / TAVILY_RESULTS_FILE).read_text(encoding="utf-8")
        assert "[EXPLORATION]" in content

    async def test_multiple_queries(self, tmp_path):
        research_dir = _setup_dir(tmp_path)

        async def _fake_search(query):
            return ("full", {1: f"answer for {query}"}, {1: f"https://{query}.com"})

        with patch(_PATCH_SEARCH, side_effect=_fake_search):
            result = await run_tavily_research_tool(str(research_dir), ["q1", "q2", "q3"])

        assert result["queries_processed"] == 3
        assert result["sources_added"] == 3

    async def test_raises_for_missing_output_folder(self, tmp_path):
        """Tool validates that research_path / RESEARCH_OUTPUT_FOLDER exists."""
        with pytest.raises(ValueError):
            await run_tavily_research_tool(str(tmp_path), ["q"])
