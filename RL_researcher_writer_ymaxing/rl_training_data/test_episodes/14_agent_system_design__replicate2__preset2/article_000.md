# Lesson 14: A Decision Framework for Production-Ready Agents

In Lesson 12, we defined the scope of our capstone project: two production-oriented agents that collaborate to produce publish-ready technical articles. We have the research agent, Nova, and the writing workflow, Brown. In Lesson 13, we compared agent frameworks and chose our stack: Nova will ship as FastMCP tools for portability, while Brown will run a durable LangGraph workflow, also fronted by FastMCP.

With our frameworks selected, we now move to system design. This is the layer that determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads. This shift to system-level thinking is crucial because AI agents represent a new software paradigm. Unlike traditional software where decision logic is pre-encoded by engineers, an agent's logic is generated at runtime, making the architectural choices that constrain it paramount [[17]](https://arxiv.org/html/2606.05608). Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement have an order-of-magnitude impact on cost, latency, and reliability.

This lesson introduces a reusable 7-step decision playbook that moves from business value to a concrete system architecture. We will then apply this framework to our capstone, producing the global Nova-versus-Brown architecture, complete with component interaction diagrams and a decision matrix you can reuse on future projects. By the end, you will know where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal.

With the stakes clear, we will now walk through the general 7-step framework before specializing it for the capstone.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook guides you from a problem statement to a design that balances capability, cost, and reliability.

### 1. Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice. For example, a real-time customer support bot needs sub-second latency and can tolerate moderate accuracy, while a batch research job for a legal firm requires near-zero hallucination tolerance, with throughput measured in hours.

### 2. Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Anthropic, and Google deliver state-of-the-art performance with low operational overhead but can lead to vendor lock-in. Open-weight models such as those from Meta, Mistral, and DeepSeek guarantee privacy, deep customization through fine-tuning, and data locality, but place the entire burden of GPU management and infrastructure security on your team [[1]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/).

### 3. Define Your Context Strategy

