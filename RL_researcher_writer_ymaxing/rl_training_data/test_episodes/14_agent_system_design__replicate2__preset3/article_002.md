# Lesson 14: A Decision Framework for Production-Ready AI Agents

## Introduction

In the last two lessons, we established the capstone project for this course: two production-oriented agents that collaborate to produce publish-ready technical articles. In Lesson 12, we defined the scope, splitting the work between an explorative research agent, Nova, and a deterministic writing workflow, Brown. In Lesson 13, we compared agent frameworks and justified our choices: Nova will use FastMCP for portable, steerable tools, while Brown will run a durable, auditable LangGraph workflow.

Now, we move from framework selection to system design. This is the layer that determines whether our agents become dependable products or brittle demos that fail under real-world conditions. Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement exert an order-of-magnitude influence on cost, latency, and reliability.

This lesson provides a reusable 7-step decision playbook that moves systematically from business requirements to a concrete architectural blueprint. We will apply this framework in full to our capstone, yielding the global Nova-Brown architecture and a detailed decision matrix you can adapt for your own projects. You will learn where extra thinking tokens deliver genuine value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal.

With the stakes clear, let's walk through the general 7-step framework before specializing it for our capstone project.

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

## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework now become specific, implementable defaults for the Nova and Brown agents. This matrix is not aspirational; it is the exact blueprint we will implement starting in the next lesson. It serves as a living document that prevents ad-hoc choices during implementation, ensuring every trade-off aligns with our goals for cost, latency, and reliability. We will refer to it repeatedly in Lessons 15–22 whenever a design choice arises, making sure our code stays true to our architectural vision.

## Table 1: Decision matrix for the capstone project

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, the three supporting diagrams, and the concrete decision matrix that will guide our implementation. Adopting a system-level view is the foundation that turns prototypes into scalable, production-ready agent products. This means focusing on the entire architecture, not just on prompts or single models, to build systems that are debuggable and cost-effective at scale.

The decisions and diagrams recorded in this lesson are not just theoretical. They will be referenced repeatedly in all future implementation lessons so that every code-level choice stays aligned with the original cost, latency, and quality goals. This architectural blueprint is our source of truth as we move from design to code, ensuring consistency and purpose in our engineering efforts.

We will begin the hands-on construction of the FastMCP server and client loop for Nova in the next lesson. There, we will define the core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. The implementation of the Brown workflow will follow in Lessons 19–22, where we will build out the stateful writing and review cycles. The real skill you are developing is the ability to make these system-level trade-offs deliberately and repeatedly, turning AI engineering from an intuitive art into a disciplined, repeatable practice.

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [Information-theoretic origins of the “lost-in-the-middle” phenomenon in LLMs](https://arxiv.org/html/2510.10276v1)
- [3] [Positional Biases in Language Models Shift as Inputs Approach Context Window Limits](https://openreview.net/forum?id=vlUk8z8LaM)
- [4] [Human-in-the-Loop Autonomous Agent Oversight](https://galileo.ai/blog/human-in-the-loop-agent-oversight)
- [5] [Multi-agent AI systems are the next evolution of microservices](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices)
- [6] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [7] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [8] [The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs](https://arxiv.org/html/2509.09677v1)
- [9] [On the Visible Thought of Large Language Models](https://arxiv.org/html/2604.02460v1)
- [10] [A Taxonomy of Failure Modes in Large Language Model-based Multi-Agent Systems](https://arxiv.org/html/2503.13657v1)
- [11] [API Pricing](https://openai.com/api/pricing/)
- [12] [File Systems for Agents](https://www.amplifypartners.com/blog-posts/file-systems-for-agents)
- [13] [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [14] [What is the Model Context Protocol (MCP)?](https://www.databricks.com/blog/what-is-model-context-protocol)
- [15] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [16] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)