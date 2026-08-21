================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:21:26.019 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:21:26.179 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-06 09:24:57.565 | INFO     | logging:callHandlers:1762 | Infer server is ready.
2026-08-06 09:25:05.307 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-06 09:25:05.326 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:12.765 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=75%  H=1.05bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.344  P1/light:0.452  P2/standard:0.454  P3/deep:0.329
  Regret     : -0.0019  (regret -0.0019)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:25:12.786 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:20.278 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=40%  H=1.37bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.324  P1/light:0.457  P2/standard:0.387  P3/deep:0.238
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:25:20.297 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:31.077 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=56%  H=1.44bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.263  P1/light:0.261  P2/standard:0.176  P3/deep:0.241
  Regret     : +0.0215  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-06 09:25:31.095 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:40.629 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=70%  H=1.09bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.273  P1/light:0.339  P2/standard:0.421  P3/deep:0.282
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:25:40.647 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:50.632 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=30%  H=1.58bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.265  P1/light:0.339  P2/standard:0.294  P3/deep:0.315
  Regret     : 0.0450  (regret +0.0450)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:25:50.683 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:25:59.141 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=36%  H=1.93bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.288  P1/light:0.276  P2/standard:0.294  P3/deep:0.283
  Regret     : +0.0118  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-06 09:25:59.152 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:08.856 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=73%  H=1.11bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.287  P1/light:0.497  P2/standard:0.436  P3/deep:0.489
  Regret     : 0.0612  (regret +0.0612)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:26:08.881 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:17.314 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=47%  H=1.00bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.254  P1/light:0.528  P2/standard:0.498  P3/deep:0.474
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:26:17.342 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:28.271 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=42%  H=1.45bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.195  P1/light:0.171  P2/standard:0.088  P3/deep:0.079
  Regret     : +0.0240  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-06 09:26:28.288 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:40.355 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=52%  H=1.41bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.117  P1/light:0.259  P2/standard:0.297  P3/deep:0.388
  Regret     : 0.0914  (regret +0.0914)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:26:40.372 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:51.704 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.19bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.090  P1/light:0.222  P2/standard:0.258  P3/deep:0.288
  Regret     : 0.0304  (regret +0.0304)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:26:51.747 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:26:59.058 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=33%  H=1.58bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.086  P2/standard:0.102  P3/deep:0.110
  Regret     : +0.1225  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-06 09:26:59.101 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:06.469 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=91%  H=0.44bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.147  P1/light:0.322  P2/standard:0.088  P3/deep:0.102
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:27:06.488 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:15.653 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=85%  H=0.61bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.225  P1/light:0.210  P2/standard:0.405  P3/deep:0.286
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:27:15.709 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:23.246 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=48%  H=1.50bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.130  P2/standard:0.163  P3/deep:0.164
  Regret     : -0.0136  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-06 09:27:23.256 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:30.748 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=66%  H=1.17bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.088  P1/light:0.200  P2/standard:0.174  P3/deep:0.247
  Regret     : 0.0725  (regret +0.0725)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:27:30.799 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:38.788 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=28%  H=1.56bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.217  P1/light:0.255  P2/standard:0.235  P3/deep:0.265
  Regret     : 0.0294  (regret +0.0294)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:27:38.812 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:48.535 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=64%  H=1.29bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.164  P1/light:0.189  P2/standard:0.108  P3/deep:0.109
  Regret     : -0.0246  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-06 09:27:48.555 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:27:57.056 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=62%  H=1.33bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.194  P1/light:0.273  P2/standard:0.224  P3/deep:0.242
  Regret     : 0.0488  (regret +0.0488)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:27:57.075 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:05.927 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.220  P1/light:0.325  P2/standard:0.340  P3/deep:0.368
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-06 09:28:05.959 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:16.568 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P1 light     conf=41%  H=1.84bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.138  P1/light:0.177  P2/standard:0.068  P3/deep:0.044
  Regret     : -0.0390  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-06 09:28:16.591 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:26.473 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=53%  H=1.46bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.390  P1/light:0.417  P2/standard:0.216  P3/deep:0.385
  Regret     : 0.0313  (regret +0.0313)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-06 09:28:26.488 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:36.700 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=47%  H=1.44bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.377  P1/light:0.392  P2/standard:0.377  P3/deep:0.404
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-06 09:28:36.716 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:45.364 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=53%  H=1.28bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.333  P1/light:0.383  P2/standard:0.464  P3/deep:0.446
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-06 09:28:45.381 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:28:56.281 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.80bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.007  P1/light:-0.048  P2/standard:-0.026  P3/deep:-0.006
  Regret     : 0.0128  (regret +0.0128)
  Verdict    : ✗  MISS

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-06 09:28:56.306 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:14.197 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=49%  H=1.50bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.358  P1/light:0.374  P2/standard:0.365  P3/deep:0.411
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-06 09:29:14.220 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:22.581 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=62%  H=1.32bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.294  P1/light:0.410  P2/standard:0.418  P3/deep:0.392
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-06 09:29:22.597 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:31.815 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=91%  H=0.43bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-06 09:29:31.831 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:43.121 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=59%  H=1.17bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0926  (regret +0.0926)
  Verdict    : ✗  MISS

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-06 09:29:43.141 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:48.273 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

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
2026-08-06 09:29:48.294 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:52.032 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=66%  H=0.93bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.380  P1/light:0.486  P2/standard:0.459  P3/deep:0.488
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-06 09:29:52.062 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:29:58.040 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=1.53bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P3 deep
  R_w        : P0/skip:0.350  P1/light:0.492  P2/standard:0.468  P3/deep:0.509
  Regret     : 0.0169  (regret +0.0169)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-06 09:29:58.061 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:03.103 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=0.86bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.213  P1/light:0.277  P2/standard:0.312  P3/deep:0.315
  Regret     : -0.0032  (regret -0.0032)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-06 09:30:03.134 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:09.409 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=56%  H=1.43bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P2 standard
  R_w        : P0/skip:0.364  P1/light:0.422  P2/standard:0.421  P3/deep:0.360
  Regret     : -0.0009  (regret -0.0009)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-06 09:30:09.429 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:14.630 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=95%  H=0.27bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P2 standard  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.1273  (regret +0.1273)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-06 09:30:14.648 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:18.338 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P1 light     conf=64%  H=1.09bits  [floor applied]
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P1 light  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.400  P1/light:0.560  P2/standard:0.475  P3/deep:0.514
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-06 09:30:18.361 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:24.711 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P3 deep      conf=74%  H=0.84bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P1 light
  R_w        : P0/skip:0.196  P1/light:0.372  P2/standard:0.312  P3/deep:0.339
  Regret     : 0.0337  (regret +0.0337)
  Verdict    : ✗  MISS

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-06 09:30:24.729 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:30:55.189 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : forbidden
  RL model   : P3 deep      conf=55%  H=1.43bits
  Grok 4.2   : (skipped — --rl-only / --rl-guards-only or XAI_API_KEY not set)
  -> Chosen  : P3 deep  (by RL)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0107  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✗  MISS

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-06 09:30:55.236 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-06 09:31:06.175 | INFO     | logging:callHandlers:1762 | rl_only=True; skipping Grok planner stage.

  Policy     : allowed
  RL model   : P2 standard  conf=88%  H=0.65bits
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
  07_reasoning_planning                          TEST    P3     —    P3  → P0    ✗ MISS
  13_agent_framework                             TEST    P3     —    P3  → P3    ✓ EXACT
  14_agent_system_design                         TEST    P2     —    P2  → P2    ✓ EXACT
  29_evaluation_metrics                          TEST    P3     —    P3  → P1    ✗ MISS
  31_CI                                          TEST    P3     —    P3  → P1    ✗ MISS
  Bird_Eye_Extreme                               TEST    P2     —    P2  → P1    ~ NEAR
  Dark_Dimension                                 TEST    P3     —    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1     —    P1  → P3    ✗ MISS
  Earth_Oceans_Origin                            TEST    P3     —    P3  → P2    ~ NEAR
  Gravity_Entropy                                TEST    P1     —    P1  → P2    ~ NEAR
  HNSW                                           TEST    P2     —    P2  → P1    ~ NEAR
  Insects_Consciousness                          TEST    P1     —    P1  → P1    ✓ EXACT
  Space-Time_QECC                                TEST    P3     —    P3  → P1    ✗ MISS
  State_of_LLM_Reasoning                         TEST    P3     —    P3  → P0    ✗ MISS
  Understanding_Reasoning_LLMs                   TEST    P2     —    P2  → P2    ✓ EXACT

  n=16  exact=6 (38%)  near=4 (25%)  miss=6 (38%)  no-oracle/error=0
  Ordinal MAE: 1.125
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0257  max=0.1273

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         0         0         2  (n=2)
  P1 light                        0         1         2         3  (n=6)
  P2 standard                     0         1         3         1  (n=5)
  P3 deep                         0         1         0         2  (n=3)

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
  03_context_engineering__var_minimal            TRAIN    P3     —    P3  → P0    ✗ MISS
  03_context_engineering__var_standard           TRAIN    P2     —    P2  → P2    ✓ EXACT
  03_context_engineering__var_demanding          TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_minimal              TRAIN    P1     —    P1  → P0    ~ NEAR
  05_workflow_patterns__var_standard             TRAIN    P2     —    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN    P1     —    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1     —    P1  → P0    ~ NEAR
  06_tools__var_standard                         TRAIN    P2     —    P2  → P3    ~ NEAR
  06_tools__var_demanding                        TRAIN    P2     —    P2  → P3    ~ NEAR
  08_react_practice__var_minimal                 TRAIN    P1     —    P1  → P0    ~ NEAR
  08_react_practice__var_standard                TRAIN    P1     —    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P2     —    P2  → P2    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P3     —    P3  → P0    ✗ MISS
  09_RAG__var_standard                           TRAIN    P2     —    P2  → P3    ~ NEAR
  09_RAG__var_demanding                          TRAIN    P2     —    P2  → P3    ~ NEAR
  10_memory_knowledge_access__var_minimal        TRAIN    P1     —    P1  → P0    ~ NEAR
  10_memory_knowledge_access__var_standard       TRAIN    P2     —    P2  → P1    ~ NEAR
  10_memory_knowledge_access__var_demanding      TRAIN    P2     —    P2  → P2    ✓ EXACT
  11_multimodal__var_minimal                     TRAIN    P1     —    P1  → P0    ~ NEAR
  11_multimodal__var_standard                    TRAIN    P3     —    P3  → P1    ✗ MISS
  11_multimodal__var_demanding                   TRAIN    P2     —    P2  → P2    ✓ EXACT

  n=24  exact=7 (29%)  near=14 (58%)  miss=3 (12%)  no-oracle/error=0
  Ordinal MAE: 0.917
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0255  max=0.0914

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         6         0         2  (n=8)
  P1 light                        0         3         4         1  (n=8)
  P2 standard                     0         0         4         0  (n=4)
  P3 deep                         0         0         4         0  (n=4)

  --- Baselines ---
  Oracle distribution: P0=8  P1=8  P2=4  P3=4
  Majority-class baseline (always P0 skip): 33.3%  (8/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  27.8%
  var_minimal      ( 8):  exact 0/8   exact+near 6/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 2/8   exact+near 7/8   regret mean=0.0379 max=0.0914
  var_demanding    ( 8):  exact 5/8   exact+near 8/8   regret mean=0.0131 max=0.0450

################################################################################
  COMBINED  [RL-only]  (n=40)
################################################################################
  n=40  exact=13 (32%)  near=18 (45%)  miss=9 (22%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0256  max=0.1273