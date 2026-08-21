"""A.15.4 detail request (2026-08-20): margin, spread (cross-draw reward_sd), and
section-level flip-rate diagnostics for the 12 replicated TEST articles -- the
TEST-side analogue of A.13.1 (noise floor)/A.13.2 (defensible share)/A.15.4
(article margins), which so far have only been reported for TRAIN or at the
article-level for TEST.

Read-only, zero LLM calls. Reads section_oracle.json (production) and
section_oracle_averaged.json (written by merge_replicate_oracles.py, includes
"reward_sd" per arm/section -- the raw cross-draw std this script reports as
"spread") for the 12 already-replicated TEST articles.
"""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path

_TRAINING = Path(__file__).resolve().parent
sys.path.insert(0, str(_TRAINING))

import audit_oracle_margins as aom  # noqa: E402
import compute_article_oracle as cao  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402

_TEST_ARTICLES = [
    "Earth_Oceans_Origin", "Gravity_Entropy", "Dark_Dimension",
    "14_agent_system_design", "07_reasoning_planning", "Distinct_AI_Models",
    "04_structured_outputs", "Space-Time_QECC", "13_agent_framework",
    "Bird_Eye_Extreme", "Understanding_Reasoning_LLMs", "Insects_Consciousness",
]
ARM_ORDER = mrn._ARM_ORDER


