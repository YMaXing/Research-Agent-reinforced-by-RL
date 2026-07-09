# RL-Only Planner Train & Test Results

All decisions in this dataset are RL-only (no Grok arbitration; `chosen_by` = RL throughout).

## Test summary — held-out, primary metric (n=16)

| # | Variant | RL preset | Oracle | Verdict |
|---|---|---|---|---|
| 1 | 04_structured_outputs | P1 | P2 (standard) | ~ NEAR |
| 2 | 07_reasoning_planning | P0 | P0 (skip) | ✓ EXACT |
| 3 | 13_agent_framework | P0 | P3 (deep) | ✗ MISS |
| 4 | 14_agent_system_design | P1 | P1 (light) | ✓ EXACT |
| 5 | 29_evaluation_metrics | P0 | P1 (light) | ~ NEAR |
| 6 | 31_CI | P0 | P1 (light) | ~ NEAR |
| 7 | Bird_Eye_Extreme | P0 | P1 (light) | ~ NEAR |
| 8 | Dark_Dimension | P0 | P0 (skip) | ✓ EXACT |
| 9 | Distinct_AI_Models | P0 | P1 (light) | ~ NEAR |
| 10 | Earth_Oceans_Origin | P1 | P3 (deep) | ✗ MISS |
| 11 | Gravity_Entropy | P1 | P1 (light) | ✓ EXACT |
| 12 | HNSW | P0 | P1 (light) | ~ NEAR |
| 13 | Insects_Consciousness | P0 | P1 (light) | ~ NEAR |
| 14 | Space-Time_QECC | P0 | P1 (light) | ~ NEAR |
| 15 | State_of_LLM_Reasoning (policy: forbidden) | P0 | P0 (skip) | ✓ EXACT |
| 16 | Understanding_Reasoning_LLMs | P0 | P2 (standard) | ✗ MISS |

**Overall:** n=16 · exact=5 (31%) · near=8 (50%) · miss=3 (19%) · no-oracle/error=0
**Ordinal MAE:** 0.938
**Reward-regret** (allowed/required only, n=15; 1 forbidden excluded): mean=0.1185, max=0.3118

### Confusion matrix (Test)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 3 | 0 | 0 | 0 | 3 |
| P1 light | 7 | 2 | 0 | 0 | 9 |
| P2 standard | 1 | 1 | 0 | 0 | 2 |
| P3 deep | 1 | 1 | 0 | 0 | 2 |

### Baselines (Test)

- Oracle distribution: P0=3, P1=9, P2=2, P3=2
- Majority-class baseline (always P1 light): 56.2% (9/16)
- Uniform-random baseline (1/4): 25.0%
- Weighted-random baseline: 38.3%

---

## Train summary — reference (n=24)

| # | Variant | Policy | RL preset | Oracle | Verdict |
|---|---|---|---|---|---|
| 1 | 02_workflows_vs_agents__var_minimal | forbidden | P1 | P0 (skip) | ~ NEAR |
| 2 | 02_workflows_vs_agents__var_standard | allowed | P1 | P1 (light) | ✓ EXACT |
| 3 | 02_workflows_vs_agents__var_demanding | allowed | P2 | P1 (light) | ~ NEAR |
| 4 | 03_context_engineering__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 5 | 03_context_engineering__var_standard | allowed | P1 | P0 (skip) | ~ NEAR |
| 6 | 03_context_engineering__var_demanding | required | P1 | P1 (light) | ✓ EXACT |
| 7 | 05_workflow_patterns__var_minimal | forbidden | P1 | P0 (skip) | ~ NEAR |
| 8 | 05_workflow_patterns__var_standard | allowed | P2 | P1 (light) | ~ NEAR |
| 9 | 05_workflow_patterns__var_demanding | required | P1 | P1 (light) | ✓ EXACT |
| 10 | 06_tools__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 11 | 06_tools__var_standard | allowed | P0 | P0 (skip) | ✓ EXACT |
| 12 | 06_tools__var_demanding | required | P3 | P3 (deep) | ✓ EXACT |
| 13 | 08_react_practice__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 14 | 08_react_practice__var_standard | allowed | P0 | P1 (light) | ~ NEAR |
| 15 | 08_react_practice__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |
| 16 | 09_RAG__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 17 | 09_RAG__var_standard | allowed | P0 | P1 (light) | ~ NEAR |
| 18 | 09_RAG__var_demanding | allowed | P3 | P3 (deep) | ✓ EXACT |
| 19 | 10_memory_knowledge_access__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 20 | 10_memory_knowledge_access__var_standard | allowed | P1 | P1 (light) | ✓ EXACT |
| 21 | 10_memory_knowledge_access__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |
| 22 | 11_multimodal__var_minimal | forbidden | P0 | P0 (skip) | ✓ EXACT |
| 23 | 11_multimodal__var_standard | allowed | P1 | P1 (light) | ✓ EXACT |
| 24 | 11_multimodal__var_demanding | required | P2 | P2 (standard) | ✓ EXACT |

