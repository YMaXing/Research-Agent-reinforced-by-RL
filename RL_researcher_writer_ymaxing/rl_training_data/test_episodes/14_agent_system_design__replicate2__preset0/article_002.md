# A 7-Step Framework for Designing Production-Ready AI Agents

In the last two lessons, we defined the scope for our course's capstone project: two production-oriented agents that collaborate to produce publish-ready technical articles. We have Nova, the research agent, and Brown, the writing workflow. In Lesson 12, we established the high-level design, splitting the exploratory research from the deterministic writing process. In Lesson 13, we chose our frameworks: Nova will be built using FastMCP for portable, steerable tools, while Brown will run on a durable, auditable LangGraph workflow.

Now, we move from framework selection to system design. This is the layer that determines whether our agents behave like polished products or fragile demos that collapse under real workloads. Core design variables, such as reasoning budgets, context strategies, and human-in-the-loop (HITL) placement, are critical. Each exerts an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has different needs than a high-accuracy overnight research job.

This lesson provides a reusable 7-step decision playbook for moving from a business problem to a concrete agent architecture. We will apply this framework to our capstone, yielding the global Nova-versus-Brown architecture and a decision matrix you can reuse. By the end, you will be able to decide where extra thinking tokens deliver value, when to parallelize, when human gates are non-negotiable, and how to keep context lean without sacrificing quality. With the stakes clear, we will now walk through the general framework before specializing it for our capstone.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define what success looks like. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limits. These targets dictate every downstream choice. For example, a real-time customer support bot must have sub-second latency, and moderate accuracy might be acceptable if a human can intervene. In contrast, a batch research job for a financial report might have a throughput measured in hours, but it requires a near-zero tolerance for hallucinations.

Quantifying the cost of failure is essential. A small error in a customer-facing chatbot is an inconvenience; a hallucination in a medical diagnostic agent is a critical failure. This risk assessment directly informs how much you should invest in reliability measures like HITL and more powerful models. Your budget is not just a number; it is a direct reflection of your risk tolerance. A higher budget for a high-stakes task allows for more inference-time scaling, such as using more powerful models or parallel runs, to increase accuracy and reliability.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like Google, OpenAI, or Anthropic deliver state-of-the-art performance with low operational overhead. This path is ideal when you need access to the most powerful models without managing infrastructure. However, it can lead to vendor lock-in and less control over model updates. Unannounced changes to a proprietary model can degrade your system's performance without warning, a risk that must be managed with continuous evaluation.

Open-weight models like Llama, Mistral, or DeepSeek guarantee privacy, deep customization, and data locality when self-hosted. This is the right choice when security is paramount or when you need to fine-tune a model for a specialized domain. The trade-off is the significant burden of managing your own GPU infrastructure, which is both complex and expensive. While self-hosting simplifies compliance with regulations like GDPR, it places the entire burden of securing that infrastructure on your team. Top API providers often offer private cloud endpoints and contractual agreements that can meet stringent regulatory standards, making the choice more nuanced than a simple open-versus-closed binary [[3]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/).

### Define Your Context Strategy

