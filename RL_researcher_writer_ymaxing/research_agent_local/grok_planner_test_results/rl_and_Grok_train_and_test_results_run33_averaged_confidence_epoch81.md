================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:40:43.497 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:40:43.791 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-24 19:46:28.172 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run33_averaged_confidence/epochs/epoch_0081
2026-08-24 19:46:41.589 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=58%  H=1.10bits  [floor applied]
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint from external-evidence policy = forbidden requires P0 skip
               reasoning: External-evidence policy is explicitly FORBIDDEN (exploration output cannot be used); hard constraint mandates P0 regardless of scorer's P1-light recommendation (58% light / 46% deep mass), self-contained flags, or large residuals in S1-S3.
               drivers: external-evidence-policy, hard-constraint
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-24 19:46:41.637 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:47:09.058 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=36%  H=1.41bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (already cost-adjusted); vote is UNCERTAIN (36% top-pick, 52% standard / 13% deep mass). No sanctioned upward escalation from P1 (hard guard), downward override not met (standard mass >30%, S2/S3 show large residuals), 100% self-contained is only context. Dominant depth gaps and 42 unbacked anchors noted but do not trigger escalation per policy.
               drivers: RL aggregate P1, override policy gates, budget-weighted vote mass
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:47:09.202 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:47:28.298 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=72%  H=1.11bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Scorer aggregate is decisive P2 standard (72% vote mass on standard, 0% deep, low entropy). This matches dominant depth gaps in S2/S3 (residuals 42/0 and 34/0, must-ev 5+3) while highest-budget S5/S4 (29%+18%) already show full coverage (residual 0/0, cov 8·6); all sections self-contained. No sanctioned upward escalation (deep mass <30%) or downward override justified (large residuals in key sections, decisive vote). External-evidence allowed but not required; P2 hits the calibrated reward peak.
               drivers: decisive_72pct_standard_vote, balanced_residuals_in_high-budget_sections, dominant_depth_gaps_with_self-contained_context
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.274  P1/light:0.394  P2/standard:0.399  P3/deep:0.319
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:47:28.320 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:47:36.404 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=False)

  Policy     : forbidden
  RL model   : P0 skip      conf=79%  H=0.74bits  [floor applied]
  Grok 4.2   : P0 skip      [agrees with RL]
               reasoning: External-evidence policy is explicitly FORBIDDEN, triggering the hard constraint that mandates P0 skip. Section-scorer aggregate is also decisive P0 (79% skip vote mass, 0% standard, 21% deep <30% threshold); every section is self-contained, brief-flagged, and the guideline demands only surface-level conceptual overview with no external examples or depth.
               drivers: external-evidence-forbidden, decisive-P0-vote, all-sections-brief-self-contained
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-24 19:47:36.430 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:47:51.427 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=55%  H=1.45bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Scorer aggregate is P2 standard (55% budget-weighted standard mass, moderate but dominant arm); deep mass only 22% <30% so no sanctioned P2→P3; high-residual sections (S4 37/4, S1 27/2) exist yet strongest coverage is already in S6/S7/S8 and all sections self-contained, matching the cost-adjusted RL prior.
               drivers: RL aggregate P2, standard-mass 55%, deep-mass<30% gate
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.298  P2/standard:0.323  P3/deep:0.281
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:47:51.452 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:48:13.809 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.72bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (already cost-adjusted); UNCERTAIN (entropy 1.72) with vote mass standard 44%/deep 7%. No sanctioned override: not a P2 so P2->P3 escalation blocked; standard mass >30% prevents downward clause; high-budget residuals (S3 40/0, S4 14/2, S6 6/2+must-ev 12) and 48 unbacked anchors give no basis for P0. Self-contained flag noted but explicitly non-decisive. Decisive signal: budget-weighted section votes place peak at light given hard guardrails.
               drivers: RL aggregate P1, vote-mass gates, no sanctioned override, high residuals in S3/S4/S6
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:48:13.873 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:48:23.733 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=32%  H=1.36bits  [floor applied]
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: External-evidence policy explicitly requires P0 skip
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN mandates P0 (exploration output cannot be used). Scorer aggregate is P1 light (weak 32% top-pick mass, 56% skip mass) but policy overrides all votes, residual gaps, and self-contained flags. Guideline reinforces surface-level conceptual treatment with no external libs/cases allowed.
               drivers: external-evidence policy forbidden
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-24 19:48:23.812 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:48:41.198 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=54%  H=1.45bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: RL aggregate votes P2 (54% standard mass dominant); deep mass=26% blocks P2->P3 escalation per override policy. High-budget sections (S1/S2/S4) retain large residual depth (29/6, 37/6, 16/6) plus 41 unbacked anchors and dominant depth gaps, but no brief flags or near-zero residuals justify downward override. Self-contained flag is context only.
               drivers: RL aggregate P2 vote, deep-mass <30%, residual depth in S1/S3/S4/S7
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0672  (regret +0.0672)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:48:41.221 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:49:01.386 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.40bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (already cost-adjusted); vote split is uncertain (43% light / 45% standard / 12% deep) but deep-vote mass=12% <30% bars any P2→P3 escalation and standard mass >30% bars general downward override. All 100% of budget is self-contained with near-zero residual in 5/7 sections (only S1/S2 show large residual, yet their own RL picks are already light·1.00 and deep·1.00); dominant gap is depth but policy forbids escalating a P1 pick. No qualitative red flags in guideline override the calibrated scorer vote.
               drivers: RL-aggregate P1, vote-mass gates, universal self-containment + low residuals in high-budget sections
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:49:01.413 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:49:14.834 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=26%  H=1.89bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: external-evidence policy explicitly FORBIDDEN (hard constraint trumps RL pick and vote mass)
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN means exploration output cannot be used, mandating P0. Scorer aggregate is UNCERTAIN P1 (37% skip / 26% deep mass, entropy 1.89) but policy overrides all votes; 100% self-contained sections + pervasive 'must stay brief' flags and explicit 'surface-level / no external examples' guideline reinforce no new evidence needed.
               drivers: forbidden-policy, self-contained-flags, brevity-instructions
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-24 19:49:14.861 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:49:28.806 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=1.55bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Scorer aggregate is already P3 (61% deep-vote mass from S3/S4/S5/S6 totalling >60% budget) with high residual depth (e.g. S3 53/6, S4 32/6), 20+ must-ev in core impl sections, and dominant depth-gap type; uncertain entropy does not trigger downward override as high-budget sections are not well-covered and deep mass >>30%.
               drivers: scorer-P3-with-61pct-deep-mass, high-residual-depth-in-26pct+16pct-sections, no-downward-criteria-met
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:49:28.874 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:49:50.798 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=69%  H=1.17bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is P1 light (69% budget-weighted vote mass; moderate/not decisive). Standard mass 22% and deep mass 9% fall below all escalation gates; no P2→P3 sanction possible from a P1 pick and no general-downward conditions met (S3 24% and S4 15% retain high residual 47/2 and 28/2 plus must-ev/orphans). RL pick already cost-adjusted; self-contained flags supply context but do not override.
               drivers: budget-weighted vote mass (69% light), no qualifying override (P1 guard + residual pattern), RL aggregate already cost-adjusted
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:49:50.825 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:49:59.773 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=0.87bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard policy constraint overrides the RL pick of P1
               reasoning: HARD CONSTRAINT: external-evidence policy=FORBIDDEN mandates P0 (exploration output cannot be used). Scorer aggregate is already weak (71% skip, 29% light) on a 100% self-contained article whose guideline repeatedly demands 'must stay brief', surface-level treatment, and no external sources.
               drivers: external-evidence-forbidden, 71% skip vote mass, all-sections-self-contained, brevity-must-stay-brief
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-24 19:49:59.807 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:50:25.394 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.44bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (49% light mass, 14% deep, 0% standard) after upstream cost adjustment; vote is uncertain but has a clear light lean. All sections self-contained; deep mass far below 30% gate so no P2/P3 escalation permitted from a P1 pick. High-budget S5 is brief-flagged and S5/S6 show low residual, supporting no upward move while dominant gap type and per-section votes already baked into the P1 recommendation.
               drivers: RL aggregate P1 light, light-vote dominance at 49%, deep mass 14% <30%, universal self-contained flag
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:50:25.420 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:50:48.315 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.73bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL vote is P1 light (49% budget-weighted light mass, 28% standard, 9% deep); uncertain entropy but light is clear plurality. No sanctioned override applies: deep mass <<30%, cannot escalate P1 to P2/P3 per hard guard, downward conditions not met given high residuals in S5/S6 (largest budgets) and dominant light arm. Self-contained flags and S5 brief flag noted but already baked into the cost-adjusted P1 pick.
               drivers: aggregate RL vote mass, vote-mass gates <30%, no qualifying override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:50:48.418 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:51:05.651 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.54bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard external-evidence policy = forbidden requires P0 regardless of scorer recommendation
               reasoning: External-evidence policy is explicitly FORBIDDEN, mandating P0 skip per hard constraints (overrides scorer's uncertain P3 vote, 43% deep mass, all self-contained sections, and residual gaps). Guideline demands only conceptual overview with surface-level treatment and no external examples.
               drivers: external-evidence-forbidden, policy-hard-constraint, self-contained-flags
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-24 19:51:05.754 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:51:26.683 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.91bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is P1 light (UNCERTAIN, 41% standard / 20% deep mass); no sanctioned override fits (cannot escalate P1 per hard guard; downward conditions unmet due to S3/S4 must-ev=13, residuals, and dominant standard arm). Self-contained flags and brief sections provide context but RL pick already cost-adjusted.
               drivers: scorer-aggregate-P1, vote-mass-gates, no-sanctioned-override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0342  (regret +0.0342)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:51:26.740 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:51:46.575 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=52%  H=1.27bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Aggregate RL vote is P3 (52% deep, 45% budget-weighted deep mass >30% bar). UNCERTAIN (moderate confidence, 44% skip) but no sanctioned downward override applies: highest-budget sections (S4 26%, S3 19%) show large residual depth (20/0, 54/2), 42 unbacked anchors, dominant depth gaps, and 6+ must-ev items. Self-contained flags do not override given the guideline's many named-model, production-example, and failure-mode requirements already baked into the cost-adjusted P3 pick.
               drivers: budget-weighted deep mass 45%, high residual depth in S3/S4, 42 unbacked anchors + must-ev
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:51:46.667 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:51:55.657 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=61%  H=0.97bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint from external-evidence policy = forbidden overrides the RL pick of P1
               reasoning: External-evidence policy is explicitly FORBIDDEN, which is a hard constraint mandating P0 skip regardless of the section-scorer's P1 recommendation (39% skip / 61% light). All sections are self-contained, flagged 'brief', and the guideline demands only a conceptual overview with no external libraries, case studies or production code; residual needs cannot be addressed via exploration anyway.
               drivers: external-evidence policy, self-contained flags, brevity requirements
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-24 19:51:55.755 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:52:19.854 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=48%  H=1.00bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate (already cost-adjusted) is P1 light with moderate confidence (48% light / 52% standard split); this is uncertain but the OVERRIDE POLICY bars any escalation from a P1 pick and the downward conditions are not met (standard-vote mass = 52% > 30% threshold and multiple high-budget sections (S1/S3/S4) retain large residual depth). 100% self-contained flag and dominant depth gaps supply context only and do not trigger re-derivation. External-evidence policy is ALLOWED, not required.
               drivers: scorer_aggregate_P1, override_policy_compliance, residual_need_context
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:52:19.877 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:52:56.202 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Aggregate scorer vote is decisive for P2 (81% standard, 0% deep, 81% standard-vote mass). This already balances high residual depth (24-29) in high-budget sections S1-S5 (74% total budget) plus must-ev counts against exploration cost. All sections self-contained yet scorer still picked standard for S2/S3/S4/S6; no uncertain vote, no deep-mass >=30%, and no high-budget brief-flags to trigger downward override. Dominant gap type is depth, so standard (depth->breadth) fits without escalation.
               drivers: decisive P2 scorer vote, standard-vote mass 81%, residual depth in S1-S5
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:52:56.258 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:53:05.924 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.58bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: External-evidence policy explicitly requires P0; overrides scorer's P1
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN mandates P0 skip (exploration output cannot be used). Scorer aggregate is uncertain P1 (38% light, 31% skip, 31% standard) with 100% self-contained sections and many 'brief' flags; override applies per policy.
               drivers: external-evidence policy, hard constraints, self-contained flags
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-24 19:53:06.036 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:53:35.043 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=37%  H=1.62bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is P1 light (UNCERTAIN, entropy 1.62; budget-weighted: skip 47%, light 38%, standard 10%, deep 6%). Deep- and standard-vote masses (6%/10%) below 30% gate, no sanctioned upward move from P1. 100% self-contained + many sections already at cov ≥5 support no general downward override to P0, as high-budget S3 (23%, resid 46/2) and S1 are not well-covered. Dominant gap is depth but RL pick already cost-adjusted; P1 is the calibrated peak.
               drivers: scorer_aggregate_P1, low_escalation_masses, high_self_contained_sections, residual_context_not_triggering_downward
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.0356  (regret +0.0356)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:53:35.075 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:53:50.831 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=52%  H=1.75bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Scorer aggregate is P2 standard (UNCERTAIN, entropy 1.75) with 52% standard-vote mass dominant and only 15% deep mass; this fails the >=30% deep-mass gate for sanctioned P2->P3 escalation. High-budget sections S3 (23%, resid 44/2, must-ev 4), S5 (15%, resid 25/0, must-ev 6) and S2 (13%, resid 20/0, must-ev 5) show depth-dominant residuals yet self-contained coverage already achieved, aligning with the RL pick's 2-round depth-then-breadth preset. No general downward override applies given the clear standard-mass signal and non-zero residuals in 77% of budget.
               drivers: budget-weighted standard mass 52%, P2 RL aggregate, deep-mass <30% gate, residual depth in S3/S5
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-24 19:53:50.915 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:54:10.608 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.34bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Scorer aggregate is already P3 (60% deep-vote mass, 0% standard); this is uncertain (<70%) but has dominant deep arm. Largest-budget sections (S4 40%, S3 20%) both vote deep·1.00 with must-ev counts 14+8, cov only 5·3, and residual depth 16/11; dominant gap type is depth and external-evidence is ALLOWED. No sanctioned downward override applies (high-budget impl sections neither brief-flagged nor well-covered).
               drivers: budget-weighted deep mass from S3/S4, high must-ev + residual depth in core hands-on sections, dominant depth-gap economics
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.276  P1/light:0.315  P2/standard:0.350  P3/deep:0.350
  Regret     : -0.0000
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-24 19:54:10.685 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:54:42.562 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=31%  H=1.79bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (already cost-adjusted); uncertain (entropy 1.79) but deep-vote mass only 9% and standard mass, while 44%, does not trigger sanctioned escalation from a P1. 100% self-contained sections plus strong coverage (resid near 0, cov depth >=5) on the two largest sections (S5 22%, S7 24%) support no upward move; high residuals are confined to smaller/brief-flagged sections already factored into the scorer.
               drivers: RL aggregate P1, vote-mass gates (deep 9%<30%), self-contained + low-resid on high-budget sections
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.050  P1/light:0.001  P2/standard:0.002  P3/deep:0.033
  Regret     : 0.0495  (regret +0.0495)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-24 19:54:42.588 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:55:15.659 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.84bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (already cost-adjusted); uncertain (entropy 1.84 bits) with standard mass 39% / light 32% / deep mass only 9%. No sanctioned override applies: cannot escalate P1 to P2 per hard guard, deep-vote mass <30%, standard mass >30% blocks general downward, and high-residual sections (S4 41/4, S1–S3) do not trigger escalation on raw counts. All sections self-contained with strong cov on deep dives (S5–S15 mostly resid 0) confirms P1 as reward peak.
               drivers: aggregate RL pick, vote-mass gates, self-contained + residual context, no-sanctioned-override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.348  P1/light:0.395  P2/standard:0.373  P3/deep:0.391
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-24 19:55:15.735 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:55:32.620 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=88%  H=0.54bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate is decisively P1 light (88% budget-weighted vote on light; 0% deep, 12% standard) with all high-budget sections (S2/S3/S4 = 81% of total) voting light·1.00. 100% of budget is self-contained, coverage already 6-7/8 depth, residuals reflect universal gap pressure the RL scorer has already cost-adjusted. External-evidence policy is ALLOWED not required; no sanctioned upward override applies to a P1 pick.
               drivers: decisive 88% light vote mass, self-contained + solid cov scores, no escalation gates met
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.268  P1/light:0.370  P2/standard:0.398  P3/deep:0.348
  Regret     : 0.0279  (regret +0.0279)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-24 19:55:32.668 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:55:52.977 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.32bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Section-scorer aggregate is P3 (60% deep-vote mass, moderate confidence); high-budget sections S2 (35%, RL=deep, resid 17/6) and S5 (18%, RL=deep, resid 17/6) drive the mass above the 30% gate; dominant gap type is depth with 47 unbacked anchors; 100% self-contained is noted but explicitly not a downward trigger per policy as RL pick already cost-adjusted; no sanctioned override applies.
               drivers: budget-weighted deep mass 60%, high-residual large sections S2/S5, dominant depth gaps
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-24 19:55:53.015 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:56:18.014 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.36bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is P1 light (57% light, 31% standard, 0% deep; moderate/UNCERTAIN). No sanctioned upward move from P1 (hard guard; deep mass=0%). Downward to P0 not triggered: high-budget S6 (31%, standard vote, resid 2/6) and multiple must-ev sections lack near-zero residuals or depth_score>=6. Self-contained flag and raw gaps do not override the already cost-adjusted RL pick.
               drivers: scorer_aggregate_P1, no_sanctioned_override, high_budget_section_S6
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-24 19:56:18.069 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:56:39.312 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=51%  H=1.47bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Section-scorer aggregate is P1 light (51% light, 29% deep mass) and is UNCERTAIN (moderate 51% top-pick, entropy >0). No sanctioned upward move from P1 is allowed per hard guard; deep-vote mass sits at 29% (below 30% bar) and standard mass is 0%. All sections self-contained, residuals high but already reflected in the cost-adjusted RL pick; no brief flags or qualitative guideline cues justify downward override to P0.
               drivers: scorer-aggregate, vote-mass-gates, self-contained-flags, residual-need-context
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.275  P1/light:0.361  P2/standard:0.369  P3/deep:0.289
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-24 19:56:39.365 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:57:10.503 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.51bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Aggregate RL pick is P3 deep (UNCERTAIN, 46% deep-vote mass). Largest section (S3, 46% budget) votes deep with high residual (23/4), 8 must-ev, 9 orphans; dominant gap type is depth. Downward override disallowed: deep mass >30%, residuals not near zero, not all high-budget sections well-covered despite self-contained flags and brief=yes on S3. Stick to calibrated peak.
               drivers: budget-weighted deep mass 46%, S3 RL deep pick + residuals, no sanctioned downward conditions met
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.341  P1/light:0.517  P2/standard:0.511  P3/deep:0.559
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-24 19:57:10.653 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:57:32.208 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=0.99bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is already-cost-adjusted P1 light (moderate confidence, 45% light / 55% standard vote mass, 0% deep mass). All 100% of budget is in self-contained sections; no sanctioned upward escalation from P1 is allowed per hard guard and OVERRIDE POLICY, while downward to P0 is blocked because standard-vote mass >30%. Residual needs and must-ev counts are high but explicitly not to be used for raw-gap escalation.
               drivers: RL aggregate pick, vote-mass gates, self-contained + residual context
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.335  P1/light:0.457  P2/standard:0.449  P3/deep:0.453
  Regret     : -0.0036  (regret -0.0036)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-24 19:57:32.306 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:57:48.046 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Decisive scorer aggregate (P3, 72% deep mass) from S2/S3 (72% budget) with high residual depth (27), must-ev (13), and 27 unbacked anchors; matches guideline needs for mission/experiment specifics; no override justified on decisive vote or residual context.
               drivers: scorer_decisive_P3, deep_vote_mass_72pct, S2_S3_residual_mustev
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.285  P1/light:0.361  P2/standard:0.304  P3/deep:0.426
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-24 19:57:48.220 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:57:57.889 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=0.00bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is decisive P1 (100% light vote mass, all sections self-vote light·1.00). Deep/standard masses are 0% (no escalation gate met). 100% budget in self-contained sections with positive residuals and must-ev items already baked into the cost-adjusted RL pick; no sanctioned override conditions triggered. External-evidence policy is ALLOWED not required.
               drivers: decisive scorer vote, zero escalation mass, self-contained residuals
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.362  P1/light:0.425  P2/standard:0.412  P3/deep:0.338
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-24 19:57:57.932 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:58:16.790 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=95%  H=0.27bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Section-scorer aggregate is P1 light (DECISIVE at 95% budget-weighted vote mass, 0% standard or deep, all per-section RL picks skip/light). Override policy bars any escalation of a P1 pick; high-budget S4 residual (54/2, must-ev=12) and article-wide 40 unbacked anchors already factored into the cost-adjusted RL recommendation, with no sanctioned downward conditions met (vote decisive, S4 neither brief nor well-covered).
               drivers: decisive 95% light vote mass, hard no-escalation guard on P1
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-24 19:58:16.927 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:58:33.386 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=76%  H=0.79bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is decisive P1 (76% light mass on 77% of budget); deep mass only 24% (<30% gate) with all sections self-contained; no sanctioned override applies per policy (S3 residual high but outweighed; S1 explicitly brief). Dominant gap is depth but already factored into the RL pick.
               drivers: decisive scorer vote, budget-weighted light mass, no qualifying override condition
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.360  P1/light:0.519  P2/standard:0.473  P3/deep:0.579
  Regret     : 0.0599  (regret +0.0599)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-24 19:58:33.415 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:59:01.836 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=42%  H=1.32bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (moderate confidence, standard mass 50% but deep mass 0%); hard policy guard forbids any P1-to-P2 escalation; high residuals/must-ev in S1 (34%, resid 10/8) and S4 (18%, resid 11/4) plus 24 unbacked anchors prevent sanctioned downward override despite self-contained flags on 100% budget.
               drivers: scorer_aggregate_P1, no_sanctioned_override, residuals_in_key_sections
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.299  P1/light:0.394  P2/standard:0.359  P3/deep:0.336
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-24 19:59:01.879 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:59:21.560 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=25%  H=1.80bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard policy override (forbidden external evidence) forces P0 despite RL pick of P1
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN requires P0 skip regardless of the uncertain P1 aggregate vote (36% skip / 25% light / 6% standard / 33% deep mass). All sections already self-contained with provided golden/other sources covering the 72 unbacked anchors; no exploration output can be used.
               drivers: external-evidence-forbidden, self-contained sections, provided sources
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-24 19:59:21.576 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:59:38.186 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=True)

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.26bits
  Grok 4.2   : P3 deep      [OVERRIDE]
               reason: P2->P3 escalation triggered by uncertain vote + deep mass >=30% per override policy (S5 dominance)
               reasoning: Aggregate RL vote is P2 standard (moderate/uncertain at 49% standard, 45% deep mass). Sanctioned P2->P3 escalation applies because vote is uncertain, RL pick=P2, and deep-vote mass=45% (>=30% threshold); decisive driver is S5 (45% budget, RL=deep, resid 42/0 depth, must-ev=12, orphans=16) plus article-wide depth-dominant gaps (42 unbacked anchors). Self-contained flags and residuals already baked into the upstream RL pick; no downward override warranted.
               drivers: budget-weighted deep mass 45%, S5 residual depth 42 + must-ev 12, uncertain moderate vote
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.383  P2/standard:0.400  P3/deep:0.368
  Regret     : 0.0320  (regret +0.0320)
  Verdict    : ~  NEAR MISS  (±1 preset)
