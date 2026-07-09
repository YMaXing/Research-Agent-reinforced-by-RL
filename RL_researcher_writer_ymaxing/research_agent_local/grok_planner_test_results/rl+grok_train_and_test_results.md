# RL + Grok 4.2 Planner Train & Test Results

## Summary — TEST split (held-out, primary metric), n=16

| # | Article | RL | Grok | Chosen | → Oracle | Verdict |
|---|---|---|---|---|---|---|
| 1 | 04_structured_outputs | P1 | P1 | P1 | P2 | ~ NEAR |
| 2 | 07_reasoning_planning | P0 | P0 | P0 | P0 | ✓ EXACT |
| 3 | 13_agent_framework | P0 | P0 | P0 | P3 | ✗ MISS |
| 4 | 14_agent_system_design | P1 | P1 | P1 | P1 | ✓ EXACT |
| 5 | 29_evaluation_metrics | P0 | P0 | P0 | P1 | ~ NEAR |
| 6 | 31_CI | P0 | P0 | P0 | P1 | ~ NEAR |
| 7 | Bird_Eye_Extreme | P0 | P0 | P0 | P1 | ~ NEAR |
| 8 | Dark_Dimension | P0 | P0 | P0 | P0 | ✓ EXACT |
| 9 | Distinct_AI_Models | P0 | P1 | P1 | P1 | ✓ EXACT |
| 10 | Earth_Oceans_Origin | P1 | P1 | P1 | P3 | ✗ MISS |
| 11 | Gravity_Entropy | P1 | P1 | P1 | P1 | ✓ EXACT |
| 12 | HNSW | P0 | P1 | P1 | P1 | ✓ EXACT |
| 13 | Insects_Consciousness | P0 | P1 | P1 | P1 | ✓ EXACT |
| 14 | Space-Time_QECC | P0 | P0 | P0 | P1 | ~ NEAR |
| 15 | State_of_LLM_Reasoning (policy: forbidden) | P0 | P0 | P0 | P0 | ✓ EXACT |
| 16 | Understanding_Reasoning_LLMs | P0 | P0 | P0 | P2 | ✗ MISS |

**Overall:** n=16 · exact=8 (50%) · near=5 (31%) · miss=3 (19%) · no-oracle/error=0
**Ordinal MAE:** 0.750
**Reward-regret** (allowed/required only, n=15; 1 forbidden excluded): mean=0.0677, max=0.2759

### Confusion matrix

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 3 | 0 | 0 | 0 | 3 |
| P1 light | 4 | 5 | 0 | 0 | 9 |
| P2 standard | 1 | 1 | 0 | 0 | 2 |
| P3 deep | 1 | 1 | 0 | 0 | 2 |

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
| 24 | 11_multimodal__var_demanding (required) | P2 | P2 | P2 | P2 | ✓ EXACT |

**Overall:** n=24 · exact=20 (83%) · near=4 (17%) · miss=0 (0%) · no-oracle/error=0
**Ordinal MAE:** 0.167
**Reward-regret** (allowed/required only, n=16; 8 forbidden excluded): mean=0.0139, max=0.0992

### Confusion matrix (Train)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 9 | 1 | 0 | 0 | 10 |
| P1 light | 1 | 6 | 2 | 0 | 9 |
| P2 standard | 0 | 0 | 3 | 0 | 3 |
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
| var_demanding | 8 | 7/8 | 8/8 | mean=0.0075, max=0.0601 |

---

## Combined — Train + Test (n=40)

- n=40 · exact=28 (70%) · near=9 (23%) · miss=3 (8%) · no-oracle/error=0
- Reward-regret (allowed/required only, n=31; 9 forbidden excluded): mean=0.0400, max=0.2759

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

**Reasoning:** Section-scorer aggregate is P1 light (53% light, 47% skip, 0% for standard/deep); moderate confidence but primary reward-trained signal. No section votes above light; high-budget S4 already at depth cov=6 while scorer weighed the must-ev totals. No sanctioned override condition met (vote not P0, entropy ~1 bit, not >1.5). Follow P1 as the unimodal peak.

