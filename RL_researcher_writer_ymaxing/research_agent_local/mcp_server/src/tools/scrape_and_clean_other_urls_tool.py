"""Scrape and clean other URLs tool implementation."""

import json
import logging
import asyncio
from pathlib import Path
from typing import Any, Dict, List, Tuple

from ..app.scraping_handler import build_filename, scrape_urls_concurrently
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_FOLDER,
)
from ..utils.file_utils import (
    read_file_safe,
    validate_guidelines_file,
    validate_guidelines_filenames_file,
    validate_research_folder,
)
from ..app.scraping_handler import scrape_arxiv_url
from ..utils.llm_utils import get_chat_model
from ..config.settings import settings

logger = logging.getLogger(__name__)


def write_scraped_results_to_files(completed_results: List[dict], output_dir: Path) -> Tuple[List[str], int]:
    """
    Write scraped results to markdown files and return statistics.

    Args:
        completed_results: List of scraping results from scrape_urls_concurrently
        output_dir: Directory to write the markdown files to

    Returns:
        Tuple of (saved_files_list, successful_scrapes_count)
    """
    saved_files = []
    successful_scrapes = 0
    existing_names: set[str] = set()

    for res in completed_results:
        # asyncio.gather(return_exceptions=True) can return exception objects;
        # skip them gracefully instead of crashing on .get().
        if isinstance(res, BaseException):
            logger.warning(f"Skipping failed scrape result (exception): {res}")
            continue
        cleaned_markdown = res.get("markdown", "")
        title = res.get("title", "")
        url = res.get("url", "")

        if res.get("success", False):
            successful_scrapes += 1

        url_header = f"**Source URL:** <{url}>\n\n" if url else ""
        filename = build_filename(title, url, existing_names)
        output_path = output_dir / filename
        md_body = cleaned_markdown or ""
        # Inject H1 title before the URL header so get_first_line_title() picks it up
        # as the collapsible <summary> text when LLM cleaning removed the article H1.
        if title and title.lower() not in {"n/a", "scraping timeout", "scraping failed", ""} and not any(
            ln.strip().startswith("#") for ln in md_body.splitlines()
        ):
            file_content = f"# {title}\n\n{url_header}{md_body}"
        else:
            file_content = url_header + md_body
        output_path.write_text(file_content, encoding="utf-8")
        saved_files.append(filename)

    return saved_files, successful_scrapes


async def scrape_and_clean_other_urls_tool(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
    """
    Scrape and clean other URLs (including arxiv URLs) from guidelines file in the research folder.

    Reads the guidelines file and scrapes/cleans each URL listed
    under 'other_urls'. The cleaned markdown content is saved to the
    URLS_FROM_GUIDELINES_FOLDER subfolder with appropriate filenames.

    Args:
        research_directory: Path to the research folder containing the guidelines file
        concurrency_limit: Maximum number of concurrent tasks for scraping (default: 4)

    Returns:
        Dict with status, processing results, and file paths
    """
    logger.info(f"Scraping and cleaning other URLs from research folder: {research_directory}")

    # Convert to Path object
    research_path = Path(research_directory)
    research_output_path = research_path / RESEARCH_OUTPUT_FOLDER

    # Validate folders and files
    validate_research_folder(research_path)

    # Look for GUIDELINES_FILENAMES_FILE file
    guidelines_json_path = research_output_path / GUIDELINES_FILENAMES_FILE

    # Validate the guidelines filenames file
    validate_guidelines_filenames_file(guidelines_json_path)

    # Read the guidelines JSON file
    try:
        with open(guidelines_json_path, "r", encoding="utf-8") as f:
            guidelines_data = json.load(f)
    except (IOError, OSError, json.JSONDecodeError) as e:
        msg = f"Error reading {GUIDELINES_FILENAMES_FILE}: {str(e)}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    # Get the other_urls list
    def is_arxiv_url(url: str) -> bool:
        """Return True if URL is an arXiv link (abs, pdf, or html)."""
        return "arxiv.org" in url and ("/abs/" in url or "/pdf/" in url or "/html/" in url)
    
    other_urls = [url for url in guidelines_data.get("other_urls", []) if not is_arxiv_url(url)]
    arxiv_urls = [url for url in guidelines_data.get("other_urls", []) if is_arxiv_url(url)]
    
    if not other_urls and not arxiv_urls:
        return {
            "status": "success",
            "message": f"No other URLs found in {GUIDELINES_FILENAMES_FILE} in '{research_directory}'",
            "urls_processed": 0,
            "urls_total": 0,
            "files_saved": 0,
        }

    # Look for ARTICLE_GUIDELINE_FILE file to get the guidelines content
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE

    # Validate the guidelines file
    validate_guidelines_file(guidelines_path)

    # Read the article guidelines
    try:
        article_guidelines = read_file_safe(guidelines_path)
    except (IOError, OSError) as e:
        msg = f"Error reading {ARTICLE_GUIDELINE_FILE}: {str(e)}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    # Prepare output directory
    output_dir = research_output_path / URLS_FROM_GUIDELINES_FOLDER
    output_dir.mkdir(parents=True, exist_ok=True)

    # Scrape URLs concurrently
    completed_results = await scrape_urls_concurrently(other_urls, article_guidelines, concurrency_limit)

    if arxiv_urls:
        logger.info(f"Starting arXiv scraping of {len(arxiv_urls)} paper(s)...")
        chat_model = get_chat_model(settings.scraping_model)
        arxiv_tasks = [
            scrape_arxiv_url(url, article_guidelines, chat_model) for url in arxiv_urls
        ]
        arxiv_results = await asyncio.gather(*arxiv_tasks, return_exceptions=True)
        completed_results.extend(arxiv_results)
        arxiv_success = sum(1 for r in arxiv_results if not isinstance(r, BaseException) and r.get("success", False))
        logger.info(f"Processed {arxiv_success}/{len(arxiv_urls)} arXiv papers with arxiv2markdown.")

    # Write all results (other URLs + arxiv) in a single pass so filenames are
    # deduplicated correctly and files are not written twice.
    saved_files, successful_scrapes = write_scraped_results_to_files(completed_results, output_dir)

    total_attempted = len(other_urls) + len(arxiv_urls)
    return {
        "status": "success" if successful_scrapes > 0 else "warning",
        "urls_processed": successful_scrapes,
        "urls_total": total_attempted,
        "files_saved": len(saved_files),
        "output_directory": str(output_dir.resolve()),
        "saved_files": saved_files,
        "message": (
            f"Scraped and cleaned {successful_scrapes}/{total_attempted} URLs from {GUIDELINES_FILENAMES_FILE} "
            f"in '{research_directory}'.\nSaved {len(saved_files)} files to {URLS_FROM_GUIDELINES_FOLDER} folder: "
            f"{', '.join(saved_files)}"
        ),
    }
