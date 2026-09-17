"""Decompose deep/standard's user_intent shortfall into guideline_adherence (ga)
vs research_anchoring (ra), and root-cause ga failures using the grader's own
reasoning text -- mirrors analyze_cost_imbalance.py's methodology, applied to
the OTHER (much smaller, ~14% of the gap) component flagged there.

Motivation: Part 5 (run13_rl_grok_pipeline_analysis.md, "section-level binary
enhancement scoring" finding) hypothesized that guideline_adherence's hard
length-tolerance rule (+-10%, min +-25 words -- see
writing_workflow/src/brown/evals/metrics/new_user_intent/prompts.py) penalizes
deep/standard for the extra content their exploration adds, with no
corresponding credit-side protection. analyze_cost_imbalance.py's corpus-wide
decomposition already found user_intent contributes +0.0201 to deep's average
shortfall (vs cost's +0.1320) -- real but much smaller. This script checks
WHERE that +0.0201 actually comes from: ga vs ra, and specifically whether ga
failures are actually attributable to the length rule (not some other
guideline-adherence criterion) using the grader's own stated reasoning --
zero LLM calls, zero re-grading, reads only already-graded reasoning.json.

Usage (from research_agent_local/training/):
  python3 analyze_user_intent_gap.py
"""

from __future__ import annotations

import json
import re
from collections import Counter
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

import generate_episode_oracles as geo

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_TEST_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "test_episodes"

_TRAIN_TOPICS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_TRAIN_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI", "Bird_Eye_Extreme",
    "Dark_Dimension", "Distinct_AI_Models", "Earth_Oceans_Origin", "Gravity_Entropy",
    "HNSW", "Insects_Consciousness", "Space-Time_QECC", "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]
_MIXEDDEPTH = ["Distinct_AI_Models__mixeddepth", "Insects_Consciousness__mixeddepth"]
_ALL_42 = [f"{t}__{v}" for t in _TRAIN_TOPICS for v in _TRAIN_VARIANTS] + _TEST_ARTICLES + _MIXEDDEPTH

# Phrases indicating the grader's stated reason includes a LENGTH violation
# (over OR under tolerance) as (at least one) cause of a 0 score. Deliberately
# broad (recall-favoring) -- spot-check a sample of matches before trusting
# the aggregate rate.
_LENGTH_FAIL_RE = re.compile(
    r"(exceeds?\s+(?:the\s+)?(?:target|tolerance|word)|"
    r"outside\s+the\s+.*?tolerance|"
    r"falls?\s+(?:more\s+than\s+)?(?:below|short)|"
    r"(?:over|under)\s+the\s+\S+[\s-]word|"
    r"too\s+(?:long|short)|"
    r"word\s+count\s+violation|"
    r"length\s+violation|"
    r"violates?\s+the\s+.*?word)",
    re.IGNORECASE,
)
_LENGTH_MENTION_RE = re.compile(r"word count|word-count|words? tolerance|\bwords?\b.*tolerance", re.IGNORECASE)


def _parse_sections_with_reason(text: str) -> list[tuple[str, str, int, str]]:
    """Like geo._parse_sections_ordered but also returns the raw reason text."""
    results = []
    for part in text.split("\n\n"):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(.+?):\n\*\*([01]):\*\*(.*)$", part, re.DOTALL)
        if m:
            raw = m.group(1).strip()
            if geo._is_non_content(raw):
                continue
            score = int(m.group(2))
            reason = m.group(3).strip()
            results.append((raw, geo._normalize(raw), score, reason))
    return results


def _load_dim_with_reason(ep_dir: Path, dim: str) -> list[tuple[str, str, int, str]]:
    path = ep_dir / "reasoning.json"
    if not path.exists():
        path = ep_dir / "reasons.json"
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []
    if dim not in data:
        return []
    return _parse_sections_with_reason(data[dim])


def _get_reason(entries: list[tuple[str, str, int, str]], target_norm: str, ordinal_idx: int) -> tuple[int, str] | None:
    by_norm = {norm: (score, reason) for _, norm, score, reason in entries}
    if target_norm in by_norm:
        return by_norm[target_norm]
    for norm, (score, reason) in by_norm.items():
        if target_norm in norm or norm in target_norm:
            return (score, reason)
    if ordinal_idx < len(entries):
        e = entries[ordinal_idx]
        return (e[2], e[3])
    return None


def _ep_dir_for(article: str, arm: str) -> Path | None:
    is_var = "__var_" in article
    if is_var:
        preset = geo._ARM_PRESETS[arm][0]
        d = _EPISODES_DIR / f"{article}__preset{preset}"
    else:
        preset = geo._TEST_ARM_PRESETS[arm][0]
        d = _TEST_EPISODES_DIR / f"{article}__preset{preset}"
    return d if d.is_dir() else None