**Decision drivers:** scorer_aggregate_P1 · no_higher_section_votes · balanced_gaps_already_priced

**Risk flags:**
- close 47-53 split could tilt either way on marginal coverage
- high must-ev in S3/S4 (21 total) but scorer already internalized

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

**Reasoning:** Section-scorer aggregate is P0 skip at 55% (moderate confidence, 21% light runner-up, 24% deep). S7 (24% budget) votes deep·1.00 and light mass is <25%, so the single sanctioned P0→P1 nudge is blocked. Scorer already priced in the 42 unbacked anchors, dominant depth gaps, must-ev counts, and per-section cov/need numbers; no override condition is met.

**Decision drivers:** scorer_aggregate_P0 · deep_voting_section_blocks_nudge · no_sanctioned_override

**Risk flags:**
- 24% deep vote on high-budget S7
- many must-ev and orphans still present

### 3. 13_agent_framework — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.6446 / 0.6716 / 0.5805 / 0.6939 |
| Regret (counted) | 0.0492 (0.0492) |
| Entropy | 1.3375 bits |
| Confidence | 0.5336 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Section-scorer aggregate is P0 skip (53% skip, 37% light, 10% deep, 0% standard) at moderate confidence. Sanctioned P0->P1 nudge disallowed because S11/S12 individually vote deep (depth-or-nothing pattern). Scorer already priced in 42 unbacked anchors, high must-ev in S4 (15), and dominant depth gaps; per-section cov scores show strong coverage on largest-budget deep-dive sections.

**Decision drivers:** scorer_aggregate_P0 · deep_voting_sections_block_nudge · scorer_already_weighed_must_ev_orphans

**Risk flags:**
- moderate_vote_entropy
- S1_S2_light_votes_and_S4_high_must_ev

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

**Reasoning:** Scorer aggregate is P1 light (44% plurality); entropy 1.53 bits flags uncertainty but does not trigger sanctioned downward override as high-budget sections (S2/S4/S3) are mixed on RL picks and coverage; dominant gap is depth but scorer already weighted all must-ev/orphans against reward trade-off; external-evidence is only ALLOWED so P1 is the unimodal peak.

**Decision drivers:** scorer aggregate P1 · entropy uncertainty · no sanctioned override

**Risk flags:**
- vote spread could undervalue S3 depth needs
- if gaps are deeper than scorer priced then light buys only partial evidence

### 5. 29_evaluation_metrics — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P1 (light) |
| Rewards (P0 / P1 / P2 / P3) | 0.5118 / 0.7876 / 0.7138 / 0.685 |
| Regret (counted) | 0.2759 (0.2759) |
| Entropy | 1.3424 bits |
| Confidence | 0.4559 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Section-scorer aggregate is P0 skip (46% skip / 46% light / 9% deep, moderate confidence). S2 (35% budget) votes skip·1.00 while only the 9% intro section votes deep·1.00; this triggers the 'multiple sections voting deep → keep P0' clause and blocks the single sanctioned P0→P1 nudge. Gap table and 47 unbacked anchors already priced into the scorer's reward-optimal vote; no hard external-evidence requirement.

**Decision drivers:** scorer_aggregate_P0 · deep_vote_in_S1_blocks_nudge · largest_section_skip

**Risk flags:**
- vote tie may undervalue S1 depth gap
- dominant depth gaps could justify light touch-up

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

**Reasoning:** Section-scorer aggregate is P0 skip at 100% (decisive, entropy=0); every individual section also votes skip·1.00. No sanctioned upward nudge applies (light has 0% mass). Gap table and 42 unbacked anchors were already priced into the scorer's reward-optimal vote; external-evidence policy is only ALLOWED, not required.

**Decision drivers:** scorer_100pct_P0 · no_sanctioned_override · all_sections_skip

