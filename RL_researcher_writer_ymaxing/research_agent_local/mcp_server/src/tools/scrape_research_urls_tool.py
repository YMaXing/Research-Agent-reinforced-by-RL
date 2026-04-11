"""Scrape research URLs tool implementation."""

import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict
from urllib.parse import urlparse

from ..app.github_handler import process_github_url
from ..app.scraping_handler import build_filename, scrape_urls_concurrently, scrape_arxiv_url
from ..app.youtube_handler import get_video_id, process_youtube_url
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URL_PHASES_FILE,
    URLS_FROM_RESEARCH_FOLDER,
    URLS_TO_SCRAPE_FROM_RESEARCH_FILE,
    YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS,
)
from ..utils.file_utils import read_file_safe, validate_research_folder
from ..utils.llm_utils import get_chat_model
from ..config.settings import settings

logger = logging.getLogger(__name__)


def validate_and_read_urls_file(
    urls_file_path: Path, research_directory: str
) -> tuple[list[str], Dict[str, Any] | None]:
    """
    Validate and read URLs from the research URLs file.

    Checks if the URLs file exists, reads its content, and parses the URLs.
    Returns either the list of URLs or an early return dict for error cases.

    Args:
        urls_file_path: Path to the URLs file
        research_directory: Research directory path for error messages

    Returns:
        Tuple of (urls_list, early_return_dict). If early_return_dict is not None,
        the caller should return it immediately. Otherwise, use the urls_list.
    """
    if not urls_file_path.exists():
        early_return = {
            "status": "success",
            "message": f"No URLs to scrape, file not found: {urls_file_path}",
            "urls_processed": 0,
            "urls_total": 0,
        }
        return [], early_return

    # Read the URLs file (one URL per line)
    try:
        urls_content = read_file_safe(urls_file_path)
        if not urls_content:
            early_return = {
                "status": "success",
                "message": f"No URLs found in {URLS_TO_SCRAPE_FROM_RESEARCH_FILE} in '{research_directory}'",
                "urls_processed": 0,
                "urls_total": 0,
            }
            return [], early_return

        # Split by lines and filter out empty lines
        urls = [url.strip() for url in urls_content.split("\n") if url.strip()]

        if not urls:
            early_return = {
                "status": "success",
                "message": f"No valid URLs found in {URLS_TO_SCRAPE_FROM_RESEARCH_FILE} in '{research_directory}'",
                "urls_processed": 0,
                "urls_total": 0,
            }
            return [], early_return

    except (IOError, OSError) as e:
        msg = f"Error reading {URLS_TO_SCRAPE_FROM_RESEARCH_FILE}: {str(e)}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    return urls, None


def deduplicate_urls(research_output_path: Path, urls: list[str]) -> tuple[list[str], int, int]:
    """
    Deduplicate URLs by checking against previously processed URLs from guidelines file.

    Reads the guidelines filenames JSON file to get already processed URLs and filters
    them out from the input URLs list.

    Args:
        research_output_path: Path to the research output directory
        urls: List of URLs to deduplicate

    Returns:
        Tuple of (filtered_urls, original_count, deduplicated_count)
    """
    # Read previously processed URLs from GUIDELINES_FILENAMES_FILE to deduplicate
    guidelines_json_path = research_output_path / GUIDELINES_FILENAMES_FILE
    already_processed_urls = set()

    if guidelines_json_path.exists():
        try:
            with open(guidelines_json_path, "r", encoding="utf-8") as f:
                guidelines_data = json.load(f)

            # Collect URLs from steps 2.2 and 2.3 (other_urls and github_urls)
            other_urls_guidelines = guidelines_data.get("other_urls", [])
            github_urls_guidelines = guidelines_data.get("github_urls", [])
            already_processed_urls.update(other_urls_guidelines)
            already_processed_urls.update(github_urls_guidelines)

        except (IOError, OSError, json.JSONDecodeError) as e:
            msg = f"⚠️ Warning: Could not read {GUIDELINES_FILENAMES_FILE} for deduplication: {e}"
            logger.warning(msg, exc_info=True)

    # Filter out URLs that were already processed
    original_count = len(urls)
    urls_to_process = [url for url in urls if url not in already_processed_urls]
    deduplicated_count = original_count - len(urls_to_process)

    return urls_to_process, original_count, deduplicated_count


