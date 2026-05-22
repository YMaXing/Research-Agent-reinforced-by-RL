"""Generate section-level oracles from episode reward data.

Reads reasoning.json from all 6 preset episodes for each (article, variant)
combination, computes per-section rewards using the variant-appropriate formula,
and writes section_oracle.json with the full reward vector per arm.

This REPLACES the heuristic oracle produced by generate_digests.py (_preset_2d)
with empirically derived labels from actual episode runs.

Oracle schema written (version 2):
{
  "version": 2,
  "article": "<article_slug>",
  "variant": "var_minimal|var_standard|var_demanding",
  "sections": {
    "<sec_id>": {
      "oracle":  "skip|light|standard|deep",   <- argmax arm
      "rewards": {                              <- per-arm section reward
        "skip": 0.123,
        "light": 0.456,
        "standard": 0.789,
        "deep": 0.321
      }
    },
    ...
  },
  "presets": {                                  <- legacy field (oracle label only)
    "<sec_id>": "skip|light|standard|deep",
    ...
  }
}

Usage (from research_agent_local/):
    python3 training/generate_episode_oracles.py
    python3 training/generate_episode_oracles.py --dry-run
    python3 training/generate_episode_oracles.py --articles 02_workflows_vs_agents
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
_ALL_ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
]
_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]

# Active preset → round counts (presets 2 and 4 are archived)
# 0=baseline(0r), 1=single_balanced(1r), 3=depth_then_breadth(2r), 5=depth_breadth_depth(3r)
_EPISODE_ROUNDS: dict[int, int] = {0: 0, 1: 1, 3: 2, 5: 3}

# 4-arm → single active preset  (archived presets 2 and 4 are NOT used)
_ARM_PRESETS: dict[str, list[int]] = {
    "skip":     [0],  # baseline         (0 rounds)
    "light":    [1],  # single_balanced  (1 round,  balanced)
    "standard": [3],  # depth_then_breadth (2 rounds, depth→breadth)
    "deep":     [5],  # depth_breadth_depth (3 rounds, depth→breadth→depth)
}
_ARM_ROUNDS: dict[str, int] = {"skip": 0, "light": 1, "standard": 2, "deep": 3}
_ARM_ORDER = ["skip", "light", "standard", "deep"]

# Dimensions used in the reward formula (same as _REWARD_DIMS in train_grpo.py)
_REWARD_DIMS = [
    "ground_truth_core_content",      # cc
    "ground_truth_flow",              # fl
    "ground_truth_depth_enhancement", # de
    "ground_truth_breadth_enhancement", # be
    "ground_truth_core_preservation", # cp
    "user_intent_guideline_adherence", # ga
    "user_intent_research_anchoring",  # ra
]

# Section titles that are not article content sections (skip when building oracle)
_NON_CONTENT_SECTIONS = {"references", "bibliography", "further reading", "notes"}


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _normalize(title: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    title = title.lower()
    title = re.sub(r"[^a-z0-9\s]", " ", title)
    title = re.sub(r"\s+", " ", title).strip()
    return title


def _is_non_content(title: str) -> bool:
    return _normalize(title) in _NON_CONTENT_SECTIONS


def _parse_sections_ordered(text: str) -> list[tuple[str, str, int]]:
    """Parse per-section binary scores from one reasoning.json dimension value.

    Each block is separated by a blank line and formatted as:
        Title (may contain colons):\n**[0|1]:** reasoning text

    Returns list of (raw_title, norm_title, score) in order of appearance.
    Skips non-content sections (References etc.).
    """
    results: list[tuple[str, str, int]] = []
    for part in text.split("\n\n"):
        part = part.strip()
        if not part:
            continue
        # Lazy match so it captures up to the LAST ":\n" before "**[01]:**"
        m = re.match(r"^(.+?):\n\*\*([01]):\*\*", part)
        if m:
            raw = m.group(1).strip()
            if not _is_non_content(raw):
                results.append((raw, _normalize(raw), int(m.group(2))))
    return results


def _extract_sec_ids_ordered(digest: str) -> list[str]:
    """Extract ordered section IDs from the <section_coverage> block."""
    return re.findall(r'<section\s+id="(S\d+::[^"]+)"', digest)


def _sec_id_to_norm(sec_id: str) -> str:
    """Derive a normalized title string from a sec_id slug for fuzzy matching.

    'S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces'
    -> 'introduction the critical decision every ai engineer faces'
    """
    m = re.match(r"S\d+::section-\d+-(.+)", sec_id)
    slug = m.group(1) if m else sec_id
    return _normalize(slug.replace("-", " "))


# ---------------------------------------------------------------------------
# Section-score lookup with fallback
# ---------------------------------------------------------------------------

def _get_score(
    dim_entries: list[tuple[str, str, int]],  # (raw, norm, score) ordered
    target_norm: str,
    ordinal_idx: int,
) -> float:
    """Look up a section's binary score in one dimension.

    Strategy (in priority order):
    1. Exact normalized-title match.
    2. Substring match (handles 'Introduction' vs 'Introduction: Full Title').
    3. Ordinal position fallback (nth entry in the dimension list).
    4. Return 0.0 if nothing works.
    """
    # Build lookup by norm title
    by_norm = {norm: score for _, norm, score in dim_entries}

    # 1. Exact
    if target_norm in by_norm:
        return float(by_norm[target_norm])

    # 2. Substring (one is a prefix/suffix of the other)
    for norm, score in by_norm.items():
        if target_norm in norm or norm in target_norm:
            return float(score)

    # 3. Ordinal
    if ordinal_idx < len(dim_entries):
        return float(dim_entries[ordinal_idx][2])

    return 0.0


# ---------------------------------------------------------------------------
# Reward formula (mirrors _compute_episode_reward in train_grpo.py)
# ---------------------------------------------------------------------------

def _section_reward(
    cc: float, fl: float, de: float, be: float,
    cp: float, ga: float, ra: float,
    nr: int,
    variant: str,
) -> float:
    """Compute section-level reward with variant-appropriate formula."""
    if variant == "minimal":
        gt_base     = 0.05 * cc + 0.05 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.10
        user_intent = 0.70 * ga + 0.10 * ra
        cost        = -0.02 * nr
    elif variant == "demanding":
        gt_base     = 0.12 * cc + 0.08 * fl
        explore     = cp * (0.55 * de + 0.35 * be) * 0.50
        user_intent = (0.60 * ga + 0.40 * ra) * 0.25
        cost        = -0.005 * nr
    else:  # standard
        gt_base     = 0.20 * cc + 0.20 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.30
        user_intent = (0.50 * ga + 0.50 * ra) * 0.30
        cost        = -0.02 * nr
    return gt_base + explore + user_intent + cost


# ---------------------------------------------------------------------------
# Per-episode loading
# ---------------------------------------------------------------------------

def _load_episode(episode_dir: Path) -> dict[str, list[tuple[str, str, int]]]:
    """Load reasoning.json and return {dim: [(raw, norm, score), ...]} in order."""
    path = episode_dir / "reasoning.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        log.warning("  Malformed reasoning.json in %s (%s); skipping episode.", episode_dir.name, exc)
        return {}
    return {
        dim: _parse_sections_ordered(data[dim])
        for dim in _REWARD_DIMS
        if dim in data
    }


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def _count_reasoning_sections(episode_dir: Path) -> int:
    """Count distinct content sections in one preset's reasoning.json (reference dim)."""
    path = episode_dir / "reasoning.json"
    if not path.exists():
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    ref = data.get("ground_truth_core_content", "")
    return len(_parse_sections_ordered(ref))


