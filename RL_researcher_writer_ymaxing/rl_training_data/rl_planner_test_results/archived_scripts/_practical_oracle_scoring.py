"""Margin-aware "practical oracle" scoring for exploration-preset reports.

Strict exact-match treats every miss identically, even when the true R_w
curve is a near-tie between adjacent presets (i.e. the "wrong" pick is
reward-equivalent to the true oracle_arm). This module re-scores a report
against a PRACTICAL oracle instead:

  * wide-margin article (best R_w beats every other arm by > EPS_BAND):
      scored strictly -- the choice genuinely matters, any deviation is a
      real miss (further split into undershoot/overshoot for diagnosis).
  * narrow-margin article (>=2 arms within EPS_BAND of the best R_w, forming
      a "band"): the practical oracle is the CHEAPEST arm in that band.
      Picking anything >= that arm counts as a practical hit (escalating
      beyond the practical minimum is a legitimate user/system choice, not
      an error); picking below it is a genuine undershoot miss.

EPS_BAND matches compute_article_oracle.py's own near-tie definition, so
this is not an arbitrary new threshold -- it's the same tolerance the oracle
computation itself already uses to decide when presets are reward-equivalent.

Usage:
    python3 _practical_oracle_scoring.py [report.md]
    (defaults to the RL+guards run33/ep81 report)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_DEFAULT_REPORT = _HERE / "rl_guard_only_train_and_test_results_run33_averaged_confidence_epoch81.md"

_ARMS = ["skip", "light", "standard", "deep"]
_ARM_IDX = {a: i for i, a in enumerate(_ARMS)}
_EPS_BAND = 0.03  # compute_article_oracle.py::EPS_BAND

_BLOCK_RE = re.compile(r"^ {2}Variant : (\S+)\s+\[(TRAIN|TEST)\]\s*$", re.M)
_POLICY_RE = re.compile(r"^ {2}Policy\s+: (\w+)\s*$", re.M)
_CHOSEN_RE = re.compile(r"^ {2}-> Chosen\s+: P(\d)\b", re.M)
_ORACLE_RE = re.compile(r"^ {2}Oracle\s+: P(\d)\b", re.M)
_RW_RE = re.compile(
    r"^ {2}R_w\s+: P0/skip:(-?[\d.]+)\s+P1/light:(-?[\d.]+)\s+"
    r"P2/standard:(-?[\d.]+)\s+P3/deep:(-?[\d.]+)\s*$", re.M
)


def parse_report(path: Path) -> list[dict]:
    """Parse any of the test_grok_planner.py report .md files into per-article
    records (variant, split, policy, oracle idx, chosen idx, r_w list)."""
    text = path.read_text(encoding="utf-8")
    starts = [(m.start(), m.group(1), m.group(2)) for m in _BLOCK_RE.finditer(text)]
    records = []
    for i, (pos, variant, split) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        chunk = text[pos:end]
        records.append({
            "variant": variant,
            "split": split,
            "policy": _POLICY_RE.search(chunk).group(1),
            "oracle": int(_ORACLE_RE.search(chunk).group(1)),
            "chosen": int(_CHOSEN_RE.search(chunk).group(1)),
            "r_w": [float(_RW_RE.search(chunk).group(k)) for k in (1, 2, 3, 4)],
        })
    return records


def practical_score(records: list[dict]) -> list[dict]:
    """Annotate each record with band/practical-oracle/hit classification."""
    scored = []
    for r in records:
        r_w = r["r_w"]
        best_r = max(r_w)
        band = sorted(
            (i for i in range(4) if best_r - r_w[i] <= _EPS_BAND),
        )
        practical_oracle_idx = band[0]
        wide_margin = len(band) == 1

        oracle_idx, chosen_idx = r["oracle"], r["chosen"]
        strict_hit = chosen_idx == oracle_idx
        if wide_margin:
            practical_hit = strict_hit
            undershoot = (not strict_hit) and (chosen_idx < oracle_idx)
            overshoot = (not strict_hit) and (chosen_idx > oracle_idx)
        else:
            practical_hit = chosen_idx >= practical_oracle_idx
            undershoot = chosen_idx < practical_oracle_idx
            overshoot = False  # escalating past the practical minimum is not an error

        margin = best_r - sorted(r_w, reverse=True)[1]
        scored.append({
            **r,
            "band": [_ARMS[i] for i in band],
            "practical_oracle": _ARMS[practical_oracle_idx],
            "wide_margin": wide_margin,
            "margin": round(margin, 4),
            "strict_hit": strict_hit,
            "practical_hit": practical_hit,
            "undershoot": undershoot,
            "overshoot": overshoot,
        })
    return scored


def summarize(scored: list[dict], split: str) -> dict:
    sub = [r for r in scored if r["split"] == split]
    wide = [r for r in sub if r["wide_margin"]]
    narrow = [r for r in sub if not r["wide_margin"]]
    return {
        "n": len(sub),
        "n_wide": len(wide),
        "n_narrow": len(narrow),
        "strict_exact_wide_pct": 100 * sum(r["strict_hit"] for r in wide) / max(len(wide), 1),
        "strict_exact_narrow_pct": 100 * sum(r["strict_hit"] for r in narrow) / max(len(narrow), 1),
        "strict_exact_overall_pct": 100 * sum(r["strict_hit"] for r in sub) / len(sub),
        "practical_hit_pct": 100 * sum(r["practical_hit"] for r in sub) / len(sub),
        "undershoots": [r["variant"] for r in sub if r["undershoot"]],
        "overshoots": [r["variant"] for r in sub if r["overshoot"]],
    }


def print_report(scored: list[dict]) -> None:
    for split in ("TEST", "TRAIN"):
        s = summarize(scored, split)
        if s["n"] == 0:
            continue
        print(f"=== {split} (n={s['n']}) ===")
        print(f"  wide-margin: {s['n_wide']}  narrow-margin: {s['n_narrow']}")
        print(f"  strict exact-match: wide={s['strict_exact_wide_pct']:.1f}%  "
              f"narrow={s['strict_exact_narrow_pct']:.1f}%  overall={s['strict_exact_overall_pct']:.1f}%")
        print(f"  practical hit rate (overall): {s['practical_hit_pct']:.1f}%")
        print(f"  genuine undershoot misses ({len(s['undershoots'])}): {s['undershoots']}")
        print(f"  genuine overshoot misses ({len(s['overshoots'])}): {s['overshoots']}")
        print()


if __name__ == "__main__":
    report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else _DEFAULT_REPORT
    print_report(practical_score(parse_report(report_path)))
