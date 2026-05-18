"""
Section-level reward margin analysis (8 articles × 3 variants × 6 presets).

For every section in every episode group, applies the variant-dependent
compute_reward() formula from train_grpo.py to the 6 per-preset binary
oracle vectors, then characterises the resulting reward distribution and
its decomposition into cost-driven vs oracle-driven components.

Usage (from rl_training_data/ or writing_workflow/):
    python3 _analyze_reward_margins.py
    python3 _analyze_reward_margins.py --output margins.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev, median

# ---------------------------------------------------------------------------
# Config
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
VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
N_PRESETS = 6

# Dimensions referenced in the reward formula (from train_grpo.py _REWARD_DIMS).
# NOTE: ground_truth_structure and user_intent_golden_source_priority are
# intentionally excluded from the formula even though they exist in the oracle.
REWARD_DIMS = {
    "cc":  "ground_truth_core_content",
    "fl":  "ground_truth_flow",
    "de":  "ground_truth_depth_enhancement",
    "be":  "ground_truth_breadth_enhancement",
    "cp":  "ground_truth_core_preservation",
    "ga":  "user_intent_guideline_adherence",
    "ra":  "user_intent_research_anchoring",
}
ALL_DIMS = {
    **REWARD_DIMS,
    "st":  "ground_truth_structure",
    "gsp": "user_intent_golden_source_priority",
}

# Preset → exploration-round count (from train_grpo.py).
PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}

# ---------------------------------------------------------------------------
# Reward formula (replicated from train_grpo.py compute_reward)
# ---------------------------------------------------------------------------
def compute_reward(scores: dict[str, float], preset_id: int, variant: str) -> float:
    cc = scores.get("cc", 0.0)
    fl = scores.get("fl", 0.0)
    de = scores.get("de", 0.0)
    be = scores.get("be", 0.0)
    cp = scores.get("cp", 0.0)
    ga = scores.get("ga", 0.0)
    ra = scores.get("ra", 0.0)
    nr = PRESET_ROUNDS[preset_id]

    if variant == "minimal":
        gt_base     = 0.05 * cc + 0.05 * fl
        explore     = 0.0
        user_intent = 0.80 * ga + 0.10 * ra
        cost        = -0.02 * nr
    elif variant == "demanding":
        gt_base     = 0.12 * cc + 0.08 * fl
        explore     = cp * (0.55 * de + 0.35 * be) * 0.50
        user_intent = (0.60 * ga + 0.40 * ra) * 0.25
        cost        = -0.005 * nr
    else:  # standard
        gt_base     = 0.20 * cc + 0.20 * fl
        explore     = cp * (0.60 * de + 0.40 * be) * 0.30
        user_intent = (0.50 * ga + 0.50 * ra) * 0.30
        cost        = -0.02 * nr

    return gt_base + explore + user_intent + cost


# ---------------------------------------------------------------------------
# Cost-only baseline margin (all oracles held constant, only cost varies)
# ---------------------------------------------------------------------------
def cost_only_margin(variant: str) -> float:
    """Max reward spread achievable from cost alone (presets 0 vs 4/5)."""
    nr_vals = sorted(set(PRESET_ROUNDS.values()))  # [0, 1, 2, 3]
    cost_rate = 0.005 if variant == "demanding" else 0.02
    return cost_rate * (max(nr_vals) - min(nr_vals))   # = 0.015 or 0.060


# ---------------------------------------------------------------------------
# JSON parsing helpers (copied from _analyze_section_signals.py)
# ---------------------------------------------------------------------------
_REASONING_KEYS_ORDERED = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_structure",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
    "user_intent_golden_source_priority",
]

def _extract_reasoning_tolerant(raw: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for i, key in enumerate(_REASONING_KEYS_ORDERED):
        m = re.search(f'"{re.escape(key)}"\\s*:\\s*"', raw)
        if not m:
            continue
        vs = m.end()
        if i + 1 < len(_REASONING_KEYS_ORDERED):
            nm = re.search(
                f'"{re.escape(_REASONING_KEYS_ORDERED[i+1])}"\\s*:', raw[vs:]
            )
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
    return {
        short: parse_section_scores(data.get(key, ""))
        for short, key in ALL_DIMS.items()
    }


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def ep_path(root: Path, article: str, variant: str, preset: int) -> Path:
    return root / f"{article}__{variant}__preset{preset}"


def load_all(episodes_root: Path):
    """Return nested: data[article][variant][section_title][dim_short][preset] = 0|1|None"""
    data = {}
    for article in ARTICLES:
        data[article] = {}
        for variant in VARIANTS:
            sec_data: dict[str, dict[str, list]] = defaultdict(
                lambda: {d: [None] * N_PRESETS for d in ALL_DIMS}
            )
            for preset in range(N_PRESETS):
                ep = ep_path(episodes_root, article, variant, preset)
                reasoning = load_episode(ep)
                if reasoning is None:
                    continue
                # Use cc sections as canonical section list
                for sec, sc in reasoning.get("cc", {}).items():
                    for d in ALL_DIMS:
                        sec_data[sec][d][preset] = reasoning[d].get(sec)
                # UI dims may name sections differently; add them too
                for d in ("ga", "ra", "gsp"):
                    for sec, sc in reasoning.get(d, {}).items():
                        if sec not in sec_data:
                            for d2 in ALL_DIMS:
                                sec_data[sec][d2] = [None] * N_PRESETS
                        sec_data[sec][d][preset] = sc
            data[article][variant] = dict(sec_data)
    return data


# ---------------------------------------------------------------------------
# Per-section reward computation
# ---------------------------------------------------------------------------
def section_rewards(
    oracle_profile: dict[str, list],   # dim → [v0..v5] (0|1|None)
    variant: str,
) -> list[float | None]:
    """Compute reward for each preset given binary oracle vectors per dim."""
    rewards = []
    for p in range(N_PRESETS):
        scores = {}
        for d in REWARD_DIMS:
            v = oracle_profile[d][p]
            scores[d] = float(v) if v is not None else 0.0
        rewards.append(compute_reward(scores, p, variant))
    return rewards


def margin_stats(rewards: list[float]) -> dict:
    """Compute margin (max-min), regret (max-mean), std, mean for a reward list."""
    valid = [r for r in rewards if r is not None]
    if not valid:
        return {}
    mx = max(valid)
    mn = min(valid)
    avg = mean(valid)
    sd = stdev(valid) if len(valid) > 1 else 0.0
    return {
        "max": mx,
        "min": mn,
        "mean": avg,
        "std": sd,
        "margin": mx - mn,
        "regret": mx - avg,
        "best_preset": rewards.index(mx),
    }


# ---------------------------------------------------------------------------
# Oracle variation helpers
# ---------------------------------------------------------------------------
def oracle_varies(vals: list) -> bool:
    """Return True if the dim shows at least 2 different values across presets."""
    non_null = [v for v in vals if v is not None]
    return len(set(non_null)) > 1 if len(non_null) >= 2 else False


def oracle_mean(vals: list) -> float | None:
    non_null = [v for v in vals if v is not None]
    return mean(non_null) if non_null else None


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
SEP = "=" * 80
SEP2 = "-" * 80


def build_report(data: dict) -> list[str]:
    lines: list[str] = []

    def w(*args):
        lines.append(" ".join(str(a) for a in args))

    def wl():
        lines.append("")

    # ------------------------------------------------------------------ #
    # HEADER                                                               #
    # ------------------------------------------------------------------ #
    w(SEP)
    w("SECTION-LEVEL REWARD MARGIN ANALYSIS")
    w("8 articles × 3 variants × 6 presets")
    w(SEP)
    wl()

    # ------------------------------------------------------------------ #
    # PART 0: Formula Reference                                            #
    # ------------------------------------------------------------------ #
    w("PART 0: Reward Formula Reference")
    w(SEP2)
    w("MINIMAL  : R = 0.05·cc + 0.05·fl + 0.80·ga + 0.10·ra - 0.02·nr")
    w("           (explore = 0: de/be not used for brief conceptual articles)")
    w("STANDARD : R = 0.20·cc + 0.20·fl + cp·(0.60·de + 0.40·be)·0.30")
    w("               + (0.50·ga + 0.50·ra)·0.30 - 0.02·nr")
    w("DEMANDING: R = 0.12·cc + 0.08·fl + cp·(0.55·de + 0.35·be)·0.50")
    w("               + (0.60·ga + 0.40·ra)·0.25 - 0.005·nr")
    wl()
    w("Preset rounds: P0=0, P1=1, P2=2, P3=2, P4=3, P5=3")
    w("Cost-only margin (fixed oracles, cost variation only):")
    w("  minimal/standard : 0.02 × (3-0) = 0.060")
    w("  demanding        : 0.005 × (3-0) = 0.015")
    wl()
    w("NOTE: ground_truth_structure (st) and user_intent_golden_source_priority (gsp)")
    w("      are NOT used in any reward formula — pure oracle data, no gradient signal.")
    wl()
    w("Theoretical max/min per variant (all binary dims = 1 or 0, preset = P0/P5):")
    # Compute theoretical extremes
    for var in VARIANTS:
        label = var.replace("var_", "").upper()
        all_ones = {d: 1.0 for d in REWARD_DIMS}
        all_zeros = {d: 0.0 for d in REWARD_DIMS}
        max_r = compute_reward(all_ones, 0, var.replace("var_", ""))
        min_r = compute_reward(all_zeros, 5, var.replace("var_", ""))
        w(f"  {label:10s}: max={max_r:.4f} (all=1, P0), min={min_r:.4f} (all=0, P5),"
          f" theoretical range={max_r - min_r:.4f}")
    wl()

    # ------------------------------------------------------------------ #
    # PART 1: Per-dim oracle variation rates                               #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 1: Oracle Variation Rates — % of sections where each dim varies")
    w("        across the 6 presets (at least one preset differs from others)")
    w(SEP2)
    wl()

    # Collect oracle variation counts per dim per variant
    dim_vary_count: dict[str, dict[str, int]] = {
        var: {d: 0 for d in REWARD_DIMS} for var in VARIANTS
    }
    dim_total: dict[str, int] = {var: 0 for var in VARIANTS}
    dim_means: dict[str, dict[str, list[float]]] = {
        var: {d: [] for d in REWARD_DIMS} for var in VARIANTS
    }

    for article in ARTICLES:
        for variant in VARIANTS:
            for sec, profile in data[article][variant].items():
                dim_total[variant] += 1
                for d in REWARD_DIMS:
                    m = oracle_mean(profile[d])
                    if m is not None:
                        dim_means[variant][d].append(m)
                    if oracle_varies(profile[d]):
                        dim_vary_count[variant][d] += 1

    # Table header
    w(f"{'Dim':<6} {'Weight(min)':<12} {'Weight(std)':<12} {'Weight(dem)':<12}"
      f" | {'Vary%(min)':<11} {'Vary%(std)':<11} {'Vary%(dem)':<11}"
      f" | {'Mean(min)':<10} {'Mean(std)':<10} {'Mean(dem)':<10}")
    w("-" * 110)

    weights = {
        "minimal":  {"cc": 0.05, "fl": 0.05, "de": 0.00, "be": 0.00,
                     "cp": 0.00, "ga": 0.80, "ra": 0.10},
        "standard": {"cc": 0.20, "fl": 0.20, "de": "0.18*cp", "be": "0.12*cp",
                     "cp": "gating", "ga": 0.15, "ra": 0.15},
        "demanding":{"cc": 0.12, "fl": 0.08, "de": "0.275*cp","be": "0.175*cp",
                     "cp": "gating", "ga": 0.15, "ra": 0.10},
    }
    weight_str = {
        "minimal":  {"cc":"0.05","fl":"0.05","de":"0.00","be":"0.00",
                     "cp":"0.00","ga":"0.80","ra":"0.10"},
        "standard": {"cc":"0.20","fl":"0.20","de":"0.18×cp","be":"0.12×cp",
                     "cp":"gate","ga":"0.15","ra":"0.15"},
        "demanding":{"cc":"0.12","fl":"0.08","de":"0.275×cp","be":"0.175×cp",
                     "cp":"gate","ga":"0.15","ra":"0.10"},
    }

    for d in REWARD_DIMS:
        wmin = weight_str["minimal"][d]
        wstd = weight_str["standard"][d]
        wdem = weight_str["demanding"][d]
        totals = [dim_total[v] for v in VARIANTS]
        vary_pcts = [
            100 * dim_vary_count[v][d] / dim_total[v] if dim_total[v] else 0
            for v in VARIANTS
        ]
        means_ = [
            mean(dim_means[v][d]) if dim_means[v][d] else float("nan")
            for v in VARIANTS
        ]
        w(f"  {d:<4} {wmin:>12} {wstd:>12} {wdem:>12}"
          f" | {vary_pcts[0]:>9.1f}%  {vary_pcts[1]:>9.1f}%  {vary_pcts[2]:>9.1f}% "
          f" | {means_[0]:>9.3f}  {means_[1]:>9.3f}  {means_[2]:>9.3f}")
    wl()

    # ------------------------------------------------------------------ #
    # PART 2: Reward margin distribution per variant                       #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 2: Reward Margin Distribution by Variant")
    w("        margin = max(R_P0..P5) - min(R_P0..P5) per section group")
    w(SEP2)
    wl()

    # Collect all section margins per variant
    all_margins: dict[str, list[float]] = {v: [] for v in VARIANTS}
    all_regrets: dict[str, list[float]] = {v: [] for v in VARIANTS}
    oracle_driven: dict[str, int] = {v: 0 for v in VARIANTS}
    cost_only_n: dict[str, int] = {v: 0 for v in VARIANTS}

    # Also store per-article per-variant per-section data for Part 4
    detail: dict = {}  # article → variant → list[(sec, rewards, stats, oracle_flags)]

    for article in ARTICLES:
        detail[article] = {}
        for variant in VARIANTS:
            detail[article][variant] = []
            var_key = variant.replace("var_", "")
            co_margin = cost_only_margin(var_key)

            for sec, profile in data[article][variant].items():
                rewards_list = section_rewards(profile, var_key)
                stats = margin_stats(rewards_list)
                if not stats:
                    continue
                mg = stats["margin"]
                all_margins[variant].append(mg)
                all_regrets[variant].append(stats["regret"])
                is_oracle = mg > co_margin + 1e-6
                if is_oracle:
                    oracle_driven[variant] += 1
                else:
                    cost_only_n[variant] += 1
                # Oracle variation flags per dim
                flags = {d: oracle_varies(profile[d]) for d in REWARD_DIMS}
                detail[article][variant].append(
                    (sec, rewards_list, stats, flags, profile)
                )

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        label = var_key.upper()
        mgs = sorted(all_margins[variant])
        regs = sorted(all_regrets[variant])
        total_secs = len(mgs)
        co = cost_only_margin(var_key)

        w(f"  [{label}]  cost-only baseline margin = {co:.4f}")
        if total_secs == 0:
            w("    (no data)")
            continue

        dead = sum(1 for m in mgs if m <= co + 1e-6)
        live = total_secs - dead

        def pct(n): return f"{100*n/total_secs:.1f}%"

        w(f"  Total sections : {total_secs}")
        w(f"  Dead (margin ≤ cost-only baseline)  : {dead:3d}  ({pct(dead)})")
        w(f"  Live (oracle-driven margin)          : {live:3d}  ({pct(live)})")
        wl()

        # Percentile table
        def ptile(lst, p): return lst[min(int(p / 100 * len(lst)), len(lst) - 1)]
        w(f"  Margin distribution (max-min reward across 6 presets):")
        w(f"  {'Stat':<10} {'Margin':>10} {'Regret':>10}")
        w(f"  {'-'*32}")
        for stat, lst in (("Min", mgs), ("P10", mgs), ("P25", mgs), ("Median", mgs),
                           ("P75", mgs), ("P90", mgs), ("Max", mgs)):
            ps = {"Min":0,"P10":10,"P25":25,"Median":50,"P75":75,"P90":90,"Max":100}
            mv = ptile(lst, ps[stat])
            rv = ptile(sorted(all_regrets[variant]), ps[stat])
            w(f"  {stat:<10} {mv:>10.4f} {rv:>10.4f}")
        w(f"  Mean           {mean(mgs):>10.4f} {mean(all_regrets[variant]):>10.4f}")
        wl()

        # Margin buckets
        buckets = [(0, 0.01), (0.01, 0.06), (0.06, 0.10), (0.10, 0.20), (0.20, 1.01)]
        w(f"  Margin bucket distribution:")
        for lo, hi in buckets:
            cnt = sum(1 for m in mgs if lo <= m < hi)
            label2 = f"[{lo:.2f}, {hi:.2f})"
            bar = "#" * int(40 * cnt / total_secs)
            w(f"    {label2}  {cnt:3d} ({pct(cnt)})  {bar}")
        wl()

    # ------------------------------------------------------------------ #
    # PART 3: Oracle-driven vs cost-only breakdown per article             #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 3: Oracle-driven vs Cost-only breakdown per Article × Variant")
    w(SEP2)
    wl()

    w(f"  {'Article':<35} {'Variant':<12} {'Total':>6} {'Live':>6} {'Dead':>6} "
      f"{'LivePct':>8} {'MeanMargin':>11} {'MeanRegret':>11}")
    w("  " + "-" * 105)
    for article in ARTICLES:
        for v_idx, variant in enumerate(VARIANTS):
            var_key = variant.replace("var_", "")
            co = cost_only_margin(var_key)
            rows = detail[article][variant]
            total = len(rows)
            live = sum(1 for _, _, s, _, _ in rows if s.get("margin", 0) > co + 1e-6)
            dead = total - live
            margins = [s.get("margin", 0) for _, _, s, _, _ in rows]
            regrets = [s.get("regret", 0) for _, _, s, _, _ in rows]
            avg_m = mean(margins) if margins else 0.0
            avg_r = mean(regrets) if regrets else 0.0
            pct_live = 100 * live / total if total else 0
            art_label = article if v_idx == 0 else ""
            w(f"  {art_label:<35} {var_key:<12} {total:>6} {live:>6} {dead:>6} "
              f"{pct_live:>7.1f}% {avg_m:>11.4f} {avg_r:>11.4f}")
        w("")

    # ------------------------------------------------------------------ #
    # PART 4: Per-article per-section per-variant full margin table        #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 4: Per-Section Reward Margins (all articles, all variants)")
    w("        Columns: section title | oracle means per dim (cc fl de be cp ga ra)")
    w("        | live dims | rewards P0-P5 | margin | regret | best preset")
    w("        Live dim: dim has >0 oracle variation across 6 presets")
    w("        Oracle mean shown as fraction of 6 presets where score=1")
    w(SEP2)
    wl()

    REWARD_DIM_ORDER = ["cc", "fl", "de", "be", "cp", "ga", "ra"]

    for article in ARTICLES:
        w(f"  === {article} ===")
        for variant in VARIANTS:
            var_key = variant.replace("var_", "")
            co = cost_only_margin(var_key)
            rows = detail[article][variant]
            if not rows:
                w(f"    [{var_key.upper()}] — no sections loaded")
                continue

            w(f"    [{var_key.upper()}]  cost-only baseline = {co:.4f}")
            # Header row
            w(f"    {'Section':<45} "
              f"{'cc':>4} {'fl':>4} {'de':>4} {'be':>4} {'cp':>4} {'ga':>4} {'ra':>4}  "
              f"{'Live dims':<18}  "
              f"{'P0':>6} {'P1':>6} {'P2':>6} {'P3':>6} {'P4':>6} {'P5':>6}  "
              f"{'margin':>7} {'regret':>7} {'best':>5}")
            w("    " + "-" * 165)

            for sec, rewards_list, stats, flags, profile in rows:
                dim_means_row = {
                    d: oracle_mean(profile[d]) for d in REWARD_DIM_ORDER
                }
                live_dims = " ".join(d for d in REWARD_DIM_ORDER if flags.get(d))
                r_strs = " ".join(f"{r:6.4f}" for r in rewards_list)
                mg = stats.get("margin", 0)
                rg = stats.get("regret", 0)
                bp = stats.get("best_preset", -1)
                # Marker for oracle-driven sections
                marker = " *" if mg > co + 1e-6 else "  "
                # Dim mean string (show as 0.0–1.0, - if None)
                dm_strs = " ".join(
                    f"{dim_means_row[d]:4.2f}" if dim_means_row[d] is not None else "  - "
                    for d in REWARD_DIM_ORDER
                )
                sec_label = (sec[:44] + "…") if len(sec) > 45 else sec
                w(f"  {marker} {sec_label:<45} "
                  f"{dm_strs}  "
                  f"{live_dims:<18}  "
                  f"{r_strs}  "
                  f"{mg:7.4f} {rg:7.4f} P{bp}")

            # Summary line
            total = len(rows)
            n_live = sum(1 for _, _, s, _, _ in rows if s.get("margin", 0) > co + 1e-6)
            margins_here = [s.get("margin", 0) for _, _, s, _, _ in rows]
            regrets_here = [s.get("regret", 0) for _, _, s, _, _ in rows]
            w(f"    → Live: {n_live}/{total}  mean margin={mean(margins_here):.4f}"
              f"  mean regret={mean(regrets_here):.4f}")
            wl()

    # ------------------------------------------------------------------ #
    # PART 5: Most "alive" and "dead" sections globally                    #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 5: Top-20 sections by reward margin (most GRPO-informative)")
    w(SEP2)
    wl()

    all_sections_data = []
    for article in ARTICLES:
        for variant in VARIANTS:
            var_key = variant.replace("var_", "")
            co = cost_only_margin(var_key)
            for sec, rewards_list, stats, flags, profile in detail[article][variant]:
                mg = stats.get("margin", 0)
                rg = stats.get("regret", 0)
                live_dims = [d for d in REWARD_DIM_ORDER if flags.get(d)]
                all_sections_data.append((mg, rg, article, var_key, sec, live_dims, rewards_list))

    top20 = sorted(all_sections_data, key=lambda x: x[0], reverse=True)[:20]
    w(f"  {'#':<4} {'Article+Variant':<44} {'Section':<48} {'Margin':>8} {'Regret':>8} {'Live dims'}")
    w("  " + "-" * 140)
    for i, (mg, rg, art, var_key, sec, ldims, _) in enumerate(top20, 1):
        av = f"{art}__{var_key}"[:43]
        sl = (sec[:47] + "…") if len(sec) > 48 else sec
        w(f"  {i:<4} {av:<44} {sl:<48} {mg:8.4f} {rg:8.4f} {' '.join(ldims)}")

    wl()
    w(SEP2)
    w("PART 6: Bottom-20 sections by reward margin (flattest / least informative)")
    w(SEP2)
    wl()

    bottom20 = sorted(all_sections_data, key=lambda x: x[0])[:20]
    w(f"  {'#':<4} {'Article+Variant':<44} {'Section':<48} {'Margin':>8} {'Regret':>8} {'Live dims'}")
    w("  " + "-" * 140)
    for i, (mg, rg, art, var_key, sec, ldims, rewards) in enumerate(bottom20, 1):
        av = f"{art}__{var_key}"[:43]
        sl = (sec[:47] + "…") if len(sec) > 48 else sec
        w(f"  {i:<4} {av:<44} {sl:<48} {mg:8.4f} {rg:8.4f} {' '.join(ldims) or '(none)'}")

    wl()

    # ------------------------------------------------------------------ #
    # PART 7: Variant-formula coefficient sensitivity                      #
    # ------------------------------------------------------------------ #
    w(SEP2)
    w("PART 7: Formula Sensitivity — marginal reward impact of each oracle dim")
    w("        Max possible reward delta when dim flips from 0→1 (other dims fixed)")
    w(SEP2)
    wl()

    w(f"  {'Dim':<6} {'minimal':>12} {'standard':>12} {'demanding':>14}  Notes")
    w("  " + "-" * 70)
    flip_notes = {
        "cc": "direct",
        "fl": "direct",
        "de": "gated by cp (max assumes cp=1)",
        "be": "gated by cp (max assumes cp=1)",
        "cp": "gate: controls de/be impact",
        "ga": "direct",
        "ra": "direct",
    }
    for d in REWARD_DIM_ORDER:
        deltas = {}
        for var in ("minimal", "standard", "demanding"):
            base = {d2: 0.0 for d2 in REWARD_DIMS}
            if d in ("de", "be"):
                base["cp"] = 1.0  # max sensitivity: cp gate open
            high = dict(base); high[d] = 1.0
            low  = dict(base)
            delta = compute_reward(high, 0, var) - compute_reward(low, 0, var)
            deltas[var] = delta
        w(f"  {d:<6} {deltas['minimal']:>12.4f} {deltas['standard']:>12.4f} "
          f"{deltas['demanding']:>14.4f}  {flip_notes.get(d, '')}")

    wl()
    w("  cp gate effect (setting cp=0 vs cp=1, de=be=1, P0):")
    for var in ("minimal", "standard", "demanding"):
        base_open  = {"cc":0,"fl":0,"de":1,"be":1,"cp":1,"ga":0,"ra":0}
        base_closed = {"cc":0,"fl":0,"de":1,"be":1,"cp":0,"ga":0,"ra":0}
        d_open  = compute_reward(base_open,  0, var)
        d_closed = compute_reward(base_closed, 0, var)
        w(f"    {var.upper():<12}: cp=1 → R={d_open:.4f},  cp=0 → R={d_closed:.4f},"
          f"  gate effect = {d_open - d_closed:.4f}")

    wl()
    w(SEP2)
    w("PART 8: GRPO signal quality summary (per variant)")
    w("        Sections where margin > cost-only baseline carry actual RL signal.")
    w("        Flat sections only teach the policy to minimise exploration cost.")
    w(SEP2)
    wl()

    for variant in VARIANTS:
        var_key = variant.replace("var_", "")
        co = cost_only_margin(var_key)
        mgs = all_margins[variant]
        regs = all_regrets[variant]
        total = len(mgs)
        if total == 0:
            continue
        dead = sum(1 for m in mgs if m <= co + 1e-6)
        live = total - dead
        live_mgs = [m for m in mgs if m > co + 1e-6]
        dead_mgs = [m for m in mgs if m <= co + 1e-6]

        w(f"  [{var_key.upper()}]")
        w(f"    Total section groups  : {total}")
        w(f"    Oracle-driven (live)  : {live}  ({100*live/total:.1f}%)")
        w(f"    Cost-only (dead)      : {dead}  ({100*dead/total:.1f}%)")
        if live_mgs:
            w(f"    Live  margin mean/max : {mean(live_mgs):.4f} / {max(live_mgs):.4f}")
        if dead_mgs:
            w(f"    Dead  margin mean/max : {mean(dead_mgs):.4f} / {max(dead_mgs):.4f}")
        w(f"    Overall regret mean   : {mean(regs):.4f}")
        wl()

        # Which dims drive live sections?
        dim_live_contrib = {d: 0 for d in REWARD_DIM_ORDER}
        for art in ARTICLES:
            for _, _, stats, flags, _ in detail[art][variant]:
                if stats.get("margin", 0) > co + 1e-6:
                    for d in REWARD_DIM_ORDER:
                        if flags.get(d):
                            dim_live_contrib[d] += 1
        w(f"    Dims driving live sections (times a dim varies in a live section):")
        for d, cnt in sorted(dim_live_contrib.items(), key=lambda x: -x[1]):
            if cnt > 0:
                w(f"      {d}: {cnt}")
        wl()

    return lines


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Section-level reward margin analysis")
    parser.add_argument("--output", default="_reward_margins_report.txt")
    args = parser.parse_args()

    # Auto-detect episodes root
    here = Path(__file__).resolve().parent
    if (here / "episodes").exists():
        episodes_root = here / "episodes"
    elif (here.parent / "rl_training_data" / "episodes").exists():
        episodes_root = here.parent / "rl_training_data" / "episodes"
    else:
        print("ERROR: Cannot find episodes/ directory", file=sys.stderr)
        sys.exit(1)

    print(f"Loading episodes from: {episodes_root}", flush=True)
    data = load_all(episodes_root)

    report = build_report(data)
    text = "\n".join(report)
    out = here / args.output
    out.write_text(text, encoding="utf-8")
    print(f"Report written to: {out}")
    print(f"Lines: {len(report)}")


if __name__ == "__main__":
    main()
