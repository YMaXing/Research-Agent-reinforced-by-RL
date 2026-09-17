# Test-Set Build Plan — Exploration-Preset Prediction Pipeline

Status: **Draft for review**
Owner: (you)
Scope: Build a labelled, stratified **test set of ~12 articles** to evaluate the
RL (Qwen3-4B) + Grok 4.2 exploration-preset prediction pipeline that was trained
on 24 article-variants (8 articles × {minimal, standard, demanding}).

---

## 0. TL;DR — the one thing not in the original framing

The original message describes building *inputs* (guidelines from scraped ground
truth). The hard part of a **test set** is not the inputs — it is the **labels**.

To measure top-1 accuracy you need an `article_oracle.json` per test article, and
that oracle is *empirically derived* from running the full multi-arm pipeline:

```
research × 4 presets  →  writing × 4 presets × 3 runs  →  grading × 12  →  episode oracle  →  article oracle
```

So each "test article" costs roughly **4 research runs + 12 writing runs + 12
grading runs** before it produces a single label. For 12 articles that is on the
order of **~48 research / ~144 writing / ~144 grading** runs. Budget for the
*labelling* pipeline explicitly — it dominates everything else. Section 4 covers
gold vs. silver labelling strategies to control that cost.

Everything else in this plan exists to make those labels (a) correct, (b)
**stratified across all 4 presets** (the actual point of the test set per
[presentations.md](../../../../presentations.md) §9 — the data bottleneck is the
binding constraint), and (c) leakage-free.

---

## 1. Background — how a label is produced (so we know what the test set needs)

The action space is 4 arms (see [_rl_preset.py](_rl_preset.py) and
[compute_article_oracle.py](compute_article_oracle.py)):

| Arm idx | Name | Episode preset | Exploration rounds |
|:--:|:--|:--:|:--:|
| 0 | skip | preset 0 | 0 |
| 1 | light | preset 1 | 1 (balanced) |
| 2 | standard | preset 3 | 2 (depth → breadth) |
| 3 | deep | preset 5 | 3 (depth → breadth → depth) |

Per-article artefacts and the scripts that produce them:

| Artefact | Produced by | Consumed by |
|:--|:--|:--|
| `article_ground_truth.md` | scrape source | grader (FollowsGT / UserIntent) |
| `article_guideline.md` | [generate_article_guideline.py](../../writing_workflow/generate_article_guideline.py) + hand-edit | research, writing, digest |
| `.research/` + `research.md` (×4 presets) | [rl_data_generator.py](rl_data_generator.py) | digest, writing |
| `research_digest.md`, `guideline_features.json`, heuristic `section_oracle.json` | [generate_digests.py](generate_digests.py) | RL inference, oracle weighting |
| `article.md` + `article_00{0,1,2}.md` (×4 presets) | [rl_writing_generator.py](../../writing_workflow/rl_writing_generator.py) | grading |
| `scores.json`, `reasoning.json` (×4 presets) | [rl_grading_generator.py](../../writing_workflow/rl_grading_generator.py) | episode oracle |
| `section_oracle.json` (v2, true per-arm rewards) | [generate_episode_oracles.py](generate_episode_oracles.py) | article oracle |
| `article_oracle.json` (**the label**) | [compute_article_oracle.py](compute_article_oracle.py) | eval |
| predicted preset | [predict_exploration_preset_tool.py](../mcp_server/src/tools/predict_exploration_preset_tool.py) / [infer.py](infer.py) | eval |
| accuracy / regret | [eval_accuracy.py](eval_accuracy.py) (needs update) | report |

Key reward facts that shape test-set design:
- The grader scores the generated article **against `article_ground_truth.md`**
  on 9 dimensions (6 FollowsGT + 3 UserIntent). **Ground-truth quality directly
  determines label quality.**
- The reward favours cheap arms; the 24-variant training oracle skews
  `skip≈8 / light≈11 / standard≈3 / deep≈2`. Standard/deep are rare → the model
  under-fits them → the test set must *over-sample* them to be informative.
