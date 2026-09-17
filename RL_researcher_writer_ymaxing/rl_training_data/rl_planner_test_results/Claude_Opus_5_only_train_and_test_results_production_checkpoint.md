================================================================================
  Variant : 02_workflows_vs_agents__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:31:42.928 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:31:42.931 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The external-evidence policy is 'forbidden', a hard constraint that mandates P0 regardless of gap size. Supporting this, every section is marked self-contained and 'must stay brief', must-ev is 0 everywhere, and the guideline explicitly forbids introducing external libraries, case studies, or named systems beyond the already-established golden sources.
               drivers: external-evidence policy = forbidden, must-ev = 0 in all sections, all sections self-contained and brief-capped, guideline bars new external examples
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.209  P1/light:0.263  P2/standard:0.154  P3/deep:0.216
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 02_workflows_vs_agents__var_standard  [TRAIN]
================================================================================
2026-09-16 19:31:57.153 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:31:57.154 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap and it concentrates in S2 (resid 39/7, 13 orphans) and S3 (resid 46/4, 16 orphans, 3 must-evidence bullets), together ~30% of the writing budget, with S1 adding 8 more orphans. Conversely the biggest sections S5/S4/S6 (60% of budget) have zero residual depth, full coverage and self-contained sources, so no third round is warranted. A depth-then-breadth standard pass targets the 42 unbacked anchors where they actually live without over-spending on already-covered example sections.
               drivers: depth-dominant residual in S2/S3, 42 article-wide unbacked anchors, largest sections (S5/S4/S6) fully covered and self-contained, must-ev bullets in S3/S1 requiring named sources
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.318  P1/light:0.469  P2/standard:0.392  P3/deep:0.366
  Regret     : 0.0774  (regret +0.0774)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 02_workflows_vs_agents__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:32:14.632 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:32:14.633 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth residuals remain substantial in S2 (42/0) and S3 (34/0), the two weakest sections, which together with S1 hold ~41% of the writing budget and 38 of the 45 unbacked anchors. The dominant gap type is depth and these sections carry must-evidence bullets (5 and 3) requiring named examples, costs, and regulated-industry cases, so a depth-first round is warranted. P3 is unjustified because the largest sections (S5 29%, S4 18%, S6 11%) show zero residual and all sections are self-contained.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.274  P1/light:0.428  P2/standard:0.422  P3/deep:0.319
  Regret     : 0.0062  (regret +0.0062)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:32:21.119 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:32:21.122 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The article's external-evidence policy is 'forbidden', a hard constraint that mandates P0 skip regardless of the 47 unbacked anchors or the depth-dominant residuals in S3/S4. The guideline reinforces this: it is a conceptual overview with a fixed golden-source list and an explicit ban on external libraries, case studies, named systems, and benchmark papers. All eight sections are flagged must-stay-brief and self-contained with zero must-cover-evidence bullets, so new exploration could not be used.
               drivers: external-evidence policy = forbidden, all sections brief + self-contained, must-ev = 0 article-wide, guideline bans external examples
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.225  P1/light:0.183  P2/standard:0.204  P3/deep:0.210
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 03_context_engineering__var_standard  [TRAIN]
================================================================================
2026-09-16 19:32:41.934 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:32:41.936 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: 55% of the writing budget (S5-S8) has zero residual need and the highest coverage, so escalation would target only S3/S4. Those weak sections carry must-ev of 0, meaning their residual depth is conceptual narrative rather than sourced-fact demand, while the evidence-heavy sections (S6 must-ev 3, S7 must-ev 2) are already fully covered. All eight sections are self-contained and the guideline is anchored to a fixed golden-source list, so one light balanced round suffices to backfill the S3/S4 orphan anchors.
               drivers: zero residual in 55% of budget, must-ev 0 in the weakest sections (S1, S4), all sections self-contained, evidence-critical sections S6/S7 already covered, policy allowed, not required
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.243  P1/light:0.282  P2/standard:0.316  P3/deep:0.281
  Regret     : 0.0341  (regret +0.0341)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 03_context_engineering__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:32:55.415 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:32:55.418 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap with 48 unbacked anchors and large residuals in the weakest, mid-budget sections S2 (30) and S3 (40), plus S7 (17) — and the guideline requires named evidence (model token limits, lost-in-the-middle research, named production failure mode, library comparisons) reflected in high must-ev counts. That justifies a depth-first pass followed by a breadth sweep. P3 is not warranted because every section is self-contained and the largest section S6 (20% budget) already has only 6/2 residual, so a third round would buy mostly redundancy.
               drivers: depth-dominant gap, 48 unbacked anchors, large residual in S2/S3/S7, high must-ev in S6/S4, all sections self-contained, low residual in largest section S6
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.197  P1/light:0.279  P2/standard:0.243  P3/deep:0.234
  Regret     : 0.0361  (regret +0.0361)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 05_workflow_patterns__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:33:03.064 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:33:03.065 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The external-evidence policy is 'forbidden', a hard constraint that mandates P0 regardless of gap size. The guideline confirms the intent: a ~1,250-word conceptual overview anchored to one course notebook and named golden sources, with external libraries, case studies, and benchmark papers explicitly out of scope. Any exploration output would be unusable, so spending rounds on S1/S2 residual depth would be pure waste.
               drivers: external-evidence policy = forbidden, guideline bans external examples/sources, fixed notebook + golden sources scope, all sections self-contained
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.212  P1/light:0.210  P2/standard:0.232  P3/deep:0.189
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_standard  [TRAIN]
================================================================================
2026-09-16 19:33:24.901 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:33:24.902 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: 67% of the writing budget sits in practice sections (S3, S4, S6, S7) whose residual depth is only 6-10, must-ev is 1-2, and content derives from the supplied lesson notebook rather than the web. The only sizeable residuals (S1=29, S2=37) are theory sections worth just 25% of the budget with must-ev of 1 and 0, and their claims map directly onto the already-named golden sources (Anthropic 'Building Effective Agents', Prompt Chaining Guide). Every section is flagged self-contained, so one cheap balanced round to back the ~24 theory orphans is proportionate; P2/P3 would mostly re-fetch what the notebook and golden sources already give.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.179  P1/light:0.342  P2/standard:0.275  P3/deep:0.290
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 05_workflow_patterns__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:33:33.631 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:33:33.633 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : required
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: External evidence is mandatory, so P0 is excluded. S1 and S2 carry residual depth of 54/52, all but 6 of the article's 42 unbacked anchors, and must-ev 7 apiece, while the guideline additionally demands named production systems/post-mortems for every concept section — a concrete depth-first gap. The remaining 73% of budget (S3–S7) has zero residual depth and self-contained sources, so two rounds (depth then breadth) suffice and a third depth round would be largely wasted.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.233  P1/light:0.399  P2/standard:0.364  P3/deep:0.384
  Regret     : 0.0355  (regret +0.0355)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:33:42.276 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:33:42.278 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The external-evidence policy is 'forbidden', which hard-constrains the decision to P0 skip regardless of the residual depth gaps in S2-S4. The guideline reinforces this: it forbids external libraries, case studies, named systems, or benchmark papers beyond what the course already established, and all content is to be drawn from the provided notebook. Every section is flagged self-contained, so the already-scraped sources are the intended evidence base.
               drivers: external-evidence policy = forbidden, guideline bans external examples/sources, all sections self-contained, notebook is the authoritative code source
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.150  P1/light:0.148  P2/standard:0.122  P3/deep:0.109
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 06_tools__var_standard  [TRAIN]
================================================================================
2026-09-16 19:34:05.591 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:34:05.592 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: S3 (26% budget) and S4 (16%) together hold residual depth of 53/32, 27 orphan depth anchors and 29 must-evidence bullets on top of weak existing coverage (3/8 depth each), and the article-wide dominant gap is depth — enough to justify a depth-then-breadth pass. P3 is not warranted because much of that need is notebook code-step enumeration the provided notebook already satisfies, and S5-S9 (~46% of budget) show residuals of 0-6 with all sections flagged self-contained.
               drivers: depth residual concentrated in the two largest sections, high must-ev in S3/S4 (20/9), 42 unbacked anchors, depth-dominant, low existing depth coverage (3/8) in weakest sections, later sections already near-fully covered -> no third round
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.146  P1/light:0.230  P2/standard:0.231  P3/deep:0.265
  Regret     : 0.0339  (regret +0.0339)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 06_tools__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:34:18.403 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:34:18.406 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: S3 and S4 together hold 39% of the writing budget with large residual depth (47 and 28) and 33 must-evidence bullets, and S2 adds another residual 32 with 10 depth orphans. Article-wide 47 unbacked anchors and a depth-dominant gap type, combined with guideline demands for named production systems and a published failure case, mean real sourced facts are still missing. A depth-then-breadth pass is warranted, but the fully-covered S5-S8 (46% of budget, residual 0) and universal self-containment make a third deep round wasteful.
               drivers: large residual depth in highest-budget sections S3/S4, 33 must-evidence bullets in code-heavy sections, 47 unbacked anchors, depth-dominant gap, named-production-example and failure-case requirements, S5-S8 already at zero residual
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.159  P1/light:0.243  P2/standard:0.183  P3/deep:0.233
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 08_react_practice__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:34:26.237 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:34:26.242 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is 'forbidden', a hard constraint that mandates P0 regardless of residual gaps. The guideline reinforces this: it is a 100% notebook-following practice lesson with an explicit ban on external libraries, case studies, and outside examples, and every section is marked self-contained. Exploration output could not legally be used.
               drivers: external-evidence policy = forbidden, guideline bans external examples, all sections self-contained, notebook is the prioritized source
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.175  P1/light:0.112  P2/standard:0.098  P3/deep:0.049
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_standard  [TRAIN]
================================================================================
2026-09-16 19:34:37.654 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:34:37.655 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: The two highest-budget sections (S5 at 29%, S6 at 15%) have residuals of only 7/6 with 1/0 orphans and are flagged strongest and self-contained, so the article's center of mass is already covered. Remaining depth pressure sits in S2 and S4, whose must-ev items (Gemini function calling config, docstring-derived tool descriptions, real search API alternatives) are satisfiable from the fixed notebook and the already-named Gemini docs. Since this is a 0%-theory, code-walkthrough lesson anchored to one notebook, extra rounds would buy generic ReAct theory the guideline excludes rather than missing evidence.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.203  P1/light:0.283  P2/standard:0.141  P3/deep:0.201
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 08_react_practice__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:34:54.691 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:34:54.697 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Policy is 'allowed' and the guideline's must-cover-in-depth bullets (production search API swap with rate limiting, retry/circuit-breaker error handling, benchmark-style test suites) plus the article-wide demand for named production systems and public post-mortems cannot be satisfied from the notebook alone. 58 unbacked anchors, depth-dominant gaps, and uniformly thin coverage (3/8 depth) concentrated in S5 and S6 — 44% of the writing budget — justify meaningful gap-filling. Every section is self-contained and the core narrative is a fixed code walkthrough, so a third expensive round would mostly buy prose-matching rather than missing evidence.
               drivers: 4 must-ev bullets requiring named production facts, 58 unbacked anchors, depth-dominant, large residuals in S5/S6 (44% of budget), all sections self-contained + fixed notebook core caps escalation at P2
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.170  P1/light:0.228  P2/standard:0.172  P3/deep:0.198
  Regret     : 0.0557  (regret +0.0557)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:35:03.324 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:35:03.325 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The article's external-evidence policy is 'forbidden', a hard constraint that permits only the skip preset. The guideline reinforces this: it is a 1,500-word conceptual overview restricted to course-established concepts, explicitly barring external libraries, case studies, named production systems, and benchmark papers. All sections are marked self-contained, so existing sources plus the fixed golden-source list must suffice.
               drivers: external-evidence policy = forbidden, guideline bars external examples/sources, all sections self-contained, hard 1500-word ceiling, conceptual-only scope
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.120  P1/light:0.117  P2/standard:0.101  P3/deep:0.115
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 09_RAG__var_standard  [TRAIN]
================================================================================
2026-09-16 19:35:15.349 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:35:15.350 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: S3 and S4 hold 49% of the writing budget yet are the weakest sections, with residual depth of 36 and 24, breadth coverage of only 1-2, and 13 combined must-evidence bullets naming concrete tools, embedding models, vector stores, re-rankers and GraphRAG results. Article-wide 42 unbacked anchors with a depth-dominant gap justify a real depth-then-breadth pass. Escalation to P3 is not warranted because all sections are self-contained, the remaining four sections are small with near-zero residuals (S6 at 0/0), and the guideline already supplies a golden-source list.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.077  P1/light:0.104  P2/standard:0.096  P3/deep:0.139
  Regret     : 0.0429  (regret +0.0429)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 09_RAG__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:35:34.542 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:35:34.550 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap: 42 unbacked anchors article-wide, 19 must-evidence bullets, and large depth residuals in the budget-heavy pipeline sections (S3 54/2 with 18 depth orphans, S5 25/0), while breadth residuals are near zero. The guideline's mandatory named tools, embedding models, vector stores, benchmarks and a real post-mortem cannot be written without sourced facts. Escalation to P3 is not justified because every section is self-contained and the largest section (S4, 26%) is already the best covered at 6·4 with a 20/0 residual.
               drivers: depth-dominant residual in S3/S5, 42 unbacked anchors + 19 must-ev bullets, guideline demands named production systems/benchmarks, S4 largest budget already strongest → no P3
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.115  P1/light:0.183  P2/standard:0.161  P3/deep:0.220
  Regret     : 0.0592  (regret +0.0592)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 10_memory_knowledge_access__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:35:42.509 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:35:42.515 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: External-evidence policy is 'forbidden', a hard constraint that mandates P0 regardless of gap size. The guideline reinforces this: it forbids introducing external libraries, case studies, named systems, or benchmark papers beyond what the course already established, and caps the article at 1,500 words. All sections are marked self-contained, so existing scraped sources must carry the writing.
               drivers: external-evidence policy = forbidden, guideline bars external examples/sources, all sections self-contained, hard 1400-1500 word ceiling
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.092  P1/light:0.120  P2/standard:0.040  P3/deep:0.064
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_standard  [TRAIN]
================================================================================
2026-09-16 19:35:58.464 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:35:58.465 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: The two biggest-budget sections (S5, S6 = 38%) have zero residual depth/breadth and zero orphans, and every section is flagged self-contained with a very low mandatory-evidence load (7 must-ev total, mostly 0-1). The residual depth in S1-S4 is largely author-asserted teaching content (analogies, storage pros/cons) already spelled out in the guideline and covered by the named golden sources, not facts needing new sourcing. A single balanced round is enough to back the few genuinely sourced claims (context-window limits, lost-in-the-middle, mem0 description); escalating to P2/P3 would buy prose volume, not missing evidence.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.260  P1/light:0.353  P2/standard:0.334  P3/deep:0.291
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 10_memory_knowledge_access__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:36:11.731 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:36:11.733 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap with 42 unbacked anchors and large residuals concentrated in the high-budget sections S1-S5 (resid depth 15-29), while must-ev of 4-5 in S1/S2/S4/S5 plus the guideline's explicit requirement for named production systems, benchmarks and public post-mortems means those bullets cannot be written from existing sources alone. Breadth residual is zero everywhere and all sections are flagged self-contained, so one depth round followed by a breadth sweep is proportionate. P3 is unjustified because the two strongest sections (S6, S7) covering 26% of budget are nearly complete and a third depth round would largely buy redundancy.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.211  P1/light:0.311  P2/standard:0.314  P3/deep:0.352
  Regret     : 0.0382  (regret +0.0382)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 11_multimodal__var_minimal  [TRAIN]
