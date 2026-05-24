# Article-Level Aggregator — Plan

Scope: design the second stage that turns per-section RL outputs into a single
article-level preset, while the section-level RL policy is still training.

> Reference: prior assistant message argued for **Grok 4.2 as the article-level
> decision layer** (not a local head), with a richer evidence packet from Stage 1.
> This plan adopts that direction but is written against the *current* code
> state (4 presets in the reward, planner code still on 6, `predict_exploration_preset_tool.py`
> already has an RL + Grok pipeline).

---

## 1. Decision: which aggregator do we build now?

Three candidates were on the table:

| Option | Pros | Cons | Verdict |
|---|---|---|---|
| **A. Hand-coded aggregation** (weighted vote + floor) | deterministic, fast, current fallback | brittle, ignores guideline scope, weak on conflicting sections | **Keep as fallback only** |
| **B. Local article-level head** (small classifier on top of section signals) | offline, cheap, distillable | only 21 oracle articles → not enough data; would overfit | **Defer** until Grok decisions accumulate |
| **C. Grok 4.2 reasoning planner** with a richer evidence packet | already wired in, handles guideline-scope reasoning, semantic tradeoffs | API cost, latency, non-determinism | **Adopt as primary** |

**Near-term stack:**

```text
Retrained Qwen section scorer (4-preset)
  └── normalized section signals + compact digest features
        └── Grok 4.2 article-level planner  ← authoritative decision
              └── deterministic fallback if Grok unavailable
```

**Later** (after ~100 Grok decisions + workflow outcomes): distill Grok into a
local article-level head. Not now.

---

## 2. Current gaps in the Grok call

In `predict_exploration_preset_tool.py::_call_grok_planner` Grok currently sees:

- `preset`, `name`, `confidence`, `entropy`, `floor_applied`, `guidance`
- a `section_table` line: `title  P{preset}({name})  top2=[[P3,0.81],[P2,0.11]]`
- raw `article_guideline` (full text)
- raw `digest_gap_profile` extracted from `## 3. Overall Gap Profile`

Missing inputs needed for good article-level reasoning:

1. Full P0–P{N-1} aggregate distribution (not just argmax + entropy).
2. Top-2 *margin* (rank1 - rank2) — disagreement is currently invisible.
3. Per-section **target length / weight** (this exists in the oracle weighting code
   but is not handed to Grok).
4. **Coverage strength** per section (the model has it internally; the digest section
   summary exposes it but it is not row-aligned to the section table).
5. **Normalized gap pressure** (gap count / target length) — raw gap counts mislead
   on long sections.
6. Guideline **scope constraints** in compact form (expected article length,
   theory/practice ratio, hard "no further research" flags).
7. **Section disagreement summary**: how many sections vote each preset, and the
   variance across rows.

These should be derived once in the tool and inserted into the prompt; do not ask
Grok to recompute them.

---

## 3. Evidence packet schema (Stage 1 → Stage 2 contract)

Define a single dict `article_evidence` that Stage 1 emits and Stage 2 prompts on.
Mirror the README's "structured evidence bundle" framing.

```jsonc
{
  "guideline_context": {
    "expected_total_words": 4200,
    "theory_practice_ratio": "60/40",
    "scope_constraints": ["no_more_external_research", "must_cover_eval_pipeline"],
    "sections": [
      {"title": "...", "target_words": 600, "kind": "intro|theory|practice|polish"}
    ]
  },
  "rl_aggregate": {
    "preset": 2,
    "distribution": [0.05, 0.10, 0.55, 0.30],   // length = num_presets
    "confidence": 0.55,
    "entropy_bits": 1.21,
    "top2_margin": 0.25,
    "floor_correction_applied": false
  },
  "section_signals": [
    {
      "title": "...",
      "target_words": 600,
      "weight": 0.14,                           // normalized over article
      "chosen_preset": 3,
      "top2": [["P3", 0.42], ["P2", 0.31]],
      "top2_margin": 0.11,
      "coverage_strength": "weak|moderate|strong",
      "gap_pressure_norm": 0.018,               // gaps per 100 target words
      "depth_breadth_gap": "depth_heavy|breadth_heavy|balanced|none",
      "over_exploration_risk": "low|medium|high"
    }
  ],
  "digest_global": {
    "key_insight": "one-line summary",
    "gap_pressure_norm": 0.012,
    "dominant_gap_type": "coverage|depth|breadth|polish"
  },
  "decision_instructions": [
    "Pick a single article-level preset from {P0..P_{N-1}}.",
    "Override RL when local section votes conflict with global guideline scope.",
    "Penalize exploration when marginal value is low relative to target length.",
    "Do not treat raw gap count as exploration demand; use gap_pressure_norm."
  ]
}
```

