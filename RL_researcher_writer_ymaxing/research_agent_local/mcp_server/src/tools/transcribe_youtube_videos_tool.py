"""YouTube video transcription tool implementation."""

import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict

from ..app.youtube_handler import get_video_id, process_youtube_url
from ..config.constants import (
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS,
)
from ..utils.file_utils import validate_guidelines_filenames_file, validate_research_folder

logger = logging.getLogger(__name__)


async def transcribe_youtube_videos_tool(research_directory: str) -> Dict[str, Any]:
    """
    Transcribe YouTube video URLs from GUIDELINES_JSON_FILE using an LLM.

    Reads the GUIDELINES_JSON_FILE file and processes each URL listed
    under 'youtube_videos_urls'. Each video is transcribed, and the results are
    saved as markdown files in the URLS_FROM_GUIDELINES_YOUTUBE_FOLDER subfolder.

    Args:
        research_directory: Path to the research directory containing GUIDELINES_JSON_FILE

    Returns:
        Dict with status, processing results, and file paths
    """
    logger.info(f"Starting transcription of YouTube videos from {research_directory}")

    research_path = Path(research_directory)
    research_output_path = research_path / RESEARCH_OUTPUT_FOLDER

    # Validate folders and files
    validate_research_folder(research_path)

    # Look for GUIDELINES_FILENAMES_FILE
    metadata_path = research_output_path / GUIDELINES_FILENAMES_FILE

    # Validate the guidelines filenames file
    validate_guidelines_filenames_file(metadata_path)

    try:
        data = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (IOError, OSError, json.JSONDecodeError) as e:
        msg = f"Error reading {GUIDELINES_FILENAMES_FILE}: {str(e)}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    youtube_urls: list[str] = data.get("youtube_videos_urls", [])
    url_titles: dict[str, str] = data.get("url_titles", {})

    if not youtube_urls:
        return {
            "status": "success",
            "videos_processed": 0,
            "videos_total": 0,
            "message": f"No YouTube URLs found in {GUIDELINES_FILENAMES_FILE} in '{research_directory}'",
        }

    dest_folder = research_output_path / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER
    dest_folder.mkdir(parents=True, exist_ok=True)

    logger.info(f"Processing {len(youtube_urls)} YouTube URL(s)...")

    semaphore = asyncio.Semaphore(YOUTUBE_TRANSCRIPTION_MAX_CONCURRENT_REQUESTS)
    tasks = [process_youtube_url(url, dest_folder, semaphore) for url in youtube_urls]
    await asyncio.gather(*tasks)

    # Post-process: inject guideline title as H1 when the transcription lacks one
    for url in youtube_urls:
        title = url_titles.get(url, "")
        if not title:
            continue
        video_id = get_video_id(url)
        if not video_id:
            video_id = url.replace("https://", "").replace("http://", "").replace("/", "_")
        yt_file = dest_folder / f"{video_id}.md"
        if yt_file.exists():
            content = yt_file.read_text(encoding="utf-8")
            if not any(ln.strip().startswith("# ") for ln in content.splitlines()):
                yt_file.write_text(f"# {title}\n\n{content}", encoding="utf-8")

    return {
        "status": "success",
        "videos_processed": len(youtube_urls),
        "videos_total": len(youtube_urls),
        "output_directory": str(dest_folder.resolve()),
        "message": (
            f"Processed {len(youtube_urls)} YouTube URLs from {GUIDELINES_FILENAMES_FILE} "
            f"in '{research_directory}'. Saved transcriptions to {dest_folder.name} folder."
        ),
    }