**Risk flags:**
- high must-ev counts could indicate under-covered evidence if scorer miscalibrated

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

**Reasoning:** Scorer aggregate is decisively P0 skip (80% mass, 20% light runner-up, 0% standard/deep). This meets no sanctioned upward-nudge condition (>=25% light mass required) and the asymmetric policy forbids escalating a P0 vote on gap-table grounds alone. Scorer already priced in the 31 unbacked anchors, S1/S3 must-ev counts, and dominant depth gaps; existing local golden sources plus one exploitation pass suffice for the 2050-word theory article.

**Decision drivers:** scorer's decisive 80% P0 vote · nudge threshold not met (20%<25%) · no section votes standard/deep

**Risk flags:**
- moderate residual depth gaps in S1/S3 could leave a few must-ev thin if local files insufficient

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

**Reasoning:** Section-scorer aggregate is P0 skip at 100% (decisive, every section also votes skip·1.00). Vote distribution shows 0% mass on light so the single sanctioned P0→P1 nudge is unavailable; gap table (27 unbacked anchors, must-ev 5-8, depth-dominant) was already priced into the scorer's reward-optimal pick and cannot justify escalation per instructions.

**Decision drivers:** scorer_100pct_P0 · no_sanctioned_nudge_condition · all_sections_skip

**Risk flags:**
- high must-ev and orphans could leave some claims undersourced

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

**Reasoning:** Scorer aggregate is P0 skip (60% mass, moderate confidence) with P1 light as runner-up at 40%. This exactly matches the sanctioned upward nudge (P0→P1 only) because runner-up mass ≥25%, no section votes standard/deep, and external-evidence is ALLOWED. Per-section table shows persistent must-ev (3–4 per section), 30 article-wide unbacked anchors, and S3/S4 (weakest, both voting light) still needing depth on convergence evidence and experimental critiques; light balanced round buys cheap insurance for these without violating brief flags on S1/S3.

**Override reason:** sanctioned P0-to-P1 nudge triggered by 40% light mass and absence of any standard/deep sectional votes

**Decision drivers:** scorer P0 with substantial P1 runner-up · sanctioned cheap-insurance nudge · must-ev + unbacked anchors in S3/S4

**Risk flags:**
- light round may still add little if exploitation already saturated the listed golden sources
- brief-flagged S3 could be diluted if exploration pulls in excess depth

### 10. Earth_Oceans_Origin — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| RL preset | P1 |
| Grok preset | P1 |
| Chosen preset (by Grok4.2) | P1 |
| Oracle | P3 (deep) |
| Rewards (P0 / P1 / P2 / P3) | 0.4707 / 0.5086 / 0.5917 / 0.6133 |
| Regret (counted) | 0.1046 (0.1046) |
| Entropy | 0.9367 bits |
| Confidence | 0.6471 |
| Floor applied | yes |
| Grok override | no |

**Reasoning:** Section-scorer aggregate is P1 light (65% light, 35% standard, moderate confidence). High-budget sections S2/S3 are brief-flagged with solid depth cov (7 and 6); dominant gap is breadth but scorer already priced must-ev/unbacked anchors (38 total) into its P1 vote. No sanctioned override applies: cannot escalate above P1, and conditions for dropping to P0 not decisive enough to depart from primary signal.

**Decision drivers:** scorer_aggregate_P1 · brief_flags_on_high_budget · no_upward_override_allowed

**Risk flags:**
- 35% standard mass on S3 (high must-ev=5)
- breadth-dominant gaps could benefit from extra round

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

**Reasoning:** Section-scorer aggregate is P1 light (58% light, 42% skip, 0% for standard/deep) with moderate confidence; this is the reward-trained peak. Multiple high-budget sections (S2/S3) are brief-flagged and cannot absorb extra material; dominant gap is depth (not breadth) while several sections already show depth_score >=6-7. Scorer already priced the 32 unbacked anchors, must-ev counts, and per-section needs (S2/S5 weakest) against the unimodal reward curve; no sanctioned override condition is met.

