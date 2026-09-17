# Lesson 14: A Decision Framework for AI System Design

In the last two lessons, we defined the scope for our capstone project: two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. We chose our frameworks in Lesson 13, deciding Nova will ship as a set of portable FastMCP tools, while Brown will run as a durable, auditable LangGraph workflow. Now, we move from framework selection to system design.

This is the layer that determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads. Core design variables—like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement—each exert an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has vastly different design constraints than a high-accuracy overnight research job.

This lesson introduces a reusable 7-step decision playbook that moves systematically from business value to a concrete architectural blueprint. We will then apply this framework to our capstone, producing the global Nova-Brown architecture and a decision matrix you can reuse on your own projects. You will learn where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing quality.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### 1. Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define success. What is the quality bar for the output? What are the privacy or compliance requirements? What is the expected volume, and what is your per-task spending limit? These targets dictate every downstream choice. For instance, a real-time customer support bot demands sub-second latency, and moderate accuracy might be acceptable if it can escalate to a human. In contrast, a batch research job for a financial report may have a throughput measured in hours, but it requires a near-zero tolerance for hallucinations.

### 2. Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like Google, OpenAI, and Anthropic deliver state-of-the-art performance with low operational overhead. This path is ideal when you need access to the most powerful models without managing infrastructure. However, it comes with the risk of vendor lock-in and potential data privacy concerns.

Open-weight models like Llama, Mistral, or DeepSeek offer unparalleled control, privacy, and customization. They are the right choice when you must guarantee data locality for compliance or when you need to deeply fine-tune a model on proprietary data. The trade-off is the significant burden of managing your own GPU infrastructure, a complex and expensive undertaking.

### 3. Define Your Context Strategy

