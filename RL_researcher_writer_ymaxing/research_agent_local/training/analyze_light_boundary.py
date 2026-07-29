"""Free first-look analysis: is light's tier-1 credit ALSO miscalibrated?

Reuses the ALREADY-COLLECTED single-draw pairwise judgments from the original
6-article pilot (rl_training_data/pairwise_pilot/<article>/pairwise_judgments.json
-- graded once, 137 calls already spent) to check whether the SAME kind of
tag-vs-pairwise disagreement found for standard_vs_deep (see pairwise_reward.py /
analyze_stddeep_scale.py / repo memory) also shows up for light_vs_standard and
light_vs_deep -- WITHOUT spending any new API calls.

This is a preliminary, single-draw, small-sample (6 articles) look -- the same
caveats apply as the ORIGINAL standard-vs-deep pilot before it was repeat-confirmed
and scaled up. Treat any signal here as "worth investing in a proper repeat-draws
+ scaled check", not as a validated finding on its own.

Does NOT call any LLM -- pure re-analysis of already-collected data.

Usage (from research_agent_local/training/):
  python3 analyze_light_boundary.py
  python3 analyze_light_boundary.py --pair light_vs_deep
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from pairwise_reward import PREFERENCE_TO_DELTA, _PAIRWISE_DIR, _tag_credits_for_arm
import generate_episode_oracles as geo

_STRONG_MARGIN = 0.05
_DIMENSIONS = ("depth", "breadth")
_ARTICLES = [
    "09_RAG__var_standard", "06_tools__var_standard", "13_agent_framework",
    "Dark_Dimension", "HNSW", "08_react_practice__var_demanding",
]


def _classify(tag_margin: float, pw_margin: float) -> str:
    if abs(tag_margin) < 0.02 and abs(pw_margin) < 0.02:
        return "trivial"
    if abs(tag_margin) >= _STRONG_MARGIN and abs(pw_margin) >= _STRONG_MARGIN:
        return "strong_agree" if (tag_margin > 0) == (pw_margin > 0) else "strong_disagree"
    return "weak"


def _delta_in_frame(preference: str, a_arm: str, b_arm: str, arm_x: str, arm_y: str) -> float | None:
    """Return delta(arm_y) - delta(arm_x) implied by one pairwise judgment, in the
    caller-specified (arm_x, arm_y) frame, correcting for the recorded A/B slot.
    """
    if preference not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[preference]  # positive means B > A
    if a_arm == arm_x and b_arm == arm_y:
        return raw
    if a_arm == arm_y and b_arm == arm_x:
        return -raw
    raise ValueError(f"Unexpected arm pair: {a_arm}/{b_arm} vs requested {arm_x}/{arm_y}")


def _lookup_tag_credit(tag_credits_for_arm: dict[str, dict[str, float]], norm_title: str, dim: str, idx: int | None = None) -> float:
    """Same 3-tier lookup as pairwise_reward.py's copy: exact -> substring ->
    ordinal-position fallback (needed since a grader's reasoning.json title can
    paraphrase away a word relative to the article.md heading, breaking
    substring containment in both directions -- see pairwise_reward.py's
    docstring for the real anomaly that surfaced this).
    """
    if norm_title in tag_credits_for_arm:
        return tag_credits_for_arm[norm_title][dim]
    for k, v in tag_credits_for_arm.items():
        if norm_title in k or k in norm_title:
            return v[dim]
    if idx is not None:
        values = list(tag_credits_for_arm.values())
        if idx < len(values):
            return values[idx][dim]
    return 0.0


def analyze(pair_key: str, arm_x: str, arm_y: str) -> None:
    rows = []
    for article in _ARTICLES:
        path = _PAIRWISE_DIR / article / "pairwise_judgments.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        tag_x = _tag_credits_for_arm(article, arm_x)
        tag_y = _tag_credits_for_arm(article, arm_y)

        for idx, (title, sec) in enumerate(data["sections"].items()):
            entry = sec.get(pair_key)
            if not entry or "error" in entry:
                continue
            a_arm, b_arm = entry["a_arm"], entry["b_arm"]
            norm_title = geo._normalize(title)
            for dim in _DIMENSIONS:
                dim_judgment = entry.get(dim)
                if not dim_judgment:
                    continue
                delta = _delta_in_frame(dim_judgment["preference"], a_arm, b_arm, arm_x, arm_y)
                if delta is None:
                    continue
                tag_margin = _lookup_tag_credit(tag_y, norm_title, dim, idx) - _lookup_tag_credit(tag_x, norm_title, dim, idx)
                kind = _classify(tag_margin, delta)
                rows.append(
                    {"article": article, "section": title, "dim": dim, "tag_margin": tag_margin,
                     "pw_margin": delta, "preference": dim_judgment["preference"], "classification": kind}
                )

    print("=" * 100)
    print(f"Pair: {pair_key}  (margin convention: {arm_y} minus {arm_x})")
    print("=" * 100)
    for r in rows:
        print(
            f"{r['article'][:32]:32s} {r['section'][:30]:30s} {r['dim']:8s} "
            f"tag={r['tag_margin']:+.3f} pw={r['pw_margin']:+.3f} [{r['classification']:15s}] pref={r['preference']}"
        )

    n = len(rows)
    if n < 2:
        print("Not enough data.")
        return

    def _pearson(xs, ys):
        mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
        cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        vx = sum((x - mx) ** 2 for x in xs)
        vy = sum((y - my) ** 2 for y in ys)
        return cov / (vx * vy) ** 0.5 if vx > 0 and vy > 0 else 0.0

    tag_vals = [r["tag_margin"] for r in rows]
    pw_vals = [r["pw_margin"] for r in rows]
    r_pearson = _pearson(tag_vals, pw_vals)
    trivial = sum(1 for r in rows if r["classification"] == "trivial")
    weak = sum(1 for r in rows if r["classification"] == "weak")
    agree = sum(1 for r in rows if r["classification"] == "strong_agree")
    disagree = sum(1 for r in rows if r["classification"] == "strong_disagree")
    dir_tag_y_pw_x = sum(1 for r in rows if r["classification"] == "strong_disagree" and r["tag_margin"] > 0)
    dir_tag_x_pw_y = sum(1 for r in rows if r["classification"] == "strong_disagree" and r["tag_margin"] < 0)

    print("=" * 100)
    print(f"N (section, dimension) observations: {n}")
    print(f"Pearson correlation (tag_margin vs single-draw pairwise_margin): r={r_pearson:+.3f}")
    print(f"trivial={trivial}  weak={weak}  strong_agree={agree}  strong_disagree={disagree}")
    if disagree:
        print(
            f"Direction split among strong_disagree: tag favors {arm_y}/pairwise favors {arm_x}: {dir_tag_y_pw_x}, "
            f"tag favors {arm_x}/pairwise favors {arm_y}: {dir_tag_x_pw_y}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--pair", choices=["light_vs_standard", "light_vs_deep"], default="light_vs_standard")
    args = parser.parse_args()

    arm_x, arm_y = ("light", "standard") if args.pair == "light_vs_standard" else ("light", "deep")
    analyze(args.pair, arm_x, arm_y)


if __name__ == "__main__":
    main()
