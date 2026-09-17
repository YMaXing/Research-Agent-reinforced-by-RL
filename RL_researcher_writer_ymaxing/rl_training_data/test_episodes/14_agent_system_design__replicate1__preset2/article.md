# A Decision Framework for Production-Ready AI Agents

In the last two lessons, we defined the scope for our capstone project: building two production-oriented agents, Nova and Brown, to collaborate on producing publish-ready technical articles. We chose our frameworks, deciding Nova will use FastMCP for portable research tools, while Brown will run on a durable LangGraph workflow for writing. Now we move from framework selection to system design, the layer that determines whether our agents behave like polished products or fragile demos. This shift reflects a deeper change in software engineering itself. AI agents represent a new paradigm where decision logic is generated at runtime, not pre-encoded by a human, making system-level design more important than ever [[3]](https://arxiv.org/html/2606.05608).

Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement have an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has different design constraints than a high-accuracy overnight research job. Understanding these trade-offs is what separates prototypes from production systems.

This lesson introduces a reusable 7-step decision playbook that moves from business value through model routing, context discipline, and observability. We will apply this framework to our capstone, yielding the global Nova-Brown architecture and a decision matrix you can reuse. You will learn to decide where extra thinking tokens add value, when to use human gates, and how to keep context lean.

With the stakes clear, we will now walk through the general 7-step framework before specializing it for our capstone.

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

## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix to guide our implementation. We also examined the four inference-time scaling levers: model size, series reasoning, parallel runs, and context volume. We saw how their multiplicative effects can create massive cost variations, reinforcing the need for a disciplined, system-level approach. Adopting this view, rather than focusing only on prompts or single models, is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have established here are not just theoretical. They are the blueprint for our upcoming work. We will reference them repeatedly in all future implementation lessons to ensure that every code-level choice stays aligned with our original goals for cost, latency, and quality. This disciplined approach is what separates reliable systems from brittle demos that fail under real-world pressure. It is the difference between building a toy and engineering a product.

In the next lesson, we will begin the hands-on construction of Nova, our research agent. We will build the FastMCP server, define its core research tools, and implement the client loop that orchestrates the multi-round research and filtering process to produce the final `research.md` file. This will be our first major step in turning the architectural diagrams into running code. Later, in Lessons 19-22, we will build out the durable Brown workflow using LangGraph, implementing the stateful logic for drafting, reviewing, and editing. The ability to make these system-level trade-offs repeatedly is what turns AI engineering into a repeatable practice.

## References

- [1] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)
- [2] What is the Model Context Protocol (MCP)?. (n.d.). [https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)
- [3] AI Agents Are A New Paradigm of Software. (2026). [https://arxiv.org/html/2606.05608](https://arxiv.org/html/2606.05608)
- [4] Sarukkai, V., Gupta, A., Hong, J., Gharbi, M., & Fatahalian, K. (n.d.). Inference-Time Distillation: Cost-Efficient Agents Without Fine-Tuning or Manual Prompt Engineering. [https://openreview.net/forum?id=nCEdAM5m5T](https://openreview.net/forum?id=nCEdAM5m5T)
- [5] AI Agent Failure Pattern Recognition. (n.d.). [https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition)
- [6] Six factors that drive AI inference costs in production. (n.d.). [https://www.mirantis.com/blog/inference-costs](https://www.mirantis.com/blog/inference-costs)
- [7] Extended thinking & interleaved thinking docs. (n.d.). [https://docs.claude.com/en/docs/build-with-claude/extended-thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [8] Revisiting the Test-Time Scaling of o1-like Models. (2025). [https://arxiv.org/html/2502.12215v1](https://arxiv.org/html/2502.12215v1)
- [9] Control Theory for Language Models. (2026). [https://arxiv.org/html/2602.03433v1](https://arxiv.org/html/2602.03433v1)
- [10] How LLM Inference Actually Works in Production. (n.d.). [https://www.yottalabs.ai/post/how-llm-inference-actually-works-in-production-and-why-most-systems-fail](https://www.yottalabs.ai/post/how-llm-inference-actually-works-in-production-and-why-most-systems-fail)
- [11] Manus: An Agentic AI Framework for Human-in-the-loop Task Automation. (2025). [https://arxiv.org/html/2505.02024v2](https://arxiv.org/html/2505.02024v2)
- [12] The Microservices Moment for Artificial Intelligence. (n.d.). [https://www.softwareseni.com/the-microservices-moment-for-artificial-intelligence-and-how-multi-agent-orchestration-changes-everything](https://www.softwareseni.com/the-microservices-moment-for-artificial-intelligence-and-how-multi-agent-orchestration-changes-everything)
- [13] Human-in-the-loop. (n.d.). [https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [14] What is the Model Context Protocol (MCP)?. (n.d.). [https://www.databricks.com/blog/what-is-model-context-protocol](https://www.databricks.com/blog/what-is-model-context-protocol)
- [15] Persistence. (n.d.). [https://docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [16] Interpretable Context Methodology: Folder Structure as Agent Architecture. (2026). [https://arxiv.org/html/2603.16021v1](https://arxiv.org/html/2603.16021v1)
- [17] The Decision Matrix Method for Engineering Trade-Offs. (n.d.). [https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45)
- [18] Decision Matrix for AI Projects. (n.d.). [https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects)
- [19] Agentic AI Explained: Workflows vs Agents. (n.d.). [https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows)
- [20] Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs. (n.d.). [https://openreview.net/forum?id=XSHP62BCXN](https://openreview.net/forum?id=XSHP62BCXN)
- [21] RAG vs. Long-Context LLMs. (n.d.). [https://www.meilisearch.com/blog/rag-vs-long-context-llms](https://www.meilisearch.com/blog/rag-vs-long-context-llms)
- [22] A Developer's Guide to Building Scalable AI: Workflows vs. Agents. (n.d.). [https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents)
- [23] FMEA. (n.d.). [https://www.jamasoftware.com/requirements-management-guide/meeting-regulatory-compliance-and-industry-standards/fmea](https://www.jamasoftware.com/requirements-management-guide/meeting-regulatory-compliance-and-industry-standards/fmea)
- [24] AI Agent Artifacts. (n.d.). [https://fast.io/resources/ai-agent-artifacts](https://fast.io/resources/ai-agent-artifacts)
- [25] A Multi-Robot Exploration Framework. (2025). [https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf](https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf)