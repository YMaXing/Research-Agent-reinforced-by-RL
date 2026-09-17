# RL Training Data (`rl_training_data`)

The offline artifacts behind the RL exploration-preset policy: per-article
inputs, generated episodes, reward labels, trained checkpoints, and the
research log documenting how the reward formula got calibrated. Nothing in
this directory is code — see
[`../research_agent_local/training/README.md`](../research_agent_local/training/README.md)
for the scripts that read/write it, and
[`../research_agent_local/evaluation/README.md`](../research_agent_local/evaluation/README.md)
for the harness that scores a checkpoint against it.

**Dataset split**: 24 TRAIN article-variants (8 lessons × `var_minimal`/
`var_standard`/`var_demanding`) used for GRPO training, plus 16 held-out TEST
articles (no variant expansion) never seen during training.

## Contents

- [Layout](#layout)
- [`bases/` — per-article static inputs and reward labels](#bases--per-article-static-inputs-and-reward-labels)
- [`episodes/` / `test_episodes/` — generated (article × preset) drafts](#episodes--test_episodes--generated-article--preset-drafts)
- [`checkpoints/` — GRPO training runs](#checkpoints--grpo-training-runs)
- [`oracle_review/` — human near-tie reviews](#oracle_review--human-near-tie-reviews)
- [`pairwise/` — reward-calibration A/B judging data](#pairwise--reward-calibration-ab-judging-data)
- [`rl_planner_test_results/` — eval results + the research log](#rl_planner_test_results--eval-results--the-research-log)
- [What's gitignored](#whats-gitignored)

---

## Layout

```
rl_training_data/
├── bases/                    # gitignored — per-article inputs + reward labels
├── episodes/                 # gitignored — TRAIN generated episodes (24 article-variants)
├── test_episodes/            # tracked    — TEST generated episodes (16 held-out articles)
├── checkpoints/               # gitignored — GRPO training run outputs
├── oracle_review/             # tracked    — human-readable near-tie review reports
├── pairwise/                  # tracked    — pairwise A/B judging data (reward calibration)
└── rl_planner_test_results/   # tracked    — eval results + analysis_document.md
```

---

## `bases/` — per-article static inputs and reward labels

One directory per article-variant (e.g. `09_RAG__var_standard/`, or a bare
lesson name like `04_structured_outputs/` for TEST articles — no variant
suffix). Each contains:

| File | Produced by | Contents |
|---|---|---|
| `article_guideline.md` | (authored/synthesized) | The guideline the whole pipeline works from. |
| `.research/` | `research_agent_local` workflow | Raw exploitation-phase scraped sources. |
| `guideline_features.json` | `rl_inference_service/generate_digests.py` | `external_evidence_policy` (`allowed`/`forbidden`/`required`/`capped`) + per-section `target_words` etc. |
| `research_digest.md` | `rl_inference_service/generate_digests.py` | The structured digest the RL policy actually reads — see [rl_inference_service/README.md](../research_agent_local/rl_inference_service/README.md#what-signals-feed-the-rl-model). |
| `section_oracle.json` | `training/pipeline/generate_episode_oracles.py` | Per-section, per-arm rewards (single production draw) — the GRPO training target. |
| `section_oracle_averaged.json` | `training/pipeline/merge_replicate_oracles.py` | Same, averaged across N replicate draws where replication was run. |
| `article_oracle.json` | `training/pipeline/compute_article_oracle.py` | Article-level `oracle_arm` (+ `margin`, `tied_arms` where applicable) — the eval harness's ground truth. |
| `article_oracle_prior.json` | (legacy, pre-4-preset era) | Superseded; not read by any current script. |
| `digest_section_placeholder.json` | `rl_inference_service/generate_digests.py` | Diagnostic-only digest-stage heuristic; never the reward target (kept in a distinct filename specifically to avoid colliding with `section_oracle.json`). |

## `episodes/` / `test_episodes/` — generated `(article × preset)` drafts

Each subdirectory is `<article>__preset<N>/` (production draw) or
`<article>__replicate<M>__preset<N>/` (a replicate draw, temperature 0.7,
same inputs), containing `research.md`, `article.md`, `scores.json` (9
graded dimensions — see
[`../writing_workflow/EVALS.md`](../writing_workflow/EVALS.md)), and
`reasoning.json` (the judge's free-text per-dimension reasoning, including
the `[instances=N; quality=...]` enhancement tags).

- **`episodes/`** (TRAIN, 24 article-variants): presets `{0,1,3,5}` map to
  `{skip, light, standard, deep}` — presets `2` and `4` are archived,
  historical artifacts from an earlier 6-preset scheme and are not read by
  any current script. Also holds `_noise_replication/` (older noise-floor
  experiment data, relocated here since it holds TRAIN-article replicates).
- **`test_episodes/`** (TEST, 16 held-out articles): presets `0`–`3` map
  directly to `{skip, light, standard, deep}` — no gap, since this split was
  never part of the old 6-preset scheme. Some heavily-contested near-tie
  articles (e.g. `Dark_Dimension`, `29_evaluation_metrics`) have up to 7
  replicate draws rather than the usual 2, from targeted N=5+ expansion.

## `checkpoints/` — GRPO training runs

`checkpoints/tasks/<task-id>/{best, epoch_*, latest}/` — one subdirectory per
training run, written by `training/pipeline/train_grpo.py`. The run that
produced the current production checkpoint is `run33_averaged_confidence/`;
its `best/` was **copied** (not moved — this directory remains the full
historical record) to
`research_agent_local/rl_inference_service/checkpoints/production/`, which is
what actually serves in production.

## `oracle_review/` — human near-tie reviews

One markdown report per article whose oracle label was thin enough to
warrant a manual look (generated by
`training/analysis/review_near_tie.py --save`), each with a per-section
reward-contribution breakdown and a dated "Reviewer conclusion" section
recording the KEEP / FLIP / override decision and its statistical basis
(per-draw margins, a Student-t p-value, or a cited structural argument).
Directly informs `compute_article_oracle.py`'s `_MANUAL_OVERRIDES`/
`_TIED_ARMS` registries.

## `pairwise/` — reward-calibration A/B judging data

`pairwise/{pilot, lightstd_scale, stddeep_scale}/<article>/` — direct A/B
section-comparison judgments (`PairwiseEnhancementJudgment`, see
[`../writing_workflow/EVALS.md`](../writing_workflow/EVALS.md#pairwiseenhancementjudgment--calibration-only-not-production))
used to calibrate the `enhancement_credit()` curve in
`training/pipeline/enhancement_reward.py` — not consumed by the production
reward pipeline itself, only by the `training/analysis/` calibration scripts.

## `rl_planner_test_results/` — eval results + the research log

See its own [README.md](rl_planner_test_results/README.md) — this is where
[the top-level Results section](../../README.md#results-rlguards-vs-baselines)'s
numbers come from, and where the full multi-week calibration investigation
is written up.

---

## What's gitignored

`bases/`, `episodes/`, and `checkpoints/` are excluded from version control
(regeneratable, and large — scraped source text and model weights). Notably
**`test_episodes/` is tracked** despite being generated data — the held-out
benchmark is small and valuable enough to version directly rather than
requiring a full regeneration to reproduce eval results.
