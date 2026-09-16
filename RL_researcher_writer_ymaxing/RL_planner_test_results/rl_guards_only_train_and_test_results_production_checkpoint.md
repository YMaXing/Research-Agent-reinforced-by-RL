================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:37:11.000 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-09-09 12:41:33.958 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/research_agent_local/rl_inference_service/checkpoints/production
2026-09-09 12:41:37.536 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=58%  H=1.10bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.54  standard=0.00  deep=0.46
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-09-09 12:41:40.058 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=36%  H=1.41bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.35  standard=0.52  deep=0.13
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:41:42.574 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=17%  H=1.11bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.10  light=0.17  standard=0.72  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.274  P1/light:0.428  P2/standard:0.422  P3/deep:0.319
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:41:45.811 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P0 skip      conf=79%  H=0.74bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.79  light=0.00  standard=0.00  deep=0.21
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-09-09 12:41:48.949 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=24%  H=1.45bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.23  standard=0.55  deep=0.22
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.282  P2/standard:0.316  P3/deep:0.281
  Regret     : 0.0341  (regret +0.0341)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:41:52.322 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.72bits
  Section vote mass (word-weighted hard vote): skip=0.15  light=0.35  standard=0.44  deep=0.07
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:41:55.388 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=32%  H=1.36bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.56  light=0.32  standard=0.12  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-09-09 12:41:58.312 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=21%  H=1.45bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.21  standard=0.54  deep=0.26
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:01.134 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : required
  RL model   : P1 light     conf=43%  H=1.40bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.43  standard=0.45  deep=0.12
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:42:04.863 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=26%  H=1.89bits
  Section vote mass (word-weighted hard vote): skip=0.36  light=0.27  standard=0.11  deep=0.26
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-09-09 12:42:10.935 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=1.55bits
  Section vote mass (word-weighted hard vote): skip=0.12  light=0.18  standard=0.09  deep=0.61
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:14.829 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=69%  H=1.17bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.69  standard=0.22  deep=0.09
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:42:17.384 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=0.87bits
  Section vote mass (word-weighted hard vote): skip=0.71  light=0.29  standard=0.00  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-09-09 12:42:19.741 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.44bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.37  light=0.49  standard=0.00  deep=0.14
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:22.431 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.73bits
  Section vote mass (word-weighted hard vote): skip=0.14  light=0.49  standard=0.28  deep=0.09
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:42:24.833 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.54bits
  Section vote mass (word-weighted hard vote): skip=0.23  light=0.33  standard=0.00  deep=0.43
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P3->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-09-09 12:42:27.357 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.91bits
  Section vote mass (word-weighted hard vote): skip=0.21  light=0.18  standard=0.41  deep=0.20
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0342  (regret +0.0342)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:30.015 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=52%  H=1.27bits
  Section vote mass (word-weighted hard vote): skip=0.38  light=0.17  standard=0.00  deep=0.45
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:42:32.976 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=61%  H=0.97bits
  Section vote mass (word-weighted hard vote): skip=0.39  light=0.61  standard=0.00  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-09-09 12:42:35.955 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=48%  H=1.00bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.48  standard=0.52  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:38.930 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.19  standard=0.81  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:42:44.580 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.58bits
  Section vote mass (word-weighted hard vote): skip=0.31  light=0.38  standard=0.31  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=forbidden: clamped P1->P0 skip
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-09-09 12:42:48.071 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=37%  H=1.62bits
  Section vote mass (word-weighted hard vote): skip=0.47  light=0.38  standard=0.10  deep=0.06
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.0356  (regret +0.0356)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:42:51.607 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=14%  H=1.75bits
  Section vote mass (word-weighted hard vote): skip=0.18  light=0.14  standard=0.53  deep=0.15
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0402  (regret +0.0402)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-09-09 12:42:54.478 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.34bits
  Section vote mass (word-weighted hard vote): skip=0.27  light=0.13  standard=0.00  deep=0.60
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P2 standard  (tied with P3 deep — either counts as EXACT)
  R_w        : P0/skip:0.316  P1/light:0.273  P2/standard:0.400  P3/deep:0.381
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-09-09 12:42:57.641 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=31%  H=1.79bits
  Section vote mass (word-weighted hard vote): skip=0.16  light=0.31  standard=0.44  deep=0.09
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.077  P1/light:0.038  P2/standard:0.052  P3/deep:0.078
  Regret     : 0.0400  (regret +0.0400)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-09-09 12:43:03.495 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.84bits
  Section vote mass (word-weighted hard vote): skip=0.20  light=0.32  standard=0.39  deep=0.09
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.359  P1/light:0.405  P2/standard:0.368  P3/deep:0.376
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-09-09 12:43:05.982 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=88%  H=0.54bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.88  standard=0.12  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.380  P2/standard:0.430  P3/deep:0.394
  Regret     : 0.0508  (regret +0.0508)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-09-09 12:43:09.293 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.32bits
  Section vote mass (word-weighted hard vote): skip=0.12  light=0.28  standard=0.00  deep=0.60
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.380  P1/light:0.391  P2/standard:0.429  P3/deep:0.386
  Regret     : 0.0426  (regret +0.0426)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-09-09 12:43:13.420 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.36bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.12  light=0.57  standard=0.31  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.351  P1/light:0.366  P2/standard:0.340  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-09-09 12:43:17.726 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=51%  H=1.47bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.20  light=0.51  standard=0.00  deep=0.29
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.301  P1/light:0.405  P2/standard:0.398  P3/deep:0.363
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-09-09 12:43:19.082 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.51bits
  Section vote mass (word-weighted hard vote): skip=0.20  light=0.34  standard=0.00  deep=0.46
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.515  P2/standard:0.507  P3/deep:0.547
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-09-09 12:43:21.043 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=0.99bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.45  standard=0.55  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.317  P1/light:0.474  P2/standard:0.456  P3/deep:0.442
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-09-09 12:43:23.101 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.14  standard=0.14  deep=0.72
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.386  P2/standard:0.328  P3/deep:0.469
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-09-09 12:43:25.275 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=0.00bits
  Section vote mass (word-weighted hard vote): skip=0.00  light=1.00  standard=0.00  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.432  P2/standard:0.412  P3/deep:0.328
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-09-09 12:43:27.107 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=95%  H=0.27bits
  Section vote mass (word-weighted hard vote): skip=0.05  light=0.95  standard=0.00  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.338  P1/light:0.426  P2/standard:0.344  P3/deep:0.494
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-09-09 12:43:28.376 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=76%  H=0.79bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.76  standard=0.00  deep=0.24
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.360  P1/light:0.547  P2/standard:0.473  P3/deep:0.577
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-09-09 12:43:30.529 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=42%  H=1.32bits  [floor applied]
  Section vote mass (word-weighted hard vote): skip=0.08  light=0.42  standard=0.50  deep=0.00
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.361  P1/light:0.408  P2/standard:0.361  P3/deep:0.328
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-09-09 12:43:40.346 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : capped
  RL model   : P1 light     conf=25%  H=1.80bits
  Section vote mass (word-weighted hard vote): skip=0.36  light=0.25  standard=0.06  deep=0.33
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
               policy=capped: distribution favors P0 skip over P1 light (P(skip)=0.358 vs P(light)=0.245)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.341  P1/light:0.338  P2/standard:0.332  P3/deep:0.327
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-09-09 12:43:43.918 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping LLM planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.26bits
  Section vote mass (word-weighted hard vote): skip=0.00  light=0.06  standard=0.49  deep=0.45
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light / capped→≤light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.277  P1/light:0.349  P2/standard:0.396  P3/deep:0.362
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [RL + deterministic policy guards]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST    P3     —    P3  → P2    ✓ EXACT
  07_reasoning_planning                          TEST    P1     —    P1  → P3    ~ NEAR
  13_agent_framework                             TEST    P1     —    P1  → P1    ✓ EXACT
  14_agent_system_design                         TEST    P1     —    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P3     —    P3  → P2    ~ NEAR
  31_CI                                          TEST    P1     —    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST    P1     —    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST    P3     —    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1     —    P1  → P1    ✓ EXACT
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P3    ✓ EXACT
  Gravity_Entropy                                TEST    P1     —    P1  → P1    ✓ EXACT
  HNSW                                           TEST    P1     —    P1  → P3    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P3    ✓ EXACT
  Space-Time_QECC                                TEST    P1     —    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P1     —    P0  → P0    ✓ EXACT
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=13 (81%)  near=3 (19%)  miss=0 (0%)  no-oracle/error=0
  Ordinal MAE: 0.188
  Reward-regret (allowed/required only, n=16; 0 forbidden excluded):  mean=0.0083  max=0.0508

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         0         0         0  (n=1)
  P1 light                        0         6         0         0  (n=6)
  P2 standard                     0         1         1     2(✓1)  (n=4)
  P3 deep                         0     3(✓2)         0         2  (n=5)
  (n(✓k) = of that cell's count, k were tied-arm-accepted EXACT hits, not true misses)

  --- Baselines ---
  Oracle distribution: P0=1  P1=6  P2=4  P3=5
  Majority-class baseline (always P1 light): 50.0%  (8/16)
  Uniform-random baseline:  35.9%
  Weighted-random baseline:  41.0%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P1 light): b=5 c=0 n=5  one-sided p=0.0312  [strong]
  Poisson-binomial exact, model vs. per-article chance level: observed=13/16  one-sided p=0.0002  [strong]
  Model exact-rate Wilson 95% CI: [57.0%, 93.4%]  (point estimate 81.2%)

