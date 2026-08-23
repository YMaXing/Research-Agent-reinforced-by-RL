================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:05:37.033 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:05:37.296 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-21 15:05:37.303 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-21 15:05:44.297 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:05:44.319 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:05:51.471 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=65%  H=1.49bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.292  P1/light:0.427  P2/standard:0.424  P3/deep:0.347
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-21 15:05:51.485 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:00.636 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:06:00.651 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:10.017 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:06:10.036 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:19.244 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:06:19.284 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:28.940 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.95bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:06:28.958 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:39.078 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=16%  H=1.13bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0118  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-21 15:06:39.100 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:47.450 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:06:47.464 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:06:55.597 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=60%  H=1.31bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:06:55.605 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:06.148 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:07:06.161 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:18.728 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:07:18.743 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:29.672 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=69%  H=1.17bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.137  P1/light:0.214  P2/standard:0.258  P3/deep:0.310
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:07:29.689 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:36.725 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:07:36.742 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:45.758 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:07:45.772 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:07:56.770 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=61%  H=1.34bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.187  P1/light:0.165  P2/standard:0.336  P3/deep:0.257
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:07:56.785 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:08:18.816 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.87bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : -0.0136  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-21 15:08:18.828 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:08:39.379 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.86bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.125  P2/standard:0.139  P3/deep:0.232
  Regret     : 0.1070  (regret +0.1070)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-21 15:08:39.400 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:09:07.312 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:09:07.336 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:09:34.422 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:09:34.460 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:09:34.479 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-21 15:09:34.485 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-21 15:09:42.527 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=38%  H=0.96bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.194  P1/light:0.273  P2/standard:0.232  P3/deep:0.227
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-21 15:09:42.553 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:09:51.018 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=66%  H=1.26bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.201  P1/light:0.352  P2/standard:0.361  P3/deep:0.395
  Regret     : 0.0330  (regret +0.0330)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-21 15:09:51.032 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:02.106 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=69%  H=0.89bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-21 15:10:02.124 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:11.536 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=2%  H=1.28bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : -0.0263  (regret -0.0263)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-21 15:10:11.549 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:21.282 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:10:21.296 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:29.628 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:10:29.651 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:41.700 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:10:41.722 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:10:58.796 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:10:58.812 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:05.880 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=59%  H=1.55bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0260  (regret +0.0260)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-21 15:11:05.896 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:16.857 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:11:16.882 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:27.737 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=64%  H=1.27bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-21 15:11:27.752 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:32.741 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:11:32.754 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:36.346 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:11:36.364 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:43.105 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=0.99bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0169  (regret +0.0169)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-21 15:11:43.121 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:11:59.289 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:11:59.307 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:12:16.566 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=0.98bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-21 15:12:16.582 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:12:34.868 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.69bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-21 15:12:34.891 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:12:47.592 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=60%  H=1.25bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.400  P1/light:0.560  P2/standard:0.475  P3/deep:0.514
  Regret     : -0.0455  (regret -0.0455)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-21 15:12:47.612 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:12:59.591 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-21 15:12:59.600 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:12:59.662 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-21 15:12:59.672 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-21 15:13:29.825 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=43%  H=1.65bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0132  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-21 15:13:29.844 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-21 15:13:39.372 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
  14_agent_system_design                         TEST    P3     —    P3  → P2    ~ NEAR
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
  State_of_LLM_Reasoning                         TEST    P1     —    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=9 (56%)  near=4 (25%)  miss=3 (19%)  no-oracle/error=0
  Ordinal MAE: 0.625
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0092  max=0.0667

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         2         0         0  (n=2)
  P1 light                        0         6         0         1  (n=7)
  P2 standard                     0         0         1         2  (n=3)
  P3 deep                         0         2         0         2  (n=4)

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
  09_RAG__var_standard                           TRAIN    P1     —    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P3     —    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P1     —    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_demanding                   TRAIN    P1     —    P1  → P2    ~ NEAR

  n=24  exact=11 (46%)  near=11 (46%)  miss=2 (8%)  no-oracle/error=0
  Ordinal MAE: 0.667
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0151  max=0.1070

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         7         0         1  (n=9)
  P1 light                        0         7         1         0  (n=8)
  P2 standard                     0         2         1         0  (n=3)
  P3 deep                         0         1         1         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 1/8   exact+near 7/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 4/8   exact+near 7/8   regret mean=0.0279 max=0.1070
  var_demanding    ( 8):  exact 6/8   exact+near 8/8   regret mean=0.0023 max=0.0330

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=20 (50%)  near=15 (38%)  miss=5 (12%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0122  max=0.1070