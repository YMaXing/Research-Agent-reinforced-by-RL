"""
Pairwise-grading judge repeat-draws noise-floor check.

For a small, pre-selected set of (article, section, dimension) targets (see
research_agent_local/training/select_repeat_targets.py -- 10 "strong
disagreement" cases between tag-based and pairwise-reconciled grading, plus 5
"strong agreement" cases as a control), re-runs the EXACT SAME pairwise
comparison call (same doc_a/doc_b, same A/B slot as the original pilot run --
NOT re-randomized, to isolate judge-call noise from position-bias noise) N
times each, to measure how much the judge's own preference label moves around
on IDENTICAL input.

Reuses section-loading/matching logic from rl_pairwise_grading_generator.py
(same directory) rather than duplicating it.

Writes repeated judgments to:
    rl_training_data/pairwise_pilot/<article>/pairwise_repeats.json

Usage (from writing_workflow/):
  uv run python rl_pairwise_repeat_check.py --model claude --n-repeats 4
  uv run python rl_pairwise_repeat_check.py --model claude --n-repeats 4 --concurrency 3
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
from collections import defaultdict
from pathlib import Path

from brown.evals.metrics.pairwise_enhancement import grade_pairwise
from rl_pairwise_grading_generator import (
    _GRADED_ARMS,
    _MODEL_CHOICES,
    OUTPUT_DIR,
    _load_arm_sections,
    _match_body,
    _normalize,
    _target_words_by_title,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_pairwise_repeat_check")

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent
_DEFAULT_TARGETS_PATH = _REPO_ROOT / "research_agent_local" / "training" / "pairwise_repeat_targets.json"

# Cache per-article section bodies so a 15-target run only loads/splits each
# article's 3 arm article.md files once, not once per target.
_ARM_SECTIONS_CACHE: dict[str, dict[str, list[tuple[str, str]]]] = {}
_TARGET_WORDS_CACHE: dict[str, dict[str, int]] = {}


def _section_context(article: str, section_title: str) -> tuple[str, dict[str, str]]:
    """Return (guideline_ctx, {arm: body}) for one section, resolving the
    section's index against the light arm exactly like the original grading
    run did (grade_article() uses light as the anchor/ordering arm).
    """
    if article not in _ARM_SECTIONS_CACHE:
        _ARM_SECTIONS_CACHE[article] = _load_arm_sections(article)
        _TARGET_WORDS_CACHE[article] = _target_words_by_title(article)
    arm_sections = _ARM_SECTIONS_CACHE[article]
    target_words = _TARGET_WORDS_CACHE[article]

    anchor_sections = arm_sections["light"]
    norm_title = _normalize(section_title)
    idx = next((i for i, (t, _b) in enumerate(anchor_sections) if _normalize(t) == norm_title), None)
    if idx is None:
        idx = next(
            (i for i, (t, _b) in enumerate(anchor_sections) if norm_title in _normalize(t) or _normalize(t) in norm_title),
            0,
        )
    tw = next((v for k, v in target_words.items() if norm_title in k or k in norm_title), None)
    guideline_ctx = f"Section: {section_title}" + (f"\nTarget length: {tw} words" if tw else "")
    bodies = {arm: _match_body(section_title, idx, arm_sections[arm]) for arm in _GRADED_ARMS}
    return guideline_ctx, bodies


async def _repeat_one(target: dict, n_repeats: int, model, semaphore: asyncio.Semaphore) -> list[dict]:
    guideline_ctx, bodies = _section_context(target["article"], target["section_title"])
    a_arm, b_arm = target["a_arm"], target["b_arm"]
    doc_a, doc_b = bodies[a_arm], bodies[b_arm]
    dim = target["dimension"]

    async def _one_call() -> dict:
        async with semaphore:
            resp = await grade_pairwise(doc_a=doc_a, doc_b=doc_b, section_guideline=guideline_ctx, model=model)
        dim_result = getattr(resp, dim)
        return {
            "preference": dim_result.preference,
            "a_instances": dim_result.a_instances,
            "b_instances": dim_result.b_instances,
        }

    tasks = [_one_call() for _ in range(n_repeats)]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    out = []
    for r in results:
        out.append({"error": str(r)} if isinstance(r, BaseException) else r)
    return out


async def _main_async(targets: list[dict], n_repeats: int, model, concurrency: int) -> None:
    semaphore = asyncio.Semaphore(concurrency)
    by_article: dict[str, dict] = defaultdict(dict)

    for target in targets:
        article, title, dim = target["article"], target["section_title"], target["dimension"]
        logger.info(
            "Repeating %s / %s / %s (a=%s b=%s, orig_pref=%s, class=%s) x%d ...",
            article,
            title,
            dim,
            target["a_arm"],
            target["b_arm"],
            target["original_preference"],
            target["classification"],
            n_repeats,
        )
        repeats = await _repeat_one(target, n_repeats, model, semaphore)
        n_errors = sum(1 for r in repeats if "error" in r)
        logger.info("  -> %d repeats, %d errors", len(repeats), n_errors)
        by_article[article].setdefault(title, {})[dim] = {
            "a_arm": target["a_arm"],
            "b_arm": target["b_arm"],
            "original_preference": target["original_preference"],
            "classification": target["classification"],
            "repeats": repeats,
        }

    for article, sections in by_article.items():
        out_dir = OUTPUT_DIR / article
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "pairwise_repeats.json"
        out_path.write_text(json.dumps({"article": article, "sections": sections}, indent=2), encoding="utf-8")
        logger.info("Wrote %s", out_path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--targets", type=Path, default=_DEFAULT_TARGETS_PATH, help="Path to the target list JSON produced by select_repeat_targets.py"
    )
    parser.add_argument("--model", choices=sorted(_MODEL_CHOICES), default="claude")
    parser.add_argument(
        "--n-repeats",
        type=int,
        default=4,
        help="Additional draws per target, on top of the original single draw already collected (default 4 -> 5 total per target).",
    )
    parser.add_argument("--concurrency", type=int, default=3)
    args = parser.parse_args()

    targets = json.loads(args.targets.read_text(encoding="utf-8"))
    model = _MODEL_CHOICES[args.model]
    total_calls = len(targets) * args.n_repeats
    logger.info("Judge model: %s  |  %d targets x %d repeats = %d calls", model.value, len(targets), args.n_repeats, total_calls)
    asyncio.run(_main_async(targets, args.n_repeats, model, args.concurrency))


if __name__ == "__main__":
    main()