================================================================================
2026-09-16 19:36:19.364 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:36:19.365 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P0

  Policy     : forbidden
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P0 skip      [standalone, no RL input]
               reasoning: The article's external-evidence policy is 'forbidden', a hard constraint that mandates P0 regardless of gap size. Supporting this, all eight sections are flagged self-contained, and the guideline's brevity requirements explicitly forbid introducing external libraries, case studies, or benchmark papers not already in the course. Remaining residual depth in S1/S3 must be written from the already-scraped golden sources and the provided notebook.
               drivers: external-evidence policy = forbidden, all sections self-contained, guideline bars external examples, fixed golden sources + notebook
  -> Chosen  : P0 skip  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.101  P1/light:0.155  P2/standard:0.067  P3/deep:0.035
  Regret     : +0.0000  (not counted — forbidden policy, P1+ rewards tainted)
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 11_multimodal__var_standard  [TRAIN]
================================================================================
2026-09-16 19:36:35.059 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:36:35.063 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Residual depth is large and concentrated in the biggest-budget theory sections — S3 (23% budget, resid 46 depth, 3 must-ev, 16 orphans) and S2 (13%, resid 24, explicit request for OCR failure-rate numbers) — plus S1's 12 orphan anchors. The practical sections S5–S7 (~38% of budget) already show zero residual depth and self-contained sources, so exploration only needs to target the theory cluster. A depth-then-breadth two-round pass covers that; a third round would largely duplicate the already-named golden sources (Raschka, ColPali paper, CLIP references).
               drivers: large residual depth in S3 (23% budget) and S2, 42 unbacked anchors, depth-dominant, clustered in theory sections, must-evidence bullets needing named models/benchmarks/numbers, S5–S7 already fully covered and notebook-driven
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.312  P1/light:0.276  P2/standard:0.173  P3/deep:0.294
  Regret     : 0.1385  (regret +0.1385)
  Verdict    : ✗  MISS

