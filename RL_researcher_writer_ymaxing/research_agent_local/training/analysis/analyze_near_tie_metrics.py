"""Mean + distribution analysis for a batch of near-tie articles whose margin
has fallen below ARTICLE_MARGIN_NOISE_SD/sqrt(n_draws_used) (arbitrary N, not
just N=3 -- generalized 2026-09-08 once articles started being replicated to
N=5; see run13_rl_grok_pipeline_analysis.md rl_reward_oracle_investigation.md
for why the old df=2-only closed form was a real latent bug for any N != 3).

For each article's (oracle_arm, runner_up_arm) pair, reports:
  1. Distributional basis -- per-draw R_w margin (winner - runner_up),
     mean, sample sd, one-sample t-stat vs 0, and a two-tailed p-value
     against the null that the true mean margin is 0 (df = n_draws_used - 1,
     via the regularized incomplete beta function -- exact for any df, no
     scipy dependency needed; see ``_two_tailed_p_student_t``).
  2. Quantitative basis -- per-dimension (cc/fl/de/be/cp/ga) binary score
     means for each arm, aggregated unweighted across all sections x
     n_draws_used draws (n = n_sections*n_draws_used per arm), read directly
     from each episode's reasoning.json via review_near_tie.py's own
     section/title-matching and block-extraction helpers -- no markdown
     re-parsing, no reward-formula duplication.

Read-only, zero new API calls.

Usage (from research_agent_local/training/):
    python3 analyze_near_tie_metrics.py
    python3 analyze_near_tie_metrics.py --article HNSW
    python3 analyze_near_tie_metrics.py --article 29_evaluation_metrics --arms standard deep
        -> compares any two arms directly, instead of the default oracle_arm vs runner_up_arm
"""
from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import review_near_tie as rnt  # noqa: E402
import compute_article_oracle as cao  # noqa: E402
import full_corpus_per_draw_rw_table as fcpt  # noqa: E402

BASES_DIR = cao._BASES_DIR

DEFAULT_ARTICLES = [
    "Understanding_Reasoning_LLMs",
    "29_evaluation_metrics",
    "Gravity_Entropy",
    "13_agent_framework",
]

_SCORE_RE = re.compile(r"\*\*([01])(?:\.\d+)?:\*\*")


def _betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta function (Numerical Recipes 6.4.6)."""
    MAXIT, EPS, FPMIN = 200, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1.0 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1.0 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < EPS:
            break
    return h


def _betainc(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta function I_x(a, b), x in [0, 1]."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_beta = math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
    front = math.exp(ln_beta + a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1.0 - x) / b


def _two_tailed_p_student_t(t: float, df: int) -> float:
    """Two-tailed p-value for Student's t with `df` degrees of freedom, via the
    regularized incomplete beta function: P(|T|>|t|) = I_{df/(df+t^2)}(df/2, 1/2).
    Exact for any df (verified to reduce to the old df=2 closed form,
    F(t)=1/2*(1+t/sqrt(2+t^2)), when df=2) -- no scipy dependency needed."""
    x = df / (df + t * t)
    return _betainc(df / 2.0, 0.5, x)


def distributional_basis(article: str, winner: str, runner_up: str) -> dict:
    result = fcpt.per_article_full_table(article)
    if result is None:
        raise RuntimeError(f"{article}: not eligible (missing files or n_draws_used < 2)")
    per_draw_r_w = result["per_draw_r_w"]
    draw_names = list(per_draw_r_w.keys())  # production first, then replicate1..N in order
    margins = [per_draw_r_w[d][winner] - per_draw_r_w[d][runner_up] for d in draw_names]
    n = len(margins)
    mean = statistics.mean(margins)
    sd = statistics.stdev(margins)  # sample sd, ddof=1, matches article_margin noise-floor convention
    t_stat = mean / (sd / (n ** 0.5)) if sd > 0 else float("inf")
    p_value = _two_tailed_p_student_t(t_stat, df=n - 1) if sd > 0 else 0.0
    n_favor_winner = sum(1 for m in margins if m > 0)
    return {
        "draw_names": draw_names,
        "margins": margins,
        "mean": mean,
        "sd": sd,
        "t_stat": t_stat,
        "df": n - 1,
        "p_value": p_value,
        "n_favor_winner": n_favor_winner,
        "n_draws": n,
    }


def _n_draws_for(article: str) -> int:
    """How many draws (production + replicates) this article's oracle was computed from."""
    oracle_path = BASES_DIR / article / "article_oracle.json"
    if not oracle_path.exists():
        return 1
    return json.loads(oracle_path.read_text(encoding="utf-8")).get("n_draws_used", 1)


