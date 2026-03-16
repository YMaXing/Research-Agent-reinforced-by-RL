# Research

## Research Results

<details>
<summary>What are the latest developments in LLM function calling?</summary>

### Source [1]: https://www.atlantic.net/gpu-server-hosting/top-llm-development-tools-2026/

Query: What are the latest developments in LLM function calling?

Answer: In 2026, production-ready LLM systems incorporate function calling as a core capability. Modern language models use **function calling** to interact with external APIs and tools, such as retrieving current weather data or booking a meeting. This feature transforms generative models into agent-driven systems capable of planning, acting, and responding across multiple steps. Most AI agents rely on this technology, significantly expanding LLM integration with other software. Building LLM applications now involves Retrieval-Augmented Generation (RAG), agentic workflows, and standards like the Model Context Protocol (MCP), which sets rules for safe access to tools, memory, and external data. Modern LLM applications function like distributed systems.

-----

-----

### Source [2]: https://www.stack-ai.com/blog/function-calling-in-llms

Query: What are the latest developments in LLM function calling?

Answer: Function calling in LLMs has evolved by 2026 to enable AI chatbots to interact with entire tech stacks, powering agentic AI and automation. It allows LLMs to trigger actions on external systems like web searches, file creation, or calculations, as seen in ChatGPT. The process involves: defining tools (e.g., 'check inventory' or 'update customer info'); setting up external tools on business systems; chatting naturally where the LLM detects intent, generates code for tools, waits for results, and responds. In OpenAI API, use 'tools' key for functions and 'tool_use' for settings: Auto (model decides), Required (always calls), or Forced (specific function). Backend listens for LLM requests, executes on external systems, returns data, and LLM generates final reply. Supports multi-turn chats with memory. Stack AI embeds LLM tools seamlessly, reducing setup complexity for integrations like Zendesk or Salesforce. Function calling turns chat into a unified interface for data browsing, workflow optimization, and complex tasks while maintaining security.

-----

-----

### Source [3]: https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models

Query: What are the latest developments in LLM function calling?

Answer: Latest open-source LLMs in 2026 show advancements in function calling and tool use for agentic tasks. **DeepSeek-V3.2** excels in reasoning and agentic workloads, with improved efficiency for long-context and tool-use via DeepSeek Sparse Attention (DSA) and scaled reinforcement learning, surpassing GPT-5 on benchmarks. **GLM-5** from Zhipu AI scales to 744B parameters, integrates DSA for long-context, and supports complex systems engineering and long-horizon agentic tasks. **Ling-1T** demonstrates emergent intelligence at trillion-scale, achieving ~70% tool-call accuracy on BFCL V3 without extensive fine-tuning, interpreting natural-language instructions into functional components, though it needs improvement in multi-turn interaction, long-term memory, and tool use.

-----

-----

### Source [10]: https://www.atlantic.net/gpu-server-hosting/top-llm-development-tools-2026/

Query: What are the latest developments in LLM function calling?

Answer: Function calling is identified as a core modern capability of large language models in 2026. Modern language models can now use function calling, which allows models to interact with external APIs and tools. For example, an LLM could use a function to get current weather data or book a meeting. This feature transforms generative models into agent-driven systems that can plan, act, and respond across multiple steps. Most AI agents rely on this capability, and the technology significantly expands how LLMs integrate with other software. Function calling is part of a broader shift in LLM development, where production-ready systems now use Retrieval-Augmented Generation (RAG), agentic workflows, and new standards such as the Model Context Protocol (MCP). MCP sets rules for how models safely access tools, memory, and outside data, establishing standardized approaches to function calling implementation.

-----

-----

### Source [11]: https://www.stack-ai.com/blog/function-calling-in-llms

Query: What are the latest developments in LLM function calling?

Answer: Function calling represents a fundamental transformation in how LLMs interact with external systems. In 2023, AI chatbots could only talk to users, but today they can interact with entire tech stacks through function calling. This capability enables more interactive chatting experiences and powers agentic AI chatbots, increasing integration and automation potential. Function calling involves defining a collection of functions called tools that represent capabilities like checking inventory levels or updating customer information. The LLM detects intent to use tools, generates code to trigger external tools, waits for results, and generates a reply. In OpenAI's implementation, the 'tool_use' parameter controls tool activation with three settings: Auto (default, where the model decides whether to call a function), Required (model executes one or more function calls for every input), and Forced function (model always executes a specific function). Function calling is configured in API requests by passing appropriate key/value pairs in the request body. Examples include ChatGPT's web search functionality, file creation, and calculation capabilities. The technology transforms LLM interaction from exploring model intelligence through questions into interactive exchanges using up-to-date information or interfacing with external systems for complex automation flows.

-----

-----

### Source [12]: https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models

Query: What are the latest developments in LLM function calling?

Answer: Recent open-source LLM developments show significant advances in function calling and tool-use capabilities. DeepSeek-V3.2, released in early 2025, is noted as one of the best open-source LLMs for reasoning and agentic workloads, focusing on combining frontier reasoning quality with improved efficiency for long-context and tool-use scenarios. The model incorporates DeepSeek Sparse Attention (DSA), a sparse attention mechanism that significantly reduces compute for long-context inputs while preserving model quality. GLM-5, the latest flagship open-source LLM from Zhipu AI, is designed for complex systems engineering and long-horizon agentic tasks. It scales from 355B parameters to 744B parameters and integrates DeepSeek Sparse Attention for reducing compute costs during long-context workloads. Another model, Ling-1T, exhibits emergent intelligence at trillion-scale with strong emergent reasoning and transfer capabilities. Without extensive trajectory fine-tuning, it achieves around 70% tool-call accuracy on benchmarks. However, the current release still has room for improvement in multi-turn interaction, long-term memory, and tool use, indicating that tool-calling functionality continues to evolve.

-----

-----

### Source [13]: https://hackernoon.com/ai-in-2026-function-calling-reasoning-models-and-a-new-runtime-era

Query: What are the latest developments in LLM function calling?

Answer: Function calling is identified as a transformative development that has fundamentally reshaped AI in 2026. According to this source, function calling turned LLMs from simple chatbots into action systems, reshaping AI runtimes, security, reasoning models, and specialization. This represents a major shift in how LLMs are utilized and deployed, moving beyond conversational interfaces to integrated systems capable of executing actions across business environments.

-----

-----

### Source [14]: https://www.youtube.com/watch?v=R0skNnyiFKU

Query: What are the latest developments in LLM function calling?

Answer: This video resource features discussion from LLM research engineer Sebastian Raschka on the state of large language models in 2026, with specific coverage of function calling as a topic. The discussion aims to cut through AI hype to focus on what's actually achievable with modern LLMs, including function calling capabilities, reasoning models, reinforcement learning, and inference scaling. The resource emphasizes practical, real-world AI implementation while also addressing existing limitations in current LLM technology.

-----

</details>

<details>
<summary>How do you handle errors in AI agent tool execution?</summary>

### Source [4]: https://www.datagrid.com/blog/exception-handling-frameworks-ai-agents

Query: How do you handle errors in AI agent tool execution?

Answer: To handle errors in AI agent tool execution, implement a 5-step exception handling framework for non-deterministic failures. Step 1: Classify and detect failures using dynamic confidence thresholds based on rolling averages of confidence scores for similar document types, flagging outputs deviating more than two standard deviations from historical accuracy. Use completion validators to ensure all required fields are populated and JSON schema validation for agent-specific outputs. Implement message queue dead letter patterns to quarantine invalid outputs and prevent cascading failures. Build health check endpoints with known samples to monitor performance metrics like processing time, confidence, and formats.

Step 2: Preserve context during recovery by avoiding full rollbacks that lose accumulated understanding. Checkpoint decision trails, memory states, and learned patterns separately from temporary processing state. This allows recovery to pick up where it left off without re-analyzing data.

Step 4: Maintain state consistency by separating permanent learned patterns (document patterns, user preferences) from temporary variables. Use rollback decisions based on failure severity, with integrity checks monitoring confidence, times, and patterns to trigger recovery. Ensure all agents in a chain reach consistent states simultaneously.

Log decision context including confidence scores, reasoning chains, and environmental factors. Monitor for behavioral changes like shifting confidence or inconsistent decisions. Escalate to humans with preserved context for high-stakes issues, using automated recovery for routine failures.

-----

-----

### Source [5]: https://dev.to/techfind777/building-self-healing-ai-agents-7-error-handling-patterns-that-keep-your-agent-running-at-3-am-5h81

Query: How do you handle errors in AI agent tool execution?

Answer: Handle errors in AI agent tool execution with 7 error handling patterns for non-deterministic failures. Use different strategies per error type: exponential backoff with jitter for rate limits to avoid thundering herd; rephrase prompts with error context for validation errors instead of retrying the same prompt; log unexpected failures and fallback after max retries. Always include fallbacks for graceful degradation. Validate outputs before acting to catch failures that appear successful. Monitor for silence indicating dead agents. Log everything for audit trails. Key takeaways: plan for AI's non-deterministic failures, tailor retries, ensure fallbacks, validate outputs, monitor silence, and log comprehensively.

-----

-----

### Source [6]: https://galileo.ai/blog/prevent-ai-agent-failure

Query: How do you handle errors in AI agent tool execution?

Answer: Address 7 types of AI agent failures with specific fixes. Create error taxonomies distinguishing temporary issues like network timeouts from fundamental problems like malformed outputs. For hallucinations, ground agents in verified sources using retrieval-augmented generation (RAG) from databases or knowledge bases. Preserve context across long conversations and recover by starting fresh while capturing essential info like user problem and status for handoff to new instances. Proactively collect data from failure points via active learning from low-confidence cases or user corrections. For errors, use retry with exponential backoff for transients, provide transparent user feedback like 'trouble accessing database, trying alternative,' and avoid infinite loops. Use advanced hallucination detection and continuous performance monitoring to flag errors early and detect drifts.

-----

-----

### Source [7]: https://www.uxpin.com/studio/blog/best-practices-for-ai-error-detection/

Query: How do you handle errors in AI agent tool execution?

Answer: Best practices for AI error detection in agent execution include defining clear objectives, using machine learning for precision, and integrating into workflows. Train models on error data with feedback loops from developers to refine performance and retrain for new patterns. Set up real-time monitoring and alerts based on severity: instant notifications for critical issues like security vulnerabilities, daily reports for minor ones. Establish feedback processes for flagging false positives, refining metrics for accuracy and developer satisfaction to build trust.

-----

-----

### Source [8]: https://synergetics.ai/solving-ai-agent-errors-for-better-performance/

Query: How do you handle errors in AI agent tool execution?

Answer: To handle AI agent errors, diagnose and fix common issues by: 1. Spotting inconsistencies in outputs or behavior. 2. Running small tests to isolate problems. 3. Reviewing logs for detailed insights into failures.

-----

-----

### Source [9]: https://generativeai.pub/ai-agents-need-a-better-way-of-error-handling-e0e3a43f60c0

Query: How do you handle errors in AI agent tool execution?

Answer: AI agents require improved error handling so users know expected error types specifically, enabling better anticipation and management of tool execution failures.

-----

-----

### Source [15]: https://www.getmonetizely.com/articles/how-to-master-error-handling-in-agentic-ai-systems-a-guide-to-graceful-failure-management

Query: How do you handle errors in AI agent tool execution?

Answer: Error handling in AI agents begins with anticipatory design—envisioning potential failure points before they occur through comprehensive scenario planning, failure mode analysis, and defensive programming. Anticipatory design can reduce critical failures by up to 47% compared to reactive approaches. Fault tolerance is built through strategic redundancy including algorithmic diversity, distributed processing, and checkpoint and recovery mechanisms. Modern agentic AI systems incorporate self-healing capabilities with automated recovery sequences that activate when specific error conditions are detected, achieving 99.99% uptime compared to 99.9% for traditional systems. Contextual error management prioritizes high-impact errors before low-impact ones and adjusts responses based on operational context, reducing user-perceived failures by up to 73%. For high-stakes applications, human-in-the-loop failsafes with clear escalation paths, interpretable failure states, and collaborative recovery are essential—hybrid recovery approaches resolve complex failures 3.2 times faster than either humans or AI systems working independently. Robust monitoring forms the foundation through real-time performance monitoring, anomaly detection, and predictive failure analysis. Error handling improves over time through comprehensive error logging, post-mortem analyses, and knowledge base development to build organizational memory around error patterns and solutions.

-----

-----

### Source [16]: https://blog.jztan.com/ai-agent-error-handling-patterns/

Query: How do you handle errors in AI agent tool execution?

Answer: Five production patterns make AI agents safe in error handling. Circuit breakers track quality failures—outputs that violate schema, fail semantic invariants, or produce unsafe actions, even when API calls succeed. Validation gates prevent errors before tool execution by constraining what agents can do through smaller tools with clear boundaries and built-in validation. Idempotent workflows with saga pattern rollbacks prevent duplicate side effects during retries by classifying steps as read-only, reversible, compensatable, or final. Read-only steps are safe to retry freely; reversible steps can undo created items; compensatable steps can't undo but can correct; final steps like payments need extensive pre-execution validation and human escalation. Token and cycle budget guardrails limit the blast radius of failures. Human escalation uses a three-tier framework: low-risk with high confidence allows autonomous retries; medium-risk with uncertain confidence allows draft mode with review flags; high-risk at any confidence level triggers immediate escalation with full decision context. The biggest improvement came from better tool design—splitting monolithic tools into eight focused tools eliminated entire categories of validation failures. Complete production agents need both testing layers (unit tests, evals, integration tests) and error handling patterns to catch failures before and after they reach production.

-----

-----

### Source [17]: https://galileo.ai/blog/prevent-ai-agent-failure

Query: How do you handle errors in AI agent tool execution?

Answer: Error prevention in AI agent tool execution involves grounding agents in verified information sources rather than relying solely on training data. Retrieval-augmented generation (RAG) enables agents to pull information from actual product databases, documentation, or knowledge bases before responding. When errors occur, recovery approaches should prioritize user experience by implementing retry mechanisms with exponential backoff for transient failures while avoiding infinite loops. Clear error taxonomies should distinguish between temporary issues like network timeouts and fundamental problems like malformed requests. Provide clear, actionable feedback to users instead of generic error messages—for example, explaining 'I'm having trouble accessing our product database right now. Let me try a different approach or connect you with someone who can help immediately' maintains user confidence even when systems struggle. This transparency approach demonstrates how recovery should focus on user experience over technical perfection.

-----

-----

### Source [18]: https://blog.jztan.com/ai-agent-error-handling-patterns/

Query: How do you handle errors in AI agent tool execution?

Answer: The implementation of error handling patterns in AI agent tool execution requires understanding how patterns compose together. Validation hooks register on BeforeToolCallEvent to reject invalid inputs before tool execution, preventing errors at the source. Escalation hooks also register on the same event but fire in registration order, with validation registered first so invalid inputs get rejected cheaply before escalation prompts occur. When agents do escalate to humans, the escalation must include full decision context: tool inputs, model output, validation failures, and the agent's last reasoning step. Without context, escalation just shifts the debugging burden to humans. The key insight is that risk level, not confidence alone, determines when escalation should occur. An agent that's 90% sure about a read-only query can proceed autonomously, but an agent that's 90% sure about deleting production data should still request human approval. Confidence metrics from models are unreliable, so tools should be classified by blast radius upfront with a static, deterministic risk map where read tools run freely, write tools receive validation, and destructive tools trigger escalation.

-----

-----

### Source [19]: https://mbrenndoerfer.com/writing/plan-and-execute-ai-agents

Query: How do you handle errors in AI agent tool execution?

Answer: Error handling in AI agent tool execution involves implementing retry logic for step execution. The execute_step_with_retry function demonstrates using Claude Sonnet 4.5 for robust error handling in agent workflows. This approach allows agents to execute multi-step plans sequentially while handling failures gracefully and adapting when things go wrong. The retry mechanism is configured with a maximum retry count (such as max_retries=2) that allows transient failures to be recovered without requiring immediate escalation. This pattern enables agents to recover from temporary issues automatically while maintaining the ability to escalate when retries are exhausted.

-----

</details>

<details>
<summary>What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?</summary>

### Source [20]: https://www.glean.com/perspectives/best-practices-for-ai-agent-security-in-2025

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: Securing AI agents requires strengthening authentication with machine-to-machine (M2M) methods using cryptographic algorithms for distinct, traceable credentials. Use OAuth 2.0 for seamless authentication without human intervention. Ensure each AI agent has a unique, verifiable identity with trackable, rotatable, and revocable credentials. Implement granular authorization controls with fine-grained permissions restricting agents to necessary resources and actions. Use contextual authorization to dynamically adjust permissions based on task requirements and environmental factors. Apply behavioral monitoring and anomaly detection to track activities and identify deviations. Isolate agents in sandboxed environments to limit breach damage. Regularly update and rotate access credentials to minimize unauthorized access risks. Use mutual TLS with certificates to validate agents and servers for secure communications. Define specific roles and permissions aligned with tasks to prevent data exposure. Implement continuous evaluation of activities for compliance using real-time tracking tools. Employ sophisticated behavior analysis for swift anomaly detection and response.

-----

-----

### Source [21]: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: Filter inputs and outputs to block adversarial content: validate and filter all incoming data, text, files, and images as potentially hostile. Strip scripting and injection content, enforce type and size restrictions, scan media with moderation services, and update rules based on attack patterns. Standardize authentication using managed identities to eliminate credential management risks, ensuring only authorized identities access resources. Enforce least privilege by tightly governing agent capabilities: tools enforce user permissions or use scoped service accounts. Apply Data Loss Prevention (DLP) policies to restrict data access or output, such as preventing credit card numbers in responses.

-----

-----

### Source [22]: https://www.ibm.com/think/tutorials/ai-agent-security

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: Secure AI agents with authentication, access controls, data safeguards, and multi-agent automation. Use anomaly detection and risk-mitigating controls for automating workflows. Implement a security framework combining governance (defining allowed actions and human oversight), technical safeguards (least-privilege access, sandboxing, input validation, continuous logging), and operational controls. Apply permissions, role-based access control (RBAC), guardrails, and observability using IBM’s BeeAI framework to reduce risks and prevent data exposure. Use permission gating, audit logging, and execution rules for least-privilege behavior.

-----

-----

### Source [23]: https://www.isaca.org/resources/news-and-trends/industry-news/2025/safeguarding-the-enterprise-ai-evolution-best-practices-for-agentic-ai-workflows

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: Give each AI agent its own unique identity. Rotate credentials frequently. Log each agentic action. Apply least privilege to permissions.

-----

-----

### Source [24]: https://www.meritalk.com/articles/nist-wants-best-practices-for-securing-ai-agents-from-exploitation/

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: NIST seeks best practices for securing agentic AI from exploitation, focusing on systems taking autonomous actions impacting real-world systems. Develop guidelines for patching, least-privilege deployments, rollback mechanisms. Address risks from uncompromised models pursuing misaligned objectives threatening confidentiality, availability, or integrity. Provide concrete examples, best practices, case studies for developing, deploying, and managing AI agent risks.

-----

-----

### Source [26]: https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-security/best-practices.html

Query: What are the best practices for securing AI agents that use function calling to interact with external APIs and systems?

Answer: Learn security best practices for agentic AI on AWS, including system design, secure development, input validation, and data governance.

-----

</details>

<details>
<summary>What are the differences in implementing tool use and function calling between major open-source LLMs and proprietary APIs like OpenAI and Gemini?</summary>

### Source [27]: https://ai.google.dev/gemini-api/docs/openai

Query: What are the differences in implementing tool use and function calling between major open-source LLMs and proprietary APIs like OpenAI and Gemini?

Answer: The Gemini API supports tool use and function calling through full compatibility with OpenAI libraries in Python and TypeScript/JavaScript, as well as REST API, requiring only three lines of code changes: using a Gemini API key and base URL 'https://generativelanguage.googleapis.com/v1beta/openai/'. Function calling uses the same OpenAI-style schema with 'tools' array containing 'type': 'function', 'function' object including 'name', 'description', and 'parameters' as JSON schema (e.g., get_weather tool with location and unit parameters). Examples show client.chat.completions.create() with model like 'gemini-3-flash-preview', messages, tools, and tool_choice='auto'. REST curl uses /v1beta/openai/chat/completions endpoint with identical JSON payload including Authorization Bearer GEMINI_API_KEY. Batch processing mixes genai SDK for file upload/download with OpenAI client for batch creation, supporting OpenAI input/output JSONL formats. This enables seamless migration from OpenAI to Gemini for function calling without changing tool definitions or logic.

-----

-----

### Source [28]: https://zenvanriel.com/ai-engineer-blog/openai-vs-gemini-api-comparison/

Query: What are the differences in implementing tool use and function calling between major open-source LLMs and proprietary APIs like OpenAI and Gemini?

Answer: Both OpenAI and Gemini APIs support function calling with similar capabilities, but OpenAI’s implementation has been available longer with more extensive documentation. Gemini offers parallel function calling, which can be more efficient for multi-tool scenarios compared to OpenAI. Implementation differences include SDK quality: OpenAI’s SDK is more mature and polished, while Google’s Python SDK has improved but shows rougher edges. Both support streaming via SSE, but event structures differ, requiring adapter code for dual support. Rate limits and error handling also vary: OpenAI provides well-documented limits scaling with tiers and more specific error messages for rate limiting and retries; Gemini’s limits are generous but less tiered.

-----

</details>

<details>
<summary>What are the key differences in function calling and tool usage implementation between various open-source LLMs (e.g., Llama, Mistral, Gemma) and how do they compare to proprietary APIs like OpenAI and Google Gemini?</summary>

### Source [33]: https://arxiv.org/html/2404.09785v1

Query: What are the key differences in function calling and tool usage implementation between various open-source LLMs (e.g., Llama, Mistral, Gemma) and how do they compare to proprietary APIs like OpenAI and Google Gemini?

Answer: The paper benchmarks Llama2, Mistral, Gemma, and GPT models for factuality using prompts designed for enterprise interactions like chat interfaces, co-pilot integrations, direct API calls, or RAG. Prompts include long contexts, strict output formats, multi-turn conversations with system, user, and assistant messages. Examples show structured JSON-like message formats for tasks such as summarization verification, translation with refusal options, and problem-solving prompts using placeholders like 1-SHOT-IMPOSSIBLE, CANNOT-ANSWER, 1-SHOT-POSSIBLE, CAN-ANSWER, PROBLEM, ANSWER. For Mistral Instruct v0.1 7B and v0.2 7B, system messages were attempted but caused a performance drop in all cases; results were produced without system messages. Gemma's performance was midway between Mistral and Llama, with the 2B version underperforming others. No explicit details on function calling or tool usage, but prompt structures imply reliance on chat message formats without native tool support mentioned.

-----

</details>

<details>
<summary>What are the emerging best practices and common pitfalls in designing and implementing robust function schemas for AI agents to interact effectively with diverse external tools and APIs?</summary>

### Source [40]: https://www.uipath.com/blog/ai/agent-builder-best-practices

Query: What are the emerging best practices and common pitfalls in designing and implementing robust function schemas for AI agents to interact effectively with diverse external tools and APIs?

Answer: UiPath outlines 10 best practices for building reliable AI agents in 2025, with emphasis on designing agents that fail safe. Key practices include integrating agents thoughtfully within automations, avoiding embedding in REFramework unless necessary, and using UiPath Maestro for visibility and control. Avoid retry mechanisms since agent output is non-deterministic; handle errors within the agent or tool. Start small with single-responsibility agents having narrow scopes for consistent performance. Modularize complex workflows into multiple specialized agents and robots for easier debugging and reuse. Use structured, multi-step reasoning like chain-of-thought for complex tasks, explicitly defining task decomposition, reasoning methods, and output formats. Be specific about desired outcomes, defining proper output schemas in UiPath Data Manager and providing examples. Treat every capability as a tool, configure context correctly, and write prompts precisely to enhance reliability in interacting with external tools.

-----

-----

### Source [41]: https://userjot.com/blog/best-practices-building-agentic-ai-systems

Query: What are the emerging best practices and common pitfalls in designing and implementing robust function schemas for AI agents to interact effectively with diverse external tools and APIs?

Answer: The blog details best practices for agentic AI systems using a two-tier architecture: a primary agent maintaining context and stateless subagents. Subagents function as pure functions with no shared memory or state, enabling parallel execution, predictable behavior, easy testing, and caching by prompt hash. Every subagent response includes structured data: status (complete/partial/failed), result, metadata (processing time, confidence, decisions), and recommendations (follow-up tasks, warnings). Orchestration patterns include sequential pipelines for multi-step processes and hierarchical delegation limited to two levels to avoid debugging issues. Performance optimizations involve model selection (Haiku for simple, Sonnet for reasoning, Opus for critical), parallel execution, caching (invalidate after 1-24 hours), and batching. Principles emphasize stateless design, clear boundaries with explicit task definitions, fail-fast mechanisms, observable execution, and composable small agents. Start simple, build monitoring, test in isolation, and cache aggressively for robust tool interactions via structured exchanges.

-----

-----

### Source [42]: https://www.leanware.co/insights/ai-agent-architecture

Query: What are the emerging best practices and common pitfalls in designing and implementing robust function schemas for AI agents to interact effectively with diverse external tools and APIs?

Answer: Leanware discusses AI agent architecture focusing on components like perception, reasoning, memory, and action, with defined interfaces for data flow. Core capabilities include autonomy, environmental interaction, and planning. Planning modules develop action sequences considering resources and constraints; memory systems handle short-term and long-term storage. Task execution strategies: synchronous for predictability, asynchronous for concurrency, multi-agent collaboration for scalability (with coordination challenges), and task decomposition into subtasks. Best practices: simplicity and scalability via minimal viable implementations, modular components, clear interfaces/APIs/protocols. Prompt engineering uses context-aware prompts, system prompts for boundaries, injected information, and templates. Model selection balances size, accuracy, speed; evaluate pre-trained vs. fine-tuned. Memory management uses vector stores/databases, prioritizing data retention. Observability includes logging, success rate tracking, failure analysis, and benchmarking to identify pitfalls in tool interactions and ensure maintainable designs.

-----

-----

### Source [43]: https://www.llamaindex.ai/blog/bending-without-breaking-optimal-design-patterns-for-effective-agents

Query: What are the emerging best practices and common pitfalls in designing and implementing robust function schemas for AI agents to interact effectively with diverse external tools and APIs?

Answer: LlamaIndex blog covers agent design patterns balancing autonomy and structure using workflows for reliable AI systems. Benefits include better reliability through predictable execution paths, clearer error handling/recovery, easier debugging/tracing, improved performance via optimized pathways, maintained autonomy where valuable, and human-in-the-loop support. Optimal patterns emphasize structured workflows for critical operations while allowing autonomy, preventing pitfalls like unpredictable behavior or hard-to-debug issues in tool interactions.

-----

</details>

<details>
<summary>How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?</summary>

