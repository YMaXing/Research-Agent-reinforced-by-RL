# Evaluation Harness (`evaluation`)

An **eval-only** harness that benchmarks the production RL policy — alone,
with its deterministic policy guards, and against an LLM planner — on the
same held-out TRAIN/TEST corpus used throughout this project. This is where
every number in the top-level README's
[Results](../../../README.md#results-rlguards-vs-baselines) section comes
from.

**This code never runs in production.** Production inference is RL policy +
deterministic guard only, no LLM call — see
[../rl_inference_service/README.md](../rl_inference_service/README.md). The
LLM-planner code here exists solely to measure how much the RL stage
contributes over an LLM making the same call.

---

## Contents

- [Layout](#layout)
- [The oracle and the TRAIN/TEST split](#the-oracle-and-the-traintest-split)
- [Install](#install)
- [Modes](#modes)
- [Common flags](#common-flags)
- [Output layout](#output-layout)
- [Reading a result](#reading-a-result)

---

## Layout

```
evaluation/
├── test_planner.py                    # CLI entry point + all reporting (confusion matrix,
│                                       #   baselines, McNemar/Poisson-binomial significance tests)
├── predict_exploration_preset_eval.py # In-process eval function: RL stage + optional LLM-planner stage
├── preset_planner_handler_eval.py     # LLM-planner logic: evidence brief, policy guards, call_llm_planner()
└── preset_planner_prompt_eval.py      # The LLM planner's system/user prompt text
```

A root-level shim (`research_agent_local/test_planner.py`) delegates here so
`uv run --project mcp_server python test_planner.py ...` also works from the
repo root.

---

## The oracle and the TRAIN/TEST split

Every comparison here is against an **oracle preset** per article — computed
once by rolling out the full research → write → grade pipeline under all 4
presets and reading which one the grader scored highest
(`rl_training_data/bases/<article>/article_oracle.json`, `oracle_arm_idx`).
Some articles have `tied_arm_indices` too: other preset(s) an independent
statistical review found indistinguishable from the primary oracle — landing
on any of them also counts as `EXACT`, not just the primary pick.

- **24 TRAIN article-variants** — 8 lessons × 3 guideline-depth variants
  (`var_minimal`/`var_standard`/`var_demanding`), used during GRPO training.
- **16 held-out TEST articles** — no variant expansion, never seen during
  training.

---

## Install

```bash
cd ../mcp_server            && uv sync && cd -
cd ../rl_inference_service  && uv sync && cd -
```

`evaluation/` has no `pyproject.toml` of its own — it's always run via
`uv run --project mcp_server python evaluation/test_planner.py ...`.
`mcp_server`'s venv drives the harness and calls the MCP-adjacent handler
code directly (in-process, no MCP protocol involved); `rl_inference_service`
is spawned as a subprocess to actually load Qwen3-4B + the LoRA adapter.

---

## Modes

Run from `research_agent_local/`:

```bash
# RL policy only — fastest, no LLM call, no policy guard applied
uv run --project mcp_server python evaluation/test_planner.py --rl-only --test-only

# Production-equivalent: RL policy + the deterministic policy guard actually
# used in production (forbidden→skip, required→≥light, capped→≤light)
uv run --project mcp_server python evaluation/test_planner.py --rl-guards-only --test-only

# LLM-planner standalone baseline — no RL signal at all
uv run --project mcp_server python evaluation/test_planner.py --llm-only --planner-model grok-4.6 --test-only
uv run --project mcp_server python evaluation/test_planner.py --llm-only --planner-model claude-opus-4-5 --test-only

# Default (no flag) = full pipeline: RL → LLM planner stage. Since the LLM
# planner stage is skipped by default (PRESET_PLANNER_SKIP_LLM=true), this
# is currently IDENTICAL to --rl-guards-only.
uv run --project mcp_server python evaluation/test_planner.py --test-only
```

`--planner-model` accepts **any xAI model** (e.g. `grok-4.6`, the default) or
**any Anthropic model** (e.g. `claude-opus-4-5`, `claude-sonnet-5`) — the
provider and required API key (`XAI_API_KEY`/`ANTHROPIC_API_KEY`) are
resolved automatically from the model name prefix. Both keys are read from
`os.environ` first, then `mcp_client/.env`.

For each article, the harness:

1. Reads `rl_training_data/bases/<article>/research_digest.md` (generated
   on demand via `rl_inference_service/generate_digests.py` if missing).
2. Runs section-level inference with the LoRA policy (unless `--llm-only`)
   and/or calls the LLM planner (unless `--rl-only`/`--rl-guards-only`).
3. Compares against `article_oracle.json`.
4. Reports `EXACT` / `NEAR` (±1 preset) / `MISS`, reward-regret, a confusion
   matrix, and majority-class / uniform-random / weighted-random baselines,
   plus McNemar and Poisson-binomial exact significance tests.

---

## Common flags

```bash
uv run --project mcp_server python evaluation/test_planner.py --articles 09_RAG,04_structured_outputs
uv run --project mcp_server python evaluation/test_planner.py --variants demanding     # one variant type only
uv run --project mcp_server python evaluation/test_planner.py --train-only            # 24 TRAIN variants only
uv run --project mcp_server python evaluation/test_planner.py --save-json             # persist per-article JSON
uv run --project mcp_server python evaluation/test_planner.py --adapter-dir tasks/<task-id>/best  # evaluate a non-production checkpoint
uv run --project mcp_server python evaluation/test_planner.py --bases-dir /path/to/alt/bases       # score against an alternate reward-formula experiment
```

`--adapter-dir` is relative to `rl_training_data/checkpoints/`; omit it to
use the production checkpoint (`rl_inference_service/checkpoints/production/`).

---

## Output layout

`--save-json` writes results **next to the checkpoint that generated them**
(not a shared directory), so results from different checkpoints or modes
never get silently conflated:

```
<adapter_dir>/
├── rl_only_results/<variant>.json + _summary.json
├── rl_guard_results/<variant>.json + _summary.json     # production-equivalent mode
├── llm_only_results/<variant>.json + _summary.json
└── rl_and_llm_results/<variant>.json + _summary.json
```

For the production checkpoint, `<adapter_dir>` is
`rl_inference_service/checkpoints/production/`.

---

## Reading a result

Each per-article JSON records the RL aggregate distribution (confidence,
entropy, floor-correction flag), the LLM planner's decision + reasoning
(when run), the chosen preset, the oracle preset (+ tied arms), reward-regret,
and the verdict. `chosen_by` reflects which mode produced the pick
(`"RL"`, `"RL+guards"`, `"<planner-model>-only"`, or `"<planner-model>"` for
the full pipeline).

See the top-level README's
[Results](../../../README.md#results-rlguards-vs-baselines) section for the
current headline numbers, and
[`rl_training_data/rl_planner_test_results/`](../../rl_training_data/rl_planner_test_results/README.md)
for the full statistical derivation (`analysis_document.md`).
