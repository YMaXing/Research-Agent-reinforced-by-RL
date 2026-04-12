"""Guidelines URL extraction tool implementation."""

import json
import logging
from pathlib import Path
from typing import Any, Dict

from ..app.guideline_extractions_handler import extract_local_paths, extract_urls_by_section
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    GUIDELINES_FILENAMES_FILE,
    RESEARCH_OUTPUT_FOLDER,
)
from ..utils.file_utils import validate_guidelines_file, validate_research_folder

logger = logging.getLogger(__name__)


def extract_guidelines_urls_tool(research_folder: str) -> Dict[str, Any]:
    """
    Extract URLs and local file references from the article guidelines in the research folder.

    Reads the ARTICLE_GUIDELINE_FILE file and extracts:
    - GitHub URLs
    - YouTube video URLs
    - Other HTTP/HTTPS URLs
    - Local file references

    Results are saved to GUIDELINES_FILENAMES_FILE in the research folder.

    Args:
        research_folder: Path to the research folder containing ARTICLE_GUIDELINE_FILE

    Returns:
        Dict with status, extraction results, and output file path
    """
    logger.info(f"Extracting URLs from article guidelines in: {research_folder}")

    # Convert to Path object
    research_path = Path(research_folder)
    research_output_path = research_path / RESEARCH_OUTPUT_FOLDER
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE

    # Validate folders and files
    validate_research_folder(research_path)
    validate_guidelines_file(guidelines_path)

    # Create RESEARCH_OUTPUT_FOLDER directory if it doesn't exist
    research_output_path.mkdir(parents=True, exist_ok=True)

    # Read the guidelines file
    try:
        text = guidelines_path.read_text(encoding="utf-8")
    except (IOError, OSError) as e:
        msg = f"Error reading {ARTICLE_GUIDELINE_FILE}: {e}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    # Extract URLs and categorize them by section (golden vs exploitation)
    urls_by_section = extract_urls_by_section(text)
    golden_urls = urls_by_section["golden"]
    exploitation_urls = urls_by_section["exploitation"]

    # --- Golden URLs (from "Golden Sources", "Article Code"/"Lesson Code", or unlabelled sections) ---
    github_source_urls = [u for u in golden_urls if "github.com" in u]
    youtube_source_urls = [u for u in golden_urls if "youtube.com" in u]
    web_source_urls = [u for u in golden_urls if "github.com" not in u and "youtube.com" not in u]

    # --- Exploitation URLs (from "Other Sources" section) ---
    exploitation_github_urls = [u for u in exploitation_urls if "github.com" in u]
    exploitation_youtube_urls = [u for u in exploitation_urls if "youtube.com" in u]
    exploitation_other_urls = [u for u in exploitation_urls if "github.com" not in u and "youtube.com" not in u]

    # Extract local file references
    local_file_paths = extract_local_paths(text)

    # Prepare the data structure - use keys that match what processing tools expect
    data = {
        # Golden sources (processed in step 2.1-2.4 and tagged <golden_source>)
        "github_urls": github_source_urls,
        "youtube_videos_urls": youtube_source_urls,
        "other_urls": web_source_urls,
        "local_file_paths": local_file_paths,
        # Exploitation sources from "Other Sources" section (processed in step 2.5
        # and tagged <research_source type="guideline_exploitation">)
        "exploitation_github_urls": exploitation_github_urls,
        "exploitation_youtube_videos_urls": exploitation_youtube_urls,
        "exploitation_other_urls": exploitation_other_urls,
    }

    # Write to GUIDELINES_FILENAMES_FILE in the research folder
    output_path = research_output_path / GUIDELINES_FILENAMES_FILE

    try:
        output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    except (IOError, OSError, TypeError) as e:
        msg = f"Error writing {GUIDELINES_FILENAMES_FILE}: {e}"
        logger.error(msg, exc_info=True)
        raise ValueError(msg) from e

    return {
        "status": "success",
        "github_sources_count": len(github_source_urls),
        "youtube_sources_count": len(youtube_source_urls),
        "web_sources_count": len(web_source_urls),
        "local_files_count": len(local_file_paths),
        "exploitation_github_sources_count": len(exploitation_github_urls),
        "exploitation_youtube_sources_count": len(exploitation_youtube_urls),
        "exploitation_web_sources_count": len(exploitation_other_urls),
        "output_path": str(output_path.resolve()),
        "message": (
            f"Successfully extracted URLs from article guidelines in '{research_folder}'. "
            f"Golden sources — {len(github_source_urls)} GitHub, {len(youtube_source_urls)} YouTube, "
            f"{len(web_source_urls)} other URLs, {len(local_file_paths)} local files. "
            f"Exploitation sources (Other Sources section) — {len(exploitation_github_urls)} GitHub, "
            f"{len(exploitation_youtube_urls)} YouTube, {len(exploitation_other_urls)} other URLs. "
            f"Results saved to: {output_path.resolve()}"
        ),
    }
