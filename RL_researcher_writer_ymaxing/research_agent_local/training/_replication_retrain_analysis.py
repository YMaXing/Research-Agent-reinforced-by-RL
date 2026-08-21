"""Two decision questions for the replication-based retrain, answered on real data:

Q1. HOW RELIABLE IS A SINGLE DRAW? For each TRAIN (section) compute each of the 3
    draws' own argmax arm and report unanimity (3/3), majority (2/1), and
    3-way-split rates. This directly estimates how often a single-draw training
    target was wrong, and whether N=3 is deep enough -- neither A.13 nor A.14
    reported this at the section level (they reported reward-sd and article-level
    votes instead).

Q2. IS THERE FORMULA HEADROOM LEFT? Re-scores candidate formulas -- including new
    fl/cc demotion and ga-removal variants -- using the CORRECT aggregation order
    (compute the full formula per draw, THEN average the 3 final rewards), which is
    exactly what merge_replicate_oracles.py does for a real retrain. This avoids
    sec59.5's documented caveat (it averaged raw dims first, which is not equivalent
    for the nonlinear ga gate).

For each candidate it reports the quantities that decide whether a retrain can
demonstrate learning, using train_grpo.py::load_section_groups()'s exact logic:
trainable-group count, constant-predictor baselines (strict + near-tie -- sec60.12's
success criterion), label distribution, sigma_floor_fraction, mean |advantage|.

Read-only, zero LLM calls, zero writes.
Usage (from research_agent_local/):  python3 training/_replication_retrain_analysis.py
"""
from __future__ import annotations

import json
import math
import statistics
import sys
from collections import Counter
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402

_REPO = _TRAINING.parent.parent
_BASES = _REPO / "rl_training_data" / "bases"
_NOISE = _REPO / "rl_training_data" / "noise_experiment"

ARMS = ["skip", "light", "standard", "deep"]
_SIGMA_FLOOR = 0.04
_NEAR_TIE_MARGIN = 0.06

DIMS = {
    "cc": "ground_truth_core_content", "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement", "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation", "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring", "gsp": "ground_truth_structure",
}
ENH = {"de", "be"}

_TRAIN_ARTICLES = [f"{t}__{v}" for t in geo._ALL_ARTICLES for v in geo._VARIANTS]


# --------------------------------------------------------------------------
# Candidate formulas -- (v, nr) -> scalar section reward.
# C2_shipped reproduces generate_episode_oracles.py::_section_reward exactly.
# --------------------------------------------------------------------------
def _mk(*, w_cc, w_fl, w_de, w_be, w_ga_gate_pen, cost_coef=-0.03, ga_thresh=0.5, ordinal_cost=False):
    def f(v, nr):
        gt_base = w_cc * v["cc"] + w_fl * v["fl"]
        explore = v["cp"] * (w_de * v["de"] + w_be * v["be"])
        gate = -w_ga_gate_pen if v["ga"] < ga_thresh else 0.0
        return gt_base + explore + gate + cost_coef * nr
    f._ordinal_cost = ordinal_cost
    return f


_ORDINAL_UNITS = {"skip": 0.0, "light": 1.0, "standard": 2.0, "deep": 3.0}


