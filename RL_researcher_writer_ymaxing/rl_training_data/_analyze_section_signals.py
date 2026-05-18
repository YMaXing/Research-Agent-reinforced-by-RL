"""
Section-level signal analysis across all 144 variant episodes
(8 articles × 3 variants × 6 presets).

Parses reasoning.json for each episode, extracts per-section binary scores for
all 9 grading dimensions, then aggregates into a comprehensive report.

Run from writing_workflow/ or rl_training_data/ — it auto-detects the root.

Usage:
    python3 _analyze_section_signals.py
    python3 _analyze_section_signals.py --output report.txt
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

# GT dimensions (from reasoning.json keys)
GT_DIMS = {
    "cc": "ground_truth_core_content",
    "fl": "ground_truth_flow",
    "st": "ground_truth_structure",
    "de": "ground_truth_depth_enhancement",
    "be": "ground_truth_breadth_enhancement",
    "cp": "ground_truth_core_preservation",
}
# UI dimensions
UI_DIMS = {
    "ga": "user_intent_guideline_adherence",
    "ra": "user_intent_research_anchoring",
    "gsp": "user_intent_golden_source_priority",
}
ALL_DIMS = {**GT_DIMS, **UI_DIMS}

SHORT_LABELS = list(GT_DIMS.keys()) + list(UI_DIMS.keys())  # cc fl st de be cp ga ra gsp

# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def parse_section_scores(text: str) -> dict[str, int]:
    """
    Parse section-level binary scores from a reasoning.json dimension string.

    Expected format per section:
        SectionTitle:
        **N:** reasoning...

    Returns {section_title: score (0 or 1)}.
    """
    scores: dict[str, int] = {}
    lines = text.strip().split("\n")
    i = 0
    while i < len(lines):
        title_line = lines[i].strip()
        # A title line ends with ':' and is not a **score:** marker
        if title_line.endswith(":") and not title_line.startswith("**"):
            title = title_line[:-1].strip()
            # Look at next non-blank line for **N:**
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines):
                score_line = lines[j].strip()
                m = re.match(r"^\*\*([01])[:\*]", score_line)
                if m:
                    scores[title] = int(m.group(1))
                    i = j + 1
                    continue
        i += 1
    return scores


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
    """
    Fallback extractor for reasoning.json files with unescaped quotes.
    Extracts each known key's value by finding the text between consecutive
    key declarations, which avoids the unescaped-quote parsing problem.
    """
    result: dict[str, str] = {}
    keys = _REASONING_KEYS_ORDERED
    for i, key in enumerate(keys):
        pattern = f'"{re.escape(key)}"\\s*:\\s*"'
        m = re.search(pattern, raw)
        if not m:
            continue
        value_start = m.end()
        if i + 1 < len(keys):
            next_key = keys[i + 1]
            nm = re.search(f'"{re.escape(next_key)}"\\s*:', raw[value_start:])
            raw_value = raw[value_start: value_start + nm.start()] if nm else raw[value_start:]
        else:
            raw_value = raw[value_start:]
        # Strip trailing `",\n  ` or `"\n}` delimiters
        raw_value = re.sub(r'",?\s*$', '', raw_value)
        # Decode JSON escape sequences (\\n → \n, \\" → ", \\t → \t)
        try:
            decoded = raw_value.encode("utf-8").decode("unicode_escape")
        except Exception:
            decoded = raw_value
        result[key] = decoded
    return result


def load_episode(ep_dir: Path) -> dict[str, dict[str, int]] | None:
    """
    Load reasoning.json from an episode directory and return
    {dim_short: {section_title: score}}.
    Returns None if the file doesn't exist or is unparseable.
    Falls back to a tolerant extractor for malformed JSON.
    """
    reasoning_path = ep_dir / "reasoning.json"
    if not reasoning_path.exists():
        return None
    raw = reasoning_path.read_text(encoding="utf-8")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Malformed JSON (unescaped quotes in LLM output) — use tolerant extractor
        data = _extract_reasoning_tolerant(raw)
        if not data:
            return None

    result: dict[str, dict[str, int]] = {}
    for short, key in ALL_DIMS.items():
        text = data.get(key, "")
        result[short] = parse_section_scores(text)
    return result


def load_scores_json(ep_dir: Path) -> dict[str, float] | None:
    """Load aggregate scores from scores.json."""
    path = ep_dir / "scores.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Episode key builders
# ---------------------------------------------------------------------------

def ep_dir(episodes_root: Path, article: str, variant: str, preset: int) -> Path:
    return episodes_root / f"{article}__{variant}__preset{preset}"


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyze(episodes_root: Path) -> dict:
    """
    Master analysis. Returns a nested dict:
      results[article][variant] = {
          "aggregate": {dim_short: [score_p0..p5]},        # from scores.json
          "sections": {section: {dim_short: [score_p0..p5]}},
          "n_sections_per_preset": [n_p0..p5],
          "missing_presets": [preset_ids],
      }
    """
    results: dict = {}

    for article in ARTICLES:
        results[article] = {}
        for variant in VARIANTS:
            agg: dict[str, list[float | None]] = {d: [] for d in SHORT_LABELS}
            sec_data: dict[str, dict[str, list[int | None]]] = defaultdict(
                lambda: {d: [None] * N_PRESETS for d in SHORT_LABELS}
            )
            n_sections: list[int] = []
            missing: list[int] = []

            for preset in range(N_PRESETS):
                ep = ep_dir(episodes_root, article, variant, preset)
                scores_j = load_scores_json(ep)
                reasoning = load_episode(ep)

                if scores_j is None or reasoning is None:
                    missing.append(preset)
                    for d in SHORT_LABELS:
                        agg[d].append(None)
                    n_sections.append(0)
                    continue

                # Aggregate scores from scores.json
                # Map scores.json keys to our short labels
                score_map = {
                    "cc": scores_j.get("ground_truth_core_content"),
                    "fl": scores_j.get("ground_truth_flow"),
                    "st": scores_j.get("ground_truth_structure"),
                    "de": scores_j.get("ground_truth_depth_enhancement"),
                    "be": scores_j.get("ground_truth_breadth_enhancement"),
                    "cp": scores_j.get("ground_truth_core_preservation"),
                    "ga": scores_j.get("user_intent_guideline_adherence"),
                    "ra": scores_j.get("user_intent_research_anchoring"),
                    "gsp": scores_j.get("user_intent_golden_source_priority"),
                }
                for d, v in score_map.items():
                    agg[d].append(v)

                # Section-level from reasoning.json
                # Use the GT dims to determine canonical section list
                gt_secs = reasoning.get("cc", {})
                n_sections.append(len(gt_secs))

                for section, score in gt_secs.items():
                    for d in GT_DIMS.keys():
                        sec_data[section][d][preset] = reasoning[d].get(section)

                # UI sections (may have different names — match by position/order)
                ui_secs_sample = reasoning.get("ga", {})
                for section, score in ui_secs_sample.items():
                    for d in UI_DIMS.keys():
                        sec_data[section][d][preset] = reasoning[d].get(section)

            results[article][variant] = {
                "aggregate": agg,
                "sections": dict(sec_data),
                "n_sections_per_preset": n_sections,
                "missing_presets": missing,
            }

    return results


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------

def fmt_score(v: float | int | None) -> str:
    if v is None:
        return "  - "
    if isinstance(v, int):
        return f"  {v} "
    return f"{v:.3f}"


def preset_bar(vals: list[float | int | None]) -> str:
    """Show P0..P5 values as a compact bar."""
    parts = []
    for v in vals:
        if v is None:
            parts.append("·")
        elif isinstance(v, int):
            parts.append(str(v))
        else:
            parts.append(f"{v:.2f}")
    return " ".join(parts)


def mean_valid(vals: list) -> float | None:
    valid = [v for v in vals if v is not None]
    if not valid:
        return None
    return mean(valid)


def std_valid(vals: list) -> float | None:
    valid = [v for v in vals if v is not None]
    if len(valid) < 2:
        return None
    return stdev(valid)


def score_consistency(vals: list[int | None]) -> str:
    """Classify a sequence of 0/1 scores by stability."""
    valid = [v for v in vals if v is not None]
    if not valid:
        return "NO_DATA"
    if all(v == 1 for v in valid):
        return "STABLE_1"
    if all(v == 0 for v in valid):
        return "STABLE_0"
    n1 = sum(valid)
    n0 = len(valid) - n1
    if n1 >= 5:
        return "MOSTLY_1"
    if n0 >= 5:
        return "MOSTLY_0"
    return "MIXED"


CONSISTENCY_SYMBOL = {
    "STABLE_1": "✓✓",
    "MOSTLY_1": "✓ ",
    "MIXED":    "~~ ",
    "MOSTLY_0": "✗ ",
    "STABLE_0": "✗✗",
    "NO_DATA":  "-- ",
}

# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(results: dict, episodes_root: Path) -> str:
    lines: list[str] = []
    W = 120

    def h1(title: str):
        lines.append("=" * W)
        lines.append(f"  {title}")
        lines.append("=" * W)

    def h2(title: str):
        lines.append("")
        lines.append("-" * W)
        lines.append(f"  {title}")
        lines.append("-" * W)

    def h3(title: str):
        lines.append(f"\n  >>> {title}")

    # -----------------------------------------------------------------------
    h1("SECTION-LEVEL SIGNAL ANALYSIS — 144 VARIANT EPISODES (8 articles × 3 variants × 6 presets)")
    lines.append(f"  Dimensions: {' | '.join(SHORT_LABELS)}")
    lines.append(f"  GT dims (cc fl st de be cp) | UI dims (ga ra gsp)")
    lines.append("")

    # -----------------------------------------------------------------------
    # PART 1: Global completeness
    # -----------------------------------------------------------------------
    h2("PART 1 — DATA COMPLETENESS")
    total_eps = len(ARTICLES) * len(VARIANTS) * N_PRESETS
    total_missing = sum(
        len(results[a][v]["missing_presets"])
        for a in ARTICLES for v in VARIANTS
    )
    lines.append(f"  Total episodes: {total_eps}   Missing: {total_missing}")
    lines.append("")

    for article in ARTICLES:
        for variant in VARIANTS:
            m = results[article][variant]["missing_presets"]
            n_secs = results[article][variant]["n_sections_per_preset"]
            sec_range = f"{min(s for s in n_secs if s>0)}–{max(n_secs)}" if any(n_secs) else "?"
            status = "OK" if not m else f"MISSING P{','.join(str(x) for x in m)}"
            lines.append(f"  {article}__{variant:<16}  sections/preset: {sec_range:<6}  {status}")
    lines.append("")

    # -----------------------------------------------------------------------
    # PART 2: Per-article × variant aggregate score table (mean over presets)
    # -----------------------------------------------------------------------
    h2("PART 2 — AGGREGATE SCORES (mean over 6 presets, from scores.json)")
    header = f"  {'Article + Variant':<42} {'cc':>6} {'fl':>6} {'st':>6} {'de':>6} {'be':>6} {'cp':>6}  |  {'ga':>6} {'ra':>6} {'gsp':>6}"
    lines.append(header)
    lines.append("  " + "-" * (W - 2))

    for article in ARTICLES:
        for variant in VARIANTS:
            agg = results[article][variant]["aggregate"]
            label = f"{article}__{variant}"
            row_vals = []
            for d in SHORT_LABELS:
                v = mean_valid(agg[d])
                row_vals.append(f"{v:.3f}" if v is not None else "  -- ")
            row = f"  {label:<42} " + "  ".join(f"{v:>6}" for v in row_vals[:6]) + "   |  " + "  ".join(f"{v:>6}" for v in row_vals[6:])
            lines.append(row)
        lines.append("")

    # -----------------------------------------------------------------------
    # PART 3: Preset variance per article × variant (std across 6 presets)
    # -----------------------------------------------------------------------
    h2("PART 3 — PRESET VARIANCE (std across 6 presets — lower = more consistent signal)")
    lines.append(f"  {'Article + Variant':<42} {'cc':>6} {'fl':>6} {'st':>6} {'de':>6} {'be':>6} {'cp':>6}  |  {'ga':>6} {'ra':>6} {'gsp':>6}")
    lines.append("  " + "-" * (W - 2))

    for article in ARTICLES:
        for variant in VARIANTS:
            agg = results[article][variant]["aggregate"]
            label = f"{article}__{variant}"
            row_vals = []
            for d in SHORT_LABELS:
                v = std_valid(agg[d])
                row_vals.append(f"{v:.3f}" if v is not None else "  -- ")
            row = f"  {label:<42} " + "  ".join(f"{v:>6}" for v in row_vals[:6]) + "   |  " + "  ".join(f"{v:>6}" for v in row_vals[6:])
            lines.append(row)
        lines.append("")

    # -----------------------------------------------------------------------
    # PART 4: Per-preset raw scores per article × variant
    # -----------------------------------------------------------------------
    h2("PART 4 — PER-PRESET RAW SCORES (P0 P1 P2 P3 P4 P5 for each dim)")

    for article in ARTICLES:
        h3(article.upper())
        for variant in VARIANTS:
            agg = results[article][variant]["aggregate"]
            lines.append(f"\n    [{variant}]")
            lines.append(f"    {'Dim':<5}  P0      P1      P2      P3      P4      P5      mean    std")
            lines.append(f"    {'---':<5}  {'------  ' * 6}{'------  ' * 2}")
            for d in SHORT_LABELS:
                vals = agg[d]
                mu = mean_valid(vals)
                sd = std_valid(vals)
                val_strs = [f"{v:.3f}" if v is not None else "  -- " for v in vals]
                mu_str = f"{mu:.3f}" if mu is not None else " -- "
                sd_str = f"{sd:.3f}" if sd is not None else " -- "
                lines.append(f"    {d:<5}  {'  '.join(val_strs)}  {mu_str}  {sd_str}")

    # -----------------------------------------------------------------------
    # PART 5: Section-level analysis per article × variant
    # -----------------------------------------------------------------------
    h2("PART 5 — SECTION-LEVEL SCORES (binary per section per preset)")
    lines.append("  Consistency codes: ✓✓=STABLE_1 | ✓ =MOSTLY_1 | ~~=MIXED | ✗ =MOSTLY_0 | ✗✗=STABLE_0")
    lines.append("  Format: <score_P0 P1 P2 P3 P4 P5>  [consistency]  section_title")
    lines.append("")

    for article in ARTICLES:
        h3(article.upper())
        for variant in VARIANTS:
            sec_data = results[article][variant]["sections"]
            lines.append(f"\n    [{variant}]  ({len(sec_data)} unique sections across 6 presets)")
            lines.append(f"    {'Section':<45} {'cc':>2} {'fl':>2} {'st':>2} {'de':>2} {'be':>2} {'cp':>2}  {'ga':>2} {'ra':>2} {'gsp':>2}  Cons(cc)")
            lines.append(f"    {'-'*45} {'-'*2} {'-'*2} {'-'*2} {'-'*2} {'-'*2} {'-'*2}  {'-'*2} {'-'*2} {'-'*3}  --------")

            # Sort sections by mean cc score (ascending = most problematic first)
            def section_sort_key(sec_title):
                vals = sec_data[sec_title]["cc"]
                mu = mean_valid(vals)
                return (mu if mu is not None else 0.5, sec_title)

            for sec in sorted(sec_data.keys(), key=section_sort_key):
                dim_scores = sec_data[sec]
                # For each dim, show the 6 preset scores as a compact string
                # Use mean across presets as the cell value
                cell_vals = []
                for d in SHORT_LABELS:
                    mu = mean_valid(dim_scores[d])
                    cell_vals.append(f"{mu:.2f}" if mu is not None else " -- ")

                cc_vals = dim_scores["cc"]
                cons = score_consistency(cc_vals)
                cons_sym = CONSISTENCY_SYMBOL[cons]

                # Show preset-by-preset for CC to see pattern
                cc_bar = "".join(str(v) if v is not None else "·" for v in cc_vals)

                sec_display = sec[:44]
                row = (
                    f"    {sec_display:<45}"
                    + "  ".join(f"{v:>4}" for v in cell_vals[:6])
                    + "   "
                    + "  ".join(f"{v:>4}" for v in cell_vals[6:])
                    + f"  [{cc_bar}] {cons_sym}"
                )
                lines.append(row)

    # -----------------------------------------------------------------------
    # PART 6: Anomaly summary — STABLE_0 and MOSTLY_0 sections
    # -----------------------------------------------------------------------
    h2("PART 6 — ANOMALY SUMMARY: Sections with persistent 0 scores (cc dimension)")
    lines.append("  Only sections scoring STABLE_0 (all presets cc=0) or MOSTLY_0 (5+ presets cc=0)")
    lines.append("")

    for article in ARTICLES:
        anomalies_found = False
        article_lines: list[str] = []
        for variant in VARIANTS:
            sec_data = results[article][variant]["sections"]
            variant_anomalies: list[str] = []
            for sec, dim_scores in sec_data.items():
                cc_vals = dim_scores["cc"]
                cons = score_consistency(cc_vals)
                if cons in ("STABLE_0", "MOSTLY_0"):
                    cc_bar = "".join(str(v) if v is not None else "·" for v in cc_vals)
                    ga_mu = mean_valid(dim_scores["ga"])
                    ga_str = f"{ga_mu:.2f}" if ga_mu is not None else "--"
                    variant_anomalies.append(
                        f"      [{cc_bar}] cc | ga={ga_str} | {sec}  ({cons})"
                    )
            if variant_anomalies:
                article_lines.append(f"    {variant}:")
                article_lines.extend(variant_anomalies)
                anomalies_found = True

        if anomalies_found:
            lines.append(f"  {article}:")
            lines.extend(article_lines)
            lines.append("")

    # -----------------------------------------------------------------------
    # PART 7: Cross-variant comparison — same section, different variant signal
    # -----------------------------------------------------------------------
    h2("PART 7 — CROSS-VARIANT CC SIGNAL COMPARISON (mean cc per section across variants)")
    lines.append("  Shows sections that score consistently differently across variants of the same article.")
    lines.append(f"  {'Section':<45} {'MINIMAL':>7} {'STANDARD':>8} {'DEMANDING':>9}  delta(max-min)")
    lines.append("  " + "-" * 85)

    for article in ARTICLES:
        # Collect all unique section names across all variants
        all_secs: set[str] = set()
        for variant in VARIANTS:
            all_secs.update(results[article][variant]["sections"].keys())

        variant_means: dict[str, dict[str, float | None]] = {}  # sec -> variant -> mean_cc
        for variant in VARIANTS:
            variant_means[variant] = {}
            sec_data = results[article][variant]["sections"]
            for sec in all_secs:
                if sec in sec_data:
                    variant_means[variant][sec] = mean_valid(sec_data[sec]["cc"])
                else:
                    variant_means[variant][sec] = None

        # Show sections where at least one variant has mean_cc < 0.67 (some failures)
        notable = []
        for sec in sorted(all_secs):
            vals = [variant_means[v].get(sec) for v in VARIANTS]
            valid = [x for x in vals if x is not None]
            if not valid:
                continue
            if min(valid) < 0.67 or max(valid) - min(valid) >= 0.2:
                notable.append((sec, vals))

        if notable:
            lines.append(f"\n  {article}:")
            for sec, vals in notable:
                val_strs = [f"{v:.2f}" if v is not None else " -- " for v in vals]
                valid = [v for v in vals if v is not None]
                delta = max(valid) - min(valid) if len(valid) > 1 else 0.0
                flag = "  *** HIGH DELTA" if delta >= 0.33 else ""
                lines.append(
                    f"    {sec[:44]:<45} {val_strs[0]:>7} {val_strs[1]:>8} {val_strs[2]:>9}  {delta:.2f}{flag}"
                )

    # -----------------------------------------------------------------------
    # PART 8: Dimension correlation analysis
    # -----------------------------------------------------------------------
    h2("PART 8 — DIMENSION CORRELATION PATTERNS (per article × variant)")
    lines.append("  For each episode, shows which dim-pairs consistently disagree (one is high, other is low).")
    lines.append("  This helps identify where the grader is internally inconsistent.")
    lines.append("")

    for article in ARTICLES:
        article_block: list[str] = []
        for variant in VARIANTS:
            agg = results[article][variant]["aggregate"]

            # Find dims with large range across presets (high variance = unstable signal)
            unstable = []
            for d in SHORT_LABELS:
                vals = [v for v in agg[d] if v is not None]
                if len(vals) < 2:
                    continue
                rng = max(vals) - min(vals)
                mu = mean(vals)
                if rng >= 0.33:
                    unstable.append((d, mu, rng, [agg[d][p] for p in range(N_PRESETS)]))

            if unstable:
                article_block.append(f"    [{variant}]  High-variance dimensions (range ≥ 0.33):")
                for d, mu, rng, per_preset in unstable:
                    pp_str = " ".join(f"{v:.2f}" if v else " -- " for v in per_preset)
                    article_block.append(f"      {d:<5}  mean={mu:.3f}  range={rng:.3f}  [{pp_str}]")

        if article_block:
            lines.append(f"  {article}:")
            lines.extend(article_block)
            lines.append("")

    # -----------------------------------------------------------------------
    # PART 9: Summary statistics across all 144 episodes
    # -----------------------------------------------------------------------
    h2("PART 9 — GLOBAL SUMMARY STATISTICS (all 144 episodes)")

    # Collect all aggregate scores grouped by dim
    all_scores: dict[str, list[float]] = {d: [] for d in SHORT_LABELS}
    for article in ARTICLES:
        for variant in VARIANTS:
            agg = results[article][variant]["aggregate"]
            for d in SHORT_LABELS:
                for v in agg[d]:
                    if v is not None:
                        all_scores[d].append(v)

    lines.append(f"  {'Dim':<6} {'N':>4}  {'Mean':>7}  {'Std':>7}  {'Min':>7}  {'Max':>7}  Distribution")
    lines.append("  " + "-" * 90)
    for d in SHORT_LABELS:
        vals = all_scores[d]
        if not vals:
            continue
        mu = mean(vals)
        sd = stdev(vals) if len(vals) > 1 else 0.0
        mn = min(vals)
        mx = max(vals)
        # Simple histogram buckets: [0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.0]
        buckets = [0.0, 0.17, 0.33, 0.5, 0.67, 0.83, 1.01]
        counts = [0] * (len(buckets) - 1)
        for v in vals:
            for k in range(len(buckets) - 1):
                if buckets[k] <= v < buckets[k + 1]:
                    counts[k] += 1
                    break
        bar = " ".join(f"[{buckets[k]:.2f}-{buckets[k+1]:.2f}]:{counts[k]:3d}" for k in range(len(buckets) - 1))
        lines.append(f"  {d:<6} {len(vals):>4}  {mu:>7.3f}  {sd:>7.3f}  {mn:>7.3f}  {mx:>7.3f}  {bar}")

    lines.append("")
    lines.append("  GROUP MEANS  (GT vs UI comparison)")
    gt_all = [v for d in GT_DIMS for v in all_scores[d] if all_scores[d]]
    ui_all = [v for d in UI_DIMS for v in all_scores[d] if all_scores[d]]
    if gt_all:
        lines.append(f"  GT dims mean (cc+fl+st+de+be+cp): {mean(gt_all):.4f}  n={len(gt_all)}")
    if ui_all:
        lines.append(f"  UI dims mean (ga+ra+gsp):          {mean(ui_all):.4f}  n={len(ui_all)}")

    # -----------------------------------------------------------------------
    # PART 10: Per-variant aggregate summary
    # -----------------------------------------------------------------------
    h2("PART 10 — PER-VARIANT AGGREGATE (mean over all 8 articles × 6 presets = 48 eps each)")
    lines.append(f"  {'Variant':<16} " + " ".join(f"{'  ' + d:>7}" for d in SHORT_LABELS))
    lines.append("  " + "-" * 90)

    for variant in VARIANTS:
        variant_scores: dict[str, list[float]] = {d: [] for d in SHORT_LABELS}
        for article in ARTICLES:
            agg = results[article][variant]["aggregate"]
            for d in SHORT_LABELS:
                for v in agg[d]:
                    if v is not None:
                        variant_scores[d].append(v)
        row = f"  {variant:<16} "
        for d in SHORT_LABELS:
            mu = mean(variant_scores[d]) if variant_scores[d] else None
            row += f"  {mu:.3f}" if mu is not None else "    -- "
        lines.append(row)

    lines.append("")
    lines.append("END OF REPORT")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def find_episodes_root() -> Path:
    """Auto-detect episodes directory from cwd."""
    candidates = [
        Path("rl_training_data/episodes"),
        Path("../rl_training_data/episodes"),
        Path(__file__).parent / "episodes",
    ]
    for c in candidates:
        if c.is_dir():
            return c.resolve()
    raise FileNotFoundError("Cannot find rl_training_data/episodes/. Run from the writing_workflow/ or rl_training_data/ directory.")


def main():
    parser = argparse.ArgumentParser(description="Section-level signal analysis")
    parser.add_argument("--output", default="", help="Write report to this file (default: stdout + auto file)")
    args = parser.parse_args()

    root = find_episodes_root()
    print(f"Episodes root: {root}", file=sys.stderr)
    print("Loading all 144 episodes...", file=sys.stderr)

    results = analyze(root)

    print("Generating report...", file=sys.stderr)
    report = generate_report(results, root)

    # Always write to a file
    out_path = Path(args.output) if args.output else Path(__file__).parent / "_section_signal_report.txt"
    out_path.write_text(report, encoding="utf-8")
    print(f"Report written to: {out_path}", file=sys.stderr)

    # Also print to stdout
    print(report)


if __name__ == "__main__":
    main()
