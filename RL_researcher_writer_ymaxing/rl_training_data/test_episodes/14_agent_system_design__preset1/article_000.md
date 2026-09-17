# Lesson 14: A Decision Framework for AI Agent System Design

In our last two lessons, we defined the capstone project for this course: two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. In Lesson 12, we scoped the project, establishing the split between an explorative research agent and a deterministic writing workflow. In Lesson 13, we chose our frameworks: Nova will be built using FastMCP for portable, steerable tools, while Brown will run on a durable, auditable LangGraph workflow.

But framework selection is only one piece of the puzzle. The choices you make at the system design level determine whether your agents behave like polished, dependable products or fragile research demos that collapse under real-world workloads. Core design variables—like reasoning budgets, context strategies, and human-in-the-loop (HITL) policies—exert an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has vastly different design constraints than a high-accuracy overnight research job.

This lesson introduces a reusable 7-step decision framework to navigate these trade-offs. We will walk through this playbook to move systematically from business goals to a concrete system design. Then, we will apply it to our capstone project, producing the global architecture for Nova and Brown, complete with component interaction diagrams and a decision matrix you can reuse. By the end, you will know where extra thinking tokens deliver value, when to insert human gates, and how to keep context lean without sacrificing quality.

With the stakes clear, we will now walk through the general 7-step framework before specializing it for our capstone project.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This step-by-step playbook helps you move from a problem statement to a design that balances capability, cost, and reliability. Agentic systems introduce unique failure modes not found in traditional software, such as cascading errors where a single bad tool output silently corrupts an entire workflow [[8]](https://latitude.so/blog/ai-agent-failure-detection-guide). Furthermore, traditional DevOps tools, designed for classical, stateless software, often fall short when applied to the dynamic, stateful nature of agentic AI [[9]](https://orq.ai/blog/ai-agent-frameworks). This framework is designed to address these new challenges head-on.

### 1. Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define success. What is the quality bar for the output? What are the privacy or compliance requirements? What is the expected volume of tasks, and what is your per-task spending limit? These targets dictate every downstream choice. For example, a real-time support bot might prioritize sub-second latency and accept moderate accuracy, whereas a batch research job for a legal team would demand near-zero hallucinations and measure throughput in hours, not seconds.

### 2. Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic offer state-of-the-art performance with low operational overhead but can lead to vendor lock-in. Open-weight models guarantee privacy, deep customization through fine-tuning, and data locality, but place the entire burden of GPU management and infrastructure security on your internal team.

### 3. Define Your Context Strategy

As we saw in previous lessons, a large context window is not a silver bullet. A common mistake is to dump everything into a prompt, assuming the LLM can handle it. This often leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts [[1]](https://arxiv.org/abs/2307.03172). Performance can degrade significantly long before the advertised context limit is reached. Instead of relying on brute force, you should prioritize selective retrieval, context compression, and structured summaries to manage costs and improve reliability. For instance, a sliding window or summarization approach can help an agent remember the latest information in a long conversation, while RAG is better suited for identifying and retrieving specific facts from a large knowledge base.

### 4. Pick an Orchestration Style

The choice between predictable workflows and dynamic agents depends on the task's nature. As we covered in Lesson 2, you should use predictable, auditable workflows for linear processes where the steps are known. Dynamic agents are better for open-ended problems that require flexible tool use. Often, the best systems are hybrids. For example, a research agent might autonomously explore a topic, but the final report generation could be handled by a structured workflow with fixed review and editing stages.

### 5. Establish a HITL & Evaluation Loop

The level of human oversight should be directly proportional to the cost of an error. You need to define clear triggers for human intervention. These can be based on low-confidence scores from the model, the execution of sensitive actions like sending an email or modifying a database, or flags for specific policies. HITL is also a primary defense against emergent failures like "goal drift," where an agent gradually deviates from the user's original objective during a long task, or "context loss," where it forgets key constraints from earlier turns [[8]](https://latitude.so/blog/ai-agent-failure-detection-guide). For a financial analysis agent, any transaction over a certain threshold might require human approval. In contrast, an agent that summarizes internal documents might operate fully autonomously, with humans only reviewing the final output. This is a critical step for building trust and ensuring safety.

### 6. Set Tool Boundaries & Portability

An effective design principle is to keep the LLM responsible for high-level reasoning and intent detection while delegating deterministic tasks to code. Let the LLM decide *what* to do, but let traditional code handle *how* to do it. This helps prevent "tool misuse," one of the most common production failures, where an agent calls the correct tool but with malformed arguments, silently corrupting all subsequent steps [[8]](https://latitude.so/blog/ai-agent-failure-detection-guide). For example, an agent should not be asked to calculate a mortgage payment; it should recognize the user's intent and call a dedicated function with the correct parameters. Furthermore, using a standardized protocol like Model Context Protocol (MCP) ensures your tools are portable and can be reused across different clients, like IDEs or chat interfaces, without being tied to a single vendor [[2]](https://modelcontextprotocol.io/docs/getting-started/intro), [[3]](https://www.databricks.com/blog/what-is-model-context-protocol).

### 7. Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, persistent checkpoints, and detailed tracing to survive failures. This is essential for diagnosing issues like expensive "retry loops," where an agent gets stuck retrying a failing action, or "silent quality degradation," where performance erodes over time without triggering explicit error codes [[8]](https://latitude.so/blog/ai-agent-failure-detection-guide). For a multi-hour research task, you need to be able to resume from the last successful step, not start from scratch. In contrast, for a simple, stateless task that can be retried, a basic retry policy may suffice. Your choices here should link back to the reliability and cost constraints you defined in the first step.

While LLMs provide the reasoning engine, the conceptual foundation of agentic AI predates them. Classical AI treated agents as entities that perceive an environment and act to achieve goals, using architectures that balanced fast, reactive control with slower, deliberative planning. Modern LLM agents extend this classical loop, using the generative model as a powerful reasoning substrate to drive tool use and planning [[10]](https://arxiv.org/html/2602.10479v1). This framework adapts those time-tested principles for the modern AI stack.

This framework is iterative. As you move through the design process, new constraints may surface, requiring you to revisit earlier decisions. Once the high-level decisions are framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding how to manage cost and latency at runtime is central to effective system design. Four independent levers can be adjusted on a per-step basis within a workflow: model size, series scaling, parallel scaling, and input context scaling. Their effects are multiplicative, so a lack of discipline can lead to unexpected costs.

These levers are not just theoretical; they have tangible consequences in domains like robotics and embodied AI. In this field, scaling laws confirm that larger models and more data improve performance, but with unique constraints. Increasing model size does not guarantee better real-world results if the added inference latency causes a robot to miss its window for action. Similarly, powerful models are often too large for the limited compute available on edge devices [[11]](https://arxiv.org/html/2405.14005v1).

**Model Size Scaling** is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite [[4]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/). For a simple classification task, a small model is sufficient and cost-effective. For complex reasoning or strategic planning, a larger model may be necessary despite the higher cost.

**Series Scaling** refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens.” Models like Anthropic's Claude can be given a token budget to reason through a problem before generating a final response [[5]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This should be treated as a dial, activated only for the most complex planning or validation steps and strictly capped to control both spending and latency. An unbounded "think until perfect" approach is a recipe for high costs.

**Parallel Scaling** involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, known as self-consistency, can significantly improve reliability for tasks with verifiable answers. Research has shown that, for a given computational budget, parallel scaling can sometimes outperform additional serial reasoning [[6]](https://arxiv.org/html/2502.12215v1). However, this reliability comes at a linear cost multiplier.

**Input Context Scaling** is the final lever. While relevant information is valuable, each additional token carries a direct cost and adds to latency. The key is to find the optimal balance between providing enough context and avoiding information overload. Techniques like RAG, summarization, and caching help keep the effective context small while preserving the necessary signal.![The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

To see the multiplicative effect, consider two designs for a research task.

A naive design might use:
*   **Model:** The largest, most expensive reasoning model (e.g., GPT-4.5 at $75/M input tokens).
*   **Input Tokens:** An entire 100-page document (around 50,000 tokens) dumped directly into the context.
*   **Output Tokens:** A detailed 2,000-token summary.
*   **Number of Parallel Runs:** 5 runs for self-consistency.
*   **Calculation:** (5 runs * (50k tokens * $0.000075/token + 2k tokens * $0.00015/token)) = **$20.25 per task**.

A budgeted design, on the other hand, might use:
*   **Model:** A fast, mid-tier model (e.g., GPT-4o at $2.50/M input tokens).
*   **Input Tokens:** A 2,000-token summary generated via RAG.
*   **Output Tokens:** A 2,000-token summary.
*   **Number of Parallel Runs:** 1 run.
*   **Calculation:** (1 run * (2k tokens * $0.0000025/token + 2k tokens * $0.00001/token)) = **$0.025 per task**.

This budgeted approach achieves a similar outcome at a roughly 800x cost reduction. Additional optimizations like per-step reasoning caps, prompt caching, and delegating heavy computation to external tools can further reduce costs.

With the scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.![Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The core architectural principle of our capstone, illustrated in Image 2, is to enforce a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP-driven agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. For example, a failure in Nova's research trace is isolated and cannot corrupt Brown's internal state, allowing you to debug the research logic without having to re-run the entire writing process. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable. A simple **MCP client** then runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt.

For the MCP client, we use **FastMCP’s built-in `Client` class,** a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details out of the box. Our implementation is just around 200 lines of Python that wrap this client. It connects to the server, fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation.![End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this powerful engine with a **FastMCP server**, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:
*   **Generate Article:** This orchestrates the full writing process. It loads context (guidelines, research, profiles, examples), generates media items using the orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining context awareness of the full document.![Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean contract decouples the agents, making the system modular and easier to debug.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, personal notes, or anything else they consider important. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be messy. Leaving too many gaps for the AI to fill leads to hollow text. LLMs are excellent at translation and synthesis, but they are not sources of original insight.

The architecture and diagrams are now concrete. The final step is to translate the framework principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

The abstract principles of the 7-step framework must be translated into specific, implementable defaults. The matrix below serves as the exact blueprint we will implement starting in the next lesson. It captures our default choices for each decision dimension, tailored to the distinct demands of research (Nova) and writing (Brown). This matrix is a living document that prevents ad-hoc choices during implementation. We will refer to it repeatedly in Lessons 15–22 whenever a trade-off arises.

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

In this lesson, we introduced a structured 7-step decision framework for designing AI agent systems. We then applied it to our capstone project, producing the clean global architecture for Nova and Brown, three supporting diagrams, and a concrete decision matrix. We emphasized managing the four key scaling levers—model size, series, parallel, and context—and the core architectural principle of separating concerns. Adopting this system-level view—rather than focusing only on prompts or single models—is what turns prototypes into scalable, production-ready products that are both debuggable and cost-effective.

The decisions and diagrams we have established here are not just theoretical. They will be referenced repeatedly in all future implementation lessons, ensuring that every code-level choice remains aligned with our original goals for cost, latency, and quality.

In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining its core research tools and orchestrating the process that produces the final `research.md` file. The implementation of the Brown workflow will follow in Lessons 19–22. The real skill you are developing is the ability to make these system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable practice and a core tenet of the emerging discipline of Agentic Engineering [[12]](https://arxiv.org/html/2606.05608v1).

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [3] [What is the Model Context Protocol (MCP)? | Databricks](https://www.databricks.com/blog/what-is-model-context-protocol)
- [4] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [5] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [6] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [7] [API Pricing](https://openai.com/api/pricing/)
- [8] [Detecting AI Agent Failure Modes in Production](https://latitude.so/blog/ai-agent-failure-detection-guide)
- [9] [The Guide to AI Agent Frameworks](https://orq.ai/blog/ai-agent-frameworks)
- [10] [Agentic AI: A New Paradigm of Artificial Intelligence](https://arxiv.org/html/2602.10479v1)
- [11] [Scaling Laws for Embodied AI](https://arxiv.org/html/2405.14005v1)
- [12] [Agentic Engineering: A New Software Delivery Paradigm](https://arxiv.org/html/2606.05608v1)