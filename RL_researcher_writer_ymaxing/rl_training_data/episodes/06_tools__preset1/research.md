# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>How does Gemini's GenerateContentConfig and native SDK support for direct function passing simplify production-level tool calling compared to manual schema definition and system prompts?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://composio.dev/content/tool-calling-guide-with-google-gemini

Query: How does Gemini's GenerateContentConfig and native SDK support for direct function passing simplify production-level tool calling compared to manual schema definition and system prompts?

Answer: Gemini's function-calling loop involves declaring tool schemas, Gemini returning functionCall objects, app executing them, and sending results back. The native google-genai SDK requires manual work: writing tool definitions, handling authentication, executing functions, and orchestrating the conversation loop. The request includes the user’s prompt and tools configuration via GenerateContentConfig in the Python SDK. Gemini decides if a function call is needed based on prompt and tool descriptions. Gemini responds with functionCall objects in candidate’s content.parts, specifying function name and JSON-compatible args matching the schema. The app then executes the functions, handling authentication, validation, error handling, and side effects, which are critical in production. The Genai SDK does not provide support for these aspects, implying manual schema definition and management. Composio abstracts this by providing pre-built integrations, avoiding manual tool schemas and auth.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://www.philschmid.de/gemini-function-calling

Query: How does Gemini's GenerateContentConfig and native SDK support for direct function passing simplify production-level tool calling compared to manual schema definition and system prompts?

Answer: GenerateContentConfig is used to pass tools directly as callable functions, e.g., config = GenerateContentConfig(tools=[get_weather_forecast]), where get_weather_forecast is defined as a function the LLM can use. This supports direct function passing in the SDK. System_instruction is also set in GenerateContentConfig for context. automatic_function_calling can be configured, with default behavior for callable functions to call them automatically, simplifying the process compared to manual setups. Examples show passing Python functions directly into tools list without manual JSON schema definition.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://ai.google.dev/gemini-api/docs/function-calling

Query: How does Gemini's GenerateContentConfig and native SDK support for direct function passing simplify production-level tool calling compared to manual schema definition and system prompts?

Answer: Gemini SDKs have built-in support for MCP (Model Context Protocol?), reducing boilerplate and offering automatic tool calling for MCP tools. When the model generates an MCP tool call, Python and JavaScript client SDKs can automatically execute the tool and send response back, continuing the loop until no more calls. For standard function calling, define function tool with manual schema like name, description, parameters as JSON schema (Type.OBJECT, properties, required). Use toolConfig with functionDeclarations. GenerateContent with config=types.GenerateContentConfig(tools=[tool_config]). Handle function_call.args manually, execute tool, send back FunctionResponse. This shows native SDK requires manual schema but supports config for tools; automatic execution mentioned for MCP tools simplifies production.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://glaforge.dev/posts/2023/12/22/gemini-function-calling/

Query: How does Gemini's GenerateContentConfig and native SDK support for direct function passing simplify production-level tool calling compared to manual schema definition and system prompts?

Answer: Gemini function calling involves describing external functions with parameters; model requests calls when needed, e.g., for weather info. Code examples show manual handling of generateContentRequest with tools, processing responses, executing functions, and building Content with FunctionResponse Struct for metadata like weather and location. No explicit GenerateContentConfig mention, but implies SDK streamGenerateContentCallable for handling loops. Focuses on manual execution and response feeding back, without highlighting simplification over manual schemas.

-----

</details>

<details>
<summary>How can a Pydantic model be registered as a tool using DocumentMetadata.model_json_schema() to enable on-demand structured outputs in multi-step agent loops with the Gemini SDK?</summary>

Phase: [EXPLOITATION]

### Source [5]: https://pydantic.dev/docs/ai/core-concepts/output/

Query: How can a Pydantic model be registered as a tool using DocumentMetadata.model_json_schema() to enable on-demand structured outputs in multi-step agent loops with the Gemini SDK?

Answer: By default, Pydantic AI leverages the model’s tool calling capability to make it return structured data. When multiple output types are specified (in a union or list), each member is registered with the model as a separate output tool in order to reduce the complexity of the schema and maximise the chances a model will respond correctly. This has been shown to work well across a wide range of models. If you’d like to change the names of the output tools, use a model’s native structured output feature, or pass the output schema to the model in its instructions, you can use an output mode marker class. [...] Prompted Output: In this mode, the model is prompted to output text matching the provided JSON schema through its instructions and it’s up to the model to interpret those instructions correctly. This is usable with all models, but is often the least reliable approach as the model is not forced to match the schema. Native Output mode uses a model’s native “Structured Outputs” feature (aka “JSON Schema response format”), where the model is forced to only output text matching the provided JSON schema. Note that this is not supported by all models, and sometimes comes with restrictions. For example, Gemini cannot use tools at the same time as structured output, and attempting to do so will result in an error. To use this mode, you can wrap the output type(s) in the NativeOutput marker class that also lets you specify a name and description if the name and docstring of the type or function are not sufficient.

-----

-----

Phase: [EXPLOITATION]

### Source [6]: https://pydantic.dev/docs/ai/guides/multi-agent-applications/

Query: How can a Pydantic model be registered as a tool using DocumentMetadata.model_json_schema() to enable on-demand structured outputs in multi-step agent loops with the Gemini SDK?

Answer: Define the first agent, which finds a flight. We use an explicit type annotation until PEP-747 lands, see structured output. We use a union as the output type so the model can communicate if it's unable to find a satisfactory choice; internally, each member of the union will be registered as a separate tool. Define a tool on the agent to find a flight. In this simple case we could dispense with the tool and just define the agent to return structured data, then search for a flight, but in more complex scenarios the tool would be necessary. Define usage limits for the entire app. Define a function to find a flight, which asks the user for their preferences and then calls the agent to find a flight. [...] r = await joke_generation_agent.run( f'Please generate {count} jokes.', deps=ctx.deps, # (3) usage=ctx.usage, r) return r.output @joke_generation_agent.tool # (5) async def get_jokes(ctx: RunContext[ClientAndKey], count: int) -> str: response = await ctx.deps.http_client.get( '
params={'count': count}, headers={'Authorization': f'Bearer {ctx.deps.api_key}'}, ) response.raise_for_status() return response.text async def main(): async with httpx.AsyncClient() as client: deps = ClientAndKey(client, 'foobar') result = await joke_selection_agent.run('Tell me a joke.', deps=deps) print(result.output) #> Did you hear about the toothpaste scandal? They called it Colgate. print(result.usage()) # (6) #> RunUsage(input_tokens=220, output_tokens=32, requests=4, tool_calls=2) In multi-agent applications, structured outputs are used with unions registered as tools for agent communication in loops.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://discuss.ai.google.dev/t/response-schema-from-pydantic/50028

Query: How can a Pydantic model be registered as a tool using DocumentMetadata.model_json_schema() to enable on-demand structured outputs in multi-step agent loops with the Gemini SDK?

Answer: User asks: For example, I have a Pydantic model like: from pydantic import BaseModel class LabeledText(BaseModel): text: str categories: list[str] In OpenAI API I can pass the Pydantic model into the structured output. How can I do it in Gemini API? Response: You can also use pydantic. For example: from pydantic import BaseModel class Recipe(BaseModel): recipe_name: str recipe_description: str recipe_ingredients: list[str] model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest") result = model.generate_content( "List a few imaginative cookie recipes along with a one-sentence description as if you were a gourmet restaurant and their main ingredients", generation_config=genai.GenerationConfig( response_mime_type="application/json", response_schema = list[Recipe]), request_options={"timeout": 600}, ) This shows passing Pydantic models directly to response_schema in Gemini SDK for structured outputs. Related topics include using list of Pydantic objects in response schema.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://pydantic.dev/docs/ai/tools-toolsets/tools/

Query: How can a Pydantic model be registered as a tool using DocumentMetadata.model_json_schema() to enable on-demand structured outputs in multi-step agent loops with the Gemini SDK?

Answer: The simplest way to register tools via the Agent constructor is to pass a list of functions, the function signature is inspected to determine if the tool takes RunContext. agent_a and agent_b are identical — but we can use Tool to reuse tool definitions and give more fine-grained control over how tools are defined, e.g. setting their name or description, or using a custom prepare method. Tools can return anything that Pydantic can serialize to JSON. For advanced output options including multi-modal content and metadata, see Advanced Tool Features. Tool Schema. Registering via Decorator: @agent.tool is considered the default decorator since in the majority of cases tools will need access to the agent context. Here’s an example using both: Registering via Agent Argument: As well as using the decorators, we can register tools via the tools argument to the Agent constructor. This is useful when you want to reuse tools, and can also give more fine-grained control over the tools. In Pydantic AI, tools are registered on agents, relevant for multi-step loops, but no specific mention of DocumentMetadata.model_json_schema or Gemini.

-----

</details>

<details>
<summary>What are the three main limitations of running tools sequentially in a loop without intermediate LLM interpretation, and how do they motivate more sophisticated patterns like ReAct?</summary>

Phase: [EXPLOITATION]

### Source [9]: https://myengineeringpath.dev/genai-engineer/agentic-patterns/

Query: What are the three main limitations of running tools sequentially in a loop without intermediate LLM interpretation, and how do they motivate more sophisticated patterns like ReAct?

Answer: The simplest possible agent implementation: pass the user’s query to the LLM with a list of tools, and ask it to use the tools and answer. This works for demonstrations. In production, it fails in predictable ways. Unbounded loops. Without a termination condition, an agent reasoning about a complex problem may loop indefinitely — calling tools, observing results, calling more tools, never converging. This burns tokens and produces no answer. Silent tool failure. A tool returns an error. The agent sees the error message, decides to try a different tool, encounters a second error, and returns a confident-sounding answer based on no valid data. Nothing in the loop explicitly handles the failure state. Without a maximum step count, a ReAct agent that cannot find the answer to a query will continue calling tools indefinitely. Always configure a maximum iteration count. When the limit is reached, return the best available answer with an explicit signal that the response may be incomplete — do not return nothing. The minimal viable agent is a ReAct loop: a system prompt that instructs the LLM to emit Thought/Action/Observation cycles, a loop that executes tool calls and appends observations to the context, and a termination condition that detects a Final Answer. In LangGraph, this is a graph with one node per step type and a conditional edge that checks whether the LLM has finished. In LangChain, it is an AgentExecutor with a prompt template that encodes the ReAct format. Before moving to more complex patterns, run this loop on representative inputs. Observe where it fails. Does it select wrong tools? Does it loop? Does it produce incorrect answers? The failure mode determines the next pattern to add.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://blogs.oracle.com/developers/what-is-the-ai-agent-loop-the-core-architecture-behind-autonomous-ai-systems

Query: What are the three main limitations of running tools sequentially in a loop without intermediate LLM interpretation, and how do they motivate more sophisticated patterns like ReAct?

Answer: 1. It cannot iterate on results. A single-pass system can execute a tool call within a turn, but it has no mechanism to evaluate whether that action succeeded, adapt based on the outcome, or chain a subsequent decision from the result. There is no feedback loop. 2. It cannot recover from failure. Without iterative execution, a failed tool call, an empty result set, or an ambiguous API response cannot trigger a revised strategy. The model has no visibility into downstream outcomes. 3. It cannot decompose dependent tasks. Real-world workflows require gathering information, making decisions based on that information, executing actions, and handling the consequences of those actions. Each step depends on the result of the previous one. That is a loop, not a straight line. In pseudocode, the complete pattern reduces to six lines: while not done: response = call_llm(messages) if response has tool_calls: results = execute_tools(response.tool_calls) messages.append(results) else: done = True return response This execution pattern underpins every autonomous AI system currently in production. It is the foundation on which every major AI organisation has built its agentic architecture. Anthropic’s engineering team describes the pattern directly: ‘Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop.' The principle from both OpenAI and Anthropic’s published guidance is consistent: start with the simplest architecture that solves the problem. Introduce the agent loop only when iterative reasoning and adaptive tool use are required.

-----

</details>

<details>
<summary>What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/

Query: What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?

Answer: The Neo4j Context Provider (a knowledge graph retriever) addresses accessing data beyond top-k chunks. It searches a Neo4j database and traverses the graph to return structured company data, including products, risk factors, and filing metadata, alongside text chunks from vector search. This provider is stateless, reading from the graph without writing to it. Knowledge comes from independently loaded data like SEC filings, product catalogs, maintenance records. Standard RAG uses vector search for semantic similarity but misses connections. A knowledge graph stores connections between unstructured text and structured entities, enabling retrieval via relationships. For example, it surfaces structured context on Apple's risks like competitive pricing, frequent new products, short product life cycles, evolving standards, by traversing the graph after vector search.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://www.ruh.ai/blogs/how-vector-databases-are-rewiring-the-tech-industry

Query: What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?

Answer: Vector databases provide persistent, updatable AI memory with full CRUD support, retaining knowledge across sessions unlike temporary context windows, allowing updates, corrections, or deletions. They act as long-term episodic memory for agentic AI, storing past interactions and decisions for reasoning across sessions. Used in RAG to solve LLM memory problems by serving as external, queryable knowledge stores for company documents, news, product data. Convergence with traditional databases like PostgreSQL, MongoDB, Cosmos DB adding native vector search. High memory requirements for HNSW indexes at scale, approximate accuracy trade-offs.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://promethium.ai/guides/text-to-sql-basics-benefits/

Query: What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?

Answer: Text-to-SQL enables natural language to SQL query generation for classic databases, enhancing data accessibility. Historical development includes classical ML with statistical parsing like PRECISE, and deep learning with seq2seq models, LSTMs, transformers. Benefits: Democratizes data access for non-technical users like business analysts, eliminating SQL expertise need, empowering autonomous insights from data assets.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://www.linkedin.com/posts/amanc_sql-datascience-artificialintelligence-activity-7390564257819652096-scgG

Query: What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?

Answer: LangChain connects LLMs to real-time data via databases, adds memory for past interactions, enables tool use like SQL. Key components: Retrievers pull data from external documents, Vector Stores like FAISS, Pinecone, Chroma store text embeddings for semantic search. Example: RAG over private documents - upload PDFs, embed to vector DB, retrieve similar chunks for LLM. Architecture: User → LangChain → Retriever (Vector DB) → LLM, with Memory. Supports text-to-SQL via dynamic tool calling.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.instaclustr.com/education/vector-database/top-10-open-source-vector-databases/

Query: What industry tools fall under Knowledge & Memory Access, including vector database queries, text-to-SQL for classic databases, and connections to long-term memory beyond the context window?

Answer: Vector databases manage, index, query high-dimensional vector data for ML, data mining, analytics. Used in recommendation systems, image/video recognition, NLP via similarity searches. Open source options include dedicated ones and general purpose like PostgreSQL, Cassandra with vector support. Instaclustr manages vector DBs for performance, scalability. Unlike traditional databases for structured data, vector DBs handle high-dimensional data for similarity/pattern recognition.

-----

</details>

<details>
<summary>How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?</summary>

Phase: [EXPLOITATION]

### Source [16]: https://arxiv.org/html/2507.08034v1

Query: How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?

Answer: To overcome these challenges, it is becoming necessary to integrate LLMs with external tools like calculators, calendars, and databases. This combination improves the capabilities of LLMs, allowing them to process language while having access to and analysing current data, and handling computational tasks. This expansion broadens their practical use and application by a large margin. Recent developments in LLMs have focused on extending their capabilities through external tools to address tasks like arithmetic, factual lookups, and real-time information retrieval. Integrating external tools with LLMs methods can be classified into four major categories: Retrieval-augmented generation (RAG), Code execution and computation, connection to APIs, Hybrid systems. Retrieval-augmented methods aim at connecting LLMs with external databases or retrieval systems, such as search engines and databases, to retrieve real-time data in order to provide more accurate, industry-specific, and relevant answers. Integrating code execution and computation tools, like Python, data analysis, solvers, calculator, and symbolic reasoners, allows executing code, performing mathematical computations to enhance LLMs capabilities to solve complex tasks. Connecting APIs, such as financial, health, weather, to utilise specialised service in order to handle domain-specific tasks. The Toolformer, introduced by Meta AI Research and Universitat Pompeu Fabra, enables LLMs to autonomously use simple APIs. This model employs a self-supervised loss to generate a language modelling dataset with embedded API calls, which is then fine-tuned to enhance future token predictions. Toolformer incorporates various tools like calculators and search engines, demonstrating improved zero-shot performance on downstream tasks and addressing limitations such as fact hallucination and outdated information. The Gorilla model, based on a fine-tuned LLaMA model, focuses on enhancing API interaction within LLMs. It surpasses GPT-4 in generating accurate API calls and adapting to document changes, significantly reducing hallucination issues.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://mantraideas.com/llm-web-search/

Query: How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?

Answer: Modern LLMs don’t just generate text—they can also “call functions” or use “tools.” Think of it like giving your AI assistant a toolkit. When you ask an AI to search the web, it doesn’t magically know how to browse the internet. Instead, it has access to a web search tool (like a search API) that it can call. The LLM typically uses a search API (like ChatGPT uses Bing Search API, Gemini uses Google Custom Search, or specialized search services) rather than literally opening a web browser. These APIs return structured data in particularly JSON format including metadata like publication dates, source. The model has been trained to recognize when its existing knowledge is sufficient versus when it needs fresh information. For example, if you ask “What’s the capital of Nepal?”—the LLM knows this is stable information that hasn’t changed, so it won’t search. But if you ask “What’s happening in the stock market today?”—now it is the time for the web search.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://medium.com/@anicomanesh/how-llm-reasoning-powers-the-agentic-ai-revolution-cbefd10ebf3f

Query: How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?

Answer: Instrumental reasoning manifests in three forms: 1. Retrieval-augmented reasoning: External knowledge bases (vector databases, search engines) expand the model’s knowledge beyond training cutoffs. 2. Executable reasoning: Code interpreters allow the model to “think” via execution — calculating exact arithmetic, running simulations, or validating logic through empiricism rather than pattern matching. 3. Embodied reasoning: Physical or virtual robotics ground abstract plans in sensorimotor loops, where actions have measurable physical consequences. The instrumental mode addresses the grounding gap by externalizing cognitive work. Here, reasoning extends beyond the neural network into the environment — APIs become external working memory, code interpreters become simulators, and computer interfaces become sensory organs. This aligns with the “extended mind” thesis in cognitive science: cognitive processes are not bounded by the skull (or the context window) but distributed across the tools we wield. The modern agentic architecture operates as a multi-level control system: Execution Level: Each sub-goal invokes ReAct loops with tool use (APIs, browsers, code). Verification Level: External validators check preconditions (budget constraints, calendar conflicts).

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://lnu.diva-portal.org/smash/get/diva2:1801354/FULLTEXT01.pdf

Query: How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?

Answer: LLMs show an impressive ability to understand the intention of the user, generate a custom answer to his queries or solve specific problems. They already have a general knowledge of the world, but, on their own, they lack the specific knowledge domain of a company’s knowledge base, they are unaware of the current time and date, they do not perform well with maths calculations, they are unable to access current events. The ability to use external APIs (public or private) would increase the power of the LLM to retrieve data and its ability to interact with other systems. For instance, if a user asks an LLM-powered chatbot for the current weather, the LLM alone cannot fulfil the request because it does not have real-time data. However, suppose the LLM is programmed to interact with a weather API. In that case, it can formulate a suitable API request, receive the current weather data response, and present it to the user in an understandable format. This interaction demonstrates how APIs can significantly extend the capabilities of LLMs, enabling them to provide real-time data and access to external functionalities.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://medium.com/@yugalnandurkar5/llm-engineering-part-i-fa48d4307d26

Query: How do web search & browsing tools, code execution interpreters, and external API integrations (calendar, email, file system) enable LLMs to overcome their core limitation of being simple pattern matchers and text generators?

Answer: The use of Large Language Models (LLMs) like GPT-4 and ChatGPT, combined with OpenAI Function Calling (now generally referred to as Tools), represents a paradigm shift in processing unstructured data from documents. This technique transforms the LLM from a simple text generator into a reliable structured data extraction engine. Real-Time Data Access: Function calling overcomes the LLM’s limitation of having only static training data by enabling access to real-time APIs (weather, stocks, news). Complex Actions: The assistant can perform actions, like creating a calendar event, running a database query (as demonstrated in the search results), or sending a message. Structured Output (Pydantic Integration): Libraries often use Pydantic models to define the input and output schemas for functions, ensuring the JSON arguments returned by Gemini are correct and easily parsed into type-safe Python objects. This framework is essential for building agents that go beyond simple chat to provide dynamic, actionable, and data-driven assistance.

-----

</details>

<details>
<summary>How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?</summary>

Phase: [EXPLOITATION]

### Source [21]: https://community.openai.com/t/prompting-best-practices-for-tool-use-function-calling/1123036

Query: How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?

Answer: The discussion addresses whether tool details must be included in the system prompt for LLM function calling. It states that JSON definitions serve the API or middleware, but the model relies on explicit text in its context. Including tool details in the system prompt is not strictly necessary but helps to 'emphasize' their presence or prioritize specific functions. The system prompt is about 'emphasis' in general. Users can pass description fields in JSON definitions, and the LLM can see declared tools in parameters without needing system prompt mentions. This setup influences how the model references tools during responses, demonstrating decision-making through context awareness and prioritization cues for tool selection.

-----

-----

Phase: [EXPLOITATION]

### Source [22]: https://medium.com/@hariomshahu101/building-production-ready-llm-applications-bulletproof-llm-tool-calling-with-advanced-json-b95ce8889f4e

Query: How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?

Answer: The article details building robust LLM tool calling using explicit JSON schemas and system prompts. System prompts instruct the model to respond only with minified JSON matching the schema, e.g., {"location": ""}, without extra text. Rules include: ALWAYS use exact parameter names, NEVER add extra properties, ENSURE required parameters, VALIDATE types. Examples show correct calls like {"name": "get_weather", "arguments": {"location": "New York, USA"}}. Principles: explicit descriptions, type constraints, required fields, no additional properties, examples, real-time validation. Post-extraction: verify function existence, parse/validate JSON, check schemas with Pydantic. This demonstrates LLM decision-making by constraining it to select tools and generate precise parameters via schema-guided generation and validation, revealing reasoning through structured outputs.

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://tetrate.io/learn/ai/llm-output-parsing-structured-generation

Query: How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?

Answer: Function calling frames LLM interactions as tool usage with defined functions and parameter schemas in JSON Schema syntax, specifying types, constraints, required/optional params. The model decides which function to invoke and generates matching arguments. Well-crafted descriptions guide decision-making on when/how to use functions. This structured approach demonstrates LLM decision-making for tool selection (choosing relevant function) and parameter generation (producing schema-compliant args). Compared to prompt-based methods, it provides reliability via schema enforcement, with tools evolving for schema expressiveness and validation. Output validation handles errors, showing the model's reasoning through precise selection and structured argument creation.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-1-llm-agent-tooling-foundations/tool-input-output-schemas

Query: How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?

Answer: Tool schemas use JSON Schema for input definitions, e.g., get_weather with properties like location (string, description), unit (enum), required: ["location"]. Specific types (e.g., number for port) aid valid input generation. Distinguish required/optional params to inform LLM decisions on necessary info. Schemas make tools understandable for LLMs, enabling confident use. This demonstrates decision-making as the LLM selects tools based on schema descriptions and generates parameters matching types/constraints/requirements, turning tools into predictable components for reliable agent systems.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://mbrenndoerfer.com/writing/function-calling-llm-structured-tools

Query: How does implementing tool calls from scratch with explicit JSON schemas, system prompts like TOOL_CALLING_SYSTEM_PROMPT, and extraction of function name plus arguments demonstrate LLM decision-making for tool selection and parameter generation?

Answer: OpenAI-style function calling uses JSON structure: {"role": "assistant", "tool_calls": [{"type": "function", "function": {"name": "get_weather", "arguments": "{\"location\": \"Boston, MA\"}"}}]}. Extracts function name and arguments separately. Tool registry holds schemas (for LLM) and implementations. Execution trace: agent recognizes query, extracts params, executes tool. LLM handles decision-making for tool selection and parameter generation. Architecture separates concerns: LLM decides via schemas, demonstrating reasoning through name selection and structured arg generation in the explicit JSON format for parsing and routing.

-----

</details>

<details>
<summary>How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?</summary>

Phase: [EXPLOITATION]

### Source [26]: https://openai.github.io/openai-agents-python/tools/

Query: How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?

Answer: The @function_tool decorator (referred to as @tool) automatically extracts the tool name from the Python function name (or provided name), description from the docstring (or provided), and schema for inputs from the function's arguments using Python's inspect module, griffe for docstring parsing (supports google, sphinx, numpy formats), and pydantic for schema creation. It dynamically builds a Pydantic model from type annotations supporting primitives, Pydantic models, TypedDicts, etc. This automatic parsing avoids manual schema definitions, creating a tools registry implicitly through decorated functions without explicit TOOLS_BY_NAME or TOOLS_SCHEMA mappings, adhering to DRY by eliminating redundant manual entries. Code for schema extraction is in agents.function_schema. Features like defer_loading hide tools until needed, and tool_namespace groups them, further reducing manual registry management.

-----

-----

Phase: [EXPLOITATION]

### Source [27]: https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/

Query: How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?

Answer: The @tool decorator extracts information from the function’s docstring: first paragraph as tool description, 'Args' section for parameter descriptions, combined with type hints to create complete tool specification automatically. Example: @tool def weather_forecast(city: str, days: int = 3) -> str: with docstring provides all schema details without manual inputSchema. This replaces manual TOOL_SPEC = {'name': ..., 'description': ..., 'inputSchema': {...}} definitions in modules, creating an implicit registry of tools from decorated functions. Overrides possible via @tool(name=..., description=...). Follows DRY by auto-generating specs from code/docstrings, avoiding duplication between function impl and schema mappings. Module-based tools require manual TOOL_SPEC, but decorator approach eliminates this.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://pydantic.dev/docs/ai/tools-toolsets/tools/

Query: How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?

Answer: @agent.tool or @agent.tool_plain decorators register tools by inspecting function signature for schema (type hints to JSON schema via FunctionModel), docstring for descriptions (e.g., google format, require_parameter_descriptions=True extracts Args sections). Example: @agent.tool_plain def foobar(a: int, b: str, c: dict[str, list[float]]) with docstring generates parameters_json_schema automatically. Tools registered via agent constructor list or decorator build agent.toolsets implicitly, equivalent to manual Tool(name=..., description=..., schema=...) without duplication. Identical to passing functions directly: agent_a = Agent(tools=[func]) vs agent_b with @agent.tool. DRY achieved by single source (func + hints/docstring) for impl and schema, no separate mappings needed. Supports Pydantic Field for constraints.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://docs.langchain.com/oss/python/langchain/tools

Query: How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?

Answer: LangChain's @tool decorator infers tool name from function (customizable @tool('web_search')), description from docstring or arg, schema from signature/type hints/Pydantic BaseModel/Field. Examples: @tool def search(query: str), @tool('calculator', description=...) auto-generates schema. Advanced: Pydantic models for args_schema. Used in ToolNode([decorated_tools]) creates registry like manual tools list, avoiding separate name/schema dicts. Return types (str, dict, Command) handled automatically. DRY: schema from func hints/docstring only, no manual JSON schema duplication. Custom properties via decorator args.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://reference.langchain.com/python/langchain-core/tools/convert/tool

Query: How does a @tool decorator that automatically extracts schemas from function signatures, docstrings, and type hints create a tools registry similar to manual TOOLS_BY_NAME and TOOLS_SCHEMA mappings while following DRY principles?

Answer: LangChain Core's @tool decorator converts functions/Runnables to tools, inferring input schemas from signature (infer_schema=True, default), parsing docstrings (parse_docstring=True/False). Precedence: description arg > docstring > args_schema. Accepts dict input to run(). Parameters like name_or_callable overrides func name, args_schema optional custom, return_direct, response_format. Creates tool objects with auto name/desc/schema, collectible into registry (e.g., list of @tool funcs) replacing manual TOOLS_BY_NAME={name: tool}, TOOLS_SCHEMA={name: schema}. DRY via single func def for impl+schema, inspect-based extraction eliminates redundant mappings.

-----

</details>

<details>
<summary>Why must tool descriptions be clear and distinguishing when scaling to many tools?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://composio.dev/blog/how-to-build-tools-for-ai-agents-a-field-guide

Query: Why must tool descriptions be clear and distinguishing when scaling to many tools?

Answer: Clear and distinguishing tool descriptions are essential when scaling to many tools to prevent confusion and errors, ensuring precise and reliable interactions. Tools with multiple responsibilities confuse the agent and increase the risk of mistakes; splitting large 'do-everything' tools into smaller, single-purpose ones like copy_file, move_file, delete_file instead of manage_files leads to more reliable behavior and easier debugging. Write good tool descriptions starting with 'Tool to <what it does>. Use when <specific situation>.' Keep them short to help the agent understand purpose and context quickly. Vague, overly complex, or unclear descriptions undermine effectiveness. The goal is to clearly convey what the tool does and precisely indicate when to invoke it, reducing invocation errors. This clarity is crucial for tool composition where the LLM must clearly understand each tool's scope.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://www.anthropic.com/research/building-effective-agents

Query: Why must tool descriptions be clear and distinguishing when scaling to many tools?

Answer: It is crucial to design toolsets and their documentation clearly and thoughtfully, especially when using many similar tools. Clear descriptions and parameters make it obvious how to use the tool; if it's not obvious to a human (like a junior developer), it's not for the model. Good tool definitions include example usage, edge cases, input format requirements, and clear boundaries from other tools. This is especially important with many similar tools to distinguish them and reduce mistakes. Test model usage and iterate; poka-yoke tools to make errors harder.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://techinfotech.tech.blog/2025/06/09/best-practices-to-build-llm-tools-in-2025/

Query: Why must tool descriptions be clear and distinguishing when scaling to many tools?

Answer: In more complex systems exposing dozens of tools or functions to the LLM—each with their own capabilities, input requirements, and security constraints—it's important to define clear tool interfaces explicitly and consistently. This allows structured invocation where the model outputs a clearly defined object for the appropriate tool, enabling the backend to parse and route requests accurately.

-----

</details>

<details>
<summary>OpenAI function calling vs Anthropic tool use API format comparison</summary>

Phase: [EXPLOITATION]

### Source [34]: https://www.lilbigthings.com/post/anthropic-vs-openai

Query: OpenAI function calling vs Anthropic tool use API format comparison

Answer: OpenAI is strongly pushing the Responses API as an “agentic loop” that can call multiple tools within one request. Function/tool calling and Structured Outputs are first-class, including JSON schema response formats. Anthropic: Messages API plus capability modules like prompt caching, extended thinking, etc. Anthropic has been publishing engineering updates on more advanced tool use (tool discovery/learning/execution).

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://is4.ai/blog/our-blog-1/openai-api-vs-anthropic-api-comparison-117

Query: OpenAI function calling vs Anthropic tool use API format comparison

Answer: OpenAI API Features: Function Calling: Native support for calling external functions and APIs with structured JSON outputs. Assistants API: Build stateful applications with built-in memory and tool use. Anthropic API Features: Tool Use: Similar to function calling, with JSON schema definitions. Function calling differences: Tool use implementations differ slightly between platforms.

-----

-----

Phase: [EXPLOITATION]

### Source [36]: https://www.mgsoftware.nl/en/vergelijking/openai-api-vs-anthropic-api

Query: OpenAI function calling vs Anthropic tool use API format comparison

Answer: Function calling: OpenAI API - Mature function calling and structured outputs. Anthropic API - Tool use API with comparable capabilities.

-----

-----

Phase: [EXPLOITATION]

### Source [37]: https://sfailabs.com/guides/openai-api-vs-anthropic-api

Query: OpenAI function calling vs Anthropic tool use API format comparison

Answer: Feature Comparison: Function/tool calling - OpenAI API: Native, mature. Anthropic API: Supported. JSON mode - OpenAI API: Native. Anthropic API: Supported. Assistants API - OpenAI: Yes. Anthropic: No.

-----

-----

Phase: [EXPLOITATION]

### Source [38]: https://portkey.ai/blog/open-ai-responses-api-vs-chat-completions-vs-anthropic-anthropic-messages-api

Query: OpenAI function calling vs Anthropic tool use API format comparison

Answer: OpenAI's Chat Completions API — the de facto standard, universally supported. OpenAI's Responses API — the newer, agent-oriented evolution with built-in tools and state management. Anthropic's Messages API — Claude's native interface, with capabilities like extended thinking and prompt caching. Each was designed with different goals in mind.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What mathematical foundations underlie LLM tool selection from descriptions?</summary>

Phase: [EXPLORATION]

### Source [39]: https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-3-llm-tool-selection-orchestration/agent-tool-selection

Query: What mathematical foundations underlie LLM tool selection from descriptions?

Answer: At the foundation of tool selection lies the LLM's ability to understand intent from the user's input and match it against the described capabilities of available tools. The clarity and precision of your tool descriptions, as discussed in Chapter 1 ("Foundations of LLM Agent Tooling"), are fundamental here. The LLM analyzes the query and compares its interpretation to the descriptions of tools, looking for the best fit.

### Prompting with In-Context Tool Information

One direct method for tool selection involves providing the LLM with information about available tools directly within its context window as part of the prompt. The prompt typically includes the user's query alongside a list of tools, each with its name, a description of its function, and the parameters it accepts. [...] Quality and Clarity of Tool Descriptions: As emphasized repeatedly, the LLM relies heavily on how tools are described. Vague, ambiguous, or inaccurate descriptions will lead to incorrect tool selections. Descriptions should clearly state what the tool does, what inputs it expects, and what output it produces.
 Distinctiveness of Tools: If multiple tools have very similar descriptions or overlapping functionalities, the LLM may struggle to differentiate between them or may choose a sub-optimal tool. Ensure that each tool has a clearly defined, unique purpose, or provide guidance on when to prefer one over another if overlap is intentional. [...] The router LLM is typically provided with high-level descriptions of the downstream tools or chains. Based on the input query, it selects the most appropriate route. For example, a query like "What's the weather in Paris?" might be routed to a `weather_tool`, while "Calculate 25% of 180" would be routed to a `calculator_tool` or a `math_processing_chain`.

> A router LLM analyzes the incoming query and directs it to the most suitable specialized tool or processing chain from a set of options.

