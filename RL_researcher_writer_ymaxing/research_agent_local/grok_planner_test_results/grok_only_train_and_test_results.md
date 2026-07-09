# Grok-Only Planner Train & Test Results

All decisions in this dataset are Grok-only (standalone baseline; no RL preset used, `chosen_by` = Grok-only throughout). Confidence/entropy/floor metrics are not computed in this mode.

## Test summary — held-out, primary metric (n=16)

| # | Variant | Grok preset | Oracle | Verdict |
|---|---|---|---|---|
| 1 | 04_structured_outputs | P2 | P2 (standard) | ✓ EXACT |
| 2 | 07_reasoning_planning | P2 | P0 (skip) | ✗ MISS |
| 3 | 13_agent_framework | P2 | P3 (deep) | ~ NEAR |
| 4 | 14_agent_system_design | P2 | P1 (light) | ~ NEAR |
| 5 | 29_evaluation_metrics | P2 | P1 (light) | ~ NEAR |
| 6 | 31_CI | P2 | P1 (light) | ~ NEAR |
| 7 | Bird_Eye_Extreme | P2 | P1 (light) | ~ NEAR |
| 8 | Dark_Dimension | P2 | P0 (skip) | ✗ MISS |
| 9 | Distinct_AI_Models | P2 | P1 (light) | ~ NEAR |
| 10 | Earth_Oceans_Origin | P1 | P3 (deep) | ✗ MISS |
| 11 | Gravity_Entropy | P2 | P1 (light) | ~ NEAR |
| 12 | HNSW | P2 | P1 (light) | ~ NEAR |
| 13 | Insects_Consciousness | P2 | P1 (light) | ~ NEAR |
| 14 | Space-Time_QECC | P2 | P1 (light) | ~ NEAR |
| 15 | State_of_LLM_Reasoning (policy: forbidden) | P0 | P0 (skip) | ✓ EXACT |
| 16 | Understanding_Reasoning_LLMs | P2 | P2 (standard) | ✓ EXACT |

**Overall:** n=16 · exact=3 (19%) · near=10 (62%) · miss=3 (19%) · no-oracle/error=0
**Ordinal MAE:** 1.000
**Reward-regret** (allowed/required only, n=15; 1 forbidden excluded): mean=0.1151, max=0.3092

### Confusion matrix (Test)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 1 | 0 | 2 | 0 | 3 |
| P1 light | 0 | 0 | 9 | 0 | 9 |
| P2 standard | 0 | 0 | 2 | 0 | 2 |
| P3 deep | 0 | 1 | 1 | 0 | 2 |

### Baselines (Test)

- Oracle distribution: P0=3, P1=9, P2=2, P3=2
- Majority-class baseline (always P1 light): 56.2% (9/16)
- Uniform-random baseline (1/4): 25.0%
- Weighted-random baseline: 38.3%

---

## Train summary — reference (n=24)

| # | Variant | Policy | Grok preset | Oracle | Verdict |
|---|---|---|---|---|---|
| 1 | 02_workflows_vs_agents__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 2 | 02_workflows_vs_agents__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 3 | 02_workflows_vs_agents__var_demanding | allowed | P2 | P1 (light) | ~ NEAR |
| 4 | 03_context_engineering__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 5 | 03_context_engineering__var_standard | allowed | P2 | P0 (skip) | ✗ MISS |
| 6 | 03_context_engineering__var_demanding | required | P2 | P1 (light) | ~ NEAR |
| 7 | 05_workflow_patterns__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 8 | 05_workflow_patterns__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 9 | 05_workflow_patterns__var_demanding | required | P2 | P1 (light) | ~ NEAR |
| 10 | 06_tools__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 11 | 06_tools__var_standard | allowed | P2 | P0 (skip) | ✗ MISS |
| 12 | 06_tools__var_demanding | required | P2 | P3 (deep) | ~ NEAR |
| 13 | 08_react_practice__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 14 | 08_react_practice__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 15 | 08_react_practice__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |
| 16 | 09_RAG__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 17 | 09_RAG__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 18 | 09_RAG__var_demanding | allowed | P2 | P3 (deep) | ~ NEAR |
| 19 | 10_memory_knowledge_access__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 20 | 10_memory_knowledge_access__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 21 | 10_memory_knowledge_access__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |
| 22 | 11_multimodal__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 23 | 11_multimodal__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 24 | 11_multimodal__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |

**Overall:** n=24 · exact=11 (46%) · near=11 (46%) · miss=2 (8%) · no-oracle/error=0
**Ordinal MAE:** 0.625
**Reward-regret** (allowed/required only, n=16; 8 forbidden excluded): mean=0.1186, max=0.7149

### Confusion matrix (Train)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 8 | 0 | 2 | 0 | 10 |
| P1 light | 0 | 0 | 9 | 0 | 9 |
| P2 standard | 0 | 0 | 3 | 0 | 3 |
| P3 deep | 0 | 0 | 2 | 0 | 2 |

### Baselines (Train)

- Oracle distribution: P0=10, P1=9, P2=3, P3=2
- Majority-class baseline (always P0 skip): 41.7% (10/24)
- Uniform-random baseline (1/4): 25.0%
- Weighted-random baseline: 33.7%

### By difficulty tier (Train)

