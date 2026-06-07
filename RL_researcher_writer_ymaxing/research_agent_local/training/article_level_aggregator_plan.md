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
- **The 24 article-level oracles are finalized.** `compute_article_oracle.py`
  was rewritten to the 4-arm scheme and all 24 `article_oracle.json` files were
  regenerated. Outcome skew: **skip=8, light=11, standard=3, deep=2** — the
  reward strongly favours *cheap* exploration.

---

## 0.5 The train/inference asymmetry — the aggregator *predicts* the oracle, it does not *replicate* it

This is the governing constraint for the whole stage, and it is easy to get
wrong. The article-level **oracle** we just finalized is a **training-time
labeling process**. It decides using three things that **do not exist at
inference on a new article**:

1. **R_w** — the target-words-weighted vote of per-section *rewards*. Computing
   it requires running *all four arms* (skip/light/standard/deep) end-to-end and
   scoring every section against the reference article (`section_oracle.json`).
2. **S3 / S4 / S5 tiebreakers** — bloat, structural compliance, and 3-run
   stability, each measured on the *generated `article.md` of every arm*.
3. **S1 knee / manual overrides** — per-article embedding analysis of marginal
   novelty plus human review (the four hard-coded cases).

At inference you have run **one** exploitation pass → **one** digest. There are
no scored arms, no per-arm articles, no reference text, no rewards. So R_w,
S3–S5, and the S1 knee are all **structurally uncomputable**. The aggregator is
therefore **not** a port of the oracle's decision tree — it is a *predictor* that
approximates the oracle's **output** from an inference-safe evidence packet
(digest signals + the trained section policy's distributions). The oracle is
used **only offline**, as the label that scores the aggregator's accuracy.

**Proxy mapping — every oracle signal → its inference-time stand-in:**

| Oracle signal (training label) | Needs | At inference | Inference proxy in the packet |
|---|---|---|---|
| **R_w** (reward-weighted arm vote) | 4 arms × scored section rewards | ❌ | `rl_aggregate.distribution` — the section policy's target-words-weighted vote. The policy was *trained* to predict each section's reward winner, so its weighted vote is the learned proxy for R_w. |
| **S4** structure (bullets/depth in output) | per-arm `article.md` | ❌ | Guideline *demand* only: `mandatory_bullets`, `must_cover_depth` per section (what's required, not what was produced). |
| **S3** bloat (words vs target) | per-arm `article.md` | ❌ | The *budget* only: `expected_total_words` / per-section `target_words`. |
| **S5** stability (variance over 3 runs) | 3× per-arm `article.md` | ❌ | Section policy `margin` / `confidence` (low confidence ≈ unstable section). |
| **S1 knee / overrides** (marginal novelty) | embeddings over research rounds | ❌ | `tavily_saturation` + `n_orphan_anchors` + gap profile (high saturation ⇒ little new to find). |

Two direct consequences for the build:

- **Do not bake the four manual overrides into the aggregator.** They are
  training-set-specific labels decided by S1/human review; hard-coding them would
  fit the training set and not generalize. The aggregator must *re-derive* those
  calls from the packet (saturation + gaps + RL margins) or accept the miss — and
  those four near-ties are exactly the stress set in §5.
- **Keep the packet leakage-free** (see the invariant at the end of §3): if any
  packet field needs a reward or a per-arm article, it cannot run in production.

---

## 1. Decision: which aggregator do we build now?

| Option | Verdict |
|---|---|
| **A. Hand-coded aggregation** (word-weighted vote + floor) | Keep as deterministic fallback only (Grok unavailable / parse failure). |
| **B. Local article-level head** | **Defer.** 24 article-variants is too few to train a reliable head, even though all 24 now have fresh 4-preset oracles. Revisit after ≥~100 logged Grok decisions + workflow outcomes. Its **input must be the inference-safe evidence packet (§3)**, never the oracle's R_w / S-signals (those don't exist at inference). |
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
  title — fine for Grok but worth mapping to the section heading. **(Done:**
  `_digest_parse.readable_title` + `short_label` give both.**)**
- `_call_infer_server` reads a `corrections` key the server never returns →
  dead (`meta` always `{}`). **(Done: removed; `_call_infer_server` now returns a
  3-tuple. `infer.py`'s vestigial `_meta` is left in place — harmless, internal.)**
- ~~The full raw guideline is redundant token cost.~~ **Reversed (2026-06-06):**
  the raw guideline is now sent as a clearly-delimited **primary-source appendix**
  *after* the structured brief. Rationale: it carries qualitative scope cues
  (intended depth, audience, tone, explicit "keep brief"/"go deep") that the
  numeric distillation provably loses, it exists at inference (so it is
  leakage-safe), and at ~8k tokens it is negligible for Grok. The structured
  brief remains the primary decision basis; the system prompt instructs Grok not
  to let guideline length alone inflate the preset. Gated by
  `_INCLUDE_GUIDELINE_IN_PLANNER` for ablation. **Raw source/research text is
  deliberately NOT injected** — the digest already distils the sources into the
  coverage signals, and the corpus is too large/noisy to re-reason over here.

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
    "DEFAULT TOWARD THE CHEAPER ARM: the oracle reward favours light/skip in 19/24 training articles; escalate to standard/deep only on positive evidence (high need_depth AND a depth mandate AND low saturation).",
    "If external_evidence_policy == 'forbidden' → skip (exploration is unusable).",
    "If external_evidence_policy == 'required' → bias upward at least one level.",
    "High tavily_saturation (→1.0) means more rounds mostly return duplicates → bias down (this is the inference-time proxy for the oracle's S1 marginal-novelty knee).",
    "Weight sections by target_words; a brief section (must_stay_brief>0 or small target_words) cannot absorb extra research regardless of gap size.",
    "Treat must_cover_depth as depth pressure even when need_depth looks modest.",
    "Use need_depth/need_breadth as direction (depth-first vs breadth), not as a raw round count.",
    "Override the RL aggregate only when guideline scope or saturation gives a concrete reason."
  ]
}
```

Render this as a **guided, annotated markdown brief** (not raw JSON) so the
planner reasons over a readable decision brief instead of a numeric blob; the
structured `article_evidence` dict is still returned in the tool result for
eval/replay. Append the **raw article guideline verbatim as a primary-source
appendix** after the brief (see §2.4) so Grok can weigh qualitative scope cues
the distillation loses.

**Leakage invariant (critical).** Every field above is computed from a *single*
exploitation pass — the digest (`<digest_meta>` / `<gap_profile>` /
`<section_coverage>`) plus the trained section policy's outputs. **No field may
derive from per-arm rewards or per-arm generated articles**, because at inference
on a new article none of that exists: one digest, no scored arms, no reference
text. `tavily_saturation` and `n_orphan_anchors` are legitimate precisely
because they summarise that one pass, not a comparison across arms. A CI
assertion should reject any packet field traceable to `section_oracle.json`,
per-arm `article.md`, or reward scoring (see §5.3).

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

- Replace `_PLANNER_USER_TEMPLATE` with a version that embeds the guided evidence
  brief (`_render_evidence_brief`); the decision rules live in the **system
  prompt** (constant, KV-cache friendly), not the user message. The raw guideline
  is appended verbatim as a primary-source appendix (§2.4), gated by
  `_INCLUDE_GUIDELINE_IN_PLANNER`.
- `_call_grok_planner` takes the `article_evidence` dict (+ optional
  `article_guideline`) instead of the loose positional args. Keep return keys
  `preset/name/reasoning/override/override_reason`; add
  `decision_drivers: list[str]` and `risk_flags: list[str]`.
- `_call_grok_planner_standalone` (Grok-alone baseline) receives the same brief
  with the RL sections omitted (`include_rl=False`) **and the same guideline
  appendix**, so the only difference between full and standalone is the RL signal
  — isolating its marginal value cleanly.
- Remove the dead `corrections`/`meta` path in `_call_infer_server`. **(Done.)**

### 4.3 Deterministic fallback

Move the current word-weighted-vote + entropy-gated floor into
`_fallback_aggregator(article_evidence) -> dict` consuming the same packet, used
when `XAI_API_KEY` is unset or Grok returns unparseable JSON, and as an eval
baseline. Honor `external_evidence_policy == "forbidden" → skip` here too.

### 4.4 Preset-count migration (remaining surface)

Section-level + tool + planner prompt are **already on 4 presets**.
`compute_article_oracle.py` is now **done**: rewritten to the 4-arm scheme
(`ARMS = skip/light/standard/deep`, reads `section_oracle.json` v2), and all 24
`article_oracle.json` files were **regenerated** with the new schema
(`oracle_arm`, `oracle_arm_idx`, `r_w_rewards_list`, `margin`, `reward_spread`,
`manual_override`, `needs_review`, per-section `rewards_by_preset`).

Still stale — must import `NUM_PRESETS` / `PRESET_NAMES` from `_rl_preset.py` and
read the new field names (not `oracle_preset`):

- `eval_accuracy.py` (`_NUM_PRESETS = 6`)
- `analyze_eval_results.py` (6-preset reward-gap tables)
- `recompute_oracle_with_prior.py` (`NUM_PRESETS = 6`; writes
  `article_oracle_prior.json`)

**Open:** is the `article_oracle_prior.json` / prior-smoothing path still needed?
The new oracle already encodes near-tie handling (EPS_BAND + S3/S4/S5) and the
manual overrides, so the old prior recompute is likely **obsolete** — decide to
**retire** `recompute_oracle_with_prior.py` rather than port it.

### 4.5 Eval & diagnostics

- `eval_accuracy.py` / `analyze_eval_results.py`: per article-variant emit
  `pred_fallback`, `pred_grok_full`, `pred_grok_standalone` vs the 4-preset
  oracle's `oracle_arm_idx`; report top-1 accuracy.
- **Margin-weighted accuracy.** The oracle now saves `margin` and
  `reward_spread` per article; near-tie labels (small `margin`, or
  `manual_override` / `needs_review = true`) are noisy coin-flips. Report both
  raw top-1 and a margin-weighted score so the aggregator is not over-penalised
  for missing a genuine tie.
- **Near-tie stress set.** Track accuracy separately on the 7 hard articles
  (4 manual overrides — `03_ctx__minimal→light`, `06_tools__minimal→skip`,
  `09_RAG__demanding→deep`, `11_mm__demanding→standard`; 3 signal-flip / fallback
  near-ties — `06_tools__standard`, `09_RAG__standard`, `11_mm__standard`) vs the
  17 clean unique-margin articles. Expect high top-1 on the 17; the 7 are where
  the S1-proxy (saturation / gaps) must carry the call, and some may be
  unrecoverable from inference signals alone.
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
3. **Leakage guard (blocking):** assert no `article_evidence` field is traceable
   to `section_oracle.json`, per-arm `article.md`, or reward scoring — the packet
   must be reproducible from one digest + the section policy alone (§0.5, §3).
4. **4-preset oracle wired:** ✅ `article_oracle.json` regenerated (4-preset);
   confirm eval reads `oracle_arm_idx` (not the stale `oracle_preset`) and that
   no oracle value exceeds 3.
5. **Fallback = R_w-proxy floor:** with Grok disabled, `_fallback_aggregator`
   (RL target-words-weighted vote) reproduces the oracle top-1 on the 17 clean
   articles; record its score on all 24 as the floor Grok must beat.
6. **Grok-full ≥ Grok-standalone ≥ fallback** on oracle top-1; if Grok-full does
   not beat the RL-vote fallback, the section signals / packet add no value and
   Stage 1 must be re-examined.
7. **Near-tie stress set:** report top-1 on the 7 hard articles separately
   (§4.5); audit each decision against its packet `tavily_saturation` + gaps.
8. **Policy honored:** every `forbidden` article ⇒ final preset `skip`;
   spot-check `required` articles bias upward.
9. **Override audit:** log every Grok override + `override_reason`; review until
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
2. **Resolved.** The 4-preset oracle base *is* R_w — the section reward
   re-aggregated by `target_words` — but near-ties additionally use the S3/S4/S5
   *text-signal* tiebreakers and four manual overrides. Those tiebreakers are
   **training-only** (they read per-arm articles), which is exactly why §0.5 maps
   them to inference proxies rather than reusing them in the aggregator.
3. Where should the shared digest-parsing helpers live — `training/_digest_parse.py`
   imported by both `mcp_server` and `training`, or duplicated? (Recommendation:
   shared module to prevent drift, mirroring `_rl_preset.py`.)