Stage 2 prompt renders this as compact JSON inside `<evidence>` tags, plus a
short rules block — no need to send the full guideline text once the compact
`guideline_context` is built.

---

## 4. Concrete code changes

All changes scoped to
`Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/`.

### 4.1 Section-signal builder (Stage 1)

File: `mcp_server/src/tools/predict_exploration_preset_tool.py`

- New helper `_build_section_signal(section, target_words, total_words, digest_section)`
  returning the dict above. Pull `coverage_strength` and per-section gap counts
  from the existing digest section summaries; compute `gap_pressure_norm` and
  `over_exploration_risk` here.
- New helper `_build_guideline_context(article_guideline)` that parses target
  lengths and scope flags. Reuse whatever the oracle script already does for
  section weighting (`training/compute_article_oracle.py`) to avoid drift —
  factor that logic into a shared module `training/_guideline_features.py`
  and import from both places.
- New helper `_build_article_evidence(...)` assembling the full packet.

### 4.2 Article-level Grok planner (Stage 2)

Same file:

- Replace `_PLANNER_USER_TEMPLATE` with a version that embeds the `<evidence>`
  JSON and an explicit rules block (mirroring `decision_instructions`).
- Rename `_call_grok_planner` → `_call_article_level_planner` to make the role
  explicit. Keep signature similar but accept the `article_evidence` dict.
- Keep the standalone Grok-only baseline (`_call_grok_planner_standalone`) but
  also feed it `guideline_context` + `digest_global` (not the raw guideline)
  so that the comparison isolates RL-signal value cleanly.
- Output JSON additions: `decision_drivers: list[str]`, `risk_flags: list[str]`,
  plus the existing `preset / name / reasoning / override / override_reason`.

### 4.3 Preset-count migration (blocking)

`_NUM_PRESETS` and `_PRESET_NAMES` are currently 6 in `eval_accuracy.py`,
`compute_article_oracle.py`, `recompute_oracle_with_prior.py`,
`analyze_eval_results.py`, and indirectly in `infer.py`. Reward is already on
4 presets. Before wiring the new aggregator:

- Centralize `NUM_PRESETS` and `PRESET_NAMES` in one module (e.g.
  `training/_presets.py`) and have every consumer import from it.
- Verify the trained policy head output dimension matches.

This is a prerequisite — the planner cannot emit a sane preset if the schema
is inconsistent across files.

### 4.4 Deterministic fallback

Keep the current weighted-vote + floor logic as the fallback when
`XAI_API_KEY` is missing or Grok fails to return parseable JSON. Move it into
a `_fallback_aggregator(article_evidence) -> dict` so it consumes the same
packet shape — useful both as a guardrail and as a baseline in eval.

### 4.5 Eval & diagnostics

`training/eval_accuracy.py` and `training/analyze_eval_results.py`:

- Add three columns per article: `pred_fallback`, `pred_grok_full`, `pred_grok_standalone`.
- Report article-level accuracy and oracle-margin diagnostics for each.
- Persist the evidence packet alongside predictions
  (`grok_planner_test_results/{article}.json`) so we can replay decisions
  offline once the policy changes.

---

## 5. Validation checklist (before declaring done)

1. Schema round-trip: build evidence packet for all 21 oracle articles, assert
   no missing fields, all numerics finite.
2. Fallback parity: with Grok disabled, the new pipeline must reproduce the
   current top-1 article preset on ≥19/21 oracle articles (regression guard).
3. Grok-full vs Grok-standalone: Grok-full should not be *worse* than
   Grok-standalone on oracle accuracy; if it is, the section signals are
   misleading and Stage 1 must be re-examined.
4. Override audit: log every case where Grok overrides RL, including
   `override_reason`. Review weekly until ≥80% of overrides are judged correct.

---

## 6. What we are deferring

- **Local article-level head** — revisit only after we have ≥100 logged Grok
  decisions plus matched workflow outcomes; until then, no usable training
  signal at the article level.
- **Confidence calibration on Grok output** — wait until override audit
  reveals systematic overconfidence.
- **Multi-call ensembling at the article level** — defer; not justified by
  current eval budget.

---

## 7. Open questions for the user

1. Is the 6→4 preset migration finalized, or are we still keeping P0/P5 as
   reserved slots? This decides whether step 4.3 is a rename or a real prune.
2. Should the standalone Grok baseline keep using the raw guideline text, or
   move to the compact `guideline_context`? (Recommendation: compact, for
   apples-to-apples comparison with the full pipeline.)
3. Where should `_guideline_features.py` live — `training/` or a new
   `shared/` package importable by both `training/` and `mcp_server/`?
