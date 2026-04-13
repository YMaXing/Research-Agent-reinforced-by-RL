"""
Unit tests for scrape_and_clean_other_urls_tool.py.

Design notes
------------
* No real LLM calls, no real Firecrawl calls, no network traffic.
* ``FakeLLM`` is a minimal async-capable chat model that returns a
  fixed string in a ``.content`` attribute (mirrors LangChain AIMessage).
* External I/O (scrape_urls_concurrently, scrape_arxiv_url, get_chat_model)
  is patched at the module boundary so only deterministic logic is exercised.

Modules under test
------------------
* src.tools.scrape_and_clean_other_urls_tool – write_scraped_results_to_files
                                               + orchestration function

Key design notes
----------------
* The ``is_arxiv_url`` helper is a private function nested inside the tool;
  its behaviour is exercised indirectly through the orchestration tests.
* ``src/tools/__init__.py`` exports ``scrape_and_clean_other_urls_tool`` (the
  *function*) as an attribute, shadowing the submodule name.  We use
  ``importlib.import_module`` to retrieve the actual module object.
* ``guidelines_data["other_urls"]`` holds ALL guideline URLs; the tool
  internally partitions them into arxiv vs non-arxiv.
"""

import asyncio
import importlib
import json
import sys
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

# ---------------------------------------------------------------------------
# sys.path bootstrapping
# ---------------------------------------------------------------------------
_MSERVER_ROOT = Path(__file__).resolve().parent.parent  # .../mcp_server/
if str(_MSERVER_ROOT) not in sys.path:
    sys.path.insert(0, str(_MSERVER_ROOT))

# ---------------------------------------------------------------------------
# Fake helpers
# ---------------------------------------------------------------------------


class FakeAIMessage:
    """Minimal stand-in for LangChain's AIMessage."""

    def __init__(self, content: str) -> None:
        self.content = content


class FakeLLM:
    """
    Async-capable fake chat model.

    * ``ainvoke`` returns a ``FakeAIMessage`` whose ``.content`` equals the
      string supplied at construction time.
    * ``get_num_tokens`` returns a deterministic integer.
    """

    def __init__(self, response: str = "cleaned content") -> None:
        self._response = response
        self.prompts_received: list[str] = []

    async def ainvoke(self, prompt: Any, **kwargs: Any) -> FakeAIMessage:
        self.prompts_received.append(str(prompt))
        return FakeAIMessage(self._response)

    def invoke(self, prompt: Any, **kwargs: Any) -> FakeAIMessage:
        self.prompts_received.append(str(prompt))
        return FakeAIMessage(self._response)

    def get_num_tokens(self, text: str) -> int:
        return max(1, len(text.split()))


# ---------------------------------------------------------------------------
# Import module under test
# ---------------------------------------------------------------------------
# src/tools/__init__.py re-exports scrape_and_clean_other_urls_tool (the function)
# under the same name as the submodule, shadowing it.  importlib bypasses that.
sacoU_mod = importlib.import_module("src.tools.scrape_and_clean_other_urls_tool")

from src.config.constants import (  # noqa: E402
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
)

# Shortcut to the pure function under test
write_scraped_results_to_files = sacoU_mod.write_scraped_results_to_files

# ---------------------------------------------------------------------------
# Patch target strings
# ---------------------------------------------------------------------------
_SCRAPE_CONCURRENTLY_PATCH = "src.tools.scrape_and_clean_other_urls_tool.scrape_urls_concurrently"
_SCRAPE_ARXIV_PATCH = "src.tools.scrape_and_clean_other_urls_tool.scrape_arxiv_url"
_GET_CHAT_MODEL_PATCH = "src.tools.scrape_and_clean_other_urls_tool.get_chat_model"

# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

ARXIV_URL = "https://arxiv.org/abs/2312.05678"
OTHER_URL = "https://blog.example.com/article"


