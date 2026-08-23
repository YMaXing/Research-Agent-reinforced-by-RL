================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:38:51.422 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:38:51.570 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-22 08:47:49.936 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run32_recover_epoch91/best
2026-08-22 08:47:54.171 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.42bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.285  P1/light:0.432  P2/standard:0.216  P3/deep:0.320
  Regret     : -0.1479  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-22 08:47:54.202 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:47:56.799 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=65%  H=1.27bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.292  P1/light:0.427  P2/standard:0.424  P3/deep:0.347
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:47:56.833 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:47:59.498 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=72%  H=1.11bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.314  P1/light:0.457  P2/standard:0.480  P3/deep:0.238
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:47:59.515 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:03.381 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P0 skip      conf=79%  H=0.74bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P0 skip  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.263  P1/light:0.261  P2/standard:0.176  P3/deep:0.241
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:03.396 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:06.713 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=63%  H=1.31bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.273  P1/light:0.339  P2/standard:0.421  P3/deep:0.282
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:06.735 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:10.214 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.72bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:10.243 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:13.209 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=21%  H=1.27bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0118  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:13.295 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:16.342 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=54%  H=1.45bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.287  P1/light:0.497  P2/standard:0.436  P3/deep:0.489
  Regret     : 0.0612  (regret +0.0612)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:16.401 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:19.389 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.40bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:19.419 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:23.245 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=30%  H=1.90bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.195  P1/light:0.171  P2/standard:0.088  P3/deep:0.079
  Regret     : +0.0240  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:23.285 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:27.172 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=50%  H=1.77bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.110  P1/light:0.259  P2/standard:0.297  P3/deep:0.381
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:27.252 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:31.257 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=54%  H=1.33bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.137  P1/light:0.214  P2/standard:0.258  P3/deep:0.310
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:31.308 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:34.511 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=0.87bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.086  P2/standard:0.102  P3/deep:0.110
  Regret     : +0.1225  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:34.544 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:37.158 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.50bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.147  P1/light:0.322  P2/standard:0.088  P3/deep:0.102
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:37.213 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:40.252 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=28%  H=1.89bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.187  P1/light:0.165  P2/standard:0.336  P3/deep:0.257
  Regret     : -0.1707  (regret -0.1707)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:40.312 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:43.044 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.88bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : -0.0136  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:43.103 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:45.875 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=29%  H=1.97bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.125  P2/standard:0.139  P3/deep:0.232
  Regret     : 0.0937  (regret +0.0937)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:45.928 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:48.951 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=17%  H=1.48bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.217  P1/light:0.255  P2/standard:0.235  P3/deep:0.265
  Regret     : 0.0294  (regret +0.0294)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:49.037 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:52.148 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=39%  H=0.97bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.164  P1/light:0.189  P2/standard:0.108  P3/deep:0.109
  Regret     : -0.0246  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-22 08:48:52.210 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:55.228 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=70%  H=0.88bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.194  P1/light:0.273  P2/standard:0.232  P3/deep:0.227
  Regret     : 0.0414  (regret +0.0414)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:48:55.254 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:48:58.355 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.201  P1/light:0.352  P2/standard:0.361  P3/deep:0.395
  Regret     : 0.0330  (regret +0.0330)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-22 08:48:58.377 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:01.718 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.49bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-22 08:49:01.785 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:05.394 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.41bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : -0.0263  (regret -0.0263)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-22 08:49:05.432 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:09.733 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=53%  H=1.73bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.377  P1/light:0.392  P2/standard:0.377  P3/deep:0.404
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-22 08:49:09.763 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:12.857 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=73%  H=0.84bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.333  P1/light:0.383  P2/standard:0.464  P3/deep:0.446
  Regret     : 0.0180  (regret +0.0180)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-22 08:49:12.930 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:16.397 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=54%  H=1.70bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.007  P1/light:-0.048  P2/standard:-0.026  P3/deep:-0.006
  Regret     : 0.0336  (regret +0.0336)
  Verdict    : ✗  MISS

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-22 08:49:16.410 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:22.728 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=63%  H=1.33bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.358  P1/light:0.374  P2/standard:0.365  P3/deep:0.411
  Regret     : 0.0088  (regret +0.0088)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-22 08:49:22.762 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:25.319 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=46%  H=1.53bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0077  (regret +0.0077)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-22 08:49:25.327 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:28.696 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=74%  H=1.10bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-22 08:49:28.740 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:32.734 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=1.36bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-22 08:49:32.753 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:34.552 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=51%  H=1.47bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.375  P2/standard:0.336  P3/deep:0.248
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-22 08:49:34.623 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:36.015 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=34%  H=1.51bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.380  P1/light:0.486  P2/standard:0.459  P3/deep:0.488
  Regret     : 0.0026  (regret +0.0026)
  Verdict    : ✗  MISS

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-22 08:49:36.024 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:37.734 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=82%  H=0.67bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0406  (regret +0.0406)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-22 08:49:37.772 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:40.154 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.213  P1/light:0.277  P2/standard:0.312  P3/deep:0.315
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-22 08:49:40.183 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:42.391 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=0.01bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-22 08:49:42.440 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:44.245 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=82%  H=0.84bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-22 08:49:44.276 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:45.578 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.54bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.400  P1/light:0.560  P2/standard:0.475  P3/deep:0.514
  Regret     : -0.0455  (regret -0.0455)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-22 08:49:45.586 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:47.803 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.50bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.196  P1/light:0.372  P2/standard:0.312  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-22 08:49:47.836 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:49:58.219 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.58bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0132  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-22 08:49:58.230 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-22 08:50:01.718 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=98%  H=0.17bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.197  P1/light:0.298  P2/standard:0.363  P3/deep:0.320
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [RL-only]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST    P3     —    P3  → P2    ~ NEAR
  07_reasoning_planning                          TEST    P2     —    P2  → P0    ✗ MISS
  13_agent_framework                             TEST    P2     —    P2  → P1    ~ NEAR
  14_agent_system_design                         TEST    P1     —    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P3     —    P3  → P1    ✗ MISS
  31_CI                                          TEST    P1     —    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST    P1     —    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST    P1     —    P1  → P3    ✗ MISS
  Distinct_AI_Models                             TEST    P2     —    P2  → P3    ~ NEAR
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P3    ✓ EXACT
  Gravity_Entropy                                TEST    P1     —    P1  → P1    ✓ EXACT
  HNSW                                           TEST    P1     —    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P3    ✗ MISS
  Space-Time_QECC                                TEST    P1     —    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P1     —    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=7 (44%)  near=5 (31%)  miss=4 (25%)  no-oracle/error=0
  Ordinal MAE: 0.812
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0088  max=0.0667

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         1         1         0  (n=2)
  P1 light                        0         5         1         1  (n=7)
  P2 standard                     0         1         1         1  (n=3)
  P3 deep                         0         2         1         1  (n=4)

  --- Baselines ---
  Oracle distribution: P0=2  P1=7  P2=3  P3=4
  Majority-class baseline (always P1 light): 43.8%  (7/16)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  30.5%

