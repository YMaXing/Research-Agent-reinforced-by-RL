"""
Phase 0 — Guideline Variant Generator

Generates 3 guideline variants per training article and sets up the corresponding
eval-dataset directories and exploitation-base directories required by the rest of
the RL pipeline (Phases 1, 2a, 2b).

Variant levels and intended oracle distribution:
  minimal   → 2–3 paragraph overview, no sections, forbids external examples
               → oracle skews P0/P1 (no exploration needed for minimal brief)
  standard  → exact copy of the original guideline (calibration baseline)
               → oracle P2/P3 (matches existing training articles)
  demanding → full structure + per-section word targets + production code requirements
               → oracle skews P2/P4 (exploration helps meet demanding brief)

What is created for each (article, level) pair:

  EVAL_DATA_DIR/{article}__var_{level}/
      article_guideline.md       ← variant guideline (LLM-generated or copied)
      article_ground_truth.md    ← copy of original GT (Strategy A: shared ground truth)

  BASES_DIR/{article}__var_{level}/   [only for articles with an existing base]
      <deep copy of BASES_DIR/{article}> with article_guideline.md overwritten
      exploitation_digest.md           ← copy from original (same research → same digest)

The exploitation base copy preserves all step-sentinels (_step1.done, etc.) so that
Phase 1 (rl_data_generator.py) skips the expensive exploitation re-run and proceeds
directly to copying the base into preset-specific episode directories, then runs the
exploration phase with the variant guideline.

After running this script, continue with the existing pipeline:

  Phase 1 : uv run python ../research_agent_local/rl_data_generator.py \\
                --articles {variant_names}
  Phase 2a: uv run python rl_writing_generator.py  --articles {variant_names}
  Phase 2b: uv run python rl_grading_generator.py  --articles {variant_names}

Where {variant_names} lists are printed at the end of this script's output.

Usage (from writing_workflow/):
  uv run python generate_guideline_variants.py                    # all articles, all levels
  uv run python generate_guideline_variants.py --dry-run          # show plan only
  uv run python generate_guideline_variants.py --articles 03_context_engineering
  uv run python generate_guideline_variants.py --variants minimal demanding
  uv run python generate_guideline_variants.py --force-regen      # overwrite existing guidelines

Implementation note on the training-signal coherence concern:
  All variants share the same research (copied from the original base) so the
  exploitation digest is identical across variants of the same article. The policy
  model (Qwen3-4B) therefore sees the same digest input for all three variants of
  an article. The GRPO gradient from each variant's reward array will point in
  slightly different directions (P0 for minimal, P2/P3 for demanding), but since
  the ground truth was written WITHOUT exploration, c_c anchors all variants toward
  low-exploration presets. The net effect is oracle diversity in the P0–P3 range,
  which is exactly the gap in the current 7-article training set.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Sequence

# ---------------------------------------------------------------------------
# Env / path bootstrap (must come before brown imports)
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_ENV_FILE = _THIS_DIR / ".env"

import os  # noqa: E402

# Allow ENV_FILE_PATH override for CI; default to .env beside this script.
if not os.environ.get("ENV_FILE_PATH"):
    os.environ["ENV_FILE_PATH"] = str(_ENV_FILE)

from langchain_core.messages import HumanMessage, SystemMessage  # noqa: E402

from brown.models import ModelConfig, SupportedModels, get_model  # noqa: E402

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("generate_guideline_variants")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_EVAL_DATA_DIR = _THIS_DIR / "inputs" / "evals" / "dataset" / "data"
_BASES_DIR = _THIS_DIR.parent / "rl_training_data" / "bases"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# LLM used for variant generation — Flash is sufficient and much cheaper than Pro
_GENERATION_MODEL = SupportedModels.GOOGLE_GEMINI_25_FLASH
_GENERATION_CONFIG = ModelConfig(
    temperature=0.6,
    thinking_budget=None,  # no thinking budget needed for creative generation
    max_retries=3,
)

MAX_RETRIES = 3
RETRY_BACKOFF_BASE = 15  # seconds

VARIANT_LEVELS: tuple[str, ...] = ("minimal", "standard", "demanding")

# Variant directory suffix convention
_VARIANT_SUFFIX = "__var_{level}"


# ---------------------------------------------------------------------------
# LLM prompt templates
# ---------------------------------------------------------------------------

_MINIMAL_SYSTEM = """\
You are a curriculum designer simplifying an AI course article guideline.
Return ONLY the final guideline text. No preamble, no explanation, no markdown code fences.\
"""

_MINIMAL_USER = """\
ORIGINAL GUIDELINE (full version):
{original_guideline}

---