| Variant tier | n | Exact | Exact+Near | Regret (mean / max) |
|---|---|---|---|---|
| var_minimal | 8 | 8/8 | 8/8 | n/a (all policy-forced) |
| var_standard | 8 | 0/8 | 6/8 | mean=0.1050, max=0.2841 |
| var_demanding | 8 | 3/8 | 8/8 | mean=0.1321, max=0.7149 |

---

## Combined — Train + Test (n=40)

- n=40 · exact=14 (35%) · near=21 (52%) · miss=5 (12%) · no-oracle/error=0
- Reward-regret (allowed/required only, n=31; 9 forbidden excluded): mean=0.1169, max=0.7149

---

## Detailed results

Each entry below preserves Grok's full reasoning, decision drivers, and risk flags for that planning decision.

### Test split (n=16)

#### 1. 04_structured_outputs — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P2 (standard) |
| Rewards (P0/P1/P2/P3) | 0.6067 / 0.6687 / 0.6707 / 0.6407 |
| Regret (counted) | 0.0 (0.0) |

**Reasoning:** 32 unbacked anchors and high must-ev totals (~31) concentrated in large-budget sections (S4:13 must-ev at 40%, S3:8 at 20%) create concrete evidence gaps that prevent writing without sourced facts, despite solid cov in S2/S4. S6 (need_depth 7, cov 1) and S1 (need_depth 6, cov 2) add depth pressure; dominant gap is balanced. P2 fills mandatory evidence via depth-then-breadth without overkill on brief sections or 0% S7.

**Decision drivers:** high must-ev in high-budget sections · 32 unbacked anchors · need_depth in S1/S3/S6 · balanced dominant gap

**Risk flags:**
- notebook/golden sources may already suffice for code-heavy sections
- S2 brief flag could limit absorption
- over-exploring low-budget conclusion

#### 2. 07_reasoning_planning — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.2886 / 0.2008 / 0.1839 / 0.1268 |
| Regret (counted) | 0.1047 (0.1047) |

**Reasoning:** 42 unbacked anchors and dominant depth gaps drive the choice; S4 (26/8 need, 14% budget, 3 must-ev, 8 orphans) and S5 (18/6 need, 22% budget, 2 must-ev) are large, evidence-heavy sections with low existing cov (6·1 and 5·0). S7 is already strong (5·2 cov on 24% budget); S1's brief flag caps its exploration. This matches 2-round depth-then-breadth to fill must-ev from golden sources (ReAct paper, Anthropic guide) without P3 overkill.

**Decision drivers:** unbacked anchors 42 · depth gaps in S4/S5 · must-ev total 11 · dominant depth signal

**Risk flags:**
- brief constraint on high-need S1
- possible source saturation on diagrams/pros-cons

#### 3. 13_agent_framework — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P3 (deep) |
| Rewards (P0/P1/P2/P3) | 0.6446 / 0.6716 / 0.5805 / 0.6939 |
| Regret (counted) | 0.1133 (0.1133) |

**Reasoning:** Dominant depth gap (need d/b skewed high in S1–S4), 42 article-wide unbacked anchors, and must-ev spikes (15 in 18% S4 landscape survey, 6 in S3 axes, 3–7 in intros) create concrete evidence needs for adoption metrics, golden-source citations, and capstone mappings. Deep-dive sections (S5–S12) already show solid cov (4–5 depth, 0 orphans), so targeted depth-then-breadth fills the high-budget gaps without waste. External-evidence ALLOWED but not required; P3 unwarranted as gaps are not uniformly large.

**Decision drivers:** must-ev & depth in S4/S1–S3 · 42 unbacked anchors · dominant depth gap · strong later-section cov

**Risk flags:**
- golden sources may already cover more than table implies
- future-dated pepy metrics could inflate perceived gap

#### 4. 14_agent_system_design — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.5938 / 0.6859 / 0.5966 / 0.5837 |
| Regret (counted) | 0.0894 (0.0894) |

**Reasoning:** Dominant gap is depth with 42 article-wide unbacked anchors; S2 (31% budget, need_depth 29, must-ev 7, 9 orphans) and S4 (28% budget, need_depth 36, must-ev 6, 11 orphans) show large evidence-driven shortfalls exactly where writing spend is highest. S3 adds quantitative scaling examples that require cited benchmarks/numbers (must-ev 5). S5/S6 already strong with low needs, so full P3 unnecessary. This justifies depth-then-breadth gap-filling over cheaper P1.

**Decision drivers:** unmet_depth_large_sections · must-ev_total_27 · 42_unbacked_anchors · dominant_depth_gap

**Risk flags:**
- some anchors satisfiable from listed golden sources without new rounds
- S1/S3 images may not need fresh evidence

#### 5. 29_evaluation_metrics — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.5118 / 0.7876 / 0.7138 / 0.685 |
| Regret (counted) | 0.0738 (0.0738) |

**Reasoning:** Dominant depth gaps (article-wide need_depth 13-32) plus 47 unbacked anchors and must-ev=1-2 in S3-S5 (18%+ budgets) show concrete missing evidence for business-metric examples, overfitting cases, and LLM-judge tradeoffs; cov is only mid-6/8 depth in weakest high-budget sections (S2/S5) despite golden sources already pulled. S2 brief flag and ALLOWED (not required) external policy keep us from P3; default cheaper arm is overridden by size of depth mandate and orphans.