def _make_valid_dir(
    tmp_path: Path,
    all_urls: list[str] | None = None,
    write_guideline: bool = True,
) -> Path:
    """
    Create a minimal valid directory tree for the tool.

    ``all_urls`` becomes ``guidelines_data["other_urls"]``; it may contain
    any mix of arxiv and non-arxiv URLs.
    """
    research_path = tmp_path / "research"
    research_path.mkdir()
    if write_guideline:
        (research_path / ARTICLE_GUIDELINE_FILE).write_text(
            "Article guidelines here.", encoding="utf-8"
        )
    output = research_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir()
    guidelines: dict = {"other_urls": list(all_urls or [])}
    (output / GUIDELINES_FILENAMES_FILE).write_text(
        json.dumps(guidelines), encoding="utf-8"
    )
    return research_path


def _fake_result(url: str, success: bool = True) -> dict:
    return {
        "url": url,
        "title": f"Title for {url}",
        "markdown": f"# Content for {url}",
        "success": success,
    }


# ===========================================================================
# ── write_scraped_results_to_files ──────────────────────────────────────────
# ===========================================================================


class TestWriteScrapedResultsToFiles:
    def test_successful_result_is_written(self, tmp_path):
        results = [_fake_result("https://a.com", success=True)]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 1
        assert len(saved) == 1
        assert (tmp_path / saved[0]).read_text(encoding="utf-8") == "**Source URL:** <https://a.com>\n\n# Content for https://a.com"

    def test_failed_result_still_written_but_not_counted(self, tmp_path):
        results = [_fake_result("https://b.com", success=False)]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 0
        assert len(saved) == 1
        assert (tmp_path / saved[0]).exists()

    def test_multiple_results_all_written(self, tmp_path):
        results = [_fake_result(f"https://site{i}.com") for i in range(3)]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 3
        assert len(saved) == 3
        for fname in saved:
            assert (tmp_path / fname).exists()

    def test_duplicate_titles_get_unique_filenames(self, tmp_path):
        results = [
            {"url": "https://a.com", "title": "Same Title", "markdown": "one", "success": True},
            {"url": "https://b.com", "title": "Same Title", "markdown": "two", "success": True},
        ]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        assert len(set(saved)) == 2

    def test_empty_markdown_written_with_url_header(self, tmp_path):
        results = [{"url": "https://a.com", "title": "Empty", "markdown": "", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        # Title is injected as H1 before the URL header so get_first_line_title() captures it.
        assert (tmp_path / saved[0]).read_text(encoding="utf-8") == "# Empty\n\n**Source URL:** <https://a.com>\n\n"

    def test_none_markdown_written_with_url_header(self, tmp_path):
        results = [{"url": "https://a.com", "title": "NoMd", "markdown": None, "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        # Title is injected as H1 before the URL header so get_first_line_title() captures it.
        assert (tmp_path / saved[0]).read_text(encoding="utf-8") == "# NoMd\n\n**Source URL:** <https://a.com>\n\n"

    def test_empty_results_list(self, tmp_path):
        saved, success_count = write_scraped_results_to_files([], tmp_path)
        assert saved == []
        assert success_count == 0

    def test_files_written_with_utf8_encoding(self, tmp_path):
        emoji_content = "# Résumé 🚀"
        results = [{"url": "https://a.com", "title": "Unicode", "markdown": emoji_content, "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        assert (tmp_path / saved[0]).read_text(encoding="utf-8") == f"**Source URL:** <https://a.com>\n\n{emoji_content}"

    def test_filename_ends_with_md_extension(self, tmp_path):
        results = [_fake_result("https://a.com")]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        assert saved[0].endswith(".md")

    def test_exception_in_results_is_skipped_gracefully(self, tmp_path):
        """asyncio.gather(return_exceptions=True) may yield exception objects; they must be skipped."""
        exc = RuntimeError("simulated scrape failure")
        valid = _fake_result("https://a.com", success=True)
        saved, success_count = write_scraped_results_to_files([exc, valid], tmp_path)
        assert success_count == 1
        assert len(saved) == 1
        assert (tmp_path / saved[0]).exists()

    def test_only_exception_in_results_yields_empty(self, tmp_path):
        """When all results are exceptions, nothing is written."""
        saved, success_count = write_scraped_results_to_files(
            [RuntimeError("all failed")], tmp_path
        )
        assert saved == []
        assert success_count == 0

    def test_missing_h1_injects_metadata_title(self, tmp_path):
        """When cleaned markdown has no heading, the Firecrawl metadata title is injected as H1."""
        results = [{"url": "https://a.com", "title": "My Article", "markdown": "Some body text.", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        content = (tmp_path / saved[0]).read_text(encoding="utf-8")
        assert content.startswith("# My Article\n\n")

    def test_existing_h1_not_duplicated(self, tmp_path):
        """When cleaned markdown already has a heading, no extra H1 is injected."""
        results = [{"url": "https://a.com", "title": "My Article", "markdown": "# Existing Title\n\nBody.", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        content = (tmp_path / saved[0]).read_text(encoding="utf-8")
        assert "# My Article" not in content
        assert "# Existing Title" in content


# ===========================================================================
# ── Tool validation / error paths ───────────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolValidation:
    async def test_nonexistent_directory_raises_value_error(self, tmp_path):
        bad_path = tmp_path / "does_not_exist"
        with pytest.raises(ValueError, match="does not exist"):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(bad_path))

    async def test_path_is_file_not_dir_raises_value_error(self, tmp_path):
        file_path = tmp_path / "not_a_dir.txt"
        file_path.write_text("oops", encoding="utf-8")
        with pytest.raises(ValueError):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(file_path))

    async def test_missing_guidelines_filenames_file_raises_value_error(self, tmp_path):
        research_path = tmp_path / "research"
        research_path.mkdir()
        (research_path / RESEARCH_OUTPUT_FOLDER).mkdir()
        # GUIDELINES_FILENAMES_FILE is absent
        with pytest.raises(ValueError, match="does not exist"):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

    async def test_malformed_json_raises_value_error(self, tmp_path):
        research_path = tmp_path / "research"
        research_path.mkdir()
        output = research_path / RESEARCH_OUTPUT_FOLDER
        output.mkdir()
        (output / GUIDELINES_FILENAMES_FILE).write_text("NOT VALID JSON", encoding="utf-8")
        with pytest.raises(ValueError, match="Error reading"):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

    async def test_missing_article_guideline_raises_value_error(self, tmp_path):
        research_path = tmp_path / "research"
        research_path.mkdir()
        output = research_path / RESEARCH_OUTPUT_FOLDER
        output.mkdir()
        # guidelines_filenames.json present and has URLs
        guidelines = {"other_urls": [OTHER_URL]}
        (output / GUIDELINES_FILENAMES_FILE).write_text(json.dumps(guidelines), encoding="utf-8")
        # article_guideline.md is absent
        with pytest.raises(ValueError, match="does not exist"):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))


# ===========================================================================
# ── Early returns (no URLs to process) ──────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolEarlyReturn:
    async def test_empty_other_urls_list_returns_success(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[])
        result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))
        assert result["status"] == "success"
        assert result["urls_processed"] == 0

    async def test_missing_other_urls_key_returns_success(self, tmp_path):
        """guidelines_filenames.json without an 'other_urls' key → empty list → early return."""
        research_path = tmp_path / "research"
        research_path.mkdir()
        output = research_path / RESEARCH_OUTPUT_FOLDER
        output.mkdir()
        (output / GUIDELINES_FILENAMES_FILE).write_text(json.dumps({}), encoding="utf-8")
        result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))
        assert result["status"] == "success"
        assert result["urls_processed"] == 0
        assert "No other URLs" in result["message"]

    async def test_early_return_message_contains_folder_name(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[])
        result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))
        assert str(research_path) in result["message"]


