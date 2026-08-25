================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:19:03.359 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:19:13.691 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: Hard constraint: external-evidence policy explicitly FORBIDDEN, so exploration output cannot be used and P0 is mandatory. All sections flagged self-cont with 'yes'; residuals near-zero in S4–S6 (the largest-budget sections); S1–S3 residuals large but overridden by repeated 'must stay brief', 'surface-level treatment expected' and 'depth NOT required' directives in the guideline.
               drivers: external-evidence policy=forbidden, self-cont=yes across all, brevity flags, low resid in high-budget sections
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-08-24 19:19:13.704 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:19:30.395 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps in S1 (24/10), S2 (39/7), and S3 (46/4) — the latter two flagged as weakest sections — combine for ~40% of writing budget; 42 article-wide unbacked anchors, 37 total orphans concentrated in these sections, must-ev=3 in S3, and dominant depth gap type all indicate concrete evidence shortfalls. Self-cont 'yes' across sections and zero/near-zero residuals in S4–S6 (plus their 'brief' flags) argue against deeper escalation; existing cov (4–5 depth) shows partial fill but not sufficiency for high-need intro/comparison sections.
               drivers: residual depth in S2/S3, high orphans + 42 unbacked anchors, must-ev in S3, dominant depth gap, self-cont + strong S5/S6 coverage
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0774  (regret +0.0774)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:19:30.418 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:19:49.048 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps remain in S2 (42/0) and S3 (34/0) — the second- and third-largest sections by budget — plus 5+3 must-ev items that explicitly require named/sourced evidence; these line up with the article-wide dominant depth gap, 45 unbacked anchors, and weakest-section flags. S4/S5/S6 show 0/0 residuals and self-cont 'yes', so the gaps are concentrated rather than universal; this justifies depth-then-breadth filling but not the cost of a third round.
               drivers: residual depth in S2/S3, must-ev counts, 45 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.274  P1/light:0.394  P2/standard:0.399  P3/deep:0.319
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:19:49.070 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:19:54.151 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: Hard constraint: external-evidence policy explicitly FORBIDDEN, so exploration output cannot be used. All 8 sections flagged 'brief: yes' + 'must stay brief'; self-cont = yes everywhere; guideline demands only conceptual overview with surface-level treatment and no external examples. Residual gaps exist but cannot be addressed and do not justify any spend.
               drivers: external-evidence-forbidden, all-sections-must-stay-brief, self-cont-yes, conceptual-surface-level-scope
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-08-24 19:19:54.277 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:20:10.412 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth in S1/S2/S3/S4 (27/2, 22/4, 23/2, 37/4) on 45% combined budget, plus 42 unbacked anchors and must-ev in S3/S6/S7, show concrete depth gaps in weakest sections despite universal high raw need. All sections self-cont yes and S5-S8 at 0 residual, so no P3; dominant depth gap plus orphans in intro sections rule out P0/P1.
               drivers: residual d/b in S1-S4, must-ev counts, dominant depth gap, unbacked anchors (42)
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.298  P2/standard:0.323  P3/deep:0.281
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:20:10.428 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:20:37.242 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget sections (S3 40/0 at 15%, S2 30/5 at 8%, S7 17/2 at 15%) despite self-cont=yes and moderate cov (3-5/8 depth). Article-wide 48 unbacked anchors, dominant depth gap, ~40 must-ev items (esp. S6=12, S4=7) and requirements for named benchmarks/failure modes/production examples drive gap-filling. Defaults to cheaper but concrete sizeable depth mandates in S2/S3 outweigh P1; P3 not justified as residuals not extreme enough for 3 rounds.
               drivers: resid d/b in S2/S3/S7, must-ev totals, 48 unbacked anchors, dominant depth gap, high-budget sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0361  (regret +0.0361)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:20:37.290 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:20:42.457 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN and exploration output cannot be used, triggering the hard constraint that mandates P0. All sections are flagged 'brief', guideline demands only surface-level conceptual overview with no external libs/case studies/benchmarks, self-cont is 'yes' everywhere, and S7 already shows 0/6 residual depth.
               drivers: external-evidence-forbidden, all-sections-brief, self-cont-yes, resid-0-in-S7
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-08-24 19:20:42.561 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:21:02.696 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps are large and concentrated in foundational S1/S2 (29/6 and 37/6 residuals, 25% combined budget) despite self-cont=yes; article-wide 41 unbacked anchors plus 6 must-ev bullets (esp. S4=2) confirm concrete depth-dominant shortfalls. S3/S6 already strong; guideline emphasizes evidence for benefits, downsides, timing comparisons. This matches P2 (depth→breadth) better than cheaper P1 (insufficient for theory gaps) or costlier P3 (not uniformly large across high-budget practice sections).
               drivers: high residual depth in S1/S2, 41 unbacked anchors, must-ev total=6, depth-dominant economics
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0672  (regret +0.0672)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:21:02.714 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:21:17.900 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S1 and S2 show massive residual depth gaps (54/13 and 52/14) against high must-ev=7, must-cover-in-depth lists, and 42 article-wide unbacked anchors; these foundational 27% budget sections dominate the economics while later sections are already at 0/4 or better residual with strong coverage. Dominant gap type is depth and additional requirements explicitly demand named production examples, failure modes, and industry anchors. This is concrete, sizeable, and evidence-driven but confined to specific sections, so P2 (depth-then-breadth) fills gaps without P3 overkill.
               drivers: high resid depth S1/S2, must-ev=7 in weak sections, 42 unbacked anchors, dominant depth gap, extra production/failure requirements
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0355  (regret +0.0355)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:21:17.912 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:21:23.601 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN; the brief states exploration output cannot be used, so only P0 is valid. All sections flag self-cont=yes with already-matched sources; most sections carry 'must stay brief' and the guideline demands only surface-level conceptual treatment. Large residual depth (e.g. S3 51/2, S2 33/0) is overridden by the hard policy and low writing budgets for theory-heavy parts.
               drivers: external-evidence-forbidden, self-cont=yes across sections, must-stay-brief flags, surface-level guideline
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-08-24 19:21:23.616 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:21:53.256 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth in largest-budget sections S3 (53/6, 26%, must-ev 20, 17 orphans) and S4 (32/6, 16%, must-ev 9, 10 orphans) plus article-wide 42 unbacked anchors and dominant depth gap show concrete sizeable shortfalls in core from-scratch implementation despite universal self-cont=yes. S7/S5 residuals near-zero temper escalation; P2's depth-then-breadth fills evidence needs (esp. must-ev) without P3 overkill on already-matched golden sources/notebook.
               drivers: large resid d/b in S3/S4, high must-ev + orphans in big-budget sections, dominant depth + 42 unbacked, universal self-cont capping at P2
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0339  (regret +0.0339)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:21:53.327 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:22:22.264 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Dominant depth gaps and 47 unbacked anchors are concentrated in high-budget sections S3 (resid 47/2, 24% budget, must-ev 22, 17 orphans) and S2 (resid 32/0, 9% budget), plus sizeable residuals in S4 (28/2, must-ev 11); these are the weakest sections per economics and exceed what self-cont flags can offset. S5–S8 show resid 0/0 with must-ev covered already, so gaps are not article-wide. This justifies P2 depth-then-breadth for concrete gap-filling without P3 overkill on a code-heavy lesson whose notebook sources already anchor most implementation.
               drivers: resid d/b in S2/S3/S4, must-ev 22 in S3, dominant depth + 47 unbacked, high-budget sections, self-cont + strong sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:22:22.292 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:22:27.654 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: HARD CONSTRAINT explicitly states external-evidence policy = forbidden requires P0 skip; exploration output cannot be used. All sections marked self-cont = yes, brief = yes on most, and guideline demands surface-level treatment with no external libs/cases/benchmarks permitted. Residual gaps (e.g. 4/4 across S1–S6) are irrelevant when evidence is disallowed.
               drivers: external-evidence-forbidden, self-cont yes, must-stay-brief flags, surface-level mandate
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-08-24 19:22:27.668 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:22:46.341 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps remain in high-budget S2 (35/4, must-ev 7) and S4 (41/4, must-ev 12) despite self-cont=yes everywhere; these are the weakest sections and align with dominant article-wide depth gap plus 54 unbacked anchors. S5/S6 show only 7/6 residuals and S5 is explicitly brief, so gaps are not uniform. Default to cheaper preset but concrete sizeable depth shortfalls in core implementation sections justify 2-round standard (depth→breadth) over P1.
               drivers: residual d/b in S2/S4, must-ev counts, 54 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.1419  (regret +0.1419)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:22:46.490 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:23:04.203 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget sections S5 (92/4) and S6 (77/4) despite self-cont=yes; 58 article-wide unbacked anchors, dominant depth gap, must-ev=1 in 4 sections, and guideline must-cover-in-depth items (production API replacements, advanced error handling, comprehensive test suites, named failure modes/industry examples) show concrete evidence shortfalls. Existing cov (mostly 3·1) is low relative to needs; P2's depth-then-breadth fills these without P3 cost, as S5's brief flag and self-cont temper escalation. Default to cheaper but gaps are sizeable and evidence-driven.
               drivers: high resid d in S5/S6, 58 unbacked anchors, must-ev + must-cover-depth, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0557  (regret +0.0557)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:23:04.226 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:23:09.896 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: The brief explicitly states external-evidence policy = FORBIDDEN and notes that exploration output cannot be used, triggering the hard constraint that overrides all other signals. All sections are already marked self-cont with 'yes', most carry explicit 'brief' flags, and the guideline repeatedly prohibits external libraries, benchmarks, or case studies. Large residuals (e.g. S3 41/4, must-ev=8) are therefore irrelevant.
               drivers: external-evidence policy, hard constraint, self-cont flags
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-08-24 19:23:09.980 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:23:29.377 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in the two highest-budget sections (S3: 36/4 resid + must-ev 8; S4: 24/5 resid + must-ev 5), which dominate ~49% of the 3170-word article; 42 article-wide unbacked anchors and dominant depth signal confirm concrete evidence shortfalls on tools, models, and techniques named in the guideline. Self-cont 'yes' across all sections and strong S6/S1 coverage support capping at P2 rather than P3; brief flags on S1/S2/S5 further limit escalation.
               drivers: resid d/b in S3/S4, must-ev totals (16), 42 unbacked anchors, dominant depth gap, budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0429  (regret +0.0429)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:23:29.459 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:23:55.336 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth remains large in high-budget S3 (54/2, must-ev=6, 18 orphans, weakest section) and S6 (30/0, must-ev=4) despite universal self-cont=yes and solid cov in S4/S5; article-wide 42 unbacked anchors and depth-dominant gaps confirm concrete shortfalls in core pipeline and conclusion coverage. External policy=ALLOWED permits targeted fill but does not force escalation. P2 (depth→breadth) delivers needed evidence for must-cover items without P3 cost, while P0/P1 insufficient for the size of S3 residual against its 19% budget.
               drivers: high S3 residual + must-ev=6, 42 unbacked anchors, depth-dominant economics, self-cont offset by large resid
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:23:55.437 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:24:00.650 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN, which is a hard constraint that overrides all other signals and mandates P0. All sections are marked self-cont 'yes', S5-S7 show 0/0 residual gaps, every section carries a 'must stay brief' flag, and the guideline repeatedly stresses conceptual overview with no depth or external examples required.
               drivers: external-evidence-forbidden, all-self-cont, zero-residual-in-large-sections, brevity-mandates
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-08-24 19:24:00.748 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:24:19.744 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Large residual depth gaps remain in high-budget sections S3 (19/0), S4 (32/0), S1 (17/0) and S2 (16/0) — the weakest per brief — plus 42 article-wide unbacked anchors and must-ev flags in S1/S2/S5. Dominant gap type is depth while S5–S7 are already strong (0 residuals) and S5 is explicitly brief; self-cont 'yes' across all tempers escalation. This justifies depth-then-breadth (P2) for targeted gap-filling over cheaper P1 or expensive P3.
               drivers: residual d/b in S3/S4, 42 unbacked anchors, dominant depth gaps, must-ev in intro sections, S5 brief constraint
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0193  (regret +0.0193)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:24:19.848 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:24:43.920 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget sections S1-S5 (24/0, 29/0, 29/0, 17/0, 15/0) with must-ev scores of 3-5 each and 42 article-wide unbacked anchors; dominant gap type is depth and weakest sections are S2/S3. All sections self-cont yes and S6/S7 residuals are minimal (3/0, 2/0), so existing sources cover most breadth and some depth but not the mandatory named evidence. This justifies depth-then-breadth gap-filling but not P3.
               drivers: residual d/b in budgeted sections, must-ev counts, dominant depth gaps, unbacked anchors, self-cont + strongest sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-08-24 19:24:44.027 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:24:50.073 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is explicitly FORBIDDEN, triggering the hard constraint that mandates P0. All sections show self-cont=yes, must-ev=0, and most carry explicit 'brief' flags requiring concise overviews only; residual gaps exist but cannot be addressed with exploration output. Article is defined as surface-level conceptual with no depth or external sources allowed.
               drivers: external-evidence-forbidden, self-cont-all-yes, must-ev-zero, brevity-mandates
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-08-24 19:24:50.219 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:25:13.944 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Dominant gap is depth with 42 unbacked anchors; S3 (23% budget) shows resid 46/2 + must-ev=3 + 16 orphans, S2 resid 24/4 + must-ev=1, S1 resid 38/2. These align with guideline demands for OCR benchmarks, architectures, encoders, trade-offs and 2025 model lists. S5-S7 have 0 resid + self-cont yes (S5 brief=yes), so no need to escalate to P3. Self-cont supports all sections but does not override sizeable residuals in largest theory sections.
               drivers: residual depth in S3/S2 (high-budget), must-ev totals (esp. S3=3), 42 unbacked anchors, depth-dominant economics, strongest sections already covered
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.1385  (regret +0.1385)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-08-24 19:25:13.975 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:25:30.754 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S3 (23% budget) shows 44 residual depth + must-ev=4 against heavy 'must cover in depth' demands for named-model benchmarks, architecture trade-offs, and diffusion distinctions; S5 (15%) has 25/0 residual + must-ev=6 on ColPali specifics (nDCG@5, ViDoRe, late-interaction). Article-wide 48 unbacked anchors and depth-dominant gaps confirm sizeable evidence shortfalls in highest-budget theory sections despite universal self-cont='yes'. This justifies 2-round depth-then-breadth filling; cheaper P1 insufficient for must-ev and P3 unwarranted as S4/S6 are stronger and policy only allows external evidence.
               drivers: residual depth in S3/S5, must-ev counts, dominant depth gap, high-budget sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-08-24 19:25:30.936 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:25:50.759 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S4 (40% budget) shows resid 16/6 depth with must-ev=14; S3 (20%) has resid 11/6 + must-ev=8. These dominate the 2250-word article and align with dominant depth gap + 23 unbacked anchors. Self-cont=yes across all and S2 brief=yes argue against P3; residuals already net out prior coverage so P1 is insufficient for mandatory evidence in core implementation sections.
               drivers: resid depth in high-budget S4/S3, high must-ev totals (esp. S4=14), 23 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.276  P1/light:0.315  P2/standard:0.350  P3/deep:0.350
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-08-24 19:25:50.803 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:26:08.171 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth in S1-S4 (26/4, 21/6, 26/6, 52/4) plus 41 article-wide unbacked anchors and must-ev=1 in S4 show concrete depth gaps in foundational sections (14%+9%+9%+6% budget); dominant gap type is depth. However S5/S7 (22%/24% budget) show 0 residual depth, all sections self-cont=yes, and only 3 must-ev total, so 2-round depth-then-breadth suffices; cheaper P1 would leave S4 example/diagram/pros-cons under-sourced while P3 wastes effort on already-covered large sections.
               drivers: resid d/b in S1-S4, 41 unbacked anchors, dominant depth gap, self-cont yes + strong S5/S7, must-ev=1 in key sections
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.050  P1/light:0.001  P2/standard:0.002  P3/deep:0.033
  Regret     : 0.0479  (regret +0.0479)
  Verdict    : ✗  MISS

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-08-24 19:26:08.257 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:26:24.536 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S4 (18% budget) shows massive residual 41/4 depth with 12 must-ev, 15 orphans; S1-S3 add further high residuals (24/6, 20/6, 18/6) plus 42 article-wide unbacked anchors and dominant depth gap. Deep-dive sections (S5-S15) are near-zero residual and self-cont, so P3 is excessive while P1 is insufficient for the evidence-heavy landscape and intro mandates.
               drivers: S4 residual 41/4 + must-ev 12, high residuals in S1-S3, 42 unbacked anchors, dominant depth gap
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.348  P1/light:0.395  P2/standard:0.373  P3/deep:0.391
  Regret     : 0.0215  (regret +0.0215)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-08-24 19:26:24.585 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:26:37.697 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in the dominant-budget sections (S2 20/0 with must-ev 7, S4 35/0 with must-ev 5, S3 18/0 with must-ev 6) that comprise ~81% of the 3200-word article; 42 article-wide unbacked anchors and dominant depth gap confirm concrete missing evidence for the 7-step framework, scaling levers, and capstone application despite universal self-cont 'yes'. S6 is fully covered and S5 is tiny, so escalation stops at P2's depth-then-breadth rather than P3. External-evidence ALLOWED but not required; numbers do not justify deeper spend.
               drivers: residual depth in S2/S3/S4, high must-ev counts, 42 unbacked anchors, dominant depth gap, self-cont vs. budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.268  P1/light:0.370  P2/standard:0.398  P3/deep:0.348
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-08-24 19:26:37.895 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:26:53.695 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in the two highest-budget sections (S2 17/6 at 35%, S5 17/6 at 18%) despite universal self-cont=yes; article-wide 47 unbacked anchors and dominant depth gap type confirm concrete missing evidence for the flywheel mechanics, regression testing, generic-metric pitfalls and binary-vs-Likert arguments. Must-ev=0 and strong self-cont prevent escalation to P3; cheaper P0/P1 insufficient given the size of residuals in dominant sections.
               drivers: resid d/b in S2+S5, dominant depth gap, 47 unbacked anchors, budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.241  P1/light:0.439  P2/standard:0.369  P3/deep:0.373
  Regret     : 0.0699  (regret +0.0699)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-08-24 19:26:53.874 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:27:08.238 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S5/S6/S7 (46% combined budget) show resid 2/6 depth with must-ev 3/2/0; article-wide 42 unbacked anchors and balanced gap type confirm concrete gaps in core practical tiers despite universal self-cont=yes and 0-resid in S2-S4. S1/S9 gaps are high-resid but <3% budget so ignorable. P2 (depth->breadth) fills evidence needs for must-ev sections without P3 overkill; cheaper P1 insufficient for 2-depth residuals in largest sections.
               drivers: resid 2/6 in high-budget S5/S6/S7, must-ev totals (17 across S2-S6), 42 unbacked anchors, self-cont yes but insufficient alone
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.450  P2/standard:0.361  P3/deep:0.357
  Regret     : 0.0888  (regret +0.0888)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-08-24 19:27:08.271 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:27:18.566 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: High residual depth (14-19 across all sections) despite self-cont=yes shows substantial missing evidence even with matched sources; 27 unbacked anchors, dominant depth gap, and must-ev of 7/6 in the two largest-budget sections (S3 29%, S4 32%) confirm sizeable, evidence-driven gaps in measurements, quotes, transcriptomics, and evolutionary timing. Weakest sections are exactly the highest-budget ones. This justifies 2-round depth-then-breadth filling but not the cost of P3; defaults to cheaper preset without hard external-evidence mandate.
               drivers: high residual depth, must-ev counts, 27 unbacked anchors, dominant depth in S3/S4
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.275  P1/light:0.361  P2/standard:0.369  P3/deep:0.289
  Regret     : -0.0078  (regret -0.0078)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-08-24 19:27:18.727 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:27:35.655 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (14 in S2, 23 in S3) with high must-ev (6-8) and 20 article-wide unbacked anchors; dominant gap is depth and S2 (34% budget, no 'brief' flag) is among the weakest sections. Self-cont 'yes' across all tempers escalation but does not override the concrete evidence of missing sourced facts for named models/quotes. Default to cheaper but these signals justify 2-round depth-then-breadth over P1.
               drivers: residual d/b in S2/S3, must-ev counts, 20 unbacked anchors, dominant depth gap, self-cont + brief constraints
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.341  P1/light:0.517  P2/standard:0.511  P3/deep:0.559
  Regret     : 0.0475  (regret +0.0475)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-08-24 19:27:35.696 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:27:47.734 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (10-11) after coverage of only 5-6/8, dominant article-wide gap is depth, 21 unbacked anchors plus must-ev scores of 3-5 (highest in S4 at 5) indicate many specific citations/quotes still missing despite self-cont 'yes' and golden sources already exploited. S3/S4 are weakest; brief flags on S1/S3 limit absorption but S2/S4 budgets (32%/22%) can justify gap-filling. This is concrete enough for P2 but not evidence-heavy enough for P3; P0/P1 insufficient for must-ev.
               drivers: residual d/b (depth-dominant), must-ev counts, unbacked anchors (21), weakest sections S3/S4, self-cont vs. orphans
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.335  P1/light:0.457  P2/standard:0.449  P3/deep:0.453
  Regret     : 0.0043  (regret +0.0043)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-08-24 19:27:47.803 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:01.517 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S2 (37% budget, resid 14/3 depth, must-ev 8) and S3 (35% budget, resid 13/0 depth, must-ev 5) dominate the article and show the largest concrete gaps; 27 article-wide unbacked anchors and depth-dominant economics confirm sizeable missing evidence despite universal self-cont 'yes'. This matches P2's depth-then-breadth pattern; cheaper P1 insufficient for high must-ev in large sections, P3 not justified as residuals are already partially covered and all sections carry 'brief' constraints.
               drivers: residual depth in S2/S3, high must-ev counts, 27 unbacked anchors, depth-dominant economics
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.285  P1/light:0.361  P2/standard:0.304  P3/deep:0.426
  Regret     : 0.1225  (regret +0.1225)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-08-24 19:28:01.628 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:11.139 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large (15-21) in 4/5 sections despite cov≈4/8; dominant gap type is depth with 29 unbacked anchors and 10 must-ev (esp. S4=4 in 22% budget). Self-cont 'yes' everywhere and brief=yes on S2/S3 temper escalation, but high orphans in weakest sections (S3/S5) and explicit must-ev make P1 insufficient. External policy=allowed (not required) keeps it from P3.
               drivers: residual depth 15-21, must-ev total 10 (S4=4), 29 unbacked anchors, weakest S3/S5, self-cont yes + brief flags
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.362  P1/light:0.425  P2/standard:0.412  P3/deep:0.338
  Regret     : 0.0139  (regret +0.0139)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-08-24 19:28:11.157 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:24.311 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain very large in the two highest-budget sections (S2 33, S4 54) that together dominate 81% of the article; must-ev totals 20 (esp. 12 in S4) plus 40 article-wide unbacked anchors and 40 orphans confirm concrete evidence shortfalls on skip-list mechanics, NSW greedy routing, layer-assignment probabilities, Faiss parameter internals, and Sift1M tradeoffs. Coverage achieved is only 4·1–4·2 depth across all sections while dominant gap type is depth; S1/S3 are stronger but their brief flags and tiny budgets do not offset the scale of S2/S4 shortfalls. This justifies two-round depth-then-breadth filling but not the expense of P3.
               drivers: high residual depth in S2/S4, must-ev totals & orphans, dominant depth gap, budget weighting
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.202  P1/light:0.433  P2/standard:0.306  P3/deep:0.349
  Regret     : 0.1273  (regret +0.1273)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-08-24 19:28:24.368 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:39.929 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Dominant depth gap plus 18 unbacked anchors and high must-ev (6/5/6) across sections drive escalation; S3 residual 22/6 with cov only 2·0 is a concrete sizeable gap on 24% budget, while S1 (13/4 residual) and S2 (11/4) also show meaningful shortfalls despite self-cont yes everywhere. S1 brief flag and downward pull from self-cont prevent P3; P1 too cheap for the must-ev + orphan counts and explicit quote/original-result demands in the guideline.
               drivers: S3 residual 22/6 + low cov 2·0, high must-ev and 18 unbacked anchors, dominant depth gap, self-cont yes + S1 brief flag
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.360  P1/light:0.519  P2/standard:0.473  P3/deep:0.579
  Regret     : 0.1059  (regret +0.1059)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-08-24 19:28:40.129 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:54.650 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: Residual depth gaps remain large in high-budget S1 (10) and S4 (11) plus S2 (8); 24 article-wide unbacked anchors, 21 must-ev bullets, and dominant depth type indicate real sourcing needs for specific quotes, conjectures, and reconstructions (e.g. Almheiri-Dong-Harlow, Preskill, firewalls, ER=EPR). All sections self-cont yes and some marked brief temper escalation, but weakest sections (S1/S4) plus 24 orphans justify 2-round depth-then-breadth over cheaper P1; not P3 as gaps not evidence-heavy enough to override default to cheaper preset.
               drivers: high residual depth in S1/S4, 21 must-ev + 24 unbacked anchors, dominant depth gap, self-cont yes but insufficient alone
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.299  P1/light:0.394  P2/standard:0.359  P3/deep:0.336
  Regret     : 0.0357  (regret +0.0357)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-08-24 19:28:54.699 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:28:58.601 | INFO     | logging:callHandlers:1762 | Grok standalone chose P0

  Policy     : forbidden
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P0 skip      [standalone, no RL input]
               reasoning: Hard constraint mandates P0 when external-evidence policy=forbidden; exploration output cannot be used. All sections flagged self-cont with existing sources already matched to topics; residual gaps (e.g. S2 12/6, S19 15/6) cannot be addressed under the policy.
               drivers: external-evidence policy=forbidden, self-cont=yes across all sections, HARD CONSTRAINT override
  -> Chosen  : P0 skip  (by Grok-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.183  P1/light:0.170  P2/standard:0.172  P3/deep:0.172
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-08-24 19:28:58.674 | INFO     | logging:callHandlers:1762 | Processing request of type CallToolRequest
2026-08-24 19:29:20.705 | INFO     | logging:callHandlers:1762 | Grok standalone chose P2

  Policy     : allowed
  RL model   : (skipped — --grok-only baseline)
  Grok 4.2   : P2 standard  [standalone, no RL input]
               reasoning: S5 (45% budget) shows massive residual depth (42/0) plus 12 must-ev and 16 orphans despite self-cont; S4 also has 9/0 residual and 4 must-ev. Article-wide 42 unbacked anchors, dominant depth gap, and weakest sections exactly the DeepSeek case-study core (S4/S5). S7/S8 residuals at 0/0 are strong, but total must-ev (~35) and guideline demands for named benchmarks/rewards/'Aha' moments/contrasts justify depth-first filling over P1; residuals rule out P0 and P3 is not warranted by the already-decent cov 7·4.
               drivers: S5 residual depth + must-ev, article-wide unbacked anchors, dominant depth gap in high-budget technical sections, must-ev volume
  -> Chosen  : P2 standard  (by Grok-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.383  P2/standard:0.400  P3/deep:0.368
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [Grok-only (standalone baseline)]  (n=16)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST     —    P2    P2  → P2    ✓ EXACT
  07_reasoning_planning                          TEST     —    P2    P2  → P0    ✗ MISS
  13_agent_framework                             TEST     —    P2    P2  → P1    ~ NEAR
  14_agent_system_design                         TEST     —    P2    P2  → P2    ✓ EXACT
  29_evaluation_metrics                          TEST     —    P2    P2  → P1    ~ NEAR
  31_CI                                          TEST     —    P2    P2  → P1    ~ NEAR
  Bird_Eye_Extreme                               TEST     —    P2    P2  → P1    ~ NEAR
  Dark_Dimension                                 TEST     —    P2    P2  → P3    ~ NEAR
  Distinct_AI_Models                             TEST     —    P2    P2  → P3    ~ NEAR
  Earth_Oceans_Origin                            TEST     —    P2    P2  → P3    ~ NEAR
  Gravity_Entropy                                TEST     —    P2    P2  → P1    ~ NEAR
  HNSW                                           TEST     —    P2    P2  → P1    ~ NEAR
  Insects_Consciousness                          TEST     —    P2    P2  → P3    ~ NEAR
  Space-Time_QECC                                TEST     —    P2    P2  → P1    ~ NEAR
  State_of_LLM_Reasoning                         TEST     —    P0    P0  → P0    ✓ EXACT
  Understanding_Reasoning_LLMs                   TEST     —    P2    P2  → P2    ✓ EXACT

  n=16  exact=4 (25%)  near=11 (69%)  miss=1 (6%)  no-oracle/error=0
  Ordinal MAE: 0.812
  Reward-regret (allowed/required only, n=15; 1 forbidden excluded):  mean=0.0452  max=0.1273

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         1         0         1         0  (n=2)
  P1 light                        0         0         7         0  (n=7)
  P2 standard                     0         0         3         0  (n=3)
  P3 deep                         0         0         4         0  (n=4)

  --- Baselines ---
  Oracle distribution: P0=2  P1=7  P2=3  P3=4
  Majority-class baseline (always P1 light): 43.8%  (7/16)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  30.5%

================================================================================
  TRAIN (reference)  [Grok-only (standalone baseline)]  (n=24)
================================================================================
  Article                                         Spl    RL  Grok  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN     —    P0    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN     —    P2    P2  → P1    ~ NEAR
  02_workflows_vs_agents__var_demanding          TRAIN     —    P2    P2  → P2    ✓ EXACT
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

  n=24  exact=11 (46%)  near=12 (50%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.583
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0503  max=0.1419

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         0         1         0  (n=9)
  P1 light                        0         0         8         0  (n=8)
  P2 standard                     0         0         3         0  (n=3)
  P3 deep                         0         0         4         0  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=8  P2=3  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline (1/4):  25.0%
  Weighted-random baseline:  29.5%
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 1/8   exact+near 7/8   regret mean=0.0651 max=0.1419
  var_demanding    ( 8):  exact 2/8   exact+near 8/8   regret mean=0.0355 max=0.0592

################################################################################
  COMBINED  [Grok-only (standalone baseline)]  (n=40)
################################################################################
  n=40  exact=15 (38%)  near=23 (57%)  miss=2 (5%)  no-oracle/error=0
  Reward-regret (allowed/required only, n=31; 9 forbidden excluded):  mean=0.0478  max=0.1419