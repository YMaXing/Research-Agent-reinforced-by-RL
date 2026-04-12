"""Web scraping utilities."""

import asyncio
import logging
import re
from typing import List
from urllib.parse import urlparse

from firecrawl import AsyncFirecrawl
from langchain.chat_models.base import BaseChatModel
from arxiv2md import ingest_paper

from ..config.prompts import PROMPT_CLEAN_ARXIV_MARKDOWN, PROMPT_CLEAN_MARKDOWN
from ..config.settings import settings
from ..utils.llm_utils import get_chat_model

logger = logging.getLogger(__name__)

# Cache settings for faster scraping
# maxAge values in milliseconds:
# 5 minutes: 300000, 1 hour: 3600000, 1 day: 86400000, 1 week: 604800000
MAX_AGE_ONE_WEEK = 604800000  # 1 week in milliseconds for 500% faster scraping

# LLM cleaning uses two models depending on article size:
# - Small articles (≤ MAX_TOKENS_FOR_LLM_CLEANING): cleaned by settings.scraping_model
#   (e.g. grok-4-1-fast-reasoning), which has a limited combined context window.
#   Once the input (article + guidelines + prompt) exceeds ~11K tokens there is
#   almost no room for the output, causing truncation mid-sentence.
# - Large articles (> MAX_TOKENS_FOR_LLM_CLEANING): cleaned by
#   settings.large_article_scraping_model (default: gemini-2.5-flash), which
#   supports a 1M token input context window and can handle full articles in
#   a single pass without truncation.
MAX_TOKENS_FOR_LLM_CLEANING = settings.max_tokens_for_llm_cleaning


def slugify(text: str, max_length: int = 60) -> str:
    """Convert text to a filesystem-friendly slug."""
    text = text.lower()
    # Replace non-alphanumeric characters with hyphens
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text[:max_length] or "untitled"


def build_filename(title: str, url: str, existing_names: set) -> str:
    """Generate a unique filename for a scraped source."""
    base_name = slugify(title) if title and title.lower() != "n/a" else slugify(urlparse(url).netloc)
    candidate = base_name
    counter = 1
    while candidate in existing_names:
        candidate = f"{base_name}-{counter}"
        counter += 1
    existing_names.add(candidate)
    return f"{candidate}.md"


