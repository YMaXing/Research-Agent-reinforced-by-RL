"""Quantify the real improvement in defensible-section share from real
temperature=0.7 replication (analysis md A.10 step 3).

Read-only, zero LLM calls -- reuses estimate_noise_floor.py (unconfounded
noise-floor sd, measured from real temp=0.7 replicates instead of the
temp=0.25-confounded original), measure_replicate_noise.py's recompute path
(no duplicated formula), compute_article_oracle.py's article-level aggregation,
and model_gate_candidates.py's corpus loader (for the full-corpus baseline,
current production formula = C2_soft_ga_pen010).

Four comparisons, all against the SAME new unconfounded noise-floor sd:

  A. Noise floor itself (delegates straight to estimate_noise_floor.run()).
  B. SINGLE-DRAW vs AVERAGED (N=1+len(replicates)) defensible-section share,
     across every section in --articles. Mirrors A.7's own table, on real
     (not temp=0.25-confounded) data, with the averaged side's threshold
     correctly sqrt(N)-shrunk (comparing it against the unshrunk single-draw
     threshold is an apples-to-oranges mistake -- see A.11).
  C. Full corpus (all production articles, single draw only) re-scored at
     OLD vs NEW noise-sd -- answers "does the corpus-wide picture change once
     the noise floor itself is no longer built on the 0.25 confound".
  D. Article-level: production (single-draw) oracle_arm/margin vs averaged
     oracle_arm/margin for each of --articles, cross-referenced against
     audit_oracle_margins.py's risk tier and the raw per-replicate vote tally
     -- flags CONFIRMED vs FLIPPED labels.

Usage (from research_agent_local/training/):
  python3 quantify_defensible_gain_070.py                    # full 24-article TRAIN set
  python3 quantify_defensible_gain_070.py --articles 06_tools__var_standard --replicates 2
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(_THIS_DIR))

import audit_oracle_margins as aom  # noqa: E402
import compute_article_oracle as cao  # noqa: E402
import estimate_noise_floor as enf  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402
import model_gate_candidates as mgc  # noqa: E402

_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_DEFAULT_ARTICLES = [f"{lesson}__{variant}" for lesson in _LESSONS for variant in _VARIANTS]
_DEFAULT_REPLICATES = 2

# Historical (temp=0.25-confounded) noise-floor figures, for context only --
# see run13_rl_grok_pipeline_analysis.md A.7.1 / §54.7-55.3.
_OLD_DIFF_SD_1X = 0.140
_OLD_DIFF_SD_2X = 0.280


def _margin(rewards: dict[str, float]) -> float:
    srt = sorted(rewards.values(), reverse=True)
    return srt[0] - srt[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=_DEFAULT_ARTICLES)
    parser.add_argument("--replicates", type=int, default=_DEFAULT_REPLICATES)
    args = parser.parse_args()
    articles = args.articles
    replicates = list(range(1, args.replicates + 1))

    print("=" * 100)
    print(f"STEP A: unconfounded noise-floor estimate from {len(articles)} article-variant(s), "
          f"{len(replicates)} replicate(s) each")
    print("=" * 100)
    stats = enf.run(articles, replicates)
    diff_1x = stats["diff_sd_1x"]
    diff_2x = stats["diff_sd_2x"]

    # N draws (1 production + len(replicates)) feed the averaged margin, so ITS
    # noise floor is the single-draw noise floor shrunk by sqrt(N) (SEM of the
    # mean) -- NOT the same single-draw threshold. Comparing an averaged margin
    # against the single-draw threshold is apples-to-oranges and would make
    # averaging look like it *reduces* the defensible share (it doesn't -- it
    # reduces the noise on the estimate, so the bar it needs to clear shrinks
    # too). Mirrors A.7's own methodology ("Averaged(N=4) ... 0.070 (predicted
    # sqrt(4)-shrunk)").
    n_draws = 1 + len(replicates)
    shrink = n_draws ** 0.5
    avg_1x = diff_1x / shrink
    avg_2x = diff_2x / shrink

    print()
    print("=" * 100)
    print(f"STEP B: defensible-section share, SINGLE-DRAW vs AVERAGED (N={n_draws}), "
          f"{len(articles)} article-variant(s)")
    print("=" * 100)
    print(f"Using the NEW arm-difference noise thresholds: 1x={diff_1x:.4f}  2x={diff_2x:.4f}")
    print(f"(for reference, the OLD temp=0.25-confounded thresholds were: "
          f"1x={_OLD_DIFF_SD_1X:.4f}  2x={_OLD_DIFF_SD_2X:.4f})")
    print(f"Averaged-margin (N={n_draws}) thresholds, sqrt({n_draws})-shrunk: "
          f"1x={avg_1x:.4f}  2x={avg_2x:.4f}")
    print()

    header = (f"{'article':<42} {'n_sec':>5} | {'single>1x':>9} {'single>2x':>9} | "
              f"{'avg>1x':>7} {'avg>2x':>7}")
    print(header)
    print("-" * len(header))

    tot_sec = 0
    tot_single_1x = tot_single_2x = 0
    tot_avg_1x = tot_avg_2x = 0

    for art in articles:
        orig_path = mrn._BASES_DIR / art / "section_oracle.json"
        avg_path = mrn._BASES_DIR / art / "section_oracle_averaged.json"
        if not (orig_path.exists() and avg_path.exists()):
            print(f"{art:<42}  MISSING section_oracle.json or section_oracle_averaged.json, skipped")
            continue
        orig = json.loads(orig_path.read_text(encoding="utf-8"))["sections"]
        avg = json.loads(avg_path.read_text(encoding="utf-8"))["sections"]

        n = len(orig)
        s1 = sum(1 for sid in orig if _margin(orig[sid]["rewards"]) > diff_1x)
        s2 = sum(1 for sid in orig if _margin(orig[sid]["rewards"]) > diff_2x)
        a1 = sum(1 for sid in avg if _margin(avg[sid]["rewards"]) > avg_1x)
        a2 = sum(1 for sid in avg if _margin(avg[sid]["rewards"]) > avg_2x)

        tot_sec += n
        tot_single_1x += s1
        tot_single_2x += s2
        tot_avg_1x += a1
        tot_avg_2x += a2

        print(f"{art:<42} {n:>5} | {s1:>9} {s2:>9} | {a1:>7} {a2:>7}")

    print("-" * len(header))
    print(f"{'TOTAL':<42} {tot_sec:>5} | {tot_single_1x:>9} {tot_single_2x:>9} | "
          f"{tot_avg_1x:>7} {tot_avg_2x:>7}")
    print()
    if tot_sec:
        print(f"defensible-section share (single>1x-sd vs averaged>sqrt(N)-shrunk-1x-sd): "
              f"single-draw {tot_single_1x}/{tot_sec} ({tot_single_1x/tot_sec:.1%})  ->  "
              f"averaged(N={n_draws}) {tot_avg_1x}/{tot_sec} ({tot_avg_1x/tot_sec:.1%})")
        print(f"defensible-section share (single>2x-sd vs averaged>sqrt(N)-shrunk-2x-sd): "
              f"single-draw {tot_single_2x}/{tot_sec} ({tot_single_2x/tot_sec:.1%})  ->  "
              f"averaged(N={n_draws}) {tot_avg_2x}/{tot_sec} ({tot_avg_2x/tot_sec:.1%})")

    print()
    print("=" * 100)
    print("STEP C: full corpus (all production articles, single-draw only), re-scored at OLD vs NEW noise-sd")
    print("=" * 100)
    corpus = mgc.load_corpus()
    sec_stats, art_arms = mgc.evaluate(corpus, mgc.CANDIDATES["C2_soft_ga_pen010"])
    n_all = len(sec_stats)
    old_1x = sum(1 for s in sec_stats if s["margin"] > _OLD_DIFF_SD_1X)
    old_2x = sum(1 for s in sec_stats if s["margin"] > _OLD_DIFF_SD_2X)
    new_1x = sum(1 for s in sec_stats if s["margin"] > diff_1x)
    new_2x = sum(1 for s in sec_stats if s["margin"] > diff_2x)
    print(f"n = {n_all} sections (all production articles, current C2 formula, single draw)")
    print(f"  OLD (temp=0.25-confounded) thresholds: margin>1x={old_1x}/{n_all} ({old_1x/n_all:.1%})  "
          f"margin>2x={old_2x}/{n_all} ({old_2x/n_all:.1%})")
    print(f"  NEW (temp=0.7, unconfounded) thresholds: margin>1x={new_1x}/{n_all} ({new_1x/n_all:.1%})  "
          f"margin>2x={new_2x}/{n_all} ({new_2x/n_all:.1%})")

    train_stats = [s for s in sec_stats if s["split"] == "TRAIN"]
    n_train = len(train_stats)
    if n_train:
        t_old1 = sum(1 for s in train_stats if s["margin"] > _OLD_DIFF_SD_1X)
        t_new1 = sum(1 for s in train_stats if s["margin"] > diff_1x)
        t_old2 = sum(1 for s in train_stats if s["margin"] > _OLD_DIFF_SD_2X)
        t_new2 = sum(1 for s in train_stats if s["margin"] > diff_2x)
        print(f"  TRAIN-only (n={n_train}, matches GRPO's actual training set): "
              f"OLD 1x/2x={t_old1}/{n_train} ({t_old1/n_train:.1%})/{t_old2}/{n_train} ({t_old2/n_train:.1%})  "
              f"NEW 1x/2x={t_new1}/{n_train} ({t_new1/n_train:.1%})/{t_new2}/{n_train} ({t_new2/n_train:.1%})")

    print()
    print("=" * 100)
    print("STEP D: article-level production (single-draw) vs averaged oracle_arm/margin")
    print("=" * 100)
    margin_rows = {r["name"]: r for r in aom.scan(aom._DEFAULT_BASES_DIR, aom._DEFAULT_HIGH, aom._DEFAULT_MODERATE)}

    n_confirmed = n_flipped = n_hard_ruled = 0
    d_header = (f"{'article':<42} {'tier':<15} | {'production':>9} {'margin':>8} | "
                f"{'averaged':>9} {'margin':>8} | {'votes'}")
    print(d_header)
    print("-" * len(d_header))
    for art in articles:
        avg_path = mrn._BASES_DIR / art / "section_oracle_averaged.json"
        feat_path = mrn._BASES_DIR / art / "guideline_features.json"
        if not avg_path.exists():
            continue
        avg_sections = json.loads(avg_path.read_text(encoding="utf-8"))["sections"]
        feats = json.loads(feat_path.read_text(encoding="utf-8")).get("sections", {}) if feat_path.exists() else {}
        r_w, *_ = cao._compute_r_w(avg_sections, feats)
        ranked = sorted(r_w, key=r_w.get, reverse=True)
        avg_margin = r_w[ranked[0]] - r_w[ranked[1]]

        row = margin_rows.get(art, {})
        tier = row.get("risk_tier", "?")
        prod_arm = row.get("oracle_arm", "?")
        prod_margin = row.get("margin", float("nan"))

        # per-replicate raw vote tally (production draw + each replicate's own argmax),
        # reusing measure_replicate_noise's exact recompute path -- no formula duplication.
        sec_ids = list(avg_sections.keys())
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
        else:
            n_flipped += 1
            flag = "**FLIPPED**"

        print(f"{art:<42} {tier:<15} | {str(prod_arm):>9} {prod_margin:>8.4f} | "
              f"{ranked[0]:>9} {avg_margin:>8.4f} | {vote_str:<18} {flag}")

    print("-" * len(d_header))
    print(f"{n_confirmed} confirmed, {n_flipped} flipped, {n_hard_ruled} hard-ruled "
          f"(policy-forced/manual-override, immune to this comparison) out of {len(articles)}")


if __name__ == "__main__":
    main()
