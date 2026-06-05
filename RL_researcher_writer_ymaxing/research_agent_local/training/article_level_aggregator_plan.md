# Article-Level Aggregator — Plan (v2, post section-level training)

Scope: design the second stage that turns the per-section RL outputs into a
single article-level exploration preset. The section-level RL policy is now
**trained** (run12 adapter), and the digest/inference pipeline is on the
**4-preset** scheme (`skip / light / standard / deep`). This revision rewrites
the plan against the *actual* current code and data.

> Direction (unchanged): use **Grok 4.2 as the article-level decision layer**,
> fed a structured evidence packet from Stage 1; defer a local article-level
> head until enough Grok decisions accumulate.

---

## 0. What changed since v1 of this plan

- **Presets: 6 → 4.** `_rl_preset.py` is the single source of truth:
  `NUM_PRESETS = 4`, `PRESET_NAMES = {0:skip, 1:light, 2:standard, 3:deep}`.
  `train_grpo.py`, `infer.py`, and `predict_exploration_preset_tool.py` all
  consume this. The Grok planner prompt in the tool is already on P0–P3.
- **Section-level training is done.** No retraining needed for Stage 1; the
  default adapter is `rl_training_data/checkpoints/tasks/run12/best`.
- **Digest format is XML v2** (`<digest_meta>`, `<artefact_registry>`,
  `<sources>`, `<section_coverage>`, `<gap_profile>`), produced by
  `generate_digests.py`. The legacy markdown digest is gone.
- **Two digest-generation bugs fixed (this pass):**
  1. The tool's on-the-fly digest generator emitted the *old markdown* format,
     which the trained model cannot consume → `predict_exploration_preset_tool.py`
     now delegates to `generate_digests.py --research-dir` (v2 XML, single
     source of truth).
  2. `_extract_gap_profile` only matched the markdown `## 3. Overall Gap
     Profile` header → always empty for XML digests. It now extracts the XML
     `<gap_profile>` block.
- **Dataset is 8 articles × 3 variants = 24 article-variants** (the
  `ARTICLES` list in `train_grpo.py`), not 21.

---

## 1. Decision: which aggregator do we build now?

| Option | Verdict |
|---|---|
| **A. Hand-coded aggregation** (word-weighted vote + floor) | Keep as deterministic fallback only (Grok unavailable / parse failure). |
| **B. Local article-level head** | **Defer.** 24 article-variants is too few; only one stale 6-preset article oracle exists. Revisit after ≥~100 logged Grok decisions + workflow outcomes. |
| **C. Grok 4.2 reasoning planner** with a rich evidence packet | **Adopt as primary.** Already wired (`_call_grok_planner`). Needs a much richer packet (Section 3). |

**Near-term stack:**

```text
Trained Qwen3-4B section scorer (4-preset, run12)
  └── per-section probs + digest-derived numeric signals
        └── article evidence packet (built in the tool)
              └── Grok 4.2 article-level planner   ← authoritative decision
                    └── deterministic fallback if Grok unavailable
```

---

## 2. Current gaps in the Grok call (the core of this plan)

`_call_grok_planner` in `predict_exploration_preset_tool.py` currently feeds Grok:

- RL aggregate: `preset`, `confidence`, `entropy`, `floor_applied`, `guidance`.
- `section_table`: one line per section — `[sec_id] P{preset}(name) top2=[...]`.
- raw `article_guideline` (full text).
- `digest_gap_profile` (now the XML `<gap_profile>` block, after the fix).

### 2.1 The decisive insight: the section model is deliberately blinded to article-level signals

`build_rl_input` (in `_rl_preset.py`) **strips three article-level fields** from
every per-section input, with an explicit comment that they belong to the
*downstream article-level aggregator*:

- `external_evidence_policy` ∈ {`forbidden`, `allowed`, `required`} —
  `forbidden` short-circuits exploration upstream; `allowed`/`required` are
  *meant to be consumed here*. **Today Grok never sees it.** This is the single
  most important missing signal: `required` should bias the article preset up;
  `forbidden` forces `skip`.
- `tavily_saturation` ∈ [0,1] — how exhausted exploitation search already is.
  High saturation ⇒ extra rounds yield duplicates ⇒ bias down. **Not passed.**
- `n_orphan_anchors` — article-wide count of guideline anchors with no source
  backing. **Not passed.**

Because the section model cannot see these, the **aggregator is the only place
they can influence the decision.** They must be in the packet.

### 2.2 Rich per-section signals already in the digest but not forwarded

Every digest carries, per section, numeric signals the section model saw but
that are collapsed to a single preset before reaching Grok. From `<gap_profile>`:

- `need_depth`, `need_breadth` (raw gap pressure)
- `target_words` (section weight / writing budget)
- `mandatory_bullets`, `must_cover_depth`, `must_stay_brief`

From `<section_coverage>` per `<section>`:

- `depth_score` (N/8), `breadth_score` (N/6)
- `orphan_anchors n_depth/n_breadth/n_unreachable`
- `self_contained`, `sources`, `artefacts`, `<intent>`

From `<overall>`: `weakest_sections`, `strongest_sections`, `dominant_gap_type`.
From `<digest_meta>`: `total_sources`, `total_artefacts`, `n_content_sections`.

### 2.3 RL signals collapsed too aggressively

The infer server returns, per section: `chosen`, full 4-`probs`, `margin`,
`confidence`, `weight`, `target_words`. Grok only gets `chosen` + `top2`.
Missing: the **full article aggregate distribution** `[skip,light,standard,deep]`,
the **top-2 margin** (rank1−rank2) at article and section level, and the
per-section **target-word weight** that drove the aggregate.

### 2.4 Smaller issues

- `section_signals[i].title` is the `sec_id` (e.g. `S6::...`), not a readable
  title — fine for Grok but worth mapping to the section heading.
- `_call_infer_server` reads a `corrections` key the server never returns →
  dead (`meta` always `{}`). Remove or wire up.
- The full raw guideline is sent; once `guideline_context` (Section 3) is built,
  the raw guideline is redundant token cost.

---

## 3. Evidence packet schema (Stage 1 → Stage 2 contract)

A single `article_evidence` dict built **in the tool** from (a) the infer-server
output and (b) the digest XML it already holds. All fields below are derivable
from data that exists today — no new model outputs required.

```jsonc
{
  "guideline_context": {
    "external_evidence_policy": "forbidden|allowed|required",  // digest_meta
    "n_content_sections": 8,
    "expected_total_words": 3320,                 // Σ target_words
    "sections": [
      { "sec_id": "S6::...", "title": "Key strategies...",
        "target_words": 650, "mandatory_bullets": 5,
        "must_cover_depth": 6, "must_stay_brief": 0 }
    ]
  },
  "rl_aggregate": {
    "preset": 2,
    "distribution": [0.08, 0.20, 0.50, 0.22],     // skip,light,standard,deep
    "confidence": 0.50,
    "entropy_bits": 1.61,
    "top2_margin": 0.28,
    "floor_correction_applied": false
  },
  "section_signals": [
    {
      "sec_id": "S6::...", "title": "Key strategies...",
      "target_words": 650, "weight": 0.196,        // target_words / Σ
      "chosen_preset": 3,
      "distribution": [0.05, 0.10, 0.30, 0.55],
      "top2": [["deep", 0.55], ["standard", 0.30]],
      "top2_margin": 0.25,
      "model_confidence": 0.55,                    // infer 'confidence'
      // digest-derived numeric coverage signals:
      "need_depth": 55, "need_breadth": 1,
      "depth_score": "2/8", "breadth_score": "5/6",
      "must_cover_depth": 6, "must_stay_brief": 0,
      "orphans": {"depth": 9, "breadth": 0, "unreachable": 1},
      "self_contained": true
    }
  ],
  "digest_global": {
    "tavily_saturation": 1.0,
    "n_orphan_anchors": 68,
    "total_artefacts": 20,
    "dominant_gap_type": "depth",
    "weakest_sections": ["S6::...", "S7::..."],
    "strongest_sections": ["S5::...", "S3::..."]
  },
  "decision_instructions": [
    "Pick ONE article-level preset from {skip, light, standard, deep}.",
    "If external_evidence_policy == 'forbidden' → skip (exploration is unusable).",
    "If external_evidence_policy == 'required' → bias upward at least one level.",
    "High tavily_saturation (→1.0) means more rounds mostly return duplicates → bias down.",
    "Weight sections by target_words; a brief section (must_stay_brief>0 or small target_words) cannot absorb extra research regardless of gap size.",
    "Treat must_cover_depth as depth pressure even when need_depth looks modest.",
    "Use need_depth/need_breadth as direction (depth-first vs breadth), not as a raw round count.",
    "Override the RL aggregate only when guideline scope or saturation gives a concrete reason."
  ]
}
```

Render this as compact JSON inside `<evidence>` tags plus the rules block;
drop the full raw guideline once `guideline_context` is built.

---

## 4. Concrete code changes

All in `research_agent_local/`. The digest-generation fixes (Section 0) are
**already done**; the items below are the remaining aggregator work.

### 4.1 Build the evidence packet (Stage 1 side) — `predict_exploration_preset_tool.py`

- Add `_parse_gap_profile_rows(digest) -> dict[sec_id, {...}]` and
  `_parse_section_coverage(digest) -> dict[sec_id, {depth_score, breadth_score,
  orphans, self_contained, ...}]`. Reuse the regexes already proven in
  `generate_digests.py` / `_rl_preset.py` (`_SECTION_BLOCK_RE`, the gap-profile
  `<section .../>` attribute parse) — factor them into a small shared
  `_digest_parse.py` so the tool and training do not drift.
- Add `_parse_digest_meta(digest)` for `external_evidence_policy`,
  `tavily_saturation`, `n_orphan_anchors`, `total_artefacts`,
  `n_content_sections`.
