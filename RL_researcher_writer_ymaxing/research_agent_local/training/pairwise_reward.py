"""Reconcile pairwise LLM comparison judgments into per-arm enhancement credits.

Consumes the raw judgment JSON written by writing_workflow/rl_pairwise_grading_generator.py
(rl_training_data/pairwise_pilot/<article>/pairwise_judgments.json) and produces, for
each (article, section, dimension), a least-squares-reconciled credit value per arm
(light/standard/deep) directly comparable to enhancement_credit()'s existing tag-based
output -- so the two can be diffed/validated against each other before any production
section_oracle.json change.

Does NOT call any LLM or make any API request -- pure post-hoc numeric reconciliation,
same "zero re-grading cost, freely re-tunable" spirit as sweep_reward_formula.py.

Method: light's credit is FIXED at its existing tag-based enhancement_credit() value
(the anchor -- this keeps the reconciled scale comparable to un-migrated/legacy data).
standard/deep are solved via ridge-regularized least squares from the 3 pairwise deltas
(light_vs_standard, light_vs_deep, standard_vs_deep), regularized toward the anchor so
the solve is always well-posed even when a pairwise call failed/erred for one pair.

Usage (from research_agent_local/training/):
  python3 pairwise_reward.py --articles 09_RAG__var_standard 06_tools__var_standard
  python3 pairwise_reward.py                      # all articles found under pairwise_pilot/
  python3 pairwise_reward.py --json-out out.json  # also write a machine-readable summary
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import generate_episode_oracles as geo
from enhancement_reward import enhancement_credit

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent  # RL_researcher_writer_ymaxing/
_PAIRWISE_DIR = _REPO_ROOT / "rl_training_data" / "pairwise_pilot"

# Rough initial calibration of the 5-point ordinal preference scale to a signed
# numeric delta, on roughly the same [0, 1] dynamic range as enhancement_credit().
# Magnitudes are deliberately modest: enhancement_credit()'s own tier spacing is
# ~0.20-0.25 per step (0.55 -> 0.80 -> 1.00), so a single "more" verdict is
# calibrated as "about one tier up", not an instant jump to the ceiling -- a
# larger delta would saturate almost any anchor near 0.55-0.80 on the very
# first non-tie judgment, collapsing standard-vs-deep differentiation.
# TUNABLE without any new API calls -- only the raw judgments (preference label +
# a_arm/b_arm) are ever re-consumed; changing this map just re-runs the (cheap)
# solve below, exactly like enhancement_reward.py's own curve constants.
PREFERENCE_TO_DELTA: dict[str, float] = {
    "a_much_more": -0.45,
    "a_more": -0.20,
    "tie": 0.00,
    "b_more": 0.20,
    "b_much_more": 0.45,
}

# Regularization strength pulling standard/deep toward the light anchor when
# pairwise evidence for a pair is sparse or absent (missing/errored call).
# Keeps the least-squares solve well-posed for every possible subset of the 3
# pairs (0, 1, 2, or 3 present) without needing special-cased branching.
_RIDGE_LAMBDA = 0.01

_PAIRS: list[tuple[str, str]] = [("light", "standard"), ("light", "deep"), ("standard", "deep")]
_DIMENSIONS = ("depth", "breadth")
_ARMS = ("light", "standard", "deep")


def _signed_delta(dim_judgment: dict, a_arm: str, b_arm: str, arm_x: str, arm_y: str) -> float | None:
    """Return delta(arm_y) - delta(arm_x) implied by one pairwise judgment, correcting
    for the random A/B slot assignment (a_arm/b_arm, recorded at the judgment-entry
    level, NOT inside the depth/breadth sub-dict). None if malformed.
    """
    pref = dim_judgment.get("preference")
    if pref not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[pref]  # positive means B > A, in the A/B slot's own frame
    if a_arm == arm_x and b_arm == arm_y:
        return raw
    if a_arm == arm_y and b_arm == arm_x:
        return -raw
    return None


def _ridge_lstsq_2unknowns(rows: list[list[float]], rhs: list[float], anchor: float) -> tuple[float, float]:
    """Ridge-regularized least-squares solve for (v_standard, v_deep), regularized
    toward `anchor` (light's credit). Always well-posed (no numpy dependency,
    no degenerate-case branching needed) regardless of how many of the up-to-3
    rows are present.
    """
    a11 = sum(r[0] * r[0] for r in rows) + _RIDGE_LAMBDA
    a12 = sum(r[0] * r[1] for r in rows)
    a22 = sum(r[1] * r[1] for r in rows) + _RIDGE_LAMBDA
    b1 = sum(r[0] * y for r, y in zip(rows, rhs)) + _RIDGE_LAMBDA * anchor
    b2 = sum(r[1] * y for r, y in zip(rows, rhs)) + _RIDGE_LAMBDA * anchor
    det = a11 * a22 - a12 * a12
    x1 = (b1 * a22 - b2 * a12) / det
    x2 = (a11 * b2 - a12 * b1) / det
    return x1, x2


def solve_section_credits(pair_judgments: dict, dimension: str, anchor_light_credit: float) -> dict[str, float]:
    """Reconcile light/standard/deep credits for ONE dimension of ONE section.

    Args:
        pair_judgments: {"light_vs_standard": {...}, "light_vs_deep": {...},
            "standard_vs_deep": {...}} as written by rl_pairwise_grading_generator.py
            (each value has "depth"/"breadth" sub-dicts, or "error" if the call failed).
        dimension: "depth" or "breadth".
        anchor_light_credit: light's existing tag-based enhancement_credit() value.

    Returns {"light": anchor_light_credit, "standard": ..., "deep": ...}, each
    clipped to [0.0, 1.0] to match enhancement_credit()'s own output range.
    """
    rows: list[list[float]] = []
    rhs: list[float] = []
    # Row encoding: unknowns x = [v_standard, v_deep]. v_light is fixed at anchor.
    #   light_vs_standard:  v_standard              = anchor + delta
    #   light_vs_deep:      v_deep                  = anchor + delta
    #   standard_vs_deep:  -v_standard + v_deep      = delta
    row_spec = {
        ("light", "standard"): ([1.0, 0.0], "light_vs_standard", 1.0),
        ("light", "deep"): ([0.0, 1.0], "light_vs_deep", 1.0),
        ("standard", "deep"): ([-1.0, 1.0], "standard_vs_deep", 0.0),
    }
    for (arm_x, arm_y), (coeffs, key, anchor_offset) in row_spec.items():
        entry = pair_judgments.get(key)
        if not entry or "error" in entry:
            continue
        dim_judgment = entry.get(dimension)
        if not dim_judgment:
            continue
        delta = _signed_delta(dim_judgment, entry.get("a_arm"), entry.get("b_arm"), arm_x, arm_y)
        if delta is None:
            continue
        rows.append(coeffs)
        rhs.append(anchor_light_credit * anchor_offset + delta)

    if not rows:
        return {"light": anchor_light_credit, "standard": anchor_light_credit, "deep": anchor_light_credit}

    v_standard, v_deep = _ridge_lstsq_2unknowns(rows, rhs, anchor_light_credit)
    return {
        "light": anchor_light_credit,
        "standard": max(0.0, min(1.0, v_standard)),
        "deep": max(0.0, min(1.0, v_deep)),
    }


def _arm_episode_dir(article: str, arm: str) -> Path:
    is_train_variant = "__var_" in article
    root = geo._EPISODES_DIR if is_train_variant else geo._TEST_EPISODES_DIR
    presets = geo._ARM_PRESETS if is_train_variant else geo._TEST_ARM_PRESETS
    return root / f"{article}__preset{presets[arm][0]}"


def _tag_credits_for_arm(article: str, arm: str) -> dict[str, dict[str, float]]:
    """Return {norm_section_title: {"depth": credit, "breadth": credit}} for one
    arm, using the SAME tag-parsing + enhancement_credit() logic production oracle
    generation uses (imported, not reimplemented).
    """
    ep_dir = _arm_episode_dir(article, arm)
    dims = geo._load_episode(ep_dir)
    out: dict[str, dict[str, float]] = {}
    de_entries = dims.get("ground_truth_depth_enhancement", [])
    be_entries = dims.get("ground_truth_breadth_enhancement", [])
    titles = {norm: raw for raw, norm, _score, _enh in de_entries}
    titles.update({norm: raw for raw, norm, _score, _enh in be_entries})
    for idx, norm_title in enumerate(titles):
        section_credits = {}
        for dim_name, entries in (("depth", de_entries), ("breadth", be_entries)):
            enh = geo._get_enhancement(entries, norm_title, idx)
            if enh is not None:
                _count, qualities = enh
                section_credits[dim_name] = enhancement_credit(qualities)
            else:
                section_credits[dim_name] = geo._get_score(entries, norm_title, idx)
        out[norm_title] = section_credits
    return out


def _tag_credits_all_arms(article: str) -> dict[str, dict[str, dict[str, float]]]:
    """Return {arm: {norm_section_title: {"depth": credit, "breadth": credit}}}
    for all 3 graded arms (light/standard/deep), for direct comparison against
    the pairwise-reconciled credits.
    """
    return {arm: _tag_credits_for_arm(article, arm) for arm in _ARMS}


def _lookup_tag_credit(tag_credits_for_arm: dict[str, dict[str, float]], norm_title: str, dim: str) -> float:
    if norm_title in tag_credits_for_arm:
        return tag_credits_for_arm[norm_title][dim]
    for k, v in tag_credits_for_arm.items():
        if norm_title in k or k in norm_title:
            return v[dim]
    return 0.0


def reconcile_article(article: str) -> dict:
    """Reconcile all sections of one article's pairwise_judgments.json against
    the light arm's existing tag-based credits, and attach the existing
    tag-based credits for standard/deep too (for direct side-by-side comparison).
    Returns a structured report.
    """
    judgments_path = _PAIRWISE_DIR / article / "pairwise_judgments.json"
    if not judgments_path.exists():
        raise FileNotFoundError(f"No pairwise judgments found for {article!r} at {judgments_path}")
    data = json.loads(judgments_path.read_text(encoding="utf-8"))
    tag_credits = _tag_credits_all_arms(article)

    sections_out = {}
    for title, pair_judgments in data.get("sections", {}).items():
        norm_title = geo._normalize(title)
        light_anchor = {dim: _lookup_tag_credit(tag_credits["light"], norm_title, dim) for dim in _DIMENSIONS}
        tag_side = {
            arm: {dim: _lookup_tag_credit(tag_credits[arm], norm_title, dim) for dim in _DIMENSIONS}
            for arm in _ARMS
        }
        pairwise_side = {dim: solve_section_credits(pair_judgments, dim, light_anchor[dim]) for dim in _DIMENSIONS}
        sections_out[title] = {"tag": tag_side, "pairwise": pairwise_side}
    return {"article": article, "sections": sections_out}


def _argmax(credits: dict[str, float]) -> str:
    return max(credits, key=lambda arm: credits[arm])


def _print_report(report: dict) -> tuple[int, int]:
    """Print a tag-vs-pairwise comparison table. Returns (n_compared, n_agree)
    counting standard-vs-deep argmax agreement across (section, dimension) pairs
    where the two methods differ meaningfully (skips both-near-zero cases).
    """
    article = report["article"]
    print("=" * 100)
    print(article)
    print("=" * 100)
    n_compared = n_agree = 0
    for title, entry in report["sections"].items():
        print(f"  {title}")
        for dim in _DIMENSIONS:
            tag = entry["tag"]
            pw = entry["pairwise"][dim]
            tag_line = "/".join(f"{arm[:4]}={tag[arm][dim]:.3f}" for arm in _ARMS)
            pw_line = "/".join(f"{arm[:4]}={pw[arm]:.3f}" for arm in _ARMS)
            std_deep_tag = {"standard": tag["standard"][dim], "deep": tag["deep"][dim]}
            std_deep_pw = {"standard": pw["standard"], "deep": pw["deep"]}
            flag = ""
            if abs(std_deep_tag["standard"] - std_deep_tag["deep"]) > 0.02 or abs(std_deep_pw["standard"] - std_deep_pw["deep"]) > 0.02:
                n_compared += 1
                if _argmax(std_deep_tag) == _argmax(std_deep_pw):
                    n_agree += 1
                else:
                    flag = "  <-- std/deep argmax DISAGREES tag-vs-pairwise"
            print(f"    {dim:8s}  tag[{tag_line}]  pairwise[{pw_line}]{flag}")
    return n_compared, n_agree


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None, help="Article names (default: all found under pairwise_pilot/)")
    parser.add_argument("--json-out", type=Path, default=None, help="Optional path to write a machine-readable JSON summary")
    args = parser.parse_args()

    articles = args.articles
    if articles is None:
        if not _PAIRWISE_DIR.exists():
            print(f"No pairwise pilot data found at {_PAIRWISE_DIR}")
            return
        articles = sorted(p.name for p in _PAIRWISE_DIR.iterdir() if p.is_dir())

    all_reports = []
    total_compared = total_agree = 0
    for article in articles:
        try:
            report = reconcile_article(article)
        except FileNotFoundError as exc:
            print(f"SKIP {article}: {exc}")
            continue
        n_compared, n_agree = _print_report(report)
        total_compared += n_compared
        total_agree += n_agree
        all_reports.append(report)

    if total_compared:
        print("=" * 100)
        print(
            f"STANDARD-vs-DEEP argmax agreement (tag-based vs pairwise-reconciled), "
            f"non-trivial cases only: {total_agree}/{total_compared} ({100 * total_agree / total_compared:.0f}%)"
        )

    if args.json_out:
        args.json_out.write_text(json.dumps(all_reports, indent=2), encoding="utf-8")
        print(f"\nWrote {args.json_out}")


if __name__ == "__main__":
    main()