This approach helps to manage complexity by breaking down the decision-making process and can improve efficiency by not requiring a single LLM instance to be aware of the minute details of every possible tool if some are highly specialized.

### Factors Influencing Selection Accuracy

-----

-----

Phase: [EXPLORATION]

### Source [40]: https://apxml.com/courses/agentic-llm-memory-architectures/chapter-4-complex-planning-tool-integration/tool-description-selection

Query: What mathematical foundations underlie LLM tool selection from descriptions?

Answer: Ultimately, tool selection requires a combination of clearly defined tool contracts (descriptions) and intelligent mechanisms (primarily LLM-based reasoning, potentially augmented with retrieval or routing) to match task requirements to available capabilities. This is a fundamental step in enabling agents to interact meaningfully with external systems to accomplish complex goals.

Was this section helpful? [...] Semantic Tool Retrieval: Instead of including all tools, use embedding-based retrieval to find the most relevant subset of tools based on the current task description and include only those in the prompt.
 Hierarchical Tool Organization: Group tools by category (e.g., 'Data Analysis Tools', 'Communication Tools') and potentially have the LLM first select a category, then a specific tool within that category. [...] ### Mechanisms for Tool Selection

Once tools are adequately described, the agent needs a mechanism to choose the right one at the appropriate step in its plan.

#### LLM-Based Reasoning

The most prevalent approach relies on the LLM's own reasoning capabilities. The agent's prompt includes the current goal or sub-task, relevant context from previous steps (observations, memory), and the descriptions of all available tools. The LLM is instructed to analyze the situation and determine which tool, if any, should be executed next, along with the necessary parameters derived from the context.

Example Prompt Snippet:

-----

-----

Phase: [EXPLORATION]

### Source [41]: https://www.tdcommons.org/cgi/viewcontent.cgi?article=9446&context=dpubs_series

Query: What mathematical foundations underlie LLM tool selection from descriptions?

Answer: capability identification : determining the tools that provide the required capability against the 

user query from a set of tools with different capabilities registered with the agent (e.g., selecting 

stock quote tools from a se t of stock quote, search engine, weather, and other tools); and (b) 

implementation selection : selecting the appropriate tool from a set of tools determined to be of 

appropriate capability (e.g., selecting a stock quote tool from a set of stock quote tools). 

Currently, the single -step tool selection described above involves the use of an LLM to 

identify the appropriate tool from a set of tools provided, by matching the user query to the tool 

name, description etc. This process, which tightly couples tool capab ility and tool [...] be selected based on user query by the underlying LLM. The selection of an appropriate tool 

from the set of available tools is done by matching the user query to the tool name, description, 

etc. This tightly coupled process may not provide the flexibility wherein multiple tool 

implementations are available for one capability. 

For example, an LLM agent can be provided with two tools, one related to ‘stock quotes’ 

and one related to ‘weather updates.’ Sufficient description of tools is available to advertise their 

capabilities to the LLM. When a user query about stock quote is re ceived, the LLM agent action 

will involve invoking the tool providing the stock quote based on the tool name and description. [...] implementation, does not provide the flexibility when multiple tool impleme ntations exist for the 

same capability. 

DESCRIPTION 

This disclosure describes a tool selection procedure for agentic LLMs that separates or 

provides a loose coupling between tool capability and tool implementation. Accuracy and 

flexibility of tool selection is improved, especially when multiple tool impleme ntations with 

similar capabilities exist. The techniques result in the separation of responsibility between ML 

developers (who develop LLM agents) and ML administrators (who govern or manage the tools 

used by the LLM agents). Certain definitions follow. 

● Tool capability refers to a set of abstract resource definitions within an enterprise. For

-----

-----

Phase: [EXPLORATION]

### Source [42]: https://aclanthology.org/2025.findings-acl.811.pdf

Query: What mathematical foundations underlie LLM tool selection from descriptions?

Answer: 2.1 Graph Structure Formally, we model the tool ecosystem as a graph G = (V, Es ∪Ed), where nodes represent indi-vidual tools and edges capture complex inter-tool relationships. Each tool node vi ∈V is defined as a tuple (ei, φi), where ei includes API metadata and φi represents functional insights distilled through LLM-based experience summarization. These in-sights can serve as empirical knowledge for LLMs during the tool selection phase. The edges explic-itly characterize two fundamental relationships: Semantic Similarity Edges (Es): These edges connect tool pairs (vi, vj) with partial functional overlap or semantically analogous descriptions, which may mislead LLMs into conflating their dis-tinct capabilities during tool selection.

-----

</details>

<details>
<summary>How does instruction tuning optimize LLMs for structured tool outputs?</summary>

Phase: [EXPLORATION]

### Source [44]: https://www.ibm.com/think/topics/instruction-tuning

Query: How does instruction tuning optimize LLMs for structured tool outputs?

Answer: Instruction tuning is a technique for fine-tuning large language models (LLMs) on a labeled dataset of instructional prompts and corresponding outputs. It improves model performance not only on specific tasks, but on following instructions in general, thus helping adapt pre-trained models for practical use. Pre-trained LLMs are not optimized for conversations or instruction following; they only append text to a prompt. Instruction tuning makes that appended text more useful. As per Google Research’s 2022 paper 'Finetuned Language Models are Zero-Shot Learners,' instruction tuning improves LLMs' ability to respond to NLP instructions by combining pretrain–finetune and prompting paradigms. It organically incorporates prompt engineering into supervised fine-tuning, reducing the need for prompt engineering and few-shot exemplars to elicit useful, accurate responses. Each training sample comprises three elements (though not fully detailed in excerpt). This enhances generation of structured, instruction-following outputs.

-----

-----

Phase: [EXPLORATION]

### Source [45]: https://www.labellerr.com/blog/tuning-the-power-strategies-for-enhancing-language-models-through-instruction-tuning/

Query: How does instruction tuning optimize LLMs for structured tool outputs?

Answer: Instruction tuning is an approach that involves fine-tuning pre-trained LLMs using a collection of formatted instances represented in natural language. It is closely related to supervised fine-tuning and multi-task prompted training. To perform instruction tuning, formatted instances in the form of instructions are collected or created, then used to fine-tune LLMs through supervised learning, such as training with sequence-to-sequence loss. Formulating formatted instances involves formatting existing datasets with task descriptions, augmenting with human-written instructions, and utilizing real user queries to evaluate instruction-following ability. This enhances LLMs' generalization abilities across various tasks and multilingual settings, optimizing them for producing structured outputs that follow natural language instructions accurately.

-----

-----

Phase: [EXPLORATION]

### Source [46]: https://magazine.sebastianraschka.com/p/llm-research-insights-instruction

Query: How does instruction tuning optimize LLMs for structured tool outputs?

Answer: Instruction finetuning (instruction tuning) improves the responses of a pretrained LLM to follow instructions, such as 'Summarize this article' or 'Translate this sentence.' During instruction finetuning, it is common to mask out the instruction itself when calculating the loss, focusing the training on generating the output portion. This technique, used in libraries like LitGPT and discussed in related books, optimizes the model to produce accurate, instruction-compliant responses, which can include structured formats by emphasizing output generation over instruction repetition.

-----

-----

Phase: [EXPLORATION]

### Source [47]: https://www.geeksforgeeks.org/artificial-intelligence/instruction-tuning-for-large-language-models/

Query: How does instruction tuning optimize LLMs for structured tool outputs?

Answer: Instruction tuning equips LLMs with flexibility to perform well across diverse tasks by fine-tuning on a dataset of instruction-output pairs covering simple and complex instructions. The process: 1) Data collection of diverse instruction-output pairs (e.g., 'Translate to French' -> output). 2) Fine-tuning the pre-trained LLM using supervised learning to map instructions to outputs. 3) Evaluation and iteration on validation sets. This improves usability by ensuring adherence to user intent, generalization across tasks, and reduces hallucinations by aligning with instructions. It exposes the model to diverse examples, teaching it to interpret and execute instructions accurately for structured, task-specific outputs.

-----

-----

Phase: [EXPLORATION]

### Source [48]: https://www.dataiku.com/stories/blog/your-guide-to-structured-text-generation

Query: How does instruction tuning optimize LLMs for structured tool outputs?

Answer: Fine-tuning, including instruction tuning variants, improves compliance and accuracy for structured text generation. A special case is function calling, where LLMs are specifically trained to call functions and provide inputs in correct JSON format. By including function descriptions in prompts, the LLM recognizes when to call functions (e.g., for real-time data like weather), generating structured JSON outputs. This extends capabilities beyond raw text, optimizing for precise, formatted tool-like responses. While prompt engineering specifies formats like JSON, fine-tuning reduces errors and improves reliability for structured outputs.

-----

</details>

<details>
<summary>How does LLM tool calling parallel API orchestration in microservices?</summary>

Phase: [EXPLORATION]

### Source [49]: https://airbyte.com/agentic-data/parallel-tool-calls-llm

Query: How does LLM tool calling parallel API orchestration in microservices?

Answer: With parallel tool calling, the model analyzes your prompt and identifies which tools can run simultaneously because they don't depend on each other's outputs. It returns multiple tool calls in a single response. Your orchestration layer runs these concurrently, and all results come back in one batch for the model to synthesize. One important distinction: the model requests parallel execution, but your framework determines whether the calls actually run concurrently. The code example in the implementation section shows exactly where this matters and why it's the most common source of missed speedups. Parallel tool calling is a pattern where a large language model (LLM) identifies independent operations, requests them all in a single response, and your infrastructure executes those calls concurrently. Instead of waiting for each tool to finish before starting the next, independent calls run at the same time. Total latency drops from the sum of every tool call to the duration of the slowest one. In a standard tool-calling loop, the agent follows a strict sequence: prompt, tool request, execute, return results, repeat. Total latency is the sum of all tool execution times plus an LLM inference cycle for each step. When multiple tools fire concurrently, shared API quotas, OAuth token expiry, and schema changes become the real bottleneck. Airbyte's Agent Engine handles per-source rate limiting, token renewal, and schema mapping independently per connection through 600+ connectors, so concurrent calls don't break each other.

-----

-----

Phase: [EXPLORATION]

### Source [50]: https://aclanthology.org/2026.iwsds-1.18.pdf

Query: How does LLM tool calling parallel API orchestration in microservices?

Answer: Another recent example of structured and flexible orchestration is the introduction of function calling in LLM APIs (Kim et al., 2023). Instead of relying on the model to output a well-structured tool invocation via plain text, function calling lets the developer predefine the available tools and their JSON schema, and the LLM will return a structured invocation if it decides one is needed. This reduces hallucinations, because the LLM’s decision is immediately validated against a schema. An alternative to APIs is the Model Context Protocol (MCP) (Hou et al., 2025): instead of shipping the JSON schema with every request, developers host it on an MCP server that advertises its capabilities via a standard JSON-RPC interface; LLMs can then discover and invoke those tools at runtime. LLM agents can indeed use tools to improve accuracy and handle tasks beyond pure text generation. Notably, HuggingGPT showcased an LLM (ChatGPT) acting as a controller that, given a user query, plans a task list, selects appropriate expert models for each subtask, executes them, and composes the final answer. This allowed tackling a wide range of multimodal problems by delegating to specialized models, with the LLM orchestrating the entire process. Similarly, Microsoft’s TaskMatrix.AI (Liang et al.) concept envisioned “foundation models” like ChatGPT as a brain that can call up millions of external APIs or models as needed, rather than trying to solve everything with a single model. These works illustrate the promise of agent-based orchestration: extensibility (the agent can...). Definitions and Scope Throughout this paper, we use agent-based to mean LLM-first systems that dynamically plan tools use and control flow, and workflow-based to mean developer-specified graphs/pipelines where the control flow is explicit. Microservice orchestration (our approach) is a concrete instance of the workflow-based paradigm: each capability runs in its own service, and a Manager routes requests through a predefined graph. ORCHESTRA embeds scoped agentic decisions at selected nodes inside this fixed graph. In short: microservices ⊂workflow-based orchestration; agentic LLMs are used inside the workflow, not to replace it.

-----

-----

Phase: [EXPLORATION]

### Source [51]: https://wjaets.com/sites/default/files/fulltext_pdf/WJAETS-2025-1078.pdf

Query: How does LLM tool calling parallel API orchestration in microservices?

Answer: Direct invocation patterns allow microservices to call LLM endpoints synchronously for immediate response requirements, though this approach requires robust timeout and fallback mechanisms to prevent cascading failures. Mediator patterns introduce intermediate services that abstract LLM complexity from business microservices, handling model selection, prompt engineering, and response formatting while providing a stable interface for consuming services. Event-sourcing patterns enable microservices to emit domain events that trigger LLM processing asynchronously, preserving system responsiveness while allowing complex natural language tasks to execute in parallel workflows. Event-Driven Pattern Asynchronous LLM processing Batch documentation analysis Non-blocking operations, High throughput Mediator Pattern Abstraction layer for LLM complexity Multi-model orchestration Flexibility, reduced coupling. Message broker integration provides the foundation for scalable LLM processing within microservices ecosystems, decoupling request submission from response processing. Topic-based routing through Apache Kafka enables sophisticated workflow orchestration where LLM outputs trigger subsequent processing stages across multiple services. Dead letter queues and retry mechanisms handle the inherent uncertainty of LLM processing, ensuring that temporary model unavailability or processing errors don't result in data loss. Message schemas incorporate metadata for tracking processing lineage, enabling observability across complex LLM-augmented workflows. Effective integration of LLMs into microservices demands adherence to fundamental design principles that ensure system coherence and operational efficiency. Service boundaries must be clearly defined to prevent LLM functionality from creating tight coupling between previously independent components. The principle of single responsibility extends to LLM integration, where each augmented service maintains a focused purpose.

-----

-----

Phase: [EXPLORATION]

### Source [52]: https://community.openai.com/t/parallel-tool-calling-where-there-is-an-ordering-dependency/1086995

Query: How does LLM tool calling parallel API orchestration in microservices?

Answer: The tools in the Chat completion API can be called in parallel. I do get multiple calls and execute in a different thread. I understand they can be run in parallel but I see there are calls generated that depend on each other. For example, I asked to write a hello program in C and compile it. This required a write and compile tool call. However, clearly the write must finish before the compile should start. I can’t find any information about this ordering, how do people handle this? It seems a pity to run all the given commands in one thread? The model’s sole responsibility is to produce the function and its parameters. If Function A depends on the output of Function B, managing that dependency is your task.

-----

-----

Phase: [EXPLORATION]

### Source [53]: https://apxml.com/courses/building-advanced-llm-agent-tools/chapter-3-llm-tool-selection-orchestration/sequential-parallel-tool-use

Query: How does LLM tool calling parallel API orchestration in microservices?

Answer: As your LLM agent becomes more sophisticated, it will often need to use multiple tools to achieve a single, complex goal. The way these tools are executed—whether one after another or several at once—significantly impacts the agent's efficiency and capabilities. Implementing both sequential and parallel tool use enables your agent to tackle more elaborate tasks. Sequential Tool Execution: The Ordered Approach. Agent Decision-Making for Execution Strategy. How does an LLM agent decide whether to use tools sequentially or in parallel? This often involves a combination of:

-----

</details>

<details>
<summary>What robotics control lessons can reshape LLM tool-calling architectures?</summary>

Phase: [EXPLORATION]

### Source [54]: https://acrome.net/post/controlling-robots-with-llms-large-language-models

Query: What robotics control lessons can reshape LLM tool-calling architectures?

Answer: LLMs enable intuitive and flexible control of robots through natural language, translating user prompts into specific robotic actions. This creates a more intuitive interface for controlling robots, simplifying interaction and enabling complex, coordinated movements that are challenging to program directly. Users issue commands in natural language, which the LLM translates into robotic actions, particularly useful for multi-step tasks requiring series of coordinated movements. In a project, user prompts are transferred to a mobile robot, which executes the motion. The application runs on two computational sides, demonstrating versatility across industrial automation, healthcare, service, education, and research, such as remote operation in hazardous environments, patient assistance, customer interaction, interactive learning, and rapid prototyping. This enhances human-robot interaction and robotic system efficiency.

-----

-----

Phase: [EXPLORATION]

### Source [55]: https://www.sciencedirect.com/science/article/abs/pii/S0921889024002975

Query: What robotics control lessons can reshape LLM tool-calling architectures?

Answer: The LLM-controller uses a hybrid approach integrating LLM with a nonlinear controller for dynamic robot control adaptation. The LLM acts as a consultant guiding the controller, not as the controller itself, combining traditional control precision and stability with LLM's generality and contextual understanding. A feedback loop allows the LLM to offer adaptations based on context, addressing LLM limitations like erroneous planning while enhancing controller performance. This is versatile and adaptable to different robotic platforms and control strategies via prompt modifications, applicable in dynamic environments and tasks. Previous works used LLMs to suggest actions for controllers to adopt or reject; this scheme employs feedback for better integration, maintaining accurate performance across scenarios.

-----

-----

Phase: [EXPLORATION]

### Source [56]: https://hrilab.tufts.edu/publications/sarathyetal25acmtist.pdf

Query: What robotics control lessons can reshape LLM tool-calling architectures?

Answer: Traditional robotic architectures used NLP pipelines like Combinatory Categorial Grammar (CCG) to extract semantics and connect action imperatives to function calls. LLMs replace or augment these, breaking high-level instructions into low-level executable plans, code-generation, self-talk, and world tracking. Architectures include: LLM-modular (LLM as one module), LLM-hierarchical (high-level planner), LLM-e2e (LLM replaces all cognitive parts, keeping perception/actuation). LLM-e2e leverages full natural language understanding and reasoning but challenges include generating understandable sensory input and executable outputs, potentially overwhelming LLM with data and removing performance guarantees. Lessons suggest additional components beyond LLM may be needed for improved performance in robotic architectures.

-----

-----

Phase: [EXPLORATION]

### Source [57]: https://hlfshell.ai/posts/llms-and-robotics-papers-2023/

Query: What robotics control lessons can reshape LLM tool-calling architectures?

Answer: In robotics, LLMs enable long-term task planning by generating pseudocode from scene understanding, breaking control into simplified tool calls like robot.pick_and_place('yellow block', 'green bowl'). LLMs act as dynamic routers, handing off subtasks to external tools via specific token sets, including neural, symbolic (function calls), and knowledge base tools. Fine-tuning orients LLMs towards tool use without prompting. ReAct-style patterns (Thought for reasoning like CoT, Act for tool calls like Wikipedia API, Observation for results) form modern AI agents applicable to robotics. This structures LLM outputs for reliable robotic control, expandable to states and other tools beyond language tasks.

-----

-----

Phase: [EXPLORATION]

### Source [58]: https://mikelikesrobots.github.io/blog/llm-robot-control/

Query: What robotics control lessons can reshape LLM tool-calling architectures?

Answer: Robots are controlled via LLMs translating natural language to robot commands using tools (e.g., ROSA library accessing ROS 2 topics). LLMs like Claude supplement robots with extra tools, enabling extension of capabilities for simulated or real robots. Benefits: natural language understanding of intentions, easy addition of new behaviors via tools without recoding, handling complex instructions. Framework allows defining custom tools for upgraded capabilities. Challenges: high compute needs require cloud LLMs. Lessons: structure LLM interactions via defined tools interfacing robot systems, enabling intuitive control and modularity.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agentic-design-patterns-visual-architecture-guide-myengineer.md">
<details>
<summary>Agentic Design Patterns — Visual Architecture Guide</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://myengineeringpath.dev/genai-engineer/agentic-patterns/>

# Agentic Design Patterns — Visual Architecture Guide

Agentic AI design patterns — ReAct, Plan-and-Execute, Reflection, and multi-agent orchestration — are the building blocks GenAI engineers use to architect reliable agent systems. This guide covers each pattern with production implementation details and the trade-offs interviewers expect you to articulate.

## 1\. Why Agentic Design Patterns Matter

Design patterns exist because naive agent implementations fail in predictable ways — unbounded loops, silent tool failures, context exhaustion — and each failure mode has a corresponding structural solution.

### Why Agents Need Design Patterns

A single LLM call is stateless. Given a prompt, it produces a completion. That model is powerful, but insufficient for tasks that require multiple steps, external information, error recovery, or coordination across multiple independent workstreams.

The solution is agents: systems that give the LLM access to tools and allow it to reason across multiple steps before producing a final answer. But agents introduce a new class of engineering problems. How do you structure the reasoning loop? How do you handle tool failures? How do you prevent infinite loops? How do you scale from one agent to many?

Design patterns answer these questions. They are not academic abstractions. They are solutions to failure modes that have been encountered, diagnosed, and solved repeatedly across production GenAI systems. A team that knows these patterns builds more reliable agents faster. A team that does not reinvents them, badly, under deadline pressure.

### The Pattern Library Problem

In 2022, academic papers described techniques like ReAct and Chain-of-Thought, but there was no engineering-level pattern library for agent design. Teams built ad hoc reasoning loops, discovered the failure modes independently, and built ad hoc fixes. By 2024, recognizable patterns had emerged across the industry — LangGraph, AutoGen, CrewAI, and Claude Code all implement variants of the same core patterns. Understanding the patterns lets you reason about these systems independently of the framework implementing them.

### When Design Patterns Apply

Patterns apply whenever an agent needs to handle more than a single-turn request:

- Multi-step tasks with dependencies between steps
- Tasks requiring external data retrieval, calculation, or code execution
- Tasks where output quality is uncertain and requires evaluation
- Tasks that benefit from parallel execution across independent workstreams

For simple single-turn completions, patterns add overhead without value. The pattern selection decision should be driven by the complexity and reliability requirements of the task.

* * *

## 2\. Real-World Problem Context

Understanding why naive agents fail in production — not just that they fail — is the prerequisite for choosing the right pattern to address each failure mode.

### The Failure Modes of Naive Agents

The simplest possible agent implementation: pass the user’s query to the LLM with a list of tools, and ask it to use the tools and answer. This works for demonstrations. In production, it fails in predictable ways.

**Unbounded loops.** Without a termination condition, an agent reasoning about a complex problem may loop indefinitely — calling tools, observing results, calling more tools, never converging. This burns tokens and produces no answer.

**Silent tool failure.** A tool returns an error. The agent sees the error message, decides to try a different tool, encounters a second error, and returns a confident-sounding answer based on no valid data. Nothing in the loop explicitly handles the failure state.

**Context window exhaustion.** A long reasoning chain accumulates observations from multiple tool calls. By step fifteen, the earliest observations have been pushed out of the context window. The agent makes decisions based on incomplete history.

**Scope creep.** Given a task like “analyze this codebase and suggest improvements,” an agent without explicit scope boundaries will read every file, call every available tool, and never deliver a focused answer. The blast radius of the task is undefined.

**No quality feedback.** An agent produces an answer. There is no mechanism to evaluate whether the answer is correct before returning it to the user.

Each of these failure modes has a corresponding design pattern that addresses it. Understanding the problem motivates the pattern.

### The Cost of Getting This Wrong in Production

A customer support agent that loops silently when it cannot find information in the knowledge base will either time out or return a hallucinated answer. A code analysis agent without scope control will read configuration files, lock files, and generated code — diluting the signal with noise. A research agent without a self-evaluation step will return a well-formatted summary of incorrect information.

These problems do not manifest in demos. They manifest when the system encounters the long tail of production inputs.

* * *

## 3\. How Agentic Design Patterns Work

Seven design patterns cover the majority of production agent architectures. They are ordered by increasing complexity and decreasing frequency of use — the first few apply in almost every agent system, the later ones apply in specific contexts.

### Pattern 1: Tool Use (Function Calling)

The foundation of all agent patterns. The LLM is given a schema of available tools — their names, descriptions, and typed input parameters. When the LLM determines that a tool is needed, it emits a structured tool call rather than free text. The framework executes the tool and returns the result to the LLM as an observation.

What makes this a pattern rather than just a feature is the discipline around tool design: tools should have clear names, unambiguous descriptions, and a single responsibility. A tool called `search_documents` that also updates a database is not a well-designed tool. The LLM’s ability to select the right tool depends on clear tool descriptions. Poorly described tools produce incorrect tool selection, which produces incorrect results.

### Pattern 2: ReAct (Reason + Act)

Introduced in a 2022 paper, ReAct interleaves reasoning steps with action steps. Rather than asking the LLM to produce a final answer in one shot, the framework prompts it to emit a `Thought` (explicit reasoning about what to do), an `Action` (a specific tool call), and then observe the `Observation` (the tool’s output). This cycle repeats until the LLM emits a `Final Answer`.

The insight is that explicit reasoning steps improve tool selection and reduce hallucination. The LLM’s `Thought` step forces it to articulate why it is calling a particular tool before calling it, which catches many tool misuse errors before they happen.

ReAct is the default loop in LangGraph, LangChain’s AgentExecutor, and most agent implementations you will encounter in the wild. Understanding it is foundational.

### Pattern 3: Plan-and-Execute

ReAct is a reactive pattern — the agent decides what to do at each step based on the previous observation. For long-horizon tasks, this myopia is a problem: the agent loses sight of the overall goal when intermediate steps are complex.

Plan-and-Execute separates the agent into two components. The **planner** receives the task and produces a complete plan: an ordered list of steps, each with a clear description and success criterion. The **executor** works through the plan step by step, using tools as needed. The planner only runs once (or when replanning is triggered); the executor runs N times.

The advantage: the planner has full task context when creating the plan. The executor has a clear scope for each step. Neither component has to do both jobs simultaneously.

The trade-off: planning errors are expensive. If the planner misunderstands the task, every executor step is working toward the wrong goal. Some implementations add a replanning step — if the executor encounters an unrecoverable failure, it calls the planner again with updated context.

### Pattern 4: Reflexion (Self-Evaluation)

Reflexion adds a self-evaluation loop after the agent produces an output. Rather than returning the output immediately, a separate evaluation step assesses the output against explicit criteria — correctness, completeness, relevance, safety. If the output fails evaluation, the agent revises it and evaluates again, up to a configured maximum number of iterations.

The evaluator can be the same model used for generation (the LLM critiques its own output), a separate smaller model optimized for evaluation, or a deterministic function (a test runner, a syntax checker, a schema validator).

Reflexion is appropriate for tasks with measurable quality criteria. A code generation agent should run the generated code and evaluate whether the tests pass before returning it. A research synthesis agent should evaluate whether the synthesis actually answers the original question. For tasks with no measurable criteria, reflexion adds latency without improving quality.

### Pattern 5: Multi-Agent Delegation

Single agents have a bounded context window and a single thread of execution. Complex tasks benefit from parallelism and specialization.

Multi-agent delegation uses an **orchestrator** agent that decomposes a task and delegates sub-tasks to **worker** agents. Workers can execute in parallel when tasks are independent. Workers can be specialized — a research worker, a code generation worker, a validation worker, each with its own tool set and system prompt.

The orchestrator collects worker outputs and synthesizes a final result. The complexity is in the orchestration logic: how does the orchestrator decide when all workers are done? How does it handle partial failures? How does it pass context between workers who have dependencies?

LangGraph, AutoGen, and CrewAI each provide different models for this — LangGraph as an explicit state machine, AutoGen as conversational turn-taking, CrewAI as role-and-task delegation. The underlying multi-agent pattern is the same.

### Pattern 6: Memory Patterns

By default, LLM agents are stateless between sessions. Memory patterns add persistence:

- **Short-term memory (conversation buffer):** The running message history of the current session. Limited by context window size. Managed automatically in most frameworks.
- **Sliding window memory:** A fixed-length window of the most recent N messages. Prevents context window exhaustion on long conversations.
- **Summary memory:** Periodically summarize the conversation so far and compress it into a shorter representation. Retains key facts while reducing token count.
- **Long-term memory (vector store):** Embed past interactions, facts, or documents into a vector database. Retrieve relevant memories at query time using semantic similarity. Enables agents that “remember” facts across sessions.
- **Episodic memory:** Store the outcomes of past agent tasks. When a similar task is requested in the future, retrieve the previous execution trace as a reference.

Memory pattern selection depends on the task: customer support agents typically use short-term conversation memory with long-term document retrieval; personal assistant agents use summary memory and episodic recall.

### Pattern 7: Guardrail Patterns

Guardrail patterns validate agent inputs and outputs against safety and quality criteria.

**Input validation** checks the user’s request before processing. Is the request within scope? Does it contain prompt injection attempts? Is it relevant to the agent’s domain?

**Output validation** checks the agent’s response before delivering it. Does it reference real information or hallucinated facts? Does it comply with content policies? Does it answer the original question?

**Self-critique** prompts the agent to evaluate its own output against a rubric before returning it. More flexible than deterministic validators but adds latency and token cost.

Production agent systems at scale use all three. Input validation prevents abuse; output validation prevents harm; self-critique catches quality failures that deterministic validators miss.

* * *

## 4\. Implement Each Pattern Step by Step

Building a production agent involves layering these patterns incrementally. The order matters: each layer adds complexity and should only be added when the simpler layer is proving insufficient.

### Step 1: Start with Tool Use

Before building an agent, design your tools. For each external capability the agent needs, define a tool with:

- A clear, action-oriented name (`search_knowledge_base`, not `tool1`)
- A description written for the LLM, not for a human — explain when to use the tool, not just what it does
- Typed input parameters with descriptions
- A clear return format

A common mistake is building the agent first and the tools second. Tools that were designed for the agent are better than tools that were adapted from existing APIs.

### Step 2: Implement the ReAct Loop

The minimal viable agent is a ReAct loop: a system prompt that instructs the LLM to emit Thought/Action/Observation cycles, a loop that executes tool calls and appends observations to the context, and a termination condition that detects a Final Answer.

In LangGraph, this is a graph with one node per step type and a conditional edge that checks whether the LLM has finished. In LangChain, it is an AgentExecutor with a prompt template that encodes the ReAct format.

Before moving to more complex patterns, run this loop on representative inputs. Observe where it fails. Does it select wrong tools? Does it loop? Does it produce incorrect answers? The failure mode determines the next pattern to add.

### Step 3: Add Plan-and-Execute for Long-Horizon Tasks

If the ReAct loop performs well on simple tasks but struggles with multi-step tasks that span many tool calls, add Plan-and-Execute.

The planner is typically a separate LLM call at session start that receives the full task description and produces a structured plan. The plan is stored in state and passed to the executor at each step. The executor’s system prompt instructs it to complete only the current step in the plan, not the entire task.

This separation of concerns dramatically improves performance on complex tasks. It also makes the agent’s behavior more predictable and auditable — you can log the plan and inspect whether each execution step matches the planner’s intent.

### Step 4: Add Reflexion for Quality-Critical Outputs

If the agent produces outputs with measurable quality criteria — code that must run, answers that can be fact-checked, documents that must meet a format specification — add a reflexion loop after the initial generation.

A minimal reflexion implementation runs the output through a validation function and, if validation fails, appends the validation result as a new observation and asks the agent to revise. Cap the retry loop at three iterations to prevent infinite refinement.

More sophisticated implementations use a separate evaluator model that produces a structured evaluation: what was good, what was wrong, what should be changed. This structured feedback is more useful to the generator than a raw error message.

### Step 5: Introduce Multi-Agent for Parallel Workloads

If the task naturally decomposes into independent sub-tasks that could run in parallel, and the single-agent loop is a bottleneck, introduce multi-agent delegation.

Start with the simplest possible decomposition: an orchestrator that generates a list of sub-tasks, a pool of identical worker agents that each execute one sub-task, and a synthesis step that combines results. Only introduce specialized workers when the evidence shows that different sub-tasks benefit from different tools or system prompts.

Multi-agent systems are significantly harder to debug than single-agent systems. Instrument every worker invocation with tracing (LangSmith or equivalent) before deploying to production.

* * *

## 5\. Agentic Pattern Architecture

The four primary patterns — Tool Use, ReAct, Plan-and-Execute, and Multi-Agent — form a complexity ladder where each tier addresses the limitations of the tier below it.

### Pattern Complexity vs. Task Complexity

The patterns are not mutually exclusive — production systems combine them. A research agent might use Plan-and-Execute as the outer loop, ReAct within each executor step, Reflexion before delivering the synthesis, and a multi-agent architecture for parallel source retrieval.

The diagram below maps the four primary structural patterns by their complexity and the task characteristics that motivate them.

### 📊 Visual Explanation

Agentic Pattern Complexity Tiers

Patterns layered by task complexity and reliability requirements

Pause

Tool Use

Single-step

User Request

Tool Selection

Tool Execution

Return Result

ReAct Loop

Multi-step

Thought

Action (Tool Call)

Observation

Repeat or Answer

Plan + Execute

Long-horizon

Planner: Full Plan

Executor: Step 1

Executor: Step N

Synthesize Output

Multi-Agent

Parallel / Specialized

Orchestrator

Worker A

Worker B

Aggregate Results

Idle

Each tier builds on the previous: a multi-agent system typically uses ReAct within each worker and may use Plan-and-Execute at the orchestrator level. Reflexion can be applied at any tier as a quality gate before output is returned.

### Where Each Pattern Adds Value

**Tool Use alone** is sufficient for retrieval-augmented QA, document classification, and single-step API calls. Adding a ReAct loop to a single-tool agent adds overhead without benefit.

**ReAct** is the right default for tasks that require 2–8 sequential steps with observable intermediate results. It handles the majority of production agent use cases.

**Plan-and-Execute** is appropriate when tasks have 10+ steps, when the steps have dependencies that are only visible from a full-task view, or when the ReAct loop is failing due to myopic step selection.

**Multi-Agent** is appropriate when sub-tasks are independent and can run in parallel, when specialized tool sets or system prompts improve quality on different sub-task types, or when a single agent’s context window is insufficient for the full task.

* * *

## 6\. Agentic Pattern Code Examples

The three examples below show minimal working implementations of ReAct, Plan-and-Execute, and Reflexion — each demonstrating the key design decision that makes the pattern work in practice.

### Example: ReAct Agent in Python with LangGraph

The following implements a minimal ReAct agent with two tools using LangGraph’s `create_react_agent` helper.

