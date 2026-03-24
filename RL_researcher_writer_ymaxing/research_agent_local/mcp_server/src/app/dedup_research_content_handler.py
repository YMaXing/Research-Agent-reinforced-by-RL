from pathlib import Path
import logging

from ..config.prompts import PROMPT_CONTENT_DEDUPLICATION
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE, 
    URLS_FROM_GUIDELINES_FOLDER,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,)

from ..config.settings import settings
from ..utils.file_utils import read_file_safe
from ..utils.llm_utils import get_chat_model
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

async def deduplicate_research_content(research_path:Path, output_path:Path) -> Tuple[str, Dict[str, int], int]:
    """Semantic deduplication of all research content."""

    # Gather content sources
    sources_collected: List[str] = []
    source_counts = {}

    # 1. Golden + guideline sources
    golden_dir = output_path / URLS_FROM_GUIDELINES_FOLDER
    if golden_dir.exists():
        files = list(golden_dir.glob("*.md"))
        source_counts["golden/guideline"] = len(files)
        for f in files:
            content = read_file_safe(f)
            if content:
                sources_collected.append(content)
                logger.debug(f"Added guideline source: {f.name}")
            else:
                logger.warning(f"Empty or failed to read guideline source: {f}")

    # 2. Research URLs
    research_urls = output_path / URLS_FROM_RESEARCH_FOLDER
    if research_urls.exists():
        content = read_file_safe(research_urls)
        if content:
            sources_collected.append(content)
            source_counts["research_urls"] = 1
            logger.debug("Added research URLs results")
        else:
            logger.warning("Research URLs file empty or unreadable")

    # 3. Other folders
    for folder_name, dir_path in [
        ("code summaries", output_path / URLS_FROM_GUIDELINES_CODE_FOLDER),
        ("YouTube transcripts", output_path / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER),
    ]:
        if dir_path.exists():
            files = list(dir_path.glob("*.md"))
            source_counts[folder_name] = len(files)
            for f in files:
                content = read_file_safe(f)
                if content:
                    sources_collected.append(content)
                    logger.debug(f"Added {folder_name} source: {f.name}")
                else:
                    logger.warning(f"Empty or failed to read {folder_name} source: {f}")

    if not sources_collected:
        msg = "No valid content found in any source directories/files"
        logger.error(msg)
        raise ValueError(msg)

    logger.info(f"Collected {len(sources_collected)} content parts from: {source_counts}")

    full_content = "\n\n---\n\n".join(sources_collected)

    # Article guidelines
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    article_guidelines = read_file_safe(guidelines_path) or "<none>"

    # Deduplicate
    prompt = PROMPT_CONTENT_DEDUPLICATION.format(
        article_guidelines=article_guidelines,
        all_content=full_content,
    )

    try:
        chat_llm = get_chat_model(settings.content_dedup_model)
        logger.info("Invoking LLM for content deduplication...")
        response = await chat_llm.ainvoke(prompt)
        deduplicated_md = response.content.strip() if hasattr(response, "content") else str(response).strip()

        if not deduplicated_md:
            raise ValueError("LLM returned empty deduplicated content")
        
    except Exception as e:
        logger.error(f"LLM deduplication failed: {e}", exc_info=True)
        raise RuntimeError(f"Content deduplication LLM call failed: {str(e)}") from e
    
    return deduplicated_md, source_counts, len(sources_collected)