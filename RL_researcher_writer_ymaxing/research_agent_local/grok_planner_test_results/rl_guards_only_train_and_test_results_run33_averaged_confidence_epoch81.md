================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:56:47.482 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:56:48.438 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-25 12:02:43.141 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run33_averaged_confidence/epochs/epoch_0081
2026-08-25 12:02:46.371 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=58%  H=1.10bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-25 12:02:46.416 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:02:52.131 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=36%  H=1.41bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:02:52.146 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:02:54.554 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=17%  H=1.11bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.274  P1/light:0.394  P2/standard:0.399  P3/deep:0.319
  Regret     : 0.0053  (regret +0.0053)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:02:54.567 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:02:57.677 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P0 skip      conf=79%  H=0.74bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-25 12:02:57.706 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:00.785 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=24%  H=1.45bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.298  P2/standard:0.323  P3/deep:0.281
  Regret     : 0.0247  (regret +0.0247)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:00.797 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:03.970 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.72bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:03.982 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:06.706 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=32%  H=1.36bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:06.717 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:09.450 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=21%  H=1.45bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:09.486 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:12.212 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.40bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:12.228 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:15.725 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=26%  H=1.89bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:15.767 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:19.290 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=1.55bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:19.321 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:26.413 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=69%  H=1.17bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:26.439 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:28.834 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=0.87bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:28.847 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:31.273 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.44bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:31.305 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:34.058 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.73bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:34.078 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:36.524 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.54bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:36.538 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:38.947 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.91bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0342  (regret +0.0342)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:38.985 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:41.596 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=52%  H=1.27bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:41.612 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:44.421 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=61%  H=0.97bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:44.476 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:47.249 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=48%  H=1.00bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:47.265 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:50.120 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-25 12:03:50.152 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:53.261 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.58bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-25 12:03:53.285 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:03:56.500 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=37%  H=1.62bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.0356  (regret +0.0356)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-25 12:03:56.539 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:03.212 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=14%  H=1.75bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0402  (regret +0.0402)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-25 12:04:03.263 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:06.192 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.34bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.276  P1/light:0.315  P2/standard:0.350  P3/deep:0.350
  Regret     : -0.0000
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-25 12:04:06.232 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:09.470 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=31%  H=1.79bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.050  P1/light:0.001  P2/standard:0.002  P3/deep:0.033
  Regret     : 0.0495  (regret +0.0495)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-25 12:04:09.505 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:15.295 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.84bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.348  P1/light:0.395  P2/standard:0.373  P3/deep:0.391
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-25 12:04:15.327 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:17.779 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=88%  H=0.54bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.268  P1/light:0.370  P2/standard:0.398  P3/deep:0.348
  Regret     : 0.0279  (regret +0.0279)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-25 12:04:17.818 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:20.884 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.32bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-25 12:04:20.902 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:24.574 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.36bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-25 12:04:24.590 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:26.267 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=51%  H=1.47bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.275  P1/light:0.361  P2/standard:0.369  P3/deep:0.289
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-25 12:04:26.288 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:27.498 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.51bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.341  P1/light:0.517  P2/standard:0.511  P3/deep:0.559
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-25 12:04:27.527 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:29.128 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=0.99bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.335  P1/light:0.457  P2/standard:0.449  P3/deep:0.453
  Regret     : -0.0036  (regret -0.0036)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-25 12:04:29.196 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:30.922 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.285  P1/light:0.361  P2/standard:0.304  P3/deep:0.426
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-25 12:04:30.935 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:32.972 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=0.00bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.362  P1/light:0.425  P2/standard:0.412  P3/deep:0.338
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-25 12:04:32.987 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:38.078 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=95%  H=0.27bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-25 12:04:38.139 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:39.548 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=76%  H=0.79bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.360  P1/light:0.519  P2/standard:0.473  P3/deep:0.579
  Regret     : 0.0599  (regret +0.0599)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-25 12:04:39.570 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:41.708 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=42%  H=1.32bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.299  P1/light:0.394  P2/standard:0.359  P3/deep:0.336
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-25 12:04:41.737 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:51.605 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=25%  H=1.80bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-25 12:04:51.615 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 12:04:54.869 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.26bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.383  P2/standard:0.400  P3/deep:0.368
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT
2026-08-25 12:04:54.895 | INFO     | logging:callHandlers:1762 | Stopping stale infer server (adapter changed)…

================================================================================
  TEST  (held-out, primary metric)  [RL + deterministic policy guards]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST    P3     —    P3  → P2    ~ NEAR
  07_reasoning_planning                          TEST    P1     —    P1  → P0    ~ NEAR
  13_agent_framework                             TEST    P1     —    P1  → P1    ✓ EXACT
  14_agent_system_design                         TEST    P1     —    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P3     —    P3  → P1    ✗ MISS
  31_CI                                          TEST    P1     —    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST    P1     —    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST    P3     —    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1     —    P1  → P3    ✗ MISS
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P3    ✓ EXACT
  Gravity_Entropy                                TEST    P1     —    P1  → P1    ✓ EXACT
  HNSW                                           TEST    P1     —    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P3    ✗ MISS
  Space-Time_QECC                                TEST    P1     —    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P1     —    P0  → P0    ✓ EXACT
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=10 (62%)  near=3 (19%)  miss=3 (19%)  no-oracle/error=0
  Ordinal MAE: 0.562
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0134  max=0.0667

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         1         0         0  (n=2)
  P1 light                        0         6         0         1  (n=7)
  P2 standard                     0         1         1         1  (n=3)
  P3 deep                         0         2         0         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=2  P1=7  P2=3  P3=4
  Majority-class baseline (always P1 light): 43.8%  (7/16)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  30.5%

================================================================================
  TRAIN (reference)  [RL + deterministic policy guards]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN    P1     —    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN    P1     —    P1  → P1    ✓ EXACT
  02_workflows_vs_agents__var_demanding          TRAIN    P1     —    P1  → P2    ~ NEAR
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

  n=24  exact=18 (75%)  near=5 (21%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.292
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0111  max=0.0402

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         1         0         0  (n=9)
  P1 light                        0         8         0         0  (n=8)
  P2 standard                     0         3         0         0  (n=3)
  P3 deep                         0         1         1         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 5/8   exact+near 7/8   regret mean=0.0118 max=0.0356
  var_demanding    ( 8):  exact 5/8   exact+near 8/8   regret mean=0.0105 max=0.0402

################################################################################
  COMBINED  [RL + deterministic policy guards]  (n=40)
################################################################################
  n=40  exact=28 (70%)  near=8 (20%)  miss=4 (10%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0122  max=0.0667