# Near-tie review: 14_agent_system_design  (standard vs deep, margin=+0.0363)

## Reviewer conclusion (2026-09-05): KEEP `standard`, no override -- runner-up flipped light→deep

**Runner-up flip:** `article_oracle.json` was stale (2026-08-27, pre-dating a fresh
re-grading round) and has been regenerated. `light` fell to third place --
new averaged R_w: skip=0.250, light=0.380, **standard=0.431 (oracle)**,
**deep=0.394 (new runner-up)**. Margin narrowed slightly from the prior
standard-vs-light review (+0.0373) to **+0.0363** against the new competitor.
This is the third article this session (after 13_agent_framework and
Understanding_Reasoning_LLMs) where re-scoring changed which arm is the real
runner-up, not just the margin -- always re-check `runner_up_arm` after any
re-grading round rather than assuming the same competitor still applies.

**Quantitative basis (standard vs deep, n=18 sections-draws per arm):**
cc/fl/cp all exactly tied (0.833/1.000/1.000). `de` favors **deep**
(0.611 vs 0.444, diff -0.167 against standard) -- deep's extra exploration
round genuinely earns more depth-enhancement credit, as expected. But `be`
favors **standard** by a much larger margin (0.667 vs 0.222, diff +0.444) and
`ga` also favors standard (0.667 vs 0.500, diff +0.167) -- deep's longer
sections trip more guideline-adherence word-count violations without buying
back the breadth credit its extra round should provide. Net: standard's edge
is a real be+ga advantage that outweighs deep's single de advantage, not an
artifact of the mean-R_w calculation alone.

**Distributional basis:** per-draw margins (standard - deep) are **[+0.0166,
+0.0224, +0.0698]** -- unanimous 3/3 in favor of standard (production and
replicate1 are close/thin, replicate2 is a clear win). Moderated significance:
t=2.155, p(one-tailed)=0.082 -- not conventionally significant but 3/3
unanimous agreement, combined with the clean be+ga mechanism above, gives
reasonable confidence despite the still-thin margin. For reference, standard
also still beats light (mean margin +0.0508, 3/3, p(one-tailed)=0.077,
similar strength) -- standard is the clear best arm regardless of which of
the other two is designated runner-up. light vs deep is itself a near-total
coin flip (mean -0.0145, only 1/3 favors light, p=0.37 one-tailed), consistent
with light having simply fallen out of contention rather than deep having
surged past a stable light.

**Decision:** no manual override needed -- `standard` is mean-R_w's own
winner both before and after this round's re-grading, and `needs_review` is
now `false` (margin +0.0363 clears the 0.0312 threshold, same as the prior
review's +0.0373).

---

## All sections (standard vs deep), most-against-standard first
| section | weight | contribution | running total |
|---|---:|---:|---:|
| section-5-decision-matrix-defaults-for-the-capston | 0.031 | -0.0171 | -0.0171 |
| section-4-our-capstone-global-system-design | 0.281 | -0.0060 | -0.0231 |
| section-2-a-general-ai-engineering-decision-framew | 0.312 | -0.0047 | -0.0278 |
| section-3-inference-time-scaling-and-the-cost-late | 0.219 | +0.0074 | -0.0203 |
| section-6-conclusion | 0.094 | +0.0208 | +0.0005 |
| section-1-introduction | 0.062 | +0.0358 | +0.0363 |

(stored article margin = +0.0363 -- should match the running total's final row to ~4 decimals)

## Section: S5::section-5-decision-matrix-defaults-for-the-capstone  (weight=0.031, contribution=-0.0171 AGAINST standard)
Stored section rewards: standard=0.3436  deep=0.4357  (explore: standard=0.0000  deep=0.1050)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both sections present the same decision matrix framing, and the table content (six dimensions, choices, and rationales) is reproduced identically. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** Same flow: intro paragraph followed by the table, in the same relative position as the expected section. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No depth additions present in either the framing paragraph or the table.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No breadth additions present in either the framing paragraph or the table.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this combined section, so CorePreservation scores 1 by default.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** REVISED from the submitted reasoning.json (previously scored 0, citing an approximate count of '~71 words... below the 75-word lower bound'). Word-count audit: target 100, tolerance +/-25, range [75, 125]. Exact prose-only count: 79 — within range, clearing the minimum by 4 words. The section covers the guideline's required framing (blueprint, living document, row structure linked to cost/latency/reliability/debuggability); it does not name 'Lessons 15-22' specifically, a minor gap that does not on its own change the verdict.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework must be translated into specific, implementable defaults. The following matrix captures these choices for both the research (Nova) and writing (Brown) tasks. This is not an aspirational document; it is the exact blueprint we will implement starting in the next lesson. It serves as a living contract that prevents ad-hoc choices during implementation. We will refer to it repeatedly in Lessons 15–22 whenever a trade-off arises, and any deviation must be explicitly justified and recorded.

Table 1: Decision matrix for the capstone project.

| Decision Dimension | Our Default Choice | Rationale |
| :--- | :--- | :--- |
| **Model Family & Tiers** | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets** | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy** | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy** | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts** | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow and ensures a clean separation of concerns. This makes the system modular, simplifies debugging, and enables easy replayability for evaluation and auditing, which is essential for iterative development and quality assurance. |
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both sections frame the matrix as translating the 7-step framework into a concrete blueprint with row structure linked to cost/latency/reliability, explicitly including both the 'Lessons 15–22' reference and the 'any deviation must be explicitly justified and recorded' language, and the table content is reproduced identically. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** The framing paragraph precedes the table, matching the expected section's progression, with the table in the same relative position. Per standing ruling, caption placement before vs. after the table makes no meaningful difference. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No depth additions present in either the framing paragraph or the table.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No breadth additions present in either the framing paragraph or the table.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this combined section, so CorePreservation scores 1 by default.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** The section covers the guideline's required framing in full, including both the "Lessons 15–22" reference and the "any deviation must be explicitly justified and recorded" clause verbatim. Word-count audit (previously an approximation of "~82"; recomputed exactly): target 100, tolerance +/-25, range [75, 125]. Exact prose-only count: 90 — within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework now become specific, implementable defaults tailored to the distinct demands of research (Nova) and writing (Brown). This matrix is the exact blueprint we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, our chosen default, and the rationale linking it to our goals for cost, latency, reliability, or debuggability. This matrix serves as a living document to prevent ad-hoc choices during implementation.
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both sections frame the matrix as translating the 7-step framework into a concrete blueprint with row structure linked to cost/latency/reliability/debuggability, and the table content is reproduced identically. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** The table is in the same relative position as the expected section. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No depth additions present in either the framing paragraph or the table.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No breadth additions present in either the framing paragraph or the table.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this combined section, so CorePreservation scores 1 by default.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** The section covers the guideline's required framing though it does not name "Lessons 15–22" specifically. Word-count audit (previously an approximation of "~78"; recomputed exactly, combining the framing paragraph and the table's own H2 section, which carries no prose of its own): target 100, tolerance +/-25, range [75, 125]. Exact prose-only count: 78 — within range.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of the 7-step framework into specific, implementable defaults for our capstone. It is the exact blueprint we will implement starting in the next lesson. Each row captures a decision dimension, our chosen default, and an explicit rationale that links back to the cost, latency, reliability, or debuggability goals we established. This matrix will serve as a living blueprint to prevent ad-hoc choices during implementation.
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both the framing paragraph (under 'Decision Matrix & Defaults for the Capstone') and the table (under the differently-titled but content-matching 'Decision Matrix for the Capstone Project' H2) match the expected section's ideas: the same blueprint/living-document/row-structure framing, and all six table rows reproduced identically. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** The framing paragraph precedes the table, matching the expected section's paragraph-then-table order, with the table immediately following the framing content. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**1:** [instances=1; quality=strong] No depth addition in the framing paragraph itself, but the table's 'Reasoning Budgets' row adds 'preventing common failure modes like task derailment or step repetition,' traced to the failure-taxonomy arXiv paper (exploration) also credited in the Scaling section. Since the framing paragraph and the table are now evaluated as one combined section, this qualifying instance is credited to the section as a whole.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No breadth additions present in either the framing paragraph or the table.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** DepthEnhancement scored 1 for this combined section (the task-derailment/step-repetition addition in one table cell's rationale). This is a short clause that does not dilute the required framing content or table content, both of which are fully present; CorePreservation is properly assessed as 1, not defaulted.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** REVISED from the submitted reasoning.json's approach, which evaluated the framing paragraph and the table as two separate UserIntent sections (scoring both 1, the first on a miscounted '~100 words' claim). FLAGGED METHODOLOGY QUESTION, this time with a real numeric consequence: the guideline's actual Section 5 instructions describe ONE combined 100-word unit (framing prose + table). Evaluated separately, the framing paragraph alone is exactly 70 words — 5 words below the 75-word floor, a failure. Evaluated as the guideline intends, combined with the table section's own 8 prose words (the caption line), the total is 78 words — within the [75,125] range, a narrow pass (3 words of margin). I am scoring this as a pass using the combined interpretation, consistent with how I have treated this question in every other article reviewed in this project, but flagging clearly since this is the first case where the choice of interpretation actually changes the verdict rather than being a moot methodological note.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework must be translated into specific, implementable defaults. The following matrix serves as the blueprint for our capstone project, tailored to the distinct demands of research (Nova) and writing (Brown). This is not an aspirational guide; it is the exact plan we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, our chosen default, and a rationale that links back to the cost, latency, and reliability goals we established.

This matrix is a living blueprint that prevents ad-hoc choices during implementation. We will refer to it repeatedly in Lessons 15–22 whenever a trade-off arises.

