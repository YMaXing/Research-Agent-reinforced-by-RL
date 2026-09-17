## Global Context of the Lesson

### What We Are Planning to Share

We will introduce a reusable 7-step AI engineering decision framework that guides you from initial problem statement through balanced agent system design, explicitly weighing capability, cost, latency, and reliability. We will examine the four inference-time scaling levers (model size, series reasoning via thinking tokens, parallel runs, and context volume) and demonstrate how their multiplicative effects create orders-of-magnitude differences in spend and performance, using naive versus budgeted cost examples. We will then apply the full framework to the capstone project, producing a global two-agent architecture that cleanly separates an exploration-focused Nova MCP agent from an execution-focused Brown LangGraph workflow, complete with component flows, file-based artifact contracts, HITL triggers, and a concrete decision matrix of defaults with explicit rationales. Throughout we emphasize separation of concerns, precise tool boundaries, context discipline, and observability so that the resulting system remains debuggable and production-ready.

### Why We Think It's Valuable

System-level choices around reasoning budgets, context control, orchestration style, and HITL determine whether agents become production systems or remain brittle demos. This lesson supplies you with a repeatable playbook and concrete levers that can swing cost and latency by 1000x while preserving quality and debuggability. By the end you will know exactly where to spend extra thinking tokens, when to insert human gates, how to keep context lean, and how to document those decisions so implementation stays aligned with business goals.

### Expected Length of the Lesson
**3,200 words**

### Theory / Practice Ratio

100% theory - 0% practice

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 3 parts, each with multiple lessons. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view.
- To not reintroduce concepts already thought in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons.
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

Lesson 14 sits after capstone scoping and framework selection (Lessons 12-13) plus earlier coverage of context, orchestration, and patterns (Lessons 2, 3, 9); it supplies the global design blueprint and decision matrix before hands-on Nova implementation begins in Lesson 15 and Brown construction in Lessons 19-22.

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

AI engineers who have completed prior lessons on LLM fundamentals, RAG, agent patterns, LangGraph, MCP, and the capstone outline and are now ready to learn architectural trade-offs before coding production agents.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:
**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents
- **Lesson 11 - Multimodal Data**: Foundations and Implementations of Multimodal LLMs

**Part 2:**

- **Lesson 12 - Central Project: Scope & Design**: Introducing the scope and design of the central project
- **Lesson 13 - Agent Frameworks Overview & Comparison**: Dimensions of choosing suitable a agent framework, justifying the choices made for our central project

As this is the third lesson in Part 2 - Building Agentic Systems, after we introduced the scope and design of the central project of our course, and then justified the choices we made in the best agent framework for the research and writer agents, we will zoom rom framework choice to system design to present a decision framework one can reuse for any agent project, then apply it to our agents - Nova and Brown.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:
- Hands-on construction of FastMCP server exposing research tools, client loop, and Nova's iterative research recipe (next lesson)
- Implementation of LangGraph stateful workflows for Brown, exposure as MCP tools, and evaluator-optimizer cycles (Lessons 19-22)
- Practical integration of HITL gates, context strategies, artifact contracts, and evaluation loops into running code

When you must reference these ideas, keep the explanation extremely high-level and intuitive, note that full implementation details appear in the listed lessons, and never dive into code patterns or inner workings.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in it's educational journey it's critical for this piece. You have to use only previous introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using them, use intuitive analogies and or explanations that are more general and easier to understand, as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer to them as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer to it as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection, only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are just allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection, explicitly specify in what lesson it will be explained in more detail, leveraging the particulars from the subsection. If not explicitly specified in the subsection, simply state that we will cover it in future lessons without providing a concrete lesson number. 

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
	- Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline

1. Introduction
2. A General AI Engineering Decision Framework
3. Inference-Time Scaling and the Cost/Latency Calculus
4. Our Capstone: Global System Design
5. Decision Matrix & Defaults for the Capstone
6. Table 1: Decision matrix for the capstone project
7. Conclusion

## Section 1 - Introduction

- Introduce the course by anchoring it to the capstone project defined in the last two cources: In Lesson 12, the scope of the project is defined as the two production‑oriented agents that collaborate to produce publish‑ready technical articles - the _research_ agent (Nova) and the _writing_ workflow (Brown), the split between the designs of an explorative research agent and a deterministic writing workflow is also shown. In Lesson 13, various agent frameworks were introduced and compared across 4 dimensions. The choices of the frameworks: Nova ships as FastMCP tools (portable, steerable), while Brown runs a LangGraph workflow (durable, auditable), fronted by FastMCP for tool access.
- Position **system design** as the distinct layer that sits above framework selection (FastMCP plus LangGraph) and determines whether the resulting agents behave like polished, dependable products or fragile research demos that collapse under real workloads.
- Show how core design variables (reasoning budget, context strategy, orchestration style, HITL placement, artifact contracts) each exert order-of-magnitude leverage on total cost, latency, context growth, and parallelization; illustrate with contrasting examples of a real-time support bot versus a high-accuracy overnight research job.
- Preview the reusable 7-step decision playbook that moves systematically from business value definition through model routing, context discipline, orchestration choice, HITL policy, tool boundaries, and observability requirements.
- Directly signal that the playbook will be applied in full to the capstone, yielding the global Nova-versus-Brown architecture, component interaction diagrams, and a decision matrix you can reuse on future projects.
- State the concrete learning goals: you will leave able to decide where extra thinking tokens deliver genuine value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal.
- Transition to Section 2: With the stakes clear, we now walk through the general 7-step framework before specializing it to the capstone.

