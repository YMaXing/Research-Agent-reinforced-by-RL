"""Decompose deep's R_w shortfall by reward component, before touching cost_coef.

Motivation: F3's original concern (run13_rl_grok_pipeline_analysis.md Part 5-6,
§40/§49) was that `deep` pays a flat `-0.06/round` cost (`-0.18` total for 3
rounds) that its explore credit rarely earns back. Before treating `cost_coef`
as the lever to tune, this script empirically checks WHERE `deep`'s shortfall
against the winning arm actually comes from -- it could be the cost term, but
it could equally be `ga_gate` (guideline-adherence gate penalty, C2, Part 7
§53-57 -- ra removed, ga demoted from a weighted term to a flat threshold gate)
or `gt_base`.

Reuses sweep_reward_formula.py's existing recompute machinery (episode loading,
_credit(), section-context loading) -- does NOT duplicate the reward formula.
Zero LLM calls, zero re-grading; recomputes from already-graded reasoning.json
using the CURRENT (post-G0) production config by default.

Usage (from research_agent_local/training/):
  python3 analyze_cost_imbalance.py
  python3 analyze_cost_imbalance.py --articles 06_tools__var_standard 13_agent_framework
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "pipeline"))

import compute_article_oracle as cao
import generate_episode_oracles as geo
import sweep_reward_formula as srf

_THIS_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _THIS_DIR.parent.parent.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

_TRAIN_TOPICS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access", "11_multimodal",
]
_TRAIN_VARIANTS = ["var_minimal", "var_standard", "var_demanding"]
_TEST_ARTICLES = [
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI", "Bird_Eye_Extreme",
    "Dark_Dimension", "Distinct_AI_Models", "Earth_Oceans_Origin", "Gravity_Entropy",
    "HNSW", "Insects_Consciousness", "Space-Time_QECC", "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
]
_MIXEDDEPTH = ["Distinct_AI_Models__mixeddepth", "Insects_Consciousness__mixeddepth"]

_ALL_42 = [f"{t}__{v}" for t in _TRAIN_TOPICS for v in _TRAIN_VARIANTS] + _TEST_ARTICLES + _MIXEDDEPTH


def _recompute_components(article_dir_name: str, cfg: dict) -> dict[str, dict[str, float]] | None:
    """Same recompute as sweep_reward_formula._recompute_any, but returns each
    arm's 4 reward components SEPARATELY (gt_base, explore, user_intent, cost)
    instead of just their sum, aggregated the SAME way _compute_r_w aggregates
    R_w: gt_base/user_intent are target-words-weighted means across sections;
    explore is a simple (unweighted) mean (matches shipped candidate E); cost
    is a per-article constant (-cost_coef * nr) since it never varies by
    section for a given arm.
    """
    bases_dir = _BASES_DIR / article_dir_name
    digest_path = bases_dir / "research_digest.md"
    features_path = bases_dir / "guideline_features.json"
    if not (digest_path.exists() and features_path.exists()):
        return None

    digest = digest_path.read_text(encoding="utf-8")
    sec_ids = geo._extract_sec_ids_ordered(digest)
    sec_norms = [geo._sec_id_to_norm(s) for s in sec_ids]
    features = json.loads(features_path.read_text(encoding="utf-8"))["sections"]

    is_train_variant = "__var_" in article_dir_name
    if is_train_variant:
        root = srf._EPISODES_DIR
        ep_rounds = geo._EPISODE_ROUNDS
        arm_presets = geo._ARM_PRESETS
    else:
        root = srf._TEST_EPISODES_DIR
        ep_rounds = geo._TEST_EPISODE_ROUNDS
        arm_presets = geo._TEST_ARM_PRESETS
    episode_dims = {p: geo._load_episode(root / f"{article_dir_name}__preset{p}") for p in ep_rounds}

    cost_coef = cfg.get("cost_coef", srf._PROD_COST_COEF)

    # Accumulators: {arm: {"gt_base": tw-weighted sum, "ga_gate": tw-weighted sum,
    #                      "explore": simple sum, "cost": constant}}
    acc_gt_base = {a: 0.0 for a in geo._ARM_ORDER}
    acc_ga_gate = {a: 0.0 for a in geo._ARM_ORDER}
    acc_explore = {a: 0.0 for a in geo._ARM_ORDER}
    total_w = 0
    n_sections = len(sec_ids)

    for sec_idx, (sec_id, sec_norm) in enumerate(zip(sec_ids, sec_norms)):
        feat = features.get(sec_id, {})
        tw_val = feat.get("target_words")
        tw = int(tw_val) if tw_val is not None else 100
        total_w += tw

        for arm, preset_ids in arm_presets.items():
            p = preset_ids[0]
            nr = ep_rounds[p]
            ep = episode_dims.get(p, {})

            def _score(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                return geo._get_score(_ep.get(dim, []), _sn, _si)

            def _enh(dim: str, _ep=ep, _sn=sec_norm, _si=sec_idx) -> float:
                e = geo._get_enhancement(_ep.get(dim, []), _sn, _si)
                if e is None:
                    return _score(dim)
                return srf._credit(e[1], cfg)

            cc = _score("ground_truth_core_content")
            fl = _score("ground_truth_flow")
            de = _enh("ground_truth_depth_enhancement")
            be = _enh("ground_truth_breadth_enhancement")
            cp = _score("ground_truth_core_preservation")
            ga = _score("user_intent_guideline_adherence")

            de_weight = cfg.get("de_weight", srf._PROD_DE_WEIGHT)
            be_weight = cfg.get("be_weight", srf._PROD_BE_WEIGHT)
            ga_threshold = cfg.get("ga_gate_threshold", srf._PROD_GA_GATE_THRESHOLD)
            ga_penalty = cfg.get("ga_gate_penalty", srf._PROD_GA_GATE_PENALTY)

            gt_base = 0.20 * cc + 0.20 * fl
            explore = cp * (de_weight * de + be_weight * be)
            ga_gate = ga_penalty if ga < ga_threshold else 0.0

            acc_gt_base[arm] += tw * gt_base
            acc_ga_gate[arm] += tw * ga_gate
            acc_explore[arm] += explore

    if total_w == 0:
        return None

    out = {}
    for arm, preset_ids in arm_presets.items():
        # cost uses geo._ARM_COST_UNITS (empirical, shipped as H0 2026-07-25),
        # NOT the raw ep_rounds ordinal count -- keep in sync with
        # generate_episode_oracles.py / sweep_reward_formula.py's _PROD_ARM_COST_UNITS.
        units = cfg.get("cost_units", geo._ARM_COST_UNITS)[arm]
        out[arm] = {
            "gt_base": acc_gt_base[arm] / total_w,
            "ga_gate": acc_ga_gate[arm] / total_w,
            "explore": acc_explore[arm] / n_sections,
            "cost": cost_coef * units,
        }
        out[arm]["total"] = sum(out[arm][k] for k in ("gt_base", "ga_gate", "explore", "cost"))
    return out


def analyze(articles: list[str]) -> None:
    rows = []
    for article in articles:
        components = _recompute_components(article, {})
        if components is None:
            print(f"SKIP {article}: no digest/features found")
            continue
        winner = max(components, key=lambda a: components[a]["total"])
        deep = components["deep"]
        gap = components[winner]["total"] - deep["total"]
        rows.append({"article": article, "components": components, "winner": winner, "deep_gap": gap})

        print(f"{article}")
        for arm in geo._ARM_ORDER:
            c = components[arm]
            marker = " <-- WINNER" if arm == winner else (" <-- DEEP" if arm == "deep" else "")
            print(
                f"  {arm:9s} gt_base={c['gt_base']:+.4f} explore={c['explore']:+.4f} "
                f"ga_gate={c['ga_gate']:+.4f} cost={c['cost']:+.4f}  total={c['total']:+.4f}{marker}"
            )
        if winner != "deep":
            wc, dc = components[winner], deep
            print(
                f"  deep's gap vs {winner}: {gap:+.4f}  (gt_base Δ={wc['gt_base']-dc['gt_base']:+.4f}, "
                f"explore Δ={wc['explore']-dc['explore']:+.4f}, ga_gate Δ={wc['ga_gate']-dc['ga_gate']:+.4f}, "
                f"cost Δ={wc['cost']-dc['cost']:+.4f})"
            )
        print()

    # Aggregate: for articles where deep did NOT win, decompose the average gap by component.
    non_winners = [r for r in rows if r["winner"] != "deep"]
    n = len(non_winners)
    if n == 0:
        print("deep won every article in this sample -- nothing to decompose.")
        return

    avg_delta = {"gt_base": 0.0, "explore": 0.0, "ga_gate": 0.0, "cost": 0.0}
    for r in non_winners:
        wc, dc = r["components"][r["winner"]], r["components"]["deep"]
        for k in avg_delta:
            avg_delta[k] += (wc[k] - dc[k]) / n

    print("=" * 100)
    print(f"N articles where deep did NOT win: {n}/{len(rows)}")
    print(f"Mean gap (winner - deep), decomposed by component:")
    for k, v in avg_delta.items():
        print(f"  {k:12s} {v:+.4f}")
    print(f"  {'TOTAL':12s} {sum(avg_delta.values()):+.4f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--articles", nargs="+", default=None, help="Default: all 42 production articles")
    args = parser.parse_args()
    analyze(args.articles or _ALL_42)


if __name__ == "__main__":
    main()
