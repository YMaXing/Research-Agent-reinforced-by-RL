# run13_formulaB — Full RL+Grok Pipeline Analysis (2026-07-10)

**Scope:** analysis of the first full RL+Grok evaluation with the retrained `run13_formulaB/best`
adapter against the Formula-B oracles (24 train + 16 test). Answers: are the residual failures
general failure modes or dataset noise? Is further RL improvement worth it? How should the Grok
aggregation layer change? What signals are missing?

---

## 1. Executive summary

1. **The retrain worked.** run13 fixed the structural under-prediction: first-ever exact hits on
   P2/P3 test oracles (`04_structured_outputs`→P2, `13_agent_framework`→P3), zero RL-caused
   misses on test, MAE nearly halved vs. run12-RL (0.938→0.562).
2. **The Grok layer is now the weakest link.** Its discretionary decisions this run went
   **0 helpful / 2 harmful** (both sanctioned escalations misfired). Every *correct* Grok override
   was a deterministic policy guard (forbidden→P0, required→≥P1) that the fallback already
   implements. **`--rl-guards-only` strictly dominates the full pipeline on both splits this run**
   (test 7/9/0 vs 7/8/1; train 19 exact vs 18).
3. **The escalation gate is regime-obsolete.** It was designed to fix run12's under-prediction.
   run13 self-escalates, so the gate now only fires on cases where escalation is wrong.
4. **Residual failure mass = P2-over-prediction on P1-oracle articles** (4 test articles,
   regrets 0.09–0.32). RL's P2-vote precision on test is **1/6** (vs 3/5 on train) — a genuine,
   addressable generalization gap at the P1/P2 boundary, *not* noise floor.
5. **Roughly half of everything else is noise/label artifacts:** both train "misses" have ~zero
   or *negative* regret (label near-ties + one manual-override label), and 2 of the test NEARs
   sit at oracle margins ≤0.027 (inside the documented grading-resolution band).
6. **Statistical honesty:** n=16 with 9/16 P1-oracles means the majority-class baseline (56%)
   beats every model on exact-hit. Differences of ±2 exact are within binomial noise (σ≈2).
   Regret and miss-count are the metrics that actually discriminate here.

---

## 2. Four-config comparison (TEST split, n=16, identical oracle labels)

| Config | Exact | Near | Miss | MAE | Regret mean* | P2/P3-oracle exact |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| run12 RL-only | 5 (31%) | 8 | 3 | 0.938 | 0.1185 | 0/4 |
| run12 RL+Grok (Tier-1 gate) | **9 (56%)** | 5 | 2 | 0.562 | 0.042* | 0/4 |
| run13 RL-only | 7 (44%) | 9 | **0** | **0.562** | 0.0779 | **2/4** |
| run13 RL+Grok (this run) | 7 (44%) | 8 | 1 | 0.625 | 0.0796 | **2/4** |

\* run12-era regrets were computed against the old reward values; Formula B rescaled reward
magnitudes (labels unchanged), so regret columns are only roughly comparable across eras.
MAE and exact/near/miss are label-space and fully comparable.

**How to read the confusing part:** run12+Grok's 9 exacts were **all P0/P1** — its cheap bias
plus Grok's P0→P1 nudges happened to align perfectly with a test set that is 56% P1-oracle.
run13 trades some majority-class alignment for the ability to hit the expensive tail:

| | P0 exact | P1 exact | P2 exact | P3 exact |
|---|:--:|:--:|:--:|:--:|
| run12+Grok | 3/3 | 6/9 | 0/2 | 0/2 |
| run13+Grok | 2/3 | 3/9 | 1/2 | 1/2 |

Neither dominates on exact-hit. run13 dominates on **worst-case behavior**: no 2+-level miss
(run12+Grok had two, including a 3-level `13_agent_framework` P0-vs-P3), and it is the only
configuration that predicts P2/P3 at all on held-out data — which was the original project goal.

---

## 3. Failure taxonomy — noise vs. real

All 9 non-exact test results + 2 train misses, classified:

### 3.1 Label artifacts / near-tie floor (NOT real failures) — 4 items

| Article | Chosen vs Oracle | Regret | Evidence |
|---|---|---:|---|
| `09_RAG__var_demanding` (train MISS) | P1 vs P3 | **−0.0081** | Oracle label is a **manual override**; chosen arm has *higher* reward than the label. Reward-optimal "miss". |
| `06_tools__var_demanding` (train MISS) | P1 vs P3 | +0.0176 | R_w deep 0.609 vs light 0.592 — inside the near-tie band; RL's 2.00-bit entropy correctly signals a genuine 4-way toss-up (votes 26/26/24%). |
| `Earth_Oceans_Origin` (test NEAR) | P2 vs P3 | +0.0246 | Oracle margin 0.0246 — barely above EPS_BAND (0.02). Honest coin-flip at the P2/P3 boundary. |
| `Understanding_Reasoning_LLMs` (test NEAR) | P3 vs P2 | +0.1069 | Oracle margin 0.0271; the model overshoots by one inside a shallow reward valley. Borderline-real, mostly floor. |

The two train "misses" would flip to acceptable under the eval's own near-tie logic; they are
byproducts of the 41%-near-tie / grading-resolution floor documented in the formula-B analysis.
**Nothing in this bucket justifies pipeline changes.**

### 3.2 Real failure mode #1 — P2-over-prediction on P1-oracle articles (4 test items)

| Article | RL conf | Regret | Note |
|---|:--:|---:|---|
| `Insects_Consciousness` | 61% | **0.3192** | Largest regret in the run. R_w: P1 0.982 vs P2 0.663. |
| `Distinct_AI_Models` | **87% (decisive)** | 0.1700 | Confidently wrong — Grok's deference to decisive votes cannot catch it. |
| `29_evaluation_metrics` | 65% | 0.0909 | |
| `Gravity_Entropy` | 58% | 0.0865 | |

**Pattern:** RL P2-vote precision is 3/5 on train but **1/6 on test**. Three of the four are
standalone science explainers (`Insects`, `Gravity`, `Distinct`) whose ground-truth content is
substantially covered by **local golden `.md` sources** — the guideline demands quotes/experiments
(large `need_depth`, high must-ev), but those demands are satisfiable *locally*, so the grader
rewards light exploration. The RL model reads big gap numbers and votes P2. This is a
**systematic, identifiable, addressable** miscalibration — not noise.

### 3.3 Real failure mode #2 — P0-under-prediction on P1-oracle articles (2 test items)

| Article | RL conf | Regret | Note |
|---|:--:|---:|---|
| `Space-Time_QECC` | 58% | 0.1900 | Deep-vote mass 34% but standard 0% → deep-or-nothing guard (correctly per policy) held P0. |
| `31_CI` | 73% (decisive) | 0.0819 | Light mass 14% < 25% → P0→P1 nudge blocked. |

Smaller and less clustered than #1. The nudge/guard thresholds blocked correction in both cases.

### 3.4 Real failure mode #3 — Grok discretionary overrides (2 items, both harmful)

| Article | What Grok did | Effect |
|---|---|---|
| `07_reasoning_planning` (test) | Escalated P1→P2 ("uncertain + standard mass 32% ≥ 30%") | **NEAR→MISS** — the run's only test miss. Oracle P0; all four arms reward ≤0.29 (pathological article — grades poorly under every arm; nothing at inference reveals this). |
| `02_workflows_vs_agents__var_demanding` (train) | Escalated P1→P2 ("uncertain + standard mass 31% ≥ 30%") | **EXACT→NEAR** (regret 0.061). |

Both fired the Tier-1 escalation clause at just-past-threshold mass values (31–32%) on
moderate-confidence votes. **The gate went 0-for-2**; every one of Grok's *correct* overrides
this run (3× forbidden→P0, 1× required P0→P1) is replicated by the deterministic policy guards.

---

## 4. Answers to the specific questions

### 4.1 General failure modes or dataset noise?

**Split roughly 50/50, and separable.** The P2/P3-boundary NEARs and both train misses are at or
inside the measured near-tie floor (grading-resolution limit ≈37% of sections; article margins
≤0.027) — irreducible without finer-grained re-grading. The **P1/P2 boundary over-prediction
cluster is real** (regrets up to 0.32, a repeatable article-type signature) and so is the Grok
escalation misfire (a design artifact, 100% reproducible). Additionally, exact-hit on this test
set is a weak metric: 9/16 P1-oracles put the majority-class baseline at 56%, above every model.
Use regret + miss-count + per-class rows as primary metrics until the test set is expanded.