async def scrape_url(url: str, firecrawl_app: AsyncFirecrawl) -> dict:
    """
    Scrape a URL using Firecrawl with retries and return a dict with url, title, markdown.

    Uses maxAge=1 week for 500% faster scraping by leveraging cached data when available.
    This optimization significantly improves performance for documentation, articles, and
    relatively static content while maintaining freshness within acceptable limits.
    """
    max_retries = 3
    base_delay = 5  # seconds
    timeout_seconds = 120000  # 2 minutes timeout per request

    for attempt in range(max_retries):
        try:
            # Add timeout to individual Firecrawl request
            # Use maxAge=1 week for 500% faster scraping with cached data
            res = await firecrawl_app.scrape(
                url, formats=["markdown"], maxAge=MAX_AGE_ONE_WEEK, timeout=timeout_seconds
            )
            title = res.metadata.title if res and res.metadata and res.metadata.title else "N/A"
            markdown_content = res.markdown if res and res.markdown else ""
            return {"url": url, "title": title, "markdown": markdown_content, "success": True}
        except asyncio.TimeoutError:
            error_msg = f"⚠️ Firecrawl request timed out after {timeout_seconds}s for {url}"
            logger.warning(f"{error_msg} (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                logger.warning(f"Retrying in {delay}s...")
                await asyncio.sleep(delay)
            else:
                logger.error(f"{error_msg} after {max_retries} attempts")
                return {
                    "url": url,
                    "title": "Scraping Timeout",
                    "markdown": f"{error_msg} after {max_retries} attempts.",
                    "success": False,
                }
        except Exception as e:
            # print the error with traceback
            logger.error(f"Error scraping {url}: {e}", exc_info=True)

            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                logger.warning(f"⚠️ Error scraping {url} (attempt {attempt + 1}/{max_retries}). Retrying in {delay}s...")
                await asyncio.sleep(delay)
            else:
                msg = f"⚠️ Error scraping {url} after {max_retries} attempts: {e}"
                logger.error(msg, exc_info=True)
                return {
                    "url": url,
                    "title": "Scraping Failed",
                    "markdown": msg,
                    "success": False,
                }
    return {
        "url": url,
        "title": "Scraping Failed",
        "markdown": f"⚠️ Error scraping {url} after {max_retries} attempts.",
        "success": False,
    }


def extract_arxiv_id(url: str) -> str | None:
    """Extract the arXiv ID from an arXiv URL.

    Examples
    --------
    >>> extract_arxiv_id("https://arxiv.org/abs/2501.11120v1")
    '2501.11120v1'
    >>> extract_arxiv_id("https://arxiv.org/pdf/2501.11120v1")
    '2501.11120v1'
    """
    match = re.search(r'arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5}(?:v\d+)?)', url)
    return match.group(1) if match else None


def arxiv_html_url(arxiv_id: str) -> str:
    """Return the canonical arxiv.org HTML URL for a given arXiv ID."""
    return f"https://arxiv.org/html/{arxiv_id}"


# ─────────────────────────────────────────────────────────────
# arXiv special handler (added for high-quality paper scraping)
# ─────────────────────────────────────────────────────────────

# Tiny private helper for fallback (keeps the main function clean)
async def _fallback_firecrawl_scrape(url: str) -> dict:
    """Fallback using a fresh Firecrawl instance."""
    firecrawl_app = AsyncFirecrawl(api_key=settings.firecrawl_api_key.get_secret_value())
    return await scrape_url(url, firecrawl_app)


async def scrape_arxiv_url(
    url: str,
    article_guidelines: str,
    chat_model,
) -> dict:
    """
    Dedicated handler for arXiv URLs.
    1. Uses arxiv2markdown (best quality).
    2. Runs a lightweight LLM cleanup to fix any remaining LaTeX quirks.
    3. Falls back to Firecrawl if arxiv2markdown fails.
    4. Then runs the normal clean_markdown step.
    """
    logger.info(f"🔬 Detected arXiv URL, using arxiv2markdown: {url}")

    try:
        # Primary path: arxiv2markdown
        arxiv_id = extract_arxiv_id(url)
        if not arxiv_id:
            raise ValueError(f"Could not extract arXiv ID from URL: {url}")
        version_match = re.search(r"(v\d+)$", arxiv_id)
        version = version_match.group(1) if version_match else None
        html_url = arxiv_html_url(arxiv_id)
        result, metadata = await ingest_paper(
            arxiv_id=arxiv_id,
            version=version,
            html_url=html_url,
            remove_refs=True,
            remove_toc=True,
            remove_inline_citations=True,
            section_filter_mode="exclude",
            sections=[],
        )
        raw_md = result.content
        logger.info(f"✅ arxiv2markdown succeeded for {url}")

        # Automatic LLM post-processing for LaTeX quirks — skipped for large papers.
        # arxiv2markdown output for long papers (e.g. 50K+ tokens) already exceeds
        # the model's combined context window, causing the output to be truncated
        # mid-sentence. arxiv2markdown already produces clean Markdown for large
        # papers, so skipping the LLM pass and keeping the raw output is the right
        # trade-off.
        raw_token_count = chat_model.get_num_tokens(raw_md) if raw_md.strip() else 0
        if raw_md.strip() and raw_token_count <= MAX_TOKENS_FOR_LLM_CLEANING:
            logger.info(f"🧼 Running arXiv-specific LaTeX cleanup on {url}")
            # Use .replace() instead of .format() to avoid KeyError when the
            # paper content itself contains {…} patterns (e.g. LaTeX environments
            # like "{equation}" rendered by arxiv2markdown).
            clean_prompt = (
                PROMPT_CLEAN_ARXIV_MARKDOWN
                .replace("{article_guidelines}", article_guidelines or "<none>")
                .replace("{arxiv_markdown}", raw_md)
            )
            try:
                response = await chat_model.ainvoke(clean_prompt)
                cleaned_md = response.content if hasattr(response, "content") else str(response)
                logger.info(f"✅ arXiv LaTeX cleanup completed for {url}")
            except Exception as e:
                logger.warning(f"arXiv cleanup LLM failed for {url}: {e}. Using raw output.")
                cleaned_md = raw_md
        else:
            if raw_token_count > MAX_TOKENS_FOR_LLM_CLEANING:
                logger.info(
                    f"🔄 arXiv paper too large for {settings.scraping_model} "
                    f"({raw_token_count} tokens > {MAX_TOKENS_FOR_LLM_CLEANING} threshold). "
                    f"Using {settings.large_article_scraping_model} for cleanup."
                )
                large_chat_model = get_chat_model(settings.large_article_scraping_model)
                large_clean_prompt = (
                    PROMPT_CLEAN_ARXIV_MARKDOWN
                    .replace("{article_guidelines}", article_guidelines or "<none>")
                    .replace("{arxiv_markdown}", raw_md)
                )
                try:
                    response = await large_chat_model.ainvoke(large_clean_prompt)
                    cleaned_md = response.content if hasattr(response, "content") else str(response)
                    logger.info(f"✅ arXiv LaTeX cleanup (large model) completed for {url}")
                except Exception as e:
                    logger.warning(f"arXiv cleanup (large model) failed for {url}: {e}. Using raw output.")
                    cleaned_md = raw_md
            else:
                cleaned_md = raw_md

        scraped = {
            "url": url,
            "title": metadata.get("title") or "arXiv Paper",
            "markdown": cleaned_md,
            "success": True,
        }
    except Exception as e:
        logger.warning(f"arxiv2markdown failed for {url}: {e}. Falling back to Firecrawl.")
        scraped = await _fallback_firecrawl_scrape(url)
        # Run the regular web-page cleaning step only for the Firecrawl fallback path,
        # since arxiv2markdown output does not contain web-page boilerplate and the
        # PROMPT_CLEAN_ARXIV_MARKDOWN step already handled all necessary cleanup.
        # Skipping this for the primary path prevents a second full-paper LLM pass
        # that would truncate long articles due to output-token limits.
        if scraped.get("success", False):
            final_cleaned = await clean_markdown(
                scraped["markdown"], article_guidelines, url, chat_model
            )
            scraped["markdown"] = final_cleaned

    return scraped


def convert_markdown_images_to_urls(text: str) -> str:
    """Convert markdown image and link syntax to just URLs for image content."""
    # Convert markdown images ![alt](url) to just url
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"\2", text)

    # Convert markdown links [text](url) to just url when url appears to be an image
    # Common image extensions
    image_extensions = r"\.(jpg|jpeg|png|gif|bmp|svg|webp|ico|tiff|tif)(\?[^)]*)?"
    text = re.sub(rf"\[([^\]]*)\]\(([^)]+{image_extensions})\)", r"\2", text, flags=re.IGNORECASE)

    return text


