# Exploitation Digest — Workflows vs. Agents

## 1. Source Inventory

### Golden Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
| a-developer-s-guide-to-building-scalable-ai-workflows-vs-age.md | web | Comprehensive comparison of workflows (structured pipelines like RAG with chaining/routing) vs. agents (autonomous loops); decision framework (5-factor scoring: task complexity, value/volume, reliability, maturity); hybrids; benchmarks (Bain 2024: 95% gen AI use, 79% agents but 1% mature; Klarna agent=700 reps; costs: workflows $500/mo vs agents $2k); tools (CrewAI, LangGraph, LangChain chains/agents, LangFuse). |
| building-effective-agents.md | web | Anthropic guide: workflows (prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer) vs. agents (dynamic loops for open-ended tasks); principles (simplicity, ACI via tools); frameworks (Claude Agent SDK, Strands, Rivet, Vellum); examples (SWE-bench, customer support/coding); claims workflows predictable, agents error-prone. |
| exploring-the-difference-between-agents-and-workflows.md | web | Workflows (fixed sequences) vs. agents (ReAct: reason-act-observe); "Second Brain" Agentic RAG example (SmolAgents, MongoDBRetrieverTool, HuggingFaceSummarizerTool); evals (Opik: NDCG/MRR, Hallucination, latency/costs); claims agents for multi-query refinement. |
| what-is-an-ai-agent.md | web | Agent definition (autonomous via reasoning/planning/memory/tools per ReAct); vs. assistants/bots; components (persona, memory types, tools); types (single/multi, interaction-based); benefits/challenges; deployment (Cloud Run, ADK). |
| kQxr-uOxw2o.md | youtube | Workflows (orchestrate via code: SQL gen/exec, routers, orchestrator-synthesizer) vs. real agents (System 2 reasoning, dynamic planning); examples (CrewAI=workflows, o1/o3-mini, Devin, Anthropic computer use, Cursor); claims agents overhyped, workflows power most apps. |

### Exploitation Sources
| Source | Type | Key Contributions |
|--------|------|------------------|
| 601-real-world-gen-ai-use-cases-from-the-world-s-leading-org.md | web | 1,001 gen AI cases across industries via Vertex AI/Gemini; agent types (customer/employee/creative/code/data/security); examples (Mercedes MBUX, LUXGEN 30% workload cut, Rivian NotebookLM, BBVA 3hrs/week saved, Virgin Veo ads $17M lift); claims (Mercari 500% ROI). |
| LCEmiRjPEtQ.md | youtube | Karpathy Software 3.0: autonomy slider (Cursor Cmd+K/L/I, Perplexity search/research/deep); apps (Cursor diffs, Perplexity citations); agents future but leashed; llms.txt, MCP, Gitingest. |
| TRjq7t2Ms5I.md | youtube | LlamaIndex RAG: naive→advanced (rerank, recursive ret., agentic multi-doc); evals (hit_rate/MRR/NDCG); spectrum to agentic (tools for QA/summ). |
| gemini-cli-your-open-source-ai-agent.md | web | Gemini CLI (Apache 2.0): terminal agent for coding/debug; tools (file ops, web search); MCP/exts; VS Code agent mode (multi-step, auto-recovery); free tier (1M ctx, 60/min). |
| google-gemini_gemini-cli.md | code | Gemini CLI repo: ReAct/plan-mode/subagents/model-routing/skills; tools (file-system/grep/shell/web/todo/browser); evals (concurrency, memory); MCP/sandbox. |
| introducing-chatgpt-agent-bridging-research-and-action.md | web | ChatGPT agent: tools (browser/terminal/API); benchmarks (Humanity’s Last Exam 41.6%, FrontierMath 27.4%, SpreadsheetBench 35.27%); use cases (travel/invest modeling). |
| introducing-perplexity-deep-research.md | web | Perplexity Deep Research: iterative search/read/reason (dozens searches, 2-4min reports); benchmarks (Humanity’s Last Exam 21.1%, SimpleQA 93.9%). |
| stop-building-ai-agents-here-s-what-you-should-build-instead.md | web | Anti-agents: workflows (chaining/parallel/routing/orchestrator-worker/evaluator-optimizer); CrewAI failures (70% ignore tools); hybrids for human-in-loop. |