2026-08-24 19:59:38.262 | INFO     | logging:callHandlers:1762 | Stopping stale infer server (adapter changed)…

================================================================================
  TEST  (held-out, primary metric)  [RL + Grok 4.2]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST    P3    P3    P3  → P2    ~ NEAR
  07_reasoning_planning                          TEST    P1    P1    P1  → P0    ~ NEAR
  13_agent_framework                             TEST    P1    P1    P1  → P1    ✓ EXACT
  14_agent_system_design                         TEST    P1    P1    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST    P3    P3    P3  → P1    ✗ MISS
  31_CI                                          TEST    P1    P1    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST    P1    P1    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST    P3    P3    P3  → P3    ✓ EXACT
  Distinct_AI_Models                             TEST    P1    P1    P1  → P3    ✗ MISS
  Earth_Oceans_Origin                            TEST    P3    P3    P3  → P3    ✓ EXACT
  Gravity_Entropy                                TEST    P1    P1    P1  → P1    ✓ EXACT
  HNSW                                           TEST    P1    P1    P1  → P1    ✓ EXACT
  Insects_Consciousness                          TEST    P1    P1    P1  → P3    ✗ MISS
  Space-Time_QECC                                TEST    P1    P1    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST    P1    P0    P0  → P0    ✓ EXACT
  Understanding_Reasoning_LLMs                   TEST    P2    P3    P3  → P2    ~ NEAR

  n=16  exact=9 (56%)  near=4 (25%)  miss=3 (19%)  no-oracle/error=0
  Ordinal MAE: 0.625
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0155  max=0.0667

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         1         0         0  (n=2)
  P1 light                        0         6         0         1  (n=7)
  P2 standard                     0         1         0         2  (n=3)
  P3 deep                         0         2         0         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=2  P1=7  P2=3  P3=4
  Majority-class baseline (always P1 light): 43.8%  (7/16)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  30.5%