async def clean_markdown(
    markdown_content: str, article_guidelines: str, url_for_log: str, chat_model: BaseChatModel
) -> str:
    """Clean markdown content via LLM and convert image syntax to URLs."""
    if not markdown_content.strip():
        return markdown_content

    prompt_text = (
        PROMPT_CLEAN_MARKDOWN
        .replace("{article_guidelines}", article_guidelines)
        .replace("{markdown_content}", markdown_content)
    )
    timeout_seconds = 180  # 3 minutes timeout for LLM call

    try:
        # Add timeout to LLM API call
        response = await asyncio.wait_for(chat_model.ainvoke(prompt_text), timeout=timeout_seconds)
        cleaned_content = response.content if hasattr(response, "content") else str(response)

        if isinstance(cleaned_content, list):
            cleaned_content = "".join(str(part) for part in cleaned_content)

        # Post-process: convert markdown images to just URLs
        cleaned_content = convert_markdown_images_to_urls(cleaned_content)

        return cleaned_content
    except asyncio.TimeoutError:
        logger.error(f"LLM API call timed out after {timeout_seconds}s for {url_for_log}. Using original content.")
        return markdown_content
    except Exception as e:
        logger.error(f"Error cleaning markdown for {url_for_log}: {e}. Using original content.", exc_info=True)
        return markdown_content


