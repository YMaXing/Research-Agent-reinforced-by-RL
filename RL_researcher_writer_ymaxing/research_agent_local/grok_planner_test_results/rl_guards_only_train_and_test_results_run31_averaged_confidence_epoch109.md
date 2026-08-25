================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:38:06.749 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:38:06.934 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-25 11:42:26.109 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run31_averaged_confidence/epochs/epoch_0109
2026-08-25 11:42:29.415 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.42bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-25 11:42:29.456 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:31.832 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=65%  H=1.49bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:42:31.886 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:34.298 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:42:34.321 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:37.429 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=0%  H=1.52bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-25 11:42:37.452 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:43.875 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=61%  H=1.36bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.298  P2/standard:0.323  P3/deep:0.281
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:42:43.923 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:47.221 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.53bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:42:47.249 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:50.062 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:42:50.092 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:52.970 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=21%  H=1.97bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:42:53.042 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:55.904 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:42:55.979 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:42:59.596 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=53%  H=1.36bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-25 11:42:59.642 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:03.252 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:43:03.295 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:07.062 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=77%  H=1.11bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:43:07.110 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:09.521 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:43:09.565 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:11.955 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:43:11.999 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:14.713 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=40%  H=1.88bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0299  (regret +0.0299)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:43:14.743 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:20.218 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=40%  H=1.55bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-25 11:43:20.251 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:22.739 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.86bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0342  (regret +0.0342)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:43:22.768 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:25.425 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=0%  H=0.99bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0371  (regret +0.0371)
  Verdict    : ✗  MISS

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-25 11:43:25.461 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:28.347 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=43%  H=0.99bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-25 11:43:28.378 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:31.181 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=30%  H=0.88bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:43:31.196 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:34.114 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:43:34.171 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:37.275 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.49bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-25 11:43:37.320 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:40.514 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P0 skip      conf=75%  H=0.86bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-25 11:43:40.538 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:43.828 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=28%  H=1.90bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0402  (regret +0.0402)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-25 11:43:43.861 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:46.654 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=73%  H=1.05bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.276  P1/light:0.315  P2/standard:0.350  P3/deep:0.350
  Regret     : -0.0000
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-25 11:43:46.668 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:49.861 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=1.78bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.050  P1/light:0.001  P2/standard:0.002  P3/deep:0.033
  Regret     : 0.0495  (regret +0.0495)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-25 11:43:49.903 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:43:59.056 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=7%  H=1.45bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.348  P1/light:0.395  P2/standard:0.373  P3/deep:0.391
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-25 11:43:59.074 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:01.508 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=81%  H=0.87bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.268  P1/light:0.370  P2/standard:0.398  P3/deep:0.348
  Regret     : 0.0279  (regret +0.0279)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-25 11:44:01.533 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:04.620 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:44:04.633 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:08.394 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.47bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-25 11:44:08.408 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:10.113 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:44:10.134 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:11.354 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-25 11:44:11.369 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:12.963 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=82%  H=0.67bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.335  P1/light:0.457  P2/standard:0.449  P3/deep:0.453
  Regret     : 0.0043  (regret +0.0043)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-25 11:44:13.092 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:14.844 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=0.86bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P3 deep  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.285  P1/light:0.361  P2/standard:0.304  P3/deep:0.426
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-25 11:44:14.971 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:17.167 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=79%  H=0.74bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.362  P1/light:0.425  P2/standard:0.412  P3/deep:0.338
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-25 11:44:17.338 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:19.064 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.23bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-25 11:44:19.102 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:20.391 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.54bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P3 deep
  R_w        : P0/skip:0.360  P1/light:0.519  P2/standard:0.473  P3/deep:0.579
  Regret     : 0.0599  (regret +0.0599)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-25 11:44:20.418 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:22.591 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=52%  H=1.44bits  [floor applied]
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P1 light  (by RL+guards)
  Oracle     : P1 light
  R_w        : P0/skip:0.299  P1/light:0.394  P2/standard:0.359  P3/deep:0.336
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-25 11:44:22.679 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:35.602 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=53%  H=1.57bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P0 skip  (by RL+guards)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-25 11:44:35.630 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-25 11:44:38.894 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=94%  H=0.32bits
  Guards     : deterministic policy clamp (forbidden→skip / required→≥light)
  -> Chosen  : P2 standard  (by RL+guards)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.383  P2/standard:0.400  P3/deep:0.368
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT
2026-08-25 11:44:38.941 | INFO     | logging:callHandlers:1762 | Stopping stale infer server (adapter changed)…

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
  Distinct_AI_Models                             TEST    P2     —    P2  → P3    ~ NEAR
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P3    ✓ EXACT
  Gravity_Entropy                                TEST    P1     —    P1  → P1    ✓ EXACT
  HNSW                                           TEST    P1     —    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P3    ✗ MISS
  Space-Time_QECC                                TEST    P1     —    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P1     —    P0  → P0    ✓ EXACT
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=10 (62%)  near=4 (25%)  miss=2 (12%)  no-oracle/error=0
  Ordinal MAE: 0.500
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0139  max=0.0667

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         1         0         0  (n=2)
  P1 light                        0         6         0         1  (n=7)
  P2 standard                     0         1         1         1  (n=3)
  P3 deep                         0         1         1         2  (n=4)

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
  03_context_engineering__var_minimal            TRAIN    P1     —    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN    P2     —    P2  → P2    ✓ EXACT
  03_context_engineering__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P0  → P0    ✓ EXACT
  05_workflow_patterns__var_standard             TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P0  → P0    ✓ EXACT
  06_tools__var_standard                         TRAIN    P3     —    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_minimal                 TRAIN    P1     —    P0  → P0    ✓ EXACT
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P3     —    P3  → P1    ✗ MISS
  09_RAG__var_minimal                            TRAIN    P1     —    P0  → P0    ✓ EXACT
  09_RAG__var_standard                           TRAIN    P1     —    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P1     —    P1  → P3    ✗ MISS
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P0  → P0    ✓ EXACT
  10_memory_knowledge_access__var_standard       TRAIN    P1     —    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P0  → P0    ✓ EXACT
  11_multimodal__var_standard                    TRAIN    P0     —    P0  → P0    ✓ EXACT
  11_multimodal__var_demanding                   TRAIN    P1     —    P1  → P2    ~ NEAR

  n=24  exact=18 (75%)  near=3 (12%)  miss=3 (12%)  no-oracle/error=0
  Ordinal MAE: 0.375
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0116  max=0.0402

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         9         0         0         0  (n=9)
  P1 light                        0         7         0         1  (n=8)
  P2 standard                     0         2         1         0  (n=3)
  P3 deep                         0         2         1         1  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 7/8   exact+near 7/8   regret mean=0.0043 max=0.0342
  var_demanding    ( 8):  exact 3/8   exact+near 6/8   regret mean=0.0188 max=0.0402

################################################################################
  COMBINED  [RL + deterministic policy guards]  (n=40)
################################################################################
  n=40  exact=28 (70%)  near=7 (18%)  miss=5 (12%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0127  max=0.0667