### Tavily Exploitation Results
- Total exploitation rounds: 12
- Total queries run: 53 sources across 12 targeted queries
- Per-query yield quality: High overall (avg 4-5 relevant sources/query); strongest on Gemini CLI/Perplexity (direct impl details), moderate on case studies (anecdotal vs billion-dollar specifics), consistent depth on patterns/challenges.

## 2. Per-Section Coverage Analysis

### S1 — Introduction: The Critical Decision Every AI Engineer Faces
**Coverage: PARTIAL**
**What we have:** Golden sources like a-developer-s-guide... provide real-world stakes (Bain 2024: 95% firms use gen AI, 79% agents but 1% mature; Klarna agent=700 reps, BCG 45-50% cuts; costs workflows $500/mo vs agents $2k/multi $7.5k) and decision impact (dev time wasted, reliability/costs); kQxr-uOxw2o.md echoes hype vs reality (Devin overcomplicates, Anthropic agent fades); Tavily Q1 yields failures (Replit Rogue Agent DB wipe, HurumoAI fabricated reports) contrasting successes (Base44 $80M sale via workflows/agents). Exploitation 601-real-world... adds ROI (Mercari 500%, LUXGEN 30% cut). Maps to personal story/problem/why matters/walkthrough.  
**Remaining depth gaps:** Specific 2024-2025 billion-dollar startup successes/failures tied to arch choice (e.g., exact valuation impacts); quantified exec frustration costs; precise hybrid combo stats from leading firms.  
**Remaining breadth gaps:** Personal engineer anecdotes from non-promo sources; MVP rapid deployment metrics for workflows.

### S2 — Understanding the Spectrum: From Workflows to Agents
**Coverage: STRONG**
**What we have:** building-effective-agents.md defines workflows (predefined orchestration: chaining/routing/parallel/orchestrator-worker) vs agents (dynamic LLM loops/tools/memory); what-is-an-ai-agent.md details agent chars (adaptive/ReAct: reasoning/acting/observing/planning/memory/tools); kQxr-uOxw2o.md contrasts code-orchestrated workflows vs LLM-directed agents (System 1/2); exploring... adds ReAct agent example (SmolAgents tools); Tavily Q10 analogies (assembly line deterministic vs probabilistic agent loops, 95% acc decay in multi-agent); Q6 orchestration diff (fixed seq vs dynamic loops). Images/mermaid-ready from LangGraph/StateGraph in a-developer-s....  
**Remaining depth gaps:** Exact simple workflow/agent diagram sources (e.g., factory/human expert visuals); detailed orchestration layer code snippets for both.  
**Remaining breadth gaps:** Multimodal agent examples; non-ReAct agent types (e.g., Plan-and-Exec high-level tease).

### S3 — Choosing Your Path
**Coverage: STRONG**
**What we have:** a-developer-s-guide... excels with when-to-use (workflows: high-volume/reliability; agents: ambiguous/dynamic; hybrids); decision framework (5-pt score ≥6); examples (data extract/pipelines, research/debug); strengths/weaknesses (predictable costs vs variable/errors); Tavily Q9 regulated domains (finance: RAG/fine-tune for compliance/FinBEN; health: guardrails/oversight/HIPAA); Q4 autonomy slider (Cursor Cmd+K/L/I, Perplexity search/deep; Karpathy LCEmiRjPEtQ); stop-building-ai-agents... agent fails (CrewAI 70% tool ignore); mermaid-ready loops. Enterprise prefs (finance/health accuracy/lives).  
**Remaining depth gaps:** Notion/Slack/Zoom extract specifics; exact cost/latency variance numbers for agent calls; Cursor/Perplexity UI screenshots/details.  
**Remaining breadth gaps:** Repetitive tasks quantifiable benchmarks (e.g., emails/social ROI).

