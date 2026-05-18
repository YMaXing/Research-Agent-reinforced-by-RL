"""
Deep analysis of P0 oracle dominance and margin distribution in the 4B scenario
{P0, P1, P3, P5}.

Questions answered:
  Q2: Where does P0's ~47% oracle share come from?
      - Variant breakdown (minimal/standard/demanding)
      - Article breakdown
      - Reward-dimension breakdown — does P0 win because quality is flat?
      - Cost-penalty-vs-quality decomposition

  Q3: How much would different cost rates shift the oracle distribution?
      - Sweep cost_rate ∈ {0.0, 0.005, 0.01, 0.02, 0.03}
      - Per-variant impact on P0-win-rate and live-section fraction
"""
from __future__ import annotations
import json, re, sys
from collections import defaultdict, Counter
from pathlib import Path
from statistics import mean, stdev

EPISODES_ROOT = Path(__file__).parent / "episodes"
ARTICLES = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG",
    "10_memory_knowledge_access", "11_multimodal",
]
VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
SCEN_4B = [0, 1, 3, 5]

REWARD_DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
}
_REASONING_KEYS_ORDERED = [
    "ground_truth_core_content", "ground_truth_flow", "ground_truth_structure",
    "ground_truth_depth_enhancement", "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation", "user_intent_guideline_adherence",
    "user_intent_research_anchoring", "user_intent_golden_source_priority",
]

# Default cost rates from train_grpo.py
DEFAULT_RATE = {"minimal": 0.02, "standard": 0.02, "demanding": 0.005}


def compute_reward(scores, nr, variant, cost_rate=None):
    cc=scores.get("cc",0); fl=scores.get("fl",0)
    de=scores.get("de",0); be=scores.get("be",0)
    cp=scores.get("cp",0); ga=scores.get("ga",0); ra=scores.get("ra",0)
    if cost_rate is None:
        cost_rate = DEFAULT_RATE[variant]
    if variant == "minimal":
        return (0.05*cc + 0.05*fl
                + cp*(0.60*de + 0.40*be)*0.10
                + 0.70*ga + 0.10*ra - cost_rate*nr)
    if variant == "demanding":
        return (0.12*cc + 0.08*fl + cp*(0.55*de + 0.35*be)*0.50
                + (0.60*ga + 0.40*ra)*0.25 - cost_rate*nr)
    return (0.20*cc + 0.20*fl + cp*(0.60*de + 0.40*be)*0.30
            + (0.50*ga + 0.50*ra)*0.30 - cost_rate*nr)


def quality_only(scores, variant):
    return compute_reward(scores, nr=0, variant=variant, cost_rate=0.0)


# ──────────────────────────────────────────────────────────────────────────
def _parse_section_scores(text):
    scores = {}
    lines = text.strip().split("\n")
    i = 0
    while i < len(lines):
        tl = lines[i].strip()
        if tl.endswith(":") and not tl.startswith("**"):
            title = tl[:-1].strip()
            j = i + 1
            while j < len(lines) and not lines[j].strip(): j += 1
            if j < len(lines):
                m = re.match(r"^\*\*([01])[:\*]", lines[j].strip())
                if m:
                    scores[title] = int(m.group(1)); i = j + 1; continue
        i += 1
    return scores


def _tolerant_load(raw):
    out = {}
    for i, key in enumerate(_REASONING_KEYS_ORDERED):
        m = re.search(f'"{re.escape(key)}"\\s*:\\s*"', raw)
        if not m: continue
        vs = m.end()
        if i + 1 < len(_REASONING_KEYS_ORDERED):
            nm = re.search(f'"{re.escape(_REASONING_KEYS_ORDERED[i+1])}"\\s*:', raw[vs:])
            rv = raw[vs: vs + nm.start()] if nm else raw[vs:]
        else: rv = raw[vs:]
        rv = re.sub(r'",?\s*$', '', rv)
        try: rv = rv.encode("utf-8").decode("unicode_escape")
        except Exception: pass
        out[key] = rv
    return out


def load_episode(ep_dir):
    p = ep_dir / "reasoning.json"
    if not p.exists(): return None
    raw = p.read_text(encoding="utf-8", errors="replace")
    try: data = json.loads(raw)
    except json.JSONDecodeError: data = _tolerant_load(raw)
    if not data: return None
    return {s: _parse_section_scores(data.get(k, "")) for s, k in REWARD_DIMS.items()}