CANDIDATES = {
    # shipped reference
    "C2_shipped":            _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    # --- demote / drop FLOW ---
    "fl_halved(0.10)":       _mk(w_cc=0.20, w_fl=0.10, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    "fl_dropped(0.00)":      _mk(w_cc=0.20, w_fl=0.00, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    # --- demote / drop CORE CONTENT ---
    "cc_halved(0.10)":       _mk(w_cc=0.10, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    "cc_dropped(0.00)":      _mk(w_cc=0.00, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    # --- both demoted, weight reallocated to de/be ---
    "cc+fl_halved":          _mk(w_cc=0.10, w_fl=0.10, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    "cc+fl_halved,de/be_up": _mk(w_cc=0.10, w_fl=0.10, w_de=0.55, w_be=0.40, w_ga_gate_pen=0.10),
    # --- further demote GUIDELINE ADHERENCE (the gate penalty) ---
    "ga_pen_005":            _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.05),
    "ga_pen_000(removed)":   _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.00),
    "ga_pen_015":            _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.15),
    # --- combined maximal demotion of all three "weak-signal" dims ---
    "ga=0,cc+fl_halved":     _mk(w_cc=0.10, w_fl=0.10, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.00),
    # --- cost_coef interaction with the shipped shape ---
    "C2_cost-0.05":          _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.05),
    "C2_cost-0.02":          _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.02),
    # --- run26's actual winning mechanism: ORDINAL cost units {0,1,2,3}, not H0 {0,1,1.88,2.31} ---
    "run26_ORD_cost-0.06":   _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.06, ordinal_cost=True),
    "ORD_cost-0.04":         _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.04, ordinal_cost=True),
    "ORD_cost-0.03":         _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.03, ordinal_cost=True),
    "ORD_cost-0.02":         _mk(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10, cost_coef=-0.02, ordinal_cost=True),
}


def _load_reasoning(d: Path):
    p = d / "reasoning.json"
    if not p.exists():
        p = d / "reasons.json"
    if not p.exists():
        return None
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    return {k: geo._parse_sections_ordered(data[k]) for k in data if isinstance(data.get(k), str)}


def _vals(entries_by_dim, snorm, idx):
    out = {}
    for short, dim in DIMS.items():
        entries = entries_by_dim.get(dim, [])
        if short in ENH:
            enh = geo._get_enhancement(entries, snorm, idx)
            out[short] = geo._get_score(entries, snorm, idx) if enh is None else enhancement_credit(enh[1])
        else:
            out[short] = geo._get_score(entries, snorm, idx)
    return out


def load_train_draws():
    """[(section_key, {arm: [draw0_vals, draw1_vals, draw2_vals]})], TRAIN only.

    Uses production's own digest-ordered sec_id list (duplicates INCLUDED) so the
    ordinal fallback in _get_score lands on the same entry production used; a
    deduped list diverges on ~9% of cells (analysis md A.15.4, 2026-08-20).
    Later duplicates overwrite earlier ones, exactly as production's dict write does.
    """
    out = []
    for art in _TRAIN_ARTICLES:
        so_path = _BASES / art / "section_oracle.json"
        digest_path = _BASES / art / "research_digest.md"
        if not (so_path.exists() and digest_path.exists()):
            continue
        oracle_keys = list(json.loads(so_path.read_text(encoding="utf-8"))["sections"].keys())
        sec_ids = geo._extract_sec_ids_ordered(digest_path.read_text(encoding="utf-8"))
        if not sec_ids or not set(oracle_keys).issubset(set(sec_ids)):
            sec_ids = oracle_keys
        snorms = [geo._sec_id_to_norm(s) for s in sec_ids]

        arm_draws = {}
        for arm, pids in geo._ARM_PRESETS.items():
            pid = pids[0]
            draws = []
            prod = _load_reasoning(geo._EPISODES_DIR / f"{art}__preset{pid}")
            if prod is not None:
                draws.append(prod)
            for r in (1, 2):
                rep = _load_reasoning(_NOISE / f"{art}__replicate{r}__preset{pid}")
                if rep is not None:
                    draws.append(rep)
            arm_draws[arm] = draws

        n_draws = min(len(arm_draws[a]) for a in ARMS)
        if n_draws < 3:
            print(f"  NOTE {art}: only {n_draws} draws/arm available, skipping", file=sys.stderr)
            continue

        by_sid = {}
        for idx, (sid, snorm) in enumerate(zip(sec_ids, snorms)):
            by_sid[sid] = {a: [_vals(d, snorm, idx) for d in arm_draws[a][:3]] for a in ARMS}
        for sid in oracle_keys:
            out.append((f"{art}__{sid}", by_sid[sid]))
    return out


def _nr(arm, fn=None):
    if fn is not None and getattr(fn, "_ordinal_cost", False):
        return _ORDINAL_UNITS[arm]
    return geo._ARM_COST_UNITS[arm]


