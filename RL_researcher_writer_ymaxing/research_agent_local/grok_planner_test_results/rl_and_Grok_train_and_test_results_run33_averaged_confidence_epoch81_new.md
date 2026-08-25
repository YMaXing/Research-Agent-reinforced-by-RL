================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:06:35.018 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:06:35.181 | INFO     | logging:callHandlers:1762 | Starting infer.py HTTP server (this will load the model — ~5-10 min on first call over /mnt/f/)…
2026-08-24 21:09:46.966 | INFO     | logging:callHandlers:1762 | Infer server is ready. Serving adapter: /mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/checkpoints/tasks/run33_averaged_confidence/epochs/epoch_0081
2026-08-24 21:10:04.783 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=58%  H=1.10bits  [floor applied]
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint from external-evidence policy = forbidden overrides the RL pick of P1
               reasoning: External-evidence policy is explicitly FORBIDDEN and exploration output cannot be used; hard constraint mandates P0 regardless of the P1 aggregate vote (58% light, 46% deep mass) or per-section residual gaps. All sections are self-contained with 'brief' flags and the guideline demands only conceptual overview with no external examples permitted.
               drivers: external-evidence-forbidden, hard-constraint, self-contained-flags
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-24 21:10:04.805 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:10:44.456 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=36%  H=1.41bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (already cost-adjusted); uncertain vote (std mass 52%, deep only 13%) but no sanctioned override applies per policy (cannot escalate P1; downward not justified as S3/S5 lack near-zero residual and no depth_cov>=6). All sections self-contained with many brief flags; dominant gap is depth but do not escalate on raw counts. Follow primary scorer signal.
               drivers: scorer_aggregate_P1, vote_mass_gates, brief_flags_and_self_contained, no_sanctioned_override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:10:44.515 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:11:00.625 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=72%  H=1.11bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Scorer aggregate is decisively P2 standard (72% budget-weighted vote mass on standard, 0% deep, low entropy); this is already the cost-adjusted RL pick. No P2->P3 escalation (deep mass <30%, decisive vote), no general downward override (S2/S3 at 14%/17% budget still show high residual depth 42/0 and 34/0 plus must-ev/orphans). Dominant gap is depth; self-contained flags do not override the learned signal.
               drivers: decisive 72% standard vote mass, RL pick on high-budget sections, no sanctioned override condition met
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.274  P1/light:0.394  P2/standard:0.399  P3/deep:0.319
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:11:00.686 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:11:11.830 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=False)

  Policy     : forbidden
  RL model   : P0 skip      conf=79%  H=0.74bits  [floor applied]
  Grok 4.2   : P0 skip      [agrees with RL]
               reasoning: External-evidence policy explicitly FORBIDDEN (exploration output cannot be used), mandating P0; scorer aggregate is decisive 79% skip (deep mass only 21% <30%), every section self-contained + brief-flagged, guideline demands only surface-level conceptual overview with no external examples or depth.
               drivers: external-evidence-forbidden, decisive-skip-vote, all-sections-self-contained-and-brief
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-24 21:11:11.898 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:11:29.102 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=55%  H=1.45bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Aggregate RL pick is P2 standard (55% budget-weighted mass on standard, 22% on deep). Vote is moderate/UNCERTAIN but has clear dominant standard arm >30% and deep mass <30% so no sanctioned P2->P3 escalation. High-budget sections mixed (S4/S3 residuals 37/4 and 23/2 with deep/light votes; S6/S7 near-zero residual but already factored upstream); does not meet GENERAL DOWNWARD OVERRIDE criteria of most high-budget well-covered or no-dominant-arm.
               drivers: scorer_aggregate_P2, standard_vote_mass_55pct, deep_mass_below_30pct
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.298  P2/standard:0.323  P3/deep:0.281
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:11:29.178 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:11:49.168 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=35%  H=1.72bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 (UNCERTAIN but primary signal); standard mass 44% but hard guard forbids escalating P1 to P2; deep mass only 7%<30% so no P2→P3; all sections self-contained with policy against raw-gap escalation on residuals/must-ev.
               drivers: scorer-aggregate, vote-mass-gates, self-contained-flag, hard-escalation-guard
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:11:49.205 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:11:57.213 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=32%  H=1.36bits  [floor applied]
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard policy constraint mandates skip; cannot use any exploration output
               reasoning: External-evidence policy = FORBIDDEN (hard constraint) requires P0; scorer's P1 vote and 32% light mass are overridden.
               drivers: external-evidence policy, hard constraint
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-24 21:11:57.337 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:12:14.643 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=54%  H=1.45bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: P2 aggregate (54% standard mass) is the reward-trained optimum; deep mass=26% blocks P2->P3 escalation and standard dominance blocks downward override despite high residuals in S1/S2 (per OVERRIDE POLICY and residual/self-cont context).
               drivers: scorer_aggregate_P2, deep_mass_below_30pct, standard_dominance_54pct
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0672  (regret +0.0672)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:12:14.657 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:12:38.426 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=43%  H=1.40bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL vote is P1 light (moderate confidence, 43% light / 45% standard / 12% deep mass). This is UNCERTAIN but no sanctioned override applies: deep mass (12%) << 30% so no P2→P3 path, standard mass >30% blocks the 'no-escalation-signal' clause for downward to P0, and high-residual S1/S2 (27% budget) are already baked into the cost-adjusted pick. Self-contained flags across 100% budget and dominant gap being depth further align with cheap touch-up rather than standard rounds.
               drivers: RL-aggregate-pick, vote-mass-gates, self-contained+residual-context, no-sanctioned-override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:12:38.463 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:12:47.396 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=26%  H=1.89bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint requires P0 when external-evidence policy=forbidden, regardless of scorer vote or residual gaps
               reasoning: External-evidence policy is explicitly FORBIDDEN; exploration output cannot be used, making any preset >0 invalid per hard constraints. All sections are self-contained with 'brief: yes' flags and the guideline demands only surface-level conceptual treatment with no external libraries, case studies or benchmarks. Scorer's uncertain P1 aggregate (entropy 1.89 bits, 26% deep mass) is overridden by the policy.
               drivers: external-evidence policy, self-contained flags, brevity requirements
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-24 21:12:47.423 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:13:05.881 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=61%  H=1.55bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Scorer aggregate is P3 (UNCERTAIN, entropy 1.55) with 61% budget-weighted deep-vote mass (>>30% gate) driven by S3 (26%, RL=deep, resid 53/6 depth, 20 must-ev, 17 orphans) and S4 (16%, RL=deep, resid 32/6, 9 must-ev). Dominant depth gaps and 42 article-wide unbacked anchors in core implementation sections (42% combined budget) align with P3; self-contained flags do not trigger downward override because deep mass is high and no 'no dominant arm' condition holds. External-evidence=ALLOWED and gaps justify exploration.
               drivers: 61% deep-vote mass from S3/S4, high residual depth + must-ev in heaviest sections, dominant depth-gap economics
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:13:05.898 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:13:18.846 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=69%  H=1.17bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL vote is P1 (69% light mass, moderate confidence); deep/standard masses (9%/22%) below all escalation gates; high-budget residuals (e.g. S3 47/2) already factored into the cost-adjusted pick with no qualifying override triggers.
               drivers: aggregate RL vote, vote-mass gates, no qualifying override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:13:18.877 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:13:25.879 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=29%  H=0.87bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: External-evidence policy is FORBIDDEN, mandating P0 regardless of scorer pick
               reasoning: HARD CONSTRAINT: external-evidence policy=FORBIDDEN explicitly requires P0 (exploration output cannot be used). Scorer aggregate was P1 (weak 29% light, 71% skip) but policy overrides all votes, residual gaps, and self-contained flags; article is 100% notebook-mirroring practice with repeated 'must stay brief' and 'no external' rules.
               drivers: external-evidence policy, hard constraint
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-24 21:13:25.906 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:13:56.721 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.44bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL vote is P1 light (49% budget-weighted mass) with top contributions from largest sections S4 (20%, light·1.00, 12 must-ev) and S5 (29%, light·1.00, brief=yes). Deep mass only 14% (S2 alone) and standard mass 0% bar any escalation; all sections self-contained with residuals already reflected in the cost-adjusted pick. No qualitative red flags in guideline override the primary signal.
               drivers: section-scorer aggregate (P1 at 49%), budget-weighted votes from S4/S5, deep-mass <30% gate
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:13:56.837 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:14:23.380 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=49%  H=1.73bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate is P1 light (49% budget-weighted vote mass) and UNCERTAIN (entropy 1.73). No sanctioned P2->P3 (pick not P2, deep mass 9%<30%). No general downward (dominant light arm, only one brief-flagged high-budget section, RL pick already cost-adjusted). Self-contained flag and residuals supply context but are not triggers. Decisive signal: scorer's budget-weighted votes.
               drivers: scorer_aggregate_P1, light_vote_mass_49pct, no_sanctioned_override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:14:23.422 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:14:33.792 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P3 deep      conf=43%  H=1.54bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: HARD CONSTRAINT: external-evidence policy = forbidden requires P0 skip regardless of scorer or gaps
               reasoning: Hard constraint: external-evidence policy explicitly FORBIDDEN, so exploration output cannot be used and P0 is mandatory (overrides scorer's uncertain P3 vote, 43% deep mass, large residuals in S3/S4, and self-contained flags across 100% budget). Guideline demands conceptual overview only with surface-level treatment, no external libs/examples/code, and 'keep brief' on every section.
               drivers: external-evidence-forbidden, brevity-flags-all-sections, self-contained-100pct-budget
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-24 21:14:33.852 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:15:03.487 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=18%  H=1.91bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (UNCERTAIN but primary signal); standard mass 41% suggests gap-filling but escalation from P1 is forbidden by hard guard; downward to P0 blocked as S3/S4 (49% budget) have high must-ev (13 total), residuals (60/9 combined), and no dominant-arm exemption; all sections self-contained yet dominant gap type is depth.
               drivers: RL aggregate pick, override policy gates, must-ev + residual in S3/S4
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0342  (regret +0.0342)
  Verdict    : ✗  MISS

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:15:03.628 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:15:22.868 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=52%  H=1.27bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Section-scorer aggregate is P3 (52% soft vote, 45% budget-weighted deep mass >30% from S3+S4 at 45% of budget); UNCERTAIN but no sanctioned downward override applies (high-budget S3/S4 show high residual depth 54/20, must-ev 6+2, dominant depth gaps, not mostly brief/well-covered). Guideline's repeated "must cover in depth" items plus production examples/failure modes further align with P3 over lower presets.
               drivers: budget-weighted deep mass 45%, high residual depth in S3/S4, dominant depth gaps + must-ev
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:15:22.895 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:15:30.849 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=61%  H=0.97bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint for forbidden external-evidence policy requires P0 despite scorer's P1 vote
               reasoning: External-evidence policy is explicitly FORBIDDEN; exploration output cannot be used. Scorer aggregate is P1 light (61% light / 39% skip, moderate confidence) but HARD CONSTRAINT mandates P0 when external evidence is forbidden. All sections are self-contained with 'brief' flags and the guideline demands only conceptual overview with no external libraries/case studies.
               drivers: external-evidence-forbidden, policy-constraint, self-contained-sections
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-24 21:15:30.872 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:15:53.252 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=48%  H=1.00bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is already-cost-adjusted P1 (light 48%/standard 52% split, moderate confidence, 0% deep mass). All sections self-contained; residuals concentrated in S1-S4 depth (high must-ev/orphans) but S5 brief-flagged and S6-S7 near-zero residual. No sanctioned override triggers met: cannot escalate P1, downward to P0 blocked by >30% standard mass and residual context. Follows RL pick as primary calibrated signal.
               drivers: RL-pick P1, vote-mass gates, self-contained + residual context
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:15:53.298 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:16:09.016 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=81%  H=0.69bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Aggregate is decisively P2 standard (81% budget-weighted vote mass on standard, 0% deep, 19% light). This matches the strong learned signal for a depth-dominant article with substantial residuals still present in high-budget sections S1-S4 (e.g. 29/0, 24/0) and must-ev counts of 3-5. No sanctioned override applies: vote is decisive so no P2->P3 escalation, standard mass >>30% blocks downward move, and residuals/self-contained flags were already cost-adjusted upstream.
               drivers: decisive 81% standard vote mass, depth-dominant gaps + residuals in S1-S4, no OVERRIDE POLICY gates triggered
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-24 21:16:09.078 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:16:19.704 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=38%  H=1.58bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Policy hard-constraint overrides scorer's uncertain P1-light aggregate (38% light / 31% skip / 31% standard)
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN (explicitly stated at top of brief) mandates P0; 100% self-contained sections, pervasive 'must stay brief' flags, and 'conceptual overview/surface-level only' guideline confirm no usable exploration output.
               drivers: external-evidence-forbidden, self-contained-budget-100, brevity-requirements
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-24 21:16:19.860 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:16:44.431 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=37%  H=1.62bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (already cost-adjusted); uncertain (entropy 1.62) but skip 47% + light 38% dominate while standard-vote mass=10% and deep-vote mass=6% both <<30% gate. All sections self-contained; high residuals/must-ev in S3 (23% budget, light vote, must-ev=3) and S1 do not trigger sanctioned downward override per policy (not most high-budget well-covered with near-zero residual). No upward from P1 permitted. Dominant gap=depth but vote mass forbids escalation.
               drivers: aggregate RL pick, vote-mass gates, self-contained flag, no sanctioned override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.0356  (regret +0.0356)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-24 21:16:44.477 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:16:57.522 | INFO     | logging:callHandlers:1762 | Grok planner chose P2 (override=False)

  Policy     : allowed
  RL model   : P2 standard  conf=52%  H=1.75bits
  Grok 4.2   : P2 standard  [agrees with RL]
               reasoning: Aggregate RL pick is P2 standard (budget-weighted: 52% standard, 15% deep). Vote is UNCERTAIN (entropy 1.75) but standard mass dominates at 52% while deep mass=15%<30% so no sanctioned P2->P3 escalation. High-residual depth gaps in S3 (44/2) and S5 (25/0) already factored into the cost-adjusted scorer pick; all sections self-contained but this does not trigger downward override given dominant standard vote and non-zero residuals in 23%/15% budget sections.
               drivers: budget-weighted standard mass 52%, deep mass <30% gate, residuals in high-budget sections, cost-adjusted RL prior
  -> Chosen  : P2 standard  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-24 21:16:57.688 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:17:16.129 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.34bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Aggregate RL recommendation is already P3 (60% deep-vote mass from 60% of budget in S3/S4 both voting deep·1.00). Moderate confidence but dominant deep arm, high must-ev (14/8 in S4, 8 in S3), large residuals (16/6 and 11/6), and depth-dominant gaps align with P3; no sanctioned downward override applies as high-budget sections are neither brief-flagged nor well-covered (cov depth only 5 and 3).
               drivers: budget-weighted deep mass 60%, S4 40% + S3 20% deep picks, high must-ev/residuals in impl sections
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.276  P1/light:0.315  P2/standard:0.350  P3/deep:0.350
  Regret     : -0.0000
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-24 21:17:16.153 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:17:39.766 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=31%  H=1.79bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (already cost-adjusted); vote is uncertain (entropy 1.79) with standard mass at 44% but deep mass only 9%. No sanctioned P2→P3 escalation applies (pick is P1, deep mass <30%), general downward override to P0 does not trigger (standard mass >30%, S4 14% budget retains high residual 52/4), and all sections are self-contained yet several must-ev and orphans remain. Hard guard forbids escalating P1 to P2 regardless of vote mass.
               drivers: RL aggregate P1, no sanctioned override triggered, standard mass insufficient for escalation from P1
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.050  P1/light:0.001  P2/standard:0.002  P3/deep:0.033
  Regret     : 0.0495  (regret +0.0495)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-24 21:17:39.858 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:17:59.397 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=32%  H=1.84bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL recommendation is P1 light (already cost-adjusted); uncertain vote (entropy 1.84) with mass split 32% light / 39% standard / 9% deep. No sanctioned upward escalation (P1 cannot go to P2 per hard guard; deep mass only 9% < 30%). Downward to P0 not triggered (standard mass >30%; high-budget S4 voted light with large residual but self-contained). Sticking to scorer peak balances coverage in S4/S3 vs. already-strong deep-dive sections.
               drivers: scorer_aggregate_P1, vote_mass_gates, self_contained_context
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.348  P1/light:0.395  P2/standard:0.373  P3/deep:0.391
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-24 21:17:59.431 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:18:15.200 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=88%  H=0.54bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Decisive 88% budget-weighted vote for P1 (0% deep mass, 12% standard); all sections self-contained with cov depth already 6-7/8; no sanctioned override applies and policy forbids escalating any P1 pick.
               drivers: decisive scorer vote, self-contained flags, vote-mass gates
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.268  P1/light:0.370  P2/standard:0.398  P3/deep:0.348
  Regret     : 0.0279  (regret +0.0279)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-24 21:18:15.228 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:18:30.186 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=60%  H=1.32bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Scorer aggregate is P3 (moderate/60% confidence, uncertain); deep-vote mass=60% (>30%) driven by largest-budget sections S2(35%, deep, resid 17/6) and S5(18%, deep, resid 17/6) which are also the weakest; no sanctioned downward override applies (high residual depth, no brief flags, dominant depth gaps + 47 unbacked anchors).
               drivers: budget-weighted deep mass 60% in S2/S5, high residual depth in largest sections, dominant depth gaps
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0667  (regret +0.0667)
  Verdict    : ✗  MISS

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-24 21:18:30.248 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:18:46.413 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=57%  H=1.36bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is P1 light (57% light / 31% standard / 0% deep vote mass, moderate confidence). No sanctioned upward move from P1 (hard guard; deep mass = 0%). High-budget S6 (31%, standard pick, resid 2/6, must-ev 2) and other residuals exist but self-contained flags + already cost-adjusted RL pick do not trigger general downward override to P0. Dominant gap type balanced but raw gaps do not escalate.
               drivers: scorer_aggregate_P1, zero_deep_mass, no_downward_criteria_met
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-24 21:18:46.431 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:19:07.771 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=51%  H=1.47bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (51% light mass, 29% deep mass, 0% standard); moderate but not decisive. Deep mass falls below 30% gate and P2/P3 escalation from P1 is hard-prohibited. High residuals and must-ev exist but are already baked into the cost-adjusted scorer vote; all sections self-contained yet this does not trigger sanctioned downward override as no dominant well-covered pattern. Dominant gap is depth, matching S3's deep vote, but primary signal stays at P1.
               drivers: RL aggregate vote, deep-mass <30%, no-sanctioned-override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.275  P1/light:0.361  P2/standard:0.369  P3/deep:0.289
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-24 21:19:07.802 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:19:41.329 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=46%  H=1.51bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Aggregate RL pick is P3 deep (46% deep-vote mass, 0% standard) on an UNCERTAIN but deep-dominant distribution; S3 (46% budget, RL deep·1.00) carries high must-ev (8), orphans (9/0), residual depth (23/4) and dominant article gap is depth. Brief flags and self-contained status noted but already baked into the cost-adjusted P3 pick; no sanctioned downward override triggered because deep mass >30% and high-budget section RL votes are not uniformly skip/light.
               drivers: aggregate RL pick P3, deep-vote mass 46%, S3 residual 23/4 + must-ev 8
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.341  P1/light:0.517  P2/standard:0.511  P3/deep:0.559
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-24 21:19:41.426 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:20:03.314 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=45%  H=0.99bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (MODERATE confidence, 45% light / 55% standard mass). Pick is UNCERTAIN but deep-vote mass=0% so no P2->P3 escalation possible; hard guard forbids raising any P1 to P2+. Downward to P0 not justified: high-budget S2/S4 (54% combined) lack brief flags, retain large residuals (10/2 and 11/5), and standard mass exceeds 30%. All sections self-contained is already baked into the cost-adjusted RL pick.
               drivers: RL aggregate P1, no sanctioned escalation from P1, residuals in non-brief high-budget sections
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.335  P1/light:0.457  P2/standard:0.449  P3/deep:0.453
  Regret     : -0.0036  (regret -0.0036)
  Verdict    : ✗  MISS

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-24 21:20:03.370 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:20:12.712 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=False)

  Policy     : allowed
  RL model   : P3 deep      conf=72%  H=1.14bits
  Grok 4.2   : P3 deep      [agrees with RL]
               reasoning: Scorer aggregate is decisive P3 (72% deep vote mass, 0% skip); S2+S3 (72% budget) both vote deep·1.00 with highest residuals (14/3 and 13/0), must-ev (8+5), and dominant depth-gap type. No sanctioned downward override applies: high-budget sections are neither brief-flagged in a way that overrides their own deep votes nor well-covered (cov far below need). DECISIVE signal trusted; P3 selected.
               drivers: decisive 72% deep vote mass, S2/S3 residual depth needs + must-ev, dominant depth gaps
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.285  P1/light:0.361  P2/standard:0.304  P3/deep:0.426
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-24 21:20:12.747 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:20:21.762 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=100%  H=0.00bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Scorer aggregate is decisive P1 (100% light vote, 0% standard/deep mass) across all 5 sections with 100% budget-weighted light votes; all sections self-contained with low cov scores already factored into the RL pick. No sanctioned escalation from P1 (hard guard), no uncertainty for downward override to P0, and external-evidence=allowed does not force exploration.
               drivers: decisive P1 aggregate, zero deep/standard mass, self-contained flags
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.362  P1/light:0.425  P2/standard:0.412  P3/deep:0.338
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-24 21:20:21.790 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:20:37.292 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=95%  H=0.27bits
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate scorer vote is decisive at 95% for P1 light (0% standard, 0% deep) with every section RL pick being skip or light; high-budget S2/S4 already received light in the exploitation pass and the RL pick is already cost-adjusted. No self-contained sections but residual gaps do not trigger a sanctioned downward override given the decisive signal and must-ev/orphan counts already weighed by the model. External-evidence is only ALLOWED, not required.
               drivers: decisive_95pct_light_vote, no_P2_P3_mass, no_sanctioned_override
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-24 21:20:37.349 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:20:51.818 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=76%  H=0.79bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Decisive aggregate RL vote is P1 light (76% light, 24% deep mass); all sections self-contained, dominant gap is depth but vote mass <30% bars any escalation; no downward override as S3 residual 22/6 and must-ev=6 indicate remaining gaps; policy forbids moving above P1 when decisive.
               drivers: decisive scorer vote (76%), deep-mass below 30%, high residuals in S3 but no escalation from P1
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P3 deep
  R_w        : P0/skip:0.360  P1/light:0.519  P2/standard:0.473  P3/deep:0.579
  Regret     : 0.0599  (regret +0.0599)
  Verdict    : ✗  MISS

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-24 21:20:51.897 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:21:17.483 | INFO     | logging:callHandlers:1762 | Grok planner chose P1 (override=False)

  Policy     : allowed
  RL model   : P1 light     conf=42%  H=1.32bits  [floor applied]
  Grok 4.2   : P1 light     [agrees with RL]
               reasoning: Aggregate RL pick is P1 light (moderate confidence, 42% light / 50% standard vote mass). This is UNCERTAIN but no sanctioned override applies: deep mass=0% bars P2->P3, standard mass >30% and high residuals in S1/S4 (10/8 and 11/4, must-ev 7/5) bar general downward to P0, all sections self-contained is already baked into the cost-adjusted pick. Dominant gaps are depth but brief flags on 58% budget (S1/S3) and external-evidence=ALLOWED align with light touch-up only.
               drivers: RL_aggregate_P1, no_sanctioned_override, standard_mass_bars_downward, brief_flags_on_high_budget
  -> Chosen  : P1 light  (by Grok4.2)
  Oracle     : P1 light
  R_w        : P0/skip:0.299  P1/light:0.394  P2/standard:0.359  P3/deep:0.336
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-24 21:21:17.583 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:21:31.671 | INFO     | logging:callHandlers:1762 | Grok planner chose P0 (override=True)

  Policy     : forbidden
  RL model   : P1 light     conf=25%  H=1.80bits
  Grok 4.2   : P0 skip      [OVERRIDE]
               reason: Hard constraint from external-evidence policy=forbidden overrides the RL pick of P1
               reasoning: External-evidence policy is explicitly FORBIDDEN, a hard constraint that mandates P0 skip regardless of the uncertain P1 aggregate vote (36% skip / 25% light / 6% standard / 33% deep) or per-section residual needs. All sections are self-contained with pre-provided sources in the guideline appendix; no exploration is permitted.
               drivers: external-evidence policy, hard constraint
  -> Chosen  : P0 skip  (by Grok4.2)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-24 21:21:31.704 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 21:21:52.126 | INFO     | logging:callHandlers:1762 | Grok planner chose P3 (override=True)

  Policy     : allowed
  RL model   : P2 standard  conf=49%  H=1.26bits
  Grok 4.2   : P3 deep      [OVERRIDE]
               reason: Sanctioned upward escalation from P2 due to deep-vote mass >=30% on uncertain vote
               reasoning: Aggregate is uncertain P2 (49% standard / 45% deep mass); P2 pick + deep-vote mass 45% >=30% directly triggers sanctioned P2->P3 escalation per override policy. S5 (45% budget, deep·1.00, resid 42/0) dominates the signal; self-contained flags and residuals provide context but do not override given the vote mass.
               drivers: budget-weighted deep-vote mass, S5 residual depth, uncertain bimodal split
  -> Chosen  : P3 deep  (by Grok4.2)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.383  P2/standard:0.400  P3/deep:0.368
  Regret     : 0.0320  (regret +0.0320)
  Verdict    : ~  NEAR MISS  (±1 preset)
2026-08-24 21:21:52.245 | INFO     | logging:callHandlers:1762 | Stopping stale infer server (adapter changed)…

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