def load_all():
    out = defaultdict(lambda: defaultdict(dict))
    for a in ARTICLES:
        for v in VARIANTS:
            for p in range(6):
                ep = load_episode(EPISODES_ROOT / f"{a}__{v}__preset{p}")
                if ep: out[a][v][p] = ep
    return out


# ──────────────────────────────────────────────────────────────────────────
def gather_sections_4B(data, cost_rate_override=None):
    """Yields dicts {article, variant, section, scores_by_preset, rewards, oracle, gap}."""
    rows = []
    for article in ARTICLES:
        for variant in VARIANTS:
            v_short = variant.split("_")[1]
            pdata = data[article][variant]
            if not pdata: continue
            sections = set()
            for pid in SCEN_4B:
                for dvals in pdata.get(pid, {}).values():
                    sections.update(dvals.keys())
            for sec in sorted(sections):
                scores = {pid: {d: pdata.get(pid, {}).get(d, {}).get(sec, 0)
                                for d in REWARD_DIMS} for pid in SCEN_4B}
                rewards = {pid: compute_reward(
                    scores[pid], PRESET_ROUNDS[pid], v_short, cost_rate_override
                ) for pid in SCEN_4B}
                qualities = {pid: quality_only(scores[pid], v_short)
                             for pid in SCEN_4B}
                sorted_r = sorted(rewards.values(), reverse=True)
                gap = sorted_r[0] - sorted_r[1] if len(sorted_r) >= 2 else 0
                oracle = max(rewards, key=rewards.__getitem__)
                rows.append({
                    "article": article, "variant": v_short, "section": sec,
                    "scores": scores, "rewards": rewards, "qualities": qualities,
                    "oracle": oracle, "gap": gap,
                    "q_max": max(qualities.values()), "q_min": min(qualities.values()),
                    "q_spread": max(qualities.values()) - min(qualities.values()),
                })
    return rows


