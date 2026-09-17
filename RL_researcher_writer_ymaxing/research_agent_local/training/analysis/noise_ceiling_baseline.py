"""Oracle self-consistency / "noise ceiling" baseline.

For every article with replicate data (n_draws_used == 3), computes the
article-level R_w argmax from EACH single draw alone (production,
replicate1, replicate2) and compares it to the argmax of the already-stored,
3-draw-averaged R_w vector (article_oracle.json's r_w_rewards_list -- this is
used as ground truth rather than `oracle_arm` because a handful of articles
carry a manual override that is NOT the R_w argmax; using r_w_rewards_list
isolates pure cross-draw measurement noise from override decisions).

This answers: if a hypothetical policy could perfectly read a single-draw's
own reward landscape (skip/light/standard/deep, one realization each) and
picked the argmax, how often would that already disagree with the "true"
(3-draw-averaged) label purely from draw-to-draw noise? That rate is a
practical ceiling on what ANY single-shot predictor -- including run33/ep81 --
could be expected to hit, since production inference only ever sees one
realization, not an average of three.

Usage (from research_agent_local/training/):
    python noise_ceiling_baseline.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))
sys.path.insert(0, str(_THIS_DIR.parent / "pipeline"))

import compute_article_oracle as cao  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402

ARMS = cao.ARMS  # ["skip", "light", "standard", "deep"]
BASES_DIR = cao._BASES_DIR

_TRAIN_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access",
    "11_multimodal",
]
_VARIANTS = ("var_minimal", "var_standard", "var_demanding")
TRAIN_ARTICLES = [f"{l}__{v}" for l in sorted(_TRAIN_LESSONS) for v in _VARIANTS]

TEST_ARTICLES = sorted([
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI",
    "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW", "Insects_Consciousness",
    "Space-Time_QECC", "State_of_LLM_Reasoning", "Understanding_Reasoning_LLMs",
])


def _single_draw_r_w(article: str, sections: dict, features: dict) -> dict[str, float]:
    r_w, _, _, _ = cao._compute_r_w(sections, features)
    return r_w


def per_draw_argmax(article: str):
    """Return (true_arm, {draw_name: single_draw_arm}) or None if not eligible."""
    oracle_path = BASES_DIR / article / "article_oracle.json"
    avg_path = BASES_DIR / article / "section_oracle_averaged.json"
    prod_path = BASES_DIR / article / "section_oracle.json"
    if not (oracle_path.exists() and avg_path.exists() and prod_path.exists()):
        return None
    oracle = json.loads(oracle_path.read_text(encoding="utf-8"))
    if oracle.get("n_draws_used", 1) != 3:
        return None

    r_w_true = oracle["r_w_rewards"]
    true_arm = max(ARMS, key=lambda a: r_w_true[a])

    avg = json.loads(avg_path.read_text(encoding="utf-8"))
    prod = json.loads(prod_path.read_text(encoding="utf-8"))
    feat = json.loads((BASES_DIR / article / "guideline_features.json").read_text(encoding="utf-8"))
    features_sections = feat.get("sections", {})
    replicate_ids = avg.get("replicate_ids_used", [1, 2])

    prod_sec_ids = mrn._production_sec_ids(article)
    sec_ids = list(prod["sections"].keys())
    if not prod_sec_ids or not set(sec_ids).issubset(set(prod_sec_ids)):
        prod_sec_ids = sec_ids

    draws = {"production": prod["sections"]}
    for r in replicate_ids:
        prefix = mrn._NOISE_EXPERIMENT_DIR / f"{article}__replicate{r}"
        draws[f"replicate{r}"] = mrn._compute_replicate_sections(
            article, prefix, prod_sec_ids
        )

    per_draw = {}
    for name, sections in draws.items():
        r_w = _single_draw_r_w(article, sections, features_sections)
        per_draw[name] = max(ARMS, key=lambda a: r_w[a])
    return true_arm, per_draw


def main() -> None:
    for split_name, articles in (("TRAIN", TRAIN_ARTICLES), ("TEST", TEST_ARTICLES)):
        print(f"\n=== {split_name} ===")
        n = 0
        agree = {"production": 0, "replicate1": 0, "replicate2": 0}
        dist_sum = {"production": 0, "replicate1": 0, "replicate2": 0}
        skipped = []
        for article in articles:
            result = per_draw_argmax(article)
            if result is None:
                skipped.append(article)
                continue
            true_arm, per_draw = result
            n += 1
            true_idx = cao.ARM_IDX[true_arm]
            row = f"  {article:42s} true={true_arm:8s} "
            for draw_name in ("production", "replicate1", "replicate2"):
                if draw_name not in per_draw:
                    continue
                d_arm = per_draw[draw_name]
                d_idx = cao.ARM_IDX[d_arm]
                match = d_arm == true_arm
                agree[draw_name] += int(match)
                dist_sum[draw_name] += abs(d_idx - true_idx)
                row += f"{draw_name}={d_arm:8s}({'=' if match else str(abs(d_idx-true_idx))}) "
            print(row)
        if skipped:
            print(f"  (skipped, no n_draws_used==3: {skipped})")
        print(f"\n  n={n}")
        for draw_name in ("production", "replicate1", "replicate2"):
            if n == 0:
                continue
            print(f"  single-draw={draw_name:12s} agreement={agree[draw_name]}/{n} "
                  f"({agree[draw_name]/n*100:.1f}%)  MAE={dist_sum[draw_name]/n:.3f}")
        # pooled across all 3 draws x n articles
        total_draws = sum(1 for a in articles if per_draw_argmax(a) is not None) * 0  # placeholder
    # pooled summary across both splits combined, all draws pooled
    print("\n=== POOLED across all draws (production+replicate1+replicate2), both splits ===")
    pooled_n = 0
    pooled_agree = 0
    pooled_dist = 0
    for articles in (TRAIN_ARTICLES, TEST_ARTICLES):
        for article in articles:
            result = per_draw_argmax(article)
            if result is None:
                continue
            true_arm, per_draw = result
            true_idx = cao.ARM_IDX[true_arm]
            for draw_name, d_arm in per_draw.items():
                pooled_n += 1
                pooled_agree += int(d_arm == true_arm)
                pooled_dist += abs(cao.ARM_IDX[d_arm] - true_idx)
    print(f"  n(draw observations)={pooled_n}  agreement={pooled_agree}/{pooled_n} "
          f"({pooled_agree/pooled_n*100:.1f}%)  MAE={pooled_dist/pooled_n:.3f}")


if __name__ == "__main__":
    main()
