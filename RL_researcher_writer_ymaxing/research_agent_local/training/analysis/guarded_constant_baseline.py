"""Guarded-constant baselines: the 4 trivial "always-X" predictors, each run
through the SAME deterministic policy guard used by the real pipeline
(forbidden -> P0 skip, required -> >= P1 light, capped -> <= P1 light), with
no RL/LLM signal at all. Mirrors preset_planner_handler.py::_apply_policy_guards /
test_planner.py::_apply_policy_guards exactly.

Purpose: isolate how much of RL+guards' edge over a plain "always-light"
baseline is just the guard rule firing on forbidden/required articles, vs.
genuine per-article discrimination by the RL model. See
run13_rl_grok_pipeline_analysis.md Appendix A (A.19+) for where this is
written up.

All inputs are read directly from on-disk JSON -- no inference, no MCP call:
  bases/<article>/guideline_features.json  -> external_evidence_policy
  bases/<article>/article_oracle.json      -> oracle_arm_idx, r_w_rewards_list

Usage (from research_agent_local/training/):
    python guarded_constant_baseline.py
"""

from __future__ import annotations

import json
import statistics
from math import comb
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent.parent
_REPO_ROOT = _AGENT_DIR.parent
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

ARMS = ["skip", "light", "standard", "deep"]

_TRAIN_LESSONS = [
    "02_workflows_vs_agents", "03_context_engineering", "05_workflow_patterns",
    "06_tools", "08_react_practice", "09_RAG", "10_memory_knowledge_access",
    "11_multimodal",
]
_VARIANTS = ("var_minimal", "var_standard", "var_demanding")
TRAIN_ARTICLES: list[str] = [
    f"{lesson}__{var}" for lesson in sorted(_TRAIN_LESSONS) for var in _VARIANTS
]

TEST_ARTICLES: list[str] = sorted([
    "04_structured_outputs", "07_reasoning_planning", "13_agent_framework",
    "14_agent_system_design", "29_evaluation_metrics", "31_CI",
    "Bird_Eye_Extreme", "Dark_Dimension", "Distinct_AI_Models",
    "Earth_Oceans_Origin", "Gravity_Entropy", "HNSW", "Insects_Consciousness",
    "Space-Time_QECC", "State_of_LLM_Reasoning", "Understanding_Reasoning_LLMs",
])

# RL+guards (run33/ep81) chosen arm per TEST article, read directly from
# rl_guards_only_train_and_test_results_run33_averaged_confidence_epoch81.md
# (post-2026-08-27 HNSW oracle-override flip; the model's own chosen arm does
# not depend on the oracle, so these match that report unchanged).
_RL_GUARDS_CHOSEN_TEST: dict[str, int] = {
    "04_structured_outputs": 3, "07_reasoning_planning": 1, "13_agent_framework": 1,
    "14_agent_system_design": 1, "29_evaluation_metrics": 3, "31_CI": 1,
    "Bird_Eye_Extreme": 1, "Dark_Dimension": 3, "Distinct_AI_Models": 1,
    "Earth_Oceans_Origin": 3, "Gravity_Entropy": 1, "HNSW": 1,
    "Insects_Consciousness": 1, "Space-Time_QECC": 1, "State_of_LLM_Reasoning": 0,
    "Understanding_Reasoning_LLMs": 2,
}


def _read_policy(article: str) -> str:
    feat = json.loads((_BASES_DIR / article / "guideline_features.json").read_text(encoding="utf-8"))
    return feat.get("external_evidence_policy", "allowed")


def _apply_policy_guards(preset: int, policy: str) -> int:
    """Mirrors preset_planner_handler.py / test_planner.py's guard exactly.

    capped's skip-vs-light choice defers to a real distribution in the other
    two mirrors; a fixed constant has none, so this is an unconditional
    ceiling clamp to light (never skip).
    """
    if policy == "forbidden":
        return 0
    if policy == "required":
        return max(1, preset)
    if policy == "capped":
        return min(preset, ARMS.index("light"))
    return preset


def _read_oracle(article: str) -> tuple[int, list[float], list[int]]:
    data = json.loads((_BASES_DIR / article / "article_oracle.json").read_text(encoding="utf-8"))
    return int(data["oracle_arm_idx"]), data["r_w_rewards_list"], data.get("tied_arm_indices", [])