**Decision drivers:** scorer_aggregate_P1 · brief_flags_on_S2_S3 · depth_dominant_gaps · no_higher_votes

**Risk flags:**
- S2 low coverage (4·4) but brief-flagged may limit upside
- 42% skip mass could make light marginal if gaps are already overstated

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

**Reasoning:** Scorer aggregate is P0 (54% skip, 46% light, 0% on P2/P3); this exactly matches the sanctioned P0→P1 nudge (runner-up ≥25%, no section votes standard/deep). Decisive drivers are S4 (46% budget, RL pick light·1.00, 9 must-ev, 12 orphans) plus dominant depth gaps, while brief-flagged S1/S2 stay protected.

**Override reason:** Sanctioned cheap-insurance nudge from P0 to P1 per asymmetric policy; scorer already priced gaps but distribution + S4's must-ev justify light touch-up

**Decision drivers:** scorer vote split 54/46 · S4 high-budget must-ev · sanctioned P0->P1 condition · no P2/P3 section votes

**Risk flags:**
- light round may still add little on brief S2
- depth-dominant gaps could need more than one balanced round

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

**Reasoning:** Scorer aggregate P0 (68% skip, 32% light runner-up); exactly matches sanctioned P0->P1 nudge (substantial light mass, no std/deep section votes); 22 unbacked anchors + per-section must-ev 4-6 justify cheap insurance without violating asymmetry or reward curve.

**Override reason:** Sanctioned single-level P0->P1 nudge condition met; scorer's primary signal respected but overridden per explicit policy for cheap insurance

**Decision drivers:** scorer P0+32% light mass · sanctioned nudge clause · must-ev and unbacked count

**Risk flags:**
- over-escalation dilutes flow if gaps are already priced in
- depth-dominant gaps may need more than light

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

**Reasoning:** Section-scorer aggregate is decisively P0 (84% skip, 0% light/standard, 16% deep). The 16% deep mass is exactly accounted for by S2's 16% budget voting deep·1.00 with cov 0·0, yet the learned vote still peaks at skip; per asymmetric override rules, no sanctioned P0→P1 nudge exists because runner-up is not light at ≥25% and a section individually votes deep. Scorer already priced the 27 unbacked anchors, S2 must-ev=4, and brief-flagged high-budget sections, so reward peak is at P0.

**Decision drivers:** scorer 84% P0 decisive · no sanctioned upward nudge · gap table not re-derived

**Risk flags:**
- S2 zero coverage + deep vote could indicate under-explored core mechanics

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

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, mandating P0 skip per hard constraints. Scorer aggregate is also decisive P0 (71% skip, 0% standard). Per-section table shows depth-dominant gaps and unbacked anchors but these were already priced into the scorer vote; policy overrides any escalation.

**Decision drivers:** external_evidence_forbidden · scorer_P0_71pct

**Risk flags:**
- some sections show low cov_d and high must-ev

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

**Reasoning:** Section-scorer aggregate is decisive P0 skip (92% mass, 0% light/standard, only 8% deep); S6's individual deep vote and high must-ev/unbacked anchors (52 total) were already priced into the GRPO-trained recommendation. No sanctioned upward nudge applies (runner-up not P1 at ≥25%, depth-or-nothing pattern present). Gap table ignored per asymmetric-override policy.

**Decision drivers:** scorer_92pct_skip · decisive_vote · no_sanctioned_P0->P1

**Risk flags:**
- S5 45% budget + 8 must-ev could be under-covered
- all cov 0·0 but scorer already weighed



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
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 1.543 bits |
| Confidence | 0.4231 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** Hard constraint: external-evidence policy explicitly set to FORBIDDEN (exploration output cannot be used). This overrides the uncertain P1-light aggregate vote (42% light, entropy 1.54 bits) and per-section gaps (e.g. S5 standard pick, 48 unbacked anchors). Guideline also demands conceptual overview only with no external libraries/case studies.

