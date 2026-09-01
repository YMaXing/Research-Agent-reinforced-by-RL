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
future fix (dataset or model) actually worked. §16.1.1 below turns "stratified, golden-diverse"
into an exact, verified gap table instead of a slogan.

#### 16.1.1 Concrete identification method — the arm × golden-type grid

To identify *precisely* which kind of article to add next (not just "more of everything"),
cross-tabulate the current 16 TEST articles by (a) oracle arm and (b) golden-source type —
whether their `## Golden Sources` are locally-supplied files (`golden_local`, physically present
before research starts) or scraped web URLs (`golden_web`, fetched live during research).
Verified directly against the 16 saved oracle labels + the golden-type audit from §8.2:

| Oracle arm | golden_local | golden_web | course-lesson (single-variant) | **Total** |
|---|:--:|:--:|:--:|:--:|
| **P0 skip** | Dark_Dimension, State_of_LLM_Reasoning | **— none —** | 07_reasoning_planning (pathological) | 3 |
| **P1 light** | Bird_Eye_Extreme, Distinct_AI_Models, HNSW, Space-Time_QECC | Gravity_Entropy, Insects_Consciousness | 14_agent_system_design, 29_evaluation_metrics, 31_CI | 9 |
| **P2 standard** | Understanding_Reasoning_LLMs | **— none —** | 04_structured_outputs | 2 |
| **P3 deep** | Earth_Oceans_Origin | **— none —** | 13_agent_framework | 2 |

Reading the grid, three concrete, checkable gaps fall out (this is the "identification method" —
run this same cross-tab on any candidate new article before adding it, to see which cell it
actually fills):

1. **The `golden_web`-only column is nearly empty (2/16, both P1).** Every P0/P2/P3 example in
   the test set is either `golden_local`-backed or a single-variant course lesson — there is
   **not one** standalone "genuinely needs web exploration, no local paper dump" example at skip,
   standard, or deep. This is a distinct axis from the local-golden-blind-spot story in §8: it
   tests whether the model can recognize "well-covered by a *small number of canonical web
   sources*" (→P0/P1) vs. "broad/current enough that even good web sources leave real gaps"
   (→P2/P3), independent of the local-file mechanism entirely.
2. **P2/P3 (standard/deep) cells are thin everywhere (2 each), each explained by only 2
   articles.** This is the sharpest form of the n=16 problem: the *tail classes* — also where
   nearly all the interesting model behavior lives (the whole over-prediction cluster is a P1/P2
   boundary phenomenon) — have almost no statistical power. A single borderline oracle at this
   arm swings the per-class rate by 50 points.
3. **Target composition for the +16–24 new articles** (fills every cell to ~4–6, i.e. a
   ~32–40-article test set with ~8–10 per arm):

   | Oracle arm target | golden_local | golden_web | course-style | Add (≈) |
   |---|:--:|:--:|:--:|:--:|
   | P0 skip | +1–2 | **+3–4 (priority)** | +0–1 | 5–7 |
   | P1 light | +0–1 | +2–3 | +0–1 | 2–5 (already near target — lowest priority) |
   | P2 standard | +2–3 | **+3–4 (priority)** | +1–2 | 6–8 |
   | P3 deep | +2–3 | **+3–4 (priority)** | +1–2 | 6–8 |

   The bolded cells (`golden_web` at P0/P2/P3) are the highest-value additions: they are
   currently **zero-count**, and filling them gives a second, independent diagnostic axis —
   whether the model's residual error is really about *golden-source type* specifically, or
   about *depth-need calibration* in general, something the current 16-article grid genuinely
   cannot distinguish.

#### 16.1.2 A cheaper alternative — augment existing articles via guideline edits, not net-new authoring

Prompted by a direct question: since brief-writing and golden-source curation are the slowest
steps, can we fill most of §16.1.1's grid by **editing the guidelines of the current 16/40
articles** (golden-source designation, section-level depth demands) instead of authoring new
topics from scratch? **Checked against the actual pipeline, not assumed — and the answer is yes,
this is provably cheap, because it is exactly the mechanism TRAIN's 24 variant-articles already
use.**

**Verified evidence (not speculation).** Diffed the three `06_tools` guideline-demand variants
directly:

- `article_ground_truth.md` (the expensive, hand/LLM-authored grading target) is **byte-identical**
  across `06_tools__var_minimal` and `06_tools__var_demanding` (`diff -q` reports no difference;
  both 6,015 words) — the SAME reference article grades all three depth-variants.
- The base research corpus snapshot (`research.md`, synthesizer fixture copy) is likewise
  **byte-identical** across variants (69,340 words, `diff -q` clean).
- Only `article_guideline.md` differs, and only modestly (5,697 vs 5,745 words) — per-section
  `target_words` and depth language (`var_minimal` Section 3: "Must stay brief... ~390 words";
  `var_demanding` Section 3: same topic, "~1000 words", more granular technical demands).
- In the **real RL-training bases** (`rl_training_data/bases/06_tools__var_minimal` vs.
  `__var_demanding`), each variant *does* re-run its own independent `.research/` + 4-arm
  labeling pass (`research_digest.md` differs; `oracle_arm_idx` is 0 for minimal vs. 3 for
  demanding) — so the **labeling pipeline cost is not eliminated**, but the **ground-truth
  authoring cost — the single most expensive, least automatable step in §16.3 — is entirely
  reused.** This is the real reason variant-based augmentation is so much cheaper than net-new
  topics: you skip writing a new ideal reference article, and you skip re-designing section
  structure/key-points; you only edit demand parameters and re-run the (already-tooled) labeling
  pipeline.

**Three concrete augmentation levers, each mapped to a specific §16.1.1 grid gap:**

1. **Force-scrape lever (cheapest of all — fills the empty `golden_web` cells directly), refined
   in §16.1.3 below to avoid an actual live re-scrape.** The naive version: take an existing
   `golden_local` test article (e.g. `Space-Time_QECC`, `Earth_Oceans_Origin`,
   `Understanding_Reasoning_LLMs`) and delete the quoted filename line under one or more
   `## Golden Sources` entries, leaving just the URL:
   ```
   <!-- [Title](https://arxiv.org/abs/XXXX.YYYYY) -->
   ```
   (no `"Title.md"` line) so the pipeline scrapes it live. This fills the empty `golden_web` cells
   at effectively zero authoring cost, **but** it re-introduces exactly the scraping
   glitches/incompleteness the `golden_local` choice was made to avoid (per the repo owner: the
   Marker-processed local files are more complete, token-efficient, and better-formatted than a
   live scrape of the same paper — content bulk is otherwise identical) — an unwanted confound
   between "source-type label" and "content quality." §16.1.3 gives a verified, zero-code-change
   way to get the `golden_web` label attributed to the *same* Marker-quality content, isolating
   the label effect cleanly.
2. **Golden-removal lever (manufactures genuine (2b) no-variant P2/P3 examples from existing
   topics).** Strip one or more golden sources (local or web) from a currently-P0/P1 article.
   With the same guideline demands but less supplied material, sections that used to be
   satisfiable locally now have a real coverage gap that only exploration can close — pushing
   the true reward-optimal arm toward P2/P3. This directly targets Priority 2's archetype (2b)
   using topics that already have a ground truth, guideline, and section structure — no new
   topic needed.
3. **Golden-enrichment lever (manufactures genuine (2a) golden-satisfiable examples from the
   *existing hardest cases*).** Take a currently-P2/P3 article whose oracle is expensive
   specifically because its guideline demands aren't locally covered (`13_agent_framework`,
   `Earth_Oceans_Origin`, `Understanding_Reasoning_LLMs`, `04_structured_outputs`) and add
   comprehensive golden sources that substantively answer the section demands. If the added
   material genuinely closes the gaps, the true oracle should shift toward P1/P0 — manufacturing
   the exact "golden-discount" archetype (2a) that Priority 2 calls for, again with zero new
   topic-authoring.
4. **Section-level (mixed-depth) variants — the user's specific "section-level" idea, one step
   beyond what TRAIN already does.** TRAIN's `var_minimal/standard/demanding` scheme escalates
   depth *uniformly* across an entire article. A richer version — not yet used anywhere in this
   dataset — edits the `target_words`/depth language for **only a subset of sections** in an
   existing guideline (e.g. keep 4 of 6 sections at their original scope, deepen 2 specific
   sections' demands and strip their local golden coverage). Because rewards are already computed
   **per section** (`train_grpo.py`), this produces a within-article contrast the current
   whole-article variants cannot — directly exercising the model's ability to weigh
   heterogeneous per-section need rather than one global label, which is closer to what
   real-world articles look like than a uniform escalation.

#### 16.1.3 The bookkeeping trick — attribute `golden_web` without any live re-scrape

Prompted by a direct follow-up: since the whole reason several test articles use `golden_local`
is that the Marker-processed local files are measurably higher-quality than a live scrape of the
same paper (more complete, more token-efficient, cleaner formatting — content bulk is otherwise
identical), forcing a real re-scrape (Lever 1's naive version) would trade the label-diagnostic
we want for a quality regression we don't. Traced the actual code path that decides whether a URL
gets scraped, and there is an existing, unrelated piece of infrastructure that does exactly what's
needed — **no source changes required, only file placement.**

**What the code actually does (verified, not assumed).** Each preset episode for an article is
its own directory, named `<article>__preset<0-3>`, placed as **siblings** under one parent
folder — confirmed directly: `rl_training_data/test_episodes/Space-Time_QECC__preset0` through
`__preset3` sit side by side (`training/rl_data_generator.py::_episode_dir_name` / `EPISODES_DIR`
/ `TEST_EPISODES_DIR`). Before scraping any golden/other URL, the tool
(`scrape_and_clean_other_urls_tool.py`) calls `find_cached_web_files(urls, research_path)`
(`utils/scraping_cache_utils.py`) — built so an article's 4 preset arms don't each re-scrape the
*same* URL independently. It scans every **sibling** directory's
`.research/{urls_from_guidelines,...}/*.md` files for a `**Source URL:** <url>` marker in the
first 15 lines, and if found in *any* sibling, `copy_cached_files()` just `shutil.copy2`s that
file straight into the current episode's `urls_from_guidelines/` folder — **the live scrape call
is skipped entirely** for that URL. This mechanism doesn't care whether the cached file was
originally produced by a real scrape; it only checks for the literal Source-URL marker.

**The recipe (zero code changes, pure data placement):**

1. In the guideline, keep the golden source as a **plain URL entry** (delete the quoted
   `"Title.md"` line) so `extract_guidelines_urls_tool.py` routes it into `other_urls`/
   `arxiv_urls`, not `local_file_paths` — this is what makes the pipeline *attempt* to scrape it
   (and therefore hit the cache lookup) instead of silently reading a supplied local file.
2. Create one small **seed sibling directory** in the same parent as the article's real preset
   episodes, with a name containing the literal substring `__preset` so
   `_get_article_base_name()` truncates it to the correct base (e.g.
   `rl_training_data/test_episodes/Space-Time_QECC__preset_goldenseed/`). It never needs to run
   through the actual research/write/grade pipeline itself — it only needs to exist as a
   directory the cache-scanner can see.
3. Inside it, place `.research/urls_from_guidelines/<any-name>.md` containing:
   ```
   # <Title>

   **Source URL:** <the exact URL string as it appears in the guideline>

   <the Marker-processed body content, verbatim>
   ```
   The URL must match **byte-for-byte** what's in the guideline (same `/abs/` vs `/pdf/` form,
   etc. — matching is exact-string, not normalized), and the marker must fall within the first 15
   lines of the file.
4. Run the real 4-arm pipeline for that article as normal. Every preset episode's
   `scrape_and_clean_other_urls_tool` call will find the seed as a sibling, detect the Source-URL
   match, and copy the seeded file into its own `urls_from_guidelines/` — no Firecrawl/arxiv2md
   call happens for that URL, so no scraping glitches or incompleteness are possible; the exact
   Marker-quality bytes are what `generate_digests.py::collect_sources()` reads into the
   `golden_web` bucket (`research_dir / "urls_from_guidelines"`, line 747).
5. Delete/archive the seed directory once all 4 presets have run (it's a cache donor only, not a
   real preset arm, and shouldn't be mistaken for one later).

**This is a genuine, not merely cosmetic, manipulation.** `generate_digests.py`'s COMPRESS-stage
prompt explicitly includes a `Source type: {source_type}` line (verified at the call site) when
summarizing each source — so a source relabeled `golden_web` is handed to the compression LLM
with a different declared provenance than the identical bytes would get as `golden_local`, which
can genuinely change how it's compressed/weighted, independent of any content difference. That is
precisely the isolated variable the new grid cell needs to test.

**Be explicit about what this does and doesn't validate.** This technique cleanly isolates "does
the `golden_web` *label* change treatment, holding content quality fixed at Marker level" —
exactly what's needed to fill §16.1.1's empty grid cells for measurement purposes. It does **not**
exercise "does the pipeline handle typical live-scrape noise/incompleteness gracefully" — if that
separate question is ever worth answering, a genuinely-scraped variant (Lever 1's naive form)
would still be needed as its own, distinctly-labeled condition, not conflated with this one.

**Caveats to respect before mass-producing this (same discipline as §10/§13.1's pre-registered
separation tests):**

- **Statistical non-independence.** An augmented variant of `Space-Time_QECC` shares topic
  vocabulary and content with the original — if the model mishandles one, it will likely
  mishandle the other for the *same* underlying reason. These are not fully independent draws;
  report them tagged by base-topic (e.g. `Space-Time_QECC__webforced`,
  `Space-Time_QECC__degoldenated`) so a single systematic failure isn't miscounted as several
  independent test failures when computing per-arm rates. Keep a genuine mix of new topics
  (§16.1.1's sourced pools) alongside augmented variants — don't rely on augmentation alone for
  topic diversity.
- **Pilot before scaling.** Run 1–2 augmented variants through the full 4-arm pipeline first and
  confirm the oracle actually moves the *expected* direction (e.g. a golden-stripped
  `Space-Time_QECC` variant should shift toward P2/P3, not stay flat) before committing to
  producing a dozen of them — the same "pre-register the separation test" discipline used
  throughout this investigation.
- **This does not shrink the cost of net-new topics** (still needed for the empty `golden_web`
  cells' full diversity and to avoid pure topic-recycling) — it only removes the ground-truth-
  authoring cost for *augmenting the 16/40 topics that already have one*. See the revised cost
  breakdown in §16.3.

#### 16.1.4 A direct challenge, and a bigger discovery it surfaced: `golden_local` is an out-of-distribution token

Direct challenge received: since §16.1.3's sibling-cache trick still calls for re-running the
full 4-arm research/write/grade pipeline, is that even necessary — don't the downstream writing
and grading steps (everything after `research_instructions_prompt.py` step 2) treat a
`golden_local` source and the "same" content scraped from a URL identically, since the bulk of
the content is the same? **Traced every downstream consumer to check. For the oracle-labeling
pipeline, the challenge is correct — no rerun of research/write/grade is needed.** But tracing it
turned up something more important: the *RL model's own inference-time input* is not indifferent
to source type, and the specific way it isn't indifferent looks like a real, previously-unexamined
contributor to the golden_local failure cluster.

**Where the challenge is right (verified, not assumed).**
- `generate_digests.py`'s COMPRESS-stage prompt (`_COMPRESS_USER_TEMPLATE`) includes a
  `Source type: {source_type}` line, but the instructions that follow it are byte-identical
  regardless of type, and the token budget (`_MAX_TOKENS`) is the same (700) for `golden_web` and
  `golden_local`. No differential treatment.
- The GENERATE-stage digest prompt (`_DIGEST_SYSTEM`/`_DIGEST_USER_TEMPLATE`) computes
  `depth_score`/`breadth_score`/`need_depth`/`need_breadth` from `present="yes/no"` evidence
  flags via a **deterministic validator** (`_count_checklist`) — purely evidence-presence-based,
  with zero reference to source type anywhere in the formula or the instructions.
- A full grep of the entire `writing_workflow/` codebase (the article-writing and grading
  scripts) for `golden_local`, `golden_web`, and `source_type` returns **zero matches** — the
  writer and grader never see or condition on source type at all.
- Conclusion: the **oracle** (the reward-derived ground-truth preset label, which is what a
  4-arm rerun would recompute) is provably content-driven, not type-driven. Relabeling a source's
  acquisition method does not require recomputing it. The challenge is correct on this point.

**Where it's incomplete — the RL model's input is a different story.** Traced
`training/_rl_preset.py::build_rl_input()` (the function that builds the *exact* per-section
prompt the trained Qwen3-4B policy reads at inference time) line by line. It deliberately strips
the full source text from the model's input ("full source text is not needed for preset
selection and creates a length confounder... the downstream writer LLM receives the full digest")
— but it explicitly **keeps a compact `sources_summary` block containing slug + type**:
```python
sm = re.search(r'<s slug="' + re.escape(slug) + r'"([^>]*)>', all_sources_m.group(1))
if sm:
    _sm_parts.append(f'  <s slug="{slug}"{sm.group(1)}/>')
```
`sm.group(1)` is literally ` type="golden_local"` or ` type="golden_web"` — this string is
embedded verbatim into the model's per-section input as `<sources_summary>`. **The RL model does
see the type label, as a literal token, on every inference call.**

**The discovery: this token is out-of-distribution for `golden_local`.** Grepped
`type="golden_local"` across every TRAIN base's `research_digest.md` (all 24: `02`–`11` base +
`var_minimal`/`var_standard`/`var_demanding` for each) — **zero occurrences, confirmed
exhaustively.** Every TRAIN golden source is `golden_web` (course-lesson goldens are all
blog/video URLs — the same fact already noted in §8.2, now traced one level deeper: it means the
*token* `golden_local` never once appears anywhere in the RL model's training data). Grepped the
16 TEST digests: **8 articles carry 23 individual `golden_local` sources** — `Bird_Eye_Extreme`
(1), `Dark_Dimension` (2), `Distinct_AI_Models` (1), `Earth_Oceans_Origin` (2), `HNSW` (7),
`Space-Time_QECC` (3), `State_of_LLM_Reasoning` (3), `Understanding_Reasoning_LLMs` (4) — every
one of which is a member of Part 1/2's over-prediction / under-prediction failure clusters. The
model has **never once been trained on the token it sees for exactly the test articles it fails
on most.** This is a structurally plausible, previously unexamined contributor to the residual
generalization gap — separate from (and possibly compounding) the orphan-routing / self-
containment mechanisms already diagnosed in §8–10 and §14.3.

**What this means for the augmentation trick — cheaper than §16.1.3, and reframed as a diagnostic,
not a data-expansion lever.** Since the oracle doesn't care about type but the *live model input*
does, and since we don't need new content (the compressed text is unaffected by the label), there
is an even simpler mechanism than §16.1.3's sibling-cache injection: **directly edit the `type=`
attribute in the existing, already-computed `research_digest.md` files** for the 8 affected
articles — `sed 's/type="golden_local"/type="golden_web"/'` — no pipeline rerun of any kind, not
even a research/scrape step. Then re-run only the (already-cheap) RL+Grok inference call against
the **unchanged** oracle to see whether `rl_agg_probs` shifts.

**But this does NOT create new, independent test articles — it is an ablation on the *same* 8
topics with the *same* oracle**, so:
- **Count toward §16.1.1's Target Composition: 0.** These are perfectly correlated with the
  existing 8 measurements (same content, same ground truth, same failure history) — counting them
  as new arm-cell fills would repeat exactly the non-independence mistake §16.1.2 warned about,
  and would not move the n=16-floor problem at all.
- **Recommended instead as a near-zero-cost, high-priority diagnostic — run before further data
  collection, not as part of it.** If swapping the token measurably changes accuracy/regret on
  those 8 articles (holding the oracle fixed), that's direct evidence the `golden_local` cluster
  is at least partly an **OOD-token artifact**, not purely a coverage/data problem — and the fix
  would be dramatically cheaper than authoring new topics: either (a) add a `golden_local`-typed
  source to 1–2 *existing* TRAIN articles (a few-hour job, no new topic, no new ground truth,
  just gives the model *any* in-training exposure to the token) or (b) a one-line code fix in
  `generate_digests.py`/`_rl_preset.py` to stop surfacing `golden_local` as a distinct type at
  all (collapse it into `golden_web` / a single `golden` label) if the distinction was never
  meant to carry decision-relevant signal in the first place. Both are cheaper than anything
  else in §16.

#### 16.1.5 Experiment run (2026-07-12) — result: the token is not inert, but its effect was too small to flip any decision here

Ran it. Backed up all 8 affected articles' `research_digest.md` and their existing baseline
JSONs, `sed`-relabeled every `type="golden_local"` → `type="golden_web"` in place (23 occurrences
across 8 files, zero pipeline rerun), re-ran RL+Grok inference restricted to those 8 articles
(`test_grok_planner --articles ... --save-json`), then restored the original digests and JSONs
afterward. Ablation results archived separately in
`grok_planner_test_results/_goldenlocal_ablation/`.

**Per-article comparison (raw RL `agg_probs`, before vs. after relabeling):**

| Article | OLD `agg_probs` [P0,P1,P2,P3] | NEW `agg_probs` [P0,P1,P2,P3] | Changed? | Verdict (old→new) |
|---|---|---|:--:|:--:|
| `Bird_Eye_Extreme` | `[0.000, 0.707, 0.000, 0.293]` | `[0.000, 0.707, 0.293, 0.000]` | **yes** (P2/P3 mass swapped) | EXACT → EXACT |
| `Dark_Dimension` | `[0.200, 0.800, 0.000, 0.000]` | `[0.200, 0.800, 0.000, 0.000]` | no | NEAR → NEAR |
| `Distinct_AI_Models` | `[0.001, 0.174, 0.826, 0.000]` | `[0.175, 0.000, 0.825, 0.000]` | **yes** (P0/P1 mass swapped) | NEAR → NEAR |
| `Earth_Oceans_Origin` | `[0.143, 0.137, 0.000, 0.720]` | `[0.143, 0.137, 0.000, 0.720]` | no | EXACT → EXACT |
| `HNSW` (7 local sources — the most of any article) | `[0.463, 0.537, 0.000, 0.000]` | `[0.463, 0.537, 0.000, 0.000]` | no | EXACT → EXACT |
| `Space-Time_QECC` | `[0.002, 0.002, 0.628, 0.368]` | `[0.080, 0.000, 0.580, 0.340]` | **yes** (mass shifted toward P0, away from P2/P3) | MISS → MISS |
| `State_of_LLM_Reasoning` | `[0.371, 0.124, 0.360, 0.145]` | `[0.371, 0.124, 0.360, 0.145]` | no | EXACT → EXACT |
| `Understanding_Reasoning_LLMs` | `[0.000, 0.070, 0.930, 0.000]` | `[0.000, 0.070, 0.930, 0.000]` | no | EXACT → EXACT |

**Aggregate: n=8, exact=5, near=2, miss=1 — identical on both runs, article-for-article.** Not a
single verdict changed. Regret values are identical to 3 decimals for every article.

**Interpretation — a real but small effect, not a hidden major driver.**
- **The token is demonstrably not inert.** 3 of 8 articles show a genuine shift in `agg_probs`
  purely from the type-label swap (same digest content otherwise) — this rules out "the type
  label never influences the model" as a blanket claim. The mechanism traced in §16.1.4
  (`sources_summary` embeds the literal token, only for sections that cite that specific source)
  explains why exactly 3 shifted and 5 didn't: `HNSW` has by far the *most* `golden_local`
  sources (7) yet shows **zero** change — consistent with the shift depending on which specific
  sections cite the tagged source and how much section-weight they carry, not on how many
  `golden_local` sources the article has overall.
- **But the shift wasn't large enough to cross a decision boundary in this sample.**
  `Space-Time_QECC` shows the largest movement (P0 mass 0.002→0.080, P2 0.628→0.580, P3
  0.368→0.340) — and it's the one MISS in the set — but the RL argmax stays P2 either way, and
  Grok's escalation to P3 fires identically both times, so the final verdict and regret are
  unchanged.
- **Conclusion: this is a real, now-quantified artifact worth fixing on principle (§16.1.4's
  fix (b) — collapsing the type distinction — is a clean, near-zero-cost, permanent
  improvement), but it does not appear to be a major hidden driver of the residual test
  regression by itself, at least on this 8-article sample.** It does not change §15–16's
  verdict, and it does not add or remove anything from the Target Composition count (§16.1.4
  already established this correctly at 0). Worth re-running this same ablation automatically
  whenever new `golden_local` test articles are added (§16.1.1/§16.2), since a larger or
  differently-composed sample could show a bigger effect than this one did.

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
3. **Golden-source material — exact mechanics, plus concrete pools for each gap cell in
   §16.1.1's grid:**

   - **`golden_web` mechanics (fills the empty web-only cells at P0/P2/P3):** add a plain URL
     entry to the guideline's `## Golden Sources` section —
     `<!-- [Title](https://arxiv.org/abs/XXXX.YYYYY) -->` with **no filename line under it**.
     Nothing needs pre-downloading: `scraping_handler.py::scrape_arxiv_url()` already
     special-cases `arxiv.org` URLs and calls the vendored `arxiv2md` package
     (`mcp_server/.venv/bin/arxiv2md`, wraps `arxiv2md.ingest_paper()`) automatically during the
     research phase to fetch clean per-section Markdown; non-arXiv web URLs (blog posts, docs)
     go through the normal Firecrawl/Jina scrape path. This is the natural mechanism for
     "well-documented, but not locally dumped" topics — exactly the missing cells.
   - **`golden_local` mechanics (for topics that should use the local-file convention):**
     (1) fetch the source as Markdown — either the CLI (`arxiv2md <arxiv-id>`, the same tool the
     pipeline calls) or the repo's own `pdftomd.py` for non-arXiv PDFs; (2) save the result as
     `"<Title>.md"` in the article's own research-directory root — the same directory passed as
     `research_directory` to `process_local_files_tool` (sibling to `.research/`, *not* inside
     it); (3) reference it in the guideline exactly like the existing articles:
     ```
     ## Golden Sources
     <!-- [Title](https://arxiv.org/abs/XXXX.YYYYY) -->
     "Title.md"
     ```
     (`extract_guidelines_urls_tool.py` parses the quoted filename;
     `process_local_files_tool.py::_copy_one` resolves it as `research_path / rel_path` and
     copies it into `.research/local_files_from_research/`.) This is the exact mechanism §8's
     golden-local fix made the digest pipeline finally read — new articles using it are handled
     correctly from day one.
   - **An immediately-usable, zero-scrape-cost pool already sitting in the repo.**
     `research_agent_local/.arxiv2md_cache/` already holds 26 previously-fetched arXiv papers as
     cached Markdown. Cross-checked against every currently-staged brief: **18 of the 26 are not
     referenced anywhere** — free, already-converted raw material:

     | arXiv ID | Title | Suggested fit |
     |---|---|---|
     | 2307.16789 | ToolLLM: Facilitating LLMs to Master 16000+ Real-world APIs | agent-tooling explainer (P0/P1 `golden_local`) |
     | 2309.02427 | Cognitive Architectures for Language Agents | agent-framework explainer (P0/P1) |
     | 2312.05934 | Fine-Tuning or Retrieval? Comparing Knowledge Injection in LLMs | comparison/landscape → P2/P3 candidate |
     | 2404.04302 | CBR-RAG: Case-Based Reasoning for RAG in Legal QA | narrow RAG-variant explainer (P0/P1) |
     | 2404.16130 | From Local to Global: A GraphRAG Approach to Query-Focused Summarization | RAG-variant explainer (P0/P1) |
     | 2407.01449 | ColPali: Efficient Document Retrieval with Vision-Language Models | narrow single-paper explainer (P0/P1) |
     | 2409.11402 | NVLM: Open Frontier-Class Multimodal LLMs | multimodal explainer (P0/P1) |
     | 2409.12191 | Qwen2-VL: Enhancing Vision-Language Models' Perception | multimodal explainer (P0/P1) |
     | 2501.00309 | Retrieval-Augmented Generation with Graphs (GraphRAG) | RAG-variant explainer (P0/P1) |
     | 2502.02390 | CoAT: Chain-of-Associated-Thoughts Framework | reasoning-technique explainer (P0/P1) |
     | 2502.05171 | Scaling by Thinking in Continuous Space | test-time-scaling survey pool (below) |
     | 2502.06703 | Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling | test-time-scaling survey pool |
     | 2502.12521 | Inference-Time Computations for LLM Reasoning and Planning: A Benchmark | test-time-scaling survey pool |
     | 2502.13842 | Inner Thinking Transformer: Dynamic Depth Scaling | test-time-scaling survey pool |
     | 2502.14382 | S*: Test-Time Scaling for Code Generation | test-time-scaling survey pool |
     | 2502.18600 | Chain of Draft: Thinking Faster by Writing Less | test-time-scaling survey pool |
     | 2503.04378 | HelpSteer3: Human-Annotated Feedback for Inference-Time Scaling | test-time-scaling survey pool |
     | 2602.02852 | *(title extraction failed — inspect `source.html` directly before using)* | verify first |

     Seven of these (`2502.05171`, `2502.06703`, `2502.12521`, `2502.13842`, `2502.14382`,
     `2502.18600`, `2503.04378`) cluster tightly around **test-time-compute scaling** — a
     fast-moving area with real breadth. This is a strong candidate for a **(2b)-style genuine
     no-variant P2/P3 article** (Priority 2 above): write a guideline demanding a comparative
     "state of test-time scaling" survey whose demands deliberately exceed what these 7 papers
     alone answer (e.g. current production-deployment tradeoffs, cost/latency comparisons, or
     techniques published after these papers) — the goldens then only partially satisfy the
     guideline, and closing the rest genuinely requires standard/deep exploration, which is
     exactly the missing archetype. The remaining papers (ToolLLM, Cognitive Architectures,
     GraphRAG ×2, ColPali, NVLM, Qwen2-VL, CBR-RAG, CoAT) are each narrow enough to support a
     single-paper-or-small-cluster P0/P1 `golden_local` explainer, on the same template as the
     existing `Space-Time_QECC` / `Understanding_Reasoning_LLMs` articles — useful to add volume
     to the `golden_local` P1 cell, or repurposed toward P2 if paired with a guideline that asks
     for more than the paper alone covers.
   - **External source pools for the empty `golden_web`-only P0/P2/P3 cells (net-new topics, not
     yet cached anywhere):**
     - *Science-explainer style, parallel to the 8 existing science-explainer test articles:*
       mine recent submissions directly from arXiv category listings — `arxiv.org/list/cs.LG/recent`,
       `cs.CL`, `cs.AI`, `quant-ph`, `astro-ph`, `cond-mat`, `q-bio.NC` — plus Distill.pub-style
       single-paper explainers. For the P0/P1 `golden_web` cells: a topic fully covered by 1–2
       highly comprehensive papers, referenced as a plain `golden_web` URL, never downloaded
       locally. For the P2/P3 `golden_web` cells: a genuinely contested or fast-iterating
       subfield where a handful of good web sources still leave real gaps.
     - *Agent-framework "landscape" style, parallel to the course-lesson archetype but
       standalone/no-variant (fills the `course-style` P2/P3 cells):* comparative pieces sourced
       from official framework docs and engineering blogs rather than arXiv — e.g. "current state
       of open-source agent frameworks" (LangGraph/AutoGen/CrewAI docs as `golden_web`),
       "landscape of vector database options for RAG", "state of AI coding-agent benchmarks in
       2026" — broad enough that the linked docs alone don't answer everything, forcing real
       exploration.
   - **Course-lesson pool for additional P2/P3 course-style volume:** the `_TEMPLATE.yaml` scope
     notes and `writing_workflow/inputs/evals/dataset/data/` already flag natural additional
     lessons not yet built (`12_fine_tuning`, `16_observability`, `17_deployment`) — same course
     archetype as TRAIN, so lower priority than the standalone `golden_web`/`golden_local` cells
     above; use mainly to round out course-style P2/P3 volume if those cells are still thin after
     the standalone additions.
4. **Same-course held-out lessons remain available** for more course-archetype articles if
   desired: the course eval dataset (`writing_workflow/inputs/evals/dataset/data/`) and the
   synthesizer's own held-out split (09_RAG, 11_multimodal are the synthesizer's *validation*
   articles) show the pattern; additional real course lessons (12_fine_tuning, 16_observability,
   17_deployment per the `_TEMPLATE.yaml` scope notes) are natural candidates but are the SAME
   archetype we already have plenty of — lower priority than the two standalone archetypes above.

### 16.3 The cost that makes this "expensive" — be clear-eyed about it (and where augmentation helps)

Every article, new or augmented, needs the **full 4-arm pipeline** to get a trustworthy oracle
label (per §Test-Set/Per-Article Labeling): research × 4 presets (skip/light/standard/deep) →
digest → writing × 3/preset → grading against an `article_ground_truth.md` → section oracle →
article oracle — ~12 article generations + gradings, mostly API cost + a few hours of pipeline
wall-time. That part of the cost is **the same whether the topic is new or augmented** — §16.1.2
does not remove it.

What §16.1.2 *does* remove is the other line item: a **written ground-truth reference article**
(the grader's target) per topic — verified to be the real human/LLM-authoring effort, and the
part hardest to automate or estimate. For a **net-new topic**, both costs apply: GT-authoring +
the 4-arm pipeline. For an **augmented variant of one of the current 16/40 topics** (§16.1.2's
force-scrape / golden-removal / golden-enrichment / mixed-depth levers), only the 4-arm pipeline
cost applies — the ground truth is reused byte-for-byte, verified against `06_tools`'s three
variants. Practically: augmented variants are roughly half-to-a-third the effort of a genuinely
new topic, which is why the recommended mix (§16.4) leans on augmentation for most of the
Priority-1 volume, reserving net-new topics for the diversity/independence insurance §16.1.2's
caveats call for. For ~20–30 total additions (mixed net-new + augmented) this is still a
multi-day, real-budget effort overall — which is why Priorities stay ordered: **do the ~16–24 test
additions first** (they unblock measurement and are where deployment actually operates), then the
~10–16 targeted train articles only if the expanded test set shows the archetype gaps still bite.

### 16.4 Recommended sequence

| # | Action | Cost | Why |
|---|---|---|---|
| 0 | **Run §16.1.4's `golden_local`-token ablation** on all 8 affected TEST articles: `sed` the `type=` attribute in their existing digests, re-run RL+Grok inference only, compare against the unchanged oracle | ~30 min, zero pipeline rerun | Cheapest possible action in this entire document; could redirect the whole strategy if it shows the failure cluster is partly an OOD-token artifact fixable without any new data |
| 1 | Fill in §14.3 with the run13-on-new-digests number; if digests shifted `agg_probs`, re-backtest the cost-matrix thresholds (~1 h) | Cheap | Cheapest possible win; confirms production is still optimal on the new digests |
| 2 | **Pilot §16.1.2's augmentation levers on 1–2 existing articles** (force-scrape, golden-removal, golden-enrichment) through the full 4-arm pipeline; confirm the oracle moves the expected direction | ~half day | Pre-registered validation before scaling augmentation — cheapest possible source of new TEST arm coverage |
| 3 | **Fill §16.1.1's grid to ~32–40 TEST articles** — prefer augmenting existing topics (skips GT-authoring) for most of the volume, per the target-composition table, topped up with a handful of genuinely new topics (§16.1.1/§16.2 sourced pools) for diversity/independence insurance | Moderate (augmented) + Expensive (net-new) | Breaks the n=16 measurement floor — prerequisite for trusting anything else |
| 4 | Re-run run13 eval on the expanded test set to get the first *statistically meaningful* held-out number | ~30 min | Establishes whether the archetype gap is still material at n≈40 |
| 5 | Only if step 4 confirms the gap: author/augment ~10–16 new TRAIN articles in archetypes (2a) + (2b); THEN retrain (with periodic checkpoints + entropy floor to dodge collapse) | Expensive (days) | Teaches the golden-discount + decouples the demanding→escalate confound; retraining is worth it ONLY once the data actually contains the missing regimes |
| 6 | (optional) after test backfill, promote a few current standalone test articles into train (near-free — episodes exist) to further balance | Cheap | Rebalance without shrinking the (now-larger) test set |

**Bottom line:** stop retraining on the current 24 articles — it has hit its ceiling and further
runs only overfit. The lever is data — but check the free `golden_local`-token ablation (§16.1.4)
first, since it's cheaper than everything else here and could partly explain the residual gap
without needing any new data at all. Otherwise, expand the **test set first** (to make
improvement measurable) with arm-balanced, golden-source-diverse articles — **preferring cheap
guideline-level augmentation of the current 16/40 topics (§16.1.2) over net-new authoring
wherever it fills a grid gap**, backstopped by a genuine minority of new topics for diversity —
then add **train articles in the two missing archetypes** (golden-satisfiable→P1, and no-variant
genuine P2/P3). The synthesizer + briefs infrastructure to do this already exists; the real
remaining cost is the 4-arm labeling pipeline, plus ground-truth authoring only for the net-new
topics.

### 16.5 Step-2 pilot plan — two candidate articles, mixed-depth lever (2026-07-12, not yet executed)

Per §16.4 step 2: pilot §16.1.2's augmentation levers on 1–2 existing articles before scaling.
Picked **Lever 4 (section-level mixed-depth)** for both pilots, per the repo owner's observation
that TRAIN's own depth-variant scheme (`var_minimal/standard/demanding`) is empirically the most
effective augmentation mechanism seen so far — this generalizes that same proven mechanism one
level finer (per-section instead of whole-article), which is untried anywhere in this dataset.

**Selection criteria:** (a) already a member of the known over-prediction cluster (real,
addressable failure, not noise), (b) already has an identifiable "weakest section" in its own
digest gap-profile — i.e. the deepening isn't invented, it amplifies a genuine, already-measured
gap, (c) between the two picks, cover both `golden_local` and `golden_web` article types so the
pilot validates the lever independent of golden-source-type, (d) minimal edit footprint — only
one section's demand text changes, everything else (ground truth, other sections, golden
sources) stays untouched, reusing §16.1.2's proven ground-truth-reuse mechanism.

#### Candidate 1 — `Distinct_AI_Models` (`golden_local`, oracle P1, RL votes P2 at 82% decisive, regret 0.170)

Current digest gap-profile (verified, `rl_training_data/bases/Distinct_AI_Models/research_digest.md`):
4 sections, `need_depth` 15/15/15/**17**, `need_breadth` 4/4/5/**7** — **Section 4 ("Find the
Universals")** is already the article's single weakest section by both metrics, and is fully
`self_contained="yes"` today via 3 sources including the one golden paper ("The Platonic
Representation Hypothesis", arXiv 2405.07987, 2024).

**Proposed edit** — new base dir `rl_training_data/bases/Distinct_AI_Models__mixeddepth/` (copy of
the original), `article_guideline.md` changed **only** in Section 4:
- `Section length: 450 words` → `900 words`.
- Add one new bullet: *"Cite specific 2025–2026 follow-up work that empirically tests, extends,
  or challenges the Platonic Representation Hypothesis with new cross-architecture benchmarks or
  quantitative representational-alignment measurements — name the papers/authors and their
  findings."* This explicitly demands content published **after** the sole golden source (2024),
  which that paper cannot contain by construction.
- Sections 1–3, the golden-source list, and `article_ground_truth.md` are left byte-identical to
  the original.

**Pre-registered hypothesis:** the true reward-optimal arm shifts from **P1 → P2**, because one
section now has a real, unclosable-from-goldens gap while the other three remain
golden-satisfied at light effort. (Note: if it lands at P2, this article's oracle would newly
*agree* with the RL model's current 82%-decisive P2 vote — a nice, but secondary, side-check;
the primary thing being validated is whether the *mechanism* moves the oracle as designed, not
whether the model happens to look right afterward.)

#### Candidate 2 — `Insects_Consciousness` (`golden_web`, oracle P1, RL votes P2 at 61%, **largest regret in the entire investigation: 0.3192**)

Current digest gap-profile (verified,
`rl_training_data/bases/Insects_Consciousness/research_digest.md`): 3 sections, `need_depth`
18/18/**22** — **Section 3 ("Mindful Relations")** is already the weakest section, currently
`self_contained="yes"` via 3 sources, two of which are the golden position-statement pages (New
York Declaration + its background page — advocacy documents, not empirical papers).

**Proposed edit** — new base dir `rl_training_data/bases/Insects_Consciousness__mixeddepth/`:
- `Section length: 450 words` → `800 words`.
- Add one new bullet: *"Cite specific peer-reviewed neuroscience studies (name the researchers,
  species studied, and year) measuring nociceptor density, pain-avoidance learning, or analogous
  quantitative behavioral evidence in named insect species — not merely position-statement
  summaries."* Declaration pages are advocacy documents; they do not carry this level of primary
  quantitative citation, so this explicitly demands material the two goldens don't contain.
- Sections 1–2, golden sources, and `article_ground_truth.md` unchanged.

**Pre-registered hypothesis:** the true reward-optimal arm shifts from **P1 → P2**. This is
simultaneously the highest-value pilot in the whole plan: `Insects_Consciousness` is the single
largest regret in every eval run to date, it is `golden_web` (not `golden_local`), so a
successful shift would be the *first* test article to land in the currently-empty
`golden_web`-at-P2 cell (§16.1.1's bolded priority gap) — filling a grid gap and validating a
fix for the worst failure case in one pilot.

#### Execution pipeline (not yet run — full command chain, for reference/confirmation)

Both pilots reuse the exact machinery already used for TRAIN's `__var_X` variants — no new
tooling required:

1. `cp -r rl_training_data/bases/<Article> rl_training_data/bases/<Article>__mixeddepth`, then
   hand-edit only the target section of the copy's `article_guideline.md` as specified above.
2. **Phase 1 (research, all 4 presets):**
   `cd research_agent_local && uv run --project mcp_server python training/rl_data_generator.py --articles <Article>__mixeddepth`
3. **Digest generation:** `training/generate_digests.py` for the new base (produces
   `research_digest.md` + `guideline_features.json` + `digest_section_placeholder.json`).
4. **Phase 2a (writing, 3 runs/preset):**
   `cd writing_workflow && uv run python rl_writing_generator.py` (scoped to the new article).
5. **Phase 2b (grading vs. the reused `article_ground_truth.md`):**
   `uv run python rl_grading_generator.py` (scoped to the new article) → `reasoning.json`/`scores.json` per episode.
6. **Oracle computation:** `training/generate_episode_oracles.py --articles <Article>__mixeddepth`
   (→ `section_oracle.json`) then `training/compute_article_oracle.py` (→ `article_oracle.json`,
   the number that confirms or refutes each hypothesis above).

**Cost/time honesty:** unlike every experiment run so far in this document (all inference-only or
read-only), this is the **first full 4-arm pipeline run** of the whole investigation — real
Tavily/Firecrawl/LLM-grading API cost across 2 codebases, plausibly several hours of wall time
for 2 articles (research ×4 presets + writing ×3/preset + grading, ×2 articles). Matches §16.4's
own "~half day" estimate for this step. **Not started — awaiting go-ahead before spending that
budget.**

**One methodological flag specific to this lever (worth the pilot explicitly confirming, not
just assuming):** §16.1.2 validated ground-truth reuse for *whole-article* uniform depth changes
(`06_tools`'s 3 variants). This is the first time it's applied to a *partial, single-section*
depth change. The load-bearing assumption — that grading judges each section against the
guideline's own (now section-specific) demands rather than diffing literally against
`article_ground_truth.md` — has only been proven at the whole-article granularity so far; these
two pilots are also the first direct test of whether it holds at section granularity.

#### 16.5.1 The two guideline files — created (2026-07-12), deliberately NOT following the naive deep-copy convention

`writing_workflow/generate_guideline_variants.py`'s documented convention for `__var_X` variants
is to **deep-copy the entire original base directory** (including `.research/` and its
`_stepN.done` / `_exploit_roundN.done` sentinel files) and overwrite only `article_guideline.md`
— explicitly "preserves all step-sentinels and research" so the pipeline *skips* re-running
exploitation. That's correct for the existing uniform variants, because the *set* of
guideline-anchored demands doesn't change between minimal/standard/demanding — only the
word-count/depth language does — so reusing prior exploitation research is valid.

**It would be wrong here.** Both mixed-depth edits add a genuinely **new** anchor/demand (2025–26
follow-up papers; named neuroscience studies) that the *original* exploitation research never
searched for. Deep-copying the old `.research/` with its `.done` sentinels would cause the
pipeline to treat exploitation as already-complete and silently skip searching for the new
demand — defeating the entire point of the augmentation. So the two new base directories were
created **without** any `.research/`, `research_digest.md`, `guideline_features.json`,
`article_oracle.json`, or `section_oracle.json` — i.e. in the same minimal state a genuinely new
article's base would be in — forcing Phase 1 to run every step fresh, including exploitation,
for the new anchor.

**Created and verified:**
- `rl_training_data/bases/Distinct_AI_Models__mixeddepth/` — `article_guideline.md` (Section 4:
  450→900 words + the new 2025–26-follow-up bullet; `Expected Length` updated 2,000→2,450 words
  for internal consistency) + `"The Platonic Representation Hypothesis.md"` (the raw locally-
  supplied golden file, copied to the base root — required by the local-file convention so
  `process_local_files_tool` finds it fresh in each new preset episode).
- `rl_training_data/bases/Insects_Consciousness__mixeddepth/` — `article_guideline.md` (Section 3:
  450→800 words + the new named-neuroscience-studies bullet; `Expected Length` updated
  1,900→2,250 words). No local file needed — both golden sources are plain web URLs.

Ready for Phase 1 (`training/rl_data_generator.py --articles Distinct_AI_Models__mixeddepth` /
`--articles Insects_Consciousness__mixeddepth`) whenever the repo owner wants to spend the
research/writing/grading budget described above.

### 16.5.2 Pilot 1 result — `Insects_Consciousness__mixeddepth` (2026-07-12): section-level mechanism confirmed, article-level hypothesis NOT confirmed

The repo owner ran Phase 1 (research ×4 presets) + Phase 2a/2b (writing ×3/preset, grading)
externally; digest generation (`training/generate_digests.py`), section-oracle computation
(`training/generate_episode_oracles.py`), and article-oracle computation
(`training/compute_article_oracle.py`) were run here to read out the result — all local,
deterministic, zero API cost.

**Section-level: the mechanism worked exactly as designed.**

| Section | Before (original) | After (`__mixeddepth`) |
|---|---|---|
| S1 Introduction (untouched) | oracle=**deep**, rewards `[.70,.64,.58,.82]` | oracle=**skip**, rewards `[.55,.49,.43,.37]` |
| S2 A Growing Awareness (untouched) | oracle=**light**, rewards `[.35,1.14,.58,.82]` | oracle=**light**, rewards `[.50,1.14,.53,.67]` |
| S3 Mindful Relations (**edited**) | oracle=**light**, rewards `[.70,1.14,.93,.87]` | oracle=**deep**, rewards `[.55,.79,.63,1.02]` |

Section 3 — the one section whose demand was deepened — flipped from `light` (reward 1.14, now
0.79) to `deep` (reward 0.87→1.02), exactly the direction pre-registered. The augmentation lever
does what it's designed to do at the granularity it targets.

**Article-level: the oracle did NOT flip (stayed `light`/P1).**

| | oracle_arm | r_w_rewards [skip,light,standard,deep] | margin (light − deep) |
|---|:--:|---|:--:|
| Original `Insects_Consciousness` | **light** | `[.543, .982, .663, .832]` | 0.150 |
| `Insects_Consciousness__mixeddepth` | **light** | `[.531, .842, .539, .714]` | 0.128 |

The hypothesis (P1→P2) is **refuted** — but not uninformatively. The article-level oracle is a
`target_words`-weighted mean across sections (`compute_article_oracle.py`), and **Section 2
("A Growing Awareness"), which was left untouched, carries an unusually dominant `light` reward
(1.14 — the single highest value in either table) and the largest section weight (0.378 of total
words)**. Its pull toward `light` is strong enough to absorb Section 3's genuine shift toward
`deep`. The margin did shrink in the right direction (0.150→0.128), confirming the edit moved the
needle, just not far enough to flip the argmax on its own.

**One honest caveat — S1 (untouched) also changed, calling out real run-to-run noise.** Section 1
("Introduction"), which was not edited at all, still shows materially different reward *values*
between the two runs (`deep`→`skip`). Since neither the guideline text for S1 nor the ground truth
changed, this is attributable to genuine stochasticity in the freshly-rerun exploitation
research/writing/grading (a different Tavily/LLM sampling draw each time) — expected because,
per §16.5.1, the pipeline was deliberately run fully fresh (no stale `.research/` reuse). This
means small oracle-arm margin changes (like the 0.150→0.128 here) should be read with some
caution — not all of the movement is guaranteed to be attributable to the edit alone, though the
*qualitative*, large-magnitude flip on the edited section (S3, light→deep, a real ~30% relative
reward swing) is much more likely a genuine effect of the edit than of noise alone.

**Implication for next steps.** The lever is validated at section granularity but this
particular article's *other* sections are too strongly `light`-anchored to let one deepened
section carry the whole article past the P1/P2 boundary. Options if a P2 example is still wanted
from this topic: (a) deepen a second section as well (e.g. also add an unmet-demand bullet to
Section 2, whose current 1.14 `light` reward is the dominant force keeping this article at P1),
or (b) accept this as a validated section-level augmentation useful for training-signal diversity
even though it doesn't change the article-level arm, or (c) move on to checking
`Distinct_AI_Models__mixeddepth` (also fully researched/written/graded and awaiting the same
oracle computation) as the second pre-registered pilot before drawing a combined conclusion.

**Update — after the repo owner's manual grading corrections (2026-07-13):** re-reviewed
`scores.json`/`reasoning.json` for both articles, corrected some grades, then regenerated the
digest + both oracles. Result:

| | oracle_arm | r_w_rewards [skip,light,standard,deep] | margin (light − deep) |
|---|:--:|---|:--:|
| `Insects_Consciousness` (original, corrected) | **light** (unchanged) | `[.633, .982, .752, .832]` | **0.150 — byte-identical to before the correction** |
| `Insects_Consciousness__mixeddepth` (corrected) | **light** (unchanged) | `[.607, .842, .614, .790]` | **0.052 (down from 0.128)** |

The original article's decision is completely untouched by the correction — the corrected scores
only moved S2's `skip`/`standard` values, never its `light`/`deep` values, so the light-vs-deep
comparison that decides the article-level arm is unaffected (margin identical to 15 decimal
places). The `__mixeddepth` variant's margin, however, shrank by more than half again (0.128→0.052)
because the correction raised S2's `deep` reward (0.67→0.87) — working *in favor* of the P2
hypothesis. Still no flip, but the corrected numbers put this pilot's margin within a factor of
~2.5 of the `EPS_BAND=0.02` near-tie threshold — genuinely close.

### 16.5.3 Pilot 2 result — `Distinct_AI_Models__mixeddepth` (2026-07-13): section reward moved, section oracle didn't flip, article oracle didn't flip — margin collapsed to the near-tie edge

Fully researched, written, graded, digested, and oracle-computed (by the repo owner + the same
local oracle-computation commands as Pilot 1).

**Article-level: no flip, but the margin nearly vanished.**

| | oracle_arm | r_w_rewards [skip,light,standard,deep] | margin | runner-up |
|---|:--:|---|:--:|:--:|
| Original `Distinct_AI_Models` | **light** | `[.625, .899, .729, .793]` | 0.106 | deep |
| `Distinct_AI_Models__mixeddepth` | **light** | `[.611, .803, .782, .684]` | **0.021** | **standard** (changed!) |

`decision_path` for the augmented variant reads *"unique reward winner (margin=+0.0212 >
EPS_BAND=0.02)"* — it clears the near-tie threshold by only **0.0012**, the closest any article
in this whole investigation has come to a near-tie without actually crossing it. Notably the
**runner-up arm itself changed** (deep → standard), a second axis of evidence that the augmented
article's reward landscape is genuinely different, not just quantitatively shifted.

**Section-level: this time the *edited* section didn't flip its own oracle — but its internal
contest changed a lot.**

| Section | Weight (orig→aug) | Original oracle/rewards | `__mixeddepth` oracle/rewards |
|---|:--:|---|---|
| S1 Introduction (untouched) | 0.275→0.224 | **light** `[.55,.94,.63,.72]` | **standard** `[.55,.49,.78,.57]` |
| S2 Company Being Kept (untouched) | 0.325→0.265 | **light** `[.70,.94,.73,.82]` | **deep** `[.70,.79,.58,.82]` |
| S3 Convergent Evolution (untouched) | 0.175→0.143 | **standard** `[.70,.64,.88,.82]` | **light** `[.70,.84,.78,.52]` |
| S4 Find the Universals (**edited**) | 0.225→0.367 | **light** `[.55,.99,.73,.82]` | **light** `[.55,.99,.93,.72]` |

Unlike Pilot 1, **S4 — the section whose demand was deepened — stayed `light` in both runs.** But
the edit clearly moved *something*: S4's `standard` reward jumped 0.73→0.93 (nearly catching
`light`'s unchanged 0.99), while `deep` actually *dropped* slightly (0.82→0.72). Read literally,
the new "cite specific 2025–26 follow-up work" demand seems to be satisfiable with a **moderate**
(`standard`) research pass rather than requiring genuinely deep multi-round exploration — a
finding about the *demand's real difficulty*, not a failure of the lever. S4 is also now the
single heaviest section (36.7% of total words, up from 22.5%, simply because it got longer),
which is exactly why the article-level margin moved so much even though S4's own oracle held.

**All three untouched sections flipped their own individual oracle between runs** (S1
light→standard, S2 light→deep, S3 standard→light) — a stronger and more widespread version of
Pilot 1's single-section noise finding (§16.5.2). This confirms the caveat there was not a
one-off: **fresh full-pipeline re-runs (no `.done`-sentinel reuse, per §16.5.1) introduce
real, non-trivial section-level reward noise independent of any deliberate edit** — likely on
the same order of magnitude as some genuine augmentation effects. The article-level margin
collapse (0.106→0.021) is therefore **not cleanly attributable to the S4 edit alone**; it's a
combination of the edit's real (but section-oracle-preserving) effect on S4 plus noise-driven
churn across S1–S3, which in this instance happened to compound in the same direction.

### 16.5.4 Combined verdict across both pilots

| | Insects_Consciousness | Distinct_AI_Models |
|---|:--:|:--:|
| Edited section's own oracle | flipped (light→**deep**) | held (**light**), but `standard` closed most of the gap |
| Article oracle | held (**light**/P1) | held (**light**/P1) |
| Article margin, original → augmented | 0.150 → 0.052 (−65%) | 0.106 → 0.021 (−80%, to the near-tie edge) |
| Untouched sections also changed oracle? | 1 of 2 (S1) | **all 3** (S1, S2, S3) |

**Two pilots, zero article-level flips, but a consistent, real, and now twice-replicated pattern:**
the section-level mixed-depth edit *always* narrows the article's margin substantially in the
predicted direction, sometimes flipping the edited section's own oracle (Pilot 1) and sometimes
just making that section's runner-up arm much more competitive (Pilot 2) — but a single deepened
section, on these two golden-satisfiable articles, has not been enough by itself to drag the
whole `target_words`-weighted article past the P1/P2 boundary. Both articles have at least one
other section with an unusually dominant, resistant `light` reward that absorbs the shift. The
now-twice-observed noise pattern (untouched sections changing individual oracle between fresh
pipeline runs) is a genuine methodological finding in its own right: it means **any two runs of
this pipeline for the "same" article will differ somewhat even with zero guideline changes**, so
future A/B-style oracle comparisons on this pipeline should expect and budget for that baseline
noise, not just the deliberate treatment effect.

**Recommendation:** neither pilot needs to be discarded — both are legitimate, useful section-level
training signal regardless of the article-level outcome — but if the specific goal is manufacturing
a *new P2/P3 article-level test point* from an existing golden-satisfiable topic, a single-section
edit is evidently not a reliable enough lever on these two examples. Next escalation, if still
wanted: deepen **two** sections simultaneously in one guideline (compounding two section-level
push effects instead of relying on one to overcome the rest of the article's `light` inertia), or
pair the mixed-depth edit with an explicit golden-removal edit (§16.1.2 lever 2) on the *other*
dominant-light section, rather than relying on demand-text alone.

---
---

# Part 4 — Is the noise between "identical" reruns fatal to the whole approach? (2026-07-13)

**Scope:** the two mixed-depth pilots (§16.5) turned up a serious, legitimate worry: sections
whose guideline text was *never touched* still produced materially different rewards between
runs — up to a ±0.45 absolute swing on a 0–1-ish scale, enough to flip that section's own oracle
label. If the reward-generation pipeline is this noisy, are the frozen oracle labels — the entire
foundation this project trains and evaluates against — meaningful at all? This section traces the
noise to its actual source in the code (not speculation), reframes the statistical question
correctly, and lays out proportionate (not "run everything N times") fixes.

## 18. Where the noise actually comes from — traced, not assumed

Three pipeline stages could in principle be the source. Checked each directly:

1. **Grading is deterministic.** `writing_workflow/rl_grading_generator.py`:
   `_GRADING_CONFIG = ModelConfig(temperature=0.0, ...)`. Given the same article text, the grader
   scores it the same way every time (modulo the residual non-determinism any LLM API has even at
   temp=0, which is minor). **Grading is not the noise source.**
2. **Digest-generation numeric features are already confirmed stable at temp=0** — and this was
   already investigated once before, on 2026-07-11 (a docstring in `generate_digests.py` records
   it): *"Per-section numeric features are taken from the first successful call only (lower
   stakes; already stable under temperature=0, see 2026-07-11 noise study)."* Only one *categorical*
   field (`external_evidence_policy`) needed a majority-of-3 vote fix, because a single temp=0 draw
   occasionally flips a genuinely ambiguous categorical judgment — numeric depth/breadth scores did
   not need this. **Digest generation is a minor contributor at most, and was already
   noise-tested once.**
3. **The actual article-writing workflow runs at temperature 0.7 — confirmed directly in
   `writing_workflow/configs/course.yaml`** (and `debug.yaml`/`decodingai.yaml` — all three
   profiles agree):
   ```yaml
   write_article:
     model_config: { temperature: 0.7 }
   integrate_exploration:
     model_config: { temperature: 0.7 }
   review_article:
     model_config: { temperature: 0.0 }
   edit_article:
     model_config: { temperature: 0.1 }
   ```
   `write_article` (the initial draft) and `integrate_exploration` (the step that folds
   exploration-round research into the article — i.e. exactly the mechanism that turns "more
   rounds of exploration" into "more/better content") both run at **0.7**, a genuinely creative,
   high-variance temperature. Review and edit passes are near-deterministic (0.0/0.1). **This is
   the primary, verified noise source: the written article's actual content differs meaningfully
   run to run, and the (deterministic) grader is correctly scoring genuinely different text each
   time — this is not "flaky grading," it's "flaky content generation."**

**A clean, independent mechanistic confirmation this diagnosis is right:** `integrate_exploration`
only runs `if context["research"].has_exploration_sources` — true for `light`/`standard`/`deep`
(≥1 exploration round) but **false for `skip`** (0 rounds). If temperature-0.7 writing is the
noise driver, `skip`-arm rewards should be visibly *more stable* across reruns than the other
three arms, since `skip` never passes through the extra 0.7-temperature integration step.
Checking the actual §16.5 data: in 5 of 6 untouched sections across both pilots, the `skip`
reward is either byte-identical or nearly so between runs (`.55`→`.55`, `.70`→`.70`, `.70`→`.70`),
while `light`/`standard`/`deep` swing by 0.10–0.45 in the same sections. **This is exactly the
predicted pattern** — strong, falsifiable evidence for (not just a plausible story about) where
the noise originates.

**Config-scope caveat:** `rl_writing_generator.py` uses `configs/course.yaml` by default (no
`CONFIG_FILE` override found in `.env`/`.env.example`) — the **same** config used for real,
published course-content writing. Any temperature change here affects both oracle-label
generation *and* production writing quality; see §19's fix accordingly.

## 19. Reframing the statistical question — and why this doesn't invalidate the project

**The relevant question is not "is there noise" — essentially every RL/LLM pipeline has some —
it's "does the noise's magnitude threaten the signal enough to change what the label teaches,"
and, distinctly, "how does that noise interact with how the label gets used."** Two things make
this pipeline's situation different from the RL folklore that "policy gradient methods are
robust to noisy rewards":

- **In the RL folklore case, the noisy reward is resampled fresh every time the same
  state/action is encountered during training** (a stochastic environment), so noise averages
  out across the many visits a training run makes to similar states — that's *why* PPO/GRPO
  tolerate it.
- **Here, the oracle reward for a given (article, section, preset) is computed *once*, frozen
  into `section_oracle.json`, and then reused as the fixed training target for every subsequent
  GRPO epoch that touches it.** There is no resampling during training to average the noise away
  — whatever was captured in that one frozen draw *is* the ground truth the model is trained
  against, indefinitely. A noisy one-time label is a **fundamentally more serious problem** than
  noise in a resampled reward signal, and the folklore reassurance does not directly apply.

**This is not a new, independent crisis — it is very likely the mechanistic explanation for a
failure mode already documented in this very file.** §14–15's run14 post-mortem found: the model
fits the 24 TRAIN articles almost perfectly (83% strict) while TEST regresses, entropy collapses
to H≈0.01, and more epochs deepen memorization rather than improve generalization. **A model that
is asked to fit a small, fixed set of point-labels — some fraction of which are one noisy draw
rather than a stable estimate — has no way to distinguish "genuine, generalizable signal" from
"noise it should ignore."** It will do what supervised/RL fitting always does with noisy fixed
targets on limited data: memorize them, including their noise, which shows up exactly as
overfitting + entropy collapse. This reframes §15's verdict as *even better supported* than
already argued, not undermined: the data (and now, specifically, the **label-generation
noise floor**) is the binding constraint, not the optimizer.

**None of this makes the oracle labels "meaningless."** The *signal* (systematic reward
differences between genuinely different presets on genuinely different articles) is real and
large in most cases — most articles in this whole investigation show comfortable, clearly-decided
margins (`Understanding_Reasoning_LLMs` 0.93 `light`-mass, `Earth_Oceans_Origin`'s clean `deep`
win, etc.). The noise mainly matters at the **margins that are already thin** — which, not
coincidentally, is exactly where this whole investigation's hardest, most contested cases already
live (`Insects_Consciousness`, the two mixed-depth pilots). The labels aren't uniformly
unreliable; the *confidence you should place in a label* should scale inversely with how close its
margin sits to the now-measured noise floor — which is a fixable calibration problem, not a
reason to abandon the approach.

## 20. Proportionate fixes — reject the false binary

The choice is not "replicate the entire expensive pipeline N times" vs. "give up." Four much
cheaper, targeted options, cheapest first:

| # | Fix | Cost | What it addresses |
|---|---|---|---|
| 1 | **Lower `write_article`/`integrate_exploration` temperature for oracle-generation runs specifically** — clone `course.yaml` into a new `rl_generation.yaml` profile (e.g. temperature 0.7→0.2–0.3) and point `rl_writing_generator.py` at it via the existing `CONFIG_FILE` env var, leaving production `course.yaml` (real published content) untouched | **Free** (one config file, one env var) | Attacks the noise at its root, for every future label (existing pipeline change, zero extra LLM calls) |
| 2 | **Recalibrate `EPS_BAND` in `compute_article_oracle.py`** using the now-measured noise magnitude. It's currently a flat `0.02`; §18's data shows untouched-section swings up to 0.45 and article-level margin swings up to ~0.08 from noise alone. A more honest threshold (informed by a small measured noise distribution, see #3) would correctly reclassify some currently-"confident" labels as near-tie, triggering the existing secondary-signal (S3/S4/S5) tie-breaking logic instead of a possibly-noisy argmax | **Free** (one constant, informed by #3's data) | Makes the *existing* decision rule honestly reflect its own uncertainty, without regenerating anything |
| 3 | **Targeted, cheap noise measurement: re-run just the write+grade steps (reusing the existing `research.md`) 2–3× for a small sample of articles**, skipping the expensive research/exploitation/exploration phases entirely. This is far cheaper than the user's feared "full pipeline N times" — it reuses the already-completed (and now temperature-fixed, if #1 lands) research, and only repeats the comparatively fast, cheap LLM-only write+grade loop | **Cheap** (a few LLM calls per replicate, no Tavily/scraping) | Gives an actual, quantified noise distribution to calibrate #2 and to know how much to trust any given margin |
| 4 | **Targeted replication only for near-boundary cases**, using the article's own `margin`/`decision_path` as the trigger: articles with large, comfortable margins (the majority) need no extra work at all; only articles sitting close to the (now-recalibrated) `EPS_BAND` — like both `__mixeddepth` pilots — get 2–3 replicate write+grade passes (per #3) before their label is trusted | Proportionate (few articles, cheap steps only) | Concentrates the only real expense where the signal-to-noise ratio is actually in doubt, instead of paying it everywhere |

**Recommended order:** do #1 and #2 immediately (both are free, same-day changes); do #3 on a
small sample (~5–8 articles spanning comfortable and thin margins) to get an actual noise
distribution rather than reasoning from 2 data points; then apply #4 going forward for any new
or contested label. None of this requires "generate multiple runs of the full workflow for every
article" — that was never the only alternative to "proceed with unexamined noise."

**Bottom line for the crisis of confidence:** the concern was correct and worth raising — and
tracing it down turned up a real, previously-unquantified issue *and* a plausible mechanistic
explanation for part of the run13/14 generalization gap, which is a net gain for the investigation,
not a reason to distrust it. The fix is cheap (a temperature knob and a recalibrated constant),
not "unbearably expensive." The existing oracle-label corpus is not meaningless — its *comfortable-
margin* labels remain trustworthy as-is; its *thin-margin* labels (a minority) need either the
cheap replication in #3/#4 or, at minimum, honest recalibrated-EPS_BAND treatment as near-ties
rather than confident answers.

## 21. Will lowering temperature 0.7→0.2–0.3 hurt Gemini 2.5 Pro's article quality?

Short answer: **unlikely to hurt the quality dimension this pipeline actually measures, and the
fix is scoped so it cannot touch real published content regardless.**

**Why the draft temperature matters less here than it would in a single-shot pipeline.** The
0.7-temperature steps (`write_article`, `integrate_exploration`) are not the last word — the
workflow runs `review_article` (temp 0.0) → `edit_article` (temp 0.1) for `num_reviews=2`
iterations afterward (§18). The final `article.md` is several deterministic-ish refinement passes
removed from the initial creative draft. Lowering the draft temperature mainly reduces variance
*earlier* in a pipeline that already dampens variance *later*; it is not equivalent to lowering
the temperature of a single one-shot generation with no review loop.

**What actually gets graded.** `rl_grading_generator.py` scores against `article_ground_truth.md`
on dimensions like core-content coverage and flow/fidelity to the guideline's demanded facts —
not on stylistic variety or creative flourish. Temperature 0.7 is a setting for *creative
diversity*, which is not the axis this rubric rewards. If anything, a high-variance draft is more
likely to occasionally underweight, skip, or paraphrase-away a guideline-demanded bullet in favor
of a more "creative" framing; a lower temperature should make the writer *more* consistent about
mechanically covering what the guideline (and the folded-in exploration research) actually says.
That is a plausible **quality improvement for this specific rubric**, not just a neutral risk.

**Why this is safe to try regardless.** The recommended fix (§20, item 1) is a **new**
`rl_generation.yaml` profile selected via the existing `CONFIG_FILE` env var — `course.yaml` (the
config that generates real, published course content) is never touched. So even in the
hypothetical worst case where lower temperature *did* make prose blander, that tradeoff is
completely inconsequential for this project's purpose: nobody reads these RL-training articles as
final content, they exist purely to be graded into a reward number. The only thing that matters is
whether the *graded signal* is better (less noisy) or worse (systematically distorted) — not
whether the prose reads as engagingly.

**Still, don't just trust the theory — this project's whole methodology has been "verify, don't
assume."** Recommended before fully committing: generate 1–2 articles at temperature 0.2–0.3 (reuse
existing `research.md`, i.e. the cheap write+grade-only replication already proposed in §20 item 3
does double duty here), read them, and compare their `scores.json` against the existing runs for
the same article/preset. If grading scores hold steady or improve and nothing reads as
degenerate/repetitive (a real risk at very low temperatures, more relevant below ~0.2 than at
0.2–0.3), proceed with confidence; if something looks off, the config-profile approach makes it a
one-line revert.

## 22. Margin-diagnostic tool: which existing labels are actually candidates for replication?

Built `research_agent_local/training/audit_oracle_margins.py` (new, **read-only, zero pipeline
cost** — it only parses already-computed `article_oracle.json` files, it does not rerun anything)
to answer this concretely instead of guessing. It scans every `rl_training_data/bases/*/`
directory, reads `margin`/`oracle_arm`/`runner_up_arm`/`decision_path`/`needs_review`, and buckets
each into a risk tier:

| Tier | Range | Rationale |
|---|---|---|
| CRITICAL | margin < 0.02 (`EPS_BAND`) | Already flagged as near-tie by the pipeline's own existing logic |
| HIGH | 0.02 – 0.06 | Within the smaller of the two measured pilot swings (`Insects_Consciousness__mixeddepth`: 0.128→0.052, a 0.076 swing from grading corrections alone) |
| MODERATE | 0.06 – 0.10 | Within the larger measured swing (`Distinct_AI_Models__mixeddepth`: 0.106→0.021, a 0.085 swing, edit+noise combined) |
| COMFORTABLE | ≥ 0.10 | Outside the measured noise range so far |

**Important correctness fix made while building this, not before.** `compute_article_oracle.py`
computes `margin = r_w[oracle_arm] − r_w[runner_up_arm]` *unconditionally* after `_decide()`
returns — but `_decide()` has two hard-rule branches that override the raw reward argmax
entirely: `external_evidence_policy == "forbidden"` (forces `skip` regardless of R_w) and
`_MANUAL_OVERRIDES` entries. When either fires, `margin` can come out **negative** (the forced arm
need not be the top-reward one), and that negative number has *nothing to do with write/grade
noise* — it's a deterministic rule working as designed. Replicating write+grade for these
wouldn't change the label. The script detects this via `decision_path[0]` (`"policy=forbidden..."`
/ `"manual override..."`) and reports these 11 articles separately as excluded, rather than
polluting the CRITICAL tier with false positives.

**Real output against the current corpus (42 article-oracles: 40 production + 2 `__mixeddepth`
pilots):**

- **11 excluded** (policy-forced or manual-override — not reward-comparison risk at all): the 8
  `var_minimal` TRAIN variants + `State_of_LLM_Reasoning` (all `forbidden`-policy), plus
  `09_RAG__var_demanding` and `11_multimodal__var_demanding` (manual overrides).
- **31 scored**: 5 CRITICAL, 7 HIGH, 10 MODERATE, 9 COMFORTABLE.
- **12 articles recommended for replication first** (CRITICAL + HIGH, sorted by margin):
  `09_RAG__var_standard` (−0.0148), `06_tools__var_standard` (−0.0046),
  `03_context_engineering__var_standard` (0.0148), `06_tools__var_demanding` (0.0176),
  `11_multimodal__var_standard` (0.0182), `Distinct_AI_Models__mixeddepth` (0.0212),
  `Earth_Oceans_Origin` (0.0246), `04_structured_outputs` (0.0267),
  `Understanding_Reasoning_LLMs` (0.0271), `10_memory_knowledge_access__var_demanding` (0.0295),
  `Insects_Consciousness__mixeddepth` (0.0522), `03_context_engineering__var_demanding` (0.0564).

Two of these (`09_RAG__var_standard`, `06_tools__var_standard`) have negative margins *without*
being policy/override cases — genuine near-tie-band decisions where the S3/S4/S5 secondary
signals picked an arm other than the raw reward leader. These are exactly the low-confidence
labels this investigation set out to find.

**How to use this going forward:** run `python3 training/audit_oracle_margins.py` any time new
articles are added or existing ones are corrected; feed the CRITICAL/HIGH list into §20's fix #4
(targeted write+grade-only replication) instead of guessing which of the 40 labels to double-check
first. Thresholds are provisional (derived from 2 before/after comparisons that mix a deliberate
edit's effect with pipeline noise, not a clean noise-only replicate) — §20's fix #3 (a real,
noise-only replicate-2–3× experiment on a small sample) should be used to recalibrate both these
tiers and `EPS_BAND` itself with an actual empirical noise distribution.

## 23. Temperature fix landed + noise-measurement experiment designed for the 2 narrowest margins

**Fix #1 from §20 (free, done):** created `writing_workflow/configs/rl_generation.yaml`, an exact
copy of `course.yaml` with only `write_article` and `integrate_exploration` lowered from
`temperature: 0.7` to `temperature: 0.25`. `course.yaml` (real published course content) is
untouched. Selected per-invocation via the existing `CONFIG_FILE` env var — never edited
`writing_workflow/.env`, so default behavior for any other script/run is unaffected:
```
CONFIG_FILE=configs/rl_generation.yaml uv run python rl_writing_generator.py ...
```

**Experiment target, from §22's audit:** the two narrowest NON-policy-forced margins in the whole
corpus — `09_RAG__var_standard` (margin=−0.0148, `light` vs `standard`) and `06_tools__var_standard`
(margin=−0.0046, `deep` vs `standard`) — both genuine near-tie decisions where the S3/S4/S5
secondary signals, not a clean reward win, picked the recorded arm.

**Design (implements §20 fix #3, "cheap noise measurement," scoped to these 2 articles):**
reuse each article's existing `research.md`/`.research/` (Phase 1 already done, zero re-scrape
cost) and re-run *only* write+grade — at the new 0.25 temperature — **3× per arm**, then compare
the resulting article-level margin/oracle_arm distribution against the original single-draw
(temperature 0.7) production label already on disk. This simultaneously (a) measures whether 0.25
reduces noise vs. the already-documented 0.7 swings, and (b) gives each of these 2 flagged articles
a majority-of-3 label instead of a single noisy draw.

**Mechanics (zero code duplication, zero production-data risk):**
- Both target articles are TRAIN *variant* articles, so their 4 arms map to presets `{0,1,3,5}`,
  not `0-3` (presets 2/4 are archived — see `generate_episode_oracles.py::_ARM_PRESETS`). Verified
  this explicitly before designing the replicate copy step, since naively using `--presets 0 1 2 3`
  would have silently used the wrong (archived) episodes for `standard`/`deep`.
- New `training/setup_noise_experiment.py` (read/copy only, no LLM calls) copies each arm's
  `article_guideline.md` + `research.md` + `.research/` from the real production episode dir into
  a **separate** root, `rl_training_data/noise_experiment/<article>__replicate{1,2,3}__preset{p}/`
  — the real `rl_training_data/episodes/` (actual GRPO training data) is never touched, and no
  pre-existing `article.md` is copied, so the writer runs fresh. Executed (dry-run first, then for
  real): all 24 replicate directories (2 articles × 3 replicates × 4 arm-presets) are now in place.
- Added a minimal, backward-compatible `--episodes-dir` CLI override to both
  `rl_writing_generator.py` and `rl_grading_generator.py` (default unchanged, so all existing
  invocations behave exactly as before) so the generators can be pointed at
  `rl_training_data/noise_experiment/` instead of the real episodes root.
- `rl_grading_generator.py` looks up ground truth via `EVAL_DATA_DIR/<article_name>/...`, which
  would not resolve for a name like `09_RAG__var_standard__replicate2`. Added
  `_strip_replicate_suffix()` (regex `__replicate\d+$` strip) so grading transparently resolves
  the replicate back to its base article's ground truth/guideline — no file duplication needed.
- New `training/measure_replicate_noise.py` (read-only analysis) imports (does not duplicate)
  `_section_reward`, `_get_score`, `_load_episode`, `_ARM_PRESETS` from
  `generate_episode_oracles.py` and `_compute_r_w` from `compute_article_oracle.py`, so the
  noise measurement uses the exact production reward formula and target-words weighting. For each
  article it reports: per-replicate article-level margin/oracle_arm, margin mean/std/range across
  the 3 replicates, an oracle_arm vote tally, per-section per-arm reward std across replicates
  (flagging any section/arm with std > 0.02), and a comparison against the original temperature-0.7
  single-draw label.

**Commands to actually run (writing_workflow/, real Gemini 2.5 Pro API cost — NOT yet executed,
awaiting go-ahead, consistent with this investigation's practice of not spending real budget
without confirmation):**
```
CONFIG_FILE=configs/rl_generation.yaml uv run python rl_writing_generator.py \
  --articles 09_RAG__var_standard__replicate1 09_RAG__var_standard__replicate2 09_RAG__var_standard__replicate3 \
             06_tools__var_standard__replicate1 06_tools__var_standard__replicate2 06_tools__var_standard__replicate3 \
  --presets 0 1 3 5 --episodes-dir ../rl_training_data/noise_experiment

uv run python rl_grading_generator.py \
  --articles 09_RAG__var_standard__replicate1 09_RAG__var_standard__replicate2 09_RAG__var_standard__replicate3 \
             06_tools__var_standard__replicate1 06_tools__var_standard__replicate2 06_tools__var_standard__replicate3 \
  --presets 0 1 3 5 --episodes-dir ../rl_training_data/noise_experiment
```
Then, from `research_agent_local/`:
```
python3 training/measure_replicate_noise.py --articles 09_RAG__var_standard 06_tools__var_standard
```

**Decision rule once data is in:** if the 3-replicate margin distribution for either article stays
consistently on one side of 0 (majority-of-3 agrees with the original oracle_arm), keep the
existing label as-is (the single draw got it right, or close enough). If replicates disagree with
each other or with the original (a genuine flip in >=1 of 3), treat the majority vote across all 4
draws (1 original + 3 replicates) as the corrected label, matching §20 fix #4's proportionate
philosophy — only these 2 (of 40) labels need this treatment right now.

## 24. Claude Sonnet added as a grading-judge option

**Context:** the user has been manually correcting Gemini grading mistakes with Claude Sonnet
since the start of this project (the `scores.json`/`reasoning.json` manual corrections referenced
in §16.5.2's "POST-CORRECTION UPDATE" were done this way) — Gemini occasionally makes blatant
LLM-as-judge errors. This section makes Claude Sonnet a first-class, selectable grading model
instead of a manual after-the-fact fix.

**Why this was a small change, not a rearchitecture:** `get_model()` in
`writing_workflow/src/brown/models/get_model.py` already wraps LangChain's generic
`init_chat_model("provider:model", ...)`, and both grading metrics (`FollowsGTMetric`,
`UserIntentMetric`) call `.with_structured_output()` on whatever model comes back — nothing in the
metric logic is Gemini-specific. Adding a provider is additive.

**Changes made:**
- `pyproject.toml`: added `langchain-anthropic>=1.0.0` (ran `uv sync` — installed cleanly,
  pulled in `anthropic==0.116.0` + `langchain-anthropic==1.4.8`).
- `brown/models/config.py`: added `SupportedModels.ANTHROPIC_CLAUDE_SONNET = "anthropic:claude-sonnet-4-5"`
  (naming matches the existing `claude-opus-4-5` fallback model already used elsewhere in this repo,
  in `research_agent_local/training/generate_digests.py`'s Layer-3 digest-generation fallback — a
  different, unrelated Claude integration via the raw `anthropic` SDK, confirming the naming
  convention) + a `DEFAULT_MODEL_CONFIGS` entry (`temperature=0.0`).
- `brown/config.py`: added `ANTHROPIC_API_KEY: SecretStr | None` to `Settings`.
- `brown/models/get_model.py`: added `SupportedModels.ANTHROPIC_CLAUDE_SONNET: "ANTHROPIC_API_KEY"`
  to `MODEL_TO_REQUIRED_API_KEY`. Gemini-only params (`thinking_budget`, `top_k`,
  `response_modalities`) are already stripped generically for any non-`google_genai:` model via
  `GOOGLE_ONLY_PARAMS`, and the `max_output_tokens`→`max_tokens` rename already applies to any
  non-Google provider — both needed zero special-casing for Anthropic.
- `.env.example`: added `ANTHROPIC_API_KEY=...` placeholder. **The user still needs to put a real
  key in their own `writing_workflow/.env`** — not done here (secret, not committed).
- `rl_grading_generator.py`: added `--grading-model {gemini,claude}` (default `gemini`, unchanged
  behavior). Refactored the module-level `_follows_gt_metric`/`_user_intent_metric` singletons into
  a `_build_metrics(model)` factory + `configure_grading_model(model)` function, called from
  `main()` right after argument parsing (before the pipeline starts) so both metrics are graded by
  the selected judge for the whole run.

**Verified (component-level, since this environment has no real `ANTHROPIC_API_KEY` to do a live
grading call):**
- `get_model(SupportedModels.ANTHROPIC_CLAUDE_SONNET, ...)` correctly raises
  `ValueError: Required environment variable 'ANTHROPIC_API_KEY' is not set` when the key is
  absent — proves the plumbing reaches the right code path instead of silently doing nothing.
- `uv run python rl_grading_generator.py --grading-model claude --dry-run --articles 09_RAG__var_standard`
  completed successfully end-to-end (`EXIT_CODE=0`, correct plan output) — confirms the new CLI
  flag, `configure_grading_model()`, and metric construction all wire together correctly for a
  real invocation, short of the actual paid API call itself.
- Noted (not a regression from this change): without `OPIK_API_KEY`/`OPIK_PROJECT_NAME` set,
  `rl_grading_generator.py` invocations have a real multi-second-to-~1-minute startup delay before
  the "not set" warning prints — pre-existing opik-client behavior, reproduces identically with the
  default Gemini judge, unrelated to the Claude addition.

**Usage once `ANTHROPIC_API_KEY` is set:**
```
uv run python rl_grading_generator.py --grading-model claude --articles <...> --presets <...>
```
Works with the existing `--episodes-dir` override too, so it can also be used to grade the §23
noise-experiment replicates with Claude instead of (or in addition to) Gemini — which would turn
that experiment into a way to decompose whether the measured noise is writer-content-driven,
judge-side, or both (grade the same replicate articles with both judges and compare agreement),
extending §23's original writer-temperature-only design.

# Part 5 — The enhancement-ceiling bias: a deterministic reward distortion (2026-07-13)

## 25. Finding: section-level binary enhancement scoring caps credit at the first valid instance

**How this surfaced:** while auditing the 09_RAG noise-experiment replicates (§23), the user
noticed that the higher-exploration presets (3, 5) insert *substantially more* exploration-sourced
content than preset 1, yet their `depth_enhancement`/`breadth_enhancement` scores are no higher —
while their `guideline_adherence`/`core_content`/`flow` scores are often *lower*. An Opus 4.8
recount (attached as `rl_training_data/noise_experiment/09_RAG/enhancement_ceiling_analysis.md`)
quantified it: across 54 body-sections, every one of the 31 zero-instance sections scores enh=0 and
every one of the 23 sections with ≥1 instance scores enh=1 — including every 6-instance section.
No second/third/sixth instance ever bought additional credit.

**Verified directly from the grader's own `reasoning.json` (not just the recount):** I read the
per-section depth/breadth reasoning for the "Advanced RAG Techniques" section across all 9
non-skip episodes. The grader itself enumerates multiple qualifying, source-attributed instances
while still emitting a single binary `1`:
- `preset3_rep1` depth=1: *"**Multiple** qualifying depth additions are present: (1) the Reciprocal
  Rank Fusion explanation… (2) the chunking failure-modes paragraph… (3) the GraphRAG computational
  complexity paragraph…"* — three distinct source-traceable additions across three subsections.
- `preset5_rep2` depth=1: *"**Multiple** qualifying depth additions are present: (1) the bi-encoder
  vs. cross-encoder architecture explanation… (2) the query-decomposition 'open challenge'… (3)
  HyDE's precision limitation…"* — three distinct additions.
- `preset1_rep1` depth=1: *"A depth addition is present: the GraphRAG subsection includes a
  paragraph noting that 'advanced GraphRAG systems are also becoming more dynamic…'"* — **one**
  addition, one source.

`preset5_rep2`'s three differently-sourced technical additions (concrete latency/throughput data,
an open-research-problem framing, a named algorithmic limitation) are objectively more informative
to a reader than `preset1_rep1`'s single sentence, and they score identically (`1`). This confirms
the user's hypothesis exactly.

**The mechanism, traced to exact code:**
1. **Grader** (`writing_workflow/src/brown/evals/metrics/new_follows_gt/prompts.py`, criteria 4 &
   5): *"The section scores 1 if at least one instance qualifies; unqualified instances do not lower
   the score."* The output type (`types.py::FollowsGTCriteriaScores`) is
   `CriterionScore.score: Annotated[int, Ge(0), Le(1)]` — hard binary. The grader already reasons
   **per-instance** (the prompt mandates per-instance source-attribution and the reason text
   enumerates them) — it just discards the count when it collapses to the binary.
2. **Reward formula** (`generate_episode_oracles.py::_section_reward`, the active "Formula B"):
   ```python
   explore = cp * (0.60 * de + 0.40 * be) * 0.50     # de, be ∈ {0, 1}
   ```
   With binary `de`/`be`, `explore` is hard-capped at `0.5 * cp` regardless of how many valid
   instances a section contains. One instance and six instances yield an identical explore term.
   (`train_grpo.py::_compute_episode_reward` has the same `cp * (0.60*de + 0.40*be) * w` shape, but
   it is the **legacy** episode-path formula; the active training target is
   `compute_oracle_reward`, which reads the per-section arm labels that `_section_reward` already
   baked into `section_oracle.json`. So `_section_reward` is the single source of truth for this
   bias.)
3. **The asymmetry that makes it a *bias*, not just a lost opportunity:** extra instances have
   **zero marginal upside** (capped explore term) but a **real marginal downside** — the attached
   recount measured instance-count↔word-overage at r≈+0.56, and word overage is exactly what
   `guideline_adherence` (via `user_intent = (0.50*ga + 0.50*ra) * 0.30`) penalizes, with no
   corresponding cap protecting it. So the arms that do more exploration (standard/deep) pay a
   length cost for content they get no enhancement credit for.

**Why this matters well beyond one section:**
- It is **deterministic**, not stochastic — unlike the Part 4 temperature noise, it biases *every*
  grading of *every* article the same direction, so it is baked into all 40 existing oracle labels.
- It is a **plausible structural contributor to the persistent `light`/P1 majority** documented in
  §13 (TRAIN skip9/light9/std3/deep3, TEST light9/16). If `standard`/`deep` structurally cannot
  earn credit for the extra exploration they perform beyond the first instance, while paying a real
  length cost for it, the oracle will systematically under-value them relative to `light` —
  independent of whether the extra research was genuinely good. This is a much larger concern than
  any single narrow-margin article, because it would mean the entire action-space's reward
  landscape is tilted toward under-exploration.

**Honest counter-data-point (keeps the finding calibrated):** `preset5_rep1` — the densest section
(6 raw instances) — scored `breadth_enhancement = **0**`: *"No clear breadth additions… the
additions found are primarily depth-oriented."* So the ceiling is not blind "count = waste":
content *type* still matters, and piling everything into one dimension can forfeit the other
entirely. The ceiling specifically bites *within* a dimension once ≥1 qualifying instance exists —
it does not make raw instance count a free proxy for quality.

## 26. Fix options — credit qualifying instances without re-opening the length-stuffing hole

**Decision taken (user, 2026-07-13):** credit qualified, valid enhancement instances in the depth
and breadth scores rather than capping at the first. The design tension to respect: the binary cap
was (implicitly) *also* protecting against citation-stuffing — a naive uncapped count would just
reward length, which the length penalties (`ga`, `core_preservation`) are simultaneously fighting.
So the fix must credit *additional distinct, qualifying, quality-gated* instances with **diminishing
returns and a hard cap**, keeping the length counterweight intact.

**Grader change (shared by all options):** `depth_enhancement`/`breadth_enhancement` must emit a
**count of qualifying instances** (capped, e.g. 0/1/2/3+) instead of a bare 0/1. This is a low-risk
change because the grader *already* enumerates and per-instance-qualifies additions — we are asking
it to report a number it already computes internally. Requires: (a) a new/extended structured-output
field for these two dimensions (the other four stay binary), (b) prompt wording changed from "scores
1 if at least one instance qualifies" to "report the number of distinct qualifying instances, capped
at N", (c) the `reasoning.json` writer already serializes `**{score}:**`, so a capped integer flows
through unchanged. **Cost: every episode must be re-graded** — existing `reasoning.json` files only
contain binaries, and counts cannot be reliably back-parsed from the free-text reason (the grader
sometimes stops enumerating once qualification is established). This is the expensive, unavoidable
part.

**Parsing changes (both must widen from binary to capped-integer):**
- `generate_episode_oracles.py::_parse_sections_ordered` regex `\*\*([01]):\*\*` → allow a small
  integer.
- `train_grpo.py::_parse_reasoning_sections` regex already allows `\*\*(\d):\*\*` (single digit) —
  fine for a cap ≤ 9, but it is the legacy path.

**Reward-formula options** (all keep `explore = cp * (0.60*de' + 0.40*be') * 0.50`, only changing
how the count → `de'`/`be'` ∈ [0,1] map is defined):

| Opt | Map from qualifying-instance count `n` → `de'`/`be'` | Effect on today's labels | Anti-stuffing |
|---|---|---|---|
| **A — reshape to fixed ceiling (recommended)** | concave saturating, e.g. `de' = 1 − (1−k)^n` (k≈0.55) → 0, 0.55, 0.80, 0.91, … OR explicit tiers {0:0.0, 1:0.6, 2:0.85, 3+:1.0} | 1-instance sections credited **less** than today (0.6 vs 1.0); multi-instance approach today's max. Relabels light-heavy sections downward, standard/deep upward — the intended correction. **Explore cap unchanged at 0.5·cp.** | Strong — ceiling never rises, so stuffing past the cap earns nothing; length penalty still bites |
| **B — raise ceiling for multi-instance** | linear-to-higher-cap, e.g. `de' = min(n, CAP)/CAP` with the outer multiplier raised so n=1 ≈ today's credit and n=CAP exceeds it | 1-instance sections unchanged (no light regression); multi-instance sections gain new headroom above today's max | Weaker — raises total explore weight, likely needs `cost`/`ga` rebalancing or stuffing re-emerges |
| **C — count × quality tier** | grader also tags each instance high/low value; `de'` = capped sum of per-instance quality weights | Most faithful to "number *and* quality"; most grader/schema complexity and most re-grading variance | Strong if quality gate is strict |

**Recommendation: Option A (concave, fixed ceiling).** It directly targets the diagnosed bias
(a single instance currently instantly maxes the dimension, over-crediting `light`) while preserving
the carefully-tuned overall reward scale and the anti-stuffing cap that took the §"Formula B"
deconfounding work to calibrate. It reshapes *how credit accrues up to the existing ceiling* rather
than raising the ceiling, so it does not reignite length-stuffing and does not require re-tuning the
cost term. The exact curve (tiers vs. `1−(1−k)^n`, the value of `k`/`CAP`) materially changes the
oracle labels and must be chosen deliberately and recorded — this is a parameter decision to make
*before* mass re-grading, not after.

**Unavoidable consequences to acknowledge before starting:**
- **Full corpus re-grade + full oracle regeneration.** All 40 article labels change; the run13/14
  baselines become non-comparable (a *new* oracle version, not a patch). This should be a versioned
  cut (`section_oracle.json` version 3), not an in-place edit.
- **Validate the direction on a cheap pilot first.** The §23 noise-experiment episodes are already
  written and graded-once; re-grade just those (2 articles × 3 replicates × 4 arms, and ideally with
  `--grading-model claude` per §24 since Claude is the more reliable judge) under the new
  count-emitting prompt, run the new `_section_reward` map, and confirm standard/deep oracle rewards
  rise relative to light *in the predicted direction and magnitude* before committing to a
  40-article re-grade.

**Recommended sequence:** (1) settle the Option-A curve parameters (tiers or `k`, and the cap N);
(2) implement the grader schema + prompt change and the two parser widenings; (3) pilot-re-grade the
§23 episodes with Claude, apply the new formula, inspect the shift; (4) only then commit to the full
40-article re-grade + `section_oracle.json` v3 + `article_oracle.json` regeneration. Nothing is
implemented yet — this section is the design to sign off on first, because steps (2)-(4) are a
one-way, whole-corpus change.

## 27. Locked design (user decisions, 2026-07-13): hybrid count×quality, cap 3, pilot first

User chose: **reshape-to-fixed-ceiling *blended with* count×quality** (Option A refined toward C),
**cap N = 3**, and **pilot on the §23 noise-experiment episodes first** (re-graded with Claude).

**Key de-risking insight that shapes the whole implementation:** the count→credit map lives in
`generate_episode_oracles.py::_section_reward` (oracle-computation time), **not** in the grader.
So the grader only has to reliably emit, per section per enhancement dimension, a small, stable
signal — **(a) a capped count of qualifying instances (0-3), and (b) a quality tier** — and *all*
weight/curve tuning happens downstream, cheaply and re-runnably, with **no re-grading**. Re-grading
(the only expensive step) is therefore needed **once** to produce (count, quality); the reward
weights can then be re-tuned for free as many times as wanted by just re-running
`generate_episode_oracles.py` + `compute_article_oracle.py`.

**Grader schema (the part that must be pinned before re-grading, since it is baked into the graded
output):** for `depth_enhancement` and `breadth_enhancement` only (the other 4 dims stay binary),
emit:
- `count`: integer 0-3 = number of *distinct, quality-gated, source-attributed* qualifying
  instances, capped at 3 (instances beyond 3 are not counted — anti-stuffing at the source).
- `quality`: `"high" | "standard"` = the dominant value tier across the qualifying instances
  (meaningful only when `count ≥ 1`). "high" = substantive, differently-sourced, materially
  informative additions; "standard" = valid-but-modest additions. Two tiers (not three) to keep
  LLM-judge output stable and reproducible.

**Proposed reward map (freely tunable downstream, defaults shown) in `_section_reward`:**
```
_ENH_COUNT_CREDIT = {0: 0.00, 1: 0.55, 2: 0.80, 3: 1.00}   # concave, diminishing, fixed ceiling
_ENH_QUALITY_MULT = {"high": 1.00, "standard": 0.85}
def _enh_credit(count, quality):
    base = _ENH_COUNT_CREDIT[min(count, 3)]
    return base * (_ENH_QUALITY_MULT[quality] if count >= 1 else 1.0)
# de' = _enh_credit(depth_count, depth_quality);  be' = _enh_credit(breadth_count, breadth_quality)
# explore = cp * (0.60*de' + 0.40*be') * 0.50   ← unchanged shape & 0.5·cp ceiling
```
Resulting `de'`/`be'` grid: 0→0.00, 1·standard→0.47, 1·high→0.55, 2·standard→0.68, 2·high→0.80,
3·standard→0.85, 3·high→1.00. A single instance is credited **less** than today's 1.0 (the intended
correction to `light`'s over-crediting); full credit requires 3 high-quality instances; the explore
term never exceeds today's `0.5·cp` ceiling (anti-stuffing preserved, cost term untouched).

**Full change set (staged, not yet implemented):**
1. Grader `types.py`: new field shape for depth/breadth carrying `count` (0-3) + `quality`
   (`high`/`standard`); other 4 dims unchanged.
2. Grader `prompts.py`: criteria 4 & 5 reworded from "scores 1 if at least one instance qualifies"
   to "report the number of distinct qualifying instances (cap 3) and their dominant quality tier";
   the reasoning-format instruction and the pass-2 core-preservation context builder updated to
   carry the new signal; the `if not exploration_sources` hard-zero mandate in `metric.py` updated
   to zero the count (not a binary).
3. Few-shot examples (~18 sections, ~36 depth/breadth entries): re-annotated with counts + quality
   consistent with the new schema. **Highest-effort, error-prone piece** — the examples define the
   output format the judge imitates.
4. Parsers: `generate_episode_oracles.py::_parse_sections_ordered` (`\*\*([01]):\*\*` → capped int +
   quality) and `train_grpo.py::_parse_reasoning_sections` (legacy path) widened.
5. `_section_reward`: the `_enh_credit` map above; `section_oracle.json` bumped to **version 3**.
6. Pilot: re-grade the 24 §23 noise episodes with `--grading-model claude`, re-run oracle
   computation, confirm standard/deep rewards rise vs light in the predicted direction/magnitude
   before the full 40-article re-grade.

**Status: awaiting final go-ahead on the grader schema (count 0-3 + quality high/standard) before
rewriting the judge**, since that schema is the one piece baked into the (paid) re-grade and
expensive to change afterward; the reward weights above are deliberately downstream and re-tunable
without re-grading.

## 28. Implemented: grader + reward-map changes (2026-07-13)

Final design differs slightly from §27's proposal in one respect: the grader's `score` field for
depth_enhancement/breadth_enhancement **stays exactly binary (0/1)**, not (count, quality) as a new
Pydantic field. The richer signal instead lives entirely in the free-text `reason` field via a
mandated tag `[instances=N; quality=tier1,tier2,...]` (N = true, uncapped count; tiers = "strong"/
"standard" per instance). This is a strictly smaller, lower-risk change than editing `types.py`'s
schema: `to_score_result()`'s existing [0,1]-aggregation (feeding `scores.json`) needed zero changes,
and `generate_episode_oracles.py` already parses `reasoning.json` as free text — it now just also
extracts this tag, exactly matching how the grader was already observed enumerating multiple
instances in §25's real production examples.

**Grader changes (`writing_workflow/src/brown/evals/metrics/new_follows_gt/`):**
- `prompts.py`: criteria 4 & 5 now instruct enumerating *every* qualifying instance (not stopping at
  the first) and classifying each as **strong** (substantive/specific/quantified/named) or
  **standard** (valid but brief/generic); instruction 10 mandates the `[instances=N; quality=...]`
  tag immediately after the `**{score}:**` marker, with worked single- and multi-instance examples
  inline in the prompt text; CoT step 3.5 added to finalize the tag after the existing 3.4
  traceability check. All 18 few-shot example sections' depth/breadth `reason` strings (28 of 36 —
  the 2 fully-omitted/empty and 2 References sections were left as-is, not informative for this)
  were retrofitted with tags consistent with their described content.
- `metric.py`: the code-level hard-zero mandate (`_NO_EXPLORATION_SOURCES_REASON`, forces
  depth/breadth to 0 when no exploration sources exist) now embeds `[instances=0]` too, so the tag
  is present regardless of whether the 0 came from the judge or this override.

**Reward-map changes (`research_agent_local/training/`):**
- New `enhancement_reward.py` — the *only* place the count→credit curve lives, with 3 tunable
  constants at the top (`INSTANCE_CAP=3`, `QUALITY_WEIGHT={"strong":1.0,"standard":0.65}`,
  `CREDIT_AT_WEIGHTED_COUNT={0:0.00,1:0.55,2:0.80,3:1.00}`) and one function,
  `enhancement_credit(qualities) -> float`, that sums per-instance weights, caps at `INSTANCE_CAP`,
  and smoothly interpolates between the integer credit tiers. **Retuning weights/curve/cap never
  requires re-grading** — only re-running `generate_episode_oracles.py` + `compute_article_oracle.py`,
  since (count, qualities) are parsed fresh from already-graded `reasoning.json` every time.
  Verified: `[] -> 0.0`, `["standard"] -> 0.3575`, `["strong"] -> 0.55`, `["strong","strong"] -> 0.80`,
  `["strong"]*3 -> 1.00`.
- `generate_episode_oracles.py`: `_parse_sections_ordered` now captures the full reason text and
  extracts the tag via a new `_parse_enhancement_tag`; `_get_score` unchanged in behavior; new
  `_get_enhancement` mirrors `_get_score`'s exact/substring/ordinal lookup but returns the parsed
  `(count, qualities)` or `None`. In `process_article_variant`, `de`/`be` are now computed by a
  `_enh_credit` closure that calls `enhancement_credit(qualities)` **only when the tag is present**;
  when absent (legacy, un-migrated `reasoning.json`) it falls back to the raw binary score,
  unchanged. `section_oracle.json` bumped to **version 3**; module docstring documents the schema
  and the legacy fallback guarantee.
- **Critical bug caught before it did damage:** the first implementation fabricated a fallback
  `(count=score, qualities=["standard"]*score)` for untagged data, which then ran through
  `enhancement_credit` — silently turning every existing article's binary `1.0` into `0.3575`
  (`enhancement_credit(["standard"]) = 0.3575 ≠ 1.0`), i.e. corrupting all 40 un-migrated oracle
  labels' rewards on the very next `generate_episode_oracles.py` run, with no error or warning.
  Caught by directly testing the curve function before trusting the pipeline result. Fixed by making
  the absent-tag case a real `None` sentinel that bypasses `enhancement_credit` entirely and uses
  the raw score — verified via a real backup-diff-restore test on `09_RAG`'s 3 variants (all 6
  sections × 3 variants: **bit-identical rewards** before/after, only `version`/`computed_at`
  changed) and a synthetic multi-instance parse test (3 instances, 2 strong + 1 standard →
  `enhancement_credit` = 0.93, correctly below the 1.00 ceiling since not all 3 are "strong").
- `compute_article_oracle.py`: docstrings updated to acknowledge `section_oracle.json` v2 *or* v3
  (its own logic reads already-computed reward floats, so it needed no logic change); the version
  guard (`v < 2`) already accepted v3 without modification. `article_oracle.json`'s own version
  field stays 2 — its schema is unchanged, only its upstream input's semantics changed.

**Tests added** (`writing_workflow/tests/brown/evals/metrics/follows_gt/test_follows_gt_metric.py`):
new regression tests asserting the tag format, the strong/standard rubric, the
enumerate-every-instance instruction, the multi-instance worked example, and CoT step 3.5 are all
present in `SYSTEM_PROMPT`; that `DEFAULT_FEW_SHOT_EXAMPLES` were actually retrofitted (contains
`[instances=0]`, `[instances=1; quality=strong]`, `[instances=1; quality=standard]`); that the
rendered eval prompt carries the tags through; and that the hard-zero mandate's reason (both the
raw constant and end-to-end through `.score()`) carries `[instances=0]`. Existing fixtures/tests
were left untouched — they test aggregation logic with generic placeholder reasons unrelated to the
tag, so they needed no changes and continue to pass by inspection (no `score`/type changes were made
that they could regress on).

**Could not live-verify the full pytest suite in this environment** — `uv run pytest` produced no
output across repeated sync and async terminal attempts (worse than the usual slow-opik-start delay;
not root-caused, see debugging notes). All changes were instead verified individually: `get_errors`
on every modified file (clean), direct execution of `enhancement_reward.enhancement_credit` against
hand-computed expected values, a real backup/diff/restore run of `generate_episode_oracles.py`
against production `09_RAG` data (bit-identical), and a synthetic multi-instance parse test. User
will run the test suite manually.

**Claude pilot re-grade command** (writing_workflow/, real API cost — the §23 noise-experiment
episodes already have `article.md` from the writer step; this re-grades them with the new
tag-emitting prompt so `enhancement_credit` has real data to work with instead of the legacy
fallback):
```
uv run python rl_grading_generator.py --grading-model claude \
  --articles 09_RAG__var_standard__replicate1 09_RAG__var_standard__replicate2 09_RAG__var_standard__replicate3 \
             06_tools__var_standard__replicate1 06_tools__var_standard__replicate2 06_tools__var_standard__replicate3 \
  --presets 0 1 3 5 --episodes-dir ../rl_training_data/noise_experiment
```
Note this **re-grades** existing `article.md` files (scores.json for these episodes was already
written by the earlier Gemini pass per the last turn's noise-measurement results) — grading is
idempotent-guarded by `scores.json` existing, so **delete the existing `scores.json`/`reasoning.json`
in each of these 24 episode dirs first** if the intent is to replace the Gemini grades with Claude's
tag-emitting ones (rather than accumulate both): e.g.
```
find ../rl_training_data/noise_experiment -maxdepth 1 -name '09_RAG__var_standard__replicate*' -o -name '06_tools__var_standard__replicate*' \
  | xargs -I{} rm -f {}/scores.json {}/reasoning.json
```
Then, from `research_agent_local/`, re-run oracle computation and inspect the shift:
```
python3 training/generate_episode_oracles.py --articles 09_RAG 06_tools
python3 training/compute_article_oracle.py --article 09_RAG__var_standard
python3 training/compute_article_oracle.py --article 06_tools__var_standard
```
Per §23/§27's pre-registered decision rule, look for standard/deep rewards rising relative to light
in the sections that had multiple qualifying instances in the earlier §25 analysis — that is the
signal confirming the fix works before committing to the full 40-article re-grade.

## 29. Bug found and fixed: the cap must select the STRONGEST N instances, not the first N

**User caught this before the pilot re-grade was run.** `enhancement_credit()`'s original
implementation was `qualities[:INSTANCE_CAP]` — i.e. it took the first `INSTANCE_CAP` (3) entries
in whatever order they appeared in the list, not the three *strongest*. Demonstrated directly:
```python
enhancement_credit(["standard", "standard", "strong", "strong"])  # weak instances listed first
# -> 0.86  (WRONG: took the first 3 = standard, standard, strong)
enhancement_credit(["strong", "strong", "standard", "standard"])  # same 4 instances, strong first
# -> 0.93  (the "correct" value — same underlying instances, different reported order)
```
Two identical sets of underlying instances produced different credit purely because of list order —
exactly the kind of order-dependence the cap is supposed to be immune to.

**Fix (`enhancement_reward.py`):** `enhancement_credit()` now sorts the quality weights descending
before applying `INSTANCE_CAP`, so the strongest instances are always the ones counted regardless of
input order:
```python
weights = sorted((QUALITY_WEIGHT.get(q, _DEFAULT_QUALITY_WEIGHT) for q in qualities), reverse=True)
weighted = sum(weights[:INSTANCE_CAP])
```
Verified both orderings of the same 4-instance set now produce identical credit (0.93), and a
6-instance mixed-order case correctly resolves to its 3 strongest instances (all "strong" → 1.00).

**A companion gap at the grader level, fixed too:** the tag-format instruction (instruction 10)
already caps the *reported* quality list at 5 entries when N > 5, but originally said to list them
"in the order discussed" — not strongest-first. If a section has, say, 7 qualifying instances and
the two strongest are discussed 6th and 7th, they would never make it into the reported 5-slot list
at all, and no amount of sorting downstream can recover a value that was never reported. Fixed:
instruction 10 (and CoT step 3.5) now mandate the quality list be **strongest-first** (all "strong"
entries before any "standard" entries), with a new worked example: 7 instances (4 strong, 3
standard) → `[instances=7; quality=strong,strong,strong,strong,standard]` (the fifth slot filled by
one standard entry, not by prose-discussion order). `enhancement_credit()`'s own defensive sort
still applies as a second safeguard, but the grader should not rely on that alone since it can only
sort what actually got reported.

**Tests added:** `test_system_prompt_requires_strongest_first_quality_ordering` and
`test_system_prompt_documents_seven_instance_ordering_example` in `test_follows_gt_metric.py`,
verifying the new instruction text and worked example are present; the existing
`test_system_prompt_documents_multi_instance_tag_example` (3-instance case) was left unchanged and
still matches, since that example's text was untouched.

This bug is caught **before** the §28 Claude pilot re-grade command was run, so it does not require
re-doing any already-spent API cost — the fix lands cleanly before the pilot begins.

## 30. First real Claude + enhancement-credit re-grade: 09_RAG__var_standard

**Methodological fact worth recording:** ground-truth articles (`article_ground_truth.md`, used as
`expected_output` in `FollowsGTMetric`) were written at **temperature 0.7, with zero exploration
rounds** — i.e. GT itself corresponds to a "skip"-arm-like writing pass, not an idealized
deep-research article. This matters for interpreting `core_content`/`flow`/`core_preservation`
comparisons: GT's own comprehensiveness ceiling (whatever a single temp-0.7 no-exploration draft
happens to cover) may already be the limiting factor for how much room *any* arm's depth/breadth
additions have to matter, independent of the reward formula. This plausibly compounds with §30's
finding below that 4 of 6 sections show zero enhancement signal for every arm — GT's own sections
may simply not leave room for qualifying additions there, regardless of exploration depth.

**Result:** re-graded `09_RAG__var_standard`'s real production episodes (skip/light/standard/deep,
same temp-0.7 content, only the grading changed: Claude + the new enhancement-credit formula).
`r_w = {skip:0.372, light:0.397, standard:0.391, deep:0.392}` — light/standard/deep compressed into
a **0.006-wide band** (down from the old Gemini/binary formula's 0.036-wide band), oracle=standard,
margin=-0.0056 (near-tie band = all three). This is the enhancement fix working as designed — light
no longer gets free full credit for a single instance — but the *consequence* is a harder, not
easier, decision: this article was arguably never cleanly decided, just artificially separated by
the old ceiling's over-crediting of light.

**3 noise-experiment replicates (temp=0.25, same new grading) disagreed with each other:**
replicate 1 → standard (margin +0.014), replicates 2 & 3 → light (margins +0.150, +0.148). Decision
rule (§23/§27, majority across original + 3 replicates) lands on a **2-2 tie** (standard: orig+rep1;
light: rep2+rep3) — genuinely unresolved, not a case to force a pick on.

**New finding, separate from the enhancement fix:** `deep`'s reward specifically degrades at
temperature 0.25 relative to the temp-0.7 original in every section shown (Advanced RAG Techniques
0.49→0.12, Agentic RAG 0.78→0.29, Conclusion 0.44→0.39), touching negative raw values in multiple
replicates — a much sharper decline than skip/light/standard show. Since grading (Claude, new
formula) is now held constant across this comparison, the difference is a genuine content-quality
effect of writing at 0.25 vs 0.7, not a grading artifact. Working hypothesis: `deep`'s 3-round
exploration content is the hardest to integrate coherently, and a lower, less-creative temperature
may specifically hurt that harder integration task — complicating §21's "temperature reduction is
neutral-to-positive" prediction, which may hold for skip/light but not for deep. Needs a second data
point (`06_tools__var_standard`, not yet re-graded) before treating this as a general pattern.

**Diagnostic: why the near-tie, exactly (not guessed — read directly from the re-graded
`reasoning.json`'s `[instances=N; quality=...]` tags for `09_RAG__var_standard`'s real preset0/1/3/5
episodes):**

| Section | light | standard | deep |
|---|---|---|---|
| Advanced RAG Techniques (depth) | 1 strong → credit 0.55 | 3 strong → credit **1.00** | 3 strong + 1 standard → credit **1.00** (4th instance discarded by `INSTANCE_CAP=3`) |
| Agentic RAG (depth) | 1 strong → credit 0.55 | 1 strong → credit 0.55 | 3 strong → credit **1.00** |
| *(4 other sections)* | 0 for all arms — GT's own sections leave no room for qualifying additions regardless of arm |

Two distinct effects compound: (1) `INSTANCE_CAP=3` genuinely discards deep's 4th instance in
"Advanced RAG Techniques," tying it with standard's 3 there even though deep did more; (2) 4 of 6
sections carry zero enhancement signal for *any* arm, diluting whatever separation the 2 live
sections produce once target-words-weighted into the article-level R_w.

**Answered: would tuning `enhancement_reward.py`'s parameters produce a clearer signal here?**
Partially, and the objective matters. Two separable claims:
- *"Is `INSTANCE_CAP=3` too low in general?"* — Plausibly yes, on principled grounds independent of
  this article: §25's original recount already found real sections with up to 6 genuine qualifying
  instances, and this data shows a real 4th instance being discarded. Raising the cap (and extending
  the credit ladder, e.g. to 4-5) is defensible on its own merits.
- *"Would that alone resolve 09_RAG's near-tie?"* — Only partially. A higher cap would let deep pull
  ahead of standard in "Advanced RAG Techniques," but 4 of 6 sections would still contribute zero
  differentiating signal, so the article-level margin would likely stay thin rather than resolve
  decisively. **Recommendation: do not tune the curve with "fix this one article's margin" as the
  goal** — that is reverse-engineering a single data point. Any cap change should be evaluated across
  multiple re-graded articles (06_tools next, eventually the full corpus), with 09_RAG as one data
  point among several, not the target of the tuning.

**Status:** `09_RAG__var_standard` treated as a genuine, unresolved near-tie (2-2 replicate split) —
not forcing a label change on it. Awaiting `06_tools__var_standard`'s re-grade before drawing
conclusions about the temperature-sensitivity-of-deep finding or the `INSTANCE_CAP` question.

## 31. Second re-grade: 06_tools__var_standard — a contrast case, not a replication

**Result:** `r_w = {skip:0.372, light:0.502, standard:0.581, deep:0.565}`, oracle=`deep`, margin
=-0.0159 (near-tie band=[standard, deep]) — deep was picked via secondary-signal tie-break even
though `standard` (0.5813) is the raw R_w leader over `deep` (0.5654). Directionally consistent with
the old Gemini/binary result (also `deep`, margin -0.0046) — this article's standard-vs-deep
contest, unlike 09_RAG's light/standard/deep compression, was **not** dramatically reshaped by the
enhancement fix; light (0.502) stays clearly behind both.

**Replicates: clean 3-1, not a tie.** All 3 temp=0.25 replicates agree with each other (all →
`standard`) and disagree with the original's tie-break-selected `deep`: replicate margins +0.006,
+0.089, +0.020, all favoring `standard`. Majority across all 4 draws (1 original + 3 replicates):
**standard 3, deep 1** — unlike 09_RAG's genuine 2-2 deadlock, this resolves cleanly per the §23/§27
decision rule. **Recommendation: relabel `06_tools__var_standard`'s oracle_arm from `deep` to
`standard`** — the original's `deep` pick came from a secondary-signal tie-break on an already-thin
margin (standard was the raw leader even in the original single draw), and 3 independent replicates
confirm `standard` is the more robust answer, not an artifact of a single noisy draw.

**Hypothesis check #1 — "deep degrades at temperature 0.25" (from §30): does NOT replicate.**
deep's aggregate reward barely moves (0.565→0.556 mean across replicates, essentially flat), and
per-section changes are a **mix** of increases and decreases (S3 0.41→0.52 up, S5 0.535→0.57 up, S7
0.93→0.77 down, others roughly flat) — nothing resembling 09_RAG's uniform, often-negative collapse
across every section. **Retracting that hypothesis as a general pattern**: it was most likely
specific to 09_RAG's own exploration content (its "Agentic RAG"/"Advanced RAG Techniques" material
may simply be harder to integrate coherently at lower temperature), not a general
temperature×deep-arm interaction. What actually flipped 06_tools's label is far more mundane:
`standard` modestly improved (0.581→0.598) while `deep` stayed flat — enough to tip an
already-razor-thin, tie-break-decided margin. This is consistent with (not a new contradiction of)
Part 4's general finding that meaningful write-content noise persists even at reduced temperature.

**Hypothesis check #2 — is `INSTANCE_CAP=3` generally too low? Mixed evidence, cuts against a quick
fix.** Diagnostic tags for `06_tools__var_standard` (read directly from `reasoning.json`):

| Section (depth) | light | standard | deep |
|---|---|---|---|
| Understanding Why Agents Need Tools | 0 | 2 strong → 0.80 | 0 |
| Implementing Tool Calls from Scratch | 0 | 0 | 2 strong → 0.80 |
| Implementing a Tool Calling Framework | 0 | 0 | 3 strong → **1.00** (exactly at cap — nothing discarded) |
| Production-Level Tool Calls w/ Gemini | 0 | 0 | 1 strong → 0.55 |
| Pydantic Models as Tools | 0 | 0 | 1 strong → 0.55 |
| Downsides of Running Tools in a Loop | 3 strong → **1.00** | 2 strong → 0.80 | 3 strong → **1.00** |

Unlike 09_RAG (where deep's real 4th instance in "Advanced RAG Techniques" was discarded by the
cap), deep never exceeds 3 in any section here — `INSTANCE_CAP` is simply not the limiting factor
for this article. What separates deep/standard from light instead is **breadth of sections touched**
(deep qualifies in 5/9 sections, standard in 2/9, light in only 1/9, where it actually ties deep's
1.00). Two articles, two different limiting mechanisms for their near-ties. This reinforces last
turn's caution rather than resolving it: `INSTANCE_CAP` is not a universal bottleneck across
articles, so raising it is not obviously the right lever in general — it would help 09_RAG's specific
case and do nothing for 06_tools's. Any cap change still needs evaluation across many more
re-graded articles, not these 2.

**Updated status after both re-grades:**
- `09_RAG__var_standard`: genuine unresolved near-tie (2-2 split) — leave as `needs_review`, no label
  change forced.
- `06_tools__var_standard`: clean correction available — relabel oracle_arm `deep` → `standard` per
  the 3-1 majority.
- The "temperature hurts deep" hypothesis from §30 is retracted as a general claim; it does not
  generalize beyond 09_RAG on this n=2 sample.
- The `INSTANCE_CAP` question remains genuinely open — the two articles hit different bottlenecks,
  so no change to `enhancement_reward.py`'s constants is warranted from this data alone.

## 32. `cost` vs. `explore` multiplier: which lever should encode "exploration quality was underrated"?

**Motivating observation (user, reading actual generated articles):** the depth/breadth enhancement
instances found during grading are qualitatively better than expected — prompting the question of
whether the `cost` coefficient (`-0.06 * nr` in `_section_reward`) should be reduced to make
exploration more attractive.

**Verified with a real sensitivity sweep (no re-grading — pure recompute from the already-graded
09_RAG/06_tools data) that `cost` is the wrong lever for this specific motivation.** `cost` is
purely mechanical: reducing its magnitude shifts every arm's reward by *exactly*
`Δcost_coef × nr`, independent of content:

| `cost_coef` | 09_RAG R_w (skip/light/standard/deep) | 06_tools R_w (skip/light/standard/deep) |
|---|---|---|
| -0.06 (current) | 0.372 / 0.397 / 0.391 / 0.392 | 0.372 / 0.502 / 0.581 / 0.565 |
| -0.03 | 0.372 / 0.427 / 0.451 / **0.482** | 0.372 / 0.532 / 0.641 / **0.655** |
| 0.00 | 0.372 / 0.457 / 0.511 / **0.572** | 0.372 / 0.562 / 0.701 / **0.745** |

`skip` (nr=0) is bit-identical across every value, confirming the shift is pure round-count
arithmetic, not a response to whether a given episode's exploration was actually well-integrated or
mediocre. `cost` cannot distinguish "this deep episode found genuinely great content" from "this
deep episode found forgettable content" — it uniformly favors more rounds regardless.

**The content-sensitive alternative — raising the `explore` multiplier (currently 0.50, i.e.
`explore = cp*(0.60*de+0.40*be)*explore_mult`)** — was tested the same way:

| `explore_mult` | 09_RAG R_w | 06_tools R_w |
|---|---|---|
| 0.50 (current) | 0.372 / 0.397 / 0.391 / **0.392** | 0.372 / 0.502 / 0.581 / **0.565** |
| 0.65 | 0.372 / 0.434 / 0.437 / **0.446** | 0.372 / 0.515 / 0.629 / **0.629** |
| 0.80 | 0.372 / 0.471 / 0.482 / **0.501** | 0.372 / 0.528 / 0.676 / **0.693** |

This also shifts standard/deep upward, but the shift is driven by each episode's actual
`(count, quality)` enhancement tags via `enhancement_credit()` — it responds to genuine content
differences (as evidenced by it *not* moving `skip` either, since skip has zero enhancement content
by construction), unlike `cost`'s uniform per-round arithmetic.

**Recommendation: if the underlying belief is "exploration content is better than the formula
credits," encode that via `enhancement_reward.py`'s curve or the `explore` multiplier — not
`cost`.** `cost` represents research effort/opportunity cost, a different concept from content
value, and lowering it risks making the model default toward more rounds uniformly regardless of
whether a specific article's guideline+goldens actually call for it. Same caution as §26/§31: n=2
articles is not a sufficient basis to commit to either change yet — this sweep is informative, not a
decision. Both levers are equally cheap to re-test (no re-grading needed) once more articles are
re-graded.

## 33. Persistent noise at temperature 0.25 — verified, and an honest gap in the evidence

**Verified the coefficient-of-variation (std/mean of the replicate margin distribution) for both
re-graded articles:** `09_RAG__var_standard` mean=+0.104, std=0.078 → **CV=75%**;
`06_tools__var_standard` mean=+0.038, std=0.045 → **CV=116%**. Both genuinely large relative to
their means, confirming substantial residual stochasticity even at the reduced temperature.

**A gap this exposes: we have never directly measured noise at temperature 0.7 with the same
controlled methodology (fixed `research.md`, N replicates) to compare against.** The belief that
0.25 reduces noise relative to 0.7 rests on *indirect* evidence — Part 4's mixed-depth pilots, which
showed large swings at 0.7 but also used fresh exploitation research each time, confounding
writer-noise with content-source noise. We assumed a reduction; we never quantified it directly.
What this experiment's design *does* give cleanly: fixed `research.md`/`.research` across all 3
replicates plus near-deterministic grading isolates writer-sampling-noise as the only varying
factor, so the 75%/116% CVs are a real, clean measurement of the residual noise floor **at 0.25**
specifically — just not a before/after comparison against 0.7.

**Reframed justification for using 0.25 despite the persistent noise:** the plan was never
"temperature reduction eliminates noise" — it was always **replicate + aggregate** (§20 fix #3/#4),
the same logic RL/GRPO relies on generally for noisy rewards. Temperature reduction's role is to
make that replication cheaper/more sample-efficient (if variance is genuinely lower, fewer draws
are needed for a stable estimate) and to reduce the frequency of pathological single-draw outcomes
(some 0.25 replicates still hit negative raw section rewards for `deep` in 09_RAG — even 0.25
doesn't fully prevent this, but a direct comparison would be needed to know whether 0.7 produces it
more often).

**Decision: the direct 0.7-vs-0.25 controlled replicate comparison is NOT being run.** Cost
estimated at $100+ (full write + grade + manual grading correction per replicate), and the user has
decided this isn't worth spending given the other open questions already competing for budget. This
is a deliberate, cost-based call, not an oversight — recorded here so the gap is documented as a
**known, accepted limitation** rather than a forgotten TODO: we do not have direct evidence that
0.25 reduces noise relative to 0.7, only indirect evidence (Part 4) and a plausible general prior
(lower temperature reduces LLM sampling variance). If a cheaper way to probe this becomes available
later — e.g. a write-only (no grading) structural-similarity comparison across multiple 0.7 vs 0.25
drafts, skipping the expensive LLM-judge step entirely — it would be worth revisiting opportunistically,
but is not being pursued now.

## 34. Reward-formula sweep tool + a counter-intuitive result: naive cap-extension backfires

Built `research_agent_local/training/sweep_reward_formula.py` — a reusable, read-only tool that
recomputes R_w/margin for named reward-formula variants (cost_coef, explore_mult, quality_weight,
instance_cap, credit_curve/exp_k) directly from already-graded `reasoning.json`, at **zero
re-grading cost**. `baseline` reproduces the real production numbers exactly (09_RAG
0.372/0.397/0.391/0.392, 06_tools 0.372/0.502/0.581/0.565), confirming the reimplementation is
faithful. Four named candidates were defined to make §32's "which lever" question concrete:

| Candidate | Change | Hypothesis |
|---|---|---|
| A `extended_ladder_cap5` | `INSTANCE_CAP` 3→5, ladder `{0:0,1:.55,2:.80,3:.93,4:.98,5:1.00}` | Recover 09_RAG's discarded-4th-instance credit |
| B `smooth_exp_k055_cap8` | `credit(n)=1-(1-0.55)^n`, cap raised to 8 (computational bound only) | Should returns diminish forever, never hard-cap at exactly 1.0? |
| C `higher_standard_weight` | `QUALITY_WEIGHT["standard"]` 0.65→0.80 | Is "standard"-tier content underweighted relative to "strong"? |
| D `explore_065`/`explore_080` | `explore_mult` 0.50→0.65/0.80 | Should exploration count for more overall, regardless of granular count/quality? |

**Result — A and B actively backfire in both re-graded articles, opposite of intent:**

| | 09_RAG `deep` R_w | 06_tools `deep` vs `standard` |
|---|---|---|
| baseline | 0.3918 | 0.5654 vs 0.5813 (margin 0.016 to standard) |
| extended_ladder_cap5 | **0.3860** (↓) | **0.5591** (↓, margin to standard *widens* to 0.022) |
| smooth_exp_k055_cap8 | **0.3871** (↓) | **0.5585** (↓) |

**Mechanism (worked out from the actual numbers, not assumed):** any monotonic curve bounded at
1.0 that extends past the old cap must lower the value *at* the old cap to make room above it (e.g.
tier-3 drops from a flat 1.00 to ~0.93). That only pays off for sections that genuinely *exceed* the
old cap. But in both real articles, `deep`'s advantage comes mostly from hitting **exactly** 3
instances in *multiple* sections (09_RAG's "Agentic RAG"; 06_tools's "Tool Calling Framework" and
"Downsides") — only one section across both articles (09_RAG's "Advanced RAG Techniques") actually
has a 4th instance to recover. The dilution across the many exactly-capped sections outweighs the
recovery in the one section that needed it, netting `deep` *lower* overall in both cases tested.
**Conclusion: do not pursue the cap/ladder-extension family as specified** — it does not do what it
sounds like it should, based on real data, unless a future article shows *many* sections genuinely
exceeding 3 (not just one), which would change the balance.

**Candidate C (quality-weight) — modest, does not backfire:** 09_RAG's raw-argmax flips to `deep`
(barely, margin 0.0007); 06_tools's `standard` lead narrows ~15% (0.0159→0.0134) without reversing.
Gentler than the cap approach since it only reweights already-counted instances — no
cap-interaction side effect to worry about.

**Candidate D (explore_mult) — most consistently effective, but coarsest:** confirms §32's earlier
finding; at 0.65 alone it makes 06_tools a near-exact tie (0.6287 vs 0.6290) and flips 09_RAG's
raw-argmax to `deep` (margin 0.0098).

**Non-obvious interaction found:** `cap5_plus_explore_065` (A+D combined) gives a *smaller*
deep-favoring margin than `explore_065` alone in both articles — the cap-extension's harm eats into
the explore-multiplier's benefit. The two levers are not independent; combinations need testing
together, not assumed additive.

**Overall recommendation:** based on real (not assumed) sensitivity data, **C and D are the
levers worth pursuing further** if the goal is crediting exploration content more generously — D is
the blunter/stronger tool, C the more surgical one, and neither backfires the way A/B do. Still n=2
articles — this informs which direction is *plausible*, not a decision to commit to any specific
value yet. `sweep_reward_formula.py` is reusable for testing new candidates as more articles are
re-graded, with zero additional API cost.

## 35. Full C×D grid (5×4=20 cells) — explore_mult systematically overturns the confirmed-correct label; quality-weight alone does not

Extended `sweep_reward_formula.py` with a programmatic grid crossing `explore_mult ∈
{0.50,0.60,0.70,0.80,0.90}` × standard-tier `quality_weight ∈ {0.65,0.75,0.85,0.95}` (20 cells), plus
a summary (winner/margin delta vs baseline) and a cross-article-agreement view. User ran the full
grid on both re-graded articles and shared the output (`sweep_20260716_130041.txt`).

**Critical asymmetry the analysis must respect:** the two test articles are NOT equally informative.
`06_tools__var_standard` has a **confirmed-correct label** — §31's real Claude re-grade gave a clean
3-1 replicate majority for `standard` (that's the whole reason the enhancement-ceiling fix
downgraded it from `deep`). `09_RAG__var_standard` does **not** — §30 found a genuine, unresolved
3-way near-tie (2-2 replicate split). This means: **06_tools's label stability under a lever change
is real evidence; 09_RAG's is not** (a flip there is neither confirmed right nor wrong, since the
underlying question was never resolved).

**06_tools (ground truth = `standard`): robust to C, fragile to D.**

| Lever change (explore=0.50 fixed) | `standard` R_w | margin vs `deep` |
|---|---|---|
| baseline (stdw=0.65) | 0.5813 | +0.0159 |
| stdw=0.75 | 0.5813 | +0.0142 |
| stdw=0.85 | 0.5813 | +0.0125 |
| stdw=0.95 | 0.5813 | +0.0108 |

Quality-weight alone never flips the winner even at its most aggressive tested value — `standard`'s
own R_w doesn't move at all (0.65→0.95 only reweights *within* an arm's own instances; 06_tools's
`standard`-arm sections apparently have no "standard"-tier-quality instances mixed in, only
`deep`'s does, so raising the weight only inflates `deep`'s R_w, narrowing but not closing the gap).

| Lever change (stdw=0.65 fixed) | `standard` R_w | `deep` R_w | margin | winner |
|---|---|---|---|---|
| baseline (explore=0.50) | 0.5813 | 0.5654 | +0.0159 | standard |
| explore=0.60 | 0.6129 | 0.6078 | +0.0051 | standard |
| explore=0.70 | 0.6445 | 0.6502 | +0.0057 | **deep** |
| explore=0.90 | 0.7076 | 0.7349 | +0.0274 | **deep** |

`explore_mult` alone flips the confirmed-correct answer as early as 0.70, and the margin *in favor
of the wrong answer* only grows from there (up to +0.0366 at the grid's most aggressive corner,
explore=0.90/stdw=0.95). **This directly reverses the enhancement-ceiling fix's own correction** —
raising `explore_mult` re-inflates `deep` past `standard` via the same mechanical pathway the ceiling
bug used to inflate it, just from a different angle (blanket multiplier vs. binary cap).

**09_RAG (unconfirmed near-tie): fragile to both, but uninterpretable.** Baseline already picks
`light` by a similarly razor-thin margin (+0.0051, consistent with §30's near-tie finding). It flips
to `deep` as early as stdw=0.85 alone, and unconditionally once explore≥0.60. Since the true answer
here was never established (2-2 replicate split), neither direction can be scored as an improvement
or a regression from this data alone.

**Why the tool's own "cross-article agreement" heuristic is actively misleading here:** the grid's
`[AGREE]` zone (explore≥0.60 with stdw=0.95, or explore≥0.70 unconditionally — 13 of 20 cells) is
exactly the region where 06_tools flips away from its *confirmed-correct* label. Agreement between
two articles is only meaningful evidence in the *absence* of independent ground truth on either one
— once one article has a confirmed-correct answer (06_tools does), that article's own label
stability is the binding constraint, and should be checked directly rather than via the
cross-article-agreement proxy. Recorded here as a lesson for future use of this tool.

**Mechanism (traced from the formula, not assumed):** `explore_mult` multiplies
`cp*(0.60*de+0.40*be)` per arm, and each arm's `de`/`be` come from a *different episode* (more
exploration rounds → structurally larger raw de/be before any capping fix is applied). `deep`'s
episode has the largest raw de/be in both articles simply because it did the most exploration —
so scaling `explore_mult` up amplifies whichever arm already leads on that axis, which is `deep` in
both cases tested. It doesn't reason about whether that arm's *credited* instances are genuinely
strong (that's what the count/quality-cap fix and candidate C already handle) — it's a blunt,
per-arm-blind multiplier that happens to structurally favor the highest-effort arm every time.

**Revised recommendation:** do **not** increase `explore_mult` above the current production value
(0.50) — the grid shows, with real confirmed-ground-truth data, that doing so systematically
overturns the fix this whole investigation was built to make. Quality-weight (candidate C) is safer
within the tested range (never flips 06_tools's confirmed answer) but still erodes its margin
monotonically (32% shrinkage by stdw=0.95), so treat it as a lever to move cautiously/incrementally
if at all, not as a free win. **Net conclusion: current production defaults (explore_mult=0.50,
standard-tier quality_weight=0.65) remain the best-supported choice** given the one confirmed
ground-truth data point available; nothing in this grid provides evidence to change them. This
should be revisited once more articles are re-graded and confirmed (not just re-graded — confirmed
via replicate majority, as 06_tools was), since n=1 confirmed article is a thin basis for a
permanent decision.

## 36. Circularity critique of §35, a real formula-consistency bug found while checking it, and a corrected (non-circular) test

**User's challenge (2026-07-16):** §35's "confirmed-correct" label for `06_tools__var_standard`
(`standard`, via §31's 3-1 replicate majority) was itself computed **under the baseline formula's
own parameters** (`explore_mult=0.50`). Using "does raising `explore_mult` disagree with that
label" as evidence *against* raising `explore_mult` assumes the very parameters in question are
already correct — textbook circular reasoning. Confirmed as valid: §35's recommendation to avoid
raising `explore_mult` was not properly justified as stated.

**A more fundamental, purely mechanical bug found while investigating this:**
`training/measure_replicate_noise.py` (the script that actually produced §30/§31's published
replicate margins) computed `de`/`be` via the raw binary `_get_score()`, **never routing through
`_get_enhancement()`/`enhancement_credit()`** — i.e. it silently used the OLD (pre-enhancement-fix)
formula for all 3 replicates, while the "original" row (read from the real, already-regenerated
`article_oracle.json`) reflected the NEW formula. The published "3-1 majority" was therefore
comparing 1 new-formula draw against 3 old-formula draws — apples to oranges, a real inconsistency
independent of and more basic than the circularity concern. **Fixed**: `_compute_replicate_sections()`
now mirrors `generate_episode_oracles.py::process_article_variant`'s `_enh_credit` closure exactly.
Re-ran both articles with the fix: **the qualitative conclusions held up** — `09_RAG` still lands a
genuine 2-2 tie (votes: standard, light, light — same split as before, margins compressed but same
pattern), `06_tools` still gives a clean 3-1 majority for `standard` — but the exact margin
magnitudes previously published were wrong and are now superseded.

**The properly non-circular test:** rather than comparing one draw's raw-argmax against a
formula-dependent label, added `sweep_reward_formula.py --majority-vote-sweep`: for each
`explore_mult` value, recompute **all 4 independent draws** (original + 3 replicates) under the
*same* candidate cfg, and take a majority vote — this uses replicated evidence as the ground truth
proxy, not a single formula's own label, so it doesn't beg the question.

**Result — genuinely revises the previous (circular) conclusion:**
- **`09_RAG__var_standard`**: `light` remains the plurality winner across the *entire* tested range
  (explore_mult 0.50→0.90) — `deep` never takes the majority. §35's claim that raising
  `explore_mult` "flips 09_RAG to deep" was an artifact of looking at only the single production
  draw plus its own secondary-signal tiebreak — not supported once all 4 draws are considered.
- **`06_tools__var_standard`**: the majority genuinely flips from `standard` (3-1) to `deep` (3-1)
  once `explore_mult` crosses **~0.65** — and critically, this is **3 of 4 independent draws
  agreeing**, not just the cherry-picked original. This is real, non-circular evidence that raising
  `explore_mult` reveals something the single-draw comparison couldn't — it directly **reverses**
  §35's recommendation to avoid raising `explore_mult`, at least for this specific article.

**Honest caveat:** this is still a small-sample replicate vote (4 draws) for 2 articles; genuinely
informative, but not a final word. The corrected, general lesson for future use of this tool:
comparing a swept lever against a *single formula-dependent label* is circular; comparing it against
an *independently-replicated majority vote*, recomputed consistently under the same candidate
parameters for every draw, is not.

## 37. Full corpus re-grade (all 40 articles) — a counter-intuitive result opposite the original hypothesis

**User re-graded all 40 production articles' `reasoning.json`** (train + test, temperature-0.7
original episodes) with the `[instances=N; quality=...]` tag — the expensive step (§27-28) is now
done at full scale, not just the n=2 pilot. This is the actual "production cutover" this
investigation was building toward.

**Sequence run:** backed up the pre-tag state (`bases_PRETAG_BACKUP_20260724`), regenerated
`section_oracle.json` for all 40 (`generate_episode_oracles.py`, TRAIN default + TEST explicit
list — both scripts default `--articles` to only the 8 TRAIN topics; the 16 TEST no-variant
articles must be passed explicitly or are silently skipped), then `compute_article_oracle.py
--force` for both groups. Built `training/diff_oracle_regen.py` (new, read-only) to diff
before/after `article_oracle.json` across the whole corpus — reports per-article flips split by
whether the *old* margin was thin (<0.06) or comfortable (≥0.06), plus the aggregate arm
distribution.

**Result — the OPPOSITE of the motivating hypothesis:**

```
42 article(s); 34 unchanged, 8 flipped
Arm distribution BEFORE: {skip: 12, light: 19, standard: 6, deep: 5}
Arm distribution AFTER:  {skip: 12, light: 22, standard: 6, deep: 2}
```

`light` **grew** (19→22, +3) and `deep` **shrank** (5→2, -3) — precisely reversed from §25's
original hypothesis that the enhancement-ceiling fix would demote `light`'s over-crediting and
promote `standard`/`deep`. 8 flips total: 6 thin-margin (expected/lower-risk), 2 comfortable-margin
(flagged for priority inspection): `13_agent_framework` (`deep`→`skip`, margin +0.076→-0.008) and
`Dark_Dimension` (`skip`→`light`, margin +0.131→+0.055).

This did not immediately invalidate the fix — it triggered a proper investigation (§38) rather than
either reverting or rationalizing, consistent with this investigation's practice throughout.

## 38. Root-cause diagnosis: the fix's *ordering* is validated by real data, but its *scale* was mis-calibrated

Built `training/audit_enhancement_tags.py` (new, read-only) to test the fix's core assumption
directly against the full, now-tagged corpus, rather than continuing to reason from the n=2 pilot.

**The core hypothesis (deep has more/stronger instances than light) is CONFIRMED, corpus-wide:**

| | mean instance count | mean `enhancement_credit()` |
|---|---|---|
| skip | 0.000 | 0.000 |
| light | 0.327 | 0.142 |
| standard | 0.408 | 0.175 |
| deep | 0.430 | **0.182** |

Monotonic, exactly as hypothesized — this is not a case of "the whole premise was wrong."

**The real mechanism for the counter-intuitive result:** across **every arm**, 90-97% of entries
have 0 or 1 qualifying instance (skip 100%/0%, light 75.8%/19.0%, standard 71.1%/20.8%, deep
70.0%/21.3% — the 1-instance *rate* is nearly identical across arms). Only 5-9% have 2+ instances,
where deep's real edge lives (deep 8.7% vs light 5.2%). The curve's deliberate design choice — a
single instance credited at 0.55 instead of the old implicit 1.0 (§27: "intended
light-overcrediting correction") — hits this dominant 0/1-instance case **roughly equally across
all arms**, not selectively on light. Since that case is ~90%+ of all entries, `enhancement_credit()`'s
overall scale shrank by a nearly uniform ~40% for every arm (light 0.242→0.142 [×0.588], standard
0.289→0.175 [×0.605], deep 0.300→0.182 [×0.606] — using the fraction-with-count≥1 as the
old-equivalent mean). The rare 2+-instance bonus that's supposed to differentiate `deep` doesn't
occur often enough to offset that uniform shrinkage — and since `deep`'s reward advantage must
overcome its own unchanged, bigger cost penalty (`-0.06×3` vs light's `-0.06×1`), shrinking the
explore term's absolute scale hurts `deep` disproportionately even though its *relative* ranking
within the curve is correct.

**Two real-data case studies (actual reasoning.json tags), pulled to understand the mechanism
concretely:**
- **`13_agent_framework`** (deep→skip): `deep` never exceeds 1 instance in *any single section* —
  its advantage is spread thin across ~7 sections, each worth only ≤0.55 credit. Meanwhile
  `standard` hits the **full cap** (3 instances → 1.00) in one heavily-weighted section (S3), and
  `light` hits 2 instances (→0.80) in another (S5). A single big win in one heavily-weighted section
  can outweigh many small scattered wins under target-words weighting.
- **`Dark_Dimension`** (skip→light): `light`, `standard`, and `deep` all hit **exactly 3 strong
  instances** in the article's one real content section (S3) — tied at the full 1.00 credit
  ceiling, identical to what old binary scoring would have given all three. `deep`'s only edges
  (S2-depth, S3-breadth) are single instances. This flip may not even be attributable to the
  enhancement fix specifically, since the shared tied section's credit is unchanged old-vs-new.

**Tested the natural compensating lever** — the scale factor implies `explore_mult ≈
0.50/0.60 ≈ 0.83` would restore the old overall scale. Result on the real 42-article corpus: only
5 flips, and it does **not** cleanly reverse the original 8 (e.g. `06_tools__var_demanding`'s
deep→standard flip isn't recovered at all; a different, unrelated set of articles flip instead).
**Conclusion: raising `explore_mult` is not a clean fix here** — it's a genuinely mixed, blunt
effect (confirmed via `sweep_reward_formula.py --corpus-sweep`), not a scale-restoring one.

## 39. Candidate E — simple (unweighted) mean of the explore term across sections

**User's proposal (2026-07-24):** apply simple averaging to the `explore` component of the
per-section reward specifically, while the rest (`gt_base + user_intent + cost`) stays
target-words-weighted — since an enhancement instance's value shouldn't scale with the word budget
of the section it happened to land in. Directly motivated by the `13_agent_framework` case study
above (deep's advantage diluted by being spread across many low-weight sections, while standard's
concentrated in one heavily-weighted section).

**Implemented as a real schema/code change (section_oracle.json v3→v4), tested before touching
production:**
- `generate_episode_oracles.py`: added `_section_reward_components(...) -> (rest, explore)`
  (returns the pieces separately; `rest+explore == _section_reward(...)` exactly). `_section_reward()`
  itself is unchanged — existing callers (`measure_replicate_noise.py`, the sweep tool's inline
  copy) are unaffected. `process_article_variant` now stores a new `"explore"` sub-dict per section
  alongside the existing `"rewards"` dict (version bumped to 4).
- `compute_article_oracle.py::_compute_r_w()`: when `"explore"` is present, computes
  `R_w[arm] = weighted_mean(rewards[arm]-explore[arm], weights=target_words) +
  simple_mean(explore[arm])` — falls back exactly to the old pure-weighted-mean when `"explore"` is
  absent (v2/v3 data), zero behavior change for anything not yet regenerated.
- Mirrored into `sweep_reward_formula.py` (`simple_avg_explore` cfg flag) for pre-production
  testing. **Found and fixed a real bug while testing**: the plain per-article table was calling
  `_recompute()` (hardcoded to the TRAIN-variant path), silently returning garbage for TEST
  articles like `13_agent_framework`/`Dark_Dimension` — fixed to use `_recompute_any()`.

**Per-article effect is genuinely mixed, not uniformly "helps deep":**
- `13_agent_framework`: `deep` recovers modestly (0.5880→0.5927 alone; →0.6648 combined with
  `explore_mult=0.83`) — matches the story (spread-thin sections benefit from removing the
  length-weighting).
- `Dark_Dimension`: `deep` actually **drops further** (0.6436→0.5917) — its edge is partly
  concentrated in the *same* big tied section as everyone else, so simple-averaging dilutes that
  shared section's outsized contribution for `deep` too, without enough compensation from its
  smaller edges elsewhere. **Candidate E is not a "pro-deep" lever — it's a "remove an arbitrary
  length bias" lever, and those aren't the same thing.**

**Shipped to production and diffed against the full corpus (backed up as `bases_V3_BACKUP_20260724_122559`):**

```
42 article(s); 41 unchanged, 1 flipped
Arm distribution BEFORE (v3):   {skip: 12, light: 22, standard: 6, deep: 2}
Arm distribution AFTER (v4+E):  {skip: 12, light: 22, standard: 7, deep: 1}
Flip: 06_tools__var_standard   deep -> standard   (old_margin=-0.0069, new_margin=+0.0299, thin)
```

**Verdict: E is a real, principled fix (removes a genuinely arbitrary bias) but its aggregate
effect is small** — only 1/42 flips, `light`'s share is completely unchanged (22→22), and `deep`
shrinks further, not less. **E does not address §38's scale-compression finding** — it changes how
per-section explore values aggregate across sections, not the per-instance credit values
themselves. Both backups (`bases_PRETAG_BACKUP_20260724` = pre-tag state, `bases_V3_BACKUP_20260724_122559`
= v3/tag-based-no-split state) are preserved for rollback. v4 (with E) is now live in production.

## 40. The curve-scale recalibration question, in detail

**What "the curve" is.** `enhancement_reward.py` maps a section's enhancement signal —
`(count, quality-tiers)` — into a single credit value in `[0,1]` via three pieces:
```
QUALITY_WEIGHT = {"strong": 1.00, "standard": 0.65}
INSTANCE_CAP = 3
CREDIT_AT_WEIGHTED_COUNT = {0: 0.00, 1: 0.55, 2: 0.80, 3: 1.00}
```
That credit value becomes `de`/`be` in `_section_reward`'s `explore` term:
`explore = cp * (0.60*de + 0.40*be) * 0.50` (`explore_mult = 0.50`).

**What "scale" means, precisely.** The **old** (pre-fix) scoring was a step function: any
qualifying instance → `1.00`; zero → `0.00`. The new curve's first rung — `1 instance → 0.55` — is
deliberately **half** of that old value (§27: "intended light-overcrediting correction"). §38
showed this "1-instance" case is not light-specific — it's the dominant case for *every* arm
(~19-21% for light/standard/deep alike, vs. only 5-9% for 2+ instances). Halving the credit for the
dominant non-zero case shrinks the **mean** credit for every arm by roughly the same proportion
(~×0.59-0.61), not selectively for light. The **ordering is preserved and validated on real data**
(deep > standard > light, confirmed in §38) — this isn't "the fix was wrong" — but the **absolute
gaps** between arms shrank in lockstep with the uniform downscaling, because the rare 2+-instance
bonus (5-9% of sections) that's supposed to differentiate `deep` can't fully offset a reduction
hitting ~90%+ of sections. That's "the scale problem": the curve's *shape* (relative crediting
across instance counts and quality tiers) is doing its job; its *overall magnitude* wasn't re-tuned
to account for how rare multi-instance sections actually turned out to be.

**Why this specifically hurts `deep`.** `deep` pays a cost penalty of `-0.06×3 = -0.18` per section
(3 exploration rounds) vs. `skip`'s `0` and `light`'s `-0.06`. It needs `explore` to earn that back.
Rough math on the *average* section: `explore ≈ cp×0.182×0.50 ≈ 0.091` (using deep's mean credit,
`cp≈1`) — about **half** of the `0.18` cost gap it needs to overcome. So on a typical section,
exploration credit alone doesn't come close to justifying `deep`'s cost; `deep` only wins overall
when `cc`/`fl`/`ga`/`ra` also favor it, or it hits one of the rarer multi-instance sections.
Consistent with the `13_agent_framework`/`Dark_Dimension` case studies in §38.

**Two genuinely different levers — not interchangeable:**
- **(A) Raise `explore_mult`** (currently 0.50, uniform external multiplier on the whole `explore`
  term): scales *everything* — every arm, every section with *any* nonzero explore signal — by the
  same factor. Doesn't touch the curve's internal shape. Already tested (§38): blunt, with side
  effects unrelated to the enhancement fix (e.g. flipping `skip→light`/`standard` in articles where
  the change isn't about deep's exploration credit at all, just an amplified tiny residual signal).
- **(B) Recalibrate the curve itself** (e.g. raise `CREDIT_AT_WEIGHTED_COUNT[1]` from 0.55 toward
  something higher, possibly reshaping the whole ladder): changes the *relative* value of hitting
  1 vs. 2 vs. 3 instances. More surgical — only affects sections with actual enhancement signal
  (never touches `skip`'s all-zero sections) — but risks re-introducing the "single instance
  over-credited" problem if pushed too far back toward 1.0, and risks flattening the multi-instance
  differentiation (the reason this investigation started) if the tier-1-to-tier-3 gap narrows too
  much.
- A **third, softer option**: raise `QUALITY_WEIGHT["standard"]` (candidate C, already tested —
  safe, modest effect) — raises the effective weighted count for a given real instance mix without
  touching the count→credit ladder directly.

**The core tension to be explicit about.** The `0.55` single-instance value was chosen in §27
*before* the real corpus-wide instance-count distribution was known (informed by one pilot
article's recount, not all 40). The question is not "should we undo the fix" (a single instance
genuinely shouldn't auto-max credit) — it's narrower: **was `0.55` specifically well-calibrated**,
now that ~90%+ of sections never get past 1 instance? A different single-instance value (e.g.
0.65-0.70) might better balance "don't over-credit a lone instance" against "don't crush the
average explore signal so hard that `deep`'s cost penalty becomes structurally almost unbeatable."

**A side note worth carrying forward:** `standard` and `deep` have nearly identical instance-count
profiles (20.8%/8.1% vs 21.3%/8.7%), so any curve recalibration would likely lift **both** roughly
together relative to `light`/`skip` — matching the original, broader hypothesis, not a
deep-specific fix.

This is ultimately a **normative calibration decision** informed by data, not fully determined by
it — like the original `explore_mult=0.50` choice. §41 designs and tests concrete candidate curves
against this same real, full corpus.

## 41. Candidate curves tested — F3 (gentle) is the only one that doesn't erode the confirmed ground truth

Added 4 candidates to `sweep_reward_formula.py` (kept `INSTANCE_CAP=3` and tier-3 anchored at
`1.00` throughout — no cap extension, avoiding the A/B dilution mechanism entirely):

| Candidate | `credit_curve` (tiers 0/1/2/3) | Other |
|---|---|---|
| F1 `tier1_070` | `{0:.00, 1:.70, 2:.85, 3:1.00}` | — |
| F2 `tier1_080` | `{0:.00, 1:.80, 2:.90, 3:1.00}` | — |
| F3 `tier1_065_gentle` | `{0:.00, 1:.65, 2:.83, 3:1.00}` | — |
| F1+C `tier1_070` + stdw=0.80 | `{0:.00, 1:.70, 2:.85, 3:1.00}` | `quality_weight["standard"]=0.80` |

**Applied the same non-circularity discipline as §36**, since `06_tools__var_standard`'s
`standard` answer is itself a *confirmed* label (§31's replicate majority) computed under the
*current* curve — testing "does candidate X disagree with that label" would be circular unless
checked against the actual replicate-majority vote, not the single baseline draw. Generalized
`majority_vote_sweep()` into `majority_vote_sweep_named()` to accept any cfg, not just
`explore_mult`.

**Result — a clear, non-circular signal: F1/F2 erode the confirmed majority; F3 does not.**

| Candidate | `06_tools` majority (orig+3 replicates) | `09_RAG` majority | Corpus-wide raw-argmax flips (of 42) |
|---|---|---|---|
| baseline | **standard 3-1** (clean) | light 3-1 (clean) | — |
| F1 `tier1_070` | **deep 2 - standard 2 (TIE)** | light 3-1 (unchanged) | 1 (`06_tools__var_standard` std→deep, thin) |
| F2 `tier1_080` | **deep 2 - standard 2 (TIE)** | light 3-1 (unchanged) | 2 (same flip **+** `11_multimodal__var_demanding` skip→standard, **COMFORTABLE margin**) |
| F3 `tier1_065_gentle` | **standard 3-1 (unchanged)** | light 3-1 (unchanged) | **0** |
| F1+C stdw=0.80 | **deep 2 - standard 2 (TIE)** | light 3-1 (unchanged) | 1 (same as F1 alone) |

Raising the single-instance credit to 0.70 or 0.80 measurably erodes `06_tools`'s confirmed 3-1
majority down to a 2-2 tie — **confirmed two independent ways** (the replicate-majority-vote check
AND the corpus-wide raw-argmax flip), not just a single-draw artifact. F2 additionally introduces a
new **comfortable-margin** flip elsewhere (`11_multimodal__var_demanding`), a higher-priority
warning sign per this investigation's own risk tiers. **F3 (0.65) is the only candidate that leaves
both the confirmed ground truth and the rest of the corpus completely untouched** (zero flips
corpus-wide) while still doing real, measurable work — per-article inspection shows `deep`'s
absolute R_w still rises under F3 in cases like `13_agent_framework` (0.5880→0.6070, ~+3.2%),
just not enough to flip any decision.

**Recommendation:** if pursuing curve-scale recalibration at all, **F3-style gentle values
(~0.60-0.65 for the single-instance tier) are the defensible choice** — they restore some of the
scale reduction §38 diagnosed without gambling the one piece of confirmed ground truth this
investigation has. Values at or above 0.70 should be treated as failing validation, the same way
candidates A/B failed in §34. As always: n=1 confirmed article + a corpus-wide *stability* check
(not a correctness check, since most of the 42 articles have no independent confirmation) is
informative but not final — worth revisiting once more articles get a genuinely confirmed
(replicate-majority) label.

---
---

# Part 6 — Pairwise LLM Comparison Grading (2026-07-24)

**Scope:** after five different section-level signal candidates (raw citations, marginal
citations, numeric claims, connector density, embedding-distance novelty) all failed to
meaningfully separate the standard↔deep boundary specifically (each ruled out at proper
statistical rigor, not just assumed), this Part documents the pivot to a categorically different
lever — **direct pairwise LLM comparison** of two arms' renderings of the same section, instead
of grading each arm in isolation against a fixed rubric. This targets judge-side/absolute-scale
imprecision specifically, rather than searching for yet another content-derived proxy signal.

## 42. Motivation: why pairwise, and why now

The tag-based `enhancement_credit()` pipeline (Parts 5, §25-41) grades depth/breadth enhancement
per arm, per section, **in isolation** — the judge sees one document and a rubric, never a
second document to compare against. This has an inherent resolution limit: distinguishing "this
section's exploration content is worth roughly 0.55" from "worth roughly 0.80" requires the judge
to hit an *absolute* scale consistently across thousands of independent single-document
judgments, with no anchor. A **relative** judgment — "is document B's exploration content more
extensive/valuable than document A's, for the same section?" — is a categorically easier
judgment for an LLM to make reliably, and directly targets the specific failure mode this
investigation kept re-encountering: the standard↔deep boundary, where absolute-scale judgments on
two content-rich, effort-differentiated documents are hardest to calibrate consistently.

This is explicitly **not** another search for a new content-derived proxy feature (the five that
failed in §*(pre-Part-6 investigation, not written up as its own numbered section but referenced
throughout this Part's design rationale)* were all attempts to find some *new measurable property
of the text* that correlates with true quality). Pairwise comparison instead changes *how the
existing judgment is elicited*, keeping the underlying question (does this arm have more
depth/breadth enhancement content?) the same.

## 43. Design: metric module, driver script, reconciliation

**New metric module** — `writing_workflow/src/brown/evals/metrics/pairwise_enhancement/`
(mirrors the `new_follows_gt/` sibling-module pattern): `PairwiseEnhancementJudgment` (Pydantic)
carries nested `depth`/`breadth` judgments, each with a 5-point `preference` scale
(`a_much_more`/`a_more`/`tie`/`b_more`/`b_much_more`) plus `a_instances`/`b_instances` (brief
phrases of distinct qualifying enhancement instances found in each document that the *other*
document lacks). Both dimensions graded in **one** structured-output call (keeps costs at
~1 call/section/pair, not 2). `grade_pairwise()` is a lightweight standalone async function
(deliberately **not** a full `BrownBaseMetric`/`ArticleScores` subclass — this is a
single-comparison-per-call design, architecturally different from the existing whole-article
multi-section metrics) reusing `get_model`/`structured_output_kwargs` exactly like
`FollowsGTMetric`.

**Driver** — `writing_workflow/rl_pairwise_grading_generator.py`: loads light/standard/deep
`article.md` per article (auto-detects TRAIN-variant vs TEST preset convention via `"__var_" in
name`, never relying on any file's own possibly-stale `TRAIN_ARTICLES`/`TEST_ARTICLES` lists),
splits into sections (by `## ` header, including the pre-first-header text as an "Introduction"
section, stopping before `## References`), does the 3-way round robin per section
(`light_vs_standard`, `light_vs_deep`, `standard_vs_deep`) with **randomized A/B position** (not
both orders, to keep cost proportional — position bias washes out in aggregate across many
sections/articles rather than being eliminated per-call). Writes raw judgments to
`rl_training_data/pairwise_pilot/<article>/pairwise_judgments.json`.

**Reconciliation** — `research_agent_local/training/pairwise_reward.py`: converts the 5-point
ordinal preference scale to a signed numeric delta (`PREFERENCE_TO_DELTA`, calibrated to
`enhancement_credit()`'s own ~0.20-0.25 tier spacing — an early miscalibration attempt using
larger magnitudes saturated the [0,1] scale on the very first non-tie judgment and was caught via
a synthetic unit test before any real grading ran). `light`'s credit is anchored at its existing
tag-based `enhancement_credit()` value; `standard`/`deep` are solved via a ridge-regularized
least-squares fit from the 3 pairwise deltas (always well-posed regardless of how many of the 3
pairs succeeded). Zero LLM calls — pure post-hoc numeric reconciliation, same spirit as
`sweep_reward_formula.py`.

**A real bug caught before trusting any output:** the first implementation of the delta-sign
conversion looked for `a_arm`/`b_arm` *inside* the depth/breadth sub-dict — but they live at the
judgment-entry level (one A/B assignment shared by both dimensions). Caught via a synthetic
unit test (`solve_section_credits` on hand-constructed judgments) before spending any real API
budget.

## 44. Pilot result (6 articles, 137 calls): a real but weak relationship, with a genuine directional pattern

Piloted on 6 diverse articles chosen via `audit_oracle_margins.py`'s real margin data:
`09_RAG__var_standard` (unresolved near-tie), `06_tools__var_standard` (confirmed-correct via
§31's replicate majority), `13_agent_framework` and `Dark_Dimension` (TEST, thin margins), `HNSW`
(TEST, comfortable margin — sanity check), `08_react_practice__var_demanding` (TRAIN, comfortable
margin, topic diversity). 137/138 calls succeeded (1 section both-arms-empty, correctly skipped),
0 errors.

**Headline result across all 92 (section, dimension) observations:** Pearson
`r=+0.223` between tag-based and pairwise-reconciled standard-vs-deep margins — a real but weak
relationship. Stratified: 25 trivial (both methods say ~no signal), 40 weak/ambiguous, 17
strong-agree (both confident, same direction), **10 strong-disagree** (both confident, opposite
direction) — raw argmax agreement on non-trivial cases only 57% (38/67), barely above chance.

**A suggestive (not yet significant, n=10, binomial p≈0.34) directional pattern:** of the 10
disagreements, 7 have tag-based grading favoring `deep` while pairwise favors `standard` — direction
consistent with tag-based grading over-crediting `deep` from raw content volume, while direct
comparison better detects when `standard`'s specific draw had comparably distinct content.

**An important caveat surfaced immediately:** pairwise grading has its *own* internal
inconsistency, not a clean fix. `13_agent_framework`'s "Framework Deep Dive: LangGraph" section
showed a non-transitive triangle: the direct `light_vs_deep` call judged `light > deep`, but
`light_vs_standard` and `standard_vs_deep` were both judged ties — the judge disagreeing with
itself across the 3 pairwise calls for one section. Pairwise comparison is a different lens on
judge noise, not an elimination of it.

**A positive counter-example, for balance:** "A Theory for Choosing: Decision Axes"
(`13_agent_framework`) — both methods agree `standard >> deep`, and pairwise identified a concrete
mechanism (`standard` has 4 distinct cited instances vs. `deep`'s 1 in this specific section, a
genuine content-quality finding, not an artifact).

## 45. Repeat-draws noise-floor check (60 calls): the disagreement is real, not single-draw noise

Two competing explanations for §44's 10 disagreements: (1) real, repeatable judge disagreement
with tag-based grading, or (2) each disagreement is itself just one noisy draw that would flip on
a second look. Re-ran the exact same 10 disagreement cases + 5 agreement controls, same `doc_a`/
`doc_b`/section, **same A/B slot** (not re-randomized — isolates judge-call noise from
position-bias noise), 4 additional draws each (5 total per target).

**Result: 9 of 10 disagreements persisted after denoising** (only 1/10 resolved, and only to a
near-zero "weak" tie, not to actual agreement). **Within-case consistency** (fraction of the 5
draws agreeing with the majority direction) averaged 80% for disagreement cases and ~84% for
agreement controls — pairwise grading is reasonably repeatable *in general*, it just consistently
gives a different verdict than tag-based grading on these particular sections. Direction among
the 9 persisting disagreements: 7 "tag=deep/pairwise=standard" vs. 2 reverse — the same ratio as
§44, now backed by 4-5 consistent draws per case instead of one noisy call. 2/5 agreement controls
regressed to "weak" (shrunk toward zero, did not reverse sign) — expected regression-to-mean for
borderline cases under averaging, not a red flag.

## 46. Scaled standard-vs-deep check (243 calls): independent replication crosses statistical significance

A lean, dedicated driver (`writing_workflow/rl_pairwise_stddeep_scale.py`) graded **only**
`standard_vs_deep` (skipping `light` entirely) with **N=3 draws per section from the start**
(majority-vote-by-design, not a repeat pass) across **12 new, disjoint articles** covering every
remaining TRAIN base topic (`02_workflows_vs_agents`, `03_context_engineering`,
`05_workflow_patterns`, `10_memory_knowledge_access`, `11_multimodal`, all `__var_standard`) plus
7 diverse TEST articles (`04_structured_outputs`, `07_reasoning_planning`, `29_evaluation_metrics`,
`Earth_Oceans_Origin`, `Understanding_Reasoning_LLMs`, `Distinct_AI_Models`,
`Insects_Consciousness`). 81 sections × 3 draws = 243 calls, 0 errors.

**Result: N=162 observations, Pearson `r=+0.375`** — meaningfully *stronger* than the original
single-draw pilot's r=0.223, consistent with majority-voting reducing pairwise's own noise.
Breakdown: 28 trivial, 84 weak, 41 strong-agree, **9 strong-disagree**. Direction split among the
9: **7 "tag=deep/pairwise=standard" vs. 2 reverse — the identical 7:2 ratio found independently in
§45**, from a completely disjoint set of 12 articles. Concrete pattern: most of the 7 cases have
`tag_margin` near the curve's maximum magnitude (-0.55 — tag gave `deep` full credit, `standard`
zero), while pairwise's own margin is far more modest (+0.067 to +0.367) — tag-based grading
saturates at its ceiling disproportionately in the "deep wins" direction.

**Combined significance test (legitimate pooling — the two 9-disagreement sets are from entirely
disjoint articles, no double-counting):** 18 total disagreement sections across 16 distinct
topics, 14 in the "tag=deep/pairwise=standard" direction vs. 4 reversed. Binomial two-tailed
`p=0.031` (n=18, k=14) — **crosses the conventional significance threshold**, where either sample
alone (p≈0.18 each) did not. This is the single strongest, most rigorously validated empirical
result in this whole pairwise-grading investigation: **tag-based/binary-capped grading
systematically over-credits `deep` relative to `standard` on a meaningful, statistically
significant subset of sections.**

## 47. Correction designed (G0/G1): mechanism confirmed with real data, but a real spillover complication

**Mechanism, verified with real tag data (not inferred):** pulled the raw `[instances=N;
quality=...]` tags behind the 7 clearest "-0.55" disagreement cases. 5 of them are exactly:
`standard`=0 instances (credit 0.00), `deep`=1 strong instance (credit 0.55) — the disagreement
concentrates precisely at `enhancement_reward.py`'s `CREDIT_AT_WEIGHTED_COUNT` **tier-1 step**
(the 0→1 instance transition, a +0.55 jump). The interpolation formula was verified to exactly
reproduce 2 non-integer disagreement cases too (`Earth_Oceans_Origin` -0.147,
`Understanding_Reasoning_LLMs` -0.25) via manual calculation before trusting the mechanism.

**Calibration:** majority-voted pairwise margin on these same 5 sections averaged **+0.207**
(range +0.067 to +0.367) vs. the curve's assumed +0.55 — tier-1 is empirically ~2.5x too steep.
Added two candidates to `sweep_reward_formula.py`: `G0_tier1_035` (conservative,
`{0:.00,1:.35,2:.80,3:1.00}`) and `G1_tier1_020` (aggressive, directly calibrated,
`{0:.00,1:.20,2:.80,3:1.00}`) — both leave tier-2/tier-3 unchanged (weaker evidence there).

**Non-circular replicate-majority-vote result (the strongest available ground truth):**
`06_tools__var_standard` (confirmed-correct label `standard`, baseline 3-1 majority) → **G0 gives
standard=4/4 unanimous** (real, positive evidence — the correction makes the confirmed-correct
answer *more* decisive). G1 gives 3-1, same as baseline (neutral).

**Corpus-wide sweep (42 articles):** G0 causes 5/42 flips, G1 causes 8/42 — but most are **not**
what the correction set out to fix. `enhancement_credit()`'s tier-1 value is shared by all 4 arms,
not just standard/deep — lowering it also reduces `light`'s credit whenever `light` itself has
~1 instance (common, per §38's audit: ~19-21% of article-arm pairs). Most flips are
`light→skip`/`standard→light` — spillover onto boundaries the pairwise investigation, at this
point, had never tested (it deliberately compared only `standard_vs_deep`).

## 48. Light-boundary investigation: does not replicate directionally

**Free first look (zero new API calls):** the original 6-article pilot (§44) already graded
`light_vs_standard`/`light_vs_deep` — data sitting unused for a "light" bias check. Analysis
(`analyze_light_boundary.py`, generalizes the tag-vs-pairwise comparator to any arm pair):
`light_vs_standard` N=92, r=+0.329, 4 disagreements (3:1 skew, "tag=light/pairwise=standard" —
2 of the 4 show the identical -0.550 tier-1 signature, just mirrored). `light_vs_deep` N=92,
r=+0.313, 7 disagreements, 4:3 split — no clear direction, consistent with noise.

**Phase 1 — repeat-draws (32 calls) on the 4 disagreements + 4 agreement controls, same 6
articles:** all 4 disagreements persisted after denoising (0/4 flipped — even more decisive than
standard-vs-deep's 9/10), all 4 controls held (0/4 weakened). Direction: 3 of 4 match the
original "tag=light/pairwise=standard" pattern. Confirms these 4 disagreements are real,
repeatable — not noise.

**Phase 2 — scaled, independent (129 calls, 6 new disjoint articles):** N=86 observations,
r=+0.337 (healthy). 9 disagreements, but **6 show "tag=standard/pairwise=light" — the opposite
majority direction from Phase 1.**

**Pooled significance test (Phase 1's 4 + Phase 2's 9 = 13 disagreements, disjoint articles,
legitimate to pool):** direction split 6:7 — essentially a coin flip. Binomial two-tailed
`p=1.00` — **zero evidence of a systematic directional bias** when properly combined across
independent samples.

**Verdict:** unlike standard-vs-deep (same direction across 2 independent samples, p=0.031),
light-vs-standard's apparent bias **did not survive independent replication at scale** — the
third time in this whole investigation a promising small-sample signal failed to hold up (after
marginal-citations and embedding-novelty), an established, expected risk pattern here, not a
surprise. Individual sections do show real, repeatable disagreements (Phase 1 confirmed that) —
they just aren't systematically biased in one direction. This meaningfully **de-risks** (does not
fully validate) the §47 spillover concern: since light-vs-standard shows no confirmed bias either
way, there is no known "correct direction" for light's calibration that G0/G1 could be violating —
the corpus-wide light-related flips are best characterized as an unbiased perturbation, not a
confirmed error.

## 49. F3 vs. G0 tension reconciled: F3 retracted, G0 preferred

§41's `F3_tier1_065_gentle` **raises** tier-1 (0.55→0.65); §47's `G0_tier1_035` **lowers** it
(0.55→0.35) — the same parameter, opposite directions, motivated by genuinely different concerns.

**F3's actual motivation (re-read from §40, not assumed):** a cost-balance concern — `deep` pays
`-0.18` cost (3 rounds) but §38 found average explore credit only earns back ~0.091 (half the
gap), so `deep` "structurally can barely win." F1(0.70)/F2(0.80) were tested and **broke**
`06_tools`'s confirmed 3-1 majority (eroded to a 2-2 tie). F3(0.65) was the highest value that
didn't visibly break anything — never independently validated as *correct*, only as
*not-yet-broken*. §40 itself notes `standard`/`deep` have nearly identical instance-count
profiles — raising tier-1 was always meant to lift both together against `light`/`skip`, not to
specifically favor `deep` over `standard`.

**Direct re-test (today's baseline, same non-circular replicate-majority-vote):**

| | 06_tools draws (margins) |
|---|---|
| baseline | standard(+.007) deep(+.001) standard(+.021) standard(+.008) |
| **F3** | standard(+.002) **deep(+.003)** standard(+.024) standard(+.011) |
| **G0** | **standard(+.023) standard(+.005)** standard(+.021) standard(+.003) |

F3 shrinks standard's winning margins and grows the one deep-winning draw — nudging the same
direction F1/F2 pushed too far, just short of the threshold. G0 does the opposite: it makes the
confirmed-correct answer *more* decisive (unanimous 4/4).

**But F3's underlying concern is real, and G0 makes it worse.** `13_agent_framework` (F3's own
worked example):

| | skip | light | standard | deep |
|---|---|---|---|---|
| baseline | .6446 | .6522 | .5891 | .5880 |
| F3 | .6446 | .6621 | .5988 | **.6070** (+.019) |
| G0 | .6446 | .6332 | .5709 | **.5500** (−.038) |

F3 genuinely helps `deep`'s absolute cost-vs-credit balance; G0 genuinely worsens it — two
different, non-substitutable objectives fighting over one shared parameter.

**Reconciliation and recommendation: retract F3, prefer G0.**
1. G0 is backed by direct, `p=0.031`, twice-independently-replicated pairwise-comparison
   evidence about tier-1's true calibration — the single strongest empirical signal in this
   whole pairwise investigation. F3 was validated only by a coarser test (corpus-flip-count + one
   replicate label) that happened not to detect a problem at 0.65, while quantitatively sitting on
   the same failure axis F1/F2 broke harder on.
2. F3's premise is itself now questionable: if `standard`'s pairwise-validated content quality is
   frequently comparable to `deep`'s (exactly what the tier-1 finding shows), `deep` genuinely,
   *correctly* should not always win — "fixing" this via tier-1 inflation would be curve-fitting
   toward a desired outcome (deep wins more often), not correcting a real measurement bug.
3. The cost-vs-credit imbalance is real but **tier-1 is the wrong lever for it** — every arm
   shares that curve. If pursued, the honest place to look is whether `deep`'s cost coefficient
   itself is well-calibrated, as a separate, explicitly-scoped question — not yet designed or
   tested.

**Status:** recommend `G0_tier1_035` as the corrected `credit_curve` candidate;
`F3_tier1_065_gentle`'s recommendation is **withdrawn** in light of this newer, more direct
evidence. Neither has been shipped — both remain `sweep_reward_formula.py` VARIANTS entries only,
pending an explicit decision to regenerate `section_oracle.json`/`article_oracle.json`.

## 50. Recommendations and next steps

1. **Ship `G0_tier1_035`** (or hold, per the user's risk tolerance) — it is the best-supported
   correction available: statistically significant, twice-replicated pairwise evidence on its
   core motivation, a genuine improvement (not just neutrality) on the one confirmed
   ground-truth article, and the light-boundary spillover concern is now substantially de-risked.
   A full `section_oracle.json`/`article_oracle.json` regen + corpus-wide diff (mirroring §37-39's
   process) would be the concrete next action if proceeding. **DONE — see §51.**
2. **Treat the cost-vs-credit imbalance (F3's original motivation) as a separate, still-open
   question** — if it's worth pursuing, investigate `deep`'s cost coefficient specifically
   (currently `-0.06`/round, `-0.18` total for 3 rounds) rather than the shared enhancement curve.
   Not yet designed.
3. **The pairwise-grading infrastructure built this Part is fully reusable** for any future
   arm-pair or dimension question at near-zero marginal engineering cost (`select_repeat_targets.py`/
   `select_light_repeat_targets.py`, the repeat-check driver's generic `--targets`/`--output-name`
   design, `rl_pairwise_stddeep_scale.py`/`rl_pairwise_lightstd_scale.py`'s parametrized pattern) —
   worth reusing directly rather than rebuilding if a similar question arises later (e.g. does the
   `INSTANCE_CAP=3` question from §30-31 warrant its own pairwise validation).
4. **Do not extend pairwise validation to `light_vs_deep`** without new motivation — both looks at
   it (§44, §48) showed no systematic bias, consistent with noise; further spend there has low
   expected value based on current evidence.
5. **General methodological note for future work on this project:** three separate small-sample
   signals have now failed to replicate at scale in this investigation (marginal-citations,
   embedding-novelty, light-vs-standard bias) against one that did replicate cleanly
   (standard-vs-deep bias, p=0.031 across two disjoint 12+6-article samples). The discriminating
   factor each time was **actually running the independent, disjoint-sample replication** before
   trusting a promising first look — continue treating that as mandatory, not optional, before any
   further reward-formula changes ship to production.

## 51. G0 shipped to production (2026-07-25)

**Backup taken first** (established practice): `rl_training_data/bases_PRE_G0_BACKUP_20260725/`
— full copy of all 42 article dirs, verified 42/42 `article_oracle.json` present before proceeding
(`bases/` is gitignored, so this manual backup is the only rollback path — do not delete it).

**Change made:** `enhancement_reward.py`'s `CREDIT_AT_WEIGHTED_COUNT[1]` changed from `0.55` to
`0.35` (production code, not just the sweep-tool `VARIANTS` entry). Docstrings updated to match
the new worked examples (1 strong instance → 0.35, 1 standard → ~0.23, 2 standard → ~0.49, 3
standard → ~0.78; tier-2/tier-3 unchanged at 0.80/1.00). Verified via direct function calls
before regenerating anything — `enhancement_credit([]) = 0.0`, `(["standard"]) = 0.2275`,
`(["strong"]) = 0.35`, `(["strong","strong"]) = 0.8`, `(["standard"]*3) = 0.7775`,
`(["strong"]*3) = 1.0` — all matching hand-computed expected values exactly.

**Regenerated for real** (writes, not dry-run): `section_oracle.json` for all 42 (`generate_episode_oracles.py`
default = 24 TRAIN + `--articles` for the 16 TEST + 2 mixeddepth pilots — 24 OK/0 failed, then
18 OK/0 failed), then `article_oracle.json` for the same 42 (`compute_article_oracle.py --force`,
same split — 24 written + 18 written).

**Diff result (`diff_oracle_regen.py --before bases_PRE_G0_BACKUP_20260725`): 37 unchanged, 5
flipped, ALL thin-margin (<0.06), ZERO comfortable-margin flips** — better than the sweep-tool's
pre-registered prediction (§47), which had flagged `09_RAG__var_demanding` as a comfortable-margin
flip. Root-caused the discrepancy directly: `09_RAG__var_demanding` is a **manual-override**
article (forced to `deep` regardless of R_w — verified its raw R_w actually favors `skip` at
0.517, but the override forces `deep` anyway) and `13_agent_framework` is a **policy-forbidden**
article (forced to `skip` regardless of R_w) — both confirmed completely untouched by G0 in the
real pipeline. The sweep tool's simplified `_recompute_any()` doesn't fully replicate these
hard-constraint rules, so its flip predictions for override/forbidden articles were unreliable;
this is a useful caveat for any future use of that tool on articles in the excluded/override set.

**The 5 real flips (all thin-margin, all `light`-originating):**

| Article | Old → new arm | Old margin → new margin |
|---|---|---|
| `09_RAG__var_standard` | light → skip | +0.0379 → +0.0119 |
| `Distinct_AI_Models` | light → deep | +0.0300 → +0.0150 |
| `Distinct_AI_Models__mixeddepth` | light → standard | +0.0212 → -0.0115 |
| `Gravity_Entropy` | light → skip | +0.0198 → +0.0243 |
| `Insects_Consciousness__mixeddepth` | light → deep | +0.0522 → +0.1500 |

**Corpus arm distribution:** `{skip:12, light:22, standard:7, deep:1}` →
`{skip:14, light:17, standard:8, deep:3}`. `06_tools__var_standard` (the one article with
confirmed replicate-majority ground truth) stays `standard` and becomes *more* decisive
(margin +0.0370) — consistent with the unanimous 4/4 replicate-vote result that validated G0
before shipping.

**G0 is now live in production as of 2026-07-25.** Rollback path if ever needed: restore
`rl_training_data/bases/<article>/{section_oracle.json,article_oracle.json}` from
`bases_PRE_G0_BACKUP_20260725/` for the 5 affected articles (or all 42, to be safe), and/or
revert `enhancement_reward.py`'s `CREDIT_AT_WEIGHTED_COUNT[1]` to `0.55` and re-run the same
regen commands.

**Not yet done:** an actual downstream retrain+eval to confirm this label correction translates
into better real RL/eval performance (per §50 item 5's own caution against assuming a
better-calibrated label automatically yields a better-trained policy) — this is a natural
candidate for a future session, not undertaken here. **Next immediate step (per the user's
explicit direction): investigate `deep`'s cost coefficient as a separate question from the
enhancement curve** — see Part 7 below.

---

# Part 7 — Reward-signal diagnostics: which metrics actually differentiate the arms? (2026-07-28)

## 52. Motivation: the cost-coefficient arc dead-ends, and a structural question surfaces

### 52.1 How we got here

Part 7's originally-planned scope (the cost-coefficient investigation) was carried out and is
summarised here only insofar as it motivates this section. The short version:

- `analyze_cost_imbalance.py` found `cost` explained **~93%** of `deep`'s average reward shortfall
  vs. the winning arm, while the *content* terms (`gt_base` + `explore`) mildly **favoured** deep.
  I.e. deep was losing on the cost penalty, not on content quality.
- `analyze_empirical_cost.py` measured each arm's **real** exploration effort (actual query +
  scrape counts from each arm's own `.research/full_queries.md` / `url_phases.json`, n=42) and
  found the assumed ordinal units `{0,1,2,3}` overcharged deep: real effort ratios are
  `{skip:0, light:1.00, standard:1.88, deep:2.31}`. Shipped as **H0**.
- Even after H0, cost still explained ~85% of the gap, so `cost_coef` magnitude itself was staged
  down: `-0.06 → -0.045 → -0.03` (2026-07-25) `→ -0.02` (2026-07-26), each step validated by
  full-corpus regen + replicate-majority-vote on the two confirmed-ground-truth articles.

**This overcorrected.** Runs 17/18/19 (all trained on `cost_coef = -0.02`) swept
`--inv-freq-temp` across `1.0 / 0.75 / 0.5` and produced a *monotonically worsening* TEST result
in every metric, with `deep` over-predicted in 9, 10, and 11 of 16 TEST articles respectively:

| run | inv-freq-temp | cost_coef | TEST exact | TEST miss | TEST MAE | regret_mean | hi-conf misses | deep predicted |
|---|---|---|---|---|---|---|---|---|
| run15 | 0.5 | **-0.03** | 33% | 27% (4) | **0.933** | 0.0165 | **1** | 6/16 |
| run17 | 1.0 | -0.02 | 40% | 33% (5) | 1.000 | 0.0128 | 4 | 9/16 |
| run18 | 0.75 | -0.02 | 27% | 33% (5) | 1.133 | 0.0289 | 4 | 10/16 |
| run19 | 0.5 | -0.02 | 13% | 40% (6) | 1.333 | 0.0486 | 4 | 11/16 |

*(all TEST figures exclude `policy=forbidden` articles, whose labels are set by a deterministic
guard the RL-only harness deliberately doesn't apply)*

Since `run19` used the script's own default `inv-freq-temp = 0.5` — i.e. **zero** deep-scarcity
escalation — and still over-predicted deep the most, `inv-freq-temp` is exonerated as the cause;
`cost_coef = -0.02` is implicated.

### 52.2 The second, more serious symptom: the training signal itself got weaker

Replicating `train_grpo.py`'s own `sigma_floor` / advantage-normalisation logic over all 171 TRAIN
sections, comparing the `cost_coef = -0.06` snapshot (`bases_PRE_COSTCOEF_SHIP_20260725`) against
current production (`-0.02`):

| | `cost_coef = -0.06` | `cost_coef = -0.02` |
|---|---|---|
| Dropped as flat (`max-min < sigma_floor=0.04`) | 2 (1.2%) | 0 (0%) |
| **Hit `sigma_floor` (`raw_std < 0.04`)** | **9 (5.3%)** | **44 (25.7%)** |
| Mean margin (top1 − top2) | 0.098 | 0.082 |
| **Median margin (top1 − top2)** | **0.060** | **0.038** |

The 25.7% figure matches the `sigma_floor_fraction: 0.2573` logged identically in runs 17/18/19,
confirming the mechanism rather than a coincidental correlation. **Reducing `cost_coef` nearly
quintupled the share of sections whose reward spread is below the noise floor**, and pushed the
*median* top-1-vs-top-2 margin (0.038) *below* `sigma_floor` itself. That explains the otherwise
puzzling training profile — `mean_expected_reward` looks near-optimal while `strict_top1_accuracy`
stalls near 50%: when arms are nearly tied, capturing most of the available reward is easy, but
identifying *which* arm is best is close to a coin flip.

### 52.3 The structural question this raises

`cost` was doing a large share of the work of *separating the arms at all*. Shrinking it exposed
how little of the remaining formula actually varies with the arm choice. That motivates a
redesign hypothesis (user's, 2026-07-28):

> Keep only genuinely **differentiating** metrics in the additive reward; demote the
> non-differentiating ones to **satisficing safety gates** outside the reward.

§53 tests that hypothesis against the corpus.

## 53. Metric-differentiation analysis across all 40 articles

### 53.1 Tool and method

New read-only diagnostic: **`research_agent_local/training/analyze_metric_differentiation.py`**.
Zero LLM calls, zero writes.

- **Scope:** all 40 production articles (24 TRAIN variants + 16 TEST no-variant) × 4 arms.
  282 (article, section) rows — 171 TRAIN, 111 TEST.
- **Section list** is read from each article's already-reconciled `section_oracle.json`, so the
  section set is identical to the one the real oracle used (no re-derivation from digests).
- **Score extraction reuses production code** — `geo._parse_sections_ordered`,
  `geo._get_score`, `geo._get_enhancement`, `enhancement_reward.enhancement_credit` — so every
  number is exactly what `_section_reward()` would have seen. `de`/`be` are reported as
  **post-`enhancement_credit()` values** (the saturating count×quality curve), not raw binaries.
- **One deliberate deviation:** `geo._load_episode()` filters to `_REWARD_DIMS`, which silently
  excludes `ground_truth_structure` and `user_intent_golden_source_priority`. The tool uses its
  own unfiltered loader so those two can be measured too. *(A first version of this analysis
  inherited the filter and reported `st` and `gsp` as identically 0.000 across the whole corpus —
  a tooling artifact, not a finding. Corrected before the numbers below were produced.)*

### 53.2 Index definitions

All indices are computed per metric. Let $v_{s,a}$ be the metric's value in section $s$ under
arm $a \in \{\text{skip}, \text{light}, \text{standard}, \text{deep}\}$, over $N$ sections.

| index | definition | reads as |
|---|---|---|
| **`w`** | the metric's *effective additive weight* in the current reward formula | how much the formula currently listens to it |
| **`mean`** | $\frac{1}{4N}\sum_{s,a} v_{s,a}$ | overall level (near 1.0 ⇒ the grader almost always passes it) |
| **arm means** | $\bar v_a = \frac{1}{N}\sum_s v_{s,a}$, reported per arm | does the metric *systematically* move with exploration depth? |
| **`armSprd`** | $\max_a \bar v_a - \min_a \bar v_a$ | **systematic signal.** How much the metric separates arms *on average*, after per-section noise cancels out |
| **`%const`** | share of sections with $\max_a v_{s,a} - \min_a v_{s,a} = 0$ | share of sections where the metric contributes **exactly zero** to distinguishing arms |
| **`meanRng`** | $\frac{1}{N}\sum_s (\max_a v_{s,a} - \min_a v_{s,a})$ | **total variation** across arms, signal *and* noise together |
| **`monoUp`** | of the sections that vary, share with $v_{skip} \le v_{light} \le v_{std} \le v_{deep}$ | does it behave like a monotone "more exploration ⇒ more of this"? (25% ≈ chance) |
| **`SNR`** | `armSprd / meanRng` | **the key ratio.** What fraction of a metric's variation actually tracks the arm choice, rather than being section-level noise |
| **`w*Rng`** | `w × meanRng` | total variation the metric *injects into the reward* (its noise footprint) |
| **`w*Sprd`** | `w × armSprd` | systematic arm-separating signal the metric *contributes to the reward* |

The critical distinction is **`armSprd` vs `meanRng`**. A metric can swing wildly section-to-section
(large `meanRng`) while its four arm means stay identical (tiny `armSprd`). Such a metric injects
variance into the reward without helping decide *which arm is better* — it is, in the arm dimension,
pure noise. `SNR` makes this explicit.

**Caveat on `SNR`:** it is only interpretable when `meanRng` is non-trivial. For near-constant
metrics (`cp`, `ra`, `gsp`, where both numerator and denominator are ~0.02 or less) the ratio is
numerically unstable and should be ignored — `%const` and `mean` are the meaningful indices there.

### 53.3 Results — full corpus (n = 282 sections)

| metric | w | mean | skip | light | std | deep | armSprd | %const | meanRng | monoUp | SNR | w\*Rng | w\*Sprd |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **de** | 0.30 | 0.122 | 0.000 | 0.139 | 0.155 | **0.195** | **0.1955** | 41.8% | 0.2754 | 50.6% | **0.71** | 0.0826 | **0.0586** |
| **be** | 0.20 | 0.051 | 0.000 | 0.068 | **0.075** | 0.060 | 0.0753 | 59.6% | 0.1415 | 29.8% | **0.53** | 0.0283 | 0.0151 |
| fl | 0.20 | 0.702 | 0.652 | 0.716 | 0.720 | 0.720 | 0.0674 | 67.7% | 0.3227 | 40.7% | 0.21 | 0.0645 | 0.0135 |
| cc | 0.20 | 0.889 | **0.901** | 0.894 | 0.883 | **0.879** | 0.0213 | 85.5% | 0.1454 | 22.0% | 0.15 | 0.0291 | 0.0043 |
| **ga** | 0.15 | 0.698 | 0.702 | 0.702 | 0.688 | 0.699 | **0.0142** | 51.1% | **0.4894** | 23.9% | **0.03** | **0.0734** | 0.0021 |
| ra | 0.15 | 0.986 | 0.986 | 0.993 | 0.979 | 0.986 | 0.0142 | **96.8%** | 0.0319 | 11.1% | — | 0.0048 | 0.0021 |
| cp | (gate) | 0.996 | 0.996 | 0.996 | 0.993 | 0.996 | 0.0035 | **99.6%** | 0.0035 | 0.0% | — | 0.0000 | 0.0000 |
| gsp | 0.00 | 0.988 | 0.982 | 0.989 | 0.989 | 0.989 | 0.0071 | **97.9%** | 0.0213 | 33.3% | — | 0.0000 | 0.0000 |
| st | 0.00 | 0.405 | 0.394 | 0.394 | 0.436 | 0.397 | 0.0426 | 58.5% | 0.4149 | 26.5% | 0.10 | 0.0000 | 0.0000 |

`cp` is shown with `w = (gate)` because it enters multiplicatively (`explore = cp * (...)`), not
additively; `de`/`be`'s effective weights (0.30 / 0.20) already fold in `cp ≈ 1`.

### 53.4 Results — split by TRAIN / TEST

TRAIN (n = 171):

| metric | mean | skip | light | std | deep | armSprd | %const | meanRng | monoUp |
|---|---|---|---|---|---|---|---|---|---|
| de | 0.121 | 0.000 | 0.149 | 0.141 | 0.194 | 0.1943 | 43.9% | 0.2807 | 46.9% |
| be | 0.054 | 0.000 | 0.072 | 0.081 | 0.064 | 0.0812 | 57.3% | 0.1463 | 30.1% |
| fl | 0.605 | 0.538 | 0.614 | 0.626 | 0.643 | 0.1053 | 56.7% | 0.4327 | 43.2% |
| cc | 0.883 | 0.906 | 0.906 | 0.865 | 0.854 | 0.0526 | 80.7% | 0.1930 | 15.2% |
| ga | 0.740 | 0.737 | 0.749 | 0.749 | 0.725 | 0.0234 | 53.8% | 0.4620 | 22.8% |
| ra | 0.990 | 0.994 | 0.994 | 0.982 | 0.988 | 0.0117 | 95.9% | 0.0409 | 14.3% |
| cp | 0.999 | 1.000 | 1.000 | 0.994 | 1.000 | 0.0058 | 99.4% | 0.0058 | 0.0% |
| gsp | 0.990 | 0.982 | 0.994 | 0.994 | 0.988 | 0.0117 | 97.7% | 0.0234 | 25.0% |
| st | 0.399 | 0.427 | 0.398 | 0.392 | 0.380 | 0.0468 | 56.7% | 0.4327 | 18.9% |

TEST (n = 111):

| metric | mean | skip | light | std | deep | armSprd | %const | meanRng | monoUp |
|---|---|---|---|---|---|---|---|---|---|
| de | 0.124 | 0.000 | 0.123 | 0.176 | 0.197 | 0.1974 | 38.7% | 0.2672 | 55.9% |
| be | 0.045 | 0.000 | 0.062 | 0.066 | 0.054 | 0.0662 | 63.1% | 0.1342 | 29.3% |
| fl | 0.851 | 0.829 | 0.874 | 0.865 | 0.838 | 0.0450 | 84.7% | 0.1532 | 29.4% |
| cc | 0.899 | 0.892 | 0.874 | 0.910 | 0.919 | 0.0450 | 92.8% | 0.0721 | 50.0% |
| ga | 0.633 | 0.649 | 0.631 | 0.595 | 0.658 | 0.0631 | 46.8% | 0.5315 | 25.4% |
| ra | 0.980 | 0.973 | 0.991 | 0.973 | 0.982 | 0.0180 | 98.2% | 0.0180 | 0.0% |
| cp | 0.991 | 0.991 | 0.991 | 0.991 | 0.991 | 0.0000 | **100.0%** | 0.0000 | 0.0% |
| gsp | 0.984 | 0.982 | 0.982 | 0.982 | 0.991 | 0.0090 | 98.2% | 0.0180 | 50.0% |
| st | 0.414 | 0.342 | 0.387 | 0.505 | 0.423 | 0.1622 | 61.3% | 0.3874 | 39.5% |

### 53.5 Where the reward's signal and noise actually come from

Summing the weighted columns over the metrics that carry non-zero weight (full corpus):

**Systematic arm-separating signal** (`Σ w*Sprd = 0.0957`):

| metric | w\*Sprd | share of total signal |
|---|---|---|
| **de** | 0.0586 | **61.2%** |
| **be** | 0.0151 | **15.8%** |
| fl | 0.0135 | 14.1% |
| cc | 0.0043 | 4.5% |
| ga | 0.0021 | 2.2% |
| ra | 0.0021 | 2.2% |

**Total variation injected into the reward** (`Σ w*Rng = 0.2827`):

| metric | w\*Rng | share of total variation |
|---|---|---|
| de | 0.0826 | 29.2% |
| **ga** | **0.0734** | **26.0%** |
| fl | 0.0645 | 22.8% |
| cc | 0.0291 | 10.3% |
| be | 0.0283 | 10.0% |
| ra | 0.0048 | 1.7% |

### 53.6 Findings

**F1 — `cp`, `ra`, `gsp` are already satisficing metrics in everything but name.**
`%const` = 99.6% / 96.8% / 97.9%; means pinned at 0.996 / 0.986 / 0.988. `cp` is **100.0%
constant across all 111 TEST sections** — it literally never differs between arms there. `ra`
nonetheless carries a **0.15 weight** while supplying 2.2% of the systematic signal. These three
are pure quality floors: they detect "something went badly wrong," which is a real and useful
thing to detect, but it is a *gate* function, not a *ranking* function.

**F2 — `ga` is the single worst term in the formula: maximum noise, near-zero signal.**
It has the **largest per-section variation of any metric** (`meanRng = 0.489`) and yet the arm
means are effectively flat (0.702 / 0.702 / 0.688 / 0.699 ⇒ `armSprd = 0.014`, `SNR = 0.03`,
`monoUp = 23.9%` ≈ chance). Consequently **`ga` injects 26.0% of all reward variation while
supplying 2.2% of the systematic signal** — the clearest single contributor to the
thin-margin / near-tie problem in §52.2.

This is mechanistically consistent with an earlier (2026-07-25) decomposition of the
`user_intent` term via `analyze_user_intent_gap.py` — not previously written up in this document.
That analysis classified the grader's own stated reasons across n=257 `ga = 0` disagreement cases
(sections where some arm passed `ga` while `standard`/`deep` failed) and found only **24.5%**
were length-tolerance violations, while **40.5%** explicitly *passed* the length check and failed
for another reason and **35.0%** never mentioned length. Qualitative sampling of the non-length
75% found the dominant failure mode to be **missing mandated visual elements** (images, mermaid
diagrams, figures the guideline explicitly requires) — a *writing-workflow* defect with no reason
to correlate with exploration depth. `ga` is measuring something real; it is simply not measuring
anything about *how much research the article needed*.

**F3 — the exploration metrics carry the overwhelming majority of the real signal.**
`de` + `be` together supply **77.0% of all systematic arm separation** from only 39.2% of the
variation. `de` alone is 61.2% of the signal, with the cleanest behaviour of any metric: a
monotone ladder 0.000 → 0.139 → 0.155 → 0.195, the top `SNR` (0.71), the lowest `%const`
(41.8%), and the highest `monoUp` (50.6%, double chance). `be` is second-best by `SNR` (0.53) but
**non-monotone** — it peaks at `standard` (0.075) and *falls* at `deep` (0.060), consistently in
both splits. This is a real property worth remembering: a third exploration round tends to add
*depth*, not *breadth*.

**F4 — `cc` trends the wrong way and is mostly constant.**
Full corpus: skip 0.901 → deep 0.879, i.e. **more exploration mildly degrades core-content
fidelity** (most visible in TRAIN: 0.906 → 0.854). It is 85.5% constant, `monoUp` only 22.0%. At
`w = 0.20` it is a meaningful weight spent on a term that both fails to differentiate and mildly
penalises deep. *(Note the TRAIN/TEST sign disagreement — TEST shows 0.892 → 0.919, the opposite
direction. The pooled effect is small and split-unstable; treat "cc is non-differentiating" as
the robust claim and "cc penalises deep" as TRAIN-specific and tentative.)*

**F5 — `st` (structure) would have been a poor addition, confirming its exclusion.**
`SNR = 0.10`, `armSprd = 0.043` against `meanRng = 0.415`, and its arm ordering disagrees between
splits. Excluded from the reward today; this data supports keeping it excluded.

### 53.7 Implication

The current formula spends **0.30 of additive weight** (`ga` 0.15 + `ra` 0.15) on two metrics
that jointly contribute **4.4% of the systematic arm signal**, while one of them is the largest
single noise source in the whole reward. Meanwhile `de`+`be` carry 77% of the signal at 0.50
weight. Reallocating weight toward the exploration terms — and demoting `cp`/`ra`/`gsp` (and
possibly `ga`) to gates — should raise effective margins and reduce noise-driven label churn
simultaneously, addressing both symptoms in §52.2.

**What this analysis does *not* settle:** whether a demoted `ga` should be a **hard gate**
(fail ⇒ section reward zeroed/floored) or **dropped entirely**. `ga` still varies in 51% of
sections, so a hard gate would remain active in about half the corpus and could re-admit the same
noise through a different mechanism. §54 models both.

### 53.8 Caveats

1. **`armSprd` is a mean-of-means.** It measures *systematic* differentiation and deliberately
   cancels section-level idiosyncrasy. A metric with genuinely section-specific but
   arm-informative behaviour (different arms win in different sections, netting to zero on
   average) would be understated. `%const` partially guards against this — a metric that is
   constant within sections cannot have hidden per-section signal — but `ga` (51% varying,
   flat means) is precisely the shape where this caveat bites hardest, and it deserves the
   per-section modelling in §54 rather than dismissal on `armSprd` alone.
2. **Grades are binary per section** (except post-curve `de`/`be`), so `meanRng` is dominated by
   0↔1 flips; a `meanRng` of 0.49 for `ga` means roughly half of sections have at least one arm
   disagreeing with another.
3. **Single-draw labels.** Every value is one grading draw of one written article; Part 4
   established real run-to-run content noise. These aggregates are over 282 sections so they are
   far more stable than any individual cell, but per-metric noise floors were not separately
   re-measured here.
4. **`de`/`be` are post-`enhancement_credit()`**, so their `%const` and `meanRng` reflect the
   shipped G0/J0 curve, not raw grader output. Re-tuning that curve would move these numbers.

## 54. Modelling the redesign: hard vs. soft satisficing gates

### 54.1 Tool and method

New read-only diagnostic: **`research_agent_local/training/model_gate_candidates.py`**.
Zero LLM calls, zero writes, no production constant touched. It recomputes section-level rewards
for the whole 40-article corpus under each candidate formula and then replicates, exactly:

- `train_grpo.load_section_groups`'s flat-drop rule (`spread < sigma_floor = 0.04`),
  `hit_sigma_floor` test (`raw_std < 0.04`), and normalized advantage
  (`regret / max(std, sigma_floor)`);
- `compute_article_oracle._compute_r_w`'s **candidate-E** split aggregation — `rewards − explore`
  target-words-weighted, `explore` simple-mean — and the `EPS_BAND = 0.03` thin-margin test.

**Gate semantics modelled:**
- **hard gate** — any gated metric failing (`< 0.5`) ⇒ the section forfeits *all* content and
  explore credit, retaining only the cost debit.
- **soft gate** — failing subtracts a flat penalty from `rest`; the arm keeps its explore credit.

In every candidate, weight freed by demoting a metric is reallocated to `de`/`be` (the
77%-of-signal terms per §53.5). All candidates B–F use `cost_coef = -0.03`, so **`A1` is the
correct baseline for comparison** (`A0` is shown only to locate current production).

### 54.2 Results

TRAIN block (n = 171 sections / 24 articles); ALL block (n = 282 sections / 40 articles):

| candidate | floor% | nearTie | advNorm | medMargin | TRAIN sec sk/li/st/dp | TRAIN art sk/li/st/dp | ALL floor% | ALL nearTie-proxy (thin art) | ALL art sk/li/st/dp |
|---|---|---|---|---|---|---|---|---|---|
| `A0` current, cost −0.02 | 24.6% | 64.3% | 1.108 | 0.0421 | 44/55/39/33 | 5/10/3/6 | 25.6% | 20 | 5/18/5/12 |
| **`A1` baseline, cost −0.03** | 22.9% | 61.2% | 1.144 | 0.0392 | 51/56/34/30 | 7/10/3/4 | 24.6% | 21 | 11/18/4/7 |
| `B` drop `ra` only | **19.3%** | 57.9% | 1.175 | 0.0424 | 44/56/38/33 | 5/11/3/5 | **19.5%** | 21 | 6/20/4/10 |
| `C1` soft `ga`, pen 0.05 | 23.1% | 56.8% | 1.200 | 0.0393 | 45/56/35/35 | 3/12/3/6 | 26.0% | 17 | 4/19/8/9 |
| **`C2` soft `ga`, pen 0.10** | 20.5% | **55.6%** | **1.206** | **0.0436** | 43/56/38/34 | 3/11/4/6 | 23.4% | 16 | 4/18/7/11 |
| `D` **hard** `ga` | 23.4% | 56.1% | 1.172 | 0.0393 | 54/48/39/**30** | 5/11/6/**2** | 25.2% | **13** | 8/19/7/**6** |
| `E` hard trio, drop `ga` | 22.2% | 59.6% | 1.178 | 0.0383 | 46/52/39/34 | 4/11/5/4 | 25.2% | 18 | 4/17/10/9 |
| `F` hard trio, drop `ga`+`cc` | 24.0% | **55.0%** | **1.210** | 0.0445 | 48/47/39/**37** | 4/12/2/6 | 25.9% | 15 | 4/18/7/11 |

*`floor%` = of kept sections, share with `raw_std < sigma_floor` (gradient artificially floored —
the §52.2 symptom). `nearTie` = share of kept sections with 2+ arms within 0.06 of the best.
`advNorm` = mean normalized GRPO advantage. `thin art` = articles needing an `EPS_BAND` tie-break.*

### 54.3 The decisive finding: a hard `ga` gate structurally suppresses `deep`

Candidate `D` (hard gate) posts respectable aggregate numbers — it has the *lowest* thin-article
count (13) — but it **collapses `deep` representation**: TRAIN article-level `deep` falls from 4
(baseline) to **2**, and corpus-wide from 7 to 6, while `skip`/`standard` rise. That is the exact
label-imbalance failure this whole investigation has been fighting, reintroduced by the gate.

The mechanism is an **asymmetry in what each arm has to lose**, and it is measurable directly:

| arm | `ga`-fail rate | mean explore credit | explore forfeited to a hard gate | **% of its explore destroyed** |
|---|---|---|---|---|
| skip | 29.8% | 0.0000 | 0.0000 | **0.0%** |
| light | 29.8% | 0.0828 | 0.0173 | **20.9%** |
| standard | 31.2% | 0.0902 | 0.0350 | **38.8%** |
| deep | 30.1% | 0.1060 | 0.0359 | **33.9%** |

**All four arms fail `ga` at essentially the same rate (~30%)** — `ga` is arm-neutral, exactly as
§53.6/F2 established. But a hard gate's *consequence* is radically unequal: `skip` has zero explore
credit and therefore loses nothing, while `standard`/`deep` forfeit ~34–39% of the single term
that carries 77% of the real arm signal. A hard gate thus converts an arm-**neutral** noise source
into a strongly arm-**biased** penalty on exactly the arms we are least able to afford losing.

This confirms the user's prior intuition against hard gates, and supplies the mechanism: it is not
that hard gates are too strict in general — it is that gating *multiplicatively destroys the
discriminative term*, and only the expensive arms have such a term to destroy.

### 54.4 What the soft gates buy

Comparing against the correct baseline `A1`:

- **`C2` (soft `ga`, penalty 0.10)** is the strongest all-round candidate:
  `floor%` 22.9% → **20.5%**, `nearTie` 61.2% → **55.6%**, `advNorm` 1.144 → **1.206** (+5.4%),
  median margin 0.0392 → **0.0436** (+11%), thin articles 21 → **16**, and the arm distribution
  stays healthy (TRAIN articles 3/11/4/6; corpus 4/18/7/11 — `deep` *improves* from 7 to 11).
  Every headline signal-quality index moves the right way with no class collapse.
- **`B` (drop `ra` only)** is the most conservative option and posts the **best `floor%` of any
  candidate** (19.3% / 19.5%) — a 3.6pp / 5.1pp absolute reduction — for a one-line change with
  minimal label disruption. It does less for `nearTie` and `advNorm` than `C2`.
- **`F`** edges `C2` on `advNorm` (1.210) and `nearTie` (55.0%) and yields the most balanced
  *section-level* distribution (48/47/39/37), but it also drops `cc` entirely — a bigger
  semantic change resting on the split-unstable `cc` finding (§53.6/F4), so its apparent edge
  over `C2` is within the uncertainty of that caveat.

### 54.5 Recommendation (not yet shipped)

1. **Reject hard gates** for `ga` — mechanism-level evidence in §54.3, not just an aggregate
   preference.
2. **`cp` / `ra` / `gsp` can be demoted safely** — they are ≥96.8% constant, so *any* gate
   treatment barely moves the corpus (`B` disrupts almost nothing while measurably improving
   `floor%`). If a hard gate is wanted anywhere, it belongs here, where it cannot bite
   asymmetrically because it essentially never fires.
3. **`C2` (soft `ga`, penalty ≈0.10) is the recommended primary candidate**, with `B` as the
   low-risk fallback if minimal label churn is preferred over maximal signal gain.
4. **Still to do before any ship** — this section is a *model*, not a validation. Per the
   discipline established throughout this document, a real ship requires: backup → edit
   production constants → full 42-article `generate_episode_oracles.py` + `compute_article_oracle.py`
   regen → diff (flip count, comfortable-vs-thin) → replicate-majority-vote re-check on
   `06_tools__var_standard` / `09_RAG__var_standard` → and updating every `_PROD_*` mirror
   constant (`sweep_reward_formula.py` et al., per the thrice-recurring staleness bug).
5. **Open question not settled here:** whether `ga` should be a soft gate *at all* versus simply
   dropped (weight 0). `C1`/`C2` differ only in penalty size and both beat baseline; a
   penalty-0.0 variant (pure drop) was not separately modelled and is the obvious third point to
   add before deciding. **Resolved in §54.6 below.**

## 54.6 Follow-up: pure drop vs. soft penalty, and how far to push the penalty

Two more candidates added to `model_gate_candidates.py`, holding `cc`/`fl`/`de`/`be` weights and
the (inert, near-never-firing) `cp`/`ra`/`gsp` treatment identical across all four, so the *only*
thing varying is `ga`'s treatment — isolating exactly the question in §54.5 item 5:

- **`G_pure_drop_ga`** — `ga` carries zero weight and is not gated at all (no penalty of any
  kind; equivalent to simply deleting it from the formula).
- **`C3_soft_ga_pen015`** — same soft-gate mechanism as `C1`/`C2`, penalty raised to `0.15`.

| candidate | penalty | floor% (TRAIN / ALL) | nearTie | advNorm (TRAIN / ALL) | thin art (TRAIN / ALL) | corpus `deep` |
|---|---|---|---|---|---|---|
| `G` pure drop | — | 22.8% / 26.2% | 59.6% | 1.187 / 1.189 | 10 / 16 | 9 |
| `C1` soft | 0.05 | 23.1% / 26.0% | 56.8% | 1.200 / 1.198 | 9 / 17 | 9 |
| **`C2` soft** | **0.10** | 20.5% / 23.4% | 55.6% | **1.206** / 1.197 | 9 / **16** | **11** |
| `C3` soft | 0.15 | **17.5%** / **19.1%** | **52.6%** | 1.203 / **1.205** | 9 / 19 | 10 |

**Finding 1 — a pure drop is strictly dominated.** `G` underperforms *every* penalized variant on
`floor%`, `nearTie`, and `advNorm`, and has worse `deep` representation than `C2`. This is
informative given §54.3 established `ga`'s *failure rate* is arm-neutral: even though *which arm*
fails isn't informative, *which specific sections* fail still carries some real content signal,
and a flat penalty recovers part of it, a bare drop discards it entirely.

**Finding 2 — returns past `0.10` trade section-level gains for article-level cost.**
`floor%`/`nearTie` keep improving monotonically as the penalty rises (`C3` is best on both), but
the article-level **thin-margin count gets *worse* at `0.15`** (19 — worse than even the pure-drop
control's 16) and corpus `deep` dips from 11 to 10. Since GRPO trains on *section-level* rewards
while the article-level oracle is what downstream eval and labelling trust, `C3` is improving the
training signal at a real cost to label decisiveness — the two objectives diverge past `~0.10`.

**Conclusion: `C2` (soft `ga` gate, penalty ≈0.10) is confirmed as the best all-round candidate.**
It is the only variant that improves signal quality, article-level decisiveness, *and* `deep`
representation simultaneously rather than trading one for another — superseding the tentative
recommendation in §54.5.

## 54.7 Does the redesign change the "safe" `cost_coef`?

`C2`'s formula swept across every `cost_coef` value this whole investigation has tested, to see
whether fixing the `ga`-noise problem also fixes deep-scarcity independent of `cost_coef` (i.e.
does the redesign let us use a *larger*, safer cost penalty again?).

| `cost_coef` | floor% (TRAIN / ALL) | advNorm | corpus `deep` | thin articles |
|---|---|---|---|---|
| -0.06 | **8.2% / 9.6%** | **1.266** | 3 | 10 |
| -0.045 | 21.1% / 23.8% | 1.258 | 4 | 19 |
| **-0.03** | 20.5% / 23.4% | 1.206 | **11** | 16 |
| -0.02 | 20.5% / 22.7% | 1.166 | 13 | 18 |

**Answer: no — `cost_coef` and the `ga`-redesign fix two different problems, and both are needed.**
`floor%` does not move gradually with `cost_coef`; it jumps sharply between `-0.06` and `-0.045`
(8.2%→21.1%), and `C2` is better than baseline `A1` at every value tested, so the redesign helps
regardless of `cost_coef`. But **deep-scarcity is not resolved by the redesign alone**: even with
`ga`'s noise fixed, `-0.06`/`-0.045` still suppress `deep` to only 3-4 articles corpus-wide — the
jump to healthy representation (11) only happens once `cost_coef` reaches `-0.03`. **Decision:
keep `cost_coef = -0.03`** — it is where `deep` representation recovers *and* `C2`'s signal-quality
gains are fully intact, without paying the extra thin-article cost of pushing to `-0.02`.

## 54.8 Article-level threshold gate on `cp`/`ra`/`gsp` (0.90/0.95) — modelled and rejected

Prompted by the idea of hard-gating `research_anchoring`, `core_preservation`, and
`golden_source_priority` at a high threshold (0.90 or 0.95). First check:
**`cp`/`ra`/`gsp` are strictly binary at the section level** (only `{0.0, 1.0}` observed
corpus-wide, verified directly against every `reasoning.json` grade) — so a fractional threshold
can only be meaningful as an **article-level aggregate** (mean across an arm's sections), not a
per-section check. This is a different kind of mechanism than the `ga` soft-gate (which lives in
the section-level reward `train_grpo` trains on) — it belongs alongside the *existing*
`policy=forbidden` / `manual_override` layer in `compute_article_oracle.py`.

**Mechanism modelled** (`training/model_article_gate.py`): for each (article, arm), compute
`mean(cp)`, `mean(ra)`, `mean(gsp)` across that arm's sections (using the `C2` formula for `R_w`);
exclude any arm below the threshold from the article's argmax.

| threshold | arms gated out | winner changed | **no eligible arm at all** |
|---|---|---|---|
| 0.90 | 11/40 articles | 2 | **2** |
| 0.95 | 12/40 articles | 3 | **2** |

**Rejected — a real, mechanism-level problem, not just an aggregate concern.** Both "no eligible
arm" cases are **structural, not quality-driven**, verified directly:

```
06_tools__var_standard:  gsp = 0.889 for ALL 4 arms (identical)
04_structured_outputs:   cp = ra = gsp = 0.857 for ALL 4 arms (identical, all three metrics)
```

One specific section fails these dims universally, regardless of exploration depth — the gate
cannot discriminate *which arm is safer* here, it disqualifies the whole article for reasons
unrelated to arm choice. Critically, **`06_tools__var_standard` is our one confirmed-ground-truth
article** (`deep`, validated by 3-1 replicate-majority-vote, §31) — this gate design would
disqualify the *correct* answer along with every other arm. Resolved in §56.

## 55. Where does `sigma_floor = 0.04` come from — is it justified, and can we do better?

### 55.1 Provenance

Traced directly in code: `sigma_floor` is an `argparse` default in `train_grpo.py`
(`--sigma-floor`, default `0.04`), used for two jobs — (1) the flat-group filter (drop groups
whose `max-min` reward spread is "just noise") and (2) the advantage-normalisation floor
(`std_r = max(raw_std, sigma_floor)`). **It has no documented empirical derivation anywhere in
this repository.** The only nearby code comment references a *different* value (`0.05`, "raw_std
just clears sigma_floor in cost-only tie case") inside the variant-conditional formula that
Formula B has since replaced entirely. **Verdict: not strongly justified — an inherited,
unexplained constant.**

### 55.2 An empirical estimate exists, and it disagrees with 0.04 by 2.5×

New tool: **`training/estimate_noise_floor.py`**. Uses the exact data this question calls for —
the noise-experiment replicates (§22-23): 2 articles (`09_RAG__var_standard`,
`06_tools__var_standard`) × 4 arms × 3 independent write+grade replicates, re-graded with the
*current* Claude + enhancement-credit pipeline — and measures the real run-to-run reward noise of
the same `(article, section, arm)` cell, recomputed via the actual production
`_section_reward_components()`.

| | value |
|---|---|
| n cells (section × arm, ≥2 replicates) | 60 |
| mean per-cell noise sd | **0.0991** |
| median per-cell noise sd | 0.0866 |
| p90 per-cell noise sd | 0.2021 |
| noise on an arm-to-arm **difference** (√2 × cell sd) | **≈ 0.140** |
| share of cells with replicate-noise sd **below** 0.04 | 21.7% |

**The measured noise is ~2.5× the current `sigma_floor`.** A reward spread of `0.04` between two
arms is only `0.40×` the *mean single-cell* noise sd — i.e. `sigma_floor` is currently far too
permissive to be doing the job its help text claims.

### 55.3 Raising the floor doesn't fix it — it just discards data

Swept `sigma_floor` against the whole corpus under `C2`/`cost_coef=-0.03` (`training/sweep_sigma_floor.py`):

| `sigma_floor` | dropped | floored% (of kept) | meanAdv | margin > 1 noise-sd | margin > 2 noise-sd |
|---|---|---|---|---|---|
| **0.04** (current) | 0 (0%) | 23.4% | 1.197 | **45 (16%)** | **10 (4%)** |
| 0.06 | 4 (1%) | 39.6% | 1.099 | 45 (16%) | 10 (4%) |
| 0.08 | 52 (18%) | 43.5% | 1.097 | 45 (20%) | 10 (4%) |
| 0.10 | 63 (22%) | 55.3% | 1.031 | 45 (21%) | 10 (5%) |
| 0.14 | 95 (34%) | 68.4% | 0.935 | 45 (24%) | 10 (5%) |

**The absolute count of statistically-defensible sections never changes — 45 (margin exceeds one
noise sd) and 10 (exceeds two sd) at every `sigma_floor` value tested.** Raising the floor only
shrinks the denominator (discards up to 34% of training groups at `0.14`) without buying a single
additional confidently-labelled section. At `sigma_floor=0.04`, the flat-drop rule fires on
**zero** groups today — that half of the mechanism is currently inert.

**The uncomfortable headline finding, independent of any threshold choice**: only **16% of
sections (45/282) have a top-1-vs-top-2 margin exceeding one sd of measured noise, and just 4%
(10/282) exceed two sd.** For roughly 84% of sections, which arm "wins" is not statistically
distinguishable from single-draw noise. This is a measurement-floor fact about the labelling
pipeline, not something any reward-formula reweighting can fix.

### 55.4 `near_tie_margin` is the better-targeted knob — but changing it is deferred

`near_tie_margin` (default `0.06`) is the parameter that actually encodes "these arms are
indistinguishable" (it governs `acceptable_idxs`, i.e. which arms count as a correct prediction),
as opposed to `sigma_floor` which only affects the *training* denominator and the flat-drop filter.
Checked directly: at the current `0.06`, only 57.8% of sections have 2+ "acceptable" arms; at a
value matching the measured noise (`0.14`), that rises to 84.0% (mean 2.84 acceptable arms) — much
closer to the true state of measurement precision established in §55.3.

**Per explicit user instruction (2026-07-29): do not raise `near_tie_margin` at this time.** This
finding is recorded for the future, not acted on. Recommended alternative already noted in §55.3:
the only real fix for label confidence is **replication** — averaging 3 draws would cut noise sd
by `√3` (≈0.140 → 0.081 for an arm-difference), which should roughly double the fraction of
sections with a statistically defensible winner. That remains the honest, if expensive, path;
Part 4 reached the same conclusion independently.

### 55.5 Recommendation

- **Leave `sigma_floor` at its current `0.04`** (or `0.06` if a small safety margin is wanted) —
  raising it further costs real training data for zero gain in statistically-defensible sections.
- **Do not raise `near_tie_margin` right now** (user decision, 2026-07-29) — the finding that
  `0.14` would better match measured noise is recorded here for a future revisit.
- **The durable fix, if ever pursued, is replication, not a threshold change.**

## 56. Final recommendation: `ra` / `cp` / `gsp` become diagnostic metadata, not gates

Combining §53 (differentiation), §54.3 (hard-gate asymmetry), and §54.8 (article-level threshold
gate rejected — structural false positives on the one confirmed-ground-truth article):

- **`ra` (research anchoring) — remove from the additive reward entirely.** 96.8% constant,
  currently costs `0.15` weight for `2.2%` of the systematic signal (§53.5/53.6 F1). This is
  already exactly what candidate `B` (drop `ra` only) modelled, and it posted the **best `floor%`
  of any candidate tested** (19.3%/19.5%) for a one-line change. Weight reallocated to `de`/`be`.
- **`cp` (core preservation) — unchanged.** It is *already* a multiplicative gate on the explore
  term (`explore = cp * (...)`) rather than an additive weight — precisely the satisficing design
  this whole redesign is aiming for elsewhere. 99.6% constant; costs nothing; no change needed.
- **`gsp` (golden source priority) — already zero weight; stays that way.**
- **None of the three become threshold-based decision gates.** §54.8 demonstrated why directly:
  because they are section-binary, a fractional threshold is only meaningful as an article-level
  aggregate, and at that level it produces **false positives on structural, arm-invariant cases**
  — including disqualifying every arm of `06_tools__var_standard`, our one confirmed-ground-truth
  article, for reasons unrelated to which arm was chosen.
- **Instead, surface `cp`/`ra`/`gsp` as diagnostic metadata** — attach per-arm aggregate values (and
  a `needs_review`-style flag) to `article_oracle.json` for human/eval-time inspection, without
  letting them influence `oracle_arm` at all. This preserves their genuine value as safety-signal
  diagnostics (a low `cp`/`ra`/`gsp` *does* mean something concerning happened) while keeping them
  out of a ranking decision they have been shown not to be able to inform safely.
- **Open parameter, explicitly not settled here (user note, 2026-07-29): 0.90 may itself be too
  high a bar even for a non-blocking diagnostic flag**, given `cp`/`ra`/`gsp`'s corpus-wide means
  sit at 0.996/0.986/0.988 — a flag threshold that fires only when an article-arm mean drops
  further, e.g. somewhere in the 0.75-0.85 range, may be more appropriate for "worth a human
  glance" than for "certainly broken." To be finalised during implementation (§57 Phase 5), not
  modelled further at this time.

## 57. Implementation roadmap: `ra`-removal + `C2` combination (planned, NOT YET STARTED)

This section is a plan only — **no production files have been touched for this change.** It
follows the exact discipline established for every prior ship in this document (G0, H0, J0,
EPS_BAND, the staged `cost_coef` reductions): backup first, edit, full-corpus regen, diff,
non-circular replicate-majority-vote re-check, then update every `_PROD_*` mirror constant.

**Final combined design** (supersedes `A0`/current production):

```
gt_base     = 0.20*cc + 0.20*fl                                    (unchanged)
explore     = cp * (0.45*de + 0.30*be)                              (was cp*(0.60de+0.40be)*0.50;
                                                                      de/be weight raised, ra's
                                                                      freed weight folded in)
ga_penalty  = -0.10 if ga < 0.5 else 0.0                            (NEW: soft gate, replaces
                                                                      ga's old additive term)
cost        = -0.03 * nr                                            (reverted from -0.02)
reward      = gt_base + explore + ga_penalty + cost
```

`ra` no longer appears anywhere in the additive formula. `cp` keeps its existing multiplicative
role in `explore`, unchanged. `gsp` remains at zero weight (unchanged).

**Phase 1 — Backup.** Full copy of `rl_training_data/bases/` (all 42 article dirs, including the
2 mixeddepth/goldremoved pilots) to a timestamped `bases_PRE_C2_RAREMOVAL_<date>/` directory.
Verify 42/42 `article_oracle.json` present before proceeding — this is the only rollback path
(`bases/` is gitignored).

**Phase 2 — Code change.** Edit `generate_episode_oracles.py`'s `_section_reward()` and
`_section_reward_components()` (both must change identically, as with every prior ship):
implement the formula above. This is more invasive than prior ships (G0/H0/J0/cost_coef were
constant tweaks; this adds an actual conditional gate) — write it as a small named helper
(e.g. `_ga_gate_penalty(ga: float) -> float`) rather than inlining the conditional, so it's
independently unit-testable and greppable for the mirror-constant checklist in Phase 6.

**Phase 3 — Regenerate.** `generate_episode_oracles.py --force` (24 TRAIN default) +
`--articles <16 TEST + 2 pilots> --force`, then `compute_article_oracle.py --force` on the same
41/42-article split. Also implement §56's diagnostic metadata addition in
`compute_article_oracle.py` in this same pass (per-arm `cp`/`ra`/`gsp` aggregates +
`needs_review`-style flag at whatever threshold is finalised — see §56's open parameter).

**Phase 4 — Diff.** Reuse `diff_oracle_regen.py --before bases_PRE_C2_RAREMOVAL_<date>` (the same
tool used for every prior ship). Expect and specifically check: flip count, thin-vs-comfortable
margin classification, and that policy=forbidden / manual-override articles are untouched (both
mechanisms are independent of `R_w` by construction and should show zero movement).

**Phase 5 — Non-circular replicate-majority-vote re-check.** Recompute `R_w` for the existing
`noise_experiment/` replicates (both `09_RAG__var_standard` and `06_tools__var_standard`, 3
replicates × 4 arms each, already on disk — zero new generation) under the new formula. Confirm
`06_tools__var_standard`'s majority vote is still `deep` (it has held `deep` unanimously or
near-unanimously across *every* formula variant tested this entire investigation — this is the
load-bearing check). `09_RAG__var_standard` is expected to remain its known persistent toss-up;
this is not a red flag on its own, per established precedent.

**Phase 6 — Update every `_PROD_*` mirror constant.** Per the thrice-recurring staleness-bug
pattern (§ "SWEEP TOOL BUG FOUND+FIXED", 2026-07-25): grep the entire `training/` directory for
every script that independently recomputes reward components — at minimum
`sweep_reward_formula.py` (`_PROD_COST_COEF`, `_PROD_CREDIT_CURVE`, and a new mirror for the
`ga`-gate penalty), `analyze_cost_imbalance.py`, `measure_replicate_noise.py`, and any other
script identified by the grep. Do not assume the sweep tool's mirror is the only one — verify by
reproducing a known real `R_w`/margin value exactly (the `06_tools__var_standard` /
`09_RAG__var_standard` sanity check already used for every prior ship).

**Phase 7 — Explicit sign-off checkpoint.** Present the Phase 4 diff and Phase 5 replicate-vote
result to the user before proceeding to Phase 8. This is a genuine decision point, not a
formality — every prior formula change in this document went through this gate before touching
anything training-facing.

**Phase 8 — Retrain.** New task, fresh (not resumed — training inputs changed materially, same
rule applied to every prior formula-driven retrain in this document). Recommended hyperparameters
unchanged from the `run17`-`run19` recipe except `--inv-freq-temp 0.5` (the script default,
exonerated as a cause in Part 7 §52.1 — do not re-introduce the escalation):
`--epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 --warmup-epochs 10 --patience 50
--lora-r 16 --lora-alpha 16 --lora-dropout 0.05 --sigma-floor 0.04 --near-tie-margin 0.06`
(both left at current values per §55.5's decision not to change them now).

**Phase 9 — Evaluate.** `test_grok_planner.py --rl-only --save-json` once a checkpoint is chosen
(prefer checking `best_er`/`best_strict` both, per established practice, and cross-referencing
against training-log entropy/plateau behaviour before picking one — do not trust train-only
metrics, per the `run14_phase0` lesson). **Primary comparison baseline: `run15_recalibrated`**
(the last checkpoint trained on `cost_coef=-0.03`, confirmed 2026-07-28: TEST exact 33%, MAE
0.933, only 1 high-confidence miss, `deep` predicted 6/16) — since this new run shares the same
`cost_coef` and the same (exonerated, unescalated) `inv-freq-temp`, any improvement over `run15`
is cleanly attributable to the `ga`-gate + `ra`-removal reward redesign, isolating exactly the
variable this whole Part 7 investigation set out to test.

## 58. `C2` shipped — execution log and before/after signal-strength comparison (2026-07-29)

Phases 1-6 of §57's roadmap were executed for real, in order, with no deviations from the plan
except two corrected CLI-flag assumptions (documented below).

**Phase 1 — Backup.** `rl_training_data/bases/` copied to `bases_PRE_C2_RAREMOVAL_20260729/`
(45 article dirs, including the 3 non-official pilots) before any edit.

**Phase 2 — Code change.** `generate_episode_oracles.py`'s `_section_reward()` and
`_section_reward_components()` rewritten to the exact formula from §57. New
`_ga_gate_penalty(ga)` helper added (`-0.10 if ga < 0.5 else 0.0`). `ra` kept as an accepted-but-
unused parameter for call-site compatibility. Verified directly: `ra` is fully inert, the `ga`
gate fires exactly at the 0.5 boundary, and `rest + explore == _section_reward(...)` still holds.

**Phase 3 — Diagnostic metadata + regeneration.** `section_oracle.json` bumped to version 5:
each section gained a per-arm `"diagnostics"` dict (`cp`/`ra`/`gsp`, raw, not reward-weighted;
`gsp` now loaded via a new `_DIAG_DIMS` list added to `_load_episode`'s filter, since
`_REWARD_DIMS` itself deliberately excludes it and was left untouched to stay in sync with
`train_grpo.py`'s parallel list). `compute_article_oracle.py` bumped to version 3: new
`_compute_gate_diagnostics()` (simple per-arm mean of `cp`/`ra`/`gsp` across sections, `None` for
pre-v5 data) plus `gate_diagnostics`/`low_signal_flag` output fields (new
`DIAG_LOW_SIGNAL_THRESHOLD = 0.85` constant) — informational only, does **not** affect
`oracle_arm`. Uses a new field name, not `needs_review` (already means something unrelated: no
S3/S4/S5 tiebreak signal cleared its threshold). All 42 official articles (24 TRAIN + 16 TEST + 2
mixeddepth) regenerated to `section_oracle.json` v5 + `article_oracle.json` v3.

**CLI-flag corrections vs. the original §57 plan:** `generate_episode_oracles.py` has **no**
`--force` flag — it always overwrites unconditionally (`--dry-run` is the only write-suppressing
flag). `compute_article_oracle.py` **does** have `--force` (default is skip-if-exists). The 3
non-official pilots (`05_workflow_patterns__depthboost`, `11_multimodal__depthboost`,
`10_memory_knowledge_access__var_goldremoved`) were correctly left untouched (out of scope).

**Phase 4 — Diff** (`diff_oracle_regen.py --before bases_PRE_C2_RAREMOVAL_20260729`): 40/45
unchanged, 5 flipped, **all thin-margin, zero comfortable**. Arm distribution
`{skip:10,light:14,standard:12,deep:9}` → `{skip:10,light:15,standard:11,deep:9}`.
`06_tools__var_standard`/`09_RAG__var_standard` not in the flip list (unchanged). Flips:
`02_workflows_vs_agents__var_demanding` standard→light, `06_tools__var_demanding` standard→deep,
`10_memory_knowledge_access__var_demanding` deep→standard, `Dark_Dimension` standard→deep,
`Earth_Oceans_Origin` deep→standard.

**Phase 5 — Non-circular replicate-majority-vote re-check** (`measure_replicate_noise.py`,
imports `geo._section_reward` directly so it automatically reflects `C2`, no code changes
needed). `06_tools__var_standard` (the load-bearing article) stays `deep`, margin improved
0.0010 → 0.0914 (no longer needs any tiebreak at all). Replicate votes deep=2/standard=1 —
**identical to the 3-1-combined-majority pattern under every prior formula tested this entire
investigation** (cost -0.06 through -0.03, G0, J0, H0). `09_RAG__var_standard` replicate votes
light=2/standard=1/deep=0 — the same historical toss-up character as always; no label change
forced, per the long-established decision rule.

**Phase 6 — Mirror constants.** `sweep_reward_formula.py`'s `_PROD_COST_COEF` was found *already*
stale at -0.02 (left over from the run17-19 era, never reverted after that regressed) — fixed to
-0.03. Since `C2` changes the formula's *shape* (not just a value), both `_recompute_from_episode_dims`
and `_recompute_core` were rewritten (new `_PROD_DE_WEIGHT=0.45`/`_PROD_BE_WEIGHT=0.30`/
`_PROD_GA_GATE_THRESHOLD=0.5`/`_PROD_GA_GATE_PENALTY=-0.10`, `ra` removed). `_PROD_EXPLORE_MULT`
kept defined but retired from the formula (only referenced by `majority_vote_sweep`/
`corpus_explore_mult_sweep`, whose whole premise — a single explore scalar — no longer maps onto
`C2`; their explore_mult grids are archived/pre-`C2`). `analyze_cost_imbalance.py` had its own
independent inline formula copy (the 4th documented instance of this staleness-bug class) — fixed
identically, `user_intent` component renamed to `ga_gate` throughout. Both scripts verified to
reproduce real production `R_w` **exactly** (6-decimal match) for `06_tools__var_standard` and
`09_RAG__var_standard`. `measure_replicate_noise.py` re-confirmed already clean. Left untouched
(already-documented dead/stale code, established "do NOT revive" precedent): `analyze_dataset.py`,
`eval_accuracy.py`, `test_meta_reasoner.py`, `train_grpo.py::_compute_episode_reward`/`load_groups`
(confirmed still genuinely unreachable — only used via `--granularity article`, which no real
training run has ever used).

### 58.1 Signal-strength comparison: `A0` (pre-`C2` production) vs. `C2` (shipped)

Using `model_gate_candidates.py`'s existing `A0_current_cost002` (cost=-0.02, additive
`0.5·ga+0.5·ra` term — literally what `bases_PRE_C2_RAREMOVAL_20260729` contains) against
`C2_soft_ga_pen010` (cost=-0.03, `ra` dropped, `ga` soft-gated — literally what shipped), on the
same 282-section/40-article corpus:

| Metric | Before (`A0`) | After (`C2`) | Change |
|---|---|---|---|
| **TRAIN (171 sections)** | | | |
| Sections hitting `sigma_floor` (`floor%`) | 24.6% | 20.5% | **-4.1pp** |
| Mean top1-vs-top2 margin | 0.0775 | 0.0931 | **+20%** |
| Median margin | 0.0421 | 0.0436 | +3.6% |
| Normalized GRPO advantage (`advNorm`) | 1.108 | 1.206 | **+8.8%** |
| Near-tie rate (2+ arms within 0.06) | 64.3% | 55.6% | **-8.7pp** |
| **Full corpus (282 sections / 40 articles)** | | | |
| Sections hitting `sigma_floor` | 25.6% | 23.4% | -2.2pp |
| Median margin | 0.0376 | 0.0436 | **+16%** |
| Normalized GRPO advantage | 1.121 | 1.197 | **+6.8%** |
| Articles needing a tiebreak (`thin`, TRAIN) | 12/24 | 9/24 | **-3 articles** |
| Articles needing a tiebreak (`thin`, all 40) | 20/40 | 16/40 | **-4 articles** |

Arm distribution held up rather than merely shifting: TRAIN section-level skip/light/standard/deep
went 44/55/39/33 → 43/56/38/34 (deep essentially flat); TRAIN article-level went 5/10/3/6 →
3/11/4/6 (`deep` unchanged at 6). The signal got cleaner — bigger margins, fewer floor-clipped
sections, fewer near-ties, a stronger normalized gradient, ~20% fewer articles landing in the
ambiguous tiebreak zone — **without** trading away `deep`-representation, which was the whole
point of pairing the `ga`-gate redesign with the `cost_coef` revert. Mechanistically this
reproduces §53.6's finding almost exactly: `ga`'s old additive term contributed 26% of total
reward variance for only 2.2% of arm-separating signal — removing that noise source (while
keeping it as a satisficing gate) tightens margins everywhere without hurting decisiveness.

*Caveat:* this uses `model_gate_candidates.py`'s own simplified recompute (matches
`train_grpo.py`'s `sigma_floor`/near-tie logic exactly, but not `compute_article_oracle.py`'s
S3/S4/S5 tiebreak or hard policy/override rules) — so `thin` here is a proxy for tiebreak need,
not identical to the Phase 4 diff above, but it is an apples-to-apples comparison since both `A0`
and `C2` ran through the identical code path.

**Status:** Phases 1-6 complete. Phase 7 (explicit sign-off) was given by the user; Phase 8
(fresh retrain, task-id `run20_c2`, `--inv-freq-temp 0.5` + the unchanged run17-19 recipe) is
in progress. Phase 9 (eval vs. `run15_recalibrated`) is next once a checkpoint is chosen.

## 59. Exploring `cc`/`fl` as soft gates (like `ga`) — modelled and **not recommended**

Motivated by `C2`'s success, the natural follow-up question is whether `gt_base`'s other two
additive terms — `cc` (`ground_truth_core_content`, weight 0.20) and `fl` (`ground_truth_flow`,
weight 0.20) — should receive the same treatment: drop them from the additive sum and replace
them with a flat satisficing-gate penalty, the way `ga` was.

### 59.1 Why `ga` was safe to gate: the arm-neutrality precondition

§54.3 rejected a *hard* `ga` gate but validated a *soft* one specifically because `ga`'s failure
rate was **arm-neutral** — every arm failed at roughly the same rate (skip 29.8%, light 29.8%,
standard 31.2%, deep 30.1%) and, critically, `ga`'s per-arm reward *means* were nearly identical
(all corpus: skip=.702, light=.702, standard=.688, deep=.699 — a 1.4pp spread). That flatness is
what makes gating safe: converting a term that doesn't differentiate arms anyway from "noisy
additive credit" into "a satisficing floor" cannot introduce a new arm bias, because there was no
real signal to lose.

**`cc` and `fl` do not have this property.** Both carry real, non-trivial signal (§53: `cc`
SNR=0.15, `fl` SNR=0.21 — weaker than `de`/`be` (0.71/0.53) but clearly stronger than `ga`'s
0.03), and neither is arm-neutral:

| | skip | light | standard | deep | Direction |
|---|---|---|---|---|---|
| `cc` (ALL, n=282) | 0.901 | 0.894 | 0.883 | 0.879 | declines skip→deep |
| `cc` (TRAIN, n=171) | 0.906 | 0.906 | 0.865 | 0.854 | declines skip→deep (sharper) |
| `cc` (TEST, n=111) | 0.892 | 0.874 | 0.910 | 0.919 | **rises** skip→deep (opposite!) |
| `fl` (ALL, n=282) | 0.652 | 0.716 | 0.720 | 0.720 | rises skip→deep |
| `fl` (TRAIN, n=171) | 0.538 | 0.614 | 0.626 | 0.643 | rises skip→deep |
| `fl` (TEST, n=111) | 0.829 | 0.874 | 0.865 | 0.838 | peaks at light, deep ≈ skip |
| `ga` (ALL, reference) | 0.702 | 0.702 | 0.688 | 0.699 | flat (arm-neutral) |

`cc` is the more concerning of the two: it shows a *real, consistent* decline from skip to deep
on TRAIN (already flagged in §53.6 as "split-unstable" — TRAIN and TEST disagree on direction
entirely), meaning `deep` genuinely has somewhat worse core-content preservation on the training
distribution specifically, for reasons that flip sign on TEST. `fl` shows the opposite pattern —
a real, TRAIN-consistent *advantage* for `deep`/`standard`.

### 59.2 Modelled candidates

Built a small scratch extension of `model_gate_candidates.py` with independent, stackable gates
(unlike `make_candidate`'s single combined gate group, so a `cc` failure and a `ga` failure are
each penalized once, not collapsed into one shared trigger): `K1` gates `cc` only, `K2` gates `fl`
only, `K3` gates both — all at the same threshold/penalty convention as `C2` (`< 0.5` → `-0.10`),
with the freed weight folded into `de`/`be` at `C2`'s established 60:40 split, against the shipped
`C2` baseline.

| candidate | TRAIN floor% | TRAIN medMrg | TRAIN advNorm | TRAIN nearTie | TRAIN deep (sec/art) | ALL thin |
|---|---|---|---|---|---|---|
| `C2` (shipped) | 20.5% | 0.0436 | 1.203 | 56.1% | 34 / 6 | 16 |
| `K1` (gate `cc`) | 18.7% | 0.0564 | 1.234 | 50.9% | 38 / 7 | 15 |
| `K2` (gate `fl`) | 19.3% | 0.0564 | 1.245 | 51.5% | 38 / 7 | **19 (worse)** |
| `K3` (gate both) | 17.5% | 0.0581 | 1.261 | 50.9% | 40 / **10** | 15 |

At face value every aggregate metric improves, and `deep`'s representation grows substantially
(TRAIN article-level `deep` nearly doubles, 6→10, under `K3`). This is the *same shape* of result
that made the hard `ga` gate look attractive before §54.3 found the arm-bias mechanism underneath
it — so the improvement was **not taken at face value**.

### 59.3 Why the improvement is not trustworthy, on inspection

1. **The arm-neutrality precondition fails.** Because `cc` declines toward `deep` on TRAIN, the
   old additive term was *correctly* charging `deep` a real (if modest) cost for its typically
   worse core-content preservation. A flat gate penalty of 0.10 is **smaller** than the 0.20
   additive weight it replaces — so whenever the gate does fire, it charges roughly half what the
   proportional term used to. Working through the arithmetic (`cc` ALL-corpus mean for `deep` =
   0.879 ⇒ ~12.1% expected zero-rate if scores are binary): expected additive cost ≈
   `0.20 × 0.121 = 0.0242`; expected gate cost ≈ `0.10 × 0.121 = 0.0121` — the gate mechanically
   halves `deep`'s real, non-noise penalty. That is not "removing noise", it is quietly cutting
   `deep`'s true cost in half with no independent justification that 0.10 (`ga`'s calibrated
   value) is the correct exchange rate for `cc`.
2. **`cc`'s sign instability makes any single gate direction unjustifiable.** A TRAIN-favoring
   design (gate charges `deep` less) is directly contradicted by TEST, where `cc` rises toward
   `deep` — the "right" gate behavior is genuinely ambiguous, unlike `ga` where the flatness meant
   the gate's exact calibration barely mattered.
3. **The design confounds gating with reweighting.** Both `cc` and `fl`'s freed weight was folded
   into `de`/`be` (matching `C2`'s own convention) — and `de` in particular already differentiates
   *strongly* toward `deep` (§53: `armSprd`=0.196, the largest of any metric). Handing `de`/`be`
   *more* weight independently pushes toward `deep`, regardless of what happens to `cc`/`fl`'s own
   gate. This is the same lever (`explore_mult`-style reweighting) that §35/§36 already found
   **overturns confirmed-correct labels** when pushed too far — so part of `K1`-`K3`'s apparent
   improvement is plausibly just re-running that already-cautioned-against lever, not evidence
   that gating `cc`/`fl` specifically is sound.
4. **The full-corpus check contradicts the TRAIN-only story.** `K2` (gate `fl` only) *regresses*
   the full-40-article `thin`-article count (16→19) even though it improves every TRAIN-only
   metric — the same kind of view-dependent inconsistency that has caught bad candidates
   elsewhere in this investigation (§35's cross-article-agreement trap, §54.8's structural
   false-positive gate rejection).

### 59.4 Recommendation

**Do not gate `cc` or `fl`.** Both carry real (if modest) signal that the current additive
formula is using correctly and proportionally — the precondition that made `ga`'s gate safe
(arm-neutral, ~97%-noise signal) does not hold for either metric. `cc`'s TRAIN/TEST sign
instability (already flagged in §53.6) is a genuine open question, but the fix for a
sign-unstable metric is to understand *why* it flips (the way the `golden_local` investigation in
Part 2 §8 dug into a mechanism rather than gating the symptom away), not to convert it into a
threshold check with an arbitrary, unvalidated exchange rate. If `deep`'s representation is
believed to be still too low after `C2`'s retrain results come in, the correct next lever is a
fresh, independently-calibrated investigation of `cost_coef` or `de`/`be` weighting on its own
merits — not reusing `ga`'s gate mechanism on metrics that don't share `ga`'s defining property.

## 59.5 Part 7 re-run on N=3-replicated TRAIN data (2026-08-17) — do the choices hold up?

Part 7's entire analysis (§52–59) was built from single-draw (N=1) production `reasoning.json`
data. All 24 TRAIN articles now have N=3 draws (1 production + 2 real temperature=0.7 replicates,
per Appendix A.13). This section re-derives §53's metric-differentiation indices and §54/§54.6/
§54.7/§58.1's gate-candidate comparisons on the averaged data, to check whether the design choices
(soft-gate `ga` at penalty 0.10, drop `ra`, keep `cc`/`fl` additive/ungated, `cost_coef=-0.03`)
still hold. **Nothing here touches actual GRPO training-run results** (entropy, checkpoints, TEST
eval accuracy) — this is purely a re-derivation of Part 7's zero-cost reward-signal diagnostics.

**New tool**: `research_agent_local/training/reanalyze_part7_averaged.py`. Read-only, zero LLM
calls. Loads production + both replicate `reasoning.json` files for each of the 24 TRAIN articles'
4 arms, computes each (section, arm, dimension) scalar per draw exactly as
`model_gate_candidates.load_corpus()` does (raw `_get_score()`, or `enhancement_credit()` for
`de`/`be`), then **simple-averages the scalars across the 3 draws** before handing the corpus to
`model_gate_candidates.evaluate()` — so every Part 7 candidate formula (`A1`/`B`/`C1`/`C2`/`C3`/
`D`/`E`/`F`, the `H`-series `cost_coef` sweep) is re-scored using the *exact same formula code*, no
duplication. TEST articles pass through single-draw/unchanged (their replication is a separate,
still-in-progress track).

**Important methodological caveat, stated up front**: this averages RAW per-dimension inputs, then
applies each candidate's formula (including gate checks) *once* to the averaged values. This is a
*different* aggregation order than what `merge_replicate_oracles.py`/Appendix A.13 actually do for
any real future retrain — they compute the *full formula* (including the `ga` gate check)
separately per draw, then average the 3 resulting *final rewards*. For a linear weighted sum the
two orders are equivalent; for a nonlinear step-function gate (`ga < 0.5`) they are not (averaging
`ga`'s raw {0,1} values first can produce fractional values like 0.33/0.67 that the gate check then
rounds through a single threshold, rather than letting 3 independent per-draw gate decisions
combine). This tool is therefore the right instrument for asking "do the metrics' underlying
*differentiation properties* (armSprd, arm-neutrality, signal share) survive averaging" — not for
predicting exactly what a real `--use-averaged-oracle` retrain's gate behavior would be.

### 59.5.1 Gate-candidate comparison (§54.2/§54.6/§54.7 re-run), TRAIN, averaged vs. single-draw

| candidate | floor% (N=1 → N=3) | nearTie (N=1 → N=3) | advNorm (N=1 → N=3) | medMrg (N=1 → N=3) | ALL thin (N=1 → N=3) | corpus deep (N=1 → N=3) |
|---|---|---|---|---|---|---|
| `A1` (cost -0.03) | 22.9% → 29.3% | 61.2% → 65.9% | 1.144 → 1.196 | 0.0392 → 0.0455 | 21 → 25 | 7 → 5 |
| `B` (drop `ra`) | 19.3% → 29.7% | 57.9% → 59.4% | 1.175 → 1.220 | 0.0424 → 0.0499 | — → 25 | — → 9 |
| `C1` (soft `ga`, 0.05) | 23.1% → 24.7% | 56.8% → 60.5% | 1.200 → 1.209 | 0.0393 → 0.0403 | 17 → 21 | 9 → 8 |
| **`C2` (soft `ga`, 0.10, shipped)** | 20.5% → **23.5%** | 55.6% → 61.4% | 1.206 → 1.207 | 0.0436 → 0.0410 | **16 → 19** | **11 → 10** |
| `C3` (soft `ga`, 0.15) | **17.5% → 18.0%** | **52.6% → 59.9%** | 1.203 → 1.216 | 0.0403 → 0.0403 | 19 → 22 | 10 → 9 |
| `G` (pure drop `ga`) | 22.8% → 29.9% | 59.6% → 65.9% | 1.187 → 1.184 | — → 0.0367 | 16 → 20 | 9 → 8 |
| `D` (hard `ga`) | 23.4% → **49.7%** | 56.1% → **70.8%** | 1.172 → 1.147 | 0.0393 → 0.0300 | 13 → **9** | 6 → **9** |
| `E` (hard trio, drop `ga`) | 22.2% → 28.7% | 59.6% → 65.9% | 1.178 → 1.169 | 0.0383 → 0.0367 | 18 → 20 | — → 10 |
| `F` (hard trio, drop `ga`+`cc`) | 24.0% → 31.2% | 55.0% → 62.9% | 1.210 → 1.179 | 0.0445 → 0.0346 | 15 → 15 | — → 10 |

**What holds up:**
- **`C2` remains the best-justified all-round candidate.** It still has the fewest ALL-corpus
  thin-margin articles among the soft-gate family (19, vs. `C1`'s 21 and `C3`'s 22) — the *exact
  same relative ordering* §54.6 found on single-draw data (`C2` 16 < `C3` 19 < `C1` 17 there too,
  modulo the absolute-count shift documented below). `C3` again posts the best raw `floor%`/
  `nearTie` (as it did originally) but again costs more thin articles — §54.6's "returns past 0.10
  trade section-level gains for article-level cost" finding reproduces almost exactly.
- **`ga`'s arm-neutrality — the precondition the whole soft-gate design rests on — holds.** See
  §59.5.3; this is the single most important thing to have survived, since C2/C1/C3/D/E/F all
  depend on it.
- **`cost_coef=-0.03` is still where `deep` recovers.** See §59.5.2 — the qualitative relationship
  (deep-scarcity worsens as `cost_coef` goes more negative, recovers by `-0.03`) is intact.
- **Hard gates (`D`) remain disqualified — but via a different, still-decisive route.** `D`'s
  `floor%` (49.7%) and `nearTie` (70.8%) are catastrophically worse than every other candidate on
  averaged data, roughly double `D`'s already-bad single-draw numbers — the rejection is, if
  anything, *more* clear-cut now.

**What moved, worth flagging honestly:**
- **Every candidate's `floor%`/`nearTie` rose under averaging, not fell** (e.g. `A1` 22.9%→29.3%,
  `C2` 20.5%→23.5%). This is *directionally consistent* with A.14.1's own already-documented
  finding for the shipped `C2` formula specifically (floored-rate 21.1%→26.7%, near-tie 55.0%→
  58.5%, post-correction) — averaging clarifies the *typical* section (median margin/normAdv both
  still rise too, e.g. `A1` medMrg 0.0392→0.0455, advNorm 1.144→1.196) while flattening some
  sections that looked separated only by single-draw luck. Same mechanism, reproduced here at the
  gate-candidate level, not just the shipped-formula level.
- **`D`'s specific deep-collapse *mechanism* (§54.3) does not reproduce as cleanly.** On
  single-draw data `D`'s corpus `deep` fell to 6 (below `A1`'s 7). On averaged data `D`'s corpus
  `deep` is 9, *above* the averaged `A1` baseline's own 5 — `A1` itself lost deep-representation
  under averaging (7→5) independent of any gate. `D` is still unambiguously rejected (its
  floor%/nearTie are disqualifying on their own), but the *specific* "hard gate asymmetrically
  destroys deep's explore credit" story from §54.3 is not the reason anymore on this data — a
  genuine, honestly-reported divergence, not swept under the rug.
- **Absolute thin-article and corpus-deep counts shifted (mostly downward for deep) across nearly
  every candidate**, `A1` itself included — this reflects real changes in the underlying averaged
  section rewards, not a candidate-specific effect. Any future retrain using averaged labels should
  expect somewhat different absolute deep-representation than the single-draw-era numbers this
  document has cited throughout, even before any formula choice is factored in.

### 59.5.2 `cost_coef` sweep under `C2` (§54.7 re-run)

| `cost_coef` | floor% (N=1 → N=3) | advNorm (N=1 → N=3) | corpus `deep` (N=1 → N=3) | ALL thin (N=1 → N=3) |
|---|---|---|---|---|
| -0.06 | 8.2% → 21.3% | 1.266 → 1.219 | 3 → 2 | 10 → 16 |
| -0.045 | 21.1% → 25.1% | 1.258 → 1.218 | 4 → 4 | 19 → 23 |
| **-0.03** | 20.5% → 23.5% | 1.206 → 1.207 | **11 → 10** | 16 → 19 |
| -0.02 | 20.5% → 24.3% | 1.166 → 1.188 | 13 → 12 | 18 → 21 |

**The qualitative recommendation survives: `-0.03` is still the point where `deep` recovers to a
healthy count while retaining `C2`'s signal-quality gains.** `-0.06`/`-0.045` still leave `deep`
scarce (2-4 articles) on averaged data just as they did on single-draw (3-4). **But the sharp
"floor% cliff" between `-0.06` and `-0.045`** that motivated calling `-0.045` a bad
"worst-of-both-worlds" midpoint in the later §61 cost_coef investigation **is much weaker here**:
single-draw showed an 8.2%→21.1% jump (2.6×) between `-0.06` and `-0.045`; averaged shows
21.3%→25.1%, a difference of only ~4pp. This doesn't change the `cost_coef=-0.03` decision (which
was driven by `deep`-representation, not the floor% cliff specifically), but the cliff-shaped
evidence behind the later, separate `-0.045`-vs`-0.05` sharpness-cliff finding (§61 Stage 1
addendum) should be treated as a single-draw-specific observation, not necessarily one that would
reproduce if that sweep were re-run on averaged data.

### 59.5.3 `A0` vs. `C2` signal-strength comparison (§58.1 re-run)

| Metric (TRAIN) | `A0` (N=1 → N=3) | `C2` (N=1 → N=3) | `C2` advantage, N=1 | `C2` advantage, N=3 |
|---|---|---|---|---|
| `floor%` | 24.6% → 33.9% | 20.5% → 23.5% | -4.1pp | **-10.4pp** |
| Near-tie rate | 64.3% → 68.5% | 55.6% → 61.4% | -8.7pp | -7.1pp |
| Normalized advantage | 1.108 → 1.172 | 1.206 → 1.207 | +8.8% | +3.0% |
| Median margin | 0.0421 → 0.0412 | 0.0436 → 0.0410 | +3.6% | **-0.5%** |

**`C2` still beats `A0` on 3 of 4 headline metrics on averaged data, on `floor%` by an even wider
margin than on single-draw** — the core §58.1 "shipped `C2` is a real signal-quality improvement"
finding is reinforced, not just preserved. **The one metric that weakens to a wash is median
margin** (`C2`'s +3.6% single-draw advantage becomes essentially flat, -0.5%, on averaged data) —
both `A0` and `C2`'s median margins move in slightly different ways under averaging than their
means/floor%/near-tie do (the same mean-vs-median dissociation A.14.1 already documented), so this
specific sub-claim should be considered weakened, while the other three (larger, more
decision-relevant) metrics hold or strengthen.

### 59.5.4 Metric-differentiation indices (§53 re-run), TRAIN

| metric | armSprd (N=1 → N=3) | %const (N=1 → N=3) | monoUp (N=1 → N=3) | SNR (N=1 → N=3, full-corpus N=1 ref.) | arm-mean shape (N=3) |
|---|---|---|---|---|---|
| `de` | 0.1943 → 0.1745 | 43.9% → 29.2% | 46.9% → 37.2% | (0.71) → 0.72 | skip 0.000 < light≈std 0.13 < deep 0.175 — still the top signal source |
| `be` | 0.0812 → 0.0832 | 57.3% → 42.7% | 30.1% → 24.5% | (0.53) → 0.65 | skip 0 < light 0.060 < deep 0.064 < **std 0.083** — non-monotone peak-at-standard shape reproduces exactly |
| `fl` | 0.1053 → **0.0448** | 56.7% → 48.5% | 43.2% → 26.1% | (0.21) → 0.20 | now peaks at light (0.684), flat/slightly down through deep (0.676) — was monotone-increasing on N=1 |
| `cc` | 0.0526 → **0.0253** | 80.7% → 60.8% | 15.2% → 16.4% | (0.15) → 0.15 | skip≈light 0.782 > std 0.756 < deep 0.778 — the TRAIN "declines toward deep" shape (§53.6/F4) weakens substantially |
| `ga` | 0.0234 → 0.0273 | 53.8% → 25.1% | 22.8% → 17.2% | (0.03) → 0.08 | **still flat** (0.39-0.42 across all 4 arms) — arm-neutrality holds |
| `ra` | 0.0117 → 0.0136 | 95.9% → 88.9% | 14.3% → 31.6% | — → 0.30 | still ≥88% constant — safe-to-drop conclusion holds |
| `cp` | 0.0058 → 0.0039 | 99.4% → 98.2% | 0.0% → 0.0% | — → 0.67 | still ≥98% constant — unchanged multiplicative-gate role holds |
| `gsp` | 0.0117 → 0.0195 | 97.7% → 87.7% | 25.0% → 52.4% | — → 0.37 | still ≥87% constant — zero-weight decision holds |

**What holds firmly**: `de` remains the dominant, cleanest signal source (largest `armSprd`, `SNR`
≈0.7-0.72 both ways) with `deep` clearly highest. `be`'s distinctive non-monotone "peaks at
`standard`, falls at `deep`" shape — the "third round adds depth not breadth" finding — reproduces
almost exactly. **`ga`'s arm-neutrality (flat means across all 4 arms) is the load-bearing property
for the whole soft-gate design, and it survives averaging intact** — this is the single most
important confirmation in this whole re-analysis. `ra`/`cp`/`gsp` all remain safely
near-constant, supporting their unchanged treatment (drop / keep-as-multiplicative-gate /
zero-weight respectively).

**What weakens or surfaces as new, worth flagging honestly:**
- **`fl` and `cc`'s already-modest signal weakens further under averaging** (`fl` `armSprd`
  0.1053→0.0448, more than halved; `cc` 0.0526→0.0253, also more than halved). `cc`'s specific
  "declines toward `deep` on TRAIN" shape (§53.6/F4, already flagged as split-unstable against
  TEST) is *considerably* less pronounced on averaged TRAIN data — this further **reinforces**,
  not undermines, §59's decision not to gate `cc`: if anything, the original TRAIN-vs-TEST
  sign-instability finding looks even more like it was partly single-draw noise, strengthening the
  case that gating `cc` on any single-draw-derived exchange rate would have been unjustified.
- **`ga`'s absolute mean dropped sharply (TRAIN 0.740→0.412)** even though its arm-neutral *shape*
  held. Sanity-checked directly against raw per-section values (not a parsing artifact — e.g.
  `06_tools__var_standard`/light: production 4/9 sections pass, replicate1 3/9, replicate2 3/9,
  genuinely different pass/fail patterns per draw, all read via the same code path). Plausible
  mechanism, consistent with §53.6/F2's already-established finding that `ga`'s real failure mode
  is missing mandated visual elements (a writing-workflow property): whether a given independent
  draft happens to include every mandated visual element seems to vary substantially draft-to-draft,
  so `ga` carries more *cross-draft* noise than most other dimensions, on top of its already-known
  large *cross-section* noise. **Practical implication, not yet acted on**: the shipped gate's
  `0.5` threshold was calibrated against single-draw `ga`'s ~70-74% typical pass rate; if a future
  retrain ever gates on an *averaged* `ga` value directly (rather than the per-draw-gate-then-
  average-final-reward order `merge_replicate_oracles.py` actually uses), `0.5` may need
  re-calibrating against this lower baseline. Not urgent — the real merge-back path doesn't average
  raw `ga` before gating, so shipped behavior is unaffected — but worth remembering if this
  aggregation order is ever used for something other than diagnostics.

### 59.5.5 Overall verdict

**Every major Part 7 decision is reinforced, not overturned, by re-running on N=3-replicated TRAIN
data**: `C2` (soft `ga` gate, penalty 0.10) remains the best all-round candidate by the same
relative margins that justified it originally; `cost_coef=-0.03` remains the point where `deep`
recovers; dropping `ra` remains safe; not gating `cc`/`fl` remains correct (more so, if anything,
given `cc`'s weakened signal under averaging); hard gates remain disqualified. **Two findings are
genuinely new and worth carrying forward**: (1) `D`'s specific deep-collapse *mechanism* doesn't
reproduce identically, though its overall rejection still holds on stronger grounds; (2) `ga`'s
absolute pass rate is markedly lower and noisier across independent drafts than single-draw data
suggested, a data point for any future work on `ga`'s calibration, though it does not affect
anything already shipped.

## 60. `run20_c2` post-mortem: severe entropy collapse, and why `run13_formulaB` was so much better

`run20_c2` (`C2`, `cost_coef=-0.03`, task-id `run20_c2`, entropy-coef 0.22 — the unchanged
run17-19 recipe) was evaluated at its `best_strict` checkpoint (epoch 95) and produced a
catastrophic result, prompting a full diagnosis.

### 60.1 The result

From `grok_planner_test_results/_summary.json`:

| Split | exact | near | miss | MAE | chosen preset dist | oracle dist |
|---|---|---|---|---|---|---|
| TRAIN (24) | 11 | 8 | 5 | 0.875 | {light:10, standard:5, **deep:9**} | {skip:8, light:8, standard:4, deep:4} |
| TEST (16) | **1** | 5 | **10** | **1.688** | {light:3, **deep:13**} | {skip:2, light:6, standard:5, deep:3} |

TEST predicted `deep` for 13 of 16 articles and `skip` for **zero** articles on either split
(despite 10 combined skip-oracle labels across TRAIN+TEST) — a degenerate, near-constant policy,
not a genuine per-input generalization failure.

### 60.2 Root cause: entropy collapsed far earlier than any prior run

Full `training_log.jsonl` trajectory:

```
ep 0-20:  entropy 0.18-0.42  (healthy, exploring)
ep 30:    entropy 0.030      <- already collapsed
ep 40-99: entropy 0.007-0.03 (stays collapsed for the remaining 70 epochs)
peak strict_top1_accuracy: 0.5848 at epoch 95
```

Entropy collapsed by **epoch 30** — far earlier than `run13_formulaB`'s ~epoch 80 or
`run14_phase0`'s ~epoch 97, under the *identical* `--entropy-coef 0.22`/`--beta 0.15`. Worse,
`strict_top1_accuracy` kept slowly climbing through the entire collapsed regime (0.42→0.58 from
epoch 30 to 95), so `--patience 50` never fired — patience tracks a train-set metric that looks
like it's still improving even as the policy degenerates into a near-constant output, the same
"train metric ≠ generalization signal" trap already documented for `run14_phase0`.
`train_grpo.py`'s `load_section_groups()` was checked and confirmed to only read the `"rewards"`
key from `section_oracle.json` — the new `C2` `"diagnostics"` field (§58) is safely ignored, so
this is not a code regression from that change. `best_strict_epochs/` contains only
`epoch_0095` (strict accuracy climbed monotonically, never tying an earlier epoch), so there is
no earlier, pre-collapse checkpoint available to fall back to.

### 60.3 Confirming the historical comparison: `run13_formulaB` really was this much better

`run13_formulaB` (`cost_coef=-0.06`, Formula B, trained *before* `G0`/`J0`/`H0`/`EPS_BAND`/
I-series/`C2` existed — all landed 2026-07-13 through 2026-07-29, after this run):
- **TRAIN**: strict_top1 peaked **0.848** at epoch 84, near-tie top1 peaked **0.947** at epoch 90.
- **TEST**: RL-only exact 7-10/16 (44-62%), **0 misses**, MAE 0.375-0.562. Full RL+Grok pipeline:
  exact=10/16 (62%), miss=0, MAE=0.375, regret_mean=0.0384.

This confirms the recollection precisely and the gap to `run20_c2` (TEST exact=1/16, miss=10/16,
MAE=1.688) is real and severe, not exaggerated.

### 60.4 Causes — several confounded factors, `cost_coef` is real but secondary

1. **Entropy-collapse timing/severity is the primary, most direct cause.** `run13`'s peak
   checkpoint (epoch 84) was captured *before* entropy fully bottomed out — still a genuinely
   differentiated policy. `run20_c2` collapsed by epoch 30 and never recovered; its "best"
   checkpoint (epoch 95) is deep inside the collapsed regime. Same hyperparameters both runs — the
   difference is *when* collapse happened, not whether the regularizer existed.
2. **Why collapse got so much earlier — originally hypothesized as "the reward signal got
   stronger", but this claim did NOT survive checking against the true original formula (see
   §60.6 correction below).** The initial version of this section cited §58.1's `A0` vs `C2`
   comparison as evidence — but `A0` is only the *immediately preceding* formula state (already
   including `H0`, `G0`, `J0`, and four `cost_coef` reductions), not what actually trained `run13`.
   Directly compared against the true original Formula B (§60.6), `C2` is measurably **less**
   decisive by these same aggregate metrics, not more — so this specific mechanism is retracted.
   The real cause of the collapse-timing difference is not yet established; see §60.6 for the
   corrected, more honest accounting.
3. **Digest-pipeline evolution — a real, independently-already-quantified factor.** Between
   `run13` and now, the digest pipeline changed materially (Phase 0's anchor-hygiene filter,
   temp=0 fixes, `golden_local` fix, policy majority-vote — landed 2026-07-11, after `run13`).
   §14.3's decisive attribution eval already showed that taking `run13_formulaB/best` **unchanged**
   and re-evaluating on the new Phase-0 digests alone regressed TEST from exact=10/miss=0/
   MAE=0.375 to exact=10/near=3/**miss=3**/MAE=0.625 — zero retraining involved. Part of the gap
   is baked into digest evolution, independent of training or `cost_coef`.
4. **Oracle-label drift — minor, not apples-to-apples.** TEST ground-truth labels themselves
   shifted across `G0`/`J0`/`H0`/`EPS_BAND`/staged `cost_coef`/`C2` (each individually validated as
   thin-margin-only). Smaller effect than 1-3, but `run13`'s TEST score isn't measured against an
   identical target.
5. **`cost_coef` itself shapes *which* degenerate output, not *whether* collapse happens.**
   `-0.03`'s corpus deep-count (11) vs. `-0.06`'s (3, §54.7/§59 sweep) plausibly explains why this
   run's collapse specifically converged to "always deep" rather than "always cheap" (`run12`'s
   old failure mode). But `-0.06` actually has the *highest* `advNorm` (1.266) of any `cost_coef`
   value under `C2` — so reverting `cost_coef` would not obviously prevent collapse, only
   relocate it to a different constant output.

### 60.5 Interpretation and next step

Reverting to Formula B / `cost_coef=-0.06` is not recommended: its good TEST result was likely a
side effect of a *weaker* signal buying more pre-collapse epochs, not evidence of a fundamentally
more stable training setup, and it reintroduces the severe deep-scarcity problem this whole
investigation spent weeks fixing. The cleaner interpretation is that `entropy_coef=0.22` needs to
be recalibrated upward to match the genuinely-improved signal strength, not that the signal
improvements should be undone. `run21_ecoef035` (`--entropy-coef 0.35`, everything else
unchanged from `run20_c2`, fresh task-id) was launched to test this directly — the key thing to
watch is whether `mean_entropy` stays meaningfully above the ~0.01-0.03 collapsed range well past
epoch 30 this time, before trusting any checkpoint's train-set accuracy.

### 60.6 Correction (2026-07-30): the "signal got stronger" claim does not hold against the true original Formula B

**User challenge:** §60.4 point 2 cited §58.1's `A0` vs `C2` comparison as evidence the reward
signal "genuinely got stronger over time" — but `A0` (cost=-0.02, the state immediately
preceding `C2`) already includes `H0`'s empirical cost units, `G0`/`J0`'s enhancement-curve
fixes, and three prior `cost_coef` reductions. None of that existed when `run13_formulaB`
actually trained. The comparison needed is `C2` vs. the *true* original Formula B, not `C2` vs.
its immediate predecessor.

**Found the real data to check this directly.** `rl_training_data/bases_ORACLE_BACKUP_20260708_231117/`
(taken the moment Formula B first shipped, per the Part-1 shipping log) is `section_oracle.json`
version 2 — no `"explore"` field (pre-candidate-E, §39), raw-binary `de`/`be` (pre-enhancement-tag,
§25-29), `cost_coef=-0.06` with ordinal `nr` units (pre-H0). This is, as directly as the repo's
surviving artifacts allow, exactly what `run13_formulaB` trained on. Recomputed the same
signal-quality metrics (`train_grpo.py`'s own `sigma_floor`/near-tie/`advNorm` logic,
target-words-weighted article aggregation, `EPS_BAND` thin-article check) directly from this
backup's already-computed `rewards` — no reformula needed, since v2's `rewards` dict already *is*
the historical Formula-B output.

| | True original Formula B (2026-07-08) | `C2` (shipped) | Direction |
|---|---|---|---|
| **TRAIN (171 sections)** | | | |
| `floor%` | **7.0%** | 20.5% | original is *cleaner* |
| Mean margin | **0.1171** | 0.0931 | original is *bigger* |
| Median margin | **0.0500** | 0.0436 | original is *bigger* |
| `advNorm` | **1.230** | 1.206 | original is *stronger* |
| Near-tie rate | 56.1% | 55.6% | ~equal |
| TRAIN article dist (sk/li/st/dp) | 8/10/**3**/**3** | 3/11/4/**6** | original is severely `deep`-scarce |
| **Full corpus (282 sections / 40 articles)** | | | |
| `floor%` | **6.0%** | 23.4% | original is *cleaner* |
| Median margin | **0.0500** | 0.0436 | original is *bigger* |
| `advNorm` | **1.251** | 1.197 | original is *stronger* |
| ALL article dist (sk/li/st/dp) | 11/19/**5**/**5** | 4/18/7/**11** | original is severely `deep`-scarce |

**This is the opposite of the §60.4 point 2 claim.** Directly compared — not via a proxy
comparison against an intermediate state — the true original Formula B is *more* decisive on
every aggregate signal-quality metric than `C2`, on TRAIN specifically (what GRPO actually
trains on) as well as the full corpus. **The specific mechanism proposed in §60.4 point 2
("signal got stronger ⇒ faster collapse") is retracted** — it is not supported by the direct
comparison, and if anything predicts the wrong direction (a *more* decisive original signal
should, by that same logic, have collapsed faster or as fast, not slower).

**Why the original formula's aggregate numbers look better — a plausible, not yet confirmed,
reconciliation.** This finding does not contradict the rest of this investigation; it's
consistent with two already-documented, independently-diagnosed problems with the original
formula that were never framed in these particular aggregate terms before:
1. **`cost_coef=-0.06` with ordinal units spans a much wider mechanical range** than today's
   `-0.03` with H0's empirical units (max cost spread `0.18` vs. `0.069`, §52.1-52.2) — a bigger,
   blunter cost term mechanically creates bigger, "cleaner"-looking margins between cheap and
   expensive arms, independent of whether the *content* signal underneath is well-calibrated.
   `analyze_cost_imbalance.py` already found this exact term explained ~93% of `deep`'s average
   shortfall at `-0.06` — a large fraction of the original formula's "decisiveness" is this one
   mechanical term, not genuine content differentiation.
2. **Raw-binary `de`/`be` is a coarser, bigger-jump signal than the saturating `enhancement_credit()`
   curve** — a 0→1 flip is a bigger, more "decisive"-looking swing than a smooth 0.35→0.80
   transition, even though the pairwise-grading investigation (Part 6, p=0.031 across two
   independent 12+6-article samples) found the binary version specifically *overstates* the true
   content-quality gap at exactly this tier boundary. Coarser is not the same as more correct.

   Both of these mean the original formula's superior `floor%`/margin/`advNorm` numbers are
   plausibly an artifact of two mechanisms *this investigation itself later diagnosed as
   miscalibrated* (H0's cost-unit fix, the pairwise-grading tier-1 fix) — not evidence the
   original reward signal was more *correct*. The near-total `deep` scarcity in the original
   distribution (3-5 articles out of 40, matching the historical "skip≈8/light≈11/standard≈3/
   deep≈2" complaint that motivated the entire H0/G0/J0/`cost_coef` arc) is the direct cost of
   that same bluntness. **This reconciliation is plausible but not independently verified** —
   it explains why the numbers could look this way without contradicting anything else in this
   document, but it has not been tested as rigorously as the rest of this investigation's claims.

**What this means for the actual open question.** §60's core findings about `run20_c2`/
`run21_ecoef035` themselves are unaffected — the entropy-collapse timing, the `patience`
blind spot, and the recommendation against reverting `cost_coef` (§54.7's sweep already showed
`-0.06` has the *highest* `advNorm` of any tested value, so reverting wouldn't prevent collapse
regardless of this correction) all stand on their own directly-observed merits. What changes is
the **explanation** for why collapse happens so much earlier now than in `run13`. That is now
honestly unresolved. Candidate factors, none confirmed: (a) the digest-pipeline refresh between
`run13` and every later run (Phase 0, §14.3) — already independently proven to change held-out
behaviour with zero retraining, a stronger prior than the retracted signal-strength story; (b)
the underlying grading judge/pipeline changed (`run13`'s original Gemini binary grades vs.
today's Claude + tag-instrumented re-grade, §37), a different source of section-level noise
characteristics than either compared formula's *shape*; (c) genuine run-to-run stochastic
training variance — collapse-epoch claims rest on `n=1` run per configuration, a weak sample for
any deterministic causal story. Resolving this would need a dedicated, controlled comparison
(e.g. retraining on `C2` reward *values* but `run13`-era digests, or vice versa) — not attempted
here; the practical recommendation (try `entropy_coef` first, keep `cost_coef` where it is)
is unchanged since it does not depend on which of these explanations turns out to be right.

### 60.7 `run22_reg_combo` post-mortem (2026-07-31): third consecutive collapse, flat returns from the entropy_coef/grad-clip lever, and the new safety net's first real save

`run22_reg_combo` (`--entropy-coef 0.6 --max-grad-norm 0.1 --warmup-epochs 20`, otherwise the same
recipe) was checked at epoch 83/200 (still running). Full trajectory read from `training_log.jsonl`.

**Entropy collapsed again.** Peaked 0.50 (epoch 14), oscillated 0.14–0.42 through epoch 29, then
crashed epoch 30→38 (0.122→0.022) and has stayed pinned in the 0.005–0.05 range for the ~50
epochs since, with zero recovery — the identical shape as `run20_c2`/`run21_ecoef035`.

**Collapse-onset timing across all 3 runs shows flat, not improving, returns:**

| run | `entropy_coef` | extra regularization | entropy at epoch 30 | epoch entropy first `<0.03` |
|---|---|---|---|---|
| `run20_c2` | 0.22 | none | collapsed | ~epoch 30 |
| `run21_ecoef035` | 0.35 | none | 0.0662 | ~epoch 32 |
| `run22_reg_combo` | 0.60 | `max_grad_norm=0.1`, `warmup=20` | 0.1223 | ~epoch 37–38 |

Nearly tripling `entropy_coef` (0.22→0.6) plus adding gradient clipping and doubling warmup bought
only ~5–8 more epochs before full collapse. This is a flat curve, not a dose-response still
climbing — three consecutive escalations on this exact lever have now failed the same way, strong
evidence it is exhausted rather than under-tuned.

**`strict_top1_accuracy`/`top1_accuracy` (near-tie-tolerant, confirmed via
`top1_correct = top1 in group.acceptable_idxs`) both climb continuously through the entire
collapsed regime** — strict 0.42→0.55 and near-tie 0.63→0.80 from epoch 37 to 83, while entropy
sits at ~0.01–0.03 the whole time. Exactly the illusory-progress pattern §60.2 first flagged.

**The new `best_strict_healthy` tracker (built after `run21`, §-prior entry) is validated in
practice — its first real save.** It stopped updating at epoch 28, the last epoch where entropy
was still ≥ the 0.15 healthy floor, and has correctly refused to certify anything since:

| tracker | value | epoch | entropy there | trustworthy? |
|---|---|---|---|---|
| `best_strict_healthy_top1` | **0.281** | 28 | 0.186 (healthy) | **yes** |
| `best_strict_top1` | 0.573 | 75 | ~0.03 (collapsed) | no |
| `best_neartie_top1` | 0.801 | 83 | ~0.01 (collapsed) | no |

This ~2–2.8x gap is exactly the "still suboptimal" signal: the 55%/80% numbers the untethered
trackers report are an artifact of a near-deterministic policy re-confirming its own memorized
argmax on the training groups it was fit to, not genuine competence. The only currently-trustworthy
number across all 3 runs so far is **28.1%** — barely above a 25% random-4-arm baseline, meaning no
run has yet demonstrated real generalizable competence before collapsing.

**`sigma_floor_fraction` is flat at exactly 0.2222 across every logged epoch** — reconfirms (as
expected, since labels are frozen and never touched by training) that this is a static property of
the label set, not something drifting with the collapse. Ruled out as a collapse-timing mechanism.

**Recommendation: stop escalating `entropy_coef`/grad-clip/warmup as the primary lever.** Three
consecutive attempts spanning `entropy_coef` 0.22→0.35→0.6 (the last combined with grad clipping
and longer warmup) show diminishing-to-flat returns on collapse timing, all via the identical
never-recovers mechanism. Given §19's established mechanism (frozen, never-resampled reward
labels — noisy labels get memorized, not averaged away) and §55.3's finding that a large fraction
of the corpus's reward margins are statistically indistinguishable from noise, the more promising
untested lever is Appendix A's already-planned label-noise reduction (A.10 steps 2–4: real
temperature-0.7 replication → the now-built merge-back script → retrain on averaged labels). This
is mechanistically plausible as a fix for collapse too, not just for label quality: if a handful of
noisy/extreme-margin groups are driving disproportionately large policy-gradient updates each
epoch, cleaning up those labels could reduce collapse pressure directly, rather than only
delaying or safety-netting around it. Not yet confirmed — would need the retrain in step 4 to test.

### 60.8 Free diagnostic on `run22`'s existing log (2026-07-31) + candidate experiment list before committing to replication

Before spending on the noise-reduction plan, re-examined `run22`'s already-collected
`training_log.jsonl` per-group data (killed at the user's decision after §60.7) to check whether
collapse is concentrated in a few noisy/near-tie groups (which would argue replication alone might
fix it) or broad-based across most of the training set (which would argue for an independent
training-dynamics fix regardless of label quality).

**Finding: the collapse is broad, not concentrated.** At epoch 45 (well into the collapsed regime),
**146/171 groups (85.4%) have entropy `<0.001`, and 138/171 (80.7%) are at *exactly* `0.0000`** —
essentially every group's policy has gone fully deterministic, not just a noisy minority. Only 9
groups (5.3%) retain entropy `>0.1`. This is broad-based convergence toward one-hot outputs across
nearly the whole 171-group training set, consistent with **full-batch gradient ascent on a small,
fixed dataset (repeated backprop over the same 171 groups every epoch, no resampling, no
mini-batching, no fresh stochasticity — see the `train_grpo.py` architecture note) reliably driving
memorization/argmax-commitment given enough epochs**, rather than a few outlier labels dominating.

**Secondary finding: predictions are skewed, not single-mode.** `top1_preset` distribution at
epoch 45 (skip/light/standard/deep): **1 / 63 / 30 / 77** — `skip` is nearly abandoned (predicted
for only 1 of 171 groups) while `light`/`deep` dominate. Not literal collapse-to-one-class, but a
genuine skew worth tracking separately from the entropy question.

**The LR-schedule-timing hypothesis is weakened, not confirmed.** `train_grpo.py` uses cosine decay
with linear warmup; at the observed collapse window (epoch 25-40), the LR multiplier is still
~95-100% of peak regardless of `warmup_epochs=10` (`run20`/`run21`) vs. `20` (`run22`) — the cosine
curve barely moves until much later (~epoch 100+). So "LR just reaching full strength post-warmup"
does not cleanly explain why all 3 runs collapsed in the same narrow epoch band despite different
warmup lengths; this axis has not been tested in isolation (`run22` changed it simultaneously with
`entropy_coef` and `max_grad_norm`), so it isn't ruled out either.

**Candidate experiments, prioritized by expected information gain per run (each held to ONE changed
variable vs. a common baseline — `run22` conflated 3 changes at once, which is why the current
evidence can't attribute its modest delay to any one of them):**

| # | Experiment | Lever type | Why it's informative | Cost |
|---|---|---|---|---|
| 1 | Lower `--lr` (e.g. 1e-5 or 2e-5, vs. the untouched 5e-5 baseline in all 3 runs) | Untested, orthogonal to entropy_coef | Directly throttles the full-batch optimization step size; if collapse-onset scales roughly with `lr`, confirms the "too much gradient per step on a tiny fixed dataset" mechanism and gives a controllable fix (unlike `entropy_coef`'s flat returns) | 1 short run |
| 2 | Smaller LoRA capacity (`--lora-r 4` or `8`, vs. 16 in all 3 runs) | Untested, capacity-driven | Tests whether reduced adapter capacity slows/prevents the collapse-into-argmax dynamic directly | 1 short run |
| 3 | Higher `--beta` (e.g. 0.3-0.5, vs. 0.15 in all 3 runs) | Untested as primary lever | A genuinely different regularizer — pulls toward the reference *distribution shape*, not just toward high entropy in isolation | 1 short run |
| 4 | Higher `--weight-decay` (e.g. 0.05-0.1, vs. the untouched 0.01 default) | Untested, cheap | Direct, orthogonal, standard anti-overfitting lever never varied so far | 1 short run |
| 5 | Isolated `--warmup-epochs` sweep (e.g. 5 vs. 40), holding `entropy_coef`/`max_grad_norm` at `run20`'s original values | Re-test of a confounded variable | `run22` never isolated this; the LR-schedule math above weakens its priority but doesn't rule it out — cheap enough to settle cleanly | 2 short runs |
| 6 | Mini-batch/stochastic group subsampling per epoch (sample a random subset of groups each epoch instead of full-batch every time) | Bigger lever, addresses the root mechanism most directly | Injects the stochastic-gradient noise full-batch-on-fixed-data structurally lacks; requires a real code refactor (`train_grpo.py`'s loop is hard-coded to backprop every group before one `optimizer.step()`) | Code change + 1 run |
| — | Stronger inverse-frequency reweighting (`--inv-freq-temp` 1.0, vs. 0.5) | Complementary, not a substitute | Addresses the `skip`-abandonment skew specifically; unlikely to change collapse *timing*, but may change prediction quality/class balance once collapsed | 1 short run |

**Methodological suggestion: run these short, not to 200 epochs.** Collapse has now manifested by
epoch ~30-40 in all 3 configurations tried — there is no need to run future diagnostic experiments
to `--epochs 200` to learn whether a lever shifts collapse-onset timing. `--epochs 60-80` with the
same `best_strict_healthy` tracking is enough to read the entropy trajectory and cut the feedback
loop by more than half.

**Recommendation on sequencing:** #1 (lower `lr`) and #2 (smaller LoRA rank) are the highest
priority — they are the two levers most directly implicated by the broad-collapse finding above and
have never been touched across `run20`/`21`/`22`, unlike `entropy_coef`, which is now shown
exhausted (§60.7). This is independent of, and can run in parallel with, the label-noise-reduction
plan (Appendix A) — the broad-based nature of the collapse means training-dynamics fixes are worth
pursuing on their own merits, not only as a downstream consequence of cleaner labels.

### 60.9 Revisiting the pre-`run22` Formula-B reward-swap diagnostic, in light of §60.8 (2026-07-31)

Before `run22` concluded, a diagnostic was proposed for exactly this scenario (collapse recurring a
third time): swap in the *true* original Formula-B reward values (from
`bases_ORACLE_BACKUP_20260708_231117`, zero new generation) while keeping *today's* digests/model
inputs unchanged, and retrain — reasoning that if collapse still happens, that rules out "reward
decisiveness" as the driver (since §60.6 showed the old formula is *more* decisive) and points at
the digest-pipeline refresh or grading-judge change; if it doesn't collapse, that isolates the
reward labels themselves.

**Still worth running — cheap, and directly informative regardless of outcome.** Feasibility
confirmed: section IDs are identical between the old backup and today's production
`section_oracle.json` across **all 24 TRAIN articles (24/24 match, 0 mismatches)** — the Phase-0
digest refresh changed section *content*, not the ID scheme, so a merged directory (today's
`research_digest.md`/`guideline_features.json` + the old backup's `section_oracle.json`) is
directly constructable with no section-alignment risk.

**But its original two-way interpretation is now outdated — §60.8 adds a third candidate cause the
original framing didn't have.** The original logic only weighed "reward decisiveness" against
"digest-pipeline/grading-judge change." §60.8's broad-collapse finding (85%+ of groups go fully
deterministic, not a noisy minority) makes a third explanation — **full-batch gradient ascent on a
small, fixed, 171-group dataset, independent of which specific reward values populate it** — at
least as plausible as either original candidate. This changes how each outcome should be read:

- **If it still collapses early (now the more likely outcome given §60.8):** this no longer cleanly
  "points at the digest-pipeline or grading-judge" as originally stated — a full-batch/capacity-driven
  collapse would be expected to recur under *any* valid reward signal, old or new, if `lr`/`lora_r`
  are unchanged. This result would be consistent with (not exclusive proof of) the full-batch
  hypothesis, and would need to be read alongside the `lr`/`lora_r` experiments (§60.8 #1-#2) to
  disambiguate from the digest/judge explanation — not decisive on its own anymore.
- **If it does *not* collapse early:** this reading is unaffected and remains strong — it would
  isolate the old formula's specific reward *structure* (not just its aggregate decisiveness, which
  is higher and would, if anything, predict earlier collapse under the old two-way framing) as
  conferring genuine stability benefits distinct from the full-batch/capacity story, and would be a
  substantive, surprising-enough-to-need-follow-up finding.

**Recommendation: run it, but as a complementary diagnostic, not a substitute for #1/#2.** It is
diagnostic-only — the old Formula B is not a viable production fix regardless of outcome (its
severe `deep`-scarcity, §60.6, is exactly the problem the H0/G0/J0/C2 arc spent weeks fixing) —
whereas lower `lr`/smaller `lora_r` are both diagnostic *and* directly actionable. If GPU capacity
allows only one job at a time, run #1/#2 first; if there is spare capacity, this is a good use of
it in parallel, since it costs zero new generation. Hold `entropy_coef=0.22`, `lr=5e-5`,
`beta=0.15`, `lora_r=16`, `warmup=10` identical to `run20_c2` for the cleanest possible
single-variable comparison, and run short (60-80 epochs, per §60.8's methodological note).

### 60.10 `run23_lr1e5` / `run24_lorar4` handed off to the user (2026-07-31)

Local GPU allows only one run at a time, so #1 (lower `lr`) and #2 (smaller LoRA rank) are handed
off sequentially, each a single-variable change against the exact `run20_c2` baseline (recovered
from shell history: `lr=5e-5, beta=0.15, entropy-coef=0.22, warmup=10, patience=50, lora-r=16,
lora-alpha=16, lora-dropout=0.05, granularity=section, section-weight=hybrid, inv-freq-temp=0.5,
epochs=200`). `--epochs` is kept at 200 in both (not shortened) because it also sets the cosine
LR-schedule's denominator — shortening it would change the LR trajectory shape, not just when the
run stops. The "run short" methodology from §60.8 is instead applied by killing each run manually
once the entropy trajectory is clear (~epoch 60-80), the same way `run22` was handled.

```bash
# Experiment #1 — only --lr changed (5e-5 -> 1e-5)
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run23_lr1e5 --epochs 200 --lr 1e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  > ../../rl_training_data/checkpoints/tasks/run23_lr1e5_stdout.log 2>&1 &

# Experiment #2 — only --lora-r/--lora-alpha changed (16 -> 4, ratio held at 1:1); run AFTER #1
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run24_lorar4 --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 4 --lora-alpha 4 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  > ../../rl_training_data/checkpoints/tasks/run24_lorar4_stdout.log 2>&1 &
```

Watch `mean_entropy` in each `training_log.jsonl` — does it stay meaningfully above the 0.15
healthy floor well past epoch 30-40 this time — and whether `best_strict_healthy_epochs/` keeps
accumulating (health holding) vs. freezing early like `run22`'s did at epoch 28.

### 60.11 `run23_lr1e5` interim check-in (2026-08-01, epoch 149/200, still running): slower decay, but no healthier ceiling

Entropy stayed above the 0.15 healthy floor through epoch ~48 (vs. ~28-30 in `run20`/`21`/`22` —
~65% longer), and at epoch 148 sits around 0.05, not yet at `run22`'s eventual <0.03 floor —
possibly stabilizing at a slightly higher plateau, though only ~20 epochs of data so far.

**But the `best_strict_healthy` comparison shows no real improvement:**

| | `run22` (`entropy_coef=0.6`) | `run23_lr1e5` (`lr=1e-5`) |
|---|---|---|
| Epoch health lost | ~28 | ~48 (65% later) |
| Health-gated strict_top1 ceiling | 28.1% | **25.7%** |

Despite taking 65% longer to lose health, the trustworthy-ceiling did not improve — if anything it's
marginally lower. The raw (untrusted) strict/near-tie numbers climbing at epoch 135-148 (~40%/~66%)
are climbing for the identical reason `run22`'s did — entropy is below the healthy floor and still
slowly shrinking — so they carry the same interpretive caveat. **Preliminary read: lower `lr`, at
this magnitude, appears to stretch the same collapse dynamic over more wall-clock epochs rather than
changing its ultimate character** — a genuinely informative, if modest, result. Not yet conclusive
(entropy hasn't bottomed out), but the health-gated ceiling already answers the more important
question about whether this lever produces a *healthier*, not just *slower*, run.

### 60.12 The trustworthy ceiling is invariant across all 4 runs — and sits *below* the majority-class baseline (2026-08-01)

Two free checks, prompted by the user's argument that `lora_r=4` (§60.8 #2) is not worth the GPU
time because the trustworthy-learning ceiling appears reward-signal-limited rather than
training-dynamics-limited. Both computed from data already on disk, zero new runs.

**Check 1 — retroactive health-gated ceiling for every run.** `run20`/`run21` predate the
entropy-aware tracker, but the metric it computes can be reconstructed exactly from their logs
(max `strict_top1_accuracy` over epochs where `mean_entropy >= 0.15`):

| run | changed variable | health-gated ceiling | reached at | healthy epochs |
|---|---|---|---|---|
| `run20_c2` | (baseline) `entropy_coef=0.22` | 26.9% | epoch 21 | 21 |
| `run21_ecoef035` | `entropy_coef=0.35` | 25.7% | epoch 21 | 22 |
| `run22_reg_combo` | `entropy_coef=0.6` + grad-clip + warmup | 28.1% | epoch 28 | 29 |
| `run23_lr1e5` | `lr=1e-5` | 25.7% | epoch 45 | 49 |

**The ceiling spans just 25.7%–28.1% — a 2.3-point spread — across four wildly different
configurations** (`entropy_coef` 0.22→0.6, `lr` 5e-5→1e-5, grad-clip 0.2→0.1, warmup 10→20).
`run23` more than doubled the number of healthy epochs (21→49) and still did not raise the ceiling.
This strongly confirms the user's premise: **the trustworthy ceiling is essentially invariant to
training-dynamics hyperparameters**, which makes further single-hyperparameter runs (including
`lora_r=4`) low-value for raising it.

**Check 2 — constant-predictor baselines, and the finding that reframes everything.** Applying
`load_section_groups`' flat-filter and argmax logic directly to the label sets:

| label set | strict label dist (sk/li/st/dp) | best constant predictor (strict) | best constant predictor (near-tie) |
|---|---|---|---|
| **C2 (current production)** | 50 / 49 / 38 / 34 | **`skip` → 29.2%** | `light` → 58.5% |
| **True original Formula B** | 71 / 49 / 33 / 18 | **`skip` → 41.5%** | `light` → 59.1% |

**Every single run's health-gated ceiling (25.7%–28.1%) is *below* C2's 29.2% majority-class
baseline.** No run has ever, while in a genuinely healthy (non-collapsed) state, beaten a trivial
"always predict `skip`" predictor on strict top-1. The problem is not merely that trustworthy
learning is *low* — it is that **no learning above a trivial constant baseline has yet been
demonstrated at all under healthy entropy**. This is a materially stronger statement than §60.7's
"barely above the 25% random-4-arm baseline," and it reframes the whole investigation: the binding
constraint is very unlikely to be a training-dynamics hyperparameter.

**Critical caveat for the planned Formula-B swap experiment (§60.9): its success criterion must be
baseline-relative, or its result will be misleading.** Formula B's labels are substantially more
skewed than C2's (`skip` 71/171 vs. 50/171 — the known deep-scarcity, §60.6), so its
constant-predictor baseline is **41.5%, not 29.2%**. A Formula-B run reaching, say, a 35%
health-gated ceiling would *look* like a large improvement over C2's 25.7–28.1% while actually
being **6.5 points worse than its own trivial baseline**. The correct metric is
**`ceiling − that label set's own constant-predictor baseline`**, i.e. does the model beat trivial
*on the labels it was trained on*. Usefully, the **near-tie baselines are nearly identical
(58.5% vs. 59.1%)**, so `top1_accuracy` (near-tie) is directly comparable across the two label sets
without this correction and should be tracked as the cleaner cross-run comparison.

**Assessment of the user's proposal (run Formula-B swap instead of `lora_r=4`): agreed, with the
above correction.** The reasoning is sound and now well-evidenced by Check 1. It also improves on
§60.9's own framing: §60.9 judged the swap experiment partly ambiguous because the full-batch
hypothesis could explain *collapse timing* under any reward signal — but the user's reframing
targets the **ceiling**, not the timing, and the full-batch mechanism does not obviously predict a
particular ceiling. So the experiment is *more* informative under this success criterion than
§60.9 concluded, provided it is measured baseline-relative.

**Expected-outcome caveat, stated in advance to avoid post-hoc rationalization:** given Check 1's
flatness *and* the fact that Formula B's higher raw ceiling would be partly mechanical (easier,
more skewed labels), the most likely result is that Formula B also fails to beat its own 41.5%
baseline. That would be a genuinely valuable negative result — it would mean neither reward
structure tested so far supports above-trivial learning under healthy entropy, pointing at label
noise (Appendix A) or the input representation, rather than at reward *shape*, as the true binding
constraint.

### 60.13 `run25_formulab_diag` built and handed off (2026-08-01)

`run23_lr1e5` killed at the user's decision (its diagnostic question — healthier vs. just slower —
was already answered by §60.12's ceiling comparison). Built the Formula-B swap experiment instead
of `run24_lorar4` (§60.8 #2), per the user's argument in §60.12 that further training-dynamics
hyperparameter runs are low-value given the ceiling's invariance.

**Implementation (new, separate script — production paths untouched):**
- `training/build_formulab_diag_bases.py`: for each of the 24 TRAIN articles, copies today's
  `research_digest.md` + `guideline_features.json` from `rl_training_data/bases/` (current digest
  pipeline, unchanged model inputs) and `section_oracle.json` from
  `bases_ORACLE_BACKUP_20260708_231117/` (true original Formula-B rewards, zero new generation)
  into a new root, `rl_training_data/bases_FORMULAB_DIAG/`. Verified 24/24 built; a direct
  pure-JSON/regex check (no heavy-lib import, to sidestep this environment's slow
  `import train_grpo` startup) confirms every oracle section ID is present in its digest for all
  24 articles.
- `train_grpo.py`: added a minimal `--bases-dir` CLI override (mirrors the existing
  `--episodes-dir` pattern used elsewhere in the repo) — when set, overrides the module-level
  `_BASES_DIR` before data loading, so `section_oracle.json`/`research_digest.md`/
  `guideline_features.json` lookups redirect to the given root. Default `None`, so every other
  invocation is unaffected. `py_compile`-verified.

**Recipe: identical to `run20_c2`'s baseline except `--bases-dir`**, for the cleanest possible
single-variable comparison against the existing `run20`-`run23` results:

```bash
cd /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training

PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run25_formulab_diag --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  --bases-dir ../../rl_training_data/bases_FORMULAB_DIAG \
  > ../../rl_training_data/checkpoints/tasks/run25_formulab_diag_stdout.log 2>&1 &
```

**What to watch, per §60.12's baseline-relative correction — do not compare raw ceilings across
label sets:** track `top1_accuracy` (near-tie) against its own near-tie constant baseline (59.1%
for Formula-B, vs. 58.5% for C2 — nearly identical, so this metric *is* directly comparable
without correction), not `strict_top1_accuracy` against C2's 29.2% baseline. The informative
question is whether the health-gated ceiling for *either* metric clears *its own* label set's
constant-predictor floor — not whether Formula-B's raw numbers look bigger than C2's.

**Input-identity verified directly, not just by construction (2026-08-01):** `_rl_preset.py`'s
`build_rl_input(digest, target_section_id)` — what the model actually receives — is a pure
function of the digest text and section id; it never reads `section_oracle.json`. Confirmed by
direct `diff -q` on 3 sampled TRAIN articles between `bases/` and `bases_FORMULAB_DIAG/`:
`research_digest.md` and `guideline_features.json` are byte-identical, while `section_oracle.json`
correctly differs (the one deliberately swapped file). `guideline_features.json` only supplies
`word_weight` for the loss's section weighting — not part of the model's input text either. So the
only difference between `run25_formulab_diag` and `run20_c2` is the reward labels; everything else
(model input text, loss-weighting inputs, LoRA/optimizer hyperparameters) is identical — the
single-variable design holds.

**Monitoring:** `tail -f /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run25_formulab_diag_stdout.log` for raw
progress; TensorBoard via `tensorboard --logdir /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run25_formulab_diag/runs --port 6006` (path also printed by
the script itself at startup) for `eval/mean_entropy`, `eval/top1_accuracy`,
`eval/strict_top1_accuracy`, `eval/mean_expected_reward`.

### 60.14 `run13_formulaB`'s hyperparameters and time series, verified directly (2026-08-01)

Investigated `run13_formulaB`'s checkpoint state directly (not re-citing prior claims) to give
`run25_formulab_diag`'s comparison a precisely-verified baseline.

**Hyperparameters, independently verified from checkpoint state:**

| | value | source |
|---|---|---|
| `lr` (peak) | **5e-5** | scheduler `base_lrs` |
| `lr` at epoch 96 | 2.83e-5 (56.6% of peak) | optimizer `param_groups` — implies `--epochs≈200`, `--warmup≈10` via the cosine schedule's math |
| `weight_decay` | **0.01** | optimizer `param_groups` |
| `lora_r` / `lora_alpha` / `lora_dropout` | **16 / 16 / 0.05** | `adapter_config.json` (direct read) |
| `granularity` | **section** | `resume_state.pt` |
| target modules | q/k/v/o_proj, gate/up/down_proj | `adapter_config.json` |

Every value matches `run20_c2`'s recipe exactly (cross-checked against the bash-history command
recovered in §60.13). Combined with the document's already-established `entropy_coef=0.22`/
`beta=0.15` match, **the only two things that differ between `run13` and `run20_c2` are the
reward formula and the digest pipeline** — exactly the two candidates `run25_formulab_diag`
(§60.13) is designed to separate.

**Time-series behavior — a genuinely different shape, not just "collapsed later":**
- `sigma_floor_fraction` = **0.0058 (0.58%) constant for all 97 epochs** — vs. C2's 22.22%,
  confirming Formula B's labels were far less degenerate/near-tie (matches §60.6's 6-7% floor%).
- **Entropy does not crash early and stay down — it oscillates substantially throughout**:
  0.18→0.15→**0.51 (spike, epoch 10)**→0.15→0.23→0.07→0.14→0.09→0.07→0.05→**0.09 (bounce)**→
  0.03→**0.09 (bounce)**→0.06→0.05→0.02→0.01, only really settling low around epoch 75-96 —
  qualitatively different from `run20`-`23`'s sharp-cliff-then-flat pattern.
- **Despite ending collapsed (H≈0.01-0.03 by epoch 90-96), accuracy reached genuinely high
  levels**: strict **83-84%**, near-tie **93-95%** — far beyond anything in the C2 era
  (health-gated ceiling ~26-28%, raw collapsed ceiling ~55-58%/70-80%, §60.12).
- **Critically, this collapsed-but-high-accuracy state actually generalized**: TEST exact=10/16,
  miss=0, MAE=0.375 (§60.3). The opposite of `run20_c2`'s collapse, which produced a degenerate
  always-`deep` policy that failed TEST badly (exact=1/16).

**Synthesis: entropy collapse alone is not disqualifying — what matters is whether what gets
memorized is genuinely learnable/generalizable, not just low-entropy.** `run13` converged to
something that held up on TEST; `run20`-`23` converged to something that didn't, under identical
hyperparameters. This reframes the open question from "why does entropy collapse" to "why did the
thing `run13` converged to generalize, while the thing `run20`-`23` converged to did not."

**Live signal from `run25_formulab_diag` (checked at epoch 25/200) — already promising, not yet
conclusive:**
- `sigma_floor_fraction = 0.0702 (7.0%)` — an order of magnitude better than C2's 22.22%, much
  closer to `run13`'s clean-label profile than to any C2-era run.
- **Entropy already shows the same oscillating character as `run13`**: 0.26→dips→**spikes to
  0.66-0.79 at epochs 8-11**→gradually declines to 0.10 by epoch 25 — a strikingly different shape
  from `run20`-`23`'s smooth monotonic pattern, and closely resembling `run13`'s own epoch-10 spike.

Only 25/200 epochs in, but directionally suggestive that **the reward formula, not the digest
pipeline, is the operative variable** behind `run13`'s healthier dynamics — worth continued
monitoring as `run25` progresses, and directly actionable once it reaches a comparable epoch count
to check against `run13`'s eventual TEST-generalizing outcome.

### 60.15 Is replication the right primary lever for `sigma_floor_fraction`? A synthesis across §54.7/§60.6/§60.12/§60.14 (2026-08-01)

**What `sigma_floor_fraction` precisely measures, restated for clarity:** the fraction of *kept*
training groups whose population std across all 4 arm rewards (`std({r_skip,r_light,r_standard,
r_deep})`) is below `sigma_floor=0.04` — a different statistic from `margin` (top1−top2 gap, used
in §55.2/§55.3/A.7) and from the separate flat-drop filter (`max−min < sigma_floor`, which fires on
zero groups today). When it fires, `0.04` is substituted for the true (smaller) std in the
advantage-normalization denominator — this *dampens*, not amplifies, that section's contribution.

**Replication is well-justified, but has a real, currently-unknown ceiling.** It is the *only*
lever proven able to move the underlying defensible-section count — §55.3's `sigma_floor` sweep
already showed threshold tuning cannot (45/282 and 10/282 stayed flat at every value tested).
Averaging shrinks the *noise* component of a section's observed spread, which can only reveal a
genuine difference that noise was masking — **it cannot manufacture a real difference where the
true arms are genuinely tied.** What fraction of today's 22.22% (`C2`) reflects noise-masked
signal vs. genuine ties is not yet known; A.7's tiny (`n=15`) sample was suggestive but far too
small to bound this for the full corpus.

**A materially cheaper, already-measured, currently-underweighted alternative sits in this
investigation's own history: `cost_coef`.** §54.7's sweep already showed `floor%` is *extremely*
sensitive to it — 8.2% at `-0.06` → 21.1% at `-0.045` → ~20.5% at `-0.03`/`-0.02` — a pure formula
constant, zero new generation cost (just a regen from already-graded episodes). Today's `-0.03`
was chosen to protect `deep`-representation (§54.7), **not because it was judged noise-optimal** —
`floor%`/training-stability was not the deciding criterion at the time.

**But §60.6 already warned decisiveness obtained this way isn't automatically correctness** — a
blunter cost term or coarser binary scoring can manufacture bigger, "cleaner"-looking margins
mechanically, independent of genuine content differentiation. This is the real tension: is
lowering `sigma_floor_fraction` via `cost_coef` legitimate signal-sharpening, or just the same
"bluntness masquerading as decisiveness" §60.6 flagged in the original Formula B?

**§60.14 complicates the caution, empirically.** The one clean natural experiment available
(`run13` vs. `run20`-`23`, *identical* hyperparameters, only reward formula + digest differ) shows
`run13`'s much lower `sigma_floor_fraction` (0.58% vs. 22.22%) — achieved partly via the same
blunt mechanisms §60.6 flagged — nonetheless coincided with a dramatically better-generalizing
model (TEST exact=10/16 vs. 1/16). Theory says bluntness ≠ correctness; the one real before/after
comparison we have says lower `sigma_floor_fraction`, however achieved, correlated with a much
healthier outcome. Both things can be true: bluntness may not indicate *better-calibrated content
judgment*, while still producing a *more learnable training signal* in practice — decisiveness and
correctness can come apart on content quality while still moving together on trainability. This is
`n=1` clean comparison, not proof, but it's the best evidence available and shouldn't be ignored.

**Recommendation: don't treat replication as the single most important thing in isolation —
pursue it alongside two cheaper, already-informed levers, in parallel:**
1. **Replication (Appendix A)** — the theoretically cleanest fix, targets noise specifically,
   but expensive (192 cycles) and its payoff ceiling is unknown until it's run.
2. **A fresh, dedicated look at `cost_coef` with training-stability as an explicit criterion** —
   §54.7's sweep only weighed it against `deep`-representation; it was never re-evaluated against
   `sigma_floor_fraction`/generalization now that §60.14 supplies real evidence this matters. Values
   between `-0.03` and `-0.06` (e.g. `-0.045`, already swept, `floor%=21.1%`) may capture much of
   the training-stability benefit without `-0.06`'s severe deep-scarcity — worth testing directly
   with a real retrain, not just modeled, since it's near-zero cost (reuses already-graded data).
3. **A.8's confidence-weighting** — down-weights uncertain sections directly, extracting value
   without waiting on either of the above, code-only.

`run25_formulab_diag`'s outcome (§60.13/§60.14) is the fourth, currently-running data point that
will help disentangle how much of `run13`'s advantage was the reward formula (supporting lever #2
above) vs. the digest pipeline (which would argue for neither #1 nor #2 alone being sufficient).

### 60.16 `run25_formulab_diag` completed — real TEST results, and what they change (2026-08-02)

The run completed all 200 epochs. Real RL-only TEST-set inference was run at 4 checkpoints
(epoch 114, 137, 145, 155). This is the first real held-out evaluation of Formula B's reward
*values* combined with *today's* digest — directly testing what §60.9/§60.13/§60.14 set out to
separate.

**Full completed trajectory, read from `training_log.jsonl` (was only checked through epoch 25
in §60.14):** entropy actually **does** collapse early after all — crashes to 0.076 by epoch 30
and stays in the 0.02-0.06 band for the remaining 170 epochs, never recovering. The epoch-8-11
spike noted in §60.14 was real but did not prevent the same broad collapse timing as `run20`-`23`
(~epoch 20-30). **Health-gated ceiling: 22.2% at epoch 20 (23/200 healthy epochs)** — this is
*lower* than every C2-era run (25.7-28.1%, §60.12), and further below Formula B's own 41.5% strict
constant-predictor baseline than C2's runs were below C2's 29.2% baseline. By the health-gate
criterion alone, `run25` looks like the *worst* run yet.

**But the real TEST results tell the opposite story — decisively better than every C2-era run:**

| run (TEST, RL-only unless noted) | exact | miss | MAE | regret (mean) |
|---|---|---|---|---|
| `run20_c2` (best_strict, ep95) | 6.25% (1/16) | 62.5% (10) | 1.688 | — (catastrophic) |
| `run15_recalibrated` | 33% | 27% (4) | 0.933 | 0.0165 |
| `run17_invfreqtemp10_recal` | 40% | 33% (5) | 1.000 | 0.0128 |
| **`run25` @ epoch 114 (best)** | **38% (6/16)** | **12% (2)** | **0.750** | **0.0219** |
| `run25` @ epoch 137 | 38% (6/16) | 19% (3) | 0.812 | — |
| `run13_formulaB` (original, old digest — RL-only per §13.2, **not re-verified today**, see correction below) | 62.5% (10/16) | **0%** | 0.375 | 0.0384 |
| `run13_formulaB`/best on new digests, **RL-only, direct fresh re-run (2026-08-03) — the true zero-retrain baseline** | 38% (6/16) | 19% (3) | 0.812 | 0.0177 (max 0.0667) |
| §14.3 figure previously cited here as "zero-retrain" — **was actually RL+Grok, not a zero-retrain RL-only number at all** | 62.5% (10/16) | 18.75% (3) | 0.625 | 0.0472 |

Verified directly from the saved `grok_planner_test_results/_summary.json` (dated 2026-08-03,
not the stale `rl_only_train_and_test_results.md` in the same directory, which predates this run
and still reflects an older evaluation) — n=16, exact=6, near=7, miss=3, MAE=0.8125, regret
mean=0.0177/max=0.0667 over the 15 non-forbidden articles, matching the headline figures above
exactly. **The 3 misses are `13_agent_framework`** (chosen=light, oracle=deep), **`29_evaluation_
metrics`** (chosen=deep, oracle=light), **and `Dark_Dimension`** (chosen=light, oracle=deep) — all
2-level, all different from §14.2/§14.3's RL+Grok-layer miss set (`13_agent_framework`,
`29_evaluation_metrics`, `Space-Time_QECC`). `Dark_Dimension` is a genuinely new RL-only-layer miss
not present at the RL+Grok layer, and `Space-Time_QECC` — a miss at the RL+Grok layer — is only a
**near** here (chosen=standard, oracle=light), consistent with §14.4's finding that Grok escalates
that article, not corrects it. This is concrete, per-article evidence for implication #5 below:
Grok's net effect on new digests is not one isolated fix, it reshuffles several articles in both
directions.

`run25` beats every C2-era run on `miss%` and `MAE` (the more informative granular metrics),
despite a comparable or *worse* raw `exact%` to `run15`/`run17`, and obliterates `run20_c2`'s
collapse specifically. **This is strong, direct evidence that the reward formula — not just
training-dynamics hyperparameters — is a major, independently-operating lever on TEST
generalization**, confirming what §60.14's `run13`-vs-`run20`-`23` comparison already suggested,
now with a real controlled swap (only the reward labels changed) rather than a historical
before/after across many confounded changes.

**A genuinely important correction to the entropy-health-gate framework.** `run25`'s useful
checkpoints (114-155) are *all* deep in the collapsed regime (health lost at epoch ~22) — by the
health-gate criterion built in §60.7 specifically to distrust post-collapse checkpoints, *none* of
these would ever be certified as trustworthy, yet they demonstrably generalize far better than any
C2-era checkpoint (healthy or not). **Entropy collapse does not have the same consequence under
every reward formula.** Under C2, collapse converges to a degenerate, near-constant policy that
fails TEST catastrophically (§60.1-60.2). Under Formula B — in both `run13` (§60.14) and now `run25`
— collapse still happens, but what the policy converges to memorizing evidently corresponds to a
more genuinely correct decision function, one that continues to generalize despite low entropy.
**The health-gate remains a valid, valuable red flag for catching C2's specific degenerate-collapse
failure mode** (its whole reason for existing, §60.7) **but should not be treated as a universal
"post-collapse checkpoints are worthless" rule** — checkpoint trustworthiness ultimately needs to be
judged against held-out performance (or a genuine proxy for it), not entropy health alone.

**Real overfitting/drift confirmed, and it is a plateau-then-degrade pattern, not classic
still-improving overfitting.** TRAIN metrics are essentially flat from epoch 100 through 199
(exact 42-46%, near-tie 88-93%, barely moving) while TEST clearly degrades past epoch 114:

| epoch (tracker) | TEST exact | TEST near | TEST miss | TEST MAE |
|---|---|---|---|---|
| 114 (tie-best near-tie) | 38% | 50% | 12% | 0.750 |
| 137 (best mean-expected-reward) | 38% | 44% | 19% | 0.812 |
| 145 (tie-best near-tie, later tie) | 31% | 44% | 25% | 0.938 |
| 155 (best-strict) | 31% | 44% | 25% | 0.938 |

Since TRAIN isn't still climbing while this happens, continuing training past ~epoch 114-120 buys
*nothing* on the training objective while actively costing held-out performance — a pure drift
phase, not a real accuracy-vs-generalization tradeoff. The TRAIN-side checkpoint trackers
(`best_strict`/`best_neartie`) picked *worse*-for-TEST checkpoints at later ties (145, 155) than an
earlier one (114) that was never their own final answer — direct evidence that TRAIN-metric-driven
checkpoint selection is not reliable for this style of run, either.

**What is still unresolved (superseded — see the 2026-08-03 correction two paragraphs below):**
~~`run25` falls meaningfully short of `run13`'s full result, and even short of the "free"
zero-retrain baseline.~~ `run13`'s original TEST result (10/16, 0% miss, MAE 0.375) and even the
do-nothing baseline (naively re-evaluating `run13`/best on new digests with zero retraining: 10/16,
18.75% miss, MAE 0.625, §14.3) both beat `run25`'s best retrained checkpoint (6/16, 12% miss, MAE
0.750) on `exact`/`MAE`. Retraining from scratch on the new digests — even with the
historically-successful reward formula — does not fully recover, and notably underperforms just
keeping the old model and running it on new inputs with no retraining at all. This points at
something beyond reward-formula choice: either the digest pipeline itself costs real, independent
performance (consistent with §14.3's original finding), or the *process* of retraining for 100+
epochs on the new digests' specific content/structure is itself lossy in a way that zero-shot
transfer from the old model isn't — plausibly connected to the same full-batch/fixed-dataset
dynamics (§60.8) finding new material to overfit to. **(This whole framing turned out to rest on a
mislabeled RL+Grok figure — see below.)**

**Correction (2026-08-02): the §14.3 zero-retrain baseline cited above is RL+Grok, not RL-only —
`run25`'s eval is RL-only, so the miss-rate comparison above was not apples-to-apples.** Confirmed
directly: §14.3's own "baseline" column (10/16 exact, 0 miss, MAE=0.375, regret_mean=0.0384,
regret_max=0.170) exactly matches §13.4's explicitly-labeled "fresh full RL+Grok eval" result,
figure for figure. §14.4 states directly that "the full RL+Grok eval (§14.3) shows Grok escalating
[`Space-Time_QECC`] further, P2→P3, turning a recoverable near-miss into a severe 2-level miss" —
at the RL-only+cost-rule layer that same article was only a **near** (`chosen=P2, oracle=P1`,
regret 0.126), not a miss. Correcting for this one documented layer-difference, the **RL-only­
equivalent** zero-retrain baseline is: exact=10/16 (62.5%, unchanged), near=4 (not 3), **miss=2/16
(12.5%, not 18.75%)**, MAE≈**0.5625** (not 0.625). This **retracts** the earlier claim that `run25`
beats the zero-retrain baseline on miss-rate — under the corrected, consistent (both RL-only)
comparison, they are essentially **tied** on miss-rate (12% vs. 12.5%), and the baseline remains
clearly ahead on `exact%` and `MAE`. If anything this sharpens, rather than weakens, the
"retraining on new digests doesn't recover what's lost" conclusion below — the zero-retrain
baseline is now at least as good as `run25` on all three metrics, not mixed.

**Correction (2026-08-03): the reconstruction above was itself wrong — a direct re-run shows the
true RL-only zero-retrain baseline is dramatically worse than 10/16, and `run25` in fact ties or
beats it.** Rather than continuing to infer the RL-only number from the RL+Grok figure and one
documented Grok fix, `infer.py::_DEFAULT_ADAPTER_DIR` was pointed directly at `run13_formulaB/best`
and `test_grok_planner.py --rl-only --save-json` was re-run against TODAY's (current,
Phase-0-refreshed) digests — the actual "old checkpoint + new digests, RL-only" experiment, not an
inference from prose. **Real result: exact=6/16 (38%), near=7 (44%), miss=3 (19%), MAE=0.812.**

This means essentially all of the apparent 10/16-exact strength in §14.3's figure came from Grok's
correction pass, not the RL layer — Grok's marginal contribution on the new digests is far larger
than the single documented `Space-Time_QECC` near→miss case (§14.4) suggested; there must be
several more articles where Grok flips a near→exact (or otherwise improves on the raw RL vote) that
were never individually inventoried. The one-fix reconstruction method used above is now known to
fail on this dataset and should not be repeated — a genuine re-run is required whenever an RL-only
number is needed and no direct RL-only run exists.

Comparing like-for-like (both RL-only, both on new digests), the TRUE zero-retrain baseline
(exact=6/16, near=7, miss=3, MAE=0.812) is **matched or beaten by `run25`'s own checkpoints on every
metric**: epoch 114 (exact=6/16, miss=2, MAE=0.750) is strictly better on miss-rate and MAE at equal
exact%, and epoch 137 (exact=6/16, near=7, miss=3, MAE=0.812) matches it digit-for-digit on all four
metrics. **This retracts the "run25 falls short of the free zero-retrain baseline" conclusion
entirely** (the paragraph two above, marked superseded) — under a consistent RL-only comparison,
retraining does not lose to doing nothing on the new digests; it ties or wins. The only genuinely
open gap left is between
`run25`/zero-retrain-on-new-digests (~38% exact) and `run13`'s performance on the **old** digests
(62.5% exact, §13.2) — but that crosses a digest-distribution change, not a retraining-vs-no­
retraining question, so it points at the digest pipeline being harder/different, not at retraining
being lossy.

**This also reopens the question of how solid the old-digest "10/16 exact, 0 miss" RL-only figure
itself is**, given the RL-only/RL+Grok gap on new digests has just been shown to be far larger than
assumed. The case for it being genuinely RL-only: §13.2's "TEST constrained rule" row (10/16 exact,
6 near, 0 miss, MAE 0.375, regret_mean 0.0384) was measured and labeled *before* Grok was introduced
into this investigation thread (§13.4, titled "Full RL+Grok eval confirmed the concern," comes
after), and §14.2's "production baseline" row later cites the identical six figures for what it
explicitly calls the full RL+Grok pipeline — i.e. Grok was independently shown to be a complete
no-op on the old digests at the time (consistent with §13.4's own "exactly matches the RL-only
cost-rule ceiling (§13.2)" note). That is real, explicitly-labeled contemporaneous evidence, not a
reconstruction — but unlike the number above, **it has not been independently re-run today**. A
full re-verification would need the old (pre-golden_local-fix) digests for all 40 articles; only a
partial backup survives (`bases_GOLDENLOCAL_BACKUP_20260710_223940`, covering just the
golden_local-sourced TEST articles — `Bird_Eye_Extreme`, `Dark_Dimension`, `Distinct_AI_Models`,
`Earth_Oceans_Origin`, `HNSW`, `Space-Time_QECC`, and a couple more), not a full 40-article corpus.
Treat the old-digest 62.5%-exact/0-miss figure as **well-documented but not re-confirmed today**,
rather than as solidly established as the fresh new-digest number above.

**Implications for the plan:**
1. **Elevate §60.15's `cost_coef` re-investigation, and sharpen it into a real ablation.** Formula B
   differs from C2 in *two* respects simultaneously (larger/ordinal `cost_coef`, and raw-binary
   `de`/`be` instead of the saturating `enhancement_credit()` curve) — `run25` cannot tell us which
   one (or both) drives the improvement. The highest-value next experiment is a real retrain of
   **C2 with only `cost_coef` reverted** (e.g. `-0.045` or `-0.06`, everything else — `ga`-gate,
   `ra`-removal, `enhancement_credit()` curve — left as shipped), isolating the cost-magnitude
   variable cleanly against both `C2` and `run25`.
2. **Sequence formula-selection before the expensive replication spend — refined (2026-08-03, see
   below): only the FINAL retrain step actually needs to wait, not the replication generation
   itself.** Appendix A's 192-cycle plan was scoped around C2's current labels; given real evidence
   the formula itself is a major lever, this originally argued for resolving *which* formula to use
   before spending on replication. Verified directly against the code (`merge_replicate_oracles.py`
   calls `measure_replicate_noise.py::_compute_replicate_sections`, which recomputes rewards from
   each replicate's raw `reasoning.json` using whichever formula is *currently* live in
   `generate_episode_oracles.py::_section_reward` at call time — not baked in at generation time):
   the expensive step (writing + grading 192 replicate drafts) produces raw per-dimension grader
   scores that are **formula-agnostic and fully reusable**, exactly like the single-draw episode
   data `sweep_reward_formula.py`/`model_gate_candidates.py` already re-use for free. **This means
   Appendix A's replication (A.10 step 2) can run in parallel with §61's Stage 1 GPU experiments**
   — different resources entirely (external LLM write/grade API calls vs. local GPU RL training),
   no scheduling contention. Only **A.10 step 4 (retrain GRPO on the merged/averaged labels)**
   should wait for §61 to conclude — that is the one step where training under a formula that gets
   superseded shortly after would be genuinely wasted GPU time; re-running `merge_replicate_oracles.py`
   itself after §61 concludes is free and will automatically pick up whichever formula wins.
3. **The digest-pipeline gap is no longer the best-supported explanation — see §60.17's ablation,
   which weakens it considerably.** The 8-article old-vs-new-digest test shows digest content
   alone accounts for only ~1 exact hit net, far short of the full 16-article 62.5%→38% swing. The
   old-digest baseline figure's own reliability (already flagged as unconfirmed in §60.16) is now
   the more probable locus of the discrepancy, alongside newly-recognized oracle/label drift since
   the original 2026-07-10 evaluation (the oracle has been revised multiple times since — G0, J0,
   H0, `EPS_BAND`, cost_coef staging, C2 — so the historical "62.5%, 0 miss" figure and every fresh
   rerun this week are not even scored against the same ground truth). A direct content/structure
   diff between old and new digests remains informative but is no longer the leading hypothesis for
   the gap.
4. **Checkpoint selection for future Formula-B-style runs needs to be TEST-informed, not purely
   TRAIN-tracker- or entropy-gate-driven.** Concretely: periodically evaluate on TEST during/after
   training rather than trusting `best_strict`/`best_neartie`'s own notion of "best," and consider
   capping exploratory runs around epoch 120-150 rather than 200, given the confirmed drift past
   that point here.
5. **Grok's marginal contribution on the new digests needs its own accounting — it is much larger
   than previously documented.** The 2026-08-03 re-run shows RL-only alone recovers only 38% exact
   on new digests while RL+Grok (§14.3) recovers 62.5% — a 6-article swing that only one case
   (`Space-Time_QECC`, §14.4) was ever individually attributed. Before trusting any future
   RL-only ablation as a proxy for full-pipeline behavior on new digests, inventory which specific
   TEST articles Grok is correcting and why, the same way §14.4 did for the single known case.

### 60.17 One-off old-digest-structure ablation (2026-08-03) — digest structure alone explains little of the gap

**Motivation.** §60.16's zero-retrain re-run showed a large gap between `run13_formulaB`'s
historical OLD-digest result (62.5% exact, 0 miss, full 16-article TEST) and its freshly-measured
NEW-digest result (38% exact, 3 miss) — previously attributed to the digest-pipeline refresh
(implication #3, original wording). The user proposed testing this directly: rerun the *same*
checkpoint on the *old* digest structure, as a one-off, without touching the current new-digest
production code path.

**Feasibility.** Full old digests for all 40 articles are not recoverable —
`bases_ORACLE_BACKUP_20260708_231117` (2026-07-08) preserved only oracle files, no digests. The
only surviving old-digest snapshot is `bases_GOLDENLOCAL_BACKUP_20260710_223940`, covering exactly
the 8 golden_local-sourced TEST articles Phase-0's `collect_sources()` fix actually regenerated
(`Bird_Eye_Extreme`, `Dark_Dimension`, `Distinct_AI_Models`, `Earth_Oceans_Origin`, `HNSW`,
`Space-Time_QECC`, `State_of_LLM_Reasoning`, `Understanding_Reasoning_LLMs`) — the other 32
articles' digests never changed, so there is no old-vs-new question for them. Built an isolated
`rl_training_data/bases_OLDDIGEST_DIAG/`: OLD `research_digest.md`/`guideline_features.json` (the
one variable under test) paired with TODAY's current `article_oracle.json`/`section_oracle.json`
(held constant, matching how the new-digest run was scored) — confirmed the digest text genuinely
differs (313 diff lines on `Space-Time_QECC`) while the oracle is byte-identical to production.
`infer.py::_DEFAULT_ADAPTER_DIR` and `test_grok_planner.py::_BASES_DIR` were temporarily repointed
(one-off, comment-marked, reverted immediately after the run), no permanent CLI flag added, per the
user's explicit constraint.

**Result — matched 8-article subset, RL-only, `run13_formulaB/best`, old vs new digest:**

| digest | exact | near | miss | MAE | regret mean |
|---|---|---|---|---|---|
| NEW (today's production, same 8 articles pulled from §60.16's 16-article run) | 3 (37.5%) | 4 (50%) | 1 (12.5%) | 0.750 | — |
| OLD (`bases_OLDDIGEST_DIAG`, fresh 2026-08-03 run) | 4 (50%) | 3 (37.5%) | 1 (12%) | 0.750 | 0.0274 |

**MAE is identical, miss count is identical (both `Dark_Dimension`), and the exact/near split
differs by only 1 article net.** Per-article detail:

| Article | Oracle | New-digest RL (verdict) | Old-digest RL (verdict) | Changed |
|---|---|---|---|---|
| `Bird_Eye_Extreme` | light | light (EXACT) | light (EXACT) | no |
| `Dark_Dimension` | deep | light (MISS) | skip (MISS) | yes — miss got *worse* (2→3 levels off) |
| `Distinct_AI_Models` | deep | standard (NEAR) | standard (NEAR) | no |
| `Earth_Oceans_Origin` | standard | deep (NEAR) | standard (EXACT) | yes — improved |
| `HNSW` | light | light (EXACT) | light (EXACT) | no |
| `Space-Time_QECC` | light | standard (NEAR) | light (EXACT) | yes — improved |
| `State_of_LLM_Reasoning` | skip (forbidden) | light (NEAR) | light (NEAR) | no |
| `Understanding_Reasoning_LLMs` | standard | standard (EXACT) | deep (NEAR) | yes — worsened |

4 of 8 articles flip their specific RL preset between old and new digest — digest content clearly
does move individual predictions — but the flips go **both directions** (2 improve, 1 worsens, 1
miss shifts marginally worse) and **net out to almost nothing in aggregate** (+1 exact / −1 near,
tied MAE, tied miss count).

**This is real evidence against "digest pipeline" as the primary explanation for the full
16-article gap — supporting the user's hypothesis.** The historical old-digest full-TEST figure
(62.5% exact, 0 miss) vs. the fresh new-digest full-TEST figure (38% exact, 3 miss, §60.16) is a
swing of 4 exact hits and 3 misses across 16 articles. But on the only 8 articles where the digest
actually changed, the net swing is ~1 exact hit and 0 miss-count change — nowhere near enough to
account for the full-corpus gap by itself. Whatever explains the bulk of the 62.5%→38% drop, it is
very unlikely to be the digest-structure change alone.

**What's left unexplained, and two newly-sharpened candidate causes.** The other 8 TEST articles
(`04_structured_outputs`, `07_reasoning_planning`, `13_agent_framework`, `14_agent_system_design`,
`29_evaluation_metrics`, `31_CI`, `Gravity_Entropy`, `Insects_Consciousness`) never had their
digests touched by Phase-0 — today's `bases/` already holds their original digest, unchanged. Two
of the three fresh misses in §60.16's 16-article run (`13_agent_framework`, `29_evaluation_
metrics`) are in this unchanged-digest group, which rules out the digest refresh as their specific
cause. Two candidates now stand out ahead of "digest pipeline": (1) **the old-digest "62.5%, 0
miss" figure's own reliability** — already flagged in §60.16 as documented-but-not-re-confirmed
today, and now the more probable locus of the discrepancy; (2) **oracle/label drift since the
original 2026-07-10 evaluation** — the oracle has been revised multiple times since (`G0`, `J0`,
`H0`, `EPS_BAND`, cost_coef staging, `C2`, shipped 2026-07-29), so the historical figure and every
fresh rerun this week are not even scored against the same ground truth, independent of any digest
or checkpoint change at all. Both require data that no longer fully exists (old digests for the
other 8 TEST articles; the exact oracle snapshot in effect on 2026-07-10) to resolve further —
recorded as open, not resolved.

**Cleanup:** `infer.py::_DEFAULT_ADAPTER_DIR` and `test_grok_planner.py::_BASES_DIR` reverted to
production defaults (`run25_formulab_diag/best_er` and `bases/`); `bases_OLDDIGEST_DIAG/` left on
disk as a reusable diagnostic artifact (production untouched throughout).

## 61. Investigation plan: why is Formula-B-era (`run13`/`run25`) TEST performance so much better than C2-era? (2026-08-03)

**What §60.16/§60.17 have already substantially ruled out**, so this plan doesn't re-litigate them:
- **The digest pipeline** (§60.17): the only clean single-variable test available (8-article
  subset) shows digest content alone nets ~1 exact hit — nowhere near the observed gaps.
- **"Retraining itself is lossy"** (§60.16's 2026-08-03 correction): `run25` ties/beats the true
  RL-only zero-retrain baseline on new digests — retraining does not lose to doing nothing.

That leaves the **reward formula structure** as the dominant remaining candidate, with
**oracle/label drift since 2026-07-10** as a separate, still-open confound specific to the
old-vs-new-digest comparison (not the run25-vs-C2 comparison, which is a clean same-digest,
same-oracle, formula-only difference).

**Correcting an undercount before designing the ablation.** Implication #1 (§60.16) described
Formula B as differing from C2 in "two respects" (`cost_coef` magnitude/units, raw-binary `de`/`be`
vs `enhancement_credit()`). There is actually a **third**: Formula B's `user_intent = (0.50*ga +
0.50*ra) * 0.30` (additive, no gate) vs C2's `ga`-only gate penalty (`-0.10 if ga<0.5 else 0.0`,
`ra` removed entirely). §52-54's metric-differentiation analysis already found `ga`/`ra` near-zero
discriminative signal under earlier formula versions (`ga` SNR=0.03, `ra` ~97% constant) — a reason
to *deprioritize*, not ignore, this third difference; a discrete gate vs. a smooth additive term
can still behave differently for the minority of articles where `ga` actually crosses 0.5, and this
hasn't been directly tested.

### Stage 0 — free diagnostics, zero GPU / zero new API calls, do first

Reuses `sweep_reward_formula.py` / `model_gate_candidates.py` / `analyze_metric_differentiation.py`
(all already built, already proven at recomputing signal-quality metrics from already-graded data):

0.1. Re-verify the 3-way formula diff directly against the shipped `_section_reward` code and the
     `bases_ORACLE_BACKUP_20260708_231117` reconstruction, to confirm there are exactly 3 differences,
     not more (a quick correctness check before designing any ablation around it).
0.2. For each of the 3 differences **individually and in combination** (2³=8 cells, reusing
     `sweep_reward_formula.py`'s variant-recompute pattern on existing graded data, zero new
     generation), recompute `sigma_floor_fraction`, mean/median margin, `advNorm`, and the
     constant-predictor baseline (strict + near-tie, per §60.12's baseline-relative methodology) —
     isolates *which* mechanical change drives the 22%→0.6-7% `sigma_floor_fraction` gap, and
     whether it's mostly the two "bluntness" mechanisms §60.6 already suspected.
0.3. Diff `oracle_arm` assignments directly, per-article, between C2 and true-Formula-B on the
     already-available data (`diff_oracle_regen.py`-style) — quantifies how many of the 40
     articles' *labels* actually differ, not just their margins. Distinguishes "Formula B assigns
     different (better-generalizing) decisions" from "same decisions, just cleaner separation."
0.4. Cross-reference with the TEST articles where Formula-B-trained checkpoints (`run13`/`run25`)
     get it right and C2-trained checkpoints don't (already have both `_summary.json`s) — for
     those specific articles, check whether the Formula-B vs. C2 oracle labels actually differ. If
     they don't, credit goes to signal-quality/trainability, not label correctness.

**Stage 0 results (2026-08-03) — executed.** Extended `model_gate_candidates.py` (already designed
for exactly this kind of candidate-formula modeling) with two new toggles: `raw_de_be` (bypass
`enhancement_credit()` and use the plain grader score for `de`/`be`, regardless of whether tag
metadata exists) and `cost_units` (per-candidate override of the cost term's per-arm multiplier, so
the ordinal `{skip:0,light:1,standard:2,deep:3}` mechanism can be tested alongside H0's empirical
units). Added a clean 2×2×2 factorial (`S61_C2_baseline`, `S61_cost_only`, `S61_debe_only`,
`S61_gara_only`, plus the 3 pairwise + all-three cells) holding the two non-varied dimensions at
C2's exact production values, so each cell isolates exactly one/two of the three real differences.

**0.1 — formula reconstruction verified, but bit-exact backup matching is not possible (a 4th,
newly-discovered confound).** Hand-computed sanity checks (plugging known `cc/fl/de/be/cp/ga/ra/nr`
values through the new candidate code and verifying by arithmetic) confirm the 3-way reconstruction
is implemented correctly. A bit-exact check against `bases_ORACLE_BACKUP_20260708_231117`'s actual
saved rewards was attempted and **failed** (differences up to 0.52 on individual arms,
`06_tools__var_standard`) — traced to the episode grading data itself having been regenerated since
the 2026-07-08 backup (`episodes/06_tools__var_standard__preset0/reasoning.json` is dated
2026-07-15, a week later). **This means the true-Formula-B "as-shipped" result and every fresh
recompute in this document are not just formula-different but also grading-snapshot-different** —
a 4th confound (beyond digest, oracle-formula, and now grading-snapshot drift) that was silently
present in every historical-vs-fresh comparison this session. It does not undermine the Stage 0.2
factorial below (all 8 cells use today's grading data consistently, so the *relative* comparison
between them is clean), but it does mean §60.6's exact historical numbers (floor%=7.0%, TRAIN dist
8/10/3/3) cannot be reproduced from today's data even with a perfect formula reconstruction.

**0.2 — cost mechanism is overwhelmingly the dominant lever, but at a real deep-scarcity cost.**
TRAIN `floor%` (n=171 sections, lower is more decisive):

| candidate | floor% | mean margin | advNorm | TRAIN art dist (sk/li/st/dp) | thin articles |
|---|---|---|---|---|---|
| `S61_C2_baseline` (= production C2) | 20.5% | 0.0942 | 1.203 | 3/11/4/**6** | 9 |
| `S61_cost_only` | **4.1%** | 0.1031 | 1.266 | 8/12/2/**2** | 2 |
| `S61_debe_only` | 12.9% | 0.1661 | 1.246 | 1/10/6/**7** | 5 |
| `S61_gara_only` | 17.5% | 0.0986 | 1.200 | 4/11/4/**5** | 9 |
| `S61_cost_debe` | **0.0%** | 0.1732 | 1.334 | 3/13/6/2 | 7 |
| `S61_cost_gara` | 4.7% | 0.1076 | 1.262 | 8/11/2/3 | 6 |
| `S61_debe_gara` | 11.7% | 0.1684 | 1.248 | 1/10/6/7 | 6 |
| `S61_all_three_C2weights` | **0.0%** | 0.1750 | 1.334 | 3/13/7/1 | 9 |
| `S61_TRUE_FORMULAB_EXACT` (real weights) | 0.0% | 0.1306 | 1.331 | 6/14/4/**0** | 8 |

The cost mechanism alone closes **80% of the total floor% gap** (20.5%→4.1%, a 16.4pp drop out of
20.5pp available), `de`/`be` shape alone closes **37%** (20.5%→12.9%), and `ga`/`ra` treatment alone
closes only **15%** (20.5%→17.5%). `cost_debe` alone already reaches `floor%=0.0%`, matching
all-three exactly — **`ga`/`ra` treatment's marginal contribution to signal-quality is essentially
zero once cost and `de`/`be` are both changed**, consistent with §52-54's near-zero-SNR finding for
`ga`/`ra` and confirming it as the lowest priority of the three, quantitatively this time.

**But the cost mechanism is also the single biggest driver of deep-scarcity**, the exact failure
mode the whole H0/G0/J0/C2 arc was built to fix: `cost_only`'s TRAIN deep count drops to **2** (from
C2's 6) — worse than `debe_only`, which actually *improves* deep-representation slightly (6→**7**).
`TRUE_FORMULAB_EXACT` (all three combined, real weights) has **zero** deep articles in TRAIN. This
is a genuine, sharp tradeoff for Stage 1 to resolve empirically: the lever that fixes signal-quality
the most is also the one most likely to reintroduce the problem C2 exists to solve.

**0.3/0.4 — oracle labels change dramatically, not just margins: 13/24 TRAIN (54%) and 13/16 TEST
(81%) articles flip to a different `oracle_arm` under at least one of these formula variants.**
Comparing C2 directly against the full `TRUE_FORMULAB_EXACT` formula on TEST specifically, **5 of 16
articles get a genuinely different oracle label**: `07_reasoning_planning` (deep→skip),
`14_agent_system_design` (standard→light), `Dark_Dimension` (deep→light), `Distinct_AI_Models`
(deep→light), `Earth_Oceans_Origin` (deep→standard) — all Formula B pulling the label *down* from
C2's more escalation-heavy assignment. This is real evidence against the "same decisions, just
cleaner margins" framing (H2 alone) — Formula B is assigning **materially different decisions** for
the majority of articles, so the content-correctness channel (H1) is very plausibly a real,
independent contributor, not merely a signal-quality artifact. (3 TEST articles — `29_evaluation_
metrics`, `Insects_Consciousness`, `Understanding_Reasoning_LLMs` — agree across every variant
tested, including the full swap; these are not informative for attributing the gap.)

**Revised priority for Stage 1, given these results:** run `run26_costcoef_only` first — it has the
largest, most decisive signal-quality effect by far — but track TRAIN/TEST deep-representation and
arm balance explicitly alongside accuracy, not just accuracy alone, since this is also the variant
most likely to reintroduce severe deep-scarcity. If `run26` shows a real TEST gain, the open
follow-up question becomes whether that gain is *worth* the deep-scarcity cost, or whether
`run27_debecurve_only` (smaller signal-quality gain, but neutral-to-positive on deep-representation)
is the better production candidate despite a smaller raw floor%-improvement. `run28_garatreat_only`
remains lowest priority — 0.2 confirms its marginal contribution is negligible once the other two
are addressed.

### Stage 1 — single-variable incremental retraining ablation (real GPU jobs, sequential, handed off one at a time)

Unlike `run25` (all 3 Formula-B differences at once), introduce them **one at a time** onto
`run20_c2`'s exact recipe, so each run's marginal TEST-generalization delta is attributable:

1.1. `run26_costcoef_only` — C2 + Formula-B's `cost_coef` (`-0.06`, ordinal `nr` units) only.
1.2. `run27_debecurve_only` — C2 + Formula-B's raw-binary `de`/`be` (no `enhancement_credit()`)
     only, `cost_coef` stays at C2's `-0.03` H0 units.
1.3. `run28_garatreat_only` (lower priority per the SNR finding above, but still worth confirming
     empirically) — C2 + Formula-B's additive `(0.5*ga + 0.5*ra) * 0.30` term instead of the
     `ga`-gate, everything else C2.

Priority ordering of 1.1/1.2/1.3 should be set by Stage 0.2's factorial results — whichever single
change moves `sigma_floor_fraction`/margin the most is the best first candidate to also check for
real TEST impact. **Methodological notes carried forward from §60.16:** expect early entropy
collapse regardless of which variant is tested (§60.8's broad-based, dataset-size-driven mechanism,
not formula-specific) — do not kill a run just because it collapses early; track real TEST-set
RL-only accuracy across the run (not just the health-gated ceiling) and cap around epoch 120-150
per the confirmed post-114 drift in `run25`.

#### Stage 1 execution and results (2026-08-03 to 2026-08-06)

**Stage 1 built and handed off (2026-08-03).** `training/build_s61_diag_bases.py` (new, reuses
`model_gate_candidates.py`'s corpus loader + the `S61_*` candidate functions directly, zero new
generation) writes 3 isolated bases roots for the 24 TRAIN articles — `bases_S61_COSTONLY_DIAG/`,
`bases_S61_DEBEONLY_DIAG/`, `bases_S61_GARAONLY_DIAG/` — each pairing today's unchanged
`research_digest.md`/`guideline_features.json` with a freshly-computed `section_oracle.json` (v5
schema) under exactly one isolated formula difference. Verified 72/72 (24 articles × 3 candidates)
built via `--dry-run` then for real; spot-checked schema/content of one output file. Launch
commands (identical to `run25`'s recipe except `--task-id`/`--bases-dir`, run **sequentially, one
GPU job at a time**, priority order set by Stage 0.2):

```bash
cd /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training

# Priority 1 — biggest signal-quality lever, but watch deep-representation closely (§61 Stage 0.2)
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run26_costcoef_only --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  --bases-dir ../../rl_training_data/bases_S61_COSTONLY_DIAG \
  > ../../rl_training_data/checkpoints/tasks/run26_costcoef_only_stdout.log 2>&1 &

# Priority 2 — smaller signal-quality gain, but neutral-to-positive on deep-representation
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run27_debecurve_only --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  --bases-dir ../../rl_training_data/bases_S61_DEBEONLY_DIAG \
  > ../../rl_training_data/checkpoints/tasks/run27_debecurve_only_stdout.log 2>&1 &

# Priority 3 (lowest) — Stage 0.2 showed ~zero marginal signal-quality contribution once cost+de/be
# both change; run mainly to confirm it doesn't matter for real TEST accuracy either
PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run28_garatreat_only --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  --bases-dir ../../rl_training_data/bases_S61_GARAONLY_DIAG \
  > ../../rl_training_data/checkpoints/tasks/run28_garatreat_only_stdout.log 2>&1 &
```

**What to watch, per §60.16's methodological carryover:** expect early entropy collapse regardless
of variant (§60.8's broad, dataset-size-driven mechanism, not formula-specific) — do not kill a run
just because it collapses early. Track real TEST-set RL-only accuracy (via `infer.py`'s
`_DEFAULT_ADAPTER_DIR` pointed at the resulting `best`/`best_er` checkpoint + `test_grok_planner.py
--rl-only --save-json`, exactly as done for `run25` — no `--bases-dir` override needed at *eval*
time, since production `bases/` already holds the correct current digests/oracle for scoring) at
several checkpoints spanning ~epoch 100-150, not just the health-gated ceiling. Also inspect each
run's TRAIN arm distribution (`training_log.jsonl`) for deep-representation collapse, per Stage
0.2's warning that `run26_costcoef_only` in particular is the variant most likely to reproduce it.
Cap around epoch 120-150 given the confirmed post-114 drift pattern in `run25` — kill early once the
entropy/accuracy trajectory is clear, same discipline used for `run22`/`run23`.

**`run26_costcoef_only` interim results (2026-08-04) — best TEST result yet among any
new-digest, trained-from-scratch run.** Still running (PID confirmed alive, epoch 163/200 logged as
of this check, `patience=50` not yet triggered since `best_er` last improved at epoch 146). TRAIN
metrics have plateaued/oscillated without a clear trend since roughly epoch 130-140 (strict
top1 0.71-0.78, near-tie 0.92-0.94) — already past the recommended epoch 120-150 cap, worth a kill
decision now rather than waiting for `patience`/epoch 200.

*Health-gated ceiling, baseline-corrected:* entropy oscillates the same way run13/run25 did (spikes
to 0.43-0.46 around epoch 9-10, brief secondary bumps through epoch 20-34, then settles into an
unhealthy 0.02-0.05 band from ~epoch 40 onward) — 15 healthy epochs (entropy≥0.15) logged so far.
Health-gated strict ceiling = **38.0%** at epoch 34, near-tie ceiling = **60.8%** — both *look*
dramatically higher than every prior run (25.7-28.1% strict, C2-era) but this run's own
constant-predictor baseline (computed directly from `bases_S61_COSTONLY_DIAG`'s section-level
labels, section dist sk/li/st/dp=65/71/22/13) is **41.5% strict / 71.4% near-tie** ("always predict
`light`") — **both ceilings are still below their own label set's trivial baseline**, extending
§60.12's invariance finding to this formula variant too: no run has yet demonstrated genuinely
above-baseline learning while entropy is healthy, regardless of which of the 3 formula differences
is isolated.

*Real TEST result — **corrected checkpoint attribution (2026-08-04): the first eval below is
epoch 159, not epoch 146** (user directly ran both and compared; my mtime-based attribution to
epoch 146 was wrong — "`best`" evidently mirrors `best_strict`, which last updated at epoch 159,
not `best_er`). Both checkpoints run via `test_grok_planner.py --rl-only --save-json`, verified
from `grok_planner_test_results/_summary.json`:*

| run (TEST, RL-only) | exact | near | miss | MAE | regret mean |
|---|---|---|---|---|---|
| true zero-retrain baseline (§60.16/17) | 38% (6/16) | 7 | 19% (3) | 0.812 | 0.0177 |
| `run25` @ epoch 114 (best) | 38% (6/16) | — | 12% (2) | 0.750 | 0.0219 |
| `run26_costcoef_only` @ **epoch 159** ("best") | 50% (8/16) | 5 | 19% (3) | 0.6875 | 0.0129 |
| **`run26_costcoef_only` @ epoch 146** | **50% (8/16)** | **6** | **12.5% (2)** | **0.625** | **≈0.0129** |

The only difference between epoch 146 and 159: `07_reasoning_planning` (oracle=skip) is predicted
`light` at epoch 146 (near) vs. `standard` at epoch 159 (miss) — one article moving from a 2-level
miss to a 1-level near accounts for the entire delta (miss 3→2, MAE 0.6875→0.625, regret_mean
essentially unchanged since regret is reward-based not preset-distance-based). **Epoch 146 is
therefore the better of the two, and now the best real TEST result across every metric of any
from-scratch retrain on the new digests** — beating `run25` and the true zero-retrain baseline on
`exact%`, `miss%`/`MAE` (tied with `run25`'s miss-rate, better MAE), and `regret_mean`. This
isolates only the cost mechanism, not the full 3-way Formula-B swap — a genuinely important,
somewhat surprising result suggesting `cost_coef` alone may be doing most of Formula-B's real
generalization benefit, with the other two differences (`de`/`be` shape, `ga`/`ra` treatment)
adding little beyond it, or even mildly diluting it (epoch 159, later in training, is *worse* than
146 on the one article that differs — consistent with continued drift past the best point, not
further improvement).

**But the deep-scarcity tradeoff flagged in Stage 0.2 shows up concretely in these predictions.**
Of the 3 TEST articles with a `deep` oracle label, `run26` gets only 1 right (`Dark_Dimension`,
exact) and misses the other 2 by predicting `light` instead of `deep` (`13_agent_framework`,
`Distinct_AI_Models` — 2 of the remaining 2 misses at epoch 146). The miss set also changed
composition vs. the zero-retrain baseline: `run26` *fixes* `Dark_Dimension` and `29_evaluation_
metrics` (both correct now) and, at epoch 146, avoids the `07_reasoning_planning` miss too — but
keeps `Distinct_AI_Models`, and the higher exact% overall comes from several NEAR articles flipping
to EXACT, not from fixing the deep-scarcity-driven misses specifically.

**Recommendation: kill `run26_costcoef_only` now — agreed with the user's read.** TRAIN has been
plateaued/oscillating since ~epoch 130-140 with no further improvement (epoch 159 is measurably
*worse* than epoch 146 on the one TEST article that moved), the epoch 120-150 cap is already
exceeded, and `patience` won't fire until ~epoch 196 — continuing would spend real GPU time with no
evidence of further gains, exactly the pattern that justified killing `run22`/`run23` early.
Epoch 146's checkpoint is safely preserved in dedicated per-epoch snapshots (`best_er_epochs/
epoch_0146`, `best_neartie_epochs/epoch_0146`), so nothing is lost by stopping now — it is not at
risk of being overwritten. Kill and free the GPU for `run27_debecurve_only` (next priority):

```bash
kill 55407 55410   # uv wrapper + actual train_grpo.py process for run26_costcoef_only
```

`run26_costcoef_only`'s final, representative result for §61 Stage 2/3 going forward: **epoch 146,
exact=8/16 (50%), near=6, miss=2 (12.5%), MAE=0.625, regret_mean=0.0144** — the best TEST result of
the investigation so far, from isolating cost_coef alone.

**`run27_debecurve_only` interim results (2026-08-05) — decisively worse than `run26`, and a
different failure mode entirely.** Still running (epoch 134/200 logged; `sigma_floor_fraction`
constant at 0.1287 every epoch, matching Stage 0.2's `debe_only` prediction of 12.9% exactly).
TRAIN has plateaued/oscillated since ~epoch 90-134 (strict 0.44-0.64, near-tie 0.75-0.83, `best_er`
last improved at epoch 110, `patience` won't fire until ~epoch 160).

*Health-gated ceiling, baseline-corrected:* only 23/135 healthy epochs — strict ceiling 32.2% @
epoch 20 (below this run's own label-set baseline of 38.6% "always `light`", consistent with the
invariance pattern), but near-tie ceiling 58.5% @ epoch 20 is *slightly above* its own 54.4%
baseline — the first modest exception to the below-baseline pattern seen so far, though small
(4 points) and single-metric; not treated as a reversal of §60.12's finding.

*Real TEST result (checkpoint = epoch 110, the `best_er` tracker, matching the user's attached
eval — same convention as `run25`/`run26`):*

| run (TEST, RL-only) | exact | near | miss | MAE | regret mean |
|---|---|---|---|---|---|
| **`run26_costcoef_only` @ epoch 146** | **50% (8/16)** | 6 | **12.5% (2)** | **0.625** | **0.0144** |
| `run27_debecurve_only` @ epoch 110 | 25% (4/16) | 6 | 38% (6) | 1.250 | 0.0231 |

`run27` is worse than `run26` on every metric — half the exact rate, 3× the miss rate, 2× the MAE.
TRAIN tells the same story (`run27`: exact=25%, miss=25%, MAE=1.125 vs. `run26`: exact=46%,
miss=8%, MAE=0.625) — this is not TEST-specific overfitting, `run27`'s checkpoint is uniformly
worse.

**The failure mode is different from — almost opposite to — `run26`'s deep-scarcity risk.**
`run27` predicts `deep` for 7 of 16 TEST articles (44%) against a true oracle rate of 19% (3/16) —
systematic *over*-prediction of `deep`, not under-prediction. Plausible mechanism: raw
(pre-`enhancement_credit()`) `de`/`be` scores have no saturating ceiling dampening marginal
exploration credit, so any article with moderately decent depth/breadth content mechanically
inflates the `deep`/`standard` arms' explore term — teaching the model deep is often the right
call far more often than the label distribution (or reality) supports. This is a genuinely
different, novel failure mode from `run26`'s (which under-predicts `deep` instead) — both single-
variable changes distort the deep-prediction rate, just in opposite directions.

**Recommendation: kill `run27_debecurve_only` now too — agreed with the user's read.** Same
justification as `run26`: TRAIN plateaued, past the epoch cap, no evidence of further gains, and
the result is already decisively resolved (worse on every metric, at both TRAIN and TEST). This is
now two-for-two evidence that isolating `cost_coef` alone is the dominant, load-bearing lever for
real TEST generalization — `de`/`be` shape alone does not confer the benefit and actively hurts.
Given `run28_garatreat_only`'s predicted near-zero marginal signal-quality contribution (Stage 0.2)
and unchanged deep-representation (neither failure mode expected), it is now a lower-value
confirmatory experiment rather than a live open question — worth discussing whether to still run
it for completeness or move directly to Stage 2/3 with `run26`'s result as the leading candidate.

```bash
kill 67743 67762   # uv wrapper + actual train_grpo.py process for run27_debecurve_only
```

**`run28_garatreat_only` results (2026-08-06) — Stage 1 complete.** User ran this one to
completion-for-completeness, observed the same plateau pattern, killed it, and evaluated the best
checkpoint directly (no further handoff needed for this one). Trajectory confirms the pattern seen
in `run26`/`run27`: 139 epochs logged, `sigma_floor_fraction` constant at **0.1754** (matches Stage
0.2's `gara_only` prediction of 17.5% almost exactly), only 24/139 healthy epochs, health-gated
ceiling strict=26.3%/near-tie=48.5% @ epoch 21-23 — both *below* this run's own label-set baseline
(computed from `bases_S61_GARAONLY_DIAG`: 32.75% strict / 59.65% near-tie, "always `light`"),
consistent with the invariance pattern (no exception this time, unlike `run27`'s near-tie case).
`best_er` peaked at epoch 120 (TRAIN plateaued 0.62-0.70 strict from there through epoch 138,
matching the user's observation).

*Real TEST result (checkpoint = epoch 120, `best_er`):* exact=38% (6/16), near=4, miss=38% (6),
MAE=1.125, regret_mean=0.0257, regret_max=0.1273.

**Stage 1 complete — full comparison, all 3 single-variable isolations plus reference points:**

| run | isolates | exact | near | miss | MAE | regret mean | TEST `deep` predictions (true rate 19%, 3/16) |
|---|---|---|---|---|---|---|---|
| true zero-retrain baseline | — | 38% (6) | 7 | 19% (3) | 0.812 | 0.0177 | — |
| `run25_formulab_diag` @ ep114 | all 3 (full swap) | 38% (6) | — | 12% (2) | 0.750 | 0.0219 | — |
| **`run26_costcoef_only` @ ep146** | **cost mechanism only** | **50% (8)** | 6 | **12.5% (2)** | **0.625** | **0.0144** | 6% (1) — under-predicts |
| `run28_garatreat_only` @ ep120 | `ga`/`ra` treatment only | 38% (6) | 4 | 38% (6) | 1.125 | 0.0257 | 50% (8) — over-predicts most |
| `run27_debecurve_only` @ ep110 | `de`/`be` shape only | 25% (4) | 6 | 38% (6) | 1.250 | 0.0231 | 44% (7) — over-predicts |

`run26_costcoef_only` is decisively the best of all three isolated variants, and the best result of
the entire investigation — beating even `run25`'s full 3-way swap. `run27` and `run28` are both
clearly worse than the zero-retrain baseline on every metric; only `run26` beats it outright.

**A coherent mechanistic story emerges from the deep-prediction bias direction.** All three
single-variable variants distort the `deep`-prediction rate away from truth (19%), but in a
pattern that implicates the cost mechanism specifically as the thing that suppresses over-eager
escalation: when `cost_coef` itself is changed to Formula-B's blunter form (`run26`), the model
*under*-predicts `deep` (6%). When `cost_coef` is left at C2's shipped, milder form and *either*
other dimension changes instead (`run27`'s raw `de`/`be`, `run28`'s additive `ga`/`ra`), the model
swings the *other* way and *over*-predicts `deep` (44-50%) — worse than either C2 or Formula-B's
full swap. This suggests C2's cost mechanism alone is not sufficient to keep escalation in check
once other reward terms shift even slightly toward rewarding effort more freely (raw `de`/`be`'s
uncapped credit, or `ga`/`ra`'s unconditional additive bonus) — and that Formula-B's *specific*
cost magnitude/units are doing real, load-bearing suppression work, not just contributing "noise
reduction" as the Stage 0 signal-quality framing alone would suggest.

**Stage 1 conclusion and recommended next step:** `cost_coef` (magnitude + unit shape, isolated in
`run26`) is the single dominant, load-bearing lever behind Formula-B's TEST-generalization
advantage — the other two differences do not contribute positively on their own and each
introduces a distinct, opposite-direction deep-prediction distortion when isolated. This sharpens
implication #1's original proposal (a real retrain of C2 with only `cost_coef` reverted) from a
hypothesis into the best-supported next step: proceed to Stage 2/3 by testing a **range of
`cost_coef` magnitudes** (not just Formula-B's `-0.06`/ordinal-units endpoint) against `run20_c2`'s
baseline, to find whether a smaller shift already recovers most of `run26`'s gain without its
milder deep-scarcity symptom (§60.16), rather than assuming `-0.06`/ordinal-units is itself the
optimal point on this lever.

### Stage 1 addendum — cost_coef magnitude preview (2026-08-06), before committing to another real retrain

Given Stage 1 established `cost_coef` as the dominant lever, the natural next question is whether
Formula B's exact endpoint (`-0.06`, ordinal units) is the best point on that lever, or whether a
smaller shift already captures most of the benefit with less deep-scarcity cost. Extended
`model_gate_candidates.py` with a `cost_coef` magnitude sweep (`-0.035` through `-0.06`, in `0.005`
steps) under two unit conventions: **H0** (production's own empirical units, only the coefficient
scaled — matching the "C2 + a larger `cost_coef`" framing exactly) and **ORD** (ordinal units too,
for comparison against `run26`'s exact mechanism at smaller magnitudes). Zero new generation,
reuses Stage 0's corpus loader.

**TRAIN floor% and deep-representation across the sweep (H0 units, C2 shape otherwise unchanged):**

| cost_coef | floor% | mean margin | TRAIN dist (sk/li/st/dp) | thin |
|---|---|---|---|---|
| `-0.03` (C2 baseline) | 20.5% | 0.0942 | 3/11/4/**6** | 9 |
| `-0.035` | 19.9% | 0.0946 | 5/12/3/**4** | 9 |
| `-0.04` | 20.5% | 0.0952 | 6/12/2/**4** | 8 |
| `-0.045` | 21.1% | 0.0958 | 7/12/2/**3** | 9 |
| `-0.05` | **8.2%** | 0.0968 | 7/12/2/**3** | 6 |
| `-0.055` | 8.8% | 0.0979 | 7/12/2/**3** | 4 |
| `-0.06` (H0 units) | 8.2% | 0.0992 | 8/11/2/**3** | 4 |
| `-0.06` ordinal units (`run26`'s exact mechanism) | 4.1% | 0.1031 | 8/12/2/**2** | 2 |

**Key finding: the tradeoff is not a smooth curve — there's a sharpness cliff between `-0.045` and
`-0.05`, and `-0.045` specifically lands in the worst spot on both axes.** `floor%` barely moves
(20.5%→19.9%→20.5%→21.1%) from `-0.03` through `-0.045` — no real signal-quality gain yet — while
deep-representation has *already* dropped from 6 to 3 by `-0.045`. The floor% benefit only actually
appears at `-0.05` (a sudden drop to 8.2%, matching `-0.06`'s H0-unit value almost exactly) — by
which point deep-representation is unchanged from `-0.045` (still 3). **`-0.045` therefore buys
none of the signal-quality benefit while already paying essentially all of the deep-scarcity cost
`-0.05`/`-0.06` pay** — it is not the good middle-ground the "smaller than `-0.06`" framing
suggested. `-0.05`, `-0.055`, and `-0.06` (H0 units) are all roughly equivalent to each other on
both floor% (8.2-8.8%) and deep-count (3) — the benefit plateaus well before `-0.06`, so nothing is
gained by going all the way there under H0 units specifically.

The ORD-units comparison (secondary, not the primary recommendation since it changes two things at
once) shows the same cliff arriving earlier — around `-0.04`, not `-0.045`-`-0.05` — consistent
with ordinal units applying a proportionally larger penalty at `standard`/`deep` than H0's units at
the same nominal coefficient.

**Recommendation: `-0.05` (H0 units), not `-0.045`, for the next real retrain.** It is the smallest
magnitude that captures essentially all of the achievable floor%-sharpening benefit (8.2%, tied
with `-0.06`) while sitting at the same deep-representation (3) as every value from `-0.045`
onward — a strictly better choice than `-0.045` (no signal benefit yet, same deep cost) and
equivalent to `-0.06` (H0 units) at a smaller departure from production. It won't fully match
`run26`'s ordinal-units result (4.1% floor%, deep=2) since that mechanism is sharper still, but it
tests whether the H0-unit-only lever alone, at its plateau point, recovers a useful fraction of
`run26`'s real TEST gain without needing the ordinal-unit switch too.

**Built and ready:** `training/build_s61_diag_bases.py --candidates S61_cost05_H0` (new candidate
added alongside the existing three) → `rl_training_data/bases_S61_COST05_DIAG/`, verified 24/24
TRAIN articles built. Launch command (identical recipe, new `--bases-dir`):

```bash
cd /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/training

PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True nohup uv run python train_grpo.py \
  --task-id run29_costcoef05 --epochs 200 --lr 5e-5 --beta 0.15 --entropy-coef 0.22 \
  --warmup-epochs 10 --patience 50 --lora-r 16 --lora-alpha 16 --lora-dropout 0.05 \
  --granularity section --section-weight hybrid --inv-freq-temp 0.5 \
  --bases-dir ../../rl_training_data/bases_S61_COST05_DIAG \
  > ../../rl_training_data/checkpoints/tasks/run29_costcoef05_stdout.log 2>&1 &
```

Same monitoring discipline as Stage 1: expect early entropy collapse, track real TEST accuracy at
several checkpoints (not just the health-gated ceiling), and cap around epoch 120-150.

#### `run29_costcoef05` result (2026-08-07): the milder H0-unit lever does NOT recover `run26`'s gain

User ran `run29_costcoef05` to completion, observed a plateau, killed it, and ran RL-only inference
on the `best_er` checkpoint (epoch 94 — the single all-time-peak `mean_expected_reward`, 0.4027,
confirmed directly from `training_log.jsonl`; no other epoch in the 136-epoch log reaches it).

**Training dynamics**, read directly from `training_log.jsonl` (136 epochs logged): `sigma_floor_fraction`
is **constant at 0.0819 (8.19%) every single epoch** — matching the Stage 1 addendum's zero-cost
preview prediction (8.2%) almost exactly, a nice validation that the preview methodology transfers
to the real training run. Entropy shows the now-familiar shape: healthy (≥0.15) through epoch 22
(with one brief dip at epoch 16), then **permanently collapses starting epoch 23** and never
recovers above ~0.07 for the remaining 113 epochs — the earliest sustained collapse of any Stage 1
run so far (`run26`/`run27`/`run28` all stayed healthy into the high-20s/30s). Health-gated ceiling
= 33.9% strict / 54.97% near-tie @ epoch 21-22 — computed this run's own constant-predictor
baseline directly from `bases_S61_COST05_DIAG`'s 171 TRAIN sections (dist skip51/light61/standard31/deep28,
"always light" baseline = **35.7% strict / 83.6% near-tie(±1)**) — the health-gated ceiling sits
*below* its own baseline on both metrics, extending §60.12's invariant (no run has ever beaten its
own trivial constant-predictor baseline while genuinely healthy) to this candidate too. TRAIN
plateaued in a narrow `mean_expected_reward` band (0.399-0.403) for the last ~40 logged epochs
(92-135) with no clear trend, confirming the user's "plateaued" read and justifying the kill.

**Real TEST/TRAIN result vs. every reference point to date:**

| | exact | near | miss | MAE | regret_mean | regret_max |
|---|---|---|---|---|---|---|
| zero-retrain baseline (`run13_formulaB/best`, new digests) | 38% (6/16) | 44% | 19% (3/16) | 0.812 | 0.0177 | — |
| `run26_costcoef_only` (`-0.06`, **ordinal** units) @ep146 | **50% (8/16)** | 37.5% | **12.5% (2/16)** | **0.625** | **0.0144** | **0.0652** |
| `run27_debecurve_only` @ep110 | 25% (4/16) | 37.5% | 38% (6/16) | 1.250 | 0.0231 | 0.0926 |
| `run28_garatreat_only` @ep120 | 38% (6/16) | 25% | 38% (6/16) | 1.125 | 0.0257 | 0.1273 |
| `run25_formulab_diag` (full 3-way swap) @ep114 | 38% (6/16) | — | 12% (2/16) | 0.750 | 0.0219 | — |
| **`run29_costcoef05` (`-0.05`, H0 units) @ep94** | 44% (7/16) | 31% (5/16) | 25% (4/16) | 0.812 | 0.0194 | 0.1273 |

`run29` underperforms `run26` on **every single metric** — lower exact%, lower near%, more than
double the miss rate, 30% worse MAE, 35% worse mean regret. Against the zero-retrain baseline it is
roughly a wash: identical MAE, a modestly better exact% (44% vs 38%) offset by a worse miss rate
(25% vs 19%) and worse mean regret (0.0194 vs 0.0177). TRAIN (n=24): exact=46%, near=46%, miss=8%,
MAE=0.625, regret_mean=0.0113 — solid but, per this investigation's established discipline, not
informative on its own about generalization.

**Failure mode — a clean, bimodal light↔deep confusion, unlike any single-variable run so far.**
All 4 TEST misses are *exactly* the P1(light)↔P3(deep) two-level axis, split evenly by direction:
`13_agent_framework` and `Distinct_AI_Models` under-predict (true `deep`, predicted `light`, mirroring
`run26`'s under-escalation tendency); `Bird_Eye_Extreme` (regret **0.1273**, the run's `regret_max`,
predicted at 61% confidence) and `Space-Time_QECC` over-predict (true `light`, predicted `deep`,
mirroring `run27`/`run28`'s over-escalation tendency). Zero misses involve `skip` or `standard` —
every `standard`-oracle TEST article (5 of them) lands on an exact hit or a 1-level near, never a
miss, and `standard` itself is under-*represented* in predictions (2/16 vs. true 5/16) without ever
causing an outright error. The model also never predicts `skip` anywhere (0/16 TEST, 0/24 TRAIN),
matching a tendency seen since the C2 era, though it costs no regret here (the 2 TEST skip-oracle
articles are either policy-forced or land as a 1-level near).

**Interpretation — this closes the "milder lever" question negatively.** `run29` directly answers
the question the addendum posed: does the H0-unit-only magnitude increase (no ordinal-unit switch)
recover a useful fraction of `run26`'s gain? **No.** It performs worse than `run26` on every metric
and no better than doing nothing. This means Formula B's **ordinal unit convention itself**
(`{skip:0,light:1,standard:2,deep:3}`), not just the larger `cost_coef` magnitude, is doing real,
load-bearing work — consistent with the empirical-cost-ratio finding (§"EMPIRICAL COST SIGNAL
FOUND", 2026-07-25) that H0's units are *shaped* by diminishing real exploration effort
(`light:1.00 → standard:1.88 → deep:2.31`, a shrinking marginal step), so scaling the coefficient up
within H0 units still leaves the `standard→deep` cost step proportionally small (~23%) — it sharpens
overall margin decisiveness (the sigma_floor cliff) without specifically discouraging escalation past
`standard` the way ordinal units' constant per-round step (`+1` every time, a full 50% relative
jump from `standard→deep`) does. **`run26`'s ordinal-unit mechanism remains the best-validated,
leading candidate from Stage 1** — this result does not unseat it, and Stage 2/3 should proceed with
`run26`'s exact mechanism rather than investigating further intermediate H0-unit magnitudes.

### Stage 2 — content-correctness vs. signal-quality disentanglement

2.1. For whichever Stage 1 run(s) show a real TEST improvement over `run20_c2`, repeat Stage
     0.3/0.4's label-diff check for that specific variant — if the TEST improvement correlates with
     genuinely *different* label assignments on the articles that matter, that's evidence for
     "more correct decisions."
2.2. If a run improves signal-quality *without* materially changing which articles get which
     label, and still improves TEST — that's evidence for a pure trainability/SNR channel,
     independent of content correctness (a real, somewhat surprising finding if confirmed, and
     exactly the tension §60.15 already flagged but couldn't resolve with n=1).

### Stage 3 — consolidate and decide

3.1. Combine whichever single-variable change(s) show real, attributable TEST gains into one
     candidate formula, retrain, and re-check — components may compose or interact/cancel (§60.9
     already saw this with the cap-extension + `explore_mult` combination).
3.2. Re-validate the winning candidate against both baseline-relative signal-quality (§60.12) and
     real RL-only TEST metrics (§60.16/§60.17's corrected methodology) before shipping.
3.3. Only then proceed to Appendix A's 192-cycle replication spend (per implication #2) — avoids
     replicating labels under a formula that might get superseded shortly after.

**Priority note:** Stage 0 is free and should run immediately, before committing to any Stage 1
GPU job — it determines which of the 3 candidate single-variable runs to prioritize given only one
GPU job runs at a time. This mirrors the "free diagnostic before expensive experiments" discipline
that already paid off in §60.8/§60.12.

# Appendix A — The data constraint: what to actually target, and how to carry out replication (2026-07-30)

**Scope:** §60.6's correction retired "sharpen the reward signal" as a north star (decisiveness
and correctness were shown to come apart). This appendix answers the follow-up: *what is the
primary data target, is it noise reduction, and if so how is replication actually carried out —
does it need new topics or just re-running the existing ones?* Planning document; nothing here
has been executed.

## A.1 Two different "noise" problems, routinely conflated

These need separating before the target can be chosen, because they have different causes,
different fixes, and different costs:

| | **Label noise** | **Sampling noise** |
|---|---|---|
| Question it corrupts | "Is *this* article/section's `oracle_arm` the right answer?" | "Is my 16-article TEST set representative enough to detect a real change?" |
| Measured at | §55.2: per-cell reward sd ≈ 0.099; arm-difference noise ≈ 0.140 | §13/§15: n=16, σ≈2 exact-hits, 56% majority-class baseline |
| Consequence | §55.3: **84% of sections' "winning" arm is not statistically distinguishable from a single-draw coin flip** | ±2 exact is within binomial noise — most candidate improvements are unmeasurable |
| Fixed by | **Replication** (re-run write+grade N times, average) | **More articles** (new topics) |
| *Not* fixed by | more articles | replication (40 replicated articles are still 40 articles) |

**Replication does not increase `n`, and new topics do not fix label precision.** They are
complements, not substitutes. Any plan that treats "more data" as one undifferentiated goal will
mis-sequence them.

## A.2 Which is primary, and for what

- **For TRAINING (what the model learns): label noise is binding.** §19 established the specific
  mechanism — unlike the RL folklore case where a noisy reward is resampled every visit and
  averages out, this pipeline computes each `(article, section, arm)` reward **once**, freezes it
  into `section_oracle.json`, and reuses it as a fixed target for every GRPO epoch. There is no
  resampling to average anything away. A model fitting a small set of frozen point-labels, a
  large fraction of which are single noisy draws, cannot distinguish generalizable signal from
  noise it should ignore — it memorizes both. That is exactly the overfitting + entropy-collapse
  signature seen in `run14`, `run20_c2`, and `run21_ecoef035`.
- **For EVALUATION (whether a change worked): sampling noise is binding.** Replicating the 16
  TEST articles makes each label more trustworthy but leaves `n=16` — the σ≈2 measurement floor
  that has blocked adjudicating every candidate improvement in this document stays exactly where
  it is.

**Primary target: label noise first, via replication.** Not because sampling noise matters less,
but because of ordering — adding more articles under the current labelling precision just
produces *more* articles whose labels are ~84% coin-flips. Label precision is a prerequisite for
the added articles to be worth what they cost.

## A.3 Why replication is the higher-leverage first move

1. **It is the only lever that moves the §55.3 numbers at all.** The `sigma_floor` sweep proved
   thresholds cannot help: the absolute count of statistically-defensible sections stayed flat at
   45/282 (>1 sd) and 10/282 (>2 sd) at *every* `sigma_floor` value tested — raising the floor only
   discarded training data. Averaging N draws cuts noise sd by `√N`, which moves the *threshold*,
   which is the only thing that can move those counts.
2. **It is much cheaper than it sounds, because it skips the expensive half of the pipeline.**
   Replication reuses each article's existing `research.md` / `.research/` — **zero** Tavily
   searches, zero Firecrawl scrapes, zero re-research. Only the write + grade steps re-run.
3. **The infrastructure already exists and has been validated end-to-end** (§23, §30-31) — see
   A.5.
4. **It improves the labels for articles we already paid the expensive research+GT cost on**,
   rather than paying that cost again for new topics.

Expected effect, using the measured numbers: arm-difference noise `0.140` (N=1) → `0.081` (N=3)
→ `0.063` (N=5). §55.3's own estimate is that N=3 would *roughly double* the fraction of sections
with a statistically defensible winner. Diminishing returns are steep after N=3 (N=5 buys another
~22% reduction for 67% more cost), so **N=3 is the sweet spot** unless A.7's validation says
otherwise.

## A.4 Do you need new topics? Not for this — but for the other two problems, yes

**For replication specifically: no new topics at all.** Replication is by definition re-running
the *existing* articles. No new guidelines, no new golden sources, no new
`article_ground_truth.md`, no new research phase.

New topics remain necessary for the *other* two data problems already documented in §16, neither
of which replication touches:
- **TEST-set expansion** (§16.1.1's arm × golden-type grid) — the `n=16` measurement floor, the
  empty `golden_web`-only cells at P0/P2/P3, and the thin P2/P3 cells (2 articles each).
- **TRAIN archetype gaps** (§16.1's Priority 2) — the "high-demand but golden-satisfiable → P1"
  lesson, and no-variant genuine P2/P3 examples to break the `var_demanding`→escalate confound.
  Note the current TRAIN set is 24 articles but only **8 genuinely independent topics** (each ×3
  correlated variants), so its effective sample size is far below 24 for any generalization claim.

Sequencing recommendation: **replicate what exists → re-measure → then expand.** Expansion is the
larger, slower spend and its value is easier to judge once labels are trustworthy.

## A.5 What already exists (verified on disk) vs. what is missing

**Already built and validated** — the §23 noise-experiment work generalizes directly:

| Component | Path | Role |
|---|---|---|
| Replicate-dir setup | `training/setup_noise_experiment.py` | Copies `article_guideline.md` + `research.md` + `.research/` into `rl_training_data/noise_experiment/<article>__replicateN__preset{p}/`. Never touches real `episodes/`; copies no `article.md`, so the writer runs fresh. |
| Low-temp writing profile | `writing_workflow/configs/rl_generation.yaml` | `write_article`/`integrate_exploration` at temp 0.25 (vs. `course.yaml`'s 0.7). Selected per-invocation via `CONFIG_FILE`; production config untouched. |
| Writer redirect | `rl_writing_generator.py --episodes-dir` | Points the generator at the replicate root. Default unchanged. |
| Grader redirect | `rl_grading_generator.py --episodes-dir --grading-model claude` | Same, plus `_strip_replicate_suffix()` resolves `__replicateN` back to the base article's ground truth — no GT duplication needed. |
| Noise measurement | `training/measure_replicate_noise.py` | Imports the production `_section_reward_components` / `_compute_r_w` (no duplicated formula), reports per-section per-arm sd, article margin distribution, arm vote tally. |
| Noise-floor estimate | `training/estimate_noise_floor.py` | Produced §55.2's `0.099` / `0.140` figures. |
| Margin tiering | `training/audit_oracle_margins.py` | CRITICAL/HIGH/MODERATE/COMFORTABLE tiers, correctly excluding policy-forbidden / manual-override articles. |
| Real replicate data | `rl_training_data/noise_experiment/` | **2 articles × 3 replicates × 4 arms already written and graded** (`09_RAG__var_standard`, `06_tools__var_standard`) — the basis for A.7's free validation. |

**The one genuine gap — there is no merge-back path.** Today the replicates are only *measured*;
they never become the production label. `generate_episode_oracles.py` reads exactly one
`reasoning.json` per episode directory, and §23's decision rule (`majority vote across draws`)
operates at the **article** level only — coarser than what training needs, since GRPO consumes
**section-level** rewards. Closing this needs a small new step:

> For each `(section, arm)`, average the per-draw reward components across the N replicates
> (plus the original production draw), and write the averaged values into `section_oracle.json`.
> Also worth storing the per-cell sd alongside, since it is exactly the per-label confidence
> measure A.8 wants — computing it is free once the draws are loaded.

This should be a **new, separate script** that consumes replicate dirs and emits an averaged
`section_oracle.json`, rather than a modification of `generate_episode_oracles.py` — keeping the
single-draw path intact preserves the ability to reproduce every historical label, which this
investigation has relied on repeatedly (most recently §60.6).

**DONE (2026-07-30):** built `training/merge_replicate_oracles.py`. For each `(section, arm)` cell
it averages the reward across every available draw — the original production draw already in
`section_oracle.json` plus every graded replicate under `noise_experiment/` (reusing
`measure_replicate_noise.py`'s exact recompute path, no formula duplication) — and writes
`bases/<article>/section_oracle_averaged.json`: `oracle` (argmax of the averaged rewards),
`rewards` (the average), `reward_sd` (per-arm sd across draws, exactly A.8's confidence signal),
and `n_draws`. Production `section_oracle.json` is never opened for writing. Verified against the
2 existing `noise_experiment/` articles: `06_tools__var_standard` merges cleanly (0/9 section-oracle
flips vs. the single draw — the confirmed-correct `deep` label is stable under averaging),
`09_RAG__var_standard` shows 3/6 flips (expected — this was the near-tie article the whole
replication effort targeted). Confirmed via `git check-ignore`/direct read that
`section_oracle.json`'s `version` field is still `5` (untouched) after the run. **Caveat carried
forward from §A.7.1: this test run's input is the known temperature-0.25-confounded data** — the
script itself is temperature-agnostic (it only averages whatever draws it's given), so this
validates the merge *mechanism*, not a production-ready label for these 2 articles. Re-run once
real temperature-0.7 replicates exist (A.10 step 2).

## A.6 Design decisions to make before spending

**How many draws?** N=3 total (i.e. 2 additional draws per arm, since the production draw
already exists and can be counted as one). Justified by the `√N` curve above; revisit only if
A.7 contradicts it.

**Which articles?** Two defensible strategies, with a real trap between them:

- **Uniform** — replicate everything. Unbiased, and correctly matches the fact that §55.3's 84%
  figure is corpus-wide, not concentrated in a few articles.
- **Targeted** (§20 fix #4) — replicate only thin-margin articles from `audit_oracle_margins.py`
  (12 CRITICAL+HIGH). Much cheaper. **But note the trap:** that tool tiers by *article-level*
  margin, while the training-relevant noise is *section-level*. An article with a comfortable
  article margin can still contain many coin-flip sections. So article-margin targeting is a
  sound proxy for improving **eval ground truth**, and a poor proxy for improving **training
  labels**. If targeting is used for the training set, target by section-level margin-to-noise
  ratio instead — which needs a small extension to the audit tool (it does not do this today).

**Recommended split, given the A.2 finding:**
1. **TRAIN (24 articles) — uniform N=3.** This is what GRPO actually consumes and where §19's
   frozen-label memorization mechanism operates. Cost: 24 × 4 arms × 2 extra draws = **192
   write+grade cycles** (no research).
2. **TEST (16 articles) — defer, or targeted-only.** TEST label precision matters for measurement
   honesty, but `n=16` sampling noise likely dominates there anyway (A.1), so this spend competes
   directly with test-set *expansion*, which fixes the binding constraint instead. If any TEST
   replication is done first, restrict it to the CRITICAL/HIGH-margin articles where a label flip
   is actually plausible.

**Temperature: use `course.yaml` (0.7), matching GT and the original 40-article production
episodes — NOT `rl_generation.yaml` (0.25).** This reverses the original recommendation in this
section ("use 0.25 for consistency with the existing replicates"), superseded by the direct
measurement in A.7.1 below: 0.25 is not just lower-noise, it's a confirmed systematic bias against
`standard`/`deep` specifically — using it for the real replication would corrupt exactly the
arm-choice decision GRPO is being trained to make, on top of the already-known deep-arm
under-representation problem (§54.7).

**Judge:** Claude (`--grading-model claude`), matching the current production re-grade (§37).

## A.7 Free validation — DONE (2026-07-30): averaging works directionally as predicted, on a necessarily tiny sample

Computed directly from the 15 real sections that exist across the 2 replicated articles
(`09_RAG__var_standard` 6 sections, `06_tools__var_standard` 9 sections) — 4 independent draws
each (1 production + 3 replicates), same production `_section_reward`/H0 formula applied
consistently to all 4 via `measure_replicate_noise.py`'s exact recompute path. Zero new API calls.

| | threshold used | sections crossing | vs §55.3 corpus baseline (282 sections) |
|---|---|---|---|
| Single-draw margin > 1 noise-sd | 0.140 | **3/15 (20.0%)** | 45/282 (16%) |
| Single-draw margin > 2 noise-sd | 0.280 | **2/15 (13.3%)** | 10/282 (4%) |
| Averaged(N=4) margin > 1 noise-sd | 0.070 (predicted `√4`-shrunk) | **8/15 (53.3%)** | — |
| Averaged(N=4) margin > 2 noise-sd | 0.140 | **2/15 (13.3%)** | — |

**The 1-sd bar shows a real, substantial jump (20%→53%, ~2.7x)** — larger than §55.3's own
"roughly double" estimate for N=3, on this sample. **The 2-sd bar shows the same raw count (2)
both times, but they are not the same sections** — `09_RAG`'s "Agentic RAG" (single margin 0.385,
the largest in the whole set) drops to 0.106 once averaged, while `06_tools`'s "Downsides of
Running Tools in a Loop" (single margin only 0.066, invisible at the single-draw level) rises to
0.144 and newly clears the bar. This is exactly the behaviour averaging is supposed to produce —
some single-draw margins are deceptively large (regress toward the mean once averaged), others
are deceptively small (rise once the specific draw's noise cancels) — not a null result dressed
up as one.

**This is evidence against the systematic-bias failure mode, not for it.** If the noise were
mostly systematic (the same bias in every draw for a given section — a real concern given GT
itself was written at temp 0.7 with zero exploration, §30), margins would stay roughly unchanged
under averaging. Instead several margins moved substantially in both directions (`09_RAG` S5:
0.385→0.106; `06_tools` S4: 0.549→0.238; `06_tools` S7: 0.066→0.144) — consistent with genuine,
largely-independent per-draw noise being averaged out, not a fixed bias persisting through it.

**Honest caveat: `n=15` sections is far too small to treat these percentages as precise estimates**
of what N=3-replicating all 282 sections would deliver — this is a directional spot-check, not a
corpus projection.

**Superseded by A.7.1 below — this result is confounded and its "proceed" recommendation no longer
stands as stated.** The 4 "draws" averaged above are not 4 draws from one consistent distribution:
1 draw is the original production episode at temperature 0.7, and the other 3 are
`noise_experiment` replicates at temperature 0.25. Direct measurement (A.7.1) found this is not a
neutral swap — 0.25 systematically understates `standard`/`deep` rewards relative to 0.7. So the
margin shifts reported above (e.g. `09_RAG` S5 0.385→0.106) are a mix of genuine noise-averaging
*and* this regime-shift artifact, not purely the former as originally stated.

### A.7.1 Correction (2026-07-30): temp=0.25 is a systematic bias, not just lower noise

User-prompted check (the noise_experiment replicates were generated at temperature 0.25 per
`rl_generation.yaml`, while GT and all 40 original production episodes were generated at
temperature 0.7 per `course.yaml` — confirmed via direct file read plus git log showing the 0.25
profile was created 2026-07-23, three months after "all episodes generated" on 2026-04-19; the
`write_article`/`integrate_exploration` node code itself is unchanged since that commit, ruling out
a prompt-drift confound). Comparing the original 0.7 draw against the mean of the 3×0.25
replicates for all 60 `(section, arm)` cells across both noise-experiment articles:

- **Sign of (0.25-mean − 0.7-draw): 41 negative / 12 positive / 7 zero (68% negative)** — a pure
  same-distribution noise relationship would split ~50/50, not 68/20.
- **Mean signed diff: −0.0735** — a real, one-directional shift, not centered on zero.
- **Concentrated in `standard`/`deep`, near-zero in `skip`**: e.g. `09_RAG` "Agentic RAG" deep arm
  0.7=+0.786 vs 0.25-mean=+0.150 (diff=−0.636); `06_tools` S4 deep 0.7=+0.649 vs 0.25-mean=+0.262
  (diff=−0.387). `skip` (zero exploration rounds, nothing to integrate) shows no consistent shift.

**Conclusion: temperature 0.25 doesn't just reduce variance, it systematically understates how
well `standard`/`deep` integrate the extra depth/breadth research, relative to 0.7.** Plausible
mechanism: lower-temperature writing is measurably worse at creatively synthesizing supplementary
research into coherent prose, which is exactly what `de`/`be` grade. This also means **§55.2's
official noise-floor figures (sd≈0.0991, arm-diff≈0.140), which all of §55.3's sigma_floor analysis
is built on, were computed purely from the 3×0.25 replicates** (`estimate_noise_floor.py` loads only
`REPLICATES=[1,2,3]` from `noise_experiment/`, never the 0.7 draw) — so that noise-floor estimate
reflects a lower-variance-but-biased regime, not necessarily the noise of the actual
temperature-0.7-generated production `section_oracle.json` that GRPO trains on. This is a
documented limitation of §55.2/§55.3, not something to redo now — a proper re-estimate needs real
temperature-0.7 replicates, which don't exist yet.

**Revised recommendation: replicate at temperature 0.7 (A.6, revised above), not 0.25.** The
existing 2-article 0.25 dataset remains useful for the qualitative claim that *some* independent
noise exists and averaging moves margins, but should not be treated as a clean noise-floor estimate
or merged directly with 0.7 production draws going forward.

## A.8 Getting more value from the same spend: confidence-weighted training

Replication produces a per-label **sd**, not just a better mean — and that sd is currently thrown
away. `train_grpo.py` already supports `--section-weight {wordcount,variance,hybrid,regret-hybrid,uniform}`,
so a natural addition is a **confidence** mode that down-weights sections whose margin is small
relative to their measured noise, instead of treating a coin-flip section and a decisively-labelled
section as equally authoritative training targets.

This is strictly more information-efficient than averaging alone: averaging improves the label,
weighting additionally stops the model from being forced to fit labels that remain uncertain even
after averaging (which, per §55.3, will still be the majority of sections even at N=3). It costs
one new weighting function and no additional generation. Worth building in the same pass as A.5's
merge-back script, since both consume the same per-draw data.

## A.9 What replication will NOT fix

Stating plainly, to prevent over-claiming later:
- **`n=16` TEST measurement floor** — unchanged. Only new test articles fix this.
- **Archetype gaps and class imbalance** (§16) — unchanged. Only new train articles fix these.
- **The 8-independent-topics limitation** of TRAIN — unchanged.
- **Systematic (as opposed to random) label bias** — averaging N draws of a consistently-biased
  process converges on the biased answer. A.7 is specifically designed to detect this case.
- **The entropy-collapse problem currently under investigation** (§60, `run22_reg_combo`) — that
  is a training-dynamics question; better labels may or may not help it, and the two should not
  be conflated.

## A.10 Recommended sequence

| # | Action | Cost | Rationale |
|---|---|---|---|
| 0 | ~~A.7's free validation~~ **DONE, then corrected (2026-07-30, see A.7.1)** | Zero | Averaging works directionally, BUT the existing noise_experiment data is confounded: replicates were generated at temp 0.25 vs GT/production's 0.7, and this is a confirmed systematic bias against `standard`/`deep`, not just lower noise |
| 1 | ~~Build A.5's merge-back script~~ **DONE (2026-07-30)**: `training/merge_replicate_oracles.py`, keeping the single-draw path intact | Small, code only | Prerequisite — without it, replicates cannot become production labels. Verified on the 2 existing (temp=0.25, confounded) articles as a mechanism check; not yet run on real 0.7 data |
| 2 | Uniform N=3 replication of the **24 TRAIN articles at temperature 0.7** (192 write+grade cycles, no research) | Moderate | Directly attacks §19's frozen-noisy-label mechanism where it actually bites; temperature 0.7 avoids A.7.1's confirmed regime-shift bias against exploration-heavy arms |
| 3 | Regenerate labels from averaged draws; re-run `estimate_noise_floor.py` / `audit_oracle_margins.py` on the new 0.7 replicates to get an unconfounded noise-floor estimate, then quantify the real improvement in defensible-section share | Zero | Measures whether step 2 delivered what A.3 predicted, and finally gives §55.2/§55.3 a noise-floor figure not built on the 0.25 confound |
| 4 | Retrain on the averaged labels; compare entropy trajectory and held-out eval against the current runs | One training run | The actual test of whether label precision changes training behaviour |
| 5 | *Then* revisit §16's test-set expansion with new topics, now that label precision is no longer the limiting factor | Expensive | Fixes the `n=16` sampling-noise constraint replication cannot touch |
| — | (optional, alongside 1-2) A.8's confidence weighting | Small, code only | Extracts extra value from data already being collected |

**Can step 2 run in parallel with §61's reward-formula investigation? Yes (2026-08-03).** §60.16
implication #2 originally argued for resolving the formula question before spending on replication.
Verified directly against the code: `merge_replicate_oracles.py` recomputes rewards from each
replicate's raw `reasoning.json` via `measure_replicate_noise.py`, using whichever formula is
*currently* live in `generate_episode_oracles.py` at call time — the reward formula is not baked in
when the replicate drafts are written and graded. Step 2 (the actual write+grade cost, real LLM API
spend) is therefore formula-agnostic and safe to run now, in parallel with §61's local-GPU training
experiments — no resource contention, and no risk of wasted replication effort regardless of which
formula §61 settles on. **Only step 4 (the retrain) should wait** for §61 to conclude — re-running
step 3's merge/average is free and will pick up whichever formula is live at the time.

**Bottom line:** the primary data target is **label noise, addressed by replication of the
existing articles at temperature 0.7** — no new topics required for this step, and no re-research
(write+grade only). New topics remain necessary, but for a *different* constraint (`n`, archetype
coverage), and they are better spent after label precision is fixed rather than before. A.7's free
validation was worth running, but its own data source turned out to have a real confound (A.7.1) —
another instance of this investigation's recurring lesson: verify the validation data itself before
trusting what it says.

## A.11 Step 2/3 executed for real (2026-08-04): the 6 Lesson-6/9 variants, temperature=0.7

User ran the real replication: **N=3 draws (1 production + 2 replicates) at temperature 0.7**,
for all 3 variants of both Lesson 6 and Lesson 9 — `06_tools`/`09_RAG` × `{var_minimal,
var_standard, var_demanding}` — via the existing `setup_noise_experiment.py` +
`rl_writing_generator.py`/`rl_grading_generator.py --episodes-dir` infrastructure (A.5). Data lands
in `rl_training_data/noise_experiment/<article>__replicate{1,2}__preset{0,1,3,5}/`; the original
2-article/3-replicate temp=0.25 dataset was moved aside to `noise_experiment/old_experiment/` and
kept as a reference fixture. All 48 new dirs verified graded (`scores.json`+`reasoning.json`
present) before analysis.

**Tooling changes made to run this** (both minimal, backward-compatible): (1) `estimate_noise_floor.py`
gained a `--articles`/`--replicates` CLI (previously hardcoded to the 2 original articles/3
replicates, mirroring the pattern already used by `measure_replicate_noise.py`/
`merge_replicate_oracles.py`); its core loop was factored into a `run(articles, replicates)` function
that also *returns* a stats dict (mean/median/p90 sd, 1×/2× arm-difference sd) for reuse by other
scripts, not just printing. (2) Fixed a stale hardcoded `"(temp=0.25)"` print label in
`measure_replicate_noise.py` that was left over from when the script only ever saw the original
0.25 dataset — it was a cosmetic string, not an actual check, but would have been actively
misleading applied to the new 0.7 data. (3) New script `training/quantify_defensible_gain_070.py`
(read-only, reuses `estimate_noise_floor`/`measure_replicate_noise`/`model_gate_candidates`, no
duplicated formula) computes the actual "before vs after" defensible-section-share numbers below.

### A.11.1 Unconfounded noise-floor estimate

| | old (temp=0.25, 2 articles, 3 reps, n=60 cells) | new (temp=0.7, 6 articles, 2 reps, n=180 cells) | new, SAME 2 articles as old (n=60 cells) |
|---|---:|---:|---:|
| mean per-cell sd | 0.0929–0.0991* | 0.0751 | **0.0686** |
| median per-cell sd | 0.0866–0.0955* | 0.0707 | 0.0707 |
| 1× arm-diff sd (mean·√2) | 0.1313–0.1400* | 0.1062 | 0.0970 |
| 2× arm-diff sd | 0.2627–0.2800* | 0.2123 | 0.1940 |

\*range reflects that the reward *formula* has changed several times since the original §55.2
figures (0.0991/0.140) were published; re-running the identical script against the identical old
0.25 dataset today (current formula) gives 0.0929/0.1313 — a formula-vintage difference, not a
data difference.

**Headline, apples-to-apples (rightmost column, identical 2 articles both times): real
temperature=0.7 replicate-to-replicate noise (mean sd 0.0686) is *lower* than the temperature=0.25
noise it superseded (0.0929)**, not higher. This is the opposite of the original design assumption
("lower temperature *should* reduce noise", the stated rationale for `rl_generation.yaml`'s 0.25 —
see §21/§23). Caveat: n=2 replicates (new) vs n=3 (old), and this is a single article-pair
comparison — not enough to assert a general "0.7 is less noisy than 0.25" law, but it is a real,
controlled (same articles, same current formula) measurement, not an artifact of comparing
different topics. Combined with A.7.1's already-confirmed *mean* bias (0.25 systematically
understates `standard`/`deep` vs 0.7), this means 0.25 was worse on **both** axes — biased *and*
(on this evidence) not even lower-variance — reinforcing that A.7.1's temperature-0.7 pivot was the
right call.

### A.11.2 Defensible-section share: single-draw vs. averaged (N=3), the 45 sections across the 6 variants

Using the new unconfounded thresholds (1×=0.1062, 2×=0.2123), and — critically — the
**√3-shrunk** thresholds (1×=0.0613, 2×=0.1226) for the averaged-margin side, since an N=3 average's
own noise floor is the single-draw floor divided by √N (the same convention A.7 used for its
√4-shrunk N=4 comparison; comparing an averaged margin against the *unshrunk* single-draw threshold
was tried first and produces a misleading "averaging made it worse" artifact purely from the
mismatched comparison):

| bar | single-draw | averaged (N=3) |
|---|---:|---:|
| margin > 1× noise-sd | 11/45 (24.4%) | **18/45 (40.0%)** |
| margin > 2× noise-sd | 7/45 (15.6%) | 6/45 (13.3%) |

**The 1×-sd bar shows a real, substantial gain (24.4%→40.0%, ~1.6×)** — directionally matching
A.3/§55.3's "N=3 should roughly double the defensible-section share" prediction, now measured on
real unconfounded data rather than the confounded pilot. **The 2×-sd (95%-confidence) bar shows no
gain, even a slight dip** — consistent with A.7's own observation that some single-draw margins
that happen to look large by chance regress toward a smaller true value once averaged (the 2×-sd
bar is disproportionately populated by exactly those spurious cases); this is the same qualitative
pattern A.7 found on the confounded data, now replicated on real 0.7 data. **Net verdict: replication
delivers a real gain at the "reasonably confident" bar but does not manufacture confidence at the
"very confident" bar** — some fraction of sections are genuinely, irreducibly near-tied, matching
A.9's stated expectation that replication does not fix everything.

### A.11.3 Full 282-section corpus, re-scored against the new (unconfounded) noise floor

Same single-draw corpus margins used throughout §54–56 (current `C2_soft_ga_pen010` production
formula), re-thresholded:

| bar | old (confounded 0.25) threshold | new (unconfounded 0.7) threshold |
|---|---:|---:|
| margin > 1× noise-sd | 45/282 (16.0%) | **65/282 (23.0%)** |
| margin > 2× noise-sd | 10/282 (3.5%) | **24/282 (8.5%)** |

Because the new unconfounded noise floor is *smaller* than the old confounded one (A.11.1), more of
the existing single-draw corpus now clears the bar — the §54–56 "84% of sections are statistically
indistinguishable from noise" framing was itself somewhat pessimistic, an artifact of the 0.25
confound inflating the noise estimate used at the time, not a change in the underlying labels.
Still a minority of the corpus (23%) clears even the weaker 1×-sd bar — the core finding (most
single-draw section labels are not confidently defensible) survives, just less starkly than
originally stated.

### A.11.4 Article-level result — 2 of 3 reward-decided labels confirmed, 1 corrected

`audit_oracle_margins.py`'s current tiering classifies 3 of the 6 target articles as hard-ruled
(immune to this whole question by construction): `06_tools__var_minimal` and `09_RAG__var_minimal`
are `policy=forbidden` (forced `skip`), `09_RAG__var_demanding` is a manual override (forced
`deep`). Real replicated data corroborates all three anyway where reward-comparable (`skip`'s raw
argmax was itself borderline `deep` at near-zero margin for both minimal articles — moot given the
hard rule; `09_RAG__var_demanding`'s raw argmax was already `deep` before the override, and 3/3
replicate draws unanimously vote `deep`, the strongest confirmation of any article measured).

The 3 genuinely reward-decided articles (`compute_article_oracle._compute_r_w` on
`section_oracle_averaged.json` vs. the current single-draw `article_oracle.json`):

| article | risk tier (audit_oracle_margins) | production (single-draw) | averaged (N=3) |
|---|---|---|---|
| `06_tools__var_standard` | MODERATE (0.0914) | `deep`, margin +0.0914 | `deep`, margin **+0.0531** — same winner, thinner but still well outside EPS_BAND=0.03 |
| `09_RAG__var_standard` | HIGH (0.0469) | `deep`, margin +0.0469 | `deep`, margin **+0.0311** — same winner, similar margin, still outside EPS_BAND |
| `06_tools__var_demanding` | HIGH (0.0304, barely above EPS_BAND) | `deep`, margin +0.0304 | **`light`**, margin **+0.0085** — winner flips AND drops inside EPS_BAND (now a genuine near-tie) |

**`06_tools__var_standard` — the article this whole investigation has used as its one
"confirmed-correct" reference point (§31 onward) — holds up under real, unconfounded temperature=0.7
replication**: still `deep`, replicate vote 2-1 (production + replicate2 vs. replicate1), same
qualitative pattern validated repeatedly under the old confounded data. `09_RAG__var_standard` is
now also confirmed (previously only ever a persistent, unresolved toss-up under the 0.25 data —
§30/§34/§40/etc. — real 0.7 data resolves it 2-1 for `deep`, consistent both by per-draw vote and by
averaged-R_w). **`06_tools__var_demanding` is a genuine correction**: its production label (`deep`,
margin 0.0304, HIGH-risk-tiered) is contradicted by both replicates (2/2 vote `light`) and by the
averaged R_w (flips to `light`, margin collapses to 0.0085 — inside the near-tie band). This is
exactly the kind of shaky HIGH-tier label Appendix A was built to catch and is the first article in
this whole investigation directly corrected by real (not confounded) replication evidence.

**Recommendation**: do not yet merge `section_oracle_averaged.json` into production
`section_oracle.json` for any of these 6 (A.10 step 4, the retrain, is explicitly deferred pending
§61's formula investigation). `06_tools__var_demanding`'s flip should be flagged `needs_review` /
treated as a near-tie if a decision is needed before the fuller 24-article TRAIN replication (A.10
step 2 proper) is run — do not silently keep trusting its current HIGH-risk `deep` label given
direct contradicting evidence now exists.

## A.12 What the C2 RL-pipeline will actually update once the full 24-article×N=3 replication lands (2026-08-06)

User is running the full uniform N=3 replication (A.10 step 2 proper, all 24 TRAIN articles, in
parallel with §61's GPU experiments per the parallelization note above) — expected to take several
days. This section enumerates, concretely, which pipeline components change and in what order once
those scores are in, so the sequence doesn't have to be re-derived from scratch when the data
lands.

**1. Per-article averaged oracle (mechanism already built, just needs to run at full scale).**
`training/merge_replicate_oracles.py` runs for all 24 TRAIN articles (currently validated only on
the 6 Lesson-6/9 pilot variants, §A.11). For each `(section, arm)` cell it averages reward
components across all draws (1 production + 2 replicates) and writes a **sibling** file
`bases/<article>/section_oracle_averaged.json` — production `section_oracle.json` is never
overwritten, so every historical label stays reproducible.

**2. `train_grpo.py::load_section_groups()` — needs a new read path.** Currently reads only
`section_oracle.json`. Needs a small addition (e.g. `--use-averaged-oracle` flag) to read
`section_oracle_averaged.json` for the 24 replicated TRAIN articles, falling back to the
single-draw file for TEST/any non-replicated article. This is the step that actually makes
replication *matter* — without it, the averaged data just sits on disk unused (A.5's originally-
identified gap, still open at full scale).

**3. Article-level oracle recompute.** `compute_article_oracle.py` (or a parallel `_averaged`
variant of it) needs to run on the averaged section rewards to produce updated `oracle_arm`s/
margins. This is what would let a real correction like `06_tools__var_demanding`'s flip
(deep→light, §A.11.4, currently only flagged `needs_review` not applied) become an actual
production label change, pending explicit sign-off — and surfaces any other such corrections the
full 24-article pass turns up.

**4. Noise-floor re-estimate, at full scale.** `estimate_noise_floor.py` / `audit_oracle_margins.py`
rerun on the complete 24-article temp=0.7 replicate set. §A.11.1 already did this for the 6-variant
pilot (mean per-cell sd 0.0686-0.0751, vs. the old temp=0.25-confounded 0.0929-0.0991); the full run
gives a corpus-representative, not just pilot-representative, unconfounded noise floor — the real
evidentiary basis `sigma_floor`/`near_tie_margin` never had (§54.7).

**5. Possibly `sigma_floor`/`near_tie_margin` recalibration.** Once step 4 gives a trustworthy,
full-scale noise floor, `train_grpo.py`'s `sigma_floor=0.04` default (never formally derived) and
`near_tie_margin=0.06` become revisitable with real evidence — though widening `near_tie_margin` was
explicitly deferred earlier in this investigation (§54), so this needs a fresh explicit decision,
not an automatic change.

**6. The actual retrain (the real payoff, deferred until §61 concludes, A.10 step 4).** A fresh GRPO
run consuming **both** fixes together: the averaged/cleaner section labels (this replication) *and*
whichever cost_coef conclusion §61 lands on (currently `-0.05` H0-units is the leading candidate
pending `run29_costcoef05`'s result). Steps 1-5 above are formula-agnostic and safe to keep running
in parallel with §61; only this step must wait.

**7. Optional, same-pass bonus.** A.8's confidence-weighted `--section-weight` mode in
`train_grpo.py`, using the per-cell `reward_sd` that `merge_replicate_oracles.py` already computes
but nothing currently consumes — down-weights sections that stay uncertain even after averaging, at
zero extra generation cost.

**Net**: replication changes *what data exists* (steps 1, 4); making it actually influence anything
requires the loader/recompute wiring (steps 2-3, not yet built at full 24-article scale); and the
real test of whether it was worth it is the eventual joint retrain (step 6), intentionally
sequenced after — not before — `run29`'s result settles the cost_coef question.

## A.13 Full 24-article×N=3 replication landed — steps 1 and 4 executed at full scale (2026-08-15, updated in place 2026-08-16 after the TRAIN grade correction pass)

The full uniform replication anticipated by A.12 is done: **all 24 TRAIN articles** (8 lessons ×
`{var_minimal, var_standard, var_demanding}`), **N=3 draws each** (1 production + 2 replicates at
temperature 0.7) — 192 write+grade cycles, exactly A.10 step 2's plan, verified complete (all 192
`noise_experiment/` dirs have `scores.json`+`reasoning.json`). This section executes A.12's steps 1
and 4 (merge-back + full-scale noise-floor/defensible-share re-estimate) and reports the real
numbers, superseding A.11's 6-article pilot with the complete 171-section TRAIN corpus. **Steps 2/3/6
(loader wiring, article-oracle recompute wiring, the retrain) remain NOT done** — out of scope for
this pass, consistent with A.12's own sequencing (formula question / `run29` still pending).

**Update (2026-08-16): the user manually reviewed and corrected `scores.json`/`reasoning.json` for
a subset of the 24 production episodes** (32 of 96 `scores.json` files, spanning 11 articles — the
CRITICAL/HIGH/flip/erosion candidates this appendix had flagged), plus some replicate drafts for the
most concerning articles (`06_tools__var_demanding`/`__var_standard` partially, `10_memory_knowledge_access__var_demanding`
and `11_multimodal__var_standard` fully, both replicates). Backed up the pre-correction
`section_oracle.json`/`article_oracle.json` for all 24 articles to `bases_PRE_GRADECORRECTION_REGEN_20260815/`,
then regenerated both files for all 24 from the corrected grades (`generate_episode_oracles.py` +
`compute_article_oracle.py --force`) and re-ran every tool in this section against the corrected
data. `diff_oracle_regen.py` confirms exactly **2 production-level oracle_arm flips from the
correction itself** (independent of any replicate averaging): `02_workflows_vs_agents__var_demanding`
`light→standard` (old margin +0.0693, COMFORTABLE; new margin +0.0232) and
`10_memory_knowledge_access__var_demanding` `standard→deep` (old margin -0.0275, tie-broken; new
margin +0.0330, unique winner) — the second one an exact match to what the unanimous 3/3 replicate
vote below had already predicted before any correction was applied. New TRAIN arm distribution:
skip8/light7/standard4/**deep5**  (was skip8/light8/standard4/deep4) — a small but real gain for
the long-standing deep-scarcity concern. All numbers below are the post-correction, re-run values;
the pre-correction numbers this section originally reported are superseded, not shown separately.

**Tooling**: `merge_replicate_oracles.py` and `estimate_noise_floor.py` needed no changes to scale
from 6 to 24 articles (both already took `--articles`/`--replicates`, per A.11's tooling work).
Extended `quantify_defensible_gain_070.py` to (a) default to the full 24-article list instead of
the 6-article pilot, (b) add a TRAIN-only (171-section) row to the corpus-wide re-scoring, and (c)
add a new Step D — per-article production-vs-averaged oracle_arm/margin, cross-referenced against
`audit_oracle_margins.py`'s risk tier and the raw 3-draw vote tally, so CONFIRMED/FLIPPED status is
computed directly rather than eyeballed article-by-article as A.11 did by hand.

### A.13.1 Noise floor, full scale (684 cells, all 24 articles — supersedes A.11.1's 180-cell estimate)

| | mean sd | median sd | 1× arm-diff sd | 2× arm-diff sd |
|---|---:|---:|---:|---:|
| old (temp=0.25, 2 articles, 3 reps, n=60) | 0.0929 | 0.0955 | 0.1313 | 0.2627 |
| A.11 pilot (temp=0.7, 6 articles, 2 reps, n=180) | 0.0751 | 0.0707 | 0.1062 | 0.2123 |
| full, pre-correction (temp=0.7, 24 articles, 2 reps, n=684) | 0.0645 | 0.0658 | 0.0913 | 0.1825 |
| **full, post-correction (temp=0.7, 24 articles, 2 reps, n=684)** | **0.0659** | 0.0681 | **0.0932** | 0.1864 |

The full-scale unconfounded noise floor is lower still than the 6-article pilot's already-lower
estimate — consistent, not a fluke: real temperature=0.7 replicate noise is smaller than what the
temperature=0.25-confounded data implied, now confirmed on 11.4× more cells. The correction pass
nudged this UP very slightly (0.0645→0.0659) rather than down — expected, since the corrected
replicate drafts (a handful of files, not a systematic retreatment) don't mechanically reduce
variance, they just make individual cells more accurate. This is the corpus-representative figure
A.12 step 4 called for; **`sigma_floor=0.04` remains ~0.61× this mean cell sd** (was 0.62% pre-correction,
0.53× at pilot scale, 0.43× under the old confounded estimate) — still on the permissive side, but
the gap to "adequately conservative" is smaller than originally measured.

### A.13.2 Defensible-section share, full 171-section TRAIN corpus (single-draw vs. averaged N=3)

Using the corrected-data thresholds (1×=0.0932, 2×=0.1864 single-draw; 0.0538/0.1076 √3-shrunk for
the averaged side — same shrinkage discipline as A.11, required to avoid the apples-to-oranges
mistake of comparing an averaged margin against an unshrunk threshold):

| bar | single-draw | averaged (N=3) |
|---|---:|---:|
| margin > 1× noise-sd | 53/171 (31.0%) | **79/171 (46.2%)** |
| margin > 2× noise-sd | 26/171 (15.2%) | 29/171 (17.0%) |

**The 1×-sd bar still shows a substantial gain (31.0%→46.2%, 1.49×)** — slightly smaller than the
pre-correction figure (29.8%→49.1%, 1.65×) since the correction itself already resolved some of
what averaging used to fix, but still comfortably in line with A.3/§55.3's "N=3 roughly doubles the
defensible share" prediction. **The 2×-sd bar (15.2%→17.0%) is essentially unchanged from
pre-correction (17.0%→19.3%)** — modestly positive either way, consistent with the pilot's own
finding that this specific bar moves weakly.

**Section-level oracle flip rate (single-draw argmax vs. averaged argmax, raw count from
`merge_replicate_oracles.py`, all 171 sections): 79/171 = 46.2%** (was 80/171=46.8% pre-correction —
essentially unchanged). Just under half of all single-draw section-level winners change once
averaged over 3 draws — a distinct statistic from defensible-share (this one is about raw decision
instability, not confidence-vs-noise-floor), and the starkest single number this whole investigation
has produced for "how much does the training signal actually depend on which one draw happened to
get generated" — largely unmoved by directly fixing a subset of the underlying grades, since most of
the corpus's flip-rate is driven by articles/sections the correction pass didn't touch at all.

### A.13.3 Corpus-wide re-scoring at the new vs. old noise floor (single-draw only, independent of averaging)

| scope | n | OLD (0.25-confounded) 1×/2× | NEW (0.7, unconfounded) 1×/2× |
|---|---:|---|---|
| all production articles | 282 | 43 (15.2%) / 8 (2.8%) | **79 (28.0%)** / 25 (8.9%) |
| TRAIN-only (matches GRPO exactly) | 171 | 34 (19.9%) / 7 (4.1%) | **54 (31.6%)** / 22 (12.9%) |

(Pre-correction these were 45/282 (16.0%), 10/282 (3.5%), 82/282 (29.1%), 26/282 (9.2%) and
36/171 (21.1%), 9/171 (5.3%), 53/171 (31.0%), 23/171 (13.5%) respectively — small shifts throughout,
since only 11 of 24 TRAIN articles' single-draw grades actually changed.)

**Just correcting the noise floor — before any averaging — still nearly doubles the apparent
defensible-section share** (e.g. TRAIN-only 1×: 19.9%→31.6%). This means a substantial share of
§54–56's "84% of sections are statistically indistinguishable from noise" pessimism was an artifact
of the temperature=0.25 confound inflating the noise estimate (A.7.1), not an unmovable property of
the underlying labels. The core finding survives (most single-draw section labels are still not
confidently defensible — roughly 68-69% still miss the 1×-sd bar even at the corrected, smaller
threshold) but is meaningfully less dire than originally stated.

### A.13.4 Article-level: 12 confirmed, 2 flipped, 10 hard-ruled (of 24) — improved from 10/4/10 pre-correction

> **SUPERSEDED IN PART (2026-08-20, see A.16.0):** a third tooling bug (ordinal-index misalignment —
> every TRAIN digest lists each section twice, so production's ordinal fallback used index `n+i`
> while the replicate path used `i`) affected ~9% of cells. After the fix this table reads
> **11 confirmed / 3 flipped / 10 hard-ruled**: `06_tools__var_demanding`'s averaged draw now
> computes to `light +0.0101` (not `deep +0.0013`), so it moves from "CONFIRMED in name only" to a
> genuine FLIP — which **agrees with** the `light` label A.15.2 had already assigned it by
> majority vote. All 5 of A.15.2's finalized TRAIN labels are unchanged by the fix.

`audit_oracle_margins.py` classifies 10 of the 24 as hard-ruled (immune to this whole question):
**all 8 `var_minimal` articles are `policy=forbidden`→`skip`** (the already-known 8/8 pattern), plus
2 manual overrides (`09_RAG__var_demanding`, `11_multimodal__var_demanding`→`deep`/`standard`). Of
the 14 reward-decided articles:

| article | tier | production | averaged (N=3) | votes (prod,rep1,rep2) | |
|---|---|---|---|---|---|
| `02_workflows_vs_agents__var_standard` | CRITICAL | light +0.0030 | light +0.0853 | light,light,light | CONFIRMED (more decisive) |
| `02_workflows_vs_agents__var_demanding` | CRITICAL | standard +0.0232 | standard +0.0184 | standard,deep,standard | CONFIRMED — **resolved by the correction itself** (see below) |
| `03_context_engineering__var_standard` | MODERATE | standard +0.0817 | standard +0.0195 | standard,deep,light | CONFIRMED (thinner, unaffected by correction) |
| `03_context_engineering__var_demanding` | CRITICAL | light +0.0241 | light +0.0512 | light,light,light | CONFIRMED (more decisive, unaffected) |
| `05_workflow_patterns__var_standard` | CRITICAL | light +0.0076 | light +0.0384 | light,light,light | CONFIRMED (more decisive, unaffected) |
| `05_workflow_patterns__var_demanding` | HIGH | light +0.0302 | light +0.0202 | light,standard,deep | CONFIRMED (thinner, unaffected by correction despite touched presets) |
| `06_tools__var_standard` | MODERATE | deep +0.0839 | deep +0.0841 | deep,deep,light | CONFIRMED (this investigation's reference article — now *more* stable under averaging than before) |
| `06_tools__var_demanding` | HIGH | deep +0.0523 | **deep +0.0013** | deep,light,light | CONFIRMED in name only — margin collapsed to near-zero, 2/3 votes still favor `light` |
| `08_react_practice__var_standard` | COMFORTABLE | light +0.1752 | light +0.0906 | light,deep,light | CONFIRMED |
| **`08_react_practice__var_demanding`** | MODERATE (was COMFORTABLE) | standard +0.0786 | **light +0.0036** | standard,light,light | **FLIPPED** — production itself eroded from 0.1189→0.0786 under correction, averaging then flips it |
| `09_RAG__var_standard` | MODERATE (was HIGH) | deep +0.0937 | deep +0.0347 | deep,standard,deep | CONFIRMED — reinforced by correction (was +0.0469) |
| `10_memory_knowledge_access__var_standard` | HIGH | light +0.0414 | light +0.0088 | light,standard,light | CONFIRMED (thinner still, despite correction reinforcing production to +0.0414) |
| `10_memory_knowledge_access__var_demanding` | HIGH (was CRITICAL) | deep +0.0330 | deep +0.0295 | deep,light,deep | CONFIRMED — **resolved by the correction itself** (see below) |
| **`11_multimodal__var_standard`** | CRITICAL | light +0.0263 | **skip +0.0118** | light,skip,skip | **FLIPPED** — persists even with BOTH replicates fully corrected/reviewed |

**Two of the original 4 flips were resolved directly by the correction pass, without needing to
touch replication at all:**

1. **`10_memory_knowledge_access__var_demanding`** — the production draw itself now computes to
   `deep +0.0330` (a unique winner, no tie-break needed), matching exactly what the unanimous 3/3
   replicate vote predicted before any correction existed. The averaged draw agrees (`+0.0295`,
   2/3 vote `deep`). This is about as clean a resolution as this investigation gets: independent
   replication evidence and a manual grade correction converged on the identical answer.
2. **`02_workflows_vs_agents__var_demanding`** — `diff_oracle_regen.py` shows this flipped at the
   *production* level alone (`light +0.0693` → `standard +0.0232`, a COMFORTABLE-margin flip from
   correction). The averaged draw (`standard +0.0184`, 2/3 vote `standard`) corroborates it. No
   longer an "erosion" case (A.15.3.1's original framing) — it's now a resolved, cross-validated
   flip.

**Two flips remain genuinely open, and one "confirmed" label is fragile enough to be a de facto
third:**

1. **`08_react_practice__var_demanding`** newly flips (was a 2/3-vote-only concern pre-correction,
   at a COMFORTABLE production margin that made it easy to discount) — now that production itself
   independently eroded to MODERATE tier under correction, the flip to `light` is corroborated by
   two separately-sourced pieces of evidence (the corrected production value's own erosion, and the
   2/3 replicate vote) rather than resting on replication alone. Caveat: this article's *replicates*
   were not part of the review pass (only production was corrected) — an asymmetry worth knowing
   before treating this as fully resolved.
2. **`11_multimodal__var_standard`** still flips to `skip` — and this is now the single most
   trustworthy flip in the dataset, since BOTH replicates for this article were fully reviewed and
   corrected (not just production), yet the result is unchanged from pre-correction. Strong
   candidate for accepting the correction outright rather than spending more replicate budget on it.
3. **`06_tools__var_demanding`** stays nominally `deep` (CONFIRMED) but its averaged margin
   collapsed to `+0.0013` — production reinforced `deep` under correction (0.0304→0.0523), yet the
   2/3 replicate vote still favors `light`. This is *not* a clean confirmation; it is arguably the
   most unresolved article in the whole set now, since the two evidence sources (corrected
   production, replicate majority) now point in opposite directions with almost no margin on either
   side.

**Recommendation (updated)**: `10_memory_knowledge_access__var_demanding` and
`02_workflows_vs_agents__var_demanding` are resolved — their corrected production values can be
trusted as-is, no further replication needed. `08_react_practice__var_demanding`,
`11_multimodal__var_standard`, and `06_tools__var_demanding` remain open and are the concrete basis
for A.15.3's revised N=5 target list. As before, none of this should be merged into a retrain
without the explicit sign-off this investigation has required for every prior label/formula change.

## A.14 Detailed reward-signal-quality report — section and article level (2026-08-15, updated in place 2026-08-16 after the TRAIN grade correction)

New tool `training/reward_signal_quality_report.py` (read-only) consolidates A.13's metrics plus
the GRPO-specific ones `train_grpo.py` itself actually uses (`sigma_floor=0.04` flat-drop filter,
`near_tie_margin=0.06` acceptance window, normalized advantage `regret/max(std,sigma_floor)` — the
literal quantity that scales the GRPO gradient) into one run, computed identically for single-draw
(`section_oracle.json`) and averaged N=3 (`section_oracle_averaged.json`) so every number is a true
apples-to-apples comparison. Re-run after the correction pass; all numbers below are post-correction.

### A.14.1 Section-level GRPO signal quality, corpus aggregate (171 TRAIN sections)

> **Re-verified 2026-08-21** by re-running `reward_signal_quality_report.py` after A.16.0's two
> section-level bug fixes (explore-split aggregation, ordinal-index misalignment) landed — this
> table's numbers moved only slightly and the conclusion is unchanged.

| metric | single-draw | averaged (N=3) |
|---|---:|---:|
| flat-drop rate (spread < `sigma_floor`) | 0.0% | 3.5% (6 sections) |
| floored rate, of kept (std < `sigma_floor`) | 21.1% | 27.3% |
| near-tie rate (2+ arms within `near_tie_margin`) | 55.0% | **58.5%** |
| mean margin | 0.0961 | 0.0656 |
| **median margin** | 0.0446 | **0.0453** |
| mean normalized advantage (real GRPO gradient scale) | 1.216 | **1.229** |
| arm distribution (skip/light/standard/deep) | 49/50/39/33 | 49/54/33/35 |

(Pre-correction these were flat-drop 0.0%→2.3%, floored 22.2%→25.7%, near-tie 58.5%→56.7%, mean
margin 0.0974→0.0680, median margin 0.0393→0.0501, normAdv 1.200→1.235, dist 50/49/38/34→46/54/34/37
— broadly the same story, shuffled by the 11 corrected articles. The 2026-08-20 grade-correction-era
numbers just above were 1.216→1.234/0.0657/0.0491/45-53-37-36 — A.16.0's bug fixes moved these by
≤0.006 in every case, not enough to change any conclusion below.)

**Mean margin drops but median margin rises — a real, informative dissociation, not noise.** The
single-draw distribution has a fatter right tail (some sections look decisively separated purely by
chance — the same regression-to-the-mean pattern A.7/A.11/A.13 already documented for individual
articles); averaging pulls those inflated outliers down (lowering the mean) while genuinely
clarifying the *typical* section (raising the median). **Mean normalized advantage — the number that
actually scales the GRPO policy gradient — still improves slightly (1.216→1.229, +1.1%) despite more
groups being denominator-clamped (floored 21.1%→27.3%)**: averaging remains, net, not hurting
trainability, unchanged conclusion from pre-correction, though the effect is small enough to call a
wash rather than a strengthening — see A.16.2's `mean |advantage|` (all 4 arms, not just the winner)
for the complementary metric that goes the other way (0.8188→0.8061). **Near-tie rate now RISES
slightly under averaging
(55.0%→58.5%)** — the opposite direction from the pre-correction reading (58.5%→56.7%) — but this
flip is small (both close to the ~55-58% range) and better attributed to which specific sections'
grades moved than to any systematic change in what averaging does. **Deep-representation still rises**
(33→36, +9%, light also rises 50→53) while skip/standard both fall slightly — the same small, welcome
move away from this investigation's long-standing deep-scarcity concern (§54.7 onward) as before.
**Flat-drop rate rises from 0.0% to 3.5%** (was 0.0%→2.3%): averaging genuinely flattens 6 sections'
arm-spread below `sigma_floor` that weren't flat on the single draw — real information, not a
training-data loss to worry about.

### A.14.2 Per-lesson breakdown — improvement is lesson-dependent, not uniform (unchanged conclusion after correction)

The corpus aggregate (A.14.1) obscures real heterogeneity. Per-lesson near-tie rate and normalized
advantage, single-draw → averaged, post-correction:

| lesson | near-tie | normAdv | direction | touched by correction? |
|---|---|---|---|---|
| `02_workflows_vs_agents` | 55.6%→**38.9%** | 1.219→1.353 | clearly improves | yes (2 articles) |
| `03_context_engineering` | 66.7%→**79.2%** | 1.186→1.140 | **degrades** (flat-drop 0%→8.3% too) | no |
| `05_workflow_patterns` | 57.1%→61.9% | 1.079→1.179 | mixed (near-tie worse, gradient better) | yes (1 article, no aggregate effect) |
| `06_tools` | 55.6%→48.1% | 1.242→1.366 | clearly improves | yes (2 articles) |
| `08_react_practice` | 33.3%→**61.1%** | 1.381→1.224 | **degrades** (gap widened by correction) | yes (production only, 1 article) |
| `09_RAG` | 66.7%→**83.3%** | 1.169→1.106 | **degrades** | yes (1 article, no aggregate effect) |
| `10_memory_knowledge_access` | 42.9%→38.1% | 1.318→1.342 | clearly improves (single-draw itself improved from correction) | yes (2 articles) |
| `11_multimodal` | 58.3%→58.3% | 1.153→1.142 | ~flat | yes (1 article, no aggregate effect) |

**Unchanged conclusion: the same 3 of 8 lessons (`03_context_engineering`, `08_react_practice`,
`09_RAG`) still get a *noisier* reward signal under N=3 averaging on both near-tie rate and
normalized advantage simultaneously** — none of the 11 corrected articles happened to fall in a way
that resolved this pattern (only 1 of the 3 flagged lessons, `08_react_practice`, had any article
touched by the correction at all, and only its production draw, not its replicates — the aggregate
degradation, if anything, is slightly *more* pronounced now: single-draw near-tie improved 38.9%→33.3%
from the correction itself, widening the gap to averaging's unchanged 61.1%). This is real, corrected
data, not a residual pre-correction artifact — the case for N=5 on these 3 lessons (A.15.3) stands
unchanged.

### A.14.3 Per-variant breakdown — `var_standard` still improves most cleanly, but no longer with zero new flat-drops

| variant | near-tie | normAdv | flat-drop |
|---|---|---|---|
| `var_minimal` | 59.6%→61.4% | 1.214→1.271 | 0%→3.5% |
| **`var_standard`** | 54.4%→**52.6%** | 1.179→**1.239** | 0%→**1.8%** |
| `var_demanding` | 50.9%→61.4% | 1.254→1.192 | 0%→5.3% |

(Pre-correction: `var_minimal` identical (untouched by the correction); `var_standard` was
59.6%→49.1%/1.157→1.236/0%→0%; `var_demanding` was 56.1%→59.6%/1.227→1.198/0%→3.5%.)
`var_standard` remains the only variant that improves on *both* near-tie rate and normalized
advantage, but the correction pass (which touched several `var_standard` articles directly) moved
its single-draw near-tie rate down from 59.6% to 54.4% at the source, and introduced a small
(1.8%) flat-drop rate under averaging that wasn't there before — **the "incurring zero new
flat-drops" claim from the pre-correction reading no longer holds exactly**, though the variant's
overall improve-on-both-axes conclusion is unchanged. Same untested hypothesis as before for *why*
`var_standard` behaves best: `var_minimal`/`var_demanding` sit at the two extremes of the
depth-demand spectrum where section rewards are more likely to already be near a genuine
floor/ceiling, leaving less room for averaging to clarify a real signal.

### A.14.4 Article-level: flip-rate by risk tier (n=14, updated: 2 flips not 4)

Reusing A.13.4's per-article table, aggregated by `audit_oracle_margins.py` tier (reward-decided
articles only, n=14; tier populations shifted slightly since the correction moved
`08_react_practice__var_demanding` from COMFORTABLE to MODERATE):

| tier | flipped |
|---|---|
| CRITICAL | 1/5 (20%) |
| HIGH | 0/4 (0%) |
| MODERATE | 1/4 (25%) |
| COMFORTABLE | 0/1 (0%) |

(Pre-correction: CRITICAL 2/5 (40%), HIGH 1/4 (25%), MODERATE 0/3 (0%), COMFORTABLE 1/2 (50%).)
**Still not monotonic** (MODERATE's 25% exceeds HIGH's 0%) but for a different reason than before —
pre-correction the counter-example was a COMFORTABLE-tier article flipping; post-correction that
same article moved down into MODERATE (correctly reflecting its now-real fragility) and the sole
remaining COMFORTABLE-tier article did *not* flip, restoring the intuitive "COMFORTABLE = safe"
pattern at n=1. With only 1-5 articles per tier this remains not a reliable calibration curve —
just confirmation that tier alone is an incomplete predictor of stability, now slightly less
alarming than the pre-correction reading since the correction resolved the worst counter-example.

### A.14.5 Confirmed net verdict (updated)

Averaging N=3 real temperature=0.7 draws is, in aggregate, a **genuine, if partial and
non-uniform**, improvement in section-level reward-signal quality: better median margin, better
mean normalized advantage, slightly better deep-representation — largely unchanged conclusions from
before the correction pass. It still degrades the signal for the same 3 of 8 lessons, still does not
raise the 2×-sd defensible bar much (A.13.2), and article-level near-tie rate now moves in the
opposite small direction (55.0%→58.5%, was 58.5%→56.7%) — a minor, not load-bearing, reversal.
**The correction pass itself measurably improved article-level label confidence independent of
averaging**: 12 confirmed/2 flipped (was 10/4), with 2 of the original 4 flips resolved directly by
fixing the underlying grades rather than needing replication to catch them, and the 2 that remain
(`08_react_practice__var_demanding`, `11_multimodal__var_standard`) now backed by more consistent
evidence than before. None of this changes the A.12/A.13 recommendation: production labels for the
2 remaining open articles stay untouched pending A.15's N=5 expansion, and the retrain (A.12 step 6)
still waits on §61's cost_coef conclusion (already reached — see A.15).

## A.15 Updated plan after the N=3 TRAIN replication — next steps before retraining (2026-08-15, updated in place 2026-08-16 after the TRAIN grade correction)

§61 concluded with `run26`'s exact mechanism (C2 + `cost_coef=-0.06`, ordinal units) as the winning
single-variable candidate (`run29`'s H0-unit test came back worse on every metric, closing that
branch — see the Stage 1 addendum). A.12 step 6 (the joint retrain: winning formula + replicated
labels) is therefore no longer blocked on the formula question — but three things need deciding
first: what to do with the TRAIN flips (A.13.4), whether N=3 is enough everywhere it was applied,
and whether TEST also needs replication before trusting Stage 1's model comparisons. This section
answers all three, plus a fresh CRITICAL/HIGH margin audit to ground the TEST question concretely
(the only previously-published audit, §"MARGIN-DIAGNOSTIC SCRIPT", is from 2026-07-13 and predates
G0/H0/J0/C2/the cost_coef staging — stale for this purpose). **Update (2026-08-16): the user then
manually reviewed and corrected a subset of TRAIN grades (A.13's update note); this section's TEST
analysis (A.15.1, A.15.4) is unaffected since only TRAIN was touched, but A.15.2/A.15.3 are rewritten
below to reflect the correction's effect on the label-confidence picture.**

### A.15.0 Signal landscape at a glance — TRAIN vs TEST (2026-08-20)

A quick-reference summary of A.13-A.15.4's findings, once all of TRAIN's and TEST's replication work
had landed; see the referenced subsections for full evidence and derivations.

**TRAIN (24 articles, 171 sections)** — question was "does N=3 averaging help, and how much":

| metric | single-draw | N=3-averaged |
|---|---:|---:|
| defensible share (margin > 1x noise-sd) | 31.0% | **46.2%** |
| defensible share (margin > 2x noise-sd) | 15.2% | 17.0% |
| near-tie rate | 55.0% | 58.5% |
| median section margin | 0.0446 | **0.0491** |
| mean normalized advantage (GRPO gradient scale) | 1.216 | **1.234** |
| section-level oracle flip rate | — | 46.2% |

Net (A.14.5): genuine but non-uniform improvement — 5/8 lessons improve, 3/8
(`03_context_engineering`, `08_react_practice`, `09_RAG`) get noisier on both near-tie rate and
normalized advantage. Article-level: 12 confirmed / 2 flipped / 10 hard-ruled (of 24); all 5
originally-flagged articles finalized via majority vote (A.15.2), N=5 declined (A.15.3). Re-verified
2026-08-20 after the explore-split aggregation bug fix (A.15.4) — tally unchanged, TRAIN corrections
hold. **Not yet applied to production.**

**TEST (16 official articles, 12 replicated)** — question was "are the eval labels themselves
trustworthy enough for model-vs-model comparisons":

| metric | value |
|---|---:|
| scored TEST articles at CRITICAL/HIGH margin risk (A.15.1) | 12/15 (80%) |
| cross-draw cell sd, mean / median (12 replicated articles, 288 cells) | 0.0804 / 0.0577 |
| (TRAIN's cross-draw cell sd, mean / median, for comparison) | 0.0659 / 0.0681 |
| section-level oracle flip rate (12 replicated articles) | 40.3% (29/72) |
| article-level: confirmed / corrected / unresolved (of 12) | **8 / 4 / 0** (corrected 2026-08-25, was 7/4/1 — see below) |
| light↔deep confusion cluster (5 articles) | 4/5 confirmed, 1 corrected (`13_agent_framework`: deep→light) |

TEST is noisier on average than TRAIN but with a fatter right tail (median < mean, the opposite of
TRAIN) — driven by a small number of extreme-spread sections (see A.15.4 detail below), most
concentrated in `07_reasoning_planning`. `ga`'s TRAIN-side mean-drop
under averaging (0.740→0.412) does **not** replicate for TEST (0.5938→0.5880), and gate-threshold
sweeps (0.5→0.2) show zero effect on the label landscape. **Not yet applied to production.**

> **Correction (2026-08-25):** `07_reasoning_planning` was never actually an unresolved 3-way split.
> `_test_replication_eval.py` (the script that produced this vote tally) used a deduped section-id
> list instead of `_production_sec_ids()` — the digest-ordered-with-duplicates convention
> `merge_replicate_oracles.py` already used correctly, per A.16.0. Fixed the script; re-run shows all
> 3 draws (production + 2 replicates) unanimously vote `skip`, matching the existing production label
> exactly. See the correction note under A.15.4's results table for the full account.

### A.15.1 Fresh margin audit (`audit_oracle_margins.py`, re-run today) — TEST is far riskier than assumed

Re-ran the audit against current production `bases/` (all 45 article-oracles incl. augmented
pilots). Headline count: **CRITICAL=15, HIGH=10, MODERATE=6, COMFORTABLE=3** (of 34 noise-risk-scored;
11 more are policy-forced/manual-override, immune to this question). Restricting to the **16
official TEST articles** (`State_of_LLM_Reasoning` excluded, policy-forced):

| tier | TEST articles | count |
|---|---|---|
| CRITICAL | `Earth_Oceans_Origin`(-0.0032), `Gravity_Entropy`(-0.0009), `Dark_Dimension`(0.0026), `14_agent_system_design`(0.0077), `07_reasoning_planning`(0.0127), `Distinct_AI_Models`(0.0169), `04_structured_outputs`(0.0180) | 7 |
| HIGH | `Space-Time_QECC`(0.0336), `13_agent_framework`(0.0363), `Bird_Eye_Extreme`(0.0398), `Understanding_Reasoning_LLMs`(0.0431), `Insects_Consciousness`(0.0455) | 5 |
| MODERATE | `29_evaluation_metrics`(0.0667), `HNSW`(0.0845), `31_CI`(0.0888) | 3 |
| COMFORTABLE | (none) | 0 |

**12 of 15 scored TEST articles (80%) sit at CRITICAL or HIGH margin risk** — dramatically more than
the ~3/16 the stale 2026-07-13 audit implied (margins have moved substantially under G0/H0/J0/C2).
**Striking, load-bearing overlap: every article in the recurring light↔deep confusion cluster that
has driven the failure pattern in `run26`/`run27`/`run28`/`run29` (`13_agent_framework`,
`Distinct_AI_Models`, `Bird_Eye_Extreme`, `Space-Time_QECC`, `Dark_Dimension`) is on this CRITICAL/HIGH
list.** This reframes TEST replication from "optional, lower priority, competes with test-set
expansion" (A.6's original framing) to something with direct bearing on whether §61 Stage 1's
model-vs-model TEST comparisons are even measuring a stable target — if 80% of the scored TEST
oracle labels are this thin, some fraction of the exact/near/miss differences between `run26` and
its alternatives could be noise in the ORACLE, not the model.

### A.15.2 TRAIN label corrections — all 5 flagged articles now finalized at N=3 (no N=5)

**User decision (2026-08-17): do not expand to N=5 — the overall training-signal gain from N=3 is
real (A.13/A.14), even if uneven across lessons, and that's enough to finalize on.** This closes out
the 3 previously-open articles using the pre-registered decision rule from §23/A.10 (majority vote
of each draw's own arm-winner across all 3 draws — production + 2 replicates — takes precedence
over the averaged-reward-argmax computation `section_oracle_averaged.json` reports, precisely for
cases like these where the two methods disagree):

The two cleanest cases resolved directly at the grade-correction source, no vote needed:

1. **`10_memory_knowledge_access__var_demanding`** — production now independently computes to
   `deep +0.0330` (was the unanimous-3/3-contradicted `standard −0.0275` tie-broken label). **Final: `deep`.**
2. **`02_workflows_vs_agents__var_demanding`** — production now computes to `standard +0.0232` (was
   `light +0.0693`), corroborated by the averaged draw (2/3 vote `standard`). **Final: `standard`.**

The 3 remaining articles, finalized now by majority vote (2/3) rather than deferred to N=5:

3. **`08_react_practice__var_demanding`** — votes `standard, light, light`. Majority-vote and
   averaged-reward-argmax agree (both `light`). **Final: `light`.** Caveat carried forward: only
   this article's production draw was reviewed, not its replicates — a real asymmetry, but the
   2/3 majority doesn't depend on the review status of the dissenting draws to be valid evidence.
4. **`11_multimodal__var_standard`** — votes `light, skip, skip`. Majority-vote and
   averaged-reward-argmax agree (both `skip`). **Final: `skip`.** The most trustworthy of the three
   — both replicates were fully reviewed/corrected, not just production.
5. **`06_tools__var_demanding`** — votes `deep, light, light`. **This is the one case where the two
   decision methods disagree**: averaged-reward-argmax nominally says `deep` (but by a margin of
   only `+0.0013` — indistinguishable from a coin flip), while the majority-vote rule says `light`
   (2/3). Per the pre-registered decision rule (majority vote governs exactly this kind of
   disagreement, and was the ORIGINAL rule this investigation committed to before
   `merge_replicate_oracles.py`'s averaged-reward method existed), **final: `light`** — the
   near-zero averaged margin means there's no real substantive conflict, just two methods reporting
   the same underlying near-tie differently.
   **UPDATE (2026-08-20, A.16.0): this disagreement no longer exists.** After the ordinal-index bug
   fix, averaged-reward-argmax also computes `light` (+0.0101). Both methods now agree and the
   `light` label stands on strictly stronger evidence than when it was chosen.

**Net result: all 5 flagged articles are now finalized** — 2 by direct grade correction (`standard`,
`deep`), 3 by majority vote (`light`, `skip`, `light`). **APPLIED to production 2026-08-20 (A.16.7
Phase 1)** — see A.15.5.

### A.15.3 N=5 expansion — declined; N=3 accepted as final for all 24 TRAIN articles (2026-08-17)

A.14.2 flagged 3 lessons (`03_context_engineering`, `08_react_practice`, `09_RAG`) whose signal is
*noisier* under N=3 averaging on both near-tie rate and normalized advantage simultaneously, and a
prior pass of this section (2026-08-16) had built a targeted 12-article N=5 list around this plus
the 3 open flip candidates. **User decision (2026-08-17): skip N=5 entirely.** Rationale: A.13/A.14
already established a genuine, corpus-wide net gain in training-signal quality from N=3 (better
median margin, better mean normalized advantage — the number that actually scales the GRPO gradient
— modest deep-representation gains), and while that gain is uneven across lessons (3 of 8 get
noisier, A.14.2), the *aggregate* direction is favorable and real. Given this investigation has
already spent a multi-week detour on data-quality work (A.7 through A.15), the marginal value of a
further 96-cycle N=5 pass to disambiguate "genuinely harder to average" from "unlucky 2-replicate
draw" for 3 specific lessons is judged not worth the additional calendar time — the 3 previously-open
articles get finalized directly by majority vote instead (A.15.2), which is a legitimate use of the
existing N=3 evidence, not a shortcut around it.

**Consequence: N=3 (1 production + 2 replicates, temperature 0.7) is now the FINAL replication depth
for all 24 TRAIN articles.** No further TRAIN-side write+grade cycles are planned. The per-lesson
degradation for `03_context_engineering`/`08_react_practice`/`09_RAG` (A.14.2) is accepted as a known,
documented limitation of the N=3 pass rather than something requiring resolution before a retrain —
consistent with A.9's original framing that replication was never expected to fix everything.

### A.15.4 TEST replication — DONE (elevated from "optional" to a real priority, given A.15.1; completed 2026-08-25, all 16 TEST articles now N=3-replicated in production)

Given 12/15 scored TEST articles are CRITICAL/HIGH and they directly overlap the recurring failure
cluster, recommend **N=3 replication (1 production + 2 new draws, temperature 0.7, same
infrastructure as A.10/A.11/A.13 — reuses each article's existing `research.md`, zero new research
cost) for all 12 CRITICAL/HIGH TEST articles**: `Earth_Oceans_Origin`, `Gravity_Entropy`,
`Dark_Dimension`, `14_agent_system_design`, `07_reasoning_planning`, `Distinct_AI_Models`,
`04_structured_outputs`, `Space-Time_QECC`, `13_agent_framework`, `Bird_Eye_Extreme`,
`Understanding_Reasoning_LLMs`, `Insects_Consciousness`. Cost: 12 articles × 4 arms × 2 draws = **96
write+grade cycles** (TEST articles map directly to presets 0-3, no archived middle presets to
account for). The 3 MODERATE TEST articles (`29_evaluation_metrics`, `HNSW`, `31_CI`) are lower
priority — replicate only if budget allows after the CRITICAL/HIGH set.

**User decision (2026-08-17): run this now, and wait for it (plus the post-replication TEST signal
evaluation below) to complete before applying the 5 finalized TRAIN label corrections or starting
the retrain.** This reverses the earlier framing ("independent, non-blocking, can run in parallel")
— structurally TEST labels only feed §61 Stage 1's model-ranking comparisons, not GRPO training
directly, so nothing about A.12 step 6 *requires* this; the user is choosing to sequence it first
anyway, plausibly to get one consolidated, fully-validated state (TRAIN and TEST both
replication-checked) before committing GPU time, rather than revisiting TEST label confidence again
later. Generation is in progress (external LLM API calls, not GPU-bound); analysis is pending
completion.

**Post-replication TEST signal evaluation plan** (mirrors A.13/A.14's TRAIN analysis, adapted for
TEST's role as eval ground truth rather than a GRPO training target):
1. Re-run `merge_replicate_oracles.py` for the 12 replicated TEST articles to produce
   `article_oracle_averaged.json`-equivalent per-article averaged R_w/margin (TEST has no
   section-level GRPO consumer, so the section-level signal-quality metrics A.14 computed for TRAIN
   — sigma_floor/near_tie_margin/normalized-advantage — are not directly relevant here; the
   TEST-relevant output is the article-level `oracle_arm`/margin change, comparable to A.13.4's
   Step D).
2. Re-run `audit_oracle_margins.py` on the replicated TEST articles' averaged oracle to see whether
   any of the 12 CRITICAL/HIGH labels flip or erode/strengthen under averaging — same
   confirmed/flipped framework as A.13.4, applied to TEST instead of TRAIN.
3. Specifically check the recurring light↔deep confusion cluster (`13_agent_framework`,
   `Distinct_AI_Models`, `Bird_Eye_Extreme`, `Space-Time_QECC`, `Dark_Dimension` — all already in the
   replication list) for label flips, since this is the cluster that has driven every Stage 1 run's
   (`run26`/`27`/`28`/`29`) TEST failure pattern — if the TRUE oracle for any of these changes under
   replication, it directly revises the historical Stage 1 comparison, not just future runs.
4. Decide (same majority-vote-vs-averaged-argmax discipline as A.15.2) whether any TEST oracle
   labels should be corrected before treating §61's existing model comparisons as final.

**This does not change A.1's original distinction** (replication fixes label noise, not the `n=16`
sampling-noise floor) — TEST replication here is justified by a *different* rationale than A.6's
original one: not "make the eval more trustworthy in general," but "several of §61 Stage 1's
decisive TEST articles have oracle labels this thin, so the model-ranking conclusion itself needs
this check" — a sharper, more specific justification than the deferred original framing.

**Tooling fix required before execution (2026-08-18)**: `merge_replicate_oracles.py` and
`measure_replicate_noise.py::_compute_replicate_sections()` hardcoded TRAIN's variant preset mapping
(`geo._ARM_PRESETS` = `{skip:[0], light:[1], standard:[3], deep:[5]}`, flattened to `{0,1,3,5}`) with
no TEST-awareness. Running them as-is against TEST articles (which map presets **directly** `0→skip,
1→light, 2→standard, 3→deep` via `geo._TEST_ARM_PRESETS`) would have silently searched for a
nonexistent `preset5` directory and mis-attributed `preset2`/`preset3` reasoning.json data —
corrupting every downstream step. Fixed by adding `_arm_presets_for(article)`/`_arm_presets_flat_for(article)`
helpers to `measure_replicate_noise.py` (a hardcoded 16-name `_TEST_ARTICLES` set selects
`geo._TEST_ARM_PRESETS` instead of `geo._ARM_PRESETS`) and threading them through
`_compute_replicate_sections()`, `measure_article()`, and `merge_replicate_oracles.py::_discover_replicates()`.
Verified via a dry-run on `13_agent_framework` before running for real (correctly found 3 draws/arm,
15 sections). TRAIN call sites are unaffected (still default to `geo._ARM_PRESETS`).

**Results (executed 2026-08-18, `merge_replicate_oracles.py` + new `_test_replication_eval.py`;
CORRECTED 2026-08-20 — see explore-split bug below)**:

Step 1 (merge) succeeded for all 12/12 articles, writing `section_oracle_averaged.json` per article
(production `section_oracle.json` untouched).

**Second tooling bug found and fixed (2026-08-20, while investigating the ga-gate-threshold question
below)**: `merge_replicate_oracles.py`'s merged output never carried a v4+ `"explore"` sub-field, so
`compute_article_oracle.py::_compute_r_w()` silently fell back to its pre-Candidate-E pure
target-words-weighted mean for the *averaged* side, while the *production* side (real
`section_oracle.json`, which does carry `"explore"`) correctly used Candidate E's
split-weighted/simple-mean-explore aggregation — an apples-to-oranges mismatch between the two sides
of every "production vs averaged" comparison this investigation has made since A.13.4. Root-caused by
comparing a raw recompute against real production data for `14_agent_system_design` (R_w for
light/standard/deep off by +0.08 to +0.12 vs the real values; `skip`, which has zero explore credit,
matched exactly — the tell). Fixed in `measure_replicate_noise.py::_compute_replicate_sections()`
(now calls `geo._section_reward_components()` instead of `geo._section_reward()` and stores `explore`
alongside `rewards`) and `merge_replicate_oracles.py::merge_article()` (averages `explore` across
draws the same way it averages `rewards`, and writes it into `section_oracle_averaged.json`).
**Blast-radius check**: re-ran `quantify_defensible_gain_070.py`'s Step D for all 24 TRAIN articles
after regenerating their `section_oracle_averaged.json` with the fix — the tally is **unchanged**
(still 12 confirmed / 2 flipped / 10 hard-ruled, same specific articles, same votes); margins shifted
by ~0.003-0.006 in a few near-zero cases but no classification or A.15.2 correction changes. TRAIN's
finalized labels are unaffected. **TEST is materially affected** (regenerated below).

Step 2's naive production-vs-averaged-argmax comparison, post-fix:

| metric | count |
|---|---|
| CONFIRMED (averaged-argmax = production) | 4/12 |
| **FLIPPED** (averaged-argmax ≠ production) | 8/12 |

Applying the same **majority-vote-of-per-draw-winners** discipline established in A.15.2 (majority
governs over averaged-argmax when they disagree) gives a materially cleaner picture than both the
naive view above AND the pre-fix majority-vote pass reported earlier:

| article | tier | production | votes (prod, rep1, rep2) | majority vote | disposition |
|---|---|---|---|---|---|
| `Dark_Dimension` | CRITICAL | deep | deep, deep, standard | **deep** (2/3) | CONFIRMED (unchanged) |
| `14_agent_system_design` | CRITICAL | standard | standard, standard, light | **standard** (2/3) | CONFIRMED (unchanged) — averaged-argmax now agrees too, post-fix |
| `Distinct_AI_Models` | CRITICAL | deep | deep, standard, deep | **deep** (2/3) | CONFIRMED (unchanged) |
| `04_structured_outputs` | CRITICAL | standard | standard, standard, deep | **standard** (2/3) | CONFIRMED (unchanged) — was a 3-way-split UNRESOLVED before the fix |
| `Space-Time_QECC` | HIGH | light | light, standard, light | **light** (2/3) | CONFIRMED (unchanged) |
| `Bird_Eye_Extreme` | HIGH | light | light, standard, light | **light** (2/3) | CONFIRMED (unchanged) |
| `Understanding_Reasoning_LLMs` | HIGH | standard | standard, light, standard | **standard** (2/3) | CONFIRMED (unchanged) — was CORRECTED to `light` before the fix; the fix reverses that |
| `Earth_Oceans_Origin` | CRITICAL | standard | deep, deep, deep | **deep** (3/3) | **CORRECTED**: standard → deep |
| `Gravity_Entropy` | CRITICAL | standard | light, light, light | **light** (3/3) | **CORRECTED**: standard → light |
| `13_agent_framework` | HIGH | deep | deep, light, light | **light** (2/3) | **CORRECTED**: deep → light — was a 3-way-split UNRESOLVED before the fix |
| `Insects_Consciousness` | HIGH | light | light, deep, deep | **deep** (2/3) | **CORRECTED**: light → deep |
| `07_reasoning_planning` | CRITICAL | skip | skip, deep, light | **no majority** (3-way split) — **later found to itself be a bug, see correction below** | ~~UNRESOLVED~~ **CONFIRMED** |

Net (at the time): **7 confirmed, 4 corrected, 1 unresolved** — a substantially cleaner outcome than
the pre-fix pass (5 confirmed / 4 corrected / 3 unresolved). Two of the three previously-"unresolved"
3-way splits (`04_structured_outputs` and `13_agent_framework`) resolve to clean 2/3 majorities once
the aggregation is corrected; `07_reasoning_planning`'s apparent 3-way split turned out to be a
further instance of the same class of bug — see the correction immediately below.

> **Correction (2026-08-25): `07_reasoning_planning`'s "genuine 3-way split" was itself a script
> bug, distinct from the explore-split bug just fixed above.** `_test_replication_eval.py` computed
> each replicate's own vote using `sec_ids = list(avg_sections.keys())` — a **deduped** section-id
> list — instead of `_production_sec_ids()`, the digest-ordered-with-duplicates convention
> `merge_replicate_oracles.py` and `measure_replicate_noise.py::measure_article()` already used
> correctly (per A.16.0's original fix, which this one analysis script never received). For this
> specific article the two lists differ sharply (8 deduped entries vs. 16 digest-ordered, since its
> `research_digest.md` lists every section twice, same as the TRAIN quirk A.16.0 documented). Fixed
> `_test_replication_eval.py` to use `_production_sec_ids()`; re-run gives **votes=[skip, skip,
> skip], unanimous** — not a 3-way split. `07_reasoning_planning`'s production label (`skip`) was
> already correct; only its `needs_review` flag and the "sole unresolved article" framing throughout
> this section were wrong. **Net corrected outcome: 8 confirmed, 4 corrected, 0 unresolved** (of 12).
> `needs_review` cleared on `article_oracle.json` (was `True`, now `False`); see A.16.7 for the
> production-record update.

Step 3 (confusion cluster: `13_agent_framework`, `Distinct_AI_Models`, `Bird_Eye_Extreme`,
`Space-Time_QECC`, `Dark_Dimension`): **now fully resolved, no article left ambiguous**.
`Dark_Dimension`, `Distinct_AI_Models`, `Space-Time_QECC`, `Bird_Eye_Extreme` all CONFIRM their
original production label (unchanged). `13_agent_framework` — the one member that was genuinely
unresolved pre-fix — now shows a clean, confident **CORRECTION: deep → light** (2/3 majority: deep,
light, light). This is the single most consequential finding of this investigation for §61: since
`13_agent_framework` is one of the recurring TEST failure articles across `run26`-`29`, and its true
oracle appears to be `light` rather than the originally-labeled `deep`, those historical Stage 1
comparisons may have been scoring the model against the wrong ground truth on this article — worth
flagging explicitly before treating any of those runs' `13_agent_framework` verdict as settled.

**Step 4 decision (2026-08-20, supersedes the 2026-08-18 pass)**: apply these **4 corrections** to
TEST oracle labels under the same discipline as A.15.2's TRAIN corrections: `Earth_Oceans_Origin`
(standard→deep), `Gravity_Entropy` (standard→light), `13_agent_framework` (deep→light),
`Insects_Consciousness` (light→deep). Only **`07_reasoning_planning`** remains unresolved (genuine
3-way split: skip/deep/light) — leave it at its original production label (`skip`) for now, flagged
`needs_review`, pending N=5 expansion or manual grading review for this one article specifically.
**APPLIED to production 2026-08-20 (A.16.7 Phase 1)** — see A.15.5.

#### A.15.4 follow-up: does TEST show TRAIN's ga mean-drop, and does a lower gate threshold help? (2026-08-20)

§59.5 found that under N=3 averaging, TRAIN's raw `ga` (guideline_adherence) mean dropped sharply
(0.740 → 0.412) while its arm-neutral shape held — a real, sanity-checked cross-draft noise finding
(whether a draft happens to include every mandated visual element varies substantially draft-to-draft).
Question: does the same drop occur for TEST, and if so, would lowering the shipped `ga` gate
threshold (`_ga_gate_penalty()`, default 0.5, see `generate_episode_oracles.py`) clear up the label
instability found above?

**Part 1 — ga mean drop check (new `_test_ga_gate_threshold_sweep.py`, raw dimension extraction
across all 12 TEST articles' sections × arms)**:

| | n | mean | pass-rate (≥0.5) |
|---|---|---|---|
| production (single-draw) | 288 | 0.5938 | 59.4% |
| N=3-averaged | 288 | 0.5880 | 60.8% |

**No — TEST does NOT replicate TRAIN's ga drop.** The mean is essentially flat under averaging
(0.5938→0.5880, within noise) and the gate pass-rate slightly *increases* (59.4%→60.8%), the opposite
direction from TRAIN's collapse. TEST's single-draw ga baseline is also already substantially lower
than TRAIN's (59.4% vs TRAIN's ~74%-mean-implied baseline) — a separate, pre-existing difference
between the two corpora, not something averaging introduces.

**Part 2 — ga gate threshold sweep** (thresholds 0.50 down to 0.20, recomputing all 12 TEST articles'
per-draw oracle + votes at each threshold, same explore-split fix applied): **the classification
(7 confirmed / 4 corrected / 1 unresolved) is IDENTICAL at every threshold tested, 0.50 through 0.20 —
zero sensitivity.** No article's vote, majority, or disposition changes as the threshold is lowered.

**Conclusion: no, and the threshold sweep isn't the answer either.** Since ga isn't systematically
drifting under averaging for TEST (unlike TRAIN), there is no gate-miscalibration to correct by
lowering the threshold — and the sweep confirms this directly: the label instability found in this
TEST population is driven by genuine cross-draft variance in the content-quality dimensions
(cc/fl/de/be/cp), not by the `ga` gate firing inconsistently. Lowering the gate threshold would not
have "cleared" the landscape; the actual resolution (7/12 confirmed, 4/12 real corrections, 1/12
still genuinely ambiguous) came from fixing the explore-split aggregation bug above, not from touching
the gate. No change to the shipped `ga_gate_threshold=0.5` is warranted from this evidence.

*(Caveat: `07_reasoning_planning`'s raw-recomputation numbers in this specific sweep script disagree
with its real production `section_oracle.json` values for reasons not yet root-caused — isolated to
this one article, already the sole unresolved case, and does not affect the flat-threshold-sensitivity
finding since it holds identically across all 7 tested thresholds including 0.5.)*

> **CAVEAT RESOLVED (2026-08-20):** that discrepancy was the ordinal-index misalignment bug, now
> root-caused and fixed — see A.16.0. Re-run post-fix, Part 1 reads production ga mean 0.5868 →
> averaged 0.5845 (still essentially flat, still nothing like TRAIN's 0.740 → 0.412) and Part 2 is
> still **completely flat across thresholds 0.50 → 0.20**. Both conclusions stand unchanged.

#### A.15.4 detail: TEST margin/spread diagnostics (new `_test_margin_spread_detail.py`, 2026-08-20)

The TEST-side analogue of A.13.1 (noise floor) / A.13.2 (defensible share), not previously reported
for TEST at the section level — read-only, reads `section_oracle.json` (production) and
`section_oracle_averaged.json`'s `reward_sd` field (per-arm cross-draw std, written by
`merge_replicate_oracles.py`) for the 12 replicated TEST articles.

**Article margin distribution** (12 articles):

| | production | N=3-averaged |
|---|---:|---:|
| mean | +0.0210 | +0.0262 |
| median | +0.0175 | +0.0226 |
| min | −0.0032 | +0.0000 |
| max | +0.0455 | +0.0648 |
| \|margin\| < 0.02 (near-tie) | 7/12 | 6/12 |

Averaging nudges margins up slightly on average, but the population remains thin even after
averaging — half the articles are still within the near-tie band (expected, since A.15.1 selected
exactly the riskiest articles for replication).

**Cross-draw spread (cell sd), TEST vs TRAIN:**

| | TEST (12 articles, 288 cells) | TRAIN (A.13.1, 684 cells) |
|---|---:|---:|
| mean cell sd | **0.0804** | 0.0659 |
| median cell sd | 0.0577 | 0.0681 |

TEST is noisier on average than TRAIN, but with a right-skewed distribution (median < mean, the
reverse of TRAIN) — most TEST sections have TRAIN-like spread, but a handful of extreme outliers pull
the mean up.

**Per-article spread (mean/max cross-draw sd) and section-level flips:**

| article | tier | n_sec | mean_sd | max_sd | section flips |
|---|---|---:|---:|---:|---|
| `Earth_Oceans_Origin` | CRITICAL | 4 | 0.1017 | 0.2976 | 2/4 |
| `Gravity_Entropy` | CRITICAL | 5 | 0.0474 | 0.1528 | 3/5 |
| `Dark_Dimension` | CRITICAL | 3 | 0.0726 | 0.2622 | 2/3 |
| `14_agent_system_design` | CRITICAL | 6 | 0.0872 | 0.2716 | 4/6 |
| **`07_reasoning_planning`** | CRITICAL | 8 | **0.1719** | **0.4807** | 4/8 |
| `Distinct_AI_Models` | CRITICAL | 4 | 0.0740 | 0.1946 | 1/4 |
| `04_structured_outputs` | CRITICAL | 7 | 0.0559 | 0.2798 | 3/7 |
| `Space-Time_QECC` | HIGH | 5 | 0.0570 | 0.2646 | 1/5 |
| `13_agent_framework` | HIGH | 15 | 0.0482 | 0.2887 | 5/15 |
| `Bird_Eye_Extreme` | HIGH | 4 | 0.0963 | 0.1739 | 0/4 |
| `Understanding_Reasoning_LLMs` | HIGH | 8 | 0.0886 | 0.3478 | 3/8 |
| `Insects_Consciousness` | HIGH | 3 | 0.0793 | 0.2068 | 1/3 |

**`07_reasoning_planning`'s spread is more than double every other article's** (mean 0.1719 vs the
~0.05-0.10 range everyone else sits in). Its two worst sections (S4, S5 — the ReAct/Plan-and-Execute
"pros and cons" analysis) have cross-draw sd of 0.44-0.48, the largest in the whole TEST replication
set — real, substantial cross-draft content-generation instability. **Correction (2026-08-25): this
high spread does NOT, however, translate into an actual vote split** — the "3-way vote split" this
paragraph originally attributed to it was itself an artifact of a `_test_replication_eval.py` sec-id
bug (see the correction under A.15.4's main results table); the corrected, unanimous vote is `skip`
for all 3 draws despite this section-level noise. The high spread stat itself remains valid data,
just no longer explained as the cause of a split that never existed.

**Other notable findings**:
- **Section-level oracle flip rate**: 29/72 = 40.3% for this TEST subset vs TRAIN's corpus-wide
  46.2% — despite being the highest-risk TEST articles by construction, section-level flips are
  actually *lower* than TRAIN's average; article-level risk tier and section-level flip rate aren't
  tightly coupled.
- **Arm distribution shift under averaging** (section-level, all 12 articles): `skip` drops sharply
  (17→10), `light` and `deep` both gain (15→18, 19→22), `standard` holds steady (21→22). Averaging
  systematically pulls sections away from `skip` — consistent with the same deep/light-scarcity
  theme tracked on TRAIN since §54.7: single-draw grading appears to overcredit "good enough as-is"
  more than repeated draws support.
- **`13_agent_framework`** (15 sections, the largest article in this batch) has the *lowest* mean
  spread (0.0482) of the whole set, yet still had a genuine article-level label correction
  (deep→light) — low average section-level spread doesn't guarantee a stable article-level margin,
  since article R_w aggregates many low-noise sections whose small individual biases can still
  combine into a real net direction shift.

### A.15.5 Technical prerequisites — DONE (2026-08-20, A.16.7 Phase 1)

Built: (2) `train_grpo.py --use-averaged-oracle` — `load_section_groups()` reads
`section_oracle_averaged.json` when present, falling back to the single-draw file per-article; (3)
`compute_article_oracle.py --use-averaged` — recomputes article-level `oracle_arm`/margins from
averaged section rewards into a sibling `article_oracle_averaged.json`, run for all 24 TRAIN + 12
replicated TEST articles. All 5 TRAIN + 4 TEST corrections applied to production `article_oracle.json`
(backed up first to `bases_PRE_A16_LABELCORRECTIONS_20260820/`); `07_reasoning_planning` flagged
`needs_review` with oracle_arm left unchanged (this flag was cleared 2026-08-25 once its apparent
3-way split was found to be a script bug — see A.15.4's correction note). See A.16.7 for the full
account, including why the 7
non-already-correct corrections needed `compute_article_oracle.py`'s `_MANUAL_OVERRIDES` mechanism
rather than trusting the automated `--use-averaged` recompute (its S3/S4/S5 near-tie tie-break still
disagreed with the majority-vote-governed decision for these exact articles).

### A.15.6 Recommended sequence and the honest cost/time trade-off (updated 2026-08-17: N=5 declined, TEST replication now sequenced first)

| phase | items | cost | blocks retrain? |
|---|---|---|---|
| 1 (**done**, 2026-08-16) | Reviewed/corrected TRAIN grades; 2 of the original 4 flip candidates resolved directly (A.15.2) | zero further cost — complete | No |
| 1b (**done**, 2026-08-17) | N=5 declined; all 5 flagged TRAIN articles finalized at N=3 via majority vote (A.15.2) | zero further cost — complete | No |
| 2 (**done**, 2026-08-18) | N=3 TEST replication, 12 CRITICAL/HIGH articles (A.15.4, 96 cycles) | 96 write+grade cycles — complete | No further (done) |
| 3 (**done**, 2026-08-20) | TEST signal evaluation (A.15.4's 4-step plan): re-merged, re-audited margins, checked the light↔deep confusion cluster specifically. A 2nd tooling bug (explore-split aggregation, see A.15.4) was found+fixed mid-analysis; corrected result: 7 confirmed, 4 corrected (`Earth_Oceans_Origin`→deep, `Gravity_Entropy`→light, `13_agent_framework`→light, `Insects_Consciousness`→deep), 1 unresolved 3-way split (`07_reasoning_planning` — left at production label pending N=5/manual review). ga-gate-threshold follow-up: TEST does not replicate TRAIN's ga mean-drop, and threshold sweeps (0.5-0.2) show zero classification sensitivity — no gate recalibration warranted | zero cost, pure analysis — complete | No further (done) |
| 1c (**done**, 2026-08-20) | Built A.12 steps 2/3 (`train_grpo.py --use-averaged-oracle` loader flag + `--section-weight confidence` + `compute_article_oracle.py --use-averaged` variant); applied the 5 finalized TRAIN labels + 4 finalized TEST corrections to production `article_oracle.json` (A.16.7 Phase 1/2) | zero generation cost, engineering complete | No further (done) |
| 4 (GPU, **ready to launch**) | The joint retrain (A.12 step 6): C2 (not `run26`'s ordinal mechanism, per A.16.4/A.16.5) + finalized TRAIN labels + averaged oracle + confidence weighting | one training run | — |

> **Correction (2026-08-25):** phase 3's "1 unresolved 3-way split (`07_reasoning_planning`)" was
> itself a `_test_replication_eval.py` script bug (deduped vs. digest-ordered section ids); fixed,
> and the corrected vote is unanimous `skip` — no unresolved TEST articles remain. See A.15.4.

**Sequencing note**: phases 2-3 (TEST) don't structurally need to precede 1c/4 — TEST labels feed
§61 Stage 1's model-ranking comparisons, not the GRPO training target itself. The user has chosen
to sequence them first anyway (2026-08-17), for one consolidated, fully-validated state before
committing GPU time rather than revisiting TEST confidence after a retrain. This investigation's
multi-week data-quality detour (A.7 through A.15) is nearly concluded — TEST replication (already
running) plus its evaluation is the last data-quality step before the code wiring (1c) and the
actual retrain (4).

## A.16 Pre-retrain audit: is N=3 actually worth retraining on, is there formula headroom left, and does A.8 still stand? (2026-08-20)

Prompted by the user's pre-sign-off question. Everything below is derived from data already on
disk (zero LLM calls, zero GPU), using `train_grpo.py::load_section_groups()`'s **exact** flat-filter
/ near-tie / advantage arithmetic so the numbers are the ones training would actually see.

New read-only tools: `training/_compare_label_sets_for_training.py`,
`training/_replication_retrain_analysis.py`, `training/_disagreement_vs_margin.py`,
`training/_rescore_stage1_corrected_labels.py`.

### A.16.0 THIRD tooling bug found and fixed — ordinal-index misalignment (invalidated ~9% of every replicate cell)

While validating a recompute against production `section_oracle.json`, an 8.9% cell-level mismatch
surfaced that could not be explained by the formula. Root cause, confirmed exactly:

**Every one of the 24 TRAIN `research_digest.md` files lists each section TWICE** (e.g.
`06_tools__var_standard`: 18 `<section id=...>` tags for 9 real sections). `generate_episode_oracles.py`
builds `sec_ids = _extract_sec_ids_ordered(digest)` *without deduplication*, so it iterates 2n times
and each section's stored value is the one written on the **second** pass — computed at ordinal
index `n+i`, not `i`. `_get_score()` only uses that ordinal as a **fallback** when exact/substring
title matching fails, but for the ~9% of cells where it does fall back, index `i` and `n+i` return
**different graded entries**.

`merge_replicate_oracles.py` passed the *deduped* `list(section_oracle["sections"].keys())`
(indices `0..n-1`) into `measure_replicate_noise._compute_replicate_sections()`. So for ~9% of cells
the **production draw** (read from the stored file, computed at `n+i`) was being averaged against
**replicate draws computed at `i`** — an apples-to-oranges average present in every replication
result since A.13. Verified decisively: recomputing with the deduped list reproduces production for
623/684 cells (91.1%); recomputing with the full digest-ordered list reproduces it for **684/684
(100.0%)**.

Fixed by adding `measure_replicate_noise._production_sec_ids(article)` (returns the digest-ordered
list, duplicates deliberately preserved) and threading it through `merge_replicate_oracles.merge_article()`,
`measure_replicate_noise.measure_article()`, and the A.15.4/A.16 analysis scripts. All 24 TRAIN + 12
TEST `section_oracle_averaged.json` files regenerated.

**Blast radius — what actually moved:**

| result | before fix | after fix | verdict |
|---|---|---|---|
| TRAIN article-level Step D (A.13.4) | 12 confirmed / 2 flipped / 10 hard-ruled | **11 / 3 / 10** | `06_tools__var_demanding` now flips to `light` |
| TEST A.15.4 (12 articles) | 7 confirmed / 4 corrected / 1 unresolved | **7 / 4 / 1 (identical)** | fully robust |
| A.15.2's 5 finalized TRAIN labels | — | **all 5 unchanged** | 4 reinforced, 1 weakened justification |
| A.15.4's 4 TEST corrections | — | **all 4 unchanged** | robust |

Two things are worth stating plainly. First, **the fix strengthens rather than undermines A.15.2**:
`06_tools__var_demanding` was A.15.2's single awkward case, where averaged-argmax nominally said
`deep` (+0.0013) while majority-vote said `light`, and the pre-registered rule had to break the tie.
Post-fix, averaged-argmax **also** says `light` (+0.0101) — both methods now agree, and the
already-chosen label stands on stronger evidence. Second, `02_workflows_vs_agents__var_demanding`'s
justification weakens: A.15.2 cited a "2/3 vote `standard`", but the corrected per-draw votes are
`standard, deep, light` — a 3-way split with no majority. Its label (`standard`) still stands
because both production and averaged-argmax agree, but the vote-based half of that argument should
be considered withdrawn.

**Lesson (third instance of the same class)**: before trusting any tool on this corpus, verify it
reproduces production `section_oracle.json` **cell-for-cell** first. All three bugs found in this
appendix (TRAIN-only preset mapping, missing `explore` split, ordinal-index misalignment) were
silent, produced plausible-looking numbers, and would each have propagated into the retrain.

### A.16.1 How reliable is a single draw, really? (the number this whole detour was chasing)

Per-section argmax agreement across the 3 draws, shipped C2 formula, all 171 TRAIN sections:

| pattern | count | share | iid-random null |
|---|---:|---:|---:|
| unanimous (3/3) | 37/171 | **21.6%** | 6.3% |
| majority (2/1) | 95/171 | 55.6% | 56.3% |
| 3-way split (1/1/1) | 39/171 | **22.8%** | 37.5% |

Pairwise: `prod-rep1` 33.9%, `prod-rep2` 39.8%, **`rep1-rep2` 46.8%**. Only the `rep1-rep2` pair is
unbiased — the 2026-08-16 correction pass reviewed production drafts far more than replicates, so
`prod-repN` is deflated by construction and should not be quoted as the reliability figure.

**Two independent drafts of the same section agree on the best arm 46.8% of the time, against a
~26% chance rate given the observed marginal distribution — Cohen's κ ≈ 0.28, "fair" agreement at
best.** Under a simple uniform-error model this implies a **single-draw label accuracy of ~65%**,
which N=3 majority voting lifts to roughly **70-75%**. That is a real improvement, and it is also
the honest ceiling: at this per-draw reliability, N=5 would reach only ~76% and N=7 ~80%. **No
feasible replication depth produces clean labels.** This is the single most important quantitative
result in this appendix, and it reframes the entire replication programme: N=3 bought a genuine but
bounded improvement, and further N-expansion has clearly diminishing returns (retroactively
supporting A.15.3's decision to decline N=5, for a better reason than the one originally given).

**Crucially, the unreliability is not uniform — it is concentrated exactly where the decision
doesn't matter:**

| averaged margin | n | rep1=rep2 agreement | 3-way split | mean regret of worst nominee |
|---|---:|---:|---:|---:|
| 0.00 – 0.02 | 38 | **21.1%** | 42.1% | 0.0402 |
| 0.02 – 0.04 | 38 | 36.8% | 28.9% | 0.0450 |
| 0.04 – 0.08 | 50 | 54.0% | 18.0% | 0.0621 |
| 0.08 – 0.15 | 27 | 59.3% | 11.1% | 0.0738 |
| ≥ 0.15 | 18 | **83.3%** | 0.0% | 0.0882 |

Agreement rises monotonically from 21% to 83% as the margin grows. **Where the arm choice is
decisive, the labelling process is reliable; where it is near-tied, it is barely better than a coin
flip — but picking wrong there costs little.** Note however that expected regret from disagreement
(≈ `(1−agreement) × regret`) is roughly **flat at ~0.025-0.033 across every bucket** — so the noise
is not *free* at the decisive end either, it is simply rarer there. 44.4% of sections sit below the
`sigma_floor=0.04` margin with only 28.9% draw-agreement; 55.6% sit above it with 61.1% agreement.

### A.16.2 Does N=3 better prepare the next retrain? — mixed, and NOT via signal strength

Both label sets scored through `load_section_groups()`'s exact logic (`sigma_floor=0.04`,
`near_tie_margin=0.06`):

| quantity | single-draw | N=3-averaged | direction |
|---|---:|---:|---|
| trainable groups (survive flat-filter) | 171 | 165 | worse (−6) |
| **STRICT constant-predictor bar** (§60.12's success criterion) | 29.2% | **30.9%** | **worse (+1.7pp)** |
| **NEAR-TIE constant-predictor bar** | 56.7% | **54.5%** | **better (−2.2pp)** |
| label entropy (bits) | 1.980 | 1.974 | ~flat |
| `sigma_floor_fraction` | 21.1% | **27.3%** | worse (+6.2pp) |
| mean \|advantage\| | 0.8188 | 0.8061 | ~flat |
| median section margin | 0.0446 | **0.0497** | better |
| **oracle arm CHANGES vs single-draw** | — | **75/165 = 45.5%** | — |

**The honest read: N=3 does not make the training signal meaningfully stronger. Aggregate
trainability metrics are a wash or slightly worse** (6 fewer groups, 6pp more denominator-clamping,
flat advantage magnitude, and the strict trivial bar actually goes *up*). **What it does is change
45.5% of the training targets.** The case for retraining on averaged labels therefore rests entirely
on those new targets being *more correct* — which A.16.1 supports (~65% → ~70-75% accuracy) but does
not make overwhelming.

This is a materially more sober conclusion than A.13/A.14's framing. It does not say the replication
was wasted — a ~5-10pp absolute gain in label accuracy across 45% of the training set is real, it is
the largest single lever this investigation has actually validated, and it cost no GPU time. It does
say **replication alone should not be expected to break §60.12's invariant** (no run beating its own
trivial baseline under healthy entropy), because that invariant is about the *strict* bar, and the
strict bar gets slightly *harder* under averaging.

### A.16.3 Is there formula headroom left? Should `ga` / `fl` be demoted further? — Mostly no; `ga` demotion is actively wrong

All candidates re-scored on N=3-averaged TRAIN labels using the **correct aggregation order**
(full formula per draw, then average the 3 final rewards — i.e. what `merge_replicate_oracles.py`
actually does, avoiding §59.5's documented raw-dimension-averaging caveat):

| candidate | grps | sk/li/st/dp | STRICT bar | NEAR bar | floor% | \|adv\| | medMrg | labels changed |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| **`C2_shipped`** | 165 | 47/51/33/34 | 30.9% | 54.5% | 27.3% | 0.806 | 0.0497 | — |
| `fl_halved(0.10)` | 166 | 50/52/32/32 | 31.3% | 56.6% | 33.1% | 0.784 | 0.0450 | 8 |
| `fl_dropped(0.00)` | 165 | 50/53/30/32 | 32.1% | 57.0% | **35.8%** | 0.781 | 0.0439 | 20 |
| `cc_halved(0.10)` | 163 | 46/50/34/33 | 30.7% | 55.8% | 31.9% | 0.800 | 0.0453 | 6 |
| `cc_dropped(0.00)` | 165 | 48/49/35/33 | **29.7%** | 57.0% | 33.9% | 0.783 | 0.0447 | 11 |
| `cc+fl_halved,de/be_up` | 163 | 41/48/37/37 | 29.4% | **53.4%** | 28.2% | 0.795 | **0.0526** | 18 |
| `ga_pen_005` | 166 | 52/46/34/34 | 31.3% | 63.9% | 30.7% | 0.799 | 0.0465 | 8 |
| **`ga_pen_000` (ga removed)** | 167 | 48/47/34/38 | 28.7% | **63.5%** | 31.1% | 0.793 | **0.0380** | 17 |
| **`ga_pen_015`** | 165 | 48/52/31/34 | 31.5% | **52.7%** | **20.0%** | **0.816** | **0.0515** | 5 |
| `ga=0,cc+fl_halved` | 161 | 46/47/31/37 | 29.2% | **64.6%** | **42.2%** | 0.776 | **0.0311** | 22 |
| `C2_cost-0.02` | 166 | 41/44/37/44 | **26.5%** | 60.2% | 26.5% | 0.792 | 0.0462 | 12 |
| `C2_cost-0.05` | 169 | 61/55/27/26 | 36.1% | 59.2% | 21.9% | 0.822 | 0.0500 | 16 |
| **`run26_ORD_cost-0.06`** | 170 | **70/66/25/9** | **41.2%** | 61.2% | 11.8% | 0.836 | 0.0600 | 41 |

**Finding 1 — demoting `ga` further is clearly wrong, and the data points the other way.** Removing
the gate entirely (`ga_pen_000`) is among the worst candidates tested: near-tie bar blows out to
63.5% (from 54.5%), median margin collapses 0.0497 → 0.0380, `floor%` worsens. The maximal-demotion
variant (`ga=0, cc+fl` halved) is worse still on every axis (`floor%` 42.2%, medMrg 0.0311, near-tie
bar 64.6%). Conversely **`ga_pen_015` — *promoting* `ga`, not demoting it — is the single best
candidate in the table on section-level trainability** (best `floor%` 20.0%, best `|adv|` 0.816,
best near-tie bar 52.7%, second-best medMrg) **while changing only 5 labels.** §53.6/F2's finding
that `ga`'s *raw additive signal* was ~97% noise remains true and is not contradicted — but that is
precisely why C2 converted it from an additive term into a **gate**, and the gate is evidently doing
useful work that a larger penalty does more of. Note the honest counterweight: §54.6/§59.5.1 found
`C3`(=pen 0.15) costs *more* thin-margin **articles** (22 vs 19) even as it helps **sections** —
GRPO trains on sections, evaluation happens on articles, so this is a real trade-off, not a free win.

**Finding 2 — demoting `fl` is clearly wrong.** Despite `fl`'s tiny arm-spread on averaged data
(§59.5.4: 0.1053 → 0.0448), halving or dropping it *degrades* the section-level signal substantially
(`floor%` 27.3% → 33.1% → 35.8%; median margin 0.0497 → 0.0450 → 0.0439). The mechanism is
intuitive in hindsight: a low-*spread* dimension still contributes to the spread, and removing it
pushes more sections below `sigma_floor`. Low `armSprd` justified not *gating* `cc`/`fl` (§59); it
does **not** justify removing them.

**Finding 3 — `cc` is the only genuinely arguable demotion, and the gain is small.** `cc_dropped`
lowers the strict bar 30.9% → 29.7% and balances the distribution slightly, but pays `floor%`
27.3% → 33.9%. `cc+fl_halved, de/be_up` is the most interesting compound variant (best near-tie bar
53.4%, best median margin 0.0526, `floor%` roughly neutral at 28.2%) — but it changes 18 labels,
which is a lot of unvalidated movement for a marginal gain.

**Conclusion on formula headroom: essentially exhausted for the "which dimensions" question.** Part 7
already searched this space thoroughly and §59.5 confirmed its choices survive averaging; this
re-run on the *correct* aggregation order confirms it again and closes the two specific demotion
questions negatively. **The one cheap, well-evidenced experiment still worth running is
`ga_pen_015`** — 5 label changes, best-in-table section-level metrics, and it is a one-line change.

### A.16.4 The finding that should change the retrain plan: `run26`'s mechanism is badly mismatched to the corrected TEST distribution

**Correction (2026-08-20, prompted by a direct user question): the comparison below was originally
built on mismatched units and has been redone.** The first pass compared `run26`'s TRAIN
**section-level** `deep` share (9/170 = 5.3%, a raw tally of each of the ~170 individual GRPO
training groups' own best arm) against the corrected TEST **article-level** `deep` share (4/16 =
25%, `article_oracle.json`'s single `oracle_arm` per article, itself the argmax of a
target-words-weighted R_w aggregated across ALL of that article's sections). These are not the same
unit: an article's `oracle_arm` is not a majority vote of its sections' individual winners, so a low
section-level share does not mechanically imply a low article-level share, or vice versa. New tool
`_article_level_formula_check.py` redoes this at a consistent unit — for each candidate formula,
aggregate each of the 24 TRAIN articles' N=3-averaged section rewards into an article-level R_w
(target-words-weighted mean of "rest" + simple mean of "explore", the real Candidate E aggregation,
matching `compute_article_oracle.py::_compute_r_w()` — not a naive flat mean), take the argmax per
article, and tally that distribution — the proper TRAIN-side analogue of TEST's article-level share.

**Result: the corrected, apples-to-apples comparison is even more extreme than the original, not less.**

| label set (unit: articles, n=24 TRAIN / n=16 TEST) | sk/li/st/dp | `deep` share |
|---|---|---:|
| `run26_ORD_cost-0.06` on averaged TRAIN, **article-level** | 9/15/0/0 | **0.0%** |
| `C2_shipped` on averaged TRAIN, **article-level** | 5/11/4/4 | **16.7%** |
| **corrected TEST (A.15.4), article-level** | 2/7/3/4 | **25.0%** |

**Under `run26`'s ordinal-cost mechanism, `deep` wins the article-level aggregate for ZERO of the 24
TRAIN articles** — not even `standard` survives (0 articles land on `standard` either; every article
collapses to `skip` or `light`). This is a starker version of the same mechanism already documented
corpus-wide (§54.7 onward, Stage 0.2's warning that this exact variant is "the one most likely to
reproduce deep-representation collapse") — the harsher ordinal per-round cost (a full unit step
`skip:0→light:1→standard:2→deep:3`, vs H0's diminishing-marginal-cost units `light:1.00→
standard:1.88→deep:2.31`) doesn't just under-represent `deep` at the margin, it eliminates it (and
`standard`) entirely as an article-level winner on this TRAIN corpus. `C2_shipped`'s 16.7% is still
below TEST's 25%, but it is the only one of the two formulas that produces a `deep`-representative
TRAIN label set at all — training `run26`'s formula against a TEST set that is 25% `deep` means the
model would never see an article-level `deep` training target, full stop, not merely a scarce one.

*(Sanity-checked one case directly: `10_memory_knowledge_access__var_demanding` — corrected to
`deep` in production under the shipped `C2` formula (A.15.2/A.16.7) — recomputes to `light` under
`run26`'s formula (R_w: skip=0.211, light=0.281, standard=0.250, deep=0.242), consistent with the
harsher cost term suppressing `deep` even where the shipped formula clearly favors it.)*

This is a mechanistic explanation for `run26`'s already-documented failure mode (it missed 2 of the
3 `deep` TEST articles by predicting `light`) — one that survives, and is reinforced by, fixing the
original section/article unit mismatch.

### A.16.5 Re-scoring §61 Stage 1 under the corrected TEST labels — `run26`'s claimed superiority does not survive

A.15.4 corrected 4 of the 16 TEST oracle labels. Every §61 Stage 1 comparison was scored against the
*old* labels. Re-scoring the saved per-article predictions (no GPU, no re-inference):

| run | exact (orig) | exact (corrected) | MAE (corrected) | **vs. its own trivial baseline** (orig → corrected) |
|---|---:|---:|---:|---|
| `run26_costcoef_only` @ep146 | 8/16 | **9/16** | 0.625 | +2 → **+2 articles** |
| `run29_costcoef05` @ep94 | 7/16 | **9/16** | 0.688 | +1 → **+2 articles** |
| `run28_garatreat_only` | 6/16 | 6/16 | 1.250 | +0 → −1 articles |
| `run27_debecurve_only` @ep110 | 4/16 | 6/16 | 1.125 | −2 → −1 articles |

(The TEST trivial "always predict `light`" baseline itself rises from 6/16 = 37.5% to 7/16 = 43.8%
under the corrections, which is why baseline-relative scoring is mandatory here — per §60.12.)

**§61's Stage 1 addendum concluded that "`run29` underperforms `run26` on every single metric",
and used that to close the H0-unit branch and crown `run26`'s ordinal-unit mechanism. Under the
corrected labels that statement is false: the two tie on exact (9/16) and tie baseline-relative
(+2 articles each).** `run26` retains a modest edge on MAE (0.625 vs 0.688) and miss count (3 vs 4)
— it is still nominally ahead — but the evidence that the *ordinal unit convention* is load-bearing
is now much thinner than §61 claimed, resting on a one-article MAE difference at n=16.

A caution against over-reading this too: all four runs are near-constant `light` predictors (`run26`
predicts `light` for 14 of 16 TEST articles), so **every** label correction toward `light` helps all
runs and every correction away from it hurts all runs, nearly identically. That is exactly why the
raw exact% moved a lot while the ranking barely did — and it is an independent reminder that these
models are not yet doing much beyond the trivial baseline.

### A.16.6 Does A.8 (confidence-weighted training) still stand? — Yes, and it is now the best-evidenced remaining lever

**Strongly reaffirmed, and for a concrete reason that did not exist when A.8 was written.** A.8
proposed a `--section-weight confidence` mode that down-weights sections whose margin is small
relative to their measured noise. At the time this was speculative: there was no per-label sd. Now:

1. **The per-label sd exists.** `section_oracle_averaged.json` carries `reward_sd` per section/arm,
   for all 24 TRAIN articles. The input A.8 needs is already computed and on disk.
2. **A.16.1 shows the signal it would exploit is large and monotone**: draw-agreement runs from 21%
   to 83% across the margin spectrum. A weighting function keyed on margin/sd is not guessing — it
   is tracking a directly measured 4× reliability gradient.
3. **A.16.2 shows why plain averaging is not enough on its own.** N=3 changes 45.5% of targets but
   leaves aggregate trainability flat and the strict trivial bar slightly higher. Confidence
   weighting is the mechanism that converts better-measured labels into a better *gradient*, rather
   than just a differently-labelled one.
4. **44.4% of sections have margin < `sigma_floor` and only 28.9% draw-agreement.** Under the current
   uniform/hybrid weighting these contribute gradient at full strength. They are the most plausible
   single explanation for §60.12's invariant that this investigation has produced.

Concretely, the reliability-vs-volume curve it would trade along (TRAIN, averaged):

| keep sections with margin ≥ | sections kept | draw-agreement |
|---|---:|---:|
| 0.00 (current) | 171 (100%) | 46.8% |
| 0.04 | 95 (55.6%) | 61.1% |
| 0.08 | 45 (26.3%) | ~68% |
| 0.15 | 18 (10.5%) | 83.3% |

A soft weighting (not a hard cut) is the right shape here — hard-cutting to margin ≥ 0.15 would
leave 18 sections, far too few. This remains "one new weighting function, no additional generation."

### A.16.7 Recommended roadmap

**Phase 0 — data integrity (do first, ~zero cost). DONE (2026-08-20).** Built
`training/verify_oracle_reproducibility.py`: recomputes every `bases/*/section_oracle.json` cell
(`rewards`, `explore`, `oracle` arm) by calling `generate_episode_oracles.py::process_article_variant()`
itself in a new read-only mode (`dry_run=True, return_data=True`, added this pass — no other behavior
change) rather than a parallel re-implementation, since re-implementation is exactly how bug #3
(A.16.0) was introduced elsewhere. Diffs against the stored file and exits non-zero on any mismatch,
for CI/pre-job use.

**First real run, full `bases/` corpus (52 article dirs): 49/52 reproduce exactly, 3 fail.** The 3
failures are all one-off ablation pilots — `05_workflow_patterns__depthboost`,
`10_memory_knowledge_access__var_goldremoved`, `11_multimodal__depthboost` — none are part of the
24 TRAIN / 16 TEST corpus this investigation's retrain plan targets. Root cause confirmed distinct
from A.16.0's three bugs: these 3 files are `section_oracle.json` **version 4** (pre-`diagnostics`
field), while every core-corpus file is **version 5** — they were generated once and never
regenerated after the C2/H0/J0 formula shipped, so they are simply stale, not corrupted. This is
exactly the kind of drift Phase 0 is meant to catch (a label file silently no longer matching the
live formula) — regenerate them via `generate_episode_oracles.py` before using them for anything, or
exclude them from any corpus-wide sweep until then. **The 24 TRAIN + 16 TEST core corpus is fully
verified reproducible (100%).**

**Phase 1 — apply the finalized labels (zero GPU, needs sign-off). DONE (2026-08-20).** Backed up
affected `article_oracle.json` files to `bases_PRE_A16_LABELCORRECTIONS_20260820/`, then applied.
Of A.15.2's 5 TRAIN corrections, 2 (`10_memory_knowledge_access__var_demanding`→deep,
`02_workflows_vs_agents__var_demanding`→standard) were already correct in production (fixed at the
data layer by the 2026-08-16 grade correction, confirmed unchanged) — no write needed. The other 3
(`08_react_practice__var_demanding`→light, `11_multimodal__var_standard`→skip,
`06_tools__var_demanding`→light) plus all 4 of A.15.4's TEST corrections
(`Earth_Oceans_Origin`→deep, `Gravity_Entropy`→light, `13_agent_framework`→light,
`Insects_Consciousness`→deep) needed an actual write. `07_reasoning_planning` left at `skip`,
`needs_review` set `True` with a note explaining the unresolved 3-way split (later found itself to
be a script bug, not a real split — corrected 2026-08-25, `needs_review` cleared, see A.15.4).

**Important finding while applying**: `compute_article_oracle.py --use-averaged`'s own automated
near-tie tie-break (S3/S4/S5, reading a single arm's article text) still disagreed with the
majority-vote-governed decision for these exact 7 articles even after the A.16.0 ordinal-index fix
(e.g. it picks `deep` for both `06_tools__var_demanding` and `13_agent_framework`, not `light`) —
confirming the pre-registered majority-vote rule was necessary, not just a historical artifact of
the earlier bugs. The 7 corrections were therefore applied via `compute_article_oracle.py`'s
existing `_MANUAL_OVERRIDES` mechanism (same pattern as its 3 pre-existing entries), not by trusting
the automated recompute — this also makes the corrections durable: any future `--force` regeneration
(single-draw OR `--use-averaged`) reproduces the same corrected label instead of reverting.

Built A.12 steps 2/3:
- `compute_article_oracle.py --use-averaged`: sources R_w from `section_oracle_averaged.json`
  instead of the single-draw file, writing a **sibling** `article_oracle_averaged.json` (production
  `article_oracle.json` never touched by this flag). Run for all 24 TRAIN + 12 replicated TEST
  articles — the general-purpose "A.12 step 3" artifact now exists for the whole replicated corpus.
- `train_grpo.py --use-averaged-oracle`: `load_section_groups()` now reads
  `section_oracle_averaged.json` when present (falling back to single-draw per-article), and
  exposes each group's winning-arm cross-draw `reward_sd` for Phase 2.

**Phase 2 — build A.8's confidence weighting (zero GPU). DONE (2026-08-20).** Added
`--section-weight confidence` to `train_grpo.py`: `wordcount × (margin / max(reward_sd,
sigma_floor))`, where `margin = max(R) − 2nd-best(R)` and `reward_sd` is the winning arm's cross-draw
std (0.0 / degrades to margin-only when `--use-averaged-oracle` isn't also passed — a warning is
logged if `confidence` is requested without it). Validated the arithmetic against real
`06_tools__var_standard` data: weights span **12 to 1610** (>100× spread) between the noisiest
low-margin section and the cleanest high-margin one — behaving exactly as intended, not degenerate.

**Phase 3 — the retrain, with three changes from the current plan:**
1. **Use `C2` (`cost_coef=-0.03`, H0 units), NOT `run26`'s ordinal `-0.06`.** A.16.4 shows `run26`'s
   mechanism produces `deep` as the article-level winner for **0 of the 24** averaged TRAIN articles
   (vs `C2`'s 16.7%) against a 25% corrected-TEST `deep` share, and A.16.5 shows its claimed
   superiority over `run29` does not survive the label correction. Its apparent Stage 1 win was
   measured on labels now known to be wrong on 4 of 16 articles, and baseline-relative it ties a run
   §61 had already rejected.
2. **Train on averaged labels + confidence weighting together**, not averaged labels alone —
   A.16.2 is explicit that averaging by itself does not strengthen the signal.
3. **Judge it baseline-relative from the start** (§60.12): the averaged label set's own bars are
   **30.9% strict / 54.5% near-tie**, and the corrected TEST bar is **43.8% strict**. Pre-register
   these before the run so the result cannot be read optimistically after the fact.

**Phase 4 — one cheap formula probe, only if Phase 3 disappoints.** `ga_pen_015` (A.16.3): 5 label
changes, best-in-table section-level metrics, one-line change. Do **not** pursue further `ga`/`fl`
demotion — A.16.3 closes both negatively.

**What to stop doing.** Further reward-formula search has hit clear diminishing returns: Part 7,
§59.5, and A.16.3 have now each independently converged on the same shape. Further N-expansion of
replication is also closed — A.16.1's κ ≈ 0.28 means even N=7 reaches only ~80% label accuracy.
**If Phase 3 still fails to beat its own trivial baseline under healthy entropy, the binding
constraint is neither the reward formula nor label noise, and the investigation should move to the
remaining untested hypothesis from §60.12: the input representation** (what `build_rl_input` shows
the model), plus A.9's structural limits (8 TRAIN topics, `n=16` TEST) — neither of which any amount
of formula or replication work can address.

### A.16.8 `compute_article_oracle.py` retires the EPS_BAND/S3/S4/S5 near-tie tie-break — pure mean-R_w argmax is now the single decision mechanism (2026-08-25)

**What changed.** Every mechanism described above and in A.15 that decided close calls by anything
other than "take the arm with the highest mean R_w" has been removed from `compute_article_oracle.py`:
`EPS_BAND` (the flat 0.02→0.03 near-tie threshold), `MIN_DELTA_S3/S4/S5` and their three text-based
tie-break signals (`_s3_bloat()` bullet/heading-density bloat check, `_s4_structure()` structural
compliance check, `_s5_stability()` cross-draw coefficient-of-variation check), the short-lived
hard-vote-with-per-draw-tiebreak design (`_decide_hard_vote()`/`_decide_single_draw()`, built and
rejected within this same investigation), and the `article_oracle_averaged.json` sibling file /
`--use-averaged` CLI flag that let `article_oracle.json` and its averaged counterpart disagree on
`oracle_arm` for the same article. All of it is gone from the source file, not merely superseded in
prose.

**What replaced it.** `_decide()` now does exactly this, for every article:

1. If `external_evidence_policy == "forbidden"`, return `skip` (hard constraint, unchanged).
2. Else if the article is in `_MANUAL_OVERRIDES` (11 entries, unchanged — the 4 finalized TEST
   corrections from A.15.4/A.16.7 Phase 1 plus 7 earlier corrections all still apply), return that
   arm.
3. Else rank all 4 arms by **mean R_w across every available draw** (the `section_oracle_averaged.json`
   cross-draw mean when it exists — same file `train_grpo.py --use-averaged-oracle` reads at the
   section level, unaffected by anything in this note — falling back to the single production draw's
   `section_oracle.json` otherwise) and take the argmax. No text is read, no S3/S4/S5 signal is
   computed, no threshold decides a winner other than R_w itself.

**The confidence flag changed meaning too.** `needs_review` used to mean "S3/S4/S5 had to break a
tie inside `EPS_BAND`." It now means `margin < ARTICLE_MARGIN_NOISE_SD / sqrt(n_draws)`, where
`ARTICLE_MARGIN_NOISE_SD = 0.054` is the empirically measured cross-draw standard deviation of the
article-level margin itself, pooled across all 40 replicated corpus articles (n=40, not a
per-article or per-arm quantity) — a direct noise-floor comparison rather than a fixed, uncalibrated
threshold. It shrinks by `1/sqrt(n_draws)` for articles with more replicate evidence, matching how
averaging actually reduces uncertainty.

**Why the switch, briefly (full reasoning earlier in this session, not reproduced here in full):**
averaging genuinely reduces variance while discretizing-then-voting throws away the very magnitude
information that makes averaging valuable in the first place; S3/S4/S5 were syntactic proxies
calibrated only against the N=1 era and never validated against the N=3 replication data that now
exists for the whole corpus; and concrete cases (`13_agent_framework`, `Gravity_Entropy`) showed the
tie-break mechanism regressing on articles the corpus's own hand-corrected labels had already fixed,
while pure mean-R_w argmax got them right without any override at all. A "cheapest-arm fallback" for
low-confidence cases was also considered and rejected: it moved 8/12 low-confidence articles and did
so 100% toward cheaper arms (the near-tie bands are asymmetrically populated by cheaper competitors),
which would have erased 2 of the corpus's already-scarce `deep` labels and double-counts cost that is
already priced into R_w via the `nr` term. Low-confidence articles are flagged (`needs_review=True`)
and reported as-is, with no forced alternative decision.

**Net effect on the 40-article core corpus (24 TRAIN + 16 TEST), verified by full regeneration
against a pre-change backup (`bases_PRE_A16_MEANRW_20260825/`):** 36/40 articles keep the same
`oracle_arm` as under the retired mechanism; 4 TEST articles flip, all previously sitting on a
mechanism-dependent knife-edge and now flagged `needs_review=True`:

| article | old (retired mechanism) | new (mean-R_w argmax) | new margin |
|---|---|---|---:|
| `04_structured_outputs` | standard | **deep** | +0.0000 |
| `Bird_Eye_Extreme` | light | **standard** | +0.0078 |
| `Distinct_AI_Models` | deep | **light** | +0.0036 |
| `HNSW` | light | **deep** | +0.0139 |

No TRAIN label changes. 12/40 articles total are flagged `needs_review=True` under the new
threshold (up from the old mechanism's smaller, differently-defined set, since the definitions of
"close call" are no longer comparable). `article_oracle.json` is the only oracle file that exists
now — `article_oracle_averaged.json` has been deleted for all 40 core-corpus articles (both
production `bases/` and the `bases_design_c/` mirror, A.18.6) and `test_grok_planner.py`/
`_run31_run33_failure_analysis.py` were both updated to read `article_oracle.json` directly, with
no more averaged-sibling preference check. GRPO training itself is unaffected either way — it never
read either article-level file (A.18.6 traces this in code) — so this change only affects
**evaluation scoring** (`test_grok_planner.py`) and any analysis in this document that reports
`oracle_arm`/margin. A.17.1, A.17.4, and A.18.6 have all been recomputed against the new mechanism;
A.15.4/A.15.5/A.15.6 and A.18.6a describe the now-retired mechanism and should be read as history,
not current behavior.

### A.16.9 Mechanics reference: how `article_oracle.json` and `article_oracle_averaged.json` were built, before the retirement above (2026-08-25; relocated from A.18.8, 2026-08-28 — not Design-C-specific, just filed there by accident of timing)

Prompted by a direct question about how the two views were generated, back when both existed. The
recurring confusion is that this pipeline contained **two distinct combination operations**, both
loosely called "averaging," which are easy to conflate: (1) averaging **across independent draws**
of the same section, done once, upstream, at the section level; and (2) rolling up **across an
article's sections** into one R_w-per-arm vector, done identically by both views' code. Only the
first one is what "`_averaged`" in the filenames referred to. Illustrated below with real, on-disk
numbers (not a hypothetical) from two articles, as they stood before the retirement above.

**Step 1 — section level: 1 draw vs. 3 draws.** `06_tools__var_standard`, section S4
("Implementing a Tool-Calling Framework From Scratch", `target_words=560` of 3590 total, 15.6% of
the article's weight):

| | skip | light | standard | deep |
|---|---:|---:|---:|---:|
| 1 production draft (`section_oracle.json`) | 0.1000 | 0.0700 | 0.0436 | **0.6490** |
| average of 3 independent draws — production + 2 replicates, all temp 0.7 (`section_oracle_averaged.json`) | 0.1000 | 0.0700 | 0.0997 | **0.4620** |
| cross-draw sd (of those 3 draws) | 0.000 | 0.000 | 0.051 | **0.197** |

The single production draft happened to write an unusually strong `deep` version of this specific
section (0.649). Two more independently-written drafts scored the same arm markedly lower on the
same section; averaging all 3 pulls it down to 0.462, with a large spread (sd 0.197, a ~30% swing
around the mean) — real, substantial cross-draw noise on exactly the arm/section this investigation
has repeatedly found least reliable (A.16.1). `skip`/`light` barely move because they carry almost
no exploration (`de`/`be`) content to grade inconsistently. **Nothing article-level has happened
yet** — this is a pure per-section, per-arm noise-reduction step.

**Step 2 — article level: the *same* rollup code, fed either section-level file as input.**
`compute_article_oracle.py::_compute_r_w()` computes one R_w-per-arm vector for the whole article by
a target-words-weighted mean across all 9 of this article's sections — identical code regardless of
which section-level file it reads:

| | skip | light | standard | deep | `oracle_arm` | margin |
|---|---:|---:|---:|---:|---|---:|
| canonical (`article_oracle.json`, from `section_oracle.json`) | 0.1096 | 0.2594 | 0.2970 | **0.3808** | `deep` | +0.0839 (unique winner, margin ≫ `EPS_BAND=0.03`) |
| averaged (`article_oracle_averaged.json`, from `section_oracle_averaged.json`) | 0.1460 | 0.2300 | 0.2309 | **0.2648** | `deep` | +0.0339 (still a unique winner, but ~2.5× thinner) |

Same label both ways on this article — but the confidence collapses once the one noisy section is
averaged down. This is the mechanism, one step short of an actual flip.

**Step 3 — when a flip actually happens: the near-tie tie-break fires.** `HNSW`, full-article R_w
(no single-section breakdown needed — the effect is visible directly at the article level):

| | skip | light | standard | deep | `oracle_arm` | how it was decided |
|---|---:|---:|---:|---:|---|---|
| canonical | 0.2016 | **0.4331** | 0.3058 | 0.3487 | `light` | unique winner, margin +0.0845 (clears `EPS_BAND` easily) |
| averaged | 0.2949 | 0.4380 | 0.3273 | **0.4519** | `deep` | **near-tie** (`light`, `deep` both within `EPS_BAND=0.03` of the leader) → S4/S5 tie-break: S4 (structural compliance) `deep=1.000` vs `light=0.725` already separates them, so it decides the winner before S5 (`light=0.970` vs `deep=0.881`, the opposite direction) is even consulted |

Averaging barely moves `light` (0.4331→0.4380) but pulls `deep` up substantially (0.3487→0.4519) —
enough to turn a clean unique win for `light` into a near-tie against `deep`. Once inside the
near-tie band, `_decide()` stops looking at R_w altogether and falls through to the S4 (structural
compliance) → S3 (bloat) → S5 (stability) tie-break signals. (`HNSW`'s oracle has since been
overridden a second time, on entirely different — distributional/variance — grounds; see A.19.)

**The one thing that was never averaged across draws, in either view: the tie-break evidence
itself.** S3/S4/S5 were computed by reading the actual generated `article.md` text of the
**original production episode only** — never anything from the replicate drafts under
`noise_experiment/`, which existed solely to produce alternate reward *numbers* for Step 1, not
alternate candidate *articles* for a tie-break to read. So the `_averaged` view was precisely:
*averaged R_w ranking, resolved (when it's close) with un-averaged tie-break evidence* — a real,
structural seam, not an implementation bug. This asymmetry was one of the motivating factors behind
retiring the whole tie-break mechanism above.

**`_MANUAL_OVERRIDES` sat above all three steps and was applied identically to both files** — it
was checked first, unconditionally, before R_w was even ranked — which is why canonical and
`_averaged` never disagreed on any of the manually-overridden articles, only on a handful of
corpus-wide cases where neither file was overridden and Step 3's near-tie mechanism genuinely fired
differently for each.

---

## A.17 Post-retrain evaluation: `run33/ep81` — failure modes and the real headroom for a downstream LLM corrector (2026-08-24)

> **Correction (2026-08-25): `run31/ep109` removed from this section.** Phase 3 ran three times
> (`run30`, `run31`, `run33`); this section originally analysed the two checkpoints selected as each
> run's best-on-TEST-ordinal-MAE, `run31_averaged_confidence/epochs/epoch_0109` and
> `run33_averaged_confidence/epochs/epoch_0081`. `run31/ep109`'s checkpoint files are no longer
> present on disk and cannot be re-run or re-verified; it was also not the stronger of the two
> checkpoints on the metrics that matter (TRAIN sat at its own trivial baseline, 37.5%, vs `run33`'s
> 54.2%, while matching `run33` only on TEST MAE). All run31 rows,
> columns, and comparative language have been removed from A.17; every table and finding below is
> `run33/ep81`-only. Historical run31 figures are not reproduced here to avoid presenting unverifiable
> numbers as current; consult prior versions of this document (or session history) if the original
> comparison is needed for the record.

All numbers below are re-derived from the saved report files by `_run31_run33_failure_analysis.py`
(retained under its original name — the script itself still supports both checkpoints, only this
write-up now reports `run33` alone), which reparses every per-article block and recomputes every
headline metric rather than trusting the report footer. **Self-check: the recomputed exact/near/miss,
MAE and regret figures reproduce the report's own footer exactly, and the recomputed R_w top-2
margins reproduce A.15.1's margin audit to 4 decimal places** — the parser is measuring the same
quantities the rest of this investigation measures.

### A.17.0 Provenance — why this checkpoint's numbers are trustworthy where `run30`'s were not

The report contains an explicit `Infer server is ready. Serving adapter: .../epochs/epoch_0081` line,
and its log additionally shows `Stopping stale infer server (adapter changed)…` firing at the end of
the sweep. This is the `_infer_config.py` fix working as intended. It matters because the preceding
`run30` round produced two eval files that were later proven byte-identical (a stale infer subprocess
silently served an older adapter across two "different" evaluations), which invalidated a full round
of conclusions. **Every number in A.17 is adapter-attributed at the log level; `run30`'s pre-fix
numbers should not be compared against them.**

**Second correction (2026-08-24): `_read_oracle()` sourced R_w from the wrong file for every
replication-corrected article, and this section's regret figures have been recomputed.** The eval
harness's regret metric compared each model's choice against `article_oracle.json`'s R_w — the
original single, un-replicated production draft — even for the 9 articles whose `oracle_arm` was
decided from replicated/averaged evidence instead. Fixed in `test_grok_planner.py::_read_oracle()`
to prefer `article_oracle_averaged.json`'s R_w when present (same file the label itself was decided
from); `oracle_arm_idx` is unaffected (always read from `article_oracle.json`, and the two files never
disagree on the label since manual overrides apply to both unconditionally). **Exact/near/miss/MAE
are untouched by this fix (label-only, no R_w involved); every regret number in A.17 below has been
recomputed and superseded** — no new inference was needed, since the models' choices don't change,
only which R_w they're scored against. See A.17.5 for the material consequence: the regret budget's
composition changes enough to reverse one of A.17.8's original recommendations.

### A.17.1 Headline results, baseline-relative (§60.12 discipline)

> **Correction (2026-08-25): `compute_article_oracle.py` now uses pure mean-R_w argmax as the
> single canonical decision mechanism (see A.16.8) — the EPS_BAND/S3/S4/S5 near-tie tie-break and
> the canonical-vs-`_averaged`-sibling-file split are both retired.** All 40 core-corpus
> `article_oracle.json` files were regenerated under this mechanism. 36/40 are unchanged; 4 TEST
> articles flip: `04_structured_outputs` (standard→deep), `Bird_Eye_Extreme` (light→standard),
> `Distinct_AI_Models` (deep→light), `HNSW` (light→deep) — all four margins are thin enough to be
> flagged `needs_review=True` under the new noise-floor-based confidence check. No TRAIN label
> changes. The numbers below are recomputed directly from `article_oracle.json` against the SAME
> `run33/ep81` RL+guards picks already on record (no new inference needed — the model's choices
> don't change, only which labels they're scored against), superseding the `29_evaluation_metrics`
> correction below, which is now folded into this broader update.

> **Correction (2026-08-27): the `HNSW` manual override (A.19) moves one more TEST label** —
> `deep`→`light` — on distributional/variance grounds (A.19.2-A.19.3), not a further mean-R_w
> mechanism change. This flips `HNSW` from a MISS back to an EXACT hit and moves `light` from a
> tie with `deep` to TEST's unique majority class. All figures below are recomputed accordingly;
> see A.19.4/A.19.5 for the fuller post-flip baseline audit (all 4 trivial arms, guarded variants,
> bootstrap CIs).

The trivial predictor for each split is the majority-class constant: TRAIN → always `P0 skip` (9/24).
**TEST's oracle distribution is now P0=2/P1=6/P2=4/P3=4 — `light` is the unique majority class**
(6/16, no longer tied with `deep`). Regret aggregates exclude forbidden-policy articles throughout,
matching `test_grok_planner.py`.

| | TRAIN baseline | `run33/ep81` TRAIN | TEST baseline (always-light) | `run33/ep81` TEST |
|---|---:|---:|---:|---:|
| exact | 9/24 (37.5%) | **13/24 (54.2%)** | 6/16 (37.5%) | **11/16 (68.75%)** |
| ordinal MAE | 1.083 | **0.583** | 0.875 | **0.375** |
| regret mean | +0.0967 | +0.0109 | +0.0230 | **+0.0127** |
| regret max | +0.1661 | +0.0672 | +0.0648 | **+0.0599** |

Two honest observations:

1. **`run33` beats the trivial TEST baseline on every metric, more decisively than any prior
   version of this table** — exact 68.75% vs 37.5%, MAE 0.375 vs 0.875 (57% reduction), regret mean
   0.0127 vs 0.0230 (45% reduction), regret max 0.0599 vs 0.0648. Post-`HNSW`-flip, the exact-match
   *count* is 11/16, one better than every prior version of this table (10/16) — `HNSW` itself
   supplies that gain, moving from MISS to EXACT.
2. **This clears the significance threshold, and remains unchanged by the `HNSW` flip.**
   Recomputing the discordant-pair table against the `always-light` baseline: `run33` is right and
   baseline wrong on `04_structured_outputs`, `Dark_Dimension`, `Earth_Oceans_Origin`,
   `State_of_LLM_Reasoning`, and `Understanding_Reasoning_LLMs` (`b=5`); zero cases of baseline
   right/model wrong (`c=0`). **One-sided exact McNemar: `p = 0.5^5 = 0.03125`, significant at the
   conventional 0.05 threshold.** `HNSW` doesn't appear in either the `b` or `c` set here — before
   the flip it was "both wrong" against this specific baseline (model picked `light`, baseline is
   `light`, oracle was `deep`); after the flip it becomes "both correct" — a set membership change
   that leaves `b`/`c`, and therefore `p`, exactly as they were. See A.19.5 for the full post-flip
   McNemar audit against all four trivial arms (not just `light`).

**The simple majority-class baseline itself, in full.** Scored the same way as the model: ordinal
MAE over all articles, regret mean/max over the non-forbidden subset.

| | TRAIN baseline | TEST baseline (always-light) |
|---|---:|---:|
| exact | 9/24 (37.5%) | 6/16 (37.5%) |
| ordinal MAE | 1.0833 | 0.8750 |
| regret mean | +0.0967 | +0.0230 |
| regret max | +0.1661 | +0.0648 |

TRAIN's baseline is completely unaffected (no TRAIN label changed). TEST's baseline is `always-light`
alone now — the `HNSW` flip breaks its prior tie with `always-deep` (which drops to 4/16, no longer
reported here as a majority-class candidate; see A.19.4 for `always-skip`/`always-standard`/
`always-deep`'s own full stats). This is the number `run33` is being compared against; it is not
itself a fixed target and moves whenever a label is corrected.

### A.17.2 The single largest correctable defect is not in the model — it is that `--rl-only` bypasses the policy guard

`test_grok_planner.py --rl-only` reads `rl_recommendation.preset` directly. That value is
cost-rule-adjusted (`apply_cost_sensitive_rule`) but **not** policy-guarded. Every production path is
guarded: `preset_planner_handler.fallback_aggregator` forces `P0` under `policy=forbidden`, and
`_apply_policy_guards` clamps Grok's output the same way. **No production path can ever emit the
numbers in A.17.1.**

The `forbidden → P0` rule is a hard guideline constraint, not a learned one, and
`compute_article_oracle.py` implements it as a pre-argmax short-circuit ("-1. Hard constraint:
forbidden policy → skip, regardless of R_w"). It holds **9/9** across the corpus (8 TRAIN + 1 TEST)
and is derivable from TRAIN alone at 8/8. Critically, `_rl_preset.py::build_rl_input()` **strips the
`external_evidence_policy` flag from the model's input by design** (see A.17.3) — so the RL stage is
architecturally incapable of applying this rule, and the guard is not a patch over a model weakness
but the component that was always meant to own the constraint. Applying it costs nothing and leaks
nothing:

| | `run33/ep81` TRAIN | `run33/ep81` TEST |
|---|---:|---:|
| exact, RL-only | 13/24 (54.2%) | 10/16 (62.5%) |
| exact, **RL + guards** | **20/24 (83.3%)** | **11/16 (68.75%)** |
| MAE, RL-only | 0.583 | 0.4375 |
| MAE, **RL + guards** | **0.208** | **0.375** |

All figures confirmed directly against `run33`'s freshly-regenerated `epoch81` reports (TEST figures
reflect the `HNSW` manual override, A.19; regret is guard-invariant on TEST since the only
forbidden-policy article is excluded from the regret aggregate either way — see A.17.9).

The TRAIN gain is enormous (+7 articles) because 8 of the 24 TRAIN articles are forbidden-policy
`var_minimal` variants and the model gets **1/8** of them right unaided — it predicts `P1 light` on
essentially every one. The TEST gain is a single article (`State_of_LLM_Reasoning`) because TEST
contains only one forbidden-policy article.

> **Reporting correction going forward:** `--rl-guards-only` — which already exists and already
> implements exactly this clamp — is the correct RL benchmark. The `--rl-only` figure is a lower
> bound on a configuration that is never shipped, and quoting it understates the RL stage by 33
> percentage points on TRAIN.

### A.17.3 Failure modes — TRAIN

Signed error (`pick − oracle`) decomposed by policy:

| checkpoint | scope | n | over | exact | under | mean signed |
|---|---|---:|---:|---:|---:|---:|
| `run33/ep81` | forbidden | 8 | 7 | 1 | 0 | +1.125 |
| `run33/ep81` | non-forbidden | 16 | 2 | 12 | 2 | −0.062 |

**TRAIN failure mode 1 — the `forbidden` subset is not a model failure at all; it is a measurement
artefact.** Mean signed error is `+1.125` on the forbidden subset, i.e. the model never encodes the
constraint. **Verified root cause:** `_rl_preset.py::
build_rl_input()` *deliberately strips the flag before the model ever sees it* —

> ```python
> # external_evidence_policy is article-level: "forbidden" short-circuits the
> # entire exploration phase upstream (before the section-level model is called);
> # "allowed"/"required" are passed to the downstream article-level aggregator.
> # Strip it here so the section-level model sees only per-section signals.
> digest_meta = re.sub(r"\s*<external_evidence_policy>[^<]*</external_evidence_policy>", "", digest_meta)
> ```

This is **correct architecture, not a defect**: the section-level scorer is designed to score
sections, and the article-level hard constraint is deliberately delegated to the downstream policy
guard. The model is therefore being scored, under `--rl-only`, on information it was architecturally
denied — and it is doing the only thing it can. **`--rl-only` is measuring a configuration that is
not merely unshipped but incoherent by design.** This makes A.17.2 not an optional improvement but a
correction of an invalid measurement.

> **Superseded claim.** An earlier draft of this section read this as "a strong, concrete instance of
> §60.12's input-representation hypothesis." That was wrong, and the code above refutes it: the flag
> is not missing by oversight, it is removed on purpose. No input-representation change is warranted
> here.

**TRAIN failure mode 2 — mild under-prediction on the remaining 16.** Once the forbidden articles
are removed, the signed error is slightly *negative* (−0.25 / −0.06) — the opposite direction. The
model is not globally biased; the `+0.167` / `+0.333` all-TRAIN mean is entirely an artefact of the
forbidden subset.

**Prediction concentration (TRAIN):** `run33` predicts `P0=1, P1=15, P2=5, P3=3` against an oracle
distribution of `P0=9, P1=8, P2=3, P3=4`. The model emits `P0` once in 24 attempts against 9 true
`P0` labels — the `skip` class is effectively collapsed.

### A.17.4 Failure modes — TEST

**Prediction concentration (TEST):** `run33`'s own RL vote (pre-guard) is `P0=0, P1=11, P2=1, P3=4`
against an oracle of `P0=2, P1=6, P2=4, P3=4` (post `HNSW`-flip, A.19; this vote-count line describes
the model's raw prediction pattern, which does not depend on which oracle it is scored against, so
it is unaffected by the flip — see A.17.9 for the guard-clamped final `chosen` distribution).
`run33` never emits `P0` in its own vote on TEST (the guard supplies it once, on the one
forbidden-policy article), and emits `P2` exactly once.

**TEST failure mode 1 — the policy is ~2/3 the trivial baseline by construction.** `run33`'s TEST
predictions are **identical to the always-`P1` baseline on 11/16 articles (69%)** — this count
compares predictions to the constant baseline directly and is unaffected by the oracle correction.

> **Correction (2026-08-25, mean-R_w mechanism switch, see A.17.1):** decomposed against the
> `always-light` baseline under the corrected oracle, `run33` **gains** five articles the baseline
> misses (`04_structured_outputs` P3, `Dark_Dimension` P3, `Earth_Oceans_Origin` P3,
> `State_of_LLM_Reasoning` P0, `Understanding_Reasoning_LLMs` P2) and **loses zero** — this is the
> same `b=5, c=0` discordant-pair count behind A.17.1's now-significant McNemar result. **The entire
> measured skill of this checkpoint over the trivial predictor is five articles**, not three as
> previously reported — `04_structured_outputs` is a genuinely new gain (its corrected oracle,
> `deep`, now matches `run33`'s own `deep` pick), and `Distinct_AI_Models`'s flip (deep→light) makes
> its oracle equal the baseline too, so it drops out of the discordant set entirely rather than
> counting either way.

**TEST failure mode 2 — errors concentrate on near-tied labels.** Margins for `run33`'s TEST errors,
read directly from the regenerated `article_oracle.json` files (updated 2026-08-27 post `HNSW`
flip, A.19 — `04_structured_outputs` and `HNSW` are no longer in this list, both now EXACT):

| article | margin | needs_review |
|---|---:|---|
| `07_reasoning_planning` | 0.0167 | yes |
| `14_agent_system_design` | 0.0373 | no |
| `29_evaluation_metrics` | 0.0198 | no (manual override) |
| `Bird_Eye_Extreme` | 0.0184 | yes |
| `Insects_Consciousness` | 0.0599 | no (manual override) |

`run33`'s current 5 TEST errors (A.19.4's confusion matrix: `07_reasoning_planning`,
`14_agent_system_design`, `29_evaluation_metrics`, `Bird_Eye_Extreme` NEAR; `Insects_Consciousness`
MISS) sit on a mix of thin and clearer margins: only `07_reasoning_planning` and `Bird_Eye_Extreme`
(2 of 5) are flagged `needs_review` under the confidence check (`ARTICLE_MARGIN_NOISE_SD/√3 ≈
0.031`) and are not yet distinguishable from noise in the oracle itself. The other 3 are not simple
noise-floor artifacts: `14_agent_system_design`'s margin (0.0373) genuinely clears the shrunk
threshold; `29_evaluation_metrics` and `Insects_Consciousness` are both manual-override labels
(A.15.4/A.19), `needs_review=False` by construction rather than by margin size.

**TEST failure mode 3 — two errors trace to manual-override labels, but the two are NOT the same
kind of case (checked directly against `article_oracle.json` provenance, 2026-08-24).** Both
`13_agent_framework` and `Insects_Consciousness` have `oracle ≠ argmax(R_w)`:

| article | oracle | argmax(R_w) | `run33` pick | regret of the model's pick |
|---|---|---|---|---:|
| `13_agent_framework` | P1 (override) | P3 | P1 | 0.0000 (exact) |
| `Insects_Consciousness` | P3 (override) | P1 | P1 | **−0.0460** |

**Correction (2026-08-24): this is not a case of "the downstream LLM should catch what a
section-level scorer missed," and the original wording below overstated that.** Both overrides come
from the same source — `compute_article_oracle.py`'s `_MANUAL_OVERRIDES`, applied per A.15.4's
**majority-vote-of-replicated-draws** rule (production draw + 2 independent replicate re-draws of
the full write-and-grade pipeline at all four presets; see A.15.4's vote table): `Insects_Consciousness`
was `light, deep, deep` → majority **deep** (2/3), overturning the single production draw's own
`light`. This is a different mechanism from the two genuinely-inspection-based overrides in the same
dict (`06_tools__var_minimal`, `11_multimodal__var_demanding`, commented "R_w winner overridden after
inspection") — Insects_Consciousness's correction is pure cross-draw noise-averaging, not qualitative
judgment.

Three pieces of direct evidence show this specific correction is not something a downstream
reasoner (Grok or otherwise) could have derived, even with full article-level context:

1. **The replication data that flipped the label does not exist at inference time, for any article.**
   Producing it means writing and grading two *additional* complete hypothetical drafts at all four
   presets (`measure_replicate_noise.py` consumes `noise_experiment/<article>__replicateR__preset{P}/
   reasoning.json` — full alternate write-and-grade runs, not a re-read of the same digest). This is
   an offline, expensive, label-construction-only procedure run once against the fixed 40-article
   corpus. Neither the RL model nor Grok ever has access to it live — both only ever see the single
   production draft's *pre-exploration* evidence (digest, gap profile, coverage table). There is no
   channel through which "examining article-level context" could recover a 2-vs-1 replicate outcome
   that was never shown to either component.
2. **The evidence that *is* available (the single production draft's own section breakdown) already
   agrees with `light`, not `deep`** — checked directly against `bases/Insects_Consciousness/
   article_oracle.json`'s per-section `rewards`: S2 ("a growing awareness", 44.7% of article weight,
   the single largest section) favours `light` over `deep` by 0.6325 vs 0.4882; S3 ("mindful
   relations", 23.7% weight) favours `light` 0.6775 vs 0.5382. Only S1 (the intro, 31.6% weight)
   favours `deep`. The article-level aggregate of the *same* evidence Grok's guided brief is built
   from is internally coherent with the RL model's pick — there is no separate article-level signal
   sitting in that evidence for a downstream stage to notice.
3. **Independent corroborating signals that this is noise, not signal:** `article_oracle.json` already
   carries `"low_signal_flag": true` for this article (a pre-existing, unrelated methodology flag
   from `compute_article_oracle.py`, set when any gate diagnostic sits below threshold); the article
   is thin (`n_sections=3`, 1,900 target words — a small aggregate is intrinsically more volatile);
   and the flip is a bare 2/3 majority, not unanimous. All of this is consistent with A.16.1's
   corpus-wide finding that single-draw label reliability is only κ≈0.28 ("fair") — a 2-1 flip on a
   thin article is the expected behaviour of that noise floor, not an anomaly requiring an
   explanatory story about missed context.

**Revised conclusion:** on `Insects_Consciousness` specifically, the RL model's `P1` pick is not
"secretly correct" (A.16's whole discipline is not to over-read a single R_w comparison that way),
but the `P3` label it is scored against is a low-confidence, noise-driven correction that neither the
RL model nor Grok could have reproduced from the context either one actually receives. This one
article should be treated as an unreliable evaluation point (a plausible `needs_review` candidate —
though `07_reasoning_planning`'s own `needs_review` flag was later cleared, 2026-08-25, once its
apparent 3-way split turned out to be a script bug rather than genuine ambiguity, see A.15.4), not
as evidence of a downstream-correction opportunity. `13_agent_framework`'s override shares the same
majority-vote provenance and warrants the same caveat, though there the model happens to land on the
corrected label anyway (exact hit, regret 0.0000), so it does not affect A.17.5's regret accounting.

**Addendum (2026-08-24): the "noise-driven" framing above overstated the case; hard-vote and
soft-vote actually agree here.** Checking `article_oracle_averaged.json`'s own un-overridden
`r_w_rewards` (soft-vote: R_w from `section_oracle_averaged.json`'s cell-averaged rewards, computed
independently of the manual-override mechanism) gives **deep=0.579 vs light=0.519** — the
continuous-averaging method *also* picks `deep`, agreeing with the discrete majority vote
(`light, deep, deep` → 2/3). Two independent aggregation methods converge on `deep`; only the
single, un-replicated production draft (n=1) dissents. This is better evidence for `deep` than a bare
2-1 split would be, and the earlier "probably noise" framing should be softened accordingly. The
structural point stands regardless: both methods require the offline replicate drafts, which are
unavailable to the RL model or Grok at live inference time either way — so this remains an
unreliable-for-scoring, not a downstream-correctable, case; it's now better described as "probably a
real but inference-time-unrecoverable label" than "probably noise."

**Third addendum (2026-08-24): the eval harness itself was scoring this article against the wrong
R_w, and this is now fixed — the exact-match/regret "conflict" for `Insects_Consciousness` is
resolved, not just re-explained.** `test_grok_planner.py::_read_oracle()` was reading R_w from
`article_oracle.json` (the single production draft) even where `article_oracle_averaged.json`
exists — meaning the harness computed regret against the *same* draft that originally (wrongly)
favoured `light`, regardless of which evidence actually justified the `deep` label. Fixed to prefer
the averaged file's R_w when present (§ A.17.0). Recomputed for this article: regret goes from the
originally-reported **−0.0460** (implying the model's `light` pick "beats" the oracle) to
**+0.0599** (the model's pick genuinely costs reward relative to `deep`) — now in full agreement
with the MISS verdict. **This was never really a case of "exact-match and regret disagree"; it was
a data-plumbing bug making them disagree.** All regret figures elsewhere in A.17 have been
recomputed on the same basis — see A.17.5.

<details>
<summary>Original wording (2026-08-24, superseded above — kept for the record)</summary>

On `Insects_Consciousness` the model is scored a **MISS** for choosing the arm that actually earns
*more* measured reward than the labelled oracle arm. Any downstream corrector that "fixes" this
article improves exact-match while making the pipeline measurably worse on the objective the reward
function encodes. **Exact-match accuracy and reward-regret genuinely disagree on this corpus**, and
that disagreement is created by the hand-assigned labels, not by the model.

</details>

### A.17.5 Where the regret actually lives — revised after the `HNSW` manual override (2026-08-27)

**Superseded again: this section previously reported +0.1598 total regret (post `29_evaluation_
metrics` N=3 promotion, pre `HNSW` flip). That figure is now stale.** Recomputed with `HNSW`'s
manual override to `light` (A.19), which turns its own regret to exactly 0 (chosen==oracle), total
TEST regret after guards for `run33/ep81` is **+0.1912** across the 15 non-forbidden articles —
an increase, not a decrease, from +0.1598, because the flip does not touch any of the 5 articles
that were already errors; it simply removes `HNSW` from the error set entirely (it was not one of
the 4 articles the old total was computed over), and the 15-article denominator now excludes a
formerly-non-error, non-contributing article the same as before either way. (`HNSW` was, and
remains, regret=0 under `run33`'s own chosen arm both before and after the flip — only its role as
an *error* changed, from MISS pre-flip to already-EXACT under the label the model always picked.)

| article | regret | share of budget | transition needed | reachable by Grok today? |
|---|---:|---:|---|---|
| `Insects_Consciousness` | +0.0599 | **31.3%** | P1 → P3 | **no — escalation guard** |
| `07_reasoning_planning` | +0.0495 | **25.9%** | P1 → P0 | yes (demotion) |
| `14_agent_system_design` | +0.0373 | **19.5%** | P1 → P2 | **no — escalation guard** |
| `29_evaluation_metrics` | +0.0261 | **13.7%** | P3 → P2 | **yes (demotion, 1 step — already within `_COST_RULE_MAX_STEP`)** |
| `Bird_Eye_Extreme` | +0.0184 | **9.6%** | P1 → P2 | **no — escalation guard** |

**These 5 articles account for the entire TEST regret budget** (31.3+25.9+19.5+13.7+9.6 = 100.0%,
by construction — every other TEST article is an exact hit with 0 regret). Three of the five are
blocked by the escalation guard (`Insects_Consciousness`, `14_agent_system_design`,
`Bird_Eye_Extreme` — all require escalating an RL vote of `P1` to `P2` or higher, which the guard
forbids); the other two are single-step demotions, already permitted.

**The escalation-guard recommendation still reverses, on the current numbers.** The three blocked
errors carry a *combined* regret of **+0.1156** (was +0.0842 pre-flip, since `HNSW`'s removal from
the error set doesn't change any of these three articles' own regret — the increase is a
renormalization artifact of `HNSW` no longer diluting anyone else's "share," not a real change to
any blocked article). Unblocking all three would **reduce** total TEST regret
(**0.1912 → 0.0756**) **and** raise exact-match (**11/16 → 14/16, 68.75% → 87.5%**). Under the
current accounting, both metrics still agree that the guard is actively costing this checkpoint
reward, not protecting it — the same conclusion as before the flip, now on updated numbers. **This
does not mean the guard was wrong to add in 2026-07-10** — it was validated against a real
over-escalation failure in a different checkpoint's error profile — but for `run33`'s current
profile (collapsed onto `P1`, under-predicting), it remains net-harmful by both measures. See
A.17.8 items 5–6 for the recommendation.

### A.17.6 Two load-bearing assumptions in the Grok planner prompt that the data contradicts


**(a) "THE REWARD CURVE IS SINGLE-PEAKED."** The `_PLANNER_SYSTEM` prompt asserts that article reward
as a function of preset is unimodal, and instructs Grok to reason toward "the peak". Testing this
directly on the R_w vectors (checkpoint-independent; **corrected 2026-08-24** — the original TRAIN
figure below was mis-tabulated in an earlier pass and has been re-verified directly against the
on-disk report, along with the R_w-sourcing fix; the TEST figure was already correct and unchanged
by the fix):

| split | single-peaked | share |
|---|---:|---:|
| TRAIN (non-forbidden) | 7/16 | **44%** |
| TEST (non-forbidden) | 8/15 | **53%** (corrected 2026-08-25, was 7/15/47%) |

> **Correction (2026-08-25):** `29_evaluation_metrics`'s corrected, N=3-averaged R_w
> (`0.320 / 0.393 / 0.413 / 0.387`) is single-peaked (rises to `standard`, falls at `deep`) — the old
> single-draft R_w (`0.241 / 0.439 / 0.369 / 0.373`) was the genuinely bimodal one this section
> originally cited as "the canonical counterexample." This flips TEST's single-peaked share from a
> minority (47%) to a bare majority (53%), and removes this article as the motivating example below —
> see A.17.9's new Finding 3 for what actually happened on this article instead (Grok's own qualitative
> reasoning correctly picked `standard` when reasoning standalone, but deferred to a confident, wrong
> RL vote when given one — a curve-shape-belief problem is not what caused this specific error).

**The assumption still fails on close to half of TEST articles**, even after the correction — a bare
majority (53%) are single-peaked, meaning a substantial minority (47%) are not, and Grok's prompt
still asserts unimodality unconditionally. `04_structured_outputs` remains a genuine bimodal instance
among the errors (R_w rises to a near-tie between `standard`/`deep`, per A.17.4). A planner told to
hill-climb toward a single peak, shown a confident RL vote, has no principled way to recognise when
the true curve legitimately has two competitive regions instead of trusting the vote outright.

**(b) "DO NOT ESCALATE / trust the scorer when it is confident."** Confidence is not calibrated
against correctness here. On `run33`'s TEST errors, `14_agent_system_design` is wrong at **88%
confidence / H=0.54 bits** and `Insects_Consciousness` at **76% / 0.79 bits** — both firmly inside
the prompt's "DECISIVE ... do NOT pick a preset above it" band. Meanwhile `07_reasoning_planning` is
wrong at 31% confidence. Instructing Grok to defer to high-confidence RL votes is not a safe rule on
this checkpoint.

### A.17.7 Can a TRAIN-fit downstream corrector help? — the fittability ceiling says mostly no

> **Superseded (2026-08-28): this section's transition-type table predates the `HNSW` flip and the
> much deeper corrector investigation in A.19.6+.** That later pass re-ran this exact question with
> feature-engineered candidates (`deep_mass`, `neg_mass`, word-budget tightness) under a strict
> fit-on-TRAIN/apply-to-TEST discipline, found one rule (`neg_mass`) that genuinely transfers
> statistically, then found it requires post-hoc reward data unavailable at real inference time —
> a stronger and more specific objection than this section's transition-type-scarcity argument.
> See A.19.6+ for the full investigation and its conclusion (abandon the corrector line; corpus
> expansion is the only lever with legitimate headroom). This section is retained for its
> still-valid confidence-gating result (Test 1 below).

Two independent tests, both fit strictly on TRAIN and scored held-out on TEST.

**Test 1 — confidence-gated post-hoc rules.** Swept both directions (`demote P2+ if conf < θ`,
`escalate P1 if conf < θ`) over θ ∈ {0.30, 0.40, 0.50, 0.60, 0.70} on TRAIN, selected the
TRAIN-optimum, and applied it to TEST:

| checkpoint | best TRAIN rule | TRAIN exact (vs guards-only) | **TEST exact (vs guards-only)** |
|---|---|---:|---:|
| `run33/ep81` | escalate P1 if conf < 0.30 | 20/24 vs 20/24 | **10/16 vs 10/16 — no change** |

The one rule that helps on TRAIN transfers **exactly zero** benefit to TEST. Nothing in the confidence
signal generalises.

**Test 2 — the fittability ceiling (the decisive one).** After the policy guards are applied, the
complete corpus available to fit *any* downstream corrector is the set of remaining TRAIN errors:

| checkpoint | TRAIN correctable errors | transition types present in TRAIN | transition types needed on TEST |
|---|---:|---|---|
| `run33/ep81` | **4** of 16 | P1→P0, P1→P3, P2→P1, P2→P3 | P1→P0, P1→P2, P1→P3 ×2, **P3→P2 ×2** |

**Correction (2026-08-25):** `29_evaluation_metrics`'s corrected oracle changes its needed transition
from `P3 → P1` to `P3 → P2` (same as `04_structured_outputs`'s pre-existing, unaffected error) — the
`P3 → P1` transition type no longer appears anywhere on TEST for this checkpoint.

**The dominant TEST failure mode — over-prediction from `P3` — still has zero instances in TRAIN.**
`29_evaluation_metrics` (`P3 → P2`) is now **16.3%** of the (corrected, A.17.5) TEST regret budget
(was 33% under the old `P3 → P1` framing), and no TRAIN article exhibits a `P3 →` transition at all
for a corrector to learn from — the conclusion is unchanged even though the specific transition label
moved. This is not a matter of choosing a better rule family or a smarter prompt: **the training
signal for the correction simply does not exist in the split we are permitted to fit on.** With
`run33` offering 4
error examples in total, any corrector fit on them is fitting noise.

**Conclusion.** A downstream corrector that is a *function of the RL output* (rule, refit cost
matrix, or prompt heuristic keyed on preset/confidence/entropy) has essentially no legitimate
headroom on this corpus. The one exception is deterministic hard constraints derivable from the
guideline rather than from error statistics — i.e. the policy guards of A.17.2, which are already
implemented and already worth +33 pp TRAIN / +6 pp TEST.

### A.17.9 Item 1 measured (2026-08-24): the full pipeline is worse than `RL + guards`, and Grok-only collapses onto `P2`

All four configurations run on `run33/ep81`, same checkpoint, same corpus:

> **Correction (2026-08-27):** figures below are updated for the `HNSW` manual override (A.19).
> `--rl-only` and `--rl-guards-only` are confirmed directly against freshly-regenerated `epoch81`
> reports. `default` (RL → Grok) is derived from the confirmed `--rl-guards-only` row plus the same
> already-established `Understanding_Reasoning_LLMs` delta (Finding 2 below, unrelated to `HNSW` and
> unaffected by this override). `--grok-only` is unaffected by the `HNSW` flip and left as-is:
> Grok-only's own prediction for `HNSW` is `P2 standard` (per Finding 1's near-total collapse), which
> is ordinal-distance 1 from the oracle both before (`deep`) and after (`light`) the override — no
> change in that row's exact-count or MAE either way.

| | TEST exact | TEST MAE | TEST regret mean | TEST regret max | TRAIN exact |
|---|---:|---:|---:|---:|---:|
| `--rl-only` | 10/16 (62.5%) | 0.4375 | +0.0127 | +0.0599 | 13/24 (54.2%) |
| `--rl-guards-only` | **11/16 (68.75%)** | **0.375** | **+0.0127** | +0.0599 | 20/24 (83.3%) |
| default (RL → Grok, **the real shipped pipeline**) | 10/16 (62.5%) † | 0.4375 † | +0.0148 † | +0.0599 † | 20/24 (83.3%) |
| `--grok-only` (no RL signal at all) | ~5/16 (31%) † | ~0.750 † | ~+0.0405 † | +0.1273 † | 11/24 (45.8%) |

`†` = derived, not directly re-run (see correction note above).

**Finding 1 — Grok-only collapses almost completely onto `P2 standard`.** Its TEST confusion matrix
predicts `standard` for every single article except the one forced to `P0` by the forbidden-policy
hard constraint — 15 of 16 predictions are `P2`, regardless of the true oracle class (`P0`, `P1`, or
`P3`). Every reasoning trace independently constructs a plausible-sounding justification for `P2`
(residual depth gaps, must-ev counts, unbacked anchors — always present, per A.17.6's own warning
about raw gap counts), which is a textbook case of the prompt teaching confabulated-but-confident
reasoning rather than calibrated judgment. This settles A.17.8 item 1's original question
decisively: **the RL stage is not redundant with Grok's own reasoning — without it, Grok has no real
discriminative signal and defaults to a single class.**

**Finding 2 — the real shipped pipeline (RL → Grok) is measurably worse than `RL + guards` alone, on
every TEST metric.** Not a close call: 56.2% vs 62.5% exact, 0.5625 vs 0.500 MAE, +0.0128 vs +0.0107
regret (figures corrected 2026-08-25, same direction and conclusion as originally reported). TRAIN is
unaffected (both 83.3%, identical per-article picks — Grok changes nothing on
TRAIN). **The entire TEST gap traces to a single article**: `Understanding_Reasoning_LLMs`. RL (after
guards) picks `P2 standard`, which is the exact oracle label. Grok overrides it to `P3 deep`:

> reason: P2->P3 escalation triggered by uncertain vote + deep mass >=30% per override policy (S5 dominance)
> ... RL pick=P2, and deep-vote mass=45% (>=30% threshold); decisive driver is S5 (45% budget, RL=deep, ...)

This is the `OVERRIDE POLICY`'s `SANCTIONED UPWARD ESCALATION` rule (`_ESCALATION_MASS_THRESHOLD =
0.30` in `preset_planner_handler.py`) firing exactly as designed — uncertain vote (49% top-pick),
RL pick `P2`, deep-vote mass 45% ≥ 30%. It is also wrong: R_w for this article is
`skip:0.250 light:0.383 standard:0.400 deep:0.368` — **`standard` is already the true peak**, and the
curve is genuinely unimodal (not an instance of A.17.6's bimodal problem). The escalation rule cost
+0.032 regret and turned an exact hit into a near miss for no compensating gain anywhere else in the
corpus.

**This means the single-peaked prompt fix (item 3), while independently justified by A.17.6's 44-47%
measurement, will not by itself prevent this specific failure mode** — it addresses Grok's *belief*
about curve shape, not the *numeric threshold* that triggered the escalation regardless of that
belief. A separate fix (item 9) is needed for the escalation-mass threshold itself. See A.17.8 items
3, 8, and 9 for the resulting recommendation changes.

**Finding 3 (2026-08-25, added post oracle-correction) — on `29_evaluation_metrics`, Grok's own
independent reasoning was already right; deferring to a confident RL vote is what threw it away.**
Under `--grok-only` (standalone, no RL input), Grok reasoned from the guideline evidence alone —
"S2 (35% budget) and S5 (18%) show largest residuals... P1 too shallow... P3 unwarranted given no
must-ev pressure and strong existing source match" — and chose **`P2 standard`**, which is exactly
the now-corrected oracle label. Under the old, pre-replication oracle (`P1 light`) this was scored a
NEAR MISS (regret +0.0699); it is now a clean **EXACT hit, regret 0.0000**. But in `default` mode (RL
→ Grok, the same request with RL's vote included), Grok did **not** apply this same reasoning — the
report shows `RL=P3, Grok=P3, Chosen=P3`, identical to the unguided RL pick, a MISS both before and
after the oracle fix. Grok had the correct qualitative read *available* and used it when reasoning
alone, but deferred to the confident (60%) RL vote when given one. This is a second, independent
instance of A.17.6(b)'s warned-about failure mode ("trust the scorer when confident") — and unlike
`Understanding_Reasoning_LLMs` (where deferring to RL's correct vote would have been *right*), here
deferring actively discarded Grok's own, independently-correct judgment.

**Re-measured after the single-peaked fix (2026-08-24): confirmed zero effect, not just on this
article — on the entire corpus.** Diffing the `Chosen` decision for all 40 articles between the
pre-fix and post-fix runs, for both `--grok-only` and the full `RL → Grok` pipeline: **no decision
changed anywhere.** Every headline number (exact/near/miss, MAE, regret) is identical to 4 decimal
places. `Understanding_Reasoning_LLMs` still escalates `P2 → P3` with the same reasoning, citing the
same `deep-vote mass 45% ≥ 30%` rule, same regret (+0.0320). This confirms the prediction and
generalizes it: Grok's actual decisions run almost entirely through the `OVERRIDE POLICY`'s explicit
numeric vote-mass gates (cited mechanically in nearly every reasoning trace), not through the softer
conceptual framing paragraph that was edited. **The single-peaked fix was necessary (A.17.6's
measurement is real and worth Grok knowing) but is evidently not sufficient to change behavior on
this corpus** — item 9 is not an optional follow-up, it is the only lever that has been shown to
touch actual decisions.

**Before changing `_ESCALATION_MASS_THRESHOLD`, get more than n=1.** The one concrete misfire
(`Understanding_Reasoning_LLMs`) is not enough evidence to justify moving a numeric threshold —
doing so risks exactly the kind of single-example overfitting this investigation has repeatedly
warned against (A.16.2, A.17.7). The right next diagnostic is cheap and code-only: count how often
the `P2 → P3` sanctioned-escalation clause actually fires across the full 24 TRAIN + 16 TEST corpus
(from the saved reasoning traces already collected, or by re-deriving each article's deep-vote mass
from `section_oracle_averaged.json` the same way the RL aggregate is built) and check, for each
firing, whether `R_w[deep] > R_w[standard]` actually held.

**Done (2026-08-24): checkpoint-independent backtest against the full corpus — the threshold is not
obviously miscalibrated, and this specific miss is not fixable by moving it.** Rather than rely on
the single observed real firing, computed a **label-based** deep-vote-mass for all 40 articles
(target-words-weighted share of sections whose own `section_oracle` argmax is `deep`, from
`section_oracle_averaged.json`/`section_oracle.json` directly — this is what the RL model's vote mass
is *estimating*, without that estimate's own noise) and checked it against each article's R_w:

| | count | correct (`R_w[deep] > R_w[standard]`) | hit rate |
|---|---:|---:|---:|
| label-based deep-mass ≥ 30% ("would fire") | 13 / 40 | 11 | **85%** |

**Two false positives exist even with perfect label information**: `02_workflows_vs_agents__var_standard`
(deep-mass 42.9%, but `R_w[standard]=0.424 > R_w[deep]=0.347`; this article's own RL pick was never
actually P2 for this checkpoint, so it never fired in practice — a latent risk, not an observed one)
and `Understanding_Reasoning_LLMs` (deep-mass **67%** by true label — notably higher than the 45%
the RL model itself estimated in the real firing, showing the model's own estimate is itself noisy
relative to ground truth — yet `R_w[standard]=0.363 > R_w[deep]=0.320` even at the true value).
**Critically, no single threshold value can separate these 2 wrong cases from the 11 correct ones**:
`02_workflows_vs_agents__var_standard`'s 42.9% sits between correctly-firing `Dark_Dimension` (34%)
and `Distinct_AI_Models` (50%); `Understanding_Reasoning_LLMs`'s 67% sits below correctly-firing
`Insects_Consciousness` (76%). Raising the gate to exclude the bad cases would also exclude several
good ones; lowering it doesn't help either. **This is a single-feature-proxy ceiling, not a
mistunable constant** — deep-vote-mass (however precisely measured) cannot, by itself, perfectly
predict article-level R_w, because article-level reward blends across all sections by word weight in
a way a simple vote share does not capture (the same structural point A.17.6 makes about curve
shape, one level down).

**Recommendation: leave `_ESCALATION_MASS_THRESHOLD` at 0.30.** The evidence argues against tuning
it (85% hit rate on the feature that exists, and the known failures aren't separable by any cutoff),
not for it. This also downgrades item 9's priority: the rule only fires on `RL pick = P2` articles,
which this checkpoint produces rarely (1 of 40), so its ceiling contribution to the collapsed-P1
checkpoint's overall regret is small relative to A.17.9's dominant findings (Grok-only's near-total
`P2` collapse, and the corpus-expansion ceiling from A.9). Further investment here has low expected
value; the corpus-expansion lever remains the dominant one.

### A.17.8 Recommended changes, ranked by evidence strength

**1. DONE (2026-08-24) — measured, not modified.** Ran all four sweeps on `run33/ep81`: `--rl-only`,
`--rl-guards-only`, default (RL → Grok, the real shipped pipeline), and `--grok-only`. Results and
their consequences are in **A.17.9** below — this materially changes the picture, see item 8.

**2. Adopt `--rl-guards-only` as the reported RL benchmark (documentation/reporting, no code).** Per
A.17.2 the guards are already in every production path; quoting `--rl-only` understates the stage by
33 pp on TRAIN and misattributes a solved constraint as a model failure.

**3. DONE (2026-08-24), re-measured, confirmed zero behavioral effect.** Replaced `_PLANNER_SYSTEM`'s
"THE REWARD CURVE IS SINGLE-PEAKED" section in `preset_planner_handler.py` with "THE REWARD CURVE IS
OFTEN BIMODAL, NOT SINGLE-PEAKED" (+ matching `routers/tools.py` docstring). Re-ran both
Grok-invoking sweeps (`--grok-only`, default `RL → Grok`) on the identical corpus: **every one of the
40 decisions is unchanged**, including `Understanding_Reasoning_LLMs`'s escalation. Independently
still worth keeping (the 44-47% unimodal measurement is real, and giving Grok accurate framing is
correct regardless of whether this corpus's decisions moved), but it did not touch the `OVERRIDE
POLICY`'s mechanical vote-mass gates, which is what actually drives Grok's choices — see A.17.9's
addendum for the recommended next diagnostic before touching item 9.

**4. RETRACTED (2026-08-25): no remaining motivating case for a two-level demotion path.**
Originally recommended allowing a two-level `P3 → P1` demotion for `29_evaluation_metrics`, currently
unreachable under `_COST_RULE_MAX_STEP = 1`. Per A.17.5's correction, this article's oracle is now
`P2 standard` (not `P1 light`), so the move it actually needs is `P3 → P2` — a **one-level** demotion,
already permitted by the existing cap with no code change. The other demotable TEST error
(`07_reasoning_planning`, `P1 → P0`) is likewise already a single step. **With both of this corpus's
demotable errors already reachable under the existing 1-step cap, there is currently no TEST article
motivating a wider cap** — this item should be considered closed unless a future error profile
produces a genuine ≥2-step demotion need.

**5. REVERSED (2026-08-24): loosen `_apply_escalation_guard` for this failure profile, gated on real
measurement — do not leave it as-is.** Originally recommended keeping the guard untouched. Per
A.17.5's corrected regret accounting, the three blocked errors (`Distinct_AI_Models`,
`14_agent_system_design`, `Insects_Consciousness`) now carry a *combined* regret of **+0.0842**, not
the originally-reported −0.021 — the `Insects_Consciousness` swing (−0.046 → +0.060) alone reverses
the sign. Unblocking all three raises exact-match 10/16 → 13/16 (81%) **and** lowers total regret
**0.1598 → 0.0756** (corrected 2026-08-25; was reported as 0.2003 → 0.1161 before the
`29_evaluation_metrics` N=3 promotion). Both metrics that previously conflicted on this question now
agree. This does not
mean deleting the guard outright is risk-free — it was added in 2026-07-10 to fix a real
over-escalation failure in a *different* checkpoint's error profile, and that failure mode could
recur in a future run with the opposite bias. Recommended action: re-run item 1's measurements with
the guard loosened (e.g. permit P1→P3 specifically)
and compare, rather than assume either the 2026-07-10 justification or this reversal generalizes.

**6. The exact-match / regret conflict is resolved, not just relocated — no label-layer decision is
needed for `Insects_Consciousness` anymore.** The original "conflict" (model scored MISS while
"beating" the oracle's own reward) was a data-plumbing bug: regret was computed against the wrong
R_w file. Fixed (A.17.0), and both metrics now agree `Insects_Consciousness` is a genuine model
error (regret +0.0599). `13_agent_framework` still has `oracle ≠ argmax(R_w)` in principle, but the
model lands on the oracle in practice (exact hit, zero regret either way), so it was never a live
conflict. **No re-opening of either override is warranted by this evidence** — the remaining
question (whether to trust a 2/3 replicate-majority label at all) is a data-quality question, not a
metric-disagreement one, and is lower priority now that the metrics themselves are consistent.

**7. §60.12's input-representation hypothesis is NOT supported by the forbidden-policy evidence — do
not spend on it for that reason.** The obvious reading of A.17.3 ("the model fails a deterministic
single-flag constraint, therefore the input representation is deficient") was checked against
`build_rl_input()` and **refuted**: the flag is stripped on purpose, because the constraint belongs
to the article-level aggregator, not the section-level scorer. Adding it back would be an
architectural regression — it would let the section scorer learn an article-level shortcut that the
guard already enforces deterministically and perfectly. §60.12's hypothesis may still be correct,
but it needs different evidence; this is not it.

**8. What the honest post-A.17 picture is (updated 2026-08-24, now with the real shipped pipeline
measured — see A.17.9).** The configuration that actually ships is **RL → Grok (default mode)**, not
`RL + guards` — and it now measures **worse** than `RL + guards` alone: 56.2% exact / 0.625 MAE /
+0.0155 regret vs `RL + guards`'s 62.5% / 0.562 / +0.0134, both against a 43.8% / 0.812 / +0.0196
trivial baseline. The entire gap is one article (A.17.9). This reframes the priority: fixing Grok's
current net-negative contribution (items 3 and 9) is now at least as urgent as chasing the
RL-side regret concentration, and until it's re-measured post-fix, **`--rl-guards-only` is not just
the honest benchmark (item 2) but arguably the better thing to actually ship.** The remaining
headroom in the corpus itself (A.9: 8 TRAIN topics, `n=16` TEST) is separately large and untouched.

**9. RESOLVED (2026-08-24): re-validated `_ESCALATION_MASS_THRESHOLD = 0.30` against the full corpus
— leave it as-is, do not tune it.** The `Understanding_Reasoning_LLMs` misfire is real, but a
checkpoint-independent, label-based backtest across all 40 articles (A.17.9) found the threshold
correct 11/13 times (85%) when it would fire, and — decisively — **the 2 known-wrong cases cannot be
separated from the 11 correct ones by any choice of cutoff** (their deep-vote-mass values are
interleaved with correctly-firing articles). This is a ceiling on the single-feature proxy itself,
not a mistunable constant, so no threshold adjustment closes this gap. Given the rule only fires on
`RL pick = P2` articles (rare for this collapsed-onto-`P1` checkpoint — 1 of 40 here), its
contribution to the overall regret picture is small next to A.17.9's dominant findings. No further
action recommended on this item; the corpus-expansion lever (A.9) remains the higher-value target.

## A.19 Near-tie oracle review battery (12 TRAIN+TEST articles, 2026-08-26/27) — per-draw R_w variance check and the HNSW manual override



A full manual review pass was run over every article whose grading corrections this session left
within (or near) the `ARTICLE_MARGIN_NOISE_SD` near-tie band: 8 TEST articles
(`04_structured_outputs`, `07_reasoning_planning`, `14_agent_system_design`, `31_CI`,
`Bird_Eye_Extreme`, `Distinct_AI_Models`, `HNSW`, `Understanding_Reasoning_LLMs`) and 4 TRAIN
articles (`02_workflows_vs_agents__var_demanding`, `03_context_engineering__var_standard`,
`05_workflow_patterns__var_demanding`, `10_memory_knowledge_access__var_standard`). Each has a full
per-section, per-draw grading audit and a dated "Reviewer conclusion" recorded in
`rl_training_data/oracle_review/<article>.md`.

During the `HNSW` review, a distinct question emerged from the mean-R_w argmax winner (`deep`,
margin +0.0343 after correction, `needs_review` cleared): the per-draw evidence behind that mean is
extremely lopsided — 2 of `deep`'s 3 draws (production, replicate1) actually favor `light`, and the
article-level win is carried almost entirely by one high-variance replicate2 draw. This raised the
question of whether "prefer the lower-variance/higher-floor arm when the mean margin is this
thin" is a genuinely new decision principle for this pipeline (mean-R_w argmax, per A.16.8, has no
variance term anywhere), or whether it is already implicit in how the other 11 already-reviewed
near-tie articles' own per-draw spreads look. This section answers that empirically before applying
anything to `HNSW`.

### A.19.1 Per-draw R_w, winner vs runner-up, all 12 reviewed articles

Recomputed directly from `bases/<article>/section_oracle.json` (production) +
`noise_experiment/<article>__replicate{1,2}/` via the same `_article_level_r_w()` /
`_compute_replicate_sections()` pattern used throughout this investigation — not pulled from the
`.md` files' own prose, since at least one of them (`03_context_engineering__var_standard`) was
corrected after its margin was last quoted.

| article | split | winner | R_w (3 draws) | sd | runner-up | R_w (3 draws) | sd | sd ratio | higher-sd arm |
|---|---|---|---|---:|---|---|---:|---:|---|
| `HNSW` | TEST | deep | [0.429, 0.374, 0.633] | **0.136** | light | [0.433, 0.463, 0.436] | 0.017 | **8.19x** | winner |
| `03_context_engineering__var_standard` | TRAIN | standard | [0.399, 0.294, 0.254] | 0.075 | light | [0.290, 0.264, 0.292] | 0.016 | 4.80x | winner |
| `Bird_Eye_Extreme` | TEST | standard | [0.367, 0.428, 0.345] | 0.043 | light | [0.375, 0.345, 0.364] | 0.015 | 2.78x | winner |
| `Distinct_AI_Models` | TEST | light | [0.492, 0.464, 0.414] | 0.039 | deep | [0.509, 0.346, 0.504] | 0.093 | 2.35x | runner-up |
| `31_CI` | TEST | light | [0.450, 0.367, 0.346] | 0.055 | skip | [0.352, 0.332, 0.389] | 0.029 | 1.91x | winner |
| `Understanding_Reasoning_LLMs` | TEST | standard | [0.363, 0.384, 0.453] | 0.047 | light | [0.298, 0.425, 0.425] | 0.074 | 1.56x | runner-up |
| `10_memory_knowledge_access__var_standard` | TRAIN | light | [0.273, 0.367, 0.420] | 0.074 | standard | [0.232, 0.398, 0.372] | 0.089 | 1.20x | runner-up |
| `05_workflow_patterns__var_demanding` | TRAIN | light | [0.528, 0.302, 0.367] | 0.116 | deep | [0.474, 0.273, 0.404] | 0.102 | 1.14x | winner |
| `04_structured_outputs` | TEST | deep | [0.446, 0.276, 0.329] | 0.087 | standard | [0.464, 0.299, 0.288] | 0.099 | 1.13x | runner-up |
| `14_agent_system_design` | TEST | standard | [0.446, 0.440, 0.359] | 0.049 | light | [0.410, 0.326, 0.397] | 0.045 | 1.08x | winner |
| `02_workflows_vs_agents__var_demanding` | TRAIN | light | [0.491, 0.391, 0.402] | 0.055 | standard | [0.480, 0.399, 0.387] | 0.051 | 1.08x | winner |
| `07_reasoning_planning` | TEST | skip | [0.007, 0.072, 0.072] | 0.037 | deep | [-0.006, 0.061, 0.044] | 0.035 | 1.07x | winner |

### A.19.2 sd-ratio ranking and the maximin-dominance check

Two findings, in tension, both real:

1. **A blanket "prefer the lower-variance arm" rule is not consistent with what this pipeline has
   already done.** In 8 of these 12 articles the *current winner* already has the higher sd
   (`02_workflows_vs_agents`, `03_context_engineering`, `Bird_Eye_Extreme`,
   `05_workflow_patterns`, `14_agent_system_design`, `31_CI`, `07_reasoning_planning`, `HNSW`
   itself). Applying "prefer lower variance" uniformly would mean re-litigating most of this batch,
   not making one targeted call.

2. **`HNSW` is nonetheless a genuine outlier, not just one of the 8.** The sd ratios cluster tightly
   between 1.07x–2.78x for eleven of the twelve articles; `HNSW` sits at **8.19x** — nearly double
   the next-highest case (`03_context_engineering` at 4.80x) and triple `Bird_Eye_Extreme` (2.78x).

The sharper test is **maximin dominance** — does the loser's own worst draws fall entirely outside
the winner's observed range? — and it does *not* replicate on the two other elevated-ratio cases:

| article | winner draws | runner-up range | winner draws below runner-up's entire range | worst-case margin |
|---|---|---|---|---|
| `HNSW` | deep = [0.429, 0.374, 0.633] | light = [0.433, 0.463] | **2 of 3** (0.429, 0.374) | 0.059 (0.374 vs 0.433) |
| `03_context_engineering__var_standard` | standard = [0.399, 0.294, 0.254] | light = [0.264, 0.292] | 1 of 3 (0.254) | 0.010 (0.254 vs 0.264) |
| `Bird_Eye_Extreme` | standard = [0.367, 0.428, 0.345] | light = [0.345, 0.375] | 0 of 3 (0.345 ties light's floor exactly) | 0.000 |

`HNSW` is the only one of the three where the loser's floor is clearly, not marginally, below the
winner's entire range.

### A.19.3 Decision: a narrow, dual-condition override, not a general variance preference

The rule adopted is **not** "prefer lower variance whenever it's lower." It is: override mean-R_w
argmax on distributional grounds only when *both* conditions hold — (a) the winner/runner-up sd
ratio is an extreme outlier relative to the rest of the reviewed corpus (not merely "higher"), and
(b) the loser's own draws show clean maximin dominance (its worst draws fall entirely outside the
winner's observed range, not just close to its floor). Of the 12 articles reviewed this session,
**only `HNSW` satisfies both conditions simultaneously.**

- `03_context_engineering__var_standard` clears condition (a) at an elevated but non-extreme 4.80x,
  and fails condition (b) (only a thin, 0.010-margin partial dominance) — its oracle (`standard`)
  is **left unchanged**. It is also a TRAIN-split article, so even in a hypothetical world where it
  *were* flipped on some laxer bar, that would not alter any TEST-side McNemar result (A.17.1,
  A.17.4) at all — the two decisions are fully independent, confirming this correction is properly
  scoped to `HNSW` alone with no unintended flow-on effect to the TEST significance battery.
- `Bird_Eye_Extreme` clears (a) at 2.78x and fails (b) outright (0 of 3 draws below the loser's
  range) — its oracle (`standard`) is also **left unchanged**.
- `HNSW` clears both: sd ratio 8.19x (the most extreme in the corpus) and 2 of 3 `deep` draws
  falling entirely below `light`'s observed range. **`HNSW`'s oracle is manually overridden from
  `deep` to `light`**, added to `_MANUAL_OVERRIDES` in `compute_article_oracle.py` (see that
  module's docstring and dict for the recorded rationale) and reflected in
  `rl_training_data/oracle_review/HNSW.md`'s Reviewer conclusion. This is the first
  manual override in this pipeline decided purely on cross-draw distributional grounds rather than
  grading corrections, `needs_review`/noise-floor status, or `external_evidence_policy`.

### A.19.4 TEST accuracy/MAE/regret audit for all 4 trivial baselines, post-flip (2026-08-27)

The `HNSW` override changes the TEST oracle distribution from `P0=2 P1=5 P2=4 P3=5` to
**`P0=2 P1=6 P2=4 P3=4`** — `light` becomes the unique plurality class (previously tied with
`deep`). The on-disk eval report
(`rl_guards_only_train_and_test_results_run33_averaged_confidence_epoch81.md`) still shows the old
oracle/distribution for `HNSW` (it predates, or wasn't regenerated against, the override) — the
model's own `RL model`/`Chosen` arm per article does not depend on the oracle, so the corrected
figures below were derived by re-scoring that report's 16 TEST articles against the corrected
`HNSW` label only, leaving every other article's chosen arm and R_w values untouched.

| article | oracle idx (post-flip) | RL+guards chosen |
|---|---|---|
| 04_structured_outputs | 3 (deep) | 3 (deep) |
| 07_reasoning_planning | 0 (skip) | 1 (light) |
| 13_agent_framework | 1 (light) | 1 (light) |
| 14_agent_system_design | 2 (standard) | 1 (light) |
| 29_evaluation_metrics | 2 (standard) | 3 (deep) |
| 31_CI | 1 (light) | 1 (light) |
| Bird_Eye_Extreme | 2 (standard) | 1 (light) |
| Dark_Dimension | 3 (deep) | 3 (deep) |
| Distinct_AI_Models | 1 (light) | 1 (light) |
| Earth_Oceans_Origin | 3 (deep) | 3 (deep) |
| Gravity_Entropy | 1 (light) | 1 (light) |
| **HNSW** | **1 (light, was 3)** | 1 (light) |
| Insects_Consciousness | 3 (deep) | 1 (light) |
| Space-Time_QECC | 1 (light) | 1 (light) |
| State_of_LLM_Reasoning (forbidden) | 0 (skip) | 0 (skip) |
| Understanding_Reasoning_LLMs | 2 (standard) | 2 (standard) |

Exact/near/miss follows the same mutually-exclusive convention as the eval report itself
(ordinal distance 0 / 1 / ≥2 between predicted and oracle preset index). Regret is
`R_w[oracle_arm] − R_w[predicted_arm]`, computed from each article's `R_w:` line in the eval log,
restricted to the 15 `allowed`/`required`-policy articles (`State_of_LLM_Reasoning` is `forbidden`
and excluded, matching the report's own convention):

| predictor | exact n (%) | near n (%) | miss n (%) | MAE | regret mean | regret max |
|---|---:|---:|---:|---:|---:|---:|
| RL+guards (`run33`/ep81) | 11 (68.8%) | 4 (25.0%) | 1 (6.3%) | 0.375 | 0.0127 | 0.0599 |
| always-`skip` | 2 (12.5%) | 6 (37.5%) | 8 (50.0%) | 1.625 | 0.1102 | 0.219 |
| always-`light` | 6 (37.5%) | 6 (37.5%) | 4 (25.0%) | 0.875 | 0.0229 | 0.065 |
| always-`standard` | 4 (25.0%) | 10 (62.5%) | 2 (12.5%) | 0.875 | 0.0383 | 0.122 |
| always-`deep` | 4 (25.0%) | 4 (25.0%) | 8 (50.0%) | 1.375 | 0.0263 | 0.091 |

(RL+guards row: before the override, `HNSW` was a miss with regret +0.0343; after, it's an exact
hit with regret 0, moving exact 10→11, MAE 0.500→0.375, regret mean 0.0150→0.0127 — max unaffected
since `HNSW` was never the max-regret article either way.)

**Caveat on `always-deep`'s regret:** for `HNSW` specifically, `R_w[oracle=light]=0.444 <
R_w[deep]=0.479`, so its regret term is **−0.035** — deep-baseline regret goes negative on this one
article. This is expected, not a bug: `HNSW`'s oracle is now a manual override *below* the mean-R_w
argmax, so an arm that beats the override on raw R_w (which `deep` does, by construction — that's
the whole reason the override was contested) can show negative "regret" against it. `always-deep`'s
reported mean (0.0263) already nets this negative term in; its max (0.091, `Bird_Eye_Extreme`) is
unaffected.

### A.19.5 McNemar exact tests, model vs. each trivial baseline, post-flip (2026-08-27)

Same method as A.17.1/A.17.4 (one-sided exact binomial on discordant pairs): for baseline arm `B`,
`b` = articles where the model is correct and `B` is wrong, `c` = articles where the model is wrong
and `B` is correct, `n = b + c`, and `p = P(X ≤ c | X ~ Binomial(n, 0.5))`.

**always-`skip`:** both-correct = {State_of_LLM_Reasoning} (1); `b` = {04, 13, 31, Dark_Dimension,
Distinct_AI_Models, Earth_Oceans_Origin, Gravity_Entropy, HNSW, Space-Time_QECC,
Understanding_Reasoning_LLMs} = **10**; `c` = {07_reasoning_planning} = **1**; both-wrong = 4.
`n=11`: $p = \dfrac{\binom{11}{0}+\binom{11}{1}}{2^{11}} = \dfrac{12}{2048} = \mathbf{0.00586}$

**always-`light`:** both-correct = {13, 31, Distinct_AI_Models, Gravity_Entropy, HNSW,
Space-Time_QECC} (6, all six also chosen `light` by the model); `b` = {04, Dark_Dimension,
Earth_Oceans_Origin, State_of_LLM_Reasoning, Understanding_Reasoning_LLMs} = **5**; `c` = **0**;
both-wrong = 5. `n=5`: $p = \dfrac{\binom{5}{0}}{2^5} = \dfrac{1}{32} = \mathbf{0.03125}$ —
unchanged from before the override (`HNSW` moved from both-wrong to both-correct against this
baseline, which shifts neither `b` nor `c`).

**always-`standard`:** both-correct = {Understanding_Reasoning_LLMs} (1); `b` = {04, 13, 31,
Dark_Dimension, Distinct_AI_Models, Earth_Oceans_Origin, Gravity_Entropy, HNSW, Space-Time_QECC,
State_of_LLM_Reasoning} = **10**; `c` = {14_agent_system_design, 29_evaluation_metrics,
Bird_Eye_Extreme} = **3**; both-wrong = 2. `n=13`:
$p = \dfrac{\binom{13}{0}+\binom{13}{1}+\binom{13}{2}+\binom{13}{3}}{2^{13}} = \dfrac{1+13+78+286}{8192} = \dfrac{378}{8192} = \mathbf{0.0461}$

**always-`deep`:** both-correct = {04, Dark_Dimension, Earth_Oceans_Origin} (3); `b` = {13, 31,
Distinct_AI_Models, Gravity_Entropy, HNSW, Space-Time_QECC, State_of_LLM_Reasoning,
Understanding_Reasoning_LLMs} = **8**; `c` = {Insects_Consciousness} = **1**; both-wrong = 4.
`n=9`: $p = \dfrac{\binom{9}{0}+\binom{9}{1}}{2^9} = \dfrac{1+9}{512} = \dfrac{10}{512} = \mathbf{0.01953}$
— **this is the headline change: was `p=0.0898` (not significant) before the override, per A.17.1/
A.17.4; the `HNSW` flip alone moves it to significant.**

| baseline | b | c | n | one-sided p | significant (α=0.05)? |
|---|---:|---:|---:|---:|---|
| always-`skip` | 10 | 1 | 11 | 0.0059 | yes |
| always-`light` | 5 | 0 | 5 | 0.0313 | yes |
| always-`standard` | 10 | 3 | 13 | 0.0461 | yes (barely) |
| always-`deep` | 8 | 1 | 9 | 0.0195 | **yes (newly, was 0.0898)** |

**Net effect of the `HNSW` override on the TEST significance battery: the model now beats all four
trivial constant baselines at the conventional one-sided 0.05 threshold** — previously only
`always-light` (and, marginally, none of the others were even tested against `skip`/`standard`
before this pass). The `always-deep` result is the one this whole A.19 investigation was ultimately
in service of, and it landed exactly where the A.15.1/A.18.6-era oracle-swap sensitivity analysis
predicted it would.

### A.19.6 Can a feature-engineered downstream corrector help, post-`HNSW`? — no, for two different reasons

A.17.7 asked this question once already (confidence-gated post-hoc rules, transition-type
fittability) and got a clean "no." This section re-asks it with two purpose-built, more targeted
feature candidates, under the same strict discipline (fit the rule and its threshold on TRAIN only,
then apply the frozen rule unchanged to TEST — never peek at TEST while choosing anything).

**Candidate 1 — `deep_mass` escalation rule.** Mirrors the retired Tier-1 escalation clause
(§Tier-1 fix, history above): if the RL vote's budget-weighted mass on the `deep` arm exceeds a
threshold `T`, escalate the chosen preset upward by one level. Swept `T` over the same grid used
throughout this investigation's threshold work; the TRAIN-optimal `T` produces **net = 0** on TRAIN
itself — exactly as many previously-correct TRAIN articles get pushed into a new error as
previously-incorrect ones get fixed, no net gain even on the split it was fit to. Applying that
same frozen threshold to TEST unchanged gives **net = −1**: the rule introduces one more error than
it fixes. A rule that is already a wash on its own fitting data has no business being trusted on
held-out data, and the TEST number confirms it — this candidate is rejected outright.

**Candidate 2 — `neg_mass` (exploration-harmful section mass).** A different, more targeted
feature: the budget-weighted mass of an article's sections whose *own* section-level reward
genuinely favors a **cheaper** arm than the one actually chosen — i.e. sections where more
exploration is not merely wasted cost but actively reward-negative. Unlike `deep_mass` (a vote-mass
statistic available from any single RL forward pass), `neg_mass` requires each section's
**3-draw-averaged** reward (`section_oracle_averaged.json`), since a single production draw's
section-level reward is exactly the noisy quantity A.16.1/A.19.1-19.2 already found unreliable for
this kind of fine discrimination.

Swept `T` on TRAIN and found a genuinely well-supported optimum — not a single fragile point, but a
**whole plateau, `T` ∈ [0.40, 0.75]**, over which the rule's TRAIN behavior does not change: it
correctly fixes `07_reasoning_planning` (chosen `light`, oracle `skip`, this checkpoint's own
largest-margin TEST-adjacent error type per A.17.4) blind — i.e. using only TRAIN-fit machinery,
never having been shown this specific TEST article's answer — and produces **zero TEST collateral
damage**: no other TEST article's chosen preset changes for any `T` in that entire range. This is
by a wide margin the most promising single feature found in this whole corrector line, TRAIN-fit
and held-out-verified in the same rigorous style as G0/H0/J0/C2.

**But it cannot ship, for a structural reason no amount of further threshold-tuning fixes.**
`section_oracle_averaged.json` requires the 3-draw replication (production + 2 replicate write+grade
passes) to already exist for the article in question — i.e. it requires having **already generated
and graded all 4 arms' drafts** before the rule can compute its own input feature. A preset-choice
corrector's entire purpose is to decide *before* generation which arm to run; a feature that is only
computable *after* generation and grading cannot inform that decision at real inference time. This
is not a data-availability gap that more replication closes — it is definitional: the feature is
downstream of the very generation step it would need to gate.

**Qualitative dig on why `07_reasoning_planning` fixes so cleanly.** Read the actual section content
of its three highest-`neg_mass`-contributing sections (S4, S7, S8): all three are **pre-scripted
worked-example continuations** — sections that continue a fixed, already-determined worked example
or tutorial thread, where the "next step" is dictated by the example's own internal logic rather
than an open question further research could usefully inform. This is a plausible, concrete
mechanism for why exploration is reward-negative here specifically (there is nothing left to
discover, only more of the same scripted continuation to write).

**This mechanism does not generalize, checked against the only other genuine TRAIN case of the same
type.** `11_multimodal__var_standard` is the sole other TRAIN article where reward genuinely favors
`skip` over an escalated arm chosen instead (the finalized N=3 relabeling, see the N=5-decision
memory entry). Its sections do **not** show the same pre-scripted-worked-example signature — the
qualitative finding is specific to `07_reasoning_planning`, not a reusable content-type rule.

**A candidate pre-generation-available proxy for "worked-example rigidity" also fails to separate
the two cases.** Words-per-mandatory-bullet (word budget ÷ count of guideline-mandated content
bullets — tighter budgets suggesting more scripted, less open-ended content) gives
`07_reasoning_planning` wpb=90.7 vs `11_multimodal__var_standard` wpb=143.1 — a large,
right-direction gap in isolation, but a **dozen** other TRAIN/TEST articles land numerically between
these two values without exhibiting the reward-favors-skip pathology either one does. The proxy
cannot cleanly threshold the two known cases apart from the rest of the corpus, so it is not usable
as a discriminating pre-generation feature.

**Conclusion: the corrector-investigation line is abandoned, for two independent reasons that both
have to be true simultaneously for a corrector to ship — and neither candidate clears both.**
`deep_mass` fails the more basic bar (doesn't even help on TRAIN). `neg_mass` clears the statistical
bar cleanly but fails the availability bar (its feature doesn't exist before the decision it would
inform). No further threshold engineering on either candidate can fix its respective failure mode.
**Corpus expansion remains the only lever with legitimate headroom** — the same conclusion A.9
already reached for the separate `n=16` TEST-measurement-floor problem, now independently arrived at
again for the downstream-corrector question specifically: more TRAIN examples of the actual TEST
error transition types (per A.17.7's fittability-ceiling argument, still valid) is the only path
that doesn't run into one of these two walls.

### A.19.7 Guarded-constant baselines — isolating genuine RL discrimination from "free" guard credit

Every constant-baseline comparison so far in this document (A.17.1, A.19.5) has compared `run33/ep81`
(which always runs through the deterministic policy guards of A.17.2 — forbidden→`skip`,
required→≥`light`) against a **raw, unguarded** constant (e.g. plain "always predict `light`" with
no guard applied at all). This overstates the model's real edge on any article whose policy is
`forbidden` or `required`: the guard fixes those articles identically regardless of which arm the
underlying policy would otherwise have predicted, so some of `run33/ep81`'s apparent win over
`always-light` is really just "guards give both of us the same free correction on `State_of_
LLM_Reasoning`," not genuine RL-level discrimination. `guarded_constant_baseline.py` (new script,
`research_agent_local/training/`) re-scores each of the four constants **through the identical
guard function** `run33/ep81` uses, then re-runs every comparison fairly.

**TRAIN (n=24):**

| baseline | exact | near | miss | MAE | regret mean | regret max |
|---|---|---|---|---:|---:|---:|
| always-skip | 9/24 (37.5%) | 9/24 (37.5%) | 6/24 (25.0%) | 1.042 | 0.0980 | 0.1661 |
| always-light | 17/24 (70.8%) | 3/24 (12.5%) | 4/24 (16.7%) | 0.458 | 0.0161 | 0.0412 |
| always-standard | 10/24 (41.7%) | 13/24 (54.2%) | 1/24 (4.2%) | 0.625 | 0.0507 | 0.1419 |
| always-deep | 12/24 (50.0%) | 2/24 (8.3%) | 10/24 (41.7%) | 0.958 | 0.0375 | 0.1092 |

**TEST (n=16):**

| baseline | exact | near | miss | MAE | regret mean | regret max |
|---|---|---|---|---:|---:|---:|
| always-skip | 2/16 (12.5%) | 6/16 (37.5%) | 8/16 (50.0%) | 1.625 | 0.1103 | 0.2193 |
| always-light | 7/16 (43.8%) | 5/16 (31.2%) | 4/16 (25.0%) | 0.812 | 0.0230 | 0.0648 |
| always-standard | 5/16 (31.2%) | 10/16 (62.5%) | 1/16 (6.2%) | 0.750 | 0.0383 | 0.1225 |
| always-deep | 5/16 (31.2%) | 4/16 (25.0%) | 7/16 (43.8%) | 1.188 | 0.0263 | 0.0905 |

Guarding `always-light` raises its TEST exact count from A.17.1's unguarded 6/16 (37.5%) to 7/16
(43.8%) — the single extra hit is `State_of_LLM_Reasoning`, exactly the article the guard is
supposed to fix, confirming the "free credit" mechanism is real and worth this correction.

**McNemar exact test, `run33/ep81` vs. each guarded constant, TEST:**

| baseline | b | c | n | one-sided p | significant (α=0.05)? |
|---|---:|---:|---:|---:|---|
| always-skip | 10 | 1 | 11 | 0.0059 | yes |
| always-light | 4 | 0 | 4 | 0.0625 | **no** |
| always-standard | 9 | 3 | 12 | 0.0730 | **no** |
| always-deep | 7 | 1 | 8 | 0.0352 | yes |

**This is a real, honest downgrade from A.19.5's unguarded read.** Once `always-light` and
`always-standard` are given the same guard credit `run33/ep81` gets, the significance verdict flips
for both: `always-light` moves from *p*=0.03125 (significant) to *p*=0.0625 (not significant, n
shrinks from 5 discordant pairs to 4 once the guard-fixed article stops counting as a `run33`-only
win); `always-standard` moves from *p*=0.0461 (barely significant) to *p*=0.0730 (not significant).
`always-skip` and `always-deep` — the two baselines this whole A.19 pass was really about — remain
significant under fair guarding, unchanged in their qualitative conclusion.

**Cross-checked the borderline `always-light` case two more independent ways** (`stats_crosscheck.py`,
new script, same directory): exact Wilcoxon signed-rank test and an exact sign-flip permutation test
on the paired per-article ordinal-distance and regret reductions, both restricted to the n=4 (MAE) /
n=5 (regret) articles where `run33/ep81` and guarded-`light` actually disagree. **All three tests
(McNemar, Wilcoxon, sign-flip permutation) agree exactly: p=0.0625** for both the MAE/ordinal-distance
and the regret comparison. This is not a coincidence — with this few discordant pairs, all three
tests are testing essentially the same binary sign pattern and necessarily converge. The honest
reading: `run33/ep81`'s edge over guarded-`light` specifically is directionally consistent (every
one of the 4-5 discordant articles favors the model, zero favor the baseline) but, by any test that
only uses the *sign* of each article's difference, still short of conventional significance at
`n=16`. A.19.8's bootstrap, which uses the full *magnitude* of every article's difference rather
than throwing away the many zero-difference ties, gives a sharper answer to the same question.

### A.19.8 Paired bootstrap confidence intervals, `run33/ep81` vs. guarded-`light`

The sign-based tests above (McNemar/Wilcoxon/permutation) discard the 11-12 TEST articles where
`run33/ep81` and guarded-`light` agree exactly, reducing effective `n` to 4-5 and correspondingly
weakening power. A paired bootstrap over **all 16** TEST articles' per-article differences uses that
discarded information instead (an article where both are equally right or equally wrong still
correctly contributes a zero to the resampled mean, tightening the estimate without needing to
change sign).

Computed via `stats_crosscheck.py` (paired bootstrap, `B`=100,000 resamples with replacement, fixed
seed for reproducibility):

| quantity | n | observed mean reduction | 95% CI | one-sided *p* (≤0) |
|---|---:|---:|---|---:|
| MAE / ordinal-distance reduction | 16 | 0.4375 | [0.125, 0.875] | 0.0102 |
| regret reduction | 15 (forbidden excluded) | 0.0102 | [0.0014, 0.0212] | 0.0112 |

Both intervals **exclude zero** and both one-sided *p*-values clear the conventional 0.05 threshold
comfortably — a materially stronger result than A.19.7's sign-based tests on the identical
comparison (`run33/ep81` vs. guarded-`light`, *p*=0.0625 by every sign-based test). The two views are
not in conflict: sign-based tests ask "is there a directionally-consistent trend clearly beyond what
chance sign-flipping alone could produce," which needs more discordant pairs than this comparison
happens to have; the bootstrap asks "is the magnitude-weighted average difference distinguishable
from zero," which the fuller n=16/15 samples (including the ties) answer more decisively. Read
together: `run33/ep81`'s advantage over guarded-`light` is real and quantifiably positive, even
though the raw discordant-pair count alone is too thin for the sign tests to certify it at *p*<0.05.

### A.19.9 Noise-ceiling baseline: how much of the remaining gap is measurement noise, not model error?

A different question from every comparison above: not "does `run33/ep81` beat baseline X," but "how
well *could* any single-draw predictor possibly do," given that the "true" (3-draw-averaged) oracle
label is itself only knowable after averaging draws no real-time policy ever sees. `noise_ceiling_
baseline.py` (new script) computes, for every article with `n_draws_used==3` replicate data, the
single-draw R_w argmax from **each** of the 3 independent draws (production, replicate1, replicate2)
alone, and checks how often that single-draw argmax already disagrees with the argmax of the
3-draw-averaged R_w used as ground truth — a pure measurement-noise ceiling, with zero model
involved on either side.

**TRAIN (n=24):** production=19/24 (79.2%, MAE 0.333), replicate1=16/24 (66.7%, MAE 0.417),
replicate2=17/24 (70.8%, MAE 0.458).

**TEST (n=16):** production=9/16 (56.2%, MAE 0.688), replicate1=11/16 (68.8%, MAE 0.375),
replicate2=10/16 (62.5%, MAE 0.438). **Pooled across all 3 draws (n=48): 30/48 (62.5%, MAE 0.500).**

**`run33/ep81`'s actual TEST performance (68.75% exact, MAE 0.375, A.17.1) matches or exceeds every
single-draw noise-ceiling figure above, including the pooled one.** It ties replicate1's own
single-draw ceiling exactly (68.8%≈68.75%, MAE 0.375 identical to 3 decimal places) and clears the
production-draw ceiling (56.2%) and the pooled ceiling (62.5%) by a comfortable margin. This is a
positive contextualizing result, read carefully: it does not mean the model is somehow better than a
perfect oracle (the "true" label is still the 3-draw average, unbeatable by construction) — it means
that **even an idealized policy that could perfectly read one single realization's own reward
landscape and argmax it** would disagree with the true label at a rate comparable to or worse than
what `run33/ep81` already achieves in practice. The remaining gap between `run33/ep81` and a perfect
oracle is therefore substantially a **measurement-noise floor**, not obviously a model-capacity
shortfall this checkpoint could still close with more training on the current corpus — reinforcing
A.19.6's conclusion that corpus expansion, not further correction/training on the existing 40
articles, is where the remaining legitimate headroom lives.

## A.20 `external_evidence_policy` classifier redesign — Scenario A/B/C validity audit and final framework (2026-08-29)

`generate_digests.py`'s `_FEATURES_USER_TEMPLATE` classifies every article's `external_evidence_policy`
as `forbidden` / `allowed` / `required` via 3 disjunctive trigger conditions bundled under `forbidden`,
here labeled Scenario A (overt ban), Scenario B (low-effort/conceptual-overview scope note), and
Scenario C (survey-of-named-sources framing). `forbidden` short-circuits `_preset_2d()` and the
inference-time `_apply_policy_guards()` straight to `skip`, with no override — the single highest-
consequence categorical decision in the whole pipeline. This appendix documents a full validity audit
of that classifier, prompted by growing skepticism (raised independently of any single bad prediction)
about whether Scenarios B and C actually earn the same trust as Scenario A.

### A.20.1 The three trigger scenarios, as currently prompted

- **Scenario A** — overt: *"do not use sources beyond the provided list"*, *"only reference the
  supplied materials"*, *"no external research allowed"*.
- **Scenario B** — low-effort scope note: *"this article is a conceptual overview; surface-level
  treatment is expected and depth, exhaustive coverage, or production code are explicitly NOT
  required."*
- **Scenario C** — survey framing: *"the article's entire stated scope is to summarize/survey a fixed,
  named set of provided sources... such that the golden sources structurally ARE the complete content
  requirement."*

Across the full 40-article corpus (24 TRAIN + 16 TEST), only two real forbidden classifications exist
before this audit: all 8 TRAIN `var_minimal` variants (Scenario B) and 1 TEST article,
`State_of_LLM_Reasoning` (Scenario C). Scenario A had never fired on its own.

### A.20.2 Scenario B's trigger phrase is copied verbatim from the prompt's own worked example

The Scenario-B sentence embedded in the prompt as an illustrative example —
*"this article is a conceptual overview; surface-level treatment is expected and depth, exhaustive
coverage, or production code are explicitly NOT required"* — is **word-for-word identical** to the
actual guideline text found in `02_workflows_vs_agents__var_minimal/article_guideline.md` (and,
confirmed later in A.20.4, in all 8 `var_minimal` guidelines). The classifier isn't generalizing a
semantic pattern for this trigger; it's echoing its own few-shot example back. This is a stronger,
more literal form of "mechanical" than the earlier-suspected "same clause repeated 8 times" — it's
verbatim identity with the prompt itself.

### A.20.3 Raw R_w reward argmax vs. forced-skip label, all 8 TRAIN `var_minimal` articles

Pulling each article's actual 4-way `r_w_rewards` from `rl_guards_only_train_and_test_results_run33_
averaged_confidence_epoch81.md` and checking the true reward-maximizing preset, independent of the
forced-skip policy override:

| article | P0/skip | P1/light | P2/standard | P3/deep | true argmax | vs. forced skip |
|---|---:|---:|---:|---:|---|---|
| 02_workflows_vs_agents | 0.209 | **0.263** | 0.154 | 0.216 | light | **wrong by +0.054** |
| 03_context_engineering | **0.225** | 0.183 | 0.204 | 0.210 | skip | correct |
| 05_workflow_patterns | 0.212 | 0.210 | **0.232** | 0.189 | standard | **wrong by +0.020** |
| 06_tools | **0.150** | 0.148 | 0.122 | 0.109 | skip (razor-thin) | correct-ish |
| 08_react_practice | **0.175** | 0.112 | 0.098 | 0.049 | skip (decisive) | correct |
| 09_RAG | **0.120** | 0.117 | 0.101 | 0.115 | skip (near 4-way tie) | correct-ish |
| 10_memory_knowledge_access | 0.092 | **0.120** | 0.040 | 0.064 | light | **wrong by +0.028** |
| 11_multimodal | 0.101 | **0.155** | 0.067 | 0.035 | light | **wrong by +0.054** |

Only 4/8 have skip as the genuine reward-argmax, and two of those are themselves razor-thin/near-4-way
ties. 3/8 have light winning by a real, decisive margin (+0.028 to +0.054 — an order of magnitude
larger than the +0.0029 margin that A.19 already treated as worth a full manual review). 1/8 has
standard winning.

### A.20.4 The "8/8 EXACT" verdict is circular — and a `grep_search` false-negative initially hid the real cause

Two errors compounded here and are recorded for posterity:

1. **The eval report's "8/8 EXACT HIT" for `var_minimal` is not independent validation.**
   `compute_article_oracle.py` applies the *same* forbidden-policy override when computing the oracle
   label (`oracle_preset` is forced to `skip` regardless of the underlying `r_w_rewards`), and every
   one of these 8 rows is explicitly annotated `Regret: +0.0000 (not counted — forbidden policy, P1+
   rewards tainted)` and excluded from every real accuracy metric the report computes
   (`Reward-regret (allowed/required only, n=16; 8 forbidden excluded)`). Comparing a forced choice
   against an equally-forced oracle is tautological, not evidence.
2. **A `grep_search` tool malfunction produced a false "none of the other 7 have it" claim.** An
   initial check for a shared `## Brevity Requirements` clause across the other 7 `var_minimal`
   guidelines (beyond `08_react_practice`, where it was first spotted) returned empty results via the
   `grep_search` tool, seemingly confirming `08_react_practice` was an outlier. Direct shell `grep`
   against the same files immediately found the clause, byte-identical, in **all 8** — `grep_search`
   silently returns empty for files under `rl_training_data/bases/` on this workspace (the same
   failure mode already seen once earlier against `rl_training_data/checkpoints/`). **Lesson for future
   sessions: never trust a `grep_search` "no matches" result under `rl_training_data/` without a direct
   shell `grep`/`read_file` cross-check.**

### A.20.5 All 8 `var_minimal` guidelines share one identical Brevity Requirements clause — and it is genuinely Scenario-A wording, not Scenario-B

```
## Brevity Requirements
- Total article length must not exceed 1,500 words. This is a hard ceiling.
- Do NOT introduce external libraries, real-world case studies, named production
  systems, or benchmark papers that are not already established in the course.
  External examples are explicitly out of scope.
- No production code examples. Pseudocode or short illustrative snippets (under
  10 lines) are allowed only if the original section already implied code;
  otherwise omit code entirely.
```

Verified byte-for-byte identical (via direct shell `grep -A3 "^## Brevity Requirements"`) across
`02_workflows_vs_agents`, `03_context_engineering`, `05_workflow_patterns`, `06_tools`,
`08_react_practice`, `09_RAG`, `10_memory_knowledge_access`, and `11_multimodal` `var_minimal`
variants. The middle bullet — *"Do NOT introduce external ... explicitly out of scope"* — is an overt,
unambiguous prohibition, i.e. genuine Scenario-A language, distinct from (and stronger than) the
Scenario-B "conceptual overview... not required" sentence that also happens to sit earlier in the same
document.

### A.20.6 Is the light-arm reward advantage in the 3 "wrong" articles legitimate content improvement, or a rule violation?

Before concluding anything from A.20.3's reward table, every scored `depth_enhancement`/
`breadth_enhancement` credit instance across the light-arm episodes of the 3 contested articles
(`02_workflows_vs_agents`, `10_memory_knowledge_access`, `11_multimodal`; 2 replicate draws each, 6
episodes, 12 total credit instances) was read directly from `reasoning.json`. **Every single instance
traces to a genuinely new, non-golden, exploration-phase external source:**

| article | credited addition | source |
|---|---|---|
| 02_workflows_vs_agents | microservices-architecture analogy | softwareseni.com |
| 02_workflows_vs_agents | "errors cascade" failure mode | dev.to |
| 02_workflows_vs_agents | prompt-injection/data-exfiltration attack naming | thenewstack.io |
| 02_workflows_vs_agents | workflow-limitation motivation | arxiv.org/html/2510.09244v1 (not golden) |
| 10_memory_knowledge_access | multi-agent memory-conflict research | christophermeiklejohn.com |
| 10_memory_knowledge_access | healthcare-compliance case study | arxiv.org/html/2510.25445v1 (not golden) |
| 11_multimodal | ColPali's MaxSim mechanism detail | arxiv.org/html/2407.01449v4 (not golden) |
| 11_multimodal | audio-transcription-error cross-domain analogy | tianpan.co blog |

Every one of these is a textbook instance of exactly what the Brevity Requirements clause prohibits
(*"real-world case studies, named production systems, or benchmark papers that are not already
established in the course"*). The "light wins on reward" finding in A.20.3 is not neutral counter-
evidence to the forced-skip policy — it is **entirely constituted by the mechanism the policy exists to
prevent**. The reward model's `de`/`be` credit has no way to check "is this source in-scope for this
article"; it only checks "is this genuinely new, well-sourced content," so it necessarily rewards
exactly the violation. Using this reward signal to argue against enforcing the ban is circular.

### A.20.7 Conclusion on Scenarios A and B

- **Scenario B is eliminated as a trigger.** Its defining sentence is a verbatim copy of the prompt's
  own example (A.20.2) and, standing alone, conflates an effort-level statement ("depth/exhaustive
  coverage not required") with a source-access restriction — a category error. Guidelines matching only
  this language fall back to `allowed`.
- **Scenario A is kept unchanged as an unconditional, reward-independent hard force to `skip`.**
  Respecting an explicit, overt "do not do X" is a legitimate override of reward-maximization on its
  own terms — the guideline author's stated intent is the authority here, not a reward model that has
  no way to penalize violating it. This is now not just philosophically argued but empirically
  confirmed: A.20.6 shows the entire reward case against enforcement is built on citing exactly the
  material the ban forbids. The Brevity Requirements clause (A.20.5) is genuine Scenario-A wording and
  correctly forces `skip` for all 8 `var_minimal` articles, independent of whatever else Scenario B
  contributed.

### A.20.8 Scenario C case study: `State_of_LLM_Reasoning`'s near-tie margin and the same confound, found independently

`State_of_LLM_Reasoning` (TEST, the corpus's only Scenario-C article) has an article-level R_w margin
of **skip=0.2745, light=0.2716, standard=0.2486, deep=0.2423** — a raw skip-vs-light margin of just
**+0.0029**, tighter than the `HNSW` near-tie margin (0.0343) that A.19 already flagged for manual
review. The section-by-section decomposition (`oracle_review/State_of_LLM_Reasoning.md`) shows the
`(explore: skip=X light=Y)` annotation — isolating exactly the reward attributable to depth/breadth
credit — is `0.0000` for both arms in every section **except** S11 (`explore: skip=0.0000
light=0.3334`), the single largest-magnitude section in the whole table (weight=0.026,
contribution=−0.0168 against skip). Every other large-magnitude section (S19 weight=0.149, S2
weight=0.186, S4 weight=0.096) shows zero exploration credit on both arms — their skip/light gap is
pure `cc`/`fl`/`ga` draw-to-draw noise (word-count-tolerance misses, image-placement variance across
only 3 replicate draws per arm), not a genuine content-quality signal.

S11's light-arm credit is explicitly traced (in `reasoning.json`) to `lesswrong.com/posts/...on-recent-
results-in-llm-latent-reasoning` and `arxiv.org/html/2604.04902v1` — **neither is among the guideline's
declared 14-paper survey scope.** This is the same mechanism as A.20.6, independently rediscovered for
Scenario C: the one section making light look competitive earns that credit specifically by violating
the article's own stated survey scope. Discounting that one section's confounded credit moves the
effective margin from +0.0029 to roughly **+0.0232** — about 8× more comfortable in skip's favor.

### A.20.9 Is `07_reasoning_planning` (the corpus's one clear Scenario-C-adjacent failure) a genuine statistical outlier?

Before trusting any narrow threshold rule built around this article's semantic-signal profile, a
combined multivariate outlier check was run: z-scored `source_independence`, `topic_canonicity`,
word-weighted `w_scripted`, word-weighted `w_risk`, and RL `confidence`, computed purely from the
corpus's own mean/sd (n=31, all non-forbidden TEST+TRAIN articles, no threshold tuned to isolate this
article), then ranked every article by combined L2 distance from the corpus centroid.

**Result: `07_reasoning_planning` ranks 22nd of 31** — solidly mid-pack, below-median extremeness. Its
only mildly notable trait is `source_independence` (z=−1.37, 3rd-lowest), which is not an extreme-tail
value by conventional standards (|z|≳2). `w_risk` sits almost exactly on the corpus mean (z=+0.01). An
earlier 4/5-condition threshold rule that appeared to isolate this article perfectly was shown to be
curve-fitting a box around a single known point (n=1 positive example, ever) — this outlier check
falsifies the "true outlier" framing more rigorously: even the seemingly bespoke combination of traits
is unremarkable once measured against the corpus's own distribution rather than hand-picked thresholds.

### A.20.10 Confidence-gating for Scenario C's light-vote case: raw P(skip) vs. P(light) is a strong, validated discriminator

Testing whether the RL model's own **raw, pre-cost-adjustment** softmax mass (`rl_agg_probs`, not the
scalar `confidence` field, which equals `P(chosen preset)` and conflates unrelated comparisons) between
just the two allowed classes predicts which one is actually correct, across every corpus article where
the true label is skip-or-light and the model's argmax votes light:

| group | article | P(skip) | P(light) | matches P(skip) vs P(light) ordering? |
|---|---|---:|---:|---|
| true=skip | `State_of_LLM_Reasoning` | 0.358 | 0.245 | skip > light ✓ |
| true=skip | `08_react_practice__var_minimal` | 0.707 | 0.293 | skip > light ✓ |
| true=skip | `11_multimodal__var_standard` | 0.471 | 0.367 | skip > light ✓ |
| true=skip | `07_reasoning_planning` | 0.158 | 0.307 | light > skip ✗ (exception) |
| true=light | `02_workflows_vs_agents__var_demanding` | 0.103 | 0.172 | light > skip ✓ |
| true=light | `02_workflows_vs_agents__var_standard` | 0.000 | 0.356 | light > skip ✓ |
| true=light | `03_context_engineering__var_demanding` | 0.151 | 0.346 | light > skip ✓ |
| true=light | `05_workflow_patterns__var_standard` | 0.000 | 0.205 | light > skip ✓ |
| true=light | `13_agent_framework` | 0.196 | 0.323 | light > skip ✓ |
| true=light | `11_multimodal__var_minimal` | 0.310 | 0.379 | light > skip ✓ |

**9/10 correct.** The one exception, `07_reasoning_planning`, is policy=`allowed` (not Scenario-C-
capped at all — its "chosen" preset comes from the full unconstrained 4-way pipeline, so it was never
actually subject to the mechanism being tested here; it's included purely as a general correlation
check, not a claim the cap mechanism failed on it). Note also: for every article in the "true=light"
group, the raw distribution's actual argmax is `standard`, not `light` (e.g. `02_dem`: skip=0.10,
light=0.17, **standard=0.72**, deep=0.0) — the cost-sensitive rule pulls the final vote down to light,
and light only edges out skip because the whole distribution has shifted toward "needs more," pushing
skip to last place. The P(skip)-vs-P(light) comparison is riding on that real "needs more than skip"
signal, not isolating a narrow skip/light judgment in a vacuum.

### A.20.11 Standard/deep votes under Scenario C — the tail comparison becomes unstable exactly when neither class dominates

Extending the same P(skip)-vs-P(light) comparison to articles where the model's actual vote is
standard/deep (i.e., testing whether the *residual* skip/light split remains meaningful once neither is
the dominant class) using 5 general corpus examples where deep is unambiguously the correct answer:

| article | P(skip) | P(light) | true label | tail-argmax |
|---|---:|---:|---|---|
| 06_tools__var_standard | 0.120 | 0.183 | deep | light |
| Dark_Dimension | 0.200 | 0.344 | deep | light |
| Earth_Oceans_Origin | 0.000 | 0.143 | deep | light |
| 04_structured_outputs | **0.267** | 0.133 | deep | **skip** |
| 09_RAG__var_demanding | **0.436** | 0.029 | deep | **skip** |

In 2/5 cases the residual split favors skip despite the article clearly needing deep exploration —
the tail comparison is not reliable once it's not backed by a genuine top-1/top-2 preference. **Rule
adopted for Scenario C: if the RL vote is standard or deep, cap deterministically to `light` (do not
resolve via the tail-argmax); if the case remains genuinely ambiguous, leave the choice to a human/
downstream reviewer rather than auto-deciding** — flagged-for-review, not silently auto-picked, per the
same log-and-review philosophy used elsewhere in this investigation (A.17.7, A.19.6).

### A.20.12 Final consolidated framework

| scenario | trigger | final treatment | justification |
|---|---|---|---|
| **A** (overt ban, incl. the Brevity Requirements clause) | explicit "do not use/introduce external sources" | **hard, unconditional force to `skip`**, independent of downstream reward | Respects genuine, explicit user intent; A.20.6/A.20.8 confirm the reward case against it is itself built on citing exactly the forbidden material |
| **B** (low-effort scope note, standalone) | "conceptual overview... not required," no accompanying overt ban | **eliminated** — falls back to `allowed` | Verbatim copy of the prompt's own example (A.20.2); conflates effort-level with source-access, a category error; TRAIN reward data disagrees with forced-skip in 4/8 real instances (A.20.3) |
| **C** (survey-of-named-sources framing) | "the article's entire scope is to summarize/survey N named sources" | **capped ceiling at `{skip, light}`**: light stands if `P(light) ≥ P(skip)` in the raw distribution (A.20.10); skip stands otherwise; a standard/deep vote is capped down to `light`, not resolved via the unstable tail-argmax (A.20.11); genuinely ambiguous cases are flagged for review rather than auto-decided | Explicit statement of the article's fundamental *nature* (exploitation/survey, not exploration) — same principle as A (respect stated intent over reward), but a softer ceiling since a single light touch doesn't categorically contradict "this is a survey" the way any exploration would contradict an outright ban |

Scenarios A and C both subordinate reward-maximization to explicit author intent; they differ only in
what is explicitly stated (a total ban vs. a task-nature framing) and therefore in how hard the
resulting ceiling is. Scenario B never earned that trust in the first place — its trigger was
templated/mechanical, not a bespoke editorial decision, and the TRAIN reward data (A.20.3) shows it
being wrong close to half the time.

### A.20.13 Why cap standard/deep votes to `light`, not `skip`? Corpus-wide empirical validation (2026-08-30)

A.20.11 established the *design rule* (cap a standard/deep vote deterministically to `light` rather
than resolving it via the unstable tail-argmax) and A.20.12 folded it into the framework with a
*qualitative* justification only — "a softer ceiling since a single light touch doesn't categorically
contradict 'this is a survey.'" This section supplies the missing *quantitative* backing: across every
corpus article whose true oracle label is `standard` or `deep` (i.e., where meaningful exploration is
genuinely warranted) and whose policy is not `forbidden`, does `R_w[light]` actually beat `R_w[skip]`?
If light were frequently a *worse* reward choice than skip in this population, capping down to light
rather than skip would be indefensible on reward grounds, however well it reads qualitatively.

**Method:** read `oracle_arm_idx` and `r_w_rewards_list` directly from every TRAIN+TEST article's
`article_oracle.json` (no inference, no guard applied), filter to `oracle_arm ∈ {standard, deep}` and
`policy != forbidden`, and compare `R_w[skip]` vs. `R_w[light]` per article:

| article | oracle | policy | R_w[skip] | R_w[light] | winner |
|---|---|---|---:|---:|---|
| `03_context_engineering__var_standard` | standard | allowed | 0.2429 | 0.2816 | light > skip |
| `06_tools__var_standard` | deep | allowed | 0.1460 | 0.2300 | light > skip |
| `09_RAG__var_standard` | deep | allowed | 0.0772 | 0.1045 | light > skip |
| `09_RAG__var_demanding` | deep | allowed | 0.1147 | 0.1826 | light > skip |
| `10_memory_knowledge_access__var_demanding` | deep | allowed | 0.2109 | 0.3110 | light > skip |
| `11_multimodal__var_demanding` | standard | allowed | 0.2747 | 0.2731 | skip > light (exception) |
| `04_structured_outputs` | deep | allowed | 0.2756 | 0.3151 | light > skip |
| `14_agent_system_design` | standard | allowed | 0.2677 | 0.3776 | light > skip |
| `29_evaluation_metrics` | standard | allowed | 0.3201 | 0.3930 | light > skip |
| `Bird_Eye_Extreme` | standard | allowed | 0.2748 | 0.3614 | light > skip |
| `Dark_Dimension` | deep | allowed | 0.3411 | 0.5167 | light > skip |
| `Earth_Oceans_Origin` | deep | allowed | 0.2853 | 0.3615 | light > skip |
| `Insects_Consciousness` | deep | allowed | 0.3596 | 0.5191 | light > skip |
| `Understanding_Reasoning_LLMs` | standard | allowed | 0.2502 | 0.3828 | light > skip |

**`R_w[light] > R_w[skip]` in 13/14 (93%)** of every standard/deep-oracle, non-forbidden article in the
whole 40-article corpus. The sole exception, `11_multimodal__var_demanding`, is a near-tie — the
margin (0.2747 vs. 0.2731) is only 0.0016, well inside the measurement-noise floor A.19.9 already
established (single-draw MAE ≈0.33-0.69 ordinal steps; a 0.0016 R_w gap is far smaller than that noise
floor implies is distinguishable) — not a genuine counter-example.

This is a **uniform, distribution-free** finding: it is computed once across the whole corpus as a
general design justification for *which fixed direction* to clamp toward, not as a per-article rule
that consults any individual article's live RL distribution. That distinction matters for A.19.7's
"guarded-constant baselines must not borrow real per-article signal" discipline (also reaffirmed for
`guarded_constant_baseline.py` directly, A.21.1 below): choosing the clamp *target* (light, not skip)
from an aggregate, corpus-wide reward pattern is a legitimate, fixed design decision available equally
to the real model and to any trivial constant baseline — unlike the separate, genuinely per-article
`P(skip)` vs. `P(light)` arbitration (A.20.10), which only the real model's own live distribution can
supply and which a constant baseline correctly never gets to use (A.21.1's `_apply_policy_guards`
ceiling-only clamp).

**Conclusion:** capping standard/deep votes to `light` rather than `skip` is not just qualitatively
softer (A.20.12) — it is the empirically better reward choice 13/14 times in the real corpus, with the
one exception being statistically indistinguishable from a tie. No change to A.20.11/A.20.12's rule or
to any guard implementation is warranted by this check; it confirms the existing design.

### A.20.14 The residual P(skip) vs P(light) split has no confirmed skip-favoring signal — AMBIGUOUS now fires unconditionally (2026-08-31)

A.20.11's original design conditioned the AMBIGUOUS flag on the residual distribution *disagreeing*
with the light default (`P(skip) > P(light)`), implicitly treating the *agreeing* case (`P(light) >=
P(skip)`) as reassuring evidence the clamp is safe. Re-examined this assumption directly: does the raw
RL distribution's own P(skip)-vs-P(light) ordering actually track which arm is reward-better, anywhere
in the corpus's standard/deep-voted population?

Cross-referenced every corpus article where a real RL aggregate distribution is on record (A.19/A.20.11's
own 5-article validation set, plus 1 more from saved eval JSONs) against A.20.13's `R_w[skip]` vs.
`R_w[light]` figures for the same articles:

| article | P(skip) | P(light) | residual favors | R_w[skip] | R_w[light] | truly better | residual correct? |
|---|---:|---:|---|---:|---:|---|---|
| `06_tools__var_standard` | 0.120 | 0.183 | light | 0.1460 | 0.2300 | light | yes |
| `Dark_Dimension` | 0.200 | 0.344 | light | 0.3411 | 0.5167 | light | yes |
| `Earth_Oceans_Origin` | 0.000 | 0.143 | light | 0.2853 | 0.3615 | light | yes |
| `Understanding_Reasoning_LLMs` | 0.000 | 0.058 | light | 0.2502 | 0.3828 | light | yes |
| `04_structured_outputs` | 0.267 | 0.133 | **skip** | 0.2756 | 0.3151 | light | **no** |
| `09_RAG__var_demanding` | 0.436 | 0.029 | **skip** | 0.1147 | 0.1826 | light | **no** |

**Light is truly reward-better in all 6/6 cases — including both cases where the residual itself favored
skip.** This is the key result: every time the residual "voted" for skip, it was wrong; every time it
agreed with light, light really was better. Since light is already known to win 13/14 (93%) of the time
in this population regardless of what any per-article signal says (A.20.13), a residual split with *zero
real discriminating power* would be expected to look exactly like this — "agreeing" with light most of
the time purely by riding the base rate, while never once being vindicated on the occasions it disagrees.
That is precisely the pattern observed: **0/2 confirmed hits for "residual says skip," 4/4 confirmed hits
for "residual says light,"** which is fully consistent with the residual carrying no information beyond
the population base rate itself, not with it having genuine skip-vs-light discriminating skill.

**Conclusion (confirms the user's stated hypothesis): there is no data support, in either direction, for
treating a standard/deep vote's residual P(skip) vs P(light) split as evidence about which of {skip,
light} is actually better once capped — including no confirmed case, anywhere checked, where skip is
truly the reward-optimal choice.** Conditioning the AMBIGUOUS flag on the residual's direction was
therefore drawing a distinction the data doesn't support: the "non-disagreeing" cases were never actually
validated as safer, they simply hadn't been checked.

**Change shipped:** `_apply_policy_guards` (`preset_planner_handler.py`, mirrored in
`test_grok_planner.py`) and `fallback_aggregator` now mark **every** standard/deep-vote-capped-to-light
clamp as AMBIGUOUS, unconditionally — not just the subset where the residual happened to favor skip. The
residual's P(skip)/P(light) values are still reported in the flag text for transparency, but no longer
gate whether the flag fires. `research_instructions_prompt.py`'s step 3.4 updated to match: the
ask-the-user protocol now triggers on every capped + standard/deep clamp, with no "residual agrees, skip
asking" exception.

## A.21 Phase 9 — guarded-constant / statistical / noise-ceiling baselines refreshed for the `capped` policy fix (2026-08-30)

A.19.7-A.19.9 were computed 2026-08-27 — before Scenario C's `capped` policy value existed as a
classifier output at all, and before the skip-vs-light in-bounds guard bugfix. `guarded_constant_
baseline.py`, `stats_crosscheck.py`, and `noise_ceiling_baseline.py` were re-run against the current,
post-fix corpus for the record.

### A.21.1 Guarded-constant baselines refreshed (supersedes A.19.7)

**TRAIN (n=24):**

| baseline | exact | near | miss | MAE | regret mean | regret max |
|---|---|---|---|---:|---:|---:|
| always-skip | 10/24 (41.7%) | 8/24 (33.3%) | 6/24 (25.0%) | 1.000 | 0.0876 | 0.1628 |
| always-light | 17/24 (70.8%) | 3/24 (12.5%) | 4/24 (16.7%) | 0.458 | 0.0161 | 0.0412 |
| always-standard | 10/24 (41.7%) | 13/24 (54.2%) | 1/24 (4.2%) | 0.625 | 0.0507 | 0.1419 |
| always-deep | 12/24 (50.0%) | 2/24 (8.3%) | 10/24 (41.7%) | 0.958 | 0.0375 | 0.1092 |

**TEST (n=16):**

| baseline | exact | near | miss | MAE | regret mean | regret max |
|---|---|---|---|---:|---:|---:|
| always-skip | 2/16 (12.5%) | 6/16 (37.5%) | 8/16 (50.0%) | 1.625 | 0.1034 | 0.2193 |
| always-light | 6/16 (37.5%) | 6/16 (37.5%) | 4/16 (25.0%) | 0.875 | 0.0217 | 0.0648 |
| always-standard | 4/16 (25.0%) | 11/16 (68.8%) | 1/16 (6.2%) | 0.812 | 0.0361 | 0.1225 |
| always-deep | 4/16 (25.0%) | 5/16 (31.2%) | 7/16 (43.8%) | 1.250 | 0.0248 | 0.0905 |

**McNemar exact test, `run33/ep81` vs. each guarded constant, TEST:**

| baseline | b | c | n | one-sided p | significant (α=0.05)? |
|---|---:|---:|---:|---:|---|
| always-skip | 10 | 1 | 11 | 0.0059 | yes |
| always-light | 5 | 0 | 5 | 0.0312 | **yes** |
| always-standard | 10 | 3 | 13 | 0.0461 | **yes** |
| always-deep | 8 | 1 | 9 | 0.0195 | yes |

**Headline change from A.19.7: `always-light` and `always-standard` both flip back from "not
significant" to significant.** Root cause, fully traced (not just "the guard fires differently now"):
before this segment's A.20 classifier redesign, all 3 trigger scenarios (A/B/C) collapsed to the
single `forbidden` policy value (A.20's own framing — Scenario C wasn't yet split out). `State_of_
LLM_Reasoning` triggered the Scenario-C condition, so it was classified `forbidden` at the time A.19.7
ran — and `forbidden`'s guard forces **every** constant down to `skip` unconditionally, which happens
to equal this article's oracle (`skip`) exactly. That gave **all four** guarded-constant baselines an
unearned EXACT hit on this one article: precisely the "free credit" risk A.19.7 itself warned about,
just not yet visible because the classifier hadn't yet been split into A.20's finer A/B/C treatment.
After the redesign, this article is correctly reclassified `capped` — a strictly softer ceiling than
`forbidden` (clamps to `light`, never forces all the way down to `skip`). That removes the free credit
from `always-light`/`always-standard`/`always-deep` specifically: each loses exactly one EXACT→NEAR on
this one article (confirmed directly in the TEST table above vs. A.19.7's: exact 7→6, 5→4, 5→4
respectively, near +1 each, miss unchanged) — while `always-skip` is untouched (already predicting
`skip`, unaffected by which of `forbidden`/`capped` applies). Simultaneously, `run33/ep81` — via this
session's separate skip-vs-light in-bounds guard bugfix (this document's Issue 3) — still correctly
resolves to `skip` using its **own** real distribution, so it keeps its correct prediction on this
article even without the crutch of a forced-skip classification. Net effect: three fresh, genuine
discordant pairs in the model's favor (`b` +1 each for always-light/standard/deep: 4→5, 9→10, 7→8),
while `always-skip`'s `b`/`c` are unchanged (10, 1). **This is a correction of a previously* too-strong*
guard (an over-broad `forbidden` collapse silently inflating every baseline's score), not a new form of
credit invented for the model** — the model's edge on this article is now counted as real
discrimination, not a guard artifact, on every baseline it's compared against.

*(Minor, unrelated note: TRAIN's `always-skip` row also moved, 9/24→10/24 exact — this is unrelated to
the `capped` mechanism, since no TRAIN article carries `capped` policy. It traces to
`11_multimodal__var_standard`, whose current classification is `allowed` with oracle=`skip`; under the
guard, `required` is the only branch that can change an already-`skip` constant's outcome
(`max(1, preset)`), so this is consistent with that one article no longer being classified `required`
as of the Aug-29 Scenario A/B/C redesign — not a symptom of anything to do with the capped fix itself.)*

### A.21.2 Statistical cross-checks refreshed (supersedes A.19.8)

Computed via `stats_crosscheck.py` against `run33/ep81` vs. guarded-`light`, current corpus:

| test | quantity | n | statistic | p (one-sided) |
|---|---|---:|---:|---:|
| Wilcoxon signed-rank | MAE/dist reduction | 5 | W+=15.0 | 0.0312 |
| Wilcoxon signed-rank | regret reduction | 6 | W+=19.0 | 0.0469 |
| Sign-flip permutation | MAE/dist reduction | 5 | sum=8.0000 | 0.0312 |
| Sign-flip permutation | regret reduction | 6 | sum=0.1563 | 0.0469 |
| Paired bootstrap (B=100,000) | MAE/dist reduction | 16 | mean=0.5000, CI=[0.1250, 0.9375] | 0.0023 |
| Paired bootstrap (B=100,000) | regret reduction | 16 | mean=0.0098, CI=[0.0014, 0.0203] | 0.0084 |

**A.19.7's original finding — all three sign-based tests converging on an identical, non-significant
p=0.0625 — no longer holds.** With `State_of_LLM_Reasoning` now a genuine discordant pair (A.21.1), the
sign-based tests (Wilcoxon, sign-flip) themselves clear α=0.05 (p=0.0312/0.0469), not just the
bootstrap. `run33/ep81`'s edge over guarded-`light` is now significant by every method tested.

### A.21.3 Noise-ceiling baseline reconfirmed unaffected (regression check for the Design C removal)

`noise_ceiling_baseline.py` never consults policy guards (pure replicate-draw measurement noise), so
its TEST-side per-draw figures should be byte-identical to A.19.9 both before and after this segment's
Design C removal collateral fix to `measure_replicate_noise.py`. Re-running confirms exactly that:
production=9/16 (56.2%, MAE 0.688), replicate1=11/16 (68.8%, MAE 0.375), replicate2=10/16 (62.5%, MAE
0.438) — identical to A.19.9 to the decimal, serving as a regression check that the Design-C-removal
fixes changed no behavior. Bonus figure not computed in A.19.9: pooled across **both splits**, all 3
draws: n=120 draw-observations, 82/120 (68.3%) agreement, MAE 0.442.

### A.21.4 Statistical test reference: what each test asks, and how to read the result

Written for a critical reader auditing A.21.1-A.21.3 who wants to know exactly what was tested, not
just the p-values. Every test below is **paired** — the same 16 TEST articles compared under two
conditions (`run33/ep81` vs. one guarded-constant baseline) — which matters because a paired design
uses each article as its own control and is markedly more powerful, at this sample size, than an
unpaired test would be; it is also the only design not confounded by which particular 16 articles
happen to be in the TEST split.

1. **McNemar's exact test (A.21.1).** *Asks:* when two paired classifiers are each scored right/wrong
   against the same ground truth, does one disagree with the other more often in its own favor than
   chance would predict? *Mechanics:* only the discordant pairs matter — `b` = model right/baseline
   wrong, `c` = model wrong/baseline right; concordant pairs (both right or both wrong) carry no
   information about *which* is better and are correctly dropped from the test statistic (though they
   still count in `n_articles=16`, just not in `n=b+c`). *Null hypothesis:* `b` and `c` are draws from
   Binomial(`b+c`, 0.5) — i.e., disagreements are coin flips with no directional preference. *p-value:*
   one-sided, `P(X <= c | X ~ Binomial(b+c, 0.5))` — the chance of seeing a baseline-favoring count `c`
   this low or lower if there were really no asymmetry. *Caveat:* power depends only on `n=b+c`
   (4-13 here across the four baselines), which is why A.21.2 cross-checks with two more independent
   methods rather than resting on McNemar alone.

2. **Wilcoxon signed-rank test, exact (A.21.2).** *Asks:* is the **median** of the paired per-article
   difference (ordinal-distance reduction, or regret reduction) greater than zero, using the *ranks* of
   the absolute differences — so a large win counts for more than a narrow one, unlike McNemar which
   only uses the sign. *Mechanics:* exact zero-differences are dropped per convention (reducing `n` to
   5-6 here); ties among remaining absolute differences get averaged ranks; the exact (not
   normal-approximation) one-sided p-value is computed by enumerating all `2^m` sign-flip assignments of
   the observed ranks — feasible and preferred here specifically because `m<=6` is small enough to
   enumerate exhaustively rather than lean on a large-sample approximation whose assumptions wouldn't
   hold at this `n`.

3. **Sign-flip permutation test, exact (A.21.2).** *Asks:* nearly the same question as Wilcoxon, but on
   the **raw** differences rather than their within-sample ranks — is the **mean** of the paired
   differences greater than zero, under the null that each nonzero difference's sign is an independent
   coin flip. *Mechanics:* same exhaustive `2^m` enumeration as Wilcoxon, but summing raw values instead
   of ranks. Being a permutation test, it makes no distributional assumption beyond exchangeability of
   signs under the null (no normality, no symmetry) — the least assumption-laden test in this reference,
   included specifically so the Wilcoxon result isn't resting on rank-transformation alone.

4. **Paired bootstrap, B=100,000 (A.21.2).** *Asks:* is the **mean** paired difference, estimated over
   the **full** n=16/15 sample (not just the discordant/nonzero subset the three tests above reduce to),
   distinguishable from zero? *Mechanics:* resample all paired differences with replacement 100,000
   times, take the mean of each resample, and read off the empirical 2.5th/97.5th percentiles as a 95%
   CI; the one-sided p is the fraction of resampled means `<= 0`. *Why it matters here:* it is the only
   test that keeps every tied (zero-difference) article's real information rather than discarding it,
   which is exactly why it is the highest-powered test in this set (tightest CIs, smallest p-values) —
   at the cost of relying on the bootstrap resampling distribution as a stand-in for the true sampling
   distribution, a standard and normally mild assumption at this `n`.

5. **Noise-ceiling baseline (A.21.3 / A.19.9).** *Not* a significance test — a contextualizing
   benchmark. *Asks:* how often would even a perfect single-draw oracle already disagree with the
   (three-draw-averaged) ground truth, purely from measurement noise, with no model or baseline
   comparison involved on either side? *How to read it:* compare `run33/ep81`'s own raw accuracy
   directly against this figure (not against any p-value) to gauge how much headroom the corpus itself
   can even support — it is the check against overclaiming: no combination of favorable results from
   tests 1-4 should be read as implying more real-world headroom than this noise floor allows.

**Why five different methods for one underlying comparison?** Each covers a different failure mode of
the others, deliberately: McNemar/Wilcoxon/sign-flip all discard the majority-concordant or tied
articles and can under-power a real effect when discordant pairs are few (exactly what A.19.7's
original `p=0.0625` reflected); the bootstrap recovers power by using the full sample and full
magnitude, but rests on different assumptions than the sign-based family, so agreement **across both
families** (as seen here — all four now significant) is materially stronger evidence than any one test
in isolation; the noise ceiling caps the entire exercise so favorable significance results can never be
misread as claiming a bigger real-world effect than the corpus's own measurement noise permits.