Create a MINIMAL version of this guideline following these rules exactly:

1. **Total length**: 2–3 short paragraphs only.  No lesson outline, no narrative flow,
   no per-section breakdown, no headers beyond a single title line.

2. **Content**: State the article topic, target audience (from the original), a hard
   word-count ceiling ("keep the article under 1,500 words"), and the single main theme
   in plain prose.

3. **Restriction sentence** (include verbatim):
   "Use only concepts already established in the course — do not reference external
   libraries, real-world case studies, or production systems not already introduced in
   this lesson. External examples are out of scope."

4. **Framing**: Explicitly describe the article as a "conceptual overview" where
   surface-level treatment is expected. Signal that depth, exhaustive coverage, and
   code examples are NOT required.

5. **Course voice**: Preserve the we/you/our point-of-view convention and one sentence
   stating the lesson's position in the course (e.g., "This is lesson N of module M").
   Remove everything else from the Global Context section.

6. **No outline**: Do NOT include a lesson outline, narrative flow, theory/practice
   ratio, per-section word counts, or sub-section requirements of any kind.

Return ONLY the minimal guideline text.\
"""

_DEMANDING_SYSTEM = """\
You are a curriculum designer creating a demanding guideline for an AI course article.
Return ONLY the final guideline text. No preamble, no explanation, no markdown code fences.\
"""

_DEMANDING_USER = """\
ORIGINAL GUIDELINE (full version):
{original_guideline}

---

GROUND TRUTH ARTICLE (written from the original guideline without additional research):
{ground_truth}

---

Create a DEMANDING version of the original guideline following these rules exactly:

1. **Keep the complete structure**: Preserve all top-level sections from the original
   (Global Context, Lesson Scope, Narrative Flow, Lesson Outline, etc.) without removal.

2. **Per-section word targets**: For every numbered item in the Lesson Outline, add an
   estimated word count target in parentheses (e.g., "~450 words").  Distribute the
   total so sections sum to approximately 4,000–4,500 words overall.

3. **Additional Requirements block**: Append a new "## Additional Requirements" section
   after the Lesson Outline containing exactly these three bullet points:
   - "Include at least 2 production code examples showing real-world library usage with
     concrete comparisons to named alternatives (e.g., Library A vs Library B in a
     production context)."
   - "Cover at least one real-world failure mode with a named production context (company,
     benchmark, or published case study) and a concrete mitigation strategy."
   - "Every concept section must anchor its theory in at least one industry example drawn
     from a named production system, benchmark paper, or public post-mortem."

4. **Must-cover-in-depth additions**: Examine the ground truth article section by section.
   For each section where a concept is present but covered in under 100 words in the
   ground truth, add a "Must cover in depth:" line inside that section's outline entry
   listing the specific aspects to expand.  Use only topics already present in the
   ground truth — do NOT invent subjects absent from the article.

5. **Preserve all course instructions**: Keep the point-of-view rules, concepts
   introduced/future lessons, lesson scope, course context, and golden-source references
   exactly as in the original.  Add requirements on top; do not subtract.

Return ONLY the demanding guideline text.\
"""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _variant_article_name(article: str, level: str) -> str:
    return f"{article}{_VARIANT_SUFFIX.format(level=level)}"


def _read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def _copy_file(src: Path, dst: Path) -> None:
    shutil.copy2(src, dst)


def _count_words(text: str) -> int:
    return len(text.split())


# ---------------------------------------------------------------------------
# LLM variant generation
# ---------------------------------------------------------------------------


async def _generate_variant(
    llm,
    system_prompt: str,
    user_prompt: str,
    article: str,
    level: str,
) -> str:
    """Call the LLM with retry; returns the generated guideline text."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt),
            ]
            response = await llm.ainvoke(messages)
            text = response.content.strip()
            if not text:
                raise ValueError("LLM returned empty response")
            return text
        except Exception as exc:
            logger.warning(
                "[%s/%s] attempt %d/%d failed: %s",
                article,
                level,
                attempt,
                MAX_RETRIES,
                exc,
            )
            if attempt < MAX_RETRIES:
                wait = attempt * RETRY_BACKOFF_BASE
                logger.info("  retrying in %ds …", wait)
                await asyncio.sleep(wait)

    raise RuntimeError(f"Failed to generate {level} guideline for {article} after {MAX_RETRIES} attempts")


# ---------------------------------------------------------------------------
# Per-article processing
# ---------------------------------------------------------------------------


