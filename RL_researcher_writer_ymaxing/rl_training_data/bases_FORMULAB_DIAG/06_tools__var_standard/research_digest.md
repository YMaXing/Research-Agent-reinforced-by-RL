<digest_meta>
  <article_title>Tools (standard variant)</article_title>
  <total_sources>9</total_sources>
  <total_artefacts>23</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>42</n_orphan_anchors>
  <n_content_sections>9</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="building-ai-agents-from-scratch-part-1-tool-use" type="golden_web">**Main topic:** Building AI agents from scratch in Python to implement tool-use capability without LLM orchestration frameworks. The article covers AI agent basics (LLM as reasoning engine for planning, memory via system prompts, and tools), high-level tool mechanics, a `@tool` decorator for metadata extraction, JSON-structured system prompts enforcing response schemas, and a full `Agent` class for planning/executing tool calls. **Key concepts:** Agents decide actions via LLM reasoning rather than running code directly. Tools are Python functions wrapped to expose `name`, `description` (from docstring), `parameters` (from type hints + parsed docstrings), and callable `func`. The system prompt supplies tool definitions plus a strict JSON `response_format` schema requiring `requires_tools` (boolean), optional `direct_response`, `thought`, `plan` (array), and `tool_calls` (array of `{tool, args}`). Few-shot examples distinguish tool-needed vs. direct-answer cases. The agent loops over sequential tool calls when required. **Concrete examples, tools, frameworks, APIs, techniques:** - `@tool(name=None)` decorator using `inspect.signature`, `get_type_hints`, `inspect.getdoc`, and custom `parse_docstring_params`/`get_type_description` (handling `Literal`). - `Tool` dataclass with `__call__`. - `convert_currency(amount: float, from_currency: str, to_currency: str)` tool calling `https://open.er-api.com/v6/latest/{from_currency}` via `urllib.request` + `json`. - `Agent` class methods: `__init__` (OpenAI client), `add_tool`, `get_available_tools`, `use_tool`, `create_system_prompt` (builds full JSON), `plan` (gpt-4o-mini call at temperature=0), `execute` (runs plan or returns direct response). - OpenAI SDK (`openai.OpenAI`, `chat.completions.create`, model="gpt-4o-mini"); `json.dumps` for prompt; example queries test RSD→JPY conversion (returns "1500 RSD = 2087.49 JPY") vs. casual greeting. **Specific claims:** LLM never executes code; performance depends on precise system-prompt formatting and tool descriptions. Example run shows correct `requires_tools=True/False` routing and single-tool execution. **Notable limitations/gaps:** Covers only one tool and sequential calls (no parallel or multi-tool orchestration); requires rigidly formatted docstrings; no memory, long-term state, error recovery beyond try/except, or evaluation; prompt is hardcoded and lengthy; limited to currency API example. The source includes a full `Agent.execute` tool-loop implementation and the complete JSON system prompt with three examples.</s>
