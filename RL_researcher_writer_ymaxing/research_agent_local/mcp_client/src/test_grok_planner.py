"""
Preset planner test: predict_exploration_preset tool (direct MCP call).

The tool makes the final planning decision internally via two stages:
  Stage 1 — Qwen3-4B RL model  -> rl_recommendation
  Stage 2 — Grok 4.2 reasoning -> grok_recommendation

This test calls the tool directly via the MCP protocol, bypassing any LLM
agent loop.  The mcp-agent is still used to manage the server subprocess and
expose the MCP transport, but no orchestration LLM is involved.

Corpus
------
  24 article-variants: 8 lessons × 3 guideline variants
    (var_minimal, var_standard, var_demanding)

  All 8 lessons are currently in the training set.
  No held-out test set exists yet.

Oracle
------
  Read from <bases_dir>/<variant>/article_oracle.json  (version 2).
  Key field: oracle_arm_idx  (0=skip, 1=light, 2=standard, 3=deep).

Modes
-----
  default          — reads grok_recommendation.preset (full pipeline: RL → Grok 4.2)
  --rl-only        — reads rl_recommendation.preset   (Qwen3-4B only, no Grok 4.2)
  --rl-guards-only — RL aggregate + deterministic policy guards (forbidden→skip,
                     required→≥light), no Grok 4.2. The benchmark the LLM planner
                     must beat.
  --grok-only      — reads grok_recommendation.preset (Grok 4.2 standalone, no RL signals)
                     Use as a baseline to measure the RL model's marginal contribution.

Reward-regret
-------------
  Reported alongside exact/near/miss. regret = R_w[oracle] − R_w[chosen].
  Forbidden-policy articles are EXCLUDED from the regret aggregate: their P1/P2/P3
  rewards are tainted (generated with the very exploration the policy forbids) and
  the oracle is policy-forced to P0.

Usage (from research_agent_local/)
-----------------------------------
  # Test-lesson variants only (default, full pipeline)
  uv run python -m mcp_client.src.test_grok_planner

  # RL model only — faster, no Grok 4.2 call
  uv run python -m mcp_client.src.test_grok_planner --rl-only

  # Grok 4.2 standalone baseline — no RL section signals
  uv run python -m mcp_client.src.test_grok_planner --grok-only

  # All 24 variants (default, same as no flag)
  uv run python -m mcp_client.src.test_grok_planner

  # Only demanding variants
  uv run python -m mcp_client.src.test_grok_planner --variants demanding

  # Specific full variant names
  uv run python -m mcp_client.src.test_grok_planner --articles 02_workflows_vs_agents__var_demanding,09_RAG__var_minimal

  # Bare lesson names expand to all 3 variants
  uv run python -m mcp_client.src.test_grok_planner --articles 02_workflows_vs_agents,09_RAG

  # Save per-variant JSON results
  uv run python -m mcp_client.src.test_grok_planner --save-json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
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
_CLIENT_DIR = _THIS_DIR.parent                    # mcp_client/
_AGENT_DIR = _CLIENT_DIR.parent                   # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent                    # RL_researcher_writer_ymaxing/
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"

# ---------------------------------------------------------------------------
# 4-preset vocabulary (mirrors _rl_preset.py)
# ---------------------------------------------------------------------------
_NUM_PRESETS = 4
_PRESET_NAMES = {0: "skip", 1: "light", 2: "standard", 3: "deep"}
_VARIANTS = ("var_minimal", "var_standard", "var_demanding")

# ---------------------------------------------------------------------------
# Corpus: 8 lessons × 3 variants = 24 article-variants
# All 8 lessons are in the training set.  No held-out test set exists yet.
# ---------------------------------------------------------------------------
_TRAIN_LESSONS = {
    "02_workflows_vs_agents",
    "03_context_engineering",
    "05_workflow_patterns",
    "06_tools",
    "08_react_practice",
    "09_RAG",
    "10_memory_knowledge_access",
    "11_multimodal",
}
_ALL_LESSONS = sorted(_TRAIN_LESSONS)

# Full 24-variant list (variant ordering: minimal → standard → demanding)
_ALL_VARIANTS: list[str] = [
    f"{lesson}__{var}"
    for lesson in _ALL_LESSONS
    for var in _VARIANTS
]


def _lesson_of(variant_name: str) -> str:
    """Return the base lesson name from a full variant name.

    ``"02_workflows_vs_agents__var_demanding"`` → ``"02_workflows_vs_agents"``
    """
    return variant_name.split("__var_")[0]


def _expand_articles(names: list[str]) -> list[str]:
    """Expand bare lesson names to all 3 variants; pass through full variant names.

    ``["02_workflows_vs_agents", "09_RAG__var_minimal"]``
    → ``["02_workflows_vs_agents__var_minimal",
          "02_workflows_vs_agents__var_standard",
          "02_workflows_vs_agents__var_demanding",
          "09_RAG__var_minimal"]``
    """
    out: list[str] = []
    for name in names:
        if "__var_" in name:
            out.append(name)
        else:
            for var in _VARIANTS:
                out.append(f"{name}__{var}")
    return out


# ---------------------------------------------------------------------------
# MCP app (created once, shared across all variants)
# ---------------------------------------------------------------------------
_mcp_settings = get_mcp_settings(str(Path(__file__).parent / "mcp_agent.config.yaml"))
_mcp_settings.mcp.servers["research_agent"].args = [
    "--directory", str(settings.server_main_path),
    "run", "python", "-m", "src.server", "--transport", "stdio",
]
app = MCPApp(name="GrokPlannerTest", settings=_mcp_settings)


# ---------------------------------------------------------------------------
# Oracle: read from article_oracle.json  (version 2)
# ---------------------------------------------------------------------------
def _read_oracle(variant_name: str) -> tuple[int, list[float]]:
    """Return (oracle_arm_idx, r_w_rewards_list[0..3]) from article_oracle.json.

    Raises FileNotFoundError when the file is absent.
    """
    oracle_path = _BASES_DIR / variant_name / "article_oracle.json"
    if not oracle_path.exists():
        raise FileNotFoundError(f"Missing article_oracle.json: {oracle_path}")
    data = json.loads(oracle_path.read_text(encoding="utf-8"))
    return int(data["oracle_arm_idx"]), data["r_w_rewards_list"]


def _apply_policy_guards(preset: int, policy: str) -> int:
    """Deterministic hard-constraint clamp (mirrors the server-side guard).

    forbidden -> P0 skip   ·   required -> at least P1 light   ·   allowed -> unchanged.
    """
    if policy == "forbidden":
        return 0
    if policy == "required":
        return max(1, preset)
    return preset


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
# Per-variant runner
# ---------------------------------------------------------------------------
async def run_variant(
    variant: str,
    agent: Agent,
    rl_only: bool,
    grok_only: bool = False,
    rl_guards_only: bool = False,
) -> dict:
    research_dir = _BASES_DIR / variant
    if not research_dir.exists():
        return {"variant": variant, "error": f"Directory not found: {research_dir}"}

    lesson = _lesson_of(variant)
    split = "TRAIN"  # all lessons are currently in the training set

    # --- Direct MCP tool call (no LLM agent loop) ---
    tool_args: dict = {"research_directory": str(research_dir)}
    if grok_only:
        tool_args["grok_only"] = True
    if rl_only or rl_guards_only:
        # Both modes evaluate the RL stage only; skip the Grok call server-side.
        tool_args["rl_only"] = True
    try:
        tool_result = await agent.call_tool("predict_exploration_preset", tool_args)
        data = _parse_tool_result(tool_result)
    except Exception as exc:
        return {"variant": variant, "lesson": lesson, "split": split, "error": str(exc)}

    if data.get("status") == "error":
        return {
            "variant": variant, "lesson": lesson, "split": split,
            "error": data.get("message", "unknown error"),
        }

    rl = data.get("rl_recommendation")     # None when grok_only=True
    grok = data.get("grok_recommendation") # None when rl_only / XAI unset / call failed

    # External-evidence policy (drives guards + regret accounting). Always present
    # in article_evidence regardless of mode.
    evidence = data.get("article_evidence") or {}
    policy = (evidence.get("guideline_context") or {}).get(
        "external_evidence_policy", "allowed"
    )

    # Determine which preset to evaluate
    if grok_only:
        if grok is None:
            return {
                "variant": variant, "lesson": lesson, "split": split,
                "error": "Grok standalone call failed or XAI_API_KEY not set",
            }
        chosen_preset = grok["preset"]
        chosen_by = "Grok-only"
    elif rl_guards_only:
        if rl is None:
            return {
                "variant": variant, "lesson": lesson, "split": split,
                "error": "rl_recommendation missing (rl_guards_only)",
            }
        chosen_preset = _apply_policy_guards(rl["preset"], policy)
        chosen_by = "RL+guards"
    elif rl_only or grok is None:
        chosen_preset = rl["preset"]
        chosen_by = "RL"
    else:
        chosen_preset = grok["preset"]
        chosen_by = "Grok4.2"

    # --- Oracle ---
    try:
        oracle_preset, r_w_rewards = _read_oracle(variant)
    except FileNotFoundError as exc:
        return {
            "variant": variant,
            "lesson": lesson,
            "split": split,
            "policy": policy,
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

    # Reward-regret: how much reward was left on the table vs. oracle arm.
    # regret = r_w[oracle] - r_w[chosen]  (0.0 on exact hit, >0 on error)
    regret = round(
        r_w_rewards[oracle_preset] - r_w_rewards[chosen_preset], 4
    ) if len(r_w_rewards) > max(oracle_preset, chosen_preset) else None

    # Forbidden-policy articles have TAINTED P1/P2/P3 rewards: those arms were
    # generated using the very exploration the policy forbids, so their R_w is not
    # comparable and the oracle is policy-forced to P0. Exclude them from the
    # aggregate regret (regret_counted=None) so the metric is not contaminated.
    regret_counted = None if policy == "forbidden" else regret

    return {
        "variant": variant,
        "lesson": lesson,
        "split": split,
        "policy": policy,
        "rl_preset": rl["preset"] if rl else None,
        "grok_preset": grok["preset"] if grok else None,
        "chosen_preset": chosen_preset,
        "chosen_by": chosen_by,
        "oracle_preset": oracle_preset,
        "oracle_name": _PRESET_NAMES.get(oracle_preset, "?"),
        "r_w_rewards": [round(r, 4) for r in r_w_rewards],
        "verdict": verdict,
        "regret": regret,
        "regret_counted": regret_counted,
        "entropy_bits": rl["entropy_bits"] if rl else None,
        "confidence": rl["confidence"] if rl else None,
        "floor_applied": rl["floor_correction_applied"] if rl else None,
        "grok_override": grok.get("override") if grok else None,
        "grok_reasoning": grok.get("reasoning") if grok else None,
        "grok_override_reason": grok.get("override_reason") if grok else None,
        "grok_decision_drivers": grok.get("decision_drivers") if grok else None,
        "grok_risk_flags": grok.get("risk_flags") if grok else None,
    }


# ---------------------------------------------------------------------------
# Display helpers
# ---------------------------------------------------------------------------
_VERDICT_SYM = {
    "EXACT":     "✓  EXACT HIT",
    "NEAR":      "~  NEAR MISS  (±1 preset)",
    "MISS":      "✗  MISS",
    "NO_ORACLE": "?  NO ORACLE DATA",
}


def _print_variant_result(r: dict) -> None:
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
    is_guards = (chosen_by == "RL+guards")

    pol = r.get("policy")
    if pol:
        print(f"  Policy     : {pol}")

    if rl_p is not None:
        floor_tag = "  [floor applied]" if floor else ""
        rl_name = _PRESET_NAMES.get(rl_p, "?")
        print(f"  RL model   : P{rl_p} {rl_name:<8}  conf={conf:.0%}  H={entropy:.2f}bits{floor_tag}")
    elif is_grok_only:
        print(f"  RL model   : (skipped — --grok-only baseline)")

    if is_guards:
        print(f"  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)")
    elif gp is not None:
        gp_name = _PRESET_NAMES.get(gp, "?")
        if is_grok_only:
            print(f"  Grok 4.2   : P{gp} {gp_name:<8}  [standalone, no RL input]")
        else:
            override_tag = "  [OVERRIDE]" if r.get("grok_override") else "  [agrees with RL]"
            print(f"  Grok 4.2   : P{gp} {gp_name:<8}{override_tag}")
            if r.get("grok_override") and r.get("grok_override_reason"):
                print(f"               reason: {r['grok_override_reason']}")
        if r.get("grok_reasoning"):
            print(f"               reasoning: {r['grok_reasoning']}")
        if r.get("grok_decision_drivers"):
            print(f"               drivers: {', '.join(r['grok_decision_drivers'])}")
    else:
        print(f"  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)")

    if chosen is not None:
        print(f"  -> Chosen  : P{chosen} {_PRESET_NAMES.get(chosen, '?')}  (by {r.get('chosen_by', '?')})")

    if op is not None:
        rewards = r.get("r_w_rewards", [])
        reward_str = "  ".join(
            f"P{i}/{_PRESET_NAMES[i]}:{rewards[i]:.3f}" for i in range(len(rewards))
        )
        print(f"  Oracle     : P{op} {_PRESET_NAMES.get(op, '?')}")
        print(f"  R_w        : {reward_str}")
        regret = r.get("regret")
        if regret is not None:
            if pol == "forbidden":
                print(
                    f"  Regret     : {regret:+.4f}  "
                    f"(not counted — forbidden policy, P1+ rewards tainted)"
                )
            else:
                regret_tag = "" if regret == 0.0 else f"  (regret {regret:+.4f})"
                print(f"  Regret     : {regret:.4f}{regret_tag}")
    else:
        print("  Oracle     : (no data)")

    print(f"  Verdict    : {_VERDICT_SYM.get(verdict, verdict)}")


def _print_summary(
    results: list[dict],
    rl_only: bool,
    grok_only: bool = False,
    rl_guards_only: bool = False,
) -> None:
    if rl_only:
        mode = "RL-only"
    elif rl_guards_only:
        mode = "RL + deterministic policy guards"
    elif grok_only:
        mode = "Grok-only (standalone baseline)"
    else:
        mode = "RL + Grok 4.2"
    sep = "#" * 80
    print(f"\n{sep}")
    print(f"  SUMMARY  [{mode}]")
    print(sep)
    header = f"  {'Variant':<46} {'Spl':>4}  {'RL':>4}  {'Grok':>4}  {'Chsn':>4}  → {'Orcl':<4}  Verdict"
    print(header)
    print(f"  {'-'*76}")

    counts: dict[str, int] = {}
    for r in results:
        rl_p = r.get("rl_preset")
        gp = r.get("grok_preset")
        chosen = r.get("chosen_preset")
        op = r.get("oracle_preset")
        v = r.get("verdict", "ERROR")
        counts[v] = counts.get(v, 0) + 1
        rl_str = f"P{rl_p}" if rl_p is not None else "—"
        gp_str = f"P{gp}" if gp is not None else "—"
        ch_str = f"P{chosen}" if chosen is not None else "?"
        op_str = f"P{op}" if op is not None else "?"
        sym = {"EXACT": "✓", "NEAR": "~", "MISS": "✗"}.get(v, "?")
        print(
            f"  {r['variant']:<46} {r.get('split','?'):>4}  "
            f"{rl_str:>4}  {gp_str:>4}  {ch_str:>4}  → {op_str:<4}  {sym} {v}"
        )

    total = len(results)
    exact = counts.get("EXACT", 0)
    near = counts.get("NEAR", 0)
    miss = counts.get("MISS", 0)
    error = counts.get("ERROR", 0) + counts.get("NO_ORACLE", 0)
    # Regret aggregate excludes forbidden-policy articles (tainted rewards).
    counted = [r["regret_counted"] for r in results if r.get("regret_counted") is not None]
    n_forbidden = sum(1 for r in results if r.get("policy") == "forbidden")
    mean_regret = sum(counted) / len(counted) if counted else 0.0
    max_regret = max(counted) if counted else 0.0
    print(f"\n  Total {total} variants:  exact={exact}  near={near}  miss={miss}  no-oracle/error={error}")
    print(
        f"  Reward-regret (allowed/required only, n={len(counted)}; "
        f"{n_forbidden} forbidden excluded):  mean={mean_regret:.4f}  max={max_regret:.4f}"
    )

    # Per-variant-type breakdown (minimal / standard / demanding)
    for var_type in _VARIANTS:
        vt_r = [
            r for r in results
            if var_type in r.get("variant", "")
            and r.get("verdict") not in ("NO_ORACLE", "ERROR", None)
            and "error" not in r
        ]
        if not vt_r:
            continue
        n = len(vt_r)
        s_exact = sum(1 for r in vt_r if r["verdict"] == "EXACT")
        s_near = sum(1 for r in vt_r if r["verdict"] in ("EXACT", "NEAR"))
        vt_regrets = [r["regret_counted"] for r in vt_r if r.get("regret_counted") is not None]
        if vt_regrets:
            vt_mean = sum(vt_regrets) / len(vt_regrets)
            vt_max = max(vt_regrets)
            regret_str = f"regret mean={vt_mean:.4f} max={vt_max:.4f}"
        else:
            regret_str = "regret n/a (all policy-forced)"
        print(
            f"  {var_type:<16} ({n:2d} variants):  "
            f"exact {s_exact}/{n}   exact+near {s_near}/{n}   "
            f"{regret_str}"
        )


def _save_results(results: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for r in results:
        name = r["variant"]
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
            "Evaluates all 24 article-variants (8 lessons × 3 guideline variants) "
            "against the article_oracle.json oracle. "
            "No LLM orchestration layer — the tool makes the final decision internally."
        )
    )
    parser.add_argument(
        "--all", action="store_true",
        help="(No-op: all 24 variants are always run by default. Kept for future use.)",
    )
    parser.add_argument(
        "--articles", type=str,
        help=(
            "Comma-separated variant names or bare lesson names. "
            "Bare lesson names expand to all 3 variants. "
            "E.g.: 02_workflows_vs_agents,09_RAG__var_minimal"
        ),
    )
    parser.add_argument(
        "--variants", type=str, default=None,
        metavar="VARIANT_TYPE",
        help=(
            "Restrict to a single variant type: minimal, standard, or demanding. "
            "Applied AFTER --all / --articles expansion."
        ),
    )
    parser.add_argument(
        "--rl-only", action="store_true",
        help="Evaluate rl_recommendation.preset only (skip Grok 4.2 stage).",
    )
    parser.add_argument(
        "--rl-guards-only", action="store_true",
        help=(
            "Ablation: RL aggregate + deterministic policy guards "
            "(forbidden→skip, required→≥light), NO Grok 4.2. "
            "The benchmark the LLM planner must beat."
        ),
    )
    parser.add_argument(
        "--grok-only", action="store_true",
        help=(
            "Grok 4.2 standalone baseline: no RL signals. "
            "Measures Grok's marginal contribution vs. the RL model."
        ),
    )
    parser.add_argument("--save-json", action="store_true", help="Save per-variant JSON results.")
    args = parser.parse_args()

    n_modes = sum([args.rl_only, args.grok_only, args.rl_guards_only])
    if n_modes > 1:
        print("ERROR: --rl-only, --rl-guards-only and --grok-only are mutually exclusive.")
        return

    # Build variant list
    if args.articles:
        variant_list = _expand_articles([a.strip() for a in args.articles.split(",")])
    else:
        variant_list = list(_ALL_VARIANTS)  # --all is implied; no separate test set yet

    # Apply --variants filter
    if args.variants:
        vt = args.variants.strip().lstrip("var_")  # normalise "var_demanding" → "demanding"
        variant_list = [v for v in variant_list if f"var_{vt}" in v]
        if not variant_list:
            print(f"ERROR: --variants '{args.variants}' matched no variants.")
            return

    rl_only = args.rl_only
    grok_only = args.grok_only
    rl_guards_only = args.rl_guards_only
    if rl_only:
        mode = "RL-only (--rl-only)"
    elif rl_guards_only:
        mode = "RL + deterministic policy guards (--rl-guards-only)"
    elif grok_only:
        mode = "Grok-only standalone (--grok-only)"
    else:
        mode = "RL + Grok 4.2"

    print(f"\nPreset Planner Test  ({len(variant_list)} variants)")
    print(f"  Mode     : {mode}")
    print(f"  Variants : {variant_list}")

    async with app.run():
        agent = Agent(
            name="research_agent",
            instruction="",  # no LLM loop — direct tool calls only
            server_names=["research_agent"],
        )

        async with agent:
            all_tools, _, _ = await get_capabilities_from_mcp_client(agent)
            tool_names = [t.name for t in all_tools]
            # mcp_agent namespaces tool names as "{server_name}_{tool_name}",
            # so check for both the bare name and the namespaced variant.
            _TOOL = "predict_exploration_preset"
            if not any(n == _TOOL or n.endswith(f"_{_TOOL}") for n in tool_names):
                print(
                    "ERROR: predict_exploration_preset tool not found on the MCP server.\n"
                    "Make sure the server is up to date and the tool is registered."
                )
                return

            print(f"  Tool     : predict_exploration_preset (direct call, no agent loop)\n")

            results = []
            for variant in variant_list:
                lesson = _lesson_of(variant)
                split = "TRAIN" if lesson in _TRAIN_LESSONS else "TEST"
                print(f"\n{'='*80}")
                print(f"  Variant : {variant}  [{split}]")
                print("=" * 80)

                result = await run_variant(variant, agent, rl_only, grok_only, rl_guards_only)
                results.append(result)
                _print_variant_result(result)

    _print_summary(results, rl_only, grok_only, rl_guards_only)

    if args.save_json:
        out_dir = _AGENT_DIR / "grok_planner_test_results"
        _save_results(results, out_dir)


if __name__ == "__main__":
    asyncio.run(main())
