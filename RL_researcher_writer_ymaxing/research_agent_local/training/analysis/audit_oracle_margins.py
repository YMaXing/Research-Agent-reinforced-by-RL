"""Margin / at-risk audit of article_oracle.json across the whole corpus.

Motivation (see run13_rl_grok_pipeline_analysis.md, Part 4 "§18-20 — noise
investigation"): the mixed-depth pilots showed that untouched sections can
swing reward by up to ~0.45 absolute between full-pipeline reruns (writer runs
at temperature=0.7), and that this noise can move an *article-level* oracle
margin by ~0.03-0.10 even without any deliberate edit. `compute_article_oracle.py`
already computes a `margin` (winning arm's R_w minus runner-up's R_w) and a flat
`EPS_BAND=0.02` near-tie cutoff — but that cutoff was chosen before this noise
was quantified. This script does NOT re-run anything (zero cost, purely reads
already-computed `article_oracle.json` files) — it just surfaces which existing
labels sit close enough to their own decision boundary that the measured noise
could plausibly have produced a different `oracle_arm`, so replication effort
(Part 4 §20 fix #3/#4: cheap write+grade-only reruns) can be targeted instead of
guessed at.

Risk tiers (provisional — see caveat below):
  CRITICAL     margin < 0.02   (the pipeline's own EPS_BAND; already "near-tie")
  HIGH         0.02 <= margin < 0.06   (within the smallest measured swing:
                                        Insects_Consciousness__mixeddepth's
                                        margin moved 0.128->0.052, a 0.076 swing,
                                        from grading corrections alone)
  MODERATE     0.06 <= margin < 0.10   (within the largest measured swing:
                                        Distinct_AI_Models 0.106->0.021, a 0.085
                                        swing, edit+noise combined)
  COMFORTABLE  margin >= 0.10          (outside the measured noise range so far)

CAVEAT: these thresholds are provisional, derived from only 2 before/after
comparisons that mix a deliberate edit's effect with pipeline noise (neither is
a clean "rerun the identical guideline twice" experiment). Part 4 §20 fix #3
(replicate write+grade only, reusing existing research.md, 2-3x on a small
sample) would give a real noise-only distribution to recalibrate these tiers
and EPS_BAND itself. Until then, treat HIGH/CRITICAL as "worth checking first,"
not "definitely wrong."

Usage (from research_agent_local/):
  python3 training/audit_oracle_margins.py
  python3 training/audit_oracle_margins.py --bases-dir /path/to/bases
  python3 training/audit_oracle_margins.py --high 0.08 --moderate 0.12
  python3 training/audit_oracle_margins.py --csv out.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_DEFAULT_BASES_DIR = _THIS_DIR.parent.parent.parent / "rl_training_data" / "bases"

# Mirrors generate_episode_oracles.py::_ALL_ARTICLES (the 8 course-lesson bases).
_TRAIN_BASE_ARTICLES = {
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
}
_TRAIN_VARIANTS = ("var_minimal", "var_standard", "var_demanding")

# Mirrors test_grok_planner.py's 16 no-variant held-out test articles.
_TEST_ARTICLES = {
    "04_structured_outputs",
    "07_reasoning_planning",
    "13_agent_framework",
    "14_agent_system_design",
    "29_evaluation_metrics",
    "31_CI",
    "Bird_Eye_Extreme",
    "Dark_Dimension",
    "Distinct_AI_Models",
    "Earth_Oceans_Origin",
    "Gravity_Entropy",
    "HNSW",
    "Insects_Consciousness",
    "Space-Time_QECC",
    "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
}

_DEFAULT_HIGH = 0.06
_DEFAULT_MODERATE = 0.10
_EPS_BAND = 0.03  # matches compute_article_oracle.py's current constant (recalibrated 2026-07-25)


def _classify_kind(dir_name: str) -> str:
    """Best-effort split/kind label purely from the directory name."""
    for v in _TRAIN_VARIANTS:
        if dir_name.endswith(f"__{v}"):
            base = dir_name[: -(len(v) + 2)]
            return f"TRAIN ({v}, base={base})" if base in _TRAIN_BASE_ARTICLES else f"TRAIN? ({v})"
    if dir_name in _TRAIN_BASE_ARTICLES:
        return "TRAIN (base dir, duplicate of var_standard)"
    if dir_name in _TEST_ARTICLES:
        return "TEST"
    # Any other suffix on a known TEST/TRAIN stem = a deliberate augmentation
    # (e.g. "__mixeddepth", "__webforced", "__degoldenated" per run13 Part 4/§16).
    for known in _TEST_ARTICLES | _TRAIN_BASE_ARTICLES:
        if dir_name.startswith(known + "__"):
            return f"AUGMENTED (base={known})"
    return "unknown"


def _risk_tier(margin: float, decision_path: list | None, high: float, moderate: float) -> str:
    """Classify risk tier.

    Forbidden-policy and manual-override decisions are NOT reward-comparison
    calls at all — they're hard, deterministic rules applied *regardless* of
    R_w (see compute_article_oracle.py::_decide, the -1 and 0 branches). Their
    "margin" can even be negative (the forced arm need not be the R_w leader),
    which is not noise risk, it's working as designed. Replicating write+grade
    for these would not change the answer, so they're excluded from the
    noise-risk tiers entirely and reported separately.
    """
    path0 = (decision_path or [""])[0]
    if path0.startswith("policy=forbidden"):
        return "POLICY-FORCED"
    if path0.startswith("manual override"):
        return "MANUAL-OVERRIDE"
    if margin < _EPS_BAND:
        return "CRITICAL"
    if margin < high:
        return "HIGH"
    if margin < moderate:
        return "MODERATE"
    return "COMFORTABLE"


def scan(bases_dir: Path, high: float, moderate: float) -> list[dict]:
    rows: list[dict] = []
    missing: list[str] = []
    for d in sorted(bases_dir.iterdir()):
        if not d.is_dir():
            continue
        oracle_path = d / "article_oracle.json"
        if not oracle_path.exists():
            missing.append(d.name)
            continue
        try:
            data = json.loads(oracle_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"  WARN: failed to read {oracle_path}: {exc}", file=sys.stderr)
            continue

        margin = data.get("margin")
        if margin is None:
            continue

        rows.append(
            {
                "name": d.name,
                "kind": _classify_kind(d.name),
                "oracle_arm": data.get("oracle_arm"),
                "runner_up_arm": data.get("runner_up_arm"),
                "margin": round(float(margin), 4),
                "reward_spread": data.get("reward_spread"),
                "r_w_rewards": data.get("r_w_rewards"),
                "n_sections": data.get("n_sections"),
                "total_target_words": data.get("total_target_words"),
                "needs_review": data.get("needs_review", False),
                "decision_path": data.get("decision_path"),
                "risk_tier": _risk_tier(float(margin), data.get("decision_path"), high, moderate),
            }
        )
    if missing:
        print(f"  (skipped {len(missing)} dir(s) with no article_oracle.json yet: "
              f"{', '.join(missing[:8])}{' ...' if len(missing) > 8 else ''})\n",
              file=sys.stderr)
    return rows


def print_report(rows: list[dict], high: float, moderate: float) -> None:
    excluded_tiers = ("POLICY-FORCED", "MANUAL-OVERRIDE")
    excluded = [r for r in rows if r["risk_tier"] in excluded_tiers]
    scored = [r for r in rows if r["risk_tier"] not in excluded_tiers]
    rows_sorted = sorted(scored, key=lambda r: r["margin"])

    tier_order = ["CRITICAL", "HIGH", "MODERATE", "COMFORTABLE"]
    counts = {t: 0 for t in tier_order}
    for r in rows_sorted:
        counts[r["risk_tier"]] += 1

    print("=" * 100)
    print("ARTICLE ORACLE MARGIN AUDIT")
    print("=" * 100)
    print(f"Thresholds: CRITICAL < {_EPS_BAND}  |  HIGH < {high}  |  MODERATE < {moderate}  |  "
          f"COMFORTABLE >= {moderate}")
    print(f"Total article-oracles scanned: {len(rows)}  "
          f"({len(excluded)} excluded as policy-forced/manual-override, {len(rows_sorted)} noise-risk-scored)")
    print("Tier counts: " + "  ".join(f"{t}={counts[t]}" for t in tier_order))
    print()

    header = f"{'margin':>7}  {'tier':<11} {'oracle':<9} {'runner-up':<9} {'review?':<8} {'kind':<38} name"
    print(header)
    print("-" * len(header))
    for r in rows_sorted:
        print(
            f"{r['margin']:>7.4f}  {r['risk_tier']:<11} {str(r['oracle_arm']):<9} "
            f"{str(r['runner_up_arm']):<9} {'YES' if r['needs_review'] else '.':<8} "
            f"{r['kind']:<38} {r['name']}"
        )

    if excluded:
        print()
        print(f"--- {len(excluded)} article(s) excluded from risk-scoring "
              f"(hard rule decided the arm, not a reward comparison) ---")
        for r in sorted(excluded, key=lambda r: r["name"]):
            print(f"  [{r['risk_tier']:<15}] {r['name']:<45} oracle_arm={r['oracle_arm']} "
                  f"(raw margin vs runner-up would be {r['margin']:+.4f})")

    print()
    at_risk = [r for r in rows_sorted if r["risk_tier"] in ("CRITICAL", "HIGH")]
    print(f"--- {len(at_risk)} article(s) recommended for replication first "
          f"(CRITICAL + HIGH tiers, Part 4 §20 fix #3/#4) ---")
    for r in at_risk:
        print(f"  {r['name']}  (margin={r['margin']:.4f}, {r['oracle_arm']} vs {r['runner_up_arm']})")
    if not at_risk:
        print("  (none — every scanned article sits at or above the HIGH-risk threshold)")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit article_oracle.json margins across the corpus and flag at-risk labels."
    )
    parser.add_argument("--bases-dir", type=Path, default=_DEFAULT_BASES_DIR)
    parser.add_argument("--high", type=float, default=_DEFAULT_HIGH,
                         help=f"HIGH-risk margin cutoff (default {_DEFAULT_HIGH}).")
    parser.add_argument("--moderate", type=float, default=_DEFAULT_MODERATE,
                         help=f"MODERATE-risk margin cutoff (default {_DEFAULT_MODERATE}).")
    parser.add_argument("--csv", type=Path, default=None, help="Optional path to write a CSV report.")
    args = parser.parse_args()

    rows = scan(args.bases_dir, args.high, args.moderate)
    print_report(rows, args.high, args.moderate)

    if args.csv:
        fieldnames = [
            "name", "kind", "oracle_arm", "runner_up_arm", "margin", "reward_spread",
            "n_sections", "total_target_words", "needs_review", "risk_tier",
        ]
        with args.csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            for r in sorted(rows, key=lambda r: r["margin"]):
                writer.writerow(r)
        print(f"\nCSV written: {args.csv}")


if __name__ == "__main__":
    main()
