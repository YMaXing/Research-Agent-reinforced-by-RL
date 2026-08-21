================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:24:11.871 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:24:12.038 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-05 13:28:07.541 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-05 13:28:15.188 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.37bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.285  P1/light:0.432  P2/standard:0.216  P3/deep:0.320
  Regret     : -0.1479  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-05 13:28:15.225 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:28:22.599 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=68%  H=1.22bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.344  P1/light:0.452  P2/standard:0.454  P3/deep:0.329
  Regret     : -0.0019  (regret -0.0019)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:28:22.633 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:28:31.914 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=57%  H=1.35bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.324  P1/light:0.457  P2/standard:0.387  P3/deep:0.238
  Regret     : 0.2183  (regret +0.2183)
  Verdict    : ✗  MISS

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:28:31.930 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:28:41.493 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=63%  H=1.32bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.263  P1/light:0.261  P2/standard:0.176  P3/deep:0.241
  Regret     : +0.0020  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-05 13:28:41.510 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:28:50.941 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=54%  H=1.35bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.273  P1/light:0.339  P2/standard:0.421  P3/deep:0.282
  Regret     : 0.0817  (regret +0.0817)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:28:50.970 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:02.900 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=57%  H=1.35bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0450  (regret +0.0450)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:29:02.917 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:11.356 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=48%  H=1.52bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0050  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-05 13:29:11.378 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:19.868 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=52%  H=1.48bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.287  P1/light:0.497  P2/standard:0.436  P3/deep:0.489
  Regret     : 0.0612  (regret +0.0612)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:29:19.911 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:28.402 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=74%  H=0.82bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:29:28.422 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:41.283 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=30%  H=1.44bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.195  P1/light:0.171  P2/standard:0.088  P3/deep:0.079
  Regret     : +0.0240  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-05 13:29:41.301 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:29:52.274 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=58%  H=0.98bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.117  P1/light:0.259  P2/standard:0.297  P3/deep:0.388
  Regret     : 0.0914  (regret +0.0914)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:29:52.292 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:03.601 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=50%  H=1.07bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.090  P1/light:0.222  P2/standard:0.258  P3/deep:0.288
  Regret     : 0.0304  (regret +0.0304)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:30:03.619 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:12.425 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=71%  H=0.87bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.086  P2/standard:0.102  P3/deep:0.110
  Regret     : +0.0982  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-05 13:30:12.440 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:19.721 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=29%  H=1.56bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.147  P1/light:0.322  P2/standard:0.088  P3/deep:0.102
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:30:19.732 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:27.759 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=84%  H=0.64bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.225  P1/light:0.210  P2/standard:0.405  P3/deep:0.286
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:30:27.798 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:34.822 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=100%  H=0.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : -0.0136  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-05 13:30:34.832 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:44.418 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=68%  H=1.23bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.200  P2/standard:0.174  P3/deep:0.247
  Regret     : 0.0469  (regret +0.0469)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:30:44.438 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:30:52.322 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=51%  H=1.47bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.217  P1/light:0.255  P2/standard:0.235  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:30:52.372 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:00.932 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=64%  H=0.94bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.164  P1/light:0.189  P2/standard:0.108  P3/deep:0.109
  Regret     : -0.0246  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-05 13:31:00.950 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:09.388 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=52%  H=1.47bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.194  P1/light:0.273  P2/standard:0.224  P3/deep:0.242
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:31:09.409 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:20.200 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=37%  H=0.95bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.220  P1/light:0.325  P2/standard:0.340  P3/deep:0.368
  Regret     : 0.0150  (regret +0.0150)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-05 13:31:20.225 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:29.762 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=24%  H=1.85bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-05 13:31:29.791 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:39.669 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=52%  H=1.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : 0.0313  (regret +0.0313)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-05 13:31:39.689 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:31:51.835 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=51%  H=1.36bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.377  P1/light:0.392  P2/standard:0.377  P3/deep:0.404
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-05 13:31:51.872 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:00.479 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=100%  H=0.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.333  P1/light:0.383  P2/standard:0.464  P3/deep:0.446
  Regret     : 0.0180  (regret +0.0180)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-05 13:32:00.495 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:10.297 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=78%  H=0.97bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.007  P1/light:-0.048  P2/standard:-0.026  P3/deep:-0.006
  Regret     : 0.0128  (regret +0.0128)
  Verdict    : ✗  MISS

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-05 13:32:10.323 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:30.090 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=34%  H=1.57bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.358  P1/light:0.374  P2/standard:0.365  P3/deep:0.411
  Regret     : 0.0363  (regret +0.0363)
  Verdict    : ✗  MISS

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-05 13:32:30.106 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:37.312 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=66%  H=1.08bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0077  (regret +0.0077)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-05 13:32:37.328 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:46.492 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=69%  H=0.89bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-05 13:32:46.524 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:32:57.778 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=100%  H=-0.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0926  (regret +0.0926)
  Verdict    : ✗  MISS

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-05 13:32:57.796 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:04.863 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.49bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.375  P2/standard:0.336  P3/deep:0.248
  Regret     : 0.0398  (regret +0.0398)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-05 13:33:04.879 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:08.550 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=80%  H=0.72bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.380  P1/light:0.486  P2/standard:0.459  P3/deep:0.488
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-05 13:33:08.573 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:13.453 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=-0.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0169  (regret +0.0169)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-05 13:33:13.474 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:18.514 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=86%  H=0.58bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.213  P1/light:0.277  P2/standard:0.312  P3/deep:0.315
  Regret     : -0.0032  (regret -0.0032)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-05 13:33:18.529 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:24.813 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=79%  H=0.74bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : -0.0009  (regret -0.0009)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-05 13:33:24.838 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:30.036 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=40%  H=0.97bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-05 13:33:30.058 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:35.674 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=63%  H=1.08bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.400  P1/light:0.560  P2/standard:0.475  P3/deep:0.514
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-05 13:33:35.726 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:33:42.119 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=50%  H=1.45bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.196  P1/light:0.372  P2/standard:0.312  P3/deep:0.339
  Regret     : 0.0600  (regret +0.0600)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-05 13:33:42.136 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:34:13.252 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=67%  H=1.13bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0107  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-05 13:34:13.271 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-05 13:34:23.075 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=86%  H=0.71bits
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
  07_reasoning_planning                          TEST    P3     —    P3  → P0    ✗ MISS
  13_agent_framework                             TEST    P1     —    P1  → P3    ✗ MISS
  14_agent_system_design                         TEST    P1     —    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P3     —    P3  → P1    ✗ MISS
  31_CI                                          TEST    P3     —    P3  → P1    ✗ MISS
  Bird_Eye_Extreme                               TEST    P2     —    P2  → P1    ~ NEAR
  Dark_Dimension                                 TEST    P3     —    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1     —    P1  → P3    ✗ MISS
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P2    ~ NEAR
  Gravity_Entropy                                TEST    P1     —    P1  → P2    ~ NEAR
  HNSW                                           TEST    P1     —    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P1    ✓ EXACT
  Space-Time_QECC                                TEST    P2     —    P2  → P1    ~ NEAR
  State_of_LLM_Reasoning                         TEST    P3     —    P3  → P0    ✗ MISS
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=4 (25%)  near=6 (38%)  miss=6 (38%)  no-oracle/error=0
  Ordinal MAE: 1.250
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0231  max=0.0926

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         0         0         2  (n=2)
  P1 light                        0         2         2         2  (n=6)
  P2 standard                     0         2         1         2  (n=5)
  P3 deep                         0         2         0         1  (n=3)

  --- Baselines ---
  Oracle distribution: P0=2  P1=6  P2=5  P3=3
  Majority-class baseline (always P1 light): 37.5%  (6/16)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  28.9%

