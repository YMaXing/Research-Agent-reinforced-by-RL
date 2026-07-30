<digest_meta>
  <article_title>Tools (minimal variant)</article_title>
  <total_sources>9</total_sources>
  <total_artefacts>23</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>47</n_orphan_anchors>
  <n_content_sections>9</n_content_sections>
  <external_evidence_policy>forbidden</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="building-ai-agents-from-scratch-part-1-tool-use" type="golden_web">Main topic is implementing AI agent tool use from scratch in Python without orchestration frameworks. Core concepts include AI agents as LLM-driven systems for planning, memory, and tool invocation; tool definitions passed via system prompt rather than direct code execution; and strict JSON output schemas for deciding when to call tools versus respond directly. Key techniques cover a @tool decorator that wraps functions into Tool instances using docstring parsing and type hints; parse_docstring_params and get_type_description helpers; a Tool dataclass holding name, description, callable, and parameters; and JSON-structured system prompts containing role, capabilities, instructions, tool schemas, response_format with requires_tools/plan/tool_calls fields, and few-shot examples. Concrete implementation uses the convert_currency function (decorated, calling https://open.er-api.com/v6/latest/ via urllib) as the sole example tool. The Agent class provides add_tool, use_tool, create_system_prompt, plan (gpt-4o-mini at temperature 0), and execute methods that loop over sequential tool_calls. Includes a 23-line Python tool-loop example in execute and a full notebook/GitHub reference at swirl-ai/ai-angineers-handbook. No quantitative benchmarks or performance claims are present. Coverage gaps include multi-tool orchestration, memory persistence, error recovery beyond basic try/except, alternative models or APIs, and production deployment details.</s>
<s slug="efficient-tool-use-with-chain-of-abstraction-reasoning" type="golden_web">Chain-of-Abstraction (CoA) reasoning trains LLMs to first emit abstract reasoning chains containing placeholders (e.g., y1, y2) before any domain tool is invoked, then reify the completed chain with tool results in one pass. This decouples general planning from instance-specific knowledge, enabling parallel tool calls and amortization of latency across a batch. Fine-tuning data is built by prompting LLaMa-70B to rewrite gold answers from GSM8K+ASDiv (math) and HotpotQA (Wiki QA) into labeled CoA traces, then verifying each trace with domain tools; 76.6 % of math traces and 15.9 % of Wiki traces pass verification. The resulting data contain explicit connections between steps via repeated placeholders. Domain tools are an equation solver that extracts bracketed derivations, assembles them into a SymPy system, and substitutes solved values; a BM25 retriever over the KILT Wikipedia dump followed by Sentence-BERT cosine re-ranking for WikiSearch; and SpaCy (en_core_web_sm) whose 18 NER types are collapsed to six classes for entity bridging. After reification, a second LLM produces the final answer from the filled chain. On LLaMa-2 and LLaMa-2-Chat (7 B/70 B), CoA yields average absolute gains of 7.5 % on math and 4.5 % on Wiki QA versus CoT-FSP, CoT-FT, Toolformer, and FireAct, with larger margins on out-of-distribution sets (SVAMP, MAWPS, NQ, TriviaQA) and on questions requiring >3 steps. Human evaluation on 200 GSM8K items reports zero arithmetic errors and ~8 % fewer reasoning errors. Inference is 1.47× faster on math and 1.33× faster on Wiki QA because full abstract chains are decoded before any tool call and subsequent examples can be decoded while prior tool results are fetched. The source includes a 5-line table of reasoning-step distribution, an 11-line table of Wiki QA CoA examples, an 8-line SpaCy type aggregation table, multiple 14–18-line result tables, a 6-line human-error table, and 30-line prompting templates for data construction. It does not cover LoRA-style parameter-efficient tuning, non-English data, or domains beyond math and Wikipedia QA.</s>
<s slug="function-calling-with-openai-s-api" type="golden_web">Function calling (tool calling) enables OpenAI models to interface with external systems via tools. The guide covers function tools defined by JSON schema and custom tools accepting free-form text, plus built-in tools for web search, code execution, and MCP servers. Only gpt-5.4 and later support tool_search for deferred loading of large tool sets. The flow consists of five steps: send request with tools, receive tool call(s), execute locally, return function_call_output (string or image/file array) referencing call_id, and receive final model response. Function definitions require type: "function", name, description, parameters (JSON Schema), and optional strict. Namespaces group tools (e.g., crm, billing). Pydantic and Zod helpers convert objects to schemas (limited feature support). Best practices include detailed names/descriptions, enums, least-surprise design, avoiding known-argument parameters, keeping initial functions under 20, and using the Playground for schema iteration. Function definitions consume input tokens; tool_search or fine-tuning can reduce usage. tool_choice options are "auto" (default), "required", {"type":"function","name":"..."}, "none", or allowed_tools (with mode). parallel_tool_calls=false forces at most one call. strict:true enforces schema via Structured Outputs, requiring additionalProperties:false and all properties marked required (optional fields use null union); unsupported schema features are rejected. Responses API normalizes to strict by default; Chat Completions does not. Streaming (stream:true) returns delta.tool_calls (Chat Completions) or events (response.output_item.added, response.function_call_arguments.delta, response.function_call_arguments.done) (Responses API). Aggregation code reconstructs full arguments JSON. Custom tools (type:"custom") accept arbitrary string input. Optional format with grammar constrains output using lark or regex syntax (Rust regex crate). Supported Lark subset excludes lookarounds, lazy modifiers, templates, and most imports. Regex requires single-line patterns. Examples include code_exec, math_exp (Lark arithmetic), and timestamp (regex date-time). Source includes a 67-line Python complete tool-calling example, 69-line JavaScript equivalent, 22-line get_weather JSON schema, 35-line namespace example, 20-line Pydantic schema, 26-line multi-call response, and multiple streaming accumulation snippets. Limitations: no parallel calls with built-in tools; gpt-4.1-nano-2025-04-14 may duplicate calls; fine-tuned models disable strict on parallel calls; complex grammars rejected; no zero-data-retention for cached strict schemas.</s>
<s slug="function-calling-with-the-gemini-api" type="golden_web">Function calling with the Gemini API enables models to connect to external tools and APIs by outputting structured function calls instead of text. Primary use cases are augmenting knowledge from databases/APIs, extending capabilities (e.g., calculations), and taking actions (e.g., scheduling, device control). The flow requires defining function declarations (name, description, OpenAPI-subset parameters with types, properties, enum, required), passing them via types.Tool(function_declarations=[...]) in GenerateContentConfig, executing calls in application code, and returning results with matching id in subsequent turns. Exact examples include schedule_meeting (attendees array, date, time, topic), set_light_values (brightness int 0-100, color_temp enum daylight/cool/warm), power_disco_ball (power bool), start_music (energetic/loud bool), dim_lights (brightness number), get_weather_forecast (location), set_thermostat_temperature (temperature), getWeather (city), get_image (item_name) plus multimodal responses supporting image/png/jpeg/webp and application/pdf. SDKs shown are google.genai (Python) and @google/genai (JavaScript) with models.generate_content on gemini-3-flash-preview; REST uses /v1beta/models/gemini-3-flash-preview:generateContent. Parallel calling executes independent functions in one turn; compositional/sequential chains dependent calls (e.g., get_current_location then get_weather). Function calling modes are VALIDATED (default with other tools), AUTO (default for declarations only), ANY (force calls, optionally restricted by allowed_function_names), and NONE. Automatic function calling (Python SDK only) converts Python functions with type hints and Google-style docstrings directly into declarations and handles execution/response loops. Multi-tool use combines function_declarations with built-in tools such as google_search via Tool(google_search=..., function_declarations=...). Model Context Protocol (MCP) support via mcpToTool(session) or tools=[session] provides automatic calling for MCP tools. Thinking models (Gemini 3/2.5) use thought signatures for context; manual history must preserve them exactly. Includes a 23-line Python tool-loop example, a 9-line model capabilities table covering calling/parallel/compositional support, and code for from_callable schema conversion. Notable limitations: only a subset of OpenAPI schema is supported; automatic calling and full MCP integration are Python/JavaScript SDK features only and experimental; ANY mode may reject large/nested schemas; Dict types are unsupported; function descriptions count toward token limits; pre-Gemini-3 models require Live API for some combinations.</s>
<s slug="ApoDzZP8_ck" type="golden_youtube">The video explains the Tool Pattern for LLM agents by implementing tool calling from scratch, showing how LLMs access external data beyond model weights via Python functions. Core mechanism: a system prompt defines available tools inside &lt;tools&gt; XML tags (with name, description from docstring, parameters, and types), the LLM returns calls inside &lt;tool_call&gt; tags (name + arguments), a parser extracts and converts them to dicts via parse_tool_call_xml_str, the function executes, and the result is appended as an observation to chat history for a final natural-language response. Key components include the dummy get_current_weather(location, unit) function (hardcoded Madrid=25°C output) and the practical fetch_top_hacker_news_stories(n) example that retrieves top Hacker News stories with URLs. The VS Code implementation adds tool.py (with get_function_signature for schema extraction and the @tool decorator that wraps functions into Tool objects holding name/function/signature) and tool_agent.py (ToolAgent class accepting a tools list, using the Llama 3 70B tool-use model via Groq client, with a run() method that builds chat histories, validates argument types against signatures, executes via a tools dict lookup, and handles the full loop). The notebook demonstrates the end-to-end flow with the tool-use fine-tune; the agent code mirrors LangChain/LlamaIndex/CrewAI abstractions without creating a new framework. Coverage gaps include no multi-tool parallel calls, no error handling for invalid calls, and hardcoded prompt elements in the minimal notebook example.</s>
<s slug="towardsai_course-ai-agents" type="golden_code">**Main topic and key concepts:** Lesson 6 covers Tools (Function Calling) as a core AI agent building block. It teaches implementing LLM interaction with external systems via google-genai and Gemini models, building a custom tool framework with decorators (modeled on LangGraph), using Gemini's native API, Pydantic-based structured extraction, and multi-step tool loops. The flow is: send prompt + tool schemas, parse function_call, execute handler, return result to LLM. **Concrete examples, tools, frameworks, APIs:** Uses gemini-2.5-flash (MODEL_ID), google-genai client, types.Tool/FunctionDeclaration/GenerateContentConfig with function_calling_config(mode="ANY"). Mock tools: search_google_drive(query), send_discord_message(channel_id, message), summarize_financial_report(text) with JSON schemas. @tool decorator auto-generates schemas from signatures/docstrings via inspect.signature. Pydantic DocumentMetadata (summary, tags, keywords, quarter, growth_rate) treated as extract_metadata tool. Includes a tool-loop implementation (max_iterations=3) appending user prompt, function_call, and Part.from_function_response results. **Specific data points/claims:** Demonstrates sequential execution on a Q3 2023 financial document (20% revenue growth, 15% engagement, 25% digital services, 92% retention); tool loop completes search → summarize → Discord send. Native Gemini API avoids custom system prompts for optimized calling. Custom scratch implementation and decorator variant both produce valid tool_call JSON. **Notable limitations/gaps:** The loop forces immediate next calls without explicit reasoning pauses between tool results and decisions. No handling of parallel calls, error recovery, or production auth (e.g., real Google Drive/Discord APIs). Coverage ends by noting these constraints motivate ReAct patterns in the next lesson; includes a 23-line Python tool-loop example.</s>
<s slug="agentic-design-patterns-part-3-tool-use" type="exploitation">Tool Use is a core design pattern for AI agentic workflows in which an LLM receives descriptions of external functions and generates structured requests to invoke them for information retrieval, actions, or data manipulation. The pattern extends beyond basic web search or code execution by allowing an LLM to select from many tools via detailed function descriptions (purpose plus argument schemas) supplied in context; the model emits a special call string such as {tool: web-search, query: "coffee maker reviews"} or {tool: python-interpreter, code: "100 * (1+0.07)**12"}, after which a post-processor executes the function and returns results as additional context. Concrete techniques include few-shot prompting or fine-tuning to produce the call syntax, retrieval-style heuristics (described in the Gorilla paper) that select a relevant subset of tools when hundreds are available, and interfaces to productivity tools such as send-email or read/write-calendar. Early vision work relied on Tool Use because pre-LMM systems (before LLaVa, GPT-4V, Gemini) could not process images natively and therefore invoked separate object-recognition or manipulation functions. GPT-4’s function-calling release in mid-2023 provided a general-purpose implementation that subsequent LLMs have adopted. Recommended references are the Gorilla paper (Patil et al., 2023) on connecting LLMs to massive APIs, MM-REACT (Yang et al., 2023) on multimodal reasoning and action, and Efficient Tool Use with Chain-of-Abstraction Reasoning (Gao et al., 2024). The source states that both Tool Use and Reflection now operate reliably in applications, while Planning and multi-agent collaboration remain less mature. No quantitative benchmarks, accuracy numbers, or runtime measurements are supplied. The source is an overview letter and therefore omits implementation-level details such as exact parser formats, error-handling loops, or production deployment patterns.</s>
<s slug="h8gMhXYAv1k" type="exploitation">Tool calling enables LLMs to recommend actions on real-time data sources (APIs, databases, code) during chat interactions. In the traditional flow, the client application sends messages plus a tool definition (name, description, input parameters) to the LLM; the LLM returns a recommended tool call; the application executes it (e.g., Weather API for "temp in Miami?") and supplies the response ("71°") back to the LLM for final output or further calls. Tools explicitly include APIs, DBs, and code interpreted via code interpreter. Embedded tool calling inserts a library between the application and LLM. The library manages both tool definition and tool execution, automatically handling calls, retries, and responses so the LLM receives only the final answer (e.g., "71° in Miami"). This approach is presented as eliminating LLM hallucination and incorrect tool calls. No concrete library, framework, or API names beyond the generic "Weather API" and "code interpreter" are provided. No benchmarks, performance data, or implementation details appear. Coverage is limited to high-level diagrams and a single Miami-weather scenario; no code samples or production patterns are shown.</s>
<s slug="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen" type="exploitation">ReAct vs Plan-and-Execute compares two LLM agent reasoning patterns implemented in LangChain. ReAct uses an iterative loop of Thought, Action (selected from tool_names), Action Input, Observation, and Final Answer via the REACT_PROMPT template. Plan-and-Execute separates a planner that outputs numbered subtasks via PLANNER_PROMPT from an executor that runs steps with EXECUTOR_PROMPT, tools, plan, current_step, and previous_results. LangChain implementations include initialize_agent with AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION and Tool objects (Search, Calculator) for ReAct; PlanAndExecute with create_planner and create_executor for the alternative. Both accept ChatOpenAI(temperature=0) and run identical queries such as population multiplication. The data-analysis case uses create_csv_agent on sales_data.csv for ReAct and PlanAndExecute with PythonAstREPLTool plus CSVTool('sales_data.csv') to compute totals, identify top products, and produce reports. Performance comparison appears in a 6-line table of metrics (response time, accuracy) for ReAct versus Plan-and-Execute. Cost analysis for GPT-4 on complex tasks appears in a 5-line table of token consumption and API costs. Selection guidance lists ReAct for single-objective, real-time, or token-limited tasks and Plan-and-Execute for multi-step, high-accuracy, or long-horizon work, plus hybrid, caching, and parallel-execution recommendations. The source supplies prompt templates, full create_react_agent and create_plan_and_execute_agent functions, and the CSV case code but omits raw numerical values from the two tables.</s>
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
  <intent>Introduce the lesson by referencing prior workflow concepts and transitioning to tool calling as the mechanism that turns LLMs into agents capable of external action.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="efficient-tool-use-with-chain-of-abstraction-reasoning"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly supports lesson anchoring to prior workflow lessons.</orphan>
    <orphan route="depth" anchor="Transition to what we'll learn in this lesson: After presenting what we learned in the past, make a transition to what w" bullet="motivation">Explicitly required transition into tool-calling motivation.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-understanding-why-agents-need-tools" self_contained="yes" sources="h8gMhXYAv1k,ApoDzZP8_ck,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Explain the core limitation of LLMs as text generators and why external tools are required to enable interaction with the world.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="theoretical_foundations" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="technical_nuances" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="cross_domain_analogies" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="11" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Before showing how to implement tool calling from scratch and with Gemini, explain in more depth why LLMs need tools in" bullet="motivation">Core motivation for the entire section.</orphan>
    <orphan route="depth" anchor="LLMs have one fundamental limitation. They are simple pattern matchers and text generators. They cannot, by themselves," bullet="theoretical_foundations">Direct theoretical foundation statement.</orphan>
    <orphan route="depth" anchor="Analogy: The LLM is the brain, while the tools are an LLM's &quot;hands and senses,&quot; allowing it to perceive and act in the w" bullet="cross_domain_analogies">Explicit brain/hands analogy required.</orphan>
    <orphan route="depth" anchor="Thus, tools are the bridge between the LLM's internal reasoning and the external world. With the power of tools, the LLM" bullet="theoretical_foundations">Bridge concept is foundational.</orphan>
    <orphan route="depth" anchor="Use a representative image from the research to explain at a high level how tools work." bullet="motivation">Visual support for motivation.</orphan>
    <orphan route="depth" anchor="Examples of popular tools that power modern AI agents:" bullet="technical_nuances">Leads into concrete tool examples.</orphan>
    <orphan route="depth" anchor="Access real-time information through APIs (e.g., today's weather, latest news)." bullet="technical_nuances">Specific tool category detail.</orphan>
    <orphan route="depth" anchor="Interact with external databases or other storage solutions (PostgreSQL database, Snowflake data warehouse, S3 data lake" bullet="technical_nuances">Specific tool category detail.</orphan>
    <orphan route="depth" anchor="Access agent's long-term memory to remember information beyond their context window" bullet="technical_nuances">Specific tool category detail.</orphan>
    <orphan route="depth" anchor="Execute code (Python, JavaScript)" bullet="technical_nuances">Specific tool category detail.</orphan>
    <orphan route="depth" anchor="Perform precise calculations beyond their training data (basic math calculations, sorting, filtering, grouping, etc.)" bullet="technical_nuances">Specific tool category detail.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-implementing-tool-calls-from-scratch" self_contained="yes" sources="towardsai_course-ai-agents,function-calling-with-openai-s-api,function-calling-with-the-gemini-api" artefacts="">
  <intent>Provide a complete from-scratch implementation of tool schemas, system prompts, parsing, and execution using mock tools.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="17" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="The best way to understand how tools work and how LLMs use them is by implementing them from scratch. That's why the res" bullet="motivation">Section motivation statement.</orphan>
    <orphan route="depth" anchor="Before going into the code, quickly list what we will learn in this section, such as how a tool is defined, how their sc" bullet="technical_nuances">Preview of technical steps.</orphan>
    <orphan route="depth" anchor="Next provide a summary of our end goal, which is to provide the LLM with a list of available tools and let it decide whi" bullet="theoretical_foundations">End-goal summary of the flow.</orphan>
    <orphan route="depth" anchor="Provide a mermaid diagram illustrating the 5 steps from above, highlighting the request-execute-respond flow of calling" bullet="technical_nuances">Required diagram for flow.</orphan>
    <orphan route="depth" anchor="Now, let's dig into the code. To make it interesting, we will implement a simple example where we mock searching documen" bullet="implementation_tradeoffs">Code example setup.</orphan>
    <orphan route="depth" anchor="Using the code examples from the provided Notebook within the &lt;research&gt; tag, use all the code from the `2. Implementing" bullet="implementation_tradeoffs">Explicit notebook code usage directive.</orphan>
    <orphan route="depth" anchor="Here is how you should use the code from the `2. Implementing tool calls from scratch` section of the provided Notebook" bullet="implementation_tradeoffs">Detailed code mapping instructions.</orphan>
    <orphan route="depth" anchor="The tool usage guidelines" bullet="technical_nuances">System prompt component.</orphan>
    <orphan route="depth" anchor="The tool call format" bullet="technical_nuances">System prompt component.</orphan>
    <orphan route="depth" anchor="The response behavior" bullet="technical_nuances">System prompt component.</orphan>
    <orphan route="depth" anchor="The list of available tools enclosed by XML tags" bullet="technical_nuances">System prompt component.</orphan>
    <orphan route="depth" anchor="Based on the `description` field from the tool schema, the LLM *decides* if a tool call is appropriate to fulfill the us" bullet="theoretical_foundations">Decision logic explanation.</orphan>
    <orphan route="depth" anchor="Another disambiguation method when working with AI agents is to be as clear as possible in the system prompts, verbosely" bullet="technical_nuances">Prompt clarity guidance.</orphan>
    <orphan route="depth" anchor="By defining clear tool descriptions and system prompts, you ensure the AI agent will be able to make the necessary match" bullet="technical_nuances">Scaling consideration.</orphan>
    <orphan route="depth" anchor="Based on the selected tool, it then *generates* the function name and arguments as structured outputs such as JSON or Py" bullet="technical_nuances">Generation step detail.</orphan>
    <orphan route="depth" anchor="Add a quick note specifying that the LLM is specially tuned through instruction fine-tuning to interpret tool schema inp" bullet="theoretical_foundations">Fine-tuning note.</orphan>
    <orphan route="depth" anchor="Conclude by saying that this is the basic concept behind tool calling." bullet="motivation">Section conclusion.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-implementing-a-tool-calling-framework-from-scratch" self_contained="yes" sources="towardsai_course-ai-agents,agentic-design-patterns-part-3-tool-use,function-calling-with-openai-s-api" artefacts="">
  <intent>Show how a @tool decorator automates schema generation, following DRY principles and mirroring production frameworks.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="towardsai_course-ai-agents"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="10" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Manually defining schemas for every tool we want to use can quickly become cumbersome and hard to scale. That's why all" bullet="motivation">Motivation for decorator approach.</orphan>
    <orphan route="depth" anchor="Thus, in our writing from scratch exercise, as a natural progression to defining the tool schemas manually, we will impl" bullet="implementation_tradeoffs">Progression from manual to decorator.</orphan>
    <orphan route="depth" anchor="The end goal is to decorate a function with the `@tool` decorated and based on the function's docstring and signature (i" bullet="technical_nuances">Decorator goal definition.</orphan>
    <orphan route="depth" anchor="This method also follows good software engineering principles, as we respect the Don't Repeat Yourself (DRY) software pr" bullet="implementation_tradeoffs">DRY principle reference.</orphan>
    <orphan route="depth" anchor="Now, let's dig into the code and rewrite the implementation from the previous section using `@tool` decorators." bullet="implementation_tradeoffs">Code rewrite directive.</orphan>
    <orphan route="depth" anchor="Using the code examples from the provided Notebook within the &lt;research&gt; tag, use all the code from the `3. Implementing" bullet="implementation_tradeoffs">Notebook code usage.</orphan>
    <orphan route="depth" anchor="Here is how you should use the code from the `3. Implementing a tool calling framework from scratch` section of the prov" bullet="implementation_tradeoffs">Detailed code mapping.</orphan>
    <orphan route="depth" anchor="type (highlight that now it's `ToolFunction` instead of a normal Python function)" bullet="technical_nuances">Type inspection point.</orphan>
    <orphan route="depth" anchor="schema (highlight that it's identical with the one manually defined by us)" bullet="technical_nuances">Schema equivalence point.</orphan>
    <orphan route="depth" anchor="functional handler (highlight that this is how we access the function handler now)" bullet="technical_nuances">Handler access point.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-implementing-production-level-tool-calls-with-gemini" self_contained="yes" sources="function-calling-with-the-gemini-api,ApoDzZP8_ck,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Demonstrate Gemini's native GenerateContentConfig and automatic schema conversion to replace manual prompting.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="theoretical_foundations" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="technical_nuances" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="function-calling-with-the-gemini-api"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S6::section-6-using-pydantic-models-as-tools-for-on-demand-structured-outputs" self_contained="yes" sources="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen,h8gMhXYAv1k,function-calling-with-openai-s-api" artefacts="">
  <intent>Show Pydantic models used as tools to obtain structured outputs on demand inside agent loops.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="theoretical_foundations" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="technical_nuances" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="function-calling-with-openai-s-api"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S7::section-7-the-downsides-of-running-tools-in-a-loop" self_contained="yes" sources="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen,agentic-design-patterns-part-3-tool-use,efficient-tool-use-with-chain-of-abstraction-reasoning" artefacts="">
  <intent>Illustrate sequential tool loops, their limitations, and the motivation for ReAct-style patterns.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="theoretical_foundations" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="technical_nuances" present="yes" evidence="efficient-tool-use-with-chain-of-abstraction-reasoning"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="implementation_tradeoffs" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="efficient-tool-use-with-chain-of-abstraction-reasoning"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S8::section-8-popular-tools-used-within-the-industry" self_contained="yes" sources="ApoDzZP8_ck,agentic-design-patterns-part-3-tool-use,h8gMhXYAv1k" artefacts="">
  <intent>Survey common industry tool categories (memory, search, code execution, APIs) to ground the lesson in real usage.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="theoretical_foundations" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="technical_nuances" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="agentic-design-patterns-part-3-tool-use"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="ApoDzZP8_ck"/>
    <item name="industry_applications" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S9::section-9-conclusion" self_contained="yes" sources="ApoDzZP8_ck,h8gMhXYAv1k,building-ai-agents-from-scratch-part-1-tool-use" artefacts="">
  <intent>Reaffirm tool calling as foundational and preview Lesson 7 on planning/ReAct.</intent>
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
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="h8gMhXYAv1k"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="building-ai-agents-from-scratch-part-1-tool-use"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="12" need_breadth="4" target_words="60" mandatory_bullets="2" must_cover_depth="0" must_stay_brief="0"/>
  <section id="S2::section-2-understanding-why-agents-need-tools" need_depth="37" need_breadth="3" target_words="130" mandatory_bullets="3" must_cover_depth="0" must_stay_brief="3"/>
  <section id="S3::section-3-implementing-tool-calls-from-scratch" need_depth="55" need_breadth="4" target_words="390" mandatory_bullets="5" must_cover_depth="5" must_stay_brief="5"/>
  <section id="S4::section-4-implementing-a-tool-calling-framework-from-scratch" need_depth="34" need_breadth="4" target_words="230" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="4"/>
  <section id="S5::section-5-implementing-production-level-tool-calls-with-gemini" need_depth="4" need_breadth="4" target_words="160" mandatory_bullets="5" must_cover_depth="5" must_stay_brief="5"/>
  <section id="S6::section-6-using-pydantic-models-as-tools-for-on-demand-structured-outputs" need_depth="5" need_breadth="4" target_words="130" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="4"/>
  <section id="S7::section-7-the-downsides-of-running-tools-in-a-loop" need_depth="3" need_breadth="4" target_words="210" mandatory_bullets="4" must_cover_depth="4" must_stay_brief="4"/>
  <section id="S8::section-8-popular-tools-used-within-the-industry" need_depth="5" need_breadth="3" target_words="140" mandatory_bullets="1" must_cover_depth="1" must_stay_brief="1"/>
  <section id="S9::section-9-conclusion" need_depth="6" need_breadth="4" target_words="40" mandatory_bullets="2" must_cover_depth="0" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S2::section-2-understanding-why-agents-need-tools, S3::section-3-implementing-tool-calls-from-scratch</weakest_sections>
    <strongest_sections>S7::section-7-the-downsides-of-running-tools-in-a-loop, S5::section-5-implementing-production-level-tool-calls-with-gemini</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>