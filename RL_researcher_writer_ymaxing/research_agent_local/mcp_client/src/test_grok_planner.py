"""
End-to-end test: Grok's exploration planning decisions via the MCP tool.

For each article the script:
  1. Starts the MCP server (stdio transport, same as batch_runner).
  2. Asks Grok to call `predict_exploration_preset` for the article's
     research directory (rl_training_data/bases/<article>/), which already
     contains a pre-computed exploitation_digest.md.
  3. Captures Grok's chosen preset from its final JSON response.
  4. Computes the oracle preset from the offline reward data.
  5. Prints a hit/miss comparison and summary table.

This isolates step 3.4 of the research workflow (RL meta-reasoner planning)
without running the expensive scraping / writing steps.

Usage (from research_agent_local/):

  # Test-set articles only (default)
  uv run python -m mcp_client.src.test_grok_planner

  # All articles (train + test)
  uv run python -m mcp_client.src.test_grok_planner --all

  # Specific articles
  uv run python -m mcp_client.src.test_grok_planner --articles 02_workflows_vs_agents,09_RAG

  # Save per-article JSON results
  uv run python -m mcp_client.src.test_grok_planner --save-json

  # Disable LLM thinking (faster, cheaper)
  uv run python -m mcp_client.src.test_grok_planner --no-thinking
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import math
import re
import sys
from pathlib import Path

from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.config import get_settings as get_mcp_settings

from .settings import settings
from .utils.handle_agent_loop_utils import handle_agent_loop, make_user_message
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
# System instruction for Grok
# ---------------------------------------------------------------------------
_SYSTEM_INSTRUCTION = (
    "You are a research planning assistant. Your ONLY task is to call "
    "predict_exploration_preset for a given research directory, then decide "
    "which exploration preset (0–5) to use for that article.\n\n"
    "Preset meanings:\n"
    "  P0 = no exploration (exploitation only)\n"
    "  P1 = 1 exploration round, balanced breadth/depth\n"
    "  P2 = 2 rounds: balanced then depth\n"
    "  P3 = 2 rounds: depth then breadth\n"
    "  P4 = 3 rounds: balanced → depth → breadth\n"
    "  P5 = 3 rounds: depth → breadth → depth\n\n"
    "After calling the tool and reviewing its output, end your response with "
    "exactly one JSON line:\n"
    '{"chosen_preset": N, "reasoning": "one-sentence explanation"}\n\n'
    "Do NOT call any other tools. Do NOT run any research steps."
)


def _make_article_prompt(research_dir: Path) -> str:
    return (
        f"Research directory: {research_dir}\n\n"
        "The exploitation phase for this article is already complete.\n"
        "Please:\n"
        "  1. Call predict_exploration_preset with the research directory above.\n"
        "  2. Read the tool output carefully.\n"
        "  3. Decide which exploration preset (0–5) to use, following the "
        "tool's guidance unless you have a strong reason to override it.\n\n"
        "End your final response with this exact JSON on its own line:\n"
        '{"chosen_preset": N, "reasoning": "one sentence"}'
    )


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
# Response parsing
# ---------------------------------------------------------------------------
def _parse_chosen_preset(text: str) -> int | None:
    """Extract chosen_preset integer from Grok's JSON decision line."""
    m = re.search(r'"chosen_preset"\s*:\s*([0-5])', text)
    if m:
        return int(m.group(1))
    return None


def _extract_final_text(conversation_history: list) -> str:
    """Return the text content of the last assistant message in history."""
    for msg in reversed(conversation_history):
        if isinstance(msg, dict) and msg.get("role") == "assistant":
            return msg.get("content") or ""
    return ""


# ---------------------------------------------------------------------------
# Per-article runner
# ---------------------------------------------------------------------------
async def run_article(
    article: str,
    agent: Agent,
    tools: list,
    thinking_enabled: bool,
) -> dict:
    research_dir = _BASES_DIR / article
    if not research_dir.exists():
        return {"article": article, "error": f"Directory not found: {research_dir}"}

    # Build conversation history with system instruction + per-article prompt
    conversation_history: list = [
        {"role": "system", "content": _SYSTEM_INSTRUCTION},
        make_user_message(_make_article_prompt(research_dir)),
    ]

    await handle_agent_loop(conversation_history, tools, agent, thinking_enabled)

    final_text = _extract_final_text(conversation_history)
    grok_preset = _parse_chosen_preset(final_text)

    try:
        oracle_preset, rewards = _compute_oracle(article)
    except FileNotFoundError as exc:
        return {
            "article": article,
            "split": "TRAIN" if article in _TRAIN_ARTICLES else "TEST",
            "grok_preset": grok_preset,
            "oracle_preset": None,
            "verdict": "NO_ORACLE",
            "grok_response": final_text,
            "error": str(exc),
        }

    if grok_preset is None:
        verdict = "PARSE_FAIL"
    elif grok_preset == oracle_preset:
        verdict = "EXACT"
    elif abs(grok_preset - oracle_preset) == 1:
        verdict = "NEAR"
    else:
        verdict = "MISS"

    return {
        "article": article,
        "split": "TRAIN" if article in _TRAIN_ARTICLES else "TEST",
        "grok_preset": grok_preset,
        "oracle_preset": oracle_preset,
        "rewards": [round(r, 4) for r in rewards],
        "verdict": verdict,
        "grok_response": final_text,
    }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