def main():
    margin_rows = {r["name"]: r for r in aom.scan(aom._DEFAULT_BASES_DIR, aom._DEFAULT_HIGH, aom._DEFAULT_MODERATE)}

    all_cell_sds = []  # every (article, section, arm) cross-draw sd
    all_section_spans = []  # per (article, section): max(reward_sd) across arms -- worst-case spread
    per_article_rows = []
    n_section_flips_total = 0
    n_sections_total = 0
    arm_dist_prod = {a: 0 for a in ARM_ORDER}
    arm_dist_avg = {a: 0 for a in ARM_ORDER}

    print("=" * 120)
    print("Per-article: sections, spread (mean/max cross-draw reward_sd), section-level flip rate, article margin")
    print("=" * 120)
    hdr = (f"{'article':<32} {'tier':<10} {'n_sec':>5} | {'mean_sd':>7} {'max_sd':>7} | "
           f"{'sec_flips':>9} | {'prod_arm':>9} {'prod_mrg':>8} | {'avg_arm':>9} {'avg_mrg':>8}")
    print(hdr)
    print("-" * len(hdr))

    for art in _TEST_ARTICLES:
        so = json.loads((mrn._BASES_DIR / art / "section_oracle.json").read_text(encoding="utf-8"))
        avg = json.loads((mrn._BASES_DIR / art / "section_oracle_averaged.json").read_text(encoding="utf-8"))
        feats_path = mrn._BASES_DIR / art / "guideline_features.json"
        feats = json.loads(feats_path.read_text(encoding="utf-8")).get("sections", {}) if feats_path.exists() else {}

        sec_ids = list(so["sections"].keys())
        n_sections_total += len(sec_ids)
        article_cell_sds = []
        article_flips = 0
        for sid in sec_ids:
            sds = [avg["sections"][sid]["reward_sd"][a] for a in ARM_ORDER]
            article_cell_sds.extend(sds)
            all_cell_sds.extend(sds)
            all_section_spans.append(max(sds))
            prod_oracle = so["sections"][sid]["oracle"]
            avg_oracle = avg["sections"][sid]["oracle"]
            arm_dist_prod[prod_oracle] += 1
            arm_dist_avg[avg_oracle] += 1
            if prod_oracle != avg_oracle:
                article_flips += 1
                n_section_flips_total += 1

        row = margin_rows.get(art, {})
        tier = row.get("risk_tier", "?")
        prod_arm = row.get("oracle_arm", "?")
        prod_margin = row.get("margin", float("nan"))

        r_w, *_ = cao._compute_r_w(avg["sections"], feats)
        ranked = sorted(r_w, key=r_w.get, reverse=True)
        avg_margin = r_w[ranked[0]] - r_w[ranked[1]]

        mean_sd = statistics.mean(article_cell_sds)
        max_sd = max(article_cell_sds)
        print(f"{art:<32} {tier:<10} {len(sec_ids):>5} | {mean_sd:>7.4f} {max_sd:>7.4f} | "
              f"{article_flips:>6}/{len(sec_ids):<3}| {str(prod_arm):>9} {prod_margin:>8.4f} | "
              f"{ranked[0]:>9} {avg_margin:>8.4f}")

        per_article_rows.append({
            "article": art, "n_sec": len(sec_ids), "mean_sd": mean_sd, "max_sd": max_sd,
            "flips": article_flips, "prod_margin": prod_margin, "avg_margin": avg_margin,
        })

    print("-" * len(hdr))
    mean_all = statistics.mean(all_cell_sds)
    median_all = statistics.median(all_cell_sds)
    print(f"\nTEST cross-draw cell sd (n={len(all_cell_sds)} article*section*arm cells): "
          f"mean={mean_all:.4f}  median={median_all:.4f}")
    print(f"  1x/2x thresholds (mean-based): {mean_all:.4f} / {2*mean_all:.4f}")
    print(f"  (compare to TRAIN A.13.1 post-correction: mean=0.0659, median=0.0681, 1x=0.0932, 2x=0.1864)")

    print(f"\nSection-level oracle flip rate (production argmax vs averaged argmax), TEST 12 articles: "
          f"{n_section_flips_total}/{n_sections_total} = {n_section_flips_total/n_sections_total:.1%}")
    print(f"  (compare to TRAIN A.13.2: 79/171 = 46.2%)")

    print(f"\nSection-level arm distribution (production): {arm_dist_prod}")
    print(f"Section-level arm distribution (averaged):    {arm_dist_avg}")

    print("\n" + "=" * 120)
    print("Article margin distribution summary")
    print("=" * 120)
    prod_margins = [r["prod_margin"] for r in per_article_rows]
    avg_margins = [r["avg_margin"] for r in per_article_rows]
    print(f"production margins: mean={statistics.mean(prod_margins):+.4f}  median={statistics.median(prod_margins):+.4f}  "
          f"min={min(prod_margins):+.4f}  max={max(prod_margins):+.4f}")
    print(f"averaged   margins: mean={statistics.mean(avg_margins):+.4f}  median={statistics.median(avg_margins):+.4f}  "
          f"min={min(avg_margins):+.4f}  max={max(avg_margins):+.4f}")
    n_thin_prod = sum(1 for m in prod_margins if abs(m) < 0.02)
    n_thin_avg = sum(1 for m in avg_margins if abs(m) < 0.02)
    print(f"articles with |margin| < 0.02 (EPS_BAND near-tie): production {n_thin_prod}/12, averaged {n_thin_avg}/12")

    print("\nWorst cross-draw spread sections (top 8 by max arm reward_sd):")
    top_spread = sorted(
        ((art, sid, sd) for art in _TEST_ARTICLES
         for sid, sd in zip(
             json.loads((mrn._BASES_DIR / art / "section_oracle.json").read_text(encoding="utf-8"))["sections"].keys(),
             [max(json.loads((mrn._BASES_DIR / art / "section_oracle_averaged.json").read_text(encoding="utf-8"))["sections"][s]["reward_sd"][a] for a in ARM_ORDER)
              for s in json.loads((mrn._BASES_DIR / art / "section_oracle.json").read_text(encoding="utf-8"))["sections"].keys()])),
        key=lambda t: -t[2],
    )[:8]
    for art, sid, sd in top_spread:
        print(f"  {art:<32} {sid:<50} max_arm_sd={sd:.4f}")


if __name__ == "__main__":
    main()