- Add `_build_article_evidence(digest, agg_probs, preset, section_details)`
  that joins the infer output (`section_details`: chosen/probs/margin/
  confidence/target_words/weight) with the parsed digest signals by `sec_id`,
  and computes `rl_aggregate` (full distribution, top2_margin) and per-section
  `weight = target_words / Σ target_words`.
- Map `sec_id` → readable title from the guideline section headers (optional).

### 4.2 Article-level planner (Stage 2) — same file

- Replace `_PLANNER_USER_TEMPLATE` with a version that embeds the `<evidence>`
  JSON and the `decision_instructions` rules block; stop sending the full raw
  guideline.
- `_call_grok_planner` takes the `article_evidence` dict instead of the loose
  positional args. Keep return keys `preset/name/reasoning/override/
  override_reason`; add `decision_drivers: list[str]` and `risk_flags: list[str]`.
- `_call_grok_planner_standalone` (Grok-alone baseline) should receive the same
  `guideline_context` + `digest_global` (compact) instead of the raw guideline,
  so the full-vs-standalone comparison isolates the RL section signals cleanly.
- Remove the dead `corrections`/`meta` path in `_call_infer_server` (or have the
  infer server emit the floor/correction metadata it currently drops).

### 4.3 Deterministic fallback

Move the current word-weighted-vote + entropy-gated floor into
`_fallback_aggregator(article_evidence) -> dict` consuming the same packet, used
when `XAI_API_KEY` is unset or Grok returns unparseable JSON, and as an eval
baseline. Honor `external_evidence_policy == "forbidden" → skip` here too.

### 4.4 Preset-count migration (remaining surface)

Section-level + tool + planner prompt are **already on 4 presets**. Still stale:

- `compute_article_oracle.py`, `eval_accuracy.py`, `analyze_eval_results.py`,
  `recompute_oracle_with_prior.py` hardcode `NUM_PRESETS = 6` / 6-name maps.
- `article_oracle.json` / `article_oracle_prior.json` in every base dir are
  **stale 6-preset** (`oracle_preset: 4`, `"P4_bal_depth_breadth"`, 6-element
  `article_rewards`).

Action: import `NUM_PRESETS`/`PRESET_NAMES` from `_rl_preset.py` everywhere,
then **recompute the article-level oracle under the 4-preset reward** before any
article-level evaluation. This is the prerequisite for Section 5.

### 4.5 Eval & diagnostics

- `eval_accuracy.py` / `analyze_eval_results.py`: per article-variant emit
  `pred_fallback`, `pred_grok_full`, `pred_grok_standalone` vs the recomputed
  4-preset article oracle; report top-1 accuracy and oracle-margin diagnostics.
- Persist each `article_evidence` packet + Grok decision under
  `grok_planner_test_results/{article}.json` to replay decisions offline and to
  seed future distillation data.

---

## 5. Validation checklist

1. **Digest-gen parity (done-criterion for Section 0):** for ≥3 base dirs,
   `generate_digests.py --research-dir <dir> --force` reproduces a digest whose
   `<gap_profile>`/`<section_coverage>` parse identically to the committed one.
2. **Packet round-trip:** build `article_evidence` for all 24 article-variants;
   assert every field present, all numerics finite, `Σ weight ≈ 1`.
3. **Recompute 4-preset article oracle** (4.4) for all 24; sanity-check it is no
   longer a permutation of 0–5.
4. **Fallback parity:** with Grok disabled, `_fallback_aggregator` reproduces the
   current top-1 article preset on ≥22/24 (regression guard).
5. **Grok-full ≥ Grok-standalone** on article-oracle top-1; if not, the section
   signals are misleading and Stage 1 / packet must be re-examined.
6. **Policy honored:** every `forbidden` article ⇒ final preset `skip`; spot-check
   `required` articles bias upward.
7. **Override audit:** log every Grok override + `override_reason`; review until
   ≥80% judged correct.

---

## 6. Deferred

- **Local article-level head** — until ≥~100 logged Grok decisions + matched
  workflow outcomes exist.
- **Grok output calibration / multi-call ensembling** — until the override audit
  shows systematic error.

---

## 7. Open questions

1. Should the infer server emit the per-section numeric coverage signals
   directly (need_depth, scores, orphans), or should the tool keep parsing them
   from the digest XML it already has? (Recommendation: parse in the tool via a
   shared `_digest_parse.py`; the digest is already in hand and the server stays
   thin.)
2. Confirm the 4-preset article-oracle reward is just the section reward
   re-aggregated by `target_words` (as `compute_article_oracle.py` did for 6
   presets), with no new term — so only `NUM_PRESETS`/names change.
3. Where should the shared digest-parsing helpers live — `training/_digest_parse.py`
   imported by both `mcp_server` and `training`, or duplicated? (Recommendation:
   shared module to prevent drift, mirroring `_rl_preset.py`.)
