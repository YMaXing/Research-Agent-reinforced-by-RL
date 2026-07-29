<digest_meta>
  <article_title>14_agent_system_design</article_title>
  <total_sources>9</total_sources>
  <total_artefacts>13</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>42</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="api-pricing" type="golden_web">OpenAI API pricing covers flagship reasoning models optimized for complex multi-step tasks, multimodal models, built-in tools, and service tiers for agentic workloads. Flagship models include GPT-5.5 ($5/1M input, $0.50 cached, $30 output), GPT-5.4 ($2.50/$0.25/$15), and GPT-5.4 mini ($0.75/$0.075/$4.50) for coding, computer use, and subagents; all prices apply under 270K context with standard processing. Multimodal offerings comprise GPT-Realtime-2 (audio $32/$0.40/$64, text $4/$0.40/$24, image $5/$0.50 per 1M tokens), GPT-Realtime-Translate ($0.034/min), GPT-Realtime-Whisper ($0.017/min), and GPT-Image-2 (image $8/$2/$30, text $5/$1.25). Tools list Web search at $10 per 1k calls (search content tokens free) and Containers (1 GB $0.03 or 64 GB $1.92 per container, shifting to per-20-minute sessions from March 2026). Service tiers provide Batch API (50% discount on async 24-hour jobs), Priority processing for high-speed pay-as-you-go, and Flex processing for reduced cost with slower responses and possible unavailability. Enterprise features cover Data residency, Scale Tier, and Reserved Capacity via sales contact. The source includes a pricing calculator for image tokenization (e.g., 512×512 tiles yielding 210 total tokens at $0.000263) plus FAQ on model selection, Playground billing equivalence, usage dashboards, monthly budget limits, and separation from ChatGPT subscriptions. Coverage gaps include absence of latency benchmarks, exact context-window pricing tiers above 270K, tokenization formulas for specific vision models (gpt-4.1-mini, o4-mini), and integration examples with agent frameworks.</s>