def quantitative_basis(article: str, winner: str, runner_up: str) -> dict:
    contribs, _total_w = rnt._section_contributions(article, winner, runner_up)
    arm_presets = rnt.mrn._arm_presets_for(article)
    dim_names = [d for _, d in rnt._REVIEW_DIMS]
    scores: dict[str, dict[str, list[int]]] = {
        arm: {d: [] for d in dim_names} for arm in (winner, runner_up)
    }
    n_sections = len(contribs)
    n_draws = _n_draws_for(article)
    for _contribution, sec_id, norm, _info in contribs:
        ordinal_match = re.match(r"^S(\d+)::", sec_id)
        ordinal_idx = int(ordinal_match.group(1)) - 1 if ordinal_match else -1
        for arm in (winner, runner_up):
            preset = arm_presets[arm][0]
            for draw in range(n_draws):
                ep_dir = rnt._episode_dir(article, draw, preset)
                reasoning = rnt._load_json(ep_dir / "reasoning.json")
                if reasoning is None:
                    continue
                blocks = rnt._extract_reasoning_blocks(reasoning, norm, ordinal_idx)
                for dim in dim_names:
                    block = blocks.get(dim)
                    if not block:
                        continue
                    m = _SCORE_RE.search(block)
                    if m:
                        scores[arm][dim].append(int(m.group(1)))
    means = {
        arm: {d: (statistics.mean(v) if v else None) for d, v in scores[arm].items()}
        for arm in (winner, runner_up)
    }
    counts = {
        arm: {d: len(v) for d, v in scores[arm].items()}
        for arm in (winner, runner_up)
    }
    return {"means": means, "counts": counts, "n_sections": n_sections}


def analyze_article(article: str, arms: tuple[str, str] | None = None) -> None:
    oracle = json.loads((BASES_DIR / article / "article_oracle.json").read_text(encoding="utf-8"))
    if arms:
        winner, runner_up = arms
        valid_arms = {"skip", "light", "standard", "deep"}
        if winner not in valid_arms or runner_up not in valid_arms:
            print(f"=== {article}: ERROR --arms must be two of {sorted(valid_arms)}, got {arms!r} ===\n")
            return
        stored_margin = oracle["r_w_rewards"][winner] - oracle["r_w_rewards"][runner_up]
    else:
        winner = oracle["oracle_arm"]
        runner_up = oracle.get("runner_up_arm")
        if runner_up is None:
            print(f"=== {article}: no runner_up_arm (forbidden policy / no comparison) -- skipping ===\n")
            return
        stored_margin = oracle["margin"]

    print(f"=== {article}  ({winner} vs {runner_up}, stored margin={stored_margin:+.4f}) ===")

    dist = distributional_basis(article, winner, runner_up)
    m = dist["margins"]
    n = dist["n_draws"]
    print(f"  Distributional basis: per-draw margin ({winner} - {runner_up}) = "
          f"[{', '.join(f'{v:+.4f}' for v in m)}]")
    print(f"    mean={dist['mean']:+.4f}  sd={dist['sd']:.4f}  "
          f"t={dist['t_stat']:+.3f} (df={dist['df']})  p={dist['p_value']:.3f}  "
          f"{dist['n_favor_winner']}/{n} draws favor {winner}")

    quant = quantitative_basis(article, winner, runner_up)
    print(f"  Quantitative basis: per-dimension mean scores "
          f"(n_sections={quant['n_sections']}, up to n_sections*{_n_draws_for(article)} draws per arm)")
    for dim in [d for _, d in rnt._REVIEW_DIMS]:
        w_mean = quant["means"][winner][dim]
        r_mean = quant["means"][runner_up][dim]
        w_n = quant["counts"][winner][dim]
        r_n = quant["counts"][runner_up][dim]
        w_s = f"{w_mean:.3f}" if w_mean is not None else "n/a"
        r_s = f"{r_mean:.3f}" if r_mean is not None else "n/a"
        diff = (w_mean - r_mean) if (w_mean is not None and r_mean is not None) else None
        diff_s = f"{diff:+.3f}" if diff is not None else "n/a"
        print(f"    {dim}: {winner}={w_s} (n={w_n})   {runner_up}={r_s} (n={r_n})   diff={diff_s}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--article", nargs="+", default=None,
                         help="Article(s) to analyze (default: the 4 flagged this session).")
    parser.add_argument("--arms", nargs=2, metavar=("ARM_A", "ARM_B"), default=None,
                         help="Compare these two arms directly (any of skip/light/standard/deep) "
                              "instead of the default oracle_arm vs runner_up_arm.")
    args = parser.parse_args()
    articles = args.article if args.article else DEFAULT_ARTICLES
    arms = tuple(args.arms) if args.arms else None
    for article in articles:
        try:
            analyze_article(article, arms=arms)
        except Exception as exc:
            print(f"=== {article}: ERROR: {exc} ===\n")


if __name__ == "__main__":
    main()
