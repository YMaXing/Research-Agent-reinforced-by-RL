"""
Preset planner test: predict_exploration_preset tool (direct MCP call).

The tool now makes the final planning decision internally via two stages:
  Stage 1 — Qwen3-4B RL model  -> rl_recommendation
  Stage 2 — Grok 4.2 reasoning -> grok_recommendation

This test calls the tool directly via the MCP protocol, bypassing the
Grok-4.1-fast orchestration layer that previously parsed preset decisions
from free-text responses (which could return None for long contexts).

The mcp-agent is still used to manage the server subprocess and expose the
MCP transport, but no LLM agent loop is involved.

Modes
-----
  default     — reads grok_recommendation.preset (full pipeline: RL → Grok 4.2)
  --rl-only   — reads rl_recommendation.preset   (Qwen3-4B only, no Grok 4.2)
  --grok-only — reads grok_recommendation.preset (Grok 4.2 standalone, no RL signals)
                Use as a baseline to measure the RL model's marginal contribution.

Usage (from research_agent_local/)
-----------------------------------
  # Test-set articles only (default full pipeline)
  uv run python -m mcp_client.src.test_grok_planner

  # RL model only — faster, no Grok 4.2 call
  uv run python -m mcp_client.src.test_grok_planner --rl-only

  # Grok 4.2 standalone baseline — no RL section signals
  uv run python -m mcp_client.src.test_grok_planner --grok-only

  # All articles (train + test)
  uv run python -m mcp_client.src.test_grok_planner --all

  # Specific articles
  uv run python -m mcp_client.src.test_grok_planner --articles 02_workflows_vs_agents,09_RAG

  # Save per-article JSON results
  uv run python -m mcp_client.src.test_grok_planner --save-json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import math
from pathlib import Path

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.config import get_settings as get_mcp_settings

from .settings import settings
from .utils.logging_utils import configure_logging
from .utils.mcp_startup_utils import get_capabilities_from_mcp_client

configure_logging()

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent
_CLIENT_DIR = _THIS_DIR.parent                       # mcp_client/
_AGENT_DIR = _CLIENT_DIR.parent                      # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent                       # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_EPISODES_DIR = _REPO_ROOT / "rl_training_data" / "episodes"

# ---------------------------------------------------------------------------
# Article sets (mirrors test_meta_reasoner.py)
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
# Preset metadata (mirrors test_meta_reasoner.py)
# ---------------------------------------------------------------------------
_NUM_PRESETS = 6
_PRESET_ROUNDS = {0: 0, 1: 1, 2: 2, 3: 2, 4: 3, 5: 3}
_PRESET_NAMES = {
    0: "P0  no_exploration",
    1: "P1  1_round_balanced",
    2: "P2  2_rounds_balanced→depth",
    3: "P3  2_rounds_depth→breadth",
    4: "P4  3_rounds_balanced→depth→breadth",
    5: "P5  3_rounds_depth→breadth→depth",
}

# ---------------------------------------------------------------------------
# MCP app (created once, shared across all articles)
# ---------------------------------------------------------------------------
_mcp_settings = get_mcp_settings(str(Path(__file__).parent / "mcp_agent.config.yaml"))
_mcp_settings.mcp.servers["research_agent"].args = [
    "--directory", str(settings.server_main_path),
    "run", "python", "-m", "src.server", "--transport", "stdio",
]
app = MCPApp(name="GrokPlannerTest", settings=_mcp_settings)


# ---------------------------------------------------------------------------
# Oracle computation (mirrors test_meta_reasoner.py)
# ---------------------------------------------------------------------------
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
    """Return (oracle_preset, rewards[0..5])."""
    rewards = []
    for p in range(_NUM_PRESETS):
        ep_dir = _EPISODES_DIR / f"{article}__preset{p}"
        scores_path = ep_dir / "scores.json"
        if not scores_path.exists():
            raise FileNotFoundError(f"Missing scores.json: {scores_path}")
        scores = json.loads(scores_path.read_text(encoding="utf-8"))
        rewards.append(_compute_reward(scores, p))
    oracle = int(rewards.index(max(rewards)))
    return oracle, rewards


# ---------------------------------------------------------------------------
# Tool call + result parsing
# ---------------------------------------------------------------------------
def _parse_tool_result(tool_result) -> dict:
    """Extract the JSON dict from an MCP CallToolResult."""
    if getattr(tool_result, "isError", False):
        raise RuntimeError(f"Tool returned an error: {tool_result}")
    content = getattr(tool_result, "content", None)
    if not content:
        raise RuntimeError("Tool returned empty content.")
    text = getattr(content[0], "text", None)
    if text is None:
        raise RuntimeError(f"First content item has no .text: {content[0]!r}")
    return json.loads(text)


# ---------------------------------------------------------------------------
# Per-article runner
# ---------------------------------------------------------------------------
async def run_article(article: str, agent: Agent, rl_only: bool, grok_only: bool = False) -> dict:
    research_dir = _BASES_DIR / article
    if not research_dir.exists():
        return {"article": article, "error": f"Directory not found: {research_dir}"}

    # --- Direct MCP tool call (no LLM agent loop) ---
    tool_args: dict = {"research_directory": str(research_dir)}
    if grok_only:
        tool_args["grok_only"] = True
    try:
        tool_result = await agent.call_tool("predict_exploration_preset", tool_args)
        data = _parse_tool_result(tool_result)
    except Exception as exc:
        return {"article": article, "error": str(exc)}

    if data.get("status") == "error":
        return {"article": article, "error": data.get("message", "unknown error")}

    rl = data.get("rl_recommendation")   # None when grok_only=True
    grok = data.get("grok_recommendation")  # None if XAI_API_KEY unset or call failed

    # Determine which preset to evaluate
    if grok_only:
        if grok is None:
            return {"article": article, "error": "Grok standalone call failed or XAI_API_KEY not set"}
        chosen_preset = grok["preset"]
        chosen_by = "Grok-only"
    elif rl_only or grok is None:
        chosen_preset = rl["preset"]
        chosen_by = "RL"
    else:
        chosen_preset = grok["preset"]
        chosen_by = "Grok4.2"

    # --- Oracle ---
    try:
        oracle_preset, rewards = _compute_oracle(article)
    except FileNotFoundError as exc:
        return {
            "article": article,
            "split": "TRAIN" if article in _TRAIN_ARTICLES else "TEST",
            "rl_preset": rl["preset"] if rl else None,
            "grok_preset": grok["preset"] if grok else None,
            "chosen_preset": chosen_preset,
            "chosen_by": chosen_by,
            "oracle_preset": None,
            "verdict": "NO_ORACLE",
            "entropy_bits": rl["entropy_bits"] if rl else None,
            "confidence": rl["confidence"] if rl else None,
            "floor_applied": rl["floor_correction_applied"] if rl else None,
            "grok_override": grok.get("override") if grok else None,
            "grok_reasoning": grok.get("reasoning") if grok else None,
            "grok_override_reason": grok.get("override_reason") if grok else None,
            "error": str(exc),
        }

    if chosen_preset == oracle_preset:
        verdict = "EXACT"
    elif abs(chosen_preset - oracle_preset) == 1:
        verdict = "NEAR"
    else:
        verdict = "MISS"

    return {
        "article": article,
        "split": "TRAIN" if article in _TRAIN_ARTICLES else "TEST",
        "rl_preset": rl["preset"] if rl else None,
        "grok_preset": grok["preset"] if grok else None,
        "chosen_preset": chosen_preset,
        "chosen_by": chosen_by,
        "oracle_preset": oracle_preset,
        "rewards": [round(r, 4) for r in rewards],
        "verdict": verdict,
        "entropy_bits": rl["entropy_bits"] if rl else None,
        "confidence": rl["confidence"] if rl else None,
        "floor_applied": rl["floor_correction_applied"] if rl else None,
        "grok_override": grok.get("override") if grok else None,
        "grok_reasoning": grok.get("reasoning") if grok else None,
        "grok_override_reason": grok.get("override_reason") if grok else None,
    }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
_VERDICT_SYM = {
    "EXACT": "✓  EXACT HIT",
    "NEAR": "~  NEAR MISS  (±1 preset)",
    "MISS": "✗  MISS",
    "NO_ORACLE": "?  NO ORACLE DATA",
}


def _print_article_result(r: dict) -> None:
    print()
    if "error" in r and r.get("verdict") not in ("NO_ORACLE",):
        print(f"  ERROR: {r['error']}")
        return

    rl_p = r.get("rl_preset")
    gp = r.get("grok_preset")
    chosen = r.get("chosen_preset")
    op = r.get("oracle_preset")
    verdict = r.get("verdict", "?")
    entropy = r.get("entropy_bits")
    conf = r.get("confidence")
    floor = r.get("floor_applied")

    chosen_by = r.get("chosen_by", "?")
    is_grok_only = (chosen_by == "Grok-only")

    if rl_p is not None:
        floor_tag = "  [floor applied]" if floor else ""
        print(f"  RL model   : P{rl_p}  ({_PRESET_NAMES.get(rl_p, '?')})  "
              f"conf={conf:.0%}  H={entropy:.2f}bits{floor_tag}")
    elif is_grok_only:
        print(f"  RL model   : (skipped -- --grok-only baseline)")

    if gp is not None:
        if is_grok_only:
            print(f"  Grok 4.2   : P{gp}  ({_PRESET_NAMES.get(gp, '?')})  [standalone, no RL input]")
        else:
            override_tag = "  [OVERRIDE]" if r.get("grok_override") else "  [agrees with RL]"
            print(f"  Grok 4.2   : P{gp}  ({_PRESET_NAMES.get(gp, '?')}){override_tag}")
            if r.get("grok_override") and r.get("grok_override_reason"):
                print(f"               reason: {r['grok_override_reason']}")
        if r.get("grok_reasoning"):
            print(f"               reasoning: {r['grok_reasoning']}")
    else:
        print(f"  Grok 4.2   : (skipped -- --rl-only or XAI_API_KEY not set)")

    if chosen is not None:
        print(f"  -> Chosen  : P{chosen}  (by {r.get('chosen_by', '?')})")

    if op is not None:
        rewards = r.get("rewards", [])
        reward_str = "  ".join(f"P{i}:{rewards[i]:.4f}" for i in range(len(rewards)))
        print(f"  Oracle     : P{op}  ({_PRESET_NAMES[op]})")
        print(f"  Rewards    : {reward_str}")
    else:
        print("  Oracle     : (no data)")

    print(f"  Verdict    : {_VERDICT_SYM.get(verdict, verdict)}")


def _print_summary(results: list[dict], rl_only: bool, grok_only: bool = False) -> None:
    if rl_only:
        mode = "RL-only"
    elif grok_only:
        mode = "Grok-only (standalone baseline)"
    else:
        mode = "RL + Grok 4.2"
    sep = "#" * 72
    print(f"\n{sep}")
    print(f"  SUMMARY  [{mode}]")
    print(sep)
    print(f"  {'Article':<38} {'Split':<6} {'RL':>3}  {'Grok':>4}  {'Chosen':>6}  {'Oracle':>6}  Verdict")
    print(f"  {'-'*68}")

    counts: dict[str, int] = {}
    for r in results:
        rl_p = r.get("rl_preset")
        gp = r.get("grok_preset")
        chosen = r.get("chosen_preset")
        op = r.get("oracle_preset")
        v = r.get("verdict", "ERROR")
        counts[v] = counts.get(v, 0) + 1
        rl_str = f"P{rl_p}" if rl_p is not None else "-"
        gp_str = f"P{gp}" if gp is not None else "-"
        ch_str = f"P{chosen}" if chosen is not None else "?"
        op_str = f"P{op}" if op is not None else "?"
        print(f"  {r['article']:<38} {r.get('split','?'):<6} {rl_str:>3}  {gp_str:>4}  {ch_str:>6}  →  {op_str:<4}  {v}")

    total = len(results)
    exact = counts.get("EXACT", 0)
    near = counts.get("NEAR", 0)
    miss = counts.get("MISS", 0)
    print(
        f"\n  Overall  ({total} articles): "
        f"exact={exact}  near={near}  miss={miss}"
    )

    test_results = [
        r for r in results
        if r.get("split") == "TEST" and r.get("verdict") not in ("NO_ORACLE", "ERROR")
    ]
    if test_results:
        t_exact = sum(1 for r in test_results if r["verdict"] == "EXACT")
        t_near = sum(1 for r in test_results if r["verdict"] in ("EXACT", "NEAR"))
        n = len(test_results)
        print(f"  TEST accuracy (exact):      {t_exact}/{n} = {100*t_exact//n}%")
        print(f"  TEST accuracy (exact+near): {t_near}/{n} = {100*t_near//n}%")


def _save_results(results: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for r in results:
        name = r["article"]
        path = out_dir / f"{name}.json"
        path.write_text(json.dumps(r, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"  Saved: {path}")
    summary_path = out_dir / "_summary.json"
    summary_path.write_text(
        json.dumps({"results": results}, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print(f"  Saved: {summary_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Test predict_exploration_preset via direct MCP tool call. "
            "No LLM orchestration layer -- the tool makes the final decision internally."
        )
    )
    parser.add_argument("--all", action="store_true", help="Run all articles (train + test)")
    parser.add_argument(
        "--articles", type=str,
        help="Comma-separated article names, e.g. 02_workflows_vs_agents,09_RAG",
    )
    parser.add_argument(
        "--rl-only", action="store_true",
        help="Evaluate rl_recommendation.preset only (skip Grok 4.2 stage)",
    )
    parser.add_argument(
        "--grok-only", action="store_true",
        help="Grok 4.2 standalone baseline: no RL signals, Grok decides from guideline + gap profile only",
    )
    parser.add_argument("--save-json", action="store_true", help="Save per-article JSON results")
    args = parser.parse_args()

    if args.rl_only and args.grok_only:
        print("ERROR: --rl-only and --grok-only are mutually exclusive.")
        return

    if args.articles:
        article_list = [a.strip() for a in args.articles.split(",")]
    elif args.all:
        article_list = _ALL_ARTICLES
    else:
        article_list = _DEFAULT_TEST_ARTICLES

    rl_only = args.rl_only
    grok_only = args.grok_only
    if rl_only:
        mode = "RL-only (--rl-only)"
    elif grok_only:
        mode = "Grok-only standalone (--grok-only)"
    else:
        mode = "RL + Grok 4.2"

    print(f"\nPreset Planner Test")
    print(f"  Mode       : {mode}")
    print(f"  Articles   : {article_list}")

    async with app.run():
        agent = Agent(
            name="research_agent",
            instruction="",  # no LLM loop -- direct tool calls only
            server_names=["research_agent"],
        )

        async with agent:
            all_tools, _, _ = await get_capabilities_from_mcp_client(agent)
            tool_names = [t.name for t in all_tools]
            if "predict_exploration_preset" not in tool_names:
                print(
                    "ERROR: predict_exploration_preset tool not found on the MCP server.\n"
                    "Make sure the server is up to date and the tool is registered."
                )
                return

            print(f"  Tool       : predict_exploration_preset (direct call, no agent loop)\n")

            results = []
            for article in article_list:
                split = "TRAIN" if article in _TRAIN_ARTICLES else "TEST"
                print(f"\n{'='*72}")
                print(f"  Article: {article}  [{split}]")
                print("=" * 72)

                result = await run_article(article, agent, rl_only, grok_only)
                results.append(result)
                _print_article_result(result)

    _print_summary(results, rl_only, grok_only)

    if args.save_json:
        out_dir = _AGENT_DIR / "grok_planner_test_results"
        _save_results(results, out_dir)


if __name__ == "__main__":
    asyncio.run(main())
