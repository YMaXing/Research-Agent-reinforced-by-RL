================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:15:36.416 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:15:36.649 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-07 11:18:50.870 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-07 11:18:59.498 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=65%  H=0.93bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.285  P1/light:0.432  P2/standard:0.216  P3/deep:0.320
  Regret     : -0.1479  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-07 11:18:59.514 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:06.316 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=58%  H=1.35bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.344  P1/light:0.452  P2/standard:0.454  P3/deep:0.329
  Regret     : -0.0019  (regret -0.0019)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:19:06.331 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:12.943 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=30%  H=1.57bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.324  P1/light:0.457  P2/standard:0.387  P3/deep:0.238
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:19:12.956 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:21.816 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=43%  H=1.47bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.263  P1/light:0.261  P2/standard:0.176  P3/deep:0.241
  Regret     : +0.0020  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-07 11:19:21.835 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:30.609 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=56%  H=1.30bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.273  P1/light:0.339  P2/standard:0.421  P3/deep:0.282
  Regret     : 0.0817  (regret +0.0817)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:19:30.660 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:41.533 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=50%  H=1.32bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0241  (regret +0.0241)
  Verdict    : ✗  MISS

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:19:41.547 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:49.147 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=36%  H=1.46bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0118  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-07 11:19:49.178 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:19:56.937 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.55bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.287  P1/light:0.497  P2/standard:0.436  P3/deep:0.489
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:19:56.958 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:06.393 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=63%  H=0.95bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:20:06.404 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:16.402 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=34%  H=1.55bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.195  P1/light:0.171  P2/standard:0.088  P3/deep:0.079
  Regret     : +0.0240  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-07 11:20:16.419 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:26.413 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=49%  H=1.55bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.117  P1/light:0.259  P2/standard:0.297  P3/deep:0.388
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:20:26.435 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:36.804 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=46%  H=1.35bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.090  P1/light:0.222  P2/standard:0.258  P3/deep:0.288
  Regret     : 0.0304  (regret +0.0304)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:20:36.851 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:45.176 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=1.30bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.086  P2/standard:0.102  P3/deep:0.110
  Regret     : +0.1225  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-07 11:20:45.221 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:51.907 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=56%  H=0.99bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.147  P1/light:0.322  P2/standard:0.088  P3/deep:0.102
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:20:51.947 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:20:59.387 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=70%  H=1.18bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.225  P1/light:0.210  P2/standard:0.405  P3/deep:0.286
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:20:59.414 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:06.275 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=0%  H=1.36bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : +0.0204  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-07 11:21:06.290 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:14.643 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=41%  H=1.50bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.200  P2/standard:0.174  P3/deep:0.247
  Regret     : 0.0469  (regret +0.0469)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:21:14.669 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:21.987 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=43%  H=1.51bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.217  P1/light:0.255  P2/standard:0.235  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:21:22.011 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:29.932 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=54%  H=1.00bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.164  P1/light:0.189  P2/standard:0.108  P3/deep:0.109
  Regret     : -0.0246  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-07 11:21:29.960 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:37.708 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=60%  H=1.35bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.194  P1/light:0.273  P2/standard:0.224  P3/deep:0.242
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:21:37.718 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:45.751 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=56%  H=1.42bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.220  P1/light:0.325  P2/standard:0.340  P3/deep:0.368
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-07 11:21:45.767 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:21:56.039 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=41%  H=0.98bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-07 11:21:56.047 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:05.011 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=55%  H=0.99bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-07 11:22:05.059 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:14.398 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=23%  H=1.92bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.377  P1/light:0.392  P2/standard:0.377  P3/deep:0.404
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-07 11:22:14.406 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:23.845 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=52%  H=1.56bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.333  P1/light:0.383  P2/standard:0.464  P3/deep:0.446
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-07 11:22:23.852 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:32.796 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.79bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.007  P1/light:-0.048  P2/standard:-0.026  P3/deep:-0.006
  Regret     : 0.0552  (regret +0.0552)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-07 11:22:32.817 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:49.101 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=55%  H=1.42bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.358  P1/light:0.374  P2/standard:0.365  P3/deep:0.411
  Regret     : 0.0363  (regret +0.0363)
  Verdict    : ✗  MISS

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-07 11:22:49.127 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:22:57.374 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=81%  H=0.87bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0260  (regret +0.0260)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-07 11:22:57.423 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:05.837 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=50%  H=1.60bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-07 11:23:05.852 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:16.157 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.14bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-07 11:23:16.221 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:20.932 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=0.96bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.375  P2/standard:0.336  P3/deep:0.248
  Regret     : 0.1273  (regret +0.1273)
  Verdict    : ✗  MISS

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-07 11:23:20.977 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:24.361 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-07 11:23:24.376 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:30.433 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=78%  H=0.77bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0169  (regret +0.0169)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-07 11:23:30.453 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:35.016 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.213  P1/light:0.277  P2/standard:0.312  P3/deep:0.315
  Regret     : -0.0032  (regret -0.0032)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-07 11:23:35.047 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:40.754 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.41bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : -0.0009  (regret -0.0009)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-07 11:23:40.762 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:45.478 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-07 11:23:45.497 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:48.879 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=68%  H=0.90bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.400  P1/light:0.560  P2/standard:0.475  P3/deep:0.514
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-07 11:23:48.957 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:23:54.779 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=58%  H=0.98bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.196  P1/light:0.372  P2/standard:0.312  P3/deep:0.339
  Regret     : 0.0337  (regret +0.0337)
  Verdict    : ✗  MISS

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-07 11:23:54.794 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:24:23.131 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=21%  H=1.76bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0132  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-07 11:24:23.158 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-07 11:24:32.113 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=63%  H=1.00bits
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
  04_structured_outputs                          TEST    P2     —    P2  → P2    ✓ EXACT
  07_reasoning_planning                          TEST    P1     —    P1  → P0    ~ NEAR
  13_agent_framework                             TEST    P1     —    P1  → P3    ✗ MISS
  14_agent_system_design                         TEST    P3     —    P3  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P1     —    P1  → P1    ✓ EXACT
  31_CI                                          TEST    P1     —    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST    P3     —    P3  → P1    ✗ MISS
  Dark_Dimension                                 TEST    P3     —    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1     —    P1  → P3    ✗ MISS
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P2    ~ NEAR
  Gravity_Entropy                                TEST    P1     —    P1  → P2    ~ NEAR
  HNSW                                           TEST    P1     —    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1     —    P1  → P1    ✓ EXACT
  Space-Time_QECC                                TEST    P3     —    P3  → P1    ✗ MISS
  State_of_LLM_Reasoning                         TEST    P1     —    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=7 (44%)  near=5 (31%)  miss=4 (25%)  no-oracle/error=0
  Ordinal MAE: 0.812
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0194  max=0.1273

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         2         0         0  (n=2)
  P1 light                        0         4         0         2  (n=6)
  P2 standard                     0         1         2         2  (n=5)
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
  02_workflows_vs_agents__var_demanding          TRAIN    P1     —    P1  → P1    ✓ EXACT
  03_context_engineering__var_minimal            TRAIN    P1     —    P1  → P0    ~ NEAR
  03_context_engineering__var_standard           TRAIN    P1     —    P1  → P2    ~ NEAR
  03_context_engineering__var_demanding          TRAIN    P3     —    P3  → P1    ✗ MISS
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P1  → P0    ~ NEAR
  05_workflow_patterns__var_standard             TRAIN    P1     —    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P1  → P0    ~ NEAR
  06_tools__var_standard                         TRAIN    P3     —    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P2     —    P2  → P3    ~ NEAR
  08_react_practice__var_minimal                 TRAIN    P1     —    P1  → P0    ~ NEAR
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P2     —    P2  → P2    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P1     —    P1  → P0    ~ NEAR
  09_RAG__var_standard                           TRAIN    P1     —    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P3     —    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P1     —    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P2    ✓ EXACT
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P1     —    P1  → P1    ✓ EXACT
  11_multimodal__var_demanding                   TRAIN    P2     —    P2  → P2    ✓ EXACT

  n=24  exact=11 (46%)  near=11 (46%)  miss=2 (8%)  no-oracle/error=0
  Ordinal MAE: 0.625
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0113  max=0.0817

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         8         0         0  (n=8)
  P1 light                        0         6         1         1  (n=8)
  P2 standard                     0         1         3         0  (n=4)
  P3 deep                         0         1         1         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=8  P1=8  P2=4  P3=4
  Majority-class baseline (always P0 skip): 33.3%  (8/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  27.8%
  var_minimal      ( 8):  exact 0/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 5/8   exact+near 7/8   regret mean=0.0158 max=0.0817
  var_demanding    ( 8):  exact 6/8   exact+near 7/8   regret mean=0.0068 max=0.0304

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=18 (45%)  near=16 (40%)  miss=6 (15%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0152  max=0.1273