**Override reason:** External-evidence policy = forbidden mandates P0; cannot escalate or use exploration

**Decision drivers:** external-evidence policy · hard constraint override

**Risk flags:**
- scorer uncertainty and dominant depth gaps ignored due to policy

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

**Reasoning:** Section-scorer aggregate is P1 light (58% light, 29% standard, 13% deep; moderate confidence). No sanctioned override conditions met: not highly uncertain (dominant light arm), high-budget sections (S5 30%, S4 18%) not mostly brief-flagged or depth_score >=6 across the board, and upward moves from a P1+ vote are forbidden. Dominant depth gaps and 47 unbacked anchors were already priced into the scorer's P1 recommendation.

**Decision drivers:** scorer_aggregate_P1 · no_sanctioned_override · moderate_confidence

**Risk flags:**
- S2_deep_vote_and_S3/S6_standard_votes
- must_ev_4_in_largest_section_S5
- depth-dominant_gaps

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

**Reasoning:** Scorer's budget-weighted aggregate is P2 standard (49% top-pick, 29% skip runner-up, moderate confidence). No sanctioned override applies: S5 (29% budget) votes skip with cov 8·6 but the RL model already priced this against must-ev and depth needs in S2-S4 (standard ·1.00 each). Dominant gap type is depth, matching the depth-first round in the chosen preset; external-evidence policy is ALLOWED and gaps justify exploration.

**Decision drivers:** scorer_aggregate_P2 · moderate_49pct · no_sanctioned_override

**Risk flags:**
- S5_skip_vote_on_high_budget_section
- vote_entropy_from_29pct_skip

#### 20. 03_context_engineering__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.7625 / 0.7783 / 0.6314 / 0.7269 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.8967 bits |
| Confidence | 0.6908 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, which hard-constrains to P0 skip regardless of other signals. Scorer aggregate is 69% skip (moderate confidence, 0% on std/deep); every section is brief-flagged with 0 must-ev, cov scores already meet guideline surface-level intent, and the guideline repeatedly stresses conceptual overview with no external examples or depth required.

**Decision drivers:** external-evidence-forbidden · scorer-P0-dominant · all-sections-brief-flagged

**Risk flags:**
- internal exploitation may have left conceptual anchors unbacked

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

**Reasoning:** Section-scorer aggregate is P1 light (53% vs 47% skip, 0% on standard/deep) as the reward-trained peak; high-budget sections (S3/S4/S6/S7) already show cov d≥5-8 on many must-ev items and the scorer weighed the 68 orphans + dominant depth gaps. No override conditions met (no brief flags, vote not uncertain enough for downward). Light balanced round targets the direction without over-escalation risk.

**Decision drivers:** scorer aggregate (primary) · moderate confidence · no sanctioned override

**Risk flags:**
- close skip/light split could undervalue S6/S7 depth gaps
- if must-ev sourcing is harder than scored, light may leave a few anchors thin

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

**Reasoning:** Section-scorer aggregate is P1 light (68% mass, moderate confidence) after budget-weighting every section; this is the reward-trained peak. External-evidence policy is REQUIRED so P0 is forbidden, but no sanctioned upward override exists from a P1+ vote and dominant gaps are already priced into the scorer. Per-section table shows depth-dominant needs and must-ev (esp. S6 11, S4 6) yet high cov d·b scores (mostly 7-8·6) and light RL picks on the largest-budget sections; escalation would cross the single-peaked reward curve.

**Decision drivers:** scorer_aggregate_P1 · external_required_minimum · depth_dominant_but_high_cov

**Risk flags:**
- S3/S8 standard votes
- 52 unbacked anchors
- S6 high must-ev

#### 23. 05_workflow_patterns__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P1 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.872 / 0.8408 / 0.796 / 0.746 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.9912 bits |
| Confidence | 0.5552 |
| Floor applied | no |
| Grok override | **yes** |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, which is a hard constraint mandating P0 skip regardless of the section-scorer's P1-light aggregate (56% light, 44% skip). All 7 sections are brief-flagged, guideline demands only surface-level conceptual overview with no external libs/case studies, and exploration output cannot be used.

