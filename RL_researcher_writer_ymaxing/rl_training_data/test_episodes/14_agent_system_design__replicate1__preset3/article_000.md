# Lesson 14: The AI Engineering Decision Framework

In the last two lessons, we defined the scope for our capstone project—two production-oriented agents, Nova and Brown, that collaborate to produce publish-ready technical articles. We also justified our framework choices: Nova will be built using FastMCP for portability, while Brown will run on LangGraph for durability. Now, we move from framework selection to system design. This is the layer that determines whether our agents will behave like dependable products or fragile demos that collapse under real workloads.

Core design variables like reasoning budgets, context strategies, and human-in-the-loop (HITL) placement exert an order-of-magnitude influence on cost, latency, and reliability. A real-time support bot has vastly different design constraints than a high-accuracy overnight research agent. Getting these trade-offs right is what separates a successful AI product from a failed experiment.

This lesson introduces a reusable 7-step decision playbook that moves systematically from business goals to a concrete architectural blueprint. We will apply this framework to our capstone, producing the global architecture for Nova and Brown, complete with component diagrams and a decision matrix you can adapt for your own projects.

You will learn where to spend your budget on extra "thinking" tokens for genuine value, when to parallelize tasks, when human gates are non-negotiable, and how to keep your context lean without sacrificing quality. With the stakes clear, let's walk through the general framework before we specialize it for our capstone.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. This playbook will guide you from a problem statement to a design that balances capability, cost, and reliability.

### Define Value, Constraints, Cost & Latency

Before writing any code, you must explicitly define what success looks like. This includes the required output quality, any privacy or compliance constraints, the expected volume of tasks, and your per-task spending limit. These targets dictate every downstream choice. For example, a real-time customer support bot demands sub-second latency, where moderate accuracy might be acceptable. In contrast, a high-accuracy batch research job has a throughput measured in hours and a near-zero tolerance for hallucinations.

### Choose Model Family & Capability Mix

Your next decision is whether to use closed APIs or open-weight models. Closed APIs from providers like OpenAI, Google, and Anthropic deliver state-of-the-art performance with low operational overhead but can lead to vendor lock-in. Open-weight models offer unparalleled privacy, customization, and data locality, which is essential for sensitive applications. However, this path comes with the significant burden of managing your own GPU infrastructure. The choice depends on whether your priority is cutting-edge capability with simplicity or maximum control and security.

### Define Your Context Strategy

As we discussed in previous lessons, simply dumping all available information into a large context window is a common mistake. Research shows this leads to a "lost-in-the-middle" performance cliff, where models struggle to recall information buried in the middle of long prompts [[1]](https://arxiv.org/abs/2307.03172). This bias appears to stem from the model’s autoregressive nature and the information retrieval demands of its training data, which favor the beginning and end of a sequence [[8]](https://arxiv.org/html/2510.10276v1). Instead of relying on brute-force context, you should prioritize selective retrieval, compression, and structured summaries to manage costs and improve reliability. For instance, a sliding window summarization approach is effective for remembering the latest information in a long-running chat, while RAG is better suited for retrieving specific, relevant facts from a large knowledge base to answer a question.

### Pick an Orchestration Style

The choice between a predictable workflow and a dynamic agent depends on the nature of the task. As we covered in Lesson 2, you should use workflows for processes that are auditable and mostly linear. For open-ended problems that require dynamic tool use, an agent is more appropriate. Many production systems use a hybrid design, combining the reliability of workflows with the flexibility of agents. For many business processes, deterministic orchestration is preferable to dynamic, LLM-driven routing. While agentic replanning offers flexibility, predictable and auditable graphs provide superior cost control, observability, and reliability for structured tasks [[9]](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows). This approach still allows for complex logic through conditional routing and loops without sacrificing governance. For example, a workflow might handle the predictable steps of a customer onboarding process, while an agent is tasked with the open-ended problem of researching a new lead.

### Establish a HITL & Evaluation Loop

You must decide where to insert human oversight into your system. This decision should be tied directly to the cost of an error and the overall business risk. Instead of aiming for full autonomy from the start, define clear triggers for human intervention. These can include low-confidence scores from the model, requests to perform sensitive actions like sending an email, or flags indicating a policy violation. A financial trading agent might require human approval before executing a trade, whereas a content summarization tool might operate autonomously unless its confidence score drops below a certain threshold.

Production-grade HITL goes beyond simple confidence scores. Escalation should also be triggered by context-dependent factors, such as financial transactions exceeding a certain value, decisions affecting high-profile clients, or when multi-agent complexity increases cumulative uncertainty [[10]](https://galileo.ai/blog/human-in-the-loop-agent-oversight). To avoid brittle, hardcoded logic, these rules are best managed in a centralized policy engine. This separates policy from application code, making fleet-wide governance operationally manageable.

### Set Tool Boundaries & Portability

A robust design keeps the LLM responsible for high-level orchestration and intent detection while delegating deterministic tasks to code. The LLM decides *what* to do, and your code handles *how* to do it. For example, the LLM should not be asked to perform calculations; it should call a calculator tool. This separation of concerns improves reliability. Furthermore, protocols like the Model Context Protocol (MCP) enforce clean tool boundaries, ensuring your tools are portable and can be used by different agents or clients without being tied to a single vendor or framework [[2]](https://modelcontextprotocol.io/docs/getting-started/intro), [[3]](https://www.databricks.com/blog/what-is-model-context-protocol).

### Choose Durability & Observability

Finally, consider the operational requirements of your system. Long-running, stateful jobs demand resumability, checkpoints, and full tracing to recover from failures. A multi-hour research task, for instance, should be able to resume from the last completed step if it fails. LangGraph, with its built-in checkpointing, is well-suited for such tasks [[4]](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/). For stateless tasks that complete quickly, a simple retry policy may suffice.

One of the primary reasons long-running jobs fail is due to a "self-conditioning" effect. Research has shown that models become more likely to make a mistake after observing their own errors in the context history [[11]](https://arxiv.org/html/2509.09677v1). This creates a negative feedback loop where one error increases the probability of another, causing performance to degrade over long execution chains. This is distinct from simple long-context degradation and highlights the need for robust state management and error recovery. Your choice should align with the success criteria defined in the first step.

This framework is iterative. You will likely revisit earlier decisions as new constraints and insights emerge during implementation. Once the high-level design is framed, we must quantify how each inference-time lever multiplies cost and latency so we can budget for them deliberately.

## Inference-Time Scaling and the Cost/Latency Calculus

Understanding the four independent levers that control runtime performance is central to effective system design. Model size, series scaling, parallel scaling, and input context scaling interact in multiplicative ways. Mastering them allows you to fine-tune the trade-off between capability, cost, and latency on a per-step basis within your workflow.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down
Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

### Model Size Scaling

This is the most straightforward lever. Larger, more capable models like GPT-4.5 or Gemini 2.5 Pro have higher per-token costs than smaller, optimized models like GPT-5.4-mini or Gemini 2.5 Flash. For a high-value task where accuracy is paramount, using an expensive model may be justified. For high-volume, low-complexity tasks, a cheaper model is the better economic choice.

### Series Scaling

This refers to increasing the internal computational steps a model takes before answering, a feature often marketed as "thinking tokens" or "extended thinking" in models like Claude [[5]](https://docs.claude.com/en/docs/build-with-claude/extended-thinking). This allows the model to perform a longer chain-of-thought, which can improve reasoning on complex problems. However, this additional reasoning comes at the cost of increased latency and higher token usage. The best practice is to treat this as a dial, activating it only for the most complex planning or validation steps and setting a strict cap—for example, a maximum of 8,000 thinking tokens—to bound both spend and delay. However, simply increasing the token budget does not guarantee more effective reasoning. Some studies have observed that a model’s visible thought process can plateau, hitting a ceiling even as the requested budget increases [[12]](https://arxiv.org/html/2604.02460v1). This suggests that effective series scaling requires not just a larger budget, but also prompt-level incentives that encourage deeper reasoning.

### Parallel Scaling

This involves running the same prompt multiple times in parallel and selecting the best response. A common technique is majority vote, also known as self-consistency, where the most frequent answer is chosen. This approach can significantly improve reliability, especially for tasks with deterministic answers like math problems. Research has shown that, for a given computational budget, parallel scaling can sometimes outperform further serial reasoning [[6]](https://arxiv.org/html/2502.12215v1). The trade-off is a linear increase in cost, as each parallel run is billed independently.

While effective for certain tasks, research suggests that for long-horizon execution problems, additional sequential compute (series scaling) is often more effective at improving reliability than parallel compute [[11]](https://arxiv.org/html/2509.09677v1).

### Input Context Scaling

While relevant information is valuable, every additional token sent to the model carries a direct cost and adds to latency. As we have discussed, performance can also degrade if the context becomes too noisy. The key is to find the optimal balance. Techniques like RAG, summarization, and caching help keep the effective context small while preserving the necessary signal.

To illustrate how these levers multiply, consider the cost difference between a naive and a budgeted design for the same task.

**Naive Design (High Cost, High Capability):**
*   **Model:** GPT-5.5 (Input: $5.00/1M tokens, Output: $30.00/1M tokens) [[7]](https://openai.com/api/pricing/)
*   **Input Tokens:** 200,000 (full document dump)
*   **Output Tokens:** 20,000 (includes long chain-of-thought)
*   **Number of Parallel Runs:** 5 (for self-consistency)
*   **Calculation:** 5 * (($5.00/1M * 200k) + ($30.00/1M * 20k)) = 5 * ($1.00 + $0.60) = **$8.00**

**Budgeted Design (Low Cost, Targeted Capability):**
*   **Model:** GPT-5.4 mini (Input: $0.75/1M tokens, Output: $4.50/1M tokens) [[7]](https://openai.com/api/pricing/)
*   **Input Tokens:** 4,000 (RAG-retrieved chunks)
*   **Output Tokens:** 1,000 (concise answer)
*   **Number of Parallel Runs:** 1
*   **Calculation:** 1 * (($0.75/1M * 4k) + ($4.50/1M * 1k)) = $0.003 + $0.0045 = **$0.0075**

In this example, a few deliberate design choices lead to a cost reduction of over 1000x while potentially meeting the same quality target. Other optimizations, such as prompt caching for repeated calls and delegating heavy computation to external tools, can further reduce costs.

With these scaling levers quantified, we can now apply the full 7-step framework to produce the concrete global architecture for our Nova and Brown capstone project.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a more detailed architectural map than we saw in Lesson 12, cementing the intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down
Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

The image above illustrates the core architectural principle of our capstone: a clean separation of concerns. The unpredictable, open-ended research is handled by Nova, an MCP agent, while the predictable, iterative drafting and review process is managed by Brown, a stateful LangGraph workflow. This separation prevents context bloat and makes each component easier to debug and evolve independently.

This modular design is analogous to the shift from monolithic applications to microservices in traditional software engineering. Instead of a single, large prompt or agent trying to do everything, we are building specialized components with well-defined responsibilities and contracts. Just as microservices improved scalability and maintainability, this multi-agent approach avoids the brittleness of a single, massive model in favor of a more governable and robust system designed for enterprise complexity [[13]](https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices). Let's examine each component in more detail.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable across different clients. A simple MCP client runs an LLM-driven loop that follows a "Research Recipe" retrieved from the server. This recipe, defined in a master prompt, guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file.

The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures. The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt. For the client, we use FastMCP’s built-in `Client` class. Our implementation is a lightweight wrapper of about 200 lines of Python that connects to the server, fetches the research prompt, and runs a ReAct-style loop where the LLM decides which tool to call next.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down
Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this engine with a FastMCP server, which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call.

The exposed tools are:

-   **Generate Article:** This orchestrates a complete writing workflow: it loads context (guidelines, research, profiles, examples), generates media items using an orchestrator-worker pattern, writes the first draft, and then runs a configurable number of review-edit cycles using an evaluator-optimizer pattern.
-   **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, prioritizing this input over automated reviews.
-   **Edit Selected Text:** This runs a targeted review-edit cycle on a specific portion of the article while maintaining awareness of the full document.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down
Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces a `research.md` file and a structured `.nova/` directory. Brown takes these files, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean separation of concerns makes the system modular and easy to debug.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed for the entire process, where you define the article's topic, narrative, and any personal notes. Since the writing process is automated, a clear, well-articulated guideline is what distinguishes a high-quality article from generic AI-generated slop. If the ideas are not clearly enumerated and connected, the output will be sloppy. LLMs are excellent at translation and synthesis, but they are terrible at generating original, coherent ideas from scratch. Leaving too many gaps for the AI to fill without instruction leads to hollow, uninspired text.

The architecture and diagrams are now concrete. The final step is to translate these framework principles into an explicit, implementable decision matrix.

## Decision Matrix & Defaults for the Capstone

The abstract principles of our 7-step framework must be translated into specific, implementable defaults. The following matrix serves as the blueprint for our capstone project, tailored to the distinct demands of research (Nova) and writing (Brown). This is not an aspirational guide; it is the exact plan we will implement starting in the next lesson. Any deviation must be explicitly justified. Each row captures a decision, our chosen default, and a rationale that links back to the cost, latency, and reliability goals we established.

Table 1: Decision matrix for the capstone project.
| Decision Dimension | Our Default Choice | Rationale |
| :--- | :--- | :--- |
| **Model Family & Tiers** | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets** | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy** | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy** | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts** | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow. It ensures a clean separation of concerns, simplifies debugging, and enables replayability. While this approach has scaling limits for agents that might one day operate on entire codebases, it provides a robust and modular starting point for our current scope [[14]](https://www.amplifypartners.com/blog-posts/file-systems-for-agents). |

## Conclusion

In this lesson, we introduced a structured 7-step decision framework and applied it to our capstone project, resulting in the clean Nova-versus-Brown architecture and a concrete decision matrix. This system-level view, which prioritizes architectural trade-offs over isolated prompt-tuning, is the foundation that turns prototypes into scalable, production-ready agentic systems. By deliberately managing the four levers of inference-time scaling, we can design systems that are not only powerful but also debuggable and cost-effective.

The decisions and diagrams we have established here will serve as our guide throughout the upcoming implementation lessons. Every code-level choice we make will be aligned with the cost, latency, and quality goals we have defined.

In the next lesson, we will begin the hands-on construction of the FastMCP server and client loop for Nova, defining its core research tools and orchestrating the process that produces the final `research.md` file. Later, in Lessons 19-22, we will implement the durable writing workflows for Brown. The real skill you are developing is the ability to make these system-level trade-offs repeatedly, turning AI engineering from an art into a repeatable engineering practice.

## References

- [1] Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2023). Lost in the Middle: How Language Models Use Long Contexts. arXiv. https://arxiv.org/abs/2307.03172
- [2] What is the Model Context Protocol (MCP)?. (n.d.). Model Context Protocol. https://modelcontextprotocol.io/docs/getting-started/intro
- [3] What is the Model Context Protocol (MCP)? | Databricks. (n.d.). Databricks. https://www.databricks.com/blog/what-is-model-context-protocol
- [4] Human-in-the-loop. (n.d.). LangChain. https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/
- [5] Extended thinking & interleaved thinking docs. (n.d.). Claude. https://docs.claude.com/en/docs/build-with-claude/extended-thinking
- [6] Revisiting the Test-Time Scaling of o1-like Models. (2025). arXiv. https://arxiv.org/html/2502.12215v1
- [7] API Pricing. (n.d.). OpenAI. https://openai.com/api/pricing/
- [8] Positional Biases in Language Models are a Consequence of Information Retrieval Demands. (2025). arXiv. https://arxiv.org/html/2510.10276v1
- [9] Conductor: Deterministic Orchestration for Multi-Agent AI Workflows. (2026). Microsoft Open Source Blog. https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows
- [10] How to Build Production-Ready Human-in-the-Loop Autonomous Agent Oversight Systems. (n.d.). Galileo. https://galileo.ai/blog/human-in-the-loop-agent-oversight
- [11] The Illusion of Diminishing Returns: Measuring Long Horizon Execution in LLMs. (2025). arXiv. https://arxiv.org/html/2509.09677v1
- [12] Thinking on a Budget: Cheaper and Faster LLM Reasoning. (2026). arXiv. https://arxiv.org/html/2604.02460v1
- [13] Multi-agent AI systems: The next evolution of microservices. (n.d.). TEKsystems. https://www.teksystems.com/en/insights/article/multi-agent-ai-systems-microservices
- [14] File Systems for Agents. (n.d.). Amplify Partners. https://www.amplifypartners.com/blog-posts/file-systems-for-agents