**Decision drivers:** dominant_depth_gaps · 47_unbacked_anchors · must-ev_in_S3-S5 · moderate_cov_6d_in_large_sections

**Risk flags:**
- S2 brief flag may limit absorption
- golden sources may already address some depth
- over-escalation if must-ev examples are generic

#### 6. 31_CI — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.6284 / 0.6901 / 0.5939 / 0.6053 |
| Regret (counted) | 0.0962 (0.0962) |

**Reasoning:** 42 unbacked anchors and dominant depth gaps drive choice; largest-budget sections (S6 31% with must-ev 5, S5 17% with must-ev 5, S2 14% with must-ev 6) show low cov (3-5 depth) vs high need (8-13 depth) requiring sourced tool/config evidence from golden sources. P2 depth-first then breadth fills these without P3 cost, as S5 is brief, S9/S7 already strong, and small-budget sections (S1/S8/S9 <5%) add little justification for deeper rounds.

**Decision drivers:** unbacked_anchors_42 · high_must-ev_in_large_sections · dominant_depth_gaps · section_budgets_S6_S5_S2

**Risk flags:**
- S5 brief flag may limit absorption
- notebook/golden sources might already suffice for some configs
- possible over-coverage in low-budget intro/conclusion

#### 7. Bird_Eye_Extreme — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4915 / 0.7266 / 0.5656 / 0.4522 |
| Regret (counted) | 0.161 (0.161) |

**Reasoning:** 31 unbacked anchors and dominant depth gap (needs 17–25 vs cov only 3–4d/2b) plus high must-ev (4–6 per section, esp. S3 at 29% budget) show concrete sizeable gaps in key claims, quotes, numbers, and transcriptomic/evolutionary evidence. S1+S3 are weakest; external-evidence allowed. P2 depth-first then breadth buys the missing sourced facts without P3 overkill on a 2050-word theory piece.

**Decision drivers:** unbacked_anchors_31 · dominant_depth_gap · must-ev_4-6 · S3_budget+need_25 · low_cov_3-4d

**Risk flags:**
- local_golden_sources_may_already_cover_some_quotes
- S2/S4 stronger so marginal over-exploration there

#### 8. Dark_Dimension — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.814 / 0.6803 / 0.6923 / 0.6287 |
| Regret (counted) | 0.1217 (0.1217) |

**Reasoning:** 27 article-wide unbacked anchors, high must-ev (5/6/8 per section), and large unmet need_depth (12-14) despite partial cov (5-7) signal concrete evidence gaps, especially in high-budget S2 (34%) and S3 (46%); dominant depth gap plus mandatory named sources (Khoury, Vafa, DESI, Andriot quotes) justify depth-first pass, but brief flags on S1/S3 and 'allowed not required' policy prevent P3 escalation.

**Decision drivers:** must-ev · unbacked_anchors · need_depth · dominant_gap_type

**Risk flags:**
- brief=yes on large S3 may cap absorption
- existing golden sources might already cover more than numbers show

#### 9. Distinct_AI_Models — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.625 / 0.7917 / 0.6398 / 0.7135 |
| Regret (counted) | 0.152 (0.152) |

**Reasoning:** Article-wide 30 unbacked anchors + dominant depth gap; all sections show high need_depth (18-21) paired with must-ev (3-4) for named papers/quotes/experiments (e.g. Huh design, Isola/Efros quotes, Firth application). Weakest S3/S4 drive need despite S1/S3 'brief' constraint; existing cov only 5·2-3 out of 8/6 confirms sizeable sourced-evidence shortfalls in a 100% theory 2000-word piece.

**Decision drivers:** high need_depth + must-ev · 30 unbacked anchors · depth-dominant gaps · weakest S3/S4

**Risk flags:**
- brief sections may limit absorbable depth
- provided .md sources might already address some orphans beyond numeric cov

#### 10. Earth_Oceans_Origin — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P1 |
| Oracle | P3 (deep) |
| Rewards (P0/P1/P2/P3) | 0.4707 / 0.5086 / 0.5917 / 0.6133 |
| Regret (counted) | 0.1046 (0.1046) |

**Reasoning:** Coverage already strong (6-7/8 depth, 3/6 breadth) with zero orphans; dominant gap is breadth not depth and all but S4 are explicitly brief. However 38 article-wide unbacked anchors plus high must-ev (6 in 37% S2, 5 in 35% S3) on named missions, papers, quotes and experiments justify one balanced round; external-evidence is only ALLOWED, not required, so no escalation past P1.

**Decision drivers:** high must-ev in largest sections · 38 unbacked anchors · breadth-dominant gaps · already-high cov + brief constraints

**Risk flags:**
- local golden-source files may already cover must-ev
- under-counting qualitative depth for specific experimental quotes in S3

#### 11. Gravity_Entropy — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.646 / 0.7228 / 0.6604 / 0.5609 |
| Regret (counted) | 0.0623 (0.0623) |

**Reasoning:** 32 unbacked anchors and 18 must-ev bullets (esp. 5 each in S3/S4) signal large evidence gaps; dominant depth pressure (S2 need 16/8 cov 4·4; S5 weakest) plus explicit quote/derivation demands in guideline justify depth-first round then breadth, but S2/S3 'brief=yes' caps escalation and total 2000-word budget keeps it from P3.

**Decision drivers:** unbacked_anchors_32 · must_ev_high · depth_dominant_S2_S5 · high_orphans

**Risk flags:**
- brief sections limit extra absorption
- arxiv golden sources may already hold quotes

#### 12. HNSW — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4839 / 0.7672 / 0.5239 / 0.5556 |
| Regret (counted) | 0.2433 (0.2433) |

**Reasoning:** 47 article-wide unbacked anchors with dominant depth gaps; S4 (46% budget) shows need_depth=40 + must-ev=9 and cov only 4/8, S2 (35%) has need_depth=32 + must-ev=4 and cov 3/8. Golden sources (HNSW paper, skip-list PDF, Faiss HNSW.cpp) plus empirical Sift1M sweeps clearly remain under-covered on mandatory mechanics/benchmarks. Brief flags on S2 and ALLOWED (not required) policy keep us from P3; gaps are too large for P1.

**Decision drivers:** 47 unbacked anchors · high must-ev in S4/S2 · dominant depth gaps in 81% budget · low depth cov (3-4/8)

**Risk flags:**
- brief=yes on S2 might limit absorption
- golden sources may already address some orphans not reflected in cov

#### 13. Insects_Consciousness — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.5434 / 0.8553 / 0.5461 / 0.7229 |
| Regret (counted) | 0.3092 (0.3092) |

**Reasoning:** 22 unbacked anchors and high must-ev (4-6 per section) show concrete depth gaps on specific experiments, expert quotes (Sebo, Andrews, Godfrey-Smith) and behavioral citations required by the guideline; dominant gap type is depth, weakest sections are the two largest (S2 45%, S3 24%) with need_d scores of 14 and cov_d stuck at 6/8; external-evidence is only ALLOWED so default to cheaper arm rules out P3 despite sizeable gaps.

**Decision drivers:** unbacked_anchors_22 · must-ev_15_total · dominant_depth_gap · S2+S3_budget_69pct

**Risk flags:**
- coverage numbers may already incorporate golden sources
- guideline length could tempt over-researching non-mandatory breadth

#### 14. Space-Time_QECC — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.462 / 0.602 / 0.5076 / 0.5188 |
| Regret (counted) | 0.0944 (0.0944) |

**Reasoning:** S2 zero coverage + need 8/6 and must-ev 4 is the decisive hole; 27 unbacked anchors and 21 total must-ev confirm sizeable balanced gaps, yet brief flags on large sections and strong S4 coverage keep it from P3

**Decision drivers:** S2 zero-cov + max-depth need · 21 must-ev · 27 unbacked anchors · balanced gaps + brief constraints

**Risk flags:**
- golden sources may not contain all quoted remarks
- S5 small budget could still hide missed dS/CFT refs

#### 15. State_of_LLM_Reasoning — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.449 / 0.4057 / 0.4243 / 0.3653 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** The brief states external-evidence policy = FORBIDDEN in all-caps with the explicit note that exploration output cannot be used, so only skip is valid. This matches the hard constraint that overrides all per-section gaps (high need_depth in S2/S1, 72 unbacked anchors, many must-ev >3). Existing coverage is treated as already sufficient under the no-external-evidence rule.

**Decision drivers:** external-evidence-forbidden · hard-constraint-override

**Risk flags:**
- policy misread as required
- internal sources later deemed insufficient

#### 16. Understanding_Reasoning_LLMs — ✓ EXACT

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P2 (standard) |
| Rewards (P0/P1/P2/P3) | 0.4603 / 0.5987 / 0.6078 / 0.527 |
| Regret (counted) | 0.0 (0.0) |

**Reasoning:** All 8 sections show 0·0 coverage against uniform 8/6 need and 26 must-ev bullets (especially S5 at 45% budget with 8 must-ev, S7 at 14% with 5). 52 unbacked anchors and balanced gap type confirm evidence is entirely missing for the theory-heavy DeepSeek pipeline, benchmarks, emergence details, and budget methods (Sky-T1/TinyZero/journey learning). P0/P1 insufficient; P3 not justified given 'brief' flags on S1/S5 and 'allowed' (not required) external policy.

**Decision drivers:** zero coverage across all sections · high must-ev in dominant S5+S7 · 52 unbacked anchors · balanced gaps with depth mandates

**Risk flags:**
- golden sources may already suffice for core claims
- brief sections could receive excess depth
- over-reliance on DeepSeek paper vs. broader comparisons

### Train split (n=24)

#### 1. 02_workflows_vs_agents__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.4962 / 0.6931 / 0.45 / 0.475 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** External-evidence policy is explicitly FORBIDDEN, triggering the hard constraint that mandates P0. All sections carry 'must stay brief' flags; the guideline repeatedly stresses conceptual overview with surface-level treatment and no external examples or depth required. Per-section gaps exist (esp. S1/S6 depth, 48 unbacked anchors) but cannot be addressed when exploration output is unusable.

**Decision drivers:** external-evidence-forbidden · must-stay-brief everywhere · conceptual-overview mandate

