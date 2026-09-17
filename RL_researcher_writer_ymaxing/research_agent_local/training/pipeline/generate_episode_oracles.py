"""Generate section-level oracles from episode reward data.

Reads reasoning.json from all 6 preset episodes for each (article, variant)
combination, computes per-section rewards using the variant-appropriate formula,
and writes section_oracle.json with the full reward vector per arm.

This REPLACES the heuristic oracle produced by generate_digests.py (_preset_2d)
with empirically derived labels from actual episode runs.

Version 3 (current): depth_enhancement/breadth_enhancement are no longer treated
as raw 0/1 grader scores in the reward formula. The grader now reports, per
section, a capped-but-uncapped-count `[instances=N; quality=strong|standard,...]`
tag inside the reason text (see writing_workflow's new_follows_gt prompts); this
module parses that tag and maps it through enhancement_reward.enhancement_credit()
-- a tunable, saturating count x quality curve -- before folding it into
_section_reward's explore term. See run13_rl_grok_pipeline_analysis.md Part 5
(sections 25-27) for the bias this fixes and enhancement_reward.py for the tunable
parameters. Legacy (pre-tag) reasoning.json files -- i.e. articles not yet
re-graded with the new prompt -- keep their EXACT pre-v3 numeric behaviour: the
raw 0/1 grader score is used directly, bypassing enhancement_credit() entirely.
Re-running this script on an un-migrated article is a safe no-op with respect to
its computed rewards; only re-graded articles (which carry the tag) see the new
curve applied.

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

from enhancement_reward import enhancement_credit

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
_REPO_ROOT = _THIS_DIR.parent.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"

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

# No-variant (test-set) articles: rl_data_generator uses sequential IDs 0,1,2,3
# and writes to test_episodes/ rather than episodes/
_TEST_EPISODE_ROUNDS: dict[int, int] = {0: 0, 1: 1, 2: 2, 3: 3}
_TEST_ARM_PRESETS: dict[str, list[int]] = {
    "skip":     [0],  # 0 rounds
    "light":    [1],  # 1 round
    "standard": [2],  # 2 rounds
    "deep":     [3],  # 3 rounds
}
_ARM_ROUNDS: dict[str, int] = {"skip": 0, "light": 1, "standard": 2, "deep": 3}
_ARM_ORDER = ["skip", "light", "standard", "deep"]

# Empirically-measured exploration-effort units per arm (H0, shipped 2026-07-25,
# see run13_rl_grok_pipeline_analysis.md Part 7). Replaces the ordinal round
# count (_ARM_ROUNDS, {0,1,2,3}) as the cost term's per-arm multiplier.
# analyze_empirical_cost.py measured each arm's REAL exploration-phase query+
# scrape activity (from each arm's own separately-run episode's
# .research/full_queries.md + url_phases.json, corpus-wide n=42 articles):
# light=4.83, standard=9.07, deep=11.14 (mean explore_effort) -- i.e. deep's
# real activity is only 2.31x light's (not the 3.00x its old nr=3 assumption
# charged it for); standard is 1.88x (not 2.00x). Data-derived recalibration
# of what "rounds" means for cost -- cost_coef itself (-0.06) is unchanged.
_ARM_COST_UNITS: dict[str, float] = {"skip": 0.0, "light": 1.00, "standard": 1.88, "deep": 2.31}

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

# Diagnostic-only dims (not used by the reward formula) captured alongside
# _REWARD_DIMS for the C2 gate_diagnostics metadata -- see Part 7 S56/S57.
_DIAG_DIMS = ["user_intent_golden_source_priority"]  # gsp

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


def _parse_enhancement_tag(reason_text: str) -> tuple[int, list[str]] | None:
    """Extract the ``[instances=N; quality=tier1,tier2,...]`` tag from a
    depth_enhancement/breadth_enhancement reason string.

    Returns ``None`` when the tag is absent -- i.e. for reasoning.json files
    graded before this tag was introduced. Callers MUST treat ``None`` as "use
    the raw binary score directly, do not run enhancement_credit()" rather than
    guessing a count/quality: a legacy score=1 could represent anywhere from 1
    to 6 real instances, and silently assuming "1 standard instance" would
    quietly shrink credit for likely-multi-instance sections that were simply
    never re-examined, corrupting un-migrated oracle values as a side effect of
    this change. Un-migrated articles keep their exact pre-v3 numeric behaviour
    until they are actually re-graded and the tag becomes present.
    """
    m = re.search(r"\[instances=(\d+)(?:;\s*quality=([\w,]+))?\]", reason_text)
    if not m:
        return None
    count = int(m.group(1))
    quality_str = m.group(2)
    qualities = [q.strip() for q in quality_str.split(",")] if quality_str else []
    if count > 0 and not qualities:
        # Tag present but no quality list (shouldn't normally happen) -- assume standard.
        qualities = ["standard"] * min(count, 5)
    return (count, qualities)


def _parse_sections_ordered(text: str) -> list[tuple[str, str, int, tuple[int, list[str]] | None]]:
    """Parse per-section binary scores from one reasoning.json dimension value.

    Each block is separated by a blank line and formatted as:
        Title (may contain colons):\n**[0|1]:** [instances=N; quality=...] reasoning text

    The ``[instances=...]`` tag is only present for depth_enhancement/
    breadth_enhancement entries (see writing_workflow's new_follows_gt prompts);
    other dimensions and legacy (pre-tag) reasoning.json files simply won't match
    it -- the 4th tuple element is ``None`` in that case (see
    _parse_enhancement_tag for why this must NOT be silently defaulted).

    Returns list of (raw_title, norm_title, score, enhancement_or_None) in order of
    appearance. Skips non-content sections (References etc.).
    """
    results: list[tuple[str, str, int, tuple[int, list[str]] | None]] = []
    for part in text.split("\n\n"):
        part = part.strip()
        if not part:
            continue
        # Lazy match so it captures up to the LAST ":\n" before "**[01]:**"; the
        # remainder (reason text, possibly with the enhancement tag) is captured too.
        m = re.match(r"^(.+?):\n\*\*([01]):\*\*(.*)$", part, re.DOTALL)
        if m:
            raw = m.group(1).strip()
            if _is_non_content(raw):
                continue
            score = int(m.group(2))
            reason_text = m.group(3)
            enhancement = _parse_enhancement_tag(reason_text)
            results.append((raw, _normalize(raw), score, enhancement))
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
    dim_entries: list[tuple[str, str, int, tuple[int, list[str]] | None]],  # (raw, norm, score, enhancement) ordered
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
    by_norm = {norm: score for _, norm, score, _enh in dim_entries}

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


def _get_enhancement(
    dim_entries: list[tuple[str, str, int, tuple[int, list[str]] | None]],  # (raw, norm, score, enhancement) ordered
    target_norm: str,
    ordinal_idx: int,
) -> tuple[int, list[str]] | None:
    """Look up a section's (count, qualities) enhancement tag for a depth/breadth dimension.

    Same 3-tier lookup strategy as _get_score (exact -> substring -> ordinal),
    but returns the parsed ``(count, qualities)`` tuple (or ``None`` if the
    section wasn't found at all, or the tag was absent -- legacy data) for use
    with enhancement_reward.enhancement_credit(). Callers MUST fall back to the
    raw binary score (via _get_score) when this returns ``None`` rather than
    guessing a count -- see _parse_enhancement_tag for why.
    """
    by_norm = {norm: (score, enh) for _, norm, score, enh in dim_entries}

    if target_norm in by_norm:
        return by_norm[target_norm][1]

    for norm, (_score, enh) in by_norm.items():
        if target_norm in norm or norm in target_norm:
            return enh

    if ordinal_idx < len(dim_entries):
        return dim_entries[ordinal_idx][3]

    return None


# ---------------------------------------------------------------------------
# Reward formula (mirrors _compute_episode_reward in train_grpo.py)
# ---------------------------------------------------------------------------

def _ga_gate_penalty(ga: float) -> float:
    """Soft satisficing gate for guideline_adherence (C2, shipped 2026-07-29):
    a flat penalty on failure, replacing the old additive (0.50*ga+0.50*ra)*0.30
    term whose raw signal was ~97% noise -- see run13_rl_grok_pipeline_analysis.md
    Part 7 S53.6 F2 / S54."""
    return -0.10 if ga < 0.5 else 0.0


def _section_reward(
    cc: float, fl: float, de: float, be: float,
    cp: float, ga: float, ra: float,
    nr: float,
    variant: str,
) -> float:
    """Compute section-level reward with a UNIFIED formula (Formula "B", C2-revised).

    ``nr`` is the arm's cost-term multiplier. As of 2026-07-25 (H0, see
    run13_rl_grok_pipeline_analysis.md Part 7) callers pass
    _ARM_COST_UNITS[arm] (empirically-measured exploration effort, e.g.
    deep=2.31) rather than the raw ordinal round count (0/1/2/3) -- the name
    ``nr`` ("num rounds") is now a historical misnomer kept for call-site
    compatibility; it is just "the cost term's per-arm unit count".

    Historically this branched on ``variant`` (minimal/standard/demanding)
    with a 5x swing in explore-weight (0.10/0.30/0.50) and a cheaper
    per-round cost for demanding (-0.03 vs -0.05). That branching was a
    confound: build_rl_input strips the variant/policy tag from what the
    section-level RL model actually sees, so GRPO's reward target changed
    for a signal invisible to the model's input, teaching it to associate
    escalation value with the ``demanding`` guideline fingerprint rather
    than with genuine per-section gap signals (see reward-formula
    deconfounding investigation, 2026-07-08).

    Formula B (this one) removes the branch entirely and widens the
    explore/cost coefficients relative to the old 'standard' branch:
      - Section-level: nearly triples var_minimal's genuine standard/deep
        share (7%->18%) without hurting var_demanding (49%->46%).
      - Near-tie rate (arms within 0.06 of the best) drops 56%->41%,
        approaching the ~37% floor set by grading-resolution (cost-only
        ties where the top-2 arms have identical binary grades and differ
        only by the deterministic cost term -- unfixable by any formula).
      - GRPO's actual training signal (normalized advantage =
        regret/max(std, sigma_floor)) is UNCHANGED overall (1.23->1.29) and
        IMPROVES for the standard/deep classes specifically (1.22->1.31).
      - Article-level oracle labels barely move: 1/40 flips across the full
        train+test corpus (an escalation, not a loss), vs. 3/24 flips and a
        halved P3 count under the plain-'standard'-for-all alternative.

    ``variant`` is accepted for call-site compatibility (process_article_variant
    still passes it) but is no longer used to select a formula branch.

    ``de``/``be`` (as of section_oracle.json version 3) are no longer raw 0/1
    grader scores -- callers pass them through
    ``enhancement_reward.enhancement_credit()`` first, so they are saturating
    credit values in [0, 1] driven by the count and quality of qualifying
    depth/breadth instances (see enhancement_reward.py). The formula's own math
    is unchanged; it is agnostic to whether de/be are binary or fractional.

    C2 UPDATE (2026-07-29, Part 7 S53-57): ``ra`` removed from the reward
    entirely (96.8% constant corpus-wide, ~2% of arm-separating signal;
    kept as a parameter only for call-site compatibility). ``ga`` demoted
    from an additive weight to the soft gate ``_ga_gate_penalty()`` (its raw
    signal was ~97% noise relative to arm choice, S53.6 F2). Freed weight
    reallocated to de/be. ``cost_coef`` reverted -0.02 -> -0.03 (deep-scarcity
    representation only recovers at -0.03 or smaller, S54.7).
    """
    gt_base = 0.20 * cc + 0.20 * fl
    explore = cp * (0.45 * de + 0.30 * be)
    cost    = -0.03 * nr  # cost_coef: -0.06->-0.045->-0.03->-0.02 (2026-07-26) -> -0.03 (2026-07-29, C2 ship)
    return gt_base + explore + _ga_gate_penalty(ga) + cost


def _section_reward_components(
    cc: float, fl: float, de: float, be: float,
    cp: float, ga: float, ra: float,
    nr: float,
    variant: str,
) -> tuple[float, float]:
    """Same formula as _section_reward(), but returns (rest, explore) separately
    instead of their sum -- ``rest + explore == _section_reward(...)`` exactly.

    Exists so callers that need to aggregate the ``explore`` term differently
    from the rest (see section_oracle.json version 4 / compute_article_oracle.py's
    _compute_r_w()) don't have to duplicate the formula. ``_section_reward()``
    itself is UNCHANGED and still returns a single float -- existing callers
    (measure_replicate_noise.py, sweep_reward_formula.py's inline copy) are
    unaffected by this addition.

    Motivation: a genuinely valuable enhancement instance shouldn't count for
    more or less just because the section it landed in happens to have a large
    or small ``target_words`` budget -- see run13_rl_grok_pipeline_analysis.md
    Part 5 for the real-corpus case (13_agent_framework) that surfaced this:
    `deep`'s enhancement instances were spread thin across many sections while
    `standard` concentrated 3 instances into one heavily-weighted section,
    letting `standard` win on weight alone despite `deep` touching more content.

    See _section_reward()'s C2 UPDATE docstring note for the 2026-07-29 formula
    revision (ra removed, ga soft-gated, cost_coef -0.03) -- identical here.
    """
    gt_base = 0.20 * cc + 0.20 * fl
    explore = cp * (0.45 * de + 0.30 * be)
    cost    = -0.03 * nr  # cost_coef: -0.06->-0.045->-0.03->-0.02 (2026-07-26) -> -0.03 (2026-07-29, C2 ship)
    rest = gt_base + _ga_gate_penalty(ga) + cost
    return rest, explore


# ---------------------------------------------------------------------------
# Per-episode loading
# ---------------------------------------------------------------------------

def _load_episode(episode_dir: Path) -> dict[str, list[tuple[str, str, int, tuple[int, list[str]] | None]]]:
    """Load reasoning.json (or reasons.json) and return {dim: [(raw, norm, score, enhancement), ...]}."""
    path = episode_dir / "reasoning.json"
    if not path.exists():
        path = episode_dir / "reasons.json"  # test-set grader writes reasons.json
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        log.warning("  Malformed %s in %s (%s); skipping episode.", path.name, episode_dir.name, exc)
        return {}
    return {
        dim: _parse_sections_ordered(data[dim])
        for dim in _REWARD_DIMS + _DIAG_DIMS
        if dim in data
    }


# ---------------------------------------------------------------------------
# Core processing
# ---------------------------------------------------------------------------

def _count_reasoning_sections(episode_dir: Path) -> int:
    """Count distinct content sections in one preset's reasoning/reasons file."""
    path = episode_dir / "reasoning.json"
    if not path.exists():
        path = episode_dir / "reasons.json"
    if not path.exists():
        return 0
    data = json.loads(path.read_text(encoding="utf-8"))
    ref = data.get("ground_truth_core_content", "")
    return len(_parse_sections_ordered(ref))


def process_article_variant(
    article: str,
    variant: str | None,
    dry_run: bool = False,
    return_data: bool = False,
) -> bool | tuple[bool, dict | None]:
    """Derive and write the section oracle for one (article, variant) pair.

    Pass ``variant=None`` for no-variant (test-set) articles whose bases and
    episode directories carry no variant suffix, e.g.
    ``bases/<article>/`` and ``episodes/<article>__preset{p}/``.
    The reward formula will use the ``'standard'`` variant in that case.

    ``return_data=True`` returns ``(ok, sections_output)`` instead of just
    ``ok`` -- ``sections_output`` is ``None`` on failure. Used by
    verify_oracle_reproducibility.py to recompute via this EXACT code path
    (not a parallel re-implementation) and diff against the stored file.
    """
    no_variant = variant is None
    art_var = article if no_variant else f"{article}__{variant}"
    bases_dir = _BASES_DIR / art_var

    if not bases_dir.exists():
        log.warning("  Bases dir missing: %s", art_var)
        return (False, None) if return_data else False

    # Determine the digest to use for sec_id extraction.
    # Some variant digests were truncated during generation (section_coverage has
    # fewer entries than the article actually has).  When that happens, fall back
    # to the base (non-variant) directory, which has the complete coverage block.
    # (No-variant articles are already in the base directory; skip fallback.)
    digest_path = bases_dir / "research_digest.md"
    if not digest_path.exists():
        log.warning("  No digest: %s", art_var)
        return (False, None) if return_data else False

    digest = digest_path.read_text(encoding="utf-8")
    sec_ids = _extract_sec_ids_ordered(digest)

    # Check completeness against the episode's reasoning/reasons file
    if no_variant:
        # No-variant articles are normally genuine test-set articles living
        # under test_episodes/ with sequential IDs 0-3. However, one-off
        # ablation variants (e.g. "..._var_goldremoved") don't match any of
        # the three named _VARIANTS, so they fall into this same no_variant
        # branch by construction -- but their episodes actually live under
        # the main episodes/ dir (same "{article}__presetN" naming, same 0-3
        # preset numbering as the test-set scheme). Detect which root
        # actually holds this article's episodes instead of assuming
        # test_episodes/, otherwise every episode dir "goes missing" and the
        # oracle silently degrades to an all-skip, cost-only reward.
        if (_EPISODES_DIR / f"{article}__preset0").exists() and not (
            _TEST_EPISODES_DIR / f"{article}__preset0"
        ).exists():
            _ep_root = _EPISODES_DIR
        else:
            _ep_root = _TEST_EPISODES_DIR
    else:
        _ep_root = _EPISODES_DIR
    ep0_dir = _ep_root / f"{article}__preset0" if no_variant else _ep_root / f"{art_var}__preset0"
    expected_n = _count_reasoning_sections(ep0_dir) if ep0_dir.exists() else len(sec_ids)

    if len(sec_ids) < expected_n and not no_variant:
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
        return (False, None) if return_data else False

    sec_norms = [_sec_id_to_norm(sid) for sid in sec_ids]

    # Select preset map and episodes root based on variant mode
    if no_variant:
        _ep_rounds = _TEST_EPISODE_ROUNDS   # {0:0, 1:1, 2:2, 3:3}
        _arm_presets = _TEST_ARM_PRESETS    # skip→0, light→1, standard→2, deep→3
    else:
        _ep_rounds = _EPISODE_ROUNDS        # {0:0, 1:1, 3:2, 5:3}
        _arm_presets = _ARM_PRESETS         # skip→0, light→1, standard→3, deep→5
    _ACTIVE_PRESETS = sorted(_ep_rounds.keys())
    # preset id -> arm name, so the cost term can use _ARM_COST_UNITS (empirical
    # effort) instead of _ep_rounds (ordinal round count) -- see H0, Part 7.
    _preset_to_arm = {pid: arm for arm, ids in _arm_presets.items() for pid in ids}

    # Load only the active episodes upfront (dict keyed by preset id)
    episode_dims: dict[int, dict[str, list[tuple[str, str, int, tuple[int, list[str]] | None]]]] = {}
    for p in _ACTIVE_PRESETS:
        ep_dir = (
            _ep_root / f"{article}__preset{p}"
            if no_variant
            else _EPISODES_DIR / f"{art_var}__preset{p}"
        )
        if not ep_dir.exists():
            log.warning("  Missing episode dir: %s__preset%d", art_var, p)
            episode_dims[p] = {}
        else:
            episode_dims[p] = _load_episode(ep_dir)

    # Determine the variant short name for the reward formula.
    # No-variant (test-set) articles use 'standard' as the default formula.
    variant_short = "standard" if no_variant else variant.replace("var_", "")

    # For each section, compute per-arm rewards from the 4 active presets
    sections_output: dict[str, dict] = {}

    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        # Per-active-preset reward
        preset_rewards: dict[int, float] = {}
        preset_explore: dict[int, float] = {}
        preset_diag: dict[int, dict[str, float]] = {}
        for p in _ACTIVE_PRESETS:
            ep = episode_dims[p]
            nr = _ARM_COST_UNITS[_preset_to_arm[p]]

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return _get_score(_ep.get(dim, []), _sn, _si)

            def _enh_credit(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                """Enhancement credit for a depth/breadth dim: real (count, qualities)
                tag -> enhancement_credit() curve; tag absent (legacy, un-migrated
                reasoning.json) -> raw binary score, UNCHANGED from pre-v3 behaviour.
                """
                enh = _get_enhancement(_ep.get(dim, []), _sn, _si)
                if enh is None:
                    return _get_score(_ep.get(dim, []), _sn, _si)
                _count, qualities = enh
                return enhancement_credit(qualities)

            cp_val = _score("ground_truth_core_preservation")
            ra_val = _score("user_intent_research_anchoring")
            gsp_val = _score("user_intent_golden_source_priority")

            rest, explore = _section_reward_components(
                cc=_score("ground_truth_core_content"),
                fl=_score("ground_truth_flow"),
                de=_enh_credit("ground_truth_depth_enhancement"),
                be=_enh_credit("ground_truth_breadth_enhancement"),
                cp=cp_val,
                ga=_score("user_intent_guideline_adherence"),
                ra=ra_val,
                nr=nr,
                variant=variant_short,
            )
            preset_rewards[p] = rest + explore
            preset_explore[p] = explore
            preset_diag[p] = {"cp": cp_val, "ra": ra_val, "gsp": gsp_val}

        # Map active presets → 4 arms (each arm now maps to exactly one preset).
        # Pick the SAME winning preset for the combined reward, its explore
        # component, and its diagnostics, so all three always correspond to
        # the arm's actual chosen preset, not an independently-maxed value.
        arm_rewards: dict[str, float] = {}
        arm_explore: dict[str, float] = {}
        arm_diag: dict[str, dict[str, float]] = {}
        for arm, preset_ids in _arm_presets.items():
            best_p = max(preset_ids, key=lambda p: preset_rewards[p])
            arm_rewards[arm] = preset_rewards[best_p]
            arm_explore[arm] = preset_explore[best_p]
            arm_diag[arm] = preset_diag[best_p]
        oracle = max(_ARM_ORDER, key=arm_rewards.__getitem__)

        sections_output[sec_id] = {
            "oracle": oracle,
            "rewards": {k: round(arm_rewards[k], 6) for k in _ARM_ORDER},
            "explore": {k: round(arm_explore[k], 6) for k in _ARM_ORDER},
            "diagnostics": {
                k: {m: round(v, 6) for m, v in arm_diag[k].items()} for k in _ARM_ORDER
            },
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
        return (True, sections_output) if return_data else True

    # Write section_oracle.json (version 5 format -- adds a "diagnostics" dict
    # per section holding the raw (not reward-weighted) cp/ra/gsp satisficing
    # metrics per arm, for compute_article_oracle.py's gate_diagnostics/
    # low_signal_flag (informational only, does not affect oracle_arm -- see
    # Part 7 S56/S57). Version 4's "rewards"/"explore" fields are unchanged;
    # versions 2/3 (no "explore") remain readable via compute_article_oracle.py's
    # existing fallback.
    output = {
        "version": 5,
        "article": article,
        "variant": variant if variant is not None else "no_variant",
        "sections": sections_output,
        # Legacy 'presets' field kept for backward compat with any code that
        # reads the old format before load_section_groups is updated.
        "presets": {sid: info["oracle"] for sid, info in sections_output.items()},
    }
    oracle_path = bases_dir / "section_oracle.json"
    oracle_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    return (True, sections_output) if return_data else True


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
    parser.add_argument(
        "--bases-dir",
        type=Path,
        default=None,
        help=(
            "Override the bases root to read episodes/write section_oracle.json "
            "into (default: production rl_training_data/bases/). Use a separate "
            "directory (pre-populated with the same research_digest.md/"
            "guideline_features.json) when experimenting so production bases/ "
            "is never touched."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    articles = args.articles if args.articles else _ALL_ARTICLES

    if args.bases_dir is not None:
        global _BASES_DIR
        _BASES_DIR = args.bases_dir

    log.info("=== generate_episode_oracles  dry_run=%s ===", args.dry_run)
    log.info("Episodes dir: %s", _EPISODES_DIR)
    log.info("Bases dir:    %s", _BASES_DIR)
    log.info("Articles: %s", articles)
    log.info("Variants: %s", args.variants)

    ok = fail = 0
    for article in articles:
        # Detect no-variant (test-set) articles: bases/<article>/ exists but no
        # bases/<article>__var_*/ directories exist for any of the 3 variants.
        has_variant_dirs = any(
            (_BASES_DIR / f"{article}__{v}").exists() for v in _VARIANTS
        )
        if has_variant_dirs:
            variants_to_run: list[str | None] = [
                v for v in args.variants if (_BASES_DIR / f"{article}__{v}").exists()
            ]
        else:
            log.info(
                "  %s: no variant directories found — processing as no-variant article",
                article,
            )
            variants_to_run = [None]

        for variant in variants_to_run:
            if variant is not None:
                log.info("Processing %s__%s", article, variant)
            else:
                log.info("Processing %s (no-variant)", article)
            if process_article_variant(article, variant, dry_run=args.dry_run):
                ok += 1
            else:
                fail += 1

    log.info("Done: %d OK, %d failed", ok, fail)
    return 0 if fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
