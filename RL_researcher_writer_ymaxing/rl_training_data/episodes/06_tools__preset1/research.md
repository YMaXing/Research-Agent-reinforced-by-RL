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

-----

Phase: [EXPLOITATION]

### Source [2]: https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: LLMs have general knowledge but lack specific company knowledge base, current time and date, perform poorly with maths calculations, unable to access current events. The ability to use external APIs (public or private) increases LLM power to retrieve data and interact with other systems. For example, for current weather, LLM cannot fulfill alone without real-time data, but programmed to interact with weather API, it formulates API request, receives data, presents to user. This extends capabilities for real-time data and external functionalities. Researchers focus on accuracy in understanding user intent and using external tools to expand intrinsic abilities.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://arxiv.org/html/2507.08034v1

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: Current LLM models handle natural language well but face difficulties with tasks demanding current data or active computational capabilities, like current stock market trends or complex math problems, due to training on fixed datasets and limited direct connection to external databases or APIs. Integrating external tools like calculators, calendars, databases improves capabilities for current data analysis and computations. Methods: Retrieval-augmented generation (RAG) connects to databases or search engines for real-time data; code execution like Python for math computations; connecting APIs for financial, health, weather services; hybrid systems combining symbolic reasoning, knowledge graphs.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://en.wikipedia.org/wiki/Large_language_model

Query: Why do large language models require external tools or actions to interact with the real world beyond text generation, and how do these tools serve as an interface for API calls, databases, and calculations?

Answer: Tool use enables LLMs to interact with external systems, applications, or data sources, e.g., fetch real-time information from an API or execute code. A separate program watches LLM output for special tool-calling syntax, calls the tool, feeds output back into LLM input. Early tool-using LLMs fine-tuned on specific tools; fine-tuning to read API documentation expands tool range. Beyond basic text generation, techniques extend capabilities using external tools and data sources.

-----

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

-----

Phase: [EXPLOITATION]

### Source [7]: https://apxml.com/courses/prompt-engineering-agentic-workflows/chapter-3-prompt-engineering-tool-use/formatting-tool-specifications-llm

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: JSON schemas, often using JSON Schema-like type definitions, are used to describe tools for LLM agents. Each parameter is defined with: name (descriptive, e.g., 'query'), type (e.g., 'string', 'number', 'boolean', 'array', 'object' to help LLMs format data correctly), description (clear explanation of what it represents, constraints, formats), and required/optional status. This is critical for correct tool invocation. Common formats include JSON structures inspired by JSON Schema for parameters and outputs. Modern LLM APIs like OpenAI expect tool specifications in predefined JSON format, such as a list of tools with 'type': 'function', containing 'name', 'description', and 'parameters' as an object with 'properties' (each with type and description) and 'required' array. Example: [{'type': 'function', 'function': {'name': 'get_flight_booking_status', 'description': '...', 'parameters': {'type': 'object', 'properties': {'booking_id': {'type': 'string', 'description': '...'}}, 'required': ['booking_id']}}}]. Adhering to vendor-specific formats enables dedicated tool-use features, allowing LLMs to parse and generate correct calls.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://blog.promptlayer.com/how-json-schema-works-for-structured-outputs-and-tool-integration/

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: JSON Schema provides a standardized way to describe and enforce data structure for LLMs interacting with external tools. It defines input and output formats, ensuring seamless data exchange. For tool integration: 1) LLM is instructed via prompting or function calling to generate output conforming to the schema (e.g., 'Generate a user profile in JSON format according to the provided schema.'). 2) Output is validated against the schema; invalid outputs prompt refinement or flag errors. 3) Valid output is passed to the tool, which interprets it using schema knowledge. Benefits: enforces structure for predictable, machine-readable output; facilitates tool integration as common language; validates data for integrity; improves reliability in LLM-tool interactions. This makes LLM outputs suitable for external systems.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools

Query: How can JSON schemas be used to define tool functions so that LLMs can discover available tools, understand their descriptions, and generate correctly formatted function calls with parameters?

Answer: Function calling uses JSON schemas to define tools, enabling LLMs to emit structured function calls with parameters, execute external code safely, and synthesize results. Schemas are provided to the LLM via system messages, e.g., 'You have access to the following tools: {json.dumps(registry.get_schemas())}'. A ToolRegistry centralizes management, mapping function names to schemas (for LLM consumption) and implementations (for execution). Schemas describe available tools, allowing discovery. LLMs generate responses with tool_calls (list of FunctionCall with name, arguments dict, call_id). The loop: LLM generates response; if tool calls present, execute them (parallel), add results to conversation. This transforms LLMs into agents interacting with external systems. Key: schemas in JSON format teach models to produce correct calls.

-----

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

-----

Phase: [EXPLOITATION]

### Source [12]: https://learn.microsoft.com/en-us/python/api/agent-framework-core/agent_framework?view=agent-framework-python-latest

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: The @ai_function decorator in agent_framework turns a function into an AIFunction for models, executed automatically. It creates a Pydantic model from the function's signature to validate arguments and generate JSON schema for parameters. Parameters: name (uses function __name__ if None), description (uses function docstring if None), approval_mode, max_invocations, max_invocation_exceptions. AIFunction implements ToolProtocol. The decorator extracts function signature for Pydantic model (handling type hints), docstring for description, automating schema generation for agent tools.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://builder.aws.com/content/38oLPJ7KYLglawz3dScA5q8H4XJ/tool-function-decorators-for-strands-agents

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: In Strands Agents, the @tool decorator converts Python functions into agentic tools. The decorated function's parameters become the tool's input schema. Parameter names, data types, and annotations directly influence the schema. Uses Annotated type hints for types and descriptions. @tool description parameter describes the tool generally. Examples: int with description maps to {"type": "integer", "description": "..."}; float to {"type": "number"}; List[float] to {"type": "array", "items": {"type": "number"}}. The decorator extracts type hints (including Annotated for descriptions), parameter names, and signatures to generate JSON tool schemas for agents.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://dev.to/aws/ai-agents-dont-need-complex-workflows-build-one-in-python-in-10-minutes-2m5d

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: The @tool decorator in Strands is used to create tools. The docstring matters as the model uses it with function's type hints to decide when to call and what arguments to pass. Clear docstrings improve tool usage. Agent is wired with model, tools=[decorated_functions], system_prompt. Decorator leverages docstrings and type hints for schema inference in lightweight agent setup.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://dagster.io/blog/python-type-hinting

Query: How do Python decorators automatically extract function signatures, type hints, and docstrings to generate tool schemas and registries in lightweight agent frameworks?

Answer: Type hints indicate types of variables, parameters, return values. Docstrings describe function purpose, arguments, return value, exceptions. Used together: function signature with type hints (e.g., list[dict], str, int -> list[dict]), docstring explains params, returns, exceptions, examples. Improves readability. In agent contexts, type hints and docstrings are extracted for schema generation, though not specific to decorators here.

-----

</details>

<details>
<summary>How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://www.philschmid.de/gemini-function-calling

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: The Gemini API uses GenerateContentConfig to define tools for native function calling. Function declarations are defined in the config object using the Pydantic GenerateContentConfig data structure. Example: from google.genai.types import GenerateContentConfig; config = GenerateContentConfig(system_instruction="You are a helpful assistant that use tools to access and retrieve information from a weather API.", tools=[get_weather_forecast]). The LLM decides if it should call the function or return normal text. Pydantic models like get_weather_forecast are directly passed in the tools list for the LLM to use. System instruction provides context, e.g., current date. Automatic function calling is default with callable functions, so no need to specify automatic_function_calling.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://ai.google.dev/gemini-api/docs/function-calling

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: In the Gemini API, GenerateContentConfig is used to configure tools for function calling. Example: config = types.GenerateContentConfig(tools=[power_disco_ball_impl, start_music_impl, dim_lights_impl]); response = client.models.generate_content(model="gemini-3-flash-preview", contents="Do everything you need to this place into party!", config=config). For automatic function calling, the SDK handles execution. Compositional calling combines tools like google_search and custom functions: config=types.GenerateContentConfig(tools=[types.Tool(google_search=types.ToolGoogleSearch(), function_declarations=[getWeather])], include_server_side_tool_invocations=True). Disable automatic with automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True). Pass functions directly to tools for schema declaration.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://pydantic.dev/docs/ai/core-concepts/output/

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: Pydantic integrates with models for structured outputs. Native Output mode uses model’s native Structured Outputs (JSON Schema), but Gemini cannot use tools simultaneously with structured output, resulting in error. Output functions arguments are validated using Pydantic, can take RunContext, raise ModelRetry. Specify output_type as single function, list of functions, scalars, or Pydantic models. Do not register output function as tool to avoid confusion. For models without native tool calling, other modes produce structured outputs. JSON Mode forces valid JSON, Pydantic validates and retries if fails.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://composio.dev/content/tool-calling-guide-with-google-gemini

Query: How does the Gemini API use GenerateContentConfig for native function calling with tools, and how can Pydantic models be integrated as tools to enable dynamic structured outputs in multi-step agent scenarios?

Answer: Gemini tool calling uses GenerateContentConfig in Python SDK to pass prompt and tools configuration. Gemini decides if function call needed based on prompt and tool descriptions. Returns functionCall object with name and JSON args matching schema. App executes function, feeds back. Uses Client, FunctionDeclaration, GenerateContentConfig. Steps: install google-genai, configure client. Native SDK requires manual tool definitions, execution, loop. Supports agentic workflows via declare tools → functionCall → execute → synthesize.

-----

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

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.codeant.ai/blogs/parallel-tool-calling

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Parallel tool calling allows an LLM to request and execute multiple external functions at the same time instead of waiting for each one to finish before starting the next. When an AI agent handles a complex request, it often pulls data from several sources: APIs, databases, or third-party services. Running all of those calls simultaneously rather than sequentially cuts total response time dramatically. Tool calling itself is the mechanism that lets LLMs interact with the outside world. Without it, a language model can only work with the information already in its training data. With tool calling, the model can fetch live weather, query a database, or trigger an action in another system. Independent Tool Operations: Operations with no shared dependencies are ideal candidates. Fetching user profile, preferences, and notifications from separate services is a classic example since none of those calls affects the others. High-Latency External API Calls: Parallelism provides the greatest gains when individual calls have significant network or processing overhead. If each call takes 500ms, running five of them in parallel saves 2 full seconds compared to sequential execution. When Sequential Execution Is Required: Some operations genuinely depend on each other. You can't parallelize without breaking your logic in cases like: Data dependencies: The output of one tool feeds into another (get user ID, then fetch that user's orders). Ordered operations: Steps follow a required sequence (authenticate first, then access protected resource). State mutations: Tools modify shared state that affects subsequent calls (update inventory, then check availability). Forcing parallelism in any of those scenarios creates race conditions and incorrect results.

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://www.promptingguide.ai/research/llm-agents

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: Tools correspond to a set of tool/s that enables the LLM agent to interact with external environments such as Wikipedia Search API, Code Interpreter, and Math Engine. Tools could also include databases, knowledge bases, and external models. When the agent interacts with external tools it executes tasks via workflows that assist the agent to obtain observations or necessary information to complete subtasks and satisfy the user request. In our initial health-related query, a code interpreter is an example of a tool that executes code and generates the necessary chart information requested by the user. Tools are leveraged in different ways by LLMs: LLM agents are still in their infancy so there are many challenges and limitations that remain when building them.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://arxiv.org/html/2603.22862v2

Query: What are the key limitations and inefficiencies of running multiple tools sequentially in a simple loop for LLM agents, and what common industry tool categories exist for knowledge retrieval, web browsing, code interpreters, and external system interactions?

Answer: To address the cumulative delays and inefficiencies caused by sequential execution in long-chain multi-tool calls, parallel execution (233) has become a key optimization direction. Its core idea is to decompose tasks, identify subtasks with no interdependencies, and execute them simultaneously. SoT (124) accelerates inference by expanding multiple skeleton branches in parallel instead of following a fully sequential decoding pattern. At the tool level, LLMCompiler (78) explicitly plans task dependencies so that independent tool calls can run concurrently. For longer workflows, M1-Parallel (216) further decomposes sequential tasks into independent subtasks coordinated by multiple agents. Parallelized planning-acting (91) extend the same idea by overlapping planning and execution, allowing. In multi-tool orchestration architectures, parallel execution significantly enhances agent efficiency in complex task processing; however, it introduces latent security vulnerabilities. While parallelization is relatively safe for side-effect-free read operations (e.g., web retrieval, information queries), the integration of write operations (e.g., database updates, transaction commits) within tool chains risks race conditions, leading to system state inconsistencies. The integration of external tools has substantially enhanced the capability of agents to address complex tasks. Nevertheless, the reliance on multi-step inference and sequential tool invocation introduces significant efficiency bottlenecks. This chapter reviews emerging optimization strategies from two primary perspectives: mitigating latency in multi-tool chains (§6.1) and managing tool call cost and inference budget (§6.2). Latency in multi-tool chains.

-----

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

-----

Phase: [EXPLOITATION]

### Source [27]: https://www.analyticsvidhya.com/blog/2024/09/enhancing-llms-with-structured-outputs-and-function-calling/

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Enhancing function calling for niche tasks involves fine-tuning small LLMs to handle specific data curation needs. Leveraging techniques like special tokens and LoRA fine-tuning optimizes function execution and improves model’s performance for specialized applications. Data Curation: precise data management for effective function calls. Special Tokens: custom tokens mark beginning and end of function calls for better integration. Model Training: start with instruction-based models trained on high-quality data. LoRA Fine-Tuning: enhances performance in targeted manner. Function Calling with LLMs enables execution of predefined functions as part of response generation, allowing interaction with external systems. Pydantic objects simplify defining and converting schemas for function calling.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://blog.neosage.io/p/an-engineers-guide-to-fine-tuning

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Fine-tuning enables structural consistency: always outputting tool call in exact JSON schema, even for vague user requests. Domain-native reasoning: applying business rules or jargon. Prompt-free formatting: embedded in weights, no need for shots. Fine-tuning makes structure native capability by training on hundreds or thousands of valid examples, internalizing schema's rules. Overcomes limitations of in-context learning like brittleness and inconsistency where model mimics but doesn't learn grammar. Model emits outputs bound to strict API contract, resolves ambiguous terms, refuses sensitive data. Fine-tuning encodes specialized behavior into weights, unlike prompting.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://pavelbazin.com/post/the-essential-guide-to-large-language-models-structured-output-and-function-calling/

Query: How does instruction fine-tuning enable LLMs to interpret tool schemas and produce valid function calls as structured outputs?

Answer: Structured output fine-tune allows models to output JSON more reliably. Models without it output unreliable JSON-looking text. Function calling is structured output with extra steps like RAG. Structured output acquired during fine-tuning. Workflow: provide function descriptions to LLM, it returns call request based on schema, execute, feed back. Function calling possible via structured output without API, but specialized use case of structured output. Provide data specification to LLM.

-----

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