```
from langchain_anthropic import ChatAnthropic

from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent

@tool

def search_knowledge_base(query: str) -> str:

    """Search the internal knowledge base for information relevant to the query.

    Use when the user asks about company policies, product details, or FAQs.

    """

    # In production: call your vector store retrieval API

    return f"Knowledge base result for: {query}"

@tool

def lookup_order_status(order_id: str) -> str:

    """Look up the current status of a customer order by order ID.

    Use when the user provides an order number and asks about delivery status.

    """

    # In production: call your order management system API

    return f"Order {order_id}: Shipped, estimated delivery 2 days"

model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

tools = [search_knowledge_base, lookup_order_status]

# create_react_agent handles the Thought/Action/Observation loop internally

agent = create_react_agent(model, tools)

result = agent.invoke({

    "messages": [{"role": "user", "content": "Where is order #12345?"}]

})

print(result["messages"][-1].content)
```

Key points in this example: tool descriptions are written for the LLM (they explain when to use the tool, not just what it does), the agent loop is fully managed by `create_react_agent`, and the model receives only the final assembled messages — you do not manage Thought/Action/Observation formatting manually when using LangGraph.

### Example: Plan-and-Execute with Explicit Plan State

```
from langchain_anthropic import ChatAnthropic

from langchain_core.messages import HumanMessage, SystemMessage

model = ChatAnthropic(model="claude-sonnet-4-5-20250929")

def generate_plan(task: str, tools: list[str]) -> list[str]:

    """Planner: produce an ordered list of steps to complete the task."""

    response = model.invoke([\
\
        SystemMessage(content=(\
\
            "You are a task planner. Given a task and available tools, "\
\
            "produce a numbered list of concrete steps to complete the task. "\
\
            f"Available tools: {', '.join(tools)}"\
\
        )),\
\
        HumanMessage(content=task),\
\
    ])

    # Parse the numbered list from the response

    lines = response.content.strip().split('\n')

    return [l.strip() for l in lines if l.strip() and l[0].isdigit()]

def execute_step(step: str, context: str, agent) -> str:

    """Executor: complete one step, given accumulated context."""

    result = agent.invoke({

        "messages": [{\
\
            "role": "user",\
\
            "content": f"Context so far:\n{context}\n\nComplete this step only: {step}"\
\
        }]

    })

    return result["messages"][-1].content

# Usage

task = "Analyze the quarterly sales data and produce a summary with key trends."

tools_available = ["read_csv_file", "calculate_statistics", "generate_chart"]

plan = generate_plan(task, tools_available)

context = ""

for step in plan:

    result = execute_step(step, context, agent)

    context += f"\n{step}: {result}"
```

This separates planning from execution cleanly. The planner has full task context; the executor has one job per invocation.

### Example: Reflexion Loop for Code Generation

```
import subprocess

def generate_and_validate(task: str, max_retries: int = 3) -> str:

    """Generate code and iteratively refine it until tests pass."""

    feedback = ""

    for attempt in range(max_retries):

        prompt = task if not feedback else f"{task}\n\nPrevious attempt failed:\n{feedback}\nFix the issues."

        code = model.invoke([HumanMessage(content=prompt)]).content

        # Reflexion: run the code and check for errors

        result = subprocess.run(

            ["python", "-c", code],

            capture_output=True, text=True, timeout=10

        )

        if result.returncode == 0:

            return code  # Passed — return the working code

        # Build structured feedback for the next attempt

        feedback = f"Error (attempt {attempt + 1}/{max_retries}):\n{result.stderr}"

    return code  # Return best attempt after max retries
```

The key design decision: the feedback passed back to the model is the raw error output, not a paraphrase. The model responds better to exact error messages than to summaries.

* * *

## 7\. Pattern Trade-offs and Pitfalls

Each pattern layer adds latency and cost; the failure modes below — stale plans, infinite ReAct loops, multi-agent coordination errors, and evaluator bias — are the specific problems to design against.

### Complexity vs. Reliability Trade-off

Each pattern layer adds latency and cost. A ReAct loop that runs 8 iterations before answering costs 8× the tokens of a single completion. Plan-and-Execute adds a separate planning call. Reflexion adds evaluation and revision calls. Multi-agent multiplies costs by the number of workers.

The trade-off is not complexity vs. simplicity. It is cost vs. reliability. Add pattern layers when the simpler approach is demonstrably failing, not preemptively. Over-engineering an agent system creates latency and cost overhead with no reliability gain.

### Plan-and-Execute: The Stale Plan Problem

Plans become stale when execution encounters unexpected intermediate states. An agent tasked with “refactor the authentication module” produces a plan assuming the module uses JWT. Midway through execution, it discovers the module uses session cookies. The plan is now incorrect, but the executor has no mechanism to signal this to the planner.

Solutions: trigger replanning when an executor step fails or produces unexpected output; include an explicit “check plan validity” step in the plan; design plans at a higher level of abstraction that accommodates variation in execution.

### ReAct: The Loop-Until-Timeout Anti-Pattern

Without a maximum step count, a ReAct agent that cannot find the answer to a query will continue calling tools indefinitely. Always configure a maximum iteration count. When the limit is reached, return the best available answer with an explicit signal that the response may be incomplete — do not return nothing.

### Multi-Agent: The Coordination Overhead Problem

Multi-agent systems require explicit interfaces between agents. The orchestrator must produce sub-task descriptions that worker agents can interpret without ambiguity. Workers must return outputs in formats the orchestrator can consume. The more specialized the workers, the higher the coordination overhead.

The failure mode: a worker returns a partial result in an unexpected format. The orchestrator misinterprets it. The synthesis step aggregates misinterpreted results. The final output is incorrect, but the error is invisible in the individual worker outputs.

Mitigation: define typed interfaces for all orchestrator/worker communication; require workers to return structured outputs (JSON schemas, Pydantic models); validate worker outputs before aggregation.

### Reflexion: The Evaluation Quality Problem

Reflexion is only as good as the evaluator. An LLM evaluating its own output will often give itself high marks — the same biases that produced the original output bias the evaluation. A separate evaluator model with a different training objective is significantly more reliable.

For code: use a syntax checker and test runner (deterministic validators) rather than LLM self-evaluation. For factual accuracy: use retrieval to verify claims rather than asking the model if its claims are correct.

* * *

## 8\. Agentic Design Patterns Interview Prep

Agentic design patterns are asked with increasing frequency at AI-native companies and at any organization building production LLM systems.

**“What is the ReAct pattern and why does it exist?”** The expected answer covers the interleaving of reasoning and action, why it improves tool selection compared to single-shot tool use, and a concrete example of a Thought/Action/Observation cycle. Mentioning the 2022 paper origin signals depth but is not required. What is required: you can explain what the LLM emits at each step and how the framework processes it.

**“How would you design an agent for a complex research task?”** This question expects a pattern selection decision, not a framework selection decision. Strong answers: “I would start with Plan-and-Execute because research tasks have many interdependent steps and a single ReAct loop would lose track of the overall goal. Within each executor step I’d use a ReAct sub-loop for tool use. Before returning the synthesis I’d add a Reflexion step to verify that the output actually answers the original question.” Weak answers name a framework without explaining the underlying architecture.

**“What happens when an agent gets stuck in a loop?”** This tests operational knowledge. The answer should cover: maximum iteration limits as a hard stop, distinguishing between loops caused by tool failure (handle the failure explicitly) vs. loops caused by task ambiguity (return partial answer with explanation), and logging/tracing to detect loops in production.

**“How do you evaluate whether your agent is working?”** Expected: unit tests for individual tools, integration tests with representative inputs and expected outputs, Reflexion loops for quality-critical outputs, LangSmith or equivalent for production traces, and latency/cost monitoring per agent invocation.

* * *

## 9\. Agentic Patterns in Production

Production agent systems succeed through disciplined practices — starting simple, instrumenting everything, versioning prompts, and designing explicit fallbacks for every failure path.

### Start with Single-Agent, Multi-Pattern

The most common production architecture is a single agent that layers multiple patterns: ReAct as the base loop, Plan-and-Execute for complex tasks, Reflexion before delivery for quality-critical outputs. This is simpler to deploy, monitor, and debug than a multi-agent system. Introduce multi-agent only when the single-agent architecture has a documented bottleneck that multi-agent solves.

### Instrument Everything

Every agent invocation in production should be traced: which tools were called, in what order, what they returned, how many ReAct iterations occurred, whether Reflexion triggered revision. LangSmith, Phoenix (Arize), and Weights & Biases support LLM tracing. Without tracing, debugging production failures is blind.

The specific metrics to track per agent invocation: total latency, tool call count, Reflexion iteration count, final answer token count, and a quality score if you have an evaluation function. Aggregate these metrics over time to detect degradation.

### Version Your Prompts

The system prompt and tool descriptions are the primary control surfaces for agent behavior. They are as important as application code and should be treated as such: version-controlled, reviewed in pull requests, and updated based on production failure analysis. A silent change to a tool description can break tool selection across every downstream invocation.

### Design for Graceful Degradation

Agents fail. Tools time out, LLM APIs return rate limit errors, retrieved documents are stale. Design each pattern layer with an explicit fallback:

- ReAct: if the maximum iteration count is reached, return best-available partial answer with a “may be incomplete” flag
- Plan-and-Execute: if replanning fails, fall back to ReAct on the original task
- Tool Use: if the primary tool fails, use a fallback tool if available; if not, continue without that tool and flag the gap in the response
- Multi-Agent: if a worker fails, omit that sub-task from synthesis and flag the gap

A graceful degradation story is part of the production credibility of any agent system.

* * *

## 10\. Summary & Key Takeaways

Seven design patterns cover the majority of production agent architectures:

**Tool Use** is the foundation. All other patterns depend on well-designed tools with clear descriptions and typed interfaces.

**ReAct** is the default loop for most agents. It handles multi-step tasks by interleaving explicit reasoning with action. It is sufficient for the majority of production use cases.

**Plan-and-Execute** adds robustness for long-horizon tasks by separating planning from execution. Use it when ReAct is failing due to myopic step selection, not preemptively.

**Reflexion** adds quality assurance by evaluating outputs and triggering revision. Prefer deterministic validators (test runners, schema validators) over LLM self-evaluation where possible.

**Multi-Agent** enables parallelism and specialization. Adds significant coordination complexity. Introduce only when a single agent has a documented bottleneck.

**Memory Patterns** add persistence across steps and sessions. Choose the memory type based on what the agent needs to remember: short-term conversation buffer for current session, vector store retrieval for long-term knowledge.

**Guardrail Patterns** protect against misuse and quality failures. Input validation prevents abuse; output validation prevents harm; self-critique catches quality gaps.

**Key takeaways:**

- Pattern selection should be driven by observed failure modes, not architectural preference. Add complexity when the simpler approach is demonstrably insufficient.
- ReAct is sufficient for most production agent tasks. Most agents do not need Plan-and-Execute or multi-agent coordination.
- Always configure maximum iteration limits. Unbounded reasoning loops are the most common production failure mode in agent systems.
- Instrument every agent invocation. Without traces, production debugging is impossible.
- Version your prompts and tool descriptions with the same discipline as application code.
- Graceful degradation is a requirement, not a nice-to-have.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-production-ready-llm-applications-bulletproof-llm-t.md">
<details>
<summary>Building Production-Ready LLM Applications: Bulletproof LLM Tool Calling with Advanced JSON Validation and Retry Strategies</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/@hariomshahu101/building-production-ready-llm-applications-bulletproof-llm-tool-calling-with-advanced-json-b95ce8889f4e>

# Building Production-Ready LLM Applications: Bulletproof LLM Tool Calling with Advanced JSON Validation and Retry Strategies

Hariom Sahu

5 min read

·

Jul 20, 2025

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*mpbHKUGURJU0y6yxoEhVpA.png

## The Critical Challenge: LLM Tool Calling in Production

As AI agents become the backbone of enterprise automation, one critical challenge emerges that many teams discover only after deployment: **LLM tool calling is inherently unreliable**. While LLMs excel at understanding context and reasoning about when to call functions, they struggle with the rigid JSON structure and parameter validation that production systems demand.

Consider this scenario: Your AI agent needs to call a weather API, but instead of proper JSON arguments, your application receive:

```
{
  "function_name": "get_weather",
  "arguments": "location=Paris,country=France"  // String instead of object!
}
```

Or worse:

````
//  content wrapped in Markdown code block markersjson
```json
{
"city": "Paris",
"temp_unit": celsius
}
```
````

These malformed tool calls break your entire function execution pipeline. In production environments where reliability is paramount, such inconsistencies cascade into system failures, incomplete workflows, and frustrated users trying to accomplish tasks through your AI interface.

The harsh reality: LLM tool calling fails JSON validation often in real-world applications.

### **The Foundation: Why Proper Tool Definition Matters Before diving into sophisticated retry mechanisms, let’s address the elephant in the room:**

precise tool definitions and prompting are your first line of defense.

The Wrong Way: Vague Tool Schema

```
{
  "name": "get_weather",
  "description": "Get weather info",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {"type": "string"}
    }
  }
}
```

The Right Way: Explicit Tool Schema

```
{
  "name": "get_weather",
  "description": "Get current weather conditions for a specific city",
  "parameters": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City name exactly as: 'City, Country' (e.g., 'Paris, France')"
      }
    },
    "required": ["location"],
    "additionalProperties": false
  }
}
```

### **System Prompt Engineering for Tool Calling:**

```
Respond only with a minified JSON object matching this schema:
'{"location": ""}'

Do not include any Markdown formatting, code block markers, explanations,
or extra text.

You are a function-calling assistant. When calling functions:
1. ALWAYS use the exact parameter names specified in the schema
2. NEVER add extra properties not defined in the schema
3. ENSURE all required parameters are included
4. VALIDATE parameter types match the schema exactly
5. If unsure about a parameter value, ask for clarification instead of guessing

Example correct function call:
{"name": "get_weather", "arguments": {"location": "New York, USA"}}
```

**Key Tool Definition Principles:**

1. Explicit Parameter Descriptions: Specify exact format expectations
2. Strong Type Constraints: Use specific types and validation rules
3. Required Field Marking: Clearly mark mandatory parameters
4. Disable Additional Properties: Prevent unexpected fields
5. Provide Clear Examples: Show exact expected input format
6. Validate in Real-Time: Implement immediate feedback loops

**The Temperature Factor:**

Lower temperatures (0.1–0.3) increase consistency but may reduce creativity. For structured outputs like JSON, this trade-off is usually worth it. However, when retries are needed, gradually increasing temperature can help generate different, potentially valid outputs.

### Beyond Prompting: The Fine-Tuning Alternative

While prompt engineering is crucial, there’s a more robust long-term solution: **fine-tuning your LLM on function calling datasets**.

**Why Fine-Tuning Matters:**

1. Consistency: Models learn to consistently follow function calling patterns
2. Accuracy: Significantly reduces malformed JSON outputs
3. Efficiency: Reduces token usage and API costs
4. Reliability: Creates more predictable behavior in production

**Popular Function Calling Datasets:**

- Gorilla API Dataset: 16k+ API calling examples
- ToolBench: Multi-step tool usage scenarios
- Berkeley Function Calling Dataset: Real-world function schemas
- Custom Domain Datasets: Industry-specific tool calling patterns

**When to Consider Fine-Tuning:**

- Tool calling accuracy below 85%
- High-volume production applications
- Domain-specific function calling needs
- Long-term cost optimization goals

## Implementing the Three-Stage Architecture: A Step-by-Step Guide

Here’s how to implement the three-stage retry architecture that transforms unreliable tool calling into more reliable system.

### Stage 1: LLM API Call Management

**Objective**: Ensure reliable communication with the LLM service and generate valid tool call responses.

**Implementation Steps**:

1.  **Configure Retry Parameters**

    - Set maximum retry attempts (typically 3–4)
    - Define base delay and exponential backoff multiplier
    - Configure temperature adjustment increments for response variation

2.  **Error Classification System**

    - Network errors (connection failures, DNS issues, socket errors)
    - Timeout errors (request timeouts, service unavailability)
    - Rate limiting (429 errors, quota exceeded)
    - API service errors (500, 503, temporary outages)

3.  **Intelligent Response Generation**

    - Start with base temperature (e.g., 0.5)
    - Increment temperature on each retry (+0.1) to generate different responses
    - Apply exponential backoff with jitter to prevent thundering herd
    - Track retry history with timestamps and error details

4.  **Success Validation**

    - Verify response contains expected tool calls structure
    - Ensure response format matches API specifications
    - Log successful attempts and retry statistics

### Stage 2: JSON Validation and Parameter Checking

**Objective**: Validate tool call structure and parameters before function execution.

**Implementation Steps**:

1.  **Function Existence Verification**

    - Check if the called function exists in available functions registry
    - Validate function name matches exactly (case-sensitive)
    - Ensure function is accessible and properly imported

2.  **JSON Structure Validation**

    - Parse function arguments from JSON string
    - Handle malformed JSON with descriptive error messages
    - Validate JSON syntax and structure integrity

3.  **Parameter Schema Validation**

    - Extract function signature using introspection
    - Identify required vs optional parameters
    - Check for missing required parameters
    - Validate parameter types and constraints
    - Remove unexpected or invalid parameters

4.  **Advanced Validation with Pydantic**

    - Define schema models for each function
    - Implement type validation and constraints
    - Validate parameter formats (dates, emails, patterns)
    - Provide detailed validation error messages

5.  **Retry with Error Feedback**

    - Generate specific error context for LLM
    - Include function examples and correct schema
    - Increase temperature for different JSON generation
    - Re-call LLM with corrected instructions

### Stage 3: Tool Execution with Resilience

**Objective**: Execute validated functions with robust error handling and recovery.

**Implementation Steps**:

1.  **Pre-execution Setup**

    - Initialize function-specific retry configurations
    - Set up monitoring and logging for tool execution
    - Prepare fallback strategies for critical functions

2.  **Function Execution Management**

    - Execute validated function with parsed arguments
    - Implement timeout controls for long-running operations

3.  **Error Classification and Handling**

    - Network errors (API timeouts, connection failures)
    - Service unavailability (503, 500 status codes)
    - Rate limiting from external APIs
    - Data validation errors from external services
    - Authentication and authorization failures

4.  **Adaptive Retry Strategies**

    - Apply faster retry cycles (0.5s base delay)
    - Use function-specific retry limits
    - Implement circuit breaker patterns for failing services
    - Escalate to manual fallbacks for critical failures

**Complete Implementation Available**: The full working code for this three-stage retry architecture is available in our GitHub repository.