- Oracle decisions are often **near-ties** (`EPS_BAND = 0.02`). Labels carry
  noise; `margin` and `needs_review` must be recorded and reported.
- `external_evidence_policy` ∈ {allowed, forbidden, required} is a **hard guard**
  (forbidden → P0; required → ≥P1) applied deterministically after Grok. Setting
  this per article is a lever on the achievable label.

---

## 2. Q1 — Sources of test data & what to watch when selecting

### 2.1 Two tiers, deliberately

1. **In-distribution held-outs (same Agentic-AI course)** — measures
   generalisation to *unseen topics, same format/grader/digest assumptions*.
   Ready-made candidates already in the eval dataset but **not** in training:
   - `04_structured_outputs`
   - `07_reasoning_planning`
   - `13_agent_framework` (partially present in `bases/` — verify state)
   These already have `article_ground_truth.md` and fit the lesson template, so
   they are the cheapest, lowest-risk additions and isolate "new topic" from
   "new format". **Use all available held-out course lessons first.**

2. **Out-of-distribution (broader AI/ML/science-tech)** — measures robustness to
   topic/style drift (blog posts, survey papers, docs, deep-dives). Higher
   scientific value, higher friction (Section 2.3).

Suggested split for ~12: **~5–6 same-course held-outs** + **~6–7 external**.

### 2.2 What to pay attention to when selecting (selection rubric)

- **Stratify by *expected* oracle preset, not by topic.** Before committing,
  estimate each candidate's likely arm from two signals: (a) **topic maturity**
  — stable, well-documented topics (→ skip/light) vs. fast-moving / sparsely
  documented / research-frontier topics (→ standard/deep); (b) **guideline
  depth/breadth demand** you intend to author (Section 3.3). Aim for roughly
  **3 per arm** so every arm has support. Stratification is the single most
  important selection criterion.
- **Ground-truth availability and quality.** The source must be a *complete,
  high-quality, self-contained* article you can scrape cleanly. Avoid paywalled,
  JS-only, or thin pages. The grader compares against it verbatim — a weak
  ground truth yields a meaningless label.
- **Scrapeability.** Prefer sources the existing scrapers handle (static HTML,
  arXiv, GitHub, YouTube). Pre-seed un-scrapeable domains exactly as training did
  (the `rl_data_generator` pre-seed mechanism for substack/x.com). Note the
  scrape date + URL in the manifest.
- **Length diversity.** Mix short (~2.5k words) and long (~5k+ words). Section
  count and `target_words` drive section weighting in the oracle, so length
  affects which arm wins.
- **`external_evidence_policy` diversity.** Include at least one
  `forbidden` (self-contained, citation-free) and one `required`
  (evidence-heavy) so the hard policy guards are exercised on the test set.
- **No training overlap / no few-shot leakage.** Reject any candidate whose
  topic substantially overlaps a training article (02,03,05,06,08,09,10,11), and
  **never use a test article as a few-shot example** in guideline synthesis
  (Section 5).
- **Topic diversity within external tier.** Spread across subfields (e.g.
  classical ML, systems, theory, applied science) rather than 6 LLM-agent posts,
  so "OOD" actually tests breadth.

### 2.3 Watch-outs specific to *external* (non-course) sources

The synthesizer, digest, and grader all assume a **course "lesson" framing**
(`## Global Context`, `## Anchoring the Lesson in the Course`, `## Section N -
Title`, `## Golden Sources`). External articles have no course position. Decide
per article:
- **Option A (recommended):** fabricate plausible course-anchoring (invent a
  lesson number, neighbouring-lesson callbacks) so the template stays valid and
  comparable to training inputs.
- **Option B:** adapt the template — but then the digest/grader distribution
  shifts and results are not directly comparable. Only do this if "format
  robustness" is an explicit research question, and report it separately.