def score_constant_baseline(articles: list[str], constant_idx: int) -> dict:
    """Score one guarded-constant baseline (predict `constant_idx`, then clamp
    by policy) against every article's oracle."""
    per_article: dict[str, dict] = {}
    exact = near = miss = 0
    regrets: list[float] = []
    for article in articles:
        policy = _read_policy(article)
        guarded = _apply_policy_guards(constant_idx, policy)
        oracle_idx, r_w, tied_idx = _read_oracle(article)
        accepted = {oracle_idx, *tied_idx}
        dist = 0 if guarded in accepted else min(abs(guarded - a) for a in accepted)
        if dist == 0:
            exact += 1
        elif dist == 1:
            near += 1
        else:
            miss += 1
        regret = None
        if policy != "forbidden":
            regret = r_w[oracle_idx] - r_w[guarded]
            regrets.append(regret)
        per_article[article] = {
            "policy": policy, "guarded_idx": guarded, "oracle_idx": oracle_idx,
            "tied_idx": tied_idx, "dist": dist, "regret": regret,
        }
    n = len(articles)
    mae = sum(v["dist"] for v in per_article.values()) / n
    return {
        "n": n, "exact": exact, "near": near, "miss": miss, "mae": mae,
        "regret_mean": statistics.mean(regrets) if regrets else None,
        "regret_max": max(regrets) if regrets else None,
        "regret_n": len(regrets),
        "per_article": per_article,
    }


def mcnemar_one_sided(b: int, c: int) -> float:
    """p = P(X <= c | X ~ Binomial(n=b+c, 0.5)) -- same convention as A.17.1/A.19.5."""
    n = b + c
    if n == 0:
        return float("nan")
    return sum(comb(n, i) for i in range(0, c + 1)) / (2 ** n)


def _p_tier(p: float) -> str:
    """strong (p<0.05) / suggestive (0.05<=p<0.20) / none -- unmodified 0.05 is
    underpowered at this n (see A.21 alpha discussion); 0.20 alone overclaims."""
    if p < 0.05:
        return "strong"
    if p < 0.20:
        return "suggestive"
    return "none"


def mcnemar_vs_model(per_article: dict, model_chosen: dict[str, int]) -> dict:
    b = c = both_correct = both_wrong = 0
    for article, v in per_article.items():
        accepted = {v["oracle_idx"], *v["tied_idx"]}
        baseline_correct = v["guarded_idx"] in accepted
        model_correct = model_chosen[article] in accepted
        if model_correct and baseline_correct:
            both_correct += 1
        elif model_correct:
            b += 1
        elif baseline_correct:
            c += 1
        else:
            both_wrong += 1
    return {
        "b": b, "c": c, "n": b + c, "p": mcnemar_one_sided(b, c),
        "both_correct": both_correct, "both_wrong": both_wrong,
    }


def _fmt_regret(value: float | None, width: int) -> str:
    return f"{value:{width}.4f}" if value is not None else " " * (width - 1) + "-"


def main() -> None:
    for split_name, articles in (("TRAIN", TRAIN_ARTICLES), ("TEST", TEST_ARTICLES)):
        print(f"\n=== {split_name}  (n={len(articles)}) ===")
        print(
            f"  {'baseline':<16} {'exact':>13} {'near':>13} {'miss':>13} "
            f"{'MAE':>7} {'regret_mean':>12} {'regret_max':>11}  (regret n)"
        )
        results = {}
        for idx, name in enumerate(ARMS):
            r = score_constant_baseline(articles, idx)
            results[name] = r
            n = r["n"]
            print(
                f"  always-{name:<9} "
                f"{r['exact']:>2}/{n:<3}({r['exact']/n*100:4.1f}%) "
                f"{r['near']:>2}/{n:<3}({r['near']/n*100:4.1f}%) "
                f"{r['miss']:>2}/{n:<3}({r['miss']/n*100:4.1f}%) "
                f"{r['mae']:7.3f} "
                f"{_fmt_regret(r['regret_mean'], 12)} "
                f"{_fmt_regret(r['regret_max'], 11)}  (n={r['regret_n']})"
            )

        if split_name == "TEST":
            print(f"\n  --- McNemar exact test: RL+guards (run33/ep81) vs. each guarded-constant baseline ---")
            print(f"  {'baseline':<16} {'b':>3} {'c':>3} {'n':>3} {'one-sided p':>12}  tier")
            for name, r in results.items():
                m = mcnemar_vs_model(r["per_article"], _RL_GUARDS_CHOSEN_TEST)
                print(
                    f"  always-{name:<9} {m['b']:>3} {m['c']:>3} {m['n']:>3} "
                    f"{m['p']:>12.4f}  {_p_tier(m['p'])}"
                )


if __name__ == "__main__":
    main()