**Risk flags:**
- coverage shortfalls in S1/S6 could weaken framing if internal sources prove thin

#### 2. 02_workflows_vs_agents__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.6292 / 0.794 / 0.7335 / 0.51 |
| Regret (counted) | 0.0605 (0.0605) |

**Reasoning:** 47 unbacked anchors and dominant depth gap drive escalation; S3 (17% budget, need 16/3, must-ev 3) and S5 (30% budget, must-ev 4) show sizeable evidence needs for concrete examples, decision criteria, and hybrid patterns drawn from golden sources. S1/S2 weakest but S1 is brief and cannot absorb heavy research; coverage already at 7·6–8·6 rules out P3 while ruling out P0/P1.

**Decision drivers:** unbacked anchors · must-ev in S3/S5 · dominant depth gap · weighted budgets

**Risk flags:**
- S5 cov already strong
- brief sections limit absorption
- policy allows but does not require evidence

#### 3. 02_workflows_vs_agents__var_demanding — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4835 / 0.5722 / 0.5121 / 0.4478 |
| Regret (counted) | 0.0601 (0.0601) |

**Reasoning:** 48 article-wide unbacked anchors + 16 must-ev bullets (S6=6, S3/S5=3 each) show sizeable depth gaps despite cov 7-8·6 scores; dominant gap type is depth in high-budget S4 (18%, need 7/3, must-ev=2) and S5 (29%, need 6/3, must-ev=3). Guideline requires named production examples, failure modes, Gemini CLI/Perplexity details and mermaid-anchored patterns, which the exploitation pass only partially sourced. External policy=ALLOWED; 2-round depth-then-breadth fills concrete gaps without P3 overkill on already-strong S1/S3.

**Decision drivers:** high must-ev total · 48 unbacked anchors · depth-dominant gaps in S4/S5/S6 · specific real-world example mandates

**Risk flags:**
- fresh Aug-2025 claims may need live web data
- S6 conclusion could still under-source if examples stay shallow

#### 4. 03_context_engineering__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.7625 / 0.7783 / 0.6314 / 0.7269 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** Hard constraint: external-evidence policy explicitly marked FORBIDDEN. Exploration output cannot be used in the article, making any non-zero preset wasted effort. All sections labeled 'must stay brief'; coverage already meets or exceeds most need d/b values (e.g. S5 7·4 vs 7/5, S7 7·5 vs 7/4); guideline stresses conceptual overview with no external libs, benchmarks or production examples allowed.

**Decision drivers:** external-evidence-forbidden · all-sections-brief · high-existing-cov

**Risk flags:**
- unbacked anchors still high (48) but cannot be filled

#### 5. 03_context_engineering__var_standard — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.6414 / 0.6119 / 0.5843 / 0.5143 |
| Regret (counted) | 0.0571 (0.0571) |

**Reasoning:** Dominant depth gaps (68 unbacked anchors article-wide) and high must-ev counts concentrate in largest-budget sections: S6 (55d need/20% budget/6 must-ev/18 orphans, strategies+diagrams) and S7 (55d/15%/3 must-ev/18 orphans, use-cases+prompt+stack). Weaker cov in S4/S1/S2/S8 adds up; S3/S5 already strong. P2's depth-first pass targets must-ev sourcing from golden LangChain/LlamaIndex/arXiv refs, then breadth, without P3 overkill or P1 insufficiency.

**Decision drivers:** high need_depth in S6/S7 · must-ev totals ~27 · 68 unbacked anchors · dominant depth gap · section budgets

**Risk flags:**
- golden sources may lack specific benchmarks
- some sections allow intuitive 7yo explanations
- policy is allowed not required

#### 6. 03_context_engineering__var_demanding — ~ NEAR (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4295 / 0.5055 / 0.477 / 0.4368 |
| Regret (counted) | 0.0285 (0.0285) |

**Reasoning:** External-evidence REQUIRED + 52 unbacked anchors + high must-ev (esp. S6=11, S4=6; total ~38) in large-budget sections (S6 20%, S3/S4/S7 15% each) create sizeable depth-dominant gaps despite strong existing cov (mostly 7-8·6). Additional requirements demand named production examples, failure modes, benchmarks. Modest need d/b (3-4 range in core sections) and strong S3/S5 keep it from P3; defaults to cheaper than deep but exceeds light for meaningful gap-filling.

**Decision drivers:** external-required · must-ev totals · unbacked anchors=52 · depth gaps in high-budget sections

**Risk flags:**
- existing high cov may mean some must-ev already partially sourced
- S1/S8 weaknesses could be addressed with less than full standard round

#### 7. 05_workflow_patterns__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.872 / 0.8408 / 0.796 / 0.746 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** The brief explicitly states External-evidence policy: FORBIDDEN and notes that exploration output cannot be used, directly triggering the hard constraint that mandates P0. All sections are flagged 'brief: yes' and the guideline demands only surface-level conceptual treatment (~1250 words total) with no external libraries, benchmarks, or production examples permitted. Per-section gaps exist but cannot be addressed via exploration; dominant depth gaps and 52 unbacked anchors are irrelevant under the policy.

**Decision drivers:** external-evidence-forbidden · all-sections-brief · conceptual-overview-mandate

**Risk flags:**
- policy misread as required
- future-lessons leakage

