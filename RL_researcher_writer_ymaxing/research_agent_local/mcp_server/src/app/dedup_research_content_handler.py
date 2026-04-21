from pathlib import Path
import logging
from re import L

from ..config.prompts import PROMPT_CONTENT_DEDUPLICATION
from ..config.constants import (
    ARTICLE_GUIDELINE_FILE,
    TAVILY_RESULTS_SELECTED_FILE, 
    TAVILY_RESULTS_FILE,
    URLS_FROM_GUIDELINES_FOLDER,
    URLS_FROM_GUIDELINES_CODE_FOLDER,
    URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER,
    URLS_FROM_GUIDELINES_YOUTUBE_FOLDER,
    URLS_FROM_RESEARCH_FOLDER,
    LOCAL_FILES_FROM_RESEARCH_FOLDER,)

from ..config.settings import settings
from ..utils.file_utils import read_file_safe
from ..utils.llm_utils import get_chat_model
from ..utils.markdown_utils import build_research_results_section
from ..app.tavily_handler import extract_tavily_chunks, group_tavily_by_query
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

async def deduplicate_research_content(research_path:Path, output_path:Path) -> Tuple[str, Dict[str, int], int]:
    """Semantic deduplication of all research content."""

    # Gather content sources
    sources_collected: List[str] = []
    source_counts = {}

    # 1. Guideline URL sources
    golden_dir = output_path / URLS_FROM_GUIDELINES_FOLDER
    if golden_dir.exists():
        files = list(golden_dir.glob("*.md"))
        source_counts["golden/guideline"] = len(files)
        for f in files:
            content = read_file_safe(f)
            if content:
                sources_collected.append(f'<golden_source type="guideline_url" file="{f.name}">\n{content}\n</golden_source>')
                logger.info(f"Added guideline source: {f.name}")
            else:
                logger.warning(f"Empty or failed to read guideline source: {f}")

    # 2. Other folders from guidelines: local files, code summaries, YouTube transcripts
    for folder_name, dir_path in [
        ("local files", output_path / LOCAL_FILES_FROM_RESEARCH_FOLDER),
        ("code summaries", output_path / URLS_FROM_GUIDELINES_CODE_FOLDER),
        ("YouTube transcripts", output_path / URLS_FROM_GUIDELINES_YOUTUBE_FOLDER),
    ]:
        if dir_path.exists():
            files = list(dir_path.glob("*.md"))
            source_counts[folder_name] = len(files)
            xml_type = folder_name.replace(" ", "_")
            for f in files:
                content = read_file_safe(f)
                if content:
                    sources_collected.append(f'<golden_source type="{xml_type}" file="{f.name}">\n{content}\n</golden_source>')
                    logger.info(f"Added {folder_name} source: {f.name}")
                else:
                    logger.warning(f"Empty or failed to read {folder_name} source: {f}")

    # 3. Exploitation sources from guidelines ("Other Sources" section — non-golden)
    exploitation_guideline_dir = output_path / URLS_FROM_GUIDELINES_EXPLOITATION_FOLDER
    if exploitation_guideline_dir.exists():
        files = list(exploitation_guideline_dir.glob("*.md"))
        source_counts["exploitation/guideline"] = len(files)
        for f in files:
            content = read_file_safe(f)
            if content:
                sources_collected.append(
                    f'<research_source type="guideline_exploitation" phase="exploitation" file="{f.name}">\n{content}\n</research_source>'
                )
                logger.info(f"Added exploitation guideline source: {f.name}")
            else:
                logger.warning(f"Empty or failed to read exploitation guideline source: {f}")

    # 4. Research URLs (scraped files in urls_from_research/ directory)
    research_urls_dir = output_path / URLS_FROM_RESEARCH_FOLDER
    if research_urls_dir.exists():
        files = list(research_urls_dir.glob("*.md"))
        source_counts["research_urls"] = len(files)
        for f in files:
            content = read_file_safe(f)
            if content:
                first_line = content.split("\n", 1)[0]
                phase = "exploration" if (first_line.startswith("Phase:") and "[EXPLORATION]" in first_line) else "exploitation"
                sources_collected.append(f'<research_source phase="{phase}" file="{f.name}">\n{content}\n</research_source>')
                logger.info(f"Added research URL source: {f.name} (phase: {phase})")
            else:
                logger.warning(f"Empty or failed to read research URL source: {f}")

    # 4. Tavily results (split by phase)
    selected_results_file = output_path / TAVILY_RESULTS_SELECTED_FILE
    original_results_file = output_path / TAVILY_RESULTS_FILE

    if selected_results_file.exists():
        results_md = read_file_safe(selected_results_file)
        chunks = extract_tavily_chunks(results_md)
    else:
        results_md = read_file_safe(original_results_file)
        chunks = extract_tavily_chunks(results_md)

    exploitation_ids: List[int] = []
    exploration_ids: List[int] = []
    for src_id, chunk in chunks.items():
        first_line = chunk.split("\n", 1)[0] if chunk else ""
        if first_line.startswith("Phase:") and "[EXPLORATION]" in first_line:
            exploration_ids.append(src_id)
        else:
            exploitation_ids.append(src_id)

    for phase_label, ids in [("exploitation", exploitation_ids), ("exploration", exploration_ids)]:
        if ids:
            grouped = group_tavily_by_query(chunks, ids)
            section = build_research_results_section(grouped)
            sources_collected.append(f'<tavily_results phase="{phase_label}">\n{section}\n</tavily_results>')
            logger.info(f"Added {len(ids)} Tavily chunks for deduplication (phase: {phase_label}).")

 

    if not sources_collected:
        msg = "No valid content found in any source directories/files"
        logger.error(msg)
        raise ValueError(msg)

    logger.info(f"Collected {len(sources_collected)} content parts from: {source_counts}")

    full_content = "\n\n".join(sources_collected)

    # Article guidelines
    guidelines_path = research_path / ARTICLE_GUIDELINE_FILE
    article_guidelines = read_file_safe(guidelines_path) or "<none>"

    # Deduplicate
    prompt = (
        PROMPT_CONTENT_DEDUPLICATION
        .replace("{article_guidelines}", article_guidelines)
        .replace("{all_content}", full_content)
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