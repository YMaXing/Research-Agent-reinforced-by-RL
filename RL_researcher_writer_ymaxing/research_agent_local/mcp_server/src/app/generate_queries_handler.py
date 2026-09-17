"""LLM operations and query generation utilities."""

import logging
import re
from typing import List, Tuple, Literal
from pathlib import Path

from ..config.prompts import (
    PROMPT_GENERATE_QUERIES_AND_REASONS,
    PROMPT_GENERATE_COMPLEMENTARY_QUERIES_AND_REASONS,
    PROMPT_SHORTEN_QUERY,
)
from ..config.settings import settings
from ..models.query_models import GeneratedQueries, _MAX_QUERY_CHARS
from ..utils.llm_utils import get_chat_model

logger = logging.getLogger(__name__)


async def _shorten_query_if_needed(question: str) -> str:
    """Iteratively ask the LLM to paraphrase *question* until it fits within
    _MAX_QUERY_CHARS.  Falls back to a hard word-boundary cut if the model
    still does not comply after three attempts."""
    if len(question) <= _MAX_QUERY_CHARS:
        return question

    shorten_llm = get_chat_model(settings.query_generation_model)
    current = question
    max_attempts = 3
    attempt = 0
    while len(current) > _MAX_QUERY_CHARS and attempt < max_attempts:
        attempt += 1
        prompt = PROMPT_SHORTEN_QUERY.format(query=current, max_chars=_MAX_QUERY_CHARS)
        result = await shorten_llm.ainvoke(prompt)
        current = getattr(result, "content", str(result)).strip().strip('"').strip("'")
        logger.info(
            f"Shorten attempt {attempt}/{max_attempts}: {len(current)} chars → {current!r}"
        )

    if len(current) > _MAX_QUERY_CHARS:
        # Hard fallback: cut at the last word boundary before the limit.
        # Reserve 1 char for the trailing '?' so the result never exceeds _MAX_QUERY_CHARS.
        cut = current[:_MAX_QUERY_CHARS - 1]
        last_space = cut.rfind(" ")
        current = (cut[:last_space] if last_space > 0 else cut).rstrip(".,;:") + "?"
        logger.warning(f"Query still too long after {max_attempts} shorten attempts; hard-cut to: {current!r}")

    return current

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
    logger.info("Generating candidate queries")

    max_llm_retries = 3
    for attempt in range(max_llm_retries):
        try:
            response = await chat_llm.ainvoke(prompt)

            if not isinstance(response, GeneratedQueries):
                msg = f"LLM returned unexpected type: {type(response)} (attempt {attempt + 1}/{max_llm_retries})"
                logger.warning(msg)
                if attempt < max_llm_retries - 1:
                    continue
                raise RuntimeError(f"LLM returned unexpected type: {type(response)} after {max_llm_retries} attempts")

            # Shorten any overlong questions before returning.
            for item in response.queries:
                item.question = await _shorten_query_if_needed(item.question)

            queries_and_reasons = [(item.question, item.reason) for item in response.queries]

            if len(queries_and_reasons) < n_queries:
                msg = f"LLM returned only {len(queries_and_reasons)} queries, expected {n_queries} (attempt {attempt + 1}/{max_llm_retries})"
                logger.warning(msg)
                if attempt < max_llm_retries - 1:
                    continue
                raise RuntimeError(msg)

            return queries_and_reasons[:n_queries]

        except RuntimeError:
            raise
        except Exception as exc:
            logger.error(f"⚠️ LLM call failed ({exc}).", exc_info=True)
            raise

    raise RuntimeError(f"generate_queries_with_reasons failed after {max_llm_retries} attempts")

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
    logger.info(f"Generating complementary queries (Depth {depth_pct}% / Breadth {breadth_pct}%)")

    max_llm_retries = 3
    for attempt in range(max_llm_retries):
        try:
            response = await chat_llm.ainvoke(prompt)

            if not isinstance(response, GeneratedQueries):
                msg = f"LLM returned unexpected type: {type(response)} (attempt {attempt + 1}/{max_llm_retries})"
                logger.warning(msg)
                if attempt < max_llm_retries - 1:
                    continue
                raise RuntimeError(f"LLM returned unexpected type: {type(response)} after {max_llm_retries} attempts")

            # Shorten any overlong questions before returning.
            for item in response.queries:
                item.question = await _shorten_query_if_needed(item.question)

            queries_and_reasons = [(item.question, item.reason) for item in response.queries]

            if len(queries_and_reasons) < n_queries:
                msg = f"LLM returned only {len(queries_and_reasons)} queries, expected {n_queries} (attempt {attempt + 1}/{max_llm_retries})"
                logger.warning(msg)
                if attempt < max_llm_retries - 1:
                    continue
                raise RuntimeError(msg)

            return queries_and_reasons[:n_queries]

        except RuntimeError:
            raise
        except Exception as exc:
            logger.error(f"⚠️ LLM call failed ({exc}).", exc_info=True)
            raise

    raise RuntimeError(f"generate_complementary_queries_with_reasons failed after {max_llm_retries} attempts")