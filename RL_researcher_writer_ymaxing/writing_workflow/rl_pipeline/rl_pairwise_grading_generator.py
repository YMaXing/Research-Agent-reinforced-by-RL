"""
Pairwise depth/breadth-enhancement grading pilot.

For each target article, loads the light/standard/deep arms' article.md,
splits each into sections, and for each section runs 3 pairwise comparisons
(light-vs-standard, light-vs-deep, standard-vs-deep) via
brown.evals.metrics.pairwise_enhancement.grade_pairwise(). Each call judges
BOTH depth and breadth in one structured-output response, so the total call
count is (# sections) x 3 pairs -- NOT x6.

Position-bias handling: for each (section, pair), the two named arms are
randomly assigned to the "A"/"B" slots (not both orders, to keep costs at the
~180-call estimate instead of ~360). The random assignment is recorded in the
output so results can be mapped back to the correct arm regardless of which
slot it landed in.

Raw judgments are written to:
    rl_training_data/pairwise/pilot/<article>/pairwise_judgments.json

This script does NOT compute rewards or make any oracle/production changes --
it only produces raw judgment data for a later reconciliation step
(research_agent_local/training/pairwise_reward.py, run separately) to
convert into a numeric scale comparable to enhancement_credit().

Usage (from writing_workflow/):
  uv run python rl_pipeline/rl_pairwise_grading_generator.py \\
      --articles 09_RAG__var_standard 06_tools__var_standard 13_agent_framework Dark_Dimension \\
      --model claude

  uv run python rl_pipeline/rl_pairwise_grading_generator.py --articles 13_agent_framework --model gemini --concurrency 2
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import random
import re
from pathlib import Path

from brown.evals.metrics.pairwise_enhancement import grade_pairwise
from brown.models import SupportedModels

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("rl_pairwise_grading_generator")

# ---------------------------------------------------------------------------
# Paths -- same physical rl_training_data/ tree used throughout this
# investigation, just referenced from writing_workflow/'s relative root
# (mirrors EPISODES_DIR / TEST_EPISODES_DIR in rl_grading_generator.py).
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"
BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
OUTPUT_DIR = _REPO_ROOT / "rl_training_data" / "pairwise" / "pilot"

# Active preset->arm mapping. TRAIN-variant articles (name contains "__var_")
# use presets {0,1,3,5}; TEST/no-variant articles use presets {0,1,2,3}.
# Mirrors generate_episode_oracles.py / sweep_reward_formula.py's convention
# established earlier in this investigation.
_TRAIN_ARM_PRESETS = {"skip": 0, "light": 1, "standard": 3, "deep": 5}
_TEST_ARM_PRESETS = {"skip": 0, "light": 1, "standard": 2, "deep": 3}

_GRADED_ARMS = ("light", "standard", "deep")
_PAIRS = [("light", "standard"), ("light", "deep"), ("standard", "deep")]

_H2_RE = re.compile(r"^## (.+)$", re.MULTILINE)
_H1_LINE_RE = re.compile(r"^#\s+.+?\n")
_REFERENCES_RE = re.compile(r"^## References\b.*$", re.MULTILINE | re.DOTALL)

_MODEL_CHOICES = {
    "gemini": SupportedModels.GOOGLE_GEMINI_25_PRO,
    "claude": SupportedModels.ANTHROPIC_CLAUDE_SONNET,
}


def _normalize(title: str) -> str:
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def _split_sections(text: str) -> list[tuple[str, str]]:
    """Split an article.md into (title, body) pairs by H2 header, including the
    intro (pre-first-H2 text, minus the H1 title line) as an "Introduction"
    section. Stops before "## References" (citations are not graded content).
    """
    text = _REFERENCES_RE.split(text, maxsplit=1)[0]
    parts = _H2_RE.split(text)
    out: list[tuple[str, str]] = []
    intro = _H1_LINE_RE.sub("", parts[0], count=1).strip()
    if intro:
        out.append(("Introduction", intro))
    for i in range(1, len(parts), 2):
        body = parts[i + 1] if i + 1 < len(parts) else ""
        out.append((parts[i].strip(), body.strip()))
    return out


def _load_arm_sections(article: str) -> dict[str, list[tuple[str, str]]]:
    """Load and split all 3 graded arms' (light/standard/deep) article.md for one article."""
    is_train_variant = "__var_" in article
    presets = _TRAIN_ARM_PRESETS if is_train_variant else _TEST_ARM_PRESETS
    root = EPISODES_DIR if is_train_variant else TEST_EPISODES_DIR
    sections: dict[str, list[tuple[str, str]]] = {}
    for arm in _GRADED_ARMS:
        f = root / f"{article}__preset{presets[arm]}" / "article.md"
        if not f.exists():
            raise FileNotFoundError(f"Missing episode article for {article!r} arm={arm!r}: {f}")
        text = f.read_text(encoding="utf-8", errors="replace")
        sections[arm] = _split_sections(text)
    return sections