================================================================================
  TRAIN (reference)  [RL-only]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN    P1     —    P1  → P0    ~ NEAR
  02_workflows_vs_agents__var_standard           TRAIN    P1     —    P1  → P1    ✓ EXACT
  02_workflows_vs_agents__var_demanding          TRAIN    P2     —    P2  → P2    ✓ EXACT
  03_context_engineering__var_minimal            TRAIN    P0     —    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN    P2     —    P2  → P2    ✓ EXACT
  03_context_engineering__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P1  → P0    ~ NEAR
  05_workflow_patterns__var_standard             TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P1  → P0    ~ NEAR
  06_tools__var_standard                         TRAIN    P3     —    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_minimal                 TRAIN    P1     —    P1  → P0    ~ NEAR
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P2     —    P2  → P1    ~ NEAR
  09_RAG__var_minimal                            TRAIN    P3     —    P3  → P0    ✗ MISS
  09_RAG__var_standard                           TRAIN    P2     —    P2  → P3    ~ NEAR
  09_RAG__var_demanding                          TRAIN    P2     —    P2  → P3    ~ NEAR
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P2     —    P2  → P1    ~ NEAR
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_demanding                   TRAIN    P2     —    P2  → P2    ✓ EXACT

  n=24  exact=10 (42%)  near=13 (54%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.667
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0039  max=0.0937

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         7         0         1  (n=9)
  P1 light                        0         5         3         0  (n=8)
  P2 standard                     0         0         3         0  (n=3)
  P3 deep                         0         0         3         1  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 1/8   exact+near 7/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 4/8   exact+near 8/8   regret mean=0.0213 max=0.0937
  var_demanding    ( 8):  exact 5/8   exact+near 8/8   regret mean=-0.0135 max=0.0330

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=17 (42%)  near=18 (45%)  miss=5 (12%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0063  max=0.0937