### S4 — Exploring Common Patterns
**Coverage: STRONG**
**What we have:** building-effective-agents.md core: chaining/routing/orchestrator-worker/evaluator-optimizer (mermaid-ready, code ex: marketing→translate); stop-building-ai-agents... diagrams/code (chaining asyncio.parallel, routing classify→handler, orch-worker classify→delegate, eval-opt loop score>0.8); Tavily Q7 eval-opt impls (Pydantic AI generator/fixer/eval loop, Anthropic notebook, Spring AI ChatClient, LangChain Gemini complaint classify/validate); Q11 orch-worker (LangChain Product Launch: gpt-4o plans→tech/market/risk workers→synth; Claude FlexibleOrchestrator XML tasks); ReAct components (tools=actions, short/long mem=RAM/DB); almost all agents use ReAct.  
**Remaining depth gaps:** Chaining/routing mermaid code specifics; ReAct mermaid dynamics (LLM-tool-mem loop).  
**Remaining breadth gaps:** None significant.

### S5 — Zooming In on Our Favorite Examples
**Coverage: STRONG**
**What we have:** Gemini Workspace workflow (Tavily Q8: Drive API→read/parse→chunk summary→key pts→store/display; Gemini 2.5 Pro 1M tokens, semantic idx); Gemini CLI agent (exploitation gemini-cli..., google-gemini...; Tavily Q2: ReAct loop—context (dir/tools/hist)→LLM reason→human validate→tools (grep/file/web/git/code exec/diff)→eval (run/compile)→loop; TypeScript OSS GitHub, VS Code mode); Perplexity Deep (exploitation introducing-perplexity...; Tavily Q3: orch decomp sub-Qs→parallel agents search/read→score/rank/summ→gap iter→report cites; 2-4min, Humanity’s Last Exam 21.1%); mermaid flows ready; hybrids (orchestrator-worker multi-agents). High-level 7yo expl.  
**Remaining depth gaps:** Exact Gemini Workspace mermaid (read→summ→extract→DB→UI); CLI tool ex (grep funcs, git commit); Perplexity closed-source assumptions validated.  
**Remaining breadth gaps:** Similar tools depth (Cursor/Windsurf/Claude/Warp).

### S6 — Conclusion: The Challenges of Every AI Engineer
**Coverage: PARTIAL**
**What we have:** a-developer-s... challenges (reliability/debug/costs/security); Tavily Q5 prod issues (non-det loops runaway tokens $0.15→prohibitive, debug archaeology, injection/poisoning, data silos); kQxr-uOxw2o (unpredictable 80% works/20% fails); stop-building... (hard eval/debug); exploitation sources (halluc 5-20%, token surge); good news (hybrids/evals future). Transition teases (next Lesson 3, future: structured out/chaining/routing/tools/ReAct/PlanExec/mem/RAG/etc high-level).  
**Remaining depth gaps:** Context limits specifics (coherence loss metrics); data integration pipelines (Slack/API/SQL ex); cost-perf trap numbers (thousands req/min).  
**Remaining breadth gaps:** Monitoring pipelines (Langsmith/Phoenix); security write perms ex (email delete).

## 3. Overall Gap Profile
- **Gap counts:** depth_gaps=15, breadth_gaps=8 (summed across all sections)
- **Weakest sections:** S1, S6
- **Strongest sections:** S2, S3, S4, S5
- **Gap character:** Depth gaps dominate in examples/challenges needing quantifiable metrics/code; breadth minimal, focused on visuals/complements; patterns/orchestration over-covered via gold/Tavily.
- **Query saturation:** Excellent—12 queries precisely target guideline gaps (e.g., Gemini/Perplexity specifics, regulated use, patterns), yielding 80%+ novel depth; diminishing returns on generics.
- **Key insight for exploration strategy:** Prioritize code repos/visuals for mermaid/diagrams (e.g., query Gemini CLI GitHub flows, Perplexity teardowns) and 2025 startup metrics to boost weak intros/conclusions.