### 4.2 Still worth improving the RL model?

**Not as the next step.** Evidence:
- The remaining RL errors are concentrated at boundaries where the reward signal itself is
  weakest (the {light,standard} tie region — 28% of all section near-ties).
- Two of the four over-predictions were *decisive-confidence* errors (87%, 86%) — more training
  on the same 24 articles will reinforce, not fix, OOD confidence (the science-explainer article
  type does not exist in training data).
- The cheap wins left in RL-space are data problems (no self-contained-explainer training
  articles), not optimization problems. A longer/anti-collapse rerun would polish training
  metrics without touching the failure clusters above.

The one *cheap* RL experiment worth considering: evaluate the `best_neartie/` (ep90) checkpoint
on the same harness (~30 min) — but expectation is marginal.

### 4.3 How should the Grok aggregation change?

The Grok layer must be **re-fit to the run13 regime** — its current rules were designed
against run12's under-prediction bias, which no longer exists:

1. **Retire the P1→P2 escalation clause.** Its purpose (rescuing under-prediction) is now
   handled by the model itself; empirically 0/2 this run. Keep the deep-or-nothing guard and
   the P0→P1 nudge (harmless; didn't misfire).
2. **Add a sanctioned DOWN-step — the mirror image of Tier-1.** The failure mass is now
   over-prediction. Proposal: when RL votes P2 at *moderate* confidence (<70%) AND the
   self-containment signal (below) is high or high-budget sections show strong existing
   coverage, Grok may step down P2→P1. Targets `29`/`Gravity`/`Insects` (conf 58–65%) while
   leaving decisive votes alone.
3. **Raise the escalation-mass bar if any escalation clause is kept** (31–32% just-past-30%
   firings were both wrong; 40–45% would have blocked both while preserving the legitimate
   self-escalations, which RL now makes on its own).

### 4.4 Missing signals / feature engineering?

**Correction (post-review).** `tavily_saturation` — initially flagged here as the cheapest fix — is
**demoted / dropped**. It measures *exploitation*-phase search saturation, but the preset governs the
*exploration* phase, and the two query **disjoint semantic spaces by design**: exploitation = prescribed
coverage of guideline-named anchors; exploration = depth/breadth on adjacent/deeper material; the
research prompt explicitly forbids cross-over. So exploitation saturation does not predict exploration
yield, its sign is not even stable (a mature, well-trodden topic saturates exploitation *fastest* — Tavily
keeps returning the same canonical pages — yet is often the *richest* in downstream depth/breadth
material), and whatever it does imply is already reflected in the coverage/gap numbers the packet
carries. The ideal signal — exploration *marginal novelty* — is structurally unobservable at decision
time (step 3.4 runs before exploration; the same train/inference asymmetry that makes the oracle's
S1-knee uncomputable at inference). **Do not wire it.**

Confirmed gaps that *are* phase-agnostic and target the over-prediction failure, cheapest first:

1. **Residual-need presentation (cheapest, no new data).** The brief shows raw `need_depth` next to
   `coverage` (e.g. `Insects_Consciousness` S2: need_depth 14, cov 6) and the model escalates on the
   raw 14. Presenting `residual = need_depth − coverage` — and flagging must-ev already backed by an
   available source — stops "already-covered" articles from displaying inflated gaps. Pure transform
   on signals already in the packet.
2. **Golden-source self-containment share (highest-value new feature).** The coverage score blends
   golden + Tavily material; it does *not* isolate "backed by authoritative *local/golden* sources."
   A ratio — anchors/must-ev backed by golden-or-local ÷ total — directly separates "big gap, needs
   web" from "big gap, already satisfiable locally", exactly the science-explainer cluster (`Insects`,
   `Gravity`, `Distinct`). Requires parsing the artefact registry / section `sources` attributes.
