# From Prototype to Production: A Decision Framework for AI Agent System Design

In the last two lessons, we defined the scope for our capstone project—two production-oriented agents that collaborate to produce publish-ready technical articles—and selected our core frameworks. We chose to build our research agent, Nova, with FastMCP for portability and steerability, while our writing workflow, Brown, will use LangGraph for durability and auditability.

With our tools selected, we now move to system design. This is the layer that determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads. Core design variables like the reasoning budget, context strategy, and human-in-the-loop (HITL) placement each exert an order-of-magnitude influence on cost, latency, and reliability. For example, a real-time support bot requires sub-second latency and can tolerate moderate accuracy, while an overnight research job demands near-zero hallucinations, even if it takes hours.

This lesson introduces a reusable 7-step decision playbook that moves systematically from business requirements to a concrete agent architecture. We will then apply this framework to our capstone, producing the global design for Nova and Brown, complete with component diagrams and a decision matrix you can reuse. You will learn where to spend extra thinking tokens, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal. With the stakes clear, let's walk through the general framework before specializing it for our project.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This step-by-step playbook helps you move from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice. For instance, a real-time support bot might need sub-second latency where moderate accuracy is acceptable. In contrast, a high-accuracy batch research job measures throughput in hours and has a near-zero tolerance for hallucinations.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic offer state-of-the-art performance with low operational overhead but can lead to vendor lock-in. Open-weight models such as Llama or Mistral guarantee privacy, deep customization, and data locality when self-hosted. However, this path requires you to manage the GPU infrastructure, which is a significant burden.

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not always the solution. It is a common mistake to dump everything into a prompt and assume the LLM can handle it. This often leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts [[1]](https://arxiv.org/abs/2307.03172). Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability.

For example, in a chatbot application, a sliding window or summarization strategy can help the model remember the most recent parts of a conversation. For a question-answering system, Retrieval-Augmented Generation (RAG) is more effective, as it identifies and retrieves only the most relevant information from a large knowledge base.

### Pick an Orchestration Style

The choice of orchestration depends on the task's predictability. As we discussed in Lesson 2, you should use predictable workflows for linear, auditable processes. For open-ended tasks that require dynamic tool use, agents are a better fit. Often, a hybrid design that combines both is the most effective solution. For example, an agent might handle initial data exploration, while a workflow executes a fixed reporting process based on the agent's findings.

### Establish a HITL & Evaluation Loop

You must decide where to insert human-in-the-loop triggers based on error cost and business risk. Instead of aiming for full autonomy, define clear triggers for human intervention. These can be based on low-confidence scores from the model, the execution of sensitive actions like sending an email, or flags for policy violations. For a research agent, a HITL gate could be triggered for any query above a certain ambiguity threshold. For our writing agent, a final human sign-off on the article is non-negotiable.

### Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for intent detection and high-level orchestration, while delegating deterministic tasks like math or data validation to traditional code. This separation of concerns improves reliability. Furthermore, standardizing tool interactions using a protocol like the Model Context Protocol (MCP) ensures your tools are portable. This allows you to reuse them across different clients, such as IDEs or chat interfaces, without being tied to a single vendor's ecosystem [[2]](https://modelcontextprotocol.io/docs/getting-started/intro), [[3]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, checkpoints, and full tracing to recover from failures [[4]](https://docs.langchain.com/oss/python/langgraph/persistence). For simple, stateless tasks, a basic retry policy may suffice. These choices should link back to the success criteria defined in the first step. A high-stakes financial analysis workflow needs detailed tracing for audits, while a simple summarization task does not.

This framework is iterative. You will likely revisit earlier steps as you uncover new constraints during implementation. Once the high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency so you can budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Four independent levers can be adjusted at runtime to trade cost and latency for performance: model size, series scaling, parallel scaling, and input-context scaling. Understanding how these levers interact and multiply is central to effective system design.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down> 
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite [[5]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/). For high-value tasks where mistakes are expensive, a frontier model is justified. For high-volume, low-stakes tasks, a cheaper model is more appropriate.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens” [[6]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking), [[7]](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html). You should treat extra reasoning steps as a dial that is activated only for the most complex planning or validation steps. It is also important to cap these tokens to bound both spending and latency. An unbounded "think until perfect" approach is a recipe for runaway costs.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique is also known as self-consistency [[8]](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling). The reliability gains come at a linear cost multiplier. Research shows that for a fixed budget, parallel scaling can sometimes outperform additional serial reasoning [[9]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

While relevant information is valuable, each additional token carries a direct cost and adds to latency. As discussed, the key is to find the optimal balance. Techniques like RAG, summarization, and caching help keep the effective context small while preserving the necessary signal.

### Cost Calculation Contrast

To see how these levers multiply, let's compare two designs for a research task.

A **naive design** might use the largest reasoning model, dump an entire document into the context, and run five parallel attempts to ensure accuracy.

*   **Model:** GPT-4.5 (Input: $75/M tokens, Output: $150/M tokens) [[10]](https://openai.com/api/pricing/)
*   **Input Tokens:** 100,000 (full document)
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 5
*   **Calculation:** (5 runs * (100k tokens * $0.000075/token + 2k tokens * $0.00015/token)) = **$39.00**

A **budgeted design** would use a fast model for an initial pass, use RAG to extract key chunks, summarize them, and then perform a single reasoning pass.

*   **Model:** Gemini 2.5 Flash (Input: $0.30/M tokens, Output: $2.50/M tokens) [[5]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
*   **Input Tokens:** 5,000 (RAG chunks + summary)
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 1
*   **Calculation:** (1 run * (5k tokens * $0.0000003/token + 2k tokens * $0.0000025/token)) = **$0.0065**

This budgeted approach yields a cost reduction of over 5,000x while potentially meeting the same quality target.

### Additional Optimizations

Other optimizations can further reduce costs. Per-step reasoning caps, prompt caching for repeated calls, and delegating heavy computation to external tools all help keep the LLM context small and focused.

With these scaling levers quantified, we can now apply the full framework to produce a concrete global architecture for our capstone project.

## Our Capstone: Global System Design

Let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate research and writing.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down>
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The core architectural principle of our capstone, illustrated in Image 2, is a clean separation of concerns. Unpredictable, open-ended research is handled by Nova as an MCP agent. Predictable, iterative drafting and review are handled by Brown as a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and compile everything into a `research.md` file.

For the MCP client, we use FastMCP’s built-in `Client` class. This is a lightweight, ready-to-use client that handles all protocol details like capability discovery and tool calling. Our implementation is a ~200 line Python wrapper around this class. It connects to the server, fetches the research prompt, and runs a simple ReAct-style loop where the LLM decides which tool to call next.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down>
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:
*   **Generate Article:** This orchestrates a workflow that loads context (guidelines, research, profiles), generates media items using an orchestrator-worker pattern, writes a first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, prioritizing human input over automated reviews.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down>
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

### Handoff and Human Input

The handoff between Nova and Brown is file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This clean separation makes the system modular and debuggable.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill leads to hollow text. LLMs are amazing at translation and synthesis, but they are terrible at generating original ideas.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of our 7-step framework into specific, implementable defaults for the Nova and Brown agents. This is the exact blueprint we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, the chosen default, and a rationale that links back to our goals for cost, latency, reliability, and debuggability.

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix that will guide our implementation. Adopting a system-level view—rather than focusing only on prompts or single models—is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here will be referenced repeatedly in all future implementation lessons. This ensures that every code-level choice stays aligned with our original cost, latency, and quality goals. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining the core research tools and orchestrating the process that produces the final `research.md` file. The implementation of the Brown workflow will follow in Lessons 19–22.

The real skill you are developing is the ability to make these system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable engineering practice.

## References

- [1] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv. https://arxiv.org/abs/2307.03172
- [2] What is the Model Context Protocol (MCP)?. (n.d.). Model Context Protocol. https://modelcontextprotocol.io/docs/getting-started/intro
- [3] What is the Model Context Protocol (MCP)?. (n.d.). Databricks. https://www.databricks.com/blog/what-is-model-context-protocol
- [4] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [5] Bouchard, L-F., & Peters, L. (2025, August 26). LLM System Design & Model Selection. O'Reilly. https://www.oreilly.com/radar/llm-system-design-and-model-selection/
- [6] Extended thinking & interleaved thinking docs. (n.d.). Claude. https://docs.claude.com/en/docs/build-with-claude/extended-thinking
- [7] Use Claude Messages with extended thinking. (n.d.). AWS. https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html
- [8] Raschka, S. (2025). Categories of Inference-Time Scaling for Improved LLM Reasoning. Ahead of AI. https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling
- [9] Revisiting the Test-Time Scaling of o1-like Models. (2025). arXiv. https://arxiv.org/html/2502.12215v1
- [10] API Pricing. (n.d.). OpenAI. https://openai.com/api/pricing/
- [11] Human-in-the-loop. (n.d.). LangChain. https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
- [12] Introducing Perplexity Deep Research. (2025, February 14). Perplexity. https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research
- [13] Deep Research. (n.d.). Google. https://gemini.google/overview/deep-research/