As we covered in previous lessons, a large context window is not a cure-all. A common mistake is to dump entire documents into a prompt, assuming the LLM can handle it. Research has shown this often leads to a "lost-in-the-middle" performance cliff, where models struggle to access information buried in the middle of long contexts [[32]](https://arxiv.org/abs/2307.03172).

Instead of naive full-document dumps, your strategy should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For a task that requires remembering the latest information in a long conversation, a sliding window or summarization approach might be best. For retrieving specific facts from a large knowledge base, RAG is the more effective choice.

### 4. Pick an Orchestration Style

The choice between predictable workflows and dynamic agents depends on the nature of your task. As we explored in Lesson 2, you should use predictable workflows for tasks that are auditable and follow a mostly linear sequence of steps. Dynamic agents are better suited for open-ended problems where tool use and planning are required. For many real-world systems, a hybrid design that combines both is the most effective solution.

### 5. Establish a HITL & Evaluation Loop

The level of autonomy you grant your system should be tied directly to the cost of an error. For high-stakes decisions or irreversible actions, building in HITL triggers is non-negotiable. These are not signs of failure but essential guardrails. You can define clear triggers for human intervention, such as when the model’s confidence score is low, when it attempts to perform a sensitive action like deleting a file, or when it flags a query for a policy review. For our capstone, we might trigger a human review for any research query above a certain ambiguity threshold or require a final human sign-off on the generated article.

### 6. Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic work to code. The LLM should decide *what* to do, but the code should handle *how* to do it. For example, an LLM can decide to calculate a financial metric, but the actual math should be executed by a validated Python function, not by the LLM itself.

This separation is where a standardized protocol like the Model Context Protocol (MCP) becomes valuable. As we will see, MCP allows you to define tools once and expose them to any compatible client—like an IDE or a chat interface—without tying your implementation to a single vendor or framework [[11]](https://www.guild.ai/glossary/ai-agent-portability), [[12]](https://www.databricks.com/blog/what-is-model-context-protocol), [[13]](https://openai.github.io/openai-agents-python/mcp), [[14]](https://www.ibm.com/think/topics/model-context-protocol), [[15]](https://en.wikipedia.org/wiki/Model_Context_Protocol). This enforces clean tool boundaries and ensures your agent's capabilities are portable.

### 7. Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand built-in checkpoints, resumability, and detailed tracing to survive failures and allow for debugging [[35]](https://docs.langchain.com/oss/python/langgraph/persistence), [[36]](https://medium.com/@okanyenigun/built-with-langgraph-17-checkpoints-2d1d54e1464b), [[37]](https://docs.langchain.com/oss/python/langgraph/overview), [[38]](https://use-apify.com/blog/langgraph-agents-production). A financial analysis agent that runs overnight cannot afford to start from scratch if one API call fails. In contrast, for a stateless task that can be retried from the beginning, a simple retry policy may suffice. Your choice here should link directly back to the reliability and success criteria you defined in the first step. This framework is iterative; you will likely revisit earlier steps as you uncover new constraints during implementation.

## Inference-Time Scaling and the Cost/Latency Calculus

Once you have framed the high-level decisions, you must quantify how each choice affects cost and latency. Four independent levers can be adjusted at runtime, often on a per-step basis, and understanding how they multiply is central to effective system design.

**Model Size Scaling** is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite. For a high-value task where accuracy is paramount, the expensive model may be justified. For high-volume, low-complexity tasks, a cheaper model is the better choice.

**Series Scaling** refers to increasing the internal computational steps a model takes before answering, often implemented as “thinking tokens.” This allows the model to perform a longer chain of thought, which can improve reasoning on complex problems [[6]](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html), [[7]](https://cobusgreyling.substack.com/p/building-with-claude-extended-thinking), [[8]](https://stevekinney.com/courses/ai-development/claude-code-thinking), [[9]](https://www.lesswrong.com/posts/qkfRNcvWz3GqoPaJk/anthropic-releases-claude-3-7-sonnet-with-extended-thinking), [[10]](https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a). However, research shows that longer reasoning chains do not always lead to better accuracy; in some cases, correct solutions are shorter than incorrect ones [[31]](https://arxiv.org/html/2502.12215v1). The key is to treat extra reasoning as a dial, activated only for the most complex planning or validation steps and strictly capped to control both cost and latency.

**Parallel Scaling** involves running the same prompt multiple times and selecting the best response, often through a majority vote—a technique known as self-consistency [[4]](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling). This adds a linear cost multiplier but can significantly improve reliability. For the same budget, studies suggest that beyond a certain point, parallel scaling can outperform additional serial reasoning [[31]](https://arxiv.org/html/2502.12215v1).

**Input Context Scaling** is the final lever. While more context can provide more signal, each additional token has a direct cost and adds latency. The goal is to find the optimal balance. Techniques like RAG, summarization, and caching help keep the effective context small while preserving the necessary information.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

To see how these levers multiply, let's contrast two designs for the same task.

A **naive design** might use the largest reasoning model, dump an entire 100,000-token document into the context, and run five parallel attempts for self-consistency.

*   **Model:** GPT-4.5 ($75.00 / 1M input tokens, $150.00 / 1M output tokens)
*   **Input Tokens:** 100,000
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 5
*   **Calculation:** (100,000 * $75/1M + 2,000 * $150/1M) * 5 = ($7.50 + $0.30) * 5 = **$39.00**

A **budgeted design** might use a fast "mini" model, use RAG to retrieve only the most relevant 1,000 tokens, and run a single pass.

*   **Model:** Gemini 2.5 Flash Lite ($0.10 / 1M input tokens, $0.40 / 1M output tokens)
*   **Input Tokens:** 1,000
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 1
*   **Calculation:** (1,000 * $0.10/1M + 2,000 * $0.40/1M) * 1 = ($0.0001 + $0.0008) * 1 = **$0.0009**

This simple shift in design choices results in a cost reduction of over 40,000x while potentially meeting the same quality target. Other optimizations, like prompt caching for repeated calls and delegating heavy computation to external tools, can further reduce costs. With the scaling levers quantified, we can now apply the full framework to produce a concrete global architecture for our capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The image above illustrates the core architectural principle of our capstone: a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP-driven agent. Predictable, iterative drafting and review are handled by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt.

For the MCP client, we use FastMCP’s built-in `Client` class, a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details out of the box. Our implementation is just around 200 lines of Python that wrap this client. It connects to the server, fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine [[16]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch), [[17]](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows), [[18]](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo). We front this powerful engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:

*   **Generate Article:** This orchestrates the entire writing workflow. It loads context (guidelines, research, profiles, examples), generates media items using the orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining context awareness of the full document.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This file-based contract ensures a clean separation of concerns, making the system modular, debuggable, and easier to maintain [[19]](https://fast.io/resources/ai-agent-artifacts), [[20]](https://blog.cloudflare.com/artifacts-git-for-agents-beta), [[21]](https://arxiv.org/html/2603.16021v1), [[22]](https://www.scitepress.org/Papers/2026/144223/144223.pdf).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, personal notes, or anything else they consider important. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill without instructions leads to the LLM generating hollow text. LLMs are amazing at translation and synthesis, but they are not good at generating original ideas. The architecture and diagrams are now concrete; the final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of our 7-step framework into specific, implementable defaults for the research (Nova) and writing (Brown) tasks. This is not an aspirational guide but the exact blueprint we will implement starting in the next lesson. Each row captures a decision dimension, our chosen default, and a rationale that links back to the cost, latency, reliability, or debuggability goals we established for the capstone. This matrix serves as a living document, preventing ad-hoc choices during implementation.

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

In this lesson, we introduced a structured 7-step decision framework for AI system design. We applied it to our capstone project, producing the clean Nova-versus-Brown global architecture, supporting diagrams, and a concrete decision matrix that will guide our implementation. Adopting this system-level view, rather than focusing only on prompts or individual models, is what turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here will be referenced repeatedly in all future implementation lessons. This ensures that every code-level choice stays aligned with our original cost, latency, and quality goals. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining the core research tools and orchestrating the process that produces our `research.md` file. Later, in Lessons 19–22, we will dive into the implementation of the Brown writing workflow. The real skill you are developing is the ability to make these system-level trade-offs repeatedly, turning AI engineering from an art into a repeatable engineering practice.

## References

- [1] What causes lost-in-the-middle performance cliff in LLMs? (https://atlan.com/know/llm/lost-in-the-middle-problem)
- [2] Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs (https://openreview.net/forum?id=XSHP62BCXN)
- [3] 'Lost in the middle' phenomenon of LLMs is an architectural and AI training problem (https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html)
- [4] Categories of Inference-Time Scaling for Improved LLM Reasoning (https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling)
- [5] LLM Optimization Techniques: A Guide to Faster, More Efficient Inference (https://www.mirantis.com/blog/llm-optimization-techniques)
- [6] Use extended thinking with Claude (https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html)
- [7] Building with Claude: Extended Thinking (https://cobusgreyling.substack.com/p/building-with-claude-extended-thinking)
- [8] Extended Thinking in Claude Code (https://stevekinney.com/courses/ai-development/claude-code-thinking)
- [9] Anthropic releases Claude 3.7 Sonnet, with extended thinking (https://www.lesswrong.com/posts/qkfRNcvWz3GqoPaJk/anthropic-releases-claude-3-7-sonnet-with-extended-thinking)
- [10] Claude 3.7 Sonnet Extended Thinking (https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a)
- [11] AI Agent Portability (https://www.guild.ai/glossary/ai-agent-portability)
- [12] What is the Model Context Protocol (MCP)? (https://www.databricks.com/blog/what-is-model-context-protocol)
- [13] Model context protocol (MCP) (https://openai.github.io/openai-agents-python/mcp)
- [14] Model Context Protocol (MCP): The key to interoperable AI (https://www.ibm.com/think/topics/model-context-protocol)
- [15] Model Context Protocol (https://en.wikipedia.org/wiki/Model_Context_Protocol)
- [16] Human-in-the-Loop (HITL) with LangGraph and Elasticsearch (https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch)
- [17] Building Human-In-The-Loop Agentic Workflows (https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows)
- [18] Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo (https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [19] What Is an AI Agent Artifact? (https://fast.io/resources/ai-agent-artifacts)
- [20] Announcing Artifacts: Git for Agents (beta) (https://blog.cloudflare.com/artifacts-git-for-agents-beta)
- [21] Stage Contracts: A File-Based Handoff Protocol for Hybrid AI Workflows (https://arxiv.org/html/2603.16021v1)
- [22] Artifact and Resume Services for Regulation-Aware AI Agents (https://www.scitepress.org/Papers/2026/144223/144223.pdf)
- [23] Decision Matrix for AI Projects (https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects)
- [24] The Decision Matrix Method for Engineering Trade-offs (https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45)
- [25] Agentic AI Explained: Workflows vs Agents (https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows)
- [26] Agents vs. Workflows: How to tell the difference? (https://www.reddit.com/r/AI_Agents/comments/1nwwb5g/agents_vs_workflows_how_to_tell_the_difference)
- [27] A Developer’s Guide to Building Scalable AI: Workflows vs. Agents (https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents)
- [28] AI Agents vs. Workflows: Why Not Both? (https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both)
- [29] AI Workflows vs. AI Agents (https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents)
- [30] LLM System Design & Model Selection (https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [31] Revisiting the Test-Time Scaling of o1-like Models (https://arxiv.org/html/2502.12215v1)
- [32] Lost in the Middle: How Language Models Use Long Contexts (https://arxiv.org/abs/2307.03172)
- [33] Extended thinking & interleaved thinking docs (https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [34] Human-in-the-loop (https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [35] Persistence (https://docs.langchain.com/oss/python/langgraph/persistence)
- [36] Built with LangGraph #17: Checkpoints (https://medium.com/@okanyenigun/built-with-langgraph-17-checkpoints-2d1d54e1464b)
- [37] Overview (https://docs.langchain.com/oss/python/langgraph/overview)
- [38] LangGraph agents in production (https://use-apify.com/blog/langgraph-agents-production)
- [39] What is the Model Context Protocol (MCP)? (https://modelcontextprotocol.io/docs/getting-started/intro)
- [40] API Pricing (https://openai.com/api/pricing/)