def process_article_variant(
    article: str,
    variant: str,
    dry_run: bool = False,
) -> bool:
    """Derive and write the section oracle for one (article, variant) pair."""
    art_var = f"{article}__{variant}"
    bases_dir = _BASES_DIR / art_var

    if not bases_dir.exists():
        log.warning("  Bases dir missing: %s", art_var)
        return False

    # Determine the digest to use for sec_id extraction.
    # Some variant digests were truncated during generation (section_coverage has
    # fewer entries than the article actually has).  When that happens, fall back
    # to the base (non-variant) directory, which has the complete coverage block.
    digest_path = bases_dir / "research_digest.md"
    if not digest_path.exists():
        log.warning("  No digest: %s", art_var)
        return False

    digest = digest_path.read_text(encoding="utf-8")
    sec_ids = _extract_sec_ids_ordered(digest)

    # Check completeness against the episode's reasoning.json
    ep0_dir = _EPISODES_DIR / f"{art_var}__preset0"
    expected_n = _count_reasoning_sections(ep0_dir) if ep0_dir.exists() else len(sec_ids)

    if len(sec_ids) < expected_n:
        # Try the base directory (no variant suffix) as fallback
        base_digest_path = _BASES_DIR / article / "research_digest.md"
        if base_digest_path.exists():
            base_sec_ids = _extract_sec_ids_ordered(base_digest_path.read_text(encoding="utf-8"))
            if len(base_sec_ids) >= expected_n:
                log.info(
                    "  %s: digest has %d/%d sections; using base dir for sec_ids",
                    art_var, len(sec_ids), expected_n,
                )
                sec_ids = base_sec_ids
            else:
                log.warning(
                    "  %s: digest incomplete (%d sections, expected %d); "
                    "base dir also incomplete (%d). Using what we have.",
                    art_var, len(sec_ids), expected_n, len(base_sec_ids),
                )
        else:
            log.warning(
                "  %s: digest incomplete (%d sections, expected %d); "
                "no base dir fallback available.",
                art_var, len(sec_ids), expected_n,
            )

    if not sec_ids:
        log.warning("  No section IDs found for %s", art_var)
        return False

    sec_norms = [_sec_id_to_norm(sid) for sid in sec_ids]

    # Active preset IDs (archived presets 2 and 4 are excluded)
    _ACTIVE_PRESETS = sorted(_EPISODE_ROUNDS.keys())  # [0, 1, 3, 5]

    # Load only the active episodes upfront (dict keyed by preset id)
    episode_dims: dict[int, dict[str, list[tuple[str, str, int]]]] = {}
    for p in _ACTIVE_PRESETS:
        ep_dir = _EPISODES_DIR / f"{art_var}__preset{p}"
        if not ep_dir.exists():
            log.warning("  Missing episode dir: %s__preset%d", art_var, p)
            episode_dims[p] = {}
        else:
            episode_dims[p] = _load_episode(ep_dir)

    # Determine the variant short name for the reward formula
    variant_short = variant.replace("var_", "")  # minimal / standard / demanding

    # For each section, compute per-arm rewards from the 4 active presets
    sections_output: dict[str, dict] = {}

    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        # Per-active-preset reward
        preset_rewards: dict[int, float] = {}
        for p in _ACTIVE_PRESETS:
            ep = episode_dims[p]
            nr = _EPISODE_ROUNDS[p]

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return _get_score(_ep.get(dim, []), _sn, _si)

            preset_rewards[p] = _section_reward(
                cc=_score("ground_truth_core_content"),
                fl=_score("ground_truth_flow"),
                de=_score("ground_truth_depth_enhancement"),
                be=_score("ground_truth_breadth_enhancement"),
                cp=_score("ground_truth_core_preservation"),
                ga=_score("user_intent_guideline_adherence"),
                ra=_score("user_intent_research_anchoring"),
                nr=nr,
                variant=variant_short,
            )

        # Map active presets → 4 arms (each arm now maps to exactly one preset)
        arm_rewards: dict[str, float] = {
            arm: max(preset_rewards[p] for p in preset_ids)
            for arm, preset_ids in _ARM_PRESETS.items()
        }
        oracle = max(_ARM_ORDER, key=arm_rewards.__getitem__)

        sections_output[sec_id] = {
            "oracle": oracle,
            "rewards": {k: round(arm_rewards[k], 6) for k in _ARM_ORDER},
        }

    # Summary stats for logging
    dist: dict[str, int] = {}
    for info in sections_output.values():
        dist[info["oracle"]] = dist.get(info["oracle"], 0) + 1
    log.info(
        "  %s: %d sections  oracle dist: %s",
        art_var, len(sections_output), dist,
    )

    if dry_run:
        return True

    # Write section_oracle.json (version 2 format)
    output = {
        "version": 2,
        "article": article,
        "variant": variant,
        "sections": sections_output,
        # Legacy 'presets' field kept for backward compat with any code that
        # reads the old format before load_section_groups is updated.
        "presets": {sid: info["oracle"] for sid, info in sections_output.items()},
    }
    oracle_path = bases_dir / "section_oracle.json"
    oracle_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate section-level oracles from episode reward data."
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        metavar="SLUG",
        default=None,
        help="Process only these article slugs (default: all 8).",
    )
    parser.add_argument(
        "--variants",
        nargs="+",
        choices=_VARIANTS,
        default=_VARIANTS,
        help="Process only these variants (default: all 3).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and compute rewards but do NOT write oracle files.",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    articles = args.articles if args.articles else _ALL_ARTICLES

    log.info("=== generate_episode_oracles  dry_run=%s ===", args.dry_run)
    log.info("Episodes dir: %s", _EPISODES_DIR)
    log.info("Bases dir:    %s", _BASES_DIR)
    log.info("Articles: %s", articles)
    log.info("Variants: %s", args.variants)

    ok = fail = 0
    for article in articles:
        for variant in args.variants:
            log.info("Processing %s__%s", article, variant)
            if process_article_variant(article, variant, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1

    log.info("Done: %d OK, %d failed", ok, fail)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