def is_arxiv_url(url: str) -> bool:
    """Return True if URL is an arXiv link (abs or pdf)."""
    return "arxiv.org" in url and ("/abs/" in url or "/pdf/" in url)


def is_github_url(url: str) -> bool:
    """Return True if URL is a GitHub link."""
    return "github.com" in url


def categorize_urls(urls: list[str]) -> tuple[list[str], list[str], list[str], list[str]]:
    """
    Categorize URLs into YouTube, arXiv, GitHub, and other URLs.

    Separates the input URLs into four categories:
    - YouTube URLs (containing youtube.com or youtu.be)
    - arXiv URLs (containing arxiv.org with /abs/ or /pdf/)
    - GitHub URLs (containing github.com)
    - Other URLs (all remaining URLs)

    Args:
        urls: List of URLs to categorize

    Returns:
        Tuple of (youtube_urls, arxiv_urls, github_urls, other_urls)
    """
    youtube_urls = [url for url in urls if "youtube.com" in url or "youtu.be" in url]
    arxiv_urls = [url for url in urls if is_arxiv_url(url)]
    github_urls = [url for url in urls if is_github_url(url)]
    other_urls = [
            url for url in urls
            if url not in youtube_urls and url not in arxiv_urls and url not in github_urls
        ]
    return youtube_urls, arxiv_urls, github_urls, other_urls


def write_scraped_results_to_files(
    completed_results: list[dict],
    output_dir: Path,
    url_to_phase: dict[str, str] | None = None,
) -> tuple[list[str], int]:
    """
    Write scraped results to markdown files and return statistics.

    Args:
        completed_results: List of scraping results from scrape_urls_concurrently
        output_dir: Directory to write the markdown files to
        url_to_phase: Optional mapping of URL → phase label for tagging

    Returns:
        Tuple of (saved_files_list, successful_scrapes_count)
    """
    saved_files = []
    successful_scrapes = 0
    existing_names: set[str] = set()

    for res in completed_results:
        cleaned_markdown = res.get("markdown", "")
        title = res.get("title", "")
        url = res.get("url", "")

        if res.get("success", False):
            successful_scrapes += 1

        url_header = f"**Source URL:** <{url}>\n\n" if url else ""
        if url_to_phase:
            phase = url_to_phase.get(url, "[EXPLOITATION]")
            cleaned_markdown = f"Phase: {phase}\n\n{url_header}" + (cleaned_markdown or "")
        else:
            cleaned_markdown = url_header + (cleaned_markdown or "")

        filename = build_filename(title, url, existing_names)
        output_path = output_dir / filename
        output_path.write_text(cleaned_markdown or "", encoding="utf-8")
        saved_files.append(filename)

    return saved_files, successful_scrapes


