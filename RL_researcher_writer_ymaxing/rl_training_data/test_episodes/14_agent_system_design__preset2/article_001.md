# The AI Engineer's Decision Framework: From Prototype to Production Agent

In the last two lessons, we defined the capstone project for this course: two production-oriented agents that collaborate to produce publish-ready technical articles. In Lesson 12, we scoped the research agent, Nova, and the writing workflow, Brown. In Lesson 13, we chose our frameworks: Nova will ship as portable FastMCP tools, while Brown will run a durable LangGraph workflow.

With those foundational choices made, we now move to system design. This layer separates a polished product from a fragile demo that collapses under real workloads. Agentic systems represent a fundamental shift in software engineering: for decades, humans encoded decision logic into static code, but now the agent *is* the software, generating its logic at runtime [[41]](https://arxiv.org/html/2606.05608). This changes how we must think about design. Core variables like reasoning budgets, context strategy, and human-in-the-loop (HITL) placement have an order-of-magnitude impact on cost, latency, and reliability. A real-time support bot has different needs than a high-accuracy overnight research job.

This lesson provides a reusable 7-step decision playbook that moves from business goals to a concrete system architecture. We will apply this framework to our capstone, producing the global Nova-Brown architecture and a decision matrix you can reuse. You will learn where to spend thinking tokens, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing quality. With the stakes clear, let's walk through the general 7-step framework before applying it to our capstone.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define success. What is the quality bar for the output? What are the privacy or compliance requirements? What is the expected volume of tasks? And what are your per-task spending and latency limits? These targets dictate every downstream choice. For example, a real-time support bot needs sub-second latency, and moderate accuracy might be acceptable. In contrast, a batch research job for a legal team has a throughput measured in hours and a near-zero tolerance for hallucinations.

To formalize these trade-offs, you can use a decision matrix. This involves listing your criteria (e.g., cost, accuracy, latency), assigning weights based on their importance, and scoring each design option against them. This structured process forces explicit prioritization and provides a clear rationale for your architectural choices, moving beyond intuition [[23]](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects), [[4]](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45).

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like Google, OpenAI, or Anthropic deliver state-of-the-art performance with low operational overhead. However, they can lead to vendor lock-in, where your system is vulnerable to unexpected API changes or deprecations. Open-weight models guarantee privacy, deep customization, and data locality since you host them yourself. The trade-off is the significant burden of managing and scaling your own GPU infrastructure, which requires specialized expertise and can be costly.

A powerful pattern is *inference-time distillation*, where a capable “teacher” model generates examples to guide a cheaper “student” model at runtime. This allows the student to perform complex tasks at a fraction of the cost, without any fine-tuning [[42]](https://openreview.net/forum?id=nCEdAM5m5T).

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not a magic solution. A common mistake is to dump everything into a prompt, assuming the LLM can handle it. Research shows this leads to a "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of a long context [[1]](https://arxiv.org/abs/2307.03172), [[2]](https://openreview.net/forum?id=XSHP62BCXN), [[3]](https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html). This U-shaped performance curve is a result of cognitive biases mirrored in the model's attention mechanism: primacy and recency effects cause information at the beginning and end of a long context to be recalled far more reliably than information in the middle [[43]](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf). Instead of naive full-document dumps, you should prioritize selective retrieval, compression, and structured summaries to manage cost and improve reliability. For a chatbot that needs to remember recent turns, a sliding window summarization is a cost-effective way to manage context [[29]](https://www.meilisearch.com/blog/rag-vs-long-context-llms). For an agent answering questions from a knowledge base, RAG is the right tool to identify and retrieve only the most relevant information [[30]](https://atlan.com/know/context-engineering-vs-rag).

### Pick an Orchestration Style

The choice between predictable workflows and dynamic agents depends on the task. As we discussed, workflows are ideal when the steps are known, repeatable, and need to be auditable and reliable at scale [[27]](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both). Use them for processes like the `agentic_research` workflow in Orkes Conductor, which follows a structured path for searching, synthesizing, and reporting [[24]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows). Agents are better suited for open-ended problems where the path is not clear, such as the deep research features in Perplexity or Gemini that autonomously explore topics [[10]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research), [[8]](https://gemini.google.com/overview/deep-research/). Hybrid designs, which combine both, are often the most powerful solution for complex enterprise systems, like our capstone project [[26]](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents).

### Establish a HITL & Evaluation Loop

Full autonomy is risky. The decision to insert HITL triggers should be tied directly to error cost and business risk. You need to define clear triggers for human intervention, such as when the model's confidence score is low, when it attempts to perform a sensitive action like deleting a file, or when it flags a policy violation. This helps mitigate unique agent failure modes. A *cascading failure* occurs when a small, early error propagates and corrupts the entire workflow. A *silent failure* is when the agent returns a confident but completely wrong result, with no error signals to flag the mistake [[44]](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition). For example, a legal research agent might require human approval before finalizing a brief, whereas a simple content summarizer might run autonomously. Using a framework like LangGraph, you can build these interruption points directly into your workflow, allowing a person to validate or edit the agent's work before it proceeds [[16]](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch), [[17]](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows).

### Set Tool Boundaries & Portability

A well-designed system keeps the LLM responsible for intent detection and high-level planning, while delegating deterministic work to code. For example, an LLM should not be asked to perform arithmetic; it should call a calculator tool. This separation of concerns improves reliability and reduces cost. Furthermore, standardizing how tools are exposed to agents is essential for portability. The Model Context Protocol (MCP) provides a standard interface, like a USB-C port for AI, allowing you to define a tool once and use it across different agents, clients, and IDEs without being locked into a single vendor's ecosystem. This solves the "N×M integration problem," where each of M clients needs a custom integration for each of N tools, by creating a single, reusable connection point [[11]](https://www.guild.ai/glossary/ai-agent-portability), [[12]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Durability & Observability

Finally, your choice of infrastructure depends on the job's requirements. For long-running, stateful tasks like our article-writing agent, you need durability. This means the system must have built-in checkpoints and resumability so that it can recover from failures without starting from scratch. LangGraph's `checkpointer` objects, for instance, save the graph's state at every step, enabling fault-tolerant execution [[34]](https://docs.langchain.com/oss/python/langgraph/persistence). For simple, stateless tasks that can be retried easily, a basic retry policy may suffice. Without good observability, costs can silently inflate from patterns like unbounded RAG searches or verbose logging. Real-time cost observability—attributing spend to specific requests or agents—is what makes monitoring and control possible [[45]](https://www.cloudzero.com/blog/inference-cost), [[46]](https://www.mirantis.com/blog/inference-costs). This choice links directly back to the success criteria you defined in the first step.

This framework is iterative. You will often revisit earlier steps as you uncover new constraints during implementation. Once the high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency to budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding and controlling the four independent runtime levers that scale inference-time compute is central to effective system design. Each can be adjusted on a per-step basis, and their interactions are multiplicative, creating a massive dynamic range for cost and performance.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash [[14]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/), [[15]](https://openai.com/api/pricing/). For high-stakes tasks where accuracy is paramount, a frontier model is often justified. For high-volume, low-complexity tasks like routing customer queries, a cheaper model is the better choice.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often implemented as "thinking tokens" in models like Claude or through longer chains of thought [[6]](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html). These extra reasoning steps should be treated as a dial, activated only for the most complex planning or validation steps. A good practice is to set a strict budget, like a maximum of 8,000 thinking tokens, rather than letting the model "think until perfect," which can lead to unbounded costs and latency. More is not always better. Research shows that beyond a certain point, simply increasing the thinking token budget can lead to diminishing returns, where additional computation does not yield meaningful accuracy gains [[47]](https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token). This is because inference-time compute helps decouple raw intelligence from model size; a well-designed 7B parameter model can outperform a 70B model on certain tasks when given sufficient thinking time [[48]](https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained). Some models also support *interleaved thinking*, where the model thinks, calls a tool, and then thinks again about the result before proceeding [[7]](https://cobusgreyling.substack.com/p/building-with-claude-extended-thinking).

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, known as self-consistency, can significantly improve reliability for tasks with deterministic answers, like math problems. Research indicates that for a given budget, parallel scaling can sometimes outperform additional serial reasoning [[40]](https://arxiv.org/html/2502.12215v1). However, the reliability gains come at a linear cost multiplier. This enables cost-saving patterns like *cascades*. For example, if multiple samples from a cheap model disagree (low self-consistency), the system can “cascade” the query to an expensive model. This reserves the expensive model for only the most ambiguous steps [[42]](https://openreview.net/forum?id=nCEdAM5m5T).

### Input Context Scaling

While relevant information is valuable, each additional token carries a direct cost and adds to latency. As we have discussed, "lost-in-the-middle" issues mean that simply providing more context does not guarantee better performance [[1]](https://arxiv.org/abs/2307.03172). The key is to find the optimal balance. Techniques like RAG, summarization, and caching keep the effective context small while preserving the necessary signal.![The four independent levers that drive runtime cost and latency in LLM agent systems.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

To see how these levers multiply, consider this simplified but illustrative cost calculation. A naive design might use the largest reasoning model, dump an entire document into the context, and run five parallel attempts for reliability. A budgeted design for the same task might use a fast mini-model, retrieve relevant chunks with RAG, and use a single pass. The difference in cost can easily be 1000x or more.

**Naive Design:**
*   **Model:** GPT-4.5 ($75/M input, $150/M output)
*   **Input Tokens:** 100,000 (full document)
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 5
*   **Calculation:** (100k * $75/M + 2k * $150/M) * 5 = ($7.50 + $0.30) * 5 = **$39.00**

**Budgeted Design:**
*   **Model:** Gemini 2.5 Flash ($0.30/M input, $2.50/M output)
*   **Input Tokens:** 4,000 (RAG chunks + query)
*   **Output Tokens:** 2,000
*   **Number of Parallel Runs:** 1
*   **Calculation:** (4k * $0.30/M + 2k * $2.50/M) * 1 = ($0.0012 + $0.005) * 1 = **$0.0062**

Additional optimizations like per-step reasoning caps, prompt caching, and delegating heavy computation to external tools can further reduce costs. With the scaling levers quantified, we can now apply the full framework to produce the concrete global architecture for our capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a more detailed architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, collaborate to automate research and writing.![Global architecture diagram showing Nova (research agent) and Brown (writing workflow) interacting via file-based artifacts.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The image above illustrates the core architectural principle of our capstone: a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP agent, while predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. This split between exploration and execution is a pattern borrowed from fields like robotics, where a “leader” agent might map a space before “executor” agents explore assigned zones. This separation prevents conflicts and ensures efficient coverage—principles we apply to our information space [[49]](https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf). Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” retrieved from the server. This recipe guides the agent through a multi-step process: querying sources, scraping and transcribing them, running iterative research loops, filtering results, selecting top sources for a full scrape, and compiling everything into a `research.md` file.

For the MCP client, we use FastMCP’s built-in `Client` class. This lightweight client connects to our server and handles all protocol details like capability discovery and tool calling. Our implementation is just a ~200-line Python wrapper around this client. It connects to the server, fetches the research prompt, and runs a simple ReAct-style loop where the LLM decides which tool to call next, executes it via `client.call_tool()`, and feeds the result back into the conversation. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures.![Flowchart of the Nova research agent, showing steps from query to research.md output.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call. This approach reflects an emerging trend in multi-agent orchestration. LangGraph provides the programmable, stateful graph needed for durable workflows with checkpoints and recovery, while MCP provides the standardized, portable interface for tool use. Together, they create a system that is both resilient and interoperable, overcoming the limitations of simpler agent loops [[50]](https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp).

The exposed tools are:
*   **Generate Article:** This orchestrates a full workflow: it loads context (guidelines, research, profiles), generates media items using an orchestrator-worker pattern, writes a first draft, and then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.
*   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.
*   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article for targeted revisions.![Sequence diagram for Brown's "Generate Article" workflow, showing interactions between components.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This clean separation of concerns, where each stage's output becomes the next stage's input, makes the system modular, debuggable, and easier to maintain. This concept of a "file-based contract" ensures that the interface between the two agents is explicit and inspectable [[19]](https://fast.io/resources/ai-agent-artifacts), [[21]](https://arxiv.org/html/2603.16021v1).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where you define what you want to write, the narrative of the article, and any personal notes. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill leads to hollow text. LLMs are excellent at translation and synthesis, but they are not sources of original ideas.

The architecture and diagrams are now concrete. The final step is to translate these framework principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

The abstract principles from our 7-step framework now become specific, implementable defaults tailored for the distinct demands of research (Nova) versus writing (Brown). This matrix is the exact blueprint we will implement starting in the next lesson. It is a living document that prevents ad-hoc choices during coding. Each row captures a decision, the chosen default, and a rationale that links back to our goals for cost, latency, reliability, and debuggability.

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

In this lesson, we introduced a structured 7-step decision framework and applied it directly to our capstone project. This process produced the clean Nova-versus-Brown global architecture, three supporting diagrams, and a concrete decision matrix. It forced us to make deliberate trade-offs on model tiers, reasoning budgets, context strategies, and HITL policies. Adopting this system-level view—rather than focusing only on prompts or single models—is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams recorded in this lesson will be referenced repeatedly in all future implementation lessons. This ensures that every code-level choice stays aligned with our original goals for cost, latency, and quality. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining our core research tools and orchestrating the multi-round research and filtering process that produces the final `research.md` file. The implementation of the Brown workflow will follow in Lessons 19–22.

Mastering these system-level trade-offs is the core skill that turns AI engineering from an art into a repeatable practice. You are learning to build a new kind of software—one where decision logic is no longer pre-encoded by a human, but generated dynamically at runtime. Mastering the architectural principles that make such systems reliable, cost-effective, and observable is the core skill of the modern AI engineer [[41]](https://arxiv.org/html/2606.05608).

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs](https://openreview.net/forum?id=XSHP62BCXN)
- [3] ['Lost in the middle' phenomenon not just an LLM architecture flaw, AI researchers find](https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html)
- [4] [The Decision Matrix Method for Engineering Trade-Offs](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45)
- [5] [Categories of Inference-Time Scaling for LLMs](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling)
- [6] [Use extended thinking with Claude](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html)
- [7] [Building with Claude: Extended Thinking](https://cobusgreyling.substack.com/p/building-with-claude-extended-thinking)
- [8] [Gemini Review](https://gemini.google/overview/deep-research/)
- [9] [Anthropic releases Claude 3.7 Sonnet, with "extended thinking"](https://www.lesswrong.com/posts/qkfRNcvWz3GqoPaJk/anthropic-releases-claude-3-7-sonnet-with-extended-thinking)
- [10] [Intro to Perplexity](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [11] [AI Agent Portability](https://www.guild.ai/glossary/ai-agent-portability)
- [12] [What is the Model Context Protocol (MCP)?](https://www.databricks.com/blog/what-is-model-context-protocol)
- [13] [Model context protocol (MCP)](https://openai.github.io/openai-agents-python/mcp)
- [14] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [15] [API Pricing](https://openai.com/api/pricing/)
- [16] [Human-in-the-Loop with LangGraph and Elasticsearch for Enhanced RAG](https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch)
- [17] [Building Human-in-the-Loop Agentic Workflows](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows)
- [18] [Human-in-the-Loop for AI Agents: Best Practices, Frameworks, Use Cases, and Demo](https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo)
- [19] [AI Agent Artifacts](https://fast.io/resources/ai-agent-artifacts)
- [20] [Artifacts is Git for Agents (Beta)](https://blog.cloudflare.com/artifacts-git-for-agents-beta)
- [21] [Interpretable Context Methodology: Folder Structure as Agent Architecture](https://arxiv.org/html/2603.16021v1)
- [22] [Artifact and Resume Services for Legal Agent Workflows](https://www.scitepress.org/Papers/2026/144223/144223.pdf)
- [23] [Decision Matrix for AI Projects](https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects)
- [24] [Agentic AI Explained: Workflows vs Agents](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows)
- [25] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [26] [A Developer’s Guide to Building Scalable AI: Workflows vs. Agents](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents)
- [27] [Agents vs. Workflows: Why Not Both?](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both)
- [28] [AI Workflows vs. AI Agents](https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents)
- [29] [RAG vs. Long Context LLMs](https://www.meilisearch.com/blog/rag-vs-long-context-llms)
- [30] [Context Engineering vs RAG](https://atlan.com/know/context-engineering-vs-rag)
- [31] [RAG vs. Large Context Window in AI Apps](https://redis.io/blog/rag-vs-large-context-window-ai-apps)
- [32] [Is summarized context (sliding window) the best memory type for a chatbot?](https://learn.microsoft.com/en-gb/answers-questions/2259997/is-summarized-context-sliding-window-the-best-memo)
- [33] [Simplifying RAG & Context Windows With Conversation Buffers. How to Stop Your Agent Forgetting.](https://medium.com/@levi_stringer/simplifying-rag-context-windows-with-conversation-buffers-how-to-stop-your-agent-forgetting-df2149ad7403)
- [34] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [35] [Built with LangGraph #17: Checkpoints](https://medium.com/@okanyenigun/built-with-langgraph-17-checkpoints-2d1d54e1464b)
- [36] [Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [37] [How to build production-ready LangGraph agents](https://use-apify.com/blog/langgraph-agents-production)
- [38] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [39] [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [40] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [41] [The End of Software](https://arxiv.org/html/2606.05608)
- [42] [Inference-Time Distillation: Cost-Efficient Agents Without Fine-Tuning or Manual Prompt Engineering](https://openreview.net/forum?id=nCEdAM5m5T)
- [43] [Lost in the Middle: How Language Models Use Long Contexts](https://cs.stanford.edu/~nfliu/papers/lost-in-the-middle.tacl2023.pdf)
- [44] [AI Agent Failure Pattern Recognition](https://www.mindstudio.ai/blog/ai-agent-failure-pattern-recognition)
- [45] [How To Understand And Reduce AI Inference Cost](https://www.cloudzero.com/blog/inference-cost)
- [46] [AI inference costs in production: A practical guide](https://www.mirantis.com/blog/inference-costs)
- [47] [Qwen2-Instruct Thinks When Token Costs Are High](https://kaitchup.substack.com/p/qwen3-instruct-thinks-when-token)
- [48] [What is Inference-Time Compute? The AI Pivot Explained](https://www.mindstudio.ai/blog/what-is-inference-time-compute-ai-pivot-explained)
- [49] [A Multi-Robot Exploration Framework for Autonomous Surface Mobility in Planetary-Like Environments](https://www.federico.io/pdf/Nayak.Lim.ea.AURO25.pdf)
- [50] [Orchestrating Multi-Agent Systems with LangGraph and MCP](https://healthark.ai/orchestrating-multi-agent-systems-with-lang-graph-mcp)
- [51] [Intro to OpenAI's o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)