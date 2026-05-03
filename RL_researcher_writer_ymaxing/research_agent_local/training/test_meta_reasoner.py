"""
Meta-reasoner integration test.

For each test article (held-out from RL training), this script:

  1. Reads the research_digest.md that already exists in rl_training_data/bases/
  2. Runs the Qwen3-4B LoRA model inference via ExplorationStrategySelector
  3. Prints the full structured RL signal JSON (exactly what Grok would receive)
  4. Computes the oracle preset from the offline reward data
  5. Records a hit/miss comparison and prints a summary table

The "plan vs label" comparison is:
  - RL preset == oracle preset  →  EXACT HIT
  - |RL preset - oracle preset| == 1  →  NEAR MISS (adjacent strategy)
  - otherwise  →  MISS

Usage (from research_agent_local/):
  uv run python training/test_meta_reasoner.py

  # Use a specific checkpoint
  uv run python training/test_meta_reasoner.py \
      --checkpoint rl_training_data/checkpoints/tasks/task_20260420_223150/best

  # Override which articles to test (comma-separated, no spaces)
  uv run python training/test_meta_reasoner.py --articles 02_workflows_vs_agents,09_RAG

  # Save full signal JSON for each article to disk
  uv run python training/test_meta_reasoner.py --save-json
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths (mirrors eval_accuracy.py)
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_AGENT_DIR = _THIS_DIR.parent                  # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent                 # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"
_DEFAULT_CHECKPOINT = (
    _REPO_ROOT / "rl_training_data" / "checkpoints" / "tasks"
    / "task_20260420_223150" / "best"
)

# ---------------------------------------------------------------------------
# Article sets
# ---------------------------------------------------------------------------
_TRAIN_ARTICLES = {
    "03_context_engineering",
    "05_workflow_patterns",
    "08_react_practice",
    "11_multimodal",
}
_ALL_ARTICLES = [
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "11_multimodal",
]
_DEFAULT_TEST_ARTICLES = [a for a in _ALL_ARTICLES if a not in _TRAIN_ARTICLES]

# ---------------------------------------------------------------------------
# Preset metadata (mirrors eval_accuracy.py)
# ---------------------------------------------------------------------------
_PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
_PRESET_NAMES = {
    0: "P0  no_exploration",
    1: "P1  1_round_balanced",
    2: "P2  2_rounds_balanced→depth",
    3: "P3  2_rounds_depth→breadth",
    4: "P4  3_rounds_balanced→depth→breadth",
    5: "P5  3_rounds_depth→breadth→depth",
}
_NUM_PRESETS = 6
_REWARD_DIMS = [
    "ground_truth_core_content",
    "ground_truth_flow",
    "ground_truth_depth_enhancement",
    "ground_truth_breadth_enhancement",
    "ground_truth_core_preservation",
    "user_intent_guideline_adherence",
    "user_intent_research_anchoring",
]

# ---------------------------------------------------------------------------
# Oracle helpers (copied from eval_accuracy.py)
# ---------------------------------------------------------------------------
import re


def _compute_reward(scores: dict, preset_id: int) -> float:
    cc = scores["ground_truth_core_content"]
    fl = scores["ground_truth_flow"]
    de = scores["ground_truth_depth_enhancement"]
    be = scores["ground_truth_breadth_enhancement"]
    cp = scores["ground_truth_core_preservation"]
    ga = scores["user_intent_guideline_adherence"]
    ra = scores["user_intent_research_anchoring"]
    nr = _PRESET_ROUNDS[preset_id]
    gt_base = 0.20 * cc + 0.20 * fl
    explore = cp * (0.60 * de + 0.40 * be) * 0.30
    user_intent = (0.50 * ga + 0.50 * ra) * 0.30
    cost = -0.02 * nr
    return gt_base + explore + user_intent + cost


def _compute_oracle(article: str) -> tuple[int, list[float]]:
    """Return (oracle_preset, rewards[0..5]) from article-level scores.json."""
    rewards = []
    for p in range(_NUM_PRESETS):
        ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
        scores_path = ep_dir / "scores.json"
        if not scores_path.exists():
            raise FileNotFoundError(f"Missing scores.json for {article} preset {p}: {scores_path}")
        scores = json.loads(scores_path.read_text(encoding="utf-8"))
        rewards.append(_compute_reward(scores, p))
    oracle = int(rewards.index(max(rewards)))
    return oracle, rewards


# ---------------------------------------------------------------------------
# Signal helpers
# ---------------------------------------------------------------------------

def _entropy(probs: list[float]) -> float:
    eps = 1e-12
    return -sum(p * math.log2(p + eps) for p in probs)


def _top2(probs: list[float]) -> list[list]:
    ranked = sorted(enumerate(probs), key=lambda x: x[1], reverse=True)
    return [[f"P{ranked[i][0]}", round(ranked[i][1], 4)] for i in range(2)]


def _guidance(preset: int, confidence: float, entropy: float, floor_applied: bool) -> str:
    parts: list[str] = []
    if entropy > 1.5:
        parts.append(f"RL model is uncertain (H={entropy:.2f} bits > 1.5) — apply own judgement.")
    elif confidence >= 0.70:
        parts.append(
            f"RL model strongly recommends P{preset} "
            f"({_PRESET_NAMES[preset].strip()}, confidence {confidence:.0%})."
        )
    else:
        parts.append(
            f"RL model recommends P{preset} "
            f"({_PRESET_NAMES[preset].strip()}, confidence {confidence:.0%})."
        )
    if floor_applied:
        parts.append(
            "Floor correction fired: a technical section needed more exploration "
            "than the aggregate vote suggested."
        )
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Per-article test
# ---------------------------------------------------------------------------

def run_article(article: str, selector) -> dict:
    """Run RL inference on one article and return the full result dict."""
    digest_path = _BASES_DIR / article / "research_digest.md"
    if not digest_path.exists():
        return {"article": article, "status": "error", "message": f"Digest not found: {digest_path}"}

    digest = digest_path.read_text(encoding="utf-8")

    preset, agg_probs, section_details, meta = selector.predict_article_verbose(digest)

    confidence = round(agg_probs[preset], 4)
    h = round(_entropy(agg_probs), 4)
    section_vote = meta.get("section_vote", preset)
    section_floor = meta.get("section_floor", 0)
    floor_applied = section_vote <= 2 and section_floor > section_vote and h <= 1.5

    section_signals = []
    for d in section_details:
        section_signals.append({
            "title": d["title"],
            "preset": d["chosen"],
            "name": _PRESET_NAMES[d["chosen"]].strip(),
            "top2": _top2(d["probs"]),
        })

    guidance_str = _guidance(preset, confidence, h, floor_applied)

    # Oracle
    try:
        oracle, oracle_rewards = _compute_oracle(article)
    except FileNotFoundError as exc:
        oracle, oracle_rewards = -1, []
        print(f"  [WARN] Oracle data missing: {exc}")

    # Comparison
    if oracle == -1:
        verdict = "UNKNOWN (no oracle data)"
    elif preset == oracle:
        verdict = "EXACT HIT"
    elif abs(preset - oracle) == 1:
        verdict = "NEAR MISS  (±1 preset)"
    else:
        verdict = f"MISS  (predicted P{preset} vs oracle P{oracle})"

    return {
        "article": article,
        "status": "success",
        "split": "TRAIN" if article in _TRAIN_ARTICLES else "TEST",
        "rl_signal": {
            "rl_recommendation": {
                "preset": preset,
                "name": _PRESET_NAMES[preset].strip(),
                "confidence": confidence,
                "entropy_bits": h,
                "floor_correction_applied": floor_applied,
            },
            "section_signals": section_signals,
            "guidance": guidance_str,
        },
        "oracle": {
            "preset": oracle,
            "name": _PRESET_NAMES[oracle].strip() if oracle >= 0 else "N/A",
            "rewards": [round(r, 4) for r in oracle_rewards],
        },
        "verdict": verdict,
    }


# ---------------------------------------------------------------------------
# Rendering helpers
# ---------------------------------------------------------------------------

_VERDICT_ICON = {
    "EXACT HIT": "✓",
}


def _print_article_result(result: dict, verbose: bool = True) -> None:
    article = result["article"]
    split = result.get("split", "?")
    print(f"\n{'='*72}")
    print(f"  Article: {article}  [{split}]")
    print(f"{'='*72}")

    if result["status"] == "error":
        print(f"  ERROR: {result['message']}")
        return

    sig = result["rl_signal"]
    rec = sig["rl_recommendation"]
    oracle = result["oracle"]

    print(f"\n  RL RECOMMENDATION")
    print(f"    Preset      : {rec['preset']}  ({rec['name']})")
    print(f"    Confidence  : {rec['confidence']:.2%}")
    print(f"    Entropy     : {rec['entropy_bits']:.3f} bits", end="")
    if rec["entropy_bits"] > 1.5:
        print("  ← HIGH (uncertain)", end="")
    elif rec["entropy_bits"] < 0.5:
        print("  ← LOW (very confident)", end="")
    print()
    print(f"    Floor fired : {rec['floor_correction_applied']}")
    print(f"    Guidance    : {sig['guidance']}")

    print(f"\n  ORACLE")
    print(f"    Preset      : {oracle['preset']}  ({oracle['name']})")
    if oracle["rewards"]:
        reward_str = "  ".join(f"P{i}:{r:.4f}" for i, r in enumerate(oracle["rewards"]))
        print(f"    Rewards     : {reward_str}")

    verdict = result["verdict"]
    icon = "✓" if "EXACT HIT" in verdict else ("~" if "NEAR MISS" in verdict else "✗")
    print(f"\n  VERDICT: {icon}  {verdict}")

    if verbose and sig["section_signals"]:
        print(f"\n  SECTION SIGNALS  ({len(sig['section_signals'])} sections)")
        for s in sig["section_signals"]:
            top1, top2 = s["top2"][0], s["top2"][1]
            gap = round(top1[1] - top2[1], 4)
            print(f"    [{s['preset']}]  {s['title'][:50]:<50}  "
                  f"top2: {top1[0]}={top1[1]:.3f}  {top2[0]}={top2[1]:.3f}  gap={gap:.3f}")


def _print_summary(results: list[dict]) -> None:
    print(f"\n{'#'*72}")
    print(f"  SUMMARY")
    print(f"{'#'*72}")

    header = f"  {'Article':<35} {'Split':<6} {'RL':>3}  {'Oracle':>6}  Verdict"
    print(header)
    print(f"  {'-'*67}")

    exact = near = miss = unknown = 0
    for r in results:
        if r["status"] == "error":
            print(f"  {r['article']:<35} {'?':<6}  ERROR: {r['message']}")
            unknown += 1
            continue
        split = r["split"]
        rl_p = r["rl_signal"]["rl_recommendation"]["preset"]
        oracle_p = r["oracle"]["preset"]
        verdict = r["verdict"]
        icon = "✓" if "EXACT HIT" in verdict else ("~" if "NEAR MISS" in verdict else "✗")
        print(f"  {r['article']:<35} {split:<6}  P{rl_p}  →  P{oracle_p}   {icon}  {verdict}")
        if "EXACT HIT" in verdict:
            exact += 1
        elif "NEAR MISS" in verdict:
            near += 1
        elif "UNKNOWN" in verdict:
            unknown += 1
        else:
            miss += 1

    total = len(results)
    test_results = [r for r in results if r.get("split") == "TEST" and r["status"] == "success"]
    test_exact = sum(1 for r in test_results if "EXACT HIT" in r["verdict"])
    test_near = sum(1 for r in test_results if "NEAR MISS" in r["verdict"])

    print(f"\n  Overall  ({total} articles):  "
          f"exact={exact}  near={near}  miss={miss}  unknown={unknown}")
    if test_results:
        print(f"  TEST-set ({len(test_results)} articles): "
              f"exact={test_exact}  near={test_near}  "
              f"miss={len(test_results)-test_exact-test_near}")
        print(f"  TEST accuracy (exact):     {test_exact}/{len(test_results)} = "
              f"{test_exact/len(test_results):.0%}")
        print(f"  TEST accuracy (exact+near):{(test_exact+test_near)}/{len(test_results)} = "
              f"{(test_exact+test_near)/len(test_results):.0%}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Test the RL meta-reasoner on held-out articles")
    p.add_argument(
        "--checkpoint",
        type=Path,
        default=_DEFAULT_CHECKPOINT,
        help="Path to LoRA adapter checkpoint directory",
    )
    p.add_argument(
        "--articles",
        default=",".join(_DEFAULT_TEST_ARTICLES),
        help=(
            "Comma-separated list of article IDs to evaluate. "
            f"Default: test articles {_DEFAULT_TEST_ARTICLES}"
        ),
    )
    p.add_argument(
        "--all",
        action="store_true",
        help="Evaluate all articles (including training articles)",
    )
    p.add_argument(
        "--save-json",
        action="store_true",
        help="Save each article's full result JSON to meta_reasoner_test_results/",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Skip per-section signal breakdown in per-article output",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if args.all:
        articles = _ALL_ARTICLES
    else:
        articles = [a.strip() for a in args.articles.split(",") if a.strip()]

    checkpoint = args.checkpoint
    if not checkpoint.exists():
        print(f"ERROR: Checkpoint not found: {checkpoint}")
        sys.exit(1)

    print(f"\nMeta-Reasoner Test")
    print(f"  Checkpoint : {checkpoint}")
    print(f"  Articles   : {articles}")

    sys.path.insert(0, str(_THIS_DIR))
    from infer import ExplorationStrategySelector

    print("\nLoading RL model (may take ~3 min on GPU, ~30 s on CPU)…")
    selector = ExplorationStrategySelector(adapter_dir=checkpoint)
    print("Model loaded.\n")

    results: list[dict] = []
    for article in articles:
        result = run_article(article, selector)
        results.append(result)
        _print_article_result(result, verbose=not args.quiet)

    _print_summary(results)

    if args.save_json:
        out_dir = _AGENT_DIR / "meta_reasoner_test_results"
        out_dir.mkdir(exist_ok=True)
        for r in results:
            out_path = out_dir / f"{r['article']}.json"
            out_path.write_text(json.dumps(r, indent=2), encoding="utf-8")
            print(f"  Saved: {out_path}")
        summary_path = out_dir / "_summary.json"
        summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"  Saved: {summary_path}")


if __name__ == "__main__":
    main()