async def process_and_save_urls(
    other_urls: list[str],
    arxiv_urls: list[str],
    github_urls: list[str],
    youtube_urls: list[str],
    article_guidelines: str,
    output_dir: Path,
    concurrency_limit: int,
    url_to_phase: dict[str, str] | None = None,
) -> tuple[list[str], int, list[str]]:
    """
    Process and save other URLs, arXiv, GitHub, and YouTube URLs.

    Args:
        other_urls: List of non-special URLs to scrape
        arxiv_urls: List of arXiv URLs to scrape
        github_urls: List of GitHub URLs to process with gitingest
        youtube_urls: List of YouTube URLs to transcribe
        article_guidelines: Guidelines content for cleaning scraped data
        output_dir: Directory to save the processed files
        concurrency_limit: Maximum number of concurrent tasks
        url_to_phase: Optional mapping of URL → phase label for tagging saved files

    Returns:
        Tuple of (saved_files_list, successful_scrapes_count, report_parts_list)
    """
    saved_files = []
    successful_scrapes = 0
    report_parts = []

    # Process OTHER URLs
    if other_urls:
        logger.debug(
            f"Starting scraping of {len(other_urls)} web pages with a concurrency limit of {concurrency_limit}..."
        )

        # Scrape URLs concurrently
        completed_results = await scrape_urls_concurrently(other_urls, article_guidelines, concurrency_limit)

        # Write outputs
        saved_files_batch, successful = write_scraped_results_to_files(completed_results, output_dir, url_to_phase)
        saved_files.extend(saved_files_batch)
        successful_scrapes += successful
        report_parts.append(f"Scraped {successful}/{len(other_urls)} web pages.")

    # Process arXiv URLs
    if arxiv_urls:
        logger.debug(f"Starting arXiv scraping of {len(arxiv_urls)} paper(s)...")
        chat_model = get_chat_model(settings.scraping_model)
        arxiv_tasks = [
            scrape_arxiv_url(url, article_guidelines, chat_model) for url in arxiv_urls
        ]
        arxiv_results = await asyncio.gather(*arxiv_tasks, return_exceptions=True)

        arxiv_saved, arxiv_success = write_scraped_results_to_files(arxiv_results, output_dir, url_to_phase)
        saved_files.extend(arxiv_saved)
        successful_scrapes += arxiv_success
        report_parts.append(f"Processed {arxiv_success}/{len(arxiv_urls)} arXiv papers with arxiv2markdown.")

    # Process GITHUB URLs
    if github_urls:
        logger.debug(f"Starting gitingest processing of {len(github_urls)} GitHub repo(s)...")
        github_success = 0
        for url in github_urls:
            try:
                result = await process_github_url(url, output_dir, settings.github_token.get_secret_value())
                if result:
                    github_success += 1
                # Determine the filename that process_github_url wrote
                parsed = urlparse(url)
                parts = [p for p in parsed.path.strip("/").split("/") if p]
                if len(parts) >= 2:
                    dest_name = f"{parts[0]}_{parts[1]}.md"
                else:
                    dest_name = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".md"
                saved_files.append(dest_name)
                # Prepend phase header
                if url_to_phase:
                    gh_file = output_dir / dest_name
                    if gh_file.exists():
                        phase = url_to_phase.get(url, "[EXPLOITATION]")
                        existing = gh_file.read_text(encoding="utf-8")
                        gh_file.write_text(f"Phase: {phase}\n\n" + existing, encoding="utf-8")
            except Exception as e:
                logger.error(f"Error processing GitHub URL {url}: {e}", exc_info=True)
        report_parts.append(f"Processed {github_success}/{len(github_urls)} GitHub repositories with gitingest.")

    # Process YOUTUBE URLs
    if youtube_urls:
        logger.debug(f"Starting transcription of {len(youtube_urls)} YouTube video(s)...")
        try:
            yt_semaphore = asyncio.Semaphore(YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS)

            yt_tasks = [process_youtube_url(url, output_dir, yt_semaphore) for url in youtube_urls]
            await asyncio.gather(*yt_tasks)

            # Prepend phase header to each YouTube transcription file
            if url_to_phase:
                for url in youtube_urls:
                    video_id = get_video_id(url)
                    if not video_id:
                        sanitized = url.replace("https://", "").replace("http://", "").replace("/", "_")
                        video_id = sanitized
                    yt_file = output_dir / f"{video_id}.md"
                    if yt_file.exists():
                        phase = url_to_phase.get(url, "[EXPLOITATION]")
                        existing = yt_file.read_text(encoding="utf-8")
                        yt_file.write_text(f"Phase: {phase}\n\n" + existing, encoding="utf-8")

            report_parts.append(f"Transcribed {len(youtube_urls)} YouTube videos.")
        except Exception as e:
            logger.error(f"Failed to initialize or run YouTube transcription: {e}", exc_info=True)
            report_parts.append(f"Failed to transcribe {len(youtube_urls)} YouTube videos.")

    return saved_files, successful_scrapes, report_parts


