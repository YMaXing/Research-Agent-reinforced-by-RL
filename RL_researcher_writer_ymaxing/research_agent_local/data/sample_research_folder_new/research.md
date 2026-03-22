# Research

## Research Results

<details>
<summary>Why do AI agents and large language models need external tools and function calling to handle complex real-world tasks?</summary>

### Source [5]: https://thenewstack.io/ai-agents-key-concepts-and-how-they-overcome-llm-limitations/

Query: Why do AI agents and large language models need external tools and function calling to handle complex real-world tasks?

Answer: Agents augment LLMs by integrating tools like web browsing and code execution to combine real-world data with complex calculations, analyzed by the LLM. Agents bridge traditional software tools and LLMs, overcoming limitations such as statelessness (no memory), synchronous processing, hallucinations, no internet access, poor math skills, and non-deterministic outputs. Agents add memory for context retention, asynchronous/parallel processing, fact-checking via real-time data access, specialized math engines, consistent output formatting, enhancing reliability for complex tasks. LLMs are limited to trained data without real-time access or action performance; agents connect them to external services needed to complete tasks.

-----

</details>

<details>
<summary>What are real-world applications, case studies, and best practices for building tool-calling AI agents?</summary>

### Source [15]: https://www.oracle.com/artificial-intelligence/ai-agents/ai-agent-use-cases/

Query: What are real-world applications, case studies, and best practices for building tool-calling AI agents?

Answer: Real-world AI agent use cases: Healthcare (clinical assistants draft notes, disease ID, scheduling, drug discovery). HR (job postings, interview scheduling, onboarding, benefits explanation, retention analysis). Manufacturing (maintenance estimates from photos, delivery optimization, sales guidance, supply chain risk). Finance (KYC, anti-money laundering, trading, credit underwriting). Customer support (ticket triage, returns, tracking, resolutions). Oracle AI Agent Studio for Fusion Apps provides templates for autonomous agents in Cloud Applications, customizing functions, limits, data access; 50+ agents rolling out at no extra cost. Agents automate multistep workflows using LLMs for natural language, accessing multiple systems.

-----

</details>

<details>
<summary>What are common challenges, limitations, and advanced techniques in implementing function calling with LLMs?</summary>

### Source [20]: https://martinfowler.com/articles/function-call-LLM.html

Query: What are common challenges, limitations, and advanced techniques in implementing function calling with LLMs?

Answer: Function calling using LLMs introduces new risks—especially when user input can ultimately trigger sensitive functions or APIs. Challenges include adversarial behavior where users try to bypass safeguards via prompt injections, such as revealing system prompts to manipulate actions like unauthorized refunds or exposing sensitive data. Restricting the agent’s action space using explicit conditional logic is essential to avoid security risks like unauthorized code execution from dynamic invocation. Guardrails against prompt injections: sanitize user input with regular expressions, input denylisting, or LLM-based validation for manipulation detection. Limitations in traditional rules engines that function calling might replace: complexity over time with growing rules leading to unintended interactions, hard to test and maintain. LLM-based systems offer context-aware behavior but lack full transparency or determinism. Different LLM providers have unique approaches (e.g., OpenAI JSON-based, Anthropic structured prompts), requiring frameworks like LangChain for abstraction. MCP enables dynamic tool discovery but adds complexity and security considerations for scaling agents. Prudent to start with low-risk operations and extend gradually as safety mechanisms mature.

-----

-----

### Source [21]: https://aclanthology.org/2025.coling-main.39.pdf

Query: What are common challenges, limitations, and advanced techniques in implementing function calling with LLMs?

Answer: The Dark Side of Function Calling: Pathways to Jailbreaking Large Language Models. Function calling vulnerabilities: alignment discrepancies where function arguments are less aligned with safety standards than chat mode; user coercion forcing execution of harmful functions via modes like 'function' or 'tool'; absence of rigorous safety filters in function calling. Jailbreak function attack exploits these, achieving over 90% success rate on models like GPT-4o, Claude-3.5-Sonnet, Gemini-1.5-pro by designing a 'WriteNovel' function inducing harmful content in arguments. Reasons: lack of alignment training for function calls (ASR drops significantly in chat mode); incapability to refuse execution in forced modes (ASR drops in auto mode); overlooked safety filtering. Defensive strategies: restrict user permissions to auto mode; align function calls with safety training; configure safety filters; incorporate defensive prompts (e.g., 'check security before executing, return ‘I’m sorry’ if harmful') inserted in function description most effective, reducing ASR to 0% on several models. Limitations: narrow testing scope on single jailbreak function; need robust defenses against evolving attacks.

-----

-----

### Source [22]: https://www.promptingguide.ai/applications/function_calling

Query: What are common challenges, limitations, and advanced techniques in implementing function calling with LLMs?

Answer: Function Calling with LLMs: LLMs like GPT-4 fine-tuned to detect function needs and output JSON arguments, but requires careful prompting (e.g., one-shot/few-shot) for accuracy. Challenges implied in reliable connection to external tools, converting natural language to structured API calls. Use cases highlight limitations: complex conversational agents need external APIs/knowledge bases; math solving requires multi-step custom functions; information extraction from text. OpenAI API modes (auto, required, function, none) affect behavior—forced modes risk coercion. Open-source LLMs support noted as developing. References indicate benchmarking needed for agent tool use quality across models.

-----

</details>

<details>
<summary>How is tool calling and AI agent technology expected to evolve in the future, with implications for developers?</summary>

### Source [23]: https://a16z.com/a-deep-dive-into-mcp-and-the-future-of-ai-tooling/

Query: How is tool calling and AI agent technology expected to evolve in the future, with implications for developers?

Answer: Tool calling and AI agent technology is evolving toward the Model Context Protocol (MCP), an open protocol introduced in November 2024 that standardizes how AI models interact with external tools, data, and APIs, enabling agent-centric execution, autonomous workflows, and human-in-the-loop capabilities. MCP draws from LSP but supports proactive agent decisions on tool usage, order, and chaining. Current use cases include dev-centric workflows (e.g., Postgres MCP server for SQL in IDEs, Browsertools for debugging) and net-new experiences (e.g., Slack, email, image generation via MCP servers in Cursor or Claude Desktop). Future developments include hosting/multi-tenancy for SaaS, standardized authentication/authorization (OAuth 2.1), gateways for traffic management, server discoverability via registries/marketplaces (Mintlify mcpt, Smithery), execution environments for multi-step workflows, standard client experiences, and debugging tools. Implications for developers: Competitive advantage shifts from API design to agent-optimized tools that are discoverable and granular; new pricing models based on agent preferences (speed/cost/relevance); documentation becomes machine-readable infrastructure (llms.txt); tools as higher abstractions (e.g., draft_email_and_send over send_email); scenario-centric MCP server design; new hosting modes for multi-step workloads with resumability/retries. Developers must adapt to MCP standards, build discoverable tools, focus on agent usability, and address unsolved challenges like auth and multi-tenancy to unlock ecosystems.

-----

-----

### Source [24]: https://arxiv.org/html/2503.12687v1

Query: How is tool calling and AI agent technology expected to evolve in the future, with implications for developers?

Answer: AI agent technology evolves from LLM-based agents augmenting reasoning with modules for memory, planning, tool use, and environmental interaction. Tool use frameworks standardize interfaces for invoking APIs, databases, and services, enabling agents to retrieve real-time data, perform computations, and act beyond language generation (e.g., IBM: tool calling for up-to-date info, workflow optimization, subtasks; Microsoft: secure access to programs). Future research trends include advanced reasoning (neuro-symbolic hybrids), long-term memory/context management (hierarchical/episodic), multi-agent coordination (hierarchical/market-based), human-agent collaboration, continual learning, multimodal capabilities, enhanced tool use/discovery, safety/alignment, efficiency optimization, and comprehensive evaluation. Long-term vision: seamless human-agent collaboration, autonomous problem-solving, collective intelligence, personalized lifelong learning, augmented creativity. Implications for developers: Need robust architectures integrating perception, knowledge representation, reasoning, action, learning; hybrid implementations (rule-based, statistical, neural); memory/context management; evaluation balancing accuracy/cost/robustness; address challenges like reasoning limits, tool integration, generalization, reliability, efficiency, multimodal/temporal reasoning, scalability; ethical considerations (privacy, bias, safety); focus on agent-ready enterprises with APIs, governance, strategy for ROI.

-----

-----

### Source [26]: https://www.ibm.com/think/insights/ai-agents-2025-expectations-vs-reality

Query: How is tool calling and AI agent technology expected to evolve in the future, with implications for developers?

Answer: AI agents evolve from rudimentary planning/tool-calling on LLMs to more autonomous entities with reasoning, planning, execution via better models (faster/smaller, COT training, larger contexts, function calling). 2025: year of agent exploration (99% enterprises experimenting), but not fully autonomous for complex tasks; orchestration for multi-agent networks with compliance; augment humans via HITL. Challenges: enterprise readiness (APIs), governance/transparency/traceability, ROI focus. Realistic: simple use cases viable, sophisticated maturing; back-and-forth single vs multi-agent; humans oversee. Implications for developers: Build agent-ready orgs (expose APIs, organize data); empower employees for optimal use; strong governance (audit/rollback); strategy for economic value/scaling; open source enables agent marketplaces.

-----

</details>

<details>
<summary>How do major AI providers like OpenAI, Google Gemini, and Anthropic implement and differ in their function calling or tool use APIs?</summary>

### Source [29]: https://ai.google.dev/gemini-api/docs/function-calling

Query: How do major AI providers like OpenAI, Google Gemini, and Anthropic implement and differ in their function calling or tool use APIs?

Answer: The Gemini API implements function calling to connect models to external tools and APIs, allowing the model to determine when to call specific functions and provide parameters for real-world actions. Key features include: structured interaction where the app sends function declarations, the model responds with functionCall objects (with unique id, name, args), the app executes the function, and sends back functionResponse with the id for mapping. Supports parallel function calling (multiple functions in one turn), compositional/sequential calling (chaining functions), and multi-tool use (combining built-in tools like Google Search with custom functions). Function declarations use OpenAPI schema subset (name, description, parameters with type object/properties/required/enum). Python SDK offers automatic function calling (pass Python functions directly, SDK handles conversion/execution), from_callable for schema generation. Modes: AUTO (default, model decides), ANY (call any), NONE (no calls), VALIDATED (strict schema adherence). Supports multimodal function responses (images/PDFs in responses via inlineData with displayName). Gemini 3/2.5 models use internal thinking for better reasoning, with thought signatures for context. Best practices: low temperature, validate calls, check finishReason, error handling. Supported models: Gemini 3.1 Pro/Flash Preview, 2.5 Pro/Flash/Lite/Flash-Lite, 2.0 Flash (full support varies). Limitations: functionCall not toolCall, no toolResponse.

-----

-----

### Source [30]: https://ai.google.dev/gemini-api/docs/openai

Query: How do major AI providers like OpenAI, Google Gemini, and Anthropic implement and differ in their function calling or tool use APIs?

Answer: Gemini API provides OpenAI compatibility for function calling via OpenAI libraries (Python/JS) and REST, using base_url 'https://generativelanguage.googleapis.com/v1beta/openai/'. Tools defined as OpenAI-style function objects (type:function, function:{name,description,parameters}). Example: client.chat.completions.create with tools=[{type:'function', function:{name:'get_weather', parameters:{...}}}], tool_choice='auto'. Supports streaming, image/audio understanding, structured output (Pydantic/zod), embeddings (gemini-embedding-2-preview/001), batch API, extra_body for Gemini-specific like thinking_config/cached_content. reasoning_effort maps to Gemini thinking levels (minimal/low/medium/high). Differences: uses Gemini models (e.g., gemini-3-flash-preview), native multimodal (image_url/input_audio), no full Assistants API parity.

-----

</details>

<details>
<summary>What are effective prompting strategies and best practices for ensuring reliable and accurate function calling in large language models?</summary>

### Source [40]: https://martinfowler.com/articles/function-call-LLM.html

Query: What are effective prompting strategies and best practices for ensuring reliable and accurate function calling in large language models?

Answer: Effective prompting strategies for reliable function calling in LLMs include using a clear system prompt that defines the agent's role (e.g., shopping assistant) and specifies available functions with their purposes and when to use them, such as 'search_products' for finding products, 'get_product_details' for specific product info, and 'clarify_request' for unclear requests. Provide detailed function schemas in the API call with name, description, parameters (type, properties, required fields), helping the LLM understand structure and usage. Enhance with one-shot prompting (single example of user message and action) or few-shot prompting (multiple examples covering scenarios) to improve accuracy and reliability. Restrict the agent's action space with explicit conditional logic to prevent security risks like prompt injections. Include conversation history for context-aware decisions. Use libraries like Instructor to reduce boilerplate by auto-serializing Pydantic models into OpenAI schemas. Implement guardrails like input sanitization with denylists or LLM-based validation against malicious intents (e.g., 'ignore previous instructions'). Define action classes to execute LLM decisions safely.

-----

-----

### Source [41]: https://arxiv.org/html/2412.01130v1

Query: What are effective prompting strategies and best practices for ensuring reliable and accurate function calling in large language models?

