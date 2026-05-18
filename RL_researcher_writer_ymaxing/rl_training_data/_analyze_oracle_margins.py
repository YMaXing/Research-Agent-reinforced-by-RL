"""
Oracle-vs-runner-up margin analysis and oracle preset distribution.
(8 articles × 3 variants × 6 presets)

For every section group the "oracle" is the preset with the highest reward.
The "runner-up" is the second-highest.  The oracle-to-runner-up margin
(oracle gap) measures how decisively the training signal distinguishes the
best exploration choice from the next-best alternative.

Complement to _analyze_reward_margins.py — that script characterises the
full max-min spread; this one focuses on the top-2 gap and on which presets
actually win (oracle distribution).

Usage:
    python3 _analyze_oracle_margins.py
    python3 _analyze_oracle_margins.py --output oracle_margins.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

# ---------------------------------------------------------------------------
# Config (mirrors _analyze_reward_margins.py)
# ---------------------------------------------------------------------------
ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
]
VARIANTS       = ["var_minimal", "var_standard", "var_demanding"]
N_PRESETS      = 6
PRESET_ROUNDS  = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}

REWARD_DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
}
ALL_DIMS = {
    **REWARD_DIMS,
    "st":  "ground_truth_structure",
    "gsp": "user_intent_golden_source_priority",
}
REWARD_DIM_ORDER = ["cc", "fl", "de", "be", "cp", "ga", "ra"]

# ---------------------------------------------------------------------------
# Reward formula (from train_grpo.py)
# ---------------------------------------------------------------------------
def compute_reward(scores: dict[str, float], preset_id: int, variant: str) -> float:
    cc = scores.get("cc", 0.0);  fl = scores.get("fl", 0.0)
    de = scores.get("de", 0.0);  be = scores.get("be", 0.0)
    cp = scores.get("cp", 0.0);  ga = scores.get("ga", 0.0)
    ra = scores.get("ra", 0.0)
    nr = PRESET_ROUNDS[preset_id]
    if variant == "minimal":
        return 0.05*cc + 0.05*fl + 0.80*ga + 0.10*ra - 0.02*nr
    if variant == "demanding":
        return (0.12*cc + 0.08*fl
                + cp*(0.55*de + 0.35*be)*0.50
                + (0.60*ga + 0.40*ra)*0.25
                - 0.005*nr)
    # standard
    return (0.20*cc + 0.20*fl
            + cp*(0.60*de + 0.40*be)*0.30
            + (0.50*ga + 0.50*ra)*0.30
            - 0.02*nr)


def cost_only_margin(variant: str) -> float:
    cost_rate = 0.005 if variant == "demanding" else 0.02
    return cost_rate * 3   # max_nr - min_nr = 3


# ---------------------------------------------------------------------------
# JSON / reasoning parsers (copied from _analyze_reward_margins.py)
# ---------------------------------------------------------------------------
_REASONING_KEYS_ORDERED = [
    "ground_truth_core_content", "ground_truth_flow", "ground_truth_structure",
    "ground_truth_depth_enhancement", "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation", "user_intent_guideline_adherence",
    "user_intent_research_anchoring", "user_intent_golden_source_priority",
]

def _extract_reasoning_tolerant(raw: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for i, key in enumerate(_REASONING_KEYS_ORDERED):
        m = re.search(f'"{re.escape(key)}"\\s*:\\s*"', raw)
        if not m:
            continue
        vs = m.end()
        if i + 1 < len(_REASONING_KEYS_ORDERED):
            nm = re.search(f'"{re.escape(_REASONING_KEYS_ORDERED[i+1])}"\\s*:', raw[vs:])
            raw_val = raw[vs: vs + nm.start()] if nm else raw[vs:]
        else:
            raw_val = raw[vs:]
        raw_val = re.sub(r'",?\s*$', '', raw_val)
        try:
            decoded = raw_val.encode("utf-8").decode("unicode_escape")
        except Exception:
            decoded = raw_val
        result[key] = decoded
    return result


def parse_section_scores(text: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    lines = text.strip().split("\n")
    i = 0
    while i < len(lines):
        tl = lines[i].strip()
        if tl.endswith(":") and not tl.startswith("**"):
            title = tl[:-1].strip()
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                m = re.match(r"^\*\*([01])[:\*]", lines[j].strip())
                if m:
                    scores[title] = int(m.group(1))
                    i = j + 1
                    continue
        i += 1
    return scores


def load_episode(ep_dir: Path) -> dict[str, dict[str, int]] | None:
    path = ep_dir / "reasoning.json"
    if not path.exists():
        return None
    raw = path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = _extract_reasoning_tolerant(raw)
        if not data:
            return None
    return {short: parse_section_scores(data.get(key, ""))
            for short, key in ALL_DIMS.items()}


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_all(episodes_root: Path) -> dict:
    """data[article][variant][section][dim][preset] = 0|1|None"""
    data = {}
    for article in ARTICLES:
        data[article] = {}
        for variant in VARIANTS:
            sec_data: dict[str, dict[str, list]] = defaultdict(
                lambda: {d: [None]*N_PRESETS for d in ALL_DIMS}
            )
            for preset in range(N_PRESETS):
                ep = episodes_root / f"{article}__{variant}__preset{preset}"
                reasoning = load_episode(ep)
                if reasoning is None:
                    continue
                for sec, sc in reasoning.get("cc", {}).items():
                    for d in ALL_DIMS:
                        sec_data[sec][d][preset] = reasoning[d].get(sec)
                for d in ("ga", "ra", "gsp"):
                    for sec, sc in reasoning.get(d, {}).items():
                        if sec not in sec_data:
                            for d2 in ALL_DIMS:
                                sec_data[sec][d2] = [None]*N_PRESETS
                        sec_data[sec][d][preset] = sc
            data[article][variant] = dict(sec_data)
    return data


def section_rewards(profile: dict[str, list], variant: str) -> list[float]:
    rewards = []
    for p in range(N_PRESETS):
        scores = {d: float(profile[d][p]) if profile[d][p] is not None else 0.0
                  for d in REWARD_DIMS}
        rewards.append(compute_reward(scores, p, variant))
    return rewards


# ---------------------------------------------------------------------------
# Top-2 statistics
# ---------------------------------------------------------------------------
def top2_stats(rewards: list[float]) -> dict:
    indexed = sorted(enumerate(rewards), key=lambda x: x[1], reverse=True)
    p_oracle,  r_oracle   = indexed[0]
    p_runnerup, r_runnerup = indexed[1]
    p3        = indexed[2][0] if len(indexed) > 2 else -1
    oracle_gap = r_oracle - r_runnerup
    return {
        "oracle_preset":   p_oracle,
        "oracle_r":        r_oracle,
        "runnerup_preset": p_runnerup,
        "runnerup_r":      r_runnerup,
        "third_preset":    p3,
        "oracle_gap":      oracle_gap,        # max - 2nd-max
        "full_margin":     r_oracle - min(rewards),
        "regret":          r_oracle - mean(rewards),
        "rewards":         rewards,
    }


# ---------------------------------------------------------------------------
# Report helpers
# ---------------------------------------------------------------------------
SEP  = "=" * 80
SEP2 = "-" * 80


def ptile(lst: list[float], p: float) -> float:
    if not lst:
        return float("nan")
    s = sorted(lst)
    idx = min(int(p / 100.0 * len(s)), len(s) - 1)
    return s[idx]


def pct(n: int, total: int) -> str:
    return f"{100*n/total:.1f}%" if total else "0.0%"


def bar(n: int, total: int, width: int = 40) -> str:
    return "#" * int(width * n / total) if total else ""


# ---------------------------------------------------------------------------
# Main report builder
# ---------------------------------------------------------------------------
def build_report(data: dict) -> list[str]:
    lines: list[str] = []

    def w(*args): lines.append(" ".join(str(a) for a in args))
    def wl():     lines.append("")

    # ── collect all section stats ────────────────────────────────────────────
    # per_variant_stats[variant] = list of top2_stats dicts
    per_variant_stats: dict[str, list[dict]] = {v: [] for v in VARIANTS}
    # full detail for per-article tables
    # detail[article][variant] = list of (sec_title, stats_dict)
    detail: dict = {}

    for article in ARTICLES:
        detail[article] = {}
        for variant in VARIANTS:
            var_key = variant.replace("var_", "")
            rows = []
            for sec, profile in data[article][variant].items():
                rs = section_rewards(profile, var_key)
                stats = top2_stats(rs)
                # also flag whether oracle is truly oracle-driven
                stats["is_live"] = stats["full_margin"] > cost_only_margin(var_key) + 1e-6
                # oracle dim contribution: which dims vary?
                stats["live_dims"] = [
                    d for d in REWARD_DIM_ORDER
                    if len({profile[d][p] for p in range(N_PRESETS)
                             if profile[d][p] is not None}) > 1
                ]
                rows.append((sec, stats))
                per_variant_stats[variant].append(stats)
            detail[article][variant] = rows

    # ═══════════════════════════════════════════════════════════════════════ #
    w(SEP)
    w("ORACLE vs RUNNER-UP MARGIN ANALYSIS")
    w("8 articles × 3 variants × 6 presets")
    w(SEP)
    wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 1: Oracle preset distribution                                      #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 1: Oracle Preset Distribution")
    w("        Which preset achieves the highest reward most often?")
    w("        Broken down by: All sections / Live-only (oracle-driven)")
    w(SEP2)
    wl()

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        stats_list = per_variant_stats[variant]
        total     = len(stats_list)
        live_list  = [s for s in stats_list if s["is_live"]]
        dead_list  = [s for s in stats_list if not s["is_live"]]
        total_live = len(live_list)
        total_dead = len(dead_list)

        w(f"  [{var_key.upper()}]  total={total}  live={total_live}  dead={total_dead}")
        wl()

        # preset → count  (all / live / dead)
        oracle_all  = [0]*N_PRESETS
        oracle_live = [0]*N_PRESETS
        oracle_dead = [0]*N_PRESETS
        for s in stats_list:
            oracle_all[s["oracle_preset"]] += 1
        for s in live_list:
            oracle_live[s["oracle_preset"]] += 1
        for s in dead_list:
            oracle_dead[s["oracle_preset"]] += 1

        w(f"  {'Preset':<8} {'rounds':>7} {'All':>6} {'All%':>6} {'Live':>6} {'Live%':>7} "
          f"{'Dead':>6} {'Dead%':>7}  bar (All)")
        w("  " + "-" * 80)
        for p in range(N_PRESETS):
            nr = PRESET_ROUNDS[p]
            w(f"  P{p:<7} {nr:>7} {oracle_all[p]:>6} {pct(oracle_all[p], total):>6} "
              f"{oracle_live[p]:>6} {pct(oracle_live[p], total_live):>7} "
              f"{oracle_dead[p]:>6} {pct(oracle_dead[p], total_dead):>7}  "
              f"{bar(oracle_all[p], total, 30)}")
        wl()

        # Runner-up distribution
        runnerup_cnt = [0]*N_PRESETS
        for s in stats_list:
            runnerup_cnt[s["runnerup_preset"]] += 1
        w(f"  Runner-up distribution (all sections):")
        w(f"  {'Preset':<8} {'Count':>6} {'Pct':>7}  bar")
        w("  " + "-" * 50)
        for p in range(N_PRESETS):
            w(f"  P{p:<7} {runnerup_cnt[p]:>6} {pct(runnerup_cnt[p], total):>7}  "
              f"{bar(runnerup_cnt[p], total, 30)}")
        wl()

        # Oracle == P0 breakdown
        p0_oracle = oracle_all[0]
        w(f"  P0 oracle rate (all): {p0_oracle}/{total} = {pct(p0_oracle, total)}")
        w(f"  P0 is oracle by default when oracles are identical (cost alone favours P0).")
        # Among dead sections, P0 should always win (min cost, identical quality)
        p0_dead = oracle_dead[0]
        w(f"  Among dead sections: P0 oracle = {p0_dead}/{total_dead} = {pct(p0_dead, total_dead)}")
        wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 2: Oracle-gap (oracle − runner-up) distribution                   #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 2: Oracle Gap Distribution  (oracle_R − runner_up_R)")
    w("        A small gap means GRPO must discriminate near-equal reward presets.")
    w("        A large gap gives a clear training signal.")
    w(SEP2)
    wl()

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        stats_list = per_variant_stats[variant]
        total = len(stats_list)
        live_list = [s for s in stats_list if s["is_live"]]

        gaps_all  = [s["oracle_gap"] for s in stats_list]
        gaps_live = [s["oracle_gap"] for s in live_list]
        co = cost_only_margin(var_key)

        w(f"  [{var_key.upper()}]  cost-only baseline = {co:.4f}")
        wl()

        def dist_table(gaps: list[float], label: str) -> None:
            n = len(gaps)
            if not n:
                return
            w(f"  {label} (n={n}):")
            w(f"  {'Stat':<10} {'Oracle gap':>12}")
            w(f"  {'-'*24}")
            for stat, p in [("Min",0),("P10",10),("P25",25),("Median",50),
                             ("P75",75),("P90",90),("Max",100),("Mean",-1)]:
                val = ptile(gaps, p) if p >= 0 else mean(gaps)
                w(f"  {stat:<10} {val:>12.4f}")
            wl()

            # bucket breakdown
            buckets = [(0, 0.005),(0.005, 0.01),(0.01, 0.06),(0.06, 0.10),
                       (0.10, 0.20),(0.20, 0.50),(0.50, 1.1)]
            w(f"  Gap bucket distribution:")
            for lo, hi in buckets:
                cnt = sum(1 for g in gaps if lo <= g < hi)
                label2 = f"[{lo:.3f},{hi:.3f})"
                w(f"    {label2}  {cnt:3d} ({pct(cnt,n)})  {bar(cnt,n,30)}")
            wl()

            # "decisive" thresholds
            w(f"  Decisive oracle rates (gap > threshold):")
            for thr in [0.01, 0.05, 0.10, 0.20, 0.30]:
                cnt = sum(1 for g in gaps if g > thr)
                w(f"    gap > {thr:.2f}:  {cnt}/{n} = {pct(cnt, n)}")
            wl()

        dist_table(gaps_all,  "All sections")
        dist_table(gaps_live, "Live sections only (oracle-driven)")

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 3: Oracle gap vs full margin comparison                            #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 3: Oracle gap vs full margin — how much of the reward spread sits")
    w("        between oracle and runner-up vs the full max-min range?")
    w(SEP2)
    wl()
    w("  ratio = oracle_gap / full_margin")
    w("  ratio ≈ 1.0 → runner-up is almost as bad as the worst preset")
    w("  ratio ≈ 0.0 → oracle is barely better than runner-up despite large full spread")
    wl()

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        live_list = [s for s in per_variant_stats[variant]
                     if s["is_live"] and s["full_margin"] > 1e-8]
        if not live_list:
            continue
        ratios = [s["oracle_gap"] / s["full_margin"] for s in live_list]
        w(f"  [{var_key.upper()}]  live sections n={len(live_list)}")
        for stat, p in [("P10",10),("P25",25),("Median",50),("P75",75),("P90",90),("Mean",-1)]:
            val = ptile(ratios, p) if p >= 0 else mean(ratios)
            w(f"    {stat:<8} {val:.3f}")
        wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 4: Cross-variant oracle agreement                                  #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 4: Cross-variant oracle agreement")
    w("        For each section present in all 3 variants, do min/std/dem")
    w("        agree on the same oracle preset?")
    w(SEP2)
    wl()

    # collect per (article, sec) → {variant: oracle_preset}
    agree_total = agree_all3 = agree_2of3 = 0
    disagree_cases: list[tuple] = []

    for article in ARTICLES:
        for sec in set.intersection(
            *(set(s for s, _ in detail[article][v]) for v in VARIANTS)
        ):
            entry = {}
            for variant in VARIANTS:
                for s, stats in detail[article][variant]:
                    if s == sec:
                        entry[variant] = stats["oracle_preset"]
                        break
            if len(entry) == 3:
                agree_total += 1
                presets = list(entry.values())
                if len(set(presets)) == 1:
                    agree_all3 += 1
                elif len(set(presets)) == 2:
                    agree_2of3 += 1
                    disagree_cases.append((article, sec, entry))
                else:
                    disagree_cases.append((article, sec, entry))

    w(f"  Sections present in all 3 variants: {agree_total}")
    w(f"  All 3 variants agree on same oracle: {agree_all3} ({pct(agree_all3, agree_total)})")
    w(f"  Exactly 2 of 3 variants agree:      {agree_2of3} ({pct(agree_2of3, agree_total)})")
    w(f"  All 3 variants disagree:             {agree_total - agree_all3 - agree_2of3} "
      f"({pct(agree_total - agree_all3 - agree_2of3, agree_total)})")
    wl()
    if disagree_cases:
        w(f"  Disagreement cases (oracle differs across variants):")
        w(f"  {'Article':<35} {'Section':<48} {'min':>6} {'std':>6} {'dem':>6}")
        w("  " + "-" * 105)
        for article, sec, entry in sorted(disagree_cases)[:40]:
            sl = (sec[:47] + "…") if len(sec) > 48 else sec
            m = entry.get("var_minimal", "?")
            s = entry.get("var_standard", "?")
            d = entry.get("var_demanding", "?")
            w(f"  {article:<35} {sl:<48} {f'P{m}':>6} {f'P{s}':>6} {f'P{d}':>6}")
    wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 5: Per-article per-variant full section table                      #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 5: Per-section oracle and runner-up breakdown (all articles)")
    w("        Cols: section | oracle Px→R | runner-up Px→R | gap | full-margin | live?")
    w("        * = oracle-driven (margin > cost-only baseline)")
    w("        Reward values: P0  P1  P2  P3  P4  P5")
    w(SEP2)
    wl()

    for article in ARTICLES:
        w(f"  === {article} ===")
        for variant in VARIANTS:
            var_key = variant.replace("var_", "")
            co = cost_only_margin(var_key)
            rows = detail[article][variant]
            if not rows:
                continue
            w(f"    [{var_key.upper()}]  cost-only baseline = {co:.4f}")
            w(f"    {'Section':<45} {'Oracle':>8} {'RunUp':>8} "
              f"{'Gap':>7} {'FullMg':>7} {'Regret':>7}  "
              f"{'P0':>6} {'P1':>6} {'P2':>6} {'P3':>6} {'P4':>6} {'P5':>6}")
            w("    " + "-" * 160)
            for sec, stats in rows:
                marker = "*" if stats["is_live"] else " "
                sl = (sec[:44] + "…") if len(sec) > 45 else sec
                op = stats["oracle_preset"]
                rp = stats["runnerup_preset"]
                oracle_str   = f"P{op}→{stats['oracle_r']:.3f}"
                runnerup_str = f"P{rp}→{stats['runnerup_r']:.3f}"
                rs = stats["rewards"]
                r_strs = "  ".join(f"{r:6.3f}" for r in rs)
                w(f"  {marker}   {sl:<45} {oracle_str:>9} {runnerup_str:>9} "
                  f"{stats['oracle_gap']:>7.4f} {stats['full_margin']:>7.4f} "
                  f"{stats['regret']:>7.4f}  {r_strs}")
            gaps_here = [s["oracle_gap"] for _, s in rows]
            live_n    = sum(1 for _, s in rows if s["is_live"])
            w(f"    → Live:{live_n}/{len(rows)}  mean gap={mean(gaps_here):.4f}"
              f"  mean full-margin={mean(s['full_margin'] for _, s in rows):.4f}")
            wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 6: GRPO learning-signal quality per variant                        #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 6: GRPO signal quality — oracle gap perspective")
    w("        The oracle gap is the reward difference GRPO must amplify.")
    w("        Sections with gap < sigma_floor (default ~0.01) get their")
    w("        advantages collapsed to ±1/sigma_floor: near-useless gradient.")
    w(SEP2)
    wl()

    SIGMA_FLOORS = [0.005, 0.010, 0.020, 0.040]

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        all_stats = per_variant_stats[variant]
        gaps  = [s["oracle_gap"]   for s in all_stats]
        fmgs  = [s["full_margin"]  for s in all_stats]
        regs  = [s["regret"]       for s in all_stats]
        total = len(all_stats)

        w(f"  [{var_key.upper()}]  n={total}")
        w(f"    Oracle gap  — mean={mean(gaps):.4f}  median={ptile(gaps,50):.4f}"
          f"  max={max(gaps):.4f}")
        w(f"    Full margin — mean={mean(fmgs):.4f}  median={ptile(fmgs,50):.4f}"
          f"  max={max(fmgs):.4f}")
        w(f"    Regret      — mean={mean(regs):.4f}  median={ptile(regs,50):.4f}"
          f"  max={max(regs):.4f}")
        wl()
        w(f"    Sections below various sigma_floor thresholds (gap < floor → flat group):")
        w(f"    {'sigma_floor':<14} {'n_flat':>8} {'pct_flat':>10} {'n_usable':>10} {'pct_usable':>12}")
        w(f"    {'-'*56}")
        for sf in SIGMA_FLOORS:
            n_flat    = sum(1 for g in gaps if g < sf)
            n_usable  = total - n_flat
            w(f"    {sf:<14.3f} {n_flat:>8} {pct(n_flat, total):>10} "
              f"{n_usable:>10} {pct(n_usable, total):>12}")
        wl()

        # Also show oracle distribution restricted to "decisive" sections (gap > 0.10)
        decisive = [s for s in all_stats if s["oracle_gap"] > 0.10]
        nd = len(decisive)
        w(f"    Oracle distribution for 'decisive' sections (gap > 0.10, n={nd}):")
        if nd:
            cnt_decisive = [0]*N_PRESETS
            for s in decisive:
                cnt_decisive[s["oracle_preset"]] += 1
            for p in range(N_PRESETS):
                if cnt_decisive[p]:
                    w(f"      P{p}: {cnt_decisive[p]} ({pct(cnt_decisive[p], nd)})  "
                      f"{bar(cnt_decisive[p], nd, 25)}")
        wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 7: Top-20 most decisive sections                                   #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 7: Top-20 most decisive sections (largest oracle gap)")
    w(SEP2)
    wl()

    all_rows: list[tuple] = []
    for article in ARTICLES:
        for variant in VARIANTS:
            for sec, stats in detail[article][variant]:
                var_key = variant.replace("var_", "")
                all_rows.append((stats["oracle_gap"], article, var_key, sec, stats))

    top20 = sorted(all_rows, key=lambda x: x[0], reverse=True)[:20]
    w(f"  {'#':<4} {'Article+Variant':<43} {'Section':<46} "
      f"{'Gap':>7} {'Oracle':>9} {'RunUp':>9}")
    w("  " + "-" * 125)
    for i, (gap, art, var_key, sec, stats) in enumerate(top20, 1):
        av = f"{art}__{var_key}"[:42]
        sl = (sec[:45] + "…") if len(sec) > 46 else sec
        op = f"P{stats['oracle_preset']}→{stats['oracle_r']:.3f}"
        rp = f"P{stats['runnerup_preset']}→{stats['runnerup_r']:.3f}"
        w(f"  {i:<4} {av:<43} {sl:<46} {gap:>7.4f} {op:>9} {rp:>9}")
    wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 8: Top-20 most ambiguous sections (smallest oracle gap, live only) #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 8: Top-20 most ambiguous sections (smallest oracle gap, live only)")
    w("        These sections have oracle-driven spread but the top-2 presets")
    w("        are nearly tied — GRPO may not reliably learn the distinction.")
    w(SEP2)
    wl()

    live_rows = [(g, art, vk, sec, stats)
                 for g, art, vk, sec, stats in all_rows
                 if stats["is_live"]]
    bottom20 = sorted(live_rows, key=lambda x: x[0])[:20]
    w(f"  {'#':<4} {'Article+Variant':<43} {'Section':<46} "
      f"{'Gap':>7} {'FullMg':>7} {'Oracle':>9} {'RunUp':>9}")
    w("  " + "-" * 130)
    for i, (gap, art, var_key, sec, stats) in enumerate(bottom20, 1):
        av = f"{art}__{var_key}"[:42]
        sl = (sec[:45] + "…") if len(sec) > 46 else sec
        op = f"P{stats['oracle_preset']}→{stats['oracle_r']:.3f}"
        rp = f"P{stats['runnerup_preset']}→{stats['runnerup_r']:.3f}"
        w(f"  {i:<4} {av:<43} {sl:<46} {gap:>7.4f} {stats['full_margin']:>7.4f} "
          f"{op:>9} {rp:>9}")
    wl()

    # ─────────────────────────────────────────────────────────────────────── #
    # PART 9: Oracle-gap summary across all variants                          #
    # ─────────────────────────────────────────────────────────────────────── #
    w(SEP2)
    w("PART 9: Global oracle-gap summary")
    w(SEP2)
    wl()

    all_gaps = [(s["oracle_gap"], variant.replace("var_",""))
                for variant in VARIANTS
                for s in per_variant_stats[variant]]
    all_gap_vals = [g for g, _ in all_gaps]
    w(f"  Total section groups: {len(all_gap_vals)}")
    w(f"  Oracle gap — mean={mean(all_gap_vals):.4f}  median={ptile(all_gap_vals,50):.4f}"
      f"  max={max(all_gap_vals):.4f}  min={min(all_gap_vals):.4f}")
    wl()
    w(f"  Global decisive rates:")
    for thr in [0.01, 0.05, 0.10, 0.20]:
        cnt = sum(1 for g in all_gap_vals if g > thr)
        w(f"    gap > {thr:.2f}:  {cnt}/{len(all_gap_vals)} = {pct(cnt, len(all_gap_vals))}")
    wl()
    w(f"  Oracle preset distribution across all variants:")
    combined_cnt = [0]*N_PRESETS
    for s in [s for v in VARIANTS for s in per_variant_stats[v]]:
        combined_cnt[s["oracle_preset"]] += 1
    total_all = len(all_gap_vals)
    for p in range(N_PRESETS):
        w(f"    P{p}: {combined_cnt[p]:3d} ({pct(combined_cnt[p], total_all)})  "
          f"{bar(combined_cnt[p], total_all, 30)}")
    wl()

    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="_oracle_margins_report.txt")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    if (here / "episodes").exists():
        episodes_root = here / "episodes"
    elif (here.parent / "rl_training_data" / "episodes").exists():
        episodes_root = here.parent / "rl_training_data" / "episodes"
    else:
        print("ERROR: Cannot find episodes/", file=sys.stderr)
        sys.exit(1)

    print(f"Loading from: {episodes_root}", flush=True)
    data = load_all(episodes_root)
    report = build_report(data)
    text = "\n".join(report)
    out = here / args.output
    out.write_text(text, encoding="utf-8")
    print(f"Written: {out}  ({len(report)} lines)")


if __name__ == "__main__":
    main()
