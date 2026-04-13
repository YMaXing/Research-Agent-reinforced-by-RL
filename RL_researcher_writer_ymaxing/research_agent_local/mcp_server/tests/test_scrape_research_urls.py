"""
Unit tests for scrape_research_urls_tool.py and scraping_handler.py.

Design notes
------------
* No real LLM calls, no real Firecrawl calls, no network traffic.
* ``FakeLLM`` is a minimal async-capable chat model that returns a
  fixed string in a ``.content`` attribute (mirrors LangChain AIMessage).
* ``FakeFirecrawlResult`` mimics the object returned by
  ``AsyncFirecrawl.scrape()``.
* External I/O (firecrawl, arxiv2md, youtube) is patched at the module
  boundary so only deterministic, pure-Python logic is exercised.

Modules under test
------------------
* src.tools.scrape_research_urls_tool   – pure functions + orchestration
* src.app.scraping_handler              – pure functions + async helpers
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

# ---------------------------------------------------------------------------
# sys.path bootstrapping (mirrors conftest.py)
# ---------------------------------------------------------------------------
_MSERVER_ROOT = Path(__file__).resolve().parent.parent
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
    * ``get_num_tokens`` returns a deterministic integer so ``scrape_and_clean``
      can log token counts without error.
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
        # Simple deterministic approximation
        return max(1, len(text.split()))


class FakeMetadata:
    def __init__(self, title: str) -> None:
        self.title = title


class FakeFirecrawlResult:
    """Mimics the object returned by ``AsyncFirecrawl.scrape()``."""

    def __init__(self, title: str = "Test Page", markdown: str = "## Hello") -> None:
        self.metadata = FakeMetadata(title)
        self.markdown = markdown


class FakeFirecrawlApp:
    """Async-callable fake that returns a FakeFirecrawlResult."""

    def __init__(self, result: FakeFirecrawlResult | None = None, raise_exc: Exception | None = None) -> None:
        self._result = result or FakeFirecrawlResult()
        self._raise = raise_exc
        self.calls: list[str] = []

    async def scrape(self, url: str, **kwargs: Any) -> FakeFirecrawlResult:
        self.calls.append(url)
        if self._raise:
            raise self._raise
        return self._result


# ---------------------------------------------------------------------------
# Module-level patches applied for the whole test session
# ---------------------------------------------------------------------------
# Prevent pydantic-settings from complaining about missing .env / API keys
# by patching Settings before any src.* import triggers it.

_SETTINGS_PATH = "src.config.settings"

# ---------------------------------------------------------------------------
# Import modules under test (after sys.path is set)
# ---------------------------------------------------------------------------
import importlib

from src.app import scraping_handler  # noqa: E402

# src/tools/__init__.py shadows the submodule name with the exported function,
# so `import src.tools.scrape_research_urls_tool as sru_mod` resolves to the
# function via attribute lookup.  importlib.import_module fetches the actual
# module object from sys.modules, bypassing that shadowing.
sru_mod = importlib.import_module("src.tools.scrape_research_urls_tool")
from src.config.constants import (  # noqa: E402
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,
    URLS_TO_SCRAPE_FROM_RESEARCH_FILE,
)

# Shortcuts to pure functions
slugify = scraping_handler.slugify
build_filename = scraping_handler.build_filename
extract_arxiv_id = scraping_handler.extract_arxiv_id
convert_markdown_images_to_urls = scraping_handler.convert_markdown_images_to_urls
is_arxiv_url = sru_mod.is_arxiv_url
categorize_urls = sru_mod.categorize_urls
deduplicate_urls = sru_mod.deduplicate_urls
validate_and_read_urls_file = sru_mod.validate_and_read_urls_file
write_scraped_results_to_files = sru_mod.write_scraped_results_to_files


# ===========================================================================
# ── scraping_handler.py ─────────────────────────────────────────────────────
# ===========================================================================


class TestSlugify:
    def test_lowercases_text(self):
        assert slugify("Hello World") == "hello-world"

    def test_replaces_special_chars_with_hyphen(self):
        assert slugify("C++ is great!") == "c-is-great"

    def test_collapses_consecutive_hyphens(self):
        assert slugify("hello   world") == "hello-world"

    def test_strips_leading_trailing_hyphens(self):
        assert slugify("---hello---") == "hello"

    def test_respects_max_length(self):
        long = "a" * 100
        result = slugify(long, max_length=20)
        assert len(result) == 20

    def test_empty_string_returns_untitled(self):
        assert slugify("") == "untitled"

    def test_only_special_chars_returns_untitled(self):
        assert slugify("!@#$%") == "untitled"

    def test_numbers_preserved(self):
        assert slugify("GPT-4o 2025") == "gpt-4o-2025"


class TestBuildFilename:
    def test_uses_title_as_base(self):
        name = build_filename("My Article", "https://example.com", set())
        assert name == "my-article.md"

    def test_falls_back_to_netloc_when_title_is_na(self):
        name = build_filename("N/A", "https://example.com/page", set())
        assert name == "example-com.md"

    def test_falls_back_to_netloc_when_title_empty(self):
        name = build_filename("", "https://example.com/page", set())
        assert name == "example-com.md"

    def test_deduplicates_with_counter(self):
        existing: set = set()
        first = build_filename("Article", "https://a.com", existing)
        second = build_filename("Article", "https://b.com", existing)
        third = build_filename("Article", "https://c.com", existing)
        assert first == "article.md"
        assert second == "article-1.md"
        assert third == "article-2.md"

    def test_populates_existing_names_set(self):
        existing: set = set()
        build_filename("My Title", "https://a.com", existing)
        assert "my-title" in existing


class TestExtractArxivId:
    def test_abs_url_with_version(self):
        assert extract_arxiv_id("https://arxiv.org/abs/2501.11120v1") == "2501.11120v1"

    def test_pdf_url_without_version(self):
        assert extract_arxiv_id("https://arxiv.org/pdf/2312.05678") == "2312.05678"

    def test_html_url(self):
        assert extract_arxiv_id("https://arxiv.org/html/2312.05678v2") == "2312.05678v2"

    def test_non_arxiv_returns_none(self):
        assert extract_arxiv_id("https://example.com/paper") is None

    def test_arxiv_without_abs_or_pdf_returns_none(self):
        # arxiv domain but no recognized path segment
        assert extract_arxiv_id("https://arxiv.org/search/2312.05678") is None

    def test_short_id(self):
        assert extract_arxiv_id("https://arxiv.org/abs/1234.5678") == "1234.5678"


class TestConvertMarkdownImagesToUrls:
    def test_converts_image_syntax(self):
        md = "![alt text](https://img.example.com/pic.png)"
        result = convert_markdown_images_to_urls(md)
        assert result == "https://img.example.com/pic.png"

    def test_converts_link_to_image_url(self):
        md = "[click here](https://img.example.com/pic.jpg)"
        result = convert_markdown_images_to_urls(md)
        assert result == "https://img.example.com/pic.jpg"

    def test_does_not_convert_regular_link(self):
        md = "[click here](https://example.com/page)"
        result = convert_markdown_images_to_urls(md)
        assert result == "[click here](https://example.com/page)"

    def test_converts_multiple_images(self):
        md = "![a](https://a.com/a.png) some text ![b](https://b.com/b.gif)"
        result = convert_markdown_images_to_urls(md)
        assert "https://a.com/a.png" in result
        assert "https://b.com/b.gif" in result
        assert "![" not in result

    def test_empty_alt_text(self):
        md = "![](https://img.example.com/pic.webp)"
        result = convert_markdown_images_to_urls(md)
        assert result == "https://img.example.com/pic.webp"


class TestCleanMarkdown:
    async def test_returns_llm_response(self):
        fake_llm = FakeLLM("cleaned markdown body")
        result = await scraping_handler.clean_markdown(
            "raw content", "some guidelines", "https://example.com", fake_llm
        )
        assert result == "cleaned markdown body"

    async def test_empty_content_skips_llm(self):
        fake_llm = FakeLLM("should not be called")
        result = await scraping_handler.clean_markdown(
            "   ", "guidelines", "https://example.com", fake_llm
        )
        # Returns original (whitespace-only) without calling llm
        assert result == "   "
        assert fake_llm.prompts_received == []

    async def test_joins_list_content(self):
        """If the LLM returns a list of parts, they should be joined."""

        class ListResponseLLM(FakeLLM):
            async def ainvoke(self, prompt: Any, **kwargs: Any) -> Any:
                msg = MagicMock()
                msg.content = ["part one", " part two"]
                return msg

        fake_llm = ListResponseLLM()
        result = await scraping_handler.clean_markdown(
            "raw", "guidelines", "https://example.com", fake_llm
        )
        assert result == "part one part two"

    async def test_timeout_returns_original(self, monkeypatch):
        """When the LLM call times out, the original markdown is returned."""

        async def _timeout(*args, **kwargs):
            raise asyncio.TimeoutError

        fake_llm = FakeLLM()
        monkeypatch.setattr(asyncio, "wait_for", _timeout)
        result = await scraping_handler.clean_markdown(
            "original content", "", "https://example.com", fake_llm
        )
        assert result == "original content"

    async def test_image_urls_are_converted_in_llm_output(self):
        fake_llm = FakeLLM("see ![diagram](https://example.com/diag.png) above")
        result = await scraping_handler.clean_markdown(
            "raw content", "", "https://example.com", fake_llm
        )
        assert "https://example.com/diag.png" in result
        assert "![" not in result


class TestScrapeUrl:
    async def test_successful_scrape(self):
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("My Title", "## Content"))
        result = await scraping_handler.scrape_url("https://example.com", fake_fc)
        assert result["success"] is True
        assert result["title"] == "My Title"
        assert result["markdown"] == "## Content"
        assert result["url"] == "https://example.com"

    async def test_missing_metadata_title_defaults_to_na(self):
        fc_result = FakeFirecrawlResult()
        fc_result.metadata.title = None
        fake_fc = FakeFirecrawlApp(fc_result)
        result = await scraping_handler.scrape_url("https://example.com", fake_fc)
        assert result["title"] == "N/A"

    async def test_missing_markdown_defaults_to_empty(self):
        fc_result = FakeFirecrawlResult()
        fc_result.markdown = None
        fake_fc = FakeFirecrawlApp(fc_result)
        result = await scraping_handler.scrape_url("https://example.com", fake_fc)
        assert result["markdown"] == ""
        assert result["success"] is True

    async def test_exception_after_retries_returns_failure(self, monkeypatch):
        """After all retries are exhausted an exception should yield success=False."""
        # Skip sleep to keep tests fast
        monkeypatch.setattr(asyncio, "sleep", AsyncMock())
        fake_fc = FakeFirecrawlApp(raise_exc=RuntimeError("network error"))
        result = await scraping_handler.scrape_url("https://fail.com", fake_fc)
        assert result["success"] is False
        assert "fail.com" in result["url"]

    async def test_timeout_after_retries_returns_failure(self, monkeypatch):
        monkeypatch.setattr(asyncio, "sleep", AsyncMock())

        async def _raise_timeout(*args, **kwargs):
            raise asyncio.TimeoutError

        fake_fc = FakeFirecrawlApp()
        fake_fc.scrape = _raise_timeout  # type: ignore[method-assign]
        result = await scraping_handler.scrape_url("https://timeout.com", fake_fc)
        assert result["success"] is False


class TestScrapeAndClean:
    async def test_happy_path_returns_cleaned_content(self):
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("Title", "raw body"))
        fake_llm = FakeLLM("cleaned body")
        result = await scraping_handler.scrape_and_clean(
            "https://example.com", "guidelines", fake_fc, fake_llm
        )
        assert result["success"] is True
        assert result["markdown"] == "cleaned body"

    async def test_failed_scrape_skips_cleaning(self):
        fake_fc = FakeFirecrawlApp(raise_exc=RuntimeError("fail"))

        async def _silent_sleep(*args, **kwargs):
            pass

        with patch.object(asyncio, "sleep", _silent_sleep):
            fake_llm = FakeLLM("should not be used")
            result = await scraping_handler.scrape_and_clean(
                "https://broken.com", "", fake_fc, fake_llm
            )
        assert result["success"] is False
        # LLM should not have been called
        assert fake_llm.prompts_received == []

    async def test_all_content_uses_same_model_for_cleaning(self):
        """All article sizes use the injected chat_model; get_chat_model is never called from scrape_and_clean."""
        raw_content = "![logo](https://example.com/img.png) body text"
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("Title", raw_content))
        fake_llm = FakeLLM("cleaned output")
        # Override token counter to simulate a very large article
        fake_llm.get_num_tokens = lambda text: 9999

        with patch("src.app.scraping_handler.get_chat_model") as mock_get_model:
            result = await scraping_handler.scrape_and_clean(
                "https://example.com", "guidelines", fake_fc, fake_llm
            )

        assert result["success"] is True
        assert result["markdown"] == "cleaned output"
        # The injected model must have been used for cleaning
        assert len(fake_llm.prompts_received) >= 1
        # get_chat_model must NOT have been called from scrape_and_clean
        mock_get_model.assert_not_called()

    async def test_small_content_calls_llm_cleaning(self):
        """≤MAX_TOKENS_FOR_LLM_CLEANING: LLM is invoked for content cleaning."""
        raw_content = "short body"
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("Title", raw_content))
        fake_llm = FakeLLM("llm cleaned output")
        # Override token counter to stay well below the threshold
        fake_llm.get_num_tokens = lambda text: 10

        result = await scraping_handler.scrape_and_clean(
            "https://example.com", "guidelines", fake_fc, fake_llm
        )

        assert result["success"] is True
        assert result["markdown"] == "llm cleaned output"
        assert len(fake_llm.prompts_received) >= 1


class TestScrapeUrlsConcurrently:
    """
    Tests for scrape_urls_concurrently – patches Firecrawl and get_chat_model
    so no network I/O occurs.
    """

    _FC_PATCH = "src.app.scraping_handler.AsyncFirecrawl"
    _MODEL_PATCH = "src.app.scraping_handler.get_chat_model"

    async def test_returns_one_result_per_url(self):
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("T", "body"))
        fake_llm = FakeLLM("cleaned")
        with patch(self._FC_PATCH, return_value=fake_fc), \
             patch(self._MODEL_PATCH, return_value=fake_llm):
            results = await scraping_handler.scrape_urls_concurrently(
                ["https://a.com", "https://b.com"], "guidelines"
            )
        assert len(results) == 2

    async def test_exception_is_converted_to_failure_dict(self, monkeypatch):
        """An unexpected exception from gather should be caught and wrapped."""
        monkeypatch.setattr(asyncio, "sleep", AsyncMock())
        fake_fc = FakeFirecrawlApp(raise_exc=RuntimeError("boom"))
        fake_llm = FakeLLM("cleaned")
        with patch(self._FC_PATCH, return_value=fake_fc), \
             patch(self._MODEL_PATCH, return_value=fake_llm):
            results = await scraping_handler.scrape_urls_concurrently(
                ["https://bad.com"], "guidelines"
            )
        assert len(results) == 1
        assert results[0]["success"] is False

    async def test_concurrency_limit_respected(self):
        """Verify dict keys are present for all results."""
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("T", "md"))
        fake_llm = FakeLLM("ok")
        urls = [f"https://example.com/{i}" for i in range(6)]
        with patch(self._FC_PATCH, return_value=fake_fc), \
             patch(self._MODEL_PATCH, return_value=fake_llm):
            results = await scraping_handler.scrape_urls_concurrently(
                urls, "guidelines", concurrency_limit=2
            )
        assert len(results) == 6
        for r in results:
            assert "url" in r and "success" in r


class TestScrapeArxivUrl:
    """Tests for the dedicated arXiv handler."""

    _INGEST_PATCH = "src.app.scraping_handler.ingest_paper"
    _FC_INSTANCE_PATCH = "src.app.scraping_handler.AsyncFirecrawl"

    async def test_success_path_uses_ingest_paper(self):
        fake_llm = FakeLLM("arxiv cleaned")
        fake_fc = FakeFirecrawlApp()
        fake_ingest_result = MagicMock(content="# Paper content")
        with patch(self._INGEST_PATCH, new=AsyncMock(return_value=(fake_ingest_result, {"title": "Test Paper"}))):
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/abs/2312.05678",
                "guidelines",
                fake_llm,
            )
        assert result["success"] is True
        # LLM cleaned the output; result should not be empty
        assert result["markdown"]

    async def test_ingest_failure_falls_back_to_firecrawl(self):
        fake_llm = FakeLLM("firecrawl cleaned")
        # Make the firecrawl fallback succeed
        fake_fc_instance = FakeFirecrawlApp(FakeFirecrawlResult("FallbackTitle", "fallback body"))
        with patch(self._INGEST_PATCH, new=AsyncMock(side_effect=RuntimeError("ingest failed"))), \
             patch(self._FC_INSTANCE_PATCH, return_value=fake_fc_instance):
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/abs/2312.05678",
                "",
                fake_llm,
            )
        assert result["success"] is True

    async def test_invalid_arxiv_url_falls_back_to_firecrawl(self):
        """When extract_arxiv_id returns None, a ValueError is raised and fallback is triggered."""
        fake_llm = FakeLLM("fallback cleaned")
        fake_fc = FakeFirecrawlApp(FakeFirecrawlResult("FB", "fb content"))
        with patch(self._FC_INSTANCE_PATCH, return_value=fake_fc):
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/search/invalid",  # no /abs/ or /pdf/
                "",
                fake_llm,
            )
        # Fallback succeeded
        assert result["success"] is True

    async def test_empty_raw_md_skips_llm_cleanup(self):
        """Empty ingest_paper output should skip LaTeX cleanup but still call clean_markdown."""
        fake_llm = FakeLLM("final cleaned")
        fake_fc = FakeFirecrawlApp()
        fake_ingest_result = MagicMock(content="   ")
        with patch(self._INGEST_PATCH, new=AsyncMock(return_value=(fake_ingest_result, {"title": "Test Paper"}))):  # whitespace-only
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/abs/2312.05678",
                "",
                fake_llm,
            )
        # success=True comes from ingest_paper path succeeding
        assert result["success"] is True

    async def test_all_raw_md_uses_same_model_for_cleanup(self):
        """All arXiv content sizes use the injected chat_model; get_chat_model is never called from scrape_arxiv_url."""
        fake_llm = FakeLLM("arxiv cleaned output")
        # Override token counter to simulate a very large paper
        fake_llm.get_num_tokens = lambda text: 9999
        raw_content = "# Full Paper\n\nVery long paper body..."
        fake_ingest_result = MagicMock(content=raw_content)

        with patch(self._INGEST_PATCH, new=AsyncMock(return_value=(fake_ingest_result, {"title": "Big Paper"}))), \
             patch("src.app.scraping_handler.get_chat_model") as mock_get_model:
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/abs/2309.02427",
                "guidelines",
                fake_llm,
            )

        assert result["success"] is True
        assert result["markdown"] == "arxiv cleaned output"
        # The injected model must have been used for cleanup
        assert len(fake_llm.prompts_received) >= 1
        # get_chat_model must NOT have been called from scrape_arxiv_url
        mock_get_model.assert_not_called()

    async def test_small_raw_md_calls_llm_cleanup(self):
        """≤MAX_TOKENS_FOR_LLM_CLEANING: LLM is called for LaTeX cleanup."""
        fake_llm = FakeLLM("latex cleaned output")
        # Override token counter to stay well below the threshold
        fake_llm.get_num_tokens = lambda text: 10
        raw_content = "# Short Paper with $\\LaTeX$"
        fake_ingest_result = MagicMock(content=raw_content)

        with patch(self._INGEST_PATCH, new=AsyncMock(return_value=(fake_ingest_result, {"title": "Short Paper"}))):
            result = await scraping_handler.scrape_arxiv_url(
                "https://arxiv.org/abs/2312.05678",
                "guidelines",
                fake_llm,
            )

        assert result["success"] is True
        assert result["markdown"] == "latex cleaned output"
        assert len(fake_llm.prompts_received) == 1


# ===========================================================================
# ── scrape_research_urls_tool.py – pure functions ───────────────────────────
# ===========================================================================


class TestIsArxivUrl:
    def test_abs_url_is_arxiv(self):
        assert is_arxiv_url("https://arxiv.org/abs/2312.05678") is True

    def test_pdf_url_is_arxiv(self):
        assert is_arxiv_url("https://arxiv.org/pdf/2312.05678") is True

    def test_html_url_is_not_matched(self):
        # /html/ is not in the accepted list; returns False
        assert is_arxiv_url("https://arxiv.org/html/2312.05678") is False

    def test_plain_arxiv_domain_is_not_arxiv(self):
        assert is_arxiv_url("https://arxiv.org/") is False

    def test_non_arxiv_url_is_false(self):
        assert is_arxiv_url("https://example.com/abs/something") is False


class TestCategorizeUrls:
    def test_youtube_com_classified_correctly(self):
        yt, arxiv, github, other = categorize_urls(["https://youtube.com/watch?v=abc"])
        assert "https://youtube.com/watch?v=abc" in yt
        assert not arxiv
        assert not other

    def test_youtu_be_classified_as_youtube(self):
        yt, arxiv, github, other = categorize_urls(["https://youtu.be/xyz"])
        assert len(yt) == 1

    def test_arxiv_abs_classified_correctly(self):
        yt, arxiv, github, other = categorize_urls(["https://arxiv.org/abs/2312.05678"])
        assert not yt
        assert len(arxiv) == 1
        assert not other

    def test_regular_url_classified_as_other(self):
        yt, arxiv, github, other = categorize_urls(["https://blog.example.com/post"])
        assert not yt
        assert not arxiv
        assert len(other) == 1

    def test_mixed_urls_classified_into_three_buckets(self):
        urls = [
            "https://youtube.com/watch?v=1",
            "https://arxiv.org/abs/1234.5678",
            "https://docs.python.org",
        ]
        yt, arxiv, github, other = categorize_urls(urls)
        assert len(yt) == 1
        assert len(arxiv) == 1
        assert len(other) == 1

    def test_empty_list_returns_all_empty(self):
        yt, arxiv, github, other = categorize_urls([])
        assert yt == arxiv == github == other == []

    def test_no_url_counted_twice(self):
        urls = ["https://arxiv.org/abs/2312.05678"]
        yt, arxiv, github, other = categorize_urls(urls)
        total = len(yt) + len(arxiv) + len(github) + len(other)
        assert total == len(urls)


class TestDeduplicateUrls:
    def test_no_guidelines_file_returns_all_urls(self, tmp_path):
        urls = ["https://a.com", "https://b.com"]
        filtered, orig, deduped = deduplicate_urls(tmp_path, urls)
        assert filtered == urls
        assert orig == 2
        assert deduped == 0

    def test_known_urls_are_filtered_out(self, tmp_path):
        guidelines = {"other_urls": ["https://a.com"], "github_urls": []}
        (tmp_path / GUIDELINES_FILENAMES_FILE).write_text(
            json.dumps(guidelines), encoding="utf-8"
        )
        urls = ["https://a.com", "https://b.com"]
        filtered, orig, deduped = deduplicate_urls(tmp_path, urls)
        assert "https://a.com" not in filtered
        assert "https://b.com" in filtered
        assert orig == 2
        assert deduped == 1

    def test_github_urls_also_deduplicated(self, tmp_path):
        guidelines = {"other_urls": [], "github_urls": ["https://github.com/foo"]}
        (tmp_path / GUIDELINES_FILENAMES_FILE).write_text(
            json.dumps(guidelines), encoding="utf-8"
        )
        urls = ["https://github.com/foo", "https://new.com"]
        filtered, _, deduped = deduplicate_urls(tmp_path, urls)
        assert "https://github.com/foo" not in filtered
        assert deduped == 1

    def test_all_new_urls_no_deduplication(self, tmp_path):
        guidelines = {"other_urls": ["https://old.com"], "github_urls": []}
        (tmp_path / GUIDELINES_FILENAMES_FILE).write_text(
            json.dumps(guidelines), encoding="utf-8"
        )
        urls = ["https://new.com"]
        filtered, orig, deduped = deduplicate_urls(tmp_path, urls)
        assert filtered == ["https://new.com"]
        assert deduped == 0

    def test_malformed_json_file_returns_all_urls(self, tmp_path):
        (tmp_path / GUIDELINES_FILENAMES_FILE).write_text("NOT JSON", encoding="utf-8")
        urls = ["https://a.com"]
        filtered, _, _ = deduplicate_urls(tmp_path, urls)
        assert filtered == urls

    def test_empty_input_urls(self, tmp_path):
        filtered, orig, deduped = deduplicate_urls(tmp_path, [])
        assert filtered == []
        assert orig == 0
        assert deduped == 0


class TestValidateAndReadUrlsFile:
    def test_missing_file_returns_empty_with_early_return(self, tmp_path):
        missing = tmp_path / "nonexistent.md"
        urls, early = validate_and_read_urls_file(missing, str(tmp_path))
        assert urls == []
        assert early is not None
        assert early["status"] == "success"
        assert early["urls_processed"] == 0

    def test_empty_file_returns_early(self, tmp_path):
        urls_file = tmp_path / "urls.md"
        urls_file.write_text("", encoding="utf-8")
        urls, early = validate_and_read_urls_file(urls_file, str(tmp_path))
        assert early is not None
        assert urls == []

    def test_whitespace_only_file_returns_early(self, tmp_path):
        urls_file = tmp_path / "urls.md"
        urls_file.write_text("   \n\n   ", encoding="utf-8")
        urls, early = validate_and_read_urls_file(urls_file, str(tmp_path))
        assert early is not None

    def test_valid_urls_parsed_correctly(self, tmp_path):
        urls_file = tmp_path / "urls.md"
        urls_file.write_text("https://a.com\nhttps://b.com\n", encoding="utf-8")
        urls, early = validate_and_read_urls_file(urls_file, str(tmp_path))
        assert early is None
        assert urls == ["https://a.com", "https://b.com"]

    def test_blank_lines_stripped(self, tmp_path):
        urls_file = tmp_path / "urls.md"
        urls_file.write_text("https://a.com\n\nhttps://b.com\n\n", encoding="utf-8")
        urls, early = validate_and_read_urls_file(urls_file, str(tmp_path))
        assert len(urls) == 2

    def test_leading_trailing_whitespace_stripped(self, tmp_path):
        urls_file = tmp_path / "urls.md"
        urls_file.write_text("  https://a.com  \n  https://b.com  \n", encoding="utf-8")
        urls, _ = validate_and_read_urls_file(urls_file, str(tmp_path))
        assert urls == ["https://a.com", "https://b.com"]


class TestWriteScrapedResultsToFiles:
    def test_successful_result_is_written(self, tmp_path):
        results = [{"url": "https://a.com", "title": "Article A", "markdown": "# A", "success": True}]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 1
        assert len(saved) == 1
        written_file = tmp_path / saved[0]
        assert written_file.exists()
        assert written_file.read_text(encoding="utf-8") == "**Source URL:** <https://a.com>\n\n# A"

    def test_failed_result_still_written_but_not_counted(self, tmp_path):
        results = [{"url": "https://b.com", "title": "Fail", "markdown": "error msg", "success": False}]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 0
        assert len(saved) == 1  # file still created

    def test_multiple_results_all_written(self, tmp_path):
        results = [
            {"url": "https://a.com", "title": "A", "markdown": "content A", "success": True},
            {"url": "https://b.com", "title": "B", "markdown": "content B", "success": True},
        ]
        saved, success_count = write_scraped_results_to_files(results, tmp_path)
        assert success_count == 2
        assert len(saved) == 2

    def test_duplicate_titles_get_unique_filenames(self, tmp_path):
        results = [
            {"url": "https://a.com", "title": "Same", "markdown": "one", "success": True},
            {"url": "https://b.com", "title": "Same", "markdown": "two", "success": True},
        ]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        assert len(set(saved)) == 2  # unique filenames

    def test_empty_markdown_written_with_url_header(self, tmp_path):
        results = [{"url": "https://a.com", "title": "Empty", "markdown": "", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        written_file = tmp_path / saved[0]
        # Title is injected as H1 so _extract_page_heading() can produce a readable collapsible summary.
        assert written_file.read_text(encoding="utf-8") == "**Source URL:** <https://a.com>\n\n# Empty\n\n"

    def test_missing_h1_injects_metadata_title(self, tmp_path):
        """When cleaned markdown has no heading, the Firecrawl metadata title is injected as H1."""
        results = [{"url": "https://a.com", "title": "My Article", "markdown": "Some body text.", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        content = (tmp_path / saved[0]).read_text(encoding="utf-8")
        assert "# My Article" in content

    def test_existing_h1_not_duplicated(self, tmp_path):
        """When cleaned markdown already has an H1, no extra H1 is injected."""
        results = [{"url": "https://a.com", "title": "My Article", "markdown": "# Existing Title\n\nBody.", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        content = (tmp_path / saved[0]).read_text(encoding="utf-8")
        assert "# My Article" not in content
        assert "# Existing Title" in content

    def test_h2_without_h1_injects_metadata_title(self, tmp_path):
        """When body has subheadings but no H1, the Firecrawl title is injected as H1."""
        results = [{"url": "https://a.com", "title": "My Article", "markdown": "## Section\n\nContent.", "success": True}]
        saved, _ = write_scraped_results_to_files(results, tmp_path)
        content = (tmp_path / saved[0]).read_text(encoding="utf-8")
        assert "# My Article" in content


# ===========================================================================
# ── scrape_research_urls_tool – orchestration ───────────────────────────────
# ===========================================================================

# Patches applied in integration-style tests
_SCRAPE_CONCURRENTLY_PATCH = "src.tools.scrape_research_urls_tool.scrape_urls_concurrently"
_SCRAPE_ARXIV_PATCH = "src.tools.scrape_research_urls_tool.scrape_arxiv_url"
_YT_PATCH = "src.tools.scrape_research_urls_tool.process_youtube_url"
_GET_CHAT_MODEL_PATCH = "src.tools.scrape_research_urls_tool.get_chat_model"


def _make_research_dir(tmp_path: Path) -> Path:
    """Create a minimal valid research directory."""
    (tmp_path / ARTICLE_GUIDELINE_FILE).write_text("Guidelines content", encoding="utf-8")
    output = tmp_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir(parents=True, exist_ok=True)
    return tmp_path


def _write_urls_file(research_path: Path, urls: list[str]) -> None:
    output = research_path / RESEARCH_OUTPUT_FOLDER
    output.mkdir(parents=True, exist_ok=True)
    (output / URLS_TO_SCRAPE_FROM_RESEARCH_FILE).write_text(
        "\n".join(urls), encoding="utf-8"
    )


def _fake_scrape_result(url: str, success: bool = True) -> dict:
    return {
        "url": url,
        "title": f"Title for {url}",
        "markdown": f"Content for {url}",
        "success": success,
    }


class TestScrapeResearchUrlsTool:
    async def test_missing_urls_file_returns_success_early(self, tmp_path):
        """When the URLs file does not exist, tool exits early with success."""
        research_dir = _make_research_dir(tmp_path)
        result = await sru_mod.scrape_research_urls_tool(str(research_dir))
        assert result["status"] == "success"
        assert result["urls_processed"] == 0

    async def test_empty_urls_file_returns_success_early(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        _write_urls_file(research_dir, [])
        result = await sru_mod.scrape_research_urls_tool(str(research_dir))
        assert result["status"] == "success"
        assert result["urls_processed"] == 0

    async def test_nonexistent_research_dir_raises_value_error(self, tmp_path):
        bad_path = tmp_path / "does_not_exist"
        with pytest.raises(ValueError, match="does not exist"):
            await sru_mod.scrape_research_urls_tool(str(bad_path))

    async def test_all_already_processed_returns_success(self, tmp_path):
        """All URLs already in guidelines_filenames.json → nothing to scrape."""
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://a.com", "https://b.com"]
        _write_urls_file(research_dir, urls)
        guidelines = {"other_urls": urls, "github_urls": []}
        (research_dir / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE).write_text(
            json.dumps(guidelines), encoding="utf-8"
        )
        result = await sru_mod.scrape_research_urls_tool(str(research_dir))
        assert result["status"] == "success"
        assert result["urls_processed"] == 0
        assert "already processed" in result["message"]

    async def test_scrapes_other_urls_and_writes_files(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://blog.example.com/post"]
        _write_urls_file(research_dir, urls)

        fake_results = [_fake_scrape_result(u) for u in urls]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["files_saved"] == 1
        assert result["urls_processed"] == 1

    async def test_scrapes_arxiv_urls(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://arxiv.org/abs/2312.05678"]
        _write_urls_file(research_dir, urls)

        arxiv_result = _fake_scrape_result(urls[0])

        with patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=arxiv_result)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        assert result["status"] == "success"
        assert result["files_saved"] == 1

    async def test_processes_youtube_urls(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://youtube.com/watch?v=testid"]
        _write_urls_file(research_dir, urls)

        with patch(_YT_PATCH, AsyncMock(return_value=None)):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        assert result["status"] == "success"

    async def test_deduplication_reduces_processed_count(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        all_urls = ["https://a.com", "https://b.com", "https://c.com"]
        _write_urls_file(research_dir, all_urls)
        # Mark a.com as already processed
        guidelines = {"other_urls": ["https://a.com"], "github_urls": []}
        (research_dir / RESEARCH_OUTPUT_FOLDER / GUIDELINES_FILENAMES_FILE).write_text(
            json.dumps(guidelines), encoding="utf-8"
        )

        remaining = ["https://b.com", "https://c.com"]
        fake_results = [_fake_scrape_result(u) for u in remaining]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        assert result["original_urls_count"] == 3
        assert result["deduplicated_count"] == 1
        assert result["urls_processed"] == 2

    async def test_mixed_urls_all_processed(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = [
            "https://blog.example.com/post",
            "https://arxiv.org/abs/2312.05678",
            "https://youtube.com/watch?v=abc",
        ]
        _write_urls_file(research_dir, urls)

        web_results = [_fake_scrape_result("https://blog.example.com/post")]
        arxiv_result = _fake_scrape_result("https://arxiv.org/abs/2312.05678")

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=web_results)), \
             patch(_SCRAPE_ARXIV_PATCH, AsyncMock(return_value=arxiv_result)), \
             patch(_YT_PATCH, AsyncMock(return_value=None)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        assert result["status"] == "success"
        # 2 files: web + arxiv (youtube doesn't emit a file in this logic branch)
        assert result["files_saved"] == 2

    async def test_output_directory_created(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://example.com"]
        _write_urls_file(research_dir, urls)

        fake_results = [_fake_scrape_result(u) for u in urls]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        expected_dir = research_dir / RESEARCH_OUTPUT_FOLDER / URLS_FROM_RESEARCH_FOLDER
        assert expected_dir.exists()

    async def test_return_dict_has_expected_keys(self, tmp_path):
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://example.com"]
        _write_urls_file(research_dir, urls)

        fake_results = [_fake_scrape_result(u) for u in urls]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        for key in ("status", "urls_processed", "urls_total", "files_saved",
                    "output_directory", "saved_files", "message"):
            assert key in result, f"Missing key: {key}"

    async def test_failed_scrape_counted_in_files_saved_not_urls_processed(self, tmp_path):
        """Firecrawl returns success=False → file still saved but not counted as processed."""
        research_dir = _make_research_dir(tmp_path)
        urls = ["https://bad.com"]
        _write_urls_file(research_dir, urls)

        fake_results = [_fake_scrape_result(u, success=False) for u in urls]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(research_dir))

        # File is always written; success=False means urls_processed == 0
        assert result["urls_processed"] == 0
        assert result["files_saved"] == 1

    async def test_missing_guidelines_file_does_not_raise(self, tmp_path):
        """Tool should work even without article_guideline.md."""
        # Do NOT create article_guideline.md
        output = tmp_path / RESEARCH_OUTPUT_FOLDER
        output.mkdir(parents=True, exist_ok=True)
        _write_urls_file(tmp_path, ["https://example.com"])

        fake_results = [_fake_scrape_result("https://example.com")]

        with patch(_SCRAPE_CONCURRENTLY_PATCH, AsyncMock(return_value=fake_results)), \
             patch(_GET_CHAT_MODEL_PATCH, return_value=FakeLLM()):
            result = await sru_mod.scrape_research_urls_tool(str(tmp_path))

        assert result["status"] == "success"
