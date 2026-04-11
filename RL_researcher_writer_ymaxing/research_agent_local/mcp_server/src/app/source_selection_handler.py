"""Source selection operations and utilities."""

import logging
import re
from pathlib import Path
from typing import Any, Dict, List

from ..config.constants import (
    RESEARCH_OUTPUT_FOLDER,
    TAVILY_RESULTS_FILE,
    URLS_FROM_GUIDELINES_FOLDER,
)
from ..config.prompts import (
    PROMPT_AUTO_SOURCE_SELECTION_EXPLOITATION,
    PROMPT_AUTO_SOURCE_SELECTION_EXPLORATION,
    PROMPT_SELECT_TOP_SOURCES,
)
from ..config.settings import settings
from ..models.query_models import SourceSelection, TopSourceSelection
from ..utils.llm_utils import get_chat_model

logger = logging.getLogger(__name__)


def parse_tavily_results(md_text: str) -> Dict[int, Dict[str, str]]:
    """Return mapping {id: {url, query, phase, answer}} extracted from the markdown.

    The Phase field is optional for backward compatibility with files written before
    phase tagging was introduced; it defaults to "[EXPLOITATION]" when absent.
    """
    # Handles both formats:
    #   New: Phase: [EXPLOITATION]\n\n### Source [N]: URL\n\nQuery: ...\n\nAnswer: ...
    #   Old: ### Source [N]: URL\n\nQuery: ...\n\nPhase: ...\n\nAnswer: ...
    _source_block_re = re.compile(
        r"^(?:Phase: (.*?)\n\n)?### Source \[(\d+)]\: (.*?)\n\nQuery: (.*?)\n\n(?:Phase: (.*?)\n\n)?Answer: (.*?)\n(?:-----|\Z)",
        re.S | re.M,
    )

    results: Dict[int, Dict[str, str]] = {}
    for match in _source_block_re.finditer(md_text):
        phase = (match.group(1) or match.group(5) or "[EXPLOITATION]").strip()
        src_id = int(match.group(2))
        url = match.group(3).strip()
        query = match.group(4).strip()
        answer = match.group(6).strip()
        results[src_id] = {"url": url, "query": query, "phase": phase, "answer": answer}
    return results


def build_sources_data_text(parsed: Dict[int, Dict[str, str]]) -> str:
    """Format sources into the string expected by the prompt."""
    lines: List[str] = []
    for src_id in sorted(parsed):
        entry = parsed[src_id]
        lines.append(f"**Phase:** {entry.get('phase', '[EXPLOITATION]')}")
        lines.append("")
        lines.append(f"### Source ID {src_id}: {entry['url']}")
        lines.append("")
        lines.append(f"**Query:** {entry['query']}")
        lines.append(f"**Answer:** {entry['answer']}")
        lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


async def _select_sources_for_phase(
    article_guidelines: str,
    parsed_phase: Dict[int, Dict[str, str]],
    prompt_template: str,
    phase_label: str,
) -> List[int]:
    """Run source selection for a single phase subset."""
    if not parsed_phase:
        logger.debug(f"No {phase_label} sources to evaluate.")
        return []

    sources_data_text = build_sources_data_text(parsed_phase)

    prompt_text = prompt_template.format(
        article_guidelines=article_guidelines or "<none>",
        sources_data=sources_data_text,
    )

    chat_llm = get_chat_model(settings.source_selection_model, SourceSelection)
    logger.debug(f"Selecting {phase_label} sources to keep ({len(parsed_phase)} candidates)")

    try:
        response = await chat_llm.ainvoke(prompt_text)
    except Exception as exc:
        logger.error(
            f"⚠️ LLM call failed for {phase_label} ({exc}). Falling back to accepting all.",
            exc_info=True,
        )
        return sorted(parsed_phase.keys())

    if not isinstance(response, SourceSelection):
        logger.error(f"⚠️ LLM returned unexpected type for {phase_label}: {type(response)}")
        return sorted(parsed_phase.keys())

    if response.selection_type == "none":
        logger.debug(f"No {phase_label} sources accepted.")
        return []
    if response.selection_type == "all":
        logger.info(f"👍 All {phase_label} sources accepted ({len(parsed_phase)}).")
        return sorted(parsed_phase.keys())
    # 'specific'
    accepted = [sid for sid in response.source_ids if sid in parsed_phase]
    logger.info(f"👍 {len(accepted)}/{len(parsed_phase)} {phase_label} sources accepted.")
    return accepted


async def select_sources(article_guidelines: str, md_results: str) -> List[int]:
    """Use an LLM to select the best subset of sources.

    Splits sources by phase (exploitation vs exploration) and evaluates each
    phase independently with a phase-appropriate prompt and acceptance threshold.
    """
    parsed_results = parse_tavily_results(md_results)
    if not parsed_results:
        logger.warning(f"⚠️  No sources found in {TAVILY_RESULTS_FILE} - accepting none.")
        return []

    # Split by phase
    exploitation: Dict[int, Dict[str, str]] = {}
    exploration: Dict[int, Dict[str, str]] = {}
    for src_id, entry in parsed_results.items():
        if entry.get("phase", "[EXPLOITATION]") == "[EXPLORATION]":
            exploration[src_id] = entry
        else:
            exploitation[src_id] = entry

    logger.info(
        f"Source selection: {len(exploitation)} exploitation, {len(exploration)} exploration "
        f"({len(parsed_results)} total)"
    )

    # Evaluate each phase independently
    exploitation_ids = await _select_sources_for_phase(
        article_guidelines,
        exploitation,
        PROMPT_AUTO_SOURCE_SELECTION_EXPLOITATION,
        "exploitation",
    )
    if exploration:
        exploration_ids = await _select_sources_for_phase(
            article_guidelines,
            exploration,
            PROMPT_AUTO_SOURCE_SELECTION_EXPLORATION,
            "exploration",
        )
    else:
        logger.debug("No exploration sources present; skipping exploration selection call.")
        exploration_ids = []

    # Merge and sort
    all_selected = sorted(set(exploitation_ids + exploration_ids))
    logger.info(
        f"✅ Total selected: {len(all_selected)} "
        f"(exploitation: {len(exploitation_ids)}, exploration: {len(exploration_ids)})"
    )
    return all_selected