Either way, **preserve the canonical section headings and `**Section length:** N
words` lines** — section IDs (`S1::...`), `target_words`, and oracle weighting
all parse from them.

---

## 3. Q2 — How to process each article (end-to-end recipe)

Per-article pipeline. Commands assume `cd research_agent_local/` (research/digest/
oracle/eval) and `cd writing_workflow/` (guideline/writing/grading) as noted.

### 3.1 Step 0 — Acquire ground truth
- Scrape the source → `inputs/evals/dataset/data/<article>/article_ground_truth.md`.
- Record URL, scrape date, license/usage note in the manifest (Section 7).

### 3.2 Step 1 — Extract a planning brief
```bash
# writing_workflow/
uv run python generate_article_guideline.py --from-article <article>
# → inputs/briefs/<article>.yaml   (REVIEW the YAML before continuing)
```
Review the extracted brief: fix `lesson_scope`, `concepts_from/for_*`,
`theory_practice_ratio`, and per-section `target_words` / `key_points` /
`diagrams`. This is where you encode intended difficulty.

### 3.3 Step 2 — Synthesize + hand-edit the guideline (the label lever)
```bash
# writing_workflow/ — IMPORTANT: keep few-shot pool free of test articles
uv run python generate_article_guideline.py --article <article> \
    --few-shot 03_context_engineering 08_react_practice
# → inputs/evals/dataset/data/<article>/article_guideline.md
```
Then **hand-edit** to deliberately set the article's exploration demand:
- `must_cover_depth`, `mandatory_bullets`, `target_words` per section,
- breadth cues (adjacent concepts, cross-domain, history) if you want depth/deep,
- `external_evidence_policy` (allowed/forbidden/required),
- Golden Sources list (verbatim from the brief — never invent URLs).

Document the *intended* arm per article so you can later compare intent vs. the
empirical oracle (a useful sanity check on the whole pipeline).

### 3.4 Step 3 — Research at all 4 arms (Phase 1)
```bash
# research_agent_local/
uv run --project mcp_server python rl_data_generator.py \
    --articles <article> --presets 0 1 3 5
```
Use the **same exploitation settings as training** (3 rounds, 5 queries/round,
same scrapers + pre-seeding) so the digest distribution matches. Confirm
`.research/` populates and `research.md` is written for each preset.
> Note: `rl_data_generator.py` hard-codes `TRAIN_ARTICLES`. Add the test slugs to
> a new `TEST_ARTICLES` list (or pass `--articles`) — verify the slug resolves to
> the eval-dataset folder and that no-variant slugs work.

### 3.5 Step 4 — Digest + features (Phase 2c)
```bash
# research_agent_local/
uv run --project mcp_client python training/generate_digests.py --articles <article>
# → bases/<article>/research_digest.md, guideline_features.json, section_oracle.json (heuristic)
```

### 3.6 Step 5 — Writing ×3 per arm (Phase 2a)
```bash
# writing_workflow/
uv run python rl_writing_generator.py --articles <article> --presets 0 1 3 5
# → episodes/<article>__preset{0,1,3,5}/article_00{0,1,2}.md + article.md
```

### 3.7 Step 6 — Grading (Phase 2b)
```bash
# writing_workflow/
uv run python rl_grading_generator.py --articles <article> --presets 0 1 3 5
# → episodes/<article>__preset{0,1,3,5}/scores.json, reasoning.json
```

### 3.8 Step 7 — Episode oracle → article oracle (the label)
```bash
# research_agent_local/
uv run python training/generate_episode_oracles.py --articles <article>
# → bases/<article>/section_oracle.json (v2 per-arm rewards, overwrites heuristic)

# Optional but recommended for new articles (near-tie signal breakdown):
uv run python training/prototype_oracle_signals.py --article <article>

uv run python training/compute_article_oracle.py --article <article>
# → bases/<article>/article_oracle.json  (oracle_arm_idx = the label)
```
> `compute_article_oracle.py` contains **manual overrides hard-coded for the 24
> training variants**. For test articles, do **not** reuse those overrides; run
> `prototype_oracle_signals.py` first and only add an override after manual
> review. Record `margin`, `reward_spread`, `needs_review` per article.