def q1_single_draw_reliability(corpus, fn):
    """Per-draw argmax agreement across the 3 draws, under formula `fn`.

    Also reports pairwise agreement. NOTE: draw 0 (production) and draws 1-2
    (replicates) are NOT exchangeable -- the 2026-08-16 grade-correction pass
    reviewed production drafts far more than replicates -- so the rep1-vs-rep2
    pair is the only unbiased estimate of raw draw-to-draw agreement.
    """
    patterns = Counter()
    prod_matches_majority = 0
    n_with_majority = 0
    pair_agree = {"prod-rep1": 0, "prod-rep2": 0, "rep1-rep2": 0}
    for _key, per_arm in corpus:
        draw_winners = []
        for d in range(3):
            rewards = {a: fn(per_arm[a][d], _nr(a, fn)) for a in ARMS}
            draw_winners.append(max(ARMS, key=rewards.__getitem__))
        counts = Counter(draw_winners)
        top = counts.most_common(1)[0][1]
        if top == 3:
            patterns["unanimous (3/3)"] += 1
        elif top == 2:
            patterns["majority (2/1)"] += 1
        else:
            patterns["3-way split (1/1/1)"] += 1
        if top >= 2:
            n_with_majority += 1
            if draw_winners[0] == counts.most_common(1)[0][0]:
                prod_matches_majority += 1
        pair_agree["prod-rep1"] += draw_winners[0] == draw_winners[1]
        pair_agree["prod-rep2"] += draw_winners[0] == draw_winners[2]
        pair_agree["rep1-rep2"] += draw_winners[1] == draw_winners[2]
    return patterns, prod_matches_majority, n_with_majority, pair_agree


def score_candidate(corpus, fn, average_draws: bool):
    """Build train_grpo-equivalent groups; average_draws=False uses production draw only."""
    groups = []
    n_dropped = 0
    for key, per_arm in corpus:
        if average_draws:
            rewards = [statistics.mean(fn(per_arm[a][d], _nr(a, fn)) for d in range(3)) for a in ARMS]
        else:
            rewards = [fn(per_arm[a][0], _nr(a, fn)) for a in ARMS]
        max_r = max(rewards)
        if max_r - min(rewards) < _SIGMA_FLOOR:
            n_dropped += 1
            continue
        mean_r = sum(rewards) / 4
        raw_std = (sum((r - mean_r) ** 2 for r in rewards) / 4) ** 0.5
        std_r = max(raw_std, _SIGMA_FLOOR)
        groups.append({
            "key": key,
            "best": ARMS[rewards.index(max_r)],
            "accept": [i for i, r in enumerate(rewards) if r >= max_r - _NEAR_TIE_MARGIN],
            "floored": raw_std < _SIGMA_FLOOR,
            "advs": [(r - mean_r) / std_r for r in rewards],
            "margin": max_r - sorted(rewards, reverse=True)[1],
        })
    n = len(groups)
    if n == 0:
        return None
    dist = {a: sum(1 for g in groups if g["best"] == a) for a in ARMS}
    strict_base = max(dist[a] / n for a in ARMS)
    near_base = max(sum(1 for g in groups if i in g["accept"]) / n for i, a in enumerate(ARMS))
    probs = [dist[a] / n for a in ARMS if dist[a]]
    return {
        "n": n, "dropped": n_dropped, "dist": dist,
        "strict_base": strict_base, "near_base": near_base,
        "entropy": -sum(p * math.log2(p) for p in probs),
        "floored": sum(1 for g in groups if g["floored"]) / n,
        "mean_abs_adv": statistics.mean(abs(a) for g in groups for a in g["advs"]),
        "med_margin": statistics.median(g["margin"] for g in groups),
        "labels": {g["key"]: g["best"] for g in groups},
    }


