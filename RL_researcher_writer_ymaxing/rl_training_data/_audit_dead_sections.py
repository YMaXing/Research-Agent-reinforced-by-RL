"""
Audit dead and near-tied sections in the 4B preset scenario {P0,P1,P3,P5}.

For each (article, variant, section), classify into:
  DEAD    : regret = max(R)-mean(R) < DEAD_EPS                (≈0)
  TIGHT   : DEAD_EPS <= regret < TIGHT_EPS                    (small but nonzero)
  LIVE    : regret >= TIGHT_EPS                               (clear signal)

For DEAD + TIGHT sections, diagnose WHY the signal is weak by measuring:

  (1) Quality-score identity:  are the per-dim 0/1 vectors identical across
      all 4 presets? If yes, only cost penalty differentiates rewards.
      Sub-classify by score profile:
        - ALL_PASS (1111111)  : section fully satisfied by every preset
        - ALL_FAIL (0000000)  : section failed by every preset
        - PARTIAL  (mixed)    : same partial pattern across presets

  (2) Research-artifact divergence: do the presets actually behave differently?
      Compute Jaccard distance on scraped URL domains (proxy for whether the
      presets explored different territory). Low divergence → presets converged
      on similar research → tie is HONEST (intrinsic equivalence).
      High divergence → presets explored very differently but grader gave same
      score → suggests GRADER BLINDNESS.

  (3) Section structural features:
      - position (index within article)
      - title keywords (definitional vs analytical vs synthesis)
      - reasoning text length (proxy for how much the grader "had to say")

Output: classification table per section + aggregate statistics.

Usage:
  python3 _audit_dead_sections.py
  python3 _audit_dead_sections.py --output dead_audit.txt
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, stdev
from urllib.parse import urlparse

# Reuse parsing helpers from sibling analysis script
sys.path.insert(0, str(Path(__file__).parent))
from _analyze_oracle_margins import (  # type: ignore
    ALL_DIMS, REWARD_DIMS, REWARD_DIM_ORDER,
    PRESET_ROUNDS, ARTICLES, VARIANTS,
    compute_reward, load_episode,
    _extract_reasoning_tolerant,
    parse_section_scores,
)

EPISODES_ROOT = Path(__file__).parent / "episodes"

# 4B scenario
SCEN = [0, 1, 3, 5]
N = len(SCEN)

# Classification thresholds — applied to QUALITY-ONLY regret
# (cost penalty alone always creates regret = cost_rate * spread, which is
#  a constant per-variant signal that the policy cannot exploit at section
#  level; only quality variation is genuinely learnable per section.)
DEAD_EPS = 1e-6
TIGHT_EPS_BY_VAR = {
    "var_minimal":   0.030,
    "var_standard":  0.030,
    "var_demanding": 0.020,
}

# Definitional / synthesis keyword lexicons for section-title heuristic
DEFINITIONAL = {"introduction", "intro", "overview", "definition", "background",
                "what", "summary", "conclusion", "recap", "preface"}
SYNTHESIS    = {"comparison", "vs", "versus", "trade", "tradeoff", "design",
                "architecture", "pattern", "approach", "strategy", "choosing",
                "evaluation", "discussion"}
PROCEDURAL   = {"how", "steps", "implementation", "build", "create",
                "tutorial", "example", "walkthrough", "setup", "configure"}


# ──────────────────────────────────────────────────────────────────────────
# Research artifact loading
# ──────────────────────────────────────────────────────────────────────────
def load_url_domains(ep_dir: Path) -> set[str]:
    """Return the set of domains scraped during this episode."""
    p = ep_dir / ".research" / "url_phases.json"
    if not p.exists():
        return set()
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return set()
    domains = set()
    for url in data.keys():
        try:
            d = urlparse(url).netloc.lower()
            if d.startswith("www."):
                d = d[4:]
            if d:
                domains.add(d)
        except Exception:
            pass
    return domains


def load_query_count(ep_dir: Path) -> tuple[int, int]:
    """Return (n_exploit_queries, n_explore_queries)."""
    p = ep_dir / ".research" / "full_queries.md"
    if not p.exists():
        return (0, 0)
    try:
        text = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return (0, 0)
    n_exploit = len(re.findall(r"\[Exploitation\]", text, re.IGNORECASE))
    n_explore = len(re.findall(r"\[Exploration\]", text, re.IGNORECASE))
    return (n_exploit, n_explore)


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    u = a | b
    if not u:
        return 0.0
    return len(a & b) / len(u)


def avg_pairwise_jaccard(sets: list[set]) -> float:
    """Mean Jaccard SIMILARITY across all distinct pairs."""
    pairs = [(i, j) for i in range(len(sets)) for j in range(i+1, len(sets))]
    if not pairs:
        return 1.0
    return mean(jaccard(sets[i], sets[j]) for i, j in pairs)


# ──────────────────────────────────────────────────────────────────────────
# Section classification
# ──────────────────────────────────────────────────────────────────────────
def title_category(title: str) -> str:
    t = title.lower()
    tokens = set(re.findall(r"[a-z]+", t))
    if tokens & DEFINITIONAL:
        return "definitional"
    if tokens & SYNTHESIS:
        return "synthesis"
    if tokens & PROCEDURAL:
        return "procedural"
    return "other"


def score_profile(profile_per_preset: list[dict[str, int]]) -> str:
    """Compact label for the per-dim score vector if identical across presets."""
    # All 4 vectors identical?
    vecs = [tuple(p.get(d, 0) for d in REWARD_DIM_ORDER) for p in profile_per_preset]
    if len(set(vecs)) != 1:
        return "MIXED"
    v = vecs[0]
    if all(x == 1 for x in v):
        return "ALL_PASS"
    if all(x == 0 for x in v):
        return "ALL_FAIL"
    return "PARTIAL_" + "".join(str(x) for x in v)


def build_section_table(article: str, variant: str) -> list[dict]:
    """For each section, gather scores, rewards, and research artifacts."""
    # Load per-preset reasoning (per-dim per-section 0/1)
    preset_dim_sec: dict[int, dict[str, dict[str, int]]] = {}
    preset_domains: dict[int, set] = {}
    preset_queries: dict[int, tuple[int, int]] = {}
    for p in SCEN:
        ep = EPISODES_ROOT / f"{article}__{variant}__preset{p}"
        r = load_episode(ep)
        if r is None:
            return []
        preset_dim_sec[p] = r
        preset_domains[p] = load_url_domains(ep)
        preset_queries[p] = load_query_count(ep)

    # Section set = union of sections seen in cc dim
    sec_set = set()
    for p in SCEN:
        sec_set.update(preset_dim_sec[p].get("cc", {}).keys())

    rows = []
    for idx, sec in enumerate(sorted(sec_set)):
        # Per-preset reward-dim scores for THIS section
        per_preset_scores = []
        for p in SCEN:
            s = {d: preset_dim_sec[p].get(d, {}).get(sec, 0) for d in REWARD_DIM_ORDER}
            per_preset_scores.append(s)
        rewards = [compute_reward(per_preset_scores[i], SCEN[i], variant)
                   for i in range(N)]
        # Quality-only rewards: same formula but with nr=0 forced.
        # Equivalent to stripping the cost penalty so we measure what the
        # GRADER actually distinguished, not what cost added.
        q_rewards = []
        for i in range(N):
            s = per_preset_scores[i]
            if variant == "minimal":
                q = (0.05*s["cc"] + 0.05*s["fl"]
                     + s["cp"]*(0.60*s["de"] + 0.40*s["be"])*0.10
                     + 0.70*s["ga"] + 0.10*s["ra"])
            elif variant == "demanding":
                q = (0.12*s["cc"] + 0.08*s["fl"]
                     + s["cp"]*(0.55*s["de"] + 0.35*s["be"])*0.50
                     + (0.60*s["ga"] + 0.40*s["ra"])*0.25)
            else:
                q = (0.20*s["cc"] + 0.20*s["fl"]
                     + s["cp"]*(0.60*s["de"] + 0.40*s["be"])*0.30
                     + (0.50*s["ga"] + 0.50*s["ra"])*0.30)
            q_rewards.append(q)

        oracle_idx = max(range(N), key=lambda i: rewards[i])
        oracle_preset = SCEN[oracle_idx]
        mean_r = mean(rewards)
        regret = max(rewards) - mean_r                       # full-reward regret
        q_regret = max(q_rewards) - mean(q_rewards)          # quality-only regret
        gap2   = sorted(rewards, reverse=True)[0] - sorted(rewards, reverse=True)[1]

        # Classify by QUALITY-only regret (what the grader actually saw)
        if q_regret < DEAD_EPS:
            klass = "DEAD"
        elif q_regret < TIGHT_EPS_BY_VAR[variant]:
            klass = "TIGHT"
        else:
            klass = "LIVE"

        rows.append({
            "article":   article,
            "variant":   variant,
            "sec_idx":   idx,
            "sec_title": sec,
            "title_cat": title_category(sec),
            "class":     klass,
            "regret":    regret,
            "q_regret":  q_regret,
            "gap2":      gap2,
            "oracle":    oracle_preset,
            "rewards":   rewards,
            "scores":    per_preset_scores,
            "profile":   score_profile(per_preset_scores),
            "url_jacc":  avg_pairwise_jaccard([preset_domains[p] for p in SCEN]),
            "url_sizes": [len(preset_domains[p]) for p in SCEN],
            "queries":   [preset_queries[p] for p in SCEN],
        })
    return rows


# ──────────────────────────────────────────────────────────────────────────
# Reporting
# ──────────────────────────────────────────────────────────────────────────
SEP  = "=" * 96
SEP2 = "-" * 96


def diag_reason(row: dict) -> str:
    """Heuristic explanation for why this section is DEAD/TIGHT."""
    if row["class"] == "LIVE":
        return "—"
    prof = row["profile"]
    jacc = row["url_jacc"]

    if prof == "ALL_PASS":
        base = "trivial (all presets fully passed)"
    elif prof == "ALL_FAIL":
        base = "hard-floor (all presets fully failed)"
    elif prof.startswith("PARTIAL_"):
        base = f"shared-partial-profile {prof[8:]}"
    else:
        base = "score-mixed (cost-only differentiates)"

    if prof != "MIXED":
        # Same quality scores — was research actually different?
        if jacc >= 0.6:
            sig = "research converged (intrinsic tie)"
        elif jacc <= 0.2:
            sig = "research DIVERGED (grader blindness)"
        else:
            sig = "research mod-different"
        return f"{base}; {sig} (URL-Jaccard={jacc:.2f})"
    else:
        return f"{base}; URL-Jaccard={jacc:.2f}"


def render(rows: list[dict], out) -> None:
    def w(s=""):
        out.write(s + "\n")

    # Aggregate counts
    by_class = Counter(r["class"] for r in rows)
    n = len(rows)
    w(SEP)
    w("DEAD SECTION AUDIT — 4B scenario {P0, P1, P3, P5}")
    w(SEP)
    w(f"Total sections graded: {n}")
    for k in ("LIVE", "TIGHT", "DEAD"):
        c = by_class[k]
        pct = 100*c/n if n else 0
        w(f"  {k:5s}: {c:4d} ({pct:5.1f}%)")
    w("")

    # Class × variant
    w(SEP2)
    w("By variant:")
    w(f"  {'variant':<14} {'LIVE':>8} {'TIGHT':>8} {'DEAD':>8} {'total':>8}")
    for v in VARIANTS:
        sub = [r for r in rows if r["variant"] == v]
        cnt = Counter(r["class"] for r in sub)
        t = len(sub)
        w(f"  {v:<14} "
          f"{cnt['LIVE']:4d} ({100*cnt['LIVE']/t:4.1f}%) "
          f"{cnt['TIGHT']:4d} ({100*cnt['TIGHT']/t:4.1f}%) "
          f"{cnt['DEAD']:4d} ({100*cnt['DEAD']/t:4.1f}%) "
          f"{t:4d}")
    w("")

    # Dead/tight diagnosis breakdown
    weak = [r for r in rows if r["class"] in ("DEAD", "TIGHT")]
    w(SEP2)
    w(f"Dead+Tight diagnosis ({len(weak)} sections)")
    w(SEP2)
    prof_counts = Counter(r["profile"] for r in weak)
    w("  Score profile (all 4 presets):")
    for pf, c in prof_counts.most_common():
        w(f"    {pf:<24} {c:4d} ({100*c/len(weak):5.1f}%)")
    w("")

    # Among same-vector profiles, did research diverge?
    same_vec = [r for r in weak if r["profile"] != "MIXED"]
    if same_vec:
        bins = {"converged (J>=0.6)": 0, "moderate (0.2<J<0.6)": 0, "DIVERGED (J<=0.2)": 0}
        for r in same_vec:
            j = r["url_jacc"]
            if j >= 0.6: bins["converged (J>=0.6)"] += 1
            elif j <= 0.2: bins["DIVERGED (J<=0.2)"] += 1
            else: bins["moderate (0.2<J<0.6)"] += 1
        w("  Research-artifact divergence among same-score sections:")
        for k, c in bins.items():
            pct = 100*c/len(same_vec)
            w(f"    {k:<28} {c:4d} ({pct:5.1f}%)")
        w("")
        w("  Interpretation:")
        w("    converged    -> presets agreed on what to research; tie is HONEST (intrinsic).")
        w("    DIVERGED     -> presets explored differently but grader gave same scores;")
        w("                    suggests GRADER BLINDNESS (worth a closer look).")
        w("")

    # Title-category breakdown
    w(SEP2)
    w("Section title-category vs class:")
    w(f"  {'category':<14} {'LIVE':>8} {'TIGHT':>8} {'DEAD':>8} {'%dead':>8}")
    for cat in ("definitional", "synthesis", "procedural", "other"):
        sub = [r for r in rows if r["title_cat"] == cat]
        if not sub: continue
        cnt = Counter(r["class"] for r in sub)
        pct_dead = 100*cnt["DEAD"]/len(sub)
        w(f"  {cat:<14} "
          f"{cnt['LIVE']:4d}      "
          f"{cnt['TIGHT']:4d}      "
          f"{cnt['DEAD']:4d}      "
          f"{pct_dead:5.1f}%")
    w("")

    # Section-position effect (within article)
    w(SEP2)
    w("Section position vs class (position = index in article):")
    by_pos = defaultdict(list)
    for r in rows:
        by_pos[r["sec_idx"]].append(r["class"])
    w(f"  {'position':<10} {'n':>5} {'%LIVE':>8} {'%TIGHT':>8} {'%DEAD':>8}")
    for pos in sorted(by_pos):
        cs = by_pos[pos]
        cnt = Counter(cs)
        t = len(cs)
        w(f"  {pos:<10} {t:5d} "
          f"{100*cnt['LIVE']/t:7.1f}% "
          f"{100*cnt['TIGHT']/t:7.1f}% "
          f"{100*cnt['DEAD']/t:7.1f}%")
    w("")

    # Highest-suspicion dead sections: same scores but high URL divergence
    suspicious = [r for r in weak
                  if r["profile"] != "MIXED" and r["url_jacc"] <= 0.2]
    if suspicious:
        w(SEP2)
        w(f"SUSPICIOUS DEAD SECTIONS (grader-blindness candidates): "
          f"{len(suspicious)}")
        w(SEP2)
        w("Same per-dim scores across all 4 presets, but presets scraped")
        w("very different domain sets (Jaccard <= 0.20). Listed below for review.")
        w("")
        for r in sorted(suspicious, key=lambda x: x["url_jacc"]):
            w(f"  [{r['variant'][:3]}] {r['article']}/sec{r['sec_idx']}: "
              f"{r['sec_title'][:55]}")
            w(f"      profile={r['profile']}  J={r['url_jacc']:.2f}  "
              f"domains/preset={r['url_sizes']}  regret={r['regret']:.4f}")
        w("")

    # Per-article dead summary
    w(SEP2)
    w("Per-article dead-section counts (pooled across variants):")
    art_counts = defaultdict(lambda: {"LIVE": 0, "TIGHT": 0, "DEAD": 0})
    for r in rows:
        art_counts[r["article"]][r["class"]] += 1
    w(f"  {'article':<32} {'LIVE':>8} {'TIGHT':>8} {'DEAD':>8} {'%dead':>8}")
    for a in ARTICLES:
        c = art_counts[a]
        t = sum(c.values())
        if t == 0: continue
        pct = 100*c["DEAD"]/t
        w(f"  {a:<32} {c['LIVE']:4d}     {c['TIGHT']:4d}     {c['DEAD']:4d}     {pct:5.1f}%")
    w("")

    # Per-section detail table (truncated)
    w(SEP2)
    w("Per-section detail (first 50 DEAD + 25 TIGHT shown)")
    w(SEP2)
    w(f"  {'cls':<5} {'var':<4} {'art':<24} {'sec':<40} {'regret':>8} {'profile':<20} {'J':>5} {'why':<60}")
    dead_rows  = [r for r in rows if r["class"] == "DEAD"][:50]
    tight_rows = [r for r in rows if r["class"] == "TIGHT"][:25]
    for r in dead_rows + tight_rows:
        w(f"  {r['class']:<5} {r['variant'][4:7]:<4} "
          f"{r['article'][:22]:<24} {r['sec_title'][:38]:<40} "
          f"{r['regret']:7.4f}  {r['profile'][:18]:<20} "
          f"{r['url_jacc']:5.2f} {diag_reason(r)[:58]}")
    w("")
    w(SEP)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=str, default=None,
                    help="Write report to file in addition to stdout.")
    args = ap.parse_args()

    rows = []
    for article in ARTICLES:
        for variant in VARIANTS:
            rows.extend(build_section_table(article, variant))

    render(rows, sys.stdout)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            render(rows, f)
        print(f"\n[wrote report to {args.output}]")


if __name__ == "__main__":
    main()
