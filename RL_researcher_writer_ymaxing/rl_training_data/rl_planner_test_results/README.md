# RL Planner Test Results

Eval-harness output and the running research log behind the top-level
README's [Results](../../../README.md#results-rlguards-vs-baselines)
section. Every number quoted there traces back to a file in this directory.

## Contents

| File / dir | What it is |
|---|---|
| [`analysis_document.md`](analysis_document.md) | The master research log — 10,000+ lines, §-numbered, documenting the entire multi-week reward-formula calibration and RL-vs-baseline investigation. See below for how to navigate it. |
| `rl_guards_only_train_and_test_results_production_checkpoint.md` | Raw eval output: **production baseline** — RL policy + deterministic policy guards, no LLM call (`evaluation/test_planner.py --rl-guards-only`). |
| `Grok_4_6_only_train_and_test_results_production_checkpoint.md` | Raw eval output: **LLM-only baseline** using `grok-4.6` (`evaluation/test_planner.py --llm-only --planner-model grok-4.6`). |
| `Claude_Opus_5_only_train_and_test_results_production_checkpoint.md` | Raw eval output: **LLM-only baseline** using `claude-opus-4-5` (`evaluation/test_planner.py --llm-only --planner-model claude-opus-4-5`). |
| `archived_scripts/` | One-off scripts whose specific question has been answered and written up — kept for provenance, not part of any current pipeline. |

Raw result files follow the `--save-json`/text-report convention documented
in [`../../research_agent_local/evaluation/README.md`](../../research_agent_local/evaluation/README.md#output-layout):
per-article verdicts (`EXACT`/`NEAR`/`MISS`), a confusion matrix, baseline
comparisons (majority-class/uniform-random/weighted-random), and McNemar /
Poisson-binomial significance tests, for both the TRAIN and TEST splits.

## Navigating `analysis_document.md`

The document is organized as dated, numbered sections (`## N. ...`) grouped
into narrative "Parts", with a long-running "Appendix A" (`## A.N ...`)
picking up the thread once the investigation shifted to label-noise/
replication work. Sections are **append-only and chronological** — later
sections often revise, correct, or supersede earlier ones (always clearly
flagged, e.g. "CORRECTION", "RETRACTED", "SUPERSEDED") rather than editing
history in place. **The latest section is always the most authoritative**
for any specific claim; don't stop at the first mention of a topic.

For the current state of the two things most readers want:

- **The production RL+guards baseline** (headline numbers, baseline ladder,
  significance tests): **§A.23**.
- **The two frontier-model LLM-only baselines vs. RL+guards** (the most
  recent addition, paired McNemar comparisons): **§A.24**.

For the reward-formula derivation itself (not just its results), see
[`../../research_agent_local/training/README.md`](../../research_agent_local/training/README.md#the-production-reward-formula) —
that document states the *shipped* formula plainly; this one contains the
multi-week evidence trail that arrived at it.
