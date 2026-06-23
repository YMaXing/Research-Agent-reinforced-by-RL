# Lesson 14: A Decision Framework for AI System Design

In the last two lessons, we defined the scope for our capstone project: two production-oriented agents, Nova (research) and Brown (writing), that collaborate to produce publish-ready technical articles. We also justified our framework choices, opting for FastMCP to make Nova’s tools portable and steerable, while using LangGraph to give the Brown writing workflow durability and auditability.

With those foundational choices made, we now move to the next critical layer: system design. This is the discipline that determines whether our agents behave like polished, dependable products or like fragile research demos that collapse under real workloads. Core design variables—such as reasoning budgets, context strategies, orchestration styles, and human-in-the-loop (HITL) policies—each exert an order-of-magnitude influence on cost, latency, and reliability.

This lesson introduces a reusable 7-step decision playbook that moves from business value definition to a complete system design. We will apply this framework to our capstone, yielding the global Nova-versus-Brown architecture, component interaction diagrams, and a decision matrix you can reuse on your own projects. By the end, you will know where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal. With the stakes clear, we will now walk through the general framework before specializing it for our capstone.

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

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of the 7-step framework into specific, implementable defaults for our capstone. It is the exact blueprint we will implement starting in the next lesson. Each row captures a decision dimension, our chosen default, and an explicit rationale that links back to the cost, latency, reliability, or debuggability goals we established. This matrix will serve as a living blueprint to prevent ad-hoc choices during implementation.

## Decision Matrix for the Capstone Project

Table 1: Decision matrix for the capstone project.
| Decision Dimension | Our Default Choice | Rationale |
| :--- | :--- | :--- |
| **Model Family & Tiers** | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets** | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, preventing common failure modes like task derailment or step repetition [[17]](https://arxiv.org/html/2503.13657v1). Expensive parallel runs are reserved only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy** | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy** | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts** | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow and ensures a clean separation of concerns. This makes the system modular, simplifies debugging, and enables easy replayability for evaluation and auditing, which is essential for iterative development and quality assurance. |

## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it directly to our capstone project. This systematic process yielded the clean Nova-versus-Brown global architecture, three supporting diagrams that illustrate the component interactions, and a concrete decision matrix that will guide our implementation. This system-level view, which prioritizes deliberate trade-offs over chasing the latest model, is the foundation that turns brittle prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here are not just theoretical exercises. They are our direct reference points for all upcoming implementation lessons, ensuring that every line of code we write aligns with our original goals for cost, latency, and quality. This structured approach is essential for managing the complexity of modern AI systems and delivering reliable results that meet real-world business needs.

Our journey continues in the next lesson, where we will begin the hands-on construction of the FastMCP server and client loop for Nova. We will define its core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. Later, in Lessons 19–22, we will turn our attention to implementing the durable and stateful Brown writing workflow using LangGraph. The real skill you are developing is not just how to code an agent, but how to make these critical system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable and reliable engineering practice.

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [3] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [4] [API Pricing](https://openai.com/api/pricing/)
- [5] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [6] [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [7] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [8] [Intro to OpenAI's o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)
- [9] [Gemini Review](https://gemini.google/overview/deep-research/)
- [10] [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [11] [Positional Biases Shift as Inputs Approach Context Window Limits](https://openreview.net/forum?id=vlUk8z8LaM)
- [12] [Multi-Agent Systems: Orchestration vs. Choreography](https://tetrate.io/learn/ai/multi-agent-systems)
- [13] [Conductor: Deterministic Orchestration for Multi-Agent AI Workflows](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows)
- [14] [Human-in-the-Loop Agent Oversight](https://galileo.ai/blog/human-in-the-loop-agent-oversight)
- [15] [Multi-Agent AI Systems Are the New Microservices](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices)
- [16] [The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs](https://arxiv.org/html/2509.09677v1)
- [17] [A Taxonomy of Failure Modes for Multi-Agent Systems](https://arxiv.org/html/2503.13657v1)
- [18] [File Systems for Agents](https://www.amplifypartners.com/blog-posts/file-systems-for-agents)
- [19] [Agent Orchestration Explained](https://www.dataiku.com/stories/blog/agent-orchestration-explained)
- [20] [Building AI agents: Workflow-first vs. code-first vs. hybrid](https://techcommunity.microsoft.com/blog/azurearchitectureblog/building-ai-agents-workflow-first-vs-code-first-vs-hybrid/4466788)
- [21] [Human-in-the-Loop Reinforcement Learning for Autonomous Driving](https://arxiv.org/html/2408.12548v1)
- [22] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)