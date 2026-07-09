# RL + Grok 4.2 Planner Train & Test Results

## Summary — TEST split (held-out, primary metric), n=16

| # | Article | RL | Grok | Chosen | → Oracle | Verdict |
|---|---|---|---|---|---|---|
| 1 | 04_structured_outputs | P1 | P1 | P1 | P2 | ~ NEAR |
| 2 | 07_reasoning_planning | P0 | P0 | P0 | P0 | ✓ EXACT |
| 3 | 13_agent_framework | P0 | P1 | P1 | P3 | ✗ MISS |
| 4 | 14_agent_system_design | P1 | P1 | P1 | P1 | ✓ EXACT |
| 5 | 29_evaluation_metrics | P0 | P1 | P1 | P1 | ✓ EXACT |
| 6 | 31_CI | P0 | P0 | P0 | P1 | ~ NEAR |
| 7 | Bird_Eye_Extreme | P0 | P0 | P0 | P1 | ~ NEAR |
| 8 | Dark_Dimension | P0 | P0 | P0 | P0 | ✓ EXACT |
| 9 | Distinct_AI_Models | P0 | P1 | P1 | P1 | ✓ EXACT |
| 10 | Earth_Oceans_Origin | P1 | P2 | P2 | P3 | ~ NEAR |
| 11 | Gravity_Entropy | P1 | P1 | P1 | P1 | ✓ EXACT |
| 12 | HNSW | P0 | P1 | P1 | P1 | ✓ EXACT |
| 13 | Insects_Consciousness | P0 | P1 | P1 | P1 | ✓ EXACT |
| 14 | Space-Time_QECC | P0 | P0 | P0 | P1 | ~ NEAR |
| 15 | State_of_LLM_Reasoning (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 16 | Understanding_Reasoning_LLMs | P0 | P0 | P0 | P2 | ✗ MISS |

**Overall:** n=16 · exact=9 (56%) · near=5 (31%) · miss=2 (12%) · no-oracle/error=0
**Ordinal MAE:** 0.562
**Reward-regret** (allowed/required only, n=15; 1 forbidden excluded): mean=0.0420, max=0.2351

### Confusion matrix

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 3 | 0 | 0 | 0 | 3 |
| P1 light | 3 | 6 | 0 | 0 | 9 |
| P2 standard | 1 | 1 | 0 | 0 | 2 |
| P3 deep | 0 | 1 | 1 | 0 | 2 |

### Baselines

- Oracle distribution: P0=3, P1=9, P2=2, P3=2
- Majority-class baseline (always P1 light): 56.2% (9/16)
- Uniform-random baseline (1/4): 25.0%
- Weighted-random baseline: 38.3%

---

## Summary — TRAIN split (reference), n=24

| # | Article | RL | Grok | Chosen | → Oracle | Verdict |
|---|---|---|---|---|---|---|
| 1 | 02_workflows_vs_agents__var_minimal (forbidden) | P1 | P0 | P0 | P0 | ✓ EXACT |
| 2 | 02_workflows_vs_agents__var_standard | P1 | P1 | P1 | P1 | ✓ EXACT |
| 3 | 02_workflows_vs_agents__var_demanding | P2 | P2 | P2 | P1 | ~ NEAR |
| 4 | 03_context_engineering__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 5 | 03_context_engineering__var_standard | P1 | P1 | P1 | P0 | ~ NEAR |
| 6 | 03_context_engineering__var_demanding (required) | P1 | P1 | P1 | P1 | ✓ EXACT |
| 7 | 05_workflow_patterns__var_minimal (forbidden) | P1 | P0 | P0 | P0 | ✓ EXACT |
| 8 | 05_workflow_patterns__var_standard | P2 | P2 | P2 | P1 | ~ NEAR |
| 9 | 05_workflow_patterns__var_demanding (required) | P1 | P1 | P1 | P1 | ✓ EXACT |
| 10 | 06_tools__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 11 | 06_tools__var_standard | P0 | P0 | P0 | P0 | ✓ EXACT |
| 12 | 06_tools__var_demanding (required) | P3 | P3 | P3 | P3 | ✓ EXACT |
| 13 | 08_react_practice__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 14 | 08_react_practice__var_standard | P0 | P1 | P1 | P1 | ✓ EXACT |
| 15 | 08_react_practice__var_demanding (required) | P2 | P2 | P2 | P2 | ✓ EXACT |
| 16 | 09_RAG__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 17 | 09_RAG__var_standard | P0 | P0 | P0 | P1 | ~ NEAR |
| 18 | 09_RAG__var_demanding | P3 | P3 | P3 | P3 | ✓ EXACT |
| 19 | 10_memory_knowledge_access__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 20 | 10_memory_knowledge_access__var_standard | P1 | P1 | P1 | P1 | ✓ EXACT |
| 21 | 10_memory_knowledge_access__var_demanding (required) | P2 | P2 | P2 | P2 | ✓ EXACT |
| 22 | 11_multimodal__var_minimal (forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 23 | 11_multimodal__var_standard | P1 | P1 | P1 | P1 | ✓ EXACT |
| 24 | 11_multimodal__var_demanding (required) | P2 | P3 | P3 | P2 | ~ NEAR |

**Overall:** n=24 · exact=19 (79%) · near=5 (21%) · miss=0 (0%) · no-oracle/error=0
**Ordinal MAE:** 0.208
**Reward-regret** (allowed/required only, n=16; 8 forbidden excluded): mean=0.0137, max=0.0992

### Confusion matrix (Train)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 9 | 1 | 0 | 0 | 10 |
| P1 light | 1 | 6 | 2 | 0 | 9 |
| P2 standard | 0 | 0 | 2 | 1 | 3 |
| P3 deep | 0 | 0 | 0 | 2 | 2 |

### Baselines (Train)

- Oracle distribution: P0=10, P1=9, P2=3, P3=2
- Majority-class baseline (always P0 skip): 41.7% (10/24)
- Uniform-random baseline (1/4): 25.0%
- Weighted-random baseline: 33.7%

### By difficulty tier (Train)

| Variant tier | n | Exact | Exact+Near | Regret (mean / max) |
|---|---|---|---|---|
| var_minimal | 8 | 8/8 | 8/8 | n/a (all policy-forced) |
| var_standard | 8 | 5/8 | 8/8 | mean=0.0203, max=0.0992 |
| var_demanding | 8 | 6/8 | 8/8 | mean=0.0070, max=0.0601 |

---

## Combined — Train + Test (n=40)

- n=40 · exact=28 (70%) · near=10 (25%) · miss=2 (5%) · no-oracle/error=0
- Reward-regret (allowed/required only, n=31; 9 forbidden excluded): mean=0.0274, max=0.2351

---

## Per-variant details

Each entry below expands one row of the summary table with the underlying scorer signal, Grok 4.2's reasoning, and any override rationale.

### 1. 04_structured_outputs — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.6067 / 0.6687 / 0.6707 / 0.6407 |
| Regret (counted) | 0.002 (0.002) |
| Entropy | 0.9968 bits |
| Confidence | 0.533 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate scorer vote is P1 light (53% light / 47% skip, MODERATE confidence); budget-weighted section votes identically 53% light with 0% standard and 0% deep, so both escalation gates (≥30%) are closed. Largest-budget section (S4 40%) voted light while high-must-ev sections (S3/S4 total 33 must-ev) already pulled the RL pick upward from pure skip; no brief-flagged or well-covered majority justifies downward override to P0.

**Decision drivers:** scorer_aggregate · budget_vote_mass · zero_escalation_mass

**Risk flags:**
- moderate (not decisive) confidence
- high must-ev in S3/S4 could still be under-covered

### 2. 07_reasoning_planning — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.2886 / 0.2008 / 0.1839 / 0.1268 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.4413 bits |
| Confidence | 0.5505 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P0 (55% skip, moderate confidence, not decisive). Budget-weighted section mass is skip 55% / light 21% / standard 0% / deep 24%; standard mass <<30% and deep mass <30% so no sanctioned escalation applies and the deep-or-nothing guard instructs staying put rather than entering the P2 valley. Light mass 21% falls short of the >=25% threshold for a P0->P1 nudge. Raw gaps (42 unbacked anchors, must-ev in S1/S4/S5/S8, low cov in S1/S4) are ignored per instructions; level is set solely by calibrated vote mass.

**Decision drivers:** scorer_aggregate_P0 · vote_mass_below_escalation_gates · no_P0->P1_nudge

**Risk flags:**
- S7_24pct_budget_votes_deep
- S4_14pct_light_with_3_must_ev_8_orphans
- moderate_not_decisive_confidence

### 3. 13_agent_framework — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.6446 / 0.6716 / 0.5805 / 0.6939 |
| Regret (counted) | 0.0223 (0.0223) |
| Entropy | 1.3375 bits |
| Confidence | 0.5336 |
| Floor applied | yes |
| Grok override | **yes** |

**Reasoning:** Aggregate RL vote is P0 skip (53% soft / 55% budget-weighted) but only moderate confidence (not decisive). Light holds 36-37% vote mass (>=25% runner-up threshold) while standard=0% and deep=9% both sit far below 30% escalation gates; this exactly triggers the sanctioned P0→P1 nudge. High-gap intro sections (S1 28/6 need, cov 1·0; S2 26/6, cov 3·0) plus S4 (18% budget, 15 must-ev, 7 orphans) dominate the light votes, making one balanced round cheap insurance against unbacked anchors without crossing into the standard-vote <30% reward valley.

**Override reason:** applied sanctioned P0→P1 nudge per policy (light mass >=25%, no standard/deep mass >=30%)

**Decision drivers:** moderate-confidence aggregate · 36% light vote mass · P0-to-P1 nudge rule · S1/S2/S4 gap profile

**Risk flags:**
- light round may yield mostly duplicate golden-source data
- S4's 15 must-ev could still need one deeper metric refresh

### 4. 14_agent_system_design — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.5938 / 0.6859 / 0.5966 / 0.5837 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.5305 bits |
| Confidence | 0.4379 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P1 light (44% light mass, 34% skip, 22% deep) but UNCERTAIN (entropy 1.53). Standard-vote mass is 0% and deep-vote mass is 22%, both below the 30% escalation gate, so no sanctioned upward move to P2; the explicit guard against stepping into the P2 valley when deep votes dominate without standard support applies directly. High-budget sections (S2 31% skip, S4 28% light, S3 22% deep) are mixed yet the budget-weighted peak remains at light; raw must-ev/unbacked counts were ignored per instructions. This places the decision at the reward peak without over- or under-escalation.

**Decision drivers:** budget-weighted vote mass peaking at light · escalation gates not met (0%/22%<30%) · UNCERTAIN but no dominant escalation arm

**Risk flags:**
- S3 deep vote + high need_depth could justify more depth
- dominant gap type is depth across large-budget S2/S4

### 5. 29_evaluation_metrics — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.5118 / 0.7876 / 0.7138 / 0.685 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.3424 bits |
| Confidence | 0.4559 |
| Floor applied | yes |
| Grok override | **yes** |

**Reasoning:** Aggregate RL vote is P0 skip but tied 46/46 with light (MODERATE, not decisive = UNCERTAIN). Budget-weighted section mass exactly matches (skip 46%, light 46%, standard 0%, deep 9%); standard and deep masses both <<30% so no sanctioned upward escalation. Sanctioned P0→P1 nudge applies directly (runner-up light mass 46%≥25%, no higher vote concentration). Must-ev counts in S3/S4/S5 plus 47 unbacked anchors justify cheap insurance without violating S2's 'brief' flag or large-section skip vote.

**Override reason:** applied sanctioned P0-to-P1 nudge on tied uncertain vote with light mass ≥25% and no escalation signal above 30%

**Decision drivers:** tied moderate aggregate vote · P0→P1 nudge criteria met · budget-weighted section mass · must-ev in mid-budget sections

**Risk flags:**
- S2 (35% budget) voted skip and is brief-flagged
- dominant gaps are depth but preset is breadth-balanced

### 6. 31_CI — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.6284 / 0.6901 / 0.5939 / 0.6053 |
| Regret (counted) | 0.0617 (0.0617) |
| Entropy | -0.0 bits |
| Confidence | 1.0 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P0 skip at 100% (DECISIVE, entropy=0). All 9 sections, including high-budget S6 (31%), S5 (17%) and must-ev-heavy S2/S5/S6, vote skip·1.00 with zero mass on light/standard/deep. No escalation gates met (std=0%, deep=0% <<30%); external-evidence=ALLOWED not required. Do not escalate on raw gaps (42 unbacked anchors, depth-dominant).

**Decision drivers:** decisive_100pct_skip_vote · zero_escalation_mass · no_hard_constraint

**Risk flags:**
- high must-ev in S5/S6 could still need sourcing
- S6 1350-word length might hide qualitative gaps

### 7. Bird_Eye_Extreme — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4915 / 0.7266 / 0.5656 / 0.4522 |
| Regret (counted) | 0.2351 (0.2351) |
| Entropy | 0.7121 bits |
| Confidence | 0.8049 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is decisive P0 (80% skip, 0% standard, 0% deep) with identical budget-weighted section-vote mass; all escalation gates (standard-mass ≥30%, deep-mass ≥30%) are at 0% and light runner-up is only 20% (below 25% nudge threshold). Per-section RL picks are uniformly skip (except S1 light·1.00) despite must-ev and orphan counts, confirming the learned reward peak sits at no exploration. External-evidence policy is only ALLOWED, not required, so gaps do not override the calibrated signal.

**Decision drivers:** decisive_scorer_P0 · zero_escalation_mass · budget_vote_alignment

**Risk flags:**
- 31 unbacked anchors
- S3 must-ev=6 and high need-depth

### 8. Dark_Dimension — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.814 / 0.6803 / 0.6923 / 0.6287 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | -0.0 bits |
| Confidence | 1.0 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate scorer vote is P0 skip at 100% (DECISIVE, entropy=0). All three sections independently vote skip·1.00 with 100% budget-weighted mass on skip; standard- and deep-vote masses are both 0% so no sanctioned escalation applies. Two of three sections carry explicit 'brief' flags that prohibit absorbing extra research; external-evidence policy is only ALLOWED, not required. Raw must-ev/orphan counts are ignored per instructions when the learned signal is this decisive.

**Decision drivers:** decisive scorer vote · zero escalation mass · section brief flags

**Risk flags:**
- all cov_breadth=0
- high must-ev in S3 (46% budget)

### 9. Distinct_AI_Models — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.625 / 0.7917 / 0.6398 / 0.7135 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.971 bits |
| Confidence | 0.6 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Section-scorer aggregate is P0 skip (60% mass, 40% light runner-up) but only moderate confidence and therefore uncertain. Budget-weighted section votes exactly track this split (S1+S2 60% skip; S3+S4 40% light), with zero standard or deep mass, so no sanctioned escalation to P2. Sanctioned P0→P1 nudge applies directly (light mass ≥25%, higher-preset masses <30%). Decisive signals are the 30 unbacked anchors + must-ev counts (3–4 per section) plus dominant depth gaps that the light sections themselves voted to address.

**Override reason:** Sanctioned P0→P1 nudge triggered by substantial light mass (>=25%) and absence of standard/deep votes

**Decision drivers:** scorer uncertainty + 40% light mass · sanctioned P0-to-P1 nudge · must-ev and orphan counts

**Risk flags:**
- brief=yes flags on S1/S3 could limit absorption of new evidence
- possible overlap with already-provided golden sources

### 10. Earth_Oceans_Origin — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.4707 / 0.5086 / 0.5917 / 0.6133 |
| Regret (counted) | 0.0216 (0.0216) |
| Entropy | 0.9367 bits |
| Confidence | 0.6471 |
| Floor applied | yes |
| Grok override | **yes** |

**Reasoning:** Aggregate RL vote is P1 light at moderate 65% confidence (uncertain) with exactly 35% budget-weighted standard mass. This meets the sanctioned-upward-escalation rule (RL pick=P1 + uncertain + standard-vote mass≥30%). S3 (35% budget, RL=standard·1.00, must-ev=5, need_depth=2) plus 38 article-wide unbacked anchors and dominant breadth gaps supply the concrete justification; no deep mass so P2 is the calibrated peak.

**Override reason:** sanctioned escalation from uncertain P1 to P2 because standard-vote mass=35% clears 30% threshold

**Decision drivers:** uncertain aggregate (65%) · standard-vote mass=35% · S3 must-ev=5 + need_depth=2

**Risk flags:**
- possible diminishing returns on breadth if cov_b=3 already suffices
- S2 (37%) voted light so extra round may add redundancy

### 11. Gravity_Entropy — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.646 / 0.7228 / 0.6604 / 0.5609 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.9815 bits |
| Confidence | 0.58 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P1 light (58% light / 42% skip mass, moderate confidence, UNCERTAIN). Budget-weighted section votes show 0% mass on standard or deep (far below 30% escalation gate), so no sanctioned upward move; raw gaps (32 unbacked anchors, must-ev totals) are ignored per policy. Multiple high-budget sections are already at cov ≥7·4 or brief-flagged, aligning with light touch-up rather than P0 or P2.

**Decision drivers:** scorer_aggregate_P1 · zero_escalation_mass · brief_flags_on_S2_S3

**Risk flags:**
- moderate scorer confidence (58%)
- depth-dominant gaps in S2/S5

### 12. HNSW — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4839 / 0.7672 / 0.5239 / 0.5556 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.996 bits |
| Confidence | 0.5373 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Aggregate RL vote is P0 skip (54% mass, moderate confidence, not decisive). Budget-weighted section votes show 46% light (driven by S4's 46% share voting light·1.00 with must-ev=9, orphans=12, cov=4·3). Standard- and deep-vote masses are 0% so no sanctioned escalation to P2/P3; P0→P1 nudge applies directly (light runner-up ≥25%, no higher masses). This supplies cheap insurance for dominant depth gaps and 47 unbacked anchors without entering reward valley.

**Override reason:** Sanctioned P0→P1 nudge triggered by 46% light mass + uncertain scorer (no std/deep mass ≥30%)

**Decision drivers:** RL uncertainty + light mass · S4 must-ev/orphans · P0-to-P1 nudge policy

**Risk flags:**
- Existing cov already moderate (esp. S1/S3); light round could still duplicate material
- Depth-dominant gaps in S2/S4 might need more but 0% std vote bars P2

### 13. Insects_Consciousness — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.5434 / 0.8553 / 0.5461 / 0.7229 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.9 bits |
| Confidence | 0.684 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Scorer aggregate is P0 skip (68% mass, 32% light) and is UNCERTAIN (moderate confidence <70%). Budget-weighted votes show exactly the P0->P1 nudge conditions: light mass 32% (>=25%), standard-mass 0% and deep-mass 0% (both <30%). Per-section table shows consistent must-ev (4-6 per section), 22 article-wide unbacked anchors, and dominant depth gaps even in high-budget S2/S3 despite their skip votes; P1 supplies cheap insurance without crossing into the P2 valley.

**Override reason:** applied sanctioned P0->P1 nudge per policy (light runner-up >=25% with no higher-preset mass)

**Decision drivers:** P0->P1 nudge · light-vote mass 32% · must-ev + orphan counts

**Risk flags:**
- existing golden sources may already cover many must-ev
- could be marginal gain if cov d·b already meets minimal guideline

### 14. Space-Time_QECC — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.462 / 0.602 / 0.5076 / 0.5188 |
| Regret (counted) | 0.14 (0.14) |
| Entropy | 0.6343 bits |
| Confidence | 0.84 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL vote is decisive P0 skip at 84% budget-weighted mass (soft votes: skip 84%, deep 16%, light/standard 0%). Deep-vote mass from S2 (16% budget, high-need but only one section) sits below the 30% sanctioned-escalation gate; decisive vote forbids upward moves per override policy. Article-wide must-ev/unbacked anchors exist but instructions prohibit escalating on raw gap counts; external-evidence policy is only ALLOWED, not required.

**Decision drivers:** decisive P0 aggregate · deep-mass <30% · no escalation gate met

**Risk flags:**
- S2 zero coverage + deep vote
- 27 unbacked anchors

### 15. State_of_LLM_Reasoning — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.449 / 0.4057 / 0.4243 / 0.3653 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 1.1204 bits |
| Confidence | 0.7143 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** HARD CONSTRAINT: external-evidence policy=forbidden mandates P0; scorer aggregate is decisive P0 (71% skip, 69% budget-weighted) with zero standard-mass and only 13% deep-mass (no escalation possible)

**Decision drivers:** hard_constraint_forbidden · decisive_scorer_vote

**Risk flags:**
- none

### 16. Understanding_Reasoning_LLMs — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.4603 / 0.5987 / 0.6078 / 0.527 |
| Regret (counted) | 0.1475 (0.1475) |
| Entropy | 0.4071 bits |
| Confidence | 0.9186 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P0 skip at 92% (DECISIVE, entropy near-zero). Budget-weighted mass is 92% skip / 8% deep (S6 only); standard-mass=0% and deep-mass=8% both <<30% escalation gate. No P0→P1 nudge (light mass=0%). High must-ev/unbacked counts and zero coverage scores exist but instructions forbid escalating on raw gaps when scorer is decisive; external-evidence policy only ALLOWS, does not require.

**Decision drivers:** decisive_scorer_aggregate · low_preset_specific_vote_mass · no_sanctioned_escalation

**Risk flags:**
- S5 (45% budget) and S7 show 8/5 must-ev yet scorer still picked skip
- all sections at cov 0·0 after exploitation pass


### Train split (n=24)

#### 17. 02_workflows_vs_agents__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P1 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.4962 / 0.6931 / 0.45 / 0.475 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 1.543 bits |
| Confidence | 0.4231 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Hard constraint: external-evidence policy=FORBIDDEN explicitly requires P0 skip (exploration output cannot be used). Scorer aggregate is P1 light (UNCERTAIN, entropy 1.54 bits; budget-weighted votes: light 42%, skip 35%, standard 23%, deep 0%) but override policy mandates P0 when evidence is forbidden. All 'must stay brief' flags, surface-level conceptual scope, and explicit bans on external examples reinforce no exploration needed.

**Override reason:** Hard constraint forces P0 despite scorer's P1 light recommendation

**Decision drivers:** external-evidence-forbidden · hard-constraint · brevity-flags

**Risk flags:**
- scorer uncertainty could miss minor internal gaps
- guideline cites sources but policy forbids using them

#### 18. 02_workflows_vs_agents__var_standard — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.6292 / 0.794 / 0.7335 / 0.51 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.3513 bits |
| Confidence | 0.5849 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL pick is P1 light at 58% budget-weighted mass (MODERATE confidence). Standard-vote mass=29% falls short of the 30% gate for sanctioned escalation to P2; deep mass=13% is far below. High-budget S5 (light vote, cov 8·6) plus brief flags on S1/S4 lock in the peak without override.

**Decision drivers:** RL aggregate vote · standard-mass <30% gate · high-budget section alignment

**Risk flags:**
- S2/S3 depth gaps could be understated if guideline examples require fresher 2025 sources
- moderate scorer confidence on hybrid-spectrum article

#### 19. 02_workflows_vs_agents__var_demanding — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P2 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4835 / 0.5722 / 0.5121 / 0.4478 |
| Regret (counted) | 0.0601 (0.0601) |
| Entropy | 1.4988 bits |
| Confidence | 0.4943 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P2 standard (49% budget-weighted mass on standard, exceeding 30% gate; 0% deep). Vote is moderate/uncertain (not >=70% decisive) but per-section table shows high-budget S2/S3/S4 (49% combined) voting standard with must-ev 2-3, depth gaps (need_d 6-7), and unbacked anchors; S5's skip (29%, cov 8·6) is outweighed. No sanctioned escalation to P3 (deep mass=0) or downward override (dominant standard arm, multiple must-ev). Dominant gap=depth, external policy=allowed.

**Decision drivers:** aggregate RL pick P2 + 49% standard mass · must-ev and depth gaps in S2-S4/S6 · no deep mass for P3

**Risk flags:**
- S5 large skip vote may make extra rounds duplicative
- many must-ev could still need targeted depth if sources thin

#### 20. 03_context_engineering__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.7625 / 0.7783 / 0.6314 / 0.7269 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.8967 bits |
| Confidence | 0.6908 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** HARD CONSTRAINT: external-evidence policy=FORBIDDEN explicitly requires P0 skip (exploration output cannot be used). Scorer aggregate is also P0 (69% skip, 72% budget-weighted skip mass); standard- and deep-vote masses are 0% so no sanctioned escalation applies. Every section is flagged 'brief: yes' and the guideline demands only surface-level conceptual treatment with no external examples or code.

**Decision drivers:** external-evidence-forbidden · scorer-P0 · all-sections-brief

**Risk flags:**
- moderate scorer confidence
- many unbacked anchors but policy forbids using exploration to fill them

#### 21. 03_context_engineering__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6414 / 0.6119 / 0.5843 / 0.5143 |
| Regret (counted) | 0.0295 (0.0295) |
| Entropy | 0.9967 bits |
| Confidence | 0.5339 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P1 light (53% soft vote, 51% budget-weighted) but UNCERTAIN (moderate confidence, near-tie with 49% skip, 0% standard/deep). No sanctioned escalation (standard-vote mass=0% <<30%). Several high-budget sections (S6 20%, S4 15%, S7 15%) show high must-ev (6/3), depth needs (55/33/55) and orphans (18/10/18) despite decent cov; dominant article gap is depth. P1 matches the reward peak without inflating to unsupported P2.

**Decision drivers:** scorer aggregate P1 (51% budget mass) · zero escalation mass for standard/deep · high must-ev + depth gaps in S6/S7/S4

**Risk flags:**
- close 51-49 split could justify P0 downward
- many sections already at cov_d >=6

#### 22. 03_context_engineering__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4295 / 0.5055 / 0.477 / 0.4368 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.1811 bits |
| Confidence | 0.6766 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL vote P1 light (68% mass, standard mass only 23%); escalation gate requires standard-vote mass >=30% when uncertain, which is not met; external-evidence=REQUIRED forbids P0 while high must-ev/depth gaps (esp. S6 11, S4 6) were already factored into the budget-weighted scorer votes.

**Decision drivers:** scorer_aggregate · vote_mass_below_30pct · external_policy_floor

**Risk flags:**
- moderate (68%) confidence
- S3/S8 standard votes totaling 23%

#### 23. 05_workflow_patterns__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P1 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.872 / 0.8408 / 0.796 / 0.746 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.9912 bits |
| Confidence | 0.5552 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Hard constraint: external-evidence policy=FORBIDDEN mandates P0 skip (exploration output cannot be used). Scorer aggregate is moderate P1 (56% light, 44% skip; 0% standard/deep) but OVERRIDE POLICY and HARD CONSTRAINTS require ignoring it. All sections flagged 'brief', guideline demands surface-level conceptual overview with no external libs/cases/benchmarks.

**Override reason:** external-evidence policy explicitly FORBIDDEN, forcing P0 regardless of scorer or gap counts

**Decision drivers:** hard-constraint-forbidden · all-sections-brief · 0% std/deep mass

**Risk flags:**
- many unbacked anchors (52) and must-ev items cannot be filled

#### 24. 05_workflow_patterns__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P2 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.6149 / 0.8085 / 0.7092 / 0.7192 |
| Regret (counted) | 0.0992 (0.0992) |
| Entropy | 1.3697 bits |
| Confidence | 0.4872 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate RL pick is P2 (49% standard-vote mass >30% gate); uncertain but no qualifying escalation (deep mass only 10%) or downward (dominant arm, depth-dominant gaps, no briefs). Matches weakest-section needs without overbuying on already-covered cov.

**Decision drivers:** aggregate RL pick · standard-vote mass >=30% · dominant gap type

**Risk flags:**
- moderate scorer entropy could undervalue S2 deep vote
- high unbacked anchors but instructions forbid raw-gap escalation

#### 25. 05_workflow_patterns__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.5417 / 0.6549 / -0.06 / 0.4766 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.4516 bits |
| Confidence | 0.4805 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Scorer aggregate is P1 light (48% budget-weighted mass on light, moderate confidence); standard-vote mass=0% while deep-vote mass=37% triggers the explicit deep-or-nothing guard that forbids stepping into the P2 valley from a P1 RL pick. External-evidence policy requires at least P1, which this satisfies exactly; per-section RL picks show mixed skip/light/deep but the calibrated vote-mass signal (not raw must-ev or 42 unbacked anchors) determines level. Dominant gap is depth yet escalation policy bars upward move.

**Decision drivers:** scorer_aggregate_P1 · deep_or_nothing_guard · external_evidence_required · standard_vote_mass_0

**Risk flags:**
- 37% deep mass in S2/S5/S7 could leave theory depth gaps
- high must-ev counts across S1/S2/S7

#### 26. 06_tools__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6903 / 0.6818 / 0.557 / 0.3205 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.9643 bits |
| Confidence | 0.6107 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, mandating P0 skip per hard constraints. Scorer aggregate is also P0 (61% skip, 0% standard/deep mass); all sections flagged 'brief' or surface-level only; guideline forbids external libs/case studies/benchmarks.

**Decision drivers:** forbidden-policy · scorer-P0-vote · brevity-flags

**Risk flags:**
- none

#### 27. 06_tools__var_standard — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.5598 / 0.4525 / 0.5707 / 0.5184 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.6098 bits |
| Confidence | 0.5864 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P0 skip (59% mass) despite uncertainty (entropy 1.61). Standard mass=18% and deep mass=9% both <<30% escalation gate, so no sanctioned upward move per override policy. Largest section (S3, 26% budget) voted skip·1.00 with brief=yes (must stay short); do not escalate on raw must-ev/orphans counts.

**Decision drivers:** aggregate RL vote · escalation masses below 30% · S3 brief flag

**Risk flags:**
- high must-ev in S3/S4 could leave unsourced claims
- uncertain scorer on code-heavy article

#### 28. 06_tools__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P3 |
| Grok preset | P3 |
| Chosen preset (by Grok4.2) | P3 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.3794 / 0.4551 / 0.4288 / 0.4949 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.9158 bits |
| Confidence | 0.3829 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Aggregate RL pick is P3 deep (38% deep-vote mass) on an uncertain scorer (entropy 1.92). Deep mass clears the 30% bar while standard mass (26%) does not; high-budget sections S3 (24%, deep·1.00, need_depth 8) and S8 (11%, deep·1.00, must-ev=4, cov 5·4) drive the peak. External-evidence=REQUIRED and depth-dominant article gaps (42 unbacked anchors) align with P3; no sanctioned downward override applies as deep mass dominates and several sections remain under-covered on must-ev items.

**Decision drivers:** P3 aggregate on uncertain scorer · 38% deep-vote mass from S3+S8 · must-ev=4 in S8 and depth-dominant gaps · REQUIRED external-evidence policy

**Risk flags:**
- scorer entropy >1.5 could over-weight S3/S8 at expense of well-covered S5/S7
- diminishing returns on already cov-7 sections if depth rounds add duplicates

#### 29. 08_react_practice__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6543 / 0.1224 / 0.0647 / 0.3828 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.8727 bits |
| Confidence | 0.7069 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, mandating P0. Scorer aggregate is decisive P0 skip (71% budget-weighted vote mass); standard- and deep-vote masses are both 0% so no sanctioned escalation applies. All sections are brief-flagged and guideline demands surface-level treatment with no external examples allowed.

**Decision drivers:** forbidden-evidence-policy · decisive-P0-vote · brief-flags-on-all-sections

**Risk flags:**
- none - hard constraint aligns with scorer

#### 30. 08_react_practice__var_standard — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.3892 / 0.5431 / 0.259 / 0.3283 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.9997 bits |
| Confidence | 0.5108 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Aggregate P0 (51% skip) is uncertain with 49% light runner-up from high-budget S4/S5 (both RL-pick light, 49% total mass). This triggers the exact sanctioned P0->P1 nudge (>=25% light, 0% standard/deep mass). Balanced gaps and must-ev already baked into per-section votes; S5 brief flag caps absorption.

**Override reason:** applied sanctioned P0->P1 nudge per policy (runner-up light mass 49% >=25%, no higher votes)

**Decision drivers:** budget-weighted vote mass · P0->P1 nudge eligibility · S4/S5 light picks

**Risk flags:**
- S5 brief=yes may dilute light round value
- close 51-49 split could still peak at P0

#### 31. 08_react_practice__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P2 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.4094 / 0.4042 / 0.5843 / 0.4348 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.3509 bits |
| Confidence | 0.4598 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P2 standard (46% standard-vote mass >30% gate) on an UNCERTAIN but non-decisive vote (46% top-pick, 45% skip). Largest-budget section S5 (28%) and S4 (18%) both vote standard with high need_depth (22/13); external-evidence policy forbids P0 and dominant gap type is depth. No sanctioned upward move (deep mass=0%) and no downward override trigger (standard mass dominant, not all high-budget sections brief-flagged).

**Decision drivers:** scorer_aggregate_P2 · standard_vote_mass_46pct · S5_28pct_standard_need_depth_22 · required_external_evidence

**Risk flags:**
- near-tie skip_vote_45pct
- brief_yes_on_largest_S5
- many_unbacked_anchors_42

#### 32. 09_RAG__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.7317 / 0.5683 / 0.4467 / 0.3627 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.9588 bits |
| Confidence | 0.6318 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, which hard-constrains to P0; section-scorer aggregate is also P0 skip (63% budget-weighted mass, 0% standard/deep); every section is brief-flagged with surface-level guideline intent and a 1500-word hard cap.

**Decision drivers:** hard-forbidden-policy · scorer-P0-vote · all-sections-brief

**Risk flags:**
- moderate scorer confidence (63%)
- high unbacked anchors (42) but irrelevant under policy

#### 33. 09_RAG__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4057 / 0.4394 / 0.4255 / 0.3807 |
| Regret (counted) | 0.0338 (0.0338) |
| Entropy | 1.4649 bits |
| Confidence | 0.5217 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Section-scorer aggregate is P0 skip (52% mass, MODERATE/UNCERTAIN). Budget-weighted standard-vote mass sits at 29% (explicitly flagged as below the 30% bar) and deep-vote mass is 0%; light mass is only 19% so the P0→P1 nudge also fails. No sanctioned escalation or downward override applies. Decisive signals are therefore the RL aggregate itself plus the exact escalation-gate numbers that keep us at skip.

**Decision drivers:** scorer-aggregate-P0 · standard-mass-29pct-below-gate · no-nudge-conditions-met

**Risk flags:**
- S4 (29% budget) voted standard with 6 must-ev
- 48 unbacked anchors but policy forbids raw-gap escalation

#### 34. 09_RAG__var_demanding — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P3 |
| Grok preset | P3 |
| Chosen preset (by Grok4.2) | P3 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.3767 / 0.5314 / 0.3625 / 0.5497 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.3762 bits |
| Confidence | 0.5937 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P3 deep (59% soft / 64% budget-weighted deep mass); moderate but not decisive. Deep-vote mass >>30% bar while standard mass=17%<30% so no sanctioned escalation or P2-valley risk; dominant depth gaps (need_d 10/7/7 in S1/S2/S6), 32 unbacked anchors, 8 must-ev in S3, and guideline's repeated 'must cover in depth' for embeddings, chunking, metadata, agentic distinction, plus production examples all align with P3. No downward override as high-budget weakest sections (S1 15%, S2 14%) show low cov (4·4 / 4·2).

**Decision drivers:** scorer P3 + 64% deep mass · depth-dominant gaps + 32 orphans · must-ev counts across S1-S3/S6

**Risk flags:**
- moderate scorer confidence on demanding variant
- S4/S5 already cov 7+, possible diminishing returns

#### 35. 10_memory_knowledge_access__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6893 / 0.64 / 0.6446 / 0.5982 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 0.8631 bits |
| Confidence | 0.7143 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Hard constraint: external-evidence policy=FORBIDDEN explicitly requires P0 skip (exploration output cannot be used). Scorer aggregate is decisive P0 at 71% budget-weighted mass (standard=0%, deep=0%); every section is brief-flagged and already meets cov≥6.

**Decision drivers:** forbidden-evidence-policy · decisive-P0-vote · all-sections-brief

**Risk flags:**
- none

#### 36. 10_memory_knowledge_access__var_standard — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.4776 / 0.5534 / 0.4779 / 0.4473 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.5226 bits |
| Confidence | 0.6261 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Scorer aggregate is P1 (63% light mass); uncertain but light-dominant with standard/deep masses only 15% each (below 30% escalation gates). S5 brief-flagged, S6/S7 already well-covered (cov 7·6), dominant gap type is depth but policy bars re-deriving level from raw gaps.

**Decision drivers:** scorer_aggregate · vote_mass_below_threshold · brief_flag_on_S5

**Risk flags:**
- depth_gaps_in_S3_S1_may_remain
- must-ev_4_in_S5_with_brief

#### 37. 10_memory_knowledge_access__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P2 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.3478 / 0.5424 / 0.5895 / 0.5482 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 0.6932 bits |
| Confidence | 0.814 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** The GRPO-trained section-scorer's aggregate is decisively P2 standard (81% budget-weighted mass on standard, 19% on deep). This already incorporates the per-section need_depth (3-7), must-ev counts (2-5), unbacked anchors (28 total), and dominant depth-gap economics; S6's lone deep vote (19% budget) falls below the 30% sanctioned-escalation gate for P3. External-evidence policy is REQUIRED but satisfied by P2; no brief flags or high-coverage sections justify a downward override.

**Decision drivers:** decisive_scorer_81pct_standard · standard_vote_mass_81pct · deep_vote_mass_below_30pct · required_external_evidence_met

**Risk flags:**
- S6 (19% budget) and S1/S7 weakest sections show elevated need_depth
- guideline demands many named production examples and one failure-mode case study

#### 38. 11_multimodal__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.369 / 0.3362 / 0.3024 / 0.2631 |
| Regret (counted) | 0.0 (excluded — forbidden policy, not counted in regret stats) |
| Entropy | 1.699 bits |
| Confidence | 0.5517 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Hard constraint: external-evidence policy=FORBIDDEN mandates P0 (overrides all else). Scorer aggregate is also P0 skip (55% budget-weighted mass); uncertain entropy but standard/deep masses only 14% each, so no sanctioned escalation. Most sections flagged 'brief', guideline demands conceptual overview only.

**Decision drivers:** forbidden-evidence-policy · scorer-P0-vote-mass · brevity-flags

**Risk flags:**
- none

#### 39. 11_multimodal__var_standard — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.6854 / 0.6666 / 0.4056 / 0.6013 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.2765 bits |
| Confidence | 0.4836 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Aggregate RL vote is P1 light (budget-weighted: light 55%, skip 39%, standard 0%, deep 6%); moderate confidence, not decisive. Escalation gates unmet (standard-mass 0% <<30%, deep-mass 6% <<30%), no sanctioned upward move; downward override also fails as high-budget sections (S3 23% skip cov 5·5, S5 15% light cov 8·5) mix well-covered with depth gaps in S1/S7 and 11 must-ev bullets. Dominant gap=depth but raw counts do not override the calibrated vote peak at P1.

**Decision drivers:** budget-weighted vote mass · escalation gates unmet · high-budget section coverage

**Risk flags:**
- S1 deep vote (6% budget) may leave intro gaps
- 11 must-ev items could need more than light touch-up

#### 40. 11_multimodal__var_demanding — ~ NEAR (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P2 |
| Grok preset | P3 |
| Chosen preset (by Grok4.2) | P3 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.4383 / 0.5775 / 0.6064 / 0.6104 |
| Regret (counted) | -0.004 (-0.004) |
| Entropy | 1.1036 bits |
| Confidence | 0.6313 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Scorer aggregate is P2 standard (63% standard / 34% deep mass; MODERATE confidence, not decisive). Budget-weighted votes show 64% standard + 33% deep; deep mass >=30% from S4 (18%, deep·1.00, 4 must-ev) and S5 (15%, deep·1.00, 6 must-ev) triggers sanctioned P2->P3 escalation per override policy. 38 unbacked anchors, dominant depth gaps, high must-ev in large sections (S2/S3/S4/S5), and REQUIRED external-evidence policy confirm need for extra depth round.

**Override reason:** Sanctioned upward escalation from P2 to P3 because vote uncertain and deep-vote mass (33%) clears 30% threshold on heavy technical sections

**Decision drivers:** budget-weighted deep mass 33% · high must-ev in S4/S5 (4-6) · 38 unbacked anchors · REQUIRED evidence policy

**Risk flags:**
- possible diminishing returns on already-strong S3/S5 coverage
- guideline length could inflate perceived gaps