### Source [31]: https://news.ycombinator.com/item?id=43998472

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: In an LLM agent loop with tool use, tool output is fed back by pasting results into the conversation, such as switching models when stuck: tell Gemini to summarize the problem, paste into ChatGPT (O3) for instructions, then paste O3's reply back into Aider to resume progress. Ground truth from tools like compilers or test runs anchors the LLM to prevent drift. Self-healing loops check if steps progress or regress and determine next actions, with nothing explicitly coded. Workflow involves feeding PRD and tasks into Augment Code, which checks work into git branches; Gemini reviews output for issues and feedback, all managed via git to avoid copy/paste insanity. LLMs use git for version control in iterative loops.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://www.emergentmind.com/topics/multi-turn-tool-calling-large-language-models-llms

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: A canonical multi-turn framework includes: Observation with full history of queries, tool calls (arguments), and tool outputs. Planning selects next tool or answers. Tool Execution calls API/function, records output. Termination outputs answer with citations. In advanced settings like persistent Lisp metaprogramming loop, agent-tool creation, versioning, and stateful memory (REPL) enable inventing/refining symbolic procedures across turns. Training uses supervised fine-tuning (SFT) on multi-turn trajectories where each step involves tool selection, argument filling, tool output parsing, and propagation into subsequent reasoning. Loss is next-token cross-entropy, masked for assistant turns.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://community.openai.com/t/how-can-i-ensure-every-llm-reply-includes-exactly-one-message-and-one-tool-call/1283087

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: To combine message and tool call, use structured outputs like JSON schema with strict=true to force format including explanation and tool call. For boolean queries, message shows rationales, tool assesses quality. Use structured output for reasoning first, then verdict. Reasoning models like o3/o4-mini perform background reasoning. Chain-of-thought in prompts helps generate natural language with tool calls.

-----

-----

Phase: [EXPLOITATION]

### Source [34]: https://medium.com/promptlayer/tool-calling-with-llms-how-and-when-to-use-it-d65493a87954

Query: How can tool output be effectively fed back into the LLM to generate natural language responses or determine subsequent actions in a basic tool calling loop?

Answer: Tool calling enables self-healing: LLM makes function call, reads results, decides to retry if needed. Structured JSON outputs ensure consistency. Offload parsing to model providers. For SQL chatbot, LLM detects/corrects mistakes by processing tool outputs iteratively without manual parsing.

-----

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

-----

Phase: [EXPLOITATION]

### Source [37]: https://www.codeant.ai/blogs/parallel-tool-calling

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Independent Tool Operations: Operations with no shared dependencies are ideal candidates. Fetching user profile, preferences, and notifications from separate services is a classic example since none of those calls affects the others. High-Latency External API Calls: Parallelism provides the greatest gains when individual calls have significant network or processing overhead. If each call takes 500ms, running five of them in parallel saves 2 full seconds compared to sequential execution. Batch Processing Scenarios: Applying the same operation to multiple inputs concurrently is another strong use case. Analyzing multiple code files at once, for instance, rather than processing them one by one. When Sequential Execution Is Required: Some operations genuinely depend on each other. You can't parallelize without breaking your logic in cases like: Data dependencies: The output of one tool feeds into another (get user ID, then fetch that user's orders); Ordered operations: Steps follow a required sequence (authenticate first, then access protected resource); State mutations: Tools modify shared state that affects subsequent calls (update inventory, then check availability). Forcing parallelism in any of those scenarios creates race conditions and incorrect results. When Parallel Execution Delivers Gains: Look for patterns like: Independent data fetches: Pulling user profile, preferences, and notifications from separate services. Total latency: Sum of all individual call times (sequential) vs. Duration of the slowest single call (parallel). Parallel execution changes the math. Those same four 300ms calls now complete in roughly 300ms total because they all run concurrently. How Parallel Tool Calling Works Under the Hood: The process breaks into four phases. 1. The Agent Receives a Multi-Tool Request: Picture a user asking: "What's the weather in Chicago, what's on my calendar today, and how long is my commute?" One prompt, but three completely separate data sources. The agent recognizes immediately that it will call multiple tools.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://adk.dev/agents/workflow-agents/parallel-agents/

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: The ParallelAgent is a workflow agent that executes its sub-agents concurrently. This dramatically speeds up workflows where tasks can be performed independently. Use ParallelAgent when: For scenarios prioritizing speed and involving independent, resource-intensive tasks, a ParallelAgent facilitates efficient parallel execution. When sub-agents operate without dependencies, their tasks can be performed concurrently, significantly reducing overall processing time. Example: Imagine researching multiple topics simultaneously: Researcher Agent 1: An LlmAgent that researches "renewable energy sources." Researcher Agent 2: An LlmAgent that researches "electric vehicle technology." Researcher Agent 3: An LlmAgent that researches "carbon capture methods." These research tasks are independent. Using a ParallelAgent allows them to run concurrently, potentially reducing the total research time significantly compared to running them sequentially. The results from each agent would be collected separately after they finish. When the ParallelAgent's run_async() method is called: 1. Concurrent Execution: It initiates the run_async() method of each sub-agent present in the sub_agents list concurrently. This means all the agents start running at (approximately) the same time. 2. Independent Branches: Each sub-agent operates in its own execution branch. There is no automatic sharing of conversation history or state between these branches during execution. 3. Result Collection: The ParallelAgent manages the parallel execution and, typically, provides a way to access the results from each sub-agent after they have completed (e.g., through a list of results or events). The order of results may not be deterministic. Independent Execution and State Management.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://www.kore.ai/blog/boost-ai-agent-performance-with-parallel-execution

Query: In what scenarios does parallel execution of independent tools provide significant latency reductions in agent systems, and how is it implemented?

Answer: Parallel Execution solves this bottleneck by enabling AI agents to launch independent tasks concurrently. As soon as the required input, like a user ID, is available, the agent can leverage tools to trigger simultaneous data fetches from multiple systems without waiting for one to complete before starting the next. Because these systems (e.g., Salesforce, CRM, and helpdesk) operate independently and have no dependencies on each other, the agent can query them simultaneously. Instead of 15 seconds of wait time, the agent receives all the necessary data in just 5–6 seconds on average, the time it takes for the longest of the parallel requests to resolve. Example: With Parallel Execution, the agent instantly dispatches three parallel data requests: one to Salesforce for contact info, another to the CRM for transaction history, and a third to the helpdesk database for support logs. Within 5 seconds, the agent receives and synthesizes a full customer profile, allowing it to respond to the user quickly and accurately. In contrast, a traditional agent working with sequential execution would take three times longer to gather the same information, delaying the response, degrading the user experience, and potentially causing drop-off or frustration. Parallel Execution addresses one of the biggest friction points in AI workflow automation: latency from sequential processing. By eliminating the artificial delays between steps, Parallel Execution ensures that AI agents can operate with the speed and intelligence required in today’s always-on, multi-system enterprise environments.

-----

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

-----

Phase: [EXPLOITATION]

### Source [42]: https://supercharge.io/blog/ai-prompt-engineering-best-practices

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: System prompts define the AI’s core role by outlining the task it should perform and the behavioural standards it should follow. An ideal prompt is clear, dense, and easy to understand, leaving no room for misinterpretation. In complex AI systems, prompts are enriched with additional components like context, explanations, or relevant documentation to guide the model effectively. Effective prompts contain: 1. System prompt: Defines core role, task, and behavioral standards. This may include available tools and functions. 2. Context: Relevant data sources such as retrieved documents (via RAG), available tools and functions, user background, conversation history, examples. The system prompt acts as the foundational instruction set guiding output in Agentic AI systems.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://superlinear.eu/insights/articles/prompt-engineering-for-llms-techniques-to-improve-quality-optimize-cost-reduce-latency

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: Structure prompts with XML tags to delineate instructions, context, and examples. Best practices: 1. Be explicit with instructions: Clear, specific directives for nuanced behaviors. 2. Add relevant context or motivation. 3. Pay attention to examples and details. 4. Clearly defining explicit instructions. 5. Providing context and motivations. 6. Structuring with XML tags. 7. Few-shot prompting and Chain of Thought (CoT). 8. Position critical information early. CoT implemented with phrases like “Think step-by-step,” explicit reasoning, or XML tags (e.g., <thinking> and </thinking>) to separate reasoning from final response. Example: Draft emails using XML-structured prompts: 'Draft personalized emails... Program:<program>{{PROGRAM_DETAILS}}</program> Donor:<donor>{{DONOR_DETAILS}}</donor>'.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://community.openai.com/t/prompting-best-practices-for-tool-use-function-calling/1123036

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: For tool use (function calling), include tool details in the system prompt for the model to reference them during responses. JSON definitions serve the API, but the model processes only text in the conversation; API parameters like tool definitions are not automatically added to the model's context. It is not strictly necessary to declare tools in the system prompt, but it helps to emphasize their presence or prioritize specific functions. The system prompt is about 'emphasis' in general. You can pass description fields in JSON tool definitions, but explicit text in the prompt ensures the model knows about them. Sometimes direct the model via system prompt to be consistent about tool awareness.

-----

-----

Phase: [EXPLOITATION]

### Source [45]: https://towardsdatascience.com/boost-your-llm-outputdesign-smarter-prompts-real-tricks-from-an-ai-engineers-toolbox/

Query: What are effective strategies for designing system prompts that guide LLMs on when and how to use available tools, including guidelines for response behavior and XML-tagged tool lists?

Answer: Tip 1: Ask the LLM to write its own prompt. Start with a rough outline explaining tasks and rules, then iteratively refine based on evaluation to match desired results, integrating edge cases. This co-construction produces precise, effective prompts for stable AI workflows.

-----

</details>

<details>
<summary>How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?</summary>

Phase: [EXPLOITATION]

### Source [46]: https://www.decodingai.com/p/tool-calling-from-scratch-to-production

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: The `TOOLS_BY_NAME` mapping is a dictionary that maps tool names to their corresponding function handlers, such as {'google_search': <function google_search at 0x...>, 'perplexity_search': <function perplexity_search at 0x...>, 'scrape_url': <function scrape_url at 0x...>}. The `TOOLS_SCHEMA` contains the JSON schemas for these tools. Developers decorate functions with a @tool decorator to automatically populate `TOOLS_SCHEMA` and `TOOLS_BY_NAME` registries. For example, @tool def google_search(query: str) -> dict: ... and @tool def scrape_url(url: str) -> dict: .... A central `TOOLS` dictionary is constructed as {'google_search': {'handler': google_search, 'declaration': google_search_schema}, ...}. Then, `TOOLS_BY_NAME = {tool_name: tool['handler'] for tool_name, tool in TOOLS.items()}` and `TOOLS_SCHEMA = [tool['declaration'] for tool in TOOLS.values()]`. These mappings facilitate LLM-selected tool execution in from-scratch implementations by allowing the LLM to select a tool by name from the provided schemas (`TOOLS_SCHEMA`), after which the system looks up the exact function handler in `TOOLS_BY_NAME` to execute it with the parameters generated by the LLM. This decouples schema provision to the LLM from actual function execution, enabling efficient tool calling without hardcoding.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://www.salmanq.com/blog/llm-built-in-tools/

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: In from-scratch implementations using function tools (user-defined), you provide the LLM with a list of tools including name, natural language description, and JSON schema describing parameters. The model generates a structured JSON call based on this. Your code then uses registries or mappings to execute the specified function with those parameters and passes the result back to the model. This contrasts with built-in tools where no schema is provided, but function tools rely on such mappings to handle execution after LLM selection from the schema.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/

Query: How do tool registries and mappings like TOOLS_BY_NAME and TOOLS_SCHEMA facilitate the execution of LLM-selected tools in from-scratch implementations?

Answer: In custom agent implementations (from-scratch), you decide which tools to connect and provide them to the LLM. The workflow is: LLM recognizes need for a tool, selects which one from available options (implying a registry of tools), generates parameters, executes the tool, and integrates results. Tool selection from a registry of 3-5 essential tools prevents confusion; mappings facilitate looking up and executing the selected tool efficiently.

-----

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

-----

Phase: [EXPLOITATION]

### Source [51]: https://www.awesome-testing.com/2025/09/mermaid-diagrams

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams visualize LLM function calling flows relevant to agent architectures. Example flowchart for single-turn and multi-tool loops: flowchart TD A[User Input] --> B[LLM Receives Prompt + Tool Schemas] B --> C{Should I use a tool?} C -- Yes --> D[LLM emits structured function call] D --> E[API routes call to tool handler] E --> F[Tool executes with parameters] F --> G[Tool returns result] G --> H[LLM integrates result] H --> I{Another tool needed?} I -- No --> J[LLM crafts final response] J --> K[Response sent to User] I -- Yes --> D C -- No --> J. This shows decision points (should use tool? another tool needed?), tool calling (structured function call, tool execution), loops (yes back to D for multi-tool), and integration (LLM integrates result into response). There's also an LLM Function Calling Sequence Diagram showing sequence of interactions. Mermaid supports native integrations in GitHub/GitLab for rendering in docs, enhancing clarity of complex workflows like AI agents and function calling. Collection of examples at mermaids GitHub repo covers AI agents, function calling workflows.

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://www.flowgif.com/

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams visualize complex flows, processes, or architectures in agent contexts via MCP (agent integration). Tools for agents: mermaid_generator (generate static/animated diagrams), mermaid_from_conversation (extract flows from transcripts), animate_mermaid_code (animate existing Mermaid), auto_animate_mermaid_code (deterministic animation). Example agent integration: from pydantic_ai import Agent; server = MCPServerStreamableHTTP(...); agent = Agent(..., toolsets=[server]); agent.run('Create an animated signup flow...'). Animate static Mermaid into guided walkthroughs for step-by-step processes like tool calling flows. Paste view URLs (PNG/GIF) in markdown/docs. Generates/animates diagrams for clarity in agent architectures, addressing overload in complex flows.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://ranjankumar.in/stop-pasting-screenshots-how-ai-engineers-document-systems-with-mermaid

Query: How can mermaid diagrams be used to visualize single-turn tool calling flows, multi-tool loops, and the integration of structured output tools in agent architectures?

Answer: Mermaid diagrams document AI systems like agent architectures with tool orchestration. Essential patterns for AI engineers: LLM Agent Architecture with Tool Orchestration (flowchart showing query routing through paths). Subgraphs define system boundaries (stateful/stateless components). Example: graph LR A[Agent Router] --> B[Search Tool]; click A "link_to_code"; click B "link_to_code". Makes diagrams navigable to code. RAG system flowchart shows routing logic. Updates in repo docs/ folder sync with code changes. Visualizes tool orchestration, decisions, branches in agent flows. Patterns refined for production systems handling millions of queries.

-----

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

-----

Phase: [EXPLOITATION]

### Source [56]: https://sparkco.ai/blog/advanced-tool-calling-in-llm-agents-a-deep-dive

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: The evolution of tool calling has transitioned from basic integrations to advanced capabilities involving structured reasoning and memory management. Frameworks such as LangChain, AutoGen, CrewAI, and LangGraph have played pivotal roles in this transformation. These frameworks offer robust tool calling schemas that allow LLMs to intelligently select and execute external APIs, databases, or custom functions, thus enhancing their ability to perform complex tasks. Tool calling refers to the ability of LLM agents to interact with external APIs, databases, or custom functions, thereby extending their utility and effectiveness. By 2025, tool calling has evolved from basic API integrations to encompass structured reasoning, robust memory management, and sophisticated agent orchestration. The historical development of tool calling in LLM agents has moved from simple API interactions to an intricate framework of structured reasoning, memory management, and advanced integration capabilities.

