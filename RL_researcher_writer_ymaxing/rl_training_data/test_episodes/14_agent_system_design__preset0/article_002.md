# From Prototype to Production: A Decision Framework for AI Agent System Design

In the last two lessons, we scoped our capstone project—two agents that collaborate on technical articles—and selected our frameworks: FastMCP for our research agent, Nova, and LangGraph for our writing workflow, Brown.

With our tools selected, we now move to system design. This layer determines whether our agents become dependable products or brittle research demos that collapse under real workloads. Core design variables like the reasoning budget, context strategy, and human-in-the-loop (HITL) placement each exert an order-of-magnitude influence on cost, latency, and reliability. For example, a real-time support bot requires sub-second latency and can tolerate moderate accuracy, while an overnight research job demands near-zero hallucinations, even if it takes hours.

This lesson introduces a reusable 7-step decision playbook that moves systematically from business requirements to a concrete agent architecture. We will then apply this framework to our capstone, producing the global design for Nova and Brown, complete with component diagrams and a decision matrix you can reuse. You will learn where to spend extra thinking tokens, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing signal. With the stakes clear, let's walk through the general framework.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This step-by-step playbook helps you move from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice. For instance, a real-time support bot might need sub-second latency where moderate accuracy is acceptable. In contrast, a high-accuracy batch research job measures throughput in hours and has a near-zero tolerance for hallucinations. Constraints like GDPR might force a self-hosted open-weight model choice to ensure data remains within a specific jurisdiction. Security requirements, such as enforcing Transport Layer Security (TLS), rate limiting, and maintaining audit logs, are also critical design inputs that shape the architecture from the start [[3]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic offer state-of-the-art performance with low operational overhead but can lead to vendor lock-in. Open-weight models such as Llama or Mistral guarantee privacy, deep customization, and data locality when self-hosted. However, this path requires you to manage the GPU infrastructure, which is a significant burden. The choice depends on your constraints. For a high-stakes legal analysis, the cost of GPT-4.5 at $75 per million input tokens might be justified, whereas for a high-volume email classification task, a model like Gemini 2.5 Flash Lite at $0.10 per million tokens is a more economical fit [[5]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/), [[10]](https://openai.com/api/pricing/).

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not always the solution. It is a common mistake to dump everything into a prompt and assume the LLM can handle it. This often leads to the "lost-in-the-middle" performance cliff, where models exhibit a U-shaped performance curve, struggling to use information buried in the middle of long contexts [[1]](https://arxiv.org/abs/2307.03172). Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For example, in a chatbot application, a sliding window or summarization strategy can help the model remember the most recent parts of a conversation. For a question-answering system, Retrieval-Augmented Generation (RAG) is more effective. A support bot using RAG can retrieve the three most relevant paragraphs from a 1,000-page manual, keeping the context under 1,000 tokens instead of the full document.

### Pick an Orchestration Style

The choice of orchestration depends on the task's predictability. As we discussed in Lesson 2, you should use predictable workflows for linear, auditable processes, like claims processing, where each step is well-defined. For open-ended tasks that require dynamic tool use, such as a market research agent exploring new topics, agents are a better fit [[11]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows). Often, a hybrid design that combines both is the most effective solution. For example, an agent might handle initial data exploration, while a workflow executes a fixed reporting process based on the agent's findings.

### Establish a HITL & Evaluation Loop

You must decide where to insert human-in-the-loop triggers based on error cost and business risk. Instead of aiming for full autonomy, define clear triggers for human intervention. These can be based on low-confidence scores from the model, the execution of sensitive actions like sending an email, or flags for policy violations. Frameworks like LangGraph provide an `interrupt()` function that can pause a workflow before a critical action, such as a database write, and wait for explicit human approval before proceeding. For a research agent, a HITL gate could be triggered for any query above a certain ambiguity threshold. For our writing agent, a final human sign-off on the article is non-negotiable.

### Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for intent detection and high-level orchestration, while delegating deterministic tasks like math or data validation to traditional code. This separation of concerns improves reliability. Furthermore, standardizing tool interactions using a protocol like the Model Context Protocol (MCP) ensures your tools are portable. An agent can discover and use a `send_email` tool exposed via an MCP server without needing to know if the backend is SendGrid or AWS SES. This allows you to reuse tools across different clients, such as IDEs or chat interfaces, without being tied to a single vendor's ecosystem [[2]](https://modelcontextprotocol.io/docs/getting-started/intro), [[3]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, checkpoints, and full tracing to recover from failures. For a multi-hour writing task like our Brown agent, a checkpointer ensures that if the process fails after two hours, it can resume from the last completed step, not from scratch [[4]](https://docs.langchain.com/oss/python/langgraph/persistence). For simple, stateless tasks, a basic retry policy may suffice. These choices should link back to the success criteria defined in the first step. A high-stakes financial analysis workflow needs detailed tracing for audits, while a simple summarization task does not.

This framework is iterative. You will likely revisit earlier steps as you uncover new constraints during implementation. Once the high-level decisions are framed, you must quantify how each inference-time lever multiplies cost and latency so you can budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Four independent levers can be adjusted at runtime to trade cost and latency for performance: model size, series scaling, parallel scaling, and input-context scaling. Understanding how these levers interact and multiply is central to effective system design.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down> 
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash Lite [[5]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/). The cost difference can be extreme, with GPT-4.5's input price of $75/M tokens being 750 times higher than Gemini 2.5 Flash Lite's $0.10/M tokens [[10]](https://openai.com/api/pricing/). For high-value tasks where mistakes are expensive, a frontier model is justified. For high-volume, low-stakes tasks, a cheaper model is more appropriate.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens.” For example, Claude's "extended thinking" feature allows you to set a `budget_tokens` parameter, giving the model more time to reason before responding [[6]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking), [[7]](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html). However, this is a lever to use with caution. Research on o1-like models has shown that longer chains of thought do not always improve accuracy and can even degrade performance due to failed self-revision [[9]](https://arxiv.org/html/2502.12215v1). You should treat extra reasoning as a dial activated only for the most complex steps and cap it to bound spending and latency.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response, often through a majority vote. This technique, known as self-consistency, is effective because a model is less likely to make the same reasoning error multiple times across independent runs [[8]](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling). The reliability gains come at a linear cost multiplier. For a fixed budget, research shows that parallel scaling can sometimes outperform additional serial reasoning, especially when a model's self-correction ability is weak [[9]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

While relevant information is valuable, each additional token carries a direct cost and adds to latency. As discussed, the "lost-in-the-middle" problem means that simply providing more context can hurt performance. Studies have shown that accuracy can drop by over 20% when relevant information is moved from the beginning or end of a prompt to the middle [[1]](https://arxiv.org/abs/2307.03172). This makes active context management through techniques like RAG, summarization, and caching a critical optimization, not just a cost-saving measure.

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

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple MCP client runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe is a master prompt that outlines a sequence: initial query transformation, parallel search across multiple sources, initial scrape and summary of top results, an LLM-driven decision on which sources are most promising, a full scrape of selected sources, and final synthesis into `research.md`. This iterative approach, inspired by systems like Perplexity Deep Research, allows the agent to refine its plan as it gathers more information, ensuring a more thorough and relevant output than a single search could provide [[11]](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research).

For the MCP client, we use FastMCP’s built-in `Client` class. This is a lightweight, ready-to-use client that handles all protocol details like capability discovery and tool calling. Our implementation is a ~200 line Python wrapper around this class. It connects to the server, fetches the research prompt, and runs a simple ReAct-style loop where the LLM decides which tool to call next. This design keeps the agent's logic focused purely on orchestration, while the MCP framework handles the complexities of tool interaction.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down>
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:
*   **Generate Article:** This orchestrates a complex workflow. It begins by loading all necessary context, including guidelines, research from Nova, and author profiles. It then uses an orchestrator-worker pattern to generate media items like tables and diagrams in parallel. Next, it writes the first draft and enters a configurable number of review-edit cycles. Each cycle uses an evaluator-optimizer pattern, where one LLM call critiques the draft and another rewrites it based on the feedback.
*   **Edit Article:** This tool runs a single review-edit cycle on the entire article, but it prioritizes human feedback provided in the tool call over automated reviews. This allows for direct, targeted revisions while still leveraging the power of the evaluator-optimizer pattern.
*   **Edit Selected Text:** This provides a more granular level of control, running a single review-edit cycle on a specific portion of the article. It enables targeted revisions while maintaining awareness of the full document context, ensuring that local edits remain consistent with the overall narrative. This reusability of the core LangGraph state machine for different editing scopes highlights the modularity of the design.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down>
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

### Handoff and Human Input

The handoff between Nova and Brown is file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This file-based contract is a robust software engineering pattern that decouples the two systems. It allows us to test Nova and Brown in complete isolation. We can run Nova to generate research artifacts, manually inspect or edit them, and then feed them to Brown. This modularity is essential for debugging and iterative development.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill leads to hollow text. LLMs are amazing at translation and synthesis, but they are terrible at generating original ideas.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the framework's principles into specific defaults for our research (Nova) and writing (Brown) agents. It serves as a bridge from our high-level architectural principles to concrete implementation choices. It's a living document that enforces consistency and prevents "design drift" during the coding phase. This is not an aspirational guide but the exact blueprint we will implement. We will refer to this matrix repeatedly in Lessons 15–22 to ensure every trade-off aligns with our project goals.

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, the three supporting diagrams, and the concrete decision matrix that will guide our implementation. We've established a repeatable process for designing agentic systems, moving from business value to observability. We've quantified the four levers of inference-time scaling—model size, series, parallel, and context—and seen how they create thousand-fold cost variations. Adopting this system-level view is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective.

The decisions and diagrams we have recorded here will be referenced repeatedly in all future implementation lessons, ensuring that every code-level choice stays aligned with our original cost, latency, and quality goals. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining the core research tools and orchestrating the research process. Following that, we will turn to the Brown workflow implementation in Lessons 19–22. The real skill you are developing is the ability to make these system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable engineering practice.

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [3] [What is the Model Context Protocol (MCP)?](https://www.databricks.com/blog/what-is-model-context-protocol)
- [4] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [5] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [6] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [7] [Use Claude Messages with extended thinking](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html)
- [8] [Categories of Inference-Time Scaling for Improved LLM Reasoning](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling)
- [9] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [10] [API Pricing](https://openai.com/api/pricing/)
- [11] [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)