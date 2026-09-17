# RL Inference Service (`rl_inference_service`)

The **production** RL inference path: the Qwen3-4B + LoRA exploration-preset
policy, with **no LLM call anywhere in this package**. This is what
`mcp_server`'s `predict_exploration_preset_tool` spawns as a subprocess —
see the top-level [../../../README.md](../../../README.md) for how this
fits into the overall pipeline, and its
[Results](../../../README.md#results-rlguards-vs-baselines) section for how
well it performs.

If you're looking for the harness that benchmarks this policy against an
LLM planner, see [../evaluation/README.md](../evaluation/README.md) instead
— that's a separate, eval-only package.

---

## Contents

- [Layout](#layout)
- [Install](#install)
- [Configure environment variables](#configure-environment-variables)
- [The production checkpoint](#the-production-checkpoint)
- [The inference pipeline, step by step](#the-inference-pipeline-step-by-step)
- [What signals feed the RL model](#what-signals-feed-the-rl-model)
- [What the RL model outputs](#what-the-rl-model-outputs)
- [What the guards do](#what-the-guards-do)
- [How it's invoked in production](#how-its-invoked-in-production)
- [Manual CLI usage](#manual-cli-usage)
- [Digest generation](#digest-generation)

---

## Layout

```
rl_inference_service/
├── infer.py             # Qwen3-4B + LoRA section-level inference, CLI + HTTP server (--serve)
├── generate_digests.py  # Builds research_digest.md (gap profile + section coverage) from a research dir
├── _rl_preset.py         # Preset constants (skip/light/standard/deep) + build_rl_input()
├── _infer_config.py      # Adapter-dir / model-path resolution shared by infer.py + generate_digests.py
├── _digest_parse.py      # stdlib-only parsers for <digest_meta>/<gap_profile>/<section_coverage>
├── checkpoints/
│   └── production/      # The shipped LoRA adapter (adapter_config.json + adapter_model.safetensors)
├── .env.example
└── pyproject.toml
```

---

## Install

```bash
uv sync
```

Pulls `torch`/`transformers`/`peft`/`bitsandbytes`/`accelerate` (CUDA build)
plus `openai`/`anthropic` (used only by `generate_digests.py`'s digest-writing
LLM calls, not by the RL policy itself).

## Configure environment variables

Copy `.env.example` → `.env`:

```bash
XAI_API_KEY=...            # not used by this package's own RL policy;
XAI_BASE_URL=https://api.x.ai/v1  #   present for parity with generate_digests.py's LLM calls
ANTHROPIC_API_KEY=...       # optional — Layer-3 Claude Opus fallback in generate_digests.py
```

`mcp_server` also injects `settings.xai_api_key`/`settings.anthropic_api_key`
directly into this subprocess's environment when it spawns `generate_digests.py`
(see `preset_planner_handler.py::_generate_digest_via_subprocess`), so a local
`.env` here is only needed for standalone/manual CLI runs.

---

## The production checkpoint

`checkpoints/production/` is the LoRA adapter actually used in production —
no `--adapter-dir` flag needed for the default run. It can be overridden via
the `RL_INFER_ADAPTER_DIR` environment variable (read by `mcp_server`'s
`preset_infer_handler.py`) or `infer.py --adapter-dir <path>` directly.

`infer.py` looks first at `RL_researcher_writer_ymaxing/models/Qwen3-4B/` for
the base weights (falls back to downloading `Qwen/Qwen3-4B` from the Hugging
Face Hub if missing).

To ship a newly-trained checkpoint (see
[../training/README.md](../training/README.md)) as the new production
default, copy its `best/` directory here:

```bash
cp -r ../../rl_training_data/checkpoints/tasks/<task-id>/best/* checkpoints/production/
```

---

## The inference pipeline, step by step

`predict_exploration_preset` (the MCP tool step 3.4 calls) runs the
following chain. Steps 1–3 are **this package**; steps 4–5 run in
`mcp_server` (`preset_infer_handler.py`/`preset_planner_handler.py`) but are
documented here since they're inseparable from what the RL model's output
means.

1. **Load or build the digest** — if `research_digest.md` doesn't already
   exist for the research directory, `generate_digests.py` builds one from
   the exploitation-phase content on disk (see
   [Digest generation](#digest-generation)).
2. **Per-section forward pass** — for every section in the digest's
   `<gap_profile>`, `_rl_preset.build_rl_input(digest, section_id)` builds a
   `{system, user}` prompt pair and `infer.py` runs **one** forward pass of
   Qwen3-4B + LoRA, reading the logits at the final input position restricted
   to exactly 4 candidate next-tokens (`skip`/`light`/`standard`/`deep`) and
   softmaxing them. This is a single-token classification decision, not free
   text generation — the model never writes anything.
3. **Confidence-gated aggregation into one article-level distribution** —
   each section's 4-way probability vector is weighted by
   `target_words × confidence` (see
   [What the RL model outputs](#what-the-rl-model-outputs)) and summed, then
   renormalized across all sections. The article-level **raw argmax** is the
   preset with the highest aggregated probability.
4. **Cost-sensitive adjustment** (`preset_infer_handler.apply_cost_sensitive_rule`)
   — nudges the raw argmax by up to one preset level using an empirical,
   asymmetric reward-cost matrix (see below) fit from the TRAIN-set oracle
   rewards, since a plain argmax treats every misclassification as equally
   costly when it demonstrably isn't.
5. **Deterministic policy guards** (`fallback_aggregator`) — the article's
   `external_evidence_policy` (`forbidden`/`required`/`capped`/`allowed`) can
   still clamp the cost-adjusted preset; see
   [What the guards do](#what-the-guards-do). This is the **only** step that
   can override the RL model's own recommendation in production — there is
   no LLM call anywhere in this chain.

The cost-sensitivity step exists because the 4 presets are not symmetric
mistakes: getting `light` vs. `standard` wrong costs less, on average, than
getting `skip` vs. `light` wrong. Writing $\mathrm{Cost}[c][a]$ for the
expected reward lost when the true best preset is $c$ but the pipeline picks
$a$ (fit once from the 24 TRAIN-set article oracles' $R_w$ rewards,
excluding `forbidden`-policy articles), the adjusted decision is

$$
a^\star = \operatorname*{arg\,min}_{a \,:\, |a - a_{\text{raw}}| \le 1} \; \sum_{c=0}^{3} P(c)\,\mathrm{Cost}[c][a]
$$

where $P(c)$ is the aggregated per-section vote distribution from step 3 and
$a_{\text{raw}}$ is the raw argmax. The $|a-a_{\text{raw}}|\le 1$ constraint
exists because an *unconstrained* argmin was found (by backtest) to
occasionally jump two preset levels purely because a cheap preset has
uniformly low cost as an *action* across every possible true class — adjacent
presets only, and every validated fix on the held-out set survived while that
failure mode was eliminated.

---

## What signals feed the RL model

Each section's `<target_section>` block in `research_digest.md` (built by
`generate_digests.py` from the exploitation-phase sources on disk) supplies:

| Signal | Meaning |
|---|---|
| `depth_checklist` / `breadth_checklist` | `N/8` and `N/6` coverage scores against a fixed checklist (motivation, theoretical foundations, technical nuances, latest advancements, limitations/failure modes, implementation tradeoffs, case studies/metrics, artefact availability — depth; adjacent concepts, cross-domain analogies, historical context, enabling technologies, industry applications, adjacent trends — breadth), plus the specific uncovered checklist items. |
| `writing_gaps` | Guideline bullets not yet backed by any source, each tagged `route="depth"` or `route="breadth"`. |
| `need_depth` / `need_breadth` | $(8 - \text{depth\_score}) + 3\times(\text{depth-routed writing\_gaps})$ (symmetrically for breadth) — the primary decision signal; higher means more technical gaps to fill before writing. |
| `target_words` | The writer's prose-word budget for this section — acts as a **ceiling**: exploration rounds that produce material the section cannot absorb offer no benefit regardless of gap size. |
| `must_cover_depth` / `must_stay_brief` | Guideline bullets demanding named tools/numbers/benchmarks/code (pushes toward more, depth-heavy exploration even when `need_depth` is already low) vs. bullets explicitly capped to brief treatment (pushes down regardless of gaps). |
| `<artefact_registry>` | Code/mermaid/table/quote artefacts already extracted from sources — a populated registry reduces the marginal value of further depth exploration on evidence-heavy sections. |

The article-level `external_evidence_policy` field (`allowed`/`forbidden`/
`required`/`capped`, from `guideline_features.json`) is **deliberately
stripped** before the section-level model ever sees it — it's a hard business
rule applied downstream by the guards (step 5), not something the RL policy
should learn to reason about implicitly.

---

## What the RL model outputs

Per section, a raw 4-way probability vector
$p_{\text{sec}} = [\,p_{\text{skip}},\, p_{\text{light}},\, p_{\text{standard}},\, p_{\text{deep}}\,]$.
Two derived quantities matter for aggregation and diagnostics:

- **Confidence** $= \max(\text{margin}, 0.05)$, where `margin` is the gap
  between the top-2 probabilities — a floor prevents a genuinely uncertain
  section from contributing *zero* weight to the article-level vote.
- **Effective weight** $= \text{target\_words} \times \text{confidence}$ — a
  section only dominates the article-level vote if it's both substantial
  (large writing budget) *and* the model is confident about it.

The article-level vote is the confidence-weighted sum of every section's
probability vector, renormalized:

$$
P(\text{preset}=k) \;=\; \frac{\sum_{s} w_s \, p_{\text{sec},s}[k]}{\sum_{s} w_s}, \qquad w_s = \text{target\_words}_s \times \text{confidence}_s
$$

Two extra diagnostics are surfaced (both purely informational — neither
changes the decision):

- **Entropy** $H = -\sum_k P(k)\log_2 P(k)$ (bits) — high entropy (> 1.5 bits)
  is explicitly *not* a license for a downstream client LLM to second-guess
  the pipeline's choice; it's context only.
- **Floor-correction flag** — fires when the aggregate vote is `skip`/`light`
  but at least one individual section voted `standard`/`deep` with low
  overall entropy; currently informational-only (does not itself change the
  preset), flagged for future work.

---

## What the guards do

`fallback_aggregator` is the **only** thing standing between the RL model's
(cost-adjusted) recommendation and the final decision, and it never calls an
LLM — it's a pure function of `external_evidence_policy`:

| Policy | Guard behaviour |
|---|---|
| `allowed` | Passthrough — the RL recommendation is used as-is. |
| `forbidden` | Hard-clamped to `skip` (P0) regardless of the RL vote — external evidence is unusable for this article, so no exploration should run at all. |
| `required` | If the RL vote was `skip`, it's elevated to `light` (P1) — *some* exploration is mandatory. Flagged `AMBIGUOUS` in the result, since a corpus-wide check found no consistent best pick among `light`/`standard`/`deep` once `skip` is excluded (occasionally `light` was even the *worst* of the three). |
| `capped` | If the RL vote is `standard`/`deep`, it's clamped down to `light` (P1), also flagged `AMBIGUOUS` (a corpus check found zero confirmed cases of `skip` beating `light` for capped articles, so `light` is used but not asserted as provably optimal). If the vote is already `skip`/`light`, it's resolved between just those two using the RL model's own residual probability split. |

`AMBIGUOUS` flags are a deliberate signal to a human reviewer (or a
user-directed override, see the top-level README's step-3.4 override
protocol) that the guard made a reasonable but not empirically-validated
choice — they do not indicate an error.

---

## How it's invoked in production

`mcp_server`'s `preset_infer_handler.py::ensure_infer_server()` spawns
`infer.py --serve --port 8787` (configurable via `RL_INFER_PORT`) as a
long-lived HTTP subprocess the first time `predict_exploration_preset` is
called, then reuses it for subsequent calls in the same `mcp_server`
process. A `pid` field in `/health` responses guards against a stale/orphaned
`infer.py` process from a previous crashed session answering health checks
before the freshly-spawned one has actually loaded the model.

`generate_digests.py` is invoked as a **separate, short-lived** subprocess
(`preset_planner_handler.py::_generate_digest_via_subprocess`) whenever a
research directory doesn't already have a `research_digest.md` — it does not
need the HTTP server or the LoRA adapter at all, only LLM API access.

---

## Manual CLI usage

```bash
# Single digest, verbose per-section breakdown
uv run python infer.py --digest /path/to/research_digest.md --verbose

# Long-lived HTTP server (what mcp_server actually spawns)
uv run python infer.py --serve --port 8787
```

---

## Digest generation

The RL policy is conditioned on a structured **exploitation digest** — gap
profile + per-section coverage analysis — extracted from a research
directory's exploitation-phase content:

```bash
uv run python generate_digests.py --research-dir /path/to/research/folder
```

For the offline TRAIN/TEST corpus, digests live at
`../../rl_training_data/bases/<article>/research_digest.md` and are
(re)generated via `generate_digests.py` with no `--research-dir` (defaults
to the full corpus) or `--articles <name...>` for a subset — see
[../training/README.md](../training/README.md) for how this fits into the
offline reward-labeling pipeline.