# ===========================================================================
# ── Non-arxiv URL scraping ───────────────────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolOtherUrls:
    async def test_non_arxiv_url_calls_scrape_concurrently(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)) as mock_sc, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_sc.assert_awaited_once()
        called_urls = mock_sc.call_args[0][0]
        assert called_urls == [OTHER_URL]

    async def test_concurrency_limit_passed_through(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)) as mock_sc, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path), concurrency_limit=7)

        # concurrency_limit is the third positional argument
        assert mock_sc.call_args[0][2] == 7

    async def test_files_written_to_output_dir(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["files_saved"] == 1
        output_dir = research_path / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
        assert output_dir.exists()
        assert len(list(output_dir.glob("*.md"))) == 1

    async def test_output_dir_is_created(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        expected_dir = research_path / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
        assert not expected_dir.exists()

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert expected_dir.exists()

    async def test_all_failed_scrapes_status_is_warning(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL, success=False)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["status"] == "warning"
        assert result["urls_processed"] == 0
        assert result["files_saved"] == 1  # file still written

    async def test_successful_scrape_counted_in_urls_processed(self, tmp_path):
        urls = [OTHER_URL, "https://other.example.com"]
        research_path = _make_valid_dir(tmp_path, all_urls=urls)
        fake_results = [_fake_result(u, success=(i == 0)) for i, u in enumerate(urls)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["urls_processed"] == 1
        assert result["files_saved"] == 2

    async def test_article_guidelines_passed_to_scrape_concurrently(self, tmp_path):
        """The article guideline text is forwarded to scrape_urls_concurrently."""
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        guideline_text = "Article guidelines here."

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])) as mock_sc, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        called_guidelines = mock_sc.call_args[0][1]
        assert called_guidelines == guideline_text

    async def test_arxiv_url_not_passed_to_scrape_concurrently(self, tmp_path):
        """arXiv URLs must NOT be forwarded to scrape_urls_concurrently."""
        research_path = _make_valid_dir(tmp_path, all_urls=[ARXIV_URL, OTHER_URL])
        fake_other_results = [_fake_result(OTHER_URL)]
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_other_results)) as mock_sc, \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        called_urls = mock_sc.call_args[0][0]
        assert ARXIV_URL not in called_urls
        assert OTHER_URL in called_urls


