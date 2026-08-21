"""
A.15.4 step 2-4: TEST-set replication signal evaluation.

For the 12 CRITICAL/HIGH TEST articles replicated at N=3 (production + 2
replicates, temp=0.7), compare each article's single-draw production
oracle_arm/margin against the N=3-averaged oracle_arm/margin (computed from
section_oracle_averaged.json, written by merge_replicate_oracles.py), and
tally each draw's own per-article argmax ("vote") using the same
majority-vote-vs-averaged-argmax discipline established for TRAIN in A.15.2.

This mirrors quantify_defensible_gain_070.py's "Step D" block exactly, but
scoped to TEST (no-variant) articles, using measure_replicate_noise.py's
per-article preset mapping (_arm_presets_flat_for) instead of the TRAIN-only
module constant _ARM_PRESETS_FLAT -- TEST articles map presets 0-3 directly
to skip/light/standard/deep, unlike TRAIN's {0,1,3,5}.

Read-only: no LLM calls, no writes (section_oracle_averaged.json must already
exist per article -- run merge_replicate_oracles.py first).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import audit_oracle_margins as aom  # noqa: E402
import compute_article_oracle as cao  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402

_TEST_ARTICLES = [
    "Earth_Oceans_Origin", "Gravity_Entropy", "Dark_Dimension",
    "14_agent_system_design", "07_reasoning_planning", "Distinct_AI_Models",
    "04_structured_outputs", "Space-Time_QECC", "13_agent_framework",
    "Bird_Eye_Extreme", "Understanding_Reasoning_LLMs", "Insects_Consciousness",
]

# recurring light<->deep confusion cluster flagged in A.15.4 step 3
_CONFUSION_CLUSTER = {
    "13_agent_framework", "Distinct_AI_Models", "Bird_Eye_Extreme",
    "Space-Time_QECC", "Dark_Dimension",
}


def main() -> None:
    replicates = [1, 2]
    margin_rows = {r["name"]: r for r in aom.scan(aom._DEFAULT_BASES_DIR, aom._DEFAULT_HIGH, aom._DEFAULT_MODERATE)}

    n_confirmed = n_flipped = n_hard_ruled = 0
    header = (f"{'article':<32} {'tier':<10} | {'production':>10} {'margin':>8} | "
              f"{'averaged':>10} {'margin':>8} | {'votes':<20} {'cluster'}")
    print("=" * 100)
    print("A.15.4 STEP 2-3: TEST article-level production (single-draw) vs N=3-averaged oracle_arm/margin")
    print("=" * 100)
    print(header)
    print("-" * len(header))

    rows_out = []
    for art in _TEST_ARTICLES:
        avg_path = mrn._BASES_DIR / art / "section_oracle_averaged.json"
        orig_path = mrn._BASES_DIR / art / "section_oracle.json"
        feat_path = mrn._BASES_DIR / art / "guideline_features.json"
        if not avg_path.exists():
            print(f"  SKIP {art}: no section_oracle_averaged.json (run merge_replicate_oracles.py first)")
            continue

        avg_sections = json.loads(avg_path.read_text(encoding="utf-8"))["sections"]
        feats = json.loads(feat_path.read_text(encoding="utf-8")).get("sections", {}) if feat_path.exists() else {}
        r_w, *_ = cao._compute_r_w(avg_sections, feats)
        ranked = sorted(r_w, key=r_w.get, reverse=True)
        avg_margin = r_w[ranked[0]] - r_w[ranked[1]]

        row = margin_rows.get(art, {})
        tier = row.get("risk_tier", "?")
        prod_arm = row.get("oracle_arm", "?")
        prod_margin = row.get("margin", float("nan"))

        # per-draw raw vote tally (production draw + each replicate's own argmax)
        orig_oracle = json.loads(orig_path.read_text(encoding="utf-8"))
        orig_r_w, *_ = cao._compute_r_w(orig_oracle["sections"], feats)
        votes = [max(orig_r_w, key=orig_r_w.get)]
        sec_ids = list(avg_sections.keys())
        presets_flat = mrn._arm_presets_flat_for(art)
        for r in replicates:
            prefix = mrn._NOISE_EXPERIMENT_DIR / f"{art}__replicate{r}"
            if not any((mrn._NOISE_EXPERIMENT_DIR / f"{art}__replicate{r}__preset{p}" / "reasoning.json").exists()
                       for p in presets_flat):
                continue
            rep_sections = mrn._compute_replicate_sections(art, prefix, sec_ids)
            rep_r_w, *_ = cao._compute_r_w(rep_sections, feats)
            votes.append(max(rep_r_w, key=rep_r_w.get))
        vote_str = ",".join(votes)
        vote_counts = {a: votes.count(a) for a in set(votes)}
        top_count = max(vote_counts.values())
        tied_leaders = [a for a, c in vote_counts.items() if c == top_count]
        if len(tied_leaders) == 1:
            majority_arm = tied_leaders[0]
            has_true_majority = top_count > len(votes) / 2 or (top_count == len(votes))
        else:
            # genuine N-way split (e.g. 3 draws, 3 different arms) -- no true majority exists.
            majority_arm = None
            has_true_majority = False
        cluster_flag = "CLUSTER" if art in _CONFUSION_CLUSTER else ""

        if tier in ("POLICY-FORCED", "MANUAL-OVERRIDE"):
            n_hard_ruled += 1
            flag = "(hard-ruled)"
        elif ranked[0] == prod_arm:
            n_confirmed += 1
            flag = "CONFIRMED"
        else:
            n_flipped += 1
            flag = "**FLIPPED**"

        print(f"{art:<32} {tier:<10} | {str(prod_arm):>10} {prod_margin:>8.4f} | "
              f"{ranked[0]:>10} {avg_margin:>8.4f} | {vote_str:<20} {cluster_flag:<8} {flag}")

        rows_out.append({
            "article": art, "tier": tier, "prod_arm": prod_arm, "prod_margin": prod_margin,
            "avg_arm": ranked[0], "avg_margin": avg_margin, "votes": votes,
            "majority_arm": majority_arm, "has_true_majority": has_true_majority, "flag": flag,
        })

    print("-" * len(header))
    print(f"{n_confirmed} confirmed, {n_flipped} flipped, {n_hard_ruled} hard-ruled out of {len(_TEST_ARTICLES)}")

    print()
    print("=" * 100)
    print("A.15.4 STEP 4: majority-vote vs averaged-argmax disagreement check")
    print("=" * 100)
    any_disagreement = False
    any_no_majority = False
    for r in rows_out:
        if r["majority_arm"] is None:
            any_no_majority = True
            print(f"  {r['article']:<32} averaged-argmax={r['avg_arm']:<9} "
                  f"NO TRUE MAJORITY (3-way split) votes={r['votes']}  "
                  f"-> UNRESOLVED, cannot apply A.15.2 majority-vote rule; falls back to averaged-argmax "
                  f"pending N-expansion or manual review")
        elif r["majority_arm"] != r["avg_arm"]:
            any_disagreement = True
            print(f"  {r['article']:<32} averaged-argmax={r['avg_arm']:<9} "
                  f"majority-vote={r['majority_arm']:<9} votes={r['votes']}  "
                  f"-> per A.15.2 rule, majority-vote GOVERNS")
    if not any_disagreement and not any_no_majority:
        print("  none: averaged-argmax and majority-vote agree for all 12 TEST articles.")

    print()
    print("=" * 100)
    print("A.15.4 STEP 3: light<->deep confusion cluster detail")
    print("=" * 100)
    for r in rows_out:
        if r["article"] in _CONFUSION_CLUSTER:
            mv = r["majority_arm"] if r["majority_arm"] is not None else "NO-MAJORITY"
            changed = " <<< LABEL CHANGE" if r["majority_arm"] is not None and r["majority_arm"] != r["prod_arm"] else ""
            print(f"  {r['article']:<32} production={r['prod_arm']:<9} "
                  f"averaged={r['avg_arm']:<9} majority-vote={mv:<12}{changed}")


if __name__ == "__main__":
    main()
