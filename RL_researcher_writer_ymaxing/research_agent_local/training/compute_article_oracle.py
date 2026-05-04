"""Compute article-level oracles using per-section rewards weighted by guideline
target word counts, and save the full breakdown to disk.

For each of the 21 article-variants, a file is written to:
    rl_training_data/bases/{article}/article_oracle.json

The oracle is the preset p* that maximises the article-level reward:

    R_article(p) = Σ_s  weight(s) × R_section(s, p) / Σ_s weight(s)

where:
  - weight(s) = guideline "Section length: N words" target (preferred), or the
    digest section's word count when no target annotation is present.
  - R_section(s, p) is computed from per-section binary scores in reasoning.json
    using the variant-conditioned reward formula (identical to train_grpo.py).

Using fixed guideline-target weights (rather than digest word counts or model
confidence) keeps the oracle stable across presets and matched to intended
article proportions.

Design notes
------------
* The article oracle must NOT include model-confidence weights (those are an
  inference heuristic, not a property of article utility).
* The article oracle and inference aggregation should use the same *base*
  section-importance weights (guideline targets).  At inference, an extra
  confidence factor down-weights sections where the model is near-uniform;
  the oracle deliberately omits this factor so it reflects true article utility
  regardless of which model checkpoint is being evaluated.
* Binary-scored dimensions (reasoning.json) give section rewards in {0, 0.xx};
  near-tie margins in the article-reward space therefore carry noise.  The
  saved ``margin`` field makes this visible to callers.

Constants that must stay in sync with train_grpo.py
----------------------------------------------------
  ARTICLES, PRESET_ROUNDS, NUM_PRESETS, _REWARD_DIMS, compute_reward()

Usage (from research_agent_local/training/):
  uv run python compute_article_oracle.py              # all 21 article-variants
  uv run python compute_article_oracle.py \\
      --article 09_RAG__var_demanding                  # one article
  uv run python compute_article_oracle.py --dry-run    # print only, no writes
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent               # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent              # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_GUIDELINE_DIR = (
    _REPO_ROOT / "writing_workflow" / "inputs" / "evals" / "dataset" / "data"
)

# ---------------------------------------------------------------------------
# Constants — must stay in sync with train_grpo.py
# ---------------------------------------------------------------------------
ARTICLES = [
    "02_workflows_vs_agents__var_minimal",
    "02_workflows_vs_agents__var_standard",
    "02_workflows_vs_agents__var_demanding",
    "03_context_engineering__var_minimal",
    "03_context_engineering__var_standard",
    "03_context_engineering__var_demanding",
    "05_workflow_patterns__var_minimal",
    "05_workflow_patterns__var_standard",
    "05_workflow_patterns__var_demanding",
    "06_tools__var_minimal",
    "06_tools__var_standard",
    "06_tools__var_demanding",
    "08_react_practice__var_minimal",
    "08_react_practice__var_standard",
    "08_react_practice__var_demanding",
    "09_RAG__var_minimal",
    "09_RAG__var_standard",
    "09_RAG__var_demanding",
    "11_multimodal__var_minimal",
    "11_multimodal__var_standard",
    "11_multimodal__var_demanding",
]

PRESET_ROUNDS: dict[int, int] = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
NUM_PRESETS = 6
PRESET_NAMES: dict[int, str] = {
    0: "P0_baseline",
    1: "P1_single_balanced",
    2: "P2_balanced_depth",
    3: "P3_depth_breadth",
    4: "P4_bal_depth_breadth",
    5: "P5_depth_breadth_depth",
}

_REWARD_DIMS = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
]


def _article_variant_level(article: str) -> str:
    if "__var_minimal" in article:
        return "minimal"
    if "__var_demanding" in article:
        return "demanding"
    return "standard"


# ---------------------------------------------------------------------------
# Reward formula — must stay in sync with train_grpo.py
# ---------------------------------------------------------------------------
def compute_reward(
    scores: dict,
    preset_id: int,
    variant_level: str = "standard",
) -> float:
    """Variant-conditioned reward formula.  Identical to train_grpo.compute_reward."""
    cc = scores["ground_truth_core_content"]
    fl = scores["ground_truth_flow"]
    de = scores["ground_truth_depth_enhancement"]
    be = scores["ground_truth_breadth_enhancement"]
    cp = scores["ground_truth_core_preservation"]
    ga = scores["user_intent_guideline_adherence"]
    ra = scores["user_intent_research_anchoring"]
    nr = PRESET_ROUNDS[preset_id]

    if variant_level == "minimal":
        gt_base     = 0.05 * cc + 0.05 * fl
        explore     = 0.0
        user_intent = 0.80 * ga + 0.10 * ra
        cost        = -0.02 * nr
    elif variant_level == "demanding":
        # Quarter cost: at -0.01/round, cost overwhelms explore gains at P5.
        gt_base     = 0.12 * cc + 0.08 * fl
        explore     = cp * (0.55 * de + 0.35 * be) * 0.50
        user_intent = (0.60 * ga + 0.40 * ra) * 0.25
        cost        = -0.005 * nr
    else:  # "standard"
        gt_base     = 0.20 * cc + 0.20 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.30
        user_intent = (0.50 * ga + 0.50 * ra) * 0.30
        cost        = -0.02 * nr

    return gt_base + explore + user_intent + cost


# ---------------------------------------------------------------------------
# Parsing helpers — must stay in sync with train_grpo.py
# ---------------------------------------------------------------------------
def _parse_reasoning_sections(text: str) -> dict[str, int]:
    """Parse per-section binary scores from a reasoning.json dimension value."""
    sections: dict[str, int] = {}
    for part in text.split("\n\n"):
        part = part.strip()
        if not part:
            continue
        m = re.match(r'^(.+?):\s*\n\*\*(\d):\*\*', part)
        if m:
            sections[m.group(1).strip()] = int(m.group(2))
    return sections


def _extract_digest_sections(digest: str) -> list[tuple[str, str]]:
    """Extract (title, excerpt) pairs from the Per-Section Coverage Analysis."""
    pattern = r'^### S(\d+) — (.+)$'
    matches = list(re.finditer(pattern, digest, re.MULTILINE))
    sections: list[tuple[str, str]] = []
    for i, m in enumerate(matches):
        title = m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(digest)
        excerpt = digest[start:end].strip()
        gap_idx = excerpt.find('\n## 3.')
        if gap_idx != -1:
            excerpt = excerpt[:gap_idx].strip()
        sections.append((title, excerpt))
    return sections


def _match_reasoning_to_digest(
    reasoning_name: str,
    digest_sections: list[tuple[str, str]],
) -> int | None:
    """Three-pass fuzzy match: exact → substring → stripped."""
    rn_lower = reasoning_name.lower().strip()
    for i, (title, _) in enumerate(digest_sections):
        if title.lower() == rn_lower:
            return i
    for i, (title, _) in enumerate(digest_sections):
        tl = title.lower()
        if rn_lower in tl or tl in rn_lower:
            return i
    rn_norm = re.sub(r'^the\s+', '', rn_lower).replace(',', '')
    for i, (title, _) in enumerate(digest_sections):
        tl_norm = re.sub(r'^the\s+', '', title.lower()).replace(',', '')
        if rn_norm in tl_norm or tl_norm in rn_norm:
            return i
    return None


# ---------------------------------------------------------------------------
# Section target length extraction
# ---------------------------------------------------------------------------
# Handles all formatting variants found across guideline files:
#   - "**Section length:** ~150 words"  (colon before closing **)
#   - "**Section length**: 650 words"   (colon after closing **)
#   - "**Section length**: 1,200 words" (comma thousands-separator)
# Multiple matches in one section block (sub-sections) are summed.
_SECTION_LEN_RE = re.compile(
    r'\*\*Section length[^:]*:\*\*?\s*~?([\d,]+)\s*words',
    re.IGNORECASE,
)


def _extract_section_target_lengths(
    guideline: str,
    n_sections: int,
) -> list[int | None]:
    """Return per-section target word counts from article_guideline.md.

    Splits the guideline by ``## Section N`` headers, then searches each block
    for the ``**Section length:** N words`` annotation (and format variants).

    When multiple length annotations appear in one block (a section with
    explicit sub-section budgets), their values are summed.

    Returns a list of length ``n_sections``.  Entries are ``int`` when a target
    was found; ``None`` when absent (callers use digest word count as fallback).
    """
    header_re = re.compile(r'^## Section \d+ ?[-:] ?', re.MULTILINE)
    splits = list(header_re.finditer(guideline))
    if not splits:
        return [None] * n_sections

    result: list[int | None] = [None] * n_sections
    for i, m in enumerate(splits):
        if i >= n_sections:
            break
        start = m.start()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(guideline)
        block = guideline[start:end]
        hits = _SECTION_LEN_RE.findall(block)
        if hits:
            # Strip comma thousands-separators and sum subsection budgets.
            result[i] = sum(int(h.replace(',', '')) for h in hits)
    return result


# ---------------------------------------------------------------------------
# Oracle computation
# ---------------------------------------------------------------------------
def compute_article_oracle(article: str) -> dict:
    """Compute the full article-level oracle for one article-variant.

    Returns a dict ready for JSON serialisation with the following top-level
    fields (see schema below) and a per-section breakdown.

    Schema
    ------
    article                       str   — e.g. "09_RAG__var_demanding"
    variant_level                 str   — "minimal" | "standard" | "demanding"
    computed_at                   str   — ISO 8601 UTC timestamp
    oracle_preset                 int   — argmax_p R_article(p)
    oracle_preset_name            str   — human-readable preset label
    runner_up_preset              int   — second-best preset by article reward
    runner_up_preset_name         str
    margin                        float — oracle_reward − runner_up_reward
    reward_spread                 float — max − min over all 6 presets
    article_rewards               list  — [R_article(p) for p in 0..5]
    oracle_ranking                list  — preset indices sorted desc by reward
    aggregation_scheme            str   — 'guideline_target_lengths' | 'digest_word_counts' | 'mixed_N_of_M_from_guideline'
    n_sections                    int
    n_sections_with_target        int   — sections where guideline length was found
    total_target_words            int   — sum of effective weights

    sections[]:
      index                       int   — 1-based
      title                       str
      target_words                int|null — from guideline (null = not annotated)
      weight_words                int   — effective weight (target or digest fallback)
      weight_frac                 float — fraction of total article weight
      digest_words                int   — digest excerpt word count (always present)
      rewards_by_preset           list  — [R_section(s, p) for p in 0..5]
      raw_scores_by_preset        list  — [{dim: score} for p in 0..5]
      section_oracle              int   — argmax_p R_section(s, p)
      section_runner_up           int   — second-best preset for this section
      section_margin              float — oracle_reward − runner_up reward (section)
    """
    variant_level = _article_variant_level(article)

    # Load digest and split into sections
    digest = (_BASES_DIR / article / "research_digest.md").read_text(encoding="utf-8")
    digest_sections = _extract_digest_sections(digest)
    n = len(digest_sections)
    if n == 0:
        raise ValueError(f"No sections found in digest for '{article}'")

    # Load guideline target lengths (partially or fully None when absent)
    guideline_path = _GUIDELINE_DIR / article / "article_guideline.md"
    target_lengths: list[int | None] = [None] * n
    if guideline_path.exists():
        guideline_text = guideline_path.read_text(encoding="utf-8")
        target_lengths = _extract_section_target_lengths(guideline_text, n)
    else:
        print(f"  WARNING: guideline not found at {guideline_path}", file=sys.stderr)

    # Build per-section, per-preset raw scores from reasoning.json.
    # section_raw[sec_idx][preset_id] = {dim: float}
    section_raw: list[list[dict[str, float]]] = [
        [{} for _ in range(NUM_PRESETS)] for _ in range(n)
    ]
    for p in range(NUM_PRESETS):
        ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
        reasons = json.loads(
            (ep_dir / "reasoning.json").read_text(encoding="utf-8")
        )
        for sec_idx in range(n):
            scores_dict: dict[str, float] = {}
            for dim in _REWARD_DIMS:
                if dim not in reasons:
                    scores_dict[dim] = 0.0
                    continue
                dim_sections = _parse_reasoning_sections(reasons[dim])
                matched: int | None = None
                for rname, rscore in dim_sections.items():
                    idx = _match_reasoning_to_digest(rname, digest_sections)
                    if idx == sec_idx:
                        matched = rscore
                        break
                scores_dict[dim] = float(matched if matched is not None else 0)
            section_raw[sec_idx][p] = scores_dict

    # Per-section rewards: section_rewards[sec_idx][preset_id] = float
    section_rewards: list[list[float]] = [
        [compute_reward(section_raw[s][p], p, variant_level) for p in range(NUM_PRESETS)]
        for s in range(n)
    ]

    # Effective section weights: guideline target, else digest word count
    digest_words = [max(len(exc.split()), 1) for _, exc in digest_sections]
    weight_words: list[int] = [
        target_lengths[s] if target_lengths[s] is not None else digest_words[s]
        for s in range(n)
    ]
    total_weight = sum(weight_words)
    weight_fracs = [w / total_weight for w in weight_words]

    # Article-level rewards: weighted average of section rewards
    article_rewards = [
        sum(weight_fracs[s] * section_rewards[s][p] for s in range(n))
        for p in range(NUM_PRESETS)
    ]

    # Oracle, runner-up, margin, spread
    oracle_ranking = sorted(range(NUM_PRESETS), key=lambda p: article_rewards[p], reverse=True)
    oracle_preset   = oracle_ranking[0]
    runner_up_preset = oracle_ranking[1]
    margin       = article_rewards[oracle_preset] - article_rewards[runner_up_preset]
    reward_spread = article_rewards[oracle_preset] - article_rewards[oracle_ranking[-1]]

    # Aggregation scheme label
    n_with_target = sum(1 for tl in target_lengths if tl is not None)
    if n_with_target == n:
        aggregation_scheme = "guideline_target_lengths"
    elif n_with_target == 0:
        aggregation_scheme = "digest_word_counts"
    else:
        aggregation_scheme = f"mixed_{n_with_target}_of_{n}_from_guideline"

    # Per-section detail records
    sections_out = []
    for s, (title, _) in enumerate(digest_sections):
        sec_ranking = sorted(
            range(NUM_PRESETS), key=lambda p: section_rewards[s][p], reverse=True
        )
        sec_oracle     = sec_ranking[0]
        sec_runner_up  = sec_ranking[1]
        sec_margin = section_rewards[s][sec_oracle] - section_rewards[s][sec_runner_up]
        sections_out.append({
            "index": s + 1,
            "title": title,
            "target_words": target_lengths[s],
            "weight_words": weight_words[s],
            "weight_frac": round(weight_fracs[s], 5),
            "digest_words": digest_words[s],
            "rewards_by_preset": [round(r, 6) for r in section_rewards[s]],
            "raw_scores_by_preset": [section_raw[s][p] for p in range(NUM_PRESETS)],
            "section_oracle": sec_oracle,
            "section_runner_up": sec_runner_up,
            "section_margin": round(sec_margin, 6),
        })

    return {
        "article": article,
        "variant_level": variant_level,
        "computed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "oracle_preset": oracle_preset,
        "oracle_preset_name": PRESET_NAMES[oracle_preset],
        "runner_up_preset": runner_up_preset,
        "runner_up_preset_name": PRESET_NAMES[runner_up_preset],
        "margin": round(margin, 6),
        "reward_spread": round(reward_spread, 6),
        "article_rewards": [round(r, 6) for r in article_rewards],
        "oracle_ranking": oracle_ranking,
        "aggregation_scheme": aggregation_scheme,
        "n_sections": n,
        "n_sections_with_target": n_with_target,
        "total_target_words": total_weight,
        "sections": sections_out,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Compute article-level oracles (section-reward-weighted by guideline "
            "target lengths) and save to bases/{article}/article_oracle.json."
        )
    )
    parser.add_argument(
        "--article",
        type=str,
        default=None,
        help="Process only this article-variant (default: all 21).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print results to stdout; do not write any files.",
    )
    args = parser.parse_args()

    if args.article:
        if args.article not in ARTICLES:
            sys.exit(
                f"ERROR: unknown article '{args.article}'.\nValid choices:\n"
                + "\n".join(f"  {a}" for a in ARTICLES)
            )
        targets = [args.article]
    else:
        targets = ARTICLES

    print(
        f"Computing article-level oracles for {len(targets)} article-variant(s)...\n"
        f"  Aggregation: guideline target section lengths "
        f"(fallback: digest word counts)\n"
    )

    results = []
    for article in targets:
        print(f"  {article}...", end=" ", flush=True)
        data = compute_article_oracle(article)
        results.append(data)

        oracle_p   = data["oracle_preset"]
        runner_p   = data["runner_up_preset"]
        margin     = data["margin"]
        rewards    = data["article_rewards"]
        scheme     = data["aggregation_scheme"]
        n_tgt      = data["n_sections_with_target"]
        n_sec      = data["n_sections"]
        print(
            f"oracle=P{oracle_p} runner-up=P{runner_p} "
            f"margin={margin:.4f} "
            f"rewards={[f'{r:.3f}' for r in rewards]} "
            f"[{scheme}, {n_tgt}/{n_sec} sections with guideline target]"
        )

        if not args.dry_run:
            out_path = _BASES_DIR / article / "article_oracle.json"
            out_path.write_text(
                json.dumps(data, indent=2), encoding="utf-8"
            )
            print(f"    → saved: {out_path.relative_to(_REPO_ROOT)}")

    # Summary table
    col_w = max(len(d["article"]) for d in results) + 2
    print(f"\n{'Article':<{col_w}} {'Oracle':>7}  {'RunUp':>6}  {'Margin':>8}  {'Spread':>8}  {'Scheme'}")
    print("-" * (col_w + 50))
    for d in results:
        print(
            f"  {d['article']:<{col_w - 2}}  "
            f"P{d['oracle_preset']:>5}  "
            f"P{d['runner_up_preset']:>5}  "
            f"{d['margin']:>8.4f}  "
            f"{d['reward_spread']:>8.4f}  "
            f"{d['aggregation_scheme']}"
        )

    if not args.dry_run:
        print(f"\nSaved {len(results)} article_oracle.json file(s) under rl_training_data/bases/")


if __name__ == "__main__":
    main()
