"""Content-level deduplication tool - run right before create_research_file."""

import logging
from pathlib import Path
from typing import Any, Dict

from ..config.constants import (
    DEDUPLICATED_RESEARCH_FILE,
    RESEARCH_OUTPUT_FOLDER,
)

from ..utils.file_utils import validate_research_folder
from ..app.dedup_research_content_handler import deduplicate_research_content

logger = logging.getLogger(__name__)


async def deduplicate_research_content_tool(research_directory: str) -> Dict[str, Any]:
    """
    Deduplicates ALL research sources as a whole.
    Produces a single clean deduplicated_research.md file.

    Args:
        research_directory: Path to the research directory containing all source subfolders and the output directory

    Returns:
        Dict[str, Any]: Dictionary containing:
            - status: Operation status ("success" or "error")
            - deduplicated_path: Absolute path to the generated deduplicated_research.md file
            - source_counts: Dictionary mapping each source category to the number of files collected
            - total_parts_collected: Total number of content parts fed into deduplication
            - message: Human-readable summary of the operation
    """
    research_path = Path(research_directory)
    output_path = research_path / RESEARCH_OUTPUT_FOLDER

    try:
        validate_research_folder(research_path)
        output_path.mkdir(parents=True, exist_ok=True)
        logger.info(f"Starting content deduplication in: {research_path}")
    except Exception as e:
        logger.error(f"Failed to validate/create output directory: {e}", exc_info=True)
        return {"status": "error", "message": f"Directory validation failed: {str(e)}"}

    try:
        deduplicated_md, source_counts, total_parts_collected = await deduplicate_research_content(research_path, output_path)
    except Exception as e:
        logger.error(f"Content deduplication failed: {e}", exc_info=True)
        return {"status": "error", "message": f"Content deduplication failed: {str(e)}"}

    # Save
    dedup_path = output_path / DEDUPLICATED_RESEARCH_FILE
    try:
        dedup_path.write_text(deduplicated_md, encoding="utf-8")
        logger.info(f"Successfully wrote deduplicated content to: {dedup_path}")
    except Exception as e:
        logger.error(f"Failed to write deduplicated file: {e}", exc_info=True)
        return {"status": "error", "message": f"Failed to save deduplicated file: {str(e)}"}

    return {
        "status": "success",
        "deduplicated_path": str(dedup_path.resolve()),
        "source_counts": source_counts,
        "total_parts_collected": total_parts_collected,
        "message": f"✅ Content deduplication complete ({total_parts_collected} parts → cleaned file). Saved to {dedup_path.relative_to(research_path)}",
    }