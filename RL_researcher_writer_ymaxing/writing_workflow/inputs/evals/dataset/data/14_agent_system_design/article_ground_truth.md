# Lesson 14: LLM Agent System Design Considerations and Framework

In Lesson 12, we scoped the capstone you’ll build in Part 2: two production‑oriented agents that collaborate to produce publish‑ready technical articles. We defined the _research_ agent (Nova) and the _writing_ workflow (Brown), and you saw why we split exploration from deterministic drafting. In Lesson 13, we compared agent frameworks and chose a stack that fits that split: Nova ships as FastMCP tools (portable, steerable), while Brown runs a LangGraph workflow (durable, auditable), fronted by FastMCP for tool access.

This lesson zooms out from framework choice to **system design**. The same model can feel brilliant or brittle depending on how you budget reasoning, gate expensive steps with HITL, control context growth, and decide when to fan out work in parallel. These choices swing cost/latency by orders of magnitude and determine whether your agents feel like a demo or a dependable product.

We’ll give you a **decision framework** you can reuse for any agent project, then apply it to Nova and Brown. You’ll learn where to pay for extra “thinking,” when to parallelize, how to keep context small and relevant, and where to add human approvals to keep costs and quality within bounds.

## A General AI Engineering Decision Framework

Building a reliable agent system requires a structured approach. Use this step‑by‑step playbook to move from a problem statement to a design that balances capability, cost, and reliability.

  1. **Define Value, Constraints, Cost & Latency:** Start by defining the project’s success criteria. This includes the output quality bar, privacy or compliance requirements, expected volume, and your per-task spending limits. For example, a customer-support triage bot may require a <30s first response and 95% correct routing, which pushes you toward a fast model with hard timeouts and a retry-once policy. In contrast, an invoice-extraction job might demand ≥99.5% field accuracy with no tight latency SLA, so you can batch jobs at off-peak hours and pay for a higher-accuracy model, because the cost of a data entry error is far greater than the seconds saved on processing time.
  
  2. **Choose Model Family & Capability Mix:** Your infrastructure and business needs often dictate the first choice between closed APIs and open-weight models. Closed APIs from providers like OpenAI, Anthropic, and Google offer state-of-the-art capability with low operational overhead. Open-weight models such as Llama, Qwen, and DeepSeek provide maximum control, customization, and data locality. For example, a startup prototyping a creative writing assistant will likely choose a state-of-the-art closed API (like GPT-5 Pro) to maximize capability, while a hospital system automating patient record summaries must prioritize data privacy by using a self-hosted, open-weight model (like Llama). With a platform chosen, you then match the model’s reasoning depth to the task. Exploratory, planning-heavy tasks require a dedicated reasoning model (e.g., GPT-5 Thinking, Anthropic’s extended thinking, Gemini 2.5), whereas straightforward extraction or classification can utilize a faster, less expensive model. The final consideration is the data modality itself; if your application requires processing images, documents, or video, you must select a model family with strong multimodal capabilities.

  3. **Define Your Context Strategy:** As we learned in Lessons 3 and 9, a large context window is not a free lunch. It is a common mistake to dump full documents into the prompt, assuming the model can handle it. This approach often leads to the “[lost-in-the-middle](<https://arxiv.org/abs/2307.03172>)” problem, where performance degrades long before the context limit is reached. Instead, prioritize selective retrieval, compression, and structured summaries to manage cost and improve reliability. For instance, a real-time conversational sales agent must maintain a lean context to ensure low latency; it might use a sliding window or summarization to remember only the last few turns of the conversation. Conversely, an agent performing a legal search on a 100-page contract needs high recall. It might use a RAG approach to first identify and retrieve only the most relevant clauses into its context window, ensuring it has the necessary details without the cost and performance overhead of loading the entire document.
  
  4. **Pick an Orchestration Style:** Your orchestration choice, covered in Lesson 2, depends on the predictability of your task. Use a **workflow** for predictable, auditable processes with defined steps. Use an **agent** for open-ended exploration that requires dynamic tool use. A **hybrid** approach, as in our capstone, is often the most practical solution for complex problems. For example, an employee onboarding system that provisions accounts and sends welcome emails follows a fixed, predictable sequence, making it a perfect fit for a durable **workflow** where every step is auditable. However, a market research agent tasked with “investigating competitor strategies for a new product” needs the flexibility to dynamically decide which search queries to run, which articles to read, and which data to extract based on its findings.
  
  5. **Establish a HITL & Evaluation Loop:** Human-in-the-loop is essential to prevent runaway costs, inject domain expertise, and steer the agent through ambiguity. Define clear triggers for human intervention, such as low-confidence scores, sensitive actions, or policy flags. For example, you might allow an agent that categorizes internal IT support tickets to run fully autonomously, as the cost of a rare miscategorization is low. In contrast, an agent responsible for executing stock trades or publishing official company press releases must have a mandatory HITL approval gate before any action is taken. Your evaluation plan should start with small, task-specific tests that measure utility, factuality, and safety. Public leaderboards are a useful signal, but they are no substitute for custom evaluations tailored to your specific use case.
  
  6. **Set Tool Boundaries & Portability:** Keep heavy lifting inside your tools. Functions for scraping, data transformation, or complex calculations should be executed in your application code, not by the LLM. When an agent is asked, “What was our Q3 revenue growth compared to last year?”, its job is not to perform the math. Its role is to understand the user’s intent and call the calculate_revenue_growth(quarter=3) tool, which executes deterministic Python code. The LLM’s strength is in understanding the question, while the tool’s strength is in providing a factually correct answer. This division of labor prevents mathematical errors and makes the system far more reliable. Design your tools for portability using a standard like MCP. This makes them reusable across different runtimes and clients, such as IDEs, saving significant development effort over time.
  
  7. **Choose Durability & Observability:** For complex, stateful tasks, select a runtime like LangGraph that provides built-in checkpoints, resumability, and detailed tracing. These features are non-negotiable for production systems where reliability and debuggability are critical. A simple agent that generates a tweet from a blog post URL is stateless; if it fails, you can simply retry it with minimal cost. However, a multi-day agent workflow that analyzes a massive dataset to generate a report must be built on a durable runtime. If the system fails 20 hours into a 24-hour job, resumability means you don’t have to restart from scratch, saving immense time and computational cost.

## Inference-Time Scaling and the Cost/Latency Calculus

Modern LLM systems have four independent levers that you can tune at runtime to balance cost, latency, and quality. Understanding how they interact and multiply is central to effective system design. Each can be adjusted on a per-step basis within your workflow.

  1. **Model Size Scaling:** This is the most straightforward lever. Larger, more capable models like GPT-4.5 have higher per-token costs than smaller, optimized models like Gemini 2.5 Flash-Lite. For instance, to extract a shipping address from an email, a small, fast model can reliably perform this structured task at very low cost; using a large, expensive model would be overkill. However, for a task like “summarize the legal implications of this new patent filing,” the nuance and deep reasoning required justify the higher cost of a state-of-the-art model, as a cheaper model would likely fail to provide a helpful answer.
  
  2. **Series Scaling:** This refers to increasing the internal computational steps a model takes before answering, often called “thinking tokens.” You should treat extra reasoning as a budgeted dial, not a default. For example, a math tutoring agent might enable a deep-reasoning mode only when the student asks a non-routine, multi-step problem, and cap the “thinking budget”, a control exposed by providers like Anthropic, to bound latency and spend. OpenAI’s o-series research also highlights that more test-time thinking can boost accuracy, but you should still meter it carefully on a per-step basis to keep costs in check.
  
  3. **Parallel Scaling:** This involves running the same prompt multiple times in parallel and selecting the best response, typically through a majority vote (a technique known as self-consistency). This approach can significantly improve reliability for complex reasoning tasks, but it multiplies the cost by the number of parallel runs. For instance, if you task an agent with writing a critical Python function, a single run might miss an edge case. By running the prompt three times in parallel (N=3), you can take the majority consensus from the outputs, dramatically increasing the probability of getting a robust, correct function. This 3x cost is often a worthwhile trade-off for reliability. Interestingly, recent research suggests that for many o1-like models, parallel scaling is more effective and efficient than serial scaling.
  
  4. **Input Context Scaling:** The more information you provide in the prompt, whether from retrieved documents or long files, the higher your input token costs. However, larger context also improves the model's access to relevant information. The key is to find the optimal balance: include enough context for quality while using techniques like RAG, summarization, and selective retrieval to minimize unnecessary tokens [[1]](<https://www.oreilly.com/radar/llm-system-design-and-model-selection/>), [[2]](<https://openai.com/index/learning-to-reason-with-llms/?utm_source=chatgpt.com>), [[3]](<https://docs.claude.com/en/docs/build-with-claude/extended-thinking>), [[8]](<https://arxiv.org/html/2502.12215v1>).

![Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a890-06878604bb8e/image/w=1920,quality=90,fit=scale-down)Image 1: The four independent levers that drive runtime cost and latency in LLM agent systems, along with optimization strategies.

These levers multiply, meaning that architectural choices can lead to 10,000x or greater differences in the cost to solve a problem. Let’s consider a toy example. Suppose a task requires analyzing a 10,000-token document.

A **naïve approach** might use a large reasoning model, feed the entire document into the context, and run three parallel attempts for reliability.

- **Model:** GPT-5 pro (I[nput: $15/M, Output: $120/M](<https://openai.com/api/pricing/>))
- **Input Tokens:** 10,000 (document) + 500 (prompt) = 10,500
- **Output Tokens (with reasoning):** 2,000
- **Parallel Runs:** 3
- **Calculation:** (10,500 * $15/1,000,000 + 2,000 * $120/1,000,000) * 3 = ($0.1575 + $0.24) * 3 = **$1.19 per task**

A **budgeted approach** might use RAG to select the most relevant 1,000 tokens, use a cheaper “mini” model, and skip parallelism.

- **Model:** GPT-5-mini ([Input: $0.25/M, Output: $2.00/M](<https://openai.com/api/pricing/>))
- **Input Tokens:** 1,000 (from RAG) + 100 (prompt) = 1,100
- **Output Tokens:** 500
- **Parallel Runs:** 1
- **Calculation:** (1,100 tokens * $0.25/1,000,000 + 500 tokens * $2.00/1,000,000) * 1 = $0.000275 + $0.001 = **$0.001275 per task** [[7]](<https://openai.com/api/pricing/>)

By making smarter system design choices, we reduced the cost by nearly 1,000x. This is the power of a disciplined engineering approach. You can further optimize by capping reasoning tokens, aggressively trimming context, caching repeated prompts, and using tools to do the heavy lifting to keep the LLM’s context small and focused.

## Our Capstone: Global System Design

Now, let’s apply this framework to our capstone project. This section provides a higher-resolution architectural map than in Lesson 12, cementing intuition for how our two agents, Nova and Brown, work together to automate the research and writing process.

![Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b1-0ce253cd4ed8/image/w=1920,quality=90,fit=scale-down)Image 2: Global architecture of the two-agent capstone system, Nova and Brown, and their interfaces.

This diagram illustrates the core architectural principle of our capstone: a clean separation of concerns between exploration and execution. On the top is **Nova** , an MCP-driven **agent** designed to handle the unpredictability of open-ended research. On the bottom is **Brown** , a stateful **workflow** built with LangGraph to reliably execute the predictable, multi-step process of drafting and editing. This division allows us to use the right orchestration style and framework for each job. We will now examine each component in greater detail, beginning with the research agent, Nova.

### Research Agent (Nova)

Nova is an agent designed for comprehensive, automated research. Its architecture is built around the Model Context Protocol (MCP) to ensure its tools are portable and reusable.

An **MCP server** exposes a suite of research tools, resources, and prompts. A simple **MCP client** then runs an LLM-driven loop that follows a “Research Recipe” based on a master prompt retrieved from the server. This recipe guides the agent through a multi-step process: query sources, scrape and transcribe them, run iterative research loops with Perplexity, filter the results, select top sources for a full scrape, and finally compile everything into a `research.md` file. The entire process is steerable, with configurable HITL gates and a critical stop rule to prevent failures [[5]](<https://modelcontextprotocol.io/docs/getting-started/intro>). The MCP client’s only job is to orchestrate these tool calls based on the LLM’s decisions, following the research workflow defined in the server-hosted prompt.

For the MCP client, we use **FastMCP’s built-in**`**Client**`**class,** a lightweight, ready-to-use MCP client that connects to our server and handles all the protocol details (capability discovery, tool calling, resource fetching) out of the box. Our implementation is just ~200 lines of Python that wrap FastMCP’s `Client`: it connects to the server (via in-memory or stdio transport), fetches the research prompt, runs a simple ReAct-style loop where the LLM decides which tool to call next, executes that tool via `client.call_tool()`, and feeds the result back into the conversation.

![Image 3: End-to-end agent flow for the Nova Research Agent](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0a-8a265e430c78/image/w=1920,quality=90,fit=scale-down)Image 3: End-to-end agent flow for the Nova Research Agent

### Writing Workflows (Brown)

Brown is a stateful writing system built with LangGraph for orchestration. It manages state, checkpoints, and interrupts, making it a durable and reliable workflow engine. We front this powerful engine with a **FastMCP server** , which exposes Brown’s capabilities as three coarse-grained MCP tools. This hybrid architecture allows any MCP-compatible client, like an IDE, to trigger complex, long-running writing tasks with a simple tool call [[4]](<https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/>).

The exposed tools are:

- **Generate Article:** This orchestrates the following workflow: loads context (guidelines, research, profiles, examples), generates media items using the orchestrator-worker pattern, writes the first draft, then runs a configurable number of review-edit cycles using the evaluator-optimizer pattern.

- **Edit Article:** This runs a single review-edit cycle on the entire article based on human feedback, incorporating the evaluator-optimizer pattern with human input prioritized over automated reviews.

- **Edit Selected Text:** This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisions while maintaining context awareness of the full document.

![Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-babf-7da80cb1e8e4/image/w=1920,quality=90,fit=scale-down)Image 4: Sequence diagram illustrating the interaction flow for the Brown agent's "Generate Article" workflow.

The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` directory. Brown takes these, along with the original `article_guideline.md` and writing profiles, as inputs. The final outputs are a polished `article.md`, a folder of assets, and structured review artifacts. This clean separation of concerns makes the system modular, debuggable, and easier to maintain.

The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what it wants to write, the narrative of the article, personal notes or anything else that it considers important. As the writing itself is automated, a clear, well-articulated article guideline is what distinguishes a high-quality article from AI-generated slop. 

For example, if the ideas are not clearly enumerated and connected, the output will be sloppy. Another issue is leaving too many gaps for the AI to fill without instructions. This is a well-known issue: as we give the LLM more space to interpret, it fills that space with whatever it thinks fits, often resulting in empty text that conveys nothing. LLMs are amazing at translation, but terrible at generating original ideas. That’s why the article guidelines should be as detailed as possible. The trick is that you don’t have to care about how you write. It can be a raw brain dump of the idea that you want to write about, while delegating the boring research and writing to the setup we will teach you during this course.

## Decision Matrix & Defaults for the Capstone

Applying our decision framework to the capstone project enabled a concrete set of architectural choices. This matrix summarizes our defaults and their rationale, providing a clear blueprint for the system we will build in the upcoming lessons. It translates the abstract principles from Section 2 into specific, practical decisions that balance performance, cost, and reliability for our research and writing tasks. Each choice reflects a deliberate trade-off, optimized for the particular requirements of our two-agent system.
Decision Dimension| Our Default Choice| Rationale  

## Table 1: Decision matrix for the capstone project

| Decision Dimension          | Our Default Choice                                                                 | Rationale |
|-----------------------------|------------------------------------------------------------------------------------|-----------|
| **Model Family & Tiers**    | **Research Agent Thinking:** Gemini 2.5 Pro (reasoning-capable) with budgeted thinking.<br>**Tools (Scrape/Clean):** Fast, cheap models or non-LLM logic.<br>**Writing:** Reliable mid-tier model. | This tiered approach directly manages the **Model Size Scaling** lever. We reserve the expensive, powerful model for the most complex reasoning tasks (planning research), while delegating deterministic or simple tasks to cheaper models or pure code to optimize our cost-performance ratio. This directly addresses the cost levers by using the right model for the right job. |
| **Reasoning Budgets**       | **Reasoning Effort:** Medium by default, with capped thinking tokens.<br>**Parallel Attempts:** Off by default. | This gives us direct control over the **Series and Parallel Scaling** levers. We start with a conservative budget to control cost and latency, reserving expensive parallel runs only for critical validation steps where single-pass reliability proves insufficient. |
| **Context Strategy**        | Strict summaries and selective retrieval. Caching for boilerplate prompts, summaries, and retrieval features. | This is our primary method for controlling the **Input Context Scaling** lever. By aggressively managing the context window with summaries and selective retrieval, we avoid the "lost-in-the-middle" problem, minimize token costs, and improve performance. |
| **Orchestration & Portability** | **Research (Nova):** MCP-driven agent loop (FastMCP server + client).<br>**Writing (Brown):** LangGraph for durability, fronted by FastMCP for tool access. | This choice matches the orchestration style to the job. MCP solves the portability problem, making our research tools reusable and preventing framework lock-in. LangGraph solves the durability problem for the complex writing process, providing the necessary checkpoints and resumability that a simple agent loop would lack. |
| **HITL Policy**             | Approve next research queries, the full-scrape URL list, and the final article. Critical stop on tool failures (e.g., 0/N scrapes successful). | This policy provides key control points to manage cost, ensure quality, and steer the agents through ambiguous decision points without requiring constant human micromanagement. It strikes a balance between autonomy and oversight, preventing costly errors before they happen. |
| **Artifacts & Contracts**   | Guaranteed file-based handoffs (`research.md`, `article.md`, assets, reviews) with a stable on-disk layout. | This file-based contract decouples the **Nova** research agent from the **Brown** writing workflow and ensures a clean separation of concerns. This makes the system modular, simplifies debugging, and enables easy replayability for evaluation and auditing, which is essential for iterative development and quality assurance. |

Table 1: Decision matrix for the capstone project.

## Conclusion

You now have a structured decision framework for designing LLM agent systems, covering everything from model selection and reasoning budgets to orchestration style and HITL policies. You have also seen this framework applied to our capstone project, giving you a high-resolution global architecture of the Nova and Brown agents. This system-level understanding is the foundation upon which we will build in the coming lessons.

We will keep referring back to the decisions and diagrams in this lesson to connect our specific implementation choices to the broader system-level goals of managing cost, latency, and reliability. A solid architecture is the difference between a brittle prototype and a scalable, production-ready AI product.

In the next lesson, we will begin the hands-on implementation of our research agent, Nova. You will build the FastMCP server and client, define the core research tools, and orchestrate the multi-round research and filtering process that produces the final `research.md` file. Later, in Lessons 19–22, you will build the writing system Brown using LangGraph and expose its workflows as MCP tools for generating and editing articles.

### References

  1. LLM System Design & Model Selection. (n.d.). O’Reilly. <https://www.oreilly.com/radar/llm-system-design-and-model-selection/>
  2. Anthropic. (n.d.). Extended thinking & interleaved thinking docs. Claude Docs. <https://docs.claude.com/en/docs/build-with-claude/extended-thinking>
  3. LangChain. (n.d.). Human-in-the-loop. <https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/>
  4. Model Context Protocol. (n.d.). What is the Model Context Protocol (MCP)?. <https://modelcontextprotocol.io/docs/getting-started/intro>
  5. OpenAI. (n.d.). Introducing OpenAI o3 and o4-mini. <https://openai.com/index/introducing-o3-and-o4-mini/>
  6. OpenAI. (n.d.). API Pricing. <https://openai.com/api/pricing/>
  7. Revisiting the Test-Time Scaling of o1-like Models: Do they Truly Possess Test-Time Scaling Capabilities?. (n.d.). arXiv. <https://arxiv.org/html/2502.12215v1>
  8. Perplexity. (n.d.). Introducing Perplexity Deep Research. <https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research>
  9. Google. (n.d.). Gemini Deep Research & Gemini 2.5 overview. <https://gemini.google/overview/deep-research/>