<s slug="efficient-tool-use-with-chain-of-abstraction-reasoning" type="golden_web">Chain-of-Abstraction (CoA) reasoning trains LLMs to generate multi-step chains containing abstract placeholders (e.g., y1, y2) before any tool calls, then reifies each chain once with domain tools to insert concrete results. This decouples general reasoning strategies from instance-specific knowledge, enabling holistic planning of interconnected tool calls and parallel execution of decoding across examples while tools run for prior traces. Fine-tuning data is built by prompting LLaMa-70B to rewrite gold answers from GSM8K, ASDiv, and HotpotQA into CoA traces, followed by verification that tools can correctly infill placeholders. In the math domain, an equation solver extracts bracketed derivations, forms a system of equations, and solves it with the SymPy toolkit. In the Wiki QA domain, a BM25 retriever indexes the KILT Wikipedia dump, re-ranks top-10 results with Sentence-BERT cosine similarity, and SpaCy (en_core_web_sm) performs NER aggregated into six classes to bridge successive WikiSearch queries. Evaluations use LLaMa-2 and LLaMa-2-Chat (7B/70B) against CoT-FSP, CoT-FT, Toolformer, Toolformer-Math, Toolformer-Wiki, and FireAct. On GSM8K and ASDiv, CoA yields average absolute accuracy gains of ~7.5 %; on HotpotQA it improves ~4.5 %. Zero-shot gains appear on SVAMP, MAWPS, WebQuestions, NaturalQuestions, and TriviaQA. Inference speed reaches ~1.47× (math) and ~1.33× (Wiki QA) versus interleaved baselines because tool calls occur only after full abstract traces are decoded. Human evaluation on 200 GSM8K samples reports ~8 % fewer reasoning errors and zero arithmetic errors. Stratified results show largest gains on questions requiring more than three reasoning steps. The source includes a table of reasoning-step distribution in math fine-tuning data, tables of CoA re-writing examples, tables of SpaCy NER type aggregation, and tables of per-model accuracy and wall-clock time. Limitations noted are restriction to two English-language domains and requirement for full-parameter fine-tuning.</s>
<s slug="function-calling-with-openai-s-api" type="golden_web">Function calling (tool calling) enables OpenAI models to interface with external systems via tools defined in API requests. The guide covers function tools (JSON schema), custom tools (free-form text), and built-in tools, plus tool search for large toolsets (supported only on gpt-5.4+). Key concepts include tools (e.g., get_weather with location parameter), tool calls returned by the model, and tool call outputs supplied by the application. The five-step flow comprises sending tools with the initial prompt, receiving tool calls, executing them locally, returning outputs, and obtaining a final model response. Functions use a schema with type, name, description, parameters (JSON Schema), and optional strict flag. Namespaces group tools (e.g., crm, billing). Tool search defers loading via a dedicated tool. Concrete examples include a complete get_horoscope flow (67-line Python, 69-line JavaScript), get_weather JSON schema (22 lines), namespace definitions (35 lines), pydantic/zod schema conversion helpers, multi-call handling, and streaming accumulation of deltas. Responses and Chat Completions APIs are shown for both function and custom tools. Custom tools support Lark or regex context-free grammars to constrain outputs (e.g., math_exp, timestamp examples). Specific claims cover token billing of tool definitions, recommendation of &lt;20 functions per turn, strict mode enforcement (additionalProperties:false, all properties required), tool_choice modes (auto, required, specific function, allowed_tools), parallel_tool_calls (disabled for built-ins and fine-tunes in some cases), and streaming events (response.output_item.added, response.function_call_arguments.delta). Best-practice lists address descriptions, enums, least-surprise design, and offloading logic. Notable limitations include unsupported JSON Schema features under strict mode, grammar complexity causing rejections or out-of-distribution outputs, lack of parallel calls with built-ins, higher latency for varying schemas on fine-tunes, and model-specific behaviors (e.g., gpt-4.1-nano-2025-04-14). The source includes a 23-line Python tool-loop example and multiple streaming/response accumulation snippets.</s>
<s slug="function-calling-with-the-gemini-api" type="golden_web">Function calling with the Gemini API enables models to connect to external tools and APIs by outputting structured function calls instead of (or alongside) text. The source covers three primary use cases: Augment Knowledge (external databases/APIs), Extend Capabilities (computations such as calculators or charts), and Take Actions (scheduling, email, device control). The workflow consists of four steps: (1) define a function declaration using a subset of the OpenAPI schema, (2) send the declaration(s) inside a `types.Tool` (or equivalent JSON) with the user prompt to a model such as `gemini-3-flash-preview`, (3) execute the function locally when the response contains a `functionCall` object that includes `name`, `args`, and `id`, and (4) return the result in a `functionResponse` part that references the matching `id`. Concrete examples include `schedule_meeting` (with required `attendees`, `date`, `time`, `topic`), `set_light_values` (brightness 0-100 + `color_temp` enum), `power_disco_ball`, `start_music`, `dim_lights`, `get_weather_forecast`, `set_thermostat_temperature`, and `get_image`. Code samples are shown for the Python `google.genai` SDK, the JavaScript `@google/genai` SDK, and raw REST. The Python SDK additionally supports automatic function calling via `GenerateContentConfig(tools=[python_function])`, which converts callables (with type hints and Google-style docstrings) and manages the full loop. Advanced features include parallel function calling (multiple independent calls in one turn), compositional/sequential calling (chained calls such as location then weather), multi-tool use that combines custom declarations with built-in tools such as `google_search` or `code_execution` (via `Tool(google_search=..., function_declarations=...)` and `include_server_side_tool_invocations=True`), and multimodal function responses (images or PDFs supplied as nested `inlineData` parts with `displayName` references). Function-calling modes are controlled by `FunctionCallingConfig`: `AUTO` (default), `ANY` (force a call), `VALIDATED` (schema adherence when mixed tools are present), and `NONE`. Gemini 3 and 2.5 thinking models improve accuracy; manual history management requires preserving `thought_signature` parts. The source includes a 9-line table of supported models and their parallel/compositional capabilities (ARTEFACT_A21). It also demonstrates Model Context Protocol (MCP) integration via `mcpToTool` or passing an `mcp.ClientSession` directly, and notes compatibility with structured output. Notable limitations include: automatic function calling and direct Python-callable tools are Python-SDK only; MCP support is experimental and limited to tools (not resources or prompts); only a subset of the OpenAPI schema is accepted; `ANY` mode may reject very large or deeply nested schemas; parameter types in Python are restricted; and function descriptions count toward the input token limit.</s>
<s slug="ApoDzZP8_ck" type="golden_youtube">The video explains the Tool Pattern for agentic systems by implementing tool calling from scratch, focusing on mechanics rather than framework usage. A tool is defined as a Python function enabling an LLM to access external data beyond its weights, such as via APIs or web content. The approach uses a system prompt with XML `<tools>` tags to define function signatures (name, description from docstring, parameters with types) and `<tool_call>` tags for LLM responses specifying name and arguments. Key implementation covers a Jupyter Notebook with `get_current_weather` (returns dict with temperature/unit for locations like Madrid), `parse_tool_call_xml_str` for extracting and JSON-parsing calls, and chat history appending of observations before a final LLM response. VS Code modules include `tool.py` (with `get_fs_signature` for schema extraction, `Tool` class holding name/function/signature, and `@tool` decorator to auto-convert functions) and `tool_agent.py` (ToolAgent class using Llama 3 70B tool-use model via Groq client, list of tools, `run` method for prompt handling, first LLM call, argument validation against signatures, tool execution, and final natural-language output). Practical example: `fetch_top_hacker_news_stories` (fetches top N stories with URLs from Hacker News API). Frameworks referenced: LangChain, Llama Index, CrewAI. No benchmarks or performance data are provided. Coverage gaps include lack of error handling details, multi-tool orchestration examples, and production robustness; the implementation is explicitly noted as simplified and non-framework. Includes a 23-line Python tool-loop example and a 15-line Hacker News tool demonstration.</s>
<s slug="towardsai_course-ai-agents" type="golden_code">Lesson 6 covers **Tools (Function Calling)** as a core AI agent building block using the `google-genai` library and `gemini-2.5-flash` model. It demonstrates bridging LLMs to external systems via three implementation approaches. Key concepts include the tool-calling cycle (prompt + declarations → LLM `function_call` → handler execution → result return), custom metadata schemas, and structured extraction. Concrete techniques: manual JSON schemas for `search_google_drive`, `send_discord_message`, and `summarize_financial_report` (with exact parameter definitions); `@tool` decorator (using `inspect.signature`) that auto-generates schemas into `ToolFunction` objects; Gemini native API via `types.Tool(function_declarations=[types.FunctionDeclaration(...)])`, `GenerateContentConfig` with `tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY"))`, and `call_tool` handling of `FunctionCall` objects. Pydantic integration treats `DocumentMetadata` (fields: `summary`, `tags`, `keywords`, `quarter`, `growth_rate`) as an extraction tool using `model_json_schema()`. A tool-loop implementation maintains conversation history (`messages` appending `Part.from_function_response`), runs up to 3 iterations on multi-step prompts (e.g., drive search → summarize → Discord send), and includes a 23-line Python tool-loop example. The notebook uses a fixed Q3 2023 financial document (20% revenue growth, 15% engagement, 25% digital services, 92% retention) for all examples. Limitations noted: loop forces immediate next calls without explicit reasoning steps, motivating ReAct patterns. No production benchmarks or error-handling coverage provided.</s>
<s slug="agentic-design-patterns-part-3-tool-use" type="exploitation">Tool Use enables LLMs in agentic workflows to request external functions for information gathering, action, or data manipulation rather than relying solely on transformer token generation. The pattern is implemented by fine-tuning or few-shot prompting models to emit special call strings (exact format implementation-dependent), followed by post-processing that detects the string, executes the referenced function, and injects results back into context. Concrete examples include a web-search tool invoked via _{tool: web-search, query: "coffee maker reviews"}_ to answer reviewer-based product questions, and a python-interpreter tool invoked via _{tool: python-interpreter, code: "100 * (1+0.07)**12"}_ for compound-interest calculations. Additional supported operations encompass searches over web, Wikipedia, and arXiv; productivity-tool interfaces such as send email and read/write calendar entries; and image generation or interpretation. Systems may expose hundreds of tools; when context limits are exceeded, heuristics select the relevant subset, as described in the Gorilla paper. Pre-LMM practice (prior to LLaVa, GPT-4V, and Gemini) required computer-vision Tool Use for any image manipulation. GPT-4 function calling, released mid-2023, provided a general-purpose implementation; subsequent LLMs have adopted similar capabilities. The source cites three papers: “Gorilla: Large Language Model Connected with Massive APIs” (Patil et al., 2023), “MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action” (Yang et al., 2023), and “Efficient Tool Use with Chain-of-Abstraction Reasoning” (Gao et al., 2024). It also includes a 23-line Python tool-loop example. No quantitative benchmarks, accuracy deltas, or latency figures are reported. The text notes that Tool Use and Reflection patterns operate reliably in current applications while Planning and Multi-agent collaboration remain less mature. Coverage is limited to high-level workflow descriptions and does not address implementation details such as error handling, parallel tool calls, or security boundaries.</s>
<s slug="h8gMhXYAv1k" type="exploitation">Tool calling enables LLMs to interact with external real-time data sources by recommending actions that a client application then executes. The process begins with the client sending messages plus a tool definition (containing name, description, and input parameters) to the LLM; the LLM responds with a recommended tool to invoke, after which the application executes the tool and returns the result for the LLM to interpret or chain into further calls. Traditional tool calling places full responsibility on the client application for tool definition and execution. The video illustrates this with a weather query ("temp in Miami?") using a Weather API tool; the LLM returns a tool call that the application executes against the API, receives the response (71°), and forwards it back, allowing the LLM to produce the final answer. Tools can include APIs, databases, or code executed via a code interpreter. Embedded tool calling inserts a library or framework between the application and LLM. The library manages both tool definition and tool execution, automatically appending definitions to messages, handling LLM-recommended calls, retrying on failure, and returning only the final answer to the application. This approach is presented as mitigating hallucination and incorrect tool calls that occur in the traditional variant. No concrete frameworks, libraries, or APIs beyond the generic Weather API example are named. No benchmarks, performance metrics, or quantitative claims appear. The source notes that traditional tool calling can produce hallucinations or malformed calls but provides no mitigation details beyond switching to the embedded pattern. No code samples, implementation details, or evaluation results are supplied.</s>
<s slug="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen" type="exploitation">ReAct and Plan-and-Execute are two LLM agent reasoning patterns compared via LangChain implementations. ReAct uses an iterative loop of Thought, Action (selected from tool_names), Action Input, Observation, and Final Answer. Plan-and-Execute separates a planner that outputs numbered steps from an executor that processes each step with tools. Prompt templates shown are REACT_PROMPT (with {tools}, {tool_names}, {input}, {agent_scratchpad}), PLANNER_PROMPT, and EXECUTOR_PROMPT (with {plan}, {current_step}, {previous_results}). LangChain code examples include: initialize_agent with AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION and Tool objects (Search, Calculator); PlanAndExecute with create_planner and create_executor; create_csv_agent on sales_data.csv; PythonAstREPLTool and CSVTool. Both patterns are demonstrated on the query "What is the population of China multiplied by 2?" and a CSV sales statistics task (total sales, best product, summary report) using ChatOpenAI(temperature=0). Performance comparison table covers metrics for ReAct and Plan-and-Execute. Cost analysis table details GPT-4 token consumption and API costs for complex tasks. Selection guidance matches ReAct to simple, real-time, or cost-sensitive tasks and Plan-and-Execute to multi-step, high-accuracy, or long-term planning tasks, with hybrid and caching recommendations. The source includes a 23-line Python tool-loop example for ReAct and equivalent Plan-and-Execute scaffolding but omits raw table values, latency numbers, token counts, and any evaluation against non-LangChain baselines or other agent frameworks.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 3 | 4 | 0 |
| S2::section-2-understanding-why-agents-need-tools | 1 | 4 | 0 |
| S3::section-3-implementing-tool-calls-from-scratch | 1 | 4 | 0 |
| S4::section-4-implementing-a-tool-calling-framework-from-scratch | 1 | 4 | 0 |
| S5::section-5-implementing-production-level-tool-calls-with-gemini | 2 | 3 | 0 |
| S6::section-6-using-pydantic-models-as-tools-for-on-demand-structured-outputs | 1 | 3 | 0 |
| S7::section-7-the-downsides-of-running-tools-in-a-loop | 1 | 3 | 0 |
| S8::section-8-popular-tools-used-within-the-industry | 2 | 3 | 0 |
| S9::section-9-conclusion | 2 | 3 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="yes" sources="ApoDzZP8_ck,h8gMhXYAv1k,efficient-tool-use-with-chain-of-abstraction-reasoning" artefacts="">
  <intent>Introduce the lesson by referencing prior workflow concepts and transitioning to tool calling as the bridge to agent action.</intent>
  <depth_checklist depth_score="1">
    <item name="motivation" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly supports lesson anchoring to prior concepts.</orphan>
    <orphan route="depth" anchor="Transition to what we'll learn in this lesson: After presenting what we learned in the past, make a transition to what w" bullet="motivation">Directly supports lesson anchoring to prior concepts.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-understanding-why-agents-need-tools" self_contained="yes" sources="h8gMhXYAv1k,ApoDzZP8_ck,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Explain the core limitation of LLMs and why tools are required to enable external interaction.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="theoretical_foundations" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="9" n_breadth="0" n_unreachable="1">
    <orphan route="depth" anchor="Before showing how to implement tool calling from scratch and with Gemini, explain in more depth why LLMs need tools in" bullet="motivation">Core theoretical motivation for the section.</orphan>
    <orphan route="depth" anchor="LLMs have one fundamental limitation. They are simple pattern matchers and text generators. They cannot, by themselves," bullet="theoretical_foundations">Direct theoretical foundation.</orphan>
    <orphan route="depth" anchor="Analogy: The LLM is the brain, while the tools are an LLM's "hands and senses," allowing it to perceive and act in the w" bullet="cross_domain_analogies">Explicit analogy provided.</orphan>
    <orphan route="depth" anchor="Thus, tools are the bridge between the LLM's internal reasoning and the external world. With the power of tools, the LLM" bullet="theoretical_foundations">Core theoretical foundation.</orphan>
    <orphan route="unreachable" anchor="Use a representative image from the research to explain at a high level how tools work." bullet="motivation">Pure lookup for non-text element.</orphan>
    <orphan route="depth" anchor="Examples of popular tools that power modern AI agents:" bullet="motivation">Lists concrete tool examples.</orphan>
    <orphan route="depth" anchor="Access real-time information through APIs (e.g., today's weather, latest news)." bullet="motivation">Specific tool category example.</orphan>
    <orphan route="depth" anchor="Interact with external databases or other storage solutions (PostgreSQL database, Snowflake data warehouse, S3 data lake" bullet="motivation">Specific tool category example.</orphan>
    <orphan route="depth" anchor="Access agent's long-term memory to remember information beyond their context window" bullet="motivation">Specific tool category example.</orphan>
    <orphan route="depth" anchor="Execute code (Python, JavaScript)" bullet="motivation">Specific tool category example.</orphan>
    <orphan route="depth" anchor="Perform precise calculations beyond their training data (basic math calculations, sorting, filtering, grouping, etc.)" bullet="motivation">Specific tool category example.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-implementing-tool-calls-from-scratch" self_contained="yes" sources="towardsai_course-ai-agents,function-calling-with-openai-s-api,function-calling-with-the-gemini-api" artefacts="">
  <intent>Walk through manual implementation of tool schemas, registry, prompting, and execution loop.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="17" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="The best way to understand how tools work and how LLMs use them is by implementing them from scratch. That's why the res" bullet="motivation">Section motivation statement.</orphan>
    <orphan route="depth" anchor="Before going into the code, quickly list what we will learn in this section, such as how a tool is defined, how their sc" bullet="technical_nuances">Technical outline of section.</orphan>
    <orphan route="depth" anchor="Next provide a summary of our end goal, which is to provide the LLM with a list of available tools and let it decide whi" bullet="theoretical_foundations">Core goal of tool calling.</orphan>
    <orphan route="depth" anchor="Provide a mermaid diagram illustrating the 5 steps from above, highlighting the request-execute-respond flow of calling" bullet="technical_nuances">Flow diagram request.</orphan>
    <orphan route="depth" anchor="Now, let's dig into the code. To make it interesting, we will implement a simple example where we mock searching documen" bullet="motivation">Implementation start.</orphan>
    <orphan route="depth" anchor="Using the code examples from the provided Notebook within the <research> tag, use all the code from the `2. Implementing" bullet="technical_nuances">Code usage directive.</orphan>
    <orphan route="depth" anchor="Here is how you should use the code from the `2. Implementing tool calls from scratch` section of the provided Notebook" bullet="technical_nuances">Detailed code mapping.</orphan>
    <orphan route="depth" anchor="The tool usage guidelines" bullet="technical_nuances">Prompt component.</orphan>
    <orphan route="depth" anchor="The tool call format" bullet="technical_nuances">Prompt component.</orphan>
    <orphan route="depth" anchor="The response behavior" bullet="technical_nuances">Prompt component.</orphan>
    <orphan route="depth" anchor="The list of available tools enclosed by XML tags" bullet="technical_nuances">Prompt component.</orphan>
    <orphan route="depth" anchor="Based on the `description` field from the tool schema, the LLM *decides* if a tool call is appropriate to fulfill the us" bullet="theoretical_foundations">Decision mechanism.</orphan>
    <orphan route="depth" anchor="Another disambiguation method when working with AI agents is to be as clear as possible in the system prompts, verbosely" bullet="technical_nuances">Disambiguation technique.</orphan>
    <orphan route="depth" anchor="By defining clear tool descriptions and system prompts, you ensure the AI agent will be able to make the necessary match" bullet="technical_nuances">Scaling note.</orphan>
    <orphan route="depth" anchor="Based on the selected tool, it then *generates* the function name and arguments as structured outputs such as JSON or Py" bullet="technical_nuances">Generation step.</orphan>
    <orphan route="depth" anchor="Add a quick note specifying that the LLM is specially tuned through instruction fine-tuning to interpret tool schema inp" bullet="technical_nuances">Fine-tuning note.</orphan>
    <orphan route="depth" anchor="Conclude by saying that this is the basic concept behind tool calling." bullet="motivation">Section conclusion.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-implementing-a-tool-calling-framework-from-scratch" self_contained="yes" sources="towardsai_course-ai-agents,agentic-design-patterns-part-3-tool-use,function-calling-with-openai-s-api" artefacts="">
  <intent>Introduce @tool decorator to auto-generate schemas and reduce manual repetition.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="technical_nuances" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="10" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Manually defining schemas for every tool we want to use can quickly become cumbersome and hard to scale. That's why all" bullet="motivation">Motivation for decorator.</orphan>
    <orphan route="depth" anchor="Thus, in our writing from scratch exercise, as a natural progression to defining the tool schemas manually, we will impl" bullet="motivation">Progression statement.</orphan>
    <orphan route="depth" anchor="The end goal is to decorate a function with the `@tool` decorated and based on the function's docstring and signature (i" bullet="technical_nuances">Decorator goal.</orphan>
    <orphan route="depth" anchor="This method also follows good software engineering principles, as we respect the Don't Repeat Yourself (DRY) software pr" bullet="implementation_tradeoffs">DRY principle.</orphan>
    <orphan route="depth" anchor="Now, let's dig into the code and rewrite the implementation from the previous section using `@tool` decorators." bullet="motivation">Code transition.</orphan>
    <orphan route="depth" anchor="Using the code examples from the provided Notebook within the <research> tag, use all the code from the `3. Implementing" bullet="technical_nuances">Code usage directive.</orphan>
    <orphan route="depth" anchor="Here is how you should use the code from the `3. Implementing a tool calling framework from scratch` section of the prov" bullet="technical_nuances">Detailed code mapping.</orphan>
    <orphan route="depth" anchor="type (highlight that now it's `ToolFunction` instead of a normal Python function)" bullet="technical_nuances">Inspection point.</orphan>
    <orphan route="depth" anchor="schema (highlight that it's identical with the one manually defined by us)" bullet="technical_nuances">Inspection point.</orphan>
    <orphan route="depth" anchor="functional handler (highlight that this is how we access the function handler now)" bullet="technical_nuances">Inspection point.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-implementing-production-level-tool-calls-with-gemini" self_contained="yes" sources="function-calling-with-the-gemini-api,ApoDzZP8_ck,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Show native Gemini SDK usage to replace manual prompting and schema handling.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
