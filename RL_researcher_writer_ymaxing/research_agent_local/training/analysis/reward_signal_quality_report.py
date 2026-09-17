"""Detailed reward-signal-quality report, section- and article-level, now that
all 24 TRAIN articles have N=3 draws (1 production + 2 real temperature=0.7
replicates -- see run13_rl_grok_pipeline_analysis.md Appendix A.11-A.13).

Read-only, zero LLM calls. Reads ONLY the two already-on-disk section-reward
sources per article -- ``section_oracle.json`` (single production draw) and
``section_oracle_averaged.json`` (merge_replicate_oracles.py's N=3 average) --
so single-draw and averaged numbers are computed via the exact same stat
function from the exact same reward values production/training would see; no
raw episode/reasoning.json recompute needed for this report (that path is what
model_gate_candidates.py / measure_replicate_noise.py already own, and is only
used here for the noise-floor step and the corpus-context sanity check).

The per-section stats (spread, std, margin, regret, normalized advantage,
near-tie) mirror train_grpo.py's OWN flat-drop / sigma_floor / near_tie_margin
logic exactly (SIGMA_FLOOR=0.04, NEAR_TIE_MARGIN=0.06, both train_grpo.py CLI
defaults) -- these are literally the numbers that determine what GRPO drops,
clamps, and accepts as a near-tie, not an independent metric invented for this
report.

Sections of the report:
  A. Noise floor (delegates to estimate_noise_floor.run()).
  B. Section-level GRPO-relevant signal quality: flat-drop rate, floored rate,
     near-tie rate, margin distribution, normalized advantage, arm balance --
     single-draw vs. averaged(N=3), across all 171 TRAIN sections.
  C. Defensible-section share (single-draw vs. averaged; corpus-wide context).
  D. Article-level: production vs. averaged oracle_arm/margin/risk-tier,
     confirmed/flipped/hard-ruled breakdown, confidence-erosion cases.
  E. Per-lesson and per-variant breakdown of the Step B section-level metrics.

Usage (from research_agent_local/training/):
  python3 reward_signal_quality_report.py
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import audit_oracle_margins as aom  # noqa: E402
import compute_article_oracle as cao  # noqa: E402
import estimate_noise_floor as enf  # noqa: E402
import generate_episode_oracles as geo  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402
import model_gate_candidates as mgc  # noqa: E402

ARM_ORDER = geo._ARM_ORDER  # ["skip", "light", "standard", "deep"]
SIGMA_FLOOR = 0.04       # train_grpo.py --sigma-floor default
NEAR_TIE_MARGIN = 0.06   # train_grpo.py --near-tie-margin default

_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_DEFAULT_ARTICLES = [f"{lesson}__{variant}" for lesson in _LESSONS for variant in _VARIANTS]
_DEFAULT_REPLICATES = 2

_OLD_DIFF_SD_1X = 0.140  # temp=0.25-confounded, for context only (A.7.1)
_OLD_DIFF_SD_2X = 0.280


def _section_stats(rewards: dict[str, float]) -> dict:
    """Mirrors train_grpo.py's load_section_groups()/model_gate_candidates.evaluate()
    exactly: spread/std/margin/regret/normalized-advantage/near-tie, same constants."""
    rs = [rewards[a] for a in ARM_ORDER]
    mx, mn = max(rs), min(rs)
    mean_r = sum(rs) / 4
    std = (sum((r - mean_r) ** 2 for r in rs) / 4) ** 0.5
    srt = sorted(rs, reverse=True)
    return {
        "spread": mx - mn,
        "std": std,
        "margin": srt[0] - srt[1],
        "regret": mx - mean_r,
        "adv": (mx - mean_r) / max(std, SIGMA_FLOOR),
        "near_tie": sum(1 for r in rs if r >= mx - NEAR_TIE_MARGIN) > 1,
        "hit_sigma_floor": std < SIGMA_FLOOR,
        "flat_drop": (mx - mn) < SIGMA_FLOOR,
        "arm": max(ARM_ORDER, key=lambda a: rewards[a]),
    }


def _load_sections(art: str, averaged: bool) -> dict[str, dict] | None:
    name = "section_oracle_averaged.json" if averaged else "section_oracle.json"
    p = mrn._BASES_DIR / art / name
    if not p.exists():
        return None
    return json.loads(p.read_text(encoding="utf-8"))["sections"]


def _aggregate(stats_list: list[dict]) -> dict:
    n = len(stats_list)
    if n == 0:
        return {}
    kept = [s for s in stats_list if not s["flat_drop"]]
    margins = [s["margin"] for s in stats_list]
    advs = [s["adv"] for s in kept]
    dist: dict[str, int] = {a: 0 for a in ARM_ORDER}
    for s in stats_list:
        dist[s["arm"]] += 1
    return {
        "n": n,
        "n_kept": len(kept),
        "flat_drop_frac": 1 - len(kept) / n,
        "floored_frac": (sum(1 for s in kept if s["hit_sigma_floor"]) / len(kept)) if kept else 0.0,
        "near_tie_frac": sum(1 for s in stats_list if s["near_tie"]) / n,
        "mean_margin": statistics.mean(margins),
        "median_margin": statistics.median(margins),
        "mean_adv": statistics.mean(advs) if advs else 0.0,
        "arm_dist": dist,
    }


def _print_aggregate_row(label: str, agg: dict) -> None:
    dist_str = "/".join(f"{a[:2]}{agg['arm_dist'][a]}" for a in ARM_ORDER)
    print(f"  {label:<22} n={agg['n']:>4}  flat-drop={agg['flat_drop_frac']:>6.1%}  "
          f"floored(kept)={agg['floored_frac']:>6.1%}  near-tie={agg['near_tie_frac']:>6.1%}  "
          f"mean-margin={agg['mean_margin']:.4f}  median-margin={agg['median_margin']:.4f}  "
          f"mean-normAdv={agg['mean_adv']:.3f}  dist=[{dist_str}]")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES)
    args = parser.parse_args()
    articles = args.articles
    replicates = list(range(1, args.replicates + 1))
    n_draws = 1 + len(replicates)

    print("#" * 100)
    print(f"REWARD-SIGNAL-QUALITY REPORT -- {len(articles)} TRAIN article-variant(s), "
          f"N={n_draws} draws each (1 production + {len(replicates)} replicate(s))")
    print(f"Generated {datetime.now(timezone.utc).isoformat()}")
    print("#" * 100)

    # ---------------------------------------------------------------- STEP A
    print()
    print("=" * 100)
    print("STEP A: noise floor (per-cell reward sd across independent replicates)")
    print("=" * 100)
    noise_stats = enf.run(articles, replicates)
    diff_1x = noise_stats["diff_sd_1x"]
    diff_2x = noise_stats["diff_sd_2x"]
    shrink = n_draws ** 0.5
    avg_1x, avg_2x = diff_1x / shrink, diff_2x / shrink

    # ---------------------------------------------------------------- STEP B
    print()
    print("=" * 100)
    print("STEP B: section-level GRPO signal quality -- single-draw vs. averaged(N={}), "
          "all TRAIN sections".format(n_draws))
    print("=" * 100)
    print(f"(SIGMA_FLOOR={SIGMA_FLOOR}, NEAR_TIE_MARGIN={NEAR_TIE_MARGIN} -- train_grpo.py's own defaults)")
    print()

    single_stats: list[dict] = []
    avg_stats: list[dict] = []
    per_article_single: dict[str, list[dict]] = {}
    per_article_avg: dict[str, list[dict]] = {}

    for art in articles:
        single_secs = _load_sections(art, averaged=False)
        avg_secs = _load_sections(art, averaged=True)
        if single_secs is None:
            print(f"  MISSING section_oracle.json for {art}, skipped", file=sys.stderr)
            continue
        s_list = [_section_stats(info["rewards"]) for info in single_secs.values()]
        per_article_single[art] = s_list
        single_stats.extend(s_list)
        if avg_secs is not None:
            a_list = [_section_stats(info["rewards"]) for info in avg_secs.values()]
            per_article_avg[art] = a_list
            avg_stats.extend(a_list)

    agg_single = _aggregate(single_stats)
    agg_avg = _aggregate(avg_stats)
    _print_aggregate_row("single-draw", agg_single)
    _print_aggregate_row(f"averaged(N={n_draws})", agg_avg)

    print()
    print("Section-level raw oracle-argmax flip rate (single-draw arm vs. averaged arm, same section):")
    n_sec = n_flip = 0
    for art in per_article_avg:
        single_secs = _load_sections(art, averaged=False)
        avg_secs = _load_sections(art, averaged=True)
        for sid in avg_secs:
            n_sec += 1
            if single_secs[sid]["oracle"] != avg_secs[sid]["oracle"]:
                n_flip += 1
    if n_sec:
        print(f"  {n_flip}/{n_sec} ({n_flip/n_sec:.1%}) sections change their argmax arm under averaging")

    # ---------------------------------------------------------------- STEP C
    print()
    print("=" * 100)
    print("STEP C: defensible-section share (margin vs. noise-sd threshold)")
    print("=" * 100)
    print(f"thresholds: single-draw 1x={diff_1x:.4f} 2x={diff_2x:.4f}  |  "
          f"averaged(N={n_draws}, sqrt({n_draws})-shrunk) 1x={avg_1x:.4f} 2x={avg_2x:.4f}")
    s1 = sum(1 for s in single_stats if s["margin"] > diff_1x)
    s2 = sum(1 for s in single_stats if s["margin"] > diff_2x)
    a1 = sum(1 for s in avg_stats if s["margin"] > avg_1x)
    a2 = sum(1 for s in avg_stats if s["margin"] > avg_2x)
    n = len(single_stats)
    print(f"  margin > 1x noise-sd: single-draw {s1}/{n} ({s1/n:.1%})  ->  averaged {a1}/{n} ({a1/n:.1%})")
    print(f"  margin > 2x noise-sd: single-draw {s2}/{n} ({s2/n:.1%})  ->  averaged {a2}/{n} ({a2/n:.1%})")

    corpus = mgc.load_corpus()
    sec_stats_corpus, _ = mgc.evaluate(corpus, mgc.CANDIDATES["C2_soft_ga_pen010"])
    n_all = len(sec_stats_corpus)
    old_1x = sum(1 for s in sec_stats_corpus if s["margin"] > _OLD_DIFF_SD_1X)
    new_1x = sum(1 for s in sec_stats_corpus if s["margin"] > diff_1x)
    print(f"  (corpus context, all {n_all} production sections, single-draw only: "
          f"OLD-noise-floor 1x share={old_1x}/{n_all} ({old_1x/n_all:.1%})  "
          f"NEW-noise-floor 1x share={new_1x}/{n_all} ({new_1x/n_all:.1%}))")

    # ---------------------------------------------------------------- STEP D
    print()
    print("=" * 100)
    print("STEP D: article-level production (single-draw) vs. averaged oracle_arm/margin")
    print("=" * 100)
    margin_rows = {r["name"]: r for r in aom.scan(aom._DEFAULT_BASES_DIR, aom._DEFAULT_HIGH, aom._DEFAULT_MODERATE)}

    tier_order = ["CRITICAL", "HIGH", "MODERATE", "COMFORTABLE"]
    tier_counts = {t: {"confirmed": 0, "flipped": 0} for t in tier_order}
    n_confirmed = n_flipped = n_hard_ruled = 0
    erosion_rows = []
    d_header = (f"{'article':<42} {'tier':<15} | {'production':>9} {'margin':>8} | "
                f"{'averaged':>9} {'margin':>8} | {'votes'}")
    print(d_header)
    print("-" * len(d_header))
    for art in articles:
        avg_secs = _load_sections(art, averaged=True)
        feat_path = mrn._BASES_DIR / art / "guideline_features.json"
        if avg_secs is None:
            continue
        feats = json.loads(feat_path.read_text(encoding="utf-8")).get("sections", {}) if feat_path.exists() else {}
        r_w, *_ = cao._compute_r_w(avg_secs, feats)
        ranked = sorted(r_w, key=r_w.get, reverse=True)
        avg_margin = r_w[ranked[0]] - r_w[ranked[1]]

        row = margin_rows.get(art, {})
        tier = row.get("risk_tier", "?")
        prod_arm = row.get("oracle_arm", "?")
        prod_margin = row.get("margin", float("nan"))

        sec_ids = list(avg_secs.keys())
        orig_oracle = json.loads((mrn._BASES_DIR / art / "section_oracle.json").read_text(encoding="utf-8"))
        orig_r_w, *_ = cao._compute_r_w(orig_oracle["sections"], feats)
        votes = [max(orig_r_w, key=orig_r_w.get)]
        for r in replicates:
            prefix = mrn._NOISE_EXPERIMENT_DIR / f"{art}__replicate{r}"
            if not any((mrn._NOISE_EXPERIMENT_DIR / f"{art}__replicate{r}__preset{p}" / "reasoning.json").exists()
                       for p in mrn._ARM_PRESETS_FLAT):
                continue
            rep_sections = mrn._compute_replicate_sections(art, prefix, sec_ids)
            rep_r_w, *_ = cao._compute_r_w(rep_sections, feats)
            votes.append(max(rep_r_w, key=rep_r_w.get))
        vote_str = ",".join(votes)

        if tier in ("POLICY-FORCED", "MANUAL-OVERRIDE"):
            n_hard_ruled += 1
            flag = "(hard-ruled)"
        elif ranked[0] == prod_arm:
            n_confirmed += 1
            flag = "CONFIRMED"
            if tier in tier_counts:
                tier_counts[tier]["confirmed"] += 1
        else:
            n_flipped += 1
            flag = "**FLIPPED**"
            if tier in tier_counts:
                tier_counts[tier]["flipped"] += 1

        if flag != "(hard-ruled)" and not (prod_margin != prod_margin):  # NaN-safe
            if abs(avg_margin) < 0.5 * abs(prod_margin) and abs(prod_margin) >= 0.06:
                erosion_rows.append((art, prod_margin, avg_margin))

        print(f"{art:<42} {tier:<15} | {str(prod_arm):>9} {prod_margin:>8.4f} | "
              f"{ranked[0]:>9} {avg_margin:>8.4f} | {vote_str:<18} {flag}")

    print("-" * len(d_header))
    print(f"{n_confirmed} confirmed, {n_flipped} flipped, {n_hard_ruled} hard-ruled "
          f"(policy-forced/manual-override, immune to this comparison) out of {len(articles)}")
    print()
    print("Flip-rate by risk tier (of reward-decided articles only):")
    for t in tier_order:
        c, f = tier_counts[t]["confirmed"], tier_counts[t]["flipped"]
        tot = c + f
        if tot:
            print(f"  {t:<12} {f}/{tot} flipped ({f/tot:.0%})")

    if erosion_rows:
        print()
        print("Confidence erosion (CONFIRMED same winner, but averaged margin < half the production margin,"
              " production margin was >= 0.06):")
        for art, pm, am in erosion_rows:
            print(f"  {art:<42} production={pm:+.4f}  ->  averaged={am:+.4f}")

    # ---------------------------------------------------------------- STEP E
    print()
    print("=" * 100)
    print("STEP E: per-lesson and per-variant breakdown (section-level, Step B metrics)")
    print("=" * 100)
    print()
    print("By lesson (all 3 variants pooled):")
    for lesson in _LESSONS:
        s_list = [s for art in per_article_single if art.startswith(f"{lesson}__") for s in per_article_single[art]]
        a_list = [s for art in per_article_avg if art.startswith(f"{lesson}__") for s in per_article_avg[art]]
        if not s_list:
            continue
        agg_s = _aggregate(s_list)
        agg_a = _aggregate(a_list) if a_list else None
        print(f"  {lesson}:")
        _print_aggregate_row("single-draw", agg_s)
        if agg_a:
            _print_aggregate_row(f"averaged(N={n_draws})", agg_a)

    print()
    print("By variant (all 8 lessons pooled):")
    for variant in _VARIANTS:
        s_list = [s for art in per_article_single if art.endswith(f"__{variant}") for s in per_article_single[art]]
        a_list = [s for art in per_article_avg if art.endswith(f"__{variant}") for s in per_article_avg[art]]
        if not s_list:
            continue
        agg_s = _aggregate(s_list)
        agg_a = _aggregate(a_list) if a_list else None
        print(f"  {variant}:")
        _print_aggregate_row("single-draw", agg_s)
        if agg_a:
            _print_aggregate_row(f"averaged(N={n_draws})", agg_a)


if __name__ == "__main__":
    main()
