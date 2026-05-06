"""Recompute section + article oracles under a prior-augmented reward.

Modified reward
---------------
    R'(s, p) = R_metric(s, p) + R_prior(s, p)

    R_prior(s, p) = -lambda * (nr(p) - mu(s))**2 / 9                       (1)

    mu(s) = clip( mu_base(variant) + a_w * w(s) + a_p * p(s) + a_d * d(s),
                  0, 3 )                                                   (2)

    nr(p) = PRESET_ROUNDS[p] in {0, 1, 2, 2, 3, 3}    # preset cost ladder

Feature transforms in (2):
    mu_base(minimal)   = 0.7
    mu_base(standard)  = 1.7
    mu_base(demanding) = 2.0
    w(s) = log2(n * weight_frac(s))         # log-importance vs average
    p(s) = -0.6 if first or last section,
           -0.3 if second or penultimate,
            0   otherwise
    d(s) = +0.4 if digest_words/target_words < 0.3 (sparse digest),
           -0.3 if digest_words/target_words > 1.0 (rich digest),
            0   otherwise (or if target_words missing)

Default coefficients (tunable via CLI):
    lambda = 0.05  ->  R_prior in [-0.05, 0]
    a_w = 0.4,  a_p = 1.0,  a_d = 1.0

Inputs : rl_training_data/bases/<article>/article_oracle.json (current oracles)
Output : prints comparison + writes article_oracle_prior.json next to each.
         No changes to the original article_oracle.json files.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants — must stay in sync with compute_article_oracle.py
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
NUM_PRESETS = 6
PRESET_NAMES = {
    0: "P0_baseline",
    1: "P1_single_balanced",
    2: "P2_balanced_depth",
    3: "P3_depth_breadth",
    4: "P4_bal_depth_breadth",
    5: "P5_depth_breadth_depth",
}
MU_BASE = {"minimal": 0.7, "standard": 1.7, "demanding": 2.0}


# ---------------------------------------------------------------------------
# Prior computation
# ---------------------------------------------------------------------------
def feature_w(weight_frac: float, n_sections: int) -> float:
    """Log-importance relative to mean section (0 when section is average size)."""
    if weight_frac <= 0 or n_sections <= 0:
        return 0.0
    return math.log2(max(weight_frac * n_sections, 1e-6))


def feature_p(idx: int, n: int) -> float:
    """Position shift: cheaper presets favoured at intro / conclusion."""
    if idx == 0 or idx == n - 1:
        return -0.6
    if idx == 1 or idx == n - 2:
        return -0.3
    return 0.0


def feature_d(digest_words: int, target_words: int | None) -> float:
    """Density shift: sparse digest -> breadth needed; rich digest -> cheaper."""
    if not target_words or target_words <= 0:
        return 0.0
    ratio = digest_words / target_words
    if ratio < 0.3:
        return 0.4
    if ratio > 1.0:
        return -0.3
    return 0.0


def expected_complexity(
    variant: str,
    weight_frac: float,
    n_sections: int,
    idx: int,
    digest_words: int,
    target_words: int | None,
    a_w: float,
    a_p: float,
    a_d: float,
) -> float:
    """Compute mu(s) per equation (2), clipped to [0, 3]."""
    mu = (
        MU_BASE[variant]
        + a_w * feature_w(weight_frac, n_sections)
        + a_p * feature_p(idx, n_sections)
        + a_d * feature_d(digest_words, target_words)
    )
    return max(0.0, min(3.0, mu))


def prior_reward(p: int, mu: float, lam: float) -> float:
    """R_prior(s, p) per equation (1).  In [-lambda, 0]."""
    return -lam * (PRESET_ROUNDS[p] - mu) ** 2 / 9.0


# ---------------------------------------------------------------------------
# Recomputation
# ---------------------------------------------------------------------------
def recompute_article(
    oracle_data: dict,
    a_w: float,
    a_p: float,
    a_d: float,
    lam: float,
) -> dict:
    """Apply prior to one article's oracle data; return augmented dict."""
    variant = oracle_data["variant_level"]
    sections = oracle_data["sections"]
    n = len(sections)

    new_sections = []
    for i, sec in enumerate(sections):
        mu = expected_complexity(
            variant=variant,
            weight_frac=sec["weight_frac"],
            n_sections=n,
            idx=i,
            digest_words=sec.get("digest_words", 0) or 0,
            target_words=sec.get("target_words"),
            a_w=a_w,
            a_p=a_p,
            a_d=a_d,
        )
        old_rewards = sec["rewards_by_preset"]
        prior = [prior_reward(p, mu, lam) for p in range(NUM_PRESETS)]
        new_rewards = [old_rewards[p] + prior[p] for p in range(NUM_PRESETS)]

        rank = sorted(range(NUM_PRESETS), key=lambda p: new_rewards[p], reverse=True)
        new_oracle = rank[0]
        new_runner = rank[1]
        new_margin = new_rewards[new_oracle] - new_rewards[new_runner]

        new_sections.append({
            **sec,
            "mu": round(mu, 4),
            "prior_by_preset": [round(x, 6) for x in prior],
            "rewards_by_preset_modified": [round(x, 6) for x in new_rewards],
            "section_oracle_new": new_oracle,
            "section_runner_up_new": new_runner,
            "section_margin_new": round(new_margin, 6),
            "oracle_changed": new_oracle != sec["section_oracle"],
        })

    # Article-level under modified rewards
    weights = [s["weight_frac"] for s in new_sections]
    article_rewards_new = [
        sum(weights[s] * new_sections[s]["rewards_by_preset_modified"][p] for s in range(n))
        for p in range(NUM_PRESETS)
    ]
    art_rank = sorted(range(NUM_PRESETS), key=lambda p: article_rewards_new[p], reverse=True)

    return {
        **oracle_data,
        "sections": new_sections,
        "article_rewards_modified": [round(r, 6) for r in article_rewards_new],
        "oracle_preset_new": art_rank[0],
        "runner_up_preset_new": art_rank[1],
        "margin_new": round(article_rewards_new[art_rank[0]] - article_rewards_new[art_rank[1]], 6),
        "prior_config": {
            "lambda": lam, "a_w": a_w, "a_p": a_p, "a_d": a_d,
            "mu_base": MU_BASE,
        },
    }


