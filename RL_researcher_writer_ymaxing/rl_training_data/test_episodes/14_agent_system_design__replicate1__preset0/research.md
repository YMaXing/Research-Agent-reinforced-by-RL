# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What causes lost-in-the-middle performance cliff in LLMs?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://atlan.com/know/llm/lost-in-the-middle-problem

Query: What causes lost-in-the-middle performance cliff in LLMs?

Answer: The 'lost-in-the-middle' problem occurs when LLMs prioritize the beginning and end of a context window over critical information buried in the middle. The reason the 'lost-in-the-middle' problem gains significant attention is that it causes LLMs to deliver sub-par outcomes despite having the right evidence in their context. Key reasons why information in the middle of the context window gets lost: The lost-in-the-middle problem gets worse when teams send too much unfiltered context into the model and hope the LLM will sort it out. The better fix starts before prompt assembly: decide which context is trusted, current, relevant, and specific enough to enter the context window. That means removing duplicate chunks, stale definitions, weak evidence, and loosely related policies, then serving the business context the model actually needs: definitions, lineage, ownership, policies, and decision traces. Lost-in-the-middle is the tendency of LLMs to use information at the beginning and end of a context window more reliably than information placed in the middle. The model may “see” the right passage, definition, instruction, or policy, but if it is buried mid-window, it may not carry enough weight in the final answer. Chroma’s 2025 context rot report tested 18 LLMs, including GPT-4.1, Claude 4, Gemini 2.5, and Qwen3 models. The report found that newer models still do not use context uniformly, and performance grows less reliable as input length grows. The research on Maximum Effective Context Window makes the same point. The paper distinguishes the advertised maximum context window from the maximum effective context window. In its tests, effective context varied by task, and all tested models fell short of their advertised maximum by as much as 99 percent. Atlan’s research on working memory in LLMs turns that into an enterprise lesson: context quality matters more than raw context volume. Long prompts create three problems:

-----

Phase: [EXPLOITATION]

### Source [2]: https://openreview.net/forum?id=XSHP62BCXN

Query: What causes lost-in-the-middle performance cliff in LLMs?

Answer: The performance of Large Language Models (LLMs) often degrades when crucial information appears in the middle of a long context, a “lost-in-the-middle” phenomenon that mirrors the primacy and recency effects in human memory. We propose that this behavior is not simply a flaw indicative of information loss but an adaptation to different information retrieval demands during pre-training: some tasks require uniform recall across the entire input (a long-term memory demand), while others prioritize the most recent information (a short-term memory demand). Consistent with this view, we show that this U-shaped performance curve emerges when LLMs (GPT-2 and Llama variants) are trained from scratch on two simple human memory paradigms simulating long-term and short-term memory demands. Our analysis reveals that while the recency effect directly aligns with short-term memory demand in the training data, the primacy effect is induced by the uniform long-term memory demand and is further influenced by the model's autoregressive properties and the formation of attention sinks. Our main findings from simple human memory paradigms also generalize to a sequence completion task, which more closely resembles the next-token prediction process used in LLM pre-training. Together, our findings reveal how information retrieval demands, model architecture, and structural attention dynamics during model training can jointly produce positional bias observed in LLMs.

-----

Phase: [EXPLOITATION]

### Source [3]: https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html

Query: What causes lost-in-the-middle performance cliff in LLMs?

Answer: Research has shown that large language models (LLMs) tend to overemphasize information at the beginning and end of a document or conversation, while neglecting the middle. This "position bias" means that if a lawyer is using an LLM-powered virtual assistant to retrieve a certain phrase in a 30-page affidavit, the LLM is more likely to find the right text if it is on the initial or final pages. MIT researchers have discovered the mechanism behind this phenomenon. They created a theoretical framework to study how information flows through the machine-learning architecture that forms the backbone of LLMs. They found that certain design choices which control how the model processes input data can cause position bias. The experiments showed a "lost-in-the-middle" phenomenon, where retrieval accuracy followed a U-shaped pattern. Models performed best if the right answer was located at the beginning of the sequence. Performance declined the closer it got to the middle before rebounding a bit if the correct answer was near the end. Ultimately, their work suggests that using a different masking technique, removing extra layers from the attention mechanism, or strategically employing positional encodings could reduce position bias and improve a model's accuracy. "While it is often true that earlier words and later words in a sentence are more important, if an LLM is used on a task that is not natural language generation, like ranking or information retrieval, these biases can be extremely harmful," Wu says. As a model grows, with additional layers of attention mechanism, this bias is amplified because earlier parts of the input are used more frequently in the model's reasoning process.

-----

</details>

<details>
<summary>What are four inference-time scaling levers for LLMs?</summary>

Phase: [EXPLOITATION]

### Source [4]: https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling

Query: What are four inference-time scaling levers for LLMs?

Answer: Four inference-time scaling levers for LLMs are: best-of-N ranking, self-consistency, batching requests, and parallelism strategies.

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.mirantis.com/blog/llm-optimization-techniques

Query: What are four inference-time scaling levers for LLMs?

Answer: Batching and request aggregation are among the most powerful levers for improving throughput and reducing per token cost. By processing multiple requests together, platforms amortize the cost of memory transfers and kernel launches, leading to much higher utilization. Analyses of production systems show that moving from single request serving to batches of around thirty two requests can reduce per token costs by roughly eighty five percent while increasing latency by only a modest amount. In Cost Per Token Analysis: Optimizing GPU Infrastructure for LLM Inference, Crosley quantifies this trade off, showing that batch sizes around 32 cut per token costs by about 85% with roughly 20% additional latency and that continuous batching can raise GPU utilization from around 40% to over 90%. ### Scale Inference with Parallelism Strategies

Parallelism strategies let platforms scale inference across multiple GPUs or even multiple nodes. Data parallelism replicates models so that more requests can be served concurrently. Tensor parallelism and pipeline parallelism split models across GPUs so that larger models can be hosted and served. Choosing the right mix of parallelism is an important part of LLM optimization. [...] AI inference is the stage where these techniques apply. From the platform perspective, each technique is a lever that can be pulled for particular applications and hardware types. A well designed platform, such as one built with k0rdent AI, makes it possible for teams to combine these techniques in ways that fit their specific constraints rather than forcing a single configuration.

-----

</details>

<details>
<summary>How does extended thinking work in Claude?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html

Query: How does extended thinking work in Claude?

Answer: When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. Claude incorporates insights from this reasoning before crafting a final response. The API response will include `thinking` content blocks, followed by `text` content blocks. Extended thinking gives Claude enhanced reasoning capabilities for complex tasks, while providing varying levels of transparency into its step-by-step thought process before it delivers its final answer. Whenever you enable Claude’s thinking mode, you will need to set a budget for the maximum number of tokens that Claude can use for its internal reasoning process. To turn on extended thinking, add a `thinking` object, with the `thinking` parameter set to enabled and the `budget_tokens` set to a specified token budget for extended thinking. The `budget_tokens` parameter determines the maximum number of tokens Claude is allowed to use for its internal reasoning process. In Claude 4 models, this limit applies to full thinking tokens, and not to the summarized output. Larger budgets can improve response quality by enabling more thorough analysis for complex problems, although Claude might not use the entire budget allocated, especially at ranges above 32K. Token usage tracking: Monitor thinking token usage to optimize costs and performance.

-----

Phase: [EXPLOITATION]

### Source [7]: https://cobusgreyling.substack.com/p/building-with-claude-extended-thinking

Query: How does extended thinking work in Claude?

Answer: Extended thinking gives Claude a scratchpad. Before answering, the model reasons through the problem step by step in a `thinking` block, then delivers the final answer in a `text` block. Enable thinking by adding a `thinking` parameter to your API call. The response comes back as a list of content blocks. First a `thinking` block with the model’s reasoning. Then a `text` block with the final answer. Two parameters control thinking: budget_tokens and type. With interleaved thinking, the model thinks, calls a tool, thinks again about the result, calls another tool, thinks again, then answers. On Opus 4.6 and Sonnet 4.6 with adaptive thinking, interleaved thinking is enabled automatically. You are charged for the full thinking tokens, not the summarised output. The billed output token count will not match the response token count. What changed with Claude Opus 4.6 and Sonnet 4.6 is that thinking is now summarised by default. You get the key reasoning steps, not the raw token stream. And there’s a new adaptive thinking mode that replaces the fixed `budget_tokens` approach.

-----

Phase: [EXPLOITATION]

### Source [8]: https://stevekinney.com/courses/ai-development/claude-code-thinking

Query: How does extended thinking work in Claude?

Answer: Extended thinking mode in Claude Code is a mechanism that allows the AI to perform extended reasoning and evaluate alternatives more thoroughly before producing an output. Instead of immediately generating code or an answer, Claude takes an “analytical pause” to understand the complete context and develop robust strategies. This process is particularly beneficial for complex problems where multiple factors need to be balanced. When Claude is in a thinking mode, its internal thought process is often displayed as italic gray text in the terminal, providing transparency into its reasoning. This visibility can be invaluable for developers to understand Claude’s approach and guide it effectively.

-----

Phase: [EXPLOITATION]

### Source [9]: https://www.lesswrong.com/posts/qkfRNcvWz3GqoPaJk/anthropic-releases-claude-3-7-sonnet-with-extended-thinking

Query: How does extended thinking work in Claude?

Answer: Claude 3.7 Sonnet introduces a new feature called "extended thinking" mode. In extended thinking mode, Claude produces a series of tokens which it can use to reason about a problem at length before giving its final answer. Claude was trained to do this via reinforcement learning, and it allows Claude to spend more time on questions which require extensive reasoning to produce better outputs. Users can specify how many tokens Claude 3.7 Sonnet can spend on extended thinking. When using Claude 3.7 Sonnet through the API, users can also control the budget for thinking: you can tell Claude to think for no more than N tokens, for any value of N up to its output limit of 128K tokens. This allows you to trade off speed (and cost) for quality of answer. Claude 3.7 Sonnet is both an ordinary LLM and a reasoning model in one: you can pick when you want the model to answer normally and when you want it to think longer before answering.

-----

Phase: [EXPLOITATION]

### Source [10]: https://gist.github.com/intellectronica/58571dda3581eec3e17a77741e8c858a

Query: How does extended thinking work in Claude?

Answer: Extended thinking gives Claude a "scratchpad" to reason through problems before responding. It’s the same model with more time to deliberate — not a separate model. Performance on complex tasks improves logarithmically with thinking tokens allocated.

-----

</details>

<details>
<summary>What is Model Context Protocol for agent portability?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://www.guild.ai/glossary/ai-agent-portability

Query: What is Model Context Protocol for agent portability?

Answer: Model Context Protocol (MCP), originally developed by Anthropic, standardizes how agents connect to external tools, data sources, and memory. MCP is the "USB-C port" for plug-and-play connections between LLMs (or agent frameworks) and external tools, memory stores, or live data. The two most significant are Anthropic's Model Context Protocol (MCP), which standardizes how agents connect to tools and data, and Google's Agent2Agent Protocol (A2A), which standardizes agent-to-agent communication. The A2A protocol focuses on agent collaboration, facilitating communication between AI agents. Both protocols are meant to complement each other. IBM's Agent Communication Protocol (ACP) under the Linux Foundation is also gaining adoption. AI vendor lock-in is API-based, usage-priced, and embedded inside product features. With agents, the coupling goes deeper: prompts, orchestration logic, tool schemas, and memory stores all become entangled with the platform. Switching means retraining assumptions embedded in your product, not just changing an API endpoint. Standardized Data and Configuration Formats Open data formats — storing and exchanging information in standard formats such as JSON, CSV — ensures your data remains portable and usable across different platforms. Standardized interaction protocols — new frameworks such as Model Context Protocol (MCP) — aim to codify how content is passed to models. This is a critical step toward plug-and-play AI components. Consider a deployment automator agent: if its tool definitions, memory store, and prompt templates use open formats, moving it from LangChain to CrewAI or a custom framework becomes a translation exercise, not a rebuild.

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.databricks.com/blog/what-is-model-context-protocol

Query: What is Model Context Protocol for agent portability?

Answer: The Model Context Protocol represents a fundamental shift in how AI applications access external data sources and tools. By providing an open protocol for discovery-based integration, the context protocol enables developers to build context-aware AI agents that can perform tasks using live data from popular enterprise systems without extensive boilerplate integration code. The Model Context Protocol (MCP) is an open standard that enables AI applications to connect seamlessly with external data sources, tools, and systems. Think of the Model Context Protocol as a USB-C port for AI systems—just as a USB-C port standardizes how devices connect to computers, MCP standardizes how AI agents access external resources like databases, APIs, file systems, and knowledge bases. MCP communications flow diagram between client, MCP servers, host, and backend server. The Model Context Protocol is an open-source, unified standard for interoperability that enables developers to build context-aware AI applications. MCP complements LLMOps by exposing runtime integration, observability, and governance controls that simplify deployment, monitoring, and lifecycle management of LLM applications. AI applications need access to assets such as local resources, databases, data pipelines (streaming/batch), search engines, calculators, and workflows for prompt conditioning and grounding generation. The context protocol standardizes how applications connect to those assets through a structured way that reduces boilerplate integration code.

-----

Phase: [EXPLOITATION]

### Source [13]: https://openai.github.io/openai-agents-python/mcp

Query: What is Model Context Protocol for agent portability?

Answer: The Model context protocol (MCP) standardises how applications expose tools and context to language models. From the official documentation: MCP is an open protocol that standardizes how applications provide context to LLMs. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals and accessories, MCP provides a standardized way to connect AI models to different data sources and tools. The Agents Python SDK understands multiple MCP transports. This lets you reuse existing MCP servers or build your own to expose filesystem, HTTP, or connector backed tools to an agent.

-----

Phase: [EXPLOITATION]

### Source [14]: https://www.ibm.com/think/topics/model-context-protocol

Query: What is Model Context Protocol for agent portability?

Answer: These impediments can be remedied with the Model Context Protocol (MCP). MCP allows AI agents to be context-aware while complying with a standardized protocol for tool integration. An AI agent is a system or program that is capable of autonomously performing tasks on behalf of a user or another system. It performs them by designing its workflow and by using available tools. Multiagent systems consist of multiple AI agents working collectively to perform tasks on behalf of a user or another system. The Model Context Protocol (MCP) serves as a standardization layer for AI applications to communicate effectively with external services such as tools, databases and predefined templates. MCP is not an agent framework, but a standardized integration layer for agents accessing tools. It complements agent orchestration frameworks. MCP can complement agent orchestration frameworks like LangChain, LangGraph, BeeAI, LlamaIndex and crewAI, but it does not replace them; MCP does not decide when a tool is called and for what purpose. MCP simply provides a standardized connection to streamline tool integration. Ultimately, the LLM determines which tools to call based on the context of the user’s request.

-----

Phase: [EXPLOITATION]

### Source [15]: https://en.wikipedia.org/wiki/Model_Context_Protocol

Query: What is Model Context Protocol for agent portability?

Answer: The Model Context Protocol (MCP) is an open standard and open-source framework introduced by Anthropic in November 2024 to standardize the way artificial intelligence (AI) systems like large language models (LLMs) integrate and share data with external tools, systems, and data sources. MCP provides a standardized interface for reading files, executing functions, and handling contextual prompts. Following its announcement, the protocol was adopted by major AI providers, including OpenAI and Google DeepMind.

-----

</details>

<details>
<summary>How do HITL triggers work in LangGraph workflows?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://www.elastic.co/search-labs/blog/human-in-the-loop-hitllanggraph-elasticsearch

Query: How do HITL triggers work in LangGraph workflows?

Answer: HITL is an AI concept that allows a real person to interact with AI systems to provide more context, evaluate responses, edit responses, ask for more information, and perform other tasks. This is very useful in low-error-tolerance scenarios, such as compliance, decision-making, and content generation, helping improve the reliability of LLM outputs. It's important to note that the primary purpose of HITL in agentic systems is validation, not blind trust in the agent's approach. HITL interventions should be reactive and triggered only when the system detects missing or ambiguous information. This ensures human involvement remains meaningful and adds value, rather than becoming a mandatory checkpoint that interrupts every workflow unnecessarily. The workflow begins when the lawyer submits a legal question. The system performs a vector search in Elasticsearch, retrieves the most relevant precedents, and presents them for the lawyer to choose from, using natural language. After the selection, the LLM generates a draft analysis and checks whether the information is complete. At this point, the workflow can follow two paths: If everything is clear, it proceeds directly to generate a final analysis; if not, it pauses to request clarification from the lawyer. Once the missing context is provided, the system completes the analysis and returns it, taking into consideration the clarifications. The two paths that the graph can take look like this: The left path includes an additional node that handles the clarification. requestClarification: This node triggers the second HITL step when the system identifies that the draft analysis lacks essential context. The workflow is interrupted, and the user is asked to clarify the missing contract details detected by the previous node.

-----

Phase: [EXPLOITATION]

### Source [17]: https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows

Query: How do HITL triggers work in LangGraph workflows?

Answer: The core mechanism behind the HITL setup in LangGraph is the concept of interrupts. Interrupts (using interrupt() and Command in LangGraph) enable us to pause graph execution at specific points, display certain information to the human, and await their input before resuming the workflow. Command is a versatile object that allows us to update the graph state (update), specify the next node to execute (goto), or capture the value to resume graph execution with (resume). Upon reaching the interrupt() function, execution pauses, and the payload passed into it is shown to the user. The payload passed in interrupt should typically be JSON or string format. But because interrupts work by rerunning the nodes they were called from, the node just reran the web search and passed along a different set of search results than the ones I approved earlier. Therefore, interrupts work best as a gate before an action, but if we use them after a non-deterministic step (like search), we need to persist the result or risk getting something different on resume. By placing __interrupt__ as part of a while loop, it means the loop keeps checking whether an interrupt is still ongoing. Once the interrupt is resolved, the key disappears, and the while loop exits. While interrupts are powerful in enabling HITL workflows, they can be disruptive if used incorrectly. As such, I recommend reading this LangGraph documentation. Here are some practical rules to keep in mind: For example, I faced an issue in the web search node where I placed an interrupt right after the Tavily search. The intention was to pause and allow users to review the search results for content generation.

-----

Phase: [EXPLOITATION]

### Source [18]: https://www.permit.io/blog/human-in-the-loop-for-ai-agents-best-practices-frameworks-use-cases-and-demo

Query: How do HITL triggers work in LangGraph workflows?

Answer: Interrupt & Resume: Used in: LangGraph. How it works: The agent is paused mid-execution using an interrupt() call. Human input is collected (yes/no, select from options, etc.), and then the workflow resumes based on the response. Best for: Approving tool calls (e.g. approve_access_request), Pausing long-running workflows, Inserting human checkpoints before final actions. LangGraph is ideal for building structured workflows where you need full control over how an agent reasons, routes, and pauses. Its interrupt() function lets you pause the graph mid-execution, wait for human input, and resume cleanly, making it a top choice for inserting HITL checkpoints. Use it when you need custom routing logic, deterministic, debuggable behavior, or when you're managing multiple agents/tool types. The agent initiates an access request or operation approval. The agent then pauses using LangGraph’s interrupt() function. A human reviewer (a parent) is prompted for approval. The workflow resumes only if approval is granted.

-----

</details>

<details>
<summary>How do file-based artifact contracts enable agent separation?</summary>

Phase: [EXPLOITATION]

### Source [19]: https://fast.io/resources/ai-agent-artifacts

Query: How do file-based artifact contracts enable agent separation?

Answer: File-based artifact contracts enable agent separation by defining distinct input and output directories, ensuring agents operate within their authorized scope and maintain clear accountability. An AI agent artifact is any tangible output created by an AI agent during task execution that exists outside the conversation context. Unlike transient responses, artifacts are persistent, versioned, and often need to be shared, edited, or referenced later. In production agent systems, artifacts include files, documents, code that exist independently of the agent. Workspace integration: Agents should save artifacts to locations where teams already work, not isolated sandboxes. This means creating or joining shared workspaces, setting appropriate permissions, and organizing files in existing folder structures. Event-driven workflows: When an agent creates or modifies an artifact, downstream systems need to react. Ownership and transfer: Agents may create artifacts on behalf of users or teams. The ability to transfer ownership, from the agent that generated a report to the human who requested it, maintains clear accountability and access control.

-----

Phase: [EXPLOITATION]

### Source [20]: https://blog.cloudflare.com/artifacts-git-for-agents-beta

Query: How do file-based artifact contracts enable agent separation?

Answer: Artifacts is designed to be agent-first, and notes enable agents to add notes (metadata) to Git objects. This includes prompts, agent attribution and other metadata that can be read/written from the repo without mutating the objects themselves. We’re calling this Artifacts: a versioned file system that speaks Git. You can create repositories programmatically, alongside your agents, sandboxes, Workers, or any other compute paradigm, and connect to it from any regular Git client. In the background, it starts to hydrate (download) file contents concurrently via a lightweight daemon. It prioritizes files that agents typically want to operate on first: package manifests (package.json, go.mod), configuration files, and code, deprioritizing binary blobs (images, executables and other non-text-files) where possible so that agents can scan the file tree as the files themselves are hydrated.

-----

Phase: [EXPLOITATION]

### Source [21]: https://arxiv.org/html/2603.16021v1

Query: How do file-based artifact contracts enable agent separation?

Answer: A typical stage contract looks like this: The Inputs table distinguishes between Layer 3 files (reference material that stays the same every run) and Layer 4 files (working artifacts from this specific run). The agent reads the CONTEXT.md, follows the instructions, and writes its output. The human reviews what landed in output/. If it needs adjustment, the human edits the file directly. The next stage reads whatever is there. The numbering encodes execution order. The folder boundaries enforce separation of concerns. The output/ directories are the Layer 4 handoff points: the output of stage 01 becomes available as input to stage 02. If a human edits a file in 01_research/output/ before running stage 02, the agent picks up the edited version. The references/ directories and _config/ folder hold Layer 3 material: the stable knowledge and constraints that persist across runs. Stage contracts make capabilities explicit. Markdown files support efficient correction (open, edit, save). Review gates at every stage boundary support dismissal (decide not to proceed, re-run the previous stage with different input, or abandon the run entirely).

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.scitepress.org/Papers/2026/144223/144223.pdf

Query: How do file-based artifact contracts enable agent separation?

Answer: This guarantees that tools and resumable work-flows can only access artifacts within their authorized scope. Retention policies and access logs further support compliance reviews and provenance audits. Complementary resume services capture the full invocation snapshot—event log, pending tool requests, locked artifacts—enabling human supervisors to intervene or continue execution after a pause. Together, artifact and resume services transform the agent runtime from a stateless chat loop into a stateful workflow engine suitable for regulated domains. Each layer publishes contracts to the layers above and below, ensuring that implementations

-----

</details>

<details>
<summary>How to build decision matrices for AI system tradeoffs?</summary>

Phase: [EXPLOITATION]

### Source [23]: https://www.meegle.com/en_us/topics/decision-matrix/decision-matrix-for-ai-projects

Query: How to build decision matrices for AI system tradeoffs?

Answer: Creating a decision matrix involves several key steps: 1. Define the Decision Objective: Clearly articulate the problem or choice you need to address. 2. Identify Options: List all possible alternatives or solutions. 3. Determine Criteria: Establish the factors that will influence your decision, such as cost, accuracy, or scalability. 4. Assign Weights: Prioritize criteria by assigning weights based on their importance to the decision. 5. Score Options: Evaluate each option against the criteria and assign scores. 6. Calculate Total Scores: Multiply scores by weights and sum them to determine the overall score for each option. 7. Analyze Results: Review the scores to identify the best choice and validate your decision. Decision matrices are versatile tools that can be applied to various aspects of AI projects, including: Model Selection: Comparing machine learning models based on accuracy, scalability, and computational requirements. Vendor Evaluation: Assessing AI solution providers based on cost, expertise, and support. Feature Prioritization: Ranking features for development based on user impact, technical feasibility, and ROI. Ethical Considerations: Weighing ethical implications of AI applications, such as bias and privacy concerns. Resource Allocation: Deciding how to allocate budget, personnel, and time across project phases.

-----

Phase: [EXPLOITATION]

### Source [24]: https://dev.to/william_geo/the-decision-matrix-method-for-engineering-trade-offs-k45

Query: How to build decision matrices for AI system tradeoffs?

Answer: Step 2: List All Criteria. Identify every criterion that matters for the decision. For a system architecture decision, this might include performance, scalability, development time, operational complexity, team familiarity, cost, vendor lock-in risk, and security posture. Be thorough but avoid redundancy. Each criterion should be independent -- meaning that its score should not be predictable from scores on other criteria. Step 3: Weight the Criteria. Step 4: Score Each Option. For each option and each criterion, assign a score relative to the baseline. The simplest scoring system uses three values: better than baseline (+1), same as baseline (0), worse than baseline (-1). More granular systems use five-point or ten-point scales, but the simpler system is often sufficient and avoids false precision. Score each criterion independently. Do not let your overall impression of an option influence individual criterion scores. Step 5: Calculate and Analyze. Iterative Refinement: The first pass through the Decision Matrix often reveals gaps in the option space. When you see that every option scores poorly on a particular criterion, ask whether a new option could be designed specifically to address that weakness. The matrix then serves as a design tool, not just an evaluation tool, by identifying exactly what properties an ideal solution would have. Multi-Round Evaluation: For critical decisions, use multiple evaluation rounds with different participants. Compare the matrices produced by different evaluators to identify areas of agreement and disagreement.

-----

</details>

<details>
<summary>When to choose workflows versus agents for orchestration?</summary>

Phase: [EXPLOITATION]

### Source [25]: https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows

Query: When to choose workflows versus agents for orchestration?

Answer: Deciding whether to use a standalone AI agent or an agentic workflow depends on the process’s complexity, the need for control, and the operational environment. Key considerations: 1. Task complexity: Use agents for simple, self-contained tasks, like a web search agent. For multi-stage or multi-agent pipelines, like supply chain management or financial trading, workflows offer better performance control through orchestration. 2. Governance and reliability: Agents can be unpredictable. If you need control, validation, or safety checks, workflows offer a deterministic structure with clear checkpoints, timeouts, and human sign-offs. 3. Dynamism vs predictability: Agents excel in dynamic environments, adapting in real time without predefined rules. Workflows require predefined decision points but can include AI-powered logic for flexible branching. If your process can be loosely modeled, workflows work well; if not, opt for agent loops. 4. Multi-agent coordination: Complex tasks often benefit from a modular approach that leverages specialized agents rather than one monolithic agent. Workflows orchestrate these efficiently—either sequentially or in parallel—and manage integration of their outputs. 5. Transparency and troubleshooting: Workflows are more debuggable and audit-friendly, with visual diagrams, logs, and metrics to trace decisions, failures, or delays. In contrast, agent reasoning is harder to interpret and may raise compliance concerns in regulated environments. 6. Development effort and flexibility: Agents are quicker to prototype and ideal for early-stage or lightweight use cases. Workflows may be more demanding to design but provide long-term reliability, scalability, and maintainability. When to use what: Use workflows for predictable, well-defined tasks; use agents for complex, adaptive scenarios requiring flexibility.

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.reddit.com/r/AI_Agents/comments/1nwwb5g/agents_vs_workflows_how_to_tell_the_difference

Query: When to choose workflows versus agents for orchestration?

Answer: Workflow: follows a known recipe. Steps and branches are mostly predetermined. Great for predictable tasks (route → transform → produce). Agent: runs a loop, makes choices, remembers, and can change strategy. It decides when to stop, when to ask for input, and when to try a different tool. A minimal agent usually has: Loop: Observe → Decide → Act → Reflect. Memory: state that persists across steps (and sessions) and shapes the next decision. Autonomy: can fail/retry, pick a new plan, or escalate without a human pushing every step. Structure: outputs decisions in JSON (next_action, args, stop_reason) instead of free text. Observability: logs every decision, tool call, and stop condition so you can debug reality, not vibes. When to prefer a workflow: The path is known, inputs are consistent, failure modes are well-defined, and you need speed/cost/predictability. When to reach for an agent: The path is unclear, the environment changes, tools can fail in messy ways, or you need multi-step adaptation (e.g., search → try → recover → re-plan). Practical pattern that helps: Start with a workflow baseline for the 80% cases. Add a small decision loop where unpredictability actually lives. Keep explicit strategies (e.g., “search, then re-query if empty; else ask user; else escalate”), not “figure it out.” Log everything. If you can’t see the chain of decisions, you can’t improve it.

-----

Phase: [EXPLOITATION]

### Source [27]: https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents

Query: When to choose workflows versus agents for orchestration?

Answer: Start with workflows. Add agents only when you can clearly justify the need. Workflows may not feel revolutionary, but they are reliable, testable, explainable, and cost-predictable. They teach you how your system behaves in production. They give you logs, fallback paths, and structure. And most importantly: they scale. When the use case needs flexibility, adaptation, and autonomy, then yes — bring in the agents. But only after you’re honest with yourself about whether you’re solving a real complexity… or just chasing a shiny abstraction. Complexity of the Task: Evaluate whether your use case has well-defined procedures. Can you write down steps that handle 80% of your scenarios without resorting to hand-waving? If your instructions involve phrases like “and then the system figures it out” — you’re probably in agent territory. Business Value vs. Volume: Assess the cold, hard economics of your use case. Is this a high-volume, cost-sensitive operation — or a low-volume, high-value scenario? Basically: if compute cost is more painful than getting something slightly wrong, workflows win. If being wrong is expensive and being slow loses money, agents might be worth it. Reliability Requirements.

-----

Phase: [EXPLOITATION]

### Source [28]: https://www.tellius.com/resources/blog/agents-vs-workflows-why-not-both

Query: When to choose workflows versus agents for orchestration?

Answer: AI agents are adaptive systems that can reason, plan, and take actions based on context. Automation workflows are deterministic sequences of steps designed to run the same way every time. Agents handle complexity and ambiguity; workflows handle scale and reliability. You need both for modern enterprise operations. If agents are so powerful, why do workflows still matter? Because autonomy without structure breaks things. Workflows provide the rails—repeatable, controlled execution across systems. Agents bring the intelligence—dynamic decisions, context awareness, reasoning. The strongest enterprise AI setups combine both. When should I use an AI agent vs. a workflow? Use a workflow when the steps are known, repeatable, and need to run reliably at scale. Use an AI agent when the path isn’t clear—diagnostics, exploration, or decision-making that requires reasoning, context understanding, and tool usage. Most real-world processes need both: agents to explore and decide, workflows to execute consistently.

-----

Phase: [EXPLOITATION]

### Source [29]: https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents

Query: When to choose workflows versus agents for orchestration?