### 3.9 Step 8 — Inference + evaluation
Run the pipeline in all three modes and compare to `oracle_arm_idx`:
- **RL-only** (`rl_only=True`),
- **Grok-only** (`grok_only=True`),
- **RL+Grok** (full).

See Section 6 for the harness + metrics.

---

## 4. Oracle labelling strategy — gold vs. silver (cost control)

Full 4-arm labelling is expensive. Three options, recommend a **hybrid**:

| Strategy | Cost / article | Label quality | When |
|:--|:--|:--|:--|
| **Gold** — full 4-arm research+write×3+grade+oracle | High (~28 runs) | Highest (empirical) | Core stratified subset (≥6–8 articles incl. all 4 arms) |
| **Silver-heuristic** — stop after digest; use `generate_digests.py` 2D `section_oracle.json` only | Low (4 research + digest) | Approximate | Quick coverage / triage |
| **Expert** — human reads guideline + digest, assigns arm | Lowest | Subjective, independent | Cross-check on *all* articles |

**Recommended hybrid:**
1. Gold-label a **stratified core** of ~8 (2 per arm) — this is the headline
   metric.
2. Expert-label **all 12** independently (before seeing gold) — measures
   human–oracle agreement and flags suspect gold labels.
3. Optionally silver-label the remaining ~4 for cheap directional coverage,
   clearly marked as silver in the manifest and reported separately.

Reduce writing variance cost: writing ×3 estimates stability (S5). If budget is
tight, ×2 still gives a CV; never ×1 (no variance estimate, S5 tiebreaker dies).

---

## 5. Leakage & quality controls (must-pass gates)

- **Few-shot isolation:** the synthesizer's few-shot pool must contain **only
  training articles** (default `03_context_engineering`, `08_react_practice`).
  Never pass a test slug to `--few-shot`. Confirm `run_pipeline` strips the
  target from the pool.
- **Topic non-overlap:** reject candidates overlapping 02,03,05,06,08,09,10,11.
- **Ground-truth provenance:** the scraped source must be a real published
  article not already in any training `.research/` corpus (avoid the model having
  "seen" it). Spot-check that golden/Tavily sources for the test article don't
  literally include the ground-truth URL.
- **Format validity:** guideline must pass the synthesizer's structural checks
  (`## Section N - Title`, `**Section length:** N words`, Golden Sources present);
  digest must parse `<gap_profile>` with `target_words`. Run a dry inference to
  confirm the digest yields per-section signals.
- **Determinism of settings:** pin Qwen checkpoint, Grok model name, digest
  settings, exploitation rounds. Record them in the manifest.

---

## 6. Evaluation harness & metrics

### 6.1 Harness — use `test_grok_planner.py`, NOT `eval_accuracy.py`
**`eval_accuracy.py` is retired — do not resurrect it.** It is stale on every
axis: 6-preset reward formula, reads dead oracle keys (`oracle_preset` /
`article_rewards`, removed in the v2 schema — so it `KeyError`s against current
oracles), only 7 base lessons, recomputes the oracle inline instead of reading
the canonical `article_oracle.json`, and tests the raw section model rather than
the production RL→Grok pipeline.

The current, canonical harness is
[test_grok_planner.py](../evaluation/test_grok_planner.py). It **already**:
- is 4-preset and reads `oracle_arm_idx` / `r_w_rewards_list` from
  `article_oracle.json` (v2),
- calls the production `predict_exploration_preset` tool via MCP (RL → Grok),
- supports all four modes: default (RL+Grok), `--rl-only`, `--rl-guards-only`,
  `--grok-only`,
- reports exact/near/miss + reward-regret, and **excludes forbidden-policy
  articles from the regret aggregate**.

