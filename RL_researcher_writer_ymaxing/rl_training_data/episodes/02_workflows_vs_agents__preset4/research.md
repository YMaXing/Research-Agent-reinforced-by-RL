# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>How does Google's open-source Gemini CLI implement a coding assistant using context gathering, LLM reasoning, human validation, tool execution for file operations and code generation, and dynamic evaluation loops?</summary>

Phase: [EXPLOITATION]

### Source [4]: https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli

Query: How does Google's open-source Gemini CLI implement a coding assistant using context gathering, LLM reasoning, human validation, tool execution for file operations and code generation, and dynamic evaluation loops?

Answer: The Gemini CLI is an open-source AI agent providing access to Gemini in the terminal. It uses a reason and act (ReAct) loop with built-in tools and local or remote MCP servers to complete complex use cases like fixing bugs, creating new features, and improving test coverage. The ReAct loop implements LLM reasoning combined with dynamic evaluation loops through iterative reasoning and action cycles. Built-in tools include file read, file write for file operations, grep, terminal, supporting tool execution for file operations and code generation tasks. It excels at coding tasks via these capabilities. Gemini Code Assist agent mode in VS Code is powered by Gemini CLI, featuring MCP servers, commands like /memory, /stats, /tools, /mcp, Yolo mode, built-in tools like grep, terminal, file read/write, web search, web fetch. Human validation is implied in the workflow as users interact via terminal commands and can review agent actions. Context gathering occurs through tool usage like file reads and MCP integration for codebase awareness. Quotas are shared with Gemini Code Assist agent mode.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/

Query: How does Google's open-source Gemini CLI implement a coding assistant using context gathering, LLM reasoning, human validation, tool execution for file operations and code generation, and dynamic evaluation loops?

Answer: Gemini CLI is an open-source AI agent bringing Gemini 2.5 Pro into the terminal for coding, problem-solving, task management. It provides powerful AI capabilities including code understanding, file manipulation, command execution, dynamic troubleshooting. Built-in tools enable grounding prompts with Google Search for real-time external context (context gathering), extending capabilities through MCP or bundled extensions (tool execution), customizing prompts. Gemini Code Assist shares technology with Gemini CLI; in VS Code agent mode, it builds multi-step plans, auto-recovers from failed paths (LLM reasoning and dynamic evaluation loops), recommends solutions. Integration allows prompt-driven AI-first coding in terminal and VS Code. Open-source under Apache 2.0, extensible with MCP, system prompts via GEMINI.md. Usage involves natural language for writing code, debugging (code generation). Human validation through user prompts and review in workflow.

-----

-----

Phase: [EXPLOITATION]

### Source [6]: https://developers.google.com/gemini-code-assist/docs/overview

Query: How does Google's open-source Gemini CLI implement a coding assistant using context gathering, LLM reasoning, human validation, tool execution for file operations and code generation, and dynamic evaluation loops?

Answer: Gemini Code Assist provides AI coding assistance including agentic chat for complex multi-step tasks using system tools and MCP servers. Gemini CLI quota supports usage. Agent mode prompts Gemini for tasks with tools/MCP (tool execution). Conversational assistant uses opened files' context (context gathering). Code completion/generation in IDEs. Users validate output as early-stage tech can generate incorrect info (human validation). Multi-step collaborative reasoning agent expands simple interactions (LLM reasoning). Smart actions/commands for code tasks. Source citations for transparency.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/

Query: How does Google's open-source Gemini CLI implement a coding assistant using context gathering, LLM reasoning, human validation, tool execution for file operations and code generation, and dynamic evaluation loops?

Answer: Conductor is a Gemini CLI extension for context-driven development. Workflow: /conductor:setup establishes project context (product, tech stack, workflow) persisted in Markdown files (context gathering). /conductor:newTrack generates specs and plan.md with phases/tasks/subtasks. User approves plan (human validation). /conductor:implement has agent work through plan, checking off tasks, with checkpoints for reverting/editing (dynamic evaluation loops). Supports pausing/resuming. Persistent files enable context across sessions/machines. Ideal for complex tasks beyond simple edits, maintaining human in loop via plan review/approval.

-----

</details>

<details>
<summary>What is the architecture and operational process behind Perplexity's Deep Research feature, including research planning, parallel information gathering by specialized agents, analysis, iterative gap refinement, and final report synthesis?</summary>

Phase: [EXPLOITATION]

### Source [9]: https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research

Query: What is the architecture and operational process behind Perplexity's Deep Research feature, including research planning, parallel information gathering by specialized agents, analysis, iterative gap refinement, and final report synthesis?

Answer: Deep Research performs dozens of searches, reads hundreds of sources, and reasons through the material to deliver a comprehensive report in 2-4 minutes. Process: Research with reasoning - equipped with search and coding capabilities, it iteratively searches, reads documents, reasons about next steps, refining its research plan as it learns more, similar to human research. Report writing - synthesizes all research into a clear, comprehensive report after evaluating sources. Export & Share - export to PDF/document or Perplexity Page. It excels at expert-level tasks across domains.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://trilogyai.substack.com/p/comparative-analysis-of-deep-research

Query: What is the architecture and operational process behind Perplexity's Deep Research feature, including research planning, parallel information gathering by specialized agents, analysis, iterative gap refinement, and final report synthesis?

Answer: Perplexity’s Deep Research follows Plan → Search → Read → Synthesize (repeat as needed). It iteratively searches and refines with integrated coding, using a chain where the model calls search API or code interpreter. For example, it might fetch data and run calculations via code. It performs many searches in parallel, retrieves a large number of sources (e.g., 57 for a query), prioritizes reliable domains like academic papers. Outputs concise, well-structured summaries with inline citations. Combines web search, reasoning, and coding to iteratively refine analysis. No explicit user-approved planning; done behind the scenes.

-----

</details>

<details>
<summary>How do hybrid LLM workflow and agent systems use an autonomy slider with human-in-the-loop verification, as illustrated in tools like Cursor for coding and Perplexity for research?</summary>

Phase: [EXPLOITATION]

### Source [13]: https://cursor.com/

Query: How do hybrid LLM workflow and agent systems use an autonomy slider with human-in-the-loop verification, as illustrated in tools like Cursor for coding and Perplexity for research?

Answer: Cursor implements an autonomy slider in its AI coding tools, allowing users to control the level of AI independence. As stated by Andrej Karpathy: 'The best LLM applications have an autonomy slider: you control how much independence to give the AI. In Cursor, you can do Tab completion, Cmd+K for targeted edits, or you can let it rip with the full autonomy agentic version.' This ranges from low autonomy (Tab completion where user is mostly in charge) to high autonomy (full agentic mode). Agents work autonomously, running in parallel on their own computers to build, test, and demo features end-to-end for user review, enabling human-in-the-loop verification. Features like Composer 2 and Mission Control show planning and execution with user oversight, such as reviewing generated plans, tasks, and outputs before approval.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.latent.space/p/s3

Query: How do hybrid LLM workflow and agent systems use an autonomy slider with human-in-the-loop verification, as illustrated in tools like Cursor for coding and Perplexity for research?

Answer: Andrej Karpathy's talk on Software 3.0 highlights the Autonomy Slider for partial autonomy in hybrid LLM systems. Examples: Cursor (Tab -> Cmd+K -> Cmd+L -> Cmd+I agent mode); Perplexity (search -> research -> deep research); Tesla Autopilot (Level 1-4). This fits the Iron Man suit analogy: augmentation plus controlled autonomy. In human-AI loops, AI generates, humans verify quickly via GUIs. Stresses partial autonomy due to demo-product gap ('demo works.any(), product works.all()'), keeping humans in the loop for verification to speed up workflows while managing LLM jagged intelligence and amnesia.

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://towardsdatascience.com/building-human-in-the-loop-agentic-workflows/

Query: How do hybrid LLM workflow and agent systems use an autonomy slider with human-in-the-loop verification, as illustrated in tools like Cursor for coding and Perplexity for research?

Answer: Hybrid LLM agentic workflows use human-in-the-loop (HITL) via interrupts in LangGraph to pause at checkpoints for verification, addressing LLM errors that propagate in multi-step tasks. Interrupts pause execution, display info (e.g., generated content), await human input via Command(resume), then proceed. Checkpointers (e.g., SQLite) persist state with thread IDs for resumption. Placed at node or tool levels (e.g., before publishing). Best for subjective tasks like content creation where auto-verification is hard. Balances autonomy with oversight: agents execute but humans approve/edit key steps.

-----

</details>

<details>
<summary>What are the primary production challenges AI engineers face with reliability, unpredictable costs, debugging, security risks, and data integration when scaling agents versus structured workflows?</summary>

Phase: [EXPLOITATION]

### Source [18]: https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/

Query: What are the primary production challenges AI engineers face with reliability, unpredictable costs, debugging, security risks, and data integration when scaling agents versus structured workflows?

Answer: Scaling agentic AI systems presents significant production challenges compared to structured workflows. Orchestration complexity explodes in multi-agent architectures with agents delegating tasks, retrying steps, and dynamically choosing tools, leading to coordination overhead, race conditions, async pipeline issues, and cascading failures hard to reproduce in staging. Traditional workflow engines lack support for dynamic decision-making, forcing custom layers that are maintenance nightmares. Observability lags as agentic workflows require tracing every decision point in multi-step journeys (e.g., tool choices, retries), but infrastructure is immature; non-deterministic behavior prevents reliable failure replay. Debugging is like AI archaeology due to unpredictable paths. Cost management is tricky with high LLM call volumes in chained steps; token costs scale shockingly at volume (e.g., $0.15 execution becomes prohibitive at 500k/day), variable paths cause billing unpredictability and edge-case spikes. Evaluation/testing is problematic as non-determinism breaks traditional methods; no mature tooling exists, relying on human review. Governance/safety lags with agents taking real-world actions (emails, DB mods), needing robust guardrails without killing utility; regulatory pressures on accountability mount. These contrast with structured workflows' predictability and simpler maintenance.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/

Query: What are the primary production challenges AI engineers face with reliability, unpredictable costs, debugging, security risks, and data integration when scaling agents versus structured workflows?

Answer: Scaling AI agents vs workflows reveals stark challenges. Agents' non-deterministic loops cause runaway token costs (4-15x more than chats), spiraling bills from extra calls/retries; workflows predictable. Debugging agents like archaeology with fuzzy reasoning traces, error propagation unpredictable; workflows traceable like software. New agent failure modes: injection, jailbreaks, memory poisoning; workflows simpler. Monitoring needs specialized tools (LangFuse) for tokens/tools; workflows use standard APM. Security demands RBAC, least privilege for dynamic actions; workflows deterministic/easier. Agents suit dynamic/high-stakes but demand infra; workflows for repeatable/regulated/high-volume. Hybrids combine: workflows stable, agents flexible. Production realities: agents compound costs, need cost guards/caching; workflows linear. Testing agents needs sandboxes/human review; workflows unit-testable.

-----

</details>

<details>
<summary>How does the orchestration layer function differently when executing predefined LLM workflows versus facilitating dynamic planning in AI agents?</summary>

Phase: [EXPLOITATION]

### Source [23]: https://blog.tobiaszwingmann.com/p/ai-workflows-vs-ai-agents-vs-everything-in-between

Query: How does the orchestration layer function differently when executing predefined LLM workflows versus facilitating dynamic planning in AI agents?

Answer: In predefined LLM workflows (Automated AI Workflow), the orchestration follows a fixed, controllable linear or branching sequence where AI appears as a step, not the orchestrator. The workflow runs in a predefined order: A → AI Step → B → C → done. AI (LLM) performs tasks like summarizing, extracting fields, categorizing, or generating within this fixed structure. The rest handles routing, formatting, storing, or triggering steps. This provides predictability, clear human-in-the-loop checkpoints, and control over step order, ideal when inputs vary but process doesn't, and order matters.

In contrast, for AI agents, orchestration is dynamic and autonomous. Instead of fixed sequences, the agent takes a goal, reasons, and chooses actions/tools dynamically in a loop. Planning, reasoning, and execution occur inside the agent loop. It calls tools, queries data, or runs subtasks in any order, with each run potentially following different paths based on context. This trades determinism for flexibility, suited for open-ended reasoning, adaptive paths, or when step order can't be known upfront. The agent is the orchestrator, providing autonomy but introducing unpredictability.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://rierino.com/blog/openai-frontier-ai-orchestration-llms-vs-workflows

Query: How does the orchestration layer function differently when executing predefined LLM workflows versus facilitating dynamic planning in AI agents?

Answer: In LLM-Native Orchestration (aligned with predefined workflows), most coordination logic sits inside the AI platform. The provider supplies agent runtime, tool integrations, evaluation, and orchestration. Workflows are defined, tested, monitored in this environment. Orchestration handles execution authority, but it's tightly coupled to the provider's stack, enabling fast iteration, unified tooling, but higher vendor lock-in and challenges with multi-model strategies.

In AI-Enabled Workflow Platforms (facilitating dynamic planning in agents), orchestration anchors in external workflow engines or low-code platforms that decide step order, system calls, approvals, failures. AI plugs in as a component. This separates responsibilities: models reason, workflows route/enforce rules. Provides model flexibility, reuse of existing automation, stronger governance, but requires upfront design. Execution authority stays in trusted workflow layer, suiting regulated environments.

-----

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.promptingguide.ai/agents/ai-workflows-vs-ai-agents

Query: How does the orchestration layer function differently when executing predefined LLM workflows versus facilitating dynamic planning in AI agents?

Answer: AI Workflows use predefined code paths for orchestration: structured sequences with explicit control flow (e.g., prompt chaining, routing, parallelization). LLMs/tools follow fixed steps, high predictability, well-defined boundaries. Orchestration is explicit, hard-coded logic directing flow for well-defined tasks requiring consistency.

AI Agents enable dynamic orchestration where LLMs direct their own processes autonomously. Agents reason, reflect, select/use tools dynamically, self-direct execution without predefined flow. Example: Task Planner agent autonomously chooses tools (e.g., add/update tasks, search) and sequence based on context. Suited for open-ended tasks, adaptability over predictability. Key difference: workflows have fixed control flow; agents have LLM-driven dynamic decision-making.

-----

-----

Phase: [EXPLOITATION]

### Source [27]: https://www.ibm.com/think/topics/llm-orchestration

Query: How does the orchestration layer function differently when executing predefined LLM workflows versus facilitating dynamic planning in AI agents?

Answer: The orchestration layer manages interactions in LLM apps, creating coherent workflows. For predefined workflows, it handles explicit tasks like prompt chaining (sequencing LLM calls), managing libraries, fact-checking, refining outputs. Orchestrator delegates fixed components (LLMs, prompts, vector DBs, agents) in structured sequences, ensuring cohesion, predictability.

While not explicitly contrasting agents, it notes frameworks using AI agents for collaboration on tasks/goals, implying dynamic planning where orchestration facilitates autonomous agent interactions rather than rigid sequences. Orchestration simplifies integrating prompts, APIs, data, state for both, but agentic frameworks enable multi-agent dynamic coordination vs. fixed chaining.

-----

</details>

<details>
<summary>What practical real-world implementations best demonstrate the evaluator-optimizer pattern where one LLM generates content and another provides iterative feedback for refinement?</summary>

Phase: [EXPLOITATION]

### Source [28]: https://dylancastillo.co/til/evaluator-optimizer-pydantic-ai.html

Query: What practical real-world implementations best demonstrate the evaluator-optimizer pattern where one LLM generates content and another provides iterative feedback for refinement?

Answer: The evaluator-optimizer pattern features an LLM generator that produces a solution and an LLM evaluator that checks if it meets criteria. If rejected, feedback is provided to the generator for a new iteration until accepted. Examples include content generation matching specific guidelines like style, and iterative search result improvement. A practical implementation uses Pydantic AI with three agents: 'generator' (gpt-4o-mini, generates engaging <500 word article on topic), 'fixer' (gpt-4o-mini, improves text based on feedback), and 'evaluator' (gpt-4o-mini, assesses British English usage, suitability for young audience, no em dashes; outputs structured Evaluation with explanation, feedback, is_correct). Workflow: Generate article on topic (e.g., 'Consumption of hard drugs'), evaluate; loop up to 3 times fixing with feedback if not correct; return final output. Uses Logfire for monitoring, nest_asyncio for notebooks. Full code shown with @logfire.instrumented run_workflow function producing refined article meeting criteria.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow

Query: What practical real-world implementations best demonstrate the evaluator-optimizer pattern where one LLM generates content and another provides iterative feedback for refinement?

Answer: The Anthropic Cookbook's 'Building Effective Agents Cookbook' provides a reference Jupyter notebook implementation of the Evaluator-Optimizer Workflow: one LLM generates responses, another evaluates and provides feedback in a loop until success criteria met. Effective when clear evaluation criteria exist and iterative refinement adds value; signs of fit: LLM responses improve with feedback, LLM can self-evaluate meaningfully. Key components: Generator (creates solutions from task/examples/feedback), Evaluator (assesses against criteria), Feedback Loop, Success Criteria. Technical framework: loop/exit criteria (circuit breakers), separate prompts, clear generation/evaluation guidelines (with few-shot examples), success conditions/graceful degradation, monitoring, long-term eval (caching, evolution, error types). Applications: autonomous code review/improvement, content generation with guarantees, self-improving chatbots, automated documentation. Notebook link: https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/evaluator_optimizer.ipynb.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://spring.io/blog/2025/01/21/spring-ai-agentic-patterns

Query: What practical real-world implementations best demonstrate the evaluator-optimizer pattern where one LLM generates content and another provides iterative feedback for refinement?

Answer: Spring AI implements the Evaluator-Optimizer pattern as a dual-LLM process: Generator LLM produces/refines responses, Evaluator LLM analyzes and gives feedback in iterative loop, mimicking human refinement. Use when clear criteria, iterative value, multi-critique benefits. Implementation in EvaluatorOptimizerWorkflow class using ChatClient: loop(String task) generates initial solution, evaluates; if needs improvement, incorporates feedback for new generation until satisfactory; returns RefinedResponse with final solution and chainOfThought evolution. Usage example: workflow.loop('Create a Java class implementing a thread-safe counter') outputs final solution and evolution trace. Part of agentic-patterns repo: https://github.com/spring-projects/spring-ai-examples/tree/main/agentic-patterns/evaluator-optimizer. Advantages: model portability, structured output, consistent API. Based on Anthropic's 'Building Effective Agents' research.

-----

-----

Phase: [EXPLOITATION]

### Source [31]: https://ai.plainenglish.io/agentic-ai-a-deep-dive-into-the-evaluator-optimizer-workflow-and-gaia-benchmark-7c1e4257982e

Query: What practical real-world implementations best demonstrate the evaluator-optimizer pattern where one LLM generates content and another provides iterative feedback for refinement?

Answer: Practical implementation for real-time customer complaint classification and validation using Gemini via LangChain and MongoDB. Optimizer (LLM Call 1): Classifies complaint into categories (e.g., Billing) with prompt 'Classify into one of the categories...', outputs XML <category>Billing</category>. Evaluator (LLM Call 2): Checks if category valid with prompt 'You are feedback generator... return True/False'. Decision: If True, store in 'complaints'; if False, 'complaints_unclassified' with original complaint, predicted category, evaluation, timestamp. Feedback-driven: accept/store, retry, log error, manual review. Policies: invalid to unclassified, score<0.8 re-eval/human-in-loop. Demo code: MongoClient setup, ChatGoogleGenerativeAI('gemini-1.5-flash-latest'), lists of complaints/categories, invoke for classification/evaluation, conditional DB write. Ensures clean validated data, prevents hallucinations/invalid outputs.

-----

</details>

<details>
<summary>How does Gemini within Google Workspace use sequential LLM calls to read documents, generate summaries, extract key points, store results, and display them to users?</summary>

Phase: [EXPLOITATION]

### Source [32]: https://www.datastudios.org/post/google-gemini-and-summarizing-documents-uploaded-on-drive-integration-context-and-automation

Query: How does Gemini within Google Workspace use sequential LLM calls to read documents, generate summaries, extract key points, store results, and display them to users?

Answer: Gemini in Google Workspace integrates natively with Google Drive via Drive’s API infrastructure, Drive indexing, and Workspace context linking. When a user asks to summarize a report, Gemini retrieves the file from Drive, reads its content, and generates a condensed version reflecting headings, structure, and metadata. The summarization process follows a three-step pipeline: 1) Retrieval: Identifies relevant files using semantic search over filenames, body text, and metadata. 2) Parsing and Structuring: Converts files (Docs, PDF, TXT, DOCX) into clean internal representation, recognizing headings, tables, lists. 3) Condensed Output: Generates concise summary like bullet outlines or executive abstracts based on prompt. Supports multi-file summarization by merging content, highlighting differences, grouping insights. Available in Docs (section summaries, key points), Drive (abstracts, comparative overviews), Gmail (inline previews), Chat/Meet (linked briefings). Uses Google’s semantic index (vector database) for relevant passages. Outputs in styles like executive summary, detailed outline, key insights list. Automation via Apps Script, AppSheet for recurring digests to dashboards or Gmail. Respects permissions; summaries inherit labels. Gemini 2.5 Pro handles up to 1M tokens, processes long docs or multiples by dividing into clusters.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://cloud.google.com/blog/products/ai-machine-learning/long-document-summarization-with-workflows-and-gemini-models

Query: How does Gemini within Google Workspace use sequential LLM calls to read documents, generate summaries, extract key points, store results, and display them to users?

Answer: Google Cloud Workflows orchestrates Gemini models for long document summarization. Workflow triggered by new text file in Cloud Storage bucket. Splits document into chunks (e.g., 64,000 characters) fitting LLM context window. Map phase: loop_over_chunks extracts chunks in parallel, loads from Storage, calls subworkflow generate_chunk_summary (HTTP POST to Gemini Pro REST API with prompt for summary, parameters like temperature, max length), stores summaries in array. Reduce phase: concatenates chunk summaries, calls subworkflow again to generate final summary of summaries. Returns chunk summaries and final summary. Uses parallel execution for speed over sequential refinement. Subworkflow handles authentication (OAuth2), prompt passing, model config. Example: Summarizes 'Pride and Prejudice'. Applicable to Workspace via Cloud integrations for reading docs, generating chunk summaries sequentially/parallel, combining, displaying results.

-----

-----

Phase: [EXPLOITATION]

### Source [34]: https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub

Query: How does Gemini within Google Workspace use sequential LLM calls to read documents, generate summaries, extract key points, store results, and display them to users?

Answer: Gemini in Workspace side panel (Docs, Sheets, Slides, Drive, Gmail, Meet) searches relevant organizational content user has access to (emails, docs, presentations), generates grounded response. Can summarize documents from Drive. Prompts/responses retained 90 days to indefinite per admin settings; inserted content follows Workspace retention/Vault. History per app, private to user. Accesses only permitted content; obeys permissions, DLP, IRM. No training on customer data without permission. Audit logs track interactions. Grounding uses Workspace data first, optional Google Search. Displays responses in side panel; users insert into docs/emails applying protections.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://gemini.google/re/overview/?hl=en-GB

Query: How does Gemini within Google Workspace use sequential LLM calls to read documents, generate summaries, extract key points, store results, and display them to users?

Answer: Gemini processes user prompt using post-trained LLM, context, external sources (Google Search, extensions, uploaded files). Drafts multiple response versions via retrieval augmentation, retrieves pertinent info, safety checks, ranks by quality, displays highest-scoring. For Workspace integration (via app/extension), summarizes Drive docs, finds Gmail info. Sequential: pre-training on data, post-training (SFT, RLHF), response generation (drafting, retrieval, safety, ranking), human feedback loop. No explicit storage mentioned beyond activity controls; user exports via Takeout.

-----

</details>

<details>
<summary>In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://www.nature.com/articles/s41599-026-06598-1

Query: In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?

Answer: Healthcare/Pharma companies leverage structured LLM workflows emphasizing themes (1) Data Governance & Privacy (consent, minimization), (2) Safety & Human Oversight (guardrails, validation, clinician-override protocols), and (6) Risk Management & Compliance (risk-tiering, impact assessment, post-market monitoring). This ensures consistent accuracy through safety validation and human oversight, regulatory compliance via consent and traceability, and predictable performance with life-cycle safety protocols (Ditsche et al. 2023; Shiseido 2017). Finance/Banking aligns with (3) Security & Abuse Prevention (adversarial monitoring), (5) Transparency & Explainability (audit, logs, accountability), and (6) Risk Management & Compliance (model-risk controls, governance). Major institutions like JPMorgan Chase, Wells Fargo, HSBC use AI/ML for efficiency, compliance, with cautious adoption (restrictions on ChatGPT for data security), ethical principles (HSBC), model-risk oversight, board accountability, auditability, regulator-backed sandboxes (TCS 2024; Infosys 2024). These workflows provide model validation, output monitoring (McKinsey 2024: 32% mitigate inaccuracies), ensuring accuracy, compliance, predictable performance.

-----

-----

Phase: [EXPLOITATION]

### Source [37]: https://rpc.cfainstitute.org/research/the-automation-ahead-content-series/practical-guide-for-llms-in-the-financial-industry

Query: In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?

Answer: Finance companies use structured LLM workflows with hybrid approaches combining LLMs and retrieval-augmented generation (RAG) for domain-specific accuracy. Evaluation against benchmarks like FinBEN, FLARE ensures consistent accuracy and relevance. Fine-tuning (full, PEFT like LoRA/QLoRA), CoT prompting, few-shot learning optimize performance. Regular benchmarking, continuous monitoring maintain predictable performance. Open-source models (FinLLMs, FinGPT) fine-tuned on financial data excel in sentiment analysis, headline classification for compliance-relevant tasks. Closed-source (GPT, BloombergGPT) used cautiously due to privacy/compliance. Task-based datasets (FPB, FiQA) and benchmarks standardize evaluation for regulatory acceptance, ensuring auditable, explainable outputs.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://www.ibm.com/think/insights/maximizing-compliance-integrating-gen-ai-into-the-financial-regulatory-framework

Query: In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?

Answer: Finance institutions integrate LLMs into structured workflows for AML/BSA compliance, regulatory reporting, fraud detection. Key features: sequence modeling, probabilistic decisions for report generation, compliance monitoring. Compared to traditional ML, LLMs generalize without extensive feature engineering. Ensure transparency via explainable AI, model benchmarking, documentation. Address black-box issues, RAG governance, emergent behaviors with rigorous testing, audit trails. Regulatory focus: transparency, accountability, data privacy. Use cases: real-time risk alerts, transaction analysis for violations, ensuring predictable, accurate outputs compliant with regulations.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://fintechmagazine.com/news/how-financial-services-can-harness-llms-safely-effectively

Query: In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?

Answer: Financial services use structured LLM workflows with RAG, fine-tuning, evaluation pipelines for accuracy, explainability, auditability. Continuous monitoring, benchmarking against business logic/edge cases ensure regulatory compliance, predictable performance. Human-in-loop validation, audit trails for regulators. Mitigate bias/hallucinations via layered safeguards, curated data, real-time monitoring. Promising cases: real-time risk monitoring, regulatory change summarization, personalized advisory. EU AI Act emphasizes explainability, documentation, risk management, human oversight. Enterprise AI ops platforms standardize lifecycle management.

-----

-----

Phase: [EXPLOITATION]

### Source [40]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11105142/

Query: In what ways do finance and healthcare companies leverage structured LLM workflows to ensure consistent accuracy, regulatory compliance, and predictable performance in production AI tools?

Answer: Healthcare uses LLMs in structured workflows for clinical documentation, prior authorization, patient education, scheduling. Improves accuracy via flagging discrepancies, dynamic decision support. Ensures compliance (HIPAA) with secure EMR integration (Microsoft/Epic Azure OpenAI). Predictable performance through curated medical datasets, validation, human oversight. Concerns: privacy, cybersecurity; LLMs supplement, not replace clinicians. Fine-tuning on domain-specific data, continuous learning maintain reliability.

-----

</details>

<details>
<summary>What analogies from software engineering and cognitive science best illustrate the deterministic nature of LLM workflows versus the adaptive reasoning of AI agents?</summary>

Phase: [EXPLOITATION]

### Source [42]: https://arxiv.org/html/2411.09916v3

Query: What analogies from software engineering and cognitive science best illustrate the deterministic nature of LLM workflows versus the adaptive reasoning of AI agents?

Answer: Prior SE and HCI research on tool adoption and usability generally assumes that tools exhibit deterministic and stable behavior. Developers typically interact with fixed-function tools whose outputs remain consistent across uses. In contrast, LLM-based assistants generate multi-turn, adaptive, and stochastic outputs that evolve with each user prompt. This generative behavior positions LLMs as co-participants in problem solving rather than static tools. Unlike conventional SE tools, LLMs function much more like pair-programmers: they generate evolving, context-dependent outputs that require developers to continually reinterpret, validate, and adapt their next steps. This multi-turn, co-adaptive nature introduces breakdowns that differ fundamentally from traditional usability issues. Traditional SE and HCI tool-adoption literature generally assumes that tools behave deterministically and provide stable and predictable feedback. LLMs, in contrast, may hallucinate, omit important steps, lose context across turns, or produce misleading code. These issues accumulate over time and influence the developer’s reasoning process in ways that prior models do not account for.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://intuitionlabs.ai/articles/ai-agent-vs-ai-workflow

Query: What analogies from software engineering and cognitive science best illustrate the deterministic nature of LLM workflows versus the adaptive reasoning of AI agents?

Answer: AI workflows (pipelines) are structured, deterministic processes that orchestrate AI tasks in a fixed sequence – for example, data collection, preprocessing, model training, evaluation, and deployment. A pipeline app is a sequence of conventional functions passing output of one as input to the next. Workflows are predictable, testable, and cost-efficient. AI Agents are autonomous, goal-directed software entities that perceive their environment, make decisions, and take actions without continuous human guidance. An AI agent runs in a self-directed loop, making decisions about how to behave and what tools to use at each iteration. Agents offer flexibility but introduce complexity. In terms of compute costs, workflows are deterministic and optimized, running faster and cheaper for routine tasks. AI agents rely on large LLM calls at each reasoning step, making workloads expensive.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://www.browndailyherald.com/article/2026/01/llm-reasoning-has-striking-similarities-with-human-cognition-brown-researchers-find

Query: What analogies from software engineering and cognitive science best illustrate the deterministic nature of LLM workflows versus the adaptive reasoning of AI agents?

Answer: The study provides evidence that the mechanisms of reasoning between humans and LLMs are remarkably similar. In experiments, LLMs and humans evaluate evidence to figure out a hidden rule, adjusting hypotheses based on feedback. LLMs are generally more human-like than other AI models, even when right or wrong. LLMs display biases like belief bias, similar to humans. This suggests LLMs match human decision-making processes in reasoning trajectories.

-----

-----

Phase: [EXPLOITATION]

### Source [45]: https://www.deepset.ai/blog/ai-agents-and-deterministic-workflows-a-spectrum

Query: What analogies from software engineering and cognitive science best illustrate the deterministic nature of LLM workflows versus the adaptive reasoning of AI agents?

Answer: Deterministic AI systems follow clearly defined, predictable processes like assembly lines, with each component performing a specific function in a predetermined sequence. Example: basic RAG pipeline retrieves, ranks, generates response unidirectionally. Agentic AI systems have greater autonomy, dynamically determining steps, planning, adapting, using tools, introducing looping for refinement. Decision component routes information, enabling more agentic setup. Hybrid approaches combine both for reliability and flexibility.

-----

</details>

<details>
<summary>What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?</summary>

Phase: [EXPLOITATION]

### Source [46]: https://mlpills.substack.com/p/diy-17-orchestrator-worker-llm-agent

Query: What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?

Answer: The article provides a detailed DIY example implementing the Orchestrator-Worker LLM Agent pattern using LangChain for a 'Product Launch Analysis' tool analyzing 'SmartHome Hub Pro'. The orchestrator (gpt-4o, temperature=0) analyzes the product query and dynamically creates a structured JSON plan of subtasks using Pydantic models (Plan with SubTask: task_id, worker_type like 'technical', 'market', 'risk', instructions). It delegates to specialized workers: Technical Readiness Worker (gpt-4o-mini) analyzes features/development status from PRODUCT_DATABASE; Market Position Worker evaluates positioning/audience; Risk Assessment Worker identifies challenges/mitigations. Workers use domain-optimized prompts and data. A synthesizer LLM (gpt-4o) integrates outputs into a comprehensive launch readiness report. Key benefits: task decomposition, specialization (different models/prompts/tools), scalability (add workers easily), dynamic adaptation (orchestrator adjusts plan per query). Differs from parallelization by dynamic subtask creation with varied inputs. Full code + notebook provided for LangChain implementation with orchestrator_chain = prompt | LLM | parser.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://platform.claude.com/cookbook/patterns-agents-orchestrator-workers

Query: What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?

Answer: Anthropic's Claude Cookbook details the Orchestrator-Workers pattern with a FlexibleOrchestrator class using Claude Sonnet 3.5. The orchestrator LLM dynamically analyzes tasks and generates XML-structured subtasks (<tasks><task><type>formal</type><description>...</description></task>...</tasks>). Workers execute in parallel: each receives original task, task_type (e.g., 'formal', 'conversational'), description, context. Example: product description for eco-friendly water bottle (context: target millennials, features plastic-free/insulated/warranty). Orchestrator identifies 2-3 approaches (e.g., formal technical specs, engaging conversational), delegates to workers which generate styled content extracted via XML. No explicit synthesizer mentioned, but pattern implies synthesis of worker_results dict with analysis and results. Benefits: runtime adaptability vs fixed parallelization; for complex tasks needing unpredictable perspectives. Code includes parse_tasks(), llm_call(), process() with parallel worker execution. Use when subtasks can't be predefined.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://dev.to/akshaygupta1996/the-orchestrator-pattern-routing-conversations-to-specialized-ai-agents-33h8

Query: What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?

Answer: The article describes a production-grade Orchestrator pattern for routing conversations to specialized AI agents (scheduling_agent, reporting_agent, support_agent, document_agent, task_agent, general) in a business operations platform. Central Orchestrator uses LLM-based IntentRouter to dynamically classify user messages (e.g., 'Schedule a meeting' -> scheduling_agent) via structured prompt listing agents/keywords/examples/context. State machine with Session Manager tracks modes: 'orchestrator' (route new tasks) vs 'task_active' (forward to active_agent). Off-Topic Detector checks drifts, offers user choice. Agents signal [TASK_COMPLETE] for explicit completion, triggering return to orchestrator with NextActionSuggester (e.g., post-scheduling: create agenda/reminder). AgentRegistry dynamically loads/configures agents. Achieves 95%+ routing accuracy, 94%+ task completion. Architecture diagram shows flow: message -> session -> mode check -> router/detector -> agent -> completion check -> suggestions. Anti-patterns avoided: keyword routing, implicit completion.

-----

-----

Phase: [EXPLOITATION]

### Source [49]: https://online.stevens.edu/blog/building-self-healing-ai-orchestrator-reflexion-patterns/

Query: What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?

Answer: The Orchestrator-Workers pattern is described for scalable agentic systems in complex tasks. Central Orchestrator LLM (capable/expensive model) parses intent, dynamically decomposes into subtasks, delegates to specialized Worker agents (cheaper/faster models for scoped tasks like summarizing/extracting), aggregates results. Enables parallelization (5-20x speedups as I/O bound), economic optimization (smart orchestrator + cheap workers). No specific code/example, but positioned as standard for production where subtasks unpredictable. Combined with Reflexion (actor-critic self-healing loops) and FSMs for reliability. Mentions VIGIL research system as related self-healing example reducing errors to 0%.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://www.acceli.com/blog/ai-agent-workflow-patterns

Query: What production examples demonstrate the orchestrator-worker pattern dynamically assigning subtasks to specialized LLM components before synthesis in AI applications?

Answer: Production example: contract generation system where orchestrator (gpt-4o) plans structure via generateObject (components: legal/financial/domain workers, order/dependencies). Delegates to specialized workers (legal: compliance; financial: terms/penalties; domain: industry clauses) using type-specific systems/prompts. Final orchestrator reviews coherence/integration. Another: feature implementation tool plans components (frontend/backend/database/api/tests), workers generate code. Achieves 97% attorney approval vs 78% single-model. Optimizations: parallel workers, cheap models for simple tasks, caching. Used when diverse expertise/dynamic workflows needed; most expensive (8-20 calls), but cost-reduced 60% via optimizations. Code snippets with Vercel AI SDK/zod.

-----

</details>

<details>
<summary>What frameworks do AI engineers use to evaluate trade-offs in predictability, adaptability, development effort, and operational costs when selecting between predefined workflows and autonomous agents for a given project?</summary>

Phase: [EXPLOITATION]

### Source [52]: https://medium.com/online-inference/ai-agent-evaluation-frameworks-strategies-and-best-practices-9dc3cfdf9890

Query: What frameworks do AI engineers use to evaluate trade-offs in predictability, adaptability, development effort, and operational costs when selecting between predefined workflows and autonomous agents for a given project?

Answer: The source outlines frameworks for evaluating AI agents across technical implementation levels (Basic Responder to Autonomous Self-Directed) and human oversight autonomy levels (Supervisor to Full Autonomy), using a dual-axis matrix for trade-offs. Technical levels trade predictability (low for higher levels like multi-agent/autonomous) vs adaptability (high for tool-calling/multi-agent). Autonomy levels balance oversight (high predictability/low adaptability at low levels) vs independence (high adaptability but riskier). Evaluation strategies consider capability (accuracy, latency) vs autonomy/trust (escalation accuracy, handoff success). Progressive evaluation by level: Level 1 (predictable, low effort); Level 5 (high adaptability, high dev/ops cost). Metrics: Technical (success rate, efficiency); Autonomy (escalation precision, trust calibration); Resource allocation favors technical testing for low-autonomy/high-complexity, simulations for high-autonomy. Frameworks like classical agent types (reflex low adaptability, learning high) and matrix guide selection: workflows for predictable/low-autonomy (low dev effort, low costs); agents for adaptive/high-autonomy (higher effort/costs). Hybrid approaches mitigate trade-offs.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/

Query: What frameworks do AI engineers use to evaluate trade-offs in predictability, adaptability, development effort, and operational costs when selecting between predefined workflows and autonomous agents for a given project?

Answer: The source provides a decision framework scoring workflows vs agents on: Task Complexity (workflows for predictable, agents for dynamic); Business Value/Volume (workflows high-volume low-complexity, agents low-volume high-value); Reliability (workflows consistent/traceable, agents variable); Technical Readiness (workflows easier infra, agents need observability); Organizational Maturity (workflows lower expertise). Total score ≥6 favors one. Workflows: predictable execution, low dev effort, low costs, easy monitoring. Agents: high adaptability but 4-15x token costs, debugging challenges, new failure modes (loops, injection). Hybrid: workflows for predictable, agents for unpredictable. Production: workflows linear costs/scalability; agents need token guards, LLMOps. Recommendation: workflows default for resilience; agents for justified needs (dynamic convos, high-value decisions).

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What recent 2025 advancements in LLM reasoning models have specifically improved error recovery and long-horizon planning in ReAct-style AI agents compared to earlier implementations?</summary>

Phase: [EXPLORATION]

### Source [54]: https://arxiv.org/html/2603.19685v1

Query: What recent 2025 advancements in LLM reasoning models have specifically improved error recovery and long-horizon planning in ReAct-style AI agents compared to earlier implementations?

Answer: The paper 'A Subgoal-driven Framework for Improving Long-Horizon LLM Agents' (arXiv:2603.19685v1, dated 20 Mar 2026 but referencing 2025 works) introduces a subgoal-oriented framework addressing long-horizon failures in LLM agents, including ReAct-style agents. It identifies 'mid-stuck' behaviors as dominant failures (42-49% in baselines like Gemini-2.5-Pro and Gemma-SFT on WebArena-Lite), where agents enter non-productive loops due to poor planning and error propagation.

Key advancements:
- **Process Reward Models (PRMs)**: Unlike sparse Outcome Reward Models (ORMs), PRMs (Xi et al. 2025, Li and Li 2024, Cui et al. 2025, Choudhury 2025) provide dense step-by-step supervision for real-time verification and correction. Web-Shepherd (Chae et al. 2025) uses checklist sub-goal verification to reduce error propagation in web navigation. AgentPRM (Xi et al. 2025) dual-scores 'promise' (success likelihood) and 'progress' for inference-time search/pruning.

- **Subgoal-Oriented Framework**: Decomposes tasks into verifiable milestones using Gemini-2.5-Pro. Dynamic Milestoning integrates subgoals at inference for real-time progress tracking and error recovery via retrospective reflection, preventing hallucinated progress and enabling re-planning.

- **MiRA (Milestoning your Reinforcement Learning Enhanced Agent)**: RL finetuning with subgoal-based dense rewards via Potential-Based Reward Shaping (PBRS). Dual critics: goal-conditioned value critic (sparse) and potential critic (dense progress via subgoal completion interpolation). Achieves 43.0% SR on WebArena-Lite (Gemma3-12B), surpassing GPT-4-Turbo (17.6%), GPT-4o (13.9%), WebRL (38.4%). Reduces 'Get Stuck Midway' errors from ~33-49% to ~21%.

Compared to earlier ReAct-style agents (e.g., WebRL), which suffer sparse rewards and mid-task stalls, this framework provides dense feedback, hierarchical planning, and self-correction, boosting long-horizon web navigation by 10-20% absolute SR via offline RL and online milestoning.

-----

-----

Phase: [EXPLORATION]

### Source [55]: https://karpathy.bearblog.dev/year-in-review-2025/

Query: What recent 2025 advancements in LLM reasoning models have specifically improved error recovery and long-horizon planning in ReAct-style AI agents compared to earlier implementations?

Answer: The 2025 LLM Year in Review highlights Reinforcement Learning from Verifiable Rewards (RLVR) as a major advancement, enabling reasoning models like OpenAI o3 (early 2025). RLVR trains against objective rewards (e.g., math/code puzzles), allowing LLMs to develop strategies for breaking down problems, backtracking, and error correction—key for long-horizon planning in ReAct-style agents (which interleave reasoning and acting).

Compared to earlier SFT/RLHF (short finetunes), RLVR supports longer optimization on verifiable tasks, yielding 'reasoning' behaviors (intermediate steps, self-correction) hard to elicit via prompting. o1 (late 2024) demonstrated this; o3 marked inflection, with scaling laws for test-time compute via longer traces/'thinking time'.

Progress shifted from pretraining to RLVR overhang, producing similar-sized models but superior long-horizon capabilities. Claude Code emerged as convincing LLM Agent (tool-use loops for extended solving), running locally with private context—improving error recovery via environment grounding vs. cloud agents.

Benchmarks vulnerable to RLVR/synthetic data, showing 'jagged intelligence' (spikes in verifiable domains). No direct ReAct comparison, but RLVR addresses ReAct's sustained reasoning limits in long tasks.

-----

-----

Phase: [EXPLORATION]

### Source [56]: https://medium.com/@dzianisv/vibe-engineering-langchains-tool-calling-agent-vs-react-agent-and-modern-llm-agent-architectures-bdd480347692

Query: What recent 2025 advancements in LLM reasoning models have specifically improved error recovery and long-horizon planning in ReAct-style AI agents compared to earlier implementations?

Answer: Mid-2025 agent architectures build on ReAct (Thought-Action-Observation loops for interleaved reasoning/tools). Key advancements for error recovery/long-horizon planning:

- **Plan-and-Act (2025)**: Dual LLMs—Planner generates subgoal sequences; Executor performs steps with feedback loops for re-planning. 57.6% success on WebArena (vs. baselines), addressing ReAct's myopia via lookahead/hierarchical structure.

- **Memory Systems**: Multi-tier (working/long-term via vector DBs/knowledge graphs). Mem0 reduces tokens 91%, boosts accuracy 26%; Graphiti temporal graphs enable state-tracking over sessions, preventing ReAct loop-stalls.

- **Self-Reflection (Reflexion)**: Agents critique failures, replan—improves coding/math via iterative correction.

- **Multi-Agent**: Specialization (MetaGPT roles) + verification reduces single-agent errors; but prone to coordination failures.

ReAct drawbacks (inefficiency, no explicit planning) fixed by hybrids: function-calling for tools + planning/memory. State-of-art converges: tool-use + memory + planning + reflection for robust long-horizon tasks.

-----

</details>

<details>
<summary>What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?</summary>

Phase: [EXPLORATION]

### Source [57]: https://snorkel.ai/blog/llm-observability-key-practices-tools-and-challenges/

Query: What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?

Answer: Challenges in LLM Observability for enterprise applications at scale include: Scalability of Monitoring Solutions - observability systems must scale alongside growing model complexity and volume of interactions. Handling High Model Complexity - LLMs’ multi-modal, multi-turn, and multi-agent capabilities increase monitoring complexity exponentially. Maintaining Real-Time Monitoring at Scale - enterprises require observability pipelines that combine depth of evaluation with operational scalability. Handling Infinite Possibilities of LLM Responses - unlike classification models, LLMs produce near-infinite response variations, making manual evaluation inefficient without scalable frameworks. Drifting in LLM Performance Over Time - model updates, fine-tuning, or retrieval data changes cause performance drift, requiring continuous observability. Key components include Response Monitoring (accuracy, completeness, faithfulness, relevance), Latency and Throughput Tracking, Model Drift Detection, Error and Anomaly Detection. Pillars: Model Evaluation and Testing with specialized evaluators, Feedback Loops with SME-in-the-loop, Interpretability. Future: Programmatic Evaluator Development (criteria as code), SME-in-the-Loop Collaboration, Fine-Grained Evaluation Slices, Integrated Optimization Pipeline where evaluation outputs inform prompt engineering, retrieval tuning, embedding fine-tuning, LLM alignment workflows. Observability systems must handle data privacy, ethical concerns, and provide real-time metrics with depth.

-----

-----

Phase: [EXPLORATION]

### Source [58]: https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow

Query: What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?

Answer: For evaluator-optimizer LLM workflows: Technical Implementation Framework includes Rigorous Loop run and exit criteria (circuit breakers to prevent infinite loops, resource exhaustion), Clear generation guidelines (context, examples), Clear evaluation criteria (machine-readable, business-relevant), Clear success conditions and failure recovery (graceful degradation). Measuring Success: Monitoring and Observability to ensure system quality, Memory management of Chain of Thought, Tracking experiments (immediate improvements, long-term patterns). Long Term Evaluation: Solution similarity for caching, evolution with business goals, evaluator hallucination (Type 1/2 errors). Cost Evaluation: Monetary (LLM API calls), Time (latency of fast/slow cycles), Failure costs (direct compute, indirect production errors, opportunity). Key Takeaways: Embed quality assurance in architecture, apply at multiple scales, account for fast/slow improvement cycles, focus on robust evaluation criteria over perfect prompts, graceful degradation. Strategic: Self-improving systems, governance with audit trails, progressive automation.

-----

-----

Phase: [EXPLORATION]

### Source [59]: https://langwatch.ai/blog/observability-framework-design-for-llm-apps-the-complete-langwatch-guide

Query: What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?

Answer: LLM observability challenges: Infinite possibilities/edge cases (unpredictable user inputs), Performance drift (non-deterministic, model changes). Automated Evaluations essential as manual review doesn't scale (e.g., 30k responses/month). Five pillars: Real-Time output tracking, Built-In Automated AI Testing, Precision Search & Filtering, End-to-End application visibility (tracing), Integrated Human-in-the-loop. Response Monitoring: User/session linking, hyperparameter logging, query-output mapping, custom data, performance metrics. Filtering by user/topic, LLM config, contextual data, annotations, failed evals. Offline vs real-time evals (reference-based vs metrics like relevancy, faithfulness). Application Tracing for pipelines (pinpoint bottlenecks, debug failures). Human-in-the-loop for high-stakes. Trade-offs implied in balancing real-time monitoring with depth, scaling to millions of responses, minimizing latency with async logging.

-----

-----

Phase: [EXPLORATION]

### Source [60]: https://www.tribe.ai/applied-ai/llm-observability-enterprise-workflows

Query: What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?

Answer: LLM observability framework pillars: LLM Evaluation (perplexity, BLEU, ROUGE), Traces and Spans, RAG monitoring, Fine-Tuning tracking, Prompt Engineering visibility. Key considerations: Distributed tracing for full lifecycle, asynchronous logging to prevent bottlenecks. Latency and Cost Optimization: Caching, dynamic routing, automated scaling, prompt refinement to reduce tokens. Monitoring/Governance: Version control, audit trails, compliance. Trade-offs in performance vs accuracy, real-time vs depth. For enterprise workflows, focus on scalability under heavy loads, reducing MTTR via log summarization, incident correlation.

-----

-----

Phase: [EXPLORATION]

### Source [61]: https://freeplay.ai/blog/llm-observability

Query: What are the key engineering trade-offs and observability requirements when implementing evaluator-optimizer loops at scale within LLM workflows for high-volume enterprise applications?

Answer: Challenges: Tracing nested workflows, debugging tool chains, understanding autonomous decisions, managing at scale (multi-agent, high volume). Trade-offs: Depth of insight vs performance impact (sampling, async logging), completeness vs signal-to-noise in logs. Scale issues: Huge data volumes, storage/indexing, noise filtering, instrumentation overhead. Metrics: Token usage/costs, latency, errors, model params, tool success, decision paths, quality (accuracy, relevance, safety). Best practices: Lightweight instrumentation, product-specific evals, agent patterns (hierarchical tracing), feedback loops, alerting. For scale: Correlation IDs, unified models, async architecture.

-----

</details>

<details>
<summary>How are principles from feedback control systems in cybernetics and engineering being adapted to create more stable hybrid LLM workflow and agent architectures with dynamic autonomy adjustment?</summary>

Phase: [EXPLORATION]

### Source [62]: https://aixiv.science/pdf/aixiv.251207.000004

Query: How are principles from feedback control systems in cybernetics and engineering being adapted to create more stable hybrid LLM workflow and agent architectures with dynamic autonomy adjustment?

Answer: The Cybernetic Agents proposal introduces a unified framework applying semantic control theory to LLM agents, modeling them as semantic dynamical systems under feedback control. It proposes five components: (A) Semantic Control Theory defining semantic state spaces, Lyapunov-style stability, robustness, and safety on embedding manifolds; (B) Closed-loop Cybernetic-Agent Architecture organizing observer, planner, regulator, safety filter, and executor around the LLM core; (C) LLM-based Model Predictive Control (LLM-MPC) for receding-horizon planning in semantic space; (D) Semantic Kalman Filter for belief-state estimation and hallucination drift correction; (E) Control Barrier Function (CBF)-based semantic safety filter enforcing forward invariance of safe sets at token and action levels.

Classical control tools like PID control, Kalman filtering, MPC, robust/adaptive control, and CBFs are adapted from physical systems to cognitive LLM agents. The framework models LLM agents on semantic embedding manifolds as stochastic dynamical systems, defines semantic stability via Lyapunov-like energy functions, and semantic safety via barrier functions.

Key modules include: Semantic Kalman Filter approximating LLM dynamics for state estimation; LLM-MPC using LLM rollouts for planning; semantic PID regulator for fine-grained correction; CBF safety filter enforcing constraints at token level (e.g., file deletion barrier vetoing unsafe actions).

The closed-loop performs: observe → update belief → plan → regulate → safety filter → execute. This provides theoretical foundations for stability (Lyapunov analysis) and safety (CBF guarantees), addressing open-loop LLM limitations like error accumulation, state drift, and lack of safety.

Implementation uses neural approximations, meta-learning, and prompt-based modules, with phased roadmap (CBF first, then observer/MPC/PID). Experiments on OSWorld, WebShop, SafetyBench evaluate settling time, overshoot, safety violations vs. baselines like ReAct.

Prior work includes PID for LLM robustness [Zhang et al.], Lyapunov decoding [Richards et al.], CBF safety filters, LLM-MPC in robotics.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://arxiv.org/html/2602.03433v1

Query: How are principles from feedback control systems in cybernetics and engineering being adapted to create more stable hybrid LLM workflow and agent architectures with dynamic autonomy adjustment?

Answer: Principles from feedback control systems and cybernetics are adapted to LLMs by modeling them as dynamical systems, applying controllability, observability, stability analysis, and using SSMs. LLMs support control via indirect workflow augmentation and direct controller design/synthesis.

Control for LLMs: Model editing (parameter-space control), activation engineering (state-feedback), prompt engineering (feedforward). LiSeCo provides optimal activation control with guarantees.

Control with LLMs: SSMs (Mamba) as linear dynamical systems with controllability/observability canonical forms and stability modifications. Historical evolution from cybernetics (Wiener feedback) to RLHF as control loops.

MPC with LLMs: Sampled MPC where LLM generates candidate plans, evaluated via cost function.

DriveLLM integrates LLMs with driving stacks via cyber-physical feedback for adaptation.

Challenges: Fragmented LLM-control intersection lacks unified framework.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2507.07115v1

Query: How are principles from feedback control systems in cybernetics and engineering being adapted to create more stable hybrid LLM workflow and agent architectures with dynamic autonomy adjustment?

Answer: Agentic framework uses validator-reprompting loops (feedback) for FSM traversal (symbolic planning) and continuous control (TCLab temperature regulation under disturbances).

FSM: Action agent proposes paths, Simulation executes, Validation checks, Reprompting refines invalid plans (up to 5 cycles). GPT-4o achieves 100% valid paths.

Continuous control: Action proposes powers, Temperature/Power validators check progress/bounds, reprompting refines. Compares to PID; GPT-3.5 nears PID on digital twin.

Feedback via iterative correction stabilizes LLM outputs, akin to control loops. Digital twin for safe validation.

Builds on ReAct/Reflexion iterative feedback, CoT for reasoning.

-----

</details>

<details>
<summary>What lessons from the historical development of autonomous robotics and multi-agent simulation systems can inform the design of collaborative orchestrator-worker patterns in modern LLM applications?</summary>

Phase: [EXPLORATION]

### Source [65]: https://newsletter.victordibia.com/p/multi-agent-llm-applications-a-review

Query: What lessons from the historical development of autonomous robotics and multi-agent simulation systems can inform the design of collaborative orchestrator-worker patterns in modern LLM applications?

Answer: The source discusses historical development of autonomous robotics and multi-agent systems, noting research into agent-based systems like robots focusing on path planning, navigation, and Sense-Plan-Act paradigm. Multi-agent systems studied human collaboration, collective intelligence, crowdsourcing, swarm intelligence, and network theory. Development limited by lack of reasoning engines for adapting to context and synthesizing plans. Suggests borrowing ideas from robotics, planning, swarm intelligence, reinforcement learning, network theory, actor network theory for optimized orchestration approaches. Emphasizes task termination conditions to avoid infinite loops in long-duration agent collaborations, recommending dynamic mechanisms like 'baby sitter' models for loop detection and prioritization. Highlights controllability tradeoffs (autonomy vs. deterministic behavior), evaluation challenges (task completion, reliability, cost), and efficient orchestration (defining agent workflows, routing, communication patterns). Centralized/decentralized architectures discussed for decision-making consistency.

-----

-----

Phase: [EXPLORATION]

### Source [66]: https://www.classicinformatics.com/blog/how-llms-and-multi-agent-systems-work-together-2025

Query: What lessons from the historical development of autonomous robotics and multi-agent simulation systems can inform the design of collaborative orchestrator-worker patterns in modern LLM applications?

Answer: Discusses swarm robotics where multiple autonomous robots collaborate on tasks like warehouse management, search-and-rescue, environmental monitoring. LLM-MAS enables robots to communicate, plan, execute collaboratively, e.g., distributing tasks in warehouses. Robotics applications include swarm robotics for optimized task distribution. Centralized architecture: one agent as orchestrator manages information/task flow. Peer-to-peer: direct agent communication without central orchestrator. Hybrid: combines centralized planning with independent execution. Workflow: task decomposition by Planner Agent, role assignment to specialized agents (Researcher, Coder, Reviewer), inter-agent communication via structured message passing, memory sharing (global/local), coordination strategies (leader-follower, token-passing, decentralized consensus), feedback loops with Critic Agent. Frameworks like AutoGen, CrewAI, LangChain, MetaGPT for multi-agent systems. Benefits: modularity, collaboration, task specialization, parallel execution, emergent behavior.

-----

-----

Phase: [EXPLORATION]

### Source [67]: https://arxiv.org/html/2502.03814v4

Query: What lessons from the historical development of autonomous robotics and multi-agent simulation systems can inform the design of collaborative orchestrator-worker patterns in modern LLM applications?

Answer: Survey on LLMs for Multi-Robot Systems (MRS). MRS advantages: scalability, resilience, cost-effectiveness via collective intelligence. Challenges: communication, coordination, decision-making in dynamic environments. LLMs enhance MRS via natural language interfaces for inter-robot communication, task decomposition/allocation, adaptability. Communication architectures: centralized (message distributor relays to individual LLM agents), decentralized (DMAS), hybrid (HMAS-1/2). Hybrid HMAS-2 outperforms in complex tasks. High-level task allocation/planning: LLMs allocate tasks, decompose complex instructions. Mid-level motion planning: navigation/path planning. Low-level action generation: formation control. Applications: household, construction, formation, tracking, games. Simulations: AI2-THOR, PyBullet, BEHAVIOR-1K. Benchmarks: RoCoBench, ALFRED, BOLAA, COHERENT-Benchmark. Challenges: mathematical reasoning limits, hallucination, latency, multi-modal integration, lack of benchmarks.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12402697/

Query: What lessons from the historical development of autonomous robotics and multi-agent simulation systems can inform the design of collaborative orchestrator-worker patterns in modern LLM applications?

Answer: Survey on agentic LLM-based robotic systems. Agentic AI: autonomous systems perceiving environment, making decisions, acting to achieve goals. Reviews 30 papers validated in real-world. Domains: Navigation/Mobility, Manipulation/Object Interaction, Multi-Agent/Collaborative Robotics, General-Purpose Multi-Task Robots. Agenticness classification: Autonomy, Goal-directed behavior, Adaptability, Decision-making. Multi-agent robotics: RoCo (dialectic collaboration via LLM dialogue), MALMM (specialized LLM agents for planning/coding/supervision), LaMI (interprets user states socially), VADER (seeks help on failures), LLM-MARS (behavior trees for coordination), LLM2Swarm (centralized/decentralized integration). Ethical framework: Fairness/Bias, Safety Guardrails, Transparency/Explainability, Auditability/Accountability. Clustering by ethical rigor. Challenges: sim-to-real gap, agentic AI overlooked, ethics superficial.

-----

</details>

<details>
<summary>What information-theoretic or computational complexity arguments explain the fundamental differences in predictability between developer-defined control flow in LLM workflows and emergent decision-making in autonomous LLM agents?</summary>

Phase: [EXPLORATION]

### Source [70]: https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/

Query: What information-theoretic or computational complexity arguments explain the fundamental differences in predictability between developer-defined control flow in LLM workflows and emergent decision-making in autonomous LLM agents?

Answer: Developer-defined control flow in LLM workflows is predictable and deterministic because it follows explicit, structured pipelines with predefined steps (e.g., classify → route → respond → log). Execution is linear, with known call counts, allowing precomputation, batching, caching, and linear cost scaling. Debugging is transparent via stack traces and logs, with explicit error handling. In contrast, emergent decision-making in autonomous LLM agents is non-deterministic due to recursive loops where the LLM dynamically selects tools, reasons adaptively, and self-corrects, leading to variable execution paths, potential infinite loops, and unpredictable token consumption (4x-15x more than workflows). The scheduling policy is opaque (LLM inference), making failure modes like reasoning errors hard to debug. Predictability stems from explicit vs. implicit control flow, with workflows enabling verifiable, bounded execution and agents risking runaway behavior without extensive infrastructure.

-----

-----

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2604.11378v1

Query: What information-theoretic or computational complexity arguments explain the fundamental differences in predictability between developer-defined control flow in LLM workflows and emergent decision-making in autonomous LLM agents?

Answer: The paper formalizes execution systems as schedulers with ready-set cardinality |U| and policy explicitness. Developer-defined control flow (workflows) corresponds to multi-ready-unit schedulers with deterministic, explicit policies (|U|≥1, functional P), enabling parallel dispatch, bounded recovery, and verifiable traces via static DAGs. Emergent decision-making (Agent Loops) is a single-ready-unit scheduler (|U|≤1) with non-deterministic, opaque LLM policy (relational P), leading to serial execution, unbounded recovery, and implicit dependencies. Non-determinism arises from LLM nodes producing varying outputs for identical inputs (hallucination, misinterpretation), unlike deterministic workflow nodes. Computational complexity notes optimal scheduling under budgets is likely NP-hard (DAG scheduling reduction), but Graph Harness provides semantic guarantees (termination, soundness). Predictability difference: explicit topology vs. context-window reasoning; multi-|U| enables structural parallelism absent in loops.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://www.barnacle.ai/blog/2025-09-25-agents-intro

Query: What information-theoretic or computational complexity arguments explain the fundamental differences in predictability between developer-defined control flow in LLM workflows and emergent decision-making in autonomous LLM agents?

Answer: Workflows (Level 2) use predefined code paths with fixed loops, ensuring predictability via deterministic orchestration (e.g., classify expense → route approval). Emergent decision-making in autonomous agents (Level 3+) relies on iterative agent loops (observe-think-act-reflect), where LLMs dynamically plan and adapt, introducing non-determinism from stochastic generation and unbounded iterations. No explicit complexity arguments, but workflows scale predictably (linear cost), while agents risk exponential token use from loops, requiring guardrails (max steps, budgets). Anthropic distinction: workflows have developer-defined control flow; agents have LLM-directed processes, making outcomes less predictable due to emergent behaviors.

-----

</details>

<details>
<summary>How are principles from human organizational management, hierarchy design, and team coordination being adapted to create effective multi-agent LLM systems for complex enterprise workflows?</summary>

Phase: [EXPLORATION]

### Source [75]: https://sebgnotes.substack.com/p/multi-agent-design-applying-human

Query: How are principles from human organizational management, hierarchy design, and team coordination being adapted to create effective multi-agent LLM systems for complex enterprise workflows?

Answer: The article applies human organizational principles to AI agent teams, introducing the 'Two-Pizza Rule' (teams small enough to feed with two pizzas) and hierarchical management. Key patterns include Hierarchical Management where a manager agent owns outcomes, worker agents handle specialized tasks, and dynamic task delegation occurs. Team Size Optimization limits to maximum 7 worker agents, single-threaded manager, clear individual ownership, and specialized roles. Framework selection considers language-specific approaches, minimal dependencies, production, and scalability. Strategic implications for organization design: clear agent responsibilities, measurable outcomes, quality control, team size limits. System architecture addresses token management, tool access, framework independence. Implementation framework: Manager setup with objectives, delegation, metrics, coordination; Worker configuration limits tools (≤10), task scope, success criteria, reporting; System integration with framework, dependencies, persistence, monitoring. Development strategy includes framework choices like Python SDK + Postgres, JS Vercel AI SDK. Personal notes highlight parallels to human teams needing clear leadership and specialized roles for AI agent teams. Future evolution: better orchestration, specialization, quality control, incentives, standardized patterns. This structured approach improves reliability, effectiveness, reduces complexity.

-----

-----

Phase: [EXPLORATION]

### Source [76]: https://www.fiddler.ai/articles/multi-agent-llm-systems-for-enterprises

Query: How are principles from human organizational management, hierarchy design, and team coordination being adapted to create effective multi-agent LLM systems for complex enterprise workflows?

Answer: Multi-agent LLM systems divide responsibilities across specialized agents for complex, multi-step workflows, mirroring human team coordination. Architectures include Supervisor Architecture with a top-level agent overseeing, allocating tasks, monitoring, handling exceptions for centralized governance. Hierarchical Architecture features a lead/orchestrator dividing tasks into subtasks delegated to specialized agents (e.g., retrieval, reasoning, tool calling), supporting structured workflows, traceability. Enterprise examples like travel booking: Lead Agent coordinates sub-agents for flights, hotels, car rentals. Key features: Agent Orchestration (centralized/decentralized management), Role Specialization (tasks by strengths), Collective Intelligence (collaboration for better conclusions). Best practices: Governance frameworks defining roles, responsibilities, accountability, escalation paths; Continuous Monitoring for agent decisions, interactions; Observability for visibility; Interpretability for analysis; Security. Enterprise applications: Business Process Automation (workflow stages), Data Analysis (pipeline stages), Customer Service (triage, technical, knowledge agents), Disaster Response, Cross-Functional Teamwork. Hierarchical architectures prevalent in enterprises for complex tasks, enhancing decision-making, monitoring with tools like Fiddler Agentic Observability tracking reasoning, tools, coordination.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://xue-guang.com/post/llm-marl/

Query: How are principles from human organizational management, hierarchy design, and team coordination being adapted to create effective multi-agent LLM systems for complex enterprise workflows?

Answer: LLM-based multi-agent systems mirror human collaboration with specialized roles, coordination. Architectural patterns: Centralized coordination (supervisor manages workers, e.g., AutoGen, LangGraph); Decentralized (peer-to-peer, CAMEL); Hierarchical (multi-level supervision, LangGraph teams, MegaAgent). Frameworks like CrewAI use role-based design with specific roles, goals, skills, hierarchical teams, process-driven collaboration for business automation, adopted by Oracle, Deloitte, Accenture. MetaGPT implements assembly line with roles like Product Manager, Architect, Engineer, QA. Communication: memory-based, report-based, relay, debate. Coordination across actors, types (cooperation), structures (hierarchical), strategies (role-based). Enterprise: Microsoft AutoGen at Novo Nordisk for data analytics; Business-in-a-Box automates departments. Architecture best practices: explicit role definition, communication patterns matching tasks (hierarchical for complex coordination), error handling, human oversight. CrewAI for business automation with hierarchical structures. Challenges include inter-agent misalignment, coordination complexity.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://www.linkedin.com/posts/aishwarya-srinivasan_not-all-multi-agent-ai-systems-should-be-activity-7413630297298255872-LFoG

Query: How are principles from human organizational management, hierarchy design, and team coordination being adapted to create effective multi-agent LLM systems for complex enterprise workflows?

Answer: Multi-agent AI design adapts organizational principles: Centralized for speed/simplicity (MVP, one decision-maker); Decentralized for reliability (independent agents, no single failure point, critical systems); Hierarchical for 10+ agents coordination (manager/orchestrator delegates, monitors, scales for large teams); Hybrid for complex enterprise domains (centralized control, decentralized execution, hierarchy, e.g., food delivery, workflows). Start centralized for MVP, add decentralized for reliability, hierarchical as grows, hybrid at scale. Maps to enterprise needs: coordination bottlenecks signal shift from centralized; cascading failures from decentralized; human reasoning limits trigger hierarchical. Reflects organizational operation under pressure.

-----

</details>

<details>
<summary>What techniques from video game NPC behavior, decision trees, and adaptive AI in gaming engines can inform more natural and context-aware interactions in coding assistants like Gemini CLI and research agents?</summary>

Phase: [EXPLORATION]

### Source [80]: https://lutpub.lut.fi/bitstream/handle/10024/170271/bachelorsthesis_salek_md_peash_been.pdf?sequence=1&amp;isAllowed=y

Query: What techniques from video game NPC behavior, decision trees, and adaptive AI in gaming engines can inform more natural and context-aware interactions in coding assistants like Gemini CLI and research agents?

Answer: This bachelor's thesis explores adaptive NPC behavior in video games using AI for real-time player interaction. Key techniques include behavior trees, which organize NPC decisions into hierarchical branches, nodes, and tasks based on logical conditions, enabling complex behaviors like combat or information gathering. Behavior trees are commonly used in Unreal Engine for flexible, player-reactive decision-making. Finite State Machines (FSM) provide simple decision-making for basic actions like attacks. Reinforcement Learning (RL) allows NPCs to learn from interactions, adapting strategies dynamically like humans, used for intelligent pathfinding, Q-learning, and self-improving combat. Environment Query System (EQS) in Unreal enables NPCs to analyze options like safest paths or enemy targeting. Goal-Oriented Action Planning (GOAP) lets NPCs plan actions toward goals using preconditions and effects. Unity's ML-Agents Toolkit integrates RL for training agents without manual scripts. Pathfinding with NavMesh and A* ensures adaptive navigation. These make NPCs flexible, interactive, dynamic, and adaptive, informing context-aware AI by enabling hierarchical decision-making, learning from user interactions, environmental querying, and goal-driven planning for natural responses in coding assistants.

-----

-----

Phase: [EXPLORATION]

### Source [81]: https://blog.gopenai.com/how-ai-is-revolutionizing-npc-behavior-in-modern-games-814568b423f5

Query: What techniques from video game NPC behavior, decision trees, and adaptive AI in gaming engines can inform more natural and context-aware interactions in coding assistants like Gemini CLI and research agents?

Answer: AI revolutionizes NPC behavior from scripted to adaptive using Finite State Machines (FSM), which define states like patrolling or attacking with transitions based on player proximity. Behavior trees, a sophisticated FSM variant, decompose actions into hierarchical nodes for complex, flexible decision-making responding to environmental changes. Machine learning, especially reinforcement learning, enables NPCs to learn from player actions, adapting behavior for personalized interactions. Examples include The Last of Us Part II's opponents flanking and responding in real-time, and Red Dead Redemption 2's dynamic NPC reactions to player reputation. These techniques create reactive, learning agents that evolve, informing coding assistants with state-based transitions for task contexts, hierarchical decision trees for multi-step reasoning, and RL for adapting to user patterns, yielding natural, context-aware interactions.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://www.captechu.edu/blog/ai-in-video-game-development

Query: What techniques from video game NPC behavior, decision trees, and adaptive AI in gaming engines can inform more natural and context-aware interactions in coding assistants like Gemini CLI and research agents?

Answer: AI drives smarter NPCs using machine learning and behavior trees for learning, adapting, and evolving responses to player strategies, simulating emotions, and forming relationships. Game engines like Unity, Unreal, and Capcom’s RE Engine integrate behavior trees and ML for intelligent NPCs and adaptive gameplay. Nemesis System in Middle Earth: Shadow of Mordor lets enemies remember and adapt to encounters. These enable realistic, unpredictable experiences. For coding assistants, behavior trees provide structured decision hierarchies for context analysis; ML/RL allows adaptation to user coding styles and queries; engine-like integration ensures seamless, responsive interactions mimicking dynamic NPC-player engagements.

-----

</details>

<details>
<summary>How are no-code automation platforms and citizen developer tools evolving to incorporate hybrid LLM workflows and agents, particularly in relation to visual autonomy sliders and human verification interfaces?</summary>

Phase: [EXPLORATION]

### Source [83]: https://www.emergentmind.com/topics/low-code-llm-systems

Query: How are no-code automation platforms and citizen developer tools evolving to incorporate hybrid LLM workflows and agents, particularly in relation to visual autonomy sliders and human verification interfaces?

Answer: Low-code LLM systems enable users with minimal coding skills to build AI applications using visual interfaces and natural language prompts, spanning zero-code to low-code frameworks. They integrate LLM backends with multi-agent orchestration, memory management, and RAG for workflows. Hybridization integrates LLM-driven code generation with visual programming languages (VPLs) and programming-by-demonstration. Mainstream platforms like Quickbase, OutSystems, Power Apps, Airtable provide LLM-powered app/workflow/code-generation alongside visual/block-based development. Hybrid workflows allow alternating drag-and-drop with LLM code synthesis, auto-generating logic for blocks, and multi-agent orchestration like MetaGPT, ChatDev. Platforms like Flowise enable multimodal multi-agent orchestration via drag-and-drop. Key guidelines: expose fine-tuning and retrieval parameters via simple sliders (not code); support human-in-the-loop, audit trails, versioned workflows. 'Low-code LLM' framework features graphical interfaces with Planning LLM decomposing tasks into editable workflows, Low-Code GUI for visual editing (extend/add/remove steps, conditionals), Executing LLM following verified logic, increasing transparency and user alignment. Visual flow editors, form-based GUIs, hybrid interfaces. Recommendations include human-in-the-loop for traceability.

-----

-----

Phase: [EXPLORATION]

### Source [84]: https://arxiv.org/html/2510.19747v1

Query: How are no-code automation platforms and citizen developer tools evolving to incorporate hybrid LLM workflows and agents, particularly in relation to visual autonomy sliders and human verification interfaces?

Answer: Zero-code LLM platforms enable application building without coding via natural language, visual flows, or chat interfaces. Dedicated platforms (Dust.tt, Flowise, Cognosys) for AI agents/workflows; general (Bubble, Glide) integrate LLMs into visual app builders. Taxonomy: interface (chat/visual), backend (model-agnostic), output (agents/apps/workflows), extensibility (no-code/low-code hooks). Core features: agent support with tool use (Cognosys autonomous loops, Flowise agents), memory (RAG, session), workflow logic (branches/loops), API integrations. Platforms like Flowise use visual graph for LLM chains/tools; Dust.tt chains model calls/tools. Hybrid outputs blend apps with AI. Future: multimodal, better orchestration, multi-agent, human-AI collaboration. No explicit visual autonomy sliders or verification interfaces mentioned, but emphasizes human oversight in workflows.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://www.linkedin.com/posts/princi-koirala_andrej-karpathy-software-is-changing-again-activity-7363097845760962560-TJDU

Query: How are no-code automation platforms and citizen developer tools evolving to incorporate hybrid LLM workflows and agents, particularly in relation to visual autonomy sliders and human verification interfaces?

Answer: Andrej Karpathy discusses Software 3.0 with LLMs as new programming interface via natural language prompts. LLMs as utilities/OS with context windows as memory. Designing LLM apps with partial autonomy: Human-AI cooperation where AI generates, human verifies; fast generation-verification loops. Lessons from Tesla Autopilot: autonomy sliders for partial systems, keeping AI 'on the leash' with incremental changes over massive actions; teleoperation, humans in loop differently. Iron Man analogy: augmentation (suits) vs. agents (robots) - prefer augmentation. Vibe coding: everyone programmers via natural language. Agents as 'people spirits'. Emphasizes human verification in hybrid workflows.

-----

</details>

<details>
<summary>What optimization strategies from supply chain logistics, task decomposition, and parallel processing in operations research are being applied to improve efficiency in multi-agent deep research systems like Perplexity's?</summary>

Phase: [EXPLORATION]

### Source [86]: https://aiviewer.ai/tools/perplexity-computer/

Query: What optimization strategies from supply chain logistics, task decomposition, and parallel processing in operations research are being applied to improve efficiency in multi-agent deep research systems like Perplexity's?

Answer: Perplexity Computer employs optimization strategies akin to supply chain logistics, task decomposition, and parallel processing from operations research to enhance efficiency in its multi-agent deep research system. Key features include Autonomous Task Decomposition, where high-level objectives are independently broken into actionable subtasks without manual instructions, mirroring task decomposition in operations research for complex workflows. Parallel Agent Processing spawns concurrent sub-agents for independent subtasks, dramatically compressing time-to-completion, similar to parallel processing techniques that enable simultaneous research streams instead of sequential work. This is exemplified in the Operations Manager use case: evaluating vendors for a supply chain component involves parallel research streams for pricing, SLAs, financial stability, and references across five vendors, producing a structured comparison with quantitative and qualitative factors, akin to supply chain logistics optimization. Hierarchical coordination via Claude Opus 4.6 orchestrates these, handling dependencies and synthesizing results. Multi-model orchestration routes subtasks to optimal models (e.g., Gemini for research, GPT-5.2 for web searches), optimizing like logistics routing. Extended execution maintains context over hours to months, with intelligent check-ins, improving efficiency for complex projects like competitive analysis or market evaluation that traditionally take days.

-----

-----

Phase: [EXPLORATION]

### Source [87]: https://octogamma.com/perplexity-computer-orchestration/

Query: What optimization strategies from supply chain logistics, task decomposition, and parallel processing in operations research are being applied to improve efficiency in multi-agent deep research systems like Perplexity's?

Answer: Perplexity Computer applies parallel sub-agent processing, running multiple sub-agents concurrently to accelerate throughput on large projects, such as simultaneous data extraction, interview summarization, and draft generation, delivering faster time-to-insight, directly analogous to parallel processing in operations research. Autonomous workflow execution handles multi-step processes without continuous intervention, with end-to-end orchestration executing steps autonomously and in parallel where feasible, reducing latency for research-synthesis-execution akin to optimized supply chain flows. Multi-model orchestration automatically routes subtasks to specialized models, optimizing for capability and cost like logistics resource allocation. Persistent memory retains context across sessions for continuity, reducing redundancy. 400+ app integrations push outputs into business workflows, improving handoffs like supply chain coordination. These address problems like high latency in multi-step tasks and time wasted switching tools, via parallel agent execution and automatic routing, enhancing efficiency in multi-agent research systems.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="5-production-scaling-challenges-for-agentic-ai-in-2026-machi.md">
<details>
<summary>5 Production Scaling Challenges for Agentic AI in 2026 - MachineLearningMastery.com</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://machinelearningmastery.com/5-production-scaling-challenges-for-agentic-ai-in-2026/>

# 5 Production Scaling Challenges for Agentic AI in 2026 - MachineLearningMastery.com

In this article, you will learn about five major challenges teams face when scaling agentic AI systems from prototype to production in 2026.

Topics we will cover include:

- Why orchestration complexity grows rapidly in multi-agent systems.
- How observability, evaluation, and cost control remain difficult in production environments.
- Why governance and safety guardrails are becoming essential as agentic systems take real-world actions.

Let’s not waste any more time.

https://machinelearningmastery.com/wp-content/uploads/2026/03/mlm-davies-5-production-scaling-challenges-for-agentic-ai-2026.png

5 Production Scaling Challenges for Agentic AI in 2026

Image by Editor

## Introduction

Everyone’s [building agentic AI systems right now](https://machinelearningmastery.com/agent-evaluation-how-to-test-and-measure-agentic-ai-performance/), for better or for worse. The demos look incredible, the prototypes feel magical, and the pitch decks practically write themselves.

But here’s what nobody’s tweeting about: getting these things to actually work at scale, in production, with real users and real stakes, is a completely different game. The gap between a slick demo and a reliable production system has always existed in machine learning, but agentic AI stretches it wider than anything we’ve seen before.

These systems make decisions, take actions, and chain together complex workflows autonomously. That’s powerful, and it’s also terrifying when things go sideways at scale. So let’s talk about the five biggest headaches teams are running into as they try to scale agentic AI in 2026.

## 1\. Orchestration Complexity Explodes Fast

When you’ve got a single agent handling a narrow task, orchestration feels manageable. You define a workflow, [set some guardrails](https://bigid.com/blog/agentic-ai-guardrails/), and things mostly behave. But production systems rarely stay that simple. The moment you introduce multi-agent architectures in which agents delegate to other agents, retry failed steps, or dynamically choose which tools to call, you’re [dealing with orchestration complexity](https://machinelearningmastery.com/the-complete-ai-agent-decision-framework/) that grows almost exponentially.

Teams are finding that the coordination overhead between agents becomes the bottleneck, not the individual model calls. You’ve got agents waiting on other agents, race conditions popping up in async pipelines, and cascading failures that are genuinely hard to reproduce in staging environments. Traditional workflow engines [weren’t designed for this level of dynamic decision-making](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration), and most teams end up building custom orchestration layers that quickly become the hardest part of the entire stack to maintain.

The real kicker is that these systems behave differently under load. An orchestration pattern that works beautifully at 100 requests per minute [can completely fall apart at 10,000](https://www.techaheadcorp.com/blog/ways-multi-agent-ai-fails-in-production/). Debugging that gap requires a kind of systems thinking that most machine learning teams are still developing.

## 2\. Observability Is Still Way Behind

You can’t fix what you can’t see, and right now, most teams can’t see nearly enough of what their agentic systems are doing in production. Traditional machine learning monitoring tracks things like latency, throughput, and model accuracy. Those metrics still matter, but they barely scratch the surface of agentic workflows.

When an agent takes a 12-step journey to answer a user query, you need to understand every decision point along the way. Why did it choose Tool A over Tool B? Why did it retry step 4 three times? Why did the final output completely miss the mark, despite every intermediate step looking fine? The tracing infrastructure for this kind of deep observability is still immature. Most teams cobble together some combination of LangSmith, custom logging, and a lot of hope.

What makes it harder [is that agentic behavior is non-deterministic by nature](https://arxiv.org/abs/2505.20127). The same input can produce wildly different execution paths, which means you can’t just snapshot a failure and replay it reliably. Building robust observability for systems that are inherently unpredictable remains one of the biggest unsolved problems in the space.

## 3\. Cost Management Gets Tricky at Scale

Here’s something that catches a lot of teams off guard: agentic systems are expensive to run. Each agent action typically [involves one or more LLM calls](https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/), and when agents are chaining together dozens of steps per request, the token costs add up shockingly fast. A workflow that costs $0.15 per execution sounds fine until you’re processing 500,000 requests a day.

Smart teams are getting creative with cost optimization. They’re routing simpler sub-tasks to smaller, cheaper models while reserving the heavy hitters for complex reasoning steps. They’re caching intermediate results aggressively and building kill switches that terminate runaway agent loops before they burn through budget. But there’s a constant tension between cost efficiency and output quality, and finding the right balance requires ongoing experimentation.

The billing unpredictability is what really stresses out engineering leads. Unlike traditional APIs, where you can estimate costs pretty accurately, agentic systems have [variable execution paths that make cost forecasting genuinely difficult](https://arxiv.org/html/2508.11126v1). One edge case can trigger a chain of retries that costs 50 times more than the normal path.

## 4\. Evaluation and Testing Are an Open Problem

How do you test a system that can take a different path every time it runs? That’s the question keeping machine learning engineers up at night. Traditional software testing assumes deterministic behavior, and [traditional machine learning evaluation assumes a fixed input-output mapping](https://www.machinelearningmastery.com/how-to-connect-model-input-data-with-predictions-for-machine-learning/). Agentic AI breaks both assumptions simultaneously.

Teams are experimenting with a range of approaches. Some [are building LLM-as-a-judge pipelines](https://www.manuka-ai.co.uk/content-hub/evaluating-ai-agents-without-the-wait-how-llm-as-a-judge-accelerated-development) in which a separate model evaluates the agent’s outputs. Others are creating scenario-based test suites that check for behavioral properties rather than exact outputs. A few are investing in simulation environments where agents can be stress-tested against thousands of synthetic scenarios before hitting production.

But none of these approaches feels truly mature yet. The evaluation tooling is fragmented, benchmarks are inconsistent, and there’s no industry consensus on what “good” even looks like for a complex agentic workflow. Most teams end up relying heavily on human review, which obviously doesn’t scale.

## 5\. Governance and Safety Guardrails Lag Behind Capability

Agentic AI systems can take real actions in the real world. They can send emails, modify databases, execute transactions, and interact with external services. [The safety implications of that autonomy are significant](https://www.thomsonreuters.com/en-us/posts/technology/safeguarding-agentic-ai/), and governance frameworks haven’t kept pace with how quickly these capabilities are being deployed.

The challenge is implementing guardrails that are robust enough to prevent harmful actions without being so restrictive that they kill the usefulness of the agent. It’s a delicate balance, and most teams are learning through trial and error. Permission systems, [action approval workflows](https://machinelearningmastery.com/7-must-know-agentic-ai-design-patterns/), and scope limitations all add friction that can undermine the whole point of having an autonomous agent in the first place.

Regulatory pressure is mounting too. As agentic systems start making decisions that affect customers directly, questions about accountability, auditability, and compliance become urgent. Teams that aren’t thinking about governance now are going to hit painful walls when regulations catch up.

## Final Thoughts

Agentic AI is genuinely transformative, but the path from prototype to production at scale is littered with challenges that the industry is still figuring out in real time.

The good news is that the ecosystem is maturing quickly. Better tooling, clearer patterns, and hard-won lessons from early adopters are making the path a little smoother every month.

If you’re scaling agentic systems right now, just know that the pain you’re feeling is universal. The teams that invest in solving these foundational problems early are the ones that will build systems that actually hold up when it matters.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="andrej-karpathy-on-software-3-0-software-in-the-age-of-ai.md">
<details>
<summary>Andrej Karpathy on Software 3.0: Software in the Age of AI (UPDATED with Full Transcript)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.latent.space/p/s3>

# Andrej Karpathy on Software 3.0: Software in the Age of AI (UPDATED with Full Transcript)

### Annotated screenshots of Andrej's talk at YC AI Startup School 2025

Shawn swyx Wang

Jun 17, 2025

Update: you can watch the full talk on YouTube now!

Andrej Karpathy: Software Is Changing (Again) - YouTube

[Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ) 

https://yt3.ggpht.com/dGyATx87Fp_s1nZvnupUFSnMqbAPZ6nqRby9Esk1m6YE41iBq-9Z8iGoIgHTCT9SiDBUpP2V=s68-c-k-c0x00ffffff-no-rj

[Watch on](https://www.youtube.com/watch?v=LCEmiRjPEtQ)

Slides are here: [https://docs.google.com/presentation/d/1sZqMAoIJDxz79cbC5ap5v9jknYH4Aa9cFFaWL8Rids4/edit?usp=sharing](https://docs.google.com/presentation/d/1sZqMAoIJDxz79cbC5ap5v9jknYH4Aa9cFFaWL8Rids4/edit?usp=sharing)

* * *

[Lots](https://x.com/search?q=karpathy%20startup%20school&src=typed_query) of people were excited about Andrej’s talk at [YC AI Startup School](https://events.ycombinator.com/ai-sus) today. Sadly, I wasn’t invited. Talks will be published “ [over the next few weeks](https://x.com/karpathy/status/1935072460132811011)”, by which time the talk might be [deprecated](https://x.com/karpathy/status/1935077692258558443). Nobody seems to have recorded fancams.

But… it’s not over. You can just do things!

Using PeepResearch [™](https://x.com/swyx/status/1921992616448831754) I collated all available tweets about the talk and ordered [1](https://www.latent.space/p/s3#footnote-1) them using available hints from good notetakers (credited in last slide) **UPDATE**: and now we have [the full transcript](https://www.donnamagi.com/articles/karpathy-yc-talk)! I’ll go thru most of the impt takeaways here and **subscribers can get the full slides at the bottom.**

https://substackcdn.com/image/fetch/$s_!6-Ej!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4feb05c2-736a-471d-adf0-bc4123b536dd_2938x1696.png we’ll update this **to annotate** **the full talk video** when it’s up in a few weeks.

**UPDATE: Slides are now synced with the full transcript if you want to read thru**

https://substackcdn.com/image/fetch/$s_!2pmt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46bbef44-4ed9-4b52-983b-8fedb5a4bf76_2888x1688.png scroll to bottom for slides

* * *

## Part 0: Software 3.0 - Prompts are now Programs

We first discussed Software 3.0 in **[Rise of The AI Engineer](https://www.latent.space/p/ai-engineer)**, but it’s an obvious consequence of [the Software 2.0 essay](https://news.ycombinator.com/item?id=34881881) \+ “ [the hottest new programming language is English](https://x.com/karpathy/status/1617979122625712128)”.

https://substackcdn.com/image/fetch/$s_!_BDp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbfb3a323-ecd1-471a-92bd-38e09c2e7ba4_2670x1596.png

He originally wrote the Software 2.0 essay while observing that it was eating Software 1.0 at Tesla. And he’s back now to update it for Software 3.0.

In place of modifying the Software 2.0 chart like I did, Andrej debuts a new diagram showing the patchwork/coexistence of Software 1.0/2.0/3.0, noting that “ **Software 3.0 is eating 1.0/2.0**” and that “ **a huge amount of software will be rewritten**”:

https://substackcdn.com/image/fetch/$s_!5m5_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37f6dc0f-b8a8-4234-851e-75f851a0af4f_2896x1694.png

Andrej is still focused on prompts for programs, and we [slightly disagreed back in 2023](https://x.com/karpathy/status/1674873002314563584) and still do: the “ [1+2=3](https://www.latent.space/i/131896365/the-role-of-code-in-the-evolution-from-software-to-software)” variant of Software 3.0 is the entire reason why AI Engineers have far outperformed Prompt Engineers in the last few years and continue to do so.

https://substackcdn.com/image/fetch/$s_!Hf5V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffc11ca15-3919-4b89-81b1-f5959f5dd5a2_2772x1638.png

## Part 1: LLMs are the new computers

### LLMs are like Utilities

https://substackcdn.com/image/fetch/$s_!POb9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00bd8870-c055-4e3b-a392-c55153348567_2100x1166.png

### LLMs are like Fabs

https://substackcdn.com/image/fetch/$s_!vXAU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff66e305a-7c95-4ea0-9376-74f16dc3f2c6_2096x1134.png

### LLMs are like OSes

https://substackcdn.com/image/fetch/$s_!UhtK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F38efe115-99ef-4642-8792-7b8406d486e3_1982x936.png

https://substackcdn.com/image/fetch/$s_!F0Ii!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97198a48-bac3-4de9-a360-076d66c8547d_2036x1102.png

### LLMs are like Timeshare Mainframes…

https://substackcdn.com/image/fetch/$s_!ASqJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbe1704e-99d7-4573-9986-3b596fd8fb5c_2670x1300.png

although as he argues in [Power to the People](https://karpathy.bearblog.dev/power-to-the-people/), LLMs also exhibit some unusual reversal of the normal flow of expensive frontier tech:

https://substackcdn.com/image/fetch/$s_!yu0H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb64e530a-cc3c-44c6-8393-f83fcec470cb_2020x1096.png

As we leave the cloud for [Personal/Private AI](https://www.youtube.com/watch?v=jMoAaZP_Kkw&t=1s), some signs of Personal Computing v2 are being born in [Exolabs + Apple MLX](https://x.com/abeleinin/status/1935046342336036975/photo/1) work.

### Part 1 summary:

https://substackcdn.com/image/fetch/$s_!6e1-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe2aa8ade-7f06-4f5b-b268-89ffdc8e97d1_2048x1152.png

## Part 2: LLM Psychology

LLMs are “people spirits”: stochastic simulations of people, with a kind of emergent “psychology”

https://substackcdn.com/image/fetch/$s_!UJpg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e4dc78b-83d3-4578-a0bb-a60afcffc24a_2084x1114.png

Andrej highlights two problems with how current LLMs simulate people:

**Jagged Intelligence (** [https://x.com/karpathy/status/1816531576228053133](https://x.com/karpathy/status/1816531576228053133)) **:**

> The word I came up with to describe the (strange, unintuitive) fact that state of the art LLMs can both perform extremely impressive tasks (e.g. solve complex math problems) while simultaneously struggle with some very dumb problems. E.g. example from two days ago - which number is bigger, 9.11 or 9.9? Wrong.
>
> …
>
> **Some things work extremely well (by human standards) while some things fail catastrophically (again by human standards), and it's not always obvious which is which, though you can develop a bit of intuition over time.** Different from humans, where a lot of knowledge and problem solving capabilities are all highly correlated and improve linearly all together, from birth to adulthood.
>
> Personally I think these are not fundamental issues. They demand more work across the stack, including not just scaling. T **he big one I think is the present lack of "cognitive self-knowledge", which requires more sophisticated approaches in model post-training instead of the naive "imitate human labelers and make it big" solutions that have mostly gotten us this far**. For an example of what I'm talking about, see Llama 3.1 paper section on mitigating hallucinations: https://x.com/karpathy/status/1816171241809797335
>
> For now, this is something to be aware of, especially in production settings. Use LLMs for the tasks they are good at but be on a lookout for jagged edges, and keep a human in the loop.

**Anterograde Amnesia (** [https://x.com/karpathy/status/1930003172246073412](https://x.com/karpathy/status/1930003172246073412) **):**

> I like to talk explain it as LLMs are a bit like a coworker with Anterograde amnesia - they don't consolidate or build long-running knowledge or expertise once training is over and all they have is short-term memory (context window). It's hard to build relationships (see: 50 First Dates) or do work (see: Memento) with this condition.
>
> https://substackcdn.com/image/fetch/$s_!xpM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8318487-d293-414b-8e08-c5e70b313d46_2062x1338.png
>
> The first mitigation of this deficit that I saw is the Memory feature in ChatGPT, which feels like a primordial crappy implementation of what could be, and which led me to suggest this as a possible new paradigm of learning here: [https://x.com/karpathy/status/1921368644069765486](https://x.com/karpathy/status/1921368644069765486)
>
> > We're missing (at least one) major paradigm for LLM learning. Not sure what to call it, possibly it has a name - **system prompt learning**?
> >
> > Pretraining is for knowledge.
> >
> > Finetuning (SL/RL) is for habitual behavior.
> >
> > Both of these involve a change in parameters but a lot of human learning feels more like a change in system prompt. You encounter a problem, figure something out, then "remember" something in fairly explicit terms for the next time. E.g. "It seems when I encounter this and that kind of a problem, I should try this and that kind of an approach/solution". It feels more like taking notes for yourself, i.e. **something like the "Memory" feature but not to store per-user random facts, but general/global problem solving knowledge and strategies.** LLMs are quite literally like the guy in Memento, except we haven't given them their scratchpad yet. Note that **this paradigm is also significantly more powerful and data efficient because a knowledge-guided "review" stage is a significantly higher dimensional feedback channel than a reward scaler.**
> >
> > …
> >
> > Imo this is not the kind of problem solving knowledge that should be baked into weights via Reinforcement Learning, or least not immediately/exclusively. And it certainly shouldn't come from human engineers writing system prompts by hand. **It should come from System Prompt learning, which resembles RL in the setup, with the exception of the learning algorithm (edits vs gradient descent)**. A large section of the LLM system prompt could be written via system prompt learning, it would look a bit like the LLM writing a book for itself on how to solve problems **. If this works it would be a new/powerful learning paradigm.** With a lot of details left to figure out (how do the edits work? can/should you learn the edit system? how do you gradually move knowledge from the explicit system text to habitual weights, as humans seem to do? etc.).

**Part 2 Summary:**

https://substackcdn.com/image/fetch/$s_!nSkP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52b60959-cb5a-42b7-9592-c7f0412c2c5c_1796x1064.png

## Part 3: Partial Autonomy

https://substackcdn.com/image/fetch/$s_!ebLx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff01b5d84-6abb-4e80-a6d1-4fd2d58daef2_2028x1132.png

We like the Iron Man Suit analogy — the suit extends us in two useful ways:

- Augmentation: giving the user strength, tools, sensors and information

- Autonomy: the suit at many times has a mind of its own- taking actions without being prompted


How can we design AI products that follow these patterns?

### Part 3a: Autonomy Sliders

The **Autonomy Slider** is an important concept that lets us choose the level of autonomy for the context, eg:

- **Cursor**: Tab -> cmd+K -> Cmd+L -> Cmd+I (agent mode)

- **Perplexity**: search -> research -> deep research

- **Tesla** Autopilot: Level 1 to Level 4


https://substackcdn.com/image/fetch/$s_!Vgtd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F131f6c2f-e059-4d79-a7b3-440191870891_2022x876.png

https://substackcdn.com/image/fetch/$s_!c3Qu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F074e6d7d-b491-4d80-9d9d-1b6e236731e2_2034x808.png

https://substackcdn.com/image/fetch/$s_!EinW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F25c8935e-a7df-4b01-a660-f99871df3bd2_1146x656.png

### Part 3b: Human-AI Generation-Verification Loop

In the Generation <-> verification cycle, we a need full workflow of partial autonomy - the faster the loop the better:

- **To improve verification**: Make it easy, fast to win

- **To improve generation**: Keep AI on tight leash


https://substackcdn.com/image/fetch/$s_!dg5M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d4c0207-f4e5-4a7b-b69b-7a0717b55282_2048x1536.png

### Part 3c: The Demo-Product Gap

The reason we need PARTIAL autonomy is because of the significant gap still between a working demo and a reliable product.

He [recounts](https://x.com/ethanniser/status/1935056628350599473) riding a Waymo prototype with zero interventions in 2014 and thinking that self-driving is “here”… but there was still a lot to work out.

> **"Demo is works.any(), product is works.all()"**

https://substackcdn.com/image/fetch/$s_!Z85f!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9890b449-073f-44c3-ae3c-21caa2052626_2634x1520.png

## Part 4: Vibe Coding

The tweet that launched a thousand startups:

https://substackcdn.com/image/fetch/$s_!G97n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e1b7835-b594-44d1-a9cb-b5dc4329c374_2048x1536.png

now [has its own Wikipedia page](https://en.wikipedia.org/wiki/Vibe_coding)!

However, there are still a lot of remaining issues. While [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/), he found that the AI speedups vanished shortly after getting local code running:

https://substackcdn.com/image/fetch/$s_!rHzD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc531c163-8e1f-4066-ab10-4cacb14ccd72_2048x1536.png

The [reality of building web apps in 2025](https://x.com/karpathy/status/1905051558783418370) is a disjoint mess of services that are very much designed for webdev experts to keep their jobs, and not accessible to AI.

Poor old Clerk got a NEGATIVE mention, and Vercel’s @leerob a positive one, in how their docs approaches will respectively tuned for humans vs agents.

https://substackcdn.com/image/fetch/$s_!_wm7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F09b77458-d0fe-45ce-af2a-094ce898de0b_1480x1070.png

## Part 5: Build for Agents

**The bottom line** is that toolmakers must realize that “there is new category of consumer/manipulator of digital information”:

1\. Humans (GUls)

2\. Computers (APls)

**3\. NEW: Agents <- computers... but human-like**

https://substackcdn.com/image/fetch/$s_!KUGg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd93ae423-972e-4576-8a88-ebf3a7f79b21_2048x1152.png

Concretely: having llms.txt works because HTML is not very parseable for LLMs.

https://substackcdn.com/image/fetch/$s_!kXCV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fccc58150-ca34-471f-abb5-6bb159ca4d53_1638x902.png

He also shouted out “Context builders” like Gitingest and Cognition’s DeepWiki, which we profiled for a lightning pod:

DeepWiki: The GitHub Encyclopedia - YouTube

[DeepWiki: The GitHub Encyclopedia](https://www.youtube.com/watch?v=cX4-e25xQhg) 

https://yt3.ggpht.com/pSTHcffCXEverYEPdjM0iIRPH-IUT4d2biIMZ_Z7bhyf6sME-laFer9vEfpFbM5tqFYJV-UsLQ=s68-c-k-c0x00ffffff-no-rj

[Watch on](https://www.youtube.com/watch?v=cX4-e25xQhg)

## Closing / Recap

This is the Decade of Agents.

https://substackcdn.com/image/fetch/$s_!_oGS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b1b8a05-5dae-42d5-843e-4568ff60306f_2385x1216.png

Less AGI 2027 and flashy demos that don’t work.

More partial autonomy, custom GUIs and autonomy sliders.

https://substackcdn.com/image/fetch/$s_!396e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e0d797a-0c33-41bc-83f6-89141c959468_1922x1447.png

Remember that Software 3.0 is eating Software 1/2, that their Utility/Fabs/OS characteristics will dictate their destiny, improve the generator-verifier loop, and **BUILD FOR AGENTS 🤖**.

https://substackcdn.com/image/fetch/$s_!rpf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff72d6a56-dff2-4b7f-9b49-4d5ab842bc54_2286x1336.png

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="evaluator-optimizer-llm-workflow-a-pattern-for-self-improvin.md">
<details>
<summary>Evaluator-Optimizer LLM Workflow: A Pattern for Self-Improving AI Systems</summary>

Phase: [EXPLORATION]

**Source URL:** <https://sebgnotes.substack.com/p/evaluator-optimizer-llm-workflow>

# Evaluator-Optimizer LLM Workflow: A Pattern for Self-Improving AI Systems

### My thoughts on The Anthropic Cookbook's Jupyter notebook showcasing the Evaluator-Optimizer LLM Workflow

https://images.unsplash.com/photo-1490567674331-72de84794694?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D _Image Source: [David Streit](https://unsplash.com/photos/multicolored-abstract-illustration-BumOnw4oEZo)_

## **Link**

Article: **[Evaluator-Optimizer Workflow, Jupyter Notebook](https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/evaluator_optimizer.ipynb)**

## **What the article covers**

> _**The Anthropic Cookbook provides code and guides designed to help developers build with Claude, offering copy-able code snippets that you can easily integrate into your own projects.**_
>
> _**”Building Effective Agents Cookbook” - Reference implementation for Building Effective Agents by Erik Schluntz and Barry Zhang.**_
>
> _**Evaluator-Optimizer Workflow: In this workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.**_
>
> _**This workflow is particularly effective when we have: Clear evaluation criteria Value from iterative refinement**_
>
> _**The two signs of good fit are: LLM responses can be demonstrably improved when feedback is provided The LLM can provide meaningful feedback itself**_

## **My Thoughts**

### **Context**

I’ve been diving into the Anthropic Cookbook lately, exploring different patterns for building AI systems.

The Cookbook itself is a goldmine of practical implementations, providing ready-to-use code for building with Claude.

The Evaluator-Optimizer pattern caught my attention because it represents something I’ve been thinking about: how do we move from static prompt engineering to truly dynamic AI systems?

What makes this particular pattern fascinating is how it approaches the challenge of creating self-improving AI systems.

### **Key Insight**

The key insight here is elegant in its simplicity: use one LLM to generate solutions and another to evaluate them in a continuous feedback loop until a success criteria is passed.

This separation of concerns is more powerful than it might first appear.

1.  **Pattern Recognition**: This represents a shift from static to dynamic AI implementations

2.  **Strategic Value**: Enables scalable, self-improving systems while maintaining control

3.  **Implementation Path**: Start simple, evolve with confidence

4.  **Future Direction**: Framework for building learning systems, not just response systems

Let’s take a look at the key components needed to make the Evaluator Optimizer LLM Workflow work.

### **Key Components**

1.  **Generator**: Create solutions based on the task and initial examples (if given) and later previous feedback

2.  **Evaluator**: Assesses solutions against explicit criteria

3.  **Feedback Loop**: Enables iterative refinement

4.  **Success Criteria**: Defines when to exit the loop

Though the components seem straightforward, implementing them effectively requires careful consideration of several key technical factors.

### **Technical Implementation Framework**

The Evaluator-Optimizer pattern requires careful attention to both immediate technical requirements and long-term operational considerations.

Here’s a comprehensive framework that covers key implementation aspects:

1.  Rigorous Loop run and exit criteria

- Implement circuit breakers to prevent infinite loops

- Implement circuit breakers to prevent resource exhaustion (each LLM generation & evaluation costs time and money)

- The explicit separation of generation and evaluation prompts

2.  Clear generation guidelines

- LLM needs to be given context for what needs to be generated while encouraged to be creative

- Examples can be given initially (no examples = zero shot, 1 example = one shot, 2+ examples = few shot)

- Structure generator prompts to encourage exploration within bounded constraints

3.  Clear evaluation criteria

- LLM needs to be given context for how to evaluate (and what not to add, like trying to generate a solution itself)

- Examples can be given initially (no examples = zero shot, 1 example = one shot, 2+ examples = few shot)

- Evaluation Criteria must be both machine-readable and business-relevant

4.  Clear success conditions and failure recovery

- Enable graceful degradation (stopping if no solution or loop until solution is found)

- Embed Quality Assurance direction into the system architecture rather than applied after (this can be human oversight and intervention or autonomous LLM oversight and intervention)

- Fall back to simpler responses when optimal solutions aren’t found

5.  Measuring Success

- Monitoring and Observability to ensure system quality

- Memory management of the Chain of Thought

- Keeping track of experiments (both immediate improvements and long-term learning patterns)

6.  Long Term Evaluation

- Are generated solutions similar enough that answers can be cached/saved

- As business goals evolve, how do the solutions evolve

- Does the evaluator hallucinate success and/or failure (Type 1 and type 2 errors)

While these technical considerations above are crucial, we must also carefully evaluate the operational costs:

7.  Cost Evaluation

- Monetary: Cost of running a loop of LLM API Calls

- Time: Latency of letting the loop run its course (the fast and slow improvement cycles)

- Failure: How costly is a non-successful loop?

  - Direct costs (wasted compute)

  - Indirect costs (incorrect solutions making it to production)

  - Opportunity costs (time spent in failed loops)

The real power of this pattern becomes apparent when we consider its broader applications.

### **Strategic Implications**

1.  Technical Evolution:

- Self-improving systems are now feasible at the application level

- Shift from static to dynamic AI implementations

- Decreased focus on implementation and increased focus on goal description and achievement

2.  Governance & Control:

- Autonomous quality control with reduced human oversight

- Natural checkpoints for audit trails and governance

- Progressive automation pathways (start with human oversight and remove it slowly as trust in the solution grows)

3.  Business Matters:

- This pattern enables AI systems that can improve autonomously while maintaining alignment with business objectives

- Organizations can implement progressive automation strategies that start simple and grow in sophistication

- The explicit separation of generation and evaluation creates natural points for human oversight and intervention

- Teams can focus on defining success criteria rather than perfecting prompts, leading to more scalable AI implementations

- The pattern provides a framework for balancing innovation (generator) with consistency (evaluator)

### **Key Takeaways for AI Engineers**

- Quality assurance can be embedded directly into the system architecture rather than applied as an afterthought

- The evaluator-optimizer pattern can be applied at multiple scales ranging from single responses to entire conversation flows

- System design should account for both “fast” (single iteration) and “slow” (multiple iteration) improvement cycles

- Engineers should focus on designing robust evaluation criteria rather than perfect generation prompts

- The pattern enables graceful degradation so that systems can fall back to simpler responses when optimal solutions aren’t found

## **Forward-Looking Applications**

With this implementation framework in mind, let’s explore some practical applications of this pattern:

### **Example Use Cases**

- Autonomous code review and improvement

- Content generation with quality guarantees

- Self-improving chatbot responses

- Automated documentation refinement

### **Integration Opportunities**

- CI/CD pipelines for LLM applications

- Quality assurance automation

- Progressive system improvement

- Governance and audit trails

## **Personal Notes**

When I recently implemented this pattern, I found that the key to success wasn’t in perfecting the prompts but in designing comprehensive evaluation criteria.

This matches a broader pattern in AI engineering: focus on clearly defining success and letting the system explore paths to achieve it.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="gemini-cli-gemini-for-google-cloud-google-cloud-documentatio.md">
<details>
<summary>Gemini CLI</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://docs.cloud.google.com/gemini/docs/codeassist/gemini-cli>

# Gemini CLI

The [Gemini command line interface (CLI)](https://geminicli.com/docs/) is an open source
AI agent that provides access to Gemini directly in your terminal. The
Gemini CLI uses a reason and act (ReAct) loop with your built-in tools
and local or remote MCP servers to complete complex use cases like fixing bugs,
creating new features, and improving test coverage. While the Gemini
CLI excels at coding, it's also a versatile local utility that you can use for
a wide range of tasks, from content generation and problem solving to deep
research and task management.

Each [Gemini Code Assist edition](https://docs.cloud.google.com/gemini/docs/codeassist/overview)
provides [quotas](https://geminicli.com/docs/quota-and-pricing/) for using the
Gemini CLI. Note that these quotas are shared between Gemini
CLI and [Gemini Code Assist agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode). Gemini
CLI also supports using a Gemini API key to
[pay as you go](https://geminicli.com/docs/quota-and-pricing/#pay-as-you-go).

The Gemini CLI is available without additional setup in
[Cloud Shell](https://docs.cloud.google.com/shell/docs/use-cloud-shell-terminal). To get
started with Gemini CLI in other environments, see the
[Gemini CLI documentation](https://geminicli.com/docs/).

### Privacy

For users of Gemini Code Assist Standard and Enterprise, the
data protection and privacy practices described in
[Security, privacy, and compliance for Gemini Code Assist Standard and Enterprise](https://docs.cloud.google.com/gemini/docs/codeassist/security-privacy-compliance)
also apply to Gemini CLI.

## Gemini Code Assist agent mode (Preview)

[Gemini Code Assist agent mode](https://docs.cloud.google.com/gemini/docs/codeassist/agent-mode) in VS Code is powered by
Gemini CLI. A subset of Gemini CLI functionality is
available directly in the Gemini Code Assist chat within VS Code.

The following Gemini CLI features are available in
Gemini Code Assist for VS Code.

- [Model Context Protocol (MCP) servers](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#configure-mcp-servers)
- Gemini CLI [commands](https://geminicli.com/docs/cli/commands/): `/memory`, `/stats`, `/tools`,
`/mcp`
- [Yolo mode](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer#yolo-mode)
- built-in tools like grep, terminal, file read or file write
- Web search
- Web fetch

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="google-announces-gemini-cli-your-open-source-ai-agent.md">
<details>
<summary>Gemini CLI: your open-source AI agent</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-cli-open-source-ai-agent/>

# Gemini CLI: your open-source AI agent

For developers, the command line interface (CLI) isn't just a tool; it's home. The terminal’s efficiency, ubiquity and portability make it the go-to utility for getting work done. And as developers' reliance on the terminal endures, so does the demand for integrated AI assistance.

That’s why we’re introducing [Gemini CLI](http://github.com/google-gemini/gemini-cli), an open-source AI agent that brings the power of Gemini directly into your terminal. It provides lightweight access to Gemini, giving you the most direct path from your prompt to our model. While it excels at coding, we built Gemini CLI to do so much more. It’s a versatile, local utility you can use for a wide range of tasks, from content generation and problem solving to deep research and task management.

We’ve also integrated Gemini CLI with Google’s AI coding assistant, [Gemini Code Assist](https://codeassist.google/), so that all developers — on free, Standard, and Enterprise Code Assist plans — get prompt-driven, AI-first coding in both VS Code and Gemini CLI.

https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Gemini_CLI_GIF.gif

## Unmatched usage limits for individual developers

To use Gemini CLI free-of-charge, simply login with a personal Google account to get a free Gemini Code Assist license. That free license gets you access to Gemini 2.5 Pro and its massive 1 million token context window. To ensure you rarely, if ever, hit a limit during this preview, we offer the industry’s largest allowance: 60 model requests per minute and 1,000 requests per day at no charge.

If you’re a professional developer who needs to run multiple agents simultaneously, or if you prefer to use specific models, you can use a [Google AI Studio](https://aistudio.google.com/apikey) or [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal) key for usage-based billing or get a Gemini Code Assist Standard or Enterprise license.

https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_CLI_infographic.width-100.format-webp.webp

Gemini CLI offers the industry’s largest usage allowance at 60 model requests per minute and 1,000 model requests per day at no charge

## Powerful models in your command line

Now in preview, Gemini CLI provides powerful AI capabilities, from code understanding and file manipulation to command execution and dynamic troubleshooting. It offers a fundamental upgrade to your command line experience, enabling you to write code, debug issues and streamline your workflow with natural language.

Its power comes from built-in tools allowing you to:

- **Ground prompts with Google Search** so you can fetch web pages and provide real-time, external context to the model
- **Extend Gemini CLI’s capabilities** through built-in support for the Model Context Protocol (MCP) or bundled extensions
- **Customize prompts and instructions** to tailor Gemini for your specific needs and workflows
- **Automate tasks and integrate with existing workflows** by invoking Gemini CLI non-interactively within your scripts

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GenMedia_demo_keyword.mp4) and watch it with your favorite video player!

Gemini CLI can be used for a wide variety of tasks, including making a short video showing the story of a ginger cat’s adventures around Australia with Veo and Imagen

## Open and extensible

Because Gemini CLI is fully [open source (Apache 2.0)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE), developers can inspect the code to understand how it works and verify its security implications. We fully expect (and welcome!) a global community of developers to [contribute to this project](https://github.com/google-gemini/gemini-cli/blob/main/CONTRIBUTING.md) by reporting bugs, suggesting features, continuously improving security practices and submitting code improvements. [Post your issues](http://github.com/google-gemini/gemini-cli/issues) or [submit your ideas](http://github.com/google-gemini/gemini-cli/discussions) in our GitHub repo.

We also built Gemini CLI to be extensible, building on emerging standards like MCP, system prompts (via GEMINI.md) and settings for both personal and team configuration. We know the terminal is a personal space, and everyone deserves the autonomy to make theirs unique.

## Shared technology with Gemini Code Assist

Sometimes, an IDE is the right tool for the job. When that time comes, you want all the capabilities of a powerful AI agent by your side to iterate, learn and overcome issues quickly.

[Gemini Code Assist](https://codeassist.google/), Google’s AI coding assistant for students, hobbyists and professional developers, now shares the same technology with Gemini CLI. In VS Code, you can place any prompt into the chat window using agent mode, and Code Assist will relentlessly work on your behalf to write tests, fix errors, build out features or even migrate your code. Based on your prompt, Code Assist’s agent will build a multi-step plan, auto-recover from failed implementation paths and recommend solutions you may not have even imagined.

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/gemini_cli_code_assist_demo_cut.mp4) and watch it with your favorite video player!

Gemini Code Assist’s chat agent is a multi-step, collaborative, reasoning agent that expands the capabilities of simple-command response interactions

Gemini Code Assist agent mode is available at no additional cost for all plans (free, Standard and Enterprise) through the [Insiders channel](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#before-you-begin). If you aren’t already using Gemini Code Assist, give it a try. Its free tier has the highest usage limit in the market today, and only takes less than a minute to [get started](https://codeassist.google/).

## Easy to get started

So what are you waiting for? Upgrade your terminal experience with Gemini CLI today. Get [started by installing Gemini CLI.](http://github.com/google-gemini/gemini-cli) All you need is an email address to get Gemini practically unlimited in your terminal.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="large-language-models-for-multi-robot-systems-a-survey.md">
<details>
<summary>Large Language Models for Multi-Robot Systems: A Survey</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2502.03814v4>

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2502.03814v4 \[cs.RO\]

\\equalcont

These authors contributed equally to this work.

\\equalcont

These authors contributed equally to this work.

\[\]\\fnmLifeng \\surZhou∗

\]\\orgdivDepartment of Electrical and Computer Engineering, \\orgnameDrexel University, \\orgaddress\\street3141 Chestnut Street, \\cityPhiladelphia, \\postcode19104, \\statePA, \\countryUSA

# Large Language Models for Multi-Robot Systems: A Survey

\\fnmPeihan \\surLi
[pl525@drexel.edu](mailto:pl525@drexel.edu)\\fnmZijian \\surAn
[za382@drexel.edu](mailto:za382@drexel.edu)\\fnmShams \\surAbrar
[sa3868@drexel.edu](mailto:sa3868@drexel.edu)[lz457@drexel.edu](mailto:lz457@drexel.edu)\[


###### Abstract

The rapid advancement of Large Language Models (LLMs) has opened new possibilities in Multi-Robot Systems (MRS), enabling enhanced communication, task planning, and human-robot interaction. Unlike traditional single-robot and multi-agent systems, MRS poses unique challenges, including coordination, scalability, and real-world adaptability. This survey provides the first comprehensive exploration of LLM integration into MRS. It systematically categorizes their applications across high-level task allocation, mid-level motion planning, low-level action generation, and human intervention. We highlight key applications in diverse domains, such as household robotics, construction, formation control, target tracking, and robot games, showcasing the versatility and transformative potential of LLMs in MRS.
Furthermore, we examine the challenges that limit adapting LLMs in MRS, including mathematical reasoning limitations, hallucination, latency issues, and the need for robust benchmarking systems. Finally, we outline opportunities for future research, emphasizing advancements in fine-tuning, reasoning techniques, and task-specific models. This survey aims to guide researchers in the intelligence and real-world deployment of MRS powered by LLMs. Based on the fast-evolving nature of research in the field, we keep updating the papers in the open-source [GitHub repository](https://github.com/Zhourobotics/LLM-MRS-survey "").


###### keywords:

Large Language Models, Multi-Robot Systems, Task Allocation and Planning, Motion Planning, Action Generation

\\declare

Competing Interests: The authors declare no competing interests.

## 1 Introduction

The rapid advancement of Large Language Models (LLMs) has significantly impacted various fields, including natural language processing and robotics. Initially designed for text generation and completion tasks, LLMs have evolved to demonstrate problem-understanding and problem-solving capabilities \[ [139](https://arxiv.org/html/2502.03814v4#bib.bib139 ""), [121](https://arxiv.org/html/2502.03814v4#bib.bib121 "")\]. This evolution is particularly vital for enhancing robot intelligence by enabling robots to process information and make decisions on coordination and action accordingly \[ [53](https://arxiv.org/html/2502.03814v4#bib.bib53 ""), [45](https://arxiv.org/html/2502.03814v4#bib.bib45 "")\]. With these capabilities, robots can more effectively interpret complex instructions, interact with humans, collaborate with robotic teammates, and adapt to dynamic environments \[ [116](https://arxiv.org/html/2502.03814v4#bib.bib116 "")\]. As robotic systems evolve toward more sophisticated applications, integrating LLMs has become a transformative step, bridging the gap between high-level reasoning and real-world robotic tasks.

https://arxiv.org/html/2502.03814v4/figures/LLM-MRS.pngFigure 1: Overview of the applications of LLMs in MRS as introduced in Sec. [4](https://arxiv.org/html/2502.03814v4#S4 "4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey").

On the other hand, Multi-Robot Systems (MRS), which consist of multiple autonomous robots working collaboratively \[ [95](https://arxiv.org/html/2502.03814v4#bib.bib95 ""), [8](https://arxiv.org/html/2502.03814v4#bib.bib8 "")\], have shown great potential in applications such as environmental monitoring \[ [81](https://arxiv.org/html/2502.03814v4#bib.bib81 ""), [24](https://arxiv.org/html/2502.03814v4#bib.bib24 ""), [110](https://arxiv.org/html/2502.03814v4#bib.bib110 "")\], warehouse automation \[ [67](https://arxiv.org/html/2502.03814v4#bib.bib67 ""), [111](https://arxiv.org/html/2502.03814v4#bib.bib111 ""), [99](https://arxiv.org/html/2502.03814v4#bib.bib99 "")\], and large-scale exploration \[ [12](https://arxiv.org/html/2502.03814v4#bib.bib12 ""), [27](https://arxiv.org/html/2502.03814v4#bib.bib27 "")\]. Unlike single-robot systems, MRS leverages collective intelligence to achieve high scalability, resilience, and efficiency \[ [95](https://arxiv.org/html/2502.03814v4#bib.bib95 "")\]. The distributed nature of tasks across multiple robots allows these systems to be cost-effective by relying on simpler, specialized robots instead of a single highly versatile one. Moreover, MRS provides increased robustness, as the redundancy and adaptability of the collective can often mitigate the failures of individual robots \[ [149](https://arxiv.org/html/2502.03814v4#bib.bib149 ""), [73](https://arxiv.org/html/2502.03814v4#bib.bib73 "")\]. These features make MRS indispensable in scenarios where the scale, complexity, or risk is beyond the capabilities of a single robot.

Despite their importance, MRS introduces unique challenges, such as ensuring robot communication, maintaining coordination in dynamic and uncertain environments, and making collective decisions that adapt to real-time conditions \[ [30](https://arxiv.org/html/2502.03814v4#bib.bib30 ""), [6](https://arxiv.org/html/2502.03814v4#bib.bib6 "")\]. Researchers are working to integrate LLMs into MRS to address the unique challenges associated with deploying and coordinating MRS \[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 ""), [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\]. For example, effective communication is essential for the MRS to share knowledge, coordinate tasks, and maintain cohesion in the dynamic environment among individual robots \[ [30](https://arxiv.org/html/2502.03814v4#bib.bib30 "")\]. LLMs can provide a natural language interface for inter-robot communication, allowing robots to exchange high-level information more intuitively and efficiently instead of predefined communication structures and protocols \[ [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\]. Furthermore, the problem-understanding and problem-solving abilities of LLM can enhance the adaptability of MRS when given a particular goal without specific instructions. The LLMs can understand the mission, divide it into sub-tasks, and assign them to individual robots within the team based on their capabilities \[ [74](https://arxiv.org/html/2502.03814v4#bib.bib74 ""), [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\]. The generalization ability across different contexts of LLMs can also allow MRS to adapt to new scenarios without extensive reprogramming, making them highly flexible during the deployment \[ [120](https://arxiv.org/html/2502.03814v4#bib.bib120 ""), [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\].

The application of LLMs in MRS also aligns with the growing need for human-robot collaboration \[ [44](https://arxiv.org/html/2502.03814v4#bib.bib44 "")\]. As the operators often do not have expertise in robot systems, using LLMs as a shared interface can enable operators using natural languages to communicate and command the robots to make decisions and complete complex real-world missions \[ [2](https://arxiv.org/html/2502.03814v4#bib.bib2 "")\]. These capabilities enhance the efficiency of MRS and broaden their applicability to domains requiring close human-robot collaboration.

Our paper is inspired by the survey \[ [35](https://arxiv.org/html/2502.03814v4#bib.bib35 "")\] that comprehensively reviewed LLMs for multi-agent systems where abstract agents primarily serve virtual roles. Multi-agent systems differ from MRS in that the former emphasizes the roles of the agents, while the latter focuses on the interactions between the robots and the physical world. The limited coverage we find regarding MRS in their work pertains to LLM-embodied agents, but it still skims over related work and lacks detailed summaries. Hence, we recognize the necessity of summarizing recent works on using LLMs in MRS for decision-making, task planning, human-robot collaboration, and task execution. Fig. [1](https://arxiv.org/html/2502.03814v4#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Large Language Models for Multi-Robot Systems: A Survey") illustrates the four categories outlined in this survey paper. We hope this survey can assist researchers in understanding the current progress of using LLMs in MRS, the challenges we face, and the potential opportunities to enhance multi-robot collective intelligence.

We structured our survey paper as follows to better provide a comprehensive introduction to researchers interested in applying LLMs to MRS. Sec. [2](https://arxiv.org/html/2502.03814v4#S2 "2 Backgrounds ‣ Large Language Models for Multi-Robot Systems: A Survey") lays the background for the MRS and LLMs for individuals to understand the topics better. Also, we summarize and compare several other existing survey papers about applying LLMs in robotics systems and multi-agent systems in general and explain the necessity of our work on MRS. Then, Sec. [3](https://arxiv.org/html/2502.03814v4#S3 "3 Communication Types for LLMs in Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey") reviews the communication structure among the LLMs in the MRS. After that, we review the usage of LLMs in three levels: (1) high-level task allocation and planning, (2) mid-level motion planning, and (3) low-level action execution in Sec. [4](https://arxiv.org/html/2502.03814v4#S4 "4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"). Following reviewing the usage of LLMs, we review based on the applications of the MRS embodied by the LLMs in the real world in Sec. [5](https://arxiv.org/html/2502.03814v4#S5 "5 Application ‣ Large Language Models for Multi-Robot Systems: A Survey"). In Sec. [6](https://arxiv.org/html/2502.03814v4#S6 "6 LLMs, Simulations, and Benchmarks ‣ Large Language Models for Multi-Robot Systems: A Survey"), we summarize the existing benchmark standards for evaluating the performance of LLMs in MRS and the existing simulation environments. In Sec. [7](https://arxiv.org/html/2502.03814v4#S7 "7 Challenges, and Opportunities ‣ Large Language Models for Multi-Robot Systems: A Survey"), we identify the challenges and limitations we face and the opportunities and future directions to enhance the LLMs’ ability to handle MRS coordination and decision-making. Finally, we conclude our paper in Sec. [8](https://arxiv.org/html/2502.03814v4#S8 "8 Conclusion ‣ Large Language Models for Multi-Robot Systems: A Survey").

## 2 Backgrounds

This section provides background knowledge on MRS and LLMs. While several other research papers have discussed on the applications of LLMs in robotic systems, they do not specifically focus on the MRS. We will summarize their contributions and discuss why our survey on facilitating LLMs with MRS is necessary and impactful.

### 2.1 Multi-Robot Systems

A MRS consists of multiple robots that collaborate to complete specific tasks. Unlike single-robot systems, MRS leverages the combined capabilities of multiple robots to perform complex tasks more efficiently, reliably, and flexibly \[ [5](https://arxiv.org/html/2502.03814v4#bib.bib5 ""), [98](https://arxiv.org/html/2502.03814v4#bib.bib98 ""), [147](https://arxiv.org/html/2502.03814v4#bib.bib147 "")\]. These systems are commonly employed in applications such as search and rescue \[ [8](https://arxiv.org/html/2502.03814v4#bib.bib8 ""), [78](https://arxiv.org/html/2502.03814v4#bib.bib78 ""), [55](https://arxiv.org/html/2502.03814v4#bib.bib55 ""), [95](https://arxiv.org/html/2502.03814v4#bib.bib95 "")\], target tracking \[ [144](https://arxiv.org/html/2502.03814v4#bib.bib144 ""), [146](https://arxiv.org/html/2502.03814v4#bib.bib146 ""), [136](https://arxiv.org/html/2502.03814v4#bib.bib136 ""), [63](https://arxiv.org/html/2502.03814v4#bib.bib63 ""), [71](https://arxiv.org/html/2502.03814v4#bib.bib71 "")\], environmental monitoring \[ [101](https://arxiv.org/html/2502.03814v4#bib.bib101 ""), [33](https://arxiv.org/html/2502.03814v4#bib.bib33 "")\], coverage and exploration \[ [12](https://arxiv.org/html/2502.03814v4#bib.bib12 ""), [105](https://arxiv.org/html/2502.03814v4#bib.bib105 ""), [103](https://arxiv.org/html/2502.03814v4#bib.bib103 ""), [75](https://arxiv.org/html/2502.03814v4#bib.bib75 ""), [13](https://arxiv.org/html/2502.03814v4#bib.bib13 "")\], and warehouse automation \[ [4](https://arxiv.org/html/2502.03814v4#bib.bib4 ""), [125](https://arxiv.org/html/2502.03814v4#bib.bib125 "")\], where the task’s scale or complexity exceeds a single robot’s capabilities. When all robots in the team are identical and share the same functionality, the team is called a homogeneous multi-robot team. In contrast, a heterogeneous multi-robot team consists of different types of robots \[ [92](https://arxiv.org/html/2502.03814v4#bib.bib92 ""), [102](https://arxiv.org/html/2502.03814v4#bib.bib102 ""), [13](https://arxiv.org/html/2502.03814v4#bib.bib13 "")\].
The advantages of MRS include enhanced scalability, as tasks can be distributed among robots \[ [72](https://arxiv.org/html/2502.03814v4#bib.bib72 ""), [143](https://arxiv.org/html/2502.03814v4#bib.bib143 ""), [16](https://arxiv.org/html/2502.03814v4#bib.bib16 "")\], and increased resilience, as the failure of one robot can often be mitigated by the others \[ [149](https://arxiv.org/html/2502.03814v4#bib.bib149 ""), [145](https://arxiv.org/html/2502.03814v4#bib.bib145 ""), [97](https://arxiv.org/html/2502.03814v4#bib.bib97 ""), [73](https://arxiv.org/html/2502.03814v4#bib.bib73 ""), [85](https://arxiv.org/html/2502.03814v4#bib.bib85 ""), [148](https://arxiv.org/html/2502.03814v4#bib.bib148 ""), [150](https://arxiv.org/html/2502.03814v4#bib.bib150 ""), [142](https://arxiv.org/html/2502.03814v4#bib.bib142 ""), [106](https://arxiv.org/html/2502.03814v4#bib.bib106 ""), [62](https://arxiv.org/html/2502.03814v4#bib.bib62 ""), [60](https://arxiv.org/html/2502.03814v4#bib.bib60 "")\]. In contrast to designing a single, highly versatile robot, MRS usually relies on more uncomplicated, task-specific robots, reducing the cost and complexity of individual units while benefiting from collective intelligence \[ [49](https://arxiv.org/html/2502.03814v4#bib.bib49 "")\]. However, these systems also present unique challenges, particularly in communication, coordination, and decision-making, as robots must operate cohesively in dynamic and uncertain environments \[ [95](https://arxiv.org/html/2502.03814v4#bib.bib95 "")\].
Two primary control paradigms are commonly employed to manage the interaction and task distribution within an MRS: centralized and decentralized controllers \[ [130](https://arxiv.org/html/2502.03814v4#bib.bib130 ""), [20](https://arxiv.org/html/2502.03814v4#bib.bib20 "")\]. In a centralized controller, a single controller receives all the information and directs the actions of all robots in the system, allowing for optimized coordination and global planning. However, centralized systems can become a bottleneck when the group size increases and are vulnerable to single points of failure \[ [77](https://arxiv.org/html/2502.03814v4#bib.bib77 "")\]. On the other hand, a decentralized controller distributes decision-making among the roots, enabling the robots to operate resiliently \[ [98](https://arxiv.org/html/2502.03814v4#bib.bib98 "")\]. This approach enhances scalability and resilience but often introduces additional complexity to ensure seamless communication and coordination between robots. The choice between centralized and decentralized control depends on the specific application requirements, environmental conditions, and the desired balance between efficiency and robustness \[ [130](https://arxiv.org/html/2502.03814v4#bib.bib130 "")\].

### 2.2 Large Language Models

LLMs are deep learning models with millions to billions of parameters \[ [137](https://arxiv.org/html/2502.03814v4#bib.bib137 "")\]. Initially, the application of the LLMs is for text completion based on the context or text generation from the user’s instruction \[ [139](https://arxiv.org/html/2502.03814v4#bib.bib139 "")\]. LLMs are trained using an extensive collection of text from books, articles, websites, and other written sources. During this training process, LLMs learn to predict the next word in a sentence or fill in missing information using the attention mechanism \[ [112](https://arxiv.org/html/2502.03814v4#bib.bib112 "")\]. This pre-training phase enables LLMs to develop a broad understanding of language, grammar, factual knowledge, and reasoning skills \[ [89](https://arxiv.org/html/2502.03814v4#bib.bib89 "")\].

#### 2.2.1 Fine-tuning and RAG

While LLMs are pre-trained on a diverse dataset for general tasks, the performance in specialized cases can be unideal since the training dataset might not fully cover the special usages \[ [22](https://arxiv.org/html/2502.03814v4#bib.bib22 ""), [152](https://arxiv.org/html/2502.03814v4#bib.bib152 "")\]. People can prepare a dataset dedicated to the specialized tasks and retrain the model. However, retraining the entire model is often challenging due to the limited computing resources and numerous parameters within the model \[ [22](https://arxiv.org/html/2502.03814v4#bib.bib22 "")\]. One solution to address this issue is to use techniques like low-rank adaptation (LoRA) to fine-tune the LLMs with limited computational resources \[ [39](https://arxiv.org/html/2502.03814v4#bib.bib39 "")\]. LoRA freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture \[ [112](https://arxiv.org/html/2502.03814v4#bib.bib112 "")\], significantly reducing the number of trainable parameters for the downstream tasks.

On the other hand, retrieval-augmented generation (RAG) is an alternative technique that integrates external knowledge sources to increase the zero-shot accuracy of the LLMs on specialized tasks \[ [58](https://arxiv.org/html/2502.03814v4#bib.bib58 ""), [40](https://arxiv.org/html/2502.03814v4#bib.bib40 "")\]. RAG addresses a key limitation of LLMs’ reliance on pre-trained, static knowledge, which may not include domain-specific or up-to-date information. By combining a retrieval mechanism with the generative capabilities of LLMs, RAG allows the model to query external databases or knowledge repositories to retrieve relevant information during runtime \[ [28](https://arxiv.org/html/2502.03814v4#bib.bib28 "")\]. This retrieved data is then used to guide the model’s response, enhancing its accuracy and applicability in specialized contexts. For instance, RAG can provide real-time access to task-specific knowledge or environmental updates for robots, enabling better decision-making in dynamic scenarios \[ [151](https://arxiv.org/html/2502.03814v4#bib.bib151 "")\]. Although RAG introduces additional complexity, such as managing retrieval latency and ensuring data relevance, it offers a powerful method for bridging the gap between static pre-trained knowledge and the dynamic requirements of real-world applications.

#### 2.2.2 Multimodal LLMs

Traditional LLMs process only text, limiting their ability to directly interpret sensory data. In multi-robot systems, however, perception is often the primary source of situational awareness, coming from heterogeneous sensors such as onboard cameras, LiDAR, or aerial imagery. Multimodal LLMs address this gap by integrating inputs such as images, video, audio, or structured sensor data into a shared semantic space alongside language \[ [132](https://arxiv.org/html/2502.03814v4#bib.bib132 "")\]. This allows robots to ground natural language reasoning in real-world observations—for example, identifying mission-relevant objects, understanding spatial relationships, or updating plans based on live visual feedback \[ [53](https://arxiv.org/html/2502.03814v4#bib.bib53 ""), [117](https://arxiv.org/html/2502.03814v4#bib.bib117 "")\].

Recent advances have led to the emergence of Vision-Language Models (VLMs), which couple perception and reasoning, and Vision-Language-Action Models (VLAs), which go further by linking perception and reasoning directly to executable actions. These models extend the role of LLMs in MRS from purely symbolic reasoning to perception-grounded decision-making and, in the case of VLAs, to closed-loop perception–action execution \[ [141](https://arxiv.org/html/2502.03814v4#bib.bib141 "")\]. As discussed in Sec. [6.1](https://arxiv.org/html/2502.03814v4#S6.SS1 "6.1 LLMs, VLMs, and VLAs ‣ 6 LLMs, Simulations, and Benchmarks ‣ Large Language Models for Multi-Robot Systems: A Survey"), this evolution opens new possibilities for coordinated, perception-driven, and time-critical decision-making in multi-robot teams.

### 2.3 Related Survey Papers

Several survey papers have applied LLMs in the robotics and multi-agent field.
Firoozi et al.\[ [25](https://arxiv.org/html/2502.03814v4#bib.bib25 "")\], Zeng et al.\[ [137](https://arxiv.org/html/2502.03814v4#bib.bib137 "")\], and Kim et al.\[ [53](https://arxiv.org/html/2502.03814v4#bib.bib53 "")\] all explored how LLMs and foundation models could enhance robotics in areas like perception, decision-making, and control. While they share this focus, their approaches and scopes differ. Firoozi et al.\[ [25](https://arxiv.org/html/2502.03814v4#bib.bib25 "")\] provided a broad overview of foundation models in robotics, emphasizing their adaptability across various tasks but without specific attention to MRS. Zeng et al.\[ [137](https://arxiv.org/html/2502.03814v4#bib.bib137 "")\] focused on the applications of LLMs in robotics, categorizing their impact on single-robot systems in areas like control and interaction without exploring collaborative systems. Wang et al.\[ [117](https://arxiv.org/html/2502.03814v4#bib.bib117 "")\] concentrated on summarizing the applications of LLMs for manipulation tasks for a single robot. Kim et al.\[ [53](https://arxiv.org/html/2502.03814v4#bib.bib53 "")\] divided LLM applications into communication, perception, planning, and control, offering practical guidelines for integration, but their work is also centered on single-robot applications. Hunt et al.\[ [44](https://arxiv.org/html/2502.03814v4#bib.bib44 "")\] explored the use of language-based communication in robotics, categorizing applications of LLMs based on their roles in robotic systems, such as tasking robots, inter-robot communication, and human-robot interaction. Their focus is primarily on language as a medium for interaction without addressing the unique challenges of MRS. Guo et al.\[ [35](https://arxiv.org/html/2502.03814v4#bib.bib35 "")\] reviewed LLM-based multi-agent systems, exploring their applications in problem-solving and world simulation. Although their work included embodied agents, their emphasis is on general multi-agent frameworks, which focus on abstract roles and interactions within systems that may not require physical embodiment or real-world interaction. Kawaharazuka et al.\[ [51](https://arxiv.org/html/2502.03814v4#bib.bib51 "")\] examined real-world applications of foundation models in robotics, focusing on replacing components within robotic systems but without addressing inter-robot collaboration or the collective intelligence of MRS.

None of these surveys addresses the challenges and opportunities of integrating LLMs into MRS. While multi-agent systems provide a generalized framework for understanding roles and interactions, they are often abstract and virtual, lacking the physical embodiment and real-world constraints that characterize MRS \[ [35](https://arxiv.org/html/2502.03814v4#bib.bib35 "")\]. MRS requires actual physical robots to collectively perceive, decide, and act within dynamic and uncertain environments, posing unique challenges in communication, coordination, and decision-making that go beyond the scope of virtual agents \[ [114](https://arxiv.org/html/2502.03814v4#bib.bib114 "")\]. Moreover, MRS uniquely benefits from improved scalability, failure resilience, and cost-effective collective operations, making them fundamentally different from single-robot systems or general multi-agent frameworks. This gap highlights the need for a dedicated survey that explores how LLMs can facilitate communication, coordination, and collaborative task execution in MRS, providing critical insights into this emerging and impactful area of research.

## 3 Communication Types for LLMs in Multi-robot Systems

LLMs demonstrate remarkable abilities in understanding and reasoning over complex information. However, their performance can significantly vary depending on the communication architecture employed \[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 ""), [76](https://arxiv.org/html/2502.03814v4#bib.bib76 "")\]. This variability becomes particularly pronounced in scenarios involving embodied agents, where each agent operates with its own LLM for autonomous decision-making. The independence of these LLMs introduces unique challenges in maintaining consistency, coordination, and efficiency across the MRS. Understanding these dynamics is critical to optimizing LLM-based communication and decision-making frameworks in MRS.

https://arxiv.org/html/2502.03814v4/x1.pngFigure 2: The BOLAA architecture, which employs a controller to orchestrate multiple LAAs \[ [76](https://arxiv.org/html/2502.03814v4#bib.bib76 "")\].

Liu et al.\[ [76](https://arxiv.org/html/2502.03814v4#bib.bib76 "")\] provided a comprehensive comparison of LLM-augmented Autonomous Agents (LAAs), analyzing the architectures employed to integrate LLMs into agents. While their work primarily focuses on multi-agent systems rather than exclusively MRS, their insights into LLM architectures and agent orchestration offer valuable inspiration for multi-robot applications. Their study begins with a basic structure where LLMs perform zero-shot inference based solely on task instructions and observations. This architecture is then enhanced with a self-thinking loop, incorporating previous actions and observations into subsequent decision-making rounds to improve contextual consistency. They extended the architecture by incorporating few-shot prompts, including example actions to enhance the LLMs’ ability to generate effective decisions.
Regarding multi-agent orchestration, Liu et al. proposed a centralized architecture featuring a message distributor, which relays information to individual agents equipped with their own LLMs. These agents independently process the distributed messages to generate actions, as illustrated in Fig. [2](https://arxiv.org/html/2502.03814v4#S3.F2 "Figure 2 ‣ 3 Communication Types for LLMs in Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"). As discussed in Sec. [4](https://arxiv.org/html/2502.03814v4#S4 "4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"), several studies have adopted similar self-thinking strategies to improve the consistency and reliability of decisions made by LLMs, demonstrating the utility of this approach in collaborative systems.

Additionally, Chen et al.\[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 "")\] proposed four communication architectures: a fully decentralized framework (DMAS), a fully centralized framework (CMAS), and two hybrid frameworks that combine the decentralized and centralized frameworks (HMAS-1 and HMAS-2). These frameworks are visually represented in Fig. [3](https://arxiv.org/html/2502.03814v4#S3.F3 "Figure 3 ‣ 3 Communication Types for LLMs in Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"). Their study evaluated the performance of these structures in warehouse-related tasks, revealing notable distinctions among them. For scenarios involving six or fewer agents, both CMAS and HMAS-2 demonstrated comparable performance, although CMAS required more steps to complete tasks. In contrast, the performance of DMAS and HMAS-1 was notably inferior. Furthermore, their experiments indicated that HMAS-2 outperformed CMAS in handling more complex tasks, suggesting that hybrid frameworks with optimized structures offer greater scalability and adaptability for intricate multi-robot operations.

https://arxiv.org/html/2502.03814v4/figures/chen_scalable_2024_Systems.pngFigure 3: Four LLM-based multi-agent communication architectures introduced in Chen et al.\[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 "")\]. The circles represent robots that may have actions in the current step and the ‘LLM’ text represents each LLM agent. The overlap between one circle and one ‘LLM’ text means that the robot is delegated with one LLM agent to express its special opinions to other agents. The ‘LLM’ text without the overlapped circle represents a central planning agent.

## 4 LLMs for Multi-robot Systems

In this section, we categorize the applications of LLMs in MRS into high-level task allocation, mid-level motion planning, low-level action generation, and human intervention scenarios. High-level task planning involves tasks that demand a higher degree of intelligence, such as task allocation and planning among multiple robots, where the LLM is required to exhibit logical reasoning and decision-making capabilities. Mid-level motion planning refers to navigation or path-planning scenarios. Low-level action generation uses LLMs to generate and directly control robots’ posture or motion. On the other hand, human intervention involves using LLMs to interact with human operators and guide task planning and execution. Table [1](https://arxiv.org/html/2502.03814v4#S4.T1 "Table 1 ‣ 4.4 Human Intervention ‣ 4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey") shows the list of papers based on those four categories.

### 4.1 High-Level Task Allocation and Planning

High-level task planning leverages LLMs’ advanced reasoning and decision-making capabilities to handle complex and strategic tasks. This scenario often requires allocating tasks among robot teams, developing comprehensive task plans, or solving problems requiring contextual understanding and logic. Here, we explore studies illustrating LLMs’ capability in these sophisticated domains.

Recent work has demonstrated that LLMs are capable of allocating tasks among multiple robots. Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\] proposed a hierarchical LLMs framework consisting of two layers to solve the multi-robot multi-target tracking problem. In this scenario, the LLMs assign targets to each robot for tracking based on the current relative positions, velocities, and other relevant information between the robots and targets. As shown in Fig. [4](https://arxiv.org/html/2502.03814v4#S4.F4 "Figure 4 ‣ 4.1 High-Level Task Allocation and Planning ‣ 4 LLMs for Multi-Robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"), the outer task LLM receives human instruction and the long horizon information as inputs to provide strategic guidance and reconfiguration to the robot team. Meanwhile, the inner action LLM takes short horizon information as input and outputs control parameters for the controller. The outputs of the two LLMs are transformed into executable actions through the optimization solver.

https://arxiv.org/html/2502.03814v4/figures/llm.pngFigure 4: The target tracking architecture proposed by Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\]. The optimization solver acts as the controller for the multi-robot team. The “Task LLM” is a high-level task planner, while the “Action LLM” is a mid-level motion planner integrated with the optimization solver.

In addition, Brienza et al.\[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 "")\] applied VLM and LLM to generate actionable plans for the robotic soccer team. Their approach involved providing the VLM coach with a training set comprising video frames paired with corresponding textual prompts, detailing tasks and constraints. The VLM coach generated schematic descriptions of the video frames along with high-level natural language plans. Two distinct LLMs further refined and synchronized these high-level plans to produce executable strategies suitable for various scenarios. In practical applications, the system selected pre-collected plans based on their similarity to the real-world situation. Additionally, RAG minimizes prompt size and mitigates hallucination, ensuring more reliable outputs.
Moreover, Lykov et al.\[ [79](https://arxiv.org/html/2502.03814v4#bib.bib79 "")\] developed an MRS to collect and sort colored object sets and count spherical objects. Their approach utilized a fine-tuned LLM to generate Behavior Trees (BTs) for robots to execute tasks and provide feedback to human operators regarding their behaviors. They implemented a single LLM with two LoRA adapters, each handling specific functionalities to enhance efficiency and resource compactness.
In addition, Ahn et al.\[ [2](https://arxiv.org/html/2502.03814v4#bib.bib2 "")\] introduced an MRS framework featuring a recovery mechanism. The LLM controller received natural language instructions and a library of low-level robot skills to generate plans for task execution. A key innovation in their system was detecting deviations from the expected task progression and performing error recovery by replanning or seeking assistance from other robots or human operators.
Li and Zhou \[ [64](https://arxiv.org/html/2502.03814v4#bib.bib64 "")\] propose LLM-Flock, an approach that integrates decentralized LLM-driven planning with an influence-based consensus protocol for multi-robot formation control. This method mitigates inconsistent plan and behavior by refining local plans iteratively based on the influence of neighbors, achieving stable and adaptable flocking. Validated through simulations and drone experiments, their approach significantly enhances the coherence of multi-robot formations.
The remaining studies in this domain can be further categorized into two key areas: multi-robot multi-task coordination and complex task decomposition, highlighting the breadth of LLM applications in MRS.

#### 4.1.1 Multi-Robot Multi-Task Planning

In the multi-robot multi-task scenarios, a team of robots is tasked with completing multiple objectives simultaneously. LLMs play a critical role in devising actionable and efficient task distribution strategies in such settings. By interpreting high-level instructions and understanding the context of each task, LLMs can dynamically allocate tasks among robots, ensuring optimal utilization of resources and effective collaboration. This capability enables multi-robot teams to handle complex, multi-faceted operations with increased precision and adaptability.

Lakhnati et al.\[ [56](https://arxiv.org/html/2502.03814v4#bib.bib56 "")\] proposed a framework where three heterogeneous robots aim to accomplish complex tasks instructed by human operators in VR simulation. First, each robot LLM is given an initial prompt to clarify its role and abilities. A central controller LLM analyzes human descriptions of the task and distributes them to the respective robots. Instructions from human operators can either directly specify what each robot should do (e.g., “Jupiter needs to move to the dumbbell and pick it up, Neptune and Pluto have to move to the fridge.”) or describe the tasks without assigning to specific robots (e.g., “Three dinner plates have to be put into the trash, and all agents need to end up next to the garbage bin.”).
Following this line, Chen et al.\[ [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\] proposed a centralized framework where an LLM controller distributes the human instructions to a multi-robot team. They aim to make a heterogeneous multi-robot team accomplish multiple heterogeneous household tasks. However, the task distribution process they introduced is in the form of a discussion between the “Central Planner” LLM and the robot-dedicated agent LLM on each robot. The original task information is a geometric representation from a SLAM system. It is constructed into a scene context to prompt LLM. The “Central Planner” LLM first assigns each task to each robot according to its analysis. Then, each robot-dedicated agent LLM provides feedback according to the assigned task, and its robot resume is generated from the robot’s URDF code by the robot-dedicated agent LLM. If the task does not match the robot’s resume, it prompts the “Central Planner” for a reassignment. This discussion between LLMs continues until no reassignments are required.
Lim et al.\[ [69](https://arxiv.org/html/2502.03814v4#bib.bib69 "")\] presented a centralized LLM-enabled control framework for dynamic task assignment in multi-robot manufacturing systems. The architecture consists of three main components. The Central Controller Agent (CCA) acts as a high-level decision-maker, leveraging LLM reasoning to reassign tasks when disruptions occur. The Robot Agents execute tasks using configuration-defined capabilities and report failures to the CCA. The Sensor Module provides real-time perceptual input to ensure context-aware decisions. When a robot failure is detected, the CCA formulates a structured prompt containing system constraints and objectives, and sends it to the LLM to generate a valid new configuration for an alternative robot. If the LLM-generated configuration violates task constraints, structured feedback is appended, and the process is repeated until success is achieved. This loop ensures that reassignment is both feasible and safe. Once a valid configuration is found, the task is reallocated, and execution resumes seamlessly.
Moreover, Jiang et al.\[ [48](https://arxiv.org/html/2502.03814v4#bib.bib48 "")\] introduced a decentralized swarm robotics framework that leverages LLMs to enable spontaneous inter-robot communication and coordination. Each robot maintains its own LLM session and utilizes natural language to discover peers, share information, and coordinate collaborative actions without predefined roles. The system demonstrates that LLM-driven communication can give rise to emergent social behaviors such as negotiation, assistance, and conflict resolution, pushing swarm robotics toward more human-like, adaptive coordination.
Chen et al.\[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 "")\] took a step further to investigate the scalability of an LLM-based heterogeneous multi-task planning system. The efficiency and accuracy of four different communication architectures are compared, as shown in Fig. [3](https://arxiv.org/html/2502.03814v4#S3.F3 "Figure 3 ‣ 3 Communication Types for LLMs in Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey") under four distinct environments, including BoxNet, warehouse, and BoxLift. The results demonstrate that the HMAS-2 structure achieves the highest success rate while CMAS is the most token-efficient.
On the other hand, Gupte et al.\[ [37](https://arxiv.org/html/2502.03814v4#bib.bib37 "")\] proposed an LLM-based framework to solve Initial Task Allocation for a multi-robot multi-human system. In this centralized framework, LLM first generates prescriptive rules for each user’s objective and then generates experiences based on those rules for each objective. After acquiring a practical knowledge of the rules generated, the LLM’s performance is evaluated by inferencing, where the user provides instructions, and the LLM allocates the task according to the rules and experiences. Two distinct RAG workflows are leveraged in the inferencing stage to use the acquired knowledge fully.
Moreover, Huang et al.\[ [41](https://arxiv.org/html/2502.03814v4#bib.bib41 "")\] tested the ability of LLMs to solve the multi-robot Traveling Salesman Problem (TSP). By providing appropriate prompts, the LLM plans the optimal paths for multiple robots and generates Python code to control their movements. The study set up three frameworks: single attempt, self-debugging, where the LLM checks whether the generated Python code can be executed, and self-debugging with self-verification, where the LLM checks code executability and verifies whether the execution produces correct results. Their work reveals that LLMs perform poorly in handling such problems, with higher success rates that can only be observed in specific cases, such as the min-max multi-robot TSP.
Chen et al.\[ [14](https://arxiv.org/html/2502.03814v4#bib.bib14 "")\] presented a multi-agent LLM-based framework for robotic autonomy, integrating task analysis, robot design, and RL path planning. Experiments demonstrate the effectiveness of robot configuration generation and the feasibility of control strategies, showcasing significant improvements in the scalability and flexibility of LLM-driven robotic system development.
Wan et al.\[ [115](https://arxiv.org/html/2502.03814v4#bib.bib115 "")\] introduced a supervised fine-tuned LLM-based planning framework using the novel MultiPlan dataset for embodied multi-robot collaboration. Extensive indoor and outdoor field experiments illustrate significant improvements in task decomposition, robustness, and adaptability to novel environments compared to baseline LLM planners.

#### 4.1.2 Complex Task Decomposition

Task decomposition refers to scenarios where MRS must collaborate to complete one or more complex tasks that require careful planning and division of labor. In such cases, LLM can be leveraged to break down the overall task into smaller, manageable subtasks that align with the capabilities of each robot in the team. By designing effective prompts, LLMs can generate logical and actionable task decompositions, ensuring that the workload is distributed efficiently and that the robots cooperate seamlessly to achieve the overarching objective.

Kannan et al.\[ [50](https://arxiv.org/html/2502.03814v4#bib.bib50 "")\] introduced SMART-LLM, a framework that utilizes LLMs to decompose high-level human instruction into subtasks and allocate them to heterogeneous robots based on their predefined skill sets. Unlike Chen et al.\[ [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\], where robot capabilities are inferred from their URDF code using LLMs, SMART-LLM adopts a more conventional approach by explicitly defining each robot’s skill set for heterogeneous task allocation. The process involves decomposing instructions into sub-tasks, analyzing the required skills for each sub-task to form coalitions, and distributing robots accordingly to ensure efficient task execution.
Wang et al.\[ [120](https://arxiv.org/html/2502.03814v4#bib.bib120 "")\] propose Dependency-Aware Multi-Robot Task Decomposition and Execution LLMs (DART-LLM), a system designed to address complex task dependencies and parallel execution problems for MRS, as shown in Fig. [5](https://arxiv.org/html/2502.03814v4#S4.F5 "Figure 5 ‣ 4.1.2 Complex Task Decomposition ‣ 4.1 High-Level Task Allocation and Planning ‣ 4 LLMs for Multi-Robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"). The framework utilizes LLMs to parse high-level natural language instructions, decompose them into interconnected subtasks, and define their dependencies using a Directed Acyclic Graph (DAG). DART-LLM facilitates logical task allocation and coordination by establishing dependency-aware task sequences, enabling efficient collaboration among robots. Notably, the system demonstrates robustness even with smaller models, such as Llama 3.1 8B, while excelling in handling long-horizon and collaborative tasks. This capability enhances the intelligence and efficiency of MRS in managing complex composite problems.

https://arxiv.org/html/2502.03814v4/x2.pngFigure 5: The framework of DART-LLM proposed by Wang et al.\[ [120](https://arxiv.org/html/2502.03814v4#bib.bib120 "")\]. The system consists of three modules: Sensor Module, Intelligent Command Interface Module, and Actuation Module. The task decomposition process happens in the Intelligent Command Interface Module.

Xu et al.\[ [127](https://arxiv.org/html/2502.03814v4#bib.bib127 "")\] proposed a two-step framework that leverages LLMs to translate complex natural language instructions into a hierarchical linear temporal logic (LTL) representation for MRS. In the first step, the LLM decomposes the instruction into a hierarchical task tree, capturing logical and temporal dependencies between subtasks to avoid errors in sequence. In the second step, a fine-tuned LLM translates each subtask into flat LTL formulas, enabling precise execution using off-the-shelf planners. This framework emphasizes the importance of temporal reasoning in decomposing complex instructions, ensuring accurate task allocation and execution for long-horizon and interdependent multi-robot tasks.
In contrast to the abovementioned approaches, Obata et al.\[ [90](https://arxiv.org/html/2502.03814v4#bib.bib90 "")\] adopted a slightly different approach and proposed LiP-LLM, a framework integrating LLMs with linear programming for multi-robot task planning. Instead of providing end-to-end task allocation and execution, LiP-LLM utilizes LLMs to generate a skill set and a dependency graph that maps relationships and sequential constraints among tasks. The task allocation is then solved using linear programming to optimize task distribution among robots. This hybrid approach enhances task execution efficiency and success rates by combining LLMs’ interpretative capabilities with the precision of optimization techniques. The results demonstrate the potential of integrating LLMs with traditional optimization techniques to improve the performance and coordination of MRS.
On the other hand, Liu et al.\[ [74](https://arxiv.org/html/2502.03814v4#bib.bib74 "")\] proposed the COHERENT framework, which utilizes a Proposal-Execution-Feedback-Adjustment (PEFA) mechanism for task planning in heterogeneous MRS. The PEFA process involves a centralized task assigner LLM that decomposes high-level human instructions into subgoals and assigns them to individual robots. Each robot evaluates the assigned subgoal, determines its feasibility, and provides feedback to the task assigner, enabling dynamic adjustments and iterative refinements in the task plan. This process bears similarities to the robot discussion mechanism in the EMOS framework proposed by Chen et al.\[ [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\], where task decomposition and assignment leverage embodiment-aware reasoning based on robot resumes. However, COHERENT emphasizes a real-time, feedback-driven approach to handle task allocation and execution, making it particularly suited for dynamic and complex multi-robot environments.
Huang et al.\[ [42](https://arxiv.org/html/2502.03814v4#bib.bib42 "")\] proposed LAN2CB (Language to Collective Behavior), a framework that converts natural language mission descriptions into executable multi-robot code. The system performs mission parsing, dependency analysis, and behavior tree construction, then generates task code using a library of goal generation, allocation, and motion primitives. LAN2CB supports dynamic replanning by updating the behavior tree and regenerating code when triggers occur, enabling robust adaptation in changing environments. Experiments on nine diverse scenarios in both simulation and real-world tests demonstrated high success rates and resilience to complex dependencies and environmental events.

Liang et al.\[ [68](https://arxiv.org/html/2502.03814v4#bib.bib68 "")\] proposed a communication-based, feedback-driven framework that enhances multi-robot cooperation through a novel retrospective actor-critic paradigm. Their system comprises two large language models: LLM1\\text{LLM}\_{1}, which facilitates real-time collaborative discussion among robots to devise initial plans, and LLM2\\text{LLM}\_{2}, which serves as both an action critic and proposer. After executing a task or simulation, LLM2\\text{LLM}\_{2} conducts a retrospective evaluation based on environmental feedback, critiques the earlier plans, and proposes improved alternatives. The framework leverages short-term and long-term memory to retain only the most recent retrospectives, thus maintaining contextual relevance while minimizing computational overhead. This approach demonstrates improved performance on RoCoBench tasks compared to baselines, highlighting the value of integrating LLM-based reflection into the decision-making pipeline for dynamic and uncertain multi-robot environments. Differently, Mandi et al.\[ [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\] proposed RoCo, a decentralized communication architecture for multi-robot collaboration, focusing on both high-level task planning and low-level motion planning. In the RoCo framework, each robot is equipped with an LLM that engages in dialogue with other robots to discuss and refine task strategies. This dialogue process results in a proposed sub-task plan, which is validated by the environment for feasibility. If the plan fails (e.g., due to collisions or invalid configurations), feedback is incorporated into subsequent dialogues to improve the plan iteratively. Once validated, the sub-task plan generates goal configurations for robot arms, with a centralized motion planner computing collision-free trajectories. RoCo emphasizes flexibility and adaptability in multi-robot collaboration and has been evaluated using the RoCoBench benchmark, demonstrating robust performance across diverse task scenarios. This approach highlights the synergy between decentralized LLM-driven reasoning and centralized motion planning for complex, dynamic environments.
Peng et al.\[ [93](https://arxiv.org/html/2502.03814v4#bib.bib93 "")\] introduced a knowledge-augmented automated MILP formulation framework for multi-robot task allocation and scheduling. Their approach leverages locally deployed LLMs, combined with a structured knowledge base, to extract spatiotemporal constraints from natural language and translate them into executable MILP code. The two-step pipeline first interprets fuzzy natural instructions into mathematical constraints and then generates optimized Gurobi-compatible code. Notably, the entire process is locally deployable, ensuring data privacy in sensitive industrial settings. Experimental results on aircraft skin manufacturing tasks demonstrate that the framework achieves high accuracy and efficiency in both model construction and code generation, highlighting the potential of integrating LLMs with symbolic optimization techniques for practical, privacy-sensitive MRS applications.
Cladera et al.\[ [19](https://arxiv.org/html/2502.03814v4#bib.bib19 "")\] demonstrated air-ground collaborative planning using LLM-based semantic reasoning and mapping for language-specified missions. Their decentralized system enables dynamic mission adaptation, as validated through extensive field experiments in both urban and rural settings, highlighting effective semantic-based collaboration and robust task execution.
Gupta et al.\[ [36](https://arxiv.org/html/2502.03814v4#bib.bib36 "")\] proposed a hierarchical tree-based mission planning approach that leverages LLMs for automated decomposition into manageable subtasks, explicitly tailored for heterogeneous robot teams. The proposed heuristic method efficiently schedules tasks, considering robot-specific constraints, and demonstrates flexibility and scalability across varied, complex missions.

### 4.2 Mid-Level Motion Planning

Mid-level motion planning in MRS encompasses tasks such as navigation and path planning, where the focus lies on enabling robots to traverse or coordinate within an environment efficiently. These scenarios are more direct and practical than high-level applications but critical for multi-robot teams’ seamless operation. LLMs contribute significantly to this domain by leveraging their contextual understanding and learned patterns to generate robust and adaptive solutions. By interpreting environmental data and dynamically adapting to changes, LLMs enable robots to collaboratively plan paths, avoid obstacles, and optimize movement within shared spaces. Integrating LLMs into mid-level motion planning enhances efficiency and resilience, making MRS more capable in dynamic and unpredictable environments.

Yu et al.\[ [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\] proposed Co-NavGPT framework to integrate LLMs as a global planner for multi-robot cooperative visual semantic navigation, as shown in Fig. [6](https://arxiv.org/html/2502.03814v4#S4.F6 "Figure 6 ‣ 4.2 Mid-Level Motion Planning ‣ 4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey"). Each robot captures RGB-D vision data, which is converted into semantic maps. These maps are merged and combined with the task instructions and robot states to construct prompts for the LLMs. The LLMs then assign unexplored frontiers to individual robots for efficient target exploration. By leveraging semantic representations, Co-NavGPT enhances the comprehension of the environment and guides collaborative exploration.

https://arxiv.org/html/2502.03814v4/x3.pngFigure 6: The framework of Co-NavGPT proposed by Yu et al.\[ [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\].

In this framework, the LLMs are limited to allocating unexplored frontiers to each robot for navigation, serving primarily as a task allocation mechanism.
Morad et al.\[ [88](https://arxiv.org/html/2502.03814v4#bib.bib88 "")\] took a step further and proposed a novel framework combining LLMs with offline reinforcement learning (RL) to address path-finding challenges in MRS. Their approach involves leveraging LLMs to translate natural language commands into latent embeddings, which are then encoded with agent observations to create state-task representations. Using offline RL, policies are trained on these representations to generate navigation strategies that understand and follow high-level natural language tasks. A key advantage of this framework is its ability to train policies entirely on real-world data without requiring simulators, ensuring direct applicability to physical robots. The integration of LLMs enhances the flexibility of task instruction interpretation, while RL facilitates the generation of low-latency and reactive control policies, enabling efficient multi-robot navigation.
Following this line, Godfrey et al.\[ [31](https://arxiv.org/html/2502.03814v4#bib.bib31 "")\] developed MARLIN (Multi-Agent Reinforcement Learning Guided by Language-Based Inter-Robot Negotiation), a framework combining LLMs with Multi-Agent Proximal Policy Optimization (MAPPO) to enhance training efficiency and transparency in multi-robot navigation tasks. In MARLIN, robots equipped with LLMs engage in natural language negotiations to collaboratively generate task plans, which are then used to guide policy training. This hybrid approach dynamically switches between LLM-guided planning and standard MAPPO-based reinforcement learning, leveraging the reasoning capabilities of LLMs to improve training speed and sample efficiency without sacrificing performance. Experimental results demonstrate MARLIN’s ability to achieve faster convergence and more consistent performance compared to conventional MARL approaches, with applications validated in both simulation and physical robot environments. This integration of negotiation-based planning highlights the potential of combining LLMs with MARL for scalable, explainable multi-robot coordination.
On the other hand, Garg et al.\[ [29](https://arxiv.org/html/2502.03814v4#bib.bib29 "")\] leveraged LLMs for deadlock resolution in connected multi-robot navigation systems. In obstacle-laden environments, such systems can experience deadlocks that low-level control policies cannot resolve. To address this, the LLM selects a leader robot and plans waypoints for it to reach the target. The system reconfigures into a leader-follower formation, with a GNN-based low-level controller guiding the leader along the waypoints.
Mahadevan et al.\[ [83](https://arxiv.org/html/2502.03814v4#bib.bib83 "")\] directly tackled the challenge of multi-robot deadlocks by introducing GameChat, a role-based language negotiation framework for collaborative decision-making. In this system, agents engage in natural language dialogues to dynamically assign roles—such as “leader” or “blocker”—which help resolve spatial conflicts, task interdependencies, and bottlenecks that typically lead to deadlocks. These roles emerge through decentralized negotiation, without requiring pre-defined hierarchies or centralized control. The framework demonstrates robust performance across a variety of collaborative tasks, including navigation and manipulation, in both simulation and real-world experiments. GameChat showcases how emergent role-based reasoning and interactive dialogue can effectively address deadlock resolution in complex multi-agent environments. Moreover, Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\] proposed a mid-level action LLM that uses short-horizon inputs, such as tracking errors and control costs, to generate parameters for an optimization-based robot controller, enabling it to follow planned waypoints effectively.
While the aforementioned research primarily employs centralized systems where LLMs handle planning for all robots, Wu et al.\[ [123](https://arxiv.org/html/2502.03814v4#bib.bib123 "")\] developed a decentralized multi-robot navigation system for household tasks. In this framework, each robot is equipped with an LLM to enable communication and collaboration. Robots dynamically recognize and approach target objects distributed across multiple rooms. Leadership is dynamically assigned through a communication-triggered mechanism, with the leader robot issuing orders based on the global information it gathers. This flexible and decentralized leadership strategy enhances adaptability and efficiency in collaborative navigation scenarios.
Shen et al.\[ [104](https://arxiv.org/html/2502.03814v4#bib.bib104 "")\] proposed a framework of decentralized semantic planning based on multimodal chain-of-thought reasoning. The MCoCoNav architecture consists of three modules and two auxiliary components. The Perception module evaluates the exploration value of the current scene using multimodal CoT reasoning; the Judgment module determines whether a robot should explore a new frontier or revisit a history node by analyzing the global semantic map; the Decision module selects the next long-term navigation goal based on predicted frontier scores or historical node scores. If the robots are stuck or trapped in place, the system resets their goal to a randomly sampled point on the global map to avoid deadlocks and ensure continued exploration.
Ji et al.\[ [46](https://arxiv.org/html/2502.03814v4#bib.bib46 "")\] proposed a reinforcement learning framework that groups LLM planners with collision and reachability constraints, ensuring physically valid multi-robot motion plans. Evaluations in two BoxNet environments demonstrate that constraint-aware small-scale LLMs significantly outperform larger ungrounded models in task success and generalization, highlighting the effectiveness of explicit constraint integration for reliable multi-robot planning.
Rajvanshi et al.\[ [96](https://arxiv.org/html/2502.03814v4#bib.bib96 "")\] introduced SayCoNav, a LLM-based decentralized adaptive planning approach. By dynamically updating collaboration strategies among heterogeneous robots, SayCoNav significantly improves multi-object search efficiency and adapts to changing robot conditions during mission execution, as validated through extensive simulation studies.
Wang et al.\[ [119](https://arxiv.org/html/2502.03814v4#bib.bib119 "")\] presented SAMALM, a decentralized multi-agent LLM actor-critic framework that ensures socially aware robot navigation. Utilizing parallel LLM actors and critics for verification and cooperative navigation, the system effectively balances local autonomy and global coordination, validated through diverse multi-robot navigation scenarios.

### 4.3 Low-Level Action Generation

Low-level action generation focuses on controlling robot motion or posture at the hardware level, translating high-level goals into precise control commands. These tasks are critical for ensuring smooth and efficient operations in dynamic environments. While LLMs offer contextual reasoning and adaptability, their performance in low-level tasks, which demand high precision and real-time responsiveness, is often limited compared to traditional control methods. Hybrid approaches, combining LLMs with optimization-based controllers or reinforcement learning, show promise in leveraging LLMs’ flexibility while maintaining the precision required for reliable robot actions.

https://arxiv.org/html/2502.03814v4/x4.png

https://arxiv.org/html/2502.03814v4/x5.png

https://arxiv.org/html/2502.03814v4/x6.png

Figure 7: Snapshots of five agents forming a circle \[ [61](https://arxiv.org/html/2502.03814v4#bib.bib61 "")\]. The desired distance between each agent is 5 units. The decision of Agent 4’s LLM is tracked.

Chen et al.\[ [17](https://arxiv.org/html/2502.03814v4#bib.bib17 "")\] leveraged LLMs to address the Multi-Agent Path Finding (MAPF) problem, where LLMs actively navigate robots by generating actions incrementally. Each step concludes with a high-level conflict checker to identify collisions with robots or obstacles. While effective in obstacle-free environments, LLMs face challenges in maze-like maps due to limited reasoning capabilities, restricted context length, and difficulty understanding obstacle locations. Besides path finding, most studies on using LLMs for action generation focus on the problem of formation control. For example, Venkatesh et al.\[ [113](https://arxiv.org/html/2502.03814v4#bib.bib113 "")\] proposed a centralized architecture where LLMs translate natural language instructions into robotic configurations, enabling swarms to form specific patterns. Despite their strengths as centralized controllers, Li et al.\[ [61](https://arxiv.org/html/2502.03814v4#bib.bib61 "")\] highlighted the limitations of LLMs in decentralized systems. In a decentralized setup, each robot operates with its own LLM to achieve a desired formation through coordination with other robots. However, LLMs still face challenges in this task. In a test scenario shown in Fig. [7](https://arxiv.org/html/2502.03814v4#S4.F7 "Figure 7 ‣ 4.3 Low-Level Action Generation ‣ 4 LLMs for Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey") where agents were tasked with forming a circle with a desired spacing of 5 units, the agent’s LLM misinterpreted the instruction, moving to the circle’s center instead of the perimeter. This misunderstanding caused the agent to perform consensus-based behavior rather than the intended flocking behavior, revealing the difficulties that LLMs face in this distributed coordination.

In the field of formation control and planning, Strobel et al.\[ [107](https://arxiv.org/html/2502.03814v4#bib.bib107 "")\] introduced LLM2Swarm, a system that integrates LLMs with robot swarms through two approaches: centralized controller synthesis and decentralized direct integration. In the centralized approach, LLMs are used to design and validate controllers prior to deployment, enabling efficient and adaptive behavior generation. In the decentralized approach, each robot has its own LLM instance, enabling localized reasoning, planning, and collaboration for enhanced flexibility in dynamic environments. The results highlight the potential of LLMs in swarm robotics, demonstrating their applicability to both centralized and decentralized control paradigms. Lykov et al.\[ [80](https://arxiv.org/html/2502.03814v4#bib.bib80 "")\] further showcased the potential of LLMs in swarm control with FlockGPT, a framework for orchestrating UAV flocks to achieve desired geometric formations. In this system, the LLM generates a signed distance function (SDF) to guide UAV movements relative to a target surface, while a dedicated control algorithm manages practical constraints such as collision avoidance. These studies underscore the versatility of LLMs in enhancing both centralized and decentralized swarm behaviors. Moreover, Xue et al.\[ [129](https://arxiv.org/html/2502.03814v4#bib.bib129 "")\] proposed a novel framework that leverages LLMs to achieve communication-efficient multi-robot formation control. The approach encodes formation goals, robot roles, and spatial arrangements into compact natural language instructions, which are then distributed to individual robots. These instructions are decoded into actionable local goals by each agent. The framework demonstrates that LLM-generated descriptions can maintain formation integrity while significantly lowering communication bandwidth. Following this line, Ji et al.\[ [47](https://arxiv.org/html/2502.03814v4#bib.bib47 "")\] proposed GenSwarm, an end-to-end framework that enables automatic code-policy generation and deployment for multi-robot systems. The system interprets natural language instructions to construct constraint-based skill graphs, then hierarchically generates executable code policies using LLM agents. These policies are automatically reviewed, tested in simulation, and deployed to real-world robots via scalable hardware and software infrastructure. By supporting zero-shot generalization and human/VLM-in-the-loop feedback, GenSwarm offers a highly adaptive and interpretable solution for dynamic multi-robot tasks. Moreover, it is worth mentioning that GenSwarm supports optional human intervention in the loop, allowing users to provide natural language feedback after observing execution outcomes. This feedback is interpreted by LLM agents to iteratively refine control policies, enabling intuitive human-in-the-loop policy optimization.

### 4.4 Human Intervention

In MRS, LLMs typically focus on executing tasks based on human-provided instructions, emphasizing the interpretation of instructions and autonomous task completion. Once the instructions are delivered, human involvement is often minimized. However, emerging research explores scenarios that require continuous interaction between LLMs and humans, emphasizing cooperation, decision-making, or external observation throughout task execution. These studies highlight the potential for dynamic human intervention to address unexpected challenges, refine task strategies, or ensure safety in critical applications. By enabling iterative human-robot collaboration, such approaches enhance the adaptability and reliability of LLM-driven MRS.
The simplest form of human-robot interaction is demonstrated by Lakhnati et al.\[ [56](https://arxiv.org/html/2502.03814v4#bib.bib56 "")\], where robots operate in a straightforward cycle: receiving a human command, executing the corresponding task, reporting the completion status, and awaiting the next instruction.
Building on this, Lykov et al.\[ [79](https://arxiv.org/html/2502.03814v4#bib.bib79 "")\] introduced the LLM-MARS framework, which enables humans to inquire about each robot’s current state and task progress at any time. In this system, both response generation and task execution are handled by a single LLM, enhanced with distinct LoRA adapters for efficiency.
Hunt et al.\[ [43](https://arxiv.org/html/2502.03814v4#bib.bib43 "")\] proposed a more interactive approach, requiring human approval before executing any plan generated through LLM-driven discussions. If the proposed plan is deemed unreasonable, the human supervisor can provide feedback, prompting the LLMs to refine their approach through further dialogue.
Ahn et al.\[ [2](https://arxiv.org/html/2502.03814v4#bib.bib2 "")\] introduced the VADER system, further enhancing human involvement. When a robot encounters a task-related issue, it posts a request for assistance on the Human-Robot Fleet Orchestration Service (HRFS), a shared platform accessible to both human operators and robotic agents. Any agent or human can respond to the request, and once the issue is resolved, the robot resumes its task.
Li et al.\[ [66](https://arxiv.org/html/2502.03814v4#bib.bib66 "")\] introduced HMCF, which integrates LLM-driven multi-robot coordination with human oversight. Their framework mitigates hallucination via human verification, significantly improving task success rates and providing robust zero-shot generalization capabilities in diverse robotic tasks.
These examples illustrate the varying degrees of human involvement in LLM-driven MRS, ranging from simple command execution to active collaboration and dynamic problem-solving.

| Work | Communication | MRS Type | Modality | Human <br>Intervention | Evaluation | Application | Model Type |
| High level Task Allocation and Task Planning |
| Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\] | Cent | Homo | T | | Sim(ROS,RViz), Real | Target Tracking | GPT-4o, GPT-3.5 Turbo |
| Brienza et al.\[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 "")\] | Cent | Homo | T, I | | Sim(SimRobot) | Game | V: GPT-4 Turbo, L: GPT-3.5 Turbo |
| Lykov et al.\[ [79](https://arxiv.org/html/2502.03814v4#bib.bib79 "")\] | Cent | Homo | T, A | ✓ | Real | General Purpose | Falcon |
| Ahn et al.\[ [2](https://arxiv.org/html/2502.03814v4#bib.bib2 "")\] | Dec | Hetero | T, I | ✓ | Real | General Purpose | V: CLIP, ViLD, PaLI, L: PaLM |
| Lakhnati et al.\[ [56](https://arxiv.org/html/2502.03814v4#bib.bib56 "")\] | Hier | Hetero | T, A | ✓ | Sim(VR) | General Purpose | GPT-4 |
| Chen et al.\[ [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\] | Hier | Hetero | T | | Sim | Household | GPT-4o |
| Lim et al.\[ [69](https://arxiv.org/html/2502.03814v4#bib.bib69 "")\] | Cent | Homo | T, I | | Real | Manufacturing | GPT-4o |
| Jiang et al.\[ [48](https://arxiv.org/html/2502.03814v4#bib.bib48 "")\] | Dec | Homo | T | | Sim | General Purpose | GPT-4o, Gemini-2.0-Flash, DeepSeek-V3 |
| Chen et al.\[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 "")\] | Hier | Hetero | T | | Sim(AI2THOR) | General Purpose | GPT-4, GPT-3.5 Turbo |
| Gupte et al.\[ [37](https://arxiv.org/html/2502.03814v4#bib.bib37 "")\] | Cent | Hetero | T | | Sim(GAMA) | General Purpose | - |
| Huang et al.\[ [41](https://arxiv.org/html/2502.03814v4#bib.bib41 "")\] | Cent | Homo | T | | Sim | General Purpose | GPT-4 Turbo |
| Kannan et al.\[ [50](https://arxiv.org/html/2502.03814v4#bib.bib50 "")\] | Cent | Homo | T | | Sim(AI2THOR), Real | Household | GPT-4, GPT-3.5, Llama2, Claude3 |
| Wang et al.\[ [120](https://arxiv.org/html/2502.03814v4#bib.bib120 "")\] | Cent | Hetero | T, I | | Sim | Construction | L: Llama-3.1, Claude 3.5, GPT-4o,GPT-3.5 Turbo, V: CLIP |
| Xu et al.\[ [127](https://arxiv.org/html/2502.03814v4#bib.bib127 "")\] | Cent | Homo | T | | Sim(AI2THOR+ALFRED), Real | Household | Minstral, GPT-4 |
| Obata et al.\[ [90](https://arxiv.org/html/2502.03814v4#bib.bib90 "")\] | Cent | Hetero | T | | Sim(ROS) | General Purpose | GPT |
| Liu et al.\[ [74](https://arxiv.org/html/2502.03814v4#bib.bib74 "")\] | Hier | Hetero | T | | Sim(BEHAVIOR-1K), Real | General Purpose | GPT-4 |
| Liang et al.\[ [68](https://arxiv.org/html/2502.03814v4#bib.bib68 "")\] | Cent | Homo | T | | Sim(RoCoBench) | General Purpose | Llama3.1, Nemotron LLM |
| Mandi et al.\[ [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\] | Dec | Homo | T | | Sim, Real | Household | GPT-4 |
| Peng et al.\[ [93](https://arxiv.org/html/2502.03814v4#bib.bib93 "")\] | Cent | Homo | T | | Sim | General Purpose | DeepSeek-R1-Distill-Qwen-32B, SFT-Qwen2.5-Coder-7B-Instruct |
| Yu et al.\[ [135](https://arxiv.org/html/2502.03814v4#bib.bib135 "")\] | Dec | Hetero | T | | Sim(PyBullet) | Household | GPT-3.5 Turbo, GPT-4o, Llama3.1 |
| Sueoka et al.\[ [108](https://arxiv.org/html/2502.03814v4#bib.bib108 "")\] | Dec | Hetero | T, I | | Real | Construction | V: GPT-4v, L: GPT-4 |
| Hunt et al.\[ [43](https://arxiv.org/html/2502.03814v4#bib.bib43 "")\] | Cent | Homo | T | ✓ | Real | General Purpose | GPT-4 |
| Yoshida et al.\[ [133](https://arxiv.org/html/2502.03814v4#bib.bib133 "")\] | Dec | Hetero | T, I | | - | General Purpose | - |
| Wang et al.\[ [118](https://arxiv.org/html/2502.03814v4#bib.bib118 "")\] | Cent | Hetero | T | ✓ | Sim(AI2THOR) | General Purpose | GPT-3.5, Llama-2, Llama-3 |
| Guzman-Merino et al.\[ [38](https://arxiv.org/html/2502.03814v4#bib.bib38 "")\] | Cent | Hetero | T | | - | General Purpose | GPT-4o |
| Cladera et al.\[ [19](https://arxiv.org/html/2502.03814v4#bib.bib19 "")\] | Dec | Hetero | T, I | | Sim, Real | Target Tracking | GPT-4o |
| Chen et al.\[ [14](https://arxiv.org/html/2502.03814v4#bib.bib14 "")\] | Cent | Homo | T | | Sim | Formation | GPT-4o, GPT, DeepSeek-R1 |
| Gupta et al.\[ [36](https://arxiv.org/html/2502.03814v4#bib.bib36 "")\] | Cent | Hetero | T | | Sim | Field | GPT-4, Gemini, Llama |
| Wan et al.\[ [115](https://arxiv.org/html/2502.03814v4#bib.bib115 "")\] | Cent | Hetero | T, I | | Sim, Real | Field | GPT-4, fine-tuned MultiPlan |
| Huang et al.\[ [42](https://arxiv.org/html/2502.03814v4#bib.bib42 "")\] | Cent | Homo | T | | Sim, Real | Formation | GPT-4.1 |
| Mid level Motion Planning |
| Yu et al.\[ [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\] | Cent | Homo | T | | Sim(HM3D) | Household | GPT-3.5 Turbo |
| Morad et al.\[ [88](https://arxiv.org/html/2502.03814v4#bib.bib88 "")\] | Dec | Homo | T | | Real | General Purpose | GTE-Based |
| Godfrey et al.\[ [31](https://arxiv.org/html/2502.03814v4#bib.bib31 "")\] | Cent | Homo | T | | Sim, Real | General Purpose | Llama-3.1 |
| Garg et al.\[ [29](https://arxiv.org/html/2502.03814v4#bib.bib29 "")\] | Cent | Homo | T, I | | Sim, Real | General Purpose | V: Claude-3 Sonnet/Opus, GPT-4 Turbo, GPT-4o, L: GPT-4, GPT-3.5, Claude-2, Claude-3 |
| Mahadevan et al.\[ [83](https://arxiv.org/html/2502.03814v4#bib.bib83 "")\] | Dec | Homo | T | | Sim | Game | GPT-4o-mini |
| Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\] | Cent | Homo | T | | Sim(ROS, RViz), Real | Target Tracking | GPT-4o, GPT-3.5 Turbo |
| Wu et al.\[ [123](https://arxiv.org/html/2502.03814v4#bib.bib123 "")\] | Dec | Homo | T | | Sim | Household | GPT-4o |
| Shen et al.\[ [104](https://arxiv.org/html/2502.03814v4#bib.bib104 "")\] | Dec | Homo | T, I | | Sim(HM3D, MP3D) | Target Tracking | GLM-4V-9B |
| Ji et al.\[ [46](https://arxiv.org/html/2502.03814v4#bib.bib46 "")\] | Dec | Homo | T | | Sim | Warehouse | GPT-3.5, GPT-4 |
| Li and Zhou \[ [64](https://arxiv.org/html/2502.03814v4#bib.bib64 "")\] | Dec | Homo | T | | Sim, Real | Formation | o3-mini, Llama3.2, Qwen-Max, DeepSeek-R1, Claude-3.5 Sonnet |
| Rajvanshi et al.\[ [96](https://arxiv.org/html/2502.03814v4#bib.bib96 "")\] | Dec | Hetero | T | | Sim | Household | GPT-4 |
| Wang et al.\[ [119](https://arxiv.org/html/2502.03814v4#bib.bib119 "")\] | Dec | Homo | T | | Sim | Household | GPT-4o |
| Low level Action Execution |
| Chen et al.\[ [17](https://arxiv.org/html/2502.03814v4#bib.bib17 "")\] | Cent | Homo | T | | Sim | General Purpose | GPT-4 |
| Venkatesh et al.\[ [113](https://arxiv.org/html/2502.03814v4#bib.bib113 "")\] | Cent | Homo | T, I | | Sim(Pygame), Real | General Purpose | GPT-4, Llama-2, Claude-3 Opus |
| Li et al.\[ [61](https://arxiv.org/html/2502.03814v4#bib.bib61 "")\] | Dec | Homo | T | | Sim | General Purpose | GPT-3.5 Turbo |
| Strobel et al.\[ [107](https://arxiv.org/html/2502.03814v4#bib.bib107 "")\] | Dec | Homo | T | | Sim(ARGoS), Real | General Purpose | GPT-3.5, GPT-4 |
| Lykov et al.\[ [80](https://arxiv.org/html/2502.03814v4#bib.bib80 "")\] | Cent | Homo | T | | Sim | Formation | GPT-4 |
| Xue et al.\[ [129](https://arxiv.org/html/2502.03814v4#bib.bib129 "")\] | Cent | Homo | T | | Sim | Formation | GPT-4 Turbo |
| Ji et al.\[ [47](https://arxiv.org/html/2502.03814v4#bib.bib47 "")\] | Cent | Homo | T, I | ✓ | Sim(ROS) | Formation | o1-mini, GPT-4o, MetaGPT, CaP |
| Li et al.\[ [66](https://arxiv.org/html/2502.03814v4#bib.bib66 "")\] | Dec | Hetero | T, I | ✓ | Sim | Field | GPT-4 |

Table 1: Comparison of LLM-based MRS. Abbreviations: Communication: Cent (Centralized), Dec (Decentralized), Hier (Hierarchical); System: Homo (Homogeneous), Hetero (Heterogeneous); Modal: T (Text), I (Image/Video), A (Audio); Evaluation: Sim (Simulation), Real (Real-world experiments); Model Type: V (VLM), L (LLM).

## 5 Application

The integration of LLMs into MRS has enabled advancements across a variety of application domains, each with unique challenges and opportunities. These applications leverage LLMs’ capabilities in understanding, planning, and coordinating tasks, offering solutions ranging from indoor to outdoor scenarios. The adaptability of LLMs has driven innovation in tasks requiring precise navigation, task allocation, and dynamic decision-making, demonstrating their potential to address both structured and unstructured environments.

In this section, we categorize studies based on their application scenarios, focusing on two primary domains. First, the household domain highlights MRS addressing indoor challenges such as navigation, task decomposition, and object manipulation. These systems often emphasize collaboration among heterogeneous robots to execute intricate tasks, from identifying targets in multi-room settings to organizing household appliances. Second, applications in construction, formation, target tracking, and game illustrate the versatility of LLMs in specialized fields. These studies showcase MRS solving complex problems in outdoor or competitive environments, such as drone formations for search-and-rescue missions, robotic soccer strategies, and navigation in hazardous areas. Together, these domains underscore the growing impact of LLMs in advancing MRS capabilities across diverse real-world contexts.

Household. The household domain represents a significant focus in studies with well-defined application scenarios, addressing challenges such as navigation, task allocation, and task decomposition. For example, Wu et al.\[ [123](https://arxiv.org/html/2502.03814v4#bib.bib123 "")\] and Yu et al.\[ [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\] investigated navigation and multi-target localization in complex indoor environments, such as identifying objects across multiple rooms, showcasing advancements in spatial awareness and adaptability. Furthermore, Mandi et al.\[ [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\], Yu et al.\[ [135](https://arxiv.org/html/2502.03814v4#bib.bib135 "")\], Kannan et al.\[ [50](https://arxiv.org/html/2502.03814v4#bib.bib50 "")\], and Xu et al.\[ [127](https://arxiv.org/html/2502.03814v4#bib.bib127 "")\] explored task decomposition and multi-robot collaboration to execute intricate tasks, such as preparing sandwiches or organizing dishwashers. Chen et al.\[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 "")\] emphasized task allocation for heterogeneous MRS in multi-floor indoor settings, tackling coordination challenges in dynamic environments. Notably, they proposed an EMOS framework, an embodiment-aware operating system that facilitates effective collaboration among heterogeneous robots through a novel “robot resume” approach, enabling robots to interpret their physical constraints from URDF files autonomously rather than relying on predefined roles. These studies address the temporal sequencing of subtasks while leveraging diverse robot capabilities, demonstrating the potential of MRS to solve complex, real-world problems in home environments.

Others Including Construction, Formation, Target Tracking, and Game.
Several studies focused on applications in open-world environments, highlighting the versatility and innovative potential of LLM-integrated robotic systems. For instance, Wang et al.\[ [120](https://arxiv.org/html/2502.03814v4#bib.bib120 "")\] and Sueoka et al.\[ [108](https://arxiv.org/html/2502.03814v4#bib.bib108 "")\] explored the use of LLMs in orchestrating robotic systems for excavation and transportation tasks, showcasing their applicability in construction and complex terrain rescue operations. In drone formations applications, Lykov et al.\[ [80](https://arxiv.org/html/2502.03814v4#bib.bib80 "")\] emphasized the coordination and adaptability needed for outdoor tasks such as search-and-rescue missions and environmental monitoring. Similarly, Wu et al.\[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\] addressed open-world target tracking by integrating danger zone recognition, providing robust solutions for autonomous navigation in hazardous environments. These scenarios further demonstrate the potential of LLMs in dynamic and structured environments. Brienza et al.\[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 "")\] introduced LLCoach, a framework for robotic soccer applications, where LLMs enhance strategic decision-making and team coordination. Collectively, these studies underscore the potential of LLM-driven MRS to tackle diverse and complex challenges across various domains.

## 6 LLMs, Simulations, and Benchmarks

### 6.1 LLMs, VLMs, and VLAs

#### 6.1.1 Extending LLM Capabilities

As discussed in Sec. [3](https://arxiv.org/html/2502.03814v4#S3 "3 Communication Types for LLMs in Multi-robot Systems ‣ Large Language Models for Multi-Robot Systems: A Survey")- [5](https://arxiv.org/html/2502.03814v4#S5 "5 Application ‣ Large Language Models for Multi-Robot Systems: A Survey"), LLMs form the backbone of many recent advances in MRS, enabling robots to follow natural language instructions, perform multi-step reasoning, allocate tasks, plan motions, and interact with human operators. Their strengths include flexible problem-solving across diverse scenarios, integration of symbolic or structured data, and the ability to generalize to new missions without retraining.

However, LLMs primarily operate on textual or symbolic representations of the environment. They rely on external perception modules to provide structured inputs such as maps, object lists, or state summaries. This separation between perception and reasoning can limit adaptability in visually complex or fast-changing environments where world states must be updated and integrated in real time.

To address these limitations, researchers have introduced multi-modal extensions, most notably VLMs and Vision-Language-Action models (VLAs) \[ [141](https://arxiv.org/html/2502.03814v4#bib.bib141 ""), [91](https://arxiv.org/html/2502.03814v4#bib.bib91 "")\]. VLMs incorporate visual information directly into the reasoning process, allowing robots to ground their decisions in raw sensory data \[ [52](https://arxiv.org/html/2502.03814v4#bib.bib52 ""), [11](https://arxiv.org/html/2502.03814v4#bib.bib11 "")\]. VLAs take this one step further by integrating perception, reasoning, and action generation into a single pipeline, enabling faster, more reactive responses in dynamic settings \[ [11](https://arxiv.org/html/2502.03814v4#bib.bib11 "")\].

#### 6.1.2 VLMs vs. Traditional CV

Traditional computer vision (CV) in MRS is typically task-specific, using separate modules for detection, segmentation, mapping, or action recognition. These components produce structured outputs that are passed to independent reasoning or control systems. While this modularity can yield strong performance for narrow tasks, it often lacks the flexibility and adaptability needed for unstructured or dynamic missions.

VLMs bridge this gap by embedding visual features into a shared semantic space with language, enabling unified perception and reasoning. This allows recognition of previously unseen objects without retraining, switching between perception tasks by altering prompts, and direct connection between sensory input and high-level reasoning without intermediate, hand-coded logic. In MRS, these capabilities have been leveraged for perception-informed coordination, such as in Brienza et al.\[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 "")\], where a VLM coach transformed soccer match video into schematic scene descriptions for strategic planning, and in the VADER framework \[ [2](https://arxiv.org/html/2502.03814v4#bib.bib2 "")\], where PaLI and CLIP grounded instructions in real-time affordance detection for replanning and recovery.

#### 6.1.3 VLA Models in MRS

VLAs extend VLMs by coupling perception and reasoning directly with action generation \[ [141](https://arxiv.org/html/2502.03814v4#bib.bib141 "")\]. Instead of outputting textual task plans, they can map visual observations and natural language commands to executable control sequences. This closed-loop capability shortens the cycle between sensing and actuation, allowing robots to respond faster to dynamic changes.

In an MRS setting, each VLA-equipped robot could combine the onboard camera feed, interpret the cooperative context, and directly issue motor commands for joint manipulation or navigation without routing through a separate planning layer. Although still relatively new in MRS research, VLAs are being explored in embodied AI for scenarios requiring fast perception–action loops, such as swarm coordination or hazard avoidance.

#### 6.1.4 Comparative Capabilities and Integration Patterns

From an MRS perspective, LLMs, VLMs, and VLAs have complementary strengths. LLMs excel at long-horizon reasoning, symbolic planning, and high-level negotiation between agents. VLMs add environmental grounding through perception, enabling multi-robot teams to share and reason about visual context. VLAs integrate perception and action for rapid, local decision-making.

Integration patterns in the literature generally follow three approaches: (1) visual grounding with language reasoning, where a vision encoder produces scene features that an LLM uses for planning and coordination \[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 ""), [29](https://arxiv.org/html/2502.03814v4#bib.bib29 "")\]; (2) direct multi-modal prompting, where visual and textual inputs are processed jointly for end-to-end reasoning \[ [29](https://arxiv.org/html/2502.03814v4#bib.bib29 ""), [108](https://arxiv.org/html/2502.03814v4#bib.bib108 "")\]; and (3) perception-to-action mapping, where VLA-style architectures produce executable actions directly from multi-modal inputs, bypassing explicit textual reasoning.

Hybrid systems can combine these strengths. For example, a central LLM might manage mission-level strategy, VLMs on individual robots could process onboard sensor data for situational awareness, and VLAs could execute low-latency control in fast-changing conditions.

### 6.2 Simulation Environments

We have summarized the simulation platforms used in related works, highlighting their contributions to evaluating and advancing the field.
AI2-THOR has been adapted for MRS in \[ [18](https://arxiv.org/html/2502.03814v4#bib.bib18 ""), [50](https://arxiv.org/html/2502.03814v4#bib.bib50 ""), [118](https://arxiv.org/html/2502.03814v4#bib.bib118 ""), [127](https://arxiv.org/html/2502.03814v4#bib.bib127 "")\] to evaluate embodied AI agents operating in complex indoor environments \[ [54](https://arxiv.org/html/2502.03814v4#bib.bib54 "")\]. While originally designed for single-agent tasks such as object manipulation and scene understanding, recent research extends its use to MRS scenarios, including cooperative object retrieval, shared perception, and collaborative planning in constrained environments. The physics-enabled interactions allow researchers to test LLM-driven coordination strategies in dynamic and physically grounded environments, where multiple agents must navigate, manipulate objects, and resolve conflicts dynamically.
PyBullet is an open-source physics engine widely used for simulating robotic systems, including articulated manipulators, wheeled robots, and multi-agent interactions \[ [21](https://arxiv.org/html/2502.03814v4#bib.bib21 "")\]. It provides real-time physics simulations, supporting tasks like collision detection, rigid body dynamics, and reinforcement learning in robotics. In the context of MRS, PyBullet enables accurate modeling of decentralized collaboration, object manipulation, and dynamic environment interactions \[ [135](https://arxiv.org/html/2502.03814v4#bib.bib135 "")\].
BEHAVIOR-1K, utilized by Liu et al.\[ [74](https://arxiv.org/html/2502.03814v4#bib.bib74 "")\], serves as the foundation for the COHERENT framework, which focuses on large-scale, heterogeneous multi-robot collaboration \[ [59](https://arxiv.org/html/2502.03814v4#bib.bib59 "")\]. This platform facilitates training and evaluation in complex household-like environments where different types of robots (e.g., manipulators, mobile bases) must coordinate to accomplish everyday tasks such as table setting, object handoff, and multi-step assembly processes. The benchmark ensures that LLM-enhanced systems can handle dynamic task dependencies and ambiguous role assignments.
The Pygame platform is a cross-platform Python module set designed for video game writing. Robots are modeled as point-mass entities, focusing on formation control, decentralized consensus algorithms, and motion coordination without obstacle avoidance. This platform is particularly useful for analyzing emergent behaviors in swarms, where LLM-based controllers guide self-organized formations through simple local interactions \[ [113](https://arxiv.org/html/2502.03814v4#bib.bib113 "")\].
Habitat-MAS, an extension of Habitat, introduces explicit multi-agent communication for indoor navigation and exploration \[ [100](https://arxiv.org/html/2502.03814v4#bib.bib100 ""), [109](https://arxiv.org/html/2502.03814v4#bib.bib109 ""), [94](https://arxiv.org/html/2502.03814v4#bib.bib94 "")\]. Unlike the single-agent focus of its predecessor, Habitat-MAS enables studies on cooperative search, simultaneous localization and mapping (SLAM), and inter-agent strategy adaptation, crucial for deploying multi-robot exploration teams in disaster response and service robotics \[ [15](https://arxiv.org/html/2502.03814v4#bib.bib15 "")\].
ROS-based simulation is a middleware framework widely used for MRS, enabling inter-robot communication \[ [57](https://arxiv.org/html/2502.03814v4#bib.bib57 "")\]
, decentralized control, and real-time data sharing. It provides essential tools for swarm coordination, collaborative mapping, and distributed task allocation. With built-in simulation environments like Gazebo and RViz, ROS allows researchers to develop and test MRS strategies for exploration, target tracking, and cooperative manipulation \[ [124](https://arxiv.org/html/2502.03814v4#bib.bib124 "")\].
VR platform introduces immersive simulations for human-robot collaboration and reinforcement learning. These environments are used to test human-in-the-loop control strategies for heterogeneous robot teams, such as coordinating robotic arms and mobile robots in warehouse logistics through natural language instructions \[ [56](https://arxiv.org/html/2502.03814v4#bib.bib56 "")\].
GAMA offers a multi-agent modeling environment suited for large-scale robot interactions \[ [37](https://arxiv.org/html/2502.03814v4#bib.bib37 "")\]. It supports evaluations of distributed swarm intelligence, multi-agent task negotiation, and behavior adaptation in unstructured environments, making it ideal for testing decentralized LLM-driven controllers in logistics and autonomous fleet management.
SimRobot, utilized by Brienza et al.\[ [10](https://arxiv.org/html/2502.03814v4#bib.bib10 "")\], is specialized for multi-robot teamwork in robotic soccer. The LLCoach framework, trained using SimRobot, enhances robot coordination and strategic planning by processing match data and optimizing multi-agent role assignments dynamically.
ARGoS, chosen by Strobel et al.\[ [107](https://arxiv.org/html/2502.03814v4#bib.bib107 "")\], is a scalable platform for swarm robotics research. It enables controlled experiments on decentralized control mechanisms, including aggregate-then-disperse behaviors, leader election, and emergent self-organization. LLMs integrated into ARGoS are evaluated on their ability to generate adaptive communication protocols and handle task partitioning in dynamic environments.
These diverse platforms provide essential tools for evaluating LLM-driven MRS across different scales, from small collaborative teams to large autonomous swarms. By leveraging these environments, researchers refine multi-agent coordination, communication, and decision-making strategies, advancing the integration of LLMs in MRSs for real-world applications.

### 6.3 Benchmarks

Benchmarks are essential for evaluating LLM-driven MRS, providing standardized environments to measure coordination, adaptability, and performance across diverse scenarios. They enable consistent comparisons, helping identify strengths, limitations, and the effectiveness of MRS in real-world applications.
RoCoBench, introduced by Mandi et al.\[ [84](https://arxiv.org/html/2502.03814v4#bib.bib84 "")\], focuses on human-robot collaboration in fine-grained manipulation tasks. While primarily designed for single-robot control, RoCoBench also provides insights into multi-robot collaboration, particularly in tasks requiring shared manipulation, coordinated actions, and real-time adjustments to changing conditions. The benchmark provides detailed metrics on precision, task success rates, and robustness under unpredictable physical conditions, making it valuable for evaluating LLM-assisted multi-robot cooperation in human-shared workspaces.
ALFRED, utilized in Xu et al.\[ [127](https://arxiv.org/html/2502.03814v4#bib.bib127 "")\], integrates language and vision benchmarks to test agents’ ability to follow natural language instructions and execute multi-step tasks in household environments. Though originally focused on single-agent evaluations, ALFRED’s framework can be extended to multi-robot task coordination, testing MRS on collaborative planning, sequential action execution, and efficient division of labor in domestic or service robotics applications.
BOLAA, proposed by Liu et al.\[ [76](https://arxiv.org/html/2502.03814v4#bib.bib76 "")\], introduces a multi-agent orchestration benchmark specifically designed for LLM-augmented autonomous agents (LAAs). Unlike conventional evaluations that focus on individual agents, BOLAA assesses how LLMs manage multi-agent interactions, optimizing task distribution, decision-making, and real-time adaptability. This makes it a useful benchmark for LLM-driven MRS, where autonomous robots benefit from effective communication and collaboration to tackle complex, long-horizon objectives.
COHERENT-Benchmark, developed by Liu et al.\[ [74](https://arxiv.org/html/2502.03814v4#bib.bib74 "")\], is specifically designed for heterogeneous multi-robot collaboration in dynamic and realistic scenarios. Built on the BEHAVIOR-1K platform, this benchmark evaluates MRS across diverse environments, requiring coordinated task execution among robots with distinct capabilities—such as quadrotors for aerial mapping, robotic dogs for agile mobility, and robotic arms for precise manipulation. Key evaluation metrics include task allocation efficiency, inter-robot communication, and collaborative problem-solving, making it a comprehensive benchmark for testing LLM-driven coordination strategies in MRS.

## 7 Challenges, and Opportunities

Despite the progress in integrating LLMs into MRS, significant challenges that limit their broader adoption and effectiveness remain. These challenges span areas such as reasoning capabilities, real-time performance, and adaptability to dynamic environments. Addressing these issues is critical to unlocking the full potential of LLMs in MRS. This section identifies key challenges the field faces and outlines promising opportunities for future research, offering a roadmap for enhancing the utility and robustness of LLM-driven MRS.

### 7.1 Challenges

Insufficient Mathematical Capability.
LLMs struggle with tasks requiring precise calculations or logical reasoning, such as multi-robot path planning or trajectory optimization. This limitation reduces their effectiveness in scenarios where quantitative accuracy is critical. Mirzadeh et al.\[ [87](https://arxiv.org/html/2502.03814v4#bib.bib87 "")\] performed a detailed comparison and investigation on the mathematical understanding and problem-solving ability of several state-of-the-art LLMs. Specifically, LLMs exhibit noticeable variance when responding to different variations of the same question, with performance declining significantly when only the numerical values are altered. Furthermore, their reasoning capabilities are fragile; they often mimic patterns observed in training data rather than performing genuine logical deduction. This fragility is exacerbated by an increase in the number of clauses within a question, even when the added clauses are irrelevant to the reasoning chain, leading to performance drops of up to 65% in state-of-the-art models. These vulnerabilities present serious challenges for MRS, where precise calculations and robust reasoning are essential for collision-free trajectories, spatial planning, and efficient task execution. Addressing these limitations is critical for deploying LLMs reliably in mathematically intensive applications.

Hallucination.
LLMs are prone to generating content that appears plausible but lacks factual accuracy, a phenomenon known as hallucination. This issue is particularly concerning in MRS, where precise and reliable output is crucial for effective collaboration and operation. According to a comprehensive survey on hallucination in LLMs by Huang et al.\[ [40](https://arxiv.org/html/2502.03814v4#bib.bib40 "")\], hallucination can be categorized into two main types: actuality hallucinations and faithfulness hallucinations. Factuality hallucinations involve discrepancies between generated content and verifiable real-world facts, leading to incorrect outputs. Faithful hallucinations occur when the generated content diverges from the user’s instructions or the provided context, resulting in outputs that do not accurately reflect the intended information. In the context of MRS, such hallucinations can lead to misinterpretations, faulty decision-making, and coordination errors among robots, potentially compromising mission success and safety. Addressing these challenges requires developing methods to detect and mitigate hallucinations, ensuring that LLMs produce outputs that are both factually accurate and contextually appropriate.

Difficulties in Field Deployment.
Current options for using LLMs include server-based models, which are usually closed-source, and open-source models that individuals can deploy locally. Examples of server-based models include OpenAI GPT \[ [1](https://arxiv.org/html/2502.03814v4#bib.bib1 "")\], Anthropic Claude \[ [7](https://arxiv.org/html/2502.03814v4#bib.bib7 "")\], and Google Gemini (formerly known as Bard) \[ [32](https://arxiv.org/html/2502.03814v4#bib.bib32 "")\], and open-sourced LLMs that individuals can run locally includes Meta Llama \[ [23](https://arxiv.org/html/2502.03814v4#bib.bib23 "")\], Falcon \[ [3](https://arxiv.org/html/2502.03814v4#bib.bib3 "")\], Alibaba Qwen \[ [131](https://arxiv.org/html/2502.03814v4#bib.bib131 "")\], and DeepSeek V3 \[ [70](https://arxiv.org/html/2502.03814v4#bib.bib70 "")\] and R1 \[ [34](https://arxiv.org/html/2502.03814v4#bib.bib34 "")\]. The server-based models require a reliable internet connection to send inquiries and receive responses, thus making deploying the MRS with LLMs in remote locations unachievable, which is typical for field robot systems. Moreover, server-based LLMs heavily rely on the performance of the server, where a server outage can interrupt the systems built on LLMs entirely. This issue is especially vital for multi-robot teams as the LLM guides the inter-robot collaboration and decision-making. On the other hand, local models can avoid using the servers but require hardware onboard that is powerful enough to run LLMs locally.

Relatively High Latency.
Real-time information exchange and decision-making are critical for the effective operation of MRS in real-world scenarios. However, a notable challenge of using LLMs lies in their relatively high and variable response times, which can depend on model complexity, hardware capabilities, and server availability. For example, Chen et al.\[ [17](https://arxiv.org/html/2502.03814v4#bib.bib17 "")\] reported that in a multi-agent path finding scenario utilizing GPT-4 from OpenAI, the response time per step ranged between 15 and 30 seconds, significantly impacting real-time feasibility. While local processing on more powerful hardware can reduce latency, this approach is costly and becomes less scalable as the number of robots increases. Addressing this challenge requires exploring optimized LLM architectures, efficient inference techniques, and scalable solutions that balance computational demands with real-time operational requirements.

Multi-modal Integration Difficulties.
While VLMs and VLAs extend the role of LLMs in MRS by grounding reasoning in perception and linking directly to action, they also introduce new challenges. Multi-modal inference often incurs higher latency due to the added cost of processing images, video, or sensor streams alongside text \[ [65](https://arxiv.org/html/2502.03814v4#bib.bib65 "")\]. Domain shift remains a significant issue, as models trained on internet-scale vision-language corpora may not generalize reliably to the specialized sensing modalities of robots (e.g., LiDAR, thermal cameras, aerial views) \[ [82](https://arxiv.org/html/2502.03814v4#bib.bib82 "")\]. Moreover, fusing heterogeneous and asynchronous sensor data across multiple robots introduces synchronization and consistency problems, especially in decentralized settings \[ [82](https://arxiv.org/html/2502.03814v4#bib.bib82 "")\]. VLAs face the additional challenge of grounding action outputs across diverse robot morphologies, making it difficult to generalize learned behaviors across heterogeneous teams. Addressing these multi-modal integration difficulties is critical for ensuring that perception-grounded LLMs can operate robustly in real-world MRS deployments.

Lack of Benchmarks.
Performance evaluation is essential for the new research on MRS with LLMs. However, existing benchmarking systems are primarily designed for indoor environments and household applications, which limits their applicability to the diverse and evolving scenarios where MRS operates. As current research often represents initial efforts to apply LLMs to MRS, performance comparisons typically focus on demonstrating feasibility by contrasting LLMs with traditional methods. While this approach is valuable for establishing a baseline, future advancements will likely yield significant performance and functionality improvements. A unified benchmarking framework tailored to multi-robot applications would provide researchers with consistent metrics to evaluate and quantify progress. Such a system would not only facilitate a clearer understanding of the impact of new research but also promote standardization and comparability across studies, accelerating innovation in this emerging field.

### 7.2 Opportunities

Fine-tuning and RAG.
Fine-tuning LLMs on domain-specific datasets and incorporating RAG techniques are promising avenues for improving their performance in multi-robot applications. Fine-tuning allows researchers to adapt pre-trained LLMs to specific tasks, enhancing their contextual understanding and reducing issues like hallucination. RAG complements this by integrating external knowledge retrieval mechanisms, enabling LLMs to access relevant information dynamically during runtime. Together, these techniques can significantly improve LLMs’ accuracy, reliability, and adaptability in diverse and complex multi-robot scenarios.

High-quality Task-specific Datasets.
Creating high-quality and task-specific datasets is essential for advancing LLM capabilities in MRS. Leveraging more capable models, such as the latest LLMs, to generate synthetic datasets can accelerate the development of training materials tailored to specific tasks or environments. These datasets should include diverse scenarios, reasoning-focused labels, and context-specific knowledge to improve LLMs’ problem-solving and decision-making capabilities. Task-specific datasets are particularly important for preparing MRS to operate in unstructured or open-world environments.

Advanced Reasoning Techniques.
Improving the reasoning capabilities of LLMs is critical for addressing their current limitations in logical and mathematical tasks. Techniques such as Chain of Thought (CoT) prompting \[ [122](https://arxiv.org/html/2502.03814v4#bib.bib122 "")\], fine-tuning with explicit reasoning labels \[ [138](https://arxiv.org/html/2502.03814v4#bib.bib138 "")\], integrating symbolic reasoning, and training with RL can enhance the ability of LLMs to handle complex multi-step problems. By advancing reasoning methods, LLMs can better support tasks that require precision and logical deduction, such as multi-robot path planning and coordination.

Task-specific and Lightweight Models.
While large-scale LLMs offer superior performance, they are often impractical for resource-constrained environments. Developing task-specific and lightweight models tailored for multi-robot applications can mitigate this issue \[ [9](https://arxiv.org/html/2502.03814v4#bib.bib9 "")\]. Models like SmolVLM, Moondream 2B, PaliGemma-2 3B, and Qwen2-VL 2B demonstrate how smaller architectures can reduce computational demands and latency while maintaining adequate performance for specific tasks. Model distillation is another approach to make small models more capable by distilling knowledge from a more capable LLM, like DeepSeek-R1-Distill-Qwen-1.5B, where the knowledge from DeepSeek R1 is distilled into a small Qwen2.5-Math-1.5B model \[ [128](https://arxiv.org/html/2502.03814v4#bib.bib128 "")\]. Balancing efficiency and effectiveness is key to enabling scalable deployments of LLMs in field robotics.

Multi-modal and Embodied Extensions.
Emerging research on multi-modal LLMs suggests promising opportunities for extending MRS capabilities. Video-language transformers, point cloud-language models \[ [26](https://arxiv.org/html/2502.03814v4#bib.bib26 "")\], and spatio-temporal VLAs could enable richer reasoning over dynamic events \[ [140](https://arxiv.org/html/2502.03814v4#bib.bib140 "")\], 3D spatial layouts, and real-time cooperative interactions. These architectures would allow multi-robot teams to better interpret evolving environments and adapt their strategies accordingly. As multi-modal and embodied extensions mature, they could bridge the gap between high-level symbolic reasoning and low-level perception-action execution, unlocking more adaptive and autonomous multi-robot coordination \[ [9](https://arxiv.org/html/2502.03814v4#bib.bib9 "")\].

Expanding to Unstructured Environments.
Most current applications and benchmarks focus on indoor or structured environments, leaving significant gaps in outdoor and unstructured scenarios. Research should prioritize expanding MRS capabilities to include operations in open-world contexts, such as agricultural fields, disaster zones, and remote exploration sites. Addressing the unique challenges of these environments, including variability, noise, and unpredictable dynamics, will broaden the applicability of LLM-enabled MRS.

Latest More Capable LLMs.
The continued development of state-of-the-art LLMs opens new possibilities for MRS. Models such as PaliGemma-2, Qwen-3, Claude 4 Sonnet/Opus, GPT o3 or o4-mini, GPT-5, and DeepSeek V3 and R1 offer enhanced reasoning, understanding, and multitasking capabilities \[ [86](https://arxiv.org/html/2502.03814v4#bib.bib86 ""), [126](https://arxiv.org/html/2502.03814v4#bib.bib126 "")\]. Incorporating these advanced models into MRS research can accelerate progress by providing improved baseline performance and enabling innovative applications. Exploring their integration with robotics systems can further push the boundaries of what multi-robot teams can achieve.

## 8 Conclusion

This survey provides the first comprehensive exploration of integrating LLMs into MRS, a topic at the intersection of robotics and artificial intelligence that is rapidly gaining prominence. Unlike general robotics or multi-agent systems, MRS pose unique challenges and opportunities due to their reliance on physical embodiment and real-world interaction. This paper highlights how LLMs can address these challenges, offering novel possibilities for collective intelligence and collaboration in MRS.

We introduced a structured framework for understanding the role of LLMs in MRS, spanning high-level task allocation and planning, mid-level motion planning, low-level action execution, and human intervention. This framework reflects the diverse functionalities enabled by LLMs, including decomposing complex tasks, coordinating multi-robot multi-task scenarios, and facilitating seamless human-robot interaction. Additionally, we reviewed applications of MRS across various domains, from household tasks to construction, formation control, target tracking, and game/competition, demonstrating the versatility and transformative potential of LLMs in these systems.

The significance of integrating LLMs into MRS lies in their ability to augment individual and collective intelligence, enabling robots to operate autonomously and collaboratively in increasingly complex environments. As LLMs continue to demonstrate their potential in everyday applications, their adoption in robotics promises to unlock new possibilities for innovation and efficiency in MRS.

Looking ahead, both immediate and long-term perspectives present exciting opportunities for research and development. In the near term, addressing challenges such as benchmarking, reasoning capabilities, and real-time performance will be critical for bridging the gap between lab-based simulations and real-world applications. Long-term prospects include leveraging LLMs to enable more complex missions, such as disaster response, space exploration, and large-scale autonomous operations, expanding the boundaries of what MRS can achieve.

We hope this survey will be a valuable resource for researchers, providing an overview of current progress, identifying gaps, and highlighting opportunities for future exploration. By advancing our understanding of LLMs in MRS, we aim to inspire innovation and foster collaboration across disciplines, accelerating the transition from theoretical studies to practical deployments that benefit society.

## 9 Acknowledgment

We thank the authors of \[ [76](https://arxiv.org/html/2502.03814v4#bib.bib76 ""), [18](https://arxiv.org/html/2502.03814v4#bib.bib18 ""), [120](https://arxiv.org/html/2502.03814v4#bib.bib120 ""), [134](https://arxiv.org/html/2502.03814v4#bib.bib134 "")\] for granting permission to include their original, unaltered figures in this paper.

## References

- \[1\]↑
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al.

Gpt-4 technical report.

arXiv preprint arXiv:2303.08774, 2023.

- \[2\]↑
Michael Ahn, Montserrat Gonzalez Arenas, Matthew Bennice, Noah Brown, Christine Chan, Byron David, Anthony Francis, Gavin Gonzalez, Rainer Hessmer, Tomas Jackson, Nikhil J. Joshi, Daniel Lam, Tsang-Wei Edward Lee, Alex Luong, Sharath Maddineni, Harsh Patel, Jodilyn Peralta, Jornell Quiambao, Diego Reyes, Rosario M. Jauregui Ruano, Dorsa Sadigh, Pannag Sanketi, Leila Takayama, Pavel Vodenski, and Fei Xia.

VADER: Visual Affordance Detection and Error Recovery for Multi Robot Human Collaboration.

arXiv preprint arXiv:2405.16021, May 2024.

- \[3\]↑
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra Cojocaru, Mérouane Debbah, Étienne Goffinet, Daniel Hesslow, Julien Launay, Quentin Malartic, et al.

The falcon series of open language models.

arXiv preprint arXiv:2311.16867, 2023.

- \[4\]↑
Javier Alonso-Mora, Ross Knepper, Roland Siegwart, and Daniela Rus.

Local motion planning for collaborative multi-robot manipulation of deformable objects.

In 2015 IEEE international conference on robotics and automation (ICRA), pages 5495–5502. IEEE, 2015.

- \[5\]↑
Javier Alonso-Mora, Eduardo Montijano, Mac Schwager, and Daniela Rus.

Distributed multi-robot formation control among obstacles: A geometric and optimization approach with consensus.

In 2016 IEEE international conference on robotics and automation (ICRA), pages 5356–5363. IEEE, 2016.

- \[6\]↑
Xing An, Celimuge Wu, Yangfei Lin, Min Lin, Tsutomu Yoshinaga, and Yusheng Ji.

Multi-robot systems and cooperative object transport: Communications, platforms, and challenges.

IEEE Open Journal of the Computer Society, 4:23–36, 2023.

- \[7\]↑
Anthropic.

Claude, 2024.

Accessed via Anthropic API.

- \[8\]↑
Joseph L Baxter, EK Burke, Jonathan M Garibaldi, and Mark Norman.

Multi-robot search and rescue: A potential field based approach.

Autonomous robots and agents, pages 9–16, 2007.

- \[9\]↑
Peter Belcak, Greg Heinrich, Shizhe Diao, Yonggan Fu, Xin Dong, Saurav Muralidharan, Yingyan Celine Lin, and Pavlo Molchanov.

Small language models are the future of agentic ai.

arXiv preprint arXiv:2506.02153, 2025.

- \[10\]↑
Michele Brienza, Emanuele Musumeci, Vincenzo Suriani, Daniele Affinita, Andrea Pennisi, Daniele Nardi, and Domenico Daniele Bloisi.

LLCoach: Generating Robot Soccer Plans using Multi-Role Large Language Models.

arXiv preprint arXiv:2406.18285, June 2024.

- \[11\]↑
Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, D Driess, A Dubey, C Finn, et al.

Rt-2: Vision-language-action models transfer web knowledge to robotic control. arxiv.

arXiv preprint arXiv:2307.15818, 2023.

- \[12\]↑
Wolfram Burgard, Mark Moors, Cyrill Stachniss, and Frank E Schneider.

Coordinated multi-robot exploration.

IEEE Transactions on robotics, 21(3):376–386, 2005.

- \[13\]↑
Bill Cai, Fei Lu, and Lifeng Zhou.

Energy-aware routing algorithm for mobile ground-to-air charging.

In 2024 IEEE International Symposium of Robotics Research (ISRR). IEEE, 2024.

- \[14\]↑
Junhong Chen, Ziqi Yang, Haoyuan G Xu, Dandan Zhang, and George Mylonas.

Multi-agent systems for robotic autonomy with llms.

In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 4194–4204, 2025.

- \[15\]↑
Junting Chen, Checheng Yu, Xunzhe Zhou, Tianqi Xu, Yao Mu, Mengkang Hu, Wenqi Shao, Yikai Wang, Guohao Li, and Lin Shao.

EMOS: Embodiment-aware Heterogeneous Multi-robot Operating System with LLM Agents.

arXiv preprint arXiv:2410.22662, October 2024.

- \[16\]↑
Siji Chen, Yanshen Sun, Peihan Li, Lifeng Zhou, and Chang-Tien Lu.

Learning decentralized flocking controllers with spatio-temporal graph neural network.

In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 2596–2602. IEEE, 2024.

- \[17\]↑
Weizhe Chen, Sven Koenig, and Bistra Dilkina.

Why Solving Multi-agent Path Finding with Large Language Model has not Succeeded Yet.

arXiv preprint arXiv:2401.03630, feb 2024.

- \[18\]↑
Yongchao Chen, Jacob Arkin, Yang Zhang, Nicholas Roy, and Chuchu Fan.

Scalable Multi-Robot Collaboration with Large Language Models: Centralized or Decentralized Systems?

In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 4311–4317, May 2024.

- \[19\]↑
Fernando Cladera, Zachary Ravichandran, Jason Hughes, Varun Murali, Carlos Nieto-Granda, M Ani Hsieh, George J Pappas, Camillo J Taylor, and Vijay Kumar.

Air-ground collaboration for language-specified missions in unknown environments.

arXiv preprint arXiv:2505.09108, 2025.

- \[20\]↑
Jorge Cortés and Magnus Egerstedt.

Coordinated control of multi-robot systems: A survey.

SICE Journal of Control, Measurement, and System Integration, 10(6):495–503, 2017.

- \[21\]↑
Erwin Coumans and Yunfei Bai.

Pybullet, a python module for physics simulation for games, robotics and machine learning.

[http://pybullet.org](http://pybullet.org/ ""), 2016–2021.

- \[22\]↑
Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen, Chi-Min Chan, Weize Chen, et al.

Parameter-efficient fine-tuning of large-scale pre-trained language models.

Nature Machine Intelligence, 5(3):220–235, 2023.

- \[23\]↑
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al.

The llama 3 herd of models.

arXiv preprint arXiv:2407.21783, 2024.

- \[24\]↑
Maria Valera Espina, Raphael Grech, Deon De Jager, Paolo Remagnino, Luca Iocchi, Luca Marchetti, Daniele Nardi, Dorothy Monekosso, Mircea Nicolescu, and Christopher King.

Multi-robot teams for environmental monitoring.

Innovations in Defence Support Systems–3: Intelligent Paradigms in Security, pages 183–209, 2011.

- \[25\]↑
Roya Firoozi, Johnathan Tucker, Stephen Tian, Anirudha Majumdar, Jiankai Sun, Weiyu Liu, Yuke Zhu, Shuran Song, Ashish Kapoor, Karol Hausman, Brian Ichter, Danny Driess, Jiajun Wu, Cewu Lu, and Mac Schwager.

Foundation Models in Robotics: Applications, Challenges, and the Future.

arXiv preprint arXiv:2312.07843, December 2023.

- \[26\]↑
Tsu-Jui Fu, Linjie Li, Zhe Gan, Kevin Lin, William Yang Wang, Lijuan Wang, and Zicheng Liu.

Violet: End-to-end video-language transformers with masked visual-token modeling.

arXiv preprint arXiv:2111.12681, 2021.

- \[27\]↑
Yuman Gao, Yingjian Wang, Xingguang Zhong, Tiankai Yang, Mingyang Wang, Zhixiong Xu, Yongchao Wang, Yi Lin, Chao Xu, and Fei Gao.

Meeting-merging-mission: A multi-robot coordinate framework for large-scale communication-limited exploration.

In 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 13700–13707. IEEE, 2022.

- \[28\]↑
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, and Haofen Wang.

Retrieval-augmented generation for large language models: A survey.

arXiv preprint arXiv:2312.10997, 2023.

- \[29\]↑
Kunal Garg, Songyuan Zhang, Jacob Arkin, and Chuchu Fan.

Foundation Models to the Rescue: Deadlock Resolution in Connected Multi-Robot Systems.

arXiv preprint arXiv:2404.06413, September 2024.

- \[30\]↑
Jennifer Gielis, Ajay Shankar, and Amanda Prorok.

A critical review of communications in multi-robot systems.

Current robotics reports, 3(4):213–225, 2022.

- \[31\]↑
Toby Godfrey, William Hunt, and Mohammad D. Soorati.

MARLIN: Multi-Agent Reinforcement Learning Guided by Language-Based Inter-Robot Negotiation.

arXiv preprint arXiv:2410.14383, October 2024.

- \[32\]↑
Google.

Gemini, 2024.

Accessed \[Date accessed\], Google AI system.

- \[33\]↑
Ben Grocholsky, James Keller, Vijay Kumar, and George Pappas.

Cooperative air and ground surveillance.

IEEE Robotics & Automation Magazine, 13(3):16–25, 2006.

- \[34\]↑
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al.

Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning.

arXiv preprint arXiv:2501.12948, 2025.

- \[35\]↑
Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V. Chawla, Olaf Wiest, and Xiangliang Zhang.

Large Language Model based Multi-Agents: A Survey of Progress and Challenges.

arXiv preprint arXiv:2402.01680, April 2024.

- \[36\]↑
Piyush Gupta, David Isele, Enna Sachdeva, Pin-Hao Huang, Behzad Dariush, Kwonjoon Lee, and Sangjae Bae.

Generalized mission planning for heterogeneous multi-robot teams via llm-constructed hierarchical trees.

arXiv preprint arXiv:2501.16539, 2025.

- \[37\]↑
Arjun Gupte, Ruiqi Wang, Vishnunandan L. N. Venkatesh, Taehyeon Kim, Dezhong Zhao, and Byung-Cheol Min.

REBEL: Rule-based and Experience-enhanced Learning with LLMs for Initial Task Allocation in Multi-Human Multi-Robot Teams.

arXiv preprint arXiv:2409.16266, September 2024.

- \[38\]↑
Miguel Guzmán-Merino and Nils Sören Krause.

LLM Assistant for heterogeneous multi-robot system dynamic task planning.

September 2024.

Publisher: Technische Universität Hamburg, Institut für Digitales und Autonomes Bauen.

- \[39\]↑
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen.

Lora: Low-rank adaptation of large language models.

arXiv preprint arXiv:2106.09685, 2021.

- \[40\]↑
Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, et al.

A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions.

ACM Transactions on Information Systems, 2023.

- \[41\]↑
Zhehui Huang, Guangyao Shi, and Gaurav S Sukhatme.

From words to routes: Applying large language models to vehicle routing.

arXiv preprint arXiv:2403.10795, 2024.

- \[42\]↑
Zhehui Huang, Guangyao Shi, Yuwei Wu, Vijay Kumar, and Gaurav S Sukhatme.

Compositional coordination for multi-robot teams with large language models.

arXiv preprint arXiv:2507.16068, 2025.

- \[43\]↑
William Hunt, Toby Godfrey, and Mohammad D Soorati.

Conversational language models for human-in-the-loop multi-robot coordination.

arXiv preprint arXiv:2402.19166, 2024.

- \[44\]↑
William Hunt, Sarvapali D. Ramchurn, and Mohammad D. Soorati.

A Survey of Language-Based Communication in Robotics.

arXiv preprint arXiv:2406.04086, September 2024.

- \[45\]↑
Hyeongyo Jeong, Haechan Lee, Changwon Kim, and Sungtae Shin.

A survey of robot intelligence with large language models.

Applied Sciences, 14(19):8868, 2024.

- \[46\]↑
Jiabao Ji, Yongchao Chen, Yang Zhang, Ramana Rao Kompella, Chuchu Fan, Gaowen Liu, and Shiyu Chang.

Collision-and reachability-aware multi-robot control with grounded llm planners.

arXiv preprint arXiv:2505.20573, 2025.

- \[47\]↑
Wenkang Ji, Huaben Chen, Mingyang Chen, Guobin Zhu, Lufeng Xu, Roderich Groß, Rui Zhou, Ming Cao, and Shiyu Zhao.

Genswarm: Scalable multi-robot code-policy generation and deployment via language models.

arXiv preprint arXiv:2503.23875, 2025.

- \[48\]↑
Yitao Jiang, Luyang Zhao, Alberto Quattrini Li, Muhao Chen, and Devin Balkcom.

Exploring spontaneous social interaction swarm robotics powered by large language models.

- \[49\]↑
Chris Jones, Dylan Shell, Maja J Mataric, and Brian Gerkey.

Principled approaches to the design of multi-robot systems.

In Proc. of the Workshop on Networked Robotics, IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS 2004), 2004.

- \[50\]↑
Shyam Sundar Kannan, Vishnunandan L. N. Venkatesh, and Byung-Cheol Min.

SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models.

arXiv preprint arXiv:2309.10062, March 2024.

- \[51\]↑
Kento Kawaharazuka, Tatsuya Matsushima, Andrew Gambardella, Jiaxian Guo, Chris Paxton, and Andy Zeng.

Real-World Robot Applications of Foundation Models: A Review.

arXiv preprint arXiv:2402.05741, October 2024.

- \[52\]↑
Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, and Chelsea Finn.

OpenVLA: An Open-Source Vision-Language-Action Model.

arXiv preprint arXiv:2406.09246, September 2024.

- \[53\]↑
Yeseung Kim, Dohyun Kim, Jieun Choi, Jisang Park, Nayoung Oh, and Daehyung Park.

A Survey on Integration of Large Language Models with Intelligent Robots.

arXiv preprint arXiv:2404.09228, August 2024.

- \[54\]↑
Eric Kolve, Roozbeh Mottaghi, Winson Han, Eli VanderBilt, Luca Weihs, Alvaro Herrasti, Daniel Gordon, Yuke Zhu, Abhinav Gupta, and Ali Farhadi.

AI2-THOR: An Interactive 3D Environment for Visual AI.

arXiv, 2017.

- \[55\]↑
Vijay Kumar and Nathan Michael.

Opportunities and challenges with autonomous micro aerial vehicles.

The International Journal of Robotics Research, 31(11):1279–1291, 2012.

- \[56\]↑
Younes Lakhnati, Max Pascher, and Jens Gerken.

Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming.

arXiv preprint arXiv:2312.07214, March 2024.

- \[57\]↑
Bastian Lampe, Lennart Reiher, Lukas Zanger, Timo Woopen, Raphael van Kempen, and Lutz Eckstein.

Robotkube: Orchestrating large-scale cooperative multi-robot systems with kubernetes and ros.

In 2023 IEEE 26th International Conference on Intelligent Transportation Systems (ITSC), pages 2719–2725. IEEE, 2023.

- \[58\]↑
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

Advances in Neural Information Processing Systems, 33:9459–9474, 2020.

- \[59\]↑
Chengshu Li, Ruohan Zhang, Josiah Wong, Cem Gokmen, Sanjana Srivastava, Roberto Martín-Martín, Chen Wang, Gabrael Levine, Michael Lingelbach, Jiankai Sun, et al.

Behavior-1k: A benchmark for embodied ai with 1,000 everyday activities and realistic simulation.

In Conference on Robot Learning, pages 80–93. PMLR, 2023.

- \[60\]↑
Peihan Li, Jiazhen Liu, Yuwei Wu, and Lifeng Zhou.

Failure-aware multi-robot coordination for resilient and adaptive target tracking.

arXiv preprint arXiv:2508.02529, 2025.

- \[61\]↑
Peihan Li, Vishnu Menon, Bhavanaraj Gudiguntla, Daniel Ting, and Lifeng Zhou.

Challenges Faced by Large Language Models in Solving Multi-Agent Flocking.

Distributed Autonomous Robotics Systems (DARS), April 2024.

- \[62\]↑
Peihan Li, Yuwei Wu, Jiazhen Liu, Gaurav S Sukhatme, Vijay Kumar, and Lifeng Zhou.

Resilient and adaptive replanning for multi-robot target tracking with sensing and communication danger zones.

arXiv preprint arXiv:2409.11230, 2024.

- \[63\]↑
Peihan Li and Lifeng Zhou.

Assignment algorithms for multi-robot multi-target tracking with sufficient and limited sensing capability.

In 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 11035–11041. IEEE, 2023.

- \[64\]↑
Peihan Li and Lifeng Zhou.

Llm-flock: Decentralized multi-robot flocking via large language models and influence-based consensus.

arXiv preprint arXiv:2505.06513, 2025.

- \[65\]↑
Songtao Li and Hao Tang.

Multimodal alignment and fusion: A survey.

arXiv preprint arXiv:2411.17040, 2024.

- \[66\]↑
Zhaoxing Li, Wenbo Wu, Yue Wang, Yanran Xu, William Hunt, and Sebastian Stein.

Hmcf: A human-in-the-loop multi-robot collaboration framework based on large language models.

arXiv preprint arXiv:2505.00820, 2025.

- \[67\]↑
Zhi Li, Ali Vatankhah Barenji, Jiazhi Jiang, Ray Y Zhong, and Gangyan Xu.

A mechanism for scheduling multi robot intelligent warehouse system face with dynamic demand.

Journal of Intelligent Manufacturing, 31:469–480, 2020.

- \[68\]↑
Jiazhao Liang, Hao Huang, Yu Hao, Geeta Chandra Raju Bethala, Congcong Wen, and Yi Fang.

Integrating retrospective framework in multi-robot collaboration.

In 2025 11th International Conference on Automation, Robotics, and Applications (ICARA), pages 195–199. IEEE, 2025.

- \[69\]↑
Jonghan Lim and Ilya Kovalenko.

Dynamic task adaptation for multi-robot manufacturing systems with large language models.

arXiv preprint arXiv:2505.22804, 2025.

- \[70\]↑
Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, et al.

Deepseek-v3 technical report.

arXiv preprint arXiv:2412.19437, 2024.

- \[71\]↑
Jiazhen Liu, Peihan Li, Yuwei Wu, Gaurav S Sukhatme, Vijay Kumar, and Lifeng Zhou.

Multi-robot target tracking with sensing and communication danger zones.

Distributed Autonomous Robotic Systems (DARS), 2024.

- \[72\]↑
Jiazhen Liu, Lifeng Zhou, Ragesh Ramachandran, Gaurav S Sukhatme, and Vijay Kumar.

Decentralized risk-aware tracking of multiple targets.

In International Symposium on Distributed Autonomous Robotic Systems, pages 408–423. Springer, 2022.

- \[73\]↑
Jun Liu, Lifeng Zhou, Pratap Tokekar, and Ryan K Williams.

Distributed resilient submodular action selection in adversarial environments.

IEEE Robotics and Automation Letters, 6(3):5832–5839, 2021.

- \[74\]↑
Kehui Liu, Zixin Tang, Dong Wang, Zhigang Wang, Bin Zhao, and Xuelong Li.

COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models.

arXiv preprint arXiv:2409.15146, September 2024.

- \[75\]↑
Xu Liu, Ankit Prabhu, Fernando Cladera, Ian D Miller, Lifeng Zhou, Camillo J Taylor, and Vijay Kumar.

Active metric-semantic mapping by multiple aerial robots.

In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages 3282–3288. IEEE, 2023.

- \[76\]↑
Zhiwei Liu, Weiran Yao, Jianguo Zhang, Le Xue, Shelby Heinecke, Rithesh Murthy, Yihao Feng, Zeyuan Chen, Juan Carlos Niebles, Devansh Arpit, Ran Xu, Phil Mui, Huan Wang, Caiming Xiong, and Silvio Savarese.

BOLAA: Benchmarking and Orchestrating LLM-augmented Autonomous Agents.

arXiv preprint arXiv:2308.05960, August 2023.

- \[77\]↑
Ryan Luna and Kostas E Bekris.

Efficient and complete centralized multi-robot path planning.

In 2011 IEEE/RSJ International Conference on Intelligent Robots and Systems, pages 3268–3275. IEEE, 2011.

- \[78\]↑
Cai Luo, Andre Possani Espinosa, Danu Pranantha, and Alessandro De Gloria.

Multi-robot search and rescue team.

In 2011 IEEE International Symposium on Safety, Security, and Rescue Robotics, pages 296–301. IEEE, 2011.

- \[79\]↑
Artem Lykov, Maria Dronova, Nikolay Naglov, Mikhail Litvinov, Sergei Satsevich, Artem Bazhenov, Vladimir Berman, Aleksei Shcherbak, and Dzmitry Tsetserukou.

LLM-MARS: Large Language Model for Behavior Tree Generation and NLP-enhanced Dialogue in Multi-Agent Robot Systems.

arXiv preprint arXiv:2312.09348, December 2023.

- \[80\]↑
Artem Lykov, Sausar Karaf, Mikhail Martynov, Valerii Serpiva, Aleksey Fedoseev, Mikhail Konenkov, and Dzmitry Tsetserukou.

Flockgpt: Guiding uav flocking with linguistic orchestration.

arXiv preprint arXiv:2405.05872, 2024.

- \[81\]↑
Kai-Chieh Ma, Zhibei Ma, Lantao Liu, and Gaurav S Sukhatme.

Multi-robot informative and adaptive planning for persistent environmental monitoring.

In Distributed Autonomous Robotic Systems: The 13th International Symposium, pages 285–298. Springer, 2018.

- \[82\]↑
Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, and Irwin King.

A survey on vision-language-action models for embodied ai.

arXiv preprint arXiv:2405.14093, 2024.

- \[83\]↑
Vagul Mahadevan, Shangtong Zhang, and Rohan Chandra.

Gamechat: Multi-llm dialogue for safe, agile, and socially optimal multi-agent navigation in constrained environments.

arXiv preprint arXiv:2503.12333, 2025.

- \[84\]↑
Zhao Mandi, Shreeya Jain, and Shuran Song.

RoCo: Dialectic Multi-Robot Collaboration with Large Language Models.

In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 286–299, May 2024.

- \[85\]↑
Siddharth Mayya, Ragesh K Ramachandran, Lifeng Zhou, Vinay Senthil, Dinesh Thakur, Gaurav S Sukhatme, and Vijay Kumar.

Adaptive and risk-aware target tracking for robot teams with heterogeneous sensors.

IEEE Robotics and Automation Letters, 7(2):5615–5622, 2022.

- \[86\]↑
Shervin Minaee, Tomas Mikolov, Narjes Nikzad, Meysam Chenaghlu, Richard Socher, Xavier Amatriain, and Jianfeng Gao.

Large language models: A survey.

arXiv preprint arXiv:2402.06196, 2024.

- \[87\]↑
Iman Mirzadeh, Keivan Alizadeh, Hooman Shahrokhi, Oncel Tuzel, Samy Bengio, and Mehrdad Farajtabar.

GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models.

arXiv preprint arXiv:2410.05229, October 2024.

- \[88\]↑
Steven Morad, Ajay Shankar, Jan Blumenkamp, and Amanda Prorok.

Language-Conditioned Offline RL for Multi-Robot Navigation.

arXiv preprint arXiv:2407.20164, July 2024.

- \[89\]↑
Humza Naveed, Asad Ullah Khan, Shi Qiu, Muhammad Saqib, Saeed Anwar, Muhammad Usman, Naveed Akhtar, Nick Barnes, and Ajmal Mian.

A comprehensive overview of large language models.

arXiv preprint arXiv:2307.06435, 2023.

- \[90\]↑
Kazuma Obata, Tatsuya Aoki, Takato Horii, Tadahiro Taniguchi, and Takayuki Nagai.

LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning.

arXiv preprint arXiv:2410.21040, October 2024.

- \[91\]↑
Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Abhishek Gupta, Abhishek Padalkar, Abraham Lee, Acorn Pooley, Agrim Gupta, Ajay Mandlekar, Ajinkya Jain, et al.

Open x-embodiment: Robotic learning datasets and rt-x models: Open x-embodiment collaboration 0.

In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 6892–6903. IEEE, 2024.

- \[92\]↑
Lynne E Parker.

Handbook of robotics chapter 40: Multiple mobile robot systems, 2008.

- \[93\]↑
Mingming Peng, Zhendong Chen, Jie Yang, Jin Huang, Zhengqi Shi, Qihao Liu, Xinyu Li, and Liang Gao.

Automatic milp model construction for multi-robot task allocation and scheduling based on large language models.

arXiv preprint arXiv:2503.13813, 2025.

- \[94\]↑
Xavi Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Ruslan Partsey, Jimmy Yang, Ruta Desai, Alexander William Clegg, Michal Hlavac, Tiffany Min, Theo Gervet, Vladimir Vondrus, Vincent-Pierre Berges, John Turner, Oleksandr Maksymets, Zsolt Kira, Mrinal Kalakrishnan, Jitendra Malik, Devendra Singh Chaplot, Unnat Jain, Dhruv Batra, Akshara Rai, and Roozbeh Mottaghi.

Habitat 3.0: A co-habitat for humans, avatars and robots, 2023.

- \[95\]↑
Jorge Pena Queralta, Jussi Taipalmaa, Bilge Can Pullinen, Victor Kathan Sarker, Tuan Nguyen Gia, Hannu Tenhunen, Moncef Gabbouj, Jenni Raitoharju, and Tomi Westerlund.

Collaborative multi-robot search and rescue: Planning, coordination, perception, and active vision.

Ieee Access, 8:191617–191643, 2020.

- \[96\]↑
Abhinav Rajvanshi, Pritish Sahu, Tixiao Shan, Karan Sikka, and Han-Pang Chiu.

Sayconav: Utilizing large language models for adaptive collaboration in decentralized multi-robot navigation.

arXiv preprint arXiv:2505.13729, 2025.

- \[97\]↑
Ragesh K Ramachandran, Lifeng Zhou, James A Preiss, and Gaurav S Sukhatme.

Resilient coverage: Exploring the local-to-global trade-off.

In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 11740–11747. IEEE, 2020.

- \[98\]↑
Yara Rizk, Mariette Awad, and Edward W Tunstel.

Cooperative heterogeneous multi-robot systems: A survey.

ACM Computing Surveys (CSUR), 52(2):1–31, 2019.

- \[99\]↑
Ariel Rosenfeld, A Noa, O Maksimov, and S Kraus.

Human-multi-robot team collaboration for efficient warehouse operation.

Autonomous Robots and Multirobot Systems (ARMS), 2016.

- \[100\]↑
Manolis Savva, Abhishek Kadian, Oleksandr Maksymets, Yili Zhao, Erik Wijmans, Bhavana Jain, Julian Straub, Jia Liu, Vladlen Koltun, Jitendra Malik, Devi Parikh, and Dhruv Batra.

Habitat: A Platform for Embodied AI Research.

In Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), 2019.

- \[101\]↑
Mac Schwager, Brian J Julian, Michael Angermann, and Daniela Rus.

Eyes in the sky: Decentralized control for the deployment of robotic camera networks.

Proceedings of the IEEE, 99(9):1541–1561, 2011.

- \[102\]↑
Vishnu D Sharma, Maymoonah Toubeh, Lifeng Zhou, and Pratap Tokekar.

Risk-aware planning and assignment for ground vehicles using uncertain perception from aerial vehicles.

In 2020 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pages 11763–11769. IEEE, 2020.

- \[103\]↑
Vishnu Dutt Sharma, Lifeng Zhou, and Pratap Tokekar.

D2coplan: A differentiable decentralized planner for multi-robot coverage.

In 2023 IEEE International Conference on Robotics and Automation (ICRA), pages 3425–3431. IEEE, 2023.

- \[104\]↑
Zhixuan Shen, Haonan Luo, Kexun Chen, Fengmao Lv, and Tianrui Li.

Enhancing multi-robot semantic navigation through multimodal chain-of-thought score collaboration.

In Proceedings of the AAAI Conference on Artificial Intelligence, volume 39, pages 14664–14672, 2025.

- \[105\]↑
Guangyao Shi, Ishat E Rabban, Lifeng Zhou, and Pratap Tokekar.

Communication-aware multi-robot coordination with submodular maximization.

In 2021 IEEE International Conference on Robotics and Automation (ICRA), pages 8955–8961. IEEE, 2021.

- \[106\]↑
Guangyao Shi, Lifeng Zhou, and Pratap Tokekar.

Robust multiple-path orienteering problem: Securing against adversarial attacks.

IEEE Transactions on Robotics, 39(3):2060–2077, 2023.

- \[107\]↑
Volker Strobel, Marco Dorigo, and Mario Fritz.

LLM2Swarm: Robot Swarms that Responsively Reason, Plan, and Collaborate through LLMs.

arXiv preprint arXiv:2410.11387, October 2024.

- \[108\]↑
Yuichiro Sueoka, Yuki Kato, Takahiro Yoshida, Koichi Osuka, Ryosuke Yajima, Shota Chikushi, Keiji Nagatani, and Hajime Asama.

Adaptivity of a Multi-Robot Coordination System based on Functional Expressions using Large Language Models.

Distributed Autonomous Robotics Systems (DARS), 2024.

- \[109\]↑
Andrew Szot, Alex Clegg, Eric Undersander, Erik Wijmans, Yili Zhao, John Turner, Noah Maestre, Mustafa Mukadam, Devendra Chaplot, Oleksandr Maksymets, Aaron Gokaslan, Vladimir Vondrus, Sameer Dharur, Franziska Meier, Wojciech Galuba, Angel Chang, Zsolt Kira, Vladlen Koltun, Jitendra Malik, Manolis Savva, and Dhruv Batra.

Habitat 2.0: Training home assistants to rearrange their habitat.

In Advances in Neural Information Processing Systems (NeurIPS), 2021.

- \[110\]↑
Kshitij Tiwari and Nak Young Chong.

Multi-robot Exploration for Environmental Monitoring: The Resource Constrained Perspective.

Academic Press, 2019.

- \[111\]↑
Kam Fai Elvis Tsang, Yuqing Ni, Cheuk Fung Raphael Wong, and Ling Shi.

A novel warehouse multi-robot automation system with semi-complete and computationally efficient path planning and adaptive genetic task allocation algorithms.

In 2018 15th International Conference on Control, Automation, Robotics and Vision (ICARCV), pages 1671–1676. IEEE, 2018.

- \[112\]↑
A Vaswani.

Attention is all you need.

Advances in Neural Information Processing Systems, 2017.

- \[113\]↑
Vishnunandan L. N. Venkatesh and Byung-Cheol Min.

ZeroCAP: Zero-Shot Multi-Robot Context Aware Pattern Formation via Large Language Models.

arXiv preprint arXiv:2404.02318, September 2024.

- \[114\]↑
Sebastian Wallkötter, Silvia Tulli, Ginevra Castellano, Ana Paiva, and Mohamed Chetouani.

Explainable embodied agents through social cues: a review.

ACM Transactions on Human-Robot Interaction (THRI), 10(3):1–24, 2021.

- \[115\]↑
Hanwen Wan, Yuhan Zhang, Junjie Wang, Donghao Wu, Mengkang Li, Xilun Chen, Yixuan Deng, Yuxuan Huang, Zhenglong Sun, Lin Zhang, et al.

Toward universal embodied planning in scalable heterogeneous field robots collaboration and control.

Journal of Field Robotics, 2025.

- \[116\]↑
Chao Wang, Stephan Hasler, Daniel Tanneberg, Felix Ocker, Frank Joublin, Antonello Ceravola, Joerg Deigmoeller, and Michael Gienger.

Large language models for multi-modal human-robot interaction.

arXiv preprint arXiv:2401.15174, 2024.

- \[117\]↑
Jiaqi Wang, Zihao Wu, Yiwei Li, Hanqi Jiang, Peng Shu, Enze Shi, Huawen Hu, Chong Ma, Yiheng Liu, Xuhui Wang, et al.

Large language models for robotics: Opportunities, challenges, and perspectives.

arXiv preprint arXiv:2401.04334, 2024.

- \[118\]↑
Jun Wang, Guocheng He, and Yiannis Kantaros.

Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction.

arXiv preprint arXiv:2402.15368, October 2024.

- \[119\]↑
Weizheng Wang, Ike Obi, and Byung-Cheol Min.

Multi-agent llm actor-critic framework for social robot navigation.

arXiv preprint arXiv:2503.09758, 2025.

- \[120\]↑
Yongdong Wang, Runze Xiao, Jun Younes Louhi Kasahara, Ryosuke Yajima, Keiji Nagatani, Atsushi Yamashita, and Hajime Asama.

DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models.

arXiv preprint arXiv:2411.09022 version: 1, November 2024.

- \[121\]↑
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al.

Emergent abilities of large language models.

arXiv preprint arXiv:2206.07682, 2022.

- \[122\]↑
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al.

Chain-of-thought prompting elicits reasoning in large language models.

Advances in neural information processing systems, 35:24824–24837, 2022.

- \[123\]↑
Pengying Wu, Yao Mu, Kangjie Zhou, Ji Ma, Junting Chen, and Chang Liu.

CAMON: Cooperative Agents for Multi-Object Navigation with LLM-based Conversations.

arXiv preprint arXiv:2407.00632, June 2024.

- \[124\]↑
Yuwei Wu, Yuezhan Tao, Peihan Li, Guangyao Shi, Gaurav S. Sukhatmem, Vijay Kumar, and Lifeng Zhou.

Hierarchical LLMs In-the-loop Optimization for Real-time Multi-Robot Target Tracking under Unknown Hazards.

arXiv preprint arXiv:2409.12274, September 2024.

- \[125\]↑
Peter R Wurman, Raffaello D’Andrea, and Mick Mountz.

Coordinating hundreds of cooperative, autonomous vehicles in warehouses.

AI magazine, 29(1):9–9, 2008.

- \[126\]↑
Fengli Xu, Qianyue Hao, Zefang Zong, Jingwei Wang, Yunke Zhang, Jingyi Wang, Xiaochong Lan, Jiahui Gong, Tianjian Ouyang, Fanjin Meng, et al.

Towards large reasoning models: A survey of reinforced reasoning with large language models.

arXiv preprint arXiv:2501.09686, 2025.

- \[127\]↑
Shaojun Xu, Xusheng Luo, Yutong Huang, Letian Leng, Ruixuan Liu, and Changliu Liu.

Scaling Up Natural Language Understanding for Multi-Robots Through the Lens of Hierarchy.

arXiv preprint arXiv:2408.08188, August 2024.

- \[128\]↑
Xiaohan Xu, Ming Li, Chongyang Tao, Tao Shen, Reynold Cheng, Jinyang Li, Can Xu, Dacheng Tao, and Tianyi Zhou.

A survey on knowledge distillation of large language models.

arXiv preprint arXiv:2402.13116, 2024.

- \[129\]↑
Dong Xue, Xuanjie Zhou, Ming Wang, and Fangzhou Liu.

Formation control and path planning of multi-robot systems via large language models.

Science China Information Sciences, 68(5):150205, 2025.

- \[130\]↑
Zhi Yan, Nicolas Jouandeau, and Arab Ali Cherif.

A survey and analysis of multi-robot coordination.

International Journal of Advanced Robotic Systems, 10(12):399, 2013.

- \[131\]↑
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu.

Qwen2.5 technical report.

arXiv preprint arXiv:2412.15115, 2024.

- \[132\]↑
Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong Chen.

A survey on multimodal large language models.

arXiv preprint arXiv:2306.13549, 2023.

- \[133\]↑
Takahiro Yoshida, Yuichiro Sueoka, and Koichi Osuka.

Verification of a Two-Step Inference Model for Cooperative Evaluation of Robot Actions Using Foundation Models.

Distributed Autonomous Robotics Systems (DARS), 2024.

- \[134\]↑
Bangguo Yu, Hamidreza Kasaei, and Ming Cao.

Co-NavGPT: Multi-Robot Cooperative Visual Semantic Navigation using Large Language Models.

arXiv preprint arXiv:2310.07937, December 2023.

- \[135\]↑
Wenhao Yu, Jie Peng, Yueliang Ying, Sai Li, Jianmin Ji, and Yanyong Zhang.

MHRC: Closed-loop Decentralized Multi-Heterogeneous Robot Collaboration with Large Language Models.

arXiv preprint arXiv:2409.16030, September 2024.

- \[136\]↑
Rahul Zahroof, Jiazhen Liu, Lifeng Zhou, and Vijay Kumar.

Multi-robot localization and target tracking with connectivity maintenance and collision avoidance.

In 2023 American Control Conference (ACC), pages 1331–1338. IEEE, 2023.

- \[137\]↑
Fanlong Zeng, Wensheng Gan, Yongheng Wang, Ning Liu, and Philip S. Yu.

Large Language Models for Robotics: A Survey.

arXiv preprint arXiv:2311.07226, November 2023.

- \[138\]↑
Shengyu Zhang, Linfeng Dong, Xiaoya Li, Sen Zhang, Xiaofei Sun, Shuhe Wang, Jiwei Li, Runyi Hu, Tianwei Zhang, Fei Wu, et al.

Instruction tuning for large language models: a survey. arxiv.

arXiv preprint arXiv:2308.10792, 2023.

- \[139\]↑
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al.

A survey of large language models.

arXiv preprint arXiv:2303.18223, 2023.

- \[140\]↑
Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov, Furong Huang, and Jianwei Yang.

Tracevla: Visual trace prompting enhances spatial-temporal awareness for generalist robotic policies.

arXiv preprint arXiv:2412.10345, 2024.

- \[141\]↑
Yifan Zhong, Fengshuo Bai, Shaofei Cai, Xuchuan Huang, Zhang Chen, Xiaowei Zhang, Yuanfei Wang, Shaoyang Guo, Tianrui Guan, Ka Nam Lui, et al.

A survey on vision-language-action models: An action tokenization perspective.

arXiv preprint arXiv:2507.01925, 2025.

- \[142\]↑
Lifeng Zhou and Vijay Kumar.

Robust multi-robot active target tracking against sensing and communication attacks.

IEEE Transactions on Robotics, 39(3):1768–1780, 2023.

- \[143\]↑
Lifeng Zhou, Vishnu D Sharma, Qingbiao Li, Amanda Prorok, Alejandro Ribeiro, Pratap Tokekar, and Vijay Kumar.

Graph neural networks for decentralized multi-robot target tracking.

In 2022 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR), pages 195–202. IEEE, 2022.

- \[144\]↑
Lifeng Zhou and Pratap Tokekar.

Active target tracking with self-triggered communications in multi-robot teams.

IEEE Transactions on Automation Science and Engineering, 16(3):1085–1096, 2018.

- \[145\]↑
Lifeng Zhou and Pratap Tokekar.

An approximation algorithm for risk-averse submodular optimization.

In International workshop on the algorithmic foundations of robotics, pages 144–159. Springer, 2018.

- \[146\]↑
Lifeng Zhou and Pratap Tokekar.

Sensor assignment algorithms to improve observability while tracking targets.

IEEE Transactions on Robotics, 35(5):1206–1219, 2019.

- \[147\]↑
Lifeng Zhou and Pratap Tokekar.

Multi-robot coordination and planning in uncertain and adversarial environments.

Current Robotics Reports, 2:147–157, 2021.

- \[148\]↑
Lifeng Zhou and Pratap Tokekar.

Risk-aware submodular optimization for multirobot coordination.

IEEE Transactions on Robotics, 38(5):3064–3084, 2022.

- \[149\]↑
Lifeng Zhou, Vasileios Tzoumas, George J Pappas, and Pratap Tokekar.

Resilient active target tracking with multiple robots.

IEEE Robotics and Automation Letters, 4(1):129–136, 2018.

- \[150\]↑
Lifeng Zhou, Vasileios Tzoumas, George J Pappas, and Pratap Tokekar.

Distributed attack-robust submodular maximization for multirobot planning.

IEEE Transactions on Robotics, 38(5):3097–3112, 2022.

- \[151\]↑
Yichen Zhu, Zhicai Ou, Xiaofeng Mou, and Jian Tang.

Retrieval-augmented embodied agents.

In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 17985–17995, 2024.

- \[152\]↑
Daniel M Ziegler, Nisan Stiennon, Jeffrey Wu, Tom B Brown, Alec Radford, Dario Amodei, Paul Christiano, and Geoffrey Irving.

Fine-tuning language models from human preferences.

arXiv preprint arXiv:1909.08593, 2019.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

<details>
<summary>Real Agents vs. Workflows: The Truth Behind AI 'Agents'</summary>

# Real Agents vs. Workflows: The Truth Behind AI 'Agents'

[00:00] What most people call agents aren't agents. (A cartoon man in a suit says "Hello, Mr. Agent" to a robot labeled "IMPOSTER") I've never really liked the term agent, until I saw this recent article by Anthropic, where I totally agree and now see how we can call something an agent. (A screenshot of an Anthropic blog post titled "Building effective agents" is shown, with a definition of "Agent" highlighted)
[00:12] The vast majority is simply API calls to a language model. (Text appears: "MOST AGENTS ARE JUST API CALL TO LLM", with a small robot thinking) This is this: a few lines of code and a prompt. (Python code for an OpenAI chat completion call is displayed in a box) This cannot act independently, make decisions, or do anything. It simply replies to your users. (Text highlights appear: "Can't act independently", "Can't make decisions", "Just replies to users") Still, we call them agents.
[00:29] But this isn't what we need. We need real agents. (Text appears: "WE NEED REAL AGENTS") But what is a real agent? (Question marks appear around the text)
[00:34] Before we dive into serious agentic stuff, if you are a student, writer, blogger, or content creator, like me, or would like help becoming one, you will love the sponsor of today's video with a clever name, Originality.ai. (A three-panel split screen shows a student reading, a man typing on a laptop, and a man talking; then the Originality.ai logo appears) Originality.ai is an awesome tool designed to detect AI generated content, check for plagiarism, grammar, readability, and even fact check your work. (A screenshot of the Originality.ai website is shown, highlighting its features: Accurate AI Detection, Plagiarism Checking, Fact Checking Aid) Everything you need to publish with integrity.
[00:59] Simply upload a document, in seconds it flags any AI generated text, highlights plagiarism, and even checks grammar and readability with many useful tips and suggestions. (A demo of the Originality.ai content scanner is shown, displaying AI detection, plagiarism check, fact checking, readability score, and grammar check results on a document) I really love this feature. It also offers fact checking, ensuring every claim in your content stands up to scrutiny. Pretty cool when you work on important or technical work.
[01:19] All based on the most state-of-the-art language models and systems. Try originality.ai today with the first link in the description. (Text appears: "LINK IS IN THE DESCRIPTION")
[01:26] So let's start over. (The speaker is visible in a small circle in the corner) We have an LLM access programmatically, which is through an API or access locally in your own server or machine. (A "Query" box connects to an "LLM" box with a neural network icon) And then what? Well, we needed it to take action or do something more than just generate text. How? By giving it access to tools and their documentation. (The "Query" box connects to a "SQL Query" box) We give them access to a tool like the ability to execute SQL queries in a database to access private knowledge. (Inside "SQL Query", "Infer Schema" and "Construct SQL Query" boxes appear) Specifically, we code all that ourselves to have our LLM generate SQL queries. (An "Execute SQL Query" box appears, connecting to "BigQuery Tables") And then our code will send and execute the query automatically in our database.
[02:03] We then send back the outputs so that it uses them to answer the user. (Arrows go from "Execute SQL Query" to "Error" leading to "Self Correct" and "Success" leading to "Optimize", then back to "Construct SQL Query" or "Execute SQL Query". An arrow goes from "BigQuery Tables" to "LLM" labeled "Content Retrieved", then from "LLM" to "Answer") This is what another great proportion of people call agents. They are still not agents. (Text "NOT AN AGENT" appears repeatedly in the background) This is simply a process hardcoded or with small variations like routers that we discuss in the course. Of course, it's useful and it's super powerful. Yet, it's not an intelligent being or something independent. (The background changes to "WORKFLOW") It's not an agent acting on our behalf. It's simply a program we made and control. Or, as Anthropic calls it, a workflow.
[02:36] Don't get me wrong. A workflow is pretty damn useful and it can be quite complex and advanced. (The speaker is visible again) We can implement intelligent routers to decide what tool to use and when to give it access to various databases. Have it decide which one to query and when. (A flowchart shows "In" leading to "LLM Call Router", which branches to "LLM Call 1", "LLM Call 2", "LLM Call 3", all leading to "Out") Have it execute tasks through action tools, through code, and more. Plus, you can have as many workflows as you wish. (The speaker is visible again) Yet, I simply want to state how different it is than an actual agent, the type of agent we dream of and the type Ilya mentioned at a recent talk I attended at NeurIPS.
[03:09] So right now we have our incredible language models and the unbelievable chat bot and they can even do things but they're also kind of strangely unreliable and they get confused when while also having dramatically superhuman performance on evals so it's really unclear how to reconcile this. But eventually, sooner or later, the following will be achieved: those systems are actually going to be agentic in a real ways whereas right now the systems are not agents in any meaningful sense just very that might be too strong they're very very slightly agentic. Just the beginning. (A YouTube video of Ilya Sutskever's NeurIPS 2024 talk is shown with captions and a slide titled "What comes next? The long term" with "Superintelligence" and "Agentic" listed)
[03:46] The next natural question might be: what exactly is a "real agent"? (Text: "WHAT EXACTLY IS A "REAL AGENT"?" appears on a blue background) In simple terms, a real agent is something that functions independently. (Text: "- Something that functions independently" appears) More specifically, it's something capable of employing processes like our System 2 thinking. (A brain graphic with "SYSTEM 2" on the left and "SYSTEM 1" on the right appears) Able to genuinely reason, reflect, and recognize when it lacks knowledge. (Text under "SYSTEM 2": "- Reason", "- Reflect", "- Recognize lack of knowledge") This is almost the opposite of our System 1 thinking, which is fast, automatic, and based purely on patterns and learned responses. (Text under "SYSTEM 1": "- Fast", "- Automatic", "- Based purely on patterns and learned response") Like reflexes when you need to catch a dropping glass. (Text under "SYSTEM 1": "i.e. Reflexes while catching the dropping glass")
[04:16] By contrast, System 2 thinking might involve deciding whether to prevent the glass from falling in the first place, perhaps by using a nearby tool like a tray or moving the fragile object out of the way. (Text under "SYSTEM 2": "i.e. Thinking to prevent the glass from falling") A real agent then will not only know how to use tools but also decide when and why to use them based on deliberate reasoning. (Text appears: "A real agent deliberately decides when and why to use tools with deliberate reasoning") OpenAI's new o1 and o3 series exemplified this shift. As they begin exploring System 2-like approaches and try to make models reason by first discussing with themselves internally, mimicking a human-like approach to reasoning before speaking. (Screenshots of OpenAI blog posts introducing o1 and o3-mini are shown, then a video of people discussing, with text: "System 2-like approach", and a screenshot of an o1-preview chat showing "Thinking" and "Reason" internally before answering)
[04:52] Unlike traditional language models that rely on next-word or next-token prediction, essentially a System 1 instant thinking mechanism, purely based on what it knows and learned to guess the next instant thing to go with no plan. (A diagram of a Transformer model is shown with "Next-word prediction" highlighted and arrows showing output tokens being predicted one by one) These new models aim to incorporate deeper reasoning capabilities, making a move toward the deliberate, reflective thinking associated with System 2, something required for a true agent to be. (The speaker is visible again) But we are diverging a bit too much with this Kahneman parenthesis. Let me clarify what I mean by a real agent by going back to workflows and what they really are.
[05:29] Workflows follow specific code lines and integrations and other than the LLM's outputs, are pretty predictable. (Text "WORKFLOW" appears on a blue background, with bullet points: "- Follow specific code lines and Integrations", "- Predictable output") They are responsible for most of the advanced applications you see and use today and for a reason. They are consistent, more predictable, and incredibly powerful when leveraged properly. (More bullet points appear: "- Responsible for most of the advanced applications", "- Consistent", "- More predictable", "- Incredibly powerful") As Anthropic wrote, workflows are systems where LLMs and tools are orchestrated through predefined code paths. (Screenshot of Anthropic blog post, with "Workflows are systems where LLMs and tools are orchestrated through predefined code paths" highlighted) Here's what a workflow looks like.
[05:56] We have our LLM, some tools or memory to retrieve for additional context, iterate a bit with multiple calls to the LLM, and then an output sent back to the user. (The SQL Query flowchart is shown again, with the speaker in the corner) As we discussed, when a system needs to sometimes do a task and sometimes another depending on conditions, workflows can use a router. (The LLM Call Router flowchart is shown again, with "LLM Call Router" highlighted) With various conditions to select the right tool or the right prompt to use. They can even work in parallel to be more efficient.
[06:23] Better, we can have some sort of main model, which we refer to as an orchestrator, that selects all the different fellow models to call for specific tasks and synthesizes the results, such as our SQL example, where we'd have the main orchestrator getting the user query and could decide if it needs to query a dataset or not, and if it does, ask the SQL agent to generate the SQL query and query the dataset and get it back and synthesize the final answer thanks to all the information provided. (A flowchart shows "In" leading to "Orchestrator", which branches to "LLM Call 1", "LLM Call 2", "LLM Call 3", then all converge to "Synthesizer" and finally "Out". The SQL Query flowchart is shown again, with "WORKFLOW" text in background) This is a workflow.
[06:54] Just like ChatGPT is a workflow, sometimes using Canvas and sometimes just straight-up answering your question. (A screenshot of the OpenAI Canvas blog post is shown) Even if complex and advanced, it is still all hardcoded. (The speaker is visible again) If you know what you need your system to do, you need a workflow, however advanced it may be. (Text appears: "If you know what you need your system to do", then "YOU NEED A WORKFLOW") For instance, what CrewAI calls agents function like predefined workflows assigned to specific tasks. (A screenshot of CrewAI's "Sample Use Cases" is shown, with Marketing, Analytics, Finance, and Technology use cases highlighted as "agents")
[07:18] While Anthropic envisions an agent as a single system capable of reasoning through any task independently. (Screenshot of Anthropic blog post with "Single system capable of reasoning through any task independently" highlighted) Both approaches have merit. One is predictable and intuitive, while the other aims for flexibility and adaptability. (A split screen shows "WORKFLOW" with "- Predictable", "- Intuitive", "- Easier to achieve" and "AGENT" with "- Flexibility", "- Adaptability", "- Far harder to achieve") However, the latter is far harder to achieve with current models and better fits an agent definition to me. (The speaker is visible again)
[07:40] So about those real agents. (Screenshot of Anthropic blog post again) Agents, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks themselves. (The text defining "Agents" is highlighted) This is what Anthropic wrote, and it is what I agree the most with.
[07:55] Real agents make a plan by exchanging with you and understanding your needs. (Text "REAL AGENTS" appears on a blue background with bullet points: "- Make a plan by exchanging with user", "- Understand user needs") Iterate at a "reasoning" level to decide on the steps to take to solve the problem or query. (Bullet point: "- Iterate at a "reasoning" level to decide on steps for solution") Ideally, it will even ask you if it needs more information or clarification instead of hallucinating as with current LLMs. (Bullet point: "- Ask user if it needs more information or clarification instead of hallucinating") Still, they cannot be simply built. They require a very powerful LLM, better than those we have now, and an environment to evolve in. (A diagram shows "Human" interacting with "LLM Call", which can perform "Action" in an "Environment" and receive "Feedback", or "Stop") Like a discussion with you and some extra powers like tools that they can use themselves whenever they see fit and iterate.
[08:31] In short, you can see agents almost as replacing someone or a role. (A split screen shows "WORKFLOW" with "Replace a task one would do" and "AGENT" with "Replace someone or a role") There is no hardcoded path; the agentic system will make its decisions. They are much more advanced and complex things that we still haven't built very successfully yet. This independence and trust in your system obviously makes it more susceptible to failures, more expensive to run and use, added latency, and worst of all, the results aren't that exciting now. (Text boxes with these points appear on screen) When they are, they are completely inconsistent.
[09:03] So what is an actual good example of an agent? Two examples that quickly come to my mind are Devin's and Anthropic's computer use. (Logos for "ANTHROPIC" and "Devin" appear on screen) Yet, they are for now disappointing agents. (The speaker is visible again) If you're curious about Devin, there's a really good blog from Hamel Husain sharing his experience using it. (A screenshot of Hamel Husain's blog about Devin is shown) Devin offers an intriguing glimpse into the promise and challenges of agent-based systems. (A screenshot of Devin's workspace is shown, with a user prompt to benchmark Llama 2) This designed as a fully autonomous software engineer with its own computing environment and independently handles tasks like API integrations and real-time problem solving. (Devin's planner and code editor are shown, with Devin performing tasks like reading API documentation and writing code)
[09:37] However, as Hamel's extensive testing demonstrated, while Devin excelled at simpler, well-defined tasks, things that we can usually do quite easily, it struggled with complex or autonomous ones, often providing over-complicated solutions and pursuing unfeasible paths. (The speaker is visible again) Whereas advanced workflows like Cursor don't have as many issues. (A screenshot of Cursor, "The AI Code Editor" is shown) These limitations reflect the broader challenges of building reliable, context-aware agents with current LLMs, even if you raise millions and millions.
[10:07] Here, Devin aligns more with Anthropic's vision, showcasing the promise and challenges of a reasoning agent. (Devin logo appears again) It can autonomously tackle complex problems but struggle with inconsistency. (The speaker is visible again) By contrast, workflows like those inspired by CrewAI are simpler and more robust for specific tasks but lack the flexibility of true reasoning systems. (CrewAI logo appears again) Similarly, we have Anthropic's ambitious attempt at creating an autonomous agent having access to our computer. (ANTHROPIC logo appears again) Anthropic computer use, which had lots of hype when it first came out and has since been quite forgotten. (Text: "Computer use for coding" with a mouse pointer; then a demo of Anthropic's computer use agent creating a website) The system was undeniably complex and embodied the characteristics of a true agent: autonomous decision-making, dynamic tool usage, and the ability to interact with its environment. (Highlighted text appears on screen over the demo) Its goal was also to replace anyone on a computer. Quite promising, or scary.
[10:59] Still, its decline also serves as a reminder of the challenges in creating practical agentic systems that not only work as intended but do so systematically. In short, LLMs are simply not ready yet for becoming true agents, but it may be the case soon. (The speaker is visible again) For now, as with all things code related, we should always aim to find a solution to our problem that is as simple as possible. (Text: "Find a solution that is as simple as possible" appears) One that we can iterate easily and debug easily. Simple LLM calls are often the way to go, and it is often what people and companies sell as being an agent, but you won't be fooled anymore.
[11:36] You may want to complement LLMs with some external knowledge through the use of retrieval systems or light fine-tuning, but your money and time aiming for true agents should be saved for really complex problems that cannot be solved otherwise. (Text: "Complement LLMs with RAG or fine-tuning", "Save your money and time for complex problems that we can't solve" appears) I hope this video helped you understand the difference between workflows and a real agent and when to use both. (Music starts playing, "SHARE" and "SUBSCRIBED" buttons appear) If you found it useful, please share it with a friend in the AI community and don't forget to subscribe for more in-depth AI content. Thank you for watching.
[12:07] (Social media handles and website link appear: X @whats_ai, www.louisbouchard.ai)
_This video clarifies the distinction between "workflows" and "real agents" in the context of large language models, emphasizing that most current AI applications are workflows while true agents possess independent reasoning and decision-making capabilities, which are still challenging to achieve successfully._

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>A Developer’s Guide to Building Scalable AI: Workflows vs Agents</summary>

# A Developer’s Guide to Building Scalable AI: Workflows vs Agents

**Source URL:** <https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/>

Understanding the architectural trade-offs between autonomous agents and orchestrated workflows — because someone needs to make this decision, and it might as well be you

[Hailey Quach](https://towardsdatascience.com/author/hailey-quach/)

Jun 27, 2025

38 min read

https://towardsdatascience.com/wp-content/uploads/2025/06/agent-vs-workflow.jpegImage by author

There was a time not long ago — okay, like three months ago — when I fell deep into the agent rabbit hole.

I had just started experimenting with CrewAI and LangGraph, and it felt like I’d unlocked a whole new dimension of building. Suddenly, I didn’t just have tools and pipelines — I had _crews_. I could spin up agents that could reason, plan, talk to tools, and talk to each other. Multi-agent systems! Agents that summon other agents! I was practically architecting the AI version of a startup team.

Every use case became a candidate for a crew. Meeting prep? Crew. Slide generation? Crew. Lab report review? Crew.

It was exciting — until it wasn’t.

The more I built, the more I ran into questions I hadn’t thought through: _How do I monitor this? How do I debug a loop where the agent just keeps “thinking”? What happens when something breaks? Can anyone else even maintain this with me?_

That’s when I realized I had skipped a crucial question: _Did this really need to be agentic?_ Or was I just excited to use the shiny new thing?

Since then, I’ve become a lot more cautious — and a lot more practical. Because there’s a big difference (according to [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)) between:

- A **workflow**: a structured LLM pipeline with clear control flow, where you define the steps — use a tool, retrieve context, call the model, handle the output.
- And an **agent**: an autonomous system where the LLM decides what to do next, which tools to use, and when it’s “done.”

Workflows are more like you calling the shots and the LLM following your lead. Agents are more like hiring a brilliant, slightly chaotic intern who figures things out on their own — sometimes beautifully, sometimes in terrifyingly expensive ways.

This article is for anyone who’s ever felt that same temptation to build a multi-agent empire before thinking through what it takes to maintain it. It’s not a warning, it’s a reality check — and a field guide. Because there _are_ times when agents are exactly what you need. But most of the time? You just need a solid workflow.

* * *

## Table of Contents

01. [The State of AI Agents: Everyone’s Doing It, Nobody Knows Why](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i1)
02. [Technical Reality Check: What You’re Actually Choosing Between](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i2)
    - [Workflows: The Reliable Friend Who Shows Up On Time](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i2-2)
    - [Agents: The Smart Kid Who Sometimes Goes Rogue](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i2-1)
03. [The Hidden Costs Nobody Talks About](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i3)
04. [When Agents Actually Make Sense](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i4)
05. [When Workflows Are Obviously Better (But Less Exciting)](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i5)
06. [A Decision Framework That Actually Works](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i6)
    - [The Scoring Process: Because Single-Factor Decisions Are How Projects Die](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i6-1)
07. [The Plot Twist: You Don’t Have to Choose](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i7)
08. [Production Deployment — Where Theory Meets Reality](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i8)
    - [Monitoring (Because “It Works on My Machine” Doesn’t Scale)](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i8-1)
    - [Cost Management (Before Your CFO Stages an Intervention)](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i8-2)
    - [Security (Because Autonomous AI and Security Are Best Friends)](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i8-3)
    - [Testing Methodologies (Because “Trust but Verify” Applies to AI Too)](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i8-4)
09. [The Honest Recommendation](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#i9)
10. [References](https://towardsdatascience.com/a-developers-guide-to-building-scalable-ai-workflows-vs-agents/#ref)

* * *

## The State of AI Agents: Everyone’s Doing It, Nobody Knows Why

You’ve probably seen the stats. [95% of companies are now using generative AI, with 79% specifically implementing AI agents](https://www.bain.com/insights/survey-generative-ai-uptake-is-unprecedented-despite-roadblocks/), according to Bain’s 2024 survey. That sounds impressive — until you look a little closer and find out only _1%_ of them consider those implementations “mature.”

Translation: most teams are duct-taping something together and hoping it doesn’t explode in production.

I say this with love — I was one of them.

There’s this moment when you first build an agent system that works — even a small one — and it _feels like magic_. The LLM decides what to do, picks tools, loops through steps, and comes back with an answer like it just went on a mini journey. You think: “Why would I ever write rigid pipelines again when I can just let the model figure it out?”

And then the complexity creeps in.

You go from a clean pipeline to a network of tool-wielding LLMs reasoning in circles. You start writing logic to correct the logic of the agent. You build an agent to supervise the other agents. Before you know it, you’re maintaining a distributed system of interns with anxiety and no sense of cost.

Yes, there are real success stories. [Klarna’s agent handles the workload of 700 customer service reps](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/). [BCG built a multi-agent design system that cut shipbuilding engineering time by nearly half.](https://www.bcg.com/publications/2025/how-ai-can-be-the-new-all-star-on-your-team) These are not demos — these are production systems, saving companies real time and money.

But those companies didn’t get there by accident. Behind the scenes, they invested in infrastructure, observability, fallback systems, budget controls, and teams who could debug prompt chains at 3 AM without crying.

For most of us? We’re not Klarna. We’re trying to get something working that’s reliable, cost-effective, and doesn’t eat up 20x more tokens than a well-structured pipeline.

So yes, agents _can_ be amazing. But we have to stop pretending they’re a default. Just because the model _can_ decide what to do next doesn’t mean it _should_. Just because the flow is dynamic doesn’t mean the system is smart. And just because everyone’s doing it doesn’t mean you need to follow.

Sometimes, using an agent is like replacing a microwave with a sous chef — more flexible, but also more expensive, harder to manage, and occasionally makes decisions you didn’t ask for.

Let’s figure out when it actually makes sense to go that route — and when you should just stick with something that works.

## Technical Reality Check: What You’re Actually Choosing Between

Before we dive into the existential crisis of choosing between agents and workflows, let’s get our definitions straight. Because in typical tech fashion, everyone uses these terms to mean slightly different things.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-115.pngimage by author

### Workflows: The Reliable Friend Who Shows Up On Time

Workflows are orchestrated. You write the logic: maybe retrieve context with a vector store, call a toolchain, then use the LLM to summarize the results. Each step is explicit. It’s like a recipe. If it breaks, you know exactly where it happened — and probably how to fix it.

This is what most “RAG pipelines” or prompt chains are. Controlled. Testable. Cost-predictable.

The beauty? You can debug them the same way you debug any other software. Stack traces, logs, fallback logic. If the vector search fails, you catch it. If the model response is weird, you reroute it.

Workflows are your dependable friend who shows up on time, sticks to the plan, and doesn’t start rewriting your entire database schema because it felt “inefficient.”

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-112.pngImage by author, inspired by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

In this example of a simple customer support task, this workflow always follows the same classify → route → respond → log pattern. It’s predictable, debuggable, and performs consistently.

```python
def customer_support_workflow(customer_message, customer_id):
    """Predefined workflow with explicit control flow"""

    # Step 1: Classify the message type
    classification_prompt = f"Classify this message: {customer_message}\nOptions: billing, technical, general"
    message_type = llm_call(classification_prompt)

    # Step 2: Route based on classification (explicit paths)
    if message_type == "billing":
        # Get customer billing info
        billing_data = get_customer_billing(customer_id)
        response_prompt = f"Answer this billing question: {customer_message}\nBilling data: {billing_data}"

    elif message_type == "technical":
        # Get product info
        product_data = get_product_info(customer_id)
        response_prompt = f"Answer this technical question: {customer_message}\nProduct info: {product_data}"

    else:  # general
        response_prompt = f"Provide a helpful general response to: {customer_message}"

    # Step 3: Generate response
    response = llm_call(response_prompt)

    # Step 4: Log interaction (explicit)
    log_interaction(customer_id, message_type, response)

    return response
```

The deterministic approach provides:

- **Predictable execution**: Input A always leads to Process B, then Result C
- **Explicit error handling**: “If this breaks, do that specific thing”
- **Transparent debugging**: You can literally trace through the code to find problems
- **Resource optimization**: You know exactly how much everything will cost

[Workflow implementations deliver consistent business value](https://ascendix.com/blog/salesforce-success-stories/): OneUnited Bank achieved 89% credit card conversion rates, while Sequoia Financial Group saved 700 hours annually per user. Not as sexy as “autonomous AI,” but your operations team will love you.

### Agents: The Smart Kid Who Sometimes Goes Rogue

Agents, on the other hand, are built around loops. The LLM gets a goal and starts reasoning about how to achieve it. It picks tools, takes actions, evaluates outcomes, and decides what to do next — all inside a recursive decision-making loop.

This is where things get… fun.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-111.pngImage by author, inspired by [Anthropic](https://www.anthropic.com/engineering/building-effective-agents)

The architecture enables some genuinely impressive capabilities:

- **Dynamic tool selection**: “Should I query the database or call the API? Let me think…”
- **Adaptive reasoning**: Learning from mistakes within the same conversation
- **Self-correction**: “That didn’t work, let me try a different approach”
- **Complex state management**: Keeping track of what happened three steps ago

In the same example, the agent might decide to search the knowledge base first, then get billing info, then ask clarifying questions — all based on its interpretation of the customer’s needs. The execution path varies depending on what the agent discovers during its reasoning process:

```python
def customer_support_agent(customer_message, customer_id):
    """Agent with dynamic tool selection and reasoning"""

    # Available tools for the agent
    tools = {
        "get_billing_info": lambda: get_customer_billing(customer_id),
        "get_product_info": lambda: get_product_info(customer_id),
        "search_knowledge_base": lambda query: search_kb(query),
        "escalate_to_human": lambda: create_escalation(customer_id),
    }

    # Agent prompt with tool descriptions
    agent_prompt = f"""
    You are a customer support agent. Help with this message: "{customer_message}"

    Available tools: {list(tools.keys())}

    Think step by step:
    1. What type of question is this?
    2. What information do I need?
    3. Which tools should I use and in what order?
    4. How should I respond?

    Use tools dynamically based on what you discover.
    """

    # Agent decides what to do (dynamic reasoning)
    agent_response = llm_agent_call(agent_prompt, tools)

    return agent_response
```

Yes, that autonomy is what makes agents powerful. It’s also what makes them hard to control.

Your agent might:

- decide to try a new strategy mid-way
- forget what it already tried
- or call a tool 15 times in a row trying to “figure things out”

You can’t just set a breakpoint and inspect the stack. The “stack” is inside the model’s context window, and the “variables” are fuzzy thoughts shaped by your prompts.

When something goes wrong — and it will — you don’t get a nice red error message. You get a token bill that looks like someone mistyped a loop condition and summoned the OpenAI API 600 times. (I know, because I did this at least once where I forgot to cap the loop, and the agent just kept thinking… and thinking… until the entire system crashed with an “out of token” error).

* * *

To put it in simpler terms, you can think of it like this:

A **workflow** is a GPS.

You know the destination. You follow clear instructions. “Turn left. Merge here. You’ve arrived.” It’s structured, predictable, and you almost always get where you’re going — unless you ignore it on purpose.

An **agent** is different. It’s like handing someone a map, a smartphone, a credit card, and saying:

> “Figure out how to get to the airport. You can walk, call a cab, take a detour if needed — just make it work.”

They might arrive faster. Or they might end up arguing with a rideshare app, taking a scenic detour, and arriving an hour later with a $18 smoothie. (We all know someone like that).

**Both approaches can work**, but the real question is:

> **Do you actually need autonomy here, or just a reliable set of instructions?**

Because here’s the thing — agents _sound_ amazing. And they are, in theory. You’ve probably seen the headlines:

- “Deploy an agent to handle your entire support pipeline!”
- “Let AI manage your tasks while you sleep!”
- “Revolutionary multi-agent systems — your personal consulting firm in the cloud!”

These case studies are everywhere. And some of them are real. But most of them?

They’re like travel photos on Instagram. You see the glowing sunset, the perfect skyline. You don’t see the six hours of layovers, the missed train, the $25 airport sandwich, or the three-day stomach bug from the street tacos.

That’s what agent success stories often leave out: **the operational complexity, the debugging pain, the spiraling token bill**.

So yeah, agents _can_ take you places. But before you hand over the keys, make sure you’re okay with the route they might choose. And that you can afford the tolls.

## The Hidden Costs Nobody Talks About

On paper, agents seem magical. You give them a goal, and they figure out how to achieve it. No need to hardcode control flow. Just define a task and let the system handle the rest.

In theory, it’s elegant. In practice, it’s chaos in a trench coat.

Let’s talk about what it _really_ costs to go agentic — not just in dollars, but in complexity, failure modes, and emotional wear-and-tear on your engineering team.

### Token Costs Multiply — Fast

[According to Anthropic’s research](https://www.anthropic.com/engineering/built-multi-agent-research-system), agents consume 4x more tokens than simple chat interactions. Multi-agent systems? Try 15x more tokens. This isn’t a bug — it’s the whole point. They loop, reason, re-evaluate, and often talk to themselves several times before arriving at a decision.

Here’s how that math breaks down:

- **Basic workflows**: $500/month for 100k interactions
- **Single agent systems**: $2,000/month for the same volume
- **Multi-agent systems**: $7,500/month (assuming $0.005 per 1K tokens)

And that’s if everything is working as intended.

If the agent gets stuck in a tool call loop or misinterprets instructions? You’ll see spikes that make your billing dashboard look like a crypto pump-and-dump chart.

### Debugging Feels Like AI Archaeology

With workflows, debugging is like walking through a well-lit house. You can trace input → function → output. Easy.

With agents? It’s more like wandering through an unmapped forest where the trees occasionally rearrange themselves. You don’t get traditional logs. You get _reasoning traces_, full of model-generated thoughts like:

> “Hmm, that didn’t work. I’ll try another approach.”

That’s not a stack trace. That’s an AI diary entry. It’s poetic, but not helpful when things break in production.

The really “fun” part? **Error propagation in agent systems can cascade in completely unpredictable ways.** One incorrect decision early in the reasoning chain can lead the agent down a rabbit hole of increasingly wrong conclusions, like a game of telephone where each player is also trying to solve a math problem. Traditional debugging approaches — setting breakpoints, tracing execution paths, checking variable states — become much less helpful when the “bug” is that your AI decided to interpret your instructions creatively.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-113.pngImage by author, generated by GPT-4o

### New Failure Modes You’ve Never Had to Think About

[Microsoft’s research has identified](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/) entirely **new failure modes that didn’t exist before agents**. Here are just a few that aren’t common in traditional pipelines:

- **Agent Injection**: Prompt-based exploits that hijack the agent’s reasoning
- **Multi-Agent Jailbreaks**: Agents colluding in unintended ways
- **Memory Poisoning**: One agent corrupts shared memory with hallucinated nonsense

These aren’t edge cases anymore — they’re becoming common enough that entire subfields of “LLMOps” now exist just to handle them.

If your monitoring stack doesn’t track token drift, tool spam, or emergent agent behavior, you’re flying blind.

### You’ll Need Infra You Probably Don’t Have

Agent-based systems don’t just need compute — they need new layers of tooling.

You’ll probably end up cobbling together some combo of:

- **LangFuse**, **Arize**, or **Phoenix** for observability
- **AgentOps** for cost and behavior monitoring
- Custom token guards and fallback strategies to stop runaway loops

This tooling stack _isn’t optional_. It’s required to keep your system stable.

And if you’re not already doing this? You’re not ready for agents in production — at least, not ones that impact real users or money.

* * *

So yeah. It’s not that agents are “bad.” They’re just a lot more expensive — financially, technically, and emotionally — than most people realize when they first start playing with them.

The tricky part is that none of this shows up in the demo. In the demo, it looks clean. Controlled. Impressive.

But in production, things leak. Systems loop. Context windows overflow. And you’re left explaining to your boss why your AI system spent $5,000 calculating the best time to send an email.

## When Agents Actually Make Sense

_\[Before we dive into agent success stories, a quick reality check: these are patterns observed from analyzing current implementations, not universal laws of software architecture. Your mileage may vary, and there are plenty of organizations successfully using workflows for scenarios where agents might theoretically excel. Consider these informed observations rather than divine commandments carved in silicon.\]_

Alright. I’ve thrown a lot of caution tape around agent systems so far — but I’m not here to scare you off forever.

Because sometimes, agents are _exactly_ what you need. They’re brilliant in ways that rigid workflows simply can’t be.

The trick is knowing the difference between “I want to try agents because they’re cool” and “this use case actually needs autonomy.”

Here are a few scenarios where agents genuinely earn their keep.

### Dynamic Conversations With High Stakes

Let’s say you’re building a customer support system. Some queries are straightforward — refund status, password reset, etc. A simple workflow handles those perfectly.

But other conversations? They require adaptation. Back-and-forth reasoning. Real-time prioritization of what to ask next based on what the user says.

That’s where agents shine.

In these contexts, you’re not just filling out a form — you’re navigating a situation. Personalized troubleshooting, product recommendations, contract negotiations — things where the next step depends entirely on what just happened.

Companies implementing agent-based customer support systems have reported wild ROI — we’re talking [112% to 457%](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) increases in efficiency and conversions, depending on the industry. Because when done right, agentic systems _feel_ smarter. And that leads to trust.

### High-Value, Low-Volume Decision-Making

Agents are expensive. But sometimes, the decisions they’re helping with are _more_ expensive.

BCG helped a shipbuilding firm cut 45% of its engineering effort using a multi-agent design system. That’s worth it — because those decisions were tied to multi-million dollar outcomes.

If you’re optimizing how to lay fiber optic cable across a continent or analyzing legal risks in a contract that affects your entire company — burning a few extra dollars on compute isn’t the problem. The _wrong_ decision is.

Agents work here because the _cost of being wrong_ is way higher than the _cost of computing_.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/when-agents-win-683x1024.jpegImage by author

### Open-Ended Research and Exploration

There are problems where you literally can’t define a flowchart upfront — because you don’t know what the “right steps” are.

Agents are great at diving into ambiguous tasks, breaking them down, iterating on what they find, and adapting in real-time.

Think:

- Technical research assistants that read, summarize, and compare papers
- Product analysis bots that explore competitors and synthesize insights
- Research agents that investigate edge cases and suggest hypotheses

These aren’t problems with known procedures. They’re open loops by nature — and agents thrive in those.

### **Multi-Step, Unpredictable Workflows**

Some tasks have too many branches to hardcode — the kind where writing out all the “if this, then that” conditions becomes a full-time job.

This is where agent loops can actually _simplify_ things, because the LLM handles the flow dynamically based on context, not pre-written logic.

Think diagnostics, planning tools, or systems that need to factor in dozens of unpredictable variables.

If your logic tree is starting to look like a spaghetti diagram made by a caffeinated octopus — yeah, maybe it’s time to let the model take the wheel.

* * *

So no, I’m not anti-agent (I actually love them!) I’m pro-alignment — matching the tool to the task.

When the use case _needs_ flexibility, adaptation, and autonomy, then yes — bring in the agents. But only after you’re honest with yourself about whether you’re solving a real complexity… or just chasing a shiny abstraction.

## When Workflows Are Obviously Better (But Less Exciting)

_\[Again, these are observations drawn from industry analysis rather than ironclad rules. There are undoubtedly companies out there successfully using agents for regulated processes or cost-sensitive applications — possibly because they have specific requirements, exceptional expertise, or business models that change the economics. Think of these as strong starting recommendations, not limitations on what’s possible.\]_

Let’s step back for a second.

A lot of AI architecture conversations get stuck in hype loops — “Agents are the future!” “AutoGPT can build companies!” — but in actual production environments, most systems don’t need agents.

They need something that works.

That’s where workflows come in. And while they may not feel as futuristic, they are **incredibly effective** in the environments that most of us are building for.

### Repeatable Operational Tasks

If your use case involves clearly defined steps that rarely change — like sending follow-ups, tagging data, validating form inputs — a workflow will outshine an agent every time.

It’s not just about cost. It’s about stability.

You don’t want creative reasoning in your payroll system. You want the same result, every time, with no surprises. A well-structured pipeline gives you that.

There’s nothing sexy about “process reliability” — until your agent-based system forgets what year it is and flags every employee as a minor.

### Regulated, Auditable Environments

Workflows are deterministic. That means they’re traceable. Which means if something goes wrong, you can show exactly what happened — step-by-step — with logs, fallbacks, and structured output.

If you’re working in healthcare, finance, law, or government — places where **“we think the AI decided to try something new”** is not an acceptable answer — this matters.

You can’t build a safe AI system without transparency. Workflows give you that by default.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/when-workflows-win-683x1024.jpegImage by author

### High-Frequency, Low-Complexity Scenarios

There are entire categories of tasks where the **cost per request** matters more than the sophistication of reasoning. Think:

- Fetching info from a database
- Parsing emails
- Responding to FAQ-style queries

A workflow can handle thousands of these requests per minute, at predictable costs and latency, with zero risk of runaway behavior.

If you’re scaling fast and need to stay lean, a structured pipeline beats a clever agent.

### Startups, MVPs, and Just-Get-It-Done Projects

Agents require infrastructure. Monitoring. Observability. Cost tracking. Prompt architecture. Fallback planning. Memory design.

If you’re not ready to invest in all of that — and most early-stage teams aren’t — agents are probably too much, too soon.

Workflows let you move fast and learn how LLMs behave before you get into recursive reasoning and emergent behavior debugging.

Think of it this way: workflows are how you **get to production**. Agents are how you scale specific use cases once you understand your system deeply.

* * *

One of the best mental models I’ve seen (shoutout to [Anthropic’s engineering blog](https://www.anthropic.com/engineering/building-effective-agents)) is this:

> **Use workflows to build structure around the predictable. Use agents to explore the unpredictable.**

Most real-world AI systems are a mix — and many of them lean heavily on workflows because **production doesn’t reward cleverness**. It rewards **resilience**.

## A Decision Framework That Actually Works

Here’s something I’ve learned (the hard way, of course): most bad architecture decisions don’t come from a lack of knowledge — they come from moving too fast.

You’re in a sync. Someone says, “This feels a bit too dynamic for a workflow — maybe we just go with agents?”

Everyone nods. It sounds reasonable. Agents are flexible, right?

Fast forward three months: the system’s looping in weird places, the logs are unreadable, costs are spiking, and no one remembers who suggested using agents in the first place. You’re just trying to figure out why an LLM decided to summarize a refund request by booking a flight to Peru.

So, let’s slow down for a second.

This isn’t about picking the trendiest option — it’s about building something you can explain, scale, and actually maintain.

The framework below is designed to make you pause and think clearly before the token bills stack up and your nice prototype turns into a very expensive choose-your-own-adventure story.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/Mediamodifier-Design1.svgImage by author

### The Scoring Process: Because Single-Factor Decisions Are How Projects Die

This isn’t a decision tree that bails out at the first “sounds good.” It’s a structured evaluation. You go through **five dimensions**, score each one, and see what the system is really asking for — not just what sounds fun.

**Here’s how it works:**

> - Each dimension gives **+2 points** to either workflow or agents.
> - One question gives **+1 point** (reliability).
> - Add it all up at the end — and trust the result more than your agent hype cravings.

* * *

### Complexity of the Task (2 points)

Evaluate whether your use case has well-defined procedures. Can you write down steps that handle 80% of your scenarios without resorting to hand-waving?

- Yes → +2 for **workflows**
- No, there’s ambiguity or dynamic branching → +2 for **agents**

If your instructions involve phrases like “and then the system figures it out” — you’re probably in agent territory.

### Business Value vs. Volume (2 points)

Assess the cold, hard economics of your use case. Is this a high-volume, cost-sensitive operation — or a low-volume, high-value scenario?

- High-volume and predictable → +2 for **workflows**
- Low-volume but high-impact decisions → +2 for **agents**

Basically: if compute cost is more painful than getting something slightly wrong, workflows win. If being wrong is expensive and being slow loses money, agents might be worth it.

### Reliability Requirements (1 point)

Determine your tolerance for output variability — and be honest about what your business actually needs, not what sounds flexible and modern. How much output variability can your system tolerate?

- Needs to be consistent and traceable (audits, reports, clinical workflows) → +1 for **workflows**
- Can handle some variation (creative tasks, customer support, exploration) → +1 for **agents**

This one’s often overlooked — but it directly affects how much guardrail logic you’ll need to write (and maintain).

### Technical Readiness (2 points)

Evaluate your current capabilities without the rose-colored glasses of “we’ll figure it out later.” What’s your current engineering setup and comfort level?

- You’ve got logging, traditional monitoring, and a dev team that hasn’t yet built agentic infra → +2 for **workflows**
- You already have observability, fallback plans, token tracking, and a team that understands emergent AI behavior → +2 for **agents**

This is your system maturity check. Be honest with yourself. Hope is not a debugging strategy.

### Organizational Maturity (2 points)

Assess your team’s AI expertise with brutal honesty — this isn’t about intelligence, it’s about experience with the specific weirdness of AI systems. How experienced is your team with prompt engineering, tool orchestration, and LLM weirdness?

- Still learning prompt design and LLM behavior → +2 for **workflows**
- Comfortable with distributed systems, LLM loops, and dynamic reasoning → +2 for **agents**

You’re not evaluating intelligence here — just experience with a specific class of problems. Agents demand a deeper familiarity with AI-specific failure patterns.

* * *

### Add Up Your Score

After completing all five evaluations, calculate your total scores.

- **Workflow score ≥ 6** → Stick with workflows. You’ll thank yourself later.
- **Agent score ≥ 6** → Agents might be viable — _if_ there are no workflow-critical blockers.

**Important**: This framework doesn’t tell you what’s coolest. It tells you what’s sustainable.

A lot of use cases will lean workflow-heavy. That’s not because agents are bad — it’s because true agent readiness involves _many_ systems working in harmony: infrastructure, ops maturity, team knowledge, failure handling, and cost controls.

And if any one of those is missing, it’s usually not worth the risk — yet.

## The Plot Twist: You Don’t Have to Choose

Here’s a realization I wish I’d had earlier: you don’t have to pick sides. The magic often comes from **hybrid systems** — where workflows provide stability, and agents offer flexibility. It’s the best of both worlds.

Let’s explore how that actually works.

### Why Hybrid Makes Sense

Think of it as layering:

1.  **Reactive layer** (your workflow): handles predictable, high-volume tasks
2.  **Deliberative layer** (your agent): steps in for complex, ambiguous decisions

This is exactly how many real systems are built. The workflow handles the 80% of predictable work, while the agent jumps in for the 20% that needs creative reasoning or planning

### Building Hybrid Systems Step by Step

Here’s a refined approach I’ve used (and borrowed from hybrid best practices):

1.  **Define the core workflow.**

Map out your predictable tasks — data retrieval, vector search, tool calls, response synthesis.
2.  **Identify decision points.**

Where might you _need_ an agent to decide things dynamically?
3.  **Wrap those steps with lightweight agents.**

Think of them as scoped decision engines — they plan, act, reflect, then return answers to the workflow .
4.  **Use memory and plan loops wisely.**

Give the agent just enough context to make smart choices without letting it go rogue.
5.  **Monitor and fail gracefully.**

If the agent goes wild or costs spike, fall back to a default workflow branch. Keep logs and token meters running.
6.  **Human-in-the-loop checkpoint.**

Especially in regulated or high-stakes flows, pause for human validation before agent-critical actions

### When to Use Hybrid Approach

| Scenario | Why Hybrid Works |
| --- | --- |
| Customer support | Workflow does easy stuff, agents adapt when conversations get messy |
| Content generation | Workflow handles format and publishing; agent writes the body |
| Data analysis/reporting | Agents summarize & interpret; workflows aggregate & deliver |
| High-stakes decisions | Use agent for exploration, workflow for execution and compliance |

When to use hybrid approach

This aligns with how systems like WorkflowGen, n8n, and Anthropic’s own tooling advise building — stable pipelines with scoped autonomy.

### Real Examples: Hybrid in Action

#### A Minimal Hybrid Example

Here’s a scenario I used with LangChain and LangGraph:

-   **Workflow stage**: fetch support tickets, embed & search
-   **Agent cell**: decide whether it’s a refund question, a complaint, or a bug report
-   **Workflow**: run the correct branch based on agent’s tag
-   **Agent stage**: if it’s a complaint, summarize sentiment and suggest next steps
-   **Workflow**: format and send response; log everything

The result? Most tickets flow through without agents, saving cost and complexity. But when ambiguity hits, the agent steps in and adds real value. No runaway token bills. Clear traceability. Automatic fallbacks.

This pattern splits the logic between a structured workflow and a scoped agent. ( **Note: this is a high-level demonstration**)

```python
from langchain.chat_models import init_chat_model
from langchain_community.vectorstores.faiss import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults

# 1. Workflow: set up RAG pipeline
embeddings = OpenAIEmbeddings()
vectordb = FAISS.load_local(
    "docs_index",
    embeddings,
    allow_dangerous_deserialization=True
)
retriever = vectordb.as_retriever()

system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentences maximum and keep the answer concise.\n\n"
    "Context: {context}"
)
prompt = ChatPromptTemplate.from_messages([\
    ("system", system_prompt),\
    ("human", "{input}"),\
])

llm = init_chat_model("openai:gpt-4.1", temperature=0)
qa_chain = create_retrieval_chain(
    retriever,
    create_stuff_documents_chain(llm, prompt)
)

# 2. Agent: Set up agent with Tavily search
search = TavilySearchResults(max_results=2)
agent_llm = init_chat_model("anthropic:claude-3-7-sonnet-latest", temperature=0)
agent = create_react_agent(
    model=agent_llm,
    tools=[search]
)

# Uncertainty heuristic
def is_answer_uncertain(answer: str) -> bool:
    keywords = [\
        "i don't know", "i'm not sure", "unclear",\
        "unable to answer", "insufficient information",\
        "no information", "cannot determine"\
    ]
    return any(k in answer.lower() for k in keywords)

def hybrid_pipeline(query: str) -> str:
    # RAG attempt
    rag_out = qa_chain.invoke({"input": query})
    rag_answer = rag_out.get("answer", "")

    if is_answer_uncertain(rag_answer):
        # Fallback to agent search
        agent_out = agent.invoke({
            "messages": [{"role": "user", "content": query}]
        })
        return agent_out["messages"][-1].content

    return rag_answer

if __name__ == "__main__":
    result = hybrid_pipeline("What are the latest developments in AI?")
    print(result)
```

**What’s happening here:**

-   The workflow takes the first shot.
-   If the result seems weak or uncertain, the agent takes over.
-   You only pay the agent cost when you really need to.

Simple. Controlled. Scalable.

#### Advanced: Workflow-Controlled Multi-Agent Execution

If your problem _really_ calls for multiple agents — say, in a research or planning task — structure the system as a **graph**, not a soup of recursive loops. ( **Note: this is a high level demonstration**)

```python
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import ToolNode
from langchain_core.messages import AnyMessage

# 1. Define your graph's state
class TaskState(TypedDict):
    input: str
    label: str
    output: str

# 2. Build the graph
graph = StateGraph(TaskState)

# 3. Add your classifier node
def classify(state: TaskState) -> TaskState:
    # example stub:
    state["label"] = "research" if "latest" in state["input"] else "summary"
    return state

graph.add_node("classify", classify)
graph.add_edge(START, "classify")

# 4. Define conditional transitions out of the classifier node
graph.add_conditional_edges(
    "classify",
    lambda s: s["label"],
    path_map={"research": "research_agent", "summary": "summarizer_agent"}
)

# 5. Define the agent nodes
research_agent = ToolNode([create_react_agent(...tools...)])
summarizer_agent = ToolNode([create_react_agent(...tools...)])

# 6. Add the agent nodes to the graph
graph.add_node("research_agent", research_agent)
graph.add_node("summarizer_agent", summarizer_agent)

# 7. Add edges. Each agent node leads directly to END, terminating the workflow
graph.add_edge("research_agent", END)
graph.add_edge("summarizer_agent", END)

# 8. Compile and run the graph
app = graph.compile()
final = app.invoke({"input": "What are today's AI headlines?", "label": "", "output": ""})
print(final["output"])
```

This pattern gives you:

-   **Workflow-level control** over routing and memory
-   **Agent-level reasoning** where appropriate
-   **Bounded loops** instead of infinite agent recursion

This is how tools like LangGraph are designed to work: **structured autonomy**, not free-for-all reasoning.

## Production Deployment — Where Theory Meets Reality

All the architecture diagrams, decision trees, and whiteboard debates in the world won’t save you if your AI system falls apart the moment real users start using it.

Because that’s where things get messy — the inputs are noisy, the edge cases are endless, and users have a magical ability to break things in ways you never imagined. Production traffic has a personality. It will test your system in ways your dev environment never could.

And that’s where most AI projects stumble.

The demo works. The prototype impresses the stakeholders. But then you go live — and suddenly the model starts hallucinating customer names, your token usage spikes without explanation, and you’re ankle-deep in logs trying to figure out why everything broke at 3:17 a.m. (True story!)

This is the gap between a cool proof-of-concept and a system that actually holds up in the wild. It’s also where the difference between workflows and agents stops being philosophical and starts becoming very, very operational.

Whether you’re using agents, workflows, or some hybrid in between — once you’re in production, it’s a different game.

You’re no longer trying to prove that the AI _can_ work.

You’re trying to make sure it works **reliably, affordably, and safely** — every time.

So what does that actually take?

Let’s break it down.

### Monitoring (Because “It Works on My Machine” Doesn’t Scale)

Monitoring an agent system isn’t just “nice to have” — it’s survival gear.

You can’t treat agents like regular apps. Traditional APM tools won’t tell you why an LLM decided to loop through a tool call 14 times or why it burned 10,000 tokens to summarize a paragraph.

You need observability tools that speak the agent’s language. That means tracking:

-   token usage patterns,
-   tool call frequency,
-   response latency distributions,
-   task completion outcomes,
-   and cost per interaction — **in real time**.

This is where tools like **LangFuse**, **AgentOps**, and **Arize Phoenix** come in. They let you peek into the black box — see what decisions the agent is making, how often it’s retrying things, and what’s going off the rails before your budget does.

Because when something breaks, “the AI made a weird choice” is not a helpful bug report. You need traceable reasoning paths and usage logs — not just vibes and token explosions.

Workflows, by comparison, are way easier to monitor.

You’ve got:

-   response times,
-   error rates,
-   CPU/memory usage,
-   and request throughput.

All the usual stuff you already track with your standard APM stack — Datadog, Grafana, Prometheus, whatever. No surprises. No loops trying to plan their next move. Just clean, predictable execution paths.

So yes — both need monitoring. But agent systems demand a whole new layer of visibility. If you’re not prepared for that, production will make sure you learn it the hard way.

https://contributor.insightmediagroup.io/wp-content/uploads/2025/06/image-116.pngImage by author

### Cost Management (Before Your CFO Stages an Intervention)

Token consumption in production can spiral out of control faster than you can say “autonomous reasoning.”

It starts small — a few extra tool calls here, a retry loop there — and before you know it, you’ve burned through half your monthly budget debugging a single conversation. Especially with agent systems, costs don’t just add up — they compound.

That’s why smart teams treat **cost management like infrastructure**, not an afterthought.

Some common (and necessary) strategies:

-   **Dynamic model routing** — Use lightweight models for simple tasks, save the expensive ones for when it actually matters.
-   **Caching** — If the same question comes up a hundred times, you shouldn’t pay to answer it a hundred times.
-   **Spending alerts** — Automated flags when usage gets weird, so you don’t learn about the problem from your CFO.

With agents, this matters even more.

Because once you hand over control to a reasoning loop, you lose visibility into how many steps it’ll take, how many tools it’ll call, and how long it’ll “think” before returning an answer.

If you don’t have real-time cost tracking, per-agent budget limits, and graceful fallback paths — you’re just one prompt away from a very expensive mistake.

Agents are smart. But they’re not cheap. Plan accordingly.

Workflows need cost management too.

If you’re calling an LLM for every user request, especially with retrieval, summarization, and chaining steps — the numbers add up. And if you’re using GPT-4 everywhere out of convenience? You’ll feel it on the invoice.

But workflows are _predictable_. You know how many calls you’re making. You can precompute, batch, cache, or swap in smaller models without disrupting logic. Cost scales linearly — and predictably.

### Security (Because Autonomous AI and Security Are Best Friends)

AI security isn’t just about guarding endpoints anymore — it’s about preparing for systems that can make their own decisions.

That’s where the concept of **shifting left** comes in — bringing security earlier into your development lifecycle.

> Instead of bolting on security after your app “works,” shift-left means designing with security from day one: during prompt design, tool configuration, and pipeline setup.

With **agent-based systems**, you’re not just securing a predictable app. You’re securing something that can autonomously decide to call an API, access private data, or trigger an external action — often in ways you didn’t explicitly program. That’s a very different threat surface.

This means your security strategy needs to evolve. You’ll need:

-   **Role-based access control** for every tool an agent can access
-   **Least privilege enforcement** for external API calls
-   **Audit trails** to capture every step in the agent’s reasoning and behavior
-   **Threat modeling** for novel attacks like prompt injection, agent impersonation, and collaborative jailbreaking (yes, that’s a thing now)

Most traditional app security frameworks assume the code defines the behavior. But with agents, the behavior is dynamic, shaped by prompts, tools, and user input. If you’re building with autonomy, you need **security controls designed for unpredictability**.

* * *

But what about **workflows**?

They’re easier — but not risk-free.

Workflows are deterministic. You define the path, you control the tools, and there’s no decision-making loop that can go rogue. That makes security simpler and more testable — especially in environments where compliance and auditability matter.

Still, workflows touch sensitive data, integrate with third-party services, and output user-facing results. Which means:

-   Prompt injection is still a concern
-   Output sanitation is still essential
-   API keys, database access, and PII handling still need protection

For workflows, “shifting left” means:

-   Validating input/output formats early
-   Running prompt tests for injection risk
-   Limiting what each component can access, even if it “seems safe”
-   Automating red-teaming and fuzz testing around user inputs

It’s not about paranoia — it’s about protecting your system before things go live and real users start throwing unexpected inputs at it.

* * *

Whether you’re building agents, workflows, or hybrids, the rule is the same:

> **If your system can generate actions or outputs, it can be exploited.**

So build like someone _will_ try to break it — because eventually, someone probably will.

### Testing Methodologies (Because “Trust but Verify” Applies to AI Too)

Testing production AI systems is like quality-checking a very smart but slightly unpredictable intern.

They mean well. They usually get it right. But every now and then, they surprise you — and not always in a good way.

That’s why you need **layers of testing**, especially when dealing with agents.

For **agent systems**, a single bug in reasoning can trigger a whole chain of weird decisions. One wrong judgment early on can snowball into broken tool calls, hallucinated outputs, or even data exposure. And because the logic lives inside a prompt, not a static flowchart, you can’t always catch these issues with traditional test cases.

A solid testing strategy usually includes:

-   **Sandbox environments** with carefully designed mock data to stress-test edge cases
-   **Staged deployments** with limited real data to monitor behavior before full rollout
-   **Automated regression tests** to check for unexpected changes in output between model versions
-   **Human-in-the-loop reviews** — because some things, like tone or domain nuance, still need human judgment

For agents, this isn’t optional. It’s the only way to stay ahead of unpredictable behavior.

* * *

But what about **workflows**?

They’re easier to test — and honestly, that’s one of their biggest strengths.

Because workflows follow a deterministic path, you can:

-   Write unit tests for each function or tool call
-   Mock external services cleanly
-   Snapshot expected inputs/outputs and test for consistency
-   Validate edge cases without worrying about recursive reasoning or planning loops

You still want to test prompts, guard against prompt injection, and monitor outputs — but the surface area is smaller, and the behavior is traceable. You know what happens when Step 3 fails, because you wrote Step 4.

**Workflows don’t remove the need for testing — they make it testable.**

That’s a big deal when you’re trying to ship something that won’t fall apart the moment it hits real-world data.

## The Honest Recommendation: Start Simple, Scale Intentionally

If you’ve made it this far, you’re probably not looking for hype — you’re looking for a system that actually works.

So here’s the honest, slightly unsexy advice:

> **Start with workflows. Add agents only when you can clearly justify the need.**

Workflows may not feel revolutionary, but they are reliable, testable, explainable, and cost-predictable. They teach you how your system behaves in production. They give you logs, fallback paths, and structure. And most importantly: **they scale.**

That’s not a limitation. That’s maturity.

It’s like learning to cook. You don’t start with molecular gastronomy — you start by learning how to not burn rice. Workflows are your rice. Agents are the foam.

And when you do run into a problem that actually _needs_ dynamic planning, flexible reasoning, or autonomous decision-making — you’ll know. It won’t be because a tweet told you agents are the future. It’ll be because you hit a wall workflows can’t cross. And at that point, you’ll be ready for agents — and your infrastructure will be, too.

Look at the Mayo Clinic. [They run **14 algorithms on every ECG**](https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-launches-new-technology-platform-ventures-to-revolutionize-diagnostic-medicine/#:~:text=Mayo%20Clinic%20and%20AI%2Ddriven%20health%20technology%20company,to%20Mayo%27s%20deep%20repository%20of%20medical%20data.)— not because it’s trendy, but because it improves diagnostic accuracy at scale. Or take [Kaiser Permanente](https://healthinnovation.ucsd.edu/news/11-health-systems-leading-in-ai), which says its AI-powered clinical support systems have helped save _hundreds of lives each year_.

These aren’t tech demos built to impress investors. These are real systems, in production, handling millions of cases — quietly, reliably, and with huge impact.

The secret? It’s not about choosing agents or workflows.

It’s about understanding the problem deeply, picking the right tools deliberately, and building for resilience — not for flash.

Because in the real world, value comes from what works.

Not what wows.

* * *

**Now go forth and make informed architectural decisions.** The world has enough AI demos that work in controlled environments. What we need are AI systems that work in the messy reality of production — regardless of whether they’re “cool” enough to get upvotes on Reddit.

* * *

## References

01. Anthropic. (2024). _Building effective agents_. [https://www.anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
02. Anthropic. (2024). _How we built our multi-agent research system_. [https://www.anthropic.com/engineering/built-multi-agent-research-system](https://www.anthropic.com/engineering/built-multi-agent-research-system)
03. Ascendix. (2024). _Salesforce success stories: From vision to victory_. [https://ascendix.com/blog/salesforce-success-stories/](https://ascendix.com/blog/salesforce-success-stories/)
04. Bain & Company. (2024). _Survey: Generative AI’s uptake is unprecedented despite roadblocks_. [https://www.bain.com/insights/survey-generative-ai-uptake-is-unprecedented-despite-roadblocks/](https://www.bain.com/insights/survey-generative-ai-uptake-is-unprecedented-despite-roadblocks/)
05. BCG Global. (2025). _How AI can be the new all-star on your team_. [https://www.bcg.com/publications/2025/how-ai-can-be-the-new-all-star-on-your-team](https://www.bcg.com/publications/2025/how-ai-can-be-the-new-all-star-on-your-team)
06. DigitalOcean. (2025). _7 types of AI agents to automate your workflows in 2025_. [https://www.digitalocean.com/resources/articles/types-of-ai-agents](https://www.digitalocean.com/resources/articles/types-of-ai-agents)
07. Klarna. (2024). _Klarna AI assistant handles two-thirds of customer service chats in its first month_ \[Press release\]. [https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/](https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/)
08. Mayo Clinic. (2024). _Mayo Clinic launches new technology platform ventures to revolutionize diagnostic medicine_. [https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-launches-new-technology-platform-ventures-to-revolutionize-diagnostic-medicine/](https://newsnetwork.mayoclinic.org/discussion/mayo-clinic-launches-new-technology-platform-ventures-to-revolutionize-diagnostic-medicine/)
09. McKinsey & Company. (2024). _The state of AI: How organizations are rewiring to capture value_. [https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
10. Microsoft. (2025, April 24). _New whitepaper outlines the taxonomy of failure modes in AI agents_ \[Blog post\]. [https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents/)
11. UCSD Center for Health Innovation. (2024). _11 health systems leading in AI_. [https://healthinnovation.ucsd.edu/news/11-health-systems-leading-in-ai](https://healthinnovation.ucsd.edu/news/11-health-systems-leading-in-ai)
12. Yoon, J., Kim, S., & Lee, M. (2023). Revolutionizing healthcare: The role of artificial intelligence in clinical practice. _BMC Medical Education_, 23, Article 698. [https://bmcmededuc.biomedcentral.com/articles/10.1186/s12909-023-04698-z](https://bmcmededuc.biomedcentral.com/articles/10.1186/s12909-023-04698-z)

* * *

## Other Sources

- [601 real-world gen AI use cases from the world's leading organizations](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders)
- [Stop Building AI Agents: Here’s what you should build instead](https://decodingml.substack.com/p/stop-building-ai-agents)
- [Andrej Karpathy: Software Is Changing (Again)](https://www.youtube.com/watch?v=LCEmiRjPEtQ)
- [Building Production-Ready RAG Applications: Jerry Liu](https://www.youtube.com/watch?v=TRjq7t2Ms5I)
- [Gemini CLI: your open-source AI agent](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [Gemini CLI README.md](https://github.com/google-gemini/gemini-cli/blob/main/README.md)
- [Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)
- [Introducing ChatGPT agent: bridging research and action](https://openai.com/index/introducing-chatgpt-agent/)

* * *

Written By

Hailey Quach

</details>

<details>
<summary>Building effective agents</summary>

# Building effective agents

**Source URL:** <https://www.anthropic.com/engineering/building-effective-agents>

Published Dec 19, 2024

We've worked with dozens of teams building LLM agents across industries. Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks.

Over the past year, we've worked with dozens of teams building large language model (LLM) agents across industries. Consistently, the most successful implementations weren't using complex frameworks or specialized libraries. Instead, they were building with simple, composable patterns.

In this post, we share what we’ve learned from working with our customers and building agents ourselves, and give practical advice for developers on building effective agents.

## What are agents?

"Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:

- **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
- **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

Below, we will explore both types of agentic systems in detail. In Appendix 1 (“Agents in Practice”), we describe two domains where customers have found particular value in using these kinds of systems.

## When (and when not) to use agents

When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale. For many applications, however, optimizing single LLM calls with retrieval and in-context examples is usually enough.

## When and how to use frameworks

There are many frameworks that make agentic systems easier to implement, including:

- The [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/overview);
- [Strands Agents SDK by AWS](https://strandsagents.com/latest/);
- [Rivet](https://rivet.ironcladapp.com/), a drag and drop GUI LLM workflow builder; and
- [Vellum](https://www.vellum.ai/), another GUI tool for building and testing complex workflows.

These frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. However, they often create extra layers of abstraction that can obscure the underlying prompts ​​and responses, making them harder to debug. They can also make it tempting to add complexity when a simpler setup would suffice.

We suggest that developers start by using LLM APIs directly: many patterns can be implemented in a few lines of code. If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

See our [cookbook](https://platform.claude.com/cookbook/patterns-agents-basic-workflows) for some sample implementations.

## Building blocks, workflows, and agents

In this section, we’ll explore the common patterns for agentic systems we’ve seen in production. We'll start with our foundational building block—the augmented LLM—and progressively increase complexity, from simple compositional workflows to autonomous agents.

### Building block: The augmented LLM

The basic building block of agentic systems is an LLM enhanced with augmentations such as retrieval, tools, and memory. Our current models can actively use these capabilities—generating their own search queries, selecting appropriate tools, and determining what information to retain.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png&w=3840&q=75
The augmented LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75
The prompt chaining workflow

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75
The routing workflow

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75
The parallelization workflow

**When to use this workflow:** Parallelization is effective when the divided subtasks can be parallelized for speed, or when multiple perspectives or attempts are needed for higher confidence results. For complex tasks with multiple considerations, LLMs generally perform better when each consideration is handled by a separate LLM call, allowing focused attention on each specific aspect.

**Examples where parallelization is useful:**

- **Sectioning**:
  - Implementing guardrails where one model instance processes user queries while another screens them for inappropriate content or requests. This tends to perform better than having the same LLM call handle both guardrails and the core response.
  - Automating evals for evaluating LLM performance, where each LLM call evaluates a different aspect of the model’s performance on a given prompt.
- **Voting**:
  - Reviewing a piece of code for vulnerabilities, where several different prompts review and flag the code if they find a problem.
  - Evaluating whether a given piece of content is inappropriate, with multiple prompts evaluating different aspects or requiring different vote thresholds to balance false positives and negatives.

### Workflow: Orchestrator-workers

In the orchestrator-workers workflow, a central LLM dynamically breaks down tasks, delegates them to worker LLMs, and synthesizes their results.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75
The orchestrator-workers workflow

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75
The evaluator-optimizer workflow

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75
Autonomous agent

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75
High-level flow of a coding agent

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1.  Maintain **simplicity** in your agent's design.
2.  Prioritize **transparency** by explicitly showing the agent’s planning steps.
3.  Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

Frameworks can help you get started quickly, but don't hesitate to reduce abstraction layers and build with basic components as you move to production. By following these principles, you can create agents that are not only powerful but also reliable, maintainable, and trusted by their users.

### Acknowledgements

Written by Erik S. and Barry Zhang. This work draws upon our experiences building agents at Anthropic and the valuable insights shared by our customers, for which we're deeply grateful.

## Appendix 1: Agents in practice

Our work with customers has revealed two particularly promising applications for AI agents that demonstrate the practical value of the patterns discussed above. Both applications illustrate how agents add the most value for tasks that require both conversation and action, have clear success criteria, enable feedback loops, and integrate meaningful human oversight.

### A. Customer support

Customer support combines familiar chatbot interfaces with enhanced capabilities through tool integration. This is a natural fit for more open-ended agents because:

- Support interactions naturally follow a conversation flow while requiring access to external information and actions;
- Tools can be integrated to pull customer data, order history, and knowledge base articles;
- Actions such as issuing refunds or updating tickets can be handled programmatically; and
- Success can be clearly measured through user-defined resolutions.

Several companies have demonstrated the viability of this approach through usage-based pricing models that charge only for successful resolutions, showing confidence in their agents' effectiveness.

### B. Coding agents

The software development space has shown remarkable potential for LLM features, with capabilities evolving from code completion to autonomous problem-solving. Agents are particularly effective because:

- Code solutions are verifiable through automated tests;
- Agents can iterate on solutions using test results as feedback;
- The problem space is well-defined and structured; and
- Output quality can be measured objectively.

In our own implementation, agents can now solve real GitHub issues in the [SWE-bench Verified](https://www.anthropic.com/research/swe-bench-sonnet) benchmark based on the pull request description alone. However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements.

## Appendix 2: Prompt engineering your tools

No matter which agentic system you're building, tools will likely be an important part of your agent. [Tools](https://www.anthropic.com/news/tool-use-ga) enable Claude to interact with external services and APIs by specifying their exact structure and definition in our API. When Claude responds, it will include a [tool use block](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#example-api-response-with-a-tool-use-content-block) in the API response if it plans to invoke a tool. Tool definitions and specifications should be given just as much prompt engineering attention as your overall prompts. In this brief appendix, we describe how to prompt engineer your tools.

There are often several ways to specify the same action. For instance, you can specify a file edit by writing a diff, or by rewriting the entire file. For structured output, you can return code inside markdown or inside JSON. In software engineering, differences like these are cosmetic and can be converted losslessly from one to the other. However, some formats are much more difficult for an LLM to write than others. Writing a diff requires knowing how many lines are changing in the chunk header before the new code is written. Writing code inside JSON (compared to markdown) requires extra escaping of newlines and quotes.

Our suggestions for deciding on tool formats are the following:

- Give the model enough tokens to "think" before it writes itself into a corner.
- Keep the format close to what the model has seen naturally occurring in text on the internet.
- Make sure there's no formatting "overhead" such as having to keep an accurate count of thousands of lines of code, or string-escaping any code it writes.

One rule of thumb is to think about how much effort goes into human-computer interfaces (HCI), and plan to invest just as much effort in creating good _agent_-computer interfaces (ACI). Here are some thoughts on how to do so:

- Put yourself in the model's shoes. Is it obvious how to use this tool, based on the description and parameters, or would you need to think carefully about it? If so, then it’s probably also true for the model. A good tool definition often includes example usage, edge cases, input format requirements, and clear boundaries from other tools.
- How can you change parameter names or descriptions to make things more obvious? Think of this as writing a great docstring for a junior developer on your team. This is especially important when using many similar tools.
- Test how the model uses your tools: Run many example inputs in our [workbench](https://console.anthropic.com/workbench) to see what mistakes the model makes, and iterate.
- [Poka-yoke](https://en.wikipedia.org/wiki/Poka-yoke) your tools. Change the arguments so that it is harder to make mistakes.

While building our agent for [SWE-bench](https://www.anthropic.com/research/swe-bench-sonnet), we actually spent more time optimizing our tools than the overall prompt. For example, we found that the model would make mistakes with tools using relative filepaths after the agent had moved out of the root directory. To fix this, we changed the tool to always require absolute filepaths—and we found that the model used this method flawlessly.

</details>

<details>
<summary>Exploring the difference between agents and workflows</summary>

# Exploring the difference between agents and workflows

**Source URL:** <https://decodingml.substack.com/p/llmops-for-production-agentic-rag>

LLM-powered agents combine a **language model, tools, and memory** to process information and take action.

They don’t just generate text—they **reason, retrieve data, and interact with external systems** to complete tasks.

At its core, an agent takes in an input, analyzes what needs to be done, and decides the best way to respond. Instead of working in isolation, it can tap into external tools like APIs, databases, or plugins to enhance its capabilities.

With the reasoning power of LLMs, the agent doesn’t just react—it strategizes. It breaks down the task, plans the necessary steps, and takes action to get the job done efficiently.

[https://substackcdn.com/image/fetch/$s_!gLNT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67ffe267-55f2-4af7-9910-7410c7605550_1220x754.png](https://substackcdn.com/image/fetch/$s_!gLNT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F67ffe267-55f2-4af7-9910-7410c7605550_1220x754.png) Figure 1: The components of an LLM-powered agent

The most popular way to design agents is by using the ReAct framework, which models the agent as follows:

- **act:** the LLM calls specific tools
- **observe:** pass the tool output back to the LLM
- **reason:** the LLM reason about the tool output to decide what to do next (e.g., call another tool or respond directly)

Now, let’s understand how agents and RAG fit together.

Unlike a traditional RAG setup's linear, step-by-step nature, Agentic RAG puts an agent at the center of decision-making.

Instead of passively retrieving and generating responses,the agent actively directs the process—deciding what to search for, how to refine queries, and when to use external tools, such as SQL, vector, or graph databases.

[https://substackcdn.com/image/fetch/$s_!ZnV_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c59d9df-d60f-47bc-81de-cfd4fdebf5f8_1210x704.png](https://substackcdn.com/image/fetch/$s_!ZnV_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c59d9df-d60f-47bc-81de-cfd4fdebf5f8_1210x704.png) Figure 2: The single-agent RAG system architecture

For example, instead of querying the vector database just once (what we usually do in a standard RAG workflow), the agent might decide that after its first query, it doesn’t have enough information to provide an answer, making another request to the vector database with a different query.

Now that we’ve explored LLM-powered agents and Agentic RAGs, let’s take a step back and look at a broader question: “ **How do agents differ from workflows?”** While both help automate tasks, they operate in fundamentally different ways.

A workflow follows a fixed, predefined sequence—every step is planned in advance, making it reliable but rigid (more similar to classic programming).

In contrast, an agent **dynamically decides** what to do next **based on reasoning,** memory, and available tools. Instead of just executing steps, it adapts, learns, and makes decisions on the fly.

Think of a workflow as an assembly line, executing tasks in order, while an agent is like an intelligent assistant, capable of adjusting its approach in real time. This flexibility makes agents powerful for handling unstructured, complex problems that require dynamic decision-making.

[https://substackcdn.com/image/fetch/$s_!yBni!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e64d5e0-7ef1-4e7f-b441-3bf1fef4ff9a_1276x818.png](https://substackcdn.com/image/fetch/$s_!yBni!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e64d5e0-7ef1-4e7f-b441-3bf1fef4ff9a_1276x818.png) Figure 3: Differences between workflows and agents

Therefore, the trade-off between reliability and adaptability is key—workflows offer stability but are rigid, while agents provide flexibility by making dynamic decisions at the cost of consistency.

Now that we understand the basics of working with agents, let’s dive into the architecture of our Second Brain agent.

When architecting the Agentic RAG module, the goal is to build an intelligent system that efficiently combines retrieval, reasoning, and summarization to generate high-quality responses tailored to user queries.

#### What’s the interface of the pipeline?

The pipeline takes a user query as input (submitted through the Gradio UI).

The output is a refined answer generated by the agent after reasoning, retrieving relevant context from **[MongoDB](https://www.mongodb.com/products/platform/atlas-vector-search?utm_campaign=ai-pilot&utm_medium=creator&utm_term=iusztin&utm_source=blog)** through semantic search, and processing it through the summarization tool.

#### Offline vs. online pipelines

The Agentic RAG module fundamentally differs from the offline ML pipelines we’ve built in previous lessons.

This module is entirely decoupled from the pipelines in Lessons 1-5. It lives in a separate **[second-brain-online](https://github.com/decodingml/second-brain-ai-assistant-course/tree/main/apps/second-brain-online)** folder within our repository as its own standalone Python application.

This separation is intentional—by keeping the offline pipelines (feature and training) fully independent from the online inference system, we ensure a clean architectural divide.

As a quick reminder from Lesson 1, **offline pipelines** are batch pipelines that run on a schedule or trigger. They process input data and store the output artifacts in storage, allowing other pipelines or clients to consume them as needed.

These include the data collection pipeline, ETL pipeline, RAG feature pipeline, dataset generation pipeline, and training pipeline. They operate independently and are decoupled through various storage solutions such as document databases, vector databases, data registries, or model registries.

The Agentic RAG module, on the other hand, belongs to the category of **online pipelines**. It directly interacts with the user and must remain available at all times. The online pipelines available in this project are the agentic inference pipeline, the summarization inference pipeline, and the observability pipeline.

Unlike offline pipelines, these do not require orchestration and function similarly to RESTful APIs, ensuring minimal latency and efficient responses.

#### What does the pipeline’s architecture look like?

The Agentic RAG module operates in real time, instantly responding to user queries without redundant processing.

This module's core is an agent-driven system that reasons independently and dynamically invokes tools to handle user queries. They serve as extensions of the LLM model powering the agent, allowing it to perform tasks it wouldn’t efficiently handle on its own without specialized fine-tuning.

Our agent relies on three main components:

1. **The what can I do tool**, which helps users understand the usages of the system
2. **The retriever tool** that queries MongoDB’s vector index pre-populated during our offline processing
3. **The summarization tool** uses a REST API to call a different model specialized in summarizing web documents.

We specifically picked these ones as they are a perfect use case for showing how to use a tool that runs only with Python, one that calls a database, and one that calls an API (three of the most common scenarios).

The agent layer is powered by the **[SmolAgents](https://github.com/huggingface/smolagents)** framework (by Hugging Face) and orchestrates the reasoning process. A maximum number of steps can be set to ensure the reasoning remains focused and does not take unnecessary iterations to reach a response (avoiding skyrocketing bills).

To provide a seamless user experience, we integrated the agentic inference pipeline with a **[Gradio UI](https://www.gradio.app/)**, making interactions intuitive and accessible. This setup ensures that users can engage with the assistant as naturally as possible, simulating a conversational AI experience.

The interface allows us to track how the agent selects and uses tools during interactions.

For instance, we can see when it calls the **[MongoDB vector search tool](https://www.mongodb.com/products/platform/atlas-vector-search?utm_campaign=ai-pilot&utm_medium=creator&utm_term=iusztin&utm_source=blog)** to retrieve relevant data and how it cycles between retrieving information and reasoning before generating a response.

[https://substackcdn.com/image/fetch/$s_!bqEU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb30a1f89-0c60-4a28-b87a-5390262f1500_1170x1065.png](https://substackcdn.com/image/fetch/$s_!bqEU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb30a1f89-0c60-4a28-b87a-5390262f1500_1170x1065.png) Figure 4: The architecture of the Agentic RAG module

The agentic inference pipeline is designed to handle user queries in real time, orchestrating a seamless data flow from input to response. To understand how information moves through the system, we break down the interaction between the user, the retrieval process, and the summarization mechanism.

When a user submits a query through the **Gradio UI**, the **Agentic Layer**, an LLM-powered agent, dynamically determines the most suitable tool to process the request.

If additional context is required, the **Retriever Tool** fetches relevant information from the MongoDB vector database, extracting the most relevant chunks. This vector database was previously populated through the RAG feature pipeline in Lesson 5, ensuring the system has preprocessed, structured knowledge readily available for retrieval.

The retrieved data is then refined using the **Summarization Tool**, which enhances clarity before generating the final response. For summarization, we can choose between a custom Summarization Inference Pipeline, which is powered by the Hugging Face model we trained in Lesson 4, or an OpenAI model.

The agent continues reasoning iteratively until it reaches the predefined step limit or it decides it has the final answer, ensuring efficiency while maintaining high response quality.

As a side note, given the simplicity of our use case, the Second Brain AI assistant could have been implemented using a traditional workflow, directly retrieving and responding to queries without an agentic approach.

However, by embracing this modular strategy, we achieve greater scalability and flexibility, allowing the system to integrate new data sources or tools easily in the future.

Now that we understand how the agent works, let’s dig into how we can evaluate it and then into the implementation.

When evaluating an Agentic RAG application, it’s important to distinguish between two primary evaluation approaches: **LLM evaluation** and **Application/RAG evaluation**. Each serves a different purpose, and while LLM evaluation assesses the model in isolation, Application/RAG evaluation tests the entire application as a system.

In this case, our primary focus is evaluating the RAG pipeline as a black-box system, assessing how retrieval and reasoning work together to generate the final output.

However, we also provide a brief refresher on key insights from LLM evaluation in Lesson 4 to highlight its role in the broader evaluation process.

#### LLM evaluation

As a brief reminder, LLM evaluation measures response quality without retrieval. In Lesson 4, we tested this by analyzing the model’s ability to generate answers from its internal knowledge.

Popular methods for LLM evaluation include **benchmark-based evaluation** (using standardized datasets), **heuristic evaluation**(ROUGE, BLEU, regex matching, or custom heuristics), semantic-based evaluation (BERT Score), and **LLM-as-a-judge**, where another LLM evaluates the generated outputs.

Each method has strengths and trade-offs. Benchmark-based evaluation provides standardized comparisons but may not fully capture real-world performance, while heuristic methods may offer quick, interpretable insights but often fail to assess deeper contextual understanding. Additionally, LLM-as-a-judge is flexible and scalable, though it introduces potential biases from the evaluating model itself.

#### RAG evaluation

Unlike LLM evaluation, which assesses the model’s ability to generate responses from internal knowledge, RAG evaluation focuses on how well the retrieval and generation processes work together.

Evaluating a RAG application requires analyzing how different components interact. We focus on four key dimensions:

- **User input** – The query submitted by the user.
- **Retrieved context** – The passages or documents fetched from the vector database.
- **Generated output**– The final response produced by the LLM based on retrieved information.
- **Expected output** – The ideal or ground-truth answer, if available, for comparison.

By evaluating these dimensions, we can determine whether the retrieved context is relevant, the response is grounded in the retrieved data, and the system generates complete and accurate answers.

As mentioned, we break the process into two key steps to evaluate a RAG application correctly: retrieval and generation.

Since RAG applications rely on retrieving relevant documents before generating responses, retrieval quality plays a critical role in overall performance. If the retrieval step fails, the LLM will either generate incorrect answers or hallucinate information.

To assess **retrieval step** effectiveness, we can use various ranking-based metrics, including:

- **NDCG (Normalized Discounted Cumulative Gain)** – Measures how well the retrieved documents are ranked, prioritizing the most relevant ones at the top.
- **MRR (Mean Reciprocal Rank)** – Evaluates how early the first relevant document appears in the retrieved results, ensuring high-ranking relevance.

Another option is to visualize the embedding from your vector index (using algorithms such as t-SNE or UMAP) to see if there are any meaningful clusters within your vector space.

On the other hand, during **the generation step**, you can leverage similar strategies we looked at in the LLM evaluation subsection while considering the context dimension.

#### LLM application evaluation

For LLM application evaluation, we take a black-box approach, meaning we assess the entire Agentic RAG module rather than isolating individual components.

We evaluate the entire system by analyzing the input, output, and retrieved context instead of separating retrieval and generation into independent evaluations.

This approach allows us to identify system-wide failures and measure how well the retrieved knowledge contributes to generating accurate and relevant responses.

By evaluating the entire module, we can detect common RAG issues, such as hallucinations caused by missing context or low retrieval recall leading to incomplete answers, ensuring the system performs reliably in real-world scenarios.

#### **How many samples do we need to evaluate our LLM app?**

Naturally, using too few samples for evaluation can lead to misleading conclusions. For example, 5-10 examples are insufficient for capturing meaningful patterns, while 30-50 examples provide a reasonable starting point for evaluation.

Ideally, a dataset of over 400 samples ensures a more comprehensive assessment, helping to uncover biases and edge cases.

#### What else should be monitored along the LLM outputs?

Beyond output quality, **system performance metrics** like latency, throughput, reliability, and costs should be tracked to ensure scalability.

Additionally, **business metrics**—such as conversion rates, user engagement, or behavior influenced by the assistant—help measure the real-world impact of the LLM application.

#### Popular evaluation tools

Several tools specialize in RAG and LLM evaluation, offering similar capabilities for assessing retrieval quality and model performance.

For RAG evaluation, **RAGAS** is widely used to assess retrieval-augmented models, while **ARES** focuses on measuring how well the retrieved context supports the generated response.

**[Opik](https://github.com/comet-ml/opik)** stands out as an open-source solution that provides structured evaluations, benchmarking, and observability for LLM applications, ensuring assessment transparency and consistency.

Other proprietary alternatives include **Langfuse**, **Langsmith**, which is deeply integrated into the LangChain ecosystem for debugging and evaluation, and **Phoenix**.

​In our observability pipeline, implemented with **[Opik](https://github.com/comet-ml/opik)**, we combine monitoring and evaluation to ensure our application runs smoothly. Monitoring tracks all activities, while evaluation assesses performance and correctness.

#### What’s the interface of the pipeline?

LLMOps observability pipelines consist of two parts: one for monitoring prompts and another for evaluating the RAG module. These pipelines help us track system performance and ensure the application remains reliable.

The **prompt monitoring pipeline** captures entire prompt traces and metadata, such as prompt templates or models used within the chain. It also logs latency and system behavior while providing structured insights through dashboards that help detect and resolve inefficiencies.

The **RAG evaluation pipeline** tests the agentic RAG module using heuristics and LLM judges to assess performance. It receives a set of evaluation prompts and processes them to evaluate accuracy and reasoning quality. The pipeline outputs accuracy assessments, quality scores, and alerts for performance issues, helping maintain system reliability.

We utilize **[Opik](https://github.com/comet-ml/opik)** (by **[Comet ML](https://www.comet.com/site/products/ml-experiment-tracking?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)**), an open-source platform, to handle both the monitoring and evaluation of our application. Opik offers comprehensive tracing, automated evaluations, and production-ready dashboards, making it an ideal choice for our needs.

For evaluation, Opik automates performance assessments using both built-in and custom metrics. Users can define a threshold for any metric and configure alerts for immediate intervention if performance falls below the set value.

Now that we have an overview of the interfaces and components let’s dive into more details about each of the 2 pipelines.

#### **The prompt monitoring pipeline**

This component logs and monitors prompt traces. Prompt monitoring is essential to understand how our application interacts with users and identify areas for improvement. By tracking prompts and responses, we can debug issues in LLM reasoning or other issues like latency and costs.

Opik enables us to monitor latency across every phase of the generation process—pre-generation, generation, and post-generation—ensuring our application responds promptly to user inputs. ​

Latency is crucial to the user experience, as it includes multiple factors such as Time to First Token (TTFT), Time Between Tokens (TBT), Tokens Per Second (TPS), and Total Latency. Tracking these metrics helps us optimize response generation and manage hosting costs effectively.

Figure 5 provides an overview of how **[Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** logs and tracks prompt traces, helping us analyze inputs, outputs, and execution times for better performance monitoring.

[https://substackcdn.com/image/fetch/$s_!8RLK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff794b64c-1318-41f7-85be-6fc66181b969_2896x1142.png](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons) Figure 5: [Opik dashboard](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons) displaying the logged prompt traces

You can **[visualize](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** details of the execution flow of a prompt, including its input, output, and latency at each step, as displayed in Figure 6. It helps us track the steps taken during processing, analyze latency at each stage, and identify potential inefficiencies.

[https://substackcdn.com/image/fetch/$s_!qZDa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49ea5358-cfbd-4c22-80fb-e57555c9f5e4_2538x1356.png](https://substackcdn.com/image/fetch/$s_!qZDa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49ea5358-cfbd-4c22-80fb-e57555c9f5e4_2538x1356.png) Figure 6: Details of a prompt trace stored by [Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

Finally, in Figure 7, we can also **[visualize](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** key metadata like retrieval parameters, system prompts, and model settings, providing deeper insights into prompt execution context:

[https://substackcdn.com/image/fetch/$s_!3qUW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a65f34-04cd-4daf-9044-6ff24083ce35_2522x1726.png](https://substackcdn.com/image/fetch/$s_!3qUW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F06a65f34-04cd-4daf-9044-6ff24083ce35_2522x1726.png) Figure 7: The metadata of a prompt trace in [Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

The last step is to understand the RAG evaluation pipeline.

#### **The RAG evaluation pipeline**

As previously mentioned, the RAG evaluation pipeline assesses the performance of our agentic RAG module, which performs application/RAG evaluation.

The pipeline uses built-in heuristics such as Hallucination, Answer Relevance, and Moderation to evaluate response quality. Additionally, we define and integrate a custom metric and LLM judge, which assesses if the LLM's output has appropriate length and density.

This flow can also run as an offline batch pipeline during development to assess performance on test sets. Additionally, it integrates into the CI/CD pipeline to test the RAG application before deployment, ensuring any issues are identified early (similar to integration tests).

Post-deployment, it can run on a schedule to evaluate random samples from production, maintaining consistent application performance. If metrics fall below a certain threshold, we can hook an alarm system that notifies us to address potential issues promptly.

Figure 8 illustrates the results of an evaluation experiment conducted on our RAG module. It displays both the built-in and the custom performance metrics configured by us.

[https://substackcdn.com/image/fetch/$s_!S27v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddae553e-205c-4c68-98a4-e52a9281c7bc_2908x1096.png](https://substackcdn.com/image/fetch/$s_!S27v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddae553e-205c-4c68-98a4-e52a9281c7bc_2908x1096.png) Figure 8: Results of a RAG evaluation experiment stored in [Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

**[Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)** allows us to compare multiple experiments side by side. This comparison helps track performance trends over time, making refining and improving our models easier.

[https://substackcdn.com/image/fetch/$s_!Dj6n!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca348d2f-f918-4c2e-9868-ad82b8f6bde1_2912x1064.png](https://substackcdn.com/image/fetch/$s_!Dj6n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca348d2f-f918-4c2e-9868-ad82b8f6bde1_2912x1064.png) Figure 9: Comparing 2 experiments in [Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons)

By implementing these components with Opik, we maintain a robust observability pipeline that ensures our application operates efficiently.

A final note is how similar a prompt management tool, such as Opik, is to more standard experiment tracking tools, such as Comet, W&B and MLFlow. But instead of being focused on simple metrics, it’s built around the prompts as their first-class citizen.

Finally, let’s dig into the implementation.

Now that we’ve understood what it takes to build the agentic RAG and observability pipelines, let’s start implementing them.

The agentic RAG module is implemented using the SmolAgents Hugging Face frame, to build an agent that utilizes three key tools: the MongoDB retriever, the summarizer, and the "What Can I Do" tool.

Since prompt monitoring is closely tied to agent execution, here we will also cover how the system logs input/output data, latency, and other key details for each tool, ensuring full observability with Opik.

#### Building the agent

The core of our agentic RAG module starts with `get_agent()`, a method responsible for initializing the agent:

```
def get_agent(retriever_config_path: Path) -> "AgentWrapper":
    agent = AgentWrapper.build_from_smolagents(
        retriever_config_path=retriever_config_path
    )
    return agent
```

This function builds an `AgentWrapper`, which is a custom class we implemented that extends the agent's functionality by incorporating Opik for tracking all the agent’s interactions.

Building the agent requires a retriever configuration to create the MongoDB retriever tool. As a reminder from Lesson 5, we support multiple retrieval strategies based on retriever type (e.g., parent or contextual), embedding models, and other parameters.

> _**Note**: The retrieval setup is essentially copied from the offline Second Brain app in Lesson 5, ensuring consistency in document search and retrieval methods. This means the retriever is loaded exactly as it was implemented in the previous version, preserving the same retrieval logic and configurations._

#### Wrapping the agent for monitoring

The `AgentWrapper` class extends the base agent to incorporate metadata tracking with Opik. This ensures that every action taken by the agent is logged and traceable:

```
class AgentWrapper:
    def __init__(self, agent: MultiStepAgent) -> None:
        self.__agent = agent

    @property
    def input_messages(self) -> list[dict]:
        return self.__agent.input_messages

    @property
    def agent_name(self) -> str:
        return self.__agent.agent_name

    @property
    def max_steps(self) -> str:
        return self.__agent.max_steps
```

We use composition to wrap the `MultiStepAgent` from SmolAgents and expose its properties. The `MultiStepAgent` enables our agent to execute multi-step reasoning and decision-making processes.

Next, we define a method to build the agent, specifying the retriever configuration and integrating the 3 tools necessary for execution:

```
@classmethod
    def build_from_smolagents(cls, retriever_config_path: Path) -> "AgentWrapper":
        retriever_tool = MongoDBRetrieverTool(config_path=retriever_config_path)
        if settings.USE_HUGGINGFACE_DEDICATED_ENDPOINT:
            logger.warning(
                f"Using Hugging Face dedicated endpoint as the summarizer with URL: {settings.HUGGINGFACE_DEDICATED_ENDPOINT}"
            )
            summarizer_tool = HuggingFaceEndpointSummarizerTool()
        else:
            logger.warning(
                f"Using OpenAI as the summarizer with model: {settings.OPENAI_MODEL_ID}"
            )
            summarizer_tool = OpenAISummarizerTool(stream=False)

        model = LiteLLMModel(
            model_id=settings.OPENAI_MODEL_ID,
            api_base="https://api.openai.com/v1",
            api_key=settings.OPENAI_API_KEY,
        )

        agent = ToolCallingAgent(
            tools=[what_can_i_do, retriever_tool, summarizer_tool],
            model=model,
            max_steps=3,
            verbosity_level=2,
        )

        return cls(agent)
```

This method builds the agent by selecting the retriever configuration, which defines how the MongoDB retriever tool is created and configured.

> **It’s critical** that the retriever config matches the one used during the RAG feature pipeline used to populate the MongoDB vector index.

Next, we build the summarizer tool, which can either be the custom model trained in Lesson 4 and deployed on Hugging Face or an OpenAI model, depending on the settings.

After that, we initialize the LiteLLM model, which powers our AI agent.

Finally, all tools, along with the LLM model, are wrapped inside a `ToolCallingAgent` class with a maximum of three reasoning steps, ensuring structured decision-making and controlled execution flow.

Now that our agent is built, we can define its run function:

```
@opik.track(name="Agent.run")
    def run(self, task: str, **kwargs) -> Any:
        result = self.__agent.run(task, **kwargs)

        model = self.__agent.model
        metadata = {
            "system_prompt": self.__agent.system_prompt,
            "system_prompt_template": self.__agent.system_prompt_template,
            "tool_description_template": self.__agent.tool_description_template,
            "tools": self.__agent.tools,
            "model_id": self.__agent.model.model_id,
            "api_base": self.__agent.model.api_base,
            "input_token_count": model.last_input_token_count,
            "output_token_count": model.last_output_token_count,
        }
        if hasattr(self.__agent, "step_number"):
            metadata["step_number"] = self.__agent.step_number
        opik_context.update_current_trace(
            tags=["agent"],
            metadata=metadata,
        )

        return result
```

The `run` method tracks every execution of the agent using Opik’s `@track()` decorator. It logs key metadata, including the system prompt, tool descriptions, model details, and token counts within the current trace.

Having the skeleton of our agent in place, we can dig into each of the 3 tools that our model calls.

#### Building the MongoDB retriever tool

The first tool integrated is the `MongoDBRetrieverTool`, which allows the agent to find relevant documents using semantic search.

It matches a user query to the most relevant stored documents, helping the agent retrieve context when needed.

To integrate the tool with our agent, we must inherit from the `Tool ` class from SmolAgents. We also have to specify the name, description, inputs, and output type that the LLM uses to infer what the tool does and what its interface is. These are critical elements in integrating your tool with an LLM, as they are the only properties used to integrate the tool with the LLM:

```
class MongoDBRetrieverTool(Tool):
    name = "mongodb_vector_search_retriever"
    description = """Use this tool to search and retrieve relevant documents from a knowledge base using semantic search.
    This tool performs similarity-based search to find the most relevant documents matching the query.
    Best used when you need to:
    - Find specific information from stored documents
    - Get context about a topic
    - Research historical data or documentation
    The tool will return multiple relevant document snippets."""

    inputs = {
        "query": {
            "type": "string",
            "description": """The search query to find relevant documents for using semantic search.
            Should be a clear, specific question or statement about the information you're looking for.""",
        }
    }
    output_type = "string"

    def __init__(self, config_path: Path, **kwargs):
        super().__init__(**kwargs)

        self.config_path = config_path
        self.retriever = self.__load_retriever(config_path)

    def __load_retriever(self, config_path: Path):
        config = yaml.safe_load(config_path.read_text())
        config = config["parameters"]

        return get_retriever(
            embedding_model_id=config["embedding_model_id"],
            embedding_model_type=config["embedding_model_type"],
            retriever_type=config["retriever_type"],
            k=5,
            device=config["device"],
        )
```

The retriever tool is initialized with parameters from one of the retriever config files defined in Lesson 5. The settings include essential parameters such as the embedding model and retrieval type.

Now, we get to the core part of the tool, which is the `forward` method. This method is called when the AI agent uses the tool to search for information.

The `forward` method takes a query from the agent, searches for relevant documents, and returns the results in a format the agent can use.

The method is decorated with `@track`, which means its performance is being monitored with Opik. Before performing the actual search, the method first extracts important search parameters:

```
@track(name="MongoDBRetrieverTool.forward")
    def forward(self, query: str) -> str:
        if hasattr(self.retriever, "search_kwargs"):
            search_kwargs = self.retriever.search_kwargs
        else:
            try:
                search_kwargs = {
                    "fulltext_penalty": self.retriever.fulltext_penalty,
                    "vector_score_penalty": self.retriever.vector_penalty,
                    "top_k": self.retriever.top_k,
                }
            except AttributeError:
                logger.warning("Could not extract search kwargs from retriever.")

                search_kwargs = {}

        opik_context.update_current_trace(
            tags=["agent"],
            metadata={
                "search": search_kwargs,
                "embedding_model_id": self.retriever.vectorstore.embeddings.model,
            },
        )
```

First, we check what type of retriever is used and extract the relevant search parameters. Different retrievers might have different ways of configuring searches, so this code handles various cases.

The key parameters being extracted include:

- `fulltext_penalty`: Adjusts how much weight is given to exact text matches
- `vector_score_penalty`: Influences how semantic similarity affects the ranking
- `top_k`: Determines how many search results to return

These parameters significantly impact the search results. For example, a higher vector score penalty might prioritize results that match the semantic meaning of the query over those with exact keyword matches.

After setting up tracking, the method parses the query, performs the actual search, and formats the results:

```
 try:
            query = self.__parse_query(query)
            relevant_docs = self.retriever.invoke(query)

            formatted_docs = []
            for i, doc in enumerate(relevant_docs, 1):
                formatted_docs.append(
                    f"""
<document id="{i}">
<title>{doc.metadata.get("title")}</title>
<url>{doc.metadata.get("url")}</url>
<content>{doc.page_content.strip()}</content>
</document>
"""
                )

            result = "\n".join(formatted_docs)
            result = f"""
<search_results>
{result}
</search_results>
When using context from any document, also include the document URL as reference, which is found in the <url> tag.
"""
            return result
        except Exception:
            logger.opt(exception=True).debug("Error retrieving documents.")

            return "Error retrieving documents."
```

In this code snippet, we search for documents that match the query and format them in an XML-like structure. Each document includes a title, URL, and content. Additionally, the results are wrapped in tags to make them easy for the AI agent to read.

#### Creating the summarizer tool

In our agentic RAG module, we provide two summarization options: one using Hugging Face’s API and another using OpenAI’s models. Both tools inherit from `Tool` in SmolAgents and are tracked by Opik, ensuring that every summarization step is logged and monitored.

The first option for summarization is the Hugging Face endpoint-based summarizer.

This tool sends the text to an external Hugging Face model that generates a concise summary. The model deployed on Hugging Face is the one we trained in Lesson 4, which was explicitly fine-tuned for document summarization.

```
class HuggingFaceEndpointSummarizerTool(Tool):
    name = "huggingface_summarizer"
    description = """Use this tool to summarize a piece of text. Especially useful when you need to summarize a document."""

    inputs = {
        "text": {
            "type": "string",
            "description": """The text to summarize.""",
        }
    }
    output_type = "string"

    SYSTEM_PROMPT = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
You are a helpful assistant specialized in summarizing documents. Generate a concise TL;DR summary in markdown format having a maximum of 512 characters of the key findings from the provided documents, highlighting the most significant insights

### Input:
{content}

### Response:
"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        assert settings.HUGGINGFACE_ACCESS_TOKEN is not None, (
            "HUGGINGFACE_ACCESS_TOKEN is required to use the dedicated endpoint. Add it to the .env file."
        )
        assert settings.HUGGINGFACE_DEDICATED_ENDPOINT is not None, (
            "HUGGINGFACE_DEDICATED_ENDPOINT is required to use the dedicated endpoint. Add it to the .env file."
        )

        self.__client = OpenAI(
            base_url=settings.HUGGINGFACE_DEDICATED_ENDPOINT,
            api_key=settings.HUGGINGFACE_ACCESS_TOKEN,
        )
```

The code snippet above initializes the Hugging Face summarizer tool. It verifies that the necessary API credentials are available before setting up the client connection to Hugging Face’s inference endpoint.

To generate a summary, we implement the `forward` method, which is tracked by Opik for monitoring:

```
@track
    def forward(self, text: str) -> str:
        result = self.__client.chat.completions.create(
            model="tgi",
            messages=[\
                {\
                    "role": "user",\
                    "content": self.SYSTEM_PROMPT.format(content=text),\
                },\
            ],
        )

        return result.choices[0].message.content
```

This function sends the input text to the Hugging Face API, applying the predefined system prompt. The generated response is then returned, providing a structured summary.

The second summarization option uses OpenAI’s models to generate summaries. It follows a similar structure to the Hugging Face summarizer but connects to OpenAI’s API instead.

```
class OpenAISummarizerTool(Tool):
    name = "openai_summarizer"
    description = """Use this tool to summarize a piece of text. Especially useful when you need to summarize a document or a list of documents."""

    inputs = {
        "text": {
            "type": "string",
            "description": """The text to summarize.""",
        }
    }
    output_type = "string"

    SYSTEM_PROMPT = """You are a helpful assistant specialized in summarizing documents.
Your task is to create a clear, concise TL;DR summary in plain text.
Things to keep in mind while summarizing:
- titles of sections and sub-sections
- tags such as Generative AI, LLMs, etc.
- entities such as persons, organizations, processes, people, etc.
- the style such as the type, sentiment and writing style of the document
- the main findings and insights while preserving key information and main ideas
- ignore any irrelevant information such as cookie policies, privacy policies, HTTP errors,etc.

Document content:
{content}

Generate a concise summary of the key findings from the provided documents, highlighting the most significant insights and implications.
Return the document in plain text format regardless of the original format.
"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.__client = OpenAI(
            base_url="https://api.openai.com/v1",
            api_key=settings.OPENAI_API_KEY,
        )
```

This summarizer connects to OpenAI’s API and uses a structured prompt to generate high-quality summaries.

Note that because the Hugging Face model was fine-tuned on summarizing documents, it doesn't require careful prompt engineering for the desired results (it has the logic embedded into it), resulting in fewer tokens/requests, which translates to lower costs and better latencies.

#### The "What Can I Do" tool

The third and last integrated tool is the "What Can I Do" tool, which provides a list of available capabilities within the Second Brain assistant and helps users explore relevant topics.

```
@opik.track(name="what_can_i_do")
@tool
def what_can_i_do(question: str) -> str:
    """Returns a comprehensive list of available capabilities and topics in the Second Brain system.

    This tool should be used when:
    - The user explicitly asks what the system can do
    - The user asks about available features or capabilities
    - The user seems unsure about what questions they can ask
    - The user wants to explore the system's knowledge areas

    This tool should NOT be used when:
    - The user asks a specific technical question
    - The user already knows what they want to learn about
    - The question is about a specific topic covered in the knowledge base

    Args:
        question: The user's query about system capabilities. While this parameter is required,
                 the function returns a standard capability list regardless of the specific question.

    Returns:
        str: A formatted string containing categorized lists of example questions and topics
             that users can explore within the Second Brain system.

    Examples:
        >>> what_can_i_do("What can this system do?")
        >>> what_can_i_do("What kind of questions can I ask?")
        >>> what_can_i_do("Help me understand what I can learn here")
    """

    return """
You can ask questions about the content in your Second Brain, such as:

Architecture and Systems:
- What is the feature/training/inference (FTI) architecture?
- How do agentic systems work?
- Detail how does agent memory work in agentic applications?

LLM Technology:
- What are LLMs?
- What is BERT (Bidirectional Encoder Representations from Transformers)?
- Detail how does RLHF (Reinforcement Learning from Human Feedback) work?
- What are the top LLM frameworks for building applications?
- Write me a paragraph on how can I optimize LLMs during inference?

RAG and Document Processing:
- What tools are available for processing PDFs for LLMs and RAG?
- What's the difference between vector databases and vector indices?
- How does document chunk overlap affect RAG performance?
- What is chunk reranking and why is it important?
- What are advanced RAG techniques for optimization?
- How can RAG pipelines be evaluated?

Learning Resources:
- Can you recommend courses on LLMs and RAG?
"""
```

This tool is useful when users are unsure about what they can ask or want to explore different capabilities within the system. Like other tools, it is tracked by Opik for monitoring and observability.

To see our agentic RAG module in action, check out the video below, where we query our agent using the Gradio UI, visualizing how the agent reasons and calls the tools to construct the answer to our question:

Having the agentic module tested, we can check out the results of the tracking done by Opik in Figure 10:

[https://substackcdn.com/image/fetch/$s_!77pD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F224265c3-6fd2-4b64-ac1e-39630ab9df4a_2522x1726.png](https://substackcdn.com/image/fetch/$s_!77pD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F224265c3-6fd2-4b64-ac1e-39630ab9df4a_2522x1726.png) Figure 10: Example of a prompt trace in [Opik](https://github.com/comet-ml/opik)

Here, we can see that the agent calls the MongoDB retriever tool, which in turn invokes the `forward` function. Each step is logged with latency values, providing insight into execution times at different stages.

Furthermore, all metadata related to the trace—including the system prompt, tool configurations, and token usage—is captured to ensure complete observability.

Now that we have implemented the agentic RAG module, we need a structured way to evaluate its performance. This is where the **LLM evaluation pipeline** comes in, ensuring that our agentic RAG module consistently meets quality and reliability standards.

The evaluation pipeline is built using Opik, which helps us log, analyze, and score the agent’s responses. We will focus strictly on Opik's evaluation logic and how it tracks our agent’s outputs.

Before evaluating our agent, we first need to gather a suitable evaluation dataset. This dataset will help us consistently test performance and track improvements

#### Creating the evaluation dataset

To evaluate the agent properly, we use a dataset of ~30 predefined prompts that cover various scenarios the agent might encounter. This dataset allows us to consistently test our agent’s performance across different iterations, ensuring that changes do not degrade its capabilities.

```
EVALUATION_PROMPTS: List[str] = [\
    """\
Write me a paragraph on the feature/training/inference (FTI) pipelines architecture following the next structure:\
\
- introduction\
- what are its main components\
- why it's powerful\
\
Retrieve the sources when compiling the answer. Also, return the sources you used as context.\
""",\
    "What is the feature/training/inference (FTI) pipelines architecture?",\
    "What is the Tensorflow Recommenders Python package?",\
    """How does RLHF: Reinforcement Learning from Human Feedback work?\
\
Explain to me:\
- what is RLHF\
- how it works\
- why it's important\
- what are the main components\
- what are the main challenges\
""",\
    "List 3 LLM frameworks for building LLM applications and why they are important.",\
    "Explain how does Bidirectional Encoder Representations from Transformers (BERT) work. Focus on what architecture it uses, how it's different from other models and how they are trained.",\
    "List 5 ways or tools to process PDFs for LLMs and RAG",\
    """How can I optimize my LLMs during inference?\
\
Provide a list of top 3 best practices, while providing a short explanation for each, which contains why it's important.\
""",\
    "Explain to me in more detail how does an Agent memory work and why do we need it when building Agentic apps.",\
    "What is the difference between a vector database and a vector index?",\
    "Recommend me a course on LLMs and RAG",\
    "How Document Chunk overlap affects a RAG pipeline and it's performance?",\
    """What is the importance of reranking chunks for RAG?\
Explain to me:\
- what is reranking\
- how it works\
- why it's important\
- what are the main components\
- what are the main trade-offs\
""",\
    "List the most popular advanced RAG techniques to optimize RAG performance and why they are important.",\
    "List what are the main ways of evaluating a RAG pipeline and why they are important.",\
]
```

We could have added more samples, but for the first iteration, having 30 samples is a sweet spot. The core idea is to expand this split with edge case samples you find while developing the application.

We use Opik to store and manage the dataset, as shown in the following code:

```
def get_or_create_dataset(name: str, prompts: list[str]) -> opik.Dataset | None:
    client = opik.Opik()
    try:
        dataset = client.get_dataset(name=name)
    except Exception:
        dataset = None

    if dataset:
        logger.warning(f"Dataset '{name}' already exists. Skipping dataset creation.")

        return dataset

    assert prompts, "Prompts are required to create a dataset."

    dataset_items = []
    for prompt in prompts:
        dataset_items.append(
            {
                "input": prompt,
            }
        )

    dataset = create_dataset(
        name=name,
        description="Dataset for evaluating the agentic app.",
        items=dataset_items,
    )

    return dataset
```

This function ensures the dataset is created if it doesn’t exist, avoiding unnecessary duplication. It logs whether the dataset is new or previously stored and ensures that each prompt is properly formatted before evaluation.

#### Evaluating the agent

The core of the evaluation pipeline is the `evaluate_agent()` function. This function runs the set of predefined prompts through our agent and scores its responses using a combination of built-in and custom metrics.

```
def evaluate_agent(prompts: list[str], retriever_config_path: Path) -> None:
    assert settings.COMET_API_KEY, (
        "COMET_API_KEY is not set. We need it to track the experiment with Opik."
    )

    logger.info("Starting evaluation...")
    logger.info(f"Evaluating agent with {len(prompts)} prompts.")

    def evaluation_task(x: dict) -> dict:
        """Call agentic app logic to evaluate."""
        agent = agents.get_agent(retriever_config_path=retriever_config_path)
        response = agent.run(x["input"])
        context = extract_tool_responses(agent)

        return {
            "input": x["input"],
            "context": context,
            "output": response,
        }
```

In this code section, we first ensure that Opik can log the experiment by asserting that the necessary API keys are set.

Then, we define the `evaluation_task()`, a method that retrieves an instance of our agent, runs an input prompt through it, and captures both the output and retrieval context.

Before running the actual evaluation, we either fetch an existing dataset or create a new one to store our evaluation prompts:

```
# Get or create dataset
    dataset_name = "second_brain_rag_agentic_app_evaluation_dataset"
    dataset = opik_utils.get_or_create_dataset(name=dataset_name, prompts=prompts)
```

Here, `opik_utils.get_or_create_dataset()` is used to manage the datasets dynamically, as detailed earlier in this section.

Once the dataset is set up, we retrieve our agent instance and configure the experiment. The `experiment_config` dictionary defines key parameters for tracking and logging the evaluation:

```
# Evaluate
    agent = agents.get_agent(retriever_config_path=retriever_config_path)
    experiment_config = {
        "model_id": settings.OPENAI_MODEL_ID,
        "retriever_config_path": retriever_config_path,
        "agent_config": {
            "max_steps": agent.max_steps,
            "agent_name": agent.agent_name,
        },
    }
```

Next, we define the scoring metrics used to evaluate the agent's performance. Opik provides built-in evaluation metrics, but we also include custom ones for deeper analysis.

```
scoring_metrics = [\
        Hallucination(),\
        AnswerRelevance(),\
        Moderation(),\
        SummaryDensityHeuristic(),\
        SummaryDensityJudge(),\
    ]
```

The scoring process evaluates the agent’s performance across multiple dimensions:

- **Hallucination**: Measures whether the agent generates false or misleading information.
- **Answer Relevance**: Scores the relevance of the agent's response to the given prompt.
- **Moderation**: Detects potentially inappropriate or unsafe content in responses.

In addition to these built-in Opik metrics, we include two custom components. Both compute the response density (whether the answer is too long or too short) but with different techniques: heuristics or LLM-as-Judges. This is a good example of understanding the difference between the two.

- **SummaryDensityHeuristic**: Evaluates whether a response is too short, too long, or appropriately balanced.
- **SummaryDensityJudge**: Uses an external LLM to judge response density and conciseness.

Finally, we execute the evaluation process using the metrics defined and our evaluation dataset:

```
if dataset:
        evaluate(
            dataset=dataset,
            task=evaluation_task,
            scoring_metrics=scoring_metrics,
            experiment_config=experiment_config,
            task_threads=2,
        )
    else:
        logger.error("Can't run the evaluation as the dataset items are empty.")
```

This code ensures that evaluation runs only when a dataset is available. The `evaluate()` function runs the agent using the `evaluation_task()` method on the evaluation dataset and measures the defined scoring metrics. The [results are then logged in Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons) for further analysis and comparison.

#### The summary density heuristic

In our evaluation pipeline, we include a custom metric called **summary density heuristic**.

This metric assesses whether an LLM-generated response is appropriately concise and informative. It extends `BaseMetric` from Opik, allowing us to integrate it seamlessly into our evaluation framework.

The purpose of this heuristic is to ensure that responses are neither too short nor excessively long. A well-balanced response provides sufficient detail without unnecessary verbosity.

```
class SummaryDensityHeuristic(base_metric.BaseMetric):
    """
    A metric that evaluates whether an LLM's output has appropriate length and density.

    This metric uses an heuristic to determine if the output length is appropriate for the given instruction.
    It returns a normalized score between 0 and 1, where:
    - 0.0 (Poor): Output is either too short and incomplete, or too long with unnecessary information
    - 0.5 (Good): Output has decent length balance but still slightly too short or too long
    - 1.0 (Excellent): Output length is appropriate, answering the question concisely without being verbose
    """

    def __init__(
        self,
        name: str = "summary_density_heuristic",
        min_length: int = 128,
        max_length: int = 1024,
    ) -> None:
        self.name = name
        self.min_length = min_length
        self.max_length = max_length
```

This snippet initializes the metric with a name, minimum length, and maximum length. The `min_length` and `max_length` parameters define the acceptable range for a response's length.

To evaluate the response length, we define the `score()` function, which compares the output against the predefined length limits:

```
 def score(
        self, input: str, output: str, **ignored_kwargs: Any
    ) -> score_result.ScoreResult:
        """
        Score the output of an LLM.

        Args:
            input: The input prompt given to the LLM.
            output: The output of an LLM to score.
            **ignored_kwargs: Any additional keyword arguments.

        Returns:
            ScoreResult: The computed score with explanation.
        """

        length_score = self._compute_length_score(output)

        reason = f"Output length: {len(output)} chars. "
        if length_score == 1.0:
            reason += "Length is within ideal range."
        elif length_score >= 0.5:
            reason += "Length is slightly outside ideal range."
        else:
            reason += "Length is significantly outside ideal range."

        return score_result.ScoreResult(
            name=self.name,
            value=length_score,
            reason=reason,
        )
```

The `score()` function determines how well the LLM's response fits within the acceptable length range. It assigns a normalized score between 0 and 1 based on whether the output is too short, too long, or appropriately balanced.

The core logic of this metric lies in `_compute_length_score()`, which calculates a numerical score based on response length:

```
    def _compute_length_score(self, text: str) -> float:
        """
        Compute a score based on text length relative to min and max boundaries.

        Args:
            text: The text to evaluate.

        Returns:
            float: A score between 0 and 1, where:
                - 0.0: Text length is significantly outside the boundaries
                - 0.5: Text length is slightly outside the boundaries
                - 1.0: Text length is within the ideal range
        """
        length = len(text)

        # If length is within bounds, return perfect score
        if self.min_length <= length <= self.max_length:
            return 1.0

        if length < self.min_length:
            deviation = (self.min_length - length) / self.min_length
        else:
            deviation = (length - self.max_length) / self.max_length

        # Convert deviation to a score between 0 and 1
        # deviation <= 0.5 -> score between 0.5 and 1.0
        # deviation > 0.5 -> score between 0.0 and 0.5
        score = max(0.0, 1.0 - deviation)

        return score
```

This function ensures that responses falling within the predefined length range receive a perfect score of 1.0. If a response deviates too far from the range, its score is gradually reduced to reflect the severity of the deviation.

#### The summary density judge

The summary density judge is a custom evaluation component that builds upon the summary density metric by using an external LLM to assess response length.

Instead of relying on a manually calculated heuristic, this judge uses an AI model to determine if the length of an output is appropriate for a given input.

This approach allows us to incorporate more nuanced and context-aware judgments into our evaluation pipeline. Like the heuristic, it integrates seamlessly with Opik’s evaluation framework:

```
class LLMJudgeStyleOutputResult(BaseModel):
    score: int
    reason: str

class SummaryDensityJudge(base_metric.BaseMetric):
    """
    A metric that evaluates whether an LLM's output has appropriate length and density.

    This metric uses another LLM to judge if the output length is appropriate for the given instruction.
    It returns a normalized score between 0 and 1, where:
    - 0.0 (Poor): Output is either too short and incomplete, or too long with unnecessary information
    - 0.5 (Good): Output has decent length balance but still slightly too short or too long
    - 1.0 (Excellent): Output length is appropriate, answering the question concisely without being verbose
    """

    def __init__(
        self,
        name: str = "summary_density_judge",
        model_name: str = settings.OPENAI_MODEL_ID,
    ) -> None:
        self.name = name
        self.llm_client = LiteLLMChatModel(model_name=model_name)
        self.prompt_template = """
        You are an impartial expert judge. Evaluate the quality of a given answer to an instruction based on how long the answer it is.

How to decide wether the lengths of the answer is appropriate:
1 (Poor): Too short, does not answer the question OR too long, it contains too much noise and unrequired information, where the answer could be more concise.
2 (Good): Good lengthbalance of the answer, but the answer is still too short OR too long.
3 (Excellent): The length of the answer is appropriate, it answers the question and is not too long or too short.

Example of bad answer that is too short:
<answer>
LangChain, LlamaIndex, Haystack
</answer>

Example of bad answer that is too long:
<answer>
LangChain is a powerful and versatile framework designed specifically for building sophisticated LLM applications. It provides comprehensive abstractions for essential components like prompting, memory management, agent behaviors, and chain orchestration. The framework boasts an impressive ecosystem with extensive integrations across various tools and services, making it highly flexible for diverse use cases. However, this extensive functionality comes with a steeper learning curve that might require dedicated time to master.

LlamaIndex (which was formerly known as GPTIndex) has carved out a specialized niche in the LLM tooling landscape, focusing primarily on data ingestion and advanced indexing capabilities for Large Language Models. It offers a rich set of sophisticated mechanisms to structure and query your data, including vector stores for semantic similarity search, keyword indices for traditional text matching, and tree indices for hierarchical data organization. While it particularly shines in Retrieval-Augmented Generation (RAG) applications, its comprehensive feature set might be excessive for more straightforward implementation needs.

Haystack stands out as a robust end-to-end framework that places particular emphasis on question-answering systems and semantic search capabilities. It provides a comprehensive suite of document processing tools and comes equipped with production-ready pipelines that can be deployed with minimal configuration. The framework includes advanced features like multi-stage retrieval, document ranking, and reader-ranker architectures. While these capabilities make it powerful for complex information retrieval tasks, new users might find the initial configuration and architecture decisions somewhat challenging to navigate.

Each of these frameworks brings unique strengths to the table while sharing some overlapping functionality. The choice between them often depends on specific use cases, technical requirements, and team expertise. LangChain offers the broadest general-purpose toolkit, LlamaIndex excels in data handling and RAG, while Haystack provides the most streamlined experience for question-answering systems.
</answer>

Example of excellent answer that is appropriate:
<answer>
1. LangChain is a powerful framework for building LLM applications that provides abstractions for prompting, memory, agents, and chains. It has extensive integrations with various tools and services, making it highly flexible but potentially complex to learn.
2. LlamaIndex specializes in data ingestion and indexing for LLMs, offering sophisticated ways to structure and query your data through vector stores, keyword indices, and tree indices. It excels at RAG applications but may be overkill for simpler use cases.
3. Haystack is an end-to-end framework focused on question-answering and semantic search, with strong document processing capabilities and ready-to-use pipelines. While powerful, its learning curve can be steep for beginners.
</answer>

Instruction: {input}

Answer: {output}

Provide your evaluation in JSON format with the following structure:
{{
    "accuracy": {{
        "reason": "...",
        "score": 0
    }},
    "style": {{
        "reason": "...",
        "score": 0
    }}
}}
"""
```

In this snippet, we initialize the summary density judge, specifying the model it will use to evaluate responses. The `prompt_template` provides clear instructions for the external LLM, defining the criteria for scoring an answer.

The judge’s scoring function uses the external LLM to analyze a response and assign a score based on how well its length aligns with the expected range:

```
    def score(self, input: str, output: str, **ignored_kwargs: Any):
        prompt = self.prompt_template.format(input=input, output=output)

        model_output = self.llm_client.generate_string(
            input=prompt, response_format=LLMJudgeStyleOutputResult
        )

        return self._parse_model_output(model_output)
```

The `score()` function formats the prompt and sends it to the external LLM. The model then evaluates the response and provides a structured output with a score and explanation.

Once the external model returns a score, we process it to ensure consistency and normalize the values.

```
    def _parse_model_output(self, content: str) -> score_result.ScoreResult:
        try:
            dict_content = json.loads(content)
        except Exception:
            raise exceptions.MetricComputationError("Failed to parse the model output.")

        score = dict_content["score"]
        try:
            assert 1 <= score <= 3, f"Invalid score value: {score}"
        except AssertionError as e:
            raise exceptions.MetricComputationError(str(e))

        score = (score - 1) / 2.0  # Normalize the score to be between 0 and 1

        return score_result.ScoreResult(
            name=self.name,
            value=score,
            reason=dict_content["reason"],
        )
```

The `_parse_model_output()` function ensures that the returned score is valid and within the expected range. The score is then normalized between 0 and 1 for consistency with other evaluation metrics.

#### Evaluation results

We [track evaluation results in Opik](https://www.comet.com/opik?utm_source=paul_2nd_brain_course&utm_campaign=opik&utm_medium=lessons), allowing us to compare different agent versions and detect performance regressions.

Figure 11 shows a sample evaluation run, displaying the scores across all metrics:

[https://substackcdn.com/image/fetch/$s_!KzPS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918a538b-8ac6-4fb7-864b-557a70ab1fe0_2908x1096.png](https://substackcdn.com/image/fetch/$s_!KzPS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F918a538b-8ac6-4fb7-864b-557a70ab1fe0_2908x1096.png) Figure 11: Outcome of an evaluation run in [Opik](https://github.com/comet-ml/opik)

By implementing this evaluation pipeline, we ensure that our agentic RAG module continues to improve while maintaining accuracy, relevance, and overall quality.

</details>

<details>
<summary>What is an AI agent?</summary>

# What is an AI agent?

**Source URL:** <https://cloud.google.com/discover/what-are-ai-agents>

_Last Updated: 04/02/2026_

AI agents are software systems that use AI to pursue goals and complete tasks on behalf of users. They show reasoning, planning, and memory and have a level of autonomy to make decisions, learn, and adapt.

Their capabilities are made possible in large part by the multimodal capacity of generative AI and AI foundation models. AI agents can process multimodal information like text, voice, video, audio, code, and more simultaneously; can converse, reason, learn, and make decisions. They can learn over time and facilitate transactions and business processes. Agents can work with other agents to coordinate and perform more complex workflows.

[https://www.gstatic.com/bricks/image/c944e80e-4236-48d3-ae05-a5cccb119686.png\\
7:39](https://www.youtube.com/watch?v=NWF5Jo0-ziY)

Intro to Agents: What's new and what we've learned

## Key features of an AI agent

As explained above, while the key features of an AI agent are reasoning and acting (as described in [ReAct Framework](https://arxiv.org/pdf/2210.03629)) more features have evolved over time.

- **Reasoning:** This core cognitive process involves using logic and available information to draw conclusions, make inferences, and solve problems. AI agents with strong reasoning capabilities can analyze data, identify patterns, and make informed decisions based on evidence and context.
- **Acting**: The ability to take action or perform tasks based on decisions, plans, or external input is crucial for AI agents to interact with their environment and achieve goals. This can include physical actions in the case of embodied AI, or digital actions like sending messages, updating data, or triggering other processes.
- **Observing**: Gathering information about the environment or situation through perception or sensing is essential for AI agents to understand their context and make informed decisions. This can involve various forms of perception, such as computer vision, natural language processing, or sensor data analysis.
- **Planning**: Developing a strategic plan to achieve goals is a key aspect of intelligent behavior. AI agents with planning capabilities can identify the necessary steps, evaluate potential actions, and choose the best course of action based on available information and desired outcomes. This often involves anticipating future states and considering potential obstacles.
- **Collaborating**: Working effectively with others, whether humans or other AI agents, to achieve a common goal is increasingly important in complex and dynamic environments. Collaboration requires communication, coordination, and the ability to understand and respect the perspectives of others.
- **Self-refining**: The capacity for self-improvement and adaptation is a hallmark of advanced AI systems. AI agents with self-refining capabilities can learn from experience, adjust their behavior based on feedback, and continuously enhance their performance and capabilities over time. This can involve machine learning techniques, optimization algorithms, or other forms of self-modification.

## What is the difference between AI agents, AI assistants, and bots?

**AI assistants** are AI agents designed as applications or products to collaborate directly with users and perform tasks by understanding and responding to natural human language and inputs. They can reason and take action on the users' behalf with their supervision.

AI assistants are often embedded in the product being used. A key characteristic is the interaction between the assistant and user through the different steps of the task. The assistant responds to requests or prompts from the user, and can recommend actions but decision-making is done by the user.

| | **AI agent** | **AI assistant** | **Bot** ﻿ |
| --- | --- | --- | --- |
| **Purpose** | Autonomously and proactively perform tasks | Assisting users with tasks | Automating simple tasks or conversations |
| **Capabilities** | Can perform complex, multi-step actions; learns and adapts; can make decisions independently | Responds to requests or prompts; provides information and completes simple tasks; can recommend actions but the user makes decisions | Follows pre-defined rules; limited learning; basic interactions |
| **Interaction** | Proactive; goal-oriented | Reactive; responds to user requests | Reactive; responds to triggers or commands |

### Key differences

- **Autonomy**: AI agents have the highest degree of autonomy, able to operate and make decisions independently to achieve a goal. AI assistants are less autonomous, requiring user input and direction. Bots are the least autonomous, typically following pre-programmed rules.
- **Complexity**: AI agents are designed to handle complex tasks and workflows, while AI assistants and bots are better suited for simpler tasks and interactions.
- **Learning**: AI agents often employ machine learning to adapt and improve their performance over time. AI assistants may have some learning capabilities, while bots typically have limited or no learning.

## How do AI agents work?

Every agent defines its role, personality, and communication style, including specific instructions and descriptions of available tools.

- **Persona**: A well defined persona allows an agent to maintain a consistent character and behave in a manner appropriate to its assigned role, evolving as the agent gains experience and interacts with its environment.
- **Memory**: The agent is equipped in general with short term, long term, consensus, and episodic memory. Short term memory for immediate interactions, long-term memory for historical data and conversations, episodic memory for past interactions, and consensus memory for shared information among agents. The agent can maintain context, learn from experiences, and improve performance by recalling past interactions and adapting to new situations.
- **Tools**: Tools are functions or external resources that an agent can utilize to interact with its environment and enhance its capabilities. They allow agents to perform complex tasks by accessing information, manipulating data, or controlling external systems, and can be categorized based on their user interface, including physical, graphical, and program-based interfaces. Tool learning involves teaching agents how to effectively use these tools by understanding their functionalities and the context in which they should be applied.
- **Model**: Large language models (LLMs) serve as the foundation for building AI agents, providing them with the ability to understand, reason, and act. LLMs act as the "brain" of an agent, enabling them to process and generate language, while other components facilitate reason and action.

## What are the types of agents in AI?

AI agents can be categorized in various ways based on their capabilities, roles, and environments. Here are some key categories of agents:

There are different definitions of agent types and agent categories.

### Based on interaction

One way to categorize agents is by how they interact with users. Some agents engage in direct conversation, while others operate in the background, performing tasks without direct user input:

- **Interactive partners** (also known as, surface agents) – Assisting us with tasks like customer service, healthcare, education, and scientific discovery, providing personalized and intelligent support. Conversational agents include Q&A, chit chat, and world knowledge interactions with humans. They are generally user query triggered and fulfill user queries or transactions.
- **Autonomous background processes** (also known as, background agents) – Working behind the scenes to automate routine tasks, analyze data for insights, optimize processes for efficiency, and proactively identify and address potential issues. They include workflow agents. They have limited or no human interaction and are generally driven by events and fulfill queued tasks or chains of tasks.

### Based on number of agents

- **Single agent**: Operate independently to achieve a specific goal. They utilize external tools and resources to accomplish tasks, enhancing their functional capabilities in diverse environments. They are best suited for well defined tasks that do not require collaboration with other AI agents. Can only handle one foundation model for its processing.
- **Multi-agent**: Multiple AI agents that collaborate or compete to achieve a common objective or individual goals. These systems leverage the diverse capabilities and roles of individual agents to tackle complex tasks. Multi-agent systems can simulate human behaviors, such as interpersonal communication, in interactive scenarios. Each agent can have different foundation models that best fit their needs.

### Benefits of using AI agents

AI agents can enhance the capabilities of language models by providing autonomy, task automation, and the ability to interact with the real world through tools and embodiment.

#### Efficiency and productivity

**Increased output**: Agents divide tasks like specialized workers, getting more done overall.

**Simultaneous execution**: Agents can work on different things at the same time without getting in each other's way.

**Automation**: Agents take care of repetitive tasks, freeing up humans for more creative work.

#### Improved decision-making

**Collaboration**: Agents work together, debate ideas, and learn from each other, leading to better decisions.

**Adaptability**: Agents can adjust their plans and strategies as situations change.

**Robust reasoning**: Through discussion and feedback, agents can refine their reasoning and avoid errors.

#### Enhanced capabilities

**Complex problem-solving**: Agents can tackle challenging real-world problems by combining their strengths.

**Natural language communication**: Agents can understand and use human language to interact with people and each other.

**Tool use**: Agents can interact with the external world by using tools and accessing information.

**Learning and self-improvement**: Agents learn from their experiences and get better over time.

#### Social interaction and simulation

**Realistic simulations**: Agents can model human-like social behaviors, such as forming relationships and sharing information.

**Emergent behavior**: Complex social interactions can arise organically from the interactions of individual agents.

## Challenges with using AI agents

While AI agents offer many benefits, there are also some challenges associated with their use:

**Tasks requiring deep empathy / emotional intelligence or requiring complex human interaction and social dynamics**– AI agents can struggle with nuanced human emotions. Tasks like therapy, social work, or conflict resolution require a level of emotional understanding and empathy that AI currently lacks. They may falter in complex social situations that require understanding unspoken cues.

**Situations with high ethical stakes** – AI agents can make decisions based on data, but they lack the moral compass and judgment needed for ethically complex situations. This includes areas like law enforcement, healthcare (diagnosis and treatment), and judicial decision-making.

**Domains with unpredictable physical environments** – AI agents can struggle in highly dynamic and unpredictable physical environments where real-time adaptation and complex motor skills are essential. This includes tasks like surgery, certain types of construction work, and disaster response.

**Resource-intensive applications** – Developing and deploying sophisticated AI agents can be computationally expensive and require significant resources, potentially making them unsuitable for smaller projects or organizations with limited budgets.

## Deploy AI agents for scale and efficiency with Cloud Run

AI agents, with their inherent need for flexible compute power to handle reasoning, planning, and tool use, can be an excellent fit for [Cloud Run](https://cloud.google.com/run). This fully managed serverless platform allows you to deploy your agent's code—often packaged within a container—as a scalable, reliable service or job. This approach abstracts away infrastructure management, letting developers concentrate on refining the agent's logic.

Cloud Run offers several features that directly support the architecture and demands of sophisticated AI agents:

- **Scalability and cost-efficiency:** Cloud Run automatically scales the number of container instances up to meet peak demand and, crucially, can scale down to zero when the agent is idle. This means you only pay for the exact compute resources consumed during the agent's active execution, making it cost-effective for goal-oriented, intermittent workloads.
- **Agent orchestration and serving:** The core agent logic—which manages the model calls, tool selection, and reasoning process—runs as a Cloud Run service. This service provides a stable HTTPS endpoint, making the agent easily accessible via an API for user-facing applications or for communication with other agents
- **Agent-to-Agent, or A2A:** Frameworks like the [Agent Development Kit (](https://github.com/google/adk-docs) ADK) are designed to integrate seamlessly with Cloud Run for easy deployment.

By leveraging Cloud Run's secure, auto-scaling, and flexible environment, organizations can operationalize complex single- or multi-agent systems efficiently.

### Use cases for AI agents

Organizations have been deploying agents to address a variety [use cases](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders), which we group into six key broader categories:

### Customer agents

Customer agents deliver personalized customer experiences by understanding customer needs, answering questions, resolving customer issues, or recommending the right products and services. They work seamlessly across multiple channels including the web, mobile, or point of sale, and can be integrated into product experiences with voice or video.

### Employee agents

Employee agents boost productivity by streamlining processes, managing repetitive tasks, answering employee questions, as well as editing and translating critical content and communications.

### Creative agents

Creative agents supercharge the design and creative process by generating content, images, and ideas, assisting with design, writing, personalization, and campaigns.

### Data agents

Data agents are built for complex data analysis. They have the potential to find and act on meaningful insights from data, all while ensuring the factual integrity of their results.

### Code agents

Code agents accelerate software development with AI-enabled code generation and coding assistance, and to ramp up on new languages and code bases. Many organizations are seeing significant gains in productivity, leading to faster deployment and cleaner, clearer code.

### Security agents

Security agents strengthen security posture by mitigating attacks or increasing the speed of investigations. They can oversee security across various surfaces and stages of the security life cycle: prevention, detection, and response.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org.md">
<details>
<summary>601 real-world gen AI use cases from the world's leading organizations</summary>

Phase: [EXPLOITATION]

# 601 real-world gen AI use cases from the world's leading organizations

**Source URL:** <https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders>

AI & Machine Learning

# 1,001 real-world gen AI use cases from the world's leading organizations

October 9, 2025

![https://storage.googleapis.com/gweb-cloudblog-publish/images/1001-real-world-gen-ai-use-cases-google-cl.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/1001-real-world-gen-ai-use-cases-google-cl.max-2000x2000.png)

##### Matt Renner

President and Chief Revenue Officer, Google Cloud

##### Matt A.V. Chaban

Senior Editor, Transform

#### AI is here, AI is everywhere: Top companies, governments, researchers, and startups are already enhancing their work with Google's AI solutions.

##### Try Nano Banana 2

State-of-the-art image generation and editing

[Try now](https://console.cloud.google.com/vertex-ai/studio/multimodal?model=gemini-3.1-flash-image-preview)

**Published April 12, 2024; last updated October 9, 2025.**

* * *

- [Automotive & Logistics](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Continental)
- [Business & Professional Services](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Accenture%20is)
- [Financial Services](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=*Albo)
- [Healthcare & Life Sciences](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Bennie%20Health)
- [Hospitality & Travel](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=*Agoda)
- [Manufacturing, Industrial & Electronics](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Motorola%E2%80%99s)
- [Media, Marketing & Gaming](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Data%C3%AFads)
- [Public Sector & Nonprofits](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Alma%2C)
- [Retail](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=*425DEGREE)
- [Technology](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=Abstrakt)
- [Telecommunications](https://cloud.google.com/transform/101-real-world-generative-ai-use-cases-from-industry-leaders#:~:text=*Banglalink)

* * *

A year and a half ago, during Google Cloud Next 24, we published this list for the first time. It numbered 101 entries.

It felt like a lot at the time, and served as a showcase of how much momentum both Google and the industry were seeing around generative AI adoption. In the brief period then of gen AI being widely available, organizations of all sizes had begun experimenting with it and putting it into production across their work and across the world, doing so at [a speed rarely seen with new technology](https://cloud.google.com/transform/the-prompt-prototype-to-production-gen-ai).

What a difference these past months have made. Our list has now grown by 10X. And still, that’s just scratching the surface of what’s becoming possible with AI across the enterprise, or what might be coming in the next year and a half.

Many of these use cases are coming to life this week at our Gemini at Work event, which [you can watch live today](https://www.linkedin.com/events/7374928298075791361/).

**Mercedes Benz** is building cars that can converse with their drivers while **Mercari**, Japan’s largest online marketplace, and **Commerzbank** are making it easier than ever to reach a customer service agent — Mercari even anticipates a 500% ROI while reducing employee workloads by 20%. And talk about scale: **Virgin Voyages** is using Veo’s text-to-video features to create thousands of hyper-personalized ads and emails in a single go without sacrificing brand voice or style. Nor are they alone. **Figma**, which calls itself the “collaborative interface design tool,” lets any organization create high-quality, brand-approved images and assets in seconds.

\[ _Looking for how to build AI use cases just like these? Check out [**our handy guide with 101 technical blueprints**](https://cloud.google.com/blog/products/ai-machine-learning/real-world-gen-ai-use-cases-with-technical-blueprints) from some of these real-world examples._\]

Given the incredible pace of innovation and progress we continue to see, we are confident that AI will grow beyond even our imagination as our customers continue to challenge us to design, build, deploy, and create value.

Hopefully you find something here that will propel our own AI endeavors together.

* * *

The list is organized by 11 major industry groups, and within those, six agent types: Customer, Employee, Creative, Code, Data, and Security. There are 400 new entries in this edition, denoted with an asterisk (\*) before the organization’s name.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Auto__Logistics.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Auto__Logistics.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Auto__Logistics.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Auto__Logistics.max-900x900.jpg)

Automotive & Logistics

### **Customer Agents**

- **Continental** is using Google's data and AI technologies to develop automotive solutions that are safe, efficient, and user-focused. One of the initial outcomes of this partnership is the integration of Google Cloud's conversational AI technologies into Continental's Smart Cockpit HPC, an in-vehicle speech-command solution.

- **General Motors**’ OnStar has been augmented with new AI features, including a virtual assistant powered by Google Cloud’s conversational AI technologies that are better able to recognize the speaker’s intent.

- \* **LUXGEN**, a Taiwanese electric vehicle brand, uses Vertex AI to power an AI agent that answers customer questions on its official LINE account. The chatbot has reduced the workload of human customer service agents by 30%.

- **MercedesBenz** builds cars with Google AI that can talk to their drivers. They are using Gemini via VertexAI to power their MBUX Virtual Assistant, which enables natural conversations and provides personalized answers to drivers for things like navigation and points of interest.

- **Mercedes Benz** is also infusing e-commerce capabilities into its online storefront with a gen AI-powered smart sales assistant.

- **PODS** worked with the advertising agency Tombras to create the “World’s Smartest Billboard” using Gemini — a campaign on its trucks that could adapt to each neighborhood in New York City, changing in real-time based on data. It hit all 299 neighborhoods in just 29 hours, creating more than 6,000 unique headlines.

- **UPS Capital** launched DeliveryDefense Address Confidence, which uses machine learning and UPS data to provide a confidence score for shippers to help them determine the likelihood of a successful delivery.

- **Volkswagen of America** built a virtual assistant in the myVW app, where drivers can explore their owners’ manuals and ask questions, such as, “How do I change a flat tire?” or “What does this digital cockpit indicator light mean?” Users can also use Gemini’s multimodal capabilities to see helpful information and context on indicator lights simply by pointing their smartphone cameras at the dashboard.


### **Employee Agents**

- **704 Apps** creates applications serving the last-mile transportation segment, connecting thousands of drivers and passengers every day. During trips, the audio content of conversations between car occupants is sent to Gemini, which measures the emotional “temperature." Specific words such as “robbery”, “assault”, “kidnapping”, among others, can be classified as hostile by the tool, generating alerts to anticipate risky situations before they happen.

- \* **Geotab**, one of the largest telematics companies in the world, connects 4.7 million vehicles to make them safer, more sustainable, and more efficient. Teams now use Google Workspace with Gemini for research, document summarization, status reporting, legal document review, and data filtering—supporting functions from HR to engineering.

- **Oxa**, a developer of software for autonomous vehicles, uses Gemini for Google Workspace to build campaign templates for metrics reporting, write social posts in order to make marketing processes more efficient, create job descriptions, and proofread content across all teams, saving time and resources.

- \* **Rivian**, maker of popular electric SUVs, uses Gemini integrated with Google Workspace to empower employees to conduct instant research, accelerate learning, and gain new skills rapidly. The AI enables staff to perform deep research and get up to speed on complex topics faster, enhancing productivity across the fast-paced automotive company.

- \* **Rivian** also uses NotebookLM to centralize and share answers to frequently asked questions using verified sources with interactive chat features. The AI reduced repetitive inquiries by creating a shareable knowledge base with grounded sources, saving employees time and helping them work more efficiently.

- \* **Routematic**, a Transport-as-a-Service platform for employee transportation, migrated its entire infrastructure to Google Cloud using Compute Engine and Google Kubernetes Engine in eight months with zero downtime. The company shortened product release cycles from weeks to days while unlocking significant cost savings through better control over billing and infrastructure.

- **Toyota** implemented an AI platform using Google Cloud's AI infrastructure to enable factory workers to develop and deploy machine learning models. This led to a reduction of over 10,000 man-hours per year and increased efficiency and productivity.

- **Uber** is using AI agents to help employees be more productive, save time, and be even more effective at work. For customer service representatives, the company launched new tools that summarize communications with users and can even surface context from previous interactions, so front-line staff can be more helpful and effective.

- **Uber** also uses Google Workspace with Gemini to save time on repetitive tasks, free up developers for higher-value work, reduce their agency spending, and to enhance employee retention.


### **Code Agents**

- **Renault Group**’s **Ampere**, an EV and software subsidiary created in 2023, is using an enterprise version of Gemini Code Assist, built for teams of developers and able to understand a company’s code base, standards, and conventions.


### **Data Agents**

- **BMW Group**, in collaboration with Monkeyway, developed the AI solution SORDI.ai to optimize industrial planning processes and supply chains with gen AI. This involves scanning assets and using Vertex AI to create 3D models that act as digital twins that perform thousands of simulations to optimize distribution efficiency.

- **Dematic** is using the multimodal features in Vertex AI and Gemini to build end-to-end fulfillment solutions for both ecommerce and omnichannel retailers.

- \* **Domina**, a Colombian logistics company managing over 20 million annual shipments, uses Vertex AI and Gemini to predict package returns and automate delivery validation. The AI-powered platform improved real-time data access by 80%, eliminated manual report generation time entirely, and increased delivery effectiveness by 15%.

- **Geotab**, a global leader in telematics, uses BigQuery and Vertex AI to analyze billions of data points per day from over 4.6 million vehicles. This enables real-time insights for fleet optimization, driver safety, transportation decarbonization, and macro-scale transportation analytics to drive safer and more sustainable cities.

- **Kinaxis** is building data-driven supply chain solutions to address logistics use cases including scenario modeling, planning, operations management, and automation.

- \* **Moglix**, an Indian digital supply chain platform serving over 1,000 manufacturing businesses, deployed Vertex AI for generative AI vendor discovery that connects with maintenance, repair, and operations suppliers. The company achieved a 4X improvement in Sourcing Team Efficiency business, increasing it from about INR 12 crore to 50 crore per quarter.

- **Nuro**, an autonomous driving company, uses vector search in AlloyDB to enable their vehicles to accurately classify objects encountered on the road.

- **Picterra**, which calls itself a search engine for the physical world, adopted Google Kubernetes Engine to power its platform, providing the ability to quickly scale to meet the demands of geospatial AI workloads. With GKE, Picterra can model the terrain of entire countries quickly, even at ultra-high resolutions.

- **Prewave**, a supply chain risk intelligence platform, utilizes Google Cloud's AI services to provide end-to-end risk monitoring and ESG risk detection for businesses. This enables companies to gain transparency deep into their supply chains, ensuring resilience, sustainability, and compliance with regulations like the European CSDDD.

- **TruckHouse** specializes in expedition vehicles and speeds inventory tracking with Gemini in Sheets so they can spend more time in the great outdoors.

- \* **tulanā**, an intelligent decision support provider, has a highly customizable platform that uses forecasting, optimization, simulation, and AI to help enterprise clients make better decisions across supply chains and physical infrastructure. tulanā is using Cloud Run to horizontally scale its optimization workloads, Gemini for intelligent ETL processes, and Cloud SQL and Big Query to store customer data.

- **UPS** is building a digital twin of its entire distribution network, so both workers and customers can see where their packages are at any time.

- **Woven** – **Toyota**'s investment in the future of mobility — is partnering with Google to leverage vast amounts of data and AI to enable autonomous driving, supported by thousands of ML workloads on Google Cloud’s AI Hypercomputer. This has resulted in 50% total-cost-of-ownership savings to support automated driving.


### Security Agents

- \* **Mitsubishi Motors** uses Google Security Operations with AI-powered SIEM and SOAR capabilities to protect its global operations from increasingly sophisticated cyber attacks. The cloud-based security platform simplified security management across the Mitsubishi Motors Group and reduced operational burdens through automated threat detection and response.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Business.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Business.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Business.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Business.max-900x900.jpg)

Business & Professional Services

### **Customer Agents**

- **Accenture** is transforming customer support at a major retailer by offering convenient self-service options through virtual assistants, enhancing the overall customer experience.

- **\*atmira**, a Spanish technology consulting company with 800 employees, uses Google Kubernetes Engine and Oracle on Google Cloud to power SIREC, an AI-driven debt collection platform that manages approximately 114 million monthly requests. The platform improved recovery rates by 30% to 40%, increased payment conversions by 45%, and reduced operational costs by 54%.

- **Capgemini** is using Google Cloud to build AI agents that help optimize the ecommerce experience by helping retailers accept customer orders through new revenue channels and accelerate the order-to-cash process for digital stores.

- **Deloitte** offers a “Care Finder” agent, built with Google Cloud, as part of its Agent Fleet. The agent helps care seekers find in-network providers — often in less than a minute — significantly faster than the average call time of five to eight minutes.

- **Ferret.ai** uses AI to offer insights about the backgrounds of people in a user's personal and professional network, providing a curated relationship intelligence and monitoring solution for its users — increasingly important services in a world of growing reputational risks.

- **\*Humanizadas** uses Google Kubernetes Engine, Cloud Run, and Vertex AI with Gemini models to deliver real-time ESG indicators and sustainability intelligence to organizations across multiple countries. The company built an AI-powered conversational chatbot using Dialogflow that acts as a 24/7 sustainability specialist trained on client-specific data, while automated classification systems process millions of stakeholder data points across 150 hierarchical sustainability themes.

- **Intuit**, the makers of TurboTax, integrated Google Cloud’s visual recognition platform, Doc AI, and Gemini models into Intuit’s proprietary GenOS. This will expand the capabilities of Intuit’s “done-for-you” autofill of tax returns across the ten most common U.S. tax forms (variations of the 1099 and 1040 forms), helping users save time and boosting accuracy.

- **\*NoBroker**, a real estate platform, uses its ConvoZen AI, powered by Gemini and L4 GPUs, to automate customer support across multiple Indian languages. The platform processes 10,000 hours of recordings daily, with AI agents projected to handle 25-40% of future calls and save customers $1 billion annually.

- **Stax AI**, which aims to revolutionize retirement planning with AI, uses MongoDB Atlas and Vertex AI to automate its manual processes and transform massive volumes of trust accounting data in minutes.

- **Sutherland**, a leading digital transformation company, is focused on bringing together human expertise and AI, including boosting its client-facing teams by automatically surfacing suggested responses and automating insights in real time.

- **Wagestream**, a financial wellbeing platform for employee benefits, is using Gemini models to handle more than 80% of its internal customer inquiries, including questions about payment dates, balances, and more.

- **WealthAPI**, the leading provider of wealth management interfaces in Germany, uses Gemini and DataStax Astra DB to deliver next-gen financial insights in real time to millions of customers for personalized guidance at scale.


### **Employee Agents**

- **Allegis Group**, a global leader in talent solutions, partnered with TEKsystems to implement AI models to streamline its recruitment process, including automating tasks such as updating candidate profiles, generating job descriptions, and analyzing recruiter-candidate interactions. The implementation resulted in significant improvements in recruiter efficiency and a reduction in technical debt.

- \* **Altumatim**, a legal tech startup, uses a platform powered by Gemini on Vertex AI to analyze millions of documents for eDiscovery. This accelerates the process from months to hours, improves accuracy to over 90%, and enables attorneys to focus on building compelling legal arguments.

- \* **Anara**, a generative AI research assistant, helps users find and understand scientific documents with verifiable AI summaries and insights. It uses Google Cloud's scalable infrastructure, AI Studio, and Cloud Functions to power its models and data processing for a global user base.

- **BCG** uses Google Cloud to provide a sales optimization tool that improves the effectiveness and impact of insurance advisors.

- **Beyond** is a technology consultancy that guides their clients through transformational journeys to unlock the potential of AI and cloud-based technology. Google Workspace with Gemini helps them reduce the time from project brief to project kickoff from months to weeks, and the time for first drafts of RFI responses from days to minutes.

- **Cintas** is using Vertex AI Search to develop an internal knowledge center for customer service and sales teams to easily find key information.

- \* **Croud**, a global media agency specializing in performance and brand marketing, uses Gemini in Google Workspace to conduct deep research, analyze data, and complete research, planning, strategy, and note-taking tasks at the click of a button. Work that once required multiple handoffs can now be done independently, freeing employees for creative and strategic priorities.

- **Dun & Bradstreet**, a business research and intelligence service, built an email-generation tool with Gemini that helps sellers create tailored, personalized communications to prospects and customers for its research services. The company also developed intelligent search capabilities to help users with complex queries like, "Find me all the companies in this area with a high ESG rating."

- **Cognizant** used Vertex AI and Gemini built an AI agent to help legal teams draft contracts, assign risk scores and make recommendations for ways to optimize operational impact.

- **Finnit**, part of the Google for Startups Cloud AI Accelerator, provides AI automation solutions for corporate finance teams, helping to cut accounting procedures time by 90%, boost accuracy, and unlock unique insights.

- **Flashpoint** is improving efficiency and productivity across its workforce, using Google Workspace to communicate and collaborate more effectively, maximize ROI, and increase employee satisfaction, so they can dedicate more time to keeping customers secure.

- **Fluna**, a Brazilian digital services company, has automated the analysis and drafting of legal agreements using Vertex AI, Document AI, and Gemini 1.5 Pro, achieving an accuracy of 92% in data extraction while ensuring security and reliability for sensitive information.

- \* **Freshfields**, a global law firm with over 280 years' experience, uses Gemini to power Dynamic Due Diligence, its proprietary tool designed to enhance legal reviews and due diligence. The AI significantly improves the scale, accuracy, and efficiency of these processes, addressing repetitive legal workflows that can drain productivity.

- \* **Freshfields** also uses NotebookLM to quickly synthesize large quantities of information and uncover new insights. The AI helps employees process complex legal information more efficiently in their daily workflows.

- \* **Gelato**, a Norwegian software company enabling local production for global ecommerce through 140+ printers in 32 countries, uses Gemini models to automate engineering ticket triage and customer error categorization. The AI-powered system increased ticket assignment accuracy from 60% to 90% and reduced the time to deploy ML models from two weeks to one or two days using Vertex AI.

- \* **Harvey**, a legal AI company, uses Gemini 2.5 Pro on Vertex AI to automate complex document reviews, a major pain point in the legal industry. The platform provides domain-specific AI that can reason over hundreds of pages of materials, enabling legal professionals to maximize efficiency and focus on strategic work.

- \* **Inspira**, a legal tech company, tackles the time-intensive challenge of legal document analysis by providing lawyers with an AI-powered solution built on Google Cloud. Leveraging Gemini, Vertex AI, and BigQuery, Inspira's platform automates legal document search, analysis, and drafting to reduce workflow times by 80%, allowing lawyers to find answers and relevant decisions in minutes or hours instead of weeks.

- \* **Instalily** uses Google Cloud with Gemini 2.5 and Vertex AI to power InstaWorkers that transform sales, service, and operations. At a leading field service provider, InstaWorkers cut the technician’s diagnosis time from 15 minutes to under 10 seconds, lowered serving costs by 98 percent, and drove a 99 percent improvement in end-to-end workflow speed.

- **Joe the Architect**, a 25-person architecture firm, catches up on long email chains with Gemini in Gmail to keep track of client needs across dozens of conversations.

- **KPMG** is building Google AI into their newly formed KPMG Law firm, as well as driving AI transformation within the banking industry, and the company is also implementing Agentspace to enhance its own workplace operations.

- **L+R**, a design and technology agency, leverages Gemini for Google Workspace Workspace to elevate performance and precision, streamlining workflows and empowering its team to achieve more impactful results.

- \* **Markups.ai**, an AI contract negotiation agent, turns a days-long human legal review into a minute(s) automated process. By simply emailing a contract, clients receive customized revisions and analysis almost instantly. Gemini 2.5 Pro enabled us to go from handling only first revisions of NDAs, to any revision of any contract (MSAs, DPAs, etc.).

- \* **MAS**, a global experiential marketing agency, uses Gemini's "help me write" and "take notes for me" features to iterate faster in their creative workflows. The AI tools help the team work more efficiently while maintaining their "one brain" approach to collaboration.

- \* **MERGE**, a marketing and technology agency for health and wellness brands, uses Gemini to summarize meetings with clear action items and collaborate with clients in real time in Google Docs. The real-time collaboration ensures alignment and saves hours on content rework, contributing to a 33% improvement in turnaround times.

- **Monks** used Google Gemini to help Hatch build a personalized ad campaign. The campaign delivered an 80% improved click-through rate, 46% more engaged site visitors, and a 31% improved cost-per-purchase over other campaigns. On top of this, by using AI the team was able to deliver the campaign much more efficiently, reducing time to investment by 50% and costs by 97%.

- \* **ObraJobs**, a job platform, connects candidates with relevant opportunities, streamline the hiring process, and deliver personalized recommendations for both job seekers and employers. Obra uses Vertex AI to power candidate matching and personalized job recommendations, supported by Cloud Storage, Cloud Run, Cloud Scheduler, Cloud Tasks, and Firestore.

- **Own Your Brand** founder Lauren Magenta uses Google Workspace to run her business and Gemini for Google Workspace is transforming how she manages enrollment. Gemini helps her quickly draft personalized emails to potential clients in her own voice.

- \* **Provenbase** has built its talent recruitment tool for businesses on Google Cloud and is now powering its transformative Deep Search for talent feature using Google Cloud AI.

- **Randstad**, a large HR services and talent provider, is using Gemini for Workspace across its organization to transform its work culture, leading to a more culturally diverse and inclusive workplace that’s seen a double-digit reduction in sick days.

- \* **Sonata** **Design**, a design company focused on discovering the value and beauty of client spaces, uses NotebookLM to create a centralized database of product specifications and technical details. The AI tool reduces questions to senior management, improves employee self-service, and enhances knowledge sharing across the team.

- \* **Square** **Management**, a consultancy serving high-demand industries like banking, luxury, and aerospace, uses Gemini in Google Workspace to identify the most suitable consultants for client needs and optimize work methods. The AI helps the company better respond to client challenges while ensuring full GDPR compliance with secure data handling.

- \* **Story**, an intellectual property startup that powers licensing and monetization services, is working with Google Cloud’s web3 services and infrastructure to bring new capabilities to developers on its platform.

- **Sulamérica** adopted Google Workspace a decade ago to make collaboration among employees more agile, intuitive, and fluid. The insurance company recently started using Gemini in Workspace, making it available to 1,250 employees to increase operational efficiency, security, and productivity.

- \* **Transcom**, a global outsourcing company, uses NotebookLM to simplify customer research and bid processes. The AI tools are deeply embedded into workflows, helping the company improve customer interactions while maintaining top-tier security standards.

- \* **Transcom** also uses Gemini in Google Workspace to speed up agent training and help employees across all levels find creative solutions to challenges and validate decisions. The AI enhances daily work and accelerates training processes within the familiar Google Workspace platform.

- \* **Upwork**, the world's human and AI-powered work marketplace, connects businesses with independent professionals. By leveraging Vertex AI Text to Speech API, Upwork delivers faster, more accurate talent matching and hiring efficiency for clients and freelancers.

- \* **Wotter**, an employee engagement platform, uses a Gemini-powered smart assistant and Google Cloud's robust AI capability to provide real-time insights into employee sentiment. It accurately predicts flight risks and offers actionable "Wott-if" scenarios, enabling leaders to build a data-driven people strategy.

- \* **Zoi**, an international IT consultancy with 500 employees across 30 nations, uses Gemini in Google Workspace to provide real-time translation and enable seamless communication across global teams. The AI helps unify teams and improve workflows while maintaining security across diverse, international operations.

- **UKG**, an HR and workforce management solutions provider, enhances the workplace experience with UKG Bryte AI, a trusted conversational agent built with Google Cloud that enables HR administrators and people managers to request information about company policies, business insights, and more.


### **Creative Agents**

- **\*AdVon** **Commerce** uses Gemini and Veo to enhance product detail pages for major retailers, processing a 93,673-product catalog in under a month (a task that previously took up to a year) and generating engaging lifestyle videos that demonstrate product functionality. For one sporting goods client, the AI-powered solution increased top search rank placements by 30% and boosted average daily sales by 67%, delivering a $17 million revenue lift in just 60 days.

- **Agoda** is a digital travel platform that helps travelers see the world for less with its great value deals on a global network of over 4.5M hotels and holiday properties worldwide, plus flights, activities, and more. They’re now testing Imagen and Veo on Vertex AI to create visuals, allowing Agoda teams to generate unique images of travel destinations which would then be used to generate videos.

- \* **Comeen**, serving major clients like Veolia, Auchan, and Sanofi across 42 countries, uses Gemini AI to generate multilingual subtitles for workplace videos in 40 languages with one click. The feature eliminated the multi-day, multi-vendor process that previously made content obsolete before publication, enabling instant subtitle generation integrated directly into Google Workspace.

- \* **Dentsu Digital** provides digital transformation, communications, and marketing services for enterprise clients, using Vertex AI and PaLM 2 to build their "∞AI" service brand that supports advertising generation, customer service chatbots, and sales support. The platform has been adopted by over 100 companies and enabled the team to launch production systems in six months instead of the two years traditional development would have required.

- \* **Hotmob**, a Hong Kong-based data-centric media company, uses Vertex AI with Gemini models to power Caterpillar AI, a marketing tool that generates personalized text and images for specific audience personas and distribution channels. The platform enhanced marketing teams' productivity by 33%, reduced admin workloads by 50%, and enabled customers to increase posting frequency from three to 12 posts per week.

- \* **MAS**, a global experiential marketing agency, uses Gemini as a creative accelerator and idea generator, having collaborative conversations with the AI to refine ideas, bring concepts to life, and share ideas in impactful ways. The director of creative brings human input and generative AI output into harmony through an iterative process.

- \* **MERGE**, a marketing and technology agency for health and wellness brands, uses Gemini integrated across Google Workspace to generate AI-powered templates for strategy documents, project briefs, and creative briefs that include customer data and ideas. The agency achieved an 89% sustained usage rate during a three-month pilot and improved turnaround times for client work by 33%.

- \* **Monday.com**, a work management platform trusted by more than 245,000 customers worldwide, leverages Veo to produce training videos, social content, and internal communications in a fraction of the time — empowering all employees, not just designers, to move faster and focus on impact.

- **Quom**, a financial inclusion specialist in Mexico, has developed AI-powered conversational agents that optimize and personalize user and customer support.

- **Salesrun**, the world’s first dedicated sales activity suite, sees Google Cloud gen AI as an alternative for analyzing information related to purchasing habits, enabling the optimization of cash flow and boosting sales for its retail customers.

- **Thoughtworks** is a global technology consultancy that helps businesses use technology to solve problems and innovate. They use Google Workspace with Gemini to improve internal and external communication across their company, including in non-native languages — from emails to documents and blogs.

- \* **WITHIN**, a performance branding agency serving brands from startups to global enterprises, uses Gemini in Google Workspace to enable scalable creative production, rapid ideation, and efficient data analysis. The AI reduces time spent on manual tasks and addresses open-ended client questions in minutes, a task that previously took hours.

- **Yazi** turns to Google Workspace with Gemini to accelerate marketing efforts so they can launch products faster; their dev teams also use it to write and deploy more code.


### **Code Agents**

- **Capgemini** has been using Code Assist to improve software engineering productivity, quality, security, and developer experience, with early results showing workload gains for coding and more stable code quality.

- **Tata Consultancy Services** ( **TCS**) helps build persona-based AI agents on Google Cloud, contextualized with enterprise knowledge to accelerate software development.


### **Data Agents**

- **The Colombian Security Council** developed a generative AI-based chatbot to improve data analysis and its chemical emergency management processes, allowing for quick responses to urgent situations.

- **Contraktor** developed a project to analyze contracts with AI. As a result, the company achieved a reduction of up to 75% in the time taken to analyze and review a contract, with the possibility of both reading and extracting relevant data from the documents.

- \* **Croud**, a global media agency with over 650 employees specializing in performance and brand marketing, uses custom Gems for email sentiment analysis, complex data analysis, coding assistance, and supplier-specific data workflows. The AI enables employees to execute repeatable tasks independently, achieving 4-5X productivity improvements for certain tasks.

- \* **Galaxies** uses BigQuery, Vertex AI, and Cloud Storage to create "Synthetic Personas" powered by advanced clustering and LLMs trained exclusively on proprietary data, enabling marketing campaigns to be tested with hundreds of profiles in 48 hours instead of months. The Google Cloud migration achieved 85% savings in direct research costs while providing an integrated environment for data lake, data warehouse, machine learning, and generative AI operations.

- **Gamuda Berhad**, a Malaysian infrastructure and property management company, has developed Bot Unify, a platform that democratizes generative AI to allow users access to Gemini models and RAG frameworks to provide faster information and insights during construction projects.

- \* **Gazelle**, an AI service automating property documentation for real estate agents in Sweden and Norway, uses Gemini models to extract key information from lengthy property documents and generate sales content. The platform increased output accuracy from 95% to 99.9%, reduced content generation time from four hours to 10 seconds, and enabled the launch of four new products in less than a year.

- **Habi**, a Colombian real estate company, has implemented AI solutions to streamline and automate the management and verification of physical and digital documents. This improved validation operations and increased the efficiency and adaptability of employees.

- **HCLTech**, an industry-leading global technology company, launched HCLTech Insight — a manufacturing quality AI agent that helps predict and eliminate different types of defects on manufacturing using Vertex AI, Google Cloud’s Cortex Framework, and the Manufacturing Data Engine platform.

- **IPRally** built a custom machine-learning platform that uses natural language processing on the text of more than 120 million global patent documents, creating an accurate, easily searchable database that adds more than 200,000 new sources a week.

- **Ipsos** built a data analysis tool for its teams of market researchers, eliminating the need for time-consuming requests to data analysts. The tool is powered by Gemini 1.5 Pro and Flash models, as well as Grounding with Google Search, to enhance real-world accuracy from contemporaneous search information.

- **Juganu**, a SaaS provider for smart cities and smart stores, is working with Google Cloud to automate and digitize the physical store. The company has begun developing digital twins that give retailers virtual eyes in the store to help automate routine tasks, improve efficiency, and deliver better customer experiences.

- \* **Leads.io**, a performance marketing company, uses Vertex AI and Gemini to manage thousands of personalized marketing campaigns and automate lead qualification. This has reduced the time to integrate data from new acquisitions from several months to just a few days.

- **Nowports** is harnessing the power of AI to revolutionize logistics and stand out from the competition. By analyzing key operational information, they aim to accurately predict market behavior, optimizing their entire supply chain.

- \* **Persol Career** built a unified HR data platform using BigQuery, Cloud Run, and Cloud Functions to consolidate data from over 70 HR systems, reducing data collection time from weeks to just a few days. The company integrated Looker for secure data visualization with row-level access controls, enabling HR analysts to spend more time on strategic analysis instead of manual data collection and processing.

- \* **Populix**, Indonesia's leading consumer insight platform with a panel of 1 million respondents, migrated to Google Cloud and built an AI research assistant using Gemini and Vertex AI to automate survey creation and analysis. The company sped up delivery time for end-to-end research by over 50% and reduced QA time by 40%.

- \* **Precis** **Digital**, a Stockholm-based digital marketing agency, built its Alvie data platform on BigQuery and Cloud Run, enabling it to launch to its entire customer base overnight. With just 15 developers, the company runs hundreds of thousands of jobs daily and uses Gemini to automatically populate form data in 300 milliseconds.

- **Servicios** **Orienta**, a Mexican personal wellness and organizational efficiency company, has adopted AI-based solutions to analyze large volumes of data, interpret results, and provide recommendations that enhance the customer experience.

- \* **Sojern**, a leading digital marketing platform for the travel industry, built its AI-driven audience targeting system on Vertex AI and Gemini, processing billions of real-time traveler intent signals to generate more than 500 million daily predictions. The company reduced audience generation time from two weeks to less than two days while helping clients achieve a 20-50% improvement in cost-per-acquisition.

- \* **Wisesight**, a Thailand-based social media analytics and marketing consultancy established in 2007, uses Gemini on Google Cloud to analyze large volumes of social voice data and deliver intelligent insights to clients. The platform reduced research, insights, and content creation time from two days to just 30 minutes, making data analysis accessible even to individuals with no prior data analysis experience.

- \* **WITHIN**, a performance branding agency, uses NotebookLM to generate insights rooted in first-party data to stay aligned with client specifics, and creates custom Gems based on its unique agency perspective to ensure brand consistency. The AI tools help the team deliver impactful results and maximize client ROI across global teams in a hybrid work environment.

- **Workday** is using natural language processing in Vertex AI Search and Conversation to make data insights more accessible for technical and non-technical users alike.

- \* **XEBO.ai**, an AI-powered experience management platform founded in 2018 in India, integrated Gemini into its platform to analyze large volumes of customer survey data and derive actionable insights for businesses. The company achieved a 20% increase in overall productivity by completing tasks in minutes that previously required hours, while also reducing time spent on operational tasks by 30%.

- **Zenpli**, a digital identity partner for other businesses, leverages the multimodal capabilities of the models available in Vertex AI to provide its clients with a radically enhanced experience: a 90% faster onboarding process with contracts, a 50% reduction in costs thanks to AI-powered automation, and superior data quality that ensures regulatory compliance.

- \* **Zoi** uses Gemini to provide AI-powered search for enhanced data insights and AI assistance in document creation. The technology democratization empowers employees to unlock new value and break down data silos that hinder digital transformation.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Financial_Services.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Financial_Services.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Financial_Services.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Financial_Services.max-900x900.jpg)

Financial Services

### **Customer Agents**

- **\*Albo**, a Mexican neobank, uses Gemini models to power its "Albot" AI chatbot that provides 24/7 financial advice, customer onboarding, and support to millions of first-time banking users. The platform advances financial inclusion while streamlining regulatory compliance and improving operational efficiency.

- **Apex** **Fintech** **Solutions** is leveraging Google Cloud to power seamless access, frictionless investing, and investor education at scale. Using BigQuery, Looker, Google Kubernetes Engine, Apex is enhancing accessibility to financial insights while laying the groundwork for AI-driven innovation.

- **Banco Covalto** in Mexico is transforming its operations with gen AI to streamline processes and enhance customer experience, reducing credit approval response times by more than 90%.

- \* **Banco** **Macro**, Argentina's leading private national bank with over 6 million customers, uses BigQuery, Vertex AI, and Gemini to power conversational AI assistants for customer service and enable 30+ business domains to create and share machine learning models. The platform accelerated data processing times, allowing teams to generate data products at previously unimaginable speeds.

- **Bud** **Financial** uses its Financial LLM, powered by Gemini models, to provide personalized answers to customer queries and automate banking tasks, such as moving money between accounts to avoid overdrafts.

- \* **Commerzbank** were early adopters of Customer Engagement Suite, using it to build Bene, their own specialized chatbot. They are now leveraging Gemini to further enhance the experience, enabling it to handle over 2 million chats and successfully resolve 70% of all inquiries.

- **Contabilizei** is improving customer service in Brazilian financial services with “The Concierge,” its AI solution powered by Vertex AI. Using tools like Vertex AI Search and Model Garden, the platform delivers fast, personalized responses.

- \* **Definity**, with help from Google Cloud partner Deloitte, leverages Google’s AI capabilities to summarize calls, automate caller authentication, analyze customer sentiment, and provide real-time recommendations to contact center team members — reducing call handle times by 20% and boosting productivity by 15%.

- **Discover** **Financial** has created the Discover Virtual Assistant, powered by generative AI, that can assist customers directly and provide additional information to Discover service agents, delivering smoother, more efficient, and more satisfying interactions to customers around the world — in whatever channel they prefer.

- **Figure**, a fintech offering home equity lines of credit, leverages Gemini’s multimodal models to create AI-powered chatbots that help streamline, simplify, and accelerate lending experiences for both consumers and employees.

- **Fundwell** helps businesses secure the funding they need to grow with speed and confidence. Utilizing Google Cloud, Fundwell simplifies the customer journey by analyzing financial health with AI to match businesses with their ideal funding solution.

- **ING** **Bank** aims to offer a superior customer experience and has developed a gen AI chatbot for workers to enhance self-service capabilities and improve answer quality on customer queries.

- \* **Loft** migrated 100% of its real estate technology platform data to Google Cloud in two phases over three months, implementing BigQuery for data analytics and Gemini 2.0 Flash for AI-powered features. The migration delivered a 40% reduction in costs and 15% reduction in customer support tickets, while enabling 900 weekly mortgage simulations via WhatsApp and connecting 9,000 real estate agencies with improved usability and response speed.

- \* **OneUnited Bank**, America's largest Black-owned bank, deployed Contact Center AI and Dialogflow to automate customer support workflows after its customer base doubled in 60 days in 2020. The bank reduced call resolution time from six to four minutes and cut agent onboarding time from four to six weeks down to one to two weeks.

- **Safe** **Rate**, a digital mortgage lender, is using Gemini models to create an AI mortgage agent that includes gen AI chat features like “Beat this Rate” and “Refinance Me;” these help borrowers quickly compare different rates and get personalized quotes in under 30 seconds.

- **Scotiabank** is using Gemini and Vertex AI to create a more personal and predictive banking experience for its clients, including powering its award winning chatbot, which continues to elevate the bank's digital offerings and highlights the value of AI technology to enhance the digital client experience.

- **SEB**, a Nordic corporate bank, has support from Bain & Company to develop an AI agent for the wealth management division. The agent, built with Google Cloud, enhances end-customer conversations with suggested responses and generates call summaries, helping to increase efficiency by 15%.

- **United** **Wholesale** **Mortgage** is transforming the mortgage experience with Vertex AI, Gemini, and BigQuery, already more than doubling underwriter productivity in just nine months, resulting in shorter loan close times for 50,000 brokers and their clients.

- **Wayfair** automates its product catalog enrichment and now updates product attributes 5x faster, achieving significant operational cost savings.


### **Employee Agents**

- **ATB Financial**, a leading financial institution in Alberta, Canada, has successfully deployed Google Workspace with Gemini to its more than 5,000 team members, allowing them to automate routine tasks, access information quickly, and collaborate more effectively, all while ensuring data is secure and trustworthy.

- **Banco** **BV** implemented Agentspace, enabling its employees to use gen AI technologies for research, assistance, and operations across several of its critical systems, in a secure and compliant manner.

- **Banco** **Rendimento**, a currency exchange market, is using Vertex AI and other solutions to create a service that enables sending international transfers through WhatsApp, delivering 24/7 service without requiring a representative to complete the transaction.

- **Banestes**, a Brazilian bank, used Gemini in Google Workspace to streamline work dynamics, such as accelerating credit analysis by simplifying balance sheet reviews and boosting productivity in marketing and legal departments.

- **Bank of New York Mellon** built a virtual assistant to help employees find relevant information and answers to their questions.

- **\*BBVA**, a global bank with 100,000 employees in more than 25 countries, uses Gemini in Google Workspace to summarize, draft, and find information across emails, chats, and files, and create professional documents, presentations, spreadsheets, and videos. Employees report that automating repetitive tasks with AI saves them nearly three hours per week on average.

- **\*BBVA**, also uses NotebookLM for research tasks, generating audio overviews of complex findings, and creating reports. The AI-powered research and writing assistant helps employees free up time for more strategic, customer-focused work.

- \* **Chiba** **Bank**, a major regional bank in Japan, partnered with Google Cloud's Advanced Solutions Lab to train employees in AI and machine learning. They built a Gemini Pro-based chatbot prototype that answers questions about internal banking policies and procedures and enables employees to access policy information through natural language queries.

- **Citi** uses Vertex AI to deliver gen AI capabilities across the company, fueling generative AI initiatives related to developer toolkits, document processing, and digitization capabilities to empower customer servicing teams.

- **Commerzbank**, a leading German bank, implemented an AI agent powered by Gemini 1.5 Pro to automate the documentation of client calls, freeing up its financial advisors from tedious manual processes; a significant reduction in processing time allowed advisors to focus on higher-value activities like building client relationships and providing personalized advice.

- **DBS**, a leading Asian financial services group, is reducing customer call handling times by 20% with Customer Engagement Suite.

- **Deutsche** **Bank** has created DB Lumina, an AI-powered research tool that accelerates the time it takes financial analysts to create research reports and notes. Work that used to take hours or even days can now be completed in a matter of minutes, all while maintaining data privacy requirements for the highly regulated financial sector.

- **Discover Financial** helps its 10,000 contact center representatives to search and synthesize information across detailed policies and procedures during calls.

- \* **Equifax** a global credit bureau, uses Gemini's "take notes for me" feature in Google Meet to create transcripts, summaries, and action items from calls, putting all details in one place to share with anyone who misses a meeting. During a trial, 97% of participants wanted to keep their Gemini licenses after experiencing the productivity benefits.

- **\*Equifax** also uses Gemini to help help desk representatives look deeper at data to determine how to improve the service they provide to end users. During a trial with over 1,500 participants, 90% saw an increase in work quality and quantity, and employees from nearly all business units saved more than one hour per day.

- **FinQuery**, a fintech company, is using Gemini for Google Workspace as a valuable productivity and collaboration tool to help in brainstorming sessions, draft emails 20% faster, manage complex cross-organizational project plans, and aid engineering teams with debugging code and evaluating new monitoring tools.

- **Five** **Sigma** created an AI engine which frees up human claims handlers to focus on areas where a human touch is valuable, like complex decision-making and empathic customer service. This has led to an 80% reduction in errors, a 25% increase in adjustor’s productivity, and a 10% reduction in claims cycle processing time.

- **Generali** utilizes Vertex AI and Google Cloud solutions to enable salespeople to access policy information instantly through natural language queries.

- \* **Hang** **Seng** **Bank**, Hong Kong's largest local bank, is using Vertex AI to power a new knowledge management platform, which enables contact center representatives to easily retrieve information with AI-powered search from millions of documents around products and regulations.

- **HDFC** **ERGO**, India's leading non-life insurance company, built a pair of insurance "superapps" for the Indian market. On the 1Up app, the insurer leverages Vertex AI to give insurance agents context-sensitive "nudges" through different scenarios to facilitate the customer onboarding experience.

- **HDFC ERGO** also runs advanced data insight from BigQuery through Vertex AI to drive highly personalized offerings for consumers in specific geographical locations.

- **Hiscox** used BigQuery and Vertex AI to create the first AI-enhanced lead underwriting model for insurers, automating and accelerating the quoting for complex risks from three days down to a few minutes.

- **Loadsure** utilizes Google Cloud's Document AI and Gemini AI to automate insurance claims processing, extracting data from various documents and classifying them with high accuracy. This has led to faster processing times, increased accuracy, and improved customer satisfaction by settling claims in near real-time.

- **Macquarie Bank** uses Google Cloud AI to enable efficient and proactive fraud protection and digital self-service capabilities — their Help Centre Search directed 38% more users towards self-service and they reduced false positive alerts for client protection by 40%.

- **Multimodal**, part of the Google for Startups Cloud AI Accelerator, automates complex financial services workflows with multimodal AI agents that can process documents, query databases, power chatbots, make decisions, and generate reports.

- **OSTTRA** chose Google Workspace to boost teamwork, and Gemini is now helping automate tasks like writing proposals and generating interview questions, using features like “Help me write” to save employees time and increase productivity.

- **Pinnacol** **Assurance**, Colorado’s largest worker’s compensation carrier, leans on Gemini to accelerate repetitive tasks, such as creating questions for client interviews and digging deeper into insurance claims, with 96% of surveyed employees reporting time savings.

- \* **Plutos** **ONE**, a licensed Bharat bill payment system provider and India's largest merchant-funded offers platform with 400+ online brands, migrated to Google Cloud to meet regulatory compliance requirements. The company reduced audit preparation time by 40%, cut security incident response times by over 50%, and achieved 25% lower operational costs compared to on-premise alternatives.

- \* **Qualia Clear** is an agentic system that transforms real estate closings by automating manual title & escrow workflows. It uses tool calling, Gemini 2.5 Flash & Pro, and Google Agent Development Kit to process emails and documents and simplify reporting, improving efficiency and customer service.

- \* **Questrade Financial Group**, a Canadian financial services company, uses Gemini in Google Workspace to generate speaker notes for presentations, brainstorm ideas, conduct research, and summarize documents. Gems help write blog posts in a couple of hours that previously took two days to research and write.

- \* **Questrade Financial Group** also uses Gemini to synthesize information from various files on Google Drive and NotebookLM to generate engaging audio versions of lengthy reports. Employees can listen to audio versions while performing other tasks, boosting productivity and saving time searching for relevant material.

- \* **Rogo**, an AI platform for Wall Street serving 6,000+ investment bankers and analysts, uses Gemini 2.5 Flash and Vertex AI to automate financial workflows including building slide decks, generating company profiles, and drafting investment memos. Switching to Gemini 2.5 Flash reduced hallucination rates from 34.1% to 3.9% while supporting 10x growth in tokens per query, giving Rogo's team trust in the platform's accuracy for critical financial analysis.

- **ROSHN** **Group**, one of Saudi Arabia’s leading property developers has built RoshnAI, an internal assistant that leverages a combination of AI model that include Gemini 1.5 Pro and Flash to generate valuable insights from ROSHN's internal data sources for its employees.

- \* **Seguros** **Bolivar**, an insurance provider in Colombia, uses Gemini to streamline collaboration when designing insurance products with partner companies, achieving faster turnaround times and greater alignment. Since adopting Google Workspace and Gemini, the company has reduced costs by 20-30% and improved cross-company collaboration.

- \* **Stacks**, an Amsterdam-based accounting automation startup founded in 2024, built its AI-powered platform on Google Cloud using Vertex AI, Gemini, GKE Autopilot, Cloud SQL, and Cloud Spanner to automate monthly financial closing tasks. The company reduced closing times through automated bank reconciliations and workflow standardization, with 10-15% of its production code now generated by Gemini Code Assist.

- \* **Stream** offers financial tools to employers and employees and is using Gemini models to handle more than 80% of its internal customer inquiries, including questions about pay dates, balances, and more.

- **Symphony**, the communications platform for the financial services industry, uses Vertex AI to help finance and trading teams collaborate across multiple asset classes.

- **Tributei** was founded in 2019 to simplify the complex tax assessment processes for Brazil’s state VAT. ML resources help Tributei simplify not only tax assessments but also tax management tasks, with performance improved by 400%. This initiative has already helped 19,000 companies automate and audit VAT-related transactions, spotting more than BRL 15 million in tax overcharges.

- **The Trumble Insurance Agency** is using Gemini for Google Workspace to significantly improve its creativity and the value that it delivers to its clients with enhanced efficiency, productivity, and creativity.

- **wealth.com** built a platform that simplifies estate planning while equipping financial advisors with powerful tools to visualize and manage complex plans. Its new AI-powered Ester chat agent helps accurately and securely extract information from complex and lengthy planning documents, like trusts and wills.

- **Wells Fargo** will be deploying Agentspace across the company to streamline internal operations, shorten decision times, and transform how it serves customers.

- \* **Wells** **Fargo** also uses Apigee API Management to scale generative AI adoption across teams by building task-specific, reusable APIs that simplify experimentation and model integration. The company deployed a RAG-based tool for branch bankers that retrieves policies and procedures during customer interactions, reducing workflow for query resolution by approximately 20%.

- \* **Worldline**, a global payment services company founded in 1972 that operates in 56 countries and processes millions of secure transactions daily, is migrating its North American payment platform infrastructure to Google Cloud using Security Command Center and Cloud Identity for enhanced security and compliance visibility. The migration is expected to generate significant annual infrastructure cost savings while accelerating development cycles from quarterly releases to continuous deployment.


### **Creative Agents**

- \* **ATB Financial**, the largest Alberta-based financial institution with over $62.3 billion in assets under management, uses Gemini to help marketing teams brainstorm new campaigns without waiting for subject matter experts. The AI reduced project timelines by up to two weeks, with 40% of team members using Gemini daily and saving approximately two hours per week.

- \* **Chiba Bank**, a major regional bank in Japan, partnered with Google Cloud's Advanced Solutions Lab to train employees in AI and machine learning. They developed an AI system prototype that generates advertising creative content from text and image prompts.

- \* **eToro**, a global trading and investing platform, has pioneered a groundbreaking approach to marketing by using Veo to create advertising campaigns. This enables eToro to rapidly generate professional-quality, culturally specific video content across the global markets it serves, which would traditionally require extensive production timelines and significant budgets.


### **Code Agents**

- **CME Group**, which operates the Chicago Mercantile Exchange, says most developers using Gemini Code Assist report a productivity gain of at least 10.5 hours a month.

- **Commerzbank** is enhancing developer efficiency through Code Assist's robust security and compliance features.

- **\*Questrade Financial Group**, a Canadian financial services company, uses Gemini with AppSheet to enable less technical users to create intelligent applications, building solutions and workflows in minutes that previously took hours. The AI democratizes coding by making app development accessible to business users without technical backgrounds.

- **Regnology**, a provider of regulatory reporting services, built its Ticket-to-Code Writer tool with Gemini 1.5 Pro to automate the conversion of bug tickets into actionable code, significantly streamlining the software development process.

- **ROSHN Group** is using Gemini Code Assist and Cloud Assist to increase the productivity of its engineers who are working on its unique real estate shopping website and app; shortly after launch, the organization was able to register 45,000 new users and conduct 9,400 completed purchases digitally.


### **Data Agents**

- \* **ATB Financial**, the largest Alberta-based financial institution with over $62.3 billion in assets under management, uses Gemini integrated with Google Sheets to provide analysts with fast access to formulas. The AI helps reduce routine work, with team members saving approximately two hours per week and 40% using Gemini daily.

- \* **Bud Financial**, a data intelligence provider focused on banking clients, leverages DataStax Astra DB on Google Cloud with Gemini. The platform enables ultra-fast processing of complex financial data, helping clients reduce fraud by over 90% and shortening the time required to access critical data analytics from weeks to minutes.

- \* **Carbon** **Underwriting**, a Lloyd's of London syndicate, uses Gemini to automate complex tasks like categorizing claim descriptions and occupancy data — processes that previously required months of manual data science work but now deploy in days. The company built its Graphene platform on BigQuery and Google Cloud, enabling a lean team of three engineers to scale Gross Written Premiums from £15 million to over £300 million in five years while reducing data processing time from days to hours.

- \* **Causal**, a financial planning platform, uses Cloud SQL and Gemini models to power its data foundation and accelerate innovation. By offloading database management, the company built an AI-powered wizard that helps users connect data, analyze patterns, and generate financial models in just five minutes.

- **CERC**, a Brazilian financial infrastructure company, manages more than 500 million daily transactions using Databricks, BigQuery, and Gemini. This increased processing capacity by 10x without adding to the workforce, allowing the company to process millions in revenue forecasts in just two minutes and accelerate analytics for customers.CERC now processes 100,000 transactions per second with its infrastructure on Google Cloud.

- **Ci Banco** leverages Google Cloud technologies across more than 50 projects, including a document management system powered by Vertex AI. This system has optimized the document review process for their trust authorization procedures, reducing the time from one week to less than two hours.

- **Citadel****Securities**, a top financial institution, uses Google's AI Hypercomputer and TPU chips for market data modeling and training, resulting in improved performance, scaling, and costs.

- **CME Group** is building a first-of-its-kind cloud-based commodities trading platform with AI tools built-in, offering CME’s trading customers access to deeper insights and smarter trades as well as rapid experimentation on new trading strategies that won’t interrupt existing trade flows.

- **Digits** developing next-gen accounting software for startups and small businesses. Using AI-driven bookkeeping, expense management, and financial analysis, Digits enables business owners to achieve financial clarity and focus on growth.

- **Dojo** is enabling millions of secure, reliable, and ultra-fast payment experiences daily, empowering businesses to serve more customers. Dojo is leveraging Google Cloud gen AI services like Looker and Gemini models to explore innovative use cases that offer more intuitive, natural ways to engage with payment data.

- \* **Fiscal.ai** is reinventing financial data infrastructure. Its AI-native platform transforms unstructured public filings into clean, standardized data in minutes, replacing the slow, error-prone legacy of manual aggregation and delivering the mission-critical insights that today's top investors demand.

- \* **Fundwell**, a business financing platform connecting over 5,000 businesses with funding partners, uses Vertex AI to build Nebula, a document intelligence application that automates financial document analysis and risk assessment. The AI-powered system supports funding disbursement in as little as 24 hours and has generated $22 million through a self-serve customer portal.

- **Generali Italia**, Italy's largest insurance provider, used Vertex AI to build a model evaluation pipeline that helps ML teams quickly evaluate performance and deploy models.

- \* **Grupo** **Quom**, a Mexican holding company operating payment platform Tekae for 100,000 businesses, migrated to Google Cloud to reliably process over 1,000,000 daily transactions that previously caused service outages during traffic spikes. The migration reduced operational costs by 40% to 60% while completely eliminating downtime, and positioned Quom as an AI early adopter by purchasing one of the first 10 Gemini licenses.

- **Hiperstream** is using Gemini to analyze specific information and automatically categorize it, resulting in a 200% increase in the performance of data flows and communications for its financial and B2B customers.

- **Intesa Sanpaolo** built its Democratic Data Lab using data analytics and AI to enable its risk management team to keep up with the rapid changes and complexity of modern financial markets. By democratizing access to data, the Democratic Data Lab is empowering other departments across the bank to have more oversight and control of risks.

- **Kredito**, a Chilean fintech pioneer in online lending, created an AI-based risk assessment model that improved the prediction of payment behaviors and helped clients access working capital more quickly.

- \* **Lloyds** **Banking** **Group**, the UK's largest digital bank, uses Vertex AI to scale machine learning experimentation across over 300 data scientists and AI developers. The bank reduced income verification in mortgage applications from days to seconds, while launching 18 GenAI systems into production across its business.

- \* **M-DAQ Global**, a fintech group specializing in foreign exchange and cross-border payment solutions, uses Vertex AI and Google Kubernetes Engine to power its AI-driven Know Your Business (KYB) compliance solution. The natural language processing-based system automates compliance tasks and improves productivity by 30 times, reducing onboarding times and eliminating manual bottlenecks in customer verification.

- **Macquarie** in Australia has been using predictive AI to clean and unify 100% of its data, so teams can then draw insights using gen AI tools in Vertex AI, removing roadblocks and reducing the noise to drive better results for employees and customers.

- **MSCI**, a leading publisher of market indices and data, uses machine learning with Vertex AI, BigQuery, and Cloud Run to enrich its datasets to help clients gain insights into around 1 million asset locations to help manage climate-related risks.

- \* **NatWest** **Markets**, part of one of the UK's largest financial institutions, implemented Dataplex and BigQuery to automate data quality management across departments. The bank now delivers data-quality insights daily instead of monthly and reduced the time spent writing and implementing data rules by a third compared to its previous manual approach.

- \* **Oper Credits**, a Belgian mortgage digitization company serving about 20 banks across six countries, uses Vertex AI to automate document verification that previously required several hours of manual work. The company aims for 90% of loan applications to be complete and compliant on first submission, up from the current 30-40% in Belgium where most are returned due to missing or incorrect information.

- \* **Rogo**, a generative AI platform built for the financial industry, uses Google Cloud solutions like Dataflow, Spanner, and Vertex AI to automate complex research and analysis for the world's leading investment banks and private equity firms. Gemini 2.5 Flash enabled the platform to cut AI modeling time from months to hours and reduce hallucination rates from 34.1% to 3.9%.

- **Snowdrop** leverages Google Cloud's AI and geospatial data, including Google Places and Vertex AI, to enrich transactional data for financial institutions. This automation has led to a 40% improvement in data accuracy, a 15% increase in merchant-to-transaction matching, and the ability to process over 2.1 billion transactions monthly while scaling globally.

- **SURA** Investments, the largest asset manager in Latin America, developed an AI-based analysis model for employees that allows them to better understand customer needs and improve customer experience and satisfaction.

- **Syte**'s AI-driven property platform allows the retrieval of all relevant characteristic data on properties and its development, expansion, and conversion potential in real-time, making it easy to identify sites and buildings for re-densification.

- \* **Stax** **AI**, a retirement administration platform, uses Google Cloud's generative AI and MongoDB to automate data extraction from complex financial documents. The solution processes thousands of brokerage statements in minutes, not hours, helping administrators respond to client inquiries and meet compliance deadlines in a fraction of the time.

- \* **UOB** **Asset** **Management** (UOBAM), a Singapore-based asset manager established in 1986, used Vertex AI to improve its proprietary AI hedging model, reducing processing time from 48 hours to two hours per trade. The enhanced model outperformed the buy-and-hold strategy by 28.75% and improved performance by 52.55% over the original model, potentially delivering close to an extra $10 million for every $100 million deployed.

- \* **WealthAPI**, a German fintech company, uses DataStax Astra DB on Google Cloud with Gemini to deliver real-time financial insights to millions of users. The platform's scalability allows it to analyze hundreds of thousands of transactions per second and has reduced response times by 90% for its customers.


### **Security Agents**

- **Airwallex**, an Australian multinational fintech company, detects and manages fraud in real time in a scalable, always-available environment, powered by Vertex AI, Google Kubernetes Engine, and GitLab.

- **Apex** **Fintech Services** is using Gemini in Security to accelerate the writing of complex threat detections from hours to a matter of seconds.

- **BBVA** uses AI in Google SecOps to detect, investigate, and respond to security threats with more accuracy, speed, and scale. The platform now surfaces critical security data in seconds, when it previously took minutes or even hours, and delivers highly automated responses.

- **Bradesco**, one of the largest financial institutions in Latin America, has been using Google Cloud AI to detect suspicious activity and combat money laundering more effectively and efficiently — and was one of the early adopters worldwide of Google Cloud’s Anti Money Laundering AI.

- **Charles Schwab** has integrated its own intelligence into the AI-powered Google SecOps, so analysts can better prioritize work and respond to threats.

- **Cloudwalk**, a Brazilian fintech unicorn that currently serves more than one million customers with payment solutions, uses Google Cloud infrastructure and AI services to build anti-fraud and credit analysis models. This allowed the fintech to close 2023 with a profit of $22.3 million, showing 200% growth in its commercial base.

- **Credem**, a 114-year-old Italian financial institution, uses AI to enhance security for online users, offer products tailored to customer needs, and predict software malfunctions, achieving significant results in a short time.

- **Dun & Bradstreet** is using Security Command Center to centralize monitoring of AI security threats alongside their other cloud security findings.

- **Fiserv**, a developer of financial services technology, can now summarize threats, find answers, and detect, validate, and respond to security events faster with the Gemini in Security Operations platform.

- **Resistant AI** is building AI-powered solutions to combat fraud in financial services documentation and workflows with the help of Google Cloud. These solutions can expedite background checks, reduce fraud losses, and speed up underwriting and claims processing processes.

- \* **Upsure**, an India-based insurtech platform, built its AI-powered solution on Google Kubernetes Engine, Vertex AI, and Gemini to help insurers create unified data lakes for anti-money laundering compliance and lead scoring. The platform supports more than 1 million daily users across over 2,000 locations with 99.9% uptime and response times in milliseconds.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Heath__Sciences.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Heath__Sciences.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Heath__Sciences.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Heath__Sciences.max-900x900.jpg)

Healthcare & Life Sciences

### **Customer Agents**

- **Bennie Health** uses Vertex AI to power its innovative employee health benefits platform, providing actionable insights and streamlining data management in order to enhance efficiency and decision-making for employees and HR teams.

- \* **CitiusTech**, a global healthcare technology services firm, uses Google Cloud to improve patient experience, reduce administrative burden on clinical staff, and save costs for healthcare systems. The company has developed an AI search solution using Vertex AI to efficiently connect patients with the right specialists and automate critical workflows.

- **Clivi**, a Mexican health startup, has created a gen AI platform with Google Cloud that enables personalized and continuous monitoring of its patients to offer tailored responses, improve the volume and capacity of care, and reduce complications.

- **Family Vision Care** of Ponca City uses Gemini in Gmail to easily explain medical terms in patient emails and to improve accessibility.

- \* **Fitterfly**, an India-based mobile health app helping users manage chronic diseases like diabetes and obesity, uses Gemini Flash and Vertex AI to reduce meal logging times by 80% and automate 90% of support queries. The AI-powered platform delivers precision coaching to over 30,000 users and enterprise clients including major insurers in India and UAE.

- **Freenome** is creating diagnostic tests that will help detect life-threatening diseases like cancer in the earliest, most-treatable stages — combining the latest in science and AI with the ease of a standard blood draw.

- **Genial Care**, a Latin American healthcare network, is a reference in innovative care for children with Autism Spectrum Disorder and their families. By investing in Vertex AI, the company has improved the quality of records of sessions involving atypical children and their families, allowing caregivers to fully monitor the work carried out.

- \* **Manipal** **Hospitals**, one of India's largest healthcare providers serving over 7 million patients annually, uses Vertex AI and Gemini models to power its ePharmacy app that enables patients to view prescriptions, order medications, and arrange delivery after consultations. The AI platform reduces average order time from 15 minutes to less than 5 minutes while achieving 99% accuracy.

- \* **Moody** **Month**, a daily health and wellness tracker used by more than 100,000 women, built its AI-powered platform using Cloud Run, Gemini 2.5 Pro, and BigQuery to deliver personalized hormone forecasts while keeping sensitive health data secure. The company serves 100,000 users a month for just £1,000 with its scalable Google Cloud microservices infrastructure.

- **Orby** is combining AI and neurotechnology, applying complex mathematical models, Google Cloud’s IT resources, and Gemini to create a “digital brain.” This solution supports patients’ rehabilitation, helping them to recover lost motor skills and reduce their pain.

- \* **Pear** **Health** **Labs**, a health and fitness AI platform, develops personalized interventions to prevent chronic conditions. It powers recommendations, content search, and dynamic audio coaching. It uses Vertex AI Voice Generation, Vector Search in BigQuery, and the engineering team leverages Gemini Code Assist.


### **Employee Agents**

- **American Addiction Centers** was able to reduce employee onboarding from three days to 12 hours using Gemini for Google Workspace, and is now exploring how to streamline tasks like generating safety checklists for medical staff, saving valuable time and improving patient care.

- **Asepha**, part of the Google for Startups Cloud AI Accelerator, is building fully autonomous AI pharmacists to help automate manual work.

- **Bayer** is building a radiology platform that will assist radiologists with data analysis, intelligent search, and document creation that meet healthcare requirements needed for regulatory approval.

- **BenchSci** develops generative AI solutions empowering scientists to understand complex connections in biological research, saving them time and financial resources and ultimately bringing new medicine to patients faster.

- **Better Habits** uses Google Workspace with Gemini to reduce the time spent developing communication plans, allowing them to focus on delivering high-quality wellness workshops.

- **Certify OS** is automating credentialing, licensing, and monitoring of medical providers for healthcare networks, relieving the burden of time-consuming and often siloed information.

- **Click Therapeutics** develops prescription digital therapeutics designed to treat disease. Its Clinical Operations team leverages Gemini for Google Workspace to transform complex operations data into actionable insights so they can quickly pinpoint ways to streamline the patient experience in clinical trials.

- Mark Cuban’s **Cost Plus Drugs** widely uses Gemini for Google Workspace, estimating that employees are saving an average five hours per week just with AI capabilities in Gmail. Gemini is also streamlining time-consuming, manual processes through uses like AI-generated transcriptions and auto-formatting of pharmaceutical lab results or FDA compliance documentation.

- **Covered California**, the state’s healthcare marketplace, is using Document AI to help improve the consumer and employee experience by automating parts of the documentation and verification process when residents apply for coverage.

- \* **CoVet** is an AI assistant built by veterinary professionals, for veterinary professionals, that uses Gemini, Cloud Functions, and other solutions to help veterinary teams automate administrative work, save hours every day, and refocus on what matters most: exceptional patient care.

- **Cradle**, a biotech startup, is using Google Cloud's generative AI technology to design proteins for drug discovery, food production, and chemical manufacturing. By leveraging TPUs and Google's security infrastructure, the company accelerates R&D processes for pharmaceutical and chemical companies while protecting sensitive intellectual property.

- **CytoReason** uses AI to create computational disease models that map human diseases, tissue by tissue and cell by cell, to help pharma companies shorten clinical trials and reduce the high costs of drug development. CytoReason has been able to reduce query time from two minutes to 10 seconds.

- **Dasa**, the largest medical diagnostics company in Brazil, is helping physicians detect relevant findings in test results more quickly.

- **DaVita** is developing dozens of AI models to transform kidney care, including analyzing medical records, uncovering critical patient insights, and reducing errors. AI enables physicians to focus on personalized care, resulting in significant improvements in healthcare delivery.

- \* **Digital** **Diagnostics**, a healthcare diagnostics company, uses Google Cloud’s secure infrastructure to enhance the reach of LumineticsCore, its AI-powered diagnostic tool for diabetic retinopathy. This approach protects sensitive health data and ensures patient privacy and regulatory compliance.

- \* **Elanco**, a global leader in animal health with thousands of manufacturing compliance documents, uses Gemini within its Elanco.ai platform to automatically sort, summarize, compare, and restructure information from over 2,500 unstructured policy and procedure documents per manufacturing site. The AI agent improves accuracy and consistency of compliance documentation, reducing the risk of outdated or conflicting information that could cost up to $1.3 million in productivity impact at large sites.

- \* **Fingerpaint**, a full-service pharmaceutical marketing agency, uses NotebookLM to conduct real-time quality assurance and fact-checking for drug efficacy claims and craft compelling strategic marketing narratives. The AI addresses the challenge of verifying LLM outputs in an industry where every claim must be meticulously fact-checked and supported by scientific literature and clinical trial data, enabling the agency to scale its use of AI.

- **Hackensack Meridian Health** has developed a clinical decision-making tool that analyzes large patient data sets to identify patterns and trends. These insights can be used to help providers make better decisions about patient care.

- **HCA** **Healthcare** is testing Cati, a virtual AI caregiver assistant that helps to ensure continuity of care when one caregiver shift ends and another begins. The healthcare network operator is also using gen AI to improve workflows on time-consuming tasks, such as clinical documentation, so physicians and nurses can focus more on patient care.

- **Hemominas**, Brazil's largest blood bank, partnered with Xertica to develop an omnichannel chatbot for donor search and scheduling, streamlining processes and enhancing efficiency. The AI solution has the potential to save half-a-million lives annually by attracting more donors and optimizing blood supply management.

- **Highmark Health** is building an intelligence system equipped with AI to deliver valuable analytics and insights to healthcare workers, patients, and members, powered by Google Cloud’s Healthcare Data Engine.

- \* **Infinitus**, one of the most trusted agentic healthcare communications platforms, automates clinical and administrative conversations at scale. Our AI agents powered by Gemini's multimodal capabilities have completed over 5x more conversations than any other solution with payors, patients, and providers to drive revenue and improve health outcomes

- \* **iSono** **Health**, a medical imaging company, developed a Virtual Sonographer, an intelligent, automated 3D Ultrasound platform powered by Google Cloud AI. The platform brings breast imaging directly to the point of care, providing fast, accessible, and repeatable imaging.

- \* **Kyoto University Hospital** partnered with Fitting Cloud to develop CocktailAI, a medical document generation system using Vertex AI with Gemini and MedLM that automates clinical referral letters and discharge summaries. Doctors who previously spent 3-4 hours after each day's appointments on documentation can now generate documents that require only minor review and corrections.

- \* **Manipal** **Hospitals**, one of India's largest healthcare providers with more than 10,500 beds, is pioneering the use of Gen AI to automate nurse handoff documentation by generating comprehensive reports that summarize patient information, medication changes, laboratory results, and vital signs. The solution reduces handoff time from 90 minutes to approximately 20 minutes per nurse.

- **PwC** uses AI agent technology, powered by Google Cloud, to help oncology clinics to streamline administrative work so that doctors can better optimize the time they spend with patients.

- **Sami Saúde** uses Gemini for Google Workspace to automate repetitive tasks, empowering care providers and accelerating access to care. This has resulted in a 13% increase in productivity, 100% of patient summaries being generated by AI, and more accurate diagnoses for improved patient outcomes.

- **Seattle Children's Hospital** is pioneering a new approach to clinical care with its Pathway Assistance solution, which makes thousands of pages of clinical guidelines instantly searchable by pediatricians.

- \* **Seattle** **Children's** is also using a HIPAA-compliant version of Gemini in Google Workspace to speed up writing meeting notes, drafting emails, and creating tickets. Physicians now draft emails, notes, and tickets in seconds instead of hours, reducing administrative load and enabling more time for patient care.

- \* **SIGNAL** **IDUNA**, a leading German insurance provider, partnered with Google Cloud, Boston Consulting Group (BCG), and Deloitte to develop Co SI — a cutting-edge AI knowledge assistant that helps customer service agents resolve complex health insurance inquiries, quickly and accurately. For less experienced agents, information searches are 30% faster and inquiries that previously required further escalation dropped from 27% to just 3%

- **Straloo** uses Gemini to innovate the diagnostic approach in its digital rehabilitation platform, helping doctors and physical therapists prescribe appropriate treatments for those suffering from knee and back pain.

- \* **Tali.ai** is the leading medical AI scribe platform, designed to reduce the administrative burden of clinicians. Integrated with multiple EMRs across the U.S. and Canada, it leverages Google’s Vertex and Gemini models to automate clinical note-taking during patient encounters and extract key insights.

- \* **Think** **Research**, a provider of knowledge-based digital health software solutions, uses Google Cloud’s scalable infrastructure and analytics tools to power its platform. This enables the company to deliver more efficient patient care and improve health outcomes.

- **Ubie**, a healthcare-focused startup founded in Japan, is using Gemini models via Google Cloud to power its physician assistance tool.

- **Ufonia** helps physicians deliver care by using Google Cloud’s full AI stack alongside its own clinical evidence to automate routine clinical consultations with patients, transforming the experience for both patients and clinicians.

- \* **Virbac**, an animal health pharmaceutical company, uses Gemini in Google Workspace to compare supplier quotes for procurement and draft legal clauses for the legal department. The AI automates low-impact tasks, allowing teams to focus on high-value priorities that directly support animal health.

- \* **Virbac** also uses Gemini models to pilot an HR chatbot that streamlines international collaboration and automates routine tasks. The deployment includes clear AI governance and onboarding sessions to build AI awareness across the organization.

- **WellSky** is integrating Google Cloud's healthcare and Vertex AI capabilities to reduce the time spent completing documentation outside work hours.

- **Wipro** is supporting a national healthcare provider in using Google Cloud’s AI agent technology to develop and adjust contracts, helping to optimize and accelerate a historically complex and time-consuming task while improving accuracy.


### **Data Agents**

- **Amigo Tech** launched Amigo Intelligence, a platform based on Google AI technologies that automates medical processes, reduces costs, and improves the efficiency of clinics and practices. The solution includes tools like anamnesis automation, advanced exam analysis, and a medical AI chatbot, transforming healthcare management.

- **Apollo Hospitals** in India partnered with Google Health to build screening models for tuberculosis and breast cancer, helping an extremely limited population of radiologists cover more patients at risk, scaling to 3 million screenings in a matter of years.

- **ARC Innovation** at **Sheba Medical Center** is using Google Cloud's AI tools, including Looker Studio and BigQuery ML, to create healthcare solutions that improve critical clinical decisions during the treatment of ovarian cancer.

- \* **Atropos** **Health**, a healthcare data analytics company, optimized its GENEVA OS to work with Google Cloud’s Healthcare Data Engine (HDE) and BigQuery. This enables customers to efficiently and securely convert data into valuable insights and evidence.

- **Auransa**, an emerging clinical-stage biopharma company, has created a proprietary AI platform to derive a differentiated pipeline of novel drugs.

- **Autoscience**, a startup building AI agents to aid in scientific research, is using Google Cloud infrastructure and resources through the Google for Startups Cloud Program as it begins to build and market its products.

- **Bayer** built a data agent that uses gen AI in BigQuery to predict flu outbreaks. It combines Google Search trends and internal data for real-time, location-specific healthcare planning.

- Bayer and Google also announced a collaboration to drive early drug discovery that will apply AI-specialized Tensor Processing Units (TPUs) to help accelerate and scale Bayer’s quantum chemistry calculations.

- **Beep Saúde**, the largest home health company in Brazil, implemented an AI-powered last-mile dynamic routing system with Google Maps to optimize its operations and manage a 10% cancellation volume. The company also uses AI to speed up the processing of medical orders, aiming to reduce costs and increase efficiency to boost its expansion plans in Brazil.

- **Bliss Health** is transforming the insurance market with a digital channel for brokers, integrated with Google Cloud and technologies like Dialogflow and Gemini Pro. The solution has reduced its service-level agreement from four hours to seconds in transactional queries, improved operational efficiency, and eliminated bureaucracy, helping to speed up business closure.

- **CerebraAI**, develops AI software for analyzing non-contrast CT (NCCT) scans, with a focus on early stroke and cancer detection. It fine-tunes MedGemma on NCCT images and leverages Gemini's few-shot generalization capabilities to rapidly adapt the model for various diagnostic tasks.

- **Chopo/Grupo Proa**, a Mexican medical diagnostics company, leverages generative AI to integrate patient and physician data, obtaining a complete view that optimizes decision-making. This initiative has enabled a considerable reduction in acquisition costs and an increase in sales.

- \* **Congruence** **Therapeutics**, a computationally driven biotechnology company, uses its proprietary platform, Revenir, to build a pipeline of small molecule correctors. The platform identifies novel allosteric and cryptic pockets in proteins to rescue aberrant function.

- \* **DNAstack**, a leading genomics data management and analysis platform, leverages Google Cloud’s scalable infrastructure and advanced analytics tools to accelerate research and discovery in personalized medicine.

- **Elanco**, a leader in animal health, has implemented a gen AI framework supporting critical business processes, such as Pharmacovigilance, Customer Orders, and Clinical Insights. The framework, powered by Vertex AI and Gemini, has resulted in an estimated ROI of $1.9 million since launching last year.

- \* **Evogene** uses Google Cloud and Vertex AI to replace life sciences' costly "spray and pray" molecular discovery — testing millions of molecules hoping to stumble into effective ones — with their computational platform. They now process 40 billion molecules versus previous millions, while using Vertex AI to develop a cutting-edge small-molecule foundation model that dramatically accelerates drug discovery timelines.

- **Fairtility** is using Google Cloud's AI capabilities to enhance IVF outcomes worldwide. By leveraging AI and machine learning within Google Cloud, Fairtility analyzes embryo images and related data to identify embryos with the highest potential for successful implantation, increasing the likelihood of pregnancy for patients undergoing IVF.

- \* **GenBio** **AI**, a computational biology company, uses Google Cloud to power six specialized AI models in developing AI-driven digital organism simulators. These models simulate biological programming to address critical challenges in medicine and biology.

- **Ginkgo** **Bioworks** is building a next-generation AI platform for biological engineering and biosecurity, including pioneering new AI models for biological engineering applications that are powered by Vertex AI.

- \* **Gleamer**, a French AI radiology company deployed in over 2,500 healthcare institutions across 45 countries, uses Med-PaLM and Gemini on Vertex AI to automate radiological report generation. The platform processes over 35 million exams annually and demonstrates a 30% improvement in lesion detection, allowing general radiologists to reach specialist-level performance.

- \* **Immunai** tackles drug development's decade-long timeline with AMICA, the world's largest immune-focused single-cell database containing hundreds of millions of cells. Using Google Cloud GPU clusters, they train models that transform complex immune mechanisms into actionable recommendations for 30+ biopharmaceutical partners.

- **Mayo** **Clinic** has given thousands of its scientific researchers access to 50 petabytes worth of clinical data through Vertex AI Search, accelerating information retrieval across multiple languages.

- **Mendel** has built a clinical AI system designed to consolidate the longstanding silos in medical data into a knowledge base of holistic patient journeys, boosting patient recruitment for new therapies and clinical trials.

- \* **Menten** **AI**, a biotechnology company, uses Google Cloud’s high-performance compute and machine learning capabilities to accelerate the development of peptide therapeutics. This allows the company to rapidly design and optimize novel drug candidates.

- \* **Moonwalk** **Bio**, a preclinical-stage biotechnology company, leverages epigenetic biology and AI to pioneer new medicines for obesity and cardiometabolic disease. Their platform determines the causal relationships between genes and disease pathways for therapeutic targeting.

- **The National Institutes of Health** ( **NIH**), the U.S. government’s healthcare and research agency, uses Google Cloud as part of STRIDES, the Science and Technology Research Infrastructure for Discovery, Experimentation, and Sustainability. The initiative provides easy access to high-value NIH datasets and a wide range of Google Cloud services, including compute resources, data storage and analytics, and cutting-edge AI and ML capabilities to accelerate biomedical research.

- **Neomed**, a Brazilian healthcare startup, works in the diagnosis of cardiovascular diseases, assisting clinics and hospitals in the management of data and reports of graphical exams. Its AI-based solution reduces the time for electrocardiogram reports to around two minutes.

- **Nextnet** uses Gemini and Vertex AI to uncover novel insights and knowledge for life sciences and pharmaceutical research, enabling researchers to analyze biomedical data and identify hidden relationships in scientific literature.

- **Ordaōs**, an AI-driven drug discovery leader, relies on its cloud computing capabilities to design, process, and analyze data for millions of protein structures, notably using Google Kubernetes Engine to achieve increased flexibility and easier scalability to take on new, larger AI projects.

- **Probrain** offers personalized auditory stimulation training. By implementing cloud-based gen AI solutions, it’s modernized services and reduced costs by approximately 89%. For the end consumer, this also resulted in savings of almost 50%.

- **Red Interclinica**, the Chilean hospital network, uses AI to make better decisions through data transformed into insights, as well as making medical care more accessible for its patients, while also reducing costs and generating more value for the organization.

- \* **SandboxAQ** is expanding its usage of Google Cloud and running a new AI drug discovery simulation platform on Google Cloud.

- **Schrödinger** uses Cloud GPUs to power AI models working on advanced drug discovery.

- \* **Sully.ai**, a healthcare AI company, has built an app store for AI agents designed specifically for healthcare professionals. The platform provides support to clinicians on administrative tasks, so they can focus on patients.

- **Superluminal Medicines** uses Google Cloud's computing power to analyze multiple protein structures and integrate them into dynamic protein models for drug discovery, allowing for a more accurate representation of protein behavior and the design of more precise drug interventions.

- \* **Triplebar**, a biotechnology company, is building a genome-scale AI model for therapeutic production. Using a proprietary miniaturization process, they can test billions of cellular mutations at once, creating large datasets to train generative AI and inform new treatments.

- \* **Via** **Scientific**, a bioinformatics company, partners with Google Cloud to deliver Via Foundry, an enterprise-grade platform that uses Gemini and Vertex AI to make the drug discovery process more efficient. The platform transforms complex biological data into actionable insights that can accelerate discoveries.

- \* **Virgo Surgical**, a medical video solutions provider, uses Google Cloud Storage and Google Kubernetes Engine to host and process over 1.75 petabytes of video data. This data has been used to create EndoDINO, an AI foundation model for endoscopy that achieves high performance in medical imaging applications.


### **Security Agents**

- **apree health** uses Google Workspace to implement a Zero Trust security solution with granular access controls and device management, centralizing its data access and protecting sensitive patient data while quickly migrating nearly 1,000 users from its previous collaboration solution.

- **Pfizer** can now aggregate cybersecurity data sources, cutting analysis times from days to seconds.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Travel.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Travel.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Travel.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Travel.max-900x900.jpg)

Hospitality & Travel

### **Customer Agents**

- \*Agoda uses Gemini and Imagen to offer customized, hyper-personalized travel destination and itinerary suggestions, enhancing visitor engagement and bookings on the site. The AI Vacation Planner requires just eight user inputs to generate detailed travel plans in seconds, while Imagen creates hyper-realistic destination images at low cost compared to traditional sourcing methods.

- **Alaska Airlines** is developing natural language search, providing travelers with a conversational experience powered by AI that’s akin to interacting with a knowledgeable travel agent. This chatbot aims to streamline travel booking, enhance customer experience, and reinforce brand identity.

- \* **Bookme**, Pakistan's largest travel tech and e-ticketing company serving over 12 million registered customers, uses Document AI, Vertex AI, and Gemini to power a conversational chatbot that delivers more efficient customer interactions. The migration to Google Cloud reduced average API load time by 50% (user dashboard APIs dropped from 700ms to 255ms) and improved platform latency from 240ms to 180ms.

- \* **Catchtable** uses Vertex AI and Kubeflow with GPU optimization to build personalized restaurant recommendation models, achieving a 30% increase in reservation conversion rates and a 150% increase in impressions per restaurant search. The platform leverages BigQuery for data integration, Gemini for review analysis, and hybrid AI models that combine LLMs with custom embeddings to understand customer search intent and deliver real-time personalized recommendations.

- \* **Fitness** **Park**, a French fitness chain, uses BigQuery to improve data reliability and plans to leverage Vertex AI and Gemini for AI-powered personalized exercise recommendations, nutrition guidance, and intelligent training programs. The migration reduced query times from hours to seconds and enabled real-time marketing campaigns previously blocked by infrastructure limitations.

- **Gymshark**, a leading UK fitness community and gymwear brand, is using BigQuery, Looker, Dataflow, and Vertex AI to build a unified data platform that enhances customer insights and delivers personalized fitness experiences at scale.

- \* **Hershey** **Entertainment** **&** **Resorts** built a natural language chatbot using Conversational Agents in just 40 hours to serve millions of annual guests across Hersheypark, Hotel Hershey, and other Pennsylvania attractions. The AI-powered assistant personalizes responses for diverse audiences — from vacationing families to corporate event planners — autonomously handling requests and adapting content to deliver tailored guest experiences at scale.

- **HomeToGo**, a vacation-rental app, created AI Sunny, a new AI-powered travel assistant that supports guests while booking, and has plans to build it into Super AI Sunny, an end-to-end smart travel companion.

- **Hotelplan** **Suisse** built a chatbot trained on the business’s travel expertise to answer customer inquiries in real-time, and, following that success, it plans to use gen AI to create travel content.

- **IHG Hotels & Resorts** is building a gen AI-powered chatbot to help guests easily plan their next vacation directly in the IHG One Rewards mobile app.

- \* **Intravel** makes travel storytelling shoppable. Powered by Google's Gemini AI and Edge Video, it analyzes videos in real time to match tours, hotels, and experiences. This creates instant, interactive overlays for direct booking, automating all commerce logic from discovery to commissioning.

- **Mustard** uses proprietary computer vision and AI technology to unlock exceptional, personalized coaching experiences for every golfer and baseball pitcher who wants to level up, all with the ease of a straightforward mobile app.

- **Mystifly** is a Singapore-based travel tech company that has developed Mystic, a chatbot built on Google Cloud's conversational and generative AI platforms; it offers users self-serve options that reduce the need for direct agent support, improving efficiency and customer satisfaction.

- The **Papa John’s** pizza chain is using BigQuery, Vertex AI, and Gemini models to build predictive tools that can better anticipate customers orders in the app, as well as an enhanced loyalty program and more personalized marketing offers. There are also plans to build an AI-powered chatbot to help handle orders.

- **Priceline**’s Trip Intelligence suite features one of the travel industry’s most comprehensive array of AI tools, including more than 30 new features to dramatically streamline the travel planning and booking process.

- **Sabre** Travel AI has developed an AI agent that personalizes offers, optimizes revenue management, and streamlines operations for travel companies; this has led to improved customer experiences and increased revenue while fostering growth for Sabre's partners.

- **Six Flags** theme parks has built an industry-first digital assistant who can answer guests’ questions and help them plan their whole day. Six Flags will also apply Google Cloud's capabilities in AI, analytics, and infrastructure to offer improved operations, personalization, and customer experiences across Six Flags' diverse portfolio of parks.

- **Studiosus Reisen**, a German travel company, worked with **happtiq** and **Solid Cloud** to migrate its 40-year old on-premise system and SAP workloads to Google Cloud to enable real-time reservations, increasing its conversion rates by 40%.

- **Technogym** leverages Vertex AI and Model Garden to power Technogym Coach, an AI-driven virtual trainer that creates hyper-personalized fitness programs. This increased user engagement and motivation, improved fitness outcomes, and delivered a more personalized and effective training experience.

- **trivago**’s new “Smart AI Search” is an advanced free-text search functionality, powered by Vertex AI Search, that allows users to search for hotels using natural language, making it easier and more personalized to find the ideal accommodations.

- \* **Vivaticket**, an international event management and ticketing platform, plans to use Vertex AI Search to accelerate customer access to information about interesting events. Generative AI will also help Vivaticket generate recommendations and create SEO-friendly event and venue descriptions faster.


### **Employee Agents**

- **Attache** leverages Gemini for Google Workspace to streamline various tasks, such as analyzing historical data, which helped achieve an 80% reduction in calls from new arrivals, leading to happier customers and smoother stays.

- \* **Hershey Entertainment & Resorts** uses Customer Engagement Suite to power Agnes, an agentic AI Interactive Voice Response system that identifies employees by caller ID, addresses them by name, and processes call-off requests, late notifications, and schedule inquiries. This AI assistant now handles over 25% of employee call-offs, saving eight hours of staff work per day.

- **loveholidays** saved 20% of their customer service cost per year after deploying Customer Engagement Suite.

- **Sweets and Meats BBQ** finds local events for its food trucks with help from Gemini in Sheets, easily generating a weekly schedule in seconds.


### **Creative Agents**

- **Curb Free** with Cory Lee, a popular "wheelchair travel site," shares accessible travel guides, and brainstorms new content ideas with Gemini in Docs to keep giving readers fresh and valuable info.

- **Japan Airlines** partnered with Brandtech Group to use its Pencil generative AI platform to mock up new ads, with creative leaders writing the strategy and Veo 2 creating the magic.

- **Radisson Hotel Group** personalized its advertising at scale, in collaboration with Accenture, using Vertex AI and Gemini models. By training them on extensive datasets stored in BigQuery, its ad teams saw productivity rise around 50% while revenue increased from AI-powered campaigns by more than 20%.

- **Three Fold Noodles + Dumpling** drafts social media posts with Gemini in Docs to stay active online without compromising on quality time in the kitchen.

- \* **Virgin Voyages** is using Veo’s text-to-video features and Imagen to create thousands of hyper-personalized advertisements and emails. Each one perfectly matches Virgin Voyages unique brand voice at a scale that would be impossible just a year ago.


### **Data Agents**

- **BrushBuck Wildlife Tours** tracks seasonal animal movements with help from Gemini in Sheets so every visitor has a chance to marvel at Wyoming's wildlife.

- **Fetcherr** replaces airlines' fractured decision-making systems with their Large Market Model that simulates millions of scenarios before selecting optimal actions. Built on Vertex AI, major airlines including Virgin Atlantic, Delta, Viva Aerobus, and WestJet use the platform for predictive pricing and long-term automation strategies.

- **Fitz's Bottling Company** has been selling root beer since 1947 and now uses Gemini in Sheets to quickly pull together and format inventory information, helping them continue the success of the world's first root beer microbrewery.

- **Hog Island Oyster** simplifies sales analysis with Gemini in Sheets, creating reports on oyster sales by type, size, and quantity with a single prompt.

- **Latam Airlines** is leveraging Google Cloud AI to automate data management and governance, enhancing customer experience. By using generative AI, the airline optimized processes like table classification and metadata management, resulting in reduced time and costs.

- **Studiosus Reisen** worked with **happtiq** to use Vertex AI to build a custom AI model to automatically classify and filter security alerts, reducing the manual effort to active security concerns for travelers by 75%.


![https://storage.googleapis.com/gweb-cloudblog-publish/images/Manufacturing.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Manufacturing.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Manufacturing.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Manufacturing.max-900x900.jpg)

Manufacturing, Industrial & Electronics

### **Customer Agents**

- **Motorola**’s Moto AI leverages Gemini and Imagen to help smartphone users unlock new levels of productivity, creativity, and enjoyment with features such as conversation summaries, notification digests, image creation, and natural language search — all with reliable responses grounded in Google Search.

- **Oppo/OnePlus** is incorporating Gemini models and Google Cloud AI into its phones to deliver innovative customer experiences, including news and audio recording summaries, AI toolbox, and more.

- **Samsung** is deploying Gemini Pro and Imagen 2 to its Galaxy S24 smartphones so users can take advantage of amazing features like text summarization, organization, and magical image editing.

- **Samsung** is using Google’s generative AI technology for Ballie — its exciting new home companion robot. Ballie will be able to engage in natural, conversational interactions to help users manage home environments, including adjusting lighting, greeting people at the door, personalizing schedules, setting reminders, and more.

- **ScottsMiracle-Gro** built an AI agent on Vertex AI to provide tailored gardening advice and product recommendations for consumers.


### **Employee Agents**

- \* **Adani Group**, one of India's largest multinational conglomerates, uses Vertex AI Search and Vector Search to transform its internal a-connect newsletter platform, enabling employees to search through articles using semantic understanding across text, images, and videos. The AI-powered search significantly reduces average query time while providing automatic summarizations and citations.

- **AES**, a global energy company, uses gen AI agents built with Vertex AI and Anthropic’s Claude models to automate and streamline its energy safety audits. This has resulted in a 99% reduction in audit costs, a time reduction from 14 days to one hour, and an increase of 10-20% in accuracy.

- \* **Asia Digital Engineering** (ADE), a leading aircraft Maintenance, Repair, and Overhaul provider born from Malaysia AirAsia's engineering department during the COVID-19 pandemic, uses Gemini and Document AI alongside Vertex AI to enhance its digital operations and maintenance services. This implementation doubled development life cycle speed through containerization and significantly accelerated data processing, allowing the team to analyze large datasets much more quickly.

- \* **Bynry**'s SMART360 leverages Google Cloud’s robust infrastructure to empower small and mid-sized utilities to enhance operational efficiency and customer satisfaction.

- **Copel**, a major Brazilian electric utility company, has developed an AI agent with Gemini Pro 1.5 that interacts with the company's on-premises SAP ERP system, allowing employees to ask a variety of questions using natural language.

- \* **Danfoss**, a global manufacturer operating in over 100 countries, uses AI agents from Go Autonomous on Google Cloud to automate email-based order processing. The solution automated 80% of transactional decisions, reduced average customer response time from 42 hours to near real-time, and consolidated five systems into a single interface.

- **Enpal**, working with Google Cloud partner dida, automated part of its solar panels sales process. By automating the generation of quotes for prospective solar panel customers, including assessing roof size and the number of panels required, Enpal reduced the time required by 87.5%, from 120 minutes to 15 minutes.

- **Honeywell**, an almost 120-year-old manufacturing company, has already incorporated Gemini into building automation products and is now applying AI to transform how its engineers manage product lifecycles.

- **Hydro Ottawa** uses Gemini for Google Workspace to help employees automate daily tasks and collaborate more efficiently. This has resulted in better and more cost-effective services for its customers.

- \* **Léon** **Grosse**, a construction industry leader, uses Gemini in Google Workspace to automate complex tasks including document summarization, data analysis, and content drafting. The AI serves as a catalyst for digital transformation, helping the company gain agility, efficiency, and stronger collaboration in a rapidly evolving industry.

- \* **Mercer International**, a global bio-manufacturing company with 4,000 employees across the United States, Canada, and Germany, uses Gemini to translate safety training materials for its multilingual workforce. Some European facilities have seven different languages spoken on the factory floor daily, and the AI enables seamless multilingual communication.

- \* **Orica**, a multinational company with over 14,000 employees in 100+ countries, migrated its critical SAP system to Google Cloud and recorded performance improvements of up to 18.5% for business applications. The company reduced backup times from six hours to 17 minutes and cut its monthly business planning job time by 50%.

- **Plenitude** leverages Google Cloud's Optical Character Recognition and Gemini Flash models to automate customer onboarding, extracting data from energy bills and verifying IDs with Document AI. This has resulted in faster onboarding, reduced fraud, and significant time savings in ID verification.

- **Robert Bosch**, the world's largest automotive supplier, revolutionizes marketing through gen AI-powered solutions, streamlining processes, optimizing resource allocation, and maximizing efficiency across 100+ decentralized departments.

- **Suzano**, the world's largest pulp manufacturer and a leader in sustainable bioeconomics, worked with Google Cloud and Sauter to develop an AI agent powered by Gemini Pro to translate natural language questions into SQL code to query SAP Materials data on BigQuery. This has resulted in a 95% reduction in the time required for queries among the 50,000 employees using the data.

- \* **Talgo**, one of the world's foremost train manufacturers, used Vertex AI to create Sophia, an AI agent that provides conversational assistance to maintenance teams across multiple languages, including English, Russian, and Arabic.

- **Trimble**, a maker of software and hardware for products ranging from satellites to drones and monitors of many kinds, is leveraging Gemini for Google Workspace's advanced capabilities so employees can enhance productivity; the company has streamlined workflows, including efficient document search, concise summaries, and code generation, all within a secure and collaborative environment.

- \* **Workerbase**, a Germany-based manufacturing platform serving clients like Siemens and Porsche, leverages Vertex AI and Google Kubernetes Engine to deliver real-time, AI-powered workflows and task instructions to shop floor operators in their preferred languages. The company's low-code app development framework accelerated workflow deployment time from months to hours, allowing supervisors and engineers to design and deploy custom applications without extensive coding expertise.

- \* **Zoppas** **Industries**, a global leader in designing and manufacturing smart thermal management solutions, uses Gemini in Google Workspace to automate meeting note-taking and accelerate tasks like supplier research. The AI enables teams to create, collaborate, and innovate faster, ensuring quicker time to market and enhanced customer satisfaction.

- \* **Zoppas** **Industries** also uses Gemini to support HR analysis tasks and enhance decision-making. The generative AI tools help employees work more efficiently while maintaining premium security protocols across global teams.


### **Creative Agents**

- **Ace Sign Co.** uses Gemini in Slides to mock-up designs in seconds, not hours, giving them more time and flexibility to dream big on each design — as they’ve been doing since 1887.

- **Cottrell Boatbuilding** writes high-quality social posts with help from Gemini in Docs, winning back time to focus on the craft they've honed for 40+ years.

- **Empresas Lipigas**, a leading gas sales and distribution company in Chile, is using Google Cloud's AI to build a cloud-based model that will streamline the creation of proposals for their bulk clients, resulting in faster response times and taking into account the specific needs of each project and current regulations.

- \* **Kärcher**, the global leader in cleaning solutions, uses Gemini to generate content, create presentation slides, and produce AI-generated videos. The AI-powered solutions are integrated into daily workflows as a smart assistant, significantly accelerating collaboration and communication across the organization.

- \* **Mercer International**, a global bio-manufacturing company operating in forests, chemical facilities, and construction sites, uses Google Vids to transform documents into professional safety training videos complete with AI voiceovers, music, and effects. The company achieved a 75% reduction in safety training production costs and condensed weeks of content development into minutes by updating materials through text editing.


### **Code Agents**

- **Broadcom**, a leading provider of semiconductors and security solutions, is using an enterprise version of Gemini Code Assist, built for teams of developers and agents and able to understand a company’s code base, standards, and conventions. \[CODE\]

- **Far Eastern New Century** ( **FENC**) worked with Microfusion to streamline cross-border operations using Google Cloud VMware Engine to deliver 99% system availability and 20% higher scalability and build AI assistants with Vertex AI and Gemini that have increased FENC’s operational efficiency by 30% to 40%.

- **Sumitomo Rubber Industries** worked with **Kyocera** to deploy Cloud Workstations, which now natively includes gen AI capabilities through Gemini Code Assist, to drastically reduce development tasks from months to minutes — accelerating software development and time to market.


### **Data Agents**

- \* **Amarilo**, one of Colombia's largest construction companies with over 100 active projects, uses BigQuery to create a centralized data repository that queries 70 million records in minutes. The platform reduced data query times from 5 hours to minutes and decreased data loading time by 80%.

- **Bayer Crop Science** has developed Climate FieldView, a comprehensive agricultural platform with more than 250 layers of data and billions of data points; AI-powered recommendations allow farmers to design and monitor their fields for greater yields and efficient fertilization, with the added benefit of reduced carbon emissions.

- **Capital** **Energy**, a 100% renewable electricity company, is using Vertex AI and Fortinet technologies to apply AI to energy management. The company has accelerated decision-making, maximized the value of its assets, and reduced operating costs — all while strengthening enterprise security — to take sustainable energy to new heights.

- \* **Caddie** provides a cloud platform for manufacturing companies to digitize and search technical drawings, processing extremely large blueprint images that can be 10,000 times larger than typical images. The company uses Vertex AI with GPU support to analyze complex drawings with handwritten notes, stains, and various standards, enabling machine learning engineers to deploy APIs the same day they finish coding.

- **Casa** **Dos** **Ventos**, a Brazilian wind energy company, is using Vertex AI to automate processes like document analysis and image data extraction, as well as accelerating information searches in large document repositories and providing its employees with a platform that provides fast and relevant answers when consulted. In addition, Casa dos Ventos has automated the creation of project instruction files.

- \* **Cascades**, a public company with 10,000 employees producing sustainable packaging, hygiene, and recovery solutions, migrated its business-critical SAP environment to Google Cloud and uses BigQuery as a central data repository for employees across the company to run queries predicting financials, monitoring customer demand, and balancing manufacturing schedules.

- **COI** **Energy** is facilitating equitable green energy by leveraging advanced AI technologies to identify underutilized energy capacity, what it calls “kW for Good,” which businesses can then provide to low-income households. This offers businesses tax deductions while creating a more climate-friendly economy for all.

- **Elia** **Group**, an energy transmission provider in Northern Europe, is using Vertex AI to build an "eCO2grid" that measures and forecasts the CO2 intensity of its electricity generation, with the aim of reducing greenhouse emissions.

- **Guardian** **Bikes** specializes in kid's bikes with safer brakes, and uses Gemini in Sheets to easily query and organize the massive amounts of data its factory produces.

- **Ingrid** **Capacity**, an alternative energy supplier, uses AI combined with scenario modeling to forecast energy markets and infrastructure build-up, improving the precision of its predictions. This AI-powered forecasting has increased the total output of its asset trading operations.

- \* **Kärcher**, the global leader in cleaning solutions, uses Gemini in Google Workspace to analyze and summarize documents and simplify comparing offers from suppliers. The AI transforms tender comparison and preparation processes that were previously entirely manual and time-consuming, significantly boosting employee efficiency and productivity.

- \* **Kitz**, a leading global valve manufacturer, built their K-DAP data analytics platform using BigQuery to analyze manufacturing and demand data across their operations. The platform reduced demand calculation processing time from 1-2 hours to 20-30 seconds, enabling teams to quickly respond to customer needs and production changes.

- \* **Kraftblock**, a green tech company, uses Google Cloud Compute Engine to run simulations for its high-temperature thermal energy storage systems, helping energy-intensive industries like steel and ceramics decarbonize. This support helps the green tech startup optimize its solution and scale faster.

- \* **Labellerr**, a data labeling engine, uses Vertex AI and Cloud Run to automate annotation and smart QA to help ML teams process millions of images and thousands of hours of videos in just a few weeks.

- \* **Mitsubishi** **Heavy** **Industries** uses BigQuery and Vertex AI to predict demand for specialized sealing materials used in aircraft assembly. The system reduced monthly material waste from several million yen to eventually achieving zero waste, while enabling the team to run multiple prediction scenarios and refine accuracy based on factors like daily temperature and worker experience levels.

- \* **Panasonic** uses BigQuery, Cloud Translation API, and Natural Language API to analyze multilingual app store reviews for its Panasonic Comfort Cloud air conditioner app across 70+ countries. The Looker Studio dashboard dramatically improved the app's Google Play Store review scores by enabling the team to prioritize feature improvements based on customer feedback and reduce operational costs for data analysis.

- **Pupuk** **Indonesia**, Asia's largest fertilizer producer, implemented Vision AI and Gemini to automate document processing workflows with partner Devoteam. The company reduced data extraction time from 5-10 minutes to 40-70 seconds and now requires only a single employee to validate results.

- **Physical** **Intelligence**, a startup developing general-purpose AI for robots, recently partnered with Google Cloud to support its foundational model development, using Google Cloud’s secure and scalable AI infrastructure.

- **Solestial** optimizes production of their space-stable solar cells by tracking manufacturing data with Gemini in Sheets — bringing the future of energy a step closer to liftoff.

- **Southern California Edison** is using geospatial capabilities and AI to improve infrastructure planning and monitoring, generate new insights, and create regional resilience for communities facing climate challenges today and tomorrow.

- **Talgo**, one of the world's foremost train manufacturers, built TSMART, which can collect, ingest, store, and process more than 30,000 signals per second while providing the data needed to fuel AI models that help predict failures and problems before they occur.

- **Zebra Technologies**, maker of industry-specialized mobile computing devices, is using Gemini to deliver on-device AI capabilities that drive better work and customer experiences, including advanced analytics and AI-driven insights for retail workers so they can make in-the-moment decisions to prevent low stock or inventory shrinkage.


### **Security Agents**

- **TSMC**, one of the world’s leading chip producers, protects its data for mission-critical workloads.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Media.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Media.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Media.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Media.max-900x900.jpg)

Media, Marketing & Gaming

### **Customer Agents**

- **Dataïads** helps brands maximize the ROI of their ad spend by increasing conversion rates and average order value. It is currently evaluating Vertex AI's ability to industrialize AI models it uses to distribute traffic and generate product descriptions and images.

- \* **Dailymotion**, a video platform with over 400 million monthly users and a catalog of more than 100 million videos, implemented Vertex AI Search for media to optimize content discovery. The company achieved a 17% increase in post-search click-through rate in the first week of testing—a dramatic improvement over previous optimization efforts that peaked at 2%—while 80% of new users now perform a search during their first session.

- **Formula E** can now summarize a two-hour long race commentary into a 2-minute podcast in any language, incorporating driver data and ongoing seasonal storylines.

- **Globant**'s Advance Video Search helps audiences find the content they need, with best-quality results. Using multimodal search in Gemini models, Globant can access specific frames within a full catalog of assets, which optimizes time and cost of operations, thus improving content monetization and boosting user engagement.

- **Globo**, Latin America's largest media company, created a recommendations experience inside its streaming platform that more than doubled their click-through-play rate on videos.

- The **Golden State Warriors** consolidated all of its data into a unified data foundation in BigQuery, so the franchise can then use Vertex AI to build a content recommendation engine to bring relevant, personalized content to fans, including real-time game highlights, scores and stats, and alerts about the latest ticket sales or other entertainment events.

- \*The **Korea Economic Daily** developed ALICE, an AI-powered news search and curation service using Vertex AI, Vertex Search, and Gemini to process its extensive news archives and deliver personalized content. The system uses isolated tenant architecture for secure data processing and enables readers to search using natural language queries, with Gemini providing summarized answers with citations to maintain information accuracy and trust.

- \* **JoongAng Ilbo**, a leading Korean newspaper founded in 1965, uses Vertex AI Search and Gemini models with 60 years of archived articles to power an AI search service that enables readers to query news using natural language and receive summarized insights with accurate temporal context through custom time-parsing agents. The RAG-based system limits searches to JoongAng Ilbo's own articles to eliminate hallucinations and provide accurate, comprehensive news information that would require multiple traditional keyword searches.

- \* **Newsweek**, the global news magazine with 60 million monthly website visitors, built an AI-enabled conversational search engine using Vertex AI and Gemini that automatically translates results into seven languages. Onsite searches increased over 1,500%, from 30,000 to 500,000 per month, while article recirculation rose by 30%.

- \* **Satisfi** **Labs** will begin using Gemini models to power a new agentic platform for hundreds of customers in sports, entertainment, and tourism. The Agentic Platform delivers specialized agents for guest experiences, ticketing, on-site, safety, and merchandise tuned by industry experts to help live experience businesses sell more, service faster, and gain real-time insights from every guest conversation

- \*StatusPro builds NFL virtual reality experiences for gaming and training and is now developing its newest game on Google Cloud, including a new Gemini-powered in-game coach.

- **Spotify** has partnered with Google Cloud to cost effectively handle massive scale through BigQuery, harnessing enormous amounts of data to deliver personalized experiences to more 675 million users worldwide; Gemini also supported last year’s custom Wrapped podcasts.

- **US News** saw a double-digit impact in key metrics like click-through rate, time spent on page, and traffic volume to its pages after implementing Vertex AI Search.

- **Vertical Hoops**, a youth basketball league, uses the summarizing power of Gemini in Gmail to communicate more effectively with coaches and parents, letting founder Jason Shea shoot back to the court faster.

- **YouTube** achieved a 75% reduction in calls abandoned while waiting to speak to a representative using Customer Engagement Suite.


### **Employee Agents**

- **Adwise**, a Dutch marketing agency, relies on Google Workspace with Gemini to improve how they connect with clients; they outline new documents, summarize existing documents, and reply to emails (“With a simple prompt, Gemini responds in my tone of voice…”).

- England’s **Football Association** is training Vertex AI on the FA's historical and current scouting reports so they can be transformed into concise summaries, helping national teams discover future talent.

- **\*Formula E** uses Gemini in Google Workspace to automate repetitive tasks, format data, and summarize information. The AI is accessible across the entire business, empowering office-based teams and staff to work more efficiently.

- **Globe Telecom** integrates Gemini into Google Chat and Meet to improve its internal operations and employee experience. In Chat, Gemini powers an AI chatbot called "Ask Globe" that allows employees to quickly find information from various sources, while in Meet Gemini provides live transcriptions, summaries, and action items.

- **Gold Bond** is an advertising company that provides branded merchandise and printed materials to organizations across a broad range of industries. Google Workspace with Gemini allows them to automate workflows and speed up processes, from contract reviews to adding complex formulas in Sheets.

- The **Golden State Warriors** are using Google Workspace to automate tedious tasks that take 20 or 30 minutes and instead spend that time on the experience for its fans and staff.

- **\*Gozango**, an all-in-one marketing platform, is using Gemini 2.5 Pro Gemini 2.5 Pro in three key ways: reducing the time to model industry topics by 80%, generating thousands of ads 100x faster, and automating call outcome identification with 96% accuracy for better lead quality.

- **GrowthLoop** helps marketers and AI agents build smarter, more personalized campaigns, providing tools that optimize the power of BigQuery data to automate audience building, suggest optimal targeting, and create custom attributes.

- **\*JoongAng Ilbo**, a leading Korean newspaper founded in 1965, uses Vertex AI and Gemini in its article editing system to generate headline suggestions based on article content with appropriate length and tone. The AI tool achieves 70%+ similarity with final published headlines, providing journalists with strong starting points that capture key words and phrases before editorial review and refinement. The system also automatically summarizes front-page articles into email newsletters based on pre-designed prompts

- The **Los Angeles Rams** are utilizing AI across the board, from content analysis to player scouting.

- \* **Napster**, an immersive media and tech company, is building a no-code 3D e-commerce platform on Google Cloud using Vertex AI and Gemini. This supported 20-85% infrastructure cost reductions and saved over 3,600 developer hours, making immersive 3D web experiences accessible and affordable for its customers.

- **\*Nippon Television Network**, Japan's oldest commercial TV broadcaster, uses Gemini and Vertex AI Studio to power FACTly-Mate, a secure internal conversational AI that enables employees to brainstorm ideas, translate contracts, and summarize documents through pre-configured prompts without information leakage concerns. The chat platform achieved 2,000 unique browsers within six months of launch, with employees using it for creative "wall bouncing" ideation and common business tasks previously prohibited on public generative AI services.

- **\*Pencil**, a digital publishing platform that helps writers publish and build community, migrated its infrastructure to Google Cloud using Compute Engine, Cloud CDN, Cloud Load Balancing, Cloud Storage, Cloud Armor, and Identity and Access Management. The platform now supports over 6,000 authors who have published more than 4,000 books while handling five times more traffic than before the migration.

- **Sprinklr** built Sprinklr AI+ into its unified customer experience management platform, giving brands gen AI capabilities for customer service, insights, social media management, and marketing that have enterprise-grade governance, security, and data privacy built-in.

- **Thomson Reuters** added Gemini Pro to its suite of large language models approved for employee use; with its 2-million-token context window, Gemini makes some tasks as much as 10-times faster to process and can process entire documents in context.

- **Vimeo** teams collaborate seamlessly and boost productivity with AI-powered tools in Google Meet and Docs, Sheets, and Slides. By automating note-taking and generating summaries, Gemini lets Vimeo employees focus on collaboration and creative thinking, leading to more efficient and accurate work.

- **Warner Bros. Discovery** built an AI captioning tool with Vertex AI, delivering a 50% reduction in overall costs and an 80% reduction in the time it takes to manually caption a file without the use of machine learning.


### **Creative Agents**

- **Adobe** is incorporating Imagen 3 and Veo 2 models into its suite of products for creative professionals, beginning with Adobe Express and Project Concepts.

- \* **Afooga**, an AI-powered content experimentation factory, enables businesses to generate, test, and distribute content at massive scale from a single hypothesis, automatically optimizing across TikTok, Meta, YouTube, and more. Afooga leverages Vertex AI and Veo for generative video capabilities, and is architected entirely on Google Cloud.

- \* **Alson** **AI**, a creative platform provider, uses Veo and Gemini to power its creativity platform that helps creators turn ideas into illustrated books and animations, reducing production time from months to minutes and costs from thousands of dollars to $25.

- The **American Cornhole League** uses Gemini in Drive to select clips and write social media captions for its broadcast footage, turning an hours’ long task into a single prompt.

- \* **Ateme**, a French video streaming compression and delivery solutions provider with 580 employees across 20 countries, uses Vertex AI and Gemini models to automate multilingual subtitle generation for major telecom operators, TV channels, and streaming platforms worldwide. The AI-powered solution produces professional-quality subtitles in minutes for less than a dollar per hour of content, replacing a manual process that previously took up to 15 hours and cost several thousand euros.

- **Bending Spoons** integrated Imagen 3 into its Remini app to launch a new AI filter that transforms user photos into cartoon animals, processing 60 million photos a day for delighted users.

- **Bloomberg Connects** helps create immersive audio guides with Gemini, enhancing museum accessibility for visually impaired visitors.

- **Boyter Island SRL** uses Google Workspace with Gemini to overcome writer’s block to improve their creative process.

- **Brandtech Group** built Pencil, a gen AI platform for brands to create ads, predict performance, and optimize active campaigns.

- **CAMB.AI**, part of the Google for Startups Cloud AI Accelerator, enables storytelling in every language with foundational AI.

- **Canva** is using Vertex AI to power its Magic Design for Video, helping users skip tedious editing steps while creating shareable and engaging videos in a matter of seconds.

- \* **Capcom**, creator of hit game franchises like Monster Hunter and Street Fighter, uses Vertex AI with Gemini and Imagen 2 to automatically generate in-game object concepts and images from design documents. Individual developers can now produce ideas that previously required multiple team members working together.

- **Captions**, a next generation storytelling startup, recently released its integration with Veo 2, making it easy for users to add B-roll content to its talking videos.

- \* **Cartwheel**, a generative animation platform, helps users tell stories faster and more creatively. Its tool uses Gemini Flash for character creation prompts, Imagen for reference-image creation for 3D character development, and Veo 3 for video-to-animation input control that makes output editable by artists.

- \* **ComfyUI**, an open-source engine for visual AI, helps creators prototype and automate media generation with pre-set models and more than 20,000 extensions. The platform integrates Gemini 2.5 and Veo 3 for multimodal creation and runs on Google Cloud infrastructure.

- **Connected-Stories** is a creative management platform leveraging gen AI to transform digital content creation, personalization, and real-time optimization. Using Imagen and Gemini on Vertex AI, the platform simplifies workflows, democratizes access to data-driven creatives, and scales advertising campaigns efficiently.

- \* **Eagle** **Eye**, a leading loyalty and promotions platform provider, used BigQuery and Vertex AI to build EagleAI — an AI-powered solution that generates engaging, personalized promotions at scale that drive loyalty and customer engagement across all channels. The platform achieved 5x better engagement than traditional methods and $7 of incremental sales for every $1 invested

- **Editora Abril**, a major Brazilian publisher and printer, relies on a content recommendation model created with Vertex AI, which helped achieve a 52% chance of clicks on recommended articles, strengthening its relationship with readers.

- \* **fal**, a generative media platform for developers, accelerates generative AI model inference to improve the speed with which content is generated. The fal team is working with Google Cloud to leverage its Veo 2 technology to help its users create videos with realistic motion and high-quality output.

- \* **Figma** is helping their community create more than ever. With tools across their platform powered by Gemini’s Flash 2.5 Image model, their users can now make high quality, brand approved images with just a prompt, edit details with AI, and get all the variety their project needs.

- **Globo**, the largest media group in Latin America, is using Google Cloud AI to hyper-personalize content for its streaming users, and create a better experience for spectators.

- \* **Hedra**, an end-to-end marketing creation platform, is designed to generate high-quality content at scale. Hedra Studio combines its proprietary multimodal models with other leading models like Veo and Imagen, enabling users to produce polished marketing content for any use case. Hedra’s Live Avatars use Gemini to deliver dynamic, real-time interactive video experiences.

- \* **HeyGen**, an AI-powered video generation platform, makes creating, translating, and personalizing high-quality videos simple and accessible. HeyGen's core product leverages Gemini 2.5 Pro, Flash, and Flash-Lite to streamline content creation. With one prompt, HeyGen automates video planning, intelligently analyzes user-generated footage, and optimizes content through advanced visual and audio processing.

- **Hour One** migrated its workloads to high-performance Cloud GPUs, powering faster video content generation, better image quality, and more sophisticated AI models, improving inference speed by 1.8x and reducing inference costs by 28%.

- **Instreamatic**, part of the Google for Startups AI cloud accelerator, helps businesses maximize the potential of existing creative assets using its AI to create hundreds of hyper-personalized video and audio ad variations in minutes.

- \* **Koolio.ai** helps creators produce high-quality podcasts and audio content. Koolio.ai integrates Gemini, Lyria, and Veo to power features such as AI-generated dialogue, accurate transcription, intelligent sound effects and music selection, and audio enhancement, streamlining the entire audio creation workflow from concept to final production.

- \* **Krea.ai**, a creative suite of AI tools, offers real-time image/video generation and personalized model training for artists and marketers. It integrates with Google Cloud, including models as Veo3 and Nano Banana, to provide access to advanced models, enabling users to create high-quality ads, product photos, and game assets.

- **Lately**, part of the Google for Startups Cloud AI Accelerator, manages social media with gen AI to drive measurable engagement and ROI for businesses of all shapes, sizes, and sectors.

- **Lightricks** is developing content creation tools, including its flagship products Facetune2, Videoleap and Photoleap. Leveraging the remarkable performance and ample memory capacity of Google Cloud TPU v5p, Lightricks successfully trained its generative text-to-video model without impacting the user experience.

- **Major League Baseball** continues to innovate its Statcast platform, so teams, broadcasters, and fans have access to live in-game insights.

- \* **Mosaic** lets you build and run multimodal video-editing AI agents. A canvas of creative tools becomes your building blocks, enabling simultaneous edits and many versions on autopilot—powered by Gemini 2.5 Pro’s video understanding and Google Cloud (Storage + Cloud Run) for scalable pipelines.

- **MWM**, the company behind powerful creativity tools, such as edjing for professional DJs, is exploring advances with Gemini and Vertex AI with the aim of further driving exceptional content delivery in its family of creativity apps.

- \* **Nim.video** is an AI-first platform for instant short-form video generation from a single prompt. The multimodal platform uses top generative models, including Veo3 and Veo3 Fast, for text-to-video synthesis. It runs on Vertex AI, enabling scaled experiments and orchestration of services like speech recognition and TTS.

- \* **OpenArt** empowers social media creators and SMBs to turn ideas into stunning videos in minutes - complete with motion, music, and a narrative arc in one click. Powered by Gemini image models and Google’s Veo3 video model, it makes creating viral posts and brand content fast and effortless.

- **Paramount** currently relies on manual processes to create the essential metadata and video summaries used across its Paramount+ platform for showcasing content and creating personalized experiences for viewers. Text Bison on Vertex AI is now helping to streamline this process.

- **Photoroom**, a French startup that provides gen AI photo-editing and design capabilities to consumers and businesses, used Veo 2 and Imagen 3 to improve the quality of its offering and accelerate its development.

- **Premier Martial Arts** uses Gemini in Docs to create promotional material in minutes, instead of hours, and spend more time helping their young students build skill and confidence.

- \* **Potrero** **Labs**, a creator-focused platform, has launched Jams, an AI-first video social network empowering authentic self-expression. Its platform simplifies video creation, allowing users to record short videos and let Jams enhance them. Jams offers a simple UI with a variety of models under the hood, including Gemini 2.5 Pro for script creation, multi-modal Gemini for video analysis, and Veo 3 for backgrounds, b-rolls, and audio.

- \* **Prodia** offers APIs to integrate generative AI into creative tools. Built on Google Cloud, Prodia relies on GPUs & DWS to serve the fastest text-to-image and instruct-to-edit models in the world, as verified by Artificial Analysis benchmarks. Prodia uses Veo 3 and Nano Banana to further power multimodal AI features.

- \* **Producer.ai**, an AI music platform, trains generative music models and builds products that empower anyone to create the music they imagine. "The Producer" music collaboration agent helps users create original, studio-quality songs from text, audio, or visual prompts. Gemini on Vertex AI assists with prompt augmentation and data pipelines, while Vertex AI APIs offer access to advanced multimodal models for experimentation.

- \* **Reclip**, a "real" social media application, uses Veo and Imagen to create short, engaging animated videos from real time audio clips, captured by their proprietary app. Consumers love sharing these precious, funny and real "Reclips" with their friends and family.

- \* **Rembrand** is an AI-powered advertising platform that facilitates in-video product placements for content creators and advertisers on social media and connected TV. Powered by Google Cloud's AI Infrastructure, Rembrand enables brands to genuinely connect with audiences without disrupting the content.

- \* **Scope3** is enhancing its ad-tech platform with AI-powered features, using Gemini 2.5 Flash to offer features like real-time content classification, ensuring content is aligned with brand preference.

- \* **Scorpion**, a digital marketing company for SMBs, uses Google's Veo AI to scale video ad production. By integrating this technology into its toolkit, Scorpion makes creating professional videos for websites and advertising faster and more accessible for all businesses.

- **Sphere**, the giant globe-shaped performance and experience venue in Las Vegas, is working with Google Cloud and Google Deepmind to reimagine the Wizard of Oz for a new generation, using a specialized version of the Veo 2 video generation model to bring the film to life on a whole new scale.

- \* **Sound** **Particles**, a Portuguese audio technology company whose software powers blockbusters like Oppenheimer and Dune, developed an AI-powered binaural audio solution through the Google for Startups Cloud Program to deliver personalized 3D audio experiences over any headphones. Using Google Cloud's infrastructure, the company reduced simulation runtime from 100 hours to two seconds, making the solution affordable and scalable for millions of users.

- **Square Enix** is using customer data to develop AI-optimized marketing assets to keep its gamers engaged by sharing personalized emails suited to each player’s preferences, leading to a 20% increase in email opens and a 10% increased retention rate.

- **Synthesia**, a AI video enterprise platform, helps businesses create instructional videos for employee training, customer support, sales enablement, and product marketing. The company is using Veo 3 to contextually adapt visuals to the content delivered by its AI avatars and voices.

- **Thoughtworks** has created a new way to plan enterprise marketing events with Gemini. It enables organizations to plan personalized events in minutes, rather than weeks, emphasizing creating a variety of events that resonate deeply with customers.

- \* **Tinuiti**, a performance marketing agency, used Google's VertexAI to develop an AI-powered service that develops and optimizes ad copy to increase performance. The tool embodies a philosophy of maximizing growth by minimizing waste, and a recent experiment showed significant ROAS performance improvements compared to human-curated copy.

- \* **Toonsutra**, an India-based webcomic platform, is using Google’s Gemini AI to go global. By making stories accessible in regional languages and adding Lyria 2 for music, Gemini for voices, and Veo 3 for animation, they’re creating next-gen immersive comics.

- **Udio**, an AI music generator, uses Google Cloud TPUs to help train its models for music generation and serve its rapidly growing customer base.

- \* **Velin.ai**, a content creation platform for small businesses, offers an AI agent that explains the content and its underlying strategic implications while acting as a unified content workspace. Gemini 2.5 drafts everything from scripts to social campaigns, while Imagen 4 and Veo 3 generate aligned visuals and video clips, ensuring a consistent brand narrative across all content.

- \* **Visla** is an AI-powered video creation platform that helps businesses and creators produce pro videos in minutes. Using Google’s Imagen 4, Gemini Flash Image 2.5, Veo 3, and Visla’s AI Video Agent with Avatars, it adapts visuals, narration, and automates polished content for learning, training, and marketing.

- **Wondercraft**, an AI-powered content studio that helps users create engaging audio ads, podcasts and more, is using Gemini models to power many of its core functionalities and will soon release a new Veo 2 integration.

- **WPP** will integrate Google Cloud’s gen AI capabilities into its intelligent marketing operating system, called WPP Open, which empowers its people and clients to deliver new levels of personalization, creativity, and efficiency. This includes the use of Gemini 1.5 Pro models to supercharge both the accuracy and speed of content performance predictions.

- **ZMO AI**, a personalization engine, is using Google Cloud to build quick mobile solutions for viral video trends.


### **Data Agents**

- \* **Amber** **Mobile**, a mobile game publisher with hit titles generating tens of millions in monthly revenue and over 200 million global downloads, modernized its data lake and warehouse on Google Cloud using BigQuery, Dataproc, and Cloud Storage. The company reduced data insights acquisition time to within one day and delivered five times the data service capacity, supporting thousands of tasks daily.

- \* **AndesML**, a retail media platform, helps large enterprises launch and monetize their own ad networks by showing the right ad to the right customer at the right time. Built on Vertex AI, BigQuery, and Gemini models, the AndesML platform has delivered a 30% performance lift in customer campaigns, accelerated production time by more than 30 days, and reduced operational costs.

- \* **Audiomob**, an in-game audio ad platform, replaced its legacy business intelligence with BigQuery and Looker to gain real-time insights from its global data. This move enabled the company to handle billions of monthly transactions, contributing to triple-digit yearly revenue growth and significant savings in engineering time.

- **Formula E** developed its Driver Agent, an AI tool powered by Vertex AI and Gemini. The Driver Agent is designed to analyze extensive multimodal data generated during racing and provide actionable insights to drivers.

- **Jaguar TCS Racing** is partnering with Google Cloud to use AI for real-time analysis of race car performance data, giving them a competitive edge in Formula E racing. This collaboration aims to improve its on-track decision-making and help secure the team’s and drivers’ wins and titles.

- \* **Mavely**, an influencer marketing platform supporting more than 120,000 everyday influencers, uses BigQuery and Vertex AI to deliver real-time insights and predictive analytics that help creators optimize their content strategies. The platform has driven over $1 billion in gross merchandise value through 550 million influencer-driven purchase paths while maintaining 99.999% uptime.

- **McLaren Racing** is using Google AI to get up-to-the-millisecond insights during races and training to gain a competitive edge.

- \* **MNTN** uses Google Cloud to power its Connected TV ad platform, making TV campaigns as measurable as search or social. With AI-driven tools like MNTN Matched and Security Command Center, MNTN scales creative and targeting securely and at speed.

- \* **NACON**, a French video game publisher with 16 studios distributing games in more than 100 countries, uses BigQuery and Gemini Flash to analyze player comments from gaming platforms and social media in real time. The AI-powered platform will help Community Managers gain up to 50% more time by automating manual feedback analysis and reporting.

- **NewsCorp** uses Vertex AI to help search data across 30,000 sources and 2.5 billion news articles updated daily.

- \* **NOZ/mh:n MEDIEN**, a German publisher with more than 3,000 employees across 43 companies, migrated to Google Cloud and Google Workspace after a DDoS attack to improve collaboration and security. The company can now expand its infrastructure instantly instead of waiting up to 12 weeks and gains faster insights from BigQuery and Looker to deliver personalized content to readers.

- **Spotify** leveraged Dataflow for large-scale generation of ML podcast previews and plans to keep pushing the boundaries of what’s possible with data engineering and data science to build better experiences for its customers and creators.

- **The United Daily News Group** in Taiwan worked with Merkle to develop a new AI model using Vertex AI — creating and training an AI model in just eight months that can deliver more accurate ad targeting, increasing clickthrough rate as much as four times in some categories.


![https://storage.googleapis.com/gweb-cloudblog-publish/images/Public_Sector_NvpV4GX.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Public_Sector_NvpV4GX.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Public_Sector_NvpV4GX.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Public_Sector_NvpV4GX.max-900x900.jpg)

Public Sector & Nonprofits

### **Customer Agents**

- **Alma**, part of the Google for Startups Cloud AI Accelerator, provides personalized application support, including fast document processing with AI, to simplify US immigration for top global talent.

- \* **Arizona Health Care Cost Containment System** (AHCCCS), Arizona's Medicaid agency serving more than 2 million people, built an Opioid Use Disorder Service Provider Locator using Vertex AI and Gemini to connect residents with local treatment options. Since its late 2021 launch, the platform has reached over 20,000 unique individuals across 120 Arizona cities with a 55%+ engaged session rate.

- \* **Arizona State University**'s ASU Prep division developed Archie, a Gemini-powered chatbot that provides real-time math tutoring support for middle school and high school students. The AI tutor identifies errors, provides hints and guidance, and increased students' first-attempt correct answers by 6%.

- **Beyond 12** developed an AI-powered conversational coach with the help of Gemini 1.0 Pro. It is designed to serve first-generation college students from under-resourced communities. The AI tool interacts with students, knows their history and goals, answers questions, and evaluates their progress in a personalized way, without comparing them to others.

- **Bower**, a Swedish startup, has created an app to gamify recycling, offering rewards to users across the Nordics and UK; they've integrated generative AI into the service so users can more easily identify and input recyclable goods into the app.

- **CareerVillage** is building an app called Coach to empower job seekers, especially underrepresented youth, in their career preparedness; already featuring 35 career development activities, the aim is to have more than 100 by next year.

- The **Central Texas Regional Mobility Authority** is using Vertex AI to modernize transportation operations for a smoother, more efficient journey.

- **Justicia Lab** is developing an AI-powered assistant that will simplify legal processes for asylum seekers and immigrants; by uploading a picture from a legal letter or document, users can extract valuable information and then receive personalized guidance and next steps.

- \* **LitLab.ai**, a reading platform, leverages Veo3 and Vertex AI to generate personalized, curriculum-aligned stories and provide real-time oral reading analysis. They create decodable content and employ voice recognition for instant teacher feedback on student fluency.

- The **Minnesota Division of Driver and Vehicle Services** helps non-English speakers get licenses and other services with two-way, real-time translation.

- **mRelief** has built an SMS-accessible AI chatbot to simplify the application process for the SNAP food assistance program in the U.S., featuring easy-to-understand eligibility information and direct assistance within minutes rather than days.

- \* **Nanyang** **Technological** **University**, Singapore, deployed the Lyon Housing chatbot using Dialogflow CX and Gemini to handle student housing queries. The generative AI solution enhances student experience and saves the customer service workforce more than 100 hours per month.

- The **State of Nevada** is using AI agents to speed up unemployment claim appeals.

- The **New York State Department of Motor Vehicles** is transforming the driver service experience with AI to enable greater efficiency and accessibility within the DMV, directly benefiting the public it serves.

- **Pepperdine University** has students and faculty who speak many languages, and with Gemini in Google Meet, they can benefit from real-time translated captioning and notes.

- **The Qatari Ministry of Labour** has launched "Ouqoul," an AI-powered platform designed to connect expatriate university graduates with job opportunities in the private sector. This platform streamlines the hiring process by integrating AI-driven candidate matching with ministry services for contract authentication and work permit issuance.

- \*The **Rio De Janeiro City Data Office**, the municipal data office for Rio de Janeiro, uses Dialogflow to power its 1746 citizen service chatbot that handles urban maintenance requests and municipal inquiries. The conversational AI reduces citizen response time from 30 minutes to 5 minutes across more than 30,000 monthly conversations.

- \* **Savvy** revolutionizes learning by automatically generating flashcards and quizzes from PDFs, notes, videos, and podcasts. As students answer, Savvy leverages Gemini to dynamically grade their answers, providing instant feedback and personalized learning.

- \* **SENAI**, Brazil's national industrial training service, uses Gemini 2.0 Flash, Speech-to-Text, BigQuery, and Looker Studio to deliver language proficiency testing for workforce readiness. The platform assesses reading, logic, practical problem-solving, and speech fluency to help individuals identify skill gaps and connect with appropriate training and employment opportunities.

- **Studyhall AI**, an AI research platform, graduated from Google Cloud’s UK Growth Accelerator program and built a mobile application that uses Gemini models to help coach students on reading, writing, and exam prep.

- **Sullivan County, New York**, is utilizing gen AI to enhance citizen interactions. Despite being one of the state’s smallest counties, it has become one of the first to deploy Vertex AI to augment a constituent chatbot tool; launched in under three months with minimal staff, the bot empowers residents with increased transparency and direct communication.

- **Tabiya** has built a conversational interface, Compass, that helps young people find employment opportunities; the platform asks questions and requests information, drawing out skills and experiences and matching those to appropriate roles.

- \*The **University of Hawaii** System uses Vertex AI and BigQuery to analyze labor market data and build the Hawaii Career Pathways platform, which evaluates student qualifications and interests to create customized profiles. Gemini provides personalized guidance to align students' academic paths with career opportunities in Hawaii, helping retain graduates in the state.

- \*The **University of Hawaii** System also uses Google Translate to communicate with Pacific Islander students in their native languages, including Hawaiian, Māori, Samoan, Tongan, Cook Islands Māori, Cantonese, and Marshallese. The AI makes career guidance and communication more accessible to the diverse student population.

- \* **West Sussex County Council**, which serves 890,000 residents in the UK, uses Dialogflow to power an online chatbot that engages residents in real-time conversations to determine eligibility for adult social care services and benefits. The conversational AI helps residents quickly understand their qualification status among the 5% of inquiries that actually qualify, reducing pressure on the Customer Service Center.

- The **Var** **department** in southern France has created a team of AI experts to build AI solutions across its public service operations to see how it can make the government more responsive, efficient, and citizen-centric.


### **Employee Agents**

- **Bayes Impact** builds AI products to support nonprofits, and its flagship product, CaseAI, is a digital case manager that integrates with an NGO’s current system to add smart features to draft action plans tailored to a beneficiary’s unique history; caseworkers have saved 25 hours of work per week on average.

- **Can Do Canines** is a nonprofit that provides no-cost service dogs to persons with disabilities. The team uses Gemini in Gmail for help drafting emails, giving them more time to devote to their life-changing mission.

- **The Chef Ann Foundation** summarizes conversations with Gemini in Meet to track important info from the farmers, vendors, and school districts that help the team get healthy foods in schools nationwide.

- **Climate Ride**, an environmental and cycling fundraising organizations, uses Google Workspace for Nonprofits to collaborate remotely and automate tasks, enabling its five-person team to work more efficiently towards its mission. This increased efficiency translates to more time and resources dedicated to combating climate change.

- **CodePath** supports the next generation of engineering leaders from low-income and underrepresented communities. They use Gemini in Workspace to accelerate grant writing and recruiting so they can deepen the impact of their work.

- **The Dutch Bamboo Foundation** uses Gemini for Google Workspace to streamline everything from fundraising to research, enabling a single person to run the nonprofit effectively. This allows the founder to work strategically and maximize limited resources, ultimately advancing its mission to combat climate change

- **Erika’s Lighthouse** relies on Google Workspace with Gemini to create life-saving mental health programs for school communities worldwide. They use Gemini to automate repetitive tasks and accelerate content creation, from summarizing meeting takeaways to populating tables in Sheets to organize data.

- **The Fulton Theatre** cuts grant-writing time in half by using Gemini in Docs to fill in routine information, helping the team focus on growing the theatre and putting on shows that bring communities together.

- **The Good Earth Farm**, an animal sanctuary and event space, keeps its community updated on their favorite animals with newsletters co-written by Gemini in Docs.

- **Indigenous Made**'s cofounders improve their coordination of indigenous art markets by using suggestions from Gemini in Gmail to kick-start email responses.

- \* **Infoxchange**, a nonprofit social enterprise delivering technology for social justice, uses NotebookLM to develop training programs for four distinct audience personas by uploading data and background research to review sources, identify missing information, and elaborate on learning objectives. The AI reduced the time to create a starting point for training modules from over a week to half a day, freeing up the team to focus on strategy and client education.

- The **Mississippi Farm to School Network**, a nutrition education nonprofit, uses Gemini in Docs to proofread and organize the grant proposals that make its educational mission possible.

- \* **The National Cancer Institute**, which supports more than 3,000 scientists, partnered with Google Cloud and Barnacle Labs to develop NanCI—an app using Gemini to recommend research papers and facilitate collaboration among cancer researchers. The AI-powered app helps scientists manage the volume of more than 500 cancer research papers published daily with personalized recommendations and social networking features.

- **Opportunity@Work** is applying gen AI to scale a suite of software tools and APIs that help employers identify “STAR” job candidates — “skilled through alternative routes” such as community college, military service, and on-the-job experience — helping fill roles in a tight market and expand opportunities.

- \*The **Paraná State Department of Education**, serving 900,000 students across 2,100 schools, uses Gemini API to grade student essays and provide personalized feedback. The AI reduced grading time from 10-15 minutes per essay to under 3 minutes, freeing teachers to focus on students who need the most writing support.

- **The Red Barn**, a nonprofit that teaches children with disabilities how to work with horses, uses Gemini in Docs to help write grant proposals that allow more children to benefit from equine-assisted therapy.

- Nonprofit **Studio Be** empowers artists in New Orleans. Founder Brandan "BMike" Odums uses Gemini in Gmail to summarize and respond to hundreds of weekly emails, so he can focus more time on supporting young artists.

- **Uniformed** **Services** **University** trains the U.S. military’s medical personnel and prepares them professionally and technically for the future of digital medicine. Using Google Workspace with Gemini, they were able to support new ways of working, with 88% of pilot users reporting being more effective as what they do overall, including the acceleration of HR, academic, and proposal writing processes.

- The **U.S. Air Force** built a new proof-of-concept portal for searching, browsing, and reading e-published PDFs — all within a 90-day deadline, leveraging the prebuilt tools and speed of Vertex AI Search and Conversation.

- The **U.S. Dept. of Veterans Affairs** is using AI at the edge to improve cancer detection for service members and veterans. The Augmented Reality Microscope (ARM) is deployed at remote military treatment facilities around the world. The prototype device is helping pathologists find cancer faster and with better accuracy.

- The **U.S. Patent and Trademark Office** has improved the quality and efficiency of its patent and trademark examination process by implementing AI-driven technologies.

- **Understood.org** is using Gemini for Google Workspace to improve efficiency and communication across departments, streamlining tasks like document summarization and email writing.

- \* **West Sussex County Council**, which serves 890,000 residents in the UK, uses Dialogflow and Vertex AI to provide 14 unique generative AI agents that help council employees, particularly Adult Social Care teams, quickly access policy guides, legislation, procedures, and important documents through conversational search. The AI assistants reduce time spent searching for information and improve efficiency across internal teams.

- **The Wilmington Ballet** continues its mission of empowering students through dance with grant proposals drafted by Gemini in Docs, giving the team more time to spend nurturing the next generation of dancers.

- **YDUQS**, a Brazilian education company, uses Vertex AI to automate the screening of cover letters for student admissions, resulting in a 90% success rate and a 4-second average response time. This streamlined enrollment process has enabled YDUQS to save approximately BRL 1.5 million since adoption.


### **Creative Agents**

- \* **Bethel China**, a non-profit providing education for visually impaired children, collaborated with Google volunteers to develop 'VisAid Learn,' a platform using Gemini models, Imagen, Text-to-Speech, and MediaPipe to automatically generate teaching videos optimized for children with limited vision. The platform cuts video production time from days to about five minutes and will expand to assist over 2,000 visually impaired children across 15 schools in China and institutions in India, the Philippines, and Malaysia.

- **The Rhythm Foundation** secures funding for its free concerts with pitch decks made using Gemini in Slides, cutting the time to a first draft from hours to minutes.

- \* **Subject.com**, an AI-powered platform for grades 6-12, blends cinematic storytelling with superintelligent AI so students and teachers never get stuck. VertexAI, CloudSQL & BigQuery power Subject’s teacher assistant tool Spark, instant feedback, "ExplainThis" text simplifier, 24/7 Homework Helper, and personalized learning tied to student interests.

- **The World Bank** is developing a tool to extract key information from research literature on the causal impact of development interventions, with the ultimate goal to empower decision-makers to allocate $220 billion in annual aid and trillions in annual impact investing more effectively.

- **Wild Hearts Idaho**, a leadership program for girls, uses Gemini in Docs to write social media captions that promote its programs and help more girls find themselves in outdoor adventures.


### **Data Agents**

- The **Air Force Research Laboratory**, which helps power the innovation arm of the United States Air Force, embraced the Google Cloud ecosystem to accelerate scientific discovery, streamline operations, and address national security challenges.

- \* **Arizona State University** uses BigQuery and AI to build an enrollment propensity model that predicts the likelihood of prospective students enrolling in ASU Online. The model is four times more accurate than random predictions and increased registrations by 52% compared to traditional lead scoring methods.

- **The Asteroid Institute** is using AI to discover hidden asteroids in existing astronomical data. This is a major focus for astronomers researching the evolution of the Solar System, investors and businesses hoping to fly missions to asteroids, and for all who want to prevent future large asteroid impacts on Earth.

- The **Belo Horizonte Municipal Finance Office** used AI to analyze service descriptions in invoices and assess the correctness of classifications made by the taxpayer, impacting the tax rate. Greater accuracy and efficiency has led to improved tax collections.

- **Brazil’s Ministry of Education** was facing challenges in improving the user experience of one of its mission-critical systems, SIMEC, where the ministry distributes public education policies to more than one million users. In mid-2022, SIMEC was migrated to Google Cloud ending the system's unreliability, automating processes, and reducing the number of support calls from users.

- **Broward County, Florida**, is using geospatial capabilities and AI to improve infrastructure planning and monitoring, generate new insights, and create regional resilience for communities facing climate challenges today and tomorrow.

- \* **Citylitics**, a predictive intelligence platform, transforms public infrastructure investment for municipalities, utilities, and engineering firms. By automating data processing with Dataflow and Cloud Run, it cuts analysis time by 71% and boosts data sources by 400%, helping customers proactively identify and win new business.

- **CNI**, Brazil’s **National Confederation of Industry**, is using big data, machine learning, natural language processing, and AI technologies to better understand industrial demands, as well as individual skills and the calibration of the training portfolio of the confederation's educational institutions.

- **Colombia’s Ministry of Information and Communications Technologies** uses AI and data analysis to improve the oversight, inspection, and quality control of the country's telecommunications services. They have successfully optimized processes, increased productivity, and created a more transparent and efficient ecosystem.

- **Full Fact**, a UK-based nonprofit working in 18 countries to combat misinformation, is now using gen AI to actively monitor stories so its 30 fact-checking partner organizations can focus on addressing specific claims and harmful information.

- **Fullstory**, a behavioral data platform helping brands understand customer interactions, uses Gemini integrated with its behavioral data platform to power AI agents. The AI uses session data captured from web and mobile sessions to create more informed and contextually aware AI agents that deliver better customer experiences.

- The **Israel Antiquities Authority** worked with CommIT to modernize its data systems with Google Cloud using NetApp and VMware to migrate and back up 1 petabyte of archaeological data. The Israel Antiquities Authority also trained modern research models, powered by Gemini, to help researchers quickly find and access what they are looking for.

- \* **King's College London** and **Swansea University** use Vertex AI to design nature-inspired, sustainable materials like self-healing asphalt. In a lab test, their biobased microcapsules healed a pavement crack in just fifty minutes.

- **Materiom**, a startup researching zero-waste, bio-based alternatives to fossil-fuel-made products like plastics, is creating a gen AI tool that enables entrepreneurs to develop novel compostable materials with broad applications; AI enables faster research and information gathering to speed up the development process.

- **NOAA** and **USAID** are among the U.S. government agencies using Google Cloud AI to unlock critical data insights to streamline operations and improve mission outcomes — all with an emphasis on responsible AI.

- \* **The North American Blueberry Council**, a nonprofit supporting blueberry industry stakeholders, built the BerrySmart Insights Fresh platform using Looker Embedded and BigQuery to deliver supply and demand insights to growers and suppliers across North America.

- \* **Oak Ridge National Laboratory**, part of the US Department of Energy, uses BigQuery, Cloud Storage, and Google Kubernetes Engine to analyze massive human mobility datasets for disaster response planning. The lab's DICER workflow completed computations on mobility datasets of up to 259.2 billion rows in about 23.5 hours, accelerating analysis from weeks to hours.

- **OroraTech**, a space-based wildfire detection company, leverages Google Cloud's global infrastructure and Vertex AI to enhance the speed and accuracy of its Wildfire Solution. This solution helps customers worldwide monitor forests, detect wildfires early, and protect over 1.6 million km² of forest.

- **Prodam** is the state-run company in São Paulo responsible for providing IT and data services to other agencies. It is investing in a project to standardize processes with AI, making for faster and more accurate deliveries and ensuring greater efficiency in the public service of São Paulo.

- The **Rio De Janeiro City Data Office**, founded by the mayor, proposed data integration and the development of projects using AI, like monitoring suspicious vandalism using computer vision in city tunnels.

- **Serpro**, a federalized company that provides IT solutions to the Brazilian government, adopted Google Distributed Cloud to meet strict national regulations and the highest security standards for its government cloud. The technology offers the option of physical isolation to ensure local residency of information with access restrictions.

- \* **The South Florida Water Management District** built the Kissimmee River Floodplain Hydroperiod Calculator using Google Earth Engine, Vertex AI, Cloud Run, BigQuery, and Gemini to monitor seasonal water coverage across 40 square miles of wetlands. The tool, developed in 10 months, reduced data processing times from hours to minutes, providing scientists with faster access to critical environmental data for restoration efforts.

- \*The CNRS ICB Laboratory at **Université Bourgogne Europe**, with 300 researchers, was selected as one of fifteen winners of the GÉANT European program and used Google Cloud resources to accelerate AI research including generative AI and knowledge graph construction. The lab accessed significant computing power that accelerated research timelines while providing students with practical cloud skills through workshops led by Google Cloud experts.

- \* **Warren County, Kentucky**, used Sensemaker—developed by Google's Jigsaw team and powered by Gemini on Vertex AI—to analyze community input from over 7,700 residents who shared 3,940 unique ideas and one million opinions during a month-long digital town hall about the county's growth to 2050. The AI-powered tool saved project team members an average of 28 days of work in analysis, synthesis, visualization, and report writing while helping create one of the largest digital town halls ever held in the United States.


### **Security Agents**

- The **Minas Gerais State Government** is using Vertex AI in the State Secretariat for the Environment and Sustainable Development (Semad) to implement an AI solution that will both speed up and make the processing of environmental infraction notices in the state more efficient.

- The **Government of Singapore** uses Google Cloud Web Risk, which employs AI to proactively flag unsafe websites and protect its residents online, disrupting thousands of harmful sites so far.

- **UC Riverside** adopted Google SecOps and Security Command Center for zero-trust security along with Google AI, allowing security analysts to ask Gemini questions in real time as they’re triaging issues and capturing external and internal data to solve problems quickly.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Retail.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Retail.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Retail.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Retail.max-900x900.jpg)

Retail

### **Customer Agents**

- \* **425DEGREE**, a Thailand-based specialist store for smartphone accessories and gadgets offering 50,000 products, migrated to Google Cloud to achieve seamless auto-scaling during traffic surges. The company drove 10% more additions to customer carts through personalized recommendations powered by BigQuery ML and reduced page load speed by approximately 30%.

- **Allegro**, the largest ecommerce player of European origin, enables millions of real-time, personalized conversations with AI-powered omnichannel orchestration with Google Cloud and GrowthLoop.

- **Best Buy** uses Vertex AI to condense thousands of product reviews into concise insights that help customers make informed buying decisions. The AI-powered summarization improves customer trust and satisfaction while supporting the company's goal to bring the in-store experience into customers' homes.

- \* **Best Buy** also built a Gift Finder tool using Vertex AI that simulates a human-like shopping assistant to help customers select thoughtful gifts by understanding their preferences. The generative AI solution personalizes product recommendations and helps bridge the gap between digital and in-person shopping experiences.

- **Big Sur AI** now offers its AI-powered personalization platform for retail and e-commerce customers on Google Cloud Marketplace.

- \* **blackcircles**, a UK-based online tire retailer founded in 2001 with over 2,200 partner garages, uses BigQuery, Vertex AI, and Dialogflow CX to build TyreMate—an intelligent virtual assistant that guides customers through tire purchases with personalized recommendations. The company maintains a Net Promoter Score of 79 in a traditionally complex sector, leveraging Google Cloud's data infrastructure to centralize information and deliver AI-powered customer experiences across its expanding international operations.

- **BrainLogic** uses Anthropic’s Claude models on Vertex AI to power Zapia, a personal AI assistant that caters to the Latin American market's preference for conversational commerce. Zapia supports millions of users with product discovery, local business searches, and purchase assistance, resulting in over 90% positive user feedback.

- **Cainz**, a Japanese home improvement chain, is creating an autonomous, next-generation store where advanced AI technologies, including generative AI, merge the best of online and offline shopping to deliver a faster, seamless consumer experience.

- **Carrefour Taiwan**'s AI Sommelier, a conversational AI service integrated into its app, helps customers select wines based on their preferences. Powered by Gemini models, the AI leverages a vast wine database to provide personalized recommendations, seamlessly integrating online and offline shopping.

- **Dunelm** has partnered with Google Cloud to enhance its online shopping experience with a new gen AI-driven product discovery solution. This has shown significant improvements in a number of key areas, including reduced search friction, helping customers find the products they are looking for.

- **Eezee** found Gemini models to be the most reliable option for building its Southeast Asian B2B platform that connects small businesses with suppliers of industrial and construction materials.

- \* **Erajaya**, Indonesia's largest lifestyle smart retailer operating brands like Eraspace and Ibox, uses Dialogflow and Vertex AI to power AI-driven customer service and semantic search across its e-commerce platform. The implementation automated customer service tasks and improved product discovery, leading to increased customer interactions and enhanced operational efficiency as the company scales to meet evolving market demands.

- \* **Etsy** uses Vertex AI, BigQuery, Dataflow, and Gemini models to personalize shopping experiences for nearly 90 million shoppers across its 130 million-item marketplace. The AI-powered approach increased listings per theme by 80x through "algotorial curation," improved SEO-driven visits by 5%, and boosted conversions by 3% through enhanced alt text generation.

- \* **FairPrice** **Group** is powering their Store of Tomorrow, across their smart carts, digital wine sommelier, and Grocer Genie, their intelligent app for their frontline workers. It was truly the future of shopping.

- \* **FamilyMart**, one of Taiwan's largest convenience store chains, uses Vertex AI Search and BigQuery to provide a personalized shopping experience in its mobile app. By delivering more relevant search results, the company increased its in-app click-through rate by 4X.

- \* **Flor** **Keeps**, a dried flower shop in Austin, Texas, uses Gemini integrated with Gmail to summarize received emails in small points, pinpoint main topics from lengthy inquiries, and draft cohesive responses to customers. The AI extracts specific details from emails (like wedding order quantities) and has saved the founder hours by reducing back-and-forth conversations, to the point where emails are no longer sent without using Gemini.

- **GroupBy**, an ecommerce service provider, developed an AI-first Search and Discovery Platform powered by Vertex AI Search for Retail. This solution is meticulously designed to optimize revenue, strengthen brand loyalty, and drive sales growth for B2C and B2B retailers.

- **Home Depot** built Magic Apron, an AI agent that offers expert guidance 24/7, providing detailed how-to instructions, product recommendations, and review summaries to make home improvement easier.

- **THE ICONIC**, Australia and New Zealand's leading fashion platform with 2 million active customers, uses Vertex AI multimodal search to enable event-based product discovery, like searching for "beach-themed party" to receive curated outfit recommendations. The AI-powered search reduced null searches from 5% to nearly zero while driving a 2.6% increase in revenue, transforming how customers discover products across 20 million monthly visits.

- **Lowe's** is revolutionizing product discovery with Vertex AI Search to generate dynamic product recommendations and address customers’ complex search queries.

- \* **Lush**, a global pioneer of ethical cosmetics, uses Vertex AI and Cloud Storage to power Lush Lens, an AI-powered image recognition system that identifies packaging-free products at checkout. The system reduced queue times during peak Christmas shopping from out-the-door to just 3 minutes, while saving 440,000 liters of water previously needed for product demonstrations.

- \* **Manhattan** **Associates**, a global leader in supply chain commerce solutions has built a chatbot with Gemini models to enable retailers to deliver faster, more consistent customer service, reducing pressure on their customer support teams.

- **Magalu**, one of Brazil’s largest retailers, has put customer service at the center of its AI strategy, including using Vertex AI to create “Lu’s Brain” to power an interactive conversational agent for Lu, Magalu's popular brand persona (the 3D bot has more than 14 million followers between TikTok and Instagram).

- **Mercado Libre** has incorporated semantic search into its digital shopping platforms, using AI embeddings from the Vertex AI Agent Builder, which greatly improved product recommendations and discoverability for more than 200 million consumers across Latin America.

- **Mercari** dramatically improves the user experience for both buyers and sellers on its ecommerce marketplace with Vertex AI and Weights & Biases.

- \* **Nectar**'s AI-driven community agents with Gemini to handle customer conversations on social platforms, influencer marketing, and real-time product feedback at scale for leading brands & retailers. By transforming unstructured social data into actionable insights and powering customer conversations, Nectar helps brands deepen relationships and drive measurable growth.

- \* **OK** **Corporation**, a discount supermarket chain with 6.77 million OK Club loyalty members, uses Firebase and Flutter to build a mobile app that digitizes membership cards and enables personalized customer communication about product offerings and company values. The app leverages Firebase App Distribution for rapid testing and deployment, with Google Cloud's security solutions including Cloud Armor and Identity Platform protecting customer data.

- \* **Omoda**, the Netherlands' leading fashion retailer with 650 employees, built AI stylist using Gemini models and Vertex AI to provide personalized outfit recommendations through natural language conversations. Users of AI stylist show a conversion rate 2.5 times higher than the average customer.

- \* **PopChill**, a Taiwanese marketplace for pre-owned luxury goods, uses Vertex AI Search for commerce to provide its users with timely and relevant product recommendations. As a result, the platform has increased the click-through rate on recommended items by 2.5X.

- \* **Shop** **Global**, a major Thai ecommerce company under the Saha Group, built an AI-powered search solution using Vertex AI Search, Vertex AI Conversation, Gemini, and BigQuery that acts as a personal shopper integrated with LINE messaging app. The system delivers personalized product recommendations from over 1,000 brands in 1-2 minutes through natural language and photo search, and supported 150,000 visitors during the Saha Group Fair '25 event.

- **Target** uses Google Cloud to power AI solutions on the Target app and Target.com, including personalized Target Circle offers and Starbucks at Drive Up, its curbside pickup solution.

- **Tokopedia**, an Indonesian ecommerce leader, is using Vertex AI to improve data quality, increasing unique products being sold by 5%.

- \* **Toolstation**, one of Britain's fastest-growing tool suppliers with 580 stores, migrated its product search to Vertex AI Search for commerce, cutting searches with no results from 2% to 0.1%. The company achieved a 10% increase in click-through rate and a 5.5% increase in overall search-based revenue, while reducing irrelevant search results by 30%.

- \* **Tradera**, Sweden's largest secondhand marketplace with more than three million users, uses Gemini Flash to automate item listings by analyzing photos to generate titles, descriptions, categories, and attributes. The company increased listing completion rates by 10% while enabling users to list items in 50% less time, boosting secondhand sales across the platform.

- **Vody**, part of the Google for Startups Cloud AI Accelerator, builds fine-tuned multimodal AI models for retail, helping to improve search experiences, personalize recommendations, and enhance customer engagement.

- **Wendy’s** FreshAI pairs Gemini’s conversational AI capability with audio and visual elements to create a deeply personalized and tailored experience that is consistent and enjoyable for Wendy’s customers by freeing workers to focus on excellent service and meal preparation — marking the next evolution in the quick-serve restaurants.

- \* **Zapia** **AI**, a retail technology company, uses AI agents to support millions of users with product discovery, local business searches, and purchase assistance, resulting in over 90% positive user feedback. Its multi-agent orchestration is powered by Gemini to improve agent reasoning, reduce latency, and lower operational costs.

- \* **Zazzle** is a global platform for custom products and designs made on demand. Zazzle uses Gemini ADK and CCaaS to facilitate chat-based product discovery and enhance customer experience, making it easier to find the right designs across a wide range of products.


### **Employee Agents**

- **3 Farm Daughters**, a family-owned pasta company, writes social media posts with help from Gemini in Docs, making it easier for the three sisters-turned-cofounders to balance family life with running a business.

- \* **7-Eleven Vietnam**, serving 140 stores across the country, built an internal IT support chatbot using Vertex AI Agent Builder and Gemini models to help employees resolve technical issues independently. The chatbot reduced time spent fixing IT issues by 50%, lightening the workload for the IT team.

- **Arpalus** developed an app that can instantly analyze the physical shelf and notify employees about actions to take to improve it. Powered by patented computer vision and AR technology, the app now integrates Google Cloud’s gen AI to expand its vision capabilities, transforming images into 3D models for even more powerful and accurate product recognition.

- **Atlas**, an operating system for restaurants, is using AI to improve operational efficiency, drive sales, and surface customer insights for food and beverage brands across Singapore.

- **Best Buy** can generate conversation summaries in real time using Contact Center AI, allowing live agents to give their full attention to understanding and supporting customers; the result is a 30-to-90-second reduction in average call time and after-call work. Both customers and agents have cited improved satisfaction.

- **BLK & Bold**, a premium coffee company simplifies and speeds the tedious task of budgeting by asking Gemini in Sheets for help creating tables and importing data.

- \* **BuySell Technologies**, operating Japan's leading resale business for luxury goods, antiques, and precious metals, uses Vertex AI for image recognition of product photos to help appraisers identify and value items.

- \* **BuySell Technologies**,is also deploying Gemini models in an internal RAG system called "BuySell Buddy" to help appraisers access product knowledge through conversational queries. The system will allow employees to ask questions like "What should I be careful about when handling old coins?" and retrieve relevant information from extensive company documents.

- **Camanchaca**, a Chilean seafood company, took only six weeks to develop Elon, a virtual assistant that aims to provide more efficient customer service through digital channels, enhancing Camanchaca's customer interactions.

- \* **Compass**, the largest real estate brokerage in the United States by sales volume, powers nearly 40,000 agents with its end-to-end technology platform. Workspace tools like Google Docs, Gmail, and Google Meet are deeply embedded in daily operations, enabling seamless information sharing across employees and agents nationwide.

- **Custard** **Stand** **Chili** co-founder Angie Cowger refines her emails with Gemini in Gmail to communicate effectively with retailers and share her family's hot dog chili nationwide.

- \* **Deeli AI**, an AI-powered platform, helps companies discover and evaluate emerging technologies to make informed investment decisions. The company builds its product and data pipeline on various services such as GCE, Cloud Run, and Dataflow, and uses models from the Vertex AI Model Garden.

- **Etsy**’s customer support team uses Gemini in Sheets to reduce the time spent analyzing customer feedback from hours to minutes, enabling them to quickly identify trends and improve customer interactions.

- \* **FairPrice**, Singapore's largest food retailer with over 12,000 staff, is building an organization-wide platform with Google Agentspace that provides a seamless research assistant searching across all documents, internal systems, and third-party applications, and a natural language task assistant. The AI aims to improve knowledge discovery, reduce manual effort, and streamline processes to foster improved customer experiences and enhanced operational efficiency.

- \* **Grupo Dia**, a Spanish multinational supermarket chain founded in 1979, uses Gemini in Google Workspace to compare complex proposals and conduct market research to stay ahead of competition. The AI helps teams save time, reduce costs, and boost productivity while ensuring data is never used to train external models.

- **Grupo Nutresa**, a leader in processed foods in Colombia and Latin America, is using Gemini for Google Workspace to streamline its processes, optimize decision-making, and increase productivity, thus driving innovation.

- **Home Depot** has built an application called Sidekick, which helps store associates manage inventory and keep shelves stocked; notably, vision models help associates prioritize which actions to take.

- \* **John Lewis & Partners**, where employees co-own the business, uses Gemini in Google Workspace to automate everyday tasks, summarize long documents and meetings, and quickly find information. Through a pilot program, Partners quickly adopted the AI to free up time for deeper, more focused work.

- **Just Salad** uses Gemini for Google Workspace to streamline communication and enhance efficiency by summarizing emails and meetings, allowing employees to focus on product development, customer service, and other tasks that contribute to the company's growth.

- **McDonald’s** will leverage data, AI, and edge technologies across its thousands of restaurants to implement innovation faster and to enhance employee and customer experiences.

- \* **Mercari**, Japan's largest online marketplace, is overhauling its contact center with Google AI to foster an "AI-Driven CS" experience, which is projected to yield 500% RoI by reducing customer service rep workload by at least 20%.

- \* **Natura**, a Brazilian cosmetics and personal care brand, has reinvented its approach to meetings with Gemini for Google Workspace.

- **Miinto** uses Vertex AI Vision to identify and merge duplicate product listings, improving the customer experience and reducing operational costs. This AI-powered solution has resulted in a 40% increase in efficiency, a 20% improvement in conversion rates, and significant cost savings.

- **Momentum Climbing Gym** uses Gemini in Meet to summarize conversations with their team members nationwide, keeping everyone on the same page as they reach for new heights.

- **Mood** **Fabrics** compares vendor proposals with Gemini in Gmail, making sure to never miss a detail while managing relations with 600+ vendors worldwide.

- **Cattlemen** **at** **Morgan** **Ranch**, a worldwide Wagyu beef supplier, carve lengthy email writing down to just minutes with Gemini in Gmail, getting them back in the saddle faster.

- **Natura**, a Brazilian cosmetics company, migrated 20,000 employees in more than 10 countries to Google Workspace, and was one of the first to pilot the Gemini side panel. The beauty leader also eliminated more than 17 hours of manual work per week with AppSheet, giving the finance team more time to focus on high-value analysis and planning.

- **Nuts.com** uses Gemini in Meet's live translation to communicate with suppliers worldwide and source the high-quality nuts they've provided since 1929.

- \* **Ocado** **Retail**, the UK's largest online-only grocery supermarket, uses Gemini in Google Workspace to automate notetaking and summarization for meetings and customize workflows. The AI empowers users to automate mundane and repetitive tasks without waiting for IT projects.

- **oogiebear**, a business specializing in baby breathing care products, uses Gemini in Gmail to quickly respond to customers and vendors, helping cofounder Dr. Nina Farzin juggle her dual roles of CEO and mom of three.

- **Schwarz Group**, Europe's largest retailer (including Lidl and Kaufland), is partnering with Google to enhance workplace productivity and security. They will use Google Workspace with client-side encryption through Schwarz Digits’ Cloud STACKIT, ensuring data sovereignty and maximizing security for their 575,000 employees.

- **Sports Basement**'s customer service team is using Gemini in Google Workspace to reduce the time spent writing emails by 30-35%. This means faster response times, happier employees, and higher quality customer interactions.

- \* **Swarovski**, the 130-year-old luxury brand operating across 140+ markets, modernized its data foundation by migrating over 1,000 data objects to BigQuery and launched Génie, a generative AI portal powered by Vertex AI and Gemini used by over 1,000 employees. The company achieved 17% higher email open rates and 7% higher click-through rates through AI personalization, while accelerating campaign localization by 10x.

- **Trace One**, a product lifecycle management provider for retail and CPG companies, began using Vertex AI to automatically extract information from complex documents in order to create up-to-date product summaries and data sheets, covering different industry and regulatory standards.

- \* **TRIAL** **Company**, a Japanese retailer operating over 300 supercenters, migrated legacy on-premises systems to Google Cloud using Hybrid Subnets and Migrate to Virtual Machines without changing IP addresses, avoiding a projected full day of downtime. The company completed the cutover in under an hour, improving infrastructure stability while establishing a foundation for future cloud-native modernization.

- **Victoria’s** **Secret** is testing AI-powered agents to help its in-store associates find information about product availability, inventory, and fitting and sizing tips, so they can better tailor recommendations to customers.

- \* **Wayfair**, one of the largest online home retailers, uses Gemini in Google Workspace applications as a thought partner for data analysis, content creation, and email writing. The AI integrates directly into daily workflows, enabling employees without technical expertise to benefit from enhanced creativity and productivity.

- **Woolworths**, the leading retailer in Australia, boosts employees’ confidence in communications with “Help me write” across Google Workspace products for more than 10,000 administrative employees.

- **Woolworths** is also using Gemini to create next-generation promotions, as well as for quickly assisting customer service reps in summarizing all previous customer interactions in real time.


### **Creative Agents**

- **Adore** **Me** marketers write differentiated product descriptions, a tedious task which used to take 30-40 hours a month, in one hour thanks to Gemini for Google Workspace.

- **Belk** **ECommerce** is using gen AI to craft better product descriptions, a necessary yet time-consuming task for digital retailers that was often previously done manually.

- **Bison Coolers**' 12-person team punch above their weight by using Gemini in Docs to write product descriptions that help keep their small business thriving.

- **Carrefour** used Vertex AI to deploy Carrefour Marketing Studio in just five weeks — an innovative solution to streamline the creation of dynamic campaigns across various social networks. In just a few clicks, marketers can build ultra-personalized campaigns to deliver customers advertising that they care about.

- **Cia.Hering**, a Brazilian textile and retail company, used Google Cloud to implement AI-powered image search, which allows its customers to find desired clothing using a photo as a reference, and the Herica chatbot, which can personalize messages and answer questions. This implementation resulted in a 16% increase in click-through rates, and a 122% higher average purchase.

- **Comoferta.com** uses Gemini and Vertex AI, to revolutionize the way Brazilian consumers compare supermarket prices. The application, which recognizes products from photos of shelves using computer vision and OCR, analyzes and compares prices in different stores, displaying the results in an organized way so that users can save on their purchases.

- **Delgado Guitars**, a family business selling handcrafted guitars, uses Gemini in Gmail to send timely and personalized responses making it easier to keep sharing the family’s three generations of experience with musicians worldwide.

- **Down the Road Spice Co.** uses Gemini in Slides to create designs promoting its spice blends, helping the family-owned business share their multi-generational recipes with the world.

- The **Estee Lauder Companies** utilizes Google Cloud AI, including Gemini, to power its language assistant, Ella. This tool allows brand leaders to generate various creative content, translate languages, and summarize meetings, enhancing productivity and customer experience.

- **Farmatodo**, a Colombian chain of self-service pharmacies, uses Google Cloud, Looker, and Gemini for Workspace to personalize customer promotions and enable self-service shopping. Implemented in just 3 weeks, the platform drove virtual sales to represent over a quarter of total sales in Colombia while self-checkout solutions now account for more than a quarter of in-store transactions.

- **Grupo Pão De Açúcar**, one of the largest retail groups in South America, adopted Vertex AI to improve sales forecasting for more than 700 stores with a portfolio of over 60,000 products in stock. This approach has generated gains in sustainability, customer satisfaction, and profitability.

- **Grupo Casas Bahia** is reinforcing its ecommerce and search experience with AI tools for the Brazilian market. Using Retail Search and Recommendations AI, product searches are now much more aligned with customer desires, resulting in a 28% increase in revenue per app user.

- **Kraft Heinz** is using Google’s media generation models, Imagen and Veo, on Vertex AI, speeding up campaign creations from eight weeks to eight hours.

- **L'Oreal Groupe** uses Veo 2 and Imagen 3 as a creative partner, enabling teams to generate diverse, cinematic shots in less time, producing hundreds of new qualitative videos across 20 more countries and languages while upholding its "trustworthy AI" values.

- **Levi's** is using AI models to help marketing teams with the first drafts for content generation and translations, while everything still has a human in the loop.

- **Mondelez** quickly generates visuals with Imagen for global brands like Oreo and Cadbury, supporting campaigns in more than 150 countries, with the goal of achieving 25% increase in ROI from generatively created content.

- \* **Ocado Retail**, the UK's largest online-only grocery supermarket with nearly 50,000 products, uses Gems to quickly create "back of pack" copy with in-depth product details for its massive catalogue. The marketing team feeds tone of voice guidelines into Gemini to write individualized, branded content with recipes and jokes that make products more appealing to shoppers.

- **Procter & Gamble** used Imagen to develop an internal gen AI platform to accelerate the creation of photo-realistic images and creative assets, giving marketing teams more time to focus on high-level planning and delivering superior experiences for its consumers.

- **Puma** is using Imagen to customize product photos on its website, saving time and ensuring they are locally relevant across markets; PUMA India has already seen a 10% increase in click through rate.

- \* **Puma** also developed its AI Creator app using AI Hypercomputer, Vertex AI, and Gemini running on NVIDIA H100 chips. They’ve democratized digital "kit"-building, with passionate user response: 180,000 unique items designed, 27,000 new user signups, and highly positive social media posts.

- **T&C Surf Design** in Hawaii writes radio copy with Gemini in Docs to help share the good vibes of 50+ years on the waves.

- **The United Nations Population Fund** has found Google Workspace with Gemini to be “a superpowered writing assistant,” where it can help a country director get the tone and formality right in an email to a government official, or a non-English speaker get their message across the way they want to.

- **Wisconsin Cheese Mart** uses Gemini in Docs to quickly write online product descriptions that inform a growing online customer base without taking time away from the hands-on in-store experience.


### **Code Agents**

- \* **Grupo** **Dia**, a Spanish multinational supermarket chain, uses App Script with Google Workspace to create automated workflows, even by users with little coding experience. The AI-powered tools help teams across stores, warehouses, and offices streamline operations while maintaining full control over data privacy and sovereignty.

- **Leroy Merlin**, a global home improvement retailer, developed its Pull Request Analyzer using Vertex AI. This gen AI solution summarizes code changes, helping developers understand projects faster and improve code review efficiency.

- **L'Oreal** developed an AI agent using LangChain and Cloud Run to provide text-to-text and text-to-image generation capabilities. This AI agent streamlines processes and enables faster development and deployment of gen AI applications, saving the company time and money.

- **Wayfair** piloted Code Assist, and those developers with the code agent were able to set up their environments 55 percent faster than before; there was also a 48 percent increase in code performance during unit testing, and 60 percent of developers reported that they were able to focus on more satisfying work.


### **Data Agents**

- **Backcountry** has reduced the burden of managing and maintaining infrastructure while providing a strong, secure, and scalable data foundation to deliver advanced gen AI capabilities in the future. The retailer relies on BigQuery and Looker for all of its data analytics, providing daily reports and insights that inform decision-making across the entire organization.

- **Coop** uses Vertex AI Forecast to predict product demand and optimize inventory levels in its distribution centers. This AI-powered forecasting has resulted in a 43% improvement in forecasting accuracy, leading to reduced food waste and improved sustainability.

- The **Estee Lauder Companies** leverages BigQuery to efficiently analyze data and improve operational efficiency.

- \* **FIFCO**, a Costa Rican beverage and food company, uses Vertex AI to classify confiscated marine shells by ecosystem and return them to their native habitats. The AI model, trained on over 18,500 photographs, classified 36,000 shells with over 90% accuracy, enabling the return of over 450 kilograms of shells to Costa Rica's marine ecosystems.

- **Fortenova Group**, one of Croatia's leading food and retail companies, created an AI inventory helper that provides grocery store managers with fresh insights to help them place more accurate orders for perishables like fruits and vegetables, reducing food waste while boosting profits.

- **GPC**, the **Genuine Parts Company**, implemented a pilot program utilizing Google Distributed Cloud in one of their Atlanta stores. This modern, distributed infrastructure approach, infused with AI, provided GPC with the agility and flexibility they needed to accelerate their development cycles and streamline store infrastructure management and operations.

- **Gordon** **Food** **Services**, the largest family-operated food distribution company in North America, is transforming decision-making across the organization with AI agents connected to their enterprise data, including Google Workspace and Salesforce, to simplify insight discovery and even recommend next steps.

- **Hunkemöller**, a leading Dutch intimate apparel brand, worked with Devoteam to develop a single, scalable modern data stack on Google Cloud that enables internal development and building advanced AI solutions.

- **Jacobsen** **Salt** **Co**. uses Gemini in Sheets to organize the constantly-changing environmental data needed to produce high-quality, hand-harvested sea salt.

- **Kindred** **Post** — a gift shop and community space in Juneau, Alaska — forecasts inventory needs for tourist season with an intricate tracker made by Gemini in Sheets.

- \* **Mattel** built an AI-powered feedback classification system powered by BigQuery, Vertex AI, and Google’s Gemini models. The system analyzes millions of feedback points from a diverse range of sources (customer reviews, social media, contact center) in seconds — delivering a staggering 100x increase in data processing capacity and slashing analysis times from a month to a single minute

- **Mercado Libre** uses Vector Search and embeddings in Vertex AI to reshape online shopping by providing precise results that best match a user's query.

- \* **MobiaAuto** migrated its automotive marketplace platform to Google Cloud in 2024 to leverage Gemini models in Vertex AI and BigQuery for AI-powered data analysis. The platform uses Kubernetes infrastructure to handle traffic peaks while connecting buyers and sellers across its classified ads portal, dealer services, and market insights offerings.

- \* **Morrisons**, one of the UK's largest supermarkets serving nine million customers weekly, migrated to BigQuery and Looker to gain real-time access to business data for the first time. The company went from daily reports to real-time insights with no more than a 15-minute delay, a 98.96% improvement.

- **NotCo**, a Chilean food tech company, partnered with Eleven Solutions to develop a conversational AI chatbot, powered by Gemini; the chatbot has revolutionized data access, allowing employees to instantly query their SAP system and gain real-time insights for faster, data-driven decision-making.

- \* **OK** **Corporation**, a discount supermarket chain operating 147 stores across the Tokyo region, uses BigQuery to process purchase data from over 100 stores and enable near real-time purchase analysis that allows stores to adjust prepared food quantities based on current sales trends. The cloud analytics platform replaced an on-premises data warehouse that couldn't handle the volume and now supports the company's goal of 20% annual growth, with plans to add machine learning for sales forecasting.

- \* **OTTO**, a leading German ecommerce retailer, implemented Google Cloud's Time-series Dense Encoder (TiDE) model on Vertex AI and Google Kubernetes Engine to enhance demand forecasting. The company improved forecasting accuracy by up to 30%, reducing inventory costs and increasing product availability for customers.

- **Revionics**' intelligent retail pricing platform has incorporated gen AI to turn big data into smarter pricing decisions. Revionics built a new chat-based AI agent that can help customers understand system configuration and optimization and dive deeper into data on the factors influencing pricing.

- **Shopify**, the leading ecommerce platform for online merchants, completely transformed its data infrastructure to bring together all of its data and connect it with the latest groundbreaking data and AI technologies to deliver powerful business intelligence and AI insights.

- \* **Simbe**, a multimodal, retail-focused computer vision company, built its AI-powered Store Intelligence platform on Google Cloud. By deploying autonomous robots and sensors, Simbe provides real-time insights into shelf inventory and price accuracy. This helps retailers reduce out-of-stock instances, improve pricing and promotion execution to the high 90% range, and achieve a 4x return on investment within 90 days.

- **Spoon Guru** uses Vertex AI to process up to 14 billion data points a day, including pack labels, ingredients, nutritional values, allergens, and other metadata, so retailers and consumers can better determine a product’s suitability for any given health, nutrition or lifestyle diet.

- **Tchibo**, a major European coffee and e-commerce company, uses Vertex AI and BigQuery to optimize its demand forecasting. This AI-powered solution, known as DEMON, generates over 6 million predictions daily, allowing Tchibo to manage warehouse supplies efficiently, reduce logistics costs, and improve product availability.

- **Unilever** created digitized distribution trade processes using BigQuery. Using in-depth analytics, Unilever can now process 75,000 orders daily and reach millions of retailers in emerging markets.

- **The Village Store** simplifies accounting for its two-person team with Gemini in Sheets, so they can get back to the hands-on work of running an old-town general store.

- **The Woobles** tracks inventory of its beginner crochet kits faster with Gemini in Sheets, easily putting together forecasts and run rates to make sure every Wooble finds a home.

- **Woodward Throwbacks**, a furniture company that uses reclaimed wood, tracks projects with help from Gemini in Sheets, creating monthly or project-based trackers suited to the team’s needs with a single prompt.


### **Security**

- **Dunelm**, a leading UK furnishings retailer, integrated Google Security Operations with Google security partner Acora, to create a comprehensive risk profile and modernized its security operations to deliver adaptive, agile, highly automated defense against even the most sophisticated threats.

- **Etsy** deployed AI-powered Google Security Operations to simplify log management and ingestion, accelerated detection creation and review, and improved incident response capabilities.

- **Grupo Boticário**, one of the largest beauty retail and cosmetics companies in Brazil, employs real-time security models to prevent fraud and to detect and respond to issues.

- **ManTech**, a defense contracting firm that provides technology services to the U.S. government, launched an advanced Google Workspace practice for secure AI-driven innovation, allowing the organizations they support to “test drive the latest in generative AI and Google Workspace…”

- **Pernambucanas**, a Brazilian retailer operating in more than 340 cities, improves fraud detection through its solutions created with AI. Using Google Cloud’s OCR technology, the company has reduced manual document evaluation by 80% and improves data collection through the analysis and processing of customer photos.

- \* **Wyze Labs** is rolling out new AI-powered anomaly detection features for its security camera systems, powered by Google’s vision AI tool.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Tech.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Tech.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Tech.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Tech.max-900x900.jpg)

Technology

### **Customer Agents**

- **Abstrakt** uses Vertex AI to enhance contact center customer experiences by transcribing calls and evaluating sentiment in real-time. This empowers call center workers to have more effective conversations, resolve issues faster, and provide a better customer experience.

- **ADT** is building a customer agent to help its millions of customers select, order, and set up their home security.

- \* **AMD**, a leader in high-performance computing, deployed a Vertex AI-powered chatbot in customer operations that pulls data related to order scheduling and deliveries to answer customer questions quickly. The natural language chatbot helps the customer service team provide faster responses by accessing real-time information from SAP systems.

- **AUI**'s Apollo AI agent empowers businesses to create complex, multi-step conversational experiences for its customers. This neuro-symbolic AI agent integrates with existing systems and tools, ensuring accurate, transparent, and compliant interactions.

- **BMC** partnered with Google Cloud to bring the power of Vertex AI and Llama 3.1 to its BMC Helix platform, which has significantly boosted accuracy for conversational AI and AIOps recommendations, giving BMC customers access to cutting-edge AI solutions tailored to their needs.

- **Character.ai** built its realistic conversational chat platform using the full stack of Google Cloud AI services, including for model training and daily operations, allowing it to manage terabytes of conversations each day without interruption.

- **Flockx** lifts people out of loneliness by connecting individuals with events, communities, and like-minded people using collaborative AI agent technology, built with Google Cloud and Elastic.

- **Gojek**, an Indonesia-based super app, launched "Dira by GoTo AI," a Bahasa Indonesia AI-powered voice assistant integrated into its GoPay service, allowing customers to use voice command to eliminate typing and scrolling, and complete tasks like bill payments and money transfers with fewer steps.

- **Hand Talk** uses AI to translate spoken and written Portuguese into Brazilian sign language using a virtual character named Hugo; the embedded AI translates the oral language into ASL gloss, then converts the gloss into signs, enabling communication and education for deaf individuals and their families.

- \* **IntentAI**, a Singapore-based SaaS company developing human-like Enterprise AI Agents for financial services and healthcare, uses Google Cloud to power over 200,000 healthcare appointments annually. The AI Agent handles 77% of customer chats and increased call center agent productivity by 2x.

- \* **Inworld**, a platform for creating AI-driven characters, uses Gemini to power personalized and engaging online experiences like virtual tutors and in-app guides. The company can cost-effectively support millions of concurrent users with just millisecond latencies.

- \* **Kata.ai**, an Indonesian Conversational AI company, uses Google Cloud's LLMs to enhance its chatbots with hyper-personalization. This has improved the company's cost efficiency by 40%.

- \* **LiveX**, customer service AI agents, uses Google Kubernetes Engine Autopilot and NVIDIA GPUs to power its platform. These technologies reduced total cost of ownership by 50% and operational costs by 66% while supporting an 85% reduction in customer support costs for one of its clients.

- \* **MOGUL.sg**, a Singapore real estate platform, launched MAIA in February 2025 — an AI agent for automated property searches and viewing appointments on WhatsApp — using Vertex AI, Gemini, and Google Maps API. The company reduced user query response time by 5-10 seconds, making interactions feel instant.

- **Moveo.AI** uses Vertex AI to train and deploy custom AI models for creating AI-powered customer experience agents. This has resulted in faster model development, improved customer engagement, increased revenue, and reduced customer churn for Moveo.AI's clients.

- \* **Owl.AI**, a sports technology company, delivers AI-powered solutions to professional sports leagues. Their offerings, which include judging and scoring, aim to enhance accuracy, consistency, and eliminate bias. Owl.AI achieves this by leveraging AI models built on Gemini and fine-tuned on Google Cloud to analyze real-time video footage of athletic performances.

- **Personal** **AI** offers a “personal language model” using only the data of one individual or brand and allowing them to control and own how it is used. Built on your own data, facts, and opinions, it creates a responsive and interactive messaging experience that helps people be more productive and deepen relationships.

- \* **Plateer** built Groobee, its AI-based ecommerce marketing solution, using Vertex AI and Gemini Flash to enable natural language product search that understands queries like "things I need for my five-year-old daughter's birthday party." Gemini Flash delivered faster response speeds and better results than other large language models while costing less than half of alternative AI models.

- \* **Quanscient**, a Finnish cloud-based multiphysics simulation platform company, built a customer support chatbot using Gemini Flash that answers natural language questions about how to design simulations by searching through text and images in the platform's documentation. The deployed chatbot lowers the barrier to entry for using the platform while reducing the workload on the customer support team.

- **Quora** developed Poe, its own generative AI platform for people to discover and chat with AI-powered bots, including Gemini, Anthropic’s Claude, Meta’s Llama, and Mistral’s Large 2 — many of which are hosted on Google Cloud’s purpose-built AI infrastructure.

- **Reddit** has launched Reddit Answers, its new conversation platform, which uses gen AI built with Gemini and Vertex AI that’s grounded in Reddit’s vast repository of information. Additionally, Reddit is using Vertex AI Search to improve its homepage experience.

- \* **Replicant** automates customer conversations for enterprise brands using voice and chat AI agents that replicate the expertise of your very best agents. Gemini helps Replicant deliver consistent service 24/7 that deploys quickly, scales effortlessly and continuously improves to boost ROI and CX.

- \* **Signify's** Philips Hue Platform, managing over 153 million connected light points worldwide, built its cloud infrastructure on Google Kubernetes Engine to handle natural lighting patterns across global time zones. The platform now processes over 3.5 billion transactions daily including 100 million lighting commands, representing a 1,150% increase in traffic over the past decade while maintaining response times under a few hundred milliseconds.

- **Simular**, part of the Google for Startups Cloud AI Accelerator, is creating personal AI agents that can use computers like a human.

- **Snap** has deployed the multimodal capability of Gemini within its “My AI” chatbot and has since seen over 2.5-times as much engagement within Snapping to My AI in the United States.

- \* **Transsion**, a leading mobile phone manufacturer with 14% global market share, built AI features for its TENCO CAMON 40 series smartphones using Gemini Flash and Imagen on Vertex AI, including a multimodal assistant named Ella that responds in 0.23 seconds. The phones support text translation in 136 languages, voice translation in 44 languages, and photo translation in 51 languages, bringing advanced AI capabilities to users in emerging markets.

- **Twilio**, a leading customer engagement platform, delivers the data, communication, and AI tools businesses need to create personalized customer experiences at scale.

- \* **VideoShow**, a mobile video editing company with nearly 400 million users globally, uses Gemini Flash, Natural Language AI, and Text-to-Speech AI to power its AI Chat language assistant product that provides accurate, emotionally intelligent conversational experiences. The assistant launched in just 3 weeks from concept to deployment using Google Cloud's multimodal AI capabilities.

- \* **vivo**, a global smartphone maker serving over 500 million users across 60+ markets, integrated Gemini on Vertex AI and Speech-to-Text with Chirp to deliver multi-language writing, summarization, and transcription features in its smartphones. The company launched its first AI phones in 2024, with the X series and V series demonstrating strong market acceptance as vivo continues expanding these AI capabilities to more users worldwide.


### **Employee Agents**

- **2bots** offers technology solutions, such as chatbots and virtual agents, built with Google Cloud’s AI solutions; these intelligent chatbots and content generation tools are transforming the way companies interact with their customers.

- \* **AMD**, a leader in high-performance computing, built a finance chatbot using Vertex AI and Cortex Framework to accelerate cash-flow forecasting. The generative AI solution enables the finance team to use natural language queries to access and analyze data from SAP systems.

- \* **AMD**, also developed a generative AI chatbot for its HR team using natural language processing to access information from SAP systems. The chatbot allows HR staff to quickly find the information they need through conversational queries.

- \* **Appier**, a SaaS company providing AI-powered marketing and advertising solutions to over 1,800 global brands across 17 offices in Asia Pacific, the US, and Europe, uses Translation AI integrated with its team communication platform to accelerate collaboration within its multilingual team. The instant translation feature allows employees to exchange ideas in their native languages and see translations alongside original text in the same window, eliminating the need to copy-paste between separate tools.

- **Augment**,  an AI-powered software development platform, is building an AI personal assistant that offers enhanced note-taking and collects information across your apps, including calendar, email, texts, and social media, so users can more quickly and easily find personal information and keep their lives organized.

- \* **Autonom8** uses Vertex AI, Gemini, and Vision AI to help enterprises build autonomous, agentic workflows on its low-code platform, achieving productivity gains in excess of 3x and a 2x acceleration in response times. The company found Gemini models superior to a leading competitor at 10x lower cost per token, enabling Autonom8 to deploy chatbots and generative AI workflows to customers in several hours.

- \* **Bobble** **AI**, a conversational keyboard platform with over 50 million users, integrates a third-party generative AI solution to enable voice-to-text conversion and AI-generated content recommendations. Migrating to Google Kubernetes Engine reduced overall cloud costs by 15%, achieved a 99.95% API success rate for real-time personalization, and accelerated incident investigation from days to real-time through Cloud Logging and Managed Service for Prometheus.

- **Box** has integrated Vertex AI to build new gen AI features that help customers more efficiently process and analyze data stored in the Box Content Cloud, including ​​deep-learning-based malware detection, timely alerts about unusual activity, and content classification that can automatically protect data.

- **Causal**'s mission is to simplify financial planning for startups. Wanting to boost performance and maximize its time and talent, Causal used Gemini to build a generative AI-powered setup wizard that helps users connect their data, analyze patterns, and generate financial models in just five minutes.

- **Clodura.ai** built a sales co-pilot using Vertex AI that analyzes organizational data to help B2B sellers close deals; the Vertex platform led to 71% less technical debt, 12-times faster app delivery, and resulted in significant customer growth.

- **Devoteam** is investing in AI by obtaining 4,000 Gemini Enterprise licenses to enhance productivity and collaboration, with the aim of becoming a leader in AI innovation and strengthening its ability to guide customers in their own AI journeys.

- **Fireflies.ai** can transcribe, summarize, and analyze meetings, recordings, and other voice conversations to save time and improve collaboration and information sharing across teams.

- \* **Flashpoint**, a global leader in threat intelligence, relies heavily on Gemini for Google Workspace to help power its operations.

- \* **Fullstory**, a behavioral data platform helping brands understand customer interactions, uses Gemini to take meeting notes, summarize them into structured format, and turn them into 30-second video scripts. The team plugs scripts into Google Vids to create videos with voiceover and imagery for customers, prospects, cold outreach, and event promotion.

- **Glean** builds on Vertex AI and BigQuery to deliver powerful, unified enterprise search across all workplace applications, websites, and data sources used within an enterprise, helping users find exactly what you need and discover the information you need to do their best work.

- \* **Gobii** provides AI agents that automate complex web tasks like forms and workflows directly in the browser. To power these intelligent agents, Gobii leverages Google Cloud, utilizing Vertex AI and our scalable GKE infrastructure.

- \* **Goodlord**, a RentTech platform that allows letting agents to manage properties and handle the entire lettings process, uses Gemini in Google Workspace to automate note taking and draft and refine emails. After the initial rollout, users were saving an hour or more per week by automating these tasks.

- \* **Guane**, a Colombian AI company, uses Vertex AI with Gemini 1.0 and Document AI to power AURA for law firms, automating the analysis of land restitution sentences and embargo notices. The platform reduced land restitution sentence processing from 12 hours to 6 minutes and processes hundreds of thousands of embargo documents in minutes.

- **LiveX** **AI** delivers AI Agents that swiftly enhance product education, boost customer conversion, reduce churn, and provide personalized customer support, with the goal of offering everyone a seamless VIP experience across their customer journey.

- **Lytehouse** provides instant video intelligence for any CCTV camera, enabling businesses to extract security, operational, and business insights from their video data by having multimodal gen AI agents monitor their cameras 24/7 — acting as coworkers for their business.

- \* **Macro**, an AI productivity platform, uses Gemini to modernize knowledge work by offering a unified workspace with features like multi-document chat and editable mind maps. The platform simplifies complex workflows and scales with demand for over 125,000 users in legal, finance, and education, while offering enterprise-grade security, data privacy, and compliance.

- **Maqqie**, a Dutch startup, worked with **Rappit** to transform the future of HR recruitment, harnessing the power Vertex AI and its pretrained models to pinpoint the best candidates from its pool of 43,000 profiles, increasing revenue and retention.

- \* **OneClass**, a Taiwan-based online education provider serving more than 120,000 K-12 students, uses Gemini models and Vertex AI to enhance study counselors' productivity by 50% through automated lesson summaries and study reports. The company shortened cross-database data processing time from weeks to one hour with BigQuery and scaled from 1,000 to over 1 million daily users with zero downtime using Firebase.

- \* **Parallel** is using Gemini models to power new products including an API for AI agents to perform high-value tasks using web data.

- **Quantum** **Metric** has introduced Felix AI, powered by Gemini Pro, to simplify digital analytics and decision-making. Felix AI automatically summarizes a user’s web or mobile session and consolidates the moments that matter most into short, readable summaries for customer service workers.

- \* **Quench.ai**, an AI workplace assistant that helps teams search across all company tools and data instantly, built its platform on Google Cloud using Cloud Run, Memorystore, and Gemini 2.5. The company reduced development time for a custom debugging tool by 85%—completing in two afternoons what previously took weeks—while giving customers faster access to the internal information they need to work productively.

- **Rubrik**, a cybersecurity company, is leveraging knowledge agents in Agentspace to develop deeper customer insights and prepare for impactful sales interactions.

- **Salesforce** is working with Google Cloud to create AI agents that work across both platforms using the newly launched Agent2Agent (A2) open protocol.

- **SAP** is using Vertex AI and Gemini in its the SAP Business Technology Platform, so business users now have new opportunities to gain actionable insights from their data using natural, everyday language.

- **ServiceNow** CRM works with Customer Engagement Suite, helping automate and personalize customer interactions across systems.

- \* **Skyvern** helps companies automate browser-based workflows with AI. Skyvern uses Large Language Models (LLMs) like Gemini 2.5 Pro and computer vision, to interact with websites, enabling it to automate tasks like filling out forms, procuring materials, and downloading invoices. Skyvern's AI agents can adapt to website changes, making automation more robust.

- \* **STACKIT**, a subsidiary of The Schwarz Group offering sovereign Google Workspace solutions in Germany, uses Gemini to summarize email inboxes and efficiently manage email content. The AI helps employees work more productively while protecting against cyber threats through a secure, browser-based environment.

- \* **Systalyze**, an enterprise AI optimization platform founded by MIT researchers, uses Google Kubernetes Engine and Google Cloud's AI infrastructure to help businesses deploy AI applications with up to 90% cost reduction. The company delivers 2-15x performance improvements across inference, fine-tuning, and training while maintaining complete data privacy, and is now available on Google Cloud Marketplace.

- \* **TeknTrash** **Robotics**, a UK company developing AI-powered waste sorting robots called ALPHA, built its Robots-as-a-Service platform on Google Cloud using Compute Engine, Cloud Data Fusion, and Cloud Storage to manage over 49 terabytes of hyperspectral imaging data. The company reduced simulation runtime dramatically and projects a 10% improvement in material recovery efficiency with potential future gains up to 50%.

- \* **Temporal**, a durable execution platform for developers, uses Vertex AI to enhance its customer support operations. The solution provides improved visibility into support trends by automatically categorizing 80% of support tickets, allowing the team to anticipate customer needs and identify new opportunities.

- \* **tenXengage**, an AI-powered channel success platform for technology companies, migrated to Google Cloud using Google Kubernetes Engine, Vertex AI, and Gemini, reducing deployment times by 50%. The company plans to integrate Gemini across the four pillars of its platform—incentives, deal acceleration, training, and partner engagement—while enabling its team to focus on high-value development activities.

- **TransCrypts** leverages Llama on Google Cloud to bring its AI-powered copilot, Castello, to thousands of customers in a matter of days. The performance and cost-efficiency of TPUs allow them to deploy these advanced models at lightning speed, handling complex workloads that would otherwise be out of reach.

- \* **Trellix**, an AI-powered cybersecurity platform provider, uses Gemini embedded in Google Docs, Sheets, and Slides to conduct industry research. Team members save time by asking Gemini questions directly from their existing projects.

- \* **Turing Enterprises** uses Gems, customized tools and prompting within Gemini, to create career-focused AI assistants tailored to technical roles that upskill and validate technical proficiency for hundreds of team members. The company also deployed Google's Career Builder Gem, which delivers personalized career guidance, motivation, and learning support, contributing to a 32% rise in team member satisfaction.

- \* **Turing** also built a custom AI model trained on internal knowledge to draft replies to HR support tickets, reducing ticket processing time by 33% after two days of development. The company has built Gems on track to automate 60% of 52,000 annual tickets by year end, freeing up staff for other HR tasks.

- **Typeface** uses gen AI to allow brands to create captivating content that deeply engages customers at scale, improving operational efficiency while retaining branding consistency and control.

- \* **Visma** **Tripletex**, Norway's premier cloud-based ERP system with 140,000 customers, uses Vertex AI and Gemini with BigQuery to automate customer support ticket summarization and categorization for 50,000 monthly queries. The solution saves the customer support team more than 8 hours per day on manual tagging and reduces customer issue analysis from two days to minutes, enabling product teams to quickly understand and address customer problems.

- **WebFX** uses Gemini in Google Workspace to brainstorm content, write emails, and plan projects in order to save time and improve the quality of work.

- \* **Zilliz**, a San Francisco-based vector database company serving over 10,000 enterprise customers including Nvidia, PayPal, and Walmart, rapidly launched Zilliz Cloud on Google Cloud by developing 50-60 microservices within just a few months using Google Kubernetes Engine. During the peak AI boom period, the platform successfully added up to hundreds of clusters per day, with only three employees managing operations and maintenance for thousands of running clusters.


### **Creative Agents**

- **Bewe**, a Colombian digital transformation platform for small and medium-sized enterprises, has created an assistant with Google Cloud's generative AI that helps businesses in the region improve customer management and loyalty, increasing conversions and user satisfaction.

- **Birdie.ai** Transforms customer feedback into insights for companies, with generative AI providing the support they need to take action. With this technology, the company has saved 3.5X more per text processed, and reduced data analysis time.

- **Bosch** **Digital**, one of Europe's leading technology and services companies, is leveraging Gemini models to make deeper connections with its global audiences: many business units have begun localizing marketing content for a diverse range of markets and demographics — saving time and costs.

- **ClearObject**, a developer of visual AI services, is using Gemini for Google Workspace to boost both external and internal content creation, exemplified by its marketing team crafting a targeted LinkedIn strategy with Gemini's assistance.

- **Features & Labels** is a generative media platform for developers, accelerating the inference of gen AI models to improve the speed in which content is generated. The F&L team is working with Google Cloud to integrate its Veo 2 technology, empowering its users to create videos with realistic motion and high-quality output.

- **Higgsfield.ai** built a number of text-to-video apps for consumers, including Diffuse 2.0, which can combine users' photos, videos, and texts through AI models to create more realistic avatars.

- **Hunty**, a Colombian HR startup, automated, scaled, and streamlined its hiring processes with generative AI solutions, helping clients improve candidate interviews and selections, and facilitating hiring.

- \* **Infinite** **Reality**, a company that helps online retailers and other industries build immersive 3D worlds for consumers, recently began using Gemini models on Google Cloud to help Infinite Reality customers quickly design and build AI-generated experiences.

- **Jasper** trains its suite of creativity-, writing-, and marketing-focused AI models on Google’s AI infrastructure, delivering on-brand, data-optimized assets faster and at scale to teams large and small.

- \* **Learner** **Net**, an edtech company serving a global community of over 20,000 learners, uses Gemini models and Vertex AI to scale content. With Google Cloud, the company achieved a 20-fold jump in content creation.

- \* **Mediology** **Software**, a digital publishing agency serving publishers across India, integrated Vertex AI and Gemini into its SORTD product set to deliver AI-powered content operations including video analysis, content summarization, image generation, and metadata enrichment. The company lowered the average time to create a news article from a one-hour video from up to three days to just three hours.

- **Nerdmonster**, a digital platform serving over 40,000 retail establishments in Brazil, uses Gemini to automatically classify and analyze images and videos from client stores, transforming visual content into actionable data and alerts. The implementation reduced operational costs by up to 40% while processing 200 to 300 images in seconds, enabling clients to understand consumer-generated content without manual categorization.

- \* **NightCafe** **Studio**, an AI art generation platform serving 25 million users, scaled from thousands to millions of AI image requests monthly using Firebase, Cloud Run, and Vertex AI with a team of just four engineers. The bootstrapped company has generated over 1 billion images and handles over 100 TB of user-generated content with Cloud Storage.

- **Pix Force** is part of the visual inspection sector and is investing in gen AI to collaborate on around 80% of document reading services. The company reduced the time to read documents and personal authorizations from three days to 15 minutes.

- **Scaleup** has created an AI-based technology that transcribes video lessons and generates subtitles in up to seven languages. This innovation improved content absorption and reduced student dropout rates before the end of the course by 17%.

- \* **Sivi**, an AI design generator, built Large Design Models on Vertex AI and integrated Gemini to create a conversational interface that generates personalized designs in over 70 languages. The company reduced design brief formation time by more than 50% and achieved engagement rates of up to 45% with the conversational model compared to traditional user interfaces.

- \* **STACKIT**, a subsidiary of The Schwarz Group offering sovereign Google Workspace solutions in Germany, uses Gemini in Google Workspace to enable rapid creation of graphics and videos and quickly generate content. The AI capabilities optimize collaboration and boost productivity while maintaining the highest level of security.

- **Trakto** has launched a platform that uses generative AI to automate ad creation at scale. The initiative allows for quick text generation and text-to-speech conversion, providing customers with a complete and scalable marketing solution. Brazil, Technology.

- \* **Trimble**, a global industrial technology leader with 12,000 employees, uses Google Vids with AI voiceover tools to create polished, branded video content and training materials. Employees generate professional narration by typing scripts, create videos for hardware assembly and troubleshooting, and replace lengthy meetings with short, focused videos for project proposals and updates.

- **Typeface** enables users to automate marketing workloads and across teams with its Arc Agent, which supports marketers with campaign performance, creative content creation updates, and audience optimization.

- **Urmobo**, a mobile-device management platform, created a virtual agent, Odin, that significantly improved user experience and reduced support tickets by enabling clients to interact with the platform using natural language.

- \* **VideoShow**, a mobile video editing company with nearly 400 million users globally, uses Gemini Flash on Vertex AI to generate creative text and story scripts, and Imagen 3 to create images from simple prompts that its proprietary algorithm converts into short videos. The AI-powered features enable one-click video creation, reducing the complexity barrier for new users and saving 3 months of model training time.


### **Code Agents**

- **accessiBe** develops technological solutions that help businesses do the very best they can to tackle web accessibility. Google Cloud AI helps accessiBe streamline its development process, reducing time-to-deploy by 5X; accessiBe's solutions, accessWidget and accessFlow, run on a 100% serverless environment and improve the accessibility of over 23,000 business websites

- **Ai2**'s full portfolio of open AI models are accessible on Vertex AI Model Garden.

- **Anyscale**’s Ray compute engine has made it easier for developers to scale the most complex workloads such as multimodal data processing, model training, and inference across traditional and generative AI. Ray is built using GPUs and TPUs on Google Cloud, offering greater AI infrastructure flexibility to users.

- **Anysphere**, the startup behind the AI-powered code editor Cursor, has integrated advanced AI features like autonomous agents and codebase-aware chat into its platform. Cursor aims to create a highly effective human-AI programmer by automating tasks, understanding entire codebases, and accelerating development velocity, using models like Gemini and Anthropic's Claude on Google Cloud's Vertex AI.

- **Arize AI**, an AI agent and engineering platform, partners with Google Cloud to help organizations successfully develop, evaluate, and observe their generative AI applications. The Arize AX platform seamlessly integrates with Vertex AI models and runs on Google Kubernetes Engine (GKE), which allows a very lean operations team to easily scale services and provide deep visibility into every layer of AI systems.

- \* **aSim**, an AI-powered mobile app development tool, allows you to quickly generate, share, and discover mini-apps. Users can instantly generate an app from a prompt, leveraging APIs/LLMs like Google Maps and Gemini, as well as image and video generation from Nano Banana and Veo 3.

- \* **Augment Code**, an AI coding assistant, integrated Anthropic’s Claude 3.5 Sonnet via Vertex AI to power its codebase chat feature. This delivered an instant improvement to chat performance after quick implementation, enhancing security and allowing customers to build and troubleshoot code faster.

- \* **Aviator**, an engineering productivity platform, uses Google Kubernetes Engine, Vertex AI, and Gemini to scale its engineering productivity platform to thousands of users while accelerating the development of new generative AI features.

- **Box** is already leveraging Gemini 2.5 to deliver more sophisticated, higher-value applications.

- **Canonical** collaborated with Google Cloud to optimize Ubuntu as a trusted, AI-ready infrastructure, designed for sovereignty, scalability, and control, serving a range of data-intensive use cases.

- **Cognizant** uses Gemini and Vertex AI to assist in software development, improving code quality and developer productivity. By integrating Gemini into its internal operations and platforms, Cognizant aims to enhance insights, optimize processes, and improve user experiences.

- **Crew AI** is providing agent-building frameworks in Vertex AI, so organizations can streamline workflows across industries with powerful AI agents.

- \* **DataCurve**, a frontier coding data analytics provider, addresses complex data challenges by combining Web3 and generative AI on Google Cloud. Its platform uses AI agents for deep data analysis and Web3 for data authenticity, delivering insights that help customers take action and improve engagement.

- \* **DeepSource**, a platform for code quality and security, leverages Gemini and Google Kubernetes Engine (GKE) to help developers automatically analyze and remediate code. The platform uses Gemini-powered AI agents for its Autofix™ remediation engine, which increases the accuracy of its static analysis and provides automated fixes. Running on GKE, DeepSource can automatically scale to process tens of millions of lines of code per day, reducing operational costs and accelerating time to market for over 6,000 companies.

- \* **Factory** **AI**, a platform for agent-driven software development, accelerates engineering by unifying context from sources like GitHub and Jira to delegate tasks like feature development and migrations. It uses Gemini 2.5 Flash for data ingestion and Gemini 2.5 Pro for advanced code/document generation.

- \* **Fireworks** **AI**, a generative AI platform, uses Google Kubernetes Engine and Compute Engine to run its fast and efficient inference engine. This enables the company to process over 140 billion tokens daily, offering customers high uptime and throughput with lower latency and costs.

- **HydroX AI**, part of the Google for Startups Cloud AI Accelerator, automate risk evaluation and compliance for gen AI models, helping to prevent unintended consequences and harmful behaviors so businesses can fully harness AI potential without sacrificing safety.

- **Instalily**, part of the Google for Startups Cloud AI Accelerator, is building a vertical AI agent platform that can build and operate entire teams of specialized AI agents that help automate B2B workflows across various departments.

- **Kahuna Labs**, part of the Google for Startups Cloud AI Accelerator, is building the industry’s first AI platform purpose-built for technical product support.

- **Labelbox** has built a fully managed AI model evaluation solution directly integrated into the Vertex AI platform, allowing Google Cloud users to seamlessly launch human evaluation jobs and set specific criteria for evaluation, such as question-answering and summarization; this eases and accelerates the ability to deploy human-in-the-loop AI systems with higher levels of trust and authority.

- **Linear**, a product development platform, built Similar Issues, a feature that uses AI to detect and prevent duplicate or overlapping tickets and ensures cleaner and more accurate data representation.

- \* **Lovable**, an AI software engineer, leverages Google Cloud's Vertex AI to deploy and unify its core language models, including Gemini and Anthropic's models. This unique orchestration enables users to create complete, full-stack web applications from plain English descriptions, effectively cutting the time required for prototype development from weeks to minutes and app development from months to hours.

- **Magic** is building a developer platform with a 100-million-token context window, so organizations can upload extremely large code bases and more easily query and build on them using gen AI assistance.

- **Meta** has partnered with Google Cloud to offer its Llama models on Vertex AI. The Llama models prioritize accessibility, efficiency, and privacy, with a focus on responsible innovation and system-level safety.

- **NetApp** allows organizations to build AI agents with Agentspace directly on their existing NetApp data — no data duplication required.

- **Pinecone** provides infrastructure for developers to build accurate, secure, and scalable AI applications, allowing companies to easily ground gen AI apps in their proprietary data for use in AI search, retrieval-augmented generation, coding agents, and more.

- \* **Qodo** addresses critical code quality concerns with an agentic platform that works within existing developer workflows. Qodo integrates into Vertex AI Model Garden and provides automated pull request reviews at no cost to open-source projects.

- **Quantiphi** saw developer productivity gains of more than 30% during its Code Assist pilot.

- \* **Quanscient**, a Finnish cloud-based multiphysics simulation platform company, built an anomaly detection tool using Gemini Flash that verifies simulation designs for flaws before users run them. The solution uses knowledge from previous simulations to flag errors immediately, saving users money on failed simulations and time spent troubleshooting.

- \* **Quanscient** alsodeveloped a coding assistant using Gemini models on Vertex AI that generates Python simulation code from natural language descriptions. The solution makes the platform's coding API accessible to users without strong programming knowledge, enabling them to design complex simulations through conversational prompts.

- **Replit**, on a mission to empower 35 million users to build applications regardless of coding experience, uses Claude 3.5 Sonnet on Vertex AI to power Replit Agent, which transforms natural language prompts into working applications deployed to Cloud Run in minutes. The AI agent has enabled over 100,000 application deployments, including projects that have grown into companies worth tens of millions of dollars, while saving users hours or weeks previously spent on coding and debugging.

- \* **Resolve** **AI**, an always-on AI SRE, autonomously investigates incidents and helps run production systems using code, infrastructure, and observability data. With the intelligence and performance of Gemini on Vertex AI, Resolve AI improves MTTR, reliability, and engineering velocity for its customers.

- **Safe Superintelligence** is partnering with Google Cloud to use its TPUs to accelerate its research and development efforts toward building a safe, superintelligent AI.

- \* **Sieve**, an AI research lab focused on video data, builds multimodal AI systems to automate dataset creation, improve data quality, and provide relevant metadata that powers frontier model training. Sieve uses Vertex AI for large-scale video processing, content moderation, and indexing, including tasks like text recognition, captioning, and enrichment.

- **Snorkel** **AI**, an AI application development company, uses Google Cloud to deploy Snorkel Flow, a data-centric platform that accelerates AI application development by up to 100 times. This platform makes AI development easy by reducing AI development time, labeling data in minutes, and adapting to data changes without manual relabeling.

- \* **spring.new**, a platform that enables anyone to build custom business applications using natural language, runs on Anthropic's Claude models and Gemini via Vertex AI with integrations to over 200 SaaS apps. The company helps customers achieve time savings of 95-99% on R&D projects, with users creating applications in 1-2 hours that previously took up to three months.

- \* **Systalyze**, an enterprise AI deployment platform, reduces the cost and complexity of AI. Through a partnership with Google Cloud, it reduces deployment costs by up to 90% and accelerates fine-tuning, inference, and agentic AI by 2–15x, while keeping data fully private and secure.

- \* **Trimble**, a global industrial technology leader, uses AppSheet to enable employees without coding experience to build applications from Google Sheets in 90 seconds. The no-code tool automates manual processes like data entry, allowing teams to create apps that simplify daily tasks with just a few clicks.

- \* **Turbopuffer**, a startup offering serverless vector and full-text search, uses Google Cloud Storage, Google Kubernetes Engine, and Google Compute Engine to help AI businesses overcome the high costs and complexity of traditional database architectures. ​Its solution has reduced AI database cost by up to 90% for customers, manages over 1 trillion documents, and handles more than 10 million writes and 10,000 queries every second.

- **Turing** is customizing Gemini Code Assist on its private codebase, empowering its developers with highly personalized and contextually relevant coding suggestions that have increased productivity by around 30% and made day-to-day coding more enjoyable.

- \* **Vercel** democratizes access to AI models through its AI SDK and AI Gateway, making it seamless for developers to integrate agentic capabilities into their applications. By providing unified access to leading models like Google's Gemini through a single interface, Vercel has enabled teams to build AI-powered features faster and more reliably.

- \* **VESSL** **AI**, an MLOps platform, uses Google Cloud to accelerate AI model development and reduce costs for its users. By leveraging Google Kubernetes Engine, VESSL AI can dynamically scale ML workloads, helping users create AI models up to four times faster and realize up to 80% savings on cloud expenditures. The platform's integration with Vertex AI provides users with access to powerful models and AutoML solutions, further streamlining the MLOps lifecycle.

- **Weights & Biases**, a creator of AI tools for developers, created W&B Weave, a lightweight toolkit to track, evaluate, and debug gen AI applications built with Gemini, so teams can confidently go from demo to production.

- \* **Windsurf** provides an AI-powered code completion and generation tool for developers. Their AI integrates directly into IDEs, offering suggestions, generating code, and refactoring existing code. Windsurf uses Gemini 2.5 Pro to power its coding assistance IDE, and to support integrations with Cognition’s Devin AI.

- \* **Wipro**, one of India's largest technology companies offering IT services in over 165 countries, uses Gemini Code Assist to automate routine coding tasks and enhance developer productivity across its software development teams. The AI coding assistant has improved coding efficiency by 30%, freeing developers from repetitive tasks to focus on more complex, strategic initiatives that drive greater value for clients.

- **Writer** builds and trains over 17 large language models that scale up to 70 billion parameters for custom AI models using Google Cloud and NVIDIA.


### **Data Agents**

- **180 Seguros** is powering its data management platform for employees with Google Cloud AI and BigQuery to improve operational metric tracking, allowing for 3X faster query times.

- **Addy AI** is helping mortgage lenders and banks automate their lending processes with custom AI models trained on Vertex AI. For example, the platform can extract loan opportunity details from lengthy email threads with numerous attachments.

- **Agromai** uses a unified platform, powered by Google Cloud, to provide financial institutions and insurers with highly accurate risk analysis of agricultural plots. Using AI models, the company has realized significant performance gains and can now classify up to 10 million hectares per day.

- \* **AI** **Seer**, a Singapore-based deep-tech startup, built Facticity.AI—a multilingual fact-checking platform named one of TIME's Best Inventions of 2024 in the AI Category—using Cloud Run, Gemini, and Vertex AI. The company reduced backend latency from a peak of 14,693 ms to a low of 17 ms and now serves 66.67% more requests per second compared to November 2024.

- **AI21 Labs** has partnered with Google Cloud to bring the power of the Jamba 1.5 Model Family to Vertex AI. This integration offers enterprises models designed to excel in high-demand tasks like summarization, reasoning, and creative content generation.

- \* **Alphaus** provides cloud financial management solutions that help companies optimize multicloud costs and billing, using BigQuery for data analytics and Google Kubernetes Engine for processing. By migrating their database to Spanner, they reduced monthly cost fluctuations from an average of 34% down to just 4% and cut data transfer costs by 99%.

- **Aluga** **Mais** uses Vertex AI to analyze data and create a financial profile of its customers, checking civil and criminal proceedings, financial behavior, and income to the bureaucracy of the rental market in Brazil. With Document AI and BigQuery, the startup has also reduced the time for registration analysis from 90 minutes to just to 24 seconds.

- **Anthropic** has partnered with Google Cloud to offer its Claude models — including the upgraded Claude 3.5 Sonnet and Claude 3.5 Haiku — on Vertex AI Model Garden. This provides organizations with more model options for intelligence, speed, and cost-efficiency.

- **Arquivei**, which helps manage electronic tax documents quickly and securely, uses Google Cloud gen AI to discover insights and relevant data from a large volume of accounting data, as well as gaining the ability to convert tax reports into insights.

- \* **Ask-AI** solves the critical problem behind many generative AI project failures: missing context. Their Customer Context Layer unifies fragmented support data across Zendesk, Google Drive, Slack, and Salesforce, giving SaaS teams accurate answers, intelligent routing, and real-time account insights that strengthen customer relationships and improve retention.

- \* **AssemblyAI**, which builds speech-to-text and speech understanding models that solve complex audio intelligence problems like summarization and sentiment analysis, migrated to Google Cloud to train its Universal-2 model on 12.5 million hours of audio—10 times larger than its previous model. The migration delivered a 75% reduction in data storage and infrastructure costs, decreased model evaluation time from 24 hours to 20 minutes using Vertex AI, and enabled the company to release its Universal-2 model in less than six months.

- **Atlantia.ai**, a Mexican startup, is using Vertex AI and Vertex AI Search to build a platform allowing users to compare product offers in real-time based on preferences and location.

- **Birdie.ai** specializes in customer feedback analytics that provides actionable insights to companies. Using Gemini 1.5 Flash and Vertex AI, Birdie achieved a 9% improvement in model accuracy to attain a 96% accuracy rate while reducing the processed unit costs by 15%.

- \* **Box** uses Gemini on Vertex AI to develop an AI-driven metadata extraction feature that automatically captures data from large documents such as contract expiration dates and structures it for workflow integration. The solution eliminates manual processes that can consume hundreds of hours per year at enterprise companies, handling both digital documents and handwritten content while making sense of unstructured financial documents and contracts.

- **Bosch** **SDS**, which supplies technology and services globally, has integrated sustainability into its core operations. Using Google Cloud Kubernetes, BigQuery, and Firebase to manage and scale solutions, build an AI-based cognition engine, and provide real-time alerts, Bosch SDS reduced energy costs by 12%, improved indoor comfort, and better usage of renewable energy.

- **Climate Engine** and **Robeco** are using AI and geospatial technologies with their scientific expertise and investment knowledge to inform how publicly traded companies’ actions impact biodiversity.

- **Cohesity** is integrating with Agentspace to provide employees with greater data discovery for better decision-making, while also increasing security.

- **Collato**'s Vertex AI-powered assistant allows users to instantly transform raw information, including audio recordings, text, and images, into structured, polished documents, enabling users to create documents, such as requirements documents and user research summaries, in a matter of seconds.

- **Contextual** is working with Google Cloud to offer enterprises fully customizable, trustworthy, privacy-aware AI grounded in internal knowledge bases.

- \* **Crescendo** **Lab**, a provider of marketing technology solutions for e-commerce brands, uses BigQuery to analyze TB-level daily data from LINE user interactions for precise audience segmentation. This shift allows clients to generate crucial consumer segmentation reports in five minutes, a process that previously took up to five hours, enabling instant marketing strategy adjustments before major campaigns.

- **Elastic**, a leading search analytics company, partnered with Google Cloud to help SREs and SecOps use gen AI to interpret log messages and errors, optimize code, write reports, and even identify and execute a runbook.

- **Eon.io**, a cloud data protection platform, uses Google Cloud Storage and BigQuery to transform backups into AI-ready data lakes. This allows its customers to eliminate fragmented data silos, reduce secondary storage costs by up to 98%, and improve data recovery times by up to 90%.

- **Essential** **AI**, a developer of enterprise AI solutions, is using Google Cloud’s AI-optimized TPU v5p accelerator chips to train its own AI models.

- **fileAI** leverages proprietary AI to automate the processing of any file end-to-end directly into any system without manual intervention. Built for finance, logistics, and insurance teams, fileAI's AI workflows unlock unstructured data in 90% less time, saving users up to 80% in costs.

- \* **Globant**, a global technology company with over 31,000 employees and multi-year Google Cloud Partner of the Year, built a financial data warehouse using BigQuery with Gemini to automate report generation and data analysis. The self-service platform eliminated 100% of manual report generation, reduced query resolution time by 80%, and created a single source of financial truth across multiple business units acquired through rapid company growth.

- **\*Guane**, a Colombian AI company, uses Vertex AI with Gemini to power AURA for logistics companies, automating cargo transport quotes and maritime contract analysis. The platform reduced cargo transport quote generation from 30 minutes to 30 seconds and maritime contract processing from 8 hours to 30 minutes.

- **\*Guane** also uses Vertex AI, Gemini, and Document AI to power AURA for law firms, automating the analysis of land restitution sentences and embargo notices. The platform reduced land restitution sentence processing from 12 hours to 6 minutes and processes hundreds of thousands of embargo documents in minutes.

- **Hebbia**, the AI platform for knowledge work, has integrated Gemini models into its Matrix platform, which helps organizations build AI agents capable of working across all of their data.

- **Hugging** **Face** is collaborating with Google across open science, open source, cloud, and hardware to enable companies to build their own AI with the latest open models from Hugging Face and Google Cloud hardware and software.

- **Humanizadas** specializes in data intelligence for companies and used Gemini to automate the classification of online comments as toxic or those that identify people; it also optimized the extraction of information from PDFs. These have reduced the time required for these operational processes by 95%.

- **Infosys**, a global leader in next-generation digital services and consulting, optimizes digital marketplaces for a leading consumer brand manufacturer on Google Cloud, providing actionable insights on inventory planning, promotions, and product descriptions.

- **Intelligencia** **AI** is using AI models to research novel new drugs, relying on Google Cloud’s AI-optimized infrastructure to deliver scalable research that is accurate and transparent to meet the stringent needs of medicine.

- \* **Inworld**, an AI platform for builders of consumer applications, uses Google Cloud and Gemini to cost-effectively handle tens of millions of concurrent users with response times measured in milliseconds, meeting strict requirements for quality, cost control, and security.

- **Kakao** **Brain**, part of Korean technology company Kakao Group, has built a large-scale AI language model that is the largest Korean language-specific LLM in the market, with 66 billion parameters. The company also developed a text-to-image generator called Karlo.

- \* **LG** **AI** **Research** developed EXAONE 3.5, an enterprise-focused large language model using Vertex AI and Google Cloud's GPU infrastructure, achieving 56% faster inference and 72% lower costs compared to EXAONE 2.0. The 7.8B parameter model is optimized for domain-specific tasks and will be distributed through Vertex AI's Model Garden, with all training, inference, and deployment managed on Google Cloud with isolated tenant architecture for data security.

- \* **MaestroQA**, a conversation analytics data platform, is leveraging Gemini to enhance its AI-powered conversation analytics. By using Gemini, MaestroQA is improving its ability to analyze customer interactions across every channel, providing deeper insights that help businesses boost customer satisfaction and drive growth and retention.

- **Mistral AI** has partnered with Google Cloud to offer its range of models — including Codestral for code generation and Mistral Large 24.11 for complex tasks like agentic workflows — on Vertex AI.

- \* **MLtwist**, an AI data pipeline services company, processes, transcribes, translates, and labels large, complex data streams for enterprise applications. It uses Gemini and AI Studio for transcription and labeling tasks, saving approximately 63% of the time required to process even highly illegible documents.

- \* **mov** operates Kuchikomi.com, a store support SaaS platform that uses Vertex AI, BigQuery ML, and Natural Language AI to analyze customer reviews from Google Maps and 19 other platforms. The platform's AI-powered review analysis and sentiment detection help store managers respond to customer feedback efficiently, with over 2,000 unique users accessing the system within six months of launch.

- **Naologic**, an AI application platform, uses Gemini APIs, Google Kubernetes Engine , and MongoDB Atlas on Google Cloud to build apps on top of legacy ERPs. The solution delivers fast query responses regardless of complexity, enabling powerful, natural-language chat and scaling for complex AI workloads like RAG and image search.

- \* **New** **Aim**, Australia's largest private ecommerce technology company, migrated to Google Cloud to power its Dropshipzone marketplace and AirOxy.AI analytics platform for small to medium businesses. The company improved service availability from 97% to 99% and reduced infrastructure incident response time from hours to just 15 minutes.

- \* **NTT** **Data** used Cloud TPU to build domain-specific pre-trained models for government document classification and search, achieving 20 times faster training speeds than standard processors. The project successfully created six types of specialized machine learning models through over 100 training iterations, enabling accurate classification and search of government documents with complex, specialized terminology.

- **NVIDIA** is offering Google Distributed Cloud with Gemini on its NVIDIA Blackwell processors, along with NVIDIA Confidential Computing, making AI available at the edge in new ways for regulated industries and countries.

- **OpenText** offers its managed services on Google Cloud, enabling users to quickly find fast, accurate answers to inquiries that span a broad set of business domains, such as DevOps, customer service, and content management.

- **Oracle** has now integrated the full range of Oracle Database services, running on OCI, with BigQuery, Gemini, and Vertex AI.

- \* **Parseur**, a Singapore-based AI document processing platform with four team members supporting more than 50,000 users, implemented Gemini Flash and Document AI to extract data from emails and PDFs at scale. The company attributed 36.2% of overall revenue to Google Cloud AI services and grew its customer base by 50.4% year-on-year since introducing the Gemini-powered document extraction system.

- **Persistent** **Systems** has developed FinSight, a tool for analyzing financial documents Form 10-K or investment prospecta, allowing users to query the documents using natural language facilitated on Gemini models.

- \* **President** **Information** **Corporation** (PIC), a Taiwanese IT provider for the retail industry, uses Vertex AI Vision and BigQuery to create omnichannel marketing solutions. By analyzing consumer behavior, PIC helped an ecommerce client double its platform's conversion rate.

- \* **Pro-Vigil**, the largest fully customer-committed provider of video-based solutions in the US with 30,000 onsite cameras, migrated to Google Cloud to optimize its AI-enabled remote video monitoring platform. The company processes over 70 million video events monthly and is on track for significant performance improvement and cost optimization.

- \* **Quadance**, an India-based AI and automation company, used Gemini to process two million images and corresponding names from college yearbooks within one month. The company reduced development effort for the project by 50% and added a Gemini-integrated chat interface to its document storage system for faster, more relevant responses.

- \* **Satlyt**, a space compute leader, enables in-orbit AI workloads by orchestrating intersatellite communication and routing. It uses Google Cloud's Kubernetes Engine, Vertex AI, and scalable data infrastructure to deploy AI agents and plans to deploy Google's Gemma models in orbit.

- \* **Schibsted** **Marketplaces**, a leading online classifieds group in the Nordic region, migrated its recommendation engines to Bigtable and BigQuery to support machine learning model development across mobility, real estate, employment, and re-commerce verticals. The company reduced infrastructure costs by 70% while improving data access speed, allowing data scientists to develop and deliver models faster with a shorter time to market.

- \* **SE3** **Labs**, a 3D computer vision and AI company, uses Cloud Run to deploy advanced AI model technologies that create "Spatial GPTs," which are essentially AI models that can understand and interact with the world in 3D.

- **StarCloud**, part of the Google for Startups Cloud AI Accelerator, wants to transform the paradigm of hyperscale data centers, enabling the future of AI by providing the largest training clusters on data centers in space.

- **Story**, a purpose-built intellectual property blockchain, is working with Google Cloud to use its Web3 services and infrastructure to bring new capabilities to developers on its platform.

- **SuperSign**’s platform facilitates digital contract signing processes with Gemini, as well as creating solutions focused on contract summaries and comparisons, opening up new opportunities in the market.

- **Teradata** helps analyze, categorize, and summarize customer inquiries or complaints by using Google Cloud’s multimodal capabilities to process text and voice data, identify key trends, and uncover actionable insights to enhance customer loyalty.

- \* **Trellix**, an AI-powered cybersecurity platform provider, uses Gemini embedded in Google Workspace to build Looker Studio dashboards and draft formulas with correct syntax for calculated fields. The AI eliminates monotonous manual formatting work and allows the team to focus on analysis.

- \* **Trimble**, a global industrial technology leader operating in 40+ countries across construction, agriculture, and transportation, uses Gemini in Sheets to help employees create complex calculations with natural language commands. The AI summarizes long documents, generates content, and plans projects, achieving 77% adoption and making Gemini one of the company's top three Workspace applications.

- **ThoughtSpot** uses its AI agent — Spotter — to empower customers to do deep data analysis using autonomous analytics capabilities and an AI-powered chat interface.

- \* **Us** **Media**, a 25-year-old Dutch digital development company with around 20 employees, uses Google Cloud and Vertex AI to build platforms for NGOs and socially engaged organizations, managing nearly 100 projects. The company transformed archive searches from 30 minutes to several days down to a few seconds using AI, while accelerating development cycles to deliver impactful solutions for mission-driven clients.

- \* **Wipro**, one of India's largest technology companies offering IT services in over 165 countries, uses AI-powered Recommender tools to analyze its Google Cloud environment and identify inefficiencies such as unattached storage disks, idle VMs, unused IPs, idle custom images, and suboptimal configurations. The AI-driven insights enabled Wipro to implement targeted optimizations including rightsizing virtual machines and shutting down unnecessary projects, achieving multi-million dollar annual savings.

- **Zippedi**, a Chilean data capture platform, uses Google Cloud’s gen AI to power its robots and deliver real-time insights to its customers. These AI-powered robots store and process information to generate insights that optimize decision-making. The company's retail clients achieve ROI between 4x-10x with up to 3% sales increases.


### **Security Agents**

- \* **Ajax** **Systems**, a Ukraine-based security systems manufacturer protecting over four million individuals in 180+ countries, uses Gemini to automatically tag Drive documents by security level. The AI tagged 50% of all documents in one month, with totals growing by 1.5x per month until all documents were labeled, minimizing classification errors and strengthening data loss prevention.

- **Anjuna Security**, a leader in Confidential Computing, is partnering with Google Cloud to enable the secure and trustworthy use of enterprise AI workloads in the cloud. Leveraging Confidential VMs on C3 machines with Intel TDX technology, the solution ensures that data, code and models remain protected at all times — even during processing — eliminating risks of unauthorized access and tampering.

- **AppOmni** harnesses the diverse capabilities of Vertex AI in its gen AI-powered security companion, AskOmni, to provide deeper intelligent contextual security assessments to help customers manage SaaS security more efficiently.

- \* **Aptori**, an AI security company, detects vulnerabilities in AI-generated code, prioritizes risks, and automates code fixes in real-time. Aptori uses Gemini to analyze code for security weaknesses and generate context-aware fixes, integrating its AI Security Engineer directly into developer workflows.

- **Behavox** is using Google Cloud technology and LLMs to provide industry-leading regulatory compliance and front office solutions for financial institutions globally.

- **Broadcom** is modernizing its infrastructure and building a scalable and secure platform for growth, including SymantecAI, powered by Vertex AI, to provide better security monitoring and Zero Trust protection.

- \* **Chainguard**, a software supply chain security company, uses Google Cloud Run and Google Kubernetes Engine to provide developers with secure open-source building blocks. Its serverless architecture streamlines operations and product development, reducing infrastructure management costs and enabling them to scale effortlessly to meet increasing user demand.

- \* **Clavata.ai** delivers an integrated AI governance and safety platform with an intelligent, multi-modal, real-time evaluation engine powered by Gemini. Our tools enable proactive policy enforcement, dynamic debugging, iteration, observability, and problem prevention.

- **Exabeam** has built a gen AI copilot for security analysts into its New-Scale Security Operations Platform.

- \* **Fivecast**, a provider of open-source intelligence (OSINT) solutions for government, security, and financial institutions, uses Vertex AI and Gemini on Google Cloud for AI-driven threat detection and risk assessment. The platform delivers a 400% ROI for intelligence analysts and significantly improves risk assessment quality and efficiency, while Google Code Assist accelerates product development.

- \* **Galileo**, an AI observability and evaluation platform for building trustworthy AI applications, addresses the critical challenge of mitigating LLM unpredictability and hallucinations. Using Gemini to build its "evaluation agents" and running on a scalable Google Cloud infrastructure with NVIDIA GPUs, Galileo provides a holistic "trust layer" for reliable AI. This has enabled customers to de-risk over 1,000 AI applications, while go-to-market support from the Google for Startups Cloud Program helps Galileo accelerate growth and unlock new opportunities.

- \* **Moii.AI**, a software startup that transforms CCTV cameras into autonomous safety and productivity agents, uses Gemini models, Vertex AI, and BigQuery to analyze video footage and detect workplace hazards in real time. What used to take five people manually scrubbing through footage for two to three days is now a five-minute search.

- **NetRise** developed Trace to provide software supply chain security by introducing AI-powered intent-driven searches; these allow users to search their assets based on the underlying motives or purposes behind the code and configurations, rather than solely relying on signature-based methods.

- **NewPush**, a cybersecurity company, uses Google Workspace to significantly improve efficiency and security. Gemini automates time-consuming tasks like threat research and content creation, saving analysts 12 hours a week, allowing employees to focus on more strategic work.

- **Palo Alto Networks**, a leading cybersecurity provider,  is using Gemini to create a grounded AI assistant for 24/7 security platform support in order to improve agent efficiency and response time; grounding the assistant in organizational data and security protocols has greatly improved the accuracy of responses.

- **Palo Alto Networks**’s Cortex XSIAM, its AI-driven security operations platform, is built on more than a decade of expertise in machine learning models and the most comprehensive, rich, and diverse data store in the industry.

- \* **Palo** **Alto** **Networks** uses NVIDIA Triton Inference Server with NVIDIA GPUs on Google Cloud Compute Engine to power AI-driven threat detection for its data loss prevention platform. The migration from a previous cloud provider substantially reduced machine learning latency and costs while enabling near real-time detection and response to cyberattacks, leading Palo Alto Networks to plan migrating all remaining workloads to Google Cloud.

- \* **Prediction** **Guard** is using Google Cloud services like Confidential Computing and Vertex AI to support its platform for added gen AI safety.

- **Rapid7** worked with Ask AI to implement Gemini models for more efficient cybersecurity support, delivering a 30% decrease in case handling times and a 35% increase in agent capacity for better customer experiences.

- \* **Resistant** **AI**, an AI-powered security company, uses Google Cloud to build solutions that combat fraud in financial services documentation and workflows. Running on Google Cloud infrastructure, the company's specialized document fraud detectors scrutinize financial documents in 500 different ways, helping to protect automated workflows like those using Google's Document AI from sophisticated financial crime.

- **Securiti AI** has pioneered AI risk management and security with its Data + AI Command Center, a centralized platform that enables the safe use of data and gen AI, providing unified data intelligence, controls, and orchestration across hybrid multicloud environments.

- \* **Specular**, an offensive cybersecurity platform, builds AI agents using Gemini 2.5 Pro to automate attack surface management and penetration testing. Their platform automates traditional workflows to identify, assess, and remediate cybersecurity, helping enterprises proactively prioritize and respond to threats.

- **Spot AI**, a video AI startup, transforms passive security cameras into AI agents for improving security, safety, and operations in industries like manufacturing, retail, hospitals, construction and more. The team is using Google Cloud to power Iris — its new interface for building custom video AI agents.

- **Thales** is developing a global Security Operation Centre platform based on Google Cloud cybersecurity technologies and expertise, including Google Security Operations platform, VirusTotal, and Mandiant Threat Intelligence, all powered by gen AI.

- \* **Torq** uses agentic AI to automate the entire security operations lifecycle through Socrates, an AI SOC analyst that coordinates specialized agents. Running on Google Cloud's infrastructure, teams achieve 90% automation of tier-1 analyst tasks auto-remediated without human involvement, 95% decrease in manual tasks and10x faster response times.

- **Transparently.AI**'s Manipulation Risk Analyzer generates highly accurate risk reports for any organization — and for any financial year — within seconds, using AI algorithms to dig deep into large financial data sets, unearthing accounting red flags that the human eye might miss.

- ​​ **Unico**, a Brazilian technology company that validates people's real identities to ensure data privacy, puts Google Cloud's AI technologies at the core of some of its data protection solutions to help manage scale and security.

- \* **Valiance**, a deep company in India, uses Google Cloud to power an AI-driven wildlife detection system that processes 7 billion images and 30 TB of data monthly through real-time camera surveillance. The solution identifies wildlife species, triggers warnings, and alerts authorities in three seconds, reducing human fatalities from 57 to zero in deployed areas covering a population of approximately 5 million.

- \* **Verihubs**, an Indonesian identity verification company serving over 400 brands across banking, fintech, and healthcare, uses Google Kubernetes Engine to scale its verification services to over 30 million monthly requests with a 20% improvement in performance. The company leverages Gemini API and Vertex AI to develop a deepfake detection solution and created a ready-to-production service in two months through seamless integration.

- \* **Virtusa**, a global digital engineering and technology services provider for Forbes Global 2000 companies, uses Google Workspace with Gemini embedded in Docs, Sheets, and NotebookLM to help employees analyze customer data and trends, conduct industry research, and deliver technology solutions. The AI tools help Virtusa transform enterprise operations and provide better service to clients in financial services, healthcare, manufacturing, and other industries.

- **Wiz**, an Israeli cloud security startup, helps security teams empower its data teams to deploy more useful AI applications faster and more responsibly; the startup created a Vertex AI integration that helps monitor and manage the security risks associated with running AI models.

- \* **Zefr**, a global leader in responsible AI, powers Fortune 500 brand advertising with safety and suitability on platforms like YouTube and TikTok. Using patented Cognitive AI with Gemini Flash and Vertex AI, Zefr analyzes video, image, audio, and text to deliver trusted, scalable solutions.


![https://storage.googleapis.com/gweb-cloudblog-publish/images/Tele.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Tele.max-900x900.jpg)![https://storage.googleapis.com/gweb-cloudblog-publish/images/Tele.max-900x900.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Tele.max-900x900.jpg)

Telecommunications

### **Customer Agents**

- \* **Banglalink** launched REN, a Gemini-powered chatbot for its Ryze digital brand, to provide fully digital customer service to millions of young users in Bangladesh, handling balance inquiries, package purchases, bill payments, and SIM services in English, Bengali, and "Banglish" (Bengali written in Roman script). The AI assistant autonomously manages 95% of customer interactions, with only 4% requiring human intervention, significantly enhancing both customer service and satisfaction.
- **Bell Canada** has built customizable contact center solutions for its business customers that offer AI-powered agents to address callers, and Agent Assist, which listens when a human agent is on, offering suggestions and sentiment analysis. AI has contributed $20 million in savings across customer operations.
- \* **Nomad** **eSIM**, a brand of LotusFlare used by international travelers in 200 destinations, uses Gemini in Google Workspace to enable customer support agents to respond to trouble tickets more efficiently. The AI increased customer satisfaction with faster support response times.

- **Telecom Italia** ( **TIM**) implemented a Google-powered voice agent to address many customer calls, increasing efficiency by 20%.


### **Employee Agents**

- \* **Nomad eSIM** uses Gemini models to accelerate sales velocity by quickly preparing initial drafts of standard procedures and documents. The AI achieved a 15% increase in sales close rate and saved 10% of the Operations team's time in drafting SOPs.

- \* **TELUS** built Fuel iX, a proprietary generative AI platform on Vertex AI that gives 57,000+ team members access to 40+ AI models including Anthropic's Claude and Gemini, enabling the creation of 13,000+ custom AI solutions. The platform has delivered over $90 million in benefits and 500,000+ hours in time savings, with engineering teams now shipping code 30% faster.

- **TIM** **Brasil** uses Google Cloud gen AI to transcribe audio of calls made for customer service, and then classify, summarize, and qualify the customer's demand with increasing precision. The solution assists agents with their work and provides feedback to the team on best practices

- **Verizon**, the largest U.S. wireless carrier, is using AI-powered enterprise search to help teams in network operations and customer experience get the answers they need faster.

- \* **Verizon** also uses Gemini in Google Workspace to create, refine, and summarize emails and lengthy documents, and identify action items from email chains. In a user survey, 82% feel Gemini makes a positive impact on their day-to-day operations and 74% said using Gemini saves them time.

- **Vodafone** uses Vertex AI to search and understand specific commercial terms and conditions across more than 10,000 contracts with more than 800 communications operators.

- **Vodafone** also worked with Quantexa to provide clear customer insights and actionable decision intelligence with a 360-customer view for improved service experiences, built on Google Cloud and Quantexa’s Decision Intelligence platform.


### **Code Agents**

- **Nokia** leverages Vertex AI and Gemini 1.5 Pro to enhance its Network as Code platform, enabling developers to create 5G applications faster with enriched AI capabilities. This collaboration targets various industries, starting with healthcare, to improve telehealth experiences and promote innovation within Google Cloud's developer community.


### **Data Agents**

- BT Group is taking advantage of AI to deliver democratization of data for enhanced customer experience and security. Getting things done faster and with greater productivity has become a steady state.

- Cox 2M, the commercial IoT division of Cox Communications, has reduced the time to insights for non-technical users by 88% with natural-language chat and gen AI using Gemini and ThoughtSpot.

- Orange operates in 26 countries where local data must be kept in each country. They are using AI on Google Distributed Cloud to improve network performance and deliver super-responsive translation capabilities. Watch session to learn more.


### **Security Agents**

- **Vertiv** is detecting 3x the number of cyber events and closing investigations 50% faster by using the AI-powered Google Security Operations platform.

- **Vodafone** used Vertex AI along with open-source tools and Google Cloud's security foundation to establish a robust, data-driven AI security governance layer that serves more than 50,000 internal customers.


Posted in

- [AI & Machine Learning](https://cloud.google.com/blog/products/ai-machine-learning)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-2247697588.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-2247697588.max-700x700.jpg)\\
\\
AI & Machine Learning\\
\\
**5 insights to build your agentic AI advantage in 2026** \\
\\
By Anil Jain • 7-minute read](https://cloud.google.com/transform/5-insights-to-build-your-agentic-ai-advantage-in-2026)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/Sustainability_2021_GettyImages-509149293.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/Sustainability_2021_GettyImages-509149293.max-700x700.jpg)\\
\\
AI & Machine Learning\\
\\
**The "infinite capacity" myth: How AI is breaking the old cloud rules** \\
\\
By Jamie de Guerre • 3-minute read](https://cloud.google.com/transform/the-infinite-capacity-myth-how-ai-is-breaking-the-old-cloud-rules)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-171156849.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-171156849.max-700x700.jpg)\\
\\
AI & Machine Learning\\
\\
**Your agents are leaving the building** \\
\\
By Will Grannis • 6-minute read](https://cloud.google.com/transform/your-agents-are-leaving-the-building-ask-octo)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-2149589805.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/GettyImages-2149589805.max-700x700.jpg)\\
\\
AI & Machine Learning\\
\\
**The KPIs that actually matter for production AI agents** \\
\\
By Benazir Fateh • 9-minute read](https://cloud.google.com/transform/the-kpis-that-actually-matter-for-production-ai-agents)

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="LCEmiRjPEtQ.md">
<details>
<summary>Andrej Karpathy: Software Is Changing (Again)</summary>

Phase: [EXPLOITATION]

# Andrej Karpathy: Software Is Changing (Again)

[00:00] (Upbeat music plays as the screen displays "Y Combinator Presents AI Startup School" with an abstract, geometric pattern in green and teal)
Please welcome former director of AI Tesla, Andrej Karpathy.

[00:07] (Andrej Karpathy walks onto a brightly lit stage in front of a large screen displaying his name and the title "Software in the era of AI." The audience applauds and many record with their phones.)

[00:22] Um, okay. Yeah. So I'm excited to be here today to talk to you about software in the era of AI.
[00:30] (The screen changes to show a scenic photo of the Golden Gate Bridge and lavender fields, with the title "Software in the era of AI" and Andrej Karpathy's name and affiliation)
And I'm told that many of you are students, like bachelors, masters, PhD and so on, and you're about to enter the industry. And I think it's actually like an extremely unique and very interesting time to enter the industry right now. And I think fundamentally the reason for that is that, um, software is changing.
[00:48] (The screen changes to a white background with "Software is changing. (again)" in black text. Karpathy smiles)
Again. And I say again because I actually gave this talk already. Um, but the problem is that software keeps changing, so I actually have a lot of material to create new talks. And I think it's changing quite fundamentally. I think roughly speaking, software has not changed much on such a fundamental level for 70 years, and then it's changed, I think, about twice quite rapidly in the last few years. And so there's just a huge amount of work to do, a huge amount of software to write and rewrite. So let's take a look at maybe the realm of software.
[01:14] (The screen displays "Map of GitHub" with a dark blue background and many small, bright blue clusters labeled with different project names)
So if we kind of think of this as like the map of software. This is a really cool tool called Map of GitHub. Um, this is kind of like all the software that's written. Uh, these are instructions to the computer for carrying out tasks in the digital space. So if you zoom in here,
[01:25] (A zoomed-in section highlights one cluster, "Phosphorus," showing a dense network of interconnected nodes and lines)
These are all different kinds of repositories and this is all the code that has been written. And a few years ago, I kind of observed that, um, software was kind of changing and there was kind of like a new new type of software around, and I called this software 2.0 at the time.
[01:38] (The screen changes to a slide titled "Software 2.0" with an image of traditional code on top and a neural network diagram on the bottom. Text reads "Software 1.0 = code" and "Software 2.0 = weights")
And the idea here was that software 1.0 is the code you write for the computer. Software 2.0 are basically neural networks, and in particular, the weights of a neural network. And
[01:49] (Karpathy gestures while speaking)
I think like at the time, neural nets were kind of seen as like just a different kind of classifier, like a decision tree or something like that. And so I think, uh, it was kind of like, um, I I think this framing was a lot more appropriate.
[02:11] (The screen changes to compare the "Map of GitHub (Software 1.0) computer code" on the left with a "HuggingFace Model Atlas (Software 2.0) neural network weights" on the right. The HuggingFace map is a colorful, dense, radial network)
And now actually, what we have is kind of like an equivalent of GitHub in the realm of software 2.0. And I think the HuggingFace, uh, is basically equivalent of GitHub in software 2.0. And there's also Model Atlas and you can visualize all the code written there. In case you're curious, by the way, the giant circle, the point in the middle, uh, these are the parameters of Flux, the image generator.
[02:37] (Karpathy smiles and gesticulates)
And so, anytime someone tunes a LoRA on top of a Flux model, you basically create a Git commit, uh, in this space and, uh, you create a different kind of, uh, image generator.
[02:43] (The screen changes to a diagram showing "Software 1.0 computer code" pointing to "programs" which programs a "computer" with an image of a person at an old computer. Text below says "became programmable in ~1940s")
So basically, what we have is software 1.0 is the computer code that programs a computer.
[02:47] (The screen adds a second column: "Software 2.0 weights" pointing to "programs" which programs a "neural net" with an image of the AlexNet architecture. Text below says "fixed function neural net e.g. AlexNet: for image recognition (~2012)")
Software 2.0 are the weights which program neural networks. Uh, and here's an example of AlexNet image recognizer neural network. Now, so far, all of the neural networks that we've been familiar with until recently, were kind of like fixed function computers, image to categories or something like that.
[03:07] (A third column is added: "Software 3.0 prompts" pointing to "programs" which programs an "LLM". Text below says "LLM = programmable neural net (~2019)")
And I think what's changed, and I think it's a quite fundamental change, is that neural networks became programmable with large language models. And so I I see this as quite new, unique, it's new kind of a computer. And, uh, so in my mind, it's, uh, worth giving it a new designation of software 3.0. And basically, your prompts are now programs that program the LLM.
[03:30] (Karpathy claps his hands)
And, uh, remarkably, uh, these, uh, prompts are written in English. So it's kind of a very interesting programming language.
[03:34] (The screen changes to "Example: Sentiment Classification" with three columns: "Software 1.0" shows Python code, "Software 2.0" shows 10,000 positive/negative examples training a binary classifier, and "Software 3.0" shows a prompt for an LLM with few-shot examples)
Um, so maybe, uh, to, uh, summarize the difference. If you're doing sentiment classification, for example, you can imagine writing some, uh, amount of Python to to basically do sentiment classification, or you can train a neural net, or you can prompt a large language model. Uh, so here, I'm this is a few-shot prompt, and you can imagine changing it and programming the computer in a slightly different way.
[03:55] (The screen returns to the comparison of "Map of GitHub" and "HuggingFace Model Atlas" with a new icon for "Software 3.0 LLM prompts in English" at the bottom right)
So basically, we have software 1.0, software 2.0. And I think we're seeing I maybe you've seen a lot of GitHub code is not just like code anymore, there's a bunch of like English interspersed with code. And so I think kind of there's a growing category of new kind of code.
[04:12] (Karpathy raises his hands)
So, not only is it a new programming paradigm, it's also remarkable to me that it's in our native language of English. And so, when this blew my mind, uh, a few, uh, I guess years ago now, uh, I tweeted this,
[04:20] (The screen displays a screenshot of a tweet by Andrej Karpathy from Jan 24, 2023, that says "The hottest new programming language is English" with 1.1K likes, 7K retweets, and 44K bookmarks)
And, um, I think it captured the attention of a lot of people, and this is my currently pinned tweet, uh, is that remarkably, we're now programming computers in English. Now, when I was at, uh, Tesla,
[04:30] (The screen changes to "Software is eating the world Software 2.0 eating Software 1.0" with a diagram of a car's sensors feeding into a "1.0 code" (red box) and "2.0 code" (blue box), which then output "steering & acceleration". On the right is a diagram showing a car's cameras feeding into a "BEV Net" for bird's eye view predictions.)
Um, we were working on the, uh, Autopilot. And, uh, we were trying to get the car to drive. And I sort of showed this slide at the time, where you can imagine that the inputs to the car are on the bottom, and they're going through a software stack to produce the steering and acceleration.
[04:50] (Karpathy makes a gesture with his hand representing a gradual change)
And I kind of observed that over time, as we made the Autopilot better, basically, the neural network grew in capability and size. And
[05:01] (Karpathy clenches and unclenches his fists)
in addition to that, all the C++ code was being deleted, and kind of like was, um, and a lot of the kind of capabilities and functionality that was originally written in 1.0 was migrated to 2.0. So, as an example, a lot of the stitching up of information across images from the different cameras and across time was done by a neural network, and we were able to delete a lot of code.
[05:27] (The screen displays the car diagram again)
And so, the software 2.0 stack would quite literally ate through the software stack of the Autopilot. So I thought this was really remarkable at the time.
[05:36] (The screen displays a square divided into three irregularly shaped regions labeled "1.0" (red), "2.0" (blue), and "3.0" (yellow). Arrows point from 1.0 to 2.0 and from 2.0 to 3.0, and from the edges of 1.0 and 2.0 towards 3.0. Text above reads "A huge amount of Software will be (re-)written.")
And I think we're seeing the same thing again, where, uh, basically, we have a new kind of software, and it's eating through the stack. We have three completely different programming paradigms. And I think if you're entering the industry, it's a very good idea to be fluent in all of them, because they all have slight pros and cons, and you may want to program some functionality in 1.0 or 2.0 or 3.0. Are you going to train a neural net? Are you going to just prompt an LLM? Should this be a piece of code that's explicit, et cetera.
[06:05] (Karpathy makes gestures with his hands)
So, we'll all have to make these decisions, and actually potentially, uh, fluidly transition between these paradigms. So, what I wanted to get into now is,
[06:09] (The screen changes to a white background with "Part 1 How to think about LLMs" in black text)
First, I want to in the first part, talk about LLMs and how to kind of like think of this new paradigm and the ecosystem and what that looks like.
[06:21] (Karpathy smiles and gestures)
Like what are, what is this new computer? What does it look like? And what does the ecosystem look like? Um, I was struck by this quote from Andrew actually, uh, many years ago now, I think.
[06:28] (The screen changes to a white background with ""AI is the new electricity" -Andrew Ng" in black text)
And I think Andrew is going to be speaking right after me. Uh, but he said at the time, AI is the new electricity. And I do think that it, um, kind of captures something very interesting, in that LLMs certainly feel like
[06:38] (Karpathy gestures with his hands)
they have properties of utilities right now. So,
[06:42] (The screen changes to "LLMs have properties of utilities..." with bullet points on the left and an image of an electricity substation on the right. Below the image is "LLM Rankings" with a colorful bar chart)
um, LLM labs, like OpenAI, Gemini, Anthropic, et cetera, they spend CAPEX to train the LLMs, and this is kind of equivalent to build any other grid. And then there's OPEX to serve that intelligence over APIs to all of us. And this is done through metered access, where we pay per million tokens or something like that.
[07:01] (Karpathy claps his hands)
And we have a lot of demands that are very utility-like demands out of this API. We demand low latency, high uptime, consistent quality, et cetera. In electricity, you would have a transfer switch, so you can transfer your electricity source from like grid and solar or battery or generator. In LLMs, we have maybe OpenRouter and easily switch between the different types of LLMs that exist.
[07:22] (Karpathy makes hand gestures)
Because the LLMs are software, they don't compete for physical space. So it's okay to have basically like six electricity providers and you can switch between them, right? Because they don't compete in such a direct way.
[07:32] (Karpathy makes more hand gestures)
And I think what's also a little fascinating, and we saw this in the last few days actually, a lot of the LLMs went down and people were kind of like stuck and unable to work. And I think it's kind of fascinating to me that when the state-of-the-art LLMs go down, it's actually kind of like an intelligence brownout in the world. It's kind of like when the voltage is unreliable in the grid, and, uh, the planet just gets dumber
[07:54] (Karpathy makes more hand gestures)
the more reliance we have on these models, which already is like really dramatic, and I think we'll continue to grow. But LLMs don't only have properties of utilities. I think it's also fair to say that they have some properties of fabs.
[08:05] (The screen changes to "LLMs have properties of fabs..." with bullet points on the left and images of a semiconductor fabrication plant and a server room on the right)
And the reason for this is that the CAPEX required for building LLMs is actually quite large. Uh, it's not just like building some, uh, power station or something like that, right? Uh, you're investing a huge amount of money. And I think the tech tree and, uh, for the technology is growing quite rapidly. So we're in a world where we have
[08:29] (Karpathy makes hand gestures)
sort of deep tech trees, research and development, secrets that are centralizing inside the LLM labs. Um, and but I think the analogy muddies a little bit also, because as I mentioned, this is software, and software is a bit less defensible, uh, because it is so malleable.
[08:44] (Karpathy makes hand gestures)
And so, um, I think it's just an interesting kind of thing to think about potentially. There's many analogies you can make, like a 4-nanometer process node maybe is something like a cluster with certain max FLOPs. You can think about when you're using when you're using NVIDIA GPUs and you're only doing the software and you're not doing the hardware, that's kind of like the fabless model. But if you're actually also building your own hardware and you're training on TPUs if you're Google, that's kind of like the Intel model where you own your fab.
[09:05] (Karpathy makes hand gestures)
So I think there's some analogies here that make sense. But actually, I think the analogy that makes the most sense, perhaps, is that in my mind, LLMs have very strong kind of analogies to operating systems.
[09:17] (The screen changes to "LLMs have properties of Operating Systems..." with bullet points and various OS logos)
Uh, in that, this is not just electricity or water. It's not something that comes out of the tap as a commodity. Uh, this is these are now increasingly complex software ecosystems, right? So, uh, they're not just like simple commodities like electricity.
[09:30] (Karpathy makes hand gestures)
And it's kind of interesting to me that the ecosystem is shaping in a very similar kind of way where you have a few closed-source providers, like Windows or macOS, and then you have an open-source alternative like Linux. And I think for, uh, neural for LLMs as well, we have a kind of a few competing closed-source, uh, providers, and then maybe the LLaMA ecosystem is currently like, maybe a close approximation to something that may grow into something like Linux. Again, I think it's still very early because these are just simple LLMs, but we're starting to see that these are going to get a lot more complicated. It's not just about the LLM itself, it's about all the tool use and the multimodalities and how all of that works.
[10:07] (Karpathy makes hand gestures)
And so, when I sort of had this realization a while back, I tried to sketch it out.
[10:10] (The screen changes to "LLM OS" with a diagram showing an LLM as the CPU, with RAM/context window, connected to peripheral devices (video, audio, ethernet, browser), disk (file system), and other LLMs. It also interacts with "Software 1.0 tools" like calculator, Python interpreter, terminal)
And it kind of seemed to me like LLMs are kind of like a new operating system, right? So the LLM is a new kind of a computer. It's sitting, it's kind of like the CPU equivalent. Uh, the context windows are kind of like the memory. And then the LLM is orchestrating memory and compute, uh, for problem solving, um, using all of these, uh, capabilities here. And so, definitely, if you look at it, it looks very much like software operating system from that perspective.
[10:37] (The screen changes to "You can run an app like VS Code on:" with bullet points for Windows, Mac, Linux. On the right, a screenshot of the VS Code download page)
Um, a few more analogies. For example, if you want to download an app, say I go to VS Code and I go to download. You can download VS Code and you can run it on Windows, Linux, or or Mac.
[10:50] (The screen adds "Just like you can run an LLM app like Cursor on:" with bullet points for GPT o3, Claude 4-sonet, Gemini 2.5-pro, DeepSeek. On the right, a screenshot of the Cursor chat interface)
In the same way, as you can take an LLM app like Cursor, and you can run it on GPT, or Claude, or Gemini series, right? There's just a drop-down. So it's kind of like similar in that way as well.
[11:01] (The screen changes to "1950s - 1970s time-sharing era" with bullet points on the left and black and white photos of people using mainframe computers on the right)
More analogies that I think strike me is that we're kind of like in this 1960s-ish era, where LLM compute is still very expensive for this new kind of a computer. And that forces the LLMs to be centralized in the cloud, and we're all just, uh, sort of thin clients that interact with it over the network.
[11:21] (Karpathy makes hand gestures)
And none of us have full utilization of these computers, and therefore, it makes sense to use time-sharing where we're all just, you know, a dimension of the batch when they're running the computer in the cloud. And this is very much what computers used to look like at during this time. The operating systems were in the cloud, everything was streamed around, and there was batching.
[11:40] (Karpathy makes hand gestures)
And so, the personal computing revolution hasn't happened yet, because it's just not economical, it doesn't make sense. But, I think some people are trying. And it turns out that Mac Minis, for example, are a very good fit for some of the LLMs, because it's all
[11:51] (The screen changes to "Early hints of Personal Computing v2" with two tweets about stacking Mac Minis to run LLMs, one with a llama image)
if you're doing batch run inference, this is all super memory-bound, so this actually works. And, uh, I think these are some early indications maybe of personal computing, but this hasn't really happened yet, it's not clear what this looks like. Maybe some of you get to invent what what this is, or how it works, or, uh, what it should, what it should be.
[12:10] (The screen changes to a meme format: " (text) chat ~= terminal direct/native access to the OS. GUI hasn't been invented yet. (~1970) ". On the right, images of an old terminal and a ChatGPT interface. Below, Pam from The Office says, "Corporate needs you to find the differences between this picture and this picture. They're the same picture.")
Maybe one more analogy that I'll mention is whenever I talk to ChatGPT or some LLM directly in text, I feel like I'm talking to an operating system through the terminal. Like it just it's it's text, it's direct access to the operating system, and I think a GUI hasn't yet really been invented in like a general way. Like
[12:30] (Karpathy makes hand gestures)
should ChatGPT have a GUI, different than just the tech bubbles? Uh, certainly, some of the apps that we're going to go into in a bit have a GUI, but there's no like GUI across all the tasks that make sense.
[12:43] (Karpathy makes hand gestures)
Um, there are some ways in which LLMs are different from kind of operating systems in some fairly unique way, and from early computing. And I wrote about, uh, this
[12:53] (The screen changes to "Power to the people: How LLMs flip the script on technology diffusion" with a three-headed dragon meme. Text below lists examples like electricity, cryptography, computing, flight, internet, GPS)
one particular property that strikes me as very different, uh, this time around. It's that, uh, LLMs like flip, they flip the direction of technology diffusion, uh, that is usually, uh, present in technology. So, for example, with electricity, cryptography, computing, flight, internet, GPS, lots of new transformative technologies that have not been around. Typically, it is the government and corporations that are the first users, because it's new and expensive, et cetera, and it only later diffuses to consumer.
[13:21] (Karpathy makes hand gestures)
Uh, but I feel like LLMs are kind of like flipped around. So, maybe with early computers,
[13:25] (The slide changes to add an image of military ballistics calculations on the left and an image of a hand boiling an egg with a text bubble "Hi ChatGPT, how to boil egg?" on the right, under the "Consumer" dragon head)
it was all about ballistics and military use. But, with LLMs, it's all about how do you boil an egg or something like that. This is certainly like a lot of my use. And so, it's really fascinating to me that we have a new magical computer, and it's like helping me boil an egg. It's not helping the government do something really crazy like some military ballistics or some special technology.
[13:43] (Karpathy makes hand gestures)
Indeed, corporations and governments are lagging behind the adoption of all of us of all of these technologies. So, it's just backwards, and I think it informs maybe some of the uses of how we want to use this technology, or like what are some of the first apps, and so on.
[13:56] (The screen changes to "Part 1 Summary" with bullet points: "LLM labs: - Fab LLMs - LLMs ~= Operating Systems (circa 1960s) - Available via time-sharing, distributed like utility NEW: Billions of people have sudden access to them! It is our time to program them.")
So, in summary so far, LLM labs, fab LLMs. I think accurate language to use. But LLMs are complicated operating systems. They're circa 1960s in computing and we're redoing computing all over again. And they're currently available via time-sharing and distributed like a utility. What is new and unprecedented is that they're not in the hands of a few governments and corporations. They're in the hands of all of us, because we all have a computer, and it's all just software, and ChatGPT was beamed down to our computers like to billions of people like instantly and overnight, and this is insane.
[14:29] (Karpathy gestures excitedly with his hands)
Uh, and it's kind of insane to me that this is the case, and now it is our time to enter the industry and program these computers. This is crazy. So, I think this is quite remarkable.
[14:39] (The screen changes to "Part 2 LLM Psychology" with a white background)
Before we program LLMs, we have to kind of like spend some time to think about what these things are. And I especially like to kind of talk about their psychology.
[14:49] (Karpathy gestures)
So, the way I like to think about LLMs is that they're kind of like people spirits. Um,
[14:53] (The screen changes to "LLMs are "people spirits": stochastic simulations of people. Simulator = autoregressive Transformer" with an abstract, glowing image of a human-like figure surrounded by data streams. A Transformer architecture diagram is on the right. Text below reads "=> They have a kind of emergent "psychology".")
They are stochastic simulations of people. Um, and the simulator, in this case, happens to be an auto-regressive Transformer. So, Transformer is a neural net. Uh, it's and it just kind of like goes on the level of tokens, it goes chunk, chunk, chunk, chunk, chunk. And there's an almost equal amount of compute for every single chunk. Um, and, um,
[15:21] (The screen changes to "Encyclopedic knowledge/memory, ..." with an image of a young person studying surrounded by books and a movie poster for "Rain Man")
This simulator, of course, is, is just is basically there's some weights involved, and we fit it to all of text that we have on the internet and so on. And you end up with this kind of a simulator. And because it is trained on humans, it's got this emergent psychology that is human-like. So, the first thing you'll notice is, of course, LLMs have encyclopedic knowledge and memory, uh, and they can remember lots of things, a lot more than any single individual human can, because they've read so many things. It's actually kind of reminds me of this movie Rain Man, which I actually really recommend people watch, it's an amazing movie, I love this movie. Um, and Dustin Hoffman here is an autistic savant, who has almost perfect memory. So he can read it a, he can read like a phone book and remember all of the names and, uh, phone numbers. And I kind of feel like LLMs are kind of like very similar. They can remember SHA hashes and lots of different kinds of things very, very easily.
[16:01] (Karpathy gestures with his hands)
So, they certainly have superpowers in some set in some respects. But they also have a bunch of, I would say, cognitive deficits. So, they hallucinate quite a bit, um, and they kind of make up stuff and don't have a very good, uh, sort of internal model of self-knowledge, not sufficient, at least. And this has gotten better, but not perfect.
[16:20] (The screen changes to "Jagged intelligence" with an image of a frustrated student in a classroom. On the board behind, it says "2 + 2 = 5". Text below gives "Famous examples: 9.11 > 9.9, two 'r' in 'strawberry', ...")
They display jagged intelligence. So they're going to be superhuman in some problem-solving domains, and then they're going to make mistakes that basically no human will make. Like,
[16:30] (Karpathy gestures)
you know, they will insist that 9.11 is greater than 9.9, or there are two Rs in strawberry. These are some famous examples. But basically, there are rough edges that you can trip on. So, that's kind of, I think, also kind of unique.
[16:41] (The screen changes to "Anterograde amnesia" with an image of a student looking confused, holding a paper that says "What did you eat for breakfast??". Text below explains context windows as working memory and lack of continual learning/sleep equivalent)
Um, they also kind of suffer from anterograde amnesia. Um, so, uh, and I think I'm alluding to the fact that if you have a coworker who joins your organization, this coworker will over time learn your organization and, uh, they will understand and gain like a huge amount of context on the organization, and they go home and they sleep, and they consolidate knowledge, and they develop expertise over time. LLMs don't natively do this, and this is not something that has really been solved in the R&D of LLMs, I think.
[17:08] (Karpathy makes hand gestures)
And so context windows are really kind of like working memory, and you have to sort of program the working memory quite directly because they don't just kind of like get smarter by by default. And I think a lot of people get tripped up by the analogies, uh, in this way.
[17:21] (The screen changes to "In popular culture..." with movie posters for "Memento" and "50 First Dates")
In popular culture, I recommend people watch these two movies, uh, Memento and 50 First Dates. In both of these movies, the protagonists, their weights are fixed, and their context windows gets wiped every single morning, and it's really problematic to go to work or have relationships when this happens, and this happens to LLMs all the time.
[17:39] (Karpathy makes hand gestures)
I guess one more thing I would point to is security kind of related limitations of of the use of LLMs. So, for example, LLMs are quite gullible. Uh, they are susceptible to prompt injection risks. They might leak your data, et cetera. And so, um, and there's many other considerations, uh, security related. So,
[17:55] (Karpathy makes hand gestures)
so basically, long story short, you have to load your, you have to load your, you have to simultaneously think through this superhuman thing that has a bunch of cognitive deficits and issues. How do we and yet, they are extremely like useful?
[18:09] (Karpathy makes hand gestures)
And so, how do we program them, and how do we work around their deficits, and enjoy their superhuman powers? So, what I want to switch to now is talk about the opportunities of how do we use these models and what are some of the biggest opportunities. This is not a comprehensive list, just some of the things that I thought were interesting for this talk.
[18:28] (Karpathy makes hand gestures)
The first thing I'm kind of excited about is what I would call partial autonomy apps.
[18:30] (The screen changes to "Partial autonomy apps" with a spinning gear icon and text: ""Copilot" / "Cursor for X"")
So, for example, let's work with the example of coding.
[18:34] (The screen changes to "Example: you could go to an LLM to chat about code..." with a ChatGPT chat window and an image of an old computer terminal)
You can certainly go to ChatGPT directly, and you can start copy-pasting code around, and copy-pasting, uh, bug reports and stuff around, and getting code and copy-pasting everything around. Why would you, why would you do that? Why would you go directly to the operating system?
[18:48] (The screen changes to "Example: Anatomy of Cursor" with a split view of a code editor, one side for code and the other for LLM interaction)
It makes a lot more sense to have an app dedicated for this. And so I think many of you, uh, use, uh, Cursor, I do as well. Uh, and, uh, Cursor is kind of like the thing you want instead. You don't want to just directly go to the ChatGPT.
[19:08] (The screen highlights the left side as "Traditional interface" and the right side as "LLM integration". Text points 1 and 2 appear: "1. Package state into a context window before calling LLM." and "2. Orchestrate and call multiple models (e.g. embedding models, chat models, diff apply models, ...)")
And I think Cursor is a very good example of an early LLM app that has a bunch of properties that I think are, um, useful across all the LLM apps. So, in particular, you will notice that we have a traditional interface that allows a human to go in and do all the work manually, just as before. But in addition to that, we now have this LLM integration that allows us to go in bigger chunks. And so, some of the properties of LLM apps that I think are shared and useful to point out. Number one, the LLMs basically do a ton of the context management, um, number two, they orchestrate multiple calls to LLMs, right? So, in the case of Cursor, there's under the hood embedding models for all your files, the actual chat models, models that apply diffs to the code, and this is all orchestrated for you.
[19:44] (Point 3 appears: "3. Application-specific GUI")
A really big one that, uh, I think also maybe not fully appreciated always, is application-specific GUI and the importance of it. Um, because you don't just want to talk to the operating system directly in text. Text is very hard to read, interpret, understand.
[20:01] (Karpathy gestures with his hands)
And also like you don't want to take some of these actions natively in text. So, it's much better to just see a diff as like red and green change, and you can see what's being added or subtracted. It's much easier to just do command Y to accept or command N to reject. I shouldn't have to type it in text, right? So, a GUI allows a human to audit the work of these fallible systems and to go faster. I'm going to come back to this point a little bit, uh, later as well.
[20:22] (The screen changes to highlight an "autonomy slider" at the bottom of the Cursor interface. Point 4 appears: "4. Autonomy slider: Tab -> Cmd+K -> Cmd+L -> Cmd+I (agent mode)")
And the last kind of feature I want to point out is that there's what I call the autonomy slider. So, for example, in Cursor, you can just do tab completion, you're mostly in charge. You can select a chunk of code and command K to change just that chunk of code. You can do command L to change the entire file. Or you can do command I, which just, you know, let her rip do whatever you want in the entire repo. And that's the sort of full autonomy agent agentic version.
[20:47] (Karpathy gestures with his hands)
And so, you are in charge of the autonomy slider, and depending on the complexity of the task at hand, you can, uh, tune the amount of autonomy that you're willing to give up for that task.
[20:58] (The screen changes to "Example: Anatomy of Perplexity" with a Perplexity AI search results page. The autonomy slider is shown with points for search, research, deep research)
Maybe to show one more example of a fairly successful LLM app, uh, Perplexity. Um, they it also has very similar features to what I've just pointed out in Cursor. Uh, it packages up a lot of the information, it orchestrates multiple LLMs. It's got a GUI that allows you to audit some of its work. So, for example, it will cite sources and you can imagine inspecting them. And it's got an autonomy slider. You can either just do a quick search, or you can do research, or you can do deep research and come back 10 minutes later. So, this is all just varying levels of autonomy that you give up to the tool.
[21:28] (The screen changes to "What does all software look like in the partial autonomy world?" with screenshots of Adobe Photoshop and Unreal Engine, and questions below)
So, I guess my question is, I feel like a lot of software will become partially autonomous. And I'm trying to think through like, what does that look like? And for many of you who maintain products and services, how are you going to make your products and services partially autonomous? Can an LLM see all the things that a human can? Can an LLM act in all the ways that a human can act? And can humans supervise and stay in the loop of this activity?
[21:51] (Karpathy gestures with his hands)
Because again, these are fallible systems that aren't yet perfect. And what does a diff look like in Photoshop or something like that, you know? And also a lot of the traditional software right now, it has all these switches and all this kind of stuff that's all designed for human. All this has to change and become accessible to LLMs.
[22:08] (The screen changes to "Consider the full workflow of partial autonomy UIUX" with a circular diagram showing "AI" generating and "HUMAN" verifying, connected by arrows. Text below "Verification" reads "1. Make this EASY FAST to win.")
So, one thing I want to stress with a lot of these LLM apps that I'm not sure gets, uh, as much attention as it should is, um, we're now kind of like cooperating with AIs. And usually, they are doing the generation, and we as humans are doing the verification. It is in our interest to make this loop go as fast as possible, so we're getting a lot of work done. There are two major ways that I, uh, think, uh, this can be done. Number one, you can speed up verification a lot.
[22:31] (Karpathy gestures with his hands)
Um, and I think GUIs, for example, are extremely important to this, because a GUI utilizes your computer vision GPU in all of our head. Reading text is effortful, and it's not fun. But looking at stuff is fun, and it's just a kind of like a highway to your brain. So I think GUIs are very useful for auditing systems and visual representations in general.
[22:53] (Point 2 appears: "2. Keep AI 'on a tight leash' to increase the probability of successful verification.")
And number two, I would say is, we have to keep the AI on the leash. We keep I think a lot of people are getting way over-excited with AI agents, and, uh, it's not useful to me to get a diff of 1,000 lines of code to my repo. Like I have to, I'm still the bottleneck, right? Even though the 1,000 lines come out instantly, I have to make sure that this thing is not introducing bugs. Is just like,
[23:17] (Karpathy makes hand gestures)
and that is doing the correct thing, right? And that there's no security issues and so on. So, I, I think that, um, yeah, basically, you, we have to sort of like, it's in our interest to make the the flow of these two go very, very fast, and we have to somehow keep the AI on a leash, because it gets way too overactive.
[23:33] (The screen changes to "Human+AI UIUX for Coding" with a cartoon image of a human connected by a leash to a robot that is typing on multiple screens)
It's, uh, kind of like this. This is how I feel when I do AI-assisted coding. If I'm just vibe coding, everything is nice and great. But if I'm actually trying to get work done, it's not so great to have an overreactive, uh, agent doing all this kind of stuff.
[23:47] (The screen changes to "Example: keeping agents on the leash" with bullet points detailing an AI-assisted coding workflow)
So, this slide is not very good. I'm sorry, but I guess I'm trying to develop like many of you, some ways of utilizing these agents in my coding workflow, and to do AI-assisted coding. And in my own work, I'm always scared to get way too big diffs. I always go in small incremental chunks. I want to make sure that everything is good. I want to spin this loop very, very fast. And, uh, I sort of work on small chunks of single concrete thing, uh, and so I think, uh, many of you probably are developing similar ways of working with the, with LLMs.
[24:18] (The screen changes to a block of text, titled "Example: keeping agents on the leash" with a footer "AI-assisted coding for lowics that can't get lucky with ideas")
Um, I also saw a number of blog posts that try to develop these best practices for working with LLMs. And here's one that I read recently and I thought was quite good. And it kind of discussed some techniques, and some of them have to do with how you keep the AI on a leash. So, as an example, if you are prompting, if your prompt is vague, then, uh, the AI might not do exactly what you wanted, and in that case, verification will fail. You're going to ask for something else. If a verification fails, then you're going to start spinning. So, it makes a lot more sense to spend a bit more time to be more concrete in your prompts, which increases the probability of successful verification, and you can move forward. And so, I think a lot of us are going to end up finding, um, kind of techniques like this.
[24:56] (The screen changes to "Example: keeping agents on the leash - AI = Education / LLM101s" with two images: a textbook on the left and two students studying on the right)
I think in my own work as well, I'm currently interested in, uh, what education looks like in, um, together with, uh, kind of like now that we have AI, uh, and LLMs, what does education look like? And I think a a large amount of thought for me goes into how we keep AI on the leash. I don't think it just works to go to ChatGPT and be like, hey, teach me physics. I don't think this works, because the AI is like gets lost in the woods. And so for me, this is actually two separate apps, for example. There's an app for a teacher that creates courses, and then there's an app that takes courses and serves them to students. And in both cases, we now have this intermediate artifact of a course that is auditable, and we can make sure it's good, we can make sure it's consistent, and the AI is kept on the leash with respect to a certain syllabus, a certain like, um, progression of projects, and so on. And so, this is one way of keeping the AI on a leash, and I think has a lot much higher likelihood of working. And the AI is not getting lost in the woods.
[25:49] (The screen changes to "Example: Tesla Autopilot" with an image of a person sitting in the driver's seat of a Tesla, with a screen showing the car's surroundings and an "autonomy slider". Bullet points on the right describe levels of autonomy)
One more kind of analogy I wanted to sort of allude to is, I'm not, I'm no stranger to partial autonomy, and I've kind of worked on this, I think, for five years at Tesla. And this is also a partial autonomy product, and shares a lot of the features. Like, for example, right there in the instrument panel is the GUI of the Autopilot. So, it's showing me what the what the neural network sees, and so on. And we have the autonomy slider, where over the course of my tenure there, we did more and more autonomous tasks for the user.
[26:19] (The screen changes to "2015 - 2025 was the decade of 'driving agents'" with an image of a white SUV parked on a residential street. A gray bar below the title has a slider indicating progress)
And maybe the story that I wanted to tell very briefly is, uh, actually, the first time I drove a self-driving vehicle was in 2013. And I had a friend who worked at Waymo, and, uh, he offered to give me a drive around Palo Alto. I took this picture using, uh, Google Glass at the time. And many of you are so young that you might not even know what that is. Uh, but, uh, yeah, this was like all the rage at the time. And we got into this car, and we went for about a 30-minute drive around Palo Alto. Highways, uh, streets, and so on. And this drive was perfect. There were zero interventions. And this was in 2013, which is now 12 years ago.
[26:52] (Karpathy gestures)
And it kind of struck me because at the time when I had this perfect drive, this perfect demo, I felt like, wow, self-driving is imminent, because this just worked, this is incredible. Um, but here we are, 12 years later, and we are still working on autonomy. Um, we are still working on driving agents. And even now, we haven't actually like fully solved the problem. Like, you may see Waymos going around, and they look driverless. But, you know, there's still a lot of teleoperation and a lot of human in the loop of a lot of this driving. So, we still haven't even like declared success, but I think it's definitely like going to succeed at this point. But it just took a long time.
[27:27] (Karpathy clenches and unclenches his fists, holding a small clicker)
And so, I think like, like, this is software is really tricky. I think in the same way that driving is tricky. And so, when I see things like, oh, 2025 is the year of agents, I get very concerned. And I kind of feel like, you know, this is the decade of agents, and this is going to be quite some time. We need humans in the loop, we need to do this carefully. This is software. Let's be serious here.
[27:51] (Karpathy shrugs and gestures with his hands)
One more kind of analogy that I always think through is the Iron Man suit. Uh, I think this is I always love Iron Man. I think it's like so, um, correct in a bunch of ways with respect to technology and how it will play out.
[28:05] (Karpathy gestures with his hands)
And what I love about the Iron Man suit is that it's both an augmentation, and Tony Stark can drive it, and it's also an agent. And in some of the movies, the Iron Man suit is quite autonomous and can fly around, and find Tony, and all this kind of stuff. And so, this is the autonomy slider is we can be, we can build augmentations, or we can build agents. And we kind of want to do a bit of both. But,
[28:23] (The screen changes to "Building Autonomous Software" with a left column showing crossed-out items ("Iron Man robots", "Flashy demos of autonomous agents", "AGI 2027") and a right column with checked items ("Iron Man suits", "Partial autonomy products", "Custom GUI and UIUX", "Fast Generation - Verification loop", "Autonomy slider"))
at this stage, I would say, working with fallible LLMs, and so on, I would say, you know, it's less Iron Man robots, and more Iron Man suits that you want to build. It's less like building flashy demos of autonomous agents, and more building partial autonomy products. And these products have custom GUIs and UIUX, and we're trying to, um, and this is done so that the generation verification loop with the human is very, very fast. But, we are not losing the sight of the fact that it is in principle possible to automate this work. And there should be an autonomy slider in your product, and you should be thinking about how you can slide that autonomy slider and make your product, uh, sort of, uh, more autonomous over time. But, this is kind of how I think there's lots of opportunities in these kinds of products.
[29:08] (The screen changes to "Make software highly accessible" with a thinking emoji. Karpathy makes hand gestures)
I want to now switch gears a little bit, and talk about one other dimension that I think is very unique. Not only is there a new type of programming language that allows for autonomy in software, but also, as I mentioned, it's programmed in English, which is this natural interface. And,
[29:22] (Karpathy gestures with his hands)
suddenly, everyone is a programmer, because everyone speaks natural language like English. So, this is extremely bullish and very interesting to me. And also completely unprecedented, I would say. It used to be the case that you need to spend five to ten years studying something to be able to do something in software. This is not the case anymore.
[29:36] (Karpathy gestures, then looks down and shrugs)
So, I don't know if by any chance, anyone has heard of vibe coding?
[29:40] (The screen displays a tweet from Andrej Karpathy explaining "vibe coding" as fully giving in to the vibes and embracing exponentials, possible because LLMs are getting too good. It details his casual, non-rigorous approach to coding with LLMs)
Uh, this this is the tweet that's kind of like introduced this, but I'm told that this is now like a major meme. Um, fun story about this is that
[29:50] (Karpathy makes hand gestures)
I've been on Twitter for like 15 years or something like that at this point, and I still have no clue which tweet will become viral, and which tweet like fizzles and no one cares. And I thought that this tweet was going to be the latter. I don't know, it was just like a shower of thoughts, but this became like a total meme, and I really just can't tell, but I guess like it struck a chord, and gave a name to something that everyone was feeling, but couldn't quite say in words.
[30:13] (The screen displays a Wikipedia page for "Vibe coding")
So, now there's a Wikipedia page and everything.
[30:17] (Karpathy grins, the audience laughs and applauds)
So it's like, (Karpathy laughs) Yeah, this is like a major contribution now or something like that. So,
[30:31] (The screen changes to a tweet by Thomas Wolf with a video of children coding at desks, happily interacting with computers)
Um, Thomas Wolf from HuggingFace shared this beautiful video that I really love. Um, (Children exclaim "Yeah!" and clap) These are kids vibe coding. (A boy sings "Don don don") And I find that this is such a wholesome video. Like, I love this video. Like, how can you look at this video and feel bad about the future? The future is great.
[30:52] (Karpathy makes hand gestures)
I think this will end up being like a gateway drug to software development. Um, I'm not a doomer about the future of the generation. And I think, yeah, I love this video. So, I tried vibe coding a little bit as well, because it's so fun. Uh, so, vibe coding is so great when you want to build something super duper custom that doesn't appear to exist, and you just want to wing it, because it's a Saturday or something like that.
[31:15] (The screen changes to a phone screen showing a "Vibe Coding iOS app" that tracks calorie intake. A finger taps buttons to change the calorie count)
So, I built this, uh, iOS app, and I don't, I can't actually program in Swift. But I was really shocked that I was able to build like a super basic app, and I'm not going to explain it, it's really, uh, dumb. But, uh, I kind of like this was just like a day of work, and this was running on my phone like later that day, and I was like, wow, this is amazing. I didn't have to like read through Swift for like five days or something like that to like get started.
[31:38] (The screen changes to "Vibe coding MenuGen https://www.menugen.app/" with an image of a restaurant menu on the left and a generated menu with pictures on the right)
I also vibe coded this app called MenuGen. And this is live, you can try it at menugen.app. And I basically had this problem where I show up at a restaurant, I read through the menu, and I have no idea what any of the things are. And I need pictures. So, this doesn't exist. So I was like, hey, I'm going to vibe code it. So, uh, this is what it looks like.
[31:54] (The screen changes to a phone screen recording of the MenuGen app in action, showing a menu being photographed and then dishes appearing with AI-generated images)
You go to menugen.app. Um, and, uh, you take a picture of a of a menu, and then menugen generates the images. And everyone gets $5 in credits for free when you sign up. And therefore, this is a major cost center in my life. So, this is a negative negative, uh, revenue app for me right now. (Karpathy laughs) I've lost a huge amount of money on menugen.
[32:20] (The screen changes to "The code was the easiest part! :O" with bullet points: "- LLM API keys 😬 - Flux (image generation) API keys 😬 - Running locally (ez) ✅ - Vercel deployments 😬 - Domain names 😬 - Authentication 😬 - Payments 😬" and a link to Karpathy's blog post)
Okay. But the fascinating thing about menugen for me is that the code of the vibe of the vibe coding part, the code, was actually the easy part of of vibe coding menugen. And most of it actually was when I tried to make it real, so that you can actually have authentication and payments, and the domain name, and a Vercel deployment. This was really hard, and all of this was not code. All of this DevOps stuff was in me in the browser clicking stuff. And this was extreme slog, and took another week. So, it was really fascinating that I had the menugen, um, basically, demo working on my laptop in a few hours, and then it took me a week because I was trying to make it real. And the reason for this is, this was just really annoying. Um, so, for example, if you try to add Google login to your web page,
[33:09] (The screen shows a dense instruction manual titled "Example: adding Google login" with numerous steps)
I know this is very small, but just a huge amount of instructions of this, uh, Clerk library telling me how to integrate this. And this is crazy, like it's telling me, go to this URL. Click on this drop-down. Choose this. Go to this, and click on that. And it's like telling me what to do. Like a computer is telling me, the actions I should be taking. Like, you do it. Why am I doing this?
[33:29] (Karpathy laughs and shrugs)
What the hell?
[33:31] (Karpathy makes a frustrated face)
I had to follow all these instructions. This was crazy.
[33:38] (The screen changes to a white background with "Build for agents 🤖" in black text)
So, I think the last part of my talk, therefore, focuses on, can we just build for agents? I don't want to do this work. Can agents do it? Thank you. (Audience applauds)
[33:48] (The screen changes to "There is new category of consumer/manipulator of digital information:" with bullet points: "1. Humans (GUIs) 2. Computers (APIs) 3. NEW: Agents <- computers... but human-like")
Okay. So, roughly speaking, I think there's a new category of consumer and manipulator of digital information. It used to be just humans through GUIs, or computers through APIs. And now we have a completely new thing. And agents, they're computers, but they are human-like. Kind of, right? They're people spirits. There's people spirits on the internet, and they need to interact with our software infrastructure.
[34:10] (The screen changes to "robots.txt ->" with a white box containing an image of an "llms.txt" file on the left, and a white box with markdown code for "FastHTML" on the right)
Like, can we build for them? It's a new thing. So, as an example, you can have robots.txt on your domain, and you can instruct, uh, or like advise, I suppose, um, uh, web crawlers on how to behave on your website. In the same way, you can have maybe llms.txt file, which is just a simple markdown that's telling LLMs what this domain is about. And this is very readable to an LLM. If it had to instead get the HTML of your webpage and try to parse it, this is very error-prone and difficult and it will screw it up, and it's not going to work. So we can just directly speak to the LLM. It's worth it.
[34:39] (The screen changes to "Docs for people LLMs" with screenshots of Vercel and Stripe documentation pages. The Vercel doc shows a URL with "/llms.txt")
Um, a huge amount of documentation is currently written for people. So you will see things like lists, and bold, and pictures. And this is not directly accessible by an LLM. So, I see some of the services now are transitioning a lot of their docs to be specifically for LLMs. So, Vercel and Stripe, as an example, are early movers here, uh, but there are, uh, a few more that I've seen already. And they offer their documentation in markdown. Markdown is super easy for LLMs to understand. This is great.
[35:09] (The screen changes to "Manim Mathematical Animation Engine" with an image of 3blue1brown and code/animation examples)
Um, maybe one simple example from from, uh, my experience as well. Maybe some of you know 3blue1brown, he makes beautiful animation videos on, uh, YouTube. (Audience applauds)
[35:24] (Karpathy smiles)
Yeah, I love this library, so that he wrote, uh, Manim. And I wanted to make my own. And, uh, there's extensive documentations on how to use Manim, and, uh, so I didn't want to actually read through it. So, I copy-pasted the whole thing to an LLM, and I described what I wanted, and it just worked out of the box. Like LLM just vibe coded me an animation exactly what I wanted, and I was like, wow, this is amazing. So, if we can make docs legible to LLMs, it's going to unlock a huge amount of, um, kind of use, and, um, I think this is wonderful, and should, should happen more.
[35:55] (Karpathy gestures)
The other thing I wanted to point out is that you do unfortunately have to, it's not just about taking your docs and making them appear in markdown. That's the easy part. We actually have to change the docs. Because anytime your docs say click, this is bad. An LLM will not be able to natively take this action, uh, right now.
[36:10] (The screen changes to show a tweet by Lee Robinson about adding cURL commands instead of "click" for Vercel documentation, and a "Stripe Model Context Protocol (MCP) Server" code snippet)
So, Vercel, for example, is replacing every occurrence of click with the equivalent cURL command that your LLM agent could take on your behalf. Um, and so I think this is very interesting. And then, of course, there's, uh, Model Context Protocol from Anthropic, and this is also another way. It's a protocol of speaking directly to agents as this new consumer and manipulator of digital information. So, I'm very bullish on these ideas.
[36:31] (The screen changes to "Context builders, e.g.: Gitingest" with a GitHub repository page for "nanogpt" on the left, and a "Gitingest" interface showing extracted repository structure and files on the right)
The other thing I really liked is a number of little tools here and there that are helping ingest data that in like very LLM-friendly formats. So, for example, when I go to a GitHub repo, like my nanogpt repo, I can't feed this to an LLM and ask questions about it. Uh, because it's, you know, this is a human interface on GitHub. So, when you just change the URL from github to gitingest, then, uh, this will actually concatenate all the files into a single giant text. And it will create a directory structure, et cetera. And this is ready to be copy-pasted into your favorite LLM, and you can do stuff.
[37:01] (Karpathy gestures)
Maybe even more dramatic example of this is Devin DeepWiki, where it's not just the raw content of these files,
[37:05] (The screen changes to "Context builders, e.g.: Devin DeepWiki" with the GitHub repo on the left and a generated DeepWiki page with a system architecture flowchart on the right)
Uh, this is from Devin. But also, like they have Devin basically do analysis of the GitHub repo. And Devin basically builds up a whole docs, uh, pages just for your repo. And you can imagine that this is even more helpful to copy-paste into your LLM. So, I love all the little tools that basically, where you just change the URL, and it makes something accessible to an LLM. So, this is all well and great, and, uh, I think there should be a lot more of it.
[37:31] (The screen changes to "Introducing Operator" with a webpage screenshot. Text says it's an agent that can browse to perform tasks, with a keyboard and mouse shown below)
One more note I wanted to make is that it is absolutely possible that in the future, uh, LLMs will be able to, this is not even future, this is today. They'll be able to go around and they'll be able to click stuff, and so on. But I still think it's very worth, uh, basically, meeting LLM halfway, LLMs halfway, and making it easier for them to access all this information, uh, because this is still fairly expensive, I would say, to use, and, uh, a lot more difficult. And so, I do think that lots of software, there will be a long tail where it won't like adapt, because these are not like live player sort of repositories or digital infrastructure, and we will need these tools.
[38:09] (Karpathy gestures)
Uh, but I think for everyone else, I think it's very worth kind of like meeting in some middle point. So, I'm bullish on both, if that makes sense.
[38:16] (The screen changes to a summary slide with images of the Software 1.0, 2.0, 3.0 map, the LLM OS diagram, people studying, and a Human+AI workflow. Text outlines "Partial autonomy LLM apps:" features and other points. "Build for agents 🤖" is at the bottom right)
So, in summary, what an amazing time to get into the industry. We need to rewrite a ton of code. A ton of code will be written by professionals and vibe coders. These LLMs are kind of like utilities, kind of like fabs, but they're kind of especially like operating systems. But it's so early, it's like 1960s of operating systems. And, uh, and I think a lot of the analogies crossover. Um, and these LLMs are kind of like these fallible, uh, you know, people spirits that we have to learn to work with. And in order to do that properly, we need to adjust our infrastructure towards it. So, when you're building these LLM apps, I described some of the ways of working effectively with these LLMs, and some of the tools that make that kind of possible. And how you can spin this loop very, very quickly. And basically, create partial autonomy products. And then, um, yeah, a lot of code has to also be written for the agents, more directly.
[39:09] (Karpathy smiles and bows as the audience applauds. He exits the stage. The screen displays "Thank you!" and then returns to the "AI Startup School" title card with music)
But, in any case, going back to the Iron Man suit analogy. I think what we'll see over the next decade, roughly, is we're going to take the slider from left to right. And I'm very interesting. It's going to be very interesting to see what that looks like, and I can't wait to build it with all of you. Thank you.

*Andrej Karpathy discusses the evolution of software from traditional code (Software 1.0) to neural network weights (Software 2.0) and now to natural language prompts for Large Language Models (Software 3.0), highlighting the unprecedented accessibility of programming through English. He uses analogies to electricity utilities, semiconductor fabrication, and operating systems to explain the characteristics of LLMs, and explores opportunities in building partially autonomous applications that require a tight human-in-the-loop verification process, urging developers to "build for agents."*

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="TRjq7t2Ms5I.md">
<details>
<summary>Building Production-Ready RAG Applications: Jerry Liu</summary>

Phase: [EXPLOITATION]

# Building Production-Ready RAG Applications: Jerry Liu

[00:00] (Video opens with "AI Engineer SUMMIT" logo)
[00:05] (Presenting Sponsor: AutoGPT logo appears)
[00:09] (Diamond Sponsors: Fixie and Supabase logos appear)

[00:14] Hey everyone. Uh, my name is Jerry, co-founder and CEO of LlamaIndex, and today we'll be talking about how to build production-ready RAG applications. Um, I think there's still time for a raffle for the bucket hat, so if you guys stop by our booth, uh, please fill out the Google Form. Okay.
[00:27] (The speaker, Jerry Liu, is on stage. The stage has a large screen behind him displaying the presentation slides. The current slide shows the LlamaIndex logo and the title "Building Production-Ready RAG Applications")

[00:28] Let's get started. So, everybody knows that there has been a ton of amazing use cases in GenAI recently, you know, um, knowledge search and QA, conversational agents, uh, workflow automation, document processing. These are all things that you can build, uh, especially using the recent capabilities of LLMs over your data.
[00:46] (A slide titled "GenAI - Enterprise Use-cases" is displayed, showing a diagram with documents, knowledge base, LLM, inbox, and email, illustrating knowledge search, conversational agents, and workflow automation.)

[00:46] So, if we just do a quick refresher in terms of like paradigms for how do you actually get language models to understand data that hasn't been trained over. There's really like two main paradigms. One is retrieval augmentation, where you, like, fix the model, and you basically create a data pipeline to put context into the prompt from some data source into the input prompt of the language model.
[01:15] (The slide changes to "Paradigms for inserting knowledge: Retrieval Augmentation - Fix the model, put context into the prompt". A diagram shows a Notion icon feeding into an "Input Prompt" which then goes to an "LLM".)
[01:16] Um, so like a vector database, uh, you know, like unstructured text, SQL database, etc.
[01:76] The next paradigm here is fine-tuning. How can we bake knowledge into the weights of the network by actually updating the weights of the model itself, some adapter on top of the model, but basically some sort of training process over some new data to actually incorporate knowledge.
[01:38] (The slide changes to "Paradigms for inserting knowledge: Fine-tuning - baking knowledge into the weights of the network". A diagram shows a Notion icon feeding into an "LLM" with a bidirectional arrow and text "RLHF, Adam, SGD, etc.")
[01:39] We'll probably talk a little bit more about retrieval augmentation, but this is just like to help you get, uh, started and really understand the mission statement of, of the company.

[01:40] Okay. Let's talk about RAG, Retrieval Augmented Generation. Um, it's become kind of a buzzword recently, but we'll first walk through the current RAG stack for building a QA system.
[01:44] (The slide changes to "RAG Stack")
[01:45] This really consists of two main components, uh, data ingestion as well as data querying, which contains retrieval and synthesis. Uh, if you're just getting started in LlamaIndex, you can basically do this in around like five-ish lines of code, uh, so you don't really need to think about it.
[02:08] (The slide changes to "Current RAG Stack for building a QA System", showing a flowchart from "Doc" being chunked, then going to a "Vector Database", then chunks for "Retrieval + Synthesis", then to an "LLM".)
[02:10] But if you do want to learn some of the lower-level components, and I do encourage like every engineer, uh, AI engineer, to basically just like learn how these components work under the hood, um, I would encourage you to check out some of our docs to really understand how do you actually do data ingestion, uh, and data querying. Like how do you actually retrieve from a vector database and how do you synthesize that with an LLM.

[02:23] (The slide changes to "Challenges with "Naive" RAG")
[02:24] So, that's basically the key stack that's kind of emerging these days like for every sort of chatbot, like, you know, chat over your PDF, like over your unstructured data, um, a lot of these things are basically using these same principles of like how do you actually load data from some data source and actually, you know, um, uh, retrieve and query over it. But I think as developers are actually developing these applications, they're realizing that this isn't quite enough.
[02:58] (The speaker gestures as he talks about challenges with current approaches.)
[02:59] Uh, like there's there's certain issues that you're running into that are blockers for actually being able to productionize these applications. And so what are these challenges with naive RAG?
[03:00] (The slide changes to "Challenges with Naive RAG (Response Quality)". It lists "Bad Retrieval" with sub-points: "Low Precision", "Low Recall", "Outdated information".)
[03:01] One aspect here is just like, uh, the response, and and this is the key thing that we're focusing on, like the the response quality is not very good. You run into for instance like bad retrieval issues. Like, uh, during the retrieval stage from your vector database, if you're not actually returning the relevant chunks from your vector database, you're not going to be able to have the correct context actually put into the LLM. So this includes certain issues like low precision, not all chunks in the retrieved set are relevant. Uh, this leads to like hallucination, like lost in the middle problems, you have a lot of fluff in the return response. This can mean low recall, like your top K isn't high enough, or basically like the the the set of like information that you need to actually answer the question is just not there. Um, and of course there's other issues too, like outdated information.
[03:43] (The slide expands to include "Bad Response Generation" with sub-points: "Hallucination", "Irrelevance", "Toxicity/Bias".)
[03:44] And many of you who are building apps these days might be familiar with some like key concepts of like just why the LLM isn't always, you know, uh, guaranteed to give you a correct answer. There's hallucination, irrelevance, like toxicity bias, there's a lot of issues on the LLM side as well.

[03:57] (The slide changes to "What do we do?", showing the same RAG diagram as before, but with added questions and highlighted components: "Data", "Embeddings", "Retrieval", "Synthesis".)
[04:02] So, what can we do? Um, what can we actually do to try to improve the performance of a retrieval augmented generation application? Um, and and for many of you like you might be running into certain issues, and it really runs the gamut across like the entire pipeline. There are stuff you can do on the data, like can we store additional information beyond just like the raw text chunks, right? That that you're putting in the vector database. Can you optimize that data pipeline somehow? Play around with chunk sizes, that type of thing. Can you optimize the embedding representation itself? A lot of times when you're using a pre-trained embedding model, it's not really optimal for giving you the best performance.
[05:01] Um, there is the retrieval algorithm. You know, the default thing you do is just look up the top K most similar elements from your vector database to return to the LLM. Um, many times that's not enough and and what are kind of like both simple things you can do as well as hard things? Uh, and there's also synthesis. Like, uh, why is there yeah, there's like a V in the. Anyways, so so can we use LLMs for more than generation? Um, and so basically, like you can, um, use the LLM to actually help you with like reasoning as opposed to just like pure um, uh, pure, uh, just like, uh, just pure generation, right? You can actually use it to try to reason over given a question, can you break it down into simpler questions, route to different data sources, and kind of like, uh, have a, a more sophisticated way of like querying our data.
[05:18] (The slide adds "But before all this... We need a way to measure performance" at the bottom.)
[05:20] Um, of course, like if you've kind of been around some of my recent talks, like I always say, before you actually try any of these techniques, you need to be pretty task specific and make sure that you need a way to that you actually have a way to measure performance.

[05:31] (The slide changes to "Evaluation")
[05:33] So, I'll probably spend like two minutes talking about evaluation. Um, Simon, my co-founder, just ran a workshop yesterday on really just like how do you evaluate, uh, build a data set, evaluate RAG systems, and help iterate on that. Uh, if you missed the workshop, don't worry, I'll we'll have the slides and and materials, uh, available online so that you can take a look.
[05:49] (The slide changes to "Evaluation", adding "How do we properly evaluate a RAG system?" and lists "Evaluate in isolation (retrieval, synthesis)" and "Evaluate e2e". Below, the RAG diagram highlights "Retrieval" and "Synthesis".)
[05:51] Um, at a very high level, in terms of evaluation, it's important because you basically need to define a benchmark for your system to understand how are you going to iterate on and improve it. Uh, and there's like a few different ways you can try to do evaluation. I think Anton from, from Chroma, was, was just saying some of this, but like, you basically need a way to, um, evaluate both the end-to-end solution, like you have your input query as well as the output response. You also want to probably be able to evaluate like specific components. Like if you've diagnosed that the retrieval is the, is like the portion that needs improving, you need like retrieval metrics to really understand how can you improve your retrieval system.
[06:27] (The speaker explains the components of evaluation.)
[06:28] Um, so there's retrieval and there's synthesis.
[06:28] (The slide changes to "Evaluation in Isolation (Retrieval)". It lists "Evaluate quality of retrieved chunks given user query", "Create dataset", "Run retriever over dataset", "Measure ranking metrics". A diagram illustrates a "User Query" going to a "Retriever", which outputs "Retrieved IDs". An "Evaluator" compares "Retrieved IDs" with "Expected IDs".)
[06:31] Let's talk a little bit just like 30 seconds on each one. Um, evaluation on retrieval, what does this look like? You basically want to make sure that the stuff that's returned actually answers the query and that you're kind of, you know, not returning a bunch of fluff, uh, and that the stuff that you returned is relevant to the question. Um, so, first you need an evaluation dataset. A lot of people are, uh, have like human labeled datasets, if you're in, uh, building stuff in prod, you might have like user feedback as well. If not, you can synthetically generate a dataset. This dataset is input, like query, and output the IDs of like the returned documents are relevant to the query. So you need that somehow.
[07:30] (The speaker highlights the importance of a dataset for evaluation.)
[07:31] Once you have that, you can measure stuff with ranking metrics, right? You can measure stuff like success rate, hit rate, MRR, NDCG, a variety of these things. Uh, and and so like once you are able to evaluate this, like this really isn't, uh, kind of like an LLM problem, this is like an IR problem. And this has been around for at least like a decade or two. Um, but a lot of this is becoming, you like, you know, it's it's still very relevant in the face of actually building these LLM apps.
[07:31] (The slide changes to "Evaluation E2E". It lists "Evaluation of final generated response given input", "Create Dataset", "Run through full RAG pipeline", "Collect evaluation metrics". A diagram shows "User Query" through "RAG Pipeline" to "Generated Response" and "Optional Context". This then feeds into a "Label-free Evaluator" or a "With-Label Evaluator".)
[07:33] The next piece here is, um, there's a retrieve portion, right? But then you generate a response from it. And then how do you actually evaluate the whole thing end-to-end? So, evaluation of the final response, uh, given the input. You still want to generate some sort of dataset, so you could do that through like human annotations, user feedback, you could have like ground truth reference answers given the query that really indicates like, hey, this is the proper answer to this question. Um, and you can also just like, you know, synthetically generate it with like GPT-4. Uh, you run this through the full RAG pipeline that you built, the retrieval and synthesis, uh, and you can run like LLM-based evals. Um, so label-free evals, with-label evals. There's a lot of, uh, projects these days, uh, going on about, uh, how do you actually properly evaluate the outputs, uh, predicted outputs of a language model.

[08:14] (The slide changes to "Optimizing RAG Systems")
[08:16] Once you've defined your eval benchmark, now you want to think about how do you actually optimize your RAG systems.
[08:21] (The slide changes to "From Simple to Advanced RAG". It shows a spectrum from "Less Expressive, Easier to Implement, Lower Latency/Cost" to "More Expressive, Harder to Implement, Higher Latency/Cost". Categories include "Table Stakes" (Better Parsers, Chunk Sizes, Hybrid Search, Metadata Filters), "Advanced Retrieval" (Reranking, Recursive Retrieval, Embedded Tables, Small-to-big Retrieval), "Agentic Behavior" (Routing, Query Planning, Multi-document Agents), and "Fine-tuning" (Embedding fine-tuning, LLM fine-tuning).)
[08:22] So, I sent a teaser on the slide, uh, a few like yesterday, but the way I think about this is that, when you want to actually improve your system, there's like a million things you can do to try to actually improve your RAG system. Uh, and like you probably don't want to start with the hard stuff first, uh, just because like, you know, part of the value of language models is how it's kind of democratized access to every developer. It's really just made it easy for people to get up and running. And so if for instance you're running into some performance issues with RAG, I'd probably start with the basics, like I call it like table stakes RAG techniques. Uh, better parsing, um, so that you don't just split by even chunks, like adjusting your chunk sizes, trying out stuff that's already integrated with a vector database, like hybrid search, as well as like metadata filters.
[09:50] (The speaker points to the "Table Stakes" section of the slide.)
[09:51] There's also like advanced retrieval methods, uh, that you could try. This is like a little bit more advanced. Some of it pulls from like traditional IR, some of it's more like kind of, uh, really like, uh, new in this age of like LLM-based apps. There's like, uh, reranking, um, that's a traditional concept. There's also concepts in LlamaIndex like recursive retrieval, like dealing with embedded tables, like, uh, small-to-big retrieval, and a lot of other stuff that we have that help you potentially improve the performance of your application. Uh, and then the last bit like this kind of gets into more expressive stuff that might be harder to implement, might incur a higher latency and cost, but is potentially more powerful and forward-looking is like agents, like how do you incorporate agents towards better like RAG pipelines to better answer different types of questions and synthesize information. Uh, and how do you actually fine-tune stuff?
[09:51] (The slide changes to "Table Stakes: Chunk Sizes". It shows a series of bar charts comparing "Incorrect QA %" for different chunk sizes and retrieval methods, along with notes about retrieved tokens and reranking.)
[09:55] Let's talk a little bit about the table stakes first. So, chunk sizes. Tuning your chunk size can have outsized impacts on performance, right? Uh, if you've kind of like played around with RAG systems, this may or may not be obvious to you. What's interesting though is that like, more retrieved tokens does not always equate to higher performance. And that if you do like reranking of your retrieved tokens, it doesn't necessarily mean that your final generation response is going to be better. And this is again, due to stuff like lost in the middle problems where stuff in the middle of the LLM context window tends to get lost, whereas stuff at the end, uh, tends to be a little bit, uh, more well remembered by the LLM. Um, and so I think we did a workshop with like Arize a few, uh, a week ago, where basically we showed, you know, there is kind of like an optimal chunk size given your dataset, and a lot of times when you try out stuff like reranking, it actually increases your error metrics.

[10:40] (The slide changes to "Table Stakes: Metadata Filtering". It defines "Metadata: context you can inject into each text chunk" and gives examples like page number, document title, summary, questions. It also lists "Benefits".)
[10:42] Metadata filtering. Uh, this is another like very table stakes thing that I think everybody should look into, and I think vector databases, like, you know, Chroma, Pinecone, Weaviate, like these, uh, vector databases are all implementing these, uh, capabilities under the hood. Metadata filtering is basically just like how can you add structured context, uh, to your your chunks, like your text chunks, and you can use this for both for embeddings as well as synthesis, but it also integrates with like the metadata filter capabilities of a vector database. Um, so metadata is just like, again, structured JSON dictionary. It could be like page number, it could be the document title, it could be the summary of adjacent chunks, you can get creative with it too. You could hallucinate like questions, uh, that the chunk answers. Um, and it can help retrieval, it can help augment your response quality. It also integrates with the vector database filter.
[11:27] (The slide changes to "Table Stakes: Metadata Filtering", showing an example question "Can you tell me the risk factors in 2021?" and a diagram illustrating raw semantic search with low precision, returning chunks from various years.)
[11:30] So, as an example, um, let's say the question is over like the SCC, uh, like 10K document and I like, can you tell me the risk factors in 2021? If you just do raw semantic search, typically it's very low precision. You're going to return a bunch of stuff that may or may not match this. You might even return stuff from like other years if you have a bunch of documents from different years in the same vector collection. Um, and so like you're kind of like rolling the dice a little bit.
[11:52] (The slide changes to "Table Stakes: Metadata Filtering", showing how metadata filters (year=2021) can improve precision by removing irrelevant candidates, leaving only 2021 documents.)
[11:54] But one idea here is basically, you know, if you have access to the metadata of the documents, um, and you ask a question like this, you basically combine structured query capabilities by inferring the metadata filters, like a where clause in a SQL statement, like a year equals 2021, and you combine that with semantic search to return the most relevant candidates given your query. And this improves the precision of your, uh, of your results.

[12:17] (The slide changes to "Advanced Retrieval: Small-to-Big". It shows the intuition: "Embedding a big text chunk feels suboptimal." and a solution: "Embed text at the sentence-level - then expand that window during LLM synthesis". A diagram illustrates this with an "Embedding Lookup" from a query to a small chunk, which then expands for what the LLM sees.)
[12:20] Moving on to stuff that's maybe a bit more advanced, like advanced retrieval is one thing that we found generally helps is this idea of like small-to-big retrieval. Um, so what does that mean? Basically, right now, when you embed big text chunk, you also synthesize over that text chunk. And so it's a little suboptimal because what if like the embedding representation is like biased because, you know, there's a bunch of fluff in that text chunk that contains a bunch of irrelevant information, you're not actually optimizing your retrieval quality. So, embedding a big text chunk sometimes feels a little suboptimal. One thing that you could do is basically embed text at the sentence level or on a smaller level, and then expand that window during synthesis time.
[13:17] (The slide changes to "Advanced Retrieval: Small-to-Big", showing examples of "Sentence Window Retrieval" (k=2) leading to more precise retrieval and avoiding "lost in the middle" problems, compared to "Naive Retrieval" (k=5) where only one out of five chunks is relevant, causing the "lost in the middle" problem.)
[13:20] Uh, and so this is contained in a variety of like LlamaIndex abstractions, but the idea is that you return, you retrieve on more granular pieces of information, so smaller chunks. This makes it so that these chunks are more likely to be retrieved when you actually ask a query over these specific pieces of the context, but then you want to make sure that the LLM actually has access to more information to actually synthesize a proper result. So, this leads to like more precise retrieval, right? So, um, we, we tried this out. It, it helps avoid like some lost in the middle problems. You can set a smaller top K value, like K equals 2, uh, whereas like, uh, over this data set, if you set like K equals 5 for naive retrieval over big text chunks, you basically start returning a lot of context and that kind of leads into issues where, uh, you know, maybe the relevant context is in the middle, but you're not able to find out, uh, or or you're like, like the the LLM is is is not able to, uh, kind of, uh, synthesize over that information.
[13:49] (The slide changes to "Advanced Retrieval: Small-to-Big", showing "Recursive Retrieval (Chunk References)" and "Recursive Retrieval (Metadata References)" with diagrams illustrating how queries can retrieve references that point to larger parent chunks for synthesis. A table compares retrievers' hit_rate and mrr.)
[13:51] A very related idea here is just like embedding a reference to the parent chunk, um, as opposed to the actual text chunk itself. So, for instance, if you want to embed like not just the raw text chunk, or not the text chunk, but actually like a smaller chunk, um, or a summary, or questions that answer the chunk, we have found that that actually helps to improve retrieval performance a decent amount. Um, and it's it kind of go again, goes along with this idea like a lot of times you want to embed something that's more amenable for embedding based retrieval, uh, but then you want to return enough context so that the LLM can actually synthesize over that information.

[14:27] (The slide changes to "Agentic Behavior: Multi-Document Agents". It states "Intuition: There's certain questions that "top-k" RAG can't answer." and "Solution: Multi-Document Agents" with sub-points: "Fact-based QA and Summarization over any subsets of documents" and "Chain-of-thought and query planning". A diagram shows a "Multi-Document Agent" retrieving from multiple "Document Agent"s, each of which can perform "Vector Search" or "Summarization".)
[14:31] The next bit here is actually kind of even more advanced stuff, right? This goes on into agents, and this goes on into that last pillar that I, I mentioned, which is how do you use LLMs for for reasoning as opposed to just synthesis? The intuition here is that like for a lot of RAG, if you're just using the LLM at the end, you're one constrained by the quality of your retriever, and you're really only able to do stuff like question answering. And there's certain types of questions and more advanced analysis that you might want to launch that like top K RAG can't really answer. It's it's not necessarily just a one-off question. You might need to have like an entire sequence of reasoning steps actually pull together a piece of information, or you might want to like summarize the document and compare it with like other documents.
[15:30] (The speaker, Jerry Liu, is back on stage, explaining the multi-document agent concept.)
[15:33] So, one kind of architecture we're exploring right now is this idea of like multi-document agents. What if like instead of just like RAG, we moved a little bit more into agent territory. We modeled each document not just as a sequence of text chunks, but actually as a set of tools that contains the ability to both like summarize that document, as well as to do QA over that document over specific facts. Um, and of course, if you want to scale to like, you know, hundreds or thousands or millions of documents, um, a typically an agent can only have access to a limited window of tools.
[15:43] (The speaker gestures to emphasize points.)
[15:44] So, you probably want to do some sort of retrieval on these tools, similar to how you want to retrieve like text chunks from a document. The main difference is that because these are tools, you actually want to act upon them. You want to use them as opposed to just like taking the raw text and plugging it into the context window. So, blending this combination of like, uh, kind of, um, embedding based retrieval or any sort of retrieval, as well as like agent tool use, is a very interesting paradigm that I think is really only possible with this age of like LLMs and hasn't really existed, uh, before this.

[16:11] (The slide changes to "Fine-Tuning: Embeddings". It states "Intuition: Embedding Representations are not optimized over your dataset" and "Solution: Generate a synthetic query dataset from raw text chunks using LLMs. Use this synthetic dataset to finetune an embedding model." A diagram shows "Documents" being used to "Generate LLM Query Generation Prompts", which go through a "Large Language Model" to "Synthetic Queries for Documents". This "Synthetic Labeled Data" is then used to "Fine-tune an Embedding Model".)
[16:14] Another kind of advanced concept is this idea of fine-tuning. Um, and so fine-tuning, uh, you know, some other presenters have talked about this as well. But the idea of like fine-tuning in a RAG system is that it really optimizes specific pieces of this RAG pipeline for you to kind of better, um, like in improve the performance of either retriever or synthesis capabilities. So, one thing you can do is fine-tune your embeddings. Um, I think Anton was talking about this as well. Like if you just use a pre-trained model, the embedding representations are not going to be optimized over your specific data. So, sometimes you're just going to retrieve the wrong, wrong information. Um, if you can somehow tune these embeddings so that given any sort of like relevant question that the user might ask, that you're actually returning the relevant response, then you're going to have like better performance. So, an idea here, right, is to generate a synthetic query dataset from raw text chunks using LLMs and use this to fine-tune an embedding model. Um, and you can do this like,
[17:31] (The slide changes to "Fine-Tuning: LLMs". It states "Intuition: Weaker LLMs are not bad at response synthesis, reasoning, structured outputs, etc." and "Solution: Generate a synthetic dataset from raw chunks (e.g. using GPT-4). Help fix all of the above!" A diagram shows "Llama 2 Paper" leading to "Chunk", then "GPT-4" for "Generator" and "Question", then "GPT-4" again to "Generate Answers with Question/Context", resulting in a "Question Answer Dataset" used for "Fine-tuning" and ultimately a "Fine-tuned Model".)
[17:33] Uh, if we go back really quick, actually, uh, you can do this by basically, um, kind of fine-tuning the base model itself. You can also fine-tune an adapter on top of the model. Um, and fine-tuning an adapter on top of the model has a few advantages in that it, it don't require the base model's weights to actually fine-tune stuff. And if you just fine-tune the query, you don't have to re-index your entire document corpus. There's also fine-tuning LLMs, which of course, like a lot of people are very interested in doing these days. Um, an intuition here specifically for RAG is that if you have a weaker LLM, like 3.5 Turbo, like Llama 2, 7B, like these weaker LLMs are bad are are are not bad at like, um, uh, wait, yeah, weaker LLMs are are maybe a little bit worse at like response synthesis, reasoning, structured outputs, etc.
[18:13] (The speaker, Jerry Liu, is on stage as the slide is shown.)
[18:14] Um, compared to like bigger models. So, a solution here is what if you can generate a synthetic dataset, using a bigger model, like GPT-4, the something we're exploring. And you actually distill that into 3.5 Turbo. So, it gets better at chain of thought, longer response quality, um, better structured outputs, and a lot of other possibilities as well.
[18:16] (The speaker concludes his presentation.)
[18:17] So, all these things are in our docs. There's Production RAG, uh, there's Fine-tuning, and I have two seconds left. So, thank you very much.
[18:20] (The slide displays "Resources" with QR codes and links for "Production RAG" and "Fine-tuning".)
[18:24] (Audience applauds as the speaker exits the stage.)
[18:31] (Video outro with "AI Engineer SUMMIT" logo and music fades out.)

*Summary of the video*:
The speaker, Jerry Liu, CEO of LlamaIndex, provides a comprehensive overview of building and optimizing Retrieval Augmented Generation (RAG) applications, covering common GenAI use cases, paradigms for incorporating knowledge into LLMs (retrieval augmentation vs. fine-tuning), and the current RAG stack for QA systems. He highlights challenges with "naive" RAG, particularly regarding response quality due to bad retrieval (low precision, low recall, outdated information) and bad response generation (hallucination, irrelevance, bias). The presentation then details various strategies for improving RAG systems, categorized from "Table Stakes" (e.g., chunk sizes, metadata filtering) to "Advanced Retrieval" (e.g., small-to-big retrieval) and "Agentic Behavior" (e.g., multi-document agents), emphasizing the importance of evaluation and fine-tuning embeddings and LLMs to achieve better performance.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="gemini-cli-your-open-source-ai-agent.md">
<details>
<summary>Gemini CLI: your open-source AI agent</summary>

Phase: [EXPLOITATION]

# Gemini CLI: your open-source AI agent

**Source URL:** <https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/>

Free and open source, Gemini CLI brings Gemini directly into developers’ terminals — with unmatched access for individuals.

For developers, the command line interface (CLI) isn't just a tool; it's home. The terminal’s efficiency, ubiquity and portability make it the go-to utility for getting work done. And as developers' reliance on the terminal endures, so does the demand for integrated AI assistance.

That’s why we’re introducing [Gemini CLI](http://github.com/google-gemini/gemini-cli), an open-source AI agent that brings the power of Gemini directly into your terminal. It provides lightweight access to Gemini, giving you the most direct path from your prompt to our model. While it excels at coding, we built Gemini CLI to do so much more. It’s a versatile, local utility you can use for a wide range of tasks, from content generation and problem solving to deep research and task management.

We’ve also integrated Gemini CLI with Google’s AI coding assistant, [Gemini Code Assist](https://codeassist.google/), so that all developers — on free, Standard, and Enterprise Code Assist plans — get prompt-driven, AI-first coding in both VS Code and Gemini CLI.

https://storage.googleapis.com/gweb-uniblog-publish-prod/original_images/Gemini_CLI_GIF.gif

## Unmatched usage limits for individual developers

To use Gemini CLI free-of-charge, simply login with a personal Google account to get a free Gemini Code Assist license. That free license gets you access to Gemini 2.5 Pro and its massive 1 million token context window. To ensure you rarely, if ever, hit a limit during this preview, we offer the industry’s largest allowance: 60 model requests per minute and 1,000 requests per day at no charge.

If you’re a professional developer who needs to run multiple agents simultaneously, or if you prefer to use specific models, you can use a [Google AI Studio](https://aistudio.google.com/apikey) or [Vertex AI](https://console.cloud.google.com/vertex-ai/studio/multimodal) key for usage-based billing or get a Gemini Code Assist Standard or Enterprise license.

https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Gemini_CLI_infographic.width-100.format-webp.webp

Gemini CLI offers the industry’s largest usage allowance at 60 model requests per minute and 1,000 model requests per day at no charge

## Powerful models in your command line

Now in preview, Gemini CLI provides powerful AI capabilities, from code understanding and file manipulation to command execution and dynamic troubleshooting. It offers a fundamental upgrade to your command line experience, enabling you to write code, debug issues and streamline your workflow with natural language.

Its power comes from built-in tools allowing you to:

- **Ground prompts with Google Search** so you can fetch web pages and provide real-time, external context to the model
- **Extend Gemini CLI’s capabilities** through built-in support for the Model Context Protocol (MCP) or bundled extensions
- **Customize prompts and instructions** to tailor Gemini for your specific needs and workflows
- **Automate tasks and integrate with existing workflows** by invoking Gemini CLI non-interactively within your scripts

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GenMedia_demo_keyword.mp4) and watch it with your favorite video player!

Gemini CLI can be used for a wide variety of tasks, including making a short video showing the story of a ginger cat’s adventures around Australia with Veo and Imagen

## Open and extensible

Because Gemini CLI is fully [open source (Apache 2.0)](https://github.com/google-gemini/gemini-cli/blob/main/LICENSE), developers can inspect the code to understand how it works and verify its security implications. We fully expect (and welcome!) a global community of developers to [contribute to this project](https://github.com/google-gemini/gemini-cli/blob/main/CONTRIBUTING.md) by reporting bugs, suggesting features, continuously improving security practices and submitting code improvements. [Post your issues](http://github.com/google-gemini/gemini-cli/issues) or [submit your ideas](http://github.com/google-gemini/gemini-cli/discussions) in our GitHub repo.

We also built Gemini CLI to be extensible, building on emerging standards like MCP, system prompts (via GEMINI.md) and settings for both personal and team configuration. We know the terminal is a personal space, and everyone deserves the autonomy to make theirs unique.

## Shared technology with Gemini Code Assist

Sometimes, an IDE is the right tool for the job. When that time comes, you want all the capabilities of a powerful AI agent by your side to iterate, learn and overcome issues quickly.

[Gemini Code Assist](https://codeassist.google/), Google’s AI coding assistant for students, hobbyists and professional developers, now shares the same technology with Gemini CLI. In VS Code, you can place any prompt into the chat window using agent mode, and Code Assist will relentlessly work on your behalf to write tests, fix errors, build out features or even migrate your code. Based on your prompt, Code Assist’s agent will build a multi-step plan, auto-recover from failed implementation paths and recommend solutions you may not have even imagined.

Sorry, your browser doesn't support embedded videos, but don't worry, you can [download it](https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/gemini_cli_code_assist_demo_cut.mp4) and watch it with your favorite video player!

Gemini Code Assist’s chat agent is a multi-step, collaborative, reasoning agent that expands the capabilities of simple-command response interactions

Gemini Code Assist agent mode is available at no additional cost for all plans (free, Standard and Enterprise) through the [Insiders channel](https://developers.google.com/gemini-code-assist/docs/use-agentic-chat-pair-programmer#before-you-begin). If you aren’t already using Gemini Code Assist, give it a try. Its free tier has the highest usage limit in the market today, and only takes less than a minute to [get started](https://codeassist.google/).

## Easy to get started

So what are you waiting for? Upgrade your terminal experience with Gemini CLI today. Get [started by installing Gemini CLI.](http://github.com/google-gemini/gemini-cli) All you need is an email address to get Gemini practically unlimited in your terminal.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="google-gemini_gemini-cli.md">
<details>
<summary>Gemini CLI README.md</summary>

Phase: [EXPLOITATION]

# Gemini CLI README.md

## Summary
Repository: google-gemini/gemini-cli
Commit: 8573650253888a252500856e240385ff8a2553c8
Files analyzed: 2511

Estimated tokens: 5.1M

## File tree
```Directory structure:
└── google-gemini-gemini-cli/
    ├── README.md
    ├── CONTRIBUTING.md
    ├── Dockerfile
    ├── esbuild.config.js
    ├── eslint.config.js
    ├── GEMINI.md
    ├── LICENSE
    ├── Makefile
    ├── package.json
    ├── ROADMAP.md
    ├── SECURITY.md
    ├── tsconfig.json
    ├── .editorconfig
    ├── .geminiignore
    ├── .lycheeignore
    ├── .npmrc
    ├── .nvmrc
    ├── .prettierignore
    ├── .prettierrc.json
    ├── .yamllint.yml
    ├── docs/
    │   ├── index.md
    │   ├── integration-tests.md
    │   ├── issue-and-pr-automation.md
    │   ├── local-development.md
    │   ├── npm.md
    │   ├── redirects.json
    │   ├── release-confidence.md
    │   ├── releases.md
    │   ├── sidebar.json
    │   ├── admin/
    │   │   └── enterprise-controls.md
    │   ├── changelogs/
    │   │   ├── index.md
    │   │   ├── latest.md
    │   │   └── preview.md
    │   ├── cli/
    │   │   ├── acp-mode.md
    │   │   ├── auto-memory.md
    │   │   ├── checkpointing.md
    │   │   ├── cli-reference.md
    │   │   ├── creating-skills.md
    │   │   ├── custom-commands.md
    │   │   ├── enterprise.md
    │   │   ├── gemini-ignore.md
    │   │   ├── gemini-md.md
    │   │   ├── generation-settings.md
    │   │   ├── git-worktrees.md
    │   │   ├── headless.md
    │   │   ├── model-routing.md
    │   │   ├── model-steering.md
    │   │   ├── model.md
    │   │   ├── notifications.md
    │   │   ├── plan-mode.md
    │   │   ├── rewind.md
    │   │   ├── sandbox.md
    │   │   ├── session-management.md
    │   │   ├── settings.md
    │   │   ├── skills.md
    │   │   ├── system-prompt.md
    │   │   ├── telemetry.md
    │   │   ├── themes.md
    │   │   ├── token-caching.md
    │   │   ├── trusted-folders.md
    │   │   └── tutorials/
    │   │       ├── automation.md
    │   │       ├── file-management.md
    │   │       ├── mcp-setup.md
    │   │       ├── memory-management.md
    │   │       ├── plan-mode-steering.md
    │   │       ├── session-management.md
    │   │       ├── shell-commands.md
    │   │       ├── skills-getting-started.md
    │   │       ├── task-planning.md
    │   │       └── web-tools.md
    │   ├── CONTRIBUTING.md -> CONTRIBUTING.md
    │   ├── core/
    │   │   ├── index.md
    │   │   ├── local-model-routing.md
    │   │   ├── remote-agents.md
    │   │   └── subagents.md
    │   ├── examples/
    │   │   └── proxy-script.md
    │   ├── extensions/
    │   │   ├── best-practices.md
    │   │   ├── index.md
    │   │   ├── reference.md
    │   │   ├── releasing.md
    │   │   └── writing-extensions.md
    │   ├── get-started/
    │   │   ├── authentication.mdx
    │   │   ├── gemini-3.md
    │   │   ├── index.md
    │   │   └── installation.mdx
    │   ├── hooks/
    │   │   ├── best-practices.md
    │   │   ├── index.md
    │   │   ├── reference.md
    │   │   └── writing-hooks.md
    │   ├── ide-integration/
    │   │   ├── ide-companion-spec.md
    │   │   └── index.md
    │   ├── mermaid/
    │   │   ├── context.mmd
    │   │   └── render-path.mmd
    │   ├── reference/
    │   │   ├── commands.md
    │   │   ├── configuration.md
    │   │   ├── keyboard-shortcuts.md
    │   │   ├── memport.md
    │   │   ├── policy-engine.md
    │   │   └── tools.md
    │   ├── resources/
    │   │   ├── faq.md
    │   │   ├── quota-and-pricing.md
    │   │   ├── tos-privacy.md
    │   │   ├── troubleshooting.md
    │   │   └── uninstall.md
    │   └── tools/
    │       ├── activate-skill.md
    │       ├── ask-user.md
    │       ├── file-system.md
    │       ├── internal-docs.md
    │       ├── mcp-resources.md
    │       ├── mcp-server.md
    │       ├── memory.md
    │       ├── planning.md
    │       ├── shell.md
    │       ├── todos.md
    │       ├── web-fetch.md
    │       └── web-search.md
    ├── evals/
    │   ├── README.md
    │   ├── answer-vs-act.eval.ts
    │   ├── app-test-helper.ts
    │   ├── ask_user.eval.ts
    │   ├── automated-tool-use.eval.ts
    │   ├── background_processes.eval.ts
    │   ├── cli_help_delegation.eval.ts
    │   ├── component-test-helper.ts
    │   ├── concurrency-safety.eval.ts
    │   ├── edit-locations-eval.eval.ts
    │   ├── frugalReads.eval.ts
    │   ├── frugalSearch.eval.ts
    │   ├── generalist_agent.eval.ts
    │   ├── generalist_delegation.eval.ts
    │   ├── gitRepo.eval.ts
    │   ├── grep_search_functionality.eval.ts
    │   ├── hierarchical_memory.eval.ts
    │   ├── interactive-hang.eval.ts
    │   ├── model_steering.eval.ts
    │   ├── plan_mode.eval.ts
    │   ├── redundant_casts.eval.ts
    │   ├── sandbox_recovery.eval.ts
    │   ├── save_memory.eval.ts
    │   ├── shell-efficiency.eval.ts
    │   ├── skill_extraction.eval.ts
    │   ├── subagents.eval.ts
    │   ├── subtask_delegation.eval.ts
    │   ├── test-helper.test.ts
    │   ├── test-helper.ts
    │   ├── tool_output_masking.eval.ts
    │   ├── tracker.eval.ts
    │   ├── tsconfig.json
    │   ├── unsafe-cloning.eval.ts
    │   ├── update_topic.eval.ts
    │   ├── validation_fidelity.eval.ts
    │   ├── validation_fidelity_pre_existing_errors.eval.ts
    │   └── vitest.config.ts
    ├── integration-tests/
    │   ├── acp-env-auth.test.ts
    │   ├── acp-telemetry.test.ts
    │   ├── api-resilience.responses
    │   ├── api-resilience.test.ts
    │   ├── browser-agent-localhost.dynamic.responses
    │   ├── browser-agent-localhost.form.responses
    │   ├── browser-agent-localhost.multistep.responses
    │   ├── browser-agent-localhost.navigate.responses
    │   ├── browser-agent-localhost.screenshot.responses
    │   ├── browser-agent-localhost.test.ts
    │   ├── browser-agent.cleanup.responses
    │   ├── browser-agent.concurrent.responses
    │   ├── browser-agent.confirmation.responses
    │   ├── browser-agent.interaction.responses
    │   ├── browser-agent.navigate-snapshot.responses
    │   ├── browser-agent.persistent-session.responses
    │   ├── browser-agent.screenshot.responses
    │   ├── browser-agent.sequential.responses
    │   ├── browser-agent.test.ts
    │   ├── browser-policy.responses
    │   ├── browser-policy.test.ts
    │   ├── checkpointing.test.ts
    │   ├── clipboard-linux.test.ts
    │   ├── concurrency-limit.responses
    │   ├── concurrency-limit.test.ts
    │   ├── context-compress-interactive.compress-empty.responses
    │   ├── context-compress-interactive.compress-failure.responses
    │   ├── context-compress-interactive.compress.responses
    │   ├── context-compress-interactive.test.ts
    │   ├── ctrl-c-exit.test.ts
    │   ├── deprecation-warnings.test.ts
    │   ├── extensions-install.test.ts
    │   ├── extensions-reload.test.ts
    │   ├── file-system-interactive.test.ts
    │   ├── file-system.test.ts
    │   ├── flicker-detector.max-height.responses
    │   ├── flicker.test.ts
    │   ├── globalSetup.ts
    │   ├── google_web_search.test.ts
    │   ├── hooks-agent-flow-multistep.responses
    │   ├── hooks-agent-flow.responses
    │   ├── hooks-agent-flow.test.ts
    │   ├── hooks-system.after-agent.responses
    │   ├── hooks-system.after-model.responses
    │   ├── hooks-system.after-tool-context.responses
    │   ├── hooks-system.allow-tool.responses
    │   ├── hooks-system.before-agent.responses
    │   ├── hooks-system.before-model.responses
    │   ├── hooks-system.before-tool-selection.responses
    │   ├── hooks-system.before-tool-stop.responses
    │   ├── hooks-system.block-tool.responses
    │   ├── hooks-system.compress-auto.responses
    │   ├── hooks-system.disabled-via-command.responses
    │   ├── hooks-system.disabled-via-settings.responses
    │   ├── hooks-system.error-handling.responses
    │   ├── hooks-system.input-modification.responses
    │   ├── hooks-system.input-validation.responses
    │   ├── hooks-system.multiple-events.responses
    │   ├── hooks-system.notification.responses
    │   ├── hooks-system.sequential-execution.responses
    │   ├── hooks-system.session-clear.responses
    │   ├── hooks-system.session-startup.responses
    │   ├── hooks-system.tail-tool-call.responses
    │   ├── hooks-system.telemetry.responses
    │   ├── hooks-system.test.ts
    │   ├── json-output.error.responses
    │   ├── json-output.france.responses
    │   ├── json-output.session-id.responses
    │   ├── json-output.test.ts
    │   ├── list_directory.test.ts
    │   ├── mcp-list-resources.responses
    │   ├── mcp-read-resource.responses
    │   ├── mcp-resources.responses
    │   ├── mcp-resources.test.ts
    │   ├── mcp_server_cyclic_schema.test.ts
    │   ├── mixed-input-crash.test.ts
    │   ├── parallel-tools.responses
    │   ├── parallel-tools.test.ts
    │   ├── plan-mode.test.ts
    │   ├── policy-headless-readonly.responses
    │   ├── policy-headless-shell-allowed.responses
    │   ├── policy-headless-shell-denied.responses
    │   ├── policy-headless.test.ts
    │   ├── read_many_files.test.ts
    │   ├── replace.test.ts
    │   ├── resume_repro.responses
    │   ├── resume_repro.test.ts
    │   ├── ripgrep-real.test.ts
    │   ├── run_shell_command.test.ts
    │   ├── shell-background.responses
    │   ├── shell-background.test.ts
    │   ├── simple-mcp-server.test.ts
    │   ├── skill-creator-scripts.test.ts
    │   ├── skill-creator-vulnerabilities.test.ts
    │   ├── stdin-context.test.ts
    │   ├── stdout-stderr-output-error.responses
    │   ├── stdout-stderr-output.responses
    │   ├── stdout-stderr-output.test.ts
    │   ├── symlink-install.test.ts
    │   ├── telemetry.test.ts
    │   ├── test-helper.ts
    │   ├── test-mcp-server.ts
    │   ├── test-mcp-support.responses
    │   ├── test-mcp-support.test.ts
    │   ├── tsconfig.json
    │   ├── user-policy.responses
    │   ├── user-policy.test.ts
    │   ├── utf-bom-encoding.test.ts
    │   ├── vitest.config.ts
    │   ├── write_file.test.ts
    │   └── test-fixtures/
    │       ├── dynamic.html
    │       ├── form-result.html
    │       ├── form.html
    │       ├── index.html
    │       └── multi-step/
    │           ├── result.html
    │           ├── step1.html
    │           └── step2.html
    ├── memory-tests/
    │   ├── baselines.json
    │   ├── globalSetup.ts
    │   ├── memory-usage.test.ts
    │   ├── memory.idle-startup.responses
    │   ├── memory.multi-function-call.responses
    │   ├── memory.multi-turn.responses
    │   ├── memory.simple-prompt.responses
    │   ├── tsconfig.json
    │   └── vitest.config.ts
    ├── packages/
    │   ├── a2a-server/
    │   │   ├── README.md
    │   │   ├── development-extension-rfc.md
    │   │   ├── GEMINI.md
    │   │   ├── index.ts
    │   │   ├── package.json
    │   │   ├── tsconfig.json
    │   │   ├── vitest.config.ts
    │   │   └── src/
    │   │       ├── index.ts
    │   │       ├── types.ts
    │   │       ├── agent/
    │   │       │   ├── executor.test.ts
    │   │       │   ├── executor.ts
    │   │       │   ├── task-event-driven.test.ts
    │   │       │   ├── task.test.ts
    │   │       │   └── task.ts
    │   │       ├── commands/
    │   │       │   ├── command-registry.test.ts
    │   │       │   ├── command-registry.ts
    │   │       │   ├── extensions.test.ts
    │   │       │   ├── extensions.ts
    │   │       │   ├── init.test.ts
    │   │       │   ├── init.ts
    │   │       │   ├── memory.test.ts
    │   │       │   ├── memory.ts
    │   │       │   ├── restore.test.ts
    │   │       │   ├── restore.ts
    │   │       │   └── types.ts
    │   │       ├── config/
    │   │       │   ├── config.test.ts
    │   │       │   ├── config.ts
    │   │       │   ├── extension.ts
    │   │       │   ├── settings.test.ts
    │   │       │   └── settings.ts
    │   │       ├── http/
    │   │       │   ├── app.test.ts
    │   │       │   ├── app.ts
    │   │       │   ├── endpoints.test.ts
    │   │       │   ├── requestStorage.ts
    │   │       │   └── server.ts
    │   │       ├── persistence/
    │   │       │   ├── gcs.test.ts
    │   │       │   └── gcs.ts
    │   │       └── utils/
    │   │           ├── executor_utils.ts
    │   │           ├── logger.ts
    │   │           └── testing_utils.ts
    │   ├── cli/
    │   │   ├── GEMINI.md
    │   │   ├── index.ts
    │   │   ├── package.json
    │   │   ├── test-setup.ts
    │   │   ├── tsconfig.json
    │   │   ├── vitest.config.ts
    │   │   ├── examples/
    │   │   │   ├── ask-user-dialog-demo.tsx
    │   │   │   └── scrollable-list-demo.tsx
    │   │   └── src/
    │   │       ├── deferred.test.ts
    │   │       ├── deferred.ts
    │   │       ├── gemini.test.tsx
    │   │       ├── gemini.tsx
    │   │       ├── gemini_cleanup.test.tsx
    │   │       ├── interactiveCli.tsx
    │   │       ├── nonInteractiveCli.test.ts
    │   │       ├── nonInteractiveCli.ts
    │   │       ├── nonInteractiveCliAgentSession.test.ts
    │   │       ├── nonInteractiveCliAgentSession.ts
    │   │       ├── nonInteractiveCliCommands.ts
    │   │       ├── validateNonInterActiveAuth.test.ts
    │   │       ├── validateNonInterActiveAuth.ts
    │   │       ├── __snapshots__/
    │   │       │   ├── nonInteractiveCli.test.ts.snap
    │   │       │   └── nonInteractiveCliAgentSession.test.ts.snap
    │   │       ├── acp/
    │   │       │   ├── acpClient.test.ts
    │   │       │   ├── acpClient.ts
    │   │       │   ├── acpErrors.test.ts
    │   │       │   ├── acpErrors.ts
    │   │       │   ├── acpResume.test.ts
    │   │       │   ├── commandHandler.test.ts
    │   │       │   ├── commandHandler.ts
    │   │       │   ├── fileSystemService.test.ts
    │   │       │   ├── fileSystemService.ts
    │   │       │   └── commands/
    │   │       │       ├── about.ts
    │   │       │       ├── commandRegistry.ts
    │   │       │       ├── extensions.ts
    │   │       │       ├── help.test.ts
    │   │       │       ├── help.ts
    │   │       │       ├── init.ts
    │   │       │       ├── memory.ts
    │   │       │       ├── restore.ts
    │   │       │       └── types.ts
    │   │       ├── commands/
    │   │       │   ├── extensions.test.tsx
    │   │       │   ├── extensions.tsx
    │   │       │   ├── hooks.tsx
    │   │       │   ├── mcp.test.ts
    │   │       │   ├── mcp.ts
    │   │       │   ├── skills.test.tsx
    │   │       │   ├── skills.tsx
    │   │       │   ├── utils.test.ts
    │   │       │   ├── utils.ts
    │   │       │   ├── extensions/
    │   │       │   │   ├── configure.test.ts
    │   │       │   │   ├── configure.ts
    │   │       │   │   ├── disable.test.ts
    │   │       │   │   ├── disable.ts
    │   │       │   │   ├── enable.test.ts
    │   │       │   │   ├── enable.ts
    │   │       │   │   ├── install.test.ts
    │   │       │   │   ├── install.ts
    │   │       │   │   ├── link.test.ts
    │   │       │   │   ├── link.ts
    │   │       │   │   ├── list.test.ts
    │   │       │   │   ├── list.ts
    │   │       │   │   ├── new.test.ts
    │   │       │   │   ├── new.ts
    │   │       │   │   ├── uninstall.test.ts
    │   │       │   │   ├── uninstall.ts
    │   │       │   │   ├── update.test.ts
    │   │       │   │   ├── update.ts
    │   │       │   │   ├── utils.ts
    │   │       │   │   ├── validate.test.ts
    │   │       │   │   ├── validate.ts
    │   │       │   │   └── examples/
    │   │       │   │       ├── custom-commands/
    │   │       │   │       │   ├── gemini-extension.json
    │   │       │   │       │   └── commands/
    │   │       │   │       │       └── fs/
    │   │       │   │       │           └── grep-code.toml
    │   │       │   │       ├── exclude-tools/
    │   │       │   │       │   └── gemini-extension.json
    │   │       │   │       ├── hooks/
    │   │       │   │       │   ├── gemini-extension.json
    │   │       │   │       │   ├── hooks/
    │   │       │   │       │   │   └── hooks.json
    │   │       │   │       │   └── scripts/
    │   │       │   │       │       └── on-start.js
    │   │       │   │       ├── mcp-server/
    │   │       │   │       │   ├── README.md
    │   │       │   │       │   ├── example.js
    │   │       │   │       │   ├── gemini-extension.json
    │   │       │   │       │   └── package.json
    │   │       │   │       ├── policies/
    │   │       │   │       │   ├── README.md
    │   │       │   │       │   ├── gemini-extension.json
    │   │       │   │       │   └── policies/
    │   │       │   │       │       └── policies.toml
    │   │       │   │       ├── skills/
    │   │       │   │       │   ├── gemini-extension.json
    │   │       │   │       │   └── skills/
    │   │       │   │       │       └── greeter/
    │   │       │   │       │           └── SKILL.md
    │   │       │   │       └── themes-example/
    │   │       │   │           ├── README.md
    │   │       │   │           └── gemini-extension.json
    │   │       │   ├── hooks/
    │   │       │   │   ├── migrate.test.ts
    │   │       │   │   └── migrate.ts
    │   │       │   ├── mcp/
    │   │       │   │   ├── add.test.ts
    │   │       │   │   ├── add.ts
    │   │       │   │   ├── enableDisable.ts
    │   │       │   │   ├── list.test.ts
    │   │       │   │   ├── list.ts
    │   │       │   │   ├── remove.test.ts
    │   │       │   │   └── remove.ts
    │   │       │   └── skills/
    │   │       │       ├── disable.test.ts
    │   │       │       ├── disable.ts
    │   │       │       ├── enable.test.ts
    │   │       │       ├── enable.ts
    │   │       │       ├── install.test.ts
    │   │       │       ├── install.ts
    │   │       │       ├── link.test.ts
    │   │       │       ├── link.ts
    │   │       │       ├── list.test.ts
    │   │       │       ├── list.ts
    │   │       │       ├── uninstall.test.ts
    │   │       │       └── uninstall.ts
    │   │       ├── config/
    │   │       │   ├── auth.test.ts
    │   │       │   ├── auth.ts
    │   │       │   ├── config.integration.test.ts
    │   │       │   ├── config.test.ts
    │   │       │   ├── config.ts
    │   │       │   ├── extension-manager-agents.test.ts
    │   │       │   ├── extension-manager-hydration.test.ts
    │   │       │   ├── extension-manager-permissions.test.ts
    │   │       │   ├── extension-manager-scope.test.ts
    │   │       │   ├── extension-manager-skills.test.ts
    │   │       │   ├── extension-manager-themes.spec.ts
    │   │       │   ├── extension-manager.test.ts
    │   │       │   ├── extension-manager.ts
    │   │       │   ├── extension.test.ts
    │   │       │   ├── extension.ts
    │   │       │   ├── extensionRegistryClient.test.ts
    │   │       │   ├── extensionRegistryClient.ts
    │   │       │   ├── footerItems.test.ts
    │   │       │   ├── footerItems.ts
    │   │       │   ├── policy-engine.integration.test.ts
    │   │       │   ├── policy.test.ts
    │   │       │   ├── policy.ts
    │   │       │   ├── sandboxConfig.test.ts
    │   │       │   ├── sandboxConfig.ts
    │   │       │   ├── settingPaths.test.ts
    │   │       │   ├── settingPaths.ts
    │   │       │   ├── settings-validation.test.ts
    │   │       │   ├── settings-validation.ts
    │   │       │   ├── settings.test.ts
    │   │       │   ├── settings.ts
    │   │       │   ├── settings_repro.test.ts
    │   │       │   ├── settings_validation_warning.test.ts
    │   │       │   ├── settingsSchema.test.ts
    │   │       │   ├── settingsSchema.ts
    │   │       │   ├── trustedFolders.test.ts
    │   │       │   ├── trustedFolders.ts
    │   │       │   ├── workspace-policy-cli.test.ts
    │   │       │   ├── extensions/
    │   │       │   │   ├── consent.test.ts
    │   │       │   │   ├── consent.ts
    │   │       │   │   ├── extensionEnablement.test.ts
    │   │       │   │   ├── extensionEnablement.ts
    │   │       │   │   ├── extensionSettings.test.ts
    │   │       │   │   ├── extensionSettings.ts
    │   │       │   │   ├── extensionUpdates.test.ts
    │   │       │   │   ├── github.test.ts
    │   │       │   │   ├── github.ts
    │   │       │   │   ├── github_fetch.test.ts
    │   │       │   │   ├── github_fetch.ts
    │   │       │   │   ├── storage.test.ts
    │   │       │   │   ├── storage.ts
    │   │       │   │   ├── update.test.ts
    │   │       │   │   ├── update.ts
    │   │       │   │   ├── variables.test.ts
    │   │       │   │   ├── variables.ts
    │   │       │   │   ├── variableSchema.ts
    │   │       │   │   └── __snapshots__/
    │   │       │   │       └── consent.test.ts.snap
    │   │       │   └── mcp/
    │   │       │       ├── index.ts
    │   │       │       ├── mcpServerEnablement.test.ts
    │   │       │       └── mcpServerEnablement.ts
    │   │       ├── core/
    │   │       │   ├── auth.test.ts
    │   │       │   ├── auth.ts
    │   │       │   ├── initializer.test.ts
    │   │       │   ├── initializer.ts
    │   │       │   ├── theme.test.ts
    │   │       │   └── theme.ts
    │   │       ├── integration-tests/
    │   │       │   └── modelSteering.test.tsx
    │   │       ├── patches/
    │   │       │   └── is-in-ci.ts
    │   │       ├── services/
    │   │       │   ├── BuiltinCommandLoader.test.ts
    │   │       │   ├── BuiltinCommandLoader.ts
    │   │       │   ├── CommandService.test.ts
    │   │       │   ├── CommandService.ts
    │   │       │   ├── FileCommandLoader.test.ts
    │   │       │   ├── FileCommandLoader.ts
    │   │       │   ├── McpPromptLoader.test.ts
    │   │       │   ├── McpPromptLoader.ts
    │   │       │   ├── SkillCommandLoader.test.ts
    │   │       │   ├── SkillCommandLoader.ts
    │   │       │   ├── SlashCommandConflictHandler.test.ts
    │   │       │   ├── SlashCommandConflictHandler.ts
    │   │       │   ├── SlashCommandResolver.test.ts
    │   │       │   ├── SlashCommandResolver.ts
    │   │       │   ├── types.ts
    │   │       │   └── prompt-processors/
    │   │       │       ├── argumentProcessor.test.ts
    │   │       │       ├── argumentProcessor.ts
    │   │       │       ├── atFileProcessor.test.ts
    │   │       │       ├── atFileProcessor.ts
    │   │       │       ├── injectionParser.test.ts
    │   │       │       ├── injectionParser.ts
    │   │       │       ├── shellProcessor.test.ts
    │   │       │       ├── shellProcessor.ts
    │   │       │       └── types.ts
    │   │       ├── test-utils/
    │   │       │   ├── AppRig.test.tsx
    │   │       │   ├── AppRig.tsx
    │   │       │   ├── async.ts
    │   │       │   ├── createExtension.ts
    │   │       │   ├── customMatchers.ts
    │   │       │   ├── mockCommandContext.test.ts
    │   │       │   ├── mockCommandContext.ts
    │   │       │   ├── mockConfig.ts
    │   │       │   ├── mockDebugLogger.ts
    │   │       │   ├── MockShellExecutionService.ts
    │   │       │   ├── mockSpinner.tsx
    │   │       │   ├── persistentStateFake.ts
    │   │       │   ├── render.test.tsx
    │   │       │   ├── render.tsx
    │   │       │   ├── settings.ts
    │   │       │   ├── svg.ts
    │   │       │   └── fixtures/
    │   │       │       ├── simple.responses
    │   │       │       └── steering.responses
    │   │       ├── ui/
    │   │       │   ├── App.test.tsx
    │   │       │   ├── App.tsx
    │   │       │   ├── AppContainer.test.tsx
    │   │       │   ├── AppContainer.tsx
    │   │       │   ├── colors.ts
    │   │       │   ├── constants.ts
    │   │       │   ├── debug.ts
    │   │       │   ├── IdeIntegrationNudge.test.tsx
    │   │       │   ├── IdeIntegrationNudge.tsx
    │   │       │   ├── semantic-colors.ts
    │   │       │   ├── textConstants.ts
    │   │       │   ├── ToolConfirmationFullFrame.test.tsx
    │   │       │   ├── types.ts
    │   │       │   ├── __snapshots__/
    │   │       │   │   ├── App.test.tsx.snap
    │   │       │   │   └── ToolConfirmationFullFrame.test.tsx.snap
    │   │       │   ├── auth/
    │   │       │   │   ├── ApiAuthDialog.test.tsx
    │   │       │   │   ├── ApiAuthDialog.tsx
    │   │       │   │   ├── AuthDialog.test.tsx
    │   │       │   │   ├── AuthDialog.tsx
    │   │       │   │   ├── AuthInProgress.test.tsx
    │   │       │   │   ├── AuthInProgress.tsx
    │   │       │   │   ├── BannedAccountDialog.test.tsx
    │   │       │   │   ├── BannedAccountDialog.tsx
    │   │       │   │   ├── LoginWithGoogleRestartDialog.test.tsx
    │   │       │   │   ├── LoginWithGoogleRestartDialog.tsx
    │   │       │   │   ├── useAuth.test.tsx
    │   │       │   │   ├── useAuth.ts
    │   │       │   │   └── __snapshots__/
    │   │       │   │       ├── ApiAuthDialog.test.tsx.snap
    │   │       │   │       ├── AuthDialog.test.tsx.snap
    │   │       │   │       ├── BannedAccountDialog.test.tsx.snap
    │   │       │   │       └── LoginWithGoogleRestartDialog.test.tsx.snap
    │   │       │   ├── commands/
    │   │       │   │   ├── aboutCommand.test.ts
    │   │       │   │   ├── aboutCommand.ts
    │   │       │   │   ├── agentsCommand.test.ts
    │   │       │   │   ├── agentsCommand.ts
    │   │       │   │   ├── authCommand.test.ts
    │   │       │   │   ├── authCommand.ts
    │   │       │   │   ├── bugCommand.test.ts
    │   │       │   │   ├── bugCommand.ts
    │   │       │   │   ├── chatCommand.test.ts
    │   │       │   │   ├── chatCommand.ts
    │   │       │   │   ├── clearCommand.test.ts
    │   │       │   │   ├── clearCommand.ts
    │   │       │   │   ├── commandsCommand.test.ts
    │   │       │   │   ├── commandsCommand.ts
    │   │       │   │   ├── compressCommand.test.ts
    │   │       │   │   ├── compressCommand.ts
    │   │       │   │   ├── copyCommand.test.ts
    │   │       │   │   ├── copyCommand.ts
    │   │       │   │   ├── corgiCommand.test.ts
    │   │       │   │   ├── corgiCommand.ts
    │   │       │   │   ├── directoryCommand.test.tsx
    │   │       │   │   ├── directoryCommand.tsx
    │   │       │   │   ├── docsCommand.test.ts
    │   │       │   │   ├── docsCommand.ts
    │   │       │   │   ├── editorCommand.test.ts
    │   │       │   │   ├── editorCommand.ts
    │   │       │   │   ├── extensionsCommand.test.ts
    │   │       │   │   ├── extensionsCommand.ts
    │   │       │   │   ├── footerCommand.tsx
    │   │       │   │   ├── helpCommand.test.ts
    │   │       │   │   ├── helpCommand.ts
    │   │       │   │   ├── hooksCommand.test.ts
    │   │       │   │   ├── hooksCommand.ts
    │   │       │   │   ├── ideCommand.test.ts
    │   │       │   │   ├── ideCommand.ts
    │   │       │   │   ├── initCommand.test.ts
    │   │       │   │   ├── initCommand.ts
    │   │       │   │   ├── mcpCommand.test.ts
    │   │       │   │   ├── mcpCommand.ts
    │   │       │   │   ├── memoryCommand.test.ts
    │   │       │   │   ├── memoryCommand.ts
    │   │       │   │   ├── modelCommand.test.ts
    │   │       │   │   ├── modelCommand.ts
    │   │       │   │   ├── oncallCommand.tsx
    │   │       │   │   ├── permissionsCommand.test.ts
    │   │       │   │   ├── permissionsCommand.ts
    │   │       │   │   ├── planCommand.test.ts
    │   │       │   │   ├── planCommand.ts
    │   │       │   │   ├── policiesCommand.test.ts
    │   │       │   │   ├── policiesCommand.ts
    │   │       │   │   ├── privacyCommand.test.ts
    │   │       │   │   ├── privacyCommand.ts
    │   │       │   │   ├── profileCommand.ts
    │   │       │   │   ├── quitCommand.test.ts
    │   │       │   │   ├── quitCommand.ts
    │   │       │   │   ├── restoreCommand.test.ts
    │   │       │   │   ├── restoreCommand.ts
    │   │       │   │   ├── resumeCommand.test.ts
    │   │       │   │   ├── resumeCommand.ts
    │   │       │   │   ├── rewindCommand.test.tsx
    │   │       │   │   ├── rewindCommand.tsx
    │   │       │   │   ├── settingsCommand.test.ts
    │   │       │   │   ├── settingsCommand.ts
    │   │       │   │   ├── setupGithubCommand.test.ts
    │   │       │   │   ├── setupGithubCommand.ts
    │   │       │   │   ├── shortcutsCommand.ts
    │   │       │   │   ├── skillsCommand.test.ts
    │   │       │   │   ├── skillsCommand.ts
    │   │       │   │   ├── statsCommand.test.ts
    │   │       │   │   ├── statsCommand.ts
    │   │       │   │   ├── tasksCommand.test.ts
    │   │       │   │   ├── tasksCommand.ts
    │   │       │   │   ├── terminalSetupCommand.test.ts
    │   │       │   │   ├── terminalSetupCommand.ts
    │   │       │   │   ├── themeCommand.test.ts
    │   │       │   │   ├── themeCommand.ts
    │   │       │   │   ├── toolsCommand.test.ts
    │   │       │   │   ├── toolsCommand.ts
    │   │       │   │   ├── types.ts
    │   │       │   │   ├── upgradeCommand.test.ts
    │   │       │   │   ├── upgradeCommand.ts
    │   │       │   │   └── vimCommand.ts
    │   │       │   ├── components/
    │   │       │   │   ├── AboutBox.test.tsx
    │   │       │   │   ├── AboutBox.tsx
    │   │       │   │   ├── AdminSettingsChangedDialog.test.tsx
    │   │       │   │   ├── AdminSettingsChangedDialog.tsx
    │   │       │   │   ├── AgentConfigDialog.test.tsx
    │   │       │   │   ├── AgentConfigDialog.tsx
    │   │       │   │   ├── AlternateBufferQuittingDisplay.test.tsx
    │   │       │   │   ├── AlternateBufferQuittingDisplay.tsx
    │   │       │   │   ├── AnsiOutput.test.tsx
    │   │       │   │   ├── AnsiOutput.tsx
    │   │       │   │   ├── AppHeader.test.tsx
    │   │       │   │   ├── AppHeader.tsx
    │   │       │   │   ├── AppHeaderIcon.test.tsx
    │   │       │   │   ├── ApprovalModeIndicator.test.tsx
    │   │       │   │   ├── ApprovalModeIndicator.tsx
    │   │       │   │   ├── AsciiArt.ts
    │   │       │   │   ├── AskUserDialog.test.tsx
    │   │       │   │   ├── AskUserDialog.tsx
    │   │       │   │   ├── BackgroundTaskDisplay.test.tsx
    │   │       │   │   ├── BackgroundTaskDisplay.tsx
    │   │       │   │   ├── Banner.test.tsx
    │   │       │   │   ├── Banner.tsx
    │   │       │   │   ├── BubblingRegression.test.tsx
    │   │       │   │   ├── Checklist.test.tsx
    │   │       │   │   ├── Checklist.tsx
    │   │       │   │   ├── ChecklistItem.test.tsx
    │   │       │   │   ├── ChecklistItem.tsx
    │   │       │   │   ├── CliSpinner.test.tsx
    │   │       │   │   ├── CliSpinner.tsx
    │   │       │   │   ├── ColorsDisplay.test.tsx
    │   │       │   │   ├── ColorsDisplay.tsx
    │   │       │   │   ├── Composer.test.tsx
    │   │       │   │   ├── Composer.tsx
    │   │       │   │   ├── ConfigExtensionDialog.tsx
    │   │       │   │   ├── ConfigInitDisplay.test.tsx
    │   │       │   │   ├── ConfigInitDisplay.tsx
    │   │       │   │   ├── ConsentPrompt.test.tsx
    │   │       │   │   ├── ConsentPrompt.tsx
    │   │       │   │   ├── ConsoleSummaryDisplay.test.tsx
    │   │       │   │   ├── ConsoleSummaryDisplay.tsx
    │   │       │   │   ├── ContextSummaryDisplay.test.tsx
    │   │       │   │   ├── ContextSummaryDisplay.tsx
    │   │       │   │   ├── ContextUsageDisplay.test.tsx
    │   │       │   │   ├── ContextUsageDisplay.tsx
    │   │       │   │   ├── CopyModeWarning.test.tsx
    │   │       │   │   ├── CopyModeWarning.tsx
    │   │       │   │   ├── DebugProfiler.test.tsx
    │   │       │   │   ├── DebugProfiler.tsx
    │   │       │   │   ├── DetailedMessagesDisplay.test.tsx
    │   │       │   │   ├── DetailedMessagesDisplay.tsx
    │   │       │   │   ├── DialogManager.test.tsx
    │   │       │   │   ├── DialogManager.tsx
    │   │       │   │   ├── EditorSettingsDialog.test.tsx
    │   │       │   │   ├── EditorSettingsDialog.tsx
    │   │       │   │   ├── EmptyWalletDialog.test.tsx
    │   │       │   │   ├── EmptyWalletDialog.tsx
    │   │       │   │   ├── ExitPlanModeDialog.test.tsx
    │   │       │   │   ├── ExitPlanModeDialog.tsx
    │   │       │   │   ├── ExitWarning.test.tsx
    │   │       │   │   ├── ExitWarning.tsx
    │   │       │   │   ├── FolderTrustDialog.test.tsx
    │   │       │   │   ├── FolderTrustDialog.tsx
    │   │       │   │   ├── Footer.test.tsx
    │   │       │   │   ├── Footer.tsx
    │   │       │   │   ├── FooterConfigDialog.test.tsx
    │   │       │   │   ├── FooterConfigDialog.tsx
    │   │       │   │   ├── GeminiRespondingSpinner.test.tsx
    │   │       │   │   ├── GeminiRespondingSpinner.tsx
    │   │       │   │   ├── GeminiSpinner.tsx
    │   │       │   │   ├── GradientRegression.test.tsx
    │   │       │   │   ├── Header.test.tsx
    │   │       │   │   ├── Header.tsx
    │   │       │   │   ├── Help.test.tsx
    │   │       │   │   ├── Help.tsx
    │   │       │   │   ├── HistoryItemDisplay.test.tsx
    │   │       │   │   ├── HistoryItemDisplay.tsx
    │   │       │   │   ├── HooksDialog.test.tsx
    │   │       │   │   ├── HooksDialog.tsx
    │   │       │   │   ├── HookStatusDisplay.test.tsx
    │   │       │   │   ├── HookStatusDisplay.tsx
    │   │       │   │   ├── IdeTrustChangeDialog.test.tsx
    │   │       │   │   ├── IdeTrustChangeDialog.tsx
    │   │       │   │   ├── InputPrompt.test.tsx
    │   │       │   │   ├── InputPrompt.tsx
    │   │       │   │   ├── LoadingIndicator.test.tsx
    │   │       │   │   ├── LoadingIndicator.tsx
    │   │       │   │   ├── LogoutConfirmationDialog.test.tsx
    │   │       │   │   ├── LogoutConfirmationDialog.tsx
    │   │       │   │   ├── LoopDetectionConfirmation.test.tsx
    │   │       │   │   ├── LoopDetectionConfirmation.tsx
    │   │       │   │   ├── MainContent.test.tsx
    │   │       │   │   ├── MainContent.tsx
    │   │       │   │   ├── MemoryUsageDisplay.test.tsx
    │   │       │   │   ├── MemoryUsageDisplay.tsx
    │   │       │   │   ├── ModelDialog.test.tsx
    │   │       │   │   ├── ModelDialog.tsx
    │   │       │   │   ├── ModelQuotaDisplay.test.tsx
    │   │       │   │   ├── ModelQuotaDisplay.tsx
    │   │       │   │   ├── ModelStatsDisplay.test.tsx
    │   │       │   │   ├── ModelStatsDisplay.tsx
    │   │       │   │   ├── MultiFolderTrustDialog.test.tsx
    │   │       │   │   ├── MultiFolderTrustDialog.tsx
    │   │       │   │   ├── NewAgentsNotification.test.tsx
    │   │       │   │   ├── NewAgentsNotification.tsx
    │   │       │   │   ├── Notifications.test.tsx
    │   │       │   │   ├── Notifications.tsx
    │   │       │   │   ├── OverageMenuDialog.test.tsx
    │   │       │   │   ├── OverageMenuDialog.tsx
    │   │       │   │   ├── PermissionsModifyTrustDialog.test.tsx
    │   │       │   │   ├── PermissionsModifyTrustDialog.tsx
    │   │       │   │   ├── PolicyUpdateDialog.test.tsx
    │   │       │   │   ├── PolicyUpdateDialog.tsx
    │   │       │   │   ├── ProgressBar.test.tsx
    │   │       │   │   ├── ProgressBar.tsx
    │   │       │   │   ├── ProQuotaDialog.test.tsx
    │   │       │   │   ├── ProQuotaDialog.tsx
    │   │       │   │   ├── QueuedMessageDisplay.test.tsx
    │   │       │   │   ├── QueuedMessageDisplay.tsx
    │   │       │   │   ├── QuittingDisplay.test.tsx
    │   │       │   │   ├── QuittingDisplay.tsx
    │   │       │   │   ├── QuotaDisplay.test.tsx
    │   │       │   │   ├── QuotaDisplay.tsx
    │   │       │   │   ├── QuotaStatsInfo.tsx
    │   │       │   │   ├── RawMarkdownIndicator.test.tsx
    │   │       │   │   ├── RawMarkdownIndicator.tsx
    │   │       │   │   ├── RewindConfirmation.test.tsx
    │   │       │   │   ├── RewindConfirmation.tsx
    │   │       │   │   ├── RewindViewer.test.tsx
    │   │       │   │   ├── RewindViewer.tsx
    │   │       │   │   ├── SessionBrowser.test.tsx
    │   │       │   │   ├── SessionBrowser.tsx
    │   │       │   │   ├── SessionSummaryDisplay.test.tsx
    │   │       │   │   ├── SessionSummaryDisplay.tsx
    │   │       │   │   ├── SettingsDialog.test.tsx
    │   │       │   │   ├── SettingsDialog.tsx
    │   │       │   │   ├── ShellInputPrompt.test.tsx
    │   │       │   │   ├── ShellInputPrompt.tsx
    │   │       │   │   ├── ShellModeIndicator.test.tsx
    │   │       │   │   ├── ShellModeIndicator.tsx
    │   │       │   │   ├── ShortcutsHelp.test.tsx
    │   │       │   │   ├── ShortcutsHelp.tsx
    │   │       │   │   ├── ShowMoreLines.test.tsx
    │   │       │   │   ├── ShowMoreLines.tsx
    │   │       │   │   ├── ShowMoreLinesLayout.test.tsx
    │   │       │   │   ├── SkillInboxDialog.test.tsx
    │   │       │   │   ├── SkillInboxDialog.tsx
    │   │       │   │   ├── StatsDisplay.test.tsx
    │   │       │   │   ├── StatsDisplay.tsx
    │   │       │   │   ├── StatusDisplay.test.tsx
    │   │       │   │   ├── StatusDisplay.tsx
    │   │       │   │   ├── StatusRow.test.tsx
    │   │       │   │   ├── StatusRow.tsx
    │   │       │   │   ├── StickyHeader.test.tsx
    │   │       │   │   ├── StickyHeader.tsx
    │   │       │   │   ├── SuggestionsDisplay.test.tsx
    │   │       │   │   ├── SuggestionsDisplay.tsx
    │   │       │   │   ├── Table.test.tsx
    │   │       │   │   ├── Table.tsx
    │   │       │   │   ├── ThemedGradient.test.tsx
    │   │       │   │   ├── ThemedGradient.tsx
    │   │       │   │   ├── ThemeDialog.test.tsx
    │   │       │   │   ├── ThemeDialog.tsx
    │   │       │   │   ├── Tips.test.tsx
    │   │       │   │   ├── Tips.tsx
    │   │       │   │   ├── ToastDisplay.test.tsx
    │   │       │   │   ├── ToastDisplay.tsx
    │   │       │   │   ├── ToolConfirmationQueue.test.tsx
    │   │       │   │   ├── ToolConfirmationQueue.tsx
    │   │       │   │   ├── ToolStatsDisplay.test.tsx
    │   │       │   │   ├── ToolStatsDisplay.tsx
    │   │       │   │   ├── UpdateNotification.test.tsx
    │   │       │   │   ├── UpdateNotification.tsx
    │   │       │   │   ├── UserIdentity.test.tsx
    │   │       │   │   ├── UserIdentity.tsx
    │   │       │   │   ├── ValidationDialog.test.tsx
    │   │       │   │   ├── ValidationDialog.tsx
    │   │       │   │   ├── __snapshots__/
    │   │       │   │   │   ├── AdminSettingsChangedDialog.test.tsx.snap
    │   │       │   │   │   ├── AlternateBufferQuittingDisplay.test.tsx.snap
    │   │       │   │   │   ├── AppHeader.test.tsx.snap
    │   │       │   │   │   ├── AppHeaderIcon.test.tsx.snap
    │   │       │   │   │   ├── ApprovalModeIndicator.test.tsx.snap
    │   │       │   │   │   ├── AskUserDialog.test.tsx.snap
    │   │       │   │   │   ├── BackgroundTaskDisplay.test.tsx.snap
    │   │       │   │   │   ├── Banner.test.tsx.snap
    │   │       │   │   │   ├── Checklist.test.tsx.snap
    │   │       │   │   │   ├── ChecklistItem.test.tsx.snap
    │   │       │   │   │   ├── Composer.test.tsx.snap
    │   │       │   │   │   ├── ConfigInitDisplay.test.tsx.snap
    │   │       │   │   │   ├── ContextSummaryDisplay.test.tsx.snap
    │   │       │   │   │   ├── DetailedMessagesDisplay.test.tsx.snap
    │   │       │   │   │   ├── EditorSettingsDialog.test.tsx.snap
    │   │       │   │   │   ├── EmptyWalletDialog.test.tsx.snap
    │   │       │   │   │   ├── ExitPlanModeDialog.test.tsx.snap
    │   │       │   │   │   ├── Footer.test.tsx.snap
    │   │       │   │   │   ├── FooterConfigDialog.test.tsx.snap
    │   │       │   │   │   ├── HistoryItemDisplay.test.tsx.snap
    │   │       │   │   │   ├── HooksDialog.test.tsx.snap
    │   │       │   │   │   ├── HookStatusDisplay.test.tsx.snap
    │   │       │   │   │   ├── IDEContextDetailDisplay.test.tsx.snap
    │   │       │   │   │   ├── InputPrompt.test.tsx.snap
    │   │       │   │   │   ├── LoadingIndicator.test.tsx.snap
    │   │       │   │   │   ├── LoopDetectionConfirmation.test.tsx.snap
    │   │       │   │   │   ├── MainContent.test.tsx.snap
    │   │       │   │   │   ├── ModelQuotaDisplay.test.tsx.snap
    │   │       │   │   │   ├── ModelStatsDisplay.test.tsx.snap
    │   │       │   │   │   ├── NewAgentsNotification.test.tsx.snap
    │   │       │   │   │   ├── Notifications.test.tsx.snap
    │   │       │   │   │   ├── OverageMenuDialog.test.tsx.snap
    │   │       │   │   │   ├── PolicyUpdateDialog.test.tsx.snap
    │   │       │   │   │   ├── PrepareLabel.test.tsx.snap
    │   │       │   │   │   ├── ProgressBar.test.tsx.snap
    │   │       │   │   │   ├── QuotaDisplay.test.tsx.snap
    │   │       │   │   │   ├── RewindConfirmation.test.tsx.snap
    │   │       │   │   │   ├── RewindViewer.test.tsx.snap
    │   │       │   │   │   ├── SessionBrowser.test.tsx.snap
    │   │       │   │   │   ├── SessionSummaryDisplay.test.tsx.snap
    │   │       │   │   │   ├── SettingsDialog.test.tsx.snap
    │   │       │   │   │   ├── ShortcutsHelp.test.tsx.snap
    │   │       │   │   │   ├── StatsDisplay.test.tsx.snap
    │   │       │   │   │   ├── StatusDisplay.test.tsx.snap
    │   │       │   │   │   ├── SuggestionsDisplay.test.tsx.snap
    │   │       │   │   │   ├── Table.test.tsx.snap
    │   │       │   │   │   ├── ThemeDialog.test.tsx.snap
    │   │       │   │   │   ├── Tips.test.tsx.snap
    │   │       │   │   │   ├── ToastDisplay.test.tsx.snap
    │   │       │   │   │   ├── ToolConfirmationQueue.test.tsx.snap
    │   │       │   │   │   └── ToolStatsDisplay.test.tsx.snap
    │   │       │   │   ├── messages/
    │   │       │   │   │   ├── CompressionMessage.test.tsx
    │   │       │   │   │   ├── CompressionMessage.tsx
    │   │       │   │   │   ├── DenseToolMessage.test.tsx
    │   │       │   │   │   ├── DenseToolMessage.tsx
    │   │       │   │   │   ├── DiffRenderer.test.tsx
    │   │       │   │   │   ├── DiffRenderer.tsx
    │   │       │   │   │   ├── ErrorMessage.test.tsx
    │   │       │   │   │   ├── ErrorMessage.tsx
    │   │       │   │   │   ├── GeminiMessage.test.tsx
    │   │       │   │   │   ├── GeminiMessage.tsx
    │   │       │   │   │   ├── GeminiMessageContent.tsx
    │   │       │   │   │   ├── HintMessage.tsx
    │   │       │   │   │   ├── InfoMessage.test.tsx
    │   │       │   │   │   ├── InfoMessage.tsx
    │   │       │   │   │   ├── ModelMessage.tsx
    │   │       │   │   │   ├── RedirectionConfirmation.test.tsx
    │   │       │   │   │   ├── ShellToolMessage.test.tsx
    │   │       │   │   │   ├── ShellToolMessage.tsx
    │   │       │   │   │   ├── SubagentGroupDisplay.test.tsx
    │   │       │   │   │   ├── SubagentGroupDisplay.tsx
    │   │       │   │   │   ├── SubagentHistoryMessage.test.tsx
    │   │       │   │   │   ├── SubagentHistoryMessage.tsx
    │   │       │   │   │   ├── SubagentProgressDisplay.test.tsx
    │   │       │   │   │   ├── SubagentProgressDisplay.tsx
    │   │       │   │   │   ├── ThinkingMessage.test.tsx
    │   │       │   │   │   ├── ThinkingMessage.tsx
    │   │       │   │   │   ├── Todo.test.tsx
    │   │       │   │   │   ├── Todo.tsx
    │   │       │   │   │   ├── ToolConfirmationMessage.test.tsx
    │   │       │   │   │   ├── ToolConfirmationMessage.tsx
    │   │       │   │   │   ├── ToolGroupMessage.compact.test.tsx
    │   │       │   │   │   ├── ToolGroupMessage.test.tsx
    │   │       │   │   │   ├── ToolGroupMessage.tsx
    │   │       │   │   │   ├── ToolGroupMessageRegression.test.tsx
    │   │       │   │   │   ├── ToolMessage.test.tsx
    │   │       │   │   │   ├── ToolMessage.tsx
    │   │       │   │   │   ├── ToolMessageFocusHint.test.tsx
    │   │       │   │   │   ├── ToolMessageRawMarkdown.test.tsx
    │   │       │   │   │   ├── ToolOverflowConsistencyChecks.test.tsx
    │   │       │   │   │   ├── ToolResultDisplay.test.tsx
    │   │       │   │   │   ├── ToolResultDisplay.tsx
    │   │       │   │   │   ├── ToolResultDisplayOverflow.test.tsx
    │   │       │   │   │   ├── ToolShared.test.tsx
    │   │       │   │   │   ├── ToolShared.tsx
    │   │       │   │   │   ├── ToolStickyHeaderRegression.test.tsx
    │   │       │   │   │   ├── TopicMessage.test.tsx
    │   │       │   │   │   ├── TopicMessage.tsx
    │   │       │   │   │   ├── UserMessage.test.tsx
    │   │       │   │   │   ├── UserMessage.tsx
    │   │       │   │   │   ├── UserShellMessage.tsx
    │   │       │   │   │   ├── WarningMessage.test.tsx
    │   │       │   │   │   ├── WarningMessage.tsx
    │   │       │   │   │   └── __snapshots__/
    │   │       │   │   │       ├── DenseToolMessage.test.tsx.snap
    │   │       │   │   │       ├── DiffRenderer.test.tsx.snap
    │   │       │   │   │       ├── ErrorMessage.test.tsx.snap
    │   │       │   │   │       ├── GeminiMessage.test.tsx.snap
    │   │       │   │   │       ├── InfoMessage.test.tsx.snap
    │   │       │   │   │       ├── RedirectionConfirmation.test.tsx.snap
    │   │       │   │   │       ├── ShellToolMessage.test.tsx.snap
    │   │       │   │   │       ├── SubagentGroupDisplay.test.tsx.snap
    │   │       │   │   │       ├── SubagentHistoryMessage.test.tsx.snap
    │   │       │   │   │       ├── SubagentProgressDisplay.test.tsx.snap
    │   │       │   │   │       ├── ThinkingMessage.test.tsx.snap
    │   │       │   │   │       ├── Todo.test.tsx.snap
    │   │       │   │   │       ├── ToolConfirmationMessage.test.tsx.snap
    │   │       │   │   │       ├── ToolConfirmationMessageOverflow.test.tsx.snap
    │   │       │   │   │       ├── ToolGroupMessage.compact.test.tsx.snap
    │   │       │   │   │       ├── ToolGroupMessage.test.tsx.snap
    │   │       │   │   │       ├── ToolMessage.test.tsx.snap
    │   │       │   │   │       ├── ToolMessageFocusHint.test.tsx.snap
    │   │       │   │   │       ├── ToolMessageRawMarkdown.test.tsx.snap
    │   │       │   │   │       ├── ToolResultDisplay.test.tsx.snap
    │   │       │   │   │       ├── ToolShared.test.tsx.snap
    │   │       │   │   │       ├── ToolStickyHeaderRegression.test.tsx.snap
    │   │       │   │   │       ├── UserMessage.test.tsx.snap
    │   │       │   │   │       └── WarningMessage.test.tsx.snap
    │   │       │   │   ├── SessionBrowser/
    │   │       │   │   │   ├── SessionBrowserEmpty.tsx
    │   │       │   │   │   ├── SessionBrowserError.tsx
    │   │       │   │   │   ├── SessionBrowserLoading.tsx
    │   │       │   │   │   ├── SessionBrowserNav.tsx
    │   │       │   │   │   ├── SessionBrowserSearchNav.test.tsx
    │   │       │   │   │   ├── SessionBrowserStates.test.tsx
    │   │       │   │   │   ├── SessionListHeader.tsx
    │   │       │   │   │   ├── utils.test.ts
    │   │       │   │   │   ├── utils.ts
    │   │       │   │   │   └── __snapshots__/
    │   │       │   │   │       ├── SessionBrowserSearchNav.test.tsx.snap
    │   │       │   │   │       └── SessionBrowserStates.test.tsx.snap
    │   │       │   │   ├── shared/
    │   │       │   │   │   ├── BaseSelectionList.test.tsx
    │   │       │   │   │   ├── BaseSelectionList.tsx
    │   │       │   │   │   ├── BaseSettingsDialog.test.tsx
    │   │       │   │   │   ├── BaseSettingsDialog.tsx
    │   │       │   │   │   ├── DescriptiveRadioButtonSelect.test.tsx
    │   │       │   │   │   ├── DescriptiveRadioButtonSelect.tsx
    │   │       │   │   │   ├── DialogFooter.tsx
    │   │       │   │   │   ├── EnumSelector.test.tsx
    │   │       │   │   │   ├── EnumSelector.tsx
    │   │       │   │   │   ├── ExpandableText.test.tsx
    │   │       │   │   │   ├── ExpandableText.tsx
    │   │       │   │   │   ├── HalfLinePaddedBox.test.tsx
    │   │       │   │   │   ├── HalfLinePaddedBox.tsx
    │   │       │   │   │   ├── HorizontalLine.tsx
    │   │       │   │   │   ├── MaxSizedBox.test.tsx
    │   │       │   │   │   ├── MaxSizedBox.tsx
    │   │       │   │   │   ├── performance.test.ts
    │   │       │   │   │   ├── RadioButtonSelect.test.tsx
    │   │       │   │   │   ├── RadioButtonSelect.tsx
    │   │       │   │   │   ├── ScopeSelector.tsx
    │   │       │   │   │   ├── Scrollable.test.tsx
    │   │       │   │   │   ├── Scrollable.tsx
    │   │       │   │   │   ├── ScrollableList.test.tsx
    │   │       │   │   │   ├── ScrollableList.tsx
    │   │       │   │   │   ├── SearchableList.test.tsx
    │   │       │   │   │   ├── SearchableList.tsx
    │   │       │   │   │   ├── SectionHeader.test.tsx
    │   │       │   │   │   ├── SectionHeader.tsx
    │   │       │   │   │   ├── SlicingMaxSizedBox.test.tsx
    │   │       │   │   │   ├── SlicingMaxSizedBox.tsx
    │   │       │   │   │   ├── TabHeader.test.tsx
    │   │       │   │   │   ├── TabHeader.tsx
    │   │       │   │   │   ├── text-buffer.test.ts
    │   │       │   │   │   ├── text-buffer.ts
    │   │       │   │   │   ├── TextInput.test.tsx
    │   │       │   │   │   ├── TextInput.tsx
    │   │       │   │   │   ├── vim-buffer-actions.test.ts
    │   │       │   │   │   ├── vim-buffer-actions.ts
    │   │       │   │   │   ├── VirtualizedList.test.tsx
    │   │       │   │   │   ├── VirtualizedList.tsx
    │   │       │   │   │   └── __snapshots__/
    │   │       │   │   │       ├── BaseSelectionList.test.tsx.snap
    │   │       │   │   │       ├── DescriptiveRadioButtonSelect.test.tsx.snap
    │   │       │   │   │       ├── EnumSelector.test.tsx.snap
    │   │       │   │   │       ├── ExpandablePrompt.test.tsx.snap
    │   │       │   │   │       ├── ExpandableText.test.tsx.snap
    │   │       │   │   │       ├── HalfLinePaddedBox.test.tsx.snap
    │   │       │   │   │       ├── MaxSizedBox.test.tsx.snap
    │   │       │   │   │       ├── Scrollable.test.tsx.snap
    │   │       │   │   │       ├── SearchableList.test.tsx.snap
    │   │       │   │   │       ├── SectionHeader.test.tsx.snap
    │   │       │   │   │       ├── TabHeader.test.tsx.snap
    │   │       │   │   │       └── VirtualizedList.test.tsx.snap
    │   │       │   │   ├── triage/
    │   │       │   │   │   ├── TriageDuplicates.tsx
    │   │       │   │   │   └── TriageIssues.tsx
    │   │       │   │   └── views/
    │   │       │   │       ├── AgentsStatus.tsx
    │   │       │   │       ├── ChatList.test.tsx
    │   │       │   │       ├── ChatList.tsx
    │   │       │   │       ├── ExtensionDetails.test.tsx
    │   │       │   │       ├── ExtensionDetails.tsx
    │   │       │   │       ├── ExtensionRegistryView.test.tsx
    │   │       │   │       ├── ExtensionRegistryView.tsx
    │   │       │   │       ├── ExtensionsList.test.tsx
    │   │       │   │       ├── ExtensionsList.tsx
    │   │       │   │       ├── McpStatus.test.tsx
    │   │       │   │       ├── McpStatus.tsx
    │   │       │   │       ├── SkillsList.test.tsx
    │   │       │   │       ├── SkillsList.tsx
    │   │       │   │       ├── ToolsList.test.tsx
    │   │       │   │       ├── ToolsList.tsx
    │   │       │   │       └── __snapshots__/
    │   │       │   │           ├── ChatList.test.tsx.snap
    │   │       │   │           ├── McpStatus.test.tsx.snap
    │   │       │   │           └── ToolsList.test.tsx.snap
    │   │       │   ├── constants/
    │   │       │   │   ├── tips.ts
    │   │       │   │   └── wittyPhrases.ts
    │   │       │   ├── contexts/
    │   │       │   │   ├── AppContext.tsx
    │   │       │   │   ├── AskUserActionsContext.tsx
    │   │       │   │   ├── ConfigContext.tsx
    │   │       │   │   ├── InputContext.tsx
    │   │       │   │   ├── KeypressContext.test.tsx
    │   │       │   │   ├── KeypressContext.tsx
    │   │       │   │   ├── MouseContext.test.tsx
    │   │       │   │   ├── MouseContext.tsx
    │   │       │   │   ├── OverflowContext.tsx
    │   │       │   │   ├── QuotaContext.tsx
    │   │       │   │   ├── ScrollProvider.drag.test.tsx
    │   │       │   │   ├── ScrollProvider.test.tsx
    │   │       │   │   ├── ScrollProvider.tsx
    │   │       │   │   ├── SessionContext.test.tsx
    │   │       │   │   ├── SessionContext.tsx
    │   │       │   │   ├── SettingsContext.test.tsx
    │   │       │   │   ├── SettingsContext.tsx
    │   │       │   │   ├── ShellFocusContext.tsx
    │   │       │   │   ├── StreamingContext.tsx
    │   │       │   │   ├── TerminalContext.test.tsx
    │   │       │   │   ├── TerminalContext.tsx
    │   │       │   │   ├── ToolActionsContext.test.tsx
    │   │       │   │   ├── ToolActionsContext.tsx
    │   │       │   │   ├── UIActionsContext.tsx
    │   │       │   │   ├── UIStateContext.tsx
    │   │       │   │   └── VimModeContext.tsx
    │   │       │   ├── editors/
    │   │       │   │   └── editorSettingsManager.ts
    │   │       │   ├── hooks/
    │   │       │   │   ├── atCommandProcessor.test.ts
    │   │       │   │   ├── atCommandProcessor.ts
    │   │       │   │   ├── atCommandProcessor_agents.test.ts
    │   │       │   │   ├── creditsFlowHandler.test.ts
    │   │       │   │   ├── creditsFlowHandler.ts
    │   │       │   │   ├── shellReducer.test.ts
    │   │       │   │   ├── shellReducer.ts
    │   │       │   │   ├── slashCommandProcessor.test.tsx
    │   │       │   │   ├── slashCommandProcessor.ts
    │   │       │   │   ├── toolMapping.test.ts
    │   │       │   │   ├── toolMapping.ts
    │   │       │   │   ├── useAgentStream.test.tsx
    │   │       │   │   ├── useAgentStream.ts
    │   │       │   │   ├── useAlternateBuffer.test.ts
    │   │       │   │   ├── useAlternateBuffer.ts
    │   │       │   │   ├── useAnimatedScrollbar.test.tsx
    │   │       │   │   ├── useAnimatedScrollbar.ts
    │   │       │   │   ├── useApprovalModeIndicator.test.ts
    │   │       │   │   ├── useApprovalModeIndicator.ts
    │   │       │   │   ├── useAtCompletion.test.ts
    │   │       │   │   ├── useAtCompletion.ts
    │   │       │   │   ├── useAtCompletion_agents.test.ts
    │   │       │   │   ├── useBackgroundTaskManager.test.tsx
    │   │       │   │   ├── useBackgroundTaskManager.ts
    │   │       │   │   ├── useBanner.test.ts
    │   │       │   │   ├── useBanner.ts
    │   │       │   │   ├── useBatchedScroll.test.ts
    │   │       │   │   ├── useBatchedScroll.ts
    │   │       │   │   ├── useCommandCompletion.test.tsx
    │   │       │   │   ├── useCommandCompletion.tsx
    │   │       │   │   ├── useCompletion.ts
    │   │       │   │   ├── useComposerStatus.ts
    │   │       │   │   ├── useConfirmingTool.ts
    │   │       │   │   ├── useConsoleMessages.test.tsx
    │   │       │   │   ├── useConsoleMessages.ts
    │   │       │   │   ├── useEditorSettings.test.tsx
    │   │       │   │   ├── useEditorSettings.ts
    │   │       │   │   ├── useExecutionLifecycle.test.tsx
    │   │       │   │   ├── useExecutionLifecycle.ts
    │   │       │   │   ├── useExtensionRegistry.ts
    │   │       │   │   ├── useExtensionUpdates.test.tsx
    │   │       │   │   ├── useExtensionUpdates.ts
    │   │       │   │   ├── useFlickerDetector.test.ts
    │   │       │   │   ├── useFlickerDetector.ts
    │   │       │   │   ├── useFocus.test.tsx
    │   │       │   │   ├── useFocus.ts
    │   │       │   │   ├── useFolderTrust.test.ts
    │   │       │   │   ├── useFolderTrust.ts
    │   │       │   │   ├── useGeminiStream.test.tsx
    │   │       │   │   ├── useGeminiStream.ts
    │   │       │   │   ├── useGitBranchName.test.tsx
    │   │       │   │   ├── useGitBranchName.ts
    │   │       │   │   ├── useHistoryManager.test.ts
    │   │       │   │   ├── useHistoryManager.ts
    │   │       │   │   ├── useHookDisplayState.test.ts
    │   │       │   │   ├── useHookDisplayState.ts
    │   │       │   │   ├── useIdeTrustListener.test.tsx
    │   │       │   │   ├── useIdeTrustListener.ts
    │   │       │   │   ├── useInactivityTimer.ts
    │   │       │   │   ├── useIncludeDirsTrust.test.tsx
    │   │       │   │   ├── useIncludeDirsTrust.tsx
    │   │       │   │   ├── useInlineEditBuffer.test.ts
    │   │       │   │   ├── useInlineEditBuffer.ts
    │   │       │   │   ├── useInputHistory.test.ts
    │   │       │   │   ├── useInputHistory.ts
    │   │       │   │   ├── useInputHistoryStore.test.ts
    │   │       │   │   ├── useInputHistoryStore.ts
    │   │       │   │   ├── useKeyMatchers.tsx
    │   │       │   │   ├── useKeypress.test.tsx
    │   │       │   │   ├── useKeypress.ts
    │   │       │   │   ├── useKittyKeyboardProtocol.ts
    │   │       │   │   ├── useLoadingIndicator.test.tsx
    │   │       │   │   ├── useLoadingIndicator.ts
    │   │       │   │   ├── useLogger.test.tsx
    │   │       │   │   ├── useLogger.ts
    │   │       │   │   ├── useMcpStatus.test.tsx
    │   │       │   │   ├── useMcpStatus.ts
    │   │       │   │   ├── useMemoryMonitor.test.tsx
    │   │       │   │   ├── useMemoryMonitor.ts
    │   │       │   │   ├── useMessageQueue.test.tsx
    │   │       │   │   ├── useMessageQueue.ts
    │   │       │   │   ├── useModelCommand.test.tsx
    │   │       │   │   ├── useModelCommand.ts
    │   │       │   │   ├── useMouse.test.ts
    │   │       │   │   ├── useMouse.ts
    │   │       │   │   ├── useMouseClick.test.ts
    │   │       │   │   ├── useMouseClick.ts
    │   │       │   │   ├── usePermissionsModifyTrust.test.ts
    │   │       │   │   ├── usePermissionsModifyTrust.ts
    │   │       │   │   ├── usePhraseCycler.test.tsx
    │   │       │   │   ├── usePhraseCycler.ts
    │   │       │   │   ├── usePrivacySettings.test.tsx
    │   │       │   │   ├── usePrivacySettings.ts
    │   │       │   │   ├── usePromptCompletion.ts
    │   │       │   │   ├── useQuotaAndFallback.test.ts
    │   │       │   │   ├── useQuotaAndFallback.ts
    │   │       │   │   ├── useRegistrySearch.ts
    │   │       │   │   ├── useRepeatedKeyPress.ts
    │   │       │   │   ├── useReverseSearchCompletion.test.tsx
    │   │       │   │   ├── useReverseSearchCompletion.tsx
    │   │       │   │   ├── useRewind.test.ts
    │   │       │   │   ├── useRewind.ts
    │   │       │   │   ├── useRunEventNotifications.ts
    │   │       │   │   ├── useSearchBuffer.ts
    │   │       │   │   ├── useSelectionList.test.tsx
    │   │       │   │   ├── useSelectionList.ts
    │   │       │   │   ├── useSessionBrowser.test.ts
    │   │       │   │   ├── useSessionBrowser.ts
    │   │       │   │   ├── useSessionResume.test.ts
    │   │       │   │   ├── useSessionResume.ts
    │   │       │   │   ├── useSettingsCommand.ts
    │   │       │   │   ├── useSettingsNavigation.test.ts
    │   │       │   │   ├── useSettingsNavigation.ts
    │   │       │   │   ├── useShellCompletion.test.ts
    │   │       │   │   ├── useShellCompletion.ts
    │   │       │   │   ├── useShellHistory.test.ts
    │   │       │   │   ├── useShellHistory.ts
    │   │       │   │   ├── useShellInactivityStatus.test.ts
    │   │       │   │   ├── useShellInactivityStatus.ts
    │   │       │   │   ├── useSlashCompletion.test.ts
    │   │       │   │   ├── useSlashCompletion.ts
    │   │       │   │   ├── useSnowfall.test.tsx
    │   │       │   │   ├── useSnowfall.ts
    │   │       │   │   ├── useStateAndRef.ts
    │   │       │   │   ├── useSuspend.test.ts
    │   │       │   │   ├── useSuspend.ts
    │   │       │   │   ├── useTabbedNavigation.test.ts
    │   │       │   │   ├── useTabbedNavigation.ts
    │   │       │   │   ├── useTerminalSize.ts
    │   │       │   │   ├── useTerminalTheme.test.tsx
    │   │       │   │   ├── useTerminalTheme.ts
    │   │       │   │   ├── useThemeCommand.ts
    │   │       │   │   ├── useTimedMessage.ts
    │   │       │   │   ├── useTimer.test.tsx
    │   │       │   │   ├── useTimer.ts
    │   │       │   │   ├── useTips.test.ts
    │   │       │   │   ├── useTips.ts
    │   │       │   │   ├── useToolScheduler.test.ts
    │   │       │   │   ├── useToolScheduler.ts
    │   │       │   │   ├── useTurnActivityMonitor.test.ts
    │   │       │   │   ├── useTurnActivityMonitor.ts
    │   │       │   │   ├── useVisibilityToggle.ts
    │   │       │   │   ├── vim-passthrough.test.tsx
    │   │       │   │   ├── vim.test.tsx
    │   │       │   │   ├── vim.ts
    │   │       │   │   └── shell-completions/
    │   │       │   │       ├── gitProvider.test.ts
    │   │       │   │       ├── gitProvider.ts
    │   │       │   │       ├── index.ts
    │   │       │   │       ├── npmProvider.test.ts
    │   │       │   │       ├── npmProvider.ts
    │   │       │   │       └── types.ts
    │   │       │   ├── key/
    │   │       │   │   ├── keyBindings.test.ts
    │   │       │   │   ├── keyBindings.ts
    │   │       │   │   ├── keybindingUtils.test.ts
    │   │       │   │   ├── keybindingUtils.ts
    │   │       │   │   ├── keyMatchers.test.ts
    │   │       │   │   ├── keyMatchers.ts
    │   │       │   │   └── keyToAnsi.ts
    │   │       │   ├── layouts/
    │   │       │   │   ├── DefaultAppLayout.test.tsx
    │   │       │   │   ├── DefaultAppLayout.tsx
    │   │       │   │   ├── ScreenReaderAppLayout.tsx
    │   │       │   │   └── __snapshots__/
    │   │       │   │       └── DefaultAppLayout.test.tsx.snap
    │   │       │   ├── noninteractive/
    │   │       │   │   └── nonInteractiveUi.ts
    │   │       │   ├── privacy/
    │   │       │   │   ├── CloudFreePrivacyNotice.test.tsx
    │   │       │   │   ├── CloudFreePrivacyNotice.tsx
    │   │       │   │   ├── CloudPaidPrivacyNotice.test.tsx
    │   │       │   │   ├── CloudPaidPrivacyNotice.tsx
    │   │       │   │   ├── GeminiPrivacyNotice.test.tsx
    │   │       │   │   ├── GeminiPrivacyNotice.tsx
    │   │       │   │   ├── PrivacyNotice.test.tsx
    │   │       │   │   └── PrivacyNotice.tsx
    │   │       │   ├── state/
    │   │       │   │   ├── extensions.test.ts
    │   │       │   │   └── extensions.ts
    │   │       │   ├── themes/
    │   │       │   │   ├── color-utils.test.ts
    │   │       │   │   ├── color-utils.ts
    │   │       │   │   ├── semantic-tokens.ts
    │   │       │   │   ├── theme-manager.test.ts
    │   │       │   │   ├── theme-manager.ts
    │   │       │   │   ├── theme.test.ts
    │   │       │   │   ├── theme.ts
    │   │       │   │   └── builtin/
    │   │       │   │       ├── no-color.ts
    │   │       │   │       ├── dark/
    │   │       │   │       │   ├── ansi-dark.ts
    │   │       │   │       │   ├── atom-one-dark.ts
    │   │       │   │       │   ├── ayu-dark.ts
    │   │       │   │       │   ├── default-dark.ts
    │   │       │   │       │   ├── dracula-dark.ts
    │   │       │   │       │   ├── github-dark-colorblind.ts
    │   │       │   │       │   ├── github-dark.ts
    │   │       │   │       │   ├── holiday-dark.ts
    │   │       │   │       │   ├── shades-of-purple-dark.ts
    │   │       │   │       │   ├── solarized-dark.ts
    │   │       │   │       │   └── tokyonight-dark.ts
    │   │       │   │       └── light/
    │   │       │   │           ├── ansi-light.ts
    │   │       │   │           ├── ayu-light.ts
    │   │       │   │           ├── default-light.ts
    │   │       │   │           ├── github-light-colorblind.ts
    │   │       │   │           ├── github-light.ts
    │   │       │   │           ├── googlecode-light.ts
    │   │       │   │           ├── solarized-light.ts
    │   │       │   │           └── xcode-light.ts
    │   │       │   └── utils/
    │   │       │       ├── borderStyles.test.tsx
    │   │       │       ├── borderStyles.ts
    │   │       │       ├── clipboardUtils.test.ts
    │   │       │       ├── clipboardUtils.ts
    │   │       │       ├── clipboardUtils.windows.test.ts
    │   │       │       ├── CodeColorizer.test.tsx
    │   │       │       ├── CodeColorizer.tsx
    │   │       │       ├── commandUtils.test.ts
    │   │       │       ├── commandUtils.ts
    │   │       │       ├── computeStats.test.ts
    │   │       │       ├── computeStats.ts
    │   │       │       ├── confirmingTool.ts
    │   │       │       ├── ConsolePatcher.test.ts
    │   │       │       ├── ConsolePatcher.ts
    │   │       │       ├── contextUsage.ts
    │   │       │       ├── directoryUtils.test.ts
    │   │       │       ├── directoryUtils.ts
    │   │       │       ├── displayUtils.test.ts
    │   │       │       ├── displayUtils.ts
    │   │       │       ├── editorUtils.ts
    │   │       │       ├── fileUtils.ts
    │   │       │       ├── formatters.test.ts
    │   │       │       ├── formatters.ts
    │   │       │       ├── highlight.test.ts
    │   │       │       ├── highlight.ts
    │   │       │       ├── historyExportUtils.ts
    │   │       │       ├── historyUtils.ts
    │   │       │       ├── InlineMarkdownRenderer.tsx
    │   │       │       ├── inlineThinkingMode.ts
    │   │       │       ├── input.test.ts
    │   │       │       ├── input.ts
    │   │       │       ├── isNarrowWidth.ts
    │   │       │       ├── MarkdownDisplay.test.tsx
    │   │       │       ├── MarkdownDisplay.tsx
    │   │       │       ├── markdownParsingUtils.test.ts
    │   │       │       ├── markdownParsingUtils.ts
    │   │       │       ├── markdownUtilities.test.ts
    │   │       │       ├── markdownUtilities.ts
    │   │       │       ├── mouse.test.ts
    │   │       │       ├── mouse.ts
    │   │       │       ├── pendingAttentionNotification.test.ts
    │   │       │       ├── pendingAttentionNotification.ts
    │   │       │       ├── rewindFileOps.test.ts
    │   │       │       ├── rewindFileOps.ts
    │   │       │       ├── shortcutsHelp.ts
    │   │       │       ├── TableRenderer.test.tsx
    │   │       │       ├── TableRenderer.tsx
    │   │       │       ├── terminalCapabilityManager.test.ts
    │   │       │       ├── ter

[... Content truncated due to length ...]
```

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="introducing-chatgpt-agent-bridging-research-and-action.md">
<details>
<summary>Introducing ChatGPT agent: bridging research and action</summary>

Phase: [EXPLOITATION]

# Introducing ChatGPT agent: bridging research and action

**Source URL:** <https://openai.com/index/introducing-chatgpt-agent/>

July 17, 2025
[Product](https://openai.com/news/product-releases/) [Release](https://openai.com/research/index/release/)

# Introducing ChatGPT agent: bridging research and action

ChatGPT now thinks and acts, proactively choosing from a toolbox of agentic skills to complete tasks for you using its own computer.

ChatGPT can now do work for you using its own computer, handling complex tasks from start to finish.

You can now ask ChatGPT to handle requests like “look at my calendar and brief me on upcoming client meetings based on recent news,” “plan and buy ingredients to make Japanese breakfast for four,” and “analyze three competitors and create a slide deck.” ChatGPT will intelligently navigate websites, filter results, prompt you to log in securely when needed, run code, conduct analysis, and even deliver editable slideshows and spreadsheets that summarize its findings.

At the core of this new capability is a unified agentic system. It brings together three strengths of earlier breakthroughs: [Operator’s⁠](https://openai.com/index/introducing-operator/) ability to interact with websites, [deep research’s⁠](https://openai.com/index/introducing-deep-research/) skill in synthesizing information, and ChatGPT’s intelligence and conversational fluency.

ChatGPT carries out these tasks using its own virtual computer, fluidly shifting between reasoning and action to handle complex workflows from start to finish, all based on your instructions.

Most importantly, you’re always in control. ChatGPT requests permission before taking actions of consequence, and you can easily interrupt, take over the browser, or stop tasks at any point.

Starting today, Pro, Plus, and Team users can activate ChatGPT’s new agentic capabilities directly through the tools dropdown from the composer by selecting ‘agent mode’ at any point in any conversation.

While ChatGPT agent is already a powerful tool for handling complex tasks, today’s launch is just the beginning. We’ll continue to iteratively add significant improvements regularly, making it more capable and useful to more people over time.

## A natural evolution of Operator and deep research

Previously, Operator and deep research each brought unique strengths: Operator could scroll, click, and type on the web, while deep research excelled at analyzing and summarizing information. But they worked best in different situations: Operator couldn’t dive deep into analysis or write detailed reports, and deep research couldn’t interact with websites to refine results or access content requiring user authentication. In fact, we saw that many queries users attempted with Operator were actually better suited for deep research, so we brought the best of both together.

By integrating these complementary strengths in ChatGPT and introducing additional tools, we’ve unlocked entirely new capabilities within one model. It can now actively engage websites—clicking, filtering, and gathering more precise, efficient results. You can also naturally transition from a simple conversation to requesting actions directly within the same chat.

## An agent that works for you, with you

We’ve equipped ChatGPT agent with a suite of tools: a visual browser that interacts with the web through a graphical-user interface, a text-based browser for simpler reasoning-based web queries, a terminal, and direct API access.The agent can also leverage [ChatGPT connectors⁠(opens in a new window)](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt), which allows you to connect apps like Gmail and Github so ChatGPT can find information relevant to your prompts and use them in its responses. You can also log in on any website by taking over the browser, allowing it to go deeper and broader in both its research and task execution. Giving ChatGPT these different avenues for accessing and interacting with web information means it can choose the optimal path to most efficiently perform tasks. For instance, it can gather information about your calendar through an API, efficiently reason over large amounts of text using the text-based browser, while also having the ability to interact visually with websites designed primarily for humans.

All this is done using its own virtual computer, which preserves the context necessary for the task, even when multiple tools are used—the model can choose to open a page using the text browser or visual browser, download a file from the web, manipulate it by running a command in the terminal, and then view the output back in the visual browser. The model adapts its approach to carry out tasks with speed, accuracy, and efficiency.

ChatGPT agent is designed for iterative, collaborative workflows, far more interactive and flexible than previous models. As ChatGPT works, you can interrupt at any point to clarify your instructions, steer it toward desired outcomes, or change the task entirely. It will pick up where it left off, now with the new information, but without losing previous progress. Likewise, ChatGPT itself may proactively seek additional details from you when needed to ensure the task remains aligned with your goals. If a task takes longer than anticipated or feels stuck, you can pause it, ask it for a progress summary, or stop it entirely and receive partial results. If you have the ChatGPT app on your phone, it will send you a notification when it’s done with your task.

## Broadening real-world utility

These unified agentic capabilities significantly enhance ChatGPT’s usefulness in both everyday and professional contexts. At work, you can automate repetitive tasks, like converting screenshots or dashboards into presentations composed of editable vector elements, rearranging meetings, planning and booking offsites, and updating spreadsheets with new financial data while retaining the same formatting. In your personal life, you can use it to effortlessly plan and book travel itineraries, design and book entire dinner parties, or find specialists and schedule appointments.

The model’s elevated capabilities are reflected in its state-of-the-art (SOTA) performance on evaluations measuring web browsing and real-world task completion capabilities.

On [**Humanity’s Last Exam** ⁠(opens in a new window)](https://agi.safe.ai/)\*, an evaluation that measures AI’s performance across a broad range of subjects on expert-level questions, the model powering ChatGPT agent scores a new pass@1 SOTA at 41.6. Because the agent plans dynamically and chooses its own tools, it can tackle the same task in different ways across runs. When we scaled this with a simple parallel rollout strategy—running up to eight attempts at once and picking the one with the highest self-reported confidence—the agent’s HLE score increases to 44.4.

**FrontierMath\*\*** is the hardest known math benchmark, featuring novel, unpublished problems that often take expert mathematicians hours or even days to solve. With tool use, like access to a terminal for code execution, ChatGPT agent reaches 27.4% accuracy, outperforming both previous models by a wide margin.

We also assessed the model using benchmarks modeled after complex real-world tasks. On an internal benchmark designed to evaluate model performance on **complex, economically valuable knowledge-work tasks**, ChatGPT agent's output is comparable to or better than that of humans in roughly half the cases across a range of task completion times, while significantly outperforming o3 and o4-mini. Model outputs are judged by experts against high-quality human baselines created by top performers in each field. These tasks, sourced from experts across diverse occupations and industries, mirror real-world professional work—such as preparing a competitive analysis of on-demand urgent care providers, building detailed amortization schedules, and identifying viable water wells for a new green hydrogen facility.

On [**DSBench** ⁠(opens in a new window)](https://arxiv.org/abs/2409.07703) **,** designed to evaluate agents on realistic data science tasks spanning data analysis and modeling, ChatGPT agent notably surpasses human performance by a significant margin.

On **SpreadsheetBench**, which evaluates models on their ability to edit spreadsheets derived from real-world scenarios, ChatGPT agent outperforms existing models by a significant margin. When given the ability to edit spreadsheets directly, ChatGPT agent scores even higher with 45.5%, compared to Copilot in Excel’s 20.0%.

Methodology: The SpreadsheetBench authors used a Windows environment using Microsoft Excel to evaluate spreadsheets. We used an OSX environment and LibreOffice, which may result in small grading differences. For example, the authors found an Overall Hard restriction of 15.02% for GPT‑4o, and we obtained 13.38%. We used the complete 912-question benchmark.

On an internal benchmark which measures a model's ability to take on first to third-year **investment banking analyst modeling tasks**—like putting together a three-statement financial model for a Fortune 500 company with proper formatting and citations, or building a leveraged buyout model for a take-private—the model powering ChatGPT agent significantly outperforms deep research and o3. Each task is graded on hundreds of criteria related to correctness and formula use.

We also evaluated ChatGPT agent on [**BrowseComp** ⁠](https://openai.com/index/browsecomp/), a benchmark we published earlier this year that measures browsing agents’ ability to locate hard-to-find information on the web. The model set a new SOTA with 68.9%, 17.4 percentage points higher than deep research.

Finally, on [WebArena⁠(opens in a new window)](https://webarena.dev/), a benchmark designed to evaluate the performance of web-browsing agents in completing real-world web tasks, the model improves over o3‑powered CUA (the model powering Operator).

## How to use

You can activate ChatGPT’s new agentic capabilities directly through the tools dropdown from the composer by selecting ‘agent mode’ at any point in any conversation. Simply describe your desired task—whether it’s conducting deep research, creating a slideshow, or submitting expenses. As it performs your task, an on-screen narration provides visibility into exactly what ChatGPT is doing. You can interrupt and take control of the browser whenever needed, ensuring tasks remain aligned with your goals.

ChatGPT agent can access your connectors, allowing it to integrate with your workflows and access relevant, actionable information. Once authenticated, these connectors allow ChatGPT to see information and do things like summarize your inbox for the day or find time slots you’re available for a meeting—to take action on these sites, however, you’ll still be prompted to log in by taking over the browser.

Additionally, you can schedule completed tasks to recur automatically, such as generating a weekly metrics report every Monday morning.

## Novel capabilities, novel risks

This release marks the first time users can ask ChatGPT to take actions on the web. This introduces new risks, particularly because ChatGPT agent can work directly with your data, whether it’s information accessed through connectors or websites that you have logged it into via takeover mode. We’ve strengthened the robust controls from Operator’s research preview and added safeguards for challenges such as handling sensitive information on the live web, broader user reach, and (limited) terminal network access. While these mitigations significantly reduce risk, ChatGPT agent’s expanded tools and broader user reach mean its overall risk profile is higher.

We’ve placed a particular emphasis on safeguarding ChatGPT agent against **adversarial manipulation through prompt injection**, which is a risk for agentic systems generally, and have prepared more extensive mitigations accordingly. Prompt injections are attempts by third parties to manipulate its behavior through malicious instructions that ChatGPT agent may encounter on the web while completing a task. For example, a malicious prompt hidden in a webpage, such as in invisible elements or metadata, could trick the agent into taking unintended actions, like sharing private data from a connector with the attacker, or taking a harmful action on a site the user has logged into. Because ChatGPT agent can take direct actions, successful attacks can have greater impact and pose higher risks.

We’ve trained and tested the agent on identifying and resisting prompt injections, in addition to using monitoring to rapidly detect and respond to prompt injection attacks. Requiring explicit user confirmation before consequential actions further reduces the risk of harm from these attacks, and users can intervene in tasks as needed by taking over or pausing. Users should weigh these tradeoffs when deciding what information to provide to the agent, as well as take steps to minimize their exposure to these risks, such as disabling connectors when they aren’t needed for a task.

We’ve also implemented mitigations around **model mistakes,** especially since the model can now perform tasks that impact the real world:

-   **Explicit user confirmation:** ChatGPT is trained to explicitly ask for your permission before taking actions with real-world consequences, like making a purchase.
-   **Active supervision (“Watch Mode”):** Certain critical tasks, like sending emails, require your active oversight.
-   **Proactive risk mitigation:** ChatGPT is trained to actively refuse high-risk tasks such as bank transfers.

Finally, we’ve introduced additional controls to **limit the data** the model has access to:

-   **Privacy controls:** With a single click in ChatGPT’s settings, you can delete all browsing data and immediately log out of all active website sessions. Otherwise, cookies persist based on each visited website’s cookie policies, which can make repeat visits to sites more efficient.
-   **Secure browser takeover mode:** When you interact with the web using ChatGPT’s browser (“takeover mode”), your inputs remain private. ChatGPT does not collect or store any data you enter during these sessions, such as passwords, because the model doesn’t need it, and it’s safer if it never sees it.

## Our strongest safety stack yet for biological risk

With the model’s increased capabilities, we’ve made the decision to treat ChatGPT agent as High Biological and Chemical capabilities under our [Preparedness Framework⁠](https://openai.com/index/updating-our-preparedness-framework/), activating the associated safeguards. While we don’t have definitive evidence that the model could meaningfully help a novice create severe biological harm—our threshold for High capability—we are exercising caution and implementing the needed safeguards now. As a result, this model has our most comprehensive safety stack to date with enhanced safeguards for biology: comprehensive threat modeling, dual-use refusal training, always-on classifiers and reasoning monitors, and clear enforcement pipelines.

In addition to our work to secure ChatGPT agent, we know that layered biosafety works best when safeguards extend beyond any one lab, so we collaborate across the ecosystem to strengthen defenses. From day one we’ve worked with outside biosecurity experts, safety institutes, and academic researchers to shape our threat model, assessments, and policies. Biology‑trained reviewers validated our evaluation data, and domain‑expert red teamers have stress‑tested safeguards in realistic scenarios. Earlier this month we convened a Biodefense workshop with experts from government, academia, national labs, and NGOs to accelerate collaboration and advance biodefense research powered by AI. We’ll keep partnering globally to stay ahead of emerging risks.

Read more about our robust safety approach for the unified agentic model in the [system card⁠](https://openai.com/index/chatgpt-agent-system-card/). We are also launching a [bug bounty program⁠](https://openai.com/bio-bug-bounty/) so that we can find and remediate real-world risks.

## Availability

ChatGPT agent starts rolling out today to Pro, Plus, and Team; Pro will get access by the end of day, while Plus and Team users will get access over the next few days. Enterprise and Education users will get access in the coming weeks. Pro users have 400 messages per month, while other paid users get 40 messages monthly, with additional usage available via flexible credit-based options.

We are still working on enabling access for the European Economic Area and Switzerland.

The Operator research preview site will remain functional for a few more weeks, after which it will be sunset. Deep research is a part of ChatGPT agent’s capabilities. If you prefer the original deep research feature—which may take longer to run but provides more detailed, in-depth responses by default—you can still access it by selecting “deep research” from the dropdown in the message composer.

## Limitations and looking ahead

ChatGPT agent is still in its early stages. It’s capable of taking on a range of complex tasks, but it can still make mistakes.

While we see significant potential in its ability to generate slideshows, this functionality is currently in beta. At the moment, outputs can sometimes feel rudimentary in its formatting and polish, particularly when starting without an existing document. We focused the model’s initial capabilities on generating artifacts that organize information in a flow and format suitable for presentations, with elements like text, charts, images, and shapes that are natively and easily editable after export, optimizing for structure and flexibility. Currently, there are also occasional discrepancies between the slides in the viewer and the exported powerpoint that we are working to reduce. Additionally, while you can currently upload an existing spreadsheet for ChatGPT to edit or use as a template, this capability isn't yet available for slideshows. We’re already training the next iteration of ChatGPT's slideshow creation to produce more polished, sophisticated outputs, with broader capabilities and improved formatting.

Overall, we expect continued improvements to ChatGPT agent’s efficiency, depth, and versatility over time, including more seamless interactions as we continue to adjust the amount of oversight required from the user to make it more useful while ensuring it’s safe to use.

## Appendix

|     |     |     |     |     |
| --- | --- | --- | --- | --- |
| **SpreadsheetBench** |  |  |  |  |
| **Model** | **Evaluation environment** | **Soft restriction (%): Cell-level** | **Soft restriction (%): Sheet-level** | **Soft restriction (%): Overall** |
| GPT-4o | Windows, Excel | 15.03 | 23.65 | 18.35 |
| Copilot in Excel | Windows, Excel | 23.33 | 15.00 | 20.00 |
| GPT-4o | OSX, LibreOffice | 15.86 | 18.33 | 16.81 |
| OpenAI o3 | OSX, LibreOffice | 22.40 | 24.60 | 23.25 |
| ChatGPT agent | OSX, LibreOffice | 38.27 | 30.48 | **35.27** |
| ChatGPT agent with .xlsx | OSX, LibreOffice | 50.56 | 37.51 | **45.54** |
| Human |  | 75.56 | 65.00 | **71.33** |

## Footnotes

\* When enabling browsing, the model can sometimes find exact answers online, for example, by reading blog posts with sample problems from a dataset. We mitigate concerns of the model cheating while browsing with two strategies:

1.  Blocked domains that we have observed the model cheating from in the past.

2.  Used an extra model as a monitor to examine all tool output tokens in each attempt to identify suspicious behavior. Suspicious behavior is defined as "a page, file, or snippet whose main purpose is to provide the exact answer to this specific question—e.g., an official grading key, leaked “solutions” gist, or discussion quoting the finished answer verbatim." Benign behavior is defined as "Any authoritative resource a diligent human might consult (documentation, manuals, scholarly papers, reputable articles) even if it incidentally contains the correct answer." Any attempts where the monitor deemed the rollout suspicious are counted as incorrect. Most samples failed by this check were problems whose exact solution was available on multiple internet sources unrelated to HLE.

\*\*OpenAI has exclusive access to 237 out of 290 private questions on the Tier 1-3 dataset. FrontierMath tier 4 questions not included in this eval. Results evaluated as the average of 16 attempts to answer each question. ChatGPT agent results are elicited by OpenAI, graded by Epoch AI, with browser and terminal access, and a limit of 128K tokens per answer. OpenAI o4-mini and o3 evaluations are elicited and graded by Epoch AI, with no browser and terminal access, with use of python scripts via function calling, and a limit of 100K tokens per answer.

\*\*\* Oracle@64 refers to the best score achieved across 64 sampled runs, selected using ground truth (i.e., we pick the highest-scoring attempt for each task based on actual graded performance). We report the average of these per-task best scores across all tasks. This metric highlights the model’s upper-bound potential and variance in task performance—showing how capable the model can be when it succeeds and indicating room for improving consistency through further training. Unlike typical “best of N” metrics, which select based on model confidence, oracle@64 uses ground truth for selection and applies to tasks graded on a continuous 0–1 scale rather than binary pass/fail.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="introducing-perplexity-deep-research.md">
<details>
<summary>Introducing Perplexity Deep Research</summary>

Phase: [EXPLOITATION]

# Introducing Perplexity Deep Research

**Source URL:** <https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research>

**Today we’re launching Deep Research** to save you hours of time by conducting in-depth research and analysis on your behalf. When you ask a Deep Research question, Perplexity performs dozens of searches, reads hundreds of sources, and reasons through the material to autonomously deliver a comprehensive report. It excels at a range of expert-level tasks—from finance and marketing to product research—and attains high benchmarks on Humanity’s Last Exam.

### How It Works

Perplexity already excels at answering questions. Deep Research takes question answering to the next level by spending 2-4 minutes doing the work it would take a human expert many hours to perform. Here’s how it works:

- **Research with reasoning** - Equipped with search and coding capabilities, Perplexity’s Deep Research mode iteratively searches, reads documents, and reasons about what to do next, refining its research plan as it learns more about the subject areas. This is similar to how a human might research a new topic, refining one’s understanding throughout the process.

- **Report writing** - Once the source materials have been fully evaluated, the agent then synthesizes all the research into a clear and comprehensive report.

- **Export & Share** - You can then export the final report to a PDF or document, or convert it into a Perplexity Page and share it with colleagues or friends.

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

<research_source type="guideline_exploitation" phase="exploitation" file="stop-building-ai-agents-here-s-what-you-should-build-instead.md">
<details>
<summary>Stop Building AI Agents: Here’s what you should build instead</summary>

Phase: [EXPLOITATION]

# Stop Building AI Agents: Here’s what you should build instead

**Source URL:** <https://decodingml.substack.com/p/stop-building-ai-agents>

I've taught and advised dozens of teams building LLM-powered systems. There's a common pattern I keep seeing, and honestly, it's frustrating.

Everyone reaches for agents first. They set up memory systems. They add routing logic. They create tool definitions and character backstories. It feels powerful and it feels like progress.

Until everything breaks. And when things go wrong (which they always do), nobody can figure out why.

**Was it the agent forgetting its task? Is the wrong tool getting selected? Too many moving parts to debug? Is the whole system fundamentally brittle?**

I learned this the hard way. Six months ago, I built a "research crew" with CrewAI: three agents, five tools, perfect coordination on paper. But in practice? The researcher ignored the web scraper, the summarizer forgot to use the citation tool And the coordinator gave up entirely when processing longer documents. It was a beautiful plan falling apart in spectacular ways.

This flowchart came from one of my lessons after debugging countless broken agent systems. Notice that tiny box at the end? That's how rarely you actually need agents. Yet everyone starts there.

[https://substackcdn.com/image/fetch/$s_!ooRJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd63636a1-51a8-41cb-886c-63047728b055_1600x785.png](https://substackcdn.com/image/fetch/$s_!ooRJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd63636a1-51a8-41cb-886c-63047728b055_1600x785.png)

This post is about what I learned from those failures, including how to avoid them entirely.

The patterns I'll walk through are inspired by [Anthropic's Building Effective Agents post](https://www.anthropic.com/engineering/building-effective-agents). But these aren't theory. This is real code, real failures, and real decisions I've made while teaching these systems. Every example here comes from actual projects I've built or debugged.

You'll discover why agents aren't the answer (most of the time). And more importantly, you'll learn what to build instead.

## Don't Start with Agents

Everyone thinks agents are where you start. It's not their fault: frameworks make it seem easy, demo videos are exciting, and tech Twitter loves the hype.

But here's what I learned after building that CrewAI research crew: **most agent systems break down from too much complexity, not too little.**

In my demo, I had three agents working together:

- A researcher agent that could browse web pages
- A summarizer agent with access to citation tools
- A coordinator agent that managed task delegation

Pretty standard stuff, right? Except in practice:

- The researcher ignored the web scraper 70% of the time
- The summarizer completely forgot to use citations when processing long documents
- The coordinator threw up its hands when tasks weren't clearly defined

So wait: _“What exactly is an agent?”_ To answer that, we need to look at 4 characteristics of LLM systems.

1. **Memory:** Let the LLM remember past interactions
2. **Information Retrieval:** Add RAG for context
3. **Tool Usage:** Give the LLM access to functions and APIs
4. **Workflow Control:** The LLM output controls which tools are used and when

^ This makes an **agent**

[https://substackcdn.com/image/fetch/$s_!hKEL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43169d77-56ed-4b9d-8a58-891a5a1039f8_847x480.png](https://substackcdn.com/image/fetch/$s_!hKEL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43169d77-56ed-4b9d-8a58-891a5a1039f8_847x480.png)

When people say "agent," they mean that last step: the LLM output controls the workflow. Most people skip straight to letting the LLM control the workflow without realizing that **simpler patterns often work better**. Using an agent means handing control to the LLM. But unless your task is so dynamic that its flow can’t be defined upfront, that kind of freedom usually hurts more than it helps. Most of the time, simpler workflows with humans in charge still outperform full-blown agents.

I've debugged this exact pattern with dozens of teams:

1. We have multiple tasks that need automation
2. Agents seem like the obvious solution
3. We build complex systems with roles and memory
4. Everything breaks because coordination is harder than we thought
5. We realize simpler patterns would have worked better

> **🔎 Takeaway:** Start with simpler workflows like chaining or routing unless you know you need memory, delegation, and planning.

## Workflow patterns you should use

### (1) Prompt Chaining

_Use case: “Writing personalized outreach emails based on LinkedIn profiles.”_

[https://substackcdn.com/image/fetch/$s_!f_-G!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8710a8d3-bcbd-4175-9a3a-f09bba75635d_2242x507.webp](https://substackcdn.com/image/fetch/$s_!f_-G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8710a8d3-bcbd-4175-9a3a-f09bba75635d_2242x507.webp)

You want to reach out to people at companies you’re interested in. Start by extracting structured data from a LinkedIn profile (name, role, company), then generate a tailored outreach email to start a conversation.

**Here are 3 simple steps:**

1. Turn raw LinkedIn profile text into structured data (e.g., name, title, company):

```
linkedin_data = extract_structured_data(raw_profile)
```

2. Add relevant company context for personalization (e.g., mission, open roles):

```
company_context = enrich_with_context(linkedin_data)
```

3. Generate a personalized outreach email using the structured profile + company context:

```
email = generate_outreach_email(linkedin_data, company_context)
```

#### Guidelines:

✅ Use when: Tasks flow sequentially
⚠️ Failure mode: Chain breaks if one step fails
💡 Simple to debug, predictable flow

### (2) Parallelization

_Use case: Extracting structured data from profiles_

Now that chaining works, you want to process many profiles at once and speed up the processing. Split each profile into parts — like education, work history, and skills, then run extract\_structured\_data() in parallel.

**Here are 2 simple steps:**

1. Define tasks to extract key profile fields in parallel:

```
tasks = [\
    extract_work_history(profile),   # Pull out work experience details\
    extract_skills(profile),         # Identify listed skills\
    extract_education(profile)       # Parse education background\
]
```

2. Run all tasks concurrently and gather results:

```
results = await asyncio.gather(*tasks)
```

#### Guidelines:

✅ Use when: Independent tasks run faster concurrently
⚠️ Failure mode: Race conditions, timeout issues
💡 Great for data extraction across multiple sources

### (3) Routing

_Use case: LLM classifies the input and sends it to a specialized workflow_

Say you’re building a support tool that handles product questions, billing issues, and refund requests. Routing logic classifies each message and sends it to the right workflow. If it’s unclear, fall back to a generic handler.

**Here are 2 simple steps:**

1. Choose a handler based on profile type:

```
if profile_type == "executive":
    handler = executive_handler()    # Use specialized logic for executives
elif profile_type == "recruiter":
    handler = recruiter_handler()    # Use recruiter-specific processing
else:
    handler = default_handler()      # Fallback for unknown or generic profiles
```

2. Process the profile with the selected handler:

```
result = handler.process(profile)
```

#### Guidelines:

✅ Use when: Different inputs need different handling
⚠️ Failure mode: Edge cases fall through routes
💡 Add catch-all routes for unknowns

### (4) Orchestrator-Worker

_Use case: LLM breaks down the task into 1 or more dynamic steps_

You’re generating outbound emails. The orchestrator classifies the target company as tech or non-tech, then delegates to a specialized worker that crafts the message for that context.

**Here are 2 simple steps:**

1. Use LLM to classify the profile as tech or non-tech:

```
industry = llm_classify(profile_text)
```

2. Route to the appropriate worker based on classification:

```
if industry == "tech":
    email = tech_worker(profile_text, email_routes)
else:
    email = non_tech_worker(profile_text, email_routes)
```

The orchestrator-worker pattern separates decision-making from execution:

- The orchestrator controls the flow: its output controls what needs to happen and in what order
- The workers carry out those steps: they handle specific tasks delegated to them

At first glance, this might resemble routing: a classifier picks a path, then a handler runs. But in routing, control is handed off entirely. In this example, the orchestrator retains control: it initiates the classification, selects the worker, and manages the flow from start to finish.

This is a minimal version of the orchestrator-worker pattern:

- The orchestrator controls the flow, making decisions and coordinating subtasks
- The workers carry out the specialized steps based on those decisions

#### Guidelines:

✅ Use when: Tasks need specialized handling
⚠️ Failure mode: Orchestrator delegates subtasks poorly or breaks down the task incorrectly
💡 Keep orchestrator logic simple and explicit

### (5) Evaluator-Optimizer

_Use case: Refining outreach emails to better match your criteria_

[https://substackcdn.com/image/fetch/$s_!lzd4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48d8175e-a3ab-47b1-8a55-4f409ba8aee2_1825x613.png](https://substackcdn.com/image/fetch/$s_!lzd4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F48d8175e-a3ab-47b1-8a55-4f409ba8aee2_1825x613.png)

You’ve got an email generator running, but want to improve tone, structure, or alignment. Add an evaluator that scores each message and, If it doesn’t pass, send it back to the generator with feedback and loop until it meets your bar.

**Here are 2 simple steps:**

1. Generate an initial email from the profile:

```
content = generate_email(profile)
```

2. Loop until the email passes the evaluator or hits a retry limit:

```
while True:
    score = evaluate_email(content)
    if score.overall > 0.8 or score.iterations > 3:
        break
    content = optimize_email(content, score.feedback)
```

#### Guidelines:

✅ Use when: Output quality matters more than speed
⚠️ Failure mode: Infinite optimization loops
💡 Set clear stop conditions

> **🔎 Takeaway:** Most use cases don't need agents. They need better workflow structure.

## When to Use Agents (If You Really Have To)

Agents shine when you have a sharp human in the loop. Here's my hot take: agents excel at unstable workflows where human oversight can catch and correct mistakes.

_When agents actually work well:_

#### Example 1: Data Science Assistant

An agent that writes SQL queries, generates visualizations, and suggests analyses. You're there to evaluate results and fix logical errors. The agent's creativity in exploring data beats rigid workflows.

To build something like this, you’d give the LLM access to tools like run\_sql\_query(), plot\_data(), and summarize\_insights(). The agent routes between them based on the user’s request — for example, writing a query, running it, visualizing the result, and generating a narrative summary. Then, it feeds the result of each tool call back into another LLM request with its memory context.

[https://substackcdn.com/image/fetch/$s_!Aago!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf8727e9-f0c0-4420-8ce5-78d846fc15e5_1600x818.png](https://substackcdn.com/image/fetch/$s_!Aago!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf8727e9-f0c0-4420-8ce5-78d846fc15e5_1600x818.png)

#### Example 2: Creative Writing Partner

An agent brainstorming headlines, editing copy, and suggesting structures. The human judges quality and redirects when needed. Agents excel at ideation with human judgment.

#### Example 3: Code Refactoring Assistant

Proposing design patterns, catching edge cases, and suggesting optimizations. The developer reviews and approves changes. Agents spot patterns humans miss.

## When NOT to use agents

**Enterprise Automation**

Building stable, reliable software? Don't use agents. You can't have an LLM deciding critical workflows in production. Use orchestrator patterns instead.

- **High-Stakes Decisions**

Financial transactions, medical diagnoses, and legal compliance – these need deterministic logic, not LLM guesswork.

Back to my CrewAI research crew: the agents kept forgetting goals and skipping tools. Here's what I learned:

**Failure Point #1:** Agents assumed they had context that they didn’t

**Problem:** Long documents caused the summarizer to forget citations entirely

**What I'd do now:** Use explicit memory systems, not just role prompts

**Failure Point #2:** Agents failed to select the right tools

**Problem:** The researcher ignored the web scraper in favor of a general search

**What I'd do now:** Constrain choices with explicit tool menus

**Failure Point #3:** Agents did not handle coordination well

**Problem:** The coordinator gave up when tasks weren't clearly scoped

**What I'd do now:** Build explicit handoff protocols, not free-form delegation

> **🔎 Takeaway:** If you're building agents, treat them like full software systems. Don't skip observability.

[https://substackcdn.com/image/fetch/$s_!cv1W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bf927de-ab95-449f-b936-7ccb3ab5f448_1587x526.png](https://substackcdn.com/image/fetch/$s_!cv1W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3bf927de-ab95-449f-b936-7ccb3ab5f448_1587x526.png)

## TL;DR

- ❌ Agents are overhyped and overused
- 🔁 Most cases need simple patterns, not agents
- 🤝 Agents excel in human-in-the-loop scenarios
- ⚠️ Don't use agents for stable enterprise systems
- 🧪 Build with observability and explicit control

Agents are overhyped and often overused. In most real-world applications, simple patterns and direct API calls work better than complex agent frameworks. Agents do have a role—in particular, they shine in human-in-the-loop scenarios where oversight and flexibility are needed. But for stable enterprise systems, they introduce unnecessary complexity and risk. Instead, aim to build with strong observability, clear evaluation loops, and explicit control.

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>