# ---------------------------------------------------------------------------
# Analysis / reporting
# ---------------------------------------------------------------------------
def near_tie_count(sections: list[dict], reward_key: str, oracle_key: str, tol: float) -> int:
    """How many sections have >= 2 presets within `tol` reward of their oracle."""
    n = 0
    for sec in sections:
        rewards = sec[reward_key]
        oracle_r = rewards[sec[oracle_key]]
        if sum(1 for r in rewards if oracle_r - r <= tol) >= 2:
            n += 1
    return n


def analyse(all_articles: list[dict]) -> None:
    flat = [s for art in all_articles for s in art["sections"]]
    n_total = len(flat)

    print("=" * 72)
    print(f" Modified-reward oracle recomputation  ({len(all_articles)} articles, {n_total} sections)")
    print("=" * 72)

    # Coefficient echo
    cfg = all_articles[0]["prior_config"]
    print(f"  Config: lambda={cfg['lambda']}  a_w={cfg['a_w']}  a_p={cfg['a_p']}  a_d={cfg['a_d']}")
    print(f"          mu_base={cfg['mu_base']}")

    # 1. Section oracle distribution: old vs new
    print(f"\n  Section oracle class distribution (old -> new):")
    old_counts = Counter(s["section_oracle"]     for s in flat)
    new_counts = Counter(s["section_oracle_new"] for s in flat)
    print(f"    {'preset':<25} {'old':>5} {'old%':>6}   {'new':>5} {'new%':>6}   {'diff':>6}")
    for p in range(NUM_PRESETS):
        o, nw = old_counts.get(p, 0), new_counts.get(p, 0)
        print(f"    P{p} {PRESET_NAMES[p]:<22} {o:>5} {o/n_total*100:>5.1f}%   "
              f"{nw:>5} {nw/n_total*100:>5.1f}%   {nw-o:>+6}")

    # 2. How many oracles changed?
    changed = [s for s in flat if s["oracle_changed"]]
    print(f"\n  Section oracles changed: {len(changed)}/{n_total} ({len(changed)/n_total*100:.1f}%)")

    # 3. Per-variant change rate
    print(f"\n  Per-variant change rate:")
    per_v = defaultdict(lambda: [0, 0])
    for art in all_articles:
        v = art["variant_level"]
        for s in art["sections"]:
            per_v[v][1] += 1
            if s["oracle_changed"]:
                per_v[v][0] += 1
    for v in ("minimal", "standard", "demanding"):
        c, t = per_v[v]
        print(f"    {v:10s}: {c}/{t} ({c/t*100:.1f}%)")

    # 4. Direction of changes
    print(f"\n  Change matrix  (old oracle -> new oracle, count):")
    print(f"    {'old\\new':>9}  " + "  ".join(f"P{p:>2}" for p in range(NUM_PRESETS)))
    for old_p in range(NUM_PRESETS):
        row_secs = [s for s in changed if s["section_oracle"] == old_p]
        new_dist = Counter(s["section_oracle_new"] for s in row_secs)
        print(f"    P{old_p:>8}  " + "  ".join(
            f"{new_dist.get(p, 0):>3}" if new_dist.get(p, 0) else "  ." for p in range(NUM_PRESETS)
        ))

    # 5. Margin / near-tie improvement
    print(f"\n  Near-tie prevalence  (>=2 presets within tol of oracle):")
    print(f"    {'tol':>6}  {'old':>6}  {'new':>6}")
    for tol in (0.01, 0.03, 0.05, 0.10):
        old_t = near_tie_count(flat, "rewards_by_preset",          "section_oracle",     tol)
        new_t = near_tie_count(flat, "rewards_by_preset_modified", "section_oracle_new", tol)
        print(f"    {tol:>6.2f}  {old_t:>6}  {new_t:>6}  ({(new_t-old_t):+d})")

    print(f"\n  Section-margin distribution:")
    old_marg = [s["section_margin"]     for s in flat]
    new_marg = [s["section_margin_new"] for s in flat]
    print(f"    {'metric':>9}  {'mean':>7}  {'median':>7}  {'p25':>7}  {'p75':>7}")
    for label, m in (("old", old_marg), ("new", new_marg)):
        srt = sorted(m)
        print(f"    {label:>9}  {statistics.mean(m):>7.4f}  {statistics.median(m):>7.4f}  "
              f"{srt[len(srt)//4]:>7.4f}  {srt[3*len(srt)//4]:>7.4f}")

    # 6. mu(s) distribution (sanity)
    print(f"\n  mu(s) distribution per variant:")
    print(f"    {'variant':10s}  {'mean':>6}  {'median':>7}  {'min':>5}  {'max':>5}")
    for v in ("minimal", "standard", "demanding"):
        mus = [s["mu"] for art in all_articles if art["variant_level"] == v for s in art["sections"]]
        print(f"    {v:10s}  {statistics.mean(mus):>6.3f}  {statistics.median(mus):>7.3f}  "
              f"{min(mus):>5.2f}  {max(mus):>5.2f}")

    # 7. Article-level oracle changes
    art_changed = sum(1 for art in all_articles if art["oracle_preset"] != art["oracle_preset_new"])
    print(f"\n  Article-level oracle changes: {art_changed}/{len(all_articles)}")
    for art in all_articles:
        if art["oracle_preset"] != art["oracle_preset_new"]:
            print(f"    {art['article']:40s}  P{art['oracle_preset']} -> P{art['oracle_preset_new']}  "
                  f"(margin {art['margin']:.4f} -> {art['margin_new']:.4f})")

    # 8. Sample of biggest oracle shifts (for human review prep)
    print(f"\n  Sections with biggest reward shift toward a different preset (top 12):")
    big = []
    for art in all_articles:
        for s in art["sections"]:
            if not s["oracle_changed"]:
                continue
            old_r = s["rewards_by_preset"][s["section_oracle"]]
            new_r = s["rewards_by_preset_modified"][s["section_oracle_new"]]
            big.append((art["article"], s, abs(new_r - old_r) + s["section_margin_new"]))
    big.sort(key=lambda x: -x[2])
    print(f"    {'article':<35} {'section':<35}  {'old':>3}->{'new':<3} mu  margin_new")
    for art_name, s, _ in big[:12]:
        title = s["title"][:33]
        print(f"    {art_name[:34]:<34}  {title:<35}  P{s['section_oracle']}->P{s['section_oracle_new']:<3}  "
              f"{s['mu']:.2f}  {s['section_margin_new']:.4f}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--lambda", dest="lam", type=float, default=0.05, help="Prior strength (default 0.05).")
    ap.add_argument("--a_w", type=float, default=0.4, help="Weight-importance coefficient (default 0.4).")
    ap.add_argument("--a_p", type=float, default=1.0, help="Position coefficient (default 1.0).")
    ap.add_argument("--a_d", type=float, default=1.0, help="Density coefficient (default 1.0).")
    ap.add_argument("--write", action="store_true", help="Write article_oracle_prior.json next to each oracle file.")
    args = ap.parse_args()

    art_dirs = sorted([d for d in _BASES_DIR.iterdir() if d.is_dir() and "__var_" in d.name])
    all_articles = []
    for d in art_dirs:
        f = d / "article_oracle.json"
        if not f.exists():
            continue
        old = json.loads(f.read_text(encoding="utf-8"))
        new = recompute_article(old, args.a_w, args.a_p, args.a_d, args.lam)
        all_articles.append(new)
        if args.write:
            (d / "article_oracle_prior.json").write_text(
                json.dumps(new, indent=2), encoding="utf-8"
            )

    analyse(all_articles)
    if args.write:
        print(f"\n  Wrote article_oracle_prior.json for {len(all_articles)} articles.")


if __name__ == "__main__":
    main()
