"""Moderated significance test for near-tie article oracles (A.16.9).

Motivation
----------
`compute_article_oracle.py`'s `needs_review` flag uses ONE pooled noise
threshold (`ARTICLE_MARGIN_NOISE_SD=0.054 / sqrt(n_draws)`) for every article,
regardless of how much that specific article's own 3 draws (production + 2
replicates) actually agree or disagree. This script asks a more precise
question per flagged article: "given THIS article's own realized round-to-
round variability, is its margin actually distinguishable from noise?"

Naively this would be a per-article Welch/one-sample t-test on the 3 known
per-round margins -- but with only n=3 draws (df=2), a per-article sample
variance is itself extremely unreliable (a single article can look
artificially "clean" or "noisy" by chance). The statistically correct fix
for "many units, each with very few replicates, but a large corpus available
to characterize what typical per-unit noise looks like" is an Empirical Bayes
MODERATED t-test (Smyth 2004, "Linear Models and Empirical Bayes Methods for
Assessing Differential Expression in Microarray Experiments" -- the standard
solution in genomics for many genes x few replicate arrays each; here: ~30
articles x 3 draws each plays the same role as genes x arrays).

Method
------
1. For every article with real (non-manual-override) replicate data, compute
   the 3 per-round article-level R_w[winner] - R_w[runner_up] margins, using
   the exact weighting compute_article_oracle.py::_compute_r_w() uses
   (target-words-weighted "rest" + simple-mean "explore").
2. Each article's sample variance s_i^2 (df=2) is combined with the pooled
   prior variance s0^2 (mean of all s_i^2 across the corpus) via an
   Empirical-Bayes moderated estimate, using a fitted prior weight d0:
       moderated_var = (d0*s0^2 + d_i*s_i^2) / (d0 + d_i),  df = d0 + d_i
   d0 is fit by matching the empirical variance of log(s_i^2) across
   articles to its theoretical value under the hierarchical model
   (Var(log(s_i^2)) = trigamma(d_i/2) + trigamma(d0/2), a standard moment of
   the log-F distribution) -- implemented stdlib-only (no scipy in this venv).
3. One-sided one-sample t-test per flagged article: H1: true mean margin > 0
   (testing whether the ALREADY-OBSERVED winner is significantly ahead, not
   searching for any difference in either direction).

All three numerical building blocks (trigamma, the d0 method-of-moments
fit, and the Student's t upper-tail p-value via the regularized incomplete
beta function) are validated against known-answer synthetic data / textbook
t-table values in `self_test()` before being trusted on real data -- run with
`--self-test` to re-verify.

Usage (from research_agent_local/training/):
    python3 margin_moderated_significance.py                  # all currently-flagged articles
    python3 margin_moderated_significance.py --articles HNSW 07_reasoning_planning
    python3 margin_moderated_significance.py --self-test
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
import measure_replicate_noise as mrn  # noqa: E402

_REPO_ROOT = _THIS_DIR.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

_TRAIN_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns", "06_tools",
    "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_TRAIN_VARIANTS = [f"{t}__var_{v}" for t in _TRAIN_LESSONS for v in ("minimal", "standard", "demanding")]
_TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework", "14_agent_system_design",
    "29_evaluation_metrics", "31_CI", "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW", "Insects_Consciousness", "Space-Time_QECC",
    "State_of_LLM_Reasoning", "Understanding_Reasoning_LLMs",
]
ALL_ARTICLES = _TRAIN_VARIANTS + _TEST_ARTICLES

D_I = 2  # per-article df = n_draws - 1 = 3 - 1, fixed across this corpus


# ---------------------------------------------------------------------------
# Per-round article-level R_w  (mirrors compute_article_oracle.py::_compute_r_w)
# ---------------------------------------------------------------------------
def _article_level_r_w(sections: dict, features_sections: dict, arm: str) -> float:
    total_w = 0
    n_sections = 0
    acc_rest = 0.0
    acc_explore = 0.0
    for sec_id, info in sections.items():
        feat = features_sections.get(sec_id, {})
        tw_val = feat.get("target_words")
        tw = int(tw_val) if tw_val is not None else 100
        total_w += tw
        n_sections += 1
        rewards = info["rewards"]
        explore = info.get("explore", {})
        acc_rest += tw * (float(rewards.get(arm, 0.0)) - float(explore.get(arm, 0.0)))
        acc_explore += float(explore.get(arm, 0.0))
    if total_w == 0 or n_sections == 0:
        return 0.0
    return acc_rest / total_w + acc_explore / n_sections


def per_round_margins(article: str):
    """Return (round_margins[3], winner, runner_up, stored_margin) or None."""
    oracle_path = _BASES_DIR / article / "article_oracle.json"
    if not oracle_path.exists():
        return None
    oracle = json.loads(oracle_path.read_text(encoding="utf-8"))
    if oracle.get("manual_override"):
        return None  # not decided by r_w argmax -- no "margin noise" to measure
    winner = oracle["oracle_arm"]
    runner_up = oracle.get("runner_up_arm")
    if runner_up is None:
        return None  # forbidden-policy articles never computed a runner-up

    avg_path = _BASES_DIR / article / "section_oracle_averaged.json"
    prod_path = _BASES_DIR / article / "section_oracle.json"
    feat_path = _BASES_DIR / article / "guideline_features.json"
    if not avg_path.exists() or not prod_path.exists():
        return None
    avg = json.loads(avg_path.read_text(encoding="utf-8"))
    prod = json.loads(prod_path.read_text(encoding="utf-8"))
    feat = json.loads(feat_path.read_text(encoding="utf-8"))["sections"]
    replicate_ids = avg.get("replicate_ids_used", [])
    if not replicate_ids:
        return None

    prod_sec_ids = mrn._production_sec_ids(article)
    sec_ids = list(prod["sections"].keys())
    if not prod_sec_ids or not set(sec_ids).issubset(set(prod_sec_ids)):
        prod_sec_ids = sec_ids

    rounds = [prod["sections"]]
    for r in replicate_ids:
        prefix = mrn._NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}"
        rounds.append(mrn._compute_replicate_sections(article, prefix, prod_sec_ids, cost_formula="c2"))

    margins = [
        _article_level_r_w(rd, feat, winner) - _article_level_r_w(rd, feat, runner_up)
        for rd in rounds
    ]
    return margins, winner, runner_up, oracle["margin"]


# ---------------------------------------------------------------------------
# Empirical-Bayes prior fit (Smyth 2004), stdlib-only
# ---------------------------------------------------------------------------
def trigamma(x: float) -> float:
    """psi1(x) via recurrence (shift to x>=6) + Abramowitz & Stegun 6.4.12 series."""
    x = float(x)
    result = 0.0
    while x < 6.0:
        result += 1.0 / (x * x)
        x += 1.0
    inv_x = 1.0 / x
    inv_x2 = inv_x * inv_x
    result += (
        inv_x + 0.5 * inv_x2
        + inv_x2 * inv_x * (1.0 / 6.0 - inv_x2 * (1.0 / 30.0 - inv_x2 * (1.0 / 42.0 - inv_x2 / 30.0)))
    )
    return result


def _bisect_decreasing(f, lo: float, hi: float, tol: float = 1e-9, max_iter: int = 200) -> float:
    flo, fhi = f(lo), f(hi)
    assert flo > 0 > fhi, f"bracket does not contain root: f(lo)={flo}, f(hi)={fhi}"
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fmid = f(mid)
        if abs(fmid) < tol:
            return mid
        if fmid > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def fit_d0(sample_variances: list[float], d: int) -> float:
    """Method-of-moments estimate of prior df d0 (equal per-unit df d)."""
    log_s2 = [math.log(v) for v in sample_variances if v > 0]
    empirical_var = statistics.pvariance(log_s2)
    target = empirical_var - trigamma(d / 2.0)
    if target <= trigamma(25000.0):  # d0/2 = 25000 -> d0 = 50000, ~0 excess variance
        return float("inf")
    return 2.0 * _bisect_decreasing(lambda half: trigamma(half) - target, 1e-6, 1e7)


# ---------------------------------------------------------------------------
# Student's t upper-tail p-value via regularized incomplete beta, stdlib-only
# ---------------------------------------------------------------------------
def _betacf(a, b, x, max_iter=200, eps=1e-12):
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    d = 1e-30 if abs(d) < 1e-30 else d
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1e-30 if abs(d) < 1e-30 else d
        c = 1.0 + aa / c
        c = 1e-30 if abs(c) < 1e-30 else c
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1e-30 if abs(d) < 1e-30 else d
        c = 1.0 + aa / c
        c = 1e-30 if abs(c) < 1e-30 else c
        d = 1.0 / d
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            break
    return h


def betainc(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    ln_beta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(math.log(x) * a + math.log(1 - x) * b - ln_beta)
    if x < (a + 1.0) / (a + b + 2.0):
        return front * _betacf(a, b, x) / a
    return 1.0 - front * _betacf(b, a, 1 - x) / b


def t_sf(t: float, df: float) -> float:
    """One-sided upper-tail p-value P(T > t) for Student's t."""
    if df == float("inf"):
        return 0.5 * math.erfc(t / math.sqrt(2))
    if t <= 0:
        return 1.0 - t_sf(-t, df)
    x = df / (df + t * t)
    return 0.5 * betainc(df / 2.0, 0.5, x)


