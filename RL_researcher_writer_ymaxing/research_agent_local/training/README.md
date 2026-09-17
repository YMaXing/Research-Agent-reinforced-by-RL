# GRPO Training & Reward-Calibration Toolchain (`training`)

The GRPO + QLoRA trainer for the exploration-preset policy, plus the full
offline research toolchain that calibrated its reward formula and audited
label quality. One `uv` project; every script below shares the same `.venv`.

For how a trained checkpoint gets evaluated / shipped to production, see
[../evaluation/README.md](../evaluation/README.md) and
[../rl_inference_service/README.md](../rl_inference_service/README.md).

---

## Contents

- [Layout](#layout)
- [Install](#install)
- [`pipeline/` — the real data → reward → train chain](#pipeline--the-real-data--reward--train-chain)
- [The production reward formula](#the-production-reward-formula)
- [The GRPO training process, and how it differs from standard GRPO](#the-grpo-training-process-and-how-it-differs-from-standard-grpo)
- [`maintenance/` — reusable data-repair scripts](#maintenance--reusable-data-repair-scripts)
- [`analysis/` — 40+ offline research scripts (kept flat)](#analysis--40-offline-research-scripts-kept-flat)
- [Train a new checkpoint](#train-a-new-checkpoint)

---

## Layout

```
training/
├── pipeline/       # 6 files — the chain GRPO training actually consumes
├── maintenance/    # 2 files — reusable, non-one-off data-repair scripts
├── analysis/       # 40+ files — offline reward-calibration / noise / signal-quality research
├── docs/
│   └── test_set_build_plan.md
└── pyproject.toml
```

---

## Install

```bash
uv sync
```

Pulls the same CUDA `torch`/`transformers`/`peft`/`bitsandbytes`/`accelerate`
stack as `rl_inference_service` (both legitimately need it — this venv trains,
`rl_inference_service`'s serves).

---

## `pipeline/` — the real data → reward → train chain

The scripts GRPO training actually depends on, in the order they run:

| Script | Role |
|---|---|
| `rl_data_generator.py` | Phase 1: produce `research.md` per `(article × preset)` episode (same role as the root shim, kept here for the offline-labeling workflow). |
| `generate_episode_oracles.py` | Phase 2b→oracle: computes per-section rewards (`_section_reward`) from graded `reasoning.json`/`scores.json`, writes `section_oracle.json`. **The reward formula lives here.** |
| `enhancement_reward.py` | The count→credit curve (`CREDIT_AT_WEIGHTED_COUNT`) used by `generate_episode_oracles.py` for depth/breadth enhancement scoring — the single place that constant lives. |
| `compute_article_oracle.py` | Aggregates per-section rewards (target-words-weighted) into one article-level `oracle_arm` + `margin`, applies policy hard-rules (forbidden/required/capped) and the small `_MANUAL_OVERRIDES`/`_TIED_ARMS` registries, writes `article_oracle.json`. |
| `merge_replicate_oracles.py` | Averages rewards across N replicate write+grade draws per `(section, arm)` cell, writes `section_oracle_averaged.json` — never touches the single-draw `section_oracle.json`. |
| `train_grpo.py` | The GRPO + QLoRA trainer itself (reads `section_oracle.json`/`section_oracle_averaged.json` as the reward target). |

---

## The production reward formula

Every `(section, arm)` cell — `arm` ∈ {`skip`, `light`, `standard`, `deep`} —
is graded by an LLM judge (`writing_workflow`'s FollowsGT/UserIntent metrics)
on 7 binary/fractional dimensions: `cc` (core_content), `fl` (flow), `cp`
(core_preservation), `de`/`be` (depth/breadth enhancement), `ga`
(guideline_adherence), `ra` (research_anchoring, see below). Written as
**Formula B / C2** (the current, shipped version — `generate_episode_oracles.py::_section_reward`):

$$
R(cc,fl,de,be,cp,ga,\,\text{arm}) \;=\; \underbrace{0.20\,cc + 0.20\,fl}_{\text{ground-truth base}} \;+\; \underbrace{cp\,(0.45\,de + 0.30\,be)}_{\text{exploration credit}} \;+\; \underbrace{g(ga)}_{\text{adherence gate}} \;+\; \underbrace{c\cdot u_{\text{arm}}}_{\text{cost}}
$$

- **`cp` gates the whole exploration-credit term multiplicatively** — a
  draft that lost its core topical identity (`cp=0`) earns zero credit for
  its exploration content, however good that content was in isolation.
- **`ga` is a soft satisficing gate, not an additive term**:
  $g(ga) = -0.10$ if $ga < 0.5$ else $0$. This *replaced* an earlier additive
  term $(0.50\,ga + 0.50\,ra)\cdot 0.30$ after a corpus-wide signal-differentiation
  audit found `ga`'s raw value carried ~97% noise relative to arm choice (it
  barely differs skip vs. deep) — a flat penalty-on-failure is more honest
  about what `ga` can actually tell you than treating it as a graded score.
- **`ra` (research_anchoring) is dropped from the formula entirely** —
  ~97% constant across the whole corpus (2% of total arm-separating signal),
  kept only as an unused parameter for call-site compatibility.
- **`c = -0.03`** (cost coefficient) and $u_{\text{arm}}$ is each arm's
  *empirically-measured* relative exploration effort — **not** the literal
  round count `{0,1,2,3}`. Measured directly from real query/scrape logs
  across the corpus:

  $$u_{\text{skip}}=0,\quad u_{\text{light}}=1.00,\quad u_{\text{standard}}=1.88,\quad u_{\text{deep}}=2.31$$

  (not `0,1,2,3`) because round 2 mostly re-finds already-scraped sources and
  round 3 hits topic/source saturation — `deep`'s *real* marginal effort over
  `standard` is much smaller than "one more round" implies, and the old
  ordinal cost was overcharging it.

**`de`/`be` are not the judge's raw binary score.** They pass through a
separate saturating credit curve (`enhancement_reward.py`) first, driven by
the *count and quality* of qualifying instances the judge found (parsed from
a `[instances=N; quality=strong,standard,...]` tag in its free-text reason):

$$
n_w = \min\!\left(\textstyle\sum_i w(q_i),\; 3\right), \qquad w(\text{strong})=1.0,\;\, w(\text{standard})=0.65
$$

with $n_w$ linearly interpolated through a fitted, concave lookup table
(only the 3 *strongest* instances count — anti-stuffing):

| weighted count $n_w$ | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| credit | 0.00 | 0.35 | 0.45 | 1.00 |

The `1 → 0.35` value (not the naively-expected `1.0`) is itself calibrated
from real evidence, not chosen a priori: direct pairwise LLM A/B comparisons
(`training/analysis/pairwise_reward.py` and friends) found the original
binary scheme systematically over-credited `deep` over `standard` at exactly
the 0-vs-1-instance boundary (two independently-replicated samples,
binomial two-tailed $p=0.031$).

### Article-level aggregation

`compute_article_oracle.py` aggregates a section-level reward table into one
article-level $R_w$ per arm — **target-words-weighted**, except for the
exploration-credit term, which is a **simple unweighted mean** across
sections instead:

$$
R_w(\text{arm}) \;=\; \frac{\sum_s \text{tw}_s\,\big(R_s(\text{arm}) - \text{explore}_s(\text{arm})\big)}{\sum_s \text{tw}_s} \;+\; \frac{1}{|S|}\sum_s \text{explore}_s(\text{arm})
$$

(A section with a bigger writing budget legitimately deserves more say over
the article's overall content-quality/adherence/cost verdict — but a
genuinely valuable exploration instance shouldn't count for more or less just
because it happened to land in a long vs. a short section.)

`oracle_arm = argmax_{\text{arm}} R_w(\text{arm})`, subject to hard
`external_evidence_policy` overrides (`forbidden`→`skip`;
`required`→exclude `skip`; `capped`→restrict to `{skip, light}`) and a small,
individually-documented `_MANUAL_OVERRIDES`/`_TIED_ARMS` registry. An
article can have **more than one valid oracle** when a Student-t test
(df=2, from N=3 replicate draws) on the winner-vs-runner-up margin gives
$p \ge 0.20$ — both presets then count as `EXACT` in
[evaluation](../evaluation/README.md).

---

## The GRPO training process, and how it differs from standard GRPO

Standard GRPO (as used for LLM reasoning/RLHF) samples a *group* of $G$
full-text completions per prompt from the **current** policy, grades each
completion, computes a group-normalized advantage, and takes a PPO-style
clipped-ratio policy-gradient step against a KL penalty — repeated over many
rollout/update cycles, with fresh stochastic samples every time.

This project's GRPO differs in several structural ways, because the action
space is 4 fixed presets rather than free text:

1. **The "group" is the fixed action set, not resampled rollouts.** A group
   is either one *section* (`--granularity section`, the production default)
   or one *article* (`--granularity article`), and its 4 members are always
   exactly `{skip, light, standard, deep}` — never resampled. Each member's
   reward is a **frozen, precomputed** value already looked up from
   `section_oracle.json` (produced by the full, expensive offline
   research→write→grade pipeline — see the reward formula above), not a
   fresh reward from rolling out the current policy. The same 4 rewards are
   reused for every epoch of training.
2. **One forward pass, one token, no rollout.** Since the model only ever
   emits a single classification token (`skip`/`light`/`standard`/`deep`),
   there's no multi-token generation, no per-token credit assignment, and no
   sampling variance to average out with multiple completions per group.
3. **No importance-sampling ratio or PPO clipping.** Because nothing is
   reused off-policy across steps (every epoch recomputes $\pi_\theta$ fresh
   against the same frozen groups), the objective is a plain
   (unclipped) REINFORCE-with-baseline term rather than PPO's
   $\min(r_t A,\ \text{clip}(r_t, 1\!\pm\!\epsilon)A)$:

   $$
   \mathcal{L}_{\text{GRPO}} \;=\; -\,\mathbb{E}_{a \in \{\text{skip,light,standard,deep}\}}\big[A(a)\,\log \pi_\theta(a)\big]
   $$

4. **Advantage normalization has two extra, project-specific knobs.** Given
   the group's 4 raw rewards $r_a$:

   - **Near-tie acceptance clamp** — any $r_a$ within `near_tie_margin`
     (default $0.06$) of the group max is *raised to the max* before computing
     the mean/std used for the advantage. Every statistically-indistinguishable
     arm is therefore treated as equally optimal — the gradient never
     penalizes a defensible non-primary choice (the training-time analogue of
     the tied-arm concept on the labeling side).
   - **`sigma_floor`-clamped denominator** (default $0.04$) — prevents a
     near-numerically-flat group from producing an exploding advantage:

     $$
     A_i = \frac{r_i - \bar r}{\max(\mathrm{std}(r),\ \sigma_{\text{floor}})}
     $$

   - **Flat groups are dropped entirely** — if $\max(r) - \min(r) < \sigma_{\text{floor}}$,
     the whole section/article is excluded from that training run (its
     4 arms are indistinguishable; any choice is pure noise).
5. **Full-batch, not mini-batch.** A standard GRPO/PPO loop samples
   mini-batches and takes many optimizer steps per epoch. Here, **every**
   group in the training set (171 sections, for the current 24-article
   corpus) is forwarded and its gradient accumulated via a `.backward()`
   call, and only **one** `optimizer.step()` is taken per epoch — closer to
   full-batch gradient ascent on a static labeled dataset than to typical
   stochastic mini-batch RL.
6. **Closed-form KL, not a sampled estimator.** Because the action space is
   just 4 enumerable outcomes, the KL penalty against a frozen reference (the
   same base model, no LoRA) is computed *exactly* rather than estimated from
   samples (e.g. the k3 estimator common in autoregressive-LLM RLHF):

   $$
   D_{KL}(\pi_\theta \,\|\, \pi_{\text{ref}}) = \sum_{a} \pi_\theta(a)\Big(\log \pi_\theta(a) - \log \pi_{\text{ref}}(a)\Big)
   $$

7. **An explicit entropy bonus is subtracted directly in the loss** (not
   just logged as a metric), to fight a genuinely persistent entropy-collapse
   failure mode observed across many independent training runs (policy
   entropy repeatedly collapsing by epoch ~20–40 regardless of the entropy
   coefficient tried — documented at length in
   [`rl_training_data/rl_planner_test_results/analysis_document.md`](../../rl_training_data/rl_planner_test_results/analysis_document.md),
   still only partially mitigated).
8. **Inverse-frequency class reweighting** — each group gets an extra
   multiplier $(N / (4\,n_c))^{\tau}$ (`--inv-freq-temp`, default $0.5$),
   where $n_c$ is how often its best preset appears corpus-wide, to counter
   the corpus's real class imbalance (skip/light are heavily over-represented
   vs. standard/deep) — not a feature of vanilla GRPO.

Putting it together, the per-group loss actually backpropagated is

$$
\mathcal{L}_{\text{group}} = \Big(\mathcal{L}_{\text{GRPO}} \;+\; \beta\, D_{KL}(\pi_\theta \| \pi_{\text{ref}}) \;-\; \lambda_H\, H(\pi_\theta)\Big) \times w_{\text{group}}
$$

where $H(\pi_\theta) = -\sum_a \pi_\theta(a)\log \pi_\theta(a)$ and
$w_{\text{group}}$ is a per-group loss weight selected by `--section-weight`
(`wordcount` / `variance` / `hybrid` / `regret-hybrid` / `confidence` /
`uniform`) folded together with the inverse-frequency multiplier above.

| Flag | CLI default | Notes |
|---|---:|---|
| `--lr` | `5e-5` | |
| `--beta` ($\beta$, KL coef.) | `0.1` | |
| `--entropy-coef` ($\lambda_H$) | `0.15` | |
| `--sigma-floor` | `0.04` | advantage-denominator floor + flat-group filter |
| `--near-tie-margin` | `0.06` | acceptable-arm window |
| `--inv-freq-temp` | `0.5` | |
| `--lora-r` / `--lora-alpha` / `--lora-dropout` | `16` / `16` / `0.0` | |
| `--granularity` | `article` | production checkpoints use `section` |
| `--section-weight` | `hybrid` | |
| `--epochs` / `--warmup-epochs` / `--patience` | `200` / `10` / `40` | |

---

## `maintenance/` — reusable data-repair scripts

Generic, re-runnable repair tools (not tied to one historical incident):

| Script | Role |
|---|---|
| `repair_missing_tavily_queries.py` | Repairs episodes whose `next_queries.md` lost its original Tavily queries. |
| `regen_policy_features.py` | Regenerates `guideline_features.json` (`external_evidence_policy` etc.) for a research directory via `rl_inference_service/generate_digests.py`. |

---

## `analysis/` — 40+ offline research scripts (kept flat)

This directory is **deliberately not further subdivided** — the cross-import
graph among these scripts is dense (most import `generate_episode_oracles`/
`compute_article_oracle`/`enhancement_reward` from `pipeline/`, and freely
import each other across themes), so a further split risks undetectable
import breakage. The full narrative behind every one of these — what
question it answered, what it found, what shipped — lives in
[`../../rl_training_data/rl_planner_test_results/analysis_document.md`](../../rl_training_data/rl_planner_test_results/analysis_document.md);
this table is a navigation aid, not a replacement for it.

**Reward-formula calibration & sweeps** (cost coefficient, enhancement-credit
tiers, satisficing gates):

| Script | Role |
|---|---|
| `sweep_reward_formula.py` | Recomputes R_w/margin/oracle for named reward-formula variants straight from graded `reasoning.json` — zero re-grading cost. The main formula-experimentation tool. |
| `sweep_sigma_floor.py` | Sweeps `train_grpo.py`'s `sigma_floor`/near-tie-margin constants against measured noise. |
| `model_gate_candidates.py` | Models hard vs. soft satisficing gates (e.g. the `ga` guideline-adherence gate) before committing to a real regen. |
| `analyze_cost_imbalance.py` | Decomposes each arm's R_w into its components — quantified that the flat cost term dominated `deep`'s shortfall. |
| `analyze_empirical_cost.py` | Measures each arm's *real* exploration effort (queries+scrapes) from on-disk logs, grounding the cost-unit redesign. |
| `audit_enhancement_tags.py` | Corpus-wide audit of `[instances=N;quality=...]` tag distribution feeding the enhancement-credit curve. |
| `margin_moderated_significance.py` | Statistical-significance helper for margin-based label-flip claims. |

**Noise, replication & label-quality**:

| Script | Role |
|---|---|
| `estimate_noise_floor.py` | Measures real per-cell reward noise from replicate draws — grounds `sigma_floor`. |
| `measure_replicate_noise.py` | Recomputes per-section rewards from N replicate draws for direct noise-floor / margin analysis. |
| `setup_noise_experiment.py` | Copies episode inputs into an isolated `noise_experiment/` root for replicate generation without touching production episodes. |
| `quantify_defensible_gain_070.py` | Single-draw vs. averaged defensible-section share at temperature=0.7 (the corrected, unconfounded replication setting). |
| `noise_ceiling_baseline.py` | Oracle self-agreement across replicate draws — a ceiling on how accurate any predictor could look. |
| `reward_signal_quality_report.py` | GRPO-relevant signal-quality metrics (sigma-floor rate, near-tie rate, normalized advantage) single-draw vs. averaged. |
| `reanalyze_part7_averaged.py` | Re-runs the Part-7 gate/cost-coefficient analyses on N=3-replicated data. |
| `diff_oracle_regen.py` | Diffs two `bases/` snapshots' `article_oracle.json` after a reward-formula change — the standard pre-ship safety check. |
| `verify_oracle_reproducibility.py` | Confirms a formula/script change reproduces byte-identical oracle output before trusting a refactor. |
| `full_corpus_per_draw_rw_table.py` | Full-corpus per-draw R_w reference table (all 4 arms × all draws × all 40 articles). |
| `review_near_tie.py` | Generates the per-section contribution breakdown for a near-tie article (feeds `../../rl_training_data/oracle_review/`). |

**Pairwise LLM-comparison grading** (direct A/B section comparison, used to
calibrate the enhancement-credit curve against independent judge evidence):

| Script | Role |
|---|---|
| `pairwise_reward.py` | Reconciles pairwise A/B judgments into a ridge-regularized per-arm reward, anchored at the tag-based `enhancement_credit()`. |
| `select_repeat_targets.py`, `select_light_repeat_targets.py`, `select_tier2_boundary_targets.py` | Reproducibly re-select specific disagreement/boundary cases for a repeat-draws noise check. |
| `analyze_repeat_noise.py`, `analyze_light_repeat_noise.py`, `analyze_tier2_boundary_repeats.py` | Denoise repeated pairwise draws for a specific boundary/tier question. |
| `analyze_light_boundary.py`, `analyze_lightstd_scale.py`, `analyze_stddeep_scale.py` | Tag-based vs. pairwise-judged agreement analysis at the light/standard and standard/deep boundaries. |
| `pairwise_pilot_report.json`, `pairwise_repeat_targets*.json`, `pairwise_tier2_boundary_targets.json` | Persisted pilot/target data these scripts read. |

**Metric differentiation & signal-quality diagnostics**:

| Script | Role |
|---|---|
| `analyze_metric_differentiation.py` | Per-metric per-arm signal strength / noise (armSpread, SNR, monotonicity) across all graded dimensions. |
| `analyze_user_intent_gap.py` | Decomposes `guideline_adherence` failures — found most aren't length violations but missing mandated visual elements. |
| `audit_eff_need.py`, `audit_oracle_balance.py`, `audit_oracle_margins.py` | Corpus-wide audits of exploration-need signals, arm balance, and article margin risk tiers (CRITICAL/HIGH/MODERATE/COMFORTABLE). |
| `audit_semantic_signals.py` | LLM-judged semantic-novelty signal audit (uses `openai.AsyncOpenAI` against x.ai). |
| `analyze_near_tie_metrics.py` | Mean/distribution/t-test analysis for specific near-tie articles flagged for manual review. |
| `stats_crosscheck.py` | Cross-checks significance-test implementations against each other. |

**Oracle-labeling utilities & one-off diagnostic base builders**:

| Script | Role |
|---|---|
| `prototype_oracle_signals.py` | Prototypes new oracle-decision signals before wiring them into `compute_article_oracle.py` for real. |
| `build_formulab_diag_bases.py`, `build_s61_diag_bases.py` | Build isolated `bases_*_DIAG/` roots for single-variable reward-formula ablation retrains (§61 of the analysis doc). |
| `test_live_l5_variants.py` | Live smoke test against real digest-stage output for a small article set. |
| `guarded_constant_baseline.py` | The 4 trivial constant-guess baselines (always-skip/light/standard/deep), guard-clamped the same way production is. |

**Result artifacts** (read/written by the scripts above, not run directly):
`reward_grid_test_results/`, `reward_signal_quality_results/`.

---

## Train a new checkpoint

```bash
uv run python pipeline/train_grpo.py --dry-run                  # sanity-check setup
uv run python pipeline/train_grpo.py --task-id my_run            # full training
uv run python pipeline/train_grpo.py --task-id my_run --epochs 200 --lr 5e-5 --beta 0.15
```

Outputs land under
`../../rl_training_data/checkpoints/tasks/<task-id>/{best,epoch_*,latest}/`,
with a TensorBoard log under `runs/`. Evaluate via
[`evaluation/test_planner.py --adapter-dir tasks/<task-id>/best --rl-guards-only --test-only`](../evaluation/README.md),
or copy `best/` into `rl_inference_service/checkpoints/production/` to make
it the new production default.