def parse_results_selected(md_text: str) -> List[Dict[str, str]]:
    """Return list of dicts with keys url, query, phase, answer from selected results file.

    The Phase field is optional for backward compatibility with pre-tagging files.
    """
    # Handles both formats:
    #   New: Phase: [EXPLOITATION]\n\n### Source [N]: URL\n\nQuery: ...\n\nAnswer: ...
    #   Old: ### Source [N]: URL\n\nQuery: ...\n\nPhase: ...\n\nAnswer: ...
    _source_block_re = re.compile(
        r"^(?:Phase: (.*?)\n\n)?### Source \[(\d+)]\: (.*?)\n\nQuery: (.*?)\n\n(?:Phase: (.*?)\n\n)?Answer: (.*?)\n(?:-----|\Z)",
        re.S | re.M,
    )

    sources: List[Dict[str, str]] = []
    for match in _source_block_re.finditer(md_text):
        phase = (match.group(1) or match.group(5) or "[EXPLOITATION]").strip()
        url = match.group(3).strip()
        query = match.group(4).strip()
        answer = match.group(6).strip()
        sources.append({"url": url, "query": query, "phase": phase, "answer": answer})
    return sources


def load_scraped_guideline_context(research_directory: str) -> str:
    """Concatenate all markdown files from URLS_FROM_GUIDELINES_FOLDER as context."""
    ctx_parts: List[str] = []
    dir_path = Path(research_directory) / RESEARCH_OUTPUT_FOLDER / URLS_FROM_GUIDELINES_FOLDER
    if dir_path.exists():
        for md_file in sorted(dir_path.glob("*.md")):
            ctx_parts.append(md_file.read_text(encoding="utf-8"))
    return "\n\n".join(ctx_parts)


async def select_top_sources(
    article_guidelines: str, guideline_ctx: str, md_results_selected: str, max_sources: int = 5
) -> Dict[str, Any]:
    """Select up to max_sources top sources to scrape fully.

    Returns:
        dict: Contains 'selected_urls' (List[str]), 'url_to_phase' (Dict[str, str]),
              and 'reasoning' (str)
    """
    sources = parse_results_selected(md_results_selected)
    if not sources:
        msg = "⚠️  No sources found in tavily_results_selected.md. Nothing to select."
        logger.warning(msg)
        return {"selected_urls": [], "url_to_phase": {}, "reasoning": "No sources available for selection."}

    # Build URL → phase lookup from parsed sources
    url_to_phase: Dict[str, str] = {s["url"]: s.get("phase", "[EXPLOITATION]") for s in sources}

    # Build sources data text for prompt
    lines: List[str] = []
    for idx, src in enumerate(sources, 1):
        lines.append(f"Phase: {src['phase']}")
        lines.append(f"### Source {idx}: {src['url']}")
        lines.append(f"Query: {src['query']}")
        lines.append(f"Snippet: {src['answer']}")
        lines.append("---")
    sources_text = "\n".join(lines)

    prompt = PROMPT_SELECT_TOP_SOURCES.format(
        article_guidelines=article_guidelines or "<none>",
        scraped_guideline_ctx=guideline_ctx or "<none>",
        accepted_sources_data=sources_text,
        top_n=max_sources,
    )

    chat_llm = get_chat_model(settings.source_selection_model, TopSourceSelection)
    logger.debug("Selecting top sources to scrape")
    try:
        response = await chat_llm.ainvoke(prompt)
    except Exception as exc:
        msg = f"⚠️  LLM selection failed ({exc}). Returning first {max_sources} sources by default."
        logger.warning(msg)
        fallback_urls = [s["url"] for s in sources[:max_sources]]
        return {
            "selected_urls": fallback_urls,
            "url_to_phase": {url: url_to_phase.get(url, "[EXPLOITATION]") for url in fallback_urls},
            "reasoning": f"LLM selection failed, falling back to first {max_sources} sources.",
        }

    if not isinstance(response, TopSourceSelection):
        logger.error(f"⚠️ LLM call returned unexpected type: {type(response)}")
        fallback_urls = [s["url"] for s in sources[:max_sources]]
        return {
            "selected_urls": fallback_urls,
            "url_to_phase": {url: url_to_phase.get(url, "[EXPLOITATION]") for url in fallback_urls},
            "reasoning": f"LLM returned unexpected response type, falling back to first {max_sources} sources.",
        }

    # Ensure max sources limit
    selected = response.selected_urls[:max_sources]
    logger.info(f"👍 {len(selected)} sources selected to scrape.")
    return {
        "selected_urls": selected,
        "url_to_phase": {url: url_to_phase.get(url, "[EXPLOITATION]") for url in selected},
        "reasoning": response.reasoning,
    }
