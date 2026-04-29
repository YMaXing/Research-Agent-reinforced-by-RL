"""Deduplicate new queries among themselves and against full history – designed for 3 fixed exploitation rounds + RL complementary rounds."""

import json
import re
from pathlib import Path
from typing import List, NamedTuple, Tuple, Literal
import logging

from ..config.settings import settings
from ..utils.file_utils import read_file_safe
from ..utils.llm_utils import get_chat_model
from ..config.prompts import PROMPT_DEDUPLICATE_QUERIES

logger = logging.getLogger(__name__)


class DeduplicationResult(NamedTuple):
    """Return value of deduplicate_new_queries_against_history."""

    kept: List[Tuple[str, str]]      # (query, original_reason) pairs that survive dedup
    rejected: List[Tuple[str, str]]  # (query, original_reason) pairs that were dropped
    reasoning: str                   # LLM explanation of the most important decisions


def parse_queries_from_file(file_path: Path) -> List[Tuple[str, str]]:
    """Parse numbered queries markdown file into (query, reason) tuples."""
    content = read_file_safe(file_path)
    if not content:
        return []

    queries: List[Tuple[str, str]] = []
    lines = content.splitlines()
    current_query = None
    current_reason = ""

    for line in lines:
        line = line.strip()
        if re.match(r'^\d+\.\s', line):
            if current_query:
                queries.append((current_query, current_reason.strip()))
            current_query = line.split(". ", 1)[1]
            current_reason = ""
        elif line.startswith("Reason:"):
            current_reason = line[7:].strip()
        elif current_query and line:
            current_reason += " " + line

    if current_query:
        queries.append((current_query, current_reason.strip()))

    return queries

def format_dedup_prompt_inputs(
    new_queries: List[Tuple[str, str]],
    full_queries_history: str,
    query_source: Literal["exploitation", "complementary"],
) -> str:
    """Format the three placeholders for the deduplication prompt."""
    new_list = "\n".join(
        f"{i+1}. {q}\n   Reason: {r}" for i, (q, r) in enumerate(new_queries)
    )

    prompt = PROMPT_DEDUPLICATE_QUERIES.format(
        query_source=query_source,
        full_queries_history=full_queries_history or "<none>",
        new_queries_list=new_list or "<none>",
    )
    return prompt

async def deduplicate_new_queries_against_history(
    new_queries: List[Tuple[str, str]],
    full_queries_path: Path,
    query_source: Literal["exploitation", "complementary"] = "exploitation",
) -> DeduplicationResult:
    """Semantic deduplication of new batch vs entire historical queries."""
    if not new_queries:
        return DeduplicationResult(kept=[], rejected=[], reasoning="")

    # Load history for context
    history = read_file_safe(full_queries_path) or "<none>"

    prompt = format_dedup_prompt_inputs(new_queries, history, query_source)

    chat_llm = get_chat_model(settings.query_generation_model)
    response = await chat_llm.ainvoke(prompt)

    try:
        if hasattr(response, "content"):
            result = json.loads(response.content)
        else:
            result = json.loads(str(response))
        kept_texts = result.get("kept_queries", [])
        reasoning = result.get("reasoning", "")
    except Exception as e:
        logger.warning(f"Deduplication JSON parse failed: {e}. Keeping all new queries.")
        return DeduplicationResult(kept=new_queries, rejected=[], reasoning="")

    kept_set = {t.strip() for t in kept_texts}
    kept = [(q, r) for q, r in new_queries if q.strip() in kept_set]
    rejected = [(q, r) for q, r in new_queries if q.strip() not in kept_set]
    return DeduplicationResult(kept=kept, rejected=rejected, reasoning=reasoning)
