"""
Simulate reducing from 6 presets to 4 presets and measure the impact on
GRPO section-level signal quality.

Scenarios evaluated
───────────────────
  6P  (baseline): {P0, P1, P2, P3, P4, P5}
  4A            : {P0, P1, P2, P4}   (keep "balanced→depth" for nr=2 and nr=3)
  4B            : {P0, P1, P3, P5}   (keep "depth→breadth"  for nr=2 and nr=3)

Signal quality metrics (per section)
─────────────────────────────────────
  oracle_gap     : max_R − second_max_R
  is_quality_live: oracle_gap > cost_only_margin  [quality does work beyond cost]
  quality_spread : max_quality − min_quality       (pure quality, no cost term)
  is_quality_flat: quality_spread == 0             (cost is the ONLY differentiator)
  grpo_advantage_spread : max_adv − min_adv within the group
     (proxy for how much gradient signal GRPO gets per section)

All stats broken out by variant and article, then aggregated.
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev

# ──────────────────────────────────────────────────────────────────────────────
EPISODES_ROOT = Path(__file__).parent / "episodes"
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

# preset_id → nr_rounds used in cost penalty
PRESET_ROUNDS_6P = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}

# ──────────────────────────────────────────────────────────────────────────────
# Reward formula (mirrors train_grpo.py)
# ──────────────────────────────────────────────────────────────────────────────
def compute_reward(scores: dict, preset_id: int, nr: int, variant: str) -> float:
    cc = scores.get("cc", 0.0); fl = scores.get("fl", 0.0)
    de = scores.get("de", 0.0); be = scores.get("be", 0.0)
    cp = scores.get("cp", 0.0); ga = scores.get("ga", 0.0)
    ra = scores.get("ra", 0.0)
    if variant == "minimal":
        return 0.05*cc + 0.05*fl + 0.80*ga + 0.10*ra - 0.02*nr
    if variant == "demanding":
        return (0.12*cc + 0.08*fl
                + cp*(0.55*de + 0.35*be)*0.50
                + (0.60*ga + 0.40*ra)*0.25
                - 0.005*nr)
    return (0.20*cc + 0.20*fl
            + cp*(0.60*de + 0.40*be)*0.30
            + (0.50*ga + 0.50*ra)*0.30
            - 0.02*nr)


def quality_only(scores: dict, variant: str) -> float:
    """Reward without the cost penalty (nr=0)."""
    return compute_reward(scores, preset_id=0, nr=0, variant=variant)


def cost_only_margin(variant: str) -> float:
    """Max reward difference attributable purely to nr cost, across nr in {0,1,2,3}."""
    rate = 0.005 if variant == "demanding" else 0.02
    return rate * 3   # max_nr – min_nr = 3


# ──────────────────────────────────────────────────────────────────────────────
# Episode loading (mirrors _analyze_oracle_margins.py)
# ──────────────────────────────────────────────────────────────────────────────
_REASONING_KEYS_ORDERED = [
    "ground_truth_core_content", "ground_truth_flow", "ground_truth_structure",
    "ground_truth_depth_enhancement", "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation", "user_intent_guideline_adherence",
    "user_intent_research_anchoring", "user_intent_golden_source_priority",
]
REWARD_DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
}


def _parse_section_scores(text: str) -> dict[str, int]:
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


def load_episode(ep_dir: Path) -> dict[str, dict[str, int]] | None:
    path = ep_dir / "reasoning.json"
    if not path.exists():
        return None
    raw = path.read_text(encoding="utf-8", errors="replace")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = _extract_reasoning_tolerant(raw)
        if not data:
            return None
    return {short: _parse_section_scores(data.get(key, ""))
            for short, key in REWARD_DIMS.items()}


# ──────────────────────────────────────────────────────────────────────────────
# Core analysis
# ──────────────────────────────────────────────────────────────────────────────
SCENARIOS = {
    "6P": [0, 1, 2, 3, 4, 5],
    "4A": [0, 1, 2, 4],   # keep P2 (balanced→depth), P4 (balanced→depth→breadth)
    "4B": [0, 1, 3, 5],   # keep P3 (depth→breadth),  P5 (depth→breadth→depth)
}

# For 4-preset scenarios the cost nr is still the actual round count
# {preset_id: nr_rounds} from PRESET_ROUNDS_6P covers all cases


def _grpo_advantage_spread(rewards: list[float]) -> float:
    """max_advantage - min_advantage in a GRPO group.
    GRPO normalises: A_i = (R_i - mean) / std.
    Spread = max(A) - min(A) = (max(R) - min(R)) / std(R).
    """
    if len(rewards) < 2:
        return 0.0
    r_range = max(rewards) - min(rewards)
    try:
        s = stdev(rewards)
    except Exception:
        s = 0.0
    return (r_range / s) if s > 1e-9 else 0.0


def analyse_group(
    preset_data: dict[int, dict[str, dict[str, int]]],
    variant: str,
    scenario_presets: list[int],
) -> list[dict]:
    """
    preset_data[preset_id][dim_short][section_name] = 0|1
    Returns one dict per section.
    """
    # Collect all sections mentioned in any preset
    sections: set[str] = set()
    for pid in scenario_presets:
        ep = preset_data.get(pid, {})
        for dim_vals in ep.values():
            sections.update(dim_vals.keys())

    results = []
    for sec in sorted(sections):
        # Build per-preset score dict and reward
        preset_scores: dict[int, dict] = {}
        for pid in scenario_presets:
            ep = preset_data.get(pid, {})
            s = {dim: ep.get(dim, {}).get(sec, 0) for dim in REWARD_DIMS}
            preset_scores[pid] = s

        rewards = {
            pid: compute_reward(
                preset_scores[pid], pid, PRESET_ROUNDS_6P[pid], variant
            )
            for pid in scenario_presets
        }
        qualities = {
            pid: quality_only(preset_scores[pid], variant)
            for pid in scenario_presets
        }

        sorted_r = sorted(rewards.values(), reverse=True)
        oracle_gap   = sorted_r[0] - sorted_r[1] if len(sorted_r) >= 2 else 0.0
        q_max        = max(qualities.values())
        q_min        = min(qualities.values())
        q_spread     = q_max - q_min
        com          = cost_only_margin(variant)
        adv_spread   = _grpo_advantage_spread(list(rewards.values()))

        oracle_pid   = max(rewards, key=rewards.__getitem__)

        results.append({
            "section":        sec,
            "oracle_pid":     oracle_pid,
            "oracle_gap":     oracle_gap,
            "is_quality_live": oracle_gap > com,
            "is_quality_flat": q_spread < 1e-9,
            "q_spread":       q_spread,
            "adv_spread":     adv_spread,
            "rewards":        rewards,
        })
    return results


# ──────────────────────────────────────────────────────────────────────────────
# Load all episodes
# ──────────────────────────────────────────────────────────────────────────────
def load_all():
    """Returns data[article][variant][preset] = episode_dim_dict"""
    data = defaultdict(lambda: defaultdict(dict))
    for article in ARTICLES:
        for variant in VARIANTS:
            for preset in range(6):
                ep_dir = EPISODES_ROOT / f"{article}__{variant}__preset{preset}"
                ep = load_episode(ep_dir)
                if ep:
                    data[article][variant][preset] = ep
    return data


# ──────────────────────────────────────────────────────────────────────────────
# Reporting helpers
# ──────────────────────────────────────────────────────────────────────────────
def _fmt_pct(n, d):
    return f"{100*n/d:5.1f}%" if d else "  n/a"


def print_scenario_summary(label: str, all_sections: list[dict], variant_tag: str = "all"):
    n = len(all_sections)
    if n == 0:
        print(f"  {label}: no data")
        return
    live       = sum(s["is_quality_live"] for s in all_sections)
    flat       = sum(s["is_quality_flat"] for s in all_sections)
    gap_0      = sum(s["oracle_gap"] < 1e-9 for s in all_sections)
    gaps       = [s["oracle_gap"] for s in all_sections]
    adv_spr    = [s["adv_spread"] for s in all_sections if s["adv_spread"] > 1e-9]

    print(f"  {label:<4}  n={n:4d}  "
          f"live={_fmt_pct(live,n)}  "
          f"quality-flat={_fmt_pct(flat,n)}  "
          f"gap=0={_fmt_pct(gap_0,n)}  "
          f"mean_gap={mean(gaps):.4f}  "
          f"adv_spread={mean(adv_spr):.3f}" if adv_spr else
          f"  {label:<4}  n={n:4d}  "
          f"live={_fmt_pct(live,n)}  "
          f"quality-flat={_fmt_pct(flat,n)}  "
          f"gap=0={_fmt_pct(gap_0,n)}  "
          f"mean_gap={mean(gaps):.4f}  "
          f"adv_spread=n/a")


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────
def main():
    out = sys.stdout
    data = load_all()

    # Accumulate sections by (scenario_label, variant)
    bucket: dict[tuple[str, str], list[dict]] = defaultdict(list)
    # Also by (scenario_label, article, variant) for per-article breakdown
    art_bucket: dict[tuple[str, str, str], list[dict]] = defaultdict(list)

    for article in ARTICLES:
        for variant in VARIANTS:
            v_short = variant.split("_")[1]  # minimal / standard / demanding
            preset_data = data[article][variant]
            if not preset_data:
                continue
            for scen_label, scen_presets in SCENARIOS.items():
                # Only include sections present in ALL presets of this scenario
                sections = analyse_group(preset_data, v_short, scen_presets)
                bucket[(scen_label, variant)].extend(sections)
                art_bucket[(scen_label, article, variant)].extend(sections)

    # ── PART 1: Global summary by scenario × variant ──────────────────────
    print("=" * 100)
    print("PART 1: Signal quality summary by scenario × variant")
    print()
    print("  Columns:")
    print("    live          = oracle_gap > cost_only_margin  (quality beats max-cost signal)")
    print("    quality-flat  = all presets have identical quality score (cost is ONLY signal)")
    print("    gap=0         = oracle ties runner-up (zero differentiation)")
    print("    mean_gap      = mean(oracle − runner-up) across sections")
    print("    adv_spread    = mean GRPO advantage spread = (max_R − min_R) / σ_R per section")
    print("=" * 100)

    for variant in VARIANTS:
        print(f"\n[{variant}]")
        for scen_label in SCENARIOS:
            secs = bucket[(scen_label, variant)]
            print_scenario_summary(scen_label, secs)

    # ── PART 2: Global summary pooled across variants ──────────────────────
    print()
    print("=" * 100)
    print("PART 2: Pooled across all variants")
    print("=" * 100)
    for scen_label in SCENARIOS:
        all_secs = []
        for variant in VARIANTS:
            all_secs.extend(bucket[(scen_label, variant)])
        print_scenario_summary(scen_label, all_secs, "all")

    # ── PART 3: Per-article breakdown (4A vs 6P, delta) ───────────────────
    print()
    print("=" * 100)
    print("PART 3: Per-article live-section fraction — 6P vs 4A vs 4B")
    print("=" * 100)
    header = f"{'Article':<35} {'Variant':<15}  {'6P live%':>9}  {'4A live%':>9}  {'4B live%':>9}  {'Δ(4A-6P)':>9}  {'Δ(4B-6P)':>9}"
    print(header)
    print("-" * len(header))
    for article in ARTICLES:
        for variant in VARIANTS:
            def pct(secs):
                if not secs: return 0.0
                return 100 * sum(s["is_quality_live"] for s in secs) / len(secs)
            p6  = pct(art_bucket[("6P", article, variant)])
            p4a = pct(art_bucket[("4A", article, variant)])
            p4b = pct(art_bucket[("4B", article, variant)])
            print(f"{article:<35} {variant:<15}  {p6:>8.1f}%  {p4a:>8.1f}%  {p4b:>8.1f}%  "
                  f"{p4a-p6:>+8.1f}%  {p4b-p6:>+8.1f}%")

    # ── PART 4: Oracle-gap distribution histogram ──────────────────────────
    print()
    print("=" * 100)
    print("PART 4: Oracle-gap distribution — 6P vs 4A vs 4B  (pooled all variants)")
    print("  gap=0 | (0,0.01] | (0.01,0.03] | (0.03,0.06] | (0.06,0.10] | >0.10")
    print("=" * 100)
    BINS = [0.0, 0.001, 0.01, 0.03, 0.06, 0.10, float("inf")]
    BIN_LABELS = ["=0", "(0,0.01]", "(0.01,0.03]", "(0.03,0.06]", "(0.06,0.10]", ">0.10"]

    for scen_label in SCENARIOS:
        all_secs = []
        for variant in VARIANTS:
            all_secs.extend(bucket[(scen_label, variant)])
        gaps = [s["oracle_gap"] for s in all_secs]
        n = len(gaps)
        counts = [0] * len(BIN_LABELS)
        for g in gaps:
            for bi in range(len(BIN_LABELS)):
                lo = BINS[bi]; hi = BINS[bi+1]
                if lo < 1e-9:  # gap=0 bin
                    if g < 1e-9:
                        counts[bi] += 1; break
                else:
                    if lo < g <= hi:
                        counts[bi] += 1; break
        row = "  ".join(f"{BIN_LABELS[i]}:{counts[i]:3d}({100*counts[i]/n:.0f}%)"
                        for i in range(len(BIN_LABELS)))
        print(f"  {scen_label}  {row}")

    # ── PART 5: Oracle preset distribution (who wins most?) ───────────────
    print()
    print("=" * 100)
    print("PART 5: Oracle preset distribution (which preset wins each section?)")
    print("  Shows whether higher presets dominate — healthy if P_max_rounds wins most")
    print("=" * 100)
    for scen_label, scen_presets in SCENARIOS.items():
        all_secs = []
        for variant in VARIANTS:
            all_secs.extend(bucket[(scen_label, variant)])
        n = len(all_secs)
        from collections import Counter
        dist = Counter(s["oracle_pid"] for s in all_secs)
        parts = "  ".join(f"P{p}:{dist[p]:3d}({100*dist[p]/n:.0f}%)"
                           for p in scen_presets)
        print(f"  {scen_label}  {parts}")

    # ── PART 6: P2/P3 and P4/P5 tie analysis (root cause confirmation) ────
    print()
    print("=" * 100)
    print("PART 6: Tied-pair analysis — how often P2=P3 and P4=P5 (in 6P scenario)")
    print("  A tie means R(Pi) = R(Pj) → zero gradient from that pair in GRPO")
    print("=" * 100)
    tie_counts = {"P2=P3": 0, "P4=P5": 0, "both": 0, "neither": 0}
    total_6p = 0
    for variant in VARIANTS:
        for sec_dict in bucket[("6P", variant)]:
            r = sec_dict["rewards"]
            t23 = abs(r.get(2, 0) - r.get(3, 0)) < 1e-9
            t45 = abs(r.get(4, 0) - r.get(5, 0)) < 1e-9
            if t23 and t45:
                tie_counts["both"] += 1
            elif t23:
                tie_counts["P2=P3"] += 1
            elif t45:
                tie_counts["P4=P5"] += 1
            else:
                tie_counts["neither"] += 1
            total_6p += 1
    n = total_6p
    for k, v in tie_counts.items():
        print(f"  {k:<10}: {v:4d} / {n}  ({100*v/n:.1f}%)")
    tied_total = tie_counts["P2=P3"] + tie_counts["P4=P5"] + tie_counts["both"]
    print(f"  {'any tie':<10}: {tied_total:4d} / {n}  ({100*tied_total/n:.1f}%)  "
          f"← fraction of sections with at least one wasted pair")

    # ── PART 7: Effective pairwise comparisons ─────────────────────────────
    print()
    print("=" * 100)
    print("PART 7: Effective pairwise comparisons per scenario")
    print("  C(k,2) total pairs; minus tied pairs = effective signal pairs")
    print("=" * 100)
    from itertools import combinations
    for scen_label, scen_presets in SCENARIOS.items():
        k = len(scen_presets)
        total_pairs = k * (k - 1) // 2
        all_secs = []
        for variant in VARIANTS:
            all_secs.extend(bucket[(scen_label, variant)])
        tied_pairs = 0
        total_section_pairs = len(all_secs) * total_pairs
        for sec_dict in all_secs:
            r = sec_dict["rewards"]
            for pi, pj in combinations(scen_presets, 2):
                if abs(r.get(pi, 0) - r.get(pj, 0)) < 1e-9:
                    tied_pairs += 1
        eff = total_section_pairs - tied_pairs
        print(f"  {scen_label}  k={k}  C(k,2)={total_pairs}  "
              f"section×pairs={total_section_pairs}  "
              f"tied_pairs={tied_pairs}({100*tied_pairs/total_section_pairs:.1f}%)  "
              f"effective={eff}({100*eff/total_section_pairs:.1f}%)")


if __name__ == "__main__":
    main()