================================================================================
  TRAIN (reference)  [RL-only]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN    P1     —    P1  → P0    ~ NEAR
  02_workflows_vs_agents__var_standard           TRAIN    P2     —    P2  → P1    ~ NEAR
  02_workflows_vs_agents__var_demanding          TRAIN    P3     —    P3  → P1    ✗ MISS
  03_context_engineering__var_minimal            TRAIN    P1     —    P1  → P0    ~ NEAR
  03_context_engineering__var_standard           TRAIN    P1     —    P1  → P2    ~ NEAR
  03_context_engineering__var_demanding          TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_minimal              TRAIN    P3     —    P3  → P0    ✗ MISS
  05_workflow_patterns__var_standard             TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P1  → P0    ~ NEAR
  06_tools__var_standard                         TRAIN    P2     —    P2  → P3    ~ NEAR
  06_tools__var_demanding                        TRAIN    P2     —    P2  → P3    ~ NEAR
  08_react_practice__var_minimal                 TRAIN    P3     —    P3  → P0    ✗ MISS
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P2     —    P2  → P2    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P3     —    P3  → P0    ✗ MISS
  09_RAG__var_standard                           TRAIN    P1     —    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P3     —    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P1     —    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P1     —    P1  → P2    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P3     —    P3  → P1    ✗ MISS
  11_multimodal__var_demanding                   TRAIN    P2     —    P2  → P2    ✓ EXACT

  n=24  exact=6 (25%)  near=12 (50%)  miss=6 (25%)  no-oracle/error=0
  Ordinal MAE: 1.125
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0387  max=0.2183

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         5         0         3  (n=8)
  P1 light                        0         3         3         2  (n=8)
  P2 standard                     0         2         2         0  (n=4)
  P3 deep                         0         1         2         1  (n=4)

  --- Baselines ---
  Oracle distribution: P0=8  P1=8  P2=4  P3=4
  Majority-class baseline (always P0 skip): 33.3%  (8/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  27.8%
  var_minimal      ( 8):  exact 0/8   exact+near 5/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 2/8   exact+near 6/8   regret mean=0.0388 max=0.0914
  var_demanding    ( 8):  exact 4/8   exact+near 7/8   regret mean=0.0386 max=0.2183

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=10 (25%)  near=18 (45%)  miss=12 (30%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0312  max=0.2183