Table 1: Decision matrix for the capstone project.
| Decision Dimension | Our Default Choice | Rationale |
| :--- | :--- | :--- |
| **Model Family & Tiers** | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets** | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy** | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy** | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts** | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow. It ensures a clean separation of concerns, simplifies debugging, and enables replayability. While this approach has scaling limits for agents that might one day operate on entire codebases, it provides a robust and modular starting point for our current scope [[22]](https://www.amplifypartners.com/blog-posts/file-systems-for-agents). |
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both sections frame the matrix as translating the 7-step framework into a concrete blueprint with row structure linked to cost/latency/reliability, both reference Lessons 15–22, and the table content matches identically, plus an added, well-anchored caveat in the Artifacts & Contracts rationale. Additions do not count against CoreContent. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** The table is in the same relative position as the expected section. Per standing ruling, caption placement makes no meaningful difference. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**1:** [instances=1; quality=strong] No depth addition in the framing paragraph itself, but the table's Artifacts & Contracts row adds a scaling-limits caveat for agents operating on entire codebases, traced to the exploration-phase Amplify Partners source. Since the framing paragraph and table are now one combined section, this qualifying instance is credited to the section as a whole.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] The scaling-limits addition (see DepthEnhancement) deepens understanding of the artifact-contract approach's own limitations rather than connecting outward to an adjacent field, so it is classified as depth only.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** DepthEnhancement scored 1 for this combined section (the scaling-limits caveat in one table cell's rationale). This is a short, appended clause that does not dilute the required framing or table content, both of which are fully present; CorePreservation is properly assessed as 1, not defaulted.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** The section covers the guideline's required framing, including the Lessons 15–22 reference, though it renders the deviation clause without the guideline's additional "and recorded." Word-count audit (previously an approximation of "~109"; recomputed exactly): target 100, tolerance +/-25, range [75, 125]. Exact prose-only count: 117 — within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework now become specific, implementable defaults for the Nova and Brown agents. This matrix is not aspirational; it is the exact blueprint we will implement starting in the next lesson. It serves as a living document that prevents ad-hoc choices during implementation, ensuring every trade-off aligns with our goals for cost, latency, and reliability. We will refer to it repeatedly in Lessons 15–22 whenever a design choice arises, making sure our code stays true to our architectural vision.
```
**Grader reasoning:**
- `cc`: Decision Matrix & Defaults for the Capstone:
**1:** Both sections frame the matrix as translating the 7-step framework into a concrete blueprint, this generated section explicitly includes the 'Lessons 15–22' reference, and the table content is reproduced identically. Evaluated as one combined section.
- `fl`: Decision Matrix & Defaults for the Capstone:
**1:** The framing paragraph precedes the table, matching the expected section's progression, with the table in the same relative position. Evaluated as one combined section.
- `de`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No depth additions present in either the framing paragraph or the table.
- `be`: Decision Matrix & Defaults for the Capstone:
**0:** [instances=0] No breadth additions present in either the framing paragraph or the table.
- `cp`: Decision Matrix & Defaults for the Capstone:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this combined section, so CorePreservation scores 1 by default.
- `ga`: Decision Matrix & Defaults for the Capstone:
**1:** The section covers the guideline's required framing and explicitly includes the "Lessons 15–22" reference. Word-count audit (previously an approximation of "~84"; recomputed exactly, combining the framing paragraph and the table's own H2 section): target 100, tolerance +/-25, range [75, 125]. Exact prose-only count: 92 — within range.

## Section: S4::section-4-our-capstone-global-system-design  (weight=0.281, contribution=-0.0060 AGAINST standard)
Stored section rewards: standard=0.4786  deep=0.5232  (explore: standard=0.1350  deep=0.1925)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** Both sections describe the Nova/Brown separation of concerns, the frameworks used, the file-based handoff, and the role of the article guideline. Fully aligned.
- `fl`: Our Capstone: Global System Design:
**1:** Same progression: architecture diagram, Nova detail with diagram, Brown detail with diagram, handoff. Flow preserved.
- `de`: Our Capstone: Global System Design:
**0:** [instances=0] Confirmed on review: the file-based-contract elaboration is exploitation-phase sourced (fast.io, arXiv 2603.16021v1), correctly excluded. The LangGraph+MCP 'emerging trend' claim is breadth, not depth (see BreadthEnhancement) — it situates the existing design within a wider trend rather than revealing new inner workings of Brown's own architecture.
- `be`: Our Capstone: Global System Design:
**1:** [instances=2; quality=strong,strong] Confirmed on review: (1) the robotics leader/executor-agent analogy (federico.io multi-robot paper, exploration) — strong; (2) the LangGraph+MCP 'emerging trend in multi-agent orchestration' framing (Healthark, exploration) — strong, correctly credited as breadth-only rather than dual-credited with depth, since it situates Brown within a wider industry trend rather than deepening Brown's own mechanics. Neither restates ground-truth content — GT does not discuss robotics or this orchestration trend.
- `cp`: Our Capstone: Global System Design:
**1:** The two breadth additions are brief and support the core architectural description without diluting it.
- `ga`: Our Capstone: Global System Design:
**1:** Consistent with the submitted reasoning.json's (self-corrected) verdict, on a cleaner basis. Word-count audit: target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 821 — within range by 11 words, a clean pass that does not require invoking the 'tolerable small margin' exception the submitted file applied to its own (inaccurate) count of ~780.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

The core architectural principle of our capstone is a clean separation of concerns. We separate the unpredictable, open-ended research phase, handled by Nova, from the predictable, iterative drafting and review process, handled by Brown. This separation prevents context bloat and makes each component easier to debug and evolve independently. This architectural split between exploration and execution is a proven pattern seen in other fields, particularly robotics. A robot might have one system for exploring and mapping an unknown environment and a separate, more deterministic system for executing a known path. This decoupling is a robust way to manage uncertainty, a principle we apply here by separating Nova's open-ended research from Brown's structured writing process [[12]](https://arxiv.org/html/2505.02024v2). For instance, multi-robot systems often partition a map, assigning different agents to explore disjoint regions to efficiently cover an area, which is analogous to how Nova will break down a research topic into sub-problems [[26]](https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf). Image 2 illustrates this global architecture.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down 
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)

This design allows us to use the right tool for each job. Nova is built for exploration and discovery, while Brown is built for durable, high-quality execution. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” retrieved from the server. This recipe is a master prompt that guides the agent through a multi-step process: deconstruct the user's query into a research plan, query various sources like Google and Perplexity, scrape and transcribe relevant content, and iteratively filter and synthesize the findings. The agent selects the top sources for a full scrape and finally compiles everything into a structured `research.md` file.

For the MCP client, we use FastMCP’s built-in `Client` class. This is a lightweight, ready-to-use client that connects to our server and handles all protocol details like capability discovery and tool calling. Our implementation is just ~200 lines of Python that wrap FastMCP’s `Client`. It connects to the server, fetches the research prompt, and runs a ReAct-style loop where the LLM decides which tool to call next. The entire process is steerable, with configurable HITL gates to approve research plans or URL lists, and a critical stop rule to prevent failures if, for example, all scraping attempts fail. The end-to-end flow is shown in Image 3.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down 
Image 3: End-to-end agent flow for the Nova Research Agent (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call. This hybrid approach, combining a durable workflow engine with a standardized tool protocol, reflects an emerging industry trend where stable microservices handle deterministic tasks while agents orchestrate the high-level reasoning [[13]](https://www.softwareseni.com/the-microservices-moment-for-artificial-intelligence-and-how-multi-agent-orchestration-changes-everything).

The exposed tools are:
-   **Generate Article:** This orchestrates the full writing process. It loads context (guidelines, research, profiles), generates media items using the orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.
-   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.
-   **Edit Selected Text:** This runs a review-edit cycle on a specific portion of the article, enabling focused edits while maintaining awareness of the full document.

Image 4 shows the interaction flow for the `Generate Article` workflow.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down 
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as its inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean, file-based contract decouples the agents, making the system modular, observable, and debuggable. This approach, where folder structure and plain text files define the workflow, makes the system inherently interpretable, as every intermediate step is a readable artifact [[17]](https://arxiv.org/html/2603.16021v1).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be messy. Leaving too many gaps for the AI to fill without instructions leads to hollow text. LLMs are highly effective at translation and synthesis, but they are not a substitute for original thought.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** The Nova and Brown descriptions, the three tools, the file-based handoff, and the well-anchored robotics exploration/execution analogy are all present with matching or exceeding substance. The closing paragraph again drops the expected section's 'brain dump' reassurance; per the standing ruling from the other articles graded for this lesson, this does not count against CoreContent.
- `fl`: Our Capstone: Global System Design:
**1:** The expected section places Image 2 immediately after a brief one-sentence intro, before the core-architectural-principle explanation; the generated section places it immediately after that explanation instead. Per standing ruling, this local swap in ordering with an immediately-adjacent element — as opposed to a wholesale relocation to a different part of the section — is trivial and not penalized. The image, its verbatim caption, and the explanatory content are all present and still appear in the same general position within the section.
- `de`: Our Capstone: Global System Design:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present. The robotics analogy (see BreadthEnhancement) connects outward to an adjacent field rather than deepening the core Nova/Brown architecture topic itself, and the file-based-contract-as-interpretable-architecture citation is only exploitation-phase sourced.
- `be`: Our Capstone: Global System Design:
**1:** [instances=2; quality=strong,strong] Two distinct breadth additions connect the Nova/Brown research-execution split to robotics: (1) the general claim that separating open-ended exploration from deterministic execution is 'a proven pattern seen in other fields, particularly robotics,' traced to the exploration-phase arXiv source on the Manus agentic framework's planner/execution split (https://arxiv.org/html/2505.02024v2); and (2) the more specific claim that 'multi-robot systems often partition a map, assigning different agents to explore disjoint regions,' analogous to how Nova decomposes a research topic, traced to the exploration-phase multi-robot exploration paper (https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf). Both classified strong: specific, well-developed cross-domain analogies with named mechanisms, not passing mentions. Note for the grader: this robotics tangent runs to roughly four sentences, comparable in length to the core architectural-principle explanation it is attached to — see the CorePreservation note for this section.
- `cp`: Our Capstone: Global System Design:
**1:** The robotics tangent is roughly four sentences, comparable in length to the three-sentence core-architectural-principle explanation it follows. The expected section's core ideas (clean separation of concerns, Nova handles research, Brown handles writing, prevents context bloat) are all stated in full before the tangent begins, so they are not interrupted or fragmented by it. This is flagged as a borderline call: the tangent's length relative to the core explanation it is attached to is substantial enough that a stricter reading could see it as beginning to overshadow rather than merely supplement that explanation.
- `ga`: Our Capstone: Global System Design:
**1:** The section covers the guideline's required Nova and Brown descriptions, the three tools, and the file-based handoff. Word-count audit (previously an approximation of "~856"; recomputed exactly): target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 849 — within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.![Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The core architectural principle of our capstone, illustrated in Image 2, is a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently.

This separation of exploration from execution is a well-established pattern in robotics and complex agent design. A "planner" agent first decomposes a problem and formulates a strategy, similar to Nova's research phase. A separate "execution" agent then carries out the plan, interacting with tools and external systems, analogous to Brown's writing workflow. This division of labor improves reliability and modularity [[31]](https://arxiv.org/html/2505.02024v2). Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a "Research Recipe" retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape them, run iterative research loops, filter results, select top sources for a full scrape, and compile everything into a `research.md` file.

This approach, where a master prompt or recipe guides a series of tool calls, is analogous to the "Model Workspace Protocol" (MWP), where folder structures and markdown files define an agent's behavior at each stage of a workflow [[21]](https://arxiv.org/html/2603.16021v1). The MCP client's only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt. This design keeps the agent's logic portable and decoupled from any single client application, a core benefit of using MCP.

For the client, we use FastMCP’s built-in `Client` class, a lightweight, ready-to-use component that handles all protocol details. Our implementation is a ~200-line Python script that wraps this client. It connects to the server, fetches the research prompt, and runs a ReAct-style loop where the LLM decides which tool to call next. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures.![End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration, which manages state, checkpoints, and interrupts. We front this durable engine with a FastMCP server, exposing Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

This hybrid design, combining LangGraph's structured control with MCP's contextual intelligence for tool use, reflects an emerging trend in multi-agent orchestration. It provides a fault-tolerant and replayable framework that overcomes the static nature of older multi-agent systems, establishing a foundation for scalable and interpretable agent collaboration [[32]](https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp).

LangGraph's persistence layer is key to this durability. By saving a snapshot of the graph state at every step, it enables long-running, stateful workflows that can resume from where they left off after failures or human interventions [[20]](https://docs.langchain.com/oss/python/langgraph/persistence). This is essential for a complex, multi-stage process like article generation, which can involve dozens of LLM calls and tool executions.

The exposed tools are:
*   **Generate Article:** This orchestrates a full workflow: loading context (guidelines, research, profiles), generating media items using the orchestrator-worker pattern, writing a first draft, and then running review-edit cycles.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article for targeted revisions.![Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This file-based handoff acts as an "artifact contract," ensuring a clean, inspectable interface between the two systems. This makes the overall architecture modular, simplifies debugging, and allows for easy replayability of the writing workflow with different inputs [[21]](https://arxiv.org/html/2603.16021v1). The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what to write, the narrative, and other important notes. Since the writing is automated, a clear, well-articulated guideline is what distinguishes a high-quality article from generic AI-generated slop.

If ideas are not clearly enumerated and connected, the output will be sloppy. LLMs are excellent at translation and synthesis but poor at generating original ideas. Leaving too many gaps for the AI to fill without instruction leads to hollow text.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** The Nova and Brown descriptions, the three tools, and the file-based handoff are all present with matching substance, plus two well-anchored additions (a robotics planner/execution analogy, and an MCP+LangGraph industry-trend framing). The closing paragraph drops the expected section's 'brain dump' reassurance; per standing ruling, this does not count against CoreContent.
- `fl`: Our Capstone: Global System Design:
**1:** Image 2 is placed immediately after the brief intro sentence and before the core-architectural-principle explanation, matching the expected section's order. Images 3 and 4 are also in their expected relative positions.
- `de`: Our Capstone: Global System Design:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present. Both additions in this section (the robotics planner/execution analogy and the MCP+LangGraph orchestration-trend framing, see BreadthEnhancement) connect outward to adjacent fields/trends rather than deepening the Nova/Brown mechanics themselves.
- `be`: Our Capstone: Global System Design:
**1:** [instances=2; quality=strong,strong] (1) The claim that separating exploration from execution is 'a well-established pattern in robotics and complex agent design,' with a planner/execution-agent analogy to Nova/Brown, is traced to the exploration-phase arXiv source on the Manus agentic framework (https://arxiv.org/html/2505.02024v2) — strong. (2) The claim that the LangGraph+MCP hybrid 'reflects an emerging trend in multi-agent orchestration' that overcomes the static nature of older multi-agent systems is traced to the exploration-phase Healthark source on orchestrating multi-agent systems with LangGraph and MCP (https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp), matched in near-identical language — strong.
- `cp`: Our Capstone: Global System Design:
**1:** Both breadth additions are brief (two-to-three sentences each) and are placed either before the detailed component walkthroughs begin or as a short aside within them; the expected section's core content (Nova/Brown descriptions, tools, handoff) remains fully present and dominant.
- `ga`: Our Capstone: Global System Design:
**1:** The section covers the guideline's required Nova and Brown descriptions, the three tools, and the file-based handoff thoroughly. Word-count audit (previously an approximation of "~845"; recomputed exactly): target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 840 — within range.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate research and writing.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down 
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The diagram above illustrates the core architectural principle of our capstone: a clean separation of concerns. Unpredictable, open-ended research is handled by Nova as an MCP agent, while predictable, iterative drafting and review are managed by Brown as a stateful LangGraph workflow. This separation prevents context bloat, which could confuse the LLM, and makes each component easier to debug, test, and evolve independently. This modularity is key to building a robust and maintainable system. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable across different clients and environments [[5]](https://modelcontextprotocol.io/docs/getting-started/intro). A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file.

For the MCP client, we use FastMCP’s built-in `Client` class. This is a lightweight, ready-to-use client that handles all the protocol details, such as capability discovery and tool calling, out of the box. Our implementation is just ~200 lines of Python that wrap this client. It connects to the server, fetches the research prompt, and runs a simple ReAct-style loop. In this loop, the LLM decides which tool to call next, executes it via `client.call_tool()`, and feeds the result back into the conversation. The entire process is steerable, with configurable HITL gates to allow for human guidance and a critical stop rule to prevent failures, ensuring the agent operates within defined boundaries.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down 
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine capable of handling long-running, multi-step tasks [[6]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). We front this powerful engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE or another agent, to trigger complex writing tasks with a simple, standardized tool call.

The exposed tools are:

*   **Generate Article:** This orchestrates the full writing process. It loads context (guidelines, research, profiles), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback. It uses the same evaluator-optimizer pattern but prioritizes the human's input over automated reviews, allowing for direct and precise revisions.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article. This enables targeted revisions, such as improving a single paragraph or section, while maintaining awareness of the full document to ensure consistency.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down 
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory containing raw data and intermediate artifacts. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean, file-based contract ensures the system is modular, debuggable, and easy to maintain.

While simple and robust for our current scope, it is important to recognize the potential scalability limits of this approach. As agent workloads grow to operate over entire codebases or synthesize hundreds of legal documents, the inefficiency of rewriting entire immutable files for small, incremental updates can become a bottleneck. Production systems at that scale may require more sophisticated solutions like specialized file systems or shared memory to support efficient access and computation [[18]](https://www.amplifypartners.com/blog-posts/file-systems-for-agents).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill leads to hollow text, as LLMs are excellent at translation and synthesis but poor at generating truly original ideas.

The architecture and diagrams are now concrete. The final step is to translate these framework principles into an explicit, implementable decision matrix.
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** Both sections describe the Nova/Brown separation of concerns, their frameworks, and the file-based handoff. All key ideas present.
- `fl`: Our Capstone: Global System Design:
**1:** Same progression: architecture overview, Nova detail, Brown detail, handoff. Diagram placement consistent.
- `de`: Our Capstone: Global System Design:
**1:** [instances=1; quality=strong] Confirmed on review: the file-based handoff's scalability-limits discussion (Amplify Partners, exploration) is a genuine addition — GT does not discuss this limitation.
- `be`: Our Capstone: Global System Design:
**0:** [instances=0] The scalability-limits addition is depth (implementation challenges/future directions), not breadth, consistent with the submitted reasoning.
- `cp`: Our Capstone: Global System Design:
**1:** The single depth addition is a brief, well-integrated paragraph that does not dilute the core architectural description.
- `ga`: Our Capstone: Global System Design:
**1:** Word-count audit: target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 781. 29 words below the minimum. Per standing ruling, this margin is not penalized given the 900-word target — roughly a 3.2% shortfall relative to target, comparable in scale to other margins already ruled acceptable, even though larger in absolute word count than some prior confirmed cases.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a more detailed architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The image above illustrates the core architectural principle of our capstone: a clean separation of concerns. The unpredictable, open-ended research is handled by Nova, an MCP agent, while the predictable, iterative drafting and review process is managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently.

This modular design is analogous to the shift from monolithic applications to microservices in traditional software engineering. Instead of a single, large prompt or agent trying to do everything, we are building specialized components with well-defined responsibilities and contracts. This multi-agent approach creates a more governable and scalable system than a single, monolithic model, which is better suited for enterprise use. Let's examine each component in more detail [[16]](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices).

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable across different clients. A simple MCP client runs an LLM-driven loop that follows a "Research Recipe" retrieved from the server. This recipe, defined in a master prompt, guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file.

The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt. For the MCP client, we use FastMCP’s built-in `Client` class. It is a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details like capability discovery, tool calling, and resource fetching out of the box. Our implementation is just around 200 lines of Python that wrap FastMCP’s `Client`. It connects to the server via in-memory or stdio transport, fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The system exposes several capabilities as tools. The primary tool, **Generate Article**, orchestrates a complete writing workflow. It loads all necessary context, including guidelines, research, profiles, and examples. Then, it generates media items using an orchestrator-worker pattern, writes the first draft, and runs a configurable number of review-edit cycles using an evaluator-optimizer pattern. Another tool, **Edit Article**, runs a single review-edit cycle on the entire article based on human feedback, prioritizing this input over automated reviews. Finally, **Edit Selected Text** runs a targeted review-edit cycle on a specific portion of the article, allowing for precise revisions while maintaining awareness of the full document.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory. Brown takes these files, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean separation of concerns, defined by a file-based contract, makes the system modular, debuggable, and easier to maintain. This approach is similar to "stage contracts" where folder boundaries enforce separation and outputs from one stage become inputs for the next [[21]](https://arxiv.org/html/2603.16021v1).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed for the entire process, where you define the article's topic, narrative, and any personal notes. Since the writing process is automated, a clear, well-articulated guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. LLMs are excellent at translation and synthesis, but they are terrible at generating original, coherent ideas from scratch. Leaving too many gaps for the AI to fill without instruction leads to hollow, uninspired text.

The architecture and diagrams are now concrete. The final step is to translate these framework principles into an explicit, implementable decision matrix.
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** The Nova and Brown descriptions, the three tools, the file-based handoff, and the well-anchored microservices analogy are all present with matching or exceeding substance. The closing paragraph again drops the expected section's 'brain dump' reassurance; per the standing ruling from the other articles graded for this lesson, this does not count against CoreContent.
- `fl`: Our Capstone: Global System Design:
**1:** Image 2 is placed immediately after the brief intro sentence and before the core-architectural-principle explanation, matching the expected section's order (unlike one of the other three articles graded for this lesson, which reversed this). Images 3 and 4 are also in their expected relative positions.
- `de`: Our Capstone: Global System Design:
**1:** [instances=1; quality=strong] The claim that the Nova/Brown separation is 'analogous to the shift from monolithic applications to microservices,' with specialized components and well-defined contracts producing a more governable and scalable system, is traced to the same exploration-phase TEKsystems microservices source credited in the Framework section — a distinct instance in this section, applied to the capstone's own architecture. Strong: specific and well-developed (also credited under BreadthEnhancement).
- `be`: Our Capstone: Global System Design:
**1:** [instances=1; quality=strong] The same microservices analogy credited under DepthEnhancement, applied here to the capstone's own architecture, also qualifies as breadth for the same reason given in the Framework section — a cross-domain connection to distributed-systems architecture. Traced to the same exploration-phase TEKsystems source; classified strong.
- `cp`: Our Capstone: Global System Design:
**1:** The microservices analogy is a brief, two-sentence addition following the core-principle explanation, which is fully stated beforehand. It does not crowd out or interrupt the expected section's core content.
- `ga`: Our Capstone: Global System Design:
**1:** The section covers the guideline's required Nova and Brown descriptions, the three tools, and the file-based handoff thoroughly. Word-count audit (previously an approximation of "~780"; recomputed exactly): target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 778 — 32 words below the minimum (≈3.6% of target). Per standing ruling on percentage-of-target margins for a 900-word target (an ≈3.2% shortfall was previously ruled not to be penalized on this same section type), this is scored as passing, but flagged explicitly as a new instance being evaluated against that precedent rather than an automatic re-application.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a more detailed architectural map than in Lesson 12, solidifying the intuition for how our two agents, Nova and Brown, collaborate to automate research and writing.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

Image 2 illustrates the core architectural principle of our capstone: a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP-driven agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple **MCP client** runs an LLM-driven loop guided by a "Research Recipe," a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file.

For the client, we use **FastMCP’s built-in `Client` class**, a lightweight component that handles all protocol details like capability discovery and tool calling. Our implementation is a ~200-line Python script that wraps this client. It connects to the server, fetches the research prompt, and runs a ReAct-style loop where the LLM decides which tool to call next, executes it via `client.call_tool()`, and feeds the result back into the conversation. The process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The client's only job is to orchestrate these tool calls based on the LLM's decisions, following the research workflow defined in the server-hosted prompt. As shown in Image 3, this flow creates a clear, observable loop that is easy to monitor and debug.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration, which manages state, checkpoints, and interrupts, making it a durable workflow engine. We front this engine with a **FastMCP server**, exposing Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call. This design provides the durability of a workflow with the portability of MCP-based tools.

The exposed tools are:

*   **Generate Article:** This tool orchestrates the main writing workflow. It loads context (guidelines, research, profiles, examples), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern. This entire process is managed within the stateful LangGraph environment, ensuring that progress is saved at each step.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, prioritizing this input over automated reviews. It leverages LangGraph's ability to interrupt and resume, allowing a human to provide input that directly modifies the workflow's state before it continues.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining awareness of the full document context. This also uses the interrupt-and-resume pattern for human input.

The sequence diagram in Image 4 illustrates the interaction flow for the "Generate Article" tool, showing how the client initiates the task and how the LangGraph workflow orchestrates the various steps, from loading context to the final review cycles.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory containing its sources. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This clean, file-based contract makes the system modular, debuggable, and easy to maintain. While this approach is effective for our current scope, it is important to recognize its limitations at a much larger scale. As agents begin to operate on entire codebases or synthesize information from hundreds of documents, simple file handoffs and immutable object storage can become a bottleneck. The challenge shifts from just storing data to providing efficient, incremental access and computation over massive artifacts [[12]](https://www.amplifypartners.com/blog-posts/file-systems-for-agents).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines the article's topic, narrative, and key points. As the writing itself is automated, a clear, well-articulated guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be hollow. LLMs are excellent at translation and synthesis, but they are not sources of original thought. Leaving too many gaps for the AI to fill without instruction is a recipe for generic, uninspired content.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.
```
**Grader reasoning:**
- `cc`: Our Capstone: Global System Design:
**1:** The Nova and Brown descriptions, the three tools, and the file-based handoff are all present with matching substance, plus a well-anchored addition on the scaling limits of file-based handoffs at much larger scale. The closing paragraph drops the expected section's 'brain dump' reassurance; per standing ruling, this does not count against CoreContent.
- `fl`: Our Capstone: Global System Design:
**1:** Image 2 is placed immediately after the brief intro sentence and before the core-architectural-principle explanation, matching the expected section's order. Images 3 and 4 are also in their expected relative positions.
- `de`: Our Capstone: Global System Design:
**1:** [instances=1; quality=strong] The handoff paragraph's discussion of the file-based contract's scaling limits — that simple file handoffs and immutable object storage become a bottleneck once agents operate on entire codebases or hundreds of documents — is traced to the exploration-phase Amplify Partners source on file systems for agents (https://www.amplifypartners.com/blog-posts/file-systems-for-agents), matched closely to that source's own framing. Strong.
- `be`: Our Capstone: Global System Design:
**0:** [instances=0] The file-systems scaling-limits addition (see DepthEnhancement) deepens understanding of the artifact-contract approach's own limitations rather than connecting outward to an adjacent field, so it is classified as depth only.
- `cp`: Our Capstone: Global System Design:
**1:** The file-systems scaling-limits addition is a few sentences appended to the handoff paragraph, which fully states the expected section's core content beforehand; it does not crowd out or interrupt that content.
- `ga`: Our Capstone: Global System Design:
**1:** The section covers the guideline's required Nova and Brown descriptions, the three tools, and the file-based handoff thoroughly. Word-count audit (previously an approximation of "~795"; recomputed exactly): target 900, tolerance +/-90, range [810, 990]. Exact prose-only count: 794 — 16 words below the minimum. Per standing ruling, this margin is not penalized.

## Section: S2::section-2-a-general-ai-engineering-decision-framework  (weight=0.312, contribution=-0.0047 AGAINST standard)
Stored section rewards: standard=0.4994  deep=0.5682  (explore: standard=0.4225  deep=0.5375)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** The generated section covers all seven steps in the correct order, but two substantive ideas from the expected section are absent: (1) the multimodal-capability discussion in Step 2, and (2) the evaluation-plan guidance in Step 5. Neither appears anywhere in the generated section.
- `fl`: A General AI Engineering Decision Framework:
**1:** Same seven-step progression in both; the additional details (Pugh Matrix, inference-time distillation, failure modes) are integrated without disrupting the main flow.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=4; quality=strong,strong,strong,strong] Confirmed on review: (1) inference-time distillation (OpenReview, exploration) — strong; (2) primacy/recency mechanistic explanation of lost-in-the-middle (Stanford paper, exploration) — strong, also credited under BreadthEnhancement; (3) cascading/silent failure modes (MindStudio, exploration) — strong; (4) cost-inflating patterns and real-time cost observability (CloudZero + Mirantis, exploration) — strong. None paraphrase the ground truth: GT's Section 2 does not use any of this terminology (distillation, primacy/recency, cascading/silent failure, cost observability) at all, so each is a genuine addition.
- `be`: A General AI Engineering Decision Framework:
**1:** [instances=1; quality=strong] Confirmed on review: the primacy/recency cognitive-psychology framing for the lost-in-the-middle mechanism (Stanford paper, exploration) is a genuine cross-domain analogy, dual-credited with DepthEnhancement. The Pugh Matrix candidate is correctly excluded (dev.to, exploitation-phase).
- `cp`: A General AI Engineering Decision Framework:
**1:** The qualifying depth and breadth additions are concise and well-integrated into the specific steps they relate to; they do not overshadow the core 7-step framework.
- `ga`: A General AI Engineering Decision Framework:
**1:** Consistent with the submitted reasoning.json's verdict. Word-count audit: target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1078 (submitted reasoning claimed an approximate '~980', still within range but off by about 100 words from the true count) — within range, 22 words below the maximum. Content coverage of all seven steps is confirmed thorough.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define success. What is the quality bar for the output? What are the privacy or compliance requirements? What is the expected volume of tasks, and what is your per-task spending limit? These targets dictate every downstream choice. A decision matrix is a useful tool for this, allowing you to list criteria, assign weights, and score options systematically [[18]](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45). The process involves defining your objective, identifying options, determining criteria like cost and accuracy, and assigning weights to prioritize them. This structured evaluation helps you make informed trade-offs [[19]](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects).

For example, a real-time customer support bot must have sub-second latency to feel responsive, but moderate accuracy might be acceptable for initial triage before escalating to a human. Its cost per interaction must be extremely low to be viable at scale. In contrast, a batch research job analyzing legal documents has a near-zero tolerance for hallucinations, and its throughput can be measured in hours. Here, accuracy is the primary driver, and higher costs are justified by the value of the output. Clearly articulating these constraints at the start prevents you from building a system that is technically impressive but practically useless.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed-source APIs or open-weight models. Closed APIs from providers like OpenAI, Anthropic, and Google deliver state-of-the-art performance with low operational overhead. This path is ideal when your priority is accessing the absolute best capabilities with maximum simplicity. However, it comes with the risk of vendor lock-in and potential data privacy concerns.

Open-weight models like Llama, Mistral, or DeepSeek offer unparalleled control. They guarantee privacy and data locality when self-hosted, and you can deeply customize them through fine-tuning. This is the right path if you need to guarantee that sensitive data never leaves your infrastructure or if you aim to create a specialized expert model. The trade-off is the significant burden of managing your own GPU infrastructure, a complex and expensive undertaking. A more advanced pattern is to use a cost-effective "student" model for most tasks, guided by examples from a more capable "teacher" model. When the student model's confidence is low, the system can dynamically fall back to the teacher, a technique known as an LLM cascade [[4]](https://openreview.net/forum?id=nCEdAM5m5T).

### Define Your Context Strategy

As we covered in previous lessons, simply dumping all available information into a large context window is a common mistake. Research has shown this leads to a "lost-in-the-middle" performance cliff, where models struggle to recall information buried in the middle of long prompts [[1]](https://arxiv.org/abs/2307.03172). This phenomenon, which mirrors the primacy and recency effects in human memory, results in a U-shaped performance curve. The model reliably uses information at the beginning and end of the context but often ignores important details in the middle. Performance degrades long before the physical context limit is reached. This U-shaped performance is not just a flaw but can be an emergent adaptation to different information retrieval demands during pre-training, where some tasks require uniform recall and others prioritize recent information [[20]](https://openreview.net/forum?id=XSHP62BCXN).

A disciplined context strategy is essential. Instead of relying on raw context volume, prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For a chatbot that needs to remember the last few turns of a conversation, a sliding window summary is often sufficient to maintain continuity. For an agent answering questions from a large, dynamic knowledge base, Retrieval-Augmented Generation (RAG) is a better approach to identify and retrieve only the most relevant information in real-time [[21]](https://www.meilisearch.com/blog/rag-vs-long-context-llms).

### Pick an Orchestration Style

The choice between predictable workflows and dynamic agents depends on the task. As we explored earlier, predictable, orchestrated workflows are best for tasks that are auditable and follow a relatively linear sequence of steps. Use them when you need reliability, governance, and control over execution, especially in enterprise scenarios where safety and observability are paramount [[22]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows). Dynamic agents are better suited for open-ended problems that require exploration, adaptation, and autonomous tool use, such as prototyping or tasks in ultra-dynamic environments.

Often, the best systems are hybrids. A research agent might autonomously explore a topic, but its final report generation could be handled by a structured workflow that includes validation, formatting, and human review steps. This combines the flexibility of agents with the reliability of workflows, giving you the best of both worlds. The key is to start with workflows for reliability and add agents only when the task's complexity genuinely demands their autonomy [[23]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents).

### Establish a HITL & Evaluation Loop

Full autonomy is a liability in high-stakes environments. You must define clear triggers for human intervention based on error cost and business risk. A human-in-the-loop system builds confidence by inserting approval gates at critical decision points. This is essential for preventing common agent failure modes, such as *cascading failures*, where an early error propagates through a long chain of steps, or *silent failures*, where the agent produces a confident but incorrect answer [[5]](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition). A more formal approach to risk management is Failure Mode and Effects Analysis (FMEA), a systematic process for identifying potential failures in a design, which can be applied iteratively to refine the agent's workflow and determine where human oversight is most needed [[24]](https://www.jamasoftware.com/requirements-management-guide/meeting-regulatory-compliance-and-industry-standards/fmea).

Frameworks like LangGraph provide built-in mechanisms for this, such as the `interrupt()` function, which can pause a workflow and wait for human input before proceeding [[14]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). Triggers can be based on low-confidence scores from the model, requests to perform sensitive or irreversible actions, or flags for topics that require policy review. For example, in our capstone, we might require human approval for the list of URLs the research agent plans to scrape, preventing it from going down irrelevant or costly paths. A custom evaluation loop, which we will cover in future lessons, ensures that you can measure the impact of these interventions and continuously improve the system's reliability.

### Set Tool Boundaries & Portability

An LLM should be responsible for intent detection and high-level planning, not for deterministic logic or heavy computation. Delegate tasks like complex math, data validation, or large file processing to regular code. This separation of concerns makes the system more robust, efficient, and easier to debug. The LLM's job is to decide *what* to do; your code's job is to do it reliably.

Furthermore, standardizing how your agent interacts with tools is essential for portability. The Model Context Protocol (MCP) provides a "USB-C port" for AI, defining a standard way for agents to connect to external tools and data sources [[2]](https://modelcontextprotocol.io/docs/getting-started/intro). It reduces boilerplate integration code by creating a unified interface, allowing you to build tools once and reuse them across different clients, IDEs, or agent frameworks without modification [[15]](https://www.databricks.com/blog/what-is-model-context-protocol). This prevents vendor lock-in and promotes a more modular, interoperable ecosystem. File-based artifact contracts, where each stage of a workflow has defined input and output directories, further enforce this separation and ensure clear accountability [[25]](https://fast.io/resources/ai-agent-artifacts).

### Choose Durability & Observability

Finally, your system's architecture must match its operational requirements. A long-running, stateful job, like generating a detailed research report, demands a system with built-in checkpoints, resumability, and detailed tracing. If the process fails halfway through, you need to be able to resume from the last successful step, not start from scratch. Frameworks like LangGraph are designed for this, providing persistence layers that save the state of your workflow at each step, enabling fault-tolerant execution [[16]](https://docs.langchain.com/oss/python/langgraph/persistence).

In contrast, a stateless task, like a simple Q&A bot that can be retried on failure, may only need a simple retry policy. Linking these choices back to the success criteria defined in Step 1 ensures you build a system with the right level of resilience without over-engineering. Furthermore, effective optimization is impossible without visibility. Implementing robust cost observability is a prerequisite for controlling costs in production. Attributing spend to specific requests, agents, and workflows in real time makes this possible [[6]](https://www.mirantis.com/blog/inference-costs).

This framework is iterative. You will likely revisit earlier decisions as you move through implementation and uncover new constraints. Once these high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency to budget them deliberately.
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** Points 1, 3, 4, 6, and 7 cover the same core ideas as the expected section with different but equivalent illustrative examples. Point 2 (Model Family) again omits the reasoning-depth-matching sub-point (dedicated reasoning models for exploratory tasks) and the data-modality/multimodality sub-point — the third article in a row for this lesson with this exact gap. Point 5 nods at evaluation with 'a custom evaluation loop, which we will cover in future lessons' but still does not present the expected section's actual evaluation-methodology content (small task-specific tests measuring utility/factuality/safety; leaderboards as a signal, not a substitute) — a partial improvement over the complete silence in the other two articles graded for this lesson, but still a substantive gap.
- `fl`: A General AI Engineering Decision Framework:
**1:** The seven points appear in the same order as the expected section, and the closing transition sentence into Section 3 is closely paraphrased. The content gaps inside points 2 and 5 are clean absences within a point's own paragraph, scored under CoreContent rather than here.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=4; quality=strong,strong,strong,standard] Four qualifying depth additions are present, all traceable to exploration-phase sources. (1) The Model Family point's 'LLM cascade' technique (cheap student model with teacher fallback on low confidence), traced to the exploration-phase OpenReview source on inference-time distillation (https://openreview.net/forum?id=nCEdAM5m5T) — strong: a specific, named technique with a clear mechanism. (2) The HITL point's 'cascading failures' and 'silent failures' concepts, traced to the exploration-phase MindStudio source on AI agent failure pattern recognition (https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition) — strong: two specific named failure modes with brief but accurate definitions matching the source. (3) The same point's Failure Mode and Effects Analysis (FMEA) reference, traced to the exploration-phase JamaSoftware source — strong: a specific, named formal methodology, not a generic mention (this instance is also credited under BreadthEnhancement, since FMEA is imported from an unrelated engineering discipline). (4) The Durability point's cost-observability discussion, traced to the exploration-phase Mirantis inference-costs source (https://www.mirantis.com/blog/inference-costs) — standard: a valid but brief, single-sentence point.
- `be`: A General AI Engineering Decision Framework:
**1:** [instances=1; quality=strong] The FMEA reference credited under DepthEnhancement also qualifies as breadth: Failure Mode and Effects Analysis is a formal risk-management methodology imported from systems/reliability engineering, a genuinely different discipline from AI/ML — a cross-domain connection per the breadth criteria. Traced to the same exploration-phase JamaSoftware source; classified strong for the same reasons given there.
- `cp`: A General AI Engineering Decision Framework:
**1:** The four depth additions and the FMEA breadth addition are each one-to-two-sentence insertions distributed across four of the seven points. The expected section's core content — the seven-step framework itself, including its illustrative examples — remains present and dominant throughout; no single point's core explanation is crowded out or made harder to follow.
- `ga`: A General AI Engineering Decision Framework:
**0:** Point 5 gestures at evaluation methodology but does not deliver the guideline's required content. Word-count audit (previously an approximation of "~1,378"; recomputed exactly): target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1357 — 257 words above the maximum.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook guides you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice. For example, a real-time customer support bot needs sub-second latency and can tolerate moderate accuracy, while a batch research job for a legal firm requires near-zero hallucination tolerance, with throughput measured in hours.

To formalize these trade-offs, we recommend using a decision matrix. This structured tool helps you move beyond intuition by systematically evaluating options against weighted criteria. The process involves several key steps: clearly define your objective, list all possible solutions, determine the evaluation criteria (e.g., cost, accuracy, latency), assign weights to prioritize them, and then score each option against these criteria [[2]](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects), [[3]](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45).

The matrix not only identifies the best choice but also serves as a design tool, revealing where hybrid solutions might offer a better balance. We will build one for our capstone project later in this lesson.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Anthropic, and Google deliver state-of-the-art performance with low operational overhead but can lead to vendor lock-in. They benefit from economies of scale, often making them cheaper per inference than self-hosting. Many also offer enterprise-grade security and compliance guarantees, such as data residency and zero-logging, which can simplify regulatory adherence.

Open-weight models such as those from Meta, Mistral, and DeepSeek guarantee privacy, deep customization through fine-tuning, and data locality, but place the entire burden of GPU management and infrastructure security on your team. This gives you complete control over the model version, insulating your systems from unexpected updates or performance degradations that can occur with proprietary APIs. The choice is not a simple binary but a trade-off between cutting-edge capability, operational simplicity, and ultimate control [[4]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/).

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not a silver bullet. A common mistake is to dump everything into a prompt, assuming the LLM can handle it. This naive approach often leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts [[5]](https://arxiv.org/abs/2307.03172), [[6]](https://openreview.net/forum?id=XSHP62BCXN). This U-shaped performance curve is a byproduct of how attention mechanisms work, with primacy and recency biases causing models to recall information from the beginning and end of a context far more reliably than from the middle [[7]](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf).

Instead of relying on raw context volume, you should prioritize selective retrieval, compression, and structured summaries to manage cost and improve reliability. For a chatbot that needs to remember recent interactions, a sliding window or summarization approach is suitable for managing conversational history [[8]](https://medium.com/@levi_stringer/simplifying-rag-context-windows-with-conversation-buffers-how-to-stop-your-agent-forgetting-df2149ad7403). For an agent answering questions from a large knowledge base, RAG is the better choice to identify and retrieve only the most relevant information for the current query [[9]](https://www.meilisearch.com/blog/rag-vs-long-context-llms).

### Pick an Orchestration Style

The choice between a predictable workflow and a dynamic agent depends on the task's nature. Use a structured workflow when the steps are known, repeatable, and need to be auditable and reliable at scale. This is ideal for processes like claims processing or generating a monthly report. Key characteristics of workflows are predefined steps, high predictability, and explicit orchestration logic, making them suitable for production systems where reliability is critical [[10]](https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents).

Use a dynamic agent when the path is unclear and requires exploration, reasoning, and adaptive tool use, such as diagnosing a system failure or conducting open-ended research. Agents excel in dynamic environments but can be unpredictable. Their reasoning is harder to interpret, which may raise compliance concerns [[11]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows), [[12]](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both). Hybrid designs, which we will use in our capstone, combine both styles to leverage the strengths of each. Start with workflows for reliability and add agents only when you can justify the need for autonomy and flexibility [[13]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents).

### Establish a HITL & Evaluation Loop

You must decide where to insert human oversight. This decision is tied to the cost of error and business risk. Instead of aiming for full autonomy from the start, define clear triggers for human intervention. These can be based on low-confidence scores from the model, requests for sensitive actions like financial transactions, or flags for policy violations. For example, a legal research agent could be interrupted to request clarification when it detects ambiguous information, ensuring human validation before proceeding [[14]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch).

LangGraph's interrupt mechanism allows you to pause a workflow, wait for human approval, and then resume execution cleanly [[15]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/), [[16]](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo). This creates a safety net that makes agentic systems practical for high-stakes environments. HITL interventions should be reactive and triggered only when needed, adding value without becoming a mandatory checkpoint that interrupts every workflow [[14]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch).

### Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic work to code. For example, an LLM should decide to calculate a financial metric, but the calculation itself should be executed by a dedicated Python function, not by the LLM's internal reasoning. This separation of concerns improves reliability and reduces computational load on the model.

Furthermore, protocols like the Model Context Protocol (MCP) enforce clean tool boundaries and enable portability [[17]](https://modelcontextprotocol.io/docs/getting-started/intro), [[18]](https://www.databricks.com/blog/what-is-model-context-protocol). MCP standardizes how agents connect to external tools, acting like a USB-C port for AI. It solves the "N×M integration problem" by requiring each client and server to implement the protocol just once, reducing total integrations from N×M to N+M. This allows you to build a tool once and expose it to any MCP-compatible client, such as an IDE or another agent, preventing vendor lock-in and making your tools reusable across different environments [[19]](https://www.guild.ai/glossary/ai-agent-portability).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand durability features like resumability and checkpoints to survive failures. A framework like LangGraph provides this out-of-the-box, saving the graph's state at each step using a checkpointer [[20]](https://docs.langchain.com/oss/python/langgraph/persistence). This enables time-travel debugging and fault-tolerant execution. For simple, stateless tasks, a basic retry policy may suffice. Your choice should align with the success criteria from Step 1. A critical batch process needs full tracing and resumability, while a non-essential, transient task does not.

For observability, file-based artifact contracts offer an inherently interpretable approach. By defining distinct input and output directories for each agent or workflow stage, every intermediate output becomes a readable file. This makes the system a "glass box," where you can inspect the state at any point without special logging tools. This structure enforces separation of concerns and creates a natural audit trail [[21]](https://arxiv.org/html/2603.16021v1), [[22]](https://fast.io/resources/ai-agent-artifacts).

Applying this framework helps you avoid common agent failure modes that differ from classic software bugs. These include **context degradation**, where agents lose track of information over long interactions; **cascading failures**, where a small error in an early step silently propagates and corrupts the entire workflow; and **silent failures**, where the agent completes a task and returns a plausible but incorrect result without raising an error [[23]](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition).

This framework is iterative. You will likely revisit earlier steps as new constraints and insights emerge during implementation. Once these high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency to budget them deliberately.
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** Points 1, 3, 4, 6, and 7 cover the same core ideas as the expected section with different but equivalent examples, one enriched with a well-anchored failure-modes summary (context degradation, cascading failures, silent failures). Point 2 (Model Family) again omits the reasoning-depth-matching and data-modality/multimodality sub-points — the seventh article in a row for this lesson with this exact gap. Point 5 (HITL & Evaluation Loop) covers triggers and the interrupt mechanism but never presents the expected section's evaluation-methodology content — the seventh consecutive article with this same omission.
- `fl`: A General AI Engineering Decision Framework:
**1:** The seven points appear in the same order as the expected section, and the closing transition sentence into Section 3 is closely paraphrased. The content gaps inside points 2 and 5 are scored under CoreContent rather than here.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=1; quality=strong] The closing paragraph's summary of agent-specific failure modes — context degradation, cascading failures, and silent failures — is traced to the exploration-phase MindStudio source on AI agent failure pattern recognition (https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition). Strong: three specific, accurately-defined named failure modes, even though presented briefly.
- `be`: A General AI Engineering Decision Framework:
**0:** [instances=0] The context-degradation/cascading/silent-failures addition (see DepthEnhancement) deepens understanding of agent-specific failure modes intrinsic to the core topic rather than connecting outward to an adjacent field, so it is classified as depth only.
- `cp`: A General AI Engineering Decision Framework:
**1:** The failure-modes addition is a single sentence appended near the end of the section, after all seven points have already been fully presented; it does not interrupt or dilute any point's core explanation.
- `ga`: A General AI Engineering Decision Framework:
**0:** Point 5 covers HITL triggers but never mentions evaluation methodology. Word-count audit (previously an approximation of "~1,238"; recomputed exactly): target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1210 — 110 words over the maximum.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook provides a step-by-step process to move from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

First, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance requirements, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice.

For instance, a real-time support bot demands sub-second latency and can tolerate moderate accuracy. Its value is in immediate response, so the design will prioritize fast, cheap models and minimal reasoning. In contrast, a high-accuracy batch research job for a financial firm measures throughput in hours and has a near-zero tolerance for hallucinations. Its value lies in correctness, justifying the use of expensive frontier models, extensive reasoning budgets, and human review gates. Clearly articulating these constraints up front prevents over-engineering a solution that is too slow or expensive for the business need, or under-engineering one that fails to meet quality standards.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic deliver state-of-the-art performance with low operational overhead, making them ideal for teams prioritizing speed and access to frontier capabilities. However, this path can lead to vendor lock-in and less control over model updates, as your system becomes dependent on a third-party service.

Open-weight models, on the other hand, guarantee privacy, deep customization, and data locality when self-hosted. This control is essential for regulated industries or applications involving sensitive intellectual property. The trade-off is the significant engineering and financial burden of managing your own GPU infrastructure, which includes security, scaling, and maintenance. This choice is not a simple binary; it is a strategic decision about where you want to invest your resources—in external API costs or internal infrastructure and expertise.

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not a cure-all. It is a common mistake to dump everything into a prompt and assume the LLM can handle it. This leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts. Instead of naive full-document dumps, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability [[1]](https://arxiv.org/abs/2307.03172), [[11]](https://openreview.net/forum?id=vlUk8z8LaM).

The right strategy depends on the task. For an agent that needs to remember the last few turns of a conversation, a sliding window summary is a cost-effective approach to maintain short-term memory. For retrieving specific facts from a large, dynamic knowledge base, Retrieval-Augmented Generation (RAG) is more suitable, as it identifies and fetches only the most relevant information for the current query. The goal is always to provide the densest, most relevant context possible, not the largest.

### Pick an Orchestration Style

The orchestration style depends on the task's predictability. As we discussed in Lesson 2, you should use predictable workflows for processes that are auditable and mostly linear. For open-ended problems that require dynamic tool use, autonomous agents are a better fit. This choice depends on process complexity and monitoring needs. Orchestration offers a centralized view for complex, stateful processes with conditional branches and exception paths. Simpler, high-throughput tasks might benefit from decentralized choreography [[12]](https://tetrate.io/learn/ai/multi-agent-systems).

The selection criteria often involve a trade-off between latency, governance, cost, and team skills. For example, a high-throughput, low-latency system might favor choreography for its scalability, while a system in a regulated industry would prefer orchestration for its centralized monitoring and control [[19]](https://www.dataiku.com/stories/blog/agent-orchestration-explained). For many production systems, the goal is predictability. Deterministic, inspectable workflows provide cost control and auditability, while still allowing for conditional routing and loops to handle variability [[13]](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows). Often, the best solution is a hybrid design that combines both, such as using orchestration for the main workflow and choreography for internal, routine operations [[12]](https://tetrate.io/learn/ai/multi-agent-systems), [[20]](https://techcommunity.microsoft.com/blog/azurearchitectureblog/building-ai-agents-workflow-first-vs-code-first-vs-hybrid/4466788).

### Establish a Human-in-the-Loop (HITL) & Evaluation Loop

The level of human oversight should be tied directly to business risk and the cost of error. Instead of choosing between full autonomy and full manual control, you should define clear triggers for human intervention. These can include low-confidence scores from the model, requests for sensitive actions like database writes, or policy flags that require compliance checks. For a financial trading agent, you might require human approval for any trade exceeding a certain value. For a content summarizer, you might only trigger a human review if the model's confidence score falls below 90%.

Lessons from autonomous vehicle safety are relevant here. The most effective HITL systems use agent-specific protocols, where the human feedback is tailored to the agent's learning algorithm and internal state. This allows for more precise and informative guidance, accelerating learning and improving decision-making, in contrast to generic, agent-agnostic prompts [[21]](https://arxiv.org/html/2408.12548v1). Mature HITL systems also move beyond simple confidence scores. Escalation should be triggered by context-dependent factors, such as financial thresholds, reputational risk, or when multi-agent complexity degrades cumulative reliability. The architectural goal is to move from hardcoded guardrails in individual agents to a centralized policy engine, making governance manageable at scale [[14]](https://galileo.ai/blog/human-in-the-loop-agent-oversight).

### Set Tool Boundaries & Portability

An LLM’s job is to understand intent and orchestrate high-level steps, not to perform deterministic calculations or heavy data processing. Delegate tasks like math, data validation, or file manipulation to traditional code. This separation of concerns makes your system more reliable and efficient. This approach mirrors the evolution from monolithic applications to microservices. The large, brittle prompt is the new monolith. By breaking down capabilities into modular agents, each with a bounded context and a well-defined contract, you build a system that is more governable and scalable [[15]](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices).

Furthermore, using standards like the Model Context Protocol (MCP) ensures your tools are portable. This solves the N×M integration problem, where each of N tools needs a custom integration for M clients. With MCP, you implement the protocol once per tool and once per client, reducing the integration effort from N×M to N+M and allowing you to expose the same tool to different clients without being locked into a single vendor’s ecosystem [[5]](https://modelcontextprotocol.io/docs/getting-started/intro).

### Choose Durability & Observability

Finally, match your system's durability to the task's requirements. For long-running, stateful jobs, you need built-in checkpoints, resumability, and detailed tracing to survive failures and debug complex behavior. A financial reporting workflow that runs overnight needs to be able to resume from the last successful step if it fails. Frameworks like LangGraph provide this by saving a snapshot of the graph state at every step, enabling not just fault tolerance but also time-travel debugging and human-in-the-loop interventions [[22]](https://docs.langchain.com/oss/python/langgraph/persistence).

In contrast, a simple, stateless loop with a basic retry policy may suffice for quick, idempotent tasks, like a web-scraping job that can be restarted from the beginning without losing critical state. These choices should link back to the success criteria you defined in the first step, ensuring your system's reliability matches its business value.

This framework is iterative. You will likely revisit earlier steps as you uncover new constraints during implementation. Once the high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency so you can budget them deliberately.
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** The generated section covers all seven steps in the correct order, but two substantive ideas from the expected section are absent: (1) the multimodal-capability discussion in Step 2, and (2) the evaluation-plan guidance in Step 5. Neither appears anywhere in the generated section.
- `fl`: A General AI Engineering Decision Framework:
**1:** Same seven-step order in both; the added depth/breadth elements are integrated without disrupting the flow.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=4; quality=strong,strong,strong,strong] Confirmed on review — the submitted file's analysis here is sound. (1) Orchestration-vs-choreography selection criteria (Tetrate + Dataiku, exploration) — strong, also credited under BreadthEnhancement. (2) Deterministic/inspectable orchestration design philosophy (Microsoft Conductor, exploration) — strong. (3) Context-dependent HITL escalation and centralized policy engines (Galileo, exploration) — strong. (4) Agent-specific vs. agent-agnostic HITL protocols (autonomous-vehicle-safety arXiv paper, exploration) — strong, also credited under BreadthEnhancement. None paraphrase the ground truth — GT's Section 2 does not discuss choreography, Conductor, context-dependent escalation, or autonomous-vehicle HITL research at all.
- `be`: A General AI Engineering Decision Framework:
**1:** [instances=3; quality=strong,strong,strong] Confirmed on review — this is a thorough, well-reasoned analysis. (1) Orchestration/choreography imports a distinction native to SOA/distributed-systems architecture (Tetrate + Dataiku, exploration) — strong, dual-credited with DepthEnhancement. (2) Autonomous-vehicle-safety HITL lessons (arXiv, exploration) — strong, dual-credited with DepthEnhancement. (3) The monolith-to-microservices analogy (TEKsystems, exploration) — strong, correctly credited as breadth-only rather than dual, since it is a framing analogy rather than an independent technical claim about the core topic's own inner workings — this distinction is well-reasoned in the submitted file and confirmed correct here.
- `cp`: A General AI Engineering Decision Framework:
**1:** The four depth additions and three breadth additions are concise and well-integrated into the specific steps they relate to; the core 7-step framework remains dominant.
- `ga`: A General AI Engineering Decision Framework:
**0:** REVISED from the submitted reasoning.json (previously scored 1, citing an approximate '~950 words... within tolerance'). Word-count audit: target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1179. 79 words above the maximum — a real, non-borderline failure, not the pass the submitted reasoning claimed.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define what success looks like. This includes the required output quality, any privacy or compliance requirements, the expected volume of tasks, and your per-task spending limit. These targets dictate every downstream choice. For example, a real-time customer support bot demands sub-second latency, where moderate accuracy might be acceptable. In contrast, a high-accuracy batch research job has a throughput measured in hours and a near-zero tolerance for hallucinations. Constraints like GDPR might require data to remain within a specific geographic region, heavily influencing the choice between a public API and a self-hosted model.

A decision matrix is a useful tool for this step. It helps you list all your criteria, assign weights based on their importance, and score different options. This structured approach forces you to articulate your priorities and provides a clear rationale for your design choices, covering everything from model selection to feature prioritization [[9]](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects), [[10]](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45). Clearly articulating these factors upfront prevents costly redesigns later.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic deliver state-of-the-art performance with low operational overhead but can lead to vendor lock-in and data privacy concerns. Open-weight models from providers like Meta (Llama), Mistral, and DeepSeek offer unparalleled privacy, customization, and data locality, which is essential for sensitive applications. However, this path comes with the significant burden of managing your own GPU infrastructure.

The choice depends on whether your priority is cutting-edge capability with simplicity or maximum control and security. While self-hosting seems to offer a straightforward path to compliance, it places the entire burden of securing the infrastructure on your team. Top API providers often offer dedicated instances and private endpoints that meet stringent regulatory standards, making the security argument more nuanced. A hybrid approach is also common, using a powerful closed model for complex reasoning and a smaller, self-hosted open model for routine tasks like data extraction or classification.

### Define Your Context Strategy

As we discussed in previous lessons, simply dumping all available information into a large context window is a common mistake. Research shows this leads to a "lost-in-the-middle" performance cliff, where models struggle to recall information buried in the middle of long prompts. This bias appears to stem from the model’s autoregressive nature and the information retrieval demands of its training data, which favor the beginning and end of a sequence [[1]](https://arxiv.org/abs/2307.03172), [[8]](https://openreview.net/forum?id=XSHP62BCXN).

Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For instance, a sliding window summarization approach is effective for remembering the latest information in a long-running chat, as it compresses past turns to keep the working memory concise. In contrast, RAG is better suited for retrieving specific, relevant facts from a large knowledge base to answer a question, ensuring the model has the exact data it needs without being overloaded [[11]](https://www.meilisearch.com/blog/rag-vs-long-context-llms).

### Pick an Orchestration Style

The choice between a predictable workflow and a dynamic agent depends on the nature of the task. As we covered in Lesson 2, you should use workflows for processes that are auditable and mostly linear, where the steps are known and repeatable. For open-ended problems that require dynamic tool use and adaptation, an agent is more appropriate. Many production systems use a hybrid design, combining the reliability of workflows with the flexibility of agents.

For many business processes, deterministic orchestration is preferable to dynamic, LLM-driven routing. While agentic replanning offers flexibility, predictable and auditable graphs provide superior cost control, observability, and reliability for structured tasks. This approach still allows for complex logic through conditional routing and loops without sacrificing governance. For example, a workflow might handle the predictable steps of a customer onboarding process, while an agent is tasked with the open-ended problem of researching a new lead [[12]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows), [[13]](https://www.reddit.com/r/AI_Agents/comments/1nwwb5g/agents_vs_workflows_how_to_tell_the_difference).

### Establish a HITL & Evaluation Loop

You must decide where to insert human oversight into your system. This decision should be tied directly to the cost of an error and the overall business risk. Instead of aiming for full autonomy from the start, define clear triggers for human intervention. These can include low-confidence scores from the model, requests to perform sensitive actions like sending an email, or flags indicating a policy violation. A financial trading agent might require human approval before executing a trade, whereas a content summarization tool might operate autonomously unless its confidence score drops below a certain threshold.

LangGraph's `interrupt()` function is a powerful mechanism for implementing these gates, allowing you to pause execution, collect human input, and resume the workflow cleanly. Production-grade HITL goes beyond simple confidence scores. Escalation should also be triggered by context-dependent factors, such as financial transactions exceeding a certain value, decisions affecting high-profile clients, or when multi-agent complexity increases cumulative uncertainty. To avoid brittle, hardcoded logic, these rules are best managed in a centralized policy engine. This separates policy from application code, making fleet-wide governance operationally manageable [[4]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/), [[14]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch), [[15]](https://galileo.ai/blog/human-in-the-loop-agent-oversight).

### Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic tasks to code. The LLM decides *what* to do, and your code handles *how* to do it. For example, the LLM should not be asked to perform calculations; it should call a calculator tool. This separation of concerns improves reliability.

Furthermore, protocols like the Model Context Protocol (MCP) enforce clean tool boundaries, ensuring your tools are portable and can be used by different agents or clients without being tied to a single vendor or framework. This approach, similar to microservices architecture, creates a system that is more modular, governable, and scalable by avoiding the brittleness of a single, monolithic prompt [[2]](https://modelcontextprotocol.io/docs/getting-started/intro), [[3]](https://www.databricks.com/blog/what-is-model-context-protocol), [[16]](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, checkpoints, and full tracing to recover from failures. A multi-hour research task, for instance, should be able to resume from the last completed step if it fails. LangGraph, with its built-in checkpointing, is well-suited for such tasks. For stateless tasks that complete quickly, a simple retry policy may suffice [[17]](https://docs.langchain.com/oss/python/langgraph/persistence), [[18]](https://medium.com/@okanyenigun/built-with-langgraph-17-checkpoints-2d1d54e1464b).

One of the primary reasons long-running jobs fail is due to a "self-conditioning" effect. Research has shown that models become more likely to make a mistake after observing their own errors in the context history. This creates a negative feedback loop where one error increases the probability of another, causing performance to degrade over long execution chains. This is distinct from simple long-context degradation and highlights the need for robust state management and error recovery. Your choice should align with the success criteria defined in the first step [[19]](https://arxiv.org/html/2509.09677v1).

This framework is iterative. You will likely revisit earlier decisions as new constraints and insights emerge during implementation. Once the high-level design is framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget for them deliberately.
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** Points 1, 3, 4, 6, and 7 cover the same core ideas as the expected section with different but equivalent illustrative examples. Point 2 (Model Family) again omits the reasoning-depth-matching sub-point and the data-modality/multimodality sub-point — the fourth article in a row for this lesson with this exact gap. Point 5 (HITL & Evaluation Loop) contains a well-developed HITL policy-engine discussion but, like the other three articles graded for this lesson, never presents the expected section's evaluation-methodology content (task-specific tests measuring utility/factuality/safety; leaderboards as a signal, not a substitute) — this time not even a forward-reference gesture at it.
- `fl`: A General AI Engineering Decision Framework:
**1:** The seven points appear in the same order as the expected section, and the closing transition sentence into Section 3 is closely paraphrased. The content gaps inside points 2 and 5 are scored under CoreContent rather than here.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=3; quality=strong,strong,strong] Three qualifying depth additions are present, all traceable to exploration-phase sources. (1) The HITL point's discussion of context-dependent escalation triggers (financial thresholds, high-profile-client decisions, multi-agent chain complexity) and the move from hardcoded logic to a centralized policy engine, traced to the exploration-phase Galileo source on HITL agent oversight (https://galileo.ai/blog/human-in-the-loop-agent-oversight) — strong: a near-verbatim, well-developed match to the source's own framing. (2) The Tool Boundaries point's microservices analogy ('similar to microservices architecture... avoiding the brittleness of a single, monolithic prompt'), traced to the exploration-phase TEKsystems source on multi-agent systems as the next evolution of microservices (https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices) — strong: a specific, well-developed cross-domain analogy (also credited under BreadthEnhancement). (3) The Durability point's 'self-conditioning effect' — models becoming more likely to err after seeing their own prior errors in context, distinct from ordinary long-context degradation — traced to the exploration-phase arXiv paper on long-horizon execution (https://arxiv.org/html/2509.09677v1), which defines this exact effect in near-identical terms — strong.
- `be`: A General AI Engineering Decision Framework:
**1:** [instances=1; quality=strong] The microservices analogy credited under DepthEnhancement also qualifies as breadth: it imports an architectural pattern from a distinct engineering discipline (distributed systems / microservices architecture) to explain the value of tool-boundary discipline, a genuine cross-domain connection. Traced to the same exploration-phase TEKsystems source; classified strong for the same reasons given there.
- `cp`: A General AI Engineering Decision Framework:
**1:** The three depth/breadth additions (HITL policy-engine discussion, microservices analogy, self-conditioning effect) are each one-to-three-sentence insertions distributed across three of the seven points. The expected section's core content — the seven-step framework and its illustrative examples — remains present and dominant throughout; no point's core explanation is crowded out.
- `ga`: A General AI Engineering Decision Framework:
**0:** Point 5 presents a well-developed HITL policy-engine discussion but does not mention evaluation methodology at all. Word-count audit (previously an approximation of "~1,189"; recomputed exactly): target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1168 — 68 words above the maximum.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define success. What is the quality bar for the output? What are the privacy or compliance requirements? What is the expected volume of tasks, and what are your per-task spending limits? These targets dictate every downstream choice.

For example, a real-time customer support bot demands sub-second latency where moderate accuracy is acceptable. In contrast, a high-accuracy batch research job measures throughput in hours and has a near-zero tolerance for hallucinations. Clearly articulating these constraints upfront prevents over-engineering a solution that is too slow or expensive for its purpose.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic deliver state-of-the-art performance with low operational overhead but can lead to vendor lock-in.

Open-weight models guarantee privacy, deep customization through fine-tuning, and data locality, but place the entire burden of GPU management and infrastructure security on your team. This choice is not a simple open-versus-closed binary; it’s a trade-off between frontier capability and operational control. A hybrid approach, using a powerful closed model for complex reasoning and a smaller open model for routine tasks, often provides a practical balance.

### Define Your Context Strategy

As we saw in previous lessons, simply dumping everything into a prompt is a common mistake that leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts. This positional bias is not arbitrary; it stems from information retrieval demands in the training data and the autoregressive nature of LLMs, which naturally biases attention toward the beginning and end of a sequence [[1]](https://arxiv.org/abs/2307.03172), [[2]](https://arxiv.org/html/2510.10276v1).

The effect is strongest when inputs occupy up to 50% of the context window; beyond that, a simpler distance-based bias tends to dominate. A large context window is not a substitute for a disciplined context strategy. You must prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability [[3]](https://openreview.net/forum?id=vlUk8z8LaM).

For instance, when an agent needs to remember the last few turns of a conversation, a sliding window or summarization approach is often sufficient to maintain short-term memory. However, when the agent must answer a question based on a large corpus of documents, Retrieval-Augmented Generation (RAG) is the right tool to identify and retrieve only the most relevant information.

### Pick an Orchestration Style

The choice between predictable workflows and dynamic agents depends on the nature of the task. As we discussed, workflows are ideal when the steps are known, repeatable, and need to be auditable, like processing a claims form. They provide structure and predictability, which is essential for enterprise-grade reliability.

Agents excel when the path is unclear and requires open-ended tool use, such as diagnosing a software bug. Hybrid designs, which we will use in our capstone, often provide the best of both worlds by embedding intelligent agents within a structured, governable workflow, allowing for both flexibility and control.

### Establish a HITL & Evaluation Loop

You must decide where to insert human oversight. The decision to implement HITL triggers, confidence gates, or custom evaluation loops should be tied directly to error cost and business risk. Define clear triggers for human intervention, such as when an agent’s confidence score falls below a certain threshold, when it attempts a sensitive action like deleting a file, or when a policy flag is raised.

For our research agent, a good trigger would be to ask for human approval before beginning a new line of inquiry that could be costly or time-consuming. For the final article, a mandatory human sign-off is a non-negotiable quality gate.

Lessons from safety-critical domains like autonomous vehicles are relevant here. Production HITL systems move beyond simple triggers to implement confidence-based escalation, where low-confidence decisions are automatically routed for review, and centralized policy engines that can be updated without redeploying every agent. This ensures a balance between autonomy and oversight, preventing costly errors before they happen. Frameworks like LangGraph facilitate this by providing built-in `interrupt()` functions that can pause a workflow and wait for human input before proceeding, making it easier to implement these critical safety checks [[4]](https://galileo.ai/blog/human-in-the-loop-agent-oversight), [[13]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/).

### Set Tool Boundaries & Portability

A core principle of robust system design is to keep the LLM responsible for what it does best: intent detection and high-level planning. Delegate deterministic tasks, heavy computation, or complex validation to traditional code. For example, instead of asking an LLM to calculate a total, have it call a calculator tool.

This principle mirrors the shift from monolithic applications to microservices in traditional software engineering. In that world, the monolith was the enemy of scalability; in AI, the new monolith is the large, brittle prompt. By treating agents as independent services with well-defined contracts, you create a system that is more modular, governable, and scalable [[5]](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices).

Protocols like the Model Context Protocol (MCP) enforce this clean separation by creating a standardized interface for tools, which ensures they remain portable across different clients and IDEs without tying your implementation to a single vendor. MCP's client-server architecture allows an agent to discover and interact with tools at runtime, reducing the need for hardcoded integrations and making the entire system more flexible [[6]](https://modelcontextprotocol.io/docs/getting-started/intro), [[14]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, checkpoints to save progress, and full tracing to debug failures. For these, a framework like LangGraph is essential, as it provides built-in persistence layers that save the graph state at every step.

This enables not only fault tolerance but also time-travel debugging and human-in-the-loop workflows. In contrast, for stateless tasks where you can simply retry on failure, a simple policy may suffice. The choice should link back to the success criteria you defined in the first step. If a two-hour research job fails at the last minute, you need to be able to resume from the last successful step, not start from scratch [[15]](https://docs.langchain.com/oss/python/langgraph/persistence).

This framework is iterative. You will likely revisit earlier steps as new constraints and insights emerge during implementation. Once the high-level decisions are framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget them deliberately.
```
**Grader reasoning:**
- `cc`: A General AI Engineering Decision Framework:
**0:** Points 1, 3, 4, 6, and 7 cover the same core ideas as the expected section with different but equivalent examples, two enriched with well-anchored additions (a policy-engine/autonomous-vehicle-safety elaboration, a microservices analogy). Point 2 (Model Family) again omits the reasoning-depth-matching and data-modality/multimodality sub-points — the eighth article in a row for this lesson with this exact gap. Point 5 (HITL & Evaluation Loop) covers triggers, examples, and a well-developed policy-engine discussion but never presents the expected section's evaluation-methodology content — the eighth consecutive article with this same omission.
- `fl`: A General AI Engineering Decision Framework:
**1:** The seven points appear in the same order as the expected section, and the closing transition sentence into Section 3 is closely paraphrased. The content gaps inside points 2 and 5 are scored under CoreContent rather than here.
- `de`: A General AI Engineering Decision Framework:
**1:** [instances=2; quality=strong,strong] (1) Point 5's discussion of confidence-based escalation and centralized policy engines that can be updated without redeploying every agent, drawing an explicit lesson from autonomous-vehicle safety systems, is traced to the exploration-phase Galileo source on HITL agent oversight (https://galileo.ai/blog/human-in-the-loop-agent-oversight), matched closely to that source's own framing — strong. (2) Point 6's microservices analogy ('the new monolith is the large, brittle prompt... more modular, governable, and scalable') is traced to the exploration-phase TEKsystems source (https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices) — strong (also credited under BreadthEnhancement).
- `be`: A General AI Engineering Decision Framework:
**1:** [instances=1; quality=strong] The microservices analogy credited under DepthEnhancement also qualifies as breadth: it imports an architectural pattern from a distinct engineering discipline to explain the value of tool-boundary discipline, a genuine cross-domain connection. Traced to the same exploration-phase TEKsystems source; classified strong for the same reasons given there.
- `cp`: A General AI Engineering Decision Framework:
**1:** The two depth/breadth additions (policy-engine discussion, microservices analogy) are each two-to-three-sentence insertions in points 5 and 6; the expected section's core content — the seven-step framework and its illustrative examples — remains present and dominant throughout, with points 1, 3, 4, and 7 largely unaffected.
- `ga`: A General AI Engineering Decision Framework:
**0:** Point 5 never mentions evaluation methodology. Word-count audit (previously an approximation of "~1,059"; recomputed exactly): target 1000, tolerance +/-100, range [900, 1100]. Exact prose-only count: 1045 — within range; word count is not the reason for this score.

## Section: S3::section-3-inference-time-scaling-and-the-cost-latency-calculus  (weight=0.219, contribution=+0.0074 FOR standard)
Stored section rewards: standard=0.5738  deep=0.5332  (explore: standard=0.2303  deep=0.2025)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Both sections cover the four levers and provide a naive-vs-budgeted cost comparison. The core ideas are identical; the different specific models used are a numeric-illustration substitution, not a named-artifact mismatch.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Image 1 is placed after all four levers and before the cost calculation, matching the expected section's order exactly. Flow preserved.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=2; quality=strong,strong] Confirmed on review: (1) the 7B-can-outperform-70B-with-thinking-time claim (MindStudio, exploration) — strong; (2) the cascade-to-expensive-model-on-low-confidence mechanism (OpenReview, exploration), a distinct instance from the Framework section's use of the same source — strong. The o1-like-models degradation claim is correctly excluded (exploitation-phase). Neither credited instance restates ground-truth content — GT does not discuss either mechanism.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**0:** [instances=0] No breadth additions present.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The two depth additions are concise and directly support the core narrative about the four levers, which remains dominant.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Consistent with the submitted reasoning.json's verdict. Word-count audit: target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 691 (submitted claimed an approximate '~650') — within range. The five-field quantitative bullet breakdown is present for both designs, satisfying the guideline's format requirement; the underlying prices are addressed separately under research_anchoring.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
## Inference-Time Scaling and the Cost/Latency Calculus

Understanding and controlling the four independent levers of runtime scaling is central to effective system design. These levers act as control knobs, and like in control theory, adjusting them requires understanding their feedback effects on cost, latency, and quality [[10]](https://arxiv.org/html/2602.03433v1). Each can be adjusted on a per-step basis within a workflow, and their multiplicative interaction can create massive differences in cost and performance.

### Model Size Scaling

The most straightforward lever is model size. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash-Lite. The price difference can be staggering: GPT-4.5's input tokens are 750 times more expensive than those of Gemini 2.5 Flash-Lite. For high-value tasks where mistakes are expensive, such as legal analysis or medical diagnosis, using a frontier model is often justified. For high-volume, low-complexity tasks like simple data extraction or routing customer queries, a smaller, faster model provides a much better cost-performance balance.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens" or a longer chain-of-thought. Modern reasoning models can be instructed to "think harder" on a problem, which can improve accuracy on complex tasks but increases both latency and cost. For example, Anthropic's Claude models support "extended thinking," where you can allocate a specific token budget for internal reasoning before the final answer is generated [[7]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This should be treated as a dial, activated only for the most complex planning or validation steps and strictly capped to bound spend. This is important because research on o1-like models shows that simply increasing the thinking budget or chain-of-thought length does not guarantee better performance. In fact, longer reasoning chains can sometimes decrease accuracy due to flawed self-revision, where the model corrects a right answer into a wrong one [[9]](https://arxiv.org/html/2502.12215v1).

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, known as self-consistency, can significantly improve reliability by filtering out stochastic errors. Research shows that for a given compute budget, parallel scaling can sometimes be more effective than additional serial reasoning [[9]](https://arxiv.org/html/2502.12215v1). However, the reliability gains come at a linear cost multiplier, as you are paying for each parallel run. This lever should be reserved for steps where accuracy is paramount and the cost is justifiable.

### Input Context Scaling

While large context windows seem powerful, every additional token carries a direct cost and adds to latency. As discussed, this also introduces the risk of the "lost-in-the-middle" problem, where the model's performance degrades due to the U-shaped attention curve [[1]](https://arxiv.org/abs/2307.03172). The key is to find the optimal balance between providing enough information and avoiding cognitive overload. Techniques like RAG, summarization, and context caching are essential for keeping the effective context small while preserving the most critical signals for the model.

These levers can be combined into sophisticated cost-saving patterns. One powerful technique is *inference-time distillation*. A cheap "student" model, guided by examples from an expensive "teacher" model, handles most queries. Using self-consistency to check confidence, the system defers to the teacher only when needed, optimizing the cost-accuracy trade-off per-query [[4]](https://openreview.net/forum?id=nCEdAM5m5T).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down 
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)

To see how these levers multiply, consider a simple cost calculation. A naive design might use a premium reasoning model, dump an entire document into the context, and run a single pass. A budgeted design for the same task might use a fast, cheap model, employ RAG to shrink the context, and also run a single pass.

-   **Naive Design:**
    -   **Model:** Claude 4 opus (Input: $15/M, Output: $75/M)
    -   **Input Tokens:** 10,000
    -   **Output Tokens:** 1,000
    -   **Number of Parallel Runs:** 1
    -   **Calculation:** `(10,000 * $15/M + 1,000 * $75/M) * 1 = ($0.15 + $0.075) = $0.225`

-   **Budgeted Design:**
    -   **Model:** Gemini 2.5 Flash Lite (Input: $0.10/M, Output: $0.40/M)
    -   **Input Tokens:** 1,000
    -   **Output Tokens:** 200
    -   **Number of Parallel Runs:** 1
    -   **Calculation:** `(1,000 * $0.10/M + 200 * $0.40/M) * 1 = ($0.0001 + $0.00008) = $0.00018`

The difference is over 1,200x. This highlights the economic reality of designing agentic systems. Additional optimizations at the infrastructure level, such as dynamic batching and efficient KV cache management, can further reduce costs, especially at scale [[11]](https://www.yottalabs.ai/post/how-llm-inference-actually-works-in-production-and-why-most-systems-fail). Per-step reasoning caps, prompt caching, and delegating heavy computation to external tools also keep the system efficient. With the scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our capstone.
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** All four levers are covered with matching substance, the Image 1 caption is verbatim, and the naive-vs-budgeted cost exercise uses the same 5-bullet structure and reaches a comparable order of magnitude (~1,250x here vs ~1,000x in the expected section). Per standing ruling, a different but analogous numeric example reaching a different specific multiple is not a CoreContent issue; magnitude-target compliance is evaluated under guideline_adherence instead.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Image 1 is placed after all four levers and the levers-combination aside, immediately before the cost-comparison exercise — the same relative position as the expected section, unlike the other article graded for this lesson which moved this image to the very start of the section.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=1; quality=strong] The 'inference-time distillation' elaboration following the four levers — a cheap student model handling most queries, with self-consistency used to check confidence and decide when to defer to an expensive teacher model — is a well-developed, specific mechanism traced to the same exploration-phase OpenReview source (https://openreview.net/forum?id=nCEdAM5m5T) credited under the Framework section. This is a distinct instance in this section rather than a duplicate of that one, since it appears in a different section and elaborates a different aspect (the confidence-check trigger mechanism) of the same underlying technique.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=1; quality=standard] The intro paragraph's framing of the four levers as 'control knobs' whose adjustment requires understanding 'feedback effects,' explicitly likened to control theory, is traced to the exploration-phase arXiv source on control theory for language models (https://arxiv.org/html/2602.03433v1). Classified as standard: a brief, single-sentence analogy rather than a developed cross-domain argument.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The control-theory framing (one sentence) and the inference-time-distillation elaboration (two sentences) are brief and do not dilute the four-lever explanations or the cost-comparison exercise, which remain the section's clear focus.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The four levers are covered, the Image 1 caption is verbatim, and the naive-vs-budgeted cost contrast reaches approximately 1,250x, meeting the guideline's "roughly 1000x reduction" target. Word-count audit (previously an approximation of "~736"; recomputed exactly): target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 709 — within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
## Inference-Time Scaling and the Cost/Latency Calculus

The four inference-time levers can be understood through the lens of control systems theory, where each acts as a knob to regulate the system's cost, latency, and quality. This reframes the goal from simply "prompting" to actively steering a dynamic system [[24]](https://arxiv.org/html/2602.03433v1). Understanding how to manage cost and latency at runtime is central to effective system design. There are four independent levers you can adjust, often on a per-step basis, to trade performance for cost. Their multiplicative effect means that seemingly small choices can lead to a 1000x difference in spend.![The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies. (Source [https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling))

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite. For instance, GPT-4.5's input token cost is roughly 750 times higher than that of Gemini 2.5 Flash Lite [[25]](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source:). For a high-value task where mistakes are expensive, a frontier model is a sound investment. For high-volume, low-stakes tasks like simple data categorization, a cheaper "flash" or "mini" model is more appropriate.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often implemented as "thinking tokens" or a longer chain of thought. For example, Anthropic's Claude models offer an "extended thinking" mode where you can set a token budget for internal reasoning [[26]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This approach can decouple intelligence from model size, as a smaller model with an adequate thinking budget can sometimes outperform a larger one [[27]](https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained). However, this lever has diminishing returns; longer reasoning chains do not always improve accuracy and can even lead to performance degradation, particularly in weaker models [[28]](https://arxiv.org/html/2502.12215v1), [[29]](https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token). The key is to treat extra reasoning as a dial, activating it only for complex planning or validation steps and capping it to bound both cost and latency.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response. A common technique is self-consistency, where the final answer is chosen by a majority vote among several generated outputs. This can improve reliability, and research suggests that parallel scaling offers superior coverage and scalability compared to sequential scaling for the same budget [[28]](https://arxiv.org/html/2502.12215v1). The trade-off is a linear increase in cost for each parallel run. A more advanced method, "Shortest Majority Vote," enhances this by prioritizing clusters of answers that are not only more frequent but also have shorter reasoning paths, leveraging the observation that correct solutions are often more concise.

### Input Context Scaling

While providing more context can help an LLM, each additional token carries a direct cost and adds to latency. As discussed, models also struggle with the "lost-in-the-middle" problem, so simply increasing context size can be counterproductive. The goal is to find the optimal balance. Techniques like RAG, summarization, and prompt caching help keep the effective context small while preserving the necessary signal.

An effective pattern combining these levers is **inference-time distillation**. Here, a cheap "student" model handles most tasks using in-context examples from an expensive "teacher" model. The system only falls back to the teacher when the student's confidence is low (detected via self-consistency). This adaptive cascade can reduce costs by 2-4x while matching teacher accuracy, without any fine-tuning [[30]](https://openreview.net/forum?id=nCEdAM5m5T).

To see how these levers multiply, consider two designs for a research task.

**A naive design might:**
*   **Model:** Use the largest reasoning model (e.g., GPT-4.5 at $75/M input tokens).
*   **Input Tokens:** Dump a full 100-page document (approx. 50,000 tokens) into the context.
*   **Output Tokens:** Allow for a long, detailed response (e.g., 4,000 tokens).
*   **Number of Parallel Runs:** Use five parallel runs for self-consistency.
*   **Calculation:** (50,000 * $75/M + 4,000 * $150/M) * 5 runs = **$21.75 per task**.

**A budgeted design might:**
*   **Model:** Use a fast, cheap model for initial summarization (e.g., Gemini 2.5 Flash at \$0.30/M input tokens) and a mid-tier model for the final answer (e.g., GPT-4o at \$2.50/M input tokens).
*   **Input Tokens:** Use RAG to retrieve the 5 most relevant chunks (approx. 2,000 tokens).
*   **Output Tokens:** Generate a concise answer (e.g., 1,000 tokens).
*   **Number of Parallel Runs:** Use a single run.
*   **Calculation:** (2,000 * $2.50/M + 1,000 * $10/M) * 1 run = **$0.015 per task**.

The budgeted design achieves a greater than 1000x cost reduction while potentially delivering similar or even better quality by providing focused context. Other optimizations, like prompt caching and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** All four levers are covered with matching substance (plus well-anchored control-theory and inference-time-distillation additions), the Image 1 caption content is present, and the naive-vs-budgeted cost exercise uses the same 5-bullet structure, reaching ~1,450x — reasonably close to the expected section's ~1,000x. Per standing ruling, magnitude differences and the exercise's internal-consistency problems (see guideline_adherence/research_anchoring) are evaluated there, not here.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** REVISED: previously scored 0 for placing Image 1 at the section start rather than after all four levers. Applying the coherence test now applied consistently across this project: this is a standard preview-then-detail structure, coherent and non-disruptive. Not scored as a Flow failure.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=1; quality=strong] The 'inference-time distillation' pattern — a cheap student model handling most queries, falling back to an expensive teacher model only when self-consistency signals low confidence, quantified as a 2-4x cost reduction while matching teacher accuracy — is traced to the exploration-phase OpenReview source on inference-time distillation (https://openreview.net/forum?id=nCEdAM5m5T). Strong: specific, well-developed, and quantified.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=1; quality=strong] The intro's framing of the four levers through the lens of control systems theory — reframing the goal from 'prompting' to 'steering a dynamic system' — is traced to the exploration-phase arXiv source on control theory and language models (https://arxiv.org/html/2602.03433v1). Strong: a specific, well-integrated cross-domain framing.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The control-theory framing (one sentence) and the inference-time-distillation addition (a short paragraph) are both brief relative to the section and do not dilute the four-lever explanations or the cost-comparison exercise, which remain the section's clear focus.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The four levers are covered; word-count audit (previously an approximation of "~761"; recomputed exactly): target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 749 — within range. Per the prior correction on this entry: the cost exercise's unit-price slip pushed the budgeted design's cost estimate up (the conservative direction), and the result still lands comfortably under 1/1000 of the naive design's cost, so the guideline's "~1000x cheaper" point is still delivered without distortion.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
## Inference-Time Scaling and the Cost/Latency Calculus

Understanding how to manage cost and latency at runtime is central to effective system design. There are four independent levers you can adjust, often on a per-step basis, within a workflow: model size, series scaling, parallel scaling, and input context scaling. How they interact and multiply determines your final cost and performance.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down 
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-5.5 have higher per-token costs than smaller, optimized models like GPT-5.4 mini. For high-value tasks where mistakes are expensive, such as legal contract analysis, using a frontier model is justified. For high-volume, lower-stakes tasks like categorizing customer support tickets, a cheaper, faster model is a better choice. The key is to match the model's capability—and its associated cost—to the value of the task.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often through "thinking tokens" [[2]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). You should treat these extra reasoning steps as a dial that you turn up only for the most complex planning or validation steps. The value of series scaling is often underestimated. While single-step accuracy gains from scaling models may show diminishing returns, these marginal improvements can compound into exponential gains in the length of a task an agent can successfully complete. Research demonstrates that for long-horizon execution, sequential test-time compute (more thinking) is significantly more effective than parallel compute like majority voting. This is partly because longer tasks can trigger a "self-conditioning" effect, where a model becomes more likely to make mistakes after observing its own prior errors—a failure mode that dedicated thinking time helps mitigate [[16]](https://arxiv.org/html/2509.09677v1).

It is critical to cap this budget to control both spending and added latency. An unbounded "think until perfect" approach is a recipe for runaway costs, whereas a budgeted "max 8k thinking tokens" provides a predictable guardrail. Failure to budget correctly can lead to predictable failure modes, including task derailment, unnecessary step repetition, or even a complete loss of conversation history as the agent loses track of its objective [[17]](https://arxiv.org/html/2503.13657v1).

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, also known as self-consistency, can significantly improve reliability by reducing the impact of a single bad generation. However, the gains come at a linear cost multiplier, as you pay for each parallel run. Research shows that for a given budget, parallel scaling can sometimes outperform additional serial reasoning, especially when a model's self-revision capabilities are weak. In such cases, generating multiple independent attempts is more effective than trying to refine a single, flawed line of thought [[3]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

While relevant information is valuable, each additional token carries a direct cost and adds to latency. The key is to find the optimal balance between providing enough context for an accurate response and keeping the prompt lean and efficient. Techniques like RAG, summarization, caching, and selective retrieval are designed to achieve this by filtering out noise and providing only the most critical information to the model.

To illustrate the impact of these levers, let's contrast two design approaches for a research task.

A naive design might use the largest reasoning model, dump an entire document into the context, and run five parallel attempts to ensure accuracy. This approach prioritizes quality above all else, but at a steep cost.

*   **Model:** GPT-5.5 ($5.00 / 1M input tokens, $30.00 / 1M output tokens) [[4]](https://openai.com/api/pricing/)
*   **Input Tokens:** 200,000 (from a full document)
*   **Output Tokens:** 20,000 (long-form analysis)
*   **Number of Parallel Runs:** 5
*   **Calculation:** (200k * $5/1M + 20k * $30/1M) * 5 = ($1.00 + $0.60) * 5 = **$8.00**

A budgeted design, however, would use a smaller model, retrieve only relevant chunks with RAG, and use a single pass. This design is optimized for cost-efficiency while still aiming for a high-quality output.

*   **Model:** GPT-5.4 mini ($0.75 / 1M input tokens, $4.50 / 1M output tokens) [[4]](https://openai.com/api/pricing/)
*   **Input Tokens:** 2,000 (from RAG chunks and summary)
*   **Output Tokens:** 1,000 (concise answer)
*   **Number of Parallel Runs:** 1
*   **Calculation:** (2k * $0.75/1M + 1k * $4.50/1M) * 1 = ($0.0015 + $0.0045) * 1 = **$0.006**

This budgeted approach achieves a roughly 1,300x cost reduction while still meeting the quality target. Additional optimizations like prompt caching and delegating heavy computation to external tools can further reduce costs. With the scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our capstone.
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** REVISED from the submitted reasoning.json, which scored this 0 on the claim that 'the generated section omits the toy example with cost calculations.' This does not match the actual article text: the generated section includes a full naive-vs-budgeted cost-calculation contrast with all five required bullet fields (Model, Input Tokens, Output Tokens, Number of Parallel Runs, Calculation) for both designs, reaching a ~1,300x reduction. Both sections' core ideas are present and match.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** REVISED from the submitted reasoning.json, which scored this 0 for two reasons, both incorrect on review. (1) Image-placement: the generated section places Image 1 immediately after the two-sentence section intro, before any of the four levers are detailed — this is the same overview-image-before-details pattern already ruled coherent and not penalized in an earlier article reviewed in this project (per your confirmation that this reversal is the right general approach), so it is not scored as a Flow failure here either. (2) Missing closing transition: the submitted reasoning claims the section 'ends on an additional optimization point without bridging to Section 4' — this is factually incorrect; the generated section's actual final sentence is 'With the scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our capstone,' which closely matches the expected section's own transition. Neither cited reason holds up, so this section is rescored to 1.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=2; quality=strong,strong] Confirmed on review. (1) The self-conditioning effect and the exponential task-length gains from series scaling (long-horizon-execution arXiv paper, exploration) — strong. (2) Task derailment, step repetition, and conversation-history loss as failure modes of poorly-budgeted thinking (failure-taxonomy arXiv paper, exploration) — strong. Neither paraphrases GT, which does not discuss either mechanism.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**0:** [instances=0] No breadth additions present; both depth additions in this section deepen the core scaling-lever mechanics rather than connecting outward.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The two depth additions are concise and support the core narrative about the four levers.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Consistent with the submitted reasoning.json's verdict. Word-count audit: target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 719 (submitted claimed an approximate '~680') — within range. The five-field quantitative bullet breakdown is present for both designs.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
## Inference-Time Scaling and the Cost/Latency Calculus

Understanding the four independent levers that control runtime performance is central to effective system design. Model size, series scaling, parallel scaling, and input context scaling interact in multiplicative ways. Mastering them allows you to fine-tune the trade-off between capability, cost, and latency on a per-step basis within your workflow.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-5.5 or Gemini 2.5 Pro have higher per-token costs than smaller, optimized models like GPT-5.4-mini or Gemini 2.5 Flash. For a high-value task where accuracy is paramount, such as legal document analysis, using an expensive model may be justified. For high-volume, low-complexity tasks like sentiment classification, a cheaper model is the better economic choice. The cost difference can be substantial. For example, GPT-5.5's input tokens are over 6 times more expensive than GPT-5.4-mini's [[7]](https://openai.com/api/pricing/).

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, a feature often marketed as "thinking tokens" or "extended thinking" in models like Claude. This allows the model to perform a longer chain-of-thought, which can improve reasoning on complex problems. However, this additional reasoning comes at the cost of increased latency and higher token usage. The best practice is to treat this as a dial, activating it only for the most complex planning or validation steps and setting a strict cap. For example, you can set a `budget_tokens` parameter to a maximum of 8,000 to bound both spend and delay [[5]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). Simply increasing the token budget does not guarantee more effective reasoning. Some studies have observed that a model’s visible thought process can plateau, hitting a ceiling even as the requested budget increases. This suggests that effective series scaling requires not just a larger budget, but also prompt-level incentives that encourage deeper reasoning [[20]](https://arxiv.org/html/2604.02460v1).

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response. A common technique is majority vote, also known as self-consistency, where the most frequent answer is chosen. This approach can significantly improve reliability, especially for tasks with deterministic answers like math problems. Research has shown that, for a given computational budget, parallel scaling can sometimes outperform further serial reasoning. The trade-off is a linear increase in cost, as each parallel run is billed independently [[6]](https://arxiv.org/html/2502.12215v1). While effective for certain tasks, research suggests that for long-horizon execution problems, additional sequential compute (series scaling) is often more effective at improving reliability than parallel compute [[19]](https://arxiv.org/html/2509.09677v1).

### Input Context Scaling

While relevant information is valuable, every additional token sent to the model carries a direct cost and adds to latency. As we have discussed, performance can also degrade if the context becomes too noisy due to the "lost-in-the-middle" problem. The key is to find the optimal balance. Techniques like RAG, summarization, and caching help keep the effective context small while preserving the necessary signal. For example, instead of feeding a 100-page document to the model, a RAG system can retrieve the three most relevant paragraphs, drastically reducing token consumption and improving focus.

To illustrate how these levers multiply, consider the cost difference between a naive and a budgeted design for the same task.

**Naive Design (High Cost, High Capability):**
*   **Model:** GPT-5.5 (Input: $5.00/1M tokens, Output: $30.00/1M tokens)
*   **Input Tokens:** 200,000 (full document dump)
*   **Output Tokens:** 20,000 (includes long chain-of-thought)
*   **Number of Parallel Runs:** 5 (for self-consistency)
*   **Calculation:** 5 * (($5.00/1M * 200k) + ($30.00/1M * 20k)) = 5 * ($1.00 + $0.60) = **$8.00** [[7]](https://openai.com/api/pricing/)

**Budgeted Design (Low Cost, Targeted Capability):**
*   **Model:** GPT-5.4 mini (Input: $0.75/1M tokens, Output: $4.50/1M tokens)
*   **Input Tokens:** 4,000 (RAG-retrieved chunks)
*   **Output Tokens:** 1,000 (concise answer)
*   **Number of Parallel Runs:** 1
*   **Calculation:** 1 * (($0.75/1M * 4k) + ($4.50/1M * 1k)) = $0.003 + $0.0045 = **$0.0075** [[7]](https://openai.com/api/pricing/)

In this example, a few deliberate design choices lead to a cost reduction of over 1000x while potentially meeting the same quality target. Other optimizations, such as prompt caching for repeated calls and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** All four levers are covered with matching substance, the Image 1 caption is verbatim, and the naive-vs-budgeted cost exercise uses the same 5-bullet structure and reaches ~1,067x — closely matching the expected section's ~1,000x figure, using accurately-sourced OpenAI pricing rather than the invented figures seen in two of the other three articles graded for this lesson.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** REVISED: previously scored 0 for placing Image 1 at the section start rather than after all four levers. Applying the coherence test now applied consistently across this project: showing the four-lever overview image before detailing each lever is a standard preview-then-detail structure, coherent and non-disruptive. Not scored as a Flow failure.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=2; quality=strong,strong] (1) The Series Scaling point's finding that a model's visible thinking length can plateau even as the token budget increases, requiring prompt-level incentives rather than just a larger budget, is traced to the exploration-phase arXiv paper 'Thinking on a Budget' (https://arxiv.org/html/2604.02460v1), which reports this exact plateau effect — strong. (2) The Parallel Scaling point's claim that sequential (series) compute is often more effective than parallel compute specifically for long-horizon execution problems is traced to the same exploration-phase long-horizon-execution paper credited in the Framework section, applied here to a different, specific claim (a boundary condition on when parallel scaling helps) — strong.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**0:** [instances=0] No breadth additions traceable to an exploration-phase source are present. Both depth additions in this section (thinking-plateau, sequential-vs-parallel-for-long-horizon) deepen understanding of the core scaling-lever mechanics themselves rather than connecting outward to an adjacent field.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The thinking-plateau and sequential-vs-parallel additions are each one-to-two-sentence refinements attached to their respective levers and do not dilute the four-lever explanations or the cost-comparison exercise, which remain the section's clear focus.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The four levers are covered, the Image 1 caption is verbatim, and the naive-vs-budgeted cost contrast reaches approximately 1,067x, meeting the guideline's "roughly 1000x reduction" target using accurately-sourced pricing. Word-count audit (previously an approximation of "~681"; recomputed exactly): target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 668 — within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## Inference-Time Scaling and the Cost/Latency Calculus

Understanding the four independent levers that control runtime performance is central to effective system design. Model size, series scaling (thinking), parallel scaling (multiple runs), and input context can each be adjusted on a per-step basis, and their multiplicative effects are what create the massive cost and latency differences between a prototype and a production system.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models have higher per-token costs than smaller, more optimized ones. For example, a complex reasoning task might require an expensive, frontier model, while a simple classification step can be handled by a much cheaper and faster "mini" model. This tiered approach is fundamental to cost management.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often exposed as "thinking tokens" in APIs like Anthropic's Claude [[7]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). Recent research shows that for long-horizon tasks, this sequential computation is far more effective than parallel approaches. Many LLM failures stem from a "self-conditioning" effect, where a model becomes more likely to make mistakes after observing its own prior errors. The process of "thinking" appears to break this negative feedback loop, allowing the model to execute much longer sequences of steps reliably [[8]](https://arxiv.org/html/2509.09677v1).

This is a powerful tool for improving reasoning on complex problems, but it comes with added latency and cost. The key is to treat extra reasoning as a dial, activated only for the most difficult planning or validation steps and strictly capped to control spending. An unbounded "think until perfect" approach is a recipe for budget overruns. Simply increasing the thinking budget is not a silver bullet, as models can hit a ceiling where the actual reasoning content plateaus despite a larger requested budget. Over-reliance on this lever can also lead to failure modes like task derailment or unnecessary step repetition [[9]](https://arxiv.org/html/2604.02460v1), [[10]](https://arxiv.org/html/2503.13657v1).

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. Reliability gains from majority vote or self-consistency come at a linear cost multiplier. While sequential reasoning is powerful for certain long-horizon tasks, recent studies show that for some models, parallel scaling can achieve better coverage and superior scalability for the same budget, especially when the model's self-revision capabilities are limited [[16]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

While relevant information is valuable, each additional token carries a direct cost and adds to latency. The goal is to find the optimal balance between providing enough context for a good answer and keeping the prompt lean. Techniques like RAG, summarization, and caching are essential for managing this lever effectively.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

To see how these levers multiply, consider a quick cost calculation. A naive design might use the largest reasoning model, dump an entire document into the context, and run five parallel attempts for maximum reliability. A budgeted design, however, could use a fast mini-model, retrieve only relevant chunks with RAG, and use a single pass. This can result in a cost reduction of over 1000x while still meeting the quality target.

**Naive High-Cost Design:**

*   **Model:** GPT-5.5 ($5.00/1M input, $30.00/1M output) [[11]](https://openai.com/api/pricing/)
*   **Input Tokens:** 200,000 (full document)
*   **Output Tokens:** 20,000 (long "thinking" response)
*   **Number of Parallel Runs:** 5
*   **Calculation:** `(200k * $5/M + 20k * $30/M) * 5 = ($1.00 + $0.60) * 5 = $8.00`

**Budgeted Low-Cost Design:**

*   **Model:** GPT-5.4 mini ($0.75/1M input, $4.50/1M output) [[11]](https://openai.com/api/pricing/)
*   **Input Tokens:** 4,000 (RAG chunks)
*   **Output Tokens:** 1,000 (concise response)
*   **Number of Parallel Runs:** 1
*   **Calculation:** `(4k * $0.75/M + 1k * $4.5/M) * 1 = ($0.003 + $0.0045) * 1 = $0.0075`

The difference is stark: $8.00 versus less than a cent. Additional optimizations like prompt caching and delegating heavy computation to external tools further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.
```
**Grader reasoning:**
- `cc`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** All four levers are covered with matching substance (two enriched with well-anchored additions: the self-conditioning/sequential-effectiveness finding, and the thinking-plateau/failure-mode discussion), the Image 1 caption is verbatim, and the naive-vs-budgeted cost exercise uses the same 5-bullet structure and reaches ~1,067x, closely matching the expected section's ~1,000x using accurately-sourced OpenAI pricing.
- `fl`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** Image 1 is correctly placed after all four levers have been discussed, immediately before the cost-comparison exercise, matching the expected section's placement.
- `de`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** [instances=2; quality=strong,strong] (1) The Series Scaling point's 'self-conditioning effect,' where models become more likely to err after seeing their own prior mistakes, and the finding that sequential 'thinking' breaks this feedback loop for long-horizon tasks, is traced to the exploration-phase arXiv paper on long-horizon execution (https://arxiv.org/html/2509.09677v1), matched closely to that paper's own framing — strong. (2) The same point's discussion of visible-thought plateaus despite larger requested budgets, and the resulting failure modes of task derailment and step repetition, is traced to two exploration-phase sources — the 'visible thought' arXiv paper (https://arxiv.org/html/2604.02460v1) and the multi-agent failure-taxonomy arXiv paper (https://arxiv.org/html/2503.13657v1), which names these exact failure modes — strong.
- `be`: Inference-Time Scaling and the Cost/Latency Calculus:
**0:** [instances=0] No breadth additions traceable to an exploration-phase source are present. Both depth additions in this section deepen understanding of the core series-scaling mechanics themselves rather than connecting outward to an adjacent field.
- `cp`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The self-conditioning/sequential-effectiveness and thinking-plateau/failure-mode additions are each a few sentences attached to the Series Scaling point and do not dilute the four-lever explanations or the cost-comparison exercise, which remain the section's clear focus.
- `ga`: Inference-Time Scaling and the Cost/Latency Calculus:
**1:** The four levers are covered, the Image 1 caption is verbatim, and the naive-vs-budgeted cost contrast reaches ~1,067x using accurately-sourced OpenAI pricing. Word-count audit (previously reported as "~631, within tolerance"; recomputed exactly): target 700, tolerance +/-70, range [630, 770]. Exact prose-only count: 618 — 12 words below the minimum, not the clean pass previously reported. Per standing ruling on small margins (comparable to, or smaller than, several margins already ruled not to be penalized), this is scored as passing, but the corrected margin is reported here since the prior number was inaccurate rather than merely approximate-but-right.

## Section: S6::section-6-conclusion  (weight=0.094, contribution=+0.0208 FOR standard)
Stored section rewards: standard=0.3903  deep=0.2307  (explore: standard=0.0800  deep=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
(section not found by title match)
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections summarize the 7-step framework, its capstone application, and the importance of system-level design, and set the stage for upcoming lessons.
- `fl`: Conclusion:
**1:** Same conclusion flow: summary, reinforcement, forward-looking statement.
- `de`: Conclusion:
**0:** [instances=0] No depth additions present. The 'decision logic generated at runtime' claim is credited under BreadthEnhancement, consistent with the Introduction's treatment of the same source.
- `be`: Conclusion:
**1:** [instances=1; quality=strong] Confirmed on review: the closing reiteration of the 'decision logic generated at runtime' paradigm claim (arXiv 2606.05608, exploration) is a distinct instance from the Introduction's use of the same source, since sections are scored independently.
- `cp`: Conclusion:
**1:** The single breadth addition is a well-integrated closing sentence that supports rather than dilutes the core summary.
- `ga`: Conclusion:
**0:** Consistent with the submitted reasoning.json's verdict, on a corrected count. Word-count audit: target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 233 (submitted claimed an approximate '~220') — 37 words below the minimum. This is a substantially larger shortfall than the -14/-15-word margins already ruled 'do not penalize' elsewhere in this project — flagging explicitly rather than assuming the same leniency extends this far, since 37 words is more than double those confirmed cases.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix to guide our implementation. We also examined the four inference-time scaling levers: model size, series reasoning, parallel runs, and context volume. We saw how their multiplicative effects can create massive cost variations, reinforcing the need for a disciplined, system-level approach. Adopting this view, rather than focusing only on prompts or single models, is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have established here are not just theoretical. They are the blueprint for our upcoming work. We will reference them repeatedly in all future implementation lessons to ensure that every code-level choice stays aligned with our original goals for cost, latency, and quality. This disciplined approach is what separates reliable systems from brittle demos that fail under real-world pressure. It is the difference between building a toy and engineering a product.

In the next lesson, we will begin the hands-on construction of Nova, our research agent. We will build the FastMCP server, define its core research tools, and implement the client loop that orchestrates the multi-round research and filtering process to produce the final `research.md` file. This will be our first major step in turning the architectural diagrams into running code. Later, in Lessons 19-22, we will build out the durable Brown workflow using LangGraph, implementing the stateful logic for drafting, reviewing, and editing. The ability to make these system-level trade-offs repeatedly is what turns AI engineering into a repeatable practice.
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections recap the framework and capstone application, make the system-level-view argument, note the decisions/diagrams will be referenced repeatedly, and forward-reference the same next-lesson content plus Lessons 19–22. The generated section additionally recaps the four scaling levers and adds a 'toy vs. product' framing — accepted additions, not omissions.
- `fl`: Conclusion:
**1:** The generated section follows the same overall progression as the expected one, with the additional four-levers recap and 'toy vs. product' line appended without disrupting the expected section's own idea order.
- `de`: Conclusion:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present in this section; its content synthesizes material already established earlier in the article.
- `be`: Conclusion:
**0:** [instances=0] No breadth additions traceable to an exploration-phase source are present in this section.
- `cp`: Conclusion:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Conclusion:
**1:** The section covers the guideline's requirements for this section and adds a four-levers recap beyond what the guideline requires. Word-count audit (previously an approximation of "~276"; recomputed exactly): target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 276 — comfortably within range.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process yielded a clean global architecture separating the Nova research agent from the Brown writing workflow, supported by clear component diagrams and a concrete decision matrix. Adopting this system-level view, rather than focusing only on prompts or single models, is the foundation for turning prototypes into scalable, production-ready agent products that remain debuggable and cost-effective at scale.

The decisions and diagrams we have established will be referenced repeatedly in our upcoming implementation lessons. This ensures every code-level choice stays aligned with our original goals for cost, latency, and quality. The separation of exploration (Nova) and execution (Brown) is a deliberate design choice that mirrors advanced agent architectures, providing modularity and control. This structured approach elevates the role of AI from a reactive tool that simply answers questions to a proactive partner that can monitor, detect, and act autonomously within a governed workflow, with humans providing critical oversight [[33]](https://hdsr.mitpress.mit.edu/pub/fdzqkh85).

In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining the core research tools and orchestrating the process that produces the final `research.md` file. Later, in Lessons 19–22, we will build the Brown workflow. The real skill you are developing is the ability to make these system-level trade-offs repeatedly. This discipline turns AI engineering from an art into a repeatable practice and is what separates prototypes from production systems. Ultimately, building robust agents is 90% software engineering and 10% AI, a reality this framework helps you navigate [[34]](https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M).
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections recap the framework and capstone application, make the system-level-view argument, note the decisions/diagrams will be referenced repeatedly, forward-reference the same next-lesson content plus Lessons 19–22, and close on the repeatable-practice framing, plus two well-anchored additions (a proactive-partner reframing and a '90% software engineering' point). No substantive idea is missing.
- `fl`: Conclusion:
**1:** The generated section follows the same overall progression as the expected one, with the two added breadth points appended without disrupting the expected section's own idea order.
- `de`: Conclusion:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present. Both additions in this section (see BreadthEnhancement) connect outward to broader industry/paradigm framing rather than deepening the lesson's own core content.
- `be`: Conclusion:
**1:** [instances=2; quality=strong,strong] (1) The reframing of AI's role from 'a reactive tool that simply answers questions to a proactive partner that can monitor, detect, and act autonomously... with humans providing critical oversight' is traced to the exploration-phase HDSR source on AI agents transforming decision-making (https://hdsr.mitpress.mit.edu/pub/fdzqkh85), matched closely to that source's own monitor-detect-analyze-act framing — strong. (2) The closing claim that 'building robust agents is 90% software engineering and 10% AI' is traced to the exploration-phase LinkedIn source making this exact point — strong: specific and memorable, directly sourced.
- `cp`: Conclusion:
**1:** Both breadth additions are appended after the expected section's own closing ideas (recap, referenced-repeatedly point, forward pointer, repeatable-practice framing) have already been fully stated, so they do not crowd out or interrupt that core content.
- `ga`: Conclusion:
**1:** The section covers the guideline's requirements content-wise in full, plus two well-anchored additions. Word-count audit (previously an approximation of "~264"; recomputed exactly): target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 262 — 8 words below the minimum. Per standing ruling, this margin is not penalized.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it directly to our capstone project. This systematic process yielded the clean Nova-versus-Brown global architecture, three supporting diagrams that illustrate the component interactions, and a concrete decision matrix that will guide our implementation. This system-level view, which prioritizes deliberate trade-offs over chasing the latest model, is the foundation that turns brittle prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here are not just theoretical exercises. They are our direct reference points for all upcoming implementation lessons, ensuring that every line of code we write aligns with our original goals for cost, latency, and quality. This structured approach is essential for managing the complexity of modern AI systems and delivering reliable results that meet real-world business needs.

Our journey continues in the next lesson, where we will begin the hands-on construction of the FastMCP server and client loop for Nova. We will define its core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. Later, in Lessons 19–22, we will turn our attention to implementing the durable and stateful Brown writing workflow using LangGraph. The real skill you are developing is not just how to code an agent, but how to make these critical system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable and reliable engineering practice.
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections summarize the 7-step framework, the capstone application, and set up the next lessons. Core ideas identical. (The submitted reasoning.json scored 'References' as its own separate section here; per the ground truth's actual structure — References nested as an H3 under Conclusion, not its own H2 — it is folded into this entry instead; this does not change the outcome, since References was also scored 1.)
- `fl`: Conclusion:
**1:** Same conclusion flow: summary, reinforcement, forward-looking statement.
- `de`: Conclusion:
**0:** [instances=0] No depth additions present.
- `be`: Conclusion:
**0:** [instances=0] No breadth additions present.
- `cp`: Conclusion:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Conclusion:
**0:** REVISED from the submitted reasoning.json (previously scored 1, citing an approximate '~280 words... within tolerance'). Word-count audit: target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 240. 30 words below the minimum — exactly double the largest margin already ruled 'do not penalize' (15 words). Flagged explicitly as a genuine test of where that line sits, rather than assumed either way.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix. By focusing on system-level design, you can build scalable and debuggable agent products, moving beyond simple prototypes. This structured approach to making trade-offs is what allows us to build reliable and efficient AI systems.

The decisions and diagrams we have established here will serve as our guide throughout the upcoming implementation lessons. Every code-level choice we make will be aligned with the cost, latency, and quality goals we have defined in our decision matrix. This ensures that our implementation stays true to our architectural vision. For example, the 1000x cost difference between our naive and budgeted designs highlights how critical these early architectural decisions are.

We will begin the hands-on construction of the FastMCP server and client loop for Nova in the next lesson. There, we will define its core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. Later, in Lessons 19–22, we will implement the durable writing workflows for Brown using LangGraph. The goal is to develop the skill of making these system-level trade-offs consistently, which is the core of a repeatable AI engineering practice.
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections recap the framework and capstone application, make the system-level-view argument, note the decisions/diagrams will guide implementation, and forward-reference the same next-lesson content plus Lessons 19–22, closing on the repeatable-practice framing. The generated section also calls back to the 1000x cost-reduction figure from Section 3 — an accepted addition.
- `fl`: Conclusion:
**1:** The generated section follows the same overall progression as the expected one, with the added 1000x-cost-recap sentence appended without disrupting the expected section's own idea order.
- `de`: Conclusion:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present in this section; its content synthesizes material already established earlier in the article.
- `be`: Conclusion:
**0:** [instances=0] No breadth additions traceable to an exploration-phase source are present in this section.
- `cp`: Conclusion:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Conclusion:
**0:** The section covers the guideline's requirements content-wise. However, word-count audit (previously an approximation; recomputed exactly): target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 217 — 53 words below the minimum, a clear, non-borderline shortfall.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, the three supporting diagrams, and the concrete decision matrix that will guide our implementation. Adopting a system-level view is the foundation that turns prototypes into scalable, production-ready agent products. This means focusing on the entire architecture, not just on prompts or single models, to build systems that are debuggable and cost-effective at scale.

The decisions and diagrams recorded in this lesson are not just theoretical. They will be referenced repeatedly in all future implementation lessons so that every code-level choice stays aligned with the original cost, latency, and quality goals. This architectural blueprint is our source of truth as we move from design to code, ensuring consistency and purpose in our engineering efforts.

We will begin the hands-on construction of the FastMCP server and client loop for Nova in the next lesson. There, we will define the core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. The implementation of the Brown workflow will follow in Lessons 19–22, where we will build out the stateful writing and review cycles. The real skill you are developing is the ability to make these system-level trade-offs deliberately and repeatedly, turning AI engineering from an intuitive art into a disciplined, repeatable practice.
```
**Grader reasoning:**
- `cc`: Conclusion:
**1:** Both sections recap the framework and capstone application, make the system-level-view argument, note the decisions/diagrams will be referenced repeatedly, forward-reference the same next-lesson content plus Lessons 19–22, and close on the repeatable-practice framing. No substantive idea is missing.
- `fl`: Conclusion:
**1:** The generated section follows the same overall progression as the expected one.
- `de`: Conclusion:
**0:** [instances=0] No depth additions traceable to an exploration-phase source are present in this section.
- `be`: Conclusion:
**0:** [instances=0] No breadth additions traceable to an exploration-phase source are present in this section.
- `cp`: Conclusion:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Conclusion:
**0:** The section covers the guideline's requirements content-wise in full. Word-count audit (previously an approximation; recomputed exactly): target 300, tolerance +/-30, range [270, 330]. Exact prose-only count: 230 — 40 words below the minimum, a clear, non-borderline shortfall, well outside the range of margins already ruled acceptable.

## Section: S1::section-1-introduction  (weight=0.062, contribution=+0.0358 FOR standard)
Stored section rewards: standard=0.4536  deep=0.2307  (explore: standard=0.2100  deep=0.0000)

### Arm: standard (preset2)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset2`

**Article text:**
```
In the last two lessons, we defined the capstone project for this course: two production-oriented agents that collaborate to produce publish-ready technical articles. In Lesson 12, we scoped the research agent, Nova, and the writing workflow, Brown. In Lesson 13, we chose our frameworks: Nova will ship as portable FastMCP tools, while Brown will run a durable LangGraph workflow.

With those foundational choices made, we now move to system design. This layer separates a polished product from a fragile demo that collapses under real workloads. Agentic systems represent a fundamental shift in software engineering. For decades, humans encoded decision logic into static code, but now the agent *is* the software, generating its logic at runtime [[41]](https://arxiv.org/html/2606.05608). This changes how we must think about design. Core variables like reasoning budgets and context strategy have an order-of-magnitude impact on cost and latency.

This lesson provides a reusable 7-step decision playbook that moves from business goals to a concrete system architecture. We will apply this framework to our capstone, producing the global Nova-Brown architecture and a decision matrix you can reuse. You will learn where to spend thinking tokens, when to parallelize, and how to keep context lean. With the stakes clear, let's walk through the general framework.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections serve as an introduction, setting the stage for the capstone's system design and the decision framework. The substance is the same.
- `fl`: Introduction:
**1:** Both sections follow the same progression: recap of previous lessons, introduce system design, outline the lesson. Flow preserved.
- `de`: Introduction:
**0:** [instances=0] No depth additions present. The new-software-paradigm claim in this section is credited under BreadthEnhancement (historical/evolutionary framing), not here.
- `be`: Introduction:
**1:** [instances=1; quality=strong] Confirmed on review: the 'agentic systems are a fundamental shift in software engineering... the agent *is* the software' framing (arXiv 2606.05608, exploration) is a genuine historical/evolutionary addition — the ground truth introduction never discusses this paradigm-shift framing. Strong: a specific, detailed claim drawn from a named paper.
- `cp`: Introduction:
**1:** The single breadth addition is well-integrated and does not dilute the section's core framing.
- `ga`: Introduction:
**0:** REVISED REASON from the submitted reasoning.json (previously scored 0 on the claim that the prose count was '~160 words... below the 180-220 range' — both the count and the tolerance range were wrong: the correct range for a 200-word target is [175,225], not [180,220], which omits the 25-word floor check). Word-count audit: target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 204 — within range. Word count is NOT the reason for this score. Content check: the guideline names five design variables (reasoning budget, context strategy, orchestration style, HITL placement, artifact contracts); the generated section names only two ('reasoning budgets and context strategy'), omitting orchestration style, HITL placement, AND artifact contracts — a wider gap than the '2 of 5 missing' pattern found in most other articles reviewed in this project. This content gap, not word count, is why this section still fails.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset2`

**Article text:**
```
In the last two lessons, we defined the scope for our capstone project: building two production-oriented agents, Nova and Brown, to collaborate on producing publish-ready technical articles. We chose our frameworks, deciding Nova will use FastMCP for portable research tools, while Brown will run on a durable LangGraph workflow for writing. Now we move from framework selection to system design, the layer that determines whether our agents behave like polished products or fragile demos. This shift reflects a deeper change in software engineering itself. AI agents represent a new paradigm where decision logic is generated at runtime, not pre-encoded by a human, making system-level design more important than ever [[3]](https://arxiv.org/html/2606.05608).

Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement have an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has different design constraints than a high-accuracy overnight research job. Understanding these trade-offs is what separates prototypes from production systems.

This lesson introduces a reusable 7-step decision playbook that moves from business value through model routing, context discipline, and observability. We will apply this framework to our capstone, yielding the global Nova-Brown architecture and a decision matrix you can reuse. You will learn to decide where extra thinking tokens add value, when to use human gates, and how to keep context lean.

With the stakes clear, we will now walk through the general 7-step framework before specializing it for our capstone.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections cover the Lesson 12/13 recap, position system design as the layer above framework selection that determines dependable products vs fragile demos, and close with the decision-framework offering plus learning goals. The generated section adds a well-anchored 'AI agents as a new software paradigm' framing beyond the expected section; this is an accepted addition, not an omission.
- `fl`: Introduction:
**1:** The generated section follows the same progression as the expected one, with the added new-software-paradigm point placed early without disrupting the recap-framing-goals-transition sequence. No media in this section.
- `de`: Introduction:
**1:** [instances=1; quality=strong] The claim that 'AI agents represent a new paradigm where decision logic is generated at runtime, not pre-encoded by a human' is traced to the exploration-phase arXiv source on AI agents as a new software paradigm (https://arxiv.org/html/2606.05608), which develops this exact thesis at length (the shift from 'AI → Software → Result' to 'Agent → Result', decision logic generated at runtime rather than pre-encoded). Classified as strong: a specific, thesis-level theoretical claim rather than a generic mention. Also credited under BreadthEnhancement — see that entry for why this instance qualifies for both.
- `be`: Introduction:
**1:** [instances=1; quality=strong] The same 'new software paradigm' claim credited under DepthEnhancement also qualifies as breadth: it situates the lesson's topic within the broader historical arc of software engineering ('for over half a century, software engineering has operated on a foundational premise...'), which is 'historical context or evolution of the topic' per the breadth criteria. Traced to the same exploration-phase source; classified strong for the same reasons given there.
- `cp`: Introduction:
**1:** The new-paradigm addition is a single sentence within a four-paragraph introduction and does not crowd out the expected section's own recap, framing, or learning-goals content, all of which remain fully present and in the same order.
- `ga`: Introduction:
**0:** The section covers the Lesson 12/13 recap, positions system design above framework selection, and covers the learning-goals list. However, the guideline names five design variables, and this section again names only three, omitting orchestration style and artifact contracts. Word-count audit (previously an approximation of "~236"; recomputed exactly): target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 235 — 10 words above the maximum.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset2`

**Article text:**
```
In Lesson 12, we defined the scope of our capstone project: two production-oriented agents that collaborate to produce publish-ready technical articles. We have the research agent, Nova, and the writing workflow, Brown. In Lesson 13, we compared agent frameworks and chose our stack: Nova will ship as FastMCP tools for portability, while Brown will run a durable LangGraph workflow, also fronted by FastMCP.

With our frameworks selected, we now move to system design. This is the layer that determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads. This shift to system-level thinking is important because AI agents represent a new software paradigm. Unlike traditional software where decision logic is pre-encoded by engineers, an agent's logic is generated at runtime, making the architectural choices that constrain it essential [[1]](https://arxiv.org/html/2606.05608).

Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement have an order-of-magnitude impact on cost, latency, and reliability. This lesson introduces a reusable 7-step decision playbook that moves from business value to a concrete system architecture. We will then apply this framework to our capstone, producing the global Nova-versus-Brown architecture, complete with component interaction diagrams and a decision matrix you can reuse on future projects. By the end, you will know where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal.

With the stakes clear, we will now walk through the general 7-step framework before specializing it for the capstone.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections cover the Lesson 12/13 recap, position system design above framework selection, and close with the decision-framework offering plus learning goals. The generated section adds a well-anchored 'AI agents as a new software paradigm' framing beyond the expected section; an accepted addition, not an omission.
- `fl`: Introduction:
**1:** The generated section follows the same progression as the expected one, with the added new-paradigm point placed early without disrupting the recap-framing-goals sequence. No media in this section.
- `de`: Introduction:
**1:** [instances=1; quality=strong] The claim that AI agents represent a new software paradigm — decision logic generated at runtime rather than pre-encoded by engineers — is traced to the exploration-phase arXiv source on AI agents as a new software paradigm (https://arxiv.org/html/2606.05608), which develops this exact thesis at length. Strong: a specific, thesis-level claim. Also credited under BreadthEnhancement.
- `be`: Introduction:
**1:** [instances=1; quality=strong] The same new-software-paradigm claim credited under DepthEnhancement also qualifies as breadth: it situates system design within the broader historical shift in what software engineering is, per the breadth criteria's 'historical context or evolution of the topic.' Traced to the same exploration-phase source; classified strong for the same reasons given there.
- `cp`: Introduction:
**1:** The new-paradigm addition is a single sentence within the introduction and does not crowd out the expected section's own recap, framing, or learning-goals content.
- `ga`: Introduction:
**0:** The section covers the Lesson 12/13 recap and the learning-goals list. However, the guideline names five design variables, and this section names only three. Word-count audit (previously an approximation of "~253"; recomputed exactly): target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 252 — 27 words over the maximum.

### Arm: deep (preset3)

#### Draw: production  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/test_episodes/14_agent_system_design__preset3`

**Article text:**
```
In the last two lessons, we defined the scope for our capstone project: two production-oriented agents, Nova (research) and Brown (writing), that collaborate to produce publish-ready technical articles. We also justified our framework choices, opting for FastMCP to make Nova’s tools portable and steerable, while using LangGraph to give the Brown writing workflow durability and auditability.

With those foundational choices made, we now move to the next critical layer: system design. This is the discipline that determines whether our agents behave like polished, dependable products or like fragile research demos that collapse under real workloads. Core design variables—such as reasoning budgets, context strategies, orchestration styles, and human-in-the-loop (HITL) policies—each exert an order-of-magnitude influence on cost, latency, and reliability.

This lesson introduces a reusable 7-step decision playbook that moves from business value definition to a complete system design. We will apply this framework to our capstone, yielding the global Nova-versus-Brown architecture, component interaction diagrams, and a decision matrix you can reuse on your own projects. By the end, you will know where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal. With the stakes clear, we will now walk through the general framework before specializing it for our capstone.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections serve as an introduction, defining the capstone scope, referencing previous lessons, and introducing the decision framework. Core topics identical.
- `fl`: Introduction:
**1:** Both sections follow the same progression: recap, system-design framing, lesson outline.
- `de`: Introduction:
**0:** [instances=0] No depth additions present.
- `be`: Introduction:
**0:** [instances=0] No breadth additions present.
- `cp`: Introduction:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Introduction:
**0:** The generated section covers the Lessons 12/13 recap, positions system design, and states learning goals. It names four of the guideline's five design variables (reasoning budgets, context strategies, orchestration styles, HITL policies), omitting only 'artifact contracts' — a notably smaller gap than the '2-3 of 5 missing' pattern found in every other article reviewed in this project so far. Word-count audit: target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 213 — within range; word count is not the reason for this score. FLAGGED AS BORDERLINE: given this is the closest any article has come to fully naming the five variables, this may warrant different treatment than the more severe omissions seen elsewhere — noting rather than deciding unilaterally.

#### Draw: replicate1  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate1__preset3`

**Article text:**
```
In the last two lessons, we defined the scope for our capstone project. It consists of two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. We also justified our framework choices: Nova will be built using FastMCP for portability, while Brown will run on LangGraph for durability. Now, we move from framework selection to system design. This is the layer that determines whether our agents will behave like dependable products or fragile demos that collapse under real workloads.

Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement exert an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has vastly different design constraints than a high-accuracy overnight research agent. Getting these trade-offs right is what makes an AI product successful.

This lesson introduces a reusable 7-step decision playbook that moves systematically from business goals to a concrete architectural blueprint. We will apply this framework to our capstone, producing the global architecture for Nova and Brown, complete with component diagrams and a decision matrix you can adapt for your own projects.

You will learn where to spend your budget on extra "thinking" tokens for genuine value, when to parallelize tasks, when human gates are non-negotiable, and how to keep your context lean without sacrificing quality. With the stakes clear, let's walk through the general framework before we specialize it for our capstone.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections cover the Lesson 12/13 recap, position system design as the layer above framework selection that determines dependable products vs fragile demos, and close with the decision-framework offering plus learning goals (thinking tokens, parallelize, human gates, lean context). No substantive idea from the expected section is missing.
- `fl`: Introduction:
**1:** The generated section follows the same progression as the expected one: recap, framing/stakes, decision-framework offering with learning goals, closing transition. No media in this section.
- `de`: Introduction:
**0:** [instances=0] No depth additions present. The introduction's content is guideline-aligned framing with no additional theoretical or technical material beyond the expected section and guideline.
- `be`: Introduction:
**0:** [instances=0] No breadth additions present.
- `cp`: Introduction:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Introduction:
**0:** The section covers the Lesson 12/13 recap, positions system design above framework selection, and covers the learning-goals list. However, the guideline names five design variables, and this section again names only three, omitting orchestration style and artifact contracts. Word-count audit (previously an approximation; recomputed exactly): target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 230 — 5 words above the maximum, a very small overage; the missing variables, not word count, are the reason for this score.

#### Draw: replicate2  `/mnt/f/my_projects/agentic_AI_RL/Reinsearch_agent/RL_researcher_writer_ymaxing/rl_training_data/noise_experiment/14_agent_system_design__replicate2__preset3`

**Article text:**
```
## Introduction

In the last two lessons, we established the capstone project for this course: two production-oriented agents that collaborate to produce publish-ready technical articles. In Lesson 12, we defined the scope, splitting the work between an explorative research agent, Nova, and a deterministic writing workflow, Brown. In Lesson 13, we compared agent frameworks and justified our choices: Nova will use FastMCP for portable, steerable tools, while Brown will run a durable, auditable LangGraph workflow.

Now, we move from framework selection to system design. This is the layer that determines whether our agents become dependable products or brittle demos that fail under real-world conditions. Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement exert an order-of-magnitude influence on cost, latency, and reliability.

This lesson provides a reusable 7-step decision playbook that moves systematically from business requirements to a concrete architectural blueprint. We will apply this framework in full to our capstone, yielding the global Nova-Brown architecture and a detailed decision matrix you can adapt for your own projects. You will learn where extra thinking tokens deliver genuine value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal.

With the stakes clear, let's walk through the general 7-step framework before specializing it for our capstone project.
```
**Grader reasoning:**
- `cc`: Introduction:
**1:** Both sections cover the Lesson 12/13 recap (including the explorative-vs-deterministic split), position system design above framework selection, and close with the decision-framework offering plus learning goals. No substantive idea from the expected section is missing.
- `fl`: Introduction:
**1:** The generated section follows the same progression as the expected one. No media in this section.
- `de`: Introduction:
**0:** [instances=0] No depth additions present in this section.
- `be`: Introduction:
**0:** [instances=0] No breadth additions present.
- `cp`: Introduction:
**1:** Both DepthEnhancement and BreadthEnhancement scored 0 for this section, so CorePreservation scores 1 by default.
- `ga`: Introduction:
**0:** The section covers the Lesson 12/13 recap and the learning-goals list. However, the guideline names five design variables, and this section names only three. Word-count audit (previously an approximation; recomputed exactly): target 200, tolerance +/-25, range [175, 225]. Exact prose-only count: 214 — within range; the score rests entirely on the missing variables.