async def process_article(
    article: str,
    levels: Sequence[str],
    force_regen: bool,
    dry_run: bool,
    llm,
) -> dict[str, str]:
    """Generate and materialise all requested variant levels for one article.

    Returns a dict {level: variant_article_name} for the levels processed.
    """
    src_eval_dir = _EVAL_DATA_DIR / article
    guideline_path = src_eval_dir / "article_guideline.md"
    gt_path = src_eval_dir / "article_ground_truth.md"

    if not guideline_path.exists():
        logger.warning("[SKIP] %s — article_guideline.md not found", article)
        return {}
    if not gt_path.exists():
        logger.warning("[SKIP] %s — article_ground_truth.md not found", article)
        return {}

    original_guideline = _read_file(guideline_path)
    ground_truth = _read_file(gt_path)

    original_base = _BASES_DIR / article
    has_base = original_base.exists() and (original_base / ".research").exists()
    if not has_base:
        logger.warning(
            "[WARN] %s — no exploitation base found in %s; "
            "BASES_DIR variant directories will be skipped. "
            "Run Phase 1 (rl_data_generator.py) for this article first.",
            article,
            _BASES_DIR,
        )

    processed: dict[str, str] = {}

    for level in levels:
        variant_name = _variant_article_name(article, level)
        variant_eval_dir = _EVAL_DATA_DIR / variant_name
        variant_base_dir = _BASES_DIR / variant_name

        variant_guideline_path = variant_eval_dir / "article_guideline.md"
        already_done = variant_guideline_path.exists() and not force_regen

        # ── Determine guideline text ──────────────────────────────────────
        if level == "standard":
            guideline_text = original_guideline
            gen_source = "copy of original"
        elif already_done:
            guideline_text = _read_file(variant_guideline_path)
            gen_source = "existing (skipped regeneration)"
        else:
            # Generate via LLM
            if level == "minimal":
                sys_prompt = _MINIMAL_SYSTEM
                user_prompt = _MINIMAL_USER.format(original_guideline=original_guideline)
                gen_source = f"LLM-generated ({_GENERATION_MODEL.split(':')[-1]})"
            elif level == "demanding":
                sys_prompt = _DEMANDING_SYSTEM
                user_prompt = _DEMANDING_USER.format(
                    original_guideline=original_guideline,
                    ground_truth=ground_truth,
                )
                gen_source = f"LLM-generated ({_GENERATION_MODEL.split(':')[-1]})"
            else:
                logger.error("Unknown variant level: %s", level)
                continue

            if dry_run:
                logger.info(
                    "  [DRY-RUN] would generate %s guideline for %s via LLM",
                    level,
                    article,
                )
                guideline_text = f"[DRY-RUN placeholder for {level} variant of {article}]"
            else:
                logger.info("  Generating %s guideline for %s …", level, article)
                t0 = time.monotonic()
                guideline_text = await _generate_variant(llm, sys_prompt, user_prompt, article, level)
                elapsed = time.monotonic() - t0
                logger.info(
                    "  %s/%s generated in %.1fs (%d words)",
                    article,
                    level,
                    elapsed,
                    _count_words(guideline_text),
                )

        # ── Materialise EVAL_DATA_DIR variant ────────────────────────────
        if dry_run:
            logger.info(
                "  [DRY-RUN] would create %s  (guideline: %s)",
                variant_eval_dir,
                gen_source,
            )
        else:
            variant_eval_dir.mkdir(parents=True, exist_ok=True)
            _write_file(variant_eval_dir / "article_guideline.md", guideline_text)
            _copy_file(gt_path, variant_eval_dir / "article_ground_truth.md")
            # Also copy research.md if present (not required by grader but useful for reference)
            src_research = src_eval_dir / "research.md"
            if src_research.exists():
                _copy_file(src_research, variant_eval_dir / "research.md")
            logger.info(
                "  [EVAL_DIR] %s  (%s, %d words)",
                variant_name,
                gen_source,
                _count_words(guideline_text),
            )

        # ── Materialise BASES_DIR variant ─────────────────────────────────
        if has_base:
            if dry_run:
                logger.info("  [DRY-RUN] would copy base → %s", variant_base_dir)
            elif variant_base_dir.exists() and not force_regen:
                logger.info(
                    "  [BASE_DIR] %s already exists — skipping (use --force-regen to overwrite)",
                    variant_name,
                )
            else:
                # Deep-copy the original base (preserves all step-sentinels and research)
                if variant_base_dir.exists():
                    shutil.rmtree(variant_base_dir)
                shutil.copytree(original_base, variant_base_dir)
                # Overwrite the guideline in the copy with the variant version
                dst_guideline = variant_base_dir / "article_guideline.md"
                _write_file(dst_guideline, guideline_text)
                # Copy exploitation_digest.md if present (same research → same digest)
                src_digest = original_base / "exploitation_digest.md"
                if src_digest.exists():
                    _copy_file(src_digest, variant_base_dir / "exploitation_digest.md")
                logger.info("  [BASE_DIR] %s  (copied from %s)", variant_name, article)

        processed[level] = variant_name

    return processed