async def scrape_research_urls_tool(research_directory: str, concurrency_limit: int = 4) -> Dict[str, Any]:
    """
    Scrape the selected research URLs for full content.

    Reads the URLs from urls_to_scrape_from_research.md and scrapes/cleans each URL's
    full content. The cleaned markdown files are saved to the urls_from_research
    subfolder with appropriate filenames. Deduplicates URLs that were already processed.

    Args:
        research_directory: Path to the research directory containing urls_to_scrape_from_research.md
        concurrency_limit: Maximum number of concurrent tasks for scraping (default: 4)

    Returns:
        Dict with status, processing results, and file paths
    """
    logger.debug(f"Scraping research URLs from directory: {research_directory}")

    # Convert to Path object
    research_path = Path(research_directory)
    research_output_path = research_path / RESEARCH_OUTPUT_FOLDER

    # Validate folders and files
    validate_research_folder(research_path)

    # Create RESEARCH_OUTPUT_FOLDER directory if it doesn't exist
    research_output_path.mkdir(parents=True, exist_ok=True)

    # Look for urls_to_scrape_from_research.md file
    urls_file_path = research_output_path / URLS_TO_SCRAPE_FROM_RESEARCH_FILE

    # Validate and read URLs from file
    urls, early_return = validate_and_read_urls_file(urls_file_path, research_directory)
    if early_return is not None:
        return early_return

    # Deduplicate URLs against previously processed ones
    urls_to_process, original_count, deduplicated_count = deduplicate_urls(research_output_path, urls)

    # Categorize URLs into YouTube, arXiv, GitHub, and other types
    youtube_urls, arxiv_urls, github_urls, other_urls = categorize_urls(urls_to_process)

    if not youtube_urls and not arxiv_urls and not github_urls and not other_urls:
        return {
            "status": "success",
            "message": f"All {original_count} URLs were already processed. No new URLs to scrape.",
            "urls_processed": 0,
            "urls_total": original_count,
            "deduplicated_count": deduplicated_count,
        }

    # Look for ARTICLE_GUIDELINE_FILE file to get the guidelines content
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    article_guidelines = ""
    if guidelines_path.exists():
        try:
            article_guidelines = read_file_safe(guidelines_path)
        except Exception as e:
            msg = f"Error reading {ARTICLE_GUIDELINE_FILE}: {str(e)}"
            logger.error(msg, exc_info=True)
            raise ValueError(msg) from e
    else:
        logger.warning(f"{ARTICLE_GUIDELINE_FILE} not found in research folder: {research_directory}")

    # Prepare output directory
    output_dir = research_output_path / URLS_FROM_RESEARCH_FOLDER
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load phase mapping written by select_research_sources_to_scrape (best-effort)
    url_phases_path = research_output_path / URL_PHASES_FILE
    url_to_phase: dict[str, str] = {}
    if url_phases_path.exists():
        try:
            with url_phases_path.open("r", encoding="utf-8") as _f:
                url_to_phase = json.load(_f)
        except (json.JSONDecodeError, OSError) as _e:
            logger.warning(f"Could not read {URL_PHASES_FILE}: {_e}. Phase tagging will be skipped.")

    # Process and save URLs
    saved_files, successful_scrapes, report_parts = await process_and_save_urls(
        other_urls, arxiv_urls, github_urls, youtube_urls, article_guidelines, output_dir, concurrency_limit,
        url_to_phase=url_to_phase or None,
    )

    # Final Report
    total_urls_processed = len(youtube_urls) + len(other_urls) + len(github_urls) + len(arxiv_urls)
    base_message = (
        f"Processed {total_urls_processed} new URLs "
        f"from {URLS_TO_SCRAPE_FROM_RESEARCH_FILE} in '{research_directory}'."
    )

    return {
        "status": "success" if len(report_parts) > 0 else "warning",
        "urls_processed": successful_scrapes,
        "urls_total": total_urls_processed,
        "original_urls_count": original_count,
        "deduplicated_count": deduplicated_count,
        "files_saved": len(saved_files),
        "output_directory": str(output_dir.resolve()),
        "saved_files": saved_files,
        "message": f"{base_message} {' '.join(report_parts)}",
    }