-----

-----

Phase: [EXPLOITATION]

### Source [57]: https://composio.dev/content/ai-agent-tool-calling-guide

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: The shift from 'chatbots' to 'AI agents' hinges on a single technical capability: Tool Calling. Tool Calling provides the I/O layer for LLMs, allowing them to execute actions and access real-time data. Tool Calling transforms LLMs from passive text generators into active agents that interact with external systems like Salesforce or GitHub. Tool Calling is the mechanism. The fundamental ability of a model to output structured JSON arguments instead of text. It allows the brain (LLM) to manipulate objects. For engineering leaders evaluating integration strategies, you need to separate the core mechanism (Tool Calling) from the discovery standards (Tool Search) and the emerging interface protocols (MCP). The real challenge isn’t the LLM’s reasoning, but the complex engineering required for secure and reliable tool execution (auth, error handling, etc.). This guide dissects the modern tool calling stack, moving from foundational concepts to enterprise architecture.

-----

-----

Phase: [EXPLOITATION]

### Source [58]: https://galileo.ai/blog/7-essential-skills-for-building-ai-agents

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: Building AI agents demands technical skillsets that extend beyond traditional software development. As enterprises deploy AI agents in production environments, tasks like model evaluation, hallucination detection, and system monitoring require specialized expertise and robust development patterns. This article examines the essential skills required for building robust, production-ready AI agents, focusing on advanced development patterns that drive successful AI agent development.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://www.getmaxim.ai/articles/understanding-tool-calling-mechanisms-in-ai-agents-a-deep-dive-into-execution-efficiency/

Query: In what ways does tool calling form the foundational skill for AI engineers to build, debug, and monitor agentic systems, with transitions to advanced patterns like planning and memory?

Answer: Tool calling is the mechanism by which an AI agent decides to use external tools—functions, APIs, databases, or retrieval pipelines—while solving a task. Efficient execution depends on deterministic planning, low-latency routing, robust observability, and evaluations that quantify correctness and cost. Engineering teams should standardize on an AI gateway with distributed tracing, semantic caching, failover, and governance; pair this with pre-release simulations and in-production observability to ensure reliable, scalable agent behavior. Use structured schemas, measurable evals, and prompt versioning to drive continuous improvement. Maxim AI’s full-stack approach addresses this lifecycle end-to-end: experimentation, simulation, evaluation, observability, and data curation for multimodal agents.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?</summary>

Phase: [EXPLORATION]

### Source [60]: https://www.decodingai.com/p/tool-calling-from-scratch-to-production

Query: What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?

Answer: Implementing tool calls from scratch involves manually keeping track of function schemas or complex tool calling system prompts, which reveals the core mechanics but is burdensome for production systems. For production-level tool calls, modern LLM APIs like Google’s Gemini allow declaring tools directly in the API call, which is more efficient, modern, and reliable. The only focus should be on defining well-documented functions, as the provider optimizes schemas and prompts for specific models. Doing it yourself with open-source models quickly becomes a big burden, highlighting trade-offs in reliability, efficiency, and maintenance when building custom frameworks from scratch without API support.

-----

-----

Phase: [EXPLORATION]

### Source [61]: https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/tool-error-handling

Query: What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?

Answer: Primary error sources in LLM agent tools include: 1. Input Issues: Invalid, malformed, or unexpected input from LLM misunderstanding format or constraints (e.g., text instead of number). 2. External Service Failures: APIs or databases unavailable, internal errors, rate limits, authentication failures. 3. Network Problems: Connectivity issues, timeouts, DNS failures. 4. Internal Tool Logic Errors: Bugs or unhandled edge cases. 5. Resource Unavailability: Missing files, dropped database tables, insufficient resources. For retries with exponential backoff: Effective for transient issues like network glitches or overloads (delays: 1s, 2s, 4s), but cap retries to avoid indefinite looping and overwhelming services. Timeouts: Essential to prevent indefinite hanging; report clearly to LLM, but handling requires care as unresponsive services block agents.

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://www.codecentric.de/en/knowledge-hub/blog/resilience-design-patterns-retry-fallback-timeout-circuit-breaker

Query: What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?

Answer: Timeouts challenge: Avoid requests stuck forever, but not trivial—e.g., order placement timeout leaves uncertainty if processed or not. Combining with retry risks duplicates (e.g., duplicate orders); marking as failed might miss successes. Timeouts must balance: high enough for slow responses, low enough to discard hopeless ones. No framework supports all resilience patterns out-of-box (e.g., Vert.x lacks some). Alternatives: Dedicated libraries like resilience4j, failsafe (code-level integration via interfaces/annotations), Hystrix (inactive), or service meshes like Istio (infrastructure-level). Trade-offs: Choose based on framework compatibility; no one-size-fits-all—teams must evaluate application needs for resilience implementation.

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://www.elastic.co/es/pdf/agentic-frameworks-practical-considerations-for-building-ai-augmented-security-systems.pdf

Query: What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?

Answer: In custom tool calling, keep tools simple/reliable (one task like API call/DB query, concise results). On failure (network issues/error): Catch exception, retry or fallback message to agent (e.g., “no data available”). Clear failure policy: Treat tool error/no result as neutral (“didn’t find anything”) vs. catastrophic fail; use fallback tools/redundant sources (e.g., VirusTotal fail → internal cache); log usage/outcomes for debugging/observability to detect over-reliance on flaky tools or token waste. Manual tool calls show benefits of frameworks abstracting complexity. Frameworks provide built-in: robust error handling, efficient parallel tool calls, traceability. Trade-offs in custom: Iteration for balance in tool calls (monitor frequency/relevance); avoid over-calling unneeded tools.

-----

-----

Phase: [EXPLORATION]

### Source [64]: https://sparkco.ai/blog/advanced-error-handling-strategies-in-langgraph-applications

Query: What are the primary engineering challenges and trade-offs in implementing robust error handling, retry logic, and fallback mechanisms within custom tool calling frameworks from scratch?

Answer: LangGraph simplifies orchestration of complex AI systems (tool calling, memory, agents) but error handling is critical challenge—if mishandled, causes disruptions/performance degradation. Advanced strategies needed for interconnected nodes/processes. Example tool calling with error management: Try-catch around tool call; for transient errors, implement retry or fallback; else throw critical failure. Future trends: Real-time adaptive systems, tool calling patterns (e.g., CrewAI) with memory for multi-turn convos/agent ops drive error management innovations. Implementing from scratch requires custom logic for distinguishing transient vs. permanent errors, retries, fallbacks to maintain robustness/scalability in graph-based pipelines.

-----

</details>

<details>
<summary>How does the choice of embedding models and similarity thresholds affect the precision of tool selection when descriptions are scaled to hundreds of options in production systems?</summary>

Phase: [EXPLORATION]

### Source [65]: https://www.linkedin.com/posts/anthony-alcaraz-b80763155_openai-limits-you-to-128-tools-per-session-activity-7415341671103488000-2V8c

Query: How does the choice of embedding models and similarity thresholds affect the precision of tool selection when descriptions are scaled to hundreds of options in production systems?

Answer: The scalability cliff for tool selection: For tool counts <128, direct access works; 128-512, retrieval recommended; >512, retrieval mandatory. Most enterprises hit 512+ tools within months. The survey focuses heavily on vector similarity search using embeddings for tool selection. Graph-based approaches (semantic search + dependency traversal) and ontology-driven methods outperform pure vector retrieval in production. Context engineering matters more than model selection for handling large numbers of tools. Production systems must manage tool results to avoid context overflow by reducing, isolating, or offloading. Questions raised include validating retrieval-based tool selection precision vs. confidently wrong choices and failure rates in production with hundreds of tools.

-----

</details>

<details>
<summary>How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?</summary>

Phase: [EXPLORATION]

### Source [70]: https://arxiv.org/html/2412.15660v1

Query: How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?

Answer: The paper describes an enterprise-scenario LLM function-calling capability training pipeline tested in a digital HR intelligent agent scenario within a large corporate group involving over 8,000 employees. Users interact with the agent in Chinese to inquire about company employees and departments. The system provides 14 specialized workflows, each encapsulated as function tools. The LLM interprets user queries, accurately passes them as parameters to these workflows. The workflows automatically query relevant data from the database, summarize results, and deliver them back to users. This demonstrates adaptation of LLM function-calling for enterprise workflows, where LLMs use tools like APIs, algorithms, code workflows, and operational pipelines. Models select tools based on format and provide input parameters. For stable data synthesis and tool usage, tools require: Tool Name, Tool Description, Parameter Names, Parameter Descriptions, Parameter Data Types, Parameter Necessity. High-accuracy parameters use specific examples and default values. Toolformer enhances LLM’s tool usage by annotating examples and training with augmented data to identify retrievable information via function calls.

-----

-----

Phase: [EXPLORATION]

### Source [71]: http://www.dre.vanderbilt.edu/~schmidt/PDF/LLM-chapter-2024-12-15.pdf

Query: How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?

Answer: LLMs are integrated into software development and DevOps pipelines for tasks like generating code from prompts, code refactoring, code transformations to different languages, and software quality control such as peer reviews and static/dynamic analysis. Developers use LLMs via browser prompts or coding assistants like GitHub Copilot and Amazon CodeWhisperer merged with IDEs (IntelliJ, Android Studio, Visual Studio, Eclipse). This creates hybrid workflows where AI augments human developers by automating routine coding tasks while humans oversee and integrate the outputs.

-----

-----

Phase: [EXPLORATION]

### Source [72]: https://devm.io/machine-learning/llm-software-development-coding

Query: How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?

Answer: LLMs enable hybrid human-AI collaborative workflows in software development lifecycles. In requirements analysis, they generate, validate, refine SRS. In design/development, generate code snippets, documentation, test cases, design explanations, integrating with IDEs for contextual assistance. For lifecycle management, facilitate continuous integration, automated code reviews, requirement traceability. Emphasizes human-in-the-loop designs: AI generates suggestions, flags issues, automates routine tasks; humans make final decisions for accountability. Integrates with traditional tools like IDEs embedding LLM assistants, continuous integration, testing, version control for seamless adoption without compromising rigor.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://www.zenml.io/blog/llmops-in-production-457-case-studies-of-what-actually-works

Query: How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?

Answer: Barclays adapts MLOps infrastructure for LLMs using a hybrid approach combining traditional ML with GenAI in production. Emphasizes open-source tools, interoperability, vector databases for RAG, new LLM monitoring metrics, regulatory compliance, focusing on business value and ROI. This represents enterprise adaptation of LLM paradigms into DevOps pipelines.

-----

-----

Phase: [EXPLORATION]

### Source [74]: https://martinfowler.com/articles/function-call-LLM.html

Query: How have function calling and tool use paradigms from LLMs been adapted to create hybrid human-AI collaborative workflows in enterprise software development and DevOps pipelines?

Answer: Function calling (or tool calling) enables LLMs to interact with external tools and real-world applications, allowing AI agents to interpret user intent, reason, and take actions. LLM analyzes natural language input, extracts intent, generates structured output with function name and arguments for invocation. LLM does not execute calls; it creates data structures passed to separate programs for execution. Prompts include details on possible functions and usage conditions. Tool calling is broader, including code interpreters, retrieval from files/databases. Supports building AI agents interacting with external world in workflows.

-----

</details>

<details>
<summary>What insights from cognitive science on human tool use and affordance perception can inform the design of more intuitive tool descriptions and registries for LLM agents?</summary>

Phase: [EXPLORATION]

### Source [75]: https://arxiv.org/html/2602.20867v1

Query: What insights from cognitive science on human tool use and affordance perception can inform the design of more intuitive tool descriptions and registries for LLM agents?

Answer: Cognitive science provides a useful lens for understanding skills in LLM agents beyond mere tool use. Foundational works from cognitive science, such as Anderson’s ACT-R theory, distinguish declarative memory (facts and episodes) from procedural memory (production rules that encode condition–action pairs). Experts differ from novices less in what they know than in the richness of their procedural repertoire: action patterns that trigger automatically when conditions are met, freeing working memory for higher-level reasoning. This suggests that intuitive tool descriptions for LLM agents should highlight affordances and procedural memory, focusing on how tools can be used effectively, akin to skills as procedural memory. In agent benchmarks, SayCan in robotics uses affordance-based approaches, indicating relevance to tool registries that emphasize condition-action pairs for intuitive access and use.

-----

-----

Phase: [EXPLORATION]

### Source [76]: https://pubmed.ncbi.nlm.nih.gov/26881695/

Query: What insights from cognitive science on human tool use and affordance perception can inform the design of more intuitive tool descriptions and registries for LLM agents?

Answer: The source discusses manipulation-based versus reasoning-based approaches to tool use and affordance perception in cognitive science. Manipulation-based approaches involve direct physical interaction to perceive affordances, while reasoning-based approaches rely on mental simulation or inference about tool possibilities. Human tool use combines both, with affordances being perceived properties that indicate action possibilities (e.g., a hammer affords hammering). For LLM agent tool design, intuitive descriptions should incorporate both direct (e.g., clear input/output specs mimicking manipulation) and reasoning-based (e.g., semantic descriptions of potential uses) elements. A new framework accommodating both could inform registries by structuring tools with dual representations: perceptual affordance cues and inferential guidelines, shedding light on cognitive bases for more natural tool selection and application by agents.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://escholarship.org/content/qt3pm8k2kv/qt3pm8k2kv.pdf

Query: What insights from cognitive science on human tool use and affordance perception can inform the design of more intuitive tool descriptions and registries for LLM agents?

Answer: Findings from studies on LLM-based tool design highlight cognitive barriers like information overload and limited conceptions of LLMs’ abilities, analogous to human affordance perception challenges. Humans tend to overgeneralize or design prompts resembling human-to-human instructions, impeding effective tool use. For intuitive tool descriptions and registries, manage attention by surfacing relevant affordance-like information (e.g., key capabilities) at the right time, avoiding overload. Implications for non-AI-expert-facing LLM tools include improving 'LLM-and-prompt literacy' through structured registries that present tools with clear, non-overloaded affordance cues, aiding perception of what tools 'afford' in task contexts.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://cogscillm.com/

Query: What insights from cognitive science on human tool use and affordance perception can inform the design of more intuitive tool descriptions and registries for LLM agents?

Answer: The CogSci 2023 workshop on 'Large language models meet cognitive science' discusses LLMs as tools and models for human cognition, including topics on psychological tasks LLMs struggle with and using psychological theory to structure understanding. Relevant to tool use, it explores how LLMs encode knowledge differently from humans, potentially informing affordance perception in agent registries by drawing on cognitive science methods to test and design intuitive tool interfaces that align LLM tool selection with human-like perception of action possibilities.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="apxml-com.md">
<details>
<summary>apxml-com</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://apxml.com/courses/prompt-engineering-agentic-workflows/chapter-1-llm-agent-tooling-foundations/tool-error-handling>

The provided markdown content is a "404 Page Not Found" error page, which is entirely web-page boilerplate and not substantive article content. Therefore, all of it should be removed.

```markdown

```

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

## Function Calling

