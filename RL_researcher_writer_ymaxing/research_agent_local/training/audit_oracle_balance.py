"""Comprehensive one-shot audit of section-oracle class balance.

Reads all section_oracle.json + guideline_features.json + research_digest.md
under rl_training_data/bases/ and reports:

  1. Overall oracle-class distribution (skip/light/standard/deep)
  2. Per-variant-type breakdown (base / minimal / standard / demanding)
  3. Per-article breakdown (summed across its variants)
  4. Per (article, variant) detail table
  5. eff_need distribution for non-forbidden sections
     (reconstructs from gap_profile XML - assesses threshold calibration)
  6. Oracle vs. recomputed label consistency check (should be 100%)
  7. Threshold sensitivity: what eff_need thresholds would equalise classes?
  8. Data-driven recommendation: accept-as-is / upsample / retune thresholds

Usage (from research_agent_local/):
  python3 training/audit_oracle_balance.py
  python3 training/audit_oracle_balance.py --bases-dir /path/to/bases
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))
from _rl_preset import PRESET_NAMES, PRESET_ORDER  # noqa: E402

_DEFAULT_BASES_DIR = _THIS_DIR.parent.parent / "rl_training_data" / "bases"
_VARIANTS = ("minimal", "standard", "demanding")
_ALARM_LO = 0.10
_ALARM_HI = 0.45

# Base dirs duplicate __var_standard for every article except lesson-10
# (which has no base dir).  Exclude them from all stats to avoid double-counting.
_EXCLUDE_FROM_STATS = {"base"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_dir_name(name: str) -> tuple[str, str]:
    for v in _VARIANTS:
        if name.endswith(f"__var_{v}"):
            return name[: -(len(v) + 6)], v
    return name, "base"


def _preset_2d(
    need: int,
    target_words: int,
    mandatory_bullets: int,
    must_cover_depth: int,
    must_stay_brief: int,
    policy: str,
) -> tuple[str, int]:
    """Mirror of generate_digests._preset_2d; returns (preset_name, eff_need)."""
    if policy == "forbidden":
        return "skip", -999
    headroom = 0
    if target_words >= 400:
        headroom += 1
    elif 0 < target_words < 200:
        headroom -= 1
    if mandatory_bullets >= 5:
        headroom += 1
    elif 0 < mandatory_bullets <= 2:
        headroom -= 1
    if must_cover_depth >= 3:
        headroom += 1
    if must_stay_brief >= 2:
        headroom -= 1
    if policy == "required":
        headroom += 1
    eff = need + 2 * headroom
    if eff <= 2:
        return "skip", eff
    if eff <= 5:
        return "light", eff
    if eff <= 9:
        return "standard", eff
    return "deep", eff


def _load_dir(d: Path) -> dict:
    """Load oracle, features, and gap_profile from a single article-variant dir."""
    result: dict = {
        "oracle": {},
        "policy": None,
        "sections": {},      # sec_id -> (need, eff_need, computed_label)
        "has_digest": (d / "research_digest.md").exists(),
        "has_features": (d / "guideline_features.json").exists(),
        "has_oracle": (d / "section_oracle.json").exists(),
    }
    if result["has_oracle"]:
        try:
            result["oracle"] = (
                json.loads((d / "section_oracle.json").read_text(encoding="utf-8"))
                .get("presets", {}) or {}
            )
        except (OSError, json.JSONDecodeError) as e:
            print(f"  WARN: {d / 'section_oracle.json'}: {e}", file=sys.stderr)

    if result["has_features"]:
        try:
            feat = json.loads((d / "guideline_features.json").read_text(encoding="utf-8"))
            result["policy"] = feat.get("external_evidence_policy", "allowed")
        except (OSError, json.JSONDecodeError):
            pass

    if result["has_digest"] and result["policy"] is not None:
        try:
            text = (d / "research_digest.md").read_text(encoding="utf-8")
            gp = re.search(r"<gap_profile>(.*?)</gap_profile>", text, re.DOTALL)
            if gp:
                for sm in re.finditer(
                    r'<section\s+id="([^"]+)"\s+need_depth="(\d+)"\s+need_breadth="(\d+)"'
                    r'\s+target_words="(\d+)"\s+mandatory_bullets="(\d+)"'
                    r'\s+must_cover_depth="(\d+)"\s+must_stay_brief="(\d+)"',
                    gp.group(1),
                ):
                    sec_id = sm.group(1)
                    need = int(sm.group(2)) + int(sm.group(3))
                    label, eff = _preset_2d(
                        need, int(sm.group(4)), int(sm.group(5)),
                        int(sm.group(6)), int(sm.group(7)), result["policy"],
                    )
                    result["sections"][sec_id] = (need, eff, label)
        except OSError:
            pass

    return result


def _fmt_bar(counter: Counter[str], total: int, width: int = 32) -> str:
    syms = {"skip": "S", "light": "L", "standard": "T", "deep": "D"}
    bar = ""
    for name in ("skip", "light", "standard", "deep"):
        n = counter.get(name, 0)
        chars = round(width * n / max(1, total))
        bar += syms[name] * chars
    return f"[{bar:<{width}}]"


def _fmt_dist(counter: Counter[str], total: int) -> str:
    if total == 0:
        return "(no sections)"
    return "  ".join(
        f"{PRESET_NAMES[i]}={counter.get(PRESET_NAMES[i], 0)}({100*counter.get(PRESET_NAMES[i],0)/total:.0f}%)"
        for i in range(len(PRESET_NAMES))
    )


def _flag_skew(counter: Counter[str], total: int) -> list[str]:
    if total == 0:
        return []
    flags = []
    for i in range(len(PRESET_NAMES)):
        name = PRESET_NAMES[i]
        f = counter.get(name, 0) / total
        if f < _ALARM_LO:
            flags.append(f"{name} starved ({f:.1%})")
        elif f > _ALARM_HI:
            flags.append(f"{name} dominant ({f:.1%})")
    return flags


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(bases_dir: Path) -> int:
    if not bases_dir.is_dir():
        print(f"ERROR: bases dir not found: {bases_dir}", file=sys.stderr)
        return 1

    dir_data: dict[tuple[str, str], dict] = {}
    missing_oracle: list[str] = []
    missing_complete: list[str] = []

    for d in sorted(bases_dir.iterdir()):
        if not d.is_dir() or d.name.endswith("_OLD"):
            continue
        article, variant = _parse_dir_name(d.name)
        info = _load_dir(d)
        if not info["has_oracle"]:
            missing_oracle.append(d.name)
            continue
        if not info["has_digest"] or not info["has_features"]:
            missing_complete.append(d.name)
        dir_data[(article, variant)] = info

    if not dir_data:
        print("ERROR: no section_oracle.json files found.", file=sys.stderr)
        return 1

    # Aggregate
    overall: Counter[str] = Counter()
    by_vtype: dict[str, Counter[str]] = defaultdict(Counter)
    by_article: dict[str, Counter[str]] = defaultdict(Counter)
    eff_needs_all: list[int] = []
    mismatch_count = 0
    total_with_eff = 0
    policy_counts: Counter[str] = Counter()
    sec_counts: list[int] = []

    for (article, variant), info in dir_data.items():
        oracle = info["oracle"]
        if variant not in _EXCLUDE_FROM_STATS:
            sec_counts.append(len(oracle))
        if variant not in _EXCLUDE_FROM_STATS and info["policy"]:
            policy_counts[info["policy"]] += 1
        for sec_id, label in oracle.items():
            if label not in PRESET_ORDER:
                continue
            if variant not in _EXCLUDE_FROM_STATS:
                overall[label] += 1
                by_vtype[variant][label] += 1
                by_article[article][label] += 1
            if sec_id in info["sections"]:
                if variant not in _EXCLUDE_FROM_STATS:
                    total_with_eff += 1
                    need, eff, computed = info["sections"][sec_id]
                    if computed != label:
                        mismatch_count += 1
                    if info["policy"] != "forbidden":
                        eff_needs_all.append(eff)

    total_sections = sum(overall.values())
    total_dirs = len(dir_data)

    # =========================================================================
    print("=" * 80)
    print(" SECTION-ORACLE CLASS BALANCE AUDIT")
    print("=" * 80)
    print(f"Bases dir:          {bases_dir}")
    print(f"Dirs with oracle:   {total_dirs}")
    print(f"Total sections:     {total_sections}")
    if missing_oracle:
        print(f"Missing oracle:     {len(missing_oracle)}: {', '.join(missing_oracle)}")
    if missing_complete:
        print(f"Missing digest/features: {', '.join(missing_complete)}")
    print(f"Sections per dir:   min={min(sec_counts)}  max={max(sec_counts)}  "
          f"avg={sum(sec_counts)/len(sec_counts):.1f}")
    print(f"Policy distribution: "
          + "  ".join(f"{k}={v}" for k, v in sorted(policy_counts.items())))
    print()

    # ---- 1. Overall ---------------------------------------------------------
    print("-" * 80)
    print("1. OVERALL DISTRIBUTION")
    print("-" * 80)
    print(f"  {_fmt_bar(overall, total_sections)}  (S=skip L=light T=standard D=deep)")
    print(f"  " + _fmt_dist(overall, total_sections))
    flags = _flag_skew(overall, total_sections)
    if flags:
        print("  WARN: " + "; ".join(flags))
    print()

    # ---- 2. Per variant type ------------------------------------------------
    print("-" * 80)
    print("2. PER VARIANT TYPE")
    print("-" * 80)
    for vtype in ("base", *_VARIANTS):
        c = by_vtype.get(vtype, Counter())
        tot = sum(c.values())
        if tot == 0:
            continue
        bar = _fmt_bar(c, tot)
        flag_str = ("  WARN: " + "; ".join(_flag_skew(c, tot))) if _flag_skew(c, tot) else ""
        print(f"  {vtype:9s} ({tot:3d} sec) {bar}  {_fmt_dist(c, tot)}{flag_str}")
    print()

    # ---- 3. Per article (summed across variants) ----------------------------
    print("-" * 80)
    print("3. PER ARTICLE (summed across variants)")
    print("-" * 80)
    for article in sorted(by_article):
        c = by_article[article]
        tot = sum(c.values())
        print(f"  {article:42s} ({tot:3d} sec)  {_fmt_dist(c, tot)}")
    print()

    # ---- 4. Per (article, variant) detail -----------------------------------
    print("-" * 80)
    print("4. PER (ARTICLE, VARIANT) DETAIL")
    print("-" * 80)
    prev_art = None
    for (article, variant) in sorted(dir_data):
        if article != prev_art:
            print()
            prev_art = article
        info = dir_data[(article, variant)]
        c = Counter(info["oracle"].values())
        tot = sum(c.values())
        policy_tag = f"[{info['policy'] or '?':9s}]" if info["policy"] else "[?        ]"
        print(f"  {article:42s} [{variant:9s}] {policy_tag} ({tot:2d} sec)  "
              f"{_fmt_dist(c, tot)}")
    print()

    # ---- 5. eff_need distribution -------------------------------------------
    if eff_needs_all:
        n_eff = len(eff_needs_all)
        print("-" * 80)
        print(f"5. EFF_NEED DISTRIBUTION (non-forbidden sections, n={n_eff})")
        print("-" * 80)
        eff_counter = Counter(eff_needs_all)
        cumulative = 0
        prev_band = None
        for i in sorted(eff_counter):
            n = eff_counter[i]
            cumulative += n
            band = ("skip" if i <= 2 else
                    "light" if i <= 5 else
                    "standard" if i <= 9 else "deep")
            sep = "  |" if band != prev_band and prev_band is not None else "   "
            prev_band = band
            print(f"  {sep} eff={i:3d}: {n:3d} ({100*n/n_eff:.1f}%)"
                  f"  cum={100*cumulative/n_eff:.0f}%  [{band}]")
        print()

        eff_sorted = sorted(eff_needs_all)
        n = len(eff_sorted)
        q25 = eff_sorted[int(0.25 * n)]
        q50 = eff_sorted[int(0.50 * n)]
        q75 = eff_sorted[int(0.75 * n)]
        print(f"  Quartile thresholds (equalise non-forbidden into 4 equal buckets):")
        print(f"    eff <= {q25:2d} -> skip (p25)   eff <= {q50:2d} -> light (p50)")
        print(f"    eff <= {q75:2d} -> standard (p75)   eff > {q75:2d} -> deep")
        print()
    else:
        q25 = q50 = q75 = None

    # ---- 6. Consistency check -----------------------------------------------
    print("-" * 80)
    print("6. ORACLE CONSISTENCY (recomputed vs. stored)")
    print("-" * 80)
    if total_with_eff == 0:
        print("  No gap_profile data available for consistency check.")
    elif mismatch_count == 0:
        print(f"  PASS  {total_with_eff}/{total_with_eff} labels match recomputed (100.0%).")
    else:
        pct = 100 * (total_with_eff - mismatch_count) / total_with_eff
        print(f"  WARN  {mismatch_count} mismatches / {total_with_eff} ({pct:.1f}% consistent).")
        print("        Oracle files may be stale; re-run generate_digests.py --force.")
    print()

    # ---- 7. Recommendation --------------------------------------------------
    print("-" * 80)
    print("7. RECOMMENDATION")
    print("-" * 80)
    frac = {name: overall.get(name, 0) / total_sections for name in ("skip", "light", "standard", "deep")}
    forbidden_dirs = policy_counts.get("forbidden", 0)
    total_policy_dirs = sum(policy_counts.values())
    print(f"  Distribution: skip={frac['skip']:.1%}  light={frac['light']:.1%}  "
          f"standard={frac['standard']:.1%}  deep={frac['deep']:.1%}")
    print(f"  Forbidden-policy dirs: {forbidden_dirs}/{total_policy_dirs} "
          f"({forbidden_dirs/max(1,total_policy_dirs):.0%}) — all produce skip regardless of need.")
    print()

    overall_flags = _flag_skew(overall, total_sections)
    if not overall_flags:
        print("  BALANCED  All classes within alarm band [10%, 45%].")
        print("  Proceed directly to GRPO training.")
    elif frac["light"] < _ALARM_LO and frac["standard"] < _ALARM_LO:
        print("  BIMODAL  Distribution is skip-vs-deep dominated.")
        print()
        print("  Root cause:")
        print(f"    (a) forbidden policy forces all minimal-variant sections to skip.")
        print(f"    (b) non-forbidden eff_need is right-skewed: most sections have large")
        print(f"        coverage gaps (eff_need >= 10 -> deep with current thresholds).")
        print()
        print("  Three options - in order of preference:")
        print()
        print("  A) ACCEPT AS-IS  [recommended for first training run]")
        print("     Model will primarily learn skip <-> deep discrimination.")
        print("     light/standard contribute small but valid gradient signal.")
        print("     Evaluate: can the model distinguish all 4 classes on held-out data?")
        print()
        if q25 is not None:
            print(f"  B) THRESHOLD RECALIBRATION  [no API calls, pure relabelling]")
            print(f"     Current:   eff<=2->skip,  <=5->light,  <=9->standard,  else->deep")
            print(f"     Quartile:  eff<={q25}->skip, <={q50}->light, <={q75}->standard, >{q75}->deep")
            print(f"     This equalises non-forbidden classes but semantically eff_need={q25}")
            print(f"     represents a real coverage gap - labelling it skip corrupts the oracle.")
            print(f"     Only viable if you redefine preset semantics accordingly.")
            print()
        print("  C) STRATIFIED UPSAMPLING  in train_grpo.load_section_groups")
        light_n = overall.get("light", 0)
        std_n = overall.get("standard", 0)
        skip_n = overall.get("skip", 0)
        print(f"     Weight groups inversely to class frequency:")
        print(f"       light    x{round(skip_n/max(light_n,1))} upsample  "
              f"({light_n} examples -> high overfitting risk)")
        print(f"       standard x{round(skip_n/max(std_n,1))} upsample  "
              f"({std_n} examples -> moderate risk)")
        print(f"     Risk is high given the small count of light examples.")
    else:
        if _flag_skew(overall, total_sections):
            print("  MILD/MODERATE SKEW  Outside alarm band on some classes.")
            print("  Consider stratified upsampling in train_grpo.load_section_groups.")
        else:
            print("  MILD SKEW  Within alarm band. GRPO relative advantage absorbs this.")
            print("  Proceed to training; revisit if eval shows systematic class errors.")

    print("=" * 80)
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bases-dir", type=Path, default=_DEFAULT_BASES_DIR,
        help=f"Path to rl_training_data/bases/ (default: {_DEFAULT_BASES_DIR})",
    )
    args = parser.parse_args()
    sys.exit(main(args.bases_dir))
