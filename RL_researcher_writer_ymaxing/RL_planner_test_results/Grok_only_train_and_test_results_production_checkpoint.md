================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:54:03.490 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:54:03.510 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN explicitly mandates P0 (only valid choice). All sections marked self-cont=yes with must-ev=0; residuals concentrated in brief, low-budget S1-S3 but guideline demands only surface-level conceptual overview with repeated 'must stay brief' instructions. Exploration output cannot be used per the brief.
               drivers: external-evidence policy, self-cont across sections, brevity mandates, zero must-ev
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-09-09 12:54:17.787 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:54:17.794 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth in S1-S3 (24/10, 39/7, 46/4) plus 42 unbacked anchors and must-ev in S1/S3/S5 drive gap-filling; dominant gap is depth and weakest sections are S2/S3. Self-cont 'yes' across all, zero residual depth in high-budget S4-S6, and multiple 'brief' flags keep it from P3. External-evidence ALLOWED but not required, so default to cheaper P2 over P1.
               drivers: residual depth in S1-S3, 42 unbacked anchors, must-ev counts, self-cont + strong S5/S6
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0774  (regret +0.0774)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:54:32.430 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:54:32.431 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth (42/0 in S2, 34/0 in S3) against 14-17% budgets, combined with must-ev of 5 and 3 plus 45 article-wide unbacked anchors, show concrete depth gaps in weakest sections despite 0-residual strength in S4-S6 and universal self-cont flags. Dominant gap type is depth; P2's depth-then-breadth sequence addresses this without P3 expense, as later sections need no escalation and external-evidence is only allowed.
               drivers: residual depth S2/S3, must-ev in S2/S3/S6, 45 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.274  P1/light:0.428  P2/standard:0.422  P3/deep:0.319
  Regret     : 0.0062  (regret +0.0062)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:54:36.858 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:54:36.860 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: Hard constraint: external-evidence policy=FORBIDDEN explicitly requires P0; exploration output cannot be used. All sections marked 'brief: yes' and 'must stay brief'; guideline stresses conceptual overview with surface-level treatment, no depth or external examples allowed. Every section self-cont='yes' and resid d/b is irrelevant under the ban.
               drivers: external-evidence-forbidden, all-sections-brief, self-cont-yes, guideline-surface-level
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-09-09 12:54:55.887 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:54:55.894 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps dominate in S1-S4 (resid 27/2, 22/4, 23/2, 37/4) with combined ~45% budget, 42 article-wide unbacked anchors, dominant depth gap type, and 8 must-ev items (esp. S3:2, S6:3). All sections self-cont 'yes' and S5-S8 (55% budget) show 0 residual, so gaps are real but contained; P2 depth-then-breadth fills evidence needs without P3 overkill. External-evidence ALLOWED but not forced; cheaper P1 insufficient for sizeable S4/S3 depth shortfalls.
               drivers: resid d/b in S1-S4, unbacked anchors (42), must-ev count (8), dominant depth gap, budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.282  P2/standard:0.316  P3/deep:0.281
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:55:11.655 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:55:11.658 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget sections S3 (40/0), S2 (30/5), S7 (17/2) and S4 (14/2) despite universal self-cont; must-ev totals are high (S6:12, S4:7, S3:5) with 48 article-wide unbacked anchors and dominant depth gap type. S6/S5 are strongest yet still need named evidence for mandatory bullets. This is concrete evidence of meaningful gaps that justify depth-first then breadth (P2); existing cov (mostly 3-5/8) plus golden sources keep it from P3 while ruling out P0/P1.
               drivers: high residual depth in S2/S3/S7, must-ev counts (esp S6/S4), 48 unbacked anchors, dominant depth gap, budget-weighted sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0361  (regret +0.0361)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:55:17.169 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:55:17.170 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN and exploration output cannot be used; this hard constraint overrides all per-section residuals (e.g. S1 35/6, S2 42/6), 41 unbacked anchors, and dominant depth gap. All sections flagged 'brief' with surface-level treatment required per guideline; self-cont='yes' everywhere and strongest coverage already in S7/S5.
               drivers: external-evidence-forbidden, resid-vs-budget, all-brief-flags
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-09-09 12:55:31.541 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:55:31.542 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps in high-budget foundational sections S1 (29/6) and S2 (37/6) plus S4 (16/6), 41 article-wide unbacked anchors, dominant depth gap type, and 6 must-ev items outweigh the universal self-cont flags; P2's depth-first round directly targets these concrete shortfalls while cheaper P1 is insufficient and P3 is unwarranted given lower residuals in S3/S6/S7.
               drivers: residual depth in S1/S2, 41 unbacked anchors, dominant depth gaps, must-ev count
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0672  (regret +0.0672)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:55:44.135 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:55:44.136 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : required
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S1 and S2 dominate decision with massive residuals (54/13 and 52/14), 14 combined must-ev bullets, and 36/7 orphans despite self-cont; these 27% budget sections contain most of the 42 article-wide unbacked anchors and all 'must cover in depth' theory anchors (modularity, debugging, information loss, etc.). Later practice sections show near-zero depth residuals and solid coverage, so no need for P3. External-evidence REQUIRED plus dominant depth gap and named-production/failure-mode mandates in guideline confirm 2-round depth-then-breadth over P1 touch-up.
               drivers: high residual depth in S1/S2, must-ev totals (7+7 in weakest sections), 42 unbacked anchors, external-evidence REQUIRED, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0355  (regret +0.0355)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:55:48.509 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:55:48.515 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: The brief explicitly states external-evidence policy = FORBIDDEN and notes that exploration output cannot be used, making P0 the only valid choice per hard constraints. All sections are already marked self-cont = yes with many low resid d/b values (e.g. S5/S7 at 0/2); the dominant gap type is depth but this is irrelevant under the policy. Large need figures in S2/S3 are overridden by the explicit forbid on new external sources.
               drivers: external-evidence policy FORBIDDEN, self-cont = yes across all sections, low resid d/b in strongest sections
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-09-09 12:56:06.978 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:56:06.980 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth in highest-budget sections S3 (53/6, 26% budget, must-ev=20) and S4 (32/6, 16% budget, must-ev=9) plus 42 article-wide unbacked anchors and dominant depth gap show concrete sizeable shortfalls despite universal self-cont=yes and low residuals in S7/S5. External-evidence=ALLOWED permits escalation only where gaps justify; raw need ignored per instructions, but residuals + must-ev drive P2 for depth-then-breadth gap-filling without P3 cost.
               drivers: high resid in S3/S4, high must-ev in core sections, 42 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0339  (regret +0.0339)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:56:24.293 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:56:24.299 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps dominate in highest-budget sections (S3: 47/2 resid at 24% budget + must-ev 22; S4: 28/2 at 15% + must-ev 11; S2: 32/0 at 9%), plus 47 article-wide unbacked anchors and guideline mandates for industry examples, production comparisons, named failure modes, and 'must cover in depth' anchors in S8/S9. All sections self-cont 'yes' but this is outweighed by residuals + must-ev pressure; dominant gap type is depth. P2 (depth->breadth) fills these without P3 overkill on already-strong sections (S5/S7 resid 0/0). External-ev ALLOWED but gaps clearly justify escalation from P0/P1.
               drivers: residual depth in S3/S4/S2, high must-ev counts, 47 unbacked anchors, additional reqs for named production examples/failures
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:56:28.296 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:56:28.302 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN; exploration output cannot be used. All sections are marked self-cont=yes and most carry explicit 'must stay brief' flags. Residual gaps exist but HARD CONSTRAINT mandates P0 when external evidence is forbidden. Article is 100% practical notebook mirroring with surface-level treatment required.
               drivers: external-evidence-forbidden, self-cont across all sections, multiple 'must stay brief' directives
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-09-09 12:56:44.846 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:56:44.855 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget sections S2 (35/4, must-ev 7, 14%), S4 (41/4, must-ev 12, 20%) and still notable in S1/S3; article-wide 54 unbacked anchors and dominant depth gap type confirm concrete missing evidence for implementation details, tool mocks, function calling, and prompt mechanics. Self-cont 'yes' across all sections and low residuals in largest-budget S5 (7/6) plus its 'brief' flag pull downward, but high must-ev totals (49) and weakest-section signals outweigh this for gap-filling. P2 (depth-then-breadth) buys the needed coverage without P3 expense.
               drivers: residual d/b in S2/S4, must-ev totals, unbacked anchors (54), dominant depth gap, self-cont + S5/S6 strength
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.1419  (regret +0.1419)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:57:14.689 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:57:14.695 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps remain in high-budget sections S5 (92/4), S6 (77/4), S4 (33/2) and S2 (35/5) despite universal self-cont=yes; multiple must-ev=1 and explicit "must cover in depth" items require production examples, error-handling strategies, test-suite benchmarks, real-world failure modes, and named industry anchors (matching the guideline's golden/other sources and additional requirements). 58 article-wide unbacked anchors plus dominant depth gap justify meaningful gap-filling, but S5's brief flag and self-cont evidence keep it from P3.
               drivers: residual d/b in large-budget sections, must-ev + must-cover-depth mandates, unbacked anchors + production anchoring requirements, self-cont vs dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0557  (regret +0.0557)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:57:24.199 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:57:24.201 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN; the brief states exploration output cannot be used and only skip is valid. All sections are self-cont='yes', the guideline demands only a surface-level conceptual overview (100% theory, no real-world examples or external libs), and brevities plus 'must stay brief' flags further remove justification for any new sourcing despite large residual depth gaps (e.g. S3 41/4) and must-ev counts.
               drivers: external-evidence policy=forbidden, self-cont=yes across all, conceptual-overview mandate, 0% real-world examples
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-09-09 12:57:36.915 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:57:36.917 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S3 and S4 dominate (49% combined budget) with largest residuals (36/4 and 24/5), highest must-ev (8+5), 22 orphans, and no 'brief' flag; article-wide 42 unbacked anchors and dominant depth gap confirm concrete need for depth-first then breadth work. Self-cont 'yes' everywhere and strong S6/S1 keep us from P3; cheaper P1 insufficient for must-ev and largest sections.
               drivers: resid+must-ev in S3/S4, dominant depth gap, high-budget non-brief sections, 42 unbacked anchors
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0429  (regret +0.0429)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:57:54.323 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:57:54.323 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth (esp. S3 at 54 with must-ev=6 + 18 orphans, S6 at 30 with must-ev=4) plus article-wide 42 unbacked anchors and dominant depth gap show concrete evidence shortfalls despite self-cont=yes everywhere and strong cov in S4. Must-ev total of 19 and added requirements for production examples/failure modes further justify gap-filling. Default to cheaper but sizeable depth-driven gaps in 19%+budget sections rule out P0/P1; P3 unnecessary as S1/S4 already decent and brief sections cannot absorb extra rounds.
               drivers: high residual depth in S3/S6, must-ev total 19 + 42 unbacked, dominant depth gap, self-cont yes but low cov in weak sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:57:59.594 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:57:59.601 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN, mandating P0 per hard constraints. All sections marked 'brief: yes' with self-cont='yes'; guideline demands only surface-level conceptual overview and prohibits depth/production code/external examples. Residual gaps (e.g. S3 19/0, S4 46/0) and must-ev counts are overridden by the policy and brevity requirements.
               drivers: external-evidence-forbidden, all-sections-brief, self-cont-yes, surface-level-guideline
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-09-09 12:58:14.961 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:58:14.967 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth (17/16/19/32) in S1-S4 (55% combined budget), 42 unbacked anchors (esp. 12 orphans in S4), dominant depth gap, and must-ev=3 in S1 drive need for gap-filling; self-cont=yes and strong cov in S5-S7 (plus S5 brief=yes) cap escalation at 2 rounds (depth→breadth) rather than P3 or cheap P0/P1.
               drivers: residual d/b, orphans d/b, dominant depth gap, must-ev, section budgets
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0193  (regret +0.0193)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:58:31.837 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:58:31.839 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (24-29/0) in high-budget sections S1-S5 (15-19% each) with high must-ev (3-5) and orphans (7-11); S2/S3 flagged as weakest. 42 unbacked anchors and dominant depth gap confirm need despite self-cont=yes everywhere and strong S6/S7 (residuals 3/0, 2/0). Policy=allowed permits escalation; P2 depth-then-breadth fills evidence for must-cover industry examples/failure modes/code comparisons without P3 cost.
               drivers: residual d/b in large sections, high must-ev counts, dominant depth gaps, unbacked anchors (42), weakest sections S2/S3
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-09-09 12:58:36.872 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:58:36.877 | INFO     | logging:callHandlers:1762 | LLM standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN, mandating P0. All sections self-cont=yes with already-matched sources; residuals are modest after coverage (e.g. S5 resid 1/4, S4 6/4) especially in high-budget sections (S3 17%, S5–S6 14% each). Brief flags and 'must stay brief' instructions on S2–S6 further reduce any depth pressure. Article-wide 50 unbacked anchors are offset by the policy and the minimal-variant scope that relies on notebook code plus fixed golden sources.
               drivers: external-evidence policy=forbidden, universal self-cont=yes, low residuals vs. budget, brevity mandates
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-09-09 12:58:58.715 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:58:58.720 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S3 (23% budget) shows resid 46/2 depth with must-ev=3 and 16 orphans; S2 has resid 24/4 + must-ev=1 needing OCR performance numbers; article-wide 42 unbacked anchors and dominant depth gap confirm sizeable evidence shortfalls in foundational sections. Self-cont 'yes' across most and zero-resid in S5-S7 (plus S5 'brief') argue against P3; P1 too cheap for the concrete depth mandate in largest sections.
               drivers: S3/S2 residual depth + must-ev, 42 unbacked anchors, dominant depth gap, high-budget foundations
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.1385  (regret +0.1385)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-09-09 12:59:15.360 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:59:15.361 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Dominant depth gaps remain large in high-budget sections (S3 resid 44/2 + must-ev 4 at 23%; S5 resid 25/0 + must-ev 6 at 15%; S2 resid 20/0 + must-ev 5 at 13%) despite self-cont 'yes' everywhere. 48 article-wide unbacked anchors,  high orphans in S3/S5, and guideline's many 'must cover in depth' items (named models/benchmarks like ViDoRe/nDCG@5, quantitative metrics, failure modes) show concrete evidence shortfalls. P1 too cheap for these sizeable depth mandates; P3 not justified as gaps are not uniformly evidence-heavy and policy is only 'allowed'.
               drivers: residual depth in S3/S5, high must-ev counts, dominant depth gap + 48 unbacked, budget-weighted must-cover specifics
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-09-09 12:59:36.562 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:59:36.569 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth (esp. S4 at 16/6 with must-ev=14 and 40% budget; S3/S5 also >10/6 with must-ev 8+4) plus article-wide 23 unbacked anchors and dominant depth gap show concrete evidence shortfalls in the core 80% hands-on sections that rely on golden sources (Gemini/Pydantic docs). All self-cont=yes pulls cheaper, but must-ev totals >30 and S4 scale override to meaningful gap-filling; S2 brief=yes limits escalation there. P2 (depth→breadth) sufficient; P3 unwarranted, P1 too shallow for the mandatory sourced facts.
               drivers: resid d/b in S4/S3, must-ev totals (31), 23 unbacked anchors, dominant depth gap, self-cont vs budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard  (tied with P3 deep — either counts as EXACT)
  R_w        : P0/skip:0.316  P1/light:0.273  P2/standard:0.400  P3/deep:0.381
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-09-09 12:59:56.196 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 12:59:56.198 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large and concrete in S1–S4 (26/4, 21/6, 26/6, 52/4), including the 14% budget S4 ReAct section that carries must-ev=1; article-wide 41 unbacked anchors and dominant-depth economics confirm sizeable missing evidence. S5 & S7 show 0 depth residual and all sections flag self-cont, so escalation stops at depth-then-breadth rather than P3. Policy is ALLOWED, not required, favoring the cheaper justified arm.
               drivers: resid d/b in S3/S4, 41 unbacked anchors, dominant depth gap, must-ev in S4/S5/S8
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.077  P1/light:0.038  P2/standard:0.052  P3/deep:0.078
  Regret     : 0.0256  (regret +0.0256)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-09-09 13:00:11.508 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:00:11.513 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S4 (18% budget) shows 41 residual depth + 12 must-ev + 15 orphans; S1-S3 add another ~62 residual depth combined; article-wide 42 unbacked anchors and dominant depth gap confirm sizeable evidence shortfalls in foundational/landscape sections. Later deep-dive sections (S5+) are at resid 0 with high self-cont, so depth-then-breadth (P2) fills the concrete gaps without P3 overkill.
               drivers: resid d/b in S1-S4, must-ev totals, unbacked anchors (42), dominant depth gap, budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.359  P1/light:0.405  P2/standard:0.368  P3/deep:0.376
  Regret     : 0.0370  (regret +0.0370)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-09-09 13:00:30.717 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:00:30.720 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth in large-budget sections S2 (20/0, must-ev 7, 8 orphans), S3 (18/0, must-ev 6), and especially S4 (35/0, must-ev 5, 13 orphans, 28% budget) plus 42 article-wide unbacked anchors show concrete depth gaps in core framework/application content; self-cont 'yes' across all and zero breadth residuals support defaulting away from P3, while dominant depth gap and must-ev pressure rule out P0/P1.
               drivers: residual d in S2/S4, must-ev counts, total unbacked anchors, dominant depth gap, self-cont + zero b-residual
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.380  P2/standard:0.430  P3/deep:0.394
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-09-09 13:00:52.045 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:00:52.047 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Dominant depth gaps persist with large residuals in the two highest-budget sections (S2 35% at 17/6; S5 18% at 17/6), 47 article-wide unbacked anchors, and depth as the primary missing type; self-cont 'yes' everywhere and must-ev=0 argue against deeper escalation, but the size of residuals in S2/S5 plus orphan counts (7/0 each) still justify gap-filling over a mere touch-up.
               drivers: residual d/b in high-budget sections, dominant depth gap, 47 unbacked anchors, self-cont + zero must-ev
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.380  P1/light:0.391  P2/standard:0.429  P3/deep:0.386
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-09-09 13:01:23.979 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:01:23.982 | INFO     | logging:callHandlers:1762 | LLM standalone chose P1

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P1 light     [standalone, no RL input]
               reasoning: Residual gaps are 0/6 in high-budget S2/S3/S4 (strongest sections, high must-ev already covered); only modest 2/6 residuals in S5/S6/S7 (combined ~60% budget) despite balanced dominant gap type and 42 unbacked anchors. All sections self-cont=yes with well-matched scraped sources; S1/S9 high residuals irrelevant due to 3% combined budget and brief intent. External-allowed policy does not mandate exploration; modest residuals support cheap balanced touch-up over P0 or costlier P2.
               drivers: low resid in large-budget technical sections, universal self-cont, tiny gaps in S1/S9, balanced gap type with must-ev mostly satisfied
  -> Chosen  : P1 light  (by Grok-only)
  Oracle     : P1 light  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.351  P1/light:0.366  P2/standard:0.340  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-09-09 13:01:42.336 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:01:42.337 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (14–19) in high-budget S3/S4 (29–32%, must-ev 7/6, orphans 8/7) despite self-cont 'yes' and moderate existing cov (5–7 depth); 27 unbacked anchors and dominant depth gap plus guideline demands for specific measurements, transcriptomics, evolutionary timing, and multiple named quotes (Damsgaard, Baden, Lewin) create sizeable sourced-evidence shortfalls. P2 depth-first then breadth fills these without P3 expense; policy 'ALLOWED' lets gaps drive escalation from P0/P1 default.
               drivers: residual depth in large sections, high must-ev & orphans, 27 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.301  P1/light:0.405  P2/standard:0.398  P3/deep:0.363
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-09-09 13:02:42.703 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:02:42.708 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (13/4, 14/4, 23/4) despite self-cont=yes; 20 unbacked anchors and high must-ev (5-8 per section) plus 20 orphans show many specific models/quotes (Khoury, Vafa, Andriot, Teixeira, Obied et al.) lack backing. Dominant gap is depth and S3 (46% budget) is weakest with 9 orphans; guideline demands concrete named evidence from listed arXiv sources not yet sufficient per table. P2 depth-then-breadth fills meaningfully; P3 unwarranted as external evidence only allowed not required and brief flags on S1/S3 limit absorption.
               drivers: residual d/b, must-ev counts, orphans d/b, dominant depth gap, section budgets
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.515  P2/standard:0.507  P3/deep:0.547
  Regret     : 0.0405  (regret +0.0405)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-09-09 13:03:09.544 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:03:09.548 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth 10-11 across all sections (esp. S4 at 11/5) plus 21 article-wide unbacked anchors and must-ev scores of 3-5 show concrete depth gaps remain despite self-cont 'yes' and cov ~5-6; dominant gap type is depth and S2/S4 (54% combined budget) are not brief. This justifies P2 depth-then-breadth for gap-filling; P3 unwarranted given only 'allowed' policy, brief flags on S1/S3, and no extreme evidence-heavy mandate.
               drivers: residual d/b, must-ev counts, unbacked anchors (21), dominant depth gap, budget-weighted weakest sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.317  P1/light:0.474  P2/standard:0.456  P3/deep:0.442
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-09-09 13:03:31.458 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:03:31.459 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S2 (37% budget) and S3 (35% budget) show large residual depth gaps (14 and 13) with high must-ev counts (8 and 5); article-wide 27 unbacked anchors and dominant depth gap in weakest sections justify gap-filling. Self-cont 'yes' across all and 'brief=yes' on S1-S3 pull downward, but sizeable residuals in the two largest sections outweigh this for P2 (depth-then-breadth) over cheaper P1. External-evidence ALLOWED but not required; gaps are concrete enough to escalate from P0/P1 without reaching P3.
               drivers: residual_depth_S2_S3, high_must_ev, unbacked_anchors_27, depth_dominant
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.386  P2/standard:0.328  P3/deep:0.469
  Regret     : 0.1404  (regret +0.1404)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-09-09 13:03:52.942 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:03:52.945 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: 29 unbacked anchors and dominant depth gap drive escalation; S3/S5 show highest residuals (21/4) plus must-ev totals 10 (esp. S4=4) despite uniform self-cont=yes and brief=yes on S2/S3. Residual depth (15-21 range) exceeds existing cov (~4/8), justifying depth-then-breadth but not P3 given even budgets and no external-evidence mandate.
               drivers: residual depth in weakest sections, must-ev count, unbacked anchors, self-cont vs. resid tension
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.432  P2/standard:0.412  P3/deep:0.328
  Regret     : 0.0209  (regret +0.0209)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-09-09 13:04:51.280 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:04:51.286 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in the two highest-budget sections (S2 33/2 with must-ev 4; S4 54/2 with must-ev 12), producing 40 article-wide unbacked anchors and dominant depth shortfall. Existing cov (≈4·2) fills only a fraction of the mandatory evidence needed for algorithmic details, parameter effects, and Sift1M tradeoffs. P2 supplies depth-first then breadth coverage on the dominant sections while respecting the 'ALLOWED' policy and downward pressure from already-scraped golden sources.
               drivers: residual d/b in S2/S4, must-ev counts (esp. S4), 40 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.338  P1/light:0.426  P2/standard:0.344  P3/deep:0.494
  Regret     : 0.1500  (regret +0.1500)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-09-09 13:05:11.728 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:05:11.729 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S3 shows extreme residual depth (22/6) with cov only 2·0, must-ev=6 and 6 orphans despite 24% budget; article-wide 18 unbacked anchors and dominant depth gap reinforce need, outweighing universal high raw need and self-cont=yes flags. S1 brief=yes and S2's lower residual (11/4) argue against P3; ALLOWED policy permits but does not force exploration, so default stops at depth-then-breadth.
               drivers: S3 residual 22/6 + must-ev, 18 article-wide unbacked anchors, dominant depth gap, S1 brief constraint
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.360  P1/light:0.547  P2/standard:0.473  P3/deep:0.577
  Regret     : 0.1042  (regret +0.1042)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-09-09 13:05:36.953 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:05:36.957 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth remains high in dominant-budget S1 (10) and weakest S4 (11), paired with must-ev of 7/5 and 24 article-wide unbacked anchors; dominant gap is depth while self-cont is uniformly 'yes' and S1/S3 are brief. This justifies depth-first gap-filling but not P3 given partial strength in S3/S5 and no external-evidence mandate.
               drivers: residual depth S1/S4, must-ev counts, unbacked anchors (24), dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.361  P1/light:0.408  P2/standard:0.361  P3/deep:0.328
  Regret     : 0.0464  (regret +0.0464)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-09-09 13:05:54.916 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:05:54.918 | INFO     | logging:callHandlers:1762 | LLM standalone chose P1

  Policy     : capped
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P1 light     [standalone, no RL input]
               reasoning: Capped policy forbids P2/P3; P0 ruled out by high residuals in large-budget sections (S2 12/6 resid at 19%, S19 15/6 at 15%, must-ev 4 and 0), 72 unbacked anchors, and dominant depth gap. Self-cont 'yes' across all sections and many already-high cov scores (e.g. S4/S7/S8/S11–S18 at 7–8 depth) keep the escalation to cheapest valid touch-up only. Guideline's named-source survey scope and 'keep brief' flags on S5 further cap any deeper dive.
               drivers: capped policy, S2/S19 residuals + budget, 72 unbacked anchors, must-ev counts
  -> Chosen  : P1 light  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.341  P1/light:0.338  P2/standard:0.332  P3/deep:0.327
  Regret     : 0.0033  (regret +0.0033)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-09-09 13:06:17.272 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-09 13:06:17.277 | INFO     | logging:callHandlers:1762 | LLM standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S5 dominates at 45% budget with extreme residual depth (42/0), 12 must-ev, 16 orphans despite self-cont=yes and cov 7·4; S4/S1/S2 add further 9/0 residuals each while S7 carries 6 must-ev even at 0 residual. Article-wide 42 unbacked anchors and depth-dominant gaps align with the core DeepSeek techniques/benchmarks that guideline demands. This is sizeable and evidence-driven but not uniformly large enough for P3; P2's depth-then-breadth fills the decisive S5 gap at acceptable cost. Self-cont and strong S7/S8 keep it from P3.
               drivers: S5 residual 42 + must-ev 12 at 45% budget, depth-dominant + 42 unbacked anchors, high must-ev in S4/S6/S7, resid vs self-cont balance
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.277  P1/light:0.349  P2/standard:0.396  P3/deep:0.362
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [Grok-only (standalone baseline)]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST     —    P2    P2  → P2    ✓ EXACT
  07_reasoning_planning                          TEST     —    P2    P2  → P3    ~ NEAR
  13_agent_framework                             TEST     —    P2    P2  → P1    ~ NEAR
  14_agent_system_design                         TEST     —    P2    P2  → P2    ✓ EXACT
  29_evaluation_metrics                          TEST     —    P2    P2  → P2    ✓ EXACT
  31_CI                                          TEST     —    P1    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST     —    P2    P2  → P1    ✓ EXACT
  Dark_Dimension                                 TEST     —    P2    P2  → P3    ~ NEAR
  Distinct_AI_Models                             TEST     —    P2    P2  → P1    ✓ EXACT
  Earth_Oceans_Origin                            TEST     —    P2    P2  → P3    ~ NEAR
  Gravity_Entropy                                TEST     —    P2    P2  → P1    ~ NEAR
  HNSW                                           TEST     —    P2    P2  → P3    ~ NEAR
  Insects_Consciousness                          TEST     —    P2    P2  → P3    ~ NEAR
  Space-Time_QECC                                TEST     —    P2    P2  → P1    ~ NEAR
  State_of_LLM_Reasoning                         TEST     —    P1    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST     —    P2    P2  → P2    ✓ EXACT

  n=16  exact=7 (44%)  near=9 (56%)  miss=0 (0%)  no-oracle/error=0
  Ordinal MAE: 0.562
  Reward-regret (allowed/required only, n=16; 0 forbidden excluded):  mean=0.0355  max=0.1500

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         1         0         0  (n=1)
  P1 light                        0         1     5(✓2)         0  (n=6)
  P2 standard                     0         0         4         0  (n=4)
  P3 deep                         0         0         5         0  (n=5)
  (n(✓k) = of that cell's count, k were tied-arm-accepted EXACT hits, not true misses)

  --- Baselines ---
  Oracle distribution: P0=1  P1=6  P2=4  P3=5
  Majority-class baseline (always P1 light): 50.0%  (8/16)
  Uniform-random baseline:  35.9%
  Weighted-random baseline:  41.0%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P1 light): b=4 c=5 n=9  one-sided p=0.7461  [none]
  Poisson-binomial exact, model vs. per-article chance level: observed=7/16  one-sided p=0.3363  [none]
  Model exact-rate Wilson 95% CI: [23.1%, 66.8%]  (point estimate 43.8%)

================================================================================
  TRAIN (reference)  [Grok-only (standalone baseline)]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN     —    P0    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN     —    P2    P2  → P1    ~ NEAR
  02_workflows_vs_agents__var_demanding          TRAIN     —    P2    P2  → P1    ~ NEAR
  03_context_engineering__var_minimal            TRAIN     —    P0    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN     —    P2    P2  → P2    ✓ EXACT
  03_context_engineering__var_demanding          TRAIN     —    P2    P2  → P1    ~ NEAR
  05_workflow_patterns__var_minimal              TRAIN     —    P0    P0  → P0    ✓ EXACT
  05_workflow_patterns__var_standard             TRAIN     —    P2    P2  → P1    ~ NEAR
  05_workflow_patterns__var_demanding            TRAIN     —    P2    P2  → P1    ~ NEAR
  06_tools__var_minimal                          TRAIN     —    P0    P0  → P0    ✓ EXACT
  06_tools__var_standard                         TRAIN     —    P2    P2  → P3    ~ NEAR
  06_tools__var_demanding                        TRAIN     —    P2    P2  → P1    ~ NEAR
  08_react_practice__var_minimal                 TRAIN     —    P0    P0  → P0    ✓ EXACT
  08_react_practice__var_standard                TRAIN     —    P2    P2  → P1    ~ NEAR
  08_react_practice__var_demanding               TRAIN     —    P2    P2  → P1    ~ NEAR
  09_RAG__var_minimal                            TRAIN     —    P0    P0  → P0    ✓ EXACT
  09_RAG__var_standard                           TRAIN     —    P2    P2  → P3    ~ NEAR
  09_RAG__var_demanding                          TRAIN     —    P2    P2  → P3    ~ NEAR
  10_memory_knowledge_access__var_minimal        TRAIN     —    P0    P0  → P0    ✓ EXACT
  10_memory_knowledge_access__var_standard       TRAIN     —    P2    P2  → P1    ~ NEAR
  10_memory_knowledge_access__var_demanding      TRAIN     —    P2    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN     —    P0    P0  → P0    ✓ EXACT
  11_multimodal__var_standard                    TRAIN     —    P2    P2  → P0    ✗ MISS
  11_multimodal__var_demanding                   TRAIN     —    P2    P2  → P2    ✓ EXACT

  n=24  exact=10 (42%)  near=13 (54%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.625
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0507  max=0.1419

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         0         1         0  (n=9)
  P1 light                        0         0         9         0  (n=9)
  P2 standard                     0         0         2         0  (n=2)
  P3 deep                         0         0         4         0  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=9  P2=2  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline:  25.0%
  Weighted-random baseline:  31.6%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P0 skip): b=2 c=1 n=3  one-sided p=0.5000  [none]
  Poisson-binomial exact, model vs. per-article chance level: observed=10/24  one-sided p=0.0547  [suggestive]
  Model exact-rate Wilson 95% CI: [24.5%, 61.2%]  (point estimate 41.7%)
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 1/8   exact+near 7/8   regret mean=0.0651 max=0.1419
  var_demanding    ( 8):  exact 1/8   exact+near 8/8   regret mean=0.0363 max=0.0592

################################################################################
  COMBINED  [Grok-only (standalone baseline)]  (n=40)
################################################################################
  n=40  exact=17 (42%)  near=22 (55%)  miss=1 (2%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=32; 8 forbidden excluded):  mean=0.0431  max=0.1500