================================================================================
  TRAIN (reference)  [RL + Grok 4.2]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN    P1    P0    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN    P1    P1    P1  → P1    ✓ EXACT
  02_workflows_vs_agents__var_demanding          TRAIN    P2    P2    P2  → P2    ✓ EXACT
  03_context_engineering__var_minimal            TRAIN    P0    P0    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN    P2    P2    P2  → P2    ✓ EXACT
  03_context_engineering__var_demanding          TRAIN    P1    P1    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_minimal              TRAIN    P1    P0    P0  → P0    ✓ EXACT
  05_workflow_patterns__var_standard             TRAIN    P2    P2    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN    P1    P1    P1  → P1    ✓ EXACT
  06_tools__var_minimal                          TRAIN    P1    P0    P0  → P0    ✓ EXACT
  06_tools__var_standard                         TRAIN    P3    P3    P3  → P3    ✓ EXACT
  06_tools__var_demanding                        TRAIN    P1    P1    P1  → P1    ✓ EXACT
  08_react_practice__var_minimal                 TRAIN    P1    P0    P0  → P0    ✓ EXACT
  08_react_practice__var_standard                TRAIN    P1    P1    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN    P1    P1    P1  → P1    ✓ EXACT
  09_RAG__var_minimal                            TRAIN    P3    P0    P0  → P0    ✓ EXACT
  09_RAG__var_standard                           TRAIN    P1    P1    P1  → P3    ✗ MISS
  09_RAG__var_demanding                          TRAIN    P3    P3    P3  → P3    ✓ EXACT
  10_memory_knowledge_access__var_minimal        TRAIN    P1    P0    P0  → P0    ✓ EXACT
  10_memory_knowledge_access__var_standard       TRAIN    P1    P1    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN    P2    P2    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN    P1    P0    P0  → P0    ✓ EXACT
  11_multimodal__var_standard                    TRAIN    P1    P1    P1  → P0    ~ NEAR
  11_multimodal__var_demanding                   TRAIN    P2    P2    P2  → P2    ✓ EXACT

  n=24  exact=20 (83%)  near=3 (12%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.208
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0109  max=0.0672

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         1         0         0  (n=9)
  P1 light                        0         7         1         0  (n=8)
  P2 standard                     0         0         3         0  (n=3)
  P3 deep                         0         1         1         2  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 5/8   exact+near 7/8   regret mean=0.0171 max=0.0672
  var_demanding    ( 8):  exact 7/8   exact+near 8/8   regret mean=0.0048 max=0.0382

################################################################################
  COMBINED  [RL + Grok 4.2]  (n=40)
################################################################################
  n=40  exact=29 (72%)  near=7 (18%)  miss=4 (10%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0131  max=0.0672