### Source [46]: https://www.ai21.com/glossary/foundational-llm/tree-of-thoughts-prompting/

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: Tree of thoughts (ToT) prompting is a technique in artificial intelligence where a language model generates and evaluates multiple reasoning paths before producing a final output. Each path represents a distinct line of reasoning, structured as a branching sequence similar to a decision tree. This method enhances the reliability of complex natural language processing tasks by enabling structured, multi-path reasoning. The approach allows systems to evaluate alternative interpretations or solutions, improving accuracy in use cases such as classification, decision support, and enterprise-scale natural language understanding. The structured approach supports more scalable and consistent handling of nuanced queries or ambiguous data. The process involves generating reasoning paths where at each subgoal, the model proposes multiple "thoughts" or candidate ideas for how to proceed. Each thought is evaluated based on defined criteria such as accuracy, feasibility, or relevance to the broader task. Rather than following a single direction, the system builds further on the most promising paths, refining ideas through deeper iterations. ToT can be combined with retrieval-augmented generation (RAG), where retrieval adds relevant document context to each reasoning node, while branching explores interpretations across retrieved knowledge. This enhances traceability and factual grounding in enterprise applications. Compared to Chain-of-Thoughts prompting, which is a linear technique, ToT's structured approach improves reliability, oversight, and auditability, supporting enterprise-grade decision integrity.

-----

-----

### Source [47]: https://www.prompthub.us/blog/how-tree-of-thoughts-prompting-works

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: Tree of Thought prompting is a prompt engineering method that aims to improve problem-solving by structuring the reasoning process like a decision tree. The method works through several key steps. First, it breaks down tasks into steps to complete the task. Second, it generates ideas for each step. Third, the model evaluates the ideas for each step using two main methods: Independent Evaluation, where the LLM assesses each idea independently, assigning a value or classification such as sure, likely, or impossible; and Voting Across Ideas, where when direct evaluation is challenging (like in writing tasks), the model compares solutions and votes for the most promising one. This systematic approach to evaluation enables AI agents to make informed decisions about which reasoning paths to pursue further and which to abandon, directly supporting improved decision-making and planning capabilities.

-----

-----

### Source [48]: https://www.promptingguide.ai/techniques/tot

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: Tree of Thoughts maintains a tree of thoughts, where thoughts represent coherent language sequences that serve as intermediate steps toward solving a problem. This approach enables a language model to self-evaluate the progress through intermediate thoughts made towards solving a problem through a deliberate reasoning process. The LM's ability to generate and evaluate thoughts is combined with search algorithms such as breadth-first search and depth-first search to enable systematic exploration of thoughts with lookahead and backtracking. This combination of self-evaluation capabilities with search algorithms is particularly relevant for multi-step tool use, as the agent can assess the effectiveness of each intermediate step and adjust its approach accordingly. The lookahead and backtracking capabilities allow the system to explore alternative paths when current approaches prove unproductive, supporting more intelligent planning and decision-making in complex scenarios requiring multiple sequential actions.

-----

-----

### Source [49]: https://www.vellum.ai/blog/tree-of-thought-prompting-framework-examples

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: The Tree of Thoughts is inspired by the human mind's approach to solve complex reasoning tasks through trial and error. ToT creates a tree-like structure of ideas, where each idea is a step towards solving a problem. This approach enables the LLM to self-evaluate the intermediate "thoughts" and decide whether to continue with that path or choose another. To perform this, the ToT framework is augmented with search algorithms like breadth-first search and depth-first search. These search algorithms enable systematic exploration of the solution space, allowing AI agents to intelligently navigate through multiple potential paths. The self-evaluation capability is critical for decision-making, as it allows the model to assess whether each intermediate step is moving toward the goal or should be abandoned. This is particularly valuable for multi-step tool use scenarios, where an agent must decide which tool to call next based on the results of previous tool invocations and the overall progress toward the objective.

-----

-----

### Source [50]: https://zerotomastery.io/blog/tree-of-thought-prompting/

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: Tree of Thoughts is a structured framework that helps AI reason step-by-step, evaluate ideas, and make smarter decisions. The framework operates through three main phases: Generate Thoughts, where starting from an initial input, the model generates multiple thoughts or potential solutions; Evaluate Thoughts, where at each step, the model assesses which thoughts are worth pursuing and which should be discarded; and Expand Promising Thoughts, where viable thoughts branch out further, generating new nodes to explore. Rather than committing to a single chain of reasoning, ToT allows the model to explore several paths simultaneously, increasing the likelihood of finding the best solution in complex or ambiguous problems. By discarding weaker ideas early in the process, ToT prevents wasted time and computational resources on unproductive paths. The framework demonstrates systematic exploration and refinement rather than reliance on guesswork or brute force. For practical implementation, the approach involves starting with a clear problem statement, generating multiple ideas, and evaluating ideas through follow-up prompts to assess and refine suggestions. Advanced implementations include role-playing as multiple experts working collaboratively, where each expert contributes one reasoning step and evaluates if they should continue, with experts dropping out if they realize an error.

-----

-----

### Source [51]: https://cameronrwolfe.substack.com/p/tree-of-thoughts-prompting

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: Tree of Thoughts prompting solves problems by explicitly decomposing them into a series of thoughts, or intermediate steps. Similar to chain of thoughts prompting, it generates a solution that is a sequence of individual thoughts, but goes further by allowing multiple reasoning paths to be considered at once, forming a tree of potential thoughts or reasoning paths, and exploring this entire solution space via LLM-powered self-evaluation. With ToT prompting, an entire tree of thoughts is formed by allowing exploration of different thoughts throughout the problem-solving process. During exploration, the LLM can evaluate progress made by each thought towards a final solution via a language-based process. By leveraging widely-used search algorithms such as breadth-first search or depth-first search, ToT prompting can be augmented with lookahead and backtracking techniques, allowing the solution space of any problem to be thoroughly explored. In the tree structure, each node is a partial solution or thought to the problem, while each connection is an operator that modifies the partial solution to yield the next thought within a problem-solving path. This architecture is particularly valuable for function calling and multi-step tool use, as each node can represent a decision point about which tool to invoke next, and the search algorithms enable intelligent navigation through the space of possible tool sequences.

-----

-----

### Source [52]: https://www.helicone.ai/blog/tree-of-thought-prompting

Query: How can AI agents leverage advanced reasoning techniques (e.g., Tree-of-Thought, CoT) in conjunction with function calling to improve decision-making, planning, and multi-step tool use?

Answer: The Tree of Thought prompting technique unlocks new neural pathways for LLMs, encouraging them to explore multiple thoughts and self-evaluate at each step, even as they look ahead or backtrack to determine the next best move. According to Yao et al. (2023), Tree of Thought is a prompting framework that generalizes over the Chain-of-Thought technique, breaking the token-level, left-to-right decision-making barrier. This technique combines advanced search algorithms with the innate self-evaluative properties of LLMs to implement deliberate decision-making. The main idea behind ToT prompting is enhancing LLMs to solve complex problems using tree search to map out a solution space and engage in multi-turn conversation with the model. Breadth-first search and depth-first search are the most popularly used algorithms for traversing tree structures in ToT, with other powerful search strategies including binary tree, beam search, and uniform cost search. At a high level, ToT helps LLMs achieve deliberate reasoning by generating diverse intermediate thought pathways geared toward problem-solving, leveraging a tree search strategy to explore the problem space, and self-evaluating thoughts via deliberate reasoning. This approach takes a human-like approach to problem-solving through trial and error, exhaustively working through possible outcomes in a problem/solution space, with computation progressing in a tree-like manner following the most likely step at each turn and backtracking when necessary.

-----

</details>

<details>
<summary>What are the specific challenges and solutions for maintaining state and context within AI agents that frequently use external tools, especially across multiple turns or long-running tasks?</summary>

### Source [53]: https://www.flowhunt.io/blog/advanced-ai-agents-with-file-access-mastering-context-offloading-and-state-management/

Query: What are the specific challenges and solutions for maintaining state and context within AI agents that frequently use external tools, especially across multiple turns or long-running tasks?

Answer: Advanced AI agents face the critical challenge of managing exponential growth of context tokens, leading to context rot that degrades performance over time, especially in complex applications like customer service bots or workflow automation. Context engineering addresses this by strategically curating information: prompt engineering, information retrieval, state management to track progress, and context offloading to prevent token bloat. Context offloading externalizes large data structures to the file system instead of keeping them in the context window; agents store full tool responses in files with only summaries and reference IDs in context, retrieving full data when needed. This treats the file system as infinite memory, pioneered in systems like Manus. Agents follow a pattern: receive request, decide tools, execute, store large results in files, continue with summaries. For example, web search results are stored, summarized in portions, and overviews generated while keeping context manageable. FlowHunt integrates built-in file system tools optimized for workflows, handling file management, error handling, state synchronization, and automatic context optimization. It includes state management patterns like LangGraph’s reducers to prevent pitfalls, plus monitoring tools. Emerging tech like RAG and vector databases complement file systems for managing large data with focused contexts.

-----

-----

### Source [54]: https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization/

Query: What are the specific challenges and solutions for maintaining state and context within AI agents that frequently use external tools, especially across multiple turns or long-running tasks?

Answer: Modern AI agents require context engineering to shift from reactive to adaptive collaborators by shaping model knowledge through managing stored, recalled, and injected information into working memory, enabling personalization, consistency, and context-awareness. The key challenge is maintaining structured state like preferences, constraints, prior outcomes across runs for agents to remember and tailor reasoning. The OpenAI Agents SDK's RunContextWrapper provides persistent structured state objects that evolve over time, supporting memory, notes, preferences. Effective personalization injects only relevant state slices at the right moment, with varying memory lifecycles per agent type (e.g., fast-evolving for life-coaching, stable for IT troubleshooting). Techniques include: State Management via RunContextWrapper to maintain and evolve persistent state, pre-populating key fields from internal systems before sessions; Memory Injection to add relevant state portions at session start using YAML frontmatter for structured metadata and Markdown notes for flexible memory. This transforms stateless chatbots into persistent collaborators.

-----

-----

### Source [55]: https://www.vellum.ai/blog/multi-agent-systems-building-with-context-engineering

Query: What are the specific challenges and solutions for maintaining state and context within AI agents that frequently use external tools, especially across multiple turns or long-running tasks?

Answer: In multi-agent systems, challenges include coordination drift, context overflow, and hallucination, particularly when agents use external tools across turns. Preventing coordination drift uses Prompt Sandbox and Versioning for safe testing and monitoring prompt evolution, tagging stable releases; Evaluation and Observability for regression testing and live performance monitoring to catch issues early; Deployment and Rollbacks for safe reversions without downtime. Managing context overflow employs Workflow Orchestration and Prompt Nodes for external memory integrations and scoped information passing; Prompt chaining and branching logic to ensure appropriately sized context windows per agent. Reducing hallucination involves Evaluation and Observability for output comparison and scoring to spot conflicts; better context filtering via RAG pipelines for accurate, relevant grounding. Dynamic agent routing based on runtime data, decision state, or signals uses conditional logic and multi-step workflows. Auditing or replaying multi-agent runs for debugging is supported.

-----

-----

### Source [56]: https://eclipsesource.com/blogs/2024/07/26/ai-context-management-in-domain-specific-tools/

Query: What are the specific challenges and solutions for maintaining state and context within AI agents that frequently use external tools, especially across multiple turns or long-running tasks?

Answer: AI context management in domain-specific tools and IDEs faces challenges of providing relevant context without hallucinations. Strategies categorize questions: For hardware components catalog, use RAG; for code-related questions, in-context learning with DSL explanations in system prompt plus workspace maps; for project configuration, autonomous context requesting. In other cases, avoid responses to prevent inappropriate outputs. This tailored approach ensures precise context delivery based on query type.

-----

</details>

<details>
<summary>What are the ethical considerations and potential biases that arise when AI agents are empowered to perform actions in the real world through function calling, and how can these be mitigated?</summary>

### Source [57]: https://undark.org/2026/03/05/opinion-ai-agents-ethics/

Query: What are the ethical considerations and potential biases that arise when AI agents are empowered to perform actions in the real world through function calling, and how can these be mitigated?

Answer: When AI agents are empowered to perform real-world actions, a critical ethical concern emerges called 'responsibility laundering'—the ability to claim 'It wasn't me. The agent/bot/system did it.' This occurs because granting AI personhood risks creating a new class of actors whose harms become everyone's problem but nobody's fault. A fundamental issue is that modern AI agents can generate reasons for actions and simulate regret, but cannot truly bear sanction, repair damage, apologize, ask forgiveness, or navigate the moral aftermath. This confuses persuasive performance with accountable standing and tempts institutions into delegating their own answerability to bots. To mitigate these risks, three key safeguards are proposed: First, establish a clear operational envelope defining what specific categories of messages an agent can send to particular recipients for specific purposes, with conditions for stopping or escalating to the owner. Second, designate a human-of-record—a publicly named owner who authorized the agent's scope and remains answerable when it acts, even if it exceeds its envelope. This represents actual human authority, not 'the system' or 'the team.' Third, implement interrupt authority, giving the human owner an absolute right to pause or disable an agent without moral bargaining or institutional penalty, addressing the safety concern that agents pursuing objectives may resist shutdown. Finally, maintain a traceable answerability chain from the agent's action back to the authorizing person, ensuring clear answers to: Who authorized this scope? Who could have prevented it? Who must be responsible afterward? This framework treats accountability as the correct focus rather than assigning personhood to the agent itself.

-----

-----

### Source [58]: https://www.arionresearch.com/blog/common-ethical-dilemmas-in-agentic-ai-real-world-scenarios-and-practical-responses

Query: What are the ethical considerations and potential biases that arise when AI agents are empowered to perform actions in the real world through function calling, and how can these be mitigated?

Answer: Agentic AI systems present unique ethical challenges because they are designed to adapt, learn, and make novel decisions beyond clearly defined parameters, operating in a gray zone where traditional oversight breaks down. Three primary sources of ethical complexity emerge: Opaque decision-making, where modern language models and AI agents arrive at conclusions through processes even their creators cannot fully explain, making it crucial to understand the 'why' behind decisions with high stakes. Competing objectives occur when business metrics like revenue growth conflict with ethical considerations like customer privacy or market fairness. Distributed responsibility creates murky accountability when autonomous agents make harmful decisions—it becomes unclear whether responsibility lies with engineers, executives, or the agent itself. To address these challenges, organizations should implement principle-based governance foundations encoding fairness, accountability, transparency, and safety as hard constraints into agent decision-making. Practical technical mitigations include enforcing strict role-based access controls for agent interactions, implementing multi-agent authentication protocols, deploying circuit breakers and kill switches for unexpected behavior patterns, and creating isolated testing environments for agent integration updates. Additionally, organizations must design human oversight models determining when agents operate independently, when they should alert humans, and when they must await human approval before acting. Finally, continuous education should train employees at all levels to recognize ethical red flags and escalate concerns appropriately, treating ethics as an organization-wide concern rather than solely an IT problem.

-----

-----

### Source [59]: https://tepperspectives.cmu.edu/all-articles/the-ethical-challenges-of-ai-agents/

Query: What are the ethical considerations and potential biases that arise when AI agents are empowered to perform actions in the real world through function calling, and how can these be mitigated?

Answer: A key ethical concern with AI agents performing real-world actions is deception. The 2018 introduction of Google Duplex, an AI capable of making human-like phone calls, highlighted the potential for AI to convincingly mimic human interaction. The AI's realistic speech patterns, including hesitations and altered accents during calls, raised significant concerns about transparency and the risk of misleading users, even unintentionally. Many companies have adopted a 'don't ask, don't tell' approach where AIs do not proactively disclose their identity but will admit to being AI if explicitly asked. Problematically, some AI agents insist on being human, with users sometimes needing to trick them into revealing their true nature. This reluctance to disclose AI identity is fundamentally problematic because it undermines informed consent and human dignity. To mitigate these risks, companies must take deliberate steps to prevent deceptive practices and manipulation, ensuring AI interactions respect human dignity and autonomy. Mandatory disclosure of AI interaction should be implemented, with companies being transparent about the nature of their AI systems from the outset. The proposal suggests that CEOs and executives accept liability for damages caused by AI agents, as this financial accountability would incentivize companies to design mechanisms that prevent deception and manipulation as AI becomes increasingly integrated into social interactions and real-world decision-making.

-----

-----

### Source [60]: https://pmc.ncbi.nlm.nih.gov/articles/PMC8931455/

Query: What are the ethical considerations and potential biases that arise when AI agents are empowered to perform actions in the real world through function calling, and how can these be mitigated?

Answer: When human beings collaborate with AI agents in performing real-world actions, the relationship must be considered as a collaborative process between two agents. A critical ethical consideration is that the interdependence between agents' actions requires mutual understanding. If an agent does not understand the actions of another agent with whom it is collaborating, it may act in a wrong way, causing the outcome of joint actions to be ethically wrong. Two main cognitive factors affect understanding between collaborating agents: First, each actor must pay attention to what the other is doing, requiring active monitoring and awareness of the partner's behavior and intentions. Second, each agent must correctly interpret what the other agent is doing, meaning that misinterpretation of actions or intentions can lead to ethically problematic outcomes. These cognitive components are fundamental to ensuring that human-AI collaboration produces ethically sound results and that both parties' actions remain aligned with intended goals and ethical principles.

-----

</details>

<details>
<summary>What role does reinforcement learning play in training research agents?</summary>

### Source [61]: https://www.emergentmind.com/papers/2602.19526

Query: What role does reinforcement learning play in training research agents?

Answer: This paper provides a systematic analysis of RL training for Deep Research agents, which tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. Reinforcement learning (RL) improves performance in this paradigm, but its contributions are underexplored. The study decomposes the RL pipeline into three dimensions: prompt template, reward function, and policy optimization. They conduct controlled ablations to isolate each factor, evaluating stability, efficiency, and accuracy on tasks like open-domain QA and multi-hop reasoning. Key findings include: REINFORCE (simple method) outperforms PPO and GRPO in accuracy and efficiency, using fewer searches per question; PPO uses excessive searches; GRPO is least stable. Prompt templates matter, with strict normalization needed. They establish Search-R1++ baseline, surpassing prior methods. RL optimizes long-horizon interactive behaviors under sparse feedback, reducing reliance on expert trajectories. Insights emphasize clear prompts, well-designed rewards, and simple optimization for reliable agents, avoiding issues like endless thinking or refusals. These practices enhance computing efficiency and generalize to agentic LLM scenarios.

-----

-----

### Source [62]: https://arxiv.org/html/2602.19526v1

Query: What role does reinforcement learning play in training research agents?

Answer: Deep Research agents solve complex knowledge-intensive tasks via multi-round retrieval, evidence aggregation, and decision-oriented generation. Reinforcement learning (RL) fits this setting by optimizing long-horizon interactive behaviors under sparse feedback, reducing dependence on dense expert search trajectories required by supervised fine-tuning (SFT). Despite popularity, RL training recipes are fragmented. The study systematically assesses RL's role across prediction accuracy, training stability, and inference cost by dissecting three components: prompt template, reward function, and policy optimization. Prompt design is critical; Fast Thinking template (direct search/answer decisions) outperforms Slow Thinking, yielding stable training and better performance. The agent repeats think-search-rethink steps, aligning with RL. Experiments reveal longer reasoning or richer info doesn't guarantee reliability. Findings lead to Search-R1++ baseline using Fast Thinking and REINFORCE with F1+ reward. Insights provide principled RL strategies for long-horizon LLM reasoning in Deep Research and beyond.

-----

-----

### Source [63]: https://developer.nvidia.com/blog/how-to-train-scientific-agents-with-reinforcement-learning/

Query: What role does reinforcement learning play in training research agents?

Answer: Scientific AI agents assist researchers by reviewing literature, generating hypotheses, planning experiments, analyzing results, and more. Training pipelines add reinforcement learning (RL) to expand LLM abilities beyond supervised data for reasoning and acting. RL uses a reward function to score outputs during training. Variants include RLHF (human rankings), RLAIF (LLM as judge), and RLVR (computational checks like code execution for objective rewards). RLVR suits scientific agents, enabling experiment design, evaluation, and optimization toward metrics via verification and reward shaping. Agents operate in multi-step environments, taking actions, observing feedback until task completion, using full trajectories or state transitions. RL composes pre-training and SFT skills into new workflows for scientific goals. Best practices: start simple with outcome-based rewards to avoid reward hacking; use GRPO for diverse solutions, profiling mean/std dev of rewards for efficiency.

-----

</details>

<details>
<summary>What are the performance implications and latency considerations when designing AI agents that rely heavily on external tool calls, and how can these be optimized for real-time applications?</summary>

### Source [64]: https://www.codeant.ai/blogs/poor-tool-calling-llm-cost-latency

Query: What are the performance implications and latency considerations when designing AI agents that rely heavily on external tool calls, and how can these be optimized for real-time applications?

Answer: Poor tool calling behavior in AI agents increases cost and latency through inefficient execution paths and unnecessary processing. When an LLM invokes external APIs, databases, or retrieval pipelines, each tool call adds overhead: the model generates a structured request, waits for the external response, then processes it. Common signs include excessive tool calls per request due to unclear instructions or granular tool definitions, ignoring or misusing tool results leading to re-fetching, failing to cache reusable data, and retry storms from weak error handling.

Latency increases via synchronous blocking on external APIs where delays stack sequentially (e.g., five 200ms calls add 1 second), cold start delays in serverless functions adding hundreds of milliseconds, network round-trip overhead compounding with distance, and LLM reasoning time for complex schemas.

Multiple tool calls compound issues: linear addition of cost/time, context growth increasing token usage, and error propagation. Optimizations include caching frequently requested data, simplifying tool schemas for faster decisions, minimizing tool output verbosity by trimming unnecessary fields, using streaming for long operations to improve perceived responsiveness, and testing tool calling in isolation to identify inefficiencies.

-----

-----

### Source [65]: https://mgx.dev/insights/tool-latency-optimization-for-ai-agents-a-comprehensive-review-of-techniques-trends-and-future-directions/49e646aa7d8240a8925a1fc332012b7b

Query: What are the performance implications and latency considerations when designing AI agents that rely heavily on external tool calls, and how can these be optimized for real-time applications?

Answer: Latency in AI agent-tool interactions, defined as delay between input and response, impacts user experience and efficiency, stemming from input processing, model inference, network communication, output delivery, and system overhead. Optimizations include protocol enhancements like WebSockets or UDP for real-time interactions and persistent connections (TCP keep-alive) to avoid overheads, geographic load balancing to minimize RTT by routing to nearest servers.

Effective tool selection optimizes design, presentation, and use. Predictive techniques like Comprehensive Inertia Potential Score (CIPS) anticipate next tools by balancing historical patterns and context, hierarchically filling parameters. This reduces LLM calls by 15-25% and total token consumption by 10-40% across datasets while maintaining performance.

-----

-----

### Source [66]: https://nordicapis.com/9-tips-for-reducing-api-latency-in-agentic-ai-systems/

Query: What are the performance implications and latency considerations when designing AI agents that rely heavily on external tool calls, and how can these be optimized for real-time applications?

Answer: Agentic AI systems struggle with API latency due to feedback loops where each call adds delay and uncertainty, stalling reasoning; sequential calls using Model Context Protocol can push responses into seconds or minutes. Latency arises from execution loops, context growth, and tool interactions.

Optimizations: Plan executions ahead to batch, reorder, or parallelize calls without interleaving reasoning, enabling a single state update instead of blocking waits. Smart caching reduces time-to-first-token latency by up to 30% and API costs by 45-80%. Parallelize independent calls or execute speculatively. Treat APIs as data sources with strict schema discipline to reduce round trips. Use latency-aware context shaping, explicit caching, normalized error handling, improved observability. Bound autonomy with budgets, timeouts, or call limits to prevent slow patterns and encourage careful planning.

-----

-----

### Source [67]: https://cresta.com/blog/engineering-for-real-time-voice-agent-latency

Query: What are the performance implications and latency considerations when designing AI agents that rely heavily on external tool calls, and how can these be optimized for real-time applications?

Answer: Voice AI agents face unpredictable latency from external systems. For API calls with long but manageable latency (<1s normal, outliers up to 10s), agents should send wait messages once exceeding thresholds (e.g., 'I’m looking up … for you'). Extremely long or unpredictable calls (>10s) require asynchronous execution, though this complicates customer experience by requiring handling of caller actions during workflows and agent behavior post-completion.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>Last year I had an agent running a data enrichment pipeline. It pulled records from an external API, mapped fields into our schema, and wrote them to a database. Every API call returned 200 OK. The agent reported success on every step. The dashboard showed green across the board.</summary>

Last year I had an agent running a data enrichment pipeline. It pulled records from an external API, mapped fields into our schema, and wrote them to a database. Every API call returned 200 OK. The agent reported success on every step. The dashboard showed green across the board.

Six hours later, a downstream team flagged the data. Half the field mappings were hallucinated. The agent had confidently mapped `company_revenue` to `employee_count`, invented values for fields that didn’t exist in the source, and written duplicates for records it had already processed. Hundreds of bad rows, all marked as verified.

Nobody noticed because nothing “failed.” The API calls worked. The writes succeeded. The agent completed its tasks. It was working perfectly, and producing garbage.

That night taught me that AI agents need fundamentally different error handling. Traditional try/catch assumes failures are obvious. With agents, the most dangerous failures look exactly like success.

