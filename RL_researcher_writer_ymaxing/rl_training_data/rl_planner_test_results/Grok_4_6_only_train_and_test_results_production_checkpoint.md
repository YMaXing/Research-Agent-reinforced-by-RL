================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:20:54.963 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:20:54.968 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, so exploration output cannot be used and P0 is mandatory. Section residuals, unbacked anchors, and depth pressure cannot escalate past that constraint. All sections are also flagged brief with must-ev of 0.
               drivers: external-evidence-forbidden, hard-constraint-P0
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-09-16 18:21:47.026 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:21:47.028 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: S4–S6 (60% of budget) already have resid depth 0, solid cov, and self-contained sources, including the evidence-heavy S5 examples. Remaining residuals sit in S1–S3, but S1/S2 are brief and low-budget so they cannot use extra research; S3 is the only sizeable, must-ev gap. External evidence is allowed not required, so a single cheap round is the cheapest way to patch S3 without over-exploring filled sections.
               drivers: resid-d/b concentrated in S1-S3, S4-S5 already filled (60% budget), all sections self-cont, brief flags on S1/S2/S4/S5, S3 must-ev + orphans, default cheaper, policy ALLOWED
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:23:43.379 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:23:43.381 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S4–S6 (58% of budget) are already filled (resid 0/0, self-cont, cov 7–8·6), so P3 is unjustified waste. S2 and S3 still have large residual depth (42 and 34), must-ev of 5 and 3, and 16+14 orphan depth anchors—the exact all-self-cont-but-large-resid pattern the brief flags as P2—and they plus S1 cover 41% of the article. ALLOWED policy plus 45 unbacked anchors rules out P0; P1 is only a touch-up and would leave the depth-dominant gaps in the weakest sections under-filled.
               drivers: large resid depth in S2/S3, must-ev on S2/S3, 41% budget still gapped, S4-S6 already filled, 45 unbacked anchors, all-self-cont P2 pattern, default-cheaper vs P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.274  P1/light:0.428  P2/standard:0.422  P3/deep:0.319
  Regret     : 0.0062  (regret +0.0062)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:23:55.012 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:23:55.013 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: The article's external-evidence policy is FORBIDDEN, which hard-requires P0 skip because any exploration output is unusable. All eight sections are flagged brief and self-contained with must-ev=0, and the guideline explicitly bars external libraries, named systems, and benchmark papers, so residual depth numbers do not authorize escalation.
               drivers: external-evidence policy forbidden, hard constraint P0, all sections brief/self-cont, must-ev=0
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-09-16 18:25:41.789 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:25:41.792 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: Policy is ALLOWED, so P0 is permitted. Every section is self-contained and S5–S8 (55% of the writing budget, including S6’s 3 must-ev and S7’s 2) already have resid d = 0. Residual depth is concentrated in S1–S4, but S1/S2 are tiny brief intros and S4 has must-ev = 0; S3 is already at 6/8 depth. Default-cheaper plus no large-need plus depth-mandate pair means existing coverage is enough.
               drivers: ALLOWED policy, all sections self-contained, majority-budget resid 0, no depth mandate on weakest sections, default cheaper
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.282  P2/standard:0.316  P3/deep:0.281
  Regret     : 0.0727  (regret +0.0727)
  Verdict    : ✗  MISS

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:26:57.376 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:26:57.377 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: Policy is ALLOWED, so cost follows gaps: residual breadth is ~0 outside tiny S1 while residual depth is large in high-budget S3 (resid 40, 14 depth orphans) and weak S2 (resid 30), with 48 unbacked anchors and a depth-dominant gap—P1’s 50/50 split would waste the breadth half. S6/S5 already have small residuals despite high must-ev, all eight sections are self-contained, and golden sources are specified, so a third round (P3) is not justified. Two rounds (depth then breadth) fill the remaining named-evidence needs without over-exploring the already-strong majority of the word budget.
               drivers: resid-depth in S3/S2, near-zero resid-breadth, 48 unbacked anchors, self-cont + strong S6/S5 downward pressure, ALLOWED not required, must-ev named-evidence mandate
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0361  (regret +0.0361)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:27:08.920 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:27:08.928 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, so exploration output cannot be used and P0 skip is mandatory. Residual depth gaps in S1/S2 and 41 unbacked anchors are irrelevant because the article must stay inside already-fixed course/notebook sources. All seven sections are also marked brief and self-contained, which further argues against any exploration spend.
               drivers: external-evidence-forbidden, hard-constraint-P0
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-09-16 18:28:20.496 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:28:20.497 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED and every section is self-contained, with practice sections (S3, S4, S6, S7) already backed by the course notebook and listed golden sources; must-ev is only 0–2. Residual depth and depth-orphans are concentrated in S1/S2 (resid 29/6 and 37/6; 11 and 13 orphans) and the article still has 41 unbacked anchors plus zero breadth coverage, so a single balanced round is justified. That is not a large depth-mandate plus high-budget gap pattern, so P2/P3 would waste exploration on a notebook-driven lesson.
               drivers: ALLOWED policy, all self-cont, modest must-ev, S1/S2 residual depth and orphans, 41 unbacked anchors, notebook/golden-source practice core, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:29:07.041 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:29:07.049 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : required
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: External-evidence policy is required, so skip is forbidden. S1 and S2 still have large residual depth (54/13, 52/14), must-ev of 7, and most of the 42 unbacked anchors, which is a concrete depth mandate that a cheap P1 touch-up will not fill. The remaining 73% of the article (S3–S7) already has resid depth 0 and is self-contained, so a third expensive round is not justified.
               drivers: policy-required-floor-P1, S1-S2-large-resid-depth, S1-S2-must-ev-7, 42-unbacked-anchors, S3-S7-resid-depth-0, all-self-contained, default-cheaper-vs-P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0355  (regret +0.0355)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:29:16.111 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:29:16.118 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, which hard-requires P0 skip regardless of residual gaps or must-ev. Exploration output cannot be used in this article, so any spend would be pure waste. Section residuals and the 47 unbacked anchors are therefore irrelevant to the preset.
               drivers: external-evidence policy forbidden, hard constraint override
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-09-16 18:31:18.231 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:31:18.231 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S3 and S4 dominate the budget and still show large residual depth (53/6 and 32/6), 17+10 depth orphans, and high must-ev (20 and 9), so existing self-contained sources are not enough. Forty-two unbacked anchors and depth-dominant gaps across more than half the article justify a depth-then-breadth pass rather than a single touch-up. P3 is not warranted: S5–S7 already have small or zero residuals, the lesson is notebook-anchored, and external evidence is only ALLOWED.
               drivers: large resid in high-budget S3/S4, high must-ev, 42 unbacked anchors, depth-dominant gaps, self-cont not sufficient
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0339  (regret +0.0339)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:33:07.076 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:33:07.082 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: External-evidence policy is ALLOWED, so we only explore if gaps justify cost. S5–S8 already have resid 0/0 (or 0/2) and every section is self-contained; S3/S4 residuals are inflated by notebook-walkthrough orphans the guideline already assigns to existing code, with depth coverage already 5–6/8. A single cheap balanced round covers remaining S2 conceptual leftovers plus the extra industry-example and failure-mode requirements without wasting a second round on implementation sections that will not benefit from new web sources.
               drivers: resid-already-filled S5-S8, self-cont all sections, notebook-driven S3/S4, default cheaper, ALLOWED not required, S2 leftover depth, additional industry-evidence extras
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:33:15.241 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:33:15.242 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is forbidden, which hard-requires P0 skip because exploration results cannot be used. The article is a short, notebook-mirroring practice lesson with explicit keep-brief sections and a ban on outside libraries, case studies, and named systems, so new source gathering would also be wasted even if the policy allowed it.
               drivers: external-evidence forbidden, hard constraint P0, notebook-self-contained practice lesson
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-09-16 18:34:21.980 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:34:21.984 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S2 and S4 (34% of budget) plus S1/S3 still have large residual depth (28–41) and many unbacked depth orphans, with S4 also carrying must-ev 12; article-wide 54 unbacked anchors and a depth-dominant gap make one light round insufficient. S5+S6 (44%) are already strong (resid 7/6, self-contained; S5 must stay brief), so a third deep round would be waste. Policy is ALLOWED, so P2 is the cheapest preset that actually fills the remaining high-budget depth gaps.
               drivers: large resid depth S1-S4, S4 must-ev 12, 54 unbacked anchors, dominant gap=depth, S5+S6 already filled/brief, policy ALLOWED
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.1419  (regret +0.1419)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:35:45.735 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:35:45.738 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED not required, every section is self-contained, and this is a 100% practice notebook walkthrough whose primary evidence is already named (notebook plus listed golden sources). Residual depth looks large, but the biggest hole (S5, 28% budget, resid 92) is flagged brief with must-ev=0, so it cannot absorb extra research; remaining must-ev is only 1 each on S1/S2/S4/S6. Those bounded extras (production API swap-ins, circuit-breaker/error handling, test-suite comparisons, named industry/failure examples) justify a cheap touch-up rather than skip, but not a depth-then-breadth campaign.
               drivers: allowed-not-required policy, all sections self-cont, S5 brief + must-ev=0 despite largest resid, modest article-wide must-ev, notebook-first practice lesson, default-cheaper, bounded production/industry extras
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:35:56.132 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:35:56.137 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, so exploration output cannot be used and P0 skip is mandatory. Large residual depth figures and 48 unbacked anchors do not override that hard constraint. The article is a 1500-word conceptual overview with self-contained, mostly brief sections, so skip also matches intended scope.
               drivers: external-evidence-forbidden, hard-constraint-override
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-09-16 18:37:44.329 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:37:44.337 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S3 (20%, not brief) has coverage only 4·1, residual 36/4, 8 must-ev bullets and 12 orphan depth anchors, so named ingestion/retrieval evidence is still missing. S4 (29%) adds 5 must-ev and 10 depth orphans, making half the article an evidence-mandated depth gap that a light touch-up will not fill. P3 is unwarranted because all sections are self-contained, S4/S5 already have high depth coverage, S6 is done, and four sections must stay brief; policy ALLOWED permits P2.
               drivers: S3 must-ev and low coverage, S4 budget plus must-ev, 42 unbacked depth anchors, residuals not small, self-cont caps at P2, brief-section weighting
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0429  (regret +0.0429)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:38:36.551 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:38:36.552 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: Policy is ALLOWED, so exploration is justified only by remaining gaps. Those gaps are concentrated in depth: S3 (19% budget) still has resid 54/2, must-ev 6, and 18 unbacked depth anchors, and S2 is only cov 3·2 with must-ev 3, while 42 article-wide unbacked anchors remain. Breadth residuals are already ~0–2 except S1, so P1’s 50/50 mix would waste budget; P3 is not warranted because every section is self-cont, the largest section (S4, 26%) is already the strongest (cov 6·4), and S1/S5 must stay brief.
               drivers: S3 depth residual + must-ev 6, dominant gap type is depth, 42 unbacked anchors, breadth already mostly filled, all sections self-cont, S4/S5 already strong, default cheaper than P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:38:46.012 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:38:46.016 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, which hard-constrains the article to P0 skip because exploration output cannot be used. Residual depth in S3/S4 and 42 unbacked anchors do not justify escalation when new sources are disallowed. All seven sections are already self-contained and must stay brief, matching the guideline's surface-level conceptual overview.
               drivers: external-evidence forbidden, hard constraint P0, self-contained brief sections
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-09-16 18:39:55.194 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:39:55.204 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED, all seven sections are self-contained, and the two largest sections (S5 19% brief/notebook-constrained, S6 19%) plus S7 already have resid 0, so P2/P3 would waste budget. Residual depth remains in S1–S4 (resid 17/16/19/32) with 42 unbacked anchors and S1’s 3 must-ev bullets, which is enough for one cheap balanced round but not a depth mandate across high-budget sections (S3/S4 have must-ev 0 and coverage already 5–6/8). Named golden sources and a fully specified pedagogical guideline further argue against escalating.
               drivers: allowed-not-required, all-self-contained, S5-S7 already filled, S1 must-ev=3, S3/S4 must-ev=0, high-budget sections covered, named golden sources
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:41:31.971 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:41:31.972 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Coverage is already 6–7/8 depth with breadth residual 0 on every section and all seven sections flagged self-contained, so existing golden sources, the mem0 notebook, and the detailed guideline already carry most of the article. Remaining gaps are named-evidence must-ev bullets (especially S4/S5) plus 42 unbacked anchors and the demanding-variant industry-example/failure-mode requirements—enough to justify one balanced round, not two. Defaulting cheaper rules out P2/P3; P0 would leave those mandatory sourced facts unfilled.
               drivers: high existing depth coverage, all sections self-contained, breadth residual zero, must-ev named-evidence remainder, 42 unbacked anchors, default cheaper, policy allowed
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0412  (regret +0.0412)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-09-16 18:41:38.324 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:41:38.325 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is FORBIDDEN, so exploration results cannot be used in the article and the only valid preset is skip. Residual depth gaps and unbacked anchors are irrelevant under this constraint. The guideline also frames the piece as a brief conceptual overview drawing on fixed course materials, which further confirms no new exploration is warranted.
               drivers: external-evidence-forbidden, hard-constraint-P0
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-09-16 18:42:43.596 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:42:43.602 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S3 is 23% of the article with residual depth 46, must-ev 3, and 16 depth orphans, and S2 (13%) still needs named OCR performance evidence—together a sizeable depth-and-mandate gap in the theory half. S5–S7 are already covered (resid 0, self-cont, notebook-provided), so P3 would overspend, while P1’s single balanced round under-serves a clearly depth-dominant remainder. Policy is ALLOWED, not required or capped, so two rounds (depth then breadth) is the cheapest preset that actually fills those gaps.
               drivers: S3 resid+must-ev+budget, depth-dominant orphans, S2 OCR must-ev, S5-S7 already filled, default-cheaper vs P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.1385  (regret +0.1385)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-09-16 18:43:52.912 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 18:43:52.913 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S3, S5, and S2 (51% of the budget) still show large residual depth (44/25/20), high must-ev (4/6/5), and many orphan depth anchors (16/11/8), with 48 unbacked anchors article-wide and a depth-dominant gap—enough for meaningful depth-then-breadth filling, not a light touch-up. P3 is not warranted: every section is self-contained, S4/S6 already look strong, a notebook plus named golden sources (Raschka, ColPali, CLIP) already back the 70% practice spine, and S1/S8 are tiny. External evidence is only ALLOWED, so we stop at two rounds.
               drivers: high must-ev on S2/S3/S5, depth-dominant residuals, 48 unbacked anchors, S3 budget+orphans, all-sections self-cont, existing golden sources/notebook, default-cheaper vs P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-09-16 19:02:22.384 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:02:22.389 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED, so explore only if gaps justify it. Coverage is not sufficient for P0: 23 unbacked anchors, breadth 0 everywhere, and S4 (40% budget) still has resid 16/6 plus 14 must-ev. Escalation past P1 is not justified: every section is self-contained, 80% of the lesson is a provided-notebook walkthrough (S3–S5), S2 must stay brief, and S1/S6/S7 are 7%/7%/0%. One balanced round can fill remaining Gemini/Pydantic/OpenAI named-source holes without a wasteful depth→breadth second round.
               drivers: self-contained sources, notebook-primary 80% hands-on, S4 must-ev vs residual depth, 23 unbacked anchors, default cheaper, S2 brief / tiny S1-S6-S7, ALLOWED not required
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P2 standard  (tied with P3 deep — either counts as EXACT)
  R_w        : P0/skip:0.316  P1/light:0.273  P2/standard:0.400  P3/deep:0.381
  Regret     : 0.1269  (regret +0.1269)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-09-16 19:03:22.882 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:03:22.884 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Budget-weighted residuals are near zero on S5 and S7 (46% of the article) and tiny on S6/S8; every section is self-contained and must-ev is only three bullets, one of which is already filled. The real leftover is S4 (14%, resid 52/4, 18 depth orphans, must-ev 1) plus smaller S1–S3 gaps that cannot absorb much research. External evidence is allowed not required, so one cheap balanced round is enough rather than P0 (S4 still needs a source touch-up) or P2/P3 (majority of the article is already covered).
               drivers: budget-weighted resid d/b, S5/S7 already filled, S4 depth residual and must-ev, all sections self-cont, policy ALLOWED, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P3 deep  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.077  P1/light:0.038  P2/standard:0.052  P3/deep:0.078
  Regret     : 0.0400  (regret +0.0400)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-09-16 19:04:56.994 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:04:56.998 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Eleven of fifteen sections (S5–S15, ~61% of budget) already have residual depth 0 and no orphan anchors, so existing coverage is sufficient for the deep dives, matrix, pivots, and conclusion. Remaining pressure sits in S1–S4—especially S4 (18% budget, resid 41/4, must-ev 12, 15 depth orphans) plus 42 article-wide unbacked anchors—which justifies a touch-up but not two depth/breadth rounds. All sections are self-contained, golden sources and metric screenshots are already specified, and policy is ALLOWED, so default-cheaper P1 fills the landscape/intro evidence gap with the least waste.
               drivers: resid-d/b concentrated in S1-S4, S5-S15 resid depth 0, S4 must-ev 12 and 15 orphans, 42 unbacked anchors, all self-cont, ALLOWED not required, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.359  P1/light:0.405  P2/standard:0.368  P3/deep:0.376
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-09-16 19:06:13.540 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:06:13.545 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED, every section is self-contained, existing depth is already 6–7/8, and residual breadth is 0 everywhere, so P2/P3 would waste a breadth round. The live gaps are depth-shaped: 42 unbacked anchors plus must-ev 7/6 on budget-heavy S2 and S3 (lost-in-the-middle, test-time scaling, API pricing, HITL/MCP docs). S4’s resid 35 and 13 orphans are mostly original capstone architecture, and S5/S6 cannot absorb research, so one balanced round to land the named golden sources is the cheapest fill that is still justified.
               drivers: self-cont all yes, resid breadth 0, cov depth 6-7/8, unbacked 42, must-ev S2/S3, S4 original architecture, policy ALLOWED, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.380  P2/standard:0.430  P3/deep:0.394
  Regret     : 0.0508  (regret +0.0508)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-09-16 19:07:51.167 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:07:51.172 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED (not required/capped), must-ev is 0 everywhere, and every section is self-contained with major sections already at depth 6/8, so P2/P3 are not justified. Residual depth is still high on the budget-dominant sections (S2 35% and S5 18% each have resid 17/6 and 7 depth orphans) and 47 unbacked anchors remain article-wide with breadth coverage at 0, so existing coverage is not quite sufficient for a skip. One cheap balanced round is enough to attach sources to those orphans without a multi-round hunt.
               drivers: ALLOWED not required, must-ev=0, all self-cont, S2/S5 budget+orphans, 47 unbacked anchors, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.380  P1/light:0.391  P2/standard:0.429  P3/deep:0.386
  Regret     : 0.0378  (regret +0.0378)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-09-16 19:09:13.076 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:09:13.077 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P0

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P0 skip      [standalone, no RL input]
               reasoning: Every section is self-contained with orphans 0/0. Residual depth is 0 on S2–S4 and only 2 on high-budget S5 (17%), S6 (31%), and S7 (12%), so the honest gaps are already mostly filled. must-ev is highest on S2 and S4, which already have cov depth 4–5 and resid 0. S1/S9 look weakest but are 2% and 1% stubs. External evidence is ALLOWED not required, and the guideline already supplies the notebook, configs, and golden sources, so existing coverage is sufficient.
               drivers: all-sections-self-cont, small-resid-depth-on-large-sections, orphans-zero, tiny-weak-sections, policy-allowed-not-required, default-cheaper
  -> Chosen  : P0 skip  (by grok-4.6-only)
  Oracle     : P1 light  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.351  P1/light:0.366  P2/standard:0.340  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-09-16 19:10:45.031 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:10:45.034 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: External evidence is ALLOWED, not required; all four sections are self-contained with depth coverage already 5–7/8 and residual breadth of 0, so a cheap default is warranted. Remaining pressure is real—27 unbacked depth anchors and must-ev of 4–7, concentrated in high-budget S3/S4—but named golden sources already target the core Nature study and supporting papers, so this is a touch-up for leftover quotes and figures rather than a missing-evidence hole. P2/P3 would waste a breadth round and are not justified.
               drivers: policy-allowed-not-required, all-sections-self-contained, residual-breadth-zero, existing-depth-coverage-5-7/8, must-ev-and-orphans-need-touch-up, default-cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.301  P1/light:0.405  P2/standard:0.398  P3/deep:0.363
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-09-16 19:12:17.490 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:12:17.492 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: External evidence is only ALLOWED, every section is self-contained, and existing depth coverage is already 5–6/8, so the default cheaper arm applies and P2/P3 would over-explore. Twenty unbacked anchors plus must-ev of 5/6/8 (S3 also has 9 depth orphans at 46% budget) mean P0 would leave mandatory sourced claims unwritable, so a single balanced round to pick up missing named papers and quotes is the justified touch-up. S1 is brief and only 20% of the budget, so its residual should not drive escalation.
               drivers: ALLOWED policy, all sections self-cont, existing depth 5-6/8, 20 unbacked anchors, high must-ev, S1 brief/small, default cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.515  P2/standard:0.507  P3/deep:0.547
  Regret     : 0.0323  (regret +0.0323)
  Verdict    : ✗  MISS

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-09-16 19:13:12.644 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:13:12.647 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: Policy is ALLOWED not required, all four sections are self-contained, and S1/S3 are marked brief, so the default cheaper arm applies and P2/P3 are not justified. Coverage is already mid-depth (5–6/8) from named golden/other sources, but resid ~10 depth, 21 unbacked anchors, and must-ev of 3–5 (S4=5) mean existing coverage is not sufficient for the required Isola/Huh/Efros/Clune/Wolfram quotes and paper citations. One balanced round is enough to back those named-evidence bullets without over-exploring a 2000-word theory piece.
               drivers: policy-allowed-not-required, all-self-cont, must-ev-S4, unbacked-anchors-21, brief-S1-S3, default-cheaper, mid-depth-coverage
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.317  P1/light:0.474  P2/standard:0.456  P3/deep:0.442
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-09-16 19:14:14.644 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:14:14.647 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S2 and S3 are 72% of the article and still show large residual depth (14/3 and 13/0) plus high must-ev (8 and 5) and 13 orphaned depth anchors, with 27 unbacked claims overall; that is a concrete depth mandate, not a touch-up. Every section is already self-contained and golden/local sources are on hand, so a third round would mostly duplicate existing coverage. External evidence is only ALLOWED, which permits P2 without forcing P3.
               drivers: large resid depth on S2/S3, high must-ev, budget-weighted weakest sections, 27 unbacked anchors, self-cont + golden sources cap at P2, policy ALLOWED
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.386  P2/standard:0.328  P3/deep:0.469
  Regret     : 0.1404  (regret +0.1404)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-09-16 19:16:16.887 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:16:16.891 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: Coverage sits at depth 4/8 with residual depth 15–21 on all five sections and 29 unbacked anchors, so existing scrapes are not sufficient (P0) and a single touch-up round (P1) underfills a depth-dominant article. must-ev pressure is material—especially S4’s 4 mandatory sourced bullets plus S1/S5—and the two largest non-brief sections (S1, S4) can absorb that evidence. All-self-cont plus brief flags on S2/S3, a 2000-word budget, and already-named golden sources (Carney 2025, Jacobson, Verlinde) make P3 unjustified, so P2’s depth-then-breadth pair is the cheapest preset that actually closes the gaps.
               drivers: large resid depth, 29 unbacked anchors, must-ev on S4/S1/S5, depth-dominant gaps, self-cont not overriding resid, brief flags blocking P3, ALLOWED not required/capped
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.432  P2/standard:0.412  P3/deep:0.328
  Regret     : 0.0209  (regret +0.0209)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-09-16 19:17:16.547 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:17:16.551 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S4 (46%) and S2 (35%) dominate the budget with large residual depth (54/2 and 33/2), high must-ev (12 and 4), and many unbacked depth anchors, and no section is self-contained, so existing coverage cannot write the Faiss/Sift1M and foundations claims. Policy is ALLOWED rather than required, S1/S2 are brief, and the outline already names papers, figures, and numeric results, so two rounds of depth-then-breadth fill the gaps without a third expensive pass.
               drivers: high-budget residual depth, S4 must-ev 12, 40 unbacked anchors, not self-contained, ALLOWED not required, brief S1/S2, default-cheaper vs P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.338  P1/light:0.426  P2/standard:0.344  P3/deep:0.494
  Regret     : 0.1500  (regret +0.1500)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-09-16 19:18:03.738 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:18:03.739 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: Policy is ALLOWED, so exploration is permitted. Article-wide 18 unbacked anchors, must-ev of 5–6 in every section, and a depth-dominant residual—especially S3 (resid 22/6, cov 2·0)—mean named studies, declaration wording, and expert quotes still need to be gathered, which exceeds a light touch-up. S2 (45% of budget) already has decent depth (6/8) and every section is self-cont, while S1 is marked brief, so a third deep round would be waste; two rounds (depth then breadth) match the gap.
               drivers: high must-ev across sections, 18 unbacked anchors, S3 residual 22/6 with cov 2·0, depth-dominant gaps, self-cont + S1-brief cap against P3, ALLOWED policy
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.360  P1/light:0.547  P2/standard:0.473  P3/deep:0.577
  Regret     : 0.1042  (regret +0.1042)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-09-16 19:19:18.261 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:19:18.262 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: External evidence is ALLOWED, not required; all five sections are self-contained with depth already at 5–6/8 on S1–S4. S1 and S3 (58% of budget) are brief-flagged and cannot absorb extra research, while S5 is only 8%, so P2/P3 would mostly waste rounds. Residual gaps are real—must-ev of 7 in S1 and 5 in S4, 24 unbacked anchors, weak breadth—but they are quote/named-fact holes against already-matched golden papers, which a single balanced round can cover. Default cheaper arm therefore selects P1, not skip.
               drivers: ALLOWED-not-required, all-sections-self-cont, brief-flags-on-58%-budget, depth-cov-already-5-6/8, must-ev-quotes-still-missing, default-cheaper
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.361  P1/light:0.408  P2/standard:0.361  P3/deep:0.328
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-09-16 19:20:17.733 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:20:17.738 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P1

  Policy     : capped
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P1 light     [standalone, no RL input]
               reasoning: External-evidence policy is CAPPED, so only P0 or P1 are legal. All sections are self-contained and most paper summaries (S4, S6–S18) already have depth 7–8 with residual 0–1, but S2 (19% budget, resid 12/6, must-ev 4) plus S19 (15% budget, resid 15/6) and 72 unbacked anchors are a sizeable remaining depth gap. One balanced light round is the cheapest preset that can touch those gaps without exceeding the named-source cap.
               drivers: capped evidence policy, S2 high-budget resid+must-ev, 72 unbacked anchors, all sections self-contained, paper sections already well covered
  -> Chosen  : P1 light  (by grok-4.6-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.341  P1/light:0.338  P2/standard:0.332  P3/deep:0.327
  Regret     : 0.0033  (regret +0.0033)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-09-16 19:21:22.479 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.x.ai/v1/chat/completions "HTTP/1.1 200 OK"
2026-09-16 19:21:22.481 | INFO     | logging:callHandlers:1762 | LLM standalone (grok-4.6) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  grok-4.6  : P2 standard  [standalone, no RL input]
               reasoning: S5 alone is 45% of the writing budget with resid d/b 42/0, must-ev 12, and 16 depth orphans, and article-wide unbacked anchors are 42 with a depth-dominant gap—this is a concrete, sizeable evidence gap that warrants meaningful filling rather than a light touch-up. Remaining sections do not support P3: S7/S8 already sit at resid 0/0, S3/S6 at 3/0, every section is self-cont, and existing coverage is already 7/8 depth. External evidence is only ALLOWED, so two rounds (depth then breadth) buy the missing S5/S4 facts without over-exploring an otherwise well-matched source set.
               drivers: S5 45% budget + resid 42/0, must-ev 12 and 16 orphans in S5, 42 unbacked anchors / depth-dominant gap, all sections self-cont with cov 7/8, S7/S8 resid 0/0, ALLOWED not required, cheaper-arm default vs P3
  -> Chosen  : P2 standard  (by grok-4.6-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.277  P1/light:0.349  P2/standard:0.396  P3/deep:0.362
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [grok-4.6-only (standalone baseline)]  (n=16)
================================================================================
  Article                                         Spl    RL   LLM  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST     —    P1    P1  → P2    ~ NEAR
  07_reasoning_planning                          TEST     —    P1    P1  → P3    ~ NEAR
  13_agent_framework                             TEST     —    P1    P1  → P1    ✓ EXACT
  14_agent_system_design                         TEST     —    P1    P1  → P2    ~ NEAR
  29_evaluation_metrics                          TEST     —    P1    P1  → P2    ~ NEAR
  31_CI                                          TEST     —    P0    P0  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST     —    P1    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST     —    P1    P1  → P3    ✗ MISS
  Distinct_AI_Models                             TEST     —    P1    P1  → P1    ✓ EXACT
  Earth_Oceans_Origin                            TEST     —    P2    P2  → P3    ~ NEAR
  Gravity_Entropy                                TEST     —    P2    P2  → P1    ~ NEAR
  HNSW                                           TEST     —    P2    P2  → P3    ~ NEAR
  Insects_Consciousness                          TEST     —    P2    P2  → P3    ~ NEAR
  Space-Time_QECC                                TEST     —    P1    P1  → P1    ✓ EXACT
  State_of_LLM_Reasoning                         TEST     —    P1    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST     —    P2    P2  → P2    ✓ EXACT

  n=16  exact=6 (38%)  near=9 (56%)  miss=1 (6%)  no-oracle/error=0
  Ordinal MAE: 0.688
  Reward-regret (allowed/required only, n=16; 0 forbidden excluded):  mean=0.0442  max=0.1500

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         1         0         0  (n=1)
  P1 light                    1(✓1)         4         1         0  (n=6)
  P2 standard                     0         3         1         0  (n=4)
  P3 deep                         0         2         3         0  (n=5)
  (n(✓k) = of that cell's count, k were tied-arm-accepted EXACT hits, not true misses)

  --- Baselines ---
  Oracle distribution: P0=1  P1=6  P2=4  P3=5
  Majority-class baseline (always P1 light): 50.0%  (8/16)
  Uniform-random baseline:  35.9%
  Weighted-random baseline:  41.0%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P1 light): b=1 c=3 n=4  one-sided p=0.9375  [none]
  Poisson-binomial exact, model vs. per-article chance level: observed=6/16  one-sided p=0.5447  [none]
  Model exact-rate Wilson 95% CI: [18.5%, 61.4%]  (point estimate 37.5%)