================================================================================
  Variant : 11_multimodal__var_demanding  [TRAIN]
================================================================================
2026-09-16 19:36:53.332 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:36:53.334 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: The budget-dominant theory sections (S3 23%, S5 15%, S2 13%) carry large depth residuals (44, 25, 20), 35 of the article's 48 unbacked anchors, and 15 must-evidence bullets requiring named benchmarks and figures (ViDoRe nDCG@5, ColPali latency gains, OCR failure metrics, model-family capabilities) that current coverage (6-8 depth) cannot back. Dominant gap type is depth, so a depth-then-breadth two-round pass is the right buy. P3 is not justified because breadth residuals are ~0, every section is self-contained, and the code-driven sections (S4, S6, S7) are already the strongest with residuals of 6-10.
               drivers: depth-dominant residuals in high-budget theory sections, 48 unbacked anchors, 15 must-evidence bullets needing named benchmarks/numbers, near-zero breadth residuals argue against P3, practical sections already well covered by notebook sources
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.275  P1/light:0.273  P2/standard:0.313  P3/deep:0.273
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 04_structured_outputs  [TEST]
================================================================================
2026-09-16 19:37:04.590 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:37:04.594 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: The article is a notebook-driven code lesson: the high must-ev counts in S3 (8) and S4 (14) point to the author-supplied notebook and a fixed golden-source list, not to open research gaps. All seven sections are self-contained with existing coverage in the heaviest sections (S4 cov depth 5, 40% of budget), so residual need is largely prose rather than missing evidence. A single light round suffices to back the theory claims in S2 (4 must-ev, 5 orphan anchors) and the Pydantic-vs-TypedDict/dataclass comparison in S4.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P2 standard  (tied with P3 deep — either counts as EXACT)
  R_w        : P0/skip:0.316  P1/light:0.273  P2/standard:0.400  P3/deep:0.381
  Regret     : 0.1269  (regret +0.1269)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 07_reasoning_planning  [TEST]
