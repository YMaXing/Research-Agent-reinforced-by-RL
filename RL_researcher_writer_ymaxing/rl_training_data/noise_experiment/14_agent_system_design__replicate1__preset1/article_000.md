# Lesson 14: An AI Engineering Decision Framework

In the last two lessons, we defined the scope for our capstone project—two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. In Lesson 12, we established the high-level design, splitting the work between an explorative research agent and a deterministic writing workflow. In Lesson 13, we chose our frameworks: Nova will ship as a set of portable FastMCP tools, while Brown will run a durable, auditable LangGraph workflow.

With our frameworks selected, we now move to a distinct and critical layer: system design. This is what determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads. Core design variables—such as reasoning budgets, context strategy, orchestration style, and human-in-the-loop (HITL) placement—each exert an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot, for instance, must prioritize sub-second latency, while an overnight research job can trade speed for near-zero hallucination.

This lesson introduces a reusable, 7-step decision playbook that moves systematically from business requirements to a concrete agent architecture. We will then apply this framework to our capstone, producing the global design for Nova and Brown, complete with component interaction diagrams and a decision matrix you can reuse on future projects. By the end, you will know exactly where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal. With the stakes clear, we will now walk through the general framework before specializing it for our capstone.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. While the conceptual foundations of agentic AI predate LLMs by decades, with classical architectures based on beliefs, desires, and intentions, modern LLM-based agents introduce unique challenges [[8]](https://arxiv.org/html/2602.10479v1). Traditional DevOps tools, designed for stateless services, are ill-equipped for the dynamic, stateful workflows of agents, necessitating a new engineering discipline [[9]](https://orq.ai/blog/ai-agent-frameworks). This playbook provides a step-by-step process to move from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define your success criteria. What is the required output quality? What are the privacy or compliance constraints? What is the expected volume of tasks, and what is your per-task spending limit? These targets dictate every downstream choice. For example, a real-time support bot might require sub-second latency where moderate accuracy is acceptable. In contrast, a high-accuracy batch research job may measure throughput in hours and have a near-zero tolerance for hallucinations. Clearly defining these constraints upfront prevents you from over-engineering a solution or, worse, building one that is economically unviable.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic deliver state-of-the-art performance with low operational overhead but come with the risk of vendor lock-in and less control over data. Open-weight models, on the other hand, guarantee privacy, deep customization through fine-tuning, and data locality, but place the entire burden of GPU management and infrastructure security on your internal team. The choice depends on your priorities: maximum capability with simplicity versus maximum control and privacy.

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not a silver bullet. It is a common mistake to dump everything into a prompt and assume the LLM can handle it. This approach often leads to the "lost-in-the-middle" performance cliff, where models struggle to find and use relevant information buried in a long context [[1]](https://arxiv.org/abs/2307.03172). Performance degrades significantly when models must access information located in the middle of their input, with the highest accuracy often coming from information placed at the very beginning or end [[1]](https://arxiv.org/abs/2307.03172).

Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries. For a long-running chatbot, a sliding window or summarization of the conversation history can help the agent remember the latest information without being overwhelmed. For a question-answering system, Retrieval-Augmented Generation (RAG) is a better approach to identify and retrieve only the most relevant document chunks. This discipline of managing the context window is key to managing costs and improving reliability.

### Pick an Orchestration Style

The choice of orchestration style depends on the predictability of your task. As we discussed in Lesson 2, you should use predictable workflows for processes that are linear and require auditable steps. For open-ended problems that demand dynamic tool use, autonomous agents are more suitable. Often, the best solution is a hybrid design that combines both. A research task might use an agent for exploration, which then hands off its findings to a structured workflow for report generation. This matches the right architectural pattern to the right sub-problem, balancing flexibility with control.

### Establish a HITL & Evaluation Loop

You must decide where to inject human oversight. Full autonomy is tempting but risky, especially when error costs are high. Instead, define clear triggers for human intervention. These can be based on low-confidence scores from the model, requests to perform sensitive actions like sending an email, or flags for ambiguous or high-stakes queries. For an internal research agent, you might trigger HITL if a query's ambiguity score exceeds a certain threshold. For our writing agent, Brown, the final sign-off on an article is a non-negotiable human checkpoint. This loop is critical for preventing subtle, long-term failures like **goal drift**, where an agent gradually shifts away from the user's original objective over a long workflow [[10]](https://latitude.so/blog/ai-agent-failure-detection-guide). This loop of automated work followed by human review is central to building trustworthy systems.

### Set Tool Boundaries & Portability

A core principle of robust system design is to keep the LLM responsible for what it does best: intent detection and high-level planning. Delegate deterministic tasks, heavy computation, or complex validation to traditional code. For example, do not ask an LLM to calculate the total of a list of numbers; have it call a Python function instead. This discipline is not just about efficiency; it is a critical defense against **tool misuse**, one of the most common and damaging failure modes in production, where a single malformed argument can silently corrupt an entire workflow [[10]](https://latitude.so/blog/ai-agent-failure-detection-guide).

Furthermore, protocols like the Model Context Protocol (MCP) enforce clean tool boundaries and ensure portability [[2]](https://modelcontextprotocol.io/docs/getting-started/intro). By standardizing how tools are exposed to agents, MCP allows you to swap out clients, models, or even IDEs without rewriting your tool implementations. This prevents you from tying your core business logic to any single vendor or framework.

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs, like our article generation workflow, demand resumability, persistent checkpoints, and full execution tracing. If the process fails halfway through, you need to be able to resume from the last saved state, not start from scratch. Frameworks like LangGraph provide this durability out of the box. For simple, stateless tasks that can be retried without consequence, a basic retry policy may suffice. In a multi-agent system like our capstone, this becomes even more important to prevent **cascading errors**, where a failure in one agent propagates to others [[10]](https://latitude.so/blog/ai-agent-failure-detection-guide). A particularly dangerous form of this is hallucination propagation, where one agent's fabricated output becomes trusted input for the next, amplifying the error down the chain [[11]](https://www.augmentcode.com/guides/multi-agent-ai-systems). Your choice here should link directly back to the reliability and cost constraints you defined in the first step.

This framework is iterative. You will likely revisit earlier steps as you uncover new constraints during implementation. However, by starting with this structured approach, you ensure your design is grounded in clear trade-offs from the beginning. Once the high-level decisions are framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding and controlling the four independent levers of runtime scaling is central to effective system design. Model size, series scaling (thinking), parallel scaling (multiple runs), and input context each multiply cost and latency. The key is to know which dial to turn for which task.

These principles are not unique to language-based agents. The same scaling laws are being actively studied in fields like embodied AI and robotics, where performance also improves with model size, data, and compute. However, these domains introduce unique constraints, such as real-world inference latency directly impacting a physical task's success rate [[12]](https://arxiv.org/html/2405.14005v1).![https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down) 
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models have higher per-token costs. For instance, a frontier model like GPT-4.5 costs around $75 per million input tokens, while a hyper-efficient model like Gemini 2.5 Flash-Lite costs only $0.10 for the same amount [[3]](https://openai.com/api/pricing/), [[4]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/). The choice depends on the task's complexity. For simple data extraction, a small model is sufficient and cost-effective. For complex reasoning and planning, the higher cost of a frontier model may be justified by its superior performance.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often implemented as "thinking tokens" or a longer chain of thought. For example, Claude's "extended thinking" feature allows it to reason at length before giving a final answer [[5]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This is a powerful tool for complex problems but adds both cost and latency. The best practice is to treat extra reasoning as a dial, activating it only for the most difficult planning or validation steps and setting a strict cap (e.g., a maximum of 8,000 thinking tokens) to bound spend. An unbounded "think until perfect" approach is a recipe for budget overruns.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, known as self-consistency, can significantly improve reliability for tasks with deterministic answers, like math problems. However, the reliability gain comes at a linear cost multiplier; five parallel runs mean five times the cost. Research suggests that for a given compute budget, parallel scaling can sometimes outperform further serial reasoning, making it a valuable trade-off to consider [[6]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

While models with large context windows are now common, every token of input carries a direct cost and an indirect latency penalty. The key is to find the optimal balance between providing sufficient information and keeping the context lean. As discussed, techniques like RAG, summarization, and prompt caching are essential for preserving the signal while minimizing noise and cost. A well-designed RAG system that retrieves five relevant 500-token chunks is far more efficient than dumping an entire 100,000-token document into the prompt.

To see how these levers multiply, consider a simple cost calculation.

A **naive design** might use the largest reasoning model, dump an entire document into the context, and run multiple parallel attempts for maximum reliability.

-   **Model:** GPT-4.5 ($75/M input, $150/M output)
-   **Input Tokens:** 100,000 (full document)
-   **Output Tokens:** 4,000 (summary)
-   **Number of Parallel Runs:** 5
-   **Calculation:** (100,000 tokens × $75/M + 4,000 tokens × $150/M) × 5 runs = ($7.50 + $0.60) × 5 = **$40.50 per task**

A **budgeted design** uses a tiered approach, applying the right resource for each part of the job.

-   **Model:** Gemini 2.5 Flash-Lite ($0.10/M input, $0.40/M output)
-   **Input Tokens:** 3,000 (RAG retrieval + prompt)
-   **Output Tokens:** 4,000 (summary)
-   **Number of Parallel Runs:** 1
-   **Calculation:** (3,000 tokens × $0.10/M + 4,000 tokens × $0.40/M) × 1 run = ($0.0003 + $0.0016) × 1 = **$0.0019 per task**

The difference is over 20,000x. This is not an exaggeration; it is the reality of system design in the agentic era. By making deliberate choices about these four levers, you can build systems that are both highly capable and economically sustainable. With these scaling dynamics quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate research and writing.![https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce53cd4ed8/image/w=1920,quality=90,fit=scale-down](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce53cd4ed8/image/w=1920,quality=90,fit=scale-down)
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The core architectural principle of our capstone, illustrated in Image 2, is a clean separation of concerns. We isolate the unpredictable, open-ended research phase, handled by Nova as an MCP agent, from the predictable, iterative drafting and review process, handled by Brown as a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug, evaluate, and evolve independently. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple **MCP client** runs an LLM-driven loop that follows a “Research Recipe” retrieved from a master prompt on the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file.

For the MCP client, we use **FastMCP’s built-in `Client` class**, a lightweight, ready-to-use client that handles all protocol details like capability discovery and tool calling. Our implementation is a ~200-line Python script that wraps this client. It connects to the server, fetches the research prompt, and runs a simple ReAct-style loop where the LLM decides which tool to call next via `client.call_tool()`. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures if, for example, all scraping attempts fail.![https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine [[7]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). We front this engine with a **FastMCP server**, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:

-   **Generate Article:** This orchestrates a full workflow. It loads context (guidelines, research, profiles), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern.
-   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, prioritizing human input over automated reviews.
-   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining awareness of the full document.![https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory containing its artifacts. Brown takes these, along with the original `article_guideline.md` and our writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean contract makes the system modular and debuggable.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what to write, the article's narrative, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill without instructions leads to hollow text. LLMs are amazing at translation and synthesis, but they are not a substitute for original thought.

The architecture and diagrams are now concrete. The final step is to translate these framework principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of our 7-step framework into specific, implementable defaults for the Nova and Brown agents. It is not an aspirational document; it is the exact blueprint we will implement starting in the next lesson. Any deviation from these defaults must be explicitly justified. Each row captures a decision dimension, our chosen default, and the rationale that links it back to our cost, latency, and reliability goals. This matrix serves as a living blueprint that prevents ad-hoc choices during implementation.

Table 1: Decision matrix for the capstone project.
| Decision Dimension | Our Default Choice | Rationale |
| :--- | :--- | :--- |
| **Model Family & Tiers** | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets** | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy** | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy** | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts** | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow and ensures a clean separation of concerns. This makes the system modular, simplifies debugging, and enables easy replayability for evaluation and auditing, which is essential for iterative development and quality assurance. |

## Conclusion

In this lesson, we introduced a structured 7-step decision framework for AI engineering. We applied it directly to our capstone project, producing the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix that will guide our implementation. Adopting this system-level view—rather than focusing only on prompts or single models—is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here will be referenced repeatedly in all future implementation lessons. This ensures that every code-level choice stays aligned with our original cost, latency, and quality goals. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining our core research tools and orchestrating the multi-round research process that produces the final `research.md` file. The implementation of the Brown writing workflow will follow in Lessons 19–22.

The real skill you are developing is the ability to make these system-level trade-offs deliberately and repeatedly across projects. This is what turns AI engineering from an art into a repeatable engineering practice. It is part of a broader shift toward what some call **Agentic Engineering**, a discipline focused on building systems that can not only execute tasks but also learn and self-improve from their interactions over time [[13]](https://arxiv.org/html/2606.05608v1).

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [3] [API Pricing](https://openai.com/api/pricing/)
- [4] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [5] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [6] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [7] [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [8] [Classical and Modern AI Agent Architectures](https://arxiv.org/html/2602.10479v1)
- [9] [AI Agent Frameworks: A Guide](https://orq.ai/blog/ai-agent-frameworks)
- [10] [Detecting AI Agent Failure Modes in Production](https://latitude.so/blog/ai-agent-failure-detection-guide)
- [11] [Multi-Agent AI Systems: Architecture & Failure Modes](https://www.augmentcode.com/guides/multi-agent-ai-systems)
- [12] [Scaling Laws for Embodied AI and Robotics](https://arxiv.org/html/2405.14005v1)
- [13] [Agentic Engineering: A Paradigm Shift](https://arxiv.org/html/2606.05608v1)