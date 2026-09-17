# Lesson 14: A Decision Framework for Designing Agentic Systems

In the last two lessons, we established the foundation for our capstone project. In Lesson 12, we defined its scope: two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. We designed Nova as an explorative research agent and Brown as a deterministic writing workflow. Then, in Lesson 13, we compared agent frameworks and selected our tools: Nova will ship as a set of portable FastMCP tools, while Brown will run a durable and auditable LangGraph workflow.

With our frameworks chosen, we now move to **system design**. This is the layer that determines whether our agents behave like polished, dependable products or fragile research demos that collapse under real workloads.

Core design variables, such as reasoning budgets, context strategies, and human-in-the-loop (HITL) policies, exert an order-of-magnitude influence on cost, latency, and reliability. This lesson introduces a reusable 7-step decision playbook that moves from business value to a concrete design. We will apply this framework to our capstone, producing the global architecture for Nova and Brown and a detailed decision matrix you can reuse. By the end, you will know where extra thinking tokens deliver value, when to parallelize, and how to keep context lean without sacrificing quality.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. While LLMs have made these systems more accessible, the core concepts predate them by decades. Classical AI defined an agent as an entity that perceives its environment and acts to achieve goals, using architectures that balanced fast, reactive control with slower, deliberative planning [[8]](https://arxiv.org/html/2602.10479v1).

This playbook adapts those foundational ideas for modern, LLM-driven systems. It guides you from a problem statement to a design that balances capability, cost, and reliability.

### 1. Define Value, Constraints, Cost & Latency

First, you must explicitly define your success criteria. This includes the required output quality, any privacy or compliance requirements, expected usage volume, and your per-task spending limits. These targets dictate every downstream choice. A decision matrix is a useful tool for this, allowing you to list all relevant criteria, assign weights based on their relative importance, and score different options to clarify trade-offs. This structured process augments engineering judgment and ensures all factors are considered appropriately [[13]](https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45).

For example, a real-time customer support bot must have sub-second latency to feel responsive. Here, speed is more important than perfect accuracy, so a smaller, faster model is appropriate. In contrast, a batch research job that runs overnight to generate a financial analysis report has a near-zero tolerance for hallucinations. For this task, latency is secondary to accuracy, justifying the use of a larger, more expensive reasoning model.

### 2. Choose Model Family & Capability Mix

Next, decide between closed APIs and open-weight models. Closed APIs from providers like OpenAI, Google, or Anthropic offer state-of-the-art performance with low operational overhead. This path is ideal when your priority is accessing the best models with maximum simplicity. However, it can lead to vendor lock-in, where your system becomes dependent on a single provider's platform and pricing.

Open-weight models like Llama or Mistral guarantee privacy, deep customization, and data locality when self-hosted. This is the right choice when you need to fine-tune a model on proprietary data or ensure sensitive information never leaves your infrastructure. The trade-off is the significant burden of managing your own GPU infrastructure, which includes handling everything from hardware provisioning to model deployment and scaling [[14]](https://www.mirantis.com/blog/llm-optimization-techniques).

### 3. Define Your Context Strategy

As we saw in previous lessons, a large context window is not a cure-all. It is a common mistake to dump everything into a prompt and assume the LLM can handle it. This often leads to the "lost-in-the-middle" performance cliff, where models struggle to use information buried in the middle of long contexts [[1]](https://arxiv.org/abs/2307.03172). Performance can degrade significantly when critical information is not at the beginning or end of the context window. This positional bias means that even if the correct information is present, the model may ignore it.

Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For instance, a sliding window or summarization approach is suitable for tasks that need to remember the latest information in a long conversation. In contrast, RAG is better for identifying and retrieving the most relevant facts from a large knowledge base, ensuring the model gets only the necessary information.

### 4. Pick an Orchestration Style

Your choice of orchestration depends on the task's predictability. As we discussed in Lesson 2, the decision between workflows and agents is a trade-off between control and autonomy. Use well-defined workflows for processes that are linear and need to be auditable, such as claims processing or generating a standardized report. Here, the steps are known, and reliability is paramount [[15]](https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows).

For open-ended problems that require dynamic tool use, autonomous agents are more appropriate. Examples include complex debugging or open-ended research where the path to a solution is not known in advance. Hybrid designs, which combine both, are often the most practical solution for complex systems that contain both predictable and unpredictable components [[16]](https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both).

### 5. Establish a HITL & Evaluation Loop

Decide on the level of human oversight. This involves defining clear triggers for human intervention, such as when the model's confidence is low, when it attempts a sensitive action, or when it encounters a policy flag. The decision to implement HITL should be tied to the cost of an error and the overall business risk. For example, you might require human approval for any financial transaction above a certain threshold or for the final sign-off on a generated legal document.

This is especially important because agentic systems have unique failure modes. Unlike traditional software that often fails with clear error codes, agents can fail silently. They might complete a workflow and produce an output that appears correct, only for an error to be revealed much later by its downstream consequences [[9]](https://latitude.so/blog/ai-agent-failure-detection-guide).

Common issues include **goal drift**, where the agent gradually strays from its original objective, and **context loss**, where it forgets earlier instructions. In systems with multiple agents, a mistake from one can propagate as trusted but flawed input to others, a problem known as **hallucination propagation** that is difficult to debug without a strong evaluation loop [[10]](https://www.augmentcode.com/guides/multi-agent-ai-systems).

### 6. Set Tool Boundaries & Portability

Define a clear separation of concerns. The LLM should be responsible for intent detection and high-level planning, while deterministic tasks like complex math, data validation, or heavy processing should be delegated to code. For example, instead of asking an LLM to calculate an average, have it call a Python function. This separation is a fundamental reliability pattern. Tool misuse is the most common and insidious failure mode for agents in production. This includes calling the wrong tool or providing malformed arguments, where a single error can silently corrupt every subsequent step [[9]](https://latitude.so/blog/ai-agent-failure-detection-guide).

Using a standardized protocol like Model Context Protocol (MCP) enforces this separation. MCP provides a "USB-C port" for AI, standardizing how agents connect to external tools and data sources. This ensures your tools are portable across different clients and IDEs, preventing vendor lock-in and making your system more modular and maintainable [[2]](https://modelcontextprotocol.io/docs/getting-started/intro).

### 7. Choose Durability & Observability

Finally, match your system's resilience to its requirements. Long-running, stateful jobs demand features like resumability, checkpoints, and detailed tracing to survive failures [[3]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). For simple, stateless loops, a basic retry policy may suffice. This choice should link back to the success criteria you defined in the first step.

Traditional DevOps and observability tools, designed for stateless requests, are often insufficient for agentic workflows [[11]](https://orq.ai/blog/ai-agent-frameworks). They can log individual errors but miss the causal chain connecting a tool failure at step 2 to a bad output at step 9. Agent-native observability requires capturing every action as a structured trace, allowing you to debug the entire execution flow, not just isolated events [[9]](https://latitude.so/blog/ai-agent-failure-detection-guide).

This framework is iterative. You will likely revisit earlier steps as you uncover new constraints during implementation. Once the high-level decisions are framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding the four independent levers that control runtime performance is central to effective system design. Model size, series scaling, parallel scaling, and input context scaling interact in multiplicative ways. Mastering them allows you to adjust cost and latency on a per-step basis within a workflow. These four levers are not unique to text-based agents; they are fundamental to scaling intelligence in any domain. In embodied AI and robotics, for example, the same scaling laws apply, with performance improving with model size, data, and compute. However, the physical world introduces harder constraints: inference latency directly impacts a robot’s ability to react in real-time, and larger models consume more power, which is a critical limitation for battery-operated devices [[12]](https://arxiv.org/html/2405.14005v1).

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash-Lite [[4]](https://www.oreilly.com/radar/llm-system-design-and-model-selection/). The key is to use the right model for the right job. For simple tasks like data extraction or classification, a small model is often sufficient and more cost-effective. For complex reasoning or creative generation, a larger model may be necessary to achieve the desired quality. For instance, a high-stakes financial analysis might justify the cost of a frontier model, whereas a simple content tagging task would be better served by a cheaper, faster alternative.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, often enabled via "thinking tokens" [[5]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This is a powerful tool for complex reasoning, as it allows the model to perform a longer chain of thought before producing an answer. However, it adds significant cost and latency. It is also not a guaranteed improvement; some research shows that for models with weak self-revision capabilities, longer reasoning chains can actually degrade performance [[6]](https://arxiv.org/html/2502.12215v1). Treat extra reasoning as a dial you turn up only for the most difficult planning or validation steps, and always cap it to bound your spending. For example, you might allocate a budget of 8,000 thinking tokens for an initial planning phase but disable it for subsequent, more routine steps.

### Parallel Scaling

This involves running the same prompt multiple times and selecting the best response. This is often done through a majority vote. This technique is also known as self-consistency. While this improves reliability by reducing the impact of a single bad generation, it comes at a linear cost multiplier. For a given budget, parallel scaling can sometimes outperform additional serial reasoning, especially when a model's ability to self-correct is limited. The trade-off is between spending compute on one long thought process versus several shorter, independent ones [[6]](https://arxiv.org/html/2502.12215v1).

### Input Context Scaling

Every token you add to the input context carries a direct cost and an indirect latency penalty. While relevant information is valuable, the goal is to find the optimal balance. As discussed, models can suffer from the "lost-in-the-middle" problem, where they fail to use information buried in a long context [[1]](https://arxiv.org/abs/2307.03172). Techniques like RAG, summarization, caching, and selective retrieval are essential for keeping the effective context small while preserving the signal, ensuring the model gets the information it needs without being overwhelmed.![The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)

Let's illustrate this with a quick cost calculation. Compare a naive design to a budgeted one for a research task.

A **naive design** might look like this:
*   **Model:** GPT-4.5 (expensive reasoning model)
*   **Input Tokens:** 32,000 (a large chunk of a document)
*   **Output Tokens:** 4,000
*   **Number of Parallel Runs:** 5
*   **Calculation:** (32k input * $75/M + 4k output * $150/M) * 5 runs = **$15.00 per task**

A **budgeted design** for the same task:
*   **Model:** GPT-4o Mini (fast, cheap model)
*   **Input Tokens:** 4,000 (RAG + summary)
*   **Output Tokens:** 4,000
*   **Number of Parallel Runs:** 1
*   **Calculation:** (4k input * $0.15/M + 4k output * $0.60/M) * 1 run = **$0.003 per task**

This simple adjustment yields a cost reduction of 5,000x while potentially meeting the same quality target. Other optimizations, like prompt caching and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.![Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)

As illustrated in Image 2, the core principle of our capstone architecture is a clean separation of concerns. Unpredictable, open-ended research is handled by Nova, an MCP agent. Predictable, iterative drafting and review are managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently. Let's examine each component in greater detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around MCP to ensure its tools are portable and reusable. A simple **MCP client** then runs an LLM-driven loop that follows a "Research Recipe" based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process.

The process includes querying sources, scraping and transcribing them, running iterative research loops with Perplexity, filtering the results, selecting top sources for a full scrape, and finally compiling everything into a `research.md` file. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt.

For the MCP client, we use **FastMCP’s built-in `Client` class,** a lightweight, ready-to-use MCP client that connects to our server and handles all protocol details out of the box. This includes capability discovery, tool calling, and resource fetching. Our implementation is just ~200 lines of Python that wrap this client. It connects to the server via in-memory or stdio transport, fetches the research prompt, and runs a simple ReAct-style loop where the LLM decides which tool to call next. It then executes that tool via `client.call_tool()` and feeds the result back into the conversation.![End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)
Image 3: End-to-end agent flow for the Nova Research Agent (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine [[3]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). We front this engine with a **FastMCP server**, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:
-   **Generate Article:** This tool orchestrates a complete workflow. It loads context (guidelines, research, profiles, examples), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern. This modular approach allows for specialized agents to handle different parts of the process, improving efficiency and quality.
-   **Edit Article:** This tool runs a single review-edit cycle on the entire article based on human feedback. It uses the evaluator-optimizer pattern, but with human input prioritized over automated reviews, allowing for direct control over the final output.
-   **Edit Selected Text:** This tool runs a review-edit cycle on a specific portion of the article. This enables targeted revisions while maintaining awareness of the full document, ensuring that local changes are consistent with the overall context.![Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow. (Source https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)

The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This decoupled, file-based contract is a deliberate architectural choice to mitigate common multi-agent failure modes. A failure in Nova, the upstream agent, is contained within its output artifacts rather than being passed directly to Brown. This prevents **cascading errors**, where one agent's mistake becomes corrupt input for the next, and mitigates **hallucination propagation**, where a hallucinated fact could otherwise poison the entire downstream workflow [[9]](https://latitude.so/blog/ai-agent-failure-detection-guide), [[10]](https://www.augmentcode.com/guides/multi-agent-ai-systems). This clean separation of concerns makes the system modular, debuggable, and easier to maintain [[7]](https://fast.io/resources/ai-agent-artifacts).

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what they want to write, the narrative of the article, and any other important details. Since the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop.

If the ideas are not clearly enumerated and connected, the output will be sloppy. Leaving too many gaps for the AI to fill without instructions leads to hollow text. LLMs are proficient at translation, but terrible at generating original ideas.

The architecture and diagrams are now concrete. The final step is to translate these principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

This matrix translates the abstract principles of our 7-step framework into specific, implementable defaults for the research (Nova) and writing (Brown) agents. This is not an aspirational guide; it is the exact blueprint we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, our chosen default, and a rationale that links back to the cost, latency, and reliability goals of our capstone project.

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

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project. This process produced the clean Nova-versus-Brown global architecture, a concrete decision matrix that will guide our implementation, and three supporting diagrams. This system-level view, rather than a narrow focus on prompts or single models, is what turns prototypes into scalable, production-ready agent products. It is the foundation for building systems that are debuggable, cost-effective, and reliable at scale.

The decisions and diagrams we have established here are not just theoretical. They will be our guide in all future implementation lessons, ensuring that every code-level choice aligns with our original goals for cost, latency, and quality. This structured approach prevents the ad-hoc decisions that often lead to systems that are fragile and difficult to maintain.

In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova. We will define its core research tools and orchestrate the multi-round research and filtering process that produces the final `research.md` file. Later, in Lessons 19–22, we will implement the Brown writing workflow using LangGraph. The ability to make these system-level trade-offs is a core skill in AI engineering, and this is how you build AI systems with repeatable engineering discipline.

## References

- [1] N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, & P. Liang. (2023). Lost in the Middle: How Language Models Use Long Contexts. *arXiv*. https://arxiv.org/abs/2307.03172
- [2] What is the Model Context Protocol (MCP)?. (n.d.). *Model Context Protocol*. https://modelcontextprotocol.io/docs/getting-started/intro
- [3] Human-in-the-loop. (n.d.). *LangChain*. https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
- [4] L. Bouchard & L. Peters. (2025). LLM System Design & Model Selection. *O'Reilly*. https://www.oreilly.com/radar/llm-system-design-and-model-selection/
- [5] Extended thinking & interleaved thinking docs. (n.d.). *Claude*. https://docs.claude.com/en/docs/build-with-claude/extended-thinking
- [6] Revisiting the Test-Time Scaling of o1-like Models. (2025). *arXiv*. https://arxiv.org/html/2502.12215v1
- [7] How to Manage AI Agent Artifacts - Complete Guide 2025 | Fastio. (n.d.). *Fast.io*. https://fast.io/resources/ai-agent-artifacts
- [8] Agentic AI: A High-level Overview of the Terminology, Concepts, and its Current State. (2026). *arXiv*. https://arxiv.org/html/2602.10479v1
- [9] Detecting AI Agent Failure Modes in Production: A Framework for Observability-Driven Diagnosis. (2026). *Latitude*. https://latitude.so/blog/ai-agent-failure-detection-guide
- [10] Multi-Agent AI Systems: Architecture & Failure Modes. (n.d.). *Augment Code*. https://www.augmentcode.com/guides/multi-agent-ai-systems
- [11] AI Agent Frameworks: The Production-Ready Guide. (n.d.). *Orq.ai*. https://orq.ai/blog/ai-agent-frameworks
- [12] Scaling Laws for Embodied AI. (2024). *arXiv*. https://arxiv.org/html/2405.14005v1
- [13] The Decision Matrix Method for Engineering Trade-Offs. (n.d.). *DEV Community*. https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45
- [14] LLM Optimization: Techniques and Guide. (2026). *Mirantis*. https://www.mirantis.com/blog/llm-optimization-techniques
- [15] Agentic AI Explained: Workflows vs Agents. (n.d.). *Orkes*. https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows
- [16] Agents vs. Workflows: Why Not Both?. (n.d.). *Tellius*. https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both