# ===========================================================================
# ── arXiv URL handling ───────────────────────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolArxivUrls:
    async def test_arxiv_url_calls_scrape_arxiv_url(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[ARXIV_URL])
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)) as mock_arxiv, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_arxiv.assert_awaited_once()
        called_url = mock_arxiv.call_args[0][0]
        assert called_url == ARXIV_URL

    async def test_arxiv_url_triggers_get_chat_model(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[ARXIV_URL])
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()) as mock_gcm:
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_gcm.assert_called_once()

    async def test_arxiv_only_file_saved(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[ARXIV_URL])
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        # The final write_scraped_results_to_files covers the arxiv result
        assert result["files_saved"] == 1

    async def test_arxiv_only_no_get_chat_model_without_arxiv_urls(self, tmp_path):
        """get_chat_model should NOT be called when there are no arXiv URLs."""
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()) as mock_gcm:
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_gcm.assert_not_called()

    async def test_multiple_arxiv_urls_each_scraped(self, tmp_path):
        arxiv_urls = [
            "https://arxiv.org/abs/2312.05678",
            "https://arxiv.org/pdf/2501.11120",
        ]
        research_path = _make_valid_dir(tmp_path, all_urls=arxiv_urls)
        fake_arxiv_results = _fake_result(arxiv_urls[0])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_results)) as mock_arxiv, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert mock_arxiv.await_count == 2

    async def test_arxiv_article_guidelines_passed_to_scrape_arxiv(self, tmp_path):
        """article_guideline.md content is forwarded to scrape_arxiv_url."""
        guideline_text = "Article guidelines here."
        research_path = _make_valid_dir(tmp_path, all_urls=[ARXIV_URL])
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)) as mock_arxiv, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        called_guidelines = mock_arxiv.call_args[0][1]
        assert called_guidelines == guideline_text

    async def test_html_arxiv_url_routed_to_scrape_arxiv_url(self, tmp_path):
        """/html/ arXiv URLs must route to scrape_arxiv_url, not scrape_urls_concurrently."""
        html_url = "https://arxiv.org/html/2309.02427"
        research_path = _make_valid_dir(tmp_path, all_urls=[html_url])
        fake_arxiv_result = _fake_result(html_url)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[])) as mock_sc, \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)) as mock_ax, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_ax.assert_awaited_once()
        assert mock_ax.call_args[0][0] == html_url
        # scrape_urls_concurrently must receive an empty non-arxiv list
        called_other_urls = mock_sc.call_args[0][0]
        assert html_url not in called_other_urls
        assert result["files_saved"] == 1


