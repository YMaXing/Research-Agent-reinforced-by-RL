"""Model an ARTICLE-LEVEL hard gate on cp/ra/gsp (thresholds 0.90 and 0.95).

Since cp/ra/gsp are strictly binary at the section level (verified: only {0.0, 1.0}
observed corpus-wide), a fractional threshold like 0.90/0.95 can only be meaningful
as an ARTICLE-LEVEL aggregate (mean across an arm's sections) -- analogous to the
EXISTING policy=forbidden / manual_override mechanism in compute_article_oracle.py,
not a change to the section-level reward formula GRPO trains on.

Mechanism modelled: for each (article, arm), compute mean(cp), mean(ra), mean(gsp)
across that arm's sections. If ANY falls below the threshold, that arm is EXCLUDED
from the article's argmax (hard-gated out) -- same spirit as "forbidden -> forced
skip", but here it's "any-arm-that-violates-a-safety-floor -> disqualified", not a
global article-level policy.

R_w itself is computed with the candidate-E split aggregation (rewards-explore
target-words-weighted, explore simple-mean) using the C2 formula (soft ga gate,
penalty 0.10, cost_coef=-0.03) as the base -- the leading candidate from Part 7 S53-54.
"""
import json
import sys
from pathlib import Path

_TRAINING = Path("/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training")
sys.path.insert(0, str(_TRAINING))
import generate_episode_oracles as geo  # noqa: E402
import model_gate_candidates as m  # noqa: E402

ARMS = geo._ARM_ORDER
BASE_FN = m.CANDIDATES["C2_soft_ga_pen010"]

GATE_DIMS = {"cp": "ground_truth_core_preservation",
             "ra": "user_intent_research_anchoring",
             "gsp": "user_intent_golden_source_priority"}


def compute(corpus, fn):
    """Return list of dicts: one per article, with per-arm R_w and per-arm gate means."""
    out = []
    for art_var, split, secs, no_variant in corpus:
        acc_rest = {a: 0.0 for a in ARMS}
        acc_expl = {a: 0.0 for a in ARMS}
        gate_sum = {a: {k: 0.0 for k in GATE_DIMS} for a in ARMS}
        tot_w = 0
        n = len(secs)
        for sid, tw, per_arm in secs:
            for arm in ARMS:
                nr = geo._ARM_COST_UNITS[arm]
                rest, expl = fn(per_arm[arm], nr)
                acc_rest[arm] += rest * tw
                acc_expl[arm] += expl
                for k in GATE_DIMS:
                    gate_sum[arm][k] += per_arm[arm][k]
            tot_w += tw
        r_w = {a: (acc_rest[a] / tot_w) + (acc_expl[a] / n) for a in ARMS}
        gate_mean = {a: {k: gate_sum[a][k] / n for k in GATE_DIMS} for a in ARMS}
        out.append({"art": art_var, "split": split, "r_w": r_w, "gate_mean": gate_mean})
    return out


def apply_gate(rows, threshold):
    results = []
    for row in rows:
        r_w = row["r_w"]
        gm = row["gate_mean"]
        eligible = [a for a in ARMS if all(gm[a][k] >= threshold for k in GATE_DIMS)]
        baseline_arm = max(ARMS, key=lambda a: r_w[a])
        if eligible:
            gated_arm = max(eligible, key=lambda a: r_w[a])
        else:
            gated_arm = None  # pathological: every arm violates the safety floor
        gated_out = [a for a in ARMS if a not in eligible]
        results.append({
            "art": row["art"], "split": row["split"],
            "baseline_arm": baseline_arm, "gated_arm": gated_arm,
            "gated_out_arms": gated_out,
            "flipped": gated_arm is not None and gated_arm != baseline_arm,
            "all_gated": not eligible,
        })
    return results


def summarize(results, threshold):
    n = len(results)
    flips = [r for r in results if r["flipped"]]
    all_gated = [r for r in results if r["all_gated"]]
    from collections import Counter
    baseline_dist = Counter(r["baseline_arm"] for r in results)
    gated_dist = Counter((r["gated_arm"] or "NONE") for r in results)
    n_any_gated_out = sum(1 for r in results if r["gated_out_arms"])

    print(f"\n=== threshold = {threshold} ===")
    print(f"  articles with >=1 arm gated out: {n_any_gated_out}/{n}")
    print(f"  articles where the WINNING arm changed: {len(flips)}/{n}")
    print(f"  articles where ALL 4 arms violate the gate (no eligible arm): {len(all_gated)}")
    print(f"  baseline arm dist: {dict(baseline_dist)}")
    print(f"  post-gate arm dist: {dict(gated_dist)}")
    if flips:
        print("  flips:")
        for r in flips:
            print(f"    {r['art']:40s} {r['baseline_arm']:8s} -> {r['gated_arm']:8s}  "
                  f"(gated out: {r['gated_out_arms']})")
    if all_gated:
        print("  ALL-GATED (no eligible arm) articles:")
        for r in all_gated:
            print(f"    {r['art']:40s} baseline was {r['baseline_arm']}")


if __name__ == "__main__":
    corpus = m.load_corpus()
    rows = compute(corpus, BASE_FN)
    for thresh in (0.90, 0.95):
        results = apply_gate(rows, thresh)
        summarize(results, thresh)