Answer: How Agents Differ from Workflows: Control Flow - AI Workflows: Predefined, explicit; AI Agents: Dynamic, autonomous. Decision Making - AI Workflows: Hard-coded logic; AI Agents: LLM-driven reasoning. Tool Usage - AI Workflows: Orchestrated by code; AI Agents: Self-selected by agent. Adaptability - AI Workflows: Fixed paths; AI Agents: Flexible execution. Complexity - AI Workflows: Lower, more predictable; AI Agents: Higher, more capable. Use Cases - AI Workflows: Well-defined tasks; AI Agents: Open-ended problems. Choosing Between Workflows and Agents: Use AI Workflows when: Task requirements are clear and stable; Predictability is essential; You need explicit control over execution; Debugging and monitoring are priorities; Cost management is critical. Use AI Agents when: Task requirements are clear and stable (no, for agents it's when open-ended); Predictability is essential (no); You need explicit control over execution (no); etc. AI workflows are systems where LLMs and tools are orchestrated through predefined code paths. These systems follow a structured sequence of operations with explicit control flow. Key Characteristics: Predefined steps and execution paths; High predictability and control; Well-defined task boundaries; Explicit orchestration logic. When to Use Workflows: Well-defined tasks with clear requirements; Scenarios requiring predictability and consistency; Tasks where you need explicit control over execution flow; Production systems where reliability is critical. AI Agents: for complex, open-ended problems.

-----

</details>

<details>
<summary>How does LangGraph provide checkpoints for stateful workflows?</summary>

Phase: [EXPLOITATION]

### Source [35]: https://docs.langchain.com/oss/python/langgraph/persistence

Query: How does LangGraph provide checkpoints for stateful workflows?

Answer: LangGraph has a built-in persistence layer that saves graph state as checkpoints. When you compile a graph with a checkpointer, a snapshot of the graph state is saved at every step of execution, organized into threads. This enables human-in-the-loop workflows, conversational memory, time travel debugging, and fault-tolerant execution. LangGraph creates a checkpoint at each super-step boundary. A super-step is a single “tick” of the graph where all nodes scheduled for that step execute (potentially in parallel). For a sequential graph like START -> A -> B -> END, there are separate super-steps for the input, node A, and node B — producing a checkpoint after each one. Understanding super-step boundaries is important for time travel, because you can only resume execution from a checkpoint (i.e., a super-step boundary). In addition to super-step checkpoints, LangGraph also persists writes at the node (task) level. As each node within a super-step finishes, its outputs are written to the checkpointer’s checkpoint_writes table as task entries linked to the in-progress checkpoint. Under the hood, checkpointing is powered by checkpointer objects that conform to BaseCheckpointSaver interface. LangGraph provides several checkpointer implementations, all implemented via standalone, installable libraries. See checkpointer integrations for available providers.

-----

Phase: [EXPLOITATION]

### Source [36]: https://medium.com/@okanyenigun/built-with-langgraph-17-checkpoints-2d1d54e1464b

Query: How does LangGraph provide checkpoints for stateful workflows?

Answer: LangGraph provides checkpoints for stateful workflows using the InMemorySaver by default, which stores checkpoints in memory for instant access. It also supports external persistence options like PostgreSQL for more robust storage. To illustrate how checkpointing works in LangGraph, let’s construct a simple stateful workflow and configure it with in-memory persistence. from langgraph.graph import StateGraph, START, END from langgraph.checkpoint.memory import InMemorySaver from typing import Annotated from typing_extensions import TypedDict from operator import add class State(TypedDict): foo: str bar: Annotated[list[str], add] def node_a(state: State): print("Running node_a") return {"foo": "a", "bar": ["a"]} def node_b(state: State): print("Running node_b") return {"foo": "b", "bar": ["b"]} workflow = StateGraph(State) workflow.add_node(node_a) workflow.add_node(node_b) workflow.add_edge(START, "node_a") workflow.add_edge("node_a", "node_b") workflow.add_edge("node_b", END) checkpointer = InMemorySaver() graph = workflow.compile(checkpointer=checkpointer) When the workflow is compiled with this checkpointer, every state transition is automatically saved in memory. The config is telling LangGraph how to run and persist this execution. Most importantly, it specifies a thread_id. config = {"configurable": {"thread_id": "1"}} graph.invoke({"foo": ""}, config) The InMemorySaver serves as the checkpointer, storing state snapshots after each node (super-step).

-----

Phase: [EXPLOITATION]

### Source [37]: https://docs.langchain.com/oss/python/langgraph/overview

Query: How does LangGraph provide checkpoints for stateful workflows?

Answer: LangGraph provides low-level supporting infrastructure for any long-running, stateful workflow or agent. LangGraph does not abstract prompts or architecture, and provides the following central benefits: Persistence: Build agents that persist through failures and can run for extended periods, resuming from where they left off. Human-in-the-loop: Incorporate human oversight by inspecting and modifying agent state at any point. Comprehensive memory: Create stateful agents with both short-term working memory for ongoing reasoning and long-term memory across sessions. Debugging with LangSmith: Gain deep visibility into complex agent behavior with visualization tools that trace execution paths, capture state transitions, and provide detailed runtime metrics.

-----

Phase: [EXPLOITATION]

### Source [38]: https://use-apify.com/blog/langgraph-agents-production

Query: How does LangGraph provide checkpoints for stateful workflows?

Answer: LangGraph is LangChain's graph-based framework for building stateful, multi-step AI agents. Unlike simple chains, LangGraph lets you define nodes (functions), edges (transitions), conditional branching, loops, and human-in-the-loop checkpoints. It’s the go-to choice for production agents that need persistence, interrupts, and complex control flow. Checkpointing: None | PostgreSQL, memory. Use interrupt_before when compiling: graph.compile(interrupt_before=[‘node_name’]). The graph pauses before that node; resume with invoke(None, config) after human approval. Yes. Add a node that uses ApifyWrapper or the Apify API.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agentic-ai-explained-workflows-vs-agents.md">
<details>
<summary>Agentic AI Explained: Workflows vs Agents</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://orkes.io/blog/agentic-ai-explained-agents-vs-workflows>

# Agentic AI Explained: Workflows vs Agents

The cleaned markdown content is below:

The next wave in AI is agentic systems, where AI autonomously plan, decide, and act toward goals. In this article, we explain the two primary forms of agentic AI: **AI agents** and **agentic workflows**. Identify which strategy best suits your use case, and get a demonstration for how to build an an agentic workflow using Orkes Conductor, an enterprise-grade platform for orchestrating distributed systems and AI components.

## What is agentic AI?

Agentic AI refers to AI-driven systems that operate fully or semi-autonomously to achieve goals without step-by-step instructions. These systems integrate **reasoning modules** (often LLMs), **tool interfaces**, **memory**, and **feedback loops** to make decisions, adapt to context, and execute tasks in real time.

This approach represents a shift from traditional rule-based or predictive models toward **goal-driven, self-directed architectures**. Core characteristics include:

- **Autonomy:** Operate without requiring human input at every step.
- **Goal Orientation:** Plan and execute toward defined objectives.
- **Adaptability:** Adjust behavior in response to new inputs or environmental changes.
- **Self-Improvement:** Learn from outcomes to refine future decisions.
- **Interactivity:** Leverage tools, databases, systems, other AI agents, or humans as needed.

Agentic AI systems can be implemented as **AI agents** or **agentic workflows**, which offer distinct architectural patterns and benefits.

## AI agents vs agentic workflows

When it comes to agentic AI, many tend to confuse AI agents with agentic workflows. While both are decision-centric systems that can act autonomously, there are some fundamental differences in their underlying architecture and, subsequently, the extent of their autonomy. In general, agents are ideal for more dynamic uses, while workflows are best for more structured scenarios. Let’s explore each approach in turn.

### What are AI agents?

An **AI agent** is an autonomous software entity that perceives its environment, reasons about its goals, and takes actions. Examples include:

- A chatbot resolving customer queries
- A scheduling assistant managing calendar events
- A coding agent generating boilerplate code

Modern agents are often built around LLMs, configured with:

- System prompts for behavior guidance
- A toolset (e.g., APIs, search, database access)
- LLM parameters like `max_turns` or temperature for reasoning control

AI agents are the **building blocks of an agentic AI system**. Each agent encapsulates a specific capability or behavior, like booking flights or writing frontend code. Single-agent systems work well for bounded tasks, like a research agent. For complex, multi-domain challenges like website building, multi-agent systems are better for coordinating specialized agents.

**Architectural components:**

- **LLM core:** Reasoning and decision-making capabilities, powered by prompts
- **Tool Wrappers:** Interfaces to external APIs or systems
- **Memory:** Store of intermediate context or results

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_AI-Agent-Diagram.jpg

Agents reason recursively using instruction prompts, and can access tools via APIs as well as databases for memory.

A popular prompting pattern is the [ReAct framework](https://www.promptingguide.ai/techniques/react), where the agent is instructed to explicitly reason through **Thought → Action → Observation** cycles. Here is an example prompt:

textCopy

```text
Resolve the customer query with interleaving Thought, Action, Observation
steps.
- Thought can reason about the current situation.
- Action can be three types:
(1) Search [query], which searches the internal knowledge base for information regarding the customer query and returns a targeted response if it exists.
(2) Get [customer_info], which retrieves the customer's name, email, and order history.
(3) Book [flight], which retrieves the necessary information from the customer and calls the Booking API using the information.
- Observation can interpret results to decide next steps.
```

### What are agentic workflows?

What happens when you have to coordinate more complex processes that go beyond a single agent’s scope? This is where **agentic workflows** come into the picture.

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_Agentic-Workflow-Diagram.jpg

Agentic workflows are wider processes that involve multiple components, including AI agents and agentic decision nodes, making AI autonomy more governable.

An [agentic workflow](https://orkes.io/blog/what-are-agentic-workflows/) is a multi-step, dynamic process that orchestrates multiple API calls, AI tasks, agents, and even human-in-the-loop steps within a dynamic control graph. The workflow can branch, loop, or change course based on AI-driven evaluations, allowing it to adapt in real time.

Rather than embedding all logic inside a single agent, the workflow externalizes decision points and coordinates agents and services. Agentic workflows enable output validation, decision overriding, human oversight, and other observability features out-of-the-box. This is crucial for enterprise uses where **governance over autonomous agents** is needed.

**Example use cases:**

- Threat detection pipelines
- Fraud or claims processing
- Research assistants coordinating search, summarization, and synthesis

**Key elements:**

- **Task Nodes:** AI agents, LLM tasks, API calls, database queries, manual review steps
- **Decision Nodes:** AI-driven logic for routing control flow
- **Working Memory:** Shared state across workflow steps
- **Flexible Control Flow:** Branching, looping, and fallback paths for dynamic control

Essentially, the workflow provides a structure within which the AI agent can choose different paths or repeat steps as needed.

**Workflow implementation:**

Agentic workflows are typically built using [orchestration](https://orkes.io/blog/what-is-orchestration/) platforms that support AI-driven development. With state management, execution tracing, retry and error handling policies, the orchestration engine can coordinate many design patterns:

- Externalize a single agent’s high-level flow for observability
- Orchestrate multiple agents to collaborate on a project
- Embed an agent as part of a wider process

With tools like [Orkes Conductor](https://orkes.io/platform), developers can design workflows visually or programmatically, embedding AI tasks seamlessly alongside microservices, databases, and human oversight.

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_agentic-workflow-layer.jpg

Agentic workflows under the hood.

### Differences between an AI agent and an agentic workflow

In summary, an AI agent solves problems in an emergent manner: the LLM, powered by a prompt, dynamically directs tools and processes to accomplish tasks. Meanwhile, agentic workflows are orchestrated through explicit control flow paths consisting of tools, databases, AI agents, and even humans. Here’s a table summarizing the key differences between AI agents and agentic workflows:

| Area | AI Agent | Agentic Workflow |
| --- | --- | --- |
| **System Composition** | A single entity with an internal reasoning loop to execute the set of tasks it’s responsible for. | An orchestrated series of tasks across agents, services, and APIs, in a dynamic and iterative sequence. |
| **Architecture** | Opaque (black box), with minimal external control. | Modular, traceable, with externalized control flow. |
| **Autonomy** | Does not follow a strictly pre-coded sequence, with freedom to choose actions within whatever capabilities it has. | Follows defined stages at a high-level, but can dynamically choose execution paths at runtime​. |
| **Decision-Making** | Internalized within the agent’s chain-of-thought process. | Externalized to workflow decision nodes based on the LLM’s evaluation ( _if result X > threshold, do branch A else branch B_). |
| **Adaptability** | Highly adaptive, but also highly unpredictable. | Adaptive with guardrails, fallbacks, and manual reviews. |
| **Traceability** | Low — difficult to debug or audit. | High — step-wise visibility for auditing, logs, and metrics. |
| **Control** | Custom implementation required for guardrails and agent control. | Built-in controls via orchestration, human checkpoints, and retries. |

## Choosing between an agent and a workflow

Deciding whether to use a standalone AI agent or an agentic workflow depends on the process’s complexity, the need for control, and the operational environment. Here are some key considerations:

1.  **Task complexity**

    Use agents for simple, self-contained tasks, like a web search agent. For multi-stage or multi-agent pipelines, like supply chain management or financial trading, workflows offer better performance control through orchestration.

2.  **Governance and reliability**

    Agents can be unpredictable. If you need control, validation, or safety checks, workflows offer a deterministic structure with clear checkpoints, timeouts, and human sign-offs.

3.  **Dynamism vs predictability**

    Agents excel in dynamic environments, adapting in real time without predefined rules. Workflows require predefined decision points but can include AI-powered logic for flexible branching. If your process can be loosely modeled, workflows work well; if not, opt for agent loops.

4.  **Multi-agent coordination**

    Complex tasks often benefit from a modular approach that leverages specialized agents rather than one monolithic agent. Workflows orchestrate these efficiently—either sequentially or in parallel—and manage integration of their outputs.

5.  **Transparency and troubleshooting**

    Workflows are more debuggable and audit-friendly, with visual diagrams, logs, and metrics to trace decisions, failures, or delays. In contrast, agent reasoning is harder to interpret and may raise compliance concerns in regulated environments.

6.  **Development effort and flexibility**

    Agents are quicker to prototype and ideal for early-stage or lightweight use cases. Workflows may be more demanding to design but provide long-term reliability, scalability, and maintainability.

### When to use what

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_When_to_use_which.jpg

-   **AI Agents**: Best for self-contained, intelligent tasks with fast set-up and minimal control needs. Ideal for prototyping or experimenting with ultra-dynamic processes.

-   **Agentic Workflows**: Suitable for complex, multi-step, and high-reliability scenarios. They offer structure, observability, and safe integration of AI components.

One approach is to start with an agent for prototyping and migrate to a workflow as you scale into production for better governance.

## Building an agentic workflow in Orkes Conductor

In this section, we’ll walk through how to build an agentic workflow using Orkes Conductor, an orchestration engine for building modern workflows and agentic systems. We’ll use a practical example of an **agentic research assistant** to illustrate the process. [Check out the full tutorial documentation here.](https://orkes.io/content/templates/agentic-research)

**Step 1: Set up Orkes Conductor**

Sign up for the free [Developer Edition](https://developer.orkescloud.com/?utm_campaign=agentic-ai-blog&utm_source=orkes-blog&utm_medium=web) to get started with Orkes Conductor.

**Step 2: Design the workflow**

Here’s the high-level flow for our research agent workflow:

1.  Accept the user’s question as input and identify what to do next (e.g., literature review or research gap).
2.  Synthesize sub-topics based on the user’s questions.
3.  Use search grounding to compile research for each sub-topic.
4.  Synthesize research into a clear report and return the answer.

**To get started quickly**:

Import the agentic research workflow template from the **Launch Pad** in the [Developer Edition](https://developer.orkescloud.com/?utm_campaign=agentic-ai-blog&utm_source=orkes-blog&utm_medium=web)'s left navigation panel. Ensure you have API keys for OpenAI, Perplexity, and Anthropic, which will power the workflow's agentic and LLM components.

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_Launchpad_Screenshot.png

You will see the `agentic_research` workflow.

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_Workflow_Screenshot.png

Before you can run the workflow, you need to add the AI models and prompts in the next few steps.

**Step 3: Add models to the AI/LLM integrations**

Next, add the models to be used in the workflow For instance, if you plan to use OpenAI’s gpt-4o for researching topics, you must add the model to the integration in Conductor.

https://orkes.io/images/blogs/2025-05-19-agentic-ai-explained/Agentic-AI-Explained_LLM-Integrations.jpg

List of AI integrations available in Orkes.

Using the imported `agentic_research` workflow, the following AI integrations are required:

-   **OpenAI**–used to identify what task to do.
-   **Perplexity**—used for research generation with web search grounding.
-   **Anthropic**—used to synthesize the final report.

**To add the AI models for each integration:**

1.  Go to the **Integrations** tab in the left navigation bar.
2.  For each integration, select the **Add/Edit models** icon ( **+**) and select **New model**.
3.  Add the following models for the corresponding integration:
    -   **OpenAI**–gpt-4o
    -   **Perplexity**—sonar
    -   **Anthropic**—claude-3-7-sonnet-20250219

**Step 4: Define AI prompts**

Conductor has powerful features for defining reusable **AI prompt templates**. Use this to define the prompts for LLM models for generative, evaluative, and reasoning purposes.

For example, your research agent workflow needs to break down a research topic into relevant sub-topics, like so:

textCopy

```text
You are an academic research agent. Your task is to identify relevant and specific sub-topics within the field mentioned in the user's query:
"${user-query}"
```

Variables like `${user-query}` enable you to create flexible, reusable prompts.

Using the imported `agentic_research` workflow, the following required AI prompts have already been created:

-   **break\_into\_subtopics**—breaks a research query into distinct subtopics.
-   **query\_task\_decision**—determines subsequent tasks (research-gap, literature-review, both or none) based on the user's query.
-   **literature\_review\_task**—conducts a literature review given a subtopic.
-   **research\_gap\_task**—conducts a research-gap analysis given a subtopic.
-   **compile\_subtopic\_responses**—compiles a report, given a list of literature reviews and/or research gap analysis.

**To use the AI prompts in the workflow:**

1.  Go to **Definitions** \> **AI Prompts**.
2.  Select each prompt, add the associated **Model(s)**, then select **Save** \> **Confirm save**:

-   **break\_into\_subtopics**—\[yourOpenAIIntegration\]:gpt-4o
-   **query\_task\_decision**—\[yourOpenAIIntegration\]:gpt-4o
-   **literature\_review\_task**—\[yourPerplexityIntegration\]:sonar
-   **research\_gap\_task**—\[yourPerplexityIntegration\]:sonar
-   **compile\_subtopic\_responses**—\[yourAnthropicIntegration\]:claude-3-7-sonnet-20250219

**Step 5: Test the workflow**

Once the workflow is ready:

1.  Test it with a sample input question, like “what is the latest developments in liver cancer research?”
2.  Inspect the execution graph and task logs in the Conductor UI.
3.  Review the output.

Use this chance to debug and refine the workflow further.

**Step 6: Deploy and iterate**

When ready to deploy, you can expose the workflow as a service using Conductor’s [Start Workflow API](https://orkes.io/content/reference-docs/api/workflow/start-workflow-execution). You might also enhance it by implementing other orchestration patterns:

-   **Parallel agent execution**: Use a [Fork/Join](https://orkes.io/content/reference-docs/operators/fork-join) operator to conduct research across multiple LLM models in parallel, then compare their answers to produce a finalized research report.
-   **Human-in-the-loop**: Insert [Human](https://orkes.io/content/reference-docs/operators/human) tasks at key decision points. For example, you can enable the user to modify the generated list of research sub-topics before proceeding to the next task.

### Why use orchestration?

Orchestration is essential for implementing agentic systems effectively. Using Conductor, we gained:

-   **Observability**: Execution tracing, metrics, and logs into every AI action
-   **Governance**: Structure enforcement, human-in-the-loop approval gates
-   **Integration**: Seamless connection to services, APIs, and agents
-   **Reusability**: Prompts, tasks, and integrations sharing across workflows
-   **Reliability**: Built-in retries, error handling, and scaling

## Conclusion

Agentic AI enables flexible, autonomous automation. While standalone agents offer vast adaptability, agentic workflows provide the control, observability, and coordination needed for production environments. The optimal strategy combines both approaches:

-   Use workflows to govern and control AI agents
-   Use AI agents to inject intelligence and adaptability into workflows.

When done right, this hybrid model allows you to build powerful, flexible automation systems for use cases that were previously too brittle or impossible to automate. With orchestration tools like Orkes Conductor, teams can build robust, intelligent automation systems ready for enterprise use.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-human-in-the-loop-agentic-workflows-towards-data-sc.md">
<details>
<summary>Building Human-In-The-Loop Agentic Workflows</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows>

[Agentic AI](https://towardsdatascience.com/category/artificial-intelligence/agentic-ai/)

# Building Human-In-The-Loop Agentic Workflows

[Kenneth Leung](https://towardsdatascience.com/author/kennethleungty/)

Mar 25, 2026

10 min read

https://towardsdatascience.com/wp-content/uploads/2026/03/jeanna-song-_ZxH5kLIlFA-unsplash.jpg[Photo](https://unsplash.com/id/foto/sekelompok-orang-berjalan-naik-turun-tangga-spiral-_ZxH5kLIlFA) by Jeanna Song on Unsplash

Recent LLMs like OpenAI’s GPT-5.4 and Anthropic’s Opus 4.6 have demonstrated outstanding capabilities in executing long-running agentic tasks.

As a result, we see an increased use of **LLM agents** across individual and enterprise settings to accomplish complex tasks, such as running financial analyses, building apps, and conducting extensive research.

These agents, whether part of a highly autonomous setup or a pre-defined workflow, can execute multi-step tasks using tools to achieve goals with **minimal human oversight.**

However, ‘minimal’ does not mean zero human oversight.

On the contrary, human review remains important because of LLMs’ inherent probabilistic nature and the potential for errors.

These errors can propagate and compound along the workflow, especially when we string numerous agentic components together.

You would have noticed the impressive progress agents have made in the coding domain. The reason is that code is relatively easy to verify (i.e., it either runs or fails, and feedback is visible immediately).

But in areas like content creation, research, or decision-making, correctness is often subjective and harder to evaluate automatically.

That is why **human-in-the-loop (HITL)** design remains critical.

In this article, we will walk through how to use [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) to set up a **human-in-the-loop** agentic workflow for content generation and publication on [Bluesky](https://bsky.app/).

#### Contents

> **_(1)_** _[Primer to LangGraph](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/#section-one)_
>
> **_(2)_** _[Example Workflow](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/#section-two)_ **_(3)_** _[Key Concepts](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/#section-three)_ **_(4)_** _[Code Walkthrough](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/#section-four)_ **_(5)_** _[Best Practices of Interrupts](https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/#section-five)_

_You can find the accompanying_ [_GitHub repo here_](https://github.com/kennethleungty/Human-in-the-Loop-Workflow-LangGraph) _._

* * *

## (1) Primer to LangGraph

[LangGraph](https://docs.langchain.com/oss/python/langgraph/overview) (part of the [LangChain](https://www.langchain.com/langchain) ecosystem) is a low-level agent orchestration framework and runtime for building agentic workflows.

It is my go-to framework given its high degree of control and customizability, which is vital for production-grade solutions.

While LangChain offers a middleware object ( [HumanInTheLoopMiddleware](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)) to easily get started with human oversight in agent calls, it is done at a high level of abstraction that masks the underlying mechanics.

LangGraph, by contrast, does not abstract the prompts or architecture, thereby giving us the finer degree of control that we need. It explicitly lets us define:

- How data flows between steps
- Where decisions and code executions happen
- Where human intervention is required

Therefore, we will use **LangGraph** to demonstrate the HITL concept within an **agentic workflow**.

It is also helpful to distinguish between **agentic workflows** and **autonomous AI agents.**

**Agentic workflows** have predetermined paths and are designed to execute in a defined order, with LLMs and/or agents integrated into one or more components. On the other hand, **AI agents** autonomously plan, execute, and iterate towards a goal.

In this article, we focus on **agentic workflows**, in which we deliberately insert human checkpoints into a pre-defined flow.

https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/1QtM-00H9dQmzyJWYoAM4EA.pngComparing agentic workflows and LLM agents \| Image used under [license](https://github.com/langchain-ai/docs/blob/main/LICENSE)

* * *

### (2) Example Workflow

For our example, we shall build a social media content generation workflow as follows:

https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/1AAz1KW8te4HEclVQpQBSuA.pngContent generation workflow \| Image by author

1. User enters a topic of interest (e.g., “ _latest news about Anthropic_”).
2. The **web search node** utilizes the [Tavily](https://www.tavily.com/) tool to search online for articles matching the top.
3. The top search result is selected and fed into an LLM in the **content-creation node** to generate a social media post.
4. In the **review node**, there are two human review checkpoints:

**(i)** Present generated content for humans to approve, reject, or edit;

**(ii)** Upon approval, the workflow triggers the [Bluesky](https://bsky.app/) API **tool** and requests final confirmation before posting it online.

Here is what it looks like when run from the terminal:

https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/1S7mCy1vmw8Wl496zLyljTQ.pngWorkflow run in terminal \| Image by author

And here is the live post on my Bluesky profile:

https://contributor.insightmediagroup.io/wp-content/uploads/2026/03/1esK6HGx-47fIjw5maS-M-A.pngBluesky social media post generated from workflow \| Image by author

> Bluesky is a social platform similar to Twitter (X), and it is chosen in this demo because its API is much easier to access and use.

* * *

## (3) Key Concepts

The core mechanism behind the HITL setup in LangGraph is the concept of **interrupts**.

**Interrupts**(using `interrupt()` and `Command` in LangGraph) enable us to **pause graph execution** at specific points, **display** certain information to the human, and **await** their input before resuming the workflow.

> [Command](https://blog.langchain.com/command-a-new-tool-for-multi-agent-architectures-in-langgraph/) is a versatile object that allows us to update the graph state (`update`), specify the next node to execute (`goto`), or capture the value to resume graph execution with (`resume`).

Here is what the flow looks like:

**(1)** Upon reaching the `interrupt()` function, execution pauses, and the payload passed into it is shown to the user. The payload passed in `interrupt` should typically be JSON or string format, e.g.,

```python
decision = interrupt("Should we get KFC for lunch?") # String shown to user
```

**(2)** After the user responds, we pass the response values to the graph to resume execution. It involves using `Command` and its `resume` parameter as part of re-invoking the graph:

```python
if human_response == "yes":
    return graph.invoke(Command(resume="KFC"))
else:
    return graph.invoke(Command(resume="McDonalds"))
```

**(3)** The response value in `resume` is returned in the `decision` variable, which the node will use for the rest of the node execution and subsequent graph flow:

```python
if decision == "KFC":
    return Command(goto="kfc_order_node", update={"lunch_choice": "KFC")
else:
    return Command(goto="mcd_order_node", update={"lunch_choice": "McDonalds")
```

Interrupts are dynamic and can be placed anywhere in the code, unlike static breakpoints, which are fixed before or after specific nodes.

That said, we typically place interrupts either within the nodes or within the tools called during graph execution.

* * *

Finally, let’s talk about **checkpointers**. When a workflow pauses at an interrupt, we need a way to **save its current state** so it can resume later.

We therefore need a checkpoint to [persist](https://docs.langchain.com/oss/python/langgraph/persistence) the state so that the state is not lost during the interrupt pause. Think of a checkpoint as **a snapshot of the graph state** at a given point in time.

For development, it is acceptable to save the state in memory with the `InMemorySaver` checkpointer.

For production, it is better to use stores like [Postgres](https://pypi.org/project/langgraph-checkpoint-postgres/) or [Redis](https://pypi.org/project/langgraph-checkpoint-redis/). With that in mind, we shall use the [**SQLite**](https://pypi.org/project/langgraph-checkpoint-sqlite/) **checkpoint** in this example instead of an in-memory store.

To ensure the graph **resumes exactly at the point** where the interrupt occurred, we need to pass and use the same **thread ID**.

> _Think of a thread as an single execution session (like a separate individual conversation) where each one has a unique ID, and maintains its own state and history._

The thread ID is passed into `config` on each graph invocation so that LangGraph knows which state to resume from after the interrupt.

Now that we have covered the concepts of interrupts, `Command`, checkpoints, and threads, let’s get into the code walkthrough.

* * *

> _As the focus will be on the human-in-the-loop mechanics, we will not be covering the comprehensive code setup. Visit the [GitHub repo](https://github.com/kennethleungty/Human-in-the-Loop-Workflow-LangGraph) for the full implementation._

## (4) Code Walkthrough

### (4.1) Initial Setup

We start by installing the required dependencies and generating API keys for Bluesky, OpenAI, LangChain, LangGraph, and Tavily.

```python
# requirements.txt
langchain-openai>=1.1.9
langgraph>=1.0.8
langgraph-checkpoint-sqlite>=3.0.3
openai>=2.20.0
tavily-python>=0.7.21
```

```python
# env.example
export OPENAI_API_KEY=your_openai_api_key
export TAVILY_API_KEY=your_tavily_api_key
export BLUESKY_HANDLE=yourname.bsky.social
export BLUESKY_APP_PASSWORD=your_bluesky_app_password
```

* * *

### (4.2) Define State

We set up the `State`, which is the shared, structured data object serving as the graph’s central memory. It includes fields that capture key information, like post content and approval status.

The `post_data` key is where the generated post content will be stored.

* * *

### (4.3) Interrupt at node level

We mentioned earlier that interrupts can occur at the node level or within tool calls. Let us see how the former works by setting up the human review node.

The purpose of the review node is to pause execution and present the draft content to the user for review.

Here we see the `interrupt()` in action (lines 8 to 13), where the graph execution pauses at the first section of the node function.

The `details` key passed into `interrupt()` contains the generated content, while the `action` key triggers a handler function (`handle_content_interrupt()`) to support the review:

The generated content is printed in the terminal for the user to view, and they can approve it as-is, reject it outright, or edit it directly in the terminal before approving.

Based on the decision, the handler function returns one of three values:

- `True` (approved),
- `False` (rejected), or
- String value corresponding to the user-edited content (`edited`).

This return value is passed back to the review node using `graph.invoke(Command=resume…)`, which resumes execution from where `interrupt()` was called (line 15) and determines which node to go next: approve, reject, or edit content and proceed to approve.

* * *

### (4.4) Interrupt at Tool level

Interrupts can also be defined at the tool call level. This is demonstrated in the next human review checkpoint in the **approve node** before the content is published online on Bluesky.

Instead of placing `interrupt()` inside a node, we place it within the `publish_post` tool that creates posts via the Bluesky API:

Just like what we saw at the node level, we call a handler function (`handle_publish_interrupt`) to capture the human decision:

The return value from this review step is either:

- `{"action": "confirm"}`, or
- `{"action": "cancel}` ,

The latter part of the code (i.e., from line 19) in the `publish_post` tool uses this return value to determine whether to proceed with post publication on Bluesky or not.

* * *

### (4.5) Setup Graph with Checkpointer

Next, we connect the nodes in a graph for compilation and introduce a SQLite checkpointer to capture snapshots of the state at each interrupt.

> _SQLite by default only allows the thread that created the database connection to use it. Since LangGraph uses a thread pool for checkpoint writes, we need to set_`check_same_thread=False` _to allow those threads to access the connection too._

* * *

### (4.6) Setup Full Workflow with Config

With the graph ready, we now place it into a workflow that kickstarts the content generation pipeline.

This workflow includes configuring a thread ID, which is passed to each`graph.invoke()`. This ID is the link that ties the invocations together, so that the graph pauses at an interrupt and resumes from where it left off.

You might have noticed the `__interrupt__` key in the code above. It is simply a special key that LangGraph adds to the result whenever an `interrupt()` is hit.

In other words, it is the **primary signal indicating that graph execution has paused** and is waiting for human input before continuing.

By placing `__interrupt__` as part of a `while` loop, it means the loop keeps checking whether an interrupt is still ongoing. Once the interrupt is resolved, the key disappears, and the while loop exits.

With the workflow complete, we can run it like this:

```python
run_hitl_workflow(query="latest news about Anthropic")
```

* * *

## (5) Best Practices of Interrupts

While interrupts are powerful in enabling HITL workflows, they can be disruptive if used incorrectly.

As such, I recommend reading this [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/interrupts#rules-of-interrupts). Here are some practical rules to keep in mind:

- Do not wrap interrupt calls in try/except blocks, or they will not pause execution properly
- Keep interrupt calls in the same order every time and do not skip or rearrange them
- Only pass JSON-safe values into interrupts and avoid complex objects
- Make sure any code before an interrupt can safely run multiple times (i.e., idempotency) or move it after the interrupt

For example, I faced an issue in the web search node where I placed an interrupt right after the Tavily search. The intention was to pause and allow users to review the search results for content generation.

But because interrupts work by rerunning the nodes they were called from, the node just reran the web search and passed along a different set of search results than the ones I approved earlier.

Therefore, interrupts work best as a gate before an action, but if we use them after a non-deterministic step (like search), we need to persist the result or risk getting something different on resume.

* * *

## Wrapping It Up

Human review can seem like a bottleneck in agentic tasks, but it remains critical, especially in domains where outcomes are subjective or hard to verify.

LangGraph makes it straightforward to build HITL workflows with interrupts and checkpointing.

Therefore, the challenge is deciding where to place those human decision points to strike a good balance between oversight and efficiency.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="categories-of-inference-time-scaling-for-improved-llm-reason.md">
<details>
<summary>Categories of Inference-Time Scaling for Improved LLM Reasoning</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling>

# Categories of Inference-Time Scaling for Improved LLM Reasoning
### And an Overview of Recent Inference-Scaling Papers (Including Recursive Language Models)

Inference scaling has become one of the most effective ways to improve answer quality and accuracy in deployed LLMs.

The idea is straightforward. If we are willing to spend a bit more compute, and more time at inference time (when we use the model to generate text), we can get the model to produce better answers.

Every major LLM provider relies on some flavor of inference-time scaling today. And the academic literature around these methods has grown a lot, too.

Back in March, I wrote an overview of the inference scaling landscape and summarized some of the early techniques.

In this article, I want to take that earlier discussion a step further, group the different approaches into clearer categories, and highlight the newest work that has appeared over the past few months.

As part of drafting a full book chapter on inference scaling for _[Build a Reasoning Model (From Scratch)](https://mng.bz/Nwr7)_, I ended up experimenting with many of the fundamental flavors of these methods myself. With hyperparameter tuning, this quickly turned into thousands of runs and a lot of thought and work to figure out which approaches should be covered in more detail in the chapter itself. (The chapter grew so much that I eventually split it into two, and both are now available in the early access program.)

PS: I am especially happy with how the chapter(s) turned out. It takes the base model from about 15 percent to around 52 percent accuracy, which makes it one of the most rewarding pieces of the book so far.

What follows here is a collection of ideas, notes, and papers that did not quite fit into the final chapter narrative but are still worth sharing.

I also plan to add more code implementations to the [bonus materials on GitHub](https://github.com/rasbt/reasoning-from-scratch) over time.

**Table of Contents (Overview)**

1. Inference-Time Scaling Overview

2. Chain-of-Thought Prompting

3. Self-Consistency

4. Best-of-N Ranking

5. Rejection Sampling with a Verifier

6. Self-Refinement

7. Search Over Solution Paths

8. Conclusions, Categories, and Combinations

9. Bonus: What Do Proprietary LLMs Use?


You can use the left-hand navigation bar in the article’s web view to jump directly to any section.

# 1\. Inference-Time Scaling Overview

_Inference-time scaling_ (also called _inference-compute scaling_, _test-time scaling_, or just _inference scaling_) is an umbrella term for methods that allocate more compute and time during inference to improve model performance.

This idea has been around for a long time, and one can think of ensemble methods in classic machine learning as an early example of inference-time scaling. I.e., using multiple models requires more compute resources but can give better results.

​Even in LLM contexts, this idea has been around for a long time. However, I remember it became particularly popular (again) when OpenAI showed an inference-time scaling and training plot in one of their o1 announcement blog articles last year ( [Learning to Reason with LLMs](https://openai.com/index/learning-to-reason-with-llms/)).

https://substackcdn.com/image/fetch/$s_!oiA2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffff769a2-8324-4fbd-8659-4615e4711ce2_1600x900.png _Figure 1: Spending additional resources during inference (left) and training (right) generally improves the model’s accuracy._

I think this figure, adapted from OpenAI’s [blog post](https://openai.com/index/learning-to-reason-with-llms/), nicely captures the idea behind the two knobs we can use to improve LLMs. We can spend more resources during training (more data, bigger models, more or longer training stages) or inference.

Actually, in practice, it’s even better to do both at the same time: train a stronger model and use additional inference scaling to make it even better.

In this article, I only focus on the left part of the figure, inference-time scaling techniques, i.e., those training-free techniques that don’t change the model weights.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="checking-your-connection.md">
<details>
<summary>Checking your connection</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://techxplore.com/news/2025-06-lost-middle-llm-architecture-ai.html>

# Checking your connection

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="lost-in-the-middle-an-emergent-property-from-information-ret.md">
<details>
<summary>Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs | OpenReview</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://openreview.net/forum?id=XSHP62BCXN>

# Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs | OpenReview

## Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs

### [Nikolaus Salvatore](https://openreview.net/profile?id=~Nikolaus_Salvatore2 ""), [Hao Wang](https://openreview.net/profile?id=~Hao_Wang3 ""), [Qiong Zhang](https://openreview.net/profile?id=~Qiong_Zhang6 "")

**Keywords:** language modeling, lost-in-the-middle phenomenon, attention dynamics, human memory parallels

**TL;DR:** The lost-in-the-middle phenomenon in LLMs can arise through fundamental human memory tasks with different retrieval demands.

**Abstract:**

The performance of Large Language Models (LLMs) often degrades when crucial information appears in the middle of a long context, a “lost-in-the-middle” phenomenon that mirrors the primacy and recency effects in human memory. We propose that this behavior is not simply a flaw indicative of information loss but an adaptation to different information retrieval demands during pre-training: some tasks require uniform recall across the entire input (a long-term memory demand), while others prioritize the most recent information (a short-term memory demand). Consistent with this view, we show that this U-shaped performance curve emerges when LLMs (GPT-2 and Llama variants) are trained from scratch on two simple human memory paradigms simulating long-term and short-term memory demands. Our analysis reveals that while the recency effect directly aligns with short-term memory demand in the training data, the primacy effect is induced by the uniform long-term memory demand and is further influenced by the model's autoregressive properties and the formation of attention sinks. Our main findings from simple human memory paradigms also generalize to a sequence completion task, which more closely resembles the next-token prediction process used in LLM pre-training. Together, our findings reveal how information retrieval demands, model architecture, and structural attention dynamics during model training can jointly produce positional bias observed in LLMs.

**Primary Area:** foundation or frontier models, including LLMs

#### **Paper Decision**

Decisionby Program Chairs26 Jan 2026, 03:51 (modified: 06 Feb 2026, 00:04)Everyone

**Decision:** Reject

#### Meta Review of Submission21588 by Area Chair VjhG

Meta Reviewby Area Chair VjhG06 Jan 2026, 21:01 (modified: 09 Feb 2026, 01:48)Everyone

**Summary:**

The paper proposes that the "Lost-in-the-Middle" (LitM) phenomenon in LLMs is an emergent adaptation to conflicting information retrieval demands during pre-training. By training models (GPT-2, Llama variants) from scratch on synthetic cognitive science paradigms, Free Recall (long-term demand) and Running Span (short-term demand), the authors demonstrate that LitM emerges when these demands are combined. They identify two key mechanisms: Recency aligns with short-term retrieval demands, while Primacy emerges from long-term demands interacting with autoregressive architecture and attention sinks. The submission further validates these findings using a masked sequence completion task and ablation studies.

The primary concerns identified across the reviews centered on model scale and practical significance. While the experimental design was praised for its "clean" isolation of variables, high-confidence reviewers (L5FX, Xfd2) questioned whether LitM is a fundamental property of the architecture or merely an artifact of limited capacity in smaller models. Specifically, the concern was that if the phenomenon disappears in state-of-the-art models (as suggested by prior literature), the mechanism described here might be of limited relevance to the current frontier of foundation models. Reviewers also noted the reliance on synthetic tasks, questioning the transfer of these findings to naturalistic pre-training distributions.

Based on these concerns and the rebuttal data, I recommend _Rejection_. The authors provided a robust rebuttal that included training larger models (up to Llama 3.2 3B). However, this new data confirmed the trend identified by the reviewers: the "U-shape index" steadily declines as model size increases. While the authors argue the underlying mechanism persists even when behavioral symptoms diminish (being compensated by capacity), this interpretation does not adequately address the practical relevance concern raised by the negative reviewers.

This decision balances methodological rigor against significance. The paper is scientifically sound and the experimental design is elegant. However, the high-confidence reviewers (L5FX, Xfd2) correctly identified that the central phenomenon is transient, and it disappears as models scale up. While mechanistic understanding has intrinsic value, the paper does not demonstrate that these insights lead to actionable improvements for larger models or predict when mitigations will be effective. Consequently, the contribution is primarily of theoretical interest regarding small-model dynamics rather than current impact for the foundation model community.

**Reviewer Concerns:**

### Addressed concerns:

- The reviewer Ni46 noted that dropping entire layers was too coarse. The authors added Appendix A.3 with "surgical" ablations (head masking/key rescaling), which satisfied this technical critique.
- The reviewer Xfd2 raised novelty concerns. The distinction from Wu et al. (2025) was clarified in the revision, distinguishing the mechanistic cause (causal masking) from the functional emergence (retrieval demands).

### Outstanding Concerns:

- Reviewers L5FX and Xfd2 raised concerns about the significance and the scale of the reported results, which remains the pivotal issue here. The rebuttal added Appendix A.2, showing the U-shape index drops significantly with model scale. While the authors argue the mechanism is still detectable, the problem effectively vanishes. This strengthens the negative reviewers' position that the work lacks urgency or impact for the current generation of models.
- Reviewers Ni46 and Xfd2 argued against validity, since the bridge between synthetic memory tasks and real-world "wild" pre-training remains theoretical. The masked sequence completion task is a good proxy, but does not fully resolve whether these mechanisms dictate behavior in complex natural language tasks.

**Reviewer Scores:**

- **Reviewer Ni46. Original score: 6. Predicted score: 6**. The authors addressed the specific technical critique regarding ablation. However, the reviewer's broader concerns about external validity and naturalistic benchmarks remain outstanding, making a jump to the next tier (8) unlikely.
- **Reviewer Xfd2. Original score: 4. Predicted score: 4**. The novelty was clarified, but the scale experiments confirmed their doubts about relevance.
- **Reviewer L5FX. Original score: 2. Predicted score: 2**. This reviewer’s primary critique was that LitM is an artifact of scale. The rebuttal provided data (Appendix A.2) that supported this view. They are unlikely to increase their score.
- **Reviewer Bp4r. Original score: 6. Predicted score: 6**. They were positive but had lower confidence; likely remains unchanged.

#### **General Reviewer Response**

Official Commentby Authors03 Dec 2025, 18:36Everyone

**Comment:**

We thank all the reviewers for their valuable and constructive comments. Lost-in-the-middle is an important phenomenon to understand in LLMs. We are glad that the reviewers find (i) our approach “novel” and “effective” (Ni46, Xfd2, L5FX31, Bp4r), (ii) our results “convincing” in demonstrating the “causal contribution” and “root cause” of information-retrieval demands (Xfd2, L5FX31, Bp4r), (iii) our findings “generalizable” and tested over multiple model architectures (Ni46, Xfd2, L5FX31), and (iv) our paper “well-written” with “clear exposition” (Ni46, Xfd2).

Before addressing each reviewer’s comments in detail, we highlight three common comments identified across reviewers and our responses.

* * *

### Q1. Model scale (Ni46, Xfd2, L5FX)

To assess the role of model scale, we trained several larger open-weight models from scratch on the same task suite used in the main paper: Gemma-2 2B, Qwen-2.5 1.5B, and Llama-3.2 3B, and added these results to Appendix A.2. These models span distinct architectural design choices and positional-encoding variants.

Consistent with our previous conclusion based on GPT-2 small, GPT-2 large, and Llama 2-1.3B, the lost-in-the-middle effect also emerges from these additional models. The degree of the effect reduces with increasing model scale. We quantify this trend using a U-shape index, which declines steadily from GPT-2 to Gemma-2, Qwen-2.5, and Llama-3.2, demonstrating that the U-shape pattern decreases with increasing model complexity. These results indicate that the attenuation is primarily scale-related rather than specific to the Llama architecture or training dynamics, aligning with prior observations that larger models exhibit reduced positional bias (see Appendix A.2).

* * *

### Q2. Validation over more naturalistic tasks (Ni46, Xfd2)

We used well-defined and synthetic tasks to train models from scratch. Two reviewers suggested using more naturalistic tasks to demonstrate the proposed mechanisms. We argue that using simplified rather than naturalistic tasks is a strength rather than a weakness of the present work:

- Previous work has already demonstrated the existence of the lost-in-the-middle effect in more naturalistic tasks. The goal of the current work is to isolate the minimal task conditions under which the lost-in-the-middle phenomenon emerges. By stripping away the confounding factors present in naturalistic tasks, we’re aiming to pinpoint which retrieval demands and architectural features are causally responsible for the effect.

- To bridge the gap between controlled memory experiments and more natural tasks, we replicated our results using a masked sequence completion task, which more closely resembles the next-token prediction process in real-world LLM pre-training.


While two reviewers (Ni46, Xfd2) viewed the simplicity of our experimental design as a potential weakness, the other two reviewers highlighted this same design's contribution:

- **L5FX:** “ Training models from scratch on well-defined, synthetic tasks is a significant strength. This methodology provides a clean environment for causal attribution, effectively isolating the training objectives as the primary variable and avoiding the confounding factors of large, diverse pre-training datasets. ”
- **Bp4r:** “This is the first paper that I have seen to illustrate the cause clearly convincingly without involving other causal factors where the paper 1) trains from scratch 2) using synthetic almost toy tasks to illustrate this.”

* * *

### Q3. Novelty compared to existing work (Xfd2, L5FX)

Two reviewers requested clarification on which findings are confirmations of prior work and which are new insights.

- We’ve revised the Discussion section to explicitly separate which findings are confirmatory from what are new. Liu et al. document the U-shape in natural long-context tasks, and Wu et al. analyze how causal masking leads to positional bias; our novel contribution is to identify a minimal task framework (free recall, running span, and combined task) that shows how specific information-retrieval demands generate the lost-in-the-middle effect.

- We added a new paragraph in the Related Work section to directly compare our work with Wu et al. (2025) and Barbero et al. (2024). These mechanistic accounts describe why positional bias emerges from architectural constraints. Our results distinguish from these perspectives by identifying when these biases affect downstream task performance and behavior. This helps reconcile why positional biases are visible in some settings and attenuated in others, even within the same architecture.

- The way we draw our key hypothesis based on cognitive science literature is novel. While prior work has noted the similarity of the lost-in-the-middle effect in LLMs and humans, our paper is the first in transferring what we know about human memory, i.e., what contributes to the lost-in-the-middle effect in humans, to systematically test these hypotheses in LLMs.


#### Official Review of Submission21588 by Reviewer Ni46

Official Reviewby Reviewer Ni4602 Nov 2025, 18:32 (modified: 12 Nov 2025, 05:04)Everyone

**Summary:**

The paper studies the “lost-in-the-middle” effect in LLMs and argues it is an emergent adaptation to information-retrieval (IR) demands during training rather than merely a flaw. The authors train GPT-2 (small/large) and Llama-3.2-1B from scratch on toy but principled human-memory paradigms: Free Recall (uniform long-term demand) and Running Span (end-weighted short-term demand). Training on both yields a U-shaped serial-position curve (primacy + recency), i.e., lost-in-the-middle (Figure 2C; Figure 3G–I). They further: (i) link primacy to autoregressive processing by showing strong primacy in an RNN seq2seq but not in a bidirectional T5 (Figure 4), and (ii) implicate attention sinks by ablating heads/layers flagged by a sink metric, which selectively degrades tasks with long-term retrieval demand and removes primacy (Figure 5D–G). Finally, they replicate the phenomena in a masked sequence completion task that more closely resembles next-token prediction (Figure 6). Formal task definitions and additional ablations are in the Appendix.

**Soundness:** 3: good

**Presentation:** 3: good

**Contribution:** 3: good

**Strengths:**

Originality: Elegant, minimal task-design lens that unifies primacy/recency and lost-in-the-middle; neat architectural contrast (RNN/T5) and sink-based analysis. (Figures 2–6).
Quality: Multiple models (GPT-2 S/L, Llama-3.2-1B) trained from scratch; consistent behavioral metrics; ablations that selectively hit long-term retrieval tasks (Figure 5G; Figure 6G).
Clarity: Clear exposition; formal task definitions; helpful visuals of sink heatmaps and SPC/PFR/CRP curves (pp. 6–8, 12–13).
Significance: Offers a theoretical framing likely to influence evaluation/mitigation strategies and spur work that tailors training curricula or architectures to desired IR profiles.

**Weaknesses:**

External validity: No natural-data or real long-context benchmarks (QA/book-sum/code) to demonstrate that the mechanism quantitatively explains or predicts behavior in practice.
Ablation method: “Attention-sink dropout” removes entire attention layers flagged as sinks; this may simultaneously remove useful computation. More surgical interventions (head-level masking, key-positional rescaling) or counterfactual re-routing would strengthen causal claims.
Sensitivity & controls: Limited analysis of ε thresholding (0.8), dependence on context length, tokenization, or positional encodings (e.g., RoPE vs absolute). The combined-task loss weighting (FR vs RS) and its effect on the U-shape are not detailed.
Scale: Only up to ~1B parameters; the paper notes reduced U-shape at larger scale—directly charting trend vs scale/length would be valuable.

**Questions:**

Generalization: Can you test the IR-demand hypothesis on natural long-context suites (e.g., re-ordering/context-insertion diagnostics) to predict when mitigations help?
Loss mixing: How are FR and RS combined—same batch, same loss weight? What happens when you sweep the mixing ratio; does the U-shape vary smoothly?
Sequence length: Does primacy’s dependence on attention sinks persist at much longer contexts (e.g., 4k–32k)? Any qualitative shifts?
Sink metric robustness: Results vs different ε thresholds and identification methods? What about ablating non-sink heads/layers matched for magnitude to isolate the sink-specific effect?
Positional encodings/architectures: How do RoPE variants, ALiBi, or state-space and hybrid encoder-decoder models affect primacy/recency under the same tasks?
Surgical ablations: Could you replace sink layers with frozen copies or attention reweighting to rule out capacity loss as the driver?
Data realism: If you train on skewed temporal distributions (e.g., recency-heavy Zipfian windows approximating web/news), does the learned curve match your predicted balance of primacy/recency?

**Rating:** 6: marginally above the acceptance threshold. But would not mind if paper is rejected

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**Code Of Conduct:** Yes

#### Official Comment by Authors

Official Commentby Authors03 Dec 2025, 18:56Everyone

**Comment:**

Thank you for your constructive feedback and insightful questions. Below we address your questions in detail.

* * *

### Weaknesses:

**External validity:**

We agree that validating mechanisms on natural long-context benchmarks is important, but the lost-in-the-middle effect has already been documented on several real datasets, and our goal was to isolate the minimal task conditions under which the phenomenon emerges. By stripping away confounding factors present in naturalistic tasks, we aim to pinpoint which retrieval demands and architectural features are causally responsible for the effect. We also bridge the gap between controlled recall experiments and natural settings using the masked sequence-completion task, which preserves next-token prediction structure while allowing controlled manipulation of retrieval demands. We acknowledge this point of concern and have highlighted that prior work on the U-shaped effect has hinted at its presence in more naturalistic datasets (L265). We pose direct confirmation of retrieval demands producing this effect in natural data as a direction for future work.

**Ablation method:**

Please refer to Q2. \[Alternative attention sink ablation experiments\] in the General Response.

In response to your concerns, we implemented two more targeted ablations (per-head masking of identified sink heads and key–positional rescaling) following your suggestions. Both interventions reproduce similar patterns to our original findings: primacy and long-term retrieval degrade selectively, while short-term retrieval remains largely unaffected. These new analyses have been added to appendix section A.3.

**Sensitivity and controls:**

We have clarified why we chose a single value for ε thresholding. A threshold of 0.8 cleanly isolates layers containing clear attention sinks, while lower thresholds broaden ablation to many more layers and cause nonspecific degradation. We clarify that FR and RS losses were weighted equally during combined-task training (added to Task Definitions). Although a full sweep over tokenization, positional encodings, and context lengths is beyond scope, we now report results from additional model families with differing encodings and longer training contexts. These models show similar primacy/recency/U-shape patterns (section A.2), providing evidence that these effects generalize beyond the presented architectures.

**Scale:**

Please refer to Q1. \[Generalizability and model scale\] in the General Response. In revision, we included additional models spanning a wider parameter range and added a plot quantifying U-shape strength as a function of scale (Figure 8, appendix A.2). The trend aligns with our and prior observations: primacy and recency weaken with increased scale, while overall recall improves.

* * *

### Questions:

**Generalization:**

Since natural long-context benchmarks already show the U-shape (and multiple works provide mitigation strategies), our focus was identifying minimal conditions that reproduce the effect to expose underlying causes. We include direct predictive tests on natural suites as future work.

**Loss mixing:**

We added clarification that FR and RS were combined with equal loss weighting in shared batches (Task Definitions). While a full sweep is outside the revision scope, our IR-demand hypothesis suggests a smooth trade-off between primacy and recency under different mixing ratios. This would be a natural extension for future work.

**Sequence length:**

Our new scale experiments (section A.2) modestly extend context (64→256 items), and within this range the primacy–sink relationship remains stable. Because attention sinks and lost-in-the-middle behavior both scale with sequence length in prior work, evaluating the interaction at 4k+ contexts would clarify whether sink-driven primacy strengthens, saturates, or changes qualitatively. We mention this in the Future Work section.

**Sink metric robustness:**

We clarify the use of ε=0.8. As shown in Fig. 5A–C, ε=0.8 is the only value that cleanly isolates genuine sink heads. Lower values add many more layers to the ablation, causing broad degradation that obscures sink-specific effects.

**Positional encodings and architectures:**

Our revision includes results from additional model families with varying scales and positional embeddings, and the primacy/recency patterns persist (appendix A.2). A broader sweep over other architectural components is beyond scope, but we list these as directions for future work.

**Surgical ablations:**

We added more targeted ablations (head masking and key–positional rescaling), which reproduce the main effects (appendix A.3). More extensive study of attention sink layers is a promising future direction.

**Data realism:**

Our masked-sequence experiments show that sampling distributions shift the primacy/recency balance, and extending this to more realistic temporal statistics is a natural follow-up. We mention this in Future Work.

#### Official Review of Submission21588 by Reviewer Xfd2

Official Reviewby Reviewer Xfd201 Nov 2025, 10:26 (modified: 12 Nov 2025, 05:04)Everyone

**Summary:**

The paper draws parallels with resource-rational perspectives in cognitive psychology, explaining the recency and primacy effect usually observed in autoregressive LLMs. It interprets the positional bias as an emergent behavior arising due to different memory demands and architectural design.

It trains model from scratch with minimal training tasks to show emergence of U-shaped curve. Their analysis reveals that training for free recall task shows primacy effect and short-term running span task shows recency effect. And combining both tasks yield U-shaped curve, also referred to as lost-in-the-middle effect.

The paper performs controlled study to show these effects over 3 small to medium scale autoregressive LLMs. Where the U-shaped phenomena is weakened for the largest model (LLama 3B). This is attributed to the large scale of the model. The paper shows that causal architecture is one of the main reason for the emergence of lost-in-the-middle effect and it disappears when using bidirectional encoder-decoder architecture. The causal architecture leads to the formation of attention sinks which is responsible for the primacy effect. The paper performs ablation on attention sinks by destroying stronger sinks to confirm their effect.

**Soundness:** 3: good

**Presentation:** 3: good

**Contribution:** 2: fair

**Strengths:**

1. The work proposed an isolated setup with minimal tasks to demonstrate the formation attention sinks using a causal architecture. This is a novel contribution of this work. The memory demand task design is simple and easy to interpret.

2. The study makes clear observations by training the model from scratch. It makes a convincing case for the role of short- and long-term memory demands and for the role of causal model for the observed primacy and recency bias.

3. The study conducts thorough empirical analysis with different memory demands. The study disrupting attention sinks with long-term memory demands is particularly insightful. Additional experiment with masking strategy shows that the observations are generalizable.

4. The paper is well-structured and easy to read.


**Weaknesses:**

1. Large-scale experiment is only limited to one Llama model which does show weak U-shaped curve. It is unclear whether the weakened U-shape performance is due to the scale of the model, model architecture or training dynamics. More baseline at multiple scales are needed to confirm the effect of scaling.

2. While the proposed memory tasks allow clean analysis, but it is a much simplified task compared to real LLM tasks. Although masked sequence completion does show similar U-shaped behavior, it is unclear whether such attention-sink issue arise in general-purposed LLMs in practice. For example, do recent large-scale (>10B) general-purpose LLMs trained with standard next-token prediction format also show this U-shaped effect?

3. The contribution of this work are unclear. Which experiment setup and evaluation metrics are novel in this work? Please clarify which findings are confirmations of previous work and which are new insights (include comparison to Liu et al 2023 and Wu et al. 2025) . Also, is the usage SPC, PFR, and CRP to study positional bias novel to this work or has it been proposed before?


Some more questions are included in the Questions section below.

**Questions:**

1. It is an interesting observation that larger models show flattened U-shaped recall curves. It is unclear how scaling changes the attention pattern and distributes it more evenly. A quantitative analysis of attention distribution and sink strength would clarify this observation.

2. Wu et al. 2025 already showed in their work that causal nature of the autoregressive model is responsible for primacy effect due to attention sink formation. It is unclear what new insights does this study offer in this regard specifically?

3. It is insightful to know that attention sinks formed at early positions in causal models are responsible for the primacy effect. However, it is unclear how do the formation of these attention sinks occur and why only in the early tokens.


**Flag For Ethics Review:** No ethics review needed.

**Rating:** 4: marginally below the acceptance threshold. But would not mind if paper is accepted

**Confidence:** 4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**Code Of Conduct:** Yes

#### Official Comment by Authors

Official Commentby Authors03 Dec 2025, 19:03Everyone

**Comment:**

Thank you for your constructive feedback and insightful questions.

* * *

### Weaknesses

**Large-scale experiment is only limited to one Llama model**

Please refer to Q1. \[Generalizability and model scale\] in General Response. We agree that isolating the source of the weakened U-shape requires looking across multiple scales. In the revision, we have added experiments with additional model sizes and included a plot showing how U-shape strength varies with scale. These results indicate that the attenuation is primarily scale-related rather than specific to Llama architecture or training dynamics, and they align with prior observations that larger models exhibit reduced positional bias (see appendix section A.2).

**Simplified tasks versus natural LLM tasks**

Our goal here was to isolate the minimal task conditions under which the U-shape effect emerges. The U-shaped effect has already been observed in large general-purpose LLMs trained with standard next-token prediction (in addition to the appearance of attention sinks), so our aim was to explain why it reliably appears rather than re-demonstrate it. Our masked-sequence experiments serve as a bridge toward natural pretraining, showing that when next-token prediction is paired with the mixed retrieval demands, the same effects emerge. We have added references to related works that have previously investigated the U-shaped phenomenon and attention sinks (but not necessarily the link between them), which have shown the U-shaped effect appearing in larger, general-purpose LLMs (L484 in the Discussion section).

**Clarification of contributions and novelty**

We’ve revised the Discussion section to explicitly separate what is confirmatory from what is new and to compare against Liu et al. (2023) and Wu et al. (2025) (L466)). Liu et al. document the U-shape in natural long-context tasks, and Wu et al. analyze how causal masking leads to positional bias; our main new contributions are: (i) a minimal task framework (free recall, running span, and combined task) that shows how specific information-retrieval demands generate primacy, recency, and the full U-shape, (ii) a masked sequence-completion task that connects these retrieval demands to a more standard next token prediction task, and (iii) causal evidence that attention sinks functionally support primacy and long-range recall by sink ablation studies (plus the architecture comparison (autoregressive RNN vs T5) under identical tasks). SPC-, PFR, and CRP-style curves have been used extensively to study these effects in cognitive science experiments, but their use in analyzing this effect in LLMs is relatively recent.

* * *

### Questions

**Scaling and flattened U-shaped curves**

Please refer to Q1. \[Generalizability and model scale\] in the General Response.

Our results (appendix A.2) show flatter serial-position curves in larger models. Without deeper attention-level analysis we cannot determine exactly how attention allocation changes with scale. Prior work suggests that scale smooths positional biases and reduces early-token anchoring. A systematic comparison of sink magnitude and attention dispersion across layers and scales would directly test this, and we added it to Future Work.

**Relationship to Wu et al. (2025)**

Please refer to Q3. \[Novelty compared to existing work\] in the General Response.

Wu et al. provide a mechanistic account linking causal masking to positional bias. Our work builds on that by showing when these architectural biases actually produce primacy. We show that primacy emerges only when causal architectures are paired with uniform long-term retrieval demands, and disappears in autoregressive models trained on short-term retrieval tasks. We also demonstrate that primacy, recency, and full U-shapes can be induced or removed by manipulating task demands alone, and that attention sinks selectively support long-range retrieval via ablation studies. More clarification is added in the Discussion (L476).

**Formation of attention sinks and early-token localization**

Prior work (e.g., Wu et al. 2025; Gu et al. 2024) shows that sinks arise because causal masking and residual-stream accumulation make early tokens persistent anchors that later states can always attend to. Our contribution is to show the functional impact. When tasks place uniform long-term retrieval demands on the sequence, the model uses these early anchors to support primacy, whereas tasks emphasizing recent information do not rely on sinks. A full analysis of why sinks localize at early positions remains open, but our results help clarify when and why these structures become behaviorally relevant.

#### Official Review of Submission21588 by Reviewer L5FX

Official Reviewby Reviewer L5FX31 Oct 2025, 07:02 (modified: 12 Nov 2025, 05:04)Everyone

**Summary:**

This paper investigates the "lost-in-the-middle" phenomenon, where Large Language Models (LLMs) often struggle to recall information from the middle of their context window. The authors posit that this U-shaped recall curve is not an inherent architectural flaw but rather an emergent property from training on mixed retrieval objectives. To test this, they train several models (GPT-2 Small/Large, Llama 3.2-1B, RNNs, and T5) from scratch on synthetic memory tasks. They demonstrate that tasks requiring "free recall" tend to produce a primacy effect (good recall at the beginning), while "running span" tasks produce a recency effect (good recall at the end). When trained on a mixture of these objectives, the models exhibit the full U-shaped curve.

**Soundness:** 3: good

**Presentation:** 3: good

**Contribution:** 2: fair

**Strengths:**

**Controlled Experimental Setup:** Training models from scratch on well-defined, synthetic tasks is a significant strength. This methodology provides a clean environment for causal attribution, effectively isolating the training objectives as the primary variable and avoiding the confounding factors of large, diverse pre-training datasets.

**Systematic Ablation Studies:** The paper provides valuable mechanistic insights, particularly through the attention sink dropout experiments. These studies effectively demonstrate how different components (like attention sinks) contribute selectively to different task-driven biases (e.g., primacy).

**Inclusion of Multiple Architectures:** Testing across decoder-only (GPT, Llama), encoder-decoder (T5), and RNN seq2seq models helps to disentangle architectural contributions from training-objective effects, strengthening the paper's claims about the generality of the phenomenon.

**Weaknesses:**

While the paper presents a novel and interesting hypothesis, its conclusions would be strengthened by addressing the following points regarding the generalizability and implications of the findings.

1. Generalizability and Model Scale A key point of tension arises from the Llama 3.2-1B results (Fig 3G, H). These larger, more modern models do not seem to exhibit the same pronounced U-shaped phenomenon observed in the smaller GPT-2 models. This divergence raises crucial questions about the paper's central claim:

Does this suggest the 'lost-in-the-middle' effect, as framed here, is primarily an artifact of limited model capacity rather than a fundamental property of the training objective?

The paper would be significantly strengthened if the authors could elaborate on how their explanation generalizes to modern, more capable architectures that seem to mitigate this issue. If the phenomenon disappears with scale, it suggests the retrieval-objective trade-off may not be the primary bottleneck for today's SOTA models.

2. Situating the Work within Existing Literature The paper would benefit from a more thorough engagement with related literature on positional biases. For instance:

Recent work (e.g., "Transformers need glasses!" \[2406.04267\], "Why do LLMs attend to the first token?" \[2504.02732\]) has also explored primacy and recency effects, attributing them to different mechanisms like "information over-squashing."

Connecting to this adjacent work would help clarify the unique contributions of this paper's retrieval-objective hypothesis versus other explanations.

3. Implications for Modern Architectures The reliance on older architectures like GPT-2 (2019) and RNNs, while valuable for the controlled comparison, makes it difficult to ascertain the implications for current SOTA models.

How do the authors reconcile their findings with models like Gemini 1.5 Pro, which demonstrate near-perfect recall across million-token contexts?

A discussion on this point is essential. Are the mechanisms identified here still at play, but simply overcome by sheer scale? Or do modern architectures (e.g., different positional encodings, data mixtures, and attention mechanisms) fundamentally resolve the retrieval-objective trade-off described in this work?

**Questions:**

To help clarify the paper's contributions, I would encourage the authors to elaborate on the following in a revised version:

1. What are the unique contributions of the mixed-retrieval-objective hypothesis when viewed against prior work on positional biases and information "squashing"?

2. What are the practical implications of these findings? Do the results suggest concrete, recommended changes to LLM architectures or pre-training data mixtures?

3. How does the paper's thesis account for the capability of modern SOTA LLMs (and the paper's own Llama 3.2 results) that seem to largely solve the 'lost-in-the-middle' problem at scale? Is the U-shape a temporary phase of training/scale, or a fundamental trade-off that is simply "solved" by other, more dominant mechanisms in larger models?


**Flag For Ethics Review:** No ethics review needed.

**Rating:** 2: reject, not good enough

**Confidence:** 4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**Code Of Conduct:** Yes

#### Official Comment by Authors

Official Commentby Authors03 Dec 2025, 19:51Everyone

**Comment:**

Thank you for your constructive feedback and insightful questions. We are glad that you find i) our hypothesis “novel”, ii) our model training methods "effective" and providing a “clean environment for causal attribution”, iii) the insights regarding the attention sinks “valuable”, and (iv) our results “generalizable” across architectures. Below we will address your questions in detail.

* * *

### Weaknesses

**Generalizability and Model Scale**

Please refer to Q1. in the General Response.

We have expanded the paper to clarify what the Llama-3.2–1B results imply (L486). Although the 1B model has a flatter SPC, its recall strategy still shifts under different retrieval demands (e.g., its PFR curve changes under the combined task). This indicates that underlying mechanisms remain active, despite optimal recall. We have also added experiments across model scales and longer context lengths. These show a reduction of the U-shape with scale consistent with prior work reporting reduced lost-in-the-middle in larger LLMs (appendix section A.2). This suggests the reduction is not due to the absence of the mechanism, but to larger models compensating for positional biases.

**Explanations for modern architectures**

Please refer to Q3. in the General Response.

Our expanded scale sweep shows that larger models exhibit reduced U-shape but still display the same behavioral shifts under changing retrieval demand (e.g., PFR changes, sink sensitivity). Model scale reduces symptoms, not the underlying interaction between retrieval demands and causal processing (Appendix A.2). We have also expanded the Discussion to include more recent papers (L465). Our results complement these more theoretical works by showing when these architectural tendencies have functional behavioral impact under specific retrieval objectives. One of our central findings is that attention sinks support long-range, but not short-range, retrieval tasks.

**Implications for modern architectures**

In the revision, we added explicit discussion connecting our findings to other recent explanations (L476). Our results show when these biases matter depends on the training objective. Regarding modern systems, we add discussion that high-capacity LLMs can mask positional biases even while the underlying forces remain. Our scale sweep shows that primacy/recency decreases steadily with increasing capacity (appendix A.2). Literature reports that architectural changes, new positional encodings, and diverse training mixtures further mitigate positional bias. These observations suggest that the mechanisms we identify still exist, but their influence is outweighed by scale and design choices in large models. Our minimal tasks clarify why lost-in-the-middle arises and why SOTA systems often do not express it.

* * *

### Questions

**Unique contributions of the mixed-retrieval-objective hypothesis**

Our hypothesis contributes by showing that architectural biases alone do not determine whether a U-shape emerges. Instead, the training objective determines which biases become behaviorally expressed. Our results explain _when_ that early-token influence matters: primacy arises under long-term retrieval demand, recency under short-term demand, and the full U-shape under mixed demands. This framing clarifies why positional effects vary across tasks, architectures, and scales, and provides a basis for predicting mitigation effectiveness. We have added a dedicated discussion addressing this (L466).

**Practical implications**

Our results suggest two practical implications. First, the retrieval demands in the pre-training mixture matter: shifting the balance between long-range and short-range retrieval changes whether primacy, recency, or neither becomes dominant in task performance. This provides a means to anticipate when positional-bias mitigation techniques will help. Second, the analysis highlights which components primarily drive long-range retrieval bias (causal-style attention and sink formation) indicating that positional encodings, attention routing, and model scale can be tuned to reduce reliance on early-token anchors. While we believe that our current results suggest these potential changes, we have added a mention of experiments confirming this to Future Work.

**SOTA performance**

Our view is that the U-shape reflects an interaction between retrieval demands and causal processing, but one that can be overridden by capacity, positional-encoding improvements, and diverse training mixtures. Our Llama-3.2 results illustrate this: the serial-position curve flattens, but the model’s retrieval strategy (e.g., PFR behavior, sink sensitivity) still responds to differing demands. This indicates the mechanism continues to operate, but its behavioral impact is reduced with scale; Modern SOTA systems push this further through scale and architectural refinement. We have added this explanation to the Discussion section.

#### Official Review of Submission21588 by Reviewer Bp4r

Official Reviewby Reviewer Bp4r18 Oct 2025, 18:22 (modified: 12 Nov 2025, 05:04)Everyone

**Summary:**

The paper examines the now well know "lost in the effect" of LLMs and show that the phenomenon originates from training (akin to objectives in psychology) that maximizes recency objectives as well as maximizing some long term objectives using an autoregressive model. The paper shows the effect by first constructing the learning from scratch experiment using synthetic data and later on turn to language modelling real use cases.

The paper is able to notably contribute to the understanding of "primacy" effect and shows that 1) the primacy effect is due to autoregressive training with long term tasks 2) the primacy effect is strongly related to the attention sink phenomenon

**Soundness:** 3: good

**Presentation:** 2: fair

**Contribution:** 3: good

**Strengths:**

Although the hypothesis has been around in the community for a while for the root case of "lost in the middle effect", this is the first paper that I have seen to illustrate the cause clearly convincingly without involving other causal factors where the paper 1) trains from scratch 2) using synthetic almost toy tasks to illustrate this.

The experimental designs are set up nicely in this paper. The paper investigates into if primacy is related to the autoregressive training and examines a positive case (RNN) and a negative case (T5) for this which are well chosen since the architecture is significantly different to be convincing and informative. The attention sink link is built with its own contribution as well.

**Weaknesses:**

I think the organization of the paper can be made better.

In terms of what I want to see more: in the discussion section, the paper mentions quite some related works mitigate the "lost in the middle effect". The paper posits that intervention on positional attention should have more effect when applied to long term tasks; however, the paper does not state which techniques exactly and don't performs experiments and cite related works for if what the paper posits are true. It would be something informative for the readers.

In terms of what I think can be simplified: the paper examines 3 metrics, however, they seem to connect to each other and lag is not very much used in the texts. Furthermore, although it is valuable to examine real cases (3.4); the conclusion is not expected to differ since the settings are very similar and the phenomenon is relatively well known.

**Questions:**

None

**Flag For Ethics Review:** No ethics review needed.

**Rating:** 6: marginally above the acceptance threshold. But would not mind if paper is rejected

**Confidence:** 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**Code Of Conduct:** Yes

#### Official Comment by Authors

Official Commentby Authors03 Dec 2025, 20:01Everyone

**Comment:**

We appreciate your feedback on our work. We’re encouraged that you viewed our paper as “the first to illustrate the root cause of the lost-in-the-middle effect clearly and convincingly,” found the experiment design “nicely set up,” and considered the model architectures “well chosen.” We address your specific points below.

* * *

### Weaknesses

**Connecting Mitigation Strategies to Our Claims**

Thank you for highlighting this; we’ve clarified this point in our revised discussion. Our claim is that mitigation methods that explicitly reshape positional attention (e.g., RoPE rescaling, attention-offsetting, context-reordering, or position-agnostic training) should matter most when the task demands uniform long-range retrieval, because this is when primacy and sink-based mechanisms play a functional role. While a full sweep of mitigation techniques is beyond the revision scope, we now cite the relevant works and pose the confirmation of these potential effects as a possible future work.

**Metric selection and potential simplification**

Thank you for pointing this out. These metrics serve distinct roles in our analysis and are customarily used in the cognitive science literature that informs our fundamental approach. It is true that these metrics connect to one another, but as evidenced in the change of behavior in PFR, but not SPC, for Llama-3.2 1B (L486 in the Discussion), they each serve as important indicators of the model’s underlying behavior. For the masked-sequence experiments, we present this experiment as a bridge to the next-token prediction as a way of confirming that these results can extend to more naturalistic tasks learned by general LLMs.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="persistence-docs-by-langchain.md">
<details>
<summary>Persistence - Docs by LangChain</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://docs.langchain.com/oss/python/langgraph/persistence>

# Persistence - Docs by LangChain

Persistence lets LangGraph applications keep useful information beyond a single graph run. It matters when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions.LangGraph provides two complementary persistence systems:

- **[Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers)** persist a thread’s graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance.
- **[Stores](https://docs.langchain.com/oss/python/langgraph/stores)** persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge.

Most applications can use both: a [checkpointer](https://docs.langchain.com/oss/python/langgraph/checkpointers) tracks the current thread, and a [store](https://docs.langchain.com/oss/python/langgraph/stores) tracks durable information across threads.

## Quickstart

Compile your graph with a checkpointer, a store, or both:

```
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

graph = builder.compile(checkpointer=checkpointer, store=store)

result = graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, my name is Bob."}]},
    {"configurable": {"thread_id": "thread-1"}},
)
```

## Checkpointer vs. store

| | Checkpointer | Store |
| --- | --- | --- |
| Persists | Graph state snapshots | Application-defined key-value data |
| Scope | A single thread | Across threads |
| Memory type | Short-term, thread-scoped memory | Long-term, cross-thread memory |
| Use for | Conversation continuity, human-in-the-loop, time travel, and fault tolerance | User preferences, facts, and shared knowledge |
| Access pattern | Pass a `thread_id` in graph config | Read and write items from nodes or application code |
| Full guide | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | [Stores](https://docs.langchain.com/oss/python/langgraph/stores) |

## Next steps

- [Use checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) to persist and inspect thread state.
- [Use stores](https://docs.langchain.com/oss/python/langgraph/stores) to persist durable data across threads.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="what-is-the-model-context-protocol-mcp-databricks.md">
<details>
<summary>What is the Model Context Protocol (MCP)? | Databricks</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.databricks.com/blog/what-is-model-context-protocol>

# What is the Model Context Protocol (MCP)? | Databricks

Summary

- The Model Context Protocol (MCP) is an open standard that lets AI assistants securely connect to tools, data sources and services through a consistent interface.
- MCP separates how clients like IDEs or chat tools talk to models from how they discover and call external tools, so you can reuse the same integrations across many AI experiences.
- By standardizing how models access context and actions, MCP reduces vendor lock in and makes it easier to build secure, reliable AI applications on platforms such as Databricks.

## Introduction: Understanding the Model Context Protocol

The Model Context Protocol (MCP) is an open standard that enables AI applications to connect seamlessly with external data sources, tools, and systems. Think of the Model Context Protocol as a USB-C port for AI systems—just as a USB-C port standardizes how devices connect to computers, MCP standardizes how AI agents access external resources like databases, APIs, file systems, and knowledge bases.

https://www.databricks.com/sites/default/files/inline-images/image6_25.png

The context protocol addresses a critical challenge in building AI agents: the "N×M integration problem." Without a standardized protocol, each AI application must integrate directly with every external service, creating N×M separate integrations where N represents the number of tools and M represents the number of clients. This approach quickly becomes impossible to scale. The Model Context Protocol MCP solves this by requiring each client and each MCP server to implement the protocol just once, reducing total integrations from N×M to N+M.

By enabling AI systems to access real-time data beyond their LLM's training data, MCP helps AI models provide accurate, up-to-date responses rather than relying solely on static training data from their initial learning phase.

## What Is a Model Context Protocol?

The Model Context Protocol is an open-source, unified standard for interoperability that enables developers to build context-aware AI applications. MCP complements LLMOps by exposing runtime integration, observability, and governance controls that simplify deployment, monitoring, and lifecycle management of LLM applications.

AI applications need access to assets such as local resources, databases, data pipelines (streaming/batch), search engines, calculators, and workflows for prompt conditioning and grounding generation. The context protocol standardizes how applications connect to those assets through a structured way that reduces boilerplate integration code.

The scalability issue means that AI models ( large language models in particular) typically must rely on pre-existing, static data for training. This can lead to inaccurate or outdated responses because models trained on static datasets need additional updates to incorporate new information. By addressing scalability, MCP enables AI applications to be context aware and provide up-to-date outputs that aren't constrained by the limitations of static training data.

## What Is MCP and Why Is It Used?

The Model Context Protocol MCP serves as a standardized way for AI applications to discover and interact with external tools and data sources at runtime. Rather than hardcoding connections to each external service, AI agents using MCP can dynamically discover available tools, understand their capabilities through structured calls, and invoke them with proper tool permissions.

MCP is used because it transforms how AI powered tools access information. Traditional AI systems are limited by their training data, which becomes outdated quickly. The context protocol enables developers to build AI agents that can perform tasks using live data from popular enterprise systems, development environments, and other external sources—all through a single, standardized protocol.

The open protocol also reduces boilerplate integration code. Instead of writing custom connectors for every new integration, developers implement MCP once on both the client and server sides. This approach is particularly valuable for agentic AI systems that need to autonomously discover and use multiple tools across different contexts.

## What Is MCP vs API?

### Traditional API Limitations

Traditional APIs expose endpoints with typed parameters that clients must hardcode and update whenever an API changes. Context stitching becomes the client's responsibility because APIs provide minimal semantic guidance about how returned data should be used. An API request typically follows a simple request-response pattern without maintaining state or context between calls.

### How the Model Context Protocol Differs

MCP defines a different approach from traditional APIs. Rather than hardcoded endpoints, MCP servers expose a machine-readable capability surface discoverable at runtime. AI systems can query available tools, resources, and prompts instead of relying on predefined connections. The Model Context Protocol standardizes resource shapes—documents, database rows, files—reducing serialization complexity so AI models receive relevant context optimized for reasoning.

MCP implementations support bidirectional, stateful communication with streaming semantics. This enables MCP servers to push updates and progress notifications directly into an AI agent's context loop, supporting multi-step workflows and partial results that traditional APIs cannot provide natively. This client-server architecture allows for more sophisticated tool usage patterns in agentic systems.

## MCP Versus RAG: Complementary Approaches

Retrieval-Augmented Generation (RAG) improves AI accuracy by converting documents into embeddings, storing them in vector databases, and retrieving relevant information during generation. However, RAG typically relies on indexed, static sources from content repositories. The Model Context Protocol provides on-demand access to live APIs, databases, and streams, returning authoritative, up-to-date context when freshness matters.

https://www.databricks.com/sites/default/files/inline-images/image9_7.png

Unlike RAG, which mainly returns read-only context, the context protocol separates resources from tools so AI agents can both fetch data and perform tasks on external systems with controlled schemas. MCP addresses broader integration needs—enabling agentic workflows, multi-turn orchestration, runtime capability discovery, and multi-tenant governance—which RAG does not natively provide.

MCP can complement RAG implementations. Organizations can use RAG to index evergreen content for fast retrieval while using the Model Context Protocol for transactional lookups, SQL query execution, and actions requiring the right context from live systems. This hybrid approach provides both speed and accuracy.

## The Value of Standardization in the MCP Ecosystem

As a runtime-discoverable, bidirectional protocol, the Model Context Protocol turns disparate external tools and data into addressable resources and callable actions. A single MCP client can uniformly discover files, database rows, vector snippets, live streams, and API endpoints. Coexisting with indexed RAG caches, MCP offers authoritative, just-in-time lookups and action semantics.

The practical result is fewer bespoke connectors, less custom code, faster integrations, and more reliable agentic systems with proper error handling and audit trails. This standardized way of connecting AI assistants to remote resources accelerates development cycles while maintaining enterprise security controls. The MCP ecosystem benefits from this standardization as more MCP server implementations become available for popular enterprise systems.

## Core MCP Architecture: Understanding the Client-Server Model

The MCP architecture organizes integrations around three key roles—MCP servers, MCP clients, and MCP hosts—connected through persistent communication channels. This client-server architecture enables AI tools to run multi-step, stateful workflows rather than isolated request-response interactions.

### What MCP Servers Do

MCP servers expose data and tools via standardized interfaces and can run in cloud, on-premises, or hybrid environments. Each server publishes a capability surface of named resources, callable tools, prompts, and notification hooks. Resources may include documents, database rows, files, and pipeline outputs.

MCP server implementations use JSON-RPC 2.0 methods and notifications, support streaming for long-running operations, and provide machine-readable discovery through the transport layer. This lets MCP hosts and AI models query capabilities at runtime without requiring predefined knowledge of available tools.

Popular MCP server implementations connect AI systems to external services like Google Drive, Slack, GitHub, and PostgreSQL databases. These MCP servers handle authentication, data retrieval, and tool execution while presenting a consistent interface through the standardized protocol. Each server in the MCP ecosystem can serve multiple clients simultaneously.

### How MCP Clients Function

MCP clients are components within host applications that translate user or model intents into protocol messages. Each client typically maintains a one-to-one connection with an MCP server and manages lifecycle, authentication, and transport details through a structured way.

MCP clients serialize requests as structured calls using JSON-RPC, handle asynchronous notifications and partial streams, and present a unified local API to reduce integration complexity. Multiple clients can operate from the same MCP host, each connecting to different MCP servers simultaneously.

These clients enable AI agents to interact with external data sources without understanding the implementation details of each external service. The client handles all communication protocols, error handling, and retry logic automatically.

### The Role of MCP Hosts

MCP hosts provide the AI application layer that coordinates MCP clients and server capabilities. Examples include Claude Desktop, Claude Code, AI-powered IDEs, and other platforms where AI agents operate. The MCP host aggregates prompts, conversation state, and client responses to orchestrate multi-tool workflows.

The MCP host decides when to call tools, request additional input, or surface notifications. This centralized orchestration enables AI models to work across heterogeneous MCP servers without bespoke per-service code, supporting the MCP ecosystem's goal of universal interoperability in connecting AI assistants to diverse systems.

### Context Flow and Bidirectional Communication

Client-server communication in the Model Context Protocol is bidirectional and message-driven using JSON-RPC 2.0 over the transport layer. MCP clients call methods to fetch resources or invoke tools, while MCP servers return results, stream partial outputs, and send notifications with relevant information.

https://www.databricks.com/sites/default/files/inline-images/image10_4.png

MCP servers can also initiate requests, asking MCP hosts to sample options or elicit user input through function calling mechanisms. This bidirectional capability distinguishes the context protocol from traditional one-way API patterns. MCP's live authoritative lookups complement RAG by supplying just-in-time records with provenance metadata for traceability.

Persistent transports preserve message ordering and enable real-time updates, letting AI systems iterate over intermediate outputs and run agentic loops that make autonomous AI agents possible.

## What Are the Requirements for Model Context Protocol?

### Security Requirements and Threat Protection

MCP implementations must enforce Transport Layer Security (TLS) for remote transports, strict tool permissions, and scoped credentials to protect against security threats. The protocol requires rate limiting and robust input validation via JSON Schema enforcement on both MCP clients and servers to prevent injection attacks and malformed requests.

Audit logging, token rotation, and least-privilege grants are essential requirements for governing long-lived channels. These security measures protect against unauthorized access while preserving the discoverable integration capabilities that the Model Context Protocol enables. Organizations must implement encryption in transit and at rest, masking, and scoped permissions for long-lived MCP channels to ensure data security.

### Infrastructure and System Requirements

Organizations deploying MCP need compute and networking infrastructure that can host large language models, MCP servers, and connected data sources. This includes adequate GPU/CPU capacity, memory, disk I/O, and low-latency network paths between components in the client-server architecture.

Cloud platforms should support elastic scaling of model instances and MCP servers. Teams must define autoscaling policies for concurrent streams and long-running operations. The transport layer should support both local STDIO for embedded components and remote streaming channels like HTTP/SSE or WebSocket for distributed deployments.

### Implementation Requirements for MCP Work

MCP work requires implementing JSON-RPC 2.0 messaging, discovery endpoints, and resource/tool schemas. MCP servers must publish their capabilities in a machine-readable format through the standard protocol. This enables developers to build discovery-based integrations that support tool discovery without hardcoded connections.

Error handling, reconnection strategies, and backpressure management are critical implementation requirements for production reliability. Organizations should implement observability for persistent streams, method latencies, and resource usage using metrics, traces, and logs. Rate limiters, circuit breakers, and quotas protect downstream systems from overload.

## Practical Benefits: Real-Time Data Access and Reduced Hallucination

With the Model Context Protocol, AI models retrieve live records, pipeline outputs, API responses, and files on demand rather than relying solely on cached embeddings or static LLM's training data. This grounds responses in current, authoritative data sources and reduces hallucinations where AI systems generate incorrect information.

Resources returned at query time include provenance metadata such as source IDs and timestamps, enabling MCP hosts to log origins and make outputs traceable. This transparency is crucial when AI agents perform tasks that require auditability in regulated industries. The context protocol ensures relevant context is always available from authoritative external systems.

## Support for Agentic AI Workflows

Because MCP servers publish resources, tools, and prompts through a standardized way, AI models can discover and call services without hardcoded endpoints. The open standard supports server-initiated elicitation and streaming responses from MCP servers, enabling multi-step reasoning, input clarification, and iteration on partial results.

Tools expose JSON Schema-defined inputs/outputs with scoped tool permissions, allowing AI agents to perform controlled actions like creating tickets, executing SQL queries, or running workflows. This autonomous tool discovery, bidirectional interaction, and built-in guardrails provide the foundation for reliable agentic AI across external systems.

The Model Context Protocol MCP explicitly enables agentic workflows that rely on dynamic tool discovery and action primitives to perceive, decide, and act across systems. This makes it possible to build AI agents that operate autonomously while maintaining proper governance controls.

## Simplified Development with Standardized Integrations

The context protocol enables developers to implement a single server surface that MCP hosts and AI models can reuse with consistent discovery and call semantics. This eliminates separate connectors for common services, reducing the engineering effort required to connect AI assistants to new data sources.

Typed resources and JSON Schema reduce custom serialization, validation, and error handling code that would otherwise be necessary. Local STDIO or remote streaming transports let teams choose on-premises, cloud, or hybrid deployments without changing MCP host logic. This flexibility accelerates how teams build AI agents across different development environments.

MCP offers a practical way to standardize integrations once rather than building custom adapters for each new integration. This standardized protocol approach benefits the entire MCP ecosystem as more organizations adopt the standard.

## Increased Automation Potential for Complex Workflows

MCP's persistent, stateful channels enable AI systems to combine lookups, transformations, and side effects across multiple external services in one continuous loop. For long-running operations, MCP servers can stream partial results so AI agents make intermediate decisions, fork workflows, or request human input when needed.

Combining indexed retrieval for evergreen content repositories with the Model Context Protocol's on-demand authoritative lookups supports fast, accurate responses. This hybrid approach maintains governance controls while enabling AI powered tools to access both static knowledge bases and dynamic external data sources.

The context protocol's support for multi-turn orchestration allows agentic systems to handle complex workflows that require coordination across multiple tools and data sources. This automation potential transforms how organizations deploy AI applications in production environments.

## Implementation Best Practices: System Preparation

Validate your infrastructure can support LLM hosting, MCP servers, and connected data sources. Ensure adequate GPU/CPU resources, memory allocation, and network bandwidth for the client-server architecture. Choose cloud platforms that support elastic scaling for concurrent users and define autoscaling policies.

Standardize secure transports using TLS for all remote connections between MCP clients and servers. Document connection lifecycle management, including reconnection strategies and observable stream health metrics. Implement rate limits, circuit breakers, and quotas to protect downstream external systems from overload.

Organizations should standardize streaming channels (HTTP/SSE, WebSocket) plus local STDIO for embedded components. Validate JSON payloads and schema on both server and client to prevent injection attacks and ensure proper error handling throughout the system.

## Leveraging Open-Source Resources in Programming Languages

The MCP ecosystem includes community SDKs in multiple programming languages that accelerate client and server development. These SDKs provide established patterns for JSON-RPC messaging, streaming, and schema validation, eliminating the need to reimplement protocol plumbing.

Developers can reuse existing MCP server implementations for popular enterprise systems and extend them to domain-specific use cases through the open standard. Building simulators that mimic notifications, long-running streams, and error conditions helps teams test agentic systems before production deployment.

Adopt community resources to accelerate MCP work and avoid rebuilding common functionality. These open-source tools enable developers to focus on business logic rather than protocol implementation details.

## Integration Strategy for Production Deployment

Start with high-impact use cases that demonstrate measurable ROI, such as context-aware AI assistants or automated workflows using AI agents. Limit initial tool scopes and tool permissions, collect telemetry and user feedback, then expand capabilities after stabilizing core functionality.

https://www.databricks.com/sites/default/files/inline-images/image4_54.png

Balance latency and freshness by combining MCP's live lookups with RAG for large static corpora from content repositories. Define SLAs, audit trails, and escalation procedures before broad production rollout. This phased approach reduces risk while building organizational confidence in agentic AI deployments.

MCP addresses the need for structured integration plans that scale as more MCP servers and clients are added to the ecosystem. Organizations should document their integration architecture and governance policies early in the deployment process.

## Common Misconceptions: MCP Is Not Just Another API Framework

**Reality:** The Model Context Protocol standardizes protocol-level integration with persistent context management and dynamic capability discovery. Unlike REST or RPC calls, MCP defines how AI agents discover capabilities, subscribe to streams, and maintain contextual state across interactions through the standard protocol.

This standardized protocol means you can build tools once and expose them uniformly to multiple AI agents and model providers through the MCP ecosystem. Rather than treating model context as an ephemeral payload, the context protocol addresses context as a first-class, versioned resource with proper lifecycle management.

## Tools and Agents Are Different Components

**Reality:** Tools are discrete capabilities exposed through MCP servers—such as database access, file operations, or API integrations. AI agents are decision-making computer programs that discover, orchestrate, and invoke those available tools to perform tasks autonomously.

The context protocol enables AI agents to discover tool metadata dynamically, invoke tool interfaces safely with function calling semantics, and integrate outputs into conversations through MCP clients. This separation allows different agentic systems to use the same catalog of tools while tool owners update interfaces independently of agent logic.

## MCP Manages Comprehensive Data Connectivity

**Reality:** The Model Context Protocol manages comprehensive connectivity to external data sources beyond simple tool usage. It supports streaming notifications, authenticated access to content repositories and vector stores, and consistent semantics for long-running operations and error handling.

MCP offers a practical way to unify access to local resources, remote resources, live data queries, and operational actions through a structured way. This unified approach helps governance, observability, and access control scale alongside AI capabilities in enterprise environments. The context protocol handles other tools and external services through a consistent interface.

## Future Research Directions and Evolution

As the open standard matures, future research directions include enhanced security frameworks for multi-tenant deployments, improved streaming semantics for complex agentic workflows, and standardized patterns for integrating with additional programming languages and development environments.

https://www.databricks.com/sites/default/files/inline-images/image1_87.png

The growing MCP ecosystem continues to expand with new MCP server implementations for emerging external tools and platforms. Community contributions to SDKs, adapters, and reference architectures accelerate adoption while maintaining the protocol's core goal: enabling any AI application to connect with any external service through a standardized way.

Organizations exploring the Model Context Protocol should monitor ecosystem developments, contribute to MCP implementations, and participate in working groups shaping how connecting AI assistants to external systems evolves. This collaborative approach ensures MCP implementations remain interoperable as AI systems and external services continue to advance. Future research directions will likely focus on expanding the protocol's capabilities while maintaining its core simplicity.

## Conclusion: The Model Context Protocol as Foundation for Modern AI

The Model Context Protocol represents a fundamental shift in how AI applications access external data sources and tools. By providing an open protocol for discovery-based integration, the context protocol enables developers to build context-aware AI agents that can perform tasks using live data from popular enterprise systems without extensive boilerplate integration code.

The standardized protocol reduces complexity through the client-server architecture, accelerates development cycles, and enables AI systems to move beyond the limitations of static LLM's training data. Through its bidirectional communication between MCP clients and MCP servers, and support for agentic AI workflows, the Model Context Protocol MCP establishes the foundation for more capable, autonomous AI tools across diverse environments.

As the MCP ecosystem grows with new MCP server implementations and integrations, organizations can build sophisticated AI agents that discover and orchestrate multiple external services while maintaining proper tool permissions, security controls, and audit trails. This standardized approach to connecting AI systems with external tools and data sources will continue shaping how enterprises deploy production AI applications. The context protocol provides the essential infrastructure that enables developers to build next-generation AI applications with confidence.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>API Pricing</summary>

# API Pricing

**Source URL:** <https://openai.com/api/pricing/>

[Contact sales](https://openai.com/contact-sales/)

## Flagship models

Our frontier models are designed to spend more time thinking before producing a response, making them ideal for complex, multi-step problems.

Choose your processing mode

Standard Batch -50%Data residency +10%

## GPT-5.5

A new class of intelligence for coding and professional work.

### Price

Input:

$5.00 / 1M tokens

Cached input:

$0.50 / 1M tokens

Output:

$30.00 / 1M tokens

## GPT-5.4

A more affordable model for coding and professional work.

### Price

Input:

$2.50 / 1M tokens

Cached input:

$0.25 / 1M tokens

Output:

$15.00 / 1M tokens

## GPT-5.4 mini

Our strongest mini model yet for coding, computer use, and subagents.

### Price

Input:

$0.75 / 1M tokens

Cached input:

$0.075 / 1M tokens

Output:

$4.50 / 1M tokens

Pricing above reflects standard processing rates for context lengths under 270K.

Learn more about [Batch Processing⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/batch) and [Data residency & Regional Processing⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data#how-does-data-residency-work)

*   [Explore detailed pricing(opens in a new window)](https://developers.openai.com/api/docs/pricing)

### Multimodal models

Power applications across text, image, and audio with models built for real-time interaction and rich media generation.

## GPT-Realtime-2

Our most capable model for realtime voice interactions.

### Price

Audio:

$32.00 / 1M tokens for inputs

$0.40 / 1M tokens for cached inputs

$64.00 / 1M tokens for outputs

Text:

$4.00 / 1M tokens for inputs

$0.40 / 1M tokens for cached inputs

$24.00 / 1M tokens for outputs

Image:

$5.00 / 1M tokens for inputs

$0.50 / 1M tokens for cached inputs

## GPT-Realtime-Translate

A new live translation model that translates speech in real time and keeps pace with the speaker.

### Price

$0.034 per minute / $0.00057 per second

## GPT-Realtime-Whisper

A new streaming speech-to-text that transcribes speech live as the speaker talks.

### Price

$0.017 per minute / $0.00028 per second

## GPT-Image-2

State-of-the-art image generation model.

### Price

Image:

$8.00 / 1M tokens for inputs

$2.00 / 1M tokens for cached inputs

$30.00 / 1M tokens for outputs

Text:

$5.00 / 1M tokens for inputs

$1.25 / 1M tokens for cached inputs

### Tools

Extend model capabilities with built-in tools for retrieval, execution, and external data access.

## Web search

Retrieve up-to-date information from the web to ground model responses.

### Price

$10.00 / 1k calls

Search content tokens are free.

## Containers

Run code and tools in secure, scalable environments alongside your models.

### Price

Now:

1 GB for $0.03 / 64GB for $1.92 per container

Starting March 31, 2026:

1 GB for $0.03 / 64GB for $1.92 per 20-minute session per container

### Service tiers

Balance performance, predictable costs, and availability based on your needs.

![Image 1: Stack icon](https://images.ctfassets.net/kftzwdyauwt9/63IFaqEsuiZRkZCc13Tork/a68b9165722e9f97d85dd644617f532f/stack.svg?w=3840&q=90)

#### Batch API

Save 50% on inputs and outputs with the Batch API and run tasks asynchronously over 24 hours.

[Learn more(opens in a new window)](https://platform.openai.com/docs/guides/batch)

![Image 2: Timer icon](https://images.ctfassets.net/kftzwdyauwt9/1Z5wlpPLNklcKRQYA1eZ6H/1974956da475b28cfb5e340a5313eff3/timer.svg?w=3840&q=90)

#### Priority processing

Offers reliable, high-speed performance with the flexibility to pay-as-you-go.

[Learn more(opens in a new window)](https://openai.com/api-priority-processing)

![Image 3: Arrow up and down icon](https://images.ctfassets.net/kftzwdyauwt9/6Sv3BxS2Sseug7quNfVRwD/cf9ec80df211cc8905bd4c7ac3d73ef2/arrow-down-arrow-up.svg?w=3840&q=90)

#### Flex processing

Provides lower costs for requests in exchange for slower response times and occasional resource unavailability. Ideal for non-production or lower priority tasks.

[Learn more(opens in a new window)](https://developers.openai.com/api/docs/guides/flex-processing)

### Enterprise offerings

Contact our sales team to learn more about [**Data residency**⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/your-data#data-residency-controls), [**Scale Tier**⁠](https://openai.com/api-scale-tier/)**and**[**Reserved Capacity**⁠](https://openai.com/reserved-capacity/) designed for cutting-edge customers running larger workloads.

*   [Contact sales](https://openai.com/contact-sales/)

### FAQ

### Which model should I use?

We recommend that developers use our large and mini GPT models for everyday tasks. Our large GPT models generally perform better on a wide range of tasks, while our mini GPT models are fast and inexpensive for simpler tasks.

Our large and mini reasoning models are ideal for complex, multi-step tasks and STEM use cases that require deep thinking about tough problems. You can choose the mini reasoning model if you're looking for a faster, more inexpensive option.

We recommend experimenting with all of these models in the [Playground⁠⁠(opens in a new window)](https://platform.openai.com/playground) to explore which models provide the best price performance trade-off for your usage.

### Do you offer an enterprise package or SLAs?

We offer different tiers of access to our enterprise customers that include SLAs, lower latency, and more. Please [contact our sales team⁠](https://openai.com/contact-sales/) to learn more.

### Will I be charged for API usage in the Playground?

Yes, we treat Playground usage the same as regular API usage. You will be billed at the per-token input and output prices mentioned above.

### How will I know how many tokens I’ve used each month?

A token is a mathematical representation of natural language. Log in to your account to view your [usage tracking dashboard⁠(opens in a new window)](https://platform.openai.com/account/usage). This dashboard will show you how many tokens you’ve used during the current and past billing cycles.

### How can I manage my spending on the API platform?

You can set a monthly budget in [your billing settings⁠⁠(opens in a new window)](https://platform.openai.com/settings/organization/limits), after which we’ll stop serving your requests. There may be a delay in enforcing the limit, and you are responsible for any overage incurred. You can also configure an email notification threshold to receive an email alert once you cross that threshold each month. We recommend checking your [usage tracking dashboard⁠(opens in a new window)](https://platform.openai.com/account/usage) regularly to monitor your spend.

For customers managing work with Projects, you can [set and manage billing restrictions per project⁠(opens in a new window)](https://help.openai.com/en/articles/9186755-managing-your-work-in-the-api-platform-with-projects)⁠ in the Dashboard.

### Is access to the API included in ChatGPT Plus, Business, Enterprise or Edu?

No, OpenAI APIs are billed separately from ChatGPT Plus, Business, Enterprise and Edu. ChatGPT subscription pricing can be found at [openai.com/chatgpt/pricing/⁠](https://openai.com/chatgpt/pricing/).

### How is pricing calculated for images?

Images are converted into tokens and charged per token. Text models price image tokens at standard text token rates, while GPT Image and gpt-realtime uses a separate image token rate. Models like gpt-4.1-mini, gpt-4.1-nano, and o4-mini convert images into tokens differently. [Learn more in our docs⁠(opens in a new window)](https://platform.openai.com/docs/guides/images-vision?api-mode=chat#calculating-costs).

Pricing calculator

Set model

 

Set width

px

 

by

Set height

px

 

=$0.000263

- [x] 

Low resolution 

=$0.000263

Price per 1M tokens (fixed)$1.25
512 × 512 tiles 1 × 1
Total tiles 1
Base tokens 70
Tile tokens 140 × 1 = 140
Total tokens 210
Total price$0.000263

</details>

<details>
<summary>Extended thinking & interleaved thinking docs</summary>

# Extended thinking & interleaved thinking docs

**Source URL:** <https://docs.claude.com/en/docs/build-with-claude/extended-thinking>

This feature is eligible for [Zero Data Retention (ZDR)](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

Extended thinking gives Claude enhanced reasoning capabilities for complex tasks, while providing varying levels of transparency into its step-by-step thought process before it delivers its final answer.

On `claude-fable-5` and `claude-mythos-5`, extended thinking is always enabled and cannot be disabled. Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported; use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) instead. Adaptive thinking is always on, and `thinking: {type: "disabled"}` returns an error.

For Claude Opus 4.8 and Claude Opus 4.7, set `thinking: {type: "adaptive"}` to enable [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) and use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth. On both models, manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is not supported and returns a 400 error. With adaptive thinking, the model decides when and how much to think based on each request, so it triggers thinking only as needed. For Claude Opus 4.6 and Claude Sonnet 4.6, adaptive thinking is also recommended; the manual configuration is still functional on these models but is deprecated and will be removed in a future model release.

## Supported models

Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is supported on all current Claude models **except Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, and Claude Opus 4.7**, where it is not accepted and returns a 400 error. A few models have mode-specific behavior:

- **Claude Fable 5 (`claude-fable-5`) and Claude Mythos 5 (`claude-mythos-5`):** manual extended thinking is not supported and returns a 400 error. [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) is always on; use the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth.
- **Claude Opus 4.8 (claude-opus-4-8):** manual extended thinking is not supported and returns a 400 error. Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`) with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) instead. The model determines whether and how much to use extended thinking based on each request.
- **Claude Opus 4.7 (claude-opus-4-7):** manual extended thinking is no longer supported. Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (`thinking: {type: "adaptive"}`) with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) instead.
- **[Claude Mythos Preview](https://anthropic.com/glasswing):** [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) is the default; `thinking: {type: "enabled", budget_tokens: N}` is also accepted. `thinking: {type: "disabled"}` is not supported, and `display` defaults to `"omitted"` rather than returning thinking content. Pass `display: "summarized"` to receive summaries.
- **Claude Opus 4.6 (claude-opus-4-6):** [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) recommended; manual mode (`type: "enabled"`) is deprecated but still functional.
- **Claude Sonnet 4.6 (claude-sonnet-4-6):** [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) recommended; manual mode (`type: "enabled"`) with [interleaved mode](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking) is deprecated but still functional.

Thinking behavior differs across Claude model versions. See [Differences in thinking across model versions](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#differences-in-thinking-across-model-versions) for details.

## How extended thinking works

When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. Claude incorporates insights from this reasoning before crafting a final response.

The API response includes `thinking` content blocks, followed by `text` content blocks.

Here's an example of the default response format:

```
{
  "content": [\
    {\
      "type": "thinking",\
      "thinking": "Let me analyze this step by step...",\
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."\
    },\
    {\
      "type": "text",\
      "text": "Based on my analysis..."\
    }\
  ]
}
```

For more information about the response format of extended thinking, see the [Messages API Reference](https://platform.claude.com/docs/en/api/messages/create).

## How to use extended thinking

Here is an example of using extended thinking in the Messages API:

```
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[\
        {\
            "role": "user",\
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",\
        }\
    ],
)

# The response contains summarized thinking blocks and text blocks
for block in response.content:
    if block.type == "thinking":
        print(f"\nThinking summary: {block.thinking}")
    elif block.type == "text":
        print(f"\nResponse: {block.text}")
```

To turn on extended thinking, add a `thinking` object, with the `type` parameter set to `enabled` and the `budget_tokens` to a specified token budget for extended thinking. For Claude Opus 4.6 and Claude Sonnet 4.6, use `type: "adaptive"` instead. See [Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) for details. While `type: "enabled"` with `budget_tokens` is still functional on these models, it is deprecated and will be removed in a future release.

The `budget_tokens` parameter determines the maximum number of tokens Claude is allowed to use for its internal reasoning process. This limit applies to full thinking tokens, not to [the summarized output](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking). Larger budgets can improve response quality by enabling more thorough analysis for complex problems, although Claude may not use the entire budget allocated, especially at ranges above 32k.

`budget_tokens` is [deprecated](https://platform.claude.com/docs/en/build-with-claude/overview#feature-availability) on Claude Opus 4.6 and Claude Sonnet 4.6 and will be removed in a future model release. Use [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) with the [effort parameter](https://platform.claude.com/docs/en/build-with-claude/effort) to control thinking depth instead.

[Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6 support up to 128k output tokens. Claude Sonnet 4.6 and Claude Haiku 4.5 support up to 64k. See the [models overview](https://platform.claude.com/docs/en/about-claude/models/overview) for limits on legacy models. On the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing#extended-output-beta), the `output-300k-2026-03-24` [beta header](https://platform.claude.com/docs/en/api/beta-headers) raises the output limit to 300k for Claude Opus 4.8, Opus 4.7, Opus 4.6, and Sonnet 4.6.

`budget_tokens` must be set to a value less than `max_tokens`. However, when using [interleaved thinking with tools](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking), you can exceed this limit as the token limit becomes your entire context window. Because `budget_tokens` must be less than `max_tokens`, extended thinking cannot be combined with `max_tokens: 0` ( [cache pre-warming](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#pre-warming-the-cache)).

### Summarized thinking

With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse. This is the default behavior on Claude 4 models when the `display` field on the thinking configuration is unset or set to `"summarized"`. On Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing), `display` defaults to `"omitted"` instead, so you must set `display: "summarized"` explicitly to receive summarized thinking.

Here are some important considerations for summarized thinking:

- You're charged for the full thinking tokens generated by the original request, not the summary tokens.
- The billed output token count will **not match** the count of tokens you see in the response.
- On Claude 4 models, the first few lines of thinking output are more verbose, providing detailed reasoning that's particularly helpful for prompt engineering purposes. [Claude Mythos Preview](https://anthropic.com/glasswing) summarizes from the first token, so its thinking blocks do not show this verbose preamble.
- As Anthropic seeks to improve the extended thinking feature, summarization behavior is subject to change.
- Summarization preserves the key ideas of Claude's thinking process with minimal added latency, enabling a streamable user experience.
- Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

In rare cases where you need access to full thinking output for Claude 4 models, [contact Anthropic sales](https://platform.claude.com/cdn-cgi/l/email-protection#96e5f7faf3e5d6f7f8e2fee4f9e6fff5b8f5f9fb).

### Controlling thinking display

The `display` field on the thinking configuration controls how thinking content is returned in API responses. It accepts two values:

- `"summarized"`: Thinking blocks contain summarized thinking text. See [Summarized thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#summarized-thinking) for details. This is the default on Claude Opus 4.6, Claude Sonnet 4.6, and earlier Claude 4 models.
- `"omitted"`: Thinking blocks are returned with an empty `thinking` field. The `signature` field still carries the encrypted full thinking for multi-turn continuity (see [Thinking encryption](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#thinking-encryption)). This is the default on Claude Fable 5, Claude Mythos 5, Claude Opus 4.8, Claude Opus 4.7, and [Claude Mythos Preview](https://anthropic.com/glasswing).

Setting `display: "omitted"` is useful when your application doesn't surface thinking content to users. The primary benefit is **faster time-to-first-text-token when streaming:** The server skips streaming thinking tokens entirely and delivers only the signature, so the final text response begins streaming sooner.

Here are some important considerations for omitted thinking:

- You're still charged for the full thinking tokens. Omitting reduces latency, not cost.
- If you pass thinking blocks back in multi-turn conversations, pass them unchanged. The server decrypts the `signature` to reconstruct the original thinking for prompt construction (see [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#preserving-thinking-blocks)). Any text you place in the `thinking` field of a round-tripped omitted block is ignored.
- `display` is invalid with `thinking.type: "disabled"` (there is nothing to display).
- When using `thinking.type: "adaptive"` and the model skips thinking for a simple request, no thinking block is produced regardless of `display`.

The `signature` field is identical whether `display` is `"summarized"` or `"omitted"`. Switching `display` values between turns in a conversation is supported.

On [Claude Mythos Preview](https://anthropic.com/glasswing), `display` defaults to `"omitted"`. The examples in this section pass `display` explicitly so they apply to all models, but on Mythos Preview you can leave it unset and receive the same behavior. To receive summarized thinking on Mythos Preview, set `display: "summarized"` explicitly.

Automated pipelines that never surface thinking content to end users can skip the overhead of receiving thinking tokens over the wire. Latency-sensitive applications get the same reasoning quality without waiting for thinking text to stream before the final response begins.

```
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000,
        "display": "omitted",
    },
    messages=[\
        {"role": "user", "content": "What is 27 * 453?"},\
    ],
)

for block in response.content:
    if block.type == "thinking":
        if block.thinking:
            print(f"Thinking: {block.thinking}")
        else:
            print("Thinking: [omitted]")
    elif block.type == "text":
        print(f"Response: {block.text}")
```

When `display: "omitted"` is set, the response contains `thinking` blocks with an empty `thinking` field:

Output

```
{
  "content": [\
    {\
      "type": "thinking",\
      "thinking": "",\
      "signature": "EosnCkYICxIMMb3LzNrMu..."\
    },\
    {\
      "type": "text",\
      "text": "The answer is 12,231."\
    }\
  ]
}
```

When streaming with `display: "omitted"`, no `thinking_delta` events are emitted; see [Streaming thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#streaming-thinking) below for the event sequence.

### Streaming thinking

You can stream extended thinking responses using [server-sent events (SSE)](https://developer.mozilla.org/en-US/Web/API/Server-sent%5Fevents/Using%5Fserver-sent%5Fevents).

When streaming is enabled for extended thinking, you receive thinking content via `thinking_delta` events.

When `display: "omitted"` is set, no `thinking_delta` events are emitted. See [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#controlling-thinking-display).

For more documentation on streaming via the Messages API, see [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming).

Here's how to handle streaming with thinking:

```
client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[\
        {\
            "role": "user",\
            "content": "What is the greatest common divisor of 1071 and 462?",\
        }\
    ],
) as stream:
    thinking_started = False
    response_started = False

    for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
            # Reset flags for each new block
            thinking_started = False
            response_started = False
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                if not thinking_started:
                    print("Thinking: ", end="", flush=True)
                    thinking_started = True
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                if not response_started:
                    print("Response: ", end="", flush=True)
                    response_started = True
                print(event.delta.text, end="", flush=True)
        elif event.type == "content_block_stop":
            print("\nBlock complete.")
```

Example streaming output:

Output

```
event: message_start
data: {"type": "message_start", "message": {"id": "msg_01...", "type": "message", "role": "assistant", "content": [], "model": "claude-sonnet-4-6", "stop_reason": null, "stop_sequence": null}}

event: content_block_start
data: {"type": "content_block_start", "index": 0, "content_block": {"type": "thinking", "thinking": "", "signature": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "I need to find the GCD of 1071 and 462 using the Euclidean algorithm.\n\n1071 = 2 × 462 + 147"}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "thinking_delta", "thinking": "\n462 = 3 × 147 + 21\n147 = 7 × 21 + 0\n\nSo GCD(1071, 462) = 21"}}

// Additional thinking deltas...

event: content_block_delta
data: {"type": "content_block_delta", "index": 0, "delta": {"type": "signature_delta", "signature": "EqQBCgIYAhIM1gbcDa9GJwZA2b3hGgxBdjrkzLoky3dl1pkiMOYds..."}}

event: content_block_stop
data: {"type": "content_block_stop", "index": 0}

event: content_block_start
data: {"type": "content_block_start", "index": 1, "content_block": {"type": "text", "text": ""}}

event: content_block_delta
data: {"type": "content_block_delta", "index": 1, "delta": {"type": "text_delta", "text": "The greatest common divisor of 1071 and 462 is **21**."}}

// Additional text deltas...

event: content_block_stop
data: {"type": "content_block_stop", "index": 1}

event: message_delta
data: {"type": "message_delta", "delta": {"stop_reason": "end_turn", "stop_sequence": null}}

event: message_stop
data: {"type": "message_stop"}
```

When `display: "omitted"` is set, the thinking block opens, a single `signature_delta` arrives, and the block closes without any `thinking_delta` events. Text streaming begins immediately after:

Output

```
event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"thinking","thinking":"","signature":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"signature_delta","signature":"EosnCkYICxIMMb3LzNrMu..."}}

event: content_block_stop
data: {"type":"content_block_stop","index":0}

event: content_block_start
data: {"type":"content_block_start","index":1,"content_block":{"type":"text","text":""}}
```

When using streaming with thinking enabled, you might notice that text sometimes arrives in larger chunks alternating with smaller, token-by-token delivery. This is expected behavior, especially for thinking content.

The streaming system needs to process content in batches for optimal performance, which can result in this "chunky" delivery pattern, with possible delays between streaming events.

## Extended thinking with tool use

Extended thinking can be used alongside [tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), allowing Claude to reason through tool selection and results processing.

When using extended thinking with tool use, be aware of the following limitations:

1.  **Tool choice limitation**: Tool use with thinking only supports `tool_choice: {"type": "auto"}` (the default) or `tool_choice: {"type": "none"}`. Using `tool_choice: {"type": "any"}` or `tool_choice: {"type": "tool", "name": "..."}` will result in an error because these options force tool use, which is incompatible with extended thinking.

2.  **Preserving thinking blocks**: During tool use, you must pass `thinking` blocks back to the API for the last assistant message. Include the complete unmodified block back to the API to maintain reasoning continuity.

### Toggling thinking modes in conversations

You can't toggle thinking in the middle of an assistant turn, including during tool use loops. The entire assistant turn should operate in a single thinking mode:

-   **If thinking is enabled**, the final assistant turn should start with a thinking block.
-   **If thinking is disabled**, the final assistant turn shouldn't contain any thinking blocks

From the model's perspective, **tool use loops are part of the assistant turn**. An assistant turn doesn't complete until Claude finishes its full response, which may include multiple tool calls and results.

For example, this sequence is all part of a **single assistant turn**:

```
User: "What's the weather in Paris?"
Assistant: [thinking] + [tool_use: get_weather]
User: [tool_result: "20°C, sunny"]
Assistant: [text: "The weather in Paris is 20°C and sunny"]
```

Even though there are multiple API messages, the tool use loop is conceptually part of one continuous assistant response.

#### Graceful thinking degradation

When a mid-turn thinking conflict occurs (such as toggling thinking on or off during a tool use loop), the API automatically disables thinking for that request. To preserve model quality and remain on-distribution, the API may:

-   Strip thinking blocks from the conversation when they would create an invalid turn structure
-   Disable thinking for the current request when the conversation history is incompatible with thinking being enabled

This means that attempting to toggle thinking mid-turn won't cause an error, but thinking will be silently disabled for that request. To confirm whether thinking was active, check for the presence of `thinking` blocks in the response.

#### Practical guidance

**Best practice**: Plan your thinking strategy at the start of each turn rather than trying to toggle mid-turn.

**Example: Toggling thinking after completing a turn**

```
User: "What's the weather?"
Assistant: [tool_use] (thinking disabled)
User: [tool_result]
Assistant: [text: "It's sunny"]
User: "What about tomorrow?"
Assistant: [thinking] + [text: "..."] (thinking enabled - new turn)
```

By completing the assistant turn before toggling thinking, you ensure that thinking is actually enabled for the new request.

Toggling thinking modes also invalidates prompt caching for message history. For more details, see the [Extended thinking with prompt caching](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-prompt-caching) section.

### Example: Passing thinking blocks with tool results

### Preserving thinking blocks

During tool use, you must pass `thinking` blocks back to the API, and you must include the complete unmodified block back to the API. This is critical for maintaining the model's reasoning flow and conversation integrity.

While you can omit `thinking` blocks from prior `assistant` role turns, always pass back all thinking blocks to the API for any multi-turn conversation. The API:

-   Automatically filters the provided thinking blocks
-   Uses the relevant thinking blocks necessary to preserve the model's reasoning
-   Only bills for the input tokens for the blocks shown to Claude

Which blocks are kept depends on the model. See [Thinking block preservation by model](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#thinking-block-preservation-in-claude-opus-45-and-later) for the per-class defaults. To override the default, use the [`clear_thinking_20251015` context-editing strategy](https://platform.claude.com/docs/en/build-with-claude/context-editing#thinking-block-clearing).

When toggling thinking modes during a conversation, remember that the entire assistant turn (including tool use loops) must operate in a single thinking mode. For more details, see [Toggling thinking modes in conversations](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#toggling-thinking-modes-in-conversations).

When Claude invokes tools, it is pausing its construction of a response to await external information. When tool results are returned, Claude continues building that existing response. This necessitates preserving thinking blocks during tool use, for a couple of reasons:

1.  **Reasoning continuity**: The thinking blocks capture Claude's step-by-step reasoning that led to tool requests. When you post tool results, including the original thinking ensures Claude can continue its reasoning from where it left off.

2.  **Context maintenance**: While tool results appear as user messages in the API structure, they're part of a continuous reasoning flow. Preserving thinking blocks maintains this conceptual flow across multiple API calls. For more information on context management, see the [guide on context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows).

**Important**: When providing `thinking` blocks, the entire sequence of consecutive `thinking` blocks must match the outputs generated by the model during the original request; you can't rearrange or modify the sequence of these blocks.

If thinking blocks are modified, the API returns a 400 `invalid_request_error` whose message contains ```thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified``. The most common cause is application code that filters content blocks by type and drops `redacted_thinking` blocks, or that rebuilds the assistant message instead of echoing it. See [Thinking blocks cannot be modified](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified) for the full error and fix steps.

### Interleaved thinking

Extended thinking with tool use in Claude 4 models supports interleaved thinking, which enables Claude to think between tool calls and make more sophisticated reasoning after receiving tool results.

With interleaved thinking, Claude can:

-   Reason about the results of a tool call before deciding what to do next
-   Chain multiple tool calls with reasoning steps in between
-   Make more nuanced decisions based on intermediate results

**Model support:**

-   **Claude Opus 4.8**: Interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (the only supported thinking mode on Claude Opus 4.8). No beta header is needed.
-   **[Claude Mythos Preview](https://anthropic.com/glasswing)**: Interleaved thinking happens automatically. Every inter-tool reasoning step moves into a thinking block instead of plain text, and thinking blocks are preserved across turns by default. No beta header is needed or supported.
-   **Claude Opus 4.7**: Interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (the only supported thinking mode on Opus 4.7). No beta header is needed.
-   **Claude Opus 4.6**: Interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking). No beta header is needed. The `interleaved-thinking-2025-05-14` beta header is **deprecated** on Opus 4.6 and is safely ignored if included.
-   **Claude Sonnet 4.6**: Interleaved thinking is automatically enabled when using [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) (recommended). The `interleaved-thinking-2025-05-14` beta header with manual extended thinking (`thinking: {type: "enabled"}`) is still functional but deprecated.
-   **Other Claude 4 models** (Opus 4.5, Opus 4.1 (deprecated), Opus 4 (deprecated), Sonnet 4.5, Sonnet 4 (deprecated)): Add [the beta header](https://platform.claude.com/docs/en/api/beta-headers)`interleaved-thinking-2025-05-14` to your API request to enable interleaved thinking.

Here are some important considerations for interleaved thinking:

-   With interleaved thinking, the `budget_tokens` can exceed the `max_tokens` parameter, as it represents the total budget across all thinking blocks within one assistant turn.
-   Interleaved thinking is only supported for [tools used via the Messages API](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
-   The Claude API and [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) accept `interleaved-thinking-2025-05-14` in requests to any model without returning an error. On models that don't support interleaved thinking, the header is ignored. On Claude Opus 4.8, Claude Opus 4.7, and Claude Opus 4.6, it's deprecated and safely ignored. On Claude Mythos Preview, it's not needed and safely ignored.
-   On partner-operated platforms (for example, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock) and [Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)), if you pass `interleaved-thinking-2025-05-14` to any model aside from Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5, Claude Opus 4.1 (deprecated), Opus 4 (deprecated), Sonnet 4.5, or Sonnet 4 (deprecated), your request will fail.

### Tool use without interleaved thinking

### Tool use with interleaved thinking

## Extended thinking with prompt caching

[Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) with thinking has several important considerations:

Extended thinking tasks often take longer than 5 minutes to complete. Consider using the [1-hour cache duration](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#1-hour-cache-duration) to maintain cache hits across longer thinking sessions and multi-step workflows.

**Thinking block context removal**

-   On earlier Opus/Sonnet models and all Haiku models, thinking blocks from previous turns are removed from context, which can affect cache breakpoints. On Opus 4.5+ and Sonnet 4.6+, they are kept by default.
-   When continuing conversations with tool use, thinking blocks are cached and count as input tokens when read from cache
-   This creates a tradeoff: while thinking blocks don't consume context window space visually, they still count toward your input token usage when cached
-   If thinking becomes disabled and you pass thinking content in the current tool use turn, the thinking content will be stripped and thinking will remain disabled for that request

**Cache invalidation patterns**

-   Changes to thinking parameters (enabled/disabled or budget allocation) invalidate message cache breakpoints
-   [Interleaved thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking) amplifies cache invalidation, as thinking blocks can occur between multiple [tool calls](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use)
-   System prompts and tools remain cached despite thinking parameter changes or block removal

On earlier Opus/Sonnet models and all Haiku models, thinking blocks are removed for caching and context calculations; on Opus 4.5+ and Sonnet 4.6+, they are kept by default. In either case, they must be preserved when continuing conversations with [tool use](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use), especially with [interleaved thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking).

### Understanding thinking block caching behavior

When using extended thinking with tool use, thinking blocks exhibit specific caching behavior that affects token counting:

**How it works:**

1.  Caching only occurs when you make a subsequent request that includes tool results
2.  When the subsequent request is made, the previous conversation history (including thinking blocks) can be cached
3.  These cached thinking blocks count as input tokens in your usage metrics when read from the cache
4.  When a non-tool-result user block is included: on Opus 4.5+ and Sonnet 4.6+, previous thinking blocks are kept; on earlier Opus/Sonnet models and all Haiku models, all previous thinking blocks are ignored and stripped from context

**Detailed example flow:**

**Request 1:**

```
User: "What's the weather in Paris?"
```

**Response 1:**

```
[thinking_block_1] + [tool_use block 1]
```

**Request 2:**

```
User: ["What's the weather in Paris?"],
Assistant: [thinking_block_1] + [tool_use block 1],
User: [tool_result_1, cache=True]
```

**Response 2:**

```
[thinking_block_2] + [text block 2]
```

Request 2 writes a cache of the request content (not the response). The cache includes the original user message, the first thinking block, tool use block, and the tool result.

**Request 3:**

```
User: ["What's the weather in Paris?"],
Assistant: [thinking_block_1] + [tool_use block 1],
User: [tool_result_1, cache=True],
Assistant: [thinking_block_2] + [text block 2],
User: [Text response, cache=True]
```

For Opus 4.5+ and Sonnet 4.6+, all previous thinking blocks are kept by default. For earlier Opus/Sonnet models and all Haiku models, because a non-tool-result user block was included, all previous thinking blocks are ignored and stripped from context. This request will be processed the same as:

```
User: ["What's the weather in Paris?"],
Assistant: [tool_use block 1],
User: [tool_result_1, cache=True],
Assistant: [text block 2],
User: [Text response, cache=True]
```

**Key points:**

-   This caching behavior happens automatically, even without explicit `cache_control` markers
-   This behavior is consistent whether using regular thinking or interleaved thinking

### System prompt caching (preserved when thinking changes)

### Messages caching (invalidated when thinking changes)

## Max tokens and context window size with extended thinking

`max_tokens` (which includes your thinking budget when thinking is enabled) is enforced as a strict limit. On Claude 4.5 models and newer, if input tokens plus `max_tokens` exceeds the context window size, the API accepts the request. If generation then reaches the context window limit, it stops with `stop_reason: "model_context_window_exceeded"`. On earlier models, the API returns a validation error instead. See [Handling stop reasons](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons).

You can read through the [guide on context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows) for a more thorough deep dive.

### The context window with extended thinking

When calculating context window usage with thinking enabled, there are some considerations to be aware of:

-   On Opus 4.5+ and Sonnet 4.6+, thinking blocks from previous turns are kept and count towards your context window; on earlier Opus/Sonnet models and all Haiku models, they are stripped and not counted
-   Current turn thinking counts towards your `max_tokens` limit for that turn

The diagram below demonstrates the specialized token management when extended thinking is enabled:

https://platform.claude.com/docs/images/context-window-thinking.svg

The effective context window is calculated as:

```
context window =
  (current input tokens - previous thinking tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)
```

Use the [token counting API](https://platform.claude.com/docs/en/build-with-claude/token-counting) to get accurate token counts for your specific use case, especially when working with multi-turn conversations that include thinking.

### The context window with extended thinking and tool use

When using extended thinking with tool use, thinking blocks must be explicitly preserved and returned with the tool results.

The effective context window calculation for extended thinking with tool use becomes:

```
context window =
  (current input tokens + previous thinking tokens + tool use tokens) +
  (thinking tokens + encrypted thinking tokens + text output tokens)
```

The diagram below illustrates token management for extended thinking with tool use:

https://platform.claude.com/docs/images/context-window-thinking-tools.svg

### Managing tokens with extended thinking

Given the context window and `max_tokens` behavior with extended thinking, you may need to:

-   More actively monitor and manage your token usage
-   Adjust `max_tokens` values as your prompt length changes
-   Potentially use the [token counting endpoints](https://platform.claude.com/docs/en/build-with-claude/token-counting) more frequently
-   Be aware that previous thinking blocks don't accumulate in your context window

## Thinking encryption

Full thinking content is encrypted and returned in the `signature` field. This field is used to verify that thinking blocks were generated by Claude when passed back to the API.

It is only strictly necessary to send back thinking blocks when using [tools with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use). Otherwise you can omit thinking blocks from previous turns. If you pass them back, whether the API keeps or strips them depends on the model: Opus 4.5+ and Sonnet 4.6+ keep them in context by default; earlier Opus/Sonnet models and all Haiku models strip them. See [context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) to configure this.

If sending back thinking blocks, pass everything back as you received it for consistency and to avoid potential issues.

Here are some important considerations on thinking encryption:

-   When [streaming responses](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#streaming-thinking), the signature is added via a `signature_delta` inside a `content_block_delta` event just before the `content_block_stop` event.
-   `signature` values are significantly longer in Claude 4 models than in previous models.
-   The `signature` field is an opaque field and should not be interpreted or parsed.
-   `signature` values are compatible across platforms (Claude APIs, [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock), and [Vertex AI](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)). Values generated on one platform will be compatible with another.

## Redacted thinking blocks

In addition to regular `thinking` blocks, the API may return `redacted_thinking` blocks. A `redacted_thinking` block contains encrypted thinking content in a `data` field, with no readable summary:

```
{
  "type": "redacted_thinking",
  "data": "..."
}
```

The `data` field is opaque and encrypted. Like the `signature` field on regular thinking blocks, you should pass `redacted_thinking` blocks back to the API unchanged when continuing a multi-turn conversation with [tools](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-tool-use).

If your code filters content blocks by type (for example, `block.type == "thinking"`) when round-tripping responses with tool use, also include `redacted_thinking` blocks. Filtering on `block.type == "thinking"` alone silently drops `redacted_thinking` blocks and breaks the multi-turn protocol described above.

`redacted_thinking` blocks are a distinct content block type returned by the API when portions of thinking are safety-redacted. This is separate from the [`display: "omitted"`](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#controlling-thinking-display) option, which returns regular `thinking` blocks with an empty `thinking` field.

## Differences in thinking across model versions

The Messages API handles thinking differently across Claude model versions. The following table gives a condensed comparison:

| Feature | Claude 4 models (pre-Opus 4.5) | Claude Opus 4.5 | Claude Sonnet 4.6 | Claude Opus 4.6 ( [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)) | Claude Opus 4.7 ( [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)) | Claude Opus 4.8 ( [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)) | [Claude Mythos Preview](https://anthropic.com/glasswing) ( [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Thinking output** | Returns summarized thinking | Returns summarized thinking | Returns summarized thinking | Returns summarized thinking | Omitted by default; set `display: "summarized"` to receive summarized thinking | Omitted by default; set `display: "summarized"` to receive summarized thinking | Omitted by default; set `display: "summarized"` to receive summarized thinking. Raw thinking tokens are never returned. |
| **Interleaved thinking** | Supported with `interleaved-thinking-2025-05-14` beta header | Supported with `interleaved-thinking-2025-05-14` beta header | Supported with `interleaved-thinking-2025-05-14` beta header or automatic with [adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) | Automatic with adaptive thinking (beta header deprecated and safely ignored) | Automatic with adaptive thinking (beta header deprecated and safely ignored) | Automatic with adaptive thinking (beta header deprecated and safely ignored) | Automatic with adaptive thinking (beta header not needed and safely ignored). Inter-tool reasoning moves into thinking blocks on this model. |
| **Thinking block preservation** | Not preserved across turns | **Preserved by default** | **Preserved by default** | **Preserved by default** | **Preserved by default** | **Preserved by default** | **Preserved by default.** Blocks are stripped when continuing the conversation on a model that does not support the Mythos thinking format. |

### Thinking block preservation by model

Whether thinking blocks from previous assistant turns are preserved in context by default depends on the model class. **Opus**: Claude Opus 4.5 and later Opus models keep all prior thinking blocks; Claude Opus 4.1 (deprecated) and earlier Opus models keep only the last assistant turn's thinking. **Sonnet**: Claude Sonnet 4.6 and later Sonnet models keep all; Claude Sonnet 4.5 and earlier Sonnet models keep only the last turn. **Haiku**: all Haiku models through Claude Haiku 4.5 keep only the last turn. [Claude Mythos Preview](https://anthropic.com/glasswing) also keeps all prior thinking blocks.

**Benefits of thinking block preservation:**

-   **Cache optimization**: When using tool use, preserved thinking blocks enable cache hits as they are passed back with tool results and cached incrementally across the assistant turn, resulting in token savings in multi-step workflows
-   **No intelligence impact**: Preserving thinking blocks has no negative effect on model performance

**Important considerations:**

-   **Context usage**: Long conversations will consume more context space since thinking blocks are retained in context
-   **Automatic behavior**: This is the default for each model as listed above. No code changes or beta headers are required
-   **Backward compatibility**: To leverage this feature, continue passing complete, unmodified thinking blocks back to the API as you would for tool use

For earlier models (Claude Sonnet 4.5, Opus 4.1 (deprecated), etc.), thinking blocks from previous turns continue to be removed from context. The existing behavior described in the [Extended thinking with prompt caching](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#extended-thinking-with-prompt-caching) section applies to those models.

## Pricing

For complete pricing information including base rates, cache writes, cache hits, and output tokens, see the [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).

The thinking process incurs charges for:

-   Tokens used during thinking (output tokens)
-   Thinking blocks from prior assistant turns kept in context: only the last turn on earlier Opus/Sonnet models and all Haiku models; all turns by default on Opus 4.5+ and Sonnet 4.6+ (input tokens)
-   Standard text output tokens

When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.

When using summarized thinking:

-   **Input tokens:** Tokens in your original request (excludes thinking tokens from previous turns)
-   **Output tokens (billed):** The original thinking tokens that Claude generated internally
-   **Output tokens (visible):** The summarized thinking tokens you see in the response
-   **No charge:** Tokens used to generate the summary

When using `display: "omitted"`:

-   **Input tokens:** Tokens in your original request (same as summarized)
-   **Output tokens (billed):** The original thinking tokens that Claude generated internally (same as summarized)
-   **Output tokens (visible):** Zero thinking tokens (the `thinking` field is empty)

The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the thinking content visible in the response.

To see how many billed output tokens were spent on internal reasoning, read `usage.output_tokens_details.thinking_tokens` in the response. This value reflects the raw reasoning the model generated (not the summarized text returned in the body) and is always less than or equal to `output_tokens`. Subtract it from `output_tokens` to approximate the non-reasoning portion of the output.

```
{
  "usage": {
    "input_tokens": 25,
    "output_tokens": 348,
    "output_tokens_details": {
      "thinking_tokens": 312
    }
  }
}
```

`output_tokens` remains the inclusive, authoritative total used for billing. `output_tokens_details` is a read-only breakdown for observability.

## Best practices and considerations for extended thinking

### Working with thinking budgets

-   **Budget optimization:** The minimum budget is 1,024 tokens. Start at the minimum and increase the thinking budget incrementally to find the optimal range for your use case. Higher token counts enable more comprehensive reasoning but with diminishing returns depending on the task. Increasing the budget can improve response quality at the tradeoff of increased latency. For critical tasks, test different settings to find the optimal balance. Note that the thinking budget is a target rather than a strict limit. Actual token usage may vary based on the task.
-   **Starting points:** Start with larger thinking budgets (16k+ tokens) for complex tasks and adjust based on your needs.
-   **Large budgets:** For thinking budgets above 32k, use [batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) to avoid networking issues. Requests pushing the model to think above 32k tokens causes long running requests that might run up against system timeouts and open connection limits.
-   **Token usage tracking:** Monitor thinking token usage to optimize costs and performance. The `usage.output_tokens_details.thinking_tokens` field in the response reports how many of the billed output tokens were internal reasoning. When streaming, this breakdown appears only on the final `message_delta` event.

### Performance considerations

-   **Response times:** Be prepared for longer response times due to additional processing. Generating thinking blocks increases overall response time.
-   **Streaming requirements:** The SDKs require streaming when `max_tokens` is greater than 21,333 to avoid HTTP timeouts on long-running requests. This is a client-side validation, not an API restriction. If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` (Python) or `.finalMessage()` (TypeScript) to get the complete `Message` object without handling individual events. See [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for details. When streaming, be prepared to handle both thinking and text content blocks as they arrive.
-   **Omitting thinking for latency:** If your application doesn't display thinking content, set `display: "omitted"` on the thinking configuration to reduce time-to-first-text-token. See [Controlling thinking display](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#controlling-thinking-display).

### Feature compatibility

-   Thinking isn't compatible with `temperature` or `top_k` modifications as well as [forced tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools#forcing-tool-use).
-   When thinking is enabled, you can set `top_p` to values between 1 and 0.95.
-   You can't pre-fill responses when thinking is enabled.
-   Changes to the thinking budget invalidate cached prompt prefixes that include messages. However, cached system prompts and tool definitions will continue to work when thinking parameters change.

### Usage guidelines

-   **Task selection:** Use extended thinking for particularly complex tasks that benefit from step-by-step reasoning, like math, coding, and analysis.
-   **Context handling:** You don't need to remove previous thinking blocks yourself. On Opus 4.5+ and Sonnet 4.6+, the Claude API keeps thinking blocks from previous turns by default; on earlier Opus/Sonnet models and all Haiku models, it automatically ignores them and they aren't included when calculating context usage.
-   **Prompt engineering:** Review the [extended thinking prompting tips](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#leverage-thinking-and-interleaved-thinking-capabilities) if you want to maximize Claude's thinking capabilities.

## Next steps

[Try the extended thinking cookbook](https://platform.claude.com/cookbook/extended-thinking-extended-thinking) [Explore practical examples of thinking in the cookbook.](https://platform.claude.com/cookbook/extended-thinking-extended-thinking) [Extended thinking prompting tips](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#leverage-thinking-and-interleaved-thinking-capabilities) [Learn prompt engineering best practices for extended thinking.](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#leverage-thinking-and-interleaved-thinking-capabilities)

</details>

<details>
<summary>Human-in-the-loop</summary>

# Human-in-the-loop

**Source URL:** <https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/>

Interrupts allow you to pause graph execution at specific points and wait for external input before continuing. This enables human-in-the-loop patterns where you need external input to proceed. When an interrupt is triggered, LangGraph saves the graph state using its [persistence](https://docs.langchain.com/oss/python/langgraph/persistence) layer and waits indefinitely until you resume execution.Interrupts work by calling the `interrupt()` function at any point in your graph nodes. The function accepts any JSON-serializable value which is surfaced to the caller. When you’re ready to continue, you resume execution by re-invoking the graph using `Command`, which then becomes the return value of the `interrupt()` call from inside the node.Unlike static breakpoints (which pause before or after specific nodes), interrupts are **dynamic**: they can be placed anywhere in your code and can be conditional based on your application logic.

- **Checkpointing keeps your place:** the checkpointer writes the exact graph state so you can resume later, even when in an error state.
- **`thread_id` is your pointer:** set `config={"configurable": {"thread_id": ...}}` to tell the checkpointer which state to load.
- **Interrupt payloads surface via `stream.interrupts`:** when using [event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) (`graph.stream_events(..., version="v3")`), the values you pass to `interrupt()` appear on `stream.interrupts`, and `stream.interrupted` is `True` when the run pauses for input.

The `thread_id` you choose is effectively your persistent cursor. Reusing it resumes the same checkpoint; using a new value starts a brand-new thread with an empty state.

## Pause using `interrupt`

The [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function pauses graph execution and returns a value to the caller. When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) within a node, LangGraph saves the current graph state and waits for you to resume execution with input.To use [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt), you need:

1. A **checkpointer** to persist the graph state (use a durable checkpointer in production)
2. A **thread ID** in your config so the runtime knows which state to resume from
3. To call `interrupt()` where you want to pause (payload must be JSON-serializable)

```
from langgraph.types import interrupt

def approval_node(state: State):
    # Pause and ask for approval
    approved = interrupt("Do you approve this action?")

    # When you resume, Command(resume=...) returns that value here
    return {"approved": approved}
```

When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt), here’s what happens:

1. **Graph execution gets suspended** at the exact point where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) is called
2. **State is saved** using the checkpointer so execution can be resumed later, In production, this should be a persistent checkpointer (e.g. backed by a database)
3. **Value is returned** to the caller on `stream.interrupts` when using [event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) (`graph.stream_events(..., version="v3")`), or under `__interrupt__` with the default `invoke()` API; it can be any JSON-serializable value (string, object, array, etc.)
4. **Graph waits indefinitely** until you resume execution with a response
5. **Response is passed back** into the node when you resume, becoming the return value of the `interrupt()` call

## Resuming interrupts

After an interrupt pauses execution, you resume the graph by invoking it again with a `Command` that contains the resume value. The resume value is passed back to the `interrupt` call, allowing the node to continue execution with the external input.The recommended way to drive a graph that may interrupt is [event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) — it surfaces interrupts via `stream.interrupts` and `stream.interrupted`, and exposes the final state through `stream.output`.

```
from langgraph.types import Command

# Initial run - hits the interrupt and pauses
# thread_id is the persistent pointer (stores a stable ID in production)
config = {"configurable": {"thread_id": "thread-1"}}
stream = graph.stream_events({"input": "data"}, config=config, version="v3")

# Drain the stream to drive the run; stream.output awaits the final state.
final = stream.output

# stream.interrupted is True when the run paused for human input, and
# stream.interrupts contains the payloads passed to interrupt().
if stream.interrupted:
    print(stream.interrupts)
    # > (Interrupt(value='Do you approve this action?'),)

# Resume with the human's response
# The resume payload becomes the return value of interrupt() inside the node
resumed = graph.stream_events(Command(resume=True), config=config, version="v3")
final = resumed.output
```

The default `graph.invoke(...)` API still works and surfaces interrupts under `result["__interrupt__"]`. Use it when you don’t need streamed projections; otherwise prefer `graph.stream_events(..., version="v3")`.

**Key points about resuming:**

- You must use the **same thread ID** when resuming that was used when the interrupt occurred
- The value passed to `Command(resume=...)` becomes the return value of the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) call
- The node restarts from the beginning of the node where the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called when resumed, so any code before the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) runs again
- You can pass any JSON-serializable value as the resume value

`Command(resume=...)` is the **only**`Command` pattern intended as input to `invoke()`/`stream()`/`stream_events()`. The other `Command` parameters (`update`, `goto`, `graph`) are designed for [returning from node functions](https://docs.langchain.com/oss/python/langgraph/graph-api#command). Do not pass `Command(update=...)` as input to continue multi-turn conversations—pass a plain input dict instead.

## Common patterns

The key thing that interrupts unlock is the ability to pause execution and wait for external input. This is useful for a variety of use cases, including:

- [Approval workflows](https://docs.langchain.com/oss/python/langgraph/interrupts#approve-or-reject): Pause before executing critical actions (API calls, database changes, financial transactions)
- [Handling multiple interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts#handling-multiple-interrupts): Pair interrupt IDs with resume values when resuming multiple interrupts in a single invocation
- [Review and edit](https://docs.langchain.com/oss/python/langgraph/interrupts#review-and-edit-state): Let humans review and modify LLM outputs or tool calls before continuing
- [Interrupting tool calls](https://docs.langchain.com/oss/python/langgraph/interrupts#interrupts-in-tools): Pause before executing tool calls to review and edit the tool call before execution
- [Validating human input](https://docs.langchain.com/oss/python/langgraph/interrupts#validating-human-input): Pause before proceeding to the next step to validate human input

### Stream with human-in-the-loop (HITL) interrupts

When building interactive agents with human-in-the-loop workflows, you can use [event streaming](https://docs.langchain.com/oss/python/langgraph/event-streaming) to consume message chunks and state snapshots concurrently while handling interrupts.Use the typed projections returned by `graph.stream_events(..., version="v3")` in a loop until the run finishes:

- Stream AI responses token-by-token via `stream.messages`
- Observe per-step state snapshots via `stream.values`
- Detect interrupts via `stream.interrupted` and read their payloads from `stream.interrupts`
- Resume execution by calling `stream_events` again with `Command(resume=...)` and repeat until `stream.interrupted` is false

```
from langgraph.types import Command

stream_input: dict | Command = initial_input

while True:
    stream = graph.stream_events(stream_input, config=config, version="v3")

    # Stream LLM message chunks (including any in subgraphs) as they arrive.
    for message in stream.messages:
        for token in message.text:
            display_streaming_content(token)

    # After the run finishes (or pauses), check for interrupts and resume.
    if not stream.interrupted:
        final_state = stream.output
        break

    interrupt_info = stream.interrupts[0].value
    user_response = get_user_input(interrupt_info)
    stream_input = Command(resume=user_response)
```

- **`stream.messages`**: Chat-model output as content blocks; iterate each `message.text` for token deltas. For nested subgraphs, read message chunks from `stream.subgraphs[*].messages`.
- **`stream.values`**: Full state snapshots after each step
- **`stream.interrupted` / `stream.interrupts`**: After each run, check whether the graph paused; read payloads from `stream.interrupts`
- **`Command(resume=...)`**: Pass as the next `stream_events` input to resume; loop until the run completes without interrupting

### Handling multiple interrupts

When parallel branches interrupt simultaneously (for example, fan-out to multiple nodes that each call `interrupt()`), you may need to resume multiple interrupts in a single invocation.
When resuming multiple interrupts with a single invocation, map each interrupt ID to its resume value.
This ensures each response is paired with the correct interrupt at runtime.

```
from typing import Annotated, TypedDict
import operator

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class State(TypedDict):
    vals: Annotated[list[str], operator.add]

def node_a(state):
    answer = interrupt("question_a")
    return {"vals": [f"a:{answer}"]}

def node_b(state):
    answer = interrupt("question_b")
    return {"vals": [f"b:{answer}"]}

graph = (
    StateGraph(State)
    .add_node("a", node_a)
    .add_node("b", node_b)
    .add_edge(START, "a")
    .add_edge(START, "b")
    .add_edge("a", END)
    .add_edge("b", END)
    .compile(checkpointer=InMemorySaver())
)

config = {"configurable": {"thread_id": "1"}}

# Step 1: stream events to drive the run; both parallel nodes hit interrupt() and pause
stream = graph.stream_events({"vals": []}, config, version="v3")
_ = stream.output  # drive the stream to completion
# stream.interrupts contains the pending Interrupt payloads
print(stream.interrupts)
# > (Interrupt(value='question_a', id='...'), Interrupt(value='question_b', id='...'))

# Step 2: resume all pending interrupts at once
resume_map = {
    i.id: f"answer for {i.value}" for i in stream.interrupts
}
resumed = graph.stream_events(Command(resume=resume_map), config, version="v3")

print("Final state:", resumed.output)
# Final state: {'vals': ['a:answer for question_a', 'b:answer for question_b']}
```

### Approve or reject

One of the most common uses of interrupts is to pause before a critical action and ask for approval. For example, you might want to ask a human to approve an API call, a database change, or any other important decision.

```
from typing import Literal
from langgraph.types import interrupt, Command

def approval_node(state: State) -> Command[Literal["proceed", "cancel"]]:
    # Pause execution; payload shows up on stream.interrupts (with stream_events) or result["__interrupt__"] (with invoke)
    is_approved = interrupt({
        "question": "Do you want to proceed with this action?",
        "details": state["action_details"]
    })

    # Route based on the response
    if is_approved:
        return Command(goto="proceed")  # Runs after the resume payload is provided
    else:
        return Command(goto="cancel")
```

When you resume the graph, pass `True` to approve or `False` to reject:

```
# To approve
graph.stream_events(Command(resume=True), config=config, version="v3").output

# To reject
graph.stream_events(Command(resume=False), config=config, version="v3").output
```

Full example

```
from typing import Literal, Optional, TypedDict

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class ApprovalState(TypedDict):
    action_details: str
    status: Optional[Literal["pending", "approved", "rejected"]]

def approval_node(state: ApprovalState) -> Command[Literal["proceed", "cancel"]]:
    # Expose details so the caller can render them in a UI
    decision = interrupt(
        {
            "question": "Approve this action?",
            "details": state["action_details"],
        }
    )

    # Route to the appropriate node after resume
    return Command(goto="proceed" if decision else "cancel")

def proceed_node(state: ApprovalState):
    return {"status": "approved"}

def cancel_node(state: ApprovalState):
    return {"status": "rejected"}

builder = StateGraph(ApprovalState)
builder.add_node("approval", approval_node)
builder.add_node("proceed", proceed_node)
builder.add_node("cancel", cancel_node)
builder.add_edge(START, "approval")
builder.add_edge("proceed", END)
builder.add_edge("cancel", END)

# Use a more durable checkpointer in production
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "approval-123"}}
initial = graph.stream_events(
    {"action_details": "Transfer $500", "status": "pending"},
    config=config,
    version="v3",
)
_ = initial.output  # drive the stream to completion
print(initial.interrupts)  # -> (Interrupt(value={'question': ..., 'details': ...}),)

# Resume with the decision; True routes to proceed, False to cancel
resumed = graph.stream_events(Command(resume=True), config=config, version="v3")
print(resumed.output["status"])
```

### Review and edit state

Sometimes you want to let a human review and edit part of the graph state before continuing. This is useful for correcting LLMs, adding missing information, or making adjustments.

```
from langgraph.types import interrupt

def review_node(state: State):
    # Pause and show the current content for review (payload surfaces on stream.interrupts)
    edited_content = interrupt({
        "instruction": "Review and edit this content",
        "content": state["generated_text"]
    })

    # Update the state with the edited version
    return {"generated_text": edited_content}
```

When resuming, provide the edited content:

```
graph.stream_events(
    Command(resume="The edited and improved text"),  # Value becomes the return from interrupt()
    config=config,
    version="v3",
).output
```

Full example

```
from typing import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class ReviewState(TypedDict):
    generated_text: str

def review_node(state: ReviewState):
    # Ask a reviewer to edit the generated content
    updated = interrupt(
        {
            "instruction": "Review and edit this content",
            "content": state["generated_text"],
        }
    )
    return {"generated_text": updated}

builder = StateGraph(ReviewState)
builder.add_node("review", review_node)
builder.add_edge(START, "review")
builder.add_edge("review", END)

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "review-42"}}
initial = graph.stream_events(
    {"generated_text": "Initial draft"}, config=config, version="v3"
)
_ = initial.output  # drive the stream to completion
print(initial.interrupts)  # -> (Interrupt(value={'instruction': ..., 'content': ...}),)

# Resume with the edited text from the reviewer
final_state = graph.stream_events(
    Command(resume="Improved draft after review"),
    config=config,
    version="v3",
)
print(final_state.output["generated_text"])  # -> "Improved draft after review"
```

### Interrupts in tools

You can also place interrupts directly inside tool functions. This makes the tool itself pause for approval whenever it’s called, and allows for human review and editing of the tool call before it is executed.First, define a tool that uses [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt):

```
from langchain.tools import tool
from langgraph.types import interrupt

@tool
def send_email(to: str, subject: str, body: str):
    """Send an email to a recipient."""

    # Pause before sending; payload surfaces on stream.interrupts when using event streaming
    response = interrupt({
        "action": "send_email",
        "to": to,
        "subject": subject,
        "body": body,
        "message": "Approve sending this email?"
    })

    if response.get("action") == "approve":
        # Resume value can override inputs before executing
        final_to = response.get("to", to)
        final_subject = response.get("subject", subject)
        final_body = response.get("body", body)
        return f"Email sent to {final_to} with subject '{final_subject}'"
    return "Email cancelled by user"
```

This approach is useful when you want the approval logic to live with the tool itself, making it reusable across different parts of your graph. The LLM can call the tool naturally, and the interrupt will pause execution whenever the tool is invoked, allowing you to approve, edit, or cancel the action.

Full example

```
import sqlite3
import operator
from typing import TypedDict, Annotated, Literal
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt
from langchain.messages import AnyMessage, SystemMessage, ToolMessage

class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

@tool
def send_email(to: str, subject: str, body: str):
    """Send an email to a recipient."""

    # Pause before sending; payload surfaces on stream.interrupts when using event streaming
    response = interrupt({
        "action": "send_email",
        "to": to,
        "subject": subject,
        "body": body,
        "message": "Approve sending this email?",
    })

    if response.get("action") == "approve":
        final_to = response.get("to", to)
        final_subject = response.get("subject", subject)
        final_body = response.get("body", body)

        # Actually send the email (your implementation here)
        print(f"[send_email] to={final_to} subject={final_subject} body={final_body}")
        return f"Email sent to {final_to}"

    return "Email cancelled by user"

model = ChatAnthropic(model="claude-sonnet-4-6").bind_tools([send_email])
tools_by_name = {"send_email": send_email}

def agent_node(state: AgentState):
    # LLM may decide to call the tool; interrupt pauses before sending
    result = model.invoke(state["messages"])
    return {"messages": [result]}

def tool_node(state: AgentState):
    """Performs the tool call"""
    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

def should_continue(state: AgentState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""
    messages = state["messages"]
    last_message = messages[-1]

    if last_message.tool_calls:
        return "tool_node"
    return END

builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)
builder.add_node("tool_node", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", should_continue, ["tool_node", END])  # Routes to "tools" or END
builder.add_edge("tool_node", "agent")  # Loop back after tools

checkpointer = SqliteSaver(
    sqlite3.connect("tool-approval.db", check_same_thread=False)
)
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "email-workflow"}}
initial = graph.stream_events(
    {
        "messages": [\
            {"role": "user", "content": "Send an email to alice@example.com about the meeting"}\
        ]
    },
    config=config,
    version="v3",
)
initial.output  # drive the stream to completion
print(initial.interrupts)  # -> (Interrupt(value={'action': 'send_email', ...}),)

# Resume with approval and optionally edited arguments
resumed = graph.stream_events(
    Command(resume={"action": "approve", "subject": "Updated subject"}),
    config=config,
    version="v3",
)
print(resumed.output["messages"][-1])  # -> Tool result returned by send_email
```

### Validating human input

Sometimes you need to validate input from humans and ask again if it’s invalid. You can do this using multiple [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls in a loop.

```
from langgraph.types import interrupt

def get_age_node(state: State):
    prompt = "What is your age?"

    while True:
        answer = interrupt(prompt)  # payload surfaces on stream.interrupts when using event streaming

        # Validate the input
        if isinstance(answer, int) and answer > 0:
            # Valid input - continue
            break
        else:
            # Invalid input - ask again with a more specific prompt
            prompt = f"'{answer}' is not a valid age. Please enter a positive number."

    return {"age": answer}
```

Each time you resume the graph with invalid input, it will ask again with a clearer message. Once valid input is provided, the node completes and the graph continues.

Full example

```
import sqlite3
from typing import TypedDict

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

class FormState(TypedDict):
    age: int | None

def get_age_node(state: FormState):
    prompt = "What is your age?"

    while True:
        answer = interrupt(prompt)

        if isinstance(answer, int) and answer > 0:
            return {"age": answer}

        prompt = f"'{answer}' is not a valid age. Please enter a positive number."

builder = StateGraph(FormState)
builder.add_node("collect_age", get_age_node)
builder.add_edge(START, "collect_age")
builder.add_edge("collect_age", END)

checkpointer = SqliteSaver(sqlite3.connect("forms.db"))
graph = builder.compile(checkpointer=checkpointer)

config = {"configurable": {"thread_id": "form-1"}}
first = graph.stream_events({"age": None}, config=config, version="v3")
_ = first.output  # drive the stream to completion
print(first.interrupts)  # -> (Interrupt(value='What is your age?', ...),)

# Provide invalid data; the node re-prompts
retry = graph.stream_events(Command(resume="thirty"), config=config, version="v3")
_ = retry.output  # drive the stream to completion
print(retry.interrupts)  # -> (Interrupt(value="'thirty' is not a valid age...", ...),)

# Provide valid data; loop exits and state updates
final = graph.stream_events(Command(resume=30), config=config, version="v3")
print(final.output["age"])  # -> 30
```

## Rules of interrupts

When you call [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) within a node, LangGraph suspends execution by raising an exception that signals the runtime to pause. This exception propagates up through the call stack and is caught by the runtime, which notifies the graph to save the current state and wait for external input.When execution resumes (after you provide the requested input), the runtime restarts the entire node from the beginning—it does not resume from the exact line where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called. This means any code that ran before the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) will execute again. Because of this, there’s a few important rules to follow when working with interrupts to ensure they behave as expected.

### Do not wrap `interrupt` calls in try/except

The way that [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) pauses execution at the point of the call is by throwing a special exception. If you wrap the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) call in a try/except block, you will catch this exception and the interrupt will not be passed back to the graph.

- ✅ Separate [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls from error-prone code
- ✅ Use specific exception types in try/except blocks

Separating logic

Explicit exception handling

```
def node_a(state: State):
    # ✅ Good: interrupting first, then handling
    # error conditions separately
    interrupt("What's your name?")
    try:
        fetch_data()  # This can fail
    except Exception as e:
        print(e)
    return state
```

- 🔴 Do not wrap [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls in bare try/except blocks

```
def node_a(state: State):
    # ❌ Bad: wrapping interrupt in bare try/except
    # will catch the interrupt exception
    try:
        interrupt("What's your name?")
    except Exception as e:
        print(e)
    return state
```

### Do not reorder `interrupt` calls within a node

It’s common to use multiple interrupts in a single node, however this can lead to unexpected behavior if not handled carefully.When a node contains multiple interrupt calls, LangGraph keeps a list of resume values specific to the task executing the node. Whenever execution resumes, it starts at the beginning of the node. For each interrupt encountered, LangGraph checks if a matching value exists in the task’s resume list. Matching is **strictly index-based**, so the order of interrupt calls within the node is important.

- ✅ Keep [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls consistent across node executions

```
def node_a(state: State):
    # ✅ Good: interrupt calls happen in the same order every time
    name = interrupt("What's your name?")
    age = interrupt("What's your age?")
    city = interrupt("What's your city?")

    return {
        "name": name,
        "age": age,
        "city": city
    }
```

- 🔴 Do not conditionally skip [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls within a node
- 🔴 Do not loop [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls using logic that isn’t deterministic across executions

Skipping interrupts

Looping interrupts

```
def node_a(state: State):
    # ❌ Bad: conditionally skipping interrupts changes the order
    name = interrupt("What's your name?")

    # On first run, this might skip the interrupt
    # On resume, it might not skip it - causing index mismatch
    if state.get("needs_age"):
        age = interrupt("What's your age?")

    city = interrupt("What's your city?")

    return {"name": name, "city": city}
```

### Do not return complex values in `interrupt` calls

Depending on which checkpointer is used, complex values may not be serializable (e.g. you can’t serialize a function). To make your graphs adaptable to any deployment, it’s best practice to only use values that can be reasonably serialized.

- ✅ Pass simple, JSON-serializable types to [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
- ✅ Pass dictionaries/objects with simple values

Simple values

Structured data

```
def node_a(state: State):
    # ✅ Good: passing simple types that are serializable
    name = interrupt("What's your name?")
    count = interrupt(42)
    approved = interrupt(True)

    return {"name": name, "count": count, "approved": approved}
```

- 🔴 Do not pass functions, class instances, or other complex objects to [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)

Functions

Class instances

```
def validate_input(value):
    return len(value) > 0

def node_a(state: State):
    # ❌ Bad: passing a function to interrupt
    # The function cannot be serialized
    response = interrupt({
        "question": "What's your name?",
        "validator": validate_input  # This will fail
    })
    return {"name": response}
```

### Side effects called before `interrupt` must be idempotent

Because interrupts work by re-running the nodes they were called from, side effects called before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) should (ideally) be idempotent. For context, idempotency means that the same operation can be applied multiple times without changing the result beyond the initial execution.As an example, you might have an API call to update a record inside of a node. If [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) is called after that call is made, it will be re-run multiple times when the node is resumed, potentially overwriting the initial update or creating duplicate records.

- ✅ Use idempotent operations before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
- ✅ Place side effects after [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) calls
- ✅ Separate side effects into separate nodes when possible

Idempotent operations

Side effects after interrupt

Separating into different nodes

```
def node_a(state: State):
    # ✅ Good: using upsert operation which is idempotent
    # Running this multiple times will have the same result
    db.upsert_user(
        user_id=state["user_id"],
        status="pending_approval"
    )

    approved = interrupt("Approve this change?")

    return {"approved": approved}
```

- 🔴 Do not perform non-idempotent operations before [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt)
- 🔴 Do not create new records without checking if they exist

Creating records

Appending to lists

```
def node_a(state: State):
    # ❌ Bad: creating a new record before interrupt
    # This will create duplicate records on each resume
    audit_id = db.create_audit_log({
        "user_id": state["user_id"],
        "action": "pending_approval",
        "timestamp": datetime.now()
    })

    approved = interrupt("Approve this change?")

    return {"approved": approved, "audit_id": audit_id}
```

## Using with subgraphs called as functions

When invoking a subgraph within a node, the parent graph will resume execution from the **beginning of the node** where the subgraph was invoked and the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was triggered. Similarly, the **subgraph** will also resume from the beginning of the node where [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) was called.

```
def node_in_parent_graph(state: State):
    some_code()  # <-- This will re-execute when resumed
    # Invoke a subgraph as a function.
    # The subgraph contains an `interrupt` call.
    subgraph_result = subgraph.invoke(some_input)
    # ...

def node_in_subgraph(state: State):
    some_other_code()  # <-- This will also re-execute when resumed
    result = interrupt("What's your name?")
    # ...
```

## Debugging with interrupts

To debug and test a graph, you can use static interrupts as breakpoints to step through the graph execution one node at a time. Static interrupts are triggered at defined points either before or after a node executes. You can set these by specifying `interrupt_before` and `interrupt_after` when compiling the graph.

Static interrupts are **not** recommended for human-in-the-loop workflows. Use the [`interrupt`](https://reference.langchain.com/python/langgraph/types/interrupt) function instead.

- At compile time

- At run time


```
graph = builder.compile(
    interrupt_before=["node_a"],
    interrupt_after=["node_b", "node_c"],
    checkpointer=checkpointer,
)

# Pass a thread ID to the graph
config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run the graph until the breakpoint
graph.invoke(inputs, config=config)

# Resume the graph
graph.invoke(None, config=config)
```

1. The breakpoints are set during `compile` time.
2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
4. A checkpointer is required to enable breakpoints.
5. The graph is run until the first breakpoint is hit.
6. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.

```
config = {
    "configurable": {
        "thread_id": "some_thread"
    }
}

# Run the graph until the breakpoint
graph.invoke(
    inputs,
    interrupt_before=["node_a"],
    interrupt_after=["node_b", "node_c"],
    config=config,
)

# Resume the graph
graph.invoke(None, config=config)
```

1. `graph.invoke` is called with the `interrupt_before` and `interrupt_after` parameters. This is a run-time configuration and can be changed for every invocation.
2. `interrupt_before` specifies the nodes where execution should pause before the node is executed.
3. `interrupt_after` specifies the nodes where execution should pause after the node is executed.
4. The graph is run until the first breakpoint is hit.
5. The graph is resumed by passing in `None` for the input. This will run the graph until the next breakpoint is hit.

To debug your interrupts, use [LangSmith](https://docs.langchain.com/langsmith/home).

### Using LangSmith Studio

You can use [LangSmith Studio](https://docs.langchain.com/langsmith/studio) to set static interrupts in your graph in the UI before running the graph. You can also use the UI to inspect the graph state at any point in the execution.https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/static-interrupt.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=5aa4e7cea2ab147cef5b4e210dd6c4a1

</details>

<details>
<summary>LLM System Design & Model Selection</summary>

# LLM System Design & Model Selection

**Source URL:** <https://www.oreilly.com/radar/llm-system-design-and-model-selection/>

https://www.oreilly.com/radar/wp-content/uploads/sites/4/2025/08/LouisFrancoisBouchard-150x150.pnghttps://www.oreilly.com/radar/wp-content/uploads/sites/4/2025/08/LouiePeters-150x150.png

By [Louis-François Bouchard](https://www.oreilly.com/people/louis-francois-bouchard/) and [Louie Peters](https://www.oreilly.com/people/louie-peters/)August 26, 2025 • 22 minute read

Choosing the right LLM has become a full-time job. New models appear almost daily, each offering different capabilities, prices, and quirks, from reasoning strengths to cost efficiency to code generation. This competition creates strong incentives for AI labs to carve out a niche and gives new startups room to emerge, resulting in a fragmented landscape where one model may excel at reasoning, another at code, and a third at cost efficiency.

AI, in one sense, is getting cheaper faster than any previous technology, at least per _unit of intelligence_. For example, input tokens for Gemini 2.5 Flash-Lite are approximately 600 times cheaper than what OpenAI’s GPT-3 (davinci-002) cost in August 2022, while outperforming it on every metric. At the same time, access to frontier capabilities is also becoming more expensive than ever. The reason is simple: we can now pay directly for more capability, which has led to the rise of $300+ per month Pro subscription tiers.

Today, any developer can run capable open-weight models locally for negligible marginal cost using tools like Ollama. At the same time, enterprise systems can experience sharp cost increases, depending on the model size (number of parameters, such as 3 billion, 70 billion, or even in the trillions), the number of internal processing steps, and the volume of input data. For developers, these are central system design choices that directly affect feasibility and cost structure. For end users, this complexity explains why a basic subscription differs so much from a premium plan with higher limits on advanced models.

The choices you make in these broader development decisions also determine which LLM and inference settings are optimal for your use case.

At Towards AI, we work across the LLM stack, building applications, designing enterprise systems, and offering online courses ( [including one on O’Reilly](https://www.oreilly.com/videos/building-and-operating/019283645221/)), custom corporate training, and LLM development consultancy. In our experience, model selection and system design have become central to getting meaningful results from these tools. Much of that, in turn, depends on where today’s models are gaining their capabilities. While scale still plays a role, recent progress has come from a broader mix of factors, including training-data quality, post-training methods, and especially how models are used at inference time.

## **The Shifting Foundations of Model Capability**

While early gains in LLM performance tracked closely with increases in pretraining compute, larger datasets, bigger models, and more training steps, this approach now yields diminishing returns.

Recent improvements come from a broader mix of strategies. Pretraining-data quality has become just as important as quantity, with better filtering and AI-generated synthetic data contributing to stronger models. Architectural efficiency, like the innovations introduced by DeepSeek, has started to close the gap between size and capability. And post-training techniques, especially instruction tuning and reinforcement learning from human or AI feedback (RLHF/RLAIF), have made models more aligned, controllable, and responsive in practice.

The more fundamental shift, however, is happening at inference time. Since late 2024, with models like OpenAI’s o1, we’ve entered a new phase where models can trade compute for reasoning _on demand_. Rather than relying solely on what was baked in during training, they can now “think harder” at runtime, running more internal steps, exploring alternative answers, or chaining thoughts before responding. This opens up new capability ceilings, but also introduces new cost dynamics.

These varied improvement strategies have led to a clear divergence among AI labs and models, a rapid expansion in model choice, and in some cases, an explosion in model usage costs.

## **The Modern Cost Explosion: How Inference Scaling Changed the Game**

Inference-time compute scaling has introduced a new dynamic in LLM system design: We’ve gone from a single lever model size, to at least four distinct ways to trade cost for capability at runtime. The result is a widening gap in inference cost across models and use cases, sometimes by factors of 10,000x or more.

**Larger models (size scaling):** The most obvious lever is sheer model size. Frontier LLMs, like GPT-4.5, often built with mixture of experts (MoE) architectures, can have input token costs 750 times higher than streamlined models like Gemini Flash-Lite. Larger parameter counts mean more compute per token, especially when multiple experts are active per query.

**Series scaling (“thinking tokens”):** Newer “reasoning” LLMs perform more internal computational steps, or a longer chain of thought, before producing their final answer. For example, OpenAI’s o1 used ~30x more compute than GPT-4o on average, and often 5x more output tokens per task. Agentic systems introduce an additional method of series scaling and an extra layer of cost multiplication. As these agents think, plan, act, reassess, plan, act, and so on, they often make many LLM steps in a loop, each incurring additional cost.

**Parallel scaling:** Here, the system runs multiple model instances on the same task and then automatically selects the best output via automated methods, such as majority voting (which assumes the most common answer is likely correct) or self-confidence scores (where the model output claiming the highest confidence in its response is taken as the best). The o3-pro model likely runs 5–10x parallel instances over o3. This multiplies the cost by the number of parallel attempts (with some nuance).

**Input context scaling:** In RAG pipelines, the number of retrieved chunks and their size directly influence input token costs and the LLM’s ability to synthesize a good answer. More context can often improve results, but this comes at a higher cost and potential latency. Context isn’t free; it’s another dimension of scaling that developers must budget for.

Taken together, these four factors represent a fundamental shift in how model cost scales. For developers designing systems for high-value problems, **10,000x to 1,000,000x differences in API costs to solve a problem based on architectural choices are now realistic possibilities**. Reasoning LLMs, although only prominent for about nine months, reversed the trend of declining access costs to the very best models. This transforms the decision from “Which LLM should I use?” to include “How much reasoning do I _want to pay for_?”

This shift changes how we think about selection. Choosing an LLM is no longer about chasing the highest benchmark score; it’s about finding the balance point where capability, latency, and cost align with your use case.

## **Core Model Selection Criteria**

When choosing a model we find it is important to first clearly identify your use case and the minimum core AI capabilities and attributes needed to deliver it.

A common first step is to take a look at standard benchmark scores (for example LiveBench, MMLU-Pro, SWE-Bench). These benchmarks are a useful starting point, but some models are tuned on benchmark data, and real-world performance on tasks that are actually relevant to you will often vary. Filtering benchmark tests and scores by your industry and task category is a valuable step here. An LLM optimized for software development might perform poorly in creative writing or vice versa. The match between a model’s training focus and your application domain can outweigh general-purpose benchmarks.

Leaderboards like [LMArena](https://lmarena.ai/leaderboard) and [Artificial Analysis](https://artificialanalysis.ai/) offer broader human‑preference comparisons but still don’t replace custom real-world testing. It helps to have a set of your own example questions or tasks at hand to test out a new model for yourself and see how it performs. This should include a mix of easy tasks to establish a baseline and tough edge cases where it’s easy for a model to make mistakes.

As you move beyond ad hoc testing, for any serious development effort, **custom evaluations are non-negotiable.** They must be tailored to your use case and the types of problems you solve. This is the only way to truly know if a model, or a change to your system, is genuinely improving things for _your_ users and _your_ specific business goals.

Here are some core factors we consider:

**Multimodality** is emerging as a major differentiator. Models like GPT-4o and Gemini can handle not just text but also images, audio, and in some cases video, unlocking applications that pure text models can’t support.

**Context window** and effective **context window utilization** are also key: How many tokens or documents can the model process and how much of that advertised context window can the LLM _actually use_ effectively without performance degradation relative to tasks that use less context?

**Latency** is especially critical for interactive applications. In general, smaller or cheaper models tend to respond faster, while reasoning-heavy models introduce delays due to deeper internal computation.

**Reasoning** is the ability to scale inference-time compute and perform multistep problem-solving, planning, or deep analysis.

**Privacy and security** are often key considerations here. For example, if you want to keep your intellectual property private, you must use a model that won’t train on your inputs, which often points toward self-hosted or specific enterprise-grade API solutions.

**Trustworthiness** is also becoming important and can come down to the reputation and track record of the AI lab. A model that produces erratic, biased, or reputationally damaging outputs is a liability, regardless of its benchmark scores. For instance, Grok has had well-publicized issues with its alignment. Even if such issues are supposedly fixed, it creates a lingering question of trust: How can one be sure it won’t behave similarly in the future?

Additionally, the **knowledge cutoff date** also matters if it is to be used in a fast-moving field.

After working out if a model meets your minimum capability, the next decision is often on optimizing trade-offs among cost, reliability, security, and latency. A key rule of thumb we find useful here: If the reliability gain from a more expensive model or more inference time saves more of your or your users’ time (valued in terms of pay) than the model costs, going with the larger model is a good decision!

## **The Pros and Cons of Open-Weight and Closed-API LLMs**

The rise of increasingly competitive open-weight LLMs, such as Meta’s Llama series, Mistral, DeepSeek, Gemma, Qwen, and now OpenAI’s GPT-OSS has added a critical dimension to the model selection landscape. Momentum behind this open ecosystem surged with the release of DeepSeek’s R1 reasoning model, competitive with OpenAI’s o1 but priced at roughly 30x lower API **costs**. This sparked debate around efficiency versus scale and intensified the broader AI rivalry between China and the US. Reactions ranged from “OpenAI and Nvidia are obsolete” to “DeepSeek’s costs must be fabricated,” but regardless of hype, the release was a milestone. It showed that architectural innovation, not just scale, could deliver frontier-level performance with far greater cost efficiency.

This open-model offensive has continued with strong contributions from other Chinese labs like Alibaba (Qwen), Kimi, and Tencent (Hunyuan), and has put competitive pressure on Meta after its open-weight Llama models fell behind. China’s recent leadership in open-weight LLMs has raised new security/IP issues with some US- and European-based organizations, though we note accessing these model weights and running the model on your own infrastructure doesn’t require sending data to China.

This brings us back to the pros and cons of open weights. While closed-API LLMs still lead at the frontier of capability, the primary advantage of open-weight models is quick and affordable local testing, unparalleled flexibility, and increased data security when run internally. Organizations can also perform **full fine-tuning**, adapting the model’s core weights and behaviors to their specific domain, language, and tasks. Open models also provide **stability and predictability**—you control the version you deploy, insulating your production systems from unexpected changes or degradations that can sometimes occur with unannounced updates to proprietary API-based models.

Public closed-model APIs from major providers benefit from immense economies of scale and highly optimized GPU utilization by batching requests from thousands of users, an efficiency that is difficult for a single organization to replicate. This often means that using a closed-source API can be cheaper per inference than self-hosting an open model. Security and compliance are also more nuanced than they first appear. While some organizations must use self-hosted models to simplify compliance with regulations like GDPR by keeping data entirely within their own perimeter, this places the entire burden of securing the infrastructure on the internal team—a complex and expensive undertaking. Top API providers also often offer dedicated instances, private cloud endpoints, and contractual agreements that can guarantee data residency, zero-logging, and meet stringent regulatory standards. The choice, therefore, is not a simple open-versus-closed binary.

The boundary between open and closed models is also becoming increasingly blurred. Open-weight models are increasingly offered via API by third-party LLM inference platforms, combining the flexibility of open models with the simplicity of hosted access. This hybrid approach often strikes a practical balance between control and operational complexity.

## **Leading Closed LLMs**

Below, we present some key costs and metrics for leading closed-source models available via API. Many of these models have additional complexity and varied pricing including options for fast modes, thinking modes, context caching, and longer context.

We present the latest LiveBench benchmark score for each model as one measure for comparison. LiveBench is a continuously updated benchmark designed to provide a “contamination-free” evaluation of large language models by regularly releasing new questions with objective, verifiable answers. It scores models out of 100 on a diverse set of challenging tasks, with a significant focus on capabilities like reasoning, coding, and data analysis. The similar LiveBench scores between GPT-4.5 and 2.5 Flash-Lite, despite 750x input token cost variation, highlights both that smaller models are now very capable but also that not all capabilities are captured in a single benchmark!

https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing1.png_Source: Towards AI, Company Reports, [LiveBench AI](https://livebench.ai/)_

## **Leading open-weight LLMs**

Below, we also present key costs, the LiveBench benchmark score, and context length for leading open-weight models available via API. We compare hosted versions of these models for easy comparison. Different API providers may choose to host open-weight models with different levels of quantization, different context lengths, and different pricing, so performance can vary between providers.

https://www.oreilly.com/radar/wp-content/uploads/sites/3/2025/08/AI-Model-Pricing-and-Specifications.png_Source: Towards AI, Company Reports, [LiveBench AI](https://livebench.ai/)_

Whether hosted or self-deployed, selecting a model only solves part of the problem. In practice, most of the complexity and opportunity lies in how that model is used: how it’s prompted, extended, fine-tuned, or embedded within a broader workflow. These system-level decisions often have a greater impact on performance and cost than the model choice itself.

## **A Practical Guide to Designing an LLM System**

Simply picking the biggest or newest LLM is rarely the optimal strategy. A more effective approach starts with a deep understanding of the developer’s toolkit: knowing which technique to apply to which problem to achieve the desired capability and reliability without unnecessary cost. This is all part of the constant “ **march of nines” as you develop LLM systems modularly to solve for more reliability and capability.** There is a need to prioritize the easiest wins that deliver tangible value before investing in further incremental and often costly accuracy improvements. The reality will always vary on a case-by-case basis, but here is a quick guide to navigating this process.

### **Step 1: Open Versus Closed?**

This is often your first decision.

- **Go with a closed-API model (e.g., from OpenAI, Google, Anthropic) if:** Your priority is accessing the absolute state-of-the-art models with maximum simplicity.
- **Go with an open-weight model (e.g., Llama, Mistral, Qwen, DeepSeek) if:**
  - **Data security and compliance are paramount:** If you need to guarantee that sensitive data never leaves your own infrastructure.
  - **You need deep customization and control:** If your goal is to fine-tune a model on proprietary data and to create a specialized expert that you control completely.

If you went open, what can you _realistically_ run? Your own GPU infrastructure is a hard constraint. Assess your cluster size and memory to determine if you can efficiently run a large, leading 1 trillion+ parameter MoE model, such as Kimi K2, or if you are better served by a medium-size model such as Gemma 3 27B or a much smaller model like Gemma 3n that can even run on mobile.

### **Step 2: Gauging the Need for Reasoning**

Does your task require the model to simply blast out a response, or does it need to _think_ first?

- **Reasoning:** For tasks that involve complex, multistep problem-solving, brainstorming, strategic planning, intricate code generation, or deep analysis, you need a dedicated reasoning model such as o3, Gemini 2.5 Pro, DeepSeek R1, or Claude 4. In some cases these models can be used in high-reasoning mode, which encourages the model to think for longer before responding.
- **No reasoning:** For straightforward tasks like simple Q&A, summarization of a single document, data extraction, or classification, a powerful reasoning model is overkill.
- **The middle ground:** For tasks requiring moderate reasoning, such as generating a structured report from a few data points or performing basic data analysis at scale, a “mini” reasoning model, like OpenAI’s o4-mini or Gemini Flash 2.5, offers a balance of capability and cost.

### **Step 3: Pinpointing Key Model Attributes**

Beyond general intelligence and reasoning, modern LLMs are specialists. Your choice should be guided by the specific attributes and “superpowers” your application needs.

- **Prioritize accuracy over cost** for high-value tasks where mistakes are costly or where a human expert’s time is being saved. o3-pro is a standout model here and it can even be used as a fact checker to meticulously check the details of an earlier LLM output.
- **Prioritize speed and cost over accuracy:** For user-facing, real-time applications like chatbots or high-volume, low-value tasks like simple data categorization, latency and cost are paramount. Choose a hyper-efficient “flash” or “mini” model such as Gemini 2.5 Flash-Lite. Qwen3-235B models can also be a great option here but are too complex to inference yourself.
- **Do you need a deep, long-context researcher?** For tasks that require synthesizing information from massive documents, entire codebases, or extensive legal contracts, a model with a vast and highly effective context window is crucial. **Gemini 2.5 Pro** excels here.
- **Is multimodality essential?** If your application needs to understand or generate images, process audio in real time, or analyze video, your choice narrows to models like **GPT-4o** or the **Gemini** family. For one-shot YouTube video processing, Gemini is the standout.
- **Is it a code-specific task?** While many models can code, some are explicitly tuned for it. In the open world, Codestral and Gemma do a decent job. But Claude has won hearts and minds, at least for now.
- **Do you need live, agentic web search?** For answering questions about current events or topics beyond the model’s knowledge cutoff, consider a model with a built-in, reliable web search, such as **o3.**
- Do you need complex **dialogue and emotional nuance?** GPT-4.5, Kimi K2, Claude Opus 4.0, or Grok 4 do a great job.

### **Step 4: Prompting, Then RAG, Then Evaluation**

Before you dive into more complex and costly development, always see how far you can get with the simplest techniques. This is a path of escalating complexity. Model choice for RAG pipelines is often centered around latency for end users, but recently more complex agentic RAG workflows or long-context RAG tasks require reasoning models or longer context capabilities.

1.  **Prompt engineering first:** Your first step is always to maximize the model’s inherent capabilities through clear, well-structured prompting. Often, a better prompt with a more capable model is all you need.
2.  **Move to retrieval-augmented generation (RAG):** If your model’s limitation is a lack of specific, private, or up-to-date _knowledge_, RAG is the next logical step. This is the best approach for reducing hallucinations, providing answers based on proprietary documents, and ensuring responses are current. However, RAG is not a panacea. Its effectiveness is entirely dependent on the quality and freshness of your dataset, and building a retrieval system that consistently finds and uses the _most_ relevant information is a significant engineering challenge. RAG also comes with many associated decisions, such as the quantity of data to retrieve and feed into the model’s context window, and just how much use you make of long-context capabilities and context caching.
3.  **Iterate with advanced RAG:** To push performance, you will need to implement more advanced techniques like hybrid search (combining keyword and vector search), re-ranking retrieved results for relevance, and query transformation.
4.  **Build custom evaluation**: Ensure iterations on your system design, additions of new advanced RAG techniques, or updates to the latest model are always moving progress forward on your key metrics!

### **Step 5: Fine-Tune or Distill for Deep Specialization**

If the model’s core _behavior_—not its knowledge—is still the problem, then it’s time to consider fine-tuning. Fine-tuning is a significant undertaking that requires a high-quality dataset, engineering effort, and computational resources. However, it can enable a smaller, cheaper open-weight model to outperform a massive generalist model on a specific, narrow task, making it a powerful tool for optimization and specialization.

-   **Fine-tuning is for changing behavior, not adding knowledge.**Use it to teach a model a specific skill, style, or format. For example:
    -   To reliably output data in a complex, structured format like specific JSON or XML schemas.
    -   To master the unique vocabulary and nuances of a highly specialized domain (e.g., legal, medical).
    -   Some closed-source models are available for fine-tuning via API such as Gemini 2.5 Flash and various OpenAI models. Larger models are normally not available.
    -   **In open-weight models,** Llama 3.3 70B and Qwen 70B are fine-tuning staples. The process is more complex to fine-tune an open-weight model yourself.
-   Model **distillation** can also serve as a production-focused optimization step. In its simplest form, this consists of generating synthetic data from larger models to create fine-tuning datasets to improve the capabilities of smaller models.
-   **Reinforcement fine-tuning (RFT) for problem-solving accuracy**

Instead of just imitating correct answers, the model learns by trial, error, and correction. It is rewarded for getting answers right and penalized for getting them wrong.
  -   **Use RFT to:** Create a true “expert model” that excels at complex tasks with objectively correct outcomes.
  -   **The advantage:** RFT is incredibly data-efficient, often requiring only a few dozen high-quality examples to achieve significant performance gains.
  -   **The catch:** RFT requires a reliable, automated “grader” to provide the reward signal. Designing this grader is a critical engineering challenge.

### **Step 6: Orchestrated Workflows Versus Autonomous Agents**

The critical decision here is how much freedom to grant. Autonomous agents are also more likely to need more expensive reasoning models with greater levels of inference scaling. Parallel inference scaling methods with multiple agents are also beginning to deliver great results. Small errors can accumulate and multiply during many successive agentic steps so the investment in a stronger more capable model can make all the difference in building a usable product.

-   **Choose an orchestrated workflow for predictable tasks**

You design a specific, often linear, sequence of steps, and the LLM acts as a powerful component at one or more of those steps.
  -   **Use when:** You are automating a known, repeatable business process (e.g., processing a customer support ticket, generating a monthly financial summary). The goal is reliability, predictability, and control.
  -   **Benefit:** You maintain complete control over the process, ensuring consistency and managing costs effectively because the number and type of LLM calls are predefined.
-   **Build hybrid pipelines:**Often, the best results will come from combining many LLMs, open and closed, within a pipeline.
  -   This means using different LLMs for different stages of a workflow: a fast, cheap LLM for initial query routing; a specialized LLM for a specific subtask; a powerful reasoning LLM for complex planning; and perhaps another LLM for verification or refinement.
  -   At Towards AI, we often have 2-3 different LLMs from different companies in an LLM pipeline.
-   **Choose an autonomous agent for open-ended problems.**You give the LLM a high-level goal, a set of tools (e.g., APIs, databases, code interpreters), and the autonomy to figure out the steps to achieve that goal.
  -   **Use when:** The path to the solution is unknown and requires dynamic problem-solving, exploration, or research (e.g., debugging a complex software issue, performing deep market analysis, planning a multistage project).
  -   **The critical risk—runaway costs:** An agent that gets stuck in a loop, makes poor decisions, or explores inefficient paths can rapidly accumulate enormous API costs. **Implementing strict guardrails is critical:**
    -   **Budget limits:** Set hard caps on the cost per task.
    -   **Step counters:** Limit the total number of “thoughts” or “actions” an agent can take.
    -   **Human-in-the-loop:** Require human approval for potentially expensive or irreversible actions.
  -   Gemini 2.5 Pro and o3 are our favourite closed-API models for agent pipelines, while in open-weight models we like Kimi K2.

Working through these steps helps translate a vague problem into a concrete implementation plan, one that’s grounded in clear trade-offs and tailored to your needs. This structured approach often yields systems that are not only more capable and reliable but also far more effective for specific tasks than a general-purpose chatbot ever could be.

## **Conclusion**

The open-versus-closed race gives us rapid access to strong LLMs but also creates complexity. Selecting and deploying them demands both engineering discipline and economic clarity.

Developing in the LLM ecosystem demands a new level of engineering discipline and keen economic awareness. No single LLM is a cure-all. A practical, evolving toolkit is essential, but knowing which tool to pull out for which job is the real art. The challenge isn’t just picking a model from a list; it’s about architecting a solution. This requires a systematic approach, moving from high-level strategic decisions about data and security down to the granular, technical choices of development and implementation.

The success of specialized “LLM wrapper” applications like Anyscale/Cursor for coding or Perplexity for search, some of which are now valued at over $10 billion, underscores the immense value in this tailored approach. These applications aren’t just thin wrappers; they are sophisticated systems that leverage foundation LLMs but add significant value through custom workflows, fine-tuning, data integration, and user experience design.

Ultimately, success hinges on informed pragmatism. Developers and organizations need a sharp understanding of their problem space and a firm grasp of how cost scales across model choice, series and parallel reasoning, context usage, and agentic behavior. Above all, custom evaluation is non-negotiable because your use case, not a benchmark, is the only standard that truly matters.

</details>

<details>
<summary>Revisiting the Test-Time Scaling of o1-like Models</summary>

# Revisiting the Test-Time Scaling of o1-like Models

**Source URL:** <https://arxiv.org/html/2502.12215v1>

## Abstract

The advent of test-time scaling in large language models (LLMs), exemplified by OpenAI’s o1 series, has advanced reasoning capabilities by scaling computational resource allocation during inference. While successors like QwQ, Deepseek-R1 (R1) and LIMO replicate these advancements, whether these models truly possess test-time scaling capabilities remains underexplored. This study found that longer CoTs of these o1-like models do not consistently enhance accuracy; in fact, correct solutions are often shorter than incorrect ones for the same questions. Further investigation shows this phenomenon is closely related to models’ self-revision capabilities - longer CoTs contain more self-revisions, which often lead to performance degradation. We then compare sequential and parallel scaling strategies on QwQ, R1 and LIMO, finding that parallel scaling achieves better coverage and scalability. Based on these insights, we propose “Shortest Majority Vote”, a method that combines parallel scaling strategies with CoT length characteristics, significantly improving models’ test-time scalability compared to conventional majority voting approaches.

## 1 Introduction

The release of the OpenAI o1 series models marked a pivotal advancement in the reasoning capabilities of Large Language Models (LLMs), introducing a novel scaling paradigm, test-time scaling, which allocates more compute resources during test time. The test-time scaling has two dimensions, sequential and parallel. Sequential scaling increases test-time compute by scaling the length of Chain-of-Thought (CoT), while parallel scaling samples multiple solutions in parallel and picks the best one.

Following o1’s success, models such as QwQ, Deepseek-R1 (R1) and LIMO have emerged as leading open-source successors, replicating o1’s achievements and demonstrating comparable reasoning abilities. Although both QwQ, R1 and LIMO demonstrate strong reasoning capabilities and the ability to generate lengthy CoT at test time, the existence of true test-time scaling where performance consistently improves with longer CoTs remains to be verified for these models.

To explore this question, we systematically investigate the relationship between CoT length and reasoning performance in QwQ, R1 and LIMO, challenging the conventional assumption that extended reasoning chains inherently lead to improved accuracy. Contrary to expectations, our analysis reveals that longer CoTs do not consistently improve accuracy of these o1-like models. Notably, we found that the average length of correct solutions is shorter than that of incorrect ones for the same questions, which is shown in Image 1. This counterintuitive finding underscores the need for a deeper understanding of the test-time scaling of o1-like models.

To understand why the longer CoTs do not lead to the better performance, we compared the difference between long CoTs and short CoTs, finding that long CoTs contain more self-revisions (“Wait”, “Alternatively”) than the short CoTs, which is shown in Appendix E. Inspired by that, we iteratively prompted QwQ, R1 and LIMO for more self-revisions. Our observations revealed that QwQ and R1-Distill-1.5b exhibited performance degradation as the length of reflection increased. In contrast, R1-Distill-14b, R1-Distill-32b, and LIMO demonstrated initial performance improvements during early revisions, followed by oscillatory behavior in subsequent iterations. To further understand the limitations of sequential scaling, we evaluated the models’ capacity to revise incorrect answers. Our findings indicate that QwQ, R1 and LIMO all demonstrated limited ability to convert incorrect answers to correct ones during the revision process. Most revisions retained the original answers, and more concerning, both QwQ and R1-Distill-1.5b showed a higher propensity to change correct answers to incorrect ones rather than vice versa. These results reveal that self-revision ability is a key factor in the effectiveness of sequential scaling for o1-like models.

Given the limited effectiveness of sequential scaling, we explored an alternative test-time scaling strategy, parallel scaling. Our comparative analysis of sequential and parallel scaling revealed that parallel scaling not only achieves the better coverage (pass@k score) but also offers superior scalability compared to sequential scaling for QwQ and R1, which demonstrates that o1-like models have limited sequential-scaling capability, but strong parallel-scaling capability.

Building on these findings, we propose a novel test-time scaling method, Shortest Majority Vote, which incorporates parallel scaling approaches with our insight on sequential scaling. In particular, this method leverages the observation that shorter solutions tend to lead to better performance compared to longer ones. Shortest Majority Vote improves majority vote by prioritizing clusters that have both more solutions and shorter solution lengths. Experimental results demonstrate that Shortest Majority Vote substantially outperforms conventional Majority Vote, significantly improving the test-time scalability of both QwQ and R1 models.

Our contributions are as follows:

1. We systematically investigate the test-time scaling capabilities of o1-like models QwQ, R1 and LIMO, and find that their performance cannot be continuously improved through increasing CoT length.
2. We reveal that insufficient self-revision capability of o1-like models is the primary reason for their failure in sequential scaling.
3. We find that parallel scaling achieves better coverage and scalability than sequential revision for o1-like models.
4. Based on our insights into sequential and parallel scaling, we propose Shortest Majority Vote, a test-time scaling method that enhances majority voting by considering solution length, significantly outperforming traditional methods.

![Image 1: The average length of correct solutions versus incorrect solutions evaluated on the same questions. For each question, solution lengths were averaged separately for correct and incorrect responses, then averaged across all questions.](x1.png)

## 2 Related Work

The success of o1 has ushered in a new scaling paradigm, test-time compute scaling, which enables continuous improvements in model performance by increasing computational expenditure during inference. Currently, scaling test-time compute can be approached in two dimensions: parallel scaling and sequential scaling.

### Parallel Scaling

Parallel scaling typically samples multiple solutions in parallel and picks one according to some guidance signal like reward. Notable examples of parallel scaling include Best-of-N Search, which is based on a reward model, and Majority Vote, which exploits model uncertainty. The primary distinction between these approaches lies in the method used to select the final solution or answer after sampling multiple candidates. Both Best-of-N Search and Majority Vote are parallel scaling techniques at the solution level, while Tree-Search algorithms can be viewed as parallel scaling at the token or step level. Beam-Search and MCTS are classic examples of Tree-Search algorithms. All parallel scaling methods rely on guidance signals to select the optimal token, step, or solution from a set of candidates.

### Sequential Scaling

Sequential scaling enhances test-time computation by generating progressively longer solutions along the sequence dimension. The most prevalent method of sequential scaling is Self-Revision, where first generate an initial response and then iteratively evaluate and refine it based on self-assessment. In contrast, leverage external feedback—such as signals from a code execution environment—rather than self-evaluation to enhance solutions.

The effectiveness of sequential scaling with self-revision remains a contentious issue. argue that models cannot achieve effective self-refinement without external feedback. Conversely, some researchers posit that evaluating a solution’s correctness is inherently easier than generating a correct solution, suggesting that LLMs have the capacity for self-evaluation. show that it is possible to teach LLM to self-refine through reinforcement learning or supervised fine-tuning. compared various test-time scaling algorithms and found that when feedback accuracy exceeds 90%, Self-Revision outperforms Best-of-N Search.

### O1-like Models

The release of o1 has further underscored the significance of sequential scaling, as o1’s CoT length is substantially greater than that of conventional models. The research community has made significant efforts to reproduce the capabilities of o1, with QwQ and R1 and LIMO emerging as the most successful attempts. However, Our findings reveal that for R1 and QwQ, extending solution length does not necessarily yield better performance due to the models’ limited self-revision capabilities. Parallel findings by attribute this phenomenon to model underthinking, where models initially reach correct intermediate solutions but subsequently deviate toward incorrect conclusions during extended reasoning.

## 3 Experiment Setting

### Models

Our experiments involved models from the QwQ, LIMO and Deepseek-R1 series, including Deepseek-R1, Deepseek-R1-Distill-Qwen-32b, Deepseek-R1-Distill-Qwen-14b, and Deepseek-R1-Distill-Qwen-1.5b. For simplicity, we call these R1 models as R1-671b, R1-Distill-32b, R1-Distill-14b and R1-Distill-1.5b respectively. The models were run using SGLang framework, with the sampling temperature set to 0.7 and the maximum generation length set to 32k. We show the system prompt and instructions used for evaluation in Appendix D.

### Benchmark

We conducted comprehensive evaluations across four benchmarks: MATH-500, AIME, Omini-MATH, and GPQA. While MATH-500, AIME, and Omini-MATH focus on mathematical reasoning, GPQA encompasses broader scientific domains. For AIME evaluation, we utilized the AIMO validation set, comprising 90 questions from AIME 22, 23, and 24. Given the computational demands of evaluating the full Omini-MATH dataset (4.4K questions), we randomly sampled 500 questions to maintain efficiency. For GPQA, we focused on the diamond subset containing 198 questions. To ensure robust evaluation of answer correctness, we employed both the OpenCompass and Qwen Math evaluators, considering an answer correct if validated by either evaluator.

![Image 2: (a) Evaluation for Solution length.](x2.png)

## 4 The Failure of Sequential Scaling

### 4.1 Invalid Scaling of CoT Length: Longer CoTs Do not Improve Performance

To investigate whether the accuracy of QwQ, R1 and LIMO genuinely improves with increasing CoT length, we sampled each model five times on the same question and sorted the five solutions by length in ascending order. We grouped the solutions based on their rank in this sorted list, with the $i$-th ranked solutions forming a distinct group. For instance, all the longest solutions (rank 5) from different questions formed one group, while all the shortest solutions (rank 1) formed another, resulting in 5 comprehensive solution groups for analysis.

We present the average lengths of the five groups of solutions in Image 2(a). Since the grouping of solutions is based on their lengths, the differences in length between the groups are pronounced. The average length of the longest solutions is approximately twice that of the shortest solutions. This indicates that long-chain-of-thought (CoT) models like QwQ, R1 and LIMO exhibit a high diversity in the lengths of the solutions they sample.

There is no clear correlation between the length of solutions and the model’s size. For example, R1-Distill-1.5b produces the longest solutions while QwQ (32b) generates the shortest. A comparison of solution lengths across different datasets shows that solutions for simpler datasets, such as Math, are significantly shorter than those for more difficult datasets, like AIME. This suggests that the model adjusts the solution length based on the difficulty of the problem.

The accuracy of the five groups of solutions is presented in Image 2(b). Although there is a significant disparity in solution lengths across the groups, the differences in accuracy are much less pronounced. Notably, we do not observe a consistent improvement in accuracy for either QwQ or R1 as solution length increases. This trend holds true across all model variants as well as across all evaluated datasets. In some cases, we even observe an inverse scaling phenomenon, where accuracy decreases with increasing CoT length, especially on more difficult datasets like AIME and Omini-MATH. These findings cast doubt on the presumed test-time scaling capabilities of o1-like models, challenging the assumption that extended reasoning chains inherently yield superior problem-solving performance.

To make the relationship between CoT length and accuracy more clear, we compared the lengths of correct and incorrect solutions for the same question. First, we identified questions that had both correct and incorrect answers. For each of these questions, we calculated the average length of correct and incorrect solutions. We then averaged these values across all questions to determine the overall average length for correct and incorrect solutions. The results are shown in Image 1. We found that, for QwQ, R1 and LIMO, across all model sizes and datasets, the length of correct solutions is consistently shorter than that of incorrect solutions. This observation suggests that longer CoTs do not necessarily lead to better performance and may even be associated with lower accuracy. Moreover, we observed that for weaker models, such as QwQ and R1-Distill-1.5B, the gap in solution length between correct and incorrect solutions is significantly larger than for stronger models, such as R1-671b. This suggests that the invalid scaling phenomenon is more pronounced in the weaker models.

### 4.2 Explaining Invalid Scaling: The Key Factor is the Failure of Self-Revision

![Image 3: (a) Max Token Limitation](x4.png)

In Section 4.1, we observed the phenomenon that long solutions exhibit lower accuracy compared to short solutions. In this section, we investigate the underlying reasons for this phenomenon. We first analyzed how the maximum token limitation affects generation performance and confirmed that the observed invalid scaling phenomenon was not caused by constraints in the maximum token length. Next, we examined the differences between long and short solutions, finding that long solutions exhibit a higher frequency of self-revision. Moreover, our analysis suggests a strong correlation between self-revision, solution length, and accuracy.

#### Max Token Limitation

The max token limitation parameter controls the maximum number of tokens a model can generate for a question, which plays a critical role in influencing model accuracy, especially when generating long solutions. To explore its impact, we tested several max token limitation values and compared the performance of QwQ, R1 and LIMO on the AIME benchmark. The results are shown in Image 3(a), which revealed that 16k is a key threshold: when the max token limitation is below this value, it significantly affects the model performance. However, increasing the max token limitation beyond 16k leads to diminishing returns, particularly for QwQ. In our other experiments, we set the max token limitation to 32k, suggesting that this parameter is not the main cause of invalid scaling.

#### Difference between Short and Long CoT

To understand why long solutions of QwQ, R1 and LIMO is not better than short solutions, we analyzed their differences. We observed that QwQ, R1 and LIMO all primarily extend solution length through self-revision, characterized by markers such as “Wait” and “Alternatively”. We show some examples of that in Appendix E. To quantify this phenomenon, we counted the occurrences of “wait” in solutions of QwQ, R1 and LIMO in Image 3(b). The results demonstrates a strong linear correlation between solution length and the frequency of self-correction markers for all models. This suggests that the mechanisms of self-revision may play a significant role in generating longer solutions.

![Image 4: (a) Acc of R1-Distill-32b, 14b and LIMO](x6.png)

![Image 5: The ratio of turning an initial correct answer to incorrect one (correct to wrong) and an initial incorrect answer to a correct one (wrong to correct) during sequential scaling.](x9.png)

#### Scaling Solution Length with Self-Revision

We have tried to investigate the revision behaviors inside the sampled solutions, however, it is difficult to extract the initial solution and the following revision exactly from QwQ, R1 and LIMO’s solutions. Alternatively to that, we prompted the models to continue thinking based on their sampled solutions.

QwQ, R1 and LIMO often conclude their solutions with phrases like “final answer: …”, and R1 additionally outputs a ‘</think>’ tag followed by a final response. To facilitate smoother continuation of the reasoning process, we removed the “final answer” portion from the solutions. We then used the keyword “Wait” or “Alternatively” as the prompt to encourage self-revision. We calculated the probabilities of the model predicting the next token as “Wait” or “Alternatively” and selected the one with the higher probability as the prompt.

We prompted QwQ, R1 and LIMO to continue reasoning for 40 additional steps on the AIME benchmark. We show the results in Image 4(c), from which we observe that the solution length increase almost linearly with additional steps. After 40 steps, the solution length of QwQ and R1 is almost third as their original length.

We show the accuracy after sequential revision in Image 4(a) and 4(b). Our results reveal that the accuracy of QwQ and R1-Distill-1.5b decreases constantly as the number of reasoning steps increases, while the accuracy of R1-Distill-32b, R1-Distill-14b and LIMO initially improves and then oscillates with further reasoning steps. Further analysis in Appendix B reveal that the improvement on R1-Distill-32b, R1-Distill-14b and LIMO during revisions mainly comes from the revision on short solutions. These results corroborate our previous experimental findings, suggesting that longer solutions do not improve performance, especially for weaker models such as QwQ and R1-Distill-1.5b. These findings suggest that the reason why longer solutions do not consistently lead to better performance in QwQ, R1 and LIMO may lie in the failure of self-revision.

#### Investigating Self-Revision Behavior

To further investigate the effectiveness of self-revision, we analyzed the proportion of cases where the model corrected an initial incorrect answer to a correct one versus changing an initial correct answer to an incorrect one during scaling solution length. We found that, the proportions of changing a incorrect answer to an correct one is extremely low, always below 10%. Notably, for QwQ and R1-Distill-1.5b, the proportion of changing a correct answer to an incorrect one was even higher than that of correcting an incorrect answer to a correct one. This observation helps explain why prompting QwQ and R1-Distill-1.5b to continue reasoning led to a decrease in accuracy. For simplicity, we call the proportions of changing a incorrect answer to an correct one as the successful-revision rate, while the reverse as the failed-revision rate.

Although R1-Distill-32b, R1-Distill-14b and LIMO exhibit a higher successful-revision rate than failed-revision rate, the increase of successful-revision rate plateaus after approximately 10 steps, with further revisions providing no additional benefits. This observation explains why their accuracy during sequential scaling initially increases with multiple rounds of revision but later stabilizes with fluctuations.

Table 1: The proportion of the revisions that models stick to the original wrong answers.

| R1-32b | R1-14b | R1-1.5b | QwQ | LIMO |
|---|---|---|---|---|
| 72% | 70% | 58% | 32% | 54% |

![Image 6: (a) Evaluation on Coverage.](x10.png)

The successful-revision rate of QwQ, R1 and LIMO are all below 10%, what is the outcome of the model’s self-revision in unsuccessful cases? We hypothesize that, in most instances, the model simply keeps its original answer unchanged. To validate that, we computed the proportion of instances where the model persists with its original answer, even when it is incorrect, and the results were as expected. As shown in Image 5, when the original answer is wrong, both R1-Distill-32b and R1-Distill-14b maintain the original answer in over 70% of cases. Although retaining the original answer does not reduce accuracy, it also makes the scaling solution length ineffective. This phenomenon suggests that the model’s ability to early stop may also be a critical factor influencing whether its performance improves with an increasing solution length.

The above analysis indicates that the key factor determining whether o1-like models’ performance improve with an increase in solution length is their ability to self-revise. The model’s accuracy increases with the more incorrect answers revised to correct and vice versa.

![Image 7: Parallel-scaling performance of Majority Vote, Shortest and Shortest Majority Vote on AIME.](x12.png)

## 5 Sequential Scaling vs. Parallel Scaling

Based on our experimental findings presented in Section 4.2, sequential scaling demonstrates limited effectiveness for QwQ, R1 and LIMO. An alternative approach to scaling test-time compute is parallel scaling, which generates multiple solutions in parallel and selects the best one as the final answer.

We compared the performance of sequential scaling and parallel scaling in terms of the coverage (pass@k score) and accuracy of QwQ and R1, which are shown in Image 6(a) and 6(b) respectively. For sequential scaling, we iteratively prompt models to self-revise for 40 steps. While for parallel scaling, we parallely sample 10 solutions. The coverage is evaluated by counting the proportion of whether multiple candidate answers contain a correct one. In parallel scaling, coverage increases by one if at least one sampled solution is correct. Similarly, in sequential scaling, coverage increases by one if at least one revision iteration succeeds.

Our findings show that, for the same number of generated tokens, parallel scaling provides a significantly larger improvement in coverage compared to sequential scaling, for both R1-Distill-32b and QwQ. However, a practical parallel scaling method must select a final answer from a set of candidate answers. We implement parallel scaling using majority vote and sequential scaling by taking the answer from the last revision as the final answer. Since majority voting requires at least three solutions to be effective, it does not provide any benefit when scaling the number of solutions from 1 to 2. In contrast, sequential revision is effective for R1-Distill-32b when scaling the number of tokens to 10k, but further scaling does not yield additional benefits. Additionally, because sequential scaling involves attention over a longer context, its computational cost is much higher than that of parallel scaling when generating the same number of tokens.

## 6 Application of Our Findings: Shortest Majority Vote

Table 2: Performance comparison between Majority Vote (MV), Shortest and Shortest Majority Vote (Shortest MV) on AIME and GPQA, when there are 2 and 16 solutions sampled.

| Model | Solutions | AIME MV | AIME Shortest | AIME Shortest MV | GPQA MV | GPQA Shortest | GPQA Shortest MV |
|---|---|---|---|---|---|---|---|
| R1-Distill-32b | 2 | 59.77 | 62.22 | 62.22 | 61.41 | 62.52 | 62.52 |
| R1-Distill-14b | 2 | 58.88 | 60.44 | 60.44 | 51.21 | 52.32 | 52.32 |
| R1-Distill-1.5b | 2 | 24 | 27.55 | 27.55 | 15.25 | 15.35 | 15.35 |
| QwQ | 2 | 41.77 | 40.22 | 40.22 | 58.05 | 57.02 | 57.02 |
| LIMO | 2 | 56.66 | 60.88 | 60.88 | 50.46 | 54.56 | 54.56 |
| R1-Distill-32b | 16 | 72.88 | 61.99 | 73.77 | 63.33 | 61.21 | 63.53 |
| R1-Distill-14b | 16 | 71.77 | 62.00 | 71.55 | 56.16 | 56.66 | 56.46 |
| R1-Distill-1.5b | 16 | 40.00 | 26.22 | 42.22 | 29.59 | 27.77 | 30.20 |
| QwQ | 16 | 51.33 | 40.88 | 50.88 | 62.25 | 56.82 | 62.25 |
| LIMO | 16 | 68.88 | 62.22 | 70.00 | 55.58 | 50.15 | 55.89 |

Given the limitation of sequential scaling of the current o1-like models, we turn to parallel scaling techniques and incorporate it with our insight on sequential scaling. Specifically, we propose a new Parallel Scaling algorithm: Shortest Majority Vote. Shortest Majority Vote is an extension of Majority Vote, but it accounts for the length of the solutions generated by the model. In the original Majority Vote, solutions with the same answer are grouped into a single category, and the number of solutions in each category is counted, with the answer corresponding to the category with the most solutions selected as the final answer. In contrast, Shortest Majority Vote not only counts the number of solutions in each category, but also computes the average length of the solutions in each category. Let the number of solutions in the $i$-th category be $c_i$ and the average solution length in that category be $l_i$. The score for category $i$ in Shortest Majority Vote is computed as:

$$
s_i = \frac{c_i}{\log{l_i}} \quad (1)
$$

and the final answer is chosen from the category with the highest score. The score $s_i$ is designed with the assumption that the correct answer is more likely to appear in categories with a larger number of solutions and shorter solution lengths. Shortest Majority Vote offers two key advantages: first, it is particularly effective for some o1-like models, where performance deteriorates with increasing solution length; second, it enables the use of solution length as a guidance signal for identifying superior solutions when candidate solutions are limited, especially in cases where conventional Majority Vote becomes ineffective due to having only two candidate solutions.

We evaluated the performance of Shortest Majority Vote and Majority Vote through experiments on the AIME and GPQA benchmarks, sampling 16 solutions from QwQ, R1 and LIMO models. We implemented a simple baseline approach, denoted as "Shortest," which selects the answer from the solution with the minimal length. The experimental results are presented in Table 2 and Image 7. Table 2 demonstrates that Shortest Majority Vote significantly outperforms both Majority Vote and Shortest methods, particularly on the AIME benchmark. Image 7 illustrates the parallel-scaling performance of these three methods, showing that as the number of generated tokens increases, Shortest Majority Vote maintains superior performance over both alternatives on AIME. The corresponding parallel-scaling results for GPQA are provided in Appendix C. Notably, while Shortest performs better than Majority Vote when only two solutions are sampled, it exhibits inferior performance in all other scenarios. These empirical findings strongly support the effectiveness of the Shortest Majority Vote approach.

## 7 Conclusion

In this study, we challenged the assumption that o1-like models like QwQ and R1 models have test-time scaling capability. We found that shorter solutions often outperform longer ones, and that sequential scaling through self-revision has limited effectiveness. Based on these insights, we developed Shortest Majority Vote, a parallel scaling method that considers solution length, which significantly outperformed traditional majority vote.

## Limitations

1. Given the considerable cost of R1-671b, evaluation on it was limited to the experiments in Images 1 and 2, whereas distilled R1 was utilized for all subsequent experiments.
2. Our experimental framework was limited to static model checkpoints. Future research should investigate test-time scaling behavior using dynamic checkpoints in reinforcement learning settings.
3. While the proposed shortest majority method may have limited applicability for models with strong sequential-scaling capabilities, solution length remains a valuable guidance signal for candidate selection in parallel scaling scenarios. The method can be adapted to a Longest Majority Vote variant for such cases.

## Ethics Statement

This paper honors the ACL Code of Ethics. The dataset used in the paper does not contain any private information. All data and tools used in this study comply with their respective licenses and terms of use.

## Appendix A Is Invalid Scaling Phenomenon Conflict to Findings of R1 technique Report?

The training objective of R1 aims to improve model accuracy, yet we observe that correct solutions tend to be shorter than incorrect ones. This raises an intriguing question: Why does R1’s reinforcement learning (RL) training consistently produce longer solutions?

To investigate this phenomenon, we analyzed five solutions per question, organizing them into groups by length in ascending order. Image 8 illustrates the distribution of correct solutions across these groups.

Our analysis revealed that correct solutions predominantly appear in shorter-length groups, particularly in the AIME dataset. However, when examining the token distribution, we found that correct solution tokens are concentrated in longer-solution groups. This apparent contradiction arises because the total token count is determined by both the number of solutions and the average tokens per solution. As shown in Image 2(a), solutions in the longest group contain nearly twice as many tokens as those in the shortest group. This explains why, despite having fewer individual solutions, longer solutions account for a greater share of the total tokens.

We hypothesize that this discrepancy explains why RL training tends to produce longer solutions: the training process may favor generating longer solutions, even if they are less accurate, because they contribute more tokens to the gradient.

![Image 8: The number of correct solutions and tokens distributed across groups of different lengths.](x13.png)

![Image 9: (a) R1-Distill-32b](x14.png)

![Image 10: Performance Comparison between Majority Vote and Shortest Majority Vote on GPQA.](x17.png)

## Appendix B Further analysis on Sequential Scaling on R1-Distill-14b, R1-Distill-32b and LIMO

In Section 4.2, we observed that R1-Distill-14b, R1-Distill-32b and LIMO demonstrated some performance improvements after multiple rounds of self-revision, followed by stabilization. Furthermore, in Section 4.1, we found that the correct solutions generated by R1-Distill-14b, R1-Distill-32b and LIMO were generally shorter than incorrect solutions. To reconcile these seemingly contradictory findings and further analyze how R1-Distill-14b, R1-Distill-32b and LIMO benefit from self-revision, we conducted a detailed analysis of self-revision outcomes on both long and short solutions. Our methodology for collecting long and short solutions involved sampling five solutions for each question, ordering them by length, and then segregating the longest and shortest solutions into separate groups. The results of self-revision on both short and long solutions are presented in Image 9. Our analysis reveals that short solutions exhibited significant performance improvements following self-revision, while this trend was less pronounced for long solutions. Therefore, the performance improvements we observed through self-revision in R1-Distill-14b, R1-Distill-32b and LIMO primarily stem from the self-revision on short solutions. This suggests that the relationship between accuracy and solution length for these models is complex, demonstrating neither a strictly positive nor negative correlation with length.

## Appendix C Parallel Scaling of Shortest Majority Vote on GPQA

In Section 6, we demonstrated that our proposed Shortest Majority Vote achieves superior test-time scaling performance compared to the other two methods on the AIME benchmark. In this section, we present the parallel-scaling results on GPQA in Image 10. While Shortest Majority Vote consistently outperforms the Shortest method on GPQA, it does not exhibit significantly better parallel scaling performance compared to Majority Vote on this benchmark. This phenomenon might be attributed to the smaller performance gap between short and long solutions on GPQA compared to AIME, suggesting that solution length plays a less critical role in determining solution quality on the GPQA benchmark, which can be observed from Image 2(b).

## Appendix D Prompt

System prompt:

Instruction for MATH-500, AIME and Omini-MATH:

Instruction for GPQA:

## Appendix E Examples of self-revision

</details>

<details>
<summary>What is the Model Context Protocol (MCP)?</summary>

# What is the Model Context Protocol (MCP)?

**Source URL:** <https://modelcontextprotocol.io/docs/getting-started/intro>

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

https://mintcdn.com/mcp/bEUxYpZqie0DsluH/images/mcp-simple-diagram.png?fit=max&auto=format&n=bEUxYpZqie0DsluH&q=85&s=35268aa0ad50b8c385913810e7604550

## What can MCP enable?

- Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
- Claude Code can generate an entire web app using a Figma design.
- Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
- AI models can create 3D designs on Blender and print them out using a 3D printer.

## Why does MCP matter?

Depending on where you sit in the ecosystem, MCP can have a range of benefits.

- **Developers**: MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
- **AI applications or agents**: MCP provides access to an ecosystem of data sources, tools and apps which will enhance capabilities and improve the end-user experience.
- **End-users**: MCP results in more capable AI applications or agents which can access your data and take actions on your behalf when necessary.

## Broad ecosystem support

MCP is an open protocol supported across a wide range of clients and servers. AI assistants like [Claude](https://claude.com/docs/connectors/building) and [ChatGPT](https://developers.openai.com/api/docs/mcp/), development tools like [Visual Studio Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Cursor](https://cursor.com/docs/context/mcp), [MCPJam](https://docs.mcpjam.com/getting-started), and many others all support MCP — making it easy to build once and integrate everywhere.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="gemini-review.md">
<details>
<summary>Gemini Review</summary>

Phase: [EXPLOITATION]

# Gemini Review

**Source URL:** <https://gemini.google/overview/deep-research/>

Save hours of work with Deep Research as your personal research assistant. Now with the ability to draw context from your Gmail, Drive and even Chat in addition to the web, and transform reports into interactive content in Canvas.

## What is Deep Research

Get up to speed on just about anything with Deep Research, an agentic feature in Gemini that can automatically browse up to hundreds of websites and even your Gmail, Drive and Chat on your behalf, think through its findings, and create insightful multi-page reports in minutes.

With the Gemini 3 model, Deep Research is even better at all stages of research, from planning to delivering even more insightful and detailed reports.

### Planning

Deep Research transforms your prompt into a personalized multi-point research plan

### Searching

Deep Research autonomously searches and deeply browses the web and your Gmail, Drive, and Chat if you choose so, to find relevant, up-to-date information

### Reasoning

Deep Research shows its thoughts as it reasons over information gathered iteratively and thinks before making its next move

### Reporting

Deep Research provides comprehensive custom research reports with more detail and insights, generated in minutes and available as an Audio Overview, saving you hours of time

## How to use Deep Research

Gemini Deep Research is designed to tackle your complex research tasks by breaking them down, exploring sources like across the web, and your Workspace content if you choose it, to find answers, and synthesizing findings into comprehensive results.

You can also upload your own files to Deep Research, and make your reports even more immersive by turning them into interactive content, quizzes, Audio Overviews, and more in Canvas.

### Competitive analysis

Build a competitor report that cross-references public web data with your internal strategy memos, feature-comparison spreadsheets, and team chats about a rival product.

### Due diligence

Investigating a potential sales lead, analyzing a company's products, funding history, team and competitive environment, and merging it with your own notes in Workspace on the client relationship.

### Topic understanding

Diving deep into subjects by comparing and contrasting key concepts, identifying relationships between ideas and explaining underlying principles.

### Product comparison

Evaluating different models of an appliance based on features, performance, price and customer reviews.

It’s a step towards more agentic AI that can move beyond simple question-answering to become a true collaborative partner capable of sophisticated thinking and execution.

## How we built the first Deep Research

The day after we pioneered the Deep Research product category on Gemini in December 2024, we gathered some of the team behind the product for a discussion.

Gemini Deep Research Roundtable \| A conversation with the Google engineers who built it - YouTube

Tap to unmute

### An agentic system

To build Deep Research, we developed a new planning system that enables Gemini app to work through complex problems. For Deep Research, we trained Gemini models to be capable of:

- **Breaking down the problem:** When presented with a complex user query, the system first formulates a detailed research plan, breaking the problem into a series of smaller, manageable sub-tasks. You’re in control of the plan: Gemini presents it to you, and you can refine it to make sure it’s focused on the right areas.

- **Research**: The model oversees the execution of this plan, and intelligently determines which sub-tasks can be tackled simultaneously and which need to be done sequentially. The model can use tools like search and web browsing to fetch information & reason over it. At each step the model reasons over information available to decide its next move. We introduced a thinking panel for users to follow what the model has learnt so far & what it intends to do next.

- **Synthesis:** Once the model determines enough information has been gathered, it synthesizes the findings into a comprehensive report. In building the report, Gemini critically evaluates the information, identifies key themes and inconsistencies, and structures the report in a logical and informative way, even performing multiple passes of self-critique to enhance clarity and detail.

### New category, new problems, new solutions

In building Deep Research, we had to work through three significant technical challenges:

#### Multi-step planning

Research tasks require multiple steps of iterative planning. At each step, the model has to ground itself on all information gathered so far, then identify missing information and discrepancies it wants to explore — all while trading off comprehensiveness with compute and user wait time. Training the model to be effective at long multi-step planning in a data efficient manner enabled us to make Deep Research function in an open domain setting across all topics.

#### Long-running inference

A typical Deep Research task involves many model calls over several minutes. This creates a challenge for building agents: It has to be built so that a single failure doesn’t mean having to restart the task from the beginning.

To address this, we developed a novel asynchronous task manager that maintains a shared state between the planner and task models, allowing for graceful error recovery without restarting the entire task. This system is truly asynchronous: you can hop to a different app or quite literally turn off your computer after starting a Deep Research project and the next time you visit Gemini, you’ll get notified when your research is done.

#### Context management

Over the course of a research session, Gemini can process hundreds of pages of content. To maintain continuity and enable follow-up questions, we use Gemini’s industry-leading 1 million token context window complemented with a RAG setup. This effectively allows the system to "remember" everything it has learned during that chat session, making it smarter the longer you interact with it.

### Evolving with new models

When Deep Research launched in December it was powered by Gemini 1.5 Pro. With the introduction of Gemini 2.0 Flash Thinking (experimental) we were able to dramatically improve both the quality and serving efficiency of this product. With thinking models, Gemini takes more time to plan out its approach before it makes its next steps. This innate characteristic of self-reflection and planning makes it a great fit for these kinds of long running agentic tasks. What we see is that now Gemini is even better at all stages of research and delivers more detailed reports. At the same time, the compute-efficiency of the Flash model allows us to expand access to Deep Research to far more users. We’re really excited about developing on flash and thinking models in general and expect deep research to keep getting better and better.

And with our most capable model, Gemini 3, Deep Research is even better at all stages of research, delivering even more insightful and detailed reports

### What’s next

We built the system to be versatile, so over time we can expand its capabilities by giving you more control over what it can browse and giving it sources beyond the open web.

We are excited to see how people use Deep Research, and these real-world experiences will inform how we continue to build and improve Deep Research. Ultimately, our goal is a truly agentic and universally helpful AI assistant.

## **Agentic** Gemini

https://lh3.googleusercontent.com/DlBS8h563Tyrf7u-yBxcC5HoGsl1lLRhO53NXk1Ka17zsh36Qs-pW4BtEdCH4ZLoZmy9MQLosCnR9uRdrth9e0Om47m9x-gZMPHj=e365-pa-nu-s0

Reason

https://lh3.googleusercontent.com/7JtrBnfXenPU4osp7fQMr4pZyWnzShlcmpfMyLIYI9moIKHk4U09Kl4v3IJMd4CDYmGjpFKgEne6D7xJsYV_n__a9PrtsxbgKR66=e365-pa-nu-s0

Search

https://lh3.googleusercontent.com/_gcKbFZF22t4T3a8bQyti8Li5T5HpgQfgbZ0IIddBf1PESOMv-vEvJFYNrhEM13lmHwqj1Zf3YQ_KFDvjh-0VdIbONkVU3l2sRQ=e365-pa-nu-s0

Browse

Gemini’s **new agentive AI system** brings together the **best of Gemini, Google Search, and web technologies** to continuously search, browse, and think through information in a continuous reasoning loop for more comprehensive results.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="intro-to-perplexity.md">
<details>
<summary>Intro to Perplexity</summary>

Phase: [EXPLOITATION]

# Intro to Perplexity

**Source URL:** <https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research>

Written by

Perplexity Team

Published on

Feb 14, 2025

# Introducing Perplexity Deep Research

**Today we’re launching Deep Research** to save you hours of time by conducting in-depth research and analysis on your behalf. When you ask a Deep Research question, Perplexity performs dozens of searches, reads hundreds of sources, and reasons through the material to autonomously deliver a comprehensive report. It excels at a range of expert-level tasks—from finance and marketing to product research—and attains high benchmarks on Humanity’s Last Exam.

We believe everyone should have access to powerful research tools. That’s why we’re making Deep Research free for all. Pro subscribers receive a high volume of Deep Research queries, while non-subscribers will have access to a limited number of answers per day. Deep Research is available on Web starting today and will soon be rolling out to iOS, Android, and Mac. (Be sure update your apps to the latest version.)

To give it a try, go to [perplexity.ai and select “Deep Research”](https://www.perplexity.ai/?model_id=deep_research) from the mode selector in the search box before submitting your query.

### How It Works

Perplexity already excels at answering questions. Deep Research takes question answering to the next level by spending 2-4 minutes doing the work it would take a human expert many hours to perform. Here’s how it works:

- **Research with reasoning** \- Equipped with search and coding capabilities, Perplexity’s Deep Research mode iteratively searches, reads documents, and reasons about what to do next, refining its research plan as it learns more about the subject areas. This is similar to how a human might research a new topic, refining one’s understanding throughout the process.

- **Report writing** \- Once the source materials have been fully evaluated, the agent then synthesizes all the research into a clear and comprehensive report.

- **Export & Share** \- You can then export the final report to a PDF or document, or convert it into a Perplexity Page and share it with colleagues or friends.


https://framerusercontent.com/images/Lc0634aprN2JYuFLQ8VfKthJnAk.png

### When to Use Deep Research

We built Deep Research to empower everyone to conduct expert-level analysis across a range of complex subject matters. Deep Research excels at creating work artifacts in domains including finance, marketing, and technology, and is equally useful as a personal consultant in areas such as health, product research, and travel planning. Here are a a few examples of how you might use Deep Research on Perplexity.

#### Finance

https://framerusercontent.com/images/trzwsXtuC3j68cIGyUb6k2lLk.png

#### Marketing

https://framerusercontent.com/images/n8ptzcWQs7qIv7JiMDS1ZwJmKA.png

#### Technology

https://framerusercontent.com/images/wRBHkQ4dqR8tLeYql0DyOUdh78.png

#### Current Affairs

https://framerusercontent.com/images/wug2dVncsmdZqLMr6KElOCtglhc.png

#### Health

https://framerusercontent.com/images/Sqc4r85ACZIQZTzC2pJhe1BCQYc.png

#### Biography

https://framerusercontent.com/images/tQO9LIHgnWvalzwrgmmLCVzqT4.png

#### Travel

https://framerusercontent.com/images/ofWFPGvvrYQWaFAr6BOBwOIvpk.png

### Humanity’s Last Exam

Deep Research on Perplexity attains a 21.1% accuracy score on Humanity’s Last Exam, significantly higher than Gemini Thinking, o3-mini, o1, DeepSeek-R1, and many other leading models. [Humanity’s Last Exam⁠](https://lastexam.ai/) is a comprehensive benchmark for AI systems consisting of over 3,000 questions across 100+ subjects ranging from mathematics and science to history and literature.

https://framerusercontent.com/images/hplibuiapLcxAxdbJQWfhnLmiJU.png

### SimpleQA

Scoring 93.9% accuracy on the [SimpleQA](https://arxiv.org/html/2411.04368v1) benchmark — a bank of several thousand questions that test for factuality — Perplexity Deep Research far exceeds the performance of leading models.

https://framerusercontent.com/images/ttftsapj52NTVpjPcXVOj8JfKw.png

### Runtime Stats

Deep Research on Perplexity not only attains high scores on industry benchmarks, but it does so while completing most research tasks in under 3 minutes — which we’re working to make even faster in the future.

https://framerusercontent.com/images/enepaQzuMoqWmDzgU6x5D9ydTqc.png

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="lost-in-the-middle-how-language-models-use-long-contexts.md">
<details>
<summary>Lost in the Middle: How Language Models Use Long Contexts</summary>

**Source URL:** <https://arxiv.org/abs/2307.03172>

# Lost in the Middle: How Language Models Use Long Contexts 

Nelson F. Liu 1∗ Kevin Lin 2 John Hewitt 1 Ashwin Paranjape 3

Michele Bevilacqua 3 Fabio Petroni 3 Percy Liang 11Stanford University 2University of California, Berkeley 3Samaya AI 

nfliu@cs.stanford.edu 

Abstract 

While recent language models have the abil-ity to take long contexts as input, relatively little is known about how well they use 

longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their in-put contexts: multi-document question an-swering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant informa-tion, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when rele-vant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models. 

1 Introduction 

Language models have become an important and flexible building block in a variety of user-facing language technologies, including conversational interfaces, search and summarization, and collabo-rative writing (Shuster et al., 2022; Thoppilan et al., 2022; Lee et al., 2022, inter alia ). These models perform downstream tasks primarily via prompting: all relevant task specification and data to process is formatted as a textual input context, and the model returns a generated text completion. These input contexts can contain thousands of tokens, espe-cially when language models are used to process long documents (e.g., legal or scientific documents, conversation histories, etc.) or when language mod-els are augmented with external information (e.g.,     

> *Work partially completed as an intern at Samaya AI. 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-0613 (closed-book)

Figure 1: Changing the location of relevant information (in this case, the position of the passage that answers an input question) within the language model’s input con-text results in a U-shaped performance curve—models are better at using relevant information that occurs at the very beginning (primacy bias) or end of its input context (recency bias), and performance degrades significantly when models must access and use information located in the middle of its input context. 

relevant documents from a search engine, database query results, etc; Petroni et al., 2020; Ram et al., 2023; Shi et al., 2023; Mallen et al., 2023; Schick et al., 2023, inter alia ). Handling these use-cases requires language mod-els to successfully operate over long sequences. Ex-isting language models are generally implemented with Transformers (Vaswani et al., 2017), which re-quire memory and compute that increases quadrat-ically in sequence length. As a result, Trans-former language models were often trained with relatively small context windows (between 512-2048 tokens). Recent improvements in hardware (e.g., faster GPUs with more memory) and algo-rithms (Dai et al., 2019; Dao et al., 2022; Poli et al., 

> arXiv:2307.03172v3 [cs.CL] 20 Nov 2023

2023; Rubin and Berant, 2023, inter alia ) have resulted in language models with larger context windows (e.g., 4096, 32K, and even 100K tokens), but it remains unclear how these extended-context language models make use of their input contexts when performing downstream tasks. We empirically investigate this question via controlled experiments with a variety of state-of-the-art open (MPT-30B-Instruct, LongChat-13B (16K)) and closed (OpenAI’s GPT-3.5-Turbo and Anthropic’s Claude-1.3) language models in set-tings that require accessing and using information within an input context. In particular, our experi-ments make controlled changes to the input context size and the position of the relevant information within the input context and study their effects on language model performance. If language models can robustly use information within long input con-texts, then their performance should be minimally affected by the position of the relevant information in the input context. We first experiment with multi-document ques-tion answering, which requires models to reason over provided documents to find relevant informa-tion and use it to answer a given question; this task mimics the retrieval-augmented generation setup underlying many commercial generative search and question answering applications (e.g., Bing Chat). In this setting, we control (i) the input context length by changing the number of documents in the input context (akin to retrieving more or less documents in retrieval-augmented generation), and (ii) control the position of the relevant information within the input context by changing the order of the documents to place the relevant document at the beginning, middle or end of the context. We find that changing the position of relevant information in the input context can substantially affect model performance, indicating that current language models do not robustly access and use information in long input contexts. Furthermore, we observe a distinctive U-shaped performance curve (Figure 1); language model performance is highest when relevant information occurs at the very beginning (primacy bias) or end of its in-put context (recency bias), and performance sig-nificantly degrades when models must access and use information in the middle of their input con-text (§2.3). For example, when relevant infor-mation is placed in the middle of its input con-text, GPT-3.5-Turbo’s performance on the multi-document question task is lower than its perfor-mance when predicting without any documents (i.e., the closed-book setting; 56.1%). Furthermore, we find that models often have identical performance to their extended-context counterparts, indicating that extended-context models are not necessarily better at using their input context (§2.3). Given that language models struggle to retrieve and use relevant information in the multi-document question answering task, to what extent can lan-guage models even retrieve from their input con-texts? We study this question with a synthetic key-value retrieval task, which is designed to be a mini-mal testbed for the basic ability to retrieve matching tokens from the input context. In this task, models are given a collection of JSON-formatted key-value pairs and must return the value associated with a specific key. Similar to the multi-document QA task, the key-value retrieval task admits controlled changes to the input context length (adding more key-value pairs) and the position of relevant in-formation. Although some models perform the synthetic key-value retrieval task perfectly, other models struggle to simply retrieve matching tokens that occur in the middle of their input context and continue to exhibit a U-shaped performance curve. To better understand why language models strug-gle to robustly access and use information in their input contexts, we study the role of model archi-tecture (decoder-only vs. encoder-decoder), query-aware contextualization, and instruction fine-tuning (§4). We find that: • Encoder-decoder models are relatively robust to changes in the position of relevant informa-tion within their input context, but only when evaluated on sequences within its training-time sequence length. When evaluated on sequences longer than those seen during train-ing, we observe a U-shaped performance curve (§4.1). • Query-aware contextualization (placing the query before and after the documents or key-value pairs) enables near-perfect performance on the synthetic key-value task, but minimally changes trends in multi-document QA (§4.2). • Even base language models (i.e., without in-struction fine-tuning) show a U-shaped per-formance curve as we vary the position of relevant information in the input context. Our results indicate that prompting language models with longer input contexts is a trade-off— providing the language model with more informa-tion may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing ac-curacy. To better understand this trade-off in prac-tice, we perform a case study with retriever-reader models on open-domain question answering (§5). In contrast to our controlled multi-document QA task, where the context always contains exactly 

one document that answers the question, none or many of the top k documents may contain the an-swer in the open-domain QA setting. When re-trieving from Wikipedia to answer queries from NaturalQuestions-Open, we find that model perfor-mance saturates long before retriever recall satu-rates, indicating that current models fail to effec-tively use additional retrieved documents—using 50 documents instead of 20 retrieved documents only marginally improves performance ( ∼1.5% for GPT-3.5-Turbo and ∼1% for claude-1.3). Our analysis provides a better understanding of how language models use their input context and introduces new evaluation protocols for future long-context models; to claim that a language model can robustly use information within long input con-texts, it is necessary to show that its performance is minimally affected by the position of the rele-vant information in the input context (e.g., minimal difference in best- and worst-case performance). To facilitate further work on understanding and improving how language models use their input context, we release our code and evaluation data. 1

2 Multi-Document Question Answering 

Our goal is to better understand how language mod-els use their input context. To this end, we analyze model performance on multi-document question answering, which requires models to find relevant information within an input context and use it to answer the question. In particular, we make con-trolled changes to the length of the input context and the position of the relevant information and measure changes in task performance. 

2.1 Experimental Setup 

In the multi-document question answering task, the model inputs are (i) a question to answer and (ii) k

documents (e.g., passages from Wikipedia), where 

exactly one of the documents contains the answer 

> 1nelsonliu.me/papers/lost-in-the-middle

to the question and k − 1 “distractor” documents do not. This task requires the model to access the document that contains the answer within its input context and use it to answer the question. Figure 2 presents an example. We instantiate this task with data from NaturalQuestions-Open (Lee et al., 2019; Kwiatkowski et al., 2019), which contains historical queries issued to the Google search engine, coupled with human-annotated answers extracted from Wikipedia. In particular, we take the 2655 queries where the annotated long answer is a paragraph (as opposed to a list or a table). We use passages (chunks of at most 100 tokens) from Wikipedia as documents within our input contexts. For each of the queries, we need a document that contains the answer and k − 1 distractor documents that do not contain the answer. To obtain a document that answers the question, we use the Wikipedia paragraph that contains the answer from the NaturalQuestions annotations. To collect k − 1 distractor documents that do not contain the answer, we use a retrieval system (Con-triever, fine-tuned on MS-MARCO; Izacard et al., 2021) to retrieve the k − 1 Wikipedia chunks that are most relevant to the query and do not contain any of the NaturalQuestions-annotated answers. 2,3 

In the input context, the distractor documents are presented in order of decreasing relevance. 4

To modulate the position of relevant information within the input context, we adjust the order of the documents to change the position of the document that contains the answer (Figure 3). To modulate the input context length in this task, we increase or decrease the number of retrieved documents that do not contain the answer (Figure 4). Following Kandpal et al. (2022) and Mallen et al. (2023), we use accuracy as our primary evaluation metric, judging whether any of the correct answers (as taken from the NaturalQuestions annotations) appear in the predicted output.    

> 2Ambiguity in NaturalQuestions-Open means that a small number of distractor passages may contain a reasonable an-swer. We additionally run experiments on subset of unam-biguous questions, finding similar results and conclusions; see Appendix A.
> 3We also explored using random documents as distractors, see Appendix B for more details.
> 4Since there might be a prior over “search results” appear-ing in ranked order, we explored randomly ordering the k−1
> distractor documents and mentioning that the documents are randomly ordered in the task description, but found the same trends. See Appendix C for more details.

Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). Document [1](Title: Asian Americans in science and technology) Prize in physics for discovery of the subatomic particle J/ψ. Subrahmanyan Chandrasekhar shared... 

Document [2](Title: List of Nobel laureates in Physics) The first Nobel Prize in Physics was awarded in 1901 to Wilhelm Conrad Röntgen, of Germany, who received... 

Document [3](Title: Scientist) and pursued through a unique method, was essentially in place. Ramón y Cajal won the Nobel Prize in 1906 for his remarkable... Question: who got the first nobel prize in physics Answer: 

Input Context 

Wilhelm Conrad Röntgen 

Desired Answer Figure 2: Example of the multi-document question answering task, with an input context and the desired model answer. The document containing the answer is bolded within the input context here for clarity. Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant).           

> Document [1](Title: List of Nobel laureates in Physics) ...
> Document [2](Title: Asian Americans in science and technology) ... Document [3](Title: Scientist) ... Question: who got the first nobel prize in physics Answer:
> Input Context
> Wilhelm Conrad Röntgen
> Desired Answer

Figure 3: Modulating the position of relevant informa-tion within the input context for the multi-document question answering example presented in Figure 2. Re-ordering the documents in the input context does not affect the desired output. 

Our experimental setup is similar to the needle-in-a-haystack experiments of Ivgi et al. (2023), who compare question answering performance when the relevant paragraph is placed (i) at the beginning of the input or (ii) a random position within the in-put. They find that encoder-decoder models have significantly higher performance when relevant in-formation is placed at the start of the input context. In contrast, we study finer-grained changes in the position of relevant information. 

2.2 Models 

We analyze several state-of-the-art open and closed language models. We use greedy decoding when generating outputs and leave exploration of other decoding methods to future work. We use a stan-dard set of prompts for each model (Figure 2). Write a high-quality answer for the given question using only the provided search results (some of which might be irrelevant). Document [1](Title: Asian Americans in science and technology) ...                    

> Document [2](Title: List of Nobel laureates in Physics) ...
> Document [3](Title: Scientist) ... Document [4](Title: Norwegian Americans) ... Document [5](Title: Maria Goeppert Mayer) ... Question: who got the first nobel prize in physics Answer:
> Input Context Input Context
> Wilhelm Conrad Röntgen
> Desired Answer

Figure 4: Modulating the input context length of the multi-document question answering example presented in Figure 2. Adding documents that do not contain the answer increases the length of the input context, but does not affect the desired output. 

Open models. We experiment with MPT-30B-Instruct, which has a maximum context length of 8192 tokens. The model was initially pre-trained on 1 trillion tokens using 2048-token sequences, followed by an additional sequence length adapta-tion pre-training phase on 50 billion tokens using 8192-token sequences. MPT-30B-Instruct uses AL-iBi (Press et al., 2022) to represent positional infor-mation. We also evaluate LongChat-13B (16K) (Li et al., 2023), which extends the LLaMA-13B (Tou-vron et al., 2023a) context window from 2048 to 16384 tokens by using condensed rotary positional embeddings before fine-tuning with 16384-token sequences. 

Closed models. We use the OpenAI API to ex-periment with GPT-3.5-Turbo and GPT-3.5-Turbo 1st 5th 10th                

> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 10 Total Retrieved Documents (~2K tokens)
> 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> 1st 5th 10th 15th 20th 25th 30th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 30 Total Retrieved Documents (~6K tokens)
> claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k

Figure 5: The effect of changing the position of relevant information (document containing the answer) on multi-document question answering performance. Lower positions are closer to the start of the input context. Performance is highest when relevant information occurs at the very start or end of the context, and rapidly degrades when models must reason over information in the middle of their input context. 

(16K). 5 GPT-3.5-Turbo has a maximum context length of 4K tokens, and GPT-3.5-Turbo (16K) is a version with an extended maximum context length of 16K tokens. We evaluate Claude-1.3 and Claude-1.3 (100K) with the Anthropic API; Claude-1.3 has a maximum context length of 8K tokens, and Claude-1.3 (100K) has an extended context length of 100K tokens. 6

2.3 Results and Discussion 

We experiment with input contexts containing 10, 20, and 30 total documents. Figure 5 presents multi-document question answering performance when varying the position of relevant information within the input context. To contextualize model perfor-mance, we also evaluate on the closed-book and oracle settings (Table 1). In the closed-book setting, models are not given any documents in their input context, and must rely on their parametric memory to generate the correct answer. On the other hand, in the oracle setting, language models are given the single document that contains the answer and must use it to answer the question. 

Model performance is highest when relevant in-formation occurs at the beginning or end of its input context. As illustrated in Figure 5, chang-ing the position of relevant information in the in-put context leads to substantial decreases in model performance. In particular, we see a distinctive U-

> 5

We use the 0613 OpenAI model versions. 

> 6

We also evaluate GPT-4 (8K) on a subset of multi-document QA experiments, finding similar results and trends as other models (though GPT-4 has higher absolute perfor-mance). Evaluating GPT-4 on the full multi-document QA and key-value retrieval experiments would cost upwards of $6000. See Appendix D for GPT-4 results and discussion. Model Closed-Book Oracle LongChat-13B (16K) 35.0% 83.4% MPT-30B-Instruct 31.5% 81.9% GPT-3.5-Turbo 56.1% 88.3% GPT-3.5-Turbo (16K) 56.0% 88.6% Claude-1.3 48.3% 76.1% Claude-1.3 (100K) 48.2% 76.4% 

Table 1: Closed-book and oracle accuracy of language models on the multi-document question answering task. 

shaped performance curve—models are often much better at using relevant information that occurs at the very beginning (primacy bias) and very end of contexts (recency bias), and suffer degraded perfor-mance when forced to use information within the middle of its input context. For example, GPT-3.5-Turbo’s multi-document QA performance can drop by more than 20%—in the worst case, performance in 20- and 30-document settings is lower than per-formance without any input documents (i.e., closed-book performance; 56.1%). These results indicate that current models cannot effectively reason over their entire context window when prompted for downstream tasks. 

Extended-context models are not necessarily bet-ter at using input context. When the input con-text fits in the context window of both a model and its extended-context counterpart, we see that performance between them is nearly identical. For example, the 10- and 20-document settings both fit in the context window of GPT-3.5-Turbo and GPT-3.5-Turbo (16K), and we observe that their performance as a function of position of relative information is nearly superimposed (solid purple and dashed brown series in Figure 5). These results Extract the value corresponding to the specified key in the JSON object below. JSON data: {"2a8d601d-1d69-4e64-9f90-8ad825a74195": "bb3ba2a5-7de8-434b-a86e-a88bb9fa7289", "a54e2eed-e625-4570-9f74-3624e77d6684": "d1ff29be-4e2a-4208-a182-0cea716be3d4", "9f4a92b9-5f69-4725-ba1e-403f08dea695 ": "703a7ce5-f17f-4e6d-b895-5836ba5ec71c", "52a9c80c-da51-4fc9-bf70-4a4901bc2ac3": "b2f8ea3d-4b1b-49e0-a141-b9823991ebeb", "f4eb1c53-af0a-4dc4-a3a5-c2d50851a178": "d733b0d2-6af3-44e1-8592-e5637fdb76fb"} Key: "9f4a92b9-5f69-4725-ba1e-403f08dea695 "Corresponding value: 

> Input Context
> 703a7ce5-f17f-4e6d-b895-5836ba5ec71c
> Desired Output

Figure 6: Example of the key-value retrieval task, with an input context and the desired model output. Given a key, the goal is to return the associated value. All keys and values are 128-bit UUIDs. The relevant key-value pair for answering the query is bolded here within the input context for clarity. 

indicate that extended-context models are not nec-essarily better than their non-extended counterparts at using their input context. 

3 How Well Can Language Models Retrieve From Input Contexts? 

Given that language models struggle to retrieve and use information from the middle of their input contexts in the multi-document question answering task, to what extent can they simply retrieve from input contexts? We study this question with a syn-thetic key-value retrieval task, which is designed to provide a minimal testbed for the basic ability to retrieve matching tokens from an input context. 

3.1 Experimental Setup 

In our synthetic key-value retrieval task, the inputs are (i) a string-serialized JSON object with k key-value pairs, where each of the keys and values are unique, randomly-generated UUIDs and (ii) a key within the aforementioned JSON object. The goal is to return the value associated with the specified key. Thus, each JSON object contains one relevant key-value pair (where the value is to be returned), and k − 1 irrelevant “distractor” key-value pairs. Figure 6 provides an example input context and its corresponding desired output. We again measure accuracy by evaluating whether the correct value appears in the predicted output. Our synthetic key-value retrieval task shares sim-ilar goals with the Little Retrieval Test of Papail-iopoulos et al. (2023) and the fine-grained line re-trieval task of Li et al. (2023), but we explicitly seek to distill and simplify the task by removing as much natural language semantics as possible (using random UUIDs instead), since language features may present potential confounders. For example, Transformer language models may have varying sensitivity to different linguistic features in their input (O’Connor and Andreas, 2021). To modulate the position of relevant information within the input context, we change the position of the key to retrieve within the serialized JSON object. To modulate the input context length, we change the number of input JSON key-value pairs 

k by adding or removing random keys, changing the number of distractor key-value pairs. 

3.2 Results and Discussion 

We experiment with input contexts containing 75, 140, and 300 key-value pairs (500 examples each). We use the same set of models as the multi-document question answering experiments, see §2.2 for more details. Figure 7 presents key-value retrieval perfor-mance. Claude-1.3 and Claude-1.3 (100K) do nearly perfectly on all evaluated input context lengths, but other models struggle, especially when contexts have 140 or 300 key-value pairs— although the synthetic key-value retrieval task only requires identifying exact match within the input context, not all models achieve high performance. Similar to our multi-document QA results, GPT-3.5-Turbo, GPT-3.5-Turbo (16K), and MPT-30B-Instruct have the lowest performance when they must access key-value pairs in the middle of their input context. LongChat-13B (16K) exhibits a dif-ferent trend in the 140 key-value setting; we quali-tatively observe that when relevant information is 1st 25th 50th 75th                

> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 75 Key-Value Pairs (~4K tokens)
> 1st 35th 70th 105th 140th
> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 140 Key-Value Pairs (~8K tokens)
> 1st 50th 100th 150th 200th 250th 300th
> Position of Key to Retrieve
> 40
> 50
> 60
> 70
> 80
> 90
> 100
> Accuracy
> 300 Key-Value Pairs (~16K tokens)
> claude-1.3 claude-1.3-100k gpt-3.5-turbo-0613 gpt-3.5-turbo-16k-0613 mpt-30b-instruct longchat-13b-16k

Figure 7: The effect of changing the input context length and the position of relevant information on key-value retrieval performance. Lower positions are closer to the start of the input context. Although some models show perfect accuracy on this synthetic task (e.g., Claude-1.3 and Claude-1.3 (100K)), we see again that performance is often highest when relevant information is occurs at the very start or end of the context, and rapidly degrades when models must retrieve from the middle of the input context. 

placed at the start of the input context, LongChat-13B (16K) tends to generate code to retrieve the key, rather than outputting the value directly. 

4 Why Are Language Models Not Robust to Changes in the Position of Relevant Information? 

Our multi-document question answering and key-value retrieval results show that language models struggle to robustly access and use information in long input contexts, since performance degrades significantly when changing the position of rele-vant information. To better understand why, we per-form some preliminary investigations into the role of model architecture (decoder-only vs. encoder-decoder), query-aware contextualization, and in-struction fine-tuning. 

4.1 Effect of Model Architecture 

The open models we evaluated are all decoder-only models—at each timestep, they may only attend to prior tokens. To better understand the poten-tial effects of model architecture on how language model use context, we compare decoder-only and encoder-decoder language models. We experiment with Flan-T5-XXL (Raffel et al., 2020; Chung et al., 2022) and Flan-UL2 (Tay et al., 2023). Flan-T5-XXL is trained with a sequences of 512 tokens (encoder and decoder). Flan-UL2 is initially trained with sequences of 512 tokens (en-coder and decoder), but is then pre-trained for an extra 100K steps with 1024 tokens (encoder and de-coder) before instruction fine-tuning on sequences with 2048 tokens in the encoder and 512 tokens in the decoder. However, since these models use relative positional embeddings, they can (in prin-ciple) extrapolate beyond these maximum context lengths; Shaham et al. (2023) find that both mod-els can perform well with sequences of up to 8K tokens. Figure 8 compares the performance of decoder-only and encoder-decoder models. When Flan-UL2 is evaluated on sequences within its 2048-token training-time context window (Figure 8; left sub-plot), its performance is relatively robust to changes in the position of relevant information within the input context (1.9% absolute difference between best- and worst-case performance). When evalu-ated on settings with sequences longer than 2048 tokens (Figure 8; center and right), Flan-UL2 per-formance begins to degrade when relevant informa-tion is placed in the middle. Flan-T5-XXL shows a similar trend, where longer input contexts result in a greater performance degradation when placing relevant information in the middle of the input con-text. We hypothesize that encoder-decoder models may make better use of their context windows be-cause their bidirectional encoder allows processing each document in the context of future documents, potentially improving relative importance estima-tion between documents. 

4.2 Effect of Query-Aware Contextualization 

Our multi-document QA and key-value retrieval experiments place the query (i.e., question to an-swer or key to retrieve) after the data to process (i.e., the documents or the key-value pairs). As a result, decoder-only models cannot attend to query tokens when contextualizing documents or key-value pairs, since the query only appears at the end 1st 5th 10th              

> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 10 Total Retrieved Documents (~2K tokens)
> 1st 5th 10th 15th 20th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> 1st 5th 10th 15th 20th 25th 30th
> Position of Document with the Answer
> 50
> 55
> 60
> 65
> 70
> Accuracy
> 30 Total Retrieved Documents (~6K tokens)
> mpt-30b-instruct longchat-13b-16k flan-t5-xxl flan-ul2

Figure 8: When encoder-decoder models (Flan-UL2 and Flan-T5-XXL) evaluated on sequences that are shorter 

than their encoder’s training-time maximum sequence length (2048 and 512 tokens, respectively), they are relatively robust to changes in the position of relevant information within their input context (left subplot). In contrast, when these models are evaluated on sequences longer than those seen during training (center and right subplots), we observe a U-shaped performance curve—performance is higher when relevant information occurs at the beginning or end of the input context, as opposed to the middle of the input context. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 50
> 60
> 70
> 80
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, query-aware contextualization)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 9: Query-aware contextualization (placing the query before and after the documents) does not sub-stantially improve robustness of language models to changing the position of relevant information in multi-document QA; performance slightly increases when relevant information occurs at the very beginning, but otherwise slightly decreases. 

of the prompt and decoder-only models can only attend to prior tokens at each timestep. In contrast, encoder-decoder models (which seem more robust to changes in the position of relevant information; §4.1) use a bidirectional encoder to contextualize input contexts—can we use this observation to im-prove decoder-only models by placing the query be-fore and after the data, enabling query-aware con-textualization of documents (or key-value pairs)? We find that query-aware contextualization dra-matically improves performance on the key-value retrieval task—all models achieve near-perfect per-formance on the 75, 140, and 300 key-value pair settings. For example, GPT-3.5-Turbo (16K) with query-aware contextualization achieves perfect per-formance when evaluated with 300 key-value pairs. In contrast, without query-aware contextualiza-tion, the worst-case performance is 45.6% (Fig-ure 7). Despite the significant impact on key-value retrieval performance, query-aware contextu-alization minimally affects performance trends in the multi-document question answering task (Fig-ure 9); it slightly improves performance when the relevant information is located at the very begin-ning of the input context, but slightly decreases performance in other settings. 

4.3 Effect of Instruction Fine-Tuning 

The models we evaluated are all instruction fine-tuned—after their initial pre-training, they undergo supervised fine-tuning on a dataset of instructions and responses. The task specification and/or in-struction is commonly placed at the beginning of the input context in supervised instruction fine-tuning data, which might lead instruction fine-tuned language models to place more weight on the start of the input context. To better understand the potential effects of instruction fine-tuning on how language models use long input contexts, we compare the multi-document question answering performance of MPT-30B-Instruct against its base model (i.e., before instruction fine-tuning) MPT-30B. We use the same experimental setup as §2. Figure 10 compares the multi-document QA performance of MPT-30B and MPT-30B-Instruct as a function of the position of the relevant in-1st 5th 10th 15th 20th  

> Position of Document with the Answer
> 44
> 46
> 48
> 50
> 52
> 54
> 56
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> mpt-30b mpt-30b-instruct Figure 10: Multi-document QA performance of MPT-30B-Instruct compared against its base model (i.e., be-fore instruction fine-tuning) MPT-30B. Both models have a U-shaped performance curve, where performance is much higher when relevant information occurs at the start or end of the input context, indicating that the instruction fine-tuning process itself is not necessarily responsible for these performance trends.

formation in the input context. Surprisingly, we see that both MPT-30B and MPT-30B-Instruct ex-hibit a U-shaped performance curve, where perfor-mance is highest when relevant information occurs at the very beginning or very end of the context. Although the absolute performance of MPT-30B-Instruct is uniformly higher than that of MPT-30B, their overall performance trends are similar. We also observe that instruction fine-tuning slightly re-duces the worst-case performance disparity from nearly 10% between the base model best- and worst-case performance to around 4%. These observations complement prior work, which found that non-instruction fine-tuned lan-guage models are biased towards recent tokens (i.e., the end of the input context; Khandelwal et al., 2018; Press et al., 2021). This recency bias has been observed in past work when evaluating mod-els on next-word prediction of contiguous text, a setting where language models minimally benefit from long-range information (Sun et al., 2021). In contrast, our results show that language models are capable of using longer-range information (i.e., the beginning of the input context) when prompted with instruction-formatted data. We hypothesize that non-instruction fine-tuned language models learn to use these long contexts from similarly-formatted data that may occur in Internet text seen during pre-training, e.g., StackOverflow questions and answers. To better understand the effect of additional fine-tuning and model scale, we also experimented with Llama-2 models of varying sizes (7B, 13B, and 70B) with and without additional supervised fine-tuning and reinforcement learning from hu-man feedback (Appendix E). We find that the U-shaped performance curve only appears in suffi-ciently large language models (with or without ad-ditional fine-tuning)—the 7B Llama-2 models are solely recency biased, while the 13B and 70B mod-els exhibit a U-shaped performance curve. In addi-tion, we see that the Llama-2 supervised fine-tuning and reinforcement learning from human feedback procedure slightly mitigates the positional bias in smaller models (13B, akin to trends shown when comparing MPT-30B and MPT-30B-Instruct), but minimally affects trends on larger models (70B). 

5 Is More Context Is Always Better? A Case Study With Open-Domain QA 

Our results indicate that prompting language mod-els with longer input contexts is a trade-off— providing the language model with more informa-tion may help it perform the downstream task, but it also increases the amount of content that the model must reason over, potentially decreasing accuracy. Even if a language model can take in 16K tokens, is it actually beneficial to provide 16K tokens of context? The answer to this question is ultimately downstream task-specific since it de-pends on the marginal value of the added context and the model’s ability to effectively use long input contexts, but we perform a case study with open-domain question answering on NaturalQuestions-Open to better understand this trade-off in existing language models. We use language models in a standard retriever-reader setup. A retrieval system (Contriever, fine-tuned on MS-MARCO) takes an input query from NaturalQuestions-Open and returns the k docu-ments from Wikipedia with the highest relevance score. To condition language models on these re-trieved documents, we simply include them in the prompt. We evaluate retriever recall and reader accuracy (whether any of the annotated answers appear in the predicted output) as a function of the number of retrieved documents k. We use a subset of NaturalQuestions-Open where the long answer is a paragraph (as opposed to a table or a list). Figure 11 presents retriever recall and open-5 10 20 30 40 50 

> Number of Retrieved Docs
> 50
> 60
> 70
> 80
> 90
> Metric
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k
> contriever recall

Figure 11: Retriever recall and model performance as a function of the number of retrieved documents. Model performance saturates long before retriever recall, indi-cating that the models have difficulty making use of the extra retrieved documents. 

domain QA results. We see that reader model performance saturates long before retriever per-formance saturates, indicating that readers are not effectively using the extra context. Using more than 20 retrieved documents only marginally im-proves reader performance ( ∼1.5% for GPT-3.5-Turbo and ∼1% for Claude-1.3), while significantly increasing the input context length (and thus la-tency and cost). These results, coupled with the observation that models are often better at retriev-ing and using information at the start or end of the input contexts, suggest that effective rerank-ing of retrieved documents (pushing relevant infor-mation closer to the start of the input context) or ranked list truncation (retrieving fewer documents when appropriate; Arampatzis et al., 2009) may be promising directions for improving how language-model-based readers use retrieved context. 

6 Related Work 

6.1 Long-Context Language Models 

There is much prior work in designing performant language models with cheaper scaling than Trans-formers in the context length. Many lines of work pursue Transformer variants with attention modi-fications like recurrence (Dai et al., 2019), factor-izing attention into computationally less intensive approximations (Beltagy et al., 2020; Zaheer et al., 2020), or low-rank approximations (Wang et al., 2020; Peng et al., 2021). Dao et al. (2022) in-stead provide a faster exact attention by a carefully-crafted IO-aware CUDA kernel. Separately, there are attempts to do away with attention entirely to remove quadratic sequence length complexity, of-ten through convolution and/or linear RNNs, e.g., in RWKV (Peng, 2023), S4 (Gu et al., 2022), or Hyena (Poli et al., 2023). Many prior efforts evalu-ate perplexity on a diverse web corpus as a proxy for the ability to process long contexts; this work shows that precise knowledge access on long con-texts may be an added challenge. 

6.2 How Do Language Models Use Context? 

The pioneering work of Khandelwal et al. (2018) showed that small LSTM language models make increasingly coarse use of longer-term context; Sankar et al. (2019) found similar results in di-alogue models. In a similar vein, Daniluk et al. (2017) find that attentive LSTM language mod-els tend to mainly use recent history. Petroni et al. (2020) were among the first to demonstrate the potential of combining context from an in-formation retrieval system with a pretrained lan-guage models for unsupervised question answering. O’Connor and Andreas (2021) found that many information-destroying operations had marginal ef-fects on Transformer LMs’ predictions. Krishna et al. (2022) found that long-context neural gen-eration in modestly-sized Transformer language models degenerates because models fail to prop-erly condition on long context. Finally, studying long-context models, Sun et al. (2021) found that longer contexts improves prediction of only a few tokens, an empirical finding consistent with the theory of Sharan et al. (2018), who showed that sequence distributions with bounded mutual infor-mation necessarily lead to marginal average predic-tion benefits from increasingly long context. Qin et al. (2023) analyze how efficient Transformers perform on a variety of long-context downstream NLP tasks, finding that long-context transformers are recency-biased and do not effectively use long-range context. 

6.3 The Serial-Position Effect 

The U-shaped curve we observe in this work has a connection in psychology known as the serial-position effect (Ebbinghaus, 1913; Murdock Jr, 1962), that states that in free-association recall of elements from a list, humans tend to best re-member the first and last elements of the list. The serial-position effect plays a role in understanding how humans develop short- and long-term mem-ory. Observing a serial-position-like effect in lan-guage models is perhaps surprising, since the self-attention mechanisms underlying Transformer lan-guage models is technically equally capable of re-trieving any token from their contexts. 

7 Conclusion 

We empirically study how language models use long input contexts via a series of controlled ex-periments. We show that language model perfor-mance degrades significantly when changing the position of relevant information, indicating that models struggle to robustly access and use infor-mation in long input contexts. In particular, per-formance is often lowest when models must use information in the middle of long input contexts. We conduct a preliminary investigation of the role of (i) model architecture, (ii) query-aware contextu-alization, and (iii) instruction fine-tuning to better understand how they affect how language models use context. Finally, we conclude with a practi-cal case study of open-domain question answering, finding that the performance of language model readers saturates far before retriever recall. Our results and analysis provide a better understanding of how language models use their input context and provides new evaluation protocols for future long-context models. 

Acknowledgments 

We would like to thank Luke Zettlemoyer, who served as our TACL action editor, and the the anonymous reviewers for their comments and feed-back. We also thank Claudiu Leoveanu-Condrei, Megan Leszczynski, Dmytro Okhonko, Maithra Raghu, Eric Wallace and Sang Michael Xie for feedback and discussions that helped improve this work. Further, we are grateful to Sewon Min for her help with the AmbigQA dataset. This work was supported by the Stanford Center for Research on Foundation Models (CRFM), by OpenAI via an API credits grant to the Stanford CRFM, and by Anthropic via the Claude academic access pro-gram. 

References 

Avi Arampatzis, Jaap Kamps, and Stephen Robert-son. 2009. Where to stop reading a ranked list? threshold optimization using truncated score dis-tributions. In Proc. of SIGIR .Iz Beltagy, Matthew E. Peters, and Arman Cohan. 2020. Longformer: The long-document trans-former. ArXiv:2004.05150. Hyung Won Chung, Le Hou, Shayne Longpre, Bar-ret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi Wang, Mostafa Dehghani, Siddhartha Brahma, Albert Webson, Shixiang Shane Gu, Zhuyun Dai, Mirac Suzgun, Xinyun Chen, Aakanksha Chowdhery, Alex Castro-Ros, Marie Pellat, Kevin Robinson, Dasha Valter, Sharan Narang, Gaurav Mishra, Adams Yu, Vincent Zhao, Yanping Huang, Andrew Dai, Hongkun Yu, Slav Petrov, Ed H. Chi, Jeff Dean, Jacob Devlin, Adam Roberts, Denny Zhou, Quoc V. Le, and Jason Wei. 2022. Scaling instruction-finetuned language models. ArXiv:2210.11416. Zihang Dai, Zhilin Yang, Yiming Yang, Jaime Carbonell, Quoc Le, and Ruslan Salakhutdinov. 2019. Transformer-XL: Attentive language mod-els beyond a fixed-length context. In Proc. of ACL .Michał Daniluk, Tim Rocktäschel, Johannes Welbl, and Sebastian Riedel. 2017. Frustratingly short attention spans in neural language modeling. In 

Proc. of ICLR .Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. 2022. FlashAttention: Fast and memory-efficient exact attention with IO-awareness. ArXiv:2205.14135. Hermann Ebbinghaus. 1913. Memory: A contribu-tion to experimental psychology. H. A. Ruger & C. E. Bussenius, Trans. 

Albert Gu, Karan Goel, and Christopher Ré. 2022. Efficiently modeling long sequences with struc-tured state spaces. In Proc. of ICLR .Maor Ivgi, Uri Shaham, and Jonathan Berant. 2023. Efficient long-text understanding with short-text models. Transactions of the Association for Computational Linguistics , 11:284–299. Gautier Izacard, Mathilde Caron, Lucas Hosseini, Sebastian Riedel, Piotr Bojanowski, Armand Joulin, and Edouard Grave. 2021. Unsupervised dense information retrieval with contrastive learning. ArXiv:2112.09118. Gautier Izacard and Edouard Grave. 2021. Lever-aging passage retrieval with generative models for open domain question answering. In Proc. of EACL .Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric Wallace, and Colin Raffel. 2022. Large lan-guage models struggle to learn long-tail knowl-edge. ArXiv:2211.08411. Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. 2018. Sharp nearby, fuzzy far away: How neural language models use context. In 

Proc. of ACL .Kalpesh Krishna, Yapei Chang, John Wieting, and Mohit Iyyer. 2022. RankGen: Improving text generation with large ranking models. In Proc. of EMNLP .Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, Kristina Toutanova, Llion Jones, Matthew Kelcey, Ming-Wei Chang, An-drew M. Dai, Jakob Uszkoreit, Quoc Le, and Slav Petrov. 2019. Natural Questions: A bench-mark for question answering research. Trans-actions of the Association for Computational Linguistics , 7:452–466. Kenton Lee, Ming-Wei Chang, and Kristina Toutanova. 2019. Latent retrieval for weakly supervised open domain question answering. In 

Proc. of ACL .Mina Lee, Percy Liang, and Qian Yang. 2022. CoAuthor: Designing a human-AI collaborative writing dataset for exploring language model ca-pabilities. In Proc. of CHI .Dacheng Li, Rulin Shao, Anze Xie, Ying Sheng, Lianmin Zheng, Joseph E. Gonzalez, Ion Stoica, Xuezhe Ma, , and Hao Zhang. 2023. How long can open-source LLMs truly promise on context length? Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, and Hannaneh Hajishirzi. 2023. When not to trust language models: In-vestigating effectiveness of parametric and non-parametric memories. In Proc. of ACL .Sewon Min, Julian Michael, Hannaneh Hajishirzi, and Luke Zettlemoyer. 2020. AmbigQA: An-swering ambiguous open-domain questions. In 

Proc. of EMNLP .Bennet B. Murdock Jr. 1962. The serial position effect of free recall. Journal of experimental psychology , 64(5):482. Joe O’Connor and Jacob Andreas. 2021. What con-text features can Transformer language models use? In Proc. of ACL .Dimitris Papailiopoulos, Kangwook Lee, and Jy-yong Sohn. 2023. A little retrieval test for large language models. https://github.com/ anadim/the-little-retrieval-test .Bo Peng. 2023. RWKV-LM. https://github. com/BlinkDL/RWKV-LM .Hao Peng, Nikolaos Pappas, Dani Yogatama, Roy Schwartz, Noah Smith, and Lingpeng Kong. 2021. Random feature attention. In Proc. of ICLR .Fabio Petroni, Patrick Lewis, Aleksandra Piktus, Tim Rocktäschel, Yuxiang Wu, Alexander H Miller, and Sebastian Riedel. 2020. How context affects language models’ factual predictions. In 

Proc. of AKBC .Michael Poli, Stefano Massaroli, Eric Nguyen, Daniel Y. Fu, Tri Dao, Stephen Baccus, Yoshua Bengio, Stefano Ermon, and Christopher Ré. 2023. Hyena hierarchy: Towards larger con-volutional language models. In Proc. of ICML .Ofir Press, Noah A. Smith, and Mike Lewis. 2021. Shortformer: Better language modeling using shorter inputs. In Proc. of ACL .Ofir Press, Noah A. Smith, and Mike Lewis. 2022. Train short, test long: Attention with linear bi-ases enables input length extrapolation. In Proc. of ICLR .Guanghui Qin, Yukun Feng, and Benjamin Van Durme. 2023. The NLP task effectiveness of long-range transformers. In Proc. of EACL .Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J. Liu. 2020. Ex-ploring the limits of transfer learning with a uni-fied text-to-text Transformer. Journal of Ma-chine Learning Research , 21(140):1–67. Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay, Amnon Shashua, Kevin Leyton-Brown, and Yoav Shoham. 2023. In-context retrieval-augmented language models. ArXiv:2302.00083. Ohad Rubin and Jonathan Berant. 2023. Long-range language modeling with self-retrieval. ArXiv:2306.13421. Chinnadhurai Sankar, Sandeep Subramanian, Chris Pal, Sarath Chandar, and Yoshua Bengio. 2019. Do neural dialog systems use the conversation history effectively? an empirical study. In Proc. of ACL .Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettle-moyer, Nicola Cancedda, and Thomas Scialom. 2023. Toolformer: Language models can teach themselves to use tools. Uri Shaham, Maor Ivgi, Avia Efrat, Jonathan Be-rant, and Omer Levy. 2023. ZeroSCROLLS: A zero-shot benchmark for long text understanding. ArXiv:2305.14196. Vatsal Sharan, Sham Kakade, Percy Liang, and Gregory Valiant. 2018. Prediction with a short memory. In Proc. of STOC .Weijia Shi, Sewon Min, Michihiro Yasunaga, Min-joon Seo, Rich James, Mike Lewis, Luke Zettle-moyer, and Wen tau Yih. 2023. REPLUG: Retrieval-augmented black-box language mod-els. ArXiv:2301.12652. Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller, Megan Ung, Moya Chen, Kushal Arora, Joshua Lane, Morteza Behrooz, William Ngan, Spencer Poff, Naman Goyal, Arthur Szlam, Y-Lan Boureau, Melanie Kambadur, and Jason Weston. 2022. BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage. ArXiv:2208.03188. Simeng Sun, Kalpesh Krishna, Andrew Mattarella-Micke, and Mohit Iyyer. 2021. Do long-range language models actually use long-range con-text? In Proc. of EMNLP .Yi Tay, Mostafa Dehghani, Vinh Q. Tran, Xavier Garcia, Jason Wei, Xuezhi Wang, Hyung Won Chung, Siamak Shakeri, Dara Bahri, Tal Schuster, Huaixiu Steven Zheng, Denny Zhou, Neil Houlsby, and Donald Metzler. 2023. UL2: Unifying language learning paradigms. ArXiv:2205.05131. Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, YaGuang Li, Hongrae Lee, Huaixiu Steven Zheng, Amin Ghafouri, Marcelo Menegali, Yanping Huang, Maxim Krikun, Dmitry Lepikhin, James Qin, Dehao Chen, Yuanzhong Xu, Zhifeng Chen, Adam Roberts, Maarten Bosma, Vincent Zhao, Yanqi Zhou, Chung-Ching Chang, Igor Krivokon, Will Rusch, Marc Pickett, Pranesh Srinivasan, Laichee Man, Kathleen Meier-Hellstern, Meredith Ringel Mor-ris, Tulsee Doshi, Renelito Delos Santos, Toju Duke, Johnny Soraker, Ben Zevenbergen, Vin-odkumar Prabhakaran, Mark Diaz, Ben Hutchin-son, Kristen Olson, Alejandra Molina, Erin Hoffman-John, Josh Lee, Lora Aroyo, Ravi Rajakumar, Alena Butryna, Matthew Lamm, Viktoriya Kuzmina, Joe Fenton, Aaron Cohen, Rachel Bernstein, Ray Kurzweil, Blaise Aguera-Arcas, Claire Cui, Marian Croak, Ed Chi, and Quoc Le. 2022. LaMDA: Language models for dialog applications. ArXiv:2201.08239. Hugo Touvron, Thibaut Lavril, Gautier Izac-ard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guillaume Lample. 2023a. LLaMA: Open and efficient foundation language models. ArXiv:2302.13971. Hugo Touvron, Louis Martin, Kevin Stone, Pe-ter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernan-des, Jeremy Fu, Wenyin Fu, Brian Fuller, Cyn-thia Gao, Vedanuj Goswami, Naman Goyal, An-thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Ko-renev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, An-gela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023b. Llama 2: Open foundation and fine-tuned chat models. ArXiv:2307.09288. Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia Polosukhin. 2017. At-tention is all you need. In Proc. of NeurIPS .Sinong Wang, Belinda Z. Li, Madian Khabsa, Han Fang, and Hao Ma. 2020. Lin-former: Self-attention with linear complexity. ArXiv:2006.04768. Manzil Zaheer, Guru Guruganesh, Kumar Avinava Dubey, Joshua Ainslie, Chris Alberti, Santiago Ontanon, Philip Pham, Anirudh Ravula, Qifan Wang, Li Yang, and Amr Ahmed. 2020. Big Bird: Transformers for longer sequences. In 

Proc. of NeurIPS .

A Ambiguity in Multi-Document QA Distractor Documents 

Following past work on NaturalQuestions-Open (Izacard et al., 2021; Izacard and Grave, 2021, inter alia ), we use a Wikipedia dump from late 2018 as our retrieval corpus. However, this standard Wikipedia dump has a small amount of temporal mismatch with the NaturalQuestions annotations. For example, consider the question “what nfl team does robert griffin iii play for”. The Natu-ralQuestions annotated answer is “currently a free agent”. However, the Wikipedia retrieval corpus contains the information that he plays for the “Balti-more Ravens”, since he was released from the team between the Wikipedia dump’s timestamp and the NaturalQuestions annotation process. We use the ambiguity annotations of Min et al. (2020) to create a subset unambiguous questions. Experiments on this unambiguous subset of the data show similar results and conclusions as the experiments on the full questions collection (Fig-ure 12). 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, unambiguous questions)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 12: Language model performance on a unam-biguous subset of questions. 

B Random Distractors in Multi-Document QA 

We also run multi-document question answering experiments with random Wikipedia documents as distractors, which allows us to ablate the impact of retrieved distractors (hard negatives). Note that in this setting, the the document containing the an-swer can often be identified with simple heuristics (e.g., lexical overlap with the query). Figure 13 presents the results of this experiment. Although all models have higher absolute accuracy in this setting, they surprisingly still struggle to reason over their entire input context, indicating that their performance degradation is not solely due to an inability to identify relevant documents. 

C Randomizing Distractor Order in Multi-Document QA 

Our prompt instructs the language model to use the provided search results to answer the question. There may be a prior in the pre-training or instruc-tion fine-tuning data to treat search results as sorted by decreasing relevance (i.e., the documents near the beginning of the input context are more likely to be useful than those at the end). To validate that our conclusions are not simply a byproduct of this bias, we run experiments with the modified instruction “Write a high-quality answer for the given ques-tion using only the provided search results (some of which might be irrelevant). The search results are ordered randomly.” In addition, we randomly shuffle the k − 1 distractor documents. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 65
> 70
> 75
> 80
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, random distractors)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 13: Language model performance on multi-document QA when using random distractors, rather than retrieved distractors. 

Figure 14 presents the results of this experiment. We continue to see a U-shaped performance curve, with performance degrading when language mod-els must use information in the middle of their input contexts. Comparing the results in §2.3 with those when randomizing the distractor order and mentioning such in the prompt, we see that ran-domization slightly decreases performance when the relevant information is at the very beginning of the context, and slightly increases performance when using information in the middle and end of the context. 

D GPT-4 Performance 

We evaluate GPT-4 (8K) on a subset of 500 ran-dom multi-document QA examples with 20 total documents in each input context (Figure 15). GPT-4 achieves higher absolute performance than any other language model, but still shows a U-shaped performance curve—its performance is highest when relevant information occurs at the very start or end of the context, and performance degrades when it must use information in the middle of its input context. 

E Llama-2 Performance 

We evaluate Llama-2 (Touvron et al., 2023b) on multi-document QA with 20 total documents in each input context. The Llama tokenizer pro-duces longer sequences than the tokenizers for our previously-studied models, so we discard 20 exam-1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 55
> 60
> 65
> 70
> 75
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, randomly ordered)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k

Figure 14: Language model performance when random-izing the order of the distractors (rather than presenting them in order of decreasing relevance) and mentioning as such in the prompt. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 50
> 60
> 70
> 80
> 90
> Accuracy
> 20 Total Retrieved Documents
> (~4K tokens, 500 question sample)
> claude-1.3
> claude-1.3-100k
> gpt-3.5-turbo-0613
> gpt-3.5-turbo-16k-0613
> mpt-30b-instruct
> longchat-13b-16k
> gpt-4-0613

Figure 15: Although GPT-4 has higher absolute perfor-mance than other models, its performance still degrades when relevant information occurs in the middle of the input context. ples (out of 2655) that exceed Llama-2’s maximum context length of 4096 tokens. We experiment with models of varying sizes (7B, 13B, and 70B pa-rameters), with and without additional supervised fine-tuning and reinforcement learning from hu-man feedback (“ -chat-” models). The results are presented in Figure 16. Comparing Llama-2 models of varying sizes, we find that only the larger models (13B and 70B) exhibit the U-shaped performance curve (i.e., both primacy and recency bias)—the smallest Llama-2 models (7B) are solely recency-biased. Given these results, we hypothesize that prior work (e.g., Khandelwal et al., 2018; Sun et al., 2021) did not previously observe any primacy bias in language models because the models they studied were too small (less than 1B parameters). Comparing between Llama-2 models with and without additional supervised fine-tuning and re-inforcement learning from human feedback, we see that additional fine-tuning dramatically im-proves performance on the multi-document QA task. The 7B models with and without additional fine-tuning show minimal primacy bias, and are largely recency-biased. The 13B base model has a dramatic primacy and recency bias—there is a 20-point accuracy disparity between the best- and worst-case performance. Applying additional fine-tuning to the 13B seems to slightly reduce this bias (10-point worst-case degradation), but the bias remains significant. However, the 70B models with and without additional fine-tuning have largely similar trends (showing both primacy and recency bias), and additional fine-tuning minimally changes the positional bias severity. 1st 5th 10th 15th 20th 

> Position of Document with the Answer
> 20
> 30
> 40
> 50
> 60
> 70
> Accuracy
> 20 Total Retrieved Documents (~4K tokens)
> Llama-2-7b-chat-hf
> Llama-2-13b-chat-hf
> Llama-2-70b-chat-hf
> Llama-2-7b-hf
> Llama-2-13b-hf
> Llama-2-70b-hf

Figure 16: Multi-document QA performance (20 total documents) of Llama-2 models of varying sizes (7B, 13B, 70B parameters), with and without additional su-pervised fine-tuning and reinforcement learning from human feedback (“ -chat-” models). F Token Counts 

Table 2, Table 3, and Table 4 present the average and maximum number of tokens in each of the input contexts for all experimental settings. Note that MPT-30B and MPT-30B-Instruct use the same tokenizer, GPT-3.5-Turbo and GPT-3.5-Turbo (16K) use the same tokenizer, and Claude-1.3 and Claude-1.3 (100K) use the same tokenizer. Furthermore, the Claude-1.3 tokenizer is the same as the GPT-3.5-Turbo tokenizer, modulo some additional special tokens that do not appear in our data. As a result, the token counts for these two model families is the same in our experimental settings. Closed-Book Oracle avg ± stdev max avg ± stdev max LongChat-13B (16K) 55.6 ± 2.7 70 219.7 ± 48.5 588 MPT-30B 43.5 ± 2.2 58 187.9 ± 41.8 482 GPT-3.5-Turbo 15.3 ± 2.2 29 156.0 ± 41.8 449 Claude-1.3 15.3 ± 2.2 29 156.0 ± 41.8 449 

> Table 2: Token count statistics for each of the evaluated models on the closed-book and oracle multi-document question answering settings.

10 docs 20 docs 30 docs avg ± stdev max avg ± stdev max avg ± stdev max LongChat-13B (16K) 1749.9 ± 112.4 2511 3464.6 ± 202.3 4955 5181.9 ± 294.7 7729 MPT-30B 1499.7 ± 88.5 1907 2962.4 ± 158.4 3730 4426.9 ± 230.5 5475 GPT-3.5-Turbo 1475.6 ± 86.5 1960 2946.2 ± 155.1 3920 4419.2 ± 226.5 6101 Claude-1.3 1475.6 ± 86.5 1960 2946.2 ± 155.1 3920 4419.2 ± 226.5 6101 

> Table 3: Token count statistics for each of the evaluated models on each of the document question answering settings.

75 KV pairs 140 KV pairs 300 KV pairs avg ± stdev max avg ± stdev max avg ± stdev max LongChat-13B (16K) 5444.5 ± 19.1 5500 10072.4 ± 24.1 10139 21467.3 ± 35.9 21582 MPT-30B 4110.5 ± 23.8 4187 7600.9 ± 31.1 7687 16192.4 ± 46.6 16319 GPT-3.5-Turbo 3768.7 ± 25.6 3844 6992.8 ± 34.1 7088 14929.4 ± 50.7 15048 Claude-1.3 3768.7 ± 25.6 3844 6992.8 ± 34.1 7088 14929.4 ± 50.7 15048 

> Table 4: Token count statistics for each of the evaluated models on each of the key-value (KV) retrieval settings.

G Full Multi-Document Question Answering Results 

This section tabulates model performance when evaluated on the multi-document QA task with varying numbers of documents (Figure 5). “Index n” indicates performance when the document with the answer occurs at position n + 1 , where lower indices are closer to the start of the input context. For example, index 0 refers to performance when the document with the answer is placed at the very start of the context (i.e., first amongst all documents). 

G.1 10 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Claude-1.3 62.9% 58.3% 59.7% Claude-1.3 (100K) 63.1% 58.3% 59.7% GPT-3.5-Turbo 76.8% 61.2% 62.4% GPT-3.5-Turbo (16K) 76.9% 61.0% 62.5% MPT-30B-Instruct 60.2% 56.2% 59.7% LongChat-13B (16K) 72.1% 58.9% 58.5% 

> Table 5: Model performance when evaluated on the multi-document QA task with 10 total retrieved documents.

G.2 20 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Index 14 Index 19 Claude-1.3 59.9% 55.9% 56.8% 57.2% 60.1% Claude-1.3 (100K) 59.8% 55.9% 57.0% 57.4% 60.0% GPT-3.5-Turbo 75.8% 57.2% 53.8% 55.4% 63.2% GPT-3.5-Turbo (16K) 75.7% 57.3% 54.1% 55.4% 63.1% MPT-30B-Instruct 53.7% 51.8% 52.2% 52.7% 56.3% LongChat-13B (16K) 68.6% 57.4% 55.3% 52.5% 55.0% 

> Table 6: Model performance when evaluated on the multi-document QA task with 20 total retrieved documents.

G.3 30 Total Retrieved Documents 

Model Index 0 Index 4 Index 9 Index 14 Index 19 Index 24 Index 29 Claude-1.3 59.1% 55.1% 54.8% 55.7% 56.4% 56.2% 59.9% Claude-1.3 (100K) 59.1% 55.1% 54.9% 55.7% 56.6% 56.1% 60.0% GPT-3.5-Turbo (16K) 73.4% 55.1% 50.5% 50.9% 51.8% 54.9% 63.7% MPT-30B-Instruct 51.6% 51.3% 51.2% 49.0% 49.6% 51.3% 54.1% LongChat-13B (16K) 66.9% 54.8% 52.5% 52.9% 52.2% 51.3% 55.1%

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>