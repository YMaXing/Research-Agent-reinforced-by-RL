"""
Scaled light-vs-standard-only pairwise grading (majority-vote-by-design).

Companion to rl_pairwise_stddeep_scale.py (which did this for standard_vs_deep).
Follows the free first-look check (analyze_light_boundary.py, zero cost, reused
the original 6-article pilot's single-draw light_vs_standard data): N=92
observations, r=+0.329, 4/92 strong disagreements with a weak 3:1 directional
skew matching the SAME tier-1-too-steep signature found for standard_vs_deep.
n=4 is too small and single-draw to be conclusive -- light_vs_deep showed no
such signal and is NOT targeted here.

Grades ONLY the light_vs_standard comparison, N=3 draws PER SECTION from the
start (majority-vote-by-design). Random A/B slot assigned once per section.

Reuses section-loading/matching logic from rl_pairwise_grading_generator.py.

Writes to: rl_training_data/pairwise/lightstd_scale/<article>/lightstd_judgments.json

Usage (from writing_workflow/):
  uv run python rl_pipeline/rl_pairwise_lightstd_scale.py --articles 02_workflows_vs_agents__var_standard ... --model claude
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import random
from pathlib import Path

from rl_pairwise_grading_generator import (
    _MODEL_CHOICES,
    _load_arm_sections,
    _match_body,
    _normalize,
    _target_words_by_title,
)

from brown.evals.metrics.pairwise_enhancement import grade_pairwise

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_pairwise_lightstd_scale")

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_OUTPUT_DIR = _REPO_ROOT / "rl_training_data" / "pairwise" / "lightstd_scale"


async def _grade_one(semaphore: asyncio.Semaphore, doc_a: str, doc_b: str, guideline_ctx: str, model, n_draws: int) -> list[dict]:
    async def _one_call() -> dict:
        async with semaphore:
            resp = await grade_pairwise(doc_a=doc_a, doc_b=doc_b, section_guideline=guideline_ctx, model=model)
        return {
            "depth": {
                "preference": resp.depth.preference,
                "a_instances": resp.depth.a_instances,
                "b_instances": resp.depth.b_instances,
            },
            "breadth": {
                "preference": resp.breadth.preference,
                "a_instances": resp.breadth.a_instances,
                "b_instances": resp.breadth.b_instances,
            },
            "reasoning": resp.reasoning,
        }

    tasks = [_one_call() for _ in range(n_draws)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return [{"error": str(r)} if isinstance(r, BaseException) else r for r in results]


async def grade_article(article: str, model, n_draws: int, semaphore: asyncio.Semaphore) -> dict:
    arm_sections = _load_arm_sections(article)
    anchor_sections = arm_sections["light"]
    target_words = _target_words_by_title(article)

    sections_out: dict[str, dict] = {}
    for idx, (title, _body) in enumerate(anchor_sections):
        norm_title = _normalize(title)
        tw = next((v for k, v in target_words.items() if norm_title in k or k in norm_title), None)
        guideline_ctx = f"Section: {title}" + (f"\nTarget length: {tw} words" if tw else "")

        body_light = _match_body(title, idx, arm_sections["light"])
        body_standard = _match_body(title, idx, arm_sections["standard"])
        if not body_light.strip() and not body_standard.strip():
            continue  # both empty, nothing to compare

        if random.random() < 0.5:
            a_arm, b_arm, doc_a, doc_b = "light", "standard", body_light, body_standard
        else:
            a_arm, b_arm, doc_a, doc_b = "standard", "light", body_standard, body_light

        logger.info("  %s / %s  (a=%s b=%s) x%d draws ...", article, title, a_arm, b_arm, n_draws)
        draws = await _grade_one(semaphore, doc_a, doc_b, guideline_ctx, model, n_draws)
        n_errors = sum(1 for d in draws if "error" in d)
        logger.info("    -> %d draws, %d errors", len(draws), n_errors)
        sections_out[title] = {"a_arm": a_arm, "b_arm": b_arm, "draws": draws}

    return {"article": article, "model": model.value, "n_draws": n_draws, "sections": sections_out}


async def _main_async(articles: list[str], model, n_draws: int, concurrency: int) -> None:
    semaphore = asyncio.Semaphore(concurrency)
    for article in articles:
        logger.info("Grading %s ...", article)
        result = await grade_article(article, model, n_draws, semaphore)
        out_dir = _OUTPUT_DIR / article
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "lightstd_judgments.json"
        out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        n_sections = len(result["sections"])
        n_calls = n_sections * n_draws
        logger.info("  wrote %s  (%d sections, %d calls)", out_path, n_sections, n_calls)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", required=True, help="Article-variant directory names.")
    parser.add_argument("--model", choices=sorted(_MODEL_CHOICES), default="claude")
    parser.add_argument("--n-draws", type=int, default=3, help="Draws per section (majority-vote-by-design, default 3).")
    parser.add_argument("--concurrency", type=int, default=3)
    args = parser.parse_args()

    model = _MODEL_CHOICES[args.model]
    logger.info("Judge model: %s  |  %d articles x %d draws/section", model.value, len(args.articles), args.n_draws)
    asyncio.run(_main_async(args.articles, model, args.n_draws, args.concurrency))


if __name__ == "__main__":
    main()