================================================================================
2026-09-16 19:37:24.838 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:37:24.839 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: The two biggest sections (S7 24%, S5 22%) already show zero residual depth and top coverage, so nearly half the writing budget needs no new evidence. The remaining pressure is concentrated in S4 (14% budget, resid 52/4, 18 orphan depth anchors, a must-evidence bullet on the ReAct loop) plus the smaller S1-S3 motivational sections, and the article-wide 41 unbacked anchors are depth-dominant. That warrants a depth-then-breadth pass, but the theory-only scope, low must-ev count (3), and universally self-contained sections rule out the expensive P3 arm.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.077  P1/light:0.038  P2/standard:0.052  P3/deep:0.078
  Regret     : 0.0256  (regret +0.0256)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 13_agent_framework  [TEST]
================================================================================
2026-09-16 19:37:43.790 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:37:43.795 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: Residual depth is 0 across S5–S15, which together hold ~54% of the writing budget and are all flagged self-contained, so the deep dives need no new evidence. The only substantive gap is S4 (18% budget, resid 41/4, 15 orphans, 12 must-ev), and most of its adoption metrics and images are already specified verbatim in the guideline with a fixed golden-source list of official docs. S1–S3's large residuals are internal capstone narrative and decision-axis framing that external search cannot supply, so a single balanced round to firm up S4's framework claims is the right cost.
               drivers: zero residual depth in 10 of 15 sections, gaps concentrated in one section (S4), S1-S3 gaps are internal/narrative, not searchable, golden sources already enumerated
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.359  P1/light:0.405  P2/standard:0.368  P3/deep:0.376
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 14_agent_system_design  [TEST]
================================================================================
2026-09-16 19:38:03.161 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:38:03.162 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: The three budget-dominant sections (S2 31%, S3 22%, S4 28%) each carry large residual depth (20/18/35) with high must-evidence counts (7/6/5), and 42 article-wide unbacked anchors with depth as the dominant gap type — the cost/latency calculus in S3 and the framework steps in S2 cannot be written credibly without named pricing, test-time-scaling research, and the lost-in-the-middle source. P3 is not justified because breadth residual is zero everywhere, coverage already sits at 6-7/8 depth, all sections are self-contained, and S4's huge residual is internal capstone architecture that external exploration cannot supply.
               drivers: large residual depth in 80% of writing budget, high must-ev counts in S2/S3, 42 unbacked anchors, depth-dominant gap, zero breadth residual and all sections self-contained (caps escalation)
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.250  P1/light:0.380  P2/standard:0.430  P3/deep:0.394
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : 29_evaluation_metrics  [TEST]
================================================================================
2026-09-16 19:38:21.135 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:38:21.181 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: Every section is self-contained with must-ev = 0, and the lesson is 100% theory grounded in an already-supplied golden-source list, so there is no evidence mandate to justify escalation. Residual depth is only moderate (10-20) and breadth orphans are zero, indicating the unbacked anchors are mainly the author's own argumentative claims. A single balanced round is enough to add a few named citations for the heavy sections S2 and S5 (53% of budget) where breadth coverage is currently 0 and depth orphans sit at 7 each.
               drivers: must-ev = 0 in all sections, self-contained sources everywhere, moderate residual depth, zero breadth orphans, 100% theory / opinion-driven guideline with golden sources listed, breadth coverage 0 across sections warrants one balanced round
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.380  P1/light:0.391  P2/standard:0.429  P3/deep:0.386
  Regret     : 0.0378  (regret +0.0378)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : 31_CI  [TEST]