3. **Empirical calibration table in the prompt.** Grok has no access to the known error rates of
   the scorer. Injecting a compact table from the train set (e.g., "P2 votes at <70% confidence:
   oracle was P1 in 2/5 train cases") gives the LLM honest priors for when to discount. Zero new
   plumbing — the data already exists in the eval JSONs.
4. **Not fixable via features:** the `07_reasoning_planning` pathology (all arms reward ≤0.29) is
   invisible at inference by construction; no packet field can encode it.

### 4.5 Should the override *mechanics* change?

Yes, in one specific way: **confidence-conditional deference is currently symmetric and should be
asymmetric.** Decisive-P0/P1 votes were reliable this run; decisive-P2 votes were 0/2. Rather than
one 70% threshold, the policy should treat "decisive cheap" as trustworthy and "decisive
expensive on an article type with high self-containment" as challengeable — which is exactly what
the calibration table + self-containment signal enable without hand-tuned thresholds.

---

## 5. Recommended plan (ranked)

| # | Action | Cost | Expected effect |
|---|---|---|---|
| 1 | Ship **`rl-guards-only`** as the interim production mode (or equivalently: keep Grok but disable the escalation clause) | Config-only | Immediately recovers the best current numbers (test 7/9/0, MAE 0.562; train 19 exact) |
| 2 | Residual-need presentation fix (show `need − coverage`, not raw need) | ~30 min | Stops already-covered articles from showing inflated gaps; targets the over-prediction cluster with no new data |
| 3 | Add golden-source self-containment share to packet + brief | ~half day | Isolates locally-satisfiable gaps; phase-agnostic, directly fingerprints the cluster |
| 4 | Rewrite Grok override policy: retire P1→P2 escalation, add calibrated P2→P1 down-step, add calibration table | Prompt work | Re-fits the LLM layer to the run13 regime; target +2–3 exact on test |
| 5 | Expand the test set (per `test_set_build_plan.md`), prioritizing P2/P3 oracles and more self-contained explainers | Expensive | Fixes the measurement bottleneck (n=16, 56% majority class) — prerequisite for trusting any further ±2-exact deltas |
| 6 | (Optional) Evaluate `best_neartie/` ep90 checkpoint | ~30 min | Cheap variance check on checkpoint choice |

**Explicitly deprioritized:** another GRPO training run (targets noise-floor boundaries; decisive-
confidence OOD errors need new data, not more epochs), and any further section-level reward-formula
work (Formula B validated; the remaining section noise is grading-resolution-bound).

---

## 6. Config-decision footnote

`infer.py::_DEFAULT_ADAPTER_DIR` currently points at `run13_formulaB/best` (changed for this
eval). Given run13's clear superiority at the RL stage (0 misses, tail-class hits), **keeping it
is justified** — but note the production default *mode* question (full Grok vs rl-guards-only)
is now the more consequential setting. The `grok_planner_test_results/*.json` files currently
hold this run's RL+Grok results; the run2-era markdown tables in the same directory describe the
run12 pipeline and are now historical.

---
---

# Part 2 — New-Policy Eval Result, Root-Cause Correction, and Forward Plan (2026-07-10)

**Scope:** (a) result of shipping the Part-1-recommended Grok policy rewrite (retire P1→P2
escalation, add residual-need/self-containment signals, calibrated P2→P1 down-step); (b) a
**correction** to Part 1's §3.2/§4.4 "golden-source-satisfiable" explanation, prompted by a user
challenge that turned up a real data-pipeline bug; (c) a reward-asymmetry analysis that yields a
concrete, zero-retraining decision rule; (d) a ranked plan for what comes next.

---

## 7. New Grok policy — measured result

Full RL+Grok eval re-run on `run13_formulaB` with the rewritten override policy
(`preset_planner_handler.py`: retired P1→P2 escalation clause; added residual-need columns,
self-containment "down-step signal", and a calibrated P2→P1 down-step).

| | TEST exact | near | miss | MAE | regret mean |
|---|:--:|:--:|:--:|:--:|:--:|
| Old policy (Tier-1 escalation) | 7 (44%) | 8 | 1 | 0.625 | 0.0796 |
| **New policy** | 6 (38%) | 10 | **0** | 0.625 | 0.0796 |

MAE and regret mean are numerically identical — coincidental, not a null result. Two things
changed and happened to cancel:

- **Goal achieved:** `07_reasoning_planning` no longer gets escalated P1→P2. It stays P1 → NEAR
  instead of the old MISS (regret 0.125). The run's only miss is gone. Same fix landed on the
  train-side twin (`02_workflows_vs_agents__var_demanding`, EXACT restored from NEAR).
- **New regression:** the down-step fired exactly **once** in the whole run — on
  `04_structured_outputs` — and it was wrong (oracle is P2; down-step flipped EXACT→NEAR).
  Grok's own logged reasoning: *"near-zero residuals on budget-dominant standard-voting sections
  + universal self-contained + moderate confidence."*
- **The down-step did NOT touch the actual over-prediction cluster.** `Insects_Consciousness`
  (conf 61%), `Gravity_Entropy` (conf 58%), `29_evaluation_metrics` (conf 65%) are all nominally
  "uncertain" and eligible — Grok's own decision-driver logs say residual need was **not**
  near-zero for any of them, so it correctly declined. `Distinct_AI_Models` (conf 87%) was never
  eligible (down-step requires uncertainty).

**Verdict:** the rewrite is a **safe, net-neutral-to-positive** change (eliminates the only
harmful escalation, introduces one comparably-sized new miscall) but does **not** address the
core over-prediction problem — which turns out, on investigation below, to be partly a **data
bug**, not purely a modeling gap. Keep the new policy; it is strictly safer even though it didn't
move the headline numbers.

---

## 8. Correction to Part 1 — the "golden-satisfiable" story was wrong, but for a fixable reason

Part 1 (§3.2, §4.4) claimed the over-prediction cluster's articles are "substantially covered by
local golden `.md` sources" and that `Distinct_AI_Models` showed this pattern. **A user challenge
caught this: `Distinct_AI_Models` and `Understanding_Reasoning_LLMs` visibly declare golden
sources in their `article_guideline.md` files, yet the earlier digest parse reported 0 golden
sources for both.** Investigating the discrepancy found a real pipeline bug, not a modeling
insight.

### 8.1 What's actually happening

Guideline files can supply golden sources two ways: as a URL to scrape (`<!-- [Title](URL) -->`
followed by nothing local) or as **already-supplied local content**
(`<!-- [Title](URL) --> "Some File.md"` — the reference-URL-blocklist convention). The research
pipeline copies locally-supplied goldens into `.research/local_files_from_research/`
(`process_local_files_tool.py`, confirmed working — the files are physically present and
correctly separated from exploitation-local files).

`generate_digests.py::collect_sources()` (line 662) reads golden web content **only** from
`.research/urls_from_guidelines/`:

```python
"golden_web": _read_md_dir(research_dir / "urls_from_guidelines"),
```

`local_files_from_research/` is **never read by `collect_sources()` at all.** Verified directly:

| Article | `local_files_from_research/` | `urls_from_guidelines/` | Digest sees |
|---|:--:|:--:|---|
| `Distinct_AI_Models` | 1 file (`The Platonic Representation Hypothesis.md`, 79KB) | 0 (dir doesn't exist) | **0 golden sources** |
| `Understanding_Reasoning_LLMs` | 4 files (DeepSeek-R1, Zero-Shot-Reasoners, O1-Replication, Test-Time-Compute; 78–222KB each) | 0 (empty dir) | **0 golden sources** |

Both digests are dated **after** the golden files were scraped (not a staleness issue — this is
a wiring gap: the COLLECT stage's directory list is simply missing an entry). The RL model and
the Grok evidence packet are making decisions from digests that are structurally blind to real,
substantial, on-disk golden material for these two articles.

### 8.2 Scope: this is a TEST-set-concentrated bug, not random noise

Scanned all 49 base directories for `local_files_from_research/*.md` vs `urls_from_guidelines/*.md`:

| Article | local golden files | seen by digest |
|---|:--:|:--:|
| `Bird_Eye_Extreme` | 1 | 0 |
| `Dark_Dimension` | 2 | 0 |
| `Distinct_AI_Models` | 1 | 0 |
| `Earth_Oceans_Origin` | 2 | 0 |
| `HNSW` | 7 | 2 *(partially affected)* |
| `Space-Time_QECC` | 3 | 0 |
| `State_of_LLM_Reasoning` | 3 | 0 |
| `Understanding_Reasoning_LLMs` | 4 | 0 |

**8 of the 16 test articles (50%) are affected. Zero of the 24 train variants are** — every
train-set golden source happens to be URL-based (course-lesson goldens are blog posts/videos
linked online), while roughly half the standalone test articles supply goldens as local files.

This means the bug is not just "some digests are incomplete" — it is a **structural train/test
distribution shift baked into the data pipeline itself**: a model trained purely on digests where
"low/no `golden_web` sources" genuinely means "less material available" will learn to treat that
pattern as a real signal, and that association is **false** for half the test set. This is a more
mechanical, more fixable explanation than "OOD article archetype" for at least part of the
generalization gap — no new data or retraining needed, just closing the pipe.

Checking against the failure taxonomy: 3 of Part 1's "real, addressable" failures overlap with
this bug's blast radius — `Distinct_AI_Models` (regret 0.170), `Understanding_Reasoning_LLMs`
(regret 0.107), and `Space-Time_QECC` (regret 0.190, the P0-under-prediction case). That's a
meaningful fraction of the residual failure mass reclassified from "hard ML generalization
problem" to "data pipeline bug" — a much better place for it to live.

`Insects_Consciousness` and `Gravity_Entropy` (regrets 0.319 and 0.087) are **not** explained by
this bug — both already show golden_web sources correctly in their digests (2 and 1
respectively). Those two remain genuine open cases; Part 1's broader "corpus answer-coverage"
framing (§3 below, revised) still applies to them.

### 8.3 CORRECTION: `Understanding_Reasoning_LLMs` is NOT a separate bug — it is the golden-local bug plus a legitimately-empty exploitation folder

An earlier draft of this section claimed `Understanding_Reasoning_LLMs` had a *second*,
independent scrape failure requiring a full base rebuild. **That was wrong** (flagged by the repo
owner, verified here). Its `.research/guidelines_filenames.json` shows every `exploitation_*`
bucket empty and `other_urls` containing only figure-image URLs (substackcdn), not scrapeable
text sources — the guideline simply lists **no** exploitation "Other Sources". By design, only
guideline-listed exploitation URLs are scraped into `urls_from_guidelines_exploitation/` before
the exploration phase, so that folder being empty is *correct behaviour*, not a failure. The
460-line `tavily_results.md` is exploration-phase search output, which the pre-exploration digest
deliberately does not ingest.

So this article's `total_sources=0` is **entirely** explained by the golden-local bug (§8.1): its
4 golden documents live in `local_files_from_research/` (DeepSeek-R1, Zero-Shot-Reasoners,
O1-Replication, Test-Time-Compute — 78–222 KB each), which `collect_sources()` never reads.
Fixing the golden-local bug (§8.4 / plan step 1) gives this article its 4 sources and resolves it
with **no rebuild required**. Strictly good news: one fix, not two.

### 8.4 Concrete fix (recommended, not yet implemented)

`collect_sources()` needs a 5th bucket read from `local_files_from_research/`. The same hardcoded
4-tuple `("golden_web", "golden_youtube", "golden_code", "exploitation")` that would need the new
bucket threaded through appears at **6 call sites** in `generate_digests.py` (COLLECT dict
literal, artefact-extraction loop, `build_section_source_index`, the COMPRESS-stage loop, and
`process_research_dir`'s orchestration) — a mechanical, well-scoped change, not a redesign.
Tag choice: either a new `type="golden_local"` (cleanest, lets the brief distinguish
scraped-web vs supplied-local golden material) or fold into `golden_web` (simpler, loses that
distinction). Recommend `golden_local` given §3's revised signal design wants exactly this
distinction. After the fix: regenerate digests for the 8 affected test articles (cheap — digest
regen only, no re-research), rebuild `Understanding_Reasoning_LLMs` fully (§8.3), then re-run the
eval to see how much of the residual regret this alone recovers.

---

## 9. Reward-asymmetry analysis — a deterministic decision rule, no retraining required

Computed the empirical class-conditional cost matrix from the 16 non-forbidden train oracles
(forbidden-policy articles excluded — their arms are degenerate, all near-equal low reward, and
would distort the matrix): $\text{Cost}[c][a] = \mathbb{E}[R_w(c^*) - R_w(a)]$ over the true
oracle class $c$ and a candidate action $a$.

| oracle ↓ / action → | P0 | P1 | P2 | P3 | n |
|---|:--:|:--:|:--:|:--:|:--:|
| P0 | 0 | 0.015 | 0.055 | 0.122 | 1 |
| P1 | 0.147 | 0 | **0.132** | 0.173 | 9 |
| P2 | 0.169 | **0.077** | 0 | 0.080 | 3 |
| P3 | 0.067 | 0.058 | 0.079 | 0 | 3 |

Implied pairwise decision thresholds (indifference point where expected cost of escalating
equals expected cost of not):

- **P0 vs P1**: over-cost 0.015, under-cost 0.147 (~10×) → prefer P1 unless $P(\text{P0}) \gtrsim 0.9$.
- **P1 vs P2**: over-cost 0.132, under-cost 0.077 → escalate to P2 only when
  $P(\text{P2}\mid\text{P1 or P2}) > 0.63$ (not the implicit 0.50 of plain argmax).
- **P2 vs P3**: over-cost 0.080, under-cost 0.079 → symmetric; plain argmax is already correct here.

The **same-signed** asymmetry appears in the test-set oracles (computed independently, never
fit to): P1/P2 over-cost 0.163 vs under-cost 0.027 — stronger, not weaker. This is structurally
expected: the $-0.06\cdot nr$ cost term is paid unconditionally per extra round, while the
explore-gain term only pays off conditionally, so over-shooting is systematically costlier than
under-shooting at the cheap boundaries.

**Every stage of the current pipeline decides by argmax** (implicit 0.50 thresholds), and every
hand-tuned guard added so far — the 70% "decisive" bar, the 30% escalation-mass gate, the 25%
nudge floor, the new down-step — is an ad-hoc, partial approximation of this asymmetry. Applying
the P1/P2 rule (threshold 0.63) retroactively against this run's actual RL confidences:

| Article | RL vote (conf) | Rule says | Oracle | Effect |
|---|---|---|---|---|
| Insects_Consciousness | P2 (0.61) | 0.61 < 0.63 → **P1** | P1 | MISS→EXACT chain, −0.32 regret |
| Gravity_Entropy | P2 (0.58) | **P1** | P1 | −0.09 regret |
| 29_evaluation_metrics | P2 (0.65) | knife-edge (0.65 vs 0.63) | P1 | likely fixed |
| 04_structured_outputs | P2 (0.67) | 0.67 > 0.63 → **stays P2** | P2 | protects the exact the down-step broke |
| Space-Time_QECC | P0 (0.58) | 0.58 < 0.9 → **P1** | P1 | −0.19 regret |
| 31_CI | P0 (0.73) | **P1** | P1 | −0.08 regret |
| Distinct_AI_Models | P2 (0.87) | stays P2 | P1 | unfixed (decisive-wrong; also §8 data bug) |
| Dark_Dimension | P0 (?) | risk of flipping to P1 | P0 | possible −1 exact, needs checking |

Rough estimate: **test exact 6→9–11, regret roughly halved, with zero retraining and one
deterministic function** — the single highest-leverage change identified across both parts of
this analysis. Needs the full 4-vector distributions to compute precisely (not just the argmax
confidence currently saved) — that gap is what Phase 0a (§11) closes.

This also reframes §4.4's old "calibration table in the prompt" idea (Part 1): don't ask an LLM
to informally approximate this arithmetic from a table — apply the known cost matrix as a
deterministic rule in the aggregation code, and let Grok focus on what it's actually good at
(policy guards, qualitative catches the numbers can't see, like the `07_reasoning_planning`
all-arms-low pathology).

---

## 10. Revised signal-engineering plan — "corpus answer-coverage"

With 2 of the 4 cluster articles reclassified as a data bug (§8), the remaining open cases
(`Insects_Consciousness`, `Gravity_Entropy`) still fit a real pattern worth a proper signal, not
just a threshold fix — the reward curves for these show a genuine **P1-peak / P2-valley** shape
(exploration actively hurts, not just fails to help), which a decision-rule threshold papers over
by picking the right side of the peak but doesn't explain or generalize from.

Renamed from Part 1's "golden-source self-containment" to **corpus answer-coverage** — the
right question is corpus-level (golden + exploitation together), not golden-only: *"can each
specific guideline demand be answered from the already-scraped corpus, regardless of source
type?"* The current `depth_score`/`breadth_score` grade the corpus against a **generic fixed
8+6 rubric**, not against the guideline's specific demands, and orphan-matching happens against
*compressed summaries* at ASSEMBLE time — exactly where source-specific answerability gets lost.

**Design:** per-anchor answerability audit at the **COMPRESS stage** (the one point where each
source's full text is in context). While compressing source X, emit
`<answers anchor_ids="a3,a7"/>` for guideline anchors X substantively answers (not merely
mentions). ASSEMBLE aggregates per section: `n_demands`, `n_answerable`,
`answer_coverage = answerable/total`. Pre-registered separation test before wiring anything
further: cluster articles (`Insects`, `Gravity`) should show high answer-coverage; `04`/`13`/
`Earth` should show low. A cheap companion fix: **anchor hygiene** — `04_structured_outputs`'
orphans are pure formatting instructions ("Section length: 150 words") that get 3×-multiplied
into `need_depth` (`need_depth = (8 - depth_score) + 3*n_orphans`); filtering instruction-like
anchors before counting removes this noise source directly.

---

## 11. Phase 0a — save full RL probability distributions (started this session)

Both the decision-rule backtest (§9) and any future retraining need the full 4-vector aggregate
distribution, not just the argmax confidence. Confirmed via code read: `agg_probs` (the full
vector) is already computed inside `predict_exploration_preset_tool.py` (used for `confidence`/
`entropy_bits`) but discarded before being returned to callers — `rl_recommendation` only exposes
`preset`, `name`, `confidence`, `entropy_bits`, `floor_correction_applied`.

Fix in progress: add `agg_probs` to the tool's returned `rl_recommendation` dict, and propagate
it into `test_grok_planner.py`'s saved per-article JSON as `rl_agg_probs`, then re-run
`--rl-only --save-json` (train+test) to regenerate all 40 JSONs with the new field. This is
additive and read-only with respect to existing behavior — no decision logic changes yet, purely
instrumentation to unblock §9's backtest and any future analysis.

---

## 12. Revised ranked plan

| # | Action | Cost | Rationale |
|---|---|---|---|
| **0a** | Save full `agg_probs` in eval JSONs (this session) | ~30 min | Unblocks the decision-rule backtest; zero behavior change |
| **0b** | Offline, pre-registered backtest of the P1/P2 (0.63) and P0/P1 (0.9) cost-sensitive thresholds against saved distributions | ~1 h | Ship if ≥+2 test exacts, 0 new misses. Highest expected payoff of anything in this analysis |
| **0c** | Implement the rule in the deterministic aggregation layer; retire the (now-shown-ineffective) Grok down-step clause in favor of it; keep policy guards + deep-or-nothing | ~half day | Moves ad-hoc thresholds to the one actually justified by the reward structure |
| **1** | Fix `collect_sources()` golden-local blind spot (§8.4); regenerate digests for the 8 affected test articles | ~half day | Directly un-breaks `Distinct_AI_Models`/`Space-Time_QECC`, closes a real train/test distribution shift |
| **2** | ~~Rebuild `Understanding_Reasoning_LLMs` base fully~~ — **CANCELLED** (see §8.3 correction: its empty exploitation folder is correct behaviour, not a bug; subsumed entirely by step 1's golden-local fix) | — | Resolved by the golden-local fix alone |
| **3** | Prototype corpus-answer-coverage signal (§10) on `Insects_Consciousness`/`Gravity_Entropy`; pre-register the separation test | ~half day | Only proceed to wiring if separation holds |
| **4** | Anchor hygiene filter (strip instruction-like anchors from orphan/need counts) | ~2 h | Cheap, cleans `need_depth` noise at the source |
| **5** | Expand the test set (stratified per Part 1 §5 item 5); **promote the current 16 test articles into training** once new test articles exist (their 4-arm episodes already exist — near-free) | days, mostly API cost | Fixes the n=16 measurement bottleneck; closes the "no self-contained-explainer archetype in training" gap |
| **6** | LOLO-CV calibration study, only if decisive-wrong votes persist after #1/#2/#5 | 8 retrains | Last resort — expensive, only if cheaper fixes don't resolve it |

**Deprioritized/retired:** more GRPO epochs on current data (§4.2, unchanged), further
reward-formula work (Formula B validated, unchanged), `tavily_saturation` (phase-mismatched,
unchanged), the LLM-prompt calibration table (superseded by §9's deterministic rule), and treating
residual-need/self-containment as down-step *triggers* (§7 showed they're not discriminative
enough to gate on alone — they remain useful brief context, not decision inputs).

---

## 13. Phase 0b/0c — backtest result, a real failure mode, the fix, and shipped

### 13.1 Unconstrained rule: a real failure mode, caught before shipping

First backtest implemented §9's rule literally: pick
$\arg\min_a \sum_c P(c)\cdot\text{Cost}[c][a]$ over all 4 actions, no constraints. Result against
the saved `rl_agg_probs` distributions (§11):

| | exact | near | miss | MAE | regret mean | regret max |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| TEST baseline (argmax) | 7 | 9 | 0 | 0.562 | 0.0779 | 0.3192 |
| TEST unconstrained rule | 9 | 6 | **1** | 0.500 | 0.0435 | 0.1700 |

Better on average — but it introduced a new miss: `13_agent_framework` (probs
`[0.03, 0.32, 0.14, 0.51]`, raw argmax P3 at 51%, correct) got overridden all the way to **P1**,
a 2-level jump, even though P3 was the *plurality* vote and the true oracle. Expected-cost
breakdown confirmed the mechanism: `E[cost|light]=0.0407` beats `E[cost|deep]=0.0702` because
the P1 *row* of the cost matrix has uniformly low costs as a target action (max 0.077) — the rule
was picking a globally "safe hedge" rather than respecting a plurality vote, and can do this for
*any* number of levels since nothing constrains the search. Same pathology hit
`06_tools__var_standard` on train (P3 at 35%, correctly-exact, overridden to P1).

This directly repeats a lesson from Part 1 (Tier-1 escalation, run1): an unconstrained
rule calibrated in aggregate can misfire badly on an individual case outside its regime. Fix:
restrict the search to within 1 preset level of the raw argmax (mirrors the pipeline's existing
"never jump 2 levels" design principle — the deep-or-nothing guard, the old escalation gate).

### 13.2 Constrained rule (max 1-level move): clean win, shipped

| | exact | near | miss | MAE | regret mean | regret max |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **TEST baseline (argmax)** | 7 (44%) | 9 | 0 | 0.562 | 0.0779 | 0.3192 |
| **TEST constrained rule** | **10 (62%)** | 6 | **0** | **0.375** | **0.0384** | **0.1700** |
| TRAIN baseline (argmax) | 19 (79%) | 3 | 2 | 0.292 | 0.0095 | 0.1420 |
| TRAIN constrained rule | 20 (83%) | 2 | 2 | 0.250 | 0.0012 | 0.0175 |

Strictly better than baseline on every metric, zero new misses, on both splits. Fixes (all
single-level, all correct):

| Article | Split | probs | argmax → rule | oracle | Verdict change |
|---|---|---|---|---|---|
| `Insects_Consciousness` | TEST | `[0.00, 0.39, 0.61, 0.00]` | P2→P1 | P1 | NEAR→EXACT, regret 0.319→0 |
| `Space-Time_QECC` | TEST | `[0.58, 0.08, 0.00, 0.34]` | P0→P1 | P1 | NEAR→EXACT, regret 0.19→0 |
| `31_CI` | TEST | `[0.73, 0.14, 0.00, 0.14]` | P0→P1 | P1 | NEAR→EXACT, regret 0.082→0 |
| `05_workflow_patterns__var_standard` | TRAIN | `[0.00, 0.46, 0.54, 0.00]` | P2→P1 | P1 | NEAR→EXACT |
| `09_RAG__var_standard` | TRAIN | `[0.20, 0.19, 0.47, 0.15]` | P2→P1 | P1 | NEAR→EXACT |
| `06_tools__var_standard` | TRAIN | `[0.30, 0.17, 0.18, 0.35]` | P3→P2 | P3 | EXACT→NEAR (small give-back; the 2-level jump is gone, only a 1-level nudge remains) |

Pre-registration honesty check against §9's predicted table: predicted "~9–11 exact, regret
roughly halved" — **delivered 10 exact, regret −51%**, within range. But 2 *specific* per-article
predictions were wrong: `Gravity_Entropy` and `29_evaluation_metrics` were predicted to flip
P2→P1 (naive threshold: confidence 58%/65% < 0.63) but **did not** — correctly so. Diagnosed why:
the naive §9 threshold assumed the residual probability mass sits on the *adjacent* class, but
`Gravity_Entropy`'s residual 42% sits on **P0**, not P1 (`[0.42, 0.00, 0.58, 0.00]`). Full
expected-cost computation: `E[cost|standard]=0.0231` vs `E[cost|light]=0.0507` — standard wins
because `Cost[skip][standard]=0.0551` (moderate over-shoot penalty) is much smaller than
`Cost[standard][light]=0.0768` (the under-shoot penalty on the majority-mass class). The 2-way
pairwise shortcut in §9 was a useful estimate but is provably less accurate than the full
4-class computation — use the full computation, not the shortcut, going forward. Consequence:
`Gravity_Entropy` (regret 0.087) and `29_evaluation_metrics` (regret 0.091) and
`Distinct_AI_Models` (87% decisive, regret 0.170) remain open — correctly left alone by the rule,
not mis-fired on, but still needing §8's digest fix or §10's answer-coverage signal.

### 13.3 Shipped

Implemented in `preset_infer_handler.py`: `_COST_MATRIX` (module constant, the same values as
§9's table) + `apply_cost_sensitive_rule(raw_preset, probs)` (expected-cost argmin restricted to
`_COST_RULE_MAX_STEP=1`). Wired into `predict_exploration_preset_tool.py` immediately after RL
inference, before `confidence`/`entropy`/`floor_applied`/the evidence packet are built — so
`confidence` now honestly reflects support for the *final* recommended preset, not the discarded
raw argmax. Added `raw_argmax_preset` and `cost_rule_adjusted` to `rl_recommendation` for
traceability, and a guidance-string note when the rule fires. This changes the RL recommendation
**upstream of Grok** in every mode (`rl_only`, `rl_guards_only`, full pipeline) — it is not a
Grok-prompt change, so §12's "retire the Grok down-step clause" is deferred until a fresh full
RL+Grok eval shows whether the clause still does anything now that the RL vote it used to
correct arrives pre-adjusted (in progress — see next update to this file).

`get_errors` clean on both files. Not yet re-verified against a live full RL+Grok run at the time
of writing this section — that run is what determines whether §12 item 0c's "retire the Grok
down-step clause" is still necessary or now moot.

### 13.4 Full RL+Grok eval confirmed the concern, diagnosed two Grok misfires, both fixed

The predicted full-pipeline run (§13.3) came back **worse than RL-only**: TEST exact=8 (50%),
near=8, miss=0, MAE=0.500, regret_mean=0.0615 — Grok was net-negative on top of the shipped
cost-rule, undoing 2 of its fixes:

1. **`04_structured_outputs`** — the "SANCTIONED DOWNWARD STEP (P2→P1)" clause (added in the
   earlier 4-recommendations session) fired **again**, with near-identical reasoning to a prior
   run ("near-zero residual on S4/S2/S5, 100% self-contained budget, moderate-confidence P2
   vote"). This is now **2 of 2** times fired, **2 of 2** times wrong (oracle is P2 both times;
   the cost-rule already correctly preserves this article's raw-argmax P2). Zero evidence this
   clause has ever been correct.
2. **`Insects_Consciousness`** — Grok used the "68% budget-weighted standard vote-mass" number to
   escalate a cost-rule-corrected, low-confidence P1 vote (`agg_probs=[0,0.39,0.61,0]`, confidence
   shown to Grok = 0.39, the mass actually on the final P1 pick) back up to P2, reverting the
   cost-rule's single biggest fix (regret 0→0.319). **This happened despite the prompt already
   explicitly stating, in two separate places (the system prompt's OVERRIDE POLICY and the user
   template's task steps), "NEVER escalate a P0 or P1 pick up to P2 or higher... regardless of
   vote mass."** A textual "never do X" instruction was not sufficient once a locally-plausible
   number (68%) was sitting in the evidence brief.

**Fix (implemented and verified):**
- Retired the "SANCTIONED DOWNWARD STEP (P2→P1)" clause entirely — matches plan item 0c, and is
  now backed by 0-for-2 evidence across two separate full evals. Reframed the surrounding prose
  ("RESIDUAL NEED IS CONTEXT, NOT A DECISION TRIGGER") and added a new "PIPELINE NOTE — THE RL
  PICK IS ALREADY COST-ADJUSTED" paragraph telling Grok the P1/P2 boundary is handled upstream
  and not to re-derive it. Updated the evidence-brief line, legend, and `_PLANNER_USER_TEMPLATE`
  to match.
- Added a **code-level** `_apply_escalation_guard(preset, rl_preset)` in
  `preset_planner_handler.py`, next to the existing `_apply_policy_guards` (forbidden/required)
  function and applied in the same place, right after Grok's JSON is parsed: any Grok preset ≥ 2
  is hard-clamped back to 1 whenever the (cost-rule-adjusted) RL pick was P0/P1. The still-
  sanctioned P0→P1 nudge is unaffected (it only ever proposes preset=1). This is a genuine
  belt-and-suspenders fix — the updated prompt language alone might have sufficed (see result
  below), but a hard boundary that has now been observed to leak once should not rely on prose
  alone a second time.

**Result (fresh full RL+Grok eval, both fixes active):** TEST exact=**10 (62%)**, near=6, miss=0,
MAE=**0.375**, regret_mean=**0.0384**, regret_max=**0.1700** — **exactly matches the RL-only
cost-rule ceiling** (§13.2). `04_structured_outputs` is now EXACT (Grok's own driver log:
`"no_sanctioned_override"`). `Insects_Consciousness` is now EXACT (Grok's own risk-flag log:
`"68% standard mass not acted on"` — confirming Grok *saw* the same tempting number as before and
correctly declined to act on it this time, rather than the fix being a lucky non-event). TRAIN is
unchanged (19/3/2, identical to the pre-fix run) since neither misfire involved a train article.

**Interpretation:** the full RL+Grok pipeline is now, for the first time in this entire
investigation, **purely additive over RL-only** — every TEST article's `chosen_preset` equals
either the RL pick directly or a correctly-applied deterministic policy guard; no discretionary
Grok override changed a correct RL decision into an incorrect one. Across every eval run in this
whole investigation (Tier-1 era, new-signals-policy era, cost-rule era), Grok's *only* consistently
correct contributions have been the deterministic policy guards (forbidden→P0, required→≥P1) —
never a genuinely correct discretionary numeric call. The architecture's two-stage design is
intact and Grok is still called (and still produces qualitative `risk_flags` worth reading for
human review), but its authority to *change* the numeric preset is now fully bounded by hard
code-level guards rather than prompt-level trust.

---
---

# Part 3 — Post-Phase-0 retrain (run14) failed; decision: STOP retraining, EXPAND the dataset (2026-07-12)

**Scope:** (a) why the `run14_phase0` retrain (fresh model on the Phase-0-consistent digests)
regressed on held-out test; (b) the decisive attribution measurement (run13 model on the *new*
digests) that separates "model got worse" from "digests got harder"; (c) the verdict — another
training run is **not** worth it, the binding constraint is the dataset; (d) a concrete,
sourced specification of exactly what articles to add and where to get them.

---

## 14. What happened with run14_phase0

Phase 0 (§10–13 above + the memory log) regenerated **all 40 digests** on one consistent
pipeline version (anchor-hygiene + temperature=0 + improved depth/breadth prompt + policy
majority-vote + golden_local fix), eliminating the May→July pipeline-version confound. A fresh
GRPO run (`run14_phase0`, identical hyperparameters to the proven run13 recipe: epochs 200, lr
5e-5, beta 0.15, entropy-coef 0.22, patience 50, lora 16/16, dropout 0.05, section granularity,
hybrid weighting) was trained on those consistent digests and ran to **112 epochs** before being
stopped.

### 14.1 Training-metric trajectory (all TRAIN, 171 sections — memorization proxy, not generalization)

| epoch window | strict top-1 | near-tie top-1 | E[R] | mean entropy H |
|---|:--:|:--:|:--:|:--:|
| peak strict | **ep104 = 0.8246** | — | 0.742 | 0.010 |
| peak near-tie | — | **ep107 = 0.9532** | 0.743 | 0.018 |
| ep98 (best/ checkpoint shipped for eval) | 0.8187 | 0.9474 | 0.742 | 0.016 |
| last 10 (ep102–111) | 0.75–0.82 (fluctuating) | 0.94–0.95 | ~0.742 | **0.007–0.018 (collapsed)** |

The run reached the same train ceiling as run13 (~0.82 strict / ~0.95 near-tie) and then
**fluctuated in a heavily entropy-collapsed regime** (H ≈ 0.01) for the final ~15 epochs without
climbing — the textbook "converged into memorization, no more generalization signal" plateau.
Epochs 102–111 show strict bouncing 0.75↔0.82 with no upward trend; this is noise around a
ceiling, not progress.

### 14.2 Held-out eval — the retrain REGRESSED (both candidate checkpoints)

Ran the full RL+Grok pipeline on two checkpoints; both gave **numerically identical aggregate
regressions** vs. the established run13 baseline:

| Config (TEST, n=16) | exact | near | miss | MAE | regret mean | regret max |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| **run13_formulaB/best (production baseline)** | **10 (62%)** | 6 | **0** | **0.375** | **0.0384** | **0.170** |
| run14_phase0/best (ep98) | 9 (56%) | 3 | **4 (25%)** | 0.812 | 0.0592 | 0.2735 |
| run14_phase0/best_neartie (ep97) | 9 (56%) | 3 | **4 (25%)** | 0.812 | 0.0592 | 0.2735 |
| run14_phase0 TRAIN (ep98) | 20 (83%) | 3 | 1 | 0.208 | 0.0042 | — |

- **TRAIN improved (19→20 exact), TEST regressed hard (10→9 exact, 0→4 misses, MAE 0.375→0.812)**
  — the classic overfitting scissors.
- The 4 new misses are **severe** (2- and 3-level): `13_agent_framework` P3→P0, `Dark_Dimension`
  P0→P3, `14_agent_system_design` P1→P3, `29_evaluation_metrics` P1→P3. run13 never produced a
  2+-level test miss; run14 produces four. The model became **confidently wrong** (H≈0.01) on
  held-out articles.
- ep97 and ep98 being numerically identical rules out "unlucky single epoch" — the whole
  collapse regime around ep97–104 generalizes equally poorly.

**Action already taken:** reverted `infer.py::_DEFAULT_ADAPTER_DIR` to `run13_formulaB/best`.
Production is unchanged and safe.

### 14.3 The decisive attribution question — and its answer

The critical ambiguity: is run14 worse because **(A) the model overfit**, or because **(B) the
Phase-0-refreshed digests are simply harder/different inputs** that would hurt *any* model? These
have opposite implications (A → training problem, maybe fixable by a better run; B → the new
digests are the problem, retraining can't help). The clean way to separate them is to run the
**known-good run13 model on the NEW digests** — same model that scored 10/16, now fed the same
inputs run14 was trained on.

**RESULT — run13_formulaB/best on the post-Phase-0 digests (n=16 TEST held-out):**

| Metric | run13 on OLD digests (baseline) | run13 on NEW Phase-0 digests | Δ |
|---|:--:|:--:|:--:|
| Exact | **10/16 (62%)** | **10/16 (62%)** | 0 |
| Near | 6 | 3 | −3 |
| **Miss** | **0** | **3 (19%)** | **+3** |
| **Ordinal MAE** | **0.375** | **0.625** | **+0.250** |
| Regret mean | 0.0384 | 0.0472 | +0.0088 |
| Regret max | 0.170 | 0.185 | +0.015 |

The three new misses are all **severe (2–3 level)** and all newly broken by the digest refresh:
`13_agent_framework` P3→P0, `29_evaluation_metrics` P1→P3, `Space-Time_QECC` P1→P3. run13 on the
old digests produced **zero** test misses; on the new digests it produces three.

**Interpretation → this is the "digests-harder" branch, not the "pure-overfit" branch.** The
exact *count* held (10/16), but the *error quality* degraded sharply: 0→3 misses and MAE
+0.25 came from the **inputs changing**, not the model. The same known-good adapter, unchanged,
regressed simply by being fed the Phase-0 digests. This means:

- run14's regression is **substantially input/data-driven, not purely an optimizer failure.**
  A big chunk of the "10→9 exact, 0→4 misses" run14 gap is inherited from the digests themselves;
  the additional damage on top of that is overfitting. The optimizer is *not* the primary lever.
- The Phase-0 digest refresh — while *correct* (it fixed the section_oracle clobber and the
  golden-source routing) — moved the P1/P2/P3 boundary cases enough that the current 16-article
  test set can no longer be cleared by *any* model trained on the current 24. The signal the
  model needs to disambiguate `13_agent_framework`, `29_evaluation_metrics`, and
  `Space-Time_QECC` is **not present in the training distribution.**

Both the "pure-overfit" and "digests-harder" branches were pre-written to land on the same
strategic conclusion (§15–16); the measured "digests-harder" result makes that conclusion
**stronger**, because it shows retraining on the same 24 articles cannot recover what the digest
refresh exposed. The lever is the data, definitively.

### 14.4 Cost-matrix re-backtest against the new digest distributions (2026-07-12)

Since the digest refresh shifted `agg_probs`, it was worth checking whether the shipped
`_COST_MATRIX` thresholds (§9/§13, fit 2026-07-10) are still well-calibrated for the new
distributions, or need re-tuning — historically the cheapest, highest-leverage lever in this
whole investigation. Wrote a standalone, read-only backtest script
(`grok_planner_test_results/_backtest_cost_matrix.py`) that loads all 40 saved per-article JSONs
from the run13-on-new-digests eval (§14.3), refits `Cost[c][a] = E[R_w(true=c) - R_w(action=a)]`
from the 24 TRAIN articles' raw `rl_agg_probs` + `r_w_rewards`, and backtests plain argmax vs.
the shipped matrix vs. the refit matrix at the RL-only (pre-Grok) layer on both splits.

**Finding 1 — the refit matrix is numerically identical to the shipped one** (max diff 0.0001,
floating-point noise). This makes sense once you trace what actually changed: the cost matrix is
fit from `r_w_rewards`, the **oracle-labeled ground-truth rewards**, which come from the frozen
`section_oracle.json` files — Phase 0 explicitly protected these from being touched (that was the
whole point of the digest-clobber fix, §Phase 0). Only the *digests* (the RL model's inputs)
changed, not the *oracle rewards* the matrix is fit against. So there is nothing to re-tune in
the matrix values themselves — the empirically-optimal thresholds are unchanged because the
reward structure they encode is unchanged.

**Finding 2 — the existing (unchanged) matrix is still doing real, useful work on the shifted
inputs.** RL-only layer, constrained rule (max-step 1), shipped matrix vs. plain argmax:

| Split | Policy | Exact | Near | Miss | MAE | Regret mean | Regret max |
|---|---|:--:|:--:|:--:|:--:|:--:|:--:|
| TEST (n=16) | argmax (no rule) | 9 (56%) | 5 | 2 | 0.5625 | 0.0816 | 0.4387 |
| TEST (n=16) | shipped cost matrix | 9 (56%) | 5 | 2 | 0.5625 | **0.0502** | **0.1850** |
| TRAIN (n=24) | argmax (no rule) | 10 (42%) | 11 | 3 | 0.7917 | 0.0666 | 0.2760 |
| TRAIN (n=24) | shipped cost matrix | 10 (42%) | 12 | **2** | 0.7083 | **0.0389** | **0.1971** |

No exact-count change on either split this time (unlike the original 7→10 win on the old
digests), but **zero new misses, one TRAIN miss fixed** (`10_memory_knowledge_access__var_minimal`
MISS→NEAR), and **regret cut ~38–42%** on both splits purely from the rule already in
production — it is still earning its keep on the new distributions, just with less headroom
than before because the underlying inputs are the thing that moved, not the decision boundary.

**Finding 3 — the two RL-layer TEST misses are untouched by the rule at any threshold**, because
the rule never even considered moving them: `13_agent_framework`
(`agg_probs=[0.078,0.440,0.171,0.311]`, `raw_argmax=P1`, chosen=P1, oracle=**P3** — a 2-level gap
outside `MAX_STEP=1` by construction) and `29_evaluation_metrics`
(`agg_probs=[0.112,0.150,0.164,0.575]`, `raw_argmax=P3`, chosen=P3, oracle=**P1**, same story in
reverse — 57.5% confident on the wrong side). Both are genuine digest-driven input shifts
(§14.3), not decision-rule miscalibration — no cost matrix, however re-tuned, can fix a case
where the *model's own vote* is confidently on the wrong side and the rule is (correctly)
constrained from jumping 2 levels.

**Bonus finding — the third full-pipeline miss (`Space-Time_QECC`) is a Grok-layer artifact, not
an RL/cost-rule problem.** At the RL+cost-rule layer it scores `chosen=P2, oracle=P1` — a NEAR
(regret 0.126), not a miss. The full RL+Grok eval (§14.3) shows Grok escalating it further,
P2→P3, turning a recoverable near-miss into a severe 2-level miss. This is a Grok-prompt/guard
question (already flagged in Part 1/2 as the deep-or-nothing / escalation-guard territory), not
something the cost matrix can address — it fires *after* the matrix has already made its call.

**Conclusion: the ~1-hour re-backtest was worth doing but confirms there is no cost-matrix lever
left to pull.** The shipped matrix is already at its empirically-optimal fit for this reward
structure and continues to reduce regret substantially on the new distributions; the residual
TEST regression is fully explained by (a) the digest-driven input shift moving 2 articles'
`agg_probs` outside the rule's ±1-level reach, and (b) one Grok-layer escalation on a third. None
of this changes §15–16's verdict — if anything it further **narrows** the cheap, no-retrain
options that have already been exhausted (Phase 0b/0c's cost rule, now re-validated) and reinforces
that the remaining gap is a data problem, not a decision-layer or training problem. No production
code change was made — `preset_infer_handler.py::_COST_MATRIX` is confirmed still correct and is
left as-is.

---

## 15. Verdict: another training run is NOT worth it

Three independent lines of evidence, all pointing the same way:

1. **The failure mode is generalization, and generalization is data-bound here, not
   optimization-bound.** run14 hit the *same* train ceiling as run13 (0.82/0.95) and then
   overfit. The problem was never "the optimizer couldn't fit the training set" — it fits it
   fine (83% train exact). The problem is that **24 training articles, all variant-triples of 8
   base lessons, cannot teach the model the held-out archetypes** (standalone science explainers,
   golden-local-satisfiable articles, no-variant P2/P3). More epochs on the same 24 → deeper
   memorization, not better generalization. This was pre-registered as a risk in the run13
   post-mortem ("decisive-confidence OOD errors need new DATA not epochs") and run14 confirmed it.

2. **Entropy collapse is now a repeatable property of this dataset+recipe, not a tuning miss.**
   Both run13 and run14 collapse to H≈0.01 by ep~85–100. run13 happened to land a
   better-generalizing checkpoint *before* collapsing hard; run14 didn't. Chasing a lucky
   pre-collapse checkpoint via periodic saves + stronger entropy regularization is a
   *variance-reduction* play on a **~2-point exact-count metric whose binomial noise is already
   σ≈2** (n=16). Even a "successful" anti-collapse rerun that recovers run13's 10/16 buys nothing
   over just keeping run13 — and could as easily land at 8/16 by chance.

3. **The measurement itself can't adjudicate small wins.** With n=16 and a 56% majority-class
   (P1) baseline, no retrain can be *shown* to beat run13 by the only margins a retrain could
   plausibly deliver (±1–2 exact). We are optimizing against a ruler too coarse to read the
   result. Spending a ~10-hour retrain + eval cycle to move a needle we can't measure is
   negative expected value.

**Corollary — keep `run13_formulaB/best` as production.** It remains the best validated model
(TEST 10/16, 0 misses, MAE 0.375, regret 0.0384). Nothing in run14 justifies replacing it.

**The one cheap thing worth doing first (before any expensive data work):** the deterministic
cost-sensitive rule (§9/§13) is already shipped and is where all the recent real gains came from.
If the run13-on-new-digests eval (§14.3) shows the new digests shifted some `agg_probs`, it is
worth a ~1-hour **re-backtest of the cost-matrix thresholds against the new distributions** — the
rule is data-cheap to re-tune and has historically delivered more than any retrain. But that is
tuning, not training.

---

## 16. The real lever: EXPAND (and rebalance) the dataset

The binding constraint, restated precisely from all evidence across Parts 1–3:

- **Train/test archetype shift.** TRAIN = 24 variant-triples of 8 *course-lesson* base articles
  (agentic-AI engineering how-to content, all goldens URL-scraped). TEST = 16 *standalone*
  articles (science explainers, deep-dive papers) — a genuinely different distribution the model
  never trained on.
- **Class imbalance + confound.** Current oracle-arm distribution (verified):
  **TRAIN(24): skip=9, light=9, standard=3, deep=3** — and *every* train standard/deep example is
  a `var_demanding` variant, so the model learned "demanding-fingerprint → escalate" rather than
  "genuine depth-need → escalate." **TEST(16): skip=3, light=9, standard=2, deep=2** — a 56% P1
  majority, which is why exact-hit is a near-useless discriminator.
- **The residual test errors are all one archetype the training set lacks:** standalone articles
  whose high guideline demand is *satisfiable from local golden sources* (the over-prediction
  cluster: Insects, Gravity, Distinct, 29_eval, Space-Time). The model has never seen a
  "high-demand-but-golden-satisfiable → light" training example.

### 16.1 What kinds of articles we need (priority-ordered)

**PRIORITY 1 — TEST-set expansion (fixes the MEASUREMENT bottleneck; do this FIRST).**
The n=16 / σ≈2 measurement floor blocks *evaluating* every other improvement. Add **~16–24 new
held-out articles**, stratified by oracle arm so no single class dominates. Target a test set of
~32–40 articles with roughly balanced arms (≈8–10 each of skip/light/standard/deep). Crucially,
include **golden-source-type diversity matching deployment**: a mix of URL-scraped-golden and
local-file-golden ("golden_local") articles, since deployment sees both and the current test set's
golden-local half is exactly where the model fails. Without this, we cannot tell whether *any*
future fix (dataset or model) actually worked.

**PRIORITY 2 — TRAIN-set articles in the MISSING REGIMES (fixes the model's blind spots).**
Two specific archetypes, neither of which exists in training today:

  - **(2a) High-demand + golden-satisfiable → oracle P1 ("the golden-discount lesson").**
    Standalone articles whose guideline lists many specific anchors/must-cover items (large
    `need_depth`), but where those anchors are fully answered by supplied **local golden sources**
    — so the grader rewards *light* research. This is the exact fingerprint of the entire test
    over-prediction cluster. The model currently reads "big gap numbers → escalate"; these
    examples teach it to discount demand when golden coverage is high. **Need ~6–10 of these.**
  - **(2b) No-variant genuine P2/P3 (breaks the `var_demanding`→escalate confound).**
    Standalone articles that *genuinely* need standard/deep research and whose oracle is P2/P3 —
    but that are NOT `var_demanding` variants of a course lesson. This decouples "escalate" from
    the demanding-variant tag the model currently over-relies on. **Need ~4–6 of these
    (some standard, some deep).**

**AVOID (explicitly): more `var_minimal/standard/demanding` variants of the existing 8 lessons.**
This is the cheapest option and the most tempting, but it *deepens* the very confound (2b) is
meant to break, and adds no archetype diversity. Do not generate more variants.

**AVOID: naive train/test reshuffle of the current 40** — moving the 5 over-prediction-cluster
articles into train would leak the exact failure mode being measured; moving "clean" ones shrinks
the already-too-small test set. Reshuffling is only safe *after* Priority-1 expansion backfills
the test set (then promoting a few current test articles into train is near-free, since their
4-arm episodes already exist).

### 16.2 Where to get them (concrete, sourced)

There is already tooling and raw material for this — it does **not** require inventing a pipeline
from scratch:

1. **Guideline synthesizer already exists:** `writing_workflow/generate_article_guideline.py`
   (Phase 0b). It generates a full `article_guideline.md` from a structured YAML *brief* using
   few-shot examples from the existing articles (`--article <name>`, `--from-article <name>` to
   reverse-extract a brief from a finished article, `--eval-mode` to validate quality). Model =
   Grok-4 reasoning, temperature 0.5.
2. **Briefs already staged:** `writing_workflow/inputs/briefs/` already contains **18 YAML
   briefs** — including all 8 current standalone test articles (Bird_Eye_Extreme, Dark_Dimension,
   Distinct_AI_Models, Earth_Oceans_Origin, Gravity_Entropy, HNSW, Insects_Consciousness,
   Space-Time_QECC, State_of_LLM_Reasoning, Understanding_Reasoning_LLMs) plus 13/14/29/31_CI and
   two course-lesson briefs, and a `_TEMPLATE.yaml` documenting the full schema (lesson identity,
   topic_summary, target_length_words, theory_practice_ratio, sections+key_points,
   `golden_sources` [title+url], optional `other_sources`, `code_examples`). **Authoring a new
   article = write one YAML brief + run the synthesizer.**
3. **Golden-source material for the two needed archetypes is abundant and free:**
   - For **(2a) golden-satisfiable science explainers**: pick a narrow scientific/technical topic
     with 1–4 authoritative primary papers (arXiv / open-access journals), supply those papers as
     **local golden files** (the `<!-- [Title](URL) --> "File.md"` convention → they land in
     `.research/local_files_from_research/`, now correctly read post-golden_local-fix), and write
     a guideline that demands detailed coverage of exactly what those papers contain. The existing
     test articles (Space-Time_QECC = the 3 holographic-QEC papers; Understanding_Reasoning_LLMs =
     4 reasoning papers) are the exact template to clone with new topics. Source pool: arXiv
     cs.LG/cs.CL/quant-ph/astro-ph, Distill.pub, open-access Nature/Science summaries.
   - For **(2b) genuine no-variant P2/P3**: pick topics that are *broad or fast-moving* enough
     that a handful of golden sources genuinely do NOT cover the guideline's demands, forcing real
     exploration (e.g. "survey of X across N subfields", "state of the art in Y as of 2026",
     comparative/landscape articles). The guideline should list demands whose answers are NOT in
     the supplied goldens → the grader rewards deeper exploration → oracle lands P2/P3.
4. **Same-course held-out lessons remain available** for more course-archetype articles if
   desired: the course eval dataset (`writing_workflow/inputs/evals/dataset/data/`) and the
   synthesizer's own held-out split (09_RAG, 11_multimodal are the synthesizer's *validation*
   articles) show the pattern; additional real course lessons (12_fine_tuning, 16_observability,
   17_deployment per the `_TEMPLATE.yaml` scope notes) are natural candidates but are the SAME
   archetype we already have plenty of — lower priority than the two standalone archetypes above.

### 16.3 The cost that makes this "expensive" — be clear-eyed about it

Each new article is NOT just a guideline. To get a trustworthy oracle label it needs the **full
4-arm pipeline** (per §Test-Set/Per-Article Labeling): research × 4 presets (skip/light/standard/
deep) → digest → writing × 3/preset → grading against an `article_ground_truth.md` → section
oracle → article oracle. That requires, per article: a written **ground-truth reference article**
(the grader's target — this is the real human/LLM effort), the research runs, and ~12 article
generations + gradings. Ballpark: mostly API cost + a few hours of pipeline wall-time per article,
plus the GT-authoring effort. For ~20–30 new articles this is a multi-day, real-budget effort —
which is exactly why Priorities are ordered: **do the ~16–24 test articles first** (they unblock
measurement and are where deployment actually operates), then the ~10–16 targeted train articles
only if the expanded test set shows the archetype gaps still bite.

### 16.4 Recommended sequence

| # | Action | Cost | Why |
|---|---|---|---|
| 1 | Fill in §14.3 with the run13-on-new-digests number; if digests shifted `agg_probs`, re-backtest the cost-matrix thresholds (~1 h) | Cheap | Cheapest possible win; confirms production is still optimal on the new digests |
| 2 | **Author + label ~16–24 new TEST articles**, stratified by oracle arm, incl. golden-local diversity | Expensive (days) | Breaks the n=16 measurement floor — prerequisite for trusting anything else |
| 3 | Re-run run13 eval on the expanded test set to get the first *statistically meaningful* held-out number | ~30 min | Establishes whether the archetype gap is still material at n≈40 |
| 4 | Only if step 3 confirms the gap: author + label ~10–16 new TRAIN articles in archetypes (2a) + (2b); THEN retrain (with periodic checkpoints + entropy floor to dodge collapse) | Expensive (days) | Teaches the golden-discount + decouples the demanding→escalate confound; retraining is worth it ONLY once the data actually contains the missing regimes |
| 5 | (optional) after test backfill, promote a few current standalone test articles into train (near-free — episodes exist) to further balance | Cheap | Rebalance without shrinking the (now-larger) test set |

**Bottom line:** stop retraining on the current 24 articles — it has hit its ceiling and further
runs only overfit. The lever is data. Expand the **test set first** (to make improvement
measurable) with arm-balanced, golden-source-diverse articles; then add **train articles in the two
missing archetypes** (golden-satisfiable→P1, and no-variant genuine P2/P3). The synthesizer +
briefs infrastructure to do this already exists; the real cost is the 4-arm labeling pipeline and
ground-truth authoring per new article.
