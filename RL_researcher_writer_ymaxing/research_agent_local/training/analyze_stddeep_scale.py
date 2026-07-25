"""Analyze the scaled standard-vs-deep-only pairwise grading check.

Consumes rl_training_data/pairwise_stddeep_scale/<article>/stddeep_judgments.json
(written by writing_workflow/rl_pairwise_stddeep_scale.py -- N draws per section,
standard_vs_deep only, majority-vote-by-design) and compares the majority-voted
pairwise margin against the existing tag-based enhancement_credit() margin for
the SAME sections, replicating (independently, on a larger/more diverse article
sample) the directional-bias check from the repeat-draws noise-floor check.

Does NOT call any LLM -- pure post-hoc analysis, reuses _tag_credits_for_arm
from pairwise_reward.py (no reimplementation of the tag-parsing/credit logic).

Usage (from research_agent_local/training/):
  python3 analyze_stddeep_scale.py
  python3 analyze_stddeep_scale.py --articles 02_workflows_vs_agents__var_standard ...
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from pairwise_reward import PREFERENCE_TO_DELTA, _tag_credits_for_arm
import generate_episode_oracles as geo

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_SCALE_DIR = _REPO_ROOT / "rl_training_data" / "pairwise_stddeep_scale"

_STRONG_MARGIN = 0.05


def _classify(tag_margin: float, pw_margin: float) -> str:
    if abs(tag_margin) < 0.02 and abs(pw_margin) < 0.02:
        return "trivial"
    if abs(tag_margin) >= _STRONG_MARGIN and abs(pw_margin) >= _STRONG_MARGIN:
        return "strong_agree" if (tag_margin > 0) == (pw_margin > 0) else "strong_disagree"
    return "weak"


def _delta_in_std_deep_frame(preference: str, a_arm: str, b_arm: str) -> float | None:
    if preference not in PREFERENCE_TO_DELTA:
        return None
    raw = PREFERENCE_TO_DELTA[preference]  # positive means B > A
    if a_arm == "standard" and b_arm == "deep":
        return -raw
    if a_arm == "deep" and b_arm == "standard":
        return raw
    raise ValueError(f"Unexpected arm pair: {a_arm}/{b_arm}")


def _lookup_tag_credit(tag_credits_for_arm: dict[str, dict[str, float]], norm_title: str, dim: str) -> float:
    if norm_title in tag_credits_for_arm:
        return tag_credits_for_arm[norm_title][dim]
    for k, v in tag_credits_for_arm.items():
        if norm_title in k or k in norm_title:
            return v[dim]
    return 0.0


def analyze(articles: list[str]) -> None:
    rows = []
    for article in articles:
        path = _SCALE_DIR / article / "stddeep_judgments.json"
        if not path.exists():
            print(f"SKIP {article}: no data at {path}")
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        tag_standard = _tag_credits_for_arm(article, "standard")
        tag_deep = _tag_credits_for_arm(article, "deep")

        for title, entry in data["sections"].items():
            a_arm, b_arm = entry["a_arm"], entry["b_arm"]
            norm_title = geo._normalize(title)
            for dim in ("depth", "breadth"):
                prefs = [d[dim]["preference"] for d in entry["draws"] if "error" not in d]
                deltas = [dd for p in prefs if (dd := _delta_in_std_deep_frame(p, a_arm, b_arm)) is not None]
                if not deltas:
                    continue
                pw_margin = sum(deltas) / len(deltas)
                tag_margin = _lookup_tag_credit(tag_standard, norm_title, dim) - _lookup_tag_credit(tag_deep, norm_title, dim)
                kind = _classify(tag_margin, pw_margin)
                rows.append(
                    {
                        "article": article, "section": title, "dim": dim,
                        "tag_margin": tag_margin, "pw_margin": pw_margin,
                        "n_draws": len(prefs), "labels": dict(Counter(prefs)), "classification": kind,
                    }
                )

    print("=" * 100)
    for r in rows:
        print(
            f"{r['article'][:32]:32s} {r['section'][:30]:30s} {r['dim']:8s} "
            f"tag={r['tag_margin']:+.3f} pw={r['pw_margin']:+.3f} [{r['classification']:15s}] labels={r['labels']}"
        )

    n = len(rows)
    if n < 2:
        print("Not enough data to compute aggregate statistics.")
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

    dir_tag_deep_pw_std = sum(1 for r in rows if r["classification"] == "strong_disagree" and r["tag_margin"] < 0)
    dir_tag_std_pw_deep = sum(1 for r in rows if r["classification"] == "strong_disagree" and r["tag_margin"] > 0)

    print("=" * 100)
    print(f"N (section, dimension) observations: {n}")
    print(f"Pearson correlation (tag_margin vs majority-voted pairwise_margin, standard-deep): r={r_pearson:+.3f}")
    print(f"trivial={trivial}  weak={weak}  strong_agree={agree}  strong_disagree={disagree}")
    if disagree:
        print(
            f"Direction split among strong_disagree: tag=deep/pairwise=standard: {dir_tag_deep_pw_std}, "
            f"tag=standard/pairwise=deep: {dir_tag_std_pw_deep}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None, help="Default: all articles found under pairwise_stddeep_scale/")
    args = parser.parse_args()

    articles = args.articles
    if articles is None:
        if not _SCALE_DIR.exists():
            print(f"No data found at {_SCALE_DIR}")
            return
        articles = sorted(p.name for p in _SCALE_DIR.iterdir() if p.is_dir())

    analyze(articles)


if __name__ == "__main__":
    main()