#### 8. 05_workflow_patterns__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.6149 / 0.8085 / 0.7092 / 0.7192 |
| Regret (counted) | 0.0992 (0.0992) |

**Reasoning:** Dominant gap is depth with 52 article-wide unbacked anchors; S1/S2 (25% combined budget) show extreme need_d (40/44) plus 27 orphans and must-ev=2 in S1, while S4/S7 add further must-ev=2 each. S3/S6 already strong (cov 7·5, low need_d). External-evidence ALLOWED but not required; golden sources exist for theory benefits/downsides. Standard (depth→breadth) targets concrete evidence gaps in weakest sections without P3 overkill.

**Decision drivers:** high_depth_needs_S1_S2 · must_ev_aggregate_8 · 52_unbacked_anchors · dominant_depth_gap

**Risk flags:**
- theory_only_S2 may need less evidence than numbers suggest
- notebook_code already supplies most practice examples

#### 9. 05_workflow_patterns__var_demanding — ~ NEAR (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.5417 / 0.6549 / -0.06 / 0.4766 |
| Regret (counted) | 0.7149 (0.7149) |

**Reasoning:** S1 and S2 show the largest gaps (need_depth=9 each, must-ev=7 each, 4 total orphans) against only mid-5 coverage despite high writing budgets (15%+12%) and many 'must cover in depth' bullets on debugging, modularity, accuracy, and information-loss; article-wide 42 unbacked anchors plus 27 must-ev bullets (including S7's 6) confirm dominant depth gaps and REQUIRED external-evidence policy. S3/S4/S6/S7 already sit at cov 5-6 with low need and no orphans, so extra rounds would waste budget on practice sections that must stay brief. P2's depth-first then breadth pass therefore buys the mandatory sourced examples, failure modes, and industry anchors at acceptable cost.

**Decision drivers:** high must-ev in S1/S2 (27 total) · 42 unbacked anchors + dominant depth gap · REQUIRED external-evidence policy · strongest coverage already in S4/S7

**Risk flags:**
- under-estimating glue-code or rate-limit depth in S2/S4
- if production-code mandates need more than 2 rounds of breadth

#### 10. 06_tools__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.6903 / 0.6818 / 0.557 / 0.3205 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** The brief explicitly states external-evidence policy = FORBIDDEN and notes that exploration output cannot be used, triggering the hard constraint that mandates P0. All sections carry 'must stay brief' flags, the article is scoped as a conceptual overview with strict 1490-word ceiling and bans on external libraries/case studies, and existing coverage already meets the surface-level guideline intent.

**Decision drivers:** external-evidence policy = forbidden · brevity mandates across sections · surface-level conceptual scope

**Risk flags:**
- high need_depth in S3/S4 could tempt override but is barred by policy

#### 11. 06_tools__var_standard — ✗ MISS

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.5598 / 0.4525 / 0.5707 / 0.5184 |
| Regret (counted) | -0.0109 (-0.0109) |

**Reasoning:** Article-wide 52 unbacked anchors and depth-dominant gaps; S3 (26% budget) shows extreme unmet depth (57), 18 must-ev + 18 orphans despite 5·2 cov, S2 adds 40 depth need + 12 orphans, S4 contributes 25 depth + 9 must-ev. These concrete gaps in the two weakest, highest-budget sections justify depth-first gap-filling over P1; S5/S7 already strong so no need for P3.

**Decision drivers:** 52 unbacked anchors · S3/S2 depth + must-ev spikes · 26%+9% budget weighting · depth-dominant economics

**Risk flags:**
- brief=yes on S3 may constrain extra evidence absorption
- notebook code may already satisfy some must-ev implicitly

#### 12. 06_tools__var_demanding — ~ NEAR (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P3 (deep) |
| Rewards (P0/P1/P2/P3) | 0.3794 / 0.4551 / 0.4288 / 0.4949 |
| Regret (counted) | 0.066 (0.066) |

**Reasoning:** External-evidence REQUIRED forces >=P1. 42 unbacked anchors, dominant depth gaps, high must-ev (4 in S8, 3 in S9) plus explicit "must cover in depth" mandates for mechanisms/examples/failure modes in the 11% S8 and conclusion cannot be met from existing cov (S8 5·4, S9 4·3). Weakest S1 (need_d 14) and S4 (need_d 9, 15% budget) add pressure; strongest sections (S5/S7) already solid so no need for P3. P2 (depth→breadth) targets the concrete evidence shortfalls without excess.

**Decision drivers:** external_required · must_ev_S8_S9 · 42_unbacked_anchors · dominant_depth_gaps · weak_S1_S4

**Risk flags:**
- golden_sources may already satisfy some must-ev
- code-heavy sections may need less web depth than numbers imply

#### 13. 08_react_practice__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.6543 / 0.1224 / 0.0647 / 0.3828 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** The brief states external-evidence policy FORBIDDEN with the explicit note that exploration output cannot be used, triggering the hard constraint that overrides all gap signals (48 unbacked anchors, dominant depth gaps in S3/S1, must-ev counts). Multiple sections carry 'must stay brief' flags and the guideline reinforces no external sources, benchmarks or libraries.

**Decision drivers:** external-evidence policy FORBIDDEN · hard constraint override · brevity mandates across sections

**Risk flags:**
- policy misread as only partial ban
- depth gaps left unaddressed in S5 (29% budget)

#### 14. 08_react_practice__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.3892 / 0.5431 / 0.259 / 0.3283 |
| Regret (counted) | 0.2841 (0.2841) |

**Reasoning:** 42 unbacked anchors, S1/S3 weakest (cov 2·1/3·1 vs need 6/5/5/5), S4/S6 high must-ev (12/9) on 20%/15% budgets; S5 already 5·4 and brief=yes so no extra rounds needed. Balanced gaps + ALLOWED policy make 2-round depth→breadth optimal.

**Decision drivers:** unbacked_anchors_42 · must_ev_in_large_sections · low_depth_in_S1_S3 · S5_strong_and_brief

**Risk flags:**
- notebook_code_may_suffice_as_primary_evidence
- golden_sources_may_not_add_new_numbers

#### 15. 08_react_practice__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P2 (standard) |
| Rewards (P0/P1/P2/P3) | 0.4094 / 0.4042 / 0.5843 / 0.4348 |
| Regret (counted) | 0.0 (0.0) |

**Reasoning:** 42 unbacked anchors + dominant depth gaps (needs 13-23) in large-budget sections (S5 28%/22, S1 9%/23, S3 14%/21) with 29 total orphans and 4 must-ev bullets clearly exceed light coverage; external-evidence REQUIRED and guideline demands named production examples/failure modes/industry anchors. S4/S6 already strong and S5 marked brief prevent escalation to deep; 2-round depth-then-breadth is the minimal sufficient preset.

**Decision drivers:** unbacked_anchors_42 · dominant_depth_gaps · must-ev_in_4_sections · external_required · high_budget_weak_sections

**Risk flags:**
- S5 brief flag may limit absorption
- golden sources might overlap some orphans
- depth pressure could be partly qualitative not evidential

#### 16. 09_RAG__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.7317 / 0.5683 / 0.4467 / 0.3627 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** The brief states external-evidence policy FORBIDDEN and explicitly notes 'exploration output cannot be used, so the only valid choice is skip'. Hard constraint requires P0 when external evidence is forbidden; this overrides all per-section gaps (need d/b, must-ev counts, 42 unbacked anchors). Guideline reinforces surface-level conceptual overview with no external libraries, benchmarks or real-world examples allowed.

**Decision drivers:** external-evidence-forbidden · hard-constraint-override · surface-level-guideline

**Risk flags:**
- policy misread as required instead of forbidden
- underestimating must-ev pressure in S3/S4

#### 17. 09_RAG__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4057 / 0.4394 / 0.4255 / 0.3807 |
| Regret (counted) | 0.0139 (0.0139) |

**Reasoning:** 48 unbacked anchors and dominant depth gap signal clear missing evidence; S3 (20% budget) shows must-ev=8 plus need_depth=6 despite decent cov 5·4, while S4 (29% budget) carries must-ev=6. Brief-marked S1/S2 have large needs but are down-weighted per economics. This is sizeable evidence-driven depth pressure in the two highest-budget sections, justifying 2-round depth-then-breadth over P1 touch-up or P0 skip; P3 is excessive given strong existing cov in S4/S5.

**Decision drivers:** unbacked_anchors_48 · must_ev_in_S3_S4 · dominant_depth_gaps · high_budget_sections_S3_S4

**Risk flags:**
- brief sections may limit absorption
- golden sources might already address some must-ev

#### 18. 09_RAG__var_demanding — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P3 (deep) |
| Rewards (P0/P1/P2/P3) | 0.3767 / 0.5314 / 0.3625 / 0.5497 |
| Regret (counted) | 0.1872 (0.1872) |

**Reasoning:** 32 unbacked anchors article-wide + dominant depth gap drive escalation; S3 (must-ev 8, need_depth 5) and S2/S6 (must-ev 4-5, need_depth 7) show concrete sizeable gaps in high-budget sections requiring named tools/models/benchmarks. S4/S5 already strong (cov 7·5 / 7·4); S1 marked brief so limited upside. This matches 2-round depth-then-breadth for meaningful gap-filling without full P3 cost.

**Decision drivers:** unbacked_anchors_32 · must-ev_in_S3_S2_S6 · dominant_depth_gaps · mixed_section_strength

**Risk flags:**
- S1 brief constraint may dilute exploration value
- golden sources might already cover some must-ev items

#### 19. 10_memory_knowledge_access__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.6893 / 0.64 / 0.6446 / 0.5982 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** Hard constraint: external-evidence policy = FORBIDDEN, which mandates P0 regardless of other signals. All 7 sections are flagged 'brief' and cannot absorb extra research; dominant gaps are in low-budget intro sections (S1 11%, S4 14%) while strongest coverage is already in the code-heavy S5/S6 that match the guideline's 'use the provided Notebook' rule. The guideline repeatedly stresses conceptual overview, surface-level only, no external libs/cases, and a 1500-word hard ceiling.

**Decision drivers:** external-evidence-forbidden · all-sections-brief · conceptual-overview-mandate

**Risk flags:**
- unbacked anchors (35) could force light prose patching
- S1/S4 depth gaps might feel thin without any sourcing

#### 20. 10_memory_knowledge_access__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.4776 / 0.5534 / 0.4779 / 0.4473 |
| Regret (counted) | 0.0754 (0.0754) |

**Reasoning:** 32 article-wide unbacked anchors + dominant depth gap; S1/S3/S4 show large unmet depth (25/21/20), must-ev counts (2-3), and orphans (8/6/6) on 15% budgets each. S6/S7 already strong (need 7/3, cov 7·6/5·6); S5 brief=yes so cannot absorb research. Guideline supplies narrative but not the missing sourced evidence for semantic/episodic/procedural details and storage trade-offs.

**Decision drivers:** depth-dominant gaps · high must-ev in S3/S4/S5 · 32 unbacked anchors · weakest sections S1/S3

**Risk flags:**
- S5 brief constraint may limit usable depth
- guideline already dense—risk of redundant evidence

#### 21. 10_memory_knowledge_access__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P2 (standard) |
| Rewards (P0/P1/P2/P3) | 0.3478 / 0.5424 / 0.5895 / 0.5482 |
| Regret (counted) | 0.0 (0.0) |

**Reasoning:** 28 unbacked anchors and dominant depth gaps drive the choice; high must-ev (5 in both S4 and S5, which together are 34% budget) plus S1's 7/0 need_depth and weakest-section status create sizeable evidence demands that a single light round cannot satisfy. Coverage is already strong (mostly 7-8·6), orphans are low, and no section is marked brief, so 2-round depth-then-breadth fills the concrete must-ev shortfalls without P3 overkill. External-evidence REQUIRED also rules out P0.

**Decision drivers:** 28 unbacked anchors · high must-ev in large-budget sections · S1 7/0 depth gap + weakest sections · external-evidence REQUIRED

**Risk flags:**
- golden sources may already address some must-ev
- if many anchors are qualitative rather than factual, depth pressure could be lower

#### 22. 11_multimodal__var_minimal — ✓ EXACT (policy: forbidden)

| Field | Value |
|---|---|
| Policy | **forbidden** |
| Grok preset | P0 |
| Oracle | P0 (skip) |
| Rewards (P0/P1/P2/P3) | 0.369 / 0.3362 / 0.3024 / 0.2631 |
| Regret (counted) | 0.0 (excluded — forbidden) |

**Reasoning:** Hard constraint: external-evidence policy explicitly marked FORBIDDEN, which overrides all other signals and mandates P0. Existing coverage is already high (e.g. S5 8·4 vs need 3/2, S3/S4 6·3 vs 5/3); multiple sections carry 'must stay brief' flags and the guideline stresses conceptual overview only. 32 unbacked anchors exist but cannot be addressed via exploration.

**Decision drivers:** external-evidence policy = forbidden · high cov d·b scores · brevity mandates across 6/8 sections

**Risk flags:**
- unaddressed depth gaps in S8/S1
- 32 orphans remain but policy blocks use

#### 23. 11_multimodal__var_standard — ~ NEAR

| Field | Value |
|---|---|
| Policy | allowed |
| Grok preset | P2 |
| Oracle | P1 (light) |
| Rewards (P0/P1/P2/P3) | 0.6854 / 0.6666 / 0.4056 / 0.6013 |
| Regret (counted) | 0.261 (0.261) |

**Reasoning:** 42 unbacked anchors and dominant depth gap signal clear missing evidence; S3 (23% budget, need_d=6, must-ev=3, cov=5·5) and weakest sections S1 (need_d=10, cov=4·4) + S7 (need_d=7, cov=4·4) show sizeable depth shortfalls in high-impact areas, plus 11 total must-ev bullets (esp. benchmarks/numbers in S2/S3/S5). S5 already strong (cov=8·5) and brief, so no need for P3; P1 too light for the concrete gaps.

**Decision drivers:** unbacked_anchors_42 · dominant_depth_gaps · must_ev_in_S3_S5 · high_need_in_S1_S7_S3

**Risk flags:**
- existing golden sources may already address some depth
- brief sections limit absorption
- over-exploration if must-ev are non-critical

#### 24. 11_multimodal__var_demanding — ✓ EXACT (policy: required)

| Field | Value |
|---|---|
| Policy | **required** |
| Grok preset | P2 |
| Oracle | P2 (standard) |
| Rewards (P0/P1/P2/P3) | 0.4383 / 0.5775 / 0.6064 / 0.6104 |
| Regret (counted) | 0.0 (0.0) |

**Reasoning:** External-evidence REQUIRED rules out P0; 38 unbacked anchors + dominant depth gap + high must-ev in large-budget sections (S2: must-ev=5/need_depth=7 at 13%, S3:4 at 23%, S4:4 at 18%, S5:6 at 15%) create sizeable evidence-driven gaps that the exploitation pass left open (weakest S1/S2). Strong existing cov (7–8) in S3/S4/S5 limits need to targeted depth-then-breadth, making P2 the sweet spot over cheap P1 or costly P3.

**Decision drivers:** external-required · 38 unbacked anchors · high must-ev in high-budget sections · dominant depth gaps

**Risk flags:**
- golden sources may already address some ColPali/OCR benchmarks
- high-need but tiny S8 (2%) could inflate perceived gaps
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.1169  max=0.7149