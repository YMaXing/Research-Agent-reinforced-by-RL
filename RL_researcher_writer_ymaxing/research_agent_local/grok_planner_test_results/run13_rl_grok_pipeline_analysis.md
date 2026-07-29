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