================================================================================
2026-09-16 19:38:36.452 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:38:36.457 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: The dominant-budget sections (S6 31%, S5 17%, S2 14%, S4 12%) all carry residual depth of only 0-2 and are flagged self-contained, and their must-cover evidence (ci.yml, pyproject/Ruff config, Makefile targets, FakeModel code) is reproduced verbatim in the guideline or sits in fixed golden sources already scraped. The remaining gaps are breadth-flavored and small: a concrete eval cost figure in S7 and minor GitHub Actions framing, plus the weakest sections S1/S9 which together hold only 3% of the budget. That profile warrants a cheap touch-up, not depth-first multi-round exploration.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light  (tied with P0 skip — either counts as EXACT)
  R_w        : P0/skip:0.351  P1/light:0.366  P2/standard:0.340  P3/deep:0.339
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Bird_Eye_Extreme  [TEST]
================================================================================
2026-09-16 19:38:49.873 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:38:49.877 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: Every section is self-contained with depth coverage already 5-7/8 against a fixed roster of named golden/local sources, so the remaining need is narrow: attributed quotes (Damsgaard, Baden, Lewin) and a few framing numbers that probably live outside the scraped PDFs. Total budget is only 2,050 words across four short sections, so extra rounds would add little writable evidence. A single balanced round covers the orphaned quote/number anchors without waste.
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.301  P1/light:0.405  P2/standard:0.398  P3/deep:0.363
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Dark_Dimension  [TEST]
================================================================================
2026-09-16 19:39:06.373 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:39:06.375 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap and it concentrates in the two largest sections: S3 (46% budget) still has residual 23/4 with 9 orphaned depth anchors and 8 must-evidence bullets, while S2 (34%) has residual 14/4 with 6 must-evidence bullets. Much of the missing material is named, sourced fact — specific 2025 model predictions, the Kamionkowski–Kesden 2006 bound, and numerous attributed quotes — which the current arXiv-only source set does not supply. A depth-then-breadth two-round pass targets exactly this; the 1,800-word budget and universal self-containment make a third deep round wasteful.
               drivers: large residual depth in S3/S2 (80% of budget), 20 unbacked anchors, depth-dominant, high must-ev counts requiring named quotes/numbers, modest total word budget caps escalation
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.515  P2/standard:0.507  P3/deep:0.547
  Regret     : 0.0405  (regret +0.0405)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Distinct_AI_Models  [TEST]
