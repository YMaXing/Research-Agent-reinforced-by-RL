"""Stage B (no scipy dependency -- matches this codebase's stdlib-only-script
convention, e.g. _infer_config.py): fit the Empirical-Bayes prior (d0, s0^2)
for a moderated t-test, Smyth (2004)-style ("Linear Models and Empirical Bayes
Methods for Assessing Differential Expression in Microarray Experiments") --
the standard solution for "many units, each with very few replicates, but a
reliable pooled estimate of typical per-unit variance" (here: 30 articles x
n=3 draws each, vs. genes x few replicate arrays in the original application).

Model: s_i^2 | sigma_i^2 ~ sigma_i^2 * ChiSq(d_i)/d_i   (sampling variance)
       sigma_i^2         ~ scaled-inv-ChiSq(d0, s0^2)   (prior across units)
=> s_i^2/s0^2 ~ F(d_i, d0), so Var(log(s_i^2)) = trigamma(d_i/2) + trigamma(d0/2)
   (a standard moment of the log-F distribution).

Since every article here has the SAME d_i = d = 2 (n=3 draws), estimate d0 by
matching the empirical variance of log(s_i^2) across articles to this formula,
solved numerically for d0 via bisection on trigamma (monotone decreasing).

SELF-TEST FIRST: simulate synthetic s_i^2 from a KNOWN d0, verify the estimator
recovers it, before trusting it on real data.
"""
import math
import random
import statistics


def trigamma(x: float) -> float:
    """psi1(x), via recurrence (shift to x>=6) + Abramowitz & Stegun 6.4.12 asymptotic series."""
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


def _bisect_decreasing(f, lo: float, hi: float, target_zero_tol: float = 1e-9, max_iter: int = 200) -> float:
    """Root-find f (strictly decreasing) on [lo, hi] via bisection."""
    flo, fhi = f(lo), f(hi)
    assert flo > 0 > fhi, f"bracket does not contain root: f(lo)={flo}, f(hi)={fhi}"
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fmid = f(mid)
        if abs(fmid) < target_zero_tol:
            return mid
        if fmid > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def fit_d0(sample_variances: list[float], d: int) -> float:
    """Method-of-moments estimate of prior df d0, given equal per-unit df d."""
    log_s2 = [math.log(v) for v in sample_variances if v > 0]
    empirical_var = statistics.pvariance(log_s2)
    target = empirical_var - trigamma(d / 2.0)

    huge_d0_floor = trigamma(50000.0 / 2.0)  # trigamma(d0/2) as d0->infinity -> 0+
    if target <= huge_d0_floor:
        return float("inf")  # no excess variance beyond per-draw sampling noise

    return 2.0 * _bisect_decreasing(lambda d0_half2: trigamma(d0_half2 / 2.0) - target, 1e-6, 1e7)


def _self_test():
    random.seed(0)
    n_units = 30
    d_i = 2  # matches n=3 draws per article -> df = n-1 = 2
    print(f"{'true_d0':>8} {'true_s0':>8}  {'median_est_d0':>14}  finite_trials")
    for true_d0, true_s0_sq in [(4.0, 0.05 ** 2), (10.0, 0.05 ** 2), (2.0, 0.03 ** 2), (30.0, 0.05 ** 2)]:
        recovered = []
        for _trial in range(300):
            sample_vars = []
            for _ in range(n_units):
                chi_d0 = sum(random.gauss(0, 1) ** 2 for _ in range(int(true_d0)))
                chi_d0 = max(chi_d0, 1e-9)
                sigma_i_sq = true_s0_sq * true_d0 / chi_d0
                chi_di = sum(random.gauss(0, 1) ** 2 for _ in range(d_i))
                s_i_sq = sigma_i_sq * chi_di / d_i
                sample_vars.append(s_i_sq)
            est = fit_d0(sample_vars, d_i)
            recovered.append(est)
        finite = [r for r in recovered if math.isfinite(r)]
        med = statistics.median(finite) if finite else float("nan")
        print(f"{true_d0:>8.1f} {math.sqrt(true_s0_sq):>8.4f}  {med:>14.2f}  {len(finite)}/300")


if __name__ == "__main__":
    print("Sanity check: trigamma(1) should be pi^2/6 = 1.644934...")
    print(f"  trigamma(1) = {trigamma(1.0):.6f}\n")
    print("Self-test: does fit_d0() recover a known d0 from simulated data?\n")
    _self_test()
