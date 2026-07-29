"""Model candidate reward formulas that demote non-differentiating metrics to gates.

Read-only. Zero LLM calls, zero writes. Recomputes section-level rewards for the
whole 40-article corpus under several candidate formulas and reports the metrics
that matter for training-signal quality:

  - sigma_floor fraction   (share of sections whose reward spread is below the
                            GRPO noise floor -- the §52.2 symptom)
  - flat-drop rate         (share dropped entirely by train_grpo)
  - margin distribution    (top1 - top2, mean/median)
  - normalized advantage   (regret / max(std, sigma_floor)) -- the ACTUAL GRPO
                            gradient magnitude
  - section-level arm balance
  - article-level arm balance (target-words-weighted R_w, candidate-E explore
                            aggregation, matching compute_article_oracle)

Candidates model the "satisficing gate" redesign: metrics with near-zero
systematic arm differentiation (cp/ra/gsp, and arguably ga) are removed from the
additive reward and instead applied as either a HARD gate (fail => reward
floored) or a SOFT gate (fail => fixed penalty), or simply dropped.
"""
import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import generate_episode_oracles as geo  # noqa: E402
from enhancement_reward import enhancement_credit  # noqa: E402

ARMS = geo._ARM_ORDER
SIGMA_FLOOR = 0.04
NEAR_TIE = 0.06
EPS_BAND = 0.03

DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
    "gsp": "user_intent_golden_source_priority",
}
ENH = {"de", "be"}

TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI",
    "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW",
    "Insects_Consciousness", "Space-Time_QECC", "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]


# ---------------------------------------------------------------------------
# Candidate formulas.  Each returns (rest, explore) like _section_reward_components.
# v = {"cc":..,"fl":..,"de":..,"be":..,"cp":..,"ga":..,"ra":..,"gsp":..}, nr = cost units
# ---------------------------------------------------------------------------

def _gates_pass(v, gate_dims, thresh=0.5):
    return all(v[d] >= thresh for d in gate_dims)


def make_candidate(name, *, cost_coef, w_cc, w_fl, w_de, w_be, w_ga, w_ra,
                   gate_dims=(), gate_mode="none", gate_penalty=0.0):
    """gate_mode: 'none' | 'hard' (fail => explore zeroed AND rest floored to cost only)
                  | 'soft' (fail => flat gate_penalty subtracted)"""
    def f(v, nr):
        explore = v["cp"] * (0.60 * v["de"] + 0.40 * v["be"]) * 0.50 if w_de or w_be else 0.0
        # re-express explore with tunable weights while keeping the cp gate + 0.5 ceiling
        explore = v["cp"] * (w_de * v["de"] + w_be * v["be"])
        rest = w_cc * v["cc"] + w_fl * v["fl"] + w_ga * v["ga"] + w_ra * v["ra"]
        cost = cost_coef * nr
        if gate_dims:
            ok = _gates_pass(v, gate_dims)
            if not ok:
                if gate_mode == "hard":
                    return cost, 0.0          # everything forfeited except the cost debit
                if gate_mode == "soft":
                    rest -= gate_penalty
        return rest + cost, explore
    f.__name__ = name
    return f


CANDIDATES = {}

# A. current production (cost_coef -0.02) and the -0.03 variant, as references
CANDIDATES["A0_current_cost002"] = make_candidate(
    "A0", cost_coef=-0.02, w_cc=0.20, w_fl=0.20, w_de=0.30, w_be=0.20, w_ga=0.15, w_ra=0.15)
CANDIDATES["A1_current_cost003"] = make_candidate(
    "A1", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.30, w_be=0.20, w_ga=0.15, w_ra=0.15)

# B. drop the near-constant gates (ra) only; keep ga additive. weight moved to de/be
CANDIDATES["B_drop_ra"] = make_candidate(
    "B", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.375, w_be=0.25, w_ga=0.15, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp"), gate_mode="soft", gate_penalty=0.0)

# C. SOFT gate on ga: ga leaves the additive reward, small flat penalty when it fails
CANDIDATES["C1_soft_ga_pen005"] = make_candidate(
    "C1", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp", "ga"), gate_mode="soft", gate_penalty=0.05)
CANDIDATES["C2_soft_ga_pen010"] = make_candidate(
    "C2", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp", "ga"), gate_mode="soft", gate_penalty=0.10)
CANDIDATES["C3_soft_ga_pen015"] = make_candidate(
    "C3", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp", "ga"), gate_mode="soft", gate_penalty=0.15)

# G. PURE DROP: ga carries zero weight AND is not gated at all (no penalty of any kind).
# Same cc/fl/de/be weights and same (inert, near-never-firing) cp/ra/gsp soft-gate treatment
# as the C-series, so G vs C1/C2/C3 isolates EXACTLY the value (if any) of penalizing ga
# failures versus simply removing ga from the formula with no substitute mechanism.
CANDIDATES["G_pure_drop_ga"] = make_candidate(
    "G", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp"), gate_mode="soft", gate_penalty=0.0)

# D. HARD gate on ga (+cp/ra/gsp): failing forfeits all content+explore credit
CANDIDATES["D_hard_ga"] = make_candidate(
    "D", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp", "ga"), gate_mode="hard")

# E. HARD gate on the truly-constant trio only (cp/ra/gsp); ga dropped entirely
CANDIDATES["E_hard_trio_drop_ga"] = make_candidate(
    "E", cost_coef=-0.03, w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp"), gate_mode="hard")

# F. same as E but also drop cc (non-differentiating, wrong-signed on TRAIN)
CANDIDATES["F_hard_trio_drop_ga_cc"] = make_candidate(
    "F", cost_coef=-0.03, w_cc=0.0, w_fl=0.30, w_de=0.50, w_be=0.35, w_ga=0.0, w_ra=0.0,
    gate_dims=("cp", "ra", "gsp"), gate_mode="hard")


# ---------------------------------------------------------------------------

def load_corpus():
    """[(art_var, split, [ (sec_id, target_words, {arm: vals}) ... ]) ]"""
    out = []
    targets = [(f"{t}__{v}", t, False) for t in geo._ALL_ARTICLES for v in geo._VARIANTS]
    targets += [(a, a, True) for a in TEST_ARTICLES]

    for art_var, article, no_variant in targets:
        so = geo._BASES_DIR / art_var / "section_oracle.json"
        gf = geo._BASES_DIR / art_var / "guideline_features.json"
        if not so.exists():
            continue
        sec_ids = list(json.loads(so.read_text(encoding="utf-8")).get("sections", {}).keys())
        if not sec_ids:
            continue
        feats = {}
        if gf.exists():
            feats = json.loads(gf.read_text(encoding="utf-8")).get("sections", {})
        sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]

        arm_presets = geo._TEST_ARM_PRESETS if no_variant else geo._ARM_PRESETS
        ep_root = geo._TEST_EPISODES_DIR if no_variant else geo._EPISODES_DIR
        arm_eps = {}
        for arm, pids in arm_presets.items():
            nm = f"{article}__preset{pids[0]}" if no_variant else f"{art_var}__preset{pids[0]}"
            d = ep_root / nm
            if not d.exists():
                alt = geo._EPISODES_DIR / nm
                d = alt if alt.exists() else d
            arm_eps[arm] = _load_all(d) if d.exists() else {}

        secs = []
        for idx, (sid, snorm) in enumerate(zip(sec_ids, sec_norms)):
            tw = feats.get(sid, {}).get("target_words")
            tw = int(tw) if tw is not None else 100
            per_arm = {}
            for arm in ARMS:
                vals = {}
                for short, dim in DIMS.items():
                    entries = arm_eps[arm].get(dim, [])
                    if short in ENH:
                        enh = geo._get_enhancement(entries, snorm, idx)
                        vals[short] = geo._get_score(entries, snorm, idx) if enh is None \
                            else enhancement_credit(enh[1])
                    else:
                        vals[short] = geo._get_score(entries, snorm, idx)
                per_arm[arm] = vals
            secs.append((sid, tw, per_arm))
        out.append((art_var, "TEST" if no_variant else "TRAIN", secs, no_variant))
    return out


def _load_all(episode_dir: Path):
    p = episode_dir / "reasoning.json"
    if not p.exists():
        p = episode_dir / "reasons.json"
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return {d: geo._parse_sections_ordered(data[d]) for d in data if isinstance(data.get(d), str)}


def evaluate(corpus, fn):
    sec_stats = []
    art_arms = []
    for art_var, split, secs, no_variant in corpus:
        acc_rest = {a: 0.0 for a in ARMS}
        acc_expl = {a: 0.0 for a in ARMS}
        tot_w = 0
        for sid, tw, per_arm in secs:
            rewards, explores = {}, {}
            for arm in ARMS:
                nr = geo._ARM_COST_UNITS[arm]
                rest, expl = fn(per_arm[arm], nr)
                rewards[arm] = rest + expl
                explores[arm] = expl
                acc_rest[arm] += rest * tw
                acc_expl[arm] += expl
            tot_w += tw
            rs = [rewards[a] for a in ARMS]
            mx, mn = max(rs), min(rs)
            mean_r = sum(rs) / 4
            std = (sum((r - mean_r) ** 2 for r in rs) / 4) ** 0.5
            srt = sorted(rs, reverse=True)
            sec_stats.append({
                "split": split, "spread": mx - mn, "std": std,
                "margin": srt[0] - srt[1],
                "regret": mx - mean_r,
                "adv": (mx - mean_r) / max(std, SIGMA_FLOOR),
                "arm": max(ARMS, key=lambda a: rewards[a]),
                "near_tie": sum(1 for r in rs if r >= mx - NEAR_TIE) > 1,
            })
        n = len(secs)
        r_w = {a: (acc_rest[a] / tot_w) + (acc_expl[a] / n) for a in ARMS}
        srt = sorted(r_w.values(), reverse=True)
        art_arms.append({"art": art_var, "split": split,
                         "arm": max(ARMS, key=lambda a: r_w[a]),
                         "margin": srt[0] - srt[1]})
    return sec_stats, art_arms


def report(name, sec_stats, art_arms):
    for split in ("TRAIN", "ALL"):
        ss = [s for s in sec_stats if split == "ALL" or s["split"] == split]
        aa = [a for a in art_arms if split == "ALL" or a["split"] == split]
        n = len(ss)
        dropped = sum(1 for s in ss if s["spread"] < SIGMA_FLOOR)
        kept = [s for s in ss if s["spread"] >= SIGMA_FLOOR]
        floor = sum(1 for s in kept if s["std"] < SIGMA_FLOOR)
        margins = [s["margin"] for s in kept]
        advs = [s["adv"] for s in kept]
        nt = sum(1 for s in kept if s["near_tie"])
        dist = {a: sum(1 for s in ss if s["arm"] == a) for a in ARMS}
        adist = {a: sum(1 for x in aa if x["arm"] == a) for a in ARMS}
        thin = sum(1 for x in aa if abs(x["margin"]) < EPS_BAND)
        if split == "TRAIN":
            print(f"{name:24s} | {dropped/n:6.1%} {floor/len(kept):6.1%} "
                  f"{statistics.mean(margins):7.4f} {statistics.median(margins):7.4f} "
                  f"{statistics.mean(advs):6.3f} {nt/len(kept):6.1%} | "
                  f"{dist['skip']:3d}/{dist['light']:3d}/{dist['standard']:3d}/{dist['deep']:3d} | "
                  f"{adist['skip']:2d}/{adist['light']:2d}/{adist['standard']:2d}/{adist['deep']:2d} "
                  f"{thin:2d}", end="")
        else:
            print(f" || {dropped/n:6.1%} {floor/len(kept):6.1%} "
                  f"{statistics.median(margins):7.4f} {statistics.mean(advs):6.3f} | "
                  f"{adist['skip']:2d}/{adist['light']:2d}/{adist['standard']:2d}/{adist['deep']:2d} "
                  f"{thin:2d}")


if __name__ == "__main__":
    corpus = load_corpus()
    print(f"loaded {len(corpus)} articles, "
          f"{sum(len(s) for _, _, s, _ in corpus)} sections\n")
    hdr = (f"{'candidate':24s} | {'drop%':>6s} {'floor%':>6s} {'mMargin':>7s} {'medMrg':>7s} "
           f"{'advNorm':>6s} {'nearTie':>6s} | {'sec sk/li/st/dp':15s} | {'art dist':11s} thin"
           f" || {'ALLdrop':>6s} {'flr%':>6s} {'medMrg':>7s} {'adv':>6s} | {'art dist':11s} thin")
    print(hdr)
    print("-" * len(hdr))
    for name, fn in CANDIDATES.items():
        ss, aa = evaluate(corpus, fn)
        report(name, ss, aa)
    print()
    print("  LEFT block = TRAIN sections (n=171) / TRAIN articles (n=24)")
    print("  RIGHT block (after ||) = ALL 40 articles / 282 sections")
    print("  drop%   = sections dropped by train_grpo as flat (spread < sigma_floor=0.04)")
    print("  floor%  = of kept sections, share with raw_std < sigma_floor (gradient floored)")
    print("  advNorm = mean normalized GRPO advantage = regret / max(std, sigma_floor)")
    print("  nearTie = share of kept sections with 2+ arms within 0.06 of the best")
    print("  thin    = articles whose |R_w margin| < EPS_BAND (0.03) => tie-break needed")