# ══════════════════════════════════════════════════════════════════════════
# Q2: P0 dominance analysis
# ══════════════════════════════════════════════════════════════════════════
def analyse_p0_dominance(rows):
    print("=" * 100)
    print("Q2: WHERE DOES P0 ORACLE DOMINANCE COME FROM?")
    print("=" * 100)

    # ── 2a: P0 win rate by variant ────────────────────────────────────────
    print("\n[2a] P0 win-rate by variant")
    by_v = defaultdict(list)
    for r in rows: by_v[r["variant"]].append(r)
    for v in ["minimal", "standard", "demanding"]:
        rs = by_v[v]
        n = len(rs)
        p0_wins = sum(1 for r in rs if r["oracle"] == 0)
        print(f"  {v:<10}  n={n}  P0_wins={p0_wins}  ({100*p0_wins/n:.1f}%)")

    # ── 2b: P0 win-rate by article ────────────────────────────────────────
    print("\n[2b] P0 win-rate by article (pooled variants)")
    by_a = defaultdict(list)
    for r in rows: by_a[r["article"]].append(r)
    for a in ARTICLES:
        rs = by_a[a]
        if not rs: continue
        p0_wins = sum(1 for r in rs if r["oracle"] == 0)
        print(f"  {a:<35}  n={len(rs):3d}  P0%={100*p0_wins/len(rs):5.1f}")

    # ── 2c: Why does P0 win? Decompose into two reasons ───────────────────
    print("\n[2c] WHY does P0 win? Decomposing P0-oracle sections")
    print("     Reason A (Tied-quality): all 4 presets have equal quality "
          "→ P0 wins by lowest cost (DEAD section)")
    print("     Reason B (Outperforming): P0 has strictly highest quality "
          "→ exploration genuinely hurt or didn't help")
    print("     Reason C (Cost-favoured tie): P0 tied for top quality with "
          "others but cost penalty broke the tie in P0's favour")
    print()
    p0_rows = [r for r in rows if r["oracle"] == 0]
    reason_counts = Counter()
    for r in p0_rows:
        q0 = r["qualities"][0]
        q_others = [r["qualities"][p] for p in SCEN_4B if p != 0]
        q_max_other = max(q_others)
        if r["q_spread"] < 1e-9:
            reason_counts["A_tied_quality_dead"] += 1
        elif q0 > q_max_other + 1e-9:
            reason_counts["B_P0_strictly_best"] += 1
        elif abs(q0 - r["q_max"]) < 1e-9:
            reason_counts["C_cost_broke_tie"] += 1
        else:
            reason_counts["D_other_anomaly"] += 1
    total = len(p0_rows)
    for k in ["A_tied_quality_dead", "B_P0_strictly_best",
              "C_cost_broke_tie", "D_other_anomaly"]:
        v = reason_counts[k]
        print(f"  {k:<28}: {v:3d} / {total}  ({100*v/total:5.1f}%)")

    # ── 2d: Same decomposition split by variant ───────────────────────────
    print("\n[2d] P0-win reasons by variant")
    print(f"  {'Variant':<11}  {'TotalP0':>8}  "
          f"{'A_dead':>10}  {'B_strict':>10}  {'C_tie':>8}  {'D':>4}")
    for v in ["minimal", "standard", "demanding"]:
        rs = [r for r in by_v[v] if r["oracle"] == 0]
        if not rs:
            print(f"  {v:<11}  {0:>8}  {'-':>10}  {'-':>10}  {'-':>8}  {'-':>4}")
            continue
        c = Counter()
        for r in rs:
            q0 = r["qualities"][0]
            qo = max(r["qualities"][p] for p in SCEN_4B if p != 0)
            if r["q_spread"] < 1e-9: c["A"] += 1
            elif q0 > qo + 1e-9:     c["B"] += 1
            elif abs(q0 - r["q_max"]) < 1e-9: c["C"] += 1
            else: c["D"] += 1
        n = len(rs)
        print(f"  {v:<11}  {n:>8}  "
              f"{c['A']:>4} ({100*c['A']/n:4.1f}%)  "
              f"{c['B']:>4} ({100*c['B']/n:4.1f}%)  "
              f"{c['C']:>3} ({100*c['C']/n:4.1f}%)  "
              f"{c['D']:>3}")

    # ── 2e: When P0 wins by strict quality (Reason B), which dim drove it?
    print("\n[2e] When P0 strictly beats exploration (Reason B): "
          "which dim does P0 win on?")
    b_rows = [r for r in p0_rows if r["qualities"][0] >
              max(r["qualities"][p] for p in SCEN_4B if p != 0) + 1e-9]
    print(f"  Total Reason-B sections: {len(b_rows)}")
    dim_wins = Counter()
    for r in b_rows:
        for d in REWARD_DIMS:
            s0 = r["scores"][0][d]
            others = [r["scores"][p][d] for p in SCEN_4B if p != 0]
            if s0 > max(others):
                dim_wins[d] += 1
            elif s0 < min(others):
                dim_wins[f"{d}_LOSE"] += 1
    for d in REWARD_DIMS:
        w = dim_wins[d]; l = dim_wins[f"{d}_LOSE"]
        print(f"  {d}:  P0_wins={w:>3}  P0_loses={l:>3}  net={w-l:+d}")