-  **Section length:** 200 words

## Section 2 - A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. Use this step‑by‑step playbook to move from a problem statement to a design that balances capability, cost, and reliability.

- **Define Value, Constraints, Cost & Latency:** explicitly define success criteria, including the output quality bar, privacy or compliance requirements, expected volume, and your per-task spending limits; use examples to contrast a real-time support bot (sub-second latency, moderate accuracy acceptable) with a high-accuracy batch research job (throughput measured in hours, near-zero hallucination tolerance) to show how targets dictate every downstream choice.

- **Choose Model Family & Capability Mix:** when to prefer closed APIs that deliver SOTA performance and low operational overhead versus open-weight models that guarantee privacy, customization, and data-locality; include failure modes of each path (vendor lock-in versus GPU management burden) with examples.

- **Define Your Context Strategy:** Mention that, as seen in previous lessons, a large context window is not always a good solution. It is a common mistake to dump everything into a prompt and then assume the LLM can handle it. Then use the source [lost-in-the-middle](<https://arxiv.org/abs/2307.03172>) to explicitly call out such mistake leads to the lost-in-the-middle performance cliff. Emphasize prioritizing selective retrieval, compression, and structured summaries to manage cost and improve reliability instead of the naive full-document dump. Insert at least one example where a sliding window or summarization is the suitable approach remember the latest information, and another example where RAG is used to identify and retrieve the most relevant information.

- **Pick an Orchestration Style:** use predictable workflows when steps are auditable and linear, dynamic agents when open-ended tool use is required, and hybrid designs for systems that contain both; reference earlier coverage of orchestration styles without re-explaining mechanics, but with examples.

- **Establish a HITL & Evaluation Loop:** HITL triggers, confidence gates, and custom evaluation design versus full autonomy; tie the decision to error cost and business risk, giving concrete triggers (e.g., any research query above a certain ambiguity threshold, final article sign-off). Use contrasting examples to showcase defining clear triggers for human intervention, such as low-confidence scores, sensitive actions, or policy flags.

- **Set Tool Boundaries & Portability:**: keep the LLM responsible solely for intent detection and high-level orchestration while delegating deterministic math, heavy lifting, or validation to code, add an example to explain that; also explain how MCP enforces clean portability across clients and IDEs without tying implementation to any single vendor.

- **Choose Durability & Observability:** for long-running stateful jobs demand resumability, checkpoints, and full tracing; for stateless retry loops a simple retry policy suffices; link each choice back to the original success criteria defined in Step 1, also add contrasting examples to show when built-in checkpoints, resumability, and detailed tracing are necessary and when they are not.

- Throughout, emphasize that the framework is iterative: you will revisit earlier steps as new constraints surface during later implementation.

- Transition to Section 3: Once the high-level decisions are framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget them deliberately.

-  **Section length:** 1000 words

## Section 3 - Inference-Time Scaling and the Cost/Latency Calculus

- Introduce the four independent runtime levers: model size (parameter count and intelligence), series scaling (extra thinking tokens or chain-of-thought length), parallel scaling (self-consistency or majority-vote runs), and input-context scaling (tokens of retrieved or summarized material). Emphasize understanding how they interact and multiply is central to effective system design and each can be adjusted on a per-step basis within a workflow.

- **Model Size Scaling:** the most straightforward lever. Larger, more capable models have higher per-token costs than smaller, more optimized models. Use constrasting real examples to show when to use expensive or cheap models. 

- **Series Scaling:** This refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens". treat extra reasoning steps as a dial that is activated only for the most complex planning or validation steps and strictly capped to bound both spend and added latency; contrast unbounded “think until perfect” versus budgeted “max 8k thinking tokens.”

- **Parallel Scaling:** This involves running the same prompt multiple times in parallel and selecting the best response, typically through a majority vote (a technique known as self-consistency). Reliability gains from majority vote or self-consistency come at a linear cost multiplier; cite research showing that, beyond a certain point, parallel scaling can outperform additional serial reasoning for the same budget.

- **Input Context Scaling:** relevant information is valuable but each additional token carries direct cost and indirect latency, the key is to find the optimal balance; show how RAG, summarization, caching, and selective retrieval keep the effective context small while preserving signal.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies."

- Present a toy cost-calculation contrast: naive design (largest reasoning model, entire document dumped in context, five parallel runs) versus budgeted design (mini fast model, RAG plus summary, single pass) that yields roughly 1000× reduction while meeting the same quality target. In either of the two cost-calculations in the contrast, in the form of bullet points, quantitively present at least five aspects - **Model**, **Input Tokens**, **Output Tokens**, **Number of Parallel Runs** and **Calcualtion**.

- Additional optimizations that keep LLM context small and focused: per-step reasoning caps, prompt caching across similar calls, and explicit tool delegation that moves heavy computation outside the model entirely.

- Transition to Section 4: With the scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for the Nova/Brown capstone.

-  **Section length:** 700 words

## Section 4 - Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces."

- use the above image to illustrate the core architectural principle of our capstone: enforce clean separation of concerns between unpredictable, open-ended research (handled by Nova as an MCP agent) and predictable, iterative drafting plus review (handled by Brown as a stateful LangGraph workflow); this separation prevents context bloat and makes each component easier to debug and evolve independently. Make the transition to the following parts where each component is examined in greater detail, starting with the research agent, Nova.

- Start a subsection with an H3 title "Research Agent (Nova)":
Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable. A simple **MCP client** then runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt.
For the MCP client, we use **FastMCP’s built-in**`**Client**`**class,** a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details (capability discovery, tool calling, resource fetching) out of the box. Our implementation is just ~200 lines of Python that wrap FastMCP’s `Client`: it connects to the server (via in-memory or stdio transport), fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 3: End-to-end agent flow for the Nova Research Agent"

- Start a subsection with an H3 title "Writing Workflows (Brown)":
Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this powerful engine with a **FastMCP server** , which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.
The exposed tools are:

    - **Generate Article:** This orchestrates the following workflow: loads context (guidelines, research, profiles, examples), generates media items using the orchestrator-worker pattern, writes the first draft, then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.

    - **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.

    - **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining context awareness of the full document.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow."

- The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean separation of concerns makes the system modular, debuggable, and easier to maintain.

- The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what it wants to write, the narrative of the article, personal notes or anything else that it considers important. As the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. 

- If the ideas are not clearly enumerated and connected, the output will be sloppy. Expand on why the article guideliens should be as detailed as possible: leaving too many gaps for the AI to fill without instructions leads to LLM generating hollow texts. LLMs are amazing at translation, but terrible at generating original ideas.

- Transition to Section 5: The architecture and diagrams are now concrete; the final step is to translate the framework principles into an explicit, implementable decision matrix.

-  **Section length:** 900 words

## Section 5 - Decision Matrix & Defaults for the Capstone

- Show how the abstract principles of the 7-step framework are translated into specific, implementable defaults tailored to the distinct demands of research (Nova) versus writing and review (Brown) tasks.
- Emphasize that the matrix is not aspirational but the exact blueprint you will implement starting in the next lesson; any deviation must be explicitly justified and recorded.
- Describe the matrix structure itself: each row captures a decision dimension, the chosen default, and an explicit rationale that links back to cost, latency, reliability, or debuggability goals established in the capstone scoping.
- Position the matrix as a living blueprint that prevents ad-hoc choices during implementation; you will refer to it repeatedly in Lessons 15–22 whenever a trade-off arises.

- Include the following decision matrix as a table, where the caption should be verbatim "Table 1: Decision matrix for the capstone project.":

| Decision Dimension          | Our Default Choice                                                                 | Rationale |
|-----------------------------|------------------------------------------------------------------------------------|-----------|
| **Model Family & Tiers**    | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets**       | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy**        | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy**             | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts**   | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow and ensures a clean separation of concerns. This makes the system modular, simplifies debugging, and enables easy replayability for evaluation and auditing, which is essential for iterative development and quality assurance. |


- No transition line required as this is the final content section before the conclusion.

-  **Section length:** 100 words

## Section 6 - Conclusion

- Recap the structured 7-step decision framework and its direct application to the capstone that produced the clean Nova-versus-Brown global architecture, the three supporting diagrams, and the concrete decision matrix.
- Reiterate that adopting a system-level view—rather than focusing only on prompts or single models—is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective at scale.
- Remind you that the decisions and diagrams recorded in this lesson will be referenced repeatedly in all future implementation lessons so that every code-level choice stays aligned with the original cost, latency, and quality goals.
- Close with a forward pointer to the immediate next lesson, which begins hands-on construction of the FastMCP server, client loop, define the core research tools, and orchestrate the multi-round research and filtering process that produces the final `research.md` file, followed later by Brown workflow implementation in Lessons 19–22.
- End by reinforcing that the real skill you are developing is the ability to make these system-level trade-offs repeatedly across projects, turning AI engineering from art into repeatable engineering practice.

-  **Section length:** 300 words

## Golden Sources

- [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [API Pricing](https://openai.com/api/pricing/)

## Other Sources

- [lost-in-the-middle](<https://arxiv.org/abs/2307.03172>)
- [Intro to OpenAI's o3 and o4-mini](ttps://openai.com/index/introducing-o3-and-o4-mini/)
- [Gemini Review](https://gemini.google/overview/deep-research/)
- [Intro to Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)