def _target_words_by_title(article: str) -> dict[str, int]:
    """Best-effort lookup of each section's target_words from guideline_features.json,
    keyed by normalized title fragment (matched against the "S{n}::slug" key suffix).
    Returns {} if the file is missing or malformed (context is best-effort, not required).
    """
    feat_path = BASES_DIR / article / "guideline_features.json"
    if not feat_path.exists():
        return {}
    try:
        data = json.loads(feat_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    out = {}
    for key, info in data.get("sections", {}).items():
        slug = key.split("::", 1)[-1]
        out[_normalize(slug.replace("-", " "))] = info.get("target_words")
    return out


def _match_body(anchor_title: str, anchor_idx: int, arm_sections: list[tuple[str, str]]) -> str:
    """Find the body text in `arm_sections` matching `anchor_title` (by normalized
    substring match), falling back to positional index if no title match is found.
    """
    norm_anchor = _normalize(anchor_title)
    for title, body in arm_sections:
        norm_title = _normalize(title)
        if norm_anchor == norm_title or norm_anchor in norm_title or norm_title in norm_anchor:
            return body
    if anchor_idx < len(arm_sections):
        return arm_sections[anchor_idx][1]
    return ""


async def _grade_one(
    semaphore: asyncio.Semaphore,
    doc_a: str,
    doc_b: str,
    section_guideline: str,
    model: SupportedModels,
):
    async with semaphore:
        return await grade_pairwise(doc_a=doc_a, doc_b=doc_b, section_guideline=section_guideline, model=model)


async def grade_article(article: str, model: SupportedModels, semaphore: asyncio.Semaphore) -> dict:
    arm_sections = _load_arm_sections(article)
    anchor_sections = arm_sections["light"]  # title/order anchor (arbitrary choice among the 3 arms)
    target_words = _target_words_by_title(article)

    tasks = []
    task_meta = []
    for idx, (title, _body) in enumerate(anchor_sections):
        norm_title = _normalize(title)
        tw = next((v for k, v in target_words.items() if norm_title in k or k in norm_title), None)
        guideline_ctx = f"Section: {title}" + (f"\nTarget length: {tw} words" if tw else "")

        bodies = {arm: _match_body(title, idx, arm_sections[arm]) for arm in _GRADED_ARMS}

        for arm_x, arm_y in _PAIRS:
            if not bodies[arm_x].strip() and not bodies[arm_y].strip():
                continue  # both empty -- nothing to compare, skip the call entirely
            if random.random() < 0.5:
                a_arm, b_arm = arm_x, arm_y
            else:
                a_arm, b_arm = arm_y, arm_x
            tasks.append(_grade_one(semaphore, bodies[a_arm], bodies[b_arm], guideline_ctx, model))
            task_meta.append((title, arm_x, arm_y, a_arm, b_arm))

    logger.info("  %s: %d sections, %d pairwise calls queued", article, len(anchor_sections), len(tasks))
    responses = await asyncio.gather(*tasks, return_exceptions=True)

    sections_out: dict[str, dict] = {}
    for (title, arm_x, arm_y, a_arm, b_arm), resp in zip(task_meta, responses):
        sections_out.setdefault(title, {})
        pair_key = f"{arm_x}_vs_{arm_y}"
        if isinstance(resp, BaseException):
            logger.error("  %s / %s: FAILED: %s", article, pair_key, resp)
            sections_out[title][pair_key] = {"error": str(resp), "a_arm": a_arm, "b_arm": b_arm}
            continue
        sections_out[title][pair_key] = {
            "a_arm": a_arm,
            "b_arm": b_arm,
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

    return {"article": article, "model": model.value, "sections": sections_out}


async def _main_async(articles: list[str], model: SupportedModels, concurrency: int) -> None:
    semaphore = asyncio.Semaphore(concurrency)
    for article in articles:
        logger.info("Grading %s ...", article)
        result = await grade_article(article, model, semaphore)
        out_dir = OUTPUT_DIR / article
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "pairwise_judgments.json"
        out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
        n_calls = sum(len(v) for v in result["sections"].values())
        n_errors = sum(1 for v in result["sections"].values() for r in v.values() if "error" in r)
        logger.info("  wrote %s  (%d sections, %d calls, %d errors)", out_path, len(result["sections"]), n_calls, n_errors)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--articles",
        nargs="+",
        required=True,
        help="Article-variant directory names, e.g. 09_RAG__var_standard 13_agent_framework",
    )
    parser.add_argument(
        "--model",
        choices=sorted(_MODEL_CHOICES),
        default="claude",
        help="Judge model: 'claude' (Claude Sonnet, default -- the more reliable judge per this "
        "investigation's prior re-grades) or 'gemini' (Gemini 2.5 Pro).",
    )
    parser.add_argument("--concurrency", type=int, default=3, help="Max concurrent grading calls (default 3).")
    args = parser.parse_args()

    model = _MODEL_CHOICES[args.model]
    logger.info("Judge model: %s", model.value)
    asyncio.run(_main_async(args.articles, model, args.concurrency))


if __name__ == "__main__":
    main()