_VERDICT_SYM = {
    "EXACT": "✓  EXACT HIT",
    "NEAR": "~  NEAR MISS  (±1 preset)",
    "MISS": "✗  MISS",
    "PARSE_FAIL": "?  PARSE FAILED",
    "NO_ORACLE": "?  NO ORACLE DATA",
}


def _print_article_result(r: dict) -> None:
    print()
    if "error" in r and r.get("verdict") not in ("PARSE_FAIL", "NO_ORACLE"):
        print(f"  ERROR: {r['error']}")
        return

    gp = r.get("grok_preset")
    op = r.get("oracle_preset")
    verdict = r.get("verdict", "?")

    if gp is not None:
        print(f"  Grok chose : P{gp}  ({_PRESET_NAMES.get(gp, '?')})")
    else:
        print("  Grok chose : (could not parse preset from response)")

    if op is not None:
        rewards = r.get("rewards", [])
        reward_str = "  ".join(
            f"P{i}:{rewards[i]:.4f}" for i in range(len(rewards))
        )
        print(f"  Oracle     : P{op}  ({_PRESET_NAMES[op]})")
        print(f"  Rewards    : {reward_str}")
    else:
        print("  Oracle     : (no data)")

    print(f"  Verdict    : {_VERDICT_SYM.get(verdict, verdict)}")

    tail = (r.get("grok_response") or "")[-600:]
    if tail:
        indented = tail.replace("\n", "\n    ")
        print(f"\n  Grok response (tail):\n    {indented}")


def _print_summary(results: list[dict]) -> None:
    sep = "#" * 72
    print(f"\n{sep}")
    print("  SUMMARY")
    print(sep)
    print(f"  {'Article':<38} {'Split':<6} {'Grok':>4}  {'Oracle':>6}  Verdict")
    print(f"  {'-'*65}")

    counts: dict[str, int] = {}
    for r in results:
        gp = r.get("grok_preset")
        op = r.get("oracle_preset")
        v = r.get("verdict", "ERROR")
        counts[v] = counts.get(v, 0) + 1
        gp_str = f"P{gp}" if gp is not None else "?"
        op_str = f"P{op}" if op is not None else "?"
        print(f"  {r['article']:<38} {r.get('split','?'):<6} {gp_str:>4}  →  {op_str:<4}  {v}")

    total = len(results)
    exact = counts.get("EXACT", 0)
    near = counts.get("NEAR", 0)
    miss = counts.get("MISS", 0)
    pfail = counts.get("PARSE_FAIL", 0)
    print(
        f"\n  Overall  ({total} articles): "
        f"exact={exact}  near={near}  miss={miss}  parse_fail={pfail}"
    )

    test_results = [
        r for r in results
        if r.get("split") == "TEST" and r.get("verdict") not in ("NO_ORACLE", "PARSE_FAIL", "ERROR")
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
        description="Test Grok's exploration planning decisions via the MCP tool."
    )
    parser.add_argument("--all", action="store_true", help="Run all articles (train + test)")
    parser.add_argument(
        "--articles", type=str,
        help="Comma-separated article names, e.g. 02_workflows_vs_agents,09_RAG",
    )
    parser.add_argument("--no-thinking", action="store_true", help="Disable LLM extended thinking")
    parser.add_argument("--save-json", action="store_true", help="Save per-article JSON results")
    args = parser.parse_args()

    if args.articles:
        article_list = [a.strip() for a in args.articles.split(",")]
    elif args.all:
        article_list = _ALL_ARTICLES
    else:
        article_list = _DEFAULT_TEST_ARTICLES

    thinking_enabled = not args.no_thinking

    print(f"\nGrok Planner Test")
    print(f"  Model      : {settings.model_id}")
    print(f"  Articles   : {article_list}")
    print(f"  Thinking   : {'ON' if thinking_enabled else 'OFF'}")

    async with app.run():
        agent = Agent(
            name="research_agent",
            instruction=_SYSTEM_INSTRUCTION,
            server_names=["research_agent"],
        )

        async with agent:
            all_tools, _, _ = await get_capabilities_from_mcp_client(agent)

            # Restrict to only the RL meta-reasoner tool — no accidental scraping
            tools = [t for t in all_tools if t.name == "predict_exploration_preset"]
            if not tools:
                print(
                    "ERROR: predict_exploration_preset tool not found on the MCP server.\n"
                    "Make sure the server is up to date and the tool is registered."
                )
                return

            print(f"  Tool       : {tools[0].name} (only tool exposed to Grok)\n")

            results = []
            for article in article_list:
                split = "TRAIN" if article in _TRAIN_ARTICLES else "TEST"
                print(f"\n{'='*72}")
                print(f"  Article: {article}  [{split}]")
                print("=" * 72)

                result = await run_article(article, agent, tools, thinking_enabled)
                results.append(result)
                _print_article_result(result)

    _print_summary(results)

    if args.save_json:
        out_dir = _AGENT_DIR / "grok_planner_test_results"
        _save_results(results, out_dir)


if __name__ == "__main__":
    asyncio.run(main())
