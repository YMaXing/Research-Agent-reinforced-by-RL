# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: Tool calling is the mechanism that lets large language models invoke external functions and APIs. It bridges the gap between language generation and real-world actions. Without tools, an LLM is limited to what it learned during training. With tools, it can access current data, take actions, and integrate with your systems. Computation matters because data often needs processing before it’s useful for decision-making, such as calculating growth rates from sales data or sentiment analysis from customer feedback. Actions change state, including communication tools for emails, Slack messages, SMS. Graph databases excel at relationships like social networks or knowledge graphs. External APIs bring in third-party data like weather services, stock prices, news feeds. File systems provide document access for reports, contracts.

-----

Phase: [EXPLOITATION]

### Source [2]: https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: LLMs have general knowledge but lack specific company knowledge base, current time and date, perform poorly with maths calculations, unable to access current events. The ability to use external APIs (public or private) increases LLM power to retrieve data and interact with other systems. For example, for current weather, LLM cannot fulfill alone without real-time data, but programmed to interact with weather API, it formulates API request, receives data, presents to user. This extends capabilities for real-time data and external functionalities. Researchers focus on accuracy in understanding user intent and using external tools to expand intrinsic abilities.

-----

Phase: [EXPLOITATION]

### Source [3]: https://arxiv.org/html/2507.08034v1

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: Current LLM models handle natural language well but face difficulties with tasks demanding current data or active computational capabilities, like current stock market trends or complex math problems, due to training on fixed datasets and limited direct connection to external databases or APIs. Integrating external tools like calculators, calendars, databases improves capabilities for current data analysis and computations. Methods: Retrieval-augmented generation (RAG) connects to databases or search engines for real-time data; code execution like Python for math computations; connecting APIs for financial, health, weather services; hybrid systems combining symbolic reasoning, knowledge graphs.

-----

Phase: [EXPLOITATION]

### Source [4]: https://en.wikipedia.org/wiki/Large_language_model

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: Tool use enables LLMs to interact with external systems, applications, or data sources, e.g., fetch real-time information from an API or execute code. A separate program watches LLM output for special tool-calling syntax, calls the tool, feeds output back into LLM input. Early tool-using LLMs fine-tuned on specific tools; fine-tuning to read API documentation expands tool range. Beyond basic text generation, techniques extend capabilities using external tools and data sources.

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.ibm.com/think/topics/tool-calling

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: LLMs limited by training data, which is time and computationally intensive. Need for real-time data, external computations, enhanced interactivity led to tool calling. Early LLMs like GPT-2 static, generated based on training data without fetching new info, lacked real-world awareness for dynamic queries like current events, stock prices. Tool calling enables agentic AI, allows accessing external resources, automate workflows, interact with databases, multistep problem-solving, real-time decisions.

-----

</details>

<details>
<summary>How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: JSON schemas define tool functions for LLMs by specifying the function name (unique identifier), description (what the function does and when to use it), and parameters (expected arguments, their types, and which ones are required). This schema acts as a contract between the developer and the AI, telling the model when to call the function, what arguments to send, and the format to expect in return. Functions serve as interfaces between the AI and external apps or services, allowing the model to perform actions or fetch data during conversations. In OpenAI’s function calling feature, the tool definition is a JSON schema that details the function name, description, and argument structure. Models like GPT-5 can decide when a function call is needed and generate correct JSON inputs. Multiple functions can be called in a single request. Google enforces schemas natively in Gemini through Vertex AI, where developers specify strict JSON schemas, and Gemini guarantees compliance. Various ways to define schemas include standard formats describing name, inputs, and types; auto-generating from code; or using validation libraries for precision.

-----

Phase: [EXPLOITATION]

### Source [7]: https://apxml.com/courses/prompt-engineering-agentic-workflows/chapter-3-prompt-engineering-tool-use/formatting-tool-specifications-llm

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: JSON schemas, often using JSON Schema-like type definitions, are used to describe tools for LLM agents. Each parameter is defined with: name (descriptive, e.g., 'query'), type (e.g., 'string', 'number', 'boolean', 'array', 'object' to help LLMs format data correctly), description (clear explanation of what it represents, constraints, formats), and required/optional status. This is critical for correct tool invocation. Common formats include JSON structures inspired by JSON Schema for parameters and outputs. Modern LLM APIs like OpenAI expect tool specifications in predefined JSON format, such as a list of tools with 'type': 'function', containing 'name', 'description', and 'parameters' as an object with 'properties' (each with type and description) and 'required' array. Example: [{'type': 'function', 'function': {'name': 'get_flight_booking_status', 'description': '...', 'parameters': {'type': 'object', 'properties': {'booking_id': {'type': 'string', 'description': '...'}}, 'required': ['booking_id']}}}]. Adhering to vendor-specific formats enables dedicated tool-use features, allowing LLMs to parse and generate correct calls.

-----

Phase: [EXPLOITATION]

### Source [8]: https://blog.promptlayer.com/how-json-schema-works-for-structured-outputs-and-tool-integration/

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: JSON Schema provides a standardized way to describe and enforce data structure for LLMs interacting with external tools. It defines input and output formats, ensuring seamless data exchange. For tool integration: 1) LLM is instructed via prompting or function calling to generate output conforming to the schema (e.g., 'Generate a user profile in JSON format according to the provided schema.'). 2) Output is validated against the schema; invalid outputs prompt refinement or flag errors. 3) Valid output is passed to the tool, which interprets it using schema knowledge. Benefits: enforces structure for predictable, machine-readable output; facilitates tool integration as common language; validates data for integrity; improves reliability in LLM-tool interactions. This makes LLM outputs suitable for external systems.

-----

Phase: [EXPLOITATION]

### Source [9]: https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: Function calling uses JSON schemas to define tools, enabling LLMs to emit structured function calls with parameters, execute external code safely, and synthesize results. Schemas are provided to the LLM via system messages, e.g., 'You have access to the following tools: {json.dumps(registry.get_schemas())}'. A ToolRegistry centralizes management, mapping function names to schemas (for LLM consumption) and implementations (for execution). Schemas describe available tools, allowing discovery. LLMs generate responses with tool_calls (list of FunctionCall with name, arguments dict, call_id). The loop: LLM generates response; if tool calls present, execute them (parallel), add results to conversation. This transforms LLMs into agents interacting with external systems. Key: schemas in JSON format teach models to produce correct calls.

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.baseten.co/blog/how-to-build-function-calling-and-json-mode-for-open-source-and-fine-tuned-llms/

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: Function calling provides LLMs with structured tool descriptions (JSON schemas) including names, descriptions (e.g., descriptive docstrings), and parameters. Based on the prompt, the model selects appropriate tools and generates calls. Tools can be API calls, database access, etc. LLMs do not execute; the environment does after receiving the call. Implementation follows OpenAI API spec via 'tools' key in payload, ensuring compatibility. Uses logit biasing for schematically correct outputs, guaranteeing adherence. A tool registry or similar provides schemas. Example: functions with docstrings passed to LLM. This enables discovery of tools, understanding via descriptions, and correct parameter formatting. Applies to models like Llama 3.1 Instruct with built-in support.

-----

</details>

<details>
<summary>How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://reference.langchain.com/python/langchain-core/tools/convert/tool

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: The @tool decorator in LangChain Core converts Python functions and Runnables to LangChain tools. It can be used as a decorator with or without arguments. Functions can have any signature - the tool will automatically infer input schemas unless disabled. Parameters include args_schema (Optional argument schema for user to specify, default None), infer_schema (bool, default True: Whether to infer the schema of the arguments from the function's signature. This also makes the resultant tool accept a dictionary input to its run() function), run() response_format (Literal['content', 'content_and_artifact'], default 'content': determines if output is ToolMessage content or (content, artifact) tuple), and parse_docstring (bool, default False). The decorator automatically extracts function signatures to infer schemas, supporting type hints implicitly through signature inspection.

-----

Phase: [EXPLOITATION]

### Source [12]: https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework?view=agent-framework-python-latest

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: The @ai_function decorator in agent_framework turns a function into an AIFunction for models, executed automatically. It creates a Pydantic model from the function's signature to validate arguments and generate JSON schema for parameters. Parameters: name (uses function __name__ if None), description (uses function docstring if None), approval_mode, max_invocations, max_invocation_exceptions. AIFunction implements ToolProtocol. The decorator extracts function signature for Pydantic model (handling type hints), docstring for description, automating schema generation for agent tools.

-----

Phase: [EXPLOITATION]

### Source [13]: https://builder.aws.com/content/38oLPJ7KYLglawz3dScA5q8H4XJ/tool-function-decorators-for-strands-agents

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: In Strands Agents, the @tool decorator converts Python functions into agentic tools. The decorated function's parameters become the tool's input schema. Parameter names, data types, and annotations directly influence the schema. Uses Annotated type hints for types and descriptions. @tool description parameter describes the tool generally. Examples: int with description maps to {"type": "integer", "description": "..."}; float to {"type": "number"}; List[float] to {"type": "array", "items": {"type": "number"}}. The decorator extracts type hints (including Annotated for descriptions), parameter names, and signatures to generate JSON tool schemas for agents.

-----

Phase: [EXPLOITATION]

### Source [14]: https://dev.to/aws/ai-agents-dont-need-complex-workflows-build-one-in-python-in-10-minutes-2m5d

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: The @tool decorator in Strands is used to create tools. The docstring matters as the model uses it with function's type hints to decide when to call and what arguments to pass. Clear docstrings improve tool usage. Agent is wired with model, tools=[decorated_functions], system_prompt. Decorator leverages docstrings and type hints for schema inference in lightweight agent setup.

-----

</details>

<details>
<summary>How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://www.philschmid.de/gemini-function-calling

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: The Gemini API uses GenerateContentConfig to define tools for native function calling. Function declarations are defined in the config object using the Pydantic GenerateContentConfig data structure. Example: from google.genai.types import GenerateContentConfig; config = GenerateContentConfig(system_instruction="You are a helpful assistant that use tools to access and retrieve information from a weather API.", tools=[get_weather_forecast]). The LLM decides if it should call the function or return normal text. Pydantic models like get_weather_forecast are directly passed in the tools list for the LLM to use. System instruction provides context, e.g., current date. Automatic function calling is default with callable functions, so no need to specify automatic_function_calling.

-----

Phase: [EXPLOITATION]

### Source [17]: https://ai.google.dev/gemini-api/docs/function-calling

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: In the Gemini API, GenerateContentConfig is used to configure tools for function calling. Example: config = types.GenerateContentConfig(tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]); response = client.models.generate_content(model="gemini-3-flash-preview", contents="Do everything you need to this place into party!", config=config). For automatic function calling, the SDK handles execution. Compositional calling combines tools like google_search and custom functions: config=types.GenerateContentConfig(tools=[types.Tool(google_search=types.ToolGoogleSearch(), function_declarations=[getWeather])], include_server_side_tool_invocations=True). Disable automatic with automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True). Pass functions directly to tools for schema declaration.

-----

Phase: [EXPLOITATION]

### Source [18]: https://pydantic.dev/docs/ai/core-concepts/output/

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: Pydantic integrates with models for structured outputs. Native Output mode uses model’s native Structured Outputs (JSON Schema), but Gemini cannot use tools simultaneously with structured output, resulting in error. Output functions arguments are validated using Pydantic, can take RunContext, raise ModelRetry. Specify output_type as single function, list of functions, scalars, or Pydantic models. Do not register output function as tool to avoid confusion. For models without native tool calling, other modes produce structured outputs. JSON Mode forces valid JSON, Pydantic validates and retries if fails.

-----

Phase: [EXPLOITATION]

### Source [19]: https://composio.dev/content/tool-calling-guide-with-google-gemini

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: Gemini tool calling uses GenerateContentConfig in Python SDK to pass prompt and tools configuration. Gemini decides if function call needed based on prompt and tool descriptions. Returns functionCall object with name and JSON args matching schema. App executes function, feeds back. Uses Client, FunctionDeclaration, GenerateContentConfig. Steps: install google-genai, configure client. Native SDK requires manual tool definitions, execution, loop. Supports agentic workflows via declare tools → functionCall → execute → synthesize.

-----

Phase: [EXPLOITATION]

### Source [20]: https://docs.swarms.world/en/latest/swarms/examples/pydantic_structured_outputs_tutorial/

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: Pydantic models enable structured outputs. Define models with Field descriptions/constraints. Use tool_schema for single model, list_base_models for multiple outputs. Agent converts Pydantic response to dictionary or model instance. Supports multi-model configuration for different structures. Best practices: field descriptions, validation, error handling.

-----

</details>

<details>
<summary>What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?</summary>

Phase: [EXPLOITATION]

### Source [21]: https://aisera.com/blog/llm-agents/

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Tools used: LLM-based agents can also integrate external tools, APIs, and specialist modules to perform actions that are beyond their native language capabilities. These can include code interpreters (for executing code snippets, allowing the agent to execute code, generate charts, and perform complex programmatic tasks), search engines (for real-time data retrieval), databases and vector stores (for knowledge retrieval), and collaboration and productivity tools (like GitHub, Trello, Google Sheets, and more).

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.codeant.ai/blogs/parallel-tool-calling

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Parallel tool calling allows an LLM to request and execute multiple external functions at the same time instead of waiting for each one to finish before starting the next. When an AI agent handles a complex request, it often pulls data from several sources: APIs, databases, or third-party services. Running all of those calls simultaneously rather than sequentially cuts total response time dramatically. Tool calling itself is the mechanism that lets LLMs interact with the outside world. Without it, a language model can only work with the information already in its training data. With tool calling, the model can fetch live weather, query a database, or trigger an action in another system. Independent Tool Operations: Operations with no shared dependencies are ideal candidates. Fetching user profile, preferences, and notifications from separate services is a classic example since none of those calls affects the others. High-Latency External API Calls: Parallelism provides the greatest gains when individual calls have significant network or processing overhead. If each call takes 500ms, running five of them in parallel saves 2 full seconds compared to sequential execution. When Sequential Execution Is Required: Some operations genuinely depend on each other. You can't parallelize without breaking your logic in cases like: Data dependencies: The output of one tool feeds into another (get user ID, then fetch that user's orders). Ordered operations: Steps follow a required sequence (authenticate first, then access protected resource). State mutations: Tools modify shared state that affects subsequent calls (update inventory, then check availability). Forcing parallelism in any of those scenarios creates race conditions and incorrect results.

-----

Phase: [EXPLOITATION]

### Source [23]: https://www.promptingguide.ai/research/llm-agents

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Tools correspond to a set of tool/s that enables the LLM agent to interact with external environments such as Wikipedia Search API, Code Interpreter, and Math Engine. Tools could also include databases, knowledge bases, and external models. When the agent interacts with external tools it executes tasks via workflows that assist the agent to obtain observations or necessary information to complete subtasks and satisfy the user request. In our initial health-related query, a code interpreter is an example of a tool that executes code and generates the necessary chart information requested by the user. Tools are leveraged in different ways by LLMs: LLM agents are still in their infancy so there are many challenges and limitations that remain when building them.

-----

Phase: [EXPLOITATION]

### Source [24]: https://arxiv.org/html/2603.22862v2

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: To address the cumulative delays and inefficiencies caused by sequential execution in long-chain multi-tool calls, parallel execution (233) has become a key optimization direction. Its core idea is to decompose tasks, identify subtasks with no interdependencies, and execute them simultaneously. SoT (124) accelerates inference by expanding multiple skeleton branches in parallel instead of following a fully sequential decoding pattern. At the tool level, LLMCompiler (78) explicitly plans task dependencies so that independent tool calls can run concurrently. For longer workflows, M1-Parallel (216) further decomposes sequential tasks into independent subtasks coordinated by multiple agents. Parallelized planning-acting (91) extend the same idea by overlapping planning and execution, allowing. In multi-tool orchestration architectures, parallel execution significantly enhances agent efficiency in complex task processing; however, it introduces latent security vulnerabilities. While parallelization is relatively safe for side-effect-free read operations (e.g., web retrieval, information queries), the integration of write operations (e.g., database updates, transaction commits) within tool chains risks race conditions, leading to system state inconsistencies. The integration of external tools has substantially enhanced the capability of agents to address complex tasks. Nevertheless, the reliance on multi-step inference and sequential tool invocation introduces significant efficiency bottlenecks. This chapter reviews emerging optimization strategies from two primary perspectives: mitigating latency in multi-tool chains (§6.1) and managing tool call cost and inference budget (§6.2). Latency in multi-tool chains.

-----

Phase: [EXPLOITATION]

### Source [25]: https://futureagi.substack.com/p/how-tool-chaining-fails-in-production

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Tool chaining is the sequential execution of multiple tool calls by an LLM agent, where each tool’s output becomes the input for the next tool in the sequence. An agent receives a user query, decides it needs data from an API, processes that data with a second tool, and generates a final response using the combined results. This differs from a single tool call in important ways. A single call is straightforward: the LLM calls a function, gets a result, and responds. Chaining creates dependencies. The agent must determine the right order of operations, track intermediate state, and handle partial failures while staying focused on the original goal. In multi-agent systems, the complexity increases further because one agent might call a tool, hand the result to a second agent, which runs its own tool sequence before returning. The orchestration overhead compounds quickly, and potential failure points grow with it. The pattern is familiar to anyone building LLM-powered applications. Your agent chains three or four tool calls together. The first call returns slightly malformed output. The second tool accepts it but misinterprets a field. By the third call, the entire chain has gone off the rails. This is the cascading failure problem, and it remains the primary bottleneck to agent reliability in 2026. Research from Zhu et al. (2025) confirms that error propagation is the single biggest barrier to building dependable LLM agents.

-----

</details>

<details>
<summary>How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?</summary>

Phase: [EXPLOITATION]

### Source [26]: https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: While general-purpose models like GPT-4 come with robust function calling capabilities, open-source models often require fine-tuning to reliably emit structured tool calls. This process involves curating datasets of tool-use conversations and optimizing the model for schema adherence. Fine-tuning transforms a base model from a general text generator into a specialized tool-calling agent. Key hyperparameters for function calling fine-tuning include masking strategy. When computing the cross-entropy loss, the model learns to generate correct tool calls and final responses by masking user's messages or system prompt tokens out of the loss computation, ensuring gradient signal comes from model's own outputs. This is the same technique used in instruction tuning. The key insight is that function call generation is not fundamentally different from ordinary text generation: it is next-token prediction applied to structured, schema-conforming JSON. During pre-training, model predicts next token in human-written text. During function calling fine-tuning, model learns to predict next token in structured JSON. Architecture identical; only training data and target format differ. Function calling capability instilled through supervised fine-tuning on specialized datasets of conversation traces.

-----

Phase: [EXPLOITATION]

### Source [27]: https://www.analyticsvidhya.com/blog/2024/09/enhancing-llms-with-structured-outputs-and-function-calling/

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Enhancing function calling for niche tasks involves fine-tuning small LLMs to handle specific data curation needs. Leveraging techniques like special tokens and LoRA fine-tuning optimizes function execution and improves model’s performance for specialized applications. Data Curation: precise data management for effective function calls. Special Tokens: custom tokens mark beginning and end of function calls for better integration. Model Training: start with instruction-based models trained on high-quality data. LoRA Fine-Tuning: enhances performance in targeted manner. Function Calling with LLMs enables execution of predefined functions as part of response generation, allowing interaction with external systems. Pydantic objects simplify defining and converting schemas for function calling.

-----

Phase: [EXPLOITATION]

### Source [28]: https://blog.neosage.io/p/an-engineers-guide-to-fine-tuning

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Fine-tuning enables structural consistency: always outputting tool call in exact JSON schema, even for vague user requests. Domain-native reasoning: applying business rules or jargon. Prompt-free formatting: embedded in weights, no need for shots. Fine-tuning makes structure native capability by training on hundreds or thousands of valid examples, internalizing schema's rules. Overcomes limitations of in-context learning like brittleness and inconsistency where model mimics but doesn't learn grammar. Model emits outputs bound to strict API contract, resolves ambiguous terms, refuses sensitive data. Fine-tuning encodes specialized behavior into weights, unlike prompting.

-----

Phase: [EXPLOITATION]

### Source [29]: https://pavelbazin.com/post/the-essential-guide-to-large-language-models-structured-output-and-function-calling/

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Structured output fine-tune allows models to output JSON more reliably. Models without it output unreliable JSON-looking text. Function calling is structured output with extra steps like RAG. Structured output acquired during fine-tuning. Workflow: provide function descriptions to LLM, it returns call request based on schema, execute, feed back. Function calling possible via structured output without API, but specialized use case of structured output. Provide data specification to LLM.

-----

Phase: [EXPLOITATION]

### Source [30]: https://www.leewayhertz.com/structured-outputs-in-llms/

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Function calling allows LLM to generate specific function calls based on prompt and parameters, passing function names and descriptions to determine actions. Enhances ability for targeted tasks and structured output, requires fine-tuning or specific support. Achieving structured outputs involves fine-tuning on structured data, crafted prompts, or post-processing. Methods like prompt engineering, function calling, JSON schema enforcement produce consistent outputs, reducing hallucinations.

-----

</details>

<details>
<summary>How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?</summary>

Phase: [EXPLOITATION]

### Source [32]: https://www.emergentmind.com/topics/multi-turn-tool-calling-large-language-models-llms

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: A canonical multi-turn framework includes: Observation with full history of queries, tool calls (arguments), and tool outputs. Planning selects next tool or answers. Tool Execution calls API/function, records output. Termination outputs answer with citations. In advanced settings like persistent Lisp metaprogramming loop, agent-tool creation, versioning, and stateful memory (REPL) enable inventing/refining symbolic procedures across turns. Training uses supervised fine-tuning (SFT) on multi-turn trajectories where each step involves tool selection, argument filling, tool output parsing, and propagation into subsequent reasoning. Loss is next-token cross-entropy, masked for assistant turns.

-----

Phase: [EXPLOITATION]

### Source [33]: https://community.openai.com/t/how-can-i-ensure-every-llm-reply-includes-exactly-one-message-and-one-tool-call/1283087

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: To combine message and tool call, use structured outputs like JSON schema with strict=true to force format including explanation and tool call. For boolean queries, message shows rationales, tool assesses quality. Use structured output for reasoning first, then verdict. Reasoning models like o3/o4-mini perform background reasoning. Chain-of-thought in prompts helps generate natural language with tool calls.

-----

Phase: [EXPLOITATION]

### Source [34]: https://medium.com/promptlayer/tool-calling-with-llms-how-and-when-to-use-it-d65493a87954

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: Tool calling enables self-healing: LLM makes function call, reads results, decides to retry if needed. Structured JSON outputs ensure consistency. Offload parsing to model providers. For SQL chatbot, LLM detects/corrects mistakes by processing tool outputs iteratively without manual parsing.

-----

Phase: [EXPLOITATION]

### Source [35]: https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: Standard observe-act loop: Model emits structured function call; app executes, formats result as observation message appended to conversation history; model generates final natural language response incorporating new info. Training includes observations to teach synthesizing tool results into responses. Preprocess tool output: return full relevant payload with clear fields, remove irrelevant metadata. This preserves info for model to use in subsequent actions.

-----

</details>

<details>
<summary>In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://www.devtoolsfeed.com/article/parallel-tool-calling-in-llm-agents-complete-guide-with-code-examples/

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Parallel tool calling allows LLM agents to execute multiple independent tool requests concurrently, significantly reducing latency. This capability eliminates unnecessary model round trips and speeds up overall agent task completion. Developers can implement parallel tool calling across major LLM APIs like OpenAI, Anthropic Claude, and Google Gemini with asynchronous programming patterns. Effective error handling is crucial when executing tools in parallel to manage partial failures gracefully.

-----

Phase: [EXPLOITATION]

### Source [37]: https://www.codeant.ai/blogs/parallel-tool-calling

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Independent Tool Operations: Operations with no shared dependencies are ideal candidates. Fetching user profile, preferences, and notifications from separate services is a classic example since none of those calls affects the others. High-Latency External API Calls: Parallelism provides the greatest gains when individual calls have significant network or processing overhead. If each call takes 500ms, running five of them in parallel saves 2 full seconds compared to sequential execution. Batch Processing Scenarios: Applying the same operation to multiple inputs concurrently is another strong use case. Analyzing multiple code files at once, for instance, rather than processing them one by one. When Sequential Execution Is Required: Some operations genuinely depend on each other. You can't parallelize without breaking your logic in cases like: Data dependencies: The output of one tool feeds into another (get user ID, then fetch that user's orders); Ordered operations: Steps follow a required sequence (authenticate first, then access protected resource); State mutations: Tools modify shared state that affects subsequent calls (update inventory, then check availability). Forcing parallelism in any of those scenarios creates race conditions and incorrect results. When Parallel Execution Delivers Gains: Look for patterns like: Independent data fetches: Pulling user profile, preferences, and notifications from separate services. Total latency: Sum of all individual call times (sequential) vs. Duration of the slowest single call (parallel). Parallel execution changes the math. Those same four 300ms calls now complete in roughly 300ms total because they all run concurrently. How Parallel Tool Calling Works Under the Hood: The process breaks into four phases. 1. The Agent Receives a Multi-Tool Request: Picture a user asking: "What's the weather in Chicago, what's on my calendar today, and how long is my commute?" One prompt, but three completely separate data sources. The agent recognizes immediately that it will call multiple tools.

-----

Phase: [EXPLOITATION]

### Source [38]: https://adk.dev/agents/workflow-agents/parallel-agents/

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: The ParallelAgent is a workflow agent that executes its sub-agents concurrently. This dramatically speeds up workflows where tasks can be performed independently. Use ParallelAgent when: For scenarios prioritizing speed and involving independent, resource-intensive tasks, a ParallelAgent facilitates efficient parallel execution. When sub-agents operate without dependencies, their tasks can be performed concurrently, significantly reducing overall processing time. Example: Imagine researching multiple topics simultaneously: Researcher Agent 1: An LlmAgent that researches "renewable energy sources." Researcher Agent 2: An LlmAgent that researches "electric vehicle technology." Researcher Agent 3: An LlmAgent that researches "carbon capture methods." These research tasks are independent. Using a ParallelAgent allows them to run concurrently, potentially reducing the total research time significantly compared to running them sequentially. The results from each agent would be collected separately after they finish. When the ParallelAgent's run_async() method is called: 1. Concurrent Execution: It initiates the run_async() method of each sub-agent present in the sub_agents list concurrently. This means all the agents start running at (approximately) the same time. 2. Independent Branches: Each sub-agent operates in its own execution branch. There is no automatic sharing of conversation history or state between these branches during execution. 3. Result Collection: The ParallelAgent manages the parallel execution and, typically, provides a way to access the results from each sub-agent after they have completed (e.g., through a list of results or events). The order of results may not be deterministic. Independent Execution and State Management.

-----

Phase: [EXPLOITATION]

### Source [39]: https://www.kore.ai/blog/boost-ai-agent-performance-with-parallel-execution

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Parallel Execution solves this bottleneck by enabling AI agents to launch independent tasks concurrently. As soon as the required input, like a user ID, is available, the agent can leverage tools to trigger simultaneous data fetches from multiple systems without waiting for one to complete before starting the next. Because these systems (e.g., Salesforce, CRM, and helpdesk) operate independently and have no dependencies on each other, the agent can query them simultaneously. Instead of 15 seconds of wait time, the agent receives all the necessary data in just 5–6 seconds on average, the time it takes for the longest of the parallel requests to resolve. Example: With Parallel Execution, the agent instantly dispatches three parallel data requests: one to Salesforce for contact info, another to the CRM for transaction history, and a third to the helpdesk database for support logs. Within 5 seconds, the agent receives and synthesizes a full customer profile, allowing it to respond to the user quickly and accurately. In contrast, a traditional agent working with sequential execution would take three times longer to gather the same information, delaying the response, degrading the user experience, and potentially causing drop-off or frustration. Parallel Execution addresses one of the biggest friction points in AI workflow automation: latency from sequential processing. By eliminating the artificial delays between steps, Parallel Execution ensures that AI agents can operate with the speed and intelligence required in today’s always-on, multi-system enterprise environments.

-----

Phase: [EXPLOITATION]

### Source [40]: https://nordicapis.com/9-tips-for-reducing-api-latency-in-agentic-ai-systems/

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Parallelize Independent API Calls: Linked API calls are often slow because they are assumed to be sequential. In practice, many dependencies are less rigid than they appear. Agents frequently request multiple pieces of information that can be fetched independently, even if the model originally described them in sequence. A useful pattern is speculative execution. When the agent indicates a likely next set of API calls, the system can begin executing them in parallel before the agent explicitly requests the results. If the speculation is correct, the data is already available when needed. If it’s wrong, the cost is limited to a small amount of wasted computation time instead of a user-visible delay. Code mode is a good example of this principle in action. In code mode, an agent creates a typed client library from tool schemas and asks the model to write code that orchestrates those calls. That code is then executed in a sandboxed environment with controlled bindings, so the model’s reasoning about the workflow is separated from the actual execution of tool interactions.

-----

</details>

<details>
<summary>What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?</summary>

Phase: [EXPLOITATION]

### Source [41]: https://dev.to/simplr_sh/mastering-system-prompts-for-llms-2d1d

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: System prompts provide context, guide tone, and determine when to invoke specific tool calls. For effective design: 1. Clarity and Precision: Write instructions that are clear, concise, and unambiguous. Avoid mixing multiple instructions in one sentence or using language that can be interpreted in several ways. 2. Define Roles: Assign a specific role to the model, such as 'You are a helpful assistant specialized in financial analysis.' Role-specific instructions guide the model to tailor responses consistently. 3. Incorporate Tool-Call Instructions: For applications integrating external tools (e.g., data fetch APIs), include explicit instructions on when and how to call them. Example: 'When a user asks for data requiring current weather information, invoke the external "weatherAPI" tool with the user’s provided location. Format the result in JSON with "temperature" and "conditions" fields.' This tells the model what to do and how to integrate with additional functionality. By ensuring clarity, defining roles, incorporating precise tool-call instructions, and using structured formats, craft system prompts that unlock LLMs' potential for consistent, predictable interactions in tool-integrated applications.

-----

Phase: [EXPLOITATION]

### Source [42]: https://supercharge.io/blog/ai-prompt-engineering-best-practices

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: System prompts define the AI’s core role by outlining the task it should perform and the behavioural standards it should follow. An ideal prompt is clear, dense, and easy to understand, leaving no room for misinterpretation. In complex AI systems, prompts are enriched with additional components like context, explanations, or relevant documentation to guide the model effectively. Effective prompts contain: 1. System prompt: Defines core role, task, and behavioral standards. This may include available tools and functions. 2. Context: Relevant data sources such as retrieved documents (via RAG), available tools and functions, user background, conversation history, examples. The system prompt acts as the foundational instruction set guiding output in Agentic AI systems.

-----

Phase: [EXPLOITATION]

### Source [43]: https://superlinear.eu/insights/articles/prompt-engineering-for-llms-techniques-to-improve-quality-optimize-cost-reduce-latency

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: Structure prompts with XML tags to delineate instructions, context, and examples. Best practices: 1. Be explicit with instructions: Clear, specific directives for nuanced behaviors. 2. Add relevant context or motivation. 3. Pay attention to examples and details. 4. Clearly defining explicit instructions. 5. Providing context and motivations. 6. Structuring with XML tags. 7. Few-shot prompting and Chain of Thought (CoT). 8. Position critical information early. CoT implemented with phrases like “Think step-by-step,” explicit reasoning, or XML tags (e.g., <thinking> and </thinking>) to separate reasoning from final response. Example: Draft emails using XML-structured prompts: 'Draft personalized emails... Program:<program>{{PROGRAM_DETAILS}}</program> Donor:<donor>{{DONOR_DETAILS}}</donor>'.

-----

Phase: [EXPLOITATION]

### Source [44]: https://community.openai.com/t/prompting-best-practices-for-tool-use-function-calling/1123036

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: For tool use (function calling), include tool details in the system prompt for the model to reference them during responses. JSON definitions serve the API, but the model processes only text in the conversation; API parameters like tool definitions are not automatically added to the model's context. It is not strictly necessary to declare tools in the system prompt, but it helps to emphasize their presence or prioritize specific functions. The system prompt is about 'emphasis' in general. You can pass description fields in JSON tool definitions, but explicit text in the prompt ensures the model knows about them. Sometimes direct the model via system prompt to be consistent about tool awareness.

-----

</details>

<details>
<summary>How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?</summary>

Phase: [EXPLOITATION]

### Source [46]: https://www.decodingai.com/p/tool-calling-from-scratch-to-production

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: The `TOOLS_BY_NAME` mapping is a dictionary that maps tool names to their corresponding function handlers, such as {'google_search': <function google_search at 0x...>, 'perplexity_search': <function perplexity_search at 0x...>, 'scrape_url': <function scrape_url at 0x...>}. The `TOOLS_SCHEMA` contains the JSON schemas for these tools. Developers decorate functions with a @tool decorator to automatically populate `TOOLS_SCHEMA` and `TOOLS_BY_NAME` registries. For example, @tool def google_search(query: str) -> dict: ... and @tool def scrape_url(url: str) -> dict: .... A central `TOOLS` dictionary is constructed as {'google_search': {'handler': google_search, 'declaration': google_search_schema}, ...}. Then, `TOOLS_BY_NAME = {tool_name: tool['handler'] for tool_name, tool in TOOLS.items()}` and `TOOLS_SCHEMA = [tool['declaration'] for tool in TOOLS.values()]`. These mappings facilitate LLM-selected tool execution in from-scratch implementations by allowing the LLM to select a tool by name from the provided schemas (`TOOLS_SCHEMA`), after which the system looks up the exact function handler in `TOOLS_BY_NAME` to execute it with the parameters generated by the LLM. This decouples schema provision to the LLM from actual function execution, enabling efficient tool calling without hardcoding.

-----

Phase: [EXPLOITATION]

### Source [47]: https://www.salmanq.com/blog/llm-built-in-tools/

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: In from-scratch implementations using function tools (user-defined), you provide the LLM with a list of tools including name, natural language description, and JSON schema describing parameters. The model generates a structured JSON call based on this. Your code then uses registries or mappings to execute the specified function with those parameters and passes the result back to the model. This contrasts with built-in tools where no schema is provided, but function tools rely on such mappings to handle execution after LLM selection from the schema.

-----

Phase: [EXPLOITATION]

### Source [48]: https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: In custom agent implementations (from-scratch), you decide which tools to connect and provide them to the LLM. The workflow is: LLM recognizes need for a tool, selects which one from available options (implying a registry of tools), generates parameters, executes the tool, and integrates results. Tool selection from a registry of 3-5 essential tools prevents confusion; mappings facilitate looking up and executing the selected tool efficiently.

-----

Phase: [EXPLOITATION]

### Source [49]: https://www.adaline.ai/blog/understanding-llms-and-tool-calling

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: Tool calling workflow: 1. Define tools with JSONSchema (populating a schema registry like TOOLS_SCHEMA). 2. Call model with user query and function definitions. 3. Process response, executing requested functions (using a name-to-function mapping like TOOLS_BY_NAME). 4. Return results to model. Tools are defined in the tools parameter with name, description, input schema. The LLM returns structured tool_use response with function name and arguments, which the implementation maps to execution.

-----

</details>

<details>
<summary>How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?</summary>

Phase: [EXPLOITATION]

### Source [50]: https://docs.h2o.ai/enterprise-h2ogpte/tutorials/tutorial-10

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams are used to visualize agent actions in h2oGPTe. The objective is to generate Mermaid flowchart code that explains: what steps were taken by the agents, what tools or APIs were used, what decisions or branches were encountered, what errors occurred and how they were handled, and what the final outcome was. This clarifies decision points, tool usage, and error handling in agent workflows. Tips for creating diagrams include: avoiding quotes in node labels, not using parentheses (( or )), using <br /> for line breaks inside nodes, starting each node label with an appropriate emoji, and using appropriate node styles like classDef error (fill:#ffe6e6,stroke:#ff4d4d), success (fill:#e6ffe6,stroke:#00cc66), action (fill:#f0f8ff,stroke:#3399ff), decision (fill:#fff9e6,stroke:#ffcc66). Rendering methods: agent rendering in chat (success rate varies), Mermaid CLI (npm install -g @mermaid-js/mermaid-cli, create .mmd file, mmdc -i input.mmd -o output.png), or Mermaid Live Editor (paste code, view and download). If inaccurate, refine prompt or re-run. Manual review recommended for complex agents.

-----

Phase: [EXPLOITATION]

### Source [51]: https://www.awesome-testing.com/2025/09/mermaid-diagrams

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams visualize LLM function calling flows relevant to agent architectures. Example flowchart for single-turn and multi-tool loops: flowchart TD A[User Input] --> B[LLM Receives Prompt + Tool Schemas] B --> C{Should I use a tool?} C -- Yes --> D[LLM emits structured function call] D --> E[API routes call to tool handler] E --> F[Tool executes with parameters] F --> G[Tool returns result] G --> H[LLM integrates result] H --> I{Another tool needed?} I -- No --> J[LLM crafts final response] J --> K[Response sent to User] I -- Yes --> D C -- No --> J. This shows decision points (should use tool? another tool needed?), tool calling (structured function call, tool execution), loops (yes back to D for multi-tool), and integration (LLM integrates result into response). There's also an LLM Function Calling Sequence Diagram showing sequence of interactions. Mermaid supports native integrations in GitHub/GitLab for rendering in docs, enhancing clarity of complex workflows like AI agents and function calling. Collection of examples at mermaids GitHub repo covers AI agents, function calling workflows.

-----

Phase: [EXPLOITATION]

### Source [53]: https://ranjankumar.in/stop-pasting-screenshots-how-ai-engineers-document-systems-with-mermaid

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams document AI systems like agent architectures with tool orchestration. Essential patterns for AI engineers: LLM Agent Architecture with Tool Orchestration (flowchart showing query routing through paths). Subgraphs define system boundaries (stateful/stateless components). Example: graph LR A[Agent Router] --> B[Search Tool]; click A "link_to_code"; click B "link_to_code". Makes diagrams navigable to code. RAG system flowchart shows routing logic. Updates in repo docs/ folder sync with code changes. Visualizes tool orchestration, decisions, branches in agent flows. Patterns refined for production systems handling millions of queries.

-----

Phase: [EXPLOITATION]

### Source [54]: https://medium.com/@shuv.sdr/langgraph-architecture-and-design-280c365aaf2c

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams visualize multi-agent workflows in LangGraph as graphs showing nodes (individual agents/tasks), edges, and branching logic. Improves debugging/understanding complex AI workflows like sales report generation system. Each rectangle node represents an agent for specific tasks, illustrating integration in agent architectures.

-----

</details>

<details>
<summary>In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?</summary>

Phase: [EXPLOITATION]

### Source [55]: https://www.decodingai.com/p/tool-calling-from-scratch-to-production

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: Tool calling is at the core of what makes an AI agent useful. Understanding how to build, monitor, and debug tool interactions is one of the most important skills for an AI Engineer. By giving an LLM the ability to interact with the outside world, you transform it from a passive text generator into an active problem-solver. Tools are a fundamental pattern that can also power structured workflows. In the orchestrator-worker pattern, you can leverage the current tool infrastructure provided by all the AI frameworks or MCP servers to generate tool calls that can be executed in parallel later on in your code as you see fit. This article is part of the AI Agents Foundations series—a 9-part journey from Python developer to AI Engineer, covering topics like Workflows vs. Agents, Context Engineering, Structured Outputs, The 5 Workflow Patterns, and Tool Calling From Scratch.

-----

Phase: [EXPLOITATION]

### Source [56]: https://sparkco.ai/blog/advanced-tool-calling-in-llm-agents-a-deep-dive

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: The evolution of tool calling has transitioned from basic integrations to advanced capabilities involving structured reasoning and memory management. Frameworks such as LangChain, AutoGen, CrewAI, and LangGraph have played pivotal roles in this transformation. These frameworks offer robust tool calling schemas that allow LLMs to intelligently select and execute external APIs, databases, or custom functions, thus enhancing their ability to perform complex tasks. Tool calling refers to the ability of LLM agents to interact with external APIs, databases, or custom functions, thereby extending their utility and effectiveness. By 2025, tool calling has evolved from basic API integrations to encompass structured reasoning, robust memory management, and sophisticated agent orchestration. The historical development of tool calling in LLM agents has moved from simple API interactions to an intricate framework of structured reasoning, memory management, and advanced integration capabilities.

-----

Phase: [EXPLOITATION]

### Source [57]: https://composio.dev/content/ai-agent-tool-calling-guide

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: The shift from 'chatbots' to 'AI agents' hinges on a single technical capability: Tool Calling. Tool Calling provides the I/O layer for LLMs, allowing them to execute actions and access real-time data. Tool Calling transforms LLMs from passive text generators into active agents that interact with external systems like Salesforce or GitHub. Tool Calling is the mechanism. The fundamental ability of a model to output structured JSON arguments instead of text. It allows the brain (LLM) to manipulate objects. For engineering leaders evaluating integration strategies, you need to separate the core mechanism (Tool Calling) from the discovery standards (Tool Search) and the emerging interface protocols (MCP). The real challenge isn’t the LLM’s reasoning, but the complex engineering required for secure and reliable tool execution (auth, error handling, etc.). This guide dissects the modern tool calling stack, moving from foundational concepts to enterprise architecture.

-----

Phase: [EXPLOITATION]

### Source [58]: https://galileo.ai/blog/7-essential-skills-for-building-ai-agents

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: Building AI agents demands technical skillsets that extend beyond traditional software development. As enterprises deploy AI agents in production environments, tasks like model evaluation, hallucination detection, and system monitoring require specialized expertise and robust development patterns. This article examines the essential skills required for building robust, production-ready AI agents, focusing on advanced development patterns that drive successful AI agent development.

-----

Phase: [EXPLOITATION]

### Source [59]: https://www.getmaxim.ai/articles/understanding-tool-calling-mechanisms-in-ai-agents-a-deep-dive-into-execution-efficiency/

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: Tool calling is the mechanism by which an AI agent decides to use external tools—functions, APIs, databases, or retrieval pipelines—while solving a task. Efficient execution depends on deterministic planning, low-latency routing, robust observability, and evaluations that quantify correctness and cost. Engineering teams should standardize on an AI gateway with distributed tracing, semantic caching, failover, and governance; pair this with pre-release simulations and in-production observability to ensure reliable, scalable agent behavior. Use structured schemas, measurable evals, and prompt versioning to drive continuous improvement. Maxim AI’s full-stack approach addresses this lifecycle end-to-end: experimentation, simulation, evaluation, observability, and data curation for multimodal agents.

-----

</details>

<details>
<summary>Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?</summary>

Phase: [EXPLOITATION]

### Source [91]: https://apxml.com/courses/agentic-llm-memory-architectures/chapter-4-complex-planning-tool-integration/tool-description-selection

Query: Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?

Answer: 1. Tool Name: A unique identifier for the tool.
2. Purpose/Functionality: A clear, concise explanation of what the tool achieves and when it is applicable. This should be descriptive enough for the LLM to differentiate it from other tools.
3. Input Parameters: Detailed specification of required and optional inputs, including:
    Parameter names.
    Data types (e.g., string, integer, boolean, list).
    Descriptions explaining the purpose and expected format of each parameter.
4. Output Specification: Description of the data or result returned by the tool upon successful execution. This helps the agent understand what information to expect back. [...] Clarity and Conciseness: Ensure descriptions are unambiguous but avoid excessive verbosity that consumes valuable context window space.
 Formatting: Presenting the tool list in a structured, easily parsable format (like lists or code blocks) can help the LLM.
 Instructions: Explicitly instructing the LLM on the selection task (e.g., "Choose the best tool from the list below to achieve the current objective...") is important.

#### Managing Numerous Tools

As the number of available tools grows, simply listing all descriptions in every prompt becomes inefficient and may exceed context limits. Strategies to manage this include: [...] ```
  { "name": "get_stock_price", "description": "Retrieves the current stock price for a given ticker symbol.", "parameters": { "type": "object", "properties": { "ticker_symbol": { "type": "string", "description": "The stock ticker symbol (e.g., 'GOOGL', 'MSFT')." } }, "required": ["ticker_symbol"] } // Potentially add output schema description here as well } 
  ```

The choice of format often depends on the complexity of the tools, the agent framework being used, and the capabilities of the underlying LLM (e.g., native support for function calling based on structured schemas). Combining structured definitions with clear natural language descriptions within those structures often yields the best results.

### Mechanisms for Tool Selection

-----

Phase: [EXPLOITATION]

### Source [92]: https://milvus.io/ai-quick-reference/how-does-an-llm-handle-ambiguous-or-multipurpose-tools

Query: Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?

Answer: To handle multi-purpose tools, LLMs often map the tool’s functionality to specific tasks by referencing structured descriptions or API documentation. For instance, a tool like `curl` can transfer data, test APIs, or download files. If a user asks, “How do I fetch JSON data from an API?” the model might prioritize the `-H "Accept: application/json"` flag in `curl` to align with the task. The model also weighs probabilities—if a tool is commonly used for a specific purpose in its training data (e.g., `git` primarily for version control), it defaults to that use case unless conflicting context exists. This approach reduces errors but requires clear user input or system-provided tool metadata to improve accuracy.

`curl`
`-H "Accept: application/json"`
`curl`
`git` [...] Developers can enhance an LLM’s handling of ambiguous tools by providing explicit constraints or metadata. For example, if a tool’s API defines separate endpoints for different operations (e.g., `/send-email` vs. `/schedule-meeting`), the model can route requests more precisely. Additionally, fine-tuning the model with domain-specific examples—like distinguishing between a “pipeline” in DevOps versus data engineering—helps it recognize niche contexts. However, limitations remain: if user input lacks clarity (e.g., “run the analyzer”), the model might default to a generic or statistically common interpretation. To mitigate this, systems can prompt users for disambiguation or integrate validation layers to confirm tool usage before execution.

`/send-email`
`/schedule-meeting` [...] Milvus
Zilliz
Milvus
Zilliz

How does an LLM handle ambiguous or multi-purpose tools?

# How does an LLM handle ambiguous or multi-purpose tools?

Large language models (LLMs) handle ambiguous or multi-purpose tools by analyzing context, leveraging patterns from training data, and prioritizing the most likely interpretation based on user intent. When a tool’s purpose isn’t clear, the model relies on surrounding information to infer how the tool should be used. For example, if a user mentions “using a bat” in a sentence, the LLM might determine whether “bat” refers to an animal or a baseball bat based on adjacent words like “sports” or “cave.” Similarly, for software tools like a CLI command with overlapping flags, the model uses syntax, parameters, or user history to resolve ambiguity.

-----

Phase: [EXPLOITATION]

### Source [93]: https://arxiv.org/html/2602.20426

Query: Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?

Answer: ### 4.4 Tool Scaling Experiments

Benchmarks such as StableToolBench provide a limited set of relevant tools for each complex user queries. In practice, however, it is often unrealistic to manually restrict the candidate set to a small, carefully selected subset for each query (Qu et al., 2024).
Instead, agents are commonly exposed to many irrelevant tools, which increases the difficulty of tool selection. Here, we study how different versions of tool descriptions affect agent performance when the number of available tools scales up to the level of 100100 tools. [...] for broad utility and can be applied across many tasks. In contrast, domain-specific tools or APIs are tailored for particular applications, such as retrieving weather data, managing to-do lists, or querying specialized databases. These APIs typically require structured input arguments and return domain-specific outputs, making correct selection and invocation more challenging. In this work, we focus on domain-specific tools. As platforms such as RapidAPI, TMDB, and Spotify provide a large number of APIs with real-world responses, making accurate and informative tool descriptions especially critical for the performance of tool-using agents. [...] Tool Interface Improvement.
Tool interfaces play an important role in guiding tool-using agents towards accurate tool selection and usage.
 (Xu et al., 2023) incorporate both usage examples and tool descriptions to improve agents. However, collecting high-quality tool use examples for each tool is challenging while  (Hsieh et al., 2023) show that tool descriptions can support zero-shot tool usage.
Results from (Bandlamudi et al., 2025; Chen et al., 2025; Faghih et al., 2025) all show the importance of tool descriptions.  (Chen et al., 2025) add a new role in the chat message for tool descriptions to improve tool calling performance.

-----

Phase: [EXPLOITATION]

### Source [94]: https://www.tdcommons.org/cgi/viewcontent.cgi?article=9446&context=dpubs_series

Query: Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?

Answer: implementation, does not provide the flexibility when multiple tool implementations exist for the 

same capability. 

DESCRIPTION 

This disclosure describes a tool selection procedure for agentic LLMs that separates or 

provides a loose coupling between tool capability and tool implementation. Accuracy and 

flexibility of tool selection is improved, especially when multiple tool impleme ntations with 

similar capabilities exist. The techniques result in the separation of responsibility between ML 

developers (who develop LLM agents) and ML administrators (who govern or manage the tools 

used by the LLM agents). Certain definitions follow. 

● Tool capability refers to a set of abstract resource definitions within an enterprise. For [...] be selected based on user query by the underlying LLM. The selection of an appropriate tool 

from the set of available tools is done by matching the user query to the tool name, description, 

etc. This tightly coupled process may not provide the flexibility wherein multiple tool 

implementations are available for one capability. 

For example, an LLM agent can be provided with two tools, one related to ‘stock quotes’ 

and one related to ‘weather updates.’ Sufficient description of tools is available to advertise their 

capabilities to the LLM. When a user query about stock quote is re ceived, the LLM agent action 

will involve invoking the tool providing the stock quote based on the tool name and description. [...] most appropriate tool implementation registered under that capability. This design enables fine -

grained tool selection, dynamic adaptability, an d operational cost savings. It also introduces clear 

role separation between ML developers that define agent capabilities and ML administrators that 

manage tool implementations, improving maintainability and governance. By allowing agents to 

operate indepe ndently of specific tools, the framework enhances precision and flexibility in 

multi -tool LLM agents. The described techniques can be utilized by any entity that is involved in 

building LLMs and agentic frameworks. 

> 10
> Jagannath: Tool Selection by Large Language Model (LLM) Agents
> Published by Technical Disclosure Commons, 2025

REFERENCES

-----

Phase: [EXPLOITATION]

### Source [95]: https://towardsai.net/p/artificial-intelligence/tool-descriptions-are-critical-making-better-llm-tools-research-capability

Query: Why must tool description fields in schemas be clear, articulate and mutually distinguishing for the LLM to decide appropriate tool calls based on user queries, with examples of confusing generic descriptions versus explicit ones like "search documents on Google Drive" versus "search files on disk", how does this become crucial when scaling to 50-100 tools, and what role does instruction fine-tuning play in enabling LLMs to interpret schemas and generate structured tool call outputs like JSON or Pydantic?

Answer: ```
#In web.py, def brave_web_search()#We update its last line from:return response.json()#...to:message = "Web search results: \n" + json.dumps(response.json()) + "\nThe information here are just summaries. Use fetch_web_page tool to retrieve real content for in-depth information, especially for research purposes."return message#In web.py, def brave_web_search()#We update its last line from: return#...to:"Web search results: \n""\nThe information here are just summaries. Use fetch_web_page tool to retrieve real content for in-depth information, especially for research purposes." return
``` [...] not return "error" "BRAVE_API_KEY environment variable not found" # Prepare the API request" "Accept""application/json""Accept-Encoding" "gzip""X-Subscription-Token" "q" "count" # Make the API request # Raise an exception for HTTP errors # Return the JSON response return except as return "error"f"API request failed: {str(e)}"{str(e)} str except return "error" "Failed to decode JSON response" except as return "error"f"An unexpected error occurred: {str(e)}"{str(e)} str [...] ```

-----

</details>

<details>
<summary>Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?</summary>

Phase: [EXPLOITATION]

### Source [96]: https://dev.to/inozem/one-tool-calling-interface-for-openai-claude-and-gemini-2l1c

Query: Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?

Answer: `tool_calls`
`tool_use`
`functionCall`
`functionResponse`

These are not just syntax differences.\  
They require different request structures, response parsing, and execution loops.

Supporting multiple providers usually leads to:

The result is more code, more bugs, and much harder provider switching.

To simplify this, I built llm-api-adapter — a small Python library that provides one unified interface for multiple LLM APIs.

Define tools once and run the same application logic across OpenAI, Anthropic, and Gemini.

# Architecture

The adapter acts as a translation layer between your application and LLM providers. [...] `Application Logic
│
▼
UniversalLLMAPIAdapter
│
▼
Provider Translation Layer
│
▼
┌─────────────┬─────────────┬─────────────┐
│ OpenAI │ Anthropic │ Gemini │
│ tool_calls │ tool_use │ functionCall│
└─────────────┴─────────────┴─────────────┘`

Your application communicates with one interface, while the adapter converts requests and responses to the provider-specific formats.

# Installation

`pip install llm-api-adapter`

# The "Strawberry" problem

A classic example showing why tool calling matters:

`How many "r" letters are in "strawberry"?`

The correct answer is 3, but models often fail because they reason over tokens, not characters.

Best practice is:

Let the LLM reason, but delegate deterministic tasks to code.

This is exactly what tool calling enables.

# Defining a tool once [...] # Defining a tool once

With llm-api-adapter, tools are defined using a provider-agnostic schema.

`from llm_api_adapter.models.tools import ToolSpec
tools = [
ToolSpec(
name="count_letter_in_word",
description="Count how many times a specific letter appears in a word",
json_schema={
"type": "object",
"properties": {
"word": {"type": "string"},
"letter": {"type": "string", "minLength": 1, "maxLength": 1},
},
"required": ["word", "letter"],
"additionalProperties": False,
},
)
]`

The adapter automatically converts this schema to:

`tools`
`tool_use`
`functionCall`

# Running the same code across providers

The application logic remains identical.

Only the provider name, model, and API key change.

-----

Phase: [EXPLOITATION]

### Source [97]: https://apxml.com/courses/prompt-engineering-llm-application-development/chapter-4-interacting-with-llm-apis/overview-common-llm-apis

Query: Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?

Answer: ### Common API Functionality

Despite the different providers and models, most LLM APIs share a core set of functionalities accessed through specific endpoints: [...] A number of providers offer access to state-of-the-art LLMs through APIs. While the specific implementation details vary, the fundamental concept remains consistent: you send a request containing your prompt and configuration parameters, and the provider's service processes it using their LLM, returning the result.

Here's a look at some prominent providers and their offerings:

### Major LLM API Providers [...] OpenAI: Perhaps the most widely known provider, OpenAI offers APIs for accessing models like GPT-4, GPT-4o, and GPT-3.5-Turbo. Their APIs are well-documented and have seen extensive adoption, making them a common starting point for many developers. They typically utilize a "chat completions" format, where interactions are structured as a sequence of messages with roles (system, user, assistant).
 Anthropic: Anthropic provides APIs for their Claude family of models (e.g., Claude 3 Opus, Sonnet, and Haiku). They place a strong emphasis on AI safety and helpfulness, often building models based on principles outlined in a "constitution." Their API structure is similar in concept to OpenAI's but has its own specific format for requests and responses.

-----

Phase: [EXPLOITATION]

### Source [98]: https://mongoengine.org/best-llm-apis-for-developers/

Query: Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?

Answer: ### Why This Comparison Matters More in 2025

According to the Stanford AI Index 2024, the number of LLM API providers offering production-grade services tripled between 2022 and 2024. Developer lock-in is a real risk — switching providers mid-project means re-engineering prompts, adjusting rate-limit logic, and retraining your team. Getting the initial choice right saves weeks of rework.

## 1. OpenAI GPT-4o: The Default Choice and Its Limits

### Why GPT-4o Dominates Mindshare

OpenAI’s GPT-4o remains the most widely adopted LLM API for developers, largely because it was first to market with reliable, well-documented tooling. Its Python SDK is mature, its function-calling interface is consistent, and its 128K token context window handles most real-world document tasks without chunking. [...] ### Google Ecosystem Lock-In

The Gemini API’s tightest advantage is its integration with Google Cloud — Vertex AI, BigQuery, and Google Workspace. If your infrastructure already runs on GCP, using Gemini means unified billing, native IAM, and direct data access without copying data across clouds.

The trade-off is that Gemini’s SDK and documentation lag behind OpenAI’s in maturity. Error messages are less descriptive, streaming behavior has had documented inconsistencies, and the function-calling interface changed significantly between API versions in 2024 — a headache for teams that had already built integrations.

## 4. Meta Llama 3: Open Source Power and Self-Hosting Reality

### Why Open Source Changes the Economics

-----

Phase: [EXPLOITATION]

### Source [99]: https://stevekinney.com/writing/prompt-engineering-frontier-llms

Query: Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?

Answer: `<instructions>
You are a debugging assistant. Help the user diagnose application errors.

Tool usage policy:
- Use search_logs when you need log data that is not already in the
 conversation context.
- Use query_database ONLY with the specific query patterns listed in the
 tool description. Do not construct arbitrary SQL.
- Use get_file when you need to examine source code referenced in logs
 or error messages.
- Do not call tools speculatively. If you can answer from existing context,
 do so.
- If you are unsure whether a tool call is needed, explain what you would
 search for and ask the user to confirm. [...] The mental model: anything that isn’t your developer/system instruction is untrusted input. User messages, obviously. But also retrieved documents, tool call results, scraped web content, and file uploads. All of it can contain adversarial instructions.

### Defensive patterns

Use the instruction hierarchy. OpenAI’s developer/user message split exists partly for this reason—research on formal instruction hierarchies shows improved robustness against injection by teaching models to prioritize higher-authority instructions. Place your security constraints in the highest-authority position your API supports. [...] The iteration loop ties it together:

This loop isn’t glamorous, but it’s the difference between “it seemed to work when I tried it” and “I have evidence that this prompt performs well across 500 test cases.” OpenAI provides an Evals framework for continuous evaluation. Anthropic provides console tooling for side-by-side comparisons and prompt versioning. Gemini offers logging and datasets in its developer tooling for observation and reruns. The tooling differs, but the discipline is the same.

## What This Adds Up To

-----

Phase: [EXPLOITATION]

### Source [100]: https://grokipedia.com/page/Comparison_of_large_language_model_APIs

Query: Why do all popular LLM provider APIs including OpenAI and Anthropic follow essentially the same core logic as Gemini for instructing models on tool usage via configurations like GenerateContentConfig despite only minimal differences in their interfaces, allowing the from-scratch, decorator and Gemini-native lessons to be directly extrapolated to any chosen API after implementing production-level tool calls?

Answer: and `server_tool_use` for features like web search requests).(#ref-36)](#ref-36) Zhipu AI's GLM-4 API closely mirrors OpenAI's format for compatibility, delivering a JSON response with `id`, `created` (Unix timestamp), `model`, optional `request_id`, `choices` (array including `index`, `finish_reason` like "stop" or "length", and `message` with `role` ("assistant"), `content`, and optional `tool_calls` detailing `id`, `type`, and `function` parameters), and `usage` (breakdown of `prompt_tokens`, `completion_tokens`, and `total_tokens`).(#ref-43)](#ref-43) This near-identical schema allows developers to integrate GLM-4 with minimal code changes from OpenAI-based applications, including support for tool calls in a similar nested structure. In contrast, Google's Gemini API uses a [...] The endpoint structures for large language model APIs among major providers exhibit a mix of standardization and divergence, primarily revolving around RESTful HTTP interfaces that facilitate chat completions or message generations. OpenAI's API serves as a de facto reference, with its base URL at ` and the primary endpoint path `/chat/completions` accessed via the POST method, enabling developers to submit conversation messages for model responses.(#ref-35)](#ref-35) This structure emphasizes simplicity and versioning at the base level, allowing seamless integration for generative tasks. Anthropic's Claude API aligns partially with this model but introduces distinct versioning in the path. Its base URL is ` with the primary endpoint `/v1/messages` also using the POST method for creating [...] Large language model APIs generally support streaming to deliver responses incrementally, enabling real-time applications such as chat interfaces, while asynchronous features) allow non-blocking calls for efficient handling of long-running generations.(#ref-47)](#ref-47)(#ref-48)](#ref-48)(#ref-49)](#ref-49)(#ref-50)](#ref-50) This section examines these capabilities across OpenAI's GPT series, Anthropic's Claude, Zhipu AI's GLM-4, and Google's Gemini, highlighting similarities in server-sent events (SSE) usage and variations in implementation. OpenAI's API enables streaming by setting the `stream` parameter to `true` in chat completion requests, which triggers SSE to emit events as the model generates output, with each chunk containing delta updates in the `choices` array for

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What are the key theoretical reasons and empirical evidence showing why clear, distinctive tool descriptions and explicit system prompt instructions are critical for preventing disambiguation failures and improving reliability when scaling agents to manage 50-100 tools?</summary>

Phase: [EXPLORATION]

### Source [60]: https://www.getmaxim.ai/articles/the-importance-of-system-prompts-in-shaping-ai-agent-responses/

Query: What are the key theoretical reasons and empirical evidence showing why clear, distinctive tool descriptions and explicit system prompt instructions are critical for preventing disambiguation failures and improving reliability when scaling agents to manage 50-100 tools?

Answer: System prompts function as the operational blueprint for AI agents, defining their behavior, constraints, and decision-making frameworks before any user interaction occurs. Well-crafted system prompts ensure AI agents maintain consistency, follow ethical guidelines, and produce reliable outputs across complex multi-step workflows. Research shows that even minor variations in prompts can lead to complete changes in output distribution, making systematic prompt engineering critical for production AI applications. Teams leveraging comprehensive system prompts report significant improvements in agent performance, with proper prompt design serving as the foundation for trustworthy AI systems. AI agents differ fundamentally from simple chatbots. Agents make decisions dynamically for an indeterminate number of steps, adjusting as needed, rather than following predefined workflows. This autonomy makes system prompts exponentially more critical. Agents must decide when to search their memory, when to use external tools, how to maintain context across conversations, and how to structure responses consistently. System prompts coordinate all these capabilities, functioning as the central nervous system for autonomous AI systems. Well-structured system prompts ensure AI models behave in controlled, predictable, and useful manners, significantly improving performance in agentic workflows. The evidence is clear: teams that invest in systematic prompt engineering, comprehensive testing, and continuous refinement build more reliable, consistent, and trustworthy AI systems.

-----

Phase: [EXPLORATION]

### Source [61]: https://www.anthropic.com/engineering/writing-tools-for-agents

Query: What are the key theoretical reasons and empirical evidence showing why clear, distinctive tool descriptions and explicit system prompt instructions are critical for preventing disambiguation failures and improving reliability when scaling agents to manage 50-100 tools?

Answer: Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs. Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don’t build) can really pay off. Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use. Namespacing your tools helps distinguish them. When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`. Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors or give examples of correctly formatted tool inputs. Prompt-engineering your tool descriptions and specs is one of the most effective methods for improving tools: because these are loaded into your agents’ context, they can collectively steer agents toward effective tool-calling behaviors.

-----

Phase: [EXPLORATION]

### Source [62]: https://galileo.ai/blog/why-most-ai-agents-fail-and-how-to-fix-them

Query: What are the key theoretical reasons and empirical evidence showing why clear, distinctive tool descriptions and explicit system prompt instructions are critical for preventing disambiguation failures and improving reliability when scaling agents to manage 50-100 tools?

Answer: One key benefit of agent abstraction over prompting base language models is the ability to solve complex problems by calling multiple tools to interact with external systems and data sources. Robust tool calling mechanisms ensure that agents can perform complex tasks by leveraging various tools accurately and efficiently. However, agents often face challenges in effectively calling and using these tools. Tool calling failures can occur due to incorrect parameter passing, misinterpretation of tool outputs, or failures in integrating tool results into the agent's workflow. Define Clear Parameters: Ensure that tools have well-defined parameters and usage guidelines. In single-agent systems, one language model performs all reasoning, planning, and tool execution. The agent is given a system prompt and any necessary tools to complete its task. Scaling agents to handle increased workloads or more complex tasks is a significant challenge. As the number of agents or the complexity of interactions grows, the system must efficiently manage resources, maintain performance, and ensure reliability. Scalable Architectures: Design architectures that can efficiently manage increased workloads and complexity.

-----

Phase: [EXPLORATION]

### Source [63]: https://arxiv.org/html/2503.13657v2

Query: What are the key theoretical reasons and empirical evidence showing why clear, distinctive tool descriptions and explicit system prompt instructions are critical for preventing disambiguation failures and improving reliability when scaling agents to manage 50-100 tools?

Answer: Failures in multi-agent LLM systems (MAS) can stem from inherent design issues beyond user prompt ambiguity. For example, even with explicit prompts like 'without having a fixed word bank, and randomly select a new 5-letter word each day,' ChatDev produces code with a fixed word list and introduces new errors, suggesting failures from the MAS’s design for interpreting specifications. The paper introduces MAST, the first empirically grounded taxonomy of MAS failures, and a scalable LLM-as-a-judge evaluation pipeline for analyzing performance and diagnosing failure modes. Case studies demonstrate that failures often stem from system design issues, not just LLM limitations or simple prompt following, requiring structural MAS redesigns rather than superficial fixes.

-----

</details>

<details>
<summary>What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?</summary>

Phase: [EXPLORATION]

### Source [65]: https://docs.pydantic.dev/2.7/concepts/models

Query: What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?

Answer: Pydantic models face challenges with forward references and recursive structures. For example, defining a model Foo with x: 'Bar' where Bar is undefined raises PydanticUserError when generating model_json_schema(), stating 'Foo is not fully defined; you should define Bar, then call Foo.model_rebuild()'. Pydantic attempts automatic detection but may require explicit model_rebuild() for recursive models or generics to ensure proper schema generation with $defs and $ref.

Generics are supported via Generic[DataT], as in Response(BaseModel, Generic[DataT]) with data: Optional[DataT] = None. Instantiations like Response[int] or Response[DataModel] work, but validation fails if input doesn't match, e.g., Response[int] rejects string 'value' with ValidationError for type=int_parsing.

Model signatures are generated accurately via inspect.signature, respecting Field aliases (e.g., apple: int = Field(alias='pear') appears as pear: int) and custom __init__ methods, including variadic args like *args. This supports introspection for libraries like FastAPI.

Optional parameters are handled with Optional[str] = None or defaults like str = 'Foo'. Nested models like DataModel inside Response require proper typing for dump and validation.

-----

Phase: [EXPLORATION]

### Source [66]: https://pydantic.dev/docs/validation/latest/get-started/changelog/

Query: What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?

Answer: Pydantic changelog highlights numerous fixes for schema generation and validation challenges relevant to inferring schemas from complex signatures:

- Fix schema build for nested dataclasses / TypedDicts with discriminators (#8950).
- Remove unnecessary logic for definitions schema gen with discriminated unions (#8951).
- Fix handling of optionals in mypy plugin (#9008).
- Fix default value serializing (#9066).
- Fix ClassVar forward ref inherited from parent class (#9097).
- Fix walrus operator precedence in UrlConstraints.__get_pydantic_core_schema__() (#12826).
- Fix support for enums with NamedTuple as values (#12506).
- Refactor __pydantic_extra__ annotation handling (#12563).
- Do not eagerly evaluate annotations in signature logic (#12660).

Other fixes address nested unions, recursive structures, generics cache with free threading (#12537), tagged union serializers (#12594), and serialization warnings for nested models (#12635). These indicate engineering challenges in accurately inferring and generating schemas for nested models, optionals, generics, forward refs, discriminated unions, and custom annotations without performance overhead or errors.

-----

Phase: [EXPLORATION]

### Source [67]: https://www.datacamp.com/tutorial/pydantic

Query: What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?

Answer: Pydantic handles optional parameters via model_dump(exclude_none=True), removing unprovided fields for PATCH requests to avoid overwrites. Custom validation logic is implemented with field validators and model validators for business rules like varying password requirements or multi-country postal codes, integrating with FastAPI.

Challenges include overhead compared to dataclasses, though negligible versus bug prevention. Production apps require custom validation beyond standard types, smoothly integrating with frameworks and config. Serialization and validation scale with app growth, but complex nested structures and custom rules demand careful implementation.

-----

Phase: [EXPLORATION]

### Source [68]: https://realpython.com/python-pydantic/

Query: What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?

Answer: Custom validation uses model validators (@model_validator) and field validators (@field_validator) for arbitrary logic, e.g., blocking elected_benefits=True for IT department. Validation errors detail issues like enum mismatches, parsing failures for dates, numbers, booleans.

Pydantic supports nested structures and primitives with high customization. Flexibility in strictness: coerce types (int to float) or enforce strictly. Validation decorators validate functions beyond BaseModel, but complex custom logic requires precise implementation to handle nested data without limits.

-----

Phase: [EXPLORATION]

### Source [69]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/

Query: What specific engineering challenges arise when implementing a @tool decorator to automatically infer schemas from complex Python signatures involving optional parameters, generics, nested Pydantic models, and custom validation logic in lightweight frameworks?

Answer: Pydantic models use Optional[str] = None for optional parameters. Custom validation via @field_validator, e.g., cleaning phone numbers. Automatic validation inherits from BaseModel. For function calling or parsing, explicit control needed, indicating challenges in automatic schema inference for complex signatures in lightweight setups.

-----

</details>

<details>
<summary>What quantitative analyses or case studies reveal the precise mechanisms of error propagation, latency accumulation, and strategy fixation in sequential tool loops that lack pauses for LLM interpretation of intermediate results?</summary>

Phase: [EXPLORATION]

### Source [70]: https://openreview.net/forum?id=8wlgtUBSK4

Query: What quantitative analyses or case studies reveal the precise mechanisms of error propagation, latency accumulation, and strategy fixation in sequential tool loops that lack pauses for LLM interpretation of intermediate results?

Answer: The paper introduces the first theoretical framework for analyzing error accumulation in Model Context Protocol (MCP) agents, proving that cumulative distortion exhibits linear growth and high-probability deviations bounded by O(√T). This concentration property ensures predictable system behavior and rules out exponential failure modes. They develop a hybrid distortion metric combining discrete fact matching with continuous semantic similarity, then establish martingale concentration bounds on error propagation through sequential tool interactions. Experiments across Qwen2-7B, Llama-3-8B, and Mistral-7B validate theoretical predictions, showing empirical distortion tracks the linear trend with deviations consistently within O(√T) envelopes. Key findings include: semantic weighting reduces distortion by 80%, and periodic re-grounding approximately every 8 steps suffices for error control. Modeling MCP tool-use as a martingale, they prove sublinear distortion deviation and derive a periodic re-grounding rule; validated on Qwen2, Mistral, and Llama-3.

-----

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2604.02375v1

Query: What quantitative analyses or case studies reveal the precise mechanisms of error propagation, latency accumulation, and strategy fixation in sequential tool loops that lack pauses for LLM interpretation of intermediate results?

Answer: In ReAct sequential think-act-observe, turn i carries c + i k tokens, total ≈ O(n² k). With strict sequential dispatch, latency is O(n). Modern implementations with parallel function calling reduce this to O(t) where t is the number of reasoning turns; t ≪ n (measurements show 3–9 turns for 6–14 tool calls). Token complexity remains O(n² k) because all results accumulate in context across turns, degrading cost and attention quality on longer tasks. ReAct established sequential tool use with O(n² k) token complexity and original O(n) latency. Each turn appends tool results to growing context. Case study: DAG system vs. conversational agent on computational astronomy benchmark; DAG completed query in 31.7 seconds with 7 nodes vs. sequential approach.

-----

Phase: [EXPLORATION]

### Source [72]: https://myengineeringpath.dev/genai-engineer/agent-debugging

Query: What quantitative analyses or case studies reveal the precise mechanisms of error propagation, latency accumulation, and strategy fixation in sequential tool loops that lack pauses for LLM interpretation of intermediate results?

Answer: Agent failures are non-deterministic; depend on LLM output, user request, tool results, accumulated context. Layer 3: Context accumulation. Each iteration adds to context window. LLM reasoning at step 7 depends on steps 1-6. Small deviation in step 3 (different tool result, phrasing) cascades to different decision at step 7. This path dependence makes failures hard to reproduce. In agent systems, reproducing failure requires replaying exact sequence of LLM outputs, tool results, in exact context state. Without trace recording, impossible. Pattern 2: Fallback strategies for tool failures provide alternative paths rather than terminating.

-----

</details>

<details>
<summary>How are tool-calling patterns from LLM agents being adapted and extended in the design of collaborative human-AI systems for complex decision-making in fields like healthcare diagnostics or legal analysis?</summary>

Phase: [EXPLORATION]

### Source [74]: https://arxiv.org/html/2512.16301v1

Query: How are tool-calling patterns from LLM agents being adapted and extended in the design of collaborative human-AI systems for complex decision-making in fields like healthcare diagnostics or legal analysis?

Answer: ToolFlow (NAACL 2025) is a data synthesis pipeline designed to enhance the tool-calling capabilities of LLMs through the generation of natural and coherent dialogues. Traditional SFT approaches rely on synthetically generated tool-call data, but suffer from low diversity and limited coherence due to random tool sampling and single-turn interactions. ToolFlow introduces Graph-based Sampling, constructing a tool graph based on parameter and return-value similarities between tools, with nodes as tools and edges indicating relevance, allowing selection of tool subsets likely to interact effectively for complex user requirements. Planned Generation enables the LLM to create a high-level dialogue plan organizing user requests across multiple turns, including tool-call tasks and non-tool interactions, ensuring logical consistency and natural flow. This provides high-quality multi-turn tool-call dialogues reflecting real-world scenarios. At the core of agentic AI systems is a foundation model (LLM or multimodal) for reasoning, planning, and interaction, complemented by components extending autonomy in complex environments.

-----

Phase: [EXPLORATION]

### Source [75]: https://github.com/AGI-Edgerunners/LLM-Agents-Papers

Query: How are tool-calling patterns from LLM agents being adapted and extended in the design of collaborative human-AI systems for complex decision-making in fields like healthcare diagnostics or legal analysis?

Answer: Papers listed include: [2024/10/17] MeNTi: Bridging Medical Calculator and LLM Agent with Nested Tool Calling. [2024/10/16] MedAide: Towards an Omni Medical Aide via Specialized LLM-based Multi-Agent Collaboration. [2024/10/02] Zodiac: A Cardiologist-Level LLM Framework for Multi-Agent Diagnostics. [2024/08/28] Interactive Agents: Simulating Counselor-Client Psychological Counseling via Role-Playing LLM-to-LLM Interactions. [2024/08/23] DrugAgent: Explainable Drug Repurposing Agent with Large Language Model-based Reasoning. [2024/03/05] AgentsCourt: Building Judicial Decision-Making Agents with Court Debate Simulation and Legal Knowledge Augmentation. Recent papers: [2025/05/31] MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning. [2025/05/30] MedOrch: Medical Diagnosis with Tool-Augmented Reasoning Agents for Flexible Extensibility. [2025/05/27] Silence is Not Consensus: Disrupting Agreement Bias in Multi-Agent LLMs via Catfish Agent for Clinical Decision Making. [2025/05/27] BehaviorSFT: Behavioral Token Conditioning for Clinical Agents Across the Proactivity Spectrum. [2025/05/24] DDO: Dual-Decision Optimization via Multi-Agent Collaboration for LLM-Based Medical Consultation. These indicate adaptations in healthcare diagnostics (e.g., nested tool calling, multi-agent collaboration, tool-augmented reasoning) and legal analysis (e.g., judicial decision-making agents).

-----

Phase: [EXPLORATION]

### Source [76]: https://arxiv.org/html/2602.04813v1

Query: How are tool-calling patterns from LLM agents being adapted and extended in the design of collaborative human-AI systems for complex decision-making in fields like healthcare diagnostics or legal analysis?

Answer: LLM-based agents in healthcare integrate advanced reasoning and planning for complex tasks like differential diagnosis and real-time patient monitoring, automating workflows such as patient triage, laboratory result interpretation, and EHR management. As Agentic AI systems, they augment clinical decision making through interactive dialogues fostering collaboration between medical professionals and AI. They facilitate continuous medical education with real-time clinical knowledge access. Architectures with episodic and semantic memory maintain continuity across interactions, improving task accuracy. Adaptive learning via RLHF refines behavior with user input. Impact evident in healthcare, law, enabling intelligent, adaptive systems reshaping decision-making.

-----

Phase: [EXPLORATION]

### Source [77]: https://awellhealth.com/blog/llm-model-scoring-hides-ai-agent-performance

Query: How are tool-calling patterns from LLM agents being adapted and extended in the design of collaborative human-AI systems for complex decision-making in fields like healthcare diagnostics or legal analysis?

Answer: In healthcare, AI agents are defined as a digital teammate powered by an LLM that observes its environment, uses the model to plan next steps, and executes by calling the right tools - cycling through a “see-think-do” loop governed by guardrails until the job is done or handed off to a human. This describes tool-calling patterns in collaborative human-AI systems for complex decision-making.

-----

</details>

<details>
<summary>What historical parallels exist between modern LLM function calling and earlier AI paradigms like expert systems or planning agents from the 1980s-2000s, and what forgotten lessons could improve current agent reliability?</summary>

Phase: [EXPLORATION]

### Source [78]: https://blog.theunscalable.com/p/expert-systems-what-can-we-learn-from-its-rise-and-fall

Query: What historical parallels exist between modern LLM function calling and earlier AI paradigms like expert systems or planning agents from the 1980s-2000s, and what forgotten lessons could improve current agent reliability?

Answer: Expert systems are AI programs that achieve competence in performing a specialized task by reasoning with a body of knowledge about the task and the task domain. Today's LLMs alleviate the need for exact rule distillation and have the capability of doing reasoning leaps, but they have similar limitations to inference engines. They need us to pass the context mostly in natural language format and they can’t discover and track their context themselves. However, lots of knowledge, past experiences and current situations can’t be coded explicitly as natural languages. Drawing lessons from expert systems, one question to be answered about today’s LLM Agents would be, what kind of knowledge and situation can be economically engineered as context consumable by LLMs, and which applications would have enough residual value after context engineering and maintenance? Applying to the right areas would be the key to the success of LLM agents. To take a step further, if we want today’s LLM agents to overcome those limitations, we need them to be able to self-learn. At that point, the limit of language goes away - the agents will have their internal representation of accumulated knowledge and current situations, while language is only a way for external communication. Self learning was an articulated yet unfulfilled goal during the expert system era, and it would need to be the goal for the next generation agents as well.

-----

Phase: [EXPLORATION]

### Source [79]: https://www.linkedin.com/pulse/day-1-evolution-ai-agents-from-rule-based-systems-joaquin-marques-m3j5e

Query: What historical parallels exist between modern LLM function calling and earlier AI paradigms like expert systems or planning agents from the 1980s-2000s, and what forgotten lessons could improve current agent reliability?

Answer: Expert systems were among the first truly successful forms of AI software, proliferating in the 1980s and being widely regarded as the future of AI before the advent of successful artificial neural networks. These early systems operated on a simple but powerful architecture: a knowledge base containing domain-specific facts and rules, paired with an inference engine that applied 'if-then' logic to reach conclusions. The limitations were significant, however. Expert systems could not evolve or go beyond what they had learned, because the rules were built into the system. They required extensive manual knowledge engineering and struggled with maintenance as rule bases grew complex. In the 1990s and beyond, the term expert system largely dropped from the IT lexicon as the field moved toward machine learning approaches that could learn patterns from data rather than relying solely on manually crafted rules. This shift represented a fundamental change from symbolic reasoning to statistical learning. Machine learning introduced adaptive systems that could improve performance through experience, handling variability and uncertainty far better than their rule-based predecessors. However, these systems still operated primarily in reactive mode—responding to inputs without the ability to plan, reason through multi-step processes, or maintain persistent memory across interactions. Today's LLM-powered agents still face challenges around reliability, hallucination, and knowledge boundaries—echoes of the same issues that limited expert systems decades ago.

-----

Phase: [EXPLORATION]

### Source [80]: https://fortune.com/2026/03/24/ai-agents-are-getting-more-capable-but-reliability-is-lagging-narayanan-kapoor/

Query: What historical parallels exist between modern LLM function calling and earlier AI paradigms like expert systems or planning agents from the 1980s-2000s, and what forgotten lessons could improve current agent reliability?

Answer: Unreliability is a major drawback of current AI agents. It’s a point that Princeton University’s Sayash Kapoor and Arvind Narayanan, who cowrote the book AI Snakeoil and now cowrite the “AI As Normal Technology” blog, frequently make. And a few weeks ago they published a research paper, co-authored with four other computer scientists, that tries to think systematically about AI agent reliability and to benchmark leading AI models. The paper, entitled “Towards a Science of AI Agent Reliability,” notes that most AI models are benchmarked on their average accuracy on tasks, a metric that allows for wildly unreliable performance. Instead, they look at reliability across four dimensions: consistency (if asked to perform the same task in the same way, do they always perform the same?); robustness (can they function even when conditions aren’t ideal?); calibration (do they give users an accurate sense of their certainty?); and safety (when they do mess up, how catastrophic are those mistakes likely to be?). Stakeholders must verify not just what the agent concluded but how it got there, they write. It matters less in open-ended or creative tasks where diverse solution paths are desirable.

-----

</details>

<details>
<summary>How is the integration of tool calling with emerging decentralized AI networks and blockchain-based verification changing the security and auditability of autonomous agent actions?</summary>

Phase: [EXPLORATION]

### Source [81]: https://arxiv.org/html/2601.04583v1

Query: How is the integration of tool calling with emerging decentralized AI networks and blockchain-based verification changing the security and auditability of autonomous agent actions?

Answer: Crucially, these cognitive architectures become economically relevant when coupled with tools and APIs. Tool-using agents can query live systems, call external services, and execute multi-step procedures rather than merely generate text. Recent research has systematized how LLM agents learn tool usage and how tool interfaces are specified and optimized[326, 337]. Tool-learning mechanisms such as self-supervised tool use (e.g., Toolformer) and large API-connected models (e.g., Gorilla) further illustrate how models can be trained or prompted to select and parameterize tool calls at scale[267, 237]. At the same time, the security implications are now clear: function calling and tool invocation expand the attack surface, enabling new pathways for misuse and jailbreaking if tools are not [...]. Connecting an AI agent to a blockchain is not merely another tool integration. The fundamental properties of blockchain systems introduce a set of high-stakes characteristics that distinguish “agent-to-chain” interactions from typical API calls. These differences, summarized in Table1, necessitate a new class of standards, interfaces, and safety protocols. Table 1: Comparison of traditional web APIs versus blockchain transaction interfaces, highlighting why agent-to-chain tooling demands stronger safety controls[74, 319]. The risks associated with agent-blockchain integration extend beyond the immediate technical challenges to encompass broader systemic and societal concerns. Multi-agent systems introduce coordination challenges that can lead to emergent failures[191, 215]. The automation of financial transactions raises concerns about market stability and flash crashes[192, 206]. Privacy considerations are paramount when agents handle sensitive user data[194, 193]. The broader landscape of AI agents presents both opportunities and risks that must be carefully managed[200, 196]. The honesty and alignment of AI systems is a critical concern for high-stakes applications. Smart contract security remains a persistent challenge[207, 209]. The interoperability of different blockchain systems introduces.

-----

Phase: [EXPLORATION]

### Source [84]: https://blog.sei.io/research/unleashing-ai-agents-how-blockchain-enables-true-digital-autonomy/

Query: How is the integration of tool calling with emerging decentralized AI networks and blockchain-based verification changing the security and auditability of autonomous agent actions?

Answer: Blockchain removes the reliance on centralized authorities, enabling agents to verify their identity, manage resources, and interact securely. Decentralized identity and reputation systems provide cryptographically verifiable credentials, allowing agents to establish trust without human intervention. It also enables verifiable computation through mechanisms like zero-knowledge proofs, ensuring that an agent’s decisions and actions can be audited for correctness while preserving privacy, building trust in agent behavior. Interoperability allows agents to operate seamlessly across platforms and economic environments. Using cross-chain protocols, agents can transfer assets, credentials, and data across ecosystems autonomously, fostering a globally interconnected system. Blockchains enable fully autonomous AI Agents. Consumers’ ultimate user experience preferences are AI agents that can handle a wide range of tasks on their behalf, from booking holidays and finding the best value-for-money products to conducting research and creating work presentations. The most capable agents—those that are autonomous, highly interconnected, equipped with scalable compute resources, and able to preserve security and privacy—will ultimately win the trust and preference of users. AI agents need the following to achieve full autonomy: Identity and reputation. Scalable and verifiable computation. Economic independence (Seamless value transfer). Interoperability (multi-ecosystem operation). Security and privacy (data and interaction integrity). Traditional Web2 systems, which rely on centralized and permissioned infrastructure, come with challenges for enabling fully autonomous AI agents to participate effectively in economic systems. The reliance on centralized authorities such as cloud providers, banks, and identity verification services creates bottlenecks and vulnerabilities, as agents depend on human oversight for critical tasks like resource allocation and identity management. In other words, a bank, a payment gateway, or a supplier is likely to block a transaction coming from an agent sitting on the right end of the autonomy spectrum.

-----

</details>

<details>
<summary>In what ways are tool-calling frameworks influencing the development of educational AI tutors or adaptive learning platforms across different subjects like mathematics and language learning?</summary>

Phase: [EXPLORATION]

### Source [87]: https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/

Query: In what ways are tool-calling frameworks influencing the development of educational AI tutors or adaptive learning platforms across different subjects like mathematics and language learning?

Answer: Mathematical operations tools like Wolfram Alpha handle advanced math, symbolic computation, or scientific calculations. If your agent needs to solve equations or perform statistical analysis, these tools save you from reinventing the wheel. Tool calling transforms large language models from language models into capable agents. The three-pillar framework (Data Access, Computation, and Actions) gives you a mental model for building balanced, production-ready systems.

-----

Phase: [EXPLORATION]

### Source [90]: https://bse.berkeley.edu/leveraging-ai-improve-adaptive-tutoring-systems

Query: In what ways are tool-calling frameworks influencing the development of educational AI tutors or adaptive learning platforms across different subjects like mathematics and language learning?

Answer: Researchers are using AI in an open way to build adaptive tutoring systems to help teachers differentiate instruction and students learn math and other subjects. At the forefront is Associate Professor Zachary Pardos, whose team has developed a tutoring tool called Open Adaptive Tutor (OATutor) and released it in 2023. An open-source system, the tool has potential to powerfully assist research in the use of AI in learning scenarios. Adaptive typically means that the tutoring system is making instructional decisions that are tailored to assessments it’s making of the student in real-time. OATutor benefits from AI by allowing integration like defining a small assignment and then having ChatGPT give the feedback within the framework of the tutoring system. The log data would give indication of the student’s performance on the assignment and the interactions with ChatGPT, and the system works with Canvas, so it can link the OATutor assignment to the grade book in the learning management system. OATutor is gaining recognition and has been awarded grants for expansion in chemistry and mathematics courses.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ai-agents-don-t-need-complex-workflows-build-one-in-python-i.md">
<details>
<summary>ai-agents-don-t-need-complex-workflows-build-one-in-python-i</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://dev.to/aws/ai-agents-dont-need-complex-workflows-build-one-in-python-in-10-minutes-2m5d>

Building an AI agent in Python can be as easy as giving a model some tools and letting it figure out the rest.

Most agent setups start the same way: you wire up tool calls, manage retries, track state, and write the routing logic that decides what happens when. It works, but it's brittle. Every time the workflow changes, you're back in the code rewiring the sequence.

Strands is an open-source Python SDK built around a different idea.

Instead of you hardcoding the orchestration, you let the model handle it. You give it tools and a goal, and the SDK takes care of the agent loop, tool execution, and conversation state. You can go from zero to a working agent in about 10 minutes, and the same primitives that make a simple agent easy to build can be combined to give you more complex setups when you need them.

## A Model Driven Approach to AI Agents

The Strands team calls this a model-driven approach. The LLM is the orchestrator and you define the capabilities it can use.

In practice, your agent code is mostly plugging in the different desired components. Here's what a basic agent looks like:

```
from strands import Agent

agent = Agent(system_prompt="You are a helpful assistant.")
response = agent("What's the capital of France?")
print(response)
```

That's a working agent. It uses Amazon Bedrock as the model provider by default, but you can swap in any supported provider. We'll use OpenAI for the rest of this post.

## Setting Up a Python AI Agent with OpenAI

Install the SDK with the OpenAI extension:

```
pip install 'strands-agents[openai]' strands-agents-tools
```

Set your API key:

```
export OPENAI_API_KEY=your_api_key_here
```

Now create an agent that uses OpenAI:

```
import os
from strands import Agent
from strands.models.openai import OpenAIModel

model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id="gpt-4o",
)

agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant.",
)

response = agent("What's the capital of France?")
print(response)
```

Run it with `python agent.py` and you should get a response. The agent handles the API call to the OpenAI model and response parsing for you.

So far, this doesn't have any tools it can use to interact with the real world. It does however have a main agent loop handled, and is the starting point from which you will build a more capable agent.

## The Building Blocks of an AI Agent

Strands has a couple of main building blocks you should be aware of: agents, tools, models, and hooks. Understanding how they fit together is most of what you need to know.

### Models

A model is the LLM provider. Strands supports Bedrock (the default), OpenAI, Anthropic, Google Gemini, Meta Llama, Ollama for local models, and several others. You configure the model once and pass it to your agent.

```
model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id="gpt-4o",
    params={"temperature": 0.3},
)
```

You can set inference parameters using `params`. One good one to note is temperature. Use a lower temperature for factual tasks or a higher temperature for creative ones. Other supported inference parameters depend on the model.

### Giving Your Agent Tools

Tools are Python functions that extend what the agent can do beyond generating text.

Here's a custom tool to return weather data:

```
from strands import tool

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location.

    Args:
        location: City name, e.g. "Seattle"
    """
    # In a real app, this would call a weather API
    return f"Weather in {location}: Sunny, 72°F"
```

The `@tool` decorator is all you need. The docstring matters because the model uses it along with the function's type hints to decide when to call this function and what arguments to pass. Clear docstrings lead to better tool usage.

Strands also ships with a community tools package that includes common utilities:

```
from strands_tools import calculator, python_repl, http_request
```

These give your agent the ability to do math, run Python code, and make HTTP requests out of the box.

### Wiring It All Together

The agent brings everything together. You give it a model, tools, and a system prompt:

```
agent = Agent(
    model=model,
    tools=[get_weather, calculator],
    system_prompt="You are a helpful assistant that can check weather and do math.",
)
```

When you call the agent with a message, it enters an agent loop. The model reads the message, decides if it needs to use any tools, calls them if it does, reads the results, and either calls more tools or generates a final response. This loop continues until the model decides it has enough information to answer.

You don't write any of that loop logic, the SDK handles it for you.

### Hooking into the Agent Lifecycle

Hooks let you subscribe to lifecycle events in the agent loop without modifying the agent's core logic. The agent emits events at specific points during execution: before and after model calls, before and after tool calls, when messages are added, and at the start and end of each invocation. You register callbacks for the events you care about.

Here's a hook that logs every tool call:

```
from strands.hooks import BeforeToolCallEvent, AfterToolCallEvent

def log_tool_call(event: BeforeToolCallEvent):
    print(f"Calling tool: {event.tool_use['name']}")
    print(f"With input: {event.tool_use['input']}")

def log_tool_result(event: AfterToolCallEvent):
    print(f"Tool {event.tool_use['name']} completed")

agent = Agent(
    model=model,
    tools=[get_weather, calculator],
    system_prompt="You are a helpful assistant.",
)

agent.add_hook(log_tool_call, BeforeToolCallEvent)
agent.add_hook(log_tool_result, AfterToolCallEvent)
```

The available events cover the full lifecycle:

- `BeforeInvocationEvent` / `AfterInvocationEvent` for the overall request
- `BeforeModelCallEvent` / `AfterModelCallEvent` for LLM calls
- `BeforeToolCallEvent` / `AfterToolCallEvent` for tool execution
- `MessageAddedEvent` when messages are added to conversation history

Hooks are useful for logging, metrics, basic guardrails, and adding logic to your agents lifecycle. You can also cancel a tool call from a `BeforeToolCallEvent` hook by setting `event.cancel_tool` to a message, which stops the tool from executing and sends that message back to the model as an error. For example, you can check the tool name and arguments, and block it if something looks wrong.

Once you start building more complex agents, you'll find yourself wanting to bundle related hooks and tools into reusable packages. We'll get to that later in this post.

## Building a Multi-Tool Agent

Here's a more complete example. This agent has a few tools as examples to do things like look up weather, do calculations, and count letters in words. The actual tools themselves don't matter much for learning how to build an agent, as those will be unique to your specific use case. For now, we are just exploring how to wire all of the pieces together into an agent that does things:

```
import os
from strands import Agent, tool
from strands.models.openai import OpenAIModel
from strands_tools import calculator

@tool
def get_weather(location: str) -> str:
    """Get the current weather for a location.

    Args:
        location: City name, e.g. "Seattle"
    """
    return f"Weather in {location}: Sunny, 72°F"

@tool
def letter_counter(word: str, letter: str) -> int:
    """Count occurrences of a specific letter in a word.

    Args:
        word: The word to search in
        letter: The single letter to count
    """
    return word.lower().count(letter.lower())

model = OpenAIModel(
    client_args={"api_key": os.environ["OPENAI_API_KEY"]},
    model_id="gpt-4o",
)

agent = Agent(
    model=model,
    tools=[get_weather, calculator, letter_counter],
    system_prompt="You are a helpful assistant.",
)

response = agent("""I have a few questions:
1. What's the weather in Seattle?
2. What is 1547 * 382?
3. How many r's are in "strawberry"?
""")
print(response)
```

The agent will call each tool as needed, collect the results, and give you a single coherent response. You didn't have to write any routing logic or decide which tool to call for which question. The model handles that.

## How AI Agents Remember Conversations

Agents maintain conversation context automatically within a running process. Each call to the agent adds to the conversation history, so the model remembers what was said earlier:

```
agent("My name is Morgan.")
response = agent("What's my name?")
print(response)  # Will remember "Morgan"
```

This works across multiple turns without any extra code because the SDK manages the message history internally.

That said, this memory only lives as long as the agent's process lives. If you're running a script locally and it exits, the history is gone. If you're hosting an agent behind an API, the process restarts with every request so message history is not maintained.

This is because LLMs are stateless by default, and the conversation history that makes them feel stateful is just a list of messages that gets sent with every request.

For anything beyond a local script, you need to persist that history somewhere.

### Session Managers

Strands provides session managers that save and restore conversation state across invocations. The simplest option is `FileSessionManager`, which writes session data to the local filesystem:

```
from strands import Agent
from strands.session.file_session_manager import FileSessionManager

session_manager = FileSessionManager(
    session_id="my-session",
    storage_dir="./sessions",
)

agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant.",
    session_manager=session_manager,
)

# First run
agent("My name is Morgan.")

# Later, even after a restart, the agent remembers
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant.",
    session_manager=FileSessionManager(
        session_id="my-session",
        storage_dir="./sessions",
    ),
)
response = agent("What's my name?")
print(response)  # Still remembers "Morgan"
```

`FileSessionManager` stores each message as a JSON file on disk. It works well for local development. For hosted setups, you'd swap in a session manager backed by a database or a managed memory service like Amazon Bedrock AgentCore Memory. The integration pattern is the same, but you'd need to provision the infrastructure for the data store.

### Managing the Context Window

There's another problem that shows up in longer conversations. Every LLM has a context window, which is the maximum amount of tokens it can process in a single request. Your system prompt, the full conversation history, tool definitions, and the model's response all have to fit inside that window.

For short conversations this isn't an issue. But if your agent runs for dozens of turns, or if tools return large results, the conversation history can grow past what the model can handle.

Strands provides a few out of the box conversation managers to deal with this:

The sliding window manager keeps the most recent messages and drops the oldest ones when the history gets too long:

```
from strands import Agent
from strands.agent.conversation_manager.sliding_window_conversation_manager import SlidingWindowConversationManager

agent = Agent(
    model=model,
    conversation_manager=SlidingWindowConversationManager(
        window_size=40,  # keep the last 40 messages
    ),
)
```

This is simple and predictable: old messages fall off the end. The downside is that the agent loses context from earlier in the conversation. If a user said something important 50 messages ago, it's gone.

The summarizing manager takes a different approach. Instead of dropping old messages, it summarizes them and then keeps the summary:

```
from strands import Agent
from strands.agent.conversation_manager.summarizing_conversation_manager import SummarizingConversationManager

agent = Agent(
    model=model,
    conversation_manager=SummarizingConversationManager(
        summary_ratio=0.3,  # summarize the oldest 30% of messages
        preserve_recent_messages=10,  # always keep the last 10
    ),
)
```

When the context gets too large, the summarizing manager takes the context and generates a summary using the LLM. It then replaces those messages with the summary. The agent keeps the gist of what happened earlier without the full verbatim history. This costs an extra model call when summarization triggers, but it preserves more context than a simple sliding window.

Which one you pick depends on your use case. For short, focused interactions, the sliding window is fine. For longer sessions where earlier context matters, the summarizing manager is worth the extra cost.

There are also more advanced techniques you can use to manage your context window. Figuring out all the ways to manage context is called context engineering, and is an entire discipline in the AI engineering world. For simple agents, sliding window or summarization are good places to start.

## How the Agent Loop Ties It All Together

Stack these pieces together and you get a pretty capable agent without writing much code. A model handles reasoning and tool selection.

- Tools extend what the agent can do.

- Hooks give you control over the lifecycle.

- Session managers persist state across restarts.

- Conversation managers keep the context window under control.


The agent loop ties it all together: the model calls tools, reads results, handles errors by trying a different approach, and returns the final response.

This is the starting point. Once you start building more advanced agents you'll need more capabilities. That's where plugins come in.

Plugins are classes that bundle hooks and tools together into behavioral modifications you can attach to any agent. The SDK ships with a few built-in plugins that show what this looks like in practice, and you can build your own custom plugins as needed.

## Extending Your Agent with Plugins

### Steering

Steering is a plugin that evaluates the agent's output and sends corrective feedback when the response drifts from your guidelines. You give it a system prompt that defines the rules, and it uses a separate LLM call to judge each response before it reaches the user.

```
from strands import Agent
from strands.vended_plugins.steering import LLMSteeringHandler

agent = Agent(
    model=model,
    tools=[get_weather, calculator],
    plugins=[\
        LLMSteeringHandler(\
            system_prompt="Ensure all responses are professional and concise. "\
            "Reject any response that includes speculation or unverified claims."\
        ),\
    ],
)
```

Under the hood, the steering plugin hooks into the agent's lifecycle using a `BeforeToolCallEvent` hook. It intercepts tool calls, runs them through the evaluator, and returns one of three actions: proceed (let it through), guide (reject with feedback so the agent retries), or interrupt (escalate to a human). You don't write any of that logic. You just describe the rules in the system prompt for the steering handler.

This is useful for enforcing tone in customer-facing agents, preventing agents from calling tools with dangerous arguments, or evaluating if agents are following directions.

### Skills

Skills are modular instructions that agents discover and activate at runtime. They follow the [Agent Skills specification](https://skills.sh/), an open standard for packaging agent capabilities as folders containing instructions, scripts, and resources.

A skill might teach an agent how to perform a code review following your team's conventions, how to deploy to a specific environment, or how to write content in a particular style.

The agent only loads a skill's metadata (name and description) initially. When the agent decides a skill is relevant to the current task, it activates it and pulls in the full instructions. This keeps the context window clean since the agent only loads what it needs.

### Building Your Own Plugins

You can also build custom plugins. A plugin is a class that extends `Plugin` and uses `@hook` and `@tool` decorators:

```
from strands import Agent, tool
from strands.plugins import Plugin, hook
from strands.hooks import BeforeToolCallEvent, AfterToolCallEvent

class LoggingPlugin(Plugin):
    """A plugin that logs all tool calls and provides a utility tool."""

    name = "logging-plugin"

    @hook
    def log_before_tool(self, event: BeforeToolCallEvent) -> None:
        """Called before each tool execution."""
        print(f"[LOG] Calling tool: {event.tool_use['name']}")
        print(f"[LOG] Input: {event.tool_use['input']}")

    @hook
    def log_after_tool(self, event: AfterToolCallEvent) -> None:
        """Called after each tool execution."""
        print(f"[LOG] Tool completed: {event.tool_use['name']}")

    @tool
    def debug_print(self, message: str) -> str:
        """Print a debug message.

        Args:
            message: The message to print
        """
        print(f"[DEBUG] {message}")
        return f"Printed: {message}"

# Using the plugin
agent = Agent(plugins=[LoggingPlugin()])
agent("Calculate 2 + 2 and print the result")
```

When the agent initializes, it scans the plugin for `@hook` and `@tool` methods and registers them automatically. You can stack multiple plugins on the same agent, and each one manages its own hooks and state without interfering with the others.

Beyond plugins, Strands supports multi-agent patterns where agents invoke other agents as tools, MCP (Model Context Protocol) servers for connecting to external tool providers, and structured output for getting typed responses. These are all topics for another post. The point is that the same primitives (agents, tools, models, hooks) compose into more complex setups without requiring you to learn a different API.

## Install and Build Your First AI Agent

The fastest path from here:

1. Install: `pip install 'strands-agents[openai]' strands-agents-tools`
2. Set your API key: `export OPENAI_API_KEY=your_key`
3. Write a simple agent with one custom tool
4. Run it and see what happens

The [Strands documentation](https://strandsagents.com/docs/user-guide/quickstart/overview/) has more examples, including multi-agent setups, observability, and production deployment patterns. The [GitHub repo](https://github.com/strands-agents/sdk-python) has the source and community tools.

The SDK is open source and actively developed. If you've been putting off building an agent because the frameworks felt heavy, give Strands a look. The barrier to entry is low, and it provides enough composability to keep up with you as your use case gets more complex.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ai-tool-calling-from-scratch-to-production.md">
<details>
<summary>Tool Calling From Scratch to Production: The Complete Guide</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.decodingai.com/p/tool-calling-from-scratch-to-production>

# Tool Calling From Scratch to Production: The Complete Guide

### Master the fundamentals through a deep research agent to learn to properly implement, use, and debug tools in any AI system.

Paul Iusztin

Oct 28, 2025

_**Welcome to the AI Agents Foundations series**—a 9-part journey from Python developer to AI Engineer. Made by busy people. For busy people._

Everyone’s talking about AI agents. But what actually is an agent? When do we need them? How do they plan and use tools? How do we pick the correct AI tools and agentic architecture? …and most importantly, where do we even start?

To answer all these questions (and more!), We’ve started a 9-article straight-to-the-point series to build the skills and mental models to ship real AI agents in production.

We will write everything from scratch, jumping directly into the building blocks that will teach you _“how to fish”_.

**What’s ahead**:

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. **Tool Calling From Scratch** _← You are here_

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. [Multimodal Agents](https://www.decodingai.com/p/stop-converting-documents-to-text)


By the end, you’ll have a deep understanding of how to design agents that think, plan, and execute—and most importantly, how to integrate them in your AI apps without being overly reliant on any AI framework.

**Let’s get started.**

* * *

## Writing Tool Calls From Scratch

Often, we use frameworks like LangGraph or AgentSDK to implement tools, hook up to smart MCP servers and ultimately use APIs like Gemini or OpenAI to call them.

_But how do tools actually work under the hood?_ That’s a fundamental question to answer to be able to optimize agents to use tools exactly how we want. To understand how to properly define tools, how many tools to give to your agent to avoid tool confusion and what types of tools are even worth using. To answer these questions, the best approach is to **build tool calling from scratch**.

Recently, while building Nova, the research agent as one of the projects for the AI agents course I’m teaching with Towards AI, I ran into a frustrating problem. The agent could produce impressive research queries to call the Perplexity API, but it wasn’t flexible enough to gather context outside of that, such as YouTube transcripts, GitHub repositories or random sites. I needed this context to properly guide the research.

Thus, I realized it’s time to plug in specialized tools to pull these data sources. Then, based on the user input, before starting doing Perplexity queries, to specialize my context, the agent understood what GitHub repositories or what YouTube transcripts to pull.

The idea is that even the smartest LLM is ultimately just a sophisticated text generator. That’s why current chatbot applications such as ChatGPT or Gemini are limited by how you can provide them the proper context. Ultimately, most vertical AI applications solve this particular problem. They integrate with the right tools to provide you the right context, at the right time. Tools sit as the cornerstone of this transition.

**In this article**, we will first explain in more depth why LLMs need tools. Then, we will implement tool definition and calling from scratch before showing how to achieve the same result with a production API like Gemini. Finally, we will build an intuition on the most essential tool categories you need to know to build your own agents.

So… Let’s start with a better understanding of why tools are so important.

## Why Agents Need Tools

_LLMs have a fundamental limitation:_ they are trained on static datasets and cannot update their knowledge or interact with the external world on their own [[1]](https://www.projectpro.io/article/llm-limitations/1045), [[2]](https://blog.gdeltproject.org/large-language-models-llms-planetary-scale-realtime-data-current-limitations/). Their knowledge is fixed at the time of training, which means they are disconnected from real-time information and cannot perform actions beyond generating text [[3]](https://arxiv.org/html/2412.04503v1). To bridge this gap, we need strategies such as Retrieval-Augmented Generation (RAG) or other memory techniques. But all require one essential component: tools.

Now let’s see how this relates to agents.

In any agentic system, we have two core components: the agent and the environment. The agent uses its internal knowledge to take actions in the environment, interprets the output from those actions, updates its state, and then decides on the next action. Tools are the mechanism that allows the agent to “see” what’s happening in the environment or take actions within it. The LLM acts as the brain, while the tools are its “hands and senses,” allowing it to perceive and act in the world.

https://substackcdn.com/image/fetch/$s_!CLEq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4338079-cb78-4271-841b-f0fafcf8a3a8_1163x420.png Image 1: A high-level flowchart illustrating how an LLM agent interacts with external tools.

Most tools can be broadly categorized into two buckets:

1. **Accessing External Information (Read Actions):** These tools allow an agent to gather information to pass into its context window. This includes accessing real-time data through APIs (e.g., weather, news) or querying databases (e.g., PostgreSQL, Snowflake). These are often present when implementing RAG or the memory layer in general [[4]](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models), [[5]](https://www.getdynamiq.ai/post/llm-agents-explained-complete-guide-in-2025).

2. **Taking Actions (Write Actions):** These tools give the agent the ability to affect the external world. This can involve executing code, sending emails, creating calendar events, or writing to a database. These actions carry more risk and must be handled with care as their actions are often irreversible [[6]](https://mirascope.com/blog/llm-integration), [[7]](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models).


## Implementing Tool Calls From Scratch

The best way to understand how tools work is to implement them yourself. We will build a simple framework to see how a tool is defined, how an LLM discovers it, and how the entire call-and-response cycle works.

https://substackcdn.com/image/fetch/$s_!P07u!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F997f5d55-8138-4635-af6c-0e7f74fed82c_1161x419.png Image 2: Flowchart illustrating the 5-step request-execute-respond flow of calling a tool.

The high-level process of calling a tool involves five steps [[8]](https://python.langchain.com/docs/how_to/function_calling/):

1. **You:** Send the LLM your task, a prompt and a list of available tools with their definitions (schemas).

2. **LLM:** Responds with a `function_call` request, specifying the tool’s name and the arguments to use.

3. **You:** Parse this request and execute the corresponding function in your code.

4. **You:** Send the function’s output back to the LLM as a new message.

5. **LLM:** Uses the tool’s output to generate a final, user-facing response.


As seen in Image 3, actions are mapped to function calls, while the feedback from the environment is mapped to function outputs.

https://substackcdn.com/image/fetch/$s_!cv8k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F362128ff-7821-482e-b08a-8252d0faab99_1200x1200.png Image 3: Mapping agent actions to tools

This request-execute-respond flow is the foundation of tool use in AI agents.

Now, let’s implement this flow. We will define some mocked tools for our research agent use case: `google_search`, `perplexity_search`, and `scrape_url`.

1. First, we define our mock Python functions. The function signature and docstrings are important, as they provide the information the LLM will use to understand what each tool does.


```
def google_search(query: str) -> dict:
    “”“
    Tool used to perform Google web searches and return ranked results.

    Args:
        query (str): The search query.

    Returns:
        dict: A dictionary of search results.
    “”“
    return {”results”: “https://example.com/random/url”}

def perplexity_search(query: str) -> dict:
    “”“
    Tool used to perform AI-powered Perplexity searches with source citations.

    Args:
        query (str): The search query.

    Returns:
        dict: A dictionary with an AI-generated answer and sources.
    “”“
    return {”answer”: f”Mock Perplexity answer for: {query}”, “sources”: []}

def scrape_url(url: str) -> str:
    “”“
    Tool used to scrape and clean HTML content from a web URL.

    Args:
        url (str): The URL to scrape.

    Returns:
        str: The cleaned text content of the page.
    “”“
    return f”Mock scraped content from: {url}”
```

2. Next, we define a JSON schema for each tool. This schema tells the LLM the tool’s `name`, `description`, and `parameters`. This is the industry-standard format used by APIs from OpenAI, Google, and others [[9]](https://www.promptingguide.ai/applications/function_calling).


```
google_search_schema = {
    “name”: “google_search”,
    “description”: “Tool used to perform Google web searches and return ranked results.”,
    “parameters”: {
        “type”: “object”,
        “properties”: {
            “query”: {
                “type”: “string”,
                “description”: “The search query.”,
            }
        },
        “required”: [”query”],
    },
}

perplexity_search_schema = {
    “name”: “perplexity_search”,
    “description”: “Tool used to perform AI-powered Perplexity searches with source citations.”,
    “parameters”: {
        “type”: “object”,
        “properties”: {
            “query”: {
                “type”: “string”,
                “description”: “The search query.”,
            }
        },
        “required”: [”query”],
    },
}

scrape_url_schema = {
    “name”: “scrape_url”,
    “description”: “Tool used to scrape and clean HTML content from a web URL.”,
    “parameters”: {
        “type”: “object”,
        “properties”: {
            “url”: {
                “type”: “string”,
                “description”: “The URL to scrape.”,
            }
        },
        “required”: [”url”],
    },
}
```

3. We create a tool registry to map tool names to their handlers and schemas.


```
TOOLS = {
    “google_search”: {
        “handler”: google_search,
        “declaration”: google_search_schema,
    },
    “perplexity_search”: {
        “handler”: perplexity_search,
        “declaration”: perplexity_search_schema,
    },
    “scrape_url”: {
        “handler”: scrape_url,
        “declaration”: scrape_url_schema,
    },
}
TOOLS_BY_NAME = {tool_name: tool[”handler”] for tool_name, tool in TOOLS.items()}
TOOLS_SCHEMA = [tool[”declaration”] for tool in TOOLS.values()]
```

The `TOOLS_BY_NAME` mapping looks like this:

```
{’google_search’: <function google_search at 0x...>, ‘perplexity_search’: <function perplexity_search at 0x...>, ‘scrape_url’: <function scrape_url at 0x...>}
```

And here is an example schema from `TOOLS_SCHEMA`:

```
{
    “name”: “google_search”,
    “description”: “Tool used to perform Google web searches and return ranked results.”,
    “parameters”: {
        “type”: “object”,
        “properties”: {
            “query”: {
                “type”: “string”,
                “description”: “The search query.”
            }
        },
        “required”: [\
            “query”\
        ]
    }
}
```

4. Now, we create a system prompt to instruct the LLM on how to use these tools. This prompt includes usage guidelines and the schemas of all available tools.


```
TOOL_CALLING_SYSTEM_PROMPT = “”“
You are a helpful AI assistant with access to tools.

## Tool Usage Guidelines
- When you need to perform actions or retrieve information, choose the most appropriate tool.
- Choose different tools based on their descriptions.
- Provide all required parameters with accurate values.

## Tool Call Format
When you need to use a tool, output ONLY the tool call in this exact format:

<tool_call>
{{”name”: “tool_name”, “args”: {{”param1”: “value1”}}}}
</tool_call>

## Available Tools
<tool_definitions>
{tools}
</tool_definitions>
“”“
```

5. The LLM, which has been instruction-tuned for function calling, uses the `description` field in the schema to decide which tool is appropriate for a user’s query. This is why clear and distinct tool descriptions are essential. For example, `Tool used to perform Google web searches` is much better than `Tool used to find information`, as it prevents confusion with other search tools. The model then generates the function name and arguments as a structured JSON output.

6. Let’s test it. We send a user prompt along with our system prompt to the model.


```
from google import genai

client = genai.Client()

USER_PROMPT = “Use Google Search to find recent articles about AI agents.”

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.generate_content(
    model=”gemini-2.5-flash”,
    contents=messages,
)
```

The LLM correctly identifies the `google_search` tool and generates the required arguments:

```
<tool_call>
{”name”: “google_search”, “args”: {”query”: “recent articles about AI agents”}}
</tool_call>
```

7. Let’s try a more complex query that implies a sequence of actions.


```
USER_PROMPT = “Use Google Search to find the latest news on AI agents, then scrape the top result.”

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.generate_content(
    model=”gemini-2.5-flash”,
    contents=messages,
)
```

The model correctly identifies the first step and calls the appropriate tool:

```
<tool_call>
{”name”: “google_search”, “args”: {”query”: “latest news on AI agents”}}
</tool_call>
```

To move on to the scraping tool, which we expect based on the user prompt, we first have to execute the Google Search tool.

8. To do that, we create a helper function to extract the JSON string and another to handle the entire tool call process.


```
def extract_tool_call(response_text: str) -> str:
    “”“Extracts the tool call JSON from the response text.”“”
    return response_text.split(”<tool_call>”)[1].split(”</tool_call>”)[0].strip()

def call_tool(response_text: str, tools_by_name: dict):
    “”“Parses the LLM response and executes the requested tool.”“”
    tool_call_str = extract_tool_call(response_text)
    tool_call = json.loads(tool_call_str)

    tool_name = tool_call[”name”]
    tool_args = tool_call[”args”]
    tool_handler = tools_by_name[tool_name]

    return tool_handler(**tool_args)

tool_result = call_tool(response.text, tools_by_name=TOOLS_BY_NAME)
```

The `tool_result` is the output from our mock `google_search` function:

```
{”results”: “https://example.com/random/url”}
```

9. Now, we send this result back to the LLM so it can decide on the next action. Remember, our original query was to search AND scrape the top result.


```
messages.append(f”Tool result from google_search: {json.dumps(tool_result, indent=2)}”)

response = client.generate_content(
    model=”gemini-2.5-flash”,
    contents=messages,
)
```

10. The LLM recognizes that it needs to complete the second part of the task and calls the scraping tool:


```
<tool_call>
{”name”: “scrape_url”, “args”: {”url”: “https://example.com/random/url”}}
</tool_call>
```

11. We execute the scraping tool using the same helper function and send the final result back to the LLM.


```
tool_result = call_tool(response.text, tools_by_name=TOOLS_BY_NAME)

# The tool_result would be something like:
# {’content’: ‘Mock scraped content from: https://example.com/random/url’}

# Send the final tool result back to the LLM
messages.append(f”Create a summary of all the scraped articles: {json.dumps(tool_result, indent=2)}”)

response = client.generate_content(
    model=”gemini-2.5-flash”,
    contents=messages,
)
```

12. The LLM now provides a comprehensive final response synthesizing the scraped article.


```
I found the latest news on AI agents and scraped the top result...
```

You could further start optimizing this code by writing a decorator that automatically translates a function’s signature and docs to its schema to avoid manually copying anything. This is what happens when you see `@tool` decorators from frameworks such as LangGraph. The decorator would look something like this:

```
import inspect

TOOLS_SCHEMA = []
TOOLS_BY_NAME = {}

def tool(func):
    “”“Decorator that automatically registers a function as a tool.”“”
    signature = inspect.signature(func)

    # Generate schema from function
    schema = {
        “name”: func.__name__,
        “description”: func.__doc__.strip() if func.__doc__ else “”,
        “parameters”: {}
    }

    # Extract parameters from function signature
    for param_name, param in signature.parameters.items():
        param_type = param.annotation.__name__ if param.annotation != inspect.Parameter.empty else “string”
        schema[”parameters”][param_name] = {”type”: param_type}

    # Register the tool
    TOOLS_SCHEMA.append(schema)
    TOOLS_BY_NAME[func.__name__] = func

    return func
```

Now simply decorate your functions to populate your `TOOLS_SCHEMA`and` TOOLS_BY_NAME`registries:

```
@tool
def google_search(query: str) -> dict:
    “”“Searches Google for the given query.”“”
    return {”results”: “https://example.com/random/url”}

@tool
def scrape_url(url: str) -> dict:
    “”“Scrapes content from a given URL.”“”
    return {”content”: f”Mock scraped content from: {url}”}
```

But as you can see, the underlying mechanism is the same: the function’s signature and docstring are used to generate an input schema for the LLM [[11]](https://python.langchain.com/docs/concepts/tools/). It’s not fancy, but that’s the most important thing you should care about when defining tools. It sits at the core of making sure the LLM doesn’t confuse tools with each other and knows which tool to pick when.

You can intuitively see it as the _“system prompt”_ of the tool.

This manual process reveals the core mechanics of tool calling. However, we want to avoid manually keeping track of function schemas or complex tool calling system prompts. Thus, for production systems, modern APIs offer a much simpler and more robust approach.

## Implementing Production-Level Tool Calls

Modern LLM APIs like Google’s Gemini allow you to declare tools directly in the API call. This is more efficient, modern and reliable, as the only thing you should care about is defining well-documented functions.

Also, because you don’t have to define the schemas or write the tool calling system prompt yourself, the provider always takes care of optimizing them for every specific model. If you want to do it yourself, for example, with open-source models, it can quickly become a big burden.

Let’s see how to achieve the same result using Gemini’s native tool-calling capabilities.

1. The `google-genai` Python SDK can automatically generate the required schema from a Python function’s signature, type hints, and docstring. We can pass our functions directly to the `GenerateContentConfig` object.


```
from google.genai import types

config = types.GenerateContentConfig(
    tools=[google_search, perplexity_search, scrape_url]
)
```

This single step replaces all the manual schema definition and prompt engineering we did before.

2. With the configuration defined, our prompt becomes much simpler. We no longer need to provide tool-usage guidelines or schemas.


```
USER_PROMPT = “Use Google Search to find recent articles about AI agents.”

response = client.generate_content(
    model=”gemini-2.5-flash”,
    contents=USER_PROMPT,
    generation_config=config,
)
```

3. The Gemini client automatically parses the output. The `response.candidates[0].content.parts[0]` contains a `function_call` object with the tool name and arguments.


```
function_call = response.candidates[0].content.parts[0].function_call
```

This object contains everything we need:

```
name: “google_search”
args: {”query”: “recent articles about AI agents”}
```

4. We can then create a simplified `call_tool` function to execute the call.


```
def call_tool(function_call) -> any:
    tool_name = function_call.name
    tool_args = {key: value for key, value in function_call.args.items()}

    tool_handler = TOOLS_BY_NAME[tool_name]

    return tool_handler(**tool_args)

tool_result = call_tool(function_call)
```

The output is the same as our manual implementation. By leveraging the native SDK, we reduced dozens of lines of code to just a few, creating a more robust and maintainable system. Other popular APIs from OpenAI and Anthropic follow a similar logic, making these concepts easily transferable [[10]](https://platform.openai.com/docs/guides/function-calling).

In production, your agents often don’t call one or two tools, but 10, 20 or up to hundreds, depending on the use case. That’s why you need LLMOps tools, such as Opik, where you can easily monitor all the tool calls made by your agent. This includes tracking latency, token usage, cost, the model used to trigger the tool, and the inputs and outputs for each call. This visibility is essential for debugging and optimization.

In the video below, you can see how Opik helps us easily monitor a trace with over 100 steps using our full-fledged research agent, Nova.

💡 **Tip:** LLMOps platforms, such as Opik, can also help you A/B test different configurations of your AI app by running and comparing multiple experiments. This allows you to find the best model (e.g., GPT-4 vs. Claude vs. Gemini), hyperparameters or prompts for your use case while balancing accuracy, speed, and cost.

As the cherry on top, using Opik, you can even use their **[Agent Optimization](https://www.comet.com/docs/opik/agent_optimization/overview?utm_source=newsletter&utm_medium=partner&utm_campaign=paul)** feature to automatically refine your prompts or tool schemas to maximize your business metrics. For people who come from DS/ML/DL, this is similar to hyperoptimization tuning using tools such as Optuna, but for your prompts instead of hyperparameters.

## The Popular Tools You Need to Know

Now that you understand how tools work, what kinds of tools are most common in production agents? They generally fall into two categories.

#### 1) Tools that Access External Information (Read Actions):

- **Knowledge & Memory Access:** These tools are the foundation of Retrieval-Augmented Generation (RAG). They query vector databases, document stores, or graph databases to fetch relevant context for the agent [[14]](https://www.weka.io/learn/guide/ai-ml/retrieval-augmented-generation/), [[15]](https://www.leewayhertz.com/advanced-rag/). We will explore memory in more depth in future articles of this series.

- **Web Search & Browsing:** Essential for chatbots and research agents, these tools connect to search APIs like Google, Bing, or Perplexity to access up-to-date information from the internet [[16]](https://www.business-standard.com/technology/tech-news/microsoft-brings-copilot-ai-powered-web-search-mode-on-bing-how-it-works-125022500477_1.html), [[17]](https://gaper.io/perplexity-ai-vs-google-gemini-vs-chatgpt/). Similar to our mocked examples.

- **Database Queries:** Text-to-SQL tools translate natural language questions into SQL or NoSQL queries to retrieve data from structured databases [[18]](https://arxiv.org/html/2507.08034v1).

- **Knowledge Graph Queries:** Tools like GraphRAG access knowledge graphs to uncover relationships between entities, which helps the agent better understand a query and refine its context.

- **File System Reads:** These tools allow an agent to read local files and list directories, giving it access to its immediate environment. These are often used in coding agents like Claude Code to retrieve the right files using `grep` commands.


#### 2) Tools that Take Actions (Write Actions):

- **Code Execution:** A Python or JavaScript interpreter lets an agent write and run code in a sandboxed environment. This is invaluable for calculations, data manipulation, and visualization. However, it introduces significant security risks like arbitrary code execution and resource exhaustion, requiring robust sandboxing strategies like using Docker containers or gVisor [[19]](https://dida.do/blog/setting-up-a-secure-python-sandbox-for-llm-agents), [[20]](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution).

- **External API Actions:** Common in enterprise AI, these tools interact with external services to send emails, schedule meetings, or create tasks in project management systems [[21]](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models).

- **Database Writes:** These tools allow an agent to insert, update, or delete records in a database.

- **File System Writes:** Used in productivity apps, these tools can create, modify, or delete files on a local system.


> ⚠️ Always think twice before implementing any write actions, as these are often irreversible. For example, while I was running Claude Code over my Obsidian Second Brain it overwrote some of my beloved notes without having a way to access them back.

## Conclusion

Tool calling is at the core of what makes an AI agent useful. Understanding how to build, monitor, and debug tool interactions is one of the most important skills for an AI Engineer. By giving an LLM the ability to interact with the outside world, you transform it from a passive text generator into an active problem-solver.

**Interestingly, tools are not just for agents.** They are a fundamental pattern that can also power structured workflows. In the orchestrator-worker pattern, you can leverage the current tool infrastructure provided by all the AI frameworks or MCP servers to generate tool calls that can be executed in parallel later on in your code as you see fit. Ultimately, you should not be limited by labels. Your imagination is the only constraint.

_Remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer._

**Here’s our roadmap:**

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. **Tool Calling From Scratch** _← You just finished this one._

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning) ← _Move to this one_

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. [Multimodal Data](https://www.decodingai.com/p/stop-converting-documents-to-text)


See you next week.

Paul Iusztin

* * *

## References

01. (n.d.). LLM Limitations You Need to Know. _ProjectPro_. [https://www.projectpro.io/article/llm-limitations/1045](https://www.projectpro.io/article/llm-limitations/1045)

02. (n.d.). Large Language Models (LLMs), Planetary-Scale Realtime Data & Current Limitations. _The GDELT Project_. [https://blog.gdeltproject.org/large-language-models-llms-planetary-scale-realtime-data-current-limitations/](https://blog.gdeltproject.org/large-language-models-llms-planetary-scale-realtime-data-current-limitations/)

03. (n.d.). Efficient Tool Use with Chain-of-Abstraction Reasoning. _arXiv_. [https://arxiv.org/html/2412.04503v1](https://arxiv.org/html/2412.04503v1)

04. (n.d.). Guide to Integrating Tools and APIs with Language Models. _Mercity.ai_. [https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models)

05. (n.d.). LLM Agents Explained: A Complete Guide in 2025. _DynamiQ_. [https://www.getdynamiq.ai/post/llm-agents-explained-complete-guide-in-2025](https://www.getdynamiq.ai/post/llm-agents-explained-complete-guide-in-2025)

06. (n.d.). LLM Integration: A Guide to Connecting LLMs with External Resources & APIs. _Mirascope_. [https://mirascope.com/blog/llm-integration](https://mirascope.com/blog/llm-integration)

07. (n.d.). Guide to Integrating Tools and APIs with Language Models. _Mercity.ai_. [https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models)

08. (n.d.). How-to: Function calling. _LangChain_. [https://python.langchain.com/docs/how\_to/function\_calling/](https://python.langchain.com/docs/how_to/function_calling/)

09. (n.d.). Function Calling. _Prompting Guide_. [https://www.promptingguide.ai/applications/function\_calling](https://www.promptingguide.ai/applications/function_calling)

10. (n.d.). Function calling. _OpenAI_. [https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)

11. (n.d.). Tools. _LangChain_. [https://python.langchain.com/docs/concepts/tools/](https://python.langchain.com/docs/concepts/tools/)

12. (n.d.). Enforce and validate LLM output with Pydantic. _Xebia_. [https://xebia.com/blog/enforce-and-validate-llm-output-with-pydantic/](https://xebia.com/blog/enforce-and-validate-llm-output-with-pydantic/)

13. Cemri, F., et al. (2025). A Comprehensive Empirical Study of Failure Analysis for Multi-Agent LLM Systems. _arXiv_. [https://arxiv.org/pdf/2503.13657](https://arxiv.org/pdf/2503.13657)

14. (n.d.). Retrieval Augmented Generation: Everything You Need to Know About RAG in AI. _Weka_. [https://www.weka.io/learn/guide/ai-ml/retrieval-augmented-generation/](https://www.weka.io/learn/guide/ai-ml/retrieval-augmented-generation/)

15. (n.d.). Advanced RAG: The Next Generation of RAG an LLM Application. _LeewayHertz_. [https://www.leewayhertz.com/advanced-rag/](https://www.leewayhertz.com/advanced-rag/)

16. (n.d.). Microsoft brings Copilot AI-powered ‘web search mode’ on Bing: How it works. _Business Standard_. [https://www.business-standard.com/technology/tech-news/microsoft-brings-copilot-ai-powered-web-search-mode-on-bing-how-it-works-125022500477\_1.html](https://www.business-standard.com/technology/tech-news/microsoft-brings-copilot-ai-powered-web-search-mode-on-bing-how-it-works-125022500477_1.html)

17. (n.d.). Perplexity AI vs. Google Gemini vs. ChatGPT. _Gaper_. [https://gaper.io/perplexity-ai-vs-google-gemini-vs-chatgpt/](https://gaper.io/perplexity-ai-vs-google-gemini-vs-chatgpt/)

18. (n.d.). A developer’s guide to building scalable AI: Workflows vs agents. _arXiv_. [https://arxiv.org/html/2507.08034v1](https://arxiv.org/html/2507.08034v1)

19. (n.d.). Setting up a secure Python sandbox for LLM agents. _Dida.do_. [https://dida.do/blog/setting-up-a-secure-python-sandbox-for-llm-agents](https://dida.do/blog/setting-up-a-secure-python-sandbox-for-llm-agents)

20. (n.d.). Secure Code Execution. _Hugging Face_. [https://huggingface.co/docs/smolagents/en/tutorials/secure\_code\_execution](https://huggingface.co/docs/smolagents/en/tutorials/secure_code_execution)

21. (n.d.). Guide to Integrating Tools and APIs with Language Models. _Mercity.ai_. [https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models](https://www.mercity.ai/blog-post/guide-to-integrating-tools-and-apis-with-language-models)


* * *

## Images

If not otherwise stated, all images are created by the author.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="function-calling-guide-google-deepmind-gemini-2-0-flash.md">
<details>
<summary>Function Calling Guide: Google DeepMind Gemini 2.0 Flash</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.philschmid.de/gemini-function-calling>

# Function Calling Guide: Google DeepMind Gemini 2.0 Flash

Function calling is the capability to connect LLMs to external tools and to interact with your code and APIs in a structured way. Instead of generating text responses, LLMs understand when to call specific functions and provide the necessary parameters to execute real-world actions.

Throughout this guide, we'll look at a practical weather-based assistant access to a weather API. Yes, not very creative, but there is a free API we can use and it should be enough to demonstrate the concept understand how you can use function calling to build a more complex assistant.

## How does function calling work?

Function calling may imply that the LLM is directly performing some action. This is not the case! When a user prompts an LLM with function calling, the model analyzes the input and determines if and which function would be the most appropriate for the task (can be a single function or multiple functions). Instead of providing a text response, the model generates a structured JSON object that specifies which function to call and the necessary parameters.

https://www.philschmid.de/static/blog/gemini-function-calling/function-intro.png

In practice function calling not only describe the process of generating structured output, but also the process of calling a function and how to handle the output. As you don't want to return the raw output of the function to your user, you want the LLM to generate an appropriate response, based on the conversation history.

https://www.philschmid.de/static/blog/gemini-function-calling/function-calling.png

Practical Function Calling follows these steps:

1.  Your application sends a prompt to the LLM along with function definitions
2.  The LLM analyzes the prompt and decides whether to respond directly or use defined functions
3.  If using functions, the LLM generates structured arguments for the function call
4.  Your application receives the function call details and executes the actual function
5.  The function results are sent back to the LLM
6.  The LLM provides a final response incorporating the function results

This cycle can continue as needed, allowing for complex multi-step interactions between the application and the LLM. It is also possible that the LLM decides that it needs to call multiple functions after each other or in parallel before returning a final response to the user.

## When to Use Function Calling?

Function calling has emerged as one of the popular methods for building AI agents. It can help build human-AI interfaces that access and query real-time information from external sources like APIs, databases, and knowledge bases while providing a natural language interface (text or audio) to users.

Function calling enables automation tasks like scheduling appointments, creating invoices, or sending reminders. An example usecase could be a customer service assistant might use function calling to seamlessly handle tasks like checking order status, processing returns, and updating customer information – all while maintaining a natural conversation flow with the user.

You now longer need to build Applications which required complex forms or multiple steps to collect information from the user. Instead, you can build a natural language interface that allows the user to interact with the application in a conversational way. Or have no user interface at all and let the LLM interact with the world on your behalf.

## Function Calling with Google Gemini 2.0 Flash

Google Gemini 2.0 Flash supports function calling through multiple interfaces, [OpenAPI compatible JSON Schema](https://spec.openapis.org/oas/v3.0.3#schema) and Python functions defintions with docstrings. If you are using JavaScript/Typescript you currently have to use the JSON Schema interface. The Python SDK `google-genai` can automatically generate the JSON Schema from the Python function definitions and docstrings. We are going to take a look at both interfaces.

_Note: Gemini 2.0 Flash currently doesn't support `anyOf` type in the JSON Schema._

Lets start with the JSON Schema interface, but before that lets install the `google-genai` library and make sure we have a Gemini API key. If you don't have one yet you can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

```
%pip install "google-genai>=1.0.0" geopy requests
```

Once you have the SDK and API key, you can create a client and define the model you are going to use the new Gemini 2.0 Flash model, which is available via free tier with 1,500 request per day (at 2025-02-06).

```
import os
from google import genai

# create client
api_key = os.getenv("GEMINI_API_KEY","xxx")
client = genai.Client(api_key=api_key)

# Define the model you are going to use
model_id =  "gemini-2.0-flash"
```

Before we begin, lets quickly test if we have access to the model and can generate some text.

```
res = client.models.generate_content(
    model=model_id,
    contents=["Tell me 1 good fact about Nuremberg."]
)
print(res.text)
# Nuremberg is home to the oldest Christmas market in Germany, the Christkindlesmarkt, which dates back to the mid-16th century.

```

### Function Calling with JSON Schema

For using Function Calling with JSON Schema we need to define our functions as JSON Schema. Let's create a simple weather function as an example. The main parts of the JSON Schema are:

- `name`: name of the function, this need to match the name of your function in your code
- `description`: description of what the function does. This is important as this information will be used by the LLM to identify when to use the function
- `parameters`: JSON schema object of type definition for the input arguments of your function. Each parameter has a type, e.g. `string` and a `description` which are used by the LLM what to add here.
- `required`: What `parameters` are required if not all required the LLM might not provide an argument when it thinks its not needed.

```
weather_function = {
    "name": "get_weather_forecast",
    "description": "Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state, e.g., San Francisco, CA"
            },
            "date": {
                "type": "string",
                "description": "the forecasting date for when to get the weather format (yyyy-mm-dd)"
            }
        },
        "required": ["location","date"]
    }
}
```

We can now use this function definition and add it to our LLM call. The LLM will then decide on its own if it should "call" the function or return a normal text response. Lets test this. Function declarations are defined in the `config` object. We use the Pydantic `GenerateContentConfig` data structure to define the config.

```
from google.genai.types import GenerateContentConfig

# Generation Config
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04.", # to give the LLM context on the current date.
    tools=[{"function_declarations": [weather_function]}], # define the functions that the LLM can use
)
```

First lets try without our tool using "Whats the weather in Berlin this today?" prompt.

```
response = client.models.generate_content(
    model=model_id,
    contents='Whats the weather in Berlin this today?'
)
print(response.text)
# I can't give you a real-time weather update for Berlin. To get the most accurate and current weather information, I recommend checking a reliable weather source like:

# *   **A weather app:** (e.g., WeatherBug, AccuWeather, The Weather Channel)
# *   **A weather website:** (e.g., Google Weather, [weather.com](http://weather.com))
# *   **A local news source:** (e.g., a Berlin news website or TV station)

# These sources will provide you with up-to-the-minute details on temperature, wind, precipitation, and more.
```

As expected the output is not helpful, as the LLM does not know how to answer the question. Now lets try with our function.

_Note: When the LLM decides to use a tool the `.text` attribute might be null as the function call is returned in the `function_call` attribute of each candidate._

```
response = client.models.generate_content(
    model=model_id,
    config=config,
    contents='Whats the weather in Berlin today?'
)

# iterate over eacht return part and check if it is a function call or a normal response
for part in response.candidates[0].content.parts:
    print(part.function_call)
# id=None args={'date': '2025-03-04', 'location': 'Berlin, DE'} name='get_weather_forecast'
```

Great, Gemini correctly identified that it needs to call our function and generated the structured response including the function name and arguments. Now, lets put this into a "agentic" method that will call the Gemini then check if the response is a function call and if so call the function with the arguments and finally generate a final response.

_Note: The code below uses the available `types` data structured from the `google-genai` library to create the conversation history._

```
from google.genai import types
from geopy.geocoders import Nominatim
import requests

# Simple function to get the weather forecast for a given location and date
geolocator = Nominatim(user_agent="weather-app")
def get_weather_forecast(location, date):
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return {time: temp for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

# Function dictionary to map the function name to the function
functions = {
    "get_weather_forecast": get_weather_forecast
}

# helper function to call the function
def call_function(function_name, **kwargs):
    return functions[function_name](**kwargs)

# agentic loop to handle the function call
def function_call_loop(prompt):
    # create the conversation
    contents = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    # initial request
    response = client.models.generate_content(
        model=model_id,
        config=config,
        contents=contents
    )
    for part in response.candidates[0].content.parts:
        # add response to the conversation
        contents.append(types.Content(role="model", parts=[part]))
        # check if the response is a function call
        if part.function_call:
            print("Tool call detected")
            function_call = part.function_call
            # Call the tool with arguments
            print(f"Calling tool: {function_call.name} with args: {function_call.args}")
            tool_result = call_function(function_call.name, **function_call.args)
            # Build the response parts using the function result.
            function_response_part = types.Part.from_function_response(
                name=function_call.name,
                response={"result": tool_result},
            )
            contents.append(types.Content(role="user", parts=[function_response_part]))
            # Send follow-up with tool results, but remove the tools from the config
            print(f"Calling LLM with tool results")
            func_gen_response = client.models.generate_content(
                model=model_id, config=config, contents=contents
            )
            # Add the reponse to the conversation
            contents.append(types.Content(role="model", parts=[func_gen_response]))
    # return the final response
    return contents[-1].parts[0].text.strip()


function_call_loop("Whats the weather in Berlin today?")

# Tool call detected
# Calling tool: get_weather_forecast with args: {'date': '2025-03-04', 'location': 'Berlin, DE'}
# Calling LLM with tool results
# 'OK. Today in Berlin, the temperature will be between 1.7 and 12.2 degrees Celsius.'
```

Awesome! We successfully called our function and generated a final response using the function result.

### Function Calling using Python functions

The Python SDK `google-genai` can automatically generate the JSON Schema from the Python function definitions and docstrings.

```
from geopy.geocoders import Nominatim
import requests

geolocator = Nominatim(user_agent="weather-app")

def get_weather_forecast(location: str, date: str) -> str:
    """
    Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour."

    Args:
        location (str): The city and state, e.g., San Francisco, CA
        date (str): The forecasting date for when to get the weather format (yyyy-mm-dd)
    Returns:
        Dict[str, float]: A dictionary with the time as key and the temperature as value
    """
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return {time: temp for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}
```

Similar to the JSON Schema example we add our function to the generation config and we disable the automatic function calling for now, more on that later.

```
from google.genai.types import GenerateContentConfig

# Generation Config
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant that can help with weather related questions. Today is 2025-03-04.", # to give the LLM context on the current date.
    tools=[get_weather_forecast], # define the functions that the LLM can use
    automatic_function_calling={"disable": True} # Disable for now.
)
```

We can now generate a response.

```
r = client.models.generate_content(
    model=model_id,
    config=config,
    contents='Whats the weather in Berlin today?'
)
# iterate over eacht return part and check if it is a function call or a normal response
for part in r.candidates[0].content.parts:
    print(part.function_call)

# id=None args={'location': 'Berlin, Germany', 'date': '2025-03-04'} name='get_weather_forecast'
```

Great! Similar to our JSON Schema example Gemini correctly identified that it needs to call our function. The next step would be to implement the same logic to identify the function to call and handle the output, but the Python SDK supports this out of the box.

If we enable the `automatic_function_calling` the SDK will automatically call the function, and sends another request to Gemini with the function result. We can remove the `automatic_function_calling` as the default behavior when Python functions are used as tools is to automatically call the function.

```
from google.genai.types import GenerateContentConfig

# Generation Config
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04.", # to give the LLM context on the current date.
    tools=[get_weather_forecast], # define the functions that the LLM can use
    # removed the automatic_function_calling as the default with callable functions is to call the function
)

r = client.models.generate_content(
    model=model_id,
    config=config,
    contents='Whats the weather in Berlin today?'
)

print(r.text)
# OK. Today in Berlin, the temperature will be between 1.7 and 12.2 degrees Celsius.
```

Great. Now, lets try an example which might be closer to a real usecase, where we provide more context to our Assistant about the user to have a more natural conversation.

```
from google.genai.types import GenerateContentConfig

# Generation Config
config = GenerateContentConfig(
    system_instruction="You are a helpful assistant that use tools to access and retrieve information from a weather API.",
    tools=[get_weather_forecast], # define the functions that the LLM can use
    # removed the automatic_function_calling as the default with callable functions is to call the function
)

# Prompt includes more context about the user and the current date
prompt = f"""
Today is 2025-03-04. You are chatting with Philipp, you have access to more information about him.

User Context:
- name: Philipp
- location: Nuremberg

User: Can i wear a T-shirt later today?"""

r = client.models.generate_content(
    model=model_id,
    config=config,
    contents=prompt
)

print(r.text)
# The temperature in Nuremberg will range from 0.6 degrees Celsius to 13.2 degrees Celsius today. I would recommend bringing a jacket.
```

## Advanced: Function Calling with LangChain

[LangChain](https://python.langchain.com/docs/introduction/) is a composable framework that simplifies the development of LLM-powered application. LangChain supports Google Gemini 2.0 Flash and the function calling capabilities. [LangGraph](https://langchain-ai.github.io/langgraph/) is an orchestration framework for controllable agentic workflows, and many companies use LangChain and LangGraph together to build AI Agents.

```
%pip install langchain langchain-google-genai
```

To use Gemini with LangChain we need to create a `ChatGoogleGenerativeAI` class, that implements the `BaseChatModel` interface, which is responsible for the LLM calls and supporting function calling.

```
import os
from langchain_google_genai import ChatGoogleGenerativeAI


# Get API key and define model id
api_key = os.getenv("GEMINI_API_KEY","xxx")
model_id =  "gemini-2.0-flash"

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model=model_id,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=api_key,
)

# lets try it
res = llm.invoke("What is the weather in Berlin today?")
print(res.content)
# I do not have access to real-time information, including live weather updates. To find out the weather in Berlin today, I recommend checking a reliable weather app or website such as:

# *   **Google Weather:** Just search "weather in Berlin" on Google.
# *   **AccuWeather:** [https://www.accuweather.com/](https://www.accuweather.com/)
# *   **The Weather Channel:** [https://weather.com/](https://weather.com/)
# *   **Local German weather services:** such as Deutscher Wetterdienst (DWD)

# These sources will provide you with the most up-to-date and accurate weather information for Berlin.
```

Great! This looks similar to our initial call without tools enabled. Now lets try to add the function calling capabilities. Similar to the [SDK LangChain supports automatic python function](https://python.langchain.com/docs/concepts/tool_calling/) to tool conversion. If you want to use a function as tool you can add a `@tool` decorator to the function.

_Note: We copy the code from out `get_weather_forecast` function from the Python SDK example._

```
from geopy.geocoders import Nominatim
import requests
from langchain.tools import tool

geolocator = Nominatim(user_agent="weather-app")

@tool
def get_weather_forecast(location: str, date: str) -> str:
    """Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour."

    Args:
        location (str): The city and state, e.g., San Francisco, CA
        date (str): The forecasting date for when to get the weather format (yyyy-mm-dd)
    Returns:
        Dict[str, float]: A dictionary with the time as key and the temperature as value
    """
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return {time: temp for time, temp in zip(data["hourly"]["time"], data["hourly"]["temperature_2m"])}
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}
```

After we have our tool defined we can `bind` it to the LLM.

```
llm_with_tools = llm.bind_tools([get_weather_forecast])
```

Now, lets try it out.

```
messages = [\
    (\
        "system",\
        "You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04.",\
    ),\
    ("human", "What is the weather in Berlin today?"),\
]

# Call the LLM with the messages and tools
res = llm_with_tools.invoke(messages)

# Check if the LLM returned a function call
if res.tool_calls:
    print(res.tool_calls)

# [{'name': 'get_weather_forecast', 'args': {'date': '2025-03-04', 'location': 'Berlin, DE'}, 'id': 'c0043a1b-4430-4f7a-a0d6-35bd4ffc6501', 'type': 'tool_call'}]
```

Great! It worked. Now, we would need to call our function with the arguments again and add the result to the conversation. Similar to the Python SDK example Langchain supports automatic function calling, through the `create_tool_calling_agent` and `AgentExecutor`.

- `create_tool_calling_agent`: Creates an agent that can:
  - Understand when to use available tools based on user input
  - Generate structured arguments for tool calls
  - Process tool outputs to create natural responses
- `AgentExecutor`: Handles the execution flow by:
  - Managing the conversation between user and agent
  - Automatically calling tools when the agent requests them
  - Handling any errors during tool execution
  - Maintaining conversation context across multiple interactions

```
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Initialize the prompt template
prompt = ChatPromptTemplate.from_messages([\
    ("system", "You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04."),\
    ("human", "{input}"),\
    MessagesPlaceholder(variable_name="agent_scratchpad"),\
\
])

# Create the agent and executor with out llm, tools and prompt
agent = create_tool_calling_agent(llm_with_tools, [get_weather_forecast],prompt)
agent_executor = AgentExecutor(agent=agent, tools=[get_weather_forecast], verbose=True)

# Run our query
res = agent_executor.invoke({"input": "What is the weather in Berlin today?"})
print(res["output"])

# Entering new AgentExecutor chain...
# Invoking: `get_weather_forecast` with `{'date': '2025-03-04', 'location': 'Berlin, DE'}`
# {'2025-03-04T00:00': 3.5, '2025-03-04T01:00': 3.4, '2025-03-04T02:00': 3.2, '2025-03-04T03:00': 2.4, '2025-03-04T04:00': 2.4, '2025-03-04T05:00': 2.1, '2025-03-04T06:00': 1.7, '2025-03-04T07:00': 1.9, '2025-03-04T08:00': 3.3, '2025-03-04T09:00': 5.2, '2025-03-04T10:00': 6.9, '2025-03-04T11:00': 8.5, '2025-03-04T12:00': 10.5, '2025-03-04T13:00': 11.4, '2025-03-04T14:00': 11.8, '2025-03-04T15:00': 12.2, '2025-03-04T16:00': 11.6, '2025-03-04T17:00': 10.6, '2025-03-04T18:00': 9.6, '2025-03-04T19:00': 8.6, '2025-03-04T20:00': 7.8, '2025-03-04T21:00': 6.9, '2025-03-04T22:00': 6.3, '2025-03-04T23:00': 5.8}
# [1m> Finished chain.\
# OK. Today in Berlin, the temperature will be between 1.7 and 12.2 degrees Celsius.\
```\
\
Awesome! It worked.\
\
## Advanced: Function Calling with OpenAI Compatible API\
\
Google Gemini has an [OpenAI compatible API](https://ai.google.dev/gemini-api/docs/openai), which allows us to use Gemini models with the OpenAI API and SDKs. The API supports function calling out of the box, meaning we can use the OpenAI features to call our function.\
\
```\
%pip install openai\
```\
\
```\
from openai import OpenAI\
\
# Get API key and define model id\
api_key = os.getenv("GEMINI_API_KEY","xxx")\
model_id =  "gemini-2.0-flash"\
\
client = OpenAI(\
    api_key=api_key,\
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"\
)\
```\
\
Lets try it out.\
\
```\
response = client.chat.completions.create(\
  model=model_id,\
  messages=[{"role": "user", "content": "What is the weather in Berlin today?"}],\
)\
\
print(response.choices[0].message.content)\
# I do not have real-time access to live weather data. To find out the weather in Berlin today, I recommend checking a reliable weather source such as:\
\
# *   **A weather app:** (e.g., WeatherBug, AccuWeather, The Weather Channel)\
# *   **A weather website:** (e.g., Google Weather, a local news site)\
\
# These sources will give you the most up-to-date and accurate information.\
```\
\
Great! Now lets our JSON Schema example.\
\
```\
weather_function =   {\
    "type": "function",\
    "function": {\
    "name": "get_weather_forecast",\
    "description": "Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour.",\
    "parameters": {\
        "type": "object",\
        "properties": {\
            "location": {\
                "type": "string",\
                "description": "The city and state, e.g., San Francisco, CA"\
            },\
            "date": {\
                "type": "string",\
                "description": "the forecasting date for when to get the weather format (yyyy-mm-dd)"\
            }\
        },\
        "required": ["location","date"]\
    }\
}}\
\
response = client.chat.completions.create(\
  model=model_id,\
  messages=[\
      {"role": "system", "content": "You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04."},\
      {"role": "user", "content": "What is the weather in Berlin today?"}],\
  tools=[weather_function],\
  tool_choice="auto"\
)\
\
if response.choices[0].message.tool_calls:\
    print(response.choices[0].message.tool_calls[0].function)\
# Function(arguments='{"date":"2025-03-04","location":"Berlin, DE"}', name='get_weather_forecast')\
```\
\
Awesome! We successfully called our function and generated the structured response. If you are using the OpenAI SDK you can now easily test Gemini function calling.\
\
## Conclusion\
\
Function calling with Gemini 2.0 Flash provides a powerful way to build AI applications that can interact with external tools and APIs in a structured way. We explored three different approaches to implement function calling:\
\
1. Using JSON Schema - A flexible approach that works across programming languages\
2. Using Python Functions - A simpler approach with automatic schema generation when working in Python\
3. Using the OpenAI-compatible API - Allowing you to leverage existing OpenAI-based code\
\
Each approach has its strengths, with the Python SDK offering the most streamlined experience for Python developers, while the JSON Schema and OpenAI-compatible approaches provide more flexibility for other languages and existing codebases.\
\
Function calling enables us to build powerful AI assistants that can access real-time data, perform actions, handle complex interactions, and provide natural language interfaces to APIs and tools, making it an increasingly important capability for practical AI applications that interact with the real world.\

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="function-calling-structured-tool-use-for-large-language-mode.md">
<details>
<summary>Function Calling: Structured Tool Use for Large Language Models</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools>

# Function Calling: Structured Tool Use for Large Language Models

Michael BrenndoerferPublished: February 2, 2026•February 2, 2026•58 min read

[Machine Learning](https://mbrenndoerfer.com/writing/categories/machine-learning) [Language AI Handbook](https://mbrenndoerfer.com/writing/categories/language-ai-handbook)

Learn how function calling enables LLMs to invoke external tools and APIs through structured JSON schemas, bridging natural language and executable code.

## [Link to Function Calling](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#function-calling) Function CallingLink Copied

Large language models excel at reasoning, writing, and analysis, yet they remain confined to the text they were trained on. They cannot check the weather, calculate precise mathematical expressions, query databases, or interact with external APIs. [Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) bridges this gap by enabling models to express _intent_ to use [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools) in a structured, machine-readable format. Rather than simply describing what a calculator might do, the model outputs a precise JSON object specifying which function to invoke and with what arguments. This [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) transforms the model from a passive text generator into an active agent that can retrieve information, perform computations, and affect external systems.

The shift from natural language tool descriptions to structured function calling represents an important architectural decision. Early approaches to tool use relied on [in-context learning](https://mbrenndoerfer.com/writing/in-context-learning-llm-examples), where you provided examples of tool usage within the prompt yourself. While effective for simple cases, this approach consumed valuable [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp) space and suffered from inconsistency as the complexity of available tools increased. Native function calling capabilities, by contrast, bake the understanding of tool schemas directly into the model's weights through specialized fine-tuning. This creates a more reliable, scalable interface, where the model learns to treat tool schemas as first-class citizens in its output space, much like it learns grammar or factual associations.

As we discussed in [Tool Use Motivation](https://mbrenndoerfer.com/writing/tool-use-motivation-llm-limitations), the shift from in-context tool demonstrations to native [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) capabilities represents a significant evolution in how language models interface with the world. In this chapter, we examine the mechanics of function calling: how you define tool schemas, how models generate structured calls, how execution results feed back into the generation process, and how to fine-tune models for robust tool-use capabilities.

Function Calling vs. Tool Use

The terms "function calling" and "tool use" are often used interchangeably, but they carry slightly different connotations. Function calling emphasizes the mechanism: the model emits structured calls with named parameters. Tool use is the broader concept: the model employs external capabilities to answer queries. Every function call is a form of tool use, but tool use includes other patterns like web search, code execution, and memory retrieval that may not follow a strict function-call schema.

Understanding why [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) works requires thinking about the information-theoretic problem it solves. A language model generating free text must simultaneously decide what information to communicate and how to format it for the recipient. When the recipient is a human, natural language is ideal. When the recipient is a software system, natural language is ambiguous and brittle. Function calling resolves this by separating the decision of what to do (natural language understanding) from the specification of how to do it ([structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) generation). The model uses its linguistic training to understand intent and its fine-tuned schema knowledge to express that intent unambiguously.

## [Link to Function Schema Definition](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#function-schema-definition) Function Schema DefinitionLink Copied

For a language model to invoke [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools), it must first understand what tools are available, what parameters they accept, and what types of values those parameters require. This metadata is provided through **function schemas**, typically expressed in JSON Schema format, which serves as a contract between the model and the external environment. The schema acts as a Rosetta Stone translating between the unstructured world of human language and the rigid requirements of software APIs.

Think of a function schema as a documentation standard that a model can read and act on. When a human developer reads API documentation, they build a mental model of what the function does, what inputs it needs, and what outputs to expect. They can then write code that calls the function correctly. The model does something analogous at inference time: it reads the schema, develops a representation of the tool's purpose, and generates calls that conform to the specification. The quality of the schema directly determines how reliably this process works.

### [Link to JSON Schema Structure](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#json-schema-structure) JSON Schema StructureLink Copied

A function schema describes the interface of a callable function using a structured dictionary. At minimum, it specifies the function name, a natural language description of its purpose, and the expected parameters.

In\[2\]:

Code

```
weather_schema = {
    "name": "get_weather",
    "description": "Retrieve current weather conditions for a specific location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "The city and state/country, e.g., 'Boston, MA' or 'Paris, France'",
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "Temperature unit to use for the forecast",
            },
        },
        "required": ["location"],
    },
}
```

The key components of a function schema are:

- **name**: A unique identifier for the function using snake\_case conventions. This becomes the token the model emits to signal which tool to invoke. The choice of name matters semantically, as models often infer function purpose partially from the name itself. A function named `get_current_temperature` will likely be invoked for different queries than one named `get_historical_weather_data`, even if their schemas are similar.
- **description**: A clear, imperative explanation of what the function does and when to use it. This text is semantically embedded into the model's context, and heavily influences whether the model chooses to invoke this particular tool. Well-written descriptions act as soft classifiers, helping the model distinguish between similar tools. For instance, if you have both a `search_products` and `get_product_details` function, the description should clarify that the former is for finding items matching criteria while the latter requires a specific product ID.
- **parameters**: A JSON Schema object defining the function's arguments, including type constraints, valid ranges, and nested object structures. This section effectively constrains the model's output space, limiting what it can generate to syntactically valid structures.
- **required**: A list of parameter names that must be provided for the function call to be valid. This creates a hard constraint: if the model attempts to call the function without these parameters, the call fails validation. This forces the model to either extract the necessary information from your query or ask for clarification, rather than hallucinating missing values.

The description field deserves special attention because it operates on two levels simultaneously. At the syntactic level, it tells the model the signature of the function. At the semantic level, it guides the model's judgment about when to invoke the function at all. A description like "Retrieve current weather conditions" implicitly communicates that this function is appropriate for present-tense weather queries but not for historical weather data or general weather science questions. Writing descriptions that calibrate this boundary accurately is one of the most important skills in [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) design.

### [Link to Type System and Constraints](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#type-system-and-constraints) Type System and ConstraintsLink Copied

JSON Schema provides rich typing capabilities that help constrain model outputs and prevent hallucinated parameters. These constraints serve as [guardrails](https://mbrenndoerfer.com/writing/content-safety-and-moderation-ai-agents) that reduce the cognitive load on the model during generation. When a parameter is constrained to an integer type with a minimum value of zero, the model need not consider negative numbers or fractional values, effectively narrowing the search space during token sampling.

The available type primitives and constraint mechanisms include:

- **Primitive types**: `string`, `number`, `integer`, `boolean`, `array`, `object`, and `null`. These basic types align with most programming language type systems, making translation to actual function arguments straightforward.
- **Enum constraints**: Restrict string values to a predefined set of options, reducing the probability of invalid values. For example, a `color` parameter with enum `["red", "green", "blue"]` prevents the model from inventing colors like "turquoise" when only primary colors are supported by the underlying API.
- **Array schemas**: Define homogeneous arrays with `items` specifications or heterogeneous tuples with `prefixItems`. This allows for complex inputs like lists of coordinates or structured records.
- **Nested objects**: Support complex parameter structures through recursive `properties` definitions. This is essential for APIs that require structured data, such as shipping addresses with nested fields for street, city, and postal code.
- **Validation keywords**: `minimum`, `maximum`, `minLength`, `maxLength`, `pattern` ([regex](https://mbrenndoerfer.com/writing/regular-expressions-pattern-matching-nlp-python)), and `format` (email, URI, date-time). These constraints serve dual purposes. During inference, they guide the model toward valid outputs through the semantic cues in parameter descriptions. During structured decoding (as discussed in [Constrained Decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output)), they can be enforced grammatically to guarantee syntactic validity.

The interplay between these constraints creates a robust interface. When a model sees a parameter defined as a string with pattern `^[0-9]{5}$`, it understands not just that a zip code is required, but that the value must consist of exactly five digits. This semantic signal helps the model extract the correct information from your queries or recognize when it lacks necessary information.

A well-designed schema reduces ambiguity at every level. Numeric ranges communicate expected magnitudes: a `page_number` parameter with `minimum: 1` implicitly tells the model that pages are one-indexed, not zero-indexed. String format constraints communicate the expected structure of textual inputs. Even the choice between `number` and `integer` provides semantic information: using `integer` for a `quantity` parameter signals that fractional quantities are not meaningful. Every constraint you add is information the model can use to generate more accurate calls.

### [Link to Schema Design Best Practices](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#schema-design-best-practices) Schema Design Best PracticesLink Copied

Writing effective schemas is an iterative process that benefits from understanding how the model interprets them. The descriptions you write are not just documentation for human readers; they are the primary signal the model uses to decide whether and how to invoke the tool. Treat every word in a description as meaningful input to the model's decision process.

Several principles consistently produce more reliable schemas. First, be specific about what the function does rather than what it is. "Search products" is weaker than "Search the catalog for products matching keywords, returning up to 20 results sorted by relevance." The latter communicates the function's behavior, expected output format, and appropriate use case. Second, explicitly describe what the function does _not_ do when there is potential for confusion with similar tools. If you have both a `search_products` and a `lookup_product_by_id` function, adding "Do not use this function when you have a specific product ID; use lookup\_product\_by\_id instead" to the search function's description prevents the model from using the wrong tool.

Third, use consistent naming conventions across all functions in a toolkit. If some functions use `user_id` as a parameter name and others use `userId` or `uid`, the model may struggle to recognize that they refer to the same concept. Consistency reduces the cognitive overhead the model faces when reading schemas and makes [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) more reliable. Fourth, keep required parameters minimal. Every required parameter is a point of potential failure: if the model cannot extract or infer the value, the call fails. When a parameter can be given a sensible default, make it optional with a default value documented in the description.

Finally, test your schemas with adversarial queries: questions that are adjacent to the function's domain but should not trigger it, questions that require the function but provide information in unexpected formats, and questions that are genuinely ambiguous between multiple tools. The cases where the model makes wrong decisions reveal gaps in your schema descriptions that can be addressed iteratively.

### [Link to Multiple Function Definitions](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#multiple-function-definitions) Multiple Function DefinitionsLink Copied

Real-world applications rarely expose a single tool. Instead, they present the model with a toolkit containing multiple functions. The schemas are provided as a list, and the model must learn to select the appropriate function based on your intent. This selection process mirrors the routing logic in traditional software systems, but happens dynamically based on natural language understanding.

In\[3\]:

Code

```
tools = [\
    {\
        "name": "search_database",\
        "description": "Query the product database for items matching criteria",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "query": {"type": "string", "description": "Search terms"},\
                "category": {\
                    "type": "string",\
                    "enum": ["electronics", "clothing", "books"],\
                },\
                "max_price": {\
                    "type": "number",\
                    "description": "Maximum price filter",\
                },\
            },\
            "required": ["query"],\
        },\
    },\
    {\
        "name": "calculate_shipping",\
        "description": "Calculate shipping cost based on weight and destination",\
        "parameters": {\
            "type": "object",\
            "properties": {\
                "weight_kg": {"type": "number", "minimum": 0},\
                "destination_zip": {"type": "string", "pattern": "^[0-9]{5}$"},\
                "express": {"type": "boolean", "default": False},\
            },\
            "required": ["weight_kg", "destination_zip"],\
        },\
    },\
]
```

When multiple functions are available, the model performs implicit [tool selection](https://mbrenndoerfer.com/writing/tool-selection-llm-agents-routing-strategies) by emitting the `name` field corresponding to the appropriate schema. This selection mechanism relies on the semantic alignment between your query, function descriptions, and parameter descriptions. The model essentially performs a form of nearest-neighbor search in embedding space, matching your intent against the semantic content of available tool descriptions.

Consider asking, "How much to ship a 5kg package to Boston?" The model must recognize that while both tools are available, only `calculate_shipping` addresses the specific question. It extracts "5kg" as the weight parameter, infers the zip code for Boston (or recognizes it needs this specific information), and understands that the express parameter is optional. This discrimination capability requires the model to develop a sophisticated understanding of tool capabilities through training on diverse examples. We'll explore more sophisticated selection strategies in the upcoming chapter on Tool Selection.

The challenge of [multi-tool](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) selection scales non-linearly with the number of tools available. With two tools, the selection problem is straightforward. With ten tools, the model must maintain a richer understanding of tool boundaries. With hundreds of tools (as in enterprise environments with dozens of integrated APIs), the selection problem can overwhelm the [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp) and tax the model's attention. Practical systems often solve this by implementing a [two-stage retrieval](https://mbrenndoerfer.com/writing/reranking-cross-encoders-information-retrieval): first retrieving the most relevant tools using embedding similarity, then presenting only the top-k candidates to the model. This mirrors how human experts navigate large toolsets: they first recall which category of tool applies, then select the specific tool within that category.

Out\[4\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/tool-count-selection-accuracy.png

Tool selection accuracy as a function of the number of available tools in the context. Accuracy declines as the number of tools grows, particularly when schema descriptions are ambiguous or overlapping. The two-stage retrieval approach maintains higher accuracy at scale by reducing the selection problem to a manageable subset before the final selection step.

## [Link to Function Call Generation](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#function-call-generation) Function Call GenerationLink Copied

Given a set of function schemas and your query, the model must determine whether to answer directly, request clarification, or emit a structured function call. This decision emerges from the model's training on large corpora of tool-use demonstrations. The generation process represents a specialized form of [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) prediction, where the output must conform to a specific grammar defined by the function schema.

The key insight is that function call generation is not a fundamentally different capability from ordinary text generation: it is the same next-token prediction mechanism applied to a different output distribution. What changes is the target distribution. During pre-training, the model learns to predict the next token in human-written text. During [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) fine-tuning, the model learns to predict the next token in structured, schema-conforming JSON. The architecture is identical; only the training data and target format differ.

### [Link to Training for Tool Use](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#training-for-tool-use) Training for Tool UseLink Copied

Function calling capability is typically instilled through supervised fine-tuning on specialized datasets. These datasets consist of conversation traces where:

1. The system prompt includes available function definitions
2. User queries require tool invocation to answer correctly
3. Assistant responses alternate between function call objects and final answers based on observation results

The training objective remains next-token prediction, but the target distribution now includes structured JSON snippets interleaved with natural language. This multimodal output space requires the model to learn special transition dynamics: when to switch from natural language to JSON, how to maintain syntactic validity across token boundaries, and when to terminate a function call versus continuing with explanation.

Models learn to recognize patterns such as:

- Queries containing temporal references ("current weather," "latest stock price") likely require tool calls because the model's training data has a cutoff date and cannot provide real-time information.
- Mathematical precision requirements often necessitate calculator tools, especially for complex expressions where the model might otherwise hallucinate incorrect calculations.
- Questions about private or real-time data require retrieval functions, as these fall outside the model's parametric knowledge.

The training process also instills tool awareness: the ability to recognize when a query falls within the domain of available tools versus when it requires general knowledge. A poorly trained model might call a weather API for "What's the capital of France?", while a well-calibrated model recognizes this as factual knowledge requiring no external tool.

One subtle aspect of this training is teaching the model to be appropriately uncertain. When a query is ambiguous, the right behavior is often to ask for clarification rather than guess. "What's the weather?" lacks a location, so a well-trained model should respond with a clarifying question rather than inventing a location. Achieving this calibration requires training examples that explicitly demonstrate the clarification behavior, not just tool-use examples.

### [Link to Generation Formats](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#generation-formats) Generation FormatsLink Copied

Different model families employ varying output formats for [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents), though all share the common thread of structured, parseable text. The choice of format involves trade-offs between human readability, parsing complexity, and semantic clarity.

OpenAI-style function calling uses a specific message role and JSON structure:

```
{
  "role": "assistant",
  "tool_calls": [\
    {\
      "id": "call_abc123",\
      "type": "function",\
      "function": {\
        "name": "get_weather",\
        "arguments": "{\"location\": \"Boston, MA\", \"unit\": \"celsius\"}"\
      }\
    }\
  ]
}
```

This format treats function calls as first-class objects in the message hierarchy, with explicit typing and unique identifiers. The nested structure separates the function metadata (name) from the payload (arguments), making it easy for downstream parsers to route calls to appropriate handlers.

Anthropic-style tool use embeds XML tags within the text:

```
<function_calls>
<invoke name="get_weather">
<parameter name="location">Boston, MA</parameter>
<parameter name="unit">celsius</parameter>
</invoke>
</function_calls>
```

XML formats offer advantages in streaming scenarios, where partial JSON might be invalid but partial XML maintains structure. They also allow for easier human inspection and debugging, as the hierarchical structure is visually apparent through indentation and tag matching.

Generalized [JSON mode](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) simply instructs the model to output valid JSON matching the schema, often with special tokens delimiting the start and end of tool calls. This approach maximizes flexibility but requires careful prompt engineering to ensure the model distinguishes between explanatory text and executable code.

Regardless of format, the underlying mechanism relies on the decoder's ability to generate structured text that conforms to a grammar. Building on our discussion of [Autoregressive Generation](https://mbrenndoerfer.com/writing/autoregressive-generation-gpt-text-generation), the model samples tokens conditioned on the function schema context, with the schema effectively biasing the output distribution toward valid JSON structures. The [attention mechanism](https://mbrenndoerfer.com/writing/attention-mechanism-intuition-soft-lookup-weights-context-vectors) must learn to attend to specific parts of the schema when generating corresponding parameters, ensuring that the `location` value in the output aligns with the location parameter description in the input.

The format choice also has implications for error recovery. JSON formats are all-or-nothing: a single missing bracket or unescaped quote invalidates the entire structure. XML formats are more forgiving in streaming contexts because each field is independently delimited. Some production systems implement [constrained decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output), as we discussed in [Constrained Decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output), where the decoder's [sampling distribution](https://mbrenndoerfer.com/writing/central-limit-theorem-foundation-statistical-inference) is grammatically restricted to guarantee syntactic validity. This eliminates parse errors entirely but adds implementation complexity and may slightly restrict the model's expressive range.

### [Link to Parallel Function Calling](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#parallel-function-calling) Parallel Function CallingLink Copied

Modern implementations support parallel [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents), where the model identifies multiple independent operations that can be executed simultaneously. For example, given the query "Compare the weather in Boston and San Francisco," the model might emit two separate function calls in a single response:

```
{
  "tool_calls": [\
    {"id": "call_1", "function": {"name": "get_weather", "arguments": "{\"location\": \"Boston, MA\"}"}},\
    {"id": "call_2", "function": {"name": "get_weather", "arguments": "{\"location\": \"San Francisco, CA\"}"}}\
  ]
}
```

This capability requires the model to recognize functional dependencies and independence between requested operations. In the weather comparison example, the two calls are independent: neither requires the output of the other. However, for a query like "What's the weather in the capital of California?", the model must recognize the dependency chain: first determine the capital (Sacramento), then get its weather. Attempting to parallelize these calls would fail because the second call requires information only available after the first completes.

Parallel calling significantly reduces latency in [multi-tool](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) scenarios but requires the execution framework to handle concurrent API calls and aggregate results. The framework must track which calls belong to which logical operation, handle partial failures (where one call succeeds and another fails), and manage race conditions in stateful operations. This pattern essentially transforms the linear [request-response](https://mbrenndoerfer.com/writing/communication-between-agents) cycle into a graph execution problem, where the model defines the nodes ([function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents)) and the system manages the edges (dependencies and data flow).

Out\[5\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/parallel-vs-sequential-latency.png

Latency comparison between parallel and sequential execution strategies for multiple independent function calls. Sequential latency grows linearly at 1.2 seconds per call, while parallel latency grows much more slowly due to concurrent execution. For five independent calls, parallelization reduces total latency from 6.0 seconds to under 2.0 seconds.

## [Link to Function Output Handling](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#function-output-handling) Function Output HandlingLink Copied

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) establishes a [request-response](https://mbrenndoerfer.com/writing/communication-between-agents) cycle between the language model and [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools). Once a function executes, its return value must be formatted and presented back to the model to enable the final response generation. This cycle creates a [feedback loop](https://mbrenndoerfer.com/writing/continuous-feedback-and-improvement-ai-agents) where the model can react to real-world data, correcting misconceptions or filling knowledge gaps dynamically.

The design of this feedback loop is more subtle than it first appears. The model must not only receive the function output but interpret it in the context of the original query. A raw JSON response from a weather API contains temperature, humidity, wind speed, and conditions. The model must select which of these fields are relevant to your question, convert units if requested, and frame the information in natural language that answers the original intent. This interpretation step requires the model to maintain awareness of the original query throughout the tool-execution cycle.

### [Link to The Observation Pattern](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#the-observation-pattern) The Observation PatternLink Copied

The standard execution loop follows an observe-act pattern with distinct stages. Your query enters the conversation and the model processes it against available schemas. If a tool is warranted, the model emits a structured function call. The application executes the function with the provided arguments and formats the result as an observation message. This observation is appended to the [conversation history](https://mbrenndoerfer.com/writing/short-term-conversation-memory-ai-agents), and the model generates a final natural language response incorporating the new information.

This pattern mirrors the perception-action cycles found in cognitive architectures and robotics. The model acts (generates a function call), observes the result (receives the tool output), and then acts again (generates a response) based on the updated state. This loop can iterate multiple times for complex queries requiring sequential [tool use](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents).

The observation is typically formatted as a tool message (or function result message) containing the function output, often JSON-serialized:

```
{
  "role": "tool",
  "tool_call_id": "call_abc123",
  "name": "get_weather",
  "content": "{\"temperature\": 22, \"conditions\": \"Partly cloudy\", \"humidity\": 65}"
}
```

This message structure is critical because it maintains the conversation state necessary for the model to generate coherent multi-turn interactions. The `tool_call_id` links the observation back to the specific request, enabling the model to handle parallel calls correctly. Without this linkage, the model might confuse which result corresponds to which query, especially when multiple similar tools are invoked simultaneously.

The content of the observation should be structured to maximize the model's comprehension. Raw API responses often contain extraneous metadata, status codes, and internal identifiers. Best practice involves transforming these into clean, semantic representations that highlight the information relevant to your query. For weather data, this might mean extracting just temperature and conditions, while for database queries, it might involve formatting records as readable text or markdown tables.

There is an important design choice here: how much preprocessing to do before returning tool output to the model. Returning raw API responses preserves all information but may confuse the model with irrelevant fields. Returning heavily summarized results is more efficient but risks discarding information the model might need. A practical middle ground is to return the full relevant payload while using clear field names and removing only truly irrelevant metadata (like internal request IDs, rate limit headers, and server timestamps).

### [Link to Context Window Implications](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#context-window-implications) Context Window ImplicationsLink Copied

Each function call and observation consumes tokens in the [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp). In scenarios involving multiple tool invocations or verbose API responses, this can quickly exhaust available context length. A complex database query might return hundreds of rows, each consuming dozens of tokens when serialized as JSON. As we explored in [Context Length Challenges](https://mbrenndoerfer.com/writing/context-length-challenges-transformers), long tool outputs may need summarization or selective filtering before being presented to the model.

Strategies for managing context in tool-heavy conversations include:

- **Result summarization**: Using smaller models or heuristics to compress verbose API outputs into key points before presenting them to the main model.
- **Pagination**: Breaking large result sets into chunks and allowing the model to request specific pages or aggregates.
- **Selective retention**: Keeping only the most recent tool results in context while archiving older ones to a separate memory store.

Furthermore, the recursive nature of [tool use](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents), where observations trigger additional function calls, creates deep conversation histories. A complex research task might involve ten or more tool calls, each adding multiple messages to the thread. Efficient management of this history, potentially through [KV Cache Compression](https://mbrenndoerfer.com/writing/kv-cache-compression-eviction-quantization-h2o-algorithm) or selective context pruning, becomes essential for production deployments. Some systems implement conversation summarization at fixed intervals, condensing older tool interactions into high-level summaries that preserve essential information while freeing up tokens for new operations.

The token cost of function calling is frequently underestimated. A system prompt listing ten detailed tool schemas might consume 2,000 tokens before a single word of your query is processed. This front-loading of context means that function calling applications effectively have shorter usable context windows than their nominal context limit suggests. Designing compact but informative schemas, and using retrieval-based schema selection to present only relevant tools, helps recover this overhead.

Out\[6\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/context-window-growth.png

Cumulative token consumption across function calling iterations, illustrating how tool calls and observations accumulate in the context window. Starting from an initial system and user message of around 920 tokens, each tool call and observation cycle adds approximately 600 tokens. A dashed red line marks a typical 4096-token context limit, showing how multi-step tool use can rapidly approach capacity.

### [Link to Error Handling](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#error-handling) Error HandlingLink Copied

Not all [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) succeed. Networks fail, APIs return errors, and arguments may be invalid. The [error handling](https://mbrenndoerfer.com/writing/plan-and-execute-ai-agents) strategy significantly impacts robustness and user experience. A brittle system that crashes on API timeouts provides little value, while a resilient system that gracefully degrades maintains utility even under adverse conditions.

Common error handling patterns include:

- **Retry with correction**: Present the error to the model and allow it to generate a corrected call. For example, if a weather API returns "Location not found" for "Bostn, MA", the model might infer the typo and retry with "Boston, MA". This requires the error message to be descriptive enough to enable diagnostic reasoning.
- **Fallback to knowledge**: If the tool fails, the model falls back to its parametric knowledge with appropriate uncertainty qualifiers. For instance, "I was unable to check the live weather, but based on my training data, Boston in January is typically cold, often below freezing." This maintains utility while signaling uncertainty.
- **Escalation to you**: For critical failures, the system asks you for clarification or manual input. This is appropriate when the model lacks sufficient information to recover autonomously, such as when required authentication tokens expire.

Error messages should be structured to help the model diagnose issues. Rather than generic "Error 500" messages, provide specific feedback: "Invalid location format: expected 'City, State' but received 'Boston'". This specificity enables the model to adjust its approach, perhaps by asking you for clarification or by reformatting the parameter according to the API's expectations. The error format should mirror the success format (JSON with consistent fields) to ensure the model can parse it reliably.

There is also a category of logical errors that are harder to detect: cases where the function executes successfully but returns data that is semantically incorrect for the query. If your query asks about tomorrow's weather and the API returns today's weather, the function call technically succeeded. The model must reason about whether the returned data actually answers the question. Designing observation formats that include metadata about the query parameters (such as the date range returned by a weather API) helps the model perform this validation.

## [Link to Worked Example: Multi-Step Calculation](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#worked-example-multi-step-calculation) Worked Example: Multi-Step CalculationLink Copied

Let's walk through a concrete example involving a [calculator tool](https://mbrenndoerfer.com/writing/ai-agent-calculator-tool-implementation-guide) to illustrate the full [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) cycle.

Scenario: You ask, "If I have 150 apples and give away 30%, then buy 2 dozen more, how many do I have?"

While modern LLMs can solve this arithmetically, we'll assume our model has been instructed to use a calculator for precision. This scenario demonstrates how function calling handles multi-step reasoning where natural language must be translated into mathematical expressions.

**Step 1: Schema Definition**

In\[7\]:

Code

```
calculator_schema = {
    "name": "calculate",
    "description": "Evaluate a mathematical expression safely",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Mathematical expression to evaluate, e.g., '(150 * 0.7) + 24'",
            }
        },
        "required": ["expression"],
    },
}
```

**Step 2: Initial Query**

Your message enters the conversation context along with the available function definitions. The model processes this input through its attention layers, comparing the query against the calculator description to determine that mathematical evaluation is required.

**Step 3: Call Generation**

The model recognizes the arithmetic nature of the query and generates:

```
{
  "name": "calculate",
  "arguments": "{\"expression\": \"150 * 0.7 + 24\"}"
}
```

Note that the model has translated "give away 30%" into the multiplicative factor 0.7 and "2 dozen" into 24, demonstrating its ability to perform semantic translation into executable parameters. This translation step highlights the model's role as an interface layer between human communication patterns and machine-executable instructions. The model must understand that "giving away 30%" leaves 70%, and that a "dozen" equals twelve, making two dozen equal twenty-four.

The translation is non-trivial. The model must correctly chain two operations: first apply the percentage reduction, then add the new quantity. Expressing this as a single expression `150 * 0.7 + 24` requires understanding operator precedence (multiplication before addition) and recognizing that the 30% reduction and the subsequent purchase are independent operations on the running count.

**Step 4: Execution**

The application layer parses the JSON, validates that the expression contains only safe mathematical operations (preventing code injection), and evaluates:

In\[8\]:

Code

```
import ast
import operator

def safe_calculate(expression):
    """Safely evaluate mathematical expression using AST parsing.
    All nodes are validated against an allowlist before any evaluation occurs."""
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }

    def eval_node(node):
        if isinstance(node, ast.Num):  # Python 3.7
            return node.n
        elif isinstance(node, ast.Constant):  # Python 3.8+
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type in allowed_operators:
                return allowed_operators[op_type](
                    eval_node(node.left), eval_node(node.right)
                )
        elif isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return -eval_node(node.operand)
        raise ValueError(f"Unsupported operation: {type(node)}")

    tree = ast.parse(expression, mode="eval")
    result = eval_node(tree.body)
    return result

result = safe_calculate("150 * 0.7 + 24")
```

Out\[9\]:

Console

```
Calculation result: 129.0
```

The calculation yields 129.0 apples, confirming that after giving away 30% (45 apples) from the original 150 and adding 24 more, you have 129 apples remaining.

**Step 5: Observation Injection**

The result `129.0` is formatted as a tool message and appended to the context. This injection step is transparent to you but crucial for the model's [reasoning chain](https://mbrenndoerfer.com/writing/understanding-and-debugging-agent-behavior). The observation provides grounding, ensuring the final answer is based on actual computation rather than estimation.

**Step 6: Final Response**

The model now generates: "You would have 129 apples."

This example demonstrates the complete loop: intent recognition, [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents), safe execution, and natural language synthesis based on structured data. It illustrates how [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) creates a division of labor: the model handles language understanding and translation, while specialized tools handle precise computation. This separation of concerns allows each component to excel at what it does best, combining the linguistic flexibility of LLMs with the computational accuracy of traditional software.

The example also illustrates why safe execution matters. The `safe_calculate` function uses Python's AST module to parse the expression before evaluating it, explicitly checking that only arithmetic operations are present. The entire expression tree is walked and validated against an allowlist before any computation occurs. This architecture is a standard pattern for secure expression evaluation in function calling contexts.

## [Link to Code Implementation: Building a Function Calling System](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#code-implementation-building-a-function-calling-system) Code Implementation: Building a Function Calling SystemLink Copied

Let's implement a complete [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) pipeline using Python. We'll create a mock LLM interface that simulates generation, then build the execution framework around it. This implementation demonstrates the architectural patterns used in production systems, abstracted for clarity.

The architecture we build here separates three distinct concerns. The tool registry manages the available capabilities: it stores schemas (the contract with the LLM) and implementations (the actual executable code). The mock LLM encapsulates the decision logic: which tool to call and with what arguments. The agent orchestrates the interaction: it maintains conversation state, sends queries to the LLM, executes tool calls, and feeds results back into the conversation. In a production system, the mock LLM would be replaced by real API calls, but the registry and agent patterns remain unchanged. This separation of concerns is what makes function calling systems maintainable as they grow: you can swap out the LLM backend without touching the tool implementations, or add new tools without modifying the orchestration logic.

In\[10\]:

Code

```
from typing import Dict, List, Any
from dataclasses import dataclass, field

@dataclass
class FunctionCall:
    name: str
    arguments: Dict[str, Any]
    call_id: str

@dataclass
class Message:
    role: str
    content: str = None
    tool_calls: List[FunctionCall] = None
    tool_call_id: str = None
    name: str = None
```

First, we define a registry for available tools. This registry maps function names to implementations and maintains their schemas. The registry pattern centralizes tool management, providing a single source of truth for both the schemas (consumed by the LLM) and the implementations (consumed by the execution environment).

In\[11\]:

Code

```
from typing import Callable

class ToolRegistry:
    def __init__(self):
        self.tools: Dict[str, Dict] = {}
        self.implementations: Dict[str, Callable] = {}

    def register(self, name: str, schema: Dict, implementation: Callable):
        self.tools[name] = schema
        self.implementations[name] = implementation

    def get_schemas(self) -> List[Dict]:
        return [\
            {"type": "function", "function": schema}\
            for schema in self.tools.values()\
        ]

    def execute(self, call: FunctionCall) -> Any:
        if call.name not in self.implementations:
            raise ValueError(f"Unknown function: {call.name}")

        func = self.implementations[call.name]
        try:
            result = func(**call.arguments)
            return {"status": "success", "result": result}
        except Exception as e:
            return {"status": "error", "error": str(e)}
```

The `execute` method wraps the actual function call in a try-except block and returns a structured result with a `status` field. This pattern ensures that even when tools fail, the return value is parseable JSON that the model can reason about. A failed call that returns `{"status": "error", "error": "Location not found"}` gives the model actionable information; a failed call that raises an unhandled exception gives it nothing.

Now we implement the actual tools. We'll create a weather lookup and a calculator, simulating the weather API while actually implementing the calculator. This mixed approach is typical in development environments, where some tools connect to real services while others use mocks or local implementations.

In\[12\]:

Code

```
def mock_weather_api(location: str, unit: str = "celsius") -> dict:
    """Simulated weather API for demonstration"""
    weather_db = {
        "boston, ma": {
            "temp": 22,
            "condition": "Partly cloudy",
            "humidity": 65,
        },
        "san francisco, ca": {"temp": 18, "condition": "Foggy", "humidity": 80},
        "london, uk": {"temp": 15, "condition": "Rainy", "humidity": 90},
    }

    key = location.lower().strip()
    if key not in weather_db:
        return {"error": f"No data available for {location}"}

    data = weather_db[key]
    if unit == "fahrenheit":
        data = {**data, "temp": data["temp"] * 9 / 5 + 32}

    return data

def calculator_tool(expression: str) -> float:
    """Safe calculator using AST-based expression evaluation.
    All nodes are validated against an allowlist before any evaluation occurs."""
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.USub: operator.neg,
    }

    def eval_node(node):
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)):
                raise ValueError("Only numeric constants allowed")
            return node.value
        elif isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in allowed_ops:
                raise ValueError(f"Disallowed operator: {op_type.__name__}")
            return allowed_ops[op_type](eval_node(node.left), eval_node(node.right))
        elif isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -eval_node(node.operand)
        raise ValueError(f"Disallowed node type: {type(node).__name__}")

    tree = ast.parse(expression, mode="eval")
    return eval_node(tree.body)
```

We instantiate the registry and register our tools:

In\[13\]:

Code

```
registry = ToolRegistry()

weather_schema = {
    "name": "get_weather",
    "description": "Get current weather for a location",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and state/country",
            },
            "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "default": "celsius",
            },
        },
        "required": ["location"],
    },
}

calc_schema = {
    "name": "calculate",
    "description": "Calculate mathematical expressions",
    "parameters": {
        "type": "object",
        "properties": {
            "expression": {
                "type": "string",
                "description": "Math expression to evaluate",
            }
        },
        "required": ["expression"],
    },
}

registry.register("get_weather", weather_schema, mock_weather_api)
registry.register("calculate", calc_schema, calculator_tool)
```

For demonstration purposes, we'll simulate the LLM's [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) behavior with rule-based responses. In practice, this would be replaced with actual API calls to [GPT-4](https://mbrenndoerfer.com/writing/gpt4-multimodal-language-models-reach-human-level-performance), Claude, or open-source models with function calling capabilities. This mock implementation illustrates the expected interface: the LLM receives [conversation history](https://mbrenndoerfer.com/writing/short-term-conversation-memory-ai-agents) and returns either a text response or a structured tool call.

In\[14\]:

Code

```
import re

class MockLLM:
    """Simulates an LLM with function calling capabilities"""

    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        self.call_count = 0

    def generate(self, messages: List[Message]) -> Message:
        """Simulate generation based on message history"""
        last_message = messages[-1]
        content = last_message.content.lower() if last_message.content else ""

        # Simple pattern matching to simulate tool use decisions
        if "weather" in content:
            self.call_count += 1
            # Extract location with simple regex
            match = re.search(r"weather\s+(?:in|for)?\s+(.+?)(?:\?|$)", content)
            if match:
                location = match.group(1).strip()
                return Message(
                    role="assistant",
                    tool_calls=[\
                        FunctionCall(\
                            name="get_weather",\
                            arguments={"location": location},\
                            call_id=f"call_{self.call_count}",\
                        )\
                    ],
                )

        elif any(
            word in content
            for word in ["calculate", "compute", "sum", "product", "how many"]
        ):
            self.call_count += 1
            # Look for math expressions
            numbers = re.findall(r"\d+", content)
            if len(numbers) >= 2 and "sum" in content:
                return Message(
                    role="assistant",
                    tool_calls=[\
                        FunctionCall(\
                            name="calculate",\
                            arguments={\
                                "expression": f"{numbers[0]} + {numbers[1]}"\
                            },\
                            call_id=f"call_{self.call_count}",\
                        )\
                    ],
                )

        # Default response if no tool needed
        return Message(
            role="assistant", content="I don't need any tools to answer this."
        )
```

Now we implement the execution loop that orchestrates the interaction between the LLM and tools. This agent class encapsulates the [state management](https://mbrenndoerfer.com/writing/understanding-the-agents-state) and control flow, maintaining the [conversation history](https://mbrenndoerfer.com/writing/short-term-conversation-memory-ai-agents) and managing the iterative cycle of generation and execution.

In\[15\]:

Code

```
import json

class FunctionCallingAgent:
    def __init__(
        self, llm: MockLLM, registry: ToolRegistry, max_iterations: int = 5
    ):
        self.llm = llm
        self.registry = registry
        self.max_iterations = max_iterations
        self.conversation: List[Message] = []

    def run(self, user_query: str) -> str:
        """Execute the full function calling loop"""
        # Add system message with tool descriptions
        system_msg = f"You have access to the following tools: {json.dumps(self.registry.get_schemas())}"
        self.conversation = [Message(role="system", content=system_msg)]
        self.conversation.append(Message(role="user", content=user_query))

        for iteration in range(self.max_iterations):
            # Generate response
            response = self.llm.generate(self.conversation)

            # Check if tool calls were made
            if response.tool_calls:
                self.conversation.append(response)

                # Execute all tool calls (parallel execution)
                for call in response.tool_calls:
                    result = self.registry.execute(call)

                    # Add observation to conversation
                    obs_msg = Message(
                        role="tool",
                        content=json.dumps(result),
                        tool_call_id=call.call_id,
                        name=call.name,
                    )
                    self.conversation.append(obs_msg)

                # Continue loop for final generation
                continue
            else:
                # No tool calls, return final answer
                return response.content

        return "Maximum iterations reached without final answer."
```

In\[16\]:

Code

```
agent = FunctionCallingAgent(MockLLM(registry), registry)
agent_result = agent.run("What's the weather in Boston, MA?")
```

Out\[17\]:

Console

```
Final result: I don't need any tools to answer this.
```

The execution trace shows the complete cycle: the agent recognizes the weather query, extracts the location parameter, executes the mock API, and would typically generate a final response (in this simulation, the mock LLM returns a placeholder). This architecture separates concerns cleanly: the agent manages state and orchestration, the registry handles tool management, and the LLM handles decision-making. Such separation allows for easy extension, testing, and maintenance of production [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) systems.

The `max_iterations` guard deserves particular attention. Without it, a malfunctioning model that repeatedly generates tool calls without ever producing a final answer would loop forever, consuming API credits and blocking other requests. The iteration limit is a safety valve, not an expected boundary condition. Well-calibrated models almost never reach it. When they do, it is often a signal that the query is ambiguous, the tool outputs are confusing the model, or the model is stuck in a pattern matching loop. Logging iteration counts in production helps identify these pathological cases.

## [Link to Key Parameters](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#key-parameters) Key ParametersLink Copied

The key parameters governing a [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) system's behavior are:

- **max\_iterations**: Maximum number of tool invocation cycles allowed before terminating. This prevents infinite loops in cases where the model repeatedly invokes tools without reaching a final answer. Setting this parameter requires balancing completeness against resource constraints. A value of 3 to 5 is typically sufficient for most use cases, while complex research tasks might require 10 or more. Exceeding this limit usually indicates either a poorly calibrated model stuck in a loop or a query that genuinely requires more steps than the system allows.
- **tool\_call\_id**: Unique identifier linking each observation back to its corresponding function call, essential for handling parallel function calls correctly. In production systems, these IDs must be globally unique and persistent across the conversation lifecycle to ensure proper attribution of results. UUIDs or timestamped identifiers are commonly used.
- **required**: List of parameter names in the function schema that must be provided for the call to be valid, ensuring critical arguments are not omitted. This list acts as a contract enforcement mechanism. When the model attempts to call a function without a required parameter, the system should reject the call and either prompt the model for the missing information or return a validation error that the model can use to correct its approach.

## [Link to Function Calling Fine-Tuning](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#function-calling-fine-tuning) Function Calling Fine-TuningLink Copied

While general-purpose models like [GPT-4](https://mbrenndoerfer.com/writing/gpt4-multimodal-language-models-reach-human-level-performance) come with robust [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) capabilities, open-source models often require fine-tuning to reliably emit structured tool calls. This process involves curating datasets of tool-use conversations and optimizing the model for schema adherence. Fine-tuning transforms a base model from a general text generator into a specialized tool-calling agent.

The need for fine-tuning is not merely about format compliance. A base model might generate syntactically valid JSON that is semantically wrong: it might call the right function but with hallucinated parameter values, or invoke a tool when the answer is already in its parametric knowledge. Fine-tuning teaches the model not just the output format, but the judgment of when and how to invoke tools correctly. This judgment is fundamentally a classification problem: for every query, the model must decide among (a) answer directly, (b) request clarification, (c) call one or more tools.

### [Link to Dataset Construction](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#dataset-construction) Dataset ConstructionLink Copied

Fine-tuning data for function calling follows a conversation format where each example consists of:

1.  **System Prompt**: Defines available functions and general behavior guidelines
2.  **User Messages**: Queries that require tool invocation
3.  **Assistant Messages**: Either [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) (in the structured format) or final answers
4.  **Tool Results**: Observations returned from executed functions
5.  **Final Answers**: Natural language responses incorporating tool outputs

A single training example might look like this in ShareGPT format:

```
{
  "conversations": [\
    {"from": "system", "value": "You are a helpful assistant with access to tools..."},\
    {"from": "human", "value": "What's the weather in Paris?"},\
    {"from": "gpt", "value": "<tool_call>{\"name\": \"get_weather\", \"arguments\": {\"location\": \"Paris\"}}</tool_call>"},\
    {"from": "tool", "value": "{\"temperature\": 20, \"condition\": \"Sunny\"}"},\
    {"from": "gpt", "value": "The weather in Paris is sunny with a temperature of 20 degrees Celsius."}\
  ]
}
```

The critical aspect is maintaining the exact output format expected at inference time. If the model is expected to wrap tool calls in `<tool_call>` tags, the training data must include these tags consistently. Inconsistency between training and inference formats leads to parsing errors and failed tool invocations. Additionally, training datasets should include diverse examples covering edge cases: tool calls with nested parameters, parallel invocations, error recoveries where the model must retry with corrected parameters, and clarifications where the model asks for missing required fields.

Negative examples are equally important. The dataset should include instances where the model should _not_ call a tool, instead answering from its parametric knowledge. This prevents over-reliance on [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools) and reduces unnecessary API calls and latency.

The diversity of the dataset matters as much as its size. A dataset with 10,000 examples covering only simple single-tool queries will produce a model that fails on [multi-tool](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) queries, ambiguous queries, and error recovery scenarios. A well-constructed dataset of 2,000 examples spanning all behavioral categories will generalize better. Think of the fine-tuning data as a specification of the system's behavioral contract: every pattern you want the model to handle correctly must appear somewhere in the training data.

Constructing high-quality fine-tuning data is expensive because it requires human annotation of correct tool-use behavior. Some teams have found success with synthetic data generation: using a powerful model (like [GPT-4](https://mbrenndoerfer.com/writing/gpt4-multimodal-language-models-reach-human-level-performance)) to generate diverse queries and then annotating the correct tool calls programmatically, then using a weaker model to filter out low-quality examples. This approach can produce large, diverse datasets at reasonable cost but requires careful quality control to prevent the fine-tuned model from inheriting the generator model's failure modes.

Out\[18\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/training-data-distribution.png

Distribution of conversation types in a function calling fine-tuning dataset, showing the balance between tool-required queries, direct answers, and clarification requests. Tool-required queries dominate at 45 percent, but direct-answer and clarification examples are essential to prevent over-reliance on tools and teach appropriate uncertainty handling.

### [Link to Training Objectives](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#training-objectives) Training ObjectivesLink Copied

The fine-tuning process uses standard supervised learning with [cross-entropy loss](https://mbrenndoerfer.com/writing/cross-entropy-loss-language-models-information-theory), but with attention to special tokens that demarcate tool boundaries. As discussed in [Instruction Tuning Training](https://mbrenndoerfer.com/writing/instruction-tuning-training-data-mixing-loss-masking), the learning rate is typically lower than pre-training to preserve general capabilities while adapting to the specific tool-calling format. The model must learn not just the format, but the semantics of when to transition between natural language and structured calls.

Key hyperparameters for [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) fine-tuning include:

-   **Learning rate**: Often 1e-5 to 2e-5, smaller than general fine-tuning to maintain stability. Higher rates might cause [catastrophic forgetting](https://mbrenndoerfer.com/writing/catastrophic-forgetting-fine-tuning-mitigation) of conversational abilities or [overfitting](https://mbrenndoerfer.com/writing/statistical-modeling-overfitting-underfitting-bias-variance-tradeoff) to specific tool formats.
-   **Sequence length**: Must accommodate long tool descriptions and multi-turn conversations. Function schemas can be verbose, especially with nested objects, requiring context windows of 4k tokens or more.
-   **Masking strategy**: Typically, only assistant messages (including tool calls) are used for loss computation, while user and system prompts are masked. This focuses the model's learning on generating appropriate responses rather than predicting your inputs.
-   **Data mixture**: Combining tool-use data with general [instruction data](https://mbrenndoerfer.com/writing/instruction-data-creation-building-training-datasets) prevents catastrophic forgetting of conversational abilities, as explored in [Catastrophic Forgetting](https://mbrenndoerfer.com/writing/catastrophic-forgetting-fine-tuning-mitigation). A typical mixture might be 70% tool-use data and 30% general [instruction following](https://mbrenndoerfer.com/writing/instruction-following-llm-tuning-fundamentals) data, though this varies by base model and target application.

The masking strategy deserves a closer look. When computing the [cross-entropy loss](https://mbrenndoerfer.com/writing/cross-entropy-loss-language-models-information-theory), we want the model to learn to generate correct tool calls and final responses. We do not want it to expend capacity predicting the user's messages or the system prompt. By masking these tokens out of the loss computation (setting their weights to zero), we ensure the gradient signal comes entirely from the model's own outputs. This is the same technique used in [instruction tuning](https://mbrenndoerfer.com/writing/instruction-tuning-adapting-language-models-to-follow-explicit-instructions) more broadly and is crucial for efficient learning.

The training process must also account for the observation phase. Some implementations include simulated tool results in the training data, while others train only on the call generation phase and handle observations as context during inference. The former approach creates a more holistic understanding of the tool-use cycle but requires a dataset of realistic tool outputs. Including observations in training is generally preferred because it teaches the model how to synthesize tool results into natural language responses, which is the final step that makes [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) useful to users.

### [Link to Format-Specific Considerations](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#format-specific-considerations) Format-Specific ConsiderationsLink Copied

Different model families require different fine-tuning approaches based on their native [chat templates](https://mbrenndoerfer.com/writing/instruction-format-chat-templates-role-definitions-llm) and special token vocabularies.

ChatML format (used by many open-source models) structures tool calls as separate message types:

`<|im_start|>system
You have access to the following functions...
<|im_end|>
<|im_start|>user
What's the weather?
<|im_end|>
<|im_start|>assistant
<tool_call>{"name": "get_weather", "arguments": {"location": "Boston"}}</tool_call>
<|im_end|>
<|im_start|>tool
{"temperature": 22}
<|im_end|>
`

[Llama](https://mbrenndoerfer.com/writing/llama-architecture-design-training-efficiency)-2/3 chat formats use specific header tokens to distinguish between tool planning and final responses, often requiring the model to generate thinking tokens or plan steps before emitting the final JSON. These formats may require the model to first output reasoning in special tags, then the tool call, creating a [chain-of-thought](https://mbrenndoerfer.com/writing/chain-of-thought-emergence-how-llms-learn-to-reason) style approach that improves accuracy on complex multi-step problems.

The fine-tuning objective trains the model to recognize when its internal knowledge is insufficient (triggering a tool call) versus when it can answer directly. This calibration requires diverse training examples including:

-   **Tool-required queries**: Questions that cannot be answered without external data, such as current weather or stock prices
-   **Direct answer queries**: Questions within the model's parametric knowledge to prevent over-reliance on tools, such as historical facts or general knowledge
-   **Clarification requests**: Ambiguous queries where the model should ask for parameter specification rather than hallucinate values, training the model to recognize uncertainty and request your input

The boundary between these categories is not always sharp, which is precisely what makes calibration difficult. "What's the population of Tokyo?" can be answered from parametric knowledge with reasonable accuracy (the model knows it's around 14 million in the city proper, 37 million in the greater metropolitan area) but might warrant a database lookup for an application requiring precise current figures. The right behavior depends on the application's accuracy requirements, which should be communicated through the system prompt.

### [Link to Evaluation Metrics](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#evaluation-metrics) Evaluation MetricsLink Copied

Validating [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) models requires specialized metrics beyond standard [perplexity](https://mbrenndoerfer.com/writing/perplexity-language-model-evaluation-metric) or [BLEU](https://mbrenndoerfer.com/writing/bleu-score-machine-translation-evaluation-nlp) scores. These metrics assess both the syntactic correctness and semantic appropriateness of tool use:

-   **Schema adherence rate**: Percentage of generated calls that parse as valid JSON and match the defined schema. This is a hard constraint; even minor syntax errors render the call unusable.
-   **Parameter accuracy**: Correctness of extracted parameters (e.g., did the model correctly identify "Boston" as the location). This measures the model's ability to map natural language entities to structured fields.
-   **[Tool selection](https://mbrenndoerfer.com/writing/tool-selection-llm-agents-routing-strategies) accuracy**: Frequency with which the model chooses the correct function from multiple options. This assesses the model's semantic understanding of tool purposes and boundaries.
-   **[False positive rate](https://mbrenndoerfer.com/writing/type-i-type-ii-errors-false-positives-false-negatives-statistical-power)**: How often the model invokes tools unnecessarily for answerable questions. High false positive rates indicate poor calibration and lead to wasted computational resources.
-   **Hallucination rate**: Frequency of invented parameter values or non-existent [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents). This measures the model's tendency to confabulate when faced with uncertainty.

These metrics are typically evaluated on held-out test sets with gold-standard annotations indicating the correct tool sequence for each query. Evaluation should include adversarial examples designed to trick the model into incorrect tool selection or parameter hallucination, ensuring robustness against edge cases.

The interaction between these metrics creates interesting trade-offs. Aggressive training on tool-required examples reduces the false positive rate (the model learns that direct questions should be answered directly), but may reduce schema adherence if the training data lacks sufficient format diversity. Evaluating on all metrics simultaneously and tracking their correlations helps identify which aspects of the training data need reinforcement.

Out\[19\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/function-calling-metrics.png

Function calling evaluation metrics comparing base and fine-tuned models across four key dimensions. Fine-tuning produces substantial improvements in all metrics, with schema adherence rising from 72 to 94 percent and no-hallucination rate improving from 65 to 89 percent. The largest gains appear in the most critical quality dimensions.

## [Link to Structured Output Generation and Schema Enforcement](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#structured-output-generation-and-schema-enforcement) Structured Output Generation and Schema EnforcementLink Copied

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) and [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) generation are closely related but distinct capabilities. Function calling specifically refers to the model emitting a call to a named function with arguments. Structured output generation is the broader capability of emitting text that conforms to any specified schema, which includes function calls but also encompasses JSON objects, XML documents, CSV records, and other structured formats.

Understanding this relationship matters because the same techniques that enable function calling also underlie many other LLM capabilities. When a model generates a structured resume from a job description, or populates a database template from unstructured text, or extracts named entities in a specified JSON format, it is using the same structural generation machinery as function calling, just pointed at different schemas.

### [Link to Token-Level Schema Enforcement](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#token-level-schema-enforcement) Token-Level Schema EnforcementLink Copied

At the token generation level, two broad approaches enforce schema conformance. The first is training-time enforcement, where the fine-tuning data exclusively contains valid schema-conforming examples, and the model learns to generate valid structures probabilistically. The second is inference-time enforcement, where the decoder's [sampling distribution](https://mbrenndoerfer.com/writing/central-limit-theorem-foundation-statistical-inference) is dynamically constrained to only allow tokens that maintain schema validity at each step.

Training-time enforcement is simpler to implement but produces stochastic compliance: the model usually generates valid structures but occasionally produces invalid ones, especially on unusual inputs or when under-specified schemas leave ambiguity. The failure rate depends on the quality and diversity of training data and typically improves with more training.

Inference-time enforcement, as covered in [Constrained Decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output), guarantees syntactic validity by construction. The system maintains a parser state that tracks which tokens are currently valid according to the schema grammar, and sets the [logit](https://mbrenndoerfer.com/writing/logistic-regression-complete-guide-mathematical-foundations-python-implementation) of all invalid tokens to −∞-\\infty−∞ before sampling. This approach is computationally more expensive but eliminates parsing errors entirely. For production systems where unparseable outputs represent hard failures, the overhead is generally worth it.

The trade-off between these approaches also affects the model's reasoning quality. Inference-time constraints can sometimes prevent the model from generating the contextually best argument value if that value happens to violate a syntactic constraint mid-generation. Training-time enforcement, while noisier, allows the model more freedom to express its full linguistic capability and may produce more semantically accurate outputs even if some are syntactically invalid. Hybrid approaches train the model for high baseline compliance and apply selective inference-time constraints only for the most critical schema fields (like function names and required parameters).

### [Link to Structured Output Beyond Function Calling](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#structured-output-beyond-function-calling) Structured Output Beyond Function CallingLink Copied

The same principles that govern [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) apply when you need LLMs to produce structured data in other contexts. Consider information extraction: given a long article about a company's earnings report, you want to extract a structured record with fields for revenue, profit, year-over-year growth, and key executive commentary. You define a JSON schema for the record, provide it to the model alongside the article, and prompt the model to populate the schema.

The schema serves the same roles it does in function calling: it constrains the output space, provides semantic guidance about expected field types, and gives the model a structured template to fill. The difference is that instead of generating a function invocation, the model is generating a data record. The underlying mechanism is identical, which is why models with strong function calling capabilities tend to excel at structured extraction tasks as well.

This generalization suggests a productive mental model: think of JSON schemas not as function call specifications but as output templates that guide what the model generates. Any time you want the model to produce structured information, defining a schema is likely to improve [reliability](https://mbrenndoerfer.com/writing/monitoring-reliability-ai-agents) and consistency. The model has been trained to treat schemas as authoritative specifications of its expected output format.

## [Link to Limitations and Impact](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#limitations-and-impact) Limitations and ImpactLink Copied

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) represents a significant advance in language model capabilities, yet it introduces specific constraints and failure modes that practitioners must navigate. Understanding these limitations is crucial for deploying robust systems and setting appropriate user expectations.

### [Link to Schema Rigidity and Generalization](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#schema-rigidity-and-generalization) Schema Rigidity and GeneralizationLink Copied

Models trained on function calling often struggle with schema variations not seen during fine-tuning. If a training set always presents weather queries with "city, state" format, the model may fail when encountering "city, country" or coordinate-based locations. This brittleness contrasts with the flexibility of natural language, requiring careful prompt engineering or few-shot examples to handle edge cases. The model essentially overfits to the specific parameter patterns in its training data, lacking the compositional generalization that humans exhibit when encountering novel but semantically equivalent inputs.

Furthermore, models may exhibit parameter hallucination when facing ambiguous queries. Given "What's the weather like?" without a specified location, a poorly calibrated model might guess a location rather than ask for clarification. This necessitates robust validation layers that check required parameters before execution and implement retry loops with explicit error feedback. Some systems implement "guardian" models that pre-screen [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) for hallucinated parameters, adding a layer of safety at the cost of additional latency.

The hallucination problem is particularly challenging for string parameters that are not constrained by enums or patterns. A model generating a `customer_id` parameter has no schema-level guardrail preventing it from inventing a plausible-looking but non-existent ID. The only defense is application-layer validation that checks whether the generated ID actually exists in the system before executing the function. This validation step adds latency but prevents silent errors where the model's output looks valid but refers to non-existent entities.

### [Link to Latency and Cost Considerations](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#latency-and-cost-considerations) Latency and Cost ConsiderationsLink Copied

The function calling loop introduces multiple round-trips to the language model: initial call generation, observation injection, and final response generation. Each trip incurs latency and [API costs](https://mbrenndoerfer.com/writing/managing-reducing-ai-agent-costs-optimization-strategies). In high-throughput applications, these costs compound rapidly. A query requiring three tool calls might take three times as long and cost three times as much as a single-turn response.

Parallel [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) mitigates some latency concerns by batching independent operations, but sequential dependencies (where one tool's output is needed for the next call) require serial execution. Planning strategies, which we'll explore in the [ReAct Pattern](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents) chapter, help optimize these dependency chains by allowing the model to reason about tool dependencies before execution. Caching frequent tool results and using smaller, faster models for simple [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) can also reduce costs in production environments.

The cost model for function calling applications also includes the token overhead of schema definitions in the system prompt. For applications with dozens of available tools, the system prompt alone might cost hundreds of tokens per request. At scale, these schema tokens represent a substantial fraction of total [API costs](https://mbrenndoerfer.com/writing/managing-reducing-ai-agent-costs-optimization-strategies). Techniques like schema compression (removing verbose descriptions while preserving essential type information), retrieval-based schema selection (presenting only the most relevant tools per query), and schema caching (reusing parsed schema representations across requests) help manage this overhead.

### [Link to Security Implications](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#security-implications) Security ImplicationsLink Copied

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) creates a direct channel between unconstrained natural language and executable code. This presents significant security risks that must be addressed through defense in depth:

-   **Prompt injection**: Malicious users might craft queries that invoke tools with dangerous arguments. This is analogous to SQL injection in web applications, where user input is executed as code.
-   **Tool confusion**: Attackers may describe tools in ways that trick the model into invoking privileged functions with attacker-controlled parameters. Renaming a sensitive function to resemble a benign one might fool the model into using it inappropriately.
-   **Information leakage**: Tool outputs might contain sensitive data that gets exposed in subsequent generations. A database query tool might return private customer information that the model then reveals to unauthorized parties.

Mitigation strategies include strict input validation against schemas, allowlisting permitted operations, executing tools in sandboxed environments, and implementing [human-in-the-loop](https://mbrenndoerfer.com/writing/ethical-guidelines-human-oversight-ai-agents) confirmation for destructive operations. The principle of [least privilege](https://mbrenndoerfer.com/writing/action-restrictions-and-permissions-ai-agents) should govern tool design: functions should expose minimal capabilities necessary for their specific purpose. Additionally, [output filtering](https://mbrenndoerfer.com/writing/content-safety-and-moderation-ai-agents) can prevent sensitive data from being returned to you, and [rate limiting](https://mbrenndoerfer.com/writing/environment-boundaries-constraints-ai-agents) can prevent abuse of expensive or sensitive tools.

The prompt injection threat is particularly insidious because it can be embedded in tool outputs, not just user inputs. If a web search tool returns a result containing text that resembles instructions, the model might treat this as a legitimate system command. Sanitizing tool outputs to remove instruction-like patterns and maintaining clear separation between data and instructions in the conversation format are important defenses.

### [Link to The Path to Agency](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#the-path-to-agency) The Path to AgencyLink Copied

Despite these limitations, [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) transforms language models from passive responders into active agents capable of affecting the world. By providing a structured interface to external capabilities, it enables the construction of complex workflows where models plan, execute, observe, and adapt. This capability represents the foundation of autonomous [agent architectures](https://mbrenndoerfer.com/writing/agent-architectures-loop-state-planning-termination), where the LLM serves as the reasoning engine coordinating multiple tools to achieve high-level goals.

This capability unlocks applications ranging from automated research assistants that query databases and calculate statistics to customer service bots that modify orders and check shipping status. As we move toward more sophisticated agent architectures in subsequent chapters, function calling serves as the basic building block, the "motor cortex" that translates high-level intentions into concrete actions. The [ReAct Pattern](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents) builds directly on this foundation, adding explicit reasoning steps between observations and actions to create more robust, traceable agent behaviors. Understanding [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) is therefore essential for anyone building the next generation of AI applications that interact with the real world.

## [Link to Summary](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#summary) SummaryLink Copied

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) enables language models to bridge the gap between natural language understanding and actionable computation. By defining tool schemas in JSON format, models learn to emit structured function calls with appropriate parameters, execute external code safely, and synthesize results into coherent responses. This capability transforms static text generators into dynamic agents capable of retrieving information, performing calculations, and interacting with external systems.

Key takeaways include:

-   **Schema definition** uses JSON Schema to specify function interfaces, parameter types, and constraints, providing the model with the metadata necessary to generate valid calls. Well-designed schemas act as both technical specifications and semantic guides, helping the model understand when and how to use each tool.
-   **Call generation** leverages supervised fine-tuning on tool-use corpora, teaching models to recognize when external data is required and how to format requests appropriately. This training instills tool awareness and the ability to map natural language queries to structured parameters.
-   **Execution loops** follow an observe-act pattern where function results are injected back into the [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp) as observations, enabling multi-step reasoning. This cycle allows models to react to real-world data and correct course based on external feedback.
-   **Fine-tuning** requires carefully curated conversation datasets that demonstrate proper [tool selection](https://mbrenndoerfer.com/writing/tool-selection-llm-agents-routing-strategies), [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents), and natural language synthesis from structured data. Success requires attention to format consistency, diverse examples, and proper [evaluation metrics](https://mbrenndoerfer.com/writing/benchmark-saturation-ai-evaluation-metrics).
-   **Practical deployment** demands attention to [error handling](https://mbrenndoerfer.com/writing/plan-and-execute-ai-agents), security validation, [latency optimization](https://mbrenndoerfer.com/writing/speeding-up-ai-agents-performance-optimization), and context window management. Production systems must guard against injection attacks, handle API failures gracefully, and manage the computational costs of multi-turn interactions.

As the interface between language models and the digital world, [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) represents the key primitive upon which [autonomous agents](https://mbrenndoerfer.com/writing/agentic-ai-systems-autonomous-agents-reasoning-planning-tool-use) are constructed. Mastering its mechanics, both the mathematical foundations of [structured generation](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) and the engineering challenges of safe execution, prepares practitioners to build systems that move beyond text generation into purposeful action. The skills developed here, designing schemas, managing execution loops, and handling edge cases, form the bedrock of modern AI application development.

## [Link to Quiz](https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools\#quiz) QuizLink Copied

Ready to test your understanding? Take this quick quiz to [reinforce](https://mbrenndoerfer.com/writing/policy-gradient-methods-reinforce-algorithm) what you've learned about [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) in large language models.

### Function Calling Fundamentals

Question 1 of 70 of 7 completed

What is the primary purpose of the 'required' field in a function schema?

To specify which parameters are optional

To list parameters that must be provided for valid function calls

To define the return type of the function

To indicate deprecated parameters

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="mastering-llm-tool-calling-the-complete-framework-for-connec.md">
<details>
<summary>Mastering LLM Tool Calling: The Complete Framework for Connecting Models to the Real World - MachineLearningMastery.com</summary>

Phase: [EXPLORATION]

**Source URL:** <https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/>

# Mastering LLM Tool Calling: The Complete Framework for Connecting Models to the Real World - MachineLearningMastery.com

In this article, you will learn a practical, three-pillar framework for connecting large language models to external tools so your agents can read data, compute on it, and take real actions.

Topics we will cover include:

- What tool calling is and why it turns chatbots into capable agents
- How data access, computation, and action tools map to real production workflows
- Operational concerns such as security, HITL, error handling, and monitoring

On we go.

https://machinelearningmastery.com/wp-content/uploads/2026/01/mlm-chugani-llm-tool-calling-framework-connecting-models-real-world-feature-2.jpg

Mastering LLM Tool Calling: The Complete Framework for Connecting Models to the Real World

Image by Author

## What Tool Calling Is and Why It Matters

Most ChatGPT users don’t know this, but when the model searches the web for current information or runs Python code to analyze data, it’s using tool calling. You just don’t see it happening behind the scenes.

Tool calling is the mechanism that lets large language models invoke external functions and APIs. It bridges the gap between language generation and real-world actions. Without tools, an LLM is limited to what it learned during training. With tools, it can access current data, take actions, and integrate with your systems.

There’s a key difference between pre-built systems and custom agents. ChatGPT comes with pre-installed tools you can’t modify or customize. When you build your own agents, you decide which tools to connect. Want your agent to query your company’s database? Add a SQL tool. Need it to send Slack messages? Connect the Slack API. This flexibility makes custom agents useful.

The workflow looks like this in practice. When a user makes a request, the LLM first recognizes it needs a tool. Then it selects which tool to use from its available options. Next, it executes that tool with the right parameters. Finally, it integrates the results back into its response. The whole process happens in seconds, but understanding these steps helps you debug when things go wrong.

https://machinelearningmastery.com/wp-content/uploads/2026/01/mlm-chugani-mastering-llm-tool-1.jpg

Why does this matter for you as a developer? Because the difference between a chatbot that just talks and an agent that does things comes down to tool calling. RAG systems, autonomous workflows, and data analysis agents all rely on this core mechanism.

## The Three-Pillar Framework: Data Access, Computation, and Actions

When you’re building an agent, you need a mental framework for organizing tools. Every tool falls into one of three categories based on what it does: data access, computation, or actions.

### Pillar 1: Data Access Tools (Read-Only)

These tools retrieve information from external sources. They’re read-only, which means they’re safe to call repeatedly without side effects.

RAG fits in this framework like this: RAG is just tool calling. When your agent does RAG, it’s calling a [vector database](https://machinelearningmastery.com/the-complete-guide-to-vector-databases-for-machine-learning/) search tool. This helps clarify how RAG relates to broader agentic systems. It’s one tool type among many.

**Vector databases** handle semantic search. Use these when you’re searching unstructured content or need conceptual matches rather than exact keywords. A user asking “find documents about our Q3 strategy” benefits from vector search because it can match intent, not just keywords.

**SQL and NoSQL databases** handle structured queries. When you need transactional data, customer records, or anything with defined schemas, these are your go-to tools. They’re fast, reliable, and work well for precise lookups.

**Graph databases** excel at relationships. If your data involves connections (like social networks, knowledge graphs, or organizational hierarchies), graph databases let you traverse these relationships efficiently.

**External APIs** bring in third-party data. Weather services, stock prices, and news feeds. Anything that changes frequently and lives outside your systems needs an API tool.

**File systems** provide document access. Sometimes you just need to read files from storage. This comes up more often than you’d think, especially when dealing with reports, contracts, or reference materials.

When do you use each? Vector databases work well for unstructured or conceptual queries. SQL works best for transactional data where you know exactly what you’re looking for. Graph databases are your friend when relationships matter as much as the data itself. APIs handle real-time external data that you don’t control.

### Pillar 2: Computation Tools (Process & Transform)

Data rarely comes back in the exact format you need. Computation tools analyze, calculate, and transform information between gathering and acting.

**Code execution** tools (Python, JavaScript) let your agent run calculations, process data, or apply complex logic. This is useful when you need custom transformations that no existing API provides.

**Mathematical operations** tools like **[Wolfram Alpha](https://www.wolframalpha.com/)** handle advanced math, symbolic computation, or scientific calculations. If your agent needs to solve equations or perform statistical analysis, these tools save you from reinventing the wheel.

**Data transformation** tools (ETL, parsing) convert data between formats. You’ll use these constantly: CSV to JSON, XML parsing, data cleaning, and format standardization.

**ML model inference** brings in specialized capabilities. Need image recognition, sentiment analysis, or classification? These tools let your main LLM work with other AI models as needed.

**Media processing** tools manipulate images, videos, or audio. Resizing images, extracting frames, and audio transcription. These tasks require specialized processing that computation tools provide.

Why does computation matter? Because data often needs processing before it’s useful for decision-making. You might retrieve sales data but need to calculate growth rates before determining next steps. You might fetch customer feedback but need sentiment analysis before crafting a response. Actions often require calculations first.

### Pillar 3: Action Tools (Write/Execute)

Actions change state. They communicate externally, modify data, or trigger workflows. This is where things get real (and risky).

**Communication tools** send emails, Slack messages, SMS, or other notifications. These are common in customer service agents, alert systems, and collaboration tools.

**Workflow automation** tools create tickets, trigger pipelines, or kick off multi-step processes. Think Jira ticket creation, CI/CD pipeline triggers, or approval workflows.

**Data manipulation** tools update databases, modify records, or delete information. These require extra caution since they change your data state.

**External service integrations** handle payment processing, CRM operations, or other business-critical functions. These tools often have real financial or operational consequences.

The critical point about actions: they have consequences. An email sent can’t be unsent. A payment processed can’t be easily reversed. A database record deleted might be gone forever. This is why actions require different safety considerations than data access or computation. Common patterns you’ll see with actions include read-before-write (always verify state before changing it), conditional actions (only execute if certain conditions are met), and chained actions (multiple steps that must succeed together).

## How the Three Pillars Work Together in Production

A real example: an autonomous customer service agent handling a delayed shipment complaint.

A customer contacts support saying their order is late and they want help. The three pillars work together like this.

**Data Access phase:** The agent first searches the knowledge base using vector search to find the refund policy. It queries the order database with SQL to get shipment details. Then it calls the shipping carrier’s API to check current tracking status. All of this is gathering context.

**Computation phase:** Now the agent calculates how many days the shipment is delayed. It evaluates refund eligibility based on the policy it found earlier. It determines the refund amount using the order value and any applicable rules. This transforms raw data into actionable insights.

**Actions phase:** The agent processes the refund through your payment provider. It sends a confirmation email to the customer. It updates your CRM with notes about what happened. Finally, it creates an internal ticket for the logistics team to investigate why the shipment was delayed.

https://machinelearningmastery.com/wp-content/uploads/2026/01/mlm-chugani-mastering-llm-tool-3.jpg

Notice the workflow isn’t strictly linear. After processing the refund, the agent might loop back to Data Access to verify the refund went through. Then it takes another Action to send the confirmation. This iterative pattern is common in production systems.

Each pillar depends on the others for complete autonomous execution. Data Access alone gives you an agent that can inform but can’t act. Actions alone give you an agent operating blindly without context. But combine all three? Now you’ve got a system that can gather information, make decisions, and execute tasks.

When designing your agent, ask yourself: does it have balanced capabilities across all three pillars? An agent with strong Data Access but weak Actions can answer questions but can’t help solve problems. An agent with strong Actions but weak Computation might take the wrong actions based on unprocessed data.

## Tool Calling vs. Model Context Protocol (MCP)

There’s confusion about how MCP relates to tool calling, so here’s the distinction.

Tool calling is the **mechanism** (how agents invoke functions). MCP is a **protocol** (a standardized way to connect to tools). Tool calling is making phone calls, and MCP is the phone system’s standard for how calls should work.

When should you use MCP? If you’re building multiple integrations that need standardization, MCP saves you from reinventing connection logic each time. If you want to avoid writing custom code for each data source, MCP provides consistent interfaces. When building tools that multiple agents will use, MCP makes them reusable. In enterprise environments with many data sources, MCP brings order to potential chaos.

When should you skip MCP? For simple applications with just one or two tools, the overhead isn’t worth it. If you need ultra-low latency, MCP adds some overhead you might not want. Sometimes direct API calls are cleaner for your specific use case.

MCP is one way to implement tool calling. The three-pillar taxonomy we covered applies regardless of how you connect to tools (whether you’re using direct API calls, LangChain tools, framework integrations, or MCP). The framework is connection-agnostic.

## Advanced Considerations for Production Agents

Building a demo agent is one thing. Running it in production is another. Here’s what you need to think about.

### Security & Authorization

Every tool needs proper authentication. Use API keys, OAuth, or service accounts depending on what the tool requires. Follow the principle of least privilege. Give your agent only the minimum permissions necessary to do its job. This limits damage if something goes wrong.

Store credentials securely. Don’t hardcode API keys. Use environment variables or secret management systems. Rotate credentials periodically even if you haven’t detected any breaches.

### Human-in-the-Loop (HITL)

Not all actions should be fully autonomous. Some operations are too high-stakes to run without human approval.

Require approval for financial transactions above a certain threshold. Make data deletion operations require confirmation. Keep external communications (especially customer-facing ones) under review until you’re confident in the agent’s judgment.

The goal isn’t to eliminate automation. It’s to balance automation benefits with risk management. Start with more human oversight, then gradually reduce it as you build confidence.

### Error Handling & Resilience

Tools fail. APIs go down. Rate limits get hit. Timeouts happen. Your agent needs to handle these gracefully.

Implement retry logic with exponential backoff. If a tool fails, wait a bit, then try again. Don’t hammer a struggling service with repeated immediate requests.

Have fallback tools when possible. If your primary weather API is down, can you use a secondary one? If vector search times out, can you fall back to keyword search?

Design for graceful degradation. When a tool fails, what’s the best partial result you can provide? Clear error messages help users understand what went wrong and what they can do about it.

### Monitoring & Observability

Track which tools get called, when they’re called, and whether they succeed or fail. This data is invaluable for debugging and optimization.

Monitor performance metrics: latency, API costs, and bottlenecks. Tools that are slow or expensive might need alternatives or caching strategies.

Set up alerts for unusual patterns. If an action tool that normally runs 10 times per day suddenly runs 1,000 times, something’s probably wrong.

### Tool Selection Strategy

Start simple. Give your agent 3–5 essential tools to begin with. Too many tools confuse the agent. It has a harder time selecting the right one.

Add tools gradually based on observed needs. If you notice the agent struggling with a particular task type, that’s when to add a tool. Don’t try to anticipate every possible need upfront.

Balance the pillars. Don’t load up on Data Access tools while neglecting Computation and Actions. A well-rounded agent needs all three capabilities.

## Next Steps

Apply this framework to your own projects.

Audit your current agent for missing pillars. Does it have strong Data Access but weak Actions? Can it gather information but not process it effectively?

Identify high-value tools to add based on what tasks your agent struggles with. Look at failed interactions or workarounds users have to perform manually.

Implement human-in-the-loop for consequential actions. Start conservative and loosen restrictions as you gain confidence.

Monitor and iterate. Use your observability data to guide improvements. The best agent architecture emerges through testing and refinement, not upfront perfect design.

Tool calling transforms large language models from language models into capable agents. The three-pillar framework (Data Access, Computation, and Actions) gives you a mental model for building balanced, production-ready systems. Start simple, monitor closely, and expand capabilities based on real needs.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-evolution-of-tool-use-in-llm-agents-from-single-tool-cal.md">
<details>
<summary>The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2603.22862v2>

Title:

Content selection saved. Describe the issue below:

Description:

[License: arXiv.org perpetual non-exclusive license](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2603.22862v2 \[cs.SE\] 02 Apr 2026

# The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

Haoyuan Xu
[hyxu@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:hyxu@ir.hit.edu.cn), Chang Li
[cli@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:cli@ir.hit.edu.cn)Harbin Institute of TechnologyHarbinHeilongjiangChina150001, Xinyan Ma
[xyma@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:xyma@ir.hit.edu.cn), Xianhao Ou
[25S103427@hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:25S103427@hit.edu.cn)Harbin Institute of TechnologyHarbinHeilongjiangChina150001, Zihan Zhang
[Zihan˙zhang@hsph.harvard.edu](https://arxiv.org/html/2603.22862v2/mailto:Zihan%CB%99zhang@hsph.harvard.edu)Harvard UniversityCambridgeMAUSA02138, Tao He
[the@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:the@ir.hit.edu.cn), Xiangyu Liu
[2022112441@stu.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:2022112441@stu.hit.edu.cn), Zixiang Wang
[2022112865@stu.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:2022112865@stu.hit.edu.cn)Harbin Institute of TechnologyHarbinHeilongjiangChina150001, Jiafeng Liang
[jfliang@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:jfliang@ir.hit.edu.cn), Zheng Chu
[zchu@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:zchu@ir.hit.edu.cn), Runxuan Liu
[rxliu@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:rxliu@ir.hit.edu.cn), Rongchuan Mu
[rcmu@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:rcmu@ir.hit.edu.cn)Harbin Institute of TechnologyHarbinHeilongjiangChina150001, Dandan Tu
[tudandan@huawei.com](https://arxiv.org/html/2603.22862v2/mailto:tudandan@huawei.com)Huawei Technologies Co., Ltd.China, Ming Liu
[mliu@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:mliu@ir.hit.edu.cn) and Bing Qin
[qinb@ir.hit.edu.cn](https://arxiv.org/html/2603.22862v2/mailto:qinb@ir.hit.edu.cn)Harbin Institute of TechnologyHarbinHeilongjiangChina150001

(2026)

###### Abstract.

Tool use enables large language models (LLMs) to access external information, invoke software systems, and act in digital environments beyond what can be solved from model parameters alone. Early research mainly studied whether a model could select and execute a correct single tool call. As agent systems evolve, however, the central problem has shifted from isolated invocation to multi-tool orchestration over long trajectories with intermediate state, execution feedback, changing environments, and practical constraints such as safety, cost, and verifiability. We comprehensively review recent progress in multi-tool LLM agents and analyze the state of the art in this rapidly developing area. First, we unify task formulations and distinguish single-call tool use from long-horizon orchestration. Then, we organize the literature around six core dimensions: inference-time planning and execution, training and trajectory construction, safety and control, efficiency under resource constraints, capability completeness in open environments, and benchmark design and evaluation. We further summarize representative applications in software engineering, enterprise workflows, graphical user interfaces, and mobile systems. Finally, we discuss major challenges and outline future directions for building reliable, scalable, and verifiable multi-tool agents.

††copyright: acmlicensed††journalyear: 2026††doi: XXXXXXX.XXXXXXX††conference: Make sure to enter the correct
conference title from your rights confirmation email; June 03–05,
2018; Woodstock, NY

## 1\. Introduction

While Large Language Models (LLMs) have demonstrated exceptional reasoning and generation capabilities in natural language processing ( [119](https://arxiv.org/html/2603.22862v2#bib.bib1 "Large language models: a survey")), their ability to solve complex real-world problems remains constrained by static parametric knowledge, potential hallucination risks, and a lack of interaction with physical or digital environments. Tool learning addresses these limitations by enabling models to invoke external APIs (e.g., search engines, code interpreters), establishing a perception-action loop. Early works such as TALM ( [129](https://arxiv.org/html/2603.22862v2#bib.bib2 "Talm: tool augmented language models")), MRKL ( [74](https://arxiv.org/html/2603.22862v2#bib.bib3 "MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning")), Toolformer ( [143](https://arxiv.org/html/2603.22862v2#bib.bib4 "Toolformer: language models can teach themselves to use tools")), and ReAct ( [204](https://arxiv.org/html/2603.22862v2#bib.bib20 "React: synergizing reasoning and acting in language models")) laid the foundation for this field by teaching models to recognize single intents and correctly format API requests, effectively internalizing tool usage as an extended language capability.

As task complexity escalates, the linear application of single tools becomes insufficient for real-world challenges. Multi-tool utilization represents an independent research problem that intersects with combinatorial optimization ( [101](https://arxiv.org/html/2603.22862v2#bib.bib5 "A systematic survey on large language models for algorithm design")), programmatic semantic constraints, and system scheduling ( [62](https://arxiv.org/html/2603.22862v2#bib.bib6 "Semantic scheduling for llm inference")). The decision space for an autonomous agent undergoes a qualitative shift from simple binary tool selection to solving a series of coupled decisions within a single task. This process includes dynamic tool subset selection, cross-tool dependency modeling, sequential and parallel scheduling, failure recovery, and re-planning. When tool usage extends to long-horizon chains involving state-mutating write operations, maintaining state consistency and managing race conditions under parallel execution emerge as core bottlenecks for system stability.

The primary research objective in this domain has thus transitioned from the correctness of single-point calls to the end-to-end executability and robustness of multi-tool chains in complex environments. We begin by reviewing inference-time reasoning paradigms and architectures, highlighting the transition from serial chain reasoning to structured graph-based execution, alongside dual-system architectures designed to balance long-horizon planning complexity with execution efficiency. We then explore data synthesis and training paradigms, focusing on trajectory synthesis and closed-loop verification methods that address the combinatorial space of multi-tool usage and long-tail dependencies. Furthermore, we analyze safety and robustness, particularly concerning state safety under parallel execution, context drift in extended chains ( [142](https://arxiv.org/html/2603.22862v2#bib.bib9 "Agent drift: quantifying behavioral degradation in multi-agent llm systems over extended interactions")), and mitigation strategies for privacy risks. The discussion also encompasses operational efficiency, evaluating end-to-end agent latency, tool invocation costs, and inference budgets ( [126](https://arxiv.org/html/2603.22862v2#bib.bib10 "Routellm: learning to route llms with preference data")). To address system completeness, we review adaptive strategies for incomplete environments where tools or information may be missing. Finally, we trace the evolution of benchmark evaluation standards from single-point functional verification to system-level topological orchestration and interactive closed-loops. Based on these existing challenges, we propose a future research agenda to provide theoretical references and technical pathways for building reliable, efficient, and scalable multi-tool agent systems.

### 1.1. Aims and Motivations

Research on tool-augmented LLMs began with a relatively simple question: can a model select an appropriate tool and produce a valid call? That abstraction is no longer sufficient for agent systems. Many practical tasks require an agent to coordinate multiple tools over long trajectories, preserve intermediate state, recover from failures, and operate under constraints on latency, cost, and safety. In these settings, a key challenge lies not only in tool access, but also in orchestration.

This survey is motivated by two gaps in the current literature. The first is conceptual: terms such as tool use, tool calling, tool retrieval, workflow execution, and orchestration are often used loosely, even though they refer to different capability levels. The second is structural: planning, training, safety, efficiency, benchmarking, and open-environment adaptation are often studied separately, while deployed agent systems depend on their interaction.

### 1.2. Related Work

A growing body of survey work has examined tool use in large language models and related agent topics, yet long-horizon multi-tool orchestration has less often been treated as a primary problem in its own right. Wang et al. ( [177](https://arxiv.org/html/2603.22862v2#bib.bib11 "What are tools anyway? a survey from the language model perspective")) considered what should count as a tool from the perspective of language models and offered a unified view of external tools. Qu et al. ( [140](https://arxiv.org/html/2603.22862v2#bib.bib12 "Tool learning with large language models: a survey")) surveyed tool learning in LLMs, covering planning, tool selection, tool calling, and response generation. Shen ( [152](https://arxiv.org/html/2603.22862v2#bib.bib13 "Llm with tools: a survey")) reviewed LLM tool use with attention to tool integration, training methods, and the shift from tool use to tool creation. Li ( [89](https://arxiv.org/html/2603.22862v2#bib.bib14 "A review of prominent paradigms for llm-based agents: tool use, planning (including rag), and feedback learning")) summarized major paradigms of LLM-based agents, including tool use, planning, and feedback learning. Luo et al. ( [114](https://arxiv.org/html/2603.22862v2#bib.bib15 "Large language model agent: a survey on methodology, applications and challenges")) provided a broader review of LLM agents spanning methodology, applications, and challenges. Chen et al. ( [23](https://arxiv.org/html/2603.22862v2#bib.bib16 "A survey on llm-based multi-agent system: recent advances and new frontiers in application")) focused on LLM-based multi-agent systems rather than multi-tool orchestration within a single agent. He et al. ( [53](https://arxiv.org/html/2603.22862v2#bib.bib17 "The emerged security and privacy of llm agent: a survey with case studies")) surveyed security and privacy risks in LLM agents. Mohammadi et al. ( [122](https://arxiv.org/html/2603.22862v2#bib.bib18 "Evaluation and benchmarking of llm agents: a survey")) reviewed the evaluation and benchmarking of LLM agents.

Our survey differs from this literature in several ways. It takes multi-tool orchestration, rather than tool use in general or agent systems more broadly, as the main unit of analysis. It also organizes the field around six connected dimensions: inference, training and trajectory construction, safety and control, efficiency, capability completeness, and evaluation. In addition, it draws clearer boundaries among concepts that are often conflated in prior work, including tool invocation, tool retrieval, orchestration, and toolset expansion. Finally, it relates methodological progress to the recent shift from call-level correctness to system-level reliability in both benchmarks and applications.

![Refer to caption](https://arxiv.org/html/2603.22862v2/x1.png)

Figure 1. Paradigm Shift in LLM Tool Use: From Single-Tool Call to Multi-Tool Orchestration

{forest}

Figure 2. The main structure of this paper.

## 2\. Problem formulation

Notation.
A multi-tool learning instance contains:
(i) a query/task q∈𝒬q\\in\\mathcal{Q};
(ii) an interactive environment with latent state st∈𝒮s\_{t}\\in\\mathcal{S} and observation ot∈𝒪o\_{t}\\in\\mathcal{O} at step tt;
(iii) a tool inventory 𝒟={di}i=1N\\mathcal{D}=\\{d\_{i}\\}\_{i=1}^{N}, where each tool dd is described by a schema/signature Σd\\Sigma\_{d}
(e.g., name, description, constraints, return format).
A tool execution interface is

|     |     |     |
| --- | --- | --- |
|  | Exec​(d,u;s)→(f,s′),\\textsc{Exec}(d,u;s)\\rightarrow(f,s^{\\prime}), |  |

where u∈𝒰du\\in\\mathcal{U}\_{d} is a valid argument/parameter object for tool dd,
f∈ℱf\\in\\mathcal{F} is tool feedback (e.g., JSON/text/error code),
and s′∈𝒮s^{\\prime}\\in\\mathcal{S} is the post-call environment state .
Let πθ\\pi\_{\\theta} denote the model/policy with parameters θ\\theta.
Let τ\\tau denote a tool-use trajectory (defined below), and Cost​(τ)\\text{Cost}(\\tau) any cost functional
(number of calls, latency, API fees, risk, etc.).

We define the interaction history up to time tt as

|     |     |     |
| --- | --- | --- |
|  | ht:=(q,o0,a0,f0,o1,a1,f1,…,ot),h\_{t}:=(q,o\_{0},a\_{0},f\_{0},o\_{1},a\_{1},f\_{1},\\ldots,o\_{t}), |  |

where aka\_{k} is the action taken at step kk and fkf\_{k} is the feedback returned by Exec.
Let mtm\_{t} denote the model’s internal memory/state at step tt (e.g., a scratchpad summary or retrieved records),
which can be updated as a function of (mt−1,ht)(m\_{t-1},h\_{t}).

Multi-tool orchestration.
At each step tt, the model selects an action

|     |     |     |
| --- | --- | --- |
|  | at∈𝒜:=(𝒟×𝒰)∪{Finish​(y)},a\_{t}\\in\\mathcal{A}:=\\big(\\mathcal{D}\\times\\mathcal{U}\\big)\ \\cup\ \\{\\textsc{Finish}(y)\\}, |  |

where a tool-call action is at=(dt,ut)a\_{t}=(d\_{t},u\_{t}) with dt∈𝒟d\_{t}\\in\\mathcal{D} and ut∈𝒰dtu\_{t}\\in\\mathcal{U}\_{d\_{t}},
and Finish​(y)\\textsc{Finish}(y) terminates with final answer y∈𝒴y\\in\\mathcal{Y}.
The policy acts conditioned on history and memory:

|     |     |     |
| --- | --- | --- |
|  | at∼πθ(⋅∣ht,mt).a\_{t}\\sim\\pi\_{\\theta}(\\cdot\\mid h\_{t},m\_{t}). |  |

If at=(dt,ut)a\_{t}=(d\_{t},u\_{t}), the environment returns feedback and transitions:

|     |     |     |
| --- | --- | --- |
|  | (ft,st+1)←Exec​(dt,ut;st),ht+1=ht⊕(at,ft,ot+1),(f\_{t},s\_{t+1})\\leftarrow\\textsc{Exec}(d\_{t},u\_{t};s\_{t}),\\qquad h\_{t+1}=h\_{t}\\oplus(a\_{t},f\_{t},o\_{t+1}), |  |

where ⊕\\oplus appends new interaction records and ot+1o\_{t+1} is the next observation derived from st+1s\_{t+1}.
A trajectory is

|     |     |     |
| --- | --- | --- |
|  | τ:=((a0,f0),(a1,f1),…,(aT−1,fT−1),Finish​(y)),\\tau:=\\big((a\_{0},f\_{0}),(a\_{1},f\_{1}),\\ldots,(a\_{T-1},f\_{T-1}),\\textsc{Finish}(y)\\big), |  |

with variable horizon TT.
A generic cost-aware objective is

|     |     |     |
| --- | --- | --- |
|  | maxθ⁡𝔼​\[Rtask​(q,τ,y)−λ⋅Cost​(τ)\],\\max\_{\\theta}\\;\\mathbb{E}\\Big\[R\_{\\text{task}}(q,\\tau,y)-\\lambda\\cdot\\text{Cost}(\\tau)\\Big\], |  |

where λ≥0\\lambda\\geq 0 trades off success vs cost.
This captures long-horizon scheduling, failure recovery, and re-planning under tool/environment feedback.

## 3\. Multi-Tool Agent Inference-Time Paradigms

Multi-tool calling constitutes a fundamental shift in agent planning and reasoning. As the tool space expands to encompass thousands of APIs and non-linear dependencies, traditional autoregressive generation models struggle with context limits and cascading errors. This shift motivates a substantial rethinking of agent inference-time paradigms. Recent research focuses on task topological planning, explicit search algorithms, reflection and self-improvement, and system-level orchestration with persistent memory. This section systematically reviews representative works along these key areas.

### 3.1. Topological Planning

Traditional paradigms such as ReAct ( [204](https://arxiv.org/html/2603.22862v2#bib.bib20 "React: synergizing reasoning and acting in language models")) organize tool usage into sequential traces. This structure implicitly assumes that tasks are linearly decomposable. While highly effective for simple single-step retrievals, this linear approach exhibits severe structural mismatches when applied to nested calls, parallel I/O operations, or long-horizon goals. Linear constraints inherently limit the representation of data flow dependencies, preclude the parallel execution of independent operations, and force early decision errors to accumulate throughout the trajectory. Consequently, the field has rapidly moved toward topology-aware planning that utilizes structures with significantly higher expressive power.

As tool spaces expand into the tens of thousands, the primary challenge shifts from binary selection to dependence-aware combinatorial decision-making. One line of work represents tool use as an explicit dependency structure, allowing the agent to reason over asynchronous or partially parallelizable subproblems ( [97](https://arxiv.org/html/2603.22862v2#bib.bib21 "Graph-enhanced large language models in asynchronous plan reasoning"); [183](https://arxiv.org/html/2603.22862v2#bib.bib22 "GAP: graph-based agent planning with parallel tool use and reinforcement learning")). Related systems such as ToolNet and StructuredAgent encode reusable transition structure through directed graphs or AND/OR decompositions, reducing the effective search space while preserving non-linear task dependencies ( [104](https://arxiv.org/html/2603.22862v2#bib.bib23 "Toolnet: connecting large language models with massive tools via tool graph"); [106](https://arxiv.org/html/2603.22862v2#bib.bib24 "STRUCTUREDAGENT: planning with and/or trees for long-horizon web tasks")). AutoTool further shows that historical regularities in tool transitions can be used to bypass unnecessary inference for predictable parts of the workflow ( [70](https://arxiv.org/html/2603.22862v2#bib.bib25 "AutoTool: efficient tool selection for large language model agents")). Taken together, these approaches treat tool use as graph-structured execution rather than a flat token sequence.

To address goal drift in long-horizon tasks, monolithic planning algorithms are increasingly being replaced by hierarchical delegation. HIPLAN proposes a bi-level architecture where an upper-level planner generates a macroscopic milestone space, leaving a lower-level executor to resolve specific state gaps ( [93](https://arxiv.org/html/2603.22862v2#bib.bib19 "Hiplan: hierarchical planning for llm-based agents with adaptive global-local guidance")). ADaPT introduces a recursive representation that defaults to flat execution, invoking high-level graph decomposition only upon encountering localized failures ( [132](https://arxiv.org/html/2603.22862v2#bib.bib27 "Adapt: as-needed decomposition and planning with language models")). Pushing abstraction further, AFlow represents the reasoning process as executable node configurations and control flow edges ( [217](https://arxiv.org/html/2603.22862v2#bib.bib26 "Aflow: automating agentic workflow generation")). Dynamic planners like D-PoT ( [220](https://arxiv.org/html/2603.22862v2#bib.bib28 "Dynamic planning for llm-based graphical user interface automation")), DyFlow ( [174](https://arxiv.org/html/2603.22862v2#bib.bib29 "DyFlow: dynamic workflow framework for agentic reasoning")), and ReCAP ( [225](https://arxiv.org/html/2603.22862v2#bib.bib30 "ReCAP: recursive context-aware reasoning and planning for large language model agents")) further allow real-time subgoal reorganization.

As autoregressive decoding is inherently short-sighted, recent methods cast multi-step tool execution as a state-space search problem. Traditional tree search often suffers from context contamination in language domains. Smurfs introduces context-efficient rollback and branch isolation, reducing contamination from failed trajectories ( [20](https://arxiv.org/html/2603.22862v2#bib.bib31 "Smurfs: multi-agent system using context-efficient dfsdt for tool planning")). AB-MCTS explores adaptive branching under external feedback, while ARTIS separates exploration from commitment through an internal simulator for high-risk actions ( [67](https://arxiv.org/html/2603.22862v2#bib.bib32 "Wider or deeper? scaling llm inference-time compute with adaptive branching tree search"); [213](https://arxiv.org/html/2603.22862v2#bib.bib33 "ARTIS: agentic risk-aware test-time scaling via iterative simulation")). Closely related approaches, including Plan-and-Act, MPO, and AgentPro, also separate abstract planning from execution or use learned evaluators to prune low-quality branches during inference ( [37](https://arxiv.org/html/2603.22862v2#bib.bib34 "Plan-and-act: improving planning of agents for long-horizon tasks"); [190](https://arxiv.org/html/2603.22862v2#bib.bib35 "Mpo: boosting llm agents with meta plan optimization"); [29](https://arxiv.org/html/2603.22862v2#bib.bib36 "AgentPro: enhancing llm agents with automated process supervision")). These methods reflect a broader shift from ”generate once and execute” to ”search, verify, and then commit”.

### 3.2. Long-Horizon Orchestration

When task complexity exceeds the cognitive limitations of a single model, reasoning shifts to system-level architecture. This axis emphasizes cognitive division of labor, standardized semantic routing, and long-term dynamic memory to ensure robust performance across open-ended environments.

Inspired by dual-process reasoning, MARS separates fast parsing of large tool outputs from slower deliberative reasoning ( [19](https://arxiv.org/html/2603.22862v2#bib.bib37 "MARS: co-evolving dual-system deep research via multi-agent reinforcement learning")). In domains with strict execution requirements, CodeTool introduces structured intermediate representations that make progress easier to verify ( [110](https://arxiv.org/html/2603.22862v2#bib.bib38 "Codetool: enhancing programmatic tool invocation of llms via process supervision")). Other systems externalize durable skills or workflows into procedural memory. DeepAgent integrates tool discovery into a continuous reasoning stream ( [87](https://arxiv.org/html/2603.22862v2#bib.bib39 "Deepagent: a general reasoning agent with scalable toolsets")), while MACLA and HiAgent explicitly maintain reusable procedural abstractions across long tasks and repeated sessions ( [42](https://arxiv.org/html/2603.22862v2#bib.bib40 "Learning hierarchical procedural memory for llm agents through bayesian selection and contrastive refinement"); [60](https://arxiv.org/html/2603.22862v2#bib.bib41 "Hiagent: hierarchical working memory management for solving long-horizon agent tasks with large language model")). The common goal is to avoid placing the full burden of orchestration inside a single transient context window.

A related challenge is dynamic scheduling over large tool ecosystems. Early frameworks such as HuggingGPT illustrated the value of centralized planning and semantic routing across heterogeneous expert models ( [149](https://arxiv.org/html/2603.22862v2#bib.bib42 "Hugginggpt: solving ai tasks with chatgpt and its friends in hugging face")). Subsequent work showed that decomposing the workflow into planner, caller, and summarizer roles can allow smaller models to compete effectively with larger monolithic agents ( [148](https://arxiv.org/html/2603.22862v2#bib.bib43 "Small llms are weak tool learners: a multi-llm agent")). As tool access becomes more standardized, schedulers such as Gradientsys coordinate multiple specialized executors under capacity and observability constraints ( [155](https://arxiv.org/html/2603.22862v2#bib.bib44 "Gradientsys: a multi-agent llm scheduler with react orchestration")). Tool-to-Agent Retrieval extends this idea by jointly indexing tools and their parent agents, preserving both invocation granularity and execution context during retrieval ( [112](https://arxiv.org/html/2603.22862v2#bib.bib45 "Tool-to-agent retrieval: bridging tools and agents for scalable llm multi-agent systems")). These systems suggest that long-horizon competence depends not only on reasoning quality, but also on how execution responsibilities are routed and monitored.

Memory is the third core component of long-horizon orchestration. Raw trajectories are too large and noisy to remain fully useful over extended interaction, so practical systems compress, structure, or externalize execution history. COMPASS and Acon summarize completed subtasks into compact progress representations to maintain alignment with the global objective ( [162](https://arxiv.org/html/2603.22862v2#bib.bib46 "Compass: enhancing agent long-horizon reasoning with evolving context"); [73](https://arxiv.org/html/2603.22862v2#bib.bib47 "Acon: optimizing context compression for long-horizon llm agents")). Other approaches use graph-structured or typed memory to support retrieval and update over longer timescales. A-Mem builds semantic links among historical states ( [195](https://arxiv.org/html/2603.22862v2#bib.bib48 "A-mem: agentic memory for llm agents")), MIRIX decomposes memory into multiple specialized stores for persistent multimodal interaction ( [175](https://arxiv.org/html/2603.22862v2#bib.bib49 "Mirix: multi-agent memory system for llm-based agents")), and SEDM treats memory as a shared resource for multi-agent collaboration ( [193](https://arxiv.org/html/2603.22862v2#bib.bib50 "Sedm: scalable self-evolving distributed memory for agents")). Across these systems, the main design question is not whether to store more history, but how to retain the parts that remain relevant for decisions while suppressing noise and outdated branches.

### 3.3. Agent Self-Improvement

Inference-time capability is increasingly shaped not only by planning and memory, but also by mechanisms for self-improvement. In multi-tool settings, errors often arise from misbound parameters, invalid assumptions, or ineffective recovery strategies. As a result, many recent systems explicitly learn to diagnose and revise their own trajectories during or after execution.

A first family of methods focuses on self-correction. Reflexion stores verbalized lessons from prior failures and uses them to guide later attempts ( [153](https://arxiv.org/html/2603.22862v2#bib.bib51 "Reflexion: language agents with verbal reinforcement learning")). The Failure Makes the Agent Stronger framework turns diagnosis and repair into explicit actions trained with reward-based optimization over perturbed trajectories ( [158](https://arxiv.org/html/2603.22862v2#bib.bib52 "Failure makes the agent stronger: enhancing accuracy through structured reflection for reliable tool interactions")). SPIRAL and PreFlect further constrain or anticipate reflective behavior to reduce unproductive loops and catch likely failures before execution ( [223](https://arxiv.org/html/2603.22862v2#bib.bib53 "SPIRAL: symbolic llm planning via grounded and reflective search"); [164](https://arxiv.org/html/2603.22862v2#bib.bib54 "PreFlect: from retrospective to prospective reflection in large language model agents")). SAGE and Plan2Evolve extend this idea toward continual improvement by combining reflection with memory and planning repair ( [95](https://arxiv.org/html/2603.22862v2#bib.bib55 "Sage: self-evolving agents with reflective and memory-augmented abilities"); [63](https://arxiv.org/html/2603.22862v2#bib.bib56 "Plan2Evolve: llm self-evolution for improved planning capability via automated domain generation")).

A second family of methods treats improvement as capability evolution rather than isolated correction. MetaAgent distills accumulated experience into reusable tools and internal knowledge, enabling the agent to improve its future reasoning and tool-use strategies without additional model training ( [135](https://arxiv.org/html/2603.22862v2#bib.bib57 "MetaAgent: toward self-evolving agent via tool meta-learning")). Test-Time Tool Evolution pushes this direction further by synthesizing and validating new executable tools during inference ( [108](https://arxiv.org/html/2603.22862v2#bib.bib58 "Beyond static tools: test-time tool evolution for scientific reasoning")). DRAFT and SWE-Adept similarly revise tool descriptions or tool-memory interfaces in response to execution feedback ( [139](https://arxiv.org/html/2603.22862v2#bib.bib59 "From exploration to mastery: enabling llms to master tools via self-driven interactions"); [56](https://arxiv.org/html/2603.22862v2#bib.bib60 "SWE-adept: an llm-based agentic framework for deep codebase analysis and structured issue resolution")). This line of work suggests that inference is increasingly becoming an adaptive loop in which the agent not only uses a tool ecosystem, but also reorganizes and improves that ecosystem while solving tasks.

## 4\. Multi-Tool Agent Tuning Paradigms

Despite the remarkable generalization capabilities exhibited by LLMs across broad natural language tasks, deploying them as reliable agents in multi-tool orchestration scenarios remains a formidable challenge. Vanilla pre-trained models or general-purpose models frequently exhibit deficiencies in schema compliance, parameter precision, and long-horizon planning, which can easily lead to execution failures or hallucinations in complex multi-tool tasks. To bridge the gap between general-purpose models and specialized multi-tool agents, various adaptation strategies have been proposed to bolster the model’s proficiency in tool perception, selection, and precise execution. As shown in Figure [3](https://arxiv.org/html/2603.22862v2#S4.F3 "Figure 3 ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"), this chapter provides a systematic taxonomy of methodologies for Multi-tool Agent Tuning, organized in an ascending order of computational overhead and data dependency: we first investigate Training-free Methods that activate tool-calling capabilities without parameter updates; then introduce multi-tool trajectory data synthesis as the essential data foundation; followed by supervised fine-tuning (SFT) to align models with specific tool-calling syntaxes and planning patterns; and finally discuss reinforcement learning (RL) frameworks that exploit environmental feedback to improve agent self-evolution and decision-making robustness.

![Refer to caption](https://arxiv.org/html/2603.22862v2/x2.png)Figure 3. Taxonomy of Methodologies for Multi-tool Agent Tuning Paradigms

### 4.1. Training-free Methods

Training-free methods enhance multi-tool agents without updating LLM parameters, offering low deployment overhead and strong adaptability to newly introduced tools. Rather than altering the agent’s internal reasoning mechanism, these methods improve tool use through external augmentation, primarily along three directions: tool retrieval and discovery, prompt engineering, and non-parametric memory augmentation.

A major line of work studies tool retrieval and discovery. As the number of available APIs grows, exhaustively including tool documentation in the prompt becomes impractical. To address this issue, ToolLLM ( [138](https://arxiv.org/html/2603.22862v2#bib.bib63 "Toolllm: facilitating large language models to master 16000+ real-world apis")) and AnyTool ( [36](https://arxiv.org/html/2603.22862v2#bib.bib151 "Anytool: self-reflective, hierarchical agents for large-scale api calls")) employ retrieval-based mechanisms to dynamically select relevant tool descriptions from large tool repositories. ToolDreamer ( [144](https://arxiv.org/html/2603.22862v2#bib.bib152 "Tooldreamer: instilling llm reasoning into tool retrievers")) further improves retrieval quality by generating idealized tool descriptions as search queries, thereby better aligning user intents with real-world APIs. MCP-Zero ( [41](https://arxiv.org/html/2603.22862v2#bib.bib153 "Mcp-zero: active tool discovery for autonomous llm agents")) extends passive retrieval to active discovery, enabling agents to request tool schemas on demand and thus reducing context redundancy. Re-Invoke ( [25](https://arxiv.org/html/2603.22862v2#bib.bib154 "Re-invoke: tool invocation rewriting for zero-shot tool retrieval")) similarly improves zero-shot tool selection through multi-perspective query rewriting.
Another line of work focuses on prompt and exemplar construction for tool use. PLAY2PROMPT ( [40](https://arxiv.org/html/2603.22862v2#bib.bib160 "Play2prompt: zero-shot tool instruction optimization for llm agents via tool play")) allows agents to autonomously explore tool behavior and synthesize usage instructions together with few-shot exemplars, thereby improving tool invocation without SFT.
Finally, some methods enhance robustness through non-parametric memory augmentation. Memento ( [231](https://arxiv.org/html/2603.22862v2#bib.bib161 "Memento: fine-tuning llm agents without fine-tuning llms")) equips agents with episodic memory by retrieving successful historical trajectories to support current decision-making. GenTool ( [55](https://arxiv.org/html/2603.22862v2#bib.bib162 "GenTool: enhancing tool generalization in language models through zero-to-one and weak-to-strong simulation")) improves robustness through simulation under diverse conditions, such as missing or updated tools, thereby helping agents generalize to dynamic tool environments.

### 4.2. Multi-tool trajectory Data Synthesis

High-quality training data serves as the cornerstone for constructing robust multi-tool agents. However, the acquisition of real-world tool execution logs is constrained by privacy regulations, access permissions, and the scarcity of diverse scenarios, making large-scale manual annotation impractical. Consequently, synthetic data generation has emerged as the dominant paradigm. Recent literature reveals a systematic evolution toward a ”Synthesis-Validation-Expansion” framework, marking a strategic shift in research focus from basic data usability to the comprehensive coverage of the multi-tool composition space. This paradigm aims to synthesize training trajectories that encompass long-horizon interactions, cross-tool dependencies, and error recovery mechanisms in complex scenarios, thereby bolstering the agent’s capability to navigate intricate tasks.

Regarding data synthesis mechanisms, Early self-bootstrapping methods such as Seal-Tools ( [184](https://arxiv.org/html/2603.22862v2#bib.bib67 "Seal-tools: self-instruct tool learning dataset for agent tuning and detailed benchmark")) and Luo et al. ( [115](https://arxiv.org/html/2603.22862v2#bib.bib164 "Self-training large language models for tool-use without demonstrations")) show that LLMs can generate large amounts of tool-use data without expert demonstrations. More recent approaches improve structure and compositionality rather than scale alone. BUTTON ( [22](https://arxiv.org/html/2603.22862v2#bib.bib165 "Facilitating multi-turn function calling for llms via compositional instruction tuning")) combines bottom-up instruction construction with top-down trajectory generation to synthesize compositional interaction traces, while ASTRA ( [159](https://arxiv.org/html/2603.22862v2#bib.bib166 "ASTRA: automated synthesis of agentic trajectories and reinforcement arenas")) uses tool-call graph topology to generate structurally grounded trajectories in rule-verifiable environments.

In terms of data validation and quality control, recent advancements focus on execution-based iterative verification. As synthetic data grows in size, filtering by format alone becomes insufficient. APIGen ( [105](https://arxiv.org/html/2603.22862v2#bib.bib167 "Apigen: automated pipeline for generating verifiable and diverse function-calling datasets")) therefore verifies data through staged checking that includes syntax, actual execution, and semantic validation. StableToolBench ( [48](https://arxiv.org/html/2603.22862v2#bib.bib88 "Stabletoolbench-mirrorapi: modeling tool environments as mirrors of 7,000+ real-world apis")) reduces instability from volatile APIs through simulators and caching. ToolACE-DEV ( [65](https://arxiv.org/html/2603.22862v2#bib.bib168 "Toolace-dev: self-improving tool learning via decomposition and evolution")) and ToolACE-R ( [212](https://arxiv.org/html/2603.22862v2#bib.bib169 "ToolACE-r: model-aware iterative training and adaptive refinement for tool learning")) move further toward iterative repair, using self-improvement and model-aware refinement to adapt synthetic data to the learner’s evolving capability.

Concerning coverage and generalization expansion, numerous approaches aim to push the boundaries of the tool compositional space to tackle real-world complexity. ToolMind ( [198](https://arxiv.org/html/2603.22862v2#bib.bib170 "ToolMind technical report: a large-scale, reasoning-enhanced tool-use dataset")) advances data engineering for compositional space coverage by constructing large-scale, reasoning-intensive datasets. To enhance robustness against execution errors, LoopTool ( [219](https://arxiv.org/html/2603.22862v2#bib.bib171 "LoopTool: closing the data-training loop for robust llm tool calls")) institutionalizes failure-driven synthesis, creating a data closed-loop that mirrors real-world failure distributions. For complex orchestration, OrchDAG ( [111](https://arxiv.org/html/2603.22862v2#bib.bib172 "OrchDAG: complex tool orchestration in multi-turn interactions with plan dags")) models tool execution as Directed Acyclic Graphs (DAGs) with controllable complexity, providing structured benchmarks for multi-turn interactions. Collectively, these advancements reflect a new consensus: the critical metric for synthetic data is no longer mere quantity, but the systematic coverage of long-tail effects, complex interaction effects, and multi-step error patterns.

### 4.3. Supervised Fine-Tuning

Supervised Fine-Tuning (SFT) represents the foundational alignment phase for endowing Large Language Models with tool-use capabilities. Amidst the paradigm shift from atomic tool invocation to multi-tool orchestration, the objectives of SFT have undergone a fundamental transformation. Early methodologies primarily emphasized syntax alignment—ensuring the structural integrity of outputs (e.g., JSON schema compliance). Pioneering works such as Gorilla ( [130](https://arxiv.org/html/2603.22862v2#bib.bib173 "Gorilla: large language model connected with massive apis")) and GPT4Tools ( [201](https://arxiv.org/html/2603.22862v2#bib.bib174 "Gpt4tools: teaching large language model to use tools via self-instruction")) demonstrated that fine-tuning on high-quality (Instruction, API Call) pairs enables models to effectively acquire API semantic matching and parameter filling skills. However, mere data accumulation is no longer sufficient to address complex orchestration tasks. Consequently, recent advancements have pivoted toward more specialized objectives, such as tool selection from massive repositories and inter-tool dependency planning.

To address large-scale and noisy tool selection, ToolLLM ( [138](https://arxiv.org/html/2603.22862v2#bib.bib63 "Toolllm: facilitating large language models to master 16000+ real-world apis")) extends SFT to massive toolsets by training on Depth-First Search decision trajectories, enabling the model to internalize exploration and trial-and-error strategies for unresolvable scenarios. Hammer ( [98](https://arxiv.org/html/2603.22862v2#bib.bib175 "Hammer: robust function-calling for on-device language models via function masking")) introduces Function Masking during fine-tuning to penalize hallucinations and heighten sensitivity to irrelevant tools, establishing a new benchmark for robust on-device function calling. To optimize the interplay between reasoning and action, Chain-of-Abstraction ( [43](https://arxiv.org/html/2603.22862v2#bib.bib176 "Efficient tool use with chain-of-abstraction reasoning")) proposes a dual-stage decoding strategy; it trains the model to first generate abstract reasoning chains with placeholders and subsequently populate them with concrete tool outputs, effectively decoupling general reasoning from domain-specific knowledge retrieval. ToolGen ( [172](https://arxiv.org/html/2603.22862v2#bib.bib177 "Toolgen: unified tool retrieval and calling via generation")) unifies tool retrieval and parameter generation into a sequence of generative virtual tokens, restructuring the SFT objective to allow the simultaneous learning of tool semantics and parameter structures in a single autoregressive pass, which significantly mitigates cascading errors. Finally, addressing task granularity, the Granite-Function Calling Model ( [1](https://arxiv.org/html/2603.22862v2#bib.bib178 "Granite-function calling model: introducing function calling abilities via multi-task learning of granular tasks")) adopts a multi-task learning framework that decomposes tool usage into fine-grained subtasks—such as tool detection, parameter generation, and response formatting—thereby achieving precise control over the entire execution lifecycle. Collectively, these developments signify that SFT has evolved beyond simple pattern imitation toward the construction of autonomous systems capable of high-level decision-making and rigorous execution.

### 4.4. Reinforcement Learning

Although SFT effectively aligns models with fundamental tool-use syntax, it remains inherently constrained by the Behavioral Cloning paradigm. Models trained via SFT are often limited to myopic imitation of training trajectories, struggling to self-correct during long-horizon tasks or to explore novel paths within open-ended tool spaces. Consequently, the research focus is shifting toward Reinforcement Learning and environmental feedback to optimize high-level decision-making. As the field transitions from single-tool triggering to multi-tool orchestration, RL encounters formidable challenges: sparse reward signals, difficult credit assignment, and training instability. Thus, recent advances have transcended standard algorithms like PPO or GRPO, developing specialized paradigms centered on process reward design, turn-level policy optimization, and end-to-end agent frameworks. These innovations aim to evolve agents from passive executors into adaptive planners capable of robust error recovery and strategic exploration.

Regarding Reward Modeling and Credit Assignment, to bridge the gap between sparse outcome rewards and complex multi-step reasoning, the community has established a comprehensive reward-optimization closed loop. Addressing the sparsity of success signals in long chains, PORTool ( [182](https://arxiv.org/html/2603.22862v2#bib.bib179 "PORTool: tool-use llm training with rewarded tree")) integrates quality signals generated by tree search into policy gradient updates, while Tool-Star ( [31](https://arxiv.org/html/2603.22862v2#bib.bib180 "Tool-star: empowering llm-brained multi-tool reasoner via reinforcement learning")) designs hierarchical reward mechanisms to resolve credit assignment issues in multi-step reasoning. Moving toward systematic reward engineering, ToolRL ( [133](https://arxiv.org/html/2603.22862v2#bib.bib181 "Toolrl: reward is all tool learning needs")) conducts a comprehensive study on reward granularity, proposing principled reward designs that surpass simple pass/fail metrics to stabilize training. Similarly, ToolRM ( [4](https://arxiv.org/html/2603.22862v2#bib.bib182 "Toolrm: outcome reward models for tool-calling large language models")) trains a dedicated Outcome Reward Model to evaluate tool-based reasoning, outperforming general-purpose verifiers in complex scenarios. To reinforce intermediate steps,
Wei et al. ( [179](https://arxiv.org/html/2603.22862v2#bib.bib183 "Reinforcing multi-turn reasoning in llm agents via turn-level reward design")) introduce verifiable turn-level rewards, extending RL algorithms to handle fine-grained credit assignment in multi-turn search tasks.

In terms of Policy Optimization and Algorithm Adaptation, standard RL algorithms often struggle to adapt to drastic dynamic shifts in agent tasks. DeepAgent ( [87](https://arxiv.org/html/2603.22862v2#bib.bib39 "Deepagent: a general reasoning agent with scalable toolsets")) explores ToolPO (Tool Policy Optimization), which addresses the high cost and instability of training with real APIs by utilizing an LLM-simulated API environment for low-cost exploration. It simultaneously introduces Fine-grained Advantage Attribution, precisely allocating reward signals to the specific tokens triggering tool invocations, thereby significantly enhancing stability in open-set tool retrieval. Addressing the limitations of trajectory-level rewards in GRPO, GTPO ( [30](https://arxiv.org/html/2603.22862v2#bib.bib184 "Empowering multi-turn tool-integrated reasoning with group turn policy optimization")) innovatively adopts turn-level reward distribution and return-based advantage estimation, effectively preventing training stagnation during iterative reasoning. Furthermore, to mitigate Entropy Spikes following tool interactions, ARPO ( [32](https://arxiv.org/html/2603.22862v2#bib.bib185 "Agentic reinforced policy optimization")) incorporates an entropy-based adaptive rollback mechanism to dynamically balance global exploration and local exploitation. RAGEN ( [178](https://arxiv.org/html/2603.22862v2#bib.bib186 "Ragen: understanding self-evolution in llm agents via multi-turn reinforcement learning")) identifies the Echo Trap phenomenon specific to agent training and proposes the StarPO algorithm to stabilize the learning process through trajectory-level optimization.

Concerning End-to-End Frameworks, ToRL ( [90](https://arxiv.org/html/2603.22862v2#bib.bib187 "Torl: scaling tool-integrated rl")) demonstrates that RL can directly extend tool-use capabilities from a Base Model without a prerequisite SFT phase, unlocking emergent behaviors such as self-regulation. Finally, Agent-R1 ( [26](https://arxiv.org/html/2603.22862v2#bib.bib189 "Agent-r1: training powerful llm agents with end-to-end reinforcement learning")) comprehensively defines LLM Agents by extending the Markov Decision Process (MDP) framework, providing a modular and scalable system for end-to-end reinforcement learning.

## 5\. Safety of Multi-Tool Agents

The security landscape of tool-augmented agents has shifted from mere malicious text generation to the execution of harmful actions within digital or physical environments. While single-tool vulnerabilities—such as indirect prompt injection ( [46](https://arxiv.org/html/2603.22862v2#bib.bib190 "Not what you’ve signed up for: compromising real-world llm-integrated applications with indirect prompt injection")), unauthorized execution and privilege escalation ( [77](https://arxiv.org/html/2603.22862v2#bib.bib191 "Prompt flow integrity to prevent privilege escalation in llm agents")), privacy leakage, and tool-assisted attacks ( [53](https://arxiv.org/html/2603.22862v2#bib.bib17 "The emerged security and privacy of llm agent: a survey with case studies"); [12](https://arxiv.org/html/2603.22862v2#bib.bib192 "Design patterns for securing llm agents against prompt injections"); [146](https://arxiv.org/html/2603.22862v2#bib.bib194 "A survey on agentic security: applications, threats and defenses"))—are well-documented, the transition to multi-tool orchestration significantly expands the system’s attack surface. In multi-tool systems, security is no longer determined by the legitimacy of isolated API calls but by complex, cross-tool, and cross-timestep execution structures. These interactions breach traditional trust boundaries, where localized malicious inputs or model hallucinations are rarely isolated incidents. Instead, they often induce ”state pollution” through the tool-chain context, leading to cascading propagation of attacks. This chapter investigates the novel security challenges and defense mechanisms inherent in multi-tool orchestration. Based on the topological execution logic of tool chains, we categorize multi-tool security risks into two distinct yet interrelated dimensions: (1) security risks in parallel execution, and (2) security risks in long-horizon tool chains.

### 5.1. Security Risks in Parallel Execution

In multi-tool orchestration architectures, parallel execution significantly enhances agent efficiency in complex task processing; however, it introduces latent security vulnerabilities. While parallelization is relatively safe for side-effect-free read operations (e.g., web retrieval, information queries), the integration of write operations (e.g., database updates, transaction commits) within tool chains risks race conditions, leading to system state inconsistencies. Consequently, the central challenge of multi-tool parallelization lies in maintaining state integrity within concurrent environments.

Recent work shows that this risk is not merely an implementation detail. Les Dissonances demonstrates that when LLMs invoke interdependent tools concurrently, malicious payloads can propagate across tool boundaries and contaminate later execution ( [92](https://arxiv.org/html/2603.22862v2#bib.bib195 "Les dissonances: cross-tool harvesting and polluting in multi-tool empowered llm agents")). Related analysis of stateful tool use in multi-turn dialogue finds that reliability failures often follow a recognizable path from parameter drift to state contamination and then to irrecoverable downstream calls ( [166](https://arxiv.org/html/2603.22862v2#bib.bib196 "Rethinking stateful tool use in multi-turn dialogues: benchmarks and challenges")). SagaLLM makes this issue explicit by modeling tool use as bounded workflows with transactional semantics and rollback logic ( [17](https://arxiv.org/html/2603.22862v2#bib.bib197 "SagaLLM: context management, validation, and transaction guarantees for multi-agent llm planning")). Taken together, these studies suggest that safe parallelism requires more than better prompting; it requires explicit control over side effects and execution scope.

To address these challenges, recent studies have begun to introduce transaction management paradigms from distributed systems and software engineering into LLM orchestration frameworks. Current solutions demonstrate an evolutionary trajectory from ”pre-execution static constraints” to ”in-execution transaction management”, and ultimately to ”post-execution dynamic verification”:

Pre-execution Static Constraints:
Intercepting potentially conflicting actions before tools are concurrently triggered serves as the first line of defense. At the system implementation level, the AARM specification  ( [38](https://arxiv.org/html/2603.22862v2#bib.bib199 "Autonomous action runtime management (aarm): a system specification for securing ai-driven actions at runtime")) and AgentSpec  ( [165](https://arxiv.org/html/2603.22862v2#bib.bib200 "Agentspec: customizable runtime enforcement for safe and reliable llm agents")) propose interception-based runtime enforcement mechanisms. These approaches block illegal concurrent requests by deeply injecting intent alignment and security policies prior to execution. For complex environments, Self-Verification Sampling  ( [47](https://arxiv.org/html/2603.22862v2#bib.bib201 "Sample, predict, then proceed: self-verification sampling for tool use of llms")) preemptively filters out high-risk write operations through pre-execution self-verification, thereby mitigating the catastrophic probability of irreversible post-write scenarios.

In-execution Transaction Management:
Since concurrent errors are inherently difficult to eradicate entirely during execution, researchers have begun endowing agents with transaction semantics. SagaLLM  ( [17](https://arxiv.org/html/2603.22862v2#bib.bib197 "SagaLLM: context management, validation, and transaction guarantees for multi-agent llm planning")) and the recent Atomix framework have made breakthroughs by treating tool invocations as bounded workflows. Atomix introduces epoch-based concurrency isolation and resource frontier tracking  ( [121](https://arxiv.org/html/2603.22862v2#bib.bib202 "Atomix: timely, transactional tool use for reliable agentic workflows")), allowing harmless side effects to undergo a delayed commit while enabling secure rollbacks via compensation logic in the event of an abort. This design mirrors the localized checkpoint mechanism in the Generator-Assistant framework ( [88](https://arxiv.org/html/2603.22862v2#bib.bib203 "Generator-assistant stepwise rollback framework for large language model agent")), which strictly confines the impact of errors to localized scopes.

Post-execution Dynamic Verification:
To address anomalous scenarios beyond the reach of static constraints, post-execution verification logic must be integrated into the system to form a closed-loop feedback mechanism. CRITIC  ( [45](https://arxiv.org/html/2603.22862v2#bib.bib204 "Critic: large language models can self-correct with tool-interactive critiquing")) achieves self-correction through interactive critiquing; VerifiAgent ( [51](https://arxiv.org/html/2603.22862v2#bib.bib205 "Verifiagent: a unified verification agent in language model reasoning")) engineers verification logic into a collaborative Verifier-Executor component architecture; meanwhile, DVR ( [221](https://arxiv.org/html/2603.22862v2#bib.bib206 "Divide-verify-refine: can llms self-align with complex instructions?")) approaches the issue from a graph-structured scheduling perspective, seamlessly embedding verification subgraphs into the primary execution graph. This provides a universal template for the security auditing of parallel execution.

Table 1. Representative safety risks and defense mechanisms for multi-tool agents.

|     |     |     |
| --- | --- | --- |
| Risk | Failure Mode | Defense |
| Concurrent Conflict | Race conditions, write interference, and corrupted shared states. | Dependency-aware scheduling, policy gating, and pre-dispatch verification<br>( [92](https://arxiv.org/html/2603.22862v2#bib.bib195 "Les dissonances: cross-tool harvesting and polluting in multi-tool empowered llm agents"); [38](https://arxiv.org/html/2603.22862v2#bib.bib199 "Autonomous action runtime management (aarm): a system specification for securing ai-driven actions at runtime"); [165](https://arxiv.org/html/2603.22862v2#bib.bib200 "Agentspec: customizable runtime enforcement for safe and reliable llm agents")). |
| Partial Commit | Irreversible side effects leave globally inconsistent states. | Transaction-style isolation, delayed commit, compensation, and rollback<br>( [17](https://arxiv.org/html/2603.22862v2#bib.bib197 "SagaLLM: context management, validation, and transaction guarantees for multi-agent llm planning"); [121](https://arxiv.org/html/2603.22862v2#bib.bib202 "Atomix: timely, transactional tool use for reliable agentic workflows"); [88](https://arxiv.org/html/2603.22862v2#bib.bib203 "Generator-assistant stepwise rollback framework for large language model agent")). |
| Post-Execution Anomaly | Safety violations emerge only after tool execution. | Critic/verifier-based auditing and execution-time checking<br>( [45](https://arxiv.org/html/2603.22862v2#bib.bib204 "Critic: large language models can self-correct with tool-interactive critiquing"); [51](https://arxiv.org/html/2603.22862v2#bib.bib205 "Verifiagent: a unified verification agent in language model reasoning"); [221](https://arxiv.org/html/2603.22862v2#bib.bib206 "Divide-verify-refine: can llms self-align with complex instructions?")). |
| Memory/Plan Poisoning | Malicious context persists across steps and reactivates later. | Trajectory-level verification, meta-verification, and evidence-based rejection<br>( [34](https://arxiv.org/html/2603.22862v2#bib.bib208 "Memory injection attacks on llm agents via query-only interaction"); [136](https://arxiv.org/html/2603.22862v2#bib.bib198 "Making language models better tool learners with execution feedback"); [116](https://arxiv.org/html/2603.22862v2#bib.bib214 "Advancing tool-augmented large language models via meta-verification and reflection learning")). |
| Long-Horizon Drift | Error accumulation, state pollution, and confused-deputy behavior. | Lookahead search, rollback, and trace diagnosis<br>( [189](https://arxiv.org/html/2603.22862v2#bib.bib213 "Butterfly effects in toolchains: a comprehensive analysis of failed parameter filling in llm tool-agent systems"); [230](https://arxiv.org/html/2603.22862v2#bib.bib216 "Language agent tree search unifies reasoning acting and planning in language models"); [100](https://arxiv.org/html/2603.22862v2#bib.bib210 "AgentDoG: a diagnostic guardrail framework for ai agent safety and security")). |

### 5.2. Security Risks in Long-Horizon Tool Chains

In long-horizon tool chains, security threats manifest as stealthy propagation and cascading amplification across temporal dimensions. As agents extend multi-step invocation sequences, the continuous introduction of intermediate variables and parameter bindings renders the system susceptible to Agent Drift ( [142](https://arxiv.org/html/2603.22862v2#bib.bib9 "Agent drift: quantifying behavioral degradation in multi-agent llm systems over extended interactions")). Here, the pollution of the context window and the accumulation of autoregressive errors cause behavioral patterns to deviate from established safety baselines. In adversarial settings, this ”contextual drift” evolves into destructive Cross-Tool State Contamination. Once malicious data are introduced into intermediate results, its indiscriminate reuse in subsequent steps triggers a cascading failure that eventually collapses the trust boundaries of the system.

Centering on this temporal vulnerability, recent literature identifies novel attack modes unique to long-horizon orchestration. Attacks have evolved beyond single-step manipulation to sophisticated memory poisoning and plan injection. For instance, MINJA-style attacks inject malicious content through apparently benign read operations and allow it to persist in memory until it influences later actions ( [34](https://arxiv.org/html/2603.22862v2#bib.bib208 "Memory injection attacks on llm agents via query-only interaction")). Plan Injection attacks instead manipulate the structure of multi-step reasoning itself, steering the agent around guardrails without requiring an obviously malicious final command ( [24](https://arxiv.org/html/2603.22862v2#bib.bib209 "Deep research brings deeper harm")). Butterfly Effects in Toolchains further shows how small upstream deviations can be amplified through variable binding and parameter reuse, turning downstream tools into confused deputies whose unsafe behavior is rooted in much earlier steps ( [189](https://arxiv.org/html/2603.22862v2#bib.bib213 "Butterfly effects in toolchains: a comprehensive analysis of failed parameter filling in llm tool-agent systems")).

To mitigate malicious accumulation and state hijacking during long-horizon execution, defense mechanisms are transitioning from single-step result filtering to trajectory-level dynamic intervention and closed-loop auditing. Reflexion provides an early form of revision through verbal feedback memory, but later work places greater emphasis on execution-grounded verification ( [153](https://arxiv.org/html/2603.22862v2#bib.bib51 "Reflexion: language agents with verbal reinforcement learning")). TRICE, Tool-MVR, and ToolReflection use execution evidence, multi-agent verification, or structured returns to identify and correct errors over longer trajectories ( [136](https://arxiv.org/html/2603.22862v2#bib.bib198 "Making language models better tool learners with execution feedback"); [116](https://arxiv.org/html/2603.22862v2#bib.bib214 "Advancing tool-augmented large language models via meta-verification and reflection learning"); [131](https://arxiv.org/html/2603.22862v2#bib.bib215 "ToolReflection: improving large language models for real-world api calls with self-generated data")). LATS combines search with rollback and circuit-breaking behavior when downstream risks become visible ( [230](https://arxiv.org/html/2603.22862v2#bib.bib216 "Language agent tree search unifies reasoning acting and planning in language models")). Other systems focus on diagnosis rather than rejection alone: AgentDoG emphasizes root-cause attribution across the full execution chain ( [100](https://arxiv.org/html/2603.22862v2#bib.bib210 "AgentDoG: a diagnostic guardrail framework for ai agent safety and security")), while Thought-Aligner intervenes earlier by correcting risky internal reasoning before unsafe actions are produced ( [71](https://arxiv.org/html/2603.22862v2#bib.bib211 "Think twice before you act: enhancing agent behavioral safety with thought correction")). The overall direction is toward making long-horizon execution inspectable, interruptible, and repairable.

In addition to introducing dynamic auditing during the inference phase, specialized training methodologies tailored for long-horizon multi-tool security are crucial for raising the upper bound of defense from the foundational model level. Because traditional RLHF based on single-turn dialogues struggles to cover the complex state space of long-horizon tool chains, model alignment is evolving toward encompassing the entire multi-step invocation trajectory. The latest agent security alignment frameworks introduce customized Sandbox environments for reinforcement learning  ( [145](https://arxiv.org/html/2603.22862v2#bib.bib212 "Agent safety alignment via reinforcement learning")), compelling models to execute a ”perform-reject-verify” confirmation mechanism when confronted with ambiguous or malicious inputs. Concurrently, to combat memory pollution induced by long-horizon interactions, Episodic Memory Consolidation mechanisms  ( [142](https://arxiv.org/html/2603.22862v2#bib.bib9 "Agent drift: quantifying behavioral degradation in multi-agent llm systems over extended interactions")) are being employed to periodically compress interaction histories and purge potential malicious payloads. By integrating adversarial tool chains generated via automated red teaming as negative samples for alignment fine-tuning, the underlying LLMs’ resilience against interference and the robustness of their parameter extraction—especially when facing unreliable memories and malicious intermediate states—are fundamentally enhanced.

## 6\. Efficiency of Multi-Tool Agents

The integration of external tools has substantially enhanced the capability of agents to address complex tasks. Nevertheless, the reliance on multi-step inference and sequential tool invocation introduces significant efficiency bottlenecks. This chapter reviews emerging optimization strategies from two primary perspectives: mitigating latency in multi-tool chains (§ [6.1](https://arxiv.org/html/2603.22862v2#S6.SS1 "6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")) and managing tool call cost and inference budget (§ [6.2](https://arxiv.org/html/2603.22862v2#S6.SS2 "6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")).

### 6.1. Latency in multi-tool chains

The strict dependency of LLM inference on the completion and return of previous tool results leads to a linear or even exponential accumulation of end-to-end system latency with the number of task steps ( [78](https://arxiv.org/html/2603.22862v2#bib.bib147 "An llm compiler for parallel function calling")). To address this efficiency bottleneck, recent research has focused on refactoring the execution mechanism, evolving into three core optimization paradigms: parallel execution (§ [6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), asynchronous decoupling (§ [6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), and speculative reasoning (§ [6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")).

#### 6.1.1. Parallel execution

To address the cumulative delays and inefficiencies caused by sequential execution in long-chain multi-tool calls, parallel execution ( [233](https://arxiv.org/html/2603.22862v2#bib.bib150 "Divide-then-aggregate: an efficient tool learning method via parallel tool invocation")) has become a key optimization direction. Its core idea is to decompose tasks, identify subtasks with no interdependencies, and execute them simultaneously. SoT ( [124](https://arxiv.org/html/2603.22862v2#bib.bib146 "Skeleton-of-thought: prompting llms for efficient parallel generation")) accelerates inference by expanding multiple skeleton branches in parallel instead of following a fully sequential decoding pattern. At the tool level, LLMCompiler ( [78](https://arxiv.org/html/2603.22862v2#bib.bib147 "An llm compiler for parallel function calling")) explicitly plans task dependencies so that independent tool calls can run concurrently. For longer workflows, M1-Parallel ( [216](https://arxiv.org/html/2603.22862v2#bib.bib148 "Optimizing sequential multi-step tasks with parallel llm agents")) further decomposes sequential tasks into independent subtasks coordinated by multiple agents. Parallelized planning-acting ( [91](https://arxiv.org/html/2603.22862v2#bib.bib217 "Parallelized planning-acting for efficient llm-based multi-agent systems")) extend the same idea by overlapping planning and execution, allowing later steps to be prepared while current actions are still running. Taken together, these approaches show that parallel execution is most effective when dependency structure is explicit and side effects are sufficiently controlled to avoid invalid concurrent actions.

#### 6.1.2. Asynchronous decoupling

Traditional agent architectures generally follow a synchronous observation-thinking-action loop. LLMs must block and wait for I/O results after calling external tools. This coupling of computation and execution leads to severe latency accumulation ( [204](https://arxiv.org/html/2603.22862v2#bib.bib20 "React: synergizing reasoning and acting in language models")). To break this serial bottleneck, recent studies have proposed asynchronously decoupling the planning and acting of agents.
To overcome the I/O blocking limitations and strict serial dependencies faced by traditional agents during long toolchain calls, asynchronous decoupling significantly improves concurrent throughput by separating computationally intensive inference planning from I/O-intensive tool execution at the system architecture level. In recent years, as models have been increasingly applied in dynamic environments, this decoupling has gradually evolved into the core foundation for environment-aware task planning and multi-node decentralized inference. For example,  ( [91](https://arxiv.org/html/2603.22862v2#bib.bib217 "Parallelized planning-acting for efficient llm-based multi-agent systems")) is proposed that completely decouples macro-level environment-aware planning from low-level action execution, and uses a centralized agent memory system for asynchronous state synchronization, thoroughly mitigating inference latency caused by dynamic environmental changes. When dealing with complex constraint logic, MACI ( [18](https://arxiv.org/html/2603.22862v2#bib.bib218 "Maci: multi-agent collaborative intelligence for adaptive reasoning and temporal planning")) has demonstrated that separating task planning from external tool verification effectively prevents attention shift and constraint drift in large models during long-term calls. This decoupling paradigm, also applied in cybersecurity attack and defense and GUI, Incalmo ( [154](https://arxiv.org/html/2603.22862v2#bib.bib219 "Incalmo: an autonomous llm-assisted system for red teaming multi-host networks")) reveals that decoupling macro-level strategic intent from low-level shell script execution is key to preventing agents from getting stuck in local optima. Temac ( [99](https://arxiv.org/html/2603.22862v2#bib.bib220 "Temac: multi-agent collaboration for automated web gui testing")) specifically designed a Planner-Actor heterogeneous mechanism, using independent executors to asynchronously call interface probing tools.

#### 6.1.3. Speculative reasoning

Unlike asynchronous decoupling, which optimizes from the system architecture perspective, Speculative Execution borrows the branch prediction concept from computer architecture, aiming to mask waiting latency in long toolchains through algorithmic forward prediction. This mechanism is underpinned by speculative decoding ( [83](https://arxiv.org/html/2603.22862v2#bib.bib221 "Fast inference from transformers via speculative decoding")), which allows the model to speculatively generate subsequent action identifiers without waiting for a complete autoregressive loop. In the tool invocation domain, ReWoo ( [192](https://arxiv.org/html/2603.22862v2#bib.bib222 "Rewoo: decoupling reasoning from observations for efficient augmented language models")) is a typical example of this approach. By decoupling inference from observation, it speculatively generates a complete execution graph containing expected tool outputs, committing execution only when the speculation is correct, thus significantly reducing redundant latency when interacting with external tool environments. To improve the accuracy of speculation, LATS ( [230](https://arxiv.org/html/2603.22862v2#bib.bib216 "Language agent tree search unifies reasoning acting and planning in language models")) introduces a speculative simulation mechanism based on lookahead search. Before actually invoking an irreversible API, the agent infers and evaluates multiple possible tool interaction trajectories. Similarly, ToT ( [203](https://arxiv.org/html/2603.22862v2#bib.bib223 "Tree of thoughts: deliberate problem solving with large language models")) utilizes speculative branch exploration to predict the final benefits of different tool combinations, significantly reducing the backtracking time cost caused by tool invocation failures in complex tasks. For retrieval tools that suffer from particularly high latency, REST ( [59](https://arxiv.org/html/2603.22862v2#bib.bib224 "Rest: retrieval-based speculative decoding")) proposes a retrieval-based speculative decoding framework that can predict the subsequent generated content of a large model in advance based on cached results from an external knowledge base. At the engineering implementation and pipeline optimization level, the DSPy ( [76](https://arxiv.org/html/2603.22862v2#bib.bib225 "Dspy: compiling declarative language model calls into self-improving pipelines")) framework uses a compile-level declarative pipeline to speculatively route and merge multiple tool call requests, minimizing runtime latency across multiple toolchains without sacrificing task success rate.

### 6.2. Tool call cost and inference budget

Besides time latency, multi-tool agent invocation also faces high inference costs and limited context budgets. Frequent invocation of large-parameter models to process simple tools or filling massive tool descriptions into the context all at once leads to wasted resources and performance degradation ( [218](https://arxiv.org/html/2603.22862v2#bib.bib226 "Ecoassistant: using llm assistant more affordably and accurately")). To address these pain points, existing research mainly focuses on optimization along three core dimensions: dynamic tool retrieval (§ [6.2.1](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS1 "6.2.1. Dynamic tool search ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), adaptive model routing (§ [6.2.2](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS2 "6.2.2. Adaptive Model Routing ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), and intelligent caching and memory (§ [6.2.3](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS3 "6.2.3. Intelligent caching and memory ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")).

#### 6.2.1. Dynamic tool search

Faced with hundreds or thousands of external tool libraries, hardcoding all API descriptions into prompts at once not only consumes a huge input token budget but also easily leads to the Lost in the Middle phenomenon caused by long texts ( [102](https://arxiv.org/html/2603.22862v2#bib.bib227 "Lost in the middle: how language models use long contexts")). To efficiently organize tools within a limited context window, the current mainstream paradigm has shifted to query-based dynamic retrieval and representation compression. For example, the ToolLLM ( [138](https://arxiv.org/html/2603.22862v2#bib.bib63 "Toolllm: facilitating large language models to master 16000+ real-world apis")) framework introduces a neural API retrieval engine. Before executing a task, the agent retrieves the Top-K most relevant tool descriptions based on the user’s instructions, thus avoiding irrelevant tools crowding out the context space. For ultra-large API libraries with tens of thousands of entries, AnyTool ( [36](https://arxiv.org/html/2603.22862v2#bib.bib151 "Anytool: self-reflective, hierarchical agents for large-scale api calls")) further designs a hierarchical API retrieval mechanism, using a categorized directory tree for progressive filtering, significantly reducing the retrieval cost and context overhead of a single call. Furthermore, at the representation compression level, ToolkenGPT ( [52](https://arxiv.org/html/2603.22862v2#bib.bib228 "Toolkengpt: augmenting frozen language models with massive tools via tool embeddings")) proposes an innovative vocabulary expansion strategy that compresses and maps the lengthy tool invocation logic and its parameter descriptions into a single special term. This method allows the agent to trigger the tool simply by predicting the corresponding Toolken at the output, fundamentally bypassing the rigid limitation of using lengthy descriptions as input prompts.

#### 6.2.2. Adaptive Model Routing

To control computational costs, multi-agent architectures have gradually abandoned the crude approach of a single giant model scheduling everything, shifting towards a computational allocation strategy that dynamically matches model size to task difficulty ( [167](https://arxiv.org/html/2603.22862v2#bib.bib232 "Orchestrating intelligence: confidence-aware routing for efficient multi-agent collaboration across multi-scale models")). Model cascading mechanisms, exemplified by FrugalGPT ( [21](https://arxiv.org/html/2603.22862v2#bib.bib229 "Frugalgpt: how to use large language models while reducing cost and improving performance")), prioritize low-cost models, only routing to expensive large models when confidence is insufficient, significantly reducing budget without sacrificing accuracy. With further refinement, RouteLLM ( [126](https://arxiv.org/html/2603.22862v2#bib.bib10 "Routellm: learning to route llms with preference data")) trained a dedicated network that adaptively distributes requests among models of different sizes based on task complexity. In multi-step tasks, SwiftSage ( [96](https://arxiv.org/html/2603.22862v2#bib.bib231 "Swiftsage: a generative agent with fast and slow thinking for complex interactive tasks")) borrows from the human dual-system approach, layering its architecture into lightweight edge modules handling routine operations and a central large model responsible for complex inference, achieving globally optimal allocation of computational resources.

#### 6.2.3. Intelligent caching and memory

In complex environments with high-frequency interactions, repeated erroneous attempts and highly similar API requests are the core factors consuming inference budgets, while building a structured Agent Memory and caching layer provides key support for breaking this bottleneck. Firstly, regarding reducing trial-and-error costs, Reflexion ( [153](https://arxiv.org/html/2603.22862v2#bib.bib51 "Reflexion: language agents with verbal reinforcement learning")) framework proposes an efficient alternative that does not require updating model weights. Through Verbal Reinforcement Learning, it allows the agent to reflect on its failures and persistently store the resulting improvement strategies in Episodic Memory. In subsequent attempts, the agent can accurately avoid historical errors by calling this structured memory, significantly reducing the number of interaction rounds and total computational overhead required to reach a successful task state. To address the memory capacity bottleneck in long-cycle tasks, MemGPT ( [128](https://arxiv.org/html/2603.22862v2#bib.bib233 "MemGPT: towards llms as operating systems.")) introduces the concept of virtual memory management from operating systems into large models. By autonomously paging and swapping memory between the fast context and external database, the agent can maintain an infinite memory length with an extremely low token budget. Furthermore, at the level of API call result reuse, semantic caching systems such as GPTCache ( [9](https://arxiv.org/html/2603.22862v2#bib.bib234 "Gptcache: an open-source semantic cache for llm applications enabling faster answers and cost savings")) perform vectorized comparison of input queries and tool parameters. When semantically similar duplicate requests are detected, historical results are directly returned from the local machine, completely blocking redundant LLM inference and external network request billing.

## 7\. Completeness

In complex open-domain scenarios, multi-tool agents are gradually transitioning from closed, static API executions to dynamic interactions within real-world environments ( [94](https://arxiv.org/html/2603.22862v2#bib.bib188 "Ai meets brain: memory systems from cognitive neuroscience to autonomous agents")). However, the inherent unpredictability of these environments frequently leads to functional incompleteness, wherein predefined toolkits fail to fully satisfy emerging task requirements ( [15](https://arxiv.org/html/2603.22862v2#bib.bib241 "Large language models as tool makers")). This chapter systematically reviews the challenges and corresponding solutions regarding the tool completeness of multi-tool agents. These solutions are conceptualized as a continuous cognitive loop comprising problem diagnosis, dynamic compensation, and long-term evolution. Specifically, this loop progresses sequentially through three core phases. The first phase is capability boundary perception (§ [7.1](https://arxiv.org/html/2603.22862v2#S7.SS1 "7.1. Capability boundary perception ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), designed to identify tool deficiencies and operational failures. The second phase is autonomous tool expansion (§ [7.2](https://arxiv.org/html/2603.22862v2#S7.SS2 "7.2. Autonomous tool expansion ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")) is achieved through code generation and tool synthesis. Ultimately, the process culminates in open environment adaptation (§ [7.3](https://arxiv.org/html/2603.22862v2#S7.SS3 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration")), which leverages experience and memory mechanisms for sustained operation.

![Refer to caption](https://arxiv.org/html/2603.22862v2/x3.png)Figure 4. Overview of the completeness evolution in multi-tool agents. The framework characterizes functional completeness as a continual process with three sequential yet interrelated stages: capability boundary perception, which identifies missing tools, ambiguous intents, and parameter anomalies through clarification and safe termination; autonomous tool expansion, which compensates for capability gaps via tool creation, tool synthesis, API integration, and composite skill construction; and open environment adaptation, which consolidates successful tools and interaction traces into reusable experience memory to support dynamic updating and long-term evolution in changing environments.

### 7.1. Capability boundary perception

The logical starting point for the completeness of a multi-tool agent lies in its ability to accurately identify intent denial and detect anomalies, that is, to perceive its own capability boundaries. Traditional language models, when faced with tasks beyond the capabilities of the toolkit, are prone to hallucinate tools, creating fictitious API nodes or parameter formats. Therefore, accurately identifying incomplete conditions is the core of ensuring system robustness. Several studies have already quantified the limitations of models in terms of the boundaries of perception capabilities. The FAIL-TALMS ( [160](https://arxiv.org/html/2603.22862v2#bib.bib235 "Benchmarking failures in tool-augmented language models")) demonstrates that large language models frequently lack boundary awareness when dealing with ambiguous intentions or missing tools, rendering them prone to blind trial and error. Furthermore, ToolHaystack ( [80](https://arxiv.org/html/2603.22862v2#bib.bib236 "Toolhaystack: stress-testing tool-augmented language models in realistic long-term interactions")) reveals that during extended complex interactions involving critical information deficits, models are highly susceptible to parameter hallucinations induced by historical noise. To compensate for these deficiencies, the design paradigm of multi-tool systems is shifting from passive execution toward active intervention through two primary approaches. The first approach involves proactive clarification. Frameworks such as AskToAct ( [222](https://arxiv.org/html/2603.22862v2#bib.bib237 "Asktoact: enhancing llms tool use via self-correcting clarification")) exemplify this by dynamically triggering multi-turn clarification mechanisms upon detecting missing parameters. This strategy prevents error accumulation via self-correction and substantially improves both the accuracy and efficiency of tool invocations. The second approach relies on proactive termination to counteract the inherent action compulsion observed in large models. By equipping agents with safety mechanisms to identify uncertainty and autonomously abort execution in high-risk or highly ambiguous environments, systems can achieve substantial security improvements with minimal task completion overhead.

### 7.2. Autonomous tool expansion

When an agent successfully perceives that the existing toolset cannot meet its current needs, the system needs to undergo a paradigm shift from tool user to tool creator. Autonomous tool extension leverages the low-level code generation capabilities or multi-step planning capabilities of large language models to dynamically construct temporary tools or composite skills at runtime, thereby filling capability gaps. A breakthrough in this field lies in decoupling abstract reasoning from concrete execution. The LATM ( [15](https://arxiv.org/html/2603.22862v2#bib.bib241 "Large language models as tool makers")) framework innovatively divides agents into tool creators and tool users. Faced with new tasks, creators generate customized tools by writing Python functions and automatically generate test cases for verification. Once verified, the tools are executed by the user, achieving zero-sample tool creation. The CREATOR ( [134](https://arxiv.org/html/2603.22862v2#bib.bib238 "Creator: tool creation for disentangling abstract and concrete reasoning of large language models")) follows the same logic, transforming abstract problems such as mathematical reasoning and table processing into concrete Python scripts, enabling agents to bypass the limitations of static APIs and autonomously build dynamic computation tools. Besides creating tools from scratch, assembling fine-grained basic tools into high-level composite skills is also an effective path for capability extension. RestGPT ( [156](https://arxiv.org/html/2603.22862v2#bib.bib239 "Restgpt: connecting large language models with real-world applications via restful apis. corr, abs/2306.06624, 2023. doi: 10.48550")) explores how to use large models to plan and connect multiple real RESTful APIs to complete complex long-range tasks, combining isolated network interfaces into super tools with macroscopic semantics. ToolMaker ( [180](https://arxiv.org/html/2603.22862v2#bib.bib240 "Llm agents making agent tools")) further enhances this process. Agents can not only dynamically synthesize tool code to solve specific subtasks, but also reuse these newly created tools within the current context, greatly improving invocation efficiency in multi-round interactions. By using the code interpreter as a Meta-tool, Agents break free from the constraints of predefined interfaces, enabling on-demand dynamic scaling of capabilities.

### 7.3. Open environment adaptation

If boundary awareness and tool expansion address the lack of completeness in a single task, then open environment adaptation aims to solve the evolution problem of multi-tool agents over time. With the iterative updates of external environment API versions, the continuous integration of new tools, and the obsolescence of older tools, agents must possess memory mechanisms and lifelong learning capabilities to accumulate temporarily generated tools or successful call traces into long-term experience ( [228](https://arxiv.org/html/2603.22862v2#bib.bib245 "Lifelong learning of large language model based agents: a roadmap")).

In this field, deeply integrating the agent’s memory architecture with tool calling has become a mainstream trend. Voyager ( [163](https://arxiv.org/html/2603.22862v2#bib.bib242 "Voyager: an open-ended embodied agent with large language models")) first demonstrated this in an open environment. Through continuous exploration and feedback, the agent stores successfully executed code into an ever-expanding skill library, which functions as an external memory based on a vector database. When faced with new challenges, the agent can retrieve and combine historical skills, achieving a leapfrog evolution in tool usage capabilities. The ExpeL ( [226](https://arxiv.org/html/2603.22862v2#bib.bib243 "Expel: llm agents are experiential learners")) framework systematizes the experience learning process. The agent autonomously collects successful or failed tool call traces during training tasks and extracts cross-task insights using natural language, solidifying them into experience memory to effectively avoid repeating mistakes in subsequent API pitfalls.

In the dynamic addition and deletion adaptation of massive tools, ToolkenGPT ( [52](https://arxiv.org/html/2603.22862v2#bib.bib228 "Toolkengpt: augmenting frozen language models with massive tools via tool embeddings")) represents each newly added tool as a special tool token. When facing a new environment, the model only needs to optimize the embedding of these tool tokens, without needing to fine-tune the huge base model, achieving plug-and-play and lightweight adaptation of the tool library. AppAgent ( [215](https://arxiv.org/html/2603.22862v2#bib.bib244 "Appagent: multimodal agents as smartphone users")) demonstrates how, in the highly dynamic graphical interaction environment of smartphones, the agent updates its interaction memory for different apps through continuous exploration and clicks to adapt to UI or application version updates. In summary, by introducing long-term and short-term experience pools and dynamic skill memory, the agent can transform the instantaneous tool creation of an individual into the system’s experience inheritance, ultimately maintaining true functional completeness in an ever-evolving external environment.

## 8\. Benchmarks

The evaluation paradigm for multi-tool agents has undergone a decisive shift: from measuring isolated API invocation correctness to assessing system-level intelligence in sustaining, adapting, and repairing extended tool-use trajectories under structural, temporal, and environmental constraints. This evolution reflects a fundamental recognition—long-horizon tool orchestration is not merely the linear accumulation of atomic calls, but a holistic capability demanding topological reasoning, persistent state management, and dynamic adaptation. Early benchmarks like API-Bank ( [86](https://arxiv.org/html/2603.22862v2#bib.bib61 "Api-bank: a comprehensive benchmark for tool-augmented llms")), MetaTool ( [66](https://arxiv.org/html/2603.22862v2#bib.bib62 "Metatool benchmark for large language models: deciding whether to use tools and which to use")) and ToolBench ( [138](https://arxiv.org/html/2603.22862v2#bib.bib63 "Toolllm: facilitating large language models to master 16000+ real-world apis")) established foundational capabilities in intent detection and tool retrieval; however, contemporary research prioritizes four interdependent dimensions that define long-horizon intelligence of agents: (1) topological complexity of tool dependencies, (2) temporal scale of execution trajectories, (3) environmental dynamism during interaction, and (4) state persistence with self-correction mechanisms.

Table 2. Taxonomy of Long-Horizon Multi-Tool Benchmarks (2023–2026). Benchmarks are categorized by four core dimensions defining long-horizon intelligence. Key metrics include tool space size (Number of Tools), evaluation scale (Number of Instances). Env Type: S=Static Dataset, I=Interactive Simulator, H=Human/Dual-Control, R=Real-World OS/Web.

|     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- |
| Benchmark | \# Tools | \# Instances | Year | Link | Env Type |
| NESTFUL ( [11](https://arxiv.org/html/2603.22862v2#bib.bib64 "Nestful: a benchmark for evaluating llms on nested sequences of api calls")) | 900+ | 1,800+ | 2024 |  | S |
| ToolHop ( [205](https://arxiv.org/html/2603.22862v2#bib.bib65 "ToolHop: a query-driven benchmark for evaluating large language models in multi-hop tool use")) | 3,912 | 995 | 2025 |  | S |
| TRAJECT-Bench ( [57](https://arxiv.org/html/2603.22862v2#bib.bib69 "TRAJECT-bench: a trajectory-aware benchmark for evaluating agentic tool use")) | 1,228 | 5,670 | 2025 |  | I |
| ELT-Bench ( [72](https://arxiv.org/html/2603.22862v2#bib.bib70 "Elt-bench: an end-to-end benchmark for evaluating ai agents on elt pipelines")) | 200 | 100 | 2025 |  | I |
| Toolcomp ( [123](https://arxiv.org/html/2603.22862v2#bib.bib68 "Toolcomp: a multi-tool reasoning & process supervision benchmark")) | 11 | 493 | 2025 |  | S |
| ComplexFuncBench ( [229](https://arxiv.org/html/2603.22862v2#bib.bib66 "ComplexFuncBench: exploring multi-step and constrained function calling under long-context scenario")) | 43 | 1,000 | 2025 |  | S |
| ToolBench ( [138](https://arxiv.org/html/2603.22862v2#bib.bib63 "Toolllm: facilitating large language models to master 16000+ real-world apis")) | 3,451 | 126,486 | 2023 |  | R/I |
| TaskBench ( [150](https://arxiv.org/html/2603.22862v2#bib.bib72 "Taskbench: benchmarking large language models for task automation")) | 103 | 28,271 | 2023 |  | S |
| Seal-Tools ( [184](https://arxiv.org/html/2603.22862v2#bib.bib67 "Seal-tools: self-instruct tool learning dataset for agent tuning and detailed benchmark")) | 4,076 | 14,076 | 2024 |  | S |
| m&m’s ( [117](https://arxiv.org/html/2603.22862v2#bib.bib73 "M & m’s: a benchmark to evaluate tool-use for m ulti-step m ulti-modal tasks")) | 33 | 4,427 | 2024 |  | I |
| FuncBenchGen ( [118](https://arxiv.org/html/2603.22862v2#bib.bib76 "Towards reliable benchmarking: a contamination free, controllable evaluation framework for multi-step llm function calling")) | Varies | Varies | 2025 |  | S |
| M3-Bench ( [232](https://arxiv.org/html/2603.22862v2#bib.bib74 "Mˆ 3-bench: multi-modal, multi-hop, multi-threaded tool-using mllm agent benchmark")) | 231 | 208 | 2025 |  | I |
| MSCoRe ( [82](https://arxiv.org/html/2603.22862v2#bib.bib71 "MSCoRe: a benchmark for multi-stage collaborative reasoning in llm agents")) | Varies | 126k+ | 2025 |  | S |
| MMAU ( [209](https://arxiv.org/html/2603.22862v2#bib.bib75 "Mmau: a holistic benchmark of agent capabilities across diverse domains")) | Varies | 3k+ | 2024 |  | S |
| DICE-BENCH ( [69](https://arxiv.org/html/2603.22862v2#bib.bib77 "DICE-bench: evaluating the tool-use capabilities of large language models in multi-round, multi-party dialogues")) | 124 | 1607 | 2025 |  | S |
| Tool Decathlon ( [85](https://arxiv.org/html/2603.22862v2#bib.bib78 "The tool decathlon: benchmarking language agents for diverse, realistic, and long-horizon task execution")) | 604 | 108 | 2025 |  | R |
| TRIP-Bench ( [151](https://arxiv.org/html/2603.22862v2#bib.bib83 "TRIP-bench: a benchmark for long-horizon interactive agents in real-world scenarios")) | 18 | 40+ | 2026 |  | R |
| UltraHorizon ( [113](https://arxiv.org/html/2603.22862v2#bib.bib82 "Ultrahorizon: benchmarking agent capabilities in ultra long-horizon scenarios")) | 400+ | 168 | 2025 |  | I |
| AgentLongBench ( [39](https://arxiv.org/html/2603.22862v2#bib.bib81 "AgentLongBench: a controllable long benchmark for long-contexts agents via environment rollouts")) | Varies | Varies | 2026 |  | I |
| DeepPlanning ( [224](https://arxiv.org/html/2603.22862v2#bib.bib84 "DeepPlanning: benchmarking long-horizon agentic planning with verifiable constraints")) | 24 | 240 | 2026 |  | I |
| ShortcutsBench ( [147](https://arxiv.org/html/2603.22862v2#bib.bib79 "ShortcutsBench: A large-scale real-world benchmark for api-based agents")) | 1,414 | 7,627 | 2024 |  | R |
| HammerBench ( [169](https://arxiv.org/html/2603.22862v2#bib.bib80 "Hammerbench: fine-grained function-calling evaluation in real mobile assistant scenarios")) | 1,063 | 6,531 | 2024 |  | I |
| τ\\tau-bench ( [202](https://arxiv.org/html/2603.22862v2#bib.bib89 "τ-bench: A benchmark for tool-agent-user interaction in real-world domains")) | 28 | 165 | 2024 |  | H |
| τ2\\tau^{2}-bench ( [10](https://arxiv.org/html/2603.22862v2#bib.bib90 "τ2-bench: evaluating conversational agents in a dual-control environment")) | 68 | 279 | 2025 |  | H |
| ToolSandbox ( [107](https://arxiv.org/html/2603.22862v2#bib.bib85 "Toolsandbox: a stateful, conversational, interactive evaluation benchmark for llm tool use capabilities")) | 34 | 1,032 | 2024 |  | I |
| ToolGym ( [185](https://arxiv.org/html/2603.22862v2#bib.bib87 "ToolGym: an open-world tool-using environment for scalable agent testing and data curation")) | 5,571 | 1,170 | 2026 |  | I |
| VitaBench ( [58](https://arxiv.org/html/2603.22862v2#bib.bib100 "Vitabench: benchmarking llm agents with versatile interactive tasks in real-world applications")) | 66 | 400 | 2025 |  | I |
| OSWorld ( [187](https://arxiv.org/html/2603.22862v2#bib.bib95 "Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments")) | Varies | 369 | 2024 |  | R |
| AppWorld ( [161](https://arxiv.org/html/2603.22862v2#bib.bib86 "Appworld: a controllable world of apps and people for benchmarking interactive coding agents")) | 457 | 750 | 2024 |  | I |
| GTA ( [168](https://arxiv.org/html/2603.22862v2#bib.bib96 "GTA: a benchmark for general tool agents")) | 14 | 229 | 2024 |  | R |
| COMPASS ( [137](https://arxiv.org/html/2603.22862v2#bib.bib93 "COMPASS: a multi-turn benchmark for tool-mediated planning & preference optimization")) | 18 | 281 | 2025 |  | I |
| T1 ( [16](https://arxiv.org/html/2603.22862v2#bib.bib92 "T1: a tool-oriented conversational dataset for multi-turn agentic planning")) | 14 | 13,500 | 2025 |  | S |
| MTU-Bench ( [171](https://arxiv.org/html/2603.22862v2#bib.bib91 "MTU-bench: A multi-granularity tool-use benchmark for large language models")) | 136 | 159k | 2024 |  | S |
| WildToolBench ( [211](https://arxiv.org/html/2603.22862v2#bib.bib94 "Benchmarking LLM tool-use in the wild")) | 1,600 | 1,024 | 2026 |  | S/H |
| Windows Agent Arena ( [14](https://arxiv.org/html/2603.22862v2#bib.bib97 "Windows agent arena: evaluating multi-modal os agents at scale")) | Varies | 150+ | 2024 |  | R |
| Mobile-Bench ( [28](https://arxiv.org/html/2603.22862v2#bib.bib98 "Mobile-bench: an evaluation benchmark for llm-based mobile agents")) | 103 | 832 | 2024 |  | R |
| RealWebAssist ( [208](https://arxiv.org/html/2603.22862v2#bib.bib99 "Realwebassist: a benchmark for long-horizon web assistance with real-world users")) | Varies | 1,885 | 2025 |  | R |
| StableToolBench ( [48](https://arxiv.org/html/2603.22862v2#bib.bib88 "Stabletoolbench-mirrorapi: modeling tool environments as mirrors of 7,000+ real-world apis")) | 16k+ | 126k+ | 2024 |  | I |
| CRITICTOOL ( [64](https://arxiv.org/html/2603.22862v2#bib.bib104 "Critictool: evaluating self-critique capabilities of large language models in tool-calling error scenarios")) | 87 | 2,740 | 2025 |  | S |
| OdysseyBench ( [173](https://arxiv.org/html/2603.22862v2#bib.bib101 "Odysseybench: evaluating llm agents on long-horizon complex office application workflows")) | Office | 602 | 2025 |  | I |
| MemAgentBench ( [61](https://arxiv.org/html/2603.22862v2#bib.bib102 "Evaluating memory in llm agents via incremental multi-turn interactions")) | 289 | 6,340 | 2025 |  | I |
| ColorBench ( [157](https://arxiv.org/html/2603.22862v2#bib.bib103 "ColorBench: benchmarking mobile agents with graph-structured framework for complex long-horizon tasks")) | 21 | 175 | 2025 |  | I |
| ASTRA ( [191](https://arxiv.org/html/2603.22862v2#bib.bib105 "ASTRA-bench: evaluating tool-use agent reasoning and action planning with personal user context")) | Varies | 2,413 | 2026 |  | I |
| RoTBench ( [207](https://arxiv.org/html/2603.22862v2#bib.bib106 "Rotbench: a multi-level benchmark for evaluating the robustness of large language models in tool learning")) | 568 | 105 | 2024 |  | I |
| ToolSword ( [206](https://arxiv.org/html/2603.22862v2#bib.bib107 "Toolsword: unveiling safety issues of large language models in tool learning across three stages")) | 100 | 440 | 2024 |  | I |

### 8.1. Topological Complexity

One line of work examines whether agents can reason over non-linear tool dependencies rather than simply follow sequential scripts. The main challenge is that the correct execution order is determined by latent causal structure: intermediate outputs must be produced, preserved, and passed to later calls under branching, nesting, or multi-hop dependencies. In this setting, failure often arises not from choosing the wrong tool in isolation, but from constructing the wrong dependency graph.

Recent benchmarks expose this issue in several ways. Some emphasize nested and compositional structure, where the output of one call must be embedded into another, sometimes under strict parameter constraints ( [11](https://arxiv.org/html/2603.22862v2#bib.bib64 "Nestful: a benchmark for evaluating llms on nested sequences of api calls"); [184](https://arxiv.org/html/2603.22862v2#bib.bib67 "Seal-tools: self-instruct tool learning dataset for agent tuning and detailed benchmark"); [229](https://arxiv.org/html/2603.22862v2#bib.bib66 "ComplexFuncBench: exploring multi-step and constrained function calling under long-context scenario")). Others evaluate graph-shaped execution, including branching decisions and parallel paths, and require agents to determine which calls can proceed concurrently and which must remain causally ordered ( [57](https://arxiv.org/html/2603.22862v2#bib.bib69 "TRAJECT-bench: a trajectory-aware benchmark for evaluating agentic tool use"); [72](https://arxiv.org/html/2603.22862v2#bib.bib70 "Elt-bench: an end-to-end benchmark for evaluating ai agents on elt pipelines"); [150](https://arxiv.org/html/2603.22862v2#bib.bib72 "Taskbench: benchmarking large language models for task automation")). A further group focuses on distributed information dependencies, where the parameters required for correct execution are scattered across stages, modalities, or speakers ( [82](https://arxiv.org/html/2603.22862v2#bib.bib71 "MSCoRe: a benchmark for multi-stage collaborative reasoning in llm agents"); [117](https://arxiv.org/html/2603.22862v2#bib.bib73 "M & m’s: a benchmark to evaluate tool-use for m ulti-step m ulti-modal tasks"); [69](https://arxiv.org/html/2603.22862v2#bib.bib77 "DICE-bench: evaluating the tool-use capabilities of large language models in multi-round, multi-party dialogues")). Related benchmarks such as M3-Bench, MMAU, and FuncBenchGen further isolate graph reasoning, multimodal dependency tracking, and robustness to structurally valid distractors ( [232](https://arxiv.org/html/2603.22862v2#bib.bib74 "Mˆ 3-bench: multi-modal, multi-hop, multi-threaded tool-using mllm agent benchmark"); [209](https://arxiv.org/html/2603.22862v2#bib.bib75 "Mmau: a holistic benchmark of agent capabilities across diverse domains"); [118](https://arxiv.org/html/2603.22862v2#bib.bib76 "Towards reliable benchmarking: a contamination free, controllable evaluation framework for multi-step llm function calling")).

Taken together, these benchmarks suggest that long-horizon tool use should be evaluated as graph-structured reasoning under execution constraints, rather than as a longer version of single-step tool selection.

### 8.2. Temporal Scale

A second dimension concerns how performance changes as trajectories grow longer. Recent work has moved beyond vague references to long-horizon tasks and instead defines horizon length through approximate step counts, token budgets, or accumulated constraints. These settings reveal a distinct class of failures, including memory decay, context saturation, and the way small local errors can accumulate into global task failure.

The Tool Decathlon ( [85](https://arxiv.org/html/2603.22862v2#bib.bib78 "The tool decathlon: benchmarking language agents for diverse, realistic, and long-horizon task execution")) establishes a baseline for long-horizon evaluation with tasks averaging 20 interactive rounds across diverse domains. ShortcutsBench ( [147](https://arxiv.org/html/2603.22862v2#bib.bib79 "ShortcutsBench: A large-scale real-world benchmark for api-based agents")) tests real-world sequences by mapping multi-stage OS workflows directly to complex parameter loops, bridging the gap between natural language prompts and executable low-code horizons. HammerBench ( [169](https://arxiv.org/html/2603.22862v2#bib.bib80 "Hammerbench: fine-grained function-calling evaluation in real mobile assistant scenarios")) evaluates multi-turn conversation across 10,000 instances, while AgentLongBench ( [39](https://arxiv.org/html/2603.22862v2#bib.bib81 "AgentLongBench: a controllable long benchmark for long-contexts agents via environment rollouts")) scales the temporal horizon dramatically, executing dynamic environment rollouts up to 4 million tokens, demonstrating that models fail precipitously at dynamic information synthesis across extreme horizons.

UltraHorizon ( [113](https://arxiv.org/html/2603.22862v2#bib.bib82 "Ultrahorizon: benchmarking agent capabilities in ultra long-horizon scenarios")) defines the ultra-long-horizon frontier with trajectories averaging 400+ tool calls and 200K+ tokens, rigorously testing context window saturation and memory decay. TRIP-Bench ( [151](https://arxiv.org/html/2603.22862v2#bib.bib83 "TRIP-bench: a benchmark for long-horizon interactive agents in real-world scenarios")) constructs travel planning dialogues exceeding 150 tool invocations with hard constraints (budget, time), exposing planning fragility—where single constraint violations cascade into total failure. This is expanded upon by DeepPlanning ( [224](https://arxiv.org/html/2603.22862v2#bib.bib84 "DeepPlanning: benchmarking long-horizon agentic planning with verifiable constraints")), which forces verifiable global constraint optimization across multiple simulated days of execution, providing controlled evidence that modern agents degrade rapidly when localized reasoning conflicts with long-term budgeting. Critically, these benchmarks show steep degradation as horizon length and global constraints increase, suggesting that temporal scale is a major bottleneck.

### 8.3. Dynamic Environments

Real-world tool use occurs in environments that evolve independently of agent actions. Contemporary benchmarks immerse agents in progressively dynamic settings—from stateful simulators to human-in-the-loop systems—testing adaptation to execution feedback, user corrections, and environmental perturbations.

Stateful Interactive Environments. ToolSandbox ( [107](https://arxiv.org/html/2603.22862v2#bib.bib85 "Toolsandbox: a stateful, conversational, interactive evaluation benchmark for llm tool use capabilities")) provides a stateful conversational environment where intermediate tool outputs alter subsequent state space, requiring agents to track evolving context. AppWorld ( [161](https://arxiv.org/html/2603.22862v2#bib.bib86 "Appworld: a controllable world of apps and people for benchmarking interactive coding agents")) fundamentally shifts the verification paradigm from matching syntactic trajectories to evaluating persistent database state changes across nine heavily interconnected applications, requiring complex interactive coding to mutate a persistent digital world. ToolGym ( [185](https://arxiv.org/html/2603.22862v2#bib.bib87 "ToolGym: an open-world tool-using environment for scalable agent testing and data curation")) injects runtime interruptions to simulate real-world uncertainty, evaluating robustness to environmental volatility. StableToolBench ( [48](https://arxiv.org/html/2603.22862v2#bib.bib88 "Stabletoolbench-mirrorapi: modeling tool environments as mirrors of 7,000+ real-world apis")) addresses evaluation reproducibility by virtualizing APIs with caching layers, isolating agent performance from external API instability.

Human-in-the-Loop Environments.τ\\tau-bench ( [202](https://arxiv.org/html/2603.22862v2#bib.bib89 "τ-bench: A benchmark for tool-agent-user interaction in real-world domains")) and τ2\\tau^{2}-bench ( [10](https://arxiv.org/html/2603.22862v2#bib.bib90 "τ2-bench: evaluating conversational agents in a dual-control environment")) construct high-fidelity user simulators that issue constraint changes, ambiguity requests, and corrections during multi-turn interactions. Critically, τ2\\tau^{2}-bench formalizes a dual-control paradigm where agent and user jointly manipulate a shared world state through tools, requiring agents to negotiate action space and manage user expectations—a capability where even advanced models exhibit ¿40% performance degradation versus single-agent settings. MTU-Bench ( [171](https://arxiv.org/html/2603.22862v2#bib.bib91 "MTU-bench: A multi-granularity tool-use benchmark for large language models")) extends this to multi-turn user guidance scenarios with evolving task specifications. T1 ( [16](https://arxiv.org/html/2603.22862v2#bib.bib92 "T1: a tool-oriented conversational dataset for multi-turn agentic planning")) evaluates multi-turn conversational agents with a focus on inter-tool dependencies and replanning, utilizing an integrated caching mechanism for short and long-term memory. COMPASS ( [137](https://arxiv.org/html/2603.22862v2#bib.bib93 "COMPASS: a multi-turn benchmark for tool-mediated planning & preference optimization")) assesses strategic tool use and user preference optimization in multi-turn travel-planning interactions. Crucially, WildToolBench ( [211](https://arxiv.org/html/2603.22862v2#bib.bib94 "Benchmarking LLM tool-use in the wild")) grounds evaluation in the nature of human behavior, testing agents against implicit intent, instruction transitions, and messy conversational data.

Real-World OS and Web Environments. OSWorld ( [187](https://arxiv.org/html/2603.22862v2#bib.bib95 "Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments")) provides a state-of-the-art interactive computer environment supporting hundreds of open-domain tasks, revealing massive deficiencies in visual GUI grounding. GTA ( [168](https://arxiv.org/html/2603.22862v2#bib.bib96 "GTA: a benchmark for general tool agents")) deploys human-written queries requiring perception and logic tools across real-world multimodal contexts. Windows Agent Arena ( [14](https://arxiv.org/html/2603.22862v2#bib.bib97 "Windows agent arena: evaluating multi-modal os agents at scale")) and Mobile-Bench ( [28](https://arxiv.org/html/2603.22862v2#bib.bib98 "Mobile-bench: an evaluation benchmark for llm-based mobile agents")) evaluate cross-application operations within native GUI environments, where visual noise and UI variability challenge perception-action loops. RealWebAssist ( [208](https://arxiv.org/html/2603.22862v2#bib.bib99 "Realwebassist: a benchmark for long-horizon web assistance with real-world users")) uses authentic human-recorded web navigation trajectories to assess agents’ ability to interpret implicit user intent from sequential actions. VitaBench ( [58](https://arxiv.org/html/2603.22862v2#bib.bib100 "Vitabench: benchmarking llm agents with versatile interactive tasks in real-world applications")) targets diverse real-world applications with heterogeneous tool interfaces, emphasizing adaptation to domain-specific interaction patterns.

### 8.4. State Persistence and Self-Correction

Sustaining extended trajectories demands not only planning but also mechanisms for state persistence and error recovery. In many practical workflows, success depends on maintaining intermediate artifacts, remembering prior commitments, and detecting when the current trajectory has drifted away from task requirements. Benchmarks along this axis therefore examine not only final success, but also whether the agent can recover from partial failure.

Some benchmarks focus on persistent state management, asking agents to maintain intermediate resources or task variables across extended execution traces ( [107](https://arxiv.org/html/2603.22862v2#bib.bib85 "Toolsandbox: a stateful, conversational, interactive evaluation benchmark for llm tool use capabilities"); [161](https://arxiv.org/html/2603.22862v2#bib.bib86 "Appworld: a controllable world of apps and people for benchmarking interactive coding agents"); [232](https://arxiv.org/html/2603.22862v2#bib.bib74 "Mˆ 3-bench: multi-modal, multi-hop, multi-threaded tool-using mllm agent benchmark")). Others explicitly target self-correction and recovery, where agents must identify inconsistencies, revise previous actions, and continue toward task completion rather than restart from scratch ( [10](https://arxiv.org/html/2603.22862v2#bib.bib90 "τ2-bench: evaluating conversational agents in a dual-control environment"); [16](https://arxiv.org/html/2603.22862v2#bib.bib92 "T1: a tool-oriented conversational dataset for multi-turn agentic planning"); [211](https://arxiv.org/html/2603.22862v2#bib.bib94 "Benchmarking LLM tool-use in the wild")). Closely related evaluations also treat process supervision as a first-class target, measuring whether the agent followed a valid path even when the final outcome appears acceptable ( [123](https://arxiv.org/html/2603.22862v2#bib.bib68 "Toolcomp: a multi-tool reasoning & process supervision benchmark"); [229](https://arxiv.org/html/2603.22862v2#bib.bib66 "ComplexFuncBench: exploring multi-step and constrained function calling under long-context scenario")).

This line of work highlights an important methodological point: long-horizon evaluation should not rely solely on endpoint success. For multi-tool systems, the more informative question is often whether a benchmark isolates a specific failure mode, exposes the relevant intermediate signals, and distinguishes between accidental success and genuinely robust orchestration.

## 9\. Application

Following the analysis of reasoning, training, and core system properties, this chapter examines multi-tool LLM agent deployment in industrial settings. The primary challenge extends beyond basic tool invocation to achieving end-to-end objectives under practical engineering constraints. Since real-world workloads feature heterogeneous components and evolving states, execution strategies must seamlessly manage tool errors and distribution shifts. Consequently, effective deployment demands closed-loop orchestration based on continuous iterative execution, coupled with strict verification of all intermediate and final outcomes.

This approach builds upon neuro-symbolic architectures that enhance language models with external knowledge and discrete reasoning. Recent research integrating reasoning with actions highlights the necessity of interactive execution and systematic exception handling, while scalable tool-use learning has driven protocols that better reflect complex industrial realities. Consequently, rather than providing a domain-centric inventory, this chapter analyzes diverse applications as concrete instances of multi-tool orchestration. By characterizing specific tool ecosystems and abstracting their orchestration patterns, we examine methodologies for selecting, composing, and validating tool invocations. This approach highlights trade-offs among reliability, safety, and cost, establishing a unified framework to compare industrial practices.

### 9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration

![Refer to caption](https://arxiv.org/html/2603.22862v2/x4.png)Figure 5. A unified abstraction of application-side multi-tool orchestration. Real-world agent systems operate over heterogeneous environments, instantiate different orchestration topologies, and rely on iterative plan-act-observe-revise loops under verification, safety, and cost constraints.

A unified abstraction for multi-tool orchestration frames tasks as executable processes driving an external system toward a target state. As summarized in Figure [5](https://arxiv.org/html/2603.22862v2#S9.F5 "Figure 5 ‣ 9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"), this perspective organizes application-side orchestration into execution environments, topologies, closed-loop control, and operational constraints. Within real operating systems and web environments, tool use and low-level interface operations are subsumed into a unified sequential decision-making problem. Orchestrating these applications necessitates explicitly modeling the observation-action-state transition loop to capture the tight coupling of visual cues and actions in multimodal contexts ( [187](https://arxiv.org/html/2603.22862v2#bib.bib95 "Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments"); [79](https://arxiv.org/html/2603.22862v2#bib.bib108 "Visualwebarena: evaluating multimodal agents on realistic visual web tasks")). Concurrently, growing evidence suggests that action grounding, rather than high-level planning, is the primary execution bottleneck. Robust performance in vision-language models relies on accurately mapping natural language intents to actionable interface elements and pixel-level regions to maintain stable tool pipelines ( [199](https://arxiv.org/html/2603.22862v2#bib.bib109 "Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v")). Advancing this direction, general-purpose visual grounding solutions such as UGround ( [44](https://arxiv.org/html/2603.22862v2#bib.bib110 "Navigating the digital world as humans do: universal visual grounding for GUI agents")) improve graphical user interface agent accuracy across varying resolutions and heterogeneous elements.

Beyond individual action grounding, orchestrating these operations into extended tool chains introduces strict systems-level engineering constraints. As workflows scale, critical vulnerabilities emerge in state management, parameter binding, and variable passing across pipeline topologies ( [205](https://arxiv.org/html/2603.22862v2#bib.bib65 "ToolHop: a query-driven benchmark for evaluating large language models in multi-hop tool use"); [11](https://arxiv.org/html/2603.22862v2#bib.bib64 "Nestful: a benchmark for evaluating llms on nested sequences of api calls")). Maintaining stable execution under these implicit constraints requires integrating rigorous process supervision, treating invocation path correctness as a primary objective rather than a mere byproduct of terminal success ( [229](https://arxiv.org/html/2603.22862v2#bib.bib66 "ComplexFuncBench: exploring multi-step and constrained function calling under long-context scenario"); [123](https://arxiv.org/html/2603.22862v2#bib.bib68 "Toolcomp: a multi-tool reasoning & process supervision benchmark")). Furthermore, real-world deployments must manage highly heterogeneous ecosystems via standardized protocols to process continuous online feedback ( [176](https://arxiv.org/html/2603.22862v2#bib.bib111 "MCP-bench: benchmarking tool-using llm agents with complex real-world tasks via mcp servers")). Crucially, as agents utilize powerful read and write primitives, security transitions into a foundational requirement; orchestration frameworks must proactively prevent unauthorized access and mitigate high-risk operations without compromising task completion ( [84](https://arxiv.org/html/2603.22862v2#bib.bib112 "ST-webagentbench: a benchmark for evaluating safety and trustworthiness in web agents")).

Motivated by these dynamics, the remainder of this chapter analyzes representative domains by focusing on the sources of dominant operational constraints, such as state verification, rollback mechanisms, and access control. Rather than re-evaluating previously established structural configurations, the subsequent analysis investigates how these strict operational boundaries directly dictate application-side orchestration strategies and necessitate robust engineering implementations across diverse industrial ecosystems. Ultimately, this chapter conceptualizes application orchestration through two complementary abstractions: executable tasks within interactive environments and execution workflows governed by explicit control flow. Building upon this framework, Section 9.2 categorizes application scenarios by their deployment environments to compare operational demands across tool sets, verification mechanisms, and stringent safety constraints, translating tool integration from a theoretical algorithmic capability into actionable workflow design.

### 9.2. Orchestration Paradigms in Representative Interactive Environments

This section analyzes multi-tool orchestration across diverse interactive environments, focusing on how stringent system constraints dictate execution policies. In graphical environments, managing non-stationary interfaces and visual grounding poses a significantly greater bottleneck than high-level planning ( [54](https://arxiv.org/html/2603.22862v2#bib.bib113 "Webvoyager: building an end-to-end web agent with large multimodal models"); [125](https://arxiv.org/html/2603.22862v2#bib.bib115 "ScreenAgent: a vision language model-driven computer control agent")). Orchestrating these multimodal loops requires prioritizing engineered representations and stable state transitions to handle user interface volatility and operational latency effectively ( [227](https://arxiv.org/html/2603.22862v2#bib.bib114 "Gpt-4v (ision) is a generalist web agent, if grounded"); [3](https://arxiv.org/html/2603.22862v2#bib.bib116 "Agent-e: from autonomous web navigation to foundational design principles in agentic systems"); [200](https://arxiv.org/html/2603.22862v2#bib.bib117 "AgentOccam: a simple yet strong baseline for llm-based web agents"); [109](https://arxiv.org/html/2603.22862v2#bib.bib118 "WebLINX: real-world website navigation with multi-turn dialogue"); [2](https://arxiv.org/html/2603.22862v2#bib.bib119 "OSWorld-human: benchmarking the efficiency of computer-use agents")).

Conversely, software engineering demands rigorous execution loops where success is strictly grounded in deterministic tests ( [27](https://arxiv.org/html/2603.22862v2#bib.bib120 "Introducing SWE-bench verified"); [210](https://arxiv.org/html/2603.22862v2#bib.bib121 "UTBoost: rigorous evaluation of coding agents on SWE-bench")). The primary deployment bottleneck shifts from isolated code synthesis to the complex coupling of context retrieval, patch generation, and computationally expensive test verification ( [186](https://arxiv.org/html/2603.22862v2#bib.bib122 "Agentless: demystifying LLM-based software engineering agents"); [103](https://arxiv.org/html/2603.22862v2#bib.bib123 "RepoBench: benchmarking repository-level code auto-completion systems"); [7](https://arxiv.org/html/2603.22862v2#bib.bib124 "Unified software engineering agent as ai software engineer"); [141](https://arxiv.org/html/2603.22862v2#bib.bib125 "Swe-polybench: a multi-language benchmark for repository level evaluation of coding agents")). To mitigate these high verification costs, systems-level optimizations including tool parallelization, intelligent caching, and overlapping language model decoding with partial tool execution become critical for maximizing throughput and minimizing end-to-end latency ( [196](https://arxiv.org/html/2603.22862v2#bib.bib126 "Conveyor: efficient tool-aware llm serving with tool partial execution")).

Enterprise orchestration manifests as continuous transactional workflows encompassing retrieval, analysis, execution, and write-back operations across distributed systems ( [35](https://arxiv.org/html/2603.22862v2#bib.bib127 "Workarena: how capable are web agents at solving common knowledge work tasks?"); [13](https://arxiv.org/html/2603.22862v2#bib.bib128 "Workarena++: towards compositional planning and reasoning-based common knowledge work tasks")). The primary engineering bottlenecks are state maintenance and transactional consistency under long-context constraints ( [81](https://arxiv.org/html/2603.22862v2#bib.bib129 "Spider 2.0: evaluating language models on real-world enterprise text-to-sql workflows")). Consequently, enterprise deployment necessitates rigorous constraint systematization, elevating auditing, permission boundaries, and cost budgets to primary design variables. Agents must justify invocations, log execution trajectories for compliance, and utilize audit logs as verifiable completion signals ( [50](https://arxiv.org/html/2603.22862v2#bib.bib130 "World of workflows: a benchmark for bringing world models to enterprise systems"); [181](https://arxiv.org/html/2603.22862v2#bib.bib131 "Top of the class: benchmarking llm agents on real-world enterprise tasks")).

Conversely, mobile environments represent extreme open ecosystems requiring complex cross-application coordination under severe physical and system-level interference ( [170](https://arxiv.org/html/2603.22862v2#bib.bib132 "MobileAgentBench: an efficient and user-friendly benchmark for mobile llm agents"); [188](https://arxiv.org/html/2603.22862v2#bib.bib133 "Understanding the weakness of large language model agents within a complex android environment"); [197](https://arxiv.org/html/2603.22862v2#bib.bib134 "AndroidLab: training and systematic benchmarking of android autonomous agents")). Given the high risks of destructive misoperations in these dynamic multimodal settings, orchestration inherently demands explicit user confirmation points, continuous final state validation, and highly conservative recovery strategies rather than autonomous retries ( [194](https://arxiv.org/html/2603.22862v2#bib.bib135 "Mobile-bench-v2: a more realistic and comprehensive benchmark for vlm-based mobile agents"); [5](https://arxiv.org/html/2603.22862v2#bib.bib136 "UINavBench: a framework for comprehensive evaluation of interactive digital agents")).

Across these diverse environments, domain distinctions arise primarily from unique operational bottlenecks rather than structural topologies. Engineering challenges range from high verification costs in software development and interface drift in mobile ecosystems to strict regulatory compliance in enterprise workflows. Grounded in this unified operational perspective, the subsequent section investigates essential industrial deployment factors including tool governance, continuous observability, and strict cost-latency budget management.

### 9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration

Industrial deployment necessitates rigorous tool ecosystem governance, as unstable API availability often causes irreproducible pipeline drift, making virtualization and regression validation architectural imperatives ( [49](https://arxiv.org/html/2603.22862v2#bib.bib137 "Stabletoolbench: towards stable large-scale benchmarking on tool learning of large language models")). To manage heterogeneous access, standardized protocols mitigate integration costs ( [120](https://arxiv.org/html/2603.22862v2#bib.bib138 "Model context protocol (mcp) specification"); [68](https://arxiv.org/html/2603.22862v2#bib.bib139 "Introducing the model context protocol")), demanding fully auditable systems with strict semantic contracts and graceful degradation ( [176](https://arxiv.org/html/2603.22862v2#bib.bib111 "MCP-bench: benchmarking tool-using llm agents with complex real-world tasks via mcp servers")). Concurrently, mitigating critical vulnerabilities like indirect prompt injections ( [214](https://arxiv.org/html/2603.22862v2#bib.bib140 "InjecAgent: benchmarking indirect prompt injections in tool-integrated large language model agents")) requires externalizing safety to dedicated policy layers that enforce input/output sanitization ( [84](https://arxiv.org/html/2603.22862v2#bib.bib112 "ST-webagentbench: a benchmark for evaluating safety and trustworthiness in web agents")). Aligning with standards such as the OWASP Top 10 ( [127](https://arxiv.org/html/2603.22862v2#bib.bib141 "OWASP top 10 for large language model applications (v2025)")) and NIST guidelines ( [8](https://arxiv.org/html/2603.22862v2#bib.bib142 "Artificial intelligence risk management framework: generative artificial intelligence profile")), architectures must embed least-privilege access, environment partitioning, and comprehensive logging within the execution loop to guarantee non-repudiable auditability and secure invocations.

Beyond security, arresting error cascades during execution demands intermediate checkpoints for decidable verification ( [187](https://arxiv.org/html/2603.22862v2#bib.bib95 "Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments")) and comprehensive observability that evaluates process-level constraint satisfaction rather than mere terminal completion ( [33](https://arxiv.org/html/2603.22862v2#bib.bib143 "AgentOps: enabling observability of llm agents"); [6](https://arxiv.org/html/2603.22862v2#bib.bib144 "Beyond task completion: an assessment framework for evaluating agentic ai systems")). Post-deployment, these pipelines must adhere to strict service level agreements and budgets. Because end-to-end latency is heavily dominated by planning cycles ( [2](https://arxiv.org/html/2603.22862v2#bib.bib119 "OSWorld-human: benchmarking the efficiency of computer-use agents")), robust orchestration requires the joint optimization of quality, time, and cost. Current research addresses this through interface compression to reduce token overhead ( [75](https://arxiv.org/html/2603.22862v2#bib.bib145 "FocusAgent: simple yet effective ways of trimming the large context of web agents"); [200](https://arxiv.org/html/2603.22862v2#bib.bib117 "AgentOccam: a simple yet strong baseline for llm-based web agents")), decoupling reasoning from execution ( [192](https://arxiv.org/html/2603.22862v2#bib.bib222 "Rewoo: decoupling reasoning from observations for efficient augmented language models")), and budget-aware routing to dynamically allocate resources to high-uncertainty tasks ( [21](https://arxiv.org/html/2603.22862v2#bib.bib229 "Frugalgpt: how to use large language models while reducing cost and improving performance")).

Ultimately, industrial orchestration requires comprehensive systems-level remodeling rather than merely scaling research prototypes. The fundamental challenge lies in directly embedding these operational constraints—spanning governance, safety, verification, and efficiency—into the underlying infrastructure. Because industrial competitiveness heavily relies on capabilities like automated regression and executable acceptance testing, the subsequent section explores open research problems specifically targeting robust interface evolution, verifiability boundaries, and cost-effective long-horizon planning.

### 9.4. Open Problems and Future Directions

Although multi-tool LLM agents demonstrate encouraging generality, transitioning them from usable prototypes to trusted production systems requires addressing several critical application-side gaps: mitigating behavioral drift caused by continuous interface evolution via adaptive regression mechanisms; establishing process-level verifiability and replayable audits for long-horizon orchestration without prohibitive efficiency loss; developing systematic methodologies to jointly optimize cost, latency, and quality under strict budget constraints; and replacing heuristic failure recovery with composable, adversarial-resistant recovery frameworks. Ultimately, addressing these challenges demands a unified research agenda centered on evolvable tool governance, verifiable closed-loop execution, and adaptive orchestration to ensure these agents can be safely and reliably deployed in demanding professional environments.

## 10\. Conclusion

The development of tool use in LLM agents reflects a broader shift in the field, from isolated function invocation to sustained interaction with complex external systems. Once agents must coordinate multiple tools over long horizons, the problem is no longer only about prompting or API formatting. It also involves planning under dependencies, managing mutable state, controlling execution, and preserving correctness under uncertainty, latency, and safety constraints. This is why progress depends not only on stronger base models, but also on advances in memory, orchestration, verification, and benchmark design. This survey has reviewed work on multi-tool agents across inference-time planning, training, safety, efficiency, capability completeness, benchmarks, and applications. A central observation is that these dimensions are tightly connected. Planning interacts with state management and verifiability. Safety depends on execution control and isolation. Efficiency depends on decomposition, routing, and reuse. Looking ahead, the field needs better abstractions for stateful orchestration, stronger evaluation protocols for dynamic and long-horizon settings, and closer integration between model-level reasoning and system-level guarantees. Progress on these fronts will be necessary if multi-tool agents are to move from promising prototypes to dependable, auditable, and scalable systems for real-world use.

## References

- \[1\]I. Abdelaziz, K. Basu, M. Agarwal, S. Kumaravel, M. Stallone, R. Panda, Y. Rizk, G. S. Bhargav, M. Crouse, C. Gunasekara, et al. (2024)Granite-function calling model: introducing function calling abilities via multi-task learning of granular tasks.
In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing: Industry Track,
pp. 1131–1139.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p2.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[2\]R. Abhyankar, Q. Qi, and Y. Zhang (2025)OSWorld-human: benchmarking the efficiency of computer-use agents.
arXiv preprint arXiv:2506.16042.
External Links: [Link](https://arxiv.org/abs/2506.16042 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[3\]T. Abuelsaad, D. Akkil, P. Dey, A. Jagmohan, A. Vempaty, R. Kokku, and R. Azam (2024)Agent-e: from autonomous web navigation to foundational design principles in agentic systems.
arXiv preprint arXiv:2407.13032.
External Links: [Link](https://arxiv.org/abs/2407.13032 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[4\]M. Agarwal, I. Abdelaziz, K. Basu, M. Unuvar, L. A. Lastras, Y. Rizk, and P. Kapanipathi (2025)Toolrm: outcome reward models for tool-calling large language models.
arXiv preprint arXiv:2509.11963.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p2.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[5\]H. Agrawal, E. Schoop, X. Pan, A. Mahajan, A. Seff, D. Feng, R. Cheng, A. R. M. Y. Teran, E. Gomez, A. Sundararajan, et al. (2025)UINavBench: a framework for comprehensive evaluation of interactive digital agents.
In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 23353–23363.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p4.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[6\]S. Akshathala, B. Adnan, M. Ramesh, K. Vaidhyanathan, B. Muhammed, and K. Parthasarathy (2025)Beyond task completion: an assessment framework for evaluating agentic ai systems.
arXiv preprint arXiv:2512.12791.
External Links: [Link](https://arxiv.org/abs/2512.12791 "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[7\]L. Applis, Y. Zhang, S. Liang, N. Jiang, L. Tan, and A. Roychoudhury (2025)Unified software engineering agent as ai software engineer.
arXiv preprint arXiv:2506.14683.
External Links: [Link](https://arxiv.org/abs/2506.14683 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[8\] (2024)Artificial intelligence risk management framework: generative artificial intelligence profile.
Technical reportTechnical Report NIST AI 600-1, National Institute of Standards and Technology.
External Links: [Link](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[9\]F. Bang (2023)Gptcache: an open-source semantic cache for llm applications enabling faster answers and cost savings.
In Proceedings of the 3rd Workshop for Natural Language Processing Open Source Software (NLP-OSS 2023),
pp. 212–218.
Cited by: [§6.2.3](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS3.p1.1 "6.2.3. Intelligent caching and memory ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[10\]V. Barres, H. Dong, S. Ray, X. Si, and K. Narasimhan (2025)τ\\tau2{}^{\\mbox{2}}-bench: evaluating conversational agents in a dual-control environment.
CoRRabs/2506.07982.
External Links: [Link](https://doi.org/10.48550/arXiv.2506.07982 ""),
[Document](https://dx.doi.org/10.48550/ARXIV.2506.07982 ""),
2506.07982Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.3.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[11\]K. Basu, I. Abdelaziz, K. Kate, M. Agarwal, M. Crouse, Y. Rizk, K. Bradford, A. Munawar, S. Kumaravel, S. Goyal, et al. (2025)Nestful: a benchmark for evaluating llms on nested sequences of api calls.
In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pp. 33526–33535.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.5.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[12\]L. Beurer-Kellner, B. Buesser, A. Creţu, E. Debenedetti, D. Dobos, D. Fabian, M. Fischer, D. Froelicher, K. Grosse, D. Naeff, et al. (2025)Design patterns for securing llm agents against prompt injections.
arXiv preprint arXiv:2506.08837.
Cited by: [§5](https://arxiv.org/html/2603.22862v2#S5.p1.1 "5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[13\]L. Boisvert, M. Thakkar, M. Gasse, M. Caccia, T. L. De Chezelles, Q. Cappart, N. Chapados, A. Lacoste, and A. Drouin (2024)Workarena++: towards compositional planning and reasoning-based common knowledge work tasks.
Advances in Neural Information Processing Systems37,  pp. 5996–6051.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p3.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[14\]R. Bonatti, D. Zhao, F. Bonacci, D. Dupont, S. Abdali, Y. Li, Y. Lu, J. Wagle, K. Koishida, A. Bucker, et al. (2024)Windows agent arena: evaluating multi-modal os agents at scale.
arXiv preprint arXiv:2409.08264.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.36.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[15\]T. Cai, X. Wang, T. Ma, X. Chen, and D. Zhou (2023)Large language models as tool makers.
arXiv preprint arXiv:2305.17126.
Cited by: [§7.2](https://arxiv.org/html/2603.22862v2#S7.SS2.p1.1 "7.2. Autonomous tool expansion ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§7](https://arxiv.org/html/2603.22862v2#S7.p1.1 "7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[16\]A. Chakraborty, P. Dashore, N. Bathaee, A. Jain, A. Das, S. Zhang, S. Sahu, M. Naphade, and G. I. Winata (2025)T1: a tool-oriented conversational dataset for multi-turn agentic planning.
Advances in Neural Information Processing Systems.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.33.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[17\]E. Y. Chang and L. Geng (2025)SagaLLM: context management, validation, and transaction guarantees for multi-agent llm planning.
arXiv preprint arXiv:2503.11951.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p2.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p5.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.3.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[18\]E. Y. Chang (2025)Maci: multi-agent collaborative intelligence for adaptive reasoning and temporal planning.
arXiv preprint arXiv:2501.16689.
Cited by: [§6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2.p1.1 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[19\]G. Chen, Z. Qiao, W. Wang, D. Yu, X. Chen, H. Sun, M. Liao, K. Fan, Y. Jiang, P. Xie, W. X. Zhao, R. Song, and F. Huang (2026)MARS: co-evolving dual-system deep research via multi-agent reinforcement learning.
External Links: 2510.04935,
[Link](https://arxiv.org/abs/2510.04935 "")Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p2.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[20\]J. Chen, J. Liang, and B. Wang (2025)Smurfs: multi-agent system using context-efficient dfsdt for tool planning.
In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
pp. 3281–3298.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[21\]L. Chen, M. Zaharia, and J. Zou (2023)Frugalgpt: how to use large language models while reducing cost and improving performance.
arXiv preprint arXiv:2305.05176.
Cited by: [§6.2.2](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS2.p1.1 "6.2.2. Adaptive Model Routing ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[22\]M. Chen, H. Sun, T. Li, F. Yang, H. Liang, K. Lu, B. Cui, W. Zhang, Z. Zhou, and W. Chen (2024)Facilitating multi-turn function calling for llms via compositional instruction tuning.
arXiv preprint arXiv:2410.12952.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p2.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[23\]S. Chen, Y. Liu, W. Han, W. Zhang, and T. Liu (2024)A survey on llm-based multi-agent system: recent advances and new frontiers in application.
arXiv preprint arXiv:2412.17481.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[24\]S. Chen, Z. Li, Z. Han, B. He, T. Liu, H. Chen, G. Groh, P. Torr, V. Tresp, and J. Gu (2025)Deep research brings deeper harm.
arXiv preprint arXiv:2510.11851.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p2.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[25\]Y. Chen, J. Yoon, D. S. Sachan, Q. Wang, V. Cohen-Addad, M. Bateni, C. Lee, and T. Pfister (2024)Re-invoke: tool invocation rewriting for zero-shot tool retrieval.
In Findings of the Association for Computational Linguistics: EMNLP 2024,
pp. 4705–4726.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[26\]M. Cheng, J. Ouyang, S. Yu, R. Yan, Y. Luo, Z. Liu, D. Wang, Q. Liu, and E. Chen (2025)Agent-r1: training powerful llm agents with end-to-end reinforcement learning.
arXiv preprint arXiv:2511.14460.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p4.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[27\]N. Chowdhury, J. Aung, C. J. Shern, O. Jaffe, D. Sherburn, G. Starace, E. Mays, R. Dias, M. Aljubeh, M. Glaese, C. E. Jimenez, J. Yang, L. Ho, T. Patwardhan, K. Liu, and A. Madry (2024)Introducing SWE-bench verified.
External Links: [Link](https://openai.com/index/introducing-swe-bench-verified/ "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[28\]S. Deng, W. Xu, H. Sun, W. Liu, T. Tan, L. Liujianfeng, A. Li, J. Luan, B. Wang, R. Yan, et al. (2024)Mobile-bench: an evaluation benchmark for llm-based mobile agents.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 8813–8831.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.37.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[29\]Y. Deng, S. Fan, N. Wang, X. Zhao, and S. K. Ng (2025)AgentPro: enhancing llm agents with automated process supervision.
In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pp. 9992–10017.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[30\]Y. Ding, H. Le, S. Han, K. Ruan, Z. Jin, V. Kumar, Z. Wang, and A. Deoras (2025)Empowering multi-turn tool-integrated reasoning with group turn policy optimization.
arXiv preprint arXiv:2511.14846.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p3.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[31\]G. Dong, Y. Chen, X. Li, J. Jin, H. Qian, Y. Zhu, H. Mao, G. Zhou, Z. Dou, and J. Wen (2025)Tool-star: empowering llm-brained multi-tool reasoner via reinforcement learning.
arXiv preprint arXiv:2505.16410.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p2.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[32\]G. Dong, H. Mao, K. Ma, L. Bao, Y. Chen, Z. Wang, Z. Chen, J. Du, H. Wang, F. Zhang, et al. (2025)Agentic reinforced policy optimization.
arXiv preprint arXiv:2507.19849.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p3.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[33\]L. Dong, Q. Lu, and L. Zhu (2024)AgentOps: enabling observability of llm agents.
arXiv preprint arXiv:2411.05285.
External Links: [Link](https://arxiv.org/abs/2411.05285 "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[34\]S. Dong, S. Xu, P. He, Y. Li, J. Tang, T. Liu, H. Liu, and Z. Xiang (2025)Memory injection attacks on llm agents via query-only interaction.
arXiv preprint arXiv:2503.03704.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p2.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.5.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[35\]A. Drouin, M. Gasse, M. Caccia, I. H. Laradji, M. Del Verme, T. Marty, L. Boisvert, M. Thakkar, Q. Cappart, D. Vazquez, et al. (2024)Workarena: how capable are web agents at solving common knowledge work tasks?.
arXiv preprint arXiv:2403.07718.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p3.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[36\]Y. Du, F. Wei, and H. Zhang (2024)Anytool: self-reflective, hierarchical agents for large-scale api calls.
arXiv preprint arXiv:2402.04253.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.2.1](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS1.p1.1 "6.2.1. Dynamic tool search ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[37\]L. E. Erdogan, N. Lee, S. Kim, S. Moon, H. Furuta, G. Anumanchipalli, K. Keutzer, and A. Gholami (2025)Plan-and-act: improving planning of agents for long-horizon tasks.
arXiv preprint arXiv:2503.09572.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[38\]H. Errico (2026)Autonomous action runtime management (aarm): a system specification for securing ai-driven actions at runtime.
arXiv preprint arXiv:2602.09433.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p4.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.2.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[39\]S. Fang, Y. Wang, X. Liu, J. Lu, C. Tan, X. Chen, Y. Zheng, X. Huang, and X. Qiu (2026)AgentLongBench: a controllable long benchmark for long-contexts agents via environment rollouts.
arXiv preprint arXiv:2601.20730.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p2.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.22.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[40\]W. Fang, Y. Zhang, K. Qian, J. Glass, and Y. Zhu (2025)Play2prompt: zero-shot tool instruction optimization for llm agents via tool play.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 26274–26290.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[41\]X. Fei, X. Zheng, and H. Feng (2025)Mcp-zero: active tool discovery for autonomous llm agents.
arXiv preprint arXiv:2506.01056.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[42\]S. Forouzandeh, W. Peng, P. Moradi, X. Yu, and M. Jalili (2025)Learning hierarchical procedural memory for llm agents through bayesian selection and contrastive refinement.
arXiv preprint arXiv:2512.18950.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p2.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[43\]S. Gao, J. Dwivedi-Yu, P. Yu, X. E. Tan, R. Pasunuru, O. Golovneva, K. Sinha, A. Celikyilmaz, A. Bosselut, and T. Wang (2025)Efficient tool use with chain-of-abstraction reasoning.
In Proceedings of the 31st International Conference on Computational Linguistics,
pp. 2727–2743.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p2.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[44\]B. Gou, R. Wang, B. Zheng, Y. Xie, C. Chang, Y. Shu, H. Sun, and Y. Su (2025)Navigating the digital world as humans do: universal visual grounding for GUI agents.
In International Conference on Learning Representations,
External Links: [Link](https://openreview.net/forum?id=kxnoqaisCT "")Cited by: [§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p1.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[45\]Z. Gou, Z. Shao, Y. Gong, Y. Shen, Y. Yang, N. Duan, and W. Chen (2023)Critic: large language models can self-correct with tool-interactive critiquing.
arXiv preprint arXiv:2305.11738.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p6.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.4.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[46\]K. Greshake, S. Abdelnabi, S. Mishra, C. Endres, T. Holz, and M. Fritz (2023)Not what you’ve signed up for: compromising real-world llm-integrated applications with indirect prompt injection.
In Proceedings of the 16th ACM workshop on artificial intelligence and security,
pp. 79–90.
Cited by: [§5](https://arxiv.org/html/2603.22862v2#S5.p1.1 "5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[47\]S. Guo, O. D. Domingues, R. Avalos, A. Courville, and F. Strub (2025)Sample, predict, then proceed: self-verification sampling for tool use of llms.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p4.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[48\]Z. Guo, S. Cheng, Y. Niu, H. Wang, S. Zhou, W. Huang, and Y. Liu (2025)Stabletoolbench-mirrorapi: modeling tool environments as mirrors of 7,000+ real-world apis.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 5247–5270.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p3.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p2.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.39.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[49\]Z. Guo, S. Cheng, H. Wang, S. Liang, Y. Qin, P. Li, Z. Liu, M. Sun, and Y. Liu (2024)Stabletoolbench: towards stable large-scale benchmarking on tool learning of large language models.
In Findings of the Association for Computational Linguistics: ACL 2024,
pp. 11143–11156.
Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[50\]L. Gupta, L. Li, Y. Liu, S. G. Subramanian, K. Suleman, Z. Zhang, H. Lu, and S. Pasupalak (2026)World of workflows: a benchmark for bringing world models to enterprise systems.
arXiv preprint arXiv:2601.22130.
External Links: [Link](https://arxiv.org/abs/2601.22130 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p3.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[51\]J. Han, W. Buntine, and E. Shareghi (2025)Verifiagent: a unified verification agent in language model reasoning.
ArXiv preprint, abs/2504.00406.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p6.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.4.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[52\]S. Hao, T. Liu, Z. Wang, and Z. Hu (2023)Toolkengpt: augmenting frozen language models with massive tools via tool embeddings.
Advances in neural information processing systems36,  pp. 45870–45894.
Cited by: [§6.2.1](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS1.p1.1 "6.2.1. Dynamic tool search ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§7.3](https://arxiv.org/html/2603.22862v2#S7.SS3.p3.1 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[53\]F. He, T. Zhu, D. Ye, B. Liu, W. Zhou, and P. S. Yu (2025)The emerged security and privacy of llm agent: a survey with case studies.
ACM Computing Surveys58 (6),  pp. 1–36.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§5](https://arxiv.org/html/2603.22862v2#S5.p1.1 "5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[54\]H. He, W. Yao, K. Ma, W. Yu, Y. Dai, H. Zhang, Z. Lan, and D. Yu (2024)Webvoyager: building an end-to-end web agent with large multimodal models.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 6864–6890.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[55\]J. He, J. Neville, M. Wan, L. Yang, H. Liu, X. Xu, X. Song, J. Z. Pan, and P. Zhou (2025)GenTool: enhancing tool generalization in language models through zero-to-one and weak-to-strong simulation.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 1097–1122.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[56\]K. He and K. Roy (2026)SWE-adept: an llm-based agentic framework for deep codebase analysis and structured issue resolution.
arXiv preprint arXiv:2603.01327.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p3.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[57\]P. He, Z. Dai, B. He, H. Liu, X. Tang, H. Lu, J. Li, J. Ding, S. Mukherjee, S. Wang, et al. (2025)TRAJECT-bench: a trajectory-aware benchmark for evaluating agentic tool use.
arXiv preprint arXiv:2510.04550.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.7.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[58\]W. He, Y. Sun, H. Hao, X. Hao, Z. Xia, Q. Gu, C. Han, D. Zhao, H. Su, K. Zhang, et al. (2025)Vitabench: benchmarking llm agents with versatile interactive tasks in real-world applications.
arXiv preprint arXiv:2509.26490.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.28.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[59\]Z. He, Z. Zhong, T. Cai, J. Lee, and D. He (2024)Rest: retrieval-based speculative decoding.
In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
pp. 1582–1595.
Cited by: [§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[60\]M. Hu, T. Chen, Q. Chen, Y. Mu, W. Shao, and P. Luo (2025)Hiagent: hierarchical working memory management for solving long-horizon agent tasks with large language model.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 32779–32798.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p2.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[61\]Y. Hu, Y. Wang, and J. McAuley (2025)Evaluating memory in llm agents via incremental multi-turn interactions.
arXiv preprint arXiv:2507.05257.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.42.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[62\]W. Hua, D. Ding, Y. Gu, Y. Ren, K. Mei, M. Ma, and W. Y. Wang (2025)Semantic scheduling for llm inference.
arXiv preprint arXiv:2506.12204.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p2.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[63\]J. Huang, Z. Li, Z. Zhang, X. Quan, J. Hao, and Y. Zhang (2025)Plan2Evolve: llm self-evolution for improved planning capability via automated domain generation.
arXiv preprint arXiv:2509.21543.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[64\]S. Huang, Z. Fang, Z. Chen, S. Yuan, J. Ye, Y. Zeng, L. Chen, Q. Mao, and F. Zhao (2025)Critictool: evaluating self-critique capabilities of large language models in tool-calling error scenarios.
In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pp. 26683–26692.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.40.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[65\]X. Huang, W. Liu, X. Zeng, Y. Huang, X. Hao, Y. Wang, Y. Zeng, C. Wu, Y. Wang, R. Tang, et al. (2025)Toolace-dev: self-improving tool learning via decomposition and evolution.
arXiv preprint arXiv:2505.07512.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p3.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[66\]Y. Huang, J. Shi, Y. Li, C. Fan, S. Wu, Q. Zhang, Y. Liu, P. Zhou, Y. Wan, N. Z. Gong, et al. (2023)Metatool benchmark for large language models: deciding whether to use tools and which to use.
arXiv preprint arXiv:2310.03128.
Cited by: [§8](https://arxiv.org/html/2603.22862v2#S8.p1.1 "8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[67\]Y. Inoue, K. Misaki, Y. Imajuku, S. Kuroki, T. Nakamura, and T. Akiba (2025)Wider or deeper? scaling llm inference-time compute with adaptive branching tree search.
arXiv preprint arXiv:2503.04412.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[68\] (2024)Introducing the model context protocol.
External Links: [Link](https://www.anthropic.com/news/model-context-protocol "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[69\]K. Jang, D. Lee, K. Kim, D. Heo, T. Lee, W. Kim, and B. Suh (2025)DICE-bench: evaluating the tool-use capabilities of large language models in multi-round, multi-party dialogues.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 26822–26846.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.18.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[70\]J. Jia and Q. Li (2026)AutoTool: efficient tool selection for large language model agents.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 40,  pp. 31265–31273.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p2.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[71\]C. Jiang, X. Pan, and M. Yang (2025)Think twice before you act: enhancing agent behavioral safety with thought correction.
arXiv preprint arXiv:2505.11063.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[72\]T. Jin, Y. Zhu, and D. Kang (2025)Elt-bench: an end-to-end benchmark for evaluating ai agents on elt pipelines.
Proceedings of the VLDB Endowment19 (2),  pp. 84–98.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.8.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[73\]M. Kang, W. Chen, D. Han, H. A. Inan, L. Wutschitz, Y. Chen, R. Sim, and S. Rajmohan (2025)Acon: optimizing context compression for long-horizon llm agents.
arXiv preprint arXiv:2510.00615.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p4.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[74\]E. Karpas, O. Abend, Y. Belinkov, B. Lenz, O. Lieber, N. Ratner, Y. Shoham, H. Bata, Y. Levine, K. Leyton-Brown, et al. (2022)MRKL systems: a modular, neuro-symbolic architecture that combines large language models, external knowledge sources and discrete reasoning.
arXiv preprint arXiv:2205.00445.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p1.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[75\]I. Kerboua, S. Omidi Shayegan, M. Thakkar, X. H. Lù, L. Boisvert, M. Caccia, J. Espinas, A. Aussem, V. Eglin, and A. Lacoste (2025)FocusAgent: simple yet effective ways of trimming the large context of web agents.
arXiv preprint arXiv:2510.03204.
External Links: [Link](https://arxiv.org/abs/2510.03204 "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[76\]O. Khattab, A. Singhvi, P. Maheshwari, Z. Zhang, K. Santhanam, S. Vardhamanan, S. Haq, A. Sharma, T. T. Joshi, H. Moazam, et al. (2023)Dspy: compiling declarative language model calls into self-improving pipelines.
arXiv preprint arXiv:2310.03714.
Cited by: [§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[77\]J. Kim, W. Choi, and B. Lee (2025)Prompt flow integrity to prevent privilege escalation in llm agents.
arXiv preprint arXiv:2503.15547.
Cited by: [§5](https://arxiv.org/html/2603.22862v2#S5.p1.1 "5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[78\]S. Kim, S. Moon, R. Tabrizi, N. Lee, M. W. Mahoney, K. Keutzer, and A. Gholami (2024)An llm compiler for parallel function calling.
In Proceedings of the 41st International Conference on Machine Learning,
Cited by: [§6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1.p1.1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.1](https://arxiv.org/html/2603.22862v2#S6.SS1.p1.1 "6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[79\]J. Y. Koh, R. Lo, L. Jang, V. Duvvur, M. Lim, P. Huang, G. Neubig, S. Zhou, R. Salakhutdinov, and D. Fried (2024)Visualwebarena: evaluating multimodal agents on realistic visual web tasks.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 881–905.
Cited by: [§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p1.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[80\]B. Kwak, M. Kim, D. Lim, H. Chae, D. Kang, S. Kim, D. Yang, and J. Yeo (2025)Toolhaystack: stress-testing tool-augmented language models in realistic long-term interactions.
arXiv preprint arXiv:2505.23662.
Cited by: [§7.1](https://arxiv.org/html/2603.22862v2#S7.SS1.p1.1 "7.1. Capability boundary perception ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[81\]F. Lei, J. Chen, Y. Ye, R. Cao, D. Shin, H. Su, Z. Suo, H. Gao, W. Hu, P. Yin, V. Zhong, C. Xiong, R. Sun, Q. Liu, S. Wang, and T. Yu (2025)Spider 2.0: evaluating language models on real-world enterprise text-to-sql workflows.
In International Conference on Learning Representations,
External Links: [Link](https://openreview.net/forum?id=XmProj9cPs "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p3.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[82\]Y. Lei, H. Xie, J. Zhao, S. Liu, and X. Song (2025)MSCoRe: a benchmark for multi-stage collaborative reasoning in llm agents.
arXiv preprint arXiv:2509.17628.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.16.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[83\]Y. Leviathan, M. Kalman, and Y. Matias (2023)Fast inference from transformers via speculative decoding.
In International Conference on Machine Learning,
pp. 19274–19286.
Cited by: [§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[84\]I. Levy, B. Wiesel, S. Marreed, A. Oved, A. Yaeli, and S. Shlomov (2024)ST-webagentbench: a benchmark for evaluating safety and trustworthiness in web agents.
arXiv preprint arXiv:2410.06703.
External Links: [Link](https://arxiv.org/abs/2410.06703 "")Cited by: [§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[85\]J. Li, W. Zhao, J. Zhao, W. Zeng, H. Wu, X. Wang, R. Ge, Y. Cao, Y. Huang, W. Liu, et al. (2025)The tool decathlon: benchmarking language agents for diverse, realistic, and long-horizon task execution.
arXiv preprint arXiv:2510.25726.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p2.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.19.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[86\]M. Li, Y. Zhao, B. Yu, F. Song, H. Li, H. Yu, Z. Li, F. Huang, and Y. Li (2023)Api-bank: a comprehensive benchmark for tool-augmented llms.
In Proceedings of the 2023 conference on empirical methods in natural language processing,
pp. 3102–3116.
Cited by: [§8](https://arxiv.org/html/2603.22862v2#S8.p1.1 "8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[87\]X. Li, W. Jiao, J. Jin, G. Dong, J. Jin, Y. Wang, H. Wang, Y. Zhu, J. Wen, Y. Lu, et al. (2025)Deepagent: a general reasoning agent with scalable toolsets.
arXiv preprint arXiv:2510.21618.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p2.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p3.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[88\]X. Li, K. Chen, Y. Long, X. Bai, Y. Xu, and M. Zhang (2025)Generator-assistant stepwise rollback framework for large language model agent.
In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pp. 17694–17711.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p5.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.3.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[89\]X. Li (2025)A review of prominent paradigms for llm-based agents: tool use, planning (including rag), and feedback learning.
In Proceedings of the 31st international conference on computational linguistics,
pp. 9760–9779.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[90\]X. Li, H. Zou, and P. Liu (2025)Torl: scaling tool-integrated rl.
arXiv preprint arXiv:2503.23383.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p4.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[91\]Y. Li, S. Liu, T. Zheng, and M. Song (2025)Parallelized planning-acting for efficient llm-based multi-agent systems.
arXiv preprint arXiv:2503.03505.
Cited by: [§6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1.p1.1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2.p1.1 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[92\]Z. Li, J. Cui, X. Liao, and L. Xing (2025)Les dissonances: cross-tool harvesting and polluting in multi-tool empowered llm agents.
arXiv e-prints,  pp. arXiv–2504.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p2.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.2.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[93\]Z. Li, Y. Chang, G. Yu, and X. Le (2025)Hiplan: hierarchical planning for llm-based agents with adaptive global-local guidance.
arXiv preprint arXiv:2508.19076.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[94\]J. Liang, H. Li, C. Li, J. Zhou, S. Jiang, Z. Wang, C. Ji, Z. Zhu, R. Liu, T. Ren, et al. (2025)Ai meets brain: memory systems from cognitive neuroscience to autonomous agents.
arXiv preprint arXiv:2512.23343.
Cited by: [§7](https://arxiv.org/html/2603.22862v2#S7.p1.1 "7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[95\]X. Liang, M. Tao, Y. Xia, J. Wang, K. Li, Y. Wang, Y. He, J. Yang, T. Shi, Y. Wang, et al. (2025)Sage: self-evolving agents with reflective and memory-augmented abilities.
Neurocomputing647,  pp. 130470.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[96\]B. Y. Lin, Y. Fu, K. Yang, F. Brahman, S. Huang, C. Bhagavatula, P. Ammanabrolu, Y. Choi, and X. Ren (2023)Swiftsage: a generative agent with fast and slow thinking for complex interactive tasks.
Advances in Neural Information Processing Systems36,  pp. 23813–23825.
Cited by: [§6.2.2](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS2.p1.1 "6.2.2. Adaptive Model Routing ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[97\]F. Lin, E. La Malfa, V. Hofmann, E. M. Yang, A. Cohn, and J. B. Pierrehumbert (2024)Graph-enhanced large language models in asynchronous plan reasoning.
arXiv preprint arXiv:2402.02805.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p2.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[98\]Q. Lin, M. Wen, Q. Peng, G. Nie, J. Liao, J. Wang, X. Mo, J. Zhou, C. Cheng, Y. Zhao, et al. (2024)Hammer: robust function-calling for on-device language models via function masking.
arXiv preprint arXiv:2410.04587.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p2.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[99\]C. Liu, Z. Gu, G. Wu, Y. Zhang, J. Wei, and T. Xie (2025)Temac: multi-agent collaboration for automated web gui testing.
arXiv preprint arXiv:2506.00520.
Cited by: [§6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2.p1.1 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[100\]D. Liu, Q. Ren, C. Qian, S. Shao, Y. Xie, Y. Li, Z. Yang, H. Luo, P. Wang, Q. Liu, et al. (2026)AgentDoG: a diagnostic guardrail framework for ai agent safety and security.
arXiv preprint arXiv:2601.18491.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.6.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[101\]F. Liu, Y. Yao, P. Guo, Z. Yang, X. Lin, Z. Zhao, X. Tong, K. Mao, Z. Lu, Z. Wang, et al. (2026)A systematic survey on large language models for algorithm design.
ACM Computing Surveys58 (8),  pp. 1–32.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p2.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[102\]N. F. Liu, K. Lin, J. Hewitt, A. Paranjape, M. Bevilacqua, F. Petroni, and P. Liang (2024)Lost in the middle: how language models use long contexts.
Transactions of the association for computational linguistics12,  pp. 157–173.
Cited by: [§6.2.1](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS1.p1.1 "6.2.1. Dynamic tool search ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[103\]T. Liu, C. Xu, and J. McAuley (2023)RepoBench: benchmarking repository-level code auto-completion systems.
arXiv preprint arXiv:2306.03091.
External Links: [Link](https://arxiv.org/abs/2306.03091 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[104\]X. Liu, Z. Peng, X. Yi, X. Xie, L. Xiang, Y. Liu, and D. Xu (2024)Toolnet: connecting large language models with massive tools via tool graph.
arXiv preprint arXiv:2403.00839.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p2.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[105\]Z. Liu, T. Hoang, J. Zhang, M. Zhu, T. Lan, S. Kokane, J. Tan, W. Yao, Z. Liu, Y. Feng, et al. (2024)Apigen: automated pipeline for generating verifiable and diverse function-calling datasets.
Advances in Neural Information Processing Systems37,  pp. 54463–54482.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p3.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[106\]E. Lobo, X. Chen, J. Meng, N. Xi, Y. Jiao, C. Agarwal, Y. Zick, and Y. Gao (2026)STRUCTUREDAGENT: planning with and/or trees for long-horizon web tasks.
arXiv preprint arXiv:2603.05294.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p2.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[107\]J. Lu, T. Holleis, Y. Zhang, B. Aumayer, F. Nan, H. Bai, S. Ma, S. Ma, M. Li, G. Yin, et al. (2025)Toolsandbox: a stateful, conversational, interactive evaluation benchmark for llm tool use capabilities.
In Findings of the Association for Computational Linguistics: NAACL 2025,
pp. 1160–1183.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p2.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.26.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[108\]J. Lu, Z. Kong, Y. Wang, R. Fu, H. Wan, C. Yang, W. Lou, H. Sun, L. Wang, Y. Jiang, et al. (2026)Beyond static tools: test-time tool evolution for scientific reasoning.
arXiv preprint arXiv:2601.07641.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p3.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[109\]X. H. Lu, Z. Kasner, and S. Reddy (2024)WebLINX: real-world website navigation with multi-turn dialogue.
In Proceedings of the 41st International Conference on Machine Learning,
pp. 33007–33056.
External Links: [Link](https://proceedings.mlr.press/v235/lu24e.html "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[110\]Y. Lu, F. Ye, J. Li, Q. Gao, C. Liu, H. Luo, N. Du, X. Li, and F. Ren (2025)Codetool: enhancing programmatic tool invocation of llms via process supervision.
arXiv preprint arXiv:2503.20840.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p2.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[111\]Y. Lu, S. Liu, and L. Dong (2025)OrchDAG: complex tool orchestration in multi-turn interactions with plan dags.
arXiv preprint arXiv:2510.24663.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p4.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[112\]E. Lumer, F. Nizar, A. Gulati, P. H. Basavaraju, and V. K. Subbiah (2025)Tool-to-agent retrieval: bridging tools and agents for scalable llm multi-agent systems.
arXiv preprint arXiv:2511.01854.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p3.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[113\]H. Luo, H. Zhang, X. Zhang, H. Wang, Z. Qin, W. Lu, G. Ma, H. He, Y. Xie, Q. Zhou, et al. (2025)Ultrahorizon: benchmarking agent capabilities in ultra long-horizon scenarios.
arXiv preprint arXiv:2509.21766.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p3.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.21.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[114\]J. Luo, W. Zhang, Y. Yuan, Y. Zhao, J. Yang, Y. Gu, B. Wu, B. Chen, Z. Qiao, Q. Long, et al. (2025)Large language model agent: a survey on methodology, applications and challenges.
arXiv preprint arXiv:2503.21460.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[115\]N. Luo, A. P. Gema, X. He, E. Van Krieken, P. Lesci, and P. Minervini (2025)Self-training large language models for tool-use without demonstrations.
In Findings of the Association for Computational Linguistics: NAACL 2025,
pp. 1253–1271.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p2.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[116\]Z. Ma, J. Liu, X. Luo, Z. Huang, Q. Zhu, and W. Che (2025)Advancing tool-augmented large language models via meta-verification and reflection learning.
In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2,
pp. 2078–2089.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.5.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[117\]Z. Ma, W. Huang, J. Zhang, T. Gupta, and R. Krishna (2024)M & m’s: a benchmark to evaluate tool-use for m ulti-step m ulti-modal tasks.
In European Conference on Computer Vision,
pp. 18–34.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.14.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[118\]S. Maekawa, J. Hassell, P. Pezeshkpour, T. Mitchell, and E. Hruschka (2025)Towards reliable benchmarking: a contamination free, controllable evaluation framework for multi-step llm function calling.
arXiv preprint arXiv:2509.26553.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.15.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[119\]S. Minaee, T. Mikolov, N. Nikzad, M. Chenaghlu, R. Socher, X. Amatriain, and J. Gao (2024)Large language models: a survey.
arXiv preprint arXiv:2402.06196.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p1.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[120\] (2025)Model context protocol (mcp) specification.
External Links: [Link](https://modelcontextprotocol.io/specification/2025-06-18 "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[121\]B. Mohammadi, N. Potamitis, L. Klein, A. Arora, and L. Bindschaedler (2026)Atomix: timely, transactional tool use for reliable agentic workflows.
arXiv preprint arXiv:2602.14849.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p5.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.3.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[122\]M. Mohammadi, Y. Li, J. Lo, and W. Yip (2025)Evaluation and benchmarking of llm agents: a survey.
In Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2,
pp. 6129–6139.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[123\]V. Nath, P. Raja, C. Yoon, and S. Hendryx (2025)Toolcomp: a multi-tool reasoning & process supervision benchmark.
arXiv preprint arXiv:2501.01290.
Cited by: [§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.9.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[124\]X. Ning, Z. Lin, Z. Zhou, Z. Wang, H. Yang, and Y. Wang (2023)Skeleton-of-thought: prompting llms for efficient parallel generation.
arXiv preprint arXiv:2307.15337.
Cited by: [§6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1.p1.1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[125\]R. Niu, J. Li, S. Wang, Y. Fu, X. Hu, X. Leng, H. Kong, Y. Chang, and Q. Wang (2024)ScreenAgent: a vision language model-driven computer control agent.
In Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence,
pp. 6433–6441.
External Links: [Link](https://www.ijcai.org/proceedings/2024/711 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[126\]I. Ong, A. Almahairi, V. Wu, W. Chiang, T. Wu, J. E. Gonzalez, M. W. Kadous, and I. Stoica (2024)Routellm: learning to route llms with preference data.
arXiv preprint arXiv:2406.18665.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p3.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.2.2](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS2.p1.1 "6.2.2. Adaptive Model Routing ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[127\] (2025)OWASP top 10 for large language model applications (v2025).
External Links: [Link](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[128\]C. Packer, V. Fang, S. Patil, K. Lin, S. Wooders, and J. Gonzalez (2023)MemGPT: towards llms as operating systems..
Cited by: [§6.2.3](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS3.p1.1 "6.2.3. Intelligent caching and memory ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[129\]A. Parisi, Y. Zhao, and N. Fiedel (2022)Talm: tool augmented language models.
arXiv preprint arXiv:2205.12255.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p1.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[130\]S. G. Patil, T. Zhang, X. Wang, and J. E. Gonzalez (2024)Gorilla: large language model connected with massive apis.
Advances in Neural Information Processing Systems37,  pp. 126544–126565.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p1.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[131\]G. Polyakov, I. Alimova, D. Abulkhanov, I. Sedykh, A. Bout, S. Nikolenko, and I. Piontkovskaya (2025)ToolReflection: improving large language models for real-world api calls with self-generated data.
In Proceedings of the 1st Workshop for Research on Agent Language Models (REALM 2025),
pp. 184–199.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[132\]A. Prasad, A. Koller, M. Hartmann, P. Clark, A. Sabharwal, M. Bansal, and T. Khot (2024)Adapt: as-needed decomposition and planning with language models.
In Findings of the Association for Computational Linguistics: NAACL 2024,
pp. 4226–4252.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[133\]C. Qian, E. C. Acikgoz, Q. He, H. Wang, X. Chen, D. Hakkani-Tür, G. Tur, and H. Ji (2025)Toolrl: reward is all tool learning needs.
arXiv preprint arXiv:2504.13958.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p2.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[134\]C. Qian, C. Han, Y. Fung, Y. Qin, Z. Liu, and H. Ji (2023)Creator: tool creation for disentangling abstract and concrete reasoning of large language models.
In Findings of the Association for Computational Linguistics: EMNLP 2023,
pp. 6922–6939.
Cited by: [§7.2](https://arxiv.org/html/2603.22862v2#S7.SS2.p1.1 "7.2. Autonomous tool expansion ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[135\]H. Qian and Z. Liu (2025)MetaAgent: toward self-evolving agent via tool meta-learning.
arXiv preprint arXiv:2508.00271.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p3.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[136\]S. Qiao, H. Gui, C. Lv, Q. Jia, H. Chen, and N. Zhang (2024)Making language models better tool learners with execution feedback.
In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
pp. 3550–3568.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.5.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[137\]T. Qin, F. Bai, T. Hu, R. Vemulapalli, H. S. Koppula, Z. Xu, B. Jin, M. Cemri, J. Lu, Z. Wang, et al. (2025)COMPASS: a multi-turn benchmark for tool-mediated planning & preference optimization.
arXiv preprint arXiv:2510.07043.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.32.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[138\]Y. Qin, S. Liang, Y. Ye, K. Zhu, L. Yan, Y. Lu, Y. Lin, X. Cong, X. Tang, B. Qian, et al. (2023)Toolllm: facilitating large language models to master 16000+ real-world apis.
arXiv preprint arXiv:2307.16789.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p2.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.2.1](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS1.p1.1 "6.2.1. Dynamic tool search ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.11.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8](https://arxiv.org/html/2603.22862v2#S8.p1.1 "8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[139\]C. Qu, S. Dai, X. Wei, H. Cai, S. Wang, D. Yin, J. Xu, and J. Wen (2024)From exploration to mastery: enabling llms to master tools via self-driven interactions.
arXiv preprint arXiv:2410.08197.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p3.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[140\]C. Qu, S. Dai, X. Wei, H. Cai, S. Wang, D. Yin, J. Xu, and J. Wen (2025)Tool learning with large language models: a survey.
Frontiers of Computer Science19 (8),  pp. 198343.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[141\]M. S. Rashid, C. Bock, Y. Zhuang, A. Buchholz, T. Esler, S. Valentin, L. Franceschi, M. Wistuba, P. T. Sivaprasad, W. J. Kim, et al. (2025)Swe-polybench: a multi-language benchmark for repository level evaluation of coding agents.
arXiv preprint arXiv:2504.08703.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[142\]A. Rath (2026)Agent drift: quantifying behavioral degradation in multi-agent llm systems over extended interactions.
arXiv preprint arXiv:2601.04170.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p3.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p1.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p4.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[143\]T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu, M. Lomeli, E. Hambro, L. Zettlemoyer, N. Cancedda, and T. Scialom (2023)Toolformer: language models can teach themselves to use tools.
Advances in neural information processing systems36,  pp. 68539–68551.
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p1.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[144\]S. Sengupta, Z. Zhou, J. Araki, X. Wang, B. Wang, S. Wang, and Z. Feng (2026)Tooldreamer: instilling llm reasoning into tool retrievers.
In Proceedings of the 19th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 5465–5482.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[145\]Z. Sha, H. Tian, Z. Xu, S. Cui, C. Meng, and W. Wang (2025)Agent safety alignment via reinforcement learning.
arXiv preprint arXiv:2507.08270.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p4.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[146\]A. Shahriar, M. N. Rahman, S. Ahmed, F. Sadeque, and M. R. Parvez (2025)A survey on agentic security: applications, threats and defenses.
arXiv preprint arXiv:2510.06445.
Cited by: [§5](https://arxiv.org/html/2603.22862v2#S5.p1.1 "5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[147\]H. Shen, Y. Li, D. Meng, D. Cai, S. Qi, L. Zhang, M. Xu, and Y. Ma (2025)ShortcutsBench: A large-scale real-world benchmark for api-based agents.
In The Thirteenth International Conference on Learning Representations,
ICLR 2025, Singapore, April 24-28, 2025,
External Links: [Link](https://openreview.net/forum?id=kKILfPkhSz "")Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p2.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.24.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[148\]W. Shen, C. Li, H. Chen, M. Yan, X. Quan, H. Chen, J. Zhang, and F. Huang (2024)Small llms are weak tool learners: a multi-llm agent.
In Proceedings of the 2024 conference on empirical methods in natural language processing,
pp. 16658–16680.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p3.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[149\]Y. Shen, K. Song, X. Tan, D. Li, W. Lu, and Y. Zhuang (2023)Hugginggpt: solving ai tasks with chatgpt and its friends in hugging face.
Advances in Neural Information Processing Systems36,  pp. 38154–38180.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p3.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[150\]Y. Shen, K. Song, X. Tan, W. Zhang, K. Ren, S. Yuan, W. Lu, D. Li, and Y. Zhuang (2024)Taskbench: benchmarking large language models for task automation.
Advances in Neural Information Processing Systems37,  pp. 4540–4574.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.12.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[151\]Y. Shen, Z. Huang, Z. Wang, M. Tian, Z. Guo, C. Zhang, S. Zhou, Z. Hu, D. Li, J. Xu, et al. (2026)TRIP-bench: a benchmark for long-horizon interactive agents in real-world scenarios.
arXiv preprint arXiv:2602.01675.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p3.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.20.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[152\]Z. Shen (2024)Llm with tools: a survey.
arXiv preprint arXiv:2409.18807.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[153\]N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao (2023)Reflexion: language agents with verbal reinforcement learning.
Advances in neural information processing systems36,  pp. 8634–8652.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.2.3](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS3.p1.1 "6.2.3. Intelligent caching and memory ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[154\]B. Singer, K. Lucas, L. Adiga, M. Jain, L. Bauer, and V. Sekar (2025)Incalmo: an autonomous llm-assisted system for red teaming multi-host networks.
arXiv preprint arXiv:2501.16466.
Cited by: [§6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2.p1.1 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[155\]X. Song, Z. Wang, S. Wu, T. Shi, and L. Ai (2025)Gradientsys: a multi-agent llm scheduler with react orchestration.
arXiv preprint arXiv:2507.06520.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p3.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[156\]Y. Song, W. Xiong, D. Zhu, C. Li, K. Wang, Y. Tian, and S. Li (2023)Restgpt: connecting large language models with real-world applications via restful apis. corr, abs/2306.06624, 2023. doi: 10.48550.
arXiv preprint arXiv.2306.06624.
Cited by: [§7.2](https://arxiv.org/html/2603.22862v2#S7.SS2.p1.1 "7.2. Autonomous tool expansion ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[157\]Y. Song, H. Huang, Q. Lin, Y. Zhao, X. Qu, J. Wang, X. Lou, W. Liu, Z. Zhang, Y. Yu, et al. (2025)ColorBench: benchmarking mobile agents with graph-structured framework for complex long-horizon tasks.
arXiv preprint arXiv:2510.14621.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.43.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[158\]J. Su, Y. Wan, J. Yang, H. Shi, T. Han, J. Luo, and Y. Qiu (2025)Failure makes the agent stronger: enhancing accuracy through structured reflection for reliable tool interactions.
arXiv preprint arXiv:2509.18847.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[159\]X. Tian, H. Wang, S. Chen, H. Zhou, K. Yu, Y. Zhang, J. Ouyang, J. Yin, J. Chen, B. Guo, et al. (2026)ASTRA: automated synthesis of agentic trajectories and reinforcement arenas.
arXiv preprint arXiv:2601.21558.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p2.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[160\]E. Treviño, H. Contant, J. Ngai, G. Neubig, and Z. Z. Wang (2025)Benchmarking failures in tool-augmented language models.
In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers),
pp. 2916–2934.
Cited by: [§7.1](https://arxiv.org/html/2603.22862v2#S7.SS1.p1.1 "7.1. Capability boundary perception ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[161\]H. Trivedi, T. Khot, M. Hartmann, R. Manku, V. Dong, E. Li, S. Gupta, A. Sabharwal, and N. Balasubramanian (2024)Appworld: a controllable world of apps and people for benchmarking interactive coding agents.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 16022–16076.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p2.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.30.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[162\]G. Wan, M. Ling, X. Ren, R. Han, S. Li, and Z. Zhang (2025)Compass: enhancing agent long-horizon reasoning with evolving context.
arXiv preprint arXiv:2510.08790.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p4.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[163\]G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar (2023)Voyager: an open-ended embodied agent with large language models.
arXiv preprint arXiv:2305.16291.
Cited by: [§7.3](https://arxiv.org/html/2603.22862v2#S7.SS3.p2.1 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[164\]H. Wang, Y. Cao, L. Lin, and J. Chen (2026)PreFlect: from retrospective to prospective reflection in large language model agents.
arXiv preprint arXiv:2602.07187.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[165\]H. Wang, C. M. Poskitt, and J. Sun (2025)Agentspec: customizable runtime enforcement for safe and reliable llm agents.
arXiv preprint arXiv:2503.18666.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p4.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.2.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[166\]H. Wang, W. Huang, Y. Wang, Y. Xi, J. Lu, H. Zhang, N. Hu, Z. Liu, J. Z. Pan, and K. Wong (2025)Rethinking stateful tool use in multi-turn dialogues: benchmarks and challenges.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 5433–5453.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p2.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[167\]J. Wang, S. Zhao, J. Liu, H. Wang, W. Li, B. Qin, and T. Liu (2026)Orchestrating intelligence: confidence-aware routing for efficient multi-agent collaboration across multi-scale models.
arXiv preprint arXiv:2601.04861.
Cited by: [§6.2.2](https://arxiv.org/html/2603.22862v2#S6.SS2.SSS2.p1.1 "6.2.2. Adaptive Model Routing ‣ 6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[168\]J. Wang, Z. Ma, Y. Li, S. Zhang, C. Chen, K. Chen, and X. Le (2024)GTA: a benchmark for general tool agents.
Advances in Neural Information Processing Systems37,  pp. 75749–75790.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.31.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[169\]J. Wang, J. Zhou, X. Wang, X. Mo, H. Zhang, Q. Lin, J. Jincheng, M. Wen, W. Zhang, and Q. Peng (2025)Hammerbench: fine-grained function-calling evaluation in real mobile assistant scenarios.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 3350–3376.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p2.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.25.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[170\]L. Wang, Y. Deng, Y. Zha, G. Mao, Q. Wang, T. Min, W. Chen, and S. Chen (2024)MobileAgentBench: an efficient and user-friendly benchmark for mobile llm agents.
arXiv preprint arXiv:2406.08184.
External Links: [Link](https://arxiv.org/abs/2406.08184 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p4.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[171\]P. Wang, Y. Wu, N. Wang, J. Liu, X. Song, Z. Y. Peng, K. Deng, C. Zhang, J. Wang, J. Peng, G. Zhang, H. Guo, Z. Zhang, W. Su, and B. Zheng (2025)MTU-bench: A multi-granularity tool-use benchmark for large language models.
In The Thirteenth International Conference on Learning Representations,
ICLR 2025, Singapore, April 24-28, 2025,
External Links: [Link](https://openreview.net/forum?id=6guG2OlXsr "")Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.34.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[172\]R. Wang, X. Han, L. Ji, S. Wang, T. Baldwin, and H. Li (2024)Toolgen: unified tool retrieval and calling via generation.
arXiv preprint arXiv:2410.03439.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p2.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[173\]W. Wang, D. Han, D. M. Diaz, J. Xu, V. Rühle, and S. Rajmohan (2025)Odysseybench: evaluating llm agents on long-horizon complex office application workflows.
arXiv preprint arXiv:2508.09124.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.41.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[174\]Y. Wang, Z. Xu, Y. Huang, X. Wang, Z. Song, L. Gao, C. Wang, X. Tang, Y. Zhao, A. Cohan, et al. (2025)DyFlow: dynamic workflow framework for agentic reasoning.
arXiv preprint arXiv:2509.26062.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[175\]Y. Wang and X. Chen (2025)Mirix: multi-agent memory system for llm-based agents.
arXiv preprint arXiv:2507.07957.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p4.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[176\]Z. Wang, Q. Chang, H. Patel, S. Biju, C. Wu, Q. Liu, A. Ding, A. Rezazadeh, A. Shah, Y. Bao, and E. Siow (2025)MCP-bench: benchmarking tool-using llm agents with complex real-world tasks via mcp servers.
arXiv preprint arXiv:2508.20453.
External Links: [Link](https://arxiv.org/abs/2508.20453 "")Cited by: [§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[177\]Z. Wang, Z. Cheng, H. Zhu, D. Fried, and G. Neubig (2024)What are tools anyway? a survey from the language model perspective.
arXiv preprint arXiv:2403.15452.
Cited by: [§1.2](https://arxiv.org/html/2603.22862v2#S1.SS2.p1.1 "1.2. Related Work ‣ 1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[178\]Z. Wang, K. Wang, Q. Wang, P. Zhang, L. Li, Z. Yang, X. Jin, K. Yu, M. N. Nguyen, L. Liu, et al. (2025)Ragen: understanding self-evolution in llm agents via multi-turn reinforcement learning.
arXiv preprint arXiv:2504.20073.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p3.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[179\]Q. Wei, S. Zeng, C. Li, W. Brown, O. Frunza, W. Deng, A. Schneider, Y. Nevmyvaka, Y. K. Zhao, A. Garcia, et al. (2025)Reinforcing multi-turn reasoning in llm agents via turn-level reward design.
arXiv preprint arXiv:2505.11821.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p2.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[180\]G. Wölflein, D. Ferber, D. Truhn, O. Arandjelovic, and J. N. Kather (2025)Llm agents making agent tools.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 26092–26130.
Cited by: [§7.2](https://arxiv.org/html/2603.22862v2#S7.SS2.p1.1 "7.2. Autonomous tool expansion ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[181\]M. Wornow, V. Garodia, V. Vassalos, and U. Contractor (2025)Top of the class: benchmarking llm agents on real-world enterprise tasks.
In ICLR 2025 Workshop on Building Trust in LLMs and LLM Applications,
External Links: [Link](https://openreview.net/pdf?id=RQjUpeINII "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p3.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[182\]F. Wu, W. Zhu, Y. Zhang, S. Chatterjee, J. Zhu, F. Mo, R. Luo, and J. Gao (2025)PORTool: tool-use llm training with rewarded tree.
arXiv preprint arXiv:2510.26020.
Cited by: [§4.4](https://arxiv.org/html/2603.22862v2#S4.SS4.p2.1 "4.4. Reinforcement Learning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[183\]J. Wu, Q. Zhao, Z. Chen, K. Qin, Y. Zhao, X. Wang, and Y. Yao (2025)GAP: graph-based agent planning with parallel tool use and reinforcement learning.
arXiv preprint arXiv:2510.25320.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p2.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[184\]M. Wu, T. Zhu, H. Han, C. Tan, X. Zhang, and W. Chen (2024)Seal-tools: self-instruct tool learning dataset for agent tuning and detailed benchmark.
In CCF International Conference on Natural Language Processing and Chinese Computing,
pp. 372–384.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p2.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.13.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[185\]Z. Xi, S. Liang, Q. Liu, J. Zhang, L. Peng, F. Nan, M. Nayim, T. Zhang, R. Mundada, L. Qin, et al. (2026)ToolGym: an open-world tool-using environment for scalable agent testing and data curation.
arXiv preprint arXiv:2601.06328.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p2.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.27.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[186\]C. S. Xia, Y. Deng, S. Dunn, and L. Zhang (2024)Agentless: demystifying LLM-based software engineering agents.
arXiv preprint arXiv:2407.01489.
External Links: [Link](https://arxiv.org/abs/2407.01489 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[187\]T. Xie, D. Zhang, J. Chen, X. Li, S. Zhao, R. Cao, T. J. Hua, Z. Cheng, D. Shin, F. Lei, et al. (2024)Osworld: benchmarking multimodal agents for open-ended tasks in real computer environments.
Advances in Neural Information Processing Systems37,  pp. 52040–52094.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.29.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p1.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[188\]M. Xing, R. Zhang, H. Xue, Q. Chen, F. Yang, and Z. Xiao (2024)Understanding the weakness of large language model agents within a complex android environment.
In Proceedings of the 30th ACM SIGKDD conference on knowledge discovery and data mining,
pp. 6061–6072.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p4.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[189\]Q. Xiong, Y. Huang, Z. Jiang, Z. Chang, Y. Zheng, T. Li, and M. Li (2025)Butterfly effects in toolchains: a comprehensive analysis of failed parameter filling in llm tool-agent systems.
arXiv preprint arXiv:2507.15296.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p2.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.6.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[190\]W. Xiong, Y. Song, Q. Dong, B. Zhao, F. Song, X. Wang, and S. Li (2025)Mpo: boosting llm agents with meta plan optimization.
arXiv preprint arXiv:2503.026825 (6),  pp. 7.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[191\]Z. Xiu, D. Q. Sun, K. Cheng, M. Patel, Y. Zhang, J. Lu, O. Attia, R. Vemulapalli, O. Tuzel, M. Cao, et al. (2026)ASTRA-bench: evaluating tool-use agent reasoning and action planning with personal user context.
arXiv preprint arXiv:2603.01357.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.44.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[192\]B. Xu, Z. Peng, B. Lei, S. Mukherjee, Y. Liu, and D. Xu (2023)Rewoo: decoupling reasoning from observations for efficient augmented language models.
arXiv preprint arXiv:2305.18323.
Cited by: [§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[193\]H. Xu, J. Hu, K. Zhang, L. Yu, Y. Tang, X. Song, Y. Duan, L. Ai, and B. Shi (2025)Sedm: scalable self-evolving distributed memory for agents.
arXiv preprint arXiv:2509.09498.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p4.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[194\]W. Xu, Z. Jiang, Y. Liu, P. Gao, W. Liu, J. Luan, Y. Li, Y. Liu, B. Wang, and B. An (2025)Mobile-bench-v2: a more realistic and comprehensive benchmark for vlm-based mobile agents.
arXiv preprint arXiv:2505.11891.
External Links: [Link](https://arxiv.org/abs/2505.11891 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p4.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[195\]W. Xu, Z. Liang, K. Mei, H. Gao, J. Tan, and Y. Zhang (2025)A-mem: agentic memory for llm agents.
arXiv preprint arXiv:2502.12110.
Cited by: [§3.2](https://arxiv.org/html/2603.22862v2#S3.SS2.p4.1 "3.2. Long-Horizon Orchestration ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[196\]Y. Xu, X. Kong, T. Chen, and D. Zhuo (2024)Conveyor: efficient tool-aware llm serving with tool partial execution.
arXiv preprint arXiv:2406.00059.
External Links: [Link](https://arxiv.org/abs/2406.00059 "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[197\]Y. Xu, X. Liu, X. Sun, S. Cheng, H. Yu, H. Lai, S. Zhang, D. Zhang, J. Tang, and Y. Dong (2025)AndroidLab: training and systematic benchmarking of android autonomous agents.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 2144–2166.
External Links: [Link](https://aclanthology.org/2025.acl-long.107/ "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p4.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[198\]C. Yang, R. Le, Y. Xing, Z. An, Z. Chen, W. X. Zhao, Y. Song, and T. Zhang (2025)ToolMind technical report: a large-scale, reasoning-enhanced tool-use dataset.
arXiv preprint arXiv:2511.15718.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p4.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[199\]J. Yang, H. Zhang, F. Li, X. Zou, C. Li, and J. Gao (2023)Set-of-mark prompting unleashes extraordinary visual grounding in gpt-4v.
arXiv preprint arXiv:2310.11441.
Cited by: [§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p1.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[200\]K. Yang, Y. Liu, S. Chaudhary, R. Fakoor, P. Chaudhari, G. Karypis, and H. Rangwala (2025)AgentOccam: a simple yet strong baseline for llm-based web agents.
In International Conference on Learning Representations,
External Links: [Link](https://openreview.net/forum?id=oWdzUpOlkX "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p2.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[201\]R. Yang, L. Song, Y. Li, S. Zhao, Y. Ge, X. Li, and Y. Shan (2023)Gpt4tools: teaching large language model to use tools via self-instruction.
Advances in Neural Information Processing Systems36,  pp. 71995–72007.
Cited by: [§4.3](https://arxiv.org/html/2603.22862v2#S4.SS3.p1.1 "4.3. Supervised Fine-Tuning ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[202\]S. Yao, N. Shinn, P. Razavi, and K. Narasimhan (2024)τ\\tau-bench: A benchmark for tool-agent-user interaction in real-world domains.
CoRRabs/2406.12045.
External Links: [Link](https://doi.org/10.48550/arXiv.2406.12045 ""),
[Document](https://dx.doi.org/10.48550/ARXIV.2406.12045 ""),
2406.12045Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.2.2.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[203\]S. Yao, D. Yu, J. Zhao, I. Shafran, T. Griffiths, Y. Cao, and K. Narasimhan (2023)Tree of thoughts: deliberate problem solving with large language models.
Advances in neural information processing systems36,  pp. 11809–11822.
Cited by: [§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[204\]S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and Y. Cao (2022)React: synergizing reasoning and acting in language models.
In The eleventh international conference on learning representations,
Cited by: [§1](https://arxiv.org/html/2603.22862v2#S1.p1.1 "1. Introduction ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p1.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.1.2](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS2.p1.1 "6.1.2. Asynchronous decoupling ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[205\]J. Ye, Z. Du, X. Yao, W. Lin, Y. Xu, Z. Chen, Z. Wang, S. Zhu, Z. Xi, S. Yuan, et al. (2025)ToolHop: a query-driven benchmark for evaluating large language models in multi-hop tool use.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 2995–3021.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.6.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[206\]J. Ye, S. Li, G. Li, C. Huang, S. Gao, Y. Wu, Q. Zhang, T. Gui, and X. Huang (2024)Toolsword: unveiling safety issues of large language models in tool learning across three stages.
In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 2181–2211.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.46.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[207\]J. Ye, Y. Wu, S. Gao, C. Huang, S. Li, G. Li, X. Fan, Q. Zhang, T. Gui, and X. Huang (2024)Rotbench: a multi-level benchmark for evaluating the robustness of large language models in tool learning.
In Proceedings of the 2024 conference on empirical methods in natural language processing,
pp. 313–333.
Cited by: [Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.45.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[208\]S. Ye, H. Shi, D. Shih, H. Yun, T. G. Roosta, and T. Shu (2026)Realwebassist: a benchmark for long-horizon web assistance with real-world users.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 40,  pp. 34441–34449.
Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p4.1 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.38.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[209\]G. Yin, H. Bai, S. Ma, F. Nan, Y. Sun, Z. Xu, S. Ma, J. Lu, X. Kong, A. Zhang, et al. (2025)Mmau: a holistic benchmark of agent capabilities across diverse domains.
In Findings of the Association for Computational Linguistics: NAACL 2025,
pp. 4737–4765.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.17.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[210\]B. Yu, Y. Zhu, P. He, and D. Kang (2025)UTBoost: rigorous evaluation of coding agents on SWE-bench.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 3762–3774.
External Links: [Link](https://aclanthology.org/2025.acl-long.189/ "")Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p2.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[211\]P. Yu, W. Liu, Y. Yang, J. Li, Z. Zhang, X. Feng, and feng zhang (2026)Benchmarking LLM tool-use in the wild.
In The Fourteenth International Conference on Learning Representations,
External Links: [Link](https://openreview.net/forum?id=yz7fL5vfpn "")Cited by: [§8.3](https://arxiv.org/html/2603.22862v2#S8.SS3.p3.3 "8.3. Dynamic Environments ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.35.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[212\]X. Zeng, W. Liu, X. Huang, Z. Wang, L. Wang, L. Li, Y. Wang, L. Shang, X. Jiang, R. Tang, et al. (2026)ToolACE-r: model-aware iterative training and adaptive refinement for tool learning.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 40,  pp. 34593–34601.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p3.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[213\]X. Zeng, L. Wang, W. Liu, L. Li, Y. Wang, L. Shang, X. Jiang, and Q. Liu (2026)ARTIS: agentic risk-aware test-time scaling via iterative simulation.
arXiv preprint arXiv:2602.01709.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p4.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[214\]Q. Zhan, Z. Liang, Z. Ying, and D. Kang (2024)InjecAgent: benchmarking indirect prompt injections in tool-integrated large language model agents.
In Findings of the Association for Computational Linguistics: ACL 2024,
pp. 10471–10506.
External Links: [Link](https://aclanthology.org/2024.findings-acl.624/ "")Cited by: [§9.3](https://arxiv.org/html/2603.22862v2#S9.SS3.p1.1 "9.3. Engineering Essentials and Governance for Industrial-Grade Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[215\]C. Zhang, Z. Yang, J. Liu, Y. Li, Y. Han, X. Chen, Z. Huang, B. Fu, and G. Yu (2025)Appagent: multimodal agents as smartphone users.
In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems,
pp. 1–20.
Cited by: [§7.3](https://arxiv.org/html/2603.22862v2#S7.SS3.p3.1 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[216\]E. Zhang, E. Zhu, G. Bansal, A. Fourney, H. Mozannar, and J. Gerrits (2025)Optimizing sequential multi-step tasks with parallel llm agents.
arXiv preprint arXiv:2507.08944.
Cited by: [§6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1.p1.1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[217\]J. Zhang, J. Xiang, Z. Yu, F. Teng, X. Chen, J. Chen, M. Zhuge, X. Cheng, S. Hong, J. Wang, et al. (2024)Aflow: automating agentic workflow generation.
arXiv preprint arXiv:2410.10762.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[218\]J. Zhang, R. Krishna, A. H. Awadallah, and C. Wang (2023)Ecoassistant: using llm assistant more affordably and accurately.
arXiv preprint arXiv:2310.03046.
Cited by: [§6.2](https://arxiv.org/html/2603.22862v2#S6.SS2.p1.1 "6.2. Tool call cost and inference budget ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[219\]K. Zhang, W. Jiao, K. Du, Y. Lu, W. Liu, W. Zhang, and Y. Yu (2025)LoopTool: closing the data-training loop for robust llm tool calls.
arXiv preprint arXiv:2511.09148.
Cited by: [§4.2](https://arxiv.org/html/2603.22862v2#S4.SS2.p4.1 "4.2. Multi-tool trajectory Data Synthesis ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[220\]S. Zhang, Z. Zhang, K. Chen, X. Ma, M. Yang, T. Zhao, and M. Zhang (2024)Dynamic planning for llm-based graphical user interface automation.
In Findings of the Association for Computational Linguistics: EMNLP 2024,
pp. 1304–1320.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[221\]X. Zhang, X. Tang, H. Liu, Z. Wu, Q. He, D. Lee, and S. Wang (2025)Divide-verify-refine: can llms self-align with complex instructions?.
In Findings of the Association for Computational Linguistics: ACL 2025,
pp. 13783–13800.
Cited by: [§5.1](https://arxiv.org/html/2603.22862v2#S5.SS1.p6.1 "5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.4.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[222\]X. Zhang, Y. Shen, Z. Zheng, L. Wu, W. Zhang, Y. Yan, Q. Peng, J. Wang, and W. Lu (2025)Asktoact: enhancing llms tool use via self-correcting clarification.
In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pp. 13495–13522.
Cited by: [§7.1](https://arxiv.org/html/2603.22862v2#S7.SS1.p1.1 "7.1. Capability boundary perception ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[223\]Y. Zhang, G. Ganapavarapu, S. Jayaraman, B. Agrawal, D. Patel, and A. Fokoue (2026)SPIRAL: symbolic llm planning via grounded and reflective search.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 40,  pp. 36527–36535.
Cited by: [§3.3](https://arxiv.org/html/2603.22862v2#S3.SS3.p2.1 "3.3. Agent Self-Improvement ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[224\]Y. Zhang, S. Jiang, R. Li, J. Tu, Y. Su, L. Deng, X. Guo, C. Lv, and J. Lin (2026)DeepPlanning: benchmarking long-horizon agentic planning with verifiable constraints.
arXiv preprint arXiv:2601.18137.
Cited by: [§8.2](https://arxiv.org/html/2603.22862v2#S8.SS2.p3.1 "8.2. Temporal Scale ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.23.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[225\]Z. Zhang, T. Chen, W. Xu, A. Pentland, and J. Pei (2025)ReCAP: recursive context-aware reasoning and planning for large language model agents.
arXiv preprint arXiv:2510.23822.
Cited by: [§3.1](https://arxiv.org/html/2603.22862v2#S3.SS1.p3.1 "3.1. Topological Planning ‣ 3. Multi-Tool Agent Inference-Time Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[226\]A. Zhao, D. Huang, Q. Xu, M. Lin, Y. Liu, and G. Huang (2024)Expel: llm agents are experiential learners.
In Proceedings of the AAAI Conference on Artificial Intelligence,
Vol. 38,  pp. 19632–19642.
Cited by: [§7.3](https://arxiv.org/html/2603.22862v2#S7.SS3.p2.1 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[227\]B. Zheng, B. Gou, J. Kil, H. Sun, and Y. Su (2024)Gpt-4v (ision) is a generalist web agent, if grounded.
arXiv preprint arXiv:2401.01614.
Cited by: [§9.2](https://arxiv.org/html/2603.22862v2#S9.SS2.p1.1 "9.2. Orchestration Paradigms in Representative Interactive Environments ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[228\]J. Zheng, C. Shi, X. Cai, Q. Li, D. Zhang, C. Li, D. Yu, and Q. Ma (2026)Lifelong learning of large language model based agents: a roadmap.
IEEE Transactions on Pattern Analysis and Machine Intelligence.
Cited by: [§7.3](https://arxiv.org/html/2603.22862v2#S7.SS3.p1.1 "7.3. Open environment adaptation ‣ 7. Completeness ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[229\]L. Zhong, Z. Du, X. Zhang, H. Hu, and J. Tang (2025)ComplexFuncBench: exploring multi-step and constrained function calling under long-context scenario.
arXiv preprint arXiv:2501.10132.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.3.10.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§9.1](https://arxiv.org/html/2603.22862v2#S9.SS1.p2.1 "9.1. A Unified Abstraction for Application-Side Multi-Tool Orchestration ‣ 9. Application ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[230\]A. Zhou, K. Yan, M. Shlapentokh-Rothman, H. Wang, and Y. Wang (2023)Language agent tree search unifies reasoning acting and planning in language models.
arXiv preprint arXiv:2310.04406.
Cited by: [§5.2](https://arxiv.org/html/2603.22862v2#S5.SS2.p3.1 "5.2. Security Risks in Long-Horizon Tool Chains ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 1](https://arxiv.org/html/2603.22862v2#S5.T1.1.6.3.1.1 "In 5.1. Security Risks in Parallel Execution ‣ 5. Safety of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§6.1.3](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS3.p1.1 "6.1.3. Speculative reasoning ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[231\]H. Zhou, Y. Chen, S. Guo, X. Yan, K. H. Lee, Z. Wang, K. Y. Lee, G. Zhang, K. Shao, L. Yang, et al. (2025)Memento: fine-tuning llm agents without fine-tuning llms.
arXiv preprint arXiv:2508.16153.
Cited by: [§4.1](https://arxiv.org/html/2603.22862v2#S4.SS1.p2.1 "4.1. Training-free Methods ‣ 4. Multi-Tool Agent Tuning Paradigms ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[232\]Y. Zhou, M. Zhao, Z. Wang, D. Gu, B. Guo, R. Ye, L. Han, C. Jin, and D. N. Metaxas (2025)Mˆ 3-bench: multi-modal, multi-hop, multi-threaded tool-using mllm agent benchmark.
arXiv preprint arXiv:2511.17729.
Cited by: [§8.1](https://arxiv.org/html/2603.22862v2#S8.SS1.p2.1 "8.1. Topological Complexity ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[§8.4](https://arxiv.org/html/2603.22862v2#S8.SS4.p2.1 "8.4. State Persistence and Self-Correction ‣ 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"),
[Table 2](https://arxiv.org/html/2603.22862v2#S8.T2.1.1.1 "In 8. Benchmarks ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").

- \[233\]D. Zhu, W. Shi, Z. Shi, Z. Ren, S. Wang, L. Yan, and D. Yin (2025)Divide-then-aggregate: an efficient tool learning method via parallel tool invocation.
In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
pp. 28859–28875.
Cited by: [§6.1.1](https://arxiv.org/html/2603.22862v2#S6.SS1.SSS1.p1.1 "6.1.1. Parallel execution ‣ 6.1. Latency in multi-tool chains ‣ 6. Efficiency of Multi-Tool Agents ‣ The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration").


BETA

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="writing-effective-tools-for-ai-agents-using-ai-agents.md">
<details>
<summary>Writing effective tools for agents — with agents</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.anthropic.com/engineering/writing-tools-for-agents>

https://www-cdn.anthropic.com/images/4zrzovbb/website/876165247ba5668bd195854eef4631ad9a184001-1000x1000.svg

# Writing effective tools for agents — with agents

Published Sep 11, 2025

Agents are only as effective as the tools we give them. We share how to write high-quality tools and evaluations, and how you can boost performance by using Claude to optimize its tools for itself.

The [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) can empower LLM agents with potentially hundreds of tools to solve real-world tasks. But how do we make those tools maximally effective?

In this post, we describe our most effective techniques for improving performance in a variety of agentic AI systems1.

We begin by covering how you can:

- Build and test prototypes of your tools
- Create and run comprehensive evaluations of your tools with agents
- Collaborate with agents like Claude Code to automatically increase the performance of your tools

We conclude with key principles for writing high-quality tools we’ve identified along the way:

- Choosing the right tools to implement (and not to implement)
- Namespacing tools to define clear boundaries in functionality
- Returning meaningful context from tools back to agents
- Optimizing tool responses for token efficiency
- Prompt-engineering tool descriptions and specs

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fcdc027ad2730e4732168bb198fc9363678544f99-1920x1080.png&w=3840&q=75Building an evaluation allows you to systematically measure the performance of your tools. You can use Claude Code to automatically optimize your tools against this evaluation.

## What is a tool?

In computing, deterministic systems produce the same output every time given identical inputs, while _non-deterministic_ systems—like agents—can generate varied responses even with the same starting conditions.

When we traditionally write software, we’re establishing a contract between deterministic systems. For instance, a function call like `getWeather(“NYC”)` will always fetch the weather in New York City in the exact same manner every time it is called.

Tools are a new kind of software which reflects a contract between deterministic systems and non-deterministic agents. When a user asks "Should I bring an umbrella today?,” an agent might call the weather tool, answer from general knowledge, or even ask a clarifying question about location first. Occasionally, an agent might hallucinate or even fail to grasp how to use a tool.

This means fundamentally rethinking our approach when writing software for agents: instead of writing tools and [MCP servers](https://modelcontextprotocol.io/) the way we’d write functions and APIs for other developers or systems, we need to design them for agents.

Our goal is to increase the surface area over which agents can be effective in solving a wide range of tasks by using tools to pursue a variety of successful strategies. Fortunately, in our experience, the tools that are most “ergonomic” for agents also end up being surprisingly intuitive to grasp as humans.

## How to write tools

In this section, we describe how you can collaborate with agents both to write and to improve the tools you give them. Start by standing up a quick prototype of your tools and testing them locally. Next, run a comprehensive evaluation to measure subsequent changes. Working alongside agents, you can repeat the process of evaluating and improving your tools until your agents achieve strong performance on real-world tasks.

### Building a prototype

It can be difficult to anticipate which tools agents will find ergonomic and which tools they won’t without getting hands-on yourself. Start by standing up a quick prototype of your tools. If you’re using [Claude Code](https://www.anthropic.com/claude-code) to write your tools (potentially in one-shot), it helps to give Claude documentation for any software libraries, APIs, or SDKs (including potentially the [MCP SDK](https://modelcontextprotocol.io/docs/sdk)) your tools will rely on. LLM-friendly documentation can commonly be found in flat `llms.txt` files on official documentation sites (here’s our [API’s](https://docs.anthropic.com/llms.txt)).

Wrapping your tools in a [local MCP server](https://modelcontextprotocol.io/docs/develop/connect-local-servers) or [Desktop extension](https://www.anthropic.com/engineering/desktop-extensions) (DXT) will allow you to connect and test your tools in Claude Code or the Claude Desktop app.

To connect your local MCP server to Claude Code, run `claude mcp add <name> <command> [args...]`.

To connect your local MCP server or DXT to the Claude Desktop app, navigate to `Settings > Developer` or `Settings > Extensions`, respectively.

Tools can also be passed directly into [Anthropic API](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview) calls for programmatic testing.

Test the tools yourself to identify any rough edges. Collect feedback from your users to build an intuition around the use-cases and prompts you expect your tools to enable.

### Running an evaluation

Next, you need to measure how well Claude uses your tools by running an evaluation. Start by generating lots of evaluation tasks, grounded in real world uses. We recommend collaborating with an agent to help analyze your results and determine how to improve your tools. See this process end-to-end in our [tool evaluation cookbook](https://platform.claude.com/cookbook/tool-evaluation-tool-evaluation).

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F6e810aee67f3f3c955832fb7bf9033ffb0102000-1920x1080.png&w=3840&q=75Held-out test set performance of our internal Slack tools

**Generating evaluation tasks**

With your early prototype, Claude Code can quickly explore your tools and create dozens of prompt and response pairs. Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). We recommend you avoid overly simplistic or superficial “sandbox” environments that don’t stress-test your tools with sufficient complexity. Strong evaluation tasks might require multiple tool calls—potentially dozens.

Here are some examples of strong tasks:

- Schedule a meeting with Jane next week to discuss our latest Acme Corp project. Attach the notes from our last project planning meeting and reserve a conference room.
- Customer ID 9182 reported that they were charged three times for a single purchase attempt. Find all relevant log entries and determine if any other customers were affected by the same issue.
- Customer Sarah Chen just submitted a cancellation request. Prepare a retention offer. Determine: (1) why they're leaving, (2) what retention offer would be most compelling, and (3) any risk factors we should be aware of before making an offer.

And here are some weaker tasks:

- Schedule a meeting with jane@acme.corp next week.
- Search the payment logs for `purchase_complete` and `customer_id=9182`.
- Find the cancellation request by Customer ID 45892.

Each evaluation prompt should be paired with a verifiable response or outcome. Your verifier can be as simple as an exact string comparison between ground truth and sampled responses, or as advanced as enlisting Claude to judge the response. Avoid overly strict verifiers that reject correct responses due to spurious differences like formatting, punctuation, or valid alternative phrasings.

For each prompt-response pair, you can optionally also specify the tools you expect an agent to call in solving the task, to measure whether or not agents are successful in grasping each tool’s purpose during evaluation. However, because there might be multiple valid paths to solving tasks correctly, try to avoid overspecifying or overfitting to strategies.

**Running the evaluation**

We recommend running your evaluation programmatically with direct LLM API calls. Use simple agentic loops (`while`-loops wrapping alternating LLM API and tool calls): one loop for each evaluation task. Each evaluation agent should be given a single task prompt and your tools.

In your evaluation agents’ system prompts, we recommend instructing agents to output not just structured response blocks (for verification), but also reasoning and feedback blocks. Instructing agents to output these _before_ tool call and response blocks may increase LLMs’ effective intelligence by triggering chain-of-thought (CoT) behaviors.

If you’re running your evaluation with Claude, you can turn on [interleaved thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking#interleaved-thinking) for similar functionality “off-the-shelf”. This will help you probe why agents do or don’t call certain tools and highlight specific areas of improvement in tool descriptions and specs.

As well as top-level accuracy, we recommend collecting other metrics like the total runtime of individual tool calls and tasks, the total number of tool calls, the total token consumption, and tool errors. Tracking tool calls can help reveal common workflows that agents pursue and offer some opportunities for tools to consolidate.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F3f1f47e80974750cd924bc51e42b6df1ad997fab-1920x1080.png&w=3840&q=75Held-out test set performance of our internal Asana tools

**Analyzing results**

Agents are your helpful partners in spotting issues and providing feedback on everything from contradictory tool descriptions to inefficient tool implementations and confusing tool schemas. However, keep in mind that what agents omit in their feedback and responses can often be more important than what they include. LLMs don’t always [say what they mean](https://www.anthropic.com/research/tracing-thoughts-language-model).

Observe where your agents get stumped or confused. Read through your evaluation agents’ reasoning and feedback (or CoT) to identify rough edges. Review the raw transcripts (including tool calls and tool responses) to catch any behavior not explicitly described in the agent’s CoT. Read between the lines; remember that your evaluation agents don’t necessarily know the correct answers and strategies.

Analyze your tool calling metrics. Lots of redundant tool calls might suggest some rightsizing of pagination or token limit parameters is warranted; lots of tool errors for invalid parameters might suggest tools could use clearer descriptions or better examples. When we launched Claude’s [web search tool](https://www.anthropic.com/news/web-search), we identified that Claude was needlessly appending `2025` to the tool’s `query` parameter, biasing search results and degrading performance (we steered Claude in the right direction by improving the tool description).

### Collaborating with agents

You can even let agents analyze your results and improve your tools for you. Simply concatenate the transcripts from your evaluation agents and paste them into Claude Code. Claude is an expert at analyzing transcripts and refactoring lots of tools all at once—for example, to ensure tool implementations and descriptions remain self-consistent when new changes are made.

In fact, most of the advice in this post came from repeatedly optimizing our internal tool implementations with Claude Code. Our evaluations were created on top of our internal workspace, mirroring the complexity of our internal workflows, including real projects, documents, and messages.

We relied on held-out test sets to ensure we did not overfit to our “training” evaluations. These test sets revealed that we could extract additional performance improvements even beyond what we achieved with "expert" tool implementations—whether those tools were manually written by our researchers or generated by Claude itself.

In the next section, we’ll share some of what we learned from this process.

## Principles for writing effective tools

In this section, we distill our learnings into a few guiding principles for writing effective tools.

### Choosing the right tools for agents

More tools don’t always lead to better outcomes. A common error we’ve observed is tools that merely wrap existing software functionality or API endpoints—whether or not the tools are appropriate for agents. This is because agents have distinct “affordances” to traditional software—that is, they have different ways of perceiving the potential actions they can take with those tools

LLM agents have limited "context" (that is, there are limits to how much information they can process at once), whereas computer memory is cheap and abundant. Consider the task of searching for a contact in an address book. Traditional software programs can efficiently store and process a list of contacts one at a time, checking each one before moving on.

However, if an LLM agent uses a tool that returns ALL contacts and then has to read through each one token-by-token, it's wasting its limited context space on irrelevant information (imagine searching for a contact in your address book by reading each page from top-to-bottom—that is, via brute-force search). The better and more natural approach (for agents and humans alike) is to skip to the relevant page first (perhaps finding it alphabetically).

We recommend building a few thoughtful tools targeting specific high-impact workflows, which match your evaluation tasks and scaling up from there. In the address book case, you might choose to implement a `search_contacts` or `message_contact` tool instead of a `list_contacts` tool.

Tools can consolidate functionality, handling potentially _multiple_ discrete operations (or API calls) under the hood. For example, tools can enrich tool responses with related metadata or handle frequently chained, multi-step tasks in a single tool call.

Here are some examples:

- Instead of implementing a `list_users`, `list_events`, and `create_event` tools, consider implementing a `schedule_event` tool which finds availability and schedules an event.
- Instead of implementing a `read_logs` tool, consider implementing a `search_logs` tool which only returns relevant log lines and some surrounding context.
- Instead of implementing `get_customer_by_id`, `list_transactions`, and `list_notes` tools, implement a `get_customer_context` tool which compiles all of a customer’s recent & relevant information all at once.

Make sure each tool you build has a clear, distinct purpose. Tools should enable agents to subdivide and solve tasks in much the same way that a human would, given access to the same underlying resources, and simultaneously reduce the context that would have otherwise been consumed by intermediate outputs.

Too many tools or overlapping tools can also distract agents from pursuing efficient strategies. Careful, selective planning of the tools you build (or don’t build) can really pay off.

### Namespacing your tools

Your AI agents will potentially gain access to dozens of MCP servers and hundreds of different tools–including those by other developers. When tools overlap in function or have a vague purpose, agents can get confused about which ones to use.

Namespacing (grouping related tools under common prefixes) can help delineate boundaries between lots of tools; MCP clients sometimes do this by default. For example, namespacing tools by service (e.g., `asana_search`, `jira_search`) and by resource (e.g., `asana_projects_search`, `asana_users_search`), can help agents select the right tools at the right time.

We have found selecting between prefix- and suffix-based namespacing to have non-trivial effects on our tool-use evaluations. Effects vary by LLM and we encourage you to choose a naming scheme according to your own evaluations.

Agents might call the wrong tools, call the right tools with the wrong parameters, call too few tools, or process tool responses incorrectly. By selectively implementing tools whose names reflect natural subdivisions of tasks, you simultaneously reduce the number of tools and tool descriptions loaded into the agent’s context and offload agentic computation from the agent’s context back into the tool calls themselves. This reduces an agent’s overall risk of making mistakes.

### Returning meaningful context from your tools

In the same vein, tool implementations should take care to return only high signal information back to agents. They should prioritize contextual relevance over flexibility, and eschew low-level technical identifiers (for example: `uuid`, `256px_image_url`, `mime_type`). Fields like `name`, `image_url`, and `file_type` are much more likely to directly inform agents’ downstream actions and responses.

Agents also tend to grapple with natural language names, terms, or identifiers significantly more successfully than they do with cryptic identifiers. We’ve found that merely resolving arbitrary alphanumeric UUIDs to more semantically meaningful and interpretable language (or even a 0-indexed ID scheme) significantly improves Claude’s precision in retrieval tasks by reducing hallucinations.

In some instances, agents may require the flexibility to interact with both natural language and technical identifiers outputs, if only to trigger downstream tool calls (for example, `search_user(name=’jane’)` → `send_message(id=12345)`). You can enable both by exposing a simple `response_format` enum parameter in your tool, allowing your agent to control whether tools return `“concise”` or `“detailed”` responses (images below).

You can add more formats for even greater flexibility, similar to GraphQL where you can choose exactly which pieces of information you want to receive. Here is an example ResponseFormat enum to control tool response verbosity:

```
enum ResponseFormat {
   DETAILED = "detailed",
   CONCISE = "concise"
}
```

Copy

Here’s an example of a detailed tool response (206 tokens):

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5ed0d30526bf68624f335d075b8c1541be3bb595-1920x1006.png&w=3840&q=75

Here’s an example of a concise tool response (72 tokens):

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd4f649a66482efb5a80cf14ea85e84974ede1c49-1920x725.png&w=3840&q=75Slack threads and thread replies are identified by unique `thread_ts` which are required to fetch thread replies. `thread_ts` and other IDs (`channel_id`, `user_id`) can be retrieved from a `“detailed”` tool response to enable further tool calls that require these. `“concise”` tool responses return only thread content and exclude IDs. In this example, we use ~⅓ of the tokens with `“concise”` tool responses.

Even your tool response structure—for example XML, JSON, or Markdown—can have an impact on evaluation performance: there is no one-size-fits-all solution. This is because LLMs are trained on next-token prediction and tend to perform better with formats that match their training data. The optimal response structure will vary widely by task and agent. We encourage you to select the best response structure based on your own evaluation.

### Optimizing tool responses for token efficiency

Optimizing the quality of context is important. But so is optimizing the _quantity_ of context returned back to agents in tool responses.

We suggest implementing some combination of pagination, range selection, filtering, and/or truncation with sensible default parameter values for any tool responses that could use up lots of context. For Claude Code, we restrict tool responses to 25,000 tokens by default. We expect the effective context length of agents to grow over time, but the need for context-efficient tools to remain.

If you choose to truncate responses, be sure to steer agents with helpful instructions. You can directly encourage agents to pursue more token-efficient strategies, like making many small and targeted searches instead of a single, broad search for a knowledge retrieval task. Similarly, if a tool call raises an error (for example, during input validation), you can prompt-engineer your error responses to clearly communicate specific and actionable improvements, rather than opaque error codes or tracebacks.

Here’s an example of a truncated tool response:

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe440d6a69d0ca80e71f3bec5c2d00906ff03ce6d-1920x1162.png&w=3840&q=75

Here’s an example of an unhelpful error response:

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2445187904704fec8c50af0b950e310ba743fac2-1920x733.png&w=3840&q=75

Here’s an example of a helpful error response:

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F810661bd44a35fb273806ae95160040155978c3e-1920x850.png&w=3840&q=75Tool truncation and error responses can steer agents towards more token-efficient tool-use behaviors (using filters or pagination) or give examples of correctly formatted tool inputs.

### Prompt-engineering your tool descriptions

We now come to one of the most effective methods for improving tools: prompt-engineering your tool descriptions and specs. Because these are loaded into your agents’ context, they can collectively steer agents toward effective tool-calling behaviors.

When writing tool descriptions and specs, think of how you would describe your tool to a new hire on your team. Consider the context that you might implicitly bring—specialized query formats, definitions of niche terminology, relationships between underlying resources—and make it explicit. Avoid ambiguity by clearly describing (and enforcing with strict data models) expected inputs and outputs. In particular, input parameters should be unambiguously named: instead of a parameter named `user`, try a parameter named `user_id`.

With your evaluation you can measure the impact of your prompt engineering with greater confidence. Even small refinements to tool descriptions can yield dramatic improvements. Claude Sonnet 3.5 achieved state-of-the-art performance on the [SWE-bench Verified](https://www.anthropic.com/engineering/swe-bench-sonnet) evaluation after we made precise refinements to tool descriptions, dramatically reducing error rates and improving task completion.

You can find other best practices for tool definitions in our [Developer Guide](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#best-practices-for-tool-definitions). If you’re building tools for Claude, we also recommend reading about how tools are dynamically loaded into Claude’s [system prompt](https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/implement-tool-use#tool-use-system-prompt). Lastly, if you’re writing tools for an MCP server, [tool annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) help disclose which tools require open-world access or make destructive changes.

## Looking ahead

To build effective tools for agents, we need to re-orient our software development practices from predictable, deterministic patterns to non-deterministic ones.

Through the iterative, evaluation-driven process we’ve described in this post, we've identified consistent patterns in what makes tools successful: Effective tools are intentionally and clearly defined, use agent context judiciously, can be combined together in diverse workflows, and enable agents to intuitively solve real-world tasks.

In the future, we expect the specific mechanisms through which agents interact with the world to evolve—from updates to the MCP protocol to upgrades to the underlying LLMs themselves. With a systematic, evaluation-driven approach to improving tools for agents, we can ensure that as agents become more capable, the tools they use will evolve alongside them.

## Acknowledgements

Written by Ken Aizawa with valuable contributions from colleagues across Research (Barry Zhang, Zachary Witten, Daniel Jiang, Sami Al-Sheikh, Matt Bell, Maggie Vo), MCP (Theodora Chu, John Welsh, David Soria Parra, Adam Jones), Product Engineering (Santiago Seira), Marketing (Molly Vorwerck), Design (Drew Roper), and Applied AI (Christian Ryan, Alexander Bricken).

1Beyond training the underlying LLMs themselves.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/06_tools/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
Branch: dev
File: notebook.ipynb
Lines: 1,288

Estimated tokens: 9.7k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/06_tools/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 6: Tools

This notebook explores **Tools (Function Calling)**, one of the most critical building blocks of any AI Agent. 

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1.  **Understand and implement tool use (function calling)** from scratch to allow an LLM to interact with external systems.
2.  **Build a custom tool calling framework** using decorators similar to production frameworks like LangGraph.
3.  **Use Gemini's native tool calling API** for production-ready implementations.
4.  **Implement structured data extraction** using Pydantic models as tools for reliable JSON output.
5.  **Run tools in loops** to handle multi-step tasks and understand the limitations that lead to ReAct patterns.
"""

"""
## 1. Setup

First, let's install the necessary Python libraries using pip.
"""

"""
!pip install -q google-genai pydantic python-dotenv
"""

"""
### Configure Gemini API Key

To use the Gemini API, you need an API key. 

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Create a file named `.env` in the root of this project.
3.  Add the following line to the `.env` file, replacing `your_api_key_here` with your actual key:
    ```
    GOOGLE_API_KEY="your_api_key_here"
    ```
The code below will load this key from the `.env` file.
"""

%load_ext autoreload
%autoreload 2

from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/pauliusztin/Documents/01_projects/TAI/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import json
from typing import Any

from google import genai
from google.genai import types
from pydantic import BaseModel, Field

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast, cost-effective, and supports advanced features like tool use. We also define a sample financial document that will be used throughout our examples.
"""

MODEL_ID = "gemini-2.5-flash"

DOCUMENT = """
# Q3 2023 Financial Performance Analysis

The Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, 
beating market expectations. These impressive results reflect our successful product strategy 
and strong market positioning.

Our core business segments demonstrated remarkable resilience, with digital services leading 
the growth at 25% year-over-year. The expansion into new markets has proven particularly 
successful, contributing to 30% of the total revenue increase.

Customer acquisition costs decreased by 10% while retention rates improved to 92%, 
marking our best performance to date. These metrics, combined with our healthy cash flow 
position, provide a strong foundation for continued growth into Q4 and beyond.
"""

"""
## 2. Implementing tool calls from scratch

LLMs are trained on text and can't perform actions in the real world on their own. Tools (or Function Calling) are the mechanism we use to bridge this gap. We provide the LLM with a list of available tools, and it can decide which one to use and with what arguments to fulfill a user's request.

The process of calling a tool looks as follows:

1. **You:** Send the LLM a prompt and a list of available tools.
2. **LLM:** Responds with a function_call request, specifying the tool and arguments.
3. **You:** Execute the requested function in your code.
4. **You:** Send the function's output back to the LLM.
5. **LLM:** Uses the tool's output to generate a final, user-facing response.

"""

"""
### Define Mock Tools

Let's create three simple, mocked functions. One simulates searching Google Drive, another simulates sending a Discord message, and the last one simulates summarizing a document. 

The function signature (input parameters and output type) and docstrings are crucial, as the LLM uses them to understand what each tool does.
"""

def search_google_drive(query: str) -> dict:
    """
    Searches for a file on Google Drive and returns its content or a summary.

    Args:
        query (str): The search query to find the file, e.g., 'Q3 earnings report'.

    Returns:
        dict: A dictionary representing the search results, including file names and summaries.
    """

    # In a real scenario, this would interact with the Google Drive API.
    # Here, we mock the response for demonstration.
    return {
        "files": [
            {
                "name": "Q3_Earnings_Report_2024.pdf",
                "id": "file12345",
                "content": DOCUMENT,
            }
        ]
    }


def send_discord_message(channel_id: str, message: str) -> dict:
    """
    Sends a message to a specific Discord channel.

    Args:
        channel_id (str): The ID of the channel to send the message to, e.g., '#finance'.
        message (str): The content of the message to send.

    Returns:
        dict: A dictionary confirming the action, e.g., {"status": "success"}.
    """

    # Mocking a successful API call to Discord.
    return {
        "status": "success",
        "status_code": 200,
        "channel": channel_id,
        "message_preview": f"{message[:50]}...",
    }


def summarize_financial_report(text: str) -> str:
    """
    Summarizes a financial report.

    Args:
        text (str): The text to summarize.

    Returns:
        str: The summary of the text.
    """

    return "The Q3 2023 earnings report shows strong performance across all metrics \
with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and \
improved retention rates of 92%."

"""
Now we need to define the metadata for each function, which will be used as input to the LLM to understand what tool to use and how to call it:
"""

search_google_drive_schema = {
    "name": "search_google_drive",
    "description": "Searches for a file on Google Drive and returns its content or a summary.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query to find the file, e.g., 'Q3 earnings report'.",
            }
        },
        "required": ["query"],
    },
}

send_discord_message_schema = {
    "name": "send_discord_message",
    "description": "Sends a message to a specific Discord channel.",
    "parameters": {
        "type": "object",
        "properties": {
            "channel_id": {
                "type": "string",
                "description": "The ID of the channel to send the message to, e.g., '#finance'.",
            },
            "message": {
                "type": "string",
                "description": "The content of the message to send.",
            },
        },
        "required": ["channel_id", "message"],
    },
}

summarize_financial_report_schema = {
    "name": "summarize_financial_report",
    "description": "Summarizes a financial report.",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The text to summarize.",
            },
        },
        "required": ["text"],
    },
}


"""
Ultimately, we will aggregate all the tools in a single dictionary:
"""

TOOLS = {
    "search_google_drive": {
        "handler": search_google_drive,
        "declaration": search_google_drive_schema,
    },
    "send_discord_message": {
        "handler": send_discord_message,
        "declaration": send_discord_message_schema,
    },
    "summarize_financial_report": {
        "handler": summarize_financial_report,
        "declaration": summarize_financial_report_schema,
    },
}
TOOLS_BY_NAME = {tool_name: tool["handler"] for tool_name, tool in TOOLS.items()}
TOOLS_SCHEMA = [tool["declaration"] for tool in TOOLS.values()]

"""
Let's take a look at them:
"""

for tool_name, tool in TOOLS_BY_NAME.items():
    print(f"Tool name: {tool_name}")
    print(f"Tool handler: {tool}")
    print("-" * 75)
# Output:
#   Tool name: search_google_drive

#   Tool handler: <function search_google_drive at 0x104c7df80>

#   ---------------------------------------------------------------------------

#   Tool name: send_discord_message

#   Tool handler: <function send_discord_message at 0x104c7de40>

#   ---------------------------------------------------------------------------

#   Tool name: summarize_financial_report

#   Tool handler: <function summarize_financial_report at 0x1274f5c60>

#   ---------------------------------------------------------------------------


pretty_print.wrapped(json.dumps(TOOLS_SCHEMA[0], indent=2), title="`search_google_drive` Tool Schema")
# Output:
#   [93m-------------------------------- `search_google_drive` Tool Schema --------------------------------[0m

#     {

#     "name": "search_google_drive",

#     "description": "Searches for a file on Google Drive and returns its content or a summary.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "query": {

#           "type": "string",

#           "description": "The search query to find the file, e.g., 'Q3 earnings report'."

#         }

#       },

#       "required": [

#         "query"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


pretty_print.wrapped(json.dumps(TOOLS_SCHEMA[1], indent=2), title="`send_discord_message` Tool Schema")
# Output:
#   [93m-------------------------------- `send_discord_message` Tool Schema --------------------------------[0m

#     {

#     "name": "send_discord_message",

#     "description": "Sends a message to a specific Discord channel.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "channel_id": {

#           "type": "string",

#           "description": "The ID of the channel to send the message to, e.g., '#finance'."

#         },

#         "message": {

#           "type": "string",

#           "description": "The content of the message to send."

#         }

#       },

#       "required": [

#         "channel_id",

#         "message"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Now, let's see how to call these tools using an LLM. First, we need to define the system prompt:
"""

TOOL_CALLING_SYSTEM_PROMPT = """
You are a helpful AI assistant with access to tools that enable you to take actions and retrieve information to better 
assist users.

## Tool Usage Guidelines

**When to use tools:**
- When you need information that is not in your training data
- When you need to perform actions in external systems and environments
- When you need real-time, dynamic, or user-specific data
- When computational operations are required

**Tool selection:**
- Choose the most appropriate tool based on the user's specific request
- If multiple tools could work, select the one that most directly addresses the need
- Consider the order of operations for multi-step tasks

**Parameter requirements:**
- Provide all required parameters with accurate values
- Use the parameter descriptions to understand expected formats and constraints
- Ensure data types match the tool's requirements (strings, numbers, booleans, arrays)

## Tool Call Format

When you need to use a tool, output ONLY the tool call in this exact format:

```tool_call
{{"name": "tool_name", "args": {{"param1": "value1", "param2": "value2"}}}}
```

**Critical formatting rules:**
- Use double quotes for all JSON strings
- Ensure the JSON is valid and properly escaped
- Include ALL required parameters
- Use correct data types as specified in the tool definition
- Do not include any additional text or explanation in the tool call

## Response Behavior

- If no tools are needed, respond directly to the user with helpful information
- If tools are needed, make the tool call first, then provide context about what you're doing
- After receiving tool results, provide a clear, user-friendly explanation of the outcome
- If a tool call fails, explain the issue and suggest alternatives when possible

## Available Tools

<tool_definitions>
{tools}
</tool_definitions>

Remember: Your goal is to be maximally helpful to the user. Use tools when they add value, but don't use them unnecessarily. Always prioritize accuracy and user experience.
"""


"""
Let's try the prompt with a few examples.
"""

USER_PROMPT = """
Can you help me find the latest quarterly report and share key insights with the team?
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)

pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive", "args": {"query": "latest quarterly report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(TOOLS_SCHEMA)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
The next step is to parse the LLM response and call the tool using Python.

First, we parse the LLM output to extract the JSON from the response:
"""

def extract_tool_call(response_text: str) -> str:
    """
    Extracts the tool call from the response text.
    """
    return response_text.split("```tool_call")[1].split("```")[0].strip()


tool_call_str = extract_tool_call(response.text)
tool_call_str
# Output:
#   '{"name": "search_google_drive", "args": {"query": "Q3 earnings report"}}'

"""
Next, we parse the stringified JSON to a Python dict:
"""

tool_call = json.loads(tool_call_str)
tool_call
# Output:
#   {'name': 'search_google_drive', 'args': {'query': 'Q3 earnings report'}}

"""
Now, we retrieve the tool handler, which is a Python function:
"""

tool_handler = TOOLS_BY_NAME[tool_call["name"]]
tool_handler
# Output:
#   <function __main__.search_google_drive(query: str) -> dict>

"""
Ultimately, we call the Python function using the arguments generated by the LLM:
"""

tool_result = tool_handler(**tool_call["args"])
pretty_print.wrapped(tool_result, indent=2, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
We can summarize the tool execution in the following function:
"""

def call_tool(response_text: str, tools_by_name: dict) -> Any:
    """
    Call a tool based on the response from the LLM.
    """

    tool_call_str = extract_tool_call(response_text)
    tool_call = json.loads(tool_call_str)
    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool = tools_by_name[tool_name]

    return tool(**tool_args)

pretty_print.wrapped(
    json.dumps(call_tool(response.text, tools_by_name=TOOLS_BY_NAME), indent=2), title="LLM Tool Call Response"
)
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Usually we want the LLM to interpret the tool output:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=f"Interpret the tool result: {json.dumps(tool_result, indent=2)}",
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     The tool result provides the content of a file named `Q3_Earnings_Report_2024.pdf`.

#   

#   This document is a **Q3 2023 Financial Performance Analysis** and details exceptionally strong results, significantly beating market expectations.

#   

#   **Key highlights from the report include:**

#   

#   *   **Revenue Growth:** A 20% increase in revenue.

#   *   **User Engagement:** 15% growth in user engagement.

#   *   **Core Business Performance:** Digital services led growth at 25% year-over-year.

#   *   **Market Expansion Success:** New markets contributed 30% of the total revenue increase.

#   *   **Efficiency & Retention:**

#       *   Customer acquisition costs decreased by 10%.

#       *   Retention rates improved to 92%, marking the best performance to date.

#   *   **Financial Health:** The company maintains a healthy cash flow position.

#   

#   The report attributes these impressive results to a successful product strategy and strong market positioning, indicating a robust foundation for continued growth into Q4 and beyond.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
That's the basic concept of tool calling! We've successfully implemented function calling from scratch.
"""

"""
## 3. Implementing tool calls from scratch using @tool decorators
"""

"""
For a better analogy with what we see in frameworks such as LangGraph or MCP, let's define a `@tool` decorator that automatically computes the schemas defined above based on the function signature and docstring:
"""

from inspect import Parameter, signature
from typing import Any, Callable, Dict, Optional


class ToolFunction:
    def __init__(self, func: Callable, schema: Dict[str, Any]) -> None:
        self.func = func
        self.schema = schema
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self.func(*args, **kwargs)


def tool(description: Optional[str] = None) -> Callable[[Callable], ToolFunction]:
    """
    A decorator that creates a tool schema from a function.

    Args:
        description: Optional override for the function's docstring

    Returns:
        A decorator function that wraps the original function and adds a schema
    """

    def decorator(func: Callable) -> ToolFunction:
        # Get function signature
        sig = signature(func)

        # Create parameters schema
        properties = {}
        required = []

        for param_name, param in sig.parameters.items():
            # Skip self for methods
            if param_name == "self":
                continue

            param_schema = {
                "type": "string",  # Default to string, can be enhanced with type hints
                "description": f"The {param_name} parameter",  # Default description
            }

            # Add to required if parameter has no default value
            if param.default == Parameter.empty:
                required.append(param_name)

            properties[param_name] = param_schema

        # Create the tool schema
        schema = {
            "name": func.__name__,
            "description": description or func.__doc__ or f"Executes the {func.__name__} function.",
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            },
        }

        return ToolFunction(func, schema)

    return decorator


@tool()
def search_google_drive_example(query: str) -> dict:
    """Search for files in Google Drive."""
    return {"files": ["Q3 earnings report"]}


@tool()
def send_discord_message_example(channel_id: str, message: str) -> dict:
    """Send a message to a Discord channel."""
    return {"message": "Message sent successfully"}


@tool()
def summarize_financial_report_example(text: str) -> str:
    """Summarize the contents of a financial report."""
    return "Financial report summarized successfully"


tools = [
    search_google_drive_example,
    send_discord_message_example,
    summarize_financial_report_example,
]
tools_by_name = {tool.schema["name"]: tool.func for tool in tools}
tools_schema = [tool.schema for tool in tools]

"""
After the function has been decorated, it has been wrapped into a `ToolFunction` object:
"""

type(search_google_drive_example)
# Output:
#   __main__.ToolFunction

"""
Which has the following fields:
"""

pretty_print.wrapped(json.dumps(search_google_drive_example.schema, indent=2), title="Search Google Drive Example")
# Output:
#   [93m----------------------------------- Search Google Drive Example -----------------------------------[0m

#     {

#     "name": "search_google_drive_example",

#     "description": "Search for files in Google Drive.",

#     "parameters": {

#       "type": "object",

#       "properties": {

#         "query": {

#           "type": "string",

#           "description": "The query parameter"

#         }

#       },

#       "required": [

#         "query"

#       ]

#     }

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
...and the actual function handler:
"""

search_google_drive_example.func
# Output:
#   <function __main__.search_google_drive_example(query: str) -> dict>

"""
Let's see how this new method works with LLMs:
"""

USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [TOOL_CALLING_SYSTEM_PROMPT.format(tools=str(tools_schema)), USER_PROMPT]

response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
)
pretty_print.wrapped(response.text, title="LLM Tool Call Response")
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     ```tool_call

#   {"name": "search_google_drive_example", "args": {"query": "Q3 earnings report"}}

#   ```

#   [93m----------------------------------------------------------------------------------------------------[0m


pretty_print.wrapped(
    json.dumps(call_tool(response.text, tools_by_name=tools_by_name), indent=2), title="LLM Tool Call Response"
)
# Output:
#   [93m-------------------------------------- LLM Tool Call Response --------------------------------------[0m

#     {

#     "files": [

#       "Q3 earnings report"

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Voilà! We have our little tool calling framework.
"""

"""
## 4. Implementing tool calls with Gemini's Native API

In production, most of the time, we don't implement tool calling from scratch, but instead leverage the native interface of a specific API such as Gemini or OpenAI. So, let's see how we can use Gemini's built-in tool calling capabilities instead of our custom implementation.
"""

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(**search_google_drive_schema),
            types.FunctionDeclaration(**send_discord_message_schema),
        ]
    )
]
config = types.GenerateContentConfig(
    tools=tools,
    # Force the model to call 'any' function, instead of chatting.
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)


pretty_print.wrapped(USER_PROMPT, title="User Prompt")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=USER_PROMPT,
    config=config,
)
# Output:
#   [93m------------------------------------------- User Prompt -------------------------------------------[0m

#     

#   Please find the Q3 earnings report on Google Drive and send a summary of it to 

#   the #finance channel on Discord.

#   

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
As you can see, here we don't explictly define a system prompt that guides the LLM how to use the tools. Instead we pass the tools schema to the LLM provider which will handle them internally. This is more efficient, as they take care of optimizing tool/function calling for every specific model.
"""

response_message_part = response.candidates[0].content.parts[0]
function_call = response_message_part.function_call
function_call
# Output:
#   FunctionCall(id=None, args={'query': 'Q3 earnings report'}, name='search_google_drive')

tool_handler = TOOLS_BY_NAME[function_call.name]
tool_handler
# Output:
#   <function __main__.search_google_drive(query: str) -> dict>

tool_handler(**function_call.args)
# Output:
#   {'files': [{'name': 'Q3_Earnings_Report_2024.pdf',

#      'id': 'file12345',

#      'content': '\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n'}]}

"""
Now let's create a simplified function that works with Gemini's native function call objects:
"""

def call_tool(function_call) -> Any:
    tool_name = function_call.name
    tool_args = function_call.args

    tool_handler = TOOLS_BY_NAME[tool_name]

    return tool_handler(**tool_args)

tool_result = call_tool(response_message_part.function_call)
pretty_print.wrapped(tool_result, indent=2, title="Tool Result")
# Output:
#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 5. Using a Pydantic Model as a Tool for Structured Outputs

A more elegant and powerful pattern is to treat our Pydantic model *as a tool*. We can ask the model to "call" this Pydantic tool, and the arguments it generates will be our structured data.

This combines the power of function calling with the robustness of Pydantic for structured data extraction. It's the recommended approach for complex data extraction tasks.

Let's define the same Pydantic model as in the structured outputs lesson:
"""

class DocumentMetadata(BaseModel):
    """A class to hold structured metadata for a document."""

    summary: str = Field(description="A concise, 1-2 sentence summary of the document.")
    tags: list[str] = Field(description="A list of 3-5 high-level tags relevant to the document.")
    keywords: list[str] = Field(description="A list of specific keywords or concepts mentioned.")
    quarter: str = Field(description="The quarter of the financial year described in the document (e.g., Q3 2023).")
    growth_rate: str = Field(description="The growth rate of the company described in the document (e.g., 10%).")

"""
Now, let's see how to use it as a tool:
"""

# The Pydantic class 'DocumentMetadata' is now our 'tool'
extraction_tool = types.Tool(
    function_declarations=[
        types.FunctionDeclaration(
            name="extract_metadata",
            description="Extracts structured metadata from a financial document.",
            parameters=DocumentMetadata.model_json_schema(),
        )
    ]
)
config = types.GenerateContentConfig(
    tools=[extraction_tool],
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)

prompt = f"""
Please analyze the following document and extract its metadata.

Document:
--- 
{DOCUMENT}
--- 
"""

response = client.models.generate_content(model=MODEL_ID, contents=prompt, config=config)
response_message_part = response.candidates[0].content.parts[0]

if hasattr(response_message_part, "function_call"):
    function_call = response_message_part.function_call
    pretty_print.function_call(function_call, title="Function Call")

    try:
        document_metadata = DocumentMetadata(**function_call.args)
        pretty_print.wrapped(document_metadata.model_dump_json(indent=2), title="Pydantic Validated Object")
    except Exception as e:
        pretty_print.wrapped(f"Validation failed: {e}", title="Validation Error")
else:
    pretty_print.wrapped("The model did not call the extraction tool.", title="No Function Call")
# Output:
#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `extract_metadata

#     [38;5;208mFunction Arguments:[0m `{

#     "growth_rate": "20%",

#     "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy and market expansion. This performance provides a strong foundation for continued growth.",

#     "quarter": "Q3 2023",

#     "keywords": [

#       "Revenue",

#       "User Engagement",

#       "Market Expansion",

#       "Customer Acquisition",

#       "Retention Rates",

#       "Digital Services",

#       "Cash Flow"

#     ],

#     "tags": [

#       "Financials",

#       "Earnings",

#       "Growth",

#       "Business Strategy",

#       "Market Analysis"

#     ]

#   }`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------ Pydantic Validated Object ------------------------------------[0m

#     {

#     "summary": "The Q3 2023 earnings report shows a 20% increase in revenue and 15% growth in user engagement, driven by successful product strategy and market expansion. This performance provides a strong foundation for continued growth.",

#     "tags": [

#       "Financials",

#       "Earnings",

#       "Growth",

#       "Business Strategy",

#       "Market Analysis"

#     ],

#     "keywords": [

#       "Revenue",

#       "User Engagement",

#       "Market Expansion",

#       "Customer Acquisition",

#       "Retention Rates",

#       "Digital Services",

#       "Cash Flow"

#     ],

#     "quarter": "Q3 2023",

#     "growth_rate": "20%"

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
## 6. Running Tools in a Loop

Now, let's implement a more sophisticated approach where we put tool calling in a loop with a conversation history. This allows the agent to perform multi-step tasks by calling multiple tools in sequence. Let's create a scenario where we ask the agent to find a report on Google Drive and then communicate its findings on Discord.
"""

tools = [
    types.Tool(
        function_declarations=[
            types.FunctionDeclaration(**search_google_drive_schema),
            types.FunctionDeclaration(**send_discord_message_schema),
            types.FunctionDeclaration(**summarize_financial_report_schema),
        ]
    )
]
config = types.GenerateContentConfig(
    tools=tools,
    tool_config=types.ToolConfig(function_calling_config=types.FunctionCallingConfig(mode="ANY")),
)


USER_PROMPT = """
Please find the Q3 earnings report on Google Drive and send a summary of it to 
the #finance channel on Discord.
"""

messages = [USER_PROMPT]

pretty_print.wrapped(USER_PROMPT, title="User Prompt")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=messages,
    config=config,
)
response_message_part = response.candidates[0].content.parts[0]
pretty_print.function_call(response_message_part.function_call, title="Function Call")

messages.append(response.candidates[0].content)

# Loop until the model stops requesting function calls or we reach the max number of iterations
max_iterations = 3
while hasattr(response_message_part, "function_call") and max_iterations > 0:
    tool_result = call_tool(response_message_part.function_call)
    pretty_print.wrapped(tool_result, title="Tool Result", indent=2)

    # Add the tool result to the messages creating the following structure:
    # - user prompt
    # - tool call
    # - tool result
    # - tool call
    # - tool result
    # ...
    function_response_part = types.Part.from_function_response(
        name=response_message_part.function_call.name,
        response={"result": tool_result},
    )
    messages.append(function_response_part)

    # Ask the LLM to continue with the next step (which may involve calling another tool)
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=messages,
        config=config,
    )

    response_message_part = response.candidates[0].content.parts[0]
    pretty_print.function_call(response_message_part.function_call, only_name=True, title="Function Call")

    messages.append(response.candidates[0].content)

    max_iterations -= 1

pretty_print.wrapped(response.candidates[0].content, title="Final Agent Response")

# Output:
#   [93m------------------------------------------- User Prompt -------------------------------------------[0m

#     

#   Please find the Q3 earnings report on Google Drive and send a summary of it to 

#   the #finance channel on Discord.

#   

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `search_google_drive

#     [38;5;208mFunction Arguments:[0m `{

#     "query": "Q3 earnings report"

#   }`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "files": [

#       {

#         "name": "Q3_Earnings_Report_2024.pdf",

#         "id": "file12345",

#         "content": "\n# Q3 2023 Financial Performance Analysis\n\nThe Q3 earnings report shows a 20% increase in revenue and a 15% growth in user engagement, \nbeating market expectations. These impressive results reflect our successful product strategy \nand strong market positioning.\n\nOur core business segments demonstrated remarkable resilience, with digital services leading \nthe growth at 25% year-over-year. The expansion into new markets has proven particularly \nsuccessful, contributing to 30% of the total revenue increase.\n\nCustomer acquisition costs decreased by 10% while retention rates improved to 92%, \nmarking our best performance to date. These metrics, combined with our healthy cash flow \nposition, provide a strong foundation for continued growth into Q4 and beyond.\n"

#       }

#     ]

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `summarize_financial_report

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `send_discord_message

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------- Tool Result -------------------------------------------[0m

#     {

#     "status": "success",

#     "status_code": 200,

#     "channel": "#finance",

#     "message_preview": "The Q3 2023 earnings report shows strong performan..."

#   }

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------------ Function Call ------------------------------------------[0m

#     [38;5;208mFunction Name:[0m `send_discord_message

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m--------------------------------------- Final Agent Response ---------------------------------------[0m

#     ('parts', [Part(video_metadata=None, thought=None, inline_data=None, file_data=None, thought_signature=b'\n\xec\x02\x01T\xa8\\\xee?[\xd4\x1f\xc1\x14\x08\xc9\x87\xd6ij-{\xea\xd3\xa9E\xa3\x9eiG\x16\xb41\xad\x90\x92\x01\x17C=\xbc^\x90\x84T\xb3Z\x86\x1d%T\xb4\x10\xe1\x02\xf9\xa3\xcfJ\xc4+\xa1\x0b\xe4\r\xee\xc3e\xc5j\x82W\x8bP\xe55B\xbf\xe5@%\x1c_\xda1hE\x00\xeec\xb2\xc2\x9fGI\xaf\xbe\x06\xf8M\x1fm\xe1\xfd7!]\xe12\x93\x94\xdd\x19B\xba\\\xd1\x0caI\xfbR5\xd4\xa9\xa9\x06x\x86\xd0\x06\x94gq\xf9\xda\x80D\xba\x95\xd0[u\xa9V\x8fb\xf7%\xb0\xc3J\x8d\x1e\x9e\xca\xa6fP\x12\xd2\xe5G\xc7\x08\xd5R\xcdn\xf2YeFQ\x80\xcec\xd7h\x1e\xcb\x1c\xbbW\xfe\xd7\xe8\xe2\xcc\xdc\x06\x8e^\xa5m\xd5\x10Y[\x8b\xa2\x89+\x12\xb54k\x073\xfc\x0f\x9c!\x8f\x83t\xfe\xcb\xb01v\x8f\xa0\xb23c\xa7\x0b\xb7y\xd1?\xb4\xc5\xa0\xef\x01\xdc\xa0\xb7\xd1\r\x87\x9445\xeb\x08\x86\xd66m\xe4\xab)6vN\x99!\x87\x01Q-\x9cL*\x0b\x97\x1a\x0f\xb0v\x16\xb3\xfc2\xe1\x88c\xadj<\xbb^\x1b\'\xbb}\xa8l\x0c%\x83??,|\xc2mB\xb7\x95\xe2GF\xee\xf6\xf2\x95\x03\xbb\xf9\xba\xfe\x0c1J\xf2\x93\x83O\x95."Pl\x87\xa6[\x8c,b\x17,c\xa3\xd0\x19\x893P\xd9\xe8C\x93.o&8\x0f\x0c\x0c\x90e\xdb\xae\x97\xed\x12\x00\xd5\xbcV\xf0\xcf\xea', code_execution_result=None, executable_code=None, function_call=FunctionCall(id=None, args={'channel_id': '#finance', 'message': 'The Q3 2023 earnings report shows strong performance across all metrics with 20% revenue growth, 15% user engagement increase, 25% digital services growth, and improved retention rates of 92%.'}, name='send_discord_message'), function_response=None, text=None)])

#   [93m----------------------------------------------------------------------------------------------------[0m

#     ('role', 'model')

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Running tools in a loop is powerful for multi-step tasks, but this approach has limitations. It assumes the agent should call a tool at each iteration and doesn't provide explicit opportunities for the model to reason about tool outputs before deciding on the next action. The agent immediately moves to the next function call without pausing to think about what it learned or whether it should change strategy.

This limitation leads us to more sophisticated patterns like **ReAct** (Reasoning and Acting), which explicitly interleaves reasoning steps with tool calls, allowing the agent to think through problems more deliberately. We will explore ReAct patterns in the next lesson.
"""

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

<details>
<summary>Tool Calling Agent From Scratch</summary>

# Tool Calling Agent From Scratch

[00:00] Hello everybody. Welcome to the Neural Maze. So, in today's video, we are going to keep working on the project of implementing the four Agentic Patterns from scratch that we started a week ago when we implemented the Reflection Pattern. So today, we're going to move into the second pattern, that is the Tool Pattern.
[00:30] And before we begin, I'm pretty sure that you're already familiar with this pattern in a practical sense. What I mean by this is that you have probably used in the past tools in LangChain, (Speaker shows LangChain documentation for 'Tools' and 'Customizing Default Tools') LlamaIndex, (Speaker shows LlamaIndex documentation for 'Tools' and 'Tool Specs') or in CrewAI. (Speaker shows CrewAI documentation for 'Tools' and 'Key Characteristics of Tools') And the thing is that in today's video, I'm not going to teach you how to use these tools in specific frameworks. I'm just going to teach you how these tools work under the hood. And I think that's really insightful because if we really understand how things work under the hood, I think it's much easier for us to learn how to apply them in the proper way.

[01:00] So, as we did in the previous video, we are going to start with a Jupyter Notebook that covers all the theory step-by-step and then I will move into VS Code where I will show you all the abstractions and all the classes that I have implemented to make this tool more robust, to try to mimic the structure that all of these frameworks offer at this moment. You know, having like a Tool class and a Tool Agent class. Very similar to what we did with the Reflection Pattern, but with, with the Tool Pattern. Okay, so let's begin with the theory of the Tool Pattern.
[01:30] (Speaker points to a diagram titled 'Tool Pattern' showing 'Tool Use Pattern' with User Prompts, Tools A, B, C, and outputs linked to Wikipedia, Google, YouTube icons) You have this diagram right here that tries to offer a simplified, uh, description of what the pattern does or tries to implement under the hood. But basically, let's start by defining what is a tool. And a tool, let's put it in simple terms, it's just a way for the LLM to access the outside world. And what do I mean by this? Uh, remember that LLMs store all the information in their weights.
[02:00] So, when you ask an LLM about specific information, that information is going to be retrieved by the weights. But sometimes, the information stored in these weights is not enough, and we need a way for the LLM to access the outside world. And that's exactly what a tool does. A tool is just, uh, like a Python function that the LLM can access and run, and fetch some relevant results using an API or a parsing a web content or, uh, consulting, uh, Wolfram Alpha to to calculate some difficult integrals.
[02:30] But you get the point, it's a way for the LLM to get outside the information stored in its weights. Okay, so let's start by defining a simple Python function. (Speaker gestures with hands) You have it in here. So, uh, this Python function, (Speaker highlights a Python code block for `get_current_weather` function) which I'm a bit ashamed of it because it's a too simple. Uh, basically gets the current weather. And as you can see, uh, if location is, uh, Madrid, it's going to return a temperature of 25, uh, it varies on the unit that you want to to put, but given that it's Madrid, it will be Unit Celsius, so it's going to return a temperature of 25 degrees Celsius.
[03:30] And otherwise, it's going to return 58. So, as you can see, don't pay too much attention to this function because it's, uh, trivial, but, uh, it will help us to illustrate how a tool works. So, if we run this, as I was saying, if we run this function with location Madrid and Unit Celsius, it's going to return this, um, dictionary, well, this string containing a dictionary with temperature 25 and Unit, uh, Celsius. Okay. So, nothing to add about this, this is trivial. So, let's proceed.

[04:00] Now the question is, how can we make this function available to an LLM? Because, as you already know, LLMs are just NLP systems, and Natural Language Processing systems. So, they expect text as input. But we need a way to for the LLM to really understand that this is a Python function, and I can call this Python function to retrieve some relevant results. And how can we do that? Okay. So, what I propose here is to use this System Prompt. (Speaker highlights a system prompt text including XML tags for tools and tool calls) As you can see, in this System Prompt, we are telling the LLM to behave as a function-calling AI model. We are going to provide the function signatures within these XML tags, these, uh, Tools tags.
[04:30] And you may call one or more functions to assist with the user query, don't make assumptions about values, blah blah blah. Okay, but the important thing is that we are going to pass all the relevant information within these XML tags. (Speaker highlights `<tool_call>` XML tag structure with function_name and arguments) And the LLM is going to return the function call inside these XML tags. Okay, this tool underscore, uh, underscore call, sorry. You can see here an example of how we expect the LLM to return the tool call. It's going to be something like this. We are going to, uh, the LLM is going to provide a name, the name of the function, and also the arguments that we need to use to retrieve the relevant information with this Python function. And then a list of the available tools. In this case, uh, I'm just using, uh, this one, like get current weather because, uh, I needed to hardcode everything for this, uh, tiny example.
[05:30] But as you will see in the VS Code, we are going to make it automatic. So, given a Python function, we are going to retrieve all of this information, all of this, uh, function signature. It's going to be retrieved automatically in the VS Code, uh, implementation. But yeah, if you check the way the information that we are providing for each tool, you can see that we are providing the name of the tool, a description, this is something that we can get from the docstring by the way, you we will see that later. But yeah, like get the current weather in a given location, blah blah blah. And then the parameters where we are putting all the different parameters, and this is really important, the type of these parameters.
[06:30] In this case, both the location and the unit are going to be strings, but suppose that we are passing, I don't know, uh, the month, and we want it to behave like an integer, then we should put that type inside the the function signature. Okay, so now that we know how this System Prompt works, let's put it into practice. Just a quick reminder, today we are going to use a different LLM than the previous video.
[07:00] In the previous video, we were using Llama 3 70 billion, but today we are going to use a slightly different LLM because it's the Llama 3 70 billion tool use. So, it's a version of Llama 3 that's been, uh, fine-tuned for tool use. And that's exactly what we want to do today, so it made sense to to use this LLM. Okay, uh, we define, uh, a constant, uh, the System Prompt, um, where we copy and paste the System Prompt that I share with you, uh, right in in the in the cell below.
[07:30] And, and now, let's, uh, run this cell. We are going to ask the LLM, what's the current temperature in Madrid in Celsius? We're going to add the System Prompt, and we are also going to add the user, uh, message to the history. And, yeah, let's, uh, run this. Okay, so as you can see, uh, we are having, uh, a structure similar to the one we ask for the LLM to return in the System Prompt. The LLM is returning the name of the tool, and it's also returning the arguments. Since we asked, what's the current temperature in Madrid in Celsius? The arguments are going to be Madrid as the location, and Celsius as the unit. Okay?

[08:30] But now, this is not usable for the by the LLM. I mean, we have a string, and inside that string, we have this dictionary inside these two XML tags. So, we need a way to get rid of the XML tags and also transform this dictionary, this string dictionary into a proper dictionary using the JSON package, the JSON library. Okay, and that's exactly what this function does. This function will get rid of the tool call, or to be more specific, it will gather, it will get the code inside the tool call XML tags. And then, it will transform that string dictionary into a proper dictionary. So, let me show you how it works.
[09:30] Uh, but as you can see, when we call this parse tool call string, this method to the output, the output remember that it's, uh, this one here, it's going to return a proper Python dictionary. And now, if we run the get current weather, the function that we define at the beginning of the notebook, if we run this function with the parameters that we have just, uh, parsed, it will return the result. So, temperature 25 and unit, it's going to be Celsius. Okay? Without any information about the XML tags, that's something that we want to get rid of. Nice.
[10:00] Okay, so now we have the result. As you can see, it's this Python dictionary right here, but we are not over because we don't want the LLM to respond with this, uh, structure. I mean, if I ask the LLM for the current temperature in Madrid, I expect the LLM to respond me something like, the current temperature in Madrid, it's, uh, is 25 degrees Celsius, for example. But not something like this, not this, uh, dictionary. So, the last thing that we need to do is to add this observation, the dictionary in here. To the chat history. Okay? And we are going to add this into the prompt, this observation, uh, the observation text into the prompt.
[10:30] And finally, just call the the agent. And as you can see, the result, it's exactly what we expected. So, the current temperature in Madrid is 25 degrees Celsius. Okay. So, now this is everything for this dynamic or step-by-step way of doing things. But as you might imagine, this is not scalable. I mean, we can't generate these function signature for everything that we are going to build. I mean, we could, but it's not going to be efficient. We need a way for the agent to given a Python function, being able to extract the function signature.
[11:30] And by signature, I mean this type of structure right here. And also to decide between different tools. So, instead of doing all of this process, we need the agent to extract all of this logic away from the user, and to do it under the hood. And that's exactly what we are going to do right now, the logic that I'm going to show you in VS Code. How to implement all of this the proper way. So, let's get into VS Code.
_This section provided a detailed walk-through of the Tool Pattern in a Jupyter Notebook, covering its theoretical basis, implementation of a simple Python function, and how to integrate it with an LLM using a System Prompt and custom parsing logic, before concluding that this manual approach is not scalable and requires a more automated solution in VS Code._

[11:45] (Speaker is now in VS Code, showing a project structure with `agentic_patterns` folder) Okay, so here we are in VS Code. Let me show you the new modules that I have added to the repository. So, if you go to the source Agentic Patterns folder, you will find a new folder, the Tool Pattern folder. And inside, you have three modules: the Tool Agent, the Tool, and the Utils. Uh, let's begin with the Tool, because I think it's, uh, the most important topic, uh, of today's video. And the Tool Agent, at the end of the day, is just a way to interact with the tool.
[12:15] Okay, so this module starts by implementing a method that allows you to get the signature out of a Python function. So, this is basically the method I'm referring to. It receives as parameter a function, and it will, uh, get the schema and out of the schema, also the function signature. And the function signature, it's basically the structure that we defined on the System Prompt previously. All right. Next, we have this class right here, Tool class, that has three attributes: a name, the function, and the function signature. The function signature, as you might imagine, it's going to be generated by this function right here. And the function, it's basically the function that we want to call.
[13:15] When the LLM decides that it wants to use a specific tool, this function is the Python function that's going to be used under the hood. Then we have this Tool decorator that can be used to decorate your Python function, and to automatically transform the Python function into a tool object. If you inspect a little bit the implementation of this decorator, first, uh, you can see that it generates the function signature out of the get function signature method that we explained before. And then it returns a tool object by, uh, defining the name, using the function signature, passing the the function that you are decorating as the function attribute that the tool expects. And finally, getting the function signature, uh, from the variable that we defined previously because remember that we were getting the function signature using this method. And, and yeah, and having these three attributes, we are able to to generate a tool. Okay?
[14:10] Now, let's move into the Tool Agent, which as you can imagine, is an agent that has the capability of using tools. You pass a list of tools, and it will, uh, select the proper tool, the the right tool, for the specific question that you are asking, and then it will run the tool to fetch the relevant details that it needs from the outside world, and then returning all this information in, uh, Natural Language to you. Okay, so things that you are already familiar with. So, this Tools System Prompt is basically the one that we explained earlier in the in the video. And then the Tool Agent consists of the following attributes. So, it we need to generate, uh, the the Grok Client, then the model that, remember that by default, we are going to use the Llama 3 70 billion tool use.
[15:00] And then this is the the important part, this is the the tricky part of this agent, but we need to define the list of tools that we are going to to use for this agent. And then this list of tools are going to be used in the run method. So, the run method, uh, consists of the following steps. First of all, we expect this user message, and we transform the user message into a user prompt using the OpenAI API definition. Then we are going to generate both the Tool Chat History and the Agent Chat History. And now we are going to generate the first completion. We are going to make the first call to the Grok model. And what this is going to do, these two blocks of code, is to generate basically the logic that we explained in the notebook.
[16:00] Let me be specific. So, it's going to, first of all, return the tool call. Okay? This first call, uh, this Tool Call string is basically this output. And then the Parse Tool Call string, it's a method that mimics the same logic that we implemented in this function. Okay, so at the end, this Tool Call is going to be something like this. Okay, so now that we have the Tool Call information, we can get the tool name from from this object, from the Tool Call. We can also get the, um, the tool by using this tools dict because now that we have the tool name, we have also defined a dictionary that contains a relationship between, uh, the tool name and the tool. Okay?
[17:00] Then we are going to validate the arguments. So, to make sure that if, uh, the function expects a string, the LLM is not sending an integer. We want to make sure that the types that the LLM has generated in the Tool Call and the types expected by the Python function match. Okay? And then we are just going to run the tool with this Tool Run. And we are passing the arguments that we have just, uh, defined on the Tool Call. Remember that if we go to to the Tool Call, remember that we had these arguments key that contains the arguments and its values to achieve the to retrieve the the proper information. Okay? And finally, we are going to append this result to the chat history. And remember that we are adding this by using this observation prompt.
[18:00] Okay, so now the only thing that's missing is to make another call to to the LLM in Grok, and we will receive the output. Okay, so now that we understand how all of these classes and abstractions work, I think it's going to be really cool to see everything in action. And that's what we are going to cover next. So, uh, everything is inside this section of implementing everything the good way. Of course, you have to understand that this implementation, it's not like the perfect implementation because, uh, I'm not trying to create another framework. I'm just trying to make something that's, uh, well implemented, but at the same time, easy to understand.
[19:00] So, so, yeah, uh, just bear in mind that we are not trying to to create another Agentic framework in this case. Okay, so, uh, let's continue. Uh, let's see how the Tool Decorator works. And instead of using some dummy, uh, function, in this case, we are going to implement something more, uh, something closer to to reality. Something closer to the tools that you might be wanting to implement in the future. So, uh, in this case, the the function that I have implemented, it's a function that fetches the top and stories from Hacker News. If you don't know what Hacker News, uh, is, it's a very famous, uh, page where you have different types of of stories, and many of them, uh, link to some article, another to GitHub repositories, to tweets, to whatever.
[20:00] Uh, it's very, very used by by a lot of people, so I thought it would be cool to have these, uh, this function that allows you to retrieve top number of these functions, of these, uh, stories, sorry. And, and yeah, and to convert this, to transform this function into into a tool. And we are going to do it by using this method that we covered, uh, previously. Okay, so now that we have run the tool method, the HN tool, it's going to be a tool. We can access the name of the tool, and we can access the function signature that, as you can see, contains all the information that we put in the System Prompt at the beginning of the video. But right now, the cool thing is that everything, everything has been generated automatically.
[21:00] And yeah, you can see here that, uh, has a description, and the description has been retrieved from the docstring. And we have also the parameters here. Uh, in this case, it's a very simple function, so we just, uh, need this top and argument, and it's of type integer. So, everything seems to be working fine. And now, let's move into the Tool Agent. So, the Tool Agent, to instantiate this tool, we just need, uh, a list of tools. In this case, we are only using one tool, the HN tool. And now, let's, uh, run the agent. And in this case, uh, I wanted to check that everything works properly by doing the following, uh, strategy. So, first of all, I'm going to ask the agent about something that it's not related to Hacker News.
[22:00] So, for example, tell me your name. And if everything works properly, we should see, yeah, something not related with the agent, with the tool, sorry. And as you can see, uh, given the output, the agent has not used any kind of tool. And that's the proper way to work because, uh, if the user message is not related to any tool, we don't want the agent to spend time on interacting with tools. But what happens if we ask the same agent about the top five Hacker News stories right now? In this case, we should expect the agent to use the tool. And as you can see, uh, I have added some login to to make it easier to see, but check this.
[23:00] So, the agent is using the tool, the fetch top Hacker News stories. It's using the tool with this call dict. So, this is the name, and the arguments, the top end with value of five. And finally, it's generating a result. But remember that we don't want this kind of result. I mean, if I'm asking about the five top stories in Hacker News right now, I'm expecting something easier to understand. And that's what we achieve if we, uh, print the output, and here we have the five top stories in Hacker News. The first one is the the article about too much efficiency makes everything worse that we saw in the Hacker News page. And if we click the URL attached, you can see that everything seems to be working fine. I mean, it's not like the agent redirected us to some broken URLs.
[24:00] I mean, the URLs are real, and it's, uh, it's working as expected. So, yeah, this is everything I wanted to teach you about tools. My hope is that now, when you start using, or keep using, uh, tools from LangChain, LlamaIndex, or CrewAI, you have a deeper understanding how these objects, uh, work under the hood. And, and this is everything for today. I hope you have enjoyed the video. Subscribe to the channel if you haven't, and if you like the content. Click the Like button if you've you have enjoyed this video. And, I'll see you in the next video.
_This final section demonstrates how to use the custom ToolAgent with a real-world example (Hacker News API), showcasing how the agent intelligently decides whether to use a tool based on the user's query and processes the output into a readable format. It concludes the tutorial with an overview of the upcoming videos in the series._

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Building AI Agents from scratch - Part 1: Tool use</summary>

# Building AI Agents from scratch - Part 1: Tool use

**Source URL:** <https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part>

### Let's implement AI Agent from scratch without using any framework. Today we implement the tool use capability.

First of all, I want to wish you a joyful and peaceful holiday season in advance!

This is the first article in the series where we will build AI Agents from scratch without using any LLM orchestration frameworks. In this one you will learn:

- What are agents?

- How the Tool usage actually works.

- How to build a decorator wrapper that extracts relevant details from a Python function to be passed to the LLM via system prompt.

- How to think about constructing effective system prompts that can be used for Agents.

- How to build an Agent class that is able to plan and execute actions using provided Tools.

You can find the code examples for this and following projects in GitHub repository here:

[AI Engineer's Handbook](https://github.com/swirl-ai/ai-angineers-handbook)

> “The future of AI is Agentic.”

> “Year 2025 will be the year of Agents.”

These are the phrases you hear nowadays left and right. And there is a lot of truth to it. In order to bring the most business value out of LLMs, we are turning to complex agentic flows.

### What is an AI Agent?

In it’s simplest high level definition, an AI agent is an application that uses LLM at the core as it’s reasoning engine to decide on the steps it needs to take to solve for users intent. It is usually depicted similar to the picture bellow and is composed of multiple building blocks:

https://substackcdn.com/image/fetch/$s_!fVcp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eb64772-fbb5-4f2d-8120-d473c74fe124_2926x2198.png AI Agent

- Planning - the capability to plan a sequence of actions that the application needs to perform in order to solve for the provided intent.

- Memory - short-term and long-term memory containing any information that the agent might need to reason about the actions it needs to take. This information is usually passed to LLM via a system prompt as part of the core. You can read more about different types of memories in one of my previous articles:

[https://substackcdn.com/image/fetch/$s_!TLtB!,w_140,h_140,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7650705-54b4-49a3-91a4-aad0c4093c4b_2926x2198.png](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)

[**Memory in Agent Systems**](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)

[Aurimas Griciūnas](https://substack.com/profile/14122259-aurimas-griciunas)

·

October 30, 2024

[Read full story](https://www.newsletter.swirlai.com/p/memory-in-agent-systems)

- Tools - any functions that the application can call to enhance it’s reasoning capabilities. One should not be fooled by the simplicity of this definition as a tool can be literally anything:

  - Simple functions defined in code.

  - VectorDBs and other data stores containing context.

  - Regular Machine Learning model APIs.

  - Other Agents!

  - …

In the following set of articles, I will implement most of the moving parts of an agent from scratch without using any orchestration frameworks. This episode is about Tool use.

If you are using any orchestration frameworks for agentic applications, you might be abstracted away from what using a tool really means. This article will help you understand what providing a tool and using it via an agent involves. I believe that understanding applications from the base building blocks is really important for few reasons:

- Frameworks hide the implementation details of the system prompts used, different approaches might be needed in different use cases.

- You might want to tune the low level details to achieve most optimal performance of the agent.

- Having clarity of how the systems actually work helps build up your systems thinking enabling you to craft advanced applications more efficiently.

### Tool use on a high level.

The basic thing one needs to understand when building agentic applications is that LLMs do not run code, they are only used to produce intent via prompting. Why can ChatGPT browse the internet and return more accurate and recent results? Because ChatGPT IS an agent and there are many non LLM building blocks hidden from us behind the API.

Prompt engineering becomes critical when building agentic applications. More specifically, how you craft the system prompt. Simplified prompt structure looks like the following.

https://substackcdn.com/image/fetch/$s_!rZHR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F663cac67-4b46-428f-8876-d648f621f0e5_1878x766.png Prompt Structure

The agent will only perform well if you are able to efficiently provide the system prompt with available tool definitions and expected outputs which are in a form of planned actions or raw answers.

### Implementing the Agent.

In this part, we will create an AI Agent, that is capable of checking currency conversion rates online and performing the conversion if needed to answer the user query.

You can also find the code in a GitHub repository [here](https://github.com/swirl-ai/ai-angineers-handbook/tree/main/building_agents_from_scratch/tool_use).

You can follow the tutorial using the Jupyter notebook [here](https://github.com/swirl-ai/ai-angineers-handbook/blob/main/building_agents_from_scratch/tool_use/notebooks/tool_use.ipynb).

#### Preparing python functions to be used as tools.

The easiest and most convenient way to provide tools to an agent is through functions, in our project we will be using Python for this.

We do not need to provide the function code itself to the system prompt but we need to extract useful information about it so that LLM can decide if and how the function should be invoked.

We’ll define a dataclass that contains desired information including the function runnable.

```
@dataclass
class Tool:
    name: str
    description: str
    func: Callable[..., str]
    parameters: Dict[str, Dict[str, str]]

    def __call__(self, *args, **kwargs) -> str:
        return self.func(*args, **kwargs)
```

The information we are extracting includes:

- Function name.

- function description (we will extract this from a docstring).

- Function callable so that we can invoke it as part of the agent.

- Parameters that should be used with the function so that the LLM can decide on how to call the function.

Now we will need to extract the above information from the functions we define. One requirement for the functions we will enforce is to have properly formatted docstrings. We will require the following format:

```
"""Description of what the tool does.

Parameters:
    - param1: Description of first parameter
    - param2: Description of second parameter
"""
```

The following function extracts information about parameters - parameter names and descriptions.

```
def parse_docstring_params(docstring: str) -> Dict[str, str]:
    """Extract parameter descriptions from docstring."""
    if not docstring:
        return {}

    params = {}
    lines = docstring.split('\n')
    in_params = False
    current_param = None

    for line in lines:
        line = line.strip()
        if line.startswith('Parameters:'):
            in_params = True
        elif in_params:
            if line.startswith('-') or line.startswith('*'):
                current_param = line.lstrip('- *').split(':')[0].strip()
                params[current_param] = line.lstrip('- *').split(':')[1].strip()
            elif current_param and line:
                params[current_param] += ' ' + line.strip()
            elif not line:
                in_params = False

    return params
```

We will be extracting function parameter types from typehints provided via function definition. The bellow function will help format them.

```
def get_type_description(type_hint: Any) -> str:
    """Get a human-readable description of a type hint."""
    if isinstance(type_hint, _GenericAlias):
        if type_hint._name == 'Literal':
            return f"one of {type_hint.__args__}"
    return type_hint.__name__
```

A very convenient way to turn a function into a tool is to use a decorator. The below code defines a tool decorator that wraps a function if used. It uses either function name for the tool name or a variable provided via decorator.

```
def tool(name: str = None):
    def decorator(func: Callable[..., str]) -> Tool:
        tool_name = name or func.__name__
        description = inspect.getdoc(func) or "No description available"

        type_hints = get_type_hints(func)
        param_docs = parse_docstring_params(description)
        sig = inspect.signature(func)

        params = {}
        for param_name, param in sig.parameters.items():
            params[param_name] = {
                "type": get_type_description(type_hints.get(param_name, Any)),
                "description": param_docs.get(param_name, "No description available")
            }

        return Tool(
            name=tool_name,
            description=description.split('\n\n')[0],
            func=func,
            parameters=params
        )
    return decorator
```

#### Currency exchange tool.

The below creates a tool from a function that takes in the amount of currency to exchange from, the currency code to be converted from and the currency code to convert to. The function searches for the relevant currency exchange rate and performs the calculation of resulting currency amount.

```
@tool()
def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts currency using latest exchange rates.

    Parameters:
        - amount: Amount to convert
        - from_currency: Source currency code (e.g., USD)
        - to_currency: Target currency code (e.g., EUR)
    """
    try:
        url = f"https://open.er-api.com/v6/latest/{from_currency.upper()}"
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        if "rates" not in data:
            return "Error: Could not fetch exchange rates"

        rate = data["rates"].get(to_currency.upper())
        if not rate:
            return f"Error: No rate found for {to_currency}"

        converted = amount * rate
        return f"{amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"

    except Exception as e:
        return f"Error converting currency: {str(e)}"
```

Let’s just run

```
convert_currency
```

It should return something like

```
Tool(name='convert_currency', description='Converts currency using latest exchange rates.', func=<function convert_currency at 0x106d8fa60>, parameters={'amount': {'type': 'float', 'description': 'Amount to convert'}, 'from_currency': {'type': 'str', 'description': 'Source currency code (e.g., USD)'}, 'to_currency': {'type': 'str', 'description': 'Target currency code (e.g., EUR)'}})
```

This is great! We have successfully extracted information we will be providing to the LLM as a tool definition.

#### Crafting the system prompt.

We will be using gpt-4o-mini as our reasoning engine. It is known that GPT model family performs better when the input prompt is formatted as json. So we will do exactly that. Actually, the system prompt is the most important part of our agent, here is the final one we will be using:

```
{
    "role": "AI Assistant",
    "capabilities": [\
        "Using provided tools to help users when necessary",\
        "Responding directly without tools for questions that don't require tool usage",\
        "Planning efficient tool usage sequences"\
    ],
    "instructions": [\
        "Use tools only when they are necessary for the task",\
        "If a query can be answered directly, respond with a simple message instead of using tools",\
        "When tools are needed, plan their usage efficiently to minimize tool calls"\
    ],
    "tools": [\
        {\
            "name": tool.name,\
            "description": tool.description,\
            "parameters": {\
                name: {\
                    "type": info["type"],\
                    "description": info["description"]\
                }\
                for name, info in tool.parameters.items()\
            }\
        }\
        for tool in self.tools.values()\
    ],
    "response_format": {
        "type": "json",
        "schema": {
            "requires_tools": {
                "type": "boolean",
                "description": "whether tools are needed for this query"
            },
            "direct_response": {
                "type": "string",
                "description": "response when no tools are needed",
                "optional": True
            },
            "thought": {
                "type": "string",
                "description": "reasoning about how to solve the task (when tools are needed)",
                "optional": True
            },
            "plan": {
                "type": "array",
                "items": {"type": "string"},
                "description": "steps to solve the task (when tools are needed)",
                "optional": True
            },
            "tool_calls": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "tool": {
                            "type": "string",
                            "description": "name of the tool"
                        },
                        "args": {
                            "type": "object",
                            "description": "parameters for the tool"
                        }
                    }
                },
                "description": "tools to call in sequence (when tools are needed)",
                "optional": True
            }
        },
        "examples": [\
            {\
                "query": "Convert 100 USD to EUR",\
                "response": {\
                    "requires_tools": True,\
                    "thought": "I need to use the currency conversion tool to convert USD to EUR",\
                    "plan": [\
                        "Use convert_currency tool to convert 100 USD to EUR",\
                        "Return the conversion result"\
                    ],\
                    "tool_calls": [\
                        {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 100,\
                                "from_currency": "USD",\
                                "to_currency": "EUR"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What's 500 Japanese Yen in British Pounds?",\
                "response": {\
                    "requires_tools": True,\
                    "thought": "I need to convert JPY to GBP using the currency converter",\
                    "plan": [\
                        "Use convert_currency tool to convert 500 JPY to GBP",\
                        "Return the conversion result"\
                    ],\
                    "tool_calls": [\
                        {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 500,\
                                "from_currency": "JPY",\
                                "to_currency": "GBP"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What currency does Japan use?",\
                "response": {\
                    "requires_tools": False,\
                    "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
                }\
            }\
        ]
    }
}
```

A lot to unpack, let’s analyse it step by step:

```
"role": "AI Assistant",
"capabilities": [\
    "Using provided tools to help users when necessary",\
    "Responding directly without tools for questions that don't require tool usage",\
    "Planning efficient tool usage sequences"\
],
"instructions": [\
    "Use tools only when they are necessary for the task",\
    "If a query can be answered directly, respond with a simple message instead of using tools",\
    "When tools are needed, plan their usage efficiently to minimize tool calls"\
]
```

This is where we define the qualities of the Agent, in general we are enforcing the behaviour that tools should be used only when necessary.

```
"tools": [\
    {\
        "name": tool.name,\
        "description": tool.description,\
        "parameters": {\
            name: {\
                "type": info["type"],\
                "description": info["description"]\
            }\
            for name, info in tool.parameters.items()\
        }\
    }\
    for tool in self.tools.values()\
]
```

This is where we unpack the tools into a list. The tool list will be part of Agent class, that is why we loop through self.tools. Remember, each tool is defined by the Dataclass we created in the first part.

```
"response_format": {
    "type": "json",
    "schema": {
        "requires_tools": {
            "type": "boolean",
            "description": "whether tools are needed for this query"
        },
        "direct_response": {
            "type": "string",
            "description": "response when no tools are needed",
            "optional": True
        },
        "thought": {
            "type": "string",
            "description": "reasoning about how to solve the task (when tools are needed)",
            "optional": True
        },
        "plan": {
            "type": "array",
            "items": {"type": "string"},
            "description": "steps to solve the task (when tools are needed)",
            "optional": True
        },
        "tool_calls": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "tool": {
                        "type": "string",
                        "description": "name of the tool"
                    },
                    "args": {
                        "type": "object",
                        "description": "parameters for the tool"
                    }
                }
            },
            "description": "tools to call in sequence (when tools are needed)",
            "optional": True
        }
    }
}
```

Above enforces the LLM output schema. We provide strict instructions here:

- requires\_tools: return if tool usage is required.

- direct\_response: if above is false return a direct response.

- thought: description on how the task should be solved.

- plan: steps to solve the task.

- tool\_calls: tool calls in sequence including functions and parameters to be used. Our example only includes one tool, but it does not necessarily have to.

```
"examples": [\
    {\
        "query": "Convert 100 USD to EUR",\
        "response": {\
            "requires_tools": True,\
            "thought": "I need to use the currency conversion tool to convert USD to EUR",\
            "plan": [\
                "Use convert_currency tool to convert 100 USD to EUR",\
                "Return the conversion result"\
            ],\
            "tool_calls": [\
                {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 100,\
                                "from_currency": "USD",\
                                "to_currency": "EUR"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What's 500 Japanese Yen in British Pounds?",\
                "response": {\
                    "requires_tools": True,\
                    "thought": "I need to convert JPY to GBP using the currency converter",\
                    "plan": [\
                        "Use convert_currency tool to convert 500 JPY to GBP",\
                        "Return the conversion result"\
                    ],\
                    "tool_calls": [\
                        {\
                            "tool": "convert_currency",\
                            "args": {\
                                "amount": 500,\
                                "from_currency": "JPY",\
                                "to_currency": "GBP"\
                            }\
                        }\
                    ]\
                }\
            },\
            {\
                "query": "What currency does Japan use?",\
                "response": {\
                    "requires_tools": False,\
                    "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
                }\
            }\
        ]
    }
}
```

Finally, we provide some examples of correct reasoning above.

#### Implementing the Agent Class

The agent class is quite lengthy due to the long system prompt:

```
class Agent:
    def __init__(self):
        """Initialize Agent with empty tool registry."""
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.tools: Dict[str, Tool] = {}

    def add_tool(self, tool: Tool) -> None:
        """Register a new tool with the agent."""
        self.tools[tool.name] = tool

    def get_available_tools(self) -> List[str]:
        """Get list of available tool descriptions."""
        return [f"{tool.name}: {tool.description}" for tool in self.tools.values()]

    def use_tool(self, tool_name: str, **kwargs: Any) -> str:
        """Execute a specific tool with given arguments."""
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found. Available tools: {list(self.tools.keys())}")

        tool = self.tools[tool_name]
        return tool.func(**kwargs)

    def create_system_prompt(self) -> str:
        """Create the system prompt for the LLM with available tools."""
        tools_json = {
            "role": "AI Assistant",
            "capabilities": [\
                "Using provided tools to help users when necessary",\
                "Responding directly without tools for questions that don't require tool usage",\
                "Planning efficient tool usage sequences"\
            ],
            "instructions": [\
                "Use tools only when they are necessary for the task",\
                "If a query can be answered directly, respond with a simple message instead of using tools",\
                "When tools are needed, plan their usage efficiently to minimize tool calls"\
            ],
            "tools": [\
                {\
                    "name": tool.name,\
                    "description": tool.description,\
                    "parameters": {\
                        name: {\
                            "type": info["type"],\
                            "description": info["description"]\
                        }\
                        for name, info in tool.parameters.items()\
                    }\
                }\
                for tool in self.tools.values()\
            ],
            "response_format": {
                "type": "json",
                "schema": {
                    "requires_tools": {
                        "type": "boolean",
                        "description": "whether tools are needed for this query"
                    },
                    "direct_response": {
                        "type": "string",
                        "description": "response when no tools are needed",
                        "optional": True
                    },
                    "thought": {
                        "type": "string",
                        "description": "reasoning about how to solve the task (when tools are needed)",
                        "optional": True
                    },
                    "plan": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "steps to solve the task (when tools are needed)",
                        "optional": True
                    },
                    "tool_calls": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "tool": {
                                    "type": "string",
                                    "description": "name of the tool"
                                },
                                "args": {
                                    "type": "object",
                                    "description": "parameters for the tool"
                                }
                            }
                        },
                        "description": "tools to call in sequence (when tools are needed)",
                        "optional": True
                    }
                },
                "examples": [\
                    {\
                        "query": "Convert 100 USD to EUR",\
                        "response": {\
                            "requires_tools": True,\
                            "thought": "I need to use the currency conversion tool to convert USD to EUR",\
                            "plan": [\
                                "Use convert_currency tool to convert 100 USD to EUR",\
                                "Return the conversion result"\
                            ],\
                            "tool_calls": [\
                                {\
                                    "tool": "convert_currency",\
                                    "args": {\
                                        "amount": 100,\
                                        "from_currency": "USD",\
                                        "to_currency": "EUR"\
                                    }\
                                }\
                            ]\
                        }\
                    },\
                    {\
                        "query": "What's 500 Japanese Yen in British Pounds?",\
                        "response": {\
                            "requires_tools": True,\
                            "thought": "I need to convert JPY to GBP using the currency converter",\
                            "plan": [\
                                "Use convert_currency tool to convert 500 JPY to GBP",\
                                "Return the conversion result"\
                            ],\
                            "tool_calls": [\
                                {\
                                    "tool": "convert_currency",\
                                    "args": {\
                                        "amount": 500,\
                                        "from_currency": "JPY",\
                                        "to_currency": "GBP"\
                                    }\
                                }\
                            ]\
                        }\
                    },\
                    {\
                        "query": "What currency does Japan use?",\
                        "response": {\
                            "requires_tools": False,\
                            "direct_response": "Japan uses the Japanese Yen (JPY) as its official currency. This is common knowledge that doesn't require using the currency conversion tool."\
                        }\
                    }\
                ]
            }
        }

        return f"""You are an AI assistant that helps users by providing direct answers or using tools when necessary.
Configuration, instructions, and available tools are provided in JSON format below:

{json.dumps(tools_json, indent=2)}

Always respond with a JSON object following the response_format schema above.
Remember to use tools only when they are actually needed for the task."""

    def plan(self, user_query: str) -> Dict:
        """Use LLM to create a plan for tool usage."""
        messages = [\
            {"role": "system", "content": self.create_system_prompt()},\
            {"role": "user", "content": user_query}\
        ]

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0
        )

        try:
            return json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            raise ValueError("Failed to parse LLM response as JSON")

    def execute(self, user_query: str) -> str:
        """Execute the full pipeline: plan and execute tools."""
        try:
            plan = self.plan(user_query)

            if not plan.get("requires_tools", True):
                return plan["direct_response"]

            # Execute each tool in sequence
            results = []
            for tool_call in plan["tool_calls"]:
                tool_name = tool_call["tool"]
                tool_args = tool_call["args"]
                result = self.use_tool(tool_name, **tool_args)
                results.append(result)

            # Combine results
            return f"""Thought: {plan['thought']}
Plan: {'. '.join(plan['plan'])}
Results: {'. '.join(results)}"""

        except Exception as e:
            return f"Error executing plan: {str(e)}"
```

Let’s look into it step by step (skipping the create\_system\_prompt method as we already analysed it in the previous part).

```
def add_tool(self, tool: Tool) -> None:
    """Register a new tool with the agent."""
    self.tools[tool.name] = tool

def get_available_tools(self) -> List[str]:
    """Get list of available tool descriptions."""
    return [f"{tool.name}: {tool.description}" for tool in self.tools.values()]

def use_tool(self, tool_name: str, **kwargs: Any) -> str:
    """Execute a specific tool with given arguments."""
    if tool_name not in self.tools:
        raise ValueError(f"Tool '{tool_name}' not found. Available tools: {list(self.tools.keys())}")

    tool = self.tools[tool_name]
    return tool.func(**kwargs)
```

Above contain methods to manage tools:

- Attaching tools to the agent.

- List attached tools.

- Invoke execution of a tool.

```
def plan(self, user_query: str) -> Dict:
    """Use LLM to create a plan for tool usage."""
    messages = [\
        {"role": "system", "content": self.create_system_prompt()},\
        {"role": "user", "content": user_query}\
    ]

    response = self.client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    try:
        return json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("Failed to parse LLM response as JSON")
```

The above simply executes the system prompt, we defined the expected output as part of the system prompt. It exactly provides the actions that the LLM planned or a direct answer if the tool calling is not needed.

```
def execute(self, user_query: str) -> str:
    """Execute the full pipeline: plan and execute tools."""
    try:
        plan = self.plan(user_query)

        if not plan.get("requires_tools", True):
            return plan["direct_response"]

        # Execute each tool in sequence
        results = []
        for tool_call in plan["tool_calls"]:
            tool_name = tool_call["tool"]
            tool_args = tool_call["args"]
            result = self.use_tool(tool_name, **tool_args)
            results.append(result)

        # Combine results
        return f"""Thought: {plan['thought']}
Plan: {'. '.join(plan['plan'])}
Results: {'. '.join(results)}"""

    except Exception as e:
        return f"Error executing plan: {str(e)}"
```

The above executes the plan method and acts on it. You might remember that the plan can include multiple sequential tool executions, that is why we are looping through planned tool calls.

#### Running the Agent.

That’s it, we have all of the necessary code to create and use the Agent. in the following code we initialise the agent, attach a convert\_currency tool to it and loop through two user queries. First one should require the tool use while the second not.

```
agent = Agent()
agent.add_tool(convert_currency)

query_list = ["I am traveling to Japan from Serbia, I have 1500 of local currency, how much of Japanese currency will I be able to get?",\
                "How are you doing?"]

for query in query_list:
    print(f"\nQuery: {query}")
    result = agent.execute(query)
    print(result)
```

The output should be similar to:

```
Query: I am traveling to Japan from Serbia, I have 1500 of local currency, how much of Japanese currency will I be able to get?
Thought: I need to convert 1500 Serbian Dinars (RSD) to Japanese Yen (JPY) using the currency conversion tool.
Plan: Use convert_currency tool to convert 1500 RSD to JPY. Return the conversion result
Results: 1500 RSD = 2087.49 JPY

Query: How are you doing?
I'm just a computer program, so I don't have feelings, but I'm here and ready to help you!
```

As expected! First query uses the tool, while the second does not.

#### That’s it for today, we’ve learned:

- How to wrap python functions to be provided as tools to the Agent.

- How to craft a system prompt that uses the tool definitions in planning the execution.

- How to implement the agent that executes on the plan.

</details>

<details>
<summary>Efficient Tool Use with Chain-of-Abstraction Reasoning</summary>

# Efficient Tool Use with Chain-of-Abstraction Reasoning

**Source URL:** <https://arxiv.org/pdf/2401.17464v3>

## Abstract

To achieve faithful reasoning that aligns with human expectations, large language models (LLMs) need to ground their reasoning to real-world knowledge (e.g., web facts, math and physical rules). Tools help LLMs access this external knowledge, but there remain challenges for fine-tuning LLM agents (e.g., Toolformer) to invoke tools in multi-step reasoning problems, where inter-connected tool calls require holistic and efficient tool usage planning. In this work, we propose a new method for LLMs to better leverage tools in multi-step reasoning. Our method, Chain-of-Abstraction (CoA), trains LLMs to first decode reasoning chains with abstract placeholders, and then call domain tools to reify each reasoning chain by filling in specific knowledge. This planning with abstract chains enables LLMs to learn more general reasoning strategies, which are robust to shifts of domain knowledge (e.g., math results) relevant to different reasoning questions. It also allows LLMs to perform decoding and calling of external tools in parallel, which avoids the inference delay caused by waiting for tool responses. In mathematical reasoning and Wiki QA domains, we show that our method consistently outperforms previous chain-of-thought and tool-augmented baselines on both in-distribution and out-of-distribution test sets, with an average $\sim 6\%$ absolute QA accuracy improvement. LLM agents trained with our method also show more efficient tool use, with inference speed being on average $\sim 1.4 \times$ faster than baseline tool-augmented LLMs.

## 1 Introduction

Recent large language models (LLMs), have made progress at interpreting and executing instructions, but still make errors when recalling and composing world knowledge for their responses, e.g., making unfactual statements, incorrect calculations, etc. Using auxiliary tools (e.g., a search engine to provide credible facts, a calculator for accurate math operations, etc.) at inference time can mitigate some of these errors, motivating tool-augmented language models that integrate external API calls into their output generations.

However, we show that current tool-augmented LLMs, e.g., Toolformer, struggle to reliably and efficiently leverage tools in multi-step reasoning. In particular, tool calls in multi-step reasoning tasks are often interleaved (i.e., the response of an API call is often part of the query of a subsequent call; as shown in Figure 1). Without explicitly modeling these interconnections in reasoning chains, LLMs do not learn effective planning for tool use, which leads to less accurate reasoning with tools. (As verified by our analysis in Section 5). Meanwhile, interleaving text generation with API calls also introduces inefficient inference “waiting times,” where the model must wait for the response from the API call before resuming the decoding process. This inefficiency becomes more significant in multi-step reasoning scenarios, when multiple rounds of API calls are typically required for each reasoning process.

In this work, we propose Chain-of-Abstraction (CoA) reasoning, a robust and efficient method for LLMs to perform multi-step reasoning with tools. As shown in Figure 1, LLMs are fine-tuned with a goal of making reasoning chains with abstract placeholders. The placeholders do not affect LLMs’ reasoning flow, and are subsequently infilled with specific knowledge retrieved from specialized tools, to ground the final answer generations. Planning abstract chain of reasoning encourages LLMs to inter-connect multiple tool calls and adopt more feasible reasoning strategies, which are robust to the variation of domain knowledge involved in each reasoning process, e.g., specific calculation results. Unlike previous methods where LLM decoding and API calls are executed in an interleaved manner, our method leverages tools to infill knowledge once after the whole chain of reasoning is generated. This enables more efficient decoding across multiple examples (e.g., as in a stream) because CoA traces for subsequent examples can be decoded while tool calls are made for the preceding ones, amortizing overall inference time. We develop a simple pipeline to build fine-tuning data for models to learn CoA, where we first prompt LLMs to re-write existing responses to instructions as abstract chains, and then use domain tools to check the validity of re-writing, as shown in Figure 2.

After training LLMs to learn CoA reasoning, we evaluate the finetuned models on two representative multi-step reasoning domains, including mathematical reasoning, and Wikipedia (Wiki) QA that involves reasoning on factual descriptive knowledge. We show that our method boosts LLMs’ performances, with average $\sim 7.5\%$ and $4.5\%$ absolute accuracy improvements on math and Wiki QA, respectively. These improvements are consistent across both in-distribution and (zero-shot) out-of-distribution test sets, and are especially pronounced on questions that require complex chain-of-thought reasoning. (e.g., more than 3 steps of math derivations). Meanwhile, our method also uses tools more efficiently than previous augmentation methods, with average $\sim 1.47\times$ and $1.33\times$ faster inference speeds on math and Wiki QA tasks, respectively. Finally, extensive human evaluation demonstrates that our method guides LLMs to learn more accurate reasoning, which leads to $\sim 8\%$ fewer reasoning errors.

## 2 Related Work

#### Tool-Augmented LLMs

There is growing interest in augmenting LLMs using external tools. Considerable work has tried to adapt LLMs as tool-using reasoners through in-context learning, demonstrating promising performance improvements in various applications, e.g., math problem solving, biomedical question answering and self-critiquing. Nevertheless, guiding LLMs to effectively use tools using in-context demonstrations is challenging, which requires elaborate task-specific prompt engineering and is restricted by the model’s instruction following ability. Noticing the limitations of in-context learning, several works teach LLMs to learn the usage of tools by fine-tuning, which more robustly improves LLMs’ performance. However, all above approaches adopt sequential interactions with tools throughout reasoning, slowing the inference speed as a function of the latency of the tool (or API) and the number of API calls that are made.

Some other prior works focus on using LLMs for multi-step reasoning with other modules. In particular, ReAct and FireAct integrate LLMs with tools into a closed loop of thought, action and observation steps. This verbose reasoning loop slows down the LLM decoding, and still incorporates tools via sequential interactions, resulting in inefficient inference. Another line of work, Program of Thoughts, DECLARATIVE and PAL prompt LLMs to generate program-based reasoning and interact with code executors, which however heavily rely on closed source coding models, i.e., Codex, and are restricted to procedural arithmetic reasoning. Building on these works, CoA proposes a framework to convert natural language reasoning traces into abstract representations, and uses the abstract reasoning traces as fine-tuning data to improve tool-augmented LLMs. CoA also accelerates tool-augmented reasoning, by holistically planning the CoA traces and calling tools only once at inference time.

#### Tool Usage Planning

Several previous works research tool usage planning in LLMs. Specifically, HuggingGPT, Chameleon, OpenAGI and MetaTool focus on planning the high-level sequence of using multiple tools to address multi-domain mixed tasks. Similarly, LATM, ML-BENCH and Gorilla aim at planning program-level integration of multiple APIs for designing scripts of procedural tasks, e.g., a script for training a model described by a GitHub repository. ToolChain* combines the planning of tool usage with tree-search-based reasoning, which is especially useful for procedural tasks. Different from above work, we focus on the planning of general chain-of-thought reasoning with awareness of domain specialized tools.

## 3 Method

Figure: Figure 2: Illustration of gold data re-writing for fine-tuning data construction. Given a pair of domain question (green scroll) and gold answer (yellow scroll), an LLM is prompted to re-write the gold answer as a reasoning chain with abstract variables (purple bubble). Then, domain specialized tools validate the correctness of the re-writing by checking whether the abstract chain can be reified to get the final answer (orange label).

#### Chain-of-Abstraction (CoA) Reasoning

Our method decouples the general reasoning of LLMs from domain-specific knowledge obtained from external tools. Figure 1 shows an overview of our method. In particular, we first fine-tune LLMs to generate reasoning chains with abstract placeholders, e.g., $y1$, $y2$ and $y3$. (We also test placeholders in single-character format, e.g., $x$, $y$ and $z$, but these led to sub-optimal results.) In the second stage, we reify each reasoning chain by replacing placeholders with domain-specific knowledge obtained from external tools, e.g., calculation results from a calculator, relevant articles retrieved from web search engine, etc. Finally, the question is answered based on the reified reasoning chain.

Note that since the LLMs are trained to generate abstract chain of reasoning instead of regular chain-of-thought (CoT) reasoning with explicit values, this enables LLMs to focus on learning general and holistic reasoning strategies without needing to generate instance-specific knowledge for the model’s parameters. Moreover, decoupling general reasoning and domain-specific knowledge enables LLM decoding to proceed and switch between different samples in parallel with API calling (via a pipeline), i.e., LLM can start generating the next abstract chain while the tool fills the current chain, which speeds up the overall inference process.

#### Fine-tuning Data Construction

To construct chain-of-abstraction (CoA) data for fine-tuning LLMs, we collect question answering (QA) samples from existing open-source QA datasets, and prompt LLaMa-70B to re-write the answer of each sampled question, as shown in Figure 2. Specifically, we prompt LLaMa-70B to label the spans in gold answers that correspond to knowledge operations (e.g., math derivations, statements based on Wikipedia references) and then to re-write the sentences with labeled spans as fillable CoA traces, where the operation results are replaced with abstract placeholders. For example, the two derivations in the example in Figure 2 are re-written as “[$20+35=y1$]" and “[$90-y1=y2$]", respectively.

Note that an intermediate knowledge operation result may appear multiple times in an answer, e.g., in Figure 2, the first equation’s result $55$ is used in the second equation. We prompt LLaMa-70B to replace all occurrences of the same intermediate result with the same placeholder, thereby explicitly connecting the multiple reasoning steps. To ensure that the re-written data is accurate, we use domain-specialized tools to verify the correctness of each CoA reasoning trace. (Detailed implementations of reasoning chain verification are described in Section 4.1 and 4.2.) Specifically, we use the tools to execute the labeled operations in each CoA, and only keep questions whose CoA can be infilled with valid results by the tools.

## 4 Experimental Settings

We conduct our experiments on two representative domains: mathematical reasoning and Wikipedia (Wiki) QA, which involves commonsense and logical reasoning on factual descriptive knowledge.

### 4.1 Mathematical Reasoning

Given a math question, the QA system needs to generate a natural language solution to the problem with step-by-step arithmetic derivations (as demonstrated in the left column of Figure 1). We assume that the derivations involved in the solution are the specialized knowledge operations required in this domain, which are labeled in square brackets with derivation results being replaced by abstract placeholders, e.g., “[$20+35=y1$]".

#### Datasets

We construct most of our fine-tuning CoA data by re-writing the GSM8K training set, which contains 7473 linguistically diverse grade school math problems. As GSM8K dataset focuses on multi-step reasoning, it lacks coverage of single-step arithmetic problems, so we also re-write an additional set of 691 single-step math problems from the ASDiv dataset. Across these re-written datasets, we find that $\sim 76.6\%$ of the CoA reasoning traces generated by LLaMa-70B are verified by our equation solver (described below). Table 1 shows the reasoning step distribution (i.e., number of derivations) of our constructed fine-tuning data.

**Table 1: Reasoning step distribution of correctly re-written reasoning chains in math domain.**

| Source | Reasoning Step |       |       |       |       |      | All  |
| ------ | -------------- | ----- | ----- | ----- | ----- | ---- | ---- |
| 1      | 2              | 3     | 4     | 5     | >5    |      |      |
| GSM8K  | 8              | 1540  | 1648  | 1164  | 666   | 553  | 5579 |
| ASDiv  | 677            | 0     | 0     | 0     | 0     | 0    | 677  |

For an in-distribution evaluation, we test models on GSM8K and ASDiv, containing 1319 and 2305 testing problems. To further test the models’ generalization ability, we also conduct zero-shot evaluation on other representative math datasets, including SVAMP and MAWPS, which contain 1000 and 2065 testing samples, respectively. (For the MAWPS benchmark, we test on the 395, 508, 562 and 600 math problems from AddSub, SingleEq, SingleOp and MultiArith portions, respectively.)

#### Domain Tool

We use an equation solver to perform the arithmetic derivations required in the math domain. Our equation solver first extracts the derivations labeled in the CoA reasoning, e.g., “[$20+35=y1$]" and “[$90-y1=y2$]", and combines all derivations into a system of equations. Then the system of equations is solved by the SymPy toolkit, [https://www.sympy.org/en/index.html](https://www.sympy.org/en/index.html), to get the true value of each variable (i.e., the value of the abstract placeholder). Finally, our equation solver returns the reified chain of reasoning by replacing all the variables with their solved true values (including the final answer).

**Table 2: Example of CoA fine-tuning data construction in Wiki QA domain.**

| Question    | The director of the romantic comedy “Big Stone Gap” is based in |
| ----------- | --------------------------------------------------------------- |
|             | what New York city?                                             |
| Answer      | Greenwich Village                                               |
| Wikipedia   | Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic |
| References  | comedy film directed by Adriana Trigiani.                       |
|             | Adriana Trigiani > Adriana Trigiani is an Italian American film |
|             | director based in Greenwich Village.                            |
| CoA Trace   | Find the [director of romantic comedy “Big Stone Gap” -Wiki-> y1]. |
|             | The name of this film’s director is [y1 -NER(person)-> y2].       |
|             | Then determine [y2 in what New York city -Wiki-> y3].            |

### 4.2 Wikipedia QA

Given a question based on Wikipedia knowledge, the model needs to first identify Wikipedia articles as references related to the question, and then reason on key knowledge in the reference articles to answer the question (as shown in the right column of Figure 1). We assume that the specialized knowledge operation in this domain is the retrieval of relevant Wikipedia articles and important named-entities, which are re-written as Wikipedia searching (WikiSearch) and named-entity recognition (NER) queries. (We use NER to extract entities from the article that bridge the former WikiSearch results to the latter WikiSearch queries.) Table 2 shows an example of a re-written CoA trace for Wiki QA.

#### Datasets

We use the HotpotQA dataset to construct our fine-tuning CoA data in the Wiki QA domain. HotpotQA contains 113K multi-hop QA examples, each labeled with two Wikipedia articles that provide supporting knowledge. Among the 90447 training QA pairs, we identify 72991 as Bridge QA pairs, where an intermediate entity must be identified to link the answer to the question, as shown in Table 2. The remaining 17456 are Comparison QA pairs, where the attributes of two entities are compared, e.g., “Are Randal Kleiser and Kyle Schickner of the same nationality?”. We prompt LLaMa-70B to re-write these training QAs into CoAs with WikiSearch and NER queries, and verify each CoA with our domain tools (described below), by checking whether all the articles returned by the WikiSearch queries match one of the titles in the gold articles. Finally, 8956 Bridge QAs and 5405 Comparison QAs are used as fine-tuning data, whose re-written CoAs pass the verification. (Compared to mathematical reasoning, generating CoA data for Wiki QA requires more complex tool use that combines WikiSearch and NER models, leading to a lower re-writing success rate ($\sim 15.9\%$).) For Wiki QA, we note that besides training a LLM to produce CoA data using WikiSearch, we also fine-tune a second LLM to learn to generate the final gold answer based on a correctly reified CoA reasoning trace.

We evaluate models on the HotpotQA development set, which contains 5918 Bridge QA pairs and 1487 Comparison QA pairs. Similar to the mathematical reasoning domain, we also conduct zero-shot evaluation on other open-domain QA datasets: WebQuestions (WQ), NaturalQuestions (NQ) and TriviaQA, which contain 2032, 3610 and 17944 test questions, respectively.

#### Domain Tools

The specialized tools required for Wiki QA include a Wikipedia search engine to retrieve reference articles, and a NER toolkit to extract entities that bridge multi-step searching queries. We follow Toolformer and implement a Wikipedia search engine as a BM25 retriever that indexes the Wikipedia dump from the KILT benchmark. We use the BM25 retriever to search the top-10 articles relevant to the input query, and then re-rank the articles based on their Sentence-BERT embedding cosine similarity with the question. After re-ranking, the top-1 article is selected to be the final search result.

We use SpaCy [https://spacy.io/models/en](https://spacy.io/models/en) (en_core_web_sm) as the NER toolkit to extract named entities. To simplify NER, we aggregate the numerous SpaCy NER types into 6 general classes, as shown in Table 3. If multiple named entities are recognized, we input each recognized entity to the subsequent WikiSearch query, and select the entity whose subsequent search result has the highest Sentence-BERT embedding cosine similarity with the question.

**Table 3: Aggregation of SpaCy NER types.**

| General Class | SpaCy NER Types included in each General Class |
| ------------- | ---------------------------------------------- |
| person        | PERSON                                         |
| group         | NORP, ORG, LANGUAGE                            |
| location      | GPE, FAC, LOC                                  |
| culture       | EVENT, WORK_OF_ART, LAW, PRODUCT               |
| date          | DATE, TIME                                     |
| numeral       | CARDINAL, PERCENT, MONEY, QUANTITY, ORDINAL    |

**Table 4: Evaluation results on LLaMa-2 and LLaMa-2-Chat for mathematical reasoning. “All” denotes the averaged results on four MAWPS portions. Exact match rate to the final gold answer (i.e., accuracy) is reported. For each base model, the best and second-best results are bolded and underlined, respectively. The best results labeled with $^\ast$ are significantly better than their corresponding second-best results, with the significant test p-value $<0.05$.**

| Model        | Method         | Tool | GSM8K          | ASDiv          | SVAMP          | MAWPS AddSub   | MAWPS SingleEQ | MAWPS SingleOp | MAWPS MultiArith | MAWPS All      |
| ------------ | -------------- | ---- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | ---------------- | -------------- |
| LLaMa-2-7B   | CoT-FSP        | ✗    | 16.38          | 47.85          | 38.40          | 52.41          | 63.39          | 82.03          | 43.33            | 60.53          |
|              | CoT-FT         |      | 35.33          | 57.18          | 48.20          | 66.08          | 74.41          | 85.23          | 65.00            | 73.03          |
|              | Toolformer     | ✓    | 17.59          | 48.55          | 37.10          | 47.34          | 58.46          | 79.54          | 50.67            | 59.81          |
|              | CoA            |      | **37.83$^\ast$** | **57.61**      | **51.70$^\ast$** | **72.15$^\ast$** | **82.48$^\ast$** | **86.48$^\ast$** | **73.17$^\ast$** | **78.89$^\ast$** |
| LLaMa-2-Chat-7B | CoT-FSP        | ✗    | 24.03          | 54.14          | 51.30          | 71.90          | 72.44          | 85.41          | 74.00            | 76.32          |
|              | CoT-FT         |      | 35.41          | 59.00          | 46.90          | 58.23          | 72.24          | 85.41          | 73.00            | 73.37          |
|              | CoA (no Tool)  |      | 35.03          | 58.79          | 51.50          | 68.10          | 74.21          | 86.48          | 77.67            | 77.38          |
|              | Toolformer     | ✓    | 23.65          | 50.85          | 48.80          | 61.01          | 69.09          | 81.85          | 68.50            | 70.85          |
|              | Toolformer - Math |      | 36.01          | 59.18          | 47.60          | 58.99          | 72.44          | 85.94          | 75.50            | 74.43          |
|              | CoA            |      | **38.29$^\ast$** | **59.57**      | **54.20$^\ast$** | **72.41**      | **81.89$^\ast$** | **88.26$^\ast$** | **83.00$^\ast$** | **82.13$^\ast$** |
| LLaMa-2-Chat-70B | CoT-FSP        | ✗    | 56.18          | 65.94          | 70.60          | 86.08          | 89.17          | 92.88          | 84.50            | 88.23          |
|              | CoT-FT         |      | 60.50          | 70.24          | 70.40          | 81.52          | 87.60          | 92.35          | 89.17            | 88.18          |
|              | Toolformer     | ✓    | 52.54          | 69.07          | 73.60          | 86.84          | 89.76          | 91.46          | 81.50            | 87.26          |
|              | Toolformer - Math |      | 61.03          | 70.59          | 73.20          | 85.57          | 91.34          | 91.99          | 92.00            | 90.60          |
|              | CoA            |      | **62.32$^\ast$** | **71.89$^\ast$** | 73.40          | **86.33**      | **94.49$^\ast$** | **93.06**      | **92.33**        | **91.91$^\ast$** |

### 4.3 Baselines

We apply our CoA reasoning method to both 7B and 70B LLaMa models, and test various model versions including the first version of LLaMa and the more advanced LLaMa-2 and LLaMa-2-Chat. We compare our method to several baselines, including: a) few-shot prompting using 8 randomly sampled QA exemplars from the original (i.e., not re-written) chain-of-thought data (CoT-FSP), b) fine-tuning with original chain-of-thought data (CoT-FT) (Note that in Wiki QA domain, the HotpotQA data used for prompting or fine-tuning baselines is pre-processed to contain both gold Wikipedia articles (serving as chain-of-thought explanations) and the final answer.), and c) Toolformer which fine-tunes LLMs on CCNet texts augmented with API calls. For evaluation on Wiki QA, we also compared our method with FireAct, which fine-tunes LLMs on HotpotQA ReAct trajectories distilled from GPT-4.

## 5 Results and Analysis

### 5.1 Mathematical Reasoning

Table 4 shows the evaluation results for the LLaMa-2 and LLaMa-2-Chat models. (We include similar evaluation results for the original LLaMa model (7B) in Appendix B.) On the GSM8K and ASDiv datasets, our CoA method outperforms the few-shot baseline CoT-FSP and the regular fine-tuning baseline CoT-FT, demonstrating that CoA fine-tuning with tool augmentation is more effective in adapting LLMs to multi-step reasoning tasks. Similarly, when evaluated on out-of-distribution datasets, SVAMP and MAWPS, CoA also consistently outperforms the baselines. Interestingly, for these out-of-distribution datasets, CoT-FT lags further behind CoA, particularly for 7B models, showing that CoA reasoning yields more distributionally robust reasoning performance.

Our CoA method also surpasses the tool-augmented baseline Toolformer, which implies that planning the abstract variables in CoA can improve the accuracy of reasoning with tools. However, as Toolformer is not originally trained with in-domain fine-tuning data, (Toolformer is fine-tuned on CCNet data, which may not contain rich mathematical reasoning samples.) we also fine-tune a new version of Toolformer with the chain-of-thought data from GSM8K and ASDiv, denoted as Toolformer - Math in Table 4. We also observe that CoA performs better than Toolformer - Math, confirming that the introduction of abstract variables enables more robust tool use compared to direct integration of API calls within chain-of-thought reasoning.

#### Ablation Study

We verify that the robust generalization performance of our CoA method does not merely benefit from using additional tools, by fine-tuning another LLM to solve the equation (from the same model backbone), rather than calling the equation solver, denoted as CoA (no Tool) in Table 4. We find that CoA (no Tool) performs consistently worse than CoA across all datasets, confirming that using specialized tools enables LLM agents to conduct more precise operations, rather than directly solving the same operations. However, CoA (no Tool) still outperforms all baseline methods on zero-shot generalization to SVAMP and MAWPS datasets, implying that learning abstract reasoning chains also contributes to better robustness of CoA, perhaps due to better planning of multiple reasoning steps indexed by abstract variables.

#### Reasoning Steps

Our findings suggest that the benefits of chain-of-abstraction reasoning are most pronounced when problems require long reasoning chains to be solved. Figure 3 shows the stratified performance of three models on GSM8K QA, relative to the number of reasoning steps in the predicted and gold reasoning chains. Compared to the few-shot CoT-FSP, CoA produces reasoning chains that more often match the length of the gold reasoning chains, as reflected by the heat-map statistics (left column) being more aggregated around the diagonal (comparable to CoT-FT). At the same time, we observe that models achieve better QA accuracy when the number of reasoning steps in their generated answers are aligned with the gold references (i.e., the diagonal of heat-maps in right column). Above results show that fine-tuned models are better at learning to produce reasoning chains that match the true reasoning chain for the problem.

Figure: Figure 3: GSM8K evaluation results on LLaMa-2-Chat-7B w.r.t. the number of reasoning steps in the predicted and gold reasoning chain. (Left) The number of test examples that belong to each stratum. (Right) The corresponding model accuracy (%) for those examples. Non-diagonal cells with fewer than 15 examples are ignored.

Interestingly, we find that CoA, compared to CoT-FT, achieves higher performance especially on questions that require more reasoning steps. In the right column of Figure 3, CoA’s improvement over CoT-FT is more pronounced on questions with more than $3$ steps in the gold reasoning chain (highlighted with red squares). This indicates that the model trained with CoA has more robust long chain-of-thought reasoning capability, which is learned from planning with abstractions.

#### Human Evaluation

To more comprehensively verify that CoA improves both knowledge operation (i.e., arithmetic by using tools) and reasoning accuracy, we conduct a human evaluation on different model answers to 200 randomly sampled GSM8K test questions. Specifically, given a GSM8K question and a model’s answer to the question, we ask human workers to judge whether the answer contains any arithmetic errors (e.g., wrong calculations, invalid equations) or reasoning errors unrelated to math derivations (e.g., misunderstanding of the question, improper strategy for solving the question), and report how often the model makes these two kinds of errors. In Table 5, we find that CoA effectively reduces arithmetic errors to zero, due to the use of equation solver to perform accurate calculations. More importantly, our method also makes fewer reasoning errors compared to the baselines, verifying that CoA fine-tuning guides the model to learn more accurate reasoning through the holistic planning of abstract reasoning chains. By contrast, ordinary fine-tuning (i.e., CoT-FT) produces a more limited reasoning improvement compared to the few-shot CoT-FSP, while also failing to suppress arithmetic errors.

**Table 5: Human evaluation results of arithmetic and reasoning error rates on 200 GSM8K test samples. Models developed based on LLaMa-2-Chat-7B are presented.**

| Method  | Error Rate Arithmetic | Reasoning |
| ------- | --------------------- | --------- |
| CoT-FSP | 17.3                  | 70.3      |
| CoT-FT  | 25.2                  | 67.8      |
| CoA     | 0.0                   | 60.4      |

Figure: Figure 4: Wall-clock inference time on GSM8K (seeded with LLaMa-2-Chat-7B). Average time of answering a question is measured (in seconds) w.r.t. the number of gold reasoning steps required for the question.

#### Inference Efficiency

Importantly, we find that the performance benefits of CoA reasoning do not come with increased computational costs. In Figure 4, we show the average time (seconds) that CoA and baseline agents (seeded with LLaMa-2-Chat-7B) needs to answer a question w.r.t. required gold reasoning steps. Compared to the CoT baselines, CoA requires less time than the few-shot baseline CoT-FSP, whose generation needs to be conditioned on additional examples. However, CoA is slightly less inference-efficient compared to CoT-FT, likely due to the decoding of additional tokens (e.g., “[" and “]”) for the abstract statements.

Compared to Toolformer, CoA has a lower and flatter inference time curve, indicating better scaling as the number of reasoning steps increases. This difference arises because CoA decouples the generation of (abstract) reasoning chains from the retrieval of knowledge (i.e., tool use), allowing full reasoning chains to be decoded before any tool is called. This procedure amortizes inference costs in two ways. First, tool calls are made after the CoA trace has been decoded, enabling parallel tool calls for the same trace (e.g., using an equation solver once rather than multiple calls to a calculator), and avoiding the time delay caused by waiting for external API responses. Consequently, the model fine-tuned with CoA is more efficient at multi-step reasoning, especially when the number of reasoning steps (i.e., tool calls) increases. Second, across multiple examples, the model can generate the CoA trace of the next example while tool calls are made for the preceding one, parallelizing CoA decoding and tools calls across examples.

#### Self-Consistency Decoding

Besides of greedy decoding, we also test more advanced inference strategy, i.e., self-consistency decoding, on our CoA reasoning method. We test all methods on the GSM8K dataset seeded with LLaMa-2-Chat-7B. Each method samples 16 reasoning chains and uses majority voting to aggregate the 16 answers derived by the reasoning chains, to get the final answer. For the hyperparameters of sampling, we set the temperature, top-k and top-p as 1.0, 40 and 0.5, respectively. Table 6 shows our evaluation results. We find that our CoA method consistently outperforms all baseline methods when shifting from greedy decoding to self-consistency decoding. This shows that our method also has better potential to be generalized to different LLM decoding schemes.

**Table 6: Evaluation results on GSM8K with self-consistency decoding (seeded with LLaMa-2-Chat-7B). Each model uses majority voting to aggregate the answers of 16 sampled reasoning chains**

| Method            | Accuracy |
| ----------------- | -------- |
| CoT-FSP           | 27.90    |
| CoT-FT            | 39.12    |
| Toolformer        | 24.56    |
| Toolformer - Math | 35.25    |
| CoA               | 40.79    |

**Table 7: Wiki QA evaluation results on LLaMa-2-Chat-based models. “Both” denotes the overall evaluation results on both bridge and comparison portions of HotpotQA. “Time” denotes the average seconds that each agent needs to answer a question in HotpotQA. Exact match rate to the final gold answer (i.e., accuracy) is reported. For each base model, the best and second-best results are bolded and underlined, respectively. The best results labeled with $^\ast$ are significantly better than their corresponding second-best results, with the significant test p-value $<0.05$.**

| Model        | Method         | Tool | HotpotQA Bridge | HotpotQA Comparison | HotpotQA Both | HotpotQA Time | WQ             | NQ             | TriviaQA       |
| ------------ | -------------- | ---- | --------------- | ------------------- | ------------- | ------------- | -------------- | -------------- | -------------- |
| LLaMa-2-Chat-7B | CoT-FSP        | ✗    | 11.69           | 45.46               | 18.47         | 2.074         | 34.65          | 30.91          | 53.48          |
|              | CoT-FT         |      | 14.24           | 56.69               | 22.77         | 1.937         | 33.51          | 25.40          | 51.05          |
|              | Toolformer     | ✓    | 12.99           | 44.59               | 20.00         | 2.350         | 36.22          | 30.22          | 54.15          |
|              | Toolformer - Wiki |      | 15.68           | 56.42               | 23.86         | 2.301         | 36.61          | 32.96          | 55.08          |
|              | FireAct        |      | 19.18           | 54.14               | 26.20         | 2.706         | 36.02          | 35.87          | 52.96          |
|              | CoA            |      | **21.00$^\ast$** | **56.96**           | **28.22$^\ast$** | **1.896**     | **35.97**      | **38.67$^\ast$** | **57.90$^\ast$** |
| LLaMa-2-Chat-70B | CoT-FSP        | ✗    | 21.39           | 56.62               | 28.47         | 6.668         | 34.89          | 37.42          | 63.61          |
|              | CoT-FT         |      | 23.84           | 63.95               | 31.90         | 6.401         | 34.15          | 39.75          | 62.28          |
|              | Toolformer     | ✓    | 22.24           | 56.09               | 29.04         | 6.888         | 37.16          | 40.42          | 64.31          |
|              | Toolformer - Wiki |      | 26.38           | 63.82               | 33.90         | 6.855         | 37.70          | 41.25          | 66.64          |
|              | CoA            |      | **27.61$^\ast$** | **64.09**           | **34.94$^\ast$** | **6.369**     | **36.37**      | **43.57$^\ast$** | **69.08$^\ast$** |

### 5.2 Wiki QA

Table 7 shows our Wiki QA results using LLaMa-2-Chat models. (We include similar evaluation results on LLaMa-2-7B in Appendix B.) Similar to mathematical reasoning, we fine-tune a new version of Toolformer with in-domain chain-of-thought data from HotpotQA, denoted as Toolformer - Wiki. On HotpotQA, CoA achieves higher exact match rates with the gold reference compared to the few-shot or fine-tuning baselines. In particular, CoA outperforms all baselines on the more challenging bridge-type QAs, where two steps of reasoning over Wikipedia knowledge are consecutively entangled, i.e., cannot be performed independently in parallel as in comparison-type QAs. Compared to FireAct fine-tuning, CoA also achieves better performance on both bridge and comparison QAs, without requiring data distilled from closed source GPT-4.

As with mathematical reasoning, CoA agents also perform more efficient inference than Toolformer and FireAct agents when answering HotpotQA questions. We also find that CoA is more efficient (Time column) than both CoT-FSP and CoT-FT, as CoA does not require few-shot examples as additional inputs and does not need to generate long Wiki articles, which are instead provided by the search engine. Finally, CoA improves over the baseline methods in zero-shot generalization experiments on other Wiki QA datasets, outperforming all baselines on NaturalQuestions and TriviaQA, and matching the best baselines on WebQuestions.

## 6 Conclusion

In this work, we propose to decouple the general reasoning of LLM agents from specialized knowledge obtained via external tools. Our method, Chain-of-Abstraction (CoA), encourages LLMs to learn the planning of abstract multi-step reasoning, which are more robust to out-of-distribution knowledge shifts. CoA also achieves a more efficient pipeline for tool usage that significantly improves the speed of tool-augmented multi-step reasoning. The simple, yet effective, implementations of our method on two diverse tasks (i.e., math reasoning and open-domain QA) demonstrate its potential for being adapted to new reasoning scenarios.

## Limitations

We acknowledge a few limitations in our work. First, datasets used for testing our method cannot have exhaustive coverage of all real-world reasoning scenarios. We instead consider two representative reasoning domains, i.e., mathematical reasoning and general open-domain (Wikipedia) QA, and use English as a primary language in our testing. Furthermore, our method is tested on the setting of fine-tuning the full LLMs, which requires considerable computational resources, while more efficient model training schemes, e.g., LoRA, can be applied in future work.

## Acknowledgements

We thank Beatriz Borges, Gail Weiss, Syrielle Montariol, Li Mi and Zeming Chen for reading and providing comments on drafts of this paper. Antoine Bosselut gratefully acknowledges the support of the Swiss National Science Foundation (No. 215390), Innosuisse (PFFS-21-29), the EPFL Science Seed Fund, the EPFL Center for Imaging, Sony Group Corporation, and the Allen Institute for AI.

## Appendix A Implementation Details

#### Evaluation Details

For mathematical reasoning evaluation, we extract the last number appeared in each model’s answer, and check whether the number exactly match the gold reference. The accuracy is reported as the rate of such exact match across all QAs in a test set. For Wiki QA evaluation, similar to mathematical reasoning, we extract the final answer of each model and calculate its exact match rate to the gold reference. Specifically, the final answer is supposed to be the words after “Action: finish[" for FireAct baseline, and words after “The answer is ” for other models. Our 8-shot in-domain examples used for the CoT-FSP baseline are shown in Table 14 and 15, which enables the model to provide answer with our required format for evaluation, i.e., stating its final answer after “The answer is ”. Our human evaluation on GSM8K is conducted by 5 internal domain experts from our research group. For each math question, we provide the experts with the gold answer as reference, and ask them to evaluate each model answer in anonymous manner, i.e., experts do not know which model each answer comes from. Two yes-or-no questions are asked for evaluating each model answer, including: a) whether the answer has any arithmetic error, and b) whether the answer has any reasoning error, and binary choices from the experts are collected to calculate the error rates of each model’s generation. We present our detailed instructions for human evaluation in Figure 5. Our data collection protocol is approved by our organization in terms of ethics.

#### Model Training

We fine-tune our models with batch size $8$ and learning rate $2e^{-5}$ and $1e^{-5}$ for 7B and 70B model sizes, respectively, using cosine learning rate scheduler with warm-up step $10$. We use AdamW optimizer for all our fine-tuning experiments, with $\beta_{1}$, $\beta_{2}$ and $\epsilon$ set to $0.9$, $0.95$ and $1e^{-8}$, respectively. Training weight decay is set to $0.1$. For mathematical reasoning, we use a total of $400$ training steps, and get the best model checkpoints (with highest validation scores) at step $240$ and $200$ for 7B and 70B model sizes. For Wiki QA domain, we adjust the total training steps to $500$, and get the best checkpoints at step $450$ and $300$ for 7B and 70B models. Therefore, only $\sim$2K and $\sim$3K QAs are required in practice for fine-tuning our models in math and Wiki QA domains. The training of our 7B and 70B models is based on 8 and 64 NVIDIA A100-SXM4 (80GB) GPUs, with training time about 2 and 5 hours per model, respectively.

## Appendix B Full Experimental Results

Table 8 and 9 show the full results of our experiments on math and Wiki QA domains. Our method of CoA achieves consistent improvements over baselines across various LLaMa model versions (LLaMa, LLaMa-2 and LLaMa-2-Chat), model sizes (7B and 70B), and domain benchmarks. This shows great potential of our method being generalized to new model backbones and reasoning tasks. We also present results on GSM8K subsets according to varying numbers of gold reasoning steps in Table 10, where we confirm that CoA has more robust long chain-of-thought reasoning accuracy.

#### Fine-Tuning Data Balance

In the mathematical reasoning domain, we also validate the importance of using fine-tuning data that is balanced across different reasoning steps. Specifically, we conduct an ablation study on CoT-FT and CoA seeded with LLaMa-2-Chat-7B model, by removing the single-step QA samples of ASDiv from the fine-tuning data (no ASDiv). We find that CoT-FT (no ASDiv) and CoA (no ASDiv) turn out to be biased towards multi-step reasoning, where they achieve better performance on GSM8K and MultiArith that contain mainly multi-step QAs, but suffer from severe performance degradation on other datasets that contain many single-step math problems. This demonstrates that maintaining a good balance of single-step and multi-step reasoning data is important for adapting LLMs to be robust reasoners.

#### More Prompting Baselines

We also compare our CoA reasoning method to more prompting-based methods PAL and DECLARATIVE, which use few-shot coding demonstrations to prompt math solutions as Python or declarative programs. Table 11 shows our comparison results on the GSM8K dataset, where all methods are seeded with LLaMa-2-Chat-7B. Without seeding with dedicated coding models (e.g., code-davinci-002), PAL and DECLARATIVE get far lower accuracy on GSM8K, which significantly under-perform our CoA method, and even ordinary CoT-FSP.

In contrast, our CoA method relies less on artificial demonstrations and distributional closeness of the seed LLM to target tasks, as CoA fine-tunes the LLM agent on pre-defined abstract reasoning chains, acquired from simple rewriting of natural language reasoning traces. Consequently, CoA is flexible in various generation formats, e.g., code and plain text, and generalizes well from mathematical reasoning to open-domain QA, which is a very different type of reasoning task. This indicates our method’s generalizability to novel reasoning schemes required by a new domain.

**Table 10: Stratified LLaMa-2-Chat-7B evaluation results on GSM8K with different gold reasoning steps. The last row reports absolute accuracy improvement of our CoA method compared to CoT-FT baseline.**

| Method  | Gold Reasoning Step $\leq 2$ | 3    | 4    | 5    | >5   |
| ------- | ---------------------------- | ---- | ---- | ---- | ---- |
| CoT-FSP | 42.9                         | 26.3 | 18.0 | 10.9 | 3.6  |
| CoT-FT  | 55.5                         | 42.6 | 25.8 | 19.0 | 10.8 |
| CoA     | 55.8                         | 44.4 | 32.5 | 25.3 | 15.1 |
|         | +0.3                         | +1.8 | +6.7 | +6.3 | +4.3 |

**Table 11: Comparison of CoA to prompting-based methods on GSM8K, seeded with LLaMa-2-Chat-7B.**

| Method      | Accuracy |
| ----------- | -------- |
| CoT-FSP     | 24.03    |
| PAL         | 20.55    |
| DECLARATIVE | 9.86     |
| CoA         | 38.29    |

**Table 12: Prompting examples for fine-tuning data construction in mathematical reasoning domain. Given a question (Q) and a gold answer (A), LLaMa-70B is prompted to generate the re-writing of answer as abstract reasoning chain (C). Based on that, our method trains a LLM to generate the abstract chain based on the question, and the final answer is derived by reify the chain of reasoning with the domain tool (i.e., equation solver).**

| Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees will the grove workers plant today? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21-15=6. The answer is 6.                                          |
| C: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been [21 - 15 = y1]. The answer is y1.                                    |
| Q: The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers?                 |
| A: The clay pot costs $20 + $9 = $29. The bag of soil costs $9 - $2 = $7. The cost to plant the flowers is $9 + $29 + $7 = $45. The answer is 45.                                 |
| C: The clay pot costs [20 + 9 = y1]. The bag of soil costs [9 - 2 = y2]. The cost to plant the flowers is [9 + y1 + y2 = y3]. The answer is y3.                                     |
| Q: From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy the video game console? |
| A: Sam makes $460 / 23 hrs = $20/hr. From September to February, Sam made 8hrs x $20/hr = $160. From March to February, Sam made a total of $460 + $160 = $620. After fixing his car, he was left with $620 - $340 = $280. Sam needs another $600 - $280 = $320. Sam needs to work another $320 / $20/hr = 16 hours. The answer is 16. |
| C: Sam makes [460 / 23 = y1] dollars per hour. From September to February, Sam made [8 * y1 = y2] dollars. From March to February, Sam made a total of [460 + y2 = y3] dollars. After fixing his car, he was left with [y3 - 340 = y4]. Sam needs another [600 - y4 = y5] dollars. Sam needs to work another [y5 / y1 = y6] hours. The answer is y6. |
| Q: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room? |
| A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.                      |
| C: There were originally 9 computers. For each of 4 days, 5 more computers were added. So [5 * 4 = y1] computers were added. [9 + y1 = y2]. The answer is y2.                 |
| Q: Of the 90 people on William’s bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What’s the number of Dutch Americans who sat at the windows? |
| A: On the bus, the number of Dutch people was 3/5 of the total number, a total of 3/5 x 90 = 54 people. Out of the 54 people who were Dutch, 1/2 were Dutch Americans, a total of 1/2 x 54 = 27 people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number is 1/3 x 27 = 9. The answer is 9. |
| C: On the bus, the number of Dutch people was 3/5 of the total number, a total of [3/5 * 90 = y1] people. Out of the Dutch people, 1/2 were Dutch Americans, a total of [1/2 * y1 = y2] people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number is [1/3 * y2 = y3]. The answer is y3. |

## Appendix C Fine-Tuning Data Re-writing Details

Table 12 and 13 show the prompting examples for fine-tuning data construction of our method. We prompt LLaMa-70B to re-write existing math and Wiki QAs as abstract reasoning chains, which gets rid of data distillation from close-sourced LLMs, yet obtains data resources that enable more effective learning of multi-step reasoning.

**Table 13: Prompting examples for fine-tuning data construction in Wiki QA domain. Given a question (Q), a gold answer (A) and its supporting Wikipedia articles (W), LLaMa-70B is prompted to generate an abstract reasoning chain (C) with Wikipedia searching and NER queries. Based on that, our method first trains a LLM to generate the abstract chain of queries based on the question, and then execute the queries by domain tools (i.e., Wikipedia search engine and NER toolkit). Finally, a second LLM is trained to generate the final answer based on the Wikipedia searching results (excluding intermediate NER results) in the reified chain of reasoning.**

| Q: Fritz von Brodowski was killed during what global war that lasted from 1939 to 1945? |
| --------------------------------------------------------------------------------------- |
| A: The answer is World War II.                                                          |
| W: Fritz von Brodowski > Friedrich Wilhelm Konrad von Brodowski was controversially killed while in French custody during World War II. |
| C: Find the [war in which Fritz von Brodowski was killed -Wiki-> y1].                  |
| Q: Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?     |
| A: The answer is Jonathan Stark.                                                        |
| W: Henri Leconte > He won the French Open men’s doubles title in 1984. Jonathan Stark (tennis) > During his career he won two Grand Slam doubles titles. |
| C: First identify the [number of Grand Slam titles Henri Leconte won -Wiki-> y1]. Then find out the [number of Grand Slam titles Jonathan Stark won -Wiki-> y2]. |
| Q: The director of the romantic comedy “Big Stone Gap” is based in what New York city? |
| A: The answer is Greenwich Village.                                                     |
| W: Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic comedy film directed by Adriana Trigiani. Adriana Trigiani > Adriana Trigiani is an Italian American film director based in Greenwich Village. |
| C: First search the [director of romantic comedy “Big Stone Gap” -Wiki-> y1]. The name of this film’s director is [y1 -NER(person)-> y2]. Then determine [y2 in what New York city -Wiki-> y3]. |
| Q: Are Randal Kleiser and Kyle Schickner of the same nationality?                       |
| A: The answer is yes.                                                                   |
| W: Randal Kleiser > John Randal Kleiser (born July 20, 1946) is an American film director and producer. Kyle Schickner > Kyle Schickner is an American film producer, writer, director, actor. |
| C: First find out the [nationality of Randal Kleiser -Wiki-> y1]. Then figure out the [nationality of Kyle Schickner -Wiki-> y2]. |
| Q: Extras was created, written, and directed by Ricky Dene Gervais, an English comedian, actor, writer, producer, director, singer, and musician, born on which date? |
| A: The answer is 25 June 1961.                                                          |
| W: Ricky Gervais > Ricky Dene Gervais (born 25 June 1961) is an English comedian, actor, writer, producer, director, singer, and musician. |
| C: Search [when Ricky Dene Gervais was born -Wiki-> y1].                               |
| Q: Sameera Perera is a cricketer from what island country located southeast of the Republic of India and northeast of the Maldives? |
| A: The answer is Sri Lanka.                                                             |
| W: Sameera Perera > Sameera Perera (born 20 August 1988) is a Sri Lankan cricketer.     |
| C: Identify the [country that cricketer Sameera Perera is from -Wiki-> y1].            |
| Q: What screenwriter with credits for “Evolution” co-wrote a film starring Nicolas Cage and Téa Leoni? |
| A: The answer is David Weissman.                                                        |
| W: The Family Man > The Family Man is a 2000 American romantic comedy-drama film starring Nicolas Cage and Téa Leoni. David Weissman > His film credits include “The Family Man” (2000), “Evolution” (2001), and “When in Rome” (2010). |
| C: First figure out the [film of Nicolas Cage and Téa Leoni -Wiki-> y1]. The name of this film is [y1 -NER(culture)-> y2]. Then find out [who wrote y2 with credits for “Evolution” -Wiki-> y3]. |
| Q: Ralph Hefferline was a psychology professor at a university that is located in what city? |
| A: The answer is New York City.                                                         |
| W: Ralph Hefferline > Ralph Franklin Hefferline was a psychology professor at Columbia University. Columbia University > Columbia University is a private Ivy League research university in Upper Manhattan, New York City. |
| C: First identify the [university of psychology professor Ralph Hefferline -Wiki-> y1]. The university of this professor is [y1 -NER(group)-> y2]. Then figure out [y2 is in what city -Wiki-> y3]. |

**Table 14: Few-shot examples used for CoT-FSP baseline model in mathematical reasoning domain.**

| Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees will the grove workers plant today? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21-15=6. The answer is 6.                                          |
| Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?                                                                             |
| A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.                                                                                                     |
| Q: The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers?                 |
| A: The clay pot costs $20 + $9 = $29. The bag of soil costs $9 - $2 = $7. The cost to plant the flowers is $9 + $29 + $7 = $45. The answer is 45.                                 |
| Q: Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. A bag of coffee costs $8 and contains 10.5 ounces of beans. How much does she spend on her coffee per week? |
| A: She uses 3 ounces of beans per day because 2 x 1.5 = 3. She uses 21 ounces of beans per week because 7 x 3 = 21. She buys 2 bags of beans per week because 21 / 10.5 = 2. She spends $16 on the beans per week because 2 x 8 = 16. The answer is 16. |
| Q: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in the server room? |
| A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29.                      |
| Q: From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy the video game console? |
| A: Sam makes $460 / 23 hrs = $20/hr. From September to February, Sam made 8hrs x $20/hr = $160. From March to February, Sam made a total of $460 + $160 = $620. After fixing his car, he was left with $620 - $340 = $280. Sam needs another $600 - $280 = $320. Sam needs to work another $320 / $20/hr = 16 hours. The answer is 16. |
| Q: Of the 90 people on William’s bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What’s the number of Dutch Americans who sat at the windows? |
| A: On the bus, the number of Dutch people was 3/5 of the total number, a total of 3/5 x 90 = 54 people. Out of the 54 people who were Dutch, 1/2 were Dutch Americans, a total of 1/2 x 54 = 27 people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number is 1/3 x 27 = 9. The answer is 9. |
| Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?                                                                         |
| A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74-35=39. The answer is 39.                                   |

**Table 15: Few-shot examples used for CoT-FSP baseline model in Wiki QA domain.**

| Q: Fritz von Brodowski was killed during what global war that lasted from 1939 to 1945? |
| --------------------------------------------------------------------------------------- |
| A: Fritz von Brodowski > Friedrich Wilhelm Konrad von Brodowski was controversially killed while in French custody during World War II. The answer is World War II. |
| Q: Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?     |
| A: Henri Leconte > He won the French Open men’s doubles title in 1984. Jonathan Stark (tennis) > During his career he won two Grand Slam doubles titles. The answer is Jonathan Stark. |
| Q: The director of the romantic comedy “Big Stone Gap” is based in what New York city? |
| A: Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic comedy film directed by Adriana Trigiani. Adriana Trigiani > Adriana Trigiani is an Italian American film director based in Greenwich Village. The answer is Greenwich Village. |
| Q: Are Randal Kleiser and Kyle Schickner of the same nationality?                       |
| A: Randal Kleiser > John Randal Kleiser (born July 20, 1946) is an American film director and producer. Kyle Schickner > Kyle Schickner is an American film producer, writer, director, actor. The answer is yes. |
| Q: Extras was created, written, and directed by Ricky Dene Gervais, an English comedian, actor, writer, producer, director, singer, and musician, born on which date? |
| A: Ricky Gervais > Ricky Dene Gervais (born 25 June 1961) is an English comedian, actor, writer, producer, director, singer, and musician. The answer is 25 June 1961. |
| Q: Sameera Perera is a cricketer from what island country located southeast of the Republic of India and northeast of the Maldives? |
| A: Sameera Perera > Sameera Perera (born 20 August 1988) is a Sri Lankan cricketer. The answer is Sri Lanka. |
| Q: What screenwriter with credits for “Evolution” co-wrote a film starring Nicolas Cage and Téa Leoni? |
| A: The Family Man > The Family Man is a 2000 American romantic comedy-drama film starring Nicolas Cage and Téa Leoni. David Weissman > His film credits include “The Family Man” (2000), “Evolution” (2001), and “When in Rome” (2010). The answer is David Weissman. |
| Q: Ralph Hefferline was a psychology professor at a university that is located in what city? |
| A: Ralph Hefferline > Ralph Franklin Hefferline was a psychology professor at Columbia University. Columbia University > Columbia University is a private Ivy League research university in Upper Manhattan, New York City. The answer is New York City. |

Figure: Figure 5: Guideline for human evaluation on GSM8K mathematical reasoning.

</details>

<details>
<summary>Function calling with OpenAI's API</summary>

# Function calling with OpenAI's API

**Source URL:** <https://platform.openai.com/docs/guides/function-calling>

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
            sign = json.loads(item.arguments)["sign"]
            horoscope = get_horoscope(sign)

            # 4. Provide function call results to the model
            input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": horoscope,
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
69
70
71
72
73
74
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
      additionalProperties: false,\
    },\
    strict: true,\
  },\
];

function getHoroscope(sign) {
  return `${sign}: Next Tuesday you will befriend a baby otter.`;
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

// Preserve model output for the next turn
input.push(...response.output);

for (const item of response.output) {
  if (item.type !== "function_call") continue;

  if (item.name === "get_horoscope") {
    // 3. Execute the function logic for get_horoscope
    const { sign } = JSON.parse(item.arguments);
    const horoscope = getHoroscope(sign);

    // 4. Provide function call results to the model
    input.push({
      type: "function_call_output",
      call_id: item.call_id,
      output: horoscope,
    });
  }
}

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
console.log(response.output_text);
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

If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with `tool_search`. The `tool_search` tool lets the model search for relevant tools, add them to the model context, and then use them. Only `gpt-5.4` and later models support it. Read the [tool search guide](https://developers.openai.com/api/docs/guides/tools-tool-search) to learn more.

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

Parallel function calling is not possible when using [built-in\\
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

If you send `strict: true` and your schema does not meet the requirements above,
the request will be rejected with details about the missing constraints. If you
omit `strict`, the default depends on the API: Responses requests will
normalize your schema into strict mode (for example, by setting
`additionalProperties: false` and marking all fields as required), which can
make previously optional fields mandatory, while Chat Completions requests
remain non-strict by default. To opt out of strict mode in Responses and keep
non-strict, best-effort function calling, explicitly set `strict: false`.

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
<summary>Function calling with the Gemini API</summary>

# Function calling with the Gemini API

**Source URL:** <https://ai.google.dev/gemini-api/docs/function-calling>

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
  console.log(`ID: ${functionCall.id}`);
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

1.  **Define function declaration:** Define the function declaration in your
    application code. Function Declarations describe the function's name,
    parameters, and purpose to the model.
2.  **Call API with function declarations:** Send user prompt along with the
    function declaration(s) to the model. It analyzes the request and determines
    if a function call would be helpful. If so, it responds with a structured
    JSON object containing the function name, arguments, and a unique `id`
    (this `id` is now always returned by the API for Gemini 3 models\*).
3.  **Execute function code (your responsibility):** The Model _doesn't_
    execute the function itself. It's your application's responsibility to
    process the response and check for a function call. If
    - **Yes**: Extract the name, args, and `id` of the function and execute
      the corresponding function in your application.
    - **No:** The model has provided a direct text response to the prompt
      (this flow is less emphasized in the example but is a possible outcome).
4.  **Create user friendly response:** If a function was executed, capture the
    result and send it back to the model, ensuring you include the matching
    `id`, in a subsequent turn of the conversation. It will use the result to
    generate a final, user-friendly response that incorporates the information
    from the function call.

This process can be repeated over multiple turns, allowing for complex
interactions and workflows. The model also supports calling multiple functions
in a single turn ([parallel function calling](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#parallel_function_calling)), in
sequence ([compositional function calling](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#compositional_function_calling)),
and with built-in Gemini tools ([multi-tool use](https://ai.google.dev/gemini-api/docs/function-calling?example=meeting#native-tools)).

\* **Always map function IDs:** Gemini 3 now always returns a unique
`id` with every `functionCall`. Include this exact `id` in your
`functionResponse` so the model can accurately map your result back to the
original request.

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
id='8f2b1a3c' args={'color_temp': 'warm', 'brightness': 25} name='set_light_values'
```

```
{
  id: '8f2b1a3c',
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
    id=tool_call.id,
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
  response: { result },
  id: tool_call.id
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
-   **Always include the exact `id` from the `function_call` in your**
    **`function_response` so the API can map the result to the correct request.**
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

##### Inspecting thought signatures

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

When the model initiates multiple function calls in a single turn, you don't
need to return the `function_result` objects in the same order that the
`function_call` objects were received. The Gemini API maps each result back to
its corresponding call using the `id` from the model's output. This lets you
execute your functions asynchronously and append the results to your list as
they complete.

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
    type: Type.OBJECT,
    properties: {
      brightness: {
        type: Type.NUMBER,
        description: 'The brightness of the lights, 0.0 is off, 1.0 is full.'
      }
    },
    required: ['brightness']
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
    print(f"{fn.name}({args}) - ID: {fn.id}")
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
    console.log(`${fn.name}(${args}) - ID: ${fn.id}`);
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
      id: functionCall.id,
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
  { functionDeclarations: [turnOnTheLightsSchema, turnOffTheLightsSchema] }\
];

await run(prompt, tools=tools, modality="AUDIO")
```

## Function calling modes

The Gemini API lets you control how the model uses the provided tools
(function declarations). Specifically, you can set the mode within
the.`function_calling_config`.

-   `VALIDATED`: Default mode for tool combination (when built-in tools or
    structured outputs also enabled). The model is constrained to predict either
    function calls or natural language, and ensures function schema adherence. If
    `allowed_function_names` is not provided, the model picks from all of the
    available function declarations. If `allowed_function_names` is provided, the
    model picks from the set of allowed functions. This mode reduces malformed
    function calls (compared to `AUTO` mode).
-   `AUTO`: Default mode when only function\_declarations tool enabled.
    The model decides whether to generate a natural language response or suggest
    a function call based on the prompt and context.
-   `ANY`: The model is constrained to always predict a function call and
    ensures function schema adherence. If `allowed_function_names` is not
    specified, the model can choose from any of the provided function declarations.
    If `allowed_function_names` is provided as a list, the model can only choose
    from the functions in that list. Use this mode when you require a function
    call response to every prompt (if applicable).
-   `NONE`: The model is _prohibited_ from making function calls. This is
    equivalent to sending a request without any function declarations. Use this to
    temporarily disable function calling without removing your tool definitions.

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

## Multi-tool use: Combine built-in tools with function calling

You can enable multiple tools, combining built-in tools with function calling in
the same request.

Gemini 3 models can combine built-in tools with function calling out-of-the-box,
thanks to the tool context circulation feature. Read the page on
[Combining built-in tools and function calling](https://ai.google.dev/gemini-api/docs/tool-combination) to learn more.

PythonJavascriptMore

```
from google import genai
from google.genai import types

client = genai.Client()

getWeather = {
    "name": "getWeather",
    "description": "Gets the weather for a requested city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city and state, e.g. Utqiaġvik, Alaska",
            },
        },
        "required": ["city"],
    },
}

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the northernmost city in the United States? What's the weather like there today?",
    config=types.GenerateContentConfig(
      tools=[\
        types.Tool(\
          google_search=types.ToolGoogleSearch(),  # Built-in tool\
          function_declarations=[getWeather]       # Custom tool\
        ),\
      ],
      include_server_side_tool_invocations=True
    ),
)

history = [\
    types.Content(\
        role="user",\
        parts=[types.Part(text="What is the northernmost city in the United States? What's the weather like there today?")]\
    ),\
    response.candidates[0].content,\
    types.Content(\
        role="user",\
        parts=[types.Part(\
            function_response=types.FunctionResponse(\
                name="getWeather",\
                response={"response": "Very cold. 22 degrees Fahrenheit."},\
                id=response.candidates[0].content.parts[2].function_call.id\
            )\
        )]\
    )\
]

response_2 = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=history,
    config=types.GenerateContentConfig(
      tools=[\
        types.Tool(\
          google_search=types.ToolGoogleSearch(),\
          function_declarations=[getWeather]\
        ),\
      ],
      include_server_side_tool_invocations=True
    ),
)
```

```
import { GoogleGenAI, Type } from '@google/genai';

const client = new GoogleGenAI({});

const getWeather = {
    name: "getWeather",
    description: "Get the weather in a given location",
    parameters: {
        type: "OBJECT",
        properties: {
            location: {
                type: "STRING",
                description: "The city and state, e.g. San Francisco, CA"
            }
        },
        required: ["location"]
    }
};

async function run() {
    const model = client.models.generateContent({
        model: "gemini-3-flash-preview",
    });

    const tools = [\
      { googleSearch: {} },\
      { functionDeclarations: [getWeather] }\
    ];
    const toolConfig = { includeServerSideToolInvocations: true };

    const result1 = await model.generateContent({
        contents: [{role: "user", parts: [{text: "What is the northernmost city in the United States? What's the weather like there today?"}]}],
        tools: tools,
        toolConfig: toolConfig,
    });

    const response1 = result1.response;
    const functionCallId = response1.candidates[0].content.parts.find(p => p.functionCall)?.functionCall?.id;

    const history = [\
        {\
            role: "user",\
            parts:[{text: "What is the northernmost city in the United States? What's the weather like there today?"}]\
        },\
        response1.candidates[0].content,\
        {\
            role: "user",\
            parts: [{\
                functionResponse: {\
                    name: "getWeather",\
                    response: {response: "Very cold. 22 degrees Fahrenheit."},\
                    id: functionCallId\
                }\
            }]\
        }\
    ];

    const result2 = await model.generateContent({
        contents: history,
        tools: tools,
        toolConfig: toolConfig,
    });
}

run();
```

For models before the Gemini 3 series, use the
[Live API](https://ai.google.dev/gemini-api/docs/live-api/tools).

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
          id=function_call.id,\
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
    role: 'user',\
    parts: [\
      {\
        functionResponse: {\
          id: functionCall.id,\
          name: functionCall.name,\
          response: functionResponseData,\
          parts: [functionResponseMultimodalData]\
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
              "id": "UNIQUE_CALL_ID_HERE",\
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

For Gemini 3 series models, you can use function calling with
[structured output](https://ai.google.dev/gemini-api/docs/structured-output). This lets the model
predict function calls or outputs that adhere to a specific schema. As a result,
you receive consistently formatted responses when the model doesn't generate
function calls.

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
                model="gemini-3-flash-preview",
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
  model: "gemini-3-flash-preview",
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

| Model | Function calling | Parallel function calling | Compositional function calling |
| --- | --- | --- | --- |
| [Gemini 3.1 Pro Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) | ✔️ | ✔️ | ✔️ |
| [Gemini 3.1 Flash-Lite Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-preview) | ✔️ | ✔️ | ✔️ |
| [Gemini 3 Flash Preview](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Pro](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-pro) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash-lite) | ✔️ | ✔️ | ✔️ |
| [Gemini 2.0 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-2.0-flash) | ✔️ | ✔️ | ✔️ |

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
-   **Mix of bash and custom tools** For those building with a mix of bash and
    custom tools, Gemini 3.1 Pro Preview
    comes with a separate endpoint available via the API called
    [`gemini-3.1-pro-preview-customtools`](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview#gemini-31-pro-preview-customtools).

## Notes and limitations

-   Positioning of function call parts: When using custom function declarations
    [alongside built-in tools](https://ai.google.dev/gemini-api/docs/tool-combination) (like Google
    Search), the model may return a mix of `functionCall`, `toolCall`, and
    `toolResponse` parts in a single turn. Because of this, don't assume the
    `functionCall` will always be the last item in the parts array. If you are
    manually parsing the JSON response, always iterate through the parts array
    rather than relying on position.
-   Only a [subset of the OpenAPI\\
    schema](https://ai.google.dev/api/caching#FunctionDeclaration) is supported.
-   For `ANY` mode, the API may reject very large or deeply nested schemas. If
    you encounter errors, try simplifying your function parameter and response
    schemas by shortening property names, reducing nesting, or limiting the
    number of function declarations.
-   Supported parameter types in Python are limited.
-   Automatic function calling is a Python SDK feature only.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="agentic-design-patterns-part-3-tool-use.md">
<details>
<summary>Agentic Design Patterns Part 3, Tool Use</summary>

Phase: [EXPLOITATION]

# Agentic Design Patterns Part 3, Tool Use

**Source URL:** <https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-3-tool-use/>

Dear friends,

Tool Use, in which an LLM is given functions it can request to call for gathering information, taking action, or manipulating data, is a key design pattern of [AI agentic workflows](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S). You may be familiar with LLM-based systems that can perform a web search or execute code. Indeed, some large, consumer-facing LLMs already incorporate these features. But Tool Use goes well beyond these examples.

If you prompt an online LLM-based chat system, “What is the best coffee maker according to reviewers?”, it might decide to carry out a web search and download one or more web pages to gain context. Early on, LLM developers realized that relying only on a pre-trained transformer to generate output tokens is limiting, and that giving an LLM a tool for web search lets it do much more. With such a tool, an LLM is either fine-tuned or prompted (perhaps with few-shot prompting) to generate a special string like _{tool: web-search, query: "coffee maker reviews"}_ to request calling a search engine. (The exact format of the string depends on the implementation.) A post-processing step then looks for strings like these, calls the web search function with the relevant parameters when it finds one, and passes the result back to the LLM as additional input context for further processing.

Similarly, if you ask, “If I invest $100 at compound 7% interest for 12 years, what do I have at the end?”, rather than trying to generate the answer directly using a transformer network — which is unlikely to result in the right answer — the LLM might use a code execution tool to run a Python command to compute 1 _00 \* (1+0.07)\*\*12_ to get the right answer. The LLM might generate a string like this: _{tool: python-interpreter, code: "100 \* (1+0.07)\*\*12"}_.

But Tool Use in agentic workflows now goes much further. Developers are using functions to search different sources (web, Wikipedia, arXiv, etc.), to interface with productivity tools (send email, read/write calendar entries, etc.), generate or interpret images, and much more. We can prompt an LLM using context that gives detailed descriptions of many functions. These descriptions might include a text description of what the function does plus details of what arguments the function expects. And we’d expect the LLM to automatically choose the right function to call to do a job. Further, systems are being built in which the LLM has access to hundreds of tools. In such settings, there might be too many functions at your disposal to put all of them into the LLM context, so you might use heuristics to pick the most relevant subset to include in the LLM context at the current step of processing. This technique, which is described in the Gorilla paper cited below, is reminiscent of how, if there is too much text to include as context, retrieval augmented generation (RAG) systems offer heuristics for picking a subset of the text to include.

Early in the history of LLMs, before widespread availability of large multimodal models (LMMs) like LLaVa, GPT-4V, and Gemini, LLMs could not process images directly, so a lot of work on Tool Use was carried out by the computer vision community. At that time, the only way for an LLM-based system to manipulate an image was by calling a function to, say, carry out object recognition or some other function on it. Since then, practices for Tool Use have exploded. GPT-4’s function calling capability, released in the middle of last year, was a significant step toward a general-purpose implementation. Since then, more and more LLMs are being developed to be similarly facile with Tool Use.

If you’re interested in learning more about Tool Use, I recommend:

- “ [Gorilla: Large Language Model Connected with Massive APIs](https://arxiv.org/abs/2305.15334?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Patil et al. (2023)
- “ [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Yang et al. (2023)
- “ [Efficient Tool Use with Chain-of-Abstraction Reasoning](https://arxiv.org/abs/2401.17464?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S),” Gao et al. (2024)

Both Tool Use and Reflection, which I described in last week’s [letter](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/?utm_campaign=The%20Batch&utm_source=hs_email&utm_medium=email&_hsenc=p2ANqtz--9ARMthd09q0ABUi-abo6BH62BLbcwPo13LrXs9hUezs-L050Ay7b_rHdWuRIqBVOD6k_S), are design patterns that I can get to work fairly reliably on my applications — both are capabilities well worth learning about. In future letters, I’ll describe the Planning and Multi-agent collaboration design patterns. They allow AI agents to do much more but are less mature, less predictable — albeit very exciting — technologies.

Keep learning!

Andrew

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="h8gMhXYAv1k.md">
<details>
<summary>What is Tool Calling? Connecting LLMs to Your Data</summary>

Phase: [EXPLOITATION]

# What is Tool Calling? Connecting LLMs to Your Data

[ 00:00 ] (The video opens with a man in glasses and a black t-shirt standing in front of a black background. "IBM Technology" is in the top left corner.)
What is tool calling? Tool calling is a powerful technique where you make the LLM context-aware of real-time data, such as databases or APIs. Typically, you use tool calling via a chat interface. (The text "Roy Derks Developer Experience" appears briefly at the bottom of the screen).

[ 00:30 ] So, you would have your client application in one hand, (The man starts drawing on the invisible black board with a green marker, creating two vertical lines and labeling the left one "APP"). and then the LLM on the other side. (He labels the right vertical line "LLM" and writes "chat" at the top center). From your client application, you would send a set of messages together with a tool definition to the LLM. So, you would have your messages here, (He draws a horizontal arrow from APP to LLM and labels it "messages + tools"). together with your list of tools. The LLM will look at both your message and the list of tools, and it's going to recommend a tool you should call. (He draws a horizontal arrow from LLM back to APP and labels it "tool to call").

[ 01:00 ] From your client application, you should call this tool and then supply the answer back to the LLM. (He draws another horizontal arrow from APP to LLM and labels it "tool response"). So, this tool response will be interpreted by the LLM, and this will either tell you the next tool to call or it will give you the final answer. (He draws a final horizontal arrow from LLM back to APP). In your application, you're responsible for creating the tool definition. (He draws a box labeled "APP" on the left side, containing "tool definition" with sub-points: "name", "description", "- input").

[ 01:30 ] So, this tool definition includes a couple of things, such as the name of every tool. It also includes a description for the tool, so this is where you can give additional information about how to use the tool or when to use it. And it also includes the input parameters needed to make a tool call. And the tools can be anything. (He draws a box below "tool definition" labeled "tools" with three circles branching off: "API", "DB", "Code"). So, the tools could be APIs or databases, but it could also be code that you interpret via a code interpreter. So, let's look at an example. Assume you want to find the weather in Miami. You might ask the LLM about the temperature in Miami. (He writes "temp in Miami?" next to "messages + tools".)

[ 02:00 ] You also provide a list of tools. And one of these tools is the weather API. (He writes "Weather API" next to "tools"). The LLM will look at both your question, which is, "What is the temperature in Miami?", it would also look at the weather API. And then, based on the tool definition for the weather API, it's going to tell you how to call the weather tool. So, in here, it's going to create a tool that you can use right here on this side, where you call the API to collect the weather information. You would then supply the weather information back to the LLM. (He updates "tool to call" with "Weather API (Miami)" and then "tool response" with "71°"). So, let's say it would be 71 degrees. The LLM will look at the tool response and then give the final answer, which might be something in the trend of "the weather in Miami is pretty nice, it's 71 degrees."
*Summary: This section explains how traditional tool calling works, using an example of querying weather in Miami via an LLM, highlighting the iterative process of asking, receiving a tool call recommendation, executing the tool, and then providing the tool's response back to the LLM for a final answer.*

[ 02:54 ] This has some downsides. So, when you do traditional tool calling, where you have an LLM and a client application, you could see the LLM hallucinate. (He draws a box on the right labeled "LLM" and adds "- hallucinate" inside). Sometimes the LLM can also make up incorrect tool calls. (He adds "- incorrect" inside the LLM box). That's why I also want to look at embedded tool calling. We just looked at traditional tool calling, but traditional tool calling has its flaws. As I mentioned, the LLM could hallucinate or create incorrect tool calls. That's why I also want to take embedded tool calling into account. (He writes "embedded" above the middle section, creating a new conceptual space).

[ 03:25 ] With embedded tool calling, you use a library or framework to interact with the LLM and your tool definitions. The library would be somewhere between your application and the large language model. (He draws a large box in the middle, between APP and LLM, labeling it "library"). In the library, you would do the tool definition, but you would also execute the tool calls. So, let's draw a line between these sections here. (He draws a line from the "tools" box in APP to the "library" box). So, the library will contain your tool definition. (He writes "tool def" inside the "library" box). It would also contain the tool execution. (He writes "tool exec" inside the "library" box).

[ 03:55 ] So, when you send a message from your application to the large language model, it will go through the library. So, your message could still be "What is the temperature in Miami?" (He draws an arrow from "APP" to "library" and labels it "temp in Miami?"). The library will then append the tool definition and send your message together with the tools to the LLM. (He draws a curved arrow from "library" to "LLM" and labels it "message + tool"). Instead of sending the tool to call to the application or the user, it will be sent to the library, which will then do the tool execution. (He draws a curved arrow from "LLM" back to "library" and labels it "tool").

[ 04:25 ] In this way, the library will provide you with the final answer. (He draws an arrow from "library" back to "APP" and labels it "71°"). Which could be, it's 71 degrees in Miami. When you use embedded tool calling, the LLM will no longer hallucinate, as the library to help you with the tool calling or the embedded tool calling is going to take care of the tool execution and will retry the tool calls in case it's needed. So, in this video, we looked at both traditional tool calling and also embedded tool calling, where especially embedded tool calling will help you to prevent hallucination or help you with the execution of tools, which could be APIs, databases or code.
*Summary: This section introduces embedded tool calling, where a library acts as an intermediary between the application and the LLM, managing tool definitions and execution to prevent hallucinations and ensure correct tool calls, ultimately delivering the final answer to the application.*

[ 04:55 ] (The video ends with the IBM logo on a blue background).

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="react-vs-plan-and-execute-a-practical-comparison-of-llm-agen.md">
<details>
<summary>ReAct vs Plan-and-Execute: A Practical Comparison of LLM Agent Patterns</summary>

Phase: [EXPLOITATION]

# ReAct vs Plan-and-Execute: A Practical Comparison of LLM Agent Patterns

**Source URL:** <https://dev.to/jamesli/react-vs-plan-and-execute-a-practical-comparison-of-llm-agent-patterns-4gh9>

When building LLM Agent systems, choosing the right reasoning pattern is crucial. This article provides an in-depth comparison of two mainstream Agent reasoning patterns: ReAct (Reasoning and Acting) and Plan-and-Execute, helping you make informed technical decisions through practical cases.

## Key Takeaways

- **Understanding Two Major Agent Patterns**
  - ReAct's reasoning-action loop mechanism
  - Plan-and-Execute's planning-execution separation strategy
- **LangChain-based Implementation**
  - ReAct pattern code implementation and best practices
  - Plan-and-Execute pattern engineering solutions
- **Performance and Cost Analysis**
  - Quantitative analysis of response time and accuracy
  - Detailed calculation of token consumption and API costs
- **Practical Cases and Applications**
  - Real-world data analysis tasks
  - Optimal pattern selection for different scenarios
- **Systematic Selection Methodology**
  - Scene characteristics and pattern matching guidelines
  - Hybrid strategy implementation recommendations

## 1. Working Principles of Both Patterns

### 1.1 ReAct Pattern

ReAct (Reasoning and Acting) pattern is an iterative approach that alternates between thinking and acting. Its core workflow includes:

1.  **Reasoning**: Analyze current state and objectives
2.  **Acting**: Execute specific operations
3.  **Observation**: Obtain action results
4.  **Iteration**: Continue thinking and acting based on observations

Typical ReAct Prompt Template:

```
REACT_PROMPT = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Question: {input}
Thought: {agent_scratchpad}"""
```

### 1.2 Plan-and-Execute Pattern

Plan-and-Execute pattern adopts a "plan first, execute later" strategy, dividing tasks into two distinct phases:

1.  **Planning Phase**:
    - Analyze task objectives
    - Break down into subtasks
    - Develop execution plan
2.  **Execution Phase**:
    - Execute subtasks in sequence
    - Process execution results
    - Adjust plan if needed

Typical Plan-and-Execute Prompt Template:

```
PLANNER_PROMPT = """You are a task planning assistant. Given a task, create a detailed plan.

Task: {input}

Create a plan with the following format:
1. First step
2. Second step
...

Plan:"""

EXECUTOR_PROMPT = """You are a task executor. Follow the plan and execute each step using available tools:

{tools}

Plan:
{plan}

Current step: {current_step}
Previous results: {previous_results}

Use the following format:
Thought: think about the current step
Action: the action to take
Action Input: the input for the action"""
```

## 2. Implementation Comparison

### 2.1 ReAct Implementation with LangChain

```
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI

def create_react_agent(tools, llm):
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True
    )

# Usage example
llm = ChatOpenAI(temperature=0)
tools = [\
    Tool(\
        name="Search",\
        func=search_tool,\
        description="Useful for searching information"\
    ),\
    Tool(\
        name="Calculator",\
        func=calculator_tool,\
        description="Useful for doing calculations"\
    )\
]

agent = create_react_agent(tools, llm)
result = agent.run("What is the population of China multiplied by 2?")
```

### 2.2 Plan-and-Execute Implementation with LangChain

```
from langchain.agents import PlanAndExecute
from langchain.chat_models import ChatOpenAI

def create_plan_and_execute_agent(tools, llm):
    return PlanAndExecute(
        planner=create_planner(llm),
        executor=create_executor(llm, tools),
        verbose=True
    )

# Usage example
llm = ChatOpenAI(temperature=0)
agent = create_plan_and_execute_agent(tools, llm)
result = agent.run("What is the population of China multiplied by 2?")
```

## 3. Performance and Cost Analysis

### 3.1 Performance Comparison

| Metric | ReAct | Plan-and-Execute |
| --- | --- | --- |
| Response Time | Faster | Slower |
| Token Consumption | Medium | Higher |
| Task Completion Accuracy | 85% | 92% |
| Complex Task Handling | Medium | Strong |

### 3.2 Cost Analysis

Using GPT-4 model for complex tasks:

| Cost Item | ReAct | Plan-and-Execute |
| --- | --- | --- |
| Average Token Usage | 2000-3000 | 3000-4500 |
| API Calls | 3-5 times | 5-8 times |
| Cost per Task | $0.06-0.09 | $0.09-0.14 |

## 4. Case Study: Data Analysis Task

Let's compare both patterns through a practical data analysis task:

Task Objective: Analyze a CSV file, calculate sales statistics, and generate a report.

### 4.1 ReAct Implementation

```
from langchain.agents import create_csv_agent
from langchain.chat_models import ChatOpenAI

def analyze_with_react():
    agent = create_csv_agent(
        ChatOpenAI(temperature=0),
        'sales_data.csv',
        verbose=True
    )

    return agent.run("""
        1. Calculate the total sales
        2. Find the best performing product
        3. Generate a summary report
    """)
```

### 4.2 Plan-and-Execute Implementation

```
from langchain.agents import PlanAndExecute
from langchain.tools import PythonAstREPLTool

def analyze_with_plan_execute():
    agent = create_plan_and_execute_agent(
        llm=ChatOpenAI(temperature=0),
        tools=[\
            PythonAstREPLTool(),\
            CSVTool('sales_data.csv')\
        ]
    )

    return agent.run("""
        1. Calculate the total sales
        2. Find the best performing product
        3. Generate a summary report
    """)
```

## 5. Selection Guide and Best Practices

### 5.1 When to Choose ReAct

1.  **Simple Direct Tasks**
    - Single clear objective
    - Few steps
    - Quick response needed
2.  **Real-time Interactive Scenarios**
    - Customer service dialogues
    - Instant queries
    - Simple calculations
3.  **Cost-Sensitive Scenarios**
    - Limited token budget
    - Need to control API calls

### 5.2 When to Choose Plan-and-Execute

1.  **Complex Multi-step Tasks**
    - Requires task breakdown
    - Step dependencies
    - Intermediate result validation
2.  **High-Accuracy Scenarios**
    - Financial analysis
    - Data processing
    - Report generation
3.  **Long-term Planning Tasks**
    - Project planning
    - Research analysis
    - Strategic decisions

### 5.3 Best Practice Recommendations

1.  **Hybrid Usage Strategy**
    - Choose patterns based on subtask complexity
    - Combine both patterns in one system
2.  **Performance Optimization Tips**
    - Implement caching mechanisms
    - Enable parallel processing
    - Optimize prompt templates
3.  **Cost Control Methods**
    - Set token limits
    - Implement task interruption
    - Use result caching

## Conclusion

Both ReAct and Plan-and-Execute have their strengths, and the choice between them should consider task characteristics, performance requirements, and cost constraints. In practical applications, you can flexibly choose or even combine both patterns to achieve optimal results.

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>