def main() -> None:
    # Part 1: corpus-wide ga vs ra decomposition (target-words-weighted, same
    # aggregation as _compute_r_w's "rest" treatment).
    acc_ga = {a: 0.0 for a in geo._ARM_ORDER}
    acc_ra = {a: 0.0 for a in geo._ARM_ORDER}
    total_w = 0

    # Part 2: ga=0 root-cause classification, restricted to DISAGREEMENT cases
    # that matter for the reward gap: sections where the article's winning arm
    # (by raw section reward) scored ga=1 but standard/deep scored ga=0.
    cause_counter: Counter[str] = Counter()
    examples: list[tuple[str, str, str, str]] = []  # (article, sec_id, arm, reason)

    for article in _ALL_42:
        bases_dir = _BASES_DIR / article
        digest_path = bases_dir / "research_digest.md"
        features_path = bases_dir / "guideline_features.json"
        if not (digest_path.exists() and features_path.exists()):
            continue
        digest = digest_path.read_text(encoding="utf-8")
        sec_ids = geo._extract_sec_ids_ordered(digest)
        sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]
        features = json.loads(features_path.read_text(encoding="utf-8"))["sections"]

        arm_dims: dict[str, list[tuple[str, str, int, str]]] = {}
        for arm in geo._ARM_ORDER:
            ep_dir = _ep_dir_for(article, arm)
            arm_dims[arm] = _load_dim_with_reason(ep_dir, "user_intent_guideline_adherence") if ep_dir else []
        arm_dims_ra: dict[str, list[tuple[str, str, int, str]]] = {}
        for arm in geo._ARM_ORDER:
            ep_dir = _ep_dir_for(article, arm)
            arm_dims_ra[arm] = _load_dim_with_reason(ep_dir, "user_intent_research_anchoring") if ep_dir else []

        for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
            feat = features.get(sec_id, {})
            tw_val = feat.get("target_words")
            tw = int(tw_val) if tw_val is not None else 100
            total_w += tw

            ga_by_arm = {}
            for arm in geo._ARM_ORDER:
                r = _get_reason(arm_dims[arm], sec_norm, sec_idx)
                ga_by_arm[arm] = r if r is not None else (0, "")
                acc_ga[arm] += tw * ga_by_arm[arm][0]

            for arm in geo._ARM_ORDER:
                r = _get_reason(arm_dims_ra[arm], sec_norm, sec_idx)
                score = r[0] if r is not None else 0
                acc_ra[arm] += tw * score

            # Disagreement check: does ANY arm score ga=1 while standard/deep score ga=0?
            best_ga = max(ga_by_arm[a][0] for a in geo._ARM_ORDER)
            if best_ga == 1:
                for arm in ("standard", "deep"):
                    score, reason = ga_by_arm[arm]
                    if score == 0:
                        is_length_fail = bool(_LENGTH_FAIL_RE.search(reason))
                        mentions_length = bool(_LENGTH_MENTION_RE.search(reason))
                        if is_length_fail:
                            cause = "LENGTH_VIOLATION"
                        elif mentions_length:
                            cause = "mentions_length_but_passes (other cause)"
                        else:
                            cause = "other (no length mention)"
                        cause_counter[cause] += 1
                        if is_length_fail and len(examples) < 12:
                            examples.append((article, sec_id, arm, reason[:300]))

    if total_w == 0:
        print("No data found.")
        return

    print("=" * 100)
    print("PART 1: Corpus-wide ga vs ra decomposition (target-words-weighted mean, all 42 articles)")
    print("=" * 100)
    for arm in geo._ARM_ORDER:
        print(f"  {arm:<10} ga_mean={acc_ga[arm]/total_w:.4f}   ra_mean={acc_ra[arm]/total_w:.4f}")
    print()
    print("  user_intent = (0.5*ga + 0.5*ra) * 0.30 -- contribution of each sub-term to the arm's user_intent value:")
    for arm in geo._ARM_ORDER:
        ga_contrib = 0.5 * (acc_ga[arm] / total_w) * 0.30
        ra_contrib = 0.5 * (acc_ra[arm] / total_w) * 0.30
        print(f"  {arm:<10} ga_contrib={ga_contrib:.4f}   ra_contrib={ra_contrib:.4f}   total={ga_contrib+ra_contrib:.4f}")

    print()
    print("=" * 100)
    print("PART 2: ga=0 root-cause classification for standard/deep, DISAGREEMENT sections only")
    print("        (sections where some arm scored ga=1 but standard/deep scored ga=0)")
    print("=" * 100)
    total_cases = sum(cause_counter.values())
    print(f"  Total disagreement ga=0 cases (standard+deep combined): {total_cases}")
    for cause, cnt in cause_counter.most_common():
        pct = 100 * cnt / total_cases if total_cases else 0
        print(f"    {cnt:>3} ({pct:5.1f}%)  {cause}")
    print()
    print("  Example LENGTH_VIOLATION reason snippets:")
    for article, sec_id, arm, reason in examples:
        print(f"    [{article} / {sec_id} / {arm}]")
        print(f"      {reason}")
        print()


if __name__ == "__main__":
    main()
