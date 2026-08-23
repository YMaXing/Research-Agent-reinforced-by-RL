"""Follow-up to A.16.4: is the "run26 deep-share mismatch" finding actually
apples-to-apples?

A.16.4 compared run26_ORD_cost-0.06's TRAIN **section-level** deep share (9/170
sections = 5.3%, from _replication_retrain_analysis.py's score_candidate(),
which tallies each of the ~170 individual GRPO training groups) against the
corrected TEST **article-level** deep share (4/16 articles = 25%, from
article_oracle.json's oracle_arm). These are different units of analysis --
an article's oracle_arm is the ARGMAX of its target-words-weighted R_w across
ALL its sections, not a majority vote of individual section winners, so
section-level and article-level shares are not guaranteed to move together.

This script redoes the comparison on a consistent unit: for each candidate
formula, aggregate each of the 24 TRAIN articles' N=3-averaged section rewards
into an article-level R_w (target-words-weighted mean of "rest" + simple mean
of "explore" -- Candidate E's real aggregation, matching compute_article_oracle.py
::_compute_r_w(), not a naive flat mean), take the argmax arm per article, and
tally THAT distribution across the 24 articles -- the proper TRAIN-side
analogue of TEST's article-level oracle_arm distribution.

Read-only, zero LLM calls.
Usage (from research_agent_local/): python3 training/_article_level_formula_check.py
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import generate_episode_oracles as geo  # noqa: E402
import _replication_retrain_analysis as rra  # noqa: E402

ARMS = rra.ARMS
_BASES = rra._BASES
_TRAIN_ARTICLES = rra._TRAIN_ARTICLES


def _mk_split(*, w_cc, w_fl, w_de, w_be, w_ga_gate_pen, cost_coef=-0.03, ga_thresh=0.5, ordinal_cost=False):
    """Same formula as rra._mk(), but returns (rest, explore) separately so
    article-level aggregation can apply Candidate E's split-weighting correctly."""
    def f(v, nr):
        gt_base = w_cc * v["cc"] + w_fl * v["fl"]
        explore = v["cp"] * (w_de * v["de"] + w_be * v["be"])
        gate = -w_ga_gate_pen if v["ga"] < ga_thresh else 0.0
        rest = gt_base + gate + cost_coef * nr
        return rest, explore
    f._ordinal_cost = ordinal_cost
    return f


CANDIDATES_SPLIT = {
    "C2_shipped":         _mk_split(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10),
    "run26_ORD_cost-0.06": _mk_split(w_cc=0.20, w_fl=0.20, w_de=0.45, w_be=0.30, w_ga_gate_pen=0.10,
                                      cost_coef=-0.06, ordinal_cost=True),
}


def _nr(arm, fn):
    return rra._ORDINAL_UNITS[arm] if getattr(fn, "_ordinal_cost", False) else geo._ARM_COST_UNITS[arm]


def article_level_distribution(corpus, fn, feats_by_article):
    """(dist, n_articles) -- article-level oracle_arm tally under formula fn,
    N=3-averaged, Candidate-E split-weighted aggregation, no S3/S4/S5 tie-break
    (formula-only comparison; near-tie tie-break is formula-agnostic so omitting
    it doesn't bias a cross-formula distributional comparison)."""
    by_article: dict[str, list[tuple[str, dict]]] = {}
    for key, per_arm in corpus:
        art = next(a for a in _TRAIN_ARTICLES if key.startswith(a + "__S"))
        by_article.setdefault(art, []).append((key, per_arm))

    dist = {a: 0 for a in ARMS}
    detail = []
    for art, sections in by_article.items():
        feats = feats_by_article.get(art, {})
        acc_rest = {a: 0.0 for a in ARMS}
        acc_explore = {a: 0.0 for a in ARMS}
        total_w = 0
        n = 0
        for key, per_arm in sections:
            sid = key[len(art) + 2:]
            tw = feats.get(sid, {}).get("target_words")
            tw = int(tw) if tw is not None else 100
            total_w += tw
            n += 1
            for a in ARMS:
                vals = [fn(per_arm[a][d], _nr(a, fn)) for d in range(3)]
                rest = statistics.mean(v[0] for v in vals)
                explore = statistics.mean(v[1] for v in vals)
                acc_rest[a] += tw * rest
                acc_explore[a] += explore
        r_w = {a: (acc_rest[a] / total_w if total_w else 0.0) + (acc_explore[a] / n if n else 0.0) for a in ARMS}
        winner = max(ARMS, key=r_w.__getitem__)
        dist[winner] += 1
        detail.append((art, winner, r_w))
    return dist, len(by_article), detail


def main():
    corpus = rra.load_train_draws()
    feats_by_article = {}
    for art in _TRAIN_ARTICLES:
        p = _BASES / art / "guideline_features.json"
        if p.exists():
            feats_by_article[art] = json.loads(p.read_text(encoding="utf-8")).get("sections", {})

    print("=" * 100)
    print("ARTICLE-LEVEL (not section-level) TRAIN oracle_arm distribution, N=3-averaged, per formula")
    print("=" * 100)
    print(f"{'candidate':<22} {'sk/li/st/dp':>14}   {'deep share':>10}")
    for name, fn in CANDIDATES_SPLIT.items():
        dist, n, detail = article_level_distribution(corpus, fn, feats_by_article)
        dist_s = "/".join(str(dist[a]) for a in ARMS)
        print(f"{name:<22} {dist_s:>14}   {dist['deep']/n:>9.1%}   (n={n} articles)")
        if name == "run26_ORD_cost-0.06":
            print("  per-article winner:")
            for art, winner, r_w in sorted(detail):
                print(f"    {art:<44} {winner:<9} R_w={{{', '.join(f'{a}:{r_w[a]:.3f}' for a in ARMS)}}}")

    print()
    print("Corrected TEST article-level distribution (A.15.4, for comparison): sk/li/st/dp = 2/7/3/4")
    print(f"  TEST deep share: 4/16 = {4/16:.1%}")


if __name__ == "__main__":
    main()