# ===========================================================================
# ── Mixed URL types ──────────────────────────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolMixed:
    async def test_mixed_urls_both_paths_invoked(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL, ARXIV_URL])
        fake_other_results = [_fake_result(OTHER_URL)]
        fake_arxiv_result = _fake_result(ARXIV_URL)

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_other_results)) as mock_sc, \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=fake_arxiv_result)) as mock_ax, \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        mock_sc.assert_awaited_once()
        mock_ax.assert_awaited_once()
        # Both files saved in the final write call
        assert result["files_saved"] == 2

    async def test_mixed_urls_status_success_when_all_succeed(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL, ARXIV_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=_fake_result(ARXIV_URL))), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["status"] == "success"

    async def test_urls_total_includes_arxiv_and_other_urls(self, tmp_path):
        """urls_total in the return dict counts all attempted URLs (arxiv + non-arxiv)."""
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL, ARXIV_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=_fake_result(ARXIV_URL))), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        # urls_total = len(other_urls) + len(arxiv_urls) = 1 + 1 = 2
        assert result["urls_total"] == 2

    async def test_output_dir_holds_files_for_both_types(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL, ARXIV_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=_fake_result(ARXIV_URL))), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        output_dir = research_path / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
        files = list(output_dir.glob("*.md"))
        assert len(files) == 2


# ===========================================================================
# ── Return dict shape ────────────────────────────────────────────────────────
# ===========================================================================


class TestScrapeAndCleanOtherUrlsToolReturnShape:
    _EXPECTED_KEYS = {
        "status",
        "urls_processed",
        "urls_total",
        "files_saved",
        "output_directory",
        "saved_files",
        "message",
    }

    async def test_return_dict_has_all_expected_keys(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert self._EXPECTED_KEYS <= set(result.keys()), (
            f"Missing keys: {self._EXPECTED_KEYS - set(result.keys())}"
        )

    async def test_early_return_dict_has_required_keys(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[])
        result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))
        for key in ("status", "urls_processed", "urls_total", "message"):
            assert key in result, f"Missing key: {key}"

    async def test_output_directory_matches_expected_path(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        expected_dir = (
            research_path / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
        ).resolve()
        assert result["output_directory"] == str(expected_dir)

    async def test_saved_files_is_list_of_strings(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert isinstance(result["saved_files"], list)
        assert all(isinstance(f, str) for f in result["saved_files"])

    async def test_message_contains_research_directory(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=[_fake_result(OTHER_URL)])), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert str(research_path) in result["message"]

    async def test_status_is_success_when_at_least_one_succeeds(self, tmp_path):
        urls = [OTHER_URL, "https://second.example.com"]
        research_path = _make_valid_dir(tmp_path, all_urls=urls)
        fake_results = [_fake_result(urls[0], success=True), _fake_result(urls[1], success=False)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["status"] == "success"

    async def test_status_is_warning_when_all_scrapes_fail(self, tmp_path):
        research_path = _make_valid_dir(tmp_path, all_urls=[OTHER_URL])
        fake_results = [_fake_result(OTHER_URL, success=False)]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sacoU_mod.scrape_and_clean_other_urls_tool(str(research_path))

        assert result["status"] == "warning"