def main():
    corpus = load_train_draws()
    print(f"Loaded {len(corpus)} TRAIN sections with a full 3 draws x 4 arms.\n")

    shipped = CANDIDATES["C2_shipped"]

    print("=" * 104)
    print("Q1. SINGLE-DRAW LABEL RELIABILITY (per-section argmax agreement across the 3 draws, shipped C2)")
    print("=" * 104)
    patterns, prod_match, n_maj, pair_agree = q1_single_draw_reliability(corpus, shipped)
    total = sum(patterns.values())
    for k in ("unanimous (3/3)", "majority (2/1)", "3-way split (1/1/1)"):
        print(f"  {k:<24} {patterns[k]:>4}/{total}  = {patterns[k]/total:>6.1%}")
    print(f"    (null model, 3 iid uniform-random draws over 4 arms: 6.3% / 56.3% / 37.5%)")
    print(f"\n  Pairwise agreement between draws:")
    for k, v in pair_agree.items():
        print(f"    {k:<12} {v:>4}/{total} = {v/total:>6.1%}")
    print(f"    ^ rep1-rep2 is the ONLY unbiased pair: the 2026-08-16 correction pass reviewed")
    print(f"      production drafts far more than replicates, so prod-repN is deflated by design.")
    print(f"\n  Production (draw 0) agrees with the majority, where one exists: "
          f"{prod_match}/{n_maj} = {prod_match/n_maj:.1%}")
    print(f"  => naive single-draw 'error rate' vs the N=3 consensus: {1-prod_match/n_maj:.1%}")
    print(f"     (CAVEAT: this is an UPPER bound -- it counts 'corrected production disagrees with")
    print(f"      two uncorrected replicates' as production being wrong, which it may not be.)")
    print(f"     ({patterns['3-way split (1/1/1)']/total:.1%} of sections have no N=3 consensus at all)")

    print("\n" + "=" * 104)
    print("Q2. FORMULA CANDIDATES, scored on N=3-AVERAGED labels (correct order: formula per draw, then average)")
    print("=" * 104)
    hdr = (f"  {'candidate':<24} {'grps':>5} {'sk/li/st/dp':>14} {'ent':>6} "
           f"{'STRICT_base':>11} {'NEAR_base':>10} {'floor%':>7} {'|adv|':>6} {'medMrg':>7} {'lbl_chg':>8}")
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    ship_res = score_candidate(corpus, shipped, average_draws=True)
    for name, fn in CANDIDATES.items():
        r = score_candidate(corpus, fn, average_draws=True)
        common = set(r["labels"]) & set(ship_res["labels"])
        chg = sum(1 for k in common if r["labels"][k] != ship_res["labels"][k])
        dist_s = "/".join(str(r["dist"][a]) for a in ARMS)
        print(f"  {name:<24} {r['n']:>5} {dist_s:>14} {r['entropy']:>6.3f} "
              f"{r['strict_base']:>10.1%} {r['near_base']:>9.1%} {r['floored']:>6.1%} "
              f"{r['mean_abs_adv']:>6.3f} {r['med_margin']:>7.4f} {chg:>7}")

    print("\n  (lbl_chg = sections whose oracle arm differs from shipped C2, of those trainable in both)")
    print("  (STRICT_base/NEAR_base = the trivial constant-predictor bar a run must BEAT, per sec60.12 --")
    print("   LOWER is better: it means the labels are less skewed and learning is easier to demonstrate)")

    print("\n" + "=" * 104)
    print("Q2b. Same candidates on SINGLE-DRAW labels, for the like-for-like comparison")
    print("=" * 104)
    print(hdr)
    print("  " + "-" * (len(hdr) - 2))
    ship_single = score_candidate(corpus, shipped, average_draws=False)
    for name, fn in CANDIDATES.items():
        r = score_candidate(corpus, fn, average_draws=False)
        common = set(r["labels"]) & set(ship_single["labels"])
        chg = sum(1 for k in common if r["labels"][k] != ship_single["labels"][k])
        dist_s = "/".join(str(r["dist"][a]) for a in ARMS)
        print(f"  {name:<24} {r['n']:>5} {dist_s:>14} {r['entropy']:>6.3f} "
              f"{r['strict_base']:>10.1%} {r['near_base']:>9.1%} {r['floored']:>6.1%} "
              f"{r['mean_abs_adv']:>6.3f} {r['med_margin']:>7.4f} {chg:>7}")


if __name__ == "__main__":
    main()