# ---------------------------------------------------------------------------
# Pipeline
# ---------------------------------------------------------------------------


async def run_pipeline(
    articles: Sequence[str] | None,
    levels: Sequence[str],
    force_regen: bool,
    dry_run: bool,
) -> None:
    """Process all requested articles and levels."""

    # Discover articles from EVAL_DATA_DIR if not specified
    if articles:
        article_list = list(articles)
    else:
        article_list = sorted(
            d.name
            for d in _EVAL_DATA_DIR.iterdir()
            if d.is_dir()
            and not re.search(r"__var_", d.name)  # skip existing variant dirs
            and (d / "article_guideline.md").exists()
            and (d / "article_ground_truth.md").exists()
        )

    if not article_list:
        logger.error("No articles found with both article_guideline.md and article_ground_truth.md")
        sys.exit(1)

    logger.info("=" * 70)
    logger.info("Phase 0: Guideline Variant Generation")
    logger.info("  Articles : %s", article_list)
    logger.info("  Levels   : %s", list(levels))
    logger.info("  Eval dir : %s", _EVAL_DATA_DIR)
    logger.info("  Bases dir: %s", _BASES_DIR)
    logger.info("  Dry-run  : %s", dry_run)
    logger.info("  Force    : %s", force_regen)
    logger.info("=" * 70)

    if dry_run:
        logger.info("DRY RUN — no files will be written and no LLM calls will be made.")

    # Initialise the LLM (single instance shared across all calls)
    llm = get_model(_GENERATION_MODEL, _GENERATION_CONFIG)

    all_variants: dict[str, list[str]] = {}  # article → [variant_names]
    failed: list[str] = []

    for article in article_list:
        logger.info("─" * 60)
        logger.info("Article: %s", article)
        try:
            processed = await process_article(article, levels, force_regen, dry_run, llm)
            if processed:
                all_variants[article] = list(processed.values())
        except Exception:
            logger.exception("FAILED: %s", article)
            failed.append(article)

    # ── Summary ──────────────────────────────────────────────────────────
    logger.info("=" * 70)
    logger.info("Variant generation complete")

    if failed:
        logger.warning("Failed articles: %s", failed)

    all_variant_names: list[str] = []
    for names in all_variants.values():
        all_variant_names.extend(names)

    if all_variant_names and not dry_run:
        logger.info("")
        logger.info("Next steps — run the RL pipeline for these variant articles:")
        logger.info("")
        variant_list_str = " ".join(all_variant_names)
        logger.info(
            "  Phase 1  (research generation):\n"
            "    cd ../research_agent_local\n"
            "    uv run --project mcp_server python rl_data_generator.py \\\n"
            "        --articles %s",
            variant_list_str,
        )
        logger.info("")
        logger.info(
            "  Phase 2a (article writing):\n"
            "    cd ../writing_workflow\n"
            "    uv run python rl_writing_generator.py \\\n"
            "        --articles %s",
            variant_list_str,
        )
        logger.info("")
        logger.info(
            "  Phase 2b (grading):\n    uv run python rl_grading_generator.py \\\n        --articles %s",
            variant_list_str,
        )
        logger.info("")
        logger.info(
            "  Phase 2c (digests — if not already copied from original base):\n"
            "    cd ../research_agent_local\n"
            "    uv run --project mcp_client python training/generate_digests.py \\\n"
            "        --articles %s",
            variant_list_str,
        )

    logger.info("=" * 70)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=("Phase 0: Generate minimal / standard / demanding guideline variants for RL training-data diversity."),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        default=None,
        metavar="ARTICLE",
        help=(
            "Article folder names to process (default: all articles in EVAL_DATA_DIR "
            "that have both article_guideline.md and article_ground_truth.md)."
        ),
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        default=list(VARIANT_LEVELS),
        choices=list(VARIANT_LEVELS),
        metavar="LEVEL",
        help=f"Variant levels to generate (default: all three: {', '.join(VARIANT_LEVELS)}).",
    )
    parser.add_argument(
        "--force-regen",
        action="store_true",
        default=False,
        help=("Regenerate guideline text even if the variant directory already exists. Also overwrites existing base directories."),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=False,
        help="Show what would be done without making LLM calls or writing files.",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    asyncio.run(
        run_pipeline(
            articles=args.articles,
            levels=args.variants,
            force_regen=args.force_regen,
            dry_run=args.dry_run,
        )
    )


if __name__ == "__main__":
    main()