async def scrape_and_clean(url: str, article_guidelines: str, firecrawl_app: AsyncFirecrawl, chat_model) -> dict:
    """Scrape and clean a single URL, returning dict with url, title, markdown."""
    scraped = await scrape_url(url, firecrawl_app)
    status_marker = "✓" if scraped["success"] else "✗"
    number_of_tokens = chat_model.get_num_tokens(scraped["markdown"])
    token_info = f" ({number_of_tokens} tokens)"
    logger.info(f"📥 Scraped: {url} {status_marker}{token_info}")
    if scraped["success"]:
        if number_of_tokens > MAX_TOKENS_FOR_LLM_CLEANING:
            # Article exceeds the default scraping model's context window.
            # Route to the large-article model (e.g. gemini-2.5-flash, 1M tokens)
            # so the full content is cleaned in a single pass without truncation.
            logger.info(
                f"🔄 Article too large for {settings.scraping_model} "
                f"({number_of_tokens} tokens > {MAX_TOKENS_FOR_LLM_CLEANING} threshold). "
                f"Using {settings.large_article_scraping_model} for cleaning."
            )
            large_chat_model = get_chat_model(settings.large_article_scraping_model)
            cleaned_md = await clean_markdown(scraped["markdown"], article_guidelines, url, large_chat_model)
        else:
            cleaned_md = await clean_markdown(scraped["markdown"], article_guidelines, url, chat_model)
        scraped["markdown"] = cleaned_md
        number_of_tokens = chat_model.get_num_tokens(scraped["markdown"])
        token_info = f" (tokens: {number_of_tokens})"
        logger.info(f"🧼 Cleaned: {url} {token_info}")
    return scraped


async def scrape_urls_concurrently(
    other_urls: List[str], article_guidelines: str, concurrency_limit: int = 4
) -> List[dict]:
    """
    Scrape and clean multiple URLs concurrently.

    Args:
        other_urls: List of URLs to scrape
        article_guidelines: Guidelines content for cleaning scraped data
        concurrency_limit: Maximum number of concurrent tasks

    Returns:
        List of scraping results, each containing the scraped data or error information
    """
    # Initialize clients
    firecrawl_app = AsyncFirecrawl(api_key=settings.firecrawl_api_key.get_secret_value())
    chat_model = get_chat_model(settings.scraping_model)
    logger.info(f"Starting scraping of {len(other_urls)} URL(s) with a concurrency limit of {concurrency_limit}...")

    semaphore = asyncio.Semaphore(concurrency_limit)

    async def scrape_with_semaphore(url: str, guidelines: str) -> dict:
        async with semaphore:
            return await scrape_and_clean(url, guidelines, firecrawl_app, chat_model)

    # Process URLs concurrently
    tasks = [scrape_with_semaphore(url, article_guidelines) for url in other_urls]
    completed_results = await asyncio.gather(*tasks, return_exceptions=True)

    # Process results and handle exceptions
    processed_results = []
    for i, res in enumerate(completed_results):
        url_for_processing = other_urls[i]

        if isinstance(res, Exception):
            logger.error(f"✗ Unexpected error processing {url_for_processing}: {res}", exc_info=True)
            res = {
                "url": url_for_processing,
                "title": "Unexpected Processing Error",
                "markdown": f"An unexpected error occurred for {url_for_processing}:\n\n{res}",
                "success": False,
            }
        assert isinstance(res, dict)
        processed_results.append(res)

    return processed_results