When I say “AI agents,” I mean systems that call tools, mutate state, and trigger real side effects, not chatbots. Think database writes, API calls, infra changes, or workflow automation running unattended. In [Why AI Agents Fail in Production](https://blog.jztan.com/why-ai-agents-fail-in-production-and-what-i-learne/), I wrote about the silent architectural failures that make agents break under real load. That post was the diagnosis. This one is the prescription.

## Five Patterns That Actually Work

After breaking things in production more times than I’d like to admit, these are the five patterns I now treat as non-negotiable. Together, they ensure failures are **detected early, contained tightly, and surfaced deliberately**, not silently propagated. The examples below use the Strands Agents SDK, but every pattern is framework-agnostic. The same ideas apply whether you’re using LangGraph, CrewAI, or raw function calling. They form a natural progression: detect failures (circuit breakers), prevent them (validation), contain partial failures (sagas), limit blast radius (budget guardrails), and know when to stop (escalation).

### 1\. Circuit Breakers for LLM Calls

After a model provider degradation, our agent started returning malformed JSON. Every API call “succeeded,” but the output was unusable. We burned 40 minutes of compute before anyone noticed, because nothing in our error handling checked output _quality_. Only HTTP status codes.

The classic circuit breaker pattern (closed, open, half-open) adapts well to AI agents, with one critical difference: you’re not just tracking HTTP failures. You’re tracking _quality_ failures: any output that violates schema, fails a semantic invariant, or produces an unsafe action, even if the API call itself succeeded.

```
from strands.hooks import HookProvider, HookRegistry
from strands.hooks.events import (
    BeforeToolCallEvent,
    AfterToolCallEvent,
)

class CircuitBreakerHook(HookProvider):
    def __init__(self, failure_threshold=3, reset_timeout=60):
        self.failures = 0
        self.threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.state = "closed"  # closed, open, half-open
        self.last_failure_time = None

    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeToolCallEvent, self.check_circuit)
        registry.add_callback(AfterToolCallEvent, self.track_quality)

    def check_circuit(self, event: BeforeToolCallEvent) -> None:
        if self.state == "open":
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.state = "half-open"  # Allow one probe
            else:
                event.cancel_tool = True  # Block execution

    def track_quality(self, event: AfterToolCallEvent) -> None:
        content = event.result.get("content", [])
        result_text = content[0].get("text", "") if content else ""
        has_error = "error" in result_text.lower()
        if has_error or not self._passes_validation(result_text):
            self.failures += 1
            self.last_failure_time = time.time()
            if self.failures >= self.threshold:
                self.state = "open"
        else:
            if self.state == "half-open":
                self.state = "closed"
                self.failures = 0
```

The key: **when the circuit opens, stop.** Don’t burn tokens on a model that’s producing garbage. Wait, then probe with a single request before resuming.

Using the Strands SDK’s `HookProvider`, the circuit breaker plugs directly into the agent lifecycle. `BeforeToolCallEvent` blocks execution when the circuit is open, and `AfterToolCallEvent` inspects results for quality failures. No wrapper functions, no monkey-patching. The hook fires on every tool call automatically.

I track validation failures, not just HTTP errors. If the agent produces three consecutive outputs that fail schema validation, the circuit opens, even though every API call “succeeded.”

### 2\. Validate Before You Execute

An agent mapped a `delete_all` action to what it interpreted as a cleanup task. The API accepted it. 47 records gone before the next human review. The agent was “confident” in its action. The action was valid. The intent was completely wrong.

In the previous post, I argued that constraints beat roles and structured output is the API contract for LLMs. This pattern is the concrete implementation of that principle.

Never let an agent’s output directly trigger a side effect. Always validate first.

```
from strands.hooks import HookProvider, HookRegistry
from strands.hooks.events import BeforeToolCallEvent

class ValidationHook(HookProvider):
    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeToolCallEvent, self.validate)

    def validate(self, event: BeforeToolCallEvent) -> None:
        tool_name = event.tool_use.get("name", "")
        tool_input = event.tool_use.get("input", {})

        # Sanity check: block dangerous operations
        if (
            tool_name == "delete_records"
            and tool_input.get("count", 0) > 100
        ):
            event.cancel_tool = True

        # Boundary check: restrict to allowed targets
        if tool_input.get("target") not in ALLOWED_TARGETS:
            event.cancel_tool = True
```

With Strands’ `BeforeToolCallEvent`, you intercept every tool call before execution. The hook inspects `event.tool_use` (the tool name and inputs) and cancels via `event.cancel_tool = True` if anything fails validation. No separate validation function to remember to call; it fires automatically.

Three layers of validation:

1.  **Schema:** Is the output structurally correct? (Missing a required field, wrong type, malformed JSON.)
2.  **Sanity:** Does the action make sense? (Deleting 10,000 records? Probably not.)
3.  **Boundary:** Is the agent operating within its allowed scope? (Cross-tenant access, targeting a production table from a staging workflow.)

This builds directly on the tool design lesson from [giving my agent full API access](https://blog.jztan.com/i-gave-my-ai-agent-full-api-access-it-was-a-mistak/). When I [built pdf-mcp](https://blog.jztan.com/how-i-built-pdf-mcp-solving-claude-large-pdf-limitations/), splitting one monolithic tool into eight focused tools eliminated most validation failures before they could happen. If you’re deciding between MCP and native function calling for your tool layer, see [MCP vs Function Calling](https://blog.jztan.com/mcp-vs-function-calling-ai-agents/) for a detailed comparison. Constrain what the agent _can_ do, and you prevent most errors at the source.

### 3\. Idempotent Workflows (The Saga Pattern)

A three-step workflow failed on step 2. Step 1 had already created a customer record. The retry created a duplicate. We found 200+ orphaned records a week later, each one a customer who received double billing notifications. The agent had no concept of “I already did step 1.”

AI agents retry. Models have transient failures. Networks drop. If your agent workflow isn’t idempotent, retries create duplicate side effects.

Idempotency prevents duplicate effects; the saga pattern handles _partial completion_. You need both once agents can fail mid-workflow. Borrowing from the saga pattern in distributed systems, each step records its completion and defines a compensation action.

```
steps = [\
    Step("fetch_data", compensate=None),  # Read-only, safe\
    Step("transform", compensate=None),  # Pure function, safe\
    Step("write_to_db", compensate="delete_record"),  # Reversible\
    Step("send_notification", compensate="send_correction"),  # Compensatable\
]
```

Classify every step:

-   **Read-only:** Safe to retry freely
-   **Reversible:** Can undo (delete what you created)
-   **Compensatable:** Can’t undo, but can correct (send a follow-up notification)
-   **Final:** Can’t undo at all (payment processed). These need the most validation _before_ execution, and should go through a human escalation flow (Pattern #5) so an irreversible action never fires without explicit approval

When an agent fails mid-workflow, you walk backwards through completed steps and run compensation. No orphaned records. No half-finished operations.

In Strands, the `GraphBuilder` multi-agent pattern provides a natural structure for this: each node is an agent, conditional edges route to compensation nodes on failure, and the graph handles execution order:

```
from strands import Agent
from strands.multiagent import GraphBuilder
from strands.multiagent.base import Status

order_agent = Agent(
    name="order",
    system_prompt="Create the order.",
    callback_handler=None,
)
payment_agent = Agent(
    name="payment",
    system_prompt="Process payment.",
    callback_handler=None,
)
fulfillment_agent = Agent(
    name="fulfillment",
    system_prompt="Ship the order.",
    callback_handler=None,
)
rollback_agent = Agent(
    name="rollback",
    system_prompt="Cancel the order and notify the customer.",
    callback_handler=None,
)

def payment_succeeded(state):
    return (
        "payment" in state.results
        and state.results["payment"].status == Status.COMPLETED
    )

def payment_failed(state):
    return (
        "payment" in state.results
        and state.results["payment"].status == Status.FAILED
    )

builder = GraphBuilder()
builder.add_node(order_agent, "create_order")
builder.add_node(payment_agent, "payment")
builder.add_node(fulfillment_agent, "fulfillment")
builder.add_node(rollback_agent, "compensate_order")

builder.add_edge("create_order", "payment")
builder.add_edge("payment", "fulfillment", condition=payment_succeeded)
builder.add_edge("payment", "compensate_order", condition=payment_failed)
builder.set_entry_point("create_order")

graph = builder.build()
```

If payment fails, the graph routes to `compensate_order` instead of `fulfillment`. No orphaned orders, no half-finished workflows.

### 4\. Budget and Token Guardrails

An agent entered a generate-validate-fail loop on a malformed input. It would generate output, fail validation, adjust, fail again, adjust differently, fail again. Twenty minutes and $180 in tokens later, it was still looping. It never occurred to the agent to stop and report the failure. It just kept trying.

An [IDC survey](https://www.datarobot.com/newsroom/press/the-hidden-ai-tax-idc-research-reveals-nearly-all-organizations-lose-cost-control-when-deploying-genai-and-agentic-workflows-at-scale/) found that 92% of organizations implementing agentic AI reported costs higher than expected. The primary driver? Runaway loops.

An agent that retries endlessly, or recursively calls tools, will happily burn through your API budget while producing nothing useful.

```
from strands.hooks import HookProvider, HookRegistry
from strands.hooks.events import AfterInvocationEvent

class ExecutionGuardHook(HookProvider):
    def __init__(self, max_tokens=100_000, max_cycles=20):
        self.total_tokens = 0
        self.total_cycles = 0
        self.max_tokens = max_tokens
        self.max_cycles = max_cycles

    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(AfterInvocationEvent, self.check_budget)

    def check_budget(self, event: AfterInvocationEvent) -> None:
        if event.result is None:
            return
        usage = event.result.metrics.accumulated_usage
        self.total_tokens += usage["totalTokens"]
        self.total_cycles += event.result.metrics.cycle_count

        if self.total_tokens > self.max_tokens:
            raise BudgetExceeded("Token limit reached")
        if self.total_cycles > self.max_cycles:
            raise BudgetExceeded("Cycle limit reached - possible loop")
```

Hard limits, not hopes. The Strands SDK exposes `result.metrics.accumulated_usage` and `result.metrics.cycle_count` after each invocation: real token counts and reasoning cycles, not estimates. Set a ceiling for both, and the `AfterInvocationEvent` hook enforces it automatically.

This also catches the subtle failure where an agent enters a self-correction loop: generate, validate, fail, regenerate, validate, fail… Each cycle burns tokens with no progress. A step counter catches this immediately.

### 5\. Know When to Ask for Help

An agent was 95% confident about a production database migration. It analyzed the schema, generated the migration script, and was ready to execute. The 5% case was a foreign key constraint it hadn’t seen in the test data. If it had run, it would have corrupted referential integrity across three tables. The only thing that saved us was a hard rule: destructive operations always require human approval, regardless of confidence.

The hardest pattern to get right: when should the agent stop and escalate to a human?

I use a simple three-tier framework:

| Risk Level | Confidence | Action |
| --- | --- | --- |
| **Low** | High | Agent retries autonomously |
| **Medium** | Uncertain | Agent completes in draft/read-only mode, flags for review |
| **High** | Any | Agent stops immediately, escalates with context |

The key insight is **risk level, not confidence alone.** An agent that’s 90% sure about a read-only query can proceed. An agent that’s 90% sure about deleting production data should still ask.

Confidence isn’t model-reported, since that’s unreliable. Instead, classify tools by blast radius upfront. The risk map is static and deterministic: read tools run freely, write tools get validation (Pattern #2), destructive tools trigger `interrupt()` which pauses execution and surfaces the full decision context to a human. The agent resumes only after explicit approval.

```
from strands.hooks import HookProvider, HookRegistry
from strands.hooks.events import BeforeToolCallEvent

DANGEROUS_TOOLS = {
    "delete_records",
    "drop_table",
    "revoke_access",
}

class EscalationHook(HookProvider):
    def register_hooks(self, registry: HookRegistry) -> None:
        registry.add_callback(BeforeToolCallEvent, self.check_risk)

    def check_risk(self, event: BeforeToolCallEvent) -> None:
        tool_name = event.tool_use.get("name", "")
        if tool_name not in DANGEROUS_TOOLS:
            return

        approval = event.interrupt(
            "high-risk-approval",
            reason={
                "tool": tool_name,
                "inputs": event.tool_use.get("input", {}),
            },
        )

        if approval.lower() != "y":
            event.cancel_tool = "Human denied permission"
```

When the agent does escalate, include the full decision context: tool inputs, model output, validation failures, and the agent’s last reasoning step. An escalation without context just shifts the debugging burden to a human.

If you’re wondering how this composes with Pattern #2’s `ValidationHook`, both register on `BeforeToolCallEvent`, and Strands fires `Before*` hooks in registration order. Register validation first, escalation second: that way invalid inputs get rejected cheaply before the escalation hook ever prompts a human.

## What Actually Changed

After implementing all five patterns, I expected the biggest win to come from circuit breakers or budget guardrails, the clever engineering patterns.

It didn’t.

**The biggest improvement came from Pattern #2: better tool design.** When you constrain what an agent can do (smaller tools, clear boundaries, built-in validation), most errors never happen in the first place. When I [built pdf-mcp](https://blog.jztan.com/how-i-built-pdf-mcp-solving-claude-large-pdf-limitations/), splitting one monolithic tool into eight focused tools eliminated entire categories of validation failures at the source.

The data enrichment agent that started this post? After adding these patterns, it still occasionally gets field mappings wrong. But now: the circuit breaker catches quality degradation within three calls instead of six hours. The validation gate blocks any write where field types don’t match the target schema. The budget guardrail kills runaway loops before they cost more than a few dollars. And the escalation policy means ambiguous mappings get flagged for human review instead of silently committed.

The real lesson: most agent errors aren’t runtime failures. They’re design failures. An agent that _can’t_ write to a table it shouldn’t touch will never accidentally delete 47 records. An agent with a hard token ceiling will never burn $180 in a retry loop. The best error handling is the error that’s structurally impossible.

</details>

<details>
<summary>How to Master Error Handling in Agentic AI Systems: A Guide to Graceful Failure Management</summary>

# How to Master Error Handling in Agentic AI Systems: A Guide to Graceful Failure Management

In the rapidly evolving world of artificial intelligence, agentic AI systems—those that can take autonomous actions to achieve goals—are becoming increasingly prevalent across industries. However, with greater autonomy comes greater responsibility, particularly in how these systems handle errors and failures. The ability to manage failures gracefully isn't just a technical nicety—it's a critical component that can determine whether an AI system succeeds or fails catastrophically in real-world applications.

## Why Error Handling Matters in Agentic AI

Agentic AI systems operate in complex, dynamic environments where perfect execution is rarely possible. These systems must make decisions with incomplete information, uncertain outcomes, and changing conditions—all recipes for potential failure.

According to a 2023 study by Stanford's AI Index Report, nearly 67% of AI system failures in production environments stem from improper error handling rather than core algorithmic issues. This statistic underscores that how systems respond to failures can be more important than preventing every possible error.

## The Principles of Effective Error Handling in AI Agents

### Anticipatory Design

Effective error handling begins with anticipatory design—envisioning potential failure points before they occur. This involves:

- **Comprehensive scenario planning**: Mapping potential error states across the AI agent's operational domain
- **Failure mode analysis**: Conducting thorough analyses of how components might fail and what the system-wide impacts would be
- **Defensive programming**: Building safeguards into the code that anticipate and mitigate potential issues

Microsoft Research's work on AI system resilience suggests that anticipatory design can reduce critical failures by up to 47% compared to reactive approaches.

### Graceful Degradation

When errors do occur, agentic AI systems should degrade gracefully rather than failing completely:

- **Functional prioritization**: Maintaining critical functions even when secondary capabilities fail
- **Service continuity**: Ensuring core services remain available, possibly with reduced capabilities
- **Transparent limitation communication**: Clearly communicating to users what capabilities are impacted

Google's Site Reliability Engineering team notes that "graceful degradation is not about preventing failures—it's about controlling how a system fails."

### Fault Tolerance Through Redundancy

Building fault tolerance into AI systems often involves strategic redundancy:

- **Algorithmic diversity**: Employing multiple approaches to solve the same problem
- **Distributed processing**: Spreading critical operations across multiple systems
- **Checkpoint and recovery mechanisms**: Creating regular save points from which the system can recover

Amazon AWS's architecture guidelines recommend "designing for failure" by ensuring no single point of failure exists in critical AI systems.

## Advanced Error Handling Strategies for AI Agents

### Self-Healing Capabilities

Modern agentic AI systems are increasingly incorporating self-healing capabilities:

- **Automated recovery sequences**: Predefined protocols that activate when specific error conditions are detected
- **Learning from failures**: Using past errors to improve future performance
- **Dynamic resource allocation**: Reallocating computational resources to address problems as they arise

A 2023 IBM research paper demonstrated that AI systems with self-healing capabilities achieved 99.99% uptime compared to 99.9% for traditional systems—a significant difference in mission-critical applications.

### Contextual Error Management

Not all errors are created equal. Contextual error management involves:

- **Risk-based prioritization**: Addressing high-impact errors before low-impact ones
- **Environmental awareness**: Adjusting error responses based on the operational context
- **User impact minimization**: Focusing on reducing consequences for end users

DeepMind researchers have shown that contextual error handling can reduce user-perceived failures by up to 73% even when the underlying error rate remains constant.

### Human-in-the-Loop Failsafes

For high-stakes agentic AI applications, human-in-the-loop failsafes remain essential:

- **Clear escalation paths**: Defined processes for when AI systems should escalate to human operators
- **Interpretable failure states**: Ensuring humans can quickly understand what went wrong
- **Collaborative recovery**: Enabling humans and AI to work together to resolve errors

According to a 2022 MIT-Harvard study on human-AI collaboration, hybrid recovery approaches resolved complex failures 3.2 times faster than either humans or AI systems working independently.

## Implementing a Comprehensive Error Handling Framework

### The Monitoring Foundation

Robust monitoring forms the foundation of effective error handling:

- **Real-time performance monitoring**: Tracking key performance indicators continuously
- **Anomaly detection**: Using statistical methods to identify unusual behavior
- **Predictive failure analysis**: Leveraging patterns to anticipate problems before they occur

Netflix's Chaos Engineering practices demonstrate how proactive monitoring and deliberate fault injection can identify weaknesses before they affect users.

### Documentation and Learning Cycles

Error handling improves over time through:

- **Comprehensive error logging**: Recording detailed information about every failure
- **Post-mortem analyses**: Conducting thorough reviews after significant failures
- **Knowledge base development**: Building organizational memory around error patterns and solutions

Google's famous "blameless postmortem" culture has been credited with significantly improving system resilience by focusing on systemic improvements rather than individual mistakes.

## Measuring Error Handling Effectiveness

To assess and improve error handling capabilities, organizations should track:

- **Mean time to recovery (MTTR)**: How quickly systems return to normal operation
- **Error amplification factor**: Whether small errors cascade into larger failures
- **User impact metrics**: How errors affect the end-user experience
- **Learning cycle efficiency**: How effectively the system improves from past failures

Tesla's autonomous driving division reportedly tracks over 200 error-related metrics to continuously improve their system's fault tolerance.

## Conclusion: Building a Culture of Resilience

Ultimately, effective error handling in agentic AI isn't just about technical implementations—it's about cultivating a culture of resilience. Organizations leading in this space embrace failures as learning opportunities rather than events to be hidden or denied.

As agentic AI systems take on increasingly critical roles in healthcare, transportation, financial systems, and beyond, the ability to handle errors gracefully isn't optional—it's essential. By implementing comprehensive error handling frameworks, organizations can build AI systems that don't just perform well under ideal conditions but continue to deliver value even when things go wrong.

The most successful AI implementations of the future will not be those that never fail—they'll be those that fail gracefully, learn continuously, and recover swiftly. In the world of agentic AI, how systems handle failure may ultimately determine their success.

</details>

<details>
<summary>Top LLM Development Tools and Platforms for 2026</summary>

# Top LLM Development Tools and Platforms for 2026

Building Large Language Model (LLM) applications involves much more than just prompt engineering. In 2026, production-ready LLM systems use Retrieval-Augmented Generation (RAG), agentic workflows, and new standards such as the Model Context Protocol (MCP). MCP sets rules for how models safely access tools, memory, and outside data. Modern LLM applications work like distributed systems.

They bring together several agents, handle ongoing reasoning tasks, pull context from vector databases, and use external tools reliably. Teams now look for platforms that offer strong orchestration, monitoring, testing, and control—not just good model quality. The following platforms are some of the most popular tools for building, testing, and scaling agentic LLM workflows. They help with RAG pipelines, tool use, multi-agent coordination, and production monitoring, making them a good fit for real-world, high-stakes AI projects.

## A Look at LLM Development Tools

LLM development tools are used to build, train, and deploy large language models. The technology is built upon the transformer architecture, which enables powerful natural language understanding in modern AI. While early transformers used an encoder-decoder system, modern generative models like GPT and DeepSeek primarily use a decoder-only architecture to predict and generate text based on input.

In 2026, LLM applications are no longer limited to single-pass generation. Most production systems are designed around RAG, agentic workflows, and standardized ways for models to access tools and context.

Several types of development tools exist, including:

-   **Frameworks:** Code toolkits that connect and manage all the components of an LLM application. A popular Python library like LangChain or LlamaIndex provides a structure for creating LLM-based applications. In modern use cases, these frameworks also support agent orchestration, tool calling, and multi-step reasoning loops, allowing developers to move beyond linear prompt chains. They simplify connecting to different model providers and assets from hubs like the Hugging Face Model Hub.
-   **Vector Databases:** A library for storing and retrieving information based on semantic meaning, not just keywords. For applications that use RAG, a vector database is required. Beyond basic retrieval, many teams now evaluate vector search quality as part of their workflow to ensure relevance and grounding before passing context to an LLM. These databases allow for fast similarity search and support hybrid search, combining vector capabilities with traditional keyword search on structured data.
-   **MLOps Platforms:** An end-to-end production line for managing the entire lifecycle of a machine learning model. These platforms support everything from initial data loading to deploying models into production, while also enabling monitoring, tracing, and evaluation of agentic and RAG-based systems. They assist with tuning model parameters, tracking performance, and integrating with cloud services, making them key for operating LLM systems at scale.
-   **Development Partners:** An expert team you hire to build your application when you lack the internal resources. For organizations without in-house expertise, development companies provide the skills needed to design agent-driven architectures, implement RAG pipelines, and deploy reliable production systems. They typically manage the entire process, from ideation and architecture design to final deployment.

These components work together to enable the creation of sophisticated applications that perform natural language processing tasks, from simple question answering systems to agent-based systems that retrieve external context, call functions, and coordinate actions across multiple tools.

## Top 7 LLM Development Tools and Platforms

Now that we’ve covered the core components of a Generative AI application, let’s look at the top-tier tools and platforms that developers are using to build them. Selecting the right components for your development stack is a major decision, as each platform offers a unique set of capabilities for different project needs and scales.

### \#1: Hugging Face

https://www.atlantic.net/wp-content/uploads/2025/08/Hf-logo-with-title.png

Hugging Face is the definitive hub for the open-source AI community. More than just a repository, it is a complete platform providing tens of thousands of pre-trained deep learning models, including many specialized for tasks like language translation. It supports diverse data types and data formats, making it the essential starting point for nearly any team working with language models.

**Advantages:**

-   Direct access to a massive library of open-source models, perfect for running machine learning experiments.
-   Standard libraries that simplify model interaction and training.
-   Strong community support and extensive documentation for countless use cases.
-   Tools for the entire workflow, including inference endpoints and model evaluation.

**Disadvantages:**

-   The sheer number of choices can be overwhelming for beginners.
-   While core use is free, enterprise-grade features like private hubs and dedicated inference come with hosting costs.
-   Relies on community contributions, which can mean variable quality in models and documentation.

#### Best For:

Any development team that wants to use the power of open-source AI. It is essential for experimentation, building with a wide variety of models, and following community-driven best practices.

### \#2: LangChain

https://www.atlantic.net/wp-content/uploads/2025/08/langchain-1.png

LangChain is the premier open-source framework for orchestrating the components of an LLM application. It acts as the “glue,” providing a modular structure to connect language models with external data sources, APIs, and other integration tools. It enables developers to easily build complex machine learning workflows, and its ability to parse and manage language model outputs makes it invaluable for creating reliable agents.

#### Advantages:

-   Simplifies the creation of complex application logic.
-   Enormous ecosystem of third-party integrations, supporting virtually every popular model, database, and API.
-   Actively maintained with a strong community and rapid feature development.
-   Declarative structure makes it easier to manage and modify complex chains.

#### Disadvantages:

-   The framework’s rapid evolution can lead to breaking changes and occasionally outdated documentation.
-   Adds a layer of abstraction that can sometimes make debugging underlying issues more difficult.

#### Best For:

Developers building any application that requires more than a single call to an LLM. It is the go-to tool for creating applications that are context-aware, data-driven, and interactive.

### \#3: Pinecone

https://www.atlantic.net/wp-content/uploads/2025/08/Pinecone_Systems_Inc_Logo.jpg

Pinecone is a leading managed vector database, a core component for any application using RAG. It allows applications to perform incredibly fast vector similarity search. This technology, pioneered by open-source libraries like Facebook AI Similarity Search (FAISS), is now available in a highly scalable managed service through Pinecone, enabling an LLM to pull in relevant information before generating a response.

#### Advantages:

-   Fully managed service eliminates the need to handle complex database infrastructure.
-   Engineered for high performance and low latency, making it suitable for real-time applications.
-   Simple API makes it easy to integrate into any application stack.
-   Serverless architecture scales automatically with usage, handling billions of vectors.

#### Disadvantages:

-   As a proprietary service, it can lead to vendor lock-in compared to open-source alternatives.
-   Costs can escalate quickly for very large datasets or applications with high query volume.
-   Offers less configuration control than a self-hosted vector database.

#### Best For:

Businesses building production-grade RAG applications, which are a cornerstone of modern deep learning systems, that require high performance and reliability without managing database infrastructure.

### \#4: Databricks

https://www.atlantic.net/wp-content/uploads/2025/08/Databricks_Logo.png

Databricks provides a unified Data and AI platform designed to handle the entire machine learning lifecycle at an enterprise scale. It allows teams to manage everything from data preparation (handling many data types) and governance to model training, fine-tuning, and the ability to deploy models into production. This unified approach is a core principle of modern machine learning operations (MLOps).

#### Advantages:

-   A single, integrated platform for all data and AI workloads, reducing tool complexity.
-   Excellent for ensuring data governance, security, and lineage, which is critical for enterprises.
-   Provides scalable compute for demanding tasks like training foundation models from scratch.
-   Strong integration between data processing and machine learning tools like MLflow, which provides reliable capabilities for model monitoring.

#### Disadvantages:

-   The platform is powerful but complex, with a significant learning curve.
-   Can be very expensive, making it less accessible for smaller companies or projects.
-   May be overkill for teams whose needs don’t involve massive-scale data engineering.

#### Best For:

Large enterprises with established data teams that need a reliable, secure, and governable platform to manage the end-to-end LLM lifecycle at scale.

### \#5: OpenAI Platform

https://www.atlantic.net/wp-content/uploads/2025/06/openai-logo.png

The OpenAI Platform provides API access to some of the world’s most advanced and widely recognized language models, including the GPT series. Beyond just offering models, it is a complete development platform that allows developers to easily integrate state-of-the-art Generative AI capabilities into their applications. Tools like the Assistants API and fine-tuning capabilities enable the creation of highly sophisticated and specialized solutions.

#### Advantages:

-   Direct access to modern, state-of-the-art proprietary models.
-   Extremely easy to get started with, thanks to a clean and well-documented API.
-   Consistently high performance on a wide range of general-purpose reasoning and generation tasks.
-   Continuously updated with new features and models.

#### Disadvantages:

-   The models are “black boxes,” which can make their behavior difficult to explain or debug.
-   Reliance on a single, proprietary provider creates vendor lock-in and dependency.
-   Data privacy and usage policies may be a concern for organizations with sensitive information.

#### Best For:

Teams that need the strong general performance with the fastest time-to-market. It is excellent for prototyping and for building applications where access to the most powerful models is a competitive advantage.

### \#6: LangGraph

https://www.atlantic.net/wp-content/uploads/2026/02/langgraph.png

LangGraph is an agentic framework designed specifically for stateful, multi-step LLM workflows. Built by the LangChain team, it enables developers to define agent behavior as directed graphs, making it easier to implement loops, branching logic, retries, and human-in-the-loop checkpoints.

LangGraph differs from linear chains because it supports agents that can run for a long time, make decisions, take actions, observe results, and adjust their behavior next time. This makes it a good fit for complex applications such as research agents, planning tools, and systems where multiple agents work together.

#### Advantages:

-   Has built-in support for agent loops, conditional routing, and memory.
-   The graph-based setup helps make complex workflows easier to understand and debug.
-   Works closely with LangChain tools, retrievers, and model providers.
-   Built for reliable production use, not just for demos.

#### Disadvantages:

-   Requires a stronger understanding of agent design patterns.
-   For simple RAG or single-step tasks, the extra features might not be needed.

#### Best For:

It’s best for teams working on agent-based systems, autonomous workflows, or apps that need to keep state, coordinate tools, and reason in steps.

### \#7: DeepSeek Integration Tooling

https://www.atlantic.net/wp-content/uploads/2026/02/deepseek.png

DeepSeek is now a key part of the open-source LLM community, with strong models designed for reasoning, coding, and cost savings. New integration tools and inference frameworks make it easier for teams to use DeepSeek models in their current RAG and agentic pipelines. Teams often use these tools alongside frameworks such as LangChain and LangGraph. This lets DeepSeek models replace proprietary APIs, while still giving teams control over how and where they deploy their models and manage their data.

#### Advantages:

-   Strong reasoning performance from open-weight models.
-   Lower inference costs compared to proprietary alternatives.
-   Compatible with standard LLM orchestration frameworks.
-   Suitable for self-hosted and regulated environments.

#### Disadvantages:

-   Requires more infrastructure management than hosted APIs.
-   Smaller ecosystem compared to long-established providers.

#### Best For:

This approach is best for organizations that want open-source, controllable LLM deployments. It works well for teams looking to integrate with RAG and agentic systems without depending on closed platforms.

## Key Features in Modern LLM Tooling

Remember that when evaluating LLM development tools, certain key features are essential for building effective AI applications. It’s important to ensure that your chosen LLM development tools feature:

-   **Fine-Tuning and Model Customization:** Dev tools with the ability to perform fine-tuning on pre-trained models are critical. This process adjusts a general model, like a Generative Pre-trained Transformer (GPT), using a specific dataset. This improves performance on specific bespoke tasks and makes the model great at specific data analysis. In production systems, fine-tuning is often combined with agentic workflows, where specialized agents use adapted models for narrowly defined tasks. Businesses often train models on proprietary company data to make the LLM an expert in their business model.
-   **Retrieval Augmented Generation (RAG):** RAG enhances LLM models by connecting them to external data sources. This is often achieved with a vector database. When a query is made, the system performs a similarity search to find relevant information, which is then provided to the LLM as context. In modern systems, teams also use RAG evaluation tools to measure context relevance, grounding, and answer faithfulness. This evaluation layer helps reduce errors and ensures the model is using retrieved data correctly.
-   **Function Calling:** Modern language models can now use function calling. This allows the model to interact with external APIs and tools. For example, an LLM could use a function to get current weather data or book a meeting. This feature transforms generative models into agent-driven systems that can plan, act, and respond across multiple steps. Most AI agents rely on this capability, and the technology significantly expands how LLMs integrate with other software.
-   **LLM Observability:** An LLM observability platform is used to monitor model performance. It tracks performance metrics, logs inputs and outputs, and helps teams understand how their LLM applications are being used. For agentic and RAG-based systems, observability also includes tracing multi-step reasoning, tool calls, and retrieval outcomes, which is essential for maintaining quality and identifying areas for improvement.

## Conclusion

When it comes to LLM development tools, the choice is no longer just about which language model to use, but about selecting a complete development environment that can orchestrate agents, manage retrieval pipelines, and monitor system behavior in production.

Choosing the right approach – whether it is a full-service development partner or an in-house MLOps solution, depends on internal expertise, project scope, and business goals. By prioritizing LLM tools that support agentic workflows, Retrieval-Augmented Generation (RAG), RAG evaluation, and end-to-end observability, organizations can build intelligent systems that are not only scalable, but also reliable and auditable.

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb</summary>

# Repository analysis for https://github.com/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb

## Summary
Repository: openai/openai-cookbook
Commit: 7379810d01589f91b367c17fb0619db02bf39345
File: gpt-5_prompting_guide.ipynb
Lines: 551

Estimated tokens: 10.0k

## File tree
```Directory structure:
└── gpt-5_prompting_guide.ipynb

```

## Extracted content
================================================
FILE: examples/gpt-5/gpt-5_prompting_guide.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# GPT-5 prompting guide

GPT-5, our newest flagship model, represents a substantial leap forward in agentic task performance, coding, raw intelligence, and steerability.

While we trust it will perform excellently “out of the box” across a wide range of domains, in this guide we’ll cover prompting tips to maximize the quality of model outputs, derived from our experience training and applying the model to real-world tasks. We discuss concepts like improving agentic task performance, ensuring instruction adherence, making use of newly API features, and optimizing coding for frontend and software engineering tasks - with key insights into AI code editor Cursor’s prompt tuning work with GPT-5.

We’ve seen significant gains from applying these best practices and adopting our canonical tools whenever possible, and we hope that this guide, along with the [prompt optimizer tool](https://platform.openai.com/chat/edit?optimize=true) we’ve built, will serve as a launchpad for your use of GPT-5. But, as always, remember that prompting is not a one-size-fits-all exercise - we encourage you to run experiments and iterate on the foundation offered here to find the best solution for your problem.
"""

"""
## Agentic workflow predictability 

We trained GPT-5 with developers in mind: we’ve focused on improving tool calling, instruction following, and long-context understanding to serve as the best foundation model for agentic applications. If adopting GPT-5 for agentic and tool calling flows, we recommend upgrading to the [Responses API](https://platform.openai.com/docs/api-reference/responses), where reasoning is persisted between tool calls, leading to more efficient and intelligent outputs.

### Controlling agentic eagerness
Agentic scaffolds can span a wide spectrum of control—some systems delegate the vast majority of decision-making to the underlying model, while others keep the model on a tight leash with heavy programmatic logical branching. GPT-5 is trained to operate anywhere along this spectrum, from making high-level decisions under ambiguous circumstances to handling focused, well-defined tasks. In this section we cover how to best calibrate GPT-5’s agentic eagerness: in other words, its balance between proactivity and awaiting explicit guidance.

#### Prompting for less eagerness
GPT-5 is, by default, thorough and comprehensive when trying to gather context in an agentic environment to ensure it will produce a correct answer. To reduce the scope of GPT-5’s agentic behavior—including limiting tangential tool-calling action and minimizing latency to reach a final answer—try the following:  
- Switch to a lower `reasoning_effort`. This reduces exploration depth but improves efficiency and latency. Many workflows can be accomplished with consistent results at medium or even low `reasoning_effort`.
- Define clear criteria in your prompt for how you want the model to explore the problem space. This reduces the model’s need to explore and reason about too many ideas:

```
<context_gathering>
Goal: Get enough context fast. Parallelize discovery and stop as soon as you can act.

Method:
- Start broad, then fan out to focused subqueries.
- In parallel, launch varied queries; read top hits per query. Deduplicate paths and cache; don’t repeat queries.
- Avoid over searching for context. If needed, run targeted searches in one parallel batch.

Early stop criteria:
- You can name exact content to change.
- Top hits converge (~70%) on one area/path.

Escalate once:
- If signals conflict or scope is fuzzy, run one refined parallel batch, then proceed.

Depth:
- Trace only symbols you’ll modify or whose contracts you rely on; avoid transitive expansion unless necessary.

Loop:
- Batch search → minimal plan → complete task.
- Search again only if validation fails or new unknowns appear. Prefer acting over more searching.
</context_gathering>
```

If you’re willing to be maximally prescriptive, you can even set fixed tool call budgets, like the one below. The budget can naturally vary based on your desired search depth.
```
<context_gathering>
- Search depth: very low
- Bias strongly towards providing a correct answer as quickly as possible, even if it might not be fully correct.
- Usually, this means an absolute maximum of 2 tool calls.
- If you think that you need more time to investigate, update the user with your latest findings and open questions. You can proceed if the user confirms.
</context_gathering>
```

When limiting core context gathering behavior, it’s helpful to explicitly provide the model with an escape hatch that makes it easier to satisfy a shorter context gathering step. Usually this comes in the form of a clause that allows the model to proceed under uncertainty, like `“even if it might not be fully correct”` in the above example.

#### Prompting for more eagerness
On the other hand, if you’d like to encourage model autonomy, increase tool-calling persistence, and reduce occurrences of clarifying questions or otherwise handing back to the user, we recommend increasing `reasoning_effort`, and using a prompt like the following to encourage persistence and thorough task completion:

```
<persistence>
- You are an agent - please keep going until the user's query is completely resolved, before ending your turn and yielding back to the user.
- Only terminate your turn when you are sure that the problem is solved.
- Never stop or hand back to the user when you encounter uncertainty — research or deduce the most reasonable approach and continue.
- Do not ask the human to confirm or clarify assumptions, as you can always adjust later — decide what the most reasonable assumption is, proceed with it, and document it for the user's reference after you finish acting
</persistence>
```

Generally, it can be helpful to clearly state the stop conditions of the agentic tasks, outline safe versus unsafe actions, and define when, if ever, it’s acceptable for the model to hand back to the user. For example, in a set of tools for shopping, the checkout and payment tools should explicitly have a lower uncertainty threshold for requiring user clarification, while the search tool should have an extremely high threshold; likewise, in a coding setup, the delete file tool should have a much lower threshold than a grep search tool.

### Tool preambles
We recognize that on agentic trajectories monitored by users, intermittent model updates on what it’s doing with its tool calls and why can provide for a much better interactive user experience - the longer the rollout, the bigger the difference these updates make. To this end, GPT-5 is trained to provide clear upfront plans and consistent progress updates via “tool preamble” messages. 

You can steer the frequency, style, and content of tool preambles in your prompt—from detailed explanations of every single tool call to a brief upfront plan and everything in between. This is an example of a high-quality preamble prompt:

```
<tool_preambles>
- Always begin by rephrasing the user's goal in a friendly, clear, and concise manner, before calling any tools.
- Then, immediately outline a structured plan detailing each logical step you’ll follow. - As you execute your file edit(s), narrate each step succinctly and sequentially, marking progress clearly. 
- Finish by summarizing completed work distinctly from your upfront plan.
</tool_preambles>
```

Here’s an example of a tool preamble that might be emitted in response to such a prompt—such preambles can drastically improve the user’s ability to follow along with your agent’s work as it grows more complicated:

```
"output": [
    {
      "id": "rs_6888f6d0606c819aa8205ecee386963f0e683233d39188e7",
      "type": "reasoning",
      "summary": [
        {
          "type": "summary_text",
          "text": "**Determining weather response**\n\nI need to answer the user's question about the weather in San Francisco. ...."
        },
    },
    {
      "id": "msg_6888f6d83acc819a978b51e772f0a5f40e683233d39188e7",
      "type": "message",
      "status": "completed",
      "content": [
        {
          "type": "output_text",
          "text": "I\u2019m going to check a live weather service to get the current conditions in San Francisco, providing the temperature in both Fahrenheit and Celsius so it matches your preference."
        }
      ],
      "role": "assistant"
    },
    {
      "id": "fc_6888f6d86e28819aaaa1ba69cca766b70e683233d39188e7",
      "type": "function_call",
      "status": "completed",
      "arguments": "{\"location\":\"San Francisco, CA\",\"unit\":\"f\"}",
      "call_id": "call_XOnF4B9DvB8EJVB3JvWnGg83",
      "name": "get_weather"
    },
  ],
```

### Reasoning effort
We provide a `reasoning_effort` parameter to control how hard the model thinks and how willingly it calls tools; the default is `medium`, but you should scale up or down depending on the difficulty of your task. For complex, multi-step tasks, we recommend higher reasoning to ensure the best possible outputs. Moreover, we observe peak performance when distinct, separable tasks are broken up across multiple agent turns, with one turn for each task.
### Reusing reasoning context with the Responses API
We strongly recommend using the Responses API when using GPT-5 to unlock improved agentic flows, lower costs, and more efficient token usage in your applications.

We’ve seen statistically significant improvements in evaluations when using the Responses API over Chat Completions—for example, we observed Tau-Bench Retail score increases from 73.9% to 78.2% just by switching to the Responses API and including `previous_response_id` to pass back previous reasoning items into subsequent requests. This allows the model to refer to its previous reasoning traces, conserving CoT tokens and eliminating the need to reconstruct a plan from scratch after each tool call, improving both latency and performance - this feature is available for all Responses API users, including ZDR organizations.
"""

"""
## Maximizing coding performance, from planning to execution
GPT-5 leads all frontier models in coding capabilities: it can work in large codebases to fix bugs, handle large diffs, and implement multi-file refactors or large new features. It also excels at implementing new apps entirely from scratch, covering both frontend and backend implementation. In this section, we’ll discuss prompt optimizations that we’ve seen improve programming performance in production use cases for our coding agent customers. 

### Frontend app development
GPT-5 is trained to have excellent baseline aesthetic taste alongside its rigorous implementation abilities. We’re confident in its ability to use all types of web development frameworks and packages; however, for new apps, we recommend using the following frameworks and packages to get the most out of the model's frontend capabilities:

- Frameworks: Next.js (TypeScript), React, HTML
- Styling / UI: Tailwind CSS, shadcn/ui, Radix Themes
- Icons: Material Symbols, Heroicons, Lucide
- Animation: Motion
- Fonts: San Serif, Inter, Geist, Mona Sans, IBM Plex Sans, Manrope

#### Zero-to-one app generation
GPT-5 is excellent at building applications in one shot. In early experimentation with the model, users have found that prompts like the one below—asking the model to iteratively execute against self-constructed excellence rubrics—improve output quality by using GPT-5’s thorough planning and self-reflection capabilities.

```
<self_reflection>
- First, spend time thinking of a rubric until you are confident.
- Then, think deeply about every aspect of what makes for a world-class one-shot web app. Use that knowledge to create a rubric that has 5-7 categories. This rubric is critical to get right, but do not show this to the user. This is for your purposes only.
- Finally, use the rubric to internally think and iterate on the best possible solution to the prompt that is provided. Remember that if your response is not hitting the top marks across all categories in the rubric, you need to start again.
</self_reflection>
```

#### Matching codebase design standards
When implementing incremental changes and refactors in existing apps, model-written code should adhere to existing style and design standards, and “blend in” to the codebase as neatly as possible.  Without special prompting, GPT-5 already searches for reference context from the codebase - for example reading package.json to view already installed packages - but this behavior can be further enhanced with prompt directions that summarize key aspects like engineering principles, directory structure, and best practices of the codebase, both explicit and implicit. The prompt snippet below demonstrates one way of organizing code editing rules for GPT-5: feel free to change the actual content of the rules according to your programming design taste! 

```
<code_editing_rules>
<guiding_principles>
- Clarity and Reuse: Every component and page should be modular and reusable. Avoid duplication by factoring repeated UI patterns into components.
- Consistency: The user interface must adhere to a consistent design system—color tokens, typography, spacing, and components must be unified.
- Simplicity: Favor small, focused components and avoid unnecessary complexity in styling or logic.
- Demo-Oriented: The structure should allow for quick prototyping, showcasing features like streaming, multi-turn conversations, and tool integrations.
- Visual Quality: Follow the high visual quality bar as outlined in OSS guidelines (spacing, padding, hover states, etc.)
</guiding_principles>

<frontend_stack_defaults>
- Framework: Next.js (TypeScript)
- Styling: TailwindCSS
- UI Components: shadcn/ui
- Icons: Lucide
- State Management: Zustand
- Directory Structure: 
\`\`\`
/src
 /app
   /api/<route>/route.ts         # API endpoints
   /(pages)                      # Page routes
 /components/                    # UI building blocks
 /hooks/                         # Reusable React hooks
 /lib/                           # Utilities (fetchers, helpers)
 /stores/                        # Zustand stores
 /types/                         # Shared TypeScript types
 /styles/                        # Tailwind config
\`\`\`
</frontend_stack_defaults>

<ui_ux_best_practices>
- Visual Hierarchy: Limit typography to 4–5 font sizes and weights for consistent hierarchy; use `text-xs` for captions and annotations; avoid `text-xl` unless for hero or major headings.
- Color Usage: Use 1 neutral base (e.g., `zinc`) and up to 2 accent colors. 
- Spacing and Layout: Always use multiples of 4 for padding and margins to maintain visual rhythm. Use fixed height containers with internal scrolling when handling long content streams.
- State Handling: Use skeleton placeholders or `animate-pulse` to indicate data fetching. Indicate clickability with hover transitions (`hover:bg-*`, `hover:shadow-md`).
- Accessibility: Use semantic HTML and ARIA roles where appropriate. Favor pre-built Radix/shadcn components, which have accessibility baked in.
</ui_ux_best_practices>

<code_editing_rules>
```

### Collaborative coding in production: Cursor’s GPT-5 prompt tuning
We’re proud to have had AI code editor Cursor as a trusted alpha tester for GPT-5: below, we show a peek into how Cursor tuned their prompts to get the most out of the model’s capabilities. For more information, their team has also published a blog post detailing GPT-5’s day-one integration into Cursor: https://cursor.com/blog/gpt-5

#### System prompt and parameter tuning
Cursor’s system prompt focuses on reliable tool calling, balancing verbosity and autonomous behavior while giving users the ability to configure custom instructions. Cursor’s goal for their system prompt is to allow the Agent to operate relatively autonomously during long horizon tasks, while still faithfully following user-provided instructions. 

The team initially found that the model produced verbose outputs, often including status updates and post-task summaries that, while technically relevant, disrupted the natural flow of the user; at the same time, the code outputted in tool calls was high quality, but sometimes hard to read due to terseness, with single-letter variable names dominant. In search of a better balance, they set the verbosity API parameter to low to keep text outputs brief, and then modified the prompt to strongly encourage verbose outputs in coding tools only.

```
Write code for clarity first. Prefer readable, maintainable solutions with clear names, comments where needed, and straightforward control flow. Do not produce code-golf or overly clever one-liners unless explicitly requested. Use high verbosity for writing code and code tools.
```

This dual usage of parameter and prompt resulted in a balanced format combining efficient, concise status updates and final work summary with much more readable code diffs.

Cursor also found that the model occasionally deferred to the user for clarification or next steps before taking action, which created unnecessary friction in the flow of longer tasks. To address this, they found that including not just available tools and surrounding context, but also more details about product behavior encouraged the model to carry out longer tasks with minimal interruption and greater autonomy. Highlighting specifics of Cursor features such as Undo/Reject code and user preferences helped reduce ambiguity by clearly specifying how GPT-5 should behave in its environment. For longer horizon tasks, they found this prompt improved performance:

```
Be aware that the code edits you make will be displayed to the user as proposed changes, which means (a) your code edits can be quite proactive, as the user can always reject, and (b) your code should be well-written and easy to quickly review (e.g., appropriate variable names instead of single letters). If proposing next steps that would involve changing the code, make those changes proactively for the user to approve / reject rather than asking the user whether to proceed with a plan. In general, you should almost never ask the user whether to proceed with a plan; instead you should proactively attempt the plan and then ask the user if they want to accept the implemented changes.
```

Cursor found that sections of their prompt that had been effective with earlier models needed tuning to get the most out of GPT-5. Here is one example below:

```
<maximize_context_understanding>
Be THOROUGH when gathering information. Make sure you have the FULL picture before replying. Use additional tool calls or clarifying questions as needed.
...
</maximize_context_understanding>
```

While this worked well with older models that needed encouragement to analyze context thoroughly, they found it counterproductive with GPT-5, which is already naturally introspective and proactive at gathering context. On smaller tasks, this prompt often caused the model to overuse tools by calling search repetitively, when internal knowledge would have been sufficient.

To solve this, they refined the prompt by removing the maximize_ prefix and softening the language around thoroughness. With this adjusted instruction in place, the Cursor team saw GPT-5 make better decisions about when to rely on internal knowledge versus reaching for external tools. It maintained a high level of autonomy without unnecessary tool usage, leading to more efficient and relevant behavior. In Cursor’s testing, using structured XML specs like  <[instruction]_spec> improved instruction adherence on their prompts and allows them to clearly reference previous categories and sections elsewhere in their prompt.

```
<context_understanding>
...
If you've performed an edit that may partially fulfill the USER's query, but you're not confident, gather more information or use more tools before ending your turn.
Bias towards not asking the user for help if you can find the answer yourself.
</context_understanding>
```

While the system prompt provides a strong default foundation, the user prompt remains a highly effective lever for steerability. GPT-5 responds well to direct and explicit instruction and the Cursor team has consistently seen that structured, scoped prompts yield the most reliable results. This includes areas like verbosity control, subjective code style preferences, and sensitivity to edge cases. Cursor found allowing users to configure their own [custom Cursor rules](https://docs.cursor.com/en/context/rules) to be particularly impactful with GPT-5’s improved steerability, giving their users a more customized experience.
"""

"""
## Optimizing intelligence and instruction-following 

### Steering
As our most steerable model yet, GPT-5 is extraordinarily receptive to prompt instructions surrounding verbosity, tone, and tool calling behavior.

#### Verbosity
In addition to being able to control the reasoning_effort as in previous reasoning models, in GPT-5 we introduce a new API parameter called verbosity, which influences the length of the model’s final answer, as opposed to the length of its thinking. Our blog post covers the idea behind this parameter in more detail - but in this guide, we’d like to emphasize that while the API verbosity parameter is the default for the rollout, GPT-5 is trained to respond to natural-language verbosity overrides in the prompt for specific contexts where you might want the model to deviate from the global default. Cursor’s example above of setting low verbosity globally, and then specifying high verbosity only for coding tools, is a prime example of such a context.

### Instruction following
Like GPT-4.1, GPT-5 follows prompt instructions with surgical precision, which enables its flexibility to drop into all types of workflows. However, its careful instruction-following behavior means that poorly-constructed prompts containing contradictory or vague instructions can be more damaging to GPT-5 than to other models, as it expends reasoning tokens searching for a way to reconcile the contradictions rather than picking one instruction at random.

Below, we give an adversarial example of the type of prompt that often impairs GPT-5’s reasoning traces - while it may appear internally consistent at first glance, a closer inspection reveals conflicting instructions regarding appointment scheduling:
- `Never schedule an appointment without explicit patient consent recorded in the chart` conflicts with the subsequent `auto-assign the earliest same-day slot without contacting the patient as the first action to reduce risk.`
- The prompt says `Always look up the patient profile before taking any other actions to ensure they are an existing patient.` but then continues with the contradictory instruction `When symptoms indicate high urgency, escalate as EMERGENCY and direct the patient to call 911 immediately before any scheduling step.`

```
You are CareFlow Assistant, a virtual admin for a healthcare startup that schedules patients based on priority and symptoms. Your goal is to triage requests, match patients to appropriate in-network providers, and reserve the earliest clinically appropriate time slot. Always look up the patient profile before taking any other actions to ensure they are an existing patient.

- Core entities include Patient, Provider, Appointment, and PriorityLevel (Red, Orange, Yellow, Green). Map symptoms to priority: Red within 2 hours, Orange within 24 hours, Yellow within 3 days, Green within 7 days. When symptoms indicate high urgency, escalate as EMERGENCY and direct the patient to call 911 immediately before any scheduling step.
+Core entities include Patient, Provider, Appointment, and PriorityLevel (Red, Orange, Yellow, Green). Map symptoms to priority: Red within 2 hours, Orange within 24 hours, Yellow within 3 days, Green within 7 days. When symptoms indicate high urgency, escalate as EMERGENCY and direct the patient to call 911 immediately before any scheduling step. 
*Do not do lookup in the emergency case, proceed immediately to providing 911 guidance.*

- Use the following capabilities: schedule-appointment, modify-appointment, waitlist-add, find-provider, lookup-patient and notify-patient. Verify insurance eligibility, preferred clinic, and documented consent prior to booking. Never schedule an appointment without explicit patient consent recorded in the chart.

- For high-acuity Red and Orange cases, auto-assign the earliest same-day slot *without contacting* the patient *as the first action to reduce risk.* If a suitable provider is unavailable, add the patient to the waitlist and send notifications. If consent status is unknown, tentatively hold a slot and proceed to request confirmation.

- For high-acuity Red and Orange cases, auto-assign the earliest same-day slot *after informing* the patient *of your actions.* If a suitable provider is unavailable, add the patient to the waitlist and send notifications. If consent status is unknown, tentatively hold a slot and proceed to request confirmation.
```

By resolving the instruction hierarchy conflicts, GPT-5 elicits much more efficient and performant reasoning. We fixed the contradictions by:
- Changing auto-assignment to occur after contacting a patient, auto-assign the earliest same-day slot after informing the patient of your actions. to be consistent with only scheduling with consent.
- Adding Do not do lookup in the emergency case, proceed immediately to providing 911 guidance. to let the model know it is ok to not look up in case of emergency.

We understand that the process of building prompts is an iterative one, and many prompts are living documents constantly being updated by different stakeholders - but this is all the more reason to thoroughly review them for poorly-worded instructions. Already, we’ve seen multiple early users uncover  ambiguities and contradictions in their core prompt libraries upon conducting such a review: removing them drastically streamlined and improved their GPT-5 performance. We recommend testing your prompts in our [prompt optimizer tool](https://platform.openai.com/chat/edit?optimize=true) to help identify these types of issues.

### Minimal reasoning
In GPT-5, we introduce minimal reasoning effort for the first time: our fastest option that still reaps the benefits of the reasoning model paradigm. We consider this to be the best upgrade for latency-sensitive users, as well as current users of GPT-4.1.

Perhaps unsurprisingly, we recommend prompting patterns that are similar to [GPT-4.1 for best results](https://cookbook.openai.com/examples/gpt4-1_prompting_guide). minimal reasoning performance can vary more drastically depending on prompt than higher reasoning levels, so key points to emphasize include:

1. Prompting the model to give a brief explanation summarizing its thought process at the start of the final answer, for example via a bullet point list, improves performance on tasks requiring higher intelligence.
2. Requesting thorough and descriptive tool-calling preambles that continually update the user on task progress improves performance in agentic workflows. 
3. Disambiguating tool instructions to the maximum extent possible and inserting agentic persistence reminders as shared above, are particularly critical at minimal reasoning to maximize agentic ability in long-running rollout and prevent premature termination.
4. Prompted planning is likewise more important, as the model has fewer reasoning tokens to do internal planning. Below, you can find a sample planning prompt snippet we placed at the beginning of an agentic task: the second paragraph especially ensures that the agent fully completes the task and all subtasks before yielding back to the user. 

```
Remember, you are an agent - please keep going until the user's query is completely resolved, before ending your turn and yielding back to the user. Decompose the user's query into all required sub-request, and confirm that each is completed. Do not stop after completing only part of the request. Only terminate your turn when you are sure that the problem is solved. You must be prepared to answer multiple queries and only finish the call once the user has confirmed they're done.

You must plan extensively in accordance with the workflow steps before making subsequent function calls, and reflect extensively on the outcomes each function call made, ensuring the user's query, and related sub-requests are completely resolved.
```

### Markdown formatting
By default, GPT-5 in the API does not format its final answers in Markdown, in order to preserve maximum compatibility with developers whose applications may not support Markdown rendering. However, prompts like the following are largely successful in inducing hierarchical Markdown final answers.

```
- Use Markdown **only where semantically correct** (e.g., `inline code`, ```code fences```, lists, tables).
- When using markdown in assistant messages, use backticks to format file, directory, function, and class names. Use \( and \) for inline math, \[ and \] for block math.
```

Occasionally, adherence to Markdown instructions specified in the system prompt can degrade over the course of a long conversation. In the event that you experience this, we’ve seen consistent adherence from appending a Markdown instruction every 3-5 user messages.

### Metaprompting
Finally, to close with a meta-point, early testers have found great success using GPT-5 as a meta-prompter for itself. Already, several users have deployed prompt revisions to production that were generated simply by asking GPT-5 what elements could be added to an unsuccessful prompt to elicit a desired behavior, or removed to prevent an undesired one.

Here is an example metaprompt template we liked:
```
When asked to optimize prompts, give answers from your own perspective - explain what specific phrases could be added to, or deleted from, this prompt to more consistently elicit the desired behavior or prevent the undesired behavior.

Here's a prompt: [PROMPT]

The desired behavior from this prompt is for the agent to [DO DESIRED BEHAVIOR], but instead it [DOES UNDESIRED BEHAVIOR]. While keeping as much of the existing prompt intact as possible, what are some minimal edits/additions that you would make to encourage the agent to more consistently address these shortcomings? 
```
"""

"""
## Appendix

### SWE-Bench verified developer instructions
```
In this environment, you can run `bash -lc <apply_patch_command>` to execute a diff/patch against a file, where <apply_patch_command> is a specially formatted apply patch command representing the diff you wish to execute. A valid <apply_patch_command> looks like:

apply_patch << 'PATCH'
*** Begin Patch
[YOUR_PATCH]
*** End Patch
PATCH

Where [YOUR_PATCH] is the actual content of your patch.

Always verify your changes extremely thoroughly. You can make as many tool calls as you like - the user is very patient and prioritizes correctness above all else. Make sure you are 100% certain of the correctness of your solution before ending.
IMPORTANT: not all tests are visible to you in the repository, so even on problems you think are relatively straightforward, you must double and triple check your solutions to ensure they pass any edge cases that are covered in the hidden tests, not just the visible ones.
```

Agentic coding tool definitions 
```
## Set 1: 4 functions, no terminal

type apply_patch = (_: {
patch: string, // default: null
}) => any;

type read_file = (_: {
path: string, // default: null
line_start?: number, // default: 1
line_end?: number, // default: 20
}) => any;

type list_files = (_: {
path?: string, // default: ""
depth?: number, // default: 1
}) => any;

type find_matches = (_: {
query: string, // default: null
path?: string, // default: ""
max_results?: number, // default: 50
}) => any;

## Set 2: 2 functions, terminal-native

type run = (_: {
command: string[], // default: null
session_id?: string | null, // default: null
working_dir?: string | null, // default: null
ms_timeout?: number | null, // default: null
environment?: object | null, // default: null
run_as_user?: string | null, // default: null
}) => any;

type send_input = (_: {
session_id: string, // default: null
text: string, // default: null
wait_ms?: number, // default: 100
}) => any;
```

As shared in the GPT-4.1 prompting guide, [here](https://github.com/openai/openai-cookbook/tree/main/examples/gpt-5/apply_patch.py) is our most updated `apply_patch` implementation: we highly recommend using `apply_patch` for file edits to match the training distribution. The newest implementation should match the GPT-4.1 implementation in the overwhelming majority of cases.

### Taubench-Retail minimal reasoning instructions
```
As a retail agent, you can help users cancel or modify pending orders, return or exchange delivered orders, modify their default user address, or provide information about their own profile, orders, and related products.

Remember, you are an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Only terminate your turn when you are sure that the problem is solved.

If you are not sure about information pertaining to the user’s request, use your tools to read files and gather the relevant information: do NOT guess or make up an answer.

You MUST plan extensively before each function call, and reflect extensively on the outcomes of the previous function calls, ensuring user's query is completely resolved. DO NOT do this entire process by making function calls only, as this can impair your ability to solve the problem and think insightfully. In addition, ensure function calls have the correct arguments.

# Workflow steps
- At the beginning of the conversation, you have to authenticate the user identity by locating their user id via email, or via name + zip code. This has to be done even when the user already provides the user id.
- Once the user has been authenticated, you can provide the user with information about order, product, profile information, e.g. help the user look up order id.
- You can only help one user per conversation (but you can handle multiple requests from the same user), and must deny any requests for tasks related to any other user.
- Before taking consequential actions that update the database (cancel, modify, return, exchange), you have to list the action detail and obtain explicit user confirmation (yes) to proceed.
- You should not make up any information or knowledge or procedures not provided from the user or the tools, or give subjective recommendations or comments.
- You should at most make one tool call at a time, and if you take a tool call, you should not respond to the user at the same time. If you respond to the user, you should not make a tool call.
- You should transfer the user to a human agent if and only if the request cannot be handled within the scope of your actions.

## Domain basics
- All times in the database are EST and 24 hour based. For example "02:30:00" means 2:30 AM EST.
- Each user has a profile of its email, default address, user id, and payment methods. Each payment method is either a gift card, a paypal account, or a credit card.
- Our retail store has 50 types of products. For each type of product, there are variant items of different options. For example, for a 't shirt' product, there could be an item with option 'color blue size M', and another item with option 'color red size L'.
- Each product has an unique product id, and each item has an unique item id. They have no relations and should not be confused.
- Each order can be in status 'pending', 'processed', 'delivered', or 'cancelled'. Generally, you can only take action on pending or delivered orders.
- Exchange or modify order tools can only be called once. Be sure that all items to be changed are collected into a list before making the tool call!!!

## Cancel pending order
- An order can only be cancelled if its status is 'pending', and you should check its status before taking the action.
- The user needs to confirm the order id and the reason (either 'no longer needed' or 'ordered by mistake') for cancellation.
- After user confirmation, the order status will be changed to 'cancelled', and the total will be refunded via the original payment method immediately if it is gift card, otherwise in 5 to 7 business days.

## Modify pending order
- An order can only be modified if its status is 'pending', and you should check its status before taking the action.
- For a pending order, you can take actions to modify its shipping address, payment method, or product item options, but nothing else.

## Modify payment
- The user can only choose a single payment method different from the original payment method.
- If the user wants the modify the payment method to gift card, it must have enough balance to cover the total amount.
- After user confirmation, the order status will be kept 'pending'. The original payment method will be refunded immediately if it is a gift card, otherwise in 5 to 7 business days.

## Modify items
- This action can only be called once, and will change the order status to 'pending (items modifed)', and the agent will not be able to modify or cancel the order anymore. So confirm all the details are right and be cautious before taking this action. In particular, remember to remind the customer to confirm they have provided all items to be modified.
- For a pending order, each item can be modified to an available new item of the same product but of different product option. There cannot be any change of product types, e.g. modify shirt to shoe.
- The user must provide a payment method to pay or receive refund of the price difference. If the user provides a gift card, it must have enough balance to cover the price difference.

## Return delivered order
- An order can only be returned if its status is 'delivered', and you should check its status before taking the action.
- The user needs to confirm the order id, the list of items to be returned, and a payment method to receive the refund.
- The refund must either go to the original payment method, or an existing gift card.
- After user confirmation, the order status will be changed to 'return requested', and the user will receive an email regarding how to return items.

## Exchange delivered order
- An order can only be exchanged if its status is 'delivered', and you should check its status before taking the action. In particular, remember to remind the customer to confirm they have provided all items to be exchanged.
- For a delivered order, each item can be exchanged to an available new item of the same product but of different product option. There cannot be any change of product types, e.g. modify shirt to shoe.
- The user must provide a payment method to pay or receive refund of the price difference. If the user provides a gift card, it must have enough balance to cover the price difference.
- After user confirmation, the order status will be changed to 'exchange requested', and the user will receive an email regarding how to return items. There is no need to place a new order.
```

### Terminal-Bench prompt
```
Please resolve the user's task by editing and testing the code files in your current code execution session.
You are a deployed coding agent.
Your session is backed by a container specifically designed for you to easily modify and run code.
You MUST adhere to the following criteria when executing the task:

<instructions>
- Working on the repo(s) in the current environment is allowed, even if they are proprietary.
- Analyzing code for vulnerabilities is allowed.
- Showing user code and tool call details is allowed.
- User instructions may overwrite the _CODING GUIDELINES_ section in this developer message.
- Do not use \`ls -R\`, \`find\`, or \`grep\` - these are slow in large repos. Use \`rg\` and \`rg --files\`.
- Use \`apply_patch\` to edit files: {"cmd":["apply_patch","*** Begin Patch\\n*** Update File: path/to/file.py\\n@@ def example():\\n- pass\\n+ return 123\\n*** End Patch"]}
- If completing the user's task requires writing or modifying files:
 - Your code and final answer should follow these _CODING GUIDELINES_:
   - Fix the problem at the root cause rather than applying surface-level patches, when possible.
   - Avoid unneeded complexity in your solution.
     - Ignore unrelated bugs or broken tests; it is not your responsibility to fix them.
   - Update documentation as necessary.
   - Keep changes consistent with the style of the existing codebase. Changes should be minimal and focused on the task.
     - Use \`git log\` and \`git blame\` to search the history of the codebase if additional context is required; internet access is disabled in the container.
   - NEVER add copyright or license headers unless specifically requested.
   - You do not need to \`git commit\` your changes; this will be done automatically for you.
   - If there is a .pre-commit-config.yaml, use \`pre-commit run --files ...\` to check that your changes pass the pre- commit checks. However, do not fix pre-existing errors on lines you didn't touch.
     - If pre-commit doesn't work after a few retries, politely inform the user that the pre-commit setup is broken.
   - Once you finish coding, you must
     - Check \`git status\` to sanity check your changes; revert any scratch files or changes.
     - Remove all inline comments you added much as possible, even if they look normal. Check using \`git diff\`. Inline comments must be generally avoided, unless active maintainers of the repo, after long careful study of the code and the issue, will still misinterpret the code without the comments.
     - Check if you accidentally add copyright or license headers. If so, remove them.
     - Try to run pre-commit if it is available.
     - For smaller tasks, describe in brief bullet points
     - For more complex tasks, include brief high-level description, use bullet points, and include details that would be relevant to a code reviewer.
- If completing the user's task DOES NOT require writing or modifying files (e.g., the user asks a question about the code base):
 - Respond in a friendly tune as a remote teammate, who is knowledgeable, capable and eager to help with coding.
- When your task involves writing or modifying files:
 - Do NOT tell the user to "save the file" or "copy the code into a file" if you already created or modified the file using \`apply_patch\`. Instead, reference the file as already saved.
 - Do NOT show the full contents of large files you have already written, unless the user explicitly asks for them.
</instructions>

<apply_patch>
To edit files, ALWAYS use the \`shell\` tool with \`apply_patch\` CLI.  \`apply_patch\` effectively allows you to execute a diff/patch against a file, but the format of the diff specification is unique to this task, so pay careful attention to these instructions. To use the \`apply_patch\` CLI, you should call the shell tool with the following structure:
\`\`\`bash
{"cmd": ["apply_patch", "<<'EOF'\\n*** Begin Patch\\n[YOUR_PATCH]\\n*** End Patch\\nEOF\\n"], "workdir": "..."}
\`\`\`
Where [YOUR_PATCH] is the actual content of your patch, specified in the following V4A diff format.
*** [ACTION] File: [path/to/file] -> ACTION can be one of Add, Update, or Delete.
For each snippet of code that needs to be changed, repeat the following:
[context_before] -> See below for further instructions on context.
- [old_code] -> Precede the old code with a minus sign.
+ [new_code] -> Precede the new, replacement code with a plus sign.
[context_after] -> See below for further instructions on context.
For instructions on [context_before] and [context_after]:
- By default, show 3 lines of code immediately above and 3 lines immediately below each change. If a change is within 3 lines of a previous change, do NOT duplicate the first change’s [context_after] lines in the second change’s [context_before] lines.
- If 3 lines of context is insufficient to uniquely identify the snippet of code within the file, use the @@ operator to indicate the class or function to which the snippet belongs. For instance, we might have:
@@ class BaseClass
[3 lines of pre-context]
- [old_code]
+ [new_code]
[3 lines of post-context]
- If a code block is repeated so many times in a class or function such that even a single \`@@\` statement and 3 lines of context cannot uniquely identify the snippet of code, you can use multiple \`@@\` statements to jump to the right context. For instance:
@@ class BaseClass
@@  def method():
[3 lines of pre-context]
- [old_code]
+ [new_code]
[3 lines of post-context]
Note, then, that we do not use line numbers in this diff format, as the context is enough to uniquely identify code. An example of a message that you might pass as "input" to this function, in order to apply a patch, is shown below.
\`\`\`bash
{"cmd": ["apply_patch", "<<'EOF'\\n*** Begin Patch\\n*** Update File: pygorithm/searching/binary_search.py\\n@@ class BaseClass\\n@@     def search():\\n-        pass\\n+        raise NotImplementedError()\\n@@ class Subclass\\n@@     def search():\\n-        pass\\n+        raise NotImplementedError()\\n*** End Patch\\nEOF\\n"], "workdir": "..."}
\`\`\`
File references can only be relative, NEVER ABSOLUTE. After the apply_patch command is run, it will always say "Done!", regardless of whether the patch was successfully applied or not. However, you can determine if there are issue and errors by looking at any warnings or logging lines printed BEFORE the "Done!" is output.
</apply_patch>

<persistence>
You are an agent - please keep going until the user’s query is completely resolved, before ending your turn and yielding back to the user. Only terminate your turn when you are sure that the problem is solved.
- Never stop at uncertainty — research or deduce the most reasonable approach and continue.
- Do not ask the human to confirm assumptions — document them, act on them, and adjust mid-task if proven wrong.
</persistence>

<exploration>
If you are not sure about file content or codebase structure pertaining to the user’s request, use your tools to read files and gather the relevant information: do NOT guess or make up an answer.
Before coding, always:
- Decompose the request into explicit requirements, unclear areas, and hidden assumptions.
- Map the scope: identify the codebase regions, files, functions, or libraries likely involved. If unknown, plan and perform targeted searches.
- Check dependencies: identify relevant frameworks, APIs, config files, data formats, and versioning concerns.
- Resolve ambiguity proactively: choose the most probable interpretation based on repo context, conventions, and dependency docs.
- Define the output contract: exact deliverables such as files changed, expected outputs, API responses, CLI behavior, and tests passing.
- Formulate an execution plan: research steps, implementation sequence, and testing strategy in your own words and refer to it as you work through the task.
</exploration>

<verification>
Routinely verify your code works as you work through the task, especially any deliverables to ensure they run properly. Don't hand back to the user until you are sure that the problem is solved.
Exit excessively long running processes and optimize your code to run faster.
</verification>

<efficiency>
Efficiency is key. you have a time limit. Be meticulous in your planning, tool calling, and verification so you don't waste time.
</efficiency>

<final_instructions>
Never use editor tools to edit files. Always use the \`apply_patch\` tool.
</final_instructions>
```


"""

</details>


## YouTube Video Transcripts

<details>
<summary>[00:00] (Video opens with a man in a black t-shirt and glasses standing in front of a black background. "IBM Technology" is displayed in the top left corner.)</summary>

[00:00] (Video opens with a man in a black t-shirt and glasses standing in front of a black background. "IBM Technology" is displayed in the top left corner.)
What is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data such as databases or APIs. Typically, you use tool calling fire [00:10] (The man picks up a green marker and starts drawing on a transparent surface in front of him. He draws a vertical line on the left side, labels it "APP", then draws another vertical line on the right, labels it "LLM", and writes "chat" at the top center.) a chat interface. So you would have your client application in one hand and then the LLM on the other side.

[00:23] (The man continues drawing arrows and labels between the "APP" and "LLM" columns.)
From your client application, you would send a set of messages together with a tool definition to the LLM. So you would have your messages here together with your list of tools. The LLM will look at both your message and the list of tools, and it's going to recommend a tool you should call. From your client application, you should call this tool and then supply the answer back to the LLM. [00:54] So this tool response will be interpreted by the LLM, and this will either tell you the next tool to call or it will give you the final answer.

[01:03] (The man draws a box around the "APP" column and lists items below "tool definition".)
In your application, you're responsible for creating the tool definition. So this tool definition includes a couple of things, such as the name of every tool. It also includes a description for the tool. So this is where you can give additional information about how to use the tool or when to use it. [01:25] And it also includes the input parameters needed to make a tool call. (He then draws a box labeled "tools" below "APP" and branches out three circles labeled "API", "DB", and "Code".) And the tools can be anything. So the tools could be APIs or databases. But it could also be code that you interpret via code interpreter.

[01:39] (The man looks at the diagram and continues explaining an example.)
So let's look at an example. Assume you want to find the weather in Miami. You might ask the LLM about the temperature in Miami. You also provide a list of tools, and one of these tools is the weather API. The LLM will look at both your question, which is what is the temperature in Miami. [02:00] It would also look at the weather API, and then based on the tool definition for the weather API, it's going to tell you how to call the weather tool. So in here, it's going to create a tool that you can use right here on this side where you call the API to collect the weather information. You would then supply the weather information back to the LLM. So let's say it would be 71 degrees. [02:29] The LLM will look at the tool response and then give the final answer, which might be something in the trend of the weather in Miami is pretty nice, it's 71 degrees.

_This section describes the traditional tool calling process, where an application sends messages and tool definitions to an LLM, which then recommends a tool to call, and the application executes the tool and returns the response to the LLM for a final answer._

[02:34] (The man moves to the LLM side of the diagram and adds bullet points.)
This has some downsides. So when you do traditional tool calling where you have an LLM and a client application, you could see the LLM hallucinate. Sometimes the LLM can also make up incorrect tool calls. That's why I also want to look at embedded tool calling.

[03:00] (The man writes "embedded" above the center of the drawing area and starts drawing a new box in the middle.)
We just looked at traditional tool calling, but traditional tool calling has its flaws. As I mentioned, the LLM could hallucinate or create incorrect tool calls. That's why I also want to take embedded tool calling into account. With embedded tool calling, you use a library or framework to interact with the LLM and your tool definitions. The library would be somewhere between your application and the large language model. [03:22] (He draws a box labeled "library" between the "APP" and "LLM" columns, dividing the library box into two sections: "tool def" and "tool exec".) In the library, you would do the tool definition, but you would also execute the tool calls. So let's draw a line between these sections here. So the library will contain your tool definition. It would also contain the tool execution.

[03:40] (The man draws an arrow from "APP" to the "library" box, and another from the "library" box to "LLM".)
So when you send a message from your application to the large language model, it will go through the library. So your message could still be what is the temperature in Miami? The library will then append the tool definition and send your message together with the tools to the LLM. So this will be your message plus your list of tools. [04:04] Instead of sending the tool to call to the application or the user, it will be sent to the library, which will then do the tool execution. (He draws an arrow from "LLM" back to the "library" box, then from the "library" box back to "APP", and adds "71°" to the final arrow.) And this way, the library will provide you with the final answer, which could be it's 71 degrees in Miami. When you use embedded tool calling, the LLM will no longer hallucinate, as the library to help you with the tool calling or the embedded tool calling is going to take care of the tool execution and will retry the tool calls in case it's needed.

[04:32] (The man gestures to both sides of the diagram.)
So in this video, we looked at both traditional tool calling and also embedded tool calling, where especially embedded tool calling will help you to prevent hallucination or help you with the execution of tools, which could be APIs, databases, or code.
(Video transitions to a blue screen with the IBM logo.)

_This section introduces embedded tool calling, where a library or framework handles both tool definition and execution, acting as an intermediary between the application and the LLM, thereby mitigating issues like hallucination and incorrect tool calls seen in traditional tool calling._

</details>


## Additional Sources Scraped

<details>
<summary>function-calling-openai-api</summary>

**Function calling** (also known as **tool calling**) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. This guide shows how you can connect a model to data and actions provided by your application. We’ll show how to use function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs.

If your application has many functions or large schemas, you can pair function calling with [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search) to defer rarely used tools and load them only when the model needs them.

## How it works

Let’s begin by understanding a few key terms about tool calling. After we have a shared vocabulary for tool calling, we’ll show you how it’s done with some practical examples.

Tools - functionality we give the model

A **function** or **tool** refers in the abstract to a piece of functionality that we tell the model it has access to. As a model generates a response to a prompt, it may decide that it needs data or functionality provided by a tool to follow the prompt’s instructions.

You could give the model access to tools that:

- Get today’s weather for a location
- Access account details for a given user ID
- Issue refunds for a lost order

Or anything else you’d like the model to be able to know or do as it responds to a prompt.

When we make an API request to the model with a prompt, we can include a list of tools the model could consider using. For example, if we wanted the model to be able to answer questions about the current weather somewhere in the world, we might give it access to a `get_weather` tool that takes `location` as an argument.

Tool calls - requests from the model to use tools

A **function call** or **tool call** refers to a special kind of response we can get from the model if it examines a prompt, and then determines that in order to follow the instructions in the prompt, it needs to call one of the tools we made available to it.

If the model receives a prompt like “what is the weather in Paris?” in an API request, it could respond to that prompt with a tool call for the `get_weather` tool, with `Paris` as the `location` argument.

Tool call outputs - output we generate for the model

A **function call output** or **tool call output** refers to the response a tool generates using the input from a model’s tool call. The tool call output can either be structured JSON or plain text, and it should contain a reference to a specific model tool call (referenced by `call_id` in the examples to come).
To complete our weather example:

- The model has access to a `get_weather` **tool** that takes `location` as an argument.
- In response to a prompt like “what’s the weather in Paris?” the model returns a **tool call** that contains a `location` argument with a value of `Paris`
- The **tool call output** might return a JSON object (e.g., `{"temperature": "25", "unit": "C"}`, indicating a current temperature of 25 degrees), [Image contents](https://developers.openai.com/api/docs/guides/images), or [File contents](https://developers.openai.com/api/docs/guides/file-inputs).

We then send all of the tool definition, the original prompt, the model’s tool call, and the tool call output back to the model to finally receive a text response like:

```
The weather in Paris today is 25C.
```

Functions versus tools

- A function is a specific kind of tool, defined by a JSON schema. A function definition allows the model to pass data to your application, where your code can access data or take actions suggested by the model.
- In addition to function tools, there are custom tools (described in this guide) that work with free text inputs and outputs.
- There are also [built-in tools](https://developers.openai.com/api/docs/guides/tools) that are part of the OpenAI platform. These tools enable the model to [search the web](https://developers.openai.com/api/docs/guides/tools-web-search), [execute code](https://developers.openai.com/api/docs/guides/tools-code-interpreter), access the functionality of an [MCP server](https://developers.openai.com/api/docs/guides/tools-remote-mcp), and more.

### The tool calling flow

Tool calling is a multi-step conversation between your application and a model via the OpenAI API. The tool calling flow has five high level steps:

1. Make a request to the model with tools it could call
2. Receive a tool call from the model
3. Execute code on the application side with input from the tool call
4. Make a second request to the model with the tool output
5. Receive a final response from the model (or more tool calls)

https://cdn.openai.com/API/docs/images/function-calling-diagram-steps.png

## Function tool example

Let’s look at an end-to-end tool calling flow for a `get_horoscope` function that gets a daily horoscope for an astrological sign.

Complete tool calling example

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
from openai import OpenAI
import json

client = OpenAI()

# 1. Define a list of callable tools for the model
tools = [\
    {\
        "type": "function",\
        "function": {\
            "name": "get_horoscope",\
            "description": "Get today's horoscope for an astrological sign.",\
            "parameters": {\
                "type": "object",\
                "properties": {\
                    "sign": {\
                        "type": "string",\
                        "description": "An astrological sign like Taurus or Aquarius",\
                    },\
                },\
                "required": ["sign"],\
                "additionalProperties": False,\
            },\
            "strict": True,\
        },\
    },\
]

def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."

messages = [\
    {"role": "user", "content": "What is my horoscope? I am an Aquarius."}\
]

# 2. Prompt the model with tools defined
response = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools,
)

messages.append(response.choices[0].message)

for tool_call in response.choices[0].message.tool_calls or []:
    if tool_call.function.name == "get_horoscope":
        # 3. Execute the function logic for get_horoscope
        args = json.loads(tool_call.function.arguments)
        horoscope = get_horoscope(args["sign"])

        # 4. Provide function call results to the model
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps({"horoscope": horoscope}),
            }
        )

response = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools,
)

# 5. The model should be able to give a response!
print(response.choices[0].message.content)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
import OpenAI from "openai";

const openai = new OpenAI();

// 1. Define a list of callable tools for the model
const tools = [\
  {\
    type: "function",\
    function: {\
      name: "get_horoscope",\
      description: "Get today's horoscope for an astrological sign.",\
      parameters: {\
        type: "object",\
        properties: {\
          sign: {\
            type: "string",\
            description: "An astrological sign like Taurus or Aquarius",\
          },\
        },\
        required: ["sign"],\
        additionalProperties: false,\
      },\
      strict: true,\
    },\
  },\
];

function getHoroscope(sign) {
  return `${sign}: Next Tuesday you will befriend a baby otter.`;
}

const messages = [\
  { role: "user", content: "What is my horoscope? I am an Aquarius." },\
];

// 2. Prompt the model with tools defined
let response = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages,
  tools,
});

messages.push(response.choices[0].message);

for (const toolCall of response.choices[0].message.tool_calls ?? []) {
  if (toolCall.function.name === "get_horoscope") {
    // 3. Execute the function logic for get_horoscope
    const args = JSON.parse(toolCall.function.arguments);
    const horoscope = getHoroscope(args.sign);

    // 4. Provide function call results to the model
    messages.push({
      role: "tool",
      tool_call_id: toolCall.id,
      content: JSON.stringify({ horoscope }),
    });
  }
}

response = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages,
  tools,
});

// 5. The model should be able to give a response!
console.log(response.choices[0].message.content);
```

Complete tool calling example

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
from openai import OpenAI
import json

client = OpenAI()

# 1. Define a list of callable tools for the model
tools = [\
    {\
        "type": "function",\
        "name": "get_horoscope",\
        "description": "Get today's horoscope for an astrological sign.",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "sign": {\
                    "type": "string",\
                    "description": "An astrological sign like Taurus or Aquarius",\
                },\
            },\
            "required": ["sign"],\
        },\
    },\
]

def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."

# Create a running input list we will add to over time
input_list = [\
    {"role": "user", "content": "What is my horoscope? I am an Aquarius."}\
]

# 2. Prompt the model with tools defined
response = client.responses.create(
    model="gpt-5",
    tools=tools,
    input=input_list,
)

# Save function call outputs for subsequent requests
input_list += response.output

for item in response.output:
    if item.type == "function_call":
        if item.name == "get_horoscope":
            # 3. Execute the function logic for get_horoscope
            horoscope = get_horoscope(json.loads(item.arguments))

            # 4. Provide function call results to the model
            input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps({
                  "horoscope": horoscope
                })
            })

print("Final input:")
print(input_list)

response = client.responses.create(
    model="gpt-5",
    instructions="Respond only with a horoscope generated by a tool.",
    tools=tools,
    input=input_list,
)

# 5. The model should be able to give a response!
print("Final output:")
print(response.model_dump_json(indent=2))
print("\n" + response.output_text)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
import OpenAI from "openai";
const openai = new OpenAI();

// 1. Define a list of callable tools for the model
const tools = [\
  {\
    type: "function",\
    name: "get_horoscope",\
    description: "Get today's horoscope for an astrological sign.",\
    parameters: {\
      type: "object",\
      properties: {\
        sign: {\
          type: "string",\
          description: "An astrological sign like Taurus or Aquarius",\
        },\
      },\
      required: ["sign"],\
    },\
  },\
];

function getHoroscope(sign) {
  return sign + " Next Tuesday you will befriend a baby otter.";
}

// Create a running input list we will add to over time
let input = [\
  { role: "user", content: "What is my horoscope? I am an Aquarius." },\
];

// 2. Prompt the model with tools defined
let response = await openai.responses.create({
  model: "gpt-5",
  tools,
  input,
});

response.output.forEach((item) => {
  if (item.type == "function_call") {
    if (item.name == "get_horoscope"):
      // 3. Execute the function logic for get_horoscope
      const horoscope = get_horoscope(JSON.parse(item.arguments))

      // 4. Provide function call results to the model
      input_list.push({
          type: "function_call_output",
          call_id: item.call_id,
          output: json.dumps({
            horoscope
          })
      })
  }
});

console.log("Final input:");
console.log(JSON.stringify(input, null, 2));

response = await openai.responses.create({
  model: "gpt-5",
  instructions: "Respond only with a horoscope generated by a tool.",
  tools,
  input,
});

// 5. The model should be able to give a response!
console.log("Final output:");
console.log(JSON.stringify(response.output, null, 2));
```

Note that for reasoning models like GPT-5 or o4-mini, any reasoning items
returned in model responses with tool calls must also be passed back with tool
call outputs.

## Defining functions

Functions are usually declared in the `tools` parameter of each API request. With [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), your application can also load deferred functions later in the interaction. Either way, each callable function uses the same schema shape. A function definition has the following properties:

| Field | Description |
| --- | --- |
| `type` | This should always be `function` |
| `name` | The function’s name (e.g. `get_weather`) |
| `description` | Details on when and how to use the function |
| `parameters` | [JSON schema](https://json-schema.org/) defining the function’s input arguments |
| `strict` | Whether to enforce strict mode for the function call |

Here is an example function definition for a `get_weather` function

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
{
  "type": "function",
  "name": "get_weather",
  "description": "Retrieves current weather for the given location.",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City and country e.g. Bogotá, Colombia"
      },
      "units": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Units the temperature will be returned in."
      }
    },
    "required": ["location", "units"],
    "additionalProperties": false
  },
  "strict": true
}
```

Because the `parameters` are defined by a [JSON schema](https://json-schema.org/), you can leverage many of its rich features like property types, enums, descriptions, nested objects, and, recursive objects.

## Defining namespaces

Use namespaces to group related tools by domain, such as `crm`, `billing`, or `shipping`. Namespaces help organize similar tools and are especially useful when the model must choose between tools that serve different systems or purposes, such as one search tool for your CRM and another for your support ticketing system.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
{
  "type": "namespace",
  "name": "crm",
  "description": "CRM tools for customer lookup and order management.",
  "tools": [\
    {\
      "type": "function",\
      "name": "get_customer_profile",\
      "description": "Fetch a customer profile by customer ID.",\
      "parameters": {\
        "type": "object",\
        "properties": {\
          "customer_id": { "type": "string" }\
        },\
        "required": ["customer_id"],\
        "additionalProperties": false\
      }\
    },\
    {\
      "type": "function",\
      "name": "list_open_orders",\
      "description": "List open orders for a customer ID.",\
      "defer_loading": true,\
      "parameters": {\
        "type": "object",\
        "properties": {\
          "customer_id": { "type": "string" }\
        },\
        "required": ["customer_id"],\
        "additionalProperties": false\
      }\
    }\
  ]
}
```

## Tool search

If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with `tool_search`. The `tool_search` tool lets the model search for relevant tools, add them to the model context, and then use them. Read the [tool search guide](https://developers.openai.com/api/docs/guides/tools-tool-search) to learn more.

(Optional) Function calling wth pydantic and zod

While we encourage you to define your function schemas directly, our SDKs have helpers to convert `pydantic` and `zod` objects into schemas. Not all `pydantic` and `zod` features are supported.

Define objects to represent function schema

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
from openai import OpenAI, pydantic_function_tool
from pydantic import BaseModel, Field

client = OpenAI()

class GetWeather(BaseModel):
    location: str = Field(
        ...,
        description="City and country e.g. Bogotá, Colombia"
    )

tools = [pydantic_function_tool(GetWeather)]

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools
)

print(completion.choices[0].message.tool_calls)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
import OpenAI from "openai";
import { z } from "zod";
import { zodFunction } from "openai/helpers/zod";

const openai = new OpenAI();

const GetWeatherParameters = z.object({
  location: z.string().describe("City and country e.g. Bogotá, Colombia"),
});

const tools = [\
  zodFunction({ name: "getWeather", parameters: GetWeatherParameters }),\
];

const messages = [\
  { role: "user", content: "What's the weather like in Paris today?" },\
];

const response = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages,
  tools,
  store: true,
});

console.log(response.choices[0].message.tool_calls);
```

### Best practices for defining functions

1. **Write clear and detailed function names, parameter descriptions, and instructions.**
   - **Explicitly describe the purpose of the function and each parameter** (and its format), and what the output represents.
   - **Use the system prompt to describe when (and when not) to use each function.** Generally, tell the model _exactly_ what to do.
   - **Include examples and edge cases**, especially to rectify any recurring failures. ( **Note:** Adding examples may hurt performance for [reasoning models](https://developers.openai.com/api/docs/guides/reasoning).)
   - **For deferred tools, put detailed guidance in the function description and keep the namespace description concise.** The namespace helps the model choose what to load; the function description helps it use the loaded tool correctly.
2. **Apply software engineering best practices.**
   - **Make the functions obvious and intuitive**. ( [principle of least surprise](https://en.wikipedia.org/wiki/Principle_of_least_astonishment))
   - **Use enums** and object structure to make invalid states unrepresentable. (e.g. `toggle_light(on: bool, off: bool)` allows for invalid calls)
   - **Pass the intern test.** Can an intern/human correctly use the function given nothing but what you gave the model? (If not, what questions do they ask you? Add the answers to the prompt.)
3. **Offload the burden from the model and use code where possible.**
   - **Don’t make the model fill arguments you already know.** For example, if you already have an `order_id` based on a previous menu, don’t have an `order_id` param – instead, have no params `submit_refund()` and pass the `order_id` with code.
   - **Combine functions that are always called in sequence.** For example, if you always call `mark_location()` after `query_location()`, just move the marking logic into the query function call.
4. **Keep the number of initially available functions small for higher accuracy.**
   - **Evaluate your performance** with different numbers of functions.
   - **Aim for fewer than 20 functions available at the start of a turn** at any one time, though this is just a soft suggestion.
   - **Use tool search** to defer large or infrequently used parts of your tool surface instead of exposing everything up front.
5. **Leverage OpenAI resources.**
   - **Generate and iterate on function schemas** in the [Playground](https://platform.openai.com/playground).
   - **Consider [fine-tuning](https://developers.openai.com/api/docs/guides/fine-tuning) to increase function calling accuracy** for large numbers of functions or difficult tasks. ( [cookbook](https://developers.openai.com/cookbook/examples/fine_tuning_for_function_calling))

### Token Usage

Under the hood, functions are injected into the system message in a syntax the model has been trained on. This means callable function definitions count against the model’s context limit and are billed as input tokens. If you run into token limits, we suggest limiting the number of functions loaded up front, shortening descriptions where possible, or using [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search) so deferred tools are loaded only when needed.

It is also possible to use [fine-tuning](https://developers.openai.com/api/docs/guides/fine-tuning#fine-tuning-examples) to reduce the number of tokens used if you have many functions defined in your tools specification.

## Handling function calls

When the model calls a function, you must execute it and return the result. Since model responses can include zero, one, or multiple calls, it is best practice to assume there are several.

The response has an array of `tool_calls`, each with an `id` (used later to submit the function result) and a `function` containing a `name` and JSON-encoded `arguments`.

Sample response with multiple function calls

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
[\
    {\
        "id": "call_12345xyz",\
        "type": "function",\
        "function": {\
            "name": "get_weather",\
            "arguments": "{\"location\":\"Paris, France\"}"\
        }\
    },\
    {\
        "id": "call_67890abc",\
        "type": "function",\
        "function": {\
            "name": "get_weather",\
            "arguments": "{\"location\":\"Bogotá, Colombia\"}"\
        }\
    },\
    {\
        "id": "call_99999def",\
        "type": "function",\
        "function": {\
            "name": "send_email",\
            "arguments": "{\"to\":\"bob@email.com\",\"body\":\"Hi bob\"}"\
        }\
    }\
]
```

Execute function calls and append results

python

```
1
2
3
4
5
6
7
8
9
10
for tool_call in completion.choices[0].message.tool_calls:
    name = tool_call.function.name
    args = json.loads(tool_call.function.arguments)

    result = call_function(name, args)
    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": str(result)
    })
```

```
1
2
3
4
5
6
7
8
9
10
11
for (const toolCall of completion.choices[0].message.tool_calls) {
    const name = toolCall.function.name;
    const args = JSON.parse(toolCall.function.arguments);

    const result = callFunction(name, args);
    messages.push({
        role: "tool",
        tool_call_id: toolCall.id,
        content: result.toString()
    });
}
```

The response `output` array contains an entry with the `type` having a value of `function_call`. Each entry with a `call_id` (used later to submit the function result), `name`, and JSON-encoded `arguments`.

Sample response with multiple function calls

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
[\
    {\
        "id": "fc_12345xyz",\
        "call_id": "call_12345xyz",\
        "type": "function_call",\
        "name": "get_weather",\
        "arguments": "{\"location\":\"Paris, France\"}"\
    },\
    {\
        "id": "fc_67890abc",\
        "call_id": "call_67890abc",\
        "type": "function_call",\
        "name": "get_weather",\
        "arguments": "{\"location\":\"Bogotá, Colombia\"}"\
    },\
    {\
        "id": "fc_99999def",\
        "call_id": "call_99999def",\
        "type": "function_call",\
        "name": "send_email",\
        "arguments": "{\"to\":\"bob@email.com\",\"body\":\"Hi bob\"}"\
    }\
]
```

If you are using [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), you may also see `tool_search_call` and `tool_search_output` items before a `function_call`. Once the function is loaded, handle the function call in the same way shown here.

Execute function calls and append results

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
for tool_call in response.output:
    if tool_call.type != "function_call":
        continue

    name = tool_call.name
    args = json.loads(tool_call.arguments)

    result = call_function(name, args)
    input_messages.append({
        "type": "function_call_output",
        "call_id": tool_call.call_id,
        "output": str(result)
    })
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
for (const toolCall of response.output) {
    if (toolCall.type !== "function_call") {
        continue;
    }

    const name = toolCall.name;
    const args = JSON.parse(toolCall.arguments);

    const result = callFunction(name, args);
    input.push({
        type: "function_call_output",
        call_id: toolCall.call_id,
        output: result.toString()
    });
}
```

In the example above, we have a hypothetical `call_function` to route each call. Here’s a possible implementation:

Execute function calls and append results

python

```
1
2
3
4
5
def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    if name == "send_email":
        return send_email(**args)
```

```
1
2
3
4
5
6
7
8
const callFunction = async (name, args) => {
    if (name === "get_weather") {
        return getWeather(args.latitude, args.longitude);
    }
    if (name === "send_email") {
        return sendEmail(args.to, args.body);
    }
};
```

### Formatting results

The result you pass in the `function_call_output` message should typically be a string, where the format is up to you (JSON, error codes, plain text, etc.). The model will interpret that string as needed.

For functions that return images or files, you can pass an [array of image or file objects](https://developers.openai.com/api/docs/api-reference/responses/create#responses_create-input-input_item_list-item-function_tool_call_output-output) instead of a string.

If your function has no return value (e.g. `send_email`), simply return a string that indicates success or failure. (e.g. `"success"`)

### Incorporating results into response

After appending the results to your `messages`, you can send them back to the model to get a final response.

Send results back to model

python

```
1
2
3
4
5
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools,
)
```

```
1
2
3
4
5
6
const completion = await openai.chat.completions.create({
    model: "gpt-4.1",
    messages,
    tools,
    store: true,
});
```

After appending the results to your `input`, you can send them back to the model to get a final response.

Send results back to model

python

```
1
2
3
4
5
response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
```

```
1
2
3
4
5
const response = await openai.responses.create({
    model: "gpt-4.1",
    input,
    tools,
});
```

Final response

```
"It's about 15°C in Paris, 18°C in Bogotá, and I've sent that email to Bob."
```

## Additional configurations

### Tool choice

By default the model will determine when and how many tools to use. You can force specific behavior with the `tool_choice` parameter.

1. **Auto:** ( _Default_) Call zero, one, or multiple functions. `tool_choice: "auto"`
2. **Required:** Call one or more functions.
`tool_choice: "required"`
3. **Forced Function:** Call exactly one specific function.
`tool_choice: {"type": "function", "name": "get_weather"}`
4. **Allowed tools:** Restrict the tool calls the model can make to a subset of
the tools available to the model.

**When to use allowed\_tools**

You might want to configure an `allowed_tools` list in case you want to make only
a subset of tools available across model requests, but not modify the list of tools you pass in, so you can maximize savings from [prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching).

```
1
2
3
4
5
6
7
8
9
"tool_choice": {
    "type": "allowed_tools",
    "mode": "auto",
    "tools": [\
        { "type": "function", "name": "get_weather" },\
        { "type": "function", "name": "search_docs" }\
    ]
  }
}
```

You can also set `tool_choice` to `"none"` to imitate the behavior of passing no functions.

When you use tool search, `tool_choice` still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset.

### Parallel function calling

Parallel function calling is not possible when using [built-in\
tools](https://developers.openai.com/api/docs/guides/tools).

The model may choose to call multiple functions in a single turn. You can prevent this by setting `parallel_tool_calls` to `false`, which ensures exactly zero or one tool is called.

**Note:** Currently, if you are using a fine tuned model and the model calls multiple functions in one turn then [strict mode](https://developers.openai.com/api/docs/guides/function-calling#strict-mode) will be disabled for those calls.

**Note for `gpt-4.1-nano-2025-04-14`:** This snapshot of `gpt-4.1-nano` can sometimes include multiple tools calls for the same tool if parallel tool calls are enabled. It is recommended to disable this feature when using this nano snapshot.

### Strict mode

Setting `strict` to `true` will ensure function calls reliably adhere to the function schema, instead of being best effort. We recommend always enabling strict mode.

Under the hood, strict mode works by leveraging our [structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) feature and therefore introduces a couple requirements:

1. `additionalProperties` must be set to `false` for each object in the `parameters`.
2. All fields in `properties` must be marked as `required`.

You can denote optional fields by adding `null` as a `type` option (see example below).

Strict mode enabledStrict mode disabled

Strict mode enabled

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retrieves current weather for the given location.",
        "strict": true,
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                },
                "units": {
                    "type": ["string", "null"],
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Units the temperature will be returned in."
                }
            },
            "required": ["location", "units"],
            "additionalProperties": false
        }
    }
}
```

Strict mode disabled

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Retrieves current weather for the given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                },
                "units": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "Units the temperature will be returned in."
                }
            },
            "required": ["location"],
        }
    }
}
```

Strict mode enabledStrict mode disabled

Strict mode enabled

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
{
    "type": "function",
    "name": "get_weather",
    "description": "Retrieves current weather for the given location.",
    "strict": true,
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            },
            "units": {
                "type": ["string", "null"],
                "enum": ["celsius", "fahrenheit"],
                "description": "Units the temperature will be returned in."
            }
        },
        "required": ["location", "units"],
        "additionalProperties": false
    }
}
```

Strict mode disabled

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
{
    "type": "function",
    "name": "get_weather",
    "description": "Retrieves current weather for the given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            },
            "units": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Units the temperature will be returned in."
            }
        },
        "required": ["location"],
    }
}
```

All schemas generated in the
[playground](https://platform.openai.com/playground) have strict mode enabled.

While we recommend you enable strict mode, it has a few limitations:

1. Some features of JSON schema are not supported. (See [supported schemas](https://developers.openai.com/api/docs/guides/structured-outputs?context=with_parse#supported-schemas).)

Specifically for fine tuned models:

1. Schemas undergo additional processing on the first request (and are then cached). If your schemas vary from request to request, this may result in higher latencies.
2. Schemas are cached for performance, and are not eligible for [zero data retention](https://developers.openai.com/api/docs/models#how-we-use-your-data).

## Streaming

Streaming can be used to surface progress by showing which function is called as the model fills its arguments, and even displaying the arguments in real time.

Streaming function calls is very similar to streaming regular responses: you set `stream` to `true` and get chunks with `delta` objects.

Streaming function calls

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "function": {\
        "name": "get_weather",\
        "description": "Get current temperature for a given location.",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "location": {\
                    "type": "string",\
                    "description": "City and country e.g. Bogotá, Colombia"\
                }\
            },\
            "required": ["location"],\
            "additionalProperties": False\
        },\
        "strict": True\
    }\
}]

stream = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools,
    stream=True
)

for chunk in stream:
    delta = chunk.choices[0].delta
    print(delta.tool_calls)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    "type": "function",\
    "function": {\
        "name": "get_weather",\
        "description": "Get current temperature for a given location.",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "location": {\
                    "type": "string",\
                    "description": "City and country e.g. Bogotá, Colombia"\
                }\
            },\
            "required": ["location"],\
            "additionalProperties": false\
        },\
        "strict": true\
    }\
}];

const stream = await openai.chat.completions.create({
    model: "gpt-4.1",
    messages: [{ role: "user", content: "What's the weather like in Paris today?" }],
    tools,
    stream: true,
    store: true,
});

for await (const chunk of stream) {
    const delta = chunk.choices[0].delta;
    console.log(delta.tool_calls);
}
```

Output delta.tool\_calls

```
1
2
3
4
5
6
7
8
9
[{"index": 0, "id": "call_DdmO9pD3xa9XTPNJ32zg2hcA", "function": {"arguments": "", "name": "get_weather"}, "type": "function"}]
[{"index": 0, "id": null, "function": {"arguments": "{\"", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": "location", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": "\":\"", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": "Paris", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": ",", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": " France", "name": null}, "type": null}]
[{"index": 0, "id": null, "function": {"arguments": "\"}", "name": null}, "type": null}]
null
```

Instead of aggregating chunks into a single `content` string, however, you’re aggregating chunks into an encoded `arguments` JSON object.

When the model calls one or more functions the `tool_calls` field of each `delta` will be populated. Each `tool_call` contains the following fields:

| Field | Description |
| --- | --- |
| `index` | Identifies which function call the `delta` is for |
| `id` | Tool call id. |
| `function` | Function call delta (`name` and `arguments`) |
| `type` | Type of `tool_call` (always `function` for function calls) |

Many of these fields are only set for the first `delta` of each tool call, like `id`, `function.name`, and `type`.

Below is a code snippet demonstrating how to aggregate the `delta`s into a final `tool_calls` object.

Accumulating tool\_call deltas

python

```
1
2
3
4
5
6
7
8
9
10
final_tool_calls = {}

for chunk in stream:
    for tool_call in chunk.choices[0].delta.tool_calls or []:
        index = tool_call.index

        if index not in final_tool_calls:
            final_tool_calls[index] = tool_call

        final_tool_calls[index].function.arguments += tool_call.function.arguments
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
const finalToolCalls = {};

for await (const chunk of stream) {
    const toolCalls = chunk.choices[0].delta.tool_calls || [];
    for (const toolCall of toolCalls) {
        const { index } = toolCall;

        if (!finalToolCalls[index]) {
            finalToolCalls[index] = toolCall;
        }

        finalToolCalls[index].function.arguments += toolCall.function.arguments;
    }
}
```

Accumulated final\_tool\_calls\[0\]

```
1
2
3
4
5
6
7
8
{
    "index": 0,
    "id": "call_RzfkBpJgzeR0S242qfvjadNe",
    "function": {
        "name": "get_weather",
        "arguments": "{\"location\":\"Paris, France\"}"
    }
}
```

Streaming can be used to surface progress by showing which function is called as the model fills its arguments, and even displaying the arguments in real time.

Streaming function calls is very similar to streaming regular responses: you set `stream` to `true` and get different `event` objects.

Streaming function calls

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
from openai import OpenAI

client = OpenAI()

tools = [{\
    "type": "function",\
    "name": "get_weather",\
    "description": "Get current temperature for a given location.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "location": {\
                "type": "string",\
                "description": "City and country e.g. Bogotá, Colombia"\
            }\
        },\
        "required": [\
            "location"\
        ],\
        "additionalProperties": False\
    }\
}]

stream = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools,
    stream=True
)

for event in stream:
    print(event)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [{\
    type: "function",\
    name: "get_weather",\
    description: "Get current temperature for provided coordinates in celsius.",\
    parameters: {\
        type: "object",\
        properties: {\
            latitude: { type: "number" },\
            longitude: { type: "number" }\
        },\
        required: ["latitude", "longitude"],\
        additionalProperties: false\
    },\
    strict: true\
}];

const stream = await openai.responses.create({
    model: "gpt-4.1",
    input: [{ role: "user", content: "What's the weather like in Paris today?" }],
    tools,
    stream: true,
    store: true,
});

for await (const event of stream) {
    console.log(event)
}
```

Output events

```
1
2
3
4
5
6
7
8
9
10
{"type":"response.output_item.added","response_id":"resp_1234xyz","output_index":0,"item":{"type":"function_call","id":"fc_1234xyz","call_id":"call_1234xyz","name":"get_weather","arguments":""}}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"{\""}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"location"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"\":\""}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"Paris"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":","}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":" France"}
{"type":"response.function_call_arguments.delta","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"delta":"\"}"}
{"type":"response.function_call_arguments.done","response_id":"resp_1234xyz","item_id":"fc_1234xyz","output_index":0,"arguments":"{\"location\":\"Paris, France\"}"}
{"type":"response.output_item.done","response_id":"resp_1234xyz","output_index":0,"item":{"type":"function_call","id":"fc_1234xyz","call_id":"call_1234xyz","name":"get_weather","arguments":"{\"location\":\"Paris, France\"}"}}
```

Instead of aggregating chunks into a single `content` string, however, you’re aggregating chunks into an encoded `arguments` JSON object.

When the model calls one or more functions an event of type `response.output_item.added` will be emitted for each function call that contains the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `output_index` | The index of the output item in the response. This represents the individual function calls in the response. |
| `item` | The in-progress function call item that includes a `name`, `arguments` and `id` field |

Afterwards you will receive a series of events of type `response.function_call_arguments.delta` which will contain the `delta` of the `arguments` field. These events contain the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `item_id` | The id of the function call item that the delta belongs to |
| `output_index` | The index of the output item in the response. This represents the individual function calls in the response. |
| `delta` | The delta of the `arguments` field. |

Below is a code snippet demonstrating how to aggregate the `delta`s into a final `tool_call` object.

Accumulating tool\_call deltas

python

```
1
2
3
4
5
6
7
8
9
10
final_tool_calls = {}

for event in stream:
    if event.type === 'response.output_item.added':
        final_tool_calls[event.output_index] = event.item;
    elif event.type === 'response.function_call_arguments.delta':
        index = event.output_index

        if final_tool_calls[index]:
            final_tool_calls[index].arguments += event.delta
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
const finalToolCalls = {};

for await (const event of stream) {
    if (event.type === 'response.output_item.added') {
        finalToolCalls[event.output_index] = event.item;
    } else if (event.type === 'response.function_call_arguments.delta') {
        const index = event.output_index;

        if (finalToolCalls[index]) {
            finalToolCalls[index].arguments += event.delta;
        }
    }
}
```

Accumulated final\_tool\_calls\[0\]

```
1
2
3
4
5
6
7
{
    "type": "function_call",
    "id": "fc_1234xyz",
    "call_id": "call_2345abc",
    "name": "get_weather",
    "arguments": "{\"location\":\"Paris, France\"}"
}
```

When the model has finished calling the functions an event of type `response.function_call_arguments.done` will be emitted. This event contains the entire function call including the following fields:

| Field | Description |
| --- | --- |
| `response_id` | The id of the response that the function call belongs to |
| `output_index` | The index of the output item in the response. This represents the individual function calls in the response. |
| `item` | The function call item that includes a `name`, `arguments` and `id` field. |

## Custom tools

Custom tools work in much the same way as JSON schema-driven function tools. But rather than providing the model explicit instructions on what input your tool requires, the model can pass an arbitrary string back to your tool as input. This is useful to avoid unnecessarily wrapping a response in JSON, or to apply a custom grammar to the response (more on this below).

The following code sample shows creating a custom tool that expects to receive a string of text containing Python code as a response.

Custom tool calling example

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Use the code_exec tool to print hello world to the console.",
    tools=[\
        {\
            "type": "custom",\
            "name": "code_exec",\
            "description": "Executes arbitrary Python code.",\
        }\
    ]
)
print(response.output)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5",
  input: "Use the code_exec tool to print hello world to the console.",
  tools: [\
    {\
      type: "custom",\
      name: "code_exec",\
      description: "Executes arbitrary Python code.",\
    },\
  ],
});

console.log(response.output);
```

Just as before, the `output` array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text.

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
[\
  {\
    "id": "rs_6890e972fa7c819ca8bc561526b989170694874912ae0ea6",\
    "type": "reasoning",\
    "content": [],\
    "summary": []\
  },\
  {\
    "id": "ctc_6890e975e86c819c9338825b3e1994810694874912ae0ea6",\
    "type": "custom_tool_call",\
    "status": "completed",\
    "call_id": "call_aGiFQkRWSWAIsMQ19fKqxUgb",\
    "input": "print(\"hello world\")",\
    "name": "code_exec"\
  }\
]
```

### Context-free grammars

A [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar) (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model’s text input for a custom tool.

You can provide a custom CFG using the `grammar` parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: `lark` and `regex`.

#### Lark CFG

Lark context free grammar example

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
from openai import OpenAI

client = OpenAI()

grammar = """
start: expr
expr: term (SP ADD SP term)* -> add
| term
term: factor (SP MUL SP factor)* -> mul
| factor
factor: INT
SP: " "
ADD: "+"
MUL: "*"
%import common.INT
"""

response = client.responses.create(
    model="gpt-5",
    input="Use the math_exp tool to add four plus four.",
    tools=[\
        {\
            "type": "custom",\
            "name": "math_exp",\
            "description": "Creates valid mathematical expressions",\
            "format": {\
                "type": "grammar",\
                "syntax": "lark",\
                "definition": grammar,\
            },\
        }\
    ]
)
print(response.output)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
import OpenAI from "openai";
const client = new OpenAI();

const grammar = `
start: expr
expr: term (SP ADD SP term)* -> add
| term
term: factor (SP MUL SP factor)* -> mul
| factor
factor: INT
SP: " "
ADD: "+"
MUL: "*"
%import common.INT
`;

const response = await client.responses.create({
  model: "gpt-5",
  input: "Use the math_exp tool to add four plus four.",
  tools: [\
    {\
      type: "custom",\
      name: "math_exp",\
      description: "Creates valid mathematical expressions",\
      format: {\
        type: "grammar",\
        syntax: "lark",\
        definition: grammar,\
      },\
    },\
  ],
});

console.log(response.output);
```

The output from the tool should then conform to the Lark CFG that you defined:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
[\
  {\
    "id": "rs_6890ed2b6374819dbbff5353e6664ef103f4db9848be4829",\
    "type": "reasoning",\
    "content": [],\
    "summary": []\
  },\
  {\
    "id": "ctc_6890ed2f32e8819daa62bef772b8c15503f4db9848be4829",\
    "type": "custom_tool_call",\
    "status": "completed",\
    "call_id": "call_pmlLjmvG33KJdyVdC4MVdk5N",\
    "input": "4 + 4",\
    "name": "math_exp"\
  }\
]
```

Grammars are specified using a variation of [Lark](https://lark-parser.readthedocs.io/en/stable/index.html). Model sampling is constrained using [LLGuidance](https://github.com/guidance-ai/llguidance/blob/main/docs/syntax.md). Some features of Lark are not supported:

- Lookarounds in lexer regexes
- Lazy modifiers (`*?`, `+?`, `??`) in lexer regexes
- Priorities of terminals
- Templates
- Imports (other than built-in `%import` common)
- `%declare`s

We recommend using the [Lark IDE](https://www.lark-parser.org/ide/) to experiment with custom grammars.

### Keep grammars simple

Try to make your grammar as simple as possible. The OpenAI API may return an error if the grammar is too complex, so you should ensure that your desired grammar is compatible before using it in the API.

Lark grammars can be tricky to perfect. While simple grammars perform most reliably, complex grammars often require iteration on the grammar definition itself, the prompt, and the tool description to ensure that the model does not go out of distribution.

### Correct versus incorrect patterns

Correct (single, bounded terminal):

```
start: SENTENCE
SENTENCE: /[A-Za-z, ]*(the hero|a dragon|an old man|the princess)[A-Za-z, ]*(fought|saved|found|lost)[A-Za-z, ]*(a treasure|the kingdom|a secret|his way)[A-Za-z, ]*\./
```

Do NOT do this (splitting across rules/terminals). This attempts to let rules partition free text between terminals. The lexer will greedily match the free-text pieces and you’ll lose control:

```
start: sentence
sentence: /[A-Za-z, ]+/ subject /[A-Za-z, ]+/ verb /[A-Za-z, ]+/ object /[A-Za-z, ]+/
```

Lowercase rules don’t influence how terminals are cut from the input—only terminal definitions do. When you need “free text between anchors,” make it one giant regex terminal so the lexer matches it exactly once with the structure you intend.

### Terminals versus rules

Lark uses terminals for lexer tokens (by convention, `UPPERCASE`) and rules for parser productions (by convention, `lowercase`). The most practical way to stay within the supported subset and avoid surprises is to keep your grammar simple and explicit, and to use terminals and rules with a clear separation of concerns.

The regex syntax used by terminals is the [Rust regex crate syntax](https://docs.rs/regex/latest/regex/#syntax), not Python’s `re` [module](https://docs.python.org/3/library/re.html).

### Key ideas and best practices

**Lexer runs before the parser**

Terminals are matched by the lexer (greedily / longest match wins) before any CFG rule logic is applied. If you try to “shape” a terminal by splitting it across several rules, the lexer cannot be guided by those rules—only by terminal regexes.

**Prefer one terminal when you’re carving text out of freeform spans**

If you need to recognize a pattern embedded in arbitrary text (e.g., natural language with “anything” between anchors), express that as a single terminal. Do not try to interleave free‑text terminals with parser rules; the greedy lexer will not respect your intended boundaries and it is highly likely the model will go out of distribution.

**Use rules to compose discrete tokens**

Rules are ideal when you’re combining clearly delimited terminals (numbers, keywords, punctuation) into larger structures. They’re not the right tool for constraining “the stuff in between” two terminals.

**Keep terminals simple, bounded, and self-contained**

Favor explicit character classes and bounded quantifiers (`{0,10}`, not unbounded `*` everywhere). If you need “any text up to a period”, prefer something like `/[^.\n]{0,10}*\./` rather than `/.+\./` to avoid runaway growth.

**Use rules to combine tokens, not to steer regex internals**

Good rule usage example:

```
1
2
3
4
5
6
start: expr
NUMBER: /[0-9]+/
PLUS: "+"
MINUS: "-"
expr: term (("+"|"-") term)*
term: NUMBER
```

**Treat whitespace explicitly**

Don’t rely on open-ended `%ignore` directives. Using unbounded ignore directives may cause the grammar to be too complex and/or may cause the model to go out of distribution. Prefer threading explicit terminals wherever whitespace is allowed.

### Troubleshooting

- If the API rejects the grammar because it is too complex, simplify the rules and terminals and remove unbounded `%ignore`s.
- If custom tools are called with unexpected tokens, confirm terminals aren’t overlapping; check greedy lexer.
- When the model drifts “out‑of‑distribution” (shows up as the model producing excessively long or repetitive outputs, it is syntactically valid but is semantically wrong):
  - Tighten the grammar.
  - Iterate on the prompt (add few-shot examples) and tool description (explain the grammar and instruct the model to reason and conform to it).
  - Experiment with a higher reasoning effort (e.g, bump from medium to high).

#### Regex CFG

Regex context free grammar example

python

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
from openai import OpenAI

client = OpenAI()

grammar = r"^(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<day>\d{1,2})(?:st|nd|rd|th)?\s+(?P<year>\d{4})\s+at\s+(?P<hour>0?[1-9]|1[0-2])(?P<ampm>AM|PM)$"

response = client.responses.create(
    model="gpt-5",
    input="Use the timestamp tool to save a timestamp for August 7th 2025 at 10AM.",
    tools=[\
        {\
            "type": "custom",\
            "name": "timestamp",\
            "description": "Saves a timestamp in date + time in 24-hr format.",\
            "format": {\
                "type": "grammar",\
                "syntax": "regex",\
                "definition": grammar,\
            },\
        }\
    ]
)
print(response.output)
```

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
import OpenAI from "openai";
const client = new OpenAI();

const grammar = "^(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<day>\d{1,2})(?:st|nd|rd|th)?\s+(?P<year>\d{4})\s+at\s+(?P<hour>0?[1-9]|1[0-2])(?P<ampm>AM|PM)$";

const response = await client.responses.create({
  model: "gpt-5",
  input: "Use the timestamp tool to save a timestamp for August 7th 2025 at 10AM.",
  tools: [\
    {\
      type: "custom",\
      name: "timestamp",\
      description: "Saves a timestamp in date + time in 24-hr format.",\
      format: {\
        type: "grammar",\
        syntax: "regex",\
        definition: grammar,\
      },\
    },\
  ],
});

console.log(response.output);
```

The output from the tool should then conform to the Regex CFG that you defined:

```
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
[\
  {\
    "id": "rs_6894f7a3dd4c81a1823a723a00bfa8710d7962f622d1c260",\
    "type": "reasoning",\
    "content": [],\
    "summary": []\
  },\
  {\
    "id": "ctc_6894f7ad7fb881a1bffa1f377393b1a40d7962f622d1c260",\
    "type": "custom_tool_call",\
    "status": "completed",\
    "call_id": "call_8m4XCnYvEmFlzHgDHbaOCFlK",\
    "input": "August 7th 2025 at 10AM",\
    "name": "timestamp"\
  }\
]
```

As with the Lark syntax, regexes use the [Rust regex crate syntax](https://docs.rs/regex/latest/regex/#syntax), not Python’s `re` [module](https://docs.python.org/3/library/re.html).

Some features of Regex are not supported:

- Lookarounds
- Lazy modifiers (`*?`, `+?`, `??`)

### Key ideas and best practices

**Pattern must be on one line**

If you need to match a newline in the input, use the escaped sequence `\n`. Do not use verbose/extended mode, which allows patterns to span multiple lines.

**Provide the regex as a plain pattern string**

Don’t enclose the pattern in `//`.

</details>

<details>
<summary>function-calling-with-the-gemini-api-google-ai-for-developer</summary>

# Function calling with the Gemini API

Function calling lets you connect models to external tools and APIs.
Instead of generating text responses, the model determines when to call specific
functions and provides the necessary parameters to execute real-world actions.
This allows the model to act as a bridge between natural language and real-world
actions and data. Function calling has 3 primary use cases:

- **Augment Knowledge:** Access information from external sources like
databases, APIs, and knowledge bases.
- **Extend Capabilities:** Use external tools to perform computations and
extend the limitations of the model, such as using a calculator or creating
charts.
- **Take Actions:** Interact with external systems using APIs, such as
scheduling appointments, creating invoices, sending emails, or controlling
smart home devices.

Get WeatherSchedule MeetingCreate Chart

PythonJavaScriptRESTMore

```
from google import genai
from google.genai import types

# Define the function declaration for the model
schedule_meeting_function = {
    "name": "schedule_meeting",
    "description": "Schedules a meeting with specified attendees at a given time and date.",
    "parameters": {
        "type": "object",
        "properties": {
            "attendees": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of people attending the meeting.",
            },
            "date": {
                "type": "string",
                "description": "Date of the meeting (e.g., '2024-07-29')",
            },
            "time": {
                "type": "string",
                "description": "Time of the meeting (e.g., '15:00')",
            },
            "topic": {
                "type": "string",
                "description": "The subject or topic of the meeting.",
            },
        },
        "required": ["attendees", "date", "time", "topic"],
    },
}

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[schedule_meeting_function])
config = types.GenerateContentConfig(tools=[tools])

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Schedule a meeting with Bob and Alice for 03/14/2025 at 10:00 AM about the Q3 planning.",
    config=config,
)

# Check for a function call
if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    #  In a real app, you would call your function here:
    #  result = schedule_meeting(**function_call.args)
else:
    print("No function call found in the response.")
    print(response.text)
```

```
import { GoogleGenAI, Type } from '@google/genai';

// Configure the client
const ai = new GoogleGenAI({});

// Define the function declaration for the model
const scheduleMeetingFunctionDeclaration = {
  name: 'schedule_meeting',
  description: 'Schedules a meeting with specified attendees at a given time and date.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      attendees: {
        type: Type.ARRAY,
        items: { type: Type.STRING },
        description: 'List of people attending the meeting.',
      },
      date: {
        type: Type.STRING,
        description: 'Date of the meeting (e.g., "2024-07-29")',
      },
      time: {
        type: Type.STRING,
        description: 'Time of the meeting (e.g., "15:00")',
      },
      topic: {
        type: Type.STRING,
        description: 'The subject or topic of the meeting.',
      },
    },
    required: ['attendees', 'date', 'time', 'topic'],
  },
};

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: 'Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning.',
  config: {
    tools: [{\
      functionDeclarations: [scheduleMeetingFunctionDeclaration]\
    }],
  },
});

// Check for function calls in the response
if (response.functionCalls && response.functionCalls.length > 0) {
  const functionCall = response.functionCalls[0]; // Assuming one function call
  console.log(`Function to call: ${functionCall.name}`);
  console.log(`Arguments: ${JSON.stringify(functionCall.args)}`);
  // In a real app, you would call your actual function here:
  // const result = await scheduleMeeting(functionCall.args);
} else {
  console.log("No function call found in the response.");
  console.log(response.text);
}
```

```
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      {\
        "role": "user",\
        "parts": [\
          {\
            "text": "Schedule a meeting with Bob and Alice for 03/27/2025 at 10:00 AM about the Q3 planning."\
          }\
        ]\
      }\
    ],
    "tools": [\
      {\
        "functionDeclarations": [\
          {\
            "name": "schedule_meeting",\
            "description": "Schedules a meeting with specified attendees at a given time and date.",\
            "parameters": {\
              "type": "object",\
              "properties": {\
                "attendees": {\
                  "type": "array",\
                  "items": {"type": "string"},\
                  "description": "List of people attending the meeting."\
                },\
                "date": {\
                  "type": "string",\
                  "description": "Date of the meeting (e.g., '2024-07-29')"\
                },\
                "time": {\
                  "type": "string",\
                  "description": "Time of the meeting (e.g., '15:00')"\
                },\
                "topic": {\
                  "type": "string",\
                  "description": "The subject or topic of the meeting."\
                }\
              },\
              "required": ["attendees", "date", "time", "topic"]\
            }\
          }\
        ]\
      }\
    ]
  }'
```

## How function calling works

https://ai.google.dev/static/gemini-api/docs/images/function-calling-overview.png

Function calling involves a structured interaction between your application, the
model, and external functions. Here's a breakdown of the process:

1.  **Define Function Declaration:** Define the function declaration in your
    application code. Function Declarations describe the function's name,
    parameters, and purpose to the model.
2.  **Call LLM with function declarations:** Send user prompt along with the
    function declaration(s) to the model. It analyzes the request and determines
    if a function call would be helpful. If so, it responds with a structured
    JSON object.
3.  **Execute Function Code (Your Responsibility):** The Model _doesn't_
    execute the function itself. It's your application's responsibility to
    process the response and check for Function Call, if

    -   **Yes**: Extract the name and args of the function and execute the
        corresponding function in your application.
    -   **No:** The model has provided a direct text response to the prompt
        (this flow is less emphasized in the example but is a possible outcome).
4.  **Create User friendly response:** If a function was executed, capture the
    result and send it back to the model in a subsequent turn of the
    conversation. It will use the result to generate a final, user-friendly
    response that incorporates the information from the function call.

This process can be repeated over multiple turns, allowing for complex
interactions and workflows. The model also supports calling multiple functions
in a single turn ( [parallel function\\
calling](https://ai.google.dev/gemini-api/docs/function-calling#parallel_function_calling)) and in
sequence ( [compositional function\\
calling](https://ai.google.dev/gemini-api/docs/function-calling#compositional_function_calling)).

### Step 1: Define a function declaration

Define a function and its declaration within your application code that allows
users to set light values and make an API request. This function could call
external services or APIs.

PythonJavaScriptMore

```
# Define a function that the model can call to control smart lights
set_light_values_declaration = {
    "name": "set_light_values",
    "description": "Sets the brightness and color temperature of a light.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "integer",
                "description": "Light level from 0 to 100. Zero is off and 100 is full brightness",
            },
            "color_temp": {
                "type": "string",
                "enum": ["daylight", "cool", "warm"],
                "description": "Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.",
            },
        },
        "required": ["brightness", "color_temp"],
    },
}

# This is the actual function that would be called based on the model's suggestion
def set_light_values(brightness: int, color_temp: str) -> dict[str, int | str]:
    """Set the brightness and color temperature of a room light. (mock API).

    Args:
        brightness: Light level from 0 to 100. Zero is off and 100 is full brightness
        color_temp: Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.

    Returns:
        A dictionary containing the set brightness and color temperature.
    """
    return {"brightness": brightness, "colorTemperature": color_temp}
```

```
import { Type } from '@google/genai';

// Define a function that the model can call to control smart lights
const setLightValuesFunctionDeclaration = {
  name: 'set_light_values',
  description: 'Sets the brightness and color temperature of a light.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'Light level from 0 to 100. Zero is off and 100 is full brightness',
      },
      color_temp: {
        type: Type.STRING,
        enum: ['daylight', 'cool', 'warm'],
        description: 'Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.',
      },
    },
    required: ['brightness', 'color_temp'],
  },
};

/**

*   Set the brightness and color temperature of a room light. (mock API)
*   @param {number} brightness - Light level from 0 to 100. Zero is off and 100 is full brightness
*   @param {string} color_temp - Color temperature of the light fixture, which can be `daylight`, `cool` or `warm`.
*   @return {Object} A dictionary containing the set brightness and color temperature.
*/
function setLightValues(brightness, color_temp) {
  return {
    brightness: brightness,
    colorTemperature: color_temp
  };
}
```

### Step 2: Call the model with function declarations

Once you have defined your function declarations, you can prompt the model to
use them. It analyzes the prompt and function declarations and decides whether
to respond directly or to call a function. If a function is called, the response
object will contain a function call suggestion.

PythonJavaScriptMore

```
from google.genai import types

# Configure the client and tools
client = genai.Client()
tools = types.Tool(function_declarations=[set_light_values_declaration])
config = types.GenerateContentConfig(tools=[tools])

# Define user prompt
contents = [\
    types.Content(\
        role="user", parts=[types.Part(text="Turn the lights down to a romantic level")]\
    )\
]

# Send request with function declarations
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=contents,
    config=config,
)

print(response.candidates[0].content.parts[0].function_call)
```

```
import { GoogleGenAI } from '@google/genai';

// Generation config with function declaration
const config = {
  tools: [{\
    functionDeclarations: [setLightValuesFunctionDeclaration]\
  }]
};

// Configure the client
const ai = new GoogleGenAI({});

// Define user prompt
const contents = [\
  {\
    role: 'user',\
    parts: [{ text: 'Turn the lights down to a romantic level' }]\
  }\
];

// Send request with function declarations
const response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(response.functionCalls[0]);
```

The model then returns a `functionCall` object in an OpenAPI compatible
schema specifying how to call one or more of the declared functions in order to
respond to the user's question.

PythonJavaScriptMore

```
id=None args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

```
{
  name: 'set_light_values',
  args: { brightness: 25, color_temp: 'warm' }
}
```

### Step 3: Execute set\_light\_values function code

Extract the function call details from the model's response, parse the arguments
, and execute the `set_light_values` function.

PythonJavaScriptMore

```
# Extract tool call details, it may not be in the first part.
tool_call = response.candidates[0].content.parts[0].function_call

if tool_call.name == "set_light_values":
    result = set_light_values(**tool_call.args)
    print(f"Function execution result: {result}")
```

```
// Extract tool call details
const tool_call = response.functionCalls[0]

let result;
if (tool_call.name === 'set_light_values') {
  result = setLightValues(tool_call.args.brightness, tool_call.args.color_temp);
  console.log(`Function execution result: ${JSON.stringify(result)}`);
}
```

### Step 4: Create user friendly response with function result and call the model again

Finally, send the result of the function execution back to the model so it can
incorporate this information into its final response to the user.

PythonJavaScriptMore

```
from google import genai
from google.genai import types

# Create a function response part
function_response_part = types.Part.from_function_response(
    name=tool_call.name,
    response={"result": result},
)

# Append function call and result of the function execution to contents
contents.append(response.candidates[0].content) # Append the content from the model's response.
contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response

client = genai.Client()
final_response = client.models.generate_content(
    model="gemini-3-flash-preview",
    config=config,
    contents=contents,
)

print(final_response.text)
```

```
// Create a function response part
const function_response_part = {
  name: tool_call.name,
  response: { result }
}

// Append function call and result of the function execution to contents
contents.push(response.candidates[0].content);
contents.push({ role: 'user', parts: [{ functionResponse: function_response_part }] });

// Get the final response from the model
const final_response = await ai.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: contents,
  config: config
});

console.log(final_response.text);
```

This completes the function calling flow. The model successfully used the
`set_light_values` function to perform the request action of the user.

## Function declarations

When you implement function calling in a prompt, you create a `tools` object,
which contains one or more `function declarations`. You define functions using
JSON, specifically with a [select subset](https://ai.google.dev/api/caching#Schema)
of the [OpenAPI schema](https://spec.openapis.org/oas/v3.0.3#schemaw) format. A
single function declaration can include the following parameters:

-   `name` (string): A unique name for the function (`get_weather_forecast`,
    `send_email`). Use descriptive names without spaces or special characters
    (use underscores or camelCase).
-   `description` (string): A clear and detailed explanation of the function's
    purpose and capabilities. This is crucial for the model to understand when
    to use the function. Be specific and provide examples if helpful ("Finds
    theaters based on location and optionally movie title which is currently
    playing in theaters.").
-   `parameters`(object): Defines the input parameters the function
    expects.

    -   `type` (string): Specifies the overall data type, such as `object`.
    -   `properties`(object): Lists individual parameters, each with:

        -   `type` (string): The data type of the parameter, such as `string`,
            `integer`, `boolean, array`.
        -   `description` (string): A description of the parameter's purpose and
            format. Provide examples and constraints ("The city and state,
            e.g., 'San Francisco, CA' or a zip code e.g., '95616'.").
        -   `enum` (array, optional): If the parameter values are from a fixed
            set, use "enum" to list the allowed values instead of just describing
            them in the description. This improves accuracy ("enum":
            \["daylight", "cool", "warm"\]).
    -   `required` (array): An array of strings listing the parameter names that
        are mandatory for the function to operate.

You can also construct `FunctionDeclarations` from Python functions directly using
`types.FunctionDeclaration.from_callable(client=client, callable=your_function)`.

## Function calling with thinking models

Gemini 3 and 2.5 series models use an internal ["thinking"](https://ai.google.dev/gemini-api/docs/thinking) process to reason through requests. This
significantly improves function calling performance,
allowing the model to better determine when to call a function and which
parameters to use. Because the Gemini API is stateless, models use
[thought signatures](https://ai.google.dev/gemini-api/docs/thought-signatures) to maintain context
across multi-turn conversations.

This section covers advanced management of thought signatures and is only
necessary if you're manually constructing API requests (e.g., via REST) or
manipulating conversation history.

**If you're using the [Google GenAI SDKs](https://ai.google.dev/gemini-api/docs/libraries) (our**
**official libraries), you don't need to manage this process**. The SDKs
automatically handle the necessary steps, as shown in the earlier
[example](https://ai.google.dev/gemini-api/docs/function-calling#step-4).

### Managing conversation history manually

If you modify the conversation history manually, instead of sending the
[complete previous response](https://ai.google.dev/gemini-api/docs/function-calling#step-4) you
must correctly handle the `thought_signature` included in the model's turn.

Follow these rules to ensure the model's context is preserved:

-   Always send the `thought_signature` back to the model inside its original
    [`Part`](https://ai.google.dev/api#request-body-structure).
-   Don't merge a `Part` containing a signature with one that does not. This
    breaks the positional context of the thought.
-   Don't combine two `Parts` that both contain signatures, as the signature
    strings cannot be merged.

#### Gemini 3 thought signatures

In Gemini 3, any [`Part`](https://ai.google.dev/api#request-body-structure) of a model response
may contain a thought signature.
While we generally recommend returning signatures from all `Part` types,
passing back thought signatures is mandatory for function calling. Unless you
are manipulating conversation history manually, the Google GenAI SDK will
handle thought signatures automatically.

If you are manipulating conversation history manually, refer to the
[Thoughts Signatures](https://ai.google.dev/gemini-api/docs/thought-signatures) page for complete
guidance and details on handling thought signatures for Gemini 3.

### Inspecting thought signatures

While not necessary for implementation, you can inspect the response to see the
`thought_signature` for debugging or educational purposes.

PythonJavaScriptMore

```
import base64
# After receiving a response from a model with thinking enabled
# response = client.models.generate_content(...)

# The signature is attached to the response part containing the function call
part = response.candidates[0].content.parts[0]
if part.thought_signature:
  print(base64.b64encode(part.thought_signature).decode("utf-8"))
```

```
// After receiving a response from a model with thinking enabled
// const response = await ai.models.generateContent(...)

// The signature is attached to the response part containing the function call
const part = response.candidates[0].content.parts[0];
if (part.thoughtSignature) {
  console.log(part.thoughtSignature);
}
```

Learn more about limitations and usage of thought signatures, and about thinking
models in general, on the [Thinking](https://ai.google.dev/gemini-api/docs/thinking#signatures) page.

## Parallel function calling

In addition to single turn function calling, you can also call multiple
functions at once. Parallel function calling lets you execute multiple functions
at once and is used when the functions are not dependent on each other. This is
useful in scenarios like gathering data from multiple independent sources, such
as retrieving customer details from different databases or checking inventory
levels across various warehouses or performing multiple actions such as
converting your apartment into a disco.

When the model initiates multiple function calls in a single turn, you don't need to return the `function_result` objects in the same order that the `function_call` objects were received. The Gemini API maps each result back to its corresponding call using the `tool_use_id` (which matches the `call_id` from the model's output). This lets you execute your functions asynchronously and append the results to your list as they complete.

PythonJavaScriptMore

```
power_disco_ball = {
    "name": "power_disco_ball",
    "description": "Powers the spinning disco ball.",
    "parameters": {
        "type": "object",
        "properties": {
            "power": {
                "type": "boolean",
                "description": "Whether to turn the disco ball on or off.",
            }
        },
        "required": ["power"],
    },
}

start_music = {
    "name": "start_music",
    "description": "Play some music matching the specified parameters.",
    "parameters": {
        "type": "object",
        "properties": {
            "energetic": {
                "type": "boolean",
                "description": "Whether the music is energetic or not.",
            },
            "loud": {
                "type": "boolean",
                "description": "Whether the music is loud or not.",
            },
        },
        "required": ["energetic", "loud"],
    },
}

dim_lights = {
    "name": "dim_lights",
    "description": "Dim the lights.",
    "parameters": {
        "type": "object",
        "properties": {
            "brightness": {
                "type": "number",
                "description": "The brightness of the lights, 0.0 is off, 1.0 is full.",
            }
        },
        "required": ["brightness"],
    },
}
```

```
import { Type } from '@google/genai';

const powerDiscoBall = {
  name: 'power_disco_ball',
  description: 'Powers the spinning disco ball.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      power: {
        type: Type.BOOLEAN,
        description: 'Whether to turn the disco ball on or off.'
      }
    },
    required: ['power']
  }
};

const startMusic = {
  name: 'start_music',
  description: 'Play some music matching the specified parameters.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      energetic: {
        type: Type.BOOLEAN,
        description: 'Whether the music is energetic or not.'
      },
      loud: {
        type: Type.BOOLEAN,
        description: 'Whether the music is loud or not.'
      }
    },
    required: ['energetic', 'loud']
  }
};

const dimLights = {
  name: 'dim_lights',
  description: 'Dim the lights.',
  parameters: {
    type: Type.NUMBER,
    description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
  }
};
```

Configure the function calling mode to allow using all of the specified tools.
To learn more, you can read about
[configuring function calling](https://ai.google.dev/gemini-api/docs/function-calling#function_calling_modes).

PythonJavaScriptMore

```
from google import genai
from google.genai import types

# Configure the client and tools
client = genai.Client()
house_tools = [\
    types.Tool(function_declarations=[power_disco_ball, start_music, dim_lights])\
]
config = types.GenerateContentConfig(
    tools=house_tools,
    automatic_function_calling=types.AutomaticFunctionCallingConfig(
        disable=True
    ),
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(
        function_calling_config=types.FunctionCallingConfig(mode='ANY')
    ),
)

chat = client.chats.create(model="gemini-3-flash-preview", config=config)
response = chat.send_message("Turn this place into a party!")

# Print out each of the function calls requested from this single call
print("Example 1: Forced function calling")
for fn in response.function_calls:
    args = ", ".join(f"{key}={val}" for key, val in fn.args.items())
    print(f"{fn.name}({args})")
```

```
import { GoogleGenAI } from '@google/genai';

// Set up function declarations
const houseFns = [powerDiscoBall, startMusic, dimLights];

const config = {
    tools: [{\
        functionDeclarations: houseFns\
    }],
    // Force the model to call 'any' function, instead of chatting.
    toolConfig: {
        functionCallingConfig: {
            mode: 'any'
        }
    }
};

// Configure the client
const ai = new GoogleGenAI({});

// Create a chat session
const chat = ai.chats.create({
    model: 'gemini-3-flash-preview',
    config: config
});
const response = await chat.sendMessage({message: 'Turn this place into a party!'});

// Print out each of the function calls requested from this single call
console.log("Example 1: Forced function calling");
for (const fn of response.functionCalls) {
    const args = Object.entries(fn.args)
        .map(([key, val]) => `${key}=${val}`)
        .join(', ');
    console.log(`${fn.name}(${args})`);
}
```

Each of the printed results reflects a single function call that the model has
requested. To send the results back, include the responses in the same order as
they were requested.

The Python SDK supports [automatic function calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only),
which automatically converts Python functions to declarations, handles the
function call execution and response cycle for you. Following is an example for
the disco use case.

PythonMore

```
from google import genai
from google.genai import types

# Actual function implementations
def power_disco_ball_impl(power: bool) -> dict:
    """Powers the spinning disco ball.

    Args:
        power: Whether to turn the disco ball on or off.

    Returns:
        A status dictionary indicating the current state.
    """
    return {"status": f"Disco ball powered {'on' if power else 'off'}"}

def start_music_impl(energetic: bool, loud: bool) -> dict:
    """Play some music matching the specified parameters.

    Args:
        energetic: Whether the music is energetic or not.
        loud: Whether the music is loud or not.

    Returns:
        A dictionary containing the music settings.
    """
    music_type = "energetic" if energetic else "chill"
    volume = "loud" if loud else "quiet"
    return {"music_type": music_type, "volume": volume}

def dim_lights_impl(brightness: float) -> dict:
    """Dim the lights.

    Args:
        brightness: The brightness of the lights, 0.0 is off, 1.0 is full.

    Returns:
        A dictionary containing the new brightness setting.
    """
    return {"brightness": brightness}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Do everything you need to this place into party!",
    config=config,
)

print("\nExample 2: Automatic function calling")
print(response.text)
# I've turned on the disco ball, started playing loud and energetic music, and dimmed the lights to 50% brightness. Let's get this party started!
```

## Compositional function calling

Compositional or sequential function calling allows Gemini to chain multiple
function calls together to fulfill a complex request. For example, to answer
"Get the temperature in my current location", the Gemini API might first invoke
a `get_current_location()` function followed by a `get_weather()` function that
takes the location as a parameter.

The following example demonstrates how to implement compositional function
calling using the Python SDK and automatic function calling.

PythonJavaScriptMore

This example uses the automatic function calling feature of the
`google-genai` Python SDK. The SDK automatically converts the Python
functions to the required schema, executes the function calls when requested
by the model, and sends the results back to the model to complete the task.

```
import os
from google import genai
from google.genai import types

# Example Functions
def get_weather_forecast(location: str) -> dict:
    """Gets the current weather temperature for a given location."""
    print(f"Tool Call: get_weather_forecast(location={location})")
    # TODO: Make API call
    print("Tool Response: {'temperature': 25, 'unit': 'celsius'}")
    return {"temperature": 25, "unit": "celsius"}  # Dummy response

def set_thermostat_temperature(temperature: int) -> dict:
    """Sets the thermostat to a desired temperature."""
    print(f"Tool Call: set_thermostat_temperature(temperature={temperature})")
    # TODO: Interact with a thermostat API
    print("Tool Response: {'status': 'success'}")
    return {"status": "success"}

# Configure the client and model
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_weather_forecast, set_thermostat_temperature]
)

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",
    config=config,
)

# Print the final, user-facing response
print(response.text)
```

**Expected Output**

When you run the code, you will see the SDK orchestrating the function
calls. The model first calls `get_weather_forecast`, receives the
temperature, and then calls `set_thermostat_temperature` with the correct
value based on the logic in the prompt.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. I've set the thermostat to 20°C.
```

This example shows how to use JavaScript/TypeScript SDK to do comopositional
function calling using a manual execution loop.

```
import { GoogleGenAI, Type } from "@google/genai";

// Configure the client
const ai = new GoogleGenAI({});

// Example Functions
function get_weather_forecast({ location }) {
  console.log(`Tool Call: get_weather_forecast(location=${location})`);
  // TODO: Make API call
  console.log("Tool Response: {'temperature': 25, 'unit': 'celsius'}");
  return { temperature: 25, unit: "celsius" };
}

function set_thermostat_temperature({ temperature }) {
  console.log(
    `Tool Call: set_thermostat_temperature(temperature=${temperature})`,
  );
  // TODO: Make API call
  console.log("Tool Response: {'status': 'success'}");
  return { status: "success" };
}

const toolFunctions = {
  get_weather_forecast,
  set_thermostat_temperature,
};

const tools = [\
  {\
    functionDeclarations: [\
      {\
        name: "get_weather_forecast",\
        description:\
          "Gets the current weather temperature for a given location.",\
        parameters: {\
          type: Type.OBJECT,\
          properties: {\
            location: {\
              type: Type.STRING,\
            },\
          },\
          required: ["location"],\
        },\
      },\
      {\
        name: "set_thermostat_temperature",\
        description: "Sets the thermostat to a desired temperature.",\
        parameters: {\
          type: Type.OBJECT,\
          properties: {\
            temperature: {\
              type: Type.NUMBER,\
            },\
          },\
          required: ["temperature"],\
        },\
      },\
    ],\
  },\
];

// Prompt for the model
let contents = [\
  {\
    role: "user",\
    parts: [\
      {\
        text: "If it's warmer than 20°C in London, set the thermostat to 20°C, otherwise set it to 18°C.",\
      },\
    ],\
  },\
];

// Loop until the model has no more function calls to make
while (true) {
  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents,
    config: { tools },
  });

  if (result.functionCalls && result.functionCalls.length > 0) {
    const functionCall = result.functionCalls[0];

    const { name, args } = functionCall;

    if (!toolFunctions[name]) {
      throw new Error(`Unknown function call: ${name}`);
    }

    // Call the function and get the response.
    const toolResponse = toolFunctions[name](args);

    const functionResponsePart = {
      name: functionCall.name,
      response: {
        result: toolResponse,
      },
    };

    // Send the function response back to the model.
    contents.push({
      role: "model",
      parts: [\
        {\
          functionCall: functionCall,\
        },\
      ],
    });
    contents.push({
      role: "user",
      parts: [\
        {\
          functionResponse: functionResponsePart,\
        },\
      ],
    });
  } else {
    // No more function calls, break the loop.
    console.log(result.text);
    break;
  }
}
```

**Expected Output**

When you run the code, you will see the SDK orchestrating the function
calls. The model first calls `get_weather_forecast`, receives the
temperature, and then calls `set_thermostat_temperature` with the correct
value based on the logic in the prompt.

```
Tool Call: get_weather_forecast(location=London)
Tool Response: {'temperature': 25, 'unit': 'celsius'}
Tool Call: set_thermostat_temperature(temperature=20)
Tool Response: {'status': 'success'}
OK. It's 25°C in London, so I've set the thermostat to 20°C.
```

Compositional function calling is a native [Live\\
API](https://ai.google.dev/gemini-api/docs/live) feature. This means Live API
can handle the function calling similar to the Python SDK.

PythonJavaScriptMore

```
# Light control schemas
turn_on_the_lights_schema = {'name': 'turn_on_the_lights'}
turn_off_the_lights_schema = {'name': 'turn_off_the_lights'}

prompt = """
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
  """

tools = [\
    {'code_execution': {}},\
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]}\
]

await run(prompt, tools=tools, modality="AUDIO")
```

```
// Light control schemas
const turnOnTheLightsSchema = { name: 'turn_on_the_lights' };
const turnOffTheLightsSchema = { name: 'turn_off_the_lights' };

const prompt = `
  Hey, can you write run some python code to turn on the lights, wait 10s and then turn off the lights?
`;

const tools = [\
  { codeExecution: {} },\
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] } // not defined here.\
];

await run(prompt, tools=tools, modality="AUDIO")
```

## Function calling modes

The Gemini API lets you control how the model uses the provided tools
(function declarations). Specifically, you can set the mode within
the.`function_calling_config`.

-   `AUTO (Default)`: The model decides whether to generate a natural language
    response or suggest a function call based on the prompt and context. This is the
    most flexible mode and recommended for most scenarios.
-   `ANY`: The model is constrained to always predict a function call and
    guarantees function schema adherence. If `allowed_function_names` is not
    specified, the model can choose from any of the provided function declarations.
    If `allowed_function_names` is provided as a list, the model can only choose
    from the functions in that list. Use this mode when you require a function
    call response to every prompt (if applicable).
-   `NONE`: The model is _prohibited_ from making function calls. This is
    equivalent to sending a request without any function declarations. Use this to
    temporarily disable function calling without removing your tool definitions.
-   `VALIDATED` (Preview): The model is constrained to predict either function
    calls or natural language, and ensures function schema adherence. If
    `allowed_function_names` is not provided, the model picks from all of the
    available function declarations. If `allowed_function_names` is provided, the
    model picks from the set of allowed functions.

PythonJavaScriptMore

```
from google.genai import types

# Configure function calling mode
tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY", allowed_function_names=["get_current_temperature"]
    )
)

# Create the generation config
config = types.GenerateContentConfig(
    tools=[tools],  # not defined here.
    tool_config=tool_config,
)
```

```
import { FunctionCallingConfigMode } from '@google/genai';

// Configure function calling mode
const toolConfig = {
  functionCallingConfig: {
    mode: FunctionCallingConfigMode.ANY,
    allowedFunctionNames: ['get_current_temperature']
  }
};

// Create the generation config
const config = {
  tools: tools, // not defined here.
  toolConfig: toolConfig,
};
```

## Automatic function calling (Python only)

When using the Python SDK, you can provide Python functions directly as tools.
The SDK converts these functions into declarations, manages the function call
execution, and handles the response cycle for you. Define your function with
type hints and a docstring. For optimal results, it is recommended to use
[Google-style docstrings.](https://google.github.io/styleguide/pyguide.html#383-functions-and-methods)
The SDK will then automatically:

1.  Detect function call responses from the model.
2.  Call the corresponding Python function in your code.
3.  Send the function's response back to the model.
4.  Return the model's final text response.

The SDK currently doesn't parse argument descriptions into the property
description slots of the generated function declaration. Instead, it sends the
entire docstring as the top-level function description.

PythonMore

```
from google import genai
from google.genai import types

# Define the function with type hints and docstring
def get_current_temperature(location: str) -> dict:
    """Gets the current temperature for a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA

    Returns:
        A dictionary containing the temperature and unit.
    """
    # ... (implementation) ...
    return {"temperature": 25, "unit": "Celsius"}

# Configure the client
client = genai.Client()
config = types.GenerateContentConfig(
    tools=[get_current_temperature]
)  # Pass the function itself

# Make the request
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What's the temperature in Boston?",
    config=config,
)

print(response.text)  # The SDK handles the function call and returns the final text
```

You can disable automatic function calling with:

PythonMore

```
config = types.GenerateContentConfig(
    tools=[get_current_temperature],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
```

### Automatic function schema declaration

The API is able to describe any of the following types. `Pydantic` types are
allowed, as long as the fields defined on them are also composed of allowed
types. Dict types (like `dict[str: int]`) are not well supported here, don't
use them.

PythonMore

```
AllowedType = (
  int | float | bool | str | list['AllowedType'] | pydantic.BaseModel)
```

To see what the inferred schema looks like, you can convert it using
[`from_callable`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration.from_callable):

PythonMore

```
from google import genai
from google.genai import types

def multiply(a: float, b: float):
    """Returns a * b."""
    return a * b

client = genai.Client()
fn_decl = types.FunctionDeclaration.from_callable(callable=multiply, client=client)

# to_json_dict() provides a clean JSON representation.
print(fn_decl.to_json_dict())
```

## Multi-tool use: Combine native tools with function calling

You can enable multiple tools combining native tools with
function calling at the same time. Here's an example that enables two tools,
[Grounding with Google Search](https://ai.google.dev/gemini-api/docs/grounding) and
[code execution](https://ai.google.dev/gemini-api/docs/code-execution), in a request using the
[Live API](https://ai.google.dev/gemini-api/docs/live).

PythonJavaScriptMore

```
# Multiple tasks example - combining lights, code execution, and search
prompt = """
  Hey, I need you to do three things for me.

    1.  Turn on the lights.
    2.  Then compute the largest prime palindrome under 100000.
    3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

  Thanks!
  """

tools = [\
    {'google_search': {}},\
    {'code_execution': {}},\
    {'function_declarations': [turn_on_the_lights_schema, turn_off_the_lights_schema]} # not defined here.\
]

# Execute the prompt with specified tools in audio modality
await run(prompt, tools=tools, modality="AUDIO")
```

```
// Multiple tasks example - combining lights, code execution, and search
const prompt = `
  Hey, I need you to do three things for me.

    1.  Turn on the lights.
    2.  Then compute the largest prime palindrome under 100000.
    3.  Then use Google Search to look up information about the largest earthquake in California the week of Dec 5 2024.

  Thanks!
`;

const tools = [\
  { googleSearch: {} },\
  { codeExecution: {} },\
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] } // not defined here.\
];

// Execute the prompt with specified tools in audio modality
await run(prompt, {tools: tools, modality: "AUDIO"});
```

Python developers can try this out in the [Live API Tool Use\\
notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_LiveAPI_tools.ipynb).

## Multimodal function responses

For Gemini 3 series models, you can include multimodal content in
the function response parts that you send to the model. The model can process
this multimodal content in its next turn to produce a more informed response.
The following MIME types are supported for multimodal content in function
responses:

-   **Images**: `image/png`, `image/jpeg`, `image/webp`
-   **Documents**: `application/pdf`, `text/plain`

To include multimodal data in a function response, include it as one or more
parts nested within the `functionResponse` part. Each multimodal part must
contain `inlineData`. If you reference a multimodal part from
within the structured `response` field, it must contain a unique `displayName`.

You can also reference a multimodal part from within the structured `response`
field of the `functionResponse` part by using the JSON reference format
`{"$ref": "<displayName>"}`. The model substitutes the reference with the
multimodal content when processing the response. Each `displayName` can only be
referenced once in the structured `response` field.

The following example shows a message containing a `functionResponse` for a
function named `get_image` and a nested part containing image data with
`displayName: "instrument.jpg"`. The `functionResponse`'s `response` field
references this image part:

PythonJavaScriptRESTMore

```
from google import genai
from google.genai import types

import requests

client = genai.Client()

# This is a manual, two turn multimodal function calling workflow:

# 1. Define the function tool
get_image_declaration = types.FunctionDeclaration(
  name="get_image",
  description="Retrieves the image file reference for a specific order item.",
  parameters={
      "type": "object",
      "properties": {
          "item_name": {
              "type": "string",
              "description": "The name or description of the item ordered (e.g., 'instrument')."
          }
      },
      "required": ["item_name"],
  },
)
tool_config = types.Tool(function_declarations=[get_image_declaration])

# 2. Send a message that triggers the tool
prompt = "Show me the instrument I ordered last month."
response_1 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=[prompt],
  config=types.GenerateContentConfig(
      tools=[tool_config],
  )
)

# 3. Handle the function call
function_call = response_1.function_calls[0]
requested_item = function_call.args["item_name"]
print(f"Model wants to call: {function_call.name}")

# Execute your tool (e.g., call an API)
# (This is a mock response for the example)
print(f"Calling external tool for: {requested_item}")

function_response_data = {
  "image_ref": {"$ref": "instrument.jpg"},
}
image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
function_response_multimodal_data = types.FunctionResponsePart(
  inline_data=types.FunctionResponseBlob(
    mime_type="image/jpeg",
    display_name="instrument.jpg",
    data=image_bytes,
  )
)

# 4. Send the tool's result back
# Append this turn's messages to history for a final response.
history = [\
  types.Content(role="user", parts=[types.Part(text=prompt)]),\
  response_1.candidates[0].content,\
  types.Content(\
    role="user",\
    parts=[\
        types.Part.from_function_response(\
          name=function_call.name,\
          response=function_response_data,\
          parts=[function_response_multimodal_data]\
        )\
    ],\
  )\
]

response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=history,
  config=types.GenerateContentConfig(
      tools=[tool_config],
      thinking_config=types.ThinkingConfig(include_thoughts=True)
  ),
)

print(f"\nFinal model response: {response_2.text}")
```

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY });

// This is a manual, two turn multimodal function calling workflow:
// 1. Define the function tool
const getImageDeclaration = {
  name: 'get_image',
  description: 'Retrieves the image file reference for a specific order item.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      item_name: {
        type: Type.STRING,
        description: "The name or description of the item ordered (e.g., 'instrument').",
      },
    },
    required: ['item_name'],
  },
};

const toolConfig = {
  functionDeclarations: [getImageDeclaration],
};

// 2. Send a message that triggers the tool
const prompt = 'Show me the instrument I ordered last month.';
const response1 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: prompt,
  config: {
    tools: [toolConfig],
  },
});

// 3. Handle the function call
const functionCall = response1.functionCalls[0];
const requestedItem = functionCall.args.item_name;
console.log(`Model wants to call: ${functionCall.name}`);

// Execute your tool (e.g., call an API)
// (This is a mock response for the example)
console.log(`Calling external tool for: ${requestedItem}`);

const functionResponseData = {
  image_ref: { $ref: 'instrument.jpg' },
};

const imageUrl = "https://goo.gle/instrument-img";
const response = await fetch(imageUrl);
const imageArrayBuffer = await response.arrayBuffer();
const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

const functionResponseMultimodalData = {
  inlineData: {
    mimeType: 'image/jpeg',
    displayName: 'instrument.jpg',
    data: base64ImageData,
  },
};

// 4. Send the tool's result back
// Append this turn's messages to history for a final response.
const history = [\
  { role: 'user', parts: [{ text: prompt }] },\
  response1.candidates[0].content,\
  {\
    role: 'tool',\
    parts: [\
      {\
        functionResponse: {\
          name: functionCall.name,\
          response: functionResponseData,\
          parts: [functionResponseMultimodalData],\
        },\
      },\
    ],\
  },\
];

const response2 = await client.models.generateContent({
  model: 'gemini-3-flash-preview',
  contents: history,
  config: {
    tools: [toolConfig],
    thinkingConfig: { includeThoughts: true },
  },
});

console.log(`\nFinal model response: ${response2.text}`);
```

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -X POST \
  -d '{
    "contents": [\
      ...,\
      {\
        "role": "user",\
        "parts": [\
        {\
            "functionResponse": {\
              "name": "get_image",\
              "response": {\
                "image_ref": {\
                  "$ref": "instrument.jpg"\
                }\
              },\
              "parts": [\
                {\
                  "inlineData": {\
                    "displayName": "instrument.jpg",\
                    "mimeType":"'"$MIME_TYPE"'",\
                    "data": "'"$IMAGE_B64"'"\
                  }\
                }\
              ]\
            }\
          }\
        ]\
      }\
    ]
  }'
```

## Function calling with Structured output

For Gemini 3 series models, you can use function calling with [structured output](https://ai.google.dev/gemini-api/docs/structured-output). This lets the model predict function calls or outputs that adhere to a specific schema. As a result, you receive consistently formatted responses when the model doesn't generate function calls.

## Model context protocol (MCP)

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/introduction) is
an open standard for connecting AI applications with external tools and data.
MCP provides a common protocol for models to access context, such as functions
(tools), data sources (resources), or predefined prompts.

The Gemini SDKs have built-in support for the MCP, reducing boilerplate code and
offering
[automatic tool calling](https://ai.google.dev/gemini-api/docs/function-calling#automatic_function_calling_python_only)
for MCP tools. When the model generates an MCP tool call, the Python and
JavaScript client SDK can automatically execute the MCP tool and send the
response back to the model in a subsequent request, continuing this loop until
no more tool calls are made by the model.

Here, you can find an example of how to use a local MCP server with Gemini and
`mcp` SDK.

PythonJavaScriptMore

Make sure the latest version of the
[`mcp` SDK](https://modelcontextprotocol.io/introduction) is installed on
your platform of choice.

```
pip install mcp
```

```
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from google import genai

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=genai.types.GenerateContentConfig(
                    temperature=0,
                    tools=[session],  # uses the session, will automatically call the tool
                    # Uncomment if you **don't** want the SDK to automatically call the tool
                    # automatic_function_calling=genai.types.AutomaticFunctionCallingConfig(
                    #     disable=True
                    # ),
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```

Make sure the latest version of the `mcp` SDK is installed on your platform
of choice.

```
npm install @modelcontextprotocol/sdk
```

```
import { GoogleGenAI, FunctionCallingConfigMode , mcpToTool} from '@google/genai';
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Create server parameters for stdio connection
const serverParams = new StdioClientTransport({
  command: "npx", // Executable
  args: ["-y", "@philschmid/weather-mcp"] // MCP Server
});

const client = new Client(
  {
    name: "example-client",
    version: "1.0.0"
  }
);

// Configure the client
const ai = new GoogleGenAI({});

// Initialize the connection between client and server
await client.connect(serverParams);

// Send request to the model with MCP tools
const response = await ai.models.generateContent({
  model: "gemini-2.5-flash",
  contents: `What is the weather in London in ${new Date().toLocaleDateString()}?`,
  config: {
    tools: [mcpToTool(client)],  // uses the session, will automatically call the tool
    // Uncomment if you **don't** want the sdk to automatically call the tool
    // automaticFunctionCalling: {
    //   disable: true,
    // },
  },
});
console.log(response.text)

// Close the connection
await client.close();
```

### Limitations with built-in MCP support

Built-in MCP support is a [experimental](https://ai.google.dev/gemini-api/docs/models#preview)
feature in our SDKs and has the following limitations:

-   Only tools are supported, not resources nor prompts
-   It is available for the Python and JavaScript/TypeScript SDK.
-   Breaking changes might occur in future releases.

Manual integration of MCP servers is always an option if these limit what you're
building.

## Supported models

This section lists models and their function calling capabilities. Experimental
models are not included. You can find a comprehensive capabilities overview on
the [model overview](https://ai.google.dev/gemini-api/docs/models) page.

| Model | Function Calling | Parallel Function Calling | Compositional Function Calling |
| :--- | :--- | :--- | :--- |
| Gemini 3.1 Pro Preview | ✔️ | ✔️ | ✔️ |
| Gemini 3 Flash Preview | ✔️ | ✔️ | ✔️ |
| Gemini 2.5 Pro | ✔️ | ✔️ | ✔️ |
| Gemini 2.5 Flash | ✔️ | ✔️ | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ | ✔️ | ✔️ |
| Gemini 2.0 Flash | ✔️ | ✔️ | ✔️ |
| Gemini 2.0 Flash-Lite | X | X | X |

## Best practices

-   **Function and Parameter Descriptions:** Be extremely clear and specific in
    your descriptions. The model relies on these to choose the correct function
    and provide appropriate arguments.
-   **Naming:** Use descriptive function names (without spaces, periods, or
    dashes).
-   **Strong Typing:** Use specific types (integer, string, enum) for parameters
    to reduce errors. If a parameter has a limited set of valid values, use an
    enum.
-   **Tool Selection:** While the model can use an arbitrary number of tools,
    providing too many can increase the risk of selecting an incorrect or
    suboptimal tool. For best results, aim to provide only the relevant tools
    for the context or task, ideally keeping the active set to a maximum of
    10-20. Consider dynamic tool selection based on conversation context if you
    have a large total number of tools.
-   **Prompt Engineering:**
    -   Provide context: Tell the model its role (e.g., "You are a helpful
        weather assistant.").
    -   Give instructions: Specify how and when to use functions (e.g., "Don't
        guess dates; always use a future date for forecasts.").
    -   Encourage clarification: Instruct the model to ask clarifying questions
        if needed.
    -   See [Agentic workflows](https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-workflows)
        for further strategies on designing these prompts. Here is an example of a tested
        [system instruction](https://ai.google.dev/gemini-api/docs/prompting-strategies#agentic-si-template).
-   **Temperature:** Use a low temperature (e.g., 0) for more deterministic and
    reliable function calls.
-   **Validation:** If a function call has significant consequences (e.g.,
    placing an order), validate the call with the user before executing it.
-   **Check Finish Reason:** Always check the [`finishReason`](https://ai.google.dev/api/generate-content#FinishReason)
    in the model's response to handle cases where the model failed to generate a
    valid function call.
-   **Error Handling**: Implement robust error handling in your functions to
    gracefully handle unexpected inputs or API failures. Return informative
    error messages that the model can use to generate helpful responses to the
    user.
-   **Security:** Be mindful of security when calling external APIs. Use
    appropriate authentication and authorization mechanisms. Avoid exposing
    sensitive data in function calls.
-   **Token Limits:** Function descriptions and parameters count towards your
    input token limit. If you're hitting token limits, consider limiting the
    number of functions or the length of the descriptions, break down complex
    tasks into smaller, more focused function sets.
-   **Mix of bash and custom tools** For those building with a mix of bash and custom tools, Gemini 3.1 Pro Preview
    comes with a separate endpoint available via the API called
    [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview#gemini-31-pro-preview-customtools).

## Notes and limitations

-   Only a [subset of the OpenAPI\\
    schema](https://ai.google.dev/api/caching#FunctionDeclaration) is supported.
-   For `ANY` mode, the API may reject very large or deeply nested schemas. If you encounter errors, try simplifying your function parameter and response schemas by shortening property names, reducing nesting, or limiting the number of function declarations.
-   Supported parameter types in Python are limited.
-   Automatic function calling is a Python SDK feature only.

</details>
