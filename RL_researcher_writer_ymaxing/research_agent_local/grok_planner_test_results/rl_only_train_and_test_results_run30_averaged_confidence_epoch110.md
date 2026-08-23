================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:53:23.299 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:53:23.720 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-21 17:53:23.723 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run30_averaged_confidence/test110
2026-08-21 17:53:30.672 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.00bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.285  P1/light:0.432  P2/standard:0.216  P3/deep:0.320
  Regret     : -0.1479  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-21 17:53:30.706 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:53:37.598 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:53:37.619 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:53:44.621 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:53:44.635 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:53:56.770 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:53:56.784 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:06.057 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.53bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.273  P1/light:0.339  P2/standard:0.421  P3/deep:0.282
  Regret     : 0.0817  (regret +0.0817)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-21 17:54:06.070 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:15.312 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=20%  H=1.92bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:54:15.337 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:23.480 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=32%  H=1.36bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0118  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-21 17:54:23.523 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:34.500 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:54:34.553 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:42.840 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=44%  H=1.55bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:54:42.856 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:54:53.368 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=27%  H=1.89bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.195  P1/light:0.171  P2/standard:0.088  P3/deep:0.079
  Regret     : +0.0240  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-21 17:54:53.388 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:06.024 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=1.56bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.110  P1/light:0.259  P2/standard:0.297  P3/deep:0.381
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-21 17:55:06.040 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:16.969 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=44%  H=1.53bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.137  P1/light:0.214  P2/standard:0.258  P3/deep:0.310
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:55:16.984 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:23.980 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:55:24.012 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:31.065 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.44bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.147  P1/light:0.322  P2/standard:0.088  P3/deep:0.102
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-21 17:55:31.094 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:41.130 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=33%  H=1.94bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.187  P1/light:0.165  P2/standard:0.336  P3/deep:0.257
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:55:41.154 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:47.705 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.48bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : -0.0136  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-21 17:55:47.723 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:55:56.073 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=0%  H=1.50bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.125  P2/standard:0.139  P3/deep:0.232
  Regret     : 0.0937  (regret +0.0937)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-21 17:55:56.093 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:03.709 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=62%  H=0.96bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.217  P1/light:0.255  P2/standard:0.235  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-21 17:56:03.727 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:14.583 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:56:14.606 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:23.442 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:56:23.460 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:32.759 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:56:32.774 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:43.242 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=66%  H=0.93bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-21 17:56:43.255 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:56:55.010 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=1%  H=0.92bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : -0.0263  (regret -0.0263)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-21 17:56:55.025 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:57:05.718 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=38%  H=1.91bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.377  P1/light:0.392  P2/standard:0.377  P3/deep:0.404
  Regret     : -0.0149  (regret -0.0149)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-21 17:57:05.808 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:57:15.108 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:57:15.125 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:57:28.051 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=1.78bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.007  P1/light:-0.048  P2/standard:-0.026  P3/deep:-0.006
  Regret     : 0.0552  (regret +0.0552)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-21 17:57:28.067 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:57:45.751 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.84bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.358  P1/light:0.374  P2/standard:0.365  P3/deep:0.411
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-21 17:57:45.774 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:57:53.604 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=41%  H=1.75bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0077  (regret +0.0077)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-21 17:57:53.621 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:05.075 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.32bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-21 17:58:05.092 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:05.121 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-21 17:58:05.126 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run30_averaged_confidence/test110
2026-08-21 17:58:15.954 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=84%  H=0.66bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-21 17:58:15.968 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:20.890 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:58:20.909 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:24.480 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.51bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.380  P1/light:0.486  P2/standard:0.459  P3/deep:0.488
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-21 17:58:24.495 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:29.199 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=65%  H=0.93bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0406  (regret +0.0406)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-21 17:58:29.216 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:36.187 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:58:36.201 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:42.266 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=78%  H=0.75bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-21 17:58:42.281 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:47.260 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=14%  H=1.44bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.1273  (regret +0.1273)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-21 17:58:47.271 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:50.853 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 17:58:50.872 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:58:56.984 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=52%  H=1.31bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.196  P1/light:0.372  P2/standard:0.312  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-21 17:58:57.000 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:59:27.484 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=48%  H=1.79bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0107  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-21 17:59:27.521 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 17:59:36.978 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=94%  H=0.32bits
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
  HNSW                                           TEST    P2     —    P2  → P1    ~ NEAR
  Insects_Consciousness                          TEST    P1     —    P1  → P3    ✗ MISS
  Space-Time_QECC                                TEST    P1     —    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P3     —    P3  → P0    ✗ MISS
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=8 (50%)  near=5 (31%)  miss=3 (19%)  no-oracle/error=0
  Ordinal MAE: 0.750
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0180  max=0.1273

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         1         0         1  (n=2)
  P1 light                        0         5         1         1  (n=7)
  P2 standard                     0         1         1         1  (n=3)
  P3 deep                         0         1         1         2  (n=4)

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
  03_context_engineering__var_standard           TRAIN    P1     —    P1  → P2    ~ NEAR
  03_context_engineering__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P1  → P0    ~ NEAR
  05_workflow_patterns__var_standard             TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P1  → P0    ~ NEAR
  06_tools__var_standard                         TRAIN    P3     —    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_minimal                 TRAIN    P1     —    P1  → P0    ~ NEAR
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P1     —    P1  → P1    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P3     —    P3  → P0    ✗ MISS
  09_RAG__var_standard                           TRAIN    P2     —    P2  → P3    ~ NEAR
  09_RAG__var_demanding                          TRAIN    P3     —    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P2     —    P2  → P1    ~ NEAR
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_demanding                   TRAIN    P1     —    P1  → P2    ~ NEAR

  n=24  exact=10 (42%)  near=13 (54%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.667
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0169  max=0.0937

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         7         0         1  (n=9)
  P1 light                        0         6         2         0  (n=8)
  P2 standard                     0         2         1         0  (n=3)
  P3 deep                         0         0         2         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 1/8   exact+near 7/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 3/8   exact+near 8/8   regret mean=0.0315 max=0.0937
  var_demanding    ( 8):  exact 6/8   exact+near 8/8   regret mean=0.0023 max=0.0330

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=18 (45%)  near=18 (45%)  miss=4 (10%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0174  max=0.1273