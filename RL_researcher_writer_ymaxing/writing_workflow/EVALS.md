# Evaluation Framework (`writing_workflow` evals)

This document covers `src/brown/evals/` — the LLM-as-judge grading metrics
that score generated articles. The same metric classes are used by **two
different consumers** for two different purposes; understanding that split
is the key to this whole subsystem.

For the terminal commands to *run* Brown's own workflows, see the main
[README.md](README.md). For how the numbers documented here become the GRPO
reward, see
[`../research_agent_local/training/README.md`](../research_agent_local/training/README.md#the-production-reward-formula).

---

## Contents

- [Two consumers, one set of metrics](#two-consumers-one-set-of-metrics)
- [`FollowsGTMetric` — 6 dimensions, 2 passes](#followsgtmetric--6-dimensions-2-passes)
- [`UserIntentMetric` — 3 dimensions](#userintentmetric--3-dimensions)
- [`PairwiseEnhancementJudgment` — calibration-only, not production](#pairwiseenhancementjudgment--calibration-only-not-production)
- [How grading feeds the RL reward](#how-grading-feeds-the-rl-reward)
- [Judge model configuration](#judge-model-configuration)
- [Robustness details worth knowing](#robustness-details-worth-knowing)
- [Running the standalone quality eval](#running-the-standalone-quality-eval)
- [Running Phase 2b grading](#running-phase-2b-grading)

---

## Two consumers, one set of metrics

| Consumer | Purpose | Entry point |
|---|---|---|
| **Standalone quality eval** | One-off check: does Brown's output plausibly follow ground truth? Opik-tracked, dataset-based. | `make brown-create-eval-dataset` + `make brown-run-eval` (§6.5 of the main README) |
| **RL reward labeling (Phase 2b)** | Grade every `(article × preset)` episode's `article.md` on all 9 dimensions, feeding the offline GRPO reward formula. | [`rl_pipeline/rl_grading_generator.py`](rl_pipeline/rl_grading_generator.py) |

Both call the exact same `FollowsGTMetric`/`UserIntentMetric` classes under
`src/brown/evals/metrics/` — there is only one grading implementation, not
two. The standalone eval is a lighter-weight sanity check (usually just
`follows_gt`, on whatever articles are in `inputs/evals/dataset/`); Phase 2b
is the real, corpus-wide, 9-dimension grading pass whose output
(`scores.json` + `reasoning.json` per episode) is what actually trains the
RL policy.

---

## `FollowsGTMetric` — 6 dimensions, 2 passes

`src/brown/evals/metrics/new_follows_gt/`. Scores a generated article against
its ground-truth article, section by section, on:

| Dimension | Abbrev. | What it checks |
|---|---|---|
| `core_content` | `cc` | Every idea from the GT section is present (possibly reworded/reordered). |
| `flow` | `fl` | Logical progression isn't disrupted — reordering alone doesn't fail this; only genuine incoherence does (prerequisite-after-dependent, broken transitions, circular reasoning). |
| `structure` | `st` | Internal formatting (headings, lists, tables) matches expectations. Graded, but **not** part of the RL reward formula. |
| `depth_enhancement` | `de` | Valuable *depth* additions traceable to an exploration-phase source (inward: technical nuances, failure modes, implementation detail). |
| `breadth_enhancement` | `be` | Valuable *breadth* additions traceable to an exploration-phase source (outward: adjacent concepts, cross-domain analogies). |
| `core_preservation` | `cp` | The section didn't lose its topical identity to an addition — reserved for genuine identity shift, not just "the addition is long". |

**Two-pass grading** (`FollowsGTMetric.ascore()`): pass 1 scores
`core_content`/`flow`/`structure`/`depth_enhancement`/`breadth_enhancement`
in one structured-output call; pass 2 scores `core_preservation` in a
*separate* call that receives pass 1's `core_content`/`flow` results as
context (mirroring how a human reviewer would check preservation only after
confirming the core idea itself survived). The pass-1 placeholder for
`core_preservation` is always overwritten with the real pass-2 score before
`ascore()` returns.

**Depth/breadth are hard-zeroed, not just discouraged, when there's nothing
to trace to**: if the episode has no exploration-phase sources at all
(`skip` preset, 0 exploration rounds), `depth_enhancement`/`breadth_enhancement`
are forced to `0` for every section *after* pass 1 returns, overriding
whatever the judge said — this is a code-level mandate (not just a prompt
instruction), applied before pass 2 runs so pass 2 sees the corrected zeros.

**Instance counting, not just pass/fail**: for `depth_enhancement`/
`breadth_enhancement` specifically, the judge's free-text reason must also
carry a `[instances=N; quality=strong,standard,...]` tag enumerating *every*
qualifying instance (not just the first). The binary `score` field is
unchanged, but `training/pipeline/generate_episode_oracles.py` parses this
tag to compute a richer, saturating credit value — see
[the reward formula](../research_agent_local/training/README.md#the-production-reward-formula).

---

## `UserIntentMetric` — 3 dimensions

`src/brown/evals/metrics/new_user_intent/`. Scores how well a section serves
the *user's* stated intent, independent of the GT article:

| Dimension | Abbrev. | What it checks |
|---|---|---|
| `guideline_adherence` | `ga` | Follows `article_guideline.md`'s explicit requirements (word-count target, required visual elements, mandated sub-topics). |
| `research_anchoring` | `ra` | Claims are actually grounded in `research.md`, not invented. |
| `golden_source_priority` | `gsp` | Prefers golden (guideline-named) sources over Tavily-discovered ones when both cover the same point. |

`guideline_adherence`'s length check uses **deterministic word counting**
(`word_count.py`), not the judge's own count — LLMs are unreliable at
precise long-text counting. `word_count.compute_section_word_counts()`
splits the article by H2 heading, strips fenced code/mermaid blocks, table
rows (but not a table's own title line), image captions/embeds, and citation
markers, then injects an exact `<generated_article_section_word_counts>`
block into the judge's prompt so it only has to *look up* the count.

`research_anchoring` and `golden_source_priority` are graded and stored, but
(as of the C2 reward-formula revision) carry **near-zero weight in the RL
reward** — both were found to be >95% constant corpus-wide, so they're kept
as diagnostic metadata on `article_oracle.json` rather than decision inputs.
`guideline_adherence` is a **soft gate**, not an additive score — see the
reward formula.

---

## `PairwiseEnhancementJudgment` — calibration-only, not production

`src/brown/evals/metrics/pairwise_enhancement/`. A **third**, separate
metric used only by the reward-formula *calibration* investigation, never by
production grading: given two renderings of the same section (e.g. the
`light`-preset and `deep`-preset drafts), it judges depth and breadth
*relative to each other* in one call, rather than scoring each in isolation.
This was how the `enhancement_credit()` curve in
`enhancement_reward.py` was calibrated — direct A/B comparison caught a
systematic over-crediting of `deep` vs. `standard` that absolute (single-draft)
scoring couldn't see on its own (see the reward formula's calibration note).
Driven by `rl_pipeline/rl_pairwise_grading_generator.py` and friends — not
part of the normal Phase 2b grading run.

---

## How grading feeds the RL reward

`rl_pipeline/rl_grading_generator.py` (Phase 2b) runs `FollowsGTMetric` +
`UserIntentMetric` concurrently for every `(article × preset)` episode's
`article.md` against its `article_ground_truth.md`, writing all 9 scores to
`scores.json` (floats) and the judge's per-dimension free-text reasoning to
`reasoning.json`. `research_agent_local/training/pipeline/generate_episode_oracles.py`
reads these to compute the per-section, per-arm reward — see
[the production reward formula](../research_agent_local/training/README.md#the-production-reward-formula)
for exactly which of these 9 dimensions feed the formula (`cc`, `fl`, `de`,
`be`, `cp`, `ga`) vs. which are diagnostic-only (`st`, `ra`, `gsp`).

---

## Judge model configuration

The default judge is **Gemini 2.5 Flash** (`temperature=0.0`,
`thinking_budget=1024`, `max_retries=3` — see `_GRADING_CONFIG` in
`rl_grading_generator.py`). **Claude Sonnet 5** is available as an
alternative judge (`--grading-model claude`), added after repeated manual
correction of Gemini grading mistakes.

Anthropic models need `method="json_schema"` (not the LangChain default
`"function_calling"`) for `with_structured_output()` — `structured_output_kwargs(model)`
picks this automatically for any `anthropic:` model. Without it, Claude's
tool-call encoding was observed to corrupt nested list fields (e.g. a
`sections: list[...]` field silently becoming a JSON-encoded string, a
double-wrapped dict, or JSON with trailing prose appended) across different
calls in ways that are hard to detect from any single response.

---

## Robustness details worth knowing

- **`SectionsCoercionMixin`** (`base.py`) — a defensive Pydantic
  `model_validator` that coerces a malformed `sections` field (any of the
  three corruption shapes above) back into a real list before validation
  fails. Kept as belt-and-suspenders even after switching to
  `method="json_schema"`; any *new* structured-output schema with a
  top-level `sections` field should inherit it too.
- **Fake-model test configs must be kept in sync manually** — `configs/debug.yaml`
  (used by `make`/CI) and `tests/fixtures/configs/mocked.yaml` (used by
  pytest's `conftest.py` fixture) are two independent files with no
  enforcement that they match; adding a new workflow node means updating
  both.
- **Never call `get_app_config()` at module level** — it's `@lru_cache`d, and
  pytest imports every test module (transitively importing production code)
  *before* any fixture runs, permanently caching whatever config was active
  at import time. Always call it lazily, inside the function that needs it.

---

## Running the standalone quality eval

```bash
cd RL_researcher_writer_ymaxing/writing_workflow
make brown-create-eval-dataset   # builds the `brown-course-lessons` dataset from inputs/evals/dataset/
make brown-run-eval              # runs the follows_gt metric, caches results in outputs/evals/
```

## Running Phase 2b grading

See [README.md §7.2](README.md#72-rl_grading_generatorpy--phase-2b-llm-as-judge-grading)
for the full command reference (`rl_pipeline/rl_grading_generator.py`,
`--articles`/`--presets`/`--grading-model`/`--episodes-dir` flags, resumability
via the `scores.json` sentinel).