**Overall:** n=24 · exact=17 (71%) · near=7 (29%) · miss=0 (0%) · no-oracle/error=0
**Ordinal MAE:** 0.292
**Reward-regret** (allowed/required only, n=16; 8 forbidden excluded): mean=0.0235, max=0.1539

### Confusion matrix (Train)

| Oracle ↓ \ Predicted → | skip | light | standard | deep | n |
|---|---|---|---|---|---|
| P0 skip | 7 | 3 | 0 | 0 | 10 |
| P1 light | 2 | 5 | 2 | 0 | 9 |
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
| var_minimal | 8 | 6/8 | 8/8 | n/a (all policy-forced) |
| var_standard | 8 | 4/8 | 8/8 | mean=0.0396, max=0.1539 |
| var_demanding | 8 | 7/8 | 8/8 | mean=0.0075, max=0.0601 |

---

## Combined — Train + Test (n=40)

- n=40 · exact=22 (55%) · near=15 (38%) · miss=3 (8%) · no-oracle/error=0
- Reward-regret (allowed/required only, n=31; 9 forbidden excluded): mean=0.0695, max=0.3118

---

## Detailed results

Full per-item metrics (rewards for all four presets, regret, entropy, confidence, and whether the reward floor was applied).

### Test split (n=16)

| # | Variant | Policy | RL | Oracle | Rewards (P0/P1/P2/P3) | Verdict | Regret (counted) | Entropy | Confidence | Floor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 04_structured_outputs | allowed | P1 | P2 (standard) | 0.6067 / 0.6687 / 0.6707 / 0.6407 | ~ NEAR | 0.002 (0.002) | 0.9968 | 0.533 | no |
| 2 | 07_reasoning_planning | allowed | P0 | P0 (skip) | 0.2886 / 0.2008 / 0.1839 / 0.1268 | ✓ EXACT | 0.0 (0.0) | 1.4413 | 0.5505 | yes |
| 3 | 13_agent_framework | allowed | P0 | P3 (deep) | 0.6446 / 0.6716 / 0.5805 / 0.6939 | ✗ MISS | 0.0492 (0.0492) | 1.3375 | 0.5336 | yes |
| 4 | 14_agent_system_design | allowed | P1 | P1 (light) | 0.5938 / 0.6859 / 0.5966 / 0.5837 | ✓ EXACT | 0.0 (0.0) | 1.5305 | 0.4379 | no |
| 5 | 29_evaluation_metrics | allowed | P0 | P1 (light) | 0.5118 / 0.7876 / 0.7138 / 0.685 | ~ NEAR | 0.2759 (0.2759) | 1.3424 | 0.4559 | yes |
| 6 | 31_CI | allowed | P0 | P1 (light) | 0.6284 / 0.6901 / 0.5939 / 0.6053 | ~ NEAR | 0.0617 (0.0617) | 0.0 | 1.0 | no |
| 7 | Bird_Eye_Extreme | allowed | P0 | P1 (light) | 0.4915 / 0.7266 / 0.5656 / 0.4522 | ~ NEAR | 0.2351 (0.2351) | 0.7121 | 0.8049 | no |
| 8 | Dark_Dimension | allowed | P0 | P0 (skip) | 0.814 / 0.6803 / 0.6923 / 0.6287 | ✓ EXACT | 0.0 (0.0) | 0.0 | 1.0 | no |
| 9 | Distinct_AI_Models | allowed | P0 | P1 (light) | 0.625 / 0.7917 / 0.6398 / 0.7135 | ~ NEAR | 0.1667 (0.1667) | 0.971 | 0.6 | no |
| 10 | Earth_Oceans_Origin | allowed | P1 | P3 (deep) | 0.4707 / 0.5086 / 0.5917 / 0.6133 | ✗ MISS | 0.1046 (0.1046) | 0.9367 | 0.6471 | yes |
| 11 | Gravity_Entropy | allowed | P1 | P1 (light) | 0.646 / 0.7228 / 0.6604 / 0.5609 | ✓ EXACT | 0.0 (0.0) | 0.9815 | 0.58 | no |
| 12 | HNSW | allowed | P0 | P1 (light) | 0.4839 / 0.7672 / 0.5239 / 0.5556 | ~ NEAR | 0.2833 (0.2833) | 0.996 | 0.5373 | no |
| 13 | Insects_Consciousness | allowed | P0 | P1 (light) | 0.5434 / 0.8553 / 0.5461 / 0.7229 | ~ NEAR | 0.3118 (0.3118) | 0.9 | 0.684 | no |
| 14 | Space-Time_QECC | allowed | P0 | P1 (light) | 0.462 / 0.602 / 0.5076 / 0.5188 | ~ NEAR | 0.14 (0.14) | 0.6343 | 0.84 | yes |
| 15 | State_of_LLM_Reasoning | forbidden | P0 | P0 (skip) | 0.449 / 0.4057 / 0.4243 / 0.3653 | ✓ EXACT | 0.0 (excluded — forbidden) | 1.1204 | 0.7143 | yes |
| 16 | Understanding_Reasoning_LLMs | allowed | P0 | P2 (standard) | 0.4603 / 0.5987 / 0.6078 / 0.527 | ✗ MISS | 0.1475 (0.1475) | 0.4071 | 0.9186 | yes |

### Train split (n=24)

| # | Variant | Policy | RL | Oracle | Rewards (P0/P1/P2/P3) | Verdict | Regret (counted) | Entropy | Confidence | Floor |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 02_workflows_vs_agents__var_minimal | forbidden | P1 | P0 (skip) | 0.4962 / 0.6931 / 0.45 / 0.475 | ~ NEAR | -0.1969 (excluded — forbidden) | 1.543 | 0.4231 | no |
| 2 | 02_workflows_vs_agents__var_standard | allowed | P1 | P1 (light) | 0.6292 / 0.794 / 0.7335 / 0.51 | ✓ EXACT | 0.0 (0.0) | 1.3513 | 0.5849 | yes |
| 3 | 02_workflows_vs_agents__var_demanding | allowed | P2 | P1 (light) | 0.4835 / 0.5722 / 0.5121 / 0.4478 | ~ NEAR | 0.0601 (0.0601) | 1.4988 | 0.4943 | no |
| 4 | 03_context_engineering__var_minimal | forbidden | P0 | P0 (skip) | 0.7625 / 0.7783 / 0.6314 / 0.7269 | ✓ EXACT | 0.0 (excluded — forbidden) | 0.8967 | 0.6908 | no |
| 5 | 03_context_engineering__var_standard | allowed | P1 | P0 (skip) | 0.6414 / 0.6119 / 0.5843 / 0.5143 | ~ NEAR | 0.0295 (0.0295) | 0.9967 | 0.5339 | no |
| 6 | 03_context_engineering__var_demanding | required | P1 | P1 (light) | 0.4295 / 0.5055 / 0.477 / 0.4368 | ✓ EXACT | 0.0 (0.0) | 1.1811 | 0.6766 | yes |
| 7 | 05_workflow_patterns__var_minimal | forbidden | P1 | P0 (skip) | 0.872 / 0.8408 / 0.796 / 0.746 | ~ NEAR | 0.0312 (excluded — forbidden) | 0.9912 | 0.5552 | no |
| 8 | 05_workflow_patterns__var_standard | allowed | P2 | P1 (light) | 0.6149 / 0.8085 / 0.7092 / 0.7192 | ~ NEAR | 0.0992 (0.0992) | 1.3697 | 0.4872 | no |
| 9 | 05_workflow_patterns__var_demanding | required | P1 | P1 (light) | 0.5417 / 0.6549 / -0.06 / 0.4766 | ✓ EXACT | 0.0 (0.0) | 1.4516 | 0.4805 | yes |
| 10 | 06_tools__var_minimal | forbidden | P0 | P0 (skip) | 0.6903 / 0.6818 / 0.557 / 0.3205 | ✓ EXACT | 0.0 (excluded — forbidden) | 0.9643 | 0.6107 | no |
| 11 | 06_tools__var_standard | allowed | P0 | P0 (skip) | 0.5598 / 0.4525 / 0.5707 / 0.5184 | ✓ EXACT | 0.0 (0.0) | 1.6098 | 0.5864 | no |
| 12 | 06_tools__var_demanding | required | P3 | P3 (deep) | 0.3794 / 0.4551 / 0.4288 / 0.4949 | ✓ EXACT | 0.0 (0.0) | 1.9158 | 0.3829 | no |
| 13 | 08_react_practice__var_minimal | forbidden | P0 | P0 (skip) | 0.6543 / 0.1224 / 0.0647 / 0.3828 | ✓ EXACT | 0.0 (excluded — forbidden) | 0.8727 | 0.7069 | no |
| 14 | 08_react_practice__var_standard | allowed | P0 | P1 (light) | 0.3892 / 0.5431 / 0.259 / 0.3283 | ~ NEAR | 0.1539 (0.1539) | 0.9997 | 0.5108 | no |
| 15 | 08_react_practice__var_demanding | required | P2 | P2 (standard) | 0.4094 / 0.4042 / 0.5843 / 0.4348 | ✓ EXACT | 0.0 (0.0) | 1.3509 | 0.4598 | no |
| 16 | 09_RAG__var_minimal | forbidden | P0 | P0 (skip) | 0.7317 / 0.5683 / 0.4467 / 0.3627 | ✓ EXACT | 0.0 (excluded — forbidden) | 0.9588 | 0.6318 | no |
| 17 | 09_RAG__var_standard | allowed | P0 | P1 (light) | 0.4057 / 0.4394 / 0.4255 / 0.3807 | ~ NEAR | 0.0338 (0.0338) | 1.4649 | 0.5217 | yes |
| 18 | 09_RAG__var_demanding | allowed | P3 | P3 (deep) | 0.3767 / 0.5314 / 0.3625 / 0.5497 | ✓ EXACT | 0.0 (0.0) | 1.3762 | 0.5937 | no |
| 19 | 10_memory_knowledge_access__var_minimal | forbidden | P0 | P0 (skip) | 0.6893 / 0.64 / 0.6446 / 0.5982 | ✓ EXACT | 0.0 (excluded — forbidden) | 0.8631 | 0.7143 | no |
| 20 | 10_memory_knowledge_access__var_standard | allowed | P1 | P1 (light) | 0.4776 / 0.5534 / 0.4779 / 0.4473 | ✓ EXACT | 0.0 (0.0) | 1.5226 | 0.6261 | no |
| 21 | 10_memory_knowledge_access__var_demanding | required | P2 | P2 (standard) | 0.3478 / 0.5424 / 0.5895 / 0.5482 | ✓ EXACT | 0.0 (0.0) | 0.6932 | 0.814 | no |
| 22 | 11_multimodal__var_minimal | forbidden | P0 | P0 (skip) | 0.369 / 0.3362 / 0.3024 / 0.2631 | ✓ EXACT | 0.0 (excluded — forbidden) | 1.699 | 0.5517 | no |
| 23 | 11_multimodal__var_standard | allowed | P1 | P1 (light) | 0.6854 / 0.6666 / 0.4056 / 0.6013 | ✓ EXACT | 0.0 (0.0) | 1.2765 | 0.4836 | yes |
| 24 | 11_multimodal__var_demanding | required | P2 | P2 (standard) | 0.4383 / 0.5775 / 0.6064 / 0.6104 | ✓ EXACT | 0.0 (0.0) | 1.1036 | 0.6313 | no |