<s slug="extended-thinking-interleaved-thinking-docs" type="golden_web">Extended thinking enables Claude models to generate internal `thinking` content blocks for step-by-step reasoning before producing final `text` blocks via the Messages API. It supports manual mode (`thinking: {type: "enabled", budget_tokens: N}`) on most models and adaptive mode (`thinking: {type: "adaptive"}` with effort parameter) on Claude Opus 4.8, Opus 4.7, Fable 5, and Mythos 5. `budget_tokens` sets the reasoning allocation (minimum 1,024; must be < `max_tokens` except under interleaved thinking), with Claude Opus 4.6/Sonnet 4.6 and later supporting up to 128k output tokens and the `output-300k-2026-03-24` beta header raising limits to 300k via Message Batches API. Key concepts include summarized thinking (default on Claude 4 models via `display: "summarized"`), omitted thinking (`display: "omitted"` for empty `thinking` fields with preserved `signature`), streaming via `thinking_delta` and `signature_delta` events over SSE, and thinking encryption in the `signature` field for verification. Redacted thinking blocks use a `data` field for safety-redacted content. The source includes a 23-line Python tool-loop example and a streaming SSE event sequence. Interleaved thinking (enabled automatically under adaptive thinking on Opus 4.8/4.7/4.6 and Mythos Preview; via `interleaved-thinking-2025-05-14` beta header on earlier Claude 4 models) allows reasoning between tool calls, supporting only `tool_choice: {"type": "auto"}` or `none`. Tool results require unmodified round-tripping of prior `thinking` blocks for continuity; toggling modes mid-turn triggers graceful degradation that silently disables thinking. Prompt caching preserves system prompts and tools but invalidates message breakpoints on thinking parameter changes; Opus 4.5+ and Sonnet 4.6 retain all prior thinking blocks by default (counting as input tokens), while earlier models and Haiku retain only the last turn. The ARTEFACT_A01 table compares feature availability across Opus/Sonnet/Haiku versions. Claims note that `usage.output_tokens_details.thinking_tokens` reports billed reasoning separately from visible output, budgets above 32k benefit from batch processing, and `max_tokens` enforcement yields `stop_reason: "model_context_window_exceeded"` on newer models. Limitations include incompatibility with `temperature`, `top_k`, forced tool use, and `max_tokens: 0`; partner platforms (Bedrock, Vertex) reject the beta header on unsupported models; and no support for pre-filling responses. Gaps exist around exact performance benchmarks and multi-platform signature compatibility details.</s>
<s slug="human-in-the-loop" type="golden_web">Human-in-the-loop in LangGraph enables dynamic pauses during graph execution for external input via the `interrupt()` function from `langgraph.types`. The main topic covers interrupt mechanics, resumption with `Command(resume=...)`, persistence via checkpointers, and `thread_id` in config for state management. Interrupts are dynamic and conditional, unlike static breakpoints set with `interrupt_before`/`interrupt_after` at compile or runtime. Execution suspends at the call site, saves state through the persistence layer (e.g., `InMemorySaver`, `SqliteSaver`, `MemorySaver`), surfaces payloads on `stream.interrupts` or `result["__interrupt__"]`, and waits until resumption. Key APIs and techniques include `graph.stream_events(..., version="v3")` for concurrent message chunks via `stream.messages`, state snapshots via `stream.values`, interrupt detection via `stream.interrupted`/`stream.interrupts`, and looping resumption until completion. The default `graph.invoke()` also works but is less recommended for streaming. Resumption always restarts the node from its start; `Command(resume=...)` is the sole supported input pattern for multi-turn flows. The source details patterns such as approval workflows (routing via `Command(goto=...)` to "proceed"/"cancel"), review-and-edit of state (e.g., editing `generated_text`), interrupts inside `@tool`-decorated functions (e.g., `send_email` pausing before execution), and input validation loops that re-prompt on invalid data. Concrete examples cover parallel interrupts across fan-out nodes (resumed via ID-to-value map), an approval node exposing `action_details`, a review node updating content, a tool-integrated agent loop using `ChatAnthropic` bound to tools with `SqliteSaver` for persistence, and a form node validating age input. Code patterns demonstrate idempotent operations before `interrupt()`, separation of side effects, and consistent interrupt ordering. Rules prohibit try/except around `interrupt()`, conditional skipping or nondeterministic loops of calls, non-JSON-serializable payloads (e.g., functions or class instances), and non-idempotent side effects. Subgraph interrupts resume from the parent node start. Static breakpoints are noted as unsuitable for HITL; use `LangSmith Studio` for debugging instead. No quantitative benchmarks or performance claims appear. Coverage gaps include production deployment details beyond recommending durable checkpointers, integration with non-LangGraph runtimes, and handling of complex nested subgraph interrupt propagation beyond basic restart semantics. The source includes multiple full runnable examples (e.g., approval workflow with `ApprovalState`, tool-approval agent with `AgentState`, age validation with `FormState`) that illustrate end-to-end streaming and resumption flows.</s>
<s slug="llm-system-design-model-selection" type="golden_web">**Main topic:** LLM system design and model selection, emphasizing trade-offs among capability, cost, latency, and reliability when choosing and orchestrating models in production systems. The article argues that inference-time scaling has replaced simple pretraining scale as the dominant driver of both performance gains and cost explosion. **Key concepts:** Four inference scaling levers (model size/MoE, series/"thinking tokens", parallel sampling with majority voting or self-confidence, input context scaling in RAG); shift from pretraining compute to post-training (instruction tuning, RLHF/RLAIF), synthetic data, and inference-time reasoning (o1-style); open-weight vs closed-API decision framework; staged escalation from prompt engineering → RAG → advanced RAG → fine-tuning/distillation/RFT → orchestrated workflows vs autonomous agents; "march of nines" reliability approach and custom evaluation as non-negotiable. **Concrete examples, tools, frameworks, APIs:** Closed models referenced include GPT-4.5, GPT-4o, o1, o3, o3-pro, o4-mini, Gemini 2.5 Flash-Lite, Gemini 2.5 Pro, Gemini Flash 2.5, Claude 4, Claude Opus 4.0; open-weight models include Llama 3.3 70B, Mistral, DeepSeek R1, Qwen (Qwen3-235B, Qwen 70B), Gemma 3 27B, Gemma 3n, Codestral, Kimi K2, Hunyuan. Techniques named: RAG with hybrid search + re-ranking + query transformation, context caching, reinforcement fine-tuning (RFT) requiring an automated grader, distillation via synthetic data, tool-use agent loops. Platforms and leaderboards: Ollama, LMArena, Artificial Analysis, LiveBench (contamination-free benchmark scored out of 100). **Specific data points and claims:** Input tokens for Gemini 2.5 Flash-Lite are ~600× cheaper than GPT-3 davinci-002 (Aug 2022) while outperforming it; GPT-4.5 input cost 750× higher than Gemini Flash-Lite; o1 used ~30× more compute and often 5× more output tokens than GPT-4o; o3-pro likely runs 5–10× parallel instances; realistic API cost differences of 10,000×–1,000,000× across architectures; DeepSeek R1 priced ~30× lower than o1 while competitive; LiveBench scores of GPT-4.5 and 2.5 Flash-Lite are similar despite 750× cost gap; success examples include Cursor and Perplexity (valued >$10B). Rule of thumb: adopt higher-cost model when reliability gain saves more human time than the incremental API cost. **Notable limitations/gaps:** Detailed numeric pricing and LiveBench scores are presented only in two referenced image tables (closed-model pricing and open-weight pricing/specifications) whose contents are not reproduced in text; quantitative agent cost/runaway examples and exact grader implementations for RFT are described at high level without concrete code or failure-rate data; coverage of mobile/edge deployment and regulatory data-residency options is brief; the source does not compare specific agent frameworks or orchestration libraries.</s>
<s slug="revisiting-the-test-time-scaling-of-o1-like-models" type="golden_web">The source examines test-time scaling in o1-like models (QwQ, Deepseek-R1 variants, LIMO), distinguishing sequential scaling (extending CoT length via self-revision) from parallel scaling (sampling multiple solutions). It finds that longer CoTs do not improve accuracy; correct solutions are consistently shorter than incorrect ones across MATH-500, AIME, Omni-MATH (500-question sample), and GPQA diamond. Self-revision markers (“Wait”, “Alternatively”) correlate linearly with length, yet successful revision rates remain below 10 percent, with most outputs retaining original (often incorrect) answers and weaker models (QwQ, R1-Distill-1.5b) more often converting correct answers to incorrect ones. Parallel scaling yields higher pass@k coverage and better token efficiency than sequential revision on the same models run via SGLang (temperature 0.7, 32k max length, OpenCompass/Qwen Math evaluators). The paper introduces Shortest Majority Vote: group parallel samples by answer, score each cluster \(s_i = c_i / \log l_i\) (where \(c_i\) is count and \(l_i\) is average length), and select the highest-scoring cluster. On AIME with 16 samples this outperforms standard majority vote and a shortest-only baseline; gains are smaller on GPQA. Includes a 3-line table on LIMO revision proportions and a 12-line table comparing MV, Shortest, and Shortest MV across 2- and 16-solution regimes. Limitations noted are restricted R1-671b evaluation, static checkpoints only, and reduced applicability when models possess strong sequential scaling.</s>
<s slug="what-is-the-model-context-protocol-mcp" type="golden_web">MCP (Model Context Protocol) is an open-source standard that connects AI applications to external data sources, tools, and workflows. It functions as a standardized interface, analogous to USB-C, allowing models such as Claude or ChatGPT to access local files, databases, search engines, calculators, and specialized prompts without custom integrations for each system. Key capabilities include agents reading and acting on Google Calendar and Notion entries, Claude Code generating complete web applications from Figma designs, enterprise chatbots querying multiple organizational databases through natural language, and AI models producing 3D designs in Blender followed by direct output to 3D printers. The protocol delivers three stated benefits: developers reduce time and complexity when building or integrating AI applications; AI agents and applications gain access to a shared ecosystem of data sources, tools, and apps; and end users receive more capable agents that can retrieve personal data and execute actions on their behalf. Ecosystem support encompasses clients and servers including Claude, ChatGPT, Visual Studio Code, Cursor, and MCPJam. The source references an introductory diagram illustrating basic MCP connections but provides no implementation specifications, performance benchmarks, security details, or quantitative adoption metrics. Coverage remains limited to high-level use cases and stakeholder advantages without code samples, protocol schemas, or comparisons to prior agent-tooling approaches.</s>
<s slug="gemini-review" type="exploitation">Gemini Deep Research is an agentic research system in the Gemini app that decomposes complex queries into multi-point plans, autonomously executes web, Gmail, Drive, and Chat searches, reasons iteratively, and synthesizes multi-page reports. It supports Canvas conversion to interactive content, quizzes, and Audio Overviews. The system uses a planning component that outputs a user-editable research plan, followed by parallel/sequential task scheduling. Execution relies on search and web-browsing tools inside a continuous reasoning loop; a visible thinking panel exposes intermediate findings and next-action decisions. Synthesis applies multiple self-critique passes to identify themes and inconsistencies before final report generation. Core engineering techniques include a novel asynchronous task manager that maintains shared state between planner and task models for graceful recovery across long-running (multi-minute) sessions without full restarts. Context is preserved via Gemini’s 1-million-token window combined with RAG, enabling the model to retain hundreds of browsed pages across follow-up turns. The initial implementation ran on Gemini 1.5 Pro; later versions adopted Gemini 2.0 Flash Thinking (experimental) and Gemini 3 for improved self-reflection and serving efficiency. Concrete use cases listed are competitive analysis (cross-referencing public data with Workspace memos and spreadsheets), due diligence on sales leads, topic comparison of concepts, and product-feature benchmarking. The architecture is described as a continuous “Reason–Search–Browse” loop that integrates Google Search and web technologies. Coverage gaps include absence of quantitative benchmarks on report quality, latency, or token usage; no details on the exact RAG retrieval implementation, failure-rate statistics for the asynchronous manager, or the training data/methods used for long-horizon planning. The source notes ongoing expansion of controllable data sources but provides no implementation timeline or API surface.</s>
<s slug="intro-to-perplexity" type="exploitation">Perplexity Deep Research is an autonomous agent mode that performs multi-step expert research by executing dozens of searches, ingesting hundreds of sources, and iteratively refining a research plan before synthesizing a final report. The core loop combines search and coding capabilities for reasoning-driven exploration, followed by report generation and export options (PDF, document, or Perplexity Page). The system is positioned for domains including finance, marketing, technology, current affairs, health, biography, and travel planning. It is accessible via the mode selector at perplexity.ai (model_id=deep_research) and is free with daily limits for non-subscribers or higher volume for Pro users; rollout covers Web immediately and iOS/Android/Mac in subsequent updates. Benchmark claims include 21.1% accuracy on Humanity’s Last Exam (3,000+ questions across 100+ subjects) and 93.9% on SimpleQA, both exceeding Gemini Thinking, o3-mini, o1, and DeepSeek-R1. Most tasks complete in under 3 minutes. The source includes multiple domain-specific example screenshots but provides no implementation details, architecture diagrams, or code. Notable gaps: no discussion of internal agent architecture, tool-use schemas, memory mechanisms, or failure modes; performance numbers are self-reported without raw data or evaluation methodology; and runtime scaling behavior for longer tasks is omitted.</s>
<s slug="lost-in-the-middle-how-language-models-use-long-contexts" type="exploitation">Lost in the Middle examines how language models process long contexts on multi-document question answering (NaturalQuestions-Open) and synthetic key-value retrieval. Models exhibit a U-shaped performance curve: highest accuracy when relevant information occurs at the start (primacy bias) or end (recency bias) of the context, with sharp degradation in the middle even for explicitly long-context models. Experiments vary context length (10/20/30 documents or 75/140/300 KV pairs) and position of the single relevant item while using Contriever (MS-MARCO fine-tuned) to select distractors and accuracy (exact answer presence) as the metric. Tested models include MPT-30B-Instruct (ALiBi, 8K), LongChat-13B (16K) (condensed RoPE), GPT-3.5-Turbo / (16K), Claude-1.3 / (100K), Flan-T5-XXL, Flan-UL2, and Llama-2 (7B/13B/70B) variants. GPT-3.5-Turbo drops >20 points in middle positions (below its 56.1% closed-book baseline); Claude-1.3 achieves near-perfect KV retrieval but still shows the curve on QA. Encoder-decoder models remain robust only inside training lengths (512–2048 tokens). Query-aware contextualization yields near-perfect KV accuracy but negligible QA gains. Instruction fine-tuning and scale (≥13B) modulate but do not eliminate the bias. Open-domain QA case study shows reader accuracy saturates by ~20 documents while retriever recall continues rising. Source includes multiple exact prompt templates, position-modulation diagrams, and tabulated token statistics (e.g., 20-document contexts average 2.9K–3.5K tokens). Coverage gaps include decoder-only attention analysis beyond the tested models and non-greedy decoding effects.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 3 | 6 | 0 |
| S2::section-2-a-general-ai-engineering-decision-framework | 3 | 6 | 0 |
| S3::section-3-inference-time-scaling-and-the-cost-latency-calculus | 1 | 5 | 0 |
| S4::section-4-our-capstone-global-system-design | 1 | 5 | 0 |
| S5::section-5-decision-matrix-defaults-for-the-capstone | 2 | 5 | 0 |
| S6::section-6-conclusion | 2 | 4 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="yes" sources="llm-system-design-model-selection,gemini-review,extended-thinking-interleaved-thinking-docs" artefacts="">
  <intent>Introduce the lesson by anchoring to prior capstone scoping and framework selection while positioning system design as the layer that turns frameworks into production-ready agents.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="theoretical_foundations" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="technical_nuances" present="yes" evidence="extended-thinking-interleaved-thinking-docs"/>
    <item name="latest_advancements" present="yes" evidence="gemini-review"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="case_studies_metrics" present="yes" evidence="gemini-review"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="gemini-review"/>
    <item name="industry_applications" present="yes" evidence="gemini-review"/>
    <item name="adjacent_trends" present="yes" evidence="llm-system-design-model-selection"/>
  </breadth_checklist>
  <orphan_anchors n_depth="7" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Introduce the course by anchoring it to the capstone project defined in the last two cources: In Lesson 12, the scope of" bullet="motivation">Directly supports lesson motivation and prior-lesson anchoring.</orphan>
    <orphan route="depth" anchor="Position system design as the distinct layer that sits above framework selection (FastMCP plus LangGraph) and determines" bullet="theoretical_foundations">Core thesis of the section on system-design layer.</orphan>
    <orphan route="depth" anchor="Show how core design variables (reasoning budget, context strategy, orchestration style, HITL placement, artifact contra" bullet="implementation_tradeoffs">Details the variables that drive trade-offs.</orphan>
    <orphan route="depth" anchor="Preview the reusable 7-step decision playbook that moves systematically from business value definition through model rou" bullet="motivation">Introduces the central framework of the article.</orphan>
    <orphan route="depth" anchor="Directly signal that the playbook will be applied in full to the capstone, yielding the global Nova-versus-Brown archite" bullet="case_studies_metrics">Signals concrete application to capstone.</orphan>
    <orphan route="depth" anchor="State the concrete learning goals: you will leave able to decide where extra thinking tokens deliver genuine value, when" bullet="motivation">Explicit learning outcomes tied to design variables.</orphan>
    <orphan route="depth" anchor="Transition to Section 2: With the stakes clear, we now walk through the general 7-step framework before specializing it to the capstone." bullet="implementation_tradeoffs">Bridges to next section via framework application.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-a-general-ai-engineering-decision-framework" self_contained="yes" sources="lost-in-the-middle-how-language-models-use-long-contexts,what-is-the-model-context-protocol-mcp,revisiting-the-test-time-scaling-of-o1-like-models" artefacts="">
  <intent>Present the reusable 7-step AI engineering decision framework that balances capability, cost, latency and reliability.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="theoretical_foundations" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="technical_nuances" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="latest_advancements" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="limitations_failure_modes" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
  </breadth_checklist>
  <orphan_anchors n_depth="8" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Define Value, Constraints, Cost &amp; Latency: explicitly define success criteria, including the output quality bar, privacy" bullet="motivation">First step of the core 7-step framework.</orphan>
    <orphan route="depth" anchor="Choose Model Family &amp; Capability Mix: when to prefer closed APIs that deliver SOTA performance and low operational overh" bullet="implementation_tradeoffs">Directly addresses model-selection trade-offs.</orphan>
    <orphan route="depth" anchor="Define Your Context Strategy: Mention that, as seen in previous lessons, a large context window is not always a good sol" bullet="theoretical_foundations">Cites lost-in-the-middle evidence for context discipline.</orphan>
    <orphan route="depth" anchor="Pick an Orchestration Style: use predictable workflows when steps are auditable and linear, dynamic agents when open-end" bullet="implementation_tradeoffs">Maps orchestration choice to job type.</orphan>
    <orphan route="depth" anchor="Establish a HITL &amp; Evaluation Loop: HITL triggers, confidence gates, and custom evaluation design versus full autonomy;" bullet="limitations_failure_modes">Defines risk-based human oversight policy.</orphan>
    <orphan route="depth" anchor="Set Tool Boundaries &amp; Portability:: keep the LLM responsible solely for intent detection and high-level orchestration wh" bullet="technical_nuances">Specifies clean separation of LLM vs deterministic logic.</orphan>
    <orphan route="depth" anchor="Choose Durability &amp; Observability: for long-running stateful jobs demand resumability, checkpoints, and full tracing; fo" bullet="implementation_tradeoffs">Links durability choices to success criteria.</orphan>
    <orphan route="depth" anchor="Throughout, emphasize that the framework is iterative: you will revisit earlier steps as new constraints surface during" bullet="motivation">Reinforces iterative nature of the framework.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-inference-time-scaling-and-the-cost-latency-calculus" self_contained="yes" sources="api-pricing,intro-to-perplexity,lost-in-the-middle-how-language-models-use-long-contexts" artefacts="">
  <intent>Quantify the four inference-time scaling levers and demonstrate their multiplicative impact on cost and latency.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="api-pricing"/>
    <item name="theoretical_foundations" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="technical_nuances" present="yes" evidence="intro-to-perplexity"/>
    <item name="latest_advancements" present="yes" evidence="intro-to-perplexity"/>
    <item name="limitations_failure_modes" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="implementation_tradeoffs" present="yes" evidence="api-pricing"/>
    <item name="case_studies_metrics" present="yes" evidence="api-pricing"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="lost-in-the-middle-how-language-models-use-long-contexts"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="intro-to-perplexity"/>
    <item name="industry_applications" present="yes" evidence="intro-to-perplexity"/>
    <item name="adjacent_trends" present="yes" evidence="api-pricing"/>
  </breadth_checklist>
  <orphan_anchors n_depth="8" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Introduce the four independent runtime levers: model size (parameter count and intelligence), series scaling (extra thin" bullet="theoretical_foundations">Defines the four levers central to the section.</orphan>
    <orphan route="depth" anchor="Model Size Scaling: the most straightforward lever. Larger, more capable models have higher per-token costs than smaller" bullet="implementation_tradeoffs">Quantifies model-size cost impact.</orphan>
    <orphan route="depth" anchor="Series Scaling: This refers to increasing the internal computational steps a model takes before answering, often called" bullet="technical_nuances">Explains thinking-token budgeting.</orphan>
    <orphan route="depth" anchor="Parallel Scaling: This involves running the same prompt multiple times in parallel and selecting the best response, typi" bullet="case_studies_metrics">Covers self-consistency and majority-vote scaling.</orphan>
    <orphan route="depth" anchor="Input Context Scaling: relevant information is valuable but each additional token carries direct cost and indirect laten" bullet="limitations_failure_modes">Addresses lost-in-the-middle risk of context bloat.</orphan>
    <orphan route="depth" anchor="Include the image in the link &lt;https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/8182d40f-9b03-4f68-a89" bullet="motivation">Visual summary of the four levers.</orphan>
    <orphan route="depth" anchor="Present a toy cost-calculation contrast: naive design (largest reasoning model, entire document dumped in context, five" bullet="case_studies_metrics">Provides quantitative naive-vs-budgeted contrast.</orphan>
    <orphan route="depth" anchor="Additional optimizations that keep LLM context small and focused: per-step reasoning caps, prompt caching across similar" bullet="implementation_tradeoffs">Lists practical context-control techniques.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-our-capstone-global-system-design" self_contained="yes" sources="human-in-the-loop,gemini-review,what-is-the-model-context-protocol-mcp" artefacts="">
  <intent>Apply the 7-step framework to produce the concrete global Nova/Brown architecture with component flows and file-based contracts.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="gemini-review"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="technical_nuances" present="yes" evidence="human-in-the-loop"/>
    <item name="latest_advancements" present="yes" evidence="gemini-review"/>
    <item name="limitations_failure_modes" present="yes" evidence="human-in-the-loop"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="what-is-the-model-context-protocol-mcp"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="human-in-the-loop"/>
    <item name="industry_applications" present="yes" evidence="gemini-review"/>
    <item name="adjacent_trends" present="yes" evidence="gemini-review"/>
  </breadth_checklist>
  <orphan_anchors n_depth="13" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Include the image in the link &lt;https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7a5049bb-562c-4d03-a1b" bullet="motivation">Global architecture diagram for Nova/Brown.</orphan>
    <orphan route="depth" anchor="use the above image to illustrate the core architectural principle of our capstone: enforce clean separation of concerns" bullet="theoretical_foundations">States separation-of-concerns principle.</orphan>
    <orphan route="depth" anchor="Start a subsection with an H3 title &quot;Research Agent (Nova)&quot;:" bullet="technical_nuances">Details Nova MCP agent implementation.</orphan>
    <orphan route="depth" anchor="Include the image in the link &lt;https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/15b5ba4a-cced-48e7-8b0" bullet="case_studies_metrics">Nova research flow diagram.</orphan>
    <orphan route="depth" anchor="Start a subsection with an H3 title &quot;Writing Workflows (Brown)&quot;:" bullet="technical_nuances">Details Brown LangGraph workflow.</orphan>
    <orphan route="depth" anchor="Generate Article: This orchestrates the following workflow: loads context (guidelines, research, profiles, examples), ge" bullet="implementation_tradeoffs">Specifies Generate Article tool contract.</orphan>
    <orphan route="depth" anchor="Edit Article: This runs a single review-edit cycle on the entire article based on human feedback, incorporating the eval" bullet="implementation_tradeoffs">Specifies Edit Article tool contract.</orphan>
    <orphan route="depth" anchor="Edit Selected Text: This runs a single review-edit cycle on a specific portion of the article, enabling targeted revisio" bullet="implementation_tradeoffs">Specifies Edit Selected Text tool contract.</orphan>
    <orphan route="depth" anchor="Include the image in the link &lt;https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2a704cb-c430-4702-bab" bullet="case_studies_metrics">Brown Generate Article sequence diagram.</orphan>
    <orphan route="depth" anchor="The handoff between Nova and Brown is simple and file-based. Nova produces `research.md` and a structured `.nova/` direc" bullet="implementation_tradeoffs">Defines file-based artifact contract.</orphan>
    <orphan route="depth" anchor="The `article_guideline.md` is where the human comes into the loop. It acts as the seed, where the human defines what it" bullet="motivation">Positions human guideline as quality seed.</orphan>
    <orphan route="depth" anchor="If the ideas are not clearly enumerated and connected, the output will be sloppy. Expand on why the article guideliens s" bullet="limitations_failure_modes">Explains risk of vague guidelines producing hollow output.</orphan>
    <orphan route="depth" anchor="Transition to Section 5: The architecture and diagrams are now concrete; the final step is to translate the framework principles into an explicit, implementable decision matrix." bullet="implementation_tradeoffs">Bridges to decision-matrix section.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-decision-matrix-defaults-for-the-capstone" self_contained="yes" sources="llm-system-design-model-selection,extended-thinking-interleaved-thinking-docs,revisiting-the-test-time-scaling-of-o1-like-models" artefacts="">
  <intent>Translate the 7-step framework into an explicit, implementable decision matrix with defaults and rationales for Nova versus Brown.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="theoretical_foundations" present="yes" evidence="extended-thinking-interleaved-thinking-docs"/>
    <item name="technical_nuances" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="latest_advancements" present="yes" evidence="extended-thinking-interleaved-thinking-docs"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="case_studies_metrics" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="artefact_available" present="yes" evidence="extended-thinking-interleaved-thinking-docs"/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="llm-system-design-model-selection"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="extended-thinking-interleaved-thinking-docs"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Show how the abstract principles of the 7-step framework are translated into specific, implementable defaults tailored t" bullet="implementation_tradeoffs">Maps framework steps to concrete defaults.</orphan>
    <orphan route="depth" anchor="Emphasize that the matrix is not aspirational but the exact blueprint you will implement starting in the next lesson; an" bullet="motivation">States that matrix is the binding implementation blueprint.</orphan>
    <orphan route="depth" anchor="Describe the matrix structure itself: each row captures a decision dimension, the chosen default, and an explicit ration" bullet="technical_nuances">Defines matrix row format and rationale linkage.</orphan>
    <orphan route="depth" anchor="Position the matrix as a living blueprint that prevents ad-hoc choices during implementation; you will refer to it repea" bullet="implementation_tradeoffs">Positions matrix as living reference for Lessons 15-22.</orphan>
    <orphan route="depth" anchor="Include the following decision matrix as a table, where the caption should be verbatim &quot;Table 1: Decision matrix for the" bullet="case_studies_metrics">Presents the six-row decision matrix.</orphan>
    <orphan route="depth" anchor="No transition line required as this is the final content section before the conclusion." bullet="motivation">Signals end of content sections.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion" self_contained="yes" sources="gemini-review,intro-to-perplexity,revisiting-the-test-time-scaling-of-o1-like-models" artefacts="">
  <intent>Recap the 7-step framework, Nova/Brown architecture and decision matrix while pointing forward to implementation lessons.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="gemini-review"/>
    <item name="theoretical_foundations" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="technical_nuances" present="yes" evidence="intro-to-perplexity"/>
    <item name="latest_advancements" present="yes" evidence="gemini-review"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="case_studies_metrics" present="yes" evidence="intro-to-perplexity"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="revisiting-the-test-time-scaling-of-o1-like-models"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="gemini-review"/>
    <item name="industry_applications" present="yes" evidence="intro-to-perplexity"/>
    <item name="adjacent_trends" present="yes" evidence="gemini-review"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="23" need_breadth="2" target_words="200" mandatory_bullets="7" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S2::section-2-a-general-ai-engineering-decision-framework" need_depth="26" need_breadth="3" target_words="1000" mandatory_bullets="7" must_cover_depth="7" must_stay_brief="0"/>
  <section id="S3::section-3-inference-time-scaling-and-the-cost-latency-calculus" need_depth="25" need_breadth="2" target_words="700" mandatory_bullets="8" must_cover_depth="6" must_stay_brief="0"/>
  <section id="S4::section-4-our-capstone-global-system-design" need_depth="41" need_breadth="2" target_words="900" mandatory_bullets="6" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S5::section-5-decision-matrix-defaults-for-the-capstone" need_depth="19" need_breadth="3" target_words="100" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S6::section-6-conclusion" need_depth="2" need_breadth="2" target_words="300" mandatory_bullets="5" must_cover_depth="2" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S2::section-2-a-general-ai-engineering-decision-framework, S4::section-4-our-capstone-global-system-design</weakest_sections>
    <strongest_sections>S6::section-6-conclusion, S5::section-5-decision-matrix-defaults-for-the-capstone</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>