**Test-set work item = extend it, don't rewrite.** Add a held-out `TEST_LESSONS`
set of **no-variant** slugs alongside `_TRAIN_LESSONS`; let `_expand_articles`
pass no-variant test slugs through untouched (skip the ×3 variant expansion for
them); split the summary into TRAIN vs TEST; add a 4×4 confusion matrix +
majority/random baselines. The oracle reader, mode flags, and regret logic work
as-is. Emit a markdown table mirroring
[presentations.md](../../../../presentations.md) §7.

### 6.2 Metrics to report
- **EXACT / NEAR(±1) / MISS(≥2)** counts and rates (primary, matches existing
  vocabulary).
- **Ordinal MAE** `mean |p_chosen − p*|`.
- **Regret ΔR** `R(p*) − R(p_chosen)` using the per-arm rewards already computed
  for the oracle — the most decision-relevant metric (a 1-preset miss can be
  cheap or catastrophic; ΔR captures that, accuracy doesn't).
- **Per-arm confusion matrix** (4×4) — exposes systematic over/under-exploration.
- **Baselines for context:** majority-class (predict the train-modal arm) and
  random — accuracy is only meaningful relative to these.
- **Stratified reporting:** metrics broken down by oracle arm and by tier
  (course held-out vs. external), plus a separate line for `needs_review` /
  low-margin articles.
- **Marginal contribution:** RL+Grok vs. RL-only vs. Grok-only deltas (the n=3
  comparison in §7 was inconclusive; ~12 stratified articles is the point).

### 6.3 Statistical caveats
n≈12 is far better than n=3 but still modest; report per-arm n and treat
single-arm cells as anecdotal. State the sample size up front in any results
table (per the §9 caveat in presentations.md).

---

## 7. Manifest (provenance & reproducibility)

Maintain `rl_training_data/test_set_manifest.json` (or `.md`) with one row per
article:

```jsonc
{
  "article": "14_<slug>",
  "tier": "course_holdout | external",
  "source_url": "https://…",
  "scrape_date": "2026-06-08",
  "license_note": "…",
  "intended_arm": "standard",            // from guideline design (Section 3.3)
  "external_evidence_policy": "allowed",
  "label_strategy": "gold | silver | expert",
  "oracle_arm_idx": 2,                    // from article_oracle.json
  "oracle_margin": 0.041,
  "reward_spread": 0.18,
  "needs_review": false,
  "n_sections": 6,
  "few_shot_used": ["03_context_engineering", "08_react_practice"],
  "qwen_checkpoint": "task_…/best",
  "grok_model": "grok-4.2",
  "digest_settings": {"exploit_rounds": 3, "queries_per_round": 5}
}
```

---

## 8. Other aspects to watch (Q3 — beyond the original framing)

1. **Labels are the deliverable, not inputs** (Section 0/4) — plan compute first.
2. **Stratify by oracle arm**, over-sample standard/deep (Section 2.2).
3. **Near-tie label noise** — record margins, prefer ΔR/ordinal over exact
   accuracy, flag/segregate `needs_review` items (Section 1, 6).
4. **Guideline editing controls the label** — design depth/breadth/policy
   deliberately; log intended-vs-oracle arm (Section 3.3).
5. **Course-framing assumption for external articles** — keep canonical headings;
   fabricate course-anchoring or report format-robustness separately (Section 2.3).
6. **Research-setting parity** — identical exploitation config to training, else
   the digest (the RL input) is out of distribution (Section 3.4).
7. **Script hard-coding** — `rl_data_generator.py`, `generate_episode_oracles.py`,
   and `compute_article_oracle.py` (manual overrides) assume the 24-variant set
   and each needs a test-aware path. The eval harness is `test_grok_planner.py`
   (extend with a no-variant `TEST_LESSONS` set); **`eval_accuracy.py` is
   retired** (Section 3, 6).
8. **Pre-seeding** for un-scrapeable domains, same as training.
9. **Reproducibility manifest** — pin model versions + settings (Section 7).
10. **Statistical honesty** — report n per arm and baselines (Section 6.3).

---

## 9. Work-item checklist

- [ ] Finalise candidate list (draft in **Appendix A**): stratified ~3/arm.
- [ ] Confirm/scrape `article_ground_truth.md` for each; record provenance.
- [ ] Add `TEST_ARTICLES` lists (no-variant) to `rl_data_generator.py` and
      `generate_episode_oracles.py`; add `TEST_LESSONS` to `test_grok_planner.py`.
- [ ] Per article: brief → guideline (edit) → research×4 → digest → write×3 →
      grade → episode oracle → article oracle.
- [ ] Run `prototype_oracle_signals.py` per article; review near-ties; record
      margin / needs_review (do **not** reuse the 24-set manual overrides).
- [ ] Gold-label stratified core (≥8); expert-label all 12; silver the rest.
- [ ] Extend `test_grok_planner.py` (no-variant `TEST_LESSONS`, TRAIN/TEST split,
      4×4 confusion + majority/random baselines). **Do not** revive
      `eval_accuracy.py`.
- [ ] Produce stratified results report; update `presentations.md` §7.
- [ ] Write `test_set_manifest.json`.

## 10. Suggested milestones

1. **M1 — Inputs ready (cheap):** candidates picked, ground truth scraped,
   guidelines synthesized + edited, manifest skeleton. (No GPU/LLM-heavy runs.)
2. **M2 — One gold article end-to-end:** prove the full pipeline + updated eval
   harness on a single course held-out before scaling.
3. **M3 — Gold core (≥8, all 4 arms):** stratified labels + first real metrics.
4. **M4 — Full set (~12) + expert cross-check + report.**

---

## Appendix A — Candidate list (draft v1)

**Read this first.** “Expected arm” is a *design target*, not the label. The label
is whatever the oracle returns after full 4-arm labelling. You hit a target arm
with **two levers**: (a) **topic maturity** — pick genuinely saturated topics for
the cheap arms and genuinely frontier/sparse topics for the expensive arms
(the honest lever); (b) **guideline design** (§3.3) — depth/breadth demand +
`external_evidence_policy` to fine-tune. Editing a frontier guideline “down” to
P0 is artificial — prefer real saturated topics for skip/light, because the
whole point of those rows is to probe the model's documented **over-exploration
bias** on P0/P1-oracle articles.

Target: **~3 per arm** so every arm has support. Training is starved of
standard/deep (3 and 2 articles) **and** has no clean P0/P1 held-outs — both
ends matter.

| # | Article / topic | Tier | Source / status | Target arm | Why this arm |
|:--:|:--|:--|:--|:--:|:--|
| 1 | `04_structured_outputs` | course | **ready** (GT+guideline+research exist⁰) | **P0 skip** | JSON-schema / Pydantic / function-calling is exhaustively documented — little marginal value from exploration; probes over-exploration. |
| 2 | The Illustrated Transformer (architecture explainer) | external | scrape (static blog) | **P0 skip** | Canonical, saturated topic; nothing new to find. Classic over-exploration trap. |
| 3 | Backpropagation / gradient-descent fundamentals | external | scrape (static blog) | **P0 skip** | Decade-stable foundational topic → zero exploration upside. |
| 4 | `07_reasoning_planning` | course | **ready** (GT+guideline+research exist⁰) | **P1 light** | ReAct / Plan-and-Execute are established; modest depth. ⚠️ partial overlap with training `08_react_practice` (ReAct) — not a *clean* unseen topic; see notes. |
| 5 | Course overview lesson (e.g. `01` intro or `12` capstone¹) | course | scrape² | **P1 light** | Orientation/overview lessons have low research demand. |
| 6 | Word/sentence embeddings explainer (e.g. Illustrated Word2Vec) | external | scrape (static blog) | **P1 light** | Well-documented, stable → one balanced round suffices. |
| 7 | Model quantization / compression (GPTQ/AWQ/bitsandbytes) | external | scrape (HF blog / Raschka) | **P2 standard** | Established but actively refined → 1–2 depth rounds add real value. |
| 8 | LLM evaluation & benchmarking methodology | external | scrape (blog/survey) | **P2 standard** | Fragmented, evolving best practices → depth + breadth. |
| 9 | AI-for-science deep-dive w/ stable anchor (e.g. AlphaFold) | external | scrape (Quanta / paper) | **P2 standard** | Needs breadth into adjacent science + some depth. (border P2/P3) |
| 10 | `13_agent_framework` | course | **GT only** (needs guideline+research) | **P3 deep** | Fast-moving framework comparison (LangGraph/CrewAI/PydanticAI/…) — breadth + depth + currency. |
| 11 | Recent (2025–26) arXiv **survey** on a frontier topic³ | external | scrape (arxiv2markdown) | **P3 deep** | Sparse, fast-moving → maximal exploration. Pick a *survey* so there is breadth to explore. |
| 12 | Emerging-technique deep-dive w/ sparse docs | external | scrape (blog + primary paper) | **P3 deep** | Little consolidated coverage → deep exploration justified. |

⁰ The existing `04`/`07` `article_guideline.md` + `research.md` are from the
**pre-RL eval dataset** (single research, possibly hand-written guideline).
**Do not reuse them as labelling inputs** — regenerate the guideline via the
synthesizer and re-run the 4-arm research for parity with training.

¹ L13's intro references L12 as the capstone-overview lesson. Verify which course
lessons beyond 04/07/13 are published and scrapeable (likely `01`, `12`, `14`+)
and that they don't overlap a training topic.

² Only **3** clean-ish course held-outs exist in the dataset today (04, 07*, 13).
To raise the course share to ~5–6 (lower-risk: same grader/digest distribution),
scrape additional published course lessons. Otherwise run **3 course + 9
external**.

³ Frontier-topic ideas that don't overlap training: test-time compute / inference
scaling, reasoning-RL, diffusion language models, world models, state-space
models. Confirm recency and that a high-quality self-contained survey exists.

### A.1 Overlap / leakage check
Training topics = agents/workflows, context engineering, workflow patterns,
tools, ReAct, RAG, memory, multimodal. Every external above (transformer arch,
backprop, embeddings, quantization, evaluation, AI-for-science, frontier survey,
emerging technique) is **outside** that set. **One caveat:** course candidate
`07_reasoning_planning` partially overlaps training `08_react_practice` (both
cover ReAct). It still tests a distinct, broader guideline, but it is *not* a
clean “unseen topic” — either accept it as a *near-distribution* held-out (and
label it as such in the manifest) or swap it for an external P1 if you want all
test topics strictly unseen.

### A.2 Source-quality guidance for externals
- Prefer **static-HTML / arXiv / well-known long-form blogs** the scrapers
  already handle; **pre-seed** JS-only or paywalled sources exactly as training
  did. Record URL + scrape date + license in the manifest.
- Blog families that are static, self-contained, and close to the lesson format:
  Jay Alammar (`jalammar.github.io`), Lilian Weng (`lilianweng.github.io`),
  Sebastian Raschka (“Ahead of AI”), the Hugging Face blog, and Quanta Magazine
  for science explainers. **Verify exact URLs/licenses at scrape time** — do not
  assume any specific article still exists.
- For the P3 arXiv rows, pick **surveys** (broad reference lists → explorable
  breadth), not single-result papers.

### A.3 Guaranteeing arm coverage via guideline knobs
Independently of topic, ensure the policy guards are exercised: design **≥1
`forbidden`** article (self-contained, citation-free → forced P0 guard) and
**≥1 `required`** article (evidence-heavy → forced ≥P1 guard). Log the
*intended* arm per article in the manifest and compare it against the empirical
oracle as a sanity check on the whole pipeline.