As we saw in previous lessons, a large context window is not a silver bullet. A common mistake is to dump everything into a prompt, assuming the LLM can handle it. This naive approach often leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts [[2]](https://arxiv.org/abs/2307.03172), [[3]](https://openreview.net/forum?id=XSHP62BCXN). This U-shaped performance curve is a byproduct of how attention mechanisms work, with primacy and recency biases causing models to recall information from the beginning and end of a context far more reliably than from the middle [[18]](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf).

Instead of relying on raw context volume, you should prioritize selective retrieval, compression, and structured summaries to manage cost and improve reliability. For a chatbot that needs to remember recent interactions, a sliding window or summarization approach is suitable for managing conversational history [[4]](https://medium.com/@levi_stringer/simplifying-rag-context-windows-with-conversation-buffers-how-to-stop-your-agent-forgetting-df2149ad7403). For an agent answering questions from a large knowledge base, RAG is the better choice to identify and retrieve only the most relevant information for the current query [[5]](https://www.meilisearch.com/blog/rag-vs-long-context-llms).

### 4. Pick an Orchestration Style

The choice between a predictable workflow and a dynamic agent depends on the task's nature. Use a structured workflow when the steps are known, repeatable, and need to be auditable and reliable at scale. This is ideal for processes like claims processing or generating a monthly report. Use a dynamic agent when the path is unclear and requires exploration, reasoning, and adaptive tool use, such as diagnosing a system failure or conducting open-ended research [[6]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows), [[7]](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both). Hybrid designs, which we will use in our capstone, combine both styles to leverage the strengths of each.

### 5. Establish a HITL & Evaluation Loop

You must decide where to insert human oversight. This decision is tied to the cost of error and business risk. Instead of aiming for full autonomy from the start, define clear triggers for human intervention. These can be based on low-confidence scores from the model, requests for sensitive actions like financial transactions, or flags for policy violations. LangGraph's interrupt mechanism is a powerful tool for this, allowing you to pause a workflow, wait for human approval, and then resume execution cleanly [[8]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/), [[9]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch). This creates a safety net that makes agentic systems practical for high-stakes environments.

### 6. Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic work to code. For example, an LLM should decide to calculate a financial metric, but the calculation itself should be executed by a dedicated Python function, not by the LLM's internal reasoning. This separation of concerns improves reliability and reduces computational load on the model.

Furthermore, protocols like the Model Context Protocol (MCP) enforce clean tool boundaries and enable portability [[10]](https://modelcontextprotocol.io/docs/getting-started/intro), [[11]](https://www.databricks.com/blog/what-is-model-context-protocol). MCP standardizes how agents connect to external tools, acting like a USB-C port for AI. This allows you to build a tool once and expose it to any MCP-compatible client, such as an IDE or another agent, preventing vendor lock-in and making your tools reusable across different environments [[12]](https://www.guild.ai/glossary/ai-agent-portability).

### 7. Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand durability features like resumability and checkpoints to survive failures. A framework like LangGraph provides this out-of-the-box, saving the graph's state at each step [[13]](https://docs.langchain.com/oss/python/langgraph/persistence). For simple, stateless tasks, a basic retry policy may suffice. Your choice should align with the success criteria from Step 1. A critical batch process needs full tracing and resumability, while a non-essential, transient task does not.

Applying this framework helps you avoid common agent failure modes that differ from classic software bugs. These include **context degradation**, where agents lose track of information over long interactions; **cascading failures**, where a small error in an early step silently propagates and corrupts the entire workflow; and **silent failures**, where the agent completes a task and returns a plausible but incorrect result without raising an error [[19]](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition).

This framework is iterative. You will likely revisit earlier steps as new constraints and insights emerge during implementation. Once these high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency to budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

The four inference-time levers can be understood through the lens of control systems theory, where each acts as a knob to regulate the system's cost, latency, and quality. This reframes the goal from simply "prompting" to actively steering a dynamic system [[20]](https://arxiv.org/html/2602.03433v1). Understanding how to manage cost and latency at runtime is central to effective system design. There are four independent levers you can adjust, often on a per-step basis, to trade performance for cost. Their multiplicative effect means that seemingly small choices can lead to a 1000x difference in spend.![The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies. (Source [https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling))

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite [[14]](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source:). For a high-value task where mistakes are expensive, a frontier model is a sound investment. For high-volume, low-stakes tasks like simple data categorization, a cheaper "flash" or "mini" model is more appropriate.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often implemented as "thinking tokens" or a longer chain of thought. For example, Anthropic's Claude models offer an "extended thinking" mode where you can set a token budget for internal reasoning [[15]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This approach can decouple intelligence from model size, as a smaller model with an adequate thinking budget can sometimes outperform a larger one [[21]](https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained). However, this lever has diminishing returns; longer reasoning chains do not always improve accuracy [[16]](https://arxiv.org/html/2502.12215v1), [[22]](https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token). The key is to treat extra reasoning as a dial, activating it only for complex planning or validation steps and capping it to bound both cost and latency.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response. A common technique is self-consistency, where the final answer is chosen by a majority vote among several generated outputs. This can improve reliability, and research suggests that beyond a certain point, parallel scaling can outperform additional serial reasoning for the same budget [[16]](https://arxiv.org/html/2502.12215v1). The trade-off is a linear increase in cost for each parallel run.

### Input Context Scaling

While providing more context can help an LLM, each additional token carries a direct cost and adds to latency. As discussed, models also struggle with the "lost-in-the-middle" problem, so simply increasing context size can be counterproductive. The goal is to find the optimal balance. Techniques like RAG, summarization, and prompt caching help keep the effective context small while preserving the necessary signal.

A powerful pattern combining these levers is **inference-time distillation**. Here, a cheap "student" model handles most tasks using in-context examples from an expensive "teacher" model. The system only falls back to the teacher when the student's confidence is low (detected via self-consistency). This adaptive cascade can reduce costs by 2-4x while matching teacher accuracy, without any fine-tuning [[23]](https://openreview.net/forum?id=nCEdAM5m5T).

To see how these levers multiply, consider two designs for a research task.

**A naive design might:**
*   **Model:** Use the largest reasoning model (e.g., GPT-4.5 at $75/M input tokens).
*   **Input Tokens:** Dump a full 100-page document (approx. 50,000 tokens) into the context.
*   **Output Tokens:** Allow for a long, detailed response (e.g., 4,000 tokens).
*   **Number of Parallel Runs:** Use five parallel runs for self-consistency.
*   **Calculation:** (50,000 * $75/M + 4,000 * $150/M) * 5 runs = **$21.75 per task**.

**A budgeted design might:**
*   **Model:** Use a fast, cheap model for initial summarization (e.g., Gemini 2.5 Flash at $0.30/M input tokens) and a mid-tier model for the final answer (e.g., GPT-4o at $2.50/M input tokens).
*   **Input Tokens:** Use RAG to retrieve the 5 most relevant chunks (approx. 2,000 tokens).
*   **Output Tokens:** Generate a concise answer (e.g., 1,000 tokens).
*   **Number of Parallel Runs:** Use a single run.
*   **Calculation:** (2,000 * $2.50/M + 1,000 * $10/M) * 1 run = **$0.015 per task**.

The budgeted design achieves a greater than 1000x cost reduction while potentially delivering similar or even better quality by providing focused context. Other optimizations, like prompt caching and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

```mermaid
flowchart LR
  %% External Systems / Entry Points
  subgraph "External Systems"
    FastMCP_Client["FastMCP<br/>(Nova Client)"]
    ArticleGuidelines["article_guideline.md"]
    WritingProfiles["writing profiles"]
  end

  %% Agent Nova
  subgraph "Agent Nova"
    Nova["Exploration-focused MCP Agent"]
    HITL_Nova["HITL Trigger<br/>(Nova)"]
  end

  %% Agent Brown
  subgraph "Agent Brown"
    FastMCP_Brown["FastMCP<br/>(Brown Workflow Front)"]
    Brown["Execution-focused LangGraph Workflow"]
    HITL_Brown["HITL Trigger<br/>(Brown)"]
  end

  %% Outputs
  subgraph "System Outputs"
    ArticleMD["article.md"]
    Assets["assets"]
    ReviewArtifacts["review artifacts"]
  end

  %% Connections
  FastMCP_Client -- "triggers" --> Nova
  HITL_Nova -. "monitors / intervenes" .-> Nova

  Nova -- "produces" --> ResearchMD["research.md"]
  Nova -- "produces" --> NovaDir[".nova/ directory"]

  ResearchMD -- "input for" --> Brown
  NovaDir -- "input for" --> Brown

  ArticleGuidelines -- "provides" --> Brown
  WritingProfiles -- "provides" --> Brown

  FastMCP_Brown -- "fronts workflow<br/>(MCP Tools)" --> Brown
  HITL_Brown -. "monitors / intervenes" .-> Brown

  Brown -- "generates" --> ArticleMD
  Brown -- "generates" --> Assets
  Brown -- "generates" --> ReviewArtifacts

  %% Visual Grouping
  classDef agent stroke-width:2px
  classDef trigger stroke-dasharray:5,5
  class Nova,Brown agent
  class HITL_Nova,HITL_Brown trigger
```
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The core architectural principle of our capstone, illustrated in Image 2, is a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently.

This separation of exploration from execution is a well-established pattern in robotics and complex agent design. A "planner" agent first decomposes a problem and formulates a strategy, similar to Nova's research phase. A separate "execution" agent then carries out the plan, interacting with tools and external systems, analogous to Brown's writing workflow. This division of labor improves reliability and modularity [[24]](https://arxiv.org/html/2505.02024v2). Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a "Research Recipe" retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape them, run iterative research loops, filter results, select top sources for a full scrape, and compile everything into a `research.md` file.

For the client, we use FastMCP’s built-in `Client` class, a lightweight, ready-to-use component that handles all protocol details. Our implementation is a ~200-line Python script that wraps this client. It connects to the server, fetches the research prompt, and runs a ReAct-style loop where the LLM decides which tool to call next. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures.![End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration, which manages state, checkpoints, and interrupts. We front this durable engine with a FastMCP server, exposing Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

This hybrid design, combining LangGraph's structured control with MCP's contextual intelligence for tool use, reflects an emerging trend in multi-agent orchestration. It provides a fault-tolerant and replayable framework that overcomes the static nature of older multi-agent systems, establishing a foundation for scalable and interpretable agent collaboration [[25]](https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp).

The exposed tools are:
*   **Generate Article:** This orchestrates a full workflow: loading context (guidelines, research, profiles), generating media items using the orchestrator-worker pattern, writing a first draft, and then running review-edit cycles.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article for targeted revisions.![Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean contract makes the system modular and debuggable.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what to write, the narrative, and other important notes. Since the writing is automated, a clear, well-articulated guideline is what distinguishes a high-quality article from generic AI-generated slop. If ideas are not clearly enumerated and connected, the output will be sloppy. LLMs are excellent at translation and synthesis but poor at generating original ideas. Leaving too many gaps for the AI to fill without instruction leads to hollow text.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework now become specific, implementable defaults tailored to the distinct demands of research (Nova) and writing (Brown). This matrix is the exact blueprint we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, our chosen default, and the rationale linking it to our goals for cost, latency, reliability, or debuggability. This matrix serves as a living document to prevent ad-hoc choices during implementation.

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process yielded a clean global architecture separating the Nova research agent from the Brown writing workflow, supported by clear component diagrams and a concrete decision matrix. Adopting this system-level view, rather than focusing only on prompts or single models, is the foundation for turning prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have established will be referenced repeatedly in our upcoming implementation lessons. This ensures every code-level choice stays aligned with our original goals for cost, latency, and quality. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining the core research tools and orchestrating the process that produces the final `research.md` file. Later, in Lessons 19–22, we will build the Brown workflow.

The real skill you are developing is the ability to make these system-level trade-offs repeatedly. This discipline turns AI engineering from an art into a repeatable practice and is what separates prototypes from production systems. It elevates the role of AI from a reactive tool that simply answers questions to a proactive partner that can monitor, detect, and act autonomously within a governed workflow, with humans providing critical oversight [[26]](https://hdsr.mitpress.mit.edu/pub/fdzqkh85). Ultimately, building robust agents is 90% software engineering and 10% AI, a reality this framework helps you master [[27]](https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M).

## References

- [1] Louis-Francois Bouchard and Louie Peters. (2025, August 26). LLM System Design & Model Selection. O'Reilly. [https://www.oreilly.com/radar/llm-system-design-and-model-selection/](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [2] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv. [https://arxiv.org/abs/2307.03172](https://arxiv.org/abs/2307.03172)
- [3] Salvatore, N., Wang, H., & Zhang, Q. (2026). Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs. OpenReview. [https://openreview.net/forum?id=XSHP62BCXN](https://openreview.net/forum?id=XSHP62BCXN)
- [4] Stringer, L. (2024). Simplifying RAG & Context Windows with Conversation Buffers. Medium. [https://medium.com/@levi_stringer/simplifying-rag-context-windows-with-conversation-buffers-how-to-stop-your-agent-forgetting-df2149ad7403](https://medium.com/@levi_stringer/simplifying-rag-context-windows-with-conversation-buffers-how-to-stop-your-agent-forgetting-df2149ad7403)
- [5] RAG vs Long Context LLMs. Meilisearch. (n.d.). [https://www.meilisearch.com/blog/rag-vs-long-context-llms](https://www.meilisearch.com/blog/rag-vs-long-context-llms)
- [6] Agentic AI Explained: Workflows vs Agents. Orkes. (2025, May 19). [https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows)
- [7] Agents vs. Workflows: Why Not Both? Tellius. (n.d.). [https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both)
- [8] Human-in-the-loop. LangChain. (n.d.). [https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [9] Human-in-the-loop (HITL) with LangGraph and Elasticsearch. Elastic. (n.d.). [https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch)
- [10] What is the Model Context Protocol (MCP)? Model Context Protocol. (n.d.). [https://modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)
- [11] What is the Model Context Protocol (MCP)? Databricks. (n.d.). [https://www.databricks.com/blog/what-is-model-context-protocol](https://www.databricks.com/blog/what-is-model-context-protocol)
- [12] AI Agent Portability. Guild.AI. (n.d.). [https://www.guild.ai/glossary/ai-agent-portability](https://www.guild.ai/glossary/ai-agent-portability)
- [13] Persistence. LangChain. (n.d.). [https://docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [14] AI Model Pricing and Specifications. Towards AI, Company Reports, & LiveBench. (n.d.). [https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source:](https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source:)
- [15] Extended thinking & interleaved thinking docs. Anthropic. (n.d.). [https://docs.claude.com/en/docs/build-with-claude/extended-thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [16] Revisiting the Test-Time Scaling of o1-like Models. (2025). arXiv. [https://arxiv.org/html/2502.12215v1](https://arxiv.org/html/2502.12215v1)
- [17] The Agent is the new Software. (2026). arXiv. [https://arxiv.org/html/2606.05608](https://arxiv.org/html/2606.05608)
- [18] Lost in the Middle: How Language Models Use Long Contexts. (2023). Stanford University. [https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf)
- [19] AI Agent Failure Pattern Recognition. MindStudio. (n.d.). [https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition)
- [20] The Unreasonable Convergence of Control and Large Language Models. (2026). arXiv. [https://arxiv.org/html/2602.03433v1](https://arxiv.org/html/2602.03433v1)
- [21] What is Inference-Time Compute? The AI Pivot Explained. MindStudio. (n.d.). [https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained](https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained)
- [22] Qwen2-Instruct "thinks" when token generation is constrained. Kaitchup. (n.d.). [https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token](https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token)
- [23] Inference-Time Distillation: Cost-Efficient Agents Without Fine-Tuning or Manual Prompt Engineering. (n.d.). OpenReview. [https://openreview.net/forum?id=nCEdAM5m5T](https://openreview.net/forum?id=nCEdAM5m5T)
- [24] Manus: An Agentic AI Framework for Human-like Computer Control. (2025). arXiv. [https://arxiv.org/html/2505.02024v2](https://arxiv.org/html/2505.02024v2)
- [25] Orchestrating Multi-Agent Systems with LangGraph & MCP. Healthark AI. (n.d.). [https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp](https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp)
- [26] AI Agents Are Transforming Decision Making: What Leaders Should Know. (n.d.). MIT Press. [https://hdsr.mitpress.mit.edu/pub/fdzqkh85](https://hdsr.mitpress.mit.edu/pub/fdzqkh85)
- [27] AI Agents are about 90% Software engineering and only 10% AI. LinkedIn. (n.d.). [https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M](https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M)