================================================================================
  TRAIN (reference)  [RL + deterministic policy guards]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN    P1     —    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN    P1     —    P1  → P1    ✓ EXACT
  02_workflows_vs_agents__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  03_context_engineering__var_minimal            TRAIN    P0     —    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN    P1     —    P1  → P2    ~ NEAR
  03_context_engineering__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P0  → P0    ✓ EXACT
  05_workflow_patterns__var_standard             TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P0  → P0    ✓ EXACT
  06_tools__var_standard                         TRAIN    P3     —    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_minimal                 TRAIN    P1     —    P0  → P0    ✓ EXACT
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P1     —    P1  → P1    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P3     —    P0  → P0    ✓ EXACT
  09_RAG__var_standard                           TRAIN    P1     —    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P3     —    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P0  → P0    ✓ EXACT
  10_memory_knowledge_access__var_standard       TRAIN    P1     —    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P0  → P0    ✓ EXACT
  11_multimodal__var_standard                    TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_demanding                   TRAIN    P1     —    P1  → P2    ~ NEAR

  n=24  exact=19 (79%)  near=4 (17%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.250
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0114  max=0.0402

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         1         0         0  (n=9)
  P1 light                        0         9         0         0  (n=9)
  P2 standard                     0         2         0         0  (n=2)
  P3 deep                         0         1         1         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=9  P2=2  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline:  25.0%
  Weighted-random baseline:  31.6%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P0 skip): b=11 c=1 n=12  one-sided p=0.0032  [strong]
  Poisson-binomial exact, model vs. per-article chance level: observed=19/24  one-sided p=0.0000  [strong]
  Model exact-rate Wilson 95% CI: [59.5%, 90.8%]  (point estimate 79.2%)
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 5/8   exact+near 7/8   regret mean=0.0130 max=0.0356
  var_demanding    ( 8):  exact 6/8   exact+near 8/8   regret mean=0.0098 max=0.0402

################################################################################
  COMBINED  [RL + deterministic policy guards]  (n=40)
################################################################################
  n=40  exact=32 (80%)  near=7 (18%)  miss=1 (2%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=32; 8 forbidden excluded):  mean=0.0099  max=0.0508