def moderated_t(mean_margin: float, s_i_sq: float, n: int, d0: float, s0_sq: float):
    if math.isinf(d0):
        mod_var, df = s0_sq, float("inf")
    elif d0 == 0.0:
        mod_var, df = s_i_sq, D_I
    else:
        mod_var = (d0 * s0_sq + D_I * s_i_sq) / (d0 + D_I)
        df = d0 + D_I
    se = math.sqrt(mod_var / n)
    t_stat = mean_margin / se if se > 0 else float("inf")
    return t_stat, df, t_sf(t_stat, df)


# ---------------------------------------------------------------------------
# Self-test: verify the machinery on known-answer data before trusting it
# ---------------------------------------------------------------------------
def self_test() -> None:
    print("trigamma(1) should be pi^2/6 = 1.644934...")
    print(f"  got {trigamma(1.0):.6f}\n")

    print("Student's t upper-tail p-value vs. known t-table critical values:")
    checks = [(2, 4.303, 0.025), (2, 2.920, 0.05), (10, 1.812, 0.05), (1, 1.0, 0.25)]
    for df, t, expected in checks:
        got = t_sf(t, df)
        ok = "OK" if abs(got - expected) < 0.001 else "MISMATCH"
        print(f"  df={df:<4} t={t:<6.3f} expected_p={expected:<7.4f} got={got:.4f}  {ok}")

    print("\nfit_d0() recovers a known d0 from simulated data (median over 300 trials):")
    random.seed(0)
    for true_d0, true_s0_sq in [(4.0, 0.05 ** 2), (10.0, 0.05 ** 2)]:
        recovered = []
        for _ in range(300):
            sample_vars = []
            for _ in range(30):
                chi_d0 = max(sum(random.gauss(0, 1) ** 2 for _ in range(int(true_d0))), 1e-9)
                sigma_i_sq = true_s0_sq * true_d0 / chi_d0
                chi_di = sum(random.gauss(0, 1) ** 2 for _ in range(D_I))
                sample_vars.append(sigma_i_sq * chi_di / D_I)
            recovered.append(fit_d0(sample_vars, D_I))
        finite = [r for r in recovered if math.isfinite(r)]
        med = statistics.median(finite) if finite else float("nan")
        print(f"  true_d0={true_d0:<6.1f} -> median estimate={med:.2f}  ({len(finite)}/300 finite)")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def _currently_flagged_articles() -> list[str]:
    out = []
    for art in ALL_ARTICLES:
        p = _BASES_DIR / art / "article_oracle.json"
        if p.exists() and json.loads(p.read_text(encoding="utf-8")).get("needs_review"):
            out.append(art)
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None, help="Articles to test (default: all currently needs_review=True).")
    parser.add_argument("--self-test", action="store_true", help="Run numerical self-checks and exit.")
    parser.add_argument("--alpha", type=float, default=0.10, help="Significance threshold (default 0.10, one-sided).")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return

    targets = args.articles or _currently_flagged_articles()

    calib = {}
    for art in ALL_ARTICLES:
        r = per_round_margins(art)
        if r is None:
            continue
        margins, winner, runner_up, stored_margin = r
        calib[art] = (statistics.mean(margins), statistics.variance(margins), winner, runner_up, stored_margin)

    sample_vars = [v[1] for v in calib.values() if v[1] > 0]
    d0 = fit_d0(sample_vars, D_I)
    s0_sq = statistics.mean(sample_vars)
    print(f"Calibration corpus: {len(calib)} articles (manual-override / no-replicate-data articles excluded)")
    print(f"Fitted prior d0={d0:.2f}   s0={math.sqrt(s0_sq):.4f}   (alpha={args.alpha}, one-sided)\n")

    header = f"{'article':<42} {'winner':<9} {'margin':>8}  {'no-pool p':>10}  {'moderated p':>12} (df)   {'full-pool p':>12}   verdict"
    print(header)
    for art in targets:
        if art not in calib:
            print(f"{art:<42}  -- not eligible (manual override / no replicate data)")
            continue
        mean_m, s_i_sq, winner, runner_up, stored_margin = calib[art]
        _, _, p0 = moderated_t(mean_m, s_i_sq, 3, 0.0, s0_sq)
        _, dfm, pm = moderated_t(mean_m, s_i_sq, 3, d0, s0_sq)
        _, _, pf = moderated_t(mean_m, s_i_sq, 3, float("inf"), s0_sq)
        verdict = f"SIGNIFICANT (p<{args.alpha})" if pm < args.alpha else "still ambiguous"
        print(f"{art:<42} {winner:<9} {mean_m:>+8.4f}  {p0:>10.4f}  {pm:>12.4f} ({dfm:>5.1f})   {pf:>12.4f}   {verdict}")


if __name__ == "__main__":
    main()