================================================================================
2026-09-16 19:39:20.046 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:39:20.048 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Every section carries large residual depth (10-11) with only 1-2/6 breadth coverage, 21 unbacked anchors, and depth is the dominant gap type. The guideline's mandatory bullets require named, sourced quotes (Isola, Sucholutsky, Huh, Wolfram, Efros, Clune) and specific experimental details that the listed arXiv golden sources will not supply, so must-ev pressure (3/3/3/5) is real across all four budget-weighted sections. Two rounds of depth-then-breadth fills these evidence gaps without over-buying for a 2,000-word article that already has moderate (5-6/8) depth coverage.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light  (tied with P2 standard — either counts as EXACT)
  R_w        : P0/skip:0.317  P1/light:0.474  P2/standard:0.456  P3/deep:0.442
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  Variant : Earth_Oceans_Origin  [TEST]
================================================================================
2026-09-16 19:39:35.415 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:39:35.423 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: S2 and S3 together hold 72% of the writing budget and carry the largest residual depth gaps (14/3 and 13/0) plus 13 of the 17 must-evidence bullets, with 27 unbacked anchors article-wide and depth as the dominant gap type. The guideline requires many named, quotable specifics (Hale-Bopp, Hartley 2/Herschel, 12P/Pons-Brooks, Xe/Kr mismatches, attributed scientist quotes) that the existing golden sources do not obviously supply. Breadth residual is minimal (0 in S3) and every section is self-contained, so a depth-first round with a single breadth sweep is sufficient; a third round would be waste on a 2,550-word article.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep
  R_w        : P0/skip:0.319  P1/light:0.386  P2/standard:0.328  P3/deep:0.469
  Regret     : 0.1404  (regret +0.1404)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Gravity_Entropy  [TEST]
================================================================================
2026-09-16 19:39:49.000 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:39:49.003 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Every section sits at only 4/8 depth with breadth 1-3/6, leaving residual depth of 15-21 and 29 unbacked anchors article-wide, with depth the dominant gap type. The guideline mandates numerous named researcher quotes (Carney, Van Raamsdonk) and specific critiques that the three listed arXiv preprints cannot supply, so genuine sourced depth is missing. But the article is short (2,000 words), all sections are self-contained with modest must-ev counts and small breadth residuals, so a third deep round would buy little beyond redundancy.
               drivers: large residual depth across all budget-weighted sections, 29 unbacked anchors; dominant gap = depth, quote/attribution mandates need sourced evidence beyond the 3 listed preprints, small breadth residuals and self-contained sections argue against P3
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.352  P1/light:0.432  P2/standard:0.412  P3/deep:0.328
  Regret     : 0.0209  (regret +0.0209)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : HNSW  [TEST]
================================================================================
2026-09-16 19:40:03.666 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:40:03.674 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: The two sections holding 81% of the writing budget (S4 46%, S2 35%) both carry large residual depth needs (54/2 and 33/2), 29 of the article's 40 unbacked anchors, and neither is flagged self-contained. S4 alone has 12 must-evidence bullets requiring named Faiss internals and Sift1M empirical measurements, so depth-first exploration is genuinely warranted. P3 is unjustified because strong golden sources already cover the theoretical pillars and the key empirical numbers are pre-specified in the guideline, making a third round largely redundant.
               drivers: depth-dominant gap in the two highest-budget sections, 12 must-evidence bullets in S4 (46% of budget), 40 article-wide unbacked anchors, no section self-contained, existing golden sources cap the upside of a third round
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.338  P1/light:0.426  P2/standard:0.344  P3/deep:0.494
  Regret     : 0.1500  (regret +0.1500)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Insects_Consciousness  [TEST]
================================================================================
2026-09-16 19:40:20.029 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:40:20.037 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Policy allows exploration, and 18 article-wide unbacked anchors with depth-dominant gaps make a single light round insufficient. S3 (24% budget) is essentially uncovered (2 depth / 0 breadth, residual 22/6, 6 must-evidence bullets, 6 orphan anchors), while S1 and S2 retain 13/4 and 11/4 residuals and 5 orphans each; breadth coverage is near zero everywhere. Self-contained sources and the modest 1,900-word budget argue against the expense of P3, so a two-round depth-then-breadth pass is the best value.
               drivers: 18 unbacked anchors article-wide, S3 near-zero coverage with 6 must-ev bullets, breadth coverage ~0 in all sections, depth-dominant gap type, self-contained sources cap escalation below P3
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P3 deep  (tied with P1 light — either counts as EXACT)
  R_w        : P0/skip:0.360  P1/light:0.547  P2/standard:0.473  P3/deep:0.577
  Regret     : 0.1042  (regret +0.1042)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Space-Time_QECC  [TEST]
