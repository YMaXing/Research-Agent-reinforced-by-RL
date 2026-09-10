"""Full-corpus per-draw R_w table generator (all 40 TRAIN+TEST articles).

Read-only, zero new API calls. For every article with replicate data
(n_draws_used == 3), computes the article-level R_w for ALL FOUR arms from
EACH single draw (production, replicate1, replicate2) plus the already-
stored 3-draw-averaged R_w (article_oracle.json's r_w_rewards), and the
per-draw + averaged winning arm (argmax of that draw's own R_w vector).

Reuses noise_ceiling_baseline.py's exact per-draw section reconstruction
(_compute_replicate_sections) and compute_article_oracle.py's exact R_w
formula (_compute_r_w) -- no reward-formula duplication, per this repo's
own established convention.

Usage (from research_agent_local/training/):
    python full_corpus_per_draw_rw_table.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import compute_article_oracle as cao  # noqa: E402
import measure_replicate_noise as mrn  # noqa: E402
import noise_ceiling_baseline as ncb  # noqa: E402

ARMS = cao.ARMS
BASES_DIR = cao._BASES_DIR


def _single_draw_r_w(sections: dict, features: dict) -> dict[str, float]:
    r_w, _, _, _ = cao._compute_r_w(sections, features)
    return r_w


def per_article_full_table(article: str):
    """Return dict with per-draw R_w for all 4 arms + averaged, or None if ineligible."""
    oracle_path = BASES_DIR / article / "article_oracle.json"
    avg_path = BASES_DIR / article / "section_oracle_averaged.json"
    prod_path = BASES_DIR / article / "section_oracle.json"
    if not (oracle_path.exists() and avg_path.exists() and prod_path.exists()):
        return None
    oracle = json.loads(oracle_path.read_text(encoding="utf-8"))
    if oracle.get("n_draws_used", 1) < 2:
        return None

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
        draws[f"replicate{r}"] = mrn._compute_replicate_sections(article, prefix, prod_sec_ids)

    per_draw_r_w = {name: _single_draw_r_w(sections, features_sections) for name, sections in draws.items()}
    per_draw_winner = {name: max(ARMS, key=lambda a: r_w[a]) for name, r_w in per_draw_r_w.items()}

    r_w_avg = oracle["r_w_rewards"]
    winner_avg = max(ARMS, key=lambda a: r_w_avg[a])

    return {
        "oracle_arm": oracle.get("oracle_arm"),
        "policy": None,  # filled by caller if available
        "per_draw_r_w": per_draw_r_w,
        "per_draw_winner": per_draw_winner,
        "r_w_avg": r_w_avg,
        "winner_avg": winner_avg,
    }


def _fmt_arm_cell(per_draw_r_w: dict[str, dict[str, float]], r_w_avg: dict[str, float], arm: str) -> str:
    vals = [f"{r_w[arm]:.3f}" for r_w in per_draw_r_w.values()]
    return f"{'/'.join(vals)}\u2192{r_w_avg[arm]:.3f}"


def _fmt_winner_cell(per_draw_winner: dict[str, str], winner_avg: str) -> str:
    vals = list(per_draw_winner.values())
    return f"{'/'.join(vals)}\u2192**{winner_avg}**"


def main() -> None:
    for split_name, articles in (("TRAIN", ncb.TRAIN_ARTICLES), ("TEST", ncb.TEST_ARTICLES)):
        print(f"\n=== {split_name} (n={len(articles)}) ===")
        print("| article | R_w skip (draws→avg) | R_w light (draws→avg) "
              "| R_w standard (draws→avg) | R_w deep (draws→avg) | winner (draws→avg) |")
        print("|---|---|---|---|---|---|")
        skipped = []
        for article in articles:
            result = per_article_full_table(article)
            if result is None:
                skipped.append(article)
                continue
            pdr, avg = result["per_draw_r_w"], result["r_w_avg"]
            row = (
                f"| `{article}` "
                f"| {_fmt_arm_cell(pdr, avg, 'skip')} "
                f"| {_fmt_arm_cell(pdr, avg, 'light')} "
                f"| {_fmt_arm_cell(pdr, avg, 'standard')} "
                f"| {_fmt_arm_cell(pdr, avg, 'deep')} "
                f"| {_fmt_winner_cell(result['per_draw_winner'], result['winner_avg'])} |"
            )
            print(row)
        if skipped:
            print(f"\n(skipped, ineligible: {skipped})")


if __name__ == "__main__":
    main()