<section id="S6::section-6-using-pydantic-models-as-tools-for-on-demand-structured-outputs" self_contained="yes" sources="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen,h8gMhXYAv1k,function-calling-with-openai-s-api" artefacts="">
  <intent>Demonstrate Pydantic models as dynamic structured-output tools inside agent loops.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
<section id="S7::section-7-the-downsides-of-running-tools-in-a-loop" self_contained="yes" sources="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen,agentic-design-patterns-part-3-tool-use,efficient-tool-use-with-chain-of-abstraction-reasoning" artefacts="">
  <intent>Show sequential loop implementation then highlight its limitations that motivate ReAct.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="theoretical_foundations" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="technical_nuances" present="yes" evidence="efficient-tool-use-with-chain-of-abstraction-reasoning"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
<section id="S8::section-8-popular-tools-used-within-the-industry" self_contained="yes" sources="ApoDzZP8_ck,agentic-design-patterns-part-3-tool-use,h8gMhXYAv1k" artefacts="">
  <intent>Catalog real-world tool categories to ground the lesson in industry practice.</intent>
  <depth_checklist depth_score="1">
    <item name="motivation" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
<section id="S9::section-9-conclusion" self_contained="yes" sources="ApoDzZP8_ck,h8gMhXYAv1k,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Reinforce tool calling as foundational and preview planning/ReAct lessons.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="theoretical_foundations" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0">
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="13" need_breadth="6" target_words="135" mandatory_bullets="2" must_cover_depth="0" must_stay_brief="0"/>
  <section id="S2::section-2-understanding-why-agents-need-tools" need_depth="33" need_breadth="5" target_words="310" mandatory_bullets="6" must_cover_depth="1" must_stay_brief="0"/>
  <section id="S3::section-3-implementing-tool-calls-from-scratch" need_depth="56" need_breadth="6" target_words="930" mandatory_bullets="25" must_cover_depth="20" must_stay_brief="0"/>
  <section id="S4::section-4-implementing-a-tool-calling-framework-from-scratch" need_depth="35" need_breadth="6" target_words="560" mandatory_bullets="11" must_cover_depth="9" must_stay_brief="0"/>
  <section id="S5::section-5-implementing-production-level-tool-calls-with-gemini" need_depth="6" need_breadth="6" target_words="390" mandatory_bullets="14" must_cover_depth="12" must_stay_brief="0"/>
  <section id="S6::section-6-using-pydantic-models-as-tools-for-on-demand-structured-outputs" need_depth="6" need_breadth="6" target_words="315" mandatory_bullets="6" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S7::section-7-the-downsides-of-running-tools-in-a-loop" need_depth="4" need_breadth="6" target_words="520" mandatory_bullets="9" must_cover_depth="6" must_stay_brief="0"/>
  <section id="S8::section-8-popular-tools-used-within-the-industry" need_depth="7" need_breadth="5" target_words="340" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S9::section-9-conclusion" need_depth="6" need_breadth="6" target_words="90" mandatory_bullets="2" must_cover_depth="0" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S4::section-4-implementing-a-tool-calling-framework-from-scratch, S3::section-3-implementing-tool-calls-from-scratch</weakest_sections>
    <strongest_sections>S7::section-7-the-downsides-of-running-tools-in-a-loop, S5::section-5-implementing-production-level-tool-calls-with-gemini</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>