Answer: Prompt formats for function calling: Use ChatML with dedicated 'tools' role for JSON function descriptions or embed in system role with instructions. Blend function-calling data with instruction-following data (e.g., IF-110k + FC-110k) to improve accuracy (AST Summary) and relevance detection; instruction data enhances semantic understanding and provides non-function-call examples. Introduce Decision Token (<|answer|> or <|use_tool|>) for conditional prompts to boost relevance detection by forcing early classification, enabling synthetic non-function-call data generation. Leverage chain-of-thought (CoT) reasoning via synthetic data pipeline generating reasoning from conversation-function sequences with few-shot examples. For multilingual, use tailored translation pipeline preserving function names/descriptions, translating arguments reasonably. Fine-tune with LoRA on Breeze-7B base; dedicated tools role aids relevance detection. Results: Instruction data boosts function-calling; Decision Token + NF data improves detection; translation enhances non-English performance.

-----

-----

### Source [44]: https://www.promptingguide.ai/applications/function_calling

Query: What are effective prompting strategies and best practices for ensuring reliable and accurate function calling in large language models?

Answer: Define tools with JSON schema: name, description, parameters (type/object/properties/required/enum) for API integration, info extraction, math, agents. LLM detects need, outputs JSON args (e.g., get_current_weather(location, unit)). Pass tools in API request; model generates tool_calls with args. Combine with external APIs (e.g., weather), feed results back for final response. Use cases: Conversational agents (QA via tools), NLU (structured JSON), math solving, API calls, extraction (news/references). Supports multiple tools; fine-tuned for reliable detection/JSON output.

-----

</details>

<details>
<summary>What are proven methods and benchmarks for evaluating, testing, and monitoring the accuracy and safety of tool-calling AI agents in production environments?</summary>

### Source [73]: https://www.infoq.com/articles/evaluating-ai-agents-lessons-learned/

Query: What are proven methods and benchmarks for evaluating, testing, and monitoring the accuracy and safety of tool-calling AI agents in production environments?

Answer: Agents are systems not models – evaluate them accordingly. AI agents plan, call tools, maintain state, and adapt across multiple turns. Single-turn accuracy metrics and classical NLP benchmarks like BLEU and ROUGE don't capture how agents fail in practice. Evaluation must target the full system's behavior over time. Behavior beats benchmarks: Task success, graceful recovery from tool failures, and consistency under real-world variability matter more than scoring well on curated test sets.

Five essential pillars for production readiness: 1. Intelligence and Accuracy (task completion accuracy, logical reasoning quality, grounding faithfulness, contextual awareness, multi-step reasoning coherence) evaluated via automated benchmarks, LLM judges, reasoning trace analysis, faithfulness scoring, contextual testing, multi-turn workflow assessment. 2. Performance and Efficiency (TTFT, end-to-end latency, cost per successful task, resource utilization, concurrent scalability) via runtime monitoring, cost accounting, load testing. 3. Reliability and Resilience (input variation robustness, API failure recovery, context retention, long-session memory stability, error handling) via stress testing, failure injection, context drift analysis, extended session testing. 4. Responsibility and Governance (harmful content prevention, adversarial resistance, privacy compliance, access control, decision transparency) via safety classifiers, red-team testing, data audits, permission checks, explainability assessment. 5. User Experience (response clarity, tone appropriateness, user trust score, satisfaction rating) via readability analysis, user surveys, A/B testing, CSAT/NPS with sentiment analysis.

Hybrid evaluation: automated scoring (LLM-as-a-judge, trace analysis, load testing) for repeatability, human judgment for tone, trust, context. Continuous discipline with tools like MLflow (experiment tracing, LLM judges), TruLens (feedback functions, OpenTelemetry), LangChain Evals (task-specific chains), OpenAI Evals (model-graded metrics), Ragas (RAG scoring). Example: LLM-as-a-judge with Claude + LangChain for reference-free (helpfulness) and reference-aware (correctness) scoring. Lessons: controlled performance ≠ real-world readiness; hybrid evaluation essential; reliability > brilliance; efficiency defines viability; safety non-negotiable. Evaluation is continuous loop in AI agent lifecycle.

-----

-----

### Source [75]: https://machinelearningmastery.com/agent-evaluation-how-to-test-and-measure-agentic-ai-performance/

Query: What are proven methods and benchmarks for evaluating, testing, and monitoring the accuracy and safety of tool-calling AI agents in production environments?

Answer: Four pillars: Task Success (completion rate), Tool Usage Quality (relevance, accuracy, efficiency, completeness), Reasoning Coherence (logical steps, alternatives consideration), Cost-Performance (tokens, API calls, latency).

Approaches: LLM-as-a-Judge (rubric-based scoring), Human evaluation (edge cases), Hybrid (automated filter + human review).

Benchmarks: AgentBench (multi-domain), WebArena (web navigation), GAIA (multi-step reasoning), ToolBench (API scenarios). Tools: LangSmith (tracing, evals), Langfuse (observability), RAGAS (extended metrics).

Pipeline: Golden dataset (20-50 examples), clear criteria, 3-5 core metrics, automated evals blocking deployments (5-10% drops), human review for failures. Pitfalls: synthetic data, criteria drift, poor coverage. Start simple, iterate.

-----

</details>

<details>
<summary>How is the Model Context Protocol (MCP) and other emerging standards expected to shape the future of AI agent tool ecosystems and developer workflows?</summary>

### Source [80]: https://a16z.com/a-deep-dive-into-mcp-and-the-future-of-ai-tooling/

Query: How is the Model Context Protocol (MCP) and other emerging standards expected to shape the future of AI agent tool ecosystems and developer workflows?

Answer: MCP, introduced November 2024, is an open protocol standardizing AI model interactions with external tools, data, and services, inspired by LSP but agent-centric for autonomous workflows. It enables turning MCP clients like Cursor into 'everything apps' by integrating servers for Slack, email, images, databases, browsers. Dev-centric workflows allow IDE access to Postgres, Upstash, Browsertools without leaving the environment; auto-generating servers from docs reduces boilerplate. Net-new experiences via Claude Desktop, Highlight's @ command, Blender MCP for text-to-3D. Ecosystem includes coding-centric clients, local-first servers, emerging marketplaces like mcpt, Smithery, OpenTools akin to npm/RapidAPI. Infrastructure like Mintlify, Stainless for server generation; Cloudflare, Toolbase for hosting/management. Future unlocks: multi-tenancy hosting, standardized authentication/authorization, gateways for traffic/security, server discoverability/registry, stateful execution, standard client UX, debugging tools. Implications: shifts tool building/monetization, new pricing via dynamic selection, machine-readable docs, tools as higher abstractions, new hosting modes for multi-step workloads. MCP could become default AI-to-tool interface, enabling autonomous multi-modal AI; pivotal year for marketplaces, auth, multi-step protocol.

-----

-----

### Source [84]: https://blogs.cisco.com/news/building-trust-in-ai-agent-ecosystems

Query: How is the Model Context Protocol (MCP) and other emerging standards expected to shape the future of AI agent tool ecosystems and developer workflows?

Answer: MCP connects AI agents to enterprise tools/resources; requires supply chain security, identity/access, integrity, isolation, governance. Cisco's MCP Scanner provides visibility/validation to reduce risks. Trust controls: authenticate/authorize servers/clients with scoped permissions, validate untrusted outputs, secure discovery/provenance/approval, isolate risks, audit interactions; OAuth 2.1 for authorization. Enables governed AI operations. OWASP Top 10 for Agentic Apps as baseline; AGNTCY for discovery/connectivity; MAESTRO for threat modeling. Builds trustworthy ecosystems for scaling agentic AI.

-----

</details>


## Sources Scraped From Research Results

<details>
<summary>23 Real-World AI Agent Use Cases</summary>

# 23 Real-World AI Agent Use Cases

Software assistants called AI agents have the ability to automate computer users’ repetitive tasks and respond to routine customer and employee questions. Unlike prior generations of helpers built into business applications, which relied on pre-coded rules or keyword triggers, AI agents take advantage of large language models’ predictive power and ability to communicate with users in natural language to carry out multistep workflows.

Agents can help organizations realize a return on their AI initiatives by reducing errors and streamlining processes for tasks such as researching customers for a deal, writing job postings and offer letters, and evaluating and suggesting repair options for manufacturing equipment. They can also help make individual contributors more productive and keep processes moving ahead, even overnight. Agents can look for information across different tools, taking users’ roles and other context into account and staying topical by pulling information from business documents to supplement the underlying LLMs’ training data. Read on to learn about top enterprise use cases for AI agents that your company may be able to put into practice.

## What Is an AI Agent?