[https://github.com/hariomshahu/LLMs\_Tool\_Calling](https://github.com/hariomshahu/LLMs_Tool_Calling)

[LLM](https://medium.com/tag/llm?source=post_page-----b95ce8889f4e---------------------------------------)

[AI](https://medium.com/tag/ai?source=post_page-----b95ce8889f4e---------------------------------------)

[Llm Finetuning](https://medium.com/tag/llm-finetuning?source=post_page-----b95ce8889f4e---------------------------------------)

[Prompt Engineering](https://medium.com/tag/prompt-engineering?source=post_page-----b95ce8889f4e---------------------------------------)

[Generative Ai Tools](https://medium.com/tag/generative-ai-tools?source=post_page-----b95ce8889f4e---------------------------------------)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="connected-context-and-persistent-memory-neo4j-providers-for-.md">
<details>
<summary>Connected Context and Persistent Memory: Neo4j Providers for the Microsoft Agent Framework</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://neo4j.com/blog/agentic-ai/connected-context-and-persistent-memory-neo4j-providers-for-the-microsoft-agent-framework/>

# Connected Context and Persistent Memory: Neo4j Providers for the Microsoft Agent Framework

https://dist.neo4j.com/wp-content/uploads/20260416113842/Ryan-Knight-150x150.png

https://dist.neo4j.com/wp-content/uploads/20260416113658/George-Bittencourt-150x150.jpeg

[Ryan Knight](https://neo4j.com/blog/contributor/ryan-knight/),

[George Bittencourt](https://neo4j.com/blog/contributor/george-bittencourt/)

April 16, 2026

19 min read

https://dist.neo4j.com/wp-content/uploads/20251215093031/1-blog-resources-neo4j-integration.webp

Standard RAG retrieves document chunks by semantic similarity. Ask about Apple’s risk exposure in SEC 10-K filings, and vector search returns the right paragraphs but misses the connections between them. A chunk mentioning competitive pricing surfaces separately from product categories, separately from geographic dependencies. The retriever can’t traverse from a filing excerpt to the company that filed it, to the risk factors it faces, and the products it sells. A knowledge graph solves this by storing connections between unstructured text and the structured entities around it, so retrieval follows relationships rather than relying solely on similarity.

A second gap compounds the first. Without persistent memory, every conversation starts from zero. An agent has no record of what the user explored in prior sessions, what preferences they expressed, or which entities already surfaced. Continuity across sessions doesn’t exist.

These are two distinct problems, one of retrieval and one of memory, and they call for different architectural responses.

The Microsoft Agent Framework is an open-source SDK and runtime for building AI agents in Python and NET. Agents invoke external tools through a standardized interface, whether those tools are local functions, REST APIs, or MCP servers. They form workflows in which multiple specialized agents collaborate on complex tasks, using a graph-based architecture that routes data along typed edges between components. The framework runs locally for development and integrates with Microsoft Foundry for production deployment with tracing and metrics.

The framework provides two complementary building blocks for data access: tools and context providers. Tools let an agent take explicit actions during a conversation turn by calling APIs, querying databases, or executing code. Context providers operate around the turn. They inject knowledge before the model runs and persist information after it responds, without the agent needing to request either. Neo4j addresses both gaps through two context providers built on this interface, one for knowledge graph retrieval and one for agent memory.

## Two Neo4j Context Providers

What makes a graph database practical for these agent workloads is that graph traversal and semantic search are combined into a single operation. Neo4j includes built-in vector search, so a single query can find the most relevant text chunks based on embedding similarity, then expand through graph relationships to collect structured context such as products, risk factors, and geographic exposure, without a separate retrieval step for each. The pattern applies wherever relationships carry meaning: financial filings linking companies to risks, supply chains connecting parts through assemblies, compliance networks mapping regulations to dependencies.

The [**Neo4j Context Provider**](https://github.com/neo4j-labs/neo4j-maf-provider) (a knowledge graph retriever) addresses the first gap in the opening scenario: accessing the risk factors and products that lie beyond the top-k chunks. It searches a Neo4j database and traverses the graph to return structured company data, including products, risk factors, and filing metadata, alongside the text chunks that vector search found. This provider is stateless. It reads from the graph but doesn’t write to it. The knowledge it surfaces comes from data that was loaded independently: SEC filings, product catalogs, maintenance records, whatever the graph contains.

The [**Neo4j Agent Memory**](https://github.com/neo4j-labs/agent-memory) provider addresses the second gap by ensuring that session twelve builds on sessions one through eleven. It stores conversation history, extracts entities and relationships from messages, records user preferences, and logs reasoning traces. On each turn, it injects relevant memories from prior conversations alongside the current context. Unlike the knowledge retriever, the memory provider writes to the graph on every interaction. The graph grows as the agent converses, building a personalized knowledge base that compounds over time.

Either context provider can be used independently, or both can be attached to the same agent simultaneously. The knowledge retriever brings domain expertise from a curated knowledge graph. Agent memory brings continuity and personalization from the agent’s interaction history. Together, they give the agent access to what it needs to know and what it has already learned.

https://dist.neo4j.com/wp-content/uploads/20260416124407/maf-agent-flow-748x1024.png

## How the Knowledge Graph Context Provider Works

The knowledge retriever delegates all searches to the neo4j-graphrag Python library, which provides tested components for vector, full-text, and hybrid search. The provider acts as an adapter between that library and MAF’s context provider interface.

When a user sends a message, the provider executes a five-step sequence:

1.  **Filter messages.** Keep only the most recent user and assistant messages from the conversation, typically the last 10 turns. System messages contain instructions, not searchable content.
2.  **Build a query.** Concatenate the filtered text into a single search string. Including conversational context helps the search stay relevant when the current message references something mentioned earlier.
3.  **Execute the search.** Run the query against a configured Neo4j index. For vector search, the provider embeds the query text and finds nodes with similar embeddings ranked by cosine similarity. For full-text search, the query passes to Neo4j’s BM25 scoring algorithm. The hybrid mode runs both and combines the results.
4.  **Traverse the graph.** If a retrieval\_query is configured, execute it against each matched node. This Cypher query follows relationships from matched nodes to related entities and returns structured metadata alongside the original text. Without a retrieval query, the provider returns raw search results, which works well for simpler use cases where graph traversal isn’t needed.
5.  **Format and inject.** Package the results as messages that the framework injects into the conversation. Each result includes its relevance score, metadata fields from the retrieval query, and the text content.

The model receives the user’s question alongside formatted search results and uses them to respond. It doesn’t know the results came from Neo4j.

The context provider offers multiple retrieval patterns, all based on the neo4j-graphrag Python library. These include:

-   **VectorRetriever** — semantic similarity search using embeddings
-   **VectorCypherRetriever** — vector search followed by a Cypher graph traversal that collects structured metadata from connected entities
-   **HybridRetriever** — combines vector and fulltext (BM25) search
-   **HybridCypherRetriever** — hybrid search followed by a Cypher graph traversal
-   **FulltextRetriever** — keyword-based BM25 search

The Cypher variants add a graph traversal step after the initial search, following relationships from matched nodes to related entities. This design means graph enrichment is an upgrade path, not a commitment. Start with basic vector search and add a retrieval query later without changing agent code.

## Configuring Graph-Enriched Retrieval

Graph-enriched retrieval is where the true power of GraphRAG lies: semantic search finds relevant text chunks, and graph traversal surfaces the structured context around them. This is configured with a retrieval query, a Cypher query that runs after the vector search and defines which relationships to traverse, what metadata to collect, and how to structure the results the agent receives.

The example below shows how this would work with a knowledge graph built from SEC filings, where document chunks link to documents, documents link to companies, and companies link to products and risk factors. The following retrieval query would then be part of the context provider configuration.The query receives two variables from the vector search: node (the matched chunk) and score (its similarity ranking). From there, it walks the graph. The first MATCH follows the chain from the chunk to its parent document to the company that filed it. Two OPTIONAL MATCH clauses then collect related entities, risk factors, and products, in separate passes to avoid the cross-product duplication that would occur if both were matched in a single clause. Each collection is capped at five items. The WHERE score IS NOT NULL filter removes any rows that lost their score during the optional matching. The final RETURN assembles a flat result with the original text, the similarity score, and the structured metadata the agent will use.

RETRIEVAL\_QUERY = “””

MATCH (node)-\[:FROM\_DOCUMENT\]->(doc:Document)<-\[:FILED\]-(company:Company)

OPTIONAL MATCH (company)-\[:FACES\_RISK\]->(risk:RiskFactor)

WITH node, score, company, doc,

     collect(DISTINCT risk.name)\[0..5\] AS risks

OPTIONAL MATCH (company)-\[:MENTIONS\]->(product:Product)

WITH node, score, company, doc, risks,

     collect(DISTINCT product.name)\[0..5\] AS products

WHERE score IS NOT NULL

RETURN

    node.text AS text,

    score,

    company. name AS company,

    company.ticker AS ticker,

    risks,

    products

ORDER BY score DESC

“””

The provider configuration points at a Neo4j vector index and passes the retrieval query. The key architectural choices are index\_type, which selects the search strategy, retrieval\_query, which triggers graph traversal after search, and top\_k, which controls how many chunks the initial search returns before the Cypher traversal runs against each one.

    provider = Neo4jContextProvider(

    …

    index\_name=”chunkEmbeddings”,

    index\_type=”vector”,

    retrieval\_query=RETRIEVAL\_QUERY,

    top\_k=5,

)

Attaching the provider to an agent is a single configuration step. The context\_providers list determines which providers run on every turn.

agent = Agent(

    client=client,

    name=”company-analyst”,

    instructions=”You answer questions about companies using graph-enriched context.”,

    context\_providers=\[provider\],

)

## How Graph Traversal Changes What the Agent Sees

The configuration above points at a vector index and adds a retrieval query for graph traversal. To see what that retrieval query changes, consider the same question run both ways: first with vector search alone, then with the graph traversal applied after it. The underlying search is identical. The difference is what the agent receives.

### Vector Search Only

The retriever returns text chunks ranked by cosine similarity. These are relevant paragraphs, but disconnected fragments:

Result 1 (score: 0.92):

“The Company’s products and services include iPhone, Mac, iPad, Wearables,

Home and Accessories, and services including advertising, AppleCare, cloud

services, digital content, and payment services…”

Result 2 (score: 0.87):

“The Company competes in markets that are highly competitive and subject to

aggressive pricing. The markets for the Company’s products and services are

characterized by frequent product introductions and rapid technological

advances that have substantially increased the capabilities of computing,

communication, and electronic devices…”

The agent responds with what it can piece together from those chunks:

Apple offers products including iPhone, Mac, iPad, and Wearables, Home, and

Accessories. They also provide services such as AppleCare and cloud services.

In terms of risks, Apple operates in highly competitive markets with aggressive

pricing and frequent product introductions.

The answer is partial. The agent found products in chunk 1 and mentions competition from chunk 2, but specific risk factors like geography, short product life cycles, and evolving industry standards weren’t in the top-k chunks, so they’re missing from the response entirely.

### Graph-Enriched Retrieval

The same vector search finds the same chunks. But the retrieval query then traverses the graph, following relationships from chunks to the company node, then to connected products and risk factors:

Result 1 (score: 0.92):

text: “The Company’s products and services include iPhone, Mac, iPad…”

company: Apple Inc.

ticker: AAPL

products: \[iPhone, Mac, iPad, Wearable,s Home and Accessories, App Store\]

risks: \[Geography, Aggressive Price Competition, Frequent Introduction\
\
          of New Products, Short Product Life Cycles, Evolving Industry Standards\]

The agent now has a structured context and responds comprehensively:

Apple Inc. (Ticker: AAPL) offers a range of products, including:

– iPhone

– Mac

– iPad

– Wearables, Home, and Accessories

– App Store

The company faces several risks, including:

1\. Geography: Risks related to how complex and changing laws impact

global operations.

2\. Aggressive Price Competition: Competitors often use aggressive pricing

strategies that can put downward pressure on Apple’s gross margins.

3\. Frequent Introduction of New Products: The need to continuously introduce

Innovative products place pressure on Apple’s resources and operations.

4\. Short Product Life Cycles: Apple’s products may become obsolete quickly,

necessitating rapid development cycles.

5\. Evolving Industry Standards: Keeping up with changes in industry standards

can affect product design and sales.

Same vector search, same top-k chunks. The difference is what happens after the search. The retrieval query traverses the graph and surfaces a structured context that the agent can reason over.

Graph-enriched retrieval addresses the first gap identified in the opening: reaching entities beyond the top-k chunks. But the second gap remains. The agent still has no memory of prior sessions, no record of what the user has already explored, and no accumulated preferences. Each conversation starts from zero.

## How Neo4j Agent Memory Works

Neo4j Agent Memory closes this second gap. Where the knowledge retriever gives an agent access to a curated knowledge base, the memory provider enables it to learn from its own conversations.

The Neo4j Agent Memory provider implements MAF’s context-provider interface, with both before\_run and after\_run hooks. Before the model runs, it gathers relevant memories and injects them as context. After the model responds, it persists the new messages, extracts entities and relationships, and optionally records reasoning traces. The graph grows with every conversation.

On each turn, the before\_run hook assembles context from three memory types. It pulls recent messages from the current session along with semantically similar messages from past sessions. It retrieves user preferences and relevant entities from long-term memory. It finds similar past tasks from the reasoning trace store. All of this is formatted and injected into the agent’s context window alongside whatever the knowledge retriever contributed.

The after\_run hook handles persistence. It saves the new user and assistant messages, along with their embeddings, for future semantic search. It runs entity extraction over the conversation text, identifying people, organizations, locations, and other entities, and writes them to the graph with relationships linking them back to the messages that mentioned them. Entity extraction can run asynchronously, so it doesn’t block the response.

## What Neo4j Agent Memory Stores

The memory provider organizes knowledge into three layers, each serving a different temporal and structural purpose.

**Short-term memory** captures the conversation itself. When the analyst asks about Apple’s supply chain exposure in session twelve, the provider surfaces a relevant exchange from session three about semiconductor sourcing, even though the two conversations used different terminology. Messages are stored as nodes linked in sequence by NEXT\_MESSAGE relationships, grouped under a Conversation node for the session. Each message carries an embedding vector, enabling semantic search across the full conversation history.

**Long-term memory** structures the knowledge that accumulates across conversations. The system knows this analyst focuses on risk exposure rather than dividend yield, and that “Apple” and “Apple Inc.” refer to the same entity. It stores four types of information. Entities follow the POLE+O classification — Person, Organization, Location, Event, and Object — a taxonomy that provides consistent entity typing across extraction methods. The extraction pipeline supports domain-specific schemas beyond POLE+O for specialized use cases, including scientific, medical, legal, and business contexts. Entities are extracted from conversations, deduplicated using a combination of embedding similarity and fuzzy string matching, and connected through typed relationships. Preferences capture what the user cares about, categorized by topic. Facts represent subject-predicate-object triples with temporal validity, recording that a company appointed a new CEO effective on a specific date. Relationships between entities are first-class objects, linking a company to its products, a person to their role, or a risk factor to the geography it affects.

**Reasoning memory** records how the agent has worked, not just what it discussed. When a similar company-risk analysis arrives, the provider surfaces the prior approach: the tools used, the structure used, and whether it succeeded. Each task execution is stored as a ReasoningTrace containing the individual steps the agent took, their arguments and results, and the outcome. These traces carry embeddings of the task description, so when a similar request arrives in a future session, the provider can surface the prior approach.

(:Conversation)-\[:HAS\_MESSAGE\]->(:Message)-\[:NEXT\_MESSAGE\]->(:Message)

(:Message)-\[:MENTIONS\]->(:Entity)

(:Entity)-\[:RELATED\_TO\]->(:Entity)

(:Entity)-\[:SAME\_AS\]->(:Entity)        // deduplicated

(:ReasoningTrace)-\[:HAS\_STEP\]->(:ReasoningStep)-\[:HAS\_TOOL\_CALL\]->(:ToolCall)

The deduplication system warrants closer inspection. When extraction identifies “Apple” in one message and “Apple Inc.” in another, the resolution pipeline compares them using exact matching, fuzzy string matching, and embedding similarity. If the confidence exceeds the threshold, the two nodes merge with a SAME\_AS relationship, preserving the link. This prevents the graph from fragmenting into disconnected mentions of the same entity, thereby defeating the purpose of graph-based memory.

## How Persistent Memory Changes What the Agent Remembers

The knowledge retriever’s value is visible in a single turn. Agent memory’s value emerges across sessions. The memory provider described above stores conversations, extracts entities, and records reasoning traces on every turn. To see what that persistence changes, consider the same question with and without the memory provider attached. The underlying SEC filing data is identical. The difference is whether the agent can draw on what it learned in prior sessions.

### **Without Memory**

The analyst asks: “How does Apple’s supply chain risk compare to what we discussed last week?” The agent has no prior context. It searches SEC filing data and returns whatever the current top-k chunks contain about supply chains. It says nothing about last week’s conversation, the semiconductor sourcing discussion from session three, or the analyst’s established focus on geographic risk. Every session starts at zero.

### **With Memory**

The same question triggers the memory provider. Short-term memory surfaces the session-three exchange about semiconductor sourcing, matched by embedding similarity even though the analyst used different terminology. Long-term memory contributes to the analyst’s recorded preference for geographic risk analysis and the deduplicated entity graph linking Apple to its suppliers. Reasoning memory finds a similar company-risk analysis that the agent ran in session seven and surfaces the approach it used.

The agent synthesizes current SEC data with prior conversational context:

Based on our previous discussion about Apple’s semiconductor sourcing

dependencies and your focus on geographic risk exposure, here’s how the

The current supply chain picture compares:

In session 3, we identified that Apple’s reliance on TSMC for chip

Fabrication concentrates manufacturing risk in Taiwan. The latest 10-K

filing continues to list Geography as a primary risk factor, citing

complex and changing laws across global operations.

Compared to our earlier analysis, the filing now also emphasizes logistics

disruptions and single-source component dependencies — risks that align

With the supply chain exposure patterns you’ve been tracking across

multiple companies.

The knowledge retriever contributed the SEC filing data. The memory provider contributed the conversational continuity that made the response coherent across sessions.

## Combining Both Providers

Both providers are attached to a single agent via MAF’s context provider list. The following example shows how to configure both providers on a single agent so that it benefits from graph-enriched retrieval and persistent memory simultaneously. The configuration determines what each provider contributes to the agent’s context window on every turn.

from agent\_framework\_neo4j import Neo4jContextProvider

from neo4j\_agent\_memory.integrations.microsoft\_agent import Neo4jMicrosoftMemory

\# Knowledge retriever — searches SEC filings graph

knowledge\_provider = Neo4jContextProvider(

    …

    index\_name=”chunkEmbeddings”,

    index\_type=”vector”,

    retrieval\_query=RETRIEVAL\_QUERY,

    top\_k=5,

)

\# Agent memory — persistent conversational memory

memory = Neo4jMicrosoftMemory.from\_memory\_client(

    memory\_client=memory\_client,

    session\_id=”analyst-session-42″,

    include\_short\_term=True,

    include\_long\_term=True,

    include\_reasoning=True,

    extract\_entities=True,

    extract\_entities\_async=True,

)

agent = Agent(

    client=client,

    name=”company-analyst”,

    instructions=”You answer questions about companies using graph-enriched context.”,

    context\_providers=\[knowledge\_provider, memory.context\_provider\],

)

On each turn, the knowledge retriever searches the SEC filings graph and injects structured company data. The memory provider injects relevant past conversations, known preferences, and similar prior analyses. The agent sees both: the domain knowledge it needs and the conversational history that makes its responses coherent across sessions.

## Context That Compounds

In the first sessions, the knowledge retriever carries most of the weight. The memory graph is sparse, and the agent answers from SEC filing data alone. It surfaces risk factors, products, and geographic exposure because the retrieval query traverses those relationships. Still, it has no sense of what the analyst has already covered or what patterns they care about.

By session ten, the balance shifts. The memory graph holds dozens of entity nodes extracted from prior conversations, a record of which risk categories the analyst returns to most often, and reasoning traces from completed analyses. When the analyst asks about supply chain exposure, the memory provider surfaces the semiconductor sourcing discussion from session three and the preference for geographic risk. The knowledge retriever still searches the same SEC filings graph, but the memory provider narrows what matters. The two providers start reinforcing each other.

By session fifty, the entity graph is dense with deduplicated nodes linking companies, people, risk factors, and products across months of analysis. Reasoning traces from prior analyses provide reusable patterns for structuring new responses. A question about Apple’s risk profile no longer returns a generic summary. It lands in a context shaped by every company the analyst has compared, every risk category they have prioritized, and every analytical approach that succeeded before. The curated knowledge hasn’t changed. What changed is everything the agent learned along the way.

## Deploy and Integrate

Ready to move from concept to code? Follow these steps to implement graph-powered agents on Azure:

-   Launch **[opens in new tabNeo4j Aura on Azure](https://marketplace.microsoft.com/en-us/product/neo4j.neo4j-aura)** for a fully managed graph database experience.
-   Use the **[opens in new tabMicrosoft Agent Framework Memory Provider](https://learn.microsoft.com/en-us/agent-framework/integrations/neo4j-memory?pivots=programming-language-python)** to build conversational persistence.
-   Implement **[opens in new tabGraphRAG](https://learn.microsoft.com/en-us/agent-framework/integrations/neo4j-graphrag?pivots=programming-language-python)** to connect your agent to structured domain knowledge.

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

<research_source type="scraped_from_research" phase="exploitation" file="integrating-external-tools-with-large-language-models-llm-to.md">
<details>
<summary>Integrating External Tools with Large Language Models (LLM) to Improve Accuracy</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2507.08034v1>

# Integrating External Tools with Large Language Models (LLM) to Improve Accuracy

Nripesh Niketan1
nripesh14@gmail.com
\AndHadj Batatia1
h.batatia@hw.ac.uk
ORCID: 0009-0008-2066-1937ORCID: 0000-0003-0433-2152

###### Abstract

This paper deals with improving querying large language models (LLMs). It is well-known that without relevant contextual information, LLMs can provide poor quality responses or tend to hallucinate. Several initiatives have proposed integrating LLMs with external tools to provide them with up-to-date data to improve accuracy. In this paper, we propose a framework to integrate external tools to enhance the capabilities of LLMs in answering queries in educational settings. Precisely, we develop a framework that allows accessing external APIs to request additional relevant information. Integrated tools can also provide computational capabilities such as calculators or calendars. The proposed framework has been evaluated using datasets from the Multi-Modal Language Understanding (MMLU) collection. The data consists of questions on mathematical and scientific reasoning. Results compared to state-of-the-art language models show that the proposed approach significantly improves performance. Our Athena framework achieves 83% accuracy in mathematical reasoning and 88% in scientific reasoning, substantially outperforming all tested models including GPT-4o, LLaMA-Large, Mistral-Large, Phi-Large, and GPT-3.5, with the best baseline model (LLaMA-Large) achieving only 67% and 79% respectively. These promising results open the way to creating complex computing ecosystems around LLMs to make their use more natural to support various tasks and activities.

_Keywords_ LLM  ⋅⋅\cdot⋅
tool integration  ⋅⋅\cdot⋅
precise querying  ⋅⋅\cdot⋅
external APIs  ⋅⋅\cdot⋅
educational AI

## 1 Introduction

The recent development of Large Language Models (LLMs), such as GPT, BERT [[1](https://arxiv.org/html/2507.08034v1#bib.bib1 "")], and LLaMA [[2](https://arxiv.org/html/2507.08034v1#bib.bib2 "")], has had a big impact on natural language processing (NLP) and artificial intelligence (AI). These models have shown an impressive ability to comprehend and produce human-like text and are powered by extensive datasets and complex algorithms. Current LLM models are great in handling and producing natural language but face difficulties with tasks that demand access to current data or active computational capabilities. For example, responding to inquiries about current stock market trends or solving complex mathematical problems is beyond their reach. This limitation is largely due to LLMs being trained on fixed datasets and their limited ability to directly connect with external databases or computational tools.

To overcome these challenges, it is becoming necessary to integrate LLMs with external tools like calculators, calendars, and databases. This combination improves the capabilities of LLMs, allowing them to process language while having access to and analysing current data, and handling computational tasks. This expansion broadens their practical use and application by a large margin. Recent developments in LLMs have focused on extending their capabilities through external tools to address tasks like arithmetic, factual lookups, and real-time information retrieval. Integrating external tools with LLMs methods can be classified into four major categories: Retrieval-augmented generation (RAG), Code execution and computation, connection to APIs, Hybrid systems. Retrieval-augmented methods aim at connecting LLMs with external databases or retrieval systems, such as search engines and databases, to retrieve real-time data in order to provide more accurate, industry-specific, and relevant answers [[3](https://arxiv.org/html/2507.08034v1#bib.bib3 ""), [4](https://arxiv.org/html/2507.08034v1#bib.bib4 "")]. Integrating code execution and computation tools, like Python, data analysis, solvers, calculator, and symbolic reasoners, allows executing code, performing mathematical computations to enhance LLMs capabilities to solve complex tasks [[5](https://arxiv.org/html/2507.08034v1#bib.bib5 ""), [6](https://arxiv.org/html/2507.08034v1#bib.bib6 ""), [7](https://arxiv.org/html/2507.08034v1#bib.bib7 ""), [8](https://arxiv.org/html/2507.08034v1#bib.bib8 "")]. Connecting APIs, such as financial, health, weather, to utilise specialised service in order to handle domain-specific tasks [[9](https://arxiv.org/html/2507.08034v1#bib.bib9 ""), [10](https://arxiv.org/html/2507.08034v1#bib.bib10 ""), [11](https://arxiv.org/html/2507.08034v1#bib.bib11 ""), [12](https://arxiv.org/html/2507.08034v1#bib.bib12 "")]. More general hybrid systems aim at combining symbolic reasoning, knowledge graphs, rule-based engines and other techniques to regularise or guide LLMs towards more deterministic and explainable reasoning [[13](https://arxiv.org/html/2507.08034v1#bib.bib13 ""), [14](https://arxiv.org/html/2507.08034v1#bib.bib14 ""), [15](https://arxiv.org/html/2507.08034v1#bib.bib15 "")]. In this work, we are interested in frameworks that allow connecting external APIs, such as calculators, calendars, solvers, in order to improve precision of LLM answers in an educational context.

The Toolformer, introduced by Meta AI Research and Universitat Pompeu Fabra, enables LLMs to autonomously use simple APIs. This model employs a self-supervised loss to generate a language modelling dataset with embedded API calls, which is then fine-tuned to enhance future token predictions. Toolformer incorporates various tools like calculators and search engines, demonstrating improved zero-shot performance on downstream tasks and addressing limitations such as fact hallucination and outdated information [[16](https://arxiv.org/html/2507.08034v1#bib.bib16 "")]. The Gorilla model, based on a fine-tuned LLaMA model, focuses on enhancing API interaction within LLMs. It surpasses GPT-4 in generating accurate API calls and adapting to document changes, significantly reducing hallucination issues. Gorilla is tested against the APIBench dataset, which includes diverse APIs, showcasing its ability to handle over 1,600 APIs effectively. This model enhances the practical application of LLMs in real-world scenarios by connecting them to a broad spectrum of available APIs [[17](https://arxiv.org/html/2507.08034v1#bib.bib17 "")].

Integrating symbolic reasoning with Large Language Models (LLMs) has also been investigated to enhance their ability to execute arithmetic and other computational tasks, where deterministic solutions are critical. Models such as Program-Aided Language models (PAL) and ToolkenGPT have been pivotal in this development. PAL introduces a novel approach by generating Python programs as intermediate reasoning steps. This method leverages the LLMs’ language understanding and the precise execution of a Python interpreter, significantly improving arithmetic and symbolic reasoning tasks. For instance, PAL outperformed traditional models on the gsm8k math problem benchmark by 8%, and by 40% on the more challenging gsm-hard version [[18](https://arxiv.org/html/2507.08034v1#bib.bib18 "")]. ToolkenGPT utilizes a unique “toolken” token that triggers specific tool usage within the model, enhancing both fine-tuning and in-context learning. This framework allows the LLM to dynamically adapt to an expanding set of tools, showing strong performance in tasks requiring numerical reasoning and knowledge-based question answering [[19](https://arxiv.org/html/2507.08034v1#bib.bib19 "")].

Frameworks connecting LLMs with APIs have revolutionized task execution across various domains, with models like TaskMatrix.AI and Gorilla leading the way. TaskMatrix.AI, developed by Microsoft, integrates foundation models with APIs to tackle a wide range of tasks, leveraging collective intelligence from various models. This system combines a Multimodal Conversational Foundation Model for user interaction with a vast API platform to execute tasks effectively across digital and physical spaces [[20](https://arxiv.org/html/2507.08034v1#bib.bib20 "")]. The Gorilla model enhances LLMs’ ability to interact with APIs, bridging the gap between natural language processing and real-world application by facilitating the use of over 1,600 APIs. This model adapts to document changes and reduces hallucinations, improving how users interact with digital tools through natural language queries [[17](https://arxiv.org/html/2507.08034v1#bib.bib17 "")].

The LATM (LLMs As Tool Makers) framework represents a shift in LLM applications from using external tools to creating and utilizing bespoke tools. This approach enhances problem-solving capabilities and reduces dependency on external resources. LATM operates in two phases: tool making and tool using. Initially, LLMs create tools as Python functions tailored for specific tasks. These tools are then used by the same or different LLMs for problem-solving, allowing for a flexible, cost-effective approach. This framework has been validated in tasks like the Big-Bench, showing that it can match higher-cost models in performance while reducing inference costs. LATM demonstrates a practical, scalable method for enhancing LLMs’ functionality, potentially transforming their role in AI by enabling them to independently create and apply tools for complex tasks.

This paper focuses on creating a framework that supports the integration of Large Language Models (LLMs) with external tools. The study covers tools and technologies to implement the integration of LLMs with external tools and evaluates its effectiveness in real-world applications.

## 2 Proposed Framework

In order to allow LLMs to use external tools to enhance their capabilities, we designed a framework, named Athena. The system manages API of external tools that can be used to enable the LLM to provide accurate, up-to-date, data-driven responses across various domains.

### 2.1 Architecture

The architecture of the proposed framework is shown in Figure [1](https://arxiv.org/html/2507.08034v1#S2.F1 "Figure 1 ‣ 2.1 Architecture ‣ 2 Proposed Framework ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy"). The ExternalServiceIntegrator component manages the tools repository. Any added tool is provided to the system using a schema-like structure, implemented using frameworks like Pydantic, which specifies information about the tool such as specific functionalities, comprehensive descriptions, and required parameters. More precisely the schema includes (Listing [1](https://arxiv.org/html/2507.08034v1#LST1 "Listing 1 ‣ 2.1 Architecture ‣ 2 Proposed Framework ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy")) the tool’s name, description, and the types and details of the arguments it accepts. This structured approach allows the LLM to have explicit knowledge of each tool’s capabilities and requirements.

https://arxiv.org/html/2507.08034v1/extracted/6594090/fig/architecture.jpgFigure 1: Architecture of the proposed Athena framework showing the integration of external tools with LLMs through various components including ExternalServiceIntegrator, MessageSubmission, RunMonitoring, HandleRequiredAction, and UpdateMessage services.Listing 1: Format of a tool description.

```python
defadd(a:int,b:int)->int:
    """Addsaandb.
    Args:
        a:firstint
        b:secondint
    """
    returna+b
```

The LLM’s awareness of the available tools is facilitated by the registration of these tools within its operational environment, typically achieved through a configuration that includes each tool’s detailed schema. These schemas act like blueprints that tell the LLM what each tool does, what inputs it needs, and the kind of response it generates. By referencing these schemas, the LLM can match tools to user queries requiring specific external data or computations that are beyond the LLM’s internal processing capabilities.

The MessageSubmission component implements a user interface that allows submitting user queries and managing context.

The RunMonitoring service is responsible for identifying required external tools. The decision-making process regarding when to use these tools starts with the LLM analysing the user’s input. This analysis involves parsing the query to extract key information and intent. If the query aligns with the capabilities of one or more registered tools—determined by keyword matching, intent recognition, or query complexity—the LLM then identifies this as an opportunity to use an external tool. For instance, a question about current weather conditions might trigger the identification of a weather data tool based on keywords like “weather” and the inclusion of a geographical location.

Once a tool is deemed appropriate for a query, the HandleRequiredAction service proceeds to extract the necessary parameters from the user input. This extraction process uses natural language understanding techniques to identify and map the required data points from the query to the parameters defined in the tool’s schema. For example, if the tool requires a city name and date to fetch weather data, the LLM extracts these details from the query.

After parameter extraction, the service formats these parameters according to the API’s expected structure, ensuring that all required data points are correctly included. This often involves transforming natural language inputs into more structured data formats that the API can process, such as converting a city’s name into a standardized location code.

The system then sends the formatted parameters to the external tool’s API. Upon receiving the results from the API, the returned data is integrated into the ongoing dialogue. This integration is handled by converting the API’s raw output into a natural, conversational response that aligns with the user’s original query and maintains the flow of the dialogue. The UpdateMessage service submits the newly updated query to the LLM.

This entire process is iterative; the LLM continuously assesses whether additional information from external tools is needed to fully address the user’s query. This assessment might lead to multiple rounds of tool invocations until the query is completely answered. Finally, the comprehensive response, enriched with both the LLM’s internal knowledge and the external tool’s specialized data, is delivered to the user.

This streamlined methodology enables the LLM to effectively augment its responses with specialized external data, thereby enhancing the accuracy and relevance of the information provided to the user.

Langchain Implementation: In the LangChain implementation of the Athena framework, the system uses the Unify [[21](https://arxiv.org/html/2507.08034v1#bib.bib21 "")] platform in conjunction with the LangChain framework. Unify is different from traditional LLMs. It functions as a comprehensive hosting tool that aggregates various open-source LLMs, providing access to them through a unified API. This setup allows users to use a diverse range of LLMs tailored to different tasks and capabilities. The LangChain framework is integral to this implementation. It acts as middleware that integrates the external tools with the LLMs hosted on the Unify platform. In this setup, LangChain abstracts the complexity of tool integration from the user and streamlines the process of increasing LLM capabilities with external APIs.

In practical terms, the LangChain implementation operates under a less hands-on approach from the developers or users in terms of direct API management. Instead of manually preparing and managing API calls, users simply configure LangChain to recognize and utilize the available tools. This part of the system’s operation—deciding which LLM to deploy for a given task and how to integrate the response from an external tool—is managed internally by LangChain.

## 3 Evaluation

In order to evaluate the proposed framework, we integrated a few tools and ran various experiments on mathematical and scientific reasoning. This section describes the integrated tools, the experiments and the results.

### 3.1 Sample Integrated Tools

The proposed framework is generic and allows integrating any API. However, in this study, we focused on a few important ones, namely ArXiv, Google SERPer, OpenWeatherMap, Google Calendar, and Wolfram Alpha.

- •
As Athena’s computational backbone, the Wolfram Alpha API supports complex calculations and algorithm-based queries across various scientific and mathematical fields.
- •
The Google SERPer API enables the system to perform web searches and deliver relevant online content in response to user queries. This tool is critical for extending the model’s knowledge beyond its training data.
- •
ArXiv API allows the system to access and provide detailed information on scholarly articles. It aids users in retrieving and understanding academic content quickly, enhancing research efficiency.
- •
The OpenWeatherMap API provides real-time weather forecasts and historical data, allowing the AI to assist users in weather-related planning and inquiries effectively.
- •
Google Calendar is integrated to manage scheduling and time-based tasks. This feature allows users to interact with their calendar through natural language commands, supported by secure authentication and event management functionalities.

### 3.2 Datasets

Specific datasets from the Multi-Modal Language Understanding (MMLU) collection hosted on HuggingFace were chosen to test the Athena framework against various state-of-the-art language models. These datasets contain multiple-choice questions designed to assess the models’ proficiency across different domains and educational levels. The structured format of these datasets, where each entry includes a question, four potential answers, and the correct answer, provides a standardized method to measure the accuracy of the AI models’ responses. The selected datasets focus mostly on mathematical and scientific disciplines at various educational stages.

For mathematics, datasets labelled as Elementary Mathematics, High School Mathematics, and College Mathematics were used. To create a comprehensive math testing dataset, 33 questions were selected from the Elementary and High School Mathematics set, and 34 questions from the College Mathematics set. This selection ensures a balanced representation of both basic and advanced mathematical problems. This approach challenges the models to handle a range of complexities and mathematical concepts.

Similarly, for science, the chosen datasets included High School and College levels for Physics, Chemistry, and Biology. High School Physics, Chemistry, Biology contributed 16 questions each; and each of College Physics, Chemistry, Biology contributed 17 questions, with a total of 100 science questions. This selection tests the model’s ability to interpret and solve scientific problems that require fact-based knowledge and the application of scientific theories. This diverse range of subjects and difficulty levels in these datasets also allows for a thorough evaluation of how well the model can answer different types of inquiries.

### 3.3 Experimental Scenario

Testing Procedure: A Jupyter notebook was used to systematically test the models on the selected multiple-choice questions from the MMLU datasets. The testing process involved a setup where each question from the datasets was formatted in a specific way for consistency and to simulate a natural questioning environment. Each question was presented to the Large Language Model (LLM) along with the corresponding multiple-choice options. The format was structured to include the question followed by the options, each labelled with letters (A, B, C, D). To standardize the evaluation and to capture the model’s responses in a structured manner, the LLM was instructed to output its answers in JSON format. This requirement was specified in the prompt to the model to ensure that the output could be easily parsed and analysed. Listing [2](https://arxiv.org/html/2507.08034v1#LST2 "Listing 2 ‣ 3.3 Experimental Scenario ‣ 3 Evaluation ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy") shows an example of the specific format requested, showing clear separation between the chosen answer and the text of the answer, helping in the automated evaluation of responses.

Listing 2: Format of response.

```
"{question}
Options:{options}
Iwantyoutogivemetheoutputintheformofjson.
Example:
’’’json{
"answer":"<Therightoption(A,B,C,D)>",
"value":"<Valueofmultiplechoiceanswer>",
}’’’"
```

Recording and Evaluation: During the test runs, each response from the LLM was recorded from the Jupyter notebook. The responses were then compared to the correct answers provided in the datasets. For each response, it was recorded whether the LLM correctly identified the right option (A, B, C, or D). The primary metrics noted were the number of correct and incorrect answers, which were used to calculate the accuracy of the LLM for both the mathematics and science questions separately.

Comparison: The Athena framework and all baseline language models (GPT-3.5, GPT-4o, LLaMA-Large, Mistral-Large, and Phi-Large) were presented with the exact same set of questions under identical conditions to ensure a fair and controlled comparison. This methodology aimed to provide a clear picture of how each model performs when faced with identical academic challenges, focusing on their ability to interpret and solve mathematical and scientific problems. The comparison tests were designed to highlight the differences in accuracy and capacity across all evaluated models.

### 3.4 Results

This section presents the results of applying the proposed Athena framework to mathematical and scientific reasoning datasets, comparing its performance against state-of-the-art language models including GPT-3.5, GPT-4o, LLaMA-Large, Mistral-Large, and Phi-Large.

Mathematical Reasoning Results: The evaluation on mathematical questions revealed significant performance differences across models (Figure [2](https://arxiv.org/html/2507.08034v1#S3.F2 "Figure 2 ‣ 3.4 Results ‣ 3 Evaluation ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy") and Table [1](https://arxiv.org/html/2507.08034v1#S3.T1 "Table 1 ‣ 3.4 Results ‣ 3 Evaluation ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy")). Among the baseline language models, LLaMA-Large achieved the highest accuracy at 67%, followed by Mistral-Large at 57%, GPT-4o at 53%, Phi-Large at 47%, and GPT-3.5 at 36%. These models showed varying capabilities in handling mathematical problems, with performance generally limited to questions that could be solved through memorized knowledge rather than computational reasoning.

https://arxiv.org/html/2507.08034v1/extracted/6594090/fig/math_results.pngFigure 2: Mathematical reasoning accuracy comparison between Athena framework and state-of-the-art language models using MMLU mathematics dataset.Table 1: Mathematical reasoning accuracy comparison

| Model | Accuracy |
| --- | --- |
| GPT-3.5 | 0.36 |
| GPT-4o | 0.53 |
| LLaMA-Large | 0.67 |
| Mistral-Large | 0.57 |
| Phi-Large | 0.47 |
| Athena Framework | 0.83 |

In contrast, the Athena framework achieved an accuracy of 83%, substantially outperforming all baseline models. This improvement was largely attributed to Athena’s ability to leverage integrated computational tools, particularly calculators, for numerical problem-solving. The framework demonstrated strong capacity to handle diverse mathematical challenges, from basic arithmetic to complex algebraic problems that required step-by-step computational reasoning beyond what standalone LLMs could provide.

Scientific Reasoning Results: The scientific reasoning evaluation showed similar patterns, though with generally higher baseline performance across all models (Figure [3](https://arxiv.org/html/2507.08034v1#S3.F3 "Figure 3 ‣ 3.4 Results ‣ 3 Evaluation ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy") and Table [2](https://arxiv.org/html/2507.08034v1#S3.T2 "Table 2 ‣ 3.4 Results ‣ 3 Evaluation ‣ Integrating External Tools with Large Language Models (LLM) to Improve Accuracy")). LLaMA-Large again performed best among baseline models with 79% accuracy, followed by GPT-4o at 77%, while Mistral-Large and Phi-Large both achieved 66%, and GPT-3.5 reached 56%. The baseline models showed particular strength in theoretical questions involving direct recall of scientific concepts and definitions.

https://arxiv.org/html/2507.08034v1/extracted/6594090/fig/science_results.pngFigure 3: Scientific reasoning accuracy comparison between Athena framework and state-of-the-art language models using MMLU science dataset.Table 2: Scientific reasoning accuracy comparison

| Model | Accuracy |
| --- | --- |
| GPT-3.5 | 0.56 |
| GPT-4o | 0.77 |
| LLaMA-Large | 0.79 |
| Mistral-Large | 0.66 |
| Phi-Large | 0.66 |
| Athena Framework | 0.88 |

The Athena framework achieved 88% accuracy in scientific reasoning, maintaining its superior performance across domains. Out of 100 science questions, Athena incorrectly answered only 12, demonstrating substantial capability to handle a broad spectrum of scientific inquiries. The framework’s success was particularly evident in questions requiring numerical calculations combined with theoretical knowledge, showcasing its ability to effectively integrate computational tools with factual data retrieval.

Analysis and Implications: The results demonstrate that while modern LLMs have improved significantly over earlier generations, tool integration provides capabilities that cannot be achieved through model scaling alone. The performance gap between Athena and the best baseline model (LLaMA-Large) was 16 percentage points in mathematics and 9 percentage points in science. The smaller gap in scientific reasoning compared to mathematical reasoning suggests that newer models have improved significantly in handling factual scientific knowledge, but still benefit substantially from computational tools for calculation-intensive problems.

These findings confirm that tool integration remains a valuable approach even as base model capabilities improve, and that the Athena framework provides consistent benefits across different types of reasoning tasks. The framework’s ability to leverage external computational resources enables it to handle complex problems that require both linguistic understanding and precise mathematical computation.

## 4 Conclusion

This paper presented the Athena framework for integrating external tools with LLMs to enhance the accuracy of model response. The framework allows for the integration of any tool. A study was conducted using a set of typical tools that can benefit educational applications. The evaluation using mathematics and science questions from the MMLU dataset demonstrated significant improvements over standalone LLM performance.

The key contributions of this work include: (1) A flexible framework architecture that allows seamless integration of external APIs and computational tools with LLMs, (2) Comprehensive evaluation demonstrating significant performance improvements in educational domains, with 83% accuracy in mathematics and 88% in science, substantially outperforming all tested state-of-the-art models including GPT-4o, LLaMA-Large, Mistral-Large, and Phi-Large, (3) Evidence that tool integration provides capabilities that cannot be achieved through model scaling alone, and (4) A practical implementation using LangChain and Unify platforms that abstracts the complexity of tool integration.

The results indicate that while modern LLMs have improved substantially, there remains a significant advantage in augmenting them with specialized external tools, particularly for tasks requiring computational capabilities or access to current information. Future work will focus on expanding the range of integrated tools, improving the decision-making process for tool selection, and exploring applications in other domains beyond education.

## Acknowledgments

This work was supported by Heriot-Watt University. We thank the reviewers for their valuable feedback and suggestions that helped improve this paper.

## References

- \[1\]↑
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova.

Bert: Pre-training of deep bidirectional transformers for language understanding.

arXiv preprint arXiv:1810.04805, 2018.

- \[2\]↑
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al.

Llama: Open and efficient foundation language models.

arXiv preprint arXiv:2302.13971, 2023.

- \[3\]↑
Luyu Gao, Zhuyun Dai, and Jamie Callan.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

Advances in Neural Information Processing Systems, 36, 2023.

- \[4\]↑
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

Advances in neural information processing systems, 33:9459–9474, 2020.

- \[5\]↑
Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, et al.

Program synthesis with large language models.

arXiv preprint arXiv:2108.07732, 2021.

- \[6\]↑
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al.

Evaluating large language models trained on code.

arXiv preprint arXiv:2107.03374, 2021.

- \[7\]↑
Sean Welleck, Jiacheng Liu, Ronan Le Bras, Hannaneh Hajishirzi, Yejin Choi, and Kyunghyun Cho.

Naturalproofs: Mathematical theorem proving in natural language.

arXiv preprint arXiv:2104.01112, 2021.

- \[8\]↑
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano, et al.

Training verifiers to solve math word problems.

arXiv preprint arXiv:2110.14168, 2021.

- \[9\]↑
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al.

Webgpt: Browser-assisted question-answering with human feedback.

arXiv preprint arXiv:2112.09332, 2021.

- \[10\]↑
Mojtaba Komeili, Kurt Shuster, and Jason Weston.

Internet-augmented dialogue generation.

International Conference on Machine Learning, pages 8460–8478, 2021.

- \[11\]↑
Romal Thoppilan, Daniel De Freitas, Jamie Hall, Noam Shazeer, Apoorv Kulshreshtha, Heng-Tze Cheng, Alicia Jin, Taylor Bos, Leslie Baker, Yu Du, et al.

Lamda: Language models for dialog applications.

arXiv preprint arXiv:2201.08239, 2022.

- \[12\]↑
Baolin Peng, Michel Galley, Pengcheng He, Hao Cheng, Yujia Xie, Yu Hu, Qiuyuan Huang, Lars Liden, Zhou Yu, Weizhu Chen, et al.

Check your facts and try again: Improving large language models with external knowledge and automated feedback.

arXiv preprint arXiv:2302.12813, 2023.

- \[13\]↑
Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, and Xindong Wu.

Unifying large language models and knowledge graphs: A roadmap.

IEEE Transactions on Knowledge and Data Engineering, 2023.

- \[14\]↑
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.

React: Synergizing reasoning and acting in language models.

arXiv preprint arXiv:2210.03629, 2022.

- \[15\]↑
Liangming Pan, Alon Albalak, Xinyi Wang, and William Yang Wang.

Logic-lm: Empowering large language models with symbolic solvers for faithful logical reasoning.

arXiv preprint arXiv:2305.12295, 2023.

- \[16\]↑
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom.

Toolformer: Language models can teach themselves to use tools.

arXiv preprint arXiv:2302.04761, 2023.

- \[17\]↑
Shishir G Patil, Tianjun Zhang, Xin Wang, and Joseph E Gonzalez.

Gorilla: Large language model connected with massive apis.

arXiv preprint arXiv:2305.15334, 2023.

- \[18\]↑
Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, and Graham Neubig.

Pal: Program-aided language models.

arXiv preprint arXiv:2211.10435, 2022.

- \[19\]↑
Shibo Hao, Tianyang Liu, Zhen Wang, and Zhiting Hu.

Toolkengpt: Augmenting frozen language models with massive tools via tool embeddings.

arXiv preprint arXiv:2305.11554, 2023.

- \[20\]↑
Yaobo Liang, Chenfei Wu, Ting Song, Wenshan Wu, Yan Xia, Yu Liu, Yang Ou, Shuai Lu, Lei Ji, Shaoguang Mao, et al.

Taskmatrix.ai: Completing tasks by connecting foundation models with millions of apis.

arXiv preprint arXiv:2303.16434, 2023.

- \[21\]↑
Unify.

Unify: The complete llm platform, 2024.

Accessed: 2024-01-15.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="output-pydantic-docs.md">
<details>
<summary>Output</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://pydantic.dev/docs/ai/core-concepts/output/>

# Output

“Output” refers to the final value returned from [running an agent](https://pydantic.dev/docs/ai/core-concepts/agent#running-agents). This can be either plain text, [structured data](https://pydantic.dev/docs/ai/core-concepts/output/#structured-output), an [image](https://pydantic.dev/docs/ai/core-concepts/output/#image-output), or the result of a [function](https://pydantic.dev/docs/ai/core-concepts/output/#output-functions) called with arguments provided by the model.

The output is wrapped in [`AgentRunResult`](https://pydantic.dev/docs/ai/api/pydantic-ai/run/#pydantic_ai.run.AgentRunResult) or [`StreamedRunResult`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult) so that you can access other data, like [usage](https://pydantic.dev/docs/ai/api/pydantic-ai/usage/#pydantic_ai.usage.RunUsage) of the run and [message history](https://pydantic.dev/docs/ai/core-concepts/message-history#accessing-messages-from-results).

Both `AgentRunResult` and `StreamedRunResult` are generic in the data they wrap, so typing information about the data returned by the agent is preserved.

A run ends when the model responds with one of the output types, or, if no output type is specified or `str` is one of the allowed options, when a plain text response is received. A run can also be cancelled if usage limits are exceeded, see [Usage Limits](https://pydantic.dev/docs/ai/core-concepts/agent#usage-limits).

Here’s an example using a Pydantic model as the `output_type`, forcing the model to respond with data matching our specification:

olympics.pyDirectGateway

```python
from pydantic import BaseModelfrom pydantic_ai import Agentclass CityLocation(BaseModel):    city: str    country: stragent = Agent('google-gla:gemini-3-flash-preview', output_type=CityLocation)result = agent.run_sync('Where were the olympics held in 2012?')print(result.output)#> city='London' country='United Kingdom'print(result.usage())#> RunUsage(input_tokens=57, output_tokens=8, requests=1)




```

_(This example is complete, it can be run “as is”)_

## Structured output data

[Section titled Structured output data](https://pydantic.dev/docs/ai/core-concepts/output/#structured-output)

The [`Agent`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent) class constructor takes an `output_type` argument that takes one or more types or [output functions](https://pydantic.dev/docs/ai/core-concepts/output/#output-functions). It supports simple scalar types, list and dict types (including `TypedDict`s and [`StructuredDict`s](https://pydantic.dev/docs/ai/core-concepts/output/#structured-dict)), dataclasses and Pydantic models, as well as type unions — generally everything supported as type hints in a Pydantic model. You can also pass a list of multiple choices.

By default, Pydantic AI leverages the model’s tool calling capability to make it return structured data. When multiple output types are specified (in a union or list), each member is registered with the model as a separate output tool in order to reduce the complexity of the schema and maximise the chances a model will respond correctly. This has been shown to work well across a wide range of models. If you’d like to change the names of the output tools, use a model’s native structured output feature, or pass the output schema to the model in its [instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions), you can use an [output mode](https://pydantic.dev/docs/ai/core-concepts/output/#output-modes) marker class.

When no output type is specified, or when `str` is among the output types, any plain text response from the model will be used as the output data.
If `str` is not among the output types, the model is forced to return structured data or call an output function.

If the output type schema is not of type `"object"` (e.g. it’s `int` or `list[int]`), the output type is wrapped in a single element object, so the schema of all tools registered with the model are object schemas.

Structured outputs (like tools) use Pydantic to build the JSON schema used for the tool, and to validate the data returned by the model.

Here’s an example of returning either text or structured data:

box\_or\_error.pyDirectGateway

```python
from pydantic import BaseModelfrom pydantic_ai import Agentclass Box(BaseModel):  width: int  height: int  depth: int  units: stragent = Agent(  'openai:gpt-5-mini',  output_type=[Box, str],   instructions=(      "Extract me the dimensions of a box, "      "if you can't extract all data, ask the user to try again."  ),)result = agent.run_sync('The box is 10x20x30')print(result.output)#> Please provide the units for the dimensions (e.g., cm, in, m).result = agent.run_sync('The box is 10x20x30 cm')print(result.output)#> width=10 height=20 depth=30 units='cm'




```

This could also have been a union: `output_type=Box | str`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.

_(This example is complete, it can be run “as is”)_

Here’s an example of using a union return type, which will register multiple output tools and wrap non-object schemas in an object:

colors\_or\_sizes.py

```python
from pydantic_ai import Agentagent = Agent[None, list[str] | list[int]](  'openai:gpt-5-mini',  output_type=list[str] | list[int],  # type: ignore   instructions='Extract either colors or sizes from the shapes provided.',)result = agent.run_sync('red square, blue circle, green triangle')print(result.output)#> ['red', 'blue', 'green']result = agent.run_sync('square size 10, circle size 20, triangle size 30')print(result.output)#> [10, 20, 30]




```

As explained in the "Type checking considerations" section above, using a union rather than a list requires explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.

_(This example is complete, it can be run “as is”)_

### Output functions

[Section titled Output functions](https://pydantic.dev/docs/ai/core-concepts/output/#output-functions)

Instead of plain text or structured data, you may want the output of your agent run to be the result of a function called with arguments provided by the model, for example to further process or validate the data provided through the arguments (with the option to tell the model to try again), or to hand off to another agent.

Output functions are similar to [function tools](https://pydantic.dev/docs/ai/tools-toolsets/tools), but the model is forced to call one of them, the call ends the agent run, and the result is not passed back to the model.

As with tool functions, output function arguments provided by the model are validated using Pydantic (with optional [validation context](https://pydantic.dev/docs/ai/core-concepts/output/#validation-context)), can optionally take [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext) as the first argument, and can raise [`ModelRetry`](https://pydantic.dev/docs/ai/api/pydantic-ai/exceptions/#pydantic_ai.exceptions.ModelRetry) to ask the model to try again with modified arguments (or with a different output type).

To specify output functions, you set the agent’s `output_type` to either a single function (or bound instance method), or a list of functions. The list can also contain other output types like simple scalars or entire Pydantic models.
You typically do not want to also register your output function as a tool (using the `@agent.tool` decorator or `tools` argument), as this could confuse the model about which it should be calling.

Here’s an example of all of these features in action:

output\_functions.py

```python
import refrom pydantic import BaseModelfrom pydantic_ai import Agent, ModelRetry, RunContext, UnexpectedModelBehaviorclass Row(BaseModel):    name: str    country: strtables = {    'capital_cities': [        Row(name='Amsterdam', country='Netherlands'),        Row(name='Mexico City', country='Mexico'),    ]}class SQLFailure(BaseModel):    """An unrecoverable failure. Only use this when you can't change the query to make it work."""    explanation: strdef run_sql_query(query: str) -> list[Row]:    """Run a SQL query on the database."""    select_table = re.match(r'SELECT (.+) FROM (\w+)', query)    if select_table:        column_names = select_table.group(1)        if column_names != '*':            raise ModelRetry("Only 'SELECT *' is supported, you'll have to do column filtering manually.")        table_name = select_table.group(2)        if table_name not in tables:            raise ModelRetry(                f"Unknown table '{table_name}' in query '{query}'. Available tables: {', '.join(tables.keys())}."            )        return tables[table_name]    raise ModelRetry(f"Unsupported query: '{query}'.")sql_agent = Agent[None, list[Row] | SQLFailure](    'openai:gpt-5.2',    output_type=[run_sql_query, SQLFailure],    instructions='You are a SQL agent that can run SQL queries on a database.',)async def hand_off_to_sql_agent(ctx: RunContext, query: str) -> list[Row]:    """I take natural language queries, turn them into SQL, and run them on a database."""    # Drop the final message with the output tool call, as it shouldn't be passed on to the SQL agent    messages = ctx.messages[:-1]    try:        result = await sql_agent.run(query, message_history=messages)        output = result.output        if isinstance(output, SQLFailure):            raise ModelRetry(f'SQL agent failed: {output.explanation}')        return output    except UnexpectedModelBehavior as e:        # Bubble up potentially retryable errors to the router agent        if (cause := e.__cause__) and isinstance(cause, ModelRetry):            raise ModelRetry(f'SQL agent failed: {cause.message}') from e        else:            raiseclass RouterFailure(BaseModel):    """Use me when no appropriate agent is found or the used agent failed."""    explanation: strrouter_agent = Agent[None, list[Row] | RouterFailure](    'openai:gpt-5.2',    output_type=[hand_off_to_sql_agent, RouterFailure],    instructions='You are a router to other agents. Never try to solve a problem yourself, just pass it on.',)result = router_agent.run_sync('Select the names and countries of all capitals')print(result.output)"""[    Row(name='Amsterdam', country='Netherlands'),    Row(name='Mexico City', country='Mexico'),]"""result = router_agent.run_sync('Select all pets')print(repr(result.output))"""RouterFailure(explanation="The requested table 'pets' does not exist in the database. The only available table is 'capital_cities', which does not contain data about pets.")"""result = router_agent.run_sync('How do I fly from Amsterdam to Mexico City?')print(repr(result.output))"""RouterFailure(explanation='I am not equipped to provide travel information, such as flights from Amsterdam to Mexico City.')"""




```

#### Text output

[Section titled Text output](https://pydantic.dev/docs/ai/core-concepts/output/#text-output)

If you provide an output function that takes a string, Pydantic AI will by default create an output tool like for any other output function. If instead you’d like the model to provide the string using plain text output, you can wrap the function in the [`TextOutput`](https://pydantic.dev/docs/ai/api/pydantic-ai/output/#pydantic_ai.output.TextOutput) marker class.

If desired, this marker class can be used alongside one or more [`ToolOutput`](https://pydantic.dev/docs/ai/core-concepts/output/#tool-output) marker classes (or unmarked types or functions) in a list provided to `output_type`.

Like other output functions, text output functions can optionally take [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext) as the first argument, and can raise [`ModelRetry`](https://pydantic.dev/docs/ai/api/pydantic-ai/exceptions/#pydantic_ai.exceptions.ModelRetry) to ask the model to try again with modified arguments (or with a different output type).

text\_output\_function.pyDirectGateway

```python
from pydantic_ai import Agent, TextOutputdef split_into_words(text: str) -> list[str]:    return text.split()agent = Agent(    'openai:gpt-5.2',    output_type=TextOutput(split_into_words),)result = agent.run_sync('Who was Albert Einstein?')print(result.output)#> ['Albert', 'Einstein', 'was', 'a', 'German-born', 'theoretical', 'physicist.']




```

_(This example is complete, it can be run “as is”)_

#### Handling partial output in output functions

[Section titled Handling partial output in output functions](https://pydantic.dev/docs/ai/core-concepts/output/#handling-partial-output-in-output-functions)

When streaming with `run_stream()` or `run_stream_sync()`, output functions are called **multiple times** — once for each partial output received from the model, and once for the final complete output.

You should check the [`RunContext.partial_output`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext.partial_output) flag when your output function has **side effects** (e.g., sending notifications, logging, database updates) that should only execute on the final output.

When streaming, `partial_output` is `True` for each partial output and `False` for the final complete output.
For all [other run methods](https://pydantic.dev/docs/ai/core-concepts/agent#running-agents), `partial_output` is always `False` as the function is only called once with the complete output.

output\_function\_with\_side\_effects.pyDirectGateway

```python
from pydantic import BaseModelfrom pydantic_ai import Agent, RunContextclass DatabaseRecord(BaseModel):    name: str    value: int | None = None  # Make optional to allow partial outputdef save_to_database(ctx: RunContext, record: DatabaseRecord) -> DatabaseRecord:    """Output function with side effect - only save final output to database."""    if ctx.partial_output:        # Skip side effects for partial outputs        return record    # Only execute side effect for the final output    print(f'Saving to database: {record.name} = {record.value}')    #> Saving to database: test = 42    return recordagent = Agent('openai:gpt-5.2', output_type=save_to_database)async def main():    async with agent.run_stream('Create a record with name "test" and value 42') as result:        async for output in result.stream_output(debounce_by=None):            print(output)            #> name='test' value=None            #> name='test' value=42




```

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

### Output modes

[Section titled Output modes](https://pydantic.dev/docs/ai/core-concepts/output/#output-modes)

Pydantic AI implements three different methods to get a model to output structured data:

1. [Tool Output](https://pydantic.dev/docs/ai/core-concepts/output/#tool-output), where tool calls are used to produce the output.
2. [Native Output](https://pydantic.dev/docs/ai/core-concepts/output/#native-output), where the model is required to produce text content compliant with a provided JSON schema.
3. [Prompted Output](https://pydantic.dev/docs/ai/core-concepts/output/#prompted-output), where a prompt is injected into the model instructions including the desired JSON schema, and we attempt to parse the model’s plain-text response as appropriate.

#### Tool Output

[Section titled Tool Output](https://pydantic.dev/docs/ai/core-concepts/output/#tool-output)

In the default Tool Output mode, the output JSON schema of each output type (or function) is provided to the model as the parameters schema of a special output tool. This is the default as it’s supported by virtually all models and has been shown to work very well.

If you’d like to change the name of the output tool, pass a custom description to aid the model, or turn on or off strict mode, you can wrap the type(s) in the [`ToolOutput`](https://pydantic.dev/docs/ai/api/pydantic-ai/output/#pydantic_ai.output.ToolOutput) marker class and provide the appropriate arguments. Note that by default, the description is taken from the docstring specified on a Pydantic model or output function, so specifying it using the marker class is typically not necessary.

To dynamically modify or filter the available output tools during an agent run, you can define an agent-wide `prepare_output_tools` function that will be called ahead of each step of a run. This function should be of type [`ToolsPrepareFunc`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.ToolsPrepareFunc), which takes the [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext) and a list of [`ToolDefinition`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.ToolDefinition), and returns a new list of tool definitions (or `None` to disable all tools for that step). This is analogous to the [`prepare_tools` function](https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced#prepare-tools) for non-output tools.

tool\_output.pyDirectGateway

```python
from pydantic import BaseModelfrom pydantic_ai import Agent, ToolOutputclass Fruit(BaseModel):  name: str  color: strclass Vehicle(BaseModel):  name: str  wheels: intagent = Agent(  'openai:gpt-5.2',  output_type=[       ToolOutput(Fruit, name='return_fruit'),      ToolOutput(Vehicle, name='return_vehicle'),  ],)result = agent.run_sync('What is a banana?')print(repr(result.output))#> Fruit(name='banana', color='yellow')




```

If we were passing just `Fruit` and `Vehicle` without custom tool names, we could have used a union: `output_type=Fruit | Vehicle`. However, as `ToolOutput` is an object rather than a type, we have to use a list.

_(This example is complete, it can be run “as is”)_

##### Parallel Output Tool Calls

[Section titled Parallel Output Tool Calls](https://pydantic.dev/docs/ai/core-concepts/output/#parallel-output-tool-calls)

When the model calls other tools in parallel with an output tool, you can control how tool calls are executed by setting the agent’s [`end_strategy`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent.end_strategy):

- `'early'` (default): Output tools are executed first. Once a valid final result is found, remaining function and output tool calls are skipped
- `'graceful'`: Output tools are executed first. Once a valid final result is found, remaining output tool calls are skipped, but function tools are still executed
- `'exhaustive'`: Output tools are executed first, then all function tools are executed. The first valid output tool result becomes the final output

| Strategy | Function tools | Output tools |
| --- | --- | --- |
| `'early'` (default) | Skip remaining | Skip remaining |
| `'graceful'` | Execute all | Skip remaining |
| `'exhaustive'` | Execute all | Execute all (first valid result wins) |

The `'graceful'` and `'exhaustive'` strategies are useful when function tools have important side effects (like logging, sending notifications, or updating metrics) that should always execute. Use `'graceful'` over `'exhaustive'` when you want to avoid executing additional output tools unnecessarily — for example, when output tools have side effects that should only fire once.

#### Native Output

[Section titled Native Output](https://pydantic.dev/docs/ai/core-concepts/output/#native-output)

Native Output mode uses a model’s native “Structured Outputs” feature (aka “JSON Schema response format”), where the model is forced to only output text matching the provided JSON schema. Note that this is not supported by all models, and sometimes comes with restrictions. For example, Gemini cannot use tools at the same time as structured output, and attempting to do so will result in an error.

To use this mode, you can wrap the output type(s) in the [`NativeOutput`](https://pydantic.dev/docs/ai/api/pydantic-ai/output/#pydantic_ai.output.NativeOutput) marker class that also lets you specify a `name` and `description` if the name and docstring of the type or function are not sufficient.

native\_output.pyDirectGateway

```python
from pydantic_ai import Agent, NativeOutputfrom tool_output import Fruit, Vehicleagent = Agent(  'openai:gpt-5.2',  output_type=NativeOutput(      [Fruit, Vehicle],       name='Fruit_or_vehicle',      description='Return a fruit or vehicle.'  ),)result = agent.run_sync('What is a Ford Explorer?')print(repr(result.output))#> Vehicle(name='Ford Explorer', wheels=4)




```

This could also have been a union: `output_type=Fruit | Vehicle`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.

_(This example is complete, it can be run “as is”)_

#### Prompted Output

[Section titled Prompted Output](https://pydantic.dev/docs/ai/core-concepts/output/#prompted-output)

In this mode, the model is prompted to output text matching the provided JSON schema through its [instructions](https://pydantic.dev/docs/ai/core-concepts/agent#instructions) and it’s up to the model to interpret those instructions correctly. This is usable with all models, but is often the least reliable approach as the model is not forced to match the schema.

While we would generally suggest starting with tool or native output, in some cases this mode may result in higher quality outputs, and for models without native tool calling or structured output support it is the only option for producing structured outputs.

If the model API supports the “JSON Mode” feature (aka “JSON Object response format”) to force the model to output valid JSON, this is enabled, but it’s still up to the model to abide by the schema. Pydantic AI will validate the returned structured data and tell the model to try again if validation fails, but if the model is not intelligent enough this may not be sufficient.

To use this mode, you can wrap the output type(s) in the [`PromptedOutput`](https://pydantic.dev/docs/ai/api/pydantic-ai/output/#pydantic_ai.output.PromptedOutput) marker class that also lets you specify a `name` and `description` if the name and docstring of the type or function are not sufficient. Additionally, `template` lets you specify a custom instructions template to be used instead of the [default](https://pydantic.dev/docs/ai/api/pydantic-ai/profiles/#pydantic_ai.profiles.ModelProfile.prompted_output_template), or `template=False` to disable the schema prompt entirely.

prompted\_output.pyDirectGateway

```python
from pydantic import BaseModelfrom pydantic_ai import Agent, PromptedOutputfrom tool_output import Vehicleclass Device(BaseModel):  name: str  kind: stragent = Agent(  'openai:gpt-5.2',  output_type=PromptedOutput(      [Vehicle, Device],       name='Vehicle or device',      description='Return a vehicle or device.'  ),)result = agent.run_sync('What is a MacBook?')print(repr(result.output))#> Device(name='MacBook', kind='laptop')agent = Agent(  'openai:gpt-5.2',  output_type=PromptedOutput(      [Vehicle, Device],      template='Gimme some JSON: {schema}'  ),)result = agent.run_sync('What is a Ford Explorer?')print(repr(result.output))#> Vehicle(name='Ford Explorer', wheels=4)




```

This could also have been a union: `output_type=Vehicle | Device`. However, as explained in the "Type checking considerations" section above, that would've required explicitly specifying the generic parameters on the `Agent` constructor and adding `# type: ignore` to this line in order to be type checked correctly.

_(This example is complete, it can be run “as is”)_

### Custom JSON schema

[Section titled Custom JSON schema](https://pydantic.dev/docs/ai/core-concepts/output/#structured-dict)

If it’s not feasible to define your desired structured output object using a Pydantic `BaseModel`, dataclass, or `TypedDict`, for example when you get a JSON schema from an external source or generate it dynamically, you can use the [`StructuredDict()`](https://pydantic.dev/docs/ai/api/pydantic-ai/output/#pydantic_ai.output.StructuredDict) helper function to generate a `dict[str, Any]` subclass with a JSON schema attached that Pydantic AI will pass to the model.

Note that Pydantic AI will not perform any validation of the received JSON object and it’s up to the model to correctly interpret the schema and any constraints expressed in it, like required fields or integer value ranges.

The output type will be a `dict[str, Any]` and it’s up to your code to defensively read from it in case the model made a mistake. You can use an [output validator](https://pydantic.dev/docs/ai/core-concepts/output/#output-validator-functions) to reflect validation errors back to the model and get it to try again.

Along with the JSON schema, you can optionally pass `name` and `description` arguments to provide additional context to the model:

DirectGateway

```python
from pydantic_ai import Agent, StructuredDictHumanDict = StructuredDict(    {        'type': 'object',        'properties': {            'name': {'type': 'string'},            'age': {'type': 'integer'}        },        'required': ['name', 'age']    },    name='Human',    description='A human with a name and age',)agent = Agent('openai:gpt-5.2', output_type=HumanDict)result = agent.run_sync('Create a person')#> {'name': 'John Doe', 'age': 30}




```

### Validation context

[Section titled Validation context](https://pydantic.dev/docs/ai/core-concepts/output/#validation-context)

Some validation relies on an extra Pydantic [context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context) object. You can pass such an object to an `Agent` at definition-time via its [`validation_context`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent.__init__) parameter. It will be used in the validation of both structured outputs and [tool arguments](https://pydantic.dev/docs/ai/tools-toolsets/tools-advanced#tool-retries).

This validation context can be either:

- the context object itself (`Any`), used as-is to validate outputs, or
- a function that takes the [`RunContext`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext) and returns a context object (`Any`). This function will be called automatically before each validation, allowing you to build a dynamic validation context.

validation\_context.pyDirectGateway

```python
from dataclasses import dataclassfrom pydantic import BaseModel, ValidationInfo, field_validatorfrom pydantic_ai import Agentclass Value(BaseModel):    x: int    @field_validator('x')    def increment_value(cls, value: int, info: ValidationInfo):        return value + (info.context or 0)agent = Agent(    'google-gla:gemini-3-flash-preview',    output_type=Value,    validation_context=10,)result = agent.run_sync('Give me a value of 5.')print(repr(result.output))  # 5 from the model + 10 from the validation context#> Value(x=15)@dataclassclass Deps:    increment: intagent = Agent(    'google-gla:gemini-3-flash-preview',    output_type=Value,    deps_type=Deps,    validation_context=lambda ctx: ctx.deps.increment,)result = agent.run_sync('Give me a value of 5.', deps=Deps(increment=10))print(repr(result.output))  # 5 from the model + 10 from the validation context#> Value(x=15)




```

_(This example is complete, it can be run “as is”)_

### Output validators

[Section titled Output validators](https://pydantic.dev/docs/ai/core-concepts/output/#output-validator-functions)

Some validation is inconvenient or impossible to do in Pydantic validators, in particular when the validation requires IO and is asynchronous. Pydantic AI provides a way to add validation functions via the [`agent.output_validator`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.Agent.output_validator) decorator.

If you want to implement separate validation logic for different output types, it’s recommended to use [output functions](https://pydantic.dev/docs/ai/core-concepts/output/#output-functions) instead, to save you from having to do `isinstance` checks inside the output validator.
If you want the model to output plain text, do your own processing or validation, and then have the agent’s final output be the result of your function, it’s recommended to use an [output function](https://pydantic.dev/docs/ai/core-concepts/output/#output-functions) with the [`TextOutput` marker class](https://pydantic.dev/docs/ai/core-concepts/output/#text-output).

Here’s a simplified variant of the [SQL Generation example](https://pydantic.dev/docs/ai/examples/sql-gen):

sql\_gen.py

```python
from fake_database import DatabaseConn, QueryErrorfrom pydantic import BaseModelfrom pydantic_ai import Agent, RunContext, ModelRetryclass Success(BaseModel):    sql_query: strclass InvalidRequest(BaseModel):    error_message: strOutput = Success | InvalidRequestagent = Agent[DatabaseConn, Output](    'google-gla:gemini-3-flash-preview',    output_type=Output,  # type: ignore    deps_type=DatabaseConn,    instructions='Generate PostgreSQL flavored SQL queries based on user input.',)@agent.output_validatorasync def validate_sql(ctx: RunContext[DatabaseConn], output: Output) -> Output:    if isinstance(output, InvalidRequest):        return output    try:        await ctx.deps.execute(f'EXPLAIN {output.sql_query}')    except QueryError as e:        raise ModelRetry(f'Invalid query: {e}') from e    else:        return outputresult = agent.run_sync(    'get me users who were last active yesterday.', deps=DatabaseConn())print(result.output)#> sql_query='SELECT * FROM users WHERE last_active::date = today() - interval 1 day'




```

_(This example is complete, it can be run “as is”)_

#### Handling partial output in output validators

[Section titled Handling partial output in output validators](https://pydantic.dev/docs/ai/core-concepts/output/#handling-partial-output-in-output-validators)

When streaming with `run_stream()` or `run_stream_sync()`, output validators are called **multiple times** — once for each partial output received from the model, and once for the final complete output.

You should check the [`RunContext.partial_output`](https://pydantic.dev/docs/ai/api/pydantic-ai/tools/#pydantic_ai.tools.RunContext.partial_output) flag when you want to **validate only the complete result**, not intermediate partial values.

When streaming, `partial_output` is `True` for each partial output and `False` for the final complete output.
For all [other run methods](https://pydantic.dev/docs/ai/core-concepts/agent#running-agents), `partial_output` is always `False` as the validator is only called once with the complete output.

partial\_validation\_streaming.pyDirectGateway

```python
from pydantic_ai import Agent, ModelRetry, RunContextagent = Agent('openai:gpt-5.2')@agent.output_validatordef validate_output(ctx: RunContext, output: str) -> str:    if ctx.partial_output:        return output    if len(output) < 50:        raise ModelRetry('Output is too short.')    return outputasync def main():    async with agent.run_stream('Write a long story about a cat') as result:        async for message in result.stream_text():            print(message)            #> Once upon a            #> Once upon a time, there was            #> Once upon a time, there was a curious cat            #> Once upon a time, there was a curious cat named Whiskers who            #> Once upon a time, there was a curious cat named Whiskers who loved to explore            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around            #> Once upon a time, there was a curious cat named Whiskers who loved to explore the world around him...




```

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

## Image output

[Section titled Image output](https://pydantic.dev/docs/ai/core-concepts/output/#image-output)

Some models can generate images as part of their response, for example those that support the [Image Generation built-in tool](https://pydantic.dev/docs/ai/tools-toolsets/builtin-tools#image-generation-tool) and OpenAI models using the [Code Execution built-in tool](https://pydantic.dev/docs/ai/tools-toolsets/builtin-tools#code-execution-tool) when told to generate a chart.

To use the generated image as the output of the agent run, you can set `output_type` to [`BinaryImage`](https://pydantic.dev/docs/ai/api/pydantic-ai/messages/#pydantic_ai.messages.BinaryImage). If no image-generating built-in tool is explicitly specified, the [`ImageGenerationTool`](https://pydantic.dev/docs/ai/api/pydantic-ai/builtin_tools/#pydantic_ai.builtin_tools.ImageGenerationTool) will be enabled automatically.

image\_output.pyDirectGateway

```python
from pydantic_ai import Agent, BinaryImageagent = Agent('openai-responses:gpt-5.2', output_type=BinaryImage)result = agent.run_sync('Generate an image of an axolotl.')assert isinstance(result.output, BinaryImage)




```

_(This example is complete, it can be run “as is”)_

If an agent does not need to always generate an image, you can use a union of `BinaryImage` and `str`. If the model generates both, the image will take precedence as output and the text will be available on [`ModelResponse.text`](https://pydantic.dev/docs/ai/api/pydantic-ai/messages/#pydantic_ai.messages.ModelResponse.text):

image\_output\_union.pyDirectGateway

```python
from pydantic_ai import Agent, BinaryImageagent = Agent('openai-responses:gpt-5.2', output_type=BinaryImage | str)result = agent.run_sync('Tell me a two-sentence story about an axolotl, no image please.')print(result.output)"""Once upon a time, in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!"""result = agent.run_sync('Tell me a two-sentence story about an axolotl with an illustration.')assert isinstance(result.output, BinaryImage)print(result.response.text)"""Once upon a time, in in a hidden underwater cave, lived a curious axolotl named Pip who loved to explore. One day, while venturing further than usual, Pip discovered a shimmering, ancient coin that granted wishes!"""




```

## Optional output (allowing `None`)

[Section titled Optional output (allowing None)](https://pydantic.dev/docs/ai/core-concepts/output/#optional-output)

Some agents perform their work entirely through tool calls and don’t need to produce a final output — for example, an agent that updates a record via a tool and then stops. Certain models (notably [Anthropic](https://pydantic.dev/docs/ai/models/anthropic)) will return an empty response in this case, which by default causes Pydantic AI to retry until the model produces content.

To instead treat an empty response as a successful run, include `None` in the `output_type`:

optional\_output.pyDirectGateway

```python
from pydantic_ai import Agentagent = Agent('anthropic:claude-opus-4-6', output_type=str | None)@agent.tool_plaindef mark_task_done(task_id: int) -> str:    """Mark the task as done."""    return f'Task {task_id} marked done.'result = agent.run_sync('Mark task 1 as done, then stop without saying anything.')print(result.output)#> None




```

When the model returns an empty response and `None` is an allowed output type, the agent will return `None` instead of retrying. [Output validator functions](https://pydantic.dev/docs/ai/core-concepts/output/#output-validator-functions) still run with `None` as the argument, so you can raise [`ModelRetry`](https://pydantic.dev/docs/ai/api/pydantic-ai/exceptions/#pydantic_ai.exceptions.ModelRetry) to reject it if needed.

`output_type=str | None` is the canonical case: it’s handled as regular text output, and the **only** way the model signals `None` is by returning an empty response — there’s no output tool or structured schema involved. This mirrors how plain `str` is already treated specially as free-form text output rather than a structured tool call.

`None` is also supported in the other output modes, with an extra structured commit path in addition to (or in place of) the empty-response fallback:

- **Bare unions including `None` that use tool mode** — e.g. `output_type=int | None`, `output_type=[int, float, None]`, or `output_type=[ToolOutput(Foo), None]`: a dedicated `final_result_NoneType` output tool is exposed alongside the other output tools, so the model can commit to `None` through a tool call. An empty model response is still also treated as `None`, as with `str | None`.
- **Explicit output mode markers** — e.g. `output_type=ToolOutput(int | None)`, `output_type=NativeOutput([int, None])`, or `output_type=PromptedOutput([int, None])`: `None` is included as a branch of the structured schema the wrapper generates. The model commits by calling the tool with `null` (for `ToolOutput`) or by selecting the `NoneType` branch of the discriminated schema (for `NativeOutput`/`PromptedOutput`). An empty response is **not** accepted — once you’ve opted into an explicit structured output mode, the model is expected to commit through the schema.

## Streamed Results

[Section titled Streamed Results](https://pydantic.dev/docs/ai/core-concepts/output/#streamed-results)

There two main challenges with streamed results:

1. Validating structured responses before they’re complete, this is achieved by “partial validation” which was recently added to Pydantic in [pydantic/pydantic#10748](https://github.com/pydantic/pydantic/pull/10748).
2. When receiving a response, we don’t know if it’s the final response without starting to stream it and peeking at the content. Pydantic AI streams just enough of the response to sniff out if it’s a tool call or an output, then streams the whole thing and calls tools, or returns the stream as a [`StreamedRunResult`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult).

### Streaming Text

[Section titled Streaming Text](https://pydantic.dev/docs/ai/core-concepts/output/#streaming-text)

Example of streamed text output:

streamed\_hello\_world.pyDirectGateway

```python
from pydantic_ai import Agentagent = Agent('google-gla:gemini-3-flash-preview')  async def main():  async with agent.run_stream('Where does "hello world" come from?') as result:        async for message in result.stream_text():            print(message)          #> The first known          #> The first known use of "hello,          #> The first known use of "hello, world" was in          #> The first known use of "hello, world" was in a 1974 textbook          #> The first known use of "hello, world" was in a 1974 textbook about the C          #> The first known use of "hello, world" was in a 1974 textbook about the C programming language.




```

Streaming works with the standard [`Agent`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.AbstractAgent.run_stream) class, and doesn't require any special setup, just a model that supports streaming (currently all models support streaming).

The [`Agent.run_stream()`](https://pydantic.dev/docs/ai/api/pydantic-ai/agent/#pydantic_ai.agent.AbstractAgent.run_stream) method is used to start a streamed run, this method returns a context manager so the connection can be closed when the stream completes.

Each item yield by [`StreamedRunResult.stream_text()`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult.stream_text) is the complete text response, extended as new data is received.

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

We can also stream text as deltas rather than the entire text in each item:

streamed\_delta\_hello\_world.pyDirectGateway

```python
from pydantic_ai import Agentagent = Agent('google-gla:gemini-3-flash-preview')async def main():  async with agent.run_stream('Where does "hello world" come from?') as result:      async for message in result.stream_text(delta=True):            print(message)          #> The first known          #> use of "hello,          #> world" was in          #> a 1974 textbook          #> about the C          #> programming language.




```

[`stream_text`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult.stream_text) will error if the response is not text.

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

### Streaming Structured Output

[Section titled Streaming Structured Output](https://pydantic.dev/docs/ai/core-concepts/output/#streaming-structured-output)

Here’s an example of streaming a user profile as it’s built:

streamed\_user\_profile.pyDirectGateway

```python
from datetime import datefrom typing_extensions import NotRequired, TypedDictfrom pydantic_ai import Agentclass UserProfile(TypedDict):    name: str    dob: NotRequired[date]    bio: NotRequired[str]agent = Agent(    'openai:gpt-5.2',    output_type=UserProfile,    instructions='Extract a user profile from the input',)async def main():    user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'    async with agent.run_stream(user_input) as result:        async for profile in result.stream_output():            print(profile)            #> {'name': 'Ben'}            #> {'name': 'Ben'}            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}            #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}




```

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

As setting an `output_type` uses the [Tool Output](https://pydantic.dev/docs/ai/core-concepts/output/#tool-output) mode by default, this will only work if the model supports streaming tool arguments. For models that don’t, like Gemini, try [Native Output](https://pydantic.dev/docs/ai/core-concepts/output/#native-output) or [Prompted Output](https://pydantic.dev/docs/ai/core-concepts/output/#prompted-output) instead.

### Streaming Model Responses

[Section titled Streaming Model Responses](https://pydantic.dev/docs/ai/core-concepts/output/#streaming-model-responses)

If you want fine-grained control of validation, you can use the following pattern to get the entire partial [`ModelResponse`](https://pydantic.dev/docs/ai/api/pydantic-ai/messages/#pydantic_ai.messages.ModelResponse):

streamed\_user\_profile.pyDirectGateway

```python
from datetime import datefrom pydantic import ValidationErrorfrom typing_extensions import TypedDictfrom pydantic_ai import Agentclass UserProfile(TypedDict, total=False):  name: str  dob: date  bio: stragent = Agent('openai:gpt-5.2', output_type=UserProfile)async def main():  user_input = 'My name is Ben, I was born on January 28th 1990, I like the chain the dog and the pyramid.'  async with agent.run_stream(user_input) as result:      async for message, last in result.stream_responses(debounce_by=0.01):            try:              profile = await result.validate_response_output(                    message,                  allow_partial=not last,              )          except ValidationError:              continue          print(profile)          #> {'name': 'Ben'}          #> {'name': 'Ben'}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes'}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the '}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyr'}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}          #> {'name': 'Ben', 'dob': date(1990, 1, 28), 'bio': 'Likes the chain the dog and the pyramid'}




```

[`stream_responses`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult.stream_responses) streams the data as [`ModelResponse`](https://pydantic.dev/docs/ai/api/pydantic-ai/messages/#pydantic_ai.messages.ModelResponse) objects, thus iteration can't fail with a `ValidationError`.

[`validate_response_output`](https://pydantic.dev/docs/ai/api/pydantic-ai/result/#pydantic_ai.result.StreamedRunResult.validate_response_output) validates the data, `allow_partial=True` enables pydantic's [`experimental_allow_partial` flag on `TypeAdapter`](https://docs.pydantic.dev/latest/api/pydantic/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json).

_(This example is complete, it can be run “as is” — you’ll need to add `asyncio.run(main())` to run `main`)_

## Examples

[Section titled Examples](https://pydantic.dev/docs/ai/core-concepts/output/#examples)

The following examples demonstrate how to use streamed responses in Pydantic AI:

- [Stream markdown](https://pydantic.dev/docs/ai/examples/stream-markdown)
- [Stream Whales](https://pydantic.dev/docs/ai/examples/stream-whales)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="what-are-parallel-tool-calls-in-llms.md">
<details>
<summary>What Are Parallel Tool Calls in LLMs?</summary>

Phase: [EXPLORATION]

**Source URL:** <https://airbyte.com/agentic-data/parallel-tool-calls-llm>

# What Are Parallel Tool Calls in LLMs?

Parallel tool calling is a pattern where a large language model (LLM) identifies independent operations, requests them all in a single response, and your infrastructure executes those calls concurrently. Instead of waiting for each tool to finish before starting the next, independent calls run at the same time. Total latency drops from the sum of every tool call to the duration of the slowest one.

This matters as soon as your agent pulls from more than one or two sources. An agent that needs a customer record from Salesforce, recent orders from Snowflake, and open tickets from Zendesk can either query each one in sequence, forcing the user to wait for all three round trips, or request all three at once and get everything back in a single batch.

## **TL;DR**

Here's what matters for parallel tool calls in production:

- In many agents, especially those making application programming interface (API) and database calls, the dominant latency comes from input/output (I/O) rather than LLM inference. Parallel tool calls let the model request multiple external functions simultaneously, typically reducing total latency to the slowest single tool plus the inference cycles needed for planning and synthesis.

- Benchmarks like LLMCompiler show roughly 1.4x to 2.4x latency speedups on many tasks, with some scenarios reaching up to 3.7x. You'll use more tokens per inference step, so plan for a cost-vs-latency tradeoff.

- Provider support varies widely. See the provider comparison table in the implementation section for current behavior.

## **How Do Parallel Tool Calls Work?**

In a standard tool-calling loop, the agent follows a strict sequence: prompt, tool request, execute, return results, repeat. Total latency is the sum of all tool execution times plus an LLM inference cycle for each step.

With parallel tool calling, the model analyzes your prompt and identifies which tools can run simultaneously because they don't depend on each other's outputs. It returns multiple tool calls in a single response. Your orchestration layer runs these concurrently, and all results come back in one batch for the model to synthesize.

One important distinction: the model requests parallel execution, but your framework determines whether the calls actually run concurrently. The code example in the implementation section shows exactly where this matters and why it's the most common source of missed speedups.

## **When Should You Use Sequential vs. Parallel Execution?**

| Use Sequential When | Use Parallel When |
| --- | --- |
| Output of one tool feeds into another as input | Tools have no dependencies on each other |
| Order matters for correctness | Operations are I/O-bound |
| Maintaining state across dependent operations is essential | Multiple independent data sources need querying |
| Debugging and tracing are higher priorities than raw performance | Latency reduction is critical for user experience |
| Tools modify shared state (prevents concurrent access conflicts) | Information from diverse APIs must be aggregated |

If your agent queries a customer relationship management (CRM) system, a data warehouse, and a ticketing system to build context for a response, those lookups can run simultaneously because they don't depend on each other's outputs. For tools that modify state, enforce sequential execution to prevent concurrent access conflicts.

Two caveats are worth noting. If your bottleneck is model reasoning rather than I/O wait, parallelizing tool calls won't help. You'll pay the same inference cost regardless of how you schedule the tools. And if multiple tools hit the same rate-limited API, concurrent calls can trigger throttling and make total latency worse, not better. Profile your actual tool execution times before committing to a parallel-by-default architecture.

The hybrid approach often works best in production. Fast, independent tools execute in parallel while slow operations run separately or get cached. You might fetch user profile, recent orders, and support history in parallel during the initial phase, then use those results sequentially to determine next steps.

## **What Performance Improvements Can You Expect?**

The [LLMCompiler system](https://arxiv.org/pdf/2312.04511) demonstrated up to 3.7x faster execution on specific benchmarks, with many tasks showing speedups in the 1.4x to 2.4x range.

https://cdn.prod.website-files.com/687b2d16145b3601a227c560/69ab1516053dad8a6de26d71_9e50dfb3.jpeg

Suppose three tools each take about 200ms:

| Metric | Sequential | Parallel |
| --- | --- | --- |
| Tool execution (3 tools × 200ms each) | 600ms | 200ms (max of three) |
| LLM overhead | 3 × 500ms = 1,500ms | 1 × 500ms = 500ms |
| Total latency | 2,100ms | 700ms |
| Speedup | -- | 3x |

In practice, the gains depend on how uniform your tool latencies are. If tools take 200ms, 200ms, and 500ms respectively, the parallel batch latency is 500ms, dominated by the slowest tool. You might get better results grouping the two faster tools together and handling the slow one separately.

You'll use more tokens when the model processes multiple tool results at once. In some architectures like LLMCompiler, better planning and fewer reasoning steps can partially offset this overhead or even reduce overall cost relative to naive sequential baselines. If you're [scaling agents](https://airbyte.com/agentic-data/scaling-agentic-ai) in production, that token overhead compounds. Monitor token usage across parallel operations and consider routing tool-result synthesis to a smaller, cheaper model while keeping your primary model for planning and orchestration.

## **What Are Production Use Cases for Parallel Tool Calls?**

[Enterprise search](https://airbyte.com/agentic-data/ai-enterprise-search) is one of the clearest wins. Support teams need information from internal knowledge bases, product-specific documentation, customer configuration history, and compliance guidelines. An agent using parallel tool calls queries all these sources at once and delivers troubleshooting guidance specific to the customer and product configuration, instead of making the support engineer wait for four sequential lookups.

Development tools use the same pattern for context gathering. When you ask for code suggestions, the agent can simultaneously search your codebase for relevant implementation patterns, retrieve related test files, query API documentation, and analyze dependency graphs for compatibility. You get suggestions fast enough to stay in flow instead of waiting and context-switching.

Customer-facing agents see similar benefits. When a user opens a support chat, the agent simultaneously pulls account status from HubSpot, checks inventory levels in the warehouse, looks up shipping tracking from the logistics API, and retrieves relevant product docs. Without parallel execution, that context-gathering phase adds seconds of visible latency before the agent responds. With it, the user sees a single wait no longer than the slowest backend query.

## **How Do You Implement Parallel Tool Calls?**

### **LLM Provider Support**

Provider support varies, and capabilities evolve quickly. Confirm the latest behavior in each provider's official API docs for your specific endpoint.

| Provider | Parallel Support | Configuration |
| --- | --- | --- |
| OpenAI (GPT-4o) | Yes, on supported models/endpoints | Set parallel\_tool\_calls=True; not all models accept this parameter |
| Google Gemini | Yes, automatic | Returns multiple tool calls when appropriate |
| Cohere | Yes, automatic | Returns multiple tool calls when appropriate |
| Anthropic Claude | Provider-managed loop | Does not expose a parallel flag; design assuming one tool call at a time |

### **Framework Support for Concurrent Execution**

| Framework | Approach | Best For |
| --- | --- | --- |
| LangChain / LangGraph | RunnableParallel within LangChain Expression Language; stateful graph with concurrent processing when no dependencies exist | Explicit developer control over parallel composition; multi-agent workflows |
| LlamaIndex Workflows | @step decorator with automatic dependency analysis via directed acyclic graphs | Complex workflows where manual parallelization is error-prone |
| Microsoft AutoGen | Multi-agent conversation patterns with concurrent execution | Teams of AI agents collaborating on complex tasks |
| CrewAI | Parallel role-based "crew" architectures | Tasks requiring multiple specialist agents |

All four frameworks support concurrent execution when dependencies permit, though the specifics vary by framework and provider adapter.

### **Basic Implementation Example**

The model decides which tools can run simultaneously, but your code must actually run them concurrently. Without asyncio.gather (or equivalent concurrency), you get the same latency as sequential execution regardless of what the model requested. This is the most common mistake in parallel tool call implementations: the model returns parallel requests, the developer processes them in a for-loop, and the expected speedup never shows up.

## **How Do You Take Parallel Tool Calls to Production?**

### **Session Isolation for Concurrent Tools**

Concurrent tool calls introduce a class of bugs you don't see in sequential execution: credential bleed. If two tools share a security context, one tool's authentication token can leak into another's request, especially when connection pooling or shared HTTP clients are involved. Give each invocation its own scoped, short-lived credentials. This way a bug or compromise in one tool path can't access another tool's data.

For broader patterns like least-privilege service accounts and dynamic authorization, see the full [agent security guide](https://airbyte.com/agentic-data/ai-agent-security).

### **Monitoring Concurrent Execution**

[OpenTelemetry](https://opentelemetry.io/) provides a widely adopted instrumentation layer for distributed tracing. Each concurrent tool invocation receives its own span with attributes identifying tool type, parameters, and execution context. Links connect related spans so you can trace relationships between concurrent tool calls and identify which tool dominated batch latency.

Track these metrics across parallel tool execution:

| Metric | Description | Alert Threshold |
| --- | --- | --- |
| batch\_latency\_ms | Total time from dispatch to last tool completion | \> 2x median of slowest individual tool |
| slowest\_tool\_ms | Execution time of the longest-running tool in a batch | \> p95 of that tool's historical latency |
| tool\_success\_rate | Percentage of tools completing without error per batch | < 95% over a 5-minute window |
| concurrent\_execution\_ratio | Actual parallel execution vs. sequential baseline | < 0.5 (tools are serializing) |
| token\_overhead\_ratio | Tokens used in parallel batch vs. equivalent sequential calls | \> 1.5x sequential baseline |

For observability platforms, tools like Phoenix and LangWatch trace agent workflows from prompt to tool execution to response.

### **Error Handling and Partial Failures**

When one tool in a parallel batch fails, you can either fail the entire batch, return partial results, or retry only the failed tool while caching results from tools that succeeded. The retry approach works best in most cases because you don't waste successful work and the model gets explicit context about what's missing.

Set up per-tool circuit breakers with exponential backoff that track failure rates independently. A circuit breaker monitors consecutive failures for a given tool and temporarily stops calling it once a threshold is reached, preventing a single flaky API from cascading into your entire parallel pipeline. Use a degraded state so your agent continues with reduced functionality. Answering from three out of four data sources is better than returning nothing. Tell the model explicitly when a source was unavailable through the system prompt so it can qualify its answer rather than [hallucinate](https://airbyte.com/agentic-data/prevent-llm-hallucinations) to fill the gap.

## **What's the Right Way to Build Parallel Tool Architectures for Production?**

Most teams get the orchestration layer working quickly. LangGraph or LlamaIndex handle the parallel dispatch and dependency resolution well. The problem shows up one layer down, at the [data infrastructure](https://airbyte.com/agentic-data/ai-data-infrastructure). When three tools fire simultaneously, they're all waiting on the same database connection pool, competing for the same API rate limit, or breaking because a source changed its OAuth flow or response schema last week. Orchestration frameworks don't manage those concerns for you.

## **Frequently Asked Questions**

### **How do I prevent agents from executing dependent tools in parallel?**

Write clear tool descriptions that explicitly note dependencies, like "REQUIRES: Output from fetch\_article tool as input." At the orchestration layer, deploy explicit dependency validation through dependency graphs before executing parallel tool calls. Some frameworks like LlamaIndex's LLMCompiler automatically analyze dependencies, while others require manual specification.

### **How do I handle partial failures in parallel tool batches?**

Retry the failed tool while caching successful results. Don't discard work that already completed. The critical step most teams miss is telling the model which source failed. Include the unavailable source name and error type in the tool result so the model can qualify its response instead of guessing.

### **Can I use parallel tool calls with open-source models?**

Yes, but parallel execution depends more on your orchestration framework than the model itself. Models like Llama 3 and Mistral support tool calling, but actual concurrent execution requires framework-level orchestration through LangGraph, LlamaIndex, or AutoGen.

### **How do I manage rate limits across concurrent tool calls?**

Use per-source token buckets that coordinate across concurrent invocations so three parallel calls to the same Salesforce instance share one rate limit pool. If you're managing connections through Airbyte's connectors, each connection handles its own API rate limiting without additional coordination code.

### **How do I estimate the cost impact of parallel tool calls?**

Parallel execution uses more tokens per inference step because the model processes multiple tool results at once. Monitor token\_overhead\_ratio (parallel tokens vs. sequential baseline) and consider routing tool-result synthesis to a smaller model while keeping your primary model for planning.

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

Hello, everybody. Welcome to The Neural Maze. [00:00]
So, in today's video, we are going to keep working on the project of implementing the four agentic patterns from scratch that we started a week ago, when we implemented the reflection pattern. So today, we're going to move into the second pattern, that is the Tool Pattern. And before we begin, I'm pretty sure that you're already familiar with this pattern in a practical sense. What I mean by this is that you have probably used in the past tools in LangChain, Llama Index, or in CrewAI. [00:30] And the thing is that in today's video, I'm not going to teach you how to use these tools in specific frameworks. I'm just going to teach you how these tools work under the hood. And I think that's really insightful because if we really understand how things work under the hood, I think it's much easier for us to learn how to apply them in the proper way. [01:00]

So, as we did in the previous video, we are going to start with a Jupyter Notebook that covers all the theory step-by-step, and then I will move into VS Code, where I will show you all the abstractions and all the classes that I have implemented to make this tool more robust, to try to mimic the structure that all of these frameworks offer at this moment. You know, having like a tool class and a tool agent class. Very similar to what we did with the reflection pattern, but with with the tool pattern. [01:30] Okay, so let's begin with the theory of the tool pattern. You have this diagram right here, that tries to offer a simplified description of what the pattern does or tries to implement under the hood. But basically, let's start by defining what is a tool. And a tool, let's put it in simple terms, it's just a way for the LLM to access the outside world. [02:00] And what do I mean by this? Uh, remember that LLMs store all the information in their weights. So when you ask an LLM about specific information, that information is going to be retrieved by the weights. But sometimes, the information stored in these weights is not enough. And we need a way for the LLM to access the outside world, and that's exactly what a tool does. A tool is just a like a Python function that the LLM can access and run and fetch some relevant results. [02:30] Using an API or a parsing a web content or a consulting a Wolfram Alpha to to calculate some difficult integrals. But you get the point, it's a way for the LLM to get outside the information stored in its weights. Okay, so let's start by defining a simple Python function. [03:00] (Shows the `Tool Use Pattern` diagram in a Jupyter notebook) You have it in here. So, uh, this Python function, which I'm a bit ashamed of it, because it's a too simple. Uh, basically gets the current weather. And as you can see, uh, if location is Madrid, it's going to return a temperature of 25, uh, it varies on the unit that you want to to put, but given that it's Madrid, it will be unit Celsius, so it's going to return a temperature of 25 degrees Celsius. [03:30] (Shows the Python code for `get_current_weather` function) And otherwise, it's going to return 58. So, as you can see, don't don't pay too much attention to this function because it's trivial, but, uh, it will help us to illustrate how a tool works. So, if we run this, as I was saying, if we if we run this function with location Madrid and unit Celsius, it's going to return this, um, dictionary, well, this string, containing a dictionary, with temperature 25 and unit, uh, Celsius. [04:00] (Shows example output of the `get_current_weather` function) Okay. So, nothing to add about this. This is trivial. So, let's proceed. Now, the question is, how can we make this function available to an LLM? Because as you already know, LLMs are just NLP systems and natural language processing systems. So, they expect text as input. But we need a way to for the LLM to really understand that this is a Python function and I can call this Python function to retrieve some relevant results. And how can we do that? [04:30] Okay. So, what I propose here is to use this system prompt. So, as you can see, in this system prompt, we are telling the LLM to behave as a function calling AI model. We are going to provide the function signatures within these XML tags, these, uh, tools tags. And you may call one or more functions to assist with the user query, don't make assumptions about values, blah, blah, blah. Okay, but the important thing is that we are going to pass all the relevant information within this XML tag. [05:00] (Shows the system prompt structure for tool definition) And the LLM is going to return the function call inside this XML tag. Okay, this tool underscore tag, uh, underscore call, sorry. You can see here an example of how we expect the LLM to return the tool call. This is going to be something like this. We are going to, uh, the LLM is going to provide a name, the name of the function, and also the arguments that we need to use to retrieve the relevant information with this Python function. [05:30] And then a list of the available tools. In this case, uh, I'm just using this one, like `get_current_weather` because, uh, I needed to hard code everything for this, uh, tiny example. But as you will see in the VS Code, we are going to make it automatic. So, giving a Python function, we are going to retrieve all of this information, all of this, uh, function signature. [06:00] It's going to be retrieved automatically in the VS Code, uh, implementation. But yeah, if you checked the way the information that we are providing for each tool. You can see that we are providing the name of the tool, a description. This is something that we can get from the docstring, by the way. You will see that later. But yeah, like `get_current_weather` in a given location, blah, blah, blah. And then the parameters where we are putting all the different parameters, and this is really important, the type of these parameters. [06:30] (Highlights various parts of the tool definition: name, description, parameters, and their types) In this case, both the location and the unit are going to be strings, but suppose that we are passing, I don't know, uh, the month, and we want it to behave like an integer, then we should put that type inside the the function signature. Okay, so now that we know how this system prompt works, let's put it into practice. [07:00] (Shows the system prompt defined as a Python constant) Just a quick reminder. Today, we are going to use a different LLM than the previous video. In the previous video, we were using Llama 3 70 billion, but today we are going to use a slightly different LLM because it's the Llama 3 70 billion tool use. So, it's a version of Llama 3 that's been fine-tuned for tool use, and that's exactly what we want to do today. So, it made sense to to use this LLM. Okay, uh, we defined, uh, a constant, uh, the system prompt, um, where we copy and paste the system prompt that I shared with you right in in the cell below. [07:30] (Shows the Python code for generating chat history with the system prompt and user message) And now, let's run this cell. We are going to ask the LLM, what's the current temperature in Madrid in Celsius. We're going to add the system prompt, and we are also going to add the user, uh, message to the history. And yeah, let's run this. Okay. So, as you can see, we are having a structure similar to the one we asked for the LLM to return in the system prompt. [08:00] (Shows the LLM's output, which is an XML-like string containing the tool call) The LLM is returning the name of the tool, and it's also returning the arguments. Since we asked, what's the current temperature in Madrid in Celsius, the argument is going to be Madrid as the location and Celsius as the unit. Okay. But now, this is not usable for the by the LLM. I mean, we have a string, and inside that string, we have this dictionary inside these two XML tags. [08:30] (Highlights the tool call output in XML-like string) So, we need a way to get rid of the XML tags and also transform this dictionary, this string dictionary, into a proper dictionary using the JSON package, the JSON library. Okay, and that's exactly what this function does. This function will get rid of the tool call, or to be more specific, it will gather, it will get the code inside the tool call XML tags. [09:00] (Shows a Python function `parse_tool_call_xml_str` that processes the LLM's output) And then it will transform that string dictionary into a proper dictionary. So, let me show you how it works. Uh, but as you can see, when we call this parse tool call string, this method, to the output, the output, remember that it's uh this one here. [09:30] (Shows the parsed output as a Python dictionary) It's going to return a proper Python dictionary. And now, if we run the `get_current_weather`, the function that we defined at the beginning of the notebook, if we run this function, with the parameters that we have just, uh, parsed, it will return the result. So, temperature 25 and unit, it's going to be Celsius. [10:00] (Shows the `get_current_weather` function being called with the parsed arguments and its output) Okay, without any information about the XML tags. That's something that we want to get rid of. Nice. Okay. So, now we have the result. As you can see, it's this Python dictionary right here. But we are not over because we don't want the LLM to respond with this structure. I mean, if I ask the LLM for the current temperature in Madrid, I expect the LLM to respond me something like, "The current temperature in Madrid is, uh, is 25 degrees Celsius," for example. But not something like this, not this, uh, dictionary. [10:30] So, the last thing that we need to do is to add this observation, the dictionary in here. To the chat history. Okay? And we are going to add this into the prompt, this observation, uh, the observation text into the prompt. Okay. So, now the only thing that's missing is to make another call to to the LLM in Grok, and we will receive the output. [11:00] (Shows appending the observation to the chat history and making a final LLM call) Okay. So, now that we understand how all of these classes and abstractions work, I think it's going to be really cool to see everything in action, and that's what we are going to cover next. So, uh, everything is inside this section of implementing everything the good way. Of course, you have to understand that this implementation, it's not like the perfect implementation, because, uh, I'm not trying to create another framework, and I'm just trying to make something that's, uh, well implemented, but at the same time, easy to understand. So, so yeah, uh, just bear in mind that we are not trying to to create another agentic framework, in this case. Okay. So, uh, let's continue. [11:30] (Switches to VS Code to demonstrate the tool pattern implementation) Let's see how the tool decorator works. And instead of using some dummy, uh, function. In this case, we are going to implement something more, uh, something closer to to reality. Something closer to the tools that you might be wanting to implement in the future. So, uh, in this case, the the function that I have implemented, it's a function that fetches the top `n` stories from Hacker News. If you don't know what Hacker News, uh, is, it's a very famous, uh, page where you have different types of of stories, and many of them, uh, link to some article, another to GitHub repositories, to tweets, to whatever. [12:00] (In VS Code, shows the project structure, including `tool_pattern`, `tool_agent.py`, `tool.py`, `utils.py`. Opens `tool.py`. Shows `get_fs_signature` method in Python code.)
*The introduction covers the video's purpose: to continue implementing agentic patterns from scratch, focusing on the Tool Pattern by explaining its underlying mechanics rather than just framework usage.*

Okay, so here we are in VS Code. Let me show you the new modules that I have added to the repository. So, if you go to the source agentic patterns folder, you will find a new folder, the tool pattern folder. And inside, you have three modules: the tool agent, the tool, and the utils. Uh, let's begin with the tool, because I think it's the most important topic of today's video. And the tool agent, at the end of the day, it's just a way to interact with the tool. Okay, so this module starts by implementing a method that allows you to get the signature out of a Python function. So, this is basically the method I'm referring to. It receives as parameter a function, and it will, uh, get the schema, and out of the schema, also the function signature. And the function signature is basically the structure that we defined on the system prompt previously. All right. Next, we have this class right here, the tool class, that has three attributes: a name, the function, and the function signature. The function signature, as you might imagine, uh, it's going to be generated by this function right here. And the function, it's basically the function that we want to call when the LLM, uh, decides that it wants to use a specific tool. This function is the Python function that's going to be used under the hood. Then we have this tool decorator that, uh, can be used to decorate your Python function and to automatically transform the Python function into a tool object. If you inspect a little bit the implementation of this decorator, First, uh, you can see that it generates the function signature out of the `get_function_signature` method that we explained before. And then it returns a tool object by, uh, defining the name, using the function signature, passing the the function that you are decorating as the function attribute that the tool expects, and finally, getting the function signature, uh, from the variable that we defined previously, because remember that we were getting the function signature using this method, and, uh, and yeah, and having these three attributes, we are able to to generate a tool. Okay. Now, let's move into the tool agent, which, as you can imagine, is an agent that has the capability of using tools. [14:30]
*This section details the `tool.py` module, covering the `get_fs_signature` method for extracting function signatures, the `Tool` class for encapsulating functions and their metadata, and the `tool` decorator for automatically converting Python functions into `Tool` objects.*

You pass a list of tools, and it will, uh, select the proper tool, the the right tool, for the specific question that we are asking, and then it will run the tool to fetch the relevant details that it needs from the outside world, and then returning all this information in a natural language to you. Okay, so things that you are already familiar with. So, this tool system prompt is basically the one that we explained earlier in the video. And then the tool agent consists of the following attributes. So, it we need to generate the Grok client, then the model that remember that by default, we are going to use the Llama 3 70 billion tool use. [15:00] Then this is the important part. This is the the tricky part of this agent. But we need to define the list of tools that we are going to to use for this agent. And then this list of tools are going to be used in the `run` method. So, the `run` method, uh, consists of the following steps. First of all, we expect this user message, and we transform the user message into a user prompt using the OpenAI API definition. Then we are going to generate both the tool chat history and the agent chat history. [15:30] Now we are going to generate the first completion. We are going to make the first call to the Grok model. And what this is going to do, these two blocks of code, is to generate basically the logic that we explained in the notebook. Let me be specific. So, it's going to, first of all, return the tool call. Okay? This first, uh, call, uh, this tool call string is basically this output. And then the `parse_tool_call_string` it's a method that mimics the same logic that we implemented in this function. Okay? So, at the end, this, uh, tool call is going to be something like this. Okay? So, now that we have the tool call information, we can get the tool name from from this object, from the tool call. We can also get the the tool by using this tools dict, because now that we have the tool name, we have also defined a dictionary that contains a relationship between, uh, the tool name and the tool. Okay? Then we are going to validate the arguments. So, to make sure that if, uh, the function expects, uh, string, the LLM is not sending an integer. We want to make sure that the types that the LLM has generated in the tool call and the types expected by the Python function match. Okay? [17:15]
*The `tool_agent.py` module's `ToolAgent` class is detailed, explaining how it orchestrates tool usage by accepting a list of tools, defining the system prompt for LLM interaction, and implementing a `run` method that handles user prompts, LLM calls, tool execution, and response generation, including argument parsing and validation.*

And then we are just going to run the tool with this tool run and we are passing the arguments that we have just, uh, defined on the tool call. Remember that if we go to to the tool call, remember that we had these arguments key that contains the arguments and its values to to achieve the to retrieve the the proper information. Okay? And finally, we are going to append this result to the chat history. And remember that we are adding this by using this observation prompt. Okay, so now the only thing that's missing is to make another call to to the LLM in Grok, and we will receive the output. [18:00]
*This section demonstrates the `ToolAgent`'s `run` method, specifically how it processes an LLM's tool call response by parsing the output, validating arguments against the tool's signature, executing the tool function, and appending the observation to the chat history before generating the final LLM response.*

Okay. So, now that we understand how all of these classes and abstractions work, I think it's going to be really cool to see everything in action, and that's what we are going to cover next. So, uh, everything is inside this section of implementing everything the good way. Of course, you have to understand that this implementation, it's not like the perfect implementation, because, uh, I'm not trying to create another framework, I'm just trying to make something that's, uh, well implemented, but at the same time, easy to understand. So, so yeah, uh, just bear in mind that we are not trying to to create another agentic framework, in this case. Okay. So, uh, let's continue. [18:30]
*The video transitions to demonstrate a more practical example of the Tool Pattern using a `Hacker News` API and the custom `ToolAgent` and `Tool` decorator from VS Code.*

Let's see how the tool decorator works. And instead of using some dummy, uh, function. In this case, we are going to implement something more, uh, something closer to to reality. Something closer to the tools that you might be wanting to implement in the future. So, uh, in this case, the the function that I have implemented, it's a function that fetches the top `n` stories from Hacker News. If you don't know what Hacker News, uh, is, it's a very famous, uh, page where you have different types of of stories, and many of them, uh, link to some article, another to GitHub repositories, to tweets, to whatever. [19:30] (Shows the `fetch_top_hacker_news_stories` Python function and then a browser view of the Hacker News website) It's very very used by by a lot of people, so I thought it would be cool to have these, uh, this function that allows you to retrieve top number of these functions of these, uh, stories, sorry. And and yeah, to convert this, to transform this function into into a tool. Okay. So, let me show you first of all, that the Python function works properly. [20:00] So, if we run the `fetch_top_hacker_news_stories` with a top `n` of five, it's going to take the top five stories. Let's check the first one, too much efficiency makes everything worse, that we saw in the Hacker News page. And if we click the URL attached, you can see that everything seems to be working fine. [20:30] (Shows the output of `fetch_top_hacker_news_stories` function, then demonstrates applying the `tool` decorator to it) I mean, it's not like the agent redirected us to some broken URLs, I mean the URLs are real and it's, uh, it's working as expected. So, yeah, this is everything I wanted to teach you about tools. My hope is that now when you start using or keep using, uh, tools from LangChain, Llama Index, or CrewAI, you have a deeper understanding how these objects, uh, work under the hood. And and this is everything for today. I hope you have enjoyed the video. Subscribe to the channel, if you haven't and if you like the content. Click the like button, if you you have enjoyed this video. And I'll see you in the next video. [24:26]
*The video concludes by demonstrating the custom `ToolAgent` successfully fetching and presenting the top 5 Hacker News stories in a human-readable format, emphasizing the value of understanding the underlying mechanics of tool usage.*

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Building AI Agents from scratch - Part 1: Tool use</summary>

# Building AI Agents from scratch - Part 1: Tool use

**Source URL:** <https://www.newsletter.swirlai.com/p/building-ai-agents-from-scratch-part>

### Let's implement AI Agent from scratch without using any framework. Today we implement the tool use capability.

Dec 21, 2024

* * *

This is the first article in the series where we will build AI Agents from scratch without using any LLM orchestration frameworks. In this one you will learn:

- What are agents?

- How the Tool usage actually works.

- How to build a decorator wrapper that extracts relevant details from a Python function to be passed to the LLM via system prompt.

- How to think about constructing effective system prompts that can be used for Agents.

- How to build an Agent class that is able to plan and execute actions using provided Tools.

You can find the code examples for this and following projects in GitHub repository here:

[AI Engineer's Handbook](https://github.com/swirl-ai/ai-angineers-handbook)

If something does not work as expected, feel free to DM me or leave a comment, let’s figure it out together!

* * *

> “The future of AI is Agentic.”

> “Year 2025 will be the year of Agents.”

These are the phrases you hear nowadays left and right. And there is a lot of truth to it. In order to bring the most business value out of LLMs, we are turning to complex agentic flows.

### What is an AI Agent?

In it’s simplest high level definition, an AI agent is an application that uses LLM at the core as it’s reasoning engine to decide on the steps it needs to take to solve for users intent. It is usually depicted similar to the picture bellow and is composed of multiple building blocks:

https://substackcdn.com/image/fetch/$s_!fVcp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3eb64772-fbb5-4f2d-8120-d473c74fe124_2926x2198.png AI Agent

- Planning - the capability to plan a sequence of actions that the application needs to perform in order to solve for the provided intent.

- Memory - short-term and long-term memory containing any information that the agent might need to reason about the actions it needs to take. This information is usually passed to LLM via a system prompt as part of the core.

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

* * *

</details>

<details>
<summary>Efficient Tool Use with Chain-of-Abstraction Reasoning</summary>

# Efficient Tool Use with Chain-of-Abstraction Reasoning

**Source URL:** <https://arxiv.org/pdf/2401.17464v3>

## Abstract

To achieve faithful reasoning that aligns with human expectations, large language models (LLMs) need to ground their reasoning to real-world knowledge (e.g., web facts, math and physical rules). Tools help LLMs access this external knowledge, but there remain challenges for fine-tuning LLM agents (e.g., Toolformer) to invoke tools in multi-step reasoning problems, where inter-connected tool calls require holistic and efficient tool usage planning. In this work, we propose a new method for LLMs to better leverage tools in multi-step reasoning. Our method, Chain-of-Abstraction (CoA), trains LLMs to first decode reasoning chains with abstract placeholders, and then call domain tools to reify each reasoning chain by filling in specific knowledge. This planning with abstract chains enables LLMs to learn more general reasoning strategies, which are robust to shifts of domain knowledge (e.g., math results) relevant to different reasoning questions. It also allows LLMs to perform decoding and calling of external tools in parallel, which avoids the inference delay caused by waiting for tool responses. In mathematical reasoning and Wiki QA domains, we show that our method consistently outperforms previous chain-of-thought and tool-augmented baselines on both in-distribution and out-of-distribution test sets, with an average $\sim 6\%$ absolute QA accuracy improvement. LLM agents trained with our method also show more efficient tool use, with inference speed being on average $\sim 1.4\times$ faster than baseline tool-augmented LLMs.

## 1 Introduction

Recent large language models (LLMs), have made progress at interpreting and executing instructions, but still make errors when recalling and composing world knowledge for their responses, e.g., making unfactual statements, incorrect calculations, etc. Using auxiliary tools (e.g., a search engine to provide credible facts, a calculator for accurate math operations, etc.) at inference time can mitigate some of these errors, motivating tool-augmented language models that integrate external API calls into their output generations.

However, we show that current tool-augmented LLMs, e.g., Toolformer, struggle to reliably and efficiently leverage tools in multi-step reasoning. In particular, tool calls in multi-step reasoning tasks are often interleaved (i.e., the response of an API call is often part of the query of a subsequent call; as shown in Figure 1). Without explicitly modeling these interconnections in reasoning chains, LLMs do not learn effective planning for tool use, which leads to less accurate reasoning with tools (as verified by our analysis in Section 5). Meanwhile, interleaving text generation with API calls also introduces inefficient inference “waiting times,” where the model must wait for the response from the API call before resuming the decoding process. This inefficiency becomes more significant in multi-step reasoning scenarios, when multiple rounds of API calls are typically required for each reasoning process.

In this work, we propose Chain-of-Abstraction (CoA) reasoning, a robust and efficient method for LLMs to perform multi-step reasoning with tools. As shown in Figure 1, LLMs are fine-tuned with a goal of making reasoning chains with abstract placeholders. The placeholders do not affect LLMs’ reasoning flow, and are subsequently infilled with specific knowledge retrieved from specialized tools, to ground the final answer generations. Planning abstract chain of reasoning encourages LLMs to inter-connect multiple tool calls and adopt more feasible reasoning strategies, which are robust to the variation of domain knowledge involved in each reasoning process, e.g., specific calculation results. Unlike previous methods where LLM decoding and API calls are executed in an interleaved manner, our method leverages tools to infill knowledge once after the whole chain of reasoning is generated. This enables more efficient decoding across multiple examples (e.g., as in a stream) because CoA traces for subsequent examples can be decoded while tool calls are made for the preceding ones, amortizing overall inference time. We develop a simple pipeline to build fine-tuning data for models to learn CoA, where we first prompt LLMs to re-write existing responses to instructions as abstract chains, and then use domain tools to check the validity of re-writing, as shown in Figure 2.

After training LLMs to learn CoA reasoning, we evaluate the finetuned models on two representative multi-step reasoning domains, including mathematical reasoning, and Wikipedia (Wiki) QA that involves reasoning on factual descriptive knowledge. We show that our method boosts LLMs’ performances, with average $\sim 7.5\%$ and $4.5\%$ absolute accuracy improvements on math and Wiki QA, respectively. These improvements are consistent across both in-distribution and (zero-shot) out-of-distribution test sets, and are especially pronounced on questions that require complex chain-of-thought reasoning (e.g., more than 3 steps of math derivations). Meanwhile, our method also uses tools more efficiently than previous augmentation methods, with average $\sim 1.47\times$ and $1.33\times$ faster inference speeds on math and Wiki QA tasks, respectively. Finally, extensive human evaluation demonstrates that our method guides LLMs to learn more accurate reasoning, which leads to $\sim 8\%$ fewer reasoning errors.

## 2 Related Work

### Tool-Augmented LLMs

There is growing interest in augmenting LLMs using external tools. Considerable work has tried to adapt LLMs as tool-using reasoners through in-context learning, demonstrating promising performance improvements in various applications, e.g., math problem solving, biomedical question answering and self-critiquing. Nevertheless, guiding LLMs to effectively use tools using in-context demonstrations is challenging, which requires elaborate task-specific prompt engineering and is restricted by the model’s instruction following ability. Noticing the limitations of in-context learning, several works teach LLMs to learn the usage of tools by fine-tuning, which more robustly improves LLMs’ performance. However, all above approaches adopt sequential interactions with tools throughout reasoning, slowing the inference speed as a function of the latency of the tool (or API) and the number of API calls that are made.

Some other prior works focus on using LLMs for multi-step reasoning with other modules. In particular, ReAct and FireAct integrate LLMs with tools into a closed loop of thought, action and observation steps. This verbose reasoning loop slows down the LLM decoding, and still incorporates tools via sequential interactions, resulting in inefficient inference. Another line of work, Program of Thoughts, DECLARATIVE and PAL prompt LLMs to generate program-based reasoning and interact with code executors, which however heavily rely on closed source coding models, i.e., Codex, and are restricted to procedural arithmetic reasoning. Building on these works, CoA proposes a framework to convert natural language reasoning traces into abstract representations, and uses the abstract reasoning traces as fine-tuning data to improve tool-augmented LLMs. CoA also accelerates tool-augmented reasoning, by holistically planning the CoA traces and calling tools only once at inference time.

### Tool Usage Planning

Several previous works research tool usage planning in LLMs. Specifically, HuggingGPT, Chameleon, OpenAGI and MetaTool focus on planning the high-level sequence of using multiple tools to address multi-domain mixed tasks. Similarly, LATM, ML-BENCH and Gorilla aim at planning program-level integration of multiple APIs for designing scripts of procedural tasks, e.g., a script for training a model described by a GitHub repository. ToolChain* combines the planning of tool usage with tree-search-based reasoning, which is especially useful for procedural tasks. Different from above work, we focus on the planning of general chain-of-thought reasoning with awareness of domain specialized tools.

## 3 Method

![Figure 2](x2.png)
**Figure 2:** Illustration of gold data re-writing for fine-tuning data construction. Given a pair of domain question (green scroll) and gold answer (yellow scroll), an LLM is prompted to re-write the gold answer as a reasoning chain with abstract variables (purple bubble). Then, domain specialized tools validate the correctness of the re-writing by checking whether the abstract chain can be reified to get the final answer (orange label).

### Chain-of-Abstraction (CoA) Reasoning

Our method decouples the general reasoning of LLMs from domain-specific knowledge obtained from external tools. Figure 1 shows an overview of our method. In particular, we first fine-tune LLMs to generate reasoning chains with abstract placeholders, e.g., $y1$, $y2$ and $y3$ (We also test placeholders in single-character format, e.g., $x$, $y$ and $z$, but these led to sub-optimal results), as shown in Figure 1. In the second stage, we reify each reasoning chain by replacing placeholders with domain-specific knowledge obtained from external tools, e.g., calculation results from a calculator, relevant articles retrieved from web search engine, etc. Finally, the question is answered based on the reified reasoning chain.

Note that since the LLMs are trained to generate abstract chain of reasoning instead of regular chain-of-thought (CoT) reasoning with explicit values, this enables LLMs to focus on learning general and holistic reasoning strategies without needing to generate instance-specific knowledge for the model’s parameters. Moreover, decoupling general reasoning and domain-specific knowledge enables LLM decoding to proceed and switch between different samples in parallel with API calling (via a pipeline), i.e., LLM can start generating the next abstract chain while the tool fills the current chain, which speeds up the overall inference process.

### Fine-tuning Data Construction

To construct chain-of-abstraction (CoA) data for fine-tuning LLMs, we collect question answering (QA) samples from existing open-source QA datasets, and prompt LLaMa-70B to re-write the answer of each sampled question, as shown in Figure 2. Specifically, we prompt LLaMa-70B to label the spans in gold answers that correspond to knowledge operations (e.g., math derivations, statements based on Wikipedia references) and then to re-write the sentences with labeled spans as fillable CoA traces, where the operation results are replaced with abstract placeholders. For example, the two derivations in the example in Figure 2 are re-written as "[20+35=y1]" and "[90-y1=y2]", respectively.

Note that an intermediate knowledge operation result may appear multiple times in an answer, e.g., in Figure 2, the first equation’s result $55$ is used in the second equation. We prompt LLaMa-70B to replace all occurrences of the same intermediate result with the same placeholder, thereby explicitly connecting the multiple reasoning steps. To ensure that the re-written data is accurate, we use domain-specialized tools to verify the correctness of each CoA reasoning trace (Detailed implementations of reasoning chain verification are described in Sections 4.1 and 4.2). Specifically, we use the tools to execute the labeled operations in each CoA, and only keep questions whose CoA can be infilled with valid results by the tools.

## 4 Experimental Settings

We conduct our experiments on two representative domains: mathematical reasoning and Wikipedia (Wiki) QA, which involves commonsense and logical reasoning on factual descriptive knowledge.

### 4.1 Mathematical Reasoning

Given a math question, the QA system needs to generate a natural language solution to the problem with step-by-step arithmetic derivations (as demonstrated in the left column of Figure 1). We assume that the derivations involved in the solution are the specialized knowledge operations required in this domain, which are labeled in square brackets with derivation results being replaced by abstract placeholders, e.g., "[20+35=y1]".

#### Datasets

We construct most of our fine-tuning CoA data by re-writing the GSM8K training set, which contains 7473 linguistically diverse grade school math problems. As GSM8K dataset focuses on multi-step reasoning, it lacks coverage of single-step arithmetic problems, so we also re-write an additional set of 691 single-step math problems from the ASDiv dataset. Across these re-written datasets, we find that $\sim 76.6\%$ of the CoA reasoning traces generated by LLaMa-70B are verified by our equation solver (described below). Table 1 shows the reasoning step distribution (i.e., number of derivations) of our constructed fine-tuning data.

**Table 1: Reasoning step distribution of correctly re-written reasoning chains in math domain.**

| Source | Reasoning Step |       |       |       |       |       |       |
| :----- | :------------- | :---- | :---- | :---- | :---- | :---- | :---- |
| 1      | 2              | 3     | 4     | 5     | >5    | All   |       |
| GSM8K  | 8              | 1540  | 1648  | 1164  | 666   | 553   | 5579  |
| ASDiv  | 677            | 0     | 0     | 0     | 0     | 0     | 677   |

For an in-distribution evaluation, we test models on GSM8K and ASDiv, containing 1319 and 2305 testing problems. To further test the models’ generalization ability, we also conduct zero-shot evaluation on other representative math datasets, including SVAMP and MAWPS, which contain 1000 and 2065 testing samples, respectively (For the MAWPS benchmark, we test on the 395, 508, 562 and 600 math problems from AddSub, SingleEq, SingleOp and MultiArith portions, respectively).

#### Domain Tool

We use an equation solver to perform the arithmetic derivations required in the math domain. Our equation solver first extracts the derivations labeled in the CoA reasoning, e.g., "[20+35=y1]" and "[90-y1=y2]", and combines all derivations into a system of equations. Then the system of equations is solved by the SymPy toolkit (https://www.sympy.org/en/index.html), to get the true value of each variable (i.e., the value of the abstract placeholder). Finally, our equation solver returns the reified chain of reasoning by replacing all the variables with their solved true values (including the final answer).

**Table 2: Example of CoA fine-tuning data construction in Wiki QA domain.**

| Question    | The director of the romantic comedy “Big Stone Gap” is based in                                                                               |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| what New York city? |                                                                                                                                             |
| Answer      | Greenwich Village                                                                                                                                   |
| Wikipedia   | Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic                                                                                    |
| References  | comedy film directed by Adriana Trigiani.                                                                                                           |
|             | Adriana Trigiani > Adriana Trigiani is an Italian American film                                                                                     |
|             | director based in Greenwich Village.                                                                                                                |
| CoA Trace   | Find the [director of romantic comedy “Big Stone Gap” -Wiki-> y1].                                                                                  |
|             | The name of this film’s director is [y1 -NER(person)-> y2].                                                                                         |
|             | Then determine [y2 in what New York city -Wiki-> y3].                                                                                              |

### 4.2 Wikipedia QA

Given a question based on Wikipedia knowledge, the model needs to first identify Wikipedia articles as references related to the question, and then reason on key knowledge in the reference articles to answer the question (as shown in the right column of Figure 1). We assume that the specialized knowledge operation in this domain is the retrieval of relevant Wikipedia articles and important named-entities, which are re-written as Wikipedia searching (WikiSearch) and named-entity recognition (NER) (We use NER to extract entities from the article that bridge the former WikiSearch results to the latter WikiSearch queries) queries. Table 2 shows an example of a re-written CoA trace for Wiki QA.

#### Datasets

We use the HotpotQA dataset to construct our fine-tuning CoA data in the Wiki QA domain. HotpotQA contains 113K multi-hop QA examples, each labeled with two Wikipedia articles that provide supporting knowledge. Among the 90447 training QA pairs, we identify 72991 as Bridge QA pairs, where an intermediate entity must be identified to link the answer to the question, as shown in Table 2. The remaining 17456 are Comparison QA pairs, where the attributes of two entities are compared, e.g., “Are Randal Kleiser and Kyle Schickner of the same nationality?”. We prompt LLaMa-70B to re-write these training QAs into CoAs with WikiSearch and NER queries, and verify each CoA with our domain tools (described below), by checking whether all the articles returned by the WikiSearch queries match one of the titles in the gold articles. Finally, 8956 Bridge QAs and 5405 Comparison QAs are used as fine-tuning data, whose re-written CoAs pass the verification (Compared to mathematical reasoning, generating CoA data for Wiki QA requires more complex tool use that combines WikiSearch and NER models, leading to a lower re-writing success rate ($\sim 15.9\%$).). For Wiki QA, we note that besides training a LLM to produce CoA data using WikiSearch, we also fine-tune a second LLM to learn to generate the final gold answer based on a correctly reified CoA reasoning trace.

We evaluate models on the HotpotQA development set, which contains 5918 Bridge QA pairs and 1487 Comparison QA pairs. Similar to the mathematical reasoning domain, we also conduct zero-shot evaluation on other open-domain QA datasets: WebQuestions (WQ), NaturalQuestions (NQ) and TriviaQA, which contain 2032, 3610 and 17944 test questions, respectively.

#### Domain Tools

The specialized tools required for Wiki QA include a Wikipedia search engine to retrieve reference articles, and a NER toolkit to extract entities that bridge multi-step searching queries. We follow Toolformer and implement a Wikipedia search engine as a BM25 retriever that indexes the Wikipedia dump from the KILT benchmark. We use the BM25 retriever to search the top-10 articles relevant to the input query, and then re-rank the articles based on their Sentence-BERT embedding cosine similarity with the question. After re-ranking, the top-1 article is selected to be the final search result.

We use SpaCy (https://spacy.io/models/en) (en_core_web_sm) as the NER toolkit to extract named entities. To simplify NER, we aggregate the numerous SpaCy NER types into 6 general classes, as shown in Table 3. If multiple named entities are recognized, we input each recognized entity to the subsequent WikiSearch query, and select the entity whose subsequent search result has the highest Sentence-BERT embedding cosine similarity with the question.

**Table 3: Aggregation of SpaCy NER types.**

| General Class | SpaCy NER Types included in each General Class |
| :------------ | :--------------------------------------------- |
| person        | PERSON                                         |
| group         | NORP, ORG, LANGUAGE                            |
| location      | GPE, FAC, LOC                                  |
| culture       | EVENT, WORK_OF_ART, LAW, PRODUCT               |
| date          | DATE, TIME                                     |
| numeral       | CARDINAL, PERCENT, MONEY, QUANTITY, ORDINAL    |

**Table 4: Evaluation results on LLaMa-2 and LLaMa-2-Chat for mathematical reasoning. “All” denotes the averaged results on four MAWPS portions. Exact match rate to the final gold answer (i.e., accuracy) is reported. For each base model, the best and second-best results are bolded and underlined, respectively. The best results labeled with $^\ast$ are significantly better than their corresponding second-best results, with the significant test p-value $<0.05$.**

| Model        | Method           | Use Tool | GSM8K        | ASDiv        | SVAMP        | MAWPS        |            |            |            |            |
| :----------- | :--------------- | :------- | :----------- | :----------- | :----------- | :----------- | :--------- | :--------- | :--------- | :--------- |
|              |                  |          |              |              |              | AddSub       | SingleEQ   | SingleOp   | MultiArith | All        |
| LLaMa-2-7B   | CoT-FSP          | ✗        | 16.38        | 47.85        | 38.40        | 52.41        | 63.39      | 82.03      | 43.33      | 60.53      |
|              | CoT-FT           |          | 35.33        | 57.18        | 48.20        | 66.08        | 74.41      | 85.23      | 65.00      | 73.03      |
|              | Toolformer       | ✓        | 17.59        | 48.55        | 37.10        | 47.34        | 58.46      | 79.54      | 50.67      | 59.81      |
|              | CoA              |          | **37.83$^\ast$** | **57.61**    | **51.70$^\ast$** | **72.15$^\ast$** | **82.48$^\ast$** | **86.48$^\ast$** | **73.17$^\ast$** | **78.89$^\ast$** |
| LLaMa-2-Chat-7B | CoT-FSP          | ✗        | 24.03        | 54.14        | 51.30        | 71.90        | 72.44      | 85.41      | 74.00      | 76.32      |
|              | CoT-FT           |          | 35.41        | 59.00        | 46.90        | 58.23        | 72.24      | 85.41      | 73.00      | 73.37      |
|              | CoA (no Tool)    |          | 35.03        | 58.79        | 51.50        | 68.10        | 74.21      | 86.48      | 77.67      | 77.38      |
|              | Toolformer       | ✓        | 23.65        | 50.85        | 48.80        | 61.01        | 69.09      | 81.85      | 68.50      | 70.85      |
|              | Toolformer - Math |          | 36.01        | 59.18        | 47.60        | 58.99        | 72.44      | 85.94      | 75.50      | 74.43      |
|              | CoA              |          | **38.29$^\ast$** | **59.57**    | **54.20$^\ast$** | **72.41**    | **81.89$^\ast$** | **88.26$^\ast$** | **83.00$^\ast$** | **82.13$^\ast$** |
| LLaMa-2-Chat-70B | CoT-FSP          | ✗        | 56.18        | 65.94        | 70.60        | 86.08        | 89.17      | 92.88      | 84.50      | 88.23      |
|              | CoT-FT           |          | 60.50        | 70.24        | 70.40        | 81.52        | 87.60      | 92.35      | 89.17      | 88.18      |
|              | Toolformer       | ✓        | 52.54        | 69.07        | 73.60        | 86.84        | 89.76      | 91.46      | 81.50      | 87.26      |
|              | Toolformer - Math |          | 61.03        | 70.59        | 73.20        | 85.57        | 91.34      | 91.99      | 92.00      | 90.60      |
|              | CoA              |          | **62.32$^\ast$** | **71.89$^\ast$** | **73.40**    | **86.33**    | **94.49$^\ast$** | **93.06**    | **92.33**    | **91.91$^\ast$** |

### 4.3 Baselines

We apply our CoA reasoning method to both 7B and 70B LLaMa models, and test various model versions including the first version of LLaMa and the more advanced LLaMa-2 and LLaMa-2-Chat. We compare our method to several baselines, including: a) few-shot prompting using 8 randomly sampled QA exemplars from the original (i.e., not re-written) chain-of-thought data (CoT-FSP), b) fine-tuning with original chain-of-thought data (CoT-FT) (Note that in Wiki QA domain, the HotpotQA data used for prompting or fine-tuning baselines is pre-processed to contain both gold Wikipedia articles (serving as chain-of-thought explanations) and the final answer.), and c) Toolformer which fine-tunes LLMs on CCNet texts augmented with API calls. For evaluation on Wiki QA, we also compared our method with FireAct, which fine-tunes LLMs on HotpotQA ReAct trajectories distilled from GPT-4.

## 5 Results and Analysis

### 5.1 Mathematical Reasoning

Table 4 shows the evaluation results for the LLaMa-2 and LLaMa-2-Chat models (We include similar evaluation results for the original LLaMa model (7B) in Appendix B). On the GSM8K and ASDiv datasets, our CoA method outperforms the few-shot baseline CoT-FSP and the regular fine-tuning baseline CoT-FT, demonstrating that CoA fine-tuning with tool augmentation is more effective in adapting LLMs to multi-step reasoning tasks. Similarly, when evaluated on out-of-distribution datasets, SVAMP and MAWPS, CoA also consistently outperforms the baselines. Interestingly, for these out-of-distribution datasets, CoT-FT lags further behind CoA, particularly for 7B models, showing that CoA reasoning yields more distributionally robust reasoning performance.

Our CoA method also surpasses the tool-augmented baseline Toolformer, which implies that planning the abstract variables in CoA can improve the accuracy of reasoning with tools. However, as Toolformer is not originally trained with in-domain fine-tuning data (Toolformer is fine-tuned on CCNet data, which may not contain rich mathematical reasoning samples.), we also fine-tune a new version of Toolformer with the chain-of-thought data from GSM8K and ASDiv, denoted as Toolformer - Math in Table 4. We also observe that CoA performs better than Toolformer - Math, confirming that the introduction of abstract variables enables more robust tool use compared to direct integration of API calls within chain-of-thought reasoning.

#### Ablation Study

We verify that the robust generalization performance of our CoA method does not merely benefit from using additional tools, by fine-tuning another LLM to solve the equation (from the same model backbone), rather than calling the equation solver, denoted as CoA (no Tool) in Table 4. We find that CoA (no Tool) performs consistently worse than CoA across all datasets, confirming that using specialized tools enables LLM agents to conduct more precise operations, rather than directly solving the same operations. However, CoA (no Tool) still outperforms all baseline methods on zero-shot generalization to SVAMP and MAWPS datasets, implying that learning abstract reasoning chains also contributes to better robustness of CoA, perhaps due to better planning of multiple reasoning steps indexed by abstract variables.

#### Reasoning Steps

Our findings suggest that the benefits of chain-of-abstraction reasoning are most pronounced when problems require long reasoning chains to be solved. Figure 3 shows the stratified performance of three models on GSM8K QA, relative to the number of reasoning steps in the predicted and gold reasoning chains. Compared to the few-shot CoT-FSP, CoA produces reasoning chains that more often match the length of the gold reasoning chains, as reflected by the heat-map statistics (left column) being more aggregated around the diagonal (comparable to CoT-FT). At the same time, we observe that models achieve better QA accuracy when the number of reasoning steps in their generated answers are aligned with the gold references (i.e., the diagonal of heat-maps in right column). Above results show that fine-tuned models are better at learning to produce reasoning chains that match the true reasoning chain for the problem.

![Figure 3](x3.png)
**Figure 3:** GSM8K evaluation results on LLaMa-2-Chat-7B w.r.t. the number of reasoning steps in the predicted and gold reasoning chain. (Left) The number of test examples that belong to each stratum. (Right) The corresponding model accuracy (%) for those examples. Non-diagonal cells with fewer than 15 examples are ignored.

Interestingly, we find that CoA, compared to CoT-FT, achieves higher performance especially on questions that require more reasoning steps. In the right column of Figure 3, CoA’s improvement over CoT-FT is more pronounced on questions with more than $3$ steps in the gold reasoning chain (highlighted with red squares). This indicates that the model trained with CoA has more robust long chain-of-thought reasoning capability, which is learned from planning with abstractions.

#### Human Evaluation

To more comprehensively verify that CoA improves both knowledge operation (i.e., arithmetic by using tools) and reasoning accuracy, we conduct a human evaluation on different model answers to 200 randomly sampled GSM8K test questions. Specifically, given a GSM8K question and a model’s answer to the question, we ask human workers to judge whether the answer contains any arithmetic errors (e.g., wrong calculations, invalid equations) or reasoning errors unrelated to math derivations (e.g., misunderstanding of the question, improper strategy for solving the question), and report how often the model makes these two kinds of errors. In Table 5, we find that CoA effectively reduces arithmetic errors to zero, due to the use of equation solver to perform accurate calculations. More importantly, our method also makes fewer reasoning errors compared to the baselines, verifying that CoA fine-tuning guides the model to learn more accurate reasoning through the holistic planning of abstract reasoning chains. By contrast, ordinary fine-tuning (i.e., CoT-FT) produces a more limited reasoning improvement compared to the few-shot CoT-FSP, while also failing to suppress arithmetic errors.

**Table 5: Human evaluation results of arithmetic and reasoning error rates on 200 GSM8K test samples. Models developed based on LLaMa-2-Chat-7B are presented.**

| Method  | Error Rate |          |
| :------ | :--------- | :------- |
|         | Arithmetic | Reasoning |
| CoT-FSP | 17.3       | 70.3     |
| CoT-FT  | 25.2       | 67.8     |
| CoA     | 0.0        | 60.4     |

#### Inference Efficiency

Importantly, we find that the performance benefits of CoA reasoning do not come with increased computational costs. In Figure 4, we show the average time (seconds) that CoA and baseline agents (seeded with LLaMa-2-Chat-7B) needs to answer a question w.r.t. required gold reasoning steps. Compared to the CoT baselines, CoA requires less time than the few-shot baseline CoT-FSP, whose generation needs to be conditioned on additional examples. However, CoA is slightly less inference-efficient compared to CoT-FT, likely due to the decoding of additional tokens (e.g., “[” and “]”) for the abstract statements.

![Figure 4](x4.png)
**Figure 4:** Wall-clock inference time on GSM8K (seeded with LLaMa-2-Chat-7B). Average time of answering a question is measured (in seconds) w.r.t. the number of gold reasoning steps required for the question.

Compared to Toolformer, CoA has a lower and flatter inference time curve, indicating better scaling as the number of reasoning steps increases. This difference arises because CoA decouples the generation of (abstract) reasoning chains from the retrieval of knowledge (i.e., tool use), allowing full reasoning chains to be decoded before any tool is called. This procedure amortizes inference costs in two ways. First, tool calls are made after the CoA trace has been decoded, enabling parallel tool calls for the same trace (e.g., using an equation solver once rather than multiple calls to a calculator), and avoiding the time delay caused by waiting for external API responses. Consequently, the model fine-tuned with CoA is more efficient at multi-step reasoning, especially when the number of reasoning steps (i.e., tool calls) increases. Second, across multiple examples, the model can generate the CoA trace of the next example while tool calls are made for the preceding one, parallelizing CoA decoding and tools calls across examples.

#### Self-Consistency Decoding

Besides of greedy decoding, we also test more advanced inference strategy, i.e., self-consistency decoding, on our CoA reasoning method. We test all methods on the GSM8K dataset seeded with LLaMa-2-Chat-7B. Each method samples 16 reasoning chains and uses majority voting to aggregate the 16 answers derived by the reasoning chains, to get the final answer. For the hyperparameters of sampling, we set the temperature, top-k and top-p as 1.0, 40 and 0.5, respectively. Table 6 shows our evaluation results. We find that our CoA method consistently outperforms all baseline methods when shifting from greedy decoding to self-consistency decoding. This shows that our method also has better potential to be generalized to different LLM decoding schemes.

**Table 6: Evaluation results on GSM8K with self-consistency decoding (seeded with LLaMa-2-Chat-7B). Each model uses majority voting to aggregate the answers of 16 sampled reasoning chains**

| Method            | Accuracy |
| :---------------- | :------- |
| CoT-FSP           | 27.90    |
| CoT-FT            | 39.12    |
| Toolformer        | 24.56    |
| Toolformer - Math | 35.25    |
| CoA               | 40.79    |

### 5.2 Wiki QA

Table 7 shows our Wiki QA results using LLaMa-2-Chat models (We include similar evaluation results on LLaMa-2-7B in Appendix B). Similar to mathematical reasoning, we fine-tune a new version of Toolformer with in-domain chain-of-thought data from HotpotQA, denoted as Toolformer - Wiki. On HotpotQA, CoA achieves higher exact match rates with the gold reference compared to the few-shot or fine-tuning baselines. In particular, CoA outperforms all baselines on the more challenging bridge-type QAs, where two steps of reasoning over Wikipedia knowledge are consecutively entangled, i.e., cannot be performed independently in parallel as in comparison-type QAs. Compared to FireAct fine-tuning, CoA also achieves better performance on both bridge and comparison QAs, without requiring data distilled from closed source GPT-4.

As with mathematical reasoning, CoA agents also perform more efficient inference than Toolformer and FireAct agents when answering HotpotQA questions. We also find that CoA is more efficient (Time column) than both CoT-FSP and CoT-FT, as CoA does not require few-shot examples as additional inputs and does not need to generate long Wiki articles, which are instead provided by the search engine. Finally, CoA improves over the baseline methods in zero-shot generalization experiments on other Wiki QA datasets, outperforming all baselines on NaturalQuestions and TriviaQA, and matching the best baselines on WebQuestions.

**Table 7: Wiki QA evaluation results on LLaMa-2-Chat-based models. “Both” denotes the overall evaluation results on both bridge and comparison portions of HotpotQA. “Time” denotes the average seconds that each agent needs to answer a question in HotpotQA. Exact match rate to the final gold answer (i.e., accuracy) is reported. For each base model, the best and second-best results are bolded and underlined, respectively. The best results labeled with $^\ast$ are significantly better than their corresponding second-best results, with the significant test p-value $<0.05$.**

| Model        | Method           | Use Tool | HotpotQA     |          |          | Time  | WQ    | NQ    | TriviaQA |
| :----------- | :--------------- | :------- | :----------- | :------- | :------- | :---- | :---- | :---- | :------- |
|              |                  |          | Bridge       | Comparison | Both     |       |       |       |          |
| LLaMa-2-Chat-7B | CoT-FSP          | ✗        | 11.69        | 45.46    | 18.47    | 2.074 | 34.65 | 30.91 | 53.48    |
|              | CoT-FT           |          | 14.24        | 56.69    | 22.77    | 1.937 | 33.51 | 25.40 | 51.05    |
|              | Toolformer       | ✓        | 12.99        | 44.59    | 20.00    | 2.350 | 36.22 | 30.22 | 54.15    |
|              | Toolformer - Wiki |          | 15.68        | 56.42    | 23.86    | 2.301 | 36.61 | 32.96 | 55.08    |
|              | FireAct          |          | 19.18        | 54.14    | 26.20    | 2.706 | 36.02 | 35.87 | 52.96    |
|              | CoA              |          | **21.00$^\ast$** | **56.96** | **28.22$^\ast$** | 1.896 | 35.97 | **38.67$^\ast$** | **57.90$^\ast$** |
| LLaMa-2-Chat-70B | CoT-FSP          | ✗        | 21.39        | 56.62    | 28.47    | 6.668 | 34.89 | 37.42 | 63.61    |
|              | CoT-FT           |          | 23.84        | 63.95    | 31.90    | 6.401 | 34.15 | 39.75 | 62.28    |
|              | Toolformer       | ✓        | 22.24        | 56.09    | 29.04    | 6.888 | 37.16 | 40.42 | 64.31    |
|              | Toolformer - Wiki |          | 26.38        | 63.82    | 33.90    | 6.855 | 37.70 | 41.25 | 66.64    |
|              | CoA              |          | **27.61$^\ast$** | **64.09** | **34.94$^\ast$** | 6.369 | 36.37 | **43.57$^\ast$** | **69.08$^\ast$** |

## 6 Conclusion

In this work, we propose to decouple the general reasoning of LLM agents from specialized knowledge obtained via external tools. Our method, chain-of-abstraction (CoA), encourages LLMs to learn the planning of abstract multi-step reasoning, which are more robust to out-of-distribution knowledge shifts. CoA also achieves a more efficient pipeline for tool usage that significantly improves the speed of tool-augmented multi-step reasoning. The simple, yet effective, implementations of our method on two diverse tasks (i.e., math reasoning and open-domain QA) demonstrate its potential for being adapted to new reasoning scenarios.

## Limitations

We acknowledge a few limitations in our work. First, datasets used for testing our method cannot have exhaustive coverage of all real-world reasoning scenarios. We instead consider two representative reasoning domains, i.e., mathematical reasoning and general open-domain (Wikipedia) QA, and use English as a primary language in our testing. Furthermore, our method is tested on the setting of fine-tuning the full LLMs, which requires considerable computational resources, while more efficient model training schemes, e.g., LoRA, can be applied in future work.

## Acknowledgements

We thank Beatriz Borges, Gail Weiss, Syrielle Montariol, Li Mi and Zeming Chen for reading and providing comments on drafts of this paper. Antoine Bosselut gratefully acknowledges the support of the Swiss National Science Foundation (No. 215390), Innosuisse (PFFS-21-29), the EPFL Science Seed Fund, the EPFL Center for Imaging, Sony Group Corporation, and the Allen Institute for AI.

## Appendix A Implementation Details

#### Evaluation Details

For mathematical reasoning evaluation, we extract the last number appeared in each model’s answer, and check whether the number exactly match the gold reference. The accuracy is reported as the rate of such exact match across all QAs in a test set. For Wiki QA evaluation, similar to mathematical reasoning, we extract the final answer of each model and calculate its exact match rate to the gold reference. Specifically, the final answer is supposed to be the words after “Action: finish[” for FireAct baseline, and words after “The answer is ” for other models. Our 8-shot in-domain examples used for the CoT-FSP baseline are shown in Table 14 and 15, which enables the model to provide answer with our required format for evaluation, i.e., stating its final answer after “The answer is ”. Our human evaluation on GSM8K is conducted by 5 internal domain experts from our research group. For each math question, we provide the experts with the gold answer as reference, and ask them to evaluate each model answer in anonymous manner, i.e., experts do not know which model each answer comes from. Two yes-or-no questions are asked for evaluating each model answer, including: a) whether the answer has any arithmetic error, and b) whether the answer has any reasoning error, and binary choices from the experts are collected to calculate the error rates of each model’s generation. We present our detailed instructions for human evaluation in Figure 5. Our data collection protocol is approved by our organization in terms of ethics.

#### Model Training

We fine-tune our models with batch size $8$ and learning rate $2e^{-5}$ and $1e^{-5}$ for 7B and 70B model sizes, respectively, using cosine learning rate scheduler with warm-up step $10$. We use AdamW optimizer for all our fine-tuning experiments, with $\beta_{1}$, $\beta_{2}$ and $\epsilon$ set to $0.9$, $0.95$ and $1e^{-8}$, respectively. Training weight decay is set to $0.1$. For mathematical reasoning, we use a total of $400$ training steps, and get the best model checkpoints (with highest validation scores) at step $240$ and $200$ for 7B and 70B model sizes. For Wiki QA domain, we adjust the total training steps to $500$, and get the best checkpoints at step $450$ and $300$ for 7B and 70B models. Therefore, only $\sim 2$K and $\sim 3$K QAs are required in practice for fine-tuning our models in math and Wiki QA domains. The training of our 7B and 70B models is based on 8 and 64 NVIDIA A100-SXM4 (80GB) GPUs, with training time about 2 and 5 hours per model, respectively.

## Appendix B Full Experimental Results

Table 8 and 9 show the full results of our experiments on math and Wiki QA domains. Our method of CoA achieves consistent improvements over baselines across various LLaMa model versions (LLaMa, LLaMa-2 and LLaMa-2-Chat), model sizes (7B and 70B), and domain benchmarks. This shows great potential of our method being generalized to new model backbones and reasoning tasks. We also present results on GSM8K subsets according to varying numbers of gold reasoning steps in Table 10, where we confirm that CoA has more robust long chain-of-thought reasoning accuracy.

#### Fine-Tuning Data Balance

In the mathematical reasoning domain, we also validate the importance of using fine-tuning data that is balanced across different reasoning steps. Specifically, we conduct an ablation study on CoT-FT and CoA seeded with LLaMa-2-Chat-7B model, by removing the single-step QA samples of ASDiv from the fine-tuning data (no ASDiv). We find that CoT-FT (no ASDiv) and CoA (no ASDiv) turn out to be biased towards multi-step reasoning, where they achieve better performance on GSM8K and MultiArith that contain mainly multi-step QAs, but suffer from severe performance degradation on other datasets that contain many single-step math problems. This demonstrates that maintaining a good balance of single-step and multi-step reasoning data is important for adapting LLMs to be robust reasoners.

#### More Prompting Baselines

We also compare our CoA reasoning method to more prompting-based methods PAL and DECLARATIVE, which use few-shot coding demonstrations to prompt math solutions as Python or declarative programs. Table 11 shows our comparison results on the GSM8K dataset, where all methods are seeded with LLaMa-2-Chat-7B. Without seeding with dedicated coding models (e.g., code-davinci-002), PAL and DECLARATIVE get far lower accuracy on GSM8K, which significantly under-perform our CoA method, and even ordinary CoT-FSP.

In contrast, our CoA method relies less on artificial demonstrations and distributional closeness of the seed LLM to target tasks, as CoA fine-tunes the LLM agent on pre-defined abstract reasoning chains, acquired from simple rewriting of natural language reasoning traces. Consequently, CoA is flexible in various generation formats, e.g., code and plain text, and generalizes well from mathematical reasoning to open-domain QA, which is a very different type of reasoning task. This indicates our method’s generalizability to novel reasoning schemes required by a new domain.

**Table 10: Stratified LLaMa-2-Chat-7B evaluation results on GSM8K with different gold reasoning steps. The last row reports absolute accuracy improvement of our CoA method compared to CoT-FT baseline.**

| Method  | Gold Reasoning Step |     |     |     |    |
| :------ | :------------------ | :-- | :-- | :-- | :-- |
|         | $\leq 2$            | $3$ | $4$ | $5$ | $>5$ |
| CoT-FSP | 42.9                | 26.3 | 18.0 | 10.9 | 3.6 |
| CoT-FT  | 55.5                | 42.6 | 25.8 | 19.0 | 10.8 |
| CoA     | 55.8                | 44.4 | 32.5 | 25.3 | 15.1 |
|         | +0.3                | +1.8 | +6.7 | +6.3 | +4.3 |

**Table 11: Comparison of CoA to prompting-based methods on GSM8K, seeded with LLaMa-2-Chat-7B.**

| Method      | Accuracy |
| :---------- | :------- |
| CoT-FSP     | 24.03    |
| PAL         | 20.55    |
| DECLARATIVE | 9.86     |
| CoA         | 38.29    |

**Table 12: Prompting examples for fine-tuning data construction in mathematical reasoning domain. Given a question (Q) and a gold answer (A), LLaMa-70B is prompted to generate the re-writing of answer as abstract reasoning chain (C). Based on that, our method trains a LLM to generate the abstract chain based on the question, and the final answer is derived by reify the chain of reasoning with the domain tool (i.e., equation solver).**

| Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees will the grove |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workers plant today?                                                                                                                                        |
| A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21-15=6. The answer is 6.                   |
| C: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been [21 - 15 = y1]. The answer is y1.           |
| Q: The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers? |
| A: The clay pot costs $20 + $9 = $29. The bag of soil costs $9 - $2 = $7. The cost to plant the flowers is $9 + $29 + $7 = $45. The answer is 45.             |
| C: The clay pot costs [20 + 9 = y1]. The bag of soil costs [9 - 2 = y2]. The cost to plant the flowers is [9 + y1 + y2 = y3]. The answer is y3.           |
| Q: From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam |
| is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy |
| the video game console?                                                                                                                                     |
| A: Sam makes $460 / 23 hrs = $20/hr. From September to February, Sam made 8hrs x $20/hr = $160. From March to February, Sam made a total of $460 + $160 |
| = $620. After fixing his car, he was left with $620 - $340 = $280. Sam needs another $600 - $280 = $320. Sam needs to work another $320 / $20/hr = 16 hours. |
| The answer is 16.                                                                                                                                           |
| C: Sam makes [460 / 23 = y1] dollars per hour. From September to February, Sam made [8 * y1 = y2] dollars. From March to February, Sam made a |
| total of [460 + y2 = y3] dollars. After fixing his car, he was left with [y3 - 340 = y4]. Sam needs another [600 - y4 = y5] dollars. Sam needs to work |
| another [y5 / y1 = y6] hours. The answer is y6.                                                                                                             |
| Q: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in |
| the server room?                                                                                                                                            |
| A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29. |
| C: There were originally 9 computers. For each of 4 days, 5 more computers were added. So [5 * 4 = y1] computers were added. [9 + y1 = y2]. |
| The answer is y2.                                                                                                                                           |
| Q: Of the 90 people on William’s bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What’s the number of Dutch |
| Americans who sat at the windows?                                                                                                                           |
| A: On the bus, the number of Dutch people was 3/5 of the total number, a total of 3/5 x 90 = 54 people. Out of the 54 people who were Dutch, 1/2 were Dutch |
| Americans, a total of 1/2 x 54 = 27 people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number is 1/3 x 27 = 9. |
| The answer is 9.                                                                                                                                            |
| C: On the bus, the number of Dutch people was 3/5 of the total number, a total of [3/5 * 90 = y1] people. Out of the Dutch people, 1/2 were Dutch |
| Americans, a total of [1/2 * y1 = y2] people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number |
| is [1/3 * y2 = y3]. The answer is y3.                                                                                                                       |

## Appendix C Fine-Tuning Data Re-writing Details

Table 12 and 13 show the prompting examples for fine-tuning data construction of our method. We prompt LLaMa-70B to re-write existing math and Wiki QAs as abstract reasoning chains, which gets rid of data distillation from close-sourced LLMs, yet obtains data resources that enable more effective learning of multi-step reasoning.

**Table 13: Prompting examples for fine-tuning data construction in Wiki QA domain. Given a question (Q), a gold answer (A) and its supporting Wikipedia articles (W), LLaMa-70B is prompted to generate an abstract reasoning chain (C) with Wikipedia searching and NER queries. Based on that, our method first trains a LLM to generate the abstract chain of queries based on the question, and then execute the queries by domain tools (i.e., Wikipedia search engine and NER toolkit). Finally, a second LLM is trained to generate the final answer based on the Wikipedia searching results (excluding intermediate NER results) in the reified chain of reasoning.**

| Q: Fritz von Brodowski was killed during what global war that lasted from 1939 to 1945?                                                                                                                                                                      |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A: The answer is World War II.                                                                                                                                                                                                                             |
| W: Fritz von Brodowski > Friedrich Wilhelm Konrad von Brodowski was controversially killed while in French custody during World War II.                                                                                                                      |
| C: Find the [war in which Fritz von Brodowski was killed -Wiki-> y1].                                                                                                                                                                                     |
| Q: Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?                                                                                                                                                                       |
| A: The answer is Jonathan Stark.                                                                                                                                                                                                                           |
| W: Henri Leconte > He won the French Open men’s doubles title in 1984. Jonathan Stark (tennis) > During his career he won two Grand Slam doubles titles.                                                                                                    |
| C: First identify the [number of Grand Slam titles Henri Leconte won -Wiki-> y1]. Then find out the [number of Grand Slam titles Jonathan Stark won -Wiki-> y2].                                                                                           |
| Q: The director of the romantic comedy “Big Stone Gap” is based in what New York city?                                                                                                                                                                    |
| A: The answer is Greenwich Village.                                                                                                                                                                                                                        |
| W: Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic comedy film directed by Adriana Trigiani. Adriana Trigiani > Adriana Trigiani is an                                                                                                      |
| Italian American film director based in Greenwich Village.                                                                                                                                                                                                 |
| C: First search the [director of romantic comedy “Big Stone Gap” -Wiki-> y1]. The name of this film’s director is [y1 -NER(person)-> y2]. Then determine [y2 in |
| what New York city -Wiki-> y3].                                                                                                                                                                                                                            |
| Q: Are Randal Kleiser and Kyle Schickner of the same nationality?                                                                                                                                                                                         |
| A: The answer is yes.                                                                                                                                                                                                                                      |
| W: Randal Kleiser > John Randal Kleiser (born July 20, 1946) is an American film director and producer. Kyle Schickner > Kyle Schickner is an American film |
| producer, writer, director, actor.                                                                                                                                                                                                                         |
| C: First find out the [nationality of Randal Kleiser -Wiki-> y1]. Then figure out the [nationality of Kyle Schickner -Wiki-> y2].                                                                                                                           |
| Q: Extras was created, written, and directed by Ricky Dene Gervais, an English comedian, actor, writer, producer, director, singer, and musician, born on which date? |
| A: The answer is 25 June 1961.                                                                                                                                                                                                                             |
| W: Ricky Gervais > Ricky Dene Gervais (born 25 June 1961) is an English comedian, actor, writer, producer, director, singer, and musician.                        |
| C: Search [when Ricky Dene Gervais was born -Wiki-> y1].                                                                                                                                                                                                  |
| Q: Sameera Perera is a cricketer from what island country located southeast of the Republic of India and northeast of the Maldives?                                                                                                                        |
| A: The answer is Sri Lanka.                                                                                                                                                                                                                                |
| W: Sameera Perera > Sameera Perera (born 20 August 1988) is a Sri Lankan cricketer.                                                                                                                                                                        |
| C: Identify the [country that cricketer Sameera Perera is from -Wiki-> y1].                                                                                                                                                                               |
| Q: What screenwriter with credits for “Evolution” co-wrote a film starring Nicolas Cage and Téa Leoni?                                                                                                                                                    |
| A: The answer is David Weissman.                                                                                                                                                                                                                           |
| W: The Family Man > The Family Man is a 2000 American romantic comedy-drama film starring Nicolas Cage and Téa Leoni. David Weissman > His film credits |
| include “The Family Man” (2000), “Evolution” (2001), and “When in Rome” (2010).                                                                                                                                                                            |
| C: First figure out the [film of Nicolas Cage and Téa Leoni -Wiki-> y1]. The name of this film is [y1 -NER(culture)-> y2]. Then find out [who wrote y2 with |
| credits for “Evolution” -Wiki-> y3].                                                                                                                                                                                                                       |
| Q: Ralph Hefferline was a psychology professor at a university that is located in what city?                                                                                                                                                              |
| A: The answer is New York City.                                                                                                                                                                                                                            |
| W: Ralph Hefferline > Ralph Franklin Hefferline was a psychology professor at Columbia University. Columbia University > Columbia University is a private Ivy |
| League research university in Upper Manhattan, New York City.                                                                                                                                                                                              |
| C: First identify the [university of psychology professor Ralph Hefferline -Wiki-> y1]. The university of this professor is [y1 -NER(group)-> y2]. Then figure |
| out [y2 is in what city -Wiki-> y3].                                                                                                                                                                                                                       |

**Table 14: Few-shot examples used for CoT-FSP baseline model in mathematical reasoning domain.**

| Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done, there will be 21 trees. How many trees will the grove |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workers plant today?                                                                                                                                        |
| A: There are 15 trees originally. Then there were 21 trees after some more were planted. So there must have been 21-15=6. The answer is 6.                   |
| Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?                                                     |
| A: There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5.                                                                             |
| Q: The flowers cost $9, the clay pot costs $20 more than the flower, and the bag of soil costs $2 less than the flower. How much does it cost to plant the flowers? |
| A: The clay pot costs $20 + $9 = $29. The bag of soil costs $9 - $2 = $7. The cost to plant the flowers is $9 + $29 + $7 = $45. The answer is 45.             |
| Q: Maddie wants to see how much her mom spends on coffee each week. She makes herself 2 cups of coffee per day. Each cup has 1.5 ounces of coffee beans. |
| A bag of coffee costs $8 and contains 10.5 ounces of beans. How much does she spend on her coffee per week?                                                 |
| A: She uses 3 ounces of beans per day because 2 x 1.5 = 3. She uses 21 ounces of beans per week because 7 x 3 = 21. She buys 2 bags of beans per week |
| because 21 / 10.5 = 2. She spends $16 on the beans per week because 2 x 8 = 16. The answer is 16.                                                           |
| Q: There were nine computers in the server room. Five more computers were installed each day, from Monday to Thursday. How many computers are now in |
| the server room?                                                                                                                                            |
| A: There were originally 9 computers. For each of 4 days, 5 more computers were added. So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29. |
| Q: From March to August, Sam made $460 doing 23 hours of yard work. However, from September to February, Sam was only able to work for 8 hours. If Sam |
| is saving up to buy a video game console that costs $600 and has already spent $340 to fix his car, how many more hours does he need to work before he can buy |
| the video game console?                                                                                                                                     |
| A: Sam makes $460 / 23 hrs = $20/hr. From September to February, Sam made 8hrs x $20/hr = $160. From March to February, Sam made a total of $460 + $160 |
| = $620. After fixing his car, he was left with $620 - $340 = $280. Sam needs another $600 - $280 = $320. Sam needs to work another $320 / $20/hr = 16 hours. |
| The answer is 16.                                                                                                                                           |
| Q: Of the 90 people on William’s bus, 3/5 were Dutch. Of the 1/2 of the Dutch who were also American, 1/3 got window seats. What’s the number of Dutch |
| Americans who sat at the windows?                                                                                                                           |
| A: On the bus, the number of Dutch people was 3/5 of the total number, a total of 3/5 x 90 = 54 people. Out of the 54 people who were Dutch, 1/2 were Dutch |
| Americans, a total of 1/2 x 54 = 27 people. If 1/3 of the passengers on the bus identifying as Dutch Americans sat at the windows, their number is 1/3 x 27 = 9. |
| The answer is 9.                                                                                                                                            |
| Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?                                                 |
| A: Originally, Leah had 32 chocolates. Her sister had 42. So in total they had 32 + 42 = 74. After eating 35, they had 74-35=39. The answer is 39.         |

**Table 15: Few-shot examples used for CoT-FSP baseline model in Wiki QA domain.**

| Q: Fritz von Brodowski was killed during what global war that lasted from 1939 to 1945?                                                                                                              |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A: Fritz von Brodowski > Friedrich Wilhelm Konrad von Brodowski was controversially killed while in French custody during World War II. The answer is World War II.                                     |
| Q: Which tennis player won more Grand Slam titles, Henri Leconte or Jonathan Stark?                                                                                                                  |
| A: Henri Leconte > He won the French Open men’s doubles title in 1984. Jonathan Stark (tennis) > During his career he won two Grand Slam doubles titles.                                              |
| The answer is Jonathan Stark.                                                                                                                                                                        |
| Q: The director of the romantic comedy “Big Stone Gap” is based in what New York city?                                                                                                               |
| A: Big Stone Gap (film) > Big Stone Gap is a 2014 American romantic comedy film directed by Adriana Trigiani. Adriana Trigiani > Adriana Trigiani is an                                               |
| Italian American film director based in Greenwich Village. The answer is Greenwich Village.                                                                                                          |
| Q: Are Randal Kleiser and Kyle Schickner of the same nationality?                                                                                                                                    |
| A: Randal Kleiser > John Randal Kleiser (born July 20, 1946) is an American film director and producer. Kyle Schickner > Kyle Schickner is an American film                                           |
| producer, writer, director, actor. The answer is yes.                                                                                                                                                |
| Q: Extras was created, written, and directed by Ricky Dene Gervais, an English comedian, actor, writer, producer, director, singer, and musician, born on which date?                                     |
| A: Ricky Gervais > Ricky Dene Gervais (born 25 June 1961) is an English comedian, actor, writer, producer, director, singer, and musician. The answer is 25 June 1961.                               |
| Q: Sameera Perera is a cricketer from what island country located southeast of the Republic of India and northeast of the Maldives?                                                                    |
| A: Sameera Perera > Sameera Perera (born 20 August 1988) is a Sri Lankan cricketer. The answer is Sri Lanka.                                                                                         |
| Q: What screenwriter with credits for “Evolution” co-wrote a film starring Nicolas Cage and Téa Leoni?                                                                                                 |
| A: The Family Man > The Family Man is a 2000 American romantic comedy-drama film starring Nicolas Cage and Téa Leoni. David Weissman > His film credits                                               |
| include “The Family Man” (2000), “Evolution” (2001), and “When in Rome” (2010). The answer is David Weissman.                                                                                        |
| Q: Ralph Hefferline was a psychology professor at a university that is located in what city?                                                                                                         |
| A: Ralph Hefferline > Ralph Franklin Hefferline was a psychology professor at Columbia University. Columbia University > Columbia University is a private Ivy                                         |
| League research university in Upper Manhattan, New York City. The answer is New York City.                                                                                                           |

![Figure 5](x5.png)
**Figure 5:** Guideline for human evaluation on GSM8K mathematical reasoning.

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

```python
from openai import OpenAI
import json

client = OpenAI()

# 1. Define a list of callable tools for the model
tools = \
    [
        {
            "type": "function",
            "function": {
                "name": "get_horoscope",
                "description": "Get today's horoscope for an astrological sign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sign": {
                            "type": "string",
                            "description": "An astrological sign like Taurus or Aquarius",
                        },
                    },
                    "required": ["sign"],
                    "additionalProperties": False,
                },
                "strict": True,
            },
        },
    ]

def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."

messages = \
    [{"role": "user", "content": "What is my horoscope? I am an Aquarius."}]

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

```javascript
import OpenAI from "openai";

const openai = new OpenAI();

// 1. Define a list of callable tools for the model
const tools = \
  [
    {
      type: "function",
      function: {
        name: "get_horoscope",
        description: "Get today's horoscope for an astrological sign.",
        parameters: {
          type: "object",
          properties: {
            sign: {
              type: "string",
              description: "An astrological sign like Taurus or Aquarius",
            },
          },
          required: ["sign"],
          additionalProperties: false,
        },
        strict: true,
      },
    },
  ];

function getHoroscope(sign) {
  return `${sign}: Next Tuesday you will befriend a baby otter.`;
}

const messages = \
  [
    { role: "user", content: "What is my horoscope? I am an Aquarius." },
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

```python
from openai import OpenAI
import json

client = OpenAI()

# 1. Define a list of callable tools for the model
tools = \
    [
        {
            "type": "function",
            "name": "get_horoscope",
            "description": "Get today's horoscope for an astrological sign.",
            "parameters": {
                "type": "object",
                "properties": {
                    "sign": {
                        "type": "string",
                        "description": "An astrological sign like Taurus or Aquarius",
                    },
                },
                "required": ["sign"],
            },
        },
    ]

def get_horoscope(sign):
    return f"{sign}: Next Tuesday you will befriend a baby otter."

# Create a running input list we will add to over time
input_list = \
    [{"role": "user", "content": "What is my horoscope? I am an Aquarius."}]

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

```javascript
import OpenAI from "openai";

const openai = new OpenAI();

// 1. Define a list of callable tools for the model
const tools = \
  [
    {
      type: "function",
      name: "get_horoscope",
      description: "Get today's horoscope for an astrological sign.",
      parameters: {
        type: "object",
        properties: {
          sign: {
            type: "string",
            description: "An astrological sign like Taurus or Aquarius",
          },
        },
        required: ["sign"],
        additionalProperties: false,
      },
      strict: true,
    },
  ];

function getHoroscope(sign) {
  return `${sign}: Next Tuesday you will befriend a baby otter.`;
}

// Create a running input list we will add to over time
let input = \
  [
    { role: "user", content: "What is my horoscope? I am an Aquarius." },
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

```json
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

```json
{
  "type": "namespace",
  "name": "crm",
  "description": "CRM tools for customer lookup and order management.",
  "tools": \
    [
      {
        "type": "function",
        "name": "get_customer_profile",
        "description": "Fetch a customer profile by customer ID.",
        "parameters": {
          "type": "object",
          "properties": {
            "customer_id": { "type": "string" }
          },
          "required": ["customer_id"],
          "additionalProperties": false
        }
      },
      {
        "type": "function",
        "name": "list_open_orders",
        "description": "List open orders for a customer ID.",
        "defer_loading": true,
        "parameters": {
          "type": "object",
          "properties": {
            "customer_id": { "type": "string" }
          },
          "required": ["customer_id"],
          "additionalProperties": false
        }
      }
    ]
}
```

## Tool search

If you need to give the model access to a large ecosystem of tools, you can defer loading some or all of those tools with `tool_search`. The `tool_search` tool lets the model search for relevant tools, add them to the model context, and then use them. Only `gpt-5.4` and later models support it. Read the [tool search guide](https://developers.openai.com/api/docs/guides/tools-tool-search) to learn more.

(Optional) Function calling wth pydantic and zod

While we encourage you to define your function schemas directly, our SDKs have helpers to convert `pydantic` and `zod` objects into schemas. Not all `pydantic` and `zod` features are supported.

Define objects to represent function schema

```python
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

```javascript
import OpenAI from "openai";
import { z } from "zod";
import { zodFunction } from "openai/helpers/zod";

const openai = new OpenAI();

const GetWeatherParameters = z.object({
  location: z.string().describe("City and country e.g. Bogotá, Colombia"),
});

const tools = \
  [
    zodFunction({ name: "getWeather", parameters: GetWeatherParameters }),
  ];

const messages = \
  [
    { role: "user", content: "What's the weather like in Paris today?" },
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

```json
[
    {
        "id": "call_12345xyz",
        "type": "function",
        "function": {
            "name": "get_weather",
            "arguments": "{\"location\":\"Paris, France\"}"
        }
    },
    {
        "id": "call_67890abc",
        "type": "function",
        "function": {
            "name": "get_weather",
            "arguments": "{\"location\":\"Bogotá, Colombia\"}"
        }
    },
    {
        "id": "call_99999def",
        "type": "function",
        "function": {
            "name": "send_email",
            "arguments": "{\"to\":\"bob@email.com\",\"body\":\"Hi bob\"}"
        }
    }
]
```

Execute function calls and append results

```python
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

```javascript
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

```json
[
    {
        "id": "fc_12345xyz",
        "call_id": "call_12345xyz",
        "type": "function_call",
        "name": "get_weather",
        "arguments": "{\"location\":\"Paris, France\"}"
    },
    {
        "id": "fc_67890abc",
        "call_id": "call_67890abc",
        "type": "function_call",
        "name": "get_weather",
        "arguments": "{\"location\":\"Bogotá, Colombia\"}"
    },
    {
        "id": "fc_99999def",
        "call_id": "call_99999def",
        "type": "function_call",
        "name": "send_email",
        "arguments": "{\"to\":\"bob@email.com\",\"body\":\"Hi bob\"}"
    }
]
```

If you are using [tool search](https://developers.openai.com/api/docs/guides/tools-tool-search), you may also see `tool_search_call` and `tool_search_output` items before a `function_call`. Once the function is loaded, handle the function call in the same way shown here.

Execute function calls and append results

```python
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

```javascript
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

```python
def call_function(name, args):
    if name == "get_weather":
        return get_weather(**args)
    if name == "send_email":
        return send_email(**args)
```

```javascript
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

```python
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=messages,
    tools=tools,
)
```

```javascript
const completion = await openai.chat.completions.create({
    model: "gpt-4.1",
    messages,
    tools,
    store: true,
});
```

After appending the results to your `input`, you can send them back to the model to get a final response.

Send results back to model

```python
response = client.responses.create(
    model="gpt-4.1",
    input=input_messages,
    tools=tools,
)
```

```javascript
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

```json
"tool_choice": {
    "type": "allowed_tools",
    "mode": "auto",
    "tools": \
        [
            { "type": "function", "name": "get_weather" },
            { "type": "function", "name": "search_docs" }
        ]
  }
}
```

You can also set `tool_choice` to `"none"` to imitate the behavior of passing no functions.

When you use tool search, `tool_choice` still applies to the tools that are currently callable in the turn. This is most useful after you load a subset of tools and want to constrain the model to that subset.

### Parallel function calling

Parallel function calling is not possible when using [built-in
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

Strict mode enabled

```json
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

```json
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

Strict mode enabled

```json
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

```json
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

```python
from openai import OpenAI

client = OpenAI()

tools = [\
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia"
                    }
                },
                "required": ["location"],
                "additionalProperties": False
            },
            "strict": True
        }
    }
]

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

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [\
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current temperature for a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and country e.g. Bogotá, Colombia"
                    }
                },
                "required": ["location"],
                "additionalProperties": false
            },
            "strict": true
        }
    }
];

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

```json
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

```python
final_tool_calls = {}

for chunk in stream:
    for tool_call in chunk.choices[0].delta.tool_calls or []:
        index = tool_call.index

        if index not in final_tool_calls:
            final_tool_calls[index] = tool_call

        final_tool_calls[index].function.arguments += tool_call.function.arguments
```

```javascript
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

```json
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

```python
from openai import OpenAI

client = OpenAI()

tools = [\
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get current temperature for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "City and country e.g. Bogotá, Colombia"
                }
            },
            "required": \
                [
                    "location"
                ],
            "additionalProperties": False
        }
    }
]

stream = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What's the weather like in Paris today?"}],
    tools=tools,
    stream=True
)

for event in stream:
    print(event)
```

```javascript
import { OpenAI } from "openai";

const openai = new OpenAI();

const tools = [\
    {
        type: "function",
        name: "get_weather",
        description: "Get current temperature for provided coordinates in celsius.",
        parameters: {
            type: "object",
            properties: {
                latitude: { type: "number" },
                longitude: { type: "number" }
            },
            required: ["latitude", "longitude"],
            additionalProperties: false
        },
        strict: true
    }
];

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

```json
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

```python
final_tool_calls = {}

for event in stream:
    if event.type === 'response.output_item.added':
        final_tool_calls[event.output_index] = event.item;
    elif event.type === 'response.function_call_arguments.delta':
        index = event.output_index

        if final_tool_calls[index]:
            final_tool_calls[index].arguments += event.delta
```

```javascript
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

```json
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

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5",
    input="Use the code_exec tool to print hello world to the console.",
    tools=\
        [
            {
                "type": "custom",
                "name": "code_exec",
                "description": "Executes arbitrary Python code.",
            }
        ]
)
print(response.output)
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.create({
  model: "gpt-5",
  input: "Use the code_exec tool to print hello world to the console.",
  tools: \
    [
      {
        type: "custom",
        name: "code_exec",
        description: "Executes arbitrary Python code.",
      },
    ],
});

console.log(response.output);
```

Just as before, the `output` array will contain a tool call generated by the model. Except this time, the tool call input is given as plain text.

```json
[
  {
    "id": "rs_6890e972fa7c819ca8bc561526b989170694874912ae0ea6",
    "type": "reasoning",
    "content": [],
    "summary": []
  },
  {
    "id": "ctc_6890e975e86c819c9338825b3e1994810694874912ae0ea6",
    "type": "custom_tool_call",
    "status": "completed",
    "call_id": "call_aGiFQkRWSWAIsMQ19fKqxUgb",
    "input": "print(\"hello world\")",
    "name": "code_exec"
  }
]
```

### Context-free grammars

A [context-free grammar](https://en.wikipedia.org/wiki/Context-free_grammar) (CFG) is a set of rules that define how to produce valid text in a given format. For custom tools, you can provide a CFG that will constrain the model’s text input for a custom tool.

You can provide a custom CFG using the `grammar` parameter when configuring a custom tool. Currently, we support two CFG syntaxes when defining grammars: `lark` and `regex`.

#### Lark CFG

Lark context free grammar example

```python
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
    tools=\
        [
            {
                "type": "custom",
                "name": "math_exp",
                "description": "Creates valid mathematical expressions",
                "format": {
                    "type": "grammar",
                    "syntax": "lark",
                    "definition": grammar,
                },
            }
        ]
)
print(response.output)
```

```javascript
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
  tools: \
    [
      {
        type: "custom",
        name: "math_exp",
        description: "Creates valid mathematical expressions",
        format: {
          type: "grammar",
          syntax: "lark",
          definition: grammar,
        },
      },
    ],
});

console.log(response.output);
```

The output from the tool should then conform to the Lark CFG that you defined:

```json
[
  {
    "id": "rs_6890ed2b6374819dbbff5353e6664ef103f4db9848be4829",
    "type": "reasoning",
    "content": [],
    "summary": []
  },
  {
    "id": "ctc_6890ed2f32e8819daa62bef772b8c15503f4db9848be4829",
    "type": "custom_tool_call",
    "status": "completed",
    "call_id": "call_pmlLjmvG33KJdyVdC4MVdk5N",
    "input": "4 + 4",
    "name": "math_exp"
  }
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

```python
from openai import OpenAI

client = OpenAI()

grammar = r"^(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<day>\d{1,2})(?:st|nd|rd|th)?\s+(?P<year>\d{4})\s+at\s+(?P<hour>0?[1-9]|1[0-2])(?P<ampm>AM|PM)$"

response = client.responses.create(
    model="gpt-5",
    input="Use the timestamp tool to save a timestamp for August 7th 2025 at 10AM.",
    tools=\
        [
            {
                "type": "custom",
                "name": "timestamp",
                "description": "Saves a timestamp in date + time in 24-hr format.",
                "format": {
                    "type": "grammar",
                    "syntax": "regex",
                    "definition": grammar,
                },
            }
        ]
)
print(response.output)
```

```javascript
import OpenAI from "openai";
const client = new OpenAI();

const grammar = "^(?P<month>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<day>\d{1,2})(?:st|nd|rd|th)?\s+(?P<year>\d{4})\s+at\s+(?P<hour>0?[1-9]|1[0-2])(?P<ampm>AM|PM)$";

const response = await client.responses.create({
  model: "gpt-5",
  input: "Use the timestamp tool to save a timestamp for August 7th 2025 at 10AM.",
  tools: \
    [
      {
        type: "custom",
        name: "timestamp",
        description: "Saves a timestamp in date + time in 24-hr format.",
        format: {
          type: "grammar",
          syntax: "regex",
          definition: grammar,
        },
      },
    ],
});

console.log(response.output);
```

The output from the tool should then conform to the Regex CFG that you defined:

```json
[
  {
    "id": "rs_6894f7a3dd4c81a1823a723a00bfa8710d7962f622d1c260",
    "type": "reasoning",
    "content": [],
    "summary": []
  },
  {
    "id": "ctc_6894f7ad7fb881a1bffa1f377393b1a40d7962f622d1c260",
    "type": "custom_tool_call",
    "status": "completed",
    "call_id": "call_8m4XCnYvEmFlzHgDHbaOCFlK",
    "input": "August 7th 2025 at 10AM",
    "name": "timestamp"
  }
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

Compositional function calling is a native [Live\
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
-   Only a [subset of the OpenAPI\
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

[00:00] What is tool calling? Tool calling is a powerful technique where you make the LLM context aware of real-time data, such as databases or APIs. (A man in glasses and a black t-shirt stands in front of a black background. "IBM Technology" is in the top left corner.)

Typically, you use tool calling via a chat interface. So, you would have your client application in one hand, (The man starts drawing on a transparent board in front of him. He draws a vertical line on the left and writes "chat" at the top center. He then writes "APP" above the left vertical line.) and then the LLM on the other side. (He draws another vertical line on the right and writes "LLM" above it.)

[00:30] From your client application, you would send a set of messages together with a tool definition to the LLM. So, you would have your messages here, (He draws a horizontal arrow from APP to LLM and writes "messages" along it in green marker.) together with your list of tools. (He adds "+ tools" to the green text.) The LLM will look at both your message and the list of tools, and it's going to recommend a tool you should call. (He draws a return arrow from LLM to APP and writes "tool to call" along it.)

From your client application, you should call this tool and then supply the answer back to the LLM. (He draws another arrow from APP to LLM and writes "tool response" along it.) So this tool response will be interpreted by the LLM, and this will either tell you the next tool to call or it will give you the final answer. (He draws a final return arrow from LLM to APP.)

[01:00] In your application, you're responsible for creating the tool definition. (He draws a box around "APP" on the left and writes "tool definition" near the top of the box.) So this tool definition includes a couple of things, such as the name of every tool. (He adds "- name" below "tool definition".) It also includes a description for the tool. (He adds "- description".) So this is where you can give additional information about how to use the tool or when to use it. And it also includes the input parameters needed to make a tool call. (He adds "- input".) And the tools can be anything. (He draws a larger box labeled "tools" below the "APP" box.) So the tools could be APIs or databases. (He draws circles below the "tools" box, labeling one "API" and another "DB".)

[01:30] But it could also be code that you interpret via code interpreter. (He draws another circle labeled "Code".)

*Summary: Tool calling allows an LLM to interact with real-time data or perform actions by recommending tools (APIs, databases, code) that the client application then executes, returning the result to the LLM for final processing.*

So let's look at an example. Assume you want to find the weather in Miami. You might ask the LLM about the temperature in Miami. (He points to the "messages + tools" arrow and writes "temp in Miami?" above it.) You also provide a list of tools. And one of these tools is the weather API. (He points to the "tools" on the arrow and writes "Weather API" above it.)

[02:00] The LLM will look at both your question, which is what is the temperature in Miami, it will also look at the weather API, and then based on the tool definition for the weather API, it's going to tell you how to call the weather tool. So in here, it's going to create a tool that you can use right here on this side, where you call the API to collect the weather information. (He points to the "tool to call" arrow, then to the "API" circle under "tools".) You would then supply the weather information back to the LLM. (He points to the "tool response" arrow.) So let's say it would be 71 degrees. (He writes "71°" next to "tool response".)

[02:30] The LLM will look at the tool response and then give the final answer, which might be something in the trend of the weather in Miami is pretty nice, it's 71 degrees. This has some downsides. So when you do traditional tool calling where you have an LLM and a client application, you could see the LLM hallucinate. (He draws a new vertical line on the right, labeled "LLM", and writes "- hallucinate".) Sometimes the LLM can also make up incorrect tool calls. (He adds "- incorrect".)

[03:00] That's why I also want to look at embedded tool calling. (He writes "embedded" at the top of the new section.) We just looked at traditional tool calling, but traditional tool calling has its flaws. As I mentioned, the LLM could hallucinate or create incorrect tool calls. That's why I also want to take embedded tool calling into account. With embedded tool calling, you use a library or framework to interact with the LLM and your tool definitions. The library would be somewhere between your application and the large language model. (He draws a new box between "APP" and "LLM" sections, labeling it "library" at the top.)

[03:30] In the library, you would do the tool definition, but you would also execute the tool calls. So let's draw a line between these sections here. (He draws a horizontal line in the "library" box and writes "tool def" and "tool exec" in two separate rows.) So the library will contain your tool definition. It would also contain the tool execution. So when you send a message from your application to the large language model, it will go through the library. (He draws an arrow from "APP" to the "library" box.) So your message could still be what is the temperature in Miami. (He writes "temp in Miami?" along the arrow.)

[04:00] The library will then append the tool definition and send your message together with the tools to the LLM. (He draws an arrow from the "library" to "LLM" and writes "message + tool" along it.) So this will be your message plus your list of tools. Instead of sending the tool to call to the application or the user, it will be sent to the library, which will then do the tool execution. (He draws an arrow from "LLM" back to "library".) This way, the library will provide you with the final answer. (He draws an arrow from the "library" back to "APP".)

[04:30] Which could be it's 71 degrees in Miami. (He writes "71°" along the arrow.) When you use embedded tool calling, the LLM will no longer hallucinate as the library to help you with the tool calling or the embedded tool calling is going to take care of the tool execution and will retry the tool calls in case it's needed.

*Summary: Embedded tool calling introduces a library between the application and the LLM, handling tool definitions and execution to prevent hallucinations and manage tool calls, providing a more robust interaction.*

So in this video, we looked at both traditional tool calling and also embedded tool calling, where especially embedded tool calling will help you to prevent hallucination or help you with the execution of tools, which could be APIs, databases, or code. (The man looks directly at the camera, then the screen cuts to a blue background with the IBM logo.)

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

## 1\. Working Principles of Both Patterns

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

## 2\. Implementation Comparison

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

## 3\. Performance and Cost Analysis

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

## 4\. Case Study: Data Analysis Task

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

## 5\. Selection Guide and Best Practices

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