Large language models excel at reasoning, writing, and analysis, yet they remain confined to the text they were trained on. They cannot check the weather, calculate precise mathematical expressions, query databases, or interact with external APIs. [Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) bridges this gap by enabling models to express _intent_ to use [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools) in a structured, machine-readable format. Rather than simply describing what a calculator might do, the model outputs a precise JSON object specifying which function to invoke and with what arguments. This [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) transforms the model from a passive text generator into an active agent that can retrieve information, perform computations, and affect external systems.

The shift from natural language tool descriptions to structured function calling represents an important architectural decision. Early approaches to tool use relied on [in-context learning](https://mbrenndoerfer.com/writing/in-context-learning-llm-examples), where you provided examples of tool usage within the prompt yourself. While effective for simple cases, this approach consumed valuable [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp) space and suffered from inconsistency as the complexity of available tools increased. Native function calling capabilities, by contrast, bake the understanding of tool schemas directly into the model's weights through specialized fine-tuning. This creates a more reliable, scalable interface, where the model learns to treat tool schemas as first-class citizens in its output space, much like it learns grammar or factual associations.

As we discussed in [Tool Use Motivation](https://mbrenndoerfer.com/writing/tool-use-motivation-llm-limitations), the shift from in-context tool demonstrations to native [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) capabilities represents a significant evolution in how language models interface with the world. In this chapter, we examine the mechanics of function calling: how you define tool schemas, how models generate structured calls, how execution results feed back into the generation process, and how to fine-tune models for robust tool-use capabilities.

Function Calling vs. Tool Use

The terms "function calling" and "tool use" are often used interchangeably, but they carry slightly different connotations. Function calling emphasizes the mechanism: the model emits structured calls with named parameters. Tool use is the broader concept: the model employs external capabilities to answer queries. Every function call is a form of tool use, but tool use includes other patterns like web search, code execution, and memory retrieval that may not follow a strict function-call schema.

Understanding why [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) works requires thinking about the information-theoretic problem it solves. A language model generating free text must simultaneously decide what information to communicate and how to format it for the recipient. When the recipient is a human, natural language is ideal. When the recipient is a software system, natural language is ambiguous and brittle. Function calling resolves this by separating the decision of what to do (natural language understanding) from the specification of how to do it ( [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) generation). The model uses its linguistic training to understand intent and its fine-tuned schema knowledge to express that intent unambiguously.

## Function Schema Definition

For a language model to invoke [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools), it must first understand what tools are available, what parameters they accept, and what types of values those parameters require. This metadata is provided through **function schemas**, typically expressed in JSON Schema format, which serves as a contract between the model and the external environment. The schema acts as a Rosetta Stone translating between the unstructured world of human language and the rigid requirements of software APIs.

Think of a function schema as a documentation standard that a model can read and act on. When a human developer reads API documentation, they build a mental model of what the function does, what inputs it needs, and what outputs to expect. They can then write code that calls the function correctly. The model does something analogous at inference time: it reads the schema, develops a representation of the tool's purpose, and generates calls that conform to the specification. The quality of the schema directly determines how reliably this process works.

### JSON Schema Structure

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

### Type System and Constraints

JSON Schema provides rich typing capabilities that help constrain model outputs and prevent hallucinated parameters. These constraints serve as [guardrails](https://mbrenndoerfer.com/writing/content-safety-and-moderation-ai-agents) that reduce the cognitive load on the model during generation. When a parameter is constrained to an integer type with a minimum value of zero, the model need not consider negative numbers or fractional values, effectively narrowing the search space during token sampling.

The available type primitives and constraint mechanisms include:

- **Primitive types**: `string`, `number`, `integer`, `boolean`, `array`, `object`, and `null`. These basic types align with most programming language type systems, making translation to actual function arguments straightforward.
- **Enum constraints**: Restrict string values to a predefined set of options, reducing the probability of invalid values. For example, a `color` parameter with enum `["red", "green", "blue"]` prevents the model from inventing colors like "turquoise" when only primary colors are supported by the underlying API.
- **Array schemas**: Define homogeneous arrays with `items` specifications or heterogeneous tuples with `prefixItems`. This allows for complex inputs like lists of coordinates or structured records.
- **Nested objects**: Support complex parameter structures through recursive `properties` definitions. This is essential for APIs that require structured data, such as shipping addresses with nested fields for street, city, and postal code.
- **Validation keywords**: `minimum`, `maximum`, `minLength`, `maxLength`, `pattern` ( [regex](https://mbrenndoerfer.com/writing/regular-expressions-pattern-matching-nlp-python)), and `format` (email, URI, date-time). These constraints serve dual purposes. During inference, they guide the model toward valid outputs through the semantic cues in parameter descriptions. During structured decoding (as discussed in [Constrained Decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output)), they can be enforced grammatically to guarantee syntactic validity.

The interplay between these constraints creates a robust interface. When a model sees a parameter defined as a string with pattern `^[0-9]{5}$`, it understands not just that a zip code is required, but that the value must consist of exactly five digits. This semantic signal helps the model extract the correct information from your queries or recognize when it lacks necessary information.

A well-designed schema reduces ambiguity at every level. Numeric ranges communicate expected magnitudes: a `page_number` parameter with `minimum: 1` implicitly tells the model that pages are one-indexed, not zero-indexed. String format constraints communicate the expected structure of textual inputs. Even the choice between `number` and `integer` provides semantic information: using `integer` for a `quantity` parameter signals that fractional quantities are not meaningful. Every constraint you add is information the model can use to generate more accurate calls.

### Schema Design Best Practices

Writing effective schemas is an iterative process that benefits from understanding how the model interprets them. The descriptions you write are not just documentation for human readers; they are the primary signal the model uses to decide whether and how to invoke the tool. Treat every word in a description as meaningful input to the model's decision process.

Several principles consistently produce more reliable schemas. First, be specific about what the function does rather than what it is. "Search products" is weaker than "Search the catalog for products matching keywords, returning up to 20 results sorted by relevance." The latter communicates the function's behavior, expected output format, and appropriate use case. Second, explicitly describe what the function does _not_ do when there is potential for confusion with similar tools. If you have both a `search_products` and a `lookup_product_by_id` function, adding "Do not use this function when you have a specific product ID; use lookup\_product\_by\_id instead" to the search function's description prevents the model from using the wrong tool.

Third, use consistent naming conventions across all functions in a toolkit. If some functions use `user_id` as a parameter name and others use `userId` or `uid`, the model may struggle to recognize that they refer to the same concept. Consistency reduces the cognitive overhead the model faces when reading schemas and makes [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) more reliable. Fourth, keep required parameters minimal. Every required parameter is a point of potential failure: if the model cannot extract or infer the value, the call fails. When a parameter can be given a sensible default, make it optional with a default value documented in the description.

Finally, test your schemas with adversarial queries: questions that are adjacent to the function's domain but should not trigger it, questions that require the function but provide information in unexpected formats, and questions that are genuinely ambiguous between multiple tools. The cases where the model makes wrong decisions reveal gaps in your schema descriptions that can be addressed iteratively.

### Multiple Function Definitions

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

## Function Call Generation

Given a set of function schemas and your query, the model must determine whether to answer directly, request clarification, or emit a structured function call. This decision emerges from the model's training on large corpora of tool-use demonstrations. The generation process represents a specialized form of [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) prediction, where the output must conform to a specific grammar defined by the function schema.

The key insight is that function call generation is not a fundamentally different capability from ordinary text generation: it is the same next-token prediction mechanism applied to a different output distribution. What changes is the target distribution. During pre-training, the model learns to predict the next token in human-written text. During [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) fine-tuning, the model learns to predict the next token in structured, schema-conforming JSON. The architecture is identical; only the training data and target format differ.

### Training for Tool Use

Function calling capability is typically instilled through supervised fine-tuning on specialized datasets. These datasets consist of conversation traces where:

1.  The system prompt includes available function definitions
2.  User queries require tool invocation to answer correctly
3.  Assistant responses alternate between function call objects and final answers based on observation results

The training objective remains next-token prediction, but the target distribution now includes structured JSON snippets interleaved with natural language. This multimodal output space requires the model to learn special transition dynamics: when to switch from natural language to JSON, how to maintain syntactic validity across token boundaries, and when to terminate a function call versus continuing with explanation.

Models learn to recognize patterns such as:

-   Queries containing temporal references ("current weather," "latest stock price") likely require tool calls because the model's training data has a cutoff date and cannot provide real-time information.
-   Mathematical precision requirements often necessitate calculator tools, especially for complex expressions where the model might otherwise hallucinate incorrect calculations.
-   Questions about private or real-time data require retrieval functions, as these fall outside the model's parametric knowledge.

The training process also instills tool awareness: the ability to recognize when a query falls within the domain of available tools versus when it requires general knowledge. A poorly trained model might call a weather API for "What's the capital of France?", while a well-calibrated model recognizes this as factual knowledge requiring no external tool.

One subtle aspect of this training is teaching the model to be appropriately uncertain. When a query is ambiguous, the right behavior is often to ask for clarification rather than guess. "What's the weather?" lacks a location, so a well-trained model should respond with a clarifying question rather than inventing a location. Achieving this calibration requires training examples that explicitly demonstrate the clarification behavior, not just tool-use examples.

### Generation Formats

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

### Parallel Function Calling

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

Parallel calling significantly reduces latency in [multi-tool](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) scenarios but requires the execution framework to handle concurrent API calls and aggregate results. The framework must track which calls belong to which logical operation, handle partial failures (where one call succeeds and another fails), and manage race conditions in stateful operations. This pattern essentially transforms the linear [request-response](https://mbrenndoerfer.com/writing/communication-between-agents) cycle into a graph execution problem, where the model defines the nodes ( [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents)) and the system manages the edges (dependencies and data flow).

Out\[5\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/parallel-vs-sequential-latency.png

Latency comparison between parallel and sequential execution strategies for multiple independent function calls. Sequential latency grows linearly at 1.2 seconds per call, while parallel latency grows much more slowly due to concurrent execution. For five independent calls, parallelization reduces total latency from 6.0 seconds to under 2.0 seconds.

## Function Output Handling

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) establishes a [request-response](https://mbrenndoerfer.com/writing/communication-between-agents) cycle between the language model and [external tools](https://mbrenndoerfer.com/writing/why-ai-agents-need-tools). Once a function executes, its return value must be formatted and presented back to the model to enable the final response generation. This cycle creates a [feedback loop](https://mbrenndoerfer.com/writing/continuous-feedback-and-improvement-ai-agents) where the model can react to real-world data, correcting misconceptions or filling knowledge gaps dynamically.

The design of this feedback loop is more subtle than it first appears. The model must not only receive the function output but interpret it in the context of the original query. A raw JSON response from a weather API contains temperature, humidity, wind speed, and conditions. The model must select which of these fields are relevant to your question, convert units if requested, and frame the information in natural language that answers the original intent. This interpretation step requires the model to maintain awareness of the original query throughout the tool-execution cycle.

### The Observation Pattern

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

### Context Window Implications

Each function call and observation consumes tokens in the [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp). In scenarios involving multiple tool invocations or verbose API responses, this can quickly exhaust available context length. A complex database query might return hundreds of rows, each consuming dozens of tokens when serialized as JSON. As we explored in [Context Length Challenges](https://mbrenndoerfer.com/writing/context-length-challenges-transformers), long tool outputs may need summarization or selective filtering before being presented to the model.

Strategies for managing context in tool-heavy conversations include:

-   **Result summarization**: Using smaller models or heuristics to compress verbose API outputs into key points before presenting them to the main model.
-   **Pagination**: Breaking large result sets into chunks and allowing the model to request specific pages or aggregates.
-   **Selective retention**: Keeping only the most recent tool results in context while archiving older ones to a separate memory store.

Furthermore, the recursive nature of [tool use](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents), where observations trigger additional function calls, creates deep conversation histories. A complex research task might involve ten or more tool calls, each adding multiple messages to the thread. Efficient management of this history, potentially through [KV Cache Compression](https://mbrenndoerfer.com/writing/kv-cache-compression-eviction-quantization-h2o-algorithm) or selective context pruning, becomes essential for production deployments. Some systems implement conversation summarization at fixed intervals, condensing older tool interactions into high-level summaries that preserve essential information while freeing up tokens for new operations.

The token cost of function calling is frequently underestimated. A system prompt listing ten detailed tool schemas might consume 2,000 tokens before a single word of your query is processed. This front-loading of context means that function calling applications effectively have shorter usable context windows than their nominal context limit suggests. Designing compact but informative schemas, and using retrieval-based schema selection to present only relevant tools, helps recover this overhead.

Out\[6\]:

Visualization

https://cnassets.uk/notebooks/2_function_calling_files/context-window-growth.png

Cumulative token consumption across function calling iterations, illustrating how tool calls and observations accumulate in the context window. Starting from an initial system and user message of around 920 tokens, each tool call and observation cycle adds approximately 600 tokens. A dashed red line marks a typical 4096-token context limit, showing how multi-step tool use can rapidly approach capacity.

### Error Handling

Not all [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) succeed. Networks fail, APIs return errors, and arguments may be invalid. The [error handling](https://mbrenndoerfer.com/writing/plan-and-execute-ai-agents) strategy significantly impacts robustness and user experience. A brittle system that crashes on API timeouts provides little value, while a resilient system that gracefully degrades maintains utility even under adverse conditions.

Common error handling patterns include:

-   **Retry with correction**: Present the error to the model and allow it to generate a corrected call. For example, if a weather API returns "Location not found" for "Bostn, MA", the model might infer the typo and retry with "Boston, MA". This requires the error message to be descriptive enough to enable diagnostic reasoning.
-   **Fallback to knowledge**: If the tool fails, the model falls back to its parametric knowledge with appropriate uncertainty qualifiers. For instance, "I was unable to check the live weather, but based on my training data, Boston in January is typically cold, often below freezing." This maintains utility while signaling uncertainty.
-   **Escalation to you**: For critical failures, the system asks you for clarification or manual input. This is appropriate when the model lacks sufficient information to recover autonomously, such as when required authentication tokens expire.

Error messages should be structured to help the model diagnose issues. Rather than generic "Error 500" messages, provide specific feedback: "Invalid location format: expected 'City, State' but received 'Boston'". This specificity enables the model to adjust its approach, perhaps by asking you for clarification or by reformatting the parameter according to the API's expectations. The error format should mirror the success format (JSON with consistent fields) to ensure the model can parse it reliably.

There is also a category of logical errors that are harder to detect: cases where the function executes successfully but returns data that is semantically incorrect for the query. If your query asks about tomorrow's weather and the API returns today's weather, the function call technically succeeded. The model must reason about whether the returned data actually answers the question. Designing observation formats that include metadata about the query parameters (such as the date range returned by a weather API) helps the model perform this validation.

## Worked Example: Multi-Step Calculation

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

## Code Implementation: Building a Function Calling System

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

## Key Parameters

The key parameters governing a [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) system's behavior are:

-   **max\_iterations**: Maximum number of tool invocation cycles allowed before terminating. This prevents infinite loops in cases where the model repeatedly invokes tools without reaching a final answer. Setting this parameter requires balancing completeness against resource constraints. A value of 3 to 5 is typically sufficient for most use cases, while complex research tasks might require 10 or more. Exceeding this limit usually indicates either a poorly calibrated model stuck in a loop or a query that genuinely requires more steps than the system allows.
-   **tool\_call\_id**: Unique identifier linking each observation back to its corresponding function call, essential for handling parallel function calls correctly. In production systems, these IDs must be globally unique and persistent across the conversation lifecycle to ensure proper attribution of results. UUIDs or timestamped identifiers are commonly used.
-   **required**: List of parameter names in the function schema that must be provided for the call to be valid, ensuring critical arguments are not omitted. This list acts as a contract enforcement mechanism. When the model attempts to call a function without a required parameter, the system should reject the call and either prompt the model for the missing information or return a validation error that the model can use to correct its approach.

## Function Calling Fine-Tuning

While general-purpose models like [GPT-4](https://mbrenndoerfer.com/writing/gpt4-multimodal-language-models-reach-human-level-performance) come with robust [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) capabilities, open-source models often require fine-tuning to reliably emit structured tool calls. This process involves curating datasets of tool-use conversations and optimizing the model for schema adherence. Fine-tuning transforms a base model from a general text generator into a specialized tool-calling agent.

The need for fine-tuning is not merely about format compliance. A base model might generate syntactically valid JSON that is semantically wrong: it might call the right function but with hallucinated parameter values, or invoke a tool when the answer is already in its parametric knowledge. Fine-tuning teaches the model not just the output format, but the judgment of when and how to invoke tools correctly. This judgment is fundamentally a classification problem: for every query, the model must decide among (a) answer directly, (b) request clarification, (c) call one or more tools.

### Dataset Construction

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

### Training Objectives

The fine-tuning process uses standard supervised learning with [cross-entropy loss](https://mbrenndoerfer.com/writing/cross-entropy-loss-language-models-information-theory), but with attention to special tokens that demarcate tool boundaries. As discussed in [Instruction Tuning Training](https://mbrenndoerfer.com/writing/instruction-tuning-training-data-mixing-loss-masking), the learning rate is typically lower than pre-training to preserve general capabilities while adapting to the specific tool-calling format. The model must learn not just the format, but the semantics of when to transition between natural language and structured calls.

Key hyperparameters for [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) fine-tuning include:

-   **Learning rate**: Often 1e-5 to 2e-5, smaller than general fine-tuning to maintain stability. Higher rates might cause [catastrophic forgetting](https://mbrenndoerfer.com/writing/catastrophic-forgetting-fine-tuning-mitigation) of conversational abilities or [overfitting](https://mbrenndoerfer.com/writing/statistical-modeling-overfitting-underfitting-bias-variance-tradeoff) to specific tool formats.
-   **Sequence length**: Must accommodate long tool descriptions and multi-turn conversations. Function schemas can be verbose, especially with nested objects, requiring context windows of 4k tokens or more.
-   **Masking strategy**: Typically, only assistant messages (including tool calls) are used for loss computation, while user and system prompts are masked. This focuses the model's learning on generating appropriate responses rather than predicting your inputs.
-   **Data mixture**: Combining tool-use data with general [instruction data](https://mbrenndoerfer.com/writing/instruction-data-creation-building-training-datasets) prevents catastrophic forgetting of conversational abilities, as explored in [Catastrophic Forgetting](https://mbrenndoerfer.com/writing/catastrophic-forgetting-fine-tuning-mitigation). A typical mixture might be 70% tool-use data and 30% general [instruction following](https://mbrenndoerfer.com/writing/instruction-following-llm-tuning-fundamentals) data, though this varies by base model and target application.

The masking strategy deserves a closer look. When computing the [cross-entropy loss](https://mbrenndoerfer.com/writing/cross-entropy-loss-language-models-information-theory), we want the model to learn to generate correct tool calls and final responses. We do not want it to expend capacity predicting the user's messages or the system prompt. By masking these tokens out of the loss computation (setting their weights to zero), we ensure the gradient signal comes entirely from the model's own outputs. This is the same technique used in [instruction tuning](https://mbrenndoerfer.com/writing/instruction-tuning-adapting-language-models-to-follow-explicit-instructions) more broadly and is crucial for efficient learning.

The training process must also account for the observation phase. Some implementations include simulated tool results in the training data, while others train only on the call generation phase and handle observations as context during inference. The former approach creates a more holistic understanding of the tool-use cycle but requires a dataset of realistic tool outputs. Including observations in training is generally preferred because it teaches the model how to synthesize tool results into natural language responses, which is the final step that makes [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) useful to users.

### Format-Specific Considerations

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

### Evaluation Metrics

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

## Structured Output Generation and Schema Enforcement

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) and [structured output](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) generation are closely related but distinct capabilities. Function calling specifically refers to the model emitting a call to a named function with arguments. Structured output generation is the broader capability of emitting text that conforms to any specified schema, which includes function calls but also encompasses JSON objects, XML documents, CSV records, and other structured formats.

Understanding this relationship matters because the same techniques that enable function calling also underlie many other LLM capabilities. When a model generates a structured resume from a job description, or populates a database template from unstructured text, or extracts named entities in a specified JSON format, it is using the same structural generation machinery as function calling, just pointed at different schemas.

### Token-Level Schema Enforcement

At the token generation level, two broad approaches enforce schema conformance. The first is training-time enforcement, where the fine-tuning data exclusively contains valid schema-conforming examples, and the model learns to generate valid structures probabilistically. The second is inference-time enforcement, where the decoder's [sampling distribution](https://mbrenndoerfer.com/writing/central-limit-theorem-foundation-statistical-inference) is dynamically constrained to only allow tokens that maintain schema validity at each step.

Training-time enforcement is simpler to implement but produces stochastic compliance: the model usually generates valid structures but occasionally produces invalid ones, especially on unusual inputs or when under-specified schemas leave ambiguity. The failure rate depends on the quality and diversity of training data and typically improves with more training.

Inference-time enforcement, as covered in [Constrained Decoding](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output), guarantees syntactic validity by construction. The system maintains a parser state that tracks which tokens are currently valid according to the schema grammar, and sets the [logit](https://mbrenndoerfer.com/writing/logistic-regression-complete-guide-mathematical-foundations-python-implementation) of all invalid tokens to −∞-\\infty−∞ before sampling. This approach is computationally more expensive but eliminates parsing errors entirely. For production systems where unparseable outputs represent hard failures, the overhead is generally worth it.

The trade-off between these approaches also affects the model's reasoning quality. Inference-time constraints can sometimes prevent the model from generating the contextually best argument value if that value happens to violate a syntactic constraint mid-generation. Training-time enforcement, while noisier, allows the model more freedom to express its full linguistic capability and may produce more semantically accurate outputs even if some are syntactically invalid. Hybrid approaches train the model for high baseline compliance and apply selective inference-time constraints only for the most critical schema fields (like function names and required parameters).

### Structured Output Beyond Function Calling

The same principles that govern [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) apply when you need LLMs to produce structured data in other contexts. Consider information extraction: given a long article about a company's earnings report, you want to extract a structured record with fields for revenue, profit, year-over-year growth, and key executive commentary. You define a JSON schema for the record, provide it to the model alongside the article, and prompt the model to populate the schema.

The schema serves the same roles it does in function calling: it constrains the output space, provides semantic guidance about expected field types, and gives the model a structured template to fill. The difference is that instead of generating a function invocation, the model is generating a data record. The underlying mechanism is identical, which is why models with strong function calling capabilities tend to excel at structured extraction tasks as well.

This generalization suggests a productive mental model: think of JSON schemas not as function call specifications but as output templates that guide what the model generates. Any time you want the model to produce structured information, defining a schema is likely to improve [reliability](https://mbrenndoerfer.com/writing/monitoring-reliability-ai-agents) and consistency. The model has been trained to treat schemas as authoritative specifications of its expected output format.

## Limitations and Impact

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) represents a significant advance in language model capabilities, yet it introduces specific constraints and failure modes that practitioners must navigate. Understanding these limitations is crucial for deploying robust systems and setting appropriate user expectations.

### Schema Rigidity and Generalization

Models trained on function calling often struggle with schema variations not seen during fine-tuning. If a training set always presents weather queries with "city, state" format, the model may fail when encountering "city, country" or coordinate-based locations. This brittleness contrasts with the flexibility of natural language, requiring careful prompt engineering or few-shot examples to handle edge cases. The model essentially overfits to the specific parameter patterns in its training data, lacking the compositional generalization that humans exhibit when encountering novel but semantically equivalent inputs.

Furthermore, models may exhibit parameter hallucination when facing ambiguous queries. Given "What's the weather like?" without a specified location, a poorly calibrated model might guess a location rather than ask for clarification. This necessitates robust validation layers that check required parameters before execution and implement retry loops with explicit error feedback. Some systems implement "guardian" models that pre-screen [function calls](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) for hallucinated parameters, adding a layer of safety at the cost of additional latency.

The hallucination problem is particularly challenging for string parameters that are not constrained by enums or patterns. A model generating a `customer_id` parameter has no schema-level guardrail preventing it from inventing a plausible-looking but non-existent ID. The only defense is application-layer validation that checks whether the generated ID actually exists in the system before executing the function. This validation step adds latency but prevents silent errors where the model's output looks valid but refers to non-existent entities.

### Latency and Cost Considerations

The function calling loop introduces multiple round-trips to the language model: initial call generation, observation injection, and final response generation. Each trip incurs latency and [API costs](https://mbrenndoerfer.com/writing/managing-reducing-ai-agent-costs-optimization-strategies). In high-throughput applications, these costs compound rapidly. A query requiring three tool calls might take three times as long and cost three times as much as a single-turn response.

Parallel [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) mitigates some latency concerns by batching independent operations, but sequential dependencies (where one tool's output is needed for the next call) require serial execution. Planning strategies, which we'll explore in the [ReAct Pattern](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents) chapter, help optimize these dependency chains by allowing the model to reason about tool dependencies before execution. Caching frequent tool results and using smaller, faster models for simple [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents) can also reduce costs in production environments.

The cost model for function calling applications also includes the token overhead of schema definitions in the system prompt. For applications with dozens of available tools, the system prompt alone might cost hundreds of tokens per request. At scale, these schema tokens represent a substantial fraction of total [API costs](https://mbrenndoerfer.com/writing/managing-reducing-ai-agent-costs-optimization-strategies). Techniques like schema compression (removing verbose descriptions while preserving essential type information), retrieval-based schema selection (presenting only the most relevant tools per query), and schema caching (reusing parsed schema representations across requests) help manage this overhead.

### Security Implications

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) creates a direct channel between unconstrained natural language and executable code. This presents significant security risks that must be addressed through defense in depth:

-   **Prompt injection**: Malicious users might craft queries that invoke tools with dangerous arguments. This is analogous to SQL injection in web applications, where user input is executed as code.
-   **Tool confusion**: Attackers may describe tools in ways that trick the model into invoking privileged functions with attacker-controlled parameters. Renaming a sensitive function to resemble a benign one might fool the model into using it inappropriately.
-   **Information leakage**: Tool outputs might contain sensitive data that gets exposed in subsequent generations. A database query tool might return private customer information that the model then reveals to unauthorized parties.

Mitigation strategies include strict input validation against schemas, allowlisting permitted operations, executing tools in sandboxed environments, and implementing [human-in-the-loop](https://mbrenndoerfer.com/writing/ethical-guidelines-human-oversight-ai-agents) confirmation for destructive operations. The principle of [least privilege](https://mbrenndoerfer.com/writing/action-restrictions-and-permissions-ai-agents) should govern tool design: functions should expose minimal capabilities necessary for their specific purpose. Additionally, [output filtering](https://mbrenndoerfer.com/writing/content-safety-and-moderation-ai-agents) can prevent sensitive data from being returned to you, and [rate limiting](https://mbrenndoerfer.com/writing/environment-boundaries-constraints-ai-agents) can prevent abuse of expensive or sensitive tools.

The prompt injection threat is particularly insidious because it can be embedded in tool outputs, not just user inputs. If a web search tool returns a result containing text that resembles instructions, the model might treat this as a legitimate system command. Sanitizing tool outputs to remove instruction-like patterns and maintaining clear separation between data and instructions in the conversation format are important defenses.

### The Path to Agency

Despite these limitations, [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) transforms language models from passive responders into active agents capable of affecting the world. By providing a structured interface to external capabilities, it enables the construction of complex workflows where models plan, execute, observe, and adapt. This capability represents the foundation of autonomous [agent architectures](https://mbrenndoerfer.com/writing/agent-architectures-loop-state-planning-termination), where the LLM serves as the reasoning engine coordinating multiple tools to achieve high-level goals.

This capability unlocks applications ranging from automated research assistants that query databases and calculate statistics to customer service bots that modify orders and check shipping status. As we move toward more sophisticated agent architectures in subsequent chapters, function calling serves as the basic building block, the "motor cortex" that translates high-level intentions into concrete actions. The [ReAct Pattern](https://mbrenndoerfer.com/writing/react-pattern-llm-reasoning-action-agents) builds directly on this foundation, adding explicit reasoning steps between observations and actions to create more robust, traceable agent behaviors. Understanding [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) is therefore essential for anyone building the next generation of AI applications that interact with the real world.

## Summary

[Function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) enables language models to bridge the gap between natural language understanding and actionable computation. By defining tool schemas in JSON format, models learn to emit structured function calls with appropriate parameters, execute external code safely, and synthesize results into coherent responses. This capability transforms static text generators into dynamic agents capable of retrieving information, performing calculations, and interacting with external systems.

Key takeaways include:

-   **Schema definition** uses JSON Schema to specify function interfaces, parameter types, and constraints, providing the model with the metadata necessary to generate valid calls. Well-designed schemas act as both technical specifications and semantic guides, helping the model understand when and how to use each tool.
-   **Call generation** leverages supervised fine-tuning on tool-use corpora, teaching models to recognize when external data is required and how to format requests appropriately. This training instills tool awareness and the ability to map natural language queries to structured parameters.
-   **Execution loops** follow an observe-act pattern where function results are injected back into the [context window](https://mbrenndoerfer.com/writing/co-occurrence-matrices-distributional-semantics-nlp) as observations, enabling multi-step reasoning. This cycle allows models to react to real-world data and correct course based on external feedback.
-   **Fine-tuning** requires carefully curated conversation datasets that demonstrate proper [tool selection](https://mbrenndoerfer.com/writing/tool-selection-llm-agents-routing-strategies), [parameter extraction](https://mbrenndoerfer.com/writing/designing-simple-tool-interfaces-ai-agents), and natural language synthesis from structured data. Success requires attention to format consistency, diverse examples, and proper [evaluation metrics](https://mbrenndoerfer.com/writing/benchmark-saturation-ai-evaluation-metrics).
-   **Practical deployment** demands attention to [error handling](https://mbrenndoerfer.com/writing/plan-and-execute-ai-agents), security validation, [latency optimization](https://mbrenndoerfer.com/writing/speeding-up-ai-agents-performance-optimization), and context window management. Production systems must guard against injection attacks, handle API failures gracefully, and manage the computational costs of multi-turn interactions.

As the interface between language models and the digital world, [function calling](https://mbrenndoerfer.com/writing/function-calling-tool-use-practical-ai-agents) represents the key primitive upon which [autonomous agents](https://mbrenndoerfer.com/writing/agentic-ai-systems-autonomous-agents-reasoning-planning-tool-use) are constructed. Mastering its mechanics, both the mathematical foundations of [structured generation](https://mbrenndoerfer.com/writing/constrained-decoding-structured-llm-output) and the engineering challenges of safe execution, prepares practitioners to build systems that move beyond text generation into purposeful action. The skills developed here, designing schemas, managing execution loops, and handling edge cases, form the bedrock of modern AI application development.

## Quiz

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

<research_source type="scraped_from_research" phase="exploration" file="function-calling-using-llms.md">
<details>
<summary>Function calling using LLMs</summary>

Phase: [EXPLORATION]

**Source URL:** <https://martinfowler.com/articles/function-call-LLM.html>

# Function calling using LLMs

Building AI Agents that interact with the external world.

_While LLMs excel at generating cogent text based on their training_
_data, they may also need to interact with external systems. Function_
_calling allows them to construct such calls. The LLM does not execute these_
_calls directly, instead it creates a data structure that describes the call,_
_passing that to a separate program for execution and further processing. The_
_LLM's prompt includes details about possible function calls and when they_
_should be used._

06 May 2025

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

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-tool-chaining-fails-in-production-llm-agents-and-how-to-.md">
<details>
<summary>How Tool Chaining Fails in Production LLM Agents and How to Fix It</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://futureagi.substack.com/p/how-tool-chaining-fails-in-production>

# How Tool Chaining Fails in Production LLM Agents and How to Fix It

### Why Multi-Tool Orchestration Breaks in Production and the Patterns That Make It Reliable

[https://substackcdn.com/image/fetch/$s_!nJhF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6b1b4fc-8c10-4429-89a7-d603d3ae0b70_2566x1642.heic](https://substackcdn.com/image/fetch/$s_!nJhF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6b1b4fc-8c10-4429-89a7-d603d3ae0b70_2566x1642.heic)

Tool chaining is the backbone of every useful agentic AI system. When an LLM agent completes a multi-step task, it calls one tool, takes the output, and feeds it into the next tool in sequence. This is multi-tool orchestration at its core. It works in demos. It consistently breaks in production.

The pattern is familiar to anyone building LLM-powered applications. Your agent chains three or four tool calls together. The first call returns slightly malformed output. The second tool accepts it but misinterprets a field. By the third call, the entire chain has gone off the rails. This is the cascading failure problem, and it remains the primary bottleneck to agent reliability in 2026. [Research from Zhu et al. (2025)](https://arxiv.org/pdf/2509.25370?) confirms that error propagation is the single biggest barrier to building dependable LLM agents.

This guide breaks down why tool chaining fails, how context preservation collapses across chained calls, what evaluation frameworks catch failures before they reach users, and practical patterns using LangGraph and LangChain.

## What Is Tool Chaining and Why It Matters for Agentic AI

Tool chaining is the sequential execution of multiple tool calls by an LLM agent, where each tool’s output becomes the input for the next tool in the sequence. An agent receives a user query, decides it needs data from an API, processes that data with a second tool, and generates a final response using the combined results.

This differs from a single tool call in important ways. A single call is straightforward: the LLM calls a function, gets a result, and responds. Chaining creates dependencies. The agent must determine the right order of operations, track intermediate state, and handle partial failures while staying focused on the original goal. In multi-agent systems, the complexity increases further because one agent might call a tool, hand the result to a second agent, which runs its own tool sequence before returning. The orchestration overhead compounds quickly, and potential failure points grow with it.

Consider a practical example. A user asks an agent to find earnings data, compare it to competitors, and generate a summary. If the first call returns revenue in the wrong currency, the comparison runs but produces misleading figures. The summary then confidently presents wrong data. No error was thrown. That is the core danger of tool chaining without validation and observability.

## The Core Challenges of Tool Chaining in Production

### Context Preservation Across Tool Calls

Context preservation is the ability to maintain relevant information as data flows from one tool call to the next. LLMs operate within a finite context window, and every tool call adds tokens to that window through function parameters, response payloads, and the agent’s reasoning about what to do next. In long chains, critical context from early steps can be pushed out of the window or diluted by intermediate results.

This problem is well documented. Research shows that LLMs lose performance on information buried in the middle of long contexts, even with large context windows. When an agent forgets a user constraint from step 1 by the time it reaches step 5, the output may be technically valid but factually wrong. The user asked for revenue in USD, but the agent lost that detail three tool calls ago.

There are practical fixes. Use structured state objects instead of raw text to pass data between tool calls, keeping the payload compact and parseable. Summarize intermediate results before passing them forward by stripping out metadata the next tool does not need. Use frameworks like LangGraph that provide explicit state management across graph nodes, keeping context durable and inspectable.

### Cascading Failures and Error Propagation

Cascading failures are the biggest production risk in tool chaining. When one tool in the chain produces an incorrect or partial result, that error flows downstream and compounds at every subsequent step. Unlike traditional software where errors throw exceptions, LLM tool chains often fail silently because the agent treats bad output as valid input and moves on.

A 2025 study published on [OpenReview](https://openreview.net/forum?id=PFR4E858W) analyzed failed LLM agent trajectories and found that error propagation was the most common failure pattern, with memory and reflection errors being the most frequent cascade sources. Once these cascades begin, they are extremely difficult to reverse mid-chain.

In [multi-agent systems](https://arxiv.org/abs/2503.13657), cascading failures are amplified. The Gradient Institute found that transitive trust chains between agents mean a single wrong output propagates through the entire chain without verification. OWASP ASI08 specifically identifies cascading failures as a top security risk in agentic AI.

### Context Window Saturation

Every tool call consumes context window tokens. A chain of five calls can easily use 40 to 60 percent of available tokens before the agent generates its final response.

## Tool Chaining Failure Modes: A Developer Reference

Understanding common failure modes helps you build defenses early.

**Silent data corruption** occurs when a tool returns the wrong format and the agent passes it forward undetected. Add schema validation using JSON Schema or Pydantic on every tool output.

**Context loss** happens when key data from early calls gets pushed out of the context window. Use explicit state management and carry forward only essential fields.

**Cascading hallucination** is when the agent fills missing data with hallucinated values after a tool returns incomplete results. Implement strict null checks and instruct the agent to stop and report missing data.

**Tool misuse** occurs when the agent calls the wrong tool or uses incorrect parameters. Write precise tool descriptions with parameter examples and constraints.

**Timeout cascade** is triggered when one slow tool causes subsequent calls to timeout. Set per-tool timeouts and implement circuit breakers to isolate slow tools.

**Error swallowing** happens when API errors are caught but not surfaced, so the agent proceeds with empty data. Return explicit error objects and train the agent to handle error responses differently.

## Frameworks for Multi-Tool Orchestration

The right framework reduces the difficulty of building reliable tool chains. Here is how the leading options compare for production multi-tool orchestration in 2026.

**[LangGraph](https://www.langchain.com/langgraph)** is best suited for stateful, branching workflows with conditional routing. It offers graph-based state machine execution with durable checkpoints and deep tracing via LangSmith. Every node represents either a tool call or a decision point, and edges define transitions between steps. This makes it straightforward to add retry logic, fallback paths, and human-in-the-loop checkpoints. Its durable execution feature means that if a chain breaks at step 4 out of 7, it can resume from that exact point instead of restarting from scratch.

**[LangChain](https://www.langchain.com/)** remains the most popular starting point for LLM application development. Its LCEL pipe syntax makes it quick to compose linear tool chains, with tracing through LangSmith and Langfuse. For production workloads with branching logic or parallel tool calls, most teams migrate to LangGraph for additional control.

**AutoGen** is designed for multi-agent conversation collaboration using message-passing with built-in function call semantics. It offers moderate observability and needs external tooling for production traces.

**CrewAI** handles role-based multi-agent task execution with task delegation and tool assignment per role. It provides basic logging and tends toward longer deliberation before tool calls.

## Distributed Tracing and Observability for Tool Chains

You cannot fix what you cannot see. Observability is critical for tool chaining because failures are often silent. A tool chain that produces a wrong answer without throwing errors looks fine in your logs unless you have distributed tracing capturing every step.

Every tool chain should trace the following: the exact input and output of each tool call for failure replay, latency per step to catch timeout cascades, token consumption to identify context window saturation, and the agent’s reasoning between calls to surface logic errors.

Tools like LangSmith, Langfuse, and Future AGI provide native tracing for LangGraph and LangChain workflows. [Future AGI’s traceAI SDK](https://github.com/future-agi/traceAI?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) integrates with OpenTelemetry and provides built-in evaluation metrics for completeness, groundedness, and function calling accuracy.

## Evaluation Frameworks for Tool Chaining

Tracing tells you what happened. Evaluation frameworks tell you whether it was correct. For tool chains, evaluation must cover tool selection accuracy, parameter correctness, chain completion rate, output faithfulness, and error recovery rate.

Running evaluations at scale requires automation. Platforms like Future AGI attach [evaluation metrics](https://app.futureagi.com/dashboard/evaluations?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) directly to traces, scoring every execution and creating a continuous feedback loop.

## Building Reliable Tool Chains for Production

Based on real-world production deployments and current research, these patterns consistently improve tool chaining reliability.

**Validate at every boundary.** Add input and output validation between every tool call using Pydantic or JSON Schema. Explicit validation catches errors at the source before they propagate.

**Use plan-then-execute architecture.** Research from Scale AI shows that having the LLM formulate a structured plan first and then running it through a deterministic executor reduces tool chaining errors significantly. This separates reasoning from execution.

**Implement circuit breakers.** If a tool fails or returns unexpected results more than N times, break the circuit and return a graceful failure. This prevents one broken tool from taking down the entire workflow.

**Keep chains short.** Longer chains mean more failure opportunities and more context consumption. If your chain needs more than five or six sequential calls, restructure into sub-chains or parallel branches.

**Test with adversarial inputs.** Standard test cases will pass. Production traffic will not be standard. Test with empty responses, large payloads, unexpected types, and ambiguous queries.

**Trace everything from day one.** Instrument tool chains with distributed tracing from the first deployment. When something breaks, traces are the difference between hours of debugging and a quick fix.

## Conclusion

Tool chaining separates demo-ready agents from production-ready ones. The gap comes down to how well you handle cascading failures, preserve context across calls, and evaluate every execution against clear quality criteria. LangGraph provides the control structure, LangChain provides the integration layer, and evaluation platforms close the feedback loop.

Teams that ship reliable agentic AI treat multi-tool orchestration as a first-class engineering problem. Validate at every boundary, trace every execution, evaluate continuously, and keep chains short.

## Frequently Asked Questions

**What is tool chaining in LLM agents?**

Tool chaining is the sequential execution of multiple tool calls by an LLM agent, where each tool’s output feeds into the next step. It allows agentic AI systems to break down multi-step tasks and complete them by combining data from different sources and processing stages.

**Why do cascading failures happen in multi-tool orchestration?**

Cascading failures occur because LLM agents treat malformed tool outputs as valid inputs. The agent does not throw exceptions for bad data. Instead, it silently passes errors forward, compounding them at each subsequent step until the final output is completely wrong.

**How does context preservation affect tool chaining reliability?**

Every tool call consumes context window tokens, and critical information from early steps can get diluted or pushed out entirely. When the agent loses a user constraint or data point from earlier calls, it produces outputs that seem valid but miss key requirements.

**What evaluation frameworks help test tool chains with Future AGI?**

[Future AGI](https://docs.futureagi.com/home?utm_source=toolchaining&utm_medium=Blog&utm_campaign=blog_page) provides automated evaluation metrics that attach directly to distributed traces. These metrics measure tool selection accuracy, parameter correctness, output faithfulness, and chain completion rate, enabling continuous automated assessment of every tool chain execution at scale.

**How does LangGraph handle tool chaining differently from LangChain?**

LangGraph models tool chains as graph-based state machines with explicit nodes, edges, and conditional routing. This gives developers fine-grained control over execution flow, retry logic, and checkpoints. LangChain uses a simpler pipe-based syntax better suited for linear chains.

**What role does distributed tracing play in debugging tool chain failures?**

Distributed tracing records the inputs, outputs, latency, and token usage for every tool call in the chain. Because tool chain failures can be easy to miss, traces help developers identify the exact step where an error originates and track how it ripples through everything that follows.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="stop-pasting-screenshots-how-ai-engineers-document-systems-w.md">
<details>
<summary>Stop Pasting Screenshots: How AI Engineers Document Systems with Mermaid | Ranjan Kumar</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://ranjankumar.in/stop-pasting-screenshots-how-ai-engineers-document-systems-with-mermaid>

# Stop Pasting Screenshots: How AI Engineers Document Systems with Mermaid | Ranjan Kumar

## Introduction

Six months into your LLM project, someone asks: _"How does our RAG pipeline actually work?"_ You dig through Slack. Check Notion. Find three different architecture diagrams—each contradicting the others. None match what's actually deployed.

Sound familiar? This is the _documentation debt_ that kills AI projects. Not because teams don't document, but because _traditional diagramming tools can't keep up with how fast AI systems evolve_.

I've watched this play out dozens of times. A team spends hours crafting beautiful architecture diagrams in Lucidchart or draw.io. Two sprints later, they've added a semantic router, switched vector databases, and introduced a reflection loop. The diagrams? Still showing the old design, locked in someone's Google Drive. The fix isn't better discipline. It's better tools.

## The Real Cost of Screenshot-Driven Documentation

When I started building production AI systems, I followed the standard playbook: design in Figma, export to PNG, paste into docs. The results were predictably bad.

Here's what actually happens with static diagrams:

**They diverge immediately.** You add a cross-encoder reranking stage to your RAG pipeline. The diagram still shows simple vector similarity. Nobody updates it because that requires opening another tool, finding the original file, making edits, re-exporting, and re-uploading.

**They're invisible to code review.** Your agent architecture changes during PR review—maybe you split one tool into two, or modified the state transition logic. The code diff shows this. Your diagram? Still wrong, and nobody notices because it's not in the diff.

**They break the development flow.** Good documentation happens in context. When you're deep in implementing a multi-agent workflow, the last thing you want is to switch to a visual editor, recreate your mental model, and then switch back.

I hit this wall hard while writing production-ready agentic systems. The architecture was evolving daily. Keeping diagrams synchronized was either impossible or consumed hours I needed for actual engineering.

## Enter Diagram-as-Code

The solution isn't working harder at diagram maintenance. It's treating diagrams like we treat code: version-controlled, reviewable, and living alongside the implementation.

This is where **_Mermaid_** becomes essential infrastructure.

Instead of drawing boxes and arrows, you describe your system's structure in plain text. The rendering happens automatically, everywhere your documentation lives—GitHub READMEs, technical blogs, internal wikis, even Jupyter notebooks.

Here's a simple example. This code:

```
graph LR    A[User Query] --> B[Semantic Router]    B -->|factual| C[Vector DB]    B -->|conversational| D[LLM Direct]    C --> E[Reranker]    E --> F[Context Builder]    F --> G[LLM Generation]    D --> G
```

https://ranjankumar.in/images/2025/12/how-queries-route-through-different-paths-in-your-rag-system.png

Renders as a clean flowchart showing how queries route through different paths in your RAG system. No exports, no image hosting, no version drift.

The real power emerges when this diagram lives in your repository's `docs/` folder. Now when someone modifies the routing logic, they update both code and diagram in the same commit. Code review catches documentation drift before it happens.

## Five Essential Mermaid Patterns for AI Engineers

Let me show you the diagram patterns I use constantly. These aren't toy examples—they're templates I've refined while building production systems that handle millions of queries.

### 1\. LLM Agent Architecture with Tool Orchestration

Most agent tutorials show you a simple loop. Production agents are messier. They need memory systems, error handling, and complex tool orchestration.

```
flowchart TD    Start([User Input]) --> Router{Intent Router}    Router -->|search needed| ToolSelect[Tool Selection]    Router -->|direct answer| Memory[Check Memory]        ToolSelect --> Search[Web Search]    ToolSelect --> DB[Database Query]    ToolSelect --> Calc[Calculator]        Search --> Validate{Result Valid?}    DB --> Validate    Calc --> Validate        Validate -->|yes| Memory    Validate -->|no| Retry{Retry Count}    Retry -->|< 3| ToolSelect    Retry -->|>= 3| Fallback[Fallback Response]        Memory --> Context[Build Context]    Fallback --> Context    Context --> LLM[LLM Generation]    LLM --> Update[Update Memory]    Update --> End([Response])
```

https://ranjankumar.in/images/2025/12/llm-agent-architecture-with-tool-orchestration.png

This pattern captures what actually happens: tool failures, retry logic, and memory updates. When you're debugging why your agent keeps hitting API limits, having this documented makes the problem obvious.

### 2\. Multi-Stage RAG Pipeline

Basic RAG is "embed query, search vectors, generate response." Production RAG has stages for query rewriting, hybrid search, reranking, and context filtering.

```
graph TB    Query[User Query] --> Rewrite[Query Rewriter]    Rewrite --> Parallel{Parallel Search}        Parallel --> Dense[Dense Retrieval<br/>Vector DB]    Parallel --> Sparse[Sparse Retrieval<br/>BM25/Keyword]        Dense --> Fusion[Reciprocal Rank Fusion]    Sparse --> Fusion        Fusion --> Rerank[Cross-Encoder Reranking]    Rerank --> Filter[Context Window Filter]        Filter --> Prompt[Prompt Construction]    Prompt --> LLM[LLM Generation]    LLM --> Cite[Citation Extraction]    Cite --> Response[Final Response]
```

https://ranjankumar.in/images/2025/12/multi-stage-rag-pipeline.pngMulti-stage rag pipeline

When your retrieval quality drops, this diagram tells you exactly which stage to investigate. Is the query rewriter over-generalizing? Is fusion weighting wrong? Is the reranker actually improving results?

### 3\. Multi-Agent Research System

Research agents need more than simple tool calls. They plan, execute, reflect, and revise. This is LangGraph territory.

```
stateDiagram-v2    [*] --> Planning    Planning --> Research: Plan Created        Research --> ToolExecution: Query Generated    ToolExecution --> ResultEval: Results Retrieved        ResultEval --> Research: More Info Needed    ResultEval --> Synthesis: Sufficient Info        Synthesis --> Reflection: Draft Created    Reflection --> Revision: Gaps Found    Reflection --> Final: Quality Threshold Met        Revision --> Research: New Questions    Final --> [*]
```

https://ranjankumar.in/images/2025/12/multi-agent-research-system.pngMulti-agent research system

State machines are perfect for agent workflows. You can see the loops (research → tool → eval → research) and the exit conditions (quality threshold met). This maps directly to LangGraph's state management.

### 4\. LLM Inference Pipeline with Fallbacks

Production systems need graceful degradation. When your primary model is down or rate-limited, what happens?

```
sequenceDiagram    participant Client    participant Gateway    participant Primary as GPT-4    participant Secondary as Claude    participant Fallback as Local Model    participant Cache        Client->>Gateway: Request    Gateway->>Cache: Check Cache        alt Cache Hit        Cache-->>Gateway: Cached Response        Gateway-->>Client: Response (5ms)    else Cache Miss        Gateway->>Primary: Generate                alt Primary Success            Primary-->>Gateway: Response            Gateway->>Cache: Store            Gateway-->>Client: Response (800ms)        else Primary Error            Gateway->>Secondary: Fallback Request                        alt Secondary Success                Secondary-->>Gateway: Response                Gateway-->>Client: Response (1200ms)            else All Failed                Gateway->>Fallback: Local Generation                Fallback-->>Gateway: Degraded Response                Fallback-->>Client: Response (400ms)            end        end    end
```

https://ranjankumar.in/images/2025/12/llm-inference-pipeline-with-fallbacks.pngLLM Inference Pipeline with Fallbacks

Sequence diagrams excel at showing timing, fallback chains, and interaction patterns. This one shows exactly how your system degrades under load—critical for reliability planning.

### 5\. Agent State Transitions with Error Handling

Real agents don't just flow forward. They handle errors, timeouts, and invalid states.

```
stateDiagram-v2    [*] --> Idle        Idle --> Processing: New Task    Processing --> ToolCall: Action Required        ToolCall --> Success: Result OK    ToolCall --> Timeout: No Response    ToolCall --> Error: API Error        Timeout --> Retry: Attempt < 3    Error --> Retry: Retriable Error    Error --> Failed: Fatal Error        Retry --> ToolCall: Backoff Complete    Success --> Processing: Continue        Processing --> Complete: Task Done    Complete --> Idle: Reset        Failed --> Idle: Manual Reset
```

https://ranjankumar.in/images/2025/12/agent-state-transitions-with-error-handling.pngAgent State Transitions with Error Handling

This is the diagram I wish I'd had when debugging why agents were getting stuck. You can trace any execution path and see exactly where state transitions should happen.

## Making Mermaid Work in Your Stack

The diagrams are useful, but only if they integrate seamlessly into your workflow. Here's how I've set this up across different contexts.

### GitHub Integration

Mermaid renders natively in GitHub. Drop the code in any `.md` file. Your README, PR descriptions, and documentation all render diagrams automatically. No image hosting, no broken links.

When you're proposing architecture changes, include a Mermaid diagram showing the new flow. Reviewers see the change visually before diving into code.

### Documentation Sites

I use Quarto for technical writing, but the pattern works for MkDocs, Docusaurus, and most static site generators.

For Quarto:

```
format:  html:    mermaid:      theme: neutral
```

Then diagrams just work in your `.qmd` files. The theme setting keeps them readable in both light and dark modes.

### Jupyter Notebooks

When prototyping AI systems, I document the architecture right in the notebook:

````
from IPython.display import display, Markdown
mermaid_code = """```mermaid
graph TD
    A[Data] --> B[Preprocess]
    B --> C[Embed]
    C --> D[Index]
"""
display(Markdown(mermaid_code))
````

This keeps exploration and documentation together. When the experiment becomes production code, the diagram moves with it.

### VS Code

The Mermaid Preview extension lets you see diagrams as you write them. Edit your architecture doc, see the diagram update live. This tight feedback loop makes documentation actually enjoyable.

## Advanced Patterns I've Found Useful

Once you're comfortable with basic diagrams, these techniques will level up your documentation game.

### Custom Styling for Component Types

Different components deserve different visual treatment:

```
graph LR    A[User Input]:::input --> B[LLM]:::model    B --> C[(Vector DB)]:::storage    C --> D[Results]:::output        classDef input fill:#e1f5ff,stroke:#01579b    classDef model fill:#fff9c4,stroke:#f57f17    classDef storage fill:#f3e5f5,stroke:#4a148c    classDef output fill:#e8f5e9,stroke:#1b5e20
```

https://ranjankumar.in/images/2025/12/custom-styling-mermaid-diagram.pngcustom styling mermaid diagram

Color coding makes complex diagrams scannable. Blue for inputs, yellow for models, purple for storage, green for outputs. Your brain pattern-matches instantly.

### Subgraphs for System Boundaries

When documenting microservices or multi-container deployments:

```
graph TB    subgraph "API Layer"        A[FastAPI] --> B[Auth Middleware]    end        subgraph "Processing Layer"        C[Agent Orchestrator]        D[Tool Manager]        E[Memory Store]    end        subgraph "Infrastructure"        F[(PostgreSQL)]        G[(Redis)]        H[Vector DB]    end        B --> C    C --> D    C --> E    E --> F    D --> G    C --> H
```

https://ranjankumar.in/images/2025/12/subgraphs-for-system-boundaries.pngSubgraphs for System Boundaries Mermaid Diagrams

Subgraphs make system boundaries explicit. You can see what's stateful versus stateless, what scales horizontally, where your bottlenecks are.

### Links to Code

This is borderline magical. You can make diagram nodes clickable:

```
graph LR    A[Agent Router] --> B[Search Tool]    click A "https://github.com/yourorg/repo/blob/main/agent/router.py"    click B "https://github.com/yourorg/repo/blob/main/tools/search.py"
```

https://ranjankumar.in/images/2025/12/links-to-code-mermaid-diagram.pngLinks to Code Mermaid Diagram

Your architecture diagram becomes a navigable map of your codebase. Click a component, jump to its implementation.

## When Mermaid Isn't Enough

I'm bullish on diagram-as-code, but it's not universal. Know the limits.

**Complex visual design.** If you're creating marketing materials or presentation slides with custom branding, use proper design tools. _Mermaid is for technical documentation, not visual design._

**Extremely large graphs.** Once you hit 50+ nodes, Mermaid diagrams become hard to read. At that scale, consider breaking into multiple diagrams or using specialized graph visualization tools.

**Real-time monitoring.** Mermaid is static. If you need live system visualization—metrics flowing through your pipeline, real-time dependency graphs—you want something like Grafana or custom dashboards.

The sweet spot is architectural documentation, system design, and workflow explanation. That covers 90% of what AI engineers need to document.

## Making This Stick

Here's how I've built this into my development workflow so it actually happens:

**Diagram-first design.** When planning a new feature, I sketch it in Mermaid before writing code. The act of documenting the design forces me to think through edge cases and dependencies.

**PR templates with diagram prompts.** Our PR template asks: "Does this change affect system architecture? If yes, update or add Mermaid diagrams." Makes documentation part of the review process.

**Living architecture docs.** We maintain a `docs/architecture/` folder with Mermaid diagrams for each major subsystem. When the system changes, the diff shows both code and diagram updates.

**Blog post diagrams as code.** When I write technical posts, diagrams are Mermaid by default. This means I can update them easily, and readers can fork the code to customize for their needs.

## The Bigger Picture

This isn't really about Mermaid. It's about treating documentation as code.

When I look at successful AI engineering teams, they share a pattern: their documentation lives close to the implementation. Design docs in the repo. Architecture diagrams version-controlled. API specs generated from code.

The teams struggling with documentation debt? Their diagrams live in Google Slides. Their architecture docs are in Confluence, last updated six months ago. There's friction between writing code and updating docs, so docs don't get updated.

Mermaid removes that friction. Your diagram is a text file in your repo. Updating it is as natural as updating a comment. Code review catches documentation drift. Your architecture is always in sync because the alternative is harder.

For AI systems—where complexity grows fast, and architectures evolve constantly—this matters more than most domains. The difference between a team that can onboard new engineers in days versus weeks often comes down to documentation quality.

And documentation quality comes down to whether updating it is painful or painless.

## Getting Started Today

If you're convinced but not sure where to start:

**Pick one system to document.** Don't boil the ocean. Choose one complex workflow—maybe your RAG pipeline or agent orchestration logic—and diagram it in Mermaid.

**Put it in your repo.** Create a `docs/architecture.md` file. Diagram goes there. Commit it.

**Link from your README.** Make the documentation discoverable. "See architecture docs for system design."

**Update it in your next PR.** When you modify that system, update the diagram in the same commit. Feel how much easier this is than updating a PowerPoint.

**Expand gradually.** As you see the value, add more diagrams. Sequence diagrams for complex interactions. State machines for agent workflows. Flowcharts for decision logic.

The goal isn't comprehensive documentation on day one. It's building a habit where documentation updates are as natural as code updates.

## Resources and Templates

I've already provided production-ready Mermaid templates for common AI system patterns above. You can customize it for your needs.

**Useful Mermaid resources:**

- [Official documentation](https://mermaid.js.org/) - comprehensive reference

- [Live editor](https://mermaid.ranjankumar.in/) - test diagrams instantly ( **_I created this for FREE usage_** - No data storage, runs on your browser locally)

- [VS Code extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) - preview while editing

- [GitHub support docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) - integration details


The documentation is surprisingly good. When you need specific syntax, the live editor's auto-complete helps.

## Final Thoughts

Your AI system is going to change. New techniques will emerge. Your architecture will evolve. That's the nature of working in a fast-moving field.

The question is whether your documentation will keep up.

Static diagrams won't. Screenshot-driven workflows can't. The friction is too high.

Diagram-as-code can. When updating documentation is as easy as updating code, it actually happens.

I've seen this transform how teams work. Less time in meetings explaining architecture. Faster onboarding. Fewer "wait, how does this actually work?" moments.

The switch isn't hard. Pick one diagram you currently maintain in a visual tool. Recreate it in Mermaid. Put it in your repo. Update it once. You'll feel the difference.

That's when you'll know this isn't just another documentation fad. It's the infrastructure for how modern AI systems should be documented.
```

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="what-is-tool-calling-ibm.md">
<details>
<summary>What is tool calling?</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.ibm.com/think/topics/tool-calling>

# What is tool calling?

By

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

## Tool calling overview

Tool calling refers to the ability of artificial intelligence (AI) models to interact with external tools, [application programming interfaces](https://www.ibm.com/think/insights/llm-apis) (APIs) or systems to enhance their functions.

Instead of relying solely on pretrained knowledge, an AI system with tool-calling capabilities can query databases, fetch real-time information, execute functions or perform complex operations beyond its native capabilities.

Tool calling, sometimes referred to as function calling, is a key enabler of [agentic AI](https://www.ibm.com/think/topics/agentic-ai). It allows autonomous systems to complete complex tasks by dynamically accessing and acting upon external resources.

Instead of just answering questions, large language models (LLMs) with tool calling can automate workflows, interact with databases, perform multistep problem-solving, make real-time decisions and more.

This shift is turning LLMs from passive assistants into proactive digital agents capable of carrying out complex tasks.

## Why is tool calling important?

[Large language models](https://www.ibm.com/think/topics/large-language-models) (LLMs) are traditionally limited by the data on which they are trained, a process that can be time and computationally intensive.

Even though leading LLMs are trained on vast datasets, the need for real-time data, external computations and enhanced interactivity led to the integration of tool calling capabilities.

Early LLMs, including OpenAI’s GPT-2, were static. They generated responses based on their training data without the ability to fetch new information.

While impressive, they lacked real-world awareness and struggled with dynamic queries requiring live data, such as current events, stock prices or user-specific actions.

To address this limitation, developers began integrating external plug-ins, APIs and databases, allowing models to request and process real-time information rather than relying solely on static training data.

Developers trained LLMs to recognize when a query required external assistance. Moreover, external systems often have a particular input schema. Tool calling requests model responses that match the particular schema used by external systems.

AI agents

https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_0suvlp8f/width/1180

### 5 Types of AI Agents: Autonomous Functions & Real-World Applications

Learn how goal-driven and utility-based AI adapt to workflows and complex environments.

## How does tool calling work?

Tool calling involves several key components that work together to facilitate AI interaction with external tools. Modern LLMs including Anthropic’s Claude, Meta’s Llama 3, Mistral and [IBM® Granite™](https://www.ibm.com/granite) all possess tool calling capabilities but handle each a bit differently.

The first component is the AI model itself, which recognizes when it lacks sufficient knowledge or requires an external function to complete a request.

Next, the tool selection mechanism identifies the appropriate dependencies to handle the specific task, whether it is a search engine, a database or a computational resource.

When a tool is selected, the API interface comes into play, allowing the AI to send structured queries and receive responses in a machine-readable format.

Finally, the response processing system helps ensure that the retrieved data is formatted correctly and presented to the user in a meaningful way.

### Step 1. Recognizing the need for a tool

Let’s say a user asks an LLM “What’s the weather in San Francisco right now?” The AI uses natural language understanding to recognize that real-time weather data is needed, which cannot be derived from its static knowledge base.

A unique tool call ID is assigned automatically to a request made by a model to use a tool, which acts as a tracking number to link the request with its corresponding result.

### Step 2. Selecting the tool

The AI identifies the best tool for the task, in this case checking a current weather database. This step helps ensure that the retrieved information is accurate and relevant.

Each tool contains metadata and structured information such as a unique tool name (or function name), which helps the model and system identify it correctly. Other metadata include description, tool parameters and required input and output types.

The model performs a tool choice after determining that data must be obtained from a selection of available tools.

Templates are structured prompt formats that tell the model which tool to use and what arguments (or “args”) to provide, allowing for more controlled and structured interactions with APIs.

In the context of tool calling, args refer to the structured inputs passed to a tool or function when it is started by a generative model. These arguments define the parameters that the tool requires to execute properly.

Combining tool calling with [retrieval augmented generation](https://www.ibm.com/think/topics/retrieval-augmented-generation) (RAG) enhances AI capabilities by allowing systems to retrieve both structured and unstructured data before generating structured outputs.

This approach enhances contextual relevance by fetching the most pertinent data before generating a response, leading to more informed and accurate outputs.

It also minimizes API overhead by consolidating multiple retrievals into a single step, reducing latency and costs. RAG is more flexible than traditional tool calls, allowing models to pull from diverse sources and making it highly adaptable across different domains.

Unlike the rigid structure of traditional tool use, RAG enables more fluid integration of retrieved knowledge with reasoning and generation, resulting in more dynamic and insightful responses.

### Step 3. Constructing and sending a query

The AI then formulates a structured request that the tool or API can understand.

Each tool is associated with specific tool functions, which define what the tool does. These functions rely on an API reference, which provides documentation on how to interact with the tool’s API, including endpoint URLs, request methods and response formats.

To access an external API, many services require an API key, a unique identifier that grants permission to make requests. When the tool is selected and the parameters are set, an API call is made to fetch the requested data. This request is typically sent over HTTP to an external server.

### Step 4. Receiving and processing the response

The external tool returns data. The AI must then parse the tool results. For a weather request, the API might respond with a JSON schema object containing temperature, humidity and wind speed. The AI filters and structures this data to summarize a meaningful response for the user.

### Step 5. Presenting the information or taking action

The AI delivers the processed information in an intuitive manner. If the request involves automation, such as setting a reminder, the AI would confirm that an action has been scheduled.

### Step 6. Refining the search

If the user requests more details or modifications, the AI can repeat the process with an adjusted query, helping to ensure that it continues to refine its response based on user needs.

LangChain is commonly used in tool calling by providing an open source framework for integrating external tools, APIs and functions with LLMs. It helps manage tool execution, input or output handling and context-aware decision-making.

For example, LangChain handles function arguments with a parser for user queries, extracting relevant parameters and formatting them correctly for the tool. Unlike simple tool calling, LangChain can store and recall previous tool outputs, enabling better multiturn interactions.

LangChain allows for the combination of multiple tools in a sequence, enabling more complex agentic workflows. For example, it can first retrieve data from the weather API and then use a separate tool to recommend clothing based on the forecast.

https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_7jyt7r2n/width/1180

What is Tool Calling? Unlocking Real-Time Data Insights (4:56 min)

## Types of tool calling

Tool calling allows LLMs to do all sorts of tasks. There are limitless use cases for AI applications that use tool calling, but here are 5 common categories with some real-world examples.

### Information retrieval and search

AI fetches real-time data from the web, news sources, academic databases or financial markets. For example, an AI chat model can call a search API to provide the latest stock prices or AI research articles and deliver the information through a chatbot.

### Code execution

This allows AI to perform complex calculations or run scripts using mathematical engines such as Wolfram Alpha or Python execution environments. This is useful for solving equations, running simulations or executing small code snippets.

### Process automation

AI automates workflows such as scheduling meetings, sending emails or managing to-do lists through integrations with platforms such as Google Calendar and Zapier. AI agents can interact with CRM, finance and analytics tools such as Salesforce and QuickBooks, allowing businesses to automate processes including customer data retrieval or financial reporting.

### Smart devices and IoT monitoring

Agentic AI systems can monitor and control home automation systems, industrial IoT devices and robotics. We can easily imagine that one day entire end-to-end workflows are handled by autonomous agents.

Techsplainers | Podcast

https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_rw4kp245/width/1180

### Listen to: 'What is tool calling?'

Follow Techsplainers: [Spotify](https://open.spotify.com/show/1CuiV3XpXm68MxGpllQV4j) and [Apple Podcasts](https://podcasts.apple.com/us/podcast/techsplainers-by-ibm/id1850811611)

## Author

https://www.ibm.com/adobe/dynamicmedia/deliver/dm-aid--6ffe6fc8-d405-4a89-ad05-780d6960d862/cole-stryker-2x.jpg?preferwebp=true&width=128

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

Staff Editor, AI Models

IBM Think

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="why-parallel-tool-calling-matters-for-llm-agents.md">
<details>
<summary>How Parallel Tool Calling Accelerates LLM Agent Performance</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.codeant.ai/blogs/parallel-tool-calling>

# How Parallel Tool Calling Accelerates LLM Agent Performance

https://framerusercontent.com/images/xu7SueqXcNpwjNijr5WBnn0h4.png?width=2160&height=2160

Your LLM agent calls four APIs sequentially, each taking 300ms. That's 1.2 seconds of waiting, and your users notice every millisecond. Run those same calls in parallel, and you're down to 300ms total.

Parallel tool calling lets AI agents execute multiple external functions simultaneously instead of one at a time. This article covers how the mechanism works, when to use it over sequential execution, and how to measure the performance gains in your own agent workflows.

## What is Parallel Tool Calling in LLM Systems?

Parallel tool calling allows an LLM to request and execute multiple external functions at the same time instead of waiting for each one to finish before starting the next. When an AI agent handles a complex request, it often pulls data from several sources: APIs, databases, or third-party services. Running all of those calls simultaneously rather than sequentially cuts total response time dramatically.

Tool calling itself is the mechanism that lets LLMs interact with the outside world. Without it, a language model can only work with the information already in its training data. With tool calling, the model can fetch live weather, query a database, or trigger an action in another system.

### How LLM Tool Calling Works

The process follows a straightforward loop. First, you define the tools available to the model by describing what each function does, what inputs it accepts, and what it returns. When a user sends a prompt, the model decides whether any tools are relevant.

Here's the basic flow:

- **Tool definition:** You register functions with the LLM using a schema that describes parameters and expected outputs

- **Function invocation:** The model analyzes the prompt and generates structured calls with the right arguments

- **Response handling:** Results come back to the model, which uses them to form a final answer

This loop can repeat multiple times in a single conversation as the model gathers information step by step.

### Parallel vs Sequential Execution

The difference comes down to timing. Sequential execution means each tool call waits for the previous one to complete. If you have four API calls that each take 300ms, you're looking at 1.2 seconds of waiting.

| Aspect | Sequential Execution | Parallel Execution |
| --- | --- | --- |
| How it works | One call finishes before the next starts | Multiple calls run at the same time |
| Total latency | Sum of all individual call times | Duration of the slowest single call |
| Best for | Operations that depend on each other | Independent operations with no shared data |

Parallel execution changes the math. Those same four 300ms calls now complete in roughly 300ms total because they all run concurrently.

## How Parallel Tool Calling Works Under the Hood

Understanding the mechanics helps you spot opportunities to speed up your own agent workflows. The process breaks into four phases.

### 1. The Agent Receives a Multi-Tool Request

Picture a user asking: "What's the weather in Chicago, what's on my calendar today, and how long is my commute?" One prompt, but three completely separate data sources. The agent recognizes immediately that it will call multiple tools.

### 2. The LLM Identifies Parallelizable Operations

Next, the model figures out which operations depend on each other. Weather data doesn't affect calendar lookups. Traffic information doesn't change meeting times. Since none of the three calls rely on another's output, they're all candidates for parallel execution.

### 3. Tools Execute Concurrently

The orchestration layer dispatches all three requests at once. Your weather API, calendar service, and traffic provider all receive their queries simultaneously. No waiting in line.

### 4. Results Are Aggregated and Returned

As responses arrive, the system collects them. Once all tools report back, the LLM combines everything into a single coherent answer. The user sees one unified response and never knows three separate services contributed.

## Why Parallel Tool Calling Is a Force Multiplier

The "force multiplier" framing is accurate because parallel execution amplifies what AI agents can accomplish within the same time and resource constraints.

### Latency Reduction in Multi-Step Tasks

Total response time drops from the sum of all calls to the duration of the longest single call. For user-facing applications, this difference matters enormously.

A chatbot that takes 3 seconds to respond feels sluggish. One that answers in 500ms feels instant. Parallel tool calling often makes that gap possible without changing the underlying services at all.

### Higher Throughput for Complex Workflows

Beyond individual request speed, parallelism enables richer agent capabilities. An AI limited to sequential calls can only accomplish so much before users lose patience. Remove that constraint, and agents can gather data from many sources, cross-reference information, and deliver comprehensive answers in reasonable time.

This principle applies directly to developer tooling. Platforms like CodeAnt AI use parallel processing to analyze multiple files across a pull request simultaneously, reviewing security, quality, and standards compliance in one pass rather than scanning each concern one at a time.

### Cost Efficiency at Scale

Faster execution means lower compute costs per request. When infrastructure spends less time waiting on I/O operations, you serve more requests with the same resources. At enterprise scale, this translates directly to infrastructure savings.

## Sequential vs Parallel Tool Calling

Not every workflow benefits from parallelism. Knowing when to use each approach prevents bugs and wasted effort.

### When Sequential Execution Is Required

Some operations genuinely depend on each other. You can't parallelize without breaking your logic in cases like:

- **Data dependencies:** The output of one tool feeds into another (get user ID, then fetch that user's orders)

- **Ordered operations:** Steps follow a required sequence (authenticate first, then access protected resource)

- **State mutations:** Tools modify shared state that affects subsequent calls (update inventory, then check availability)

Forcing parallelism in any of those scenarios creates race conditions and incorrect results.

### When Parallel Execution Delivers Gains

Look for patterns like:

- **Independent data fetches:** Pulling user profile, preferences, and notifications from separate services

- **Redundant queries:** Running the same query against multiple sources for validation or failover

- **Batch operations:** Applying the same analysis to multiple inputs, like scanning several code files for vulnerabilities

The more independent operations you identify, the greater your potential speedup.

## Aggregation Strategies for Parallel Tool Outputs

Once parallel calls complete, you have multiple results to combine. The aggregation strategy depends on your use case.

### First-Response Aggregation

Use the first successful response and discard the rest. This works well for redundancy scenarios where you're querying multiple equivalent services and only care about getting one good answer quickly.

### Majority Voting Aggregation

Combine multiple responses and select the most common answer. This improves accuracy when individual sources might be unreliable. If three out of four services agree on a result, that's probably the correct one.

### Weighted Consensus Aggregation

Assign confidence scores to each response based on source reliability, then combine them accordingly. This approach suits complex decisions where some tools are more trustworthy than others.

## When to Use Parallel Tool Calling

Identifying parallelization opportunities in real workflows takes practice. Here are the clearest signals.

### Independent Tool Operations

Operations with no shared dependencies are ideal candidates. Fetching user profile, preferences, and notifications from separate services is a classic example since none of those calls affects the others.

### High-Latency External API Calls

Parallelism provides the greatest gains when individual calls have significant network or processing overhead. If each call takes 500ms, running five of them in parallel saves 2 full seconds compared to sequential execution.

### Batch Processing Scenarios

Applying the same operation to multiple inputs concurrently is another strong use case. Analyzing multiple code files at once, for instance, rather than processing them one by one.

## LLM Models and Frameworks with Parallel Tool Calling Support

The ecosystem has matured significantly. Most major providers now support parallel execution natively.

### OpenAI GPT-4 and GPT-4o

OpenAI's models support parallel function calling through the `parallel_tool_calls` parameter in the API. When enabled, the model can request multiple tool executions in a single response, and your application handles them concurrently.

### Anthropic Claude Models

Claude's tool use implementation handles parallel execution at the orchestration layer. The model can request multiple tools, and your infrastructure determines whether to run them sequentially or in parallel.

### Open-Source Models with Parallel Capabilities

Models like Llama 3 and Mistral support tool calling, though parallel execution typically depends on your orchestration framework rather than the model itself. The model generates the calls; your code decides how to execute them.

### LangChain and LlamaIndex Framework Support

Both frameworks provide built-in support for parallel tool execution. LangChain's `AgentExecutor` can run independent tool calls concurrently, while LlamaIndex offers similar capabilities through its agent abstractions.

## How to Measure Parallel Tool Calling Effectiveness

Tracking the right metrics validates your parallelization gains and surfaces problems early.

### Latency Reduction Metrics

Compare end-to-end response time before and after enabling parallel execution. Measure at the 50th, 95th, and 99th percentiles since averages hide important variation.

### Throughput and Completion Rates

Track requests processed per time unit and successful task completion rates. Parallelism often improves both, but watch for degradation under high load.

### Error Rate Tracking

Monitor for race conditions, timeout issues, or aggregation failures. Parallelism introduces new failure modes. A tool that works fine sequentially might timeout when competing for resources with other concurrent calls.

## Build Faster AI-Powered Developer Workflows

Parallel tool calling is an architectural pattern that enables entirely new categories of AI applications. When agents can gather information from multiple sources simultaneously, they become genuinely useful assistants rather than slow bottlenecks.

For engineering teams, this principle applies directly to code health. CodeAnt AI applies parallel processing across code reviews, security scans, and quality analysis, examining entire pull requests in one pass rather than sequentially checking each file and concern. The result is faster feedback loops and more comprehensive coverage.

## FAQs

What is parallelization in LLM systems?

Can parallel tool calling cause race conditions?

Does enabling parallel tool calling increase API costs?

What happens if one parallel tool call fails?

Does parallel tool calling change how LLM agents reason or just how fast they respond?

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