[AI agents](https://www.oracle.com/artificial-intelligence/ai-agents/) are software assistants, powered by generative AI, that mediate between pretrained LLMs and computer users to carry out a wide range of multistep tasks inside software applications or on the web. Instead of responding to preprogrammed rules or keywords like previous iterations of digital helpers, AI-powered agents can predict the next logical step in a series of tasks and present relevant information or complete steps in a process, tapping business documents to augment their original information sources.

## Where Are AI Agents Being Used?

Businesses are building and deploying AI agents to assist with recruiting, explain pay and benefits to employees, field customer inquiries, work on sales deals, make financial projections, and undertake equipment repairs. In healthcare, medical practices and hospitals are using agents to help with scheduling and improve automated note-taking and documentation during patient visits, among other use cases.

## 23 AI Agent Use Cases for Businesses

While it’s early days for AI agents, adopters are using them to help complete processes that require access to multiple IT systems, deliver data-driven insights, and relieve employees of some of the steps involved in routine tasks. Here are some of the most common places they can be used in healthcare, HR, manufacturing, finance, and customer support.

### Healthcare

1. 1\. **Clinical assistants.** Allow physicians to call up information from patients’ medical histories by speaking instead of navigating menus. [Clinical AI agents](https://www.oracle.com/health/clinical-suite/clinical-ai-agent/) can be authorized to listen during exams to draft clinical notes, reducing documentation time and letting physicians focus on conversing with patients.

3. 2\. **Disease identification assistance.** Compare clinical notes from patient visits with historical patient data to aid in making a list of possible diagnoses given ailments that present similar symptoms.

5. 3\. **Appointment scheduling.** Automate appointment scheduling, patient registration, and bill creation.

7. 4\. **Drug discovery.** Quickly read and extract information from large numbers of publications. Examine molecular structures to aid in finding new molecules that can serve as potential medicines.

### HR

01. 5\. **Job posting.** Write job listings with responsibilities, required experience, and other qualifications, in line with the employer’s hiring policies.

03. 6\. **Interview scheduling.** Automatically set up meetings with candidates and send follow-up emails.

05. 7\. **Employee onboarding.** Help fill out forms, conduct training, and set up user accounts and devices.

07. 8\. **Explain benefits.** [Converse with employees](https://www.oracle.com/news/announcement/ocw24-oracle-ai-agents-help-organizations-achieve-new-levels-of-productivity-2024-09-11/) about paid time off, retirement savings, healthcare, family leave, and other benefits.

09. 9\. **Employee retention.** Examine salary benchmarks and employee tenure, skills, and performance reviews to better determine turnover risks and help identify workers who could thrive in a higher-level job or benefit from a lateral move.

### Manufacturing

1. 10\. **Maintenance estimates.** Analyze damaged equipment via photos, [estimate needed repairs](https://www.oracle.com/scm/ai-agents-supply-chain-manufacturing/), and select repair options to get the process started.

3. 11\. **Optimize delivery.** Plan shipping routes based on the latest data to speed up deliveries, pare transportation costs, and reduce carbon emissions.

5. 12\. **Sales rep guidance.** Provide up-to-date information about pricing policy changes so reps can make compelling offers while preserving profitability.

7. 13\. **Supply chain risk assessment.** Analyze data on suppliers, products, and inventories, as well as weather, labor, trade, and other external data, to minimize supply chain disruptions and mitigate risk.

### Finance

1. 14\. **Know Your Customer (KYC) processes.** Replace rules-driven workflows with automated identity verification and risk scoring for KYC, the processes banks must follow to confirm their clients are who they claim to be and ask for missing information. Conduct customer assessments across multiple IT systems accumulated through bank mergers and acquisitions.

3. 15\. **Anti–money laundering and fraud detection.** Monitor transactions continuously for suspicious activity.

5. 16\. **Automated trading.** Analyze data on market fundamentals, price movements, trading volumes, risk, and other factors to inform securities trading strategies.

7. 17\. **Credit underwriting.** Pull data from various sources, compute financial ratios, show potential outcomes versus risk tolerance, and draft credit memos for review.

### Customer support

1. 20\. **Triage and route tickets.** Learn from past ticket data to classify customers’ requests and better understand sentiment, automate responses to common queries, and escalate queries needing more attention.

3. 21\. **Speed up returns.** Check the policy on returned items, generate a return order, and send it to a customer.

5. 22\. **Order delivery tracking.** Automatically answer often time-consuming questions about order status, schedule deliveries, and suggest optimal delivery routes.

7. 23\. **Recommend resolutions.** Suggest AI-recommended steps to resolve customers’ technical, product setup, or other problems, possibly reducing call center workloads.

## Future of AI Agents

More efficient AI models may lead to agents that are able to work more autonomously through routine process steps. Testing procedures will also improve as software vendors add quantitative measures of AI agents’ effectiveness. The industry may also agree on a standard protocol for communications among agents.

## AI Agent Use Cases FAQs

**What does an AI agent do?**

AI agents are generally designed to use the natural language conversation and prediction capabilities of large language models to automatically show computer users insights gleaned from multiple IT systems, or they carry out steps in a process, which can save users time.

**Is ChatGPT an AI agent?**

No, the ChatGPT service from OpenAI is a chatbot that lets users conduct a typed dialogue with the company’s LLMs, but it doesn’t autonomously take actions on a user’s behalf.

</details>

<details>
<summary>Since OpenAI released function calling in 2023, I’ve been thinking about what it would take to unlock an ecosystem of agent and tool use. As the foundational models get more intelligent, agents’ ability to interact with external tools, data, and APIs becomes increasingly fragmented: Developers need to implement agents with special business logic for every single system the agent operates in and integrates with.</summary>

Since OpenAI released function calling in 2023, I’ve been thinking about what it would take to unlock an ecosystem of agent and tool use. As the foundational models get more intelligent, agents’ ability to interact with external tools, data, and APIs becomes increasingly fragmented: Developers need to implement agents with special business logic for every single system the agent operates in and integrates with.

It’s clear that there needs to be a standard interface for execution, data fetching, and tool calling. **APIs were the internet’s first great unifier—creating a shared language for software to communicate — but AI models lack an equivalent.**

Model Context Protocol (MCP), introduced in November 2024, has gained significant traction within developer and AI communities as a potential solution. In this post, we’ll explore **what MCP is, how it changes the way AI interacts with tools, what developers are already building with it, and the challenges that still need solving.**

Let’s dive in.

## What is MCP?

**MCP is an open protocol that allows systems to provide context to AI models in a manner that’s generalizable across integrations.** The protocol defines how the AI model can call external tools, fetch data, and interact with services. As a concrete example, below is how the Resend MCP server works with multiple MCP clients.

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-Example-MCP-x2000-1024x455.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-Example-MCP-x2000.png)

The idea is not new; MCP [took inspiration from the LSP (Language Server Protocol)](https://spec.modelcontextprotocol.io/specification/2024-11-05/#:~:text=MCP%20takes%20some%20inspiration%20from,the%20ecosystem%20of%20AI%20applications). In LSP, when a user types in an editor, the client queries the language server to autocomplete suggestions or diagnostics.

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250314-LSP-x2000-1024x422.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250314-LSP-x2000.png)

Where MCP extends beyond LSP is in its agent-centric execution model: LSP is mostly reactive (responding to requests from an IDE based on user input), whereas MCP is designed to support autonomous AI workflows. Based on the context, **AI agents can decide which tools to use, in what order, and how to chain them together to accomplish a task.** MCP also introduced a human-in-the-loop capabilities for humans to provide additional data and approve execution.

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-MCP-x2000-1024x541.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-MCP-x2000.png)

## Popular use cases today

With the right set of MCP servers, users can turn every MCP client into an “everything app.”

Take Cursor as an example: Although Cursor is a code editor, it’s also a well-implemented MCP client. End users can turn it into a Slack client using the [Slack MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/slack), an email sender using [Resend MCP server](https://github.com/resend/mcp-send-email/tree/main), and an image generator using the [Replicate MCP server](https://github.com/deepfates/mcp-replicate). A more powerful way to leverage MCPs is installing multiple servers on one client to unlock new flows: Users can install a server to generate the [front-end UI](https://github.com/21st-dev/magic-mcp) from Cursor, but also ask the agent to use an image-generation MCP server to generate a hero image for the site.

Beyond Cursor, most use cases today can be summarized into either dev-centric, local-first workflows, or net-new experiences using LLM clients.

### Dev-centric workflows

For developers who live and breathe in code every day, a common sentiment is, “I don’t want to leave my IDE to do _x_”. MCP servers are great ways to make this dream a reality.

Instead of switching to Supabase to check on the database status, developers can now use the [Postgres MCP server](https://github.com/modelcontextprotocol/servers/tree/main/src/postgres) to execute read-only SQL commands and the [Upstash MCP server](https://github.com/upstash/mcp-server) to create and manage cache indices right from their IDE. When iterating on code, developers can also leverage the [Browsertools MCP](https://github.com/AgentDeskAI/browser-tools-mcp) to give coding agents access to a live environment for feedback and debugging.

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/image1-1024x989.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/image1.png)

_An example of how Cursor agent uses Browsertools to get access to console logs and other real-time data and debug more efficiently._

Outside of workflows that interact with a developer tool, a new use that MCP servers unlock is being able to add highly accurate context to coding agents by either [crawling a web page](https://github.com/mendableai/firecrawl-mcp-server) or [auto-generating an MCP server](https://mintlify.com/blog/generate-mcp-servers-for-your-docs) based on the documentation. Instead of manually wiring up integrations, developers can spin up MCP servers straight from existing documentation or APIs, making tools instantly accessible to AI agents. This means less time spent on boilerplate and more time actually using the tools — whether it’s pulling in real-time context, executing commands, or extending an AI assistant’s capabilities on the fly.

### Net-new experiences

IDEs like Cursor are not the only MCP clients available, even though they have received the most attention due to MCP’s strong appeal to technical users. For non-technical users, Claude Desktop serves as an excellent entry point, making MCP-powered tools more accessible and user-friendly to a general audience. Soon, we will likely see specialized MCP clients emerge for business-centric tasks such as customer support, marketing copywriting, design, and image editing, as these fields closely align with AI’s strengths in pattern recognition and creative tasks.

The design of an MCP client and the specific interactions it supports plays a crucial role in shaping its capabilities. A chat application, for instance, is unlikely to include a vector-rendering canvas, just as a design tool is unlikely to provide functionality for executing code on a remote machine. Ultimately, the **MCP client experience defines the overall MCP user experience** — and we have so much more to unlock when it comes to MCP client experience.

One example of this is how Highlight implemented the [@ command](https://x.com/PimDeWitte/status/1899829221813334449) to invoke any MCP servers on its client. The result is a new UX pattern in which the MCP client can pipe generated content into any downstream app of choice.

https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/Notion-screenshot.png

_An example of Highlight’s implementation of Notion MCP (plugin)._

Another example is the [Blender MCP server](https://x.com/sidahuj/status/1901632110395265452) use case: Now, amateur users who barely know Blender can use natural language to describe the model they want to build. We are seeing the text-to-3D workflow playing out in real time as the community implements servers for other tools like Unity and Unreal engine.

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/image7-1024x573.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/image7.png)

_An example of using Claude Desktop with [Blender MCP server](https://github.com/ahujasid/blender-mcp)._

Although we mostly think about servers and clients, the MCP ecosystem is gradually shaping up as the protocol evolves. This market map covers the most active areas today, although there are still many blank spaces. Knowing MCP is still in the early days, _we’re excited to add more players to the map as the market evolves and matures._(And we will explore some of these future possibilities in the next section.)

[https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-MCP-Market-Map-v2-x2000-1024x866.png](https://d1lamhf6l6yk6d.cloudfront.net/uploads/2025/03/250319-MCP-Market-Map-v2-x2000.png)

On the MCP client side, **most of the high-quality clients we see today are coding-centric**. This is not surprising, since developers are usually early adopters of new technology, but, as the protocol matures, we expect to see more business-centric clients.

**Most of the MCP servers we see are local-first and focus on single players. This is a symptom of MCP presently only supporting SSE- and command-based connections.** However, we expect to see more MCP server adoption as the ecosystem makes remote MCP first-class and MCP adopts [Streamable HTTP transport](https://github.com/modelcontextprotocol/specification/pull/206).

There is also a new wave of MCP marketplace and server-hosting solutions emerging to make MCP server-discovery possible. Marketplaces like [Mintlify](https://mintlify.com/)’s [mcpt](https://www.mcpt.com/), [Smithery](https://smithery.ai/), and [OpenTools](https://opentools.com/) are making it easier for developers to discover, share, and contribute new MCP servers — much like how npm transformed package management for JavaScript or how RapidAPI expanded API discovery. This layer will be crucial for standardizing access to high-quality MCP servers, allowing AI agents to dynamically select and integrate tools on demand.

As MCP adoption grows, **infrastructure and tooling will play a critical role in making the ecosystem more scalable, reliable, and accessible**. Server generation tools like Mintlify, [Stainless](https://www.stainless.com/), and [Speakeasy](https://www.speakeasy.com/) are reducing the friction of creating MCP-compatible services, while hosting solutions like Cloudflare and Smithery are addressing deployment and scaling challenges. At the same time, **connection-management platforms like [Toolbase](https://gettoolbase.ai/)** are beginning to streamline local-first MCP key management and proxy.

## Future possibilities

However, we are only in the early stages of the evolution of agent-native architecture. And although there is a lot of excitement on MCPs today, there are also many unsolved problems when building and shipping with MCP.

Some things to unlock in the next iteration of the protocol include:

### Hosting and multi-tenancy

MCP supports a one-to-many relationship between an AI agent and its tools, but multi-tenant architectures (e.g., SaaS products) need to support many users accessing a shared MCP server at once. Having remote servers by default could be a near-term solution to make MCP servers more accessible, but many enterprises will also want to host their own MCP server and separate data and control planes.

A streamlined toolchain to support at-scale MCP server deployment and maintenance is the next piece that can unlock broader adoption.

### Authentication

MCP does not currently define a standard authentication mechanism for how clients authenticate with servers, nor does it provide a framework for how MCP servers should securely manage and delegate authentication when interacting with third-party APIs. Authentication is currently left up to individual implementations and deployment scenarios. In practice, MCP’s adoption so far seems to be on local integrations where explicit authentication isn’t always needed.

A better authentication paradigm could be one of the big unlocks when it comes to remote MCP adoption. From a developer’s perspective, a unified approach should cover:

- **Client authentication:** standards methods like OAuth or API tokens for client-server interactions
- **Tool authentication:** helper functions or wrappers for authenticating with third-party APIs
- **Multi-user authentication:** tenant-aware authentication for enterprise deployments

### Authorization

Even if a tool is authenticated, who should be allowed to use it and how granular should their permissions be? MCP lacks a built-in permissions model, so access control is at the session level — meaning a tool is either accessible or completely restricted. While future authorization mechanisms could shape finer-grained controls, the current approach relies on [OAuth 2.1-based authorization flows](https://github.com/modelcontextprotocol/specification/blob/5c35d6dda5bf04b5c8c76352c9f7ee18d22b7a08/docs/specification/draft/basic/authorization.md) that grant session-wide access once authenticated. This creates additional complexity as more agents and tools are introduced — each agent typically requires its own session with unique authorization credentials, leading to a growing web of session-based access management.

### Gateway

As MCP adoption scales, a gateway could act as a centralized layer for authentication, authorization, traffic management, and tool selection. Similar to API gateways, it would enforce access controls, route requests to the right MCP servers, handle load balancing, and cache responses to improve efficiency. This is especially important for multi-tenant environments, where different users and agents require distinct permissions. A standardized gateway would simplify client-server interactions, improve security, and provide better observability, making MCP deployments more scalable and manageable.

### MCP server discoverability and usability

Currently, finding and setting up MCP servers is a manual process, requiring developers to locate endpoints or scripts, configure authentication, and ensure compatibility between the server and the client. Integrating new servers is time-consuming, and AI agents can’t dynamically discover or adapt to available servers.

Based on [Anthropic’s talk](https://youtu.be/kQmXtrmQ5Zg?t=4927) at the AI engineer conference last month, though, **it sounds like a MCP server registry and discovery protocol is coming**. This could unlock the next phase of adoption for MCP servers.

### Execution environment

Most AI workflows require multiple tool calls in sequence — but MCP lacks a built-in workflow concept to manage these steps. It’s not ideal to ask every client to implement resumability and retryability. Although today we see developers exploring solutions like [Inngest](https://www.inngest.com/) to make this work, promoting stateful execution to a first-class concept will clear up the execution model for most developers.

### Standard client experience

A common question we’ve heard from the developer community is how to think about tool selection when building an MCP client: Does everyone need to implement their own RAG for tools, or is there a layer waiting to be standardized?

Beyond tool selection, there’s also no unified UI/UX patterns for invoking tools (we have seen everything ranging from slash commands to pure natural language). A standard client-side layer for tool discovery, ranking and execution could help create a more predictable developer and user experience.

### Debugging

Developers of MCP servers often discover that it’s hard to make the same MCP server work across clients easily. More often than not, each MCP client has its own quirks, and client-side traces are either missing or hard to find, making debugging MCP servers an extremely difficult task. As the world starts to build more remote-first MCP servers, a new set of tooling is needed to make the dev experience more streamlined across local and remote environments.

## Implications of AI tooling

MCP’s dev experience reminds me of API development in the 2010s. The paradigm is new and exciting, but the toolchains are in the early days. If we fast-forward to years from now, what would happen if MCP becomes the de facto standard for AI-powered workflows? Some predictions:

- **The competitive advantage of dev-first companies will evolve** from shipping the best API design to also shipping the best collection of tools for agents to use. If MCPs will have the ability to autonomously discover tools, providers of APIs and SDKs will need to make sure their tooling is easily discoverable from search and be differentiated enough for the agent to pick for a particular task. This can be a lot more granular and specific than what human developers look for.
- **A new pricing model may emerge** if every app becomes a MCP client and every API becomes a MCP server: Agents may pick the tools more dynamically, based on a combination of speed, cost, and relevance. This may lead to a more market-driven tool-adoption process that picks the best-performing and the most modular tool instead of the most widely adopted one.
- **Documentation will become a critical piece of MCP infrastructure** as companies will need to design tools and APIs with clear, machine-readable formats (e.g., [llms.txt](https://mintlify.com/blog/simplifying-docs-with-llms-txt)) and make MCP servers a de facto artifact based on existing documentation.
- **APIs alone are no longer enough, but can be great starting points.** Developers will discover that the mapping from API to tools is rarely 1:1. Tools are a higher abstraction that makes the most sense for agents at the time of task execution — instead of simply calling send\_email(), an agent may opt for draft\_email\_and\_send() function that includes multiple API calls to minimize latency. MCP server design will be scenario- and use-case-centric instead of API-centric.
- **There will be a new mode of hosting** if every software by default becomes a MCP client, because the workload characteristics will be different from traditional website hosting. Every client will be multi-step in nature and require execution guarantees like resumability, retries, and long-running task management. Hosting providers will also need real-time load balancing across different MCP servers to optimize for cost, latency, and performance, allowing AI agents to choose the most efficient tool at any given moment.

MCP is already reshaping the AI-agent ecosystem, but the next wave of progress will be defined by how we address the foundational challenges. If done right, MCP could become the default interface for AI-to-tool interactions and unlock a new generation of autonomous, multi-modal, and deeply integrated AI experiences.

If adopted widely, MCPs can represent a shift in how tools are built, consumed, and monetized. We are excited to see where the market takes them. This year will be pivotal: Will we see the rise of a unified MCP marketplace? Will authentication become seamless for AI agents? Can multi-step execution be formalized into the protocol?

</details>

<details>
<summary>AI Agents: Key Concepts and How They Overcome LLM Limitations</summary>

# AI Agents: Key Concepts and How They Overcome LLM Limitations

An AI agent is an autonomous software entity that is often used to augment a large language model. Here's what developers need to know.

Jun 11th, 2024 6:24am by [Janakiram MSV](https://thenewstack.io/author/janakiram/ "Posts by Janakiram MSV")

https://cdn.thenewstack.io/media/2024/06/504e8243-allison-saeng-burzgf1rio8-unsplash-1024x768.jpg

Image via Unsplash+.


As large language models (LLMs) become more powerful, a new breed of software known as “agents” has arisen to augment and enhance the capabilities of LLMs. This article introduces the key concepts of agents and how they complement LLMs.

Since the initial release of ChatGPT, which was based on GPT 3.5, [large language models](https://thenewstack.io/what-is-a-large-language-model/) have evolved and matured. Some of the recent releases — like [GPT-4o](https://openai.com/index/hello-gpt-4o/), [Gemini Pro](https://deepmind.google/technologies/gemini/pro/), and the [Claude Opus](https://www.anthropic.com/news/claude-3-family) models — have even demonstrated advanced reasoning abilities. The [open language model](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) landscape has also been rapidly evolving in recent times. Several variants of these LLMs have been released for use in private environments. In terms of reasoning and answering complex questions, some open language models — like [Mistral](https://docs.mistral.ai/getting-started/models/) and [Llama 3](https://llama.meta.com/llama3/) — are on par with commercial models. This has all been a driver of the [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/) trend.

## What Is an AI Agent?

An agent is an autonomous software entity that leverages the language processing capabilities of LLMs to perform a wide range of tasks beyond simple text generation and comprehension. These agents extend the functionality of LLMs by incorporating mechanisms to interact with digital environments, make decisions and execute actions based on the language understanding derived from the LLM.

> In the context of operating systems, consider LLMs to be the kernel and agents to be the programs.

Agents rely heavily on the LLM to perform reasoning while augmenting an LLM’s functionality by adding new capabilities.

LLMs have several limitations that agents attempt to overcome. Let’s take a look at some of these limitations.

## Limitations of LLMs

### **LLMs Don’t Have Memory**

Similar to a REST API call, invoking an LLM is entirely stateless. Each interaction with an LLM is independent, meaning the model does not inherently remember prior exchanges or build upon previous conversations. This limitation affects the continuity and coherence of long-term interactions, as the model cannot leverage historical context to inform future responses. The stateless nature of LLMs necessitates that each input must be fully self-contained, leading to repetitive or disjointed interactions in extended use cases.

### **LLM Invocations Are Synchronous**

LLMs operate in a synchronous manner, meaning that they process and respond to each input sequentially, one at a time. This synchronous operation implies that the model must complete its response to a given input before it can process the next one. This sequential processing can be a limitation in scenarios requiring real-time interaction or simultaneous handling of multiple queries, as it cannot inherently parallelize the processing of different inputs.

### LLMs Might Hallucinate

LLMs might produce [hallucinations](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/), which are instances where the model generates information that is factually incorrect or nonsensical. This phenomenon occurs because LLMs are trained on vast datasets comprising text from the internet, where they learn patterns and correlations rather than factual accuracy. As a result, they can fabricate details or present false information confidently, creating the illusion of knowledge.

### **LLMs Cannot Access the Internet**

LLMs cannot browse the web or invoke a web service, so they are limited to the data they were trained on and do not have the capability to retrieve or verify information from live web sources in real time. This constraint means that their responses are based solely on the pre-existing knowledge embedded within them, which might not be up-to-date or contextually relevant for real-time inquiries. Consequently, LLMs are unable to provide current news updates, access the latest research or pull data from dynamic online databases — making their use less effective for tasks requiring the most recent information.

### **LLMs Are Bad at Math**

LLMs are often poor at handling mathematical tasks, particularly those that require precise calculations or complex problem-solving. This limitation arises because LLMs are primarily designed to understand and generate natural language based on patterns learned from vast textual datasets. While they can perform simple arithmetic and follow basic mathematical rules, their ability to solve more complex mathematical problems or ensure accuracy in multi-step calculations is limited. They often lack the structured logical reasoning needed to perform advanced mathematical operations reliably.

### **LLMs Have Non-Deterministic Output**

LLMs exhibit non-deterministic output in terms of data format and structure, meaning that identical inputs can produce varying outputs each time they are processed. This variability stems from the probabilistic nature of the algorithms that underpin LLMs, which select from a range of possible responses based on learned patterns rather than deterministic rules. As a result, the format and structure of the output can differ, making it challenging to achieve consistent results, particularly for applications requiring uniformity in response formatting — such as automated report generation, form filling or data extraction.

## How Do Agents Augment LLMs?

Agents bridge the gap that exists between traditional software development tools and LLMs, which helps solve or alleviate some of the above limitations.

For example, by integrating tools such as web browsing and code execution environments, agents can combine real-world data with complex calculations before having an LLM analyze and generate a detailed response.

https://cdn.thenewstack.io/media/2024/06/d2071c12-agents-1024x576.jpeg

[Zoom](https://cdn.thenewstack.io/media/2024/06/d2071c12-agents-1024x576.jpeg)

In the context of operating systems, consider LLMs to be the kernel and agents to be the programs. The shell consists of the tools and support services needed by agents to execute. Agents enhance an LLM’s functionality by connecting it with the tools and external services needed to complete a task.

Let’s understand the role of agents in augmenting the capabilities of LLM.

### **Memory and Context Retention**

Unlike LLMs, which are stateless and do not retain a memory of previous interactions, agents can incorporate memory mechanisms to remember past interactions and build upon them. This allows agents to maintain continuity and coherence in long-term engagements, leveraging historical context to inform future responses. This capability enhances the user experience by creating more personalized and contextually relevant interactions.

### **Asynchronous and Parallel Processing**

While LLMs process inputs synchronously and sequentially, agents can manage multiple tasks simultaneously and operate asynchronously. This ability to parallelize processes enables agents to handle real-time interactions more effectively, improving efficiency and responsiveness in scenarios that require simultaneous handling of multiple queries or tasks.

### **Fact-Checking and Real-Time Information Access**

Agents can mitigate the issue of hallucinations in LLMs by incorporating real-time data verification and access to external information sources. By connecting to the internet or specific databases, agents can validate the information generated by LLMs, ensuring accuracy and reducing the incidence of false or misleading outputs. This makes agents particularly valuable in applications where up-to-date and precise information is crucial.

### **Enhanced Mathematical Capabilities**

Agents can integrate specialized mathematical engines or software to handle complex calculations and problem-solving tasks, compensating for the mathematical weaknesses of LLMs. This integration allows agents to perform precise and reliable mathematical operations, expanding their utility in technical and scientific domains.

### **Consistent Output Formatting**

To address the non-deterministic nature of LLM outputs, agents can implement post-processing steps to standardize the format and structure of responses. For example, they can enforce that the output from an LLM is always formatted in JSON or XML. By ensuring consistency in data presentation, agents can enhance the reliability of outputs in applications requiring uniformity, such as report generation and data extraction.

### **Persona-Driven Interactions**

Agents enhance persona-driven interactions with LLMs by leveraging memory and personalization capabilities to create more tailored and engaging user experiences. By maintaining context over multiple interactions, agents can adapt responses to align with the user’s preferences, history and conversational style — effectively simulating a consistent persona. This personalized approach not only improves user satisfaction but also allows the agent to provide more relevant and context-aware assistance. Agents can dynamically adjust their behavior based on user feedback and past interactions, making the conversation feel more natural and human-like.

## Summary

LLMs have evolved significantly, exemplified by models like GPT-4o and Gemini 1.5. However, they remain stateless, process inputs sequentially, can hallucinate, lack real-time data access, struggle with complex math and produce non-deterministic outputs.

AI agents augment LLMs by incorporating memory mechanisms for context retention, managing tasks asynchronously and validating information in real-time, thereby enhancing accuracy and coherence. They also integrate specialized mathematical engines and standardize output formats, making them more reliable and efficient for diverse applications.

</details>

<details>
<summary>Evaluating AI Agents in Practice: Benchmarks, Frameworks, and Lessons Learned</summary>

# Evaluating AI Agents in Practice: Benchmarks, Frameworks, and Lessons Learned

### Key Takeaways

- Agents are systems not models – evaluate them accordingly. AI agents plan, call tools, maintain state, and adapt across multiple turns. Single-turn accuracy metrics and classical natural language processing (NLP) benchmarks like bilingual evaluation understudy (BLEU) and recall-oriented understudy for gisting evaluation (ROUGE) don't capture how agents fail in practice. Evaluation must target the full system's behavior over time.
- Behavior beats benchmarks. Task success, graceful recovery from tool failures, and consistency under real-world variability matter more than scoring well on curated test sets. An agent that works perfectly in a sandbox but silently misreports a failed refund in production hasn't passed any evaluation that counts.
- Hybrid evaluation is non-negotiable. Automated scoring (LLM-as-a-judge, trace analysis, and load testing) gives you repeatability and scale. Human judgment captures what automation misses: tone, trust, and contextual appropriateness. The best evaluation pipelines combine both, continuously.
- Operational constraints are first-class evaluation targets. Latency, cost per task, token efficiency, tool reliability, and policy compliance aren't afterthoughts, they are what determines whether a technically capable agent is viable at enterprise scale.
- Safety, governance, and user trust complete the picture. Red teaming, PII handling, permission boundary testing, and user experience scoring are as critical as accuracy. A technically brilliant agent that violates privacy boundaries or confuses users is a liability, not an asset.

## Introduction

You may have seen teams in your organization leveraging AI agents for demos, experiments, testing workflows where everything works perfectly. The agent plans, reasons, picks the right tool, and executes flawlessly during experiments. In production, the system fails or exhibits suboptimal behavior, and no one is quite sure whether the "smart" agent is actually reliable.

This article is for engineering and ML teams moving tool-using AI agents from prototype to production. It offers a practical evaluation framework, covering what to measure, how to measure it, and which tools to use, so you can catch failures before your users do.

The examples and code snippets in this article are intentionally minimal and illustrative, a one-sample Claude + LangChain evaluation meant to demonstrate both reference-free (helpfulness) and reference-aware (correctness) scoring, with a stable, versioned model for reproducibility. Production-grade evaluation pipelines require additional hardening around reliability, governance, cost control, version management, and data protection. In production setups, it is a good practice to use a separate judge model to reduce self-grading bias as shown in the code example.

In traditional software engineering, systems are rigorously tested before being deployed to production. AI agents, however, challenge this practice. While teams often validate individual models using established benchmarks, these evaluations rarely extend to the full agentic system operating in realistic environments. Unlike standard LLMs that generate single-turn text responses, AI agents are composite systems: They plan actions, invoke tools and APIs, maintain memory across interactions, and adapt their behavior over multiple steps and sessions. Classical NLP metrics like BLEU or ROUGE weren't designed for this situation; they score static text, not dynamic behavior. Consider a concrete example: An order-triage agent correctly identifies a shipping exception in step one, but when the refund API returns an unexpected error in step two, the agent silently skips the refund and reports the case as resolved. No single-turn accuracy test would catch that failure. For this reason, AI agents must be evaluated on behavioral dimensions, consistency, safety, resilience, and effectiveness across real-world conditions, not just on the text they generate.

This gap between how agents actually fail and what traditional metrics can detect points to a clear need: We need evaluation methods and frameworks that can capture how agents behave, not just one that simply checks the text they generate, things like success rates, reasoning quality, resilience to unexpected inputs, and how safely they can handle sensitive or risky situations.

The tooling ecosystem for agent evaluation is maturing rapidly. [MLflow](https://mlflow.org/) (v3.0+) now supports experiment tracing and built-in LLM judge capabilities. [TruLens](https://www.trulens.org/) enables pluggable feedback functions with OpenTelemetry integration. [LangChain Evals](https://docs.smith.langchain.com/) provides utilities for designing task-specific evaluation chains. [OpenAI Evals](https://github.com/openai/evals) offers a framework for model-graded metrics and version comparison. Finally, [Ragas](https://docs.ragas.io/) focuses on scoring the quality of retrieval-augmented responses. Feature sets evolve quickly across these tools, so it's worth checking each project's current documentation for precise capability boundaries. These and other emerging frameworks are making agent evaluation more structured and reproducible.

To make these ideas concrete, the rest of this article focuses on practical evaluation approaches you can apply - especially LLM-as-a-judge scoring, trace-based analysis, and repeatable test harnesses for multi-step agent workflows. The following code example demonstrates a minimal LLM-as-a-judge pattern using Claude and LangChain. The code evaluates a single-turn response for helpfulness and correctness, but the same approach extends naturally to multi-step agent traces, scoring tool-call sequences, retry behavior, and memory consistency across turns. This is a starter pattern, not a comprehensive benchmark taxonomy; adapt it to your own agent architecture, tooling, and evaluation needs.

```python
# Minimal, one-sample evaluation with Claude + LangChain
# Goal: show BOTH reference-free (helpfulness) and reference-aware (correctness) scoring.
# some of the finer points are  left for further exploration intentionally, to avoid excessive verbosity

from langchain_anthropic import ChatAnthropic
from langchain.evaluation import load_evaluator

#  Pick a stable, versioned Claude model
# We use Sonnet 4.5 here; substitute any supported Claude model
# (e.g., claude-haiku-4-5-20251001) depending on your access tier and cost/quality trade-off.
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)
```

The following repository includes an end-to-end, runnable blueprint that demonstrates these patterns in code. You can use Claude and Langchain.

## Background

In a modern e-commerce environment, many critical workflows continue to rely heavily on human input: strategy development, data management, operational triage, issue resolution, and more. These workflows span ordering, product management, pricing, and payment instrument management. Over recent quarters, teams have begun developing and piloting AI agents to automate specific operations workflows: order exception triage, pricing and promotion validation, product catalog enrichment and policy checks, payment and refund issue investigation, and L2/L3 incident response across distributed commerce services.

These agents are typically evaluated first in controlled environments (e.g., sandbox APIs, replayed tickets, and synthetic edge cases) before being considered for production use. A practical caution to consider: Real operational inputs frequently contain PII and sensitive transaction data. Before logging prompts, traces, or judge rationales, especially when integrating with observability tooling like MLflow or OpenTelemetry, teams should apply redaction or anonymization pipelines to avoid inadvertently exposing customer data in evaluation logs.

However, teams often face challenges when transitioning from experimentation to production: fragile planning, unreliable tool and API calls, memory drift across sessions, and inconsistent multi-turn behavior. Traditional LLM metrics, along with single-turn accuracy, do not adequately capture an agent's ability to plan effectively, recover from failures, maintain long-term context, control costs and latency, or remain resilient against adversarial inputs. These limitations have motivated the design and implementation of more robust evaluation frameworks aimed at minimizing risks during deployment. Figure 1 illustrates where evaluation fits within the broader AI agent development lifecycle, from initial design and prototyping through controlled testing to production deployment and continuous monitoring.

The key takeaway is that evaluation is not a one-time gate between experimentation and production; it is a recurring loop that feeds back into agent design at every stage. The five evaluation pillars introduced in the next section, intelligence, performance, reliability, responsibility, and user experience, draw on common industry practices and emerging consensus across MLOps, responsible AI, and production engineering communities rather than a single proprietary methodology.

https://imgopt.infoq.com/fit-in/3000x4000/filters:quality(85/filters:no_upscale()/articles/evaluating-ai-agents-lessons-learned/en/resources/189figure-1-1773307287862.jpg)

**Figure 1. Evaluating AI agents – AI agent development lifecycle.**

## Things to Evaluate for AI Agents

Before we discuss how to evaluate, we must define what evaluation means in an operational setting and which agent behaviors (e.g., task success, recovery, safety, cost, and user trust) should be measured to determine production readiness. Often we are interested to know how the AI agents work reliably, efficiently, and responsibly in the real world or in our production.

From experience, I've found that truly effective evaluation comes down to five essential pillars. These aren't drawn from a single proprietary framework, they're a synthesis of common patterns I've seen across MLOps, responsible AI, and production engineering practices, consolidated into a structure that covers the minimum surface area needed to assess whether an agent is production-ready. Each pillar addresses a distinct failure mode: An agent can be smart but slow, fast but brittle, reliable but unsafe, or technically sound but confusing to users. Miss any one dimension and you're carrying unquantified risk into production.

### Intelligence and Accuracy

This pillar captures how well the agent actually "thinks". This approach isn’t just about producing the right answer, it's about how it arrives there. A strong agent reasons logically, grounds its responses in evidence, and adapts gracefully when faced with new or incomplete information. Not only should an agent complete a task, but also demonstrate sound reasoning and contextual awareness throughout the process. In practice, this approach goes beyond simple correctness metrics and pays attention to how faithfully an agent stays true to its retrieved context or data sources, and how effectively it applies reasoning across multi-step workflows.

### Performance and Efficiency

This next pillar is the operational heart of any production system. Even the smartest agent fails if it is slow, expensive, or unstable under scale. Evaluation here means examining how efficiently the agent uses computational and financial resources, its time to first token (TTFT), overall latency, and cost per successful task. Evaluation is also about scalability: Can it handle growing data volumes, multiple concurrent users, and longer-running tasks without degradation? The most successful agents strike the delicate balance between intelligence and efficiency, fast enough to serve users in real time, yet economical enough to sustain at enterprise scale.

### Reliability and Resilience

This pillar is all about consistency under pressure. A reliable agent isn’t just accurate once, it’s accurate _every time_. It should handle paraphrased inputs, API errors, and missing data without breaking. Robustness testing here is crucial: Rerun tasks with varied inputs, simulate tool failures, or stress-test memory over long sessions. A resilient agent recovers gracefully, maintains context across extended conversations, and doesn’t spiral into incoherence when faced with ambiguity. In short, reliability is what separates impressive demos from production-grade systems.

### Responsibility and Governance

This pillar anchors the ethical foundation of AI agents. As these systems take on more autonomy, how they behave becomes just as important as what they achieve. This pillar covers safety, fairness, and compliance, ensuring agents handle sensitive topics with care, respect privacy boundaries, and adhere to legal and organizational policies. Evaluation must probe whether the agent can resist harmful or adversarial prompts, stay within approved access controls, and provide transparent reasoning when making decisions. In enterprise environments, this approach is non-negotiable; an agent that is technically brilliant but ethically careless can cause more harm than good.

### User Experience

User-centric experience captures what users actually care about: response clarity, appropriate tone, and, most importantly, trust. These subjective qualities often require hybrid evaluation approaches combining automated metrics with human judgment.

Taken together, these five pillars define what it means for an AI agent to be truly production-ready. They shift evaluation from a narrow accuracy exercise to a holistic assessment of intelligence, trustworthiness, and operational maturity. Because in the end, it’s not just about whether your agent works, it’s about whether it can be trusted to work well, at scale, and for the right reasons.

With these pillars defined, the next step is operationalizing them, translating each dimension into measurable signals, repeatable test cases, and evaluation routines you can run continuously. The goal is to move from abstract "agent quality" to an evaluation pipeline that produces comparable results across prompts, datasets, model versions, and tool configurations.

## How to Evaluate: Methods That Actually Work

Once you know what to measure, the next step is figuring out how to measure it effectively. Evaluating AI agents isn’t a one-time test, it’s an ongoing process that blends automation, observation, and human feedback. In e-commerce operations, this process is already showing up in real workflows where agents operate under permissioned actions and operational constraints, exactly the kind of conditions the five pillars are designed to evaluate. Shopify Sidekick takes actions inside the Shopify Admin while respecting staff permission boundaries (a reliability and governance concern). Amazon's Enhance My Listing helps sellers maintain and optimize product listings, requiring grounding faithfulness and contextual accuracy. And Walmart's My Assistant supports associates with drafting and summarizing operational content, where tone, clarity, and user trust are front and center. Each example surfaces a different evaluation challenge, permissions, accuracy, user experience, reinforcing why a multi-pillar approach matters.

Figure 2 summarizes the key metrics and evaluation methods for each pillar. Use it as a checklist when designing your evaluation plan: Start with Reliability and Performance (these are the most common blockers in production deployments), then layer in Intelligence and Responsibility testing, and round out with User Experience once the agent is functionally stable. Not every team will need every metric on day one; prioritize based on your agent's risk profile and deployment context.

|     |     |     |
| --- | --- | --- |
| **Dimension** | **Key Metrics (Summary)** | **Evaluation Methods** |
| Intelligence and Accuracy | Task Completion Accuracy<br> Logical Reasoning Quality<br> Grounding Faithfulness<br> Contextual Awareness<br> Multi-step Reasoning Coherence | - Automated benchmarks and LLM judges<br>- Reasoning trace analysis<br>- Faithfulness scoring<br>- Contextual testing<br>- Multi-turn workflow assessment |
| Performance and Efficiency | Time-to-First-Token (TTFT)<br> End-to-End Latency<br> Cost per Successful Task<br> Resource Utilization Efficiency<br> Concurrent User Scalability | - Runtime monitoring and latency tracking<br>- Cost accounting; resource usage analysis<br>- Load testing and simulation |
| Reliability and Resilience | Input Variation Robustness<br> API Failure Recovery<br> Context Retention Consistency<br> Long-session Memory Stability<br> Error Handling Gracefulness | - Stress testing and input variation<br>- Failure injection<br>- Context drift analysis<br>- Extended session testing<br>- Graceful degradation evaluation |
| Responsibility and Governance | Harmful Content Prevention<br> Adversarial Prompt Resistance<br> Privacy Boundary Compliance<br> Access Control Adherence<br> Decision Transparency | - Safety classifiers and red-team testing<br>- Data audits<br>- Permission boundary checks<br>- Explainability assessment |
| User Experience | Response Clarity<br> Tone Appropriateness<br> User Trust Score<br> Overall Satisfaction Rating<br> User Satisfaction Score | - Readability and tone analysis<br>- User surveys and trust studies<br>- A/B testing<br>- CSAT/NPS feedback with sentiment analysis |

**Figure 2. Evaluation methods.**

The best evaluation setups combine automated scoring for consistency with human judgment for nuance. For example, intelligence and accuracy can be benchmarked with automated reasoning tests or evaluated through LLM judges reviewing reasoning traces, while user experience is best captured through direct human feedback, surveys, or A/B testing. Performance and efficiency depend heavily on real-time monitoring, tracking metrics like latency, token costs, and throughput under varying loads. Reliability and resilience require stress and failure testing, deliberately injecting noise, simulating API outages, or running long-session interactions to uncover hidden weak spots. Responsibility and governance, meanwhile, need ethical stress testing through red teaming, safety classifiers, and compliance audits to ensure agents operate safely within organizational and legal boundaries.

In short, evaluating an AI agent isn’t about a single benchmark or static test suite, it’s about building a continuous evaluation pipeline: One that measures intelligence, performance, reliability, responsibility, and user trust together, because a truly production-ready agent must not only be smart, but also fast, stable, safe, and trusted by the humans who use it.

A detailed tools-and-frameworks comparison is beyond the scope of this article, but Figure 3 provides a quick orientation to the ecosystem. The tools listed below map directly to the three evaluation patterns on which we focus: LLM-as-a-judge scoring (LangChain Evals, OpenAI Evals, and TruLens), trace-based analysis (MLflow and OpenTelemetry), and safety/governance testing (Guardrails AI andMS Responsible AI). Treat this as a starting point for your own tooling decisions, not an exhaustive landscape review.

|     |     |     |     |
| --- | --- | --- | --- |
| **Category** | **Tool** | **Key Features** | **Primary Use** |
| Tracking & Observability | MLflow 3.0 | Experiment tracking, GenAI tracing, built-in LLM judges. | Agent run logging, trace comparison |
|  | Weights & Biases (W&B) | Dashboards, visual analytics | Training/evaluation monitoring |
|  | OpenTelemetry | Distributed tracing, system metrics | Latency, API call tracking |
| Evaluation & Metrics | TruLens | Feedback framework, trusted metrics | Hybrid evaluation, trust scoring |
|  | LangChain Evals | Automated test chains | Reasoning quality testing |
|  | OpenAI Evals | Model comparison framework | Version/configuration comparison |
|  | Ragas | RAG system evaluation | Document retrieval assessment |
| Safety & Governance | Guardrails AI | Safety constraints, policy enforcement | Response validation, harm prevention |
|  | MS Responsible AI | Fairness, interpretability analysis | Bias auditing, explainability |

**Figure 3. Tools and frameworks.**

These concepts become clearer when applied to an executable workflow. The following section presents a concise evaluation example using Claude and LangChain, showing how automated judges can score agent responses for usefulness and correctness in a controlled, repeatable way.

## Eval Example with Claude + LangChain

We now look at a minimal example of LLM-as-a-judge, which operates in two modes: reference-free (e.g., helpfulness, clarity, and relevance) and reference-aware (e.g., correctness vs. a gold answer). The example below evaluates a single QA item with Claude Sonnet 4.5+, producing a helpfulness score and a correctness score against the reference, using a versioned model and `temperature=0` for reproducibility.

### Prerequisites

Running this example requires a valid Anthropic API key (set as the `ANTHROPIC_API_KEY` environment variable) and a few Python packages (`langchain`, `langchain-anthropic`). The notebook runs in any local Jupyter environment or in Google Colab, though note that Colab requires you to set your API key via Colab Secrets or inline environment configuration – do not hardcode keys in shared notebooks. For full setup instructions, including pinned package versions and known compatibility notes, see the Prerequisites section in the [repository README](https://github.com/infosysamit/ai-agent-eval-blueprint).

For readability, we include only focused snippets below. The full python code is in a [Jupyter notebook file](https://github.com/infosysamit/ai-agent-eval-blueprint).

```python
# Minimal, one-sample evaluation with Claude + LangChain
# Goal: show BOTH reference-free (helpfulness) and reference-aware (correctness) scoring.

from langchain_anthropic import ChatAnthropic
from langchain.evaluation import load_evaluator

# 1) Pick a stable, versioned Claude model (use your tenant's ID/alias if different).
llm = ChatAnthropic(model="claude-sonnet-4-5-20250929", temperature=0)

# 2) One gold sample keeps the snippet readable for the paper.
item = {
    "question": "Define TTFT.",
    "reference": "Time-to-first-token: latency from request start to first token."
}

# 3) System-under-test: tiny, deterministic call to Claude.
def predict(q: str) -> str:
    return llm.invoke([("system", "Answer concisely."), ("human", q)]).content

pred = predict(item["question"])

# 4) Evaluators:
#    - "criteria": reference-free (UX-style qualities like helpfulness).
#    - "labeled_criteria": reference-aware (fact checks vs. the reference).
crit_eval = load_evaluator(
    "criteria",
    llm=llm,
    criteria={"helpfulness": "Is the answer practically useful and clear?"}
)
lab_eval = load_evaluator(
    "labeled_criteria",
    llm=llm,
    criteria={"correctness": "Is the answer correct given the reference?"}
)

# 5) Get scores (+ rationales). Keys can vary slightly across LC versions - use .get().
res_help = crit_eval.evaluate_strings(prediction=pred, input=item["question"])
res_corr = lab_eval.evaluate_strings(
    prediction=pred, input=item["question"], reference=item["reference"]
)

help_score = res_help.get("score")
# Note: LangChain evaluator output keys can vary across versions - some return
# "reasoning", others "explanation". Using .get() with a fallback handles both
help_note  = res_help.get("reasoning") or res_help.get("explanation")
corr_score = res_corr.get("score")
corr_note  = res_corr.get("reasoning") or res_corr.get("explanation")

# 6) Reviewer-friendly printout (fits in logs and manuscripts).
print(
    f"\n{'='*64}\n"
    f"Q: {item['question']}\n\n"
    f"Prediction:\n{pred}\n\n"
    f"Helpfulness: {help_score} - {help_note}\n"
    f"Correctness: {corr_score} - {corr_note}\n"
)
```

This snippet performs an LLM-as-a-judge evaluation on a single QA item with Claude Sonnet 4.5, producing a reference-free helpfulness score and a reference-aware correctness score. We pin a versioned model and set temperature=0 for reproducibility; the same pattern scales to larger datasets and can be paired with MLflow for latency/TTFT/tokens.

Here is what the console output or notebook execution result would be if we use Jupyter notebook.

```python
================================================================
Q: Define TTFT.

Prediction:
**TTFT** stands for **Time To First Token**.

It's a performance metric that measures the latency between when a user submits a request to a language model (LLM) or AI system and when the first token of the response is generated and returned to the user.

TTFT is important because:
- It affects perceived responsiveness and user experience
- Lower TTFT means users see output starting sooner
- It's particularly critical for streaming responses where users want immediate feedback

TTFT is influenced by factors like model size, prompt length, server load, and infrastructure efficiency.

Helpfulness: 1 - Let me analyze whether this submission meets the helpfulness criterion by evaluating if it is practically useful and clear.

**Step-by-step reasoning:**

1. **Does it define the term clearly?**
   - Yes, it explicitly states "TTFT stands for Time To First Token"
   - The definition is straightforward and unambiguous

2. **Does it explain what the term means in practical terms?**
   - Yes, it describes it as "a performance metric that measures the latency between when a user submits a request to a language model (LLM) or AI system and when the first token of the response is generated"
   - This provides concrete understanding of what is being measured

3. **Does it provide context for why this matters?**
   - Yes, it explains the importance through multiple points:
     - Affects user experience
     - Lower TTFT means faster perceived response
     - Critical for streaming responses
   - This helps the reader understand practical relevance

4. **Is the information organized clearly?**
   - Yes, it follows a logical structure: definition → explanation → importance → influencing factors
   - Uses bullet points for easy scanning
   - Well-formatted with bold text for the acronym

5. **Does it provide additional useful information?**
   - Yes, it mentions factors that influence TTFT (model size, prompt length, server load, infrastructure)
   - This adds practical value for someone trying to understand or optimize TTFT

6. **Is the language accessible?**
   - Yes, the explanation avoids unnecessary jargon while remaining technically accurate
   - Clear and concise

The submission is both practically useful (provides actionable understanding of the concept) and clear (well-organized, easy to understand).

Y
Correctness: 1 - Let me analyze whether the submission meets the correctness criterion by comparing it to the reference answer.

**Step-by-step reasoning:**

1. **Core Definition Check:**
   - Reference states: "Time-to-first-token: latency from request start to first token"
   - Submission states: "measures the latency between when a user submits a request to a language model (LLM) or AI system and when the first token of the response is generated and returned to the user"
   - These definitions align - both describe TTFT as the latency/time from when a request starts until the first token is received.

2. **Acronym Expansion:**
   - Reference implies: "Time-to-first-token" (hyphenated)
   - Submission states: "Time To First Token" (no hyphens)
   - This is a minor stylistic difference but conveys the same meaning.

3. **Additional Information:**
   - The submission provides extra context about why TTFT is important, what factors influence it, and its relevance to user experience
   - The reference doesn't contradict any of this additional information
   - Adding correct supplementary information doesn't make an answer incorrect

4. **Accuracy of Core Concept:**
   - Both answers correctly identify TTFT as a latency metric
   - Both correctly identify it measures from request start to first token
   - The submission's additional details about it being used in LLM/AI contexts are accurate and relevant

**Conclusion:**
The submission correctly defines TTFT in alignment with the reference answer. The core definition matches, and the additional explanatory information is accurate and helpful rather than incorrect or contradictory.

Y
```

### Interpreting the Evaluation Output

The output illustrates two complementary evaluation modes and how to interpret them. The reference-free helpfulness score assesses whether the response is clear, structured, and practically useful, independent of any gold answer; here, the judge finds the definition well-organized, accessible, and enriched with practical context (i.e., why TTFT matters for perceived latency/streaming UX, in addition to influencing factors such as model size, prompt length, server load, and infrastructure). The reference-aware correctness score compares the generated response against the provided reference (latency from request start to first token) and confirms the core definition matches, with the added explanation remaining accurate and non-contradictory. Together, these results show how LLM-as-a-judge evaluation can validate both quality of explanation and factual alignment. If a numeric score appears as 1, it reflects the evaluator’s scoring scale or a binary/pass-fail configuration (and may require normalization or remapping for dashboards); you may also see a Y/N verdict where Y indicates the criterion is satisfied and N indicates it is not.

### A Note one Scoring Scales

LangChain's built-in criteria evaluators default to a binary scale, where 1 indicates criteria have been met and 0 indicates criteria have not been met, which is often accompanied by a Y/N verdict. This verdict is configurable. You can define custom evaluators that use a 1 to 5 Likert scale (useful for grading nuance in helpfulness or tone), a 0 to 10 numeric range (common in production dashboards), or any scale that fits your reporting needs. When scaling to larger datasets or integrating with dashboards, standardize early: Pick and document one scoring convention across all evaluators and apply normalization if you're mixing scores from different evaluator types or scales. For example, if one evaluator returns binary 0/1 and another returns a 1 to 5 rating, normalizing both to a 0 to 1 float range makes aggregate comparison and threshold-setting straightforward.

## Lessons Learned in Practice

Building and evaluating AI agents reveals a consistent truth: Intelligence is easy to demonstrate, but hard to sustain. While our examples have centered on e-commerce operations, these lessons generalize to any domain where tool-using agents operate under real-world constraints: customer support, financial services, DevOps, content moderation, and beyond. In our experiments and explorations, we have seen agents perform flawlessly in controlled settings, only to falter once deployed in dynamic, unpredictable environments. From those hard-earned experiences, a few key lessons stand out:

- **Controlled performance doesn’t equal real-world readiness.**


AI agents often excel in lab settings where conditions are well-defined, datasets are curated, and objectives are unambiguous. But once those same agents face real-world variability, noisy sensor data, ambiguous goals, or changing contexts, accuracy alone no longer guarantees success. Evaluation must therefore move beyond task-specific metrics and focus on adaptability, how well an agent adjusts, learns, and recovers in non-ideal situations.
- **Hybrid evaluation is essential**.


Purely quantitative benchmarks don’t capture the complexity of intelligent behavior. The best evaluations blend automated measurement with human insight. Simulation-based testing and automated scoring give scale and consistency, while human evaluators uncover qualitative aspects, judgment, intent alignment, and contextual decision quality. Whether you’re testing a conversational agent, a robotics controller, or an AI planner, pairing algorithmic evaluation with experiential observation yields far deeper insight.
- **Reliability is more valuable than brilliance**.


Many AI systems can perform impressive feats once, but few can do it reliably a thousand times. True progress lies in stability under variation, testing how agents respond when environments shift, sensors fail, or inputs degrade. Reliability testing, through random perturbations, fault injection, or long-horizon simulation, exposes how robustly the agent handles uncertainty. In production, reliability earns more trust than raw intelligence.
- **Efficiency defines viability**.


For AI agents that act autonomously in the physical or digital world, speed and resource efficiency are not luxuries but necessities. An agent that overcomputes, reacts too slowly, or consumes excessive energy, tokens, or duration becomes impractical at scale. Continuous runtime profiling, tracking latency, energy use, and throughput help ensure agents are not only smart but operationally sustainable.
- **Safety, ethics, and governance are non-negotiable**.


As AI agents take on real-world decisions, from driving cars to approving loans to moderating content, their evaluation must extend beyond technical performance. Testing for safe behavior, bias resilience, and ethical alignment is now as critical as accuracy testing. Red teaming, bias audits, and explainability reviews aren’t checkboxes, they are the backbone of trustworthy autonomy.

## Conclusion

The most successful AI teams have learned that evaluation isn't a milestone, it's a continuous discipline. In this article, we discussed why agent evaluation is fundamentally different from standard LLM benchmarking: Agents plan, call tools, maintain state, and behave across multiple turns, so they must be evaluated as systems, not just as text generators. We introduced five pillars for production readiness, intelligence and accuracy, performance and efficiency, reliability and resilience, responsibility and governance, and user experience. We then mapped each pillar to practical evaluation methods, from automated scoring and tracing to stress testing, fault injection, red teaming, and human review. We also demonstrated how LLM-as-a-judge can be used to score both reference-free qualities (e.g., helpfulness) and reference-aware correctness in a reproducible way.

Five takeaways stand out. First, agents are systems, so evaluate them as such, not as standalone models. Second, behavior beats benchmarks: Task success, recovery, and consistency under real variability matter more than single-turn accuracy. Third, hybrid evaluation wins because automated metrics provide repeatability at scale, while human judgment captures nuance in trust and usability. Fourth, operational constraints define viability: Latency, cost, tool reliability, and policy compliance are first-class evaluation targets, not afterthoughts. Finally, safety, governance, and user trust complete the picture: Red teaming, PII handling, permission boundaries, and user experience scoring are as essential as any accuracy metric. Building a continuous evaluation pipeline across these five dimensions is what separates demonstration-grade agents from production-ready systems.

### Disclaimer

The views and opinions expressed in this article are solely those of the author and do not represent the author’s employer or affiliates. Examples are illustrative; no confidential or proprietary information is disclosed.

</details>

<details>
<summary>Function calling using LLMs</summary>

# Function calling using LLMs

Building AI Agents that interact with the external world.

_While LLMs excel at generating cogent text based on their training_
_data, they may also need to interact with external systems. Function_
_calling allows them to construct such calls. The LLM does not execute these_
_calls directly, instead it creates a data structure that describes the call,_
_passing that to a separate program for execution and further processing. The_
_LLM's prompt includes details about possible function calls and when they_
_should be used._

One of the key applications of LLMs is to enable programs (agents) that
can interpret user intent, reason about it, and take relevant actions
accordingly.

**Function calling** is a capability that enables LLMs to go beyond
simple text generation by interacting with external tools and real-world
applications. With function calling, an LLM can analyze a natural language
input, extract the user’s intent, and generate a structured output
containing the function name and the necessary arguments to invoke that
function.

It’s important to emphasize that when using function calling, the LLM
itself does not execute the function. Instead, it identifies the appropriate
function, gathers all required parameters, and provides the information in a
structured JSON format. This JSON output can then be easily deserialized
into a function call in Python (or any other programming language) and
executed within the program’s runtime environment.

https://martinfowler.com/articles/function-call-LLM/image2.png

Figure 1: natural langauge request to structured output

To see this in action, we’ll build a _Shopping Agent_ that helps users
discover and shop for fashion products. If the user’s intent is unclear, the
agent will prompt for clarification to better understand their needs.

For example, if a user says _“I’m looking for a shirt”_ or _“Show me_
_details about the blue running shirt,”_ the shopping agent will invoke the
appropriate API—whether it’s searching for products using keywords or
retrieving specific product details—to fulfill the request.

## Scaffold of a typical agent

Let's write a scaffold for building this agent. (All code examples are
in Python.)

```
class ShoppingAgent:

    def run(self, user_message: str, conversation_history: List[dict]) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        action = self.decide_next_action(user_message, conversation_history)
        return action.execute()

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        pass

    def is_intent_malicious(self, message: str) -> bool:
        pass
```

Based on the user’s input and the conversation history, the
shopping agent selects from a predefined set of possible actions, executes
it and returns the result to the user. It then continues the conversation
until the user’s goal is achieved.

Now, let’s look at the possible actions the agent can take:

```
class Search():
    keywords: List[str]

    def execute(self) -> str:
        # use SearchClient to fetch search results based on keywords
        pass

class GetProductDetails():
    product_id: str

    def execute(self) -> str:
 # use SearchClient to fetch details of a specific product based on product_id
        pass

class Clarify():
    question: str

    def execute(self) -> str:
        pass
```

## Unit tests

Let's start by writing some unit tests to validate this functionality
before implementing the full code. This will help ensure that our agent
behaves as expected while we flesh out its logic.

```
def test_next_action_is_search():
    agent = ShoppingAgent()
    action = agent.decide_next_action("I am looking for a laptop.", [])
    assert isinstance(action, Search)
    assert 'laptop' in action.keywords

def test_next_action_is_product_details(search_results):
    agent = ShoppingAgent()
    conversation_history = [\
        {"role": "assistant", "content": f"Found: Nike dry fit T Shirt (ID: p1)"}\
    ]
    action = agent.decide_next_action("Can you tell me more about the shirt?", conversation_history)
    assert isinstance(action, GetProductDetails)
    assert action.product_id == "p1"

def test_next_action_is_clarify():
    agent = ShoppingAgent()
    action = agent.decide_next_action("Something something", [])
    assert isinstance(action, Clarify)
```

Let's implement the `decide_next_action` function using OpenAI's API
and a GPT model. The function will take user input and conversation
history, send it to the model, and extract the action type along with any
necessary parameters.

```
def decide_next_action(self, user_message: str, conversation_history: List[dict]):
    response = self.client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[\
            {"role": "system", "content": SYSTEM_PROMPT},\
            *conversation_history,\
            {"role": "user", "content": user_message}\
        ],
        tools=[\
            {"type": "function", "function": SEARCH_SCHEMA},\
            {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},\
            {"type": "function", "function": CLARIFY_SCHEMA}\
        ]
    )

    tool_call = response.choices[0].message.tool_calls[0]
    function_args = eval(tool_call.function.arguments)

    if tool_call.function.name == "search_products":
        return Search(**function_args)
    elif tool_call.function.name == "get_product_details":
        return GetProductDetails(**function_args)
    elif tool_call.function.name == "clarify_request":
        return Clarify(**function_args)
```

Here, we are calling OpenAI’s chat completion API with a system prompt
that directs the LLM, in this case `gpt-4-turbo-preview` to determine the
appropriate action and extract the necessary parameters based on the
user’s message and the conversation history. The LLM returns the output as
a structured JSON response, which is then used to instantiate the
corresponding action class. This class executes the action by invoking the
necessary APIs, such as `search` and `get_product_details`.

## System prompt

Now, let’s take a closer look at the system prompt:

```
SYSTEM_PROMPT = """You are a shopping assistant. Use these functions:
1. search_products: When user wants to find products (e.g., "show me shirts")
2. get_product_details: When user asks about a specific product ID (e.g., "tell me about product p1")
3. clarify_request: When user's request is unclear"""
```

With the system prompt, we provide the LLM with the necessary context
for our task. We define its role as a _shopping assistant_, specify the
expected _output format_ (functions), and include _constraints and_
_special instructions_, such as asking for clarification when the user's
request is unclear.

This is a basic version of the prompt, sufficient for our example.
However, in real-world applications, you might want to explore more
sophisticated ways of guiding the LLM. Techniques like **One-shot**
**prompting**—where a single example pairs a user message with the
corresponding action—or **Few-shot prompting**—where multiple examples
cover different scenarios—can significantly enhance the accuracy and
reliability of the model’s responses.

This part of the Chat Completions API call defines the available
functions that the LLM can invoke, specifying their structure and
purpose:

```
tools=[\
    {"type": "function", "function": SEARCH_SCHEMA},\
    {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},\
    {"type": "function", "function": CLARIFY_SCHEMA}\
]
```

Each entry represents a function the LLM can call, detailing its
expected parameters and usage according to the _OpenAI API_
_specification_.

Now, let’s take a closer look at each of these function schemas.

```
SEARCH_SCHEMA = {
    "name": "search_products",
    "description": "Search for products using keywords",
    "parameters": {
        "type": "object",
        "properties": {
            "keywords": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Keywords to search for"
            }
        },
        "required": ["keywords"]
    }
}

PRODUCT_DETAILS_SCHEMA = {
    "name": "get_product_details",
    "description": "Get detailed information about a specific product",
    "parameters": {
        "type": "object",
        "properties": {
            "product_id": {
                "type": "string",
                "description": "Product ID to get details for"
            }
        },
        "required": ["product_id"]
    }
}

CLARIFY_SCHEMA = {
    "name": "clarify_request",
    "description": "Ask user for clarification when request is unclear",
    "parameters": {
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "Question to ask user for clarification"
            }
        },
        "required": ["question"]
    }
}
```

With this, we define each function that the LLM can invoke, along with
its parameters—such as `keywords` for the “search” function and
`product_id` for `get_product_details`. We also specify which
parameters are mandatory to ensure proper function execution.

Additionally, the `description` field provides extra context to
help the LLM understand the function's purpose, especially when the
function name alone isn’t self-explanatory.

With all the key components in place, let's now fully implement the
`run` function of the `ShoppingAgent` class. This function will
handle the end-to-end flow—taking user input, deciding the next action
using OpenAI’s function calling, executing the corresponding API calls,
and returning the response to the user.

Here’s the complete implementation of the agent:

```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI()

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        try:
            action = self.decide_next_action(user_message, conversation_history or [])
            return action.execute()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[\
                {"role": "system", "content": SYSTEM_PROMPT},\
                *conversation_history,\
                {"role": "user", "content": user_message}\
            ],
            tools=[\
                {"type": "function", "function": SEARCH_SCHEMA},\
                {"type": "function", "function": PRODUCT_DETAILS_SCHEMA},\
                {"type": "function", "function": CLARIFY_SCHEMA}\
            ]
        )

        tool_call = response.choices[0].message.tool_calls[0]
        function_args = eval(tool_call.function.arguments)

        if tool_call.function.name == "search_products":
            return Search(**function_args)
        elif tool_call.function.name == "get_product_details":
            return GetProductDetails(**function_args)
        elif tool_call.function.name == "clarify_request":
            return Clarify(**function_args)

    def is_intent_malicious(self, message: str) -> bool:
        pass
```

## Restricting the agent's action space

It's essential to restrict the agent's action space using
explicit conditional logic, as demonstrated in the above code block.
While dynamically invoking functions using `eval` might seem
convenient, it poses significant security risks, including prompt
injections that could lead to unauthorized code execution. To safeguard
the system from potential attacks, always enforce strict control over
which functions the agent can invoke.

## Guardrails against prompt injections

When building a user-facing agent that communicates in natural language and performs background actions via function calling, it's critical to anticipate adversarial behavior. Users may intentionally try to bypass safeguards and trick the agent into taking unintended actions—like SQL injection, but through language.


A common attack vector involves prompting the agent to reveal its system prompt, giving the attacker insight into how the agent is instructed. With this knowledge, they might manipulate the agent into performing actions such as issuing unauthorized refunds or exposing sensitive customer data.


While restricting the agent’s action space is a solid first step, it’s not sufficient on its own.

To enhance protection, it's essential to sanitize user input to detect and prevent malicious intent. This can be approached using a combination of:

- Traditional techniques, like regular expressions and input denylisting, to filter known malicious patterns.
- LLM-based validation, [where another model screens inputs](https://martinfowler.com/articles/gen-ai-patterns/#guardrails) for signs of manipulation, injection attempts, or prompt exploitation.

Here’s a simple implementation of a denylist-based guard that flags potentially malicious input:

```
def is_intent_malicious(self, message: str) -> bool:
    suspicious_patterns = [\
        "ignore previous instructions",\
        "ignore above instructions",\
        "disregard previous",\
        "forget above",\
        "system prompt",\
        "new role",\
        "act as",\
        "ignore all previous commands"\
    ]
    message_lower = message.lower()
    return any(pattern in message_lower for pattern in suspicious_patterns)
```

This is a basic example, but it can be extended with regex matching, contextual checks, or integrated with an LLM-based filter for more nuanced detection.


Building robust prompt injection guardrails is essential for maintaining the safety and integrity of your agent in real-world scenarios

## Action classes

This is where the action really happens! **Action classes** serve as
the gateway between the LLM’s decision-making and actual system
operations. They translate the LLM’s interpretation of the user’s
request—based on the conversation—into concrete actions by invoking the
appropriate APIs from your microservices or other internal systems.

```
class Search:
    def __init__(self, keywords: List[str]):
        self.keywords = keywords
        self.client = SearchClient()

    def execute(self) -> str:
        results = self.client.search(self.keywords)
        if not results:
            return "No products found"
        products = [f"{p['name']} (ID: {p['id']})" for p in results]
        return f"Found: {', '.join(products)}"

class GetProductDetails:
    def __init__(self, product_id: str):
        self.product_id = product_id
        self.client = SearchClient()

    def execute(self) -> str:
        product = self.client.get_product_details(self.product_id)
        if not product:
            return f"Product {self.product_id} not found"
        return f"{product['name']}: price: ${product['price']} - {product['description']}"

class Clarify:
    def __init__(self, question: str):
        self.question = question

    def execute(self) -> str:
        return self.question
```

In my implementation, the conversation history is stored in the
user interface’s session state and passed to the `run` function on
each call. This allows the shopping agent to retain context from
previous interactions, enabling it to make more informed decisions
throughout the conversation.

For example, if a user requests details about a specific product, the
LLM can extract the `product_id` from the most recent message that
displayed the search results, ensuring a seamless and context-aware
experience.

Here’s an example of how a typical conversation flows in this simple
shopping agent implementation:

https://martinfowler.com/articles/function-call-LLM/image1.png

Figure 2: Conversation with the shopping agent

## Refactoring to reduce boiler plate

A significant portion of the verbose boilerplate code in the
implementation comes from defining detailed function specifications for
the LLM. You could argue that this is redundant, as the same information
is already present in the concrete implementations of the action
classes.

Fortunately, libraries like [instructor](https://pypi.org/project/instructor/) help reduce
this duplication by providing functions that can automatically serialize
Pydantic objects into JSON following the OpenAI schema. This reduces
duplication, minimizes boilerplate code, and improves maintainability.

Let’s explore how we can simplify this implementation using
instructor. The key change
involves defining action classes as _Pydantic_ objects, like so:

```
from typing import List, Union
from pydantic import BaseModel, Field
from instructor import OpenAISchema
from neo.clients import SearchClient

class BaseAction(BaseModel):
    def execute(self) -> str:
        pass

class Search(BaseAction):
    keywords: List[str]

    def execute(self) -> str:
        results = SearchClient().search(self.keywords)
        if not results:
            return "Sorry I couldn't find any products for your search."

        products = [f"{p['name']} (ID: {p['id']})" for p in results]
        return f"Here are the products I found: {', '.join(products)}"

class GetProductDetails(BaseAction):
    product_id: str

    def execute(self) -> str:
        product = SearchClient().get_product_details(self.product_id)
        if not product:
            return f"Product {self.product_id} not found"

        return f"{product['name']}: price: ${product['price']} - {product['description']}"

class Clarify(BaseAction):
    question: str

    def execute(self) -> str:
        return self.question

class NextActionResponse(OpenAISchema):
    next_action: Union[Search, GetProductDetails, Clarify] = Field(
        description="The next action for agent to take.")
```

The agent implementation is updated to use NextActionResponse, where
the `next_action` field is an instance of either Search, GetProductDetails,
or Clarify action classes. The `from_response` method from the instructor
library simplifies deserializing the LLM’s response into a
NextActionResponse object, further reducing boilerplate code.

```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."
        try:
            action = self.decide_next_action(user_message, conversation_history or [])
            return action.execute()
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[\
                {"role": "system", "content": SYSTEM_PROMPT},\
                *conversation_history,\
                {"role": "user", "content": user_message}\
            ],
            tools=[{\
                "type": "function",\
                "function": NextActionResponse.openai_schema\
            }],
            tool_choice={"type": "function", "function": {"name": NextActionResponse.openai_schema["name"]}},
        )
        return NextActionResponse.from_response(response).next_action

    def is_intent_malicious(self, message: str) -> bool:
        suspicious_patterns = [\
            "ignore previous instructions",\
            "ignore above instructions",\
            "disregard previous",\
            "forget above",\
            "system prompt",\
            "new role",\
            "act as",\
            "ignore all previous commands"\
        ]
        message_lower = message.lower()
        return any(pattern in message_lower for pattern in suspicious_patterns)
```

## Can this pattern replace traditional rules engines?

[Rules engines](https://martinfowler.com/bliki/RulesEngine.html) have long held sway in enterprise software architecture, but in
practice, they rarely live up their promise. Martin Fowler’s observation about them from over
15 years ago still rings true:

> Often the central pitch for a rules engine is that it will allow the business people to specify the rules themselves, so they can build the rules without involving programmers. As so often, this can sound plausible but rarely works out in practice

The core issue with rules engines lies in their complexity over time. As the number of rules grows, so does the risk of unintended interactions between them. While defining individual rules in isolation — often via drag-and-drop tools might seem simple and manageable, problems emerge when the rules are executed together in real-world scenarios. The combinatorial explosion of rule interactions makes these systems increasingly difficult to test, predict and maintain.


LLM-based systems offer a compelling alternative. While they don’t yet provide full transparency or determinism in their decision making, they can reason about user intent and context in a way that traditional static rule sets cannot. Instead of rigid rule chaining, you get context-aware, adaptive behaviour driven by language understanding. And for business users or domain experts, expressing rules through natural language prompts may actually be more intuitive and accessible than using a rules engine that ultimately generates hard-to-follow code.


A practical path forward might be to combine LLM-driven reasoning with explicit manual gates for executing critical decisions—striking a balance between flexibility, control, and safety


## Function calling vs Tool calling

While these terms are often used interchangeably, “tool calling” is the more general and modern term. It refers to broader set of capabilities that LLMs can use to interact with the outside world. For example, in addition to calling custom functions, an LLM might offer inbuilt tools like code interpreter ( for executing code ) and retrieval mechanisms ( for accessing data from uploaded files or connected databases ).

## How Function calling relates to MCP ( Model Context Protocol )

[The Model Context Protocol ( MCP )](https://modelcontextprotocol.io/introduction) is an open protocol proposed by Anthropic that's gaining traction as a standardized way to structure how LLM-based applications interact with the external world. [A growing number of software as a service providers](https://github.com/modelcontextprotocol/servers) are now exposing their service to LLM Agents using this protocol.

MCP defines a client-server architecture with three main components:

https://martinfowler.com/articles/function-call-LLM/mcp.svg

Figure 3: High level architecture - shopping agent using MCP

- MCP Server: A server that exposes data sources and various tools (i.e functions) that can be invoked over HTTP
- MCP Client: A client that manages communication between an application and the MCP Server
- MCP Host: The LLM-based application (e.g our “ShoppingAgent”) that uses the data and tools provided by the MCP Server to accomplish a task (fulfill user's shopping request). The MCPHost accesses these capabilities via the MCPClient

The core problem MCP addresses is flexibility and dynamic tool discovery. In our above example of “ShoppingAgent”, you may notice that the set of available tools is hardcoded to three functions the agent can invoke i.e `search_products`, `get_product_details` and `clarify`. This in a way, limits the agent's ability to adapt or scale to new types of requests, but inturn makes it easier to secure it agains malicious usage.

With MCP, the agent can instead query the MCPServer at runtime to discover which tools are available. Based on the user's query, it can then choose and invoke the appropriate tool dynamically.

This model decouples the LLM application from a fixed set of tools, enabling modularity, extensibility, and dynamic capability expansion - which is especially valuable for complex or evolving agent systems.

Although MCP adds extra complexity, there are certain applications (or agents) where that complexity is justified. For example, LLM-based IDEs or code generation tools need to stay up to date with the latest APIs they can interact with. In theory, you could imagine a general-purpose agent with access to a wide range of tools, capable of handling a variety of user requests — unlike our example, which is limited to shopping-related tasks.

Let's look at what a simple MCP server might look like for our shopping application. Notice the `GET /tools`endpoint - it returns a list of all the functions (or tools) that server is making available.

```
TOOL_REGISTRY = {
    "search_products": SEARCH_SCHEMA,
    "get_product_details": PRODUCT_DETAILS_SCHEMA,
    "clarify": CLARIFY_SCHEMA
}

@app.route("/tools", methods=["GET"])
def get_tools():
    return jsonify(list(TOOL_REGISTRY.values()))

@app.route("/invoke/search_products", methods=["POST"])
def search_products():
    data = request.json
    keywords = data.get("keywords")
    search_results = SearchClient().search(keywords)
    return jsonify({"response": f"Here are the products I found: {', '.join(search_results)}"})

@app.route("/invoke/get_product_details", methods=["POST"])
def get_product_details():
    data = request.json
    product_id = data.get("product_id")
    product_details = SearchClient().get_product_details(product_id)
    return jsonify({"response": f"{product_details['name']}: price: ${product_details['price']} - {product_details['description']}"})

@app.route("/invoke/clarify", methods=["POST"])
def clarify():
    data = request.json
    question = data.get("question")
    return jsonify({"response": question})

if __name__ == "__main__":
    app.run(port=8000)
```

And here's the corresponding MCP client, which handles communication between the MCP host (ShoppingAgent) and the server:

```
class MCPClient:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")

    def get_tools(self):
        response = requests.get(f"{self.base_url}/tools")
        response.raise_for_status()
        return response.json()

    def invoke(self, tool_name, arguments):
        url = f"{self.base_url}/invoke/{tool_name}"
        response = requests.post(url, json=arguments)
        response.raise_for_status()
        return response.json()
```

Now let's refactor our `ShoppingAgent` (the MCP Host) to first retrieve the list of available tools from the MCP server, and then invoke the appropriate function using the MCP client.

```
class ShoppingAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.mcp_client = MCPClient(os.getenv("MCP_SERVER_URL"))
        self.tool_schemas = self.mcp_client.get_tools()

    def run(self, user_message: str, conversation_history: List[dict] = None) -> str:
        if self.is_intent_malicious(user_message):
            return "Sorry! I cannot process this request."

        try:
            tool_call = self.decide_next_action(user_message, conversation_history or [])
            result = self.mcp_client.invoke(tool_call["name"], tool_call["arguments"])
            return str(result["response"])

        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}"

    def decide_next_action(self, user_message: str, conversation_history: List[dict]):
        response = self.client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[\
                {"role": "system", "content": SYSTEM_PROMPT},\
                *conversation_history,\
                {"role": "user", "content": user_message}\
            ],
            tools=[{"type": "function", "function": tool} for tool in self.tool_schemas],
            tool_choice="auto"
        )
        tool_call = response.choices[0].message.tool_call
        return {
            "name": tool_call.function.name,
            "arguments": tool_call.function.arguments.model_dump()
        }

        def is_intent_malicious(self, message: str) -> bool:
            pass
```

## Conclusion

Function calling is an exciting and powerful capability of LLMs that opens the door to novel user experiences and development of sophisticated agentic systems. However, it also introduces new risks—especially when user input can ultimately trigger sensitive functions or APIs. With thoughtful guardrail design and proper safeguards, many of these risks can be effectively mitigated. It's prudent to start by enabling function calling for low-risk operations and gradually extend it to more critical ones as safety mechanisms mature.

</details>


## Code Sources

<details>
<summary>Repository analysis for https://github.com/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb</summary>

# Repository analysis for https://github.com/openai/openai-cookbook/blob/main/examples/gpt-5/gpt-5_prompting_guide.ipynb

## Summary
Repository: openai/openai-cookbook
Commit: 34c5048a2a5bdcb7e169254b7e23ec7f12e134ec
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
<summary>[00:00] What is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data such as databases or APIs. Typically, you use tool calling via a chat interface. (The speaker, Roy Derks, stands in front of a black board, holding a marker. Text "IBM Technology" appears in the top left corner. He starts writing on the board.)</summary>

[00:00] What is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data such as databases or APIs. Typically, you use tool calling via a chat interface. (The speaker, Roy Derks, stands in front of a black board, holding a marker. Text "IBM Technology" appears in the top left corner. He starts writing on the board.)

[00:13] So you would have your client application in one hand, (He draws a vertical line on the left side of the board and writes "APP" at the top.) and then the LLM on the other side. (He draws another vertical line on the right side of the board and writes "LLM" at the top. He then writes "chat" centered above the top of the two vertical lines.)

[00:23] From your client application, you would send a set of messages together with a tool definition to the LLM. (He draws a horizontal arrow from the "APP" column to the "LLM" column.) So you would have your messages here (He writes "messages" above the arrow.) together with your list of tools. (He adds "+ tools" next to "messages" above the arrow.)

[00:37] The LLM will look at both your message and the list of tools and it's going to recommend a tool you should call. (He draws a horizontal arrow pointing back from the "LLM" column to the "APP" column.) So this tool to call (He writes "tool to call" below the return arrow.)

[00:47] from your client application, you should call this tool and then supply the answer back to the LLM. (He draws another horizontal arrow from "APP" to "LLM".) So this tool response will be interpreted by the LLM. (He writes "tool response" below the arrow.) And this will either tell you the next tool to call or it will give you the final answer. (He draws a final horizontal arrow from "LLM" back to "APP".)

[01:03] In your application, you're responsible for creating the tool definition. (He draws a box around "APP" and adds a new section inside it, writing "tool definition".) So this tool definition includes a couple of things such as the name of every tool. (He writes "- name" under "tool definition".) It also includes a description for the tool. (He writes "- description" under "name".) So this is where you can give additional information about how to use the tool or when to use it. And it also includes the input parameters needed to make a tool call. (He writes "- input" under "description".)

[01:25] And the tools can be anything. So the tools could be APIs or databases. (He draws a box below the "APP" box and writes "tools" inside it. Then he draws three circles connected to the "tools" box, labeling them "API", "DB", and "code".) It could also be code that you interpret via code interpreter.

*Tool calling enables an LLM to be context-aware by interacting with external tools like APIs or databases, with the application acting as an intermediary to execute tool calls based on LLM recommendations.*

[01:40] So let's look at an example. Assume you want to find the weather in Miami. You might ask the LLM about the temperature in Miami. (He writes "temp in Miami?" next to "messages + tools" on the first arrow.) You also provide a list of tools, and one of these tools is the weather API. (He writes "Weather API" next to "messages + tools".)

[01:56] The LLM will look at both your question, which is what is the temperature in Miami, it will also look at the weather API, and then based on the tool definition for the weather API, it's going to tell you how to call the weather tool. So in here, it's going to create a tool that you can use right here on this side, where you call the API to collect the weather information. (He gestures towards the "tool to call" arrow from LLM to APP, and the "API" circle under the "tools" box.) You would then supply the weather information back to the LLM. So let's say it would be 71 degrees. (He writes "71°" next to "tool response" on the arrow from APP to LLM.) The LLM will look at the tool response and then give the final answer, which might be something in the trend of the weather in Miami is pretty nice, it's 71 degrees. (He gestures at the final return arrow from LLM to APP.)

[02:34] This has some downsides. So when you do traditional tool calling, where you have an LLM and a client application, you could see the LLM hallucinate. (He writes "- hallucinate" under "LLM".) Sometimes the LLM can also make up incorrect tool calls. (He writes "- incorrect" under "hallucinate".)

[02:50] That's why I also want to look at embedded tool calling. (The screen transitions to a blue background, then back to the blackboard. The speaker remains in the frame.) We just looked at traditional tool calling, but traditional tool calling has its flaws. As I mentioned, the LLM could hallucinate or create incorrect tool calls. That's why I also want to take embedded tool calling into account. (He writes "embedded" above the "LLM" column, indicating a new topic.) With embedded tool calling, you use a library or framework to interact with the LLM and your tool definitions. The library would be somewhere between your application and the large language model. (He draws a box in the middle between "APP" and "LLM" columns and writes "library" at the top of the box.)

[03:22] In the library, you would do the tool definition, but you will also execute the tool calls. So let's draw a line between these sections here. (He draws a horizontal line inside the "library" box, dividing it into two sections. He writes "tool def" in the top section and "tool exec" in the bottom section.) So the library will contain your tool definition, it would also contain the tool execution. (He draws a line from the "tools" box under "APP" to encompass both the "tool def" and "tool exec" sections of the "library" box.)

[03:39] So when you send a message from your application to the large language model, it will go through the library. (He draws a horizontal arrow from the "APP" column to the "library" box's "tool def" section.) So your message could still be what is the temperature in Miami? (He writes "temp in Miami?" above the arrow.) The library will then append the tool definition and send your message together with the tools to the LLM. (He draws a curved arrow from the "library" box's "tool def" section to the "LLM" column.) So this will be your message plus your list of tools. (He writes "message + tool" above the curved arrow.)

[04:03] Instead of sending the tool to call to the application or the user, it will be sent to the library, which will then do the tool execution. (He draws a curved arrow from the "LLM" column back to the "library" box's "tool exec" section.) In this way, the library will provide you with the final answer. (He draws a horizontal arrow from the "library" box's "tool exec" section to the "APP" column.) Which could be it's 71 degrees in Miami. (He writes "71°" above the arrow.) When you use embedded tool calling, the LLM will no longer hallucinate as the library to help you with the tool calling, or the embedded tool calling, is going to take care of the tool execution and will retry the tool calls in case it's needed. (He points to the "hallucinate" and "incorrect" items under "LLM".)

*Embedded tool calling mitigates the risks of traditional tool calling by introducing a library between the application and LLM, which manages tool definitions, executes tool calls, and retries them, thereby preventing hallucinations and incorrect tool usage by the LLM.*

[04:32] So in this video, we looked at both traditional tool calling and also embedded tool calling, where especially embedded tool calling will help you to prevent hallucination or help you with the execution of tools, which could be APIs, databases or code. (The speaker concludes, and the screen transitions to a blue background with the IBM logo.)

</details>


## Additional Sources Scraped

<details>
<summary>function-calling-openai-api</summary>

**Function calling** (also known as **tool calling**) provides a powerful and flexible way for OpenAI models to interface with external systems and access data outside their training data. This guide shows how you can connect a model to data and actions provided by your application. We’ll show how to use function tools (defined by a JSON schema) and custom tools which work with free form text inputs and outputs.

If your application has many functions or large schemas, you can pair function calling with [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search) to defer rarely used tools and load them only when the model needs them. Only `gpt-5.4` and later models support `tool_search`.

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
    print(f"ID: {function_call.id}")
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
        type: Type.STRING

</details>