As we saw in previous lessons, a large context window is not a silver bullet. A common mistake is to dump all available information into a prompt, assuming the LLM can sort it out. This often leads to the "lost-in-the-middle" performance cliff, where models exhibit a U-shaped performance curve. They recall information best from the beginning (primacy bias) and end (recency bias) of the context, while information in the middle is often overlooked [[1]](https://arxiv.org/abs/2307.03172). Instead of this naive full-document dump, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability.

For instance, in a conversational agent, a sliding window or a summarization strategy can be effective for remembering the latest information in a dialogue. For knowledge-intensive tasks, Retrieval-Augmented Generation (RAG) is a better approach to identify and retrieve only the most relevant document chunks. Building a high-quality retrieval system is a significant engineering challenge in itself, requiring careful tuning of chunking strategies, embedding models, and search algorithms. The goal is always to provide the model with the most relevant information in the most concise format possible.

### Pick an Orchestration Style

The choice between a predictable workflow and a dynamic agent depends on the nature of your task. As we covered in Lesson 2, you should use structured workflows for processes that are linear and require auditable steps, like supply chain management or financial trading. Dynamic agents are better suited for open-ended problems that demand flexible tool use, such as an autonomous web search agent.

Often, the best solution is a hybrid design that combines both. For example, you might use an agent to explore a problem and decide on a plan, then trigger a deterministic workflow to execute that plan reliably. This gives you the adaptability of an agent with the reliability and observability of a workflow. Our capstone project is a perfect example of this hybrid approach, using an agent for research and a workflow for writing.

### Establish a HITL & Evaluation Loop

Deciding between full autonomy and human oversight comes down to the cost of an error. For high-stakes or regulated domains, defining clear triggers for human intervention is non-negotiable. These triggers could be based on low-confidence scores from the model, requests to perform sensitive actions like sending an email, or flags for policy violations. In frameworks like LangGraph, these are implemented as "interrupts," which programmatically pause the workflow and wait for human input before proceeding [[5]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). For our capstone, we will require human sign-off on the final article before publication. In contrast, a simple data-tagging agent might run fully autonomously, as the cost of a mistake is low.

### Set Tool Boundaries & Portability

A robust agent system keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic logic to code. An LLM should not be calculating a mortgage payment; it should recognize the user's intent and call a well-defined function that does the math. This separation of concerns improves reliability and reduces costs.

Furthermore, standardizing how tools are exposed, for example, by using Model Context Protocol (MCP), ensures they are portable [[6]](https://modelcontextprotocol.io/docs/getting-started/intro). MCP acts like a USB-C port for AI, defining a standard way for agents to connect to external tools and data sources. This solves the "N×M integration problem" by allowing you to implement a tool server once and have it be accessible to multiple clients, such as a web interface or an IDE, without being locked into a single vendor's ecosystem. We will see this in action with our Nova agent.

### Choose Durability & Observability

Finally, your system's architecture must match its operational requirements. Long-running, stateful jobs, like our article-writing workflow, demand resumability, checkpoints, and full tracing to recover from failures. A stateless agent that can simply retry a task on failure does not need this complexity. For our Brown agent, we will use LangGraph, which provides these features out of the box through its persistence layer. This allows the workflow to save its state at every step using a checkpointer, so it can be resumed from where it left off using a consistent `thread_id` after an interruption or failure. Linking these choices back to the success criteria from Step 1 ensures your design meets its reliability targets.

This framework is iterative. You will likely revisit earlier steps as you move through implementation and uncover new constraints. Now that we have the high-level decision points, let's quantify how each choice impacts cost and latency.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding how to manage cost and latency is central to effective system design. Four independent levers can be adjusted at runtime to trade compute for capability. Critically, their effects multiply, so managing them deliberately is essential.

**Model Size Scaling** is the most straightforward lever. Larger, more capable models, like GPT-4.5, have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash-Lite. The input token cost for GPT-4.5 is 750 times higher than for Gemini 2.5 Flash-Lite [[7]](https://openai.com/api/pricing/). For simple tasks like data extraction or classification, a small, fast model is sufficient and cost-effective. For complex reasoning or tasks where accuracy is paramount, a larger, more expensive model is often necessary, and the higher cost is justified by the improved performance and time saved by human experts.

**Series Scaling** refers to increasing the internal computational steps a model takes before answering. This is often exposed as "thinking tokens," which allow the model to perform a longer chain of thought. For example, Anthropic's Claude models offer an "extended thinking" mode where you can allocate a specific `budget_tokens` for internal reasoning, allowing the model to analyze a problem more thoroughly before responding [[4]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This is a powerful tool for complex planning or validation steps, but it should be treated as a dial. You can activate it only for specific tasks and set a strict cap to bound both spend and latency. Interestingly, research on o1-like models has shown that longer chains of thought do not always lead to better accuracy. In some cases, correct solutions are shorter than incorrect ones, often because the model's limited ability to self-correct during the reasoning process leads it down the wrong path [[2]](https://arxiv.org/html/2502.12215v1).

**Parallel Scaling** involves running the same prompt multiple times and selecting the best response, often through a majority vote. This technique, known as self-consistency, can significantly improve reliability by reducing the impact of random errors. Research has shown that for a given budget, parallel scaling can sometimes outperform additional serial reasoning [[2]](https://arxiv.org/html/2502.12215v1). However, the improvement comes at a linear cost multiplier, as you are paying for each parallel run. A more advanced version of this is "Shortest Majority Vote," which prioritizes answer clusters that are not only more frequent but also have shorter average solution lengths, leveraging the insight that shorter answers are often more accurate [[2]](https://arxiv.org/html/2502.12215v1).

**Input Context Scaling** is the final lever. While more information can lead to better answers, every additional token carries a direct cost and adds to latency. As we have discussed, the "lost-in-the-middle" problem means that simply increasing the context size can actually degrade performance. The key is to find the optimal balance. Techniques like RAG, summarization, and selective retrieval are all designed to keep the effective context small while preserving the necessary information. Context caching can be a powerful optimization, allowing you to reuse the processed results of boilerplate prompts across multiple calls, which is particularly useful in multi-turn conversations or tool-use loops [[4]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking).![The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)

Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies. (Source: Agentic AI Engineering course)

To see how these levers multiply, let's contrast two designs for a research task.

A naive design might use the largest reasoning model, dump an entire 100-page document into the context, and run five parallel instances to ensure accuracy.

*   **Model:** GPT-4.5 (Input: $75/M tokens, Output: $150/M tokens)
*   **Input Tokens:** 200,000 (from a 100-page document)
*   **Output Tokens:** 5,000 (a detailed summary)
*   **Number of Parallel Runs:** 5
*   **Calculation:** (200k * $75/M + 5k * $150/M) * 5 = ($15 + $0.75) * 5 = **$78.75**

A budgeted design, on the other hand, might use a smaller model, retrieve only the most relevant chunks with RAG, and run a single pass.

*   **Model:** Gemini 2.5 Pro (Input: $1.25/M tokens, Output: $10.00/M tokens)
*   **Input Tokens:** 10,000 (from RAG retrieval)
*   **Output Tokens:** 2,000 (a focused summary)
*   **Number of Parallel Runs:** 1
*   **Calculation:** (10k * $1.25/M + 2k * $10.00/M) * 1 = ($0.0125 + $0.02) * 1 = **$0.0325**

The budgeted design achieves a similar outcome at a roughly 2400x cost reduction. This is the power of deliberate system design. Additional optimizations, like prompt caching for repeated calls and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a more detailed architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.![Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)

Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces. (Source: Agentic AI Engineering course)

The image above illustrates the core architectural principle of our capstone: a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation is crucial for building a production-ready system. It prevents context bloat, as each component only deals with the information relevant to its task. It also makes the system easier to debug and evolve independently; a change to the research process does not require a change to the writing workflow. Let's examine each component in more detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple **MCP client** runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process similar to how a human researcher would work. It might start by deconstructing the main topic into sub-questions, then use a search tool like Perplexity for each sub-question, synthesize the initial findings, and identify areas that need deeper investigation. Finally, it selects the top sources for a full scrape and compiles everything into a `research.md` file.

The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt. This ReAct-style loop allows the agent to dynamically plan its next action based on the results of the previous one, making it well-suited for the unpredictable nature of research.

For the MCP client, we use **FastMCP’s built-in** `**Client**` **class,** a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details out of the box. Our implementation is just around 200 lines of Python that wrap this client. It connects to the server, fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation. This lean implementation demonstrates the power of using a standardized protocol like MCP.![End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)

Image 3: End-to-end agent flow for the Nova Research Agent (Source: Agentic AI Engineering course)

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a **FastMCP server**, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call. This design gives us the best of both worlds: the durability of a stateful workflow and the portability of a standardized tool protocol.

The exposed tools are:

-   **Generate Article:** This orchestrates a full writing workflow. It loads context (guidelines, research, profiles, examples), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern. In this pattern, one LLM call acts as a critic (`evaluator`), providing feedback on the draft, while another call acts as the writer (`optimizer`), revising the draft based on that feedback. LangGraph's state management is perfect for this, as the state object can hold the draft, reviews, and version history across multiple cycles.
-   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews. This allows for targeted revisions without re-running the entire generation process.
-   **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining context awareness of the full document. This is useful for making small, precise changes to the text.![Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)

Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow. (Source: Agentic AI Engineering course)

The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` directory containing scraped sources and logs. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. This clean separation ensures the system is modular and debuggable. If the research phase fails, we can inspect the artifacts and re-run it without affecting the writing workflow.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any personal notes. As the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill leads to hollow text. LLMs are highly effective at translation and synthesis, but they are terrible at generating original ideas from scratch. A good guideline provides the scaffolding of original thought that the model needs to produce coherent and insightful content.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of the 7-step framework into specific, implementable defaults for our research (Nova) and writing (Brown) agents. This is not aspirational; it is the exact blueprint we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, the chosen default, and a rationale that links back to our cost, latency, reliability, or debuggability goals. This matrix will be our guide in Lessons 15-22, ensuring every trade-off is a conscious one.

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project, producing the clean Nova-versus-Brown global architecture. We detailed the supporting diagrams and the concrete decision matrix that will guide our implementation. This system-level view—rather than a narrow focus on prompts or single models—is the foundation that turns prototypes into scalable, production-ready agent products that remain debuggable and cost-effective. By making deliberate choices about model tiers, reasoning budgets, context strategies, and orchestration, we can build systems that are not only powerful but also efficient and reliable.

The decisions and diagrams recorded in this lesson will be referenced repeatedly in all future implementation lessons. They are the blueprint that ensures every code-level choice stays aligned with our original cost, latency, and quality goals. In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining our core research tools and orchestrating the multi-round research process. Later, in Lessons 19–22, we will implement the Brown writing workflow, bringing our full two-agent system to life.

This disciplined approach moves AI engineering from ad-hoc experimentation to a structured, professional practice. The real skill you are developing is the ability to make these system-level trade-offs repeatedly across projects, turning AI engineering from an art into a repeatable engineering practice.

## References

- [1] [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
- [2] [Revisiting the Test-Time Scaling of o1-like Models](https://arxiv.org/html/2502.12215v1)
- [3] [LLM System Design & Model Selection](https://www.oreilly.com/radar/llm-system-design-and-model-selection/)
- [4] [Extended thinking & interleaved thinking docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- [5] [Human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/)
- [6] [What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [7] [API Pricing](https://openai.com/api/pricing/)
- [8] [Deep Research in Gemini](https://gemini.google/overview/deep-research/)
- [9] [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [10] [Introducing o3 and o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/)