# ══════════════════════════════════════════════════════════════════════════
# Q3: Margin analysis + cost rate sweep
# ══════════════════════════════════════════════════════════════════════════
def analyse_margins(data):
    print()
    print("=" * 100)
    print("Q3a: ORACLE GAP DISTRIBUTION IN 4B SCENARIO")
    print("=" * 100)
    rows = gather_sections_4B(data)

    by_v = defaultdict(list)
    for r in rows: by_v[r["variant"]].append(r)

    BINS = [0.0, 0.001, 0.005, 0.01, 0.02, 0.04, 0.08, float("inf")]
    LBL  = ["=0", "(0,0.005]", "(0.005,0.01]", "(0.01,0.02]",
            "(0.02,0.04]", "(0.04,0.08]", ">0.08"]

    def hist(gaps):
        counts = [0]*(len(BINS)-1)
        for g in gaps:
            if g < 1e-9: counts[0] += 1; continue
            for i in range(1, len(BINS)-1):
                if BINS[i] < g <= BINS[i+1]: counts[i] += 1; break
            else:
                if g > BINS[-2]: counts[-1] += 1
        return counts

    # Recompute bin assignment cleanly
    def hist2(gaps):
        c = [0]*(len(BINS)-1)
        for g in gaps:
            placed = False
            for i in range(len(BINS)-1):
                lo, hi = BINS[i], BINS[i+1]
                if i == 0 and g < 1e-9: c[0] += 1; placed = True; break
                if lo > 0 and lo < g <= hi: c[i] += 1; placed = True; break
            if not placed and g > BINS[-2]: c[-1] += 1
        return c

    print(f"\n  {'Variant':<10}  " + "  ".join(f"{l:>13}" for l in LBL) +
          f"  {'mean':>7}  {'median':>7}")
    for v in ["minimal", "standard", "demanding"]:
        gaps = [r["gap"] for r in by_v[v]]
        c = hist2(gaps)
        n = len(gaps)
        print(f"  {v:<10}  " +
              "  ".join(f"{x:>4} ({100*x/n:4.1f}%)" for x in c) +
              f"  {mean(gaps):.4f}  {sorted(gaps)[n//2]:.4f}")

    # ── Cost-only margin reference values ────────────────────────────────
    print("\n  Cost-only margins (max cost-induced gap):")
    print("    minimal/standard:  cost_rate=0.02 × 3 rounds = 0.060")
    print("    demanding       :  cost_rate=0.005 × 3 rounds = 0.015")

    # ── Q3b: cost-rate sweep ──────────────────────────────────────────────
    print()
    print("=" * 100)
    print("Q3b: COST-RATE SWEEP — how does P0 dominance and signal change?")
    print("=" * 100)
    print("  Sweep cost_rate uniformly across variants.")
    print("  Reports: P0_win%, P1_win%, P3_win%, P5_win%, live%, mean_gap, "
          "quality-flat%")
    print()
    RATES = [0.0, 0.0025, 0.005, 0.01, 0.015, 0.02, 0.03, 0.04]

    for v in ["minimal", "standard", "demanding"]:
        print(f"\n[{v}]   (default rate: {DEFAULT_RATE[v]})")
        print(f"  {'rate':>6}  {'P0%':>6}  {'P1%':>6}  {'P3%':>6}  {'P5%':>6}  "
              f"{'live%':>6}  {'flat%':>6}  {'mean_gap':>9}")
        for rate in RATES:
            rs_v = []
            # Recompute everything with this rate
            for article in ARTICLES:
                pdata = data[article][f"var_{v}"]
                if not pdata: continue
                sections = set()
                for pid in SCEN_4B:
                    for dvals in pdata.get(pid, {}).values():
                        sections.update(dvals.keys())
                for sec in sorted(sections):
                    scores = {pid: {d: pdata.get(pid,{}).get(d,{}).get(sec,0)
                              for d in REWARD_DIMS} for pid in SCEN_4B}
                    rewards = {pid: compute_reward(
                        scores[pid], PRESET_ROUNDS[pid], v, rate
                    ) for pid in SCEN_4B}
                    qualities = {pid: quality_only(scores[pid], v)
                                 for pid in SCEN_4B}
                    sr = sorted(rewards.values(), reverse=True)
                    gap = sr[0] - sr[1] if len(sr) >= 2 else 0
                    rs_v.append({
                        "oracle": max(rewards, key=rewards.__getitem__),
                        "gap": gap,
                        "q_spread": max(qualities.values()) - min(qualities.values()),
                    })
            n = len(rs_v)
            cost_margin = rate * 3
            p_counts = Counter(r["oracle"] for r in rs_v)
            live = sum(1 for r in rs_v if r["gap"] > cost_margin)
            flat = sum(1 for r in rs_v if r["q_spread"] < 1e-9)
            mg = mean(r["gap"] for r in rs_v)
            print(f"  {rate:>6.4f}  "
                  f"{100*p_counts[0]/n:>5.1f}  "
                  f"{100*p_counts[1]/n:>5.1f}  "
                  f"{100*p_counts[3]/n:>5.1f}  "
                  f"{100*p_counts[5]/n:>5.1f}  "
                  f"{100*live/n:>5.1f}  "
                  f"{100*flat/n:>5.1f}  "
                  f"{mg:>9.4f}")


def main():
    data = load_all()
    rows = gather_sections_4B(data)
    analyse_p0_dominance(rows)
    analyse_margins(data)


if __name__ == "__main__":
    main()
