"""LLM operations and query generation utilities."""

import logging
import re
from typing import List, Tuple, Literal
from pathlib import Path

from ..config.prompts import PROMPT_GENERATE_QUERIES_AND_REASONS, PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS
from ..config.settings import settings
from ..models.query_models import GeneratedQueries
from ..utils.llm_utils import get_chat_model

logger = logging.getLogger(__name__)

def append_generated_queries_with_reasons(
        full_queries_path: Path,
        queries_and_reasons: List[Tuple[str, str]],
        starting_id: int,
        query_source: Literal["exploitation", "complementary"] = "exploitation",
    ) -> int:
        """
        Append a list of queries with reasons to full_queries.md.
        Automatically tags each query with [Exploitation] or [Exploration].
        Returns next available global id.
        """
        tag = "[Exploitation]" if query_source == "exploitation" else "[Exploration]"
        with full_queries_path.open("a", encoding="utf-8") as f:
            last_id = starting_id
            for query, reason in queries_and_reasons:
                f.write(f"Query [{last_id}] {tag}: {query}\n\n")
                f.write(f"Reason: {reason}\n\n")
                f.write("-----\n\n")
                last_id += 1
        return last_id

def compute_next_query_id(results_path: Path) -> int:
    """Compute the next query ID by finding the highest existing ID.
    Updated to support the new tagged format: "Query [42] [Exploitation]:" or "[Exploration]:"."""
    if not results_path.exists():
        return 1
    
    # Matches: Query [42]:   OR   Query [43] [Exploitation]:   OR   Query [44] [Exploration]:
    pattern = re.compile(r"Query \[(\d+)\](?:\s+\[(?:Exploitation|Exploration)\])?:")

    max_id = 0
    for line in results_path.read_text(encoding="utf-8").splitlines():
        match = pattern.search(line)   # Changed from .match() to .search() for robustness
        if match:
            max_id = max(max_id, int(match.group(1)))
    return max_id + 1

async def generate_queries_with_reasons(
    article_guidelines: str,
    past_research: str,
    full_queries: str,
    scraped_ctx: str,
    n_queries: int = 5,
) -> List[Tuple[str, str]]:
    """Return a list of tuples (query, reason)."""

    prompt = PROMPT_GENERATE_QUERIES_AND_REASONS.format(
        n_queries=n_queries,
        article_guidelines=article_guidelines or "<none>",
        past_research=past_research or "<none>",
        full_queries=full_queries or "<none>",
        scraped_ctx=scraped_ctx or "<none>",
    )

    chat_llm = get_chat_model(settings.query_generation_model, GeneratedQueries)
    logger.debug("Generating candidate queries")

    try:
        response = await chat_llm.ainvoke(prompt)

        if not isinstance(response, GeneratedQueries):
            msg = f"LLM returned unexpected type: {type(response)}"
            logger.error(msg)
            raise RuntimeError(msg)

        queries_and_reasons = [(item.question, item.reason) for item in response.queries]

        if len(queries_and_reasons) < n_queries:
            msg = f"LLM returned only {len(queries_and_reasons)} queries, expected {n_queries}."
            logger.error(msg)
            raise RuntimeError(msg)

        return queries_and_reasons[:n_queries]

    except Exception as exc:
        logger.error(f"⚠️ LLM call failed ({exc}).", exc_info=True)
        raise

async def generate_complementary_queries_with_reasons(
    article_guidelines: str,
    past_research: str,
    full_queries: str,
    scraped_ctx: str,
    n_queries: int = 5,
    depth_vs_breadth_ratio: float = 0.5,
) -> List[Tuple[str, str]]:
    """Return a list of tuples (query, reason)."""

    # Convert ratio to clean percentages for the prompt
    depth_pct = round(depth_vs_breadth_ratio * 100)
    breadth_pct = 100 - depth_pct

    prompt = PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS.format(
        n_queries=n_queries,
        article_guidelines=article_guidelines or "<none>",
        past_research=past_research or "<none>",
        full_queries=full_queries or "<none>",
        scraped_ctx=scraped_ctx or "<none>",
        depth_percentage=depth_pct,
        breadth_percentage=breadth_pct,
    )

    chat_llm = get_chat_model(settings.query_generation_model, GeneratedQueries)
    logger.debug(f"Generating complementary queries (Depth {depth_pct}% / Breadth {breadth_pct}%)")

    try:
        response = await chat_llm.ainvoke(prompt)

        if not isinstance(response, GeneratedQueries):
            msg = f"LLM returned unexpected type: {type(response)}"
            logger.error(msg)
            raise RuntimeError(msg)

        queries_and_reasons = [(item.question, item.reason) for item in response.queries]

        if len(queries_and_reasons) < n_queries:
            msg = f"LLM returned only {len(queries_and_reasons)} queries, expected {n_queries}."
            logger.error(msg)
            raise RuntimeError(msg)

        return queries_and_reasons[:n_queries]

    except Exception as exc:
        logger.error(f"⚠️ LLM call failed ({exc}).", exc_info=True)
        raise