**Override reason:** Hard constraint from external-evidence policy = forbidden requires P0 despite scorer's P1 vote

**Decision drivers:** external-evidence policy · all sections brief-flagged · surface-level guideline

**Risk flags:**
- scorer lean toward light but policy is absolute

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

**Reasoning:** Scorer aggregate is P2 standard (49% top vote, 41% light runner-up, moderate confidence); dominant gap type is depth with high need_d in S1/S2 (40/44) plus 52 article-wide unbacked anchors; high-budget sections mostly cov_d >=6 but scorer already priced this in; no sanctioned override condition met.

**Decision drivers:** scorer_aggregate_P2 · dominant_depth_gaps

**Risk flags:**
- vote split 49-41 could tilt light on marginal returns
- S2 theory-only with 14 orphans

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

**Reasoning:** Scorer aggregate is P1 light (48% vote) as the reward peak; external-evidence REQUIRED forbids P0 while override policy bars upward moves from any P1+ recommendation; per-section deep votes and depth gaps were already weighted by the GRPO model.

**Decision drivers:** scorer_aggregate_P1 · external_evidence_required · no_sanctioned_upward

**Risk flags:**
- vote_split_48_37
- high_must_ev_in_S1_S2

#### 26. 06_tools__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6903 / 0.6818 / 0.557 / 0.3205 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.9643 bits |
| Confidence | 0.6107 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy explicitly FORBIDDEN (mandates P0); section-scorer aggregate is P0 skip (61% mass, 0% on std/deep); every high-budget section (S3–S7) is brief-flagged with surface-level mandate and cov d·b already >=3·2.

**Decision drivers:** external-evidence-forbidden · scorer-aggregate-P0 · universal-brevity-flags

**Risk flags:**
- moderate scorer entropy (39% light)
- many unbacked anchors (47) but policy and brevity override

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

**Reasoning:** Section-scorer aggregate is P0 skip (59%, runner-up standard 18%) but uncertain (entropy 1.61). Multiple sections individually vote standard/deep (S2, S6, S8), violating the exact conditions for the single sanctioned P0→P1 nudge. Scorer already priced in the 52 unbacked anchors, high must-ev counts, and dominant depth gaps; instructions forbid re-deriving escalation from the per-section table. External-evidence policy=ALLOWED does not trigger mandatory exploration.

**Decision drivers:** scorer_aggregate_P0 · sanctioned_nudge_conditions_not_met · no_hard_constraint

**Risk flags:**
- high uncertainty
- large depth gaps in S3/S4 despite brief flag

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

**Reasoning:** Section-scorer aggregate is P3 deep (38% mass) despite high uncertainty (entropy 1.92 bits). This is the primary signal; high-budget S3 (24%, RL pick deep·1.00, need_depth=8) and S8 (must-ev=4, RL pick deep·1.00) dominate the weighted vote. Guideline explicitly demands named production examples, real-world failure modes, text-to-SQL mechanisms, sandbox security mitigations and concrete RAG/memory anchors in S8/S9, which the prior exploitation pass only partially met. No sanctioned downward override applies given the must-ev and depth-dominant economics.

**Decision drivers:** scorer_P3_recommendation · must-ev_in_S8_S9 · depth_gaps_in_S3

**Risk flags:**
- high entropy could justify P2 if gaps were overestimated
- P3 may surface diminishing returns on code-heavy sections

#### 29. 08_react_practice__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6543 / 0.1224 / 0.0647 / 0.3828 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.8727 bits |
| Confidence | 0.7069 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy explicitly FORBIDDEN (exploration output cannot be used), mandating P0; section-scorer aggregate decisively votes P0 skip (71% / 0% on P2/P3) with only one light section; guideline repeatedly demands 'must stay brief', surface-level notebook mirroring, and no external libraries/case studies.

**Decision drivers:** external-evidence-forbidden · scorer-aggregate-P0 · brevity-flags

**Risk flags:**
- none - hard constraint overrides all gap signals

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

**Reasoning:** Scorer aggregate is P0 (51%) but P1 runner-up holds 49% mass; sanctioned upward nudge from P0 to P1 is permitted because no section votes standard/deep and conditions match exactly. Largest-budget sections (S4/S5) individually select light and carry high must-ev (12+18); P1 is the reward peak per the unimodal curve and cheap-insurance clause.

**Override reason:** applied single sanctioned P0->P1 nudge (substantial runner-up mass, no std/deep section votes)

**Decision drivers:** scorer aggregate + vote split · sanctioned P0->P1 nudge condition · section RL picks on high-budget rows

**Risk flags:**
- S5 brief=yes may limit absorption
- 51/49 split could be noise

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

**Reasoning:** Section-scorer aggregate is P2 standard (46% vs 45% skip; moderate confidence). External-evidence policy is REQUIRED so P0 forbidden; dominant gap type is depth with 42 unbacked anchors and high-budget S5 (28%, standard·1.00, need_depth 22, cov 7) plus S4 (18%, standard·1.00) driving the weighted vote. No sanctioned downward override triggered because not all high-budget sections are brief-flagged and unmet depth pressure remains substantial.

**Decision drivers:** scorer_aggregate_P2 · external_evidence_required · dominant_depth_gaps · S5_S4_budgeted_standard_votes

**Risk flags:**
- bimodal vote (skip/standard tie)
- S5 brief flag could limit absorption

#### 32. 09_RAG__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.7317 / 0.5683 / 0.4467 / 0.3627 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.9588 bits |
| Confidence | 0.6318 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN; exploration output cannot be used, so P0 is the only valid choice per hard constraints. Section-scorer aggregate also votes P0 skip (63% mass, 0% on P2/P3). Per-section must-ev and unbacked anchors exist but are already priced into the scorer's P0 recommendation; guideline demands surface-level theory only with no external examples permitted.

**Decision drivers:** external-evidence-forbidden · scorer-P0-vote

**Risk flags:**
- moderate scorer entropy (37% on light)

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

**Reasoning:** Scorer aggregate is P0 skip at 52% (moderate; standard runner-up 29%). Sanctioned P0-to-P1 nudge disallowed: light only 19% (below 25% mass), runner-up not light, and S4 (29% budget) votes standard. No hard external-evidence constraint and gap table (48 unbacked anchors, high must-ev in S3/S4) ignored per instructions as scorer already weighted them for reward peak.

**Decision drivers:** scorer_aggregate_P0 · nudges_not_met

**Risk flags:**
- moderate vote entropy
- S4 standard vote on largest section

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

**Reasoning:** Section-scorer aggregate is P3 deep (59% deep, 0% skip) with moderate confidence; this is the primary signal. Dominant gap type is depth, weakest high-budget sections (S1/S2) show low cov (4/8 depth) + high need_depth (10/2 and 7/4), S3 carries 8 must-ev, S6 carries 5 must-ev, and 32 unbacked anchors remain. Guideline demands many named tools/benchmarks/production examples plus one failure-mode case study; these align with the scorer's reward-optimal pick of deep (3 rounds: depth → breadth → depth). No sanctioned override applies.

**Decision drivers:** scorer_P3_59pct · depth_dominant_gaps_S1_S2_S6 · 23_total_must_ev_plus_32_unbacked

**Risk flags:**
- moderate_vote_entropy_23pct_light
- S1_brief_flag_limits_absorption
- possible_diminishing_returns_on_final_depth_round

#### 35. 10_memory_knowledge_access__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.6893 / 0.64 / 0.6446 / 0.5982 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 0.8631 bits |
| Confidence | 0.7143 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, mandating P0 skip per hard constraints. Section-scorer aggregate is decisively P0 (71% skip, 0% standard/deep); all sections are brief-flagged with high existing cov d·b (>=6·6) and guideline demands surface-level conceptual overview only.

**Decision drivers:** forbidden-policy · scorer-decisive-P0 · brevity-flags

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

**Reasoning:** Section-scorer aggregate votes P1 light (63% mass) despite entropy 1.52 uncertainty; this is the reward-trained peak after pricing in all must-ev, orphans, need_depth (esp. S1/S3), and dominant depth gaps. No sanctioned override triggered (cannot escalate P1+; not all high-budget sections are brief/well-covered). Per-section RL picks and brief flag on S5 further anchor at light.

**Decision drivers:** section-scorer aggregate · vote entropy/uncertainty · no sanctioned override

**Risk flags:**
- S3 deep vote + high must-ev could leave depth shortfall
- 32 unbacked anchors if light yields duplicates

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

**Reasoning:** Scorer aggregate is P2 standard at 81% (decisive, all high-budget sections vote standard or deep); dominant gap=depth and must-ev totals align with 2-round depth->breadth; external-evidence=REQUIRED rules out P0; no override conditions triggered per asymmetric policy.

**Decision drivers:** scorer_aggregate · dominant_depth_gaps · external_required

**Risk flags:**
- S6 deep vote + high must-ev could under-serve production lessons

#### 38. 11_multimodal__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| RL preset | P0 |
| Grok preset | P0 |
| Chosen preset (by Grok4.2) | P0 |
| Oracle | P0 (skip) |
| Rewards (P0 / P1 / P2 / P3) | 0.369 / 0.3362 / 0.3024 / 0.2631 |
| Regret (counted) | 0.0 (excluded — forbidden) |
| Entropy | 1.699 bits |
| Confidence | 0.5517 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, mandating P0; section-scorer aggregate is also P0 skip (55%, entropy 1.70); all must-ev=0 and most sections are brief-flagged with surface-level guideline intent.

**Decision drivers:** external-evidence-forbidden · scorer-P0-vote · brief-flags-dominant

**Risk flags:**
- scorer entropy >1.5
- 32 unbacked anchors

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

**Reasoning:** Section-scorer aggregate is P1 light (48% light vs 45% skip, moderate confidence); no sanctioned override applies (not P0, not uncertain >1.5 bits, not all high-budget sections brief/well-covered). S3/S5 show strong coverage (5·5/8·5) yet S1/S7 remain depth-weak (4·4 cov, deep/light votes) with depth-dominant gaps and 42 unbacked anchors; scorer already priced these, so P1 is the reward peak.

**Decision drivers:** scorer_aggregate_P1 · moderate_vote_split · mixed_high-budget_cov · depth_dominant_no_escalation

**Risk flags:**
- close skip/light split could undervalue S1/S7 depth
- must-ev in S3/S5 might need one extra source

#### 40. 11_multimodal__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| RL preset | P2 |
| Grok preset | P2 |
| Chosen preset (by Grok4.2) | P2 |
| Oracle | P2 (standard) |
| Rewards (P0 / P1 / P2 / P3) | 0.4383 / 0.5775 / 0.6064 / 0.6104 |
| Regret (counted) | 0.0 (0.0) |
| Entropy | 1.1036 bits |
| Confidence | 0.6313 |
| Floor applied | no |
| Grok override | no |

**Reasoning:** Section-scorer aggregate is P2 standard (63% vote, 34% deep, moderate confidence); high must-ev counts (S5:6, S2:5, S3:4, S4:4) plus dominant depth gaps and 38 unbacked anchors already priced into the GRPO vote. External-evidence REQUIRED eliminates P0; no sanctioned downward conditions met (no brief flags, clear dominant arm, several high-budget sections show unmet need_depth).

**Decision drivers:** scorer_aggregate_P2 · must_ev_in_S2_S3_S4_S5 · external_ev_required · dominant_depth_gaps

**Risk flags:**
- 34% deep mass could indicate marginal extra value in S4/S5 but asymmetry penalizes over-escalation