================================================================================
2026-09-16 19:40:34.095 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:40:34.096 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: Depth is the dominant gap and it sits in the two budget-heaviest, weakest sections: S1 (34% budget, resid 10/8, must-ev 7) and S4 (18%, resid 11/4, must-ev 5), which together need named quotes (Aaronson, Preskill, Hayden, Almheiri) and specific facts (three-quarters reconstruction threshold, DoD-funded holographic code programs, recent dS/CFT work) that 24 unbacked anchors confirm are not yet sourced. Existing golden sources cover the theory backbone, so one depth round plus a breadth sweep should close the attributed-quote and follow-up-research gaps. P3 is not justified: S3/S5 residuals are small, every section is self-contained, and the total budget is only 2,500 words.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P1 light
  R_w        : P0/skip:0.361  P1/light:0.408  P2/standard:0.361  P3/deep:0.328
  Regret     : 0.0464  (regret +0.0464)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : State_of_LLM_Reasoning  [TEST]
================================================================================
2026-09-16 19:40:47.833 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:40:47.835 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P1

  Policy     : capped
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P1 light     [standalone, no RL input]
               reasoning: The capped external-evidence policy restricts the choice to skip or light. 72 unbacked anchors and large residual depth gaps concentrated in the two highest-budget sections (S2 at 19% with resid 12/6 and must-ev 4; S19 at 15% with resid 15/6 and 7 depth orphans) rule out skip. Most small per-paper sections already show residuals of 0-1 and are self-contained, so one balanced round is the right proportionate spend.
               drivers: capped policy hard constraint, 72 unbacked anchors, weakest sections S2/S19 hold 34% of budget, small sections already near-fully covered
  -> Chosen  : P1 light  (by claude-opus-5-only)
  Oracle     : P0 skip
  R_w        : P0/skip:0.341  P1/light:0.338  P2/standard:0.332  P3/deep:0.327
  Regret     : 0.0033  (regret +0.0033)
  Verdict    : ~  NEAR MISS  (±1 preset)

================================================================================
  Variant : Understanding_Reasoning_LLMs  [TEST]
================================================================================
2026-09-16 19:41:00.042 | INFO     | logging:callHandlers:1762 | HTTP Request: POST https://api.anthropic.com/v1/messages "HTTP/1.1 200 OK"
2026-09-16 19:41:00.045 | INFO     | logging:callHandlers:1762 | LLM standalone (claude-opus-5) chose P2

  Policy     : allowed
  RL model   : (skipped — --llm-only baseline)
  claude-opus-5: P2 standard  [standalone, no RL input]
               reasoning: S5 holds 45% of the writing budget with residual depth 42, 16 orphaned depth anchors and 12 must-evidence bullets (benchmarks, reward definitions, distillation-vs-RL results), which is a real, sizeable, evidence-driven gap that justifies escalation past a light touch-up. All other weighted sections are near-filled (S7/S8 residual 0, S3/S6 residual 3) and every section is self-contained against the four golden sources, so breadth pressure is nil and a third deep round would mostly re-mine material already gathered. A depth-first, breadth-second standard pass targets the one dominant section without overspending.
  -> Chosen  : P2 standard  (by claude-opus-5-only)
  Oracle     : P2 standard
  R_w        : P0/skip:0.277  P1/light:0.349  P2/standard:0.396  P3/deep:0.362
  Regret     : 0.0000
  Verdict    : ✓  EXACT HIT

================================================================================
  TEST  (held-out, primary metric)  [claude-opus-5-only (standalone baseline)]  (n=16)
================================================================================
  Article                                         Spl    RL   LLM  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  04_structured_outputs                          TEST     —    P1    P1  → P2    ~ NEAR
  07_reasoning_planning                          TEST     —    P2    P2  → P3    ~ NEAR
  13_agent_framework                             TEST     —    P1    P1  → P1    ✓ EXACT
  14_agent_system_design                         TEST     —    P2    P2  → P2    ✓ EXACT
  29_evaluation_metrics                          TEST     —    P1    P1  → P2    ~ NEAR
  31_CI                                          TEST     —    P1    P1  → P1    ✓ EXACT
  Bird_Eye_Extreme                               TEST     —    P1    P1  → P1    ✓ EXACT
  Dark_Dimension                                 TEST     —    P2    P2  → P3    ~ NEAR
  Distinct_AI_Models                             TEST     —    P2    P2  → P1    ✓ EXACT
  Earth_Oceans_Origin                            TEST     —    P2    P2  → P3    ~ NEAR
  Gravity_Entropy                                TEST     —    P2    P2  → P1    ~ NEAR
  HNSW                                           TEST     —    P2    P2  → P3    ~ NEAR
  Insects_Consciousness                          TEST     —    P2    P2  → P3    ~ NEAR
  Space-Time_QECC                                TEST     —    P2    P2  → P1    ~ NEAR
  State_of_LLM_Reasoning                         TEST     —    P1    P1  → P0    ~ NEAR
  Understanding_Reasoning_LLMs                   TEST     —    P2    P2  → P2    ✓ EXACT

  n=16  exact=6 (38%)  near=10 (62%)  miss=0 (0%)  no-oracle/error=0
  Ordinal MAE: 0.625
  Reward-regret (allowed/required only, n=16; 0 forbidden excluded):  mean=0.0435  max=0.1500

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         0         1         0         0  (n=1)
  P1 light                        0         3     3(✓1)         0  (n=6)
  P2 standard                     0         2         2         0  (n=4)
  P3 deep                         0         0         5         0  (n=5)
  (n(✓k) = of that cell's count, k were tied-arm-accepted EXACT hits, not true misses)

  --- Baselines ---
  Oracle distribution: P0=1  P1=6  P2=4  P3=5
  Majority-class baseline (always P1 light): 50.0%  (8/16)
  Uniform-random baseline:  35.9%
  Weighted-random baseline:  41.0%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P1 light): b=2 c=4 n=6  one-sided p=0.8906  [none]
  Poisson-binomial exact, model vs. per-article chance level: observed=6/16  one-sided p=0.5447  [none]
  Model exact-rate Wilson 95% CI: [18.5%, 61.4%]  (point estimate 37.5%)

================================================================================
  TRAIN (reference)  [claude-opus-5-only (standalone baseline)]  (n=24)
================================================================================
  Article                                         Spl    RL   LLM  Chsn  → Orcl  Verdict
  ----------------------------------------------------------------------------
  02_workflows_vs_agents__var_minimal            TRAIN     —    P0    P0  → P0    ✓ EXACT
  02_workflows_vs_agents__var_standard           TRAIN     —    P2    P2  → P1    ~ NEAR
  02_workflows_vs_agents__var_demanding          TRAIN     —    P2    P2  → P1    ~ NEAR
  03_context_engineering__var_minimal            TRAIN     —    P0    P0  → P0    ✓ EXACT
  03_context_engineering__var_standard           TRAIN     —    P1    P1  → P2    ~ NEAR
  03_context_engineering__var_demanding          TRAIN     —    P2    P2  → P1    ~ NEAR
  05_workflow_patterns__var_minimal              TRAIN     —    P0    P0  → P0    ✓ EXACT
  05_workflow_patterns__var_standard             TRAIN     —    P1    P1  → P1    ✓ EXACT
  05_workflow_patterns__var_demanding            TRAIN     —    P2    P2  → P1    ~ NEAR
  06_tools__var_minimal                          TRAIN     —    P0    P0  → P0    ✓ EXACT
  06_tools__var_standard                         TRAIN     —    P2    P2  → P3    ~ NEAR
  06_tools__var_demanding                        TRAIN     —    P2    P2  → P1    ~ NEAR
  08_react_practice__var_minimal                 TRAIN     —    P0    P0  → P0    ✓ EXACT
  08_react_practice__var_standard                TRAIN     —    P1    P1  → P1    ✓ EXACT
  08_react_practice__var_demanding               TRAIN     —    P2    P2  → P1    ~ NEAR
  09_RAG__var_minimal                            TRAIN     —    P0    P0  → P0    ✓ EXACT
  09_RAG__var_standard                           TRAIN     —    P2    P2  → P3    ~ NEAR
  09_RAG__var_demanding                          TRAIN     —    P2    P2  → P3    ~ NEAR
  10_memory_knowledge_access__var_minimal        TRAIN     —    P0    P0  → P0    ✓ EXACT
  10_memory_knowledge_access__var_standard       TRAIN     —    P1    P1  → P1    ✓ EXACT
  10_memory_knowledge_access__var_demanding      TRAIN     —    P2    P2  → P3    ~ NEAR
  11_multimodal__var_minimal                     TRAIN     —    P0    P0  → P0    ✓ EXACT
  11_multimodal__var_standard                    TRAIN     —    P2    P2  → P0    ✗ MISS
  11_multimodal__var_demanding                   TRAIN     —    P2    P2  → P2    ✓ EXACT

  n=24  exact=12 (50%)  near=11 (46%)  miss=1 (4%)  no-oracle/error=0
  Ordinal MAE: 0.542
  Reward-regret (allowed/required only, n=16; 8 forbidden excluded):  mean=0.0386  max=0.1385

  --- Confusion matrix ---
                           Predicted →
  Oracle ↓                      skip     light  standard      deep
  ------------------------------------------------------------
  P0 skip                         8         0         1         0  (n=9)
  P1 light                        0         3         6         0  (n=9)
  P2 standard                     0         1         1         0  (n=2)
  P3 deep                         0         0         4         0  (n=4)

  --- Baselines ---
  Oracle distribution: P0=9  P1=9  P2=2  P3=4
  Majority-class baseline (always P0 skip): 37.5%  (9/24)
  Uniform-random baseline:  25.0%
  Weighted-random baseline:  31.6%

  --- Significance tests ---
  McNemar exact, model vs. majority-class (P0 skip): b=4 c=1 n=5  one-sided p=0.1875  [suggestive]
  Poisson-binomial exact, model vs. per-article chance level: observed=12/24  one-sided p=0.0072  [strong]
  Model exact-rate Wilson 95% CI: [31.4%, 68.6%]  (point estimate 50.0%)
  var_minimal      ( 8):  exact 8/8   exact+near 8/8   regret n/a (all policy-forced)
  var_standard     ( 8):  exact 3/8   exact+near 7/8   regret mean=0.0408 max=0.1385
  var_demanding    ( 8):  exact 1/8   exact+near 8/8   regret mean=0.0363 max=0.0592

################################################################################
  COMBINED  [claude-opus-5-only (standalone baseline)]  (n=40)
################################################################################
  n=40  exact=18 (45%)  near=21 (52%)  miss=1 (2%)  no-oracle/error=0