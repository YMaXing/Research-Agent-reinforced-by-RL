"""
Preset planner test: predict_exploration_preset_eval (direct in-process call).

This is the EVAL-ONLY function (grok_only/rl_only ablation switches, the disabled-by-default
LLM-planner stage) -- NOT the production predict_exploration_preset MCP tool, which has neither
and is not exposed here at all. The function makes the final planning decision internally via
two stages:
  Stage 1 — Qwen3-4B RL model      -> rl_recommendation
  Stage 2 — LLM planner (currently Grok 4.2) -> llm_recommendation

This is a plain workflow script (like training/rl_data_generator.py) that imports and calls
predict_exploration_preset_eval() directly in-process — it does not start an MCP server or
go through the MCP protocol/agent loop at all.

Corpus
------
  Training: 24 article-variants — 8 lessons × 3 guideline variants
    (var_minimal, var_standard, var_demanding)
  Test:      16 no-variant held-out lessons (04, 07, 13, 14, 29, 31,
             Bird_Eye_Extreme, Dark_Dimension, Distinct_AI_Models,
             Earth_Oceans_Origin, Gravity_Entropy, HNSW,
             Insects_Consciousness, Space-Time_QECC, State_of_LLM_Reasoning,
             Understanding_Reasoning_LLMs).

Oracle
------          
  Read from <bases_dir>/<variant>/article_oracle.json  (version 2).
  Key field: oracle_arm_idx  (0=skip, 1=light, 2=standard, 3=deep).

Modes
-----
  default          — reads llm_recommendation.preset (full pipeline: RL → LLM planner
                     stage). NOTE: with predict_exploration_preset_eval's default
                     PRESET_PLANNER_SKIP_LLM=true, this is IDENTICAL to --rl-guards-only
                     (no LLM call; a deterministic policy guard only). Set
                     PRESET_PLANNER_SKIP_LLM=false in the environment to actually exercise
                     the LLM planner in this mode.
  --rl-only        — reads rl_recommendation.preset   (Qwen3-4B only, no LLM planner call)
  --rl-guards-only — RL aggregate + deterministic policy guards (forbidden→skip,
                     required→≥light, capped→≤light), no LLM planner call. The benchmark
                     the LLM planner must beat.
  --grok-only      — reads llm_recommendation.preset (LLM planner standalone, no RL signals;
                     always makes a real LLM call when XAI_API_KEY is set, regardless of
                     PRESET_PLANNER_SKIP_LLM)
                     Use as a baseline to measure the RL model's marginal contribution.

Reward-regret
-------------
  Reported alongside exact/near/miss. regret = R_w[oracle] − R_w[chosen].
  Forbidden-policy articles are EXCLUDED from the regret aggregate: their P1/P2/P3
  rewards are tainted (generated with the very exploration the policy forbids) and
  the oracle is policy-forced to P0.

Split reporting
---------------
  Results are split into TRAIN (24 variants) and TEST (16 no-variant held-outs).
  TEST articles are the primary metric; TRAIN is provided for reference.
  A 4×4 per-arm confusion matrix and majority/random baselines are printed for
  each split.

Usage (from research_agent_local/, requires the mcp_server venv)
------------------------------------------------------------------
  # All articles — train variants + test held-outs (default)
  uv run --project mcp_server python evaluation/test_grok_planner.py

  # Test held-outs only (all 16)
  uv run --project mcp_server python evaluation/test_grok_planner.py --test-only

  # Training variants only
  uv run --project mcp_server python evaluation/test_grok_planner.py --train-only

  # RL model only — faster, no LLM planner call
  uv run --project mcp_server python evaluation/test_grok_planner.py --rl-only

  # LLM planner standalone baseline (currently Grok 4.2) — no RL section signals
  uv run --project mcp_server python evaluation/test_grok_planner.py --grok-only

  # Only demanding training variants
  uv run --project mcp_server python evaluation/test_grok_planner.py --variants demanding

  # Specific articles (bare test slug → no expansion; bare train slug → 3 variants)
  uv run --project mcp_server python evaluation/test_grok_planner.py --articles 04_structured_outputs,09_RAG

  # Save per-variant JSON results (written next to the checkpoint that
  # produced them: <adapter_dir>/rl_only_results|rl_guard_results|
  # grok_only_results|rl_and_grok_results/, per RL_INFER_ADAPTER_DIR or the
  # current default checkpoint)
  uv run --project mcp_server python evaluation/test_grok_planner.py --save-json

  # Override which checkpoint the infer server loads, as a path relative to
  # rl_training_data/checkpoints/ (no need to edit _infer_config.py or export
  # RL_INFER_ADAPTER_DIR by hand) 
  For example, to test the run31_averaged_confidence/epoch_0109 checkpoint:
  uv run --project mcp_server python evaluation/test_grok_planner.py \
      --adapter-dir tasks/run31_averaged_confidence/epochs/epoch_0109 \
      --rl-guards-only --save-json

  # Or, using the research_agent_local/ root shim (mirrors rl_data_generator.py):
  uv run --project mcp_server python test_grok_planner.py --rl-only
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import sys as _sys
from pathlib import Path

from predict_exploration_preset_eval import predict_exploration_preset_eval

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_THIS_DIR = Path(__file__).resolve().parent       # evaluation/
_AGENT_DIR = _THIS_DIR.parent                     # research_agent_local/
_REPO_ROOT = _AGENT_DIR.parent                    # RL_researcher_writer_ymaxing/
# Reassigned in main() by --bases-dir to score a checkpoint against an
# alternate reward-formula experiment's own oracle labels/rewards -- both
# run_variant() and _read_oracle() below read this name unqualified, so the
# override propagates to both.
_BASES_DIR = _REPO_ROOT / "rl_training_data" / "bases"
_CHECKPOINTS_ROOT = _REPO_ROOT / "rl_training_data" / "checkpoints"

# _infer_config.py is stdlib-only (see its own docstring), so it's safe to
# import here too -- lets --save-json mirror ensure_infer_server()'s own
# checkpoint resolution (RL_INFER_ADAPTER_DIR env var, else the current
# default) instead of guessing, so results always land next to the
# checkpoint that actually served them.
_INFER_SERVICE_DIR = _AGENT_DIR / "rl_inference_service"
if str(_INFER_SERVICE_DIR) not in _sys.path:
    _sys.path.insert(0, str(_INFER_SERVICE_DIR))
from _infer_config import DEFAULT_ADAPTER_DIR as _DEFAULT_ADAPTER_DIR  # noqa: E402

# ---------------------------------------------------------------------------
# 4-preset vocabulary (mirrors _rl_preset.py)
# ---------------------------------------------------------------------------
_NUM_PRESETS = 4
_PRESET_NAMES = {0: "skip", 1: "light", 2: "standard", 3: "deep"}
_VARIANTS = ("var_minimal", "var_standard", "var_demanding")

# ---------------------------------------------------------------------------
# Corpus
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

# Held-out test lessons — no-variant (single research run, no __var_ suffix).
# Research dirs live in bases/<slug>/ (same root as training variants).
_TEST_LESSONS = {
    # Course lessons
    "04_structured_outputs",
    "07_reasoning_planning",
    "13_agent_framework",
    "14_agent_system_design",
    "29_evaluation_metrics",
    "31_CI",
    # External (non-course) standalone articles — no variant expansion.
    # Add new external test articles here as they are built.
    "Bird_Eye_Extreme",
    "Dark_Dimension",
    "Distinct_AI_Models",
    "Earth_Oceans_Origin",
    "Gravity_Entropy",
    "HNSW",
    "Insects_Consciousness",
    "Space-Time_QECC",
    "State_of_LLM_Reasoning",
    "Understanding_Reasoning_LLMs",
}

_ALL_LESSONS = sorted(_TRAIN_LESSONS)

# Full 24-variant list (variant ordering: minimal → standard → demanding)
_ALL_VARIANTS: list[str] = [
    f"{lesson}__{var}"
    for lesson in _ALL_LESSONS
    for var in _VARIANTS
]

# Sorted no-variant test article slugs
_TEST_ARTICLES: list[str] = sorted(_TEST_LESSONS)

# Combined default run: 24 training variants + 16 test articles
_ALL_ARTICLES: list[str] = _ALL_VARIANTS + _TEST_ARTICLES


def _lesson_of(variant_name: str) -> str:
    """Return the base lesson name from a full variant name.

    ``"02_workflows_vs_agents__var_demanding"`` → ``"02_workflows_vs_agents"``
    """
    return variant_name.split("__var_")[0]


def _expand_articles(names: list[str]) -> list[str]:
    """Expand bare lesson names to all 3 variants; pass no-variant test slugs through.

    Rules:
      - Name contains ``__var_``          → pass through (already a specific variant).
      - Name is in ``_TEST_LESSONS``       → pass through (no-variant held-out).
      - Otherwise (bare training lesson)   → expand to all 3 guideline variants.

    Examples::

        ["02_workflows_vs_agents", "04_structured_outputs", "09_RAG__var_minimal"]
        → ["02_workflows_vs_agents__var_minimal",
           "02_workflows_vs_agents__var_standard",
           "02_workflows_vs_agents__var_demanding",
           "04_structured_outputs",          # no expansion — test article
           "09_RAG__var_minimal"]
    """
    out: list[str] = []
    for name in names:
        if "__var_" in name:
            out.append(name)
        elif name in _TEST_LESSONS:
            out.append(name)  # no-variant test article — no expansion
        else:
            for var in _VARIANTS:
                out.append(f"{name}__{var}")
    return out

def _resolve_adapter_dir(subdir: str) -> Path:
    """Resolve a ``--adapter-dir`` value (relative to rl_training_data/checkpoints/)
    to an absolute, validated checkpoint directory.

    Rejects paths that escape the checkpoints root (path traversal) or that
    don't exist, so a typo fails fast instead of silently falling back to
    whatever checkpoint the infer server already happens to have loaded.
    """
    checkpoints_root = _CHECKPOINTS_ROOT.resolve()
    candidate = (checkpoints_root / subdir).resolve()
    if not candidate.is_relative_to(checkpoints_root):
        raise ValueError(
            f"--adapter-dir must be a subdirectory of {checkpoints_root} (got '{subdir}')"
        )
    if not candidate.is_dir():
        raise ValueError(f"--adapter-dir directory not found: {candidate}")
    return candidate


# ---------------------------------------------------------------------------
# Oracle: read from article_oracle.json  (version 3)
# ---------------------------------------------------------------------------
def _read_oracle(variant_name: str) -> tuple[int, list[float]]:
    """Return (oracle_arm_idx, r_w_rewards_list[0..3]).

    Both values come directly from article_oracle.json. As of A.16
    (2026-08-25), that file's own r_w_rewards_list already IS the mean-R_w
    across every available draw (production + replicates) whenever replicate
    data exists -- the earlier article_oracle_averaged.json sibling file /
    canonical-vs-averaged split has been retired, so there is no longer a
    second file to prefer or reconcile against.

    Raises FileNotFoundError when article_oracle.json is absent.
    """
    oracle_path = _BASES_DIR / variant_name / "article_oracle.json"
    if not oracle_path.exists():
        raise FileNotFoundError(f"Missing article_oracle.json: {oracle_path}")
    data = json.loads(oracle_path.read_text(encoding="utf-8"))
    return int(data["oracle_arm_idx"]), data["r_w_rewards_list"]


def _apply_policy_guards(
    preset: int, policy: str, distribution: list[float] | None = None
) -> tuple[int, str | None]:
    """Deterministic hard-constraint clamp (mirrors the server-side guard exactly).

    forbidden -> P0 skip   ·   required -> at least P1 light   ·
    capped -> at most P1 light; WITHIN that ceiling, ``distribution``'s own
    P(skip) vs P(light) always arbitrates the choice (even when preset is
    already in {0, 1} -- it can still disagree with the distribution, e.g.
    after the cost-sensitive rule's adjustment), no distribution -> leave
    an in-bounds preset unchanged   ·   allowed -> unchanged.

    A standard/deep vote is ALWAYS capped to light regardless of distribution
    (A.20.11: the residual P(skip) vs P(light) split is unreliable there) --
    every such clamp is marked AMBIGUOUS and flagged for review: a corpus-wide
    check (A.20.14) found zero confirmed cases of skip beating light in this
    population, including every case where the residual itself favored skip,
    so the residual's direction is not trusted in either direction.

    A skip vote under "required" is likewise ALWAYS elevated to light and marked
    AMBIGUOUS: a corpus-wide check (A.20.15) found no consistent winner among
    light/standard/deep once skip is excluded -- light was clearly best in some
    cases, but in others standard or deep won by a wide margin, and in one case
    light was even the WORST of the three eligible arms (worse than skip itself).

    Returns ``(clamped_preset, note)`` where ``note`` is a short human-readable
    string when a clamp fired, else None.
    """
    if policy == "forbidden":
        return 0, f"policy=forbidden: clamped P{preset}->P0 skip" if preset != 0 else None
    if policy == "required" and preset < 1:
        if distribution:
            return 1, (
                f"policy=required: clamped P{preset}->P1 light — AMBIGUOUS: no "
                f"data-confirmed default among light/standard/deep for a skip vote "
                f"in this population (A.20.15); RL distribution "
                f"P(light)={distribution[1]:.3f}, P(standard)={distribution[2]:.3f}, "
                f"P(deep)={distribution[3]:.3f}; flagged for review"
            )
        return 1, (
            f"policy=required: clamped P{preset}->P1 light — AMBIGUOUS: no "
            f"data-confirmed default among light/standard/deep for a skip vote "
            f"in this population (A.20.15); flagged for review"
        )
    if policy == "capped":
        if preset > 1:
            if distribution:
                return 1, (
                    f"policy=capped: clamped P{preset}->P1 light — AMBIGUOUS: no "
                    f"data-confirmed case of skip beating light for a standard/deep "
                    f"vote in this population (A.20.14); residual "
                    f"P(skip)={distribution[0]:.3f} vs P(light)={distribution[1]:.3f}, "
                    f"flagged for review"
                )
            return 1, (
                f"policy=capped: clamped P{preset}->P1 light — AMBIGUOUS: no "
                f"data-confirmed case of skip beating light for a standard/deep "
                f"vote in this population (A.20.14); flagged for review"
            )
        if distribution:
            resolved = 1 if distribution[1] >= distribution[0] else 0
            if resolved != preset:
                return resolved, (
                    f"policy=capped: distribution favors P{resolved} "
                    f"{_PRESET_NAMES[resolved]} over P{preset} {_PRESET_NAMES[preset]} "
                    f"(P(skip)={distribution[0]:.3f} vs P(light)={distribution[1]:.3f})"
                )
    return preset, None


# ---------------------------------------------------------------------------
# Per-variant runner
# ---------------------------------------------------------------------------
async def run_variant(
    variant: str,
    rl_only: bool,
    grok_only: bool = False,
    rl_guards_only: bool = False,
) -> dict:
    research_dir = _BASES_DIR / variant
    if not research_dir.exists():
        return {"variant": variant, "error": f"Directory not found: {research_dir}"}

    lesson = _lesson_of(variant)
    split = "TEST" if lesson in _TEST_LESSONS else "TRAIN"

    # --- Direct in-process call (no MCP protocol, no agent loop) ---
    call_kwargs: dict = {}
    if grok_only:
        call_kwargs["grok_only"] = True
    if rl_only or rl_guards_only:
        # Both modes evaluate the RL stage only; skip the Grok call.
        call_kwargs["rl_only"] = True
    try:
        data = await predict_exploration_preset_eval(str(research_dir), **call_kwargs)
    except Exception as exc:
        return {"variant": variant, "lesson": lesson, "split": split, "error": str(exc)}

    if data.get("status") == "error":
        return {
            "variant": variant, "lesson": lesson, "split": split,
            "error": data.get("message", "unknown error"),
        }


    rl = data.get("rl_recommendation")     # None when grok_only=True
    grok = data.get("llm_recommendation") # None when rl_only / XAI unset / call failed

    # External-evidence policy (drives guards + regret accounting). Always present
    # in article_evidence regardless of mode.
    evidence = data.get("article_evidence") or {}
    policy = (evidence.get("guideline_context") or {}).get(
        "external_evidence_policy", "allowed"
    )

    # Section-level intermediate infer results (per-section hard-argmax choice x
    # guideline target_words -> word-weighted vote mass per preset, e.g.
    # rl_aggregate["deep_mass"]). Already computed by build_article_evidence() on
    # every request; captured here so --save-json persists it going forward
    # instead of discarding it once this function returns (None in --grok-only
    # mode, where no RL section scoring runs).
    rl_aggregate = evidence.get("rl_aggregate")
    rl_section_signals = evidence.get("section_signals")

    # Determine which preset to evaluate
    guard_note: str | None = None
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
        chosen_preset, guard_note = _apply_policy_guards(rl["preset"], policy, rl.get("agg_probs"))
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
            "guard_note": guard_note,
            "oracle_preset": None,
            "verdict": "NO_ORACLE",
            "entropy_bits": rl["entropy_bits"] if rl else None,
            "confidence": rl["confidence"] if rl else None,
            "floor_applied": rl["floor_correction_applied"] if rl else None,
            "rl_agg_probs": rl.get("agg_probs") if rl else None,
            "rl_aggregate": rl_aggregate,
            "rl_section_signals": rl_section_signals,
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
        "guard_note": guard_note,
        "oracle_preset": oracle_preset,
        "oracle_name": _PRESET_NAMES.get(oracle_preset, "?"),
        "r_w_rewards": [round(r, 4) for r in r_w_rewards],
        "verdict": verdict,
        "regret": regret,
        "regret_counted": regret_counted,
        "entropy_bits": rl["entropy_bits"] if rl else None,
        "confidence": rl["confidence"] if rl else None,
        "floor_applied": rl["floor_correction_applied"] if rl else None,
        "rl_agg_probs": rl.get("agg_probs") if rl else None,
        "rl_aggregate": rl_aggregate,
        "rl_section_signals": rl_section_signals,
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

    rl_agg = r.get("rl_aggregate")
    if rl_agg and rl_agg.get("section_vote_mass"):
        vm = rl_agg["section_vote_mass"]
        vm_str = "  ".join(f"{_PRESET_NAMES[i]}={vm[i]:.2f}" for i in range(len(vm)))
        print(f"  Section vote mass (word-weighted hard vote): {vm_str}")

    if is_guards:
        print(f"  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)")
        note = r.get("guard_note")
        if note:
            flag = "  [FLAGGED FOR REVIEW]" if "AMBIGUOUS" in note else ""
            print(f"               {note}{flag}")
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


def _confusion_matrix(results: list[dict]) -> None:
    """Print a 4×4 confusion matrix (oracle rows × predicted columns) for a result set."""
    scoreable = [
        r for r in results
        if r.get("oracle_preset") is not None and r.get("chosen_preset") is not None
        and r.get("verdict") not in ("NO_ORACLE", "ERROR", None)
        and "error" not in r
    ]
    if not scoreable:
        print("  (no scoreable results for confusion matrix)")
        return

    mat = [[0] * _NUM_PRESETS for _ in range(_NUM_PRESETS)]
    for r in scoreable:
        mat[r["oracle_preset"]][r["chosen_preset"]] += 1

    print(f"  {'':24} Predicted →")
    header = f"  {'Oracle ↓':24}" + "".join(f"  {_PRESET_NAMES[i]:>8}" for i in range(_NUM_PRESETS))
    print(header)
    print(f"  {'-'*60}")
    for oracle_arm in range(_NUM_PRESETS):
        row_total = sum(mat[oracle_arm])
        if row_total == 0:
            continue
        row = f"  P{oracle_arm} {_PRESET_NAMES[oracle_arm]:<20}" + "".join(
            f"  {mat[oracle_arm][pred]:>8}" for pred in range(_NUM_PRESETS)
        )
        print(row + f"  (n={row_total})")


def _baselines(results: list[dict]) -> None:
    """Print majority-class and uniform-random accuracy baselines."""
    scoreable = [
        r for r in results
        if r.get("oracle_preset") is not None
        and r.get("verdict") not in ("NO_ORACLE", "ERROR", None)
        and "error" not in r
    ]
    if not scoreable:
        return

    n = len(scoreable)
    # Majority-class: predict the most common oracle arm
    from collections import Counter
    oracle_counts = Counter(r["oracle_preset"] for r in scoreable)
    majority_arm, majority_n = oracle_counts.most_common(1)[0]
    majority_acc = majority_n / n

    # Uniform random: 1/_NUM_PRESETS expected accuracy
    random_acc = 1.0 / _NUM_PRESETS

    # Weighted random: predict arm proportional to oracle distribution
    weighted_acc = sum((c / n) ** 2 for c in oracle_counts.values())

    dist_str = "  ".join(f"P{arm}={cnt}" for arm, cnt in sorted(oracle_counts.items()))
    print(f"  Oracle distribution: {dist_str}")
    print(
        f"  Majority-class baseline (always P{majority_arm} {_PRESET_NAMES[majority_arm]}): "
        f"{majority_acc:.1%}  ({majority_n}/{n})"
    )
    print(f"  Uniform-random baseline (1/{_NUM_PRESETS}):  {random_acc:.1%}")
    print(f"  Weighted-random baseline:  {weighted_acc:.1%}")


def _split_stats(results: list[dict]) -> tuple[int, int, int, int, list[float], int]:
    """Return (exact, near, miss, error, regret_counted_list, n_forbidden) for a result set."""
    counts: dict[str, int] = {}
    for r in results:
        v = r.get("verdict", "ERROR")
        counts[v] = counts.get(v, 0) + 1
    counted = [r["regret_counted"] for r in results if r.get("regret_counted") is not None]
    n_forbidden = sum(1 for r in results if r.get("policy") == "forbidden")
    return (
        counts.get("EXACT", 0),
        counts.get("NEAR", 0),
        counts.get("MISS", 0),
        counts.get("ERROR", 0) + counts.get("NO_ORACLE", 0),
        counted,
        n_forbidden,
    )


def _print_split_block(
    label: str,
    results: list[dict],
    mode: str,
) -> None:
    """Print the per-row table, stats, confusion matrix, and baselines for one split."""
    if not results:
        return
    sep = "=" * 80
    print(f"\n{sep}")
    print(f"  {label}  [{mode}]  (n={len(results)})")
    print(sep)
    header = f"  {'Article':<46} {'Spl':>4}  {'RL':>4}  {'Grok':>4}  {'Chsn':>4}  → {'Orcl':<4}  Verdict"
    print(header)
    print(f"  {'-'*76}")

    for r in results:
        rl_p = r.get("rl_preset")
        gp = r.get("grok_preset")
        chosen = r.get("chosen_preset")
        op = r.get("oracle_preset")
        v = r.get("verdict", "ERROR")
        rl_str = f"P{rl_p}" if rl_p is not None else "—"
        gp_str = f"P{gp}" if gp is not None else "—"
        ch_str = f"P{chosen}" if chosen is not None else "?"
        op_str = f"P{op}" if op is not None else "?"
        sym = {"EXACT": "✓", "NEAR": "~", "MISS": "✗"}.get(v, "?")
        print(
            f"  {r['variant']:<46} {r.get('split','?'):>4}  "
            f"{rl_str:>4}  {gp_str:>4}  {ch_str:>4}  → {op_str:<4}  {sym} {v}"
        )

    exact, near, miss, error, counted, n_forbidden = _split_stats(results)
    total = len(results)
    n_scoreable = exact + near + miss
    mae = (
        sum(abs(r["chosen_preset"] - r["oracle_preset"])
            for r in results
            if r.get("chosen_preset") is not None and r.get("oracle_preset") is not None)
        / n_scoreable if n_scoreable else 0.0
    )
    mean_regret = sum(counted) / len(counted) if counted else 0.0
    max_regret = max(counted) if counted else 0.0
    print(
        f"\n  n={total}  exact={exact} ({exact/total:.0%})  "
        f"near={near} ({near/total:.0%})  miss={miss} ({miss/total:.0%})  "
        f"no-oracle/error={error}"
    )
    print(f"  Ordinal MAE: {mae:.3f}")
    print(
        f"  Reward-regret (allowed/required only, n={len(counted)}; "
        f"{n_forbidden} forbidden excluded):  mean={mean_regret:.4f}  max={max_regret:.4f}"
    )

    print(f"\n  --- Confusion matrix ---")
    _confusion_matrix(results)

    print(f"\n  --- Baselines ---")
    _baselines(results)

    # Per-variant-type breakdown (training variants only)
    variant_rows = [r for r in results if "__var_" in r.get("variant", "")]
    for var_type in _VARIANTS:
        vt_r = [
            r for r in variant_rows
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
        regret_str = (
            f"regret mean={sum(vt_regrets)/len(vt_regrets):.4f} max={max(vt_regrets):.4f}"
            if vt_regrets else "regret n/a (all policy-forced)"
        )
        print(
            f"  {var_type:<16} ({n:2d}):  "
            f"exact {s_exact}/{n}   exact+near {s_near}/{n}   {regret_str}"
        )


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

    train_results = [r for r in results if r.get("split") == "TRAIN"]
    test_results  = [r for r in results if r.get("split") == "TEST"]

    if test_results:
        _print_split_block("TEST  (held-out, primary metric)", test_results, mode)
    if train_results:
        _print_split_block("TRAIN (reference)", train_results, mode)

    # Combined totals when both splits present
    if train_results and test_results:
        sep = "#" * 80
        print(f"\n{sep}")
        print(f"  COMBINED  [{mode}]  (n={len(results)})")
        print(sep)
        exact, near, miss, error, counted, n_forbidden = _split_stats(results)
        total = len(results)
        mean_regret = sum(counted) / len(counted) if counted else 0.0
        max_regret = max(counted) if counted else 0.0
        print(
            f"  n={total}  exact={exact} ({exact/total:.0%})  "
            f"near={near} ({near/total:.0%})  miss={miss} ({miss/total:.0%})  "
            f"no-oracle/error={error}"
        )
        print(
            f"  Reward-regret (allowed/required only, n={len(counted)}; "
            f"{n_forbidden} forbidden excluded):  mean={mean_regret:.4f}  max={max_regret:.4f}"
        )


_MODE_SUBDIR = {
    "rl_only": "rl_only_results",
    "rl_guards_only": "rl_guard_results",
    "grok_only": "grok_only_results",
    "rl_and_grok": "rl_and_grok_results",
}


def _resolve_output_dir(rl_only: bool, grok_only: bool, rl_guards_only: bool) -> Path:
    """Save results next to the checkpoint that generated them rather than the
    shared grok_planner_test_results/ dir, so results from different
    checkpoints never get silently conflated (this is what made the
    run31/ep109 vs run33/ep81 comparison stale -- see A.17/A.25)."""
    adapter_dir = Path(os.environ.get("RL_INFER_ADAPTER_DIR") or _DEFAULT_ADAPTER_DIR)
    if rl_only:
        mode_key = "rl_only"
    elif rl_guards_only:
        mode_key = "rl_guards_only"
    elif grok_only:
        mode_key = "grok_only"
    else:
        mode_key = "rl_and_grok"
    return adapter_dir / _MODE_SUBDIR[mode_key]


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
            "Test predict_exploration_preset_eval via a direct in-process call. "
            "Evaluates 24 training variants (8 lessons \u00d7 3 guideline variants) and/or "
            "16 held-out test articles (no-variant) against article_oracle.json. "
            "No LLM orchestration layer — the function makes the final decision internally."
        )
    )
    parser.add_argument(
        "--all", action="store_true",
        help="Run all articles: 24 training variants + 16 held-out test articles (default behaviour).",
    )
    parser.add_argument(
        "--train-only", action="store_true",
        help="Run only the 24 training variants (skip held-out test articles).",
    )
    parser.add_argument(
        "--test-only", action="store_true",
        help="Run only the 16 held-out test articles (no training variants).",
    )
    parser.add_argument(
        "--articles", type=str,
        help=(
            "Comma-separated variant names or bare lesson names. "
            "Bare training lesson names expand to all 3 variants; "
            "bare test lesson names (04, 07, 13, 14, 29, 31) pass through unchanged. "
            "E.g.: 04_structured_outputs,02_workflows_vs_agents,09_RAG__var_minimal"
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
        help="Evaluate rl_recommendation.preset only (skip LLM planner stage).",
    )
    parser.add_argument(
        "--rl-guards-only", action="store_true",
        help=(
            "Ablation: RL aggregate + deterministic policy guards "
            "(forbidden→skip, required→≥light, capped→≤light), no LLM planner call. "
            "The benchmark the LLM planner must beat."
        ),
    )
    parser.add_argument(
        "--grok-only", action="store_true",
        help=(
            "LLM planner standalone baseline (currently Grok 4.2): no RL signals. "
            "Measures the LLM planner's marginal contribution vs. the RL model."
        ),
    )
    parser.add_argument("--save-json", action="store_true", help="Save per-variant JSON results.")
    parser.add_argument(
        "--adapter-dir", type=str, default=None,
        metavar="SUBDIR",
        help=(
            "Override which RL checkpoint the infer server loads, as a path "
            "relative to rl_training_data/checkpoints/ (e.g. "
            "tasks/run31_averaged_confidence/epochs/epoch_0109). "
            "Equivalent to exporting RL_INFER_ADAPTER_DIR, but scoped to this run."
        ),
    )
    parser.add_argument(
        "--bases-dir", type=Path, default=None,
        metavar="PATH",
        help=(
            "Override the bases root used for BOTH the tool's research_directory "
            "argument AND article_oracle.json scoring (default: production "
            "rl_training_data/bases/). Use this to score a checkpoint against an "
            "alternate reward-formula experiment's own oracle labels/rewards -- "
            "without it, oracle/reward figures are always read from production "
            "C2 regardless of which checkpoint --adapter-dir points at."
        ),
    )
    args = parser.parse_args()

    if args.bases_dir is not None:
        resolved_bases_dir = args.bases_dir.resolve()
        if not resolved_bases_dir.is_dir():
            print(f"ERROR: --bases-dir directory not found: {resolved_bases_dir}")
            return
        global _BASES_DIR
        _BASES_DIR = resolved_bases_dir

    n_modes = sum([args.rl_only, args.grok_only, args.rl_guards_only])
    if n_modes > 1:
        print("ERROR: --rl-only, --rl-guards-only and --grok-only are mutually exclusive.")
        return
    if args.train_only and args.test_only:
        print("ERROR: --train-only and --test-only are mutually exclusive.")
        return

    resolved_adapter_dir: Path | None = None
    if args.adapter_dir:
        try:
            resolved_adapter_dir = _resolve_adapter_dir(args.adapter_dir)
        except ValueError as exc:
            print(f"ERROR: {exc}")
            return
        # Consumed both by ensure_infer_server() (in-process, via preset_infer_handler)
        # for which checkpoint to load, and by _resolve_output_dir() below for
        # --save-json's output path.
        os.environ["RL_INFER_ADAPTER_DIR"] = str(resolved_adapter_dir)

    # Build variant list
    if args.articles:
        variant_list = _expand_articles([a.strip() for a in args.articles.split(",")])
    elif args.test_only:
        variant_list = list(_TEST_ARTICLES)
    elif args.train_only:
        variant_list = list(_ALL_VARIANTS)
    else:
        variant_list = list(_ALL_ARTICLES)  # default: train + test

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
    if resolved_adapter_dir is not None:
        print(f"  Adapter  : {resolved_adapter_dir}  (--adapter-dir override)")
    print(f"  Bases dir: {_BASES_DIR}" + ("  (--bases-dir override)" if args.bases_dir is not None else ""))
    print(f"  Variants : {variant_list}")

    results = []
    for variant in variant_list:
        lesson = _lesson_of(variant)
        split = "TEST" if lesson in _TEST_LESSONS else "TRAIN"
        print(f"\n{'='*80}")
        print(f"  Variant : {variant}  [{split}]")
        print("=" * 80)

        result = await run_variant(variant, rl_only, grok_only, rl_guards_only)
        results.append(result)
        _print_variant_result(result)

    _print_summary(results, rl_only, grok_only, rl_guards_only)

    if args.save_json:
        out_dir = _resolve_output_dir(rl_only, grok_only, rl_guards_only)
        _save_results(results, out_dir)


if __name__ == "__main__":
    asyncio.run(main())
