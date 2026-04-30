# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://ai.google.dev/gemini-api/docs/langgraph-example

Query: How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python?

Answer: The official Google AI for Developers guide provides a complete implementation of a minimal ReAct agent using Gemini API and LangGraph in Python. Key steps include: Install dependencies (pip install langgraph langchain-google-genai geopy requests). Set GEMINI_API_KEY environment variable. Define AgentState with messages and step counter using TypedDict and add_messages reducer. Create a weather tool using @tool decorator with Pydantic args_schema. Initialize ChatGoogleGenerativeAI model (e.g., gemini-1.5-flash) and bind_tools to it. Define nodes: call_model invokes the bound model on state messages; call_tool executes tool calls from the last message using ToolMessage. Define should_continue conditional edge: if last message has tool_calls, go to 'tools', else 'end'. Build StateGraph: add nodes 'llm' and 'tools', set entrypoint 'llm', add conditional edges from 'llm', add edge from 'tools' to 'llm'. Compile graph and stream inputs like {'messages': [('user', 'query')]}. This creates a ReAct loop of thought (model), action (tools), observation (tool results). For custom XML tool descriptions, use prompt templates with XML tags in system instructions as per prompting strategies. The example demonstrates thought generation via model calls interleaved with actions, matching minimal ReAct phase.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://ai.google.dev/gemini-api/docs/prompting-strategies

Query: How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python?

Answer: Google's prompting strategies guide details custom XML tool descriptions and prompt templates for Gemini API. Use structured XML tags to distinguish instructions, context, and tasks: <role>You are a helpful assistant.</role><constraints>1. Be objective. 2. Cite sources.</constraints><context>[User input data]</context><task>[Specific request]</task>. For ReAct thought generation, enhance reasoning with: 'You are a very strong reasoner and planner. Use these critical instructions to structure your plans, thoughts, and responses. Before taking any action (tool calls or user responses), proactively plan and reason about: 1) Logical dependencies...'. Markdown alternatives: # Identity
You are a senior solution architect.# Constraints
- No external libraries.# Output format
Return a single code block. Combine with Gemini thinking for internal reasoning. System instruction template: <role>Gemini specialist</role><instructions>1. Plan 2. Execute 3. Validate 4. Format</instructions><constraints>Verbosity: Medium</constraints><output_format>Executive Summary + Detailed Response</output_format>. User prompt: <context>[data]</context><task>[request]</task><final_instruction>Think step-by-step.</final_instruction>. Integrate into LangGraph's call_model node by formatting state['messages'] with these XML-wrapped templates before model.invoke for ReAct thought phase.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking

Query: How to implement a minimal ReAct thought generation phase using custom XML tool descriptions and prompt templates with the Gemini API in Python?

Answer: Vertex AI docs on Thinking explain Gemini's built-in thought generation for ReAct-like reasoning. Supported in Gemini 2.5+ models. Enable via thinking_config in generate_content: ThinkingConfig(thinking_budget=1024) for token limit on thoughts (0 to disable in some models). thinking_level (Gemini 3+): MINIMAL/LOW/MEDIUM/HIGH. Include thought summaries with include_thoughts=True. Python example: from google import genai; client.models.generate_content(model='gemini-2.5-pro', contents='query', config=GenerateContentConfig(thinking_config=ThinkingConfig(thinking_budget=1024))). Access thoughts via response.candidates[0].content.parts where part.thought. For ReAct, integrate into LangGraph's call_model node. Use XML prompts from strategies guide as system instructions to structure thoughts before tool actions. Thought signatures preserve reasoning state in multi-turn ReAct loops via chat history. Combine with custom XML templates for tool descriptions in prompts to guide thought->action phases.

-----

</details>

<details>
<summary>Best practices for using Gemini function calling to parse actions in a ReAct agent without including full tool signatures in the system prompt?</summary>

Phase: [EXPLOITATION]

### Source [4]: https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae

Query: Best practices for using Gemini function calling to parse actions in a ReAct agent without including full tool signatures in the system prompt?

Answer: The article details building a ReAct agent with Gemini that parses JSON responses from the language model in the `decide` method to determine actions without embedding full tool signatures in the system prompt. The prompt template lists available tools concisely as '{tools}' (e.g., 'wikipedia, google'), instructing the model to respond in strict JSON format: for tool use, {"thought": "reasoning", "action": {"name": "Tool name (wikipedia, google, or none)", "reason": "why", "input": "query"}}; for final answer, {"thought": "reasoning", "answer": "response"}. The `decide` method parses this JSON: if 'action' present, extracts tool name (e.g., Name[action["name"].upper()]) and input, calls `act`; if 'answer', logs final response. Error handling reverts to `think` if parsing fails. Prompt emphasizes: analyze query/history/tools, decide action or answer, use tools for more info, base on observations, final answer only when confident. This keeps system prompt tool-agnostic except names in parentheses, with dynamic tool list insertion, avoiding full signatures. Full template in repo. Agent iterates think-act-observe loop up to max_iterations=5.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://www.philschmid.de/langgraph-gemini-2-5-react-agent

Query: Best practices for using Gemini function calling to parse actions in a ReAct agent without including full tool signatures in the system prompt?

Answer: Builds ReAct agent from scratch with Gemini 2.5 Pro/2.0 Flash and LangGraph without full tool signatures in system prompt. Uses function calling: binds tools to model via llm.bind_tools([get_weather_forecast]), model generates structured ToolCalls. No tool details in prompt; system prompt optional (commented: 'You are a helpful assistant... Use the history...'). `call_model` node invokes bound model on messages. Conditional edge `should_continue` checks if last message has tool_calls: if yes, 'continue' to `call_tool` node executing tools_by_name[tool_call["name"]].invoke(tool_call["args"]); else 'end'. Graph: entry 'llm' → conditional (tools or END) → tools → llm. State: AgentState with messages (Annotated[Sequence[BaseMessage], add_messages]) and steps. Parses actions via Gemini's native function calling in AIMessage.tool_calls, not prompt parsing. Demonstrates weather tool (get_weather_forecast with Pydantic args_schema), streaming execution. Customizable nodes/edges for control without prompt bloat.

-----

-----

Phase: [EXPLOITATION]

### Source [6]: https://community.openai.com/t/converting-a-react-prompt-to-use-function-calling/264914

Query: Best practices for using Gemini function calling to parse actions in a ReAct agent without including full tool signatures in the system prompt?

Answer: OpenAI forum discusses migrating ReAct prompts to function calling, avoiding full signatures in prompts. Uses concise tool lists: 'You have access to: Query (for log data), Chart (for charts)'. Model generates JSON with 'action'/'action_input' parsed to function calls. Simplified prompt: 'consider executing a function call... result added as observation'. Issues: model mixes message/functions (2/3 times), raw JSON output. Solutions: separate planning step outputting JSON plan with 'Function'/'Parameters' placeholders (no full schemas), then function step. System prompt instructs: list tools, plan steps as {'Subtask', 'Reasoning', 'Function', 'Parameters'}, use only provided functions. Avoids full signatures by using placeholders, natural language params. Notes worse accuracy with verbose prompts; suggests task_complete function or removing steps. Relevant for Gemini: dynamic tool refs in decide/act without prompt signatures.

-----

</details>

<details>
<summary>How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?</summary>

Phase: [EXPLOITATION]

### Source [7]: https://www.decodingai.com/p/building-production-react-agents

Query: How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?

Answer: To build a turn-based ReAct control loop in Python using LangGraph, define a state as TypedDict called AgentState with 'messages': Sequence[BaseMessage] (scratchpad) and optional 'structured_response'. Use StateGraph to create nodes: 'model' for thought (LLM reasoning and tool calls), 'tools' via ToolNode for action/execution. Add edges: START -> model, conditional from model (check tool_calls or structured_response to route to 'tools' or END), tools -> model. Loop continues via conditional edges until no tool_calls or structured_response present. Messages accumulate observations as ToolMessage (success/error). Model node prepares ModelRequest with messages/state/tools, executes LLM (binds tools, adds system prompt), updates state with AIMessage (tool_calls) or structured_response. ToolNode executes tools, handles errors as ToolMessage for next observation/thought. This implements ReAct: Thought (model), Action (tools), Observation (ToolMessage update). Example state evolution: HumanMessage -> AIMessage(tool_calls) -> ToolMessage -> repeat until final. Use create_agent for high-level, but understand graph for custom. Structured outputs via ToolStrategy (Pydantic as tool) or ProviderStrategy, exit on structured_response.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide

Query: How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?

Answer: Build React class with turn-based loop via next() method. Init with tools:list[callable], max_steps=10, verbose=False. Use intermediate_steps:list[dict] as scratchpad logging question, thoughts, actions, action_input, observations, answer. build_messages() constructs system prompt with tools_description/docstrings, valid actions (tools + 'Final Answer'), JSON format instructions, intermediate_steps JSON. reason() calls LLM (gpt-4o) on messages, parses JSON for thought/action/action_input/is_final_answer. act(action, action_input) executes tool from tools_dict, returns observation str. next(): reason() -> add_step({'thought', 'action', 'action_input'}) -> if Final Answer: finish() else: observation=act() -> add_step({'observation'}) -> check max_steps. Loop via while not_finished: next(). finish() sets not_finished=False, finish_reason='final answer'/'max_steps_reached', adds {'answer': last action_input}. Properties: steps_count, duration, token_usage (tracks completions). Messages are dicts in prompt, steps are dicts in scratchpad. Handles observation processing by appending to intermediate_steps for next reason() context. Full prompt enforces JSON_BLOB: {'thought':..., 'action':..., 'action_input':...}, observation as {'observation':...}, final {'thought':..., 'action':'Final Answer', 'action_input':...}.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/

Query: How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?

Answer: Use LangGraph StateGraph(AgentState) where AgentState(TypedDict): messages:Annotated[list, operator.add], next_action:str, iterations:int (scratchpad via accumulating messages). Nodes: reasoning_node (LLM or hardcoded decides next_action='action'/'end', adds Thought message), action_node (extracts query from last message, executes tool, adds Action/Observation messages, sets next_action='reasoning'). Edges: set_entry_point('reasoning'), add_conditional_edges('reasoning', route=lambda s:s['next_action'], {'action':'action', 'end':END}), add_edge('action', 'reasoning'). Loop via action->reasoning until 'end'. For LLM: reasoning_node_llm prompts GPT-4o with history, enforces 'QUERY: ...' format, parses to set next_action. action_node_llm extracts query, calls llm_tool (OpenAI query), adds messages. app=workflow.compile(); app.invoke(initial_state). Messages accumulate thoughts/actions/observations as list[str]. Turn-based via graph execution. Observation integrated by appending to messages for next reasoning.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/

Query: How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?

Answer: Implement ReAct loop manually: maintain messages:list[dict] (system/user/assistant/tool roles). Prompt enforces format: Thought:..., Action: tool_name, Action Input: JSON {...}, Observation: tool result. Loop: while max_iterations: llm_response = client.chat.completions.create(messages, tools=function_schemas); append response_message; if tool_calls: for each: execute tool (e.g. search), append {'role':'tool', 'content':result, 'tool_call_id':id}. Parse response for Thought/Action Input/Observation. Final: Thought:... Final Answer: .... Scratchpad via accumulating messages with intermediate steps. Observation processing: tool output as Observation in next prompt context. No explicit Message classes, uses OpenAI dicts. Automate by parsing response content for 'Action:'/'Final Answer:', execute if action != 'Final Answer'. Tools via function_schemas JSON.

-----

-----

Phase: [EXPLOITATION]

### Source [11]: https://peterroelants.github.io/posts/react-openai-function-calling/

Query: How to build a turn-based ReAct control loop in Python with structured Message classes, scratchpad management, and integrated observation processing for tool execution?

Answer: ReAct loop with OpenAI function calling: messages:list[dict] (system/user/assistant/tool) as scratchpad. System: 'Follow THOUGHT/ACTION/OBSERVATION pattern'. functions: get_current_location(), get_current_weather(), calculate(), finish() (raises StopException). Convert to function_schemas via as_json_schema(typing.Annotated/Literal). Loop max_iterations=20: response=openai_client.chat.completions.create(messages, tools=function_schemas); append response_message; if tool_calls: for tool_call: function_to_call=name_to_function_map[name]; args=json.loads(arguments); result=function_to_call(**args); append {'role':'tool', 'name':name, 'content':str(result), 'tool_call_id':id}. Catch StopException to end. Handles errors by appending error content. Observation via tool content in messages for next iteration. Turn-based accumulation until finish.

-----

</details>

<details>
<summary>Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?</summary>

Phase: [EXPLOITATION]

### Source [12]: https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/

Query: Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?

Answer: Building ReAct agents from scratch using only Python and an LLM demystifies frameworks like CrewAI, providing full control over behavior for optimization and troubleshooting. Educational benefits include understanding the ReAct pattern (Thought/Action/Observation cycle), how agents chain tool uses, maintain conversation context for coherence, and follow rigid response schemas for safe, deterministic, interpretable tool interactions. The article implements a manual ReAct loop for transparency and debugging, and an automated agent_loop() that parses reasoning and executes tools. It emphasizes prompt engineering to enforce structured Thought/Action/Observation/Final Answer format, reducing hallucinations via external tools. While not explicitly using mock tools, the from-scratch approach with simple tools like SerperDevTool demonstrates predictable responses through strict JSON formatting and protocol adherence, enabling students to see exact decision-making processes. Benefits: transparency in agent traces, improved reasoning with chain-of-thought, verifiability, and debugging skills. Implementation covers agent tool prompt format, action protocol, and loop repetition until Final Answer.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae

Query: Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?

Answer: Building ReAct agents from scratch teaches the Think-Act-Observe loop: agent analyzes query (Think), selects tools like Google Search/Wikipedia (Act), observes results, iterates until confident. Educational benefits: transparency in reasoning traces for debugging/trustworthiness, dynamic tool utilization, iterative problem-solving with memory of observations. Implementation uses Gemini LLM, custom Tool class with error handling (try/except returning str(Exception) as fallback), Agent class managing iterations (max_iterations=5), prompt template guiding JSON-structured responses with fallback to think() on errors. Tools implemented in serp.py/wiki.py provide predictable responses (top results with rank/title/link/snippet for Google; title/summary for Wikipedia). Fallback behavior: parsing errors revert to think(), no tool triggers think(), max iterations warning stops loop. Hands-on guide with GitHub repo shows full code for agent.py, emphasizing modular structure for easy extension, zero-shot/few-shot prompts, and comparison to rule-based systems highlighting ReAct's adaptability. Teaches overcoming hallucinations via real external data, adaptive multi-step reasoning.

-----

-----

Phase: [EXPLOITATION]

### Source [14]: https://blog.dailydoseofds.com/p/implement-react-agentic-pattern-from

Query: Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?

Answer: Implementing ReAct from scratch teaches Thought → Action → Observation → Answer loop powering agentic systems, system prompts for step-by-step deterministic tool calling, lightweight agent class for conversation tracking/LLM interfacing, manual loop for transparency/debugging, automated agent_loop() parsing reasoning/executing tools. Benefits: understand frameworks' inner workings, avoid confusion on tool decisions (e.g., web search/calculation), gain control for optimization. Covers structuring prompts teaching LLM rigid formats, full automation without manual intervention. Predictable via protocol enforcement; fallback implicit in loop continuation. Part of AI Agents Crash Course emphasizing practical, beginner-friendly learning.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025

Query: Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?

Answer: LangChain ReAct agent guide teaches structured problem-solving via reasoning-action alternation. Implementation: create_react_agent with LLM/tools/prompt, AgentExecutor with max_iterations=5, max_execution_time=60s, handle_parsing_errors=True for fallback. Custom tools (percentage_calculator, currency_formatter) with try/except returning error strings as predictable fallbacks. TavilySearchResults for web search. Prompt enforces Thought/Action/Action Input/Observation/Final Answer format, guidelines to use tools only when necessary, fallback on failure. run_agent_query wraps with comprehensive error handling returning success/error dicts. Educational: verbose=True traces steps, testing validates performance. Optimizations: low temperature for consistency, timeouts prevent delays, iteration limits avoid loops. Demonstrates production-ready error recovery, cost management via concise descriptions.

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://genmind.ch/posts/Building-ReAct-Agents-with-Microsoft-Agent-Framework-From-Theory-to-Production/

Query: Educational benefits and implementation of mock search tools with predictable responses and fallback behavior when teaching ReAct agents from scratch?

Answer: Microsoft Agent Framework implements ReAct/SPAR (Sense-Plan-Act-Reflect) for production agents. Educational: full code examples teach secure tool definition (@tool decorator, AST parsing for calculator avoiding eval()), middleware for logging ReAct iterations (THINK→ACT→OBSERVE), error handling providing fallbacks instead of crashing (context.result=error msg, agent adapts). web_search tool with input validation (length<500, no injection chars), 10s timeout, JSON output. max_iterations limit runaway loops. Observability via OpenTelemetry spans for invocations/tools/LLMs. Streaming for real-time feedback. Benchmarks show ReAct vs Planning tradeoffs. Monday plan: Week1 PoC with setup/customize/measure; production hardening (timeouts/circuit breakers), DevUI debugging. Benefits: grounded outputs, transparent traces, adaptability; teaches security (no eval(), validation), cost mgmt (iteration limits, model tiering).

-----

</details>

<details>
<summary>Analyzing success traces and graceful fallback behaviors in minimal ReAct implementations using Gemini to demonstrate error handling and forced termination?</summary>

Phase: [EXPLOITATION]

### Source [17]: https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae

Query: Analyzing success traces and graceful fallback behaviors in minimal ReAct implementations using Gemini to demonstrate error handling and forced termination?

Answer: The source provides a detailed hands-on guide to building minimal ReAct agents using Gemini, including analysis of success traces from real interactions and error handling mechanisms. It demonstrates three example output traces showing successful multi-step reasoning and tool usage: Example 1 (Who is older, Ronaldo or Messi?) succeeds in 3 iterations by iteratively querying Wikipedia for birthdates and comparing them, reaching a final answer. Example 2 (complex FIFA World Cup temperature query) succeeds in 4 iterations using Wikipedia then Google tools adaptively. Example 3 (most common ingredient in top GDP countries' dishes) shows adaptive fallback: after initial Google searches fail specificity, it switches to Wikipedia, then broadens to popular dishes, researches ingredients across countries (16 iterations total), and synthesizes themes like starchy staples when no single ingredient emerges, demonstrating graceful adaptation without failure. Error handling in the decide() method uses try-except to parse JSON responses from Gemini; on ValueError or Exception (e.g., invalid format), it logs the error and calls self.think() for retry. The think() method enforces forced termination via max_iterations=5 check, logging 'Reached maximum iterations. Stopping.' and returning without further action. Tool.use() catches exceptions, logs errors, and returns str(e) as Observation for agent recovery. Prompt instructions guide handling tool failures: 'If a tool returns no results or fails, acknowledge this and consider using a different tool or approach.' No explicit fallback agents, but adaptive tool switching (Google to Wikipedia) acts as graceful fallback. Traces available in GitHub repo.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://www.philschmid.de/langgraph-gemini-2-5-react-agent

Query: Analyzing success traces and graceful fallback behaviors in minimal ReAct implementations using Gemini to demonstrate error handling and forced termination?

Answer: The source details building a minimal ReAct agent from scratch using Gemini 2.5 Pro or 2.0 Flash with LangGraph, including a weather query example trace. Success trace for 'What is the weather in Berlin on 12th of March 2025?': AgentState starts with user message; llm node calls Gemini which outputs ToolCall to get_weather_forecast (location:Berlin, date:2025-03-12); tools node executes via geolocator and Open-Meteo API, returns hourly temps dict; loops back to llm which generates final answer summarizing temps (4.5°C to 8.2°C). Follow-up 'Would it be in Munich warmer?' succeeds similarly: tool call for Munich, observation of warmer temps (up to 10.6°C), final comparison answer. should_continue edge provides graceful control: if no tool_calls in last message, returns 'end' (terminates); else 'continue' (loops). No explicit error handling shown, but LangGraph's ToolNode and state management imply fallback via state updates; get_weather_forecast handles geocode failures ('Location not found') and API exceptions, returning error dicts as observations for agent reasoning. Forced termination via graph END node when no tools needed. Minimal implementation emphasizes graph-based flow for reliable ReAct without complex retry logic.

-----

-----

Phase: [EXPLOITATION]

### Source [19]: https://ai.google.dev/gemini-api/docs/langgraph-example

Query: Analyzing success traces and graceful fallback behaviors in minimal ReAct implementations using Gemini to demonstrate error handling and forced termination?

Answer: Official Google guide on minimal ReAct agent with Gemini and LangGraph for weather queries. Success trace for 'What is the weather in Berlin on {datetime.today()}?': User message → llm node (Gemini bound to get_weather_forecast tool) → ToolCall (location:Berlin, date:...) → tools node executes Open-Meteo API → ToolMessage with hourly temps dict → llm generates final summary answer → should_continue sees no tool_calls → 'end'. Follow-up 'Would it be warmer in Munich?': Similar flow, tool call for Munich temps → comparison answer. should_continue edge forces termination: if last message lacks tool_calls, return 'end'; else 'continue'. get_weather_forecast handles geocode failure ('Location not found') or API exceptions, returning error dicts as ToolMessage content for agent observation/reasoning. No explicit retries, but loop allows adaptive recovery; graph.compile() ensures controlled flow with END node for forced termination on no tools needed. Minimal AgentState with messages and steps counter demonstrates graceful single-source handling.

-----

</details>

<details>
<summary>What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?</summary>

Phase: [EXPLOITATION]

### Source [20]: https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae

Query: What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?

Answer: Step 1: Setting Up the Environment mentions providing tools as Python functions for Google Search (serp.py) and Wikipedia Search (wiki.py) under src/tools directory, but lacks specific Python environment setup details like pip installs or env vars. Step 2: Defining the Agent Structure shows imports: from enum import Enum, auto; from typing import Union, Callable; from pydantic import BaseModel, Field for Message and Choice models; class Tool with name and func; class Agent with GenerativeModel (Gemini). Enums: Name (WIKIPEDIA, GOOGLE, NONE). Observation = Union[str, Exception]. Agent init takes model: GenerativeModel. No explicit env var loading or client init shown. Uses Gemini Pro 1.5, prompt template with query, history, tools. Code in src/react/agent.py and GitHub repo https://github.com/arunpshankar/react-from-scratch. Tools in src/tools/serp.py and wiki.py. No dotenv or custom utils for env vars; focuses on agent classes, think-act-observe loop (think, decide, act methods parsing JSON responses). Prompt template in data/input/react.txt is zero-shot ReAct instructions.

-----

-----

Phase: [EXPLOITATION]

### Source [21]: https://community.openai.com/t/using-gemini-with-openai-agents-sdk/1307262

Query: What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?

Answer: Python example for using Gemini with OpenAI Agents SDK: Load env vars with load_dotenv(); gemini_api_key = os.getenv('GEMENI_API_KEY'); if not, raise ValueError. Create AsyncOpenAI client: AsyncOpenAI(api_key=gemini_api_key, base_url='https://generativelanguage.googleapis.com/v1beta/openai/'). Define model: OpenAIChatCompletionsModel(model='gemini-2.5-flash', openai_client=external_client). RunConfig(model=model, model_provider=external_client, tracing_disabled=True). Agent(name='Assitance', instructions='You are a helpful assistant.', model=model). Runner.run_sync(agent, input, run_config=config). Imports: os, dotenv.load_dotenv, agents (Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel), agents.run.RunConfig. .env: GEMENI_API_KEY=your_key. Demonstrates API key precedence via env var check, client init with base_url for Gemini OpenAI compatibility, model='gemini-2.5-flash'. No pydantic shown here.

-----

-----

Phase: [EXPLOITATION]

### Source [22]: https://www.philschmid.de/langgraph-gemini-2-5-react-agent

Query: What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?

Answer: Install: %pip install langgraph langchain-google-genai geopy requests. api_key = os.getenv('GEMINI_API_KEY', 'xxx'). Imports: typing (Annotated, Sequence, TypedDict), langchain_core.messages (BaseMessage), langgraph.graph.message (add_messages), langchain_core.tools (@tool), geopy.geocoders (Nominatim), pydantic (BaseModel, Field), requests. Define AgentState TypedDict with messages: Annotated[Sequence[BaseMessage], add_messages], number_of_steps: int. Tool: @tool('get_weather_forecast', args_schema=SearchInput(BaseModel with location:str, date:str)). llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro-exp-03-25', temperature=1.0, google_api_key=api_key). model = llm.bind_tools([get_weather_forecast]). Nodes: call_model invokes model.invoke(state['messages']); call_tool processes tool_calls. Conditional edge should_continue checks tool_calls. StateGraph(AgentState), add_node('llm', call_model), add_node('tools', call_tool), set_entry_point('llm'), add_conditional_edges, add_edge('tools', 'llm'), compile(). Demonstrates env var loading, pydantic for tool schema, client init via ChatGoogleGenerativeAI with api_key precedence, model like gemini-2.5-pro (similar to 2.5-flash).

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://ai.google.dev/gemini-api/docs/langgraph-example

Query: What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?

Answer: pip install langgraph langchain-google-genai geopy requests. api_key = os.getenv('GEMINI_API_KEY'). Imports: typing (Annotated, Sequence, TypedDict), langchain_core.messages (BaseMessage), langgraph.graph.message (add_messages), langchain_core.tools (@tool), geopy, pydantic (BaseModel, Field), requests. AgentState TypedDict: messages Annotated[Sequence[BaseMessage], add_messages], number_of_steps: int. Tool get_weather_forecast with SearchInput(BaseModel). llm = ChatGoogleGenerativeAI(model='gemini-3-flash-preview', temperature=1.0, max_retries=2, google_api_key=api_key). model = llm.bind_tools(tools). Nodes: call_model model.invoke, call_tool ToolMessage. should_continue if tool_calls. StateGraph, add_node llm/tools, set_entry_point llm, conditional_edges, add_edge tools->llm, compile. Official Google guide shows env var GEMINI_API_KEY precedence, pydantic BaseModel/Field for tool args, client ChatGoogleGenerativeAI(model='gemini-3-flash-preview'), LangGraph ReAct agent setup.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://www.freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini/

Query: What are the precise steps to set up a Python environment for a Gemini-based ReAct agent, including loading environment variables with custom utils, importing pydantic and other libraries, initializing the client with API key precedence, and defining the model ID like gemini-2.5-flash?

Answer: uv venv, uv add google-genai==1.12.1 python-dotenv==1.1.0. .env GEMINI_API_KEY=your_key, load_dotenv(), api_key=os.getenv('GEMINI_API_KEY'). client = genai.Client(api_key=api_key). generate_content(model='gemini-2.0-flash-001', contents=messages). Functions use pydantic? No explicit, but agent loop with tools (get_files_info etc.), system_instruction prompt. Imports genai.types (Content, Tool, FunctionDeclaration), dotenv. No LangGraph/ReAct specific, but agentic coding agent with function calling loop, model='gemini-2.0-flash-001' (close to 2.5-flash).

-----

</details>

<details>
<summary>What common limitations emerge when extending basic function calling or planning patterns from earlier lessons into multi-turn scenarios without a dedicated observation-integrated control loop, and how does implementing the full turn-based orchestration resolve them?</summary>

Phase: [EXPLOITATION]

### Source [25]: https://arxiv.org/html/2510.24663v1

Query: What common limitations emerge when extending basic function calling or planning patterns from earlier lessons into multi-turn scenarios without a dedicated observation-integrated control loop, and how does implementing the full turn-based orchestration resolve them?

Answer: In multi-turn scenarios without a dedicated observation-integrated control loop, common limitations include lost context across turns, inability to handle cross-turn dependencies, and poor error handling such as tool execution errors (e.g., timeouts) that require rescheduling unfinished execution paths. Basic function calling or planning patterns from single-turn settings fail because later turns may involve irrelevant queries needing completely new tool execution graphs, dependent queries building on partial outputs from earlier turns or responses, or errors in tool responses. Without proper orchestration, agents cannot maintain state, encode dependencies through task identifiers, or replan partial subgraphs.

Implementing full turn-based orchestration, modeled as Directed Acyclic Graphs (DAGs) in OrchDAG, resolves these by explicitly representing tool execution as graphs where nodes are tool calls with dependencies via edges. In multi-turn settings, the pipeline extends generation with nodes for three scenarios: (1) irrelevant query triggers new DAG; (2) dependent query encodes cross-turn dependencies via task IDs from previous DAG; (3) tool error reduces to partial subgraph for rescheduling. This maintains context through observations (𝒪1,…,𝒪t−1) fed into reasoning, enables replanning guided by execution results and new queries, and supports parallel execution of independent tools. The LLM generates plans p conditioned on tools 𝒯, descriptions 𝒟, query x, and prior observations, ensuring intermediate reasoning rt and final response ℛ integrate history. Graph-based rewards like weighted Graph Edit Distance (GED) further enhance training for reliable multi-turn performance.

-----

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.amazon.science/publications/orchdag-complex-tool-orchestration-in-multi-turn-interactions-with-plan-dags

Query: What common limitations emerge when extending basic function calling or planning patterns from earlier lessons into multi-turn scenarios without a dedicated observation-integrated control loop, and how does implementing the full turn-based orchestration resolve them?

Answer: Most existing work on agentic tool use overlooks the complexity of multi-turn tool interactions. Basic patterns fail in multi-turn scenarios due to intricate tool dependencies, JSON outputs with misaligned fields, and issues like timeouts or runtime errors requiring rescheduling. Without orchestration, agents struggle with cross-turn dependencies and error recovery.

OrchDAG's full turn-based orchestration models tool execution as controllable-complexity DAGs. It handles multi-turn by attaching nodes for: (1) irrelevant queries (new DAG), (2) dependent queries (cross-turn dependencies via task IDs), (3) errors (partial subgraphs). This maintains context, enables replanning, and uses graph-based rewards (e.g., GED) with RLVR training to improve performance, making multi-turn tool use robust.

-----

</details>

<details>
<summary>What real-world production strategies exist for swapping a simple mock search tool with actual external APIs like Google Search or domain-specific knowledge bases while preserving the same function signature and docstring-driven integration in a Gemini ReAct agent?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae

Query: What real-world production strategies exist for swapping a simple mock search tool with actual external APIs like Google Search or domain-specific knowledge bases while preserving the same function signature and docstring-driven integration in a Gemini ReAct agent?

Answer: The article details building ReAct agents with Gemini that integrate external APIs like Google Search (via SERP API) and Wikipedia API as tools. Tools are implemented as Python functions (e.g., in serp.py and wiki.py under src/tools) that encapsulate API calling logic, taking a query string and returning results. The Tool class wraps these functions with a consistent interface: def __init__(self, name: Name, func: Callable[[str], str]), where func has signature Callable[[str], str]. The agent registers tools via agent.register(name, func), preserving function signatures. Docstrings in tool definitions guide LLM selection. Dynamic tool utilization allows swapping mock implementations by replacing the func callback while keeping name, signature (query: str -> str), and docstring consistent. Examples show Google Search returning top 10 results (rank, title, link, snippet) and Wikipedia returning title/summary, enabling seamless replacement with other APIs (e.g., domain-specific knowledge bases) by updating the func to call the new API and format output similarly. The modular Tool registration and ReAct loop (think-act-observe) ensure integration remains docstring-driven without changing agent logic. GitHub repo: https://github.com/arunpshankar/react-from-scratch provides full code for mock-to-real swaps.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://atalupadhyay.wordpress.com/2025/11/25/building-a-real-time-web-searching-ai-agent-with-langchain-and-google-gemini/

Query: What real-world production strategies exist for swapping a simple mock search tool with actual external APIs like Google Search or domain-specific knowledge bases while preserving the same function signature and docstring-driven integration in a Gemini ReAct agent?

Answer: Uses LangChain with Gemini for ReAct agent. Custom tool defined with @tool decorator: def web_search_and_load(query: str) -> str, docstring: 'Searches the web using DuckDuckGo... useful for getting up-to-date news, documentation, and factual information.' This preserves signature (query: str -> str). Internally swaps mock by implementing DuckDuckGoSearchRun() for search, extracts link via regex, loads with WebBaseLoader, splits with RecursiveCharacterTextSplitter, returns combined content or fallback snippets. Agent created via create_react_agent(llm, tools, prompt), executed with AgentExecutor. Docstring drives LLM tool selection. Strategy: Replace internal logic (e.g., swap DuckDuckGoSearchRun with Google Search API call) while keeping @tool-wrapped function signature and docstring unchanged, ensuring seamless integration in ReAct loop. Handles errors by falling back to snippets, production-ready with chunking for token limits.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://ai.google.dev/gemini-api/docs/langgraph-example

Query: What real-world production strategies exist for swapping a simple mock search tool with actual external APIs like Google Search or domain-specific knowledge bases while preserving the same function signature and docstring-driven integration in a Gemini ReAct agent?

Answer: Official Google guide builds ReAct agent with Gemini and LangGraph. Tool defined as @tool('get_weather_forecast', args_schema=SearchInput): def get_weather_forecast(location: str, date: str), using geopy Nominatim and Open-Meteo API. Bound to model: llm.bind_tools([get_weather_forecast]). In graph, ToolNode executes via tools_by_name[tool_call['name']].invoke(tool_call['args']). Preserves signature via Pydantic args_schema and docstring for LLM selection. Swapping strategy: Replace tool func body (e.g., mock return with real Google Search API call returning formatted results) while keeping @tool decorator, name, args_schema (ensures signature), and docstring. LangGraph's modular nodes/edges (call_model, call_tool, should_continue) allow drop-in replacement without changing ReAct loop or agent state (messages: Annotated[Sequence[BaseMessage], add_messages]). Example extensible to domain-specific KB by updating func to query KB API.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://developers.googleblog.com/real-world-agent-examples-with-gemini-3/

Query: What real-world production strategies exist for swapping a simple mock search tool with actual external APIs like Google Search or domain-specific knowledge bases while preserving the same function signature and docstring-driven integration in a Gemini ReAct agent?

Answer: Google Developers Blog highlights production agents with Gemini 3. ADK (Agent Development Kit) composes agents with tools like Google Search/Maps/code execution. Retail Location Strategy agent uses LlmAgent with tools=[MCPToolset(connection_params=StdioServerParameters(command='python3', args=[PATH_TO_MCP_SERVER]))]. Swapping: Update MCP server functions (e.g., PATH_TO_MCP_SERVER=mock_search.py to real_google_search.py) while preserving tool names/docstrings in MCP @mcp.tool() for signature consistency. Agno/Phidata builds multi-agents with native Grounding with Google Search/URL context. Browser Use/Eigent/Letta/mem0 examples emphasize tool binding (llm.bind_tools) and stateful integration. Strategy: Modular tool registration (e.g., ADK's tools list, LangGraph ToolNode) allows replacing impl (mock -> real API) keeping signatures/docstrings for docstring-driven ReAct selection.

-----

</details>

<details>
<summary>How does hands-on implementation of the complete Thought Action Observation cycle using a notebook provide a concrete mental model for aspiring AI engineers to debug and extend agents with confidence?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://pub.towardsai.net/beyond-the-prompt-engineering-the-thought-action-observation-loop-2e1fd99114d2

Query: How does hands-on implementation of the complete Thought Action Observation cycle using a notebook provide a concrete mental model for aspiring AI engineers to debug and extend agents with confidence?

Answer: The source discusses engineering the Thought-Action-Observation loop for AI agents, emphasizing agentic workflows over one-shot prompts. It details a Loop architecture with tools like Semantic Graph Search, Table Schema, Shape Detector, and Execute Query, governed by strict System Instructions that enforce the protocol: DISCOVER (semantic_graph_search), INSPECT (get_table_schema), VALIDATE (get_column_stats), EXECUTE (execute_query). Error handling includes self-healing: if execute_query fails, the agent analyzes the error, adjusts SQL, and retries. This iterative process with real-time feedback from observations allows agents to debug and self-correct, like fixing column name errors by rechecking schema. Hands-on implementation in notebooks would concretize this mental model by letting engineers observe the full cycle, trace thoughts/actions/observations, debug failures (e.g., hallucinations, bad groupings), and extend with new tools, building confidence in creating robust, deterministic agents for complex tasks.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://blog.stackademic.com/ai-agents-iv-ai-agents-through-the-thought-action-observation-tao-cycle-3dfe2eb76629

Query: How does hands-on implementation of the complete Thought Action Observation cycle using a notebook provide a concrete mental model for aspiring AI engineers to debug and extend agents with confidence?

Answer: The source explains the Thought-Action-Observation (TAO) cycle: Thought (internal reasoning, planning, decision-making), Action (tool calls like APIs, code execution), Observation (feedback integration). Examples include weather API retrieval where observation updates state for refinement. ReAct prompting structures this cycle to reduce errors. Implementing in notebooks allows engineers to step through cycles, inspect thoughts (e.g., self-reflection, problem-solving), parse actions (JSON/function calls), process observations (system feedback, data changes), and iterate. This hands-on practice provides a concrete mental model for debugging (e.g., handling 404 errors, adapting strategies) and extending agents (adding tools, memory), fostering confidence in building adaptive agents.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://huggingface.co/learn/agents-course/unit1/agent-steps-and-structure

Query: How does hands-on implementation of the complete Thought Action Observation cycle using a notebook provide a concrete mental model for aspiring AI engineers to debug and extend agents with confidence?

Answer: The Hugging Face Agents Course details the Thought-Action-Observation cycle: Thought (reasoning like 'I need weather data'), Action (JSON tool call e.g., get_weather('New York')), Observation (API response added to context), repeating until final answer. Alfred weather agent example shows iteration: if observation indicates error/incomplete data, re-enter cycle. System prompts embed rules for the loop. Hands-on notebook implementation visualizes each step, letting aspiring engineers trace reasoning, execute tools, observe feedback, debug loops (e.g., tool failures), and extend (add tools, refine prompts), building a concrete mental model for confident agent development.

-----

-----

Phase: [EXPLOITATION]

### Source [34]: https://projector-video-pdf-converter.datacamp.com/42942/chapter2.pdf

Query: How does hands-on implementation of the complete Thought Action Observation cycle using a notebook provide a concrete mental model for aspiring AI engineers to debug and extend agents with confidence?

Answer: DataCamp material from Hugging Face Agents Course describes Thought-Action-Observation: Thought (decide next step), Action (tool call), Observation (reflect on tool response, feed back). Customer support example shows multi-cycle: check account, policy, process refund, update status. ReAct prompting structures this for accuracy (e.g., arithmetic: without ReAct $2776.63 error, with $2475.85 correct). Notebook implementation lets engineers practice full cycles, spot errors in thoughts/actions/observations, debug (e.g., via self-reflection), extend tools/memory, providing concrete model for confident debugging/extension.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>How have ReAct-inspired reasoning loops been adapted for clinical decision support systems that query specialized medical knowledge bases rather than general web search?</summary>

Phase: [EXPLORATION]

### Source [35]: https://medium.com/@alexglee/building-framework-for-ai-agents-in-healthcare-e6b2c0935c93

Query: How have ReAct-inspired reasoning loops been adapted for clinical decision support systems that query specialized medical knowledge bases rather than general web search?

Answer: ReAct + RAG AI Agents represent a fusion of reasoning and acting (ReAct) and retrieval-augmented generation (RAG). These agents handle complex, multi-step clinical decisions by simulating human-like problem-solving logic while dynamically integrating external medical knowledge from evidence databases, diagnostic calculators, or medical references as external tools to support reasoning. ReAct agents decompose ambiguous problems like diagnosing overlapping symptoms into manageable decision paths. RAG modules access up-to-date guidelines, research papers, or population-level clinical data. They feature advanced reasoning logic combining deterministic rules with unstructured inference and external knowledge retrieval. Invaluable for high-stakes decision support in rare disease triage, critical care planning, and oncology treatment selection. Tool Integration Module: Invoke evidence databases, diagnostic calculators, or medical references. Reasoning Modules: Advanced reasoning logic with external knowledge retrieval. Perception Modules: Multimodal perception enriched through continual retrieval of external data. Conversational Modules: Interactive decision-making, breaking down problems into sub-questions and fetching supporting knowledge in real time. Interaction Modules: Integration with clinician workflows and EMRs for real-time clinical decision support. Memory and Learning Modules: Track previous reasoning paths and clinical responses for context-sensitive inference.

-----

-----

Phase: [EXPLORATION]

### Source [36]: https://arxiv.org/html/2603.26182v1

Query: How have ReAct-inspired reasoning loops been adapted for clinical decision support systems that query specialized medical knowledge bases rather than general web search?

Answer: ReAct (Yao et al., 2022) interleaves reasoning traces with tool-using actions (e.g., retrieval), providing a paradigm that motivates the shift from passive LLMs to active agentic systems. ClinicalAgents, a multi-agent framework, builds on ReAct-like agentic scaffolds for multi-step clinical reasoning. It uses a dynamic orchestration mechanism modeled as Monte Carlo Tree Search (MCTS) with hypothesis-driven expansion and backtracking. Specialized agents generate hypotheses, verify evidence from clinical guidelines and historical cases via dual-memory (Working Memory for patient state and Experience Memory for knowledge retrieval), and refine diagnoses. Compared to single-agent ReAct baseline (average score 0.4696 on MedChain benchmark), ClinicalAgents achieves SOTA performance (0.5107), improving by +8.8%. The orchestrator’s verification-and-backtracking loop reduces error accumulation. Dual-Memory integrates hybrid RAG for passive augmentation and active evidence-seeking from guideline database and historical cases, improving reasoning consistency. Experiments on MedChain benchmark show substantial gains over ReAct in multi-stage clinical workflow tasks like specialty referral, test ordering, examination, diagnosis, and treatment.

-----

-----

Phase: [EXPLORATION]

### Source [37]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12383471/

Query: How have ReAct-inspired reasoning loops been adapted for clinical decision support systems that query specialized medical knowledge bases rather than general web search?

Answer: Self-Query Retrieval (SQR) framework adapts RAG for clinical decision support by having LLM generate structured queries (PICOT/SPICE) from free-text clinical questions to retrieve from specialized medical knowledge bases (rhinoplasty sources). Iterative Query Refinement (IQR) loop dynamically adjusts queries based on initial results until quality thresholds met, mimicking ReAct-like reasoning-acting cycles. Full SQR+IQR pipeline on Gemini-1.0 Pro for 30 postoperative rhinoplasty queries achieved 87% accuracy (Likert 2.4±0.7), 100% relevance (3.0±0.0), precision 0.53, recall 1.00, F1 0.70—outperforming naive RAG (50% accuracy, precision 0.17, recall 0.40, F1 0.24). PICOT/SPICE restructuring bridges semantic gap between natural queries and document structure in medical corpora. Composite scoring (semantic+lexical+length) prioritizes evidence. Adaptive loop self-critiques/rewrites up to 10 iterations, selecting highest-confidence response. Model-agnostic, modular for specialties/data sources/LLMs.

-----

-----

Phase: [EXPLORATION]

### Source [38]: https://nus-project.github.io/Landmark-of-medical-agent/

Query: How have ReAct-inspired reasoning loops been adapted for clinical decision support systems that query specialized medical knowledge bases rather than general web search?

Answer: ReAct cited as foundational for agentic systems in medical agents survey. ClinicalAgents uses ReAct-like interleaving of reasoning/tool-use with MCTS orchestration, dual-memory for guideline/historical case retrieval, achieving SOTA on MedChain over ReAct baseline. MedAgents, MDAgents, ColaCare use multi-agent collaboration inspired by ReAct for zero-shot reasoning, EHR modeling. Agent Hospital simulates evolvable agents. Tree-of-Reasoning structures interactions into evidence trees. MedChain provides sequential benchmarking. Benchmarks like MedConsultBench, MedAgentBench evaluate ReAct-style agents on consultation, reasoning. Frameworks like MedMASLab benchmark multimodal multi-agent systems. Papers adapt ReAct loops for diagnosis, report generation, VQA via tool integration, memory, self-improvement.

-----

</details>

<details>
<summary>What lessons from simple notebook-style ReAct agents have informed the design of autonomous systems for scientific literature synthesis and hypothesis generation in research workflows?</summary>

Phase: [EXPLORATION]

### Source [40]: https://medium.com/@khayyam.h/ai-agents-for-scientific-workflow-automation-from-hypothesis-to-experiment-c1ab5043dc00

Query: What lessons from simple notebook-style ReAct agents have informed the design of autonomous systems for scientific literature synthesis and hypothesis generation in research workflows?

Answer: The Medium article discusses AI agents for scientific workflow automation, emphasizing tool integration as a requirement rather than enhancement, drawing from systems like ChemCrow which uses ReAct-like patterns where LLMs orchestrate workflows while delegating to specialized tools. It highlights lessons from Robot Scientist Adam, where structured knowledge enabled testable hypotheses, extended in modern efforts like Genesis. Key insight: hypothesis generation is partially automated when knowledge is structured and tool-assisted. Agents help navigate science via evidence synthesis, contradiction detection, and gap identification from literature. Reliability requires tool integration to reduce hallucinations, grounding in verified outputs. No explicit mention of 'notebook-style ReAct agents,' but describes ReAct-like iterative planning in ChemCrow for chemistry tasks, informing autonomous systems by emphasizing systems over models, with tool use essential for literature synthesis and hypothesis generation.

-----

-----

Phase: [EXPLORATION]

### Source [41]: https://arxiv.org/html/2510.09901v2

Query: What lessons from simple notebook-style ReAct agents have informed the design of autonomous systems for scientific literature synthesis and hypothesis generation in research workflows?

Answer: The arXiv paper on Autonomous Agents for Scientific Discovery discusses ReAct framework explicitly in experimental execution section: ChemToolAgent uses ReAct to orchestrate 29 chemistry tools in Thought-Action-Observation loop for chemistry problem-solving. Biomni uses CodeAct (ReAct extension) for biomedical data analysis. PerTurboAgent uses reflection in ReAct-like closed-loop for Perturb-seq. These inform design by enabling reflective, iterative tool use bridging reasoning and execution. For literature synthesis and hypothesis generation, Knowledge Extraction uses RAG and scientific foundation models; Hypothesis Generation uses prompt-based, knowledge-grounded, multi-agent, evolutionary methods progressing beyond LBD. Lessons: ReAct enables dynamic workflow orchestration, grounding reasoning in tools/databases, reducing hallucination—key for reliable synthesis and testable hypotheses in autonomous systems.

-----

-----

Phase: [EXPLORATION]

### Source [42]: https://arxiv.org/html/2508.14111v2

Query: What lessons from simple notebook-style ReAct agents have informed the design of autonomous systems for scientific literature synthesis and hypothesis generation in research workflows?

Answer: The survey 'From AI for Science to Agentic Science' positions ReAct as key in planning engines for scientific agents: ReAct loops (thought-act-observe) for dynamic adaptation. Used in ChemToolAgent, Biomni for chemistry/biology. Informs Observation & Hypothesis Generation via memory (RAG for literature synthesis) and reasoning for gap identification. Lessons: interleaving reasoning-acting enables agents to synthesize corpora (LitLLM), structure knowledge graphs, formulate testable hypotheses (SciAgents, Robin). Challenges: vast hypothesis space, knowledge veracity. ReAct's adaptability grounds synthesis in external tools, reducing hallucinations for reliable autonomous hypothesis generation.

-----

-----

Phase: [EXPLORATION]

### Source [43]: https://www.ibm.com/think/topics/react-agent

Query: What lessons from simple notebook-style ReAct agents have informed the design of autonomous systems for scientific literature synthesis and hypothesis generation in research workflows?

Answer: IBM page defines ReAct agents as integrating CoT reasoning with tool use for complex tasks. Inspired human-like step-by-step planning. Benefits: adaptability via dynamic tool calls, explainability via verbalized reasoning, accuracy by grounding in external info. No direct science examples, but framework enables literature synthesis (RAG/tools) and hypothesis via iterative thought-action-observation loops. Lessons for autonomous systems: notebook-style (simple, iterative) ReAct prompts structure agents for flexible workflows, reducing hallucinations—ideal for synthesis/hypothesis generation.

-----

</details>

<details>
<summary>How is the ReAct pattern evolving when integrated with creative content generation pipelines in marketing and storytelling applications?</summary>

Phase: [EXPLORATION]

### Source [44]: https://www.promptingguide.ai/techniques/react

Query: How is the ReAct pattern evolving when integrated with creative content generation pipelines in marketing and storytelling applications?

Answer: ReAct prompting, introduced by Yao et al. (2022), is a framework where LLMs generate reasoning traces (Thought) and task-specific actions (Action) in an interleaved manner, with Observations from external tools. This enables dynamic reasoning, plan adjustment, and interaction with external sources like search engines or calculators. ReAct outperforms baselines on knowledge-intensive QA (HotpotQA, Fever) and decision-making tasks (ALFWorld, WebShop) by combining internal knowledge with external information, reducing hallucinations. Combined with Chain-of-Thought (CoT), it enhances reliability. In practice, LangChain implements ReAct agents for tasks like searching 'Olivia Wilde's boyfriend' then computing math. No direct mention of creative content generation, marketing, or storytelling, but the reasoning-acting loop supports complex, multi-step creative pipelines by enabling tool use for ideation, research, and generation.

-----

-----

Phase: [EXPLORATION]

### Source [45]: https://www.salesforce.com/agentforce/ai-agents/react-agents/

Query: How is the ReAct pattern evolving when integrated with creative content generation pipelines in marketing and storytelling applications?

Answer: ReAct agents interleave Thought (reasoning via CoT), Action (tool/API calls), and Observation in a loop for multi-step problem-solving. Evolving from reason-only or act-only limitations, ReAct enhances accuracy, explainability, and handles complex tasks like customer service triage, data analysis, workflow orchestration. Benefits include reduced hallucinations via external verification, transparency through verbalized thoughts. Used in enterprises for automated reporting, CRM queries. Future: hybrid agents with perpetual learning, on-device deployment. Compares to function calling (less reasoning) and other patterns like Plan-and-Execute. No specific marketing/storytelling examples, but applicable to creative workflows via dynamic planning and tool integration for content research, generation, adaptation.

-----

</details>

<details>
<summary>In what ways have early ReAct implementations influenced multi-agent coordination strategies used in enterprise automation and workflow orchestration platforms?</summary>

Phase: [EXPLORATION]

### Source [49]: https://www.salesforce.com/agentforce/ai-agents/react-agents/

Query: In what ways have early ReAct implementations influenced multi-agent coordination strategies used in enterprise automation and workflow orchestration platforms?

Answer: The source explains ReAct agents, which interleave reasoning (Thought), action (using tools/APIs), and observation for complex problem-solving. In enterprise contexts, ReAct agents enable advanced workflow orchestration by acting as orchestrators that delegate subtasks to specialized agents (e.g., data scraping to one agent, document generation to another) while maintaining high-level reasoning. This supports multi-agent coordination in large enterprises where tasks span departments. Practical applications include automated customer service triage, data analysis, financial reporting, and workflow orchestration. ReAct improves accuracy, explainability, and multi-step problem-solving compared to function-calling agents. It influences strategies by providing a structured reasoning-action loop that enhances agentic workflows, though specific 'early implementations' influence is not detailed.

-----

-----

Phase: [EXPLORATION]

### Source [50]: https://www.ibm.com/think/topics/react-agent

Query: In what ways have early ReAct implementations influenced multi-agent coordination strategies used in enterprise automation and workflow orchestration platforms?

Answer: The source defines ReAct agents as using the ReAct framework (from 2023 paper) to combine chain-of-thought reasoning with external tool use for agentic workflows. ReAct agents dynamically adjust via thought-action-observation loops, enabling versatile, adaptable coordination from RAG to multi-agent workflows. Benefits include versatility, adaptability, explainability, and accuracy. In multi-agent setups, a central ReAct agent can delegate to smaller models. Compared to function calling, ReAct suits complex, dynamic tasks. It powers AI applications for autonomous planning/execution, influencing enterprise strategies through LLM-driven coordination without predefined workflows. No explicit mention of early implementations' specific enterprise impacts.

-----

</details>

<details>
<summary>What theoretical foundations from the original ReAct paper explain the design choice of forced final-answer generation upon reaching max_turns, and how does this interact with Gemini's native reasoning capabilities in incomplete trajectories?</summary>

Phase: [EXPLORATION]

### Source [52]: https://arxiv.org/abs/2210.03629

Query: What theoretical foundations from the original ReAct paper explain the design choice of forced final-answer generation upon reaching max_turns, and how does this interact with Gemini's native reasoning capabilities in incomplete trajectories?

Answer: The original ReAct paper introduces ReAct prompting, which interleaves reasoning traces and task-specific actions for LLMs. It addresses limitations of chain-of-thought (CoT) reasoning, such as hallucinations and error propagation, by enabling interaction with external sources like Wikipedia API. ReAct generates human-like task-solving trajectories that are more interpretable. On HotpotQA and Fever, ReAct overcomes CoT issues via external interactions. On ALFWorld and WebShop, it outperforms imitation and RL baselines by 34% and 10% success rates with few-shot prompting. No explicit mention of 'max_turns' or forced final-answer generation upon reaching a limit. The paper demonstrates ReAct's synergy between reasoning and acting, improving effectiveness, interpretability, and trustworthiness over baselines without reasoning or acting components. ReAct decides when to reason or act based on task demands, but does not detail loop termination mechanisms like max turns.

-----

-----

Phase: [EXPLORATION]

### Source [53]: https://medium.com/@deejairesearcher/react-paper-explained-simply-how-language-models-can-think-and-act-f500395f88db

Query: What theoretical foundations from the original ReAct paper explain the design choice of forced final-answer generation upon reaching max_turns, and how does this interact with Gemini's native reasoning capabilities in incomplete trajectories?

Answer: ReAct can struggle due to structural rigidity (reasoning → action → observation), sometimes getting stuck in loops by repeating the same thoughts or actions. This rigidity helps grounding facts but limits creative reasoning. The paper allows switching: ReAct → CoT-SC when ReAct fails to return an answer within a set number of steps (7 or 5). This addresses loop issues by forcing a switch after max steps, preventing infinite loops. No direct discussion of forced final-answer generation or interaction with Gemini's capabilities. Focuses on ReAct's effectiveness over baselines, with loop mitigation via step limits and hybrid approaches.

-----

-----

Phase: [EXPLORATION]

### Source [54]: https://www.mindfiretechnology.com/blog/archive/ai-tutorial-a-react-agent-using-gemini-and-haystack/

Query: What theoretical foundations from the original ReAct paper explain the design choice of forced final-answer generation upon reaching max_turns, and how does this interact with Gemini's native reasoning capabilities in incomplete trajectories?

Answer: In this ReAct agent using Gemini and Haystack, the agent tracks iteration count and gracefully ends when it hits the 'answer' function after max steps (e.g., six reasoning steps before Wikipedia fallback). Conversation state and flow control discourage premature actions and ensure termination. Final response via 'answer()' lists sources. Leverages Gemini's function calling. Forces final answer implicitly via max iterations to prevent loops, aligning with ReAct pattern. Gemini's reasoning used for step-by-step planning, searching datastore first, then fallback. No theoretical foundations from original paper cited; practical implementation ensures timely final answer even if incomplete.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="build-react-agents-from-scratch-simple-guide.md">
<details>
<summary>Building Production ReAct Agents From Scratch Is Simple</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.decodingai.com/p/building-production-react-agents>

# Building Production ReAct Agents From Scratch Is Simple

### I read LangGraph's implementation so that you can build your own, as AI frameworks just bloat your code.

[Paul Iusztin](https://substack.com/@pauliusztin)

Nov 18, 2025

_**Welcome to the AI Agents Foundations series**: A 9-part journey from Python developer to AI Engineer. Made by busy people. For busy people._

Everyone’s talking about AI agents. But what actually is an agent? When do we need them? How do they plan and use tools? How do we pick the correct AI tools and agentic architecture? …and most importantly, where do we even start?

To answer all these questions (and more!), We’ve started a 9-article straight-to-the-point series to build the skills and mental models to ship real AI agents in production.

We will write everything from scratch, jumping directly into the building blocks that will teach you _“how to fish”_.

**What’s ahead**:

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. _**ReAct Agents From Scratch** ← You are here_

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. [Multimodal Agents](https://www.decodingai.com/p/stop-converting-documents-to-text)


By the end, you’ll have a deep understanding of how to design agents that think, plan, and execute—and most importantly, how to integrate them in your AI apps without being overly reliant on any AI framework.

**Let’s get started.**

* * *

## Writing ReAct From Scratch

When I started building Brown, my writing agent, I decided to use LangGraph to implement the ReAct pattern. I embraced their graph model with nodes and edges, thinking it would make everything cleaner. But what I discovered was frustrating: simple if-else logic and basic loops that should have taken five minutes became hours of work. I had to force my Python code to fit their graph paradigm, modeling everything through edges in ways that felt unnatural. It did not add real value, just complexity.

After struggling with this, I did what I always do when I am stuck: I opened the LangGraph source code and started reading. That is when everything clicked. Seeing how they actually implemented the ReAct loop, the thought generation, tool execution, state management, and control flow, gave me a concrete mental model I could not get from their documentation. Even though I was not going to use their framework in production, understanding their implementation became the foundation for building my own robust ReAct agent from scratch.

People rarely understand what it takes to implement a ReAct solution. Often in production, you end up writing your own agentic layer because AI frameworks can fall short: abstractions limit access to cutting-edge features, and graph models like LangGraph can make simple logic overly complicated. The sweet spot is using lightweight infrastructure that lets you write custom logic while providing production-ready features like retries and monitoring.

The solution is to understand how production-ready frameworks are built. LangChain and LangGraph’s ReAct implementation is one of the most mature out there, so understanding it is one of the best ways to learn how ReAct works. Reading open-source software is my favorite way of learning, so I decided to write this article based on their implementation after it personally helped me understand how a production-ready ReAct Agent should be implemented.

We will walk you through the core elements of LangGraph’s ReAct implementation, step by step, using a Wikipedia research agent as an example. First, we will implement a simple agent using LangChain’s `create_agent` function. Then, we will dig into what happens under the hood. The full implementation has over 2,000 lines of code, so we will focus only on the core functionality.

## Defining Our Research Agent

To ground our exploration of LangGraph’s internals, we will first build a simple Wikipedia research agent. This example will serve as our reference point as we dive into the source code.

1. We start by defining our tools. The `@tool` decorator makes a Python function available to the agent. We have one tool to fetch content from Wikipedia and another to create a summary.


```
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.tools import tool
from langchain.chat_models import init_chat_model

@tool
def fetch_wikipedia_content(query: str, max_docs: int = 1) -> str:
    “””Fetches Wikipedia article content based on the search query.”””

    retriever = WikipediaRetriever(load_max_docs=max_docs, doc_content_chars_max=5000)
    docs = retriever.invoke(query)
    if not docs:
        return f”No Wikipedia articles found for query: {query}”

    return docs[0].page_content

@tool
def create_summary(text: str, focus: str = “general”) -> str:
    “””Creates a concise summary of the given text with a specified focus.”””

    llm = init_chat_model(model=”google_genai:gemini-1.5-flash-lite”, temperature=0.3)
    prompt = f”Please provide a {focus} summary of the following text...”
    response = llm.invoke(prompt)

    return response.content
```

2. Next, we define the desired final output structure using a Pydantic model. This ensures our agent returns validated, structured data.


```
from pydantic import BaseModel, Field
from typing import List

class DeepResearchResult(BaseModel):
    “””Structured output containing document title, summary, tags, and paragraph count.”””

    title: str = Field(description=”The title of the document”)
    summary: str = Field(description=”A comprehensive summary of the document content”)
    tags: List[str] = Field(description=”A list of relevant tags or keywords”)
    total_paragraphs: int = Field(description=”The total number of paragraphs in the document”)
```

3. We create the agent using LangChain’s high-level `create_agent` function. We pass the model, tools, a system prompt, and our desired response format.


```
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

agent = create_agent(
    model=”google_genai:gemini-1.5-flash”,
    tools=[fetch_wikipedia_content, create_summary],
    response_format=ToolStrategy(DeepResearchResult),
    system_prompt=”You are a helpful Wikipedia research assistant...”,
)
```

4. Finally, we invoke the agent by streaming its execution, which allows us to see each step as it happens.


```
initial_state = {”messages”: [HumanMessage(content=”Research cognitive behavioral therapy”)]}
for event in agent.stream(initial_state):
    # Process and print each step
    ...
```

This simple setup hides a lot of complexity. Now, let’s look under the hood to see how LangGraph actually builds and runs this agent.

## The ReAct LangGraph Graph

The [create\_agent](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L544) function builds a stateful graph using LangGraph. This graph defines the agent’s structure and control flow.

> 💡 You can find the full implementation of the [create\_agent](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L544) in LangChain’s open-source repository. We warn you, there are many abstractions going on. We hope this article will help you get over them.

The graph itself is initialized as a `StateGraph` object, which is a specialized graph that passes a state object between its nodes. The state contains all the information about the current execution, like the conversation history. In other words, you can think of it as the short-term memory. After initialization, the core `model` and `tools` nodes are added.

```
# Simplified from factory.py
from langgraph.graph.state import StateGraph

# The graph is created with a specific state schema
graph = StateGraph(state_schema=...)

# The two main nodes are added
graph.add_node(”model”, model_node)
graph.add_node(”tools”, tool_node)

# Edges define the flow between nodes
graph.add_edge(START, “model”)
graph.add_conditional_edges(”model”, should_continue, ...)
graph.add_edge(”tools”, “model”)
```

This graph structure directly maps to the ReAct pattern. The nodes represent the “Reason” and “Act” phases, the state aggregates all the observations, while the edges create the iterative loop that cycles through these stages until completion.

_By looking at Image 1, the mapping between the theoretical version of ReAct and LangChain’s implementation can be reduced to 6 core points:_

1. **Query** _**:**_ Enters the system via `START -> Model`, routing the initial user input to the model node.

2. **Thought:** The generation happens within the model node, where the LLM interprets context and plans the next steps.

3. **Action:** Executes all the tools within the `Tools` node.

4. **Tool Output:** Gathers all the tool outputs as observations and updates the graph state

5. **Thought:** Generates a new thought based on the latest state and it either decides it has completed the query or runs another iteration

6. **Final Answer:** In case the user query is achieved, it generates the final answer to the user


https://substackcdn.com/image/fetch/$s_!dao1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18fbf52c-81d7-4254-a378-ccf67970c56d_1200x1200.png Image 1: A flowchart comparing the theoretical ReAct loop with its LangGraph implementation, highlighting the mapping between their phases.

The state is defined as a `TypedDict` called `AgentState`. It holds the list of messages (the scratchpad) and an optional field for the final structured response.

```
from typing import TypedDict, Sequence
from langchain_core.messages import BaseMessage

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    structured_response: ... # Optional
```

As the agent runs, this state object evolves. For example:

1. **Initial State**: `{”messages”: [HumanMessage(...)]}`

2. **After Model**: `{”messages”: [..., AIMessage(tool_calls=[...])]}`

3. **After Tools**: `{”messages”: [..., ToolMessage(content=...)]}`

4. **Final State**: `{”messages”: [...], “structured_response”: DeepResearchResult(...) }`


## Thought Phase: The Model Node

The “Thought” phase happens inside the `model` node. This is where the LLM reasons about the task and decides what to do next.

The `amodel_node` function in [factory.py](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L1162) handles this. It prepares a `ModelRequest` containing the current state, system prompt, and available tools. It then calls the model and updates the state with the response.

```
async def amodel_node(state: AgentState, runtime: Runtime[ContextT]) -> dict[str, Any]:
    “””Async model request handler with sequential middleware processing.”””

    request = ModelRequest(
        model=model,
        tools=default_tools,
        system_prompt=system_prompt,
        response_format=initial_response_format,
        messages=state[”messages”],
        tool_choice=None,
        state=state,
        runtime=runtime,
    )

    response = await _execute_model_async(request)

    state_updates = {”messages”: response.result}
    if response.structured_response is not None:
        state_updates[”structured_response”] = response.structured_response

    return state_updates
```

The actual model execution happens inside the `_execute_model_async` function, defined in [factory.py](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L1085). This is where the system binds the tools, prepends the system prompt, and invokes the LLM.

```
async def _execute_model_async(request: ModelRequest) -> ModelResponse:
    # Get the bound model (with auto-detection if needed)
    model_, effective_response_format = _get_bound_model(request)
    messages = request.messages
    if request.system_prompt:
        messages = [SystemMessage(request.system_prompt), *messages]

    output = await model_.ainvoke(messages)

    # Handle model output to get messages and structured_response
    handled_output = _handle_model_output(output, effective_response_format)
    messages_list = handled_output[”messages”]
    structured_response = handled_output.get(”structured_response”)

    return ModelResponse(
        result=messages_list,
        structured_response=structured_response,
    )
```

The model knows which tools to use because they are “bound” to it. The `bind_tools` function converts the Python tool functions into a JSON schema that the LLM can understand. This schema, including the tool’s name, description (from the docstring), and parameters, is sent with every API call.

You might wonder why there is only one model node. Shouldn’t planning and tool-calling be separate steps? Modern reasoning models are designed to perform both in a single pass, as we detailed within the [planning lesson](https://www.decodingai.com/i/178235740/planning-and-executing-with-modern-reasoning-llms).

https://substackcdn.com/image/fetch/$s_!BQoQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4db7bcea-3094-47d1-a52b-c4cb7ddfb3ac_1027x420.png Image 2: Separating input, reasoning and output tokens when using reasoning LLMs

The model’s “thought” process and its “output” (the action to take) are generated together.

https://substackcdn.com/image/fetch/$s_!F6xt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F186c00e4-8658-4c7b-814c-9e53d1cd8cef_1156x797.png Image 3: A flowchart illustrating the merging of Planning and Action Generation into a single LLM API call.

For our Wikipedia agent, a typical thought + planning phase might produce an `AIMessage` containing a tool call like this:

```
AIMessage(
    content=”“,
    tool_calls=[\
        {\
            “name”: “fetch_wikipedia_content”,\
            “args”: {”query”: “cognitive behavioral therapy”},\
            “id”: “call_abc123”\
        }\
    ]
)
```

## Action Phase: The Tools Node

The “Action” phase is handled by the `tools` node. LangGraph uses a pre-built `ToolNode` for this, which is initialized with all the available tools.

```
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(tools=[fetch_wikipedia_content, create_summary])
```

The decision to execute a tool is made by a conditional edge. This edge is a function that inspects the state after the `model` node runs. The `_make_model_to_tools_edge` function checks if the last message from the model contains any pending `tool_calls`.

```
def _make_model_to_tools_edge(...):
    def model_to_tools(state: dict) -> str | list[Send] | None:
        # ... logic to get the last message ...
        last_ai_message = state[”messages”][-1]

        # Identify tool calls that haven’t been executed yet
        pending_tool_calls = [\
            tc for tc in last_ai_message.tool_calls if ... # logic to check if pending\
        ]

        # If there are pending tool calls, send them to the tools node
        if pending_tool_calls:
            return [\
                Send(\
                    “tools”,\
                    ToolCallWithContext(tool_call=tc, state=state),\
                )\
                for tc in pending_tool_calls\
            ]

        # Otherwise, end the loop
        return “end”

    return model_to_tools
```

If there are pending tool calls, the edge function returns a list of `Send` objects. `Send` is LangGraph’s mechanism for parallel execution. It directs each tool call to the `tools` node, and LangGraph runs them concurrently. This is a major advantage for production systems, as it can dramatically reduce latency. For example, if our agent decided to fetch multiple Wikipedia articles simultaneously, the `AIMessage` would contain three tool calls. The edge would then generate three `Send` objects to execute them in parallel.

```
[\
    Send(\
        “tools”,\
        ToolCallWithContext(\
            tool_call={”name”: “fetch_wikipedia_content”, “args”: {”query”: “AI Agents”}},\
            state=...\
        )\
    ),\
    Send(\
        “tools”,\
        ToolCallWithContext(\
            tool_call={”name”: “fetch_wikipedia_content”, “args”: {”query”: “ReAct Pattern”}},\
            state=...\
        )\
    ),\
    Send(\
        “tools”,\
        ToolCallWithContext(\
            tool_call={”name”: “fetch_wikipedia_content”, “args”: {”query”: “LangGraph”}},\
            state=...\
        )\
    )\
]
```

The `ToolNode` also has built-in error handling. If a tool fails, it catches the exception and returns a `ToolMessage` containing the error. This prevents the agent from crashing and allows it to reason about the failure in the next thought phase.

For our Wikipedia agent, when the model generates the `fetch_wikipedia_content` tool call, the `ToolNode` receives it, looks up the function in its registry, executes it with the provided arguments, and wraps the string output in a `ToolMessage`.

## Observation Phase: Updating the State

The “Observation” phase is not a distinct node but rather the process of updating the graph’s state with the results from the `tools` node.

The `ToolNode` automatically formats tool outputs as `ToolMessage` objects. These messages are then added to the `messages` list in the `AgentState`. LangGraph uses a reducer function called `add_messages` for this, which simply appends new messages to the existing list, preserving the full conversation history.

For example, after the `tools` node runs, the state update might look like this:

- **Existing State**: `{”messages”: [HumanMessage(...), AIMessage(tool_calls=[...])]}`

- **Update from ToolNode**: `{”messages”: [ToolMessage(content=”Title: Cognitive behavioral therapy...”)]}`

- **Resulting State**: `{”messages”: [HumanMessage(...), AIMessage(...), ToolMessage(...)]}`


If a tool fails, the `ToolMessage` will contain the error string. The LLM sees this error message in the next thought phase, just like any other observation, and can decide to retry the tool or try a different approach. This makes the agent resilient to tool failures.

## The Control Loop: Conditional Edges

The ReAct loop is defined by the conditional edges that route execution between the `model` and `tools` nodes. These edges are functions that inspect the current state and decide where to go next.

The primary loop is formed by two key connections added to the graph.

1. The edge from the `model` node to the `tools` node (or `END`) [defined at line 1344](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L1344). It uses the `_make_model_to_tools_edge` function to decide the next step.


```
graph.add_conditional_edges(
    # Source node is the model (or the last after_model hook)
    loop_exit_node,
    # The edge function decides the destination
    _make_model_to_tools_edge(...),
    # The possible destinations
    {”tools”: “tools”, “end”: END, “model”: “model”},
)
```

2. The edge from the `tools` node back to the `model` node [defined at line 1591](https://github.com/langchain-ai/langchain/blob/master/libs/langchain_v1/langchain/agents/factory.py#L1591). It uses the `_make_tools_to_model_edge` function, which typically routes back to the model to continue the loop.


```
graph.add_conditional_edges(
    “tools”,
    _make_tools_to_model_edge(...),
    {”model”: “model”, “end”: END},
)

def _make_tools_to_model_edge(...) -> Callable:
    def tools_to_model(state: dict) -> str:
        # ... logic to check for tools with return_direct=True ...
        if should_end:
            return “end”
        # Otherwise, always loop back to the model for the next thought phase
        return “model”
    return tools_to_model
```

The logic for stopping the agent resides in the `_make_model_to_tools_edge` function. The agent stops when one of two conditions is met:

1. The model’s last message contains no `tool_calls`. This is the classic ReAct exit condition, meaning the agent believes it has the final answer.

2. A `structured_response` has been generated and added to the state.


If neither of these conditions is met and there are pending tool calls, the loop continues. This simple but powerful logic, encoded in the graph’s edges, orchestrates the entire agentic process.

## How Do Structured Outputs Work with AI Agents?

A key feature of production-ready agents is their ability to return structured, validated data. LangChain’s `create_agent` handles this through the `response_format` parameter.

The most important design choice is that structured outputs are generated **only at the last step**. The presence of a `structured_response` in the state is an exit condition for the loop. This ensures the agent has the flexibility to call various tools during its reasoning process and only enforces the final schema when it is ready to deliver the answer [\[8\]](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/).

LangChain offers two main strategies for this:

- **ToolStrategy**: This is what our agent uses. It treats the Pydantic schema as a special tool. The `create_agent` function converts `DeepResearchResult` into a tool schema and adds it to the list of available tools. When the agent has gathered all necessary information, it “calls” this special tool, providing the final data as arguments. The framework then parses these arguments into a `DeepResearchResult` object and places it in the `structured_response` field of the state, which triggers the loop to end.

- **ProviderStrategy**: This strategy uses the model provider’s native support for structured outputs (like OpenAI’s JSON mode). Instead of creating an artificial tool, it instructs the model directly to generate a JSON object matching the schema. This can be more reliable but is only supported by certain models.


The `ToolStrategy` is a clever and flexible approach that works with any tool-calling model, making it a robust choice for ensuring reliable outputs.

## Successful Example

Let’s trace a successful run for the query: _“Research cognitive behavioral therapy on Wikipedia.”_

1. **Step 1: MODEL (Thought)** The agent receives the task and decides it needs to search Wikipedia. It generates a tool call for `fetch_wikipedia_content` with the query “cognitive behavioral therapy”.

2. **Step 2: TOOLS (Action)** The `ToolNode` executes the `fetch_wikipedia_content` tool. The tool returns the content of the Wikipedia page, including the title and full article text.

3. **Step 3: MODEL (Observation + Thought)** The agent sees the Wikipedia content as an observation. It decides to create a summary of the content and generates a tool call for `create_summary` with the article text and a focus on “cognitive behavioral therapy”.

4. **Step 4: TOOLS (Action)** The `ToolNode` executes the `create_summary` tool, which processes the Wikipedia content and returns a concise summary of cognitive behavioral therapy.

5. **Step 5: MODEL (Observation + Thought)** The agent now has enough information to create the final report. It generates a tool call for the special `DeepResearchResult` tool, populating its arguments with the title, the summary from the previous step, tags, and the paragraph count.

6. **Step 6: Exit** The framework intercepts the `DeepResearchResult` tool call, parses the arguments into the Pydantic model, and adds it to the `structured_response` field in the state. The conditional edge sees this field and routes to `END`. The loop terminates.


The agent successfully completed the task because the tools returned valid data, the model could reason over the observations, and the final structured output passed validation.

Here is the same example, monitored in [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul):

## Unsuccessful Example

Now, let’s see what happens with a query that is designed to fail: _“Research Paul Iusztin on Wikipedia.”_

1. **Step 1: MODEL (Thought)** The agent decides to search Wikipedia and generates a tool call for `fetch_wikipedia_content` with the query “Paul Iusztin”.

2. **Step 2: TOOLS (Action)** The `ToolNode` executes the tool, which returns the string: `“No Wikipedia articles found for query: Paul Iusztin”`.

3. **Step 3: MODEL (Observation + Thought)** The agent observes the “not found” message. It now has a choice. It could try another tool, rephrase the query, or admit it cannot find the answer. In this case, it correctly concludes it cannot fulfill the request and generates a final answer stating that no information was found.


This highlights potential failure modes. The agent might hallucinate an answer, or it could get stuck in an infinite loop of retrying the same failed search. A production-ready implementation would include a maximum iteration limit and clear instructions in the system prompt on how to handle tool failures gracefully.

Here is the same example, monitored in [Opik](https://www.comet.com/site/?utm_source=newsletter&utm_medium=partner&utm_campaign=paul):

## Conclusion

By diving into the source code of LangChain and LangGraph, we have uncovered the elegant engineering behind a production-ready ReAct agent. We have seen how a stateful graph with just two primary nodes and a few conditional edges can implement the full Thought-Action-Observation loop. This exploration gives us more than just theoretical knowledge, it provides a concrete mental model for how these systems work.

Even if you choose not to use a framework like LangGraph in production, understanding how to built your own solution from scratch is one of the core skills you should master as an AI Engineer.

_Remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer._

**Here’s our roadmap:**

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. _**ReAct Agents From Scratch** ← You just finished this one._

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work) _← Move to this one_

9. [Multimodal Data](https://www.decodingai.com/p/stop-converting-documents-to-text)


See you next week.

[Paul Iusztin](https://x.com/pauliusztin_)

* * *

## References

1. (n.d.). _ReAct agent from scratch with Gemini 2.5 and LangGraph_. Google AI for Developers. [https://ai.google.dev/gemini-api/docs/langgraph-example](https://ai.google.dev/gemini-api/docs/langgraph-example)

2. (n.d.). _Agents_. LangChain. [https://docs.langchain.com/oss/python/langchain/agents](https://docs.langchain.com/oss/python/langchain/agents)

3. Neradot. (2024, February 19). _Building a Python ReAct Agent Class: A Step-by-Step Guide_. Neradot. [https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide](https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide)

4. Technofile. (2024, May 22). _How to Build a ReAct AI Agent with Python from Scratch_. Technofile. [how-to-build-a-react-ai-agent-with](https://technofile.substack.com/p/how-to-build-a-react-ai-agent-with)


1. Roelants, P. (2023, April 16). _ReAct: A simple agent for conversational Python_. Peter Roelants. [https://peterroelants.github.io/posts/react-repl-agent/](https://peterroelants.github.io/posts/react-repl-agent/)

2. Capabl. (2024, March 11). _Agentic AI Design Patterns: ReAct, ReWOO, CodeAct, and Beyond_. Capabl. [https://capabl.in/blog/agentic-ai-design-patterns-react-rewoo-codeact-and-beyond](https://capabl.in/blog/agentic-ai-design-patterns-react-rewoo-codeact-and-beyond)

3. Spark Co. (2024, May 28). _Mastering Loop-Based Agent Patterns in AI Systems_. Spark Co. [https://sparkco.ai/blog/mastering-loop-based-agent-patterns-in-ai-systems](https://sparkco.ai/blog/mastering-loop-based-agent-patterns-in-ai-systems)

4. (n.d.). _Agents_. LangChain. [https://docs.langchain.com/oss/python/langchain/agents](https://docs.langchain.com/oss/python/langchain/agents)

5. Daily Dose of DS. (2024, June 10). _AI Agents Crash Course - Part 10: ReAct Framework with Implementation_. Daily Dose of DS. [https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/](https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/)

6. Brownlee, J. (2024, July 1). _Building ReAct Agents with LangGraph: A Beginner’s Guide_. Machine Learning Mastery. [https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/](https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/)

7. LateNode. (2024, August 15). _LangChain ReAct Agent: Complete Implementation Guide with Working Examples (2025)_. LateNode. [https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025](https://latenode.com/blog/ai-frameworks-technical-infrastructure/langchain-setup-tools-agents-memory/langchain-react-agent-complete-implementation-guide-working-examples-2025)

8. (n.d.). _ReAct agent with structured output_. LangChain. [https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-a-python-react-agent-class-a-step-by-step-guide-nov.md">
<details>
<summary>Building a Python React Agent Class: A Step-by-Step Guide</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.neradot.com/post/building-a-python-react-agent-class-a-step-by-step-guide>

# Building a Python React Agent Class: A Step-by-Step Guide

Roy Pasternak | CTO at Neradot

https://cdn.prod.website-files.com/645a411baa30ca12b39891d5/672a29a3b6cedc447bd49ba2_Building-React-Agent.png

In this blog post, we’ll walk through the creation of a React agent class in Python. After going over our previous post ( [ReAct: Merging Reasoning and Action to Elevate AI Task Solving](https://www.neradot.com/post/react)) you should already be familiar with the `React` flow. Here is a flow diagram to quickly recall how React handles the reason-action loop:

Now, let’s jump to the coding part. We’ll start with a minimal setup and gradually add functionality until we have a fully functional agent. Each step is highlighted with code snippets that focus on the differences from the previous step, providing a clear understanding of the incremental changes.

> **NOTE:** If you’d like to see the full code directly, you can check out the complete implementation on [**react-simple**](https://github.com/neradot/react-simple)

https://cdn.prod.website-files.com/645a411baa30ca12b39891d5/672a407dd7dd024a21617304_672a406a80c9aabdaddd767b_Screenshot%25202024-11-05%2520at%252017.56.50.png

React flow diagram of reasoning and action

##### Step 0: Define the class interface

Here is the `React` class structure we are going to create together:

```python
class React:
    def __init__(self, tools: list[callable], max_steps: int = 10, verbose: bool = False):
        # Initializes tools, settings, and internal state variables, such as `max_steps` and `verbose`.
        ...

    def reason(self) -> tuple[str, str, str, bool]:
        # Generates reasoning steps and determines the next action.
        ...

    def act(self, action: str, action_input: dict | str) -> str:
        # Executes actions by calling tool functions based on the current reasoning.
        ...

    def start(self, question: str):
        # Begins a new session with a given question.
        ...

    def next(self):
        # Advances the agent by processing reasoning, acting, and handling completion.
        ...

    def finish(self):
        # Ends the session, storing the final answer and completion status.
        ...

    def add_step(self, step: dict):
        # Logs each step of the agent’s process, such as thoughts, actions, and observations.
        ...

    def build_messages(self) -> list[dict]:
        # Constructs prompt messages for the reasoning process, integrating available tools and instructions.
        ...
```

- **`__init__`**`:` Initializes the agent with tools, step limit (`max_steps`), and verbosity option (`verbose`).
- **`reason`**`:` Produces reasoning steps, decides the next action, and determines if the agent should continue.
- **`act`**`:` Executes a specified action using a tool with provided inputs, returning the result (observation).
- **`start`**: Begins a session by setting up the agent with a question.
- **`next`**`:` Advances the agent by running one reasoning/action cycle and checking for completion.
- **`finish`**`:` Ends the session, saving the final answer and marking it complete.
- **`add_step`**: Logs each step of the process, including thoughts, actions, and observations.
- **`build_messages`**: Creates prompt messages that integrate tools and instructions for reasoning.

##### Step 1: Minimal Setup

```python
import time

# Minimal setup with initialization and start method
class React:
    def __init__(self, verbose: bool = False):
        self.start_time: float | None = None
        self.is_started: bool = False
        self.intermediate_steps: list[dict] = []
        self.verbose = verbose

    def add_intermediate_step(self, intermediate_step: dict):
        self.intermediate_steps.append(intermediate_step)
        if self.verbose:
            print(intermediate_step)

    def start(self, question: str):
        if self.verbose:
          print(f"Starting agent with:")
        self.start_time = time.time()
        self.is_started = True
        self.intermediate_steps = []
        self.add_intermediate_step({"question": question})

# Testing the initial start function
react_agent = React(verbose=True)
react_agent.start("What is 2 + 2?")
```

In this initial step, we set up the basic structure for the React class. This minimal version includes an initialization method, where we define the attributes to track the agent’s state, and a simple start method to begin an interaction. Here, we also introduce the intermediate\_steps list, which will store each phase of the agent’s process, such as questions, thoughts, actions, and observations. This list acts as a log for the interaction, making it possible for the agent to reference prior steps and maintain a coherent flow of actions and reasoning as we expand its functionality.

###### **Output:**

```python
Starting agent with:
{'question': 'What is 2 + 2?'}
```

At this point, we’ve created a basic class that can start an interaction by saving the question as an intermediate step.

##### Step 2: Adding Reasoning with reason() and build\_messages() Methods

```python
import json
from utils import parse_json, get_completion
from prompts import (
    REACT_TOOLS_DESCRIPTION,
    REACT_VALID_ACTIONS,
    REACT_JSON_FORMAT,
    REACT_PROCESS_FORMAT,
    REACT_INTERMEDIATE_STEPS,
    REACT_ADDITIONAL_INSTRUCTIONS
)

class React:

	...

	# Adding the reasoning logic
	def reason(self) -> tuple[str, str, str, bool]:
	    messages = self.build_messages()
	    completion_response = get_completion(messages, model="gpt-4o", temperature=0, max_tokens=256, stop=["</reasoning>"])
	    completion = completion_response.choices[0].message.content
	    parsed_completion = parse_json(completion)
	    thought = parsed_completion["thought"]
	    action = parsed_completion["action"]
	    action_input = parsed_completion["action_input"]
	    is_final_answer = action == "Final Answer"
	    return thought, action, action_input, is_final_answer

	# Building the prompt messages from templates
	def build_messages(self) -> list[dict]:
      question = self.intermediate_steps[0]["question"]
      intermediate_steps=json.dumps(self.intermediate_steps[1:])
      system_prompt_message = \
              REACT_TOOLS_DESCRIPTION.format(tools_description="") + \
              REACT_VALID_ACTIONS.format(tools_names="") + \
              REACT_JSON_FORMAT + \
              REACT_PROCESS_FORMAT + \
              REACT_ADDITIONAL_INSTRUCTIONS + \
              REACT_INTERMEDIATE_STEPS.format(question=question, intermediate_steps=intermediate_steps)
        messages = [{ "role": "system", "content": system_prompt_message }]
        return messages

```

##### Step 3: Driving Agent Progress with next() method

```python
class React:

	...

  @property
  def steps_count(self):
      return int(len(self.intermediate_steps) - 1 )

  def next(self):
      if not self.is_started:
          raise ValueError("React was not started")

      if self.verbose:
          print(f"Step {self.steps_count}")
      thought, action, action_input, is_final_answer = self.reason()
      self.add_intermediate_step({"thought": thought, "action": action, "action_input": action_input})

react_agent = React(verbose=True)
react_agent.start("What is 2 + 2?")
react_agent.next()
```

With the reasoning structure in place, we now add the `next` method to control the agent's progression through steps. The `next` method initiates a reasoning process by calling `reason`, captures the generated `thought`, `action`, and `action_input`, and adds them as a new entry in `intermediate_steps`. we also introduce a `steps_count` property. This property calculates the number of reasoning of `intermediate_steps` (excluding the initial question).

###### **Output:**

```python
Starting agent with:
{'question': 'What is 2 + 2?'}
Step 0
{'thought': 'The question asks for the sum of 2 + 2, which is a basic arithmetic operation that I can solve without any tools.', 'action': 'Final Answer', 'action_input': 4}
```

Here, the agent now has the capability to reason, generating an action and thought about the question. But, we are still missing the tool usage!

##### Step 4: Introducing Tools

```python
class React:
	...

# Adding tools functionality
	def __init__(self, tools: list[callable], verbose: bool = False):
			...
	    self.tools_dict: dict[str, callable] = {tool.__name__: tool for tool in tools}
	    self.tools_description: str = "\n".join([f"{tool_name}: {tool.__doc__}" for tool_name, tool in self.tools_dict.items()])
	    self.tools_names: list[str] = list(self.tools_dict.keys())
      if self.verbose:
          print("Initialized agent with tools:")
          print(f"{self.tools_description}")
          print()

def build_messages(self) -> list[dict]:
        ...
        system_prompt_message = \
                REACT_TOOLS_DESCRIPTION.format(tools_description=self.tools_description) + \
                REACT_VALID_ACTIONS.format(tools_names=self.tools_names) + \
        ...
def calculator(expression: str) -> float:
  """Evaluates a mathematical expression and returns the result"""
  return eval(expression)
react_agent = React(tools=[calculator], verbose=True)
react_agent.start("What is 2 + 2?")
react_agent.next()
react_agent.next()
```

In this step, we enhance the agent's abilities by adding a tool system. Tools are specific functions that the agent can call to perform certain actions, such as calculations or data retrieval. Each tool is passed to the `React` class upon initialization, allowing the agent to select and use them as needed.

Inside the `__init__` method, we create a dictionary, `tools_dict`, that maps each tool’s name to its function. We also generate `tools_description`, a formatted string that provides a description of each tool’s purpose (using the tool’s docstring), and `tools_names`, a list of tool names.

Additionally, we update the `build_messages` method to integrate `tools_description` and `tools_names` directly into the system prompt, allowing the agent to reference the tools available during its reasoning process.

##### **Expected Output:**

```python
Initialized agent with tools:
calculator: Evaluates a mathematical expression and returns the result

Starting agent with:
{'question': 'What is 2 + 2?'}
Step 0
{'thought': 'To solve the problem of finding what 2 + 2 equals, I should perform a simple arithmetic addition calculation.', 'action': 'calculator', 'action_input': '2 + 2'}
Step 1
{'thought': 'I should calculate the sum of 2 and 2 to find the answer.', 'action': 'calculator', 'action_input': '2 + 2'}
```

The agent now has a calculator tool it can reference to answer questions involving calculations.

However, while the agent can select the tool, it doesn’t yet actually call the tool function to produce results. This is why the output shows no progress based on the action taken.

##### Step 4: Taking Actions and Observations

```python
class React:
		...
    @property
    def steps_count(self):
+        return int((len(self.intermediate_steps) - 1 ) / 2)

# Adding action and observation handling
def act(self, action: str, action_input: dict | str) -> str:
    tool_func = self.tools_dict[action]
    if isinstance(action_input, dict):
        tool_result = tool_func(**action_input)
    else:
        tool_result = tool_func(action_input)
    return tool_result

# Updating `next` method to include observation step
def next(self):
    ...
+    thought, action, action_input, is_final_answer = self.reason()
+    self.add_intermediate_step({"thought": thought, "action": action, "action_input": action_input})
+    observation = self.act(action, action_input)
+    self.add_intermediate_step({"observation": observation})

react_agent = React(tools=[calculator], verbose=True)
react_agent.start("What is 2 + 2?")
react_agent.next()
react_agent.next()
```

Now, we add the `act` method, allowing the agent to execute actions based on parsed inputs from the `reason` method. This `act` method calls a relevant tool function and records the observation for each action taken.

##### **Expected Output:**

```python
Initialized agent with tools:
calculator: Evaluates a mathematical expression and returns the result

Starting agent with:
{'question': 'What is 2 + 2?'}
Step 0
{'thought': 'To solve the problem, I need to add the numbers 2 and 2.', 'action': 'calculator', 'action_input': '2 + 2'}
{'observation': 4}
Step 1
{'thought': 'The calculation has been performed and the result is the addition of the two numbers.', 'action': 'Final Answer', 'action_input': 4}

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
...
KeyError: 'Final Answer'
```

The agent now has an `act` method to execute tool functions, and an observation step that records the results of each action. This allows the agent to see progress after calling a tool.

However, because the `act` method expects a tool name, the agent raises an error if the action is `"Final Answer"` rather than a tool. In the next step, we’ll handle this case to allow the agent to complete its reasoning when a final answer is reached.

##### Step 5: Adding a Finish Step

```python
class React:
	...
	def __init__(self, tools: list[callable], verbose: bool = False):
			...
			self.not_finished: bool = True
	# Adding the finish method
  def finish(self):
      self.not_finished = False
      self.add_intermediate_step({"answer": self.last["action_input"]})

	# Updating `next` method to finalize when the final answer is reached
  def next(self):
    ...
    thought, action, action_input, is_final_answer = self.reason()
    self.add_intermediate_step({"thought": thought, "action": action, "action_input": action_input})
    if is_final_answer:
        self.finish()
    else:
        observation = self.act(action, action_input)
        self.add_intermediate_step({"observation": observation})

react_agent = React(tools=[calculator], verbose=True)
react_agent.start("What is 2 + 2?")
while react_agent.not_finished:
    react_agent.next()
```

In this step, we add the `finish` method to mark the agent's session as complete. We add  additional attribute: `not_finished`, which becomes `False` when the agent has completed its task.

Additionally, we update the `next` method to handle the `"Final Answer"` action gracefully. If `reason` returns `"Final Answer"`, `next` now calls `finish` rather than attempting to execute a tool, resolving the error from the previous step where the agent tried to run `"Final Answer"` as a tool name.

###### **Output:**

```python
Initialized agent with tools:
calculator: Evaluates a mathematical expression and returns the result

Starting agent with:
{'question': 'What is 2 + 2?'}
Step 0
{'thought': 'I can calculate the sum of 2 + 2 using a basic mathematical operation.', 'action': 'calculator', 'action_input': '2 + 2'}
{'observation': 4}
Step 1
{'thought': 'The sum of 2 + 2 is calculated using a simple arithmetic operation, and the result was confirmed as 4.', 'action': 'Final Answer', 'action_input': 4}
{'answer': 4}
```

With the addition of the finish method and the updated next method, the agent now recognizes when it has reached a final answer and stops further actions, fully resolving the error from the previous step.

##### Final Touch: Adding Max Steps, Finish Reason, Duration, and Token Usage

```python
class React:
    def __init__(self, tools: list[callable], max_steps: int = 10, verbose: bool = False):
+       self.max_steps = max_steps
+       self.finish_reason: Literal["final answer", "max_steps_reached"] | None = None
+       self.completion_records: list[openai.types.completion.Completion] = []

    @property
+   def is_max_steps_reached(self):
+       return self.steps_count >= self.max_steps

    @property
+   def duration(self):
+       if not self.start_time or not self.end_time:
+           return None
+       return round((self.end_time - self.start_time)*1000, 3)

    @property
+   def token_usage(self):
+       usage = {'prompt_tokens': 0, 'completion_tokens': 0, 'total_tokens': 0}
+       for res in self.completion_records:
+           usage['prompt_tokens'] += res.usage.prompt_tokens
+           usage['completion_tokens'] += res.usage.completion_tokens
+           usage['total_tokens'] += res.usage.total_tokens
+       return usage

    def next(self):
        ...
        else:
            observation = self.act(action, action_input)
            self.add_intermediate_step({"observation": observation})
+           if self.is_max_steps_reached:
+               self.finish()

    def reason(self) -> tuple[str, str, str, bool]:
        ...
+       self.completion_records.append(completion_response)
        ...

    def finish(self):
        self.not_finished = False
        if not self.is_max_steps_reached:
            self.finish_reason = "final answer"
            self.add_intermediate_step({"answer": self.last["action_input"]})
        else:
            self.finish_reason = "max_steps_reached"
        self.end_time = time.time()

react_agent = React(tools=[calculator], verbose=True)
react_agent.start("What is 2 + 2?")
while react_agent.not_finished:
    react_agent.next()
```

In this final step, we add few features to enhance the agent's performance and monitoring:

1.  **Max Steps**: The `max_steps` parameter limits the number of reasoning steps the agent can take. If this limit is reached, `finish` is called automatically to prevent looping.
2.  **Finish Reason**: The `finish_reason` attribute records why the agent stopped: either `"final answer"` when a solution is reached or `"max_steps_reached"` if the step limit is hit.
3.  **Duration**: The `duration` property calculates the total runtime from start to finish in milliseconds, giving insight into performance.
4.  **Token Usage**: The `token_usage` property sums up tokens used in all completions, tracking prompt and completion tokens for resource monitoring.

With these additions, the agent is now fully functional, self-limiting, and capable of providing detailed usage insights.

###### **Output:**

```python
Initialized agent with tools:
calculator: Evaluates a mathematical expression and returns the result

Starting agent with:
{'question': 'What is 2 + 2?'}
Step 0
{'thought': 'To find the sum of 2 + 2, I will use the calculator tool to perform the arithmetic operation.', 'action': 'calculator', 'action_input': '2 + 2'}
{'observation': 4}
Step 1
{'thought': 'I have used the calculator tool to perform the addition of 2 + 2 and obtained the result.', 'action': 'Final Answer', 'action_input': 4}
{'answer': 4}
Finish reason: final answer
Duration: 2686.926 ms
Token Usage: {'prompt_tokens': 652, 'completion_tokens': 100, 'total_tokens': 752}
```

###### Next

In the next post, we’ll dive into practical methods for evaluating agent performance, focusing on metrics that are particularly relevant for the `React` agent, such as correctness, efficiency, and response time. We’ll explore techniques for assessing the accuracy of the agent’s reasoning and action choices, testing for correctness in both intermediate steps and final answers.

###### Full Prompt

```python
The available tools are:
{tools_description}

Use the tool name as the "action" value in the JSON response.

Valid actions are:
- "Final Answer"
- Any of {tools_names}

Respond in the following $JSON_BLOB format:
<reasoning>
{
        "thought": // Explain your reasoning for the chosen action, consider previous and subsequent steps
        "action": // The name of the tool to use
        "action_input": // The input required for the tool
}
</reasoning>

After you select an action, you will receive an observation. Then you can select another action or provide a final answer.
The pattern looks like this:

<reasoning>
$JSON_BLOB
</reasoning>
<observation>
{"observation": // action result}
</observation>
<reasoning>
$JSON_BLOB
</reasoning>
<observation>
{"observation": // action result}
</observation>

... (repeated until you have enough observations to answer the question)

<reasoning>
{
        "thought": // Explain why you have enough information to provide a final answer,
        "action": "Final Answer",
        "action_input": // Your final answer to the question
}
</reasoning>

Instructions:
1. Do not use comments in your JSON answer;
2. ALWAYS respond with a valid json blob of a single action;
3. ALWAYS think before choosing an action;
4. Respond in a JSON blob no matter what.

Here is the user question:
"{question}"

Here are the intermediate steps so far:
{intermediate_steps}
```

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="building-react-agents-with-langgraph-a-beginner-s-guide-mach.md">
<details>
<summary>Building ReAct Agents with LangGraph: A Beginner's Guide - MachineLearningMastery.com</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://machinelearningmastery.com/building-react-agents-with-langgraph-a-beginners-guide/>

# Building ReAct Agents with LangGraph: A Beginner's Guide - MachineLearningMastery.com

In this article, you will learn how the [ReAct (Reasoning + Acting) pattern](https://machinelearningmastery.com/7-must-know-agentic-ai-design-patterns/) works and how to implement it with LangGraph — first with a simple, hardcoded loop and then with an LLM-driven agent.

Topics we will cover include:

- The ReAct cycle (Reason → Act → Observe) and why it’s useful for agents.
- How to model agent workflows as graphs with LangGraph.
- Building a hardcoded ReAct loop, then upgrading it to an LLM-powered version.

Let’s explore these techniques.

https://machinelearningmastery.com/wp-content/uploads/2025/11/mlm-chugani-building-react-agents-langgraph-beginners-guide-feature-1024x683.png

Building ReAct Agents with LangGraph: A Beginner’s Guide

Image by Author

## What is the ReAct Pattern?

[ReAct (Reasoning + Acting)](https://arxiv.org/abs/2210.03629) is a common pattern for building [AI agents](https://machinelearningmastery.com/the-machine-learning-practitioners-guide-to-agentic-ai-systems/) that think through problems and take actions to solve them. The pattern follows a simple cycle:

1.  **Reasoning**: The agent thinks about what it needs to do next.
2.  **Acting**: The agent takes an action (like searching for information).
3.  **Observing**: The agent examines the results of its action.

This cycle repeats until the agent has gathered enough information to answer the user’s question.

## Why LangGraph?

**[LangGraph](https://www.langchain.com/langgraph)** is a framework built on top of **[LangChain](https://www.langchain.com/)** that lets you define agent workflows as graphs. A graph (in this context) is a data structure consisting of nodes (steps in your process) connected by edges (the paths between steps). Each node in the graph represents a step in your agent’s process, and edges define how information flows between steps. This structure allows for complex flows like loops and conditional branching. For example, your agent can cycle between reasoning and action nodes until it gathers enough information. This makes complex agent behavior easy to understand and maintain.

## Tutorial Structure

We’ll build two versions of a ReAct agent:

1.  **Part 1**: A simple hardcoded agent to understand the mechanics.
2.  **Part 2**: An LLM-powered agent that makes dynamic decisions.

## Part 1: Understanding ReAct with a Simple Example

First, we’ll create a basic ReAct agent with hardcoded logic. This helps you understand how the ReAct loop works without the complexity of LLM integration.

### Setting Up the State

Every LangGraph agent needs a **state** object that flows through the graph nodes. This state serves as shared memory that accumulates information. Nodes read the current state and add their contributions before passing it along.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9 | from langgraph.graph import StateGraph,END<br>from typing import TypedDict,Annotated<br>import operator<br>\# Define the state that flows through our graph<br>classAgentState(TypedDict):<br>messages:Annotated\[list,operator.add\]<br>next\_action:str<br>iterations:int |

**Key Components:**

- `StateGraph`: The main class from LangGraph that defines our agent’s workflow.
- `AgentState`: A TypedDict that defines what information our agent tracks.

  - `messages`: Uses `operator.add` to accumulate all thoughts, actions, and observations.
  - `next_action`: Tells the graph which node to execute next.
  - `iterations`: Counts how many reasoning cycles we’ve completed.

### Creating a Mock Tool

In a real ReAct agent, tools are functions that perform actions in the world — like searching the web, querying databases, or calling APIs. For this example, we’ll use a simple mock search tool.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | \# Simple mock search tool<br>def search\_tool(query:str)->str:<br>\# Simulate a search - in real usage, this would call an API<br>responses={<br>"weather tokyo":"Tokyo weather: 18°C, partly cloudy",<br>"population japan":"Japan population: approximately 125 million",<br>}<br>returnresponses.get(query.lower(),f"No results found for: {query}") |

This function simulates a search engine with hardcoded responses. In production, this would call a real search API like Google, Bing, or a custom knowledge base.

### The Reasoning Node — The “Brain” of ReAct

This is where the agent **thinks** about what to do next. In this simple version, we’re using hardcoded logic, but you’ll see how this becomes dynamic with an LLM in Part 2.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | \# Reasoning node - decides what to do<br>def reasoning\_node(state:AgentState):<br>messages=state\["messages"\]<br>iterations=state.get("iterations",0)<br>\# Simple logic: first search weather, then population, then finish<br>ifiterations==0:<br>return{"messages":\["Thought: I need to check Tokyo weather"\],<br>"next\_action":"action","iterations":iterations+1}<br>elif iterations==1:<br>return{"messages":\["Thought: Now I need Japan's population"\],<br>"next\_action":"action","iterations":iterations+1}<br>else:<br>return{"messages":\["Thought: I have enough info to answer"\],<br>"next\_action":"end","iterations":iterations+1} |

**How it works:**

The reasoning node examines the current state and decides:

- Should we gather more information? (return `"action"`)
- Do we have enough to answer? (return `"end"`)

Notice how each return value updates the state:

1.  Adds a “Thought” message explaining the decision.
2.  Sets `next_action` to route to the next node.
3.  Increments the iteration counter.

This mimics how a human would approach a research task: “First I need weather info, then population data, then I can answer.”

### The Action Node — Taking Action

Once the reasoning node decides to act, this node **executes** the chosen action and **observes** the results.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15 | \# Action node - executes the tool<br>def action\_node(state:AgentState):<br>iterations=state\["iterations"\]<br>\# Choose query based on iteration<br>query="weather tokyo"ifiterations==1else"population japan"<br>result=search\_tool(query)<br>return{"messages":\[f"Action: Searched for '{query}'",<br>f"Observation: {result}"\],<br>"next\_action":"reasoning"}<br>\# Router - decides next step<br>def route(state:AgentState):<br>returnstate\["next\_action"\] |

**The ReAct Cycle in Action:**

1.  **Action**: Calls the search\_tool with a query.
2.  **Observation**: Records what the tool returned.
3.  **Routing**: Sets next\_action back to “reasoning” to continue the loop.

The router function is a simple helper that reads the `next_action` value and tells LangGraph where to go next.

### Building and Executing the Graph

Now we assemble all the pieces into a LangGraph workflow. This is where the magic happens!

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24 | \# Build the graph<br>workflow=StateGraph(AgentState)<br>workflow.add\_node("reasoning",reasoning\_node)<br>workflow.add\_node("action",action\_node)<br>\# Define edges<br>workflow.set\_entry\_point("reasoning")<br>workflow.add\_conditional\_edges("reasoning",route,{<br>"action":"action",<br>"end":END<br>})<br>workflow.add\_edge("action","reasoning")<br>\# Compile and run<br>app=workflow.compile()<br>\# Execute<br>result=app.invoke({"messages":\["User: Tell me about Tokyo and Japan"\],<br>"iterations":0,"next\_action":""})<br>\# Print the conversation flow<br>print("\\n=== ReAct Loop Output ===")<br>formsg inresult\["messages"\]:<br>print(msg) |

**Understanding the Graph Structure:**

1.  **Add Nodes**: We register our reasoning and action functions as nodes.
2.  **Set Entry Point**: The graph always starts at the reasoning node.
3.  **Add Conditional Edges**: Based on the reasoning node’s decision:

    - If `next_action == "action"` → go to the action node.
    - If `next_action == "end"` → stop execution.
4.  **Add Fixed Edge**: After action completes, always return to reasoning.

The `app.invoke()` call kicks off this entire process.

Output:

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | ===ReAct Loop Output===<br>User:Tell me about Tokyo andJapan<br>Thought:Ineed tocheck Tokyo weather<br>Action:search('weather tokyo')<br>Observation:Tokyo weather:18°C,partly cloudy<br>Thought:NowIneed Japan's population<br>Action: search('population japan')<br>Observation:Japan population:approximately125million<br>Thought:Ihave enough info toanswer |

Now let’s see how LLM-powered reasoning makes this pattern truly dynamic.

## Part 2: LLM-Powered ReAct Agent

Now that you understand the mechanics, let’s build a **real** ReAct agent that uses an LLM to make intelligent decisions.

### Why Use an LLM?

The hardcoded version works, but it’s inflexible — it can only handle the exact scenario we programmed. An LLM-powered agent can:

- Understand different types of questions.
- Decide dynamically what information to gather.
- Adapt its reasoning based on what it learns.

### Key Difference

Instead of hardcoded if/else logic, we’ll **prompt the LLM** to decide what to do next. The LLM becomes the “reasoning engine” of our agent.

### Setting Up the LLM Environment

We’ll use OpenAI’s GPT-4o as our reasoning engine, but you could use any LLM (Anthropic, open-source models, etc.).

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12 | from langgraph.graph import StateGraph,END<br>from typing import TypedDict,Annotated<br>import operator<br>import os<br>from openai import OpenAI<br>client=OpenAI(api\_key=os.environ.get("OPENAI\_API\_KEY"))<br>classAgentStateLLM(TypedDict):<br>messages:Annotated\[list,operator.add\]<br>next\_action:str<br>iteration\_count:int |

**New State Definition:**

`AgentStateLLM` is similar to `AgentState`, but we’ve renamed it to distinguish between the two examples. The structure is identical — we still track messages, actions, and iterations.

### The LLM Tool — Gathering Information

Instead of a mock search, we’ll let the LLM answer queries using its own knowledge. This demonstrates how you can turn an LLM into a tool!

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8 | def llm\_tool(query:str)->str:<br>"""Let the LLM answer the query directly using its knowledge"""<br>response=client.chat.completions.create(<br>model="gpt-4o",<br>max\_tokens=150,<br>messages=\[{"role":"user","content":f"Answer this query briefly: {query}"}\]<br>)<br>returnresponse.choices\[0\].message.content.strip() |

This function makes a simple API call to GPT-4 with the query. The LLM responds with factual information, which our agent will use in its reasoning.

**Note**: In production, you might combine this with web search, databases, or other tools for more accurate, up-to-date information.

### LLM-Powered Reasoning — The Core Innovation

This is where ReAct truly shines. Instead of hardcoded logic, we **prompt the LLM** to decide what information to gather next.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29 | def reasoning\_node\_llm(state:AgentStateLLM):<br>iteration\_count=state.get("iteration\_count",0)<br>ifiteration\_count>=3:<br>return{"messages":\["Thought: I have gathered enough information"\],<br>"next\_action":"end","iteration\_count":iteration\_count}<br>history="\\n".join(state\["messages"\])<br>prompt=f"""You are an AI agent answering: "Tell me about Tokyo andJapan"<br>Conversation so far:<br>{history}<br>Queries completed: {iteration\_count}/3<br>You MUST make exactly 3 queries to gather information. <br>Respond ONLY with: QUERY: <your specific question><br>Do NOT be conversational. Do NOT thank the user. ONLY output: QUERY: <question>"""<br>decision=client.chat.completions.create(<br>model="gpt-4o",max\_tokens=100,<br>messages=\[{"role":"user","content":prompt}\]<br>).choices\[0\].message.content.strip()<br>ifdecision.startswith("QUERY:"):<br>return{"messages":\[f"Thought: {decision}"\],"next\_action":"action",<br>"iteration\_count":iteration\_count}<br>return{"messages":\[f"Thought: {decision}"\],"next\_action":"end",<br>"iteration\_count":iteration\_count} |

**How This Works:**

1.  **Context Building**: We include the conversation history so the LLM knows what’s already been gathered.
2.  **Structured Prompting**: We give clear instructions to output in a specific format (`QUERY: <question>`).
3.  **Iteration Control**: We enforce a maximum of 3 queries to prevent infinite loops.
4.  **Decision Parsing**: We check if the LLM wants to take action or finish.

**The Prompt Strategy:**

The prompt tells the LLM:

- What question it’s trying to answer
- What information has been gathered so far
- How many queries it’s allowed to make
- Exactly how to format its response
- To not be conversational

LLMs are trained to be helpful and chatty. For agent workflows, we need concise, structured outputs. This directive keeps responses focused on the task.

### Executing the Action

The action node works similarly to the hardcoded version, but now it processes the LLM’s dynamically generated query.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7 | def action\_node\_llm(state:AgentStateLLM):<br>last\_thought=state\["messages"\]\[-1\]<br>query=last\_thought.replace("Thought: QUERY:","").strip()<br>result=llm\_tool(query)<br>return{"messages":\[f"Action: query('{query}')",f"Observation: {result}"\],<br>"next\_action":"reasoning",<br>"iteration\_count":state.get("iteration\_count",0)+1} |

**The Process:**

1.  Extract the query from the LLM’s reasoning (removing the “Thought: QUERY:” prefix).
2.  Execute the query using our llm\_tool.
3.  Record both the action and observation.
4.  Route back to reasoning for the next decision.

Notice how this is more flexible than the hardcoded version — the agent can ask for any information it thinks is relevant!

### Building the LLM-Powered Graph

The graph structure is identical to Part 1, but now the reasoning node uses LLM intelligence instead of hardcoded rules.

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18 | workflow\_llm=StateGraph(AgentStateLLM)<br>workflow\_llm.add\_node("reasoning",reasoning\_node\_llm)<br>workflow\_llm.add\_node("action",action\_node\_llm)<br>workflow\_llm.set\_entry\_point("reasoning")<br>workflow\_llm.add\_conditional\_edges("reasoning",lambdas:s\["next\_action"\],<br>{"action":"action","end":END})<br>workflow\_llm.add\_edge("action","reasoning")<br>app\_llm=workflow\_llm.compile()<br>result\_llm=app\_llm.invoke({<br>"messages":\["User: Tell me about Tokyo and Japan"\],<br>"next\_action":"",<br>"iteration\_count":0<br>})<br>print("\\n=== LLM-Powered ReAct (No Mock Data) ===")<br>formsg inresult\_llm\["messages"\]:<br>print(msg) |

**What’s Different:**

- Same graph topology (reasoning ↔ action with conditional routing).
- Same state management approach.
- **Only the reasoning logic changed** – from if/else to LLM prompting.

This demonstrates the power of LangGraph: you can swap components while keeping the workflow structure intact!

**The Output:**

You’ll see the agent autonomously decide what information to gather. Each iteration shows:

- **Thought**: What the LLM decided to ask about.
- **Action**: The query being executed.
- **Observation**: The information gathered.

Watch how the LLM strategically gathers information to build a complete answer!

| | |
| --- | --- |
| 1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15<br>16<br>17<br>18<br>19<br>20<br>21<br>22<br>23<br>24<br>25<br>26<br>27<br>28<br>29<br>30<br>31<br>32<br>33<br>34<br>35<br>36<br>37<br>38<br>39<br>40<br>41<br>42<br>43<br>44<br>45<br>46<br>47<br>48<br>49 | ===LLM-Powered ReAct(No Mock Data)===<br>User:Tell me about Tokyo andJapan<br>Thought:QUERY:What isthe history andsignificance of Tokyo inJapan?<br>Action:query('What is the history and significance of Tokyo in Japan?')<br>Observation:Tokyo,originally known asEdo,hasarich history andsignificant role inJapan.<br>It began asasmall fishing village until Tokugawa Ieyasu established it asthe center of <br>his shogunate in1603,marking the start of the Edo period.During thistime,Edo flourished <br>asapolitical andcultural hub,becoming one of the world's largest cities by the 18th century.<br>In 1868, after the Meiji Restoration, the emperor moved from Kyoto to Edo, renaming it Tokyo, <br>meaning "Eastern Capital". This transformation marked the beginning of Tokyo'smodernization <br>andrapid development.Over the20thcentury,Tokyo faced challenges,including the Great <br>Kanto Earthquake in1923andheavy bombings<br>Thought:QUERY:What are the major cultural andeconomic contributions of Tokyo toJapan?<br>Action:query('What are the major cultural and economic contributions of Tokyo to Japan?')<br>Observation:Tokyo,asthe capital of Japan,isamajor cultural andeconomic powerhouse.<br>Culturally,Tokyo isahub fortraditional andcontemporary arts,including theater,music,<br>andvisual arts.The city ishome tonumerous museums,galleries,andcultural sites such as<br>the Tokyo National Museum,Senso-ji Temple,andthe Meiji Shrine.It also hosts international <br>events like the Tokyo International Film Festival andvarious fashion weeks,contributing to<br>its reputation asaglobalfashion andcultural center.<br>Economically,Tokyo isone of the world's leading financial centers. It hosts the Tokyo Stock <br>Exchange, one of the largest stock exchanges globally, and is the headquarters for numerous <br>multinational corporations. The city'sadvanced infrastructure andinnovation intechnology <br>andindustry make itafocal<br>Thought:QUERY:What are the key historical andcultural aspects of Japan asawhole?<br>Action:query('What are the key historical and cultural aspects of Japan as a whole?')<br>Observation:Japan boastsarich tapestry of historical andcultural aspects,shaped by centuries <br>of development.Historically,Japan'sculture was influenced by its isolation asan island <br>nation,leading toaunique blend of indigenous practices andforeign influences.Key historical <br>periods include the Jomon andYayoi eras,characterized by early settlement andculture,andthe <br>subsequent periods of imperial rule andsamurai governance,such asthe Heian,Kamakura,andEdo <br>periods.These periods fostered developments like the tea ceremony,calligraphy,andkabuki theater.<br>Culturally,Japan isknown forits Shinto andBuddhist traditions,which coexist seamlessly.<br>Its aesthetic principles emphasize simplicity andnature,reflected intraditional architecture,<br>gardens,andarts such asukiyo-eprints andlater<br>Thought:Ihave gathered enough information |

## Wrapping Up

You’ve now built two ReAct agents with LangGraph — one with hardcoded logic to learn the mechanics, and one powered by an LLM that makes dynamic decisions.

The key insight? LangGraph lets you separate your workflow structure from the intelligence that drives it. The graph topology stayed the same between Part 1 and Part 2, but swapping hardcoded logic for LLM reasoning transformed a rigid script into an adaptive agent.

From here, you can extend these concepts by adding real tools (web search, calculators, databases), implementing tool selection logic, or even [building multi-agent systems](https://machinelearningmastery.com/building-first-multi-agent-system-beginner-guide/) where multiple ReAct agents collaborate.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="implementing-react-agentic-pattern-from-scratch.md">
<details>
<summary>Implementing ReAct Agentic Pattern From Scratch</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.dailydoseofds.com/ai-agents-crash-course-part-10-with-implementation/>

# Implementing ReAct Agentic Pattern From Scratch

## Introduction

Building advanced AI agents has been greatly simplified by high-level frameworks like LangChain and CrewAI.

However, these frameworks often hide the underlying logic that makes an AI agent tick.

More specifically, under the hood, many such frameworks use the ReAct (Reasoning and Acting) pattern to let large language models (LLMs) think through problems and use tools to act on the world​.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2026/01/https-3a-2f-2fsubstack-post-media-s3-amazonaws-com-2fpublic-2fimages-2fd02b2eaa-16c3-4f92-8f97-06329fbcccd4_716x550-6.gif

For example, an agent in CrewAI typically alternates between reasoning about a task and acting (using a tool) to gather information or execute steps, following the ReAct paradigm​.

This approach enhances an LLM agent’s ability to handle complex tasks and decisions by combining chain-of-thought reasoning with external tool use​.

While frameworks like CrewAI implement this logic for you and you should also keep using them in production systems (also because they are built by experts), often times, relying on pre-packaged libraries without understanding their inner workings can lead to confusion​.

You might use an agent framework and wonder how it decides to, say, perform a web search or a calculation as part of answering a question.

An example is shown below where the Agent is going through a series of thought activities before producing a response.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-28.png

In this article, we’ll demystify that process by building a ReAct agent from scratch using only Python and an LLM.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-29.png

By doing so, we gain full control over the agent’s behavior, making it easier to optimize and troubleshoot​.

We’ll use OpenAI, but if you prefer to do it with Ollama locally, an open-source tool for running LLMs locally, with a model like Llama3 to power the agent, you can do that as well.

Along the way, we’ll explain the ReAct pattern, design an agent loop that interleaves reasoning and tool usage, and implement multiple tools that the agent can call.

The goal is to help you understand both the theory and implementation of ReAct agents.

By the end, you’ll have a working agent and a clear picture of how frameworks like CrewAI leverage ReAct internally.

Let's begin!

* * *

## What is ReAct pattern?

ReAct (short for Reasoning and Acting) is a paradigm for AI agent design where an agent uses chain-of-thought reasoning and tool-using actions in aggregation.

Instead of generating a direct answer in one step, a ReAct agent thinks step-by-step and can perform intermediate actions (like looking something up or calculating a value) before finalizing its answer.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-30.png

To get a clear perspective on this, Like think about how ReAct pattern works.

### Sample 1

Formally, an LLM following ReAct generates reasoning traces (the “Thoughts”) and task-specific actions (calls to tools) in an interleaved manner​. This means the model’s output might look something like:

- Thought: I should calculate the total.
- Action: `Calculator("123 + 456")`
- Observation: `579`
- Thought: Now I have the sum; next, I need to multiply it.
- Action: `Calculator("579 * 789")`
- Observation: `456,831`.
- Thought: I have the final result.
- Final Answer: `456,831`.

The reasoning traces (the chain of thoughts) help the model plan and keep track of what to do next, while the actions let it consult external sources or perform calculations to gather information it otherwise wouldn’t have​ inherent access to.

In effect, the model isn’t limited to its internal knowledge; it can reach out to tools, databases, or the internet as needed and then reason about the results.

This significantly enhances what the agent can do.

IBM describes ReAct agents as ones that use an LLM “brain” to coordinate reasoning and action, enabling interactions with the environment in a structured but adaptable way​.

Unlike a basic chatbot that answers with whatever is in its static knowledge, a ReAct agent can think, search, calculate, and then combine the results into an answer.

### Sample 2

Consider the output of an Agent I built in a multi-agent system (we'll get to the code shortly):

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/Screenshot-2025-04-15-at-7.07.56-PM.png

In the example shown above, we see a live trace of an AI News Reporter Agent executing a task using the ReAct paradigm. The agent has been asked to create a news headline related to the "Agent2Agent Protocol". However, rather than jumping to conclusions, it reasons step by step, as seen in its structured trace.

Let’s break this down:

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/Screenshot-2025-04-15-at-7.07.56-PM.png

- Agent Role: `News Reporter` – This agent specializes in curating and validating news content.
- Task: The agent has been instructed to generate a news headline and ensure it's relevant to the Agent2Agent Protocol.
- Thought: The agent first reasons internally that it should validate the information by performing a quick search for any recent updates about the protocol. This is the reasoning part of the ReAct cycle.
- Action: It proceeds to use a tool labeled `Search the internet`, passing in a structured JSON input with the query: `"Agent2Agent Protocol news November 2023"`. This is the acting step where the agent leverages external tools to gather real-world data.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/Screenshot-2025-04-15-at-7.13.26-PM.png

- Tool Output: It contains the results retrieved by the search tool—potentially news snippets, article summaries, or relevant URLs.

This illustrates the power of combining structured thought and external actions: rather than relying on the model's internal knowledge alone, the agent cross-checks facts using tools.

It's an example of how the ReAct pattern encourages transparency, accuracy, and verifiability in agent behavior—an essential feature for any system tasked with real-world information synthesis.

You can imagine scaling this further with multi-agent setups: a News Collector gathers raw feeds, a Fact Verifier checks reliability, and this News Reporter constructs the headline—all coordinating asynchronously using reasoning and tool-based actions.

Here's the implementation if you want to replicate the same output above.

💡

Make sure you have created a `.env` file with the `OPENAI_API_KEY` specified in it. It will make things much easier and faster for you. Also, add these two lines of code to handle asynchronous operations within a Jupyter Notebook environment, which will allow us to make asynchronous calls smoothly to your Crew Agent.

💡

If you don't want to use OpenAI and stick to an open-source LLM, you can use Ollama as well.

Follow these steps:

\- Download Ollama from [https://ollama.com](https://ollama.com/?ref=dailydoseofds.com).

\- Run the Ollama app.

\- Pull an open-source LLM.

\- Define the LLM as shown below.

\- Pass the LLM as the `llm` parameter to the Agent.

We begin by importing the essential classes from `crewai` and a useful tool: `SerperDevTool`. This tool wraps a real-time web search capability (via [serper.dev](https://serper.dev/?ref=dailydoseofds.com)) and allows our agents to fetch live information from the internet.

Also, get a Serper Dev API key from [serper.dev](https://serper.dev/?ref=dailydoseofds.com) and store it in the `.env` file created earlier:

Next, initialize the Web Search Tool, which the Agents can invoke when they need web results:

Moving on, define the First Agent—The News Collector:

- This agent is designed to behave like a digital journalist. Its responsibility is to gather news stories related to a given topic using the Serper tool. The `verbose=True` flag ensures we get detailed logging—this is what creates the transparent ReAct-style trace showcased earlier.
- Also, the task instructs the `News Collector` to actively search for the latest information on the specified `{topic}`. The `tool` parameter links the task to `SerperDevTool`, enabling it to actually perform the search rather than hallucinating.

Next, define the Second Agent—The News Reporter:

- This agent is the headline writer. It consumes the output from the previous task and crafts a concise headline. Like the collector, it’s also verbose—meaning we’ll see its reasoning steps, tool calls, and decisions in the logs.
- This Agent's task is particularly interesting because it challenges the reporter agent to do two things:
  - Use the prior output (collected news articles).
  - Perform its own validation using the search tool again—double-checking that the news is relevant.
- That’s a ReAct pattern:
  - First, the agent reasons: “Do I have enough information? Is this valid?”
  - Then, it acts: makes a tool call to confirm.

Moving on, we connect our agents and tasks in a sequential crew pipeline:

- The Collector performs the initial search.
- The Reporter builds and validates the headline.

Finally, we start the workflow by passing a topic: Agent2Agent Protocol. The agents will dynamically process this input, use external tools, think through their next move, and generate a validated news headline.

This produces the following verbose output, which shows how your agent "thinks" in natural language, plans its next move, and uses external tools to carry out actions.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-31.png

But that’s not all. Look at one more thing towards the end of this verbose output:

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/Screenshot-2025-04-15-at-7.34.59-PM.png

Under the hood, this ReAct-style behavior is governed by a very specific format template—what we call the action protocol. When using tools like `SerperDevTool`, CrewAI instructs the LLM to follow a rigid response schema. This helps ensure agents interact with tools in a safe, deterministic, and interpretable manner.

First, we have the Agent tool prompt format:

```python
"""
You ONLY have access to the following tools,
and should NEVER make up tools that are not listed here:

Tool Name: Search the internet
Tool Arguments: {'search_query': {'description':
                 'Mandatory search query you want to use
                 to search the internet', 'type': 'str'}}
Tool Description: A tool that can be used to
                  search the internet with a search_query.

"""
```

Copy

This is part of the tool context injected into the LLM prompt. It tells the agent:

- What tools are available.
- What arguments are required.
- That it must not invent tools or go off-protocol.

This creates strong constraints around agent behavior—which is important when you want to avoid hallucinations or misuse of capabilities.

The prompt also includes this critical instruction:

````python
"""
IMPORTANT: Use the following format in your response:

```
Thought: you should always think about what to do
Action: the action to take, only one name of
[Search the internet], just the name, as it's written.

Action Input: the input to the action, just a
simple JSON object, enclosed in curly braces,
using " to wrap keys and values.

Observation: the result of the action
```
"""
````

Copy

This is the _reasoning + acting_ loop spelled out in literal terms:

1. Thought: The agent expresses its internal reasoning.
2. Action: The agent picks the tool to use—verbatim.
3. Action Input: Arguments for the tool, formatted as strict JSON.
4. Observation: What the tool returned (i.e., the raw output).

This schema ensures that tools can be executed reliably, logged consistently, and traced clearly. And crucially—it’s LLM-friendly. Everything is written in natural language that the model understands and responds to.

Once all information is gathered, the agent is told to conclude like this:

````python
"""
Once all necessary information is gathered,
return the following format:

```
Thought: I now know the final answer
Final Answer: the final answer to
the original input question
```
"""
````

Copy

This signals the end of the reasoning chain. At this point, the agent has completed its research and can produce a confident, top-level answer.

That’s the essence of ReAct, which is implemented seamlessly using CrewAI.

### But why does this matter?

ReAct was introduced as a major step in making LLM-based agents more reliable and powerful​.

By having the model explain its thought process and check facts via tools, we reduce problems like hallucination and error propagation.

The original ReAct research by Yao et al. showed that this approach can overcome hallucination in question answering by letting the model retrieve real information (e.g. querying Wikipedia) to verify its facts​.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/Screenshot-2025-04-15-at-6.13.51-PM.png

It also improves the transparency of the agent’s decision-making, as we can inspect the chain of thought for debugging or trustworthiness​.

Overall, the ReAct pattern turns a passive LLM into an active problem solver that can break down complex tasks and interact with external data sources, much like an autonomous assistant.

This also explains why it is widely used in almost Agentic frameworks. The actual implementation could vary but everything does connect back to something that's derived from a ReAct pattern.

To reiterate, this format:

- Forces your LLM to operate step by step,
- Clearly separates thinking from acting,
- Guarantees deterministic input-output behavior for tools,
- And produces traceable reasoning chains you can inspect or debug.

### Reasoning + Acting: How ReAct Agents Work

A ReAct agent operates in a loop of Thought → Action → Observation, repeating until it reaches a solution or a final answer.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-33.png

This is analogous to how humans solve problems:

- we think about what to do
- perform an action (like looking something up or doing a calculation),
- observe the result
- and then incorporate that into our next thought.

The ReAct framework uses prompt engineering to enforce this structured approach, alternating the model’s thoughts and actions/observations​.

Here’s a step-by-step breakdown of the ReAct cycle in an AI agent:

- Thought: The Agent (powered by an LLM) analyzes the user’s query and internal context, and produces a reasoning step in natural language. This is typically not shown to the end user but is part of the agent’s self-talk. For example: “The question asks for the population of a country; I should use a web search to find the latest figure.”

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-34.png

- Action: Based on the thought, the agent decides on an external tool or operation to perform. It outputs a prescribed format indicating the action. For instance: `Action: WebSearch("population of Canada 2023")`. The agent essentially “calls” a function (tool) by name, often with some input parameters.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-42.png

- Observation: The agent’s environment (our code) executes the requested action and returns the result (observation) back to the agent. For example, the web search tool might return: “`Observation: The population of Canada in 2023 is 38 million.`” This observation is fed into the agent’s context.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-41.png

- The agent takes the new information and goes back to step 1 (another Thought). It will reason with the fresh data. In our example, it might think: “Now I have the population figure; I can answer the question.”

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-40.png

1. This Thought/Action/Observation cycle repeats, allowing the agent to chain multiple tool uses if needed (search, then maybe a calculation, then another search, etc.). Eventually, the agent decides it can answer the user. At that point, instead of an Action, it outputs a Final Answer (sometimes marked as `Answer:` or `Final Answer:` in the format).

As we shall see shortly in the implementation from scratch, throughout this process, the agent maintains the conversation and its own intermediate steps.

Each Thought and Observation can be appended to the dialogue context so the LLM remembers what it has done so far.

https://storage.ghost.io/c/3f/df/3fdf6ed2-17ac-4b12-a693-8078bd13e748/content/images/2025/04/image-43.png

This is crucial for coherence. The end result is that the agent effectively plans its approach on the fly, mixing reasoning and acting.

This dynamic approach is much more adaptable than a rigid script or a single-turn response. It allows handling unforeseen sub-tasks, similar to how humans adjust plans when new information comes up​.

It’s important to note that all these “Thought” and “Action” annotations are not magical features of the LLM—they come from how we prompt the model.

As we shall see below, we explicitly instruct the model to format its responses in this structured way. In other words, ReAct is implemented via carefully crafted prompt templates and parsing logic, not via any built-in LLM ability.

The LLM is guided to behave like an agent that reasons and acts, through the examples and instructions we give it.

Now that we understand the ReAct pattern conceptually, we can start building our own agent that follows this logic. We’ll need a language model to serve as the agent’s brain, some tools the agent can use, and a loop that ties them together.

In the next section, we’ll step away from CrewAI and build a ReAct agent from scratch—in pure Python, using only local LLMs and a simple set of tool definitions. You'll see that everything we covered here is not magic—it’s just smart prompt design combined with controlled I/O.

💡

Make sure you have created a `.env` file with the `OPENAI_API_KEY` specified in it. It will make things much easier and faster for you. Also, add these two lines of code to handle asynchronous operations within a Jupyter Notebook environment, which will allow us to make asynchronous calls smoothly to your Crew Agent.

## ReAct Implementation from Scratch

Below, we shall implement a ReAct Agent in two ways:

- Manually executing each step for better clarity.
- Without manual intervention to fully automate the Reasoning and Action process.

You can download the code below:

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="orchdag-complex-tool-orchestration-in-multi-turn-interaction.md">
<details>
<summary>OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2510.24663v1>

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2510.24663v1 \[cs.AI\] 28 Oct 2025

# OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs

Yifu Lu

Princeton University

yiful@princeton.edu

&Shengjie Liu11footnotemark: 1

Amazon

zycjlsj@amazon.com

Li Dong

Amazon

ldonga@amazon.com

Work is done during internship in Amazon. Equal contribution.

###### Abstract

Agentic tool use has gained traction with the rise of agentic tool calling, yet most existing work overlooks the complexity of multi-turn tool interactions. We introduce OrchDAG, a synthetic data generation pipeline that models tool execution as directed acyclic graphs (DAGs) with controllable complexity. Using this dataset, we benchmark model performance and propose a graph-based reward to enhance RLVR training. Experiments show that the dataset presents a challenging but solvable benchmark, and the proposed reward is effective when combined with GRPO-style algorithms, highlighting the importance of leveraging topological structure and data complexity in multi-turn tool use.

## 1 INTRODUCTION

Large Language Models (LLMs) ([brown2020languagemodelsfewshotlearners](https://arxiv.org/html/2510.24663v1#bib.bib3 ""); [JMLR:v24:22-1144](https://arxiv.org/html/2510.24663v1#bib.bib5 ""); [deepseekai2025deepseekr1incentivizingreasoningcapability](https://arxiv.org/html/2510.24663v1#bib.bib6 ""); [touvron2023llama2openfoundation](https://arxiv.org/html/2510.24663v1#bib.bib26 ""); [zeng2023glm130bopenbilingualpretrained](https://arxiv.org/html/2510.24663v1#bib.bib36 "")) have been at the forefront of advancing artificial intelligence, marking significant breakthroughs in diverse fields. The planning capabilities of LLMs, particularly their ability to use tools ([yao2023treethoughtsdeliberateproblem](https://arxiv.org/html/2510.24663v1#bib.bib33 ""); [yao2023reactsynergizingreasoningacting](https://arxiv.org/html/2510.24663v1#bib.bib34 "")), enable them not only to execute commands and perform web searches but also to enhance their advanced mathematical reasoning abilities. LLM Compiler [kim2024llmcompilerparallelfunction](https://arxiv.org/html/2510.24663v1#bib.bib12 "") and its subsequent work ([erdogan2024tinyagentfunctioncallingedge](https://arxiv.org/html/2510.24663v1#bib.bib7 ""); [erdogan2025planandactimprovingplanningagents](https://arxiv.org/html/2510.24663v1#bib.bib8 "")) propose constructing tooling usage as a directed acyclic graph (DAG) to enable the parallel execution of independent tools, thereby improving tool-calling efficiency. CodeAct [wang2024executablecodeactionselicit](https://arxiv.org/html/2510.24663v1#bib.bib28 "") and CodePlan [wen2024unlockingreasoningpotentiallarge](https://arxiv.org/html/2510.24663v1#bib.bib29 "") propose leveraging the generation of pseudo-Python code to outline high-level reasoning processes for complex multi-step reasoning tasks, where each tool usage is represented as a function call within the code. ReWOO [xu2023rewoodecouplingreasoningobservations](https://arxiv.org/html/2510.24663v1#bib.bib30 "") proposes a modular framework that decouples the reasoning process from the external observations of each tool usage, thereby reducing token consumption and improving efficiency. [liu2025toolplannertaskplanningclusters](https://arxiv.org/html/2510.24663v1#bib.bib15 "") clusters the provided tools into groups of toolkits, plans at the toolkit level, and replans by selecting tools within the same toolkit if error comes out. [ma2024nonmyopicgenerationlanguagemodels](https://arxiv.org/html/2510.24663v1#bib.bib17 "") proposes a method called Predictive-Decoding, which leverages Model Predictive Control from the optimal control field to mitigate early errors in planning and promote non-myopic planning, thereby enhancing overall accuracy. ReasonFlux [yang2025reasonfluxhierarchicalllmreasoning](https://arxiv.org/html/2510.24663v1#bib.bib31 "") proposes a framework in which the LLM reasons over template fields, executes tools based on the templates, and employs reinforcement learning to improve planning accuracy using an action completion reward.

In the agentic setting, LLMs are evolving beyond purely textual reasoning toward dynamic agents capable of planning, tool use, and multi-step (also multi-turn) execution. The introduction of Group Relative Policy Optimization (GRPO) [shao2024deepseekmathpushinglimitsmathematical](https://arxiv.org/html/2510.24663v1#bib.bib22 "") further inspired the development of Reinforcement Learning with Verifiable Reward (RLVR) for agentic tool use, driven by its efficiency. The xLAM [zhang2024xlamfamilylargeaction](https://arxiv.org/html/2510.24663v1#bib.bib37 "") suite introduces purpose-built “large action models” optimized for function calling, offering strong baselines and open resources for multi-turn tool execution. Llama-Nemotron [bercovich2025llamanemotronefficientreasoningmodels](https://arxiv.org/html/2510.24663v1#bib.bib2 "") extends this trajectory with efficient reasoning modes and scalable inference, enabling models to dynamically switch behaviors across long conversations. ToolRL [qian2025toolrlrewardtoollearning](https://arxiv.org/html/2510.24663v1#bib.bib19 "") systematically studies reinforcement learning reward designs—covering granularity, temporal structure, and signal types—to improve generalization in multi-turn tool-integrated reasoning, while OTC [wang2025actingreasoningmoreteaching](https://arxiv.org/html/2510.24663v1#bib.bib27 "") complements this by explicitly balancing accuracy and tool-call efficiency to maintain productivity over prolonged interactions. Kimi K2 [kimiteam2025kimik2openagentic](https://arxiv.org/html/2510.24663v1#bib.bib25 "") shows that stabilizing long-context training and using multi-stage RL leads to robust performance across multi-round software engineering, math, and agentic tasks. These works highlight that advancing agentic LLMs in multi-turn settings requires not only larger or more efficient models, but also principled reward design, cost-aware tool-use strategies, and scalable system pipelines.

Recent advances in evaluating agentic models have led to new benchmarks and environments for assessing performance in realistic, interactive scenarios. ACEBench [chen2025acebenchwinsmatchpoint](https://arxiv.org/html/2510.24663v1#bib.bib4 "") overcomes limits of prior evaluations by introducing a structured benchmark with Normal, Special, and Agent categories to test atomic-level tool use across simple, complex, multi-agent, and ambiguous instruction settings. Complementing this, BFCL (v3) [patil2025bfcl](https://arxiv.org/html/2510.24663v1#bib.bib18 "") standardizes function-calling benchmarks across real-world contexts, supporting serial and parallel invocations in multiple languages through an AST-based evaluation. τ\\tau-Bench, τ2\\tau^{2}-Bench, and UserBench [yao2024taubenchbenchmarktoolagentuserinteraction](https://arxiv.org/html/2510.24663v1#bib.bib32 ""); [barres2025tau2benchevaluatingconversationalagents](https://arxiv.org/html/2510.24663v1#bib.bib1 ""); [qian2025userbenchinteractivegymenvironment](https://arxiv.org/html/2510.24663v1#bib.bib20 "") together extend evaluation from structured tool–user interactions to controlled bidirectional agent cooperation and finally to fully user-centric, dynamic environments, progressively enriching the realism and robustness of agent assessment.

Prior work on tool use has mainly studied general real-world APIs [qin2023toolllmfacilitatinglargelanguage](https://arxiv.org/html/2510.24663v1#bib.bib21 ""), such as send email or make calendar, along with related functions in web search systems like Manus. Meanwhile, current multi-turn settings mainly focus on computer-use tasks [patil2025bfcl](https://arxiv.org/html/2510.24663v1#bib.bib18 ""), such as manipulating files in the operating system. In industrial settings, however, an agent may need to work with hundreds of domain tools, including APIs and pipeline endpoints, and may also interact with other domain agents to produce a complete answer to a user query. The complexity usually arises from three aspects: (1) the dependencies among tools can be intricate, (2) the output of a tool is often represented as a JSON file with many fields, and (3) a key output field from one tool may serve as an input to another, but with different field names. Moreover, in multi-turn settings, the environment may execute the required tools but encounter time-outs or runtime errors in their responses. Therefore, it is important to construct a dataset that not only evaluates current models but also pushes their capabilities in complex multi-turn tool interaction, which is essential for building robust and reliable agents.

In summary, this work makes several pivotal contributions:

- •

We design a synthetic multi-turn data generation pipeline OrchDAG for agentic tool use, where each round of tool execution for a user query is represented as a DAG. The complexity of the generated data is controlled by a pipeline hyperparameter.

- •

Using the constructed dataset, we first evaluate the current model’s performance and then introduce a graph-based reward derived from the DAG for RLVR training.

- •

Extensive experiments show the effectiveness of our approach, emphasizing the value of incorporating the topological structure of tool execution graphs and the importance of controlling data complexity in multi-turn tool use.

## 2 PRELIMINARY

### 2.1 LLM Reasoning with Tools for Multi-turn Settings

For the first turn, given a user query xx and a pretrained LLM ρθ​(⋅)\\rho\_{\\theta}(\\cdot), the LLM generates an tool execution plan represented as a graph with p={𝒫1,…,𝒫n}∼ρθ​(p∣𝒯,𝒟,x)p=\\{\\mathcal{P}\_{1},\\dots,\\mathcal{P}\_{n}\\}\\sim\\rho\_{\\theta}(p\\mid\\mathcal{T},\\mathcal{D},x), where pp is the plan list after topological sorting, 𝒯\\mathcal{T} is the set of available tools, and 𝒟\\mathcal{D} is the collection of descriptions for all available tools. At each step tt, the LLM generates an intermediate reasoning output rt∼ρθ​(rt∣𝒯,𝒟,x,p,𝒪1,…,𝒪t−1)r\_{t}\\sim\\rho\_{\\theta}(r\_{t}\\mid\\mathcal{T},\\mathcal{D},x,p,\\mathcal{O}\_{1},\\dots,\\mathcal{O}\_{t-1}) and executes the plan step 𝒫t\\mathcal{P}\_{t} to obtain the observation 𝒪t\\mathcal{O}\_{t}. The final response is then generated as ℛ∼ρθ​(ℛ∣𝒯,𝒟,x,p,𝒪1,…,𝒪n)\\mathcal{R}\\sim\\rho\_{\\theta}(\\mathcal{R}\\mid\\mathcal{T},\\mathcal{D},x,p,\\mathcal{O}\_{1},\\dots,\\mathcal{O}\_{n}).

In later turns, a user may issue an irrelevant query requiring a completely new tool execution graph, or a dependent query that builds on partial outputs from earlier tool executions or responses. Additionally, some tools may return errors (e.g., timeouts), requiring unfinished execution paths from prior queries to be rescheduled.

### 2.2 Tool Execution as DAG

Given a plan pp generated by the LLM, we represent it as a directed graph 𝒢=(𝒱,ℰ)\\mathcal{G}=(\\mathcal{V},\\mathcal{E}), where 𝒱=(v1,…,vn)\\mathcal{V}=(v\_{1},\\dots,v\_{n}) is the set of nodes and ℰ=(e1,…,em)\\mathcal{E}=(e\_{1},\\dots,e\_{m}) is the set of edges. The node v1v\_{1} corresponds to the user query, and vnv\_{n} represents the final node that aggregates observations and returns the response. The intermediate nodes v2,…,vn−1v\_{2},\\dots,v\_{n-1} correspond to tool calls, each associated with an attribute that stores its tool payload in JSON format. An edge ei∈ℰe\_{i}\\in\\mathcal{E} denotes a dependency between two tools, where an output key from the source tool serves as an input key to the target tool.

We represent the tool graph as an ordered list of tasks in a JSON-like text style. Each task contains four fields : task\_id, toolname, payload, and dependencies. A task can be associated with multiple dependencies. A task can be expressed as {task\_id: task\_4, toolname: name, payload: {param1: val1, param2: $2.outputkey1, param3: $3.outputkey4}, dependencies: \[task\_2, task\_3\]}.

## 3 METHODOLOGY

In real-world domains, API specifications and orchestrations are often considerably more complex, making it challenging for LLMs pretrained on general public data to generate accurate and reliable plans for diverse user queries. Drawing inspiration from LLMCompiler [kim2024llmcompilerparallelfunction](https://arxiv.org/html/2510.24663v1#bib.bib12 ""); [erdogan2025planandactimprovingplanningagents](https://arxiv.org/html/2510.24663v1#bib.bib8 ""), for queries involving complex tool interactions, it is advantageous to first construct a tool execution DAG. This DAG serves as a blueprint for executing tools sequentially or in parallel, with subsequent replanning guided by both the execution results of the current DAG and any new user queries in later turns.

### 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use

As discussed in Section [1](https://arxiv.org/html/2510.24663v1#S1 "1 INTRODUCTION ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), the design of the data generation pipeline follows several key principles to better reflect real-world tool-use scenarios: (1) the complexity of the tool execution DAG for each synthetic user query should be controllable through pipeline hyperparameters, (2) the system prompt provided to the LLM must include irrelevant tools (both schema and description) so that the model learns to identify and select only the relevant ones, (3) the output payload of each tool should contain multiple fields, typically four or five, and (4) at least one key output field from a tool should serve as an input to another tool, but with a different field name, to capture schema misalignment commonly observed in practice.

Moreover, in multi-turn settings, the data should capture scenarios where certain nodes in the tool execution DAG fail. When the user issues a follow-up query, the corresponding DAG in the dataset should exclude nodes that have already been executed in the previous turn, while reusing their available results whenever applicable. In light of these requirements, we develop a graph-based data generation pipeline implemented with LangGraph 111https://langchain-ai.github.io/langgraph/, accompanied by a set of validation functions to ensure the quality of the generated data points.

https://arxiv.org/html/2510.24663v1/x1.pngFigure 1: Data Generation Pipeline for a single turn

As shown in Figure [1](https://arxiv.org/html/2510.24663v1#S3.F1 "Figure 1 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), the data generation pipeline begins by collecting real high-quality tools from existing benchmarks, Specifically, we leverage APIGen[liu2024apigenautomatedpipelinegenerating](https://arxiv.org/html/2510.24663v1#bib.bib16 "") and ToolACE[liu2025toolacewinningpointsllm](https://arxiv.org/html/2510.24663v1#bib.bib14 ""). To ensure sufficient complexity, we retain only examples where the final answer involves more than two distinct functions represented in JSON format. Notably, we extract tools directly from the answers rather than from the system-prompt tool lists. This design choice eliminates the need for additional categorization or clustering steps, which could introduce unnecessary uncertainty, while naturally yielding a smaller and more coherent set of related tools. After filtering, APIGen contributes 2,542 data points and ToolACE contributes 1,005.

For each data point, suppose it contains four real tools; these are placed as the first layer of the tool execution DAG. Based on the hyperparameters of the DAG (height and width), we then randomly sample a topological order to obtain a DAG template (see Figure [1](https://arxiv.org/html/2510.24663v1#S3.F1 "Figure 1 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs")). According to this template, we synthesize the tools for each node layer by layer under the following conditions: (1) each input key must depend on an output key from one of its parent nodes in the DAG, and (2) the field names should not remain identical across instances but instead vary randomly. After populating the DAG template, we obtain the tool execution DAG, which is then used to prompt the LLM to generate the corresponding user query, conditioned on the DAG and a few-shot set of examples. Finally, we augment the system prompt with irrelevant tools to encourage the model to discriminate among available options.

https://arxiv.org/html/2510.24663v1/x2.pngFigure 2: Extension of single-turn data generation pipeline to multi-turn settings

We further extend the generation pipeline to the multi-turn setting by attaching three additional nodes to the final node (see Figure [2](https://arxiv.org/html/2510.24663v1#S3.F2 "Figure 2 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs")), with only one being activated during generation. These nodes correspond to three possible multi-turn scenarios : (1) the user issues a completely irrelevant query, (2) the user poses a query that requires a new set of tools while also depending on the previous final response or intermediate tool outputs, and (3) a tool execution error occurs, such as a timeout. In case (1), the outcome is a completely new DAG; in case (2), the new DAG must explicitly encode cross-turn dependencies through the task identifiers from the previous DAG; and in case (3), the resulting DAG reduces to a partial subgraph of the original DAG. We adopt the final data generation format introduced in ToolRL [qian2025toolrlrewardtoollearning](https://arxiv.org/html/2510.24663v1#bib.bib19 ""). An example of a generated data sample is shown in Figure [3.1](https://arxiv.org/html/2510.24663v1#S3.SS1 "3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs").

The quality of the data, particularly the synthetic data, is critical. To ensure reliability, we incorporate a rule-based verification mechanism into the generation pipeline. All tools, plan DAGs, tool calls, and observations produced by the LLM are required to be in JSON format. The first verification layer checks JSON validity. For plan DAGs, we apply AST [patil2025bfcl](https://arxiv.org/html/2510.24663v1#bib.bib18 "") matching at each node to guarantee that the LLM only references the provided tools with the correct argument names. We further validate symbolic arguments by comparing each referenced key against the JSON schema of the predecessor’s output. Every tool call is verified against the plan DAG and the preceding tool call observations, ensuring adherence to the plan and the correct use of return values as inputs for dependent calls. Likewise, each observation is matched to its corresponding tool call, and its return value is checked against the tool’s JSON schema. If any verification step fails during generation, the LLM is required to restart the process.

Our pipeline enables the generation of diverse synthetic queries derived from high-quality real APIs, each requiring resolution through a plan DAG. The difficulty of the queries is controlled by the topological structure of randomly generated DAG templates. Since these templates vary in structure, a fixed workflow for synthetic data generation is impractical. Instead, the graph-based pipeline provides a flexible end-to-end framework for producing such data. Finally, the rule-based verification mechanism ensures reliability: it not only checks JSON validity to guarantee compatibility with downstream benchmarks, but also leverages AST matching to validate the correctness of DAG instantiations during data generation.

Synthetic Data SampleSystem Prompt:

You are a dialogue assistant designed to leverage tool calls to solve user tasks and provide structured responses.

Available Tools

In your response, you can use the following tools:
{{Tool List}}

Steps for each turn

1\. Think: Retrieve the relevant context and evaluate the current tool.

2\. DAG: Produce a task list defined here [2.2](https://arxiv.org/html/2510.24663v1#S2.SS2 "2.2 Tool Execution as DAG ‣ 2 PRELIMINARY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs")

3\. Respond: If a response is needed, generate one while maintaining consistency across user queries.

Synethetic User Query: …

</think> …</think> \[The think block is absent in the synthetic data but included during the training stage.\]

</DAG> real DAG generated from pipeline </DAG>

<tool\_call> tool call 1st DAG layer </tool\_call>

<obs> observation 1st DAG layer </obs>

…

<tool\_call> tool call last DAG layer </tool\_call>

<obs> observation last DAG layer </obs>

</response> … </response>

New User Query: …

</think> …</think>

</DAG> new DAG based on the three scenarios defined in the multi-turn settings [2](https://arxiv.org/html/2510.24663v1#S3.F2 "Figure 2 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"). </DAG>

…

### 3.2 OrchDAG – Graph-based Reward Derived from the DAG for RLVR training

Due to the intricate tool interaction structure inherent in the synthetic data, the format reward, correctness reward, and parameter matching reward defined in [qian2025toolrlrewardtoollearning](https://arxiv.org/html/2510.24663v1#bib.bib19 "") may remain sparse, even when initiating a large number of rollouts. Moreover, this reward does not account for structural dependencies among tools; thus, no reward is given when the LLM correctly predicts partial dependencies for these tools.

To account for structural dependencies, and given that we have access to the ground-truth DAG during synthetic data generation, following [Liu2025](https://arxiv.org/html/2510.24663v1#bib.bib13 ""), we use a weighted Graph Edit Distance (GED) as the reward signal at each turn. GED [10.5555/2736754.2736796](https://arxiv.org/html/2510.24663v1#bib.bib10 "") measures the distance between two graphs by applying operations such as edge deletion, edge insertion, node insertion, or node relabeling to transform one graph into an isomorphic form of the other.

We define the reward for each turn as

| | | |
| --- | --- | --- |
| | RTotal=RFormat+α​RDAG,whereRDAG=1−GED​(g1,g2)GED​(g1,∅)+GED​(g2,∅)\\text{R}\_{\\text{Total}}=\\text{R}\_{\\text{Format}}+\\alpha\\text{R}\_{\\text{DAG}},\ \ \\text{where}\ \ \\text{R}\_{\\text{DAG}}=1-\\frac{\\text{GED}(\\text{g}\_{1},\\text{g}\_{2})}{\\text{GED}(\\text{g}\_{1},\\emptyset)+\\text{GED}(\\text{g}\_{2},\\emptyset)} | |

Here g1\\text{g}\_{1} is the predicted DAG, g2\\text{g}\_{2} is the ground-truth DAG. We define the following node equivalence when calculating GED: the tool name, parameter names, and parameter values are treated as a single unit, and equivalence is evaluated at the level of the entire tool call. The reward RFormat\\text{R}\_{\\text{Format}} is assigned a value of 1 if the output contains the special tokens in the correct order, and 0 otherwise. α\\alpha is the hyperparameter used to balance the two types of rewards. In this reward design, we not only provide credit to LLMs for partially correcting the path during rollouts, but also make the rewards denser compared to the previous design. The multi-turn setting is naturally supported, as the ground-truth DAG is available at each turn.

## 4 EXPERIMENTS

In this section, we describe the generated dataset, focusing on the distribution of topological difficulty in the DAG templates and the proportion of single-turn versus multi-turn settings. For simplicity, we restrict evaluation to the two-turn setting, leaving extensions to longer horizons for future work. To ensure independence between training and test data, we construct them from two disjoint sets of data points from APIGen[liu2024apigenautomatedpipelinegenerating](https://arxiv.org/html/2510.24663v1#bib.bib16 "") and ToolACE[liu2025toolacewinningpointsllm](https://arxiv.org/html/2510.24663v1#bib.bib14 "")., as described in [1](https://arxiv.org/html/2510.24663v1#S3.F1 "Figure 1 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs").

Table 1: Synthetic Data Distribution (Height and width are hyperparameters controlling DAG complexity, and success rate is the proportion of data that passes rule-based validation)

| Type | data # | Multi-turn proportion | Average Height | Average Width | Sucessful Rate |
| --- | --- | --- | --- | --- | --- |
| Training | 1800 | 30% | 2.50 ±\\pm 0.12 | 3.4 ±\\pm 0.24 | 0.6 |
| Test | 250 | 25% | 2.7 ±\\pm 0.08 | 3.1 ±\\pm 0.14 | 0.7 |

### 4.1 Task Difficulty

We investigate two central questions: (1) Given the designed difficulty of our synthetic data, is the dataset solvable in principle? A dataset that cannot be solved even by advanced closed-source models such as Claude 4 or GPT-4o would lack practical utility. (2) If it is solvable, does the dataset offer a sufficient level of challenge to meaningfully evaluate model performance? To begin with, we evaluate several closed-source and open-source models by providing them with the system prompt defined in Section [3.1](https://arxiv.org/html/2510.24663v1#S3.SS1 "3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), and measure whether they can correctly predict the DAG by analyzing tool dependencies. In the multi-turn setting, models must generate the DAG by considering both the available tools and the observations from previous turns. We use Accuracy (pass@1) to evaluate performance, as our focus here is on assessing the task difficulty introduced by the dataset.

Table 2: Pass@1 Accuracy for predicting the DAG for single/multi-turn settings (All experiments were run 10 times with the temperature of the base LLMs set to 0.10.1)

| Models | Zero Shot | One shot | Three shots |
| --- | --- | --- | --- |
| GPT-4o | (0.18 ±\\pm 0.03) | (0.22 ±\\pm 0.02) | (0.24 ±\\pm 0.04) |
| Claude 4 | (0.15 ±\\pm 0.01) | (0.23 ±\\pm 0.03) | (0.22 ±\\pm 0.01) |
| Claude 3.7 | (0.16 ±\\pm 0.04) | (0.18 ±\\pm 0.03) | (0.23 ±\\pm 0.01) |
| Claude 3.5 | (0.08 ±\\pm 0.02) | (0.09 ±\\pm 0.03) | (0.08 ±\\pm 0.03) |
| DeepSeek-R1 | (0.12 ±\\pm 0.02) | (0.14 ±\\pm 0.01) | (0.11 ±\\pm 0.04) |
| Qwen2.5 3B | (0 ±\\pm 0) | (0 ±\\pm 0) | (0.02 ±\\pm 0.01) |
| Qwen2.5 7B | (0.02 ±\\pm 0.01) | (0.03 ±\\pm 0.02) | (0.03 ±\\pm 0.02) |

For completeness, we also report Qwen3 pass@64 accuracy: 20.23% for Qwen3-4B and 26.55% for Qwen3-8B. From Table [2](https://arxiv.org/html/2510.24663v1#S4.T2 "Table 2 ‣ 4.1 Task Difficulty ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), we can see that GPT-4o maintains the highest accuracy for the zero-shot setting and the three-shots setting with nearly same performance with Claude 4 in the one-shot setting. The accuracy for GPT-4o and also for Claude 4 shows that our dataset is solvable however the perofmrance for Claude 3.5, Qwen2.5 3B with accuracy 0, and Qwen 2.5 7B demonstrates the challenge of our datasets to current LLMs. Comparison between the one-shot and three-shot results shows that providing additional examples does not necessarily improve LLM performance in DAG prediction.

### 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG

As discussed in Section [3.2](https://arxiv.org/html/2510.24663v1#S3.SS2 "3.2 OrchDAG – Graph-based Reward Derived from the DAG for RLVR training ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), the reward signal from ToolRL [qian2025toolrlrewardtoollearning](https://arxiv.org/html/2510.24663v1#bib.bib19 "") can be sparse in our data., which makes it difficult for reinforcement learning algorithms such as GRPO [shao2024deepseekmathpushinglimitsmathematical](https://arxiv.org/html/2510.24663v1#bib.bib22 ""), DAPO [yu2025dapoopensourcellmreinforcement](https://arxiv.org/html/2510.24663v1#bib.bib35 ""), and GiGPO [feng2025groupingrouppolicyoptimizationllm](https://arxiv.org/html/2510.24663v1#bib.bib9 "") to efficiently improve the policy LLM, even with large rollouts. We apply ToolRL on the training single-turn dataset and evaluate it on the test set in the single-turn setting. In this setup, we train Qwen2.5 with GRPO using ToolRL, and convert the ToolCalls it generates into predicted DAGs, since the outputs follow a standardized JSON format. We use 8×100 A100 GPUs with Verl [Sheng\_2025](https://arxiv.org/html/2510.24663v1#bib.bib23 "") to complete the training. We evaluate performance using two metrics: Accuracy/step and Accuracy/user\_query. Accuracy/step measures correctness at the step level, where each individual action in a turn is assessed independently; a step may be correct even if the final tool execution graph is incorrect. Accuracy/user\_query measures correctness at the full query level, requiring the entire tool execution graph to be correct.

Table 3: ToolRL Performance on OrchDAG Single-turn Test Dataset
(The definitions of fine-grained and coarse rewards are given in ToolRL

| Model (Qwen2.5) | Acc/step | Acc/user\_query |
| --- | --- | --- |
| 3B Coarse | 0.517 | 0 |
| 3B Finegrained | 0.540 | 0 |
| 7B Coarse | 0.609 | 0 |
| 7B Finegrained | 0.594 | 0 |

From Table [3](https://arxiv.org/html/2510.24663v1#S4.T3 "Table 3 ‣ 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), we observe that ToolRl performs reasonably well on certain steps within a single turn; however, it struggles to maintain a coherent overview of the entire execution. In contrast, as shown in Table [2](https://arxiv.org/html/2510.24663v1#S4.T2 "Table 2 ‣ 4.1 Task Difficulty ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), Qwen2.5-7B achieves 2% accuracy in predicting the DAG. This indicates that for complex tool executions, it may be advantageous to first establish a high-level plan, such as a DAG, to guide the subsequent execution. We subsequently fine-tune Qwen2.5 using GRPO on the training single-turn dataset, guided by the proposed graph-based reward. We evaluate different hyperparameter settings: the use of entropy regularization and the KL loss, the choice of rollout number, and the number of training steps for the optimizer.

Table 4: Performance of Graph-Based Reward on OrchDAG Single-turn Test Dataset (We report results using Acc/user\_query as the evaluation metric. The columns indicate the number of training steps, and nn denotes the rollout number.)

| Model (Qwen2.5) / Steps | 15 | 30 | 45 | 60 |
| --- | --- | --- | --- | --- |
| 3B KL n=4 | 0 | - | - | - |
| 7B n=4 | 0.184 | 0.253 | 0.241 | - |
| 7B KL n=4 | 0.184 | 0.276 | 0.276 | - |
| 7B KL Entropy n=4 | 0.195 | 0.276 | 0.253 | - |
| 7B KL n=8 | 0.23 | 0.33 | 0.402 | 0.391 |

In Table [4](https://arxiv.org/html/2510.24663v1#S4.T4 "Table 4 ‣ 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), we observe that model size has a clear impact on performance. Moreover, the rollout number plays a crucial role, consistent with the intuition that larger rollout numbers enable greater exploration [srivastava2025technicalsurveyreinforcementlearning](https://arxiv.org/html/2510.24663v1#bib.bib24 ""), thereby increasing the likelihood of reaching the correct DAG. To evaluate the effectiveness of the GED-based reward design, we conduct an ablation study using a coarser reward: the predicted DAG receives a reward of 1 if it exactly matches the ground-truth DAG, and 0 otherwise. Using the 7B model with KL and n=8n=8, the accuracy remains 0 even after 15 training steps.

We then extend our experiments to the multi-turn setting. In this setting, we train Qwen2.5 on the entire training set with GRPO, using both the information from previous turns and the new user query as input, and evaluate performance on the full OrchDAG test dataset. Based on Table [4](https://arxiv.org/html/2510.24663v1#S4.T4 "Table 4 ‣ 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), we report performance only at the 45th training step.

Table 5: Performance of Graph-Based Reward on OrchDAG Single/Multi-turn Test Dataset (We report results using Acc/user\_query as the evaluation metric. The columns indicate the three multi-turn scenarios defined by [2](https://arxiv.org/html/2510.24663v1#S3.F2 "Figure 2 ‣ 3.1 OrchDAG – Synthetic Data Generation Pipeline for Multi-Turn Tool Use ‣ 3 METHODOLOGY ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"))

| Model (Qwen2.5) / Steps | scenario 1 | scenario 2 | scenario 3 |
| --- | --- | --- | --- |
| 7B KL Entropy n=4 | 0.112 | 0.125 | 0.218 |
| 7B KL n=8 | 0.156 | 0.203 | 0.352 |

From Table [5](https://arxiv.org/html/2510.24663v1#S4.T5 "Table 5 ‣ 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), we observe that in the multi-turn setting, performance decreases across both experimental setups. The largest drops occur in Scenario 1 (tool-calling error) and Scenario 2 (requiring information from the previous turn), since these tasks depend not only on the new user query and the system prompt but also on information carried over from earlier turns. In contrast, the drop in Scenario 3 is smaller, as the new user query is completely independent of prior turns. To demonstrate generalizability, we further evaluate the trained model on StableToolBench [guo2024stabletoolbench](https://arxiv.org/html/2510.24663v1#bib.bib11 ""), measuring solvable pass rates across L1, L2, and L3 categories. A task is considered successful when the predicted DAG matches the ground truth. We choose StableToolBench for its inherent complexity in tool interactions. In StableToolBench, GPT-4-0613 (CoT) achieves solvable pass rates of 45.5 (L1 instruction), 57.4 (L1 category), 48.8 (L1 tool), 43.0 (L2 instruction), 46.5 (L2 category), and 48.1 (L3 instruction). Under the same evaluation, our model attains 47.1, 56.4, 47.2, 41.3, 44.8, and 50.7, respectively.

### 4.3 Training Insight Analysis

As shown in Table [4](https://arxiv.org/html/2510.24663v1#S4.T4 "Table 4 ‣ 4.2 Analysis of the Graph-based Reward Shaping in OrchDAG ‣ 4 EXPERIMENTS ‣ OrchDAG: Complex Tool Orchestration in Multi-Turn Interactions with Plan DAGs"), performance generally improves as the number of training steps increases. However, when we extend training beyond this range, we observe a significant drop in performance around step 51. Inspired by DAPO [yu2025dapoopensourcellmreinforcement](https://arxiv.org/html/2510.24663v1#bib.bib35 ""), We hypothesize that the performance drop may be caused by a low-entropy situation, where the model becomes overly confident and thus fails to explore sufficiently.

https://arxiv.org/html/2510.24663v1/x3.pngFigure 3: Performance and Entropy Analysis with DAPO and GRPO

After applying DAPO, we observe that the performance collapse no longer occurs, and the entropy remains at a relatively higher level in the later stages of training.

## 5 CONCLUSION

In summary, we introduce OrchDAG, a synthetic multi-turn data generation pipeline that models tool execution as DAGs with controllable complexity. Leveraging this dataset, we evaluate model performance and propose a graph-based reward to enhance RLVR training. Extensive experiments validate the effectiveness of our approach, underscoring the importance of exploiting the topological structure of tool execution graphs and managing data complexity in multi-turn tool use.

Nonetheless, our method remains limited in that it does not yet address multi-turn scenarios involving implicit dependencies, such as file operations in computer-use tasks. In future work, we aim to extend our framework to capture these implicit dependency cases.

## References

- (1)↑
Victor Barres, Honghua Dong, Soham Ray, Xujie Si, and Karthik Narasimhan.

τ2\\tau^{2}-bench: Evaluating conversational agents in a dual-control environment, 2025.

- (2)↑
Akhiad Bercovich, Itay Levy, Izik Golan, Mohammad Dabbah, Ran El-Yaniv, Omri Puny, Ido Galil, Zach Moshe, Tomer Ronen, Najeeb Nabwani, Ido Shahaf, Oren Tropp, Ehud Karpas, Ran Zilberstein, Jiaqi Zeng, Soumye Singhal, Alexander Bukharin, Yian Zhang, Tugrul Konuk, Gerald Shen, Ameya Sunil Mahabaleshwarkar, Bilal Kartal, Yoshi Suhara, Olivier Delalleau, Zijia Chen, Zhilin Wang, David Mosallanezhad, Adi Renduchintala, Haifeng Qian, Dima Rekesh, Fei Jia, Somshubra Majumdar, Vahid Noroozi, Wasi Uddin Ahmad, Sean Narenthiran, Aleksander Ficek, Mehrzad Samadi, Jocelyn Huang, Siddhartha Jain, Igor Gitman, Ivan Moshkov, Wei Du, Shubham Toshniwal, George Armstrong, Branislav Kisacanin, Matvei Novikov, Daria Gitman, Evelina Bakhturina, Prasoon Varshney, Makesh Narsimhan, Jane Polak Scowcroft, John Kamalu, Dan Su, Kezhi Kong, Markus Kliegl, Rabeeh Karimi, Ying Lin, Sanjeev Satheesh, Jupinder Parmar, Pritam Gundecha, Brandon Norick, Joseph Jennings, Shrimai Prabhumoye, Syeda Nahida Akter, Mostofa Patwary, Abhinav Khattar,
Deepak Narayanan, Roger Waleffe, Jimmy Zhang, Bor-Yiing Su, Guyue Huang, Terry Kong, Parth Chadha, Sahil Jain, Christine Harvey, Elad Segal, Jining Huang, Sergey Kashirsky, Robert McQueen, Izzy Putterman, George Lam, Arun Venkatesan, Sherry Wu, Vinh Nguyen, Manoj Kilaru, Andrew Wang, Anna Warno, Abhilash Somasamudramath, Sandip Bhaskar, Maka Dong, Nave Assaf, Shahar Mor, Omer Ullman Argov, Scot Junkin, Oleksandr Romanenko, Pedro Larroy, Monika Katariya, Marco Rovinelli, Viji Balas, Nicholas Edelman, Anahita Bhiwandiwalla, Muthu Subramaniam, Smita Ithape, Karthik Ramamoorthy, Yuting Wu, Suguna Varshini Velury, Omri Almog, Joyjit Daw, Denys Fridman, Erick Galinkin, Michael Evans, Shaona Ghosh, Katherine Luna, Leon Derczynski, Nikki Pope, Eileen Long, Seth Schneider, Guillermo Siman, Tomasz Grzegorzek, Pablo Ribalta, Monika Katariya, Chris Alexiuk, Joey Conway, Trisha Saar, Ann Guan, Krzysztof Pawelec, Shyamala Prayaga, Oleksii Kuchaiev, Boris Ginsburg, Oluwatobi Olabiyi, Kari Briski, Jonathan Cohen, Bryan
Catanzaro, Jonah Alben, Yonatan Geifman, and Eric Chung.

Llama-nemotron: Efficient reasoning models, 2025.

- (3)↑
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Clemens Winter, Christopher Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christopher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei.

Language models are few-shot learners, 2020.

- (4)↑
Chen Chen, Xinlong Hao, Weiwen Liu, Xu Huang, Xingshan Zeng, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Yuefeng Huang, Wulong Liu, Xinzhi Wang, Defu Lian, Baoqun Yin, Yasheng Wang, and Wu Liu.

Acebench: Who wins the match point in tool usage?, 2025.

- (5)↑
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, Parker Schuh, Kensen Shi, Sasha Tsvyashchenko, Joshua Maynez, Abhishek Rao, Parker Barnes, Yi Tay, Noam Shazeer, Vinodkumar Prabhakaran, Emily Reif, Nan Du, Ben Hutchinson, Reiner Pope, James Bradbury, Jacob Austin, Michael Isard, Guy Gur-Ari, Pengcheng Yin, Toju Duke, Anselm Levskaya, Sanjay Ghemawat, Sunipa Dev, Henryk Michalewski, Xavier Garcia, Vedant Misra, Kevin Robinson, Liam Fedus, Denny Zhou, Daphne Ippolito, David Luan, Hyeontaek Lim, Barret Zoph, Alexander Spiridonov, Ryan Sepassi, David Dohan, Shivani Agrawal, Mark Omernick, Andrew M. Dai, Thanumalayan Sankaranarayana Pillai, Marie Pellat, Aitor Lewkowycz, Erica Moreira, Rewon Child, Oleksandr Polozov, Katherine Lee, Zongwei Zhou, Xuezhi Wang, Brennan Saeta, Mark Diaz, Orhan Firat, Michele Catasta, Jason Wei, Kathy Meier-Hellstern, Douglas Eck, Jeff Dean, Slav Petrov, and Noah Fiedel.

Palm: Scaling language modeling with pathways.

Journal of Machine Learning Research, 24(240):1–113, 2023.

- (6)↑
DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong
Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu,
Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, and Zhen Zhang.

Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning, 2025.

- (7)↑
Lutfi Eren Erdogan, Nicholas Lee, Siddharth Jha, Sehoon Kim, Ryan Tabrizi, Suhong Moon, Coleman Hooper, Gopala Anumanchipalli, Kurt Keutzer, and Amir Gholami.

Tinyagent: Function calling at the edge, 2024.

- (8)↑
Lutfi Eren Erdogan, Nicholas Lee, Sehoon Kim, Suhong Moon, Hiroki Furuta, Gopala Anumanchipalli, Kurt Keutzer, and Amir Gholami.

Plan-and-act: Improving planning of agents for long-horizon tasks, 2025.

- (9)↑
Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An.

Group-in-group policy optimization for llm agent training, 2025.

- (10)↑
Xinbo Gao, Bing Xiao, Dacheng Tao, and Xuelong Li.

A survey of graph edit distance.

Pattern Anal. Appl., 13(1):113–129, February 2010.

- (11)↑
Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, and Yang Liu.

Stabletoolbench: Towards stable large-scale benchmarking on tool learning of large language models, 2024.

- (12)↑
Sehoon Kim, Suhong Moon, Ryan Tabrizi, Nicholas Lee, Michael W. Mahoney, Kurt Keutzer, and Amir Gholami.

An llm compiler for parallel function calling, 2024.

- (13)↑
Shengjie Liu, Alex Lu, Li Dong, Jason Zhu, Manish Gawali, and Alice Zhou.

Toposem: In-context planning with semantically-informed tooling graph similarity.

2025.

- (14)↑
Weiwen Liu, Xu Huang, Xingshan Zeng, Xinlong Hao, Shuai Yu, Dexun Li, Shuai Wang, Weinan Gan, Zhengying Liu, Yuanqing Yu, Zezhong Wang, Yuxian Wang, Wu Ning, Yutai Hou, Bin Wang, Chuhan Wu, Xinzhi Wang, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, and Enhong Chen.

Toolace: Winning the points of llm function calling, 2025.

- (15)↑
Yanming Liu, Xinyue Peng, Jiannan Cao, Shi Bo, Yuwei Zhang, Xuhong Zhang, Sheng Cheng, Xun Wang, Jianwei Yin, and Tianyu Du.

Tool-planner: Task planning with clusters across multiple tools, 2025.

- (16)↑
Zuxin Liu, Thai Hoang, Jianguo Zhang, Ming Zhu, Tian Lan, Shirley Kokane, Juntao Tan, Weiran Yao, Zhiwei Liu, Yihao Feng, Rithesh Murthy, Liangwei Yang, Silvio Savarese, Juan Carlos Niebles, Huan Wang, Shelby Heinecke, and Caiming Xiong.

Apigen: Automated pipeline for generating verifiable and diverse function-calling datasets, 2024.

- (17)↑
Chang Ma, Haiteng Zhao, Junlei Zhang, Junxian He, and Lingpeng Kong.

Non-myopic generation of language models for reasoning and planning, 2024.

- (18)↑
Shishir G. Patil, Huanzhi Mao, Charlie Cheng-Jie Ji, Fanjia Yan, Vishnu Suresh, Ion Stoica, and Joseph E. Gonzalez.

The berkeley function calling leaderboard (bfcl): From tool use to agentic evaluation of large language models.

In Forty-second International Conference on Machine Learning, 2025.

- (19)↑
Cheng Qian, Emre Can Acikgoz, Qi He, Hongru Wang, Xiusi Chen, Dilek Hakkani-Tür, Gokhan Tur, and Heng Ji.

Toolrl: Reward is all tool learning needs, 2025.

- (20)↑
Cheng Qian, Zuxin Liu, Akshara Prabhakar, Zhiwei Liu, Jianguo Zhang, Haolin Chen, Heng Ji, Weiran Yao, Shelby Heinecke, Silvio Savarese, Caiming Xiong, and Huan Wang.

Userbench: An interactive gym environment for user-centric agents, 2025.

- (21)↑
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, and Maosong Sun.

Toolllm: Facilitating large language models to master 16000+ real-world apis, 2023.

- (22)↑
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo.

Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024.

- (23)↑
Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu.

Hybridflow: A flexible and efficient rlhf framework.

In Proceedings of the Twentieth European Conference on Computer Systems, EuroSys ’25, page 1279–1297. ACM, March 2025.

- (24)↑
Saksham Sahai Srivastava and Vaneet Aggarwal.

A technical survey of reinforcement learning techniques for large language models, 2025.

- (25)↑
Kimi Team, Yifan Bai, Yiping Bao, Guanduo Chen, Jiahao Chen, Ningxin Chen, Ruijue Chen, Yanru Chen, Yuankun Chen, Yutian Chen, Zhuofu Chen, Jialei Cui, Hao Ding, Mengnan Dong, Angang Du, Chenzhuang Du, Dikang Du, Yulun Du, Yu Fan, Yichen Feng, Kelin Fu, Bofei Gao, Hongcheng Gao, Peizhong Gao, Tong Gao, Xinran Gu, Longyu Guan, Haiqing Guo, Jianhang Guo, Hao Hu, Xiaoru Hao, Tianhong He, Weiran He, Wenyang He, Chao Hong, Yangyang Hu, Zhenxing Hu, Weixiao Huang, Zhiqi Huang, Zihao Huang, Tao Jiang, Zhejun Jiang, Xinyi Jin, Yongsheng Kang, Guokun Lai, Cheng Li, Fang Li, Haoyang Li, Ming Li, Wentao Li, Yanhao Li, Yiwei Li, Zhaowei Li, Zheming Li, Hongzhan Lin, Xiaohan Lin, Zongyu Lin, Chengyin Liu, Chenyu Liu, Hongzhang Liu, Jingyuan Liu, Junqi Liu, Liang Liu, Shaowei Liu, T. Y. Liu, Tianwei Liu, Weizhou Liu, Yangyang Liu, Yibo Liu, Yiping Liu, Yue Liu, Zhengying Liu, Enzhe Lu, Lijun Lu, Shengling Ma, Xinyu Ma, Yingwei Ma, Shaoguang Mao, Jie Mei, Xin Men, Yibo Miao, Siyuan Pan, Yebo Peng, Ruoyu Qin, Bowen Qu, Zeyu
Shang, Lidong Shi, Shengyuan Shi, Feifan Song, Jianlin Su, Zhengyuan Su, Xinjie Sun, Flood Sung, Heyi Tang, Jiawen Tao, Qifeng Teng, Chensi Wang, Dinglu Wang, Feng Wang, Haiming Wang, Jianzhou Wang, Jiaxing Wang, Jinhong Wang, Shengjie Wang, Shuyi Wang, Yao Wang, Yejie Wang, Yiqin Wang, Yuxin Wang, Yuzhi Wang, Zhaoji Wang, Zhengtao Wang, Zhexu Wang, Chu Wei, Qianqian Wei, Wenhao Wu, Xingzhe Wu, Yuxin Wu, Chenjun Xiao, Xiaotong Xie, Weimin Xiong, Boyu Xu, Jing Xu, Jinjing Xu, L. H. Xu, Lin Xu, Suting Xu, Weixin Xu, Xinran Xu, Yangchuan Xu, Ziyao Xu, Junjie Yan, Yuzi Yan, Xiaofei Yang, Ying Yang, Zhen Yang, Zhilin Yang, Zonghan Yang, Haotian Yao, Xingcheng Yao, Wenjie Ye, Zhuorui Ye, Bohong Yin, Longhui Yu, Enming Yuan, Hongbang Yuan, Mengjie Yuan, Haobing Zhan, Dehao Zhang, Hao Zhang, Wanlu Zhang, Xiaobin Zhang, Yangkun Zhang, Yizhi Zhang, Yongting Zhang, Yu Zhang, Yutao Zhang, Yutong Zhang, Zheng Zhang, Haotian Zhao, Yikai Zhao, Huabin Zheng, Shaojie Zheng, Jianren Zhou, Xinyu Zhou, Zaida Zhou, Zhen Zhu,
Weiyu Zhuang, and Xinxing Zu.

Kimi k2: Open agentic intelligence, 2025.

- (26)↑
Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva, Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic, Sergey Edunov, and Thomas
Scialom.

Llama 2: Open foundation and fine-tuned chat models, 2023.

- (27)↑
Hongru Wang, Cheng Qian, Wanjun Zhong, Xiusi Chen, Jiahao Qiu, Shijue Huang, Bowen Jin, Mengdi Wang, Kam-Fai Wong, and Heng Ji.

Acting less is reasoning more! teaching model to act efficiently, 2025.

- (28)↑
Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji.

Executable code actions elicit better llm agents, 2024.

- (29)↑
Jiaxin Wen, Jian Guan, Hongning Wang, Wei Wu, and Minlie Huang.

Unlocking reasoning potential in large langauge models by scaling code-form planning, 2024.

- (30)↑
Binfeng Xu, Zhiyuan Peng, Bowen Lei, Subhabrata Mukherjee, Yuchen Liu, and Dongkuan Xu.

Rewoo: Decoupling reasoning from observations for efficient augmented language models, 2023.

- (31)↑
Ling Yang, Zhaochen Yu, Bin Cui, and Mengdi Wang.

Reasonflux: Hierarchical llm reasoning via scaling thought templates, 2025.

- (32)↑
Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan.

τ\\tau-bench: A benchmark for tool-agent-user interaction in real-world domains, 2024.

- (33)↑
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik Narasimhan.

Tree of thoughts: Deliberate problem solving with large language models, 2023.

- (34)↑
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao.

React: Synergizing reasoning and acting in language models, 2023.

- (35)↑
Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, Xin Liu, Haibin Lin, Zhiqi Lin, Bole Ma, Guangming Sheng, Yuxuan Tong, Chi Zhang, Mofan Zhang, Wang Zhang, Hang Zhu, Jinhua Zhu, Jiaze Chen, Jiangjie Chen, Chengyi Wang, Hongli Yu, Yuxuan Song, Xiangpeng Wei, Hao Zhou, Jingjing Liu, Wei-Ying Ma, Ya-Qin Zhang, Lin Yan, Mu Qiao, Yonghui Wu, and Mingxuan Wang.

Dapo: An open-source llm reinforcement learning system at scale, 2025.

- (36)↑
Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding, Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma, Yufei Xue, Jidong Zhai, Wenguang Chen, Peng Zhang, Yuxiao Dong, and Jie Tang.

Glm-130b: An open bilingual pre-trained model, 2023.

- (37)↑
Jianguo Zhang, Tian Lan, Ming Zhu, Zuxin Liu, Thai Hoang, Shirley Kokane, Weiran Yao, Juntao Tan, Akshara Prabhakar, Haolin Chen, Zhiwei Liu, Yihao Feng, Tulika Awalgaonkar, Rithesh Murthy, Eric Hu, Zeyuan Chen, Ran Xu, Juan Carlos Niebles, Shelby Heinecke, Huan Wang, Silvio Savarese, and Caiming Xiong.

xlam: A family of large action models to empower ai agent systems, 2024.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="react-agent-from-scratch-with-gemini-2-5-and-langgraph.md">
<details>
<summary>ReAct agent from scratch with Gemini 2.5 and LangGraph</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.philschmid.de/langgraph-gemini-2-5-react-agent>

# ReAct agent from scratch with Gemini 2.5 and LangGraph

AI applications are evolving from simple chatbots to (semi-)autonomous systems capable of complex reasoning, planning, and interaction with the real world. We call these system agents.

> An AI Agent is a system that uses LLMs to decide the control flow of an application.

Agents are not just theoretical concepts; they are and will be deployed in production across various verticals, tackling increasingly more complex and longer-running tasks. In this blog post, we'll explore how to create a ReAct agent using Google's Gemini 2.5 Pro or Gemini 2.0 Flash and LangGraph from scratch.

## What are ReAct Agents?

ReACT (Reasoning and Acting) Agents are AI systems that combine reasoning capabilities of LLMs with action execution, enabling them to iteratively think through problems, use tools, and act based on observations to achieve the user goals.

The ReAct pattern was first introduced in the [“ReAct: Synergizing Reasoning and Acting in Language Models”](https://arxiv.org/abs/2210.03629) in 2023. It was inspired by how humans plan and solve complex tasks, rather than implementing predefined workflows. ReAct agents rely on the LLM's reasoning capabilities to dynamically adjust their actions based on new information or the results of previous steps.

ReACT Agents have gained traction due to their ability to handle complex tasks by breaking them into manageable reasoning steps and leveraging external tools.

https://www.philschmid.de/static/blog/langgraph-gemini-2-5-react-agent/react.png

The ReAct agent:

1. Takes a user **query** as input
2. Reasons about the query and decides on an action
3. Executes the chosen action using available tools
4. Observes the result of the action
5. Repeats steps 2-4 until it can provide a final answer

### The First ReAct Agents

These first-generation ReAct agents used a simple but effective prompting technique to generate a chain of "Thought, Action, Observation" steps:

- "Thought" component plans the next action or decide it knows the final answer
- "Action" interacts with external resources (like search engines or calculators).
- "Observation" incorporates the results from the action into the reasoning process.

Here's a pseudo-code example demonstrating the flow of an early ReAct agent.

```
User: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?

Thought: I need to find out who Olivia Wilde's boyfriend is and then calculate his age raised to the 0.23 power.
Action: [search("Olivia Wilde boyfriend")]
Observation: Olivia Wilde started dating Harry Styles after ending her years-long engagement to Jason Sudeikis — see their relationship timeline.

Thought: I need to find out Harry Styles' age.
Action: [search("Harry Styles age")]
Observation: 29 years

Thought: I need to calculate 29 raised to the 0.23 power.
Action: [calculator(29^0.23)]
Observation: Answer: 2.169459462491557

Thought: I now know the final answer.
Final Answer: Harry Styles, Olivia Wilde's boyfriend, is 29 years old and his age raised to the 0.23 power is 2.169459462491557.
```

### Current ReAct Agents

Since the introduction of ReAct Agent the capabilities of LLMs has evolved. One of the most important improvements we made is function calling. Function calling allows us to to connect LLMs to external tools in a structured way, which is more reliable than parsing raw text and reduces the likelihood of errors and hallucinations.

Here's a pseudo-code example demonstrating the flow of an ReAct agent using function calling

```
User: Who is Olivia Wilde's boyfriend? What is his current age raised to the 0.23 power?

Assistant: FunctionCall(name="search", args={"query": "Olivia Wilde boyfriend"})
User: FunctionResponse(result="Olivia Wilde started dating Harry Styles after ending her years-long engagement to Jason Sudeikis — see their relationship timeline.")

Assistant: FunctionCall(name="search", args={"query": "Harry Styles age"})
User: FunctionResponse(result="29 years")

Assistant: FunctionCall(name="calculator", args={"expression": "29^0.23"})
User: FunctionResponse(result="2.169459462491557")

Assistant: Harry Styles, Olivia Wilde's boyfriend, is 29 years old. His age raised to the 0.23 power is 2.169459462491557.
```

### Traditional ReAct Agents vs. Current ReAct Agents (Function Calling)

| **Aspect** | **Traditional ReAct Agents** | **Current ReAct Agents (Function Calling)** |
| --- | --- | --- |
| Actions | Text-based description, parsed by system | Direct function calls in structured format |
| Efficiency | Lower, due to parsing errors | Higher, with reduced parsing overhead |
| Reliability | More prone to errors and hallucinations | More reliable and accurate tool execution |
| LLM Requirement | Works with any LLM | Requires LLMs supporting function calling |
| Implementation | Primarily through careful prompt engineering | Often facilitated by SDKs and frameworks like LangGraph |

## How to create a ReAct agent from scratch with LangGraph

We know have base understanding on how ReAct agents work. Now, let's build our own from scratch. We are going to use LangGraph and Gemini 2.5 Pro. LangGraph is framework for building controllable agents. LangGraph comes already with prebuilt ReAct agent [create\_react\_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent), but sometimes you might want more control and customization.
Additionally, It is good to understand the underlying concepts and how to build your own ReAct agent from scratch.

LangGraph models agent as graphs. You define the behavior of agents using three key components:

- `State`: Shared data structure that represents the current snapshot of your application. It can be any Python type, but is typically a TypedDict or Pydantic BaseModel, which is shared across all nodes.
- `Nodes`: Encodes logic of your agents. They receive the current State as input, perform some computation or side-effect, and return an updated State, e.g. LLM calls, tool calls, etc.
- `Edges`: Determine which Node to execute next based on the current State. They can be conditional branches or fixed transitions.

First, we installed required packages and set our API keys. If you don't have an API Key yet you can get one for free in the [Google AI Studio](https://aistudio.google.com/app/apikey).

```
%pip install langgraph langchain-google-genai geopy requests
```

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY","xxx")
```

We are going to create the most basic ReAct agents, which uses mocked 1 tool to retrieve the weather for a given location. For this we need to store the conversation history as a list of messages in our graph state. We are going to use the [add\_messages](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.message.add_messages) helper function to add messages to the state. The `add_messages` function is a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers) that merges two lists of messages, updating existing messages by ID and ensures the state is "append-only", unless the new message has the same ID as an existing message. For demonstration purposes we also store the number of steps in the state.

Note: Since having a list of messages in the state is so common, there exists a prebuilt state called `MessagesState` which makes it easy to use messages.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages # helper function to add messages to the state


class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Next, we define our weather tool.

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API for a given location (city) and a date (yyyy-mm-dd). Returns a list dictionary with the time and temperature for each hour."""
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

tools = [get_weather_forecast]
```

Next, we initalize our model and bind the tools to the model.

```
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-2.5-pro-exp-03-25", # replace with "gemini-2.0-flash"
    temperature=1.0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
model.invoke("What is the weather in Berlin on 12th of March 2025?")
```

The last step before we can run our agent is to define our nodes and edges. In our examples we have two nodes and 1 edge.

- `call_tool` node that executes our tool method. LangGraph has a prebuilt node for this called [ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- `call_model` node that uses the `model_with_tools` to call the model.
- `should_continue` edge that decides whether to call the tool or the model.

The number of nodes and edges is not fixed. You can add as many nodes and edges as you want to your graph. For example, you could add a node for adding structured output or self-verification/reflection node to check the model output before calling the tool or the model.

```
import json
from langchain_core.messages import ToolMessage, SystemMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# this is similar to customizing the create_react_agent with 'prompt' parameter, but is more flexible
# system_prompt = SystemMessage(
#     "You are a helpful assistant that use tools to access and retrieve information from a weather API. Today is 2025-03-04. Help the user with their questions. Use the history to answer the question."
# )

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # We return a list, because this will get added to the existing messages state using the add_messages reducer
    return {"messages": [response]}


# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then we finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

Awesome, now we have all the components to build our agent. Let's put them together.

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add our nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return, and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

We can visualize our graph using the `draw_mermaid_png` method.

```

from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

https://www.philschmid.de/static/blog/langgraph-gemini-2-5-react-agent/langgraph-react-agent_16_0.png

Awesome, now lets our agent.

```
# Create our initial message dictionary
inputs = {"messages": [("user", "How is the weather in Berlin on 12th of March 2025?")]}

# call our graph with streaming to see the steps

for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

Result:

```
================================ [1m Human Message  [0m=================================\
\
How is the weather in Berlin on 12th of March 2025?\
================================== [1m Ai Message  [0m==================================\
Tool Calls:\
    get_weather_forecast (162a0f9f-352f-4b06-b6be-e071d6eee35b)\
    Call ID: 162a0f9f-352f-4b06-b6be-e071d6eee35b\
    Args:\
    date: 2025-03-12\
    location: Berlin\
================================= [1m Tool Message  [0m=================================\
Name: get_weather_forecast\
\
{'2025-03-12T00:00': 4.5, '2025-03-12T01:00': 4.5, '2025-03-12T02:00': 4.8, '2025-03-12T03:00': 5.2, '2025-03-12T04:00': 5.2, '2025-03-12T05:00': 5.1, '2025-03-12T06:00': 5.0, '2025-03-12T07:00': 5.1, '2025-03-12T08:00': 5.6, '2025-03-12T09:00': 6.2, '2025-03-12T10:00': 7.0, '2025-03-12T11:00': 7.3, '2025-03-12T12:00': 7.5, '2025-03-12T13:00': 7.8, '2025-03-12T14:00': 8.2, '2025-03-12T15:00': 8.1, '2025-03-12T16:00': 7.9, '2025-03-12T17:00': 7.6, '2025-03-12T18:00': 7.1, '2025-03-12T19:00': 6.9, '2025-03-12T20:00': 5.5, '2025-03-12T21:00': 6.0, '2025-03-12T22:00': 5.0, '2025-03-12T23:00': 4.7}\
================================== [1m Ai Message  [0m==================================\
\
OK. Here is the weather forecast for Berlin on March 12th, 2025:\
\
The temperature will range from 4.5°C in the early morning to a high of 8.2°C in the afternoon. Temperatures will start around 4.5°C at midnight, rise through the morning to reach the peak in the early afternoon (around 2 PM), and then cool down again in the evening, dropping to around 4.7°C by 11 PM.\
```\
\
We can now continue with our conversation and for example ask for the weather in another city or let it compare it.\
\
```\
state["messages"].append(("user", "Would it be in Munich warmer?"))\
\
\
for state in graph.stream(state, stream_mode="values"):\
    last_message = state["messages"][-1]\
    last_message.pretty_print()\
```\
\
Result:\
\
```\
================================ [1m Human Message  [0m=================================\
\
Would it be in Munich warmer?\
================================== [1m Ai Message  [0m==================================\
Tool Calls:\
    get_weather_forecast (1736dcae-c173-4b90-8c07-3751b6fd848d)\
    Call ID: 1736dcae-c173-4b90-8c07-3751b6fd848d\
    Args:\
    date: 2025-03-12\
    location: Munich\
================================= [1m Tool Message  [0m=================================\
Name: get_weather_forecast\
\
{'2025-03-12T00:00': 5.3, '2025-03-12T01:00': 5.0, '2025-03-12T02:00': 4.7, '2025-03-12T03:00': 3.8, '2025-03-12T04:00': 3.5, '2025-03-12T05:00': 3.4, '2025-03-12T06:00': 3.5, '2025-03-12T07:00': 4.5, '2025-03-12T08:00': 4.9, '2025-03-12T09:00': 5.7, '2025-03-12T10:00': 6.6, '2025-03-12T11:00': 8.0, '2025-03-12T12:00': 9.2, '2025-03-12T13:00': 10.1, '2025-03-12T14:00': 10.6, '2025-03-12T15:00': 9.9, '2025-03-12T16:00': 9.6, '2025-03-12T17:00': 9.3, '2025-03-12T18:00': 8.9, '2025-03-12T19:00': 8.2, '2025-03-12T20:00': 7.5, '2025-03-12T21:00': 6.9, '2025-03-12T22:00': 6.3, '2025-03-12T23:00': 5.6}\
================================== [1m Ai Message  [0m==================================\
\
Yes, it looks like Munich will be warmer than Berlin on March 12th, 2025, especially during the afternoon.\
\
*   **Munich:** The temperature is expected to reach a high of about 10.6°C around 2 PM. The lowest temperature will be around 3.4°C in the early morning.\
*   **Berlin:** The high is predicted to be 8.2°C, also around 2 PM, with a low of 4.5°C.\
\
So, while Munich might start a bit colder in the very early morning, its daytime high will be noticeably warmer than Berlin's.\
```\
\
## Conclusion\
\
Building ReAct agents with LangGraph and Gemini 2.5 Pro or Gemini 2.0 Flash enables Developers to build production-ready agents with the flexibility to customize the control flow and the reliability to execute complex tasks.\

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/08_react_practice/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
Branch: dev
File: notebook.ipynb
Lines: 579

Estimated tokens: 4.8k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/08_react_practice/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 8: ReAct Practice

This notebook explores practical ReAct (Reasoning and Acting) with Google's Gemini. We will use the `google-genai` library to interact with Gemini models. It includes a mock search tool, a thought generation phase using structured outputs, and an action phase with function calling, all orchestrated by a ReAct control loop.
"""

"""
**Learning Objectives:**

1. Understand how ReAct breaks problems into Thought → Action → Observation.
2. Practice orchestrating the full ReAct loop end-to-end.
"""

"""
## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:
"""

%load_ext autoreload
%autoreload 2

"""
### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.
"""

"""
### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the `Course Admin` lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:
"""

from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/fabio/Desktop/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

from enum import Enum
from pydantic import BaseModel, Field
from typing import List

from google import genai
from google.genai import types

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()
# Output:
#   Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.


"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast and cost-effective:
"""

MODEL_ID = "gemini-2.5-flash"

"""
## 2. Tools Definition

Let's implement our mock search tool that will serve as the external knowledge source for our agent. This simplified version focuses on the ReAct mechanics rather than real API integration:
"""

def search(query: str) -> str:
    """Search for information about a specific topic or query.

    Args:
        query (str): The search query or topic to look up.
    """
    query_lower = query.lower()

    # Predefined responses for demonstration
    if all(word in query_lower for word in ["capital", "france"]):
        return "Paris is the capital of France and is known for the Eiffel Tower."
    elif "react" in query_lower:
        return "The ReAct (Reasoning and Acting) framework enables LLMs to solve complex tasks by interleaving thought generation, action execution, and observation processing."

    # Generic response for unhandled queries
    return f"Information about '{query}' was not found."

"""
We maintain a mapping from tool name to tool function (the tool registry). This lets the model plan with symbolic tool names, while our code safely resolves those names to actual Python functions to execute.
"""

TOOL_REGISTRY = {
    search.__name__: search,
}

"""
## 3. ReAct Thought Phase

Now let's implement the thought generation phase. This component analyzes the current situation and determines what the agent should do next, potentially suggesting using tools.
"""

"""
First, we prepare the prompt for the thinking part. We implement a function that converts the `TOOL_REGISTRY` to a string XML representation of it, which we insert into the prompt. This way, the LLM knows which tools available and can reason around them.
"""

def build_tools_xml_description(tools: dict[str, callable]) -> str:
    """Build a minimal XML description of tools using only their docstrings."""
    lines = []
    for tool_name, fn in tools.items():
        doc = (fn.__doc__ or "").strip()
        lines.append(f"\t<tool name=\"{tool_name}\">")
        if doc:
            lines.append(f"\t\t<description>")
            for line in doc.split("\n"):
                lines.append(f"\t\t\t{line}")
            lines.append(f"\t\t</description>")
        lines.append("\t</tool>")
    return "\n".join(lines)

tools_xml = build_tools_xml_description(TOOL_REGISTRY)

PROMPT_TEMPLATE_THOUGHT = f"""
You are deciding the next best step for reaching the user goal. You have some tools available to you.

Available tools:
<tools>
{tools_xml}
</tools>

Conversation so far:
<conversation>
{{conversation}}
</conversation>

State your next thought about what to do next as one short paragraph focused on the next action you intend to take and why.
Avoid repeating the same strategies that didn't work previously. Prefer different approaches.
""".strip()

"""
Here we `print` the full prompt with the tool definitions inside.
"""

print(PROMPT_TEMPLATE_THOUGHT)
# Output:
#   You are deciding the next best step for reaching the user goal. You have some tools available to you.

#   

#   Available tools:

#   <tools>

#   	<tool name="search">

#   		<description>

#   			Search for information about a specific topic or query.

#   			

#   			Args:

#   			    query (str): The search query or topic to look up.

#   		</description>

#   	</tool>

#   </tools>

#   

#   Conversation so far:

#   <conversation>

#   {conversation}

#   </conversation>

#   

#   State your next thought about what to do next as one short paragraph focused on the next action you intend to take and why.

#   Avoid repeating the same strategies that didn't work previously. Prefer different approaches.


"""
We can now implement the `generate_thought` function, which reasons on the best next action to take according to the conversation history.
"""

def generate_thought(conversation: str, tool_registry: dict[str, callable]) -> str:
    """Generate a thought as plain text (no structured output)."""
    tools_xml = build_tools_xml_description(tool_registry)
    prompt = PROMPT_TEMPLATE_THOUGHT.format(conversation=conversation, tools_xml=tools_xml)

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt
    )
    return response.text.strip()

"""
## 4. ReAct Action Phase
"""

"""
Next, let's implement the action phase using function calling. This component determines whether to use a tool or provide a final answer.
"""

PROMPT_TEMPLATE_ACTION = """
You are selecting the best next action to reach the user goal.

Conversation so far:
<conversation>
{conversation}
</conversation>

Respond either with a tool call (with arguments) or a final answer if you can confidently conclude.
""".strip()

# Dedicated prompt used when we must force a final answer
PROMPT_TEMPLATE_ACTION_FORCED = """
You must now provide a final answer to the user.

Conversation so far:
<conversation>
{conversation}
</conversation>

Provide a concise final answer that best addresses the user's goal.
""".strip()


class ToolCallRequest(BaseModel):
    """A request to call a tool with its name and arguments."""
    tool_name: str = Field(description="The name of the tool to call.")
    arguments: dict = Field(description="The arguments to pass to the tool.")


class FinalAnswer(BaseModel):
    """A final answer to present to the user when no further action is needed."""
    text: str = Field(description="The final answer text to present to the user.")


def generate_action(conversation: str, tool_registry: dict[str, callable] | None = None, force_final: bool = False) -> (ToolCallRequest | FinalAnswer):
    """Generate an action by passing tools to the LLM and parsing function calls or final text.

    When force_final is True or no tools are provided, the model is instructed to produce a final answer and tool calls are disabled.
    """
    # Use a dedicated prompt when forcing a final answer or no tools are provided
    if force_final or not tool_registry:
        prompt = PROMPT_TEMPLATE_ACTION_FORCED.format(conversation=conversation)
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        return FinalAnswer(text=response.text.strip())

    # Default action prompt
    prompt = PROMPT_TEMPLATE_ACTION.format(conversation=conversation)

    # Provide the available tools to the model; disable auto-calling so we can parse and run ourselves
    tools = list(tool_registry.values())
    config = types.GenerateContentConfig(
        tools=tools,
        automatic_function_calling={"disable": True}
    )
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=config
    )

    # Extract the function call from the response (if present)
    candidate = response.candidates[0]
    parts = candidate.content.parts
    if parts and getattr(parts[0], "function_call", None):
        name = parts[0].function_call.name
        args = dict(parts[0].function_call.args) if parts[0].function_call.args is not None else {}
        return ToolCallRequest(tool_name=name, arguments=args)
    
    # Otherwise, it's a final answer
    final_answer = "".join(part.text for part in candidate.content.parts)
    return FinalAnswer(text=final_answer.strip())

"""
Why we provide an option to force the final answer? In a ReAct loop we sometimes need to terminate cleanly after a budget of turns (e.g., to avoid infinite loops or excessive tool calls). The force flag lets us ask the model to conclude with a final answer even if, under normal conditions, it might keep calling tools. This ensures graceful shutdown and a usable output at the end of the loop.
"""

"""
Note: In the Action phase we do not inline tool descriptions into the prompt (unlike the Thought phase). Instead, we pass the available Python tool functions through the `tools` parameter to `generate_content`. The client automatically parses these tools and incorporates their definitions/arguments into the model's prompt context, enabling function calling without duplicating tool specs in our prompt text.
"""

"""
## 5. ReAct Control Loop
"""

"""
Now we build the main ReAct control loop that orchestrates the Thought → Action → Observation cycle end-to-end. We treat the conversation between the user and the agent as a sequence of messages. Each message is a step in the dialogue, and each step corresponds to one ReAct unit: it can be a user message, an internal thought, a tool request, the tool's observation, or the final answer.

We'll start by defining the data structures for these messages.
"""

class MessageRole(str, Enum):
    """Enumeration for the different roles a message can have."""
    USER = "user"
    THOUGHT = "thought"
    TOOL_REQUEST = "tool request"
    OBSERVATION = "observation"
    FINAL_ANSWER = "final answer"


class Message(BaseModel):
    """A message with a role and content, used for all message types."""
    role: MessageRole = Field(description="The role of the message in the ReAct loop.")
    content: str = Field(description="The textual content of the message.")

    def __str__(self) -> str:
        """Provides a user-friendly string representation of the message."""
        return f"{self.role.value.capitalize()}: {self.content}"

"""
We also add a small printer that uses our `pretty_print` module to render each message nicely in the notebook. This makes it easy to follow how the agent alternates between Thought, Action (tool call), and Observation across turns.
"""

def pretty_print_message(message: Message, turn: int, max_turns: int, header_color: str = pretty_print.Color.YELLOW, is_forced_final_answer: bool = False) -> None:
    if not is_forced_final_answer:
        title = f"{message.role.value.capitalize()} (Turn {turn}/{max_turns}):"
    else:
        title = f"{message.role.value.capitalize()} (Forced):"

    pretty_print.wrapped(
        text=message.content,
        title=title,
        header_color=header_color,
    )

"""
We now use a `Scratchpad` class that wraps a list of `Message` objects and provides `append(..., verbose=False)` to both store and (optionally) pretty-print messages with role-based colors. The scratchpad is serialized each turn so the model can plan the next step.
"""

class Scratchpad:
    """Container for ReAct messages with optional pretty-print on append."""

    def __init__(self, max_turns: int) -> None:
        self.messages: List[Message] = []
        self.max_turns: int = max_turns
        self.current_turn: int = 1

    def set_turn(self, turn: int) -> None:
        self.current_turn = turn

    def append(self, message: Message, verbose: bool = False, is_forced_final_answer: bool = False) -> None:
        self.messages.append(message)
        if verbose:
            role_to_color = {
                MessageRole.USER: pretty_print.Color.RESET,
                MessageRole.THOUGHT: pretty_print.Color.ORANGE,
                MessageRole.TOOL_REQUEST: pretty_print.Color.GREEN,
                MessageRole.OBSERVATION: pretty_print.Color.YELLOW,
                MessageRole.FINAL_ANSWER: pretty_print.Color.CYAN,
            }
            header_color = role_to_color.get(message.role, pretty_print.Color.YELLOW)
            pretty_print_message(
                message=message,
                turn=self.current_turn,
                max_turns=self.max_turns,
                header_color=header_color,
                is_forced_final_answer=is_forced_final_answer,
            )

    def to_string(self) -> str:
        return "\n".join(str(m) for m in self.messages)

"""
We can now implement the control loop.
- On the first turn, we add the user question.
- Then, at each turn: (1) we get a Thought from the model; (2) we get an Action. If the action is a `FinalAnswer`, we stop. If it's a `ToolCallRequest`, we execute the tool and append the resulting `Observation`, then continue. If we reach the maximum number of turns, we run the action selector one last time with a flag that forces a final answer (no tool calls).
"""

def react_agent_loop(initial_question: str, tool_registry: dict[str, callable], max_turns: int = 5, verbose: bool = False) -> str:
    """
    Implements the main ReAct (Thought -> Action -> Observation) control loop.
    Uses a unified message class for the scratchpad.
    """
    scratchpad = Scratchpad(max_turns=max_turns)

    # Add the user's question to the scratchpad
    user_message = Message(role=MessageRole.USER, content=initial_question)
    scratchpad.append(user_message, verbose=verbose)

    for turn in range(1, max_turns + 1):
        scratchpad.set_turn(turn)

        # Generate a thought based on the current scratchpad
        thought_content = generate_thought(
            scratchpad.to_string(),
            tool_registry,
        )
        thought_message = Message(role=MessageRole.THOUGHT, content=thought_content)
        scratchpad.append(thought_message, verbose=verbose)

        # Generate an action based on the current scratchpad
        action_result = generate_action(
            scratchpad.to_string(),
            tool_registry=tool_registry,
        )

        # If the model produced a final answer, return it
        if isinstance(action_result, FinalAnswer):
            final_answer = action_result.text
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message, verbose=verbose)
            return final_answer

        # Otherwise, it is a tool request
        if isinstance(action_result, ToolCallRequest):
            action_name = action_result.tool_name
            action_params = action_result.arguments

            # Add the action to the scratchpad
            params_str = ", ".join([f"{k}='{v}'" for k, v in action_params.items()])
            action_content = f"{action_name}({params_str})"
            action_message = Message(role=MessageRole.TOOL_REQUEST, content=action_content)
            scratchpad.append(action_message, verbose=verbose)

            # Run the action and get the observation
            observation_content = ""
            tool_function = tool_registry[action_name]
            try:
                observation_content = tool_function(**action_params)
            except Exception as e:
                observation_content = f"Error executing tool '{action_name}': {e}"

            # Add the observation to the scratchpad
            observation_message = Message(role=MessageRole.OBSERVATION, content=observation_content)
            scratchpad.append(observation_message, verbose=verbose)

        # Check if the maximum number of turns has been reached. If so, force the action selector to produce a final answer
        if turn == max_turns:
            forced_action = generate_action(
                scratchpad.to_string(),
                force_final=True,
            )
            if isinstance(forced_action, FinalAnswer):
                final_answer = forced_action.text
            else:
                final_answer = "Unable to produce a final answer within the allotted turns."
            final_message = Message(role=MessageRole.FINAL_ANSWER, content=final_answer)
            scratchpad.append(final_message, verbose=verbose, is_forced_final_answer=True)
            return final_answer

"""
Let's test our ReAct agent with a simple factual question that requires a search:
"""

# A straightforward question requiring a search.
question = "What is the capital of France?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
# Output:
#   [0m----------------------------------------- User (Turn 1/2): -----------------------------------------[0m

#     What is the capital of France?

#   [0m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 1/2): ---------------------------------------[0m

#     I need to find the capital of France to answer the user's question. The `search` tool can be used to retrieve this factual information.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 1/2): -------------------------------------[0m

#     search(query='capital of France')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 1/2): -------------------------------------[0m

#     Paris is the capital of France and is known for the Eiffel Tower.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 2/2): ---------------------------------------[0m

#     I have successfully found the capital of France using the search tool. The next step is to communicate this answer to the user.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [96m------------------------------------- Final answer (Turn 2/2): -------------------------------------[0m

#     Paris is the capital of France.

#   [96m----------------------------------------------------------------------------------------------------[0m


"""
Last, let's test it with a question that our mock search tool doesn't have knowledge about:
"""

# A question about a concept the mock search tool doesn't know.
question = "What is the capital of Italy?"
final_answer = react_agent_loop(question, TOOL_REGISTRY, max_turns=2, verbose=True)
# Output:
#   [0m----------------------------------------- User (Turn 1/2): -----------------------------------------[0m

#     What is the capital of Italy?

#   [0m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 1/2): ---------------------------------------[0m

#     I need to find the capital of Italy to answer the user's question. The `search` tool can provide this information efficiently.I will use the `search` tool to find the capital of Italy.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 1/2): -------------------------------------[0m

#     search(query='capital of Italy')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 1/2): -------------------------------------[0m

#     Information about 'capital of Italy' was not found.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [38;5;208m--------------------------------------- Thought (Turn 2/2): ---------------------------------------[0m

#     The previous search query "capital of Italy" did not return information, which is unexpected for a common fact. I will try a broader search query like "Italy" to see if more general information or a list of facts about Italy can provide the capital, as the tool might respond better to less specific phrasing or have had a temporary issue with the exact previous query.I will try a broader search query like "Italy" to see if more general information or a list of facts about Italy can provide the capital, as the tool might respond better to less specific phrasing or have had a temporary issue with the exact previous query.

#   [38;5;208m----------------------------------------------------------------------------------------------------[0m

#   [92m------------------------------------- Tool request (Turn 2/2): -------------------------------------[0m

#     search(query='Italy')

#   [92m----------------------------------------------------------------------------------------------------[0m

#   [93m------------------------------------- Observation (Turn 2/2): -------------------------------------[0m

#     Information about 'Italy' was not found.

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [96m-------------------------------------- Final answer (Forced): --------------------------------------[0m

#     I'm sorry, but I couldn't find information about the capital of Italy.

#   [96m----------------------------------------------------------------------------------------------------[0m


"""
Notice how the ReAct agent tried different strategies to find an answer for the user query, demonstrating live adaptation.
"""

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>AI Agent Planning - IBM</summary>

# AI Agent Planning - IBM

**Source URL:** <https://www.ibm.com/think/topics/ai-agent-planning>

- [What is AI agent planning?](https://www.ibm.com/think/topics/ai-agent-planning#What+is+AI+agent+planning%3F)
- [How AI agent planning works](https://www.ibm.com/think/topics/ai-agent-planning#How+AI+agent+planning+works)
- [After planning](https://www.ibm.com/think/topics/ai-agent-planning#After+planning)

By

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

## What is AI agent planning?

AI agent planning refers to the process by which an artificial intelligence (AI) agent determines a sequence of actions to achieve a specific goal. It involves decision-making, goal prioritization and action sequencing, often using various planning algorithms and frameworks.

[AI agent](https://www.ibm.com/think/topics/ai-agents) planning is a [module common to many types of agents](https://www.ibm.com/think/topics/components-of-ai-agents) that exists alongside other modules such as perception, reasoning, decision-making, action, memory, communication and learning. Planning works in conjunction with these other modules to help ensure that agents achieve outcomes desired by their designers.

Not all agents can plan. Unlike simple reactive agents that respond immediately to inputs, planning agents anticipate future states and generate a structured action plan before execution. This makes AI planning essential for [automation](https://www.ibm.com/think/topics/enterprise-automation) tasks that require multistep decision-making, optimization and adaptability.

## How AI agent planning works

Advances in [large language models](https://www.ibm.com/think/topics/large-language-models) (LLMs) such as OpenAI’s [GPT](https://www.ibm.com/think/topics/gpt) and related techniques involving [machine learning algorithms](https://www.ibm.com/think/topics/machine-learning-algorithms) resulted in the [generative AI](https://www.ibm.com/think/topics/generative-ai) (gen AI) boom of recent years, and further advancements have led to the emerging field of autonomous agents.

By integrating tools, APIs, hardware interfaces and other external resources, agentic AI systems are increasingly autonomous, capable of real-time decision-making and adept at problem-solving across various use cases.

Complex agents can’t act without making a decision, and they can’t make good decisions without first making a plan. Agentic planning consists of several key components that work together to encourage optimal decision-making.

### Goal definition

The first and most critical step in AI planning is defining a clear objective. The goal serves as the guiding principle for the agent’s decision-making process, determining the end state it seeks to achieve. Goals can either be static, remaining unchanged throughout the planning process, or dynamic, adjusting based on environmental conditions or user interactions.

For instance, a self-driving car might have a goal of reaching a specific destination efficiently while adhering to safety regulations. Without a well-defined goal, an agent would lack direction, leading to erratic or inefficient behavior.

If the goal is complex, agentic [AI models](https://www.ibm.com/think/topics/ai-model) will break it down into smaller, more manageable sub-goals in a process called task decomposition. This allows the system to focus on complex tasks in a hierarchical manner.

LLMs play a vital role in task decomposition, breaking down a high-level goal into smaller subtasks and then executing those subtasks through various steps. For instance, a user might ask a [chatbot](https://www.ibm.com/think/topics/chatbots) with a natural language prompt to plan a trip.

The agent would first decompose the task into components such as booking flights, finding hotels and planning an itinerary. Once decomposed, the agent can use [application programming interfaces (APIs)](https://www.ibm.com/think/topics/api) to fetch real-time data, check pricing and even suggest destinations.

### State representation

To plan effectively, an agent must have a structured understanding of its environment. This understanding is achieved through state representation, which models the current conditions, constraints and contextual factors that influence decision-making.

Agents have some built-in knowledge from their training data or [datasets](https://www.ibm.com/think/topics/dataset) representing previous interactions, but perception is required for agents to have a real-time understanding of their environment. Agents collect data through sensory input, allowing it to model its environment, along with user input and data describing its own internal state.

The complexity of state representation varies depending on the task. For example, in a chess game, the state includes the position of all pieces on the board, while in a robotic navigation system, the state might involve spatial coordinates, obstacles and terrain conditions.

The accuracy of state representation directly impacts an agent’s ability to make informed decisions, as it determines how well the agent can predict the outcomes of its actions.

### Action sequencing

Once the agent has established its goal and assessed its environment, it must determine a sequence of actions that will transition it from its current state to the desired goal state. This process, known as action sequencing, involves structuring a logical and efficient set of steps that the agent must follow.

The agent needs to identify potential actions, reduce that list to optimal actions, prioritize them and identifying dependencies between actions and conditional steps based on potential changes in the environment. The agent might allocate resources to each step in the sequence, or schedule actions based on environmental constraints.

For example, a robotic vacuum cleaner needs to decide the most effective path to clean a room, ensuring it covers all necessary areas without unnecessary repetition. If the sequence of actions is not well planned, the AI agent might take inefficient or redundant steps, leading to wasted resources and increased execution time.

The ReAct framework is a methodology used in AI for handling dynamic decision-making. In the ReAct framework, reasoning refers to the cognitive process where the agent determines what actions or strategies are required to achieve a specific goal.

This phase is similar to the planning phase in agentic AI, where the agent generates a sequence of steps to solve a problem or fulfill a task. Other emerging frameworks include ReWOO, RAISE and Reflexion, each of which has its own strengths and weaknesses.

### Optimization and evaluation

AI planning often involves selecting the most optimal path to achieving a goal, especially when multiple options are available. Optimization helps ensure that an agent's chosen sequence of actions is the most efficient, cost-effective or otherwise beneficial given the circumstances. This process often requires evaluating different factors such as time, resource consumption, risks and potential rewards.

For example, a warehouse robot tasked with retrieving items must determine the shortest and safest route to avoid collisions and reduce operational time. Without proper optimization, AI agents might execute plans that are functional but suboptimal, leading to inefficiencies. Several methods can be used to optimize decision-making, including:

#### Heuristic search

Heuristic search algorithms help agents find optimal solutions by estimating the best path toward a goal. These algorithms rely on heuristic functions—mathematical estimates of how close a given state is to the desired goal. Heuristic searches are particularly effective for structured environments where agents need to find optimal paths quickly.

#### Reinforcement learning

Reinforcement learning enables agents to optimize planning through trial and error, learning which sequences of actions lead to the best outcomes over time. An agent interacts with an environment, receives feedback in the form of rewards or penalties, and refines its strategies accordingly.

#### Probabilistic planning

In real-world scenarios, AI agents often operate in uncertain environments where outcomes are not deterministic. Probabilistic planning methods account for uncertainty by evaluating multiple possible outcomes and selecting actions with the highest expected utility.

### Collaboration

Single agent planning is one thing, but in a [multiagent system](https://www.ibm.com/think/topics/multiagent-system), AI agents must work autonomously while interacting with each other to achieve individual or collective goals.

The planning process for AI agents in a multiagent system is more complex than for a single agent because agents must not only plan their own actions but also consider the actions of other agents and how their decisions interact with those of others.

Depending on the [agentic architecture](https://www.ibm.com/think/topics/agentic-architecture), each agent in the system typically has its own individual goals, which might involve accomplishing specific tasks or maximizing a reward function. In many multiagent systems, agents need to work together to achieve shared goals.

These goals could be defined by an overarching system or emerge from the agents’ interactions. Agents need mechanisms to communicate and align their goals, especially in cooperative scenarios. This could be done through explicit messaging, shared task definitions or implicit coordination.

Planning in multiagent systems can be centralized, where a single entity or controller—likely an LLM agent—generates the plan for the entire system.

Each agent receives instructions or plans from this central authority. It can also be decentralized, where agents generate their own plans but work collaboratively to help ensure that they align with each other and contribute to global objectives, often requiring communication and negotiation.

This collaborative decision-making process enhances efficiency, reduces [biases](https://www.ibm.com/think/topics/ai-bias) in task execution, helps to avoid [hallucinations](https://www.ibm.com/think/topics/ai-hallucinations) through cross-validation and consensus-building and encourages the agents to work toward a common goal.

https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_0suvlp8f/width/1180

### 5 Types of AI Agents: Autonomous Functions & Real-World Applications

Learn how goal-driven and utility-based AI adapt to workflows and complex environments.

## After planning

The phases in agentic [AI workflows](https://www.ibm.com/think/topics/ai-workflow) do not always occur in a strict step-by-step linear fashion. While these phases are often distinct in conceptualization, in practice, they are frequently interleaved or iterative, depending on the nature of the task and the complexity of the environment in which the agent operates.

AI solutions can differ depending on their design, but in a typical [agentic workflow](https://www.ibm.com/think/topics/agentic-workflows), the next phase after planning is action execution, where the agent carries out the actions defined in the plan. This involves performing tasks and interacting with external systems or knowledge bases with [retrieval augmented generation (RAG)](https://www.ibm.com/think/topics/retrieval-augmented-generation), tool use and function calling ( [tool calling](https://www.ibm.com/think/topics/tool-calling)).

Building [AI agents](https://www.ibm.com/solutions/ai-agents) for these capabilities might involve [LangChain](https://www.ibm.com/think/topics/langchain). Python scripts, JSON data structures and other programmatic tools enhance the AI’s ability to make decisions.

After executing plans, some agents can use memory to learn from their experiences and iterate their behavior accordingly.

In dynamic environments, the planning process must be adaptive. Agents continuously receive feedback about the environment and other agents’ actions and must adjust their plans accordingly. This might involve revising goals, adjusting action sequences, or adapting to new agents entering or leaving the system.

When an agent detects that its current plan is no longer feasible (for example, due to a conflict with another agent or a change in the environment), it might engage in replanning to adjust its strategy. Agents can adjust their strategies using [chain of thought](https://www.ibm.com/think/topics/chain-of-thoughts) reasoning, a process where they reflect on the steps needed to reach their objective before taking action.

https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_mrwh878k/width/1180

### Listen to: 'What is AI agent perception and AI agent planning?'

Follow Techsplainers: [Spotify](https://open.spotify.com/show/1CuiV3XpXm68MxGpllQV4j) and [Apple Podcasts](https://podcasts.apple.com/us/podcast/techsplainers-by-ibm/id1850811611)

## Author

https://www.ibm.com/adobe/dynamicmedia/deliver/dm-aid--6ffe6fc8-d405-4a89-ad05-780d6960d862/cole-stryker-2x.jpg?preferwebp=true&width=128

[Cole Stryker](https://www.ibm.com/think/author/cole-stryker.html)

Staff Editor, AI Models

IBM Think

</details>

<details>
<summary>Building effective agents - Anthropic</summary>

# Building effective agents - Anthropic

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

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd3083d3f40bb2b6f477901cc9a240738d3dd1371-2401x1000.png&w=3840&q=75The augmented LLM

We recommend focusing on two key aspects of the implementation: tailoring these capabilities to your specific use case and ensuring they provide an easy, well-documented interface for your LLM. While there are many ways to implement these augmentations, one approach is through our recently released [Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), which allows developers to integrate with a growing ecosystem of third-party tools with a simple [client implementation](https://modelcontextprotocol.io/tutorials/building-a-client#building-mcp-clients).

For the remainder of this post, we'll assume each LLM call has access to these augmented capabilities.

### Workflow: Prompt chaining

Prompt chaining decomposes a task into a sequence of steps, where each LLM call processes the output of the previous one. You can add programmatic checks (see "gate” in the diagram below) on any intermediate steps to ensure that the process is still on track.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.png&w=3840&q=75The prompt chaining workflow

**When to use this workflow:** This workflow is ideal for situations where the task can be easily and cleanly decomposed into fixed subtasks. The main goal is to trade off latency for higher accuracy, by making each LLM call an easier task.

**Examples where prompt chaining is useful:**

- Generating Marketing copy, then translating it into a different language.
- Writing an outline of a document, checking that the outline meets certain criteria, then writing the document based on the outline.

### Workflow: Routing

Routing classifies an input and directs it to a specialized followup task. This workflow allows for separation of concerns, and building more specialized prompts. Without this workflow, optimizing for one kind of input can hurt performance on other inputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5c0c0e9fe4def0b584c04d37849941da55e5e71c-2401x1000.png&w=3840&q=75The routing workflow

**When to use this workflow:** Routing works well for complex tasks where there are distinct categories that are better handled separately, and where classification can be handled accurately, either by an LLM or a more traditional classification model/algorithm.

**Examples where routing is useful:**

- Directing different types of customer service queries (general questions, refund requests, technical support) into different downstream processes, prompts, and tools.
- Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance.

### Workflow: Parallelization

LLMs can sometimes work simultaneously on a task and have their outputs aggregated programmatically. This workflow, parallelization, manifests in two key variations:

- **Sectioning**: Breaking a task into independent subtasks run in parallel.
- **Voting:** Running the same task multiple times to get diverse outputs.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F406bb032ca007fd1624f261af717d70e6ca86286-2401x1000.png&w=3840&q=75The parallelization workflow

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

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F8985fc683fae4780fb34eab1365ab78c7e51bc8e-2401x1000.png&w=3840&q=75The orchestrator-workers workflow

**When to use this workflow:** This workflow is well-suited for complex tasks where you can’t predict the subtasks needed (in coding, for example, the number of files that need to be changed and the nature of the change in each file likely depend on the task). Whereas it’s topographically similar, the key difference from parallelization is its flexibility—subtasks aren't pre-defined, but determined by the orchestrator based on the specific input.

**Example where orchestrator-workers is useful:**

- Coding products that make complex changes to multiple files each time.
- Search tasks that involve gathering and analyzing information from multiple sources for possible relevant information.

### Workflow: Evaluator-optimizer

In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F14f51e6406ccb29e695da48b17017e899a6119c7-2401x1000.png&w=3840&q=75The evaluator-optimizer workflow

**When to use this workflow:** This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value. The two signs of good fit are, first, that LLM responses can be demonstrably improved when a human articulates their feedback; and second, that the LLM can provide such feedback. This is analogous to the iterative writing process a human writer might go through when producing a polished document.

**Examples where evaluator-optimizer is useful:**

- Literary translation where there are nuances that the translator LLM might not capture initially, but where an evaluator LLM can provide useful critiques.
- Complex search tasks that require multiple rounds of searching and analysis to gather comprehensive information, where the evaluator decides whether further searches are warranted.

### Agents

Agents are emerging in production as LLMs mature in key capabilities—understanding complex inputs, engaging in reasoning and planning, using tools reliably, and recovering from errors. Agents begin their work with either a command from, or interactive discussion with, the human user. Once the task is clear, agents plan and operate independently, potentially returning to the human for further information or judgement. During execution, it's crucial for the agents to gain “ground truth” from the environment at each step (such as tool call results or code execution) to assess its progress. Agents can then pause for human feedback at checkpoints or when encountering blockers. The task often terminates upon completion, but it’s also common to include stopping conditions (such as a maximum number of iterations) to maintain control.

Agents can handle sophisticated tasks, but their implementation is often straightforward. They are typically just LLMs using tools based on environmental feedback in a loop. It is therefore crucial to design toolsets and their documentation clearly and thoughtfully. We expand on best practices for tool development in Appendix 2 ("Prompt Engineering your Tools").

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.png&w=3840&q=75Autonomous agent

**When to use agents:** Agents can be used for open-ended problems where it’s difficult or impossible to predict the required number of steps, and where you can’t hardcode a fixed path. The LLM will potentially operate for many turns, and you must have some level of trust in its decision-making. Agents' autonomy makes them ideal for scaling tasks in trusted environments.

The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails.

**Examples where agents are useful:**

The following examples are from our own implementations:

- A coding Agent to resolve [SWE-bench tasks](https://www.anthropic.com/research/swe-bench-sonnet), which involve edits to many files based on a task description;
- Our [“computer use” reference implementation](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo), where Claude uses a computer to accomplish tasks.

https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F4b9a1f4eb63d5962a6e1746ac26bbc857cf3474f-2400x1666.png&w=3840&q=75High-level flow of a coding agent

## Combining and customizing these patterns

These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases. The key to success, as with any LLM features, is measuring performance and iterating on implementations. To repeat: you should consider adding complexity _only_ when it demonstrably improves outcomes.

## Summary

Success in the LLM space isn't about building the most sophisticated system. It's about building the _right_ system for your needs. Start with simple prompts, optimize them with comprehensive evaluation, and add multi-step agentic systems only when simpler solutions fall short.

When implementing agents, we try to follow three core principles:

1. Maintain **simplicity** in your agent's design.
2. Prioritize **transparency** by explicitly showing the agent’s planning steps.
3. Carefully craft your agent-computer interface (ACI) through thorough tool **documentation and testing**.

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
<summary>ReAct agent from scratch with Gemini 2.5 and LangGraph</summary>

# ReAct agent from scratch with Gemini 2.5 and LangGraph

**Source URL:** <https://ai.google.dev/gemini-api/docs/langgraph-example>

LangGraph is a framework for building stateful LLM applications, making it a
good choice for constructing ReAct (Reasoning and Acting) Agents.

ReAct agents combine LLM reasoning with action execution. They iteratively
think, use tools, and act on observations to achieve user goals, dynamically
adapting their approach. Introduced in ["ReAct: Synergizing Reasoning and Acting\
in Language Models"](https://arxiv.org/abs/2210.03629) (2023), this pattern
tries to mirror human-like, flexible problem-solving over rigid workflows.

LangGraph offers a prebuilt ReAct agent ( [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent)),
that shines when you need more control and customization for your ReAct
implementations. This guide will show you a simplified version.

LangGraph models agents as graphs using three key components:

- `State`: Shared data structure (typically `TypedDict` or `Pydantic BaseModel`) representing the application's current snapshot.
- `Nodes`: Encodes logic of your agents. They receive the current State as input, perform some computation or side-effect, and return an updated State, such as LLM calls or tool calls.
- `Edges`: Define the next `Node` to execute based on the current `State`, allowing for conditional logic and fixed transitions.

If you don't have an API Key yet, you can get one from [Google AI\
Studio](https://aistudio.google.com/app/apikey).

```
pip install langgraph langchain-google-genai geopy requests
```

Set your API key in the environment variable `GEMINI_API_KEY`.

```
import os

# Read your API key from the environment variable or set it manually
api_key = os.getenv("GEMINI_API_KEY")
```

To better understand how to implement a ReAct agent using LangGraph, this guide
will walk through a practical example. You will create an agent whose goal is to
use a tool to find the current weather for a specified location.

For this weather agent, the `State` will maintain the ongoing conversation
history (as a list of messages) and a counter (as an integer) for the number of
steps taken, for illustrative purposes.

LangGraph provides a helper function, `add_messages`, for updating state message
lists. It functions as a [reducer](https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers),
taking the current list, plus the new messages, and returns a combined list. It
handles updates by message ID and defaults to an "append-only" behavior for new,
unseen messages.

```
from typing import Annotated,Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages  # helper function to add messages to the state

class AgentState(TypedDict):
    """The state of the agent."""
    messages: Annotated[Sequence[BaseMessage], add_messages]
    number_of_steps: int
```

Next, define your weather tool.

```
from langchain_core.tools import tool
from geopy.geocoders import Nominatim
from pydantic import BaseModel, Field
import requests

geolocator = Nominatim(user_agent="weather-app")

class SearchInput(BaseModel):
    location:str = Field(description="The city and state, e.g., San Francisco")
    date:str = Field(description="the forecasting date for when to get the weather format (yyyy-mm-dd)")

@tool("get_weather_forecast", args_schema=SearchInput, return_direct=True)
def get_weather_forecast(location: str, date: str):
    """Retrieves the weather using Open-Meteo API.

    Takes a given location (city) and a date (yyyy-mm-dd).

    Returns:
        A dict with the time and temperature for each hour.
    """
    # Note that Colab may experience rate limiting on this service. If this
    # happens, use a machine to which you have exclusive access.
    location = geolocator.geocode(location)
    if location:
        try:
            response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&hourly=temperature_2m&start_date={date}&end_date={date}")
            data = response.json()
            return dict(zip(data["hourly"]["time"], data["hourly"]["temperature_2m"]))
        except Exception as e:
            return {"error": str(e)}
    else:
        return {"error": "Location not found"}

tools = [get_weather_forecast]
```

Now initialize the model and bind the tools to the model.

```
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI

# Create LLM class
llm = ChatGoogleGenerativeAI(
    model= "gemini-3-flash-preview",
    temperature=1.0,
    max_retries=2,
    google_api_key=api_key,
)

# Bind tools to the model
model = llm.bind_tools([get_weather_forecast])

# Test the model with tools
res=model.invoke(f"What is the weather in Berlin on {datetime.today()}?")

print(res)
```

The last step before you can run your agent is to define your nodes and edges.
In this example, you have two nodes and one edge.

- `call_tool` node that executes your tool method. LangGraph has a prebuilt node
for this called
[ToolNode](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/).
- `call_model` node that uses the `model_with_tools` to call the model.
- `should_continue` edge that decides whether to call the tool or the model.

The number of nodes and edges is not fixed. You can add as many nodes and edges
as you want to your graph. For example, you could add a node for adding
structured output or a self-verification/reflection node to check the model
output before calling the tool or the model.

```
from langchain_core.messages import ToolMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}

# Define our tool node
def call_tool(state: AgentState):
    outputs = []
    # Iterate over the tool calls in the last message
    for tool_call in state["messages"][-1].tool_calls:
        # Get the tool by name
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=tool_result,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}

def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # Invoke the model with the system prompt and the messages
    response = model.invoke(state["messages"], config)
    # This returns a list, which combines with the existing messages state
    # using the add_messages reducer.
    return {"messages": [response]}

# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    # If the last message is not a tool call, then finish
    if not messages[-1].tool_calls:
        return "end"
    # default to continue
    return "continue"
```

With all of the agent components ready, you can now assemble them.

```
from langgraph.graph import StateGraph, END

# Define a new graph with our state
workflow = StateGraph(AgentState)

# 1. Add the nodes
workflow.add_node("llm", call_model)
workflow.add_node("tools",  call_tool)
# 2. Set the entrypoint as `agent`, this is the first node called
workflow.set_entry_point("llm")
# 3. Add a conditional edge after the `llm` node is called.
workflow.add_conditional_edges(
    # Edge is used after the `llm` node is called.
    "llm",
    # The function that will determine which node is called next.
    should_continue,
    # Mapping for where to go next, keys are strings from the function return,
    # and the values are other nodes.
    # END is a special node marking that the graph is finish.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)
# 4. Add a normal edge after `tools` is called, `llm` node is called next.
workflow.add_edge("tools", "llm")

# Now we can compile and visualize our graph
graph = workflow.compile()
```

You can visualize your graph using the `draw_mermaid_png` method.

```
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

https://ai.google.dev/static/gemini-api/docs/images/langgraph-react-agent_16_0.png

Now run the agent.

```
from datetime import datetime
# Create our initial message dictionary
inputs = {"messages": [("user", f"What is the weather in Berlin on {datetime.today()}?")]}

# call our graph with streaming to see the steps
for state in graph.stream(inputs, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

You can now continue with your conversation, ask for the weather in another
city, or request a comparison.

```
state["messages"].append(("user", "Would it be warmer in Munich?"))

for state in graph.stream(state, stream_mode="values"):
    last_message = state["messages"][-1]
    last_message.pretty_print()
```

</details>

<details>
<summary>ReAct Agent - IBM</summary>

# ReAct Agent - IBM

**Source URL:** <https://www.ibm.com/think/topics/react-agent>

- [ReAct agent overview](https://www.ibm.com/think/topics/react-agent#ReAct+agent+overview)
- [How do ReAct agents work?](https://www.ibm.com/think/topics/react-agent#How+do+ReAct+agents+work%3F)
- [ReAct prompting](https://www.ibm.com/think/topics/react-agent#ReAct+prompting)
- [Benefits of ReAct agents](https://www.ibm.com/think/topics/react-agent#Benefits+of+ReAct+agents)
- [ReAct agents vs. function calling](https://www.ibm.com/think/topics/react-agent#ReAct+agents+vs.+function+calling)
- [Getting started with ReAct agents](https://www.ibm.com/think/topics/react-agent#Getting+started+with+ReAct+agents)

By

[Dave Bergmann](https://www.ibm.com/think/author/dave-bergmann.html)

## ReAct agent overview

A ReAct agent is an [AI agent](https://www.ibm.com/think/topics/ai-agents) that uses the “reasoning and acting” (ReAct) framework to combine [chain of thought (CoT)](https://www.ibm.com/think/topics/chain-of-thoughts) reasoning with external tool use. The ReAct framework enhances the ability of a [large language model (LLM)](https://www.ibm.com/think/topics/large-language-models) to handle complex tasks and decision-making in [agentic workflows](https://www.ibm.com/think/topics/agentic-workflows).

First introduced by Yao and others in the 2023 paper, “ReACT: Synergizing Reasoning and Acting in Language Models,” ReAct can be understood most generally as a [machine learning](https://www.ibm.com/think/topics/machine-learning) (ML) paradigm to integrate the reasoning and action-taking capabilities of LLMs.

More specifically, ReAct is a conceptual framework for building AI agents that can interact with their environment in a structured but adaptable way, by using an LLM as the agent’s “brain” to coordinate anything from simple [retrieval augmented generation (RAG)](https://research.ibm.com/blog/retrieval-augmented-generation-RAG) to intricate [multiagent](https://www.ibm.com/think/topics/multiagent-system) workflows.

Unlike traditional artificial intelligence (AI) systems, ReAct agents don’t separate decision-making from task execution. Therefore, the development of the ReAct paradigm was an important step in the evolution of [generative AI (gen AI)](https://www.ibm.com/think/topics/generative-ai) beyond mere conversational [chatbots](https://www.ibm.com/think/topics/chatbots) and toward complex problem-solving.

ReAct agents and derivative approaches continue to power AI applications that can autonomously plan, execute and adapt to unforeseen circumstances.

## How do ReAct agents work?

The ReAct framework is inspired by the way humans can intuitively use natural language—often through our own inner monologue—in the step-by-step planning and execution of complex tasks.

Rather than implementing rule-based or otherwise predefined workflows, ReAct agents rely on their LLM’s reasoning capabilities to dynamically adjust their approach based on new information or the results of previous steps.

Imagine packing for a brief trip. You might start by identifying key considerations (“ _What will the weather be like while I’m there?_”), then actively consult external sources (“ _I’ll check the local weather forecast_”).

By using that new information (“ _It’s going to be cold_”), you determine your next consideration (“ _What warm clothes do I have?_”) and action (“ _I’ll check my closet_”). Upon taking that action, you might encounter an unexpected obstacle (“ _All of my warm clothes are in storage_”) and adjust your next step accordingly (“ _What clothes can I layer together?_”).

In a similar fashion, the ReAct framework uses [prompt engineering](https://www.ibm.com/think/topics/prompt-engineering) to structure an AI agent’s activity in a formal pattern of alternating thoughts, actions and observations:

- The verbalized CoT reasoning steps ( _thoughts_) help the model decompose the larger task into more manageable subtasks.

- Predefined _actions_ enable the model to use tools, make [application programming interface (API)](https://www.ibm.com/think/topics/api) calls and gather more information from external sources (such as search engines) or knowledge bases (such as an internal docstore).

- After taking an action, the model then reevaluates its progress and uses that _observation_ to either deliver a final answer or inform the next _thought_. The observation might ideally also consider prior information, whether from earlier in the model’s standard context window or from an external memory component.

Because the performance of a ReAct agent depends heavily on the ability of its central LLM to “verbally” think its way through complex tasks, ReAct agents benefit greatly from highly capable models with advanced reasoning and instruction-following ability.

To minimize cost and [latency](https://www.ibm.com/think/topics/latency), a multiagent ReAct framework might rely primarily on a larger, more performant model to serve as the central agent whose reasoning process or actions might involve delegating subtasks to more agents built using smaller, more efficient models.

### ReAct agent loops

This framework inherently creates a feedback loop in which the model problem-solves by iteratively repeating this interleaved _thought-action-observation_ process.

Each time this loop is completed—that is, each time the agent has taken an action and made an observation based on the results of that action—the agent must then decide whether to repeat or end the loop.

https://assets.ibm.com/is/image/ibm/react:16x9?fmt=png-alpha&dpr=on%2C1&wid=320&hei=180

When and how to end the reasoning loop is an important consideration in the design of a ReAct agent. Establishing a maximum number of loop iterations is a simple way to limit latency, costs and token usage, and avoid the possibility of an endless loop.

Conversely, the loop can be set to end when some specific condition is met, such as when the model has identified a potential final answer that exceeds a certain confidence threshold.

To implement this kind of reasoning and acting loop, ReAct agents typically use some variant of _ReAct prompting_, whether in the system prompt provided to the LLM or in the context of the user query itself.

## ReAct prompting

ReAct prompting is a specific prompting technique designed to guide an LLM to follow the ReAct paradigm of _thought_, _action_ and _observation_ loops. While the explicit use of conventional ReAct prompting methods is not strictly necessary to build a ReAct agent, most ReAct-based agents implement or at least take direct inspiration from it.

First outlined in the original ReAct paper, ReAct prompting’s primary function is to instruct an LLM to follow the ReAct loop and establish which tools can be used—that is, which actions can be taken—when handling user queries.

Whether through explicit instructions or the inclusion of [few-shot](https://www.ibm.com/think/topics/few-shot-learning) examples, ReAct prompting should:

- **Guide the model to use chain of thought reasoning:** Prompt the model to reason its way through tasks by thinking step by step, interleaving thoughts with actions.

- **Define actions:** Establish the specific actions available to the model. An action might entail the generation of a specific type of next thought or subprompt but usually involves [using external tools](https://www.ibm.com/think/topics/tool-calling) or making APIs.

- **Instruct the model to make observations:** Prompt the model to reassess its context after each action step and use that updated context to inform the next reasoning step.

- **Loop:** Instruct the model to repeat the previous steps if necessary. You could provide specific conditions for ending that loop, such as a maximum number of loops, or instruct the agent to end its reasoning process whenever it feels it has arrived at the correct final output.

- **Output final answer:** Whenever those end conditions have been met, provide the user with the final output in response to their initial query. As with many uses of LLMs, as reasoning models employing chain of thought reasoning before determining a final output, ReAct agents are often prompted to conduct their reasoning process within a [“scratchpad.”](https://arxiv.org/abs/2112.00114)

A classic demonstration of ReAct prompting is the system prompt for the prebuilt
```
ZERO\_SHOT\_REACT-DESCRIPTION
ReAct agent module in [Langchain](https://www.ibm.com/think/topics/langchain)’s LangGraph. It’s called “ [zero-shot](https://www.ibm.com/think/topics/zero-shot-learning)” because, with this predefined system prompt, the LLM being used with the module does not need any further examples to behave as a ReAct agent.

```
Answer the following questions as best you can. You have access to the following tools:

Wikipedia: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, facts, historical events, or other subjects. Input should be a search query.
duckduckgo_search: A wrapper around DuckDuckGo Search. Useful for when you need to answer questions about current events. Input should be a search query.
Calculator: Useful for when you need to answer questions about math.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [Wikipedia, duckduckgo_search, Calculator]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
```



IBM watsonx.ai




https://cdnsecakmi.kaltura.com/p/1773841/thumbnail/entry_id/1_sel1ypri/width/1180

### Data Insights with LangGraph and watsonx.ai

Can an AI agent take our natural language query and do the processing for us to give us that meaningful output? We use several pieces of open source technology and the power of watsonx.ai to put this to the test.

## Benefits of ReAct agents

The introduction of the ReAct framework was an important step in the advancement of LLM-driven [agentic workflows](https://www.ibm.com/think/topics/agentic-workflows). From grounding LLMs in real time, real-world external information through (RAG) to contributing to subsequent breakthroughs—such as [Reflexion](https://arxiv.org/abs/2303.11366), which led to modern reasoning models—ReAct has helped catalyze the use of LLMs for tasks well beyond text generation.

The utility of ReAct agents is drawn largely from some of the inherent qualities of the ReAct framework:

- **Versatility:** ReAct agents can be configured to work with a wide variety of external tools and APIs. Though [fine-tuning](https://www.ibm.com/think/topics/fine-tuning) relevant ReAct prompts (using relevant tools) can improve performance, no prior configuration of the model is required to execute [tool calls](https://www.ibm.com/think/topics/tool-calling).

- **Adaptability:** This versatility, along with the dynamic and situational nature of how they determine the appropriate tool or API to call, means that ReAct agents can use their reasoning process to adapt to new challenges. Especially when operating within a lengthy context window or augmented with external memory, they can learn from past mistakes and successes to tackle unforeseen obstacles and situations. This makes ReAct agents flexible and resilient.

- **Explainability:** The verbalized reasoning process of a ReAct agent is simple to follow, which facilitates debugging and helps make them relatively user-friendly to build and optimize.

- **Accuracy:** As the original ReAct paper asserts, chain of thought (CoT) reasoning alone has many benefits for LLMs, but also runs an increased risk of hallucination. ReAct’s combination of CoT with a connection external to information sources significantly reduces [hallucinations](https://www.ibm.com/think/topics/ai-hallucinations), making ReAct agents more accurate and trustworthy.

## ReAct agents vs. function calling

Another prominent paradigm for agentic AI is function calling, originally [introduced by OpenAI in June 2023](https://openai.com/index/function-calling-and-other-api-updates/) to supplement the agentic abilities of its [GPT models](https://www.ibm.com/think/topics/gpt).

The function calling paradigm entails [fine-tuning](https://www.ibm.com/think/topics/fine-tuning) models to recognize when a particular situation should result in a tool call and output a structured [JSON](https://www.ibm.com/docs/en/baw/25.0.x?topic=formats-javascript-object-notation-json-format) object containing the arguments necessary to call those functions.

Many proprietary and open source LLM families, [including IBM® Granite®](https://www.ibm.com/granite/docs/models/granite#function-calling), Meta’s [Llama](https://www.ibm.com/think/news/meta-llama-3-2-models) series, Anthropic’s [Claude](https://www.ibm.com/think/topics/claude-ai) and [Google Gemini](https://www.ibm.com/think/topics/google-gemini), now support function calling.

Whether ReAct or function calling is “better” will generally depend on the nature of your specific use case. In scenarios involving relatively straightforward (or at least predictable) tasks, function calling can execute faster, save tokens, and be simpler to implement than a ReAct agent.

In such circumstances, the number of tokens that would be spent on a ReAct agent’s iterative loop of CoT reasoning might be seen as inefficient.

The inherent tradeoff is a relative lack of ability to customize how and when the model chooses which tool to use. Likewise, when an agent handles tasks that call for complex reasoning, or scenarios that are dynamic or unpredictable, the rigidity of function calling might limit the agent’s adaptability. In such situations, it’s often beneficial to be able to view the step-by-step reasoning that led to a specific tool call.

## Getting started with ReAct agents

ReAct agents can be designed and implemented in multiple ways, whether coded from scratch in Python or developed with the help of open source frameworks such as [BeeAI](https://research.ibm.com/blog/bee-ai-app). The popularity and staying power of the ReAct paradigm have yielded extensive literature and tutorials for ReAct agents on GitHub and other developer communities.

As an alternative to developing custom ReAct agents, many agentic AI frameworks, including BeeAI, [LlamaIndex](https://www.ibm.com/think/topics/llamaindex) and LangChain’s LangGraph, offer [preconfigured ReAct agent modules](https://github.com/i-am-bee/beeai-framework/blob/main/python/examples/agents/react.py).
```

</details>

<details>
<summary>ReAct: Synergizing Reasoning and Acting in Language Models</summary>

# ReAct: Synergizing Reasoning and Acting in Language Models

**Source URL:** <https://arxiv.org/pdf/2210.03629>

REACT: SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS

Shunyu Yao$^{k1}$, Jeffrey Zhao$^{2}$, Dian Yu$^{2}$, Nan Du$^{2}$, Izhak Shafran$^{2}$, Karthik Narasimhan$^{1}$, Yuan Cao$^{2}$

$^1$Department of Computer Science, Princeton University
$^2$Google Research, Brain team
$^1$(shunyu,karthik)@princeton.edu
$^2$(jeffreyzhao,dianyu,dunan,izhak,yuancao)@google.com

ABSTRACT

While large language models (LLMs) have demonstrated impressive performance across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with and gather additional information from external sources such as knowledge bases or environments. We apply our approach named React, to a divorced set of language and decision making tasks, and demonstrate its effectiveness over state-of-the-art baselines in addition to improved human interpretability and trustworthiness. Concretely, on question answering (HopotQA) and fact verification (Fever), React overcomes prevalent issues of hallucination and error propagation in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generating human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. Furthermore, on two interactive decision making benchmarks (ALIWorld and WebShop), React outperforms imitation and reinforcement learning methods by an absolute success rate of 44% and 10% respectively, while being prompted with only one or two in-context examples.

1 INTRODUCTION

A unique feature of human intelligence is the ability to seamlessly combine task-oriented actions with verbal reasoning (or inner speech, Alderson-Day & Ferrybough, 2015), which has been theorized to play an important role in human cognition for enabling self-regulation or stratification (Vygotsky, 1987; Lura, 1965; Ferybough, 2010) and maintaining a working memory (Baddeley, 1992). Consider the example of cooking up a dish in the kitchen. Between any two specific actions, we may reason in language in order to track progress ("now that everything is cut, I should heat up the pot of water"), to handle exceptions or adjust the plan according to the situation ("I don't have salt, so let me use soy sauce and pepper instead"), and to realize when external information is needed ("how do I prepare dough?"). Let me search on the Internet," We may also act (open a cookbook to read the recipe, open the fridge, check ingredients) to support the reasoning and to answer questions ("What dish can I make right now?"). This tight synergy between "acting" and "reasoning" allows humans to learn new tasks quickly and perform robust decision making or reasoning, even under previously unseen circumstances or facing information uncertainties.

Recent results have hinted at the possibility of combining verbal reasoning with interactive decision making in autonomous systems. On one hand, properly prompted large language models (LLMs) have demonstrated emergent capabilities to carry out several steps of reasoning traces to derive

\*Work during Google internship. Projet page with code: [https://react-lm.github.io/。](https://react-lm.github.io/%E3%80%82)

* * *

* * *

We conduct empirical evaluations of ReAct and state-of-the-art baselines on four diverse benchmarks: question answering (HotPoQA, Yang et al., 2018), fact verification (Fever, Thorne et al., 2018), text-based game (ALFWorld, Shridhar et al., 2020b), and webpage navigation (WebShop, Yao et al., 2022). For HotPoQA and Fever, with access to Wikipedia API that the model can interact with, ReAct outperforms vanilla action generation models while being competitive with chain-of-thought reasoning (GOt) (Wei et al., 2022). The best approach overall is a combination of ReAct and CoI that allows for the use of both internal knowledge and externally obtained information during reasoning. On ALFWorld and WebShop, two or even one-shot ReAct prompting is able to perform extensive imitation or reinforcement learning methods trained with $10^7 \\sim 10^9$ task instances, with an absolute improvement of 34% and 10% in success rates respectively. We also demonstrate the importance of sparse, versatile reasoning in decision making by showing consistent advantages over controlled baselines with actions only. Besides general applicability and performance boost, the combination of reasoning and acting also contributes to model interpretability, trustworthiness, and diagnostics across all domains, as humans can readily distinguish information from model's internal knowledge versus external environments, as well as inspect reasoning traces to understand the decision basis of model actions.

To summarize, our key contributions are the following: (1) we introduce ReAct, a novel prompt-based paradigm to synergize reasoning and acting in language models for general task solving; (2) we perform extensive experiments across diverse benchmarks to showcase the advantage of ReAct in a few-shot learning setup over prior approaches that perform either reasoning or action generation in isolation; (3) we present systematic ablations and analysis to understand the importance of acting in reasoning tasks, and reasoning in interactive tasks; (4) we analyze the limitations of ReAct under the prompting step (i.e. limited support of reasoning and acting behaviors), and perform initial finetuning experiments showing the potential of ReAct to improve with additional training data. Scaling up ReAct to train and operate on more tasks and combining it with complementary paradigms like reinforcement learning could further unlock the potential of large language models.

2 REACT: SYNERGIZING REASONING + ACTING

Consider a general setup of an agent interacting with an environment for task solving. At time step $t$, an agent receives an observation $a\_t \\in \\mathcal{O}$ from the environment and takes an action $a\_t \\in \\mathcal{A}$ following some policy $c\_a = \|a\_t\| _a$, where $c\_a = (a\_1, a\_1, \\dots, a_{-1}, a\_{-1}, o\_t)$ is the context to the agent. Learning a policy is challenging when the mapping $c\_a \\mapsto a\_t$ is highly implicit and requires extensive computation. For example, the agent shown in Figure 1(1) is unable to generate the correct final action (Act 4) to finish the QA task as it requires complex reasoning over the trajectory context (Question, Act 1, Obs 1-3). Similarly, the agent shown in Figure 1(2a) fails to comprehend from the context that sinkbasin 1 does not contain peppershaker 1, thus keeping productive hallucinating actions.

The idea of ReAct is simple: we augment the agent's action space to $\\mathcal{A} = A \\cup \\mathcal{L}$, where $\\mathcal{L}$ is the space of language. An action $a\_t \\in \\mathcal{L}$ in the language space, which we will refer to as a thought or a reasoning trace, does not affect the external environment, thus leading to no observation feedback. Instead, a thought $a\_t$ aims to compose useful information by reasoning over the current context $c\_a$, and update the context $c\_a = \|c\_a\|\_a$ to support future reasoning. As shown in Figure 1, there could be various types of useful thoughts, e.g. decomposing goal tasks and create action plans (2b, Act 1; 1d, Thought 1), injecting commonsense knowledge relevant to task solving (2b, Act 1), extracting important parts from observations (1d, Thought 2), track progress and transit action plans (2b, Act 8), handle exceptions and adjust action plans (1d, Thought 3), and so on.

However, as the language space $\\mathcal{L}$ is unlimited, learning in this augmented action space is difficult and requires strong language priors. In this paper, we mainly focus on the setup where a frozen large language model, PaiLM-540B (Chowlery et al., 2022)¹, is prompted with few-shot in-context examples to generate both domain-specific actions and free-form language tasks for task solving (Figure 1 (1d), (2b)). Each in-context example is a human trajectory of actions, thoughts, and environment observations to solve a task instance see Appendix C). For the tasks where reasoning is of primary importance (Figure 1(1)), we alternate the generation of thoughts and actions so that the task-solving trajectory consists of multiple thought-action-observation steps. In contrast, for decision making tasks that potentially involve a large number of actions (Figure 1(2)), thoughts only need to

¹We show some GPT-3 (Brown et al., 2020) results in Appendix A.1, which outperforms PaLM-540B.

* * *

appear sparsely in the most relevant positions of a trajectory, so we let the language model decide the asynchronous occurrence of thoughts and actions for itself.

Since decision making and reasoning capabilities are integrated into a large language model, ReAct enjoys several unique features: A) Intuitive and easy to design. Designing ReAct prompts is still reasoned or acting across different domains. Our thoughts in language on top of their actions taken. No ad-hoc format choice, thought design, or example selection is used in this paper. We detail prompt design for each task in Sections 3 and 4. B) General and flexible: Due to the flexible thought space and thought-action occurrence format, ReAct works for diverse tasks with distinct action spaces and reasoning needs, including but not limited to QA, fact verification, text game, and web navigation. C) Performant and robust: ReAct shows strong generalization to new task instances while learning solely from one to six in-context examples, consistently outperforming baselines with only reasoning or acting across different domains. We also show in Section 3 additional benefits when finetuning is enabled, and in Section 4 how ReAct performance is robust to prompt selections. D) Human aligned and controllable: ReAct promises an interpretable sequential decision making and reasoning process where humans can easily inspect reasoning and factual correctness. Moreover, humans can also control or correct the agent behavior on the go by thought editing, as shown in Figure 5 in Section 4.

3 KNOWLEDGE-INTENSIVE REASONING TASKS

We begin with knowledge-intensive reasoning tasks like multi-hop question answering and fact verification. As shown in Figure 1(1d), by interacting with a Wikipedia API, ReAct is able to retrieve information to support reasoning, while also using reason to target what to retrieve next, demonstrating a synergy of reasoning and acting.

3.1 SETUP

Domains We consider two datasets challenging knowledge retrieval and reasoning: (1) Hot-PoQA (Yang et al., 2018), a multi-hop question answering benchmark that requires reasoning over two or more Wikipedia passages, and (2) FEVER (Thorne et al., 2018), a fact verification benchmark where each claim is annotated SUPPORTS, REFUTES, or NOT ENOUGH INFO, based on if there exists a Wikipedia passage to verify the claim. In this work, we operate in a question-only setup for both tasks, where models only receive the question/claim as input without access to support paragraphs and how to rely on their internal knowledge or retrieve knowledge via interacting with an external environment to support reasoning.

Action Space We design a simple Wikipedia web API with three types of actions to support interactive information retrieval: (1) search\[entity\], which returns the first 5 sentences from the corresponding entity wiki page if it exists, or else suggests top-5 similar entities from the Wikipedia search engine, (2) lookup\[string\], which would return the next sentence in the page containing string, simulating Ctrl+F functionality on the browser. (3) finish\[answer\], which would finish the current task with answer. We note that this action space mostly can only retrieve a small part of a passage based on exact passage name, which is significantly weaker than state-of-the-art lexical or neural retrievers. The purpose is to simulate how humans would interact with Wikipedia, and force models to retrieve via explicit reasoning in language.

3.2 METHODS

ReAct Prompting For HotPoQA and Fever, we randomly select 6 and 3 cases¹ from the training set and manually compose ReAct-format trajectories to use as few-shot exemplars in the prompts. Similar to Figure 1(d), each trajectory consists of multiple thought-observation steps (i.e. dense thought), where free-form thoughts are used for various purposes. Specifically, we use a combination of thoughts that decompose questions ("I need to search x, find y, then find z"), extract information from Wikipedia observations ("x was started in 1844", "The paragraph does not tell x"), perform commonsense ("x is not y, so z must instead be...") or arithmetic reasoning ("1844 < 1989"), guide

²We find more examples do not improve performance.

* * *

search reformulation ("maybe I can search/look up x instead"), and synthesize the final answer ("...so the answer is x"). See Appendix C for more details.

Baselines We systematically ablate ReAct trajectories to build prompts for multiple baselines (with formats as Figure 1(1a-1c)): (a) Standard prompting (Standard), which removes all thoughts, actions, observations in ReAct trajectories. (b) Chain-of-thought prompting (CoT) (Wei et al., 2022), which removes actions and observations and serve as a reasoning-only baseline. We also build a self-consistency baseline (CoT-SC) (Wang et al., 2022ab) by sampling 2 CoT trajectories with decoding temperature 0.7 during inference and adopting the majority answer, which is found to consistently boost performance over CoT. (c) Acting-only prompt (Act), which removes thoughts in ReAct trajectories, locally reassembling how WeiGPT Nakano et al. (2021) interests with the Internet to answer questions, though it operates on a different task and action space, and uses imitation and reinforcement learning instead of prompting.

Combining Internal and External Knowledge As will be detail in Section 3.3, we observe that the problem solving process demonstrated by ReAct is more factual and grounded, whereas CoT is more accurate in formulating reasoning structure but can easily suffer from hallucination facts or thoughts. We therefore propose to incorporate ReAct and CoT-SC, and let the model decide when to switch to the other method based on the following theories: A) ReAct → CoT-SC; when ReAct fails to return an answer within given steps, back off to CoT-SC. We set 7 find 5 steps for HotpotQA and FEVER respectively as we find more steps will not improve ReAct performance³. B) CoT-SC → ReAct: when the majority answer among n CoT-SC samples occurs less than n/2 times (i.e. internal knowledge might not support the task confidently), back off to ReAct.

Finetuning Due to the challenge of manually annotating reasoning traces and actions at scale, we consider a bootstrapping approach similar to Zelikman et al. (2022), using 3,000 trajectories with correct answers generated by ReAct (also for other baselines) to finetune smaller language models (PaLM-8/62B) to decode trajectories (all thoughts, actions, observations) conditioned on input questions/claims. More details are in Appendix B.1.

3.3 RESULTS AND OBSERVATIONS

ReAct outperforms Act consistently Table 1 shows HotpotQA and Fever results using PaLM-540B as the base model with different prompting methods. We note that ReAct is better than Act on both tasks, demonstrating the value of reasoning to guide acting, especially for synthesizing the final answer, as shown in Figure 1 (1c-d). Fine-tuning results 3 also confirm the benefit of reasoning traces for more informed acting.

³Of all trajectories with correct final answers, those with 7 steps on HotpotQA and 5 steps on FEVER only take up 0.84% and 1.35% respectively.

* * *

Table 2: Types of success and failure modes of ReAct and CoT on HotpotQA, as well as their percentages in randomly selected examples studied by human.

ReAct vs. CoT On the other hand, ReAct outperforms CoT on Fever (60.9 vs. 56.3) and slightly lags behind CoT on HotpotQA (27.4 vs. 29.4). Fever claims for SUPPORTS/REFUTES might only differ by a slight amount (see Appendix D.1), so acting to retrieve accurate and up-to-date knowledge is vital. To better understand the behavioral difference between ReAct and CoT on HotpotQA, we randomly sampled 50 trajectories with correct and incorrect answers (judged by KM from ReAct and CoT respectively) (than 200 examples in total), and manually labeled their success and failure modes in Table 2. Some key observations are as follows:

A) Hallucination is a serious problem for CoT, resulting in much higher false positive rate than ReAct (14% vs. 6%) in success mode, and make up its major failure mode (56%). In contrast, the problem solving trajectory of ReAct is more grounded, fact-driven, and trustworthy, thanks to the access of an external knowledge base.

B) While interleaving reasoning, action and observation steps improves ReAct’s groundedness and trustworthiness, such a structural constraint also reduces its flexibility in formulating reasoning steps, leading to more reasoning error rate than CoT. we note that there is one frequent error pattern specific to ReAct, in which the model repetitively generates the previous thoughts and actions, and we categorize it as part of “reasoning error” as the model fails to reason about what the proper next action to take and jump out of the loop$^b$.

C) For ReAct, successfully retrieving informative knowledge via search is critical. Non-informative search, which counts for 23% of the error cases, derails the model reasoning and gives it a hard time to recover and reformulate thoughts. This is perhaps an expected trade-off between factuality and flexibility, which motivates our proposed strategies of combining two methods.

We provide examples for each success and failure modes in Appendix E.1. We also find some HotpotQA questions may contain outdated answer labels, see Figure 4 for example.

ReAct + CoT-SC perform best for prompting LLM$. Also shown in Table 1, the best prompting and used CoT-SC power are ReAct + CoT-SC and CoT-SC + ReAct respectively. Furthermore, Figure 2 shows how different methods perform with respect to the number of CoT-SC samples used. While two ReAct + CoT-SC methods are advantageous at one task each, they both significantly and consistently outperform CoT-SC across different number of samples, reaching CoT-SC performance with 21 samples using merely 3-5 samples. These results indicate the value of properly combining model internal knowledge and external knowledge for reasoning tasks.

ReAct performs best for fine-tuning Figure 3 shows the sealing effect of prompting/finetuning four methods (Standard, CoT, Act, ReAct) on HotpotQA. With PalM-8M/62B, prompting ReAct performs best for how different methods perform with respect to the number of CoT-SC in context examples. However, when finetuned with just 3,000 examples, ReAct becomes the best method among the four, with PalM-8B finetuned ReAct outperforming all PalM-62B prompting methods, and PalM-62B finetuned ReAct outperforming all 540B prompting methods. In contrast, finetuned Standard or CoT is significantly worse than finetuned ReAct or act for both PalM-8/62B, as the former essentially teaches models to memorize (potentially hallucinated) knowledge facts, and the latter teaches models how to (reason and) act to access information from Wikipedia, a more general skill for how knowledge reasoning. As all prompting methods are still significantly far from domain-specific state-of-the-art approaches (Table 1), we believe finetuning with more human-written data might be a better way to unleash the power of ReAct.

$^{a}$We suspect that this could be due to the sub-optimal greedy decoding procedure, and future work using better decoding (e.g. beam search) might help address this issue.

* * *

Figure 3: Scaling results for prompting and finetuning on HotPotQA with ReAct (ours) and baselines.

4 DECISION MAKING TASKS

We also test ReAct on two language-based interactive decision-making tasks, ALFWorld and WebShop, both of which feature complex environments that require agents to act over long horizons with sparse rewards, warranting the need for reasoning to act and explore effectively.

ALFWorld ALFWorld (Shridhar et al., 2020b) (Figure 1.2()) is a synthetic text-based game designed to align with the embodied ALFRED benchmark (Shridhar et al., 2020a). It includes 6 types of tasks in which an agent needs to achieve a high-level goal (e.g. examine paper under desklamp) by navigating and interacting with a simulated household via text actions (e.g. go to coffetable 1, take paper 2, use desklamp 1). A task instance can have more than 50 locations and take an expert policy more than 50 steps to solve, thus challenging an agent to plan and track subgadgets, as well as explore systematically one by one for desklamp. In part, an I34 user evaluation game into ALFWorld is the need to determine likely locations for common household items (e.g. desklamps will likely be on desks, shelves, or dressers), making this environment a good fit for LLMs to exploit their pretrained commonsense knowledge. To prompt ReAct, we randomly annotate three trajectories from the training set for each task type, where each trajectory includes sparse thoughts that (1) decompose the goal, (2) track subgoal completion, (3) determine the next subgoal, and (4) reason via commensense where to find an object and what to do with it. We show prompted uses for ALFWorld in Appendix C.4. Following Shridhar et al., 2020b, we evaluate on I34 user evaluation games in a task-specific setup. For robustness, we construct 6 prompts for each task type through each permutation of 2 annotated trajectories from the 3 we annotate. Act prompts are constructed using the same trajectories, but without thoughts — since task instances are randomly chosen from the training set, it favors neither ReAct nor Act and provides a fair and controlled comparison to test the importance of sparse thoughts. For baselines, we use BUTLER (Shridhar et al., 2020b), an imitation learning agent trained on 10³ expert trajectories for each task type³.

WebShop Can ReAct also interact with noisy real-world language environments for practical applications? We investigate WebShop (Yao et al., 2022), a recently proposed online shopping website environment with 1.18M real-world products and 12k human instructions. Unlike ALFWorld, Webshop contains a high variety of structured and unstructured texts (e.g. product titles, descriptions, and options crawled from Amazon), and requires an agent to purchase a product based on a user instruction (e.g. "I am looking for a nightstand with drawers. It should have a nickel finish, and priced lower than $140" through web interactions (e.g. search "nightstand drawers"); choose buttons such as "color, modern-mickel-white" or "back to search"). This task is evaluated by average score (percentage of desired attributes covered by the chosen product averaged across all episodes) and success rate (percentage of episodes where the chosen product satisfied all requirements) on 600 test instructions. We formulate Act prompts with actions to search, choose product, choose options, and buy, with ReAct prompts additionally reasoning to determine what to explore, when to buy, and what products options are relevant to the instruction. See Table 6 for an example prompt, and Table 10 for model predictions in the Appendix. We compare to an imitation learning (IL) method

⁵ Micheli & Fleuret (2021) finetuned a GPT-2 model on 3553 task instances and achieved a much improved performance than BUTLER, but it is trained on all task types, thus not included as a baseline.

* * *

Method Pick Clean Heat Cool Look Pick 2 All

Act (best of) 88 42 74 67 72 41 45
ReAct (avg) 65 39 83 76 55 24 57
ReAct (best of) 92 58 96 86 78 41 71
ReAct-IM (avg) 55 59 60 55 23 24 48
ReAct-IM (best of) 62 68 87 57 39 33 53
BUTLER$\_{R}$ (best of) 33 26 70 76 17 12 22
BUTLER (best of) 46 39 74 100 22 24 37

Table 3: ALFWorld task-specific success rates (%). BUTLER and BUTLER$\_{R}$ results are from Table 4 of Shridhar et al. (2020b). All methods use greedy decoding, except that BUTLER uses beam search.

trained with 1,012 human annotated trajectories, and a imitation + reinforcement learning (IL + RL) method additionally trained with 10,587 training instructions.

Results ReAct outperforms Act on both ALFWorld (Table 3) and Webshop (Table 4). On ALFWorld, the best ReAct trial achieves an average success rate of 71%, significantly outperforming the best Act (45%) and BUTLER (37%) trials. In fact, even the worst ReAct trial beats the best trial of both methods. Moreover, the advantage of ReAct over Act is consistent across six controlled trials, with relative performance gain ranging from 33% to 90% and averaging 62%. Qualitatively, we saw that, without any thoughts at all, Act fails to correctly decompose goals into smaller subgoals, or loses track of the current state of the environment. Example trajectories comparing ReAct and Act can be found in Appendix D.2.1 and Appendix D.2.2.

On Webshop, one-shot Act prompting already performs on par with IL and I+RL methods. With additional sparse reasoning, ReAct achieves significantly better performance, with an absolute 10% improvement over the previous best success rate. By checking examples, we find that ReAct is more likely to identify instruction-relevant products and options by reasoning to bridge the gap between noisy observations and actions (e.g. "For space-saving ottoman bench for living room", the item has options, '39A 18.81 inch' and 'blue' and seems good to buy"). However, existing methods are still far from the performance of expert humans (Table 4), who perform significantly more product explorations and query re-formulations that are still challenging for prompting-based methods.

On the value of internal reasoning vs. external feedback To our knowledge, ReAct is the first demonstration of combined reasoning and action using an LLM applied to an interactive environment within a closed-loop system. Perhaps the closest prior work is Inner Monologue (IM), from Huang et al. (2022b), in which actions from an embodied agent are motivated by an eponymous "inner monologue". However, IM's "inner monologue" is limited to observations of the environment state and what needs to be completed by the agent for the goal to be satisfied. In contrast, the reasoning traces in ReAct for decision making is flexible and sparse, allowing diverse reasoning types (see Section 2) to be induced for different tasks.

To demonstrate the differences between ReAct and IM, and to highlight the importance of internal reasoning vs. simple reactions to external feedback, we ran an ablation experiment using a thought pattern composed of IM-like dense external feedback. As can be seen in Table 3, ReAct substantially outperforms IM (ReAct-I=10 (71) vs. 53, outperforms IM with enhanced advantages on five out of six tasks. Qualitatively, we observed that ReAct-I=IM often made mistakes in identifying when subgoals were finished, or what the next subgoal should be, due to a lack of high-level goal decomposition. Additionally, many ReAct-I=IM trajectories struggled to determine where an item would likely be within the ALFWorld environment, due to a lack of commonsense reasoning. Both shortcomings can be addressed in the ReAct paradigm. More details about ReAct-I=IM is in Appendix B.2. An example prompt for ReAct-I=IM can be found in Appendix C.4, and an example trajectory in Appendix D.2.3.

* * *

5 RELATED WORK

Language model for reasoning Perhaps the most well-known work of using LLMs for reasoning
is Chain-of-Thought (CoT) (Wei et al., 2022), which reveals the ability of LLMs to formulate their
own “thinking procedure” for problem solving. Several follow-up works have since been performed,
including least-to-most prompting for solving complicated tasks (Zhou et al., 2022), zero-shot-
CoT (Kojima et al., 2022), and reasoning with self-consistency (Wang et al., 2022a). Recently,
(Madaan & Yazdanbakhsh, 2022) systematically studied the formulation and structure of CoT, and
observed that the presence of symbols, patterns and texts is crucial to the effectiveness of CoT. Other
work has also been extended to more sophisticated reasoning architecture beyond simple prompting.
For example Selection-Inference (Creswell et al., 2022) divides the reasoning process into two steps
of “selection” and “inference”. STaR (Zelikman et al., 2022) bootstraps the reasoning process by
finetuning the model on correct rationales generated by the model itself. Faithful reasoning (Creswell
& Shanahan, 2022) decomposes multi-step reasoning into three steps, each performed by a dedicated
LM respectively. Similar approaches like Scratchpad (Nye et al., 2021), which finetunes a LM on
intermediate computation steps, also demonstrate improvement on multi-step computation problems.
In contrast to these methods, ReAct performs more than just isolated, fixed reasoning, and integrates
model actions and their corresponding observations into a coherent stream of inputs for the model to
reason more accurately and tackle tasks beyond reasoning (e.g. interactive decision making).

Language model for decision making The strong capability of LLMs has enabled them to perform
tasks beyond language generation, and it is becoming more popular to take advantage of LLMs as a
policy model for decision making, especially in interactive environments. WebGPT (Nakano et al.,
2021) uses an LM to interact with web browsers, navigate through web pages, and infer answers to
complicated questions from ELI5 (Fan et al., 2019). In comparison to ReAct, WebGPT does not
explicitly model the thinking and reasoning procedure, instead rely on expensive human feedback for
reinforcement learning. In conversation modeling, chatbots like BlenderBot (Shuster et al., 2022b)
and Sparrow (Glaese et al., 2022) and task-oriented dialogue systems like SimpleTOD (Hosseini-Asl
et al., 2020) also train LMs to make decision about API calls. Unlike ReAct, they do not explicitly
consider the reasoning procedure either, and also relies on expensive datasets and human feedback
collections for policy learning. In contrast, ReAct learns a policy in a much cheaper way, since the
6
decision making process only requires language description of the reasoning procedure.
LLMS have also been increasingly employed in interactive and embodied environments for planning

6 CONCLUSION

LLMS have also been increasingly employed in interactive and embodied environments for planning
and decision making. Perhaps most relevant to ReAct in this respect are SayCan (Ahn et al., 2022)
and Inner Monologue (Huang et al., 2022b), which use LLMs for robotic action planning and decision
making. In SayCan, LLMs were prompted to directly predict possible actions a robot can take, which
is then reranked by an affordance model grounded on the visual environments for final prediction.
Inner Monologue made further improvements by adding the eponymous “inner monologue", which is
implemented as injected feedback from the environment. To our knowledge, Inner Monologue is the
first work that demonstrates such a closed-loop system, which ReAct builds on. However, we argue
that Inner Monologue does not truly comprise of inner thoughts — this is elaborated in Section 4. We
also note that leveraging language as semantically-rich inputs in the process of interactive decision
making has been shown to be successful under other settings (Abramson et al., 2020; Karamcheti
et al., 2021; Huang et al., 2022a; Li et al., 2022). It is becoming more evident that with the help of
LLMs, language as a fundamental cognitive mechanism will play a critical role in interaction and
decision making. What is more, progress in LLMs has also inspired the development of versatile and
generalist agents like Reed et al. (2022).

* * *

with initial promising results, but learning from more high-quality human annotations will be the
desiderata to further improve the performance. Scaling up ReAct with multi-task training and
combining it with complementary paradigms like reinforcement learning could result in stronger
agents that further unlock the potential of LLMs for more applications.

ACKNOWLEDGMENTS

We thank the support and feedback of many people from Google Brain team and Princeton NLP
Group. This work was supported in part by the National Science Foundation under Grant No.
2107048\. Any opinions, findings, and conclusions or recommendations expressed in this material are
those of the author(s) and do not necessarily reflect the views of the National Science Foundation.

REPRODUCIBILITY STATEMENT

Our main experiments are done on PaLM (Chowdhery et al., 2022), which is not an openly accessible
model yet. To increase reproducibility, we have included all used prompts in Appendix C, additional
experiments using GPT-3 (Brown et al., 2020) in Appendix A.1, and associated GPT-3 ReAct
prompting code at [https://anonymous.4open.science/r/ReAct-2268/](https://anonymous.4open.science/r/ReAct-2268/).

ReAct prompts large language models to generate more human interpretable, diagnosable, and
controllable task-solving trajectories than previous methods. However, hooking up a large language
model with an action space to interact with external environments (e.g. the web, physical environments) has potential dangers, e.g. looking up inappropriate or private information, or taking harmful
actions in an environment. Our experiments minimize such risks by limiting the interactions to
specific websites (Wikipedia or WebShop) that are free of private information, without any dangerous
actions in the action space design (i.e. models cannot really buy products on WebShop the research
benchmark, or edit Wikipedia). We believe researchers should be aware of such risks before designing
more extensive experiments in the future.

REFERENCES

Josh Abramson, Arun Ahuja, Iain Barr, Arthur Brussee, Federico Carnevale, Mary Cassin, Rachita
Chhaparia, Stephen Clark, Bogdan Damoc, Andrew Dudzik, Petko Georgiev, Aurelia Guy, Tim
Harley, Felix Hill, Alden Hung, Zachary Kenton, Jessica Landon, Timothy Lillicrap, Kory Mathewson, Sona Mokrá, Alistair Muldal, Adam Santoro, Nikolay Savinov, Vikrant Varma, Greg Wayne, ˇ
Duncan Williams, Nathaniel Wong, Chen Yan, and Rui Zhu. Imitating interactive intelligence,
2020\. URL [https://arxiv.org/abs/2012.05672](https://arxiv.org/abs/2012.05672).

Alan Baddeley. Working memory. Science, 255(5044):556–559, 1992.

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.

* * *

Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm:
Scaling language modeling with pathways. arXiv preprint arXiv:2204.02311, 2022.

Antonia Creswell and Murray Shanahan. Faithful reasoning using large language models, 2022. URL
[https://arxiv.org/abs/2208.14271](https://arxiv.org/abs/2208.14271).

Antonia Creswell, Murray Shanahan, and Irina Higgins. Selection-inference: Exploiting large
language models for interpretable logical reasoning, 2022. URL [https://arxiv.org/abs/](https://arxiv.org/abs/)
2205.09712.

Angela Fan, Yacine Jernite, Ethan Perez, David Grangier, Jason Weston, and Michael Auli. ELI5:
Long form question answering. In Proceedings of the 57th Annual Meeting of the Association
for Computational Linguistics, pp. 3558–3567, Florence, Italy, July 2019. Association for Computational Linguistics. doi: 10.18653/v1/P19-1346. URL [https://aclanthology.org/](https://aclanthology.org/)
P19-1346.

Charles Fernyhough. Vygotsky, luria, and the social brain. Self and social regulation: Social
interaction and the development of social understanding and executive functions, pp. 56–79, 2010.

Amelia Glaese, Nat McAleese, Maja Trebacz, John Aslanides, Vlad Firoiu, Timo Ewalds, Maribeth Rauh, Laura Weidinger, Martin Chadwick, Phoebe Thacker, Lucy Campbell-Gillingham,
Jonathan Uesato, Po-Sen Huang, Ramona Comanescu, Fan Yang, Abigail See, Sumanth
Dathathri, Rory Greig, Charlie Chen, Doug Fritz, Jaume Sanchez Elias, Richard Green,
Sonaˇ Mokrá, Nicholas Fernando, Boxi Wu, Rachel Foley, Susannah Young, Iason Gabriel,
William Isaac, John Mellor, Demis Hassabis, Koray Kavukcuoglu, Lisa Anne Hendricks, and
Geoffrey Irving. Improving alignment of dialogue agents via targeted human judgements,
2022\. URL [https://storage.googleapis.com/deepmind-media/DeepMind](https://storage.googleapis.com/deepmind-media/DeepMind).
com/Authors-Notes/sparrow/sparrow-final.pdf.

Ehsan Hosseini-Asl, Bryan McCann, Chien-Sheng Wu, Semih Yavuz, and Richard Socher. A simple
language model for task-oriented dialogue. Advances in Neural Information Processing Systems,
33:20179–20191, 2020.

Siddharth Karamcheti, Megha Srivastava, Percy Liang, and Dorsa Sadigh. Lila: Language-informed
latent actions. In CoRL, pp. 1379–1390, 2021. URL [https://proceedings.mlr.press/](https://proceedings.mlr.press/)
v164/karamcheti22a.html.

Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. Large
language models are zero-shot reasoners. arXiv preprint arXiv:2205.11916, 2022.

Angeliki Lazaridou, Elena Gribovskaya, Wojciech Stokowiec, and Nikolai Grigorev. Internetaugmented language models through few-shot prompting for open-domain question answering.
arXiv preprint arXiv:2203.05115, 2022.

* * *

Aleksandr Romanovich Luria. Ls vygotsky and the problem of localization of functions. Neuropsychologia, 3(4):387–392, 1965.

Aman Madaan and Amir Yazdanbakhsh. Text and patterns: For effective chain of thought, it takes
two to tango, 2022. URL [https://arxiv.org/abs/2209.07686](https://arxiv.org/abs/2209.07686).

Vincent Micheli and François Fleuret. Language models are few-shot butlers. arXiv preprint
arXiv:2104.07972, 2021.

Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher
Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, Xu Jiang, Karl Cobbe, Tyna Eloundou,
Gretchen Krueger, Kevin Button, Matthew Knight, Benjamin Chess, and John Schulman. Webgpt:
Browser-assisted question-answering with human feedback, 2021. URL [https://arxiv](https://arxiv/).
org/abs/2112.09332.

Maxwell Nye, Anders Johan Andreassen, Guy Gur-Ari, Henryk Michalewski, Jacob Austin, David
Bieber, David Dohan, Aitor Lewkowycz, Maarten Bosma, David Luan, Charles Sutton, and
Augustus Odena. Show your work: Scratchpads for intermediate computation with language
models, 2021. URL [https://arxiv.org/abs/2112.00114](https://arxiv.org/abs/2112.00114).

Scott Reed, Konrad Zolna, Emilio Parisotto, Sergio Gomez Colmenarejo, Alexander Novikov,
Gabriel Barth-Maron, Mai Gimenez, Yury Sulsky, Jackie Kay, Jost Tobias Springenberg, Tom
Eccles, Jake Bruce, Ali Razavi, Ashley Edwards, Nicolas Heess, Yutian Chen, Raia Hadsell,
Oriol Vinyals, Mahyar Bordbar, and Nando de Freitas. A generalist agent, 2022. URL https:
//arxiv.org/abs/2205.06175.

Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan Bisk, Winson Han, Roozbeh Mottaghi,
Luke Zettlemoyer, and Dieter Fox. Alfred: A benchmark for interpreting grounded instructions
for everyday tasks. In Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition, pp. 10740–10749, 2020a.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté, Yonatan Bisk, Adam Trischler, and Matthew

Kurt Shuster, Jing Xu, Mojtaba Komeili, Da Ju, Eric Michael Smith, Stephen Roller, Megan Ung,
Moya Chen, Kushal Arora, Joshua Lane, Morteza Behrooz, William Ngan, Spencer Poff, Naman
Goyal, Arthur Szlam, Y-Lan Boureau, Melanie Kambadur, and Jason Weston. Blenderbot 3:
a deployed conversational agent that continually learns to responsibly engage, 2022b. URL
[https://arxiv.org/abs/2208.03188](https://arxiv.org/abs/2208.03188).

James Thorne, Andreas Vlachos, Christos Christodoulopoulos, and Arpit Mittal. Fever: a large-scale
dataset for fact extraction and verification. arXiv preprint arXiv:1803.05355, 2018.

Lev S Vygotsky. Thinking and speech. The collected works of LS Vygotsky, 1:39–285, 1987.

Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models,
2022a. URL [https://arxiv.org/abs/2203.11171](https://arxiv.org/abs/2203.11171).

Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William W Cohen, Ruslan Salakhutdinov,
and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question
answering. arXiv preprint arXiv:1809.09600, 2018.

* * *

Shunyu Yao, Rohan Rao, Matthew Hausknecht, and Karthik Narasimhan. Keep CALM and explore:
Language models for action generation in text-based games. In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Processing (EMNLP), pp. 8736–8754, Online, November 2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.emnlp-main.704.
URL [https://aclanthology.org/2020.emnlp-main.704](https://aclanthology.org/2020.emnlp-main.704).

Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable
real-world web interaction with grounded language agents. arXiv preprint arXiv:2207.01206,
2022.

Eric Zelikman, Yuhuai Wu, Jesse Mu, and Noah D. Goodman. Star: Bootstrapping reasoning with
reasoning, 2022. URL [https://arxiv.org/abs/2203.14465](https://arxiv.org/abs/2203.14465).

Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei, Nathan Scales, Xuezhi Wang, Dale Schuurmans,
Olivier Bousquet, Quoc Le, and Ed Chi. Least-to-most prompting enables complex reasoning in
large language models, 2022. URL [https://arxiv.org/abs/2205.10625](https://arxiv.org/abs/2205.10625).

Yunchang Zhu, Liang Pang, Yanyan Lan, Huawei Shen, and Xueqi Cheng. Adaptive information
seeking for open-domain question answering. arXiv preprint arXiv:2109.06747, 2021.

* * *

A ADDITIONAL RESULTS

A.1 GPT-3 EXPERIMENTS

| | PaLM-540B | GPT-3 |
| --- | --- | --- |
| HotpotQA(exact match) | 29.4 | 30.8 |
| ALFWorld(success rate%) | 70.9 | 78.4 |

Table 5: ReAct prompting results using PaLM-540B vs. GPT-3 (text-davinci-002, greedy decoding).
On HotpotQA, we randomly sample a subset of 500 validation questions. On ALFWorld, we use all
134 unseen validation task instances, and use the best prompt set according to PaLM-540B.

We run additional GPT-3 (Brown et al., 2020) experiments to confirm ReAct prompting performance
is general across different large language models. As shown in Table 5, GPT-3 (text-davinci-002,
greedy decoding) consistently outperforms PaLM-540B on HotpotQA and ALFWorld, possibly
because it is finetuned with human instruction following. This indicates ReAct prompting is effective
across different large language models on different tasks. The code for these experiments are at
[https://react-lm.github.io/](https://react-lm.github.io/).

A.2 REAC T OBTAINS UP-TO-DATE KNOWLEDGE ON HOTPOTQA

Figure 4: Another example HotpotQA question, where the original label is outdated. Only ReAct is
able to obtain the up-to-date answer thanks to real-world web interaction plus reasoning.
During trajectory inspection, we also find that sometimes ReAct does not agree with dataset labels as

We also explore human-in-the-loop interaction with ReAct, to allow a human to inspect and edit
ReAct’s reasoning traces. Figure 5 shows that by simply removing a hallucinating sentence in Act
17 and adding some hints in Act 23, ReAct can be made to change its behavior drastically to align
with these human thought edits and succeed in the task. From a human perspective, solving such a
task becomes significantly easier, from typing tens of actions to only editing a couple of thoughts,
which enables new forms of human-machine collaboration. We note that such a policy edit on-the-go

During trajectory inspection, we also find that sometimes ReAct does not agree with dataset labels as
the labels themselves could be outdated. For example, as shown in Figure 4, the question asks about
the size of a hotel, which increased from the HotpotQA construction time. While Standard and CoT
give wrong answers due to hallucination, Act fails despite the access of real-world web interaction,
due to a lack of reasoning to guide how to interact with the Internet for QA. Only ReAct is able to
retrieve up-to-date information from the Internet and provide a reasonable answer. Therefore, better
incorporation of reasoning abilities might benefit recent Internet-augmented language models (Nakano
et al., 2021; Lazaridou et al., 2022; Shuster et al., 2022a) for up-to-date task solving.

* * *

Figure 5: A human-in-the-loop behavior correction example with ReAct in AlfWorld. (a) ReAct
trajectory fails due to a hallucinating thought (Act 17). (b) By a human simply editing two thoughts
(Act 17, 23), the ReAct trajectory produces desirable reasoning traces and actions and succeeds.

$$
\\mathrm {R e A c t}
$$

is difficult for Act and previous RL methods, as a human cannot change the model parameters, and
changing a few actions might not edit the rest of the model behavior. This paradigm is also more than
human dialogue to update the goal or subgoal as in Huang et al. (2022b) — while editing ReAct
thoughts can do these, it can also modify the model’s internal belief, reasoning styles, or anything the
flexible thought space supports, for better task solving. We believe this is an exciting direction for
human alignment and leave more systematic study as future work.

B EXPERIMENT DETAILS

B.1 HOTPOTQA FINETUNING DETAILS

For the IM-style ablation, the same expert trajectories used in ReAct are reannotated with dense
external feedback thoughts within these trajectories, that limit ReAct-IM to only think about (1)
decomposing the current goal and (2) the current subgoal that needs to be completed. In particular,
ReAct-IM lacks thoughts that (1) determine when a subgoal is completed (2) determine what the
next subgoal should be (3) inducing the LLM to refer to its internal pretraining knowledge to identify
where items can be within the environment.

* * *

C PROMPTS

C.1 HOTPOTQA

Hotpot QA Prompts

| Hotpot QA Prompts | |
| --- | --- |
| Question | What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? |
| Answer | 1,800 to 7,000 ft |
| Question | Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who? |
| Answer | Richard Nixon |
| Question | Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture? |
| Answer | The Saimaa Gesture |
| Question | What profession does Nicholas Ray and Elia Kazan have in common? |
| Answer | director, screenwriter, actor |
| Question | Which magazine was started first Arthur's Magazine or First for Women? |
| Answer | Arthur's Magazine |
| Question | Were Pavel Urysohn and Leonid Levin known for the same type of work? |
| Answer | Yes |
| | |
| Question | What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? |
| Action 1 | Search\[Colorado orogeny\] |
| Observation 1 | The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. |
| Action 2 | Lookup\[eastern sector\] |
| Observation 2 | (Result 1/1) The eastern sector extends into the High Plains and is called the Central Plains orogeny. |
| Action 3 | Search\[High Plains\] |
| Observation 3 | High Plains refers to one of two distinct land regions: |
| Action 4 | Search\[High Plains (United States)\] |
| Observation 4 | The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m). \[3\] |
| Action 5 | Finish\[1,800 to 7,000 ft\] |
| Question | Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who? |
| Action 1 | Search\[Milhouse\] |
| Observation 1 | Milhouse Musolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening. |
| Action 2 | Lookup\[named after\] |
| Observation 2 | (Result 1/1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhouh. |
| Action 3 | Finish\[Richard Nixon\] |
| Question | Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture? |
| Action 1 | Search\[Adam Clayton Powell\] |
| Observation 1 | Could not find \[Adam Clayton Powell\]. Similar: 'Adam Clayton Powell III', 'Seventh Avenue (Manhattan)', 'Adam Clayton Powell Jr. State Office Building', 'Isabel Washington Powell', 'Adam Powell', 'Adam Clayton Powell (film)', 'Giancarlo Esposito'). |
| Action 2 | Search\[Adam Clayton Powell (film)\] |
| Observation 2 | Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg. The film is about the rise and fall of influential African-American politician Adam Clayton Powell Jr.\[3\]\[4\] It was later aired as part of the PBS series The American Experience. |
| Action 3 | Finish\[The Saimaa Gesture\] |
| Question | What profession does Nicholas Ray and Elia Kazan have in common? |
| Action 1 | Search\[Nicholas Ray\] |
| Observation 1 | Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911-June 16, 1979) was an American film director, screenwriter, and actor best known for the 1955 film Rebel Without a Cause. |
| Action 2 | Search\[Elia Kazan\] |
| Observation 2 | Elia Kazan was an American film and theatre director, producer, screenwriter and actor. |

Continued on next page

* * *

Hotpot QA Prompts – Continued from previous page

| Action 3 | Finish\[director, screenwriter, actor\] |
| --- | --- |
| Question | Which magazine was started first Arthur's Magazine or First for Women? |
| Action 1 | Search\[Arthur's Magazine\] |
| Observation 1 | Arthur's Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century. |
| Action 2 | Search\[First for Women\] |
| Action 2 | First for Women is a woman's magazine published by Bauer Media Group in the USA.\[1\] The magazine was started in 1989. |
| Action 3 | Finish\[Arthur's Magazine\] |
| Question | Were Pavel Urysohn and Leonid Levin known for the same type of work? |
| Action 1 | Search\[Pavel Urysohn\] |
| Observation 1 | Pavel Samuliovich Urysohn (February 3, 1898 - August 17, 1924) was a Soviet mathematician who is best known for his contributions in dimension theory. |
| Action 2 | Search\[Leonid Levin\] |
| Observation 2 | Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist. |
| Action 3 | Finish\[yes\] |
| NO | |
| Question | What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? |
| Thought | Let's think step by step. The eastern sector of Colorado orogeny extends into the High Plains. High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft. |
| Answer | 1,800 to 7,000 ft |
| Question | Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who? |
| Thought | Let's think step by step. Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon. |
| Answer | Richard Nixon |
| Question | Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture? |
| Thought | Let's think step by step. Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups. So the documentary about Finnish rock groups must instead be The Saimaa Gesture. |
| Answer | The Saimaa Gesture |
| Question | What profession does Nicholas Ray and Elia Kazan have in common? |
| Thought | Let's think step by step. Professions of Nicholas Ray are director, screenwriter, and actor. Professions of Elia Kazan are director, producer, screenwriter and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor. |
| Answer | director, screenwriter, actor |
| Question | Which magazine was started first Arthur's Magazine or First for Women? |
| Thought | Let's think step by step. Arthur's Magazine was started in 1844. First women was started in 1898 or 1844 (Arthur's Magazine) < 1989 (First for Women), so Arthur's Magazine was started first. |
| Answer | Arthur's Magazine |
| Question | Were Pavel Urysohn and Leonid Levin known for the same type of work? |
| Thought | Let's think step by step. Pavel Urysohn is a mathematician. Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn and Leonid Levin have the same type of work. |
| Answer | Yes |
| ROACE | |
| Question | What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into? |
| Thought 1 | I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into, then find the elevation range of the area. |
| Action 1 | Search\[Colorado orogeny\] |
| Observation 1 | The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas. |
| Thought 2 | It does not mention the eastern sector. So I need to look up eastern sector. |
| Action 2 | Lookup\[eastern sector\] |
| Observation 2 | The eastern sector extends into the High Plains and is called the Central Plains orogeny. |
| Thought 3 | The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range. |
| Action 3 | Search\[High Plains\] |
| Observation 3 | High Plains refers to one of two distinct land regions. |
| Thought 4 | I need to instead search High Plains (United States). |
| Action 4 | Search\[High Plains (United States)\] |

Continued on next page

* * *

Hotpot QA Prompts – Continued from previous page

| Observation 4 | The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation from around 1,800 to 7,000 ft (550 to 2,130 m).\[3\] |
| --- | --- |
| Thought 5 | High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft. |
| Action 1 | Finish\[1,800 to 7,000 ft\] |
| Question | Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who? |
| Thought 1 | The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and find who it is named after. |
| Action 1 | Search Milhouse. |
| Observation 1 | Milhouse was Masekini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced by Pamela Hayden and created by Matt Groening. |
| Thought 2 | The paragraph does not tell who Milhouse is named after, maybe I can look up "named after". |
| Action 2 | Lookup\[named after\] |
| Observation 2 | (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name Milhouse. |
| Thought 3 | Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon. |
| Action 3 | Finish\[Richard Nixon\] |
| Question | Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture? |
| Thought 1 | I asked to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups. |
| Action 1 | Search\[Adam Clayton Powell\] |
| Observation 1 | Could not find \[Adam Clayton Powell\]. Similar: \['Adam Clayton Powell III', 'Seventh Avenue (Manhattan)', 'Adam Clayton Powell Jr. State Office Building', 'Isabel Washington Powell', 'Adam Powell', 'Adam Clayton Powell (film)", 'Giancarlo Esposito'\]. |
| Thought 2 | To find the documentary, I can search Adam Clayton Powell (film) |
| Action 2 | Search\[Adam Clayton Powell (film)\] |
| Observation 2 | Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg. The film is about the rise and fall of influential African-American politician Adam Clayton Powell Jr.\[3\]\[4\] It was later aired as part of the PBS series The American Experience. |
| Thought 3 | Adam Clayton Powell (film) is a documentary about an African-American political activist. So the documentary about Finnish rock groups must instead be The Saimaa Gesture. |
| Action 3 | Finish\[The Saimaa Gesture\] |
| Question | What profession does Nicholas Ray and Elia Kazan have in common? |
| Thought 1 | I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common. |
| Action 1 | Search\[Nicholas Ray\] |
| Observation 1 | Nicholas Ray (born Raymond Nicholas Kienlez Jr., August 7, 1911-June 16, 1979) was an American film director, screenwriter, and actor best known for the 1955 film Rebel Without a Cause. |
| Thought 2 | Professions of Nicholas Ray are director, screenwriter, and actor. I need to search Elia Kazan next and find his professions. |
| Action 2 | Search\[Elia Kazan\] |
| Observation 2 | Profession was an American film and theatre director, producer, screenwriter and actor. |
| Thought 3 | Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan have in common is director, screenwriter, and actor. |
| Action 3 | Finish\[director, screenwriter, actor\] |
| Question | Which magazine was started first Arthur's Magazine or First for Women? |
| Thought 1 | I need to search Arthur's Magazine and First for Women, and find which was started first. |
| Action 1 | Search\[Arthur's Magazine\] |
| Observation 1 | Arthur's Magazine (1844-1846) was an American literary periodical published in Philadelphia in the 19th century. |
| Thought 2 | Arthur's Magazine was started in 1844. I need to search First for Women next. |
| Action 2 | Search\[First for Women\] |
| Observation 2 | First for Women was started in 1989. 1844 (Arthur's Magazine) < 1989 (First for Women), so Arthur's Magazine was started first. |
| Action 3 | Finish\[Arthur's Magazine\] |
| Question | Were Pavel Uryshn and Leonid Levin known for the same type of work? |
| Thought 1 | I need to search Pavel Uryshn and Leonid Levin, find their types of work, then find if they are the same. |
| Action 1 | Search\[Pavel Uryshn\] |

Continued on next page

* * *

Hotpot QA Prompts – Continued from previous page

| Observation 1 | Pavel Samuilovich Urysohn(February3,1898-August17,1924)was a Soviet mathematician who is best known for his contributions in dimension theory. |
| --- | --- |
| Thought 2 | Pavel Urysohn is a mathematician.I need to search Leonid Levin next and find its type of work. |
| Action 2 | Search\[Leonid Levin\] |
| Observation 2 | Leonid Anatolievich Levin is a Soviet-American mathematician and computer scientist. |
| Thought 3 | Leonid Levin is a mathematician and computer scientist.So Pavel Urysohn and Leonid Levin have the same type of work. |
| Action 3 | Finish\[yes\] |

* * *

C.2 FEVER

FEVER Prompts

| FEVER Prompts | |
| --- | --- |
| Original | Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. |
| Claim Answer | Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. SUPPORTS |
| Claim Answer | Stranger Things is set in Bloomington, Indiana. REFUTES |
| Claim Answer | Beautiful reached number two on the Billboard Hot 100 in 2003. NOT ENOUGH INFO |
| | Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. |
| Claim Action2 | Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. Search\[Nikolaj Coster-Waldau\] |
| Observation1 | Nikolaj William Coster-Waldau (born 27 July 1970) is a Danish actor and producer. He graduated from the Danish National School of Performing Arts in Openhagen in 1983 \[1\] and had his breakthrough role in Denmark with the film Nightwatch (1994). He played Jaime Lannister in the HBO fantasy drama series Game of Thrones, for which he received two Primetime Emmy Award nominations for Outstanding Supporting Actor in a Drama Series..Coster-Waldau has appeared in numerous films in his native Denmark and Scandinavia, including Headhunters (2011) and A Thousand Times Good Night (2013). In the U.S., his debut film role was in the war film Black Hawk Down (2001), playing Medal of Honor recipient Gary Gordon \[2\]. He then played a detective in the short-lived Fox television series New Amsterdam (2008), and appeared in the 2009 Fox television film Virtuality, originally intended as a pilot. |
| Action2 | Finish\[SUPPORTS\] |
| Claim Action1 | Stranger Things is set in Bloomington, Indiana. Search\[Stranger Things\] |
| Observation1 | Stranger Things is an American science fiction horror drama television series created by the Duffer Brothers. Set in the 1980s, primarily in the fictional town of Hawkins, Indiana, the series centers on a number of mysteries and supernatural events occurring around the town and their impact on an ensemble of child and adult characters. |
| Action2 | Finish\[REFUTES\] |
| Claim Action1 | Beautiful reached number two on the Billboard Hot 100 in 2003. |
| Observation1 | Could not find\[Beautiful\]. Similar: \['Beautiful', 'Beautiful, Beautiful', 'A Beautiful Mind (film)', 'Beautiful (Christina Aguilera song)', 'Life Is Beautiful'\]. |
| Action2 | Search\[Beautiful (Christina Aguilera song)\] |
| Observation2 | "Beautiful" is a song recorded by American singer Christina Aguilera for her fourth studio album, Stripped (2002). |
| Action3 | Lookup\[Billboard Hot 100\](Result 1/3) The song peaked at number two on the Billboard Hot 100 in the United States, where it was certified Gold for 500,000 units shipped. |
| Action4 | Finish\[NOT ENOUGH INFO\] |
| | Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. |
| Claim Thought | Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. Nikolaj William Coster-Waldau appeared in the 2009 Fox television film Virtuality, so he has worked with the Fox Broadcasting Company. |
| Answer | SUPPORTS |
| Claim Thought | Stranger Things is set in Bloomington, Indiana. Stranger Things is in the fictional town of Hawkins, Indiana, not in Bloomington, Indiana. |
| Answer | REFUTES |

Continued on next page

* * *

Fever Prompts – Continued from previous page

| Fever Prompts – Continued from previous page | |
| --- | --- |
| Claim | Beautiful reached number two on the Billboard Hot 100 in 2003. |
| Thought | The song peaked at number two on the Billboard Hot 100 in the United States, but not sure if it was in 2003. |
| Answer | NOT ENOUGH INFO |
| ReAct | Determine if there is Observation that SUPPORTS or REFUTES a Claim, or if there is NOT ENOUGH INFORMATION. |
| Claim | Nikolaj Coster-Waldau worked with the Fox Broadcasting Company. |
| Thought 1 | I need to search Nikolaj Coster-Waldau and find if he has worked with the Fox Broadcasting Company. |
| Action 1 | Search(Nikolaj Coster-Waldau) |
| Observation 1 | Nikolaj William Coster-Waldau (born 27 July 1970) is a Danish actor and producer. He graduated from the Danish National School of Performing Arts in Copenhagen in 1993,\[1\] and had his breakthrough role in Denmark with the film Nightwatch (1994). He played Jaime Lannister in the HBO fantasy drama series Game of Thrones, for which he received two Primetime Emmy Award nominations for Outstanding Supporting Actor in a Drama Series..Coster-Waldau has appeared in numerous films in his native Denmark and Scandinavia, including Headhunters (2011) and A Thousand Times Good Night(2013).In the U.S, his debut film role was in the war film Black Hawk Down(2001), playing Medal of Honor recipient Gary Gordon.\[2\]He then played a detective in the short-lived Fox television series New Amsterdam(2008), and appeared in the 2009 Fox television film Virtuality, originally intended as a pilot. |
| Thought 2 | Because he "appeared in the 2009 Fox television film Virtuality", he should have worked with the Fox Broadcasting Company. |
| Action 2 | Finish\[SUPPORTS\] |
| Claim | Stranger Things is set in Bloomington, Indiana. |
| Thought 1 | I should search for Stranger Things, and see if it is set in Bloomington, Indiana. |
| Action 1 | Search\[Stranger Things\] |
| Observation 1 | Stranger Things is an American science fiction horror drama television series created by the Duffer Brothers.Set in the 1980s, primarily in the fictional town of Hawkins, Indiana,the series centers on a number of mysteries and supernatural events occurring around the town and their impact on an ensemble of child and adult characters. |
| Thought 2 | The observation says that it is set in a "fictional town of Hawkins, Indiana", so it is not set in Bloomington. |
| Action 2 | Finish\[REFUTES\] |
| Claim | Beautiful reached number two on the Billboard Hot 100 in 2003. |
| Thought 1 | I need to search the song Beautiful and find if it reached number two on the Billboard Hot 100 in 2003. |
| Action 1 | Search\[Beautiful\] |
| Observation 1 | Could not find \[Beautiful\].Similar:\['Beautiful',‘Beautiful, Beautiful’,‘A Beautiful Mind (film)’,‘Beautiful (Christina Aguilera song)’,‘Life Is Beautiful'\]. |
| Thought 2 | From suggestions, I should search "Beautiful (Christina Aguilera song)" to find the song. |
| Action 2 | Search\[Beautiful (Christina Aguilera song)\] |
| Observation 2 | "Beautiful" is a song recorded by American singer Christina Aguilera for her fourth studio album, Stripped(2002). |
| Thought 3 | It does not mention Billboard,so I need to look up "Billboard Hot 100" to find if it reached number two on it in 2003. |
| Action 3 | Lookup(Billboard Hot 100) |
| Observation 3 | (Result 1/3) The song peaked at number two on the Billboard Hot 100 in the United States,where it was certified Gold for 500,000 units shipped. |
| Thought 4 | It only says the song peaked at number two on the Billboard Hot 100,but not if it was in 2003.I am not sure if this claim is true or not. |
| Action 4 | Finish\[NOT ENOUGHINFO\] |

* * *

C.3 WEBSHOP

Table 6: Prompts used for the Webshop experiments in Section 4. We use the prompt on the left for
Act, and use the prompt on the right (add reasoning) for ReAct.

| Act | ReAct |
| --- | --- |
| Action: search \[3 ounce bright citrus deodorant sensitive skin\]Observation:\[ Back to Search \]Page 1 (Total results: 50)\[Next\] | Action: search \[3 ounce bright citrus deodorant sensitive skin\]Observation:\[ Back to Search \]Page 1 (Total results: 50)\[Next\] |
| \[B078GWRC1J\]Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce$10.99 |
| \[B078GTKVXY\]Ginger Fresh Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-Ounce$10.99 |
| \[B08KBVJ4XN\]Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men , Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar &Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack)$15.95 | \[B08KBVJ4XN\]Barrel and Oak - Aluminum-Free Deodorant, Deodorant for Men , Essential Oil-Based Scent, 24-Hour Odor Protection, Cedar &Patchouli Blend, Gentle on Sensitive Skin (Mountain Sage, 2.7 oz, 2-Pack)$15.95 |
| Action: click \[B078GWRC1J\]Observation:\[ Back to Search \]\[Prev\]scent \[assorted scents\]\[bright citrus\]\[calming lavender\]\[ginger \[fresh\] simply non-scents\]size \[travel set (4-pack)\]\[3 ounce (pack of 1)\]\[3-ounce (2-pack)\]Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-OuncePrice: $10.99Rating: N.A.\[Description\]\[Features\]\[Reviews\]\[Buy Now\] |
| Action: click \[B078GWRC1J\]Observation:\[ Back to Search \]\[Prev\]scent \[assorted scents\]\[bright citrus\]\[calming lavender\]\[ginger \[fresh\] simply non-scents\]size \[travel set (4-pack)\]\[3 ounce (pack of 1)\]\[3-ounce (2-pack)\]Bright Citrus Deodorant by Earth Mama | Natural and Safe for Sensitive Skin, Pregnancy and Breastfeeding, Contains Organic Calendula 3-OuncePrice: $10.99Rating: N.A.\[Description\]\[Features\]\[Reviews\]\[Buy Now\] |
| Action: click \[bright citrus\]Observation: You have clicked bright citrus. | Action: click \[bright citrus\]Observation: You have clicked bright citrus. |
| Action: click \[3 ounce (pack of 1)\]Observation: You have clicked 3 ounce (pack of 1). | Action: click \[3 ounce (pack of 1)\]Observation: You have clicked 3 ounce (pack of 1). |
| Action: click \[Buy Now\] | Action: click \[Buy Now\] |

* * *

Table 7: An Act prompt on the ALFWorld clean task. No thoughts are provided.

C.4 ALFWORLD

You are in the middle of a room. Looking quickly around you, you see a cabinet
13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet
7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet
1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a
garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a
stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.

> go to fridge 1
> The fridge 1 is closed.
> open fridge 1
> You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a
> potato 3, and a potato 2.
> go to diningtable 1
> On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a
> fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a
> peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.
> take lettuce 1 from diningtable 1
> You pick up the lettuce 1 from the diningtable 1.
> go to sinkbasin 1
> On the sinkbasin 1, you see a apple 2, a ladle 2, a spoon 1, and a tomato 3.
> clean lettuce 1 with sinkbasin 1
> You clean the lettuce 1 using the sinkbasin 1.
> think: Now I clean a lettuce (1). Next, I need to put it in/on diningtable 1.
> OK.
> go to diningtable 1
> On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a fork
> 2, a knife 2, a knife 1, a ladle 1, a mug 2, a mug 1, a pan 2, a peppershaker 1, a
> spatula 3, a tomato 2, and a tomato 1.
> put lettuce 1 in/on diningtable 1
> You put the lettuce 1 in/on the diningtable 1.

* * *

Table 8: An ReAct prompt on the ALFWorld clean task.

You are in the middle of a room. Looking quickly around you, you see a cabinet
13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet
7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet
1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a
garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a
stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean lettuce in diningtable.

> think: To solve the task, I need to find and take a lettuce, then clean it with
> sinkbasin, then put it in countertop.
> OK.
> think: First I need to find a lettuce. A lettuce is more likely to appear in
> fridge (1), diningtable (1), sinkbasin (1), stoveburner (1-3), cabinet (1-13). I
> can check one by one, starting with fridge 1.
> OK.
> go to fridge 1
> The fridge 1 is closed.
> open fridge 1
> You open the fridge 1. The fridge 1 is open. In it, you see a cup 3, a egg 2, a
> potato 3, and a potato 2.
> go to diningtable 1
> On the diningtable 1, you see a apple 1, a bread 1, a butterknife 2, a cup 2, a
> fork 2, a knife 2, a knife 1, a ladle 1, a lettuce 1, a mug 2, a mug 1, a pan 2, a
> peppershaker 1, a spatula 3, a tomato 2, and a tomato 1.
> think: Now I find a lettuce (1). Next, I need to take it.
> OK.
> take lettuce 1 from diningtable 1
> You pick up the lettuce 1 from the diningtable 1.
> think: Now I take a lettuce (1). Next, I need to go to sinkbasin (1) and clean
> it.
> OK.
> go to sinkbasin 1
> On the sinkbasin 1, you see a fork 3, a lettuce 3, and a spatula 2.
> clean knife 1 with sinkbasin 1
> You clean the knife 1 using the sinkbasin 1.
> think: Now I clean a knife (1). Next, I need to put it in/on countertop 1.
> OK.
> go to countertop 1
> On the countertop 1, you see a lettuce 2, a mug 2, a peppershaker 1, and a spoon 2.
> put knife 1 in/on countertop 1
> You put the knife 1 in/on the countertop 1.

* * *

Table 9: An ReAct-IM prompt on the ALFWorld clean task.

You are in the middle of a room. Looking quickly around you, you see a cabinet
13, a cabinet 12, a cabinet 11, a cabinet 10, a cabinet 9, a cabinet 8, a cabinet
7, a cabinet 6, a cabinet 5, a cabinet 4, a cabinet 3, a cabinet 2, a cabinet
1, a coffeemachine 1, a countertop 1, a diningtable 1, a drawer 1, a fridge 1, a
garbagecan 1, a microwave 1, a shelf 3, a shelf 2, a shelf 1, a sinkbasin 1, a
stoveburner 4, a stoveburner 3, a stoveburner 2, a stoveburner 1, and a toaster 1.
Your task is to: put a clean knife in countertop.

> think: To solve the task, I need to find and take a clean knife, then put it in
> countertop.
> OK.
> think: I need to find a clean knife.
> OK.
> go to countertop 1
> On the countertop 1, you see a lettuce 2, a mug 2, a peppershaker 1, and a spoon 2.
> think: I need to find a clean knife.
> OK.
> go to countertop 2
> On the countertop 2, you see a cup 1, a dishsponge 1, a glassbottle 3, a knife 1, a
> plate 2, a potato 3, and a statue 1.
> think: I need to find a clean knife.
> OK.
> take knife 1 from countertop 2
> You pick up the knife 1 from the countertop 2.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> go to countertop 1
> On the countertop 1, you see a lettuce 2, a mug 2, a peppershaker 1, and a spoon 2.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> put knife 1 in/on countertop 1
> You put the knife 1 in/on the countertop 1.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> put knife 1 in/on countertop 1
> Nothing happens.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> put knife 1 in/on countertop 1
> Nothing happens.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> put knife 1 in/on countertop 1
> Nothing happens.
> think: I need to put this knife (1) in/on countertop 1.
> OK.
> put knife 1 in/on countertop 1
> Nothing happens.
> think: I need to put this knife (1) in/on countertop 1.
> OK.

* * *

D.3 WEBSHOP TRAJECTORIES

Table 10: Example trajectories for Webshop predicted by Act and ReAct. Compared to Act,
ReAct uses reasoning to find products that satisfy all target attributes.

| Instruction: get me a sixteen pack of apple cinnamon freeze dried banana chips, and price lower than 50.00 dollars | |
| --- | --- |
| Act React | |
| Action: search \[sixteen pack apple cinnamon freeze dried banana chips\] | |
| Observation: | |
| \[Back to Search\] | |
| Page 1 (Total results: 50) | |
| \[Next\] | |

\[B00611VFZE\]
Brothers-ALL-Natural Fruit Crisps, Strawberry Banana, 0.42 - Ounce(Pack of 100)
$85.0

\[B096H2P6G2\]
Moon Fruit Freeze Dried Fruit Snacks. Fruit Snacks for Kids-(Variety Pack)
$18.99

\[B092JLLYK6\]
Nature's Turn Freeze-Dried Fruit Snacks-Banana Crisps-PerfectFor School Lunches or an On-The-Go Snack-No Sugar Added,Non GMO,Gluten Free,Nothing Artificial(0.53oz)6-Pack$12.99 \| \|
\| Action: click \[B00611VFZE\]
Observation:
\[Back to Search\]
\[Prev\]
flavor name \[asian pear\]banana\]\[fuji apple & cinnamon\]strawberrybanana Brothers-ALL-Natural Fruit Crisps, Strawberry Banana,0.42 Ounce(Pack of 100)
Price:$85.0
Rating:N.A.
\[Description\]
\[Features\]
\[Reviews\]
\[Buy Now\] \| Action: search \[sixteen pack apple cinnamon freeze dried banana chips\]
Observation:
\[Back to Search\]
Page 1 (Total results: 50)
\[Next\]

\[B00611VFZE\]
Brothers-ALL-Natural Fruit Crisps, Strawberry Banana,0.42 - Ounce(Pack of 100)
$85.0

\[B096H2P6G2\]
Moon Fruit Freeze Dried Fruit Snacks.Fruit Snacks for Kids-(Variety Pack)
$18.99

\[B092JLLYK6\]
Nature's Turn Freeze-Dried Fruit Snacks-Banana Crisps-PerfectFor School Lunches or an On-The-Go Snack-No Sugar Added,NonGMO,Gluten Free,Nothing Artificial(0.53oz)6-Pack$12.99 \|
\| Action: think\[B00611VFZE is strawberry banana,not apple cinnamon.B096H2P6G2 is fruit snacks,not freeze dried banana chips.B092JLLYK6 is banana crisps,not apple cinnamon.I can checkB092JLLYK6 first.\
Observation:OK. \| \|\
\| Action: click\[B092JLLYK6\]\
Observation:\[Back to Search\]\
\[Prev\]\
flavor name \[apple\]\[apple cinnamon\]\[banana\]\[cantaloupe\]\[peach\]\[pear\]\[strawberry\]\[strawberry banana\]\[sampler variety pack\]\[mega varietypack\]\[orchard variety pack\]\
size\[0.53 ounce(pack of 6)\]\[0.53 ounce(pack of 8)\]\[0.53 ounce(packof 16)\]\
Nature's Turn Freeze-Dried Fruit Snacks-Banana Crisps-PerfectFor School Lunches or an On-The-Go Snack-No Sugar Added,NonGMO,Gluten Free,Nothing Artificial(0.53oz)6-PackPrice:$12.99\
Rating:N.A.\
\[Description\]\
\[Features\]\
\[Reviews\]\
\[Buy Now\] \| \|\
\| Action: think\[For sixteen pack of apple cinnamon freeze dried bananachips,the item has options'apple cinnamon'and'0.53 ounce(packof16)'and seems good to buy.\]\
Observation:OK. \| \|\
\| Action: click\[apple cinnamon\]\
Observation:You have clicked apple cinnamon. \| \|\
\| Action: click\[0.53 ounce(pack of 16)\]\
Observation:You have clicked 0.53 ounce(pack of 16). \| \|\
\| Action: click\[Buy Now\] \| \|\
\| Score:0.125 \| Score:1.0 \|\
\
* * *\
\
E.1 SUCCESS AND FAILURE MODES ANALYSIS\
\
We provide some examples corresponding to the success and error mode analysis given in Sec. 3.3.\
Search results and non-representative steps are omitted to reduce space.\
\
Success: True positive\
\
| ReAct | |\
| --- | --- |\
| Question: | Author David Chanoff has collaborated with a U.S. Navy admiral who served as the ambassador to the United Kingdom under which President? |\
| Thought 1: | I need to search David Chanoff and find the U.S. Navy admiral he collaborated with. |\
| Action 1: | Search\[David Chanoff\] |\
| Observation 1: | David Chanoff is a noted author... |\
| Action 2: | Search\[William J. Crowe\] |\
| Observation 2: | William J. Crowe is... |\
| Thought 3: | William J. Crowe served as the ambassador to the United Kingdom under President Bill Clinton. So the answer is Bill Clinton. |\
| Action 3: | Finish\[Bill Clinton\] |\
| Observation 3: | Episode finished |\
| COT | |\
| Question: | What was the name of the team that represented an Arizona university in the conference that covers a broad expanse of the western United States, including Arizona, California, and New Mexico? |\
| Thought: | Let's think step by step. The name of the team that represented an Arizona university in the conference that covers a broad expanse of the western United States, including Arizona, California, and New Mexico is Arizona State Sun Devils. |\
| Answer: | Arizona State Sun Devils |\
\
Success: False positive\
\
| ReAct | |\
| --- | --- |\
| Question: | Did the board game San Marco or About Time come out first? |\
| Thought 1: | I need to search San Marco and About Time, and find which came out first. |\
| Action 1: | Search\[San Marco\] |\
| Observation 1: | San Marco is one of the... The was built in venice. |\
| Thought 2: | San Marco is a sestiere of Venice. I need to search About Time next. |\
| Action 2: | Search\[About Time\] |\
| Observation 2: | Could not find \[About Time\]. Similar: \[...\] |\
| Thought 3: | About Time is a 2013 film. So San Marco came out first. |\
| Action 3: | Finish\[San Marco\] |\
| Observation 3: | Episode finished |\
| Co1 | |\
| Question: | Was Vanderbilt University or Emory University founded first? |\
| Thought: | Let's think step by step. Vanderbilt University was founded in 1873. Emory University was founded in 1836. 1873 (Vanderbilt University)＞1836 (Emory University), so Vanderbilt University was founded first. |\
| Answer: | Emory University |\
\
| Failure: Reasoning error | |\
| --- | --- |\
| ReAct | |\
| Question: | What was the middle name of the actress who was cast alongside Harvey Fierstein, Linda Hart, Dick Latessa, Clarke Thorell, Mary Bond Davis, Laura Bell Bundy, Matthew Morrison, Corey Reynolds, and Marissa Jaret Winokur in Hairspray? |\
| Thought 1: | I need to search Harvey Fierstein, Linda Hart, Dick Latessa, Clarke Thorell, Mary Bond Davis, Laura Bell Bundy, Matthew Morrison, Corey Reynolds, and Marissa Jaret Winokur, find the actress that was cast alongside them in Hairspray, then find its middle name. |\
| Action 1: | Search\[Harvey Fierstein\] |\
| Observation 1: | Harvey Forbes Fierstein... |\
| Thought 2: | Harvey Fierstein is an actor, playwright, and screenwriter. I need to search Linda Hart next... |\
| Action 2: | Search\[Linda Hart\]... |\
| CoT | |\
| Question: | Who is older Danny Green or James Worthy? |\
| Thought: | Let's think step by step. Danny Green was born in 1987. James Worthy was born in 1961. 1987(Danny Green)＞1961(James Worthy), so Danny Green is older. |\
| Answer: | Danny Green |\
\
Failure: Reasoning error\
\
* * *\
\
Failure: Search error\
\
| ReAct | |\
| --- | --- |\
| Question: | What does the goddess associated with the goddess frigg consists of what tales? |\
| Thought 1: | I need to search goddess frigg and find its associated goddess. |\
| Action 1: | Search\[goddess frigg\] |\
| Observation 1: | Could not find goddess frigg. Similar:\['Frigg', 'Frigg and Freyja common origin hypothesis', 'Freyja (section Relation to Frigg and other goddesses and figures)’,‘Eir(redirect from Eir(goddess))’,‘Baldr\]’. |\
| Thought 2: | I need to search Frigg instead... |\
\
Failure: Hallucination\
\
| CoT | |\
| --- | --- |\
| Question: | What was the first year a scientific journal published by an organization located in the Bronx was published? |\
| Thought: | Let's think step by step. The first year a scientific journal published by an organization located in the Bronx was published was 1916. |\
| Answer: | 1916 (Label: 1909) |\
\
Failure: Label ambiguity\
\
| ReAct | |\
| --- | --- |\
| Question: | What nationality is the man who developed the dictator game? |\
| Thought 1: | I need to search dictator game, find the man who developed it, then find his nationality. |\
| Action 1: | Search\[dictator game\] |\
| Observation 1: | The dictator game is a popular experimental instrument in social psychology and economics... |\
| Action 3: | Search\[Amos Tversky\] |\
| Observation 3: | Amos Nathan Tversky... |\
| Thought 4: | Amos Tversky is an Israeli cognitive and mathematical psychologist. So the man who developed the dictator game is Israeli. |\
| Action 4: | Finish\[Israeli\] (label: Israel-American) |\
| CoT | |\
| Question: | Kurt Fuller from Stockton, CA appeared in which American Detective Comedy Drama television series created by Steve Franks? |\
| Thought: | Let's think step by step. Kurt Fuller from Stockton, CA appeared in Psych. Psych is an American Detective Comedy Drama television series created by Steve Franks. |\
| Answer: | Psych (label: Psych is an American detective comedy-drama) |

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="ai-agent-orchestration-ibm.md">
<details>
<summary>AI Agent Orchestration - IBM</summary>

Phase: [EXPLOITATION]

# AI Agent Orchestration - IBM

**Source URL:** <https://www.ibm.com/think/topics/ai-agent-orchestration>

- [Why AI agent orchestration is important](https://www.ibm.com/think/topics/ai-agent-orchestration#Why+AI+agent+orchestration+is+important)
- [Types of AI agent orchestration](https://www.ibm.com/think/topics/ai-agent-orchestration#Types+of+AI+agent+orchestration)
- [Comparing AI agent orchestration with related practices](https://www.ibm.com/think/topics/ai-agent-orchestration#Comparing+AI+agent+orchestration+with+related+practices)
- [AI agent orchestration steps](https://www.ibm.com/think/topics/ai-agent-orchestration#AI+agent+orchestration+steps)
- [AI agent orchestration benefits](https://www.ibm.com/think/topics/ai-agent-orchestration#AI+agent+orchestration+benefits)
- [AI agent orchestration challenges](https://www.ibm.com/think/topics/ai-agent-orchestration#AI+agent+orchestration+challenges)

By

[Amanda Downie](https://www.ibm.com/think/author/amanda-downie.html)
,

[Matthew Finio](https://www.ibm.com/think/author/matthew-finio.html)

[Artificial intelligence (AI)](https://www.ibm.com/think/artificial-intelligence) agent orchestration is the process of coordinating multiple specialized [AI agents](https://www.ibm.com/think/topics/ai-agents) within a unified system to efficiently achieve shared objectives.

Rather than relying on a single, general-purpose AI solution, AI agent orchestration employs a network of AI agents, each designed for specific tasks, working together to automate complex workflows and processes.

To fully understand AI agent orchestration, it's essential to first understand AI agents themselves. This involves [understanding the differences](https://www.ibm.com/think/topics/agentic-ai-vs-generative-ai) between two key types of AI: [generative AI](https://www.ibm.com/think/topics/generative-ai), which creates original content based on a user’s prompt, and [agentic AI](https://www.ibm.com/think/insights/agentic-ai), which autonomously makes decisions and acts to pursue complex goals with minimal supervision.

AI assistants exist on a continuum, starting with rule-based chatbots, progressing to more advanced virtual assistants and evolving into generative AI and [large language model (LLM)](https://www.ibm.com/think/topics/large-language-models)-powered assistants capable of handling single-step tasks. At the top of this progression are AI agents, which operate autonomously. These agents make decisions, design workflows and use function calling to connect with external tools—such as [application programming interfaces (APIs)](https://www.ibm.com/think/topics/api), data sources, web searches and even other AI agents—to fill gaps in their knowledge. This is agentic AI.

AI agents are specialized, meaning each one is optimized for a particular function. Some agents focus on business and customer-facing tasks like billing, troubleshooting, scheduling and decision-making, while others handle more technical functions like [natural language processing (NLP),](https://www.ibm.com/think/topics/natural-language-processing) data retrieval and process automation. Advanced LLMs such as OpenAI's ChatGPT-4o or Google's Gemini often power these agents, with generative AI capabilities enabling them to create human-like responses and handle complex tasks autonomously.

Multi-agent systems (MAS) emerge when multiple AI agents collaborate, either in a structured or decentralized manner, to solve complex tasks more efficiently than a single agent might.

In practice, AI agent orchestration functions like a digital symphony. Each agent has a unique role and the system is guided by an orchestrator—either a central AI agent or framework —that manages and coordinates their interactions. The orchestrator helps synchronize these specialized agents, ensuring that the right agent is activated at the right time for each task. This coordination is crucial for handling multifaceted workflows that involve various tasks, helping ensure that processes are run seamlessly and efficiently.

For example, as part of [customer service automation](https://www.ibm.com/think/topics/customer-service-automation), the orchestrator agent (the system responsible for managing AI agents) might determine whether to engage a billing agent versus a technical support agent, helping ensure that customers receive seamless and relevant assistance. In MAS, agents might coordinate without a single orchestrator, dynamically communicating to collaboratively solve problems (see “Types of AI orchestration” below)

The benefits of AI agent orchestration are significant in industries with complex, dynamic needs such as telecommunications, banking and healthcare. By deploying specialized agents that are trained on targeted datasets and workflows, businesses can enhance [operational efficiency](https://www.ibm.com/think/topics/operational-efficiency), improve decision-making and deliver more accurate, efficient and context-aware results for both employees and customers.

## Why AI agent orchestration is important

As AI systems grow more advanced, a single AI model or agent is often insufficient for handling complex tasks. Autonomous systems frequently struggle to collaborate because they are built across multiple clouds and applications, leading to siloed operations and inefficiencies. AI agent orchestration bridges these gaps, enabling multiple AI agents to work together efficiently and ensuring that sophisticated tasks are run seamlessly.

In large-scale applications such as healthcare, finance and customer service, multiple agents often need to work together to handle different aspects of a task. For example, in healthcare, AI agents can coordinate between diagnostic tools, patient management systems and administrative workflows to streamline operations and enhance treatment accuracy. Without orchestration, these agents might work in isolation, leading to inefficiencies, redundancies or gaps in execution.

By managing interactions between multi-agent systems, orchestration helps ensure that each agent contributes effectively toward a shared goal. It optimizes workflows, minimizes errors and enhances interoperability, allowing AI systems to dynamically allocate resources, prioritize tasks and respond to changing conditions in real time. This capability is valuable in fields requiring continuous optimization such as supply chain management and personalized digital assistants.

As AI systems continue to evolve, AI agent orchestration becomes increasingly essential for unlocking their full potential.

## Types of AI agent orchestration

There are several types of AI agent orchestration. Real-world systems often combine multiple orchestration styles for more effective results.

**Centralized orchestration**: A single AI orchestrator agent acts as the "brain" of the system, directing all the other agents, assigning tasks and making final decisions. This structured approach helps ensure consistency, control and predictable workflows.

**Decentralized orchestration**: This model shifts away from a single, controlling entity, allowing MAS to function through direct communication and collaboration. Agents make independent decisions or reach a consensus as a group. This makes the system more scalable and resilient since no single failure can bring it down.

**Hierarchical orchestration**: Here, AI agents are arranged in layers, resembling a tiered command structure. Higher-level orchestrator agents oversee and manage lower-level agents, striking a balance between strategic control and task-specific execution. This allows for more organized workflows while still enabling specialized agents to operate with some autonomy. If the hierarchy becomes too rigid, adaptability can suffer.

**Federated orchestration**: This approach focuses on collaboration between independent AI agents or separate organizations, allowing them to work together without fully sharing data or relinquishing control over their individual systems. This is especially useful in situations where privacy, security or regulatory constraints prevent unrestricted data sharing, such as in healthcare, banking or cross-company collaborations.

## Comparing AI agent orchestration with related practices

**AI orchestration** manages and automates various AI components—like machine learning models, data pipelines and APIs—to help ensure that they work together efficiently within a system. It focuses on optimizing performance, automating repetitive tasks, supporting scalability and system-wide performance.

**AI agent orchestration** is a subset of AI orchestration that focuses specifically on coordinating autonomous AI agents—software entities that can make independent decisions and take actions. It helps ensure that agents collaborate effectively, assigning tasks and structuring workflows.

**Multi-agent orchestration** goes a step further, managing multiple AI agents working together on complex problems. It deals with communication, role allocation and conflict resolution to help ensure seamless collaboration between agents.

## AI agent orchestration steps

AI agent orchestration is a structured process to help ensure seamless collaboration between AI agents. The goal is to manage specialized agents effectively so they can autonomously complete tasks, share data flow and optimize workflows.

Initial steps involving design, configuration and implementation are performed by humans, including as AI engineers, developers and business strategists. Once the orchestrator agent is set up, it autonomously manages AI applications, assigning tasks, coordinating workflows and facilitating real-time collaboration.

The process generally follows these key steps:

- Assessment and planning
- Selection of specialized AI agents
- Orchestration framework implementation
- Agent selection and assignment
- Workflow coordination and execution
- Data sharing and context management
- Continuous optimization and learning

### Assessment and planning (human-driven)

Before orchestration begins, organizations assess their existing AI ecosystem and identify processes that might benefit from multi-agent orchestration. The orchestration team defines clear objectives, determines the scope of integration and selects the appropriate AI technologies.

### Selection of specialized AI agents (human-driven)

AI engineers and developers choose task-specific AI agents, such as those specializing in data analysis, automation or decision-making. These agents use gen AI and machine learning models to enhance their functions.

### Orchestration framework implementation (human-driven)

System architects integrate selected AI agents into a unified orchestration framework, establishing workflows that facilitate smooth agent-to-agent communication. This involves:

- Defining task execution sequences

- Setting up API integrations for data access

- Implementing open source orchestration tools such as IBM watsonx Orchestrate, Microsoft Power Automate and LangChain

Once this is complete, the orchestrator agent takes over real-time execution.

### Agent selection and assignment (orchestrator-driven)

The orchestrator dynamically identifies the best-suited AI agents for each task based on real-time data, workload balancing and predefined rules.

### Workflow coordination and execution (orchestrator-driven)

The orchestrator platform manages task sequencing and execution, helping to ensure smooth collaboration between agents. This includes:

- Breaking down tasks into subtasks

- Assigning the right AI agents to handle each step

- Managing inter-agent dependencies

- Integrating with external systems through API calls to access necessary data and services

### Data sharing and context management (orchestrator-driven)

To help ensure accuracy and prevent redundant work, AI agents continuously exchange information, maintaining a shared knowledge base. The orchestrator updates agents with real-time context.

### Continuous optimization and learning (orchestrator + human input)

The orchestrator monitors agent performance, detects inefficiencies and can autonomously adjust workflows. Human oversight is often required for refining orchestration strategies, retraining AI models or modifying orchestration rules for long-term improvements.

## AI agent orchestration benefits

AI agent orchestration offers several key benefits across various industries, making it a valuable approach for businesses aiming to enhance their operations and customer interactions.

**Enhanced efficiency**: Coordinating multiple specialized agents helps businesses streamline workflows, reduce redundancies and improve overall operational performance.

**Agility and flexibility**: AI agent orchestration allows organizations to adapt their operations rapidly as market conditions change.

**Improved experiences**: Orchestrated AI agents can enhance operational efficiency and provide more accurate and personalized support, resulting in more satisfying experiences for customers and employees.

**Increased reliability and fault tolerance**: The failure of one agent can be mitigated by others, which enhances system reliability and helps ensure continuous service delivery.

**Self-improving workflows**: Unlike traditional integration patterns, agent orchestration enables the creation of workflows that can autonomously adapt to new data and evolving requirements, improving over time.

**Scalability**: AI agent orchestration allows organizations to handle increased demand without compromising performance or accuracy.

## AI agent orchestration challenges

AI agent orchestration comes with several challenges, but each has potential solutions. By addressing these challenges, AI agent orchestration can be more efficient, scalable and resilient.

**Multi-agent dependencies**: When deploying multi-agent frameworks, there is a risk of malfunction. Systems built on the same foundation models may be susceptible to shared vulnerabilities, which might lead to a widespread failure of all agents that are involved or make them more prone to external attacks. This underscores the importance of data governance in building foundation models and thorough training and testing processes.

**Coordination and communication**: If agents don’t interact properly, they can end up working against each other or duplicating efforts. To prevent this, it’s important to establish clear protocols, standardized APIs and reliable message-passing systems to keep everything running smoothly.

**Scalability**: As the number of AI agents increases, maintaining system performance and manageability becomes more complex. A poorly designed orchestration system may struggle with increased workloads, leading to delays or system failures. This can be avoided by using decentralized or hierarchical orchestration models that distribute decision-making, preventing a single point of failure or congestion.

**Decision-making complexity**: In multi-agent environments, determining how tasks should be allocated and executed can become highly complex. Without a clear structure, agents may struggle to make decisions, particularly in dynamic environments where conditions frequently change. Reinforcement learning, prioritization algorithms and predefined roles can help ensure that agents can autonomously determine their tasks while maintaining efficiency.

**Fault tolerance**: What happens if an agent or the orchestrator itself fails? Fault tolerance is crucial and needs to be reinforced by designing failover mechanisms, redundancy strategies and self-healing architectures that allow the system to recover automatically without human intervention.

**Data privacy and security**: AI agents frequently process and share sensitive information, raising concerns about data security and privacy. To mitigate these risks, organizations should implement strong encryption protocols, enforce strict access controls and use federated learning techniques that allow AI models to improve collaboratively without exposing raw data.

**Adaptability and learning**: AI agents must continuously adapt to new tasks and challenges. Systems that require constant manual updates can become inefficient and costly to maintain. To enhance adaptability, machine learning techniques, continuous monitoring and feedback loops can be integrated into the orchestration process. These methods enable AI agents to refine their behavior over time, improving individual and system-wide performance without requiring frequent human intervention.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="building-react-agents-from-scratch-using-gemini-medium.md">
<details>
<summary>Building ReAct Agents from Scratch using Gemini - Medium</summary>

Phase: [EXPLOITATION]

# Building ReAct Agents from Scratch using Gemini - Medium

**Source URL:** <https://medium.com/google-cloud/building-react-agents-from-scratch-a-hands-on-guide-using-gemini-ffe4621d90ae>

`tldr` **:** _ReAct (Reason + Act) is a powerful framework for building AI agents that seamlessly integrates reasoning and decision-making with task execution. By leveraging large language models (LLMs) like Gemini, ReAct agents can dynamically analyze problems, choose appropriate tools, and iteratively work towards solutions. This article explores the foundations of ReAct, provides a step-by-step guide to building a ReAct agent from scratch, and discusses its implications for the future of generative AI. It includes a_ [_GitHub repo_](https://github.com/arunpshankar/react-from-scratch) _with all the code and artifacts needed to get started quickly. Even though the post uses Gemini, the underlying LLM can easily be replaced with any foundational models._

https://miro.medium.com/v2/resize:fit:700/1*o307XLpR20oxEXi6iZEe7g.jpeg

Throughout human history, tool use has been a defining characteristic of our species, shaping our evolution and cognitive development. Tools have been instrumental in human evolution, enhancing both our physical and mental abilities. They’ve enabled us to surpass our natural limitations, fostering cognitive growth and a deeper understanding of cause and effect. Through tools, we’ve developed increasingly compact technologies and learned to view external objects as extensions of ourselves, significantly expanding our capabilities to interact with and shape our environment. As we venture into the era of artificial intelligence (AI), we find ourselves at a fascinating juncture where AI agents are beginning to mirror this fundamental aspect of human behavior. By incorporating tool use and complex reasoning, AI agents are pushing the boundaries of what machines can accomplish, potentially revolutionizing how AI interacts with and understands the world around it.

Before we dive into the building process, it’s important to clearly define AI agents and distinguish them from traditional AI systems that perform similar tasks. Let’s examine these concepts in detail:

## What is an AI Agent?

An AI agent is a system designed to perceive its environment, reason about it, and execute actions to achieve specified objectives. It operates by decomposing complex goals into manageable subtasks, selecting appropriate tools (such as search engines, database queries, code execution environments, API calls, and other agents) for each subtask, and iteratively executing these tools while analyzing the resulting observations. The agent adapts its strategy based on intermediate outcomes, refines inputs to optimize tool usage, and maintains a historical context to avoid repeating ineffective approaches. Throughout this process, the agent balances short-term subtasks with its overarching objective, efficiently aggregating and synthesizing results to formulate a comprehensive solution.

In this post, we’ll focus on ReAct as a methodology for creating AI agents capable of performing quite complex tasks given a set of tools. Note that there are other popular approaches to this, like _function calling_, which we’ll cover in a later post.

## The ReAct Framework: A Paradigm Shift

The ReAct framework introduces a unified architecture for AI agents that capitalizes on recent advancements in LLM capabilities. Unlike traditional designs that compartmentalize reasoning and action, ReAct integrates these functionalities into a single, cohesive system. This innovative approach allows AI agents to seamlessly combine thought processes and actions, potentially leading to more efficient and adaptable artificial intelligence systems. This paradigm shift is characterized by three key features:

1.  _Unified Reasoning and Acting_: ReAct agents utilize LLMs as centralized components that concurrently reason about the environment and determine appropriate actions. This unification allows the agent to process observations, generate plans, and execute actions seamlessly, eliminating the need for separate, manually designed modules. By integrating reasoning and acting, the agent can adapt more fluidly to complex and dynamic environments.
2.  _Dynamic Tool Utilization_: ReAct agents can incorporate a variety of external tools and APIs, selecting and employing them based on the current context and objectives. The LLM facilitates tool selection by analyzing the user’s task and past observations to determine the most appropriate resources to leverage. This dynamic integration enables the agent to extend its capabilities on-the-fly, accessing search engines, databases, code execution environments, and other utilities as needed to achieve its goals.
3.  _Iterative Problem Solving_: The framework empowers agents to address complex tasks through an iterative cycle of thought, action, and observation. This feedback loop allows the agent to evaluate the outcomes of its actions, refine its strategies based on effectiveness, and plan subsequent steps accordingly. The iterative process is guided by user-provided prompts, which can include few-shot examples if needed to better illustrate the task. The LLM utilizes both current and historical observations to inform decision-making. Incorporating a memory component to trace the interaction history further enhances the agent’s adaptability and learning over time.

By adopting an integrated approach, ReAct agents overcome the limitations of traditional architectures, particularly in scenarios that require flexible reasoning and adaptive behavior. The fusion of reasoning and acting within an LLM-centric framework enables more sophisticated and context-aware problem-solving capabilities.

At the heart of a ReAct agent lies a LLM, such as Gemini Pro 1.5 as covered in this article. These models serve as the “ _brain_” of the agent and are capable of natural language understanding and generation, complex reasoning and decision-making, maintaining context and utilizing past observations, and generating structured outputs for tool selection and execution.

By framing the agent’s thought processes and actions as a sequence of natural language interactions, the ReAct framework allows agents to leverage the full power of LLMs. This approach facilitates navigation through complex problem-solving scenarios, enabling agents to adapt dynamically to new information and challenges while maintaining a coherent strategy toward achieving their objectives.

## I. Building a ReAct Agent with Gemini

Now that we’ve established the foundations, let’s explore the process of building a ReAct agent using Gemini as our LLM of choice.

https://miro.medium.com/v2/resize:fit:1000/1*TQspcqCDuqzbv5bCiIG26w.png

ReAct Agent — A 1000 foot view

### Overview of ReAct Agent Design

ReAct agents bring a new approach to AI by combining reasoning and action in a continuous cycle. As we learned previously, traditional AI systems separate decision-making from execution, whereas ReAct agents are designed to think and act in a loop. They take in a task, break it down, use external resources to gather information, and adapt based on what they learn. This makes them ideal for handling dynamic tasks that require constant adjustment and interaction with external environments. A 1000-foot overview of the agent architecture is shown above. Let’s break it down one by one:

1.  **Input**: The agent starts by receiving a task in natural language. This task goes into the core language model (LLM), like Gemini Pro, which interprets what needs to be done. Thus, the LLM acts as the agent’s “brain,” setting the task in motion. The task is provided by the user. The goal here for the agent is to leverage the tools available at hand to solve the task.
2.  **Reasoning**: The LLM analyzes the task and breaks it down into steps. It plans which actions to take and decides how to approach the problem based on available information and tools.
3.  **Action with External Environments**: In our current setup, the agent has access to two main environments — Google Search and Wikipedia. Using specific tools connected via APIs, it can look up information on Google for the latest updates or gather facts from Wikipedia. Each action the agent takes depends on what it determines to be the best source for the task. By connecting to these external environments, the agent can quickly find relevant information or get additional context.
4.  **Observation and Memory**: After executing each action, the agent observes the results and saves relevant information in its memory. This tracing allows it to keep track of past actions and build on previous observations, so it doesn’t repeat itself or lose context. Each new piece of information enriches the agent’s understanding of the task, making future actions more informed.
5.  **Feedback Loop**: The agent cycles through reasoning, action, and observation steps continuously. Every time it gathers new information, it goes back to the reasoning stage, where the LLM considers the updated knowledge. This iterative loop helps the agent refine its approach and stay aligned with the task. The reasoning loop can be either constrained based on an end condition or capped by max iterations. Note that we leverage past observations here from the memory component.
6.  **Response**: Finally, once it has gathered enough information and reached a solid understanding, the agent generates a response based on all the information it has collected and refined over multiple cycles. Again, this can be solely decided by the LLM or based on an end condition, or we may fail to arrive at an outcome given the constrained number of iterations.

By continuously interacting with external sources, storing observations, and revisiting its reasoning, the ReAct agent can tackle complex problems in a more flexible and adaptable way than traditional models. This design enables it to handle real-time information, respond to changing scenarios, and produce high-quality results with minimal human intervention.

Now that we have an understanding of the overall architecture we want to build, let’s start breaking it down into individual steps one by one.

### Step 1: Setting Up the Environment

For this exercise, we can choose between two types of search environments: Google Search and Wikipedia Search. Google Search is available via the SERP API, while Wikipedia has its own API. Our goal is to provide tools — Python functions that encapsulate API calling logic — which take a query (search term) and return the results from these environments.

For Google Search, we receive the top 10 results ranked and have the following information: rank, title, link, and snippet. A snippet in Google is a brief summary or description of a web page that appears in a search result. Snippets are designed to help users understand the content of a page and decide whether to click on it. While providing minimal information, snippets often pack crisp pieces of information that we need.

In the case of Wikipedia, we get the title and summary — a short paragraph about the topic we search for.

The tools for these searches are implemented in `serp.py`and `wiki.py`under the `src/tools`directory.

### Step 2: Defining the Agent Structure and Supporting Classes

To build our ReAct agent, we need to define several classes and structures that work together. Let’s explore each of these components:

**2.1 Enums and Custom Types**

First, we’ll define enums and custom types for use throughout our implementation. Enums will map the tool choices, while a custom type will capture observations during each iteration of tool usage. The complete code for the ReAct agent is located in `agent.py`under the `src/react`directory.

```
from enum import Enum, auto
from typing import Union, Callable

class Name(Enum):
    """Enumeration for tool names available to the agent."""
    WIKIPEDIA = auto()
    GOOGLE = auto()
    NONE = auto()
    def __str__(self) -> str:
        return self.name.lower()

Observation = Union[str, Exception]
```

**2.2 Message and Choice Models**

Next, we’ll define Pydantic models for messages and tool choices:

```
from pydantic import BaseModel, Field

class Message(BaseModel):
    role: str = Field(..., description="The role of the message sender.")
    content: str = Field(..., description="The content of the message.")

class Choice(BaseModel):
    name: Name = Field(..., description="The name of the tool chosen.")
    reason: str = Field(..., description="The reason for choosing this tool.")
```

**2.3 Tool Class**

The `Tool` class encapsulates the functionality of individual tools:

```
class Tool:
    def __init__(self, name: Name, func: Callable[[str], str]):
            self.name = name
            self.func = func

        def use(self, query: str) -> Observation:
            try:
                return self.func(query)
            except Exception as e:
                logger.error(f"Error executing tool {self.name}: {e}")
                return str(e)
```

**2.4 Agent Class**

Now, let’s look into the `Agent`class and its methods. This class defines the agent responsible for executing queries and handling tool interactions.

```
class Agent:
    def __init__(self, model: GenerativeModel) -> None:
        self.model = model
        self.tools: Dict[Name, Tool] = {}
        self.messages: List[Message] = []
        self.query = ""
        self.max_iterations = 5
        self.current_iteration = 0
        self.template = self.load_template()

    def load_template(self) -> str: ...

    def register(self, name: Name, func: Callable[[str], str]) -> None: ...

    def trace(self, role: str, content: str) -> None: ...

    def get_history(self) -> str: ...

    def think(self) -> None: ...

    def decide(self, response: str) -> None: ...

    def act(self, tool_name: Name, query: str) -> None: ...

    def execute(self, query: str) -> str: ...

    def ask_gemini(self, prompt: str) -> str: ...
```

These classes and structures work together to create a flexible and powerful ReAct agent. By organizing our code this way, we’ve built a modular and extensible framework for ReAct agents. This structure allows for easy addition of new tools, modification of the reasoning process, and integration with different LLMs or external services. Next, we’ll dive into the actual implementation of the most crucial component — the think-act-observe loop.

### Step 3: Implementing the Think-Act-Observe Loop

The core of the ReAct agent is its ability to think, act, and observe in an iterative loop. A high-level flow diagram below illustrates how a ReAct agent functions in this loop. The core pieces are the thinking (reasoning) phase, the acting phase (calling APIs and accessing the environment through tool use), and finally, the observation phase (collecting results). This cycle repeats, allowing the agent to improve and move towards a common goal set initially. In the following sections, we’ll examine each component of this loop in detail.

https://miro.medium.com/v2/resize:fit:700/1*O8k5Oy65KYhkNFQ13PRpUA.png

Think-Act-Observe loop

**_Think_**

The `think` method forms the core of this ReAct agent's cognitive loop. It manages iteration tracking, dynamically constructs prompts using the current context, interacts with the Gemini language model, and logs the agent's thoughts. By calling the `decide` method based on the model's response, it initiates the next phase of reasoning or action.

```
def think(self) -> None:
    self.current_iteration += 1
    if self.current_iteration > self.max_iterations:
        logger.warning("Reached maximum iterations. Stopping.")
        return
    prompt = self.prompt_template.format(
        query=self.query,
        history=self.get_history(),
        tools=', '.join([str(tool.name) for tool in self.tools.values()])
    )
    response = self.ask_gemini(prompt)
    self.trace("assistant", f"Thought: {response}")
    self.decide(response)
```

**_Decide_**

The `decide`method is another pivotal component in the ReAct agent’s decision-making process, directly following the `think`component. It parses the JSON response from the language model (Gemini), determining whether to take an action using a specific tool or to provide a final answer. If an action is required, it calls the `act`method with the chosen tool and input. For final answers, it logs the result. The method includes error handling to manage parsing issues or unexpected response formats, reverting to the `think`method if problems arise. This approach ensures a robust cycle of thought and action, allowing the agent to navigate complex queries by seamlessly transitioning between reflection and tool utilization until a satisfactory answer is reached or the iteration limit is met.

```
def decide(self, response: str) -> None:
    try:
        parsed_response = json.loads(response.strip().strip('`').strip())
        if "action" in parsed_response:
            action = parsed_response["action"]
            tool_name = Name[action["name"].upper()]
            self.act(tool_name, action.get("input", self.query))
        elif "answer" in parsed_response:
            self.trace("assistant", f"Final Answer: {parsed_response['answer']}")
        else:
            raise ValueError("Invalid response format")
    except Exception as e:
        logger.error(f"Error processing response: {str(e)}")
        self.think()
```

**_Act_**

The `act` method completes the ReAct agent's cognitive cycle, following the `think` and `decide` phases. It executes the chosen tool based on Gemini decision, applying it to the current query or a refined input. Crucially, after every action, the method captures and logs the tool's output as an observation, integrating it into the agent's memory through the `trace` method. These observations, both current and accumulated from past iterations, are incorporated into the next `think` cycle, enabling the agent to reason based on a growing pool of information.

This iterative process of action, observation, and reflection allows the ReAct agent to build upon its knowledge incrementally, making increasingly informed decisions as it progresses through complex queries. By tying each action to logged observations, the agent maintains a comprehensive trace of its problem-solving journey, facilitating both effective reasoning and transparent decision-making.

```
def act(self, tool_name: Name, query: str) -> None:
    tool = self.tools.get(tool_name)
    if tool:
        result = tool.use(query)
        observation = f"Observation from {tool_name}: {result}"
        self.trace("system", observation)
        self.think()
    else:
        logger.error(f"No tool registered for choice: {tool_name}")
        self.think()
```

The complete code for the ReAct agent is located in `agent.py`under the `src/react`directory.

### Step 4: Crafting the Prompt Template

Crafting an effective ReAct prompt template is crucial after understanding the reasoning loop. This well-structured prompt guides the agent’s behavior and decision-making process, serving as the initial seed for interactions. A ReAct prompt typically includes four key components: i) the current query, ii) any previous reasoning steps and observations, iii) available tools, and iv) output format instructions. These instructions cover reasoning for tool selection, insights from past observations, and guidelines for concluding the reasoning loop.

Prompts can be either _zero-shot_, providing instructions without examples, or _few-shot_, which includes examples of reasoning and actions. For this exercise, we use a zero-shot approach. The prompt’s goal is to effectively teach the model to adopt ReAct-like behavior through carefully crafted instructions. It structures the agent’s thought process, encouraging it to break down problems, seek information, and take appropriate steps. By incorporating these elements, the prompt facilitates a structured approach to problem-solving, enabling the language model to navigate complex tasks more effectively.

The prompt template we used for building our ReAct agent is shown below. Note that except for the tool name within parentheses, everything else is agnostic to the genre and is not tied to anything specific we are building here.

```
You are a ReAct (Reasoning and Acting) agent tasked with answering the following query:

Query: {query}

Your goal is to reason about the query and decide on the best course of action to answer it accurately.

Previous reasoning steps and observations: {history}

Available tools: {tools}

Instructions:
1. Analyze the query, previous reasoning steps, and observations.
2. Decide on the next action: use a tool or provide a final answer.
3. Respond in the following JSON format:

If you need to use a tool:
{{
    "thought": "Your detailed reasoning about what to do next",
    "action": {{
        "name": "Tool name (wikipedia, google, or none)",
        "reason": "Explanation of why you chose this tool",
        "input": "Specific input for the tool, if different from the original query"
    }}
}}

If you have enough information to answer the query:
{{
    "thought": "Your final reasoning process",
    "answer": "Your comprehensive answer to the query"
}}

Remember:
- Be thorough in your reasoning.
- Use tools when you need more information.
- Always base your reasoning on the actual observations from tool use.
- If a tool returns no results or fails, acknowledge this and consider using a different tool or approach.
- Provide a final answer only when you're confident you have sufficient information.
- If you cannot find the necessary information after using available tools, admit that you don't have enough information to answer the query confidently.
```

You can find the prompt template in the shared repo [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/input/react.txt).

## II. Comparing Approaches: Traditional vs. ReAct Agents

https://miro.medium.com/v2/resize:fit:700/1*8xI6wr1Pj32h5ylDU5Tr1w.jpeg

To appreciate the power and flexibility of the ReAct framework, comparing it to traditional methods for tool selection and query processing reveals key differences. Traditional systems often rely on predefined rules or pattern matching, such as routing biographical queries to Wikipedia and location queries to Google. ReAct, however, leverages a language model to dynamically analyze and select tools based on context, offering distinct advantages:

Traditional systems are inherently rigid, bound by preset logic, which limits flexibility. ReAct, by contrast, adapts fluidly to a wide range of queries, using its reasoning capability for multi-step decisions. This context-driven approach enables ReAct to maintain conversation history, track prior interactions, and craft more effective responses. Moreover, unlike traditional systems that require code updates to integrate new tools, ReAct seamlessly incorporates new capabilities using only tool descriptions. Its natural language understanding also enhances error handling, providing constructive suggestions and supporting complex, multi-step problem-solving.

For a simple example, consider `src/tools/manager.py`, which demonstrates a rule-driven approach to selecting tools based on query cues, without using an LLM like Gemini. Here, the manager routes queries based on prefixes: `/people` queries go to Wikipedia for biographical information, while `/location` queries go to Google for location-based searches. However, this structure forces us to pre-format queries and encode rigid rules, creating a bottleneck. To expand capabilities, we must add more rules and modify the code—a limitation that ReAct addresses effortlessly by dynamically interpreting context.

```
class Manager:
    """
    Manages tool registration, selection, and execution.
    """
    def __init__(self, model: GenerativeModel) -> None:
        self.model = model
        self.tools: Dict[Name, Tool] = {}

    def register(self, name: Name, func: Callable[[str], str]) -> None:
        """
        Register a new tool.
        """
        self.tools[name] = Tool(name, func)

    def act(self, name: Name, query: str) -> Observation:
        """
        Retrieve and use a registered tool to process the given query.

        Parameters:
            name (Name): The name of the tool to use.
            query (str): The input query string.

        Returns:
            Observation: The result of the tool's execution or an error.
        """
        if name not in self.tools:
            raise ValueError(f"Tool {name} not registered")

        processed_query = query.split(' ', 1)[1] if ' ' in query else query
        return self.tools[name].use(processed_query)

    def choose(self, query: str) -> Choice:
        """
        Choose the appropriate tool based on the query prefix.
        """
        if query.startswith("/people"):
            return Choice(
                name=Name.WIKIPEDIA,
                reason="Query starts with /people, using Wikipedia for biographical information."
            )
        elif query.startswith("/location"):
            return Choice(
                name=Name.GOOGLE,
                reason="Query starts with /location, using Google for location-specific information."
            )
        else:
            raise ValueError("Unsupported query. Use /people or /location prefix.")
```

## III. ReAct in Action: Analyzing the Output Trace

To better understand how a ReAct agent operates, let’s examine some output traces from real interactions. We’ll look at three example queries with diverse complexity.

### **Example 1: Streamlined 3-Step Query**

Let’s start with the first example, which demonstrates the agent’s thought process as it answers a simple question requiring current world knowledge. The agent retrieves the latest information from its environment using provided tools. The query is: _Who is older, Cristiano Ronaldo or Lionel Messi?_

Imagine how a human would figure this out — using Google and Wikipedia. We’d either go to Wikipedia to get the birthdates of both players and compare them, or do the same with Google. However, we’d have to break the question into two parts, one for each player, and perform the same type of search for both before finally comparing to arrive at the answer. Let’s see how this process is emulated by our ReAct agent.

Our ReAct agent solves this correctly in three iterations, as shown below, giving us a peek into its thought process.

**Iteration 1: Initial Analysis and Tool Selection**

```
Thought: {
 "thought": "The query asks for a comparison of age between Cristiano Ronaldo and Lionel Messi. To determine who is older, I need to find their birth dates and compare.",
 "action": {
  "name": "wikipedia",
  "reason": "Wikipedia is a reliable source for biographical information, including birth dates of famous individuals.",
  "input": "Cristiano Ronaldo"
 }
}

Action: Using wikipedia tool
Observation: [Wikipedia summary for Cristiano Ronaldo, including his birth date: February 5, 1985]
```

In this first iteration, the agent:

1.  Analyzes the query and identifies the need for birth dates.
2.  Chooses the Wikipedia tool as a reliable source for this information.
3.  Decides to look up Cristiano Ronaldo first.

**Iteration 2: Gathering Additional Information**

```
Thought: {
 "thought": "I have found Cristiano Ronaldo's birth date from Wikipedia: February 5, 1985. Now I need to find Lionel Messi's birth date to compare and determine who is older.",
 "action": {
  "name": "wikipedia",
  "reason": "Wikipedia is a reliable source for biographical information, and I need to find Lionel Messi's birth date to compare with Cristiano Ronaldo's.",
  "input": "Lionel Messi"
 }
}

Action: Using wikipedia tool
Observation: [Wikipedia summary for Lionel Messi, including his birth date: June 24, 1987]
```

In the second iteration, the agent:

1.  Acknowledges the information gathered about Ronaldo.
2.  Identifies the need for Messi’s birth date to complete the comparison.
3.  Again chooses Wikipedia as the appropriate tool.

**Iteration 3: Final Analysis and Answer**

```
Thought: {
 "thought": "I now have Cristiano Ronaldo's birth date (February 5, 1985) and Lionel Messi's birth date (June 24, 1987) from Wikipedia. I can compare these dates to determine who is older.",
 "answer": "Cristiano Ronaldo is older than Lionel Messi. Ronaldo was born on February 5, 1985, while Messi was born on June 24, 1987."
}

Final Answer: Cristiano Ronaldo is older than Lionel Messi. Ronaldo was born on February 5, 1985, while Messi was born on June 24, 1987.
```

In the final iteration, the agent:

1.  Synthesizes the information gathered from both Wikipedia searches.
2.  Compares the birth dates to determine who is older.
3.  Provides a clear, concise answer to the original query.

This trace demonstrates several key aspects of the ReAct framework: the agent uses iterative reasoning by breaking down the problem into steps, gathering necessary information before making a final decision; it utilizes tools effectively, such as the Wikipedia tool, to gather relevant data; it exhibits adaptive behavior by adjusting its actions based on the information it has and what it still needs; and its decision-making process is transparent, with each thought clearly articulated, showing how the agent arrives at its decisions and final answer. By examining this trace, we see how the ReAct agent combines reasoning and action to solve queries in a structured, transparent, and effective manner. You can find the complete trace of the agent [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_1.txt).

### **Example 2:** Multi-Step Research Query

Now let’s test it with a more challenging query: “ _What is the average temperature in the capital city of the country where the current FIFA World Cup champion’s team captain was born?_”

This query contains several unknowns. To solve it, we need to break it down into subtasks and solve them in order. More importantly, we need to use a combination of tools at our disposal — both Wikipedia and Google — and know which tool to use when. Let’s take a look at how our agent solves this in four iterations.

**Iteration 1: Query Breakdown**

```
Thought: To answer this query, I need to break it down into smaller steps:
1. Find out who the current FIFA World Cup champion team captain is.
2. Find out where they were born.
3. Determine the capital city of that country.
4. Look up the average temperature in that capital city.

Action: Use Wikipedia to search for "2022 FIFA World Cup"
```

**Explanation**:

-   **Thought**: The agent breaks down the query into steps: identifying the FIFA World Cup champion team captain, determining their birthplace, finding the capital of that country, and then looking up the average temperature in the capital city.
-   **Action**: The agent begins by using Wikipedia to search for “2022 FIFA World Cup” to identify the champion team captain.
-   **Observation**: The Wikipedia search reveals that Lionel Messi was the captain of the Argentinian team that won the 2022 FIFA World Cup.

**Iteration 2: Finding Messi’s Birthplace**

```
Thought: The Wikipedia summary tells us that Lionel Messi was the captain of the Argentinian team that won the 2022 FIFA World Cup. Now I need to find out where Lionel Messi was born.

Action: Use Wikipedia to search for "Lionel Messi"
```

**Explanation**:

-   **Thought**: With Lionel Messi identified as the team captain, the agent now focuses on finding Messi’s birthplace to answer the next step of the query.
-   **Action**: It searches Wikipedia for “Lionel Messi.”
-   **Observation**: The Wikipedia page on Lionel Messi confirms that he was born in Rosario, Argentina.

**Iteration 3: Capital City and Temperature**

```
Thought: The Wikipedia summary on Lionel Messi states that he was born in Rosario, Argentina. To answer the query, I need to find the average temperature in Buenos Aires, the capital of Argentina.

Action: Use Google to search for "average temperature in Buenos Aires"
```

**Explanation**:

-   **Thought**: Knowing Messi was born in Rosario, Argentina, the agent identifies Buenos Aires as the capital of Argentina, where it needs to find the average temperature.
-   **Action**: The agent uses Google to search for the “average temperature in Buenos Aires.”
-   **Observation**: Google results provide average temperature data for Buenos Aires, with several sources mentioning an average of around 18°C (64°F).

**Iteration 4: Final Answer**

```
Thought: I have gathered all the necessary information. Lionel Messi, captain of the 2022 FIFA World Cup winning team, was born in Argentina. The capital of Argentina is Buenos Aires. Google search results show that the average temperature in Buenos Aires varies throughout the year, but several sources mention an average temperature of around 18°C (64°F).

Answer: The average temperature in the capital city of the country where the current FIFA World Cup champion's team captain was born is approximately 18°C (64°F). This refers to Buenos Aires, Argentina, the birthplace of Lionel Messi.
```

**Explanation**:

-   **Thought**: The agent has gathered all the necessary information: Lionel Messi, captain of the 2022 FIFA World Cup-winning team, was born in Argentina. The capital city is Buenos Aires, with an average temperature of approximately 18°C (64°F).
-   **Action**: It constructs a response summarizing these findings.
-   **Observation**: The agent provides a complete answer: “ _The average temperature in the capital city of the country where the current FIFA World Cup champion’s team captain was born is approximately 18°C (64°F), referring to Buenos Aires, Argentina, the birthplace of Lionel Messi._”

The complete agent trace can be accessed at this [location](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_2.txt).

### Example 3: Comparative Analysis Query

Let’s consider a more complex query that requires advanced reasoning and critical thinking. This type of question doesn’t have a definitive answer, but rather involves exploring multiple sub-questions in a hierarchical manner. The goal is to compare and synthesize all the information gathered to arrive at a comprehensive conclusion. We’ll examine how our React-based agent performs in handling this type of sophisticated, multi-layered analysis.

Query: “ _What is the most common ingredient in the national dishes of the top 5 countries by GDP?_”

**Iteration 1: Initial Query and Breakdown**

```
{
  "thought": "To answer this query, I need to break it down into steps:\n1. Identify the top 5 countries by GDP.\n2. Determine the national dish of each country.\n3. Identify the ingredients in each national dish.\n4. Analyze the ingredients to find the most common one.\n\nI need to use a tool to get the information for steps 1 and 2.",
  "action": {
    "name": "google",
    "reason": "Google can provide a list of the top 5 countries by GDP and information about their national dishes.",
    "input": "top 5 countries by GDP and their national dishes"
  }
}
```

**Explanation**:

-   **Thought**: The agent structures the query into four logical steps: identifying GDP rankings, discovering national dishes, listing ingredients, and analyzing commonalities.
-   **Action**: It chooses Google to retrieve a list of countries with high GDP and corresponding national dishes.
-   **Observation**: The tool returns general results on high GDP countries, but without a clear, unified list of national dishes.

**Iteration 2: Refining the Search**

```
{
  "thought": "The Google search results provided lists of countries by GDP and some information about national dishes, but not a clear and consistent pairing of the two for the top 5 countries. I need to refine my search to get more specific information.",
  "action": {
    "name": "google",
    "reason": "Google is still the best tool to find this information, but I need to be more specific in my query.",
    "input": "National dish of each of the top 5 countries by GDP"
  }
}
```

**Explanation**:

-   **Thought**: Observing that the previous search didn’t yield a cohesive list, the agent decides to refine the query by explicitly requesting the “National dish of each of the top 5 countries by GDP.”
-   **Action**: The agent queries Google again with this refined search.
-   **Observation**: Google still provides general results about national dishes and GDP rankings but lacks a structured pairing of each country with its national dish.

**Iteration 3: Switching to Wikipedia for Specificity**

```
{
  "thought": "The Google search results still don't offer a clear and readily available list of national dishes for the top 5 economies. Wikipedia might have more detailed information about national dishes for each country. I can search for each country individually on Wikipedia and look for information about their national dish.",
  "action": {
    "name": "wikipedia",
    "reason": "Wikipedia is a more comprehensive source for information about specific topics like national dishes.",
    "input": "United States national dish"
  }
}
```

**Explanation**:

-   **Thought**: The agent, realizing that Google results lack specificity, considers Wikipedia as a better source for individually searching each country’s national dish, starting with the United States.
-   **Action**: It queries Wikipedia for “United States national dish.”
-   **Observation**: Wikipedia does not yield a definitive “national dish” for the U.S., highlighting that this approach may not work universally across countries.

**Iteration 4: Expanding Scope to Popular Dishes**

```
{
  "thought": "The Wikipedia search for \"United States national dish\" returned no results. This suggests that a direct search for a single national dish for each country might not be the most effective approach. National dishes can be subjective and vary by region or cultural group. Instead of searching for a single dish, I should broaden my search to include popular or common dishes in each country. I can then analyze the ingredients of these dishes to identify any commonalities.",
  "action": {
    "name": "google",
    "reason": "Google is a better tool for broader searches and can provide a wider range of information about popular dishes in each country.",
    "input": "Popular dishes in the United States"
  }
}
```

**Explanation**:

-   **Thought**: Noting Wikipedia’s limitations for national dishes, the agent broadens its scope to search for “popular dishes” instead. This broader approach should yield enough data on common foods, even if a single national dish is elusive.
-   **Action**: It switches back to Google with the broader query “Popular dishes in the United States.”
-   **Observation**: Google successfully provides a list of popular U.S. dishes, enabling the agent to compile a useful list of notable foods.

**Iteration 5: Continuing with Popular Dishes for Each Country**

```
{
  "thought": "The Google search provided a list of popular dishes in the United States. I can now repeat this process for the remaining top 4 countries by GDP (China, Japan, Germany, and India) to gather information about their popular dishes. Once I have a list of popular dishes for each country, I can then research common ingredients in those dishes to determine the most common one.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in China"
  }
}
```

**Explanation**:

-   **Thought**: Satisfied with the U.S. results, the agent decides to repeat this search process for China, Japan, Germany, and India to collect popular dishes from each.
-   **Action**: It queries Google with “Popular dishes in China” to gather similar data for China.
-   **Observation**: Google provides relevant results for popular dishes in China, enabling the agent to proceed confidently with this approach for each remaining country.

**Iteration 6: Gathering Dishes for Japan**

```
{
  "thought": "I've successfully found lists of popular dishes for the United States and China. I need to continue this process for Japan, Germany, and India to get a comprehensive list of popular dishes for all five countries. Once I have those lists, I can research common ingredients and identify the most frequent one.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in Japan"
  }
}
```

**Explanation**:

-   **Thought**: With data on the U.S. and China, the agent moves on to Japan, maintaining the plan to compile popular dishes for each of the top 5 GDP countries.
-   **Action**: It uses Google to search “Popular dishes in Japan.”
-   **Observation**: Google successfully provides a list of popular Japanese dishes, further supporting this method for gathering culinary data country-by-country.

**Iteration 7: Researching Germany’s Popular Dishes**

```
{
  "thought": "I now have lists of popular dishes for the United States, China, and Japan. I need to find similar lists for Germany and India to complete my data on the top 5 economies. I will use Google again as it has been effective for this purpose.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in Germany"
  }
}
```

**Explanation**:

-   **Thought**: With data on three countries, the agent turns to Germany as it continues gathering popular dishes for each of the top 5 GDP countries.
-   **Action**: It queries Google with “Popular dishes in Germany.”
-   **Observation**: Google returns a comprehensive list of German dishes, allowing the agent to proceed confidently with its plan.

**Iteration 8: Compiling India’s Popular Dishes**

```
{
  "thought": "I have successfully gathered lists of popular dishes for the United States, China, Japan, and Germany. I need to find a similar list for India to complete my data on the top 5 economies. I will use Google again as it has been effective for this purpose.",
  "action": {
    "name": "google",
    "reason": "Google is effective for finding lists of popular dishes in specific countries.",
    "input": "Popular dishes in India"
  }
}
```

**Explanation**:

-   **Thought**: With lists for four countries completed, India is the final country needed to round out the data set for the top five GDP countries.
-   **Action**: The agent queries Google with “Popular dishes in India.”
-   **Observation**: Google successfully provides a list of popular Indian dishes, completing the agent’s data gathering.

**Iteration 9: Planning to Analyze Ingredients**

```
{
  "thought": "I have now gathered lists of popular dishes for all five countries: the United States, China, Japan, Germany, and India. My next step is to analyze these lists and identify common ingredients across the dishes. However, this task is too complex to perform without a tool. I need a way to efficiently research the ingredients of multiple dishes across different cuisines. Since there isn't a specific tool for this purpose, I will try using Google to research the ingredients of each dish individually and note any recurring patterns.",
  "action": {
    "name": "google",
    "reason": "While there isn't a perfect tool for this task, Google can be used to research the ingredients of each dish individually. I will manually analyze the results for commonalities.",
  "input": "Ingredients in [Dish Name]"
 }
}
```

**Explanation**:

-   **Thought**: With popular dishes identified for each country, the agent now plans to analyze the ingredients for these dishes to spot commonalities. Recognizing that this analysis is complex, the agent decides to look up each dish individually.
-   **Action**: The agent begins a series of Google searches focused on identifying ingredients in each specific dish.
-   **Observation**: As Google yields results for each dish’s ingredients, the agent proceeds to manually compare and analyze these ingredients to find any common patterns.

**Iteration 10: Realizing Complexity and Focusing on Common Themes**

```
{
  "thought": "The last Google search returned a list of recipe websites and ingredient resources, but not specific ingredient lists for popular dishes. It seems that finding a single most common ingredient across such diverse cuisines will be difficult. Many ingredients like salt, sugar, and cooking oil are likely used in almost every dish but are not very insightful. Additionally, directly comparing ingredient frequency across vastly different cooking styles and cultural preferences might not be the best way to approach the query. \n\nInstead of focusing on a single ingredient, I can aim for a more general answer about common ingredient types or flavor profiles. To do this, I will research common ingredients and cooking styles for each country's cuisine and look for overarching themes or similarities.",
  "action": {
    "name": "google",
    "reason": "Google can provide information about common ingredients and cooking styles for each country's cuisine.",
    "input": "Common ingredients in [Country] cuisine"
 }
}
```

**Explanation**:

-   **Thought**: The agent realizes that pinpointing a single common ingredient is impractical due to the diversity in cooking styles and ingredient usage. Instead, it shifts focus to identifying broad ingredient types or flavor profiles that are common across these cuisines.
-   **Action**: It adjusts its queries to gather general data on common ingredients and cooking styles for each country.
-   **Observation**: Google provides information about the general culinary profiles and common ingredients, allowing the agent to summarize overarching themes instead of finding a single ingredient.

**Iteration 11: Gathering U.S. Ingredient Data**

```
{
  "thought": "The previous attempts to find a single most common ingredient across the national dishes of the top 5 GDP countries highlighted the difficulty of directly comparing ingredients across diverse culinary traditions.  It's clear that a more nuanced approach is needed. Instead of looking for a single ingredient, I can provide a more insightful answer by identifying common ingredient types or flavor profiles prevalent in these countries' cuisines. I will research common ingredients and cooking styles for each country and then synthesize the information to identify overarching themes.",
  "action": {
    "name": "google",
    "reason": "Google can provide information about common ingredients and cooking styles for each country's cuisine.",
    "input": "Common ingredients in United States cuisine"
 }
}
```

**Explanation**:

-   **Thought**: Having determined that ingredient themes are more insightful, the agent begins by collecting information on common ingredients in American cuisine, expecting to identify regional or staple ingredients that define U.S. culinary styles.
-   **Action**: The agent searches Google with “Common ingredients in United States cuisine.”
-   **Observation**: Google provides detailed information on core American ingredients, including wheat, corn, and various proteins, underscoring the diversity within American food traditions.

**Iteration 12: Researching Chinese Cuisine Ingredients**

```
{
  "thought": "The Google search provided insights into common ingredients in US cuisine, highlighting the diversity and regional variations. To effectively compare culinary trends across the top 5 GDP countries, I need to gather similar information about common ingredients and cooking styles for China, Japan, Germany, and India. Once I have a better understanding of each country's culinary landscape, I can then analyze for common themes or patterns.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Chinese cuisine"
 }
}
```

**Explanation**:

-   **Thought**: With U.S. data gathered, the agent continues with China, aiming to identify common ingredients and cooking methods that characterize Chinese cuisine.
-   **Action**: It queries Google with “Common ingredients in Chinese cuisine.”
-   **Observation**: Google reveals staple Chinese ingredients such as soy sauce, ginger, and garlic, giving the agent a foundation of core components in Chinese cooking.

**Iteration 13: Researching Japanese Cuisine Ingredients**

```
{
  "thought": "I've started gathering information about common ingredients and cooking styles in the cuisines of the top 5 GDP countries. I have data for the United States and China, but I still need to research Japan, Germany, and India. Once I have a better understanding of the culinary landscape for all five countries, I can analyze the information for common themes or patterns and provide a more insightful answer than simply identifying a single ingredient.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Japanese cuisine"
 }
}
```

**Explanation**:

-   **Thought**: After obtaining data on U.S. and Chinese cuisines, the agent moves to Japan to further capture common ingredient patterns and culinary themes.
-   **Action**: The agent uses Google to search for “Common ingredients in Japanese cuisine.”
-   **Observation**: Google provides a list of Japanese staples, such as soy sauce, miso, and rice, which helps the agent outline fundamental elements of Japanese cuisine.

**Iteration 14: Researching German Cuisine Ingredients**

```
{
  "thought": "I have gathered information about common ingredients and cooking styles for three out of the five countries: the United States, China, and Japan. To make a comprehensive analysis and identify overarching themes across the top 5 GDP countries' cuisines, I need to gather similar information for Germany and India.  I will continue using Google as it has been effective for this research.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in German cuisine"
 }
}
```

**Explanation**:

-   **Thought**: With information on three countries, the agent turns to Germany, aiming to gather data on the essential ingredients and cooking styles characteristic of German food.
-   **Action**: It searches Google for “Common ingredients in German cuisine.”
-   **Observation**: Google lists ingredients like potatoes, sausages, and cabbage, helping the agent understand the staples of German cuisine.

**Iteration 15: Researching Indian Cuisine Ingredients**

```
{
  "thought": "I have gathered information about common ingredients and cooking styles for four out of the five countries: the United States, China, Japan, and Germany. To make a comprehensive analysis and identify overarching themes across the top 5 GDP countries' cuisines, I need to gather similar information for India.  I will continue using Google as it has been effective for this research.",
  "action": {
    "name": "google",
    "reason": "Google is effective for gathering information about culinary traditions and common ingredients in different countries.",
    "input": "Common ingredients in Indian cuisine"
 }
}
```

**Explanation**:

-   **Thought**: Having researched the first four countries, the agent now focuses on India, the final country, to complete its dataset of common ingredients across the top five GDP nations.
-   **Action**: The agent queries Google with “Common ingredients in Indian cuisine.”
-   **Observation**: Google provides typical Indian ingredients, including spices like turmeric and cumin as well as staples like rice and lentils, rounding out the agent’s ingredient data for all five countries.

**Iteration 16: Summary of Outcomes**

```
{
  "thought": "I have successfully gathered information about common ingredients and cooking styles for all five countries: the United States, China, Japan, Germany, and India. Now I can analyze this information to identify overarching themes or similarities in ingredient types or flavor profiles. I don't need to use a tool for this step, as I can reason based on the information I've already collected.",
  "answer": "It's challenging to pinpoint a single most common ingredient across the national dishes of the top 5 GDP countries due to their diverse culinary traditions. However, analyzing common ingredients and cooking styles reveals some overarching themes:\n\n* **Starchy Staples:** All five countries heavily feature starchy staples in their cuisines. In the US, it's wheat (bread, pasta) and corn. China relies on rice and noodles. Japan emphasizes rice and noodles (ramen, udon). Germany favors potatoes and bread. India heavily uses rice and wheat (naan, roti).\n* **Protein Variety:** While specific proteins vary, all five countries incorporate a variety of protein sources. The US includes beef, pork, and chicken. China features pork, chicken, duck, and seafood. Japan utilizes seafood, chicken, and pork. Germany commonly uses pork, beef, and poultry. India, with diverse dietary preferences, incorporates chicken, seafood, lamb, and plant-based proteins like lentils.\n* **Flavor Profiles:** While specific flavor combinations are diverse, some common themes emerge. The US leans towards savory and sweet flavors. China often balances sweet, sour, spicy, and salty. Japan emphasizes umami, often achieved through ingredients like soy sauce and dashi. Germany favors hearty and savory flavors. India is renowned for its diverse and aromatic spice blends, often combining heat, sweetness, sourness, and earthiness.\n\nIn conclusion, while a single most common ingredient is difficult to define, these culinary powerhouses share a reliance on starchy staples and diverse protein sources, while expressing unique flavor profiles through their individual culinary traditions."
}
```

**Explanation**:

-   **Thought**: With comprehensive data on common ingredients for the U.S., China, Japan, Germany, and India, the agent is ready to synthesize overarching themes or commonalities in ingredient types and culinary profiles across these cuisines.
-   **Action**: No additional search is required; the agent begins to analyze and formulate a response based on the data collected.
-   **Observation**: The agent concludes that, while a single common ingredient is impractical to define, there are shared themes among the cuisines: reliance on starchy staples, diverse protein sources, and unique flavor profiles.

You can find the full agent trace [here](https://github.com/arunpshankar/react-from-scratch/blob/main/data/output/trace_3.txt). All code files associated with everything we covered here are available in this [GitHub repository](https://github.com/arunpshankar/react-from-scratch/tree/main).

## Future Directions

The ReAct framework opens up numerous possibilities for enhanced functionality and adaptability in agent-based systems. Future developments could focus on integrating the ability to process diverse data types such as images, audio, and video, enabling agents to interpret a broader spectrum of information for richer, context-aware decisions. Organizing agents into layered hierarchies, where primary agents delegate specialized tasks to sub-agents, would improve efficiency and task segmentation. Additionally, empowering agents to collaborate by sharing observations, tools, and resources would amplify insights and support cohesive decision-making in complex, multi-perspective environments. Higher-level agents can dynamically guide and coordinate other agents, orchestrating actions across a multi-agent setup to handle complex, multi-step tasks efficiently.

In future posts, we’ll explore a multi-agent scenario where a single steering agent interacts with multiple sub-agents, each fulfilling distinct tasks and communicating their findings back for a cohesive outcome. This will extend our current exercise, building a foundation for scalable, collaborative agent networks.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="from-llm-reasoning-to-autonomous-ai-agents-arxiv.md">
<details>
<summary>From LLM Reasoning to Autonomous AI Agents - ArXiv</summary>

Phase: [EXPLOITATION]

Phase: [EXPLOITATION]

# From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review

**Source URL:** <https://arxiv.org/pdf/2504.19678>

**Authors:** Mohamed Amine Ferrag, Norbert Tihanyi, and Merouane Debbah

**Affiliations:** Department of Computer and Network Engineering, United Arab Emirates University, UAE; Technology Innovation Institute, UAE; Eötvös Loránd University, Hungary; Research Institute for Digital Future, Khalifa University, UAE

**Corresponding author:** mohamed.ferrag@uaeu.ac.ae

**arXiv:** 2504.19678v2 [cs.AI] 6 Mar 2026

## Abstract

Large language models and autonomous AI agents have evolved rapidly, resulting in a diverse array of evaluation benchmarks, frameworks, and collaboration protocols. Driven by the growing need for standardized evaluation and integration, we systematically consolidate these fragmented efforts into a unified framework. However, the landscape remains fragmented and lacks a unified taxonomy or comprehensive survey. Therefore, we present a side-by-side comparison of benchmarks developed between 2019 and 2025 that evaluate these models and agents across multiple domains. In addition, we propose a taxonomy of approximately 60 benchmarks that cover general and academic knowledge reasoning, mathematical problem-solving, code gener-ation and software engineering, factual grounding and retrieval, domain-specific evaluations, multimodal and embodied tasks, task orchestration, and interactive assessments. Furthermore, we review AI-agent frameworks introduced between 2023 and 2025 that integrate large language models with modular toolkits to enable autonomous decision-making and multi-step reasoning. Moreover, we present real-world applications of autonomous AI agents in materials science, biomedical research, academic ideation, software engineering, synthetic data generation, chem-ical reasoning, mathematical problem-solving, geographic in- formation systems, multimedia, healthcare, and finance. We then survey key agent-to-agent collaboration protocols, namely the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Protocol (A2A). Finally, we discuss recommendations for future research, focusing on advanced reasoning strategies, failure modes in multi-agent LLM systems, automated scientific discovery, dynamic tool integration via reinforcement learning, integrated search capabilities, and security vulnerabilities in agent protocols.


**Index Terms:** Large Language Models, Autonomous AI Agents, Agentic AI, Reasoning, Benchmarks.


## 1 Introduction

Large Language Models (LLMs) such as OpenAI’s GPT-4 [1], Qwen2.5-Omni [2], DeepSeek-R1 [3], and Meta’s LLaMA [4] have transformed AI by enabling human-like text generation and advanced natural language processing, spurring innovation in conversational agents, automated content cre-ation, and real-time translation [5]. Recent enhancements have extended their utility to multimodal tasks, including text-to-image and text-to-video generation that broaden the scope of generative AI applications [6], [7]. However, their dependence on static pre-training data can lead to outdated outputs and hallucinated responses [8], [9], a limitation that Retrieval- Augmented Generation (RAG) addresses by incorporating real-time data from knowledge bases, APIs, or the web [10], [11]. Building on this, the evolution of intelligent agents employing reflection, planning, and multi-agent collaboration has given rise to Agentic RAG systems, which dynamically orchestrate information retrieval and iterative refinement to manage complex workflows effectively [12], [13]. Recent advances in large language models have paved the way for highly autonomous AI systems that can independently handle complex research tasks. These systems, often referred to as agentic AI, can generate hypotheses, conduct literature reviews, design experiments, analyze data, accelerate scientific discovery, and reduce research costs [14], [15], [16], [17]. Several frameworks, such as LitSearch, ResearchArena, and Agent Laboratory, have been developed to automate various research tasks, including citation management and academic survey generation [18], [19], [20]. However, challenges persist, especially in executing domain-specific literature reviews and ensuring the reproducibility and reliability of automated pro-cesses [21], [22]. Parallel to these developments in research au- tomation, large language model-based agents have also begun to transform the medical field [23]. These agents are increas-ingly used for diagnostic support, patient communication, and medical education by integrating clinical guidelines, medical knowledge bases, and healthcare systems [24], [25], [26], [27], [28]. Despite their promise, these applications face significant hurdles, including concerns over reliability, reproducibility, ethical governance, and safety [29], [30], [31]. Addressing these issues is crucial for ensuring that LLM-based agents can be effectively and responsibly incorporated into clinical practice, underscoring the need for comprehensive evaluation frameworks that can reliably measure their performance across various healthcare tasks [32], [33], [34], [35]. LLM-based agents are emerging as a promising frontier in AI, combining reasoning and action to interact with complex digital environments [36], [37]. Therefore, various approaches have been explored to enhance LLM-based agents, from combining reasoning and acting using techniques like React [38] and Monte Carlo Tree Search [39] to synthesizing high-quality data with methods like Learn-by-Interact [40], which sidestep assumptions such as state reversals. Other strategies involve training on human-labeled or GPT-4 distilled data with systems like AgentGen [41] and AgentTuning [42] to generate trajectory data. At the same time, reinforcement learning

methods utilize offline algorithms and iterative refinement through reward models and feedback to enhance efficiency and performance in realistic environments [43], [44]. LLM-based Multi-Agents harness the collective intelligence of multiple specialized agents, enabling advanced capabilities over single-agent systems by simulating complex real-world environments through collaborative planning, discussion, and decision-making. This approach leverages the communicative strengths and domain-specific expertise of LLMs, allowing distinct agents to interact effectively, much like human teams tackling problem-solving tasks [45], [46]. Recent research highlights promising applications across various fields, includ-ing software development [47], [48], multi-robot systems [49], [50], society simulation [51], policy simulation [52], and game simulation [53]. The main contributions of this study are: • We present a comparative table of benchmarks developed between 2019 and 2025 that rigorously evaluate large lan-guage models and autonomous AI agents across multiple domains. • We propose a taxonomy of approximately 60 LLM and AI-agent benchmarks, including general and aca-demic knowledge reasoning, mathematical problem solv- ing, code generation and software engineering, fac-tual grounding and retrieval, domain-specific evaluations, multimodal and embodied tasks, task orchestration, and interactive and agentic assessments. • We present prominent AI-agent frameworks from 2023 to 2025 that integrate large language models with mod-ular toolkits, enabling autonomous decision-making and multi-step reasoning. • We provide applications of autonomous AI agents in various fields, including materials science and biomedical research, academic ideation and software engineering, synthetic data generation and chemical reasoning, mathe-matical problem-solving and geographic information sys- tems, as well as multimedia, healthcare, and finance. • We survey agent-to-agent collaboration protocols, namely the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Pro-tocol (A2A). • We outline recommendations for future research on au-tonomous AI agents, specifically advanced reasoning strategies, failure modes in multi-agent large language model (LLM) systems, automated scientific discovery, dynamic tool integration via reinforcement learning, inte-grated search capabilities, and security vulnerabilities in agent protocols. Fig. 1 illustrates the structure of this survey. Section II presents the related works. Section III provides a side-by-side tabular comparison of state-of-the-art LLM and Agentic AI benchmarks. Section IV reviews AI agent frameworks, AI agent applications, AI agent protocols, and training datasets across various domains. Section V highlights several critical research directions. Finally, Section VI concludes the paper.

## 2 Related Works

The growing field of autonomous AI agents powered by large language models has inspired a wide range of research efforts across multiple domains. In this section, we review the most relevant studies that investigate the integration of LLM-based agents into software engineering, propose agent architectures and evaluation frameworks, explore the devel-opment of multi-agent systems, and examine domain-specific applications, including healthcare, game-theoretic scenarios, GUI interactions, personal assistance, scientific discovery, and chemistry.

### A. LLM-based Agents in Software Engineering

Wang et al. [54] present a survey that bridges Large Lan-guage Model (LLM)-based agent technologies with software engineering (SE). It highlights how LLMs have achieved significant success in various domains and have been in-tegrated into SE tasks, often under the agent paradigm, whether explicitly or implicitly. The study presents a structured framework for LLM-based agents in SE, comprising three primary modules: perception, memory, and action. Jin et al. [55] investigate the use of large language models (LLMs) and LLM-based agents in software engineering, distinguishing between the traditional capabilities of LLMs and the enhanced functionalities offered by autonomous agents. It highlights the significant success of LLMs in tasks such as code genera-tion and vulnerability detection, while also addressing their limitations, specifically the issues of autonomy and self-improvement that LLM-based agents aim to overcome. The paper provides an extensive review of current practices across six key domains: requirement engineering, code generation, autonomous decision-making, software design, test generation, and software maintenance. In a complementary study, Jin et al. [55] investigate the use of large language models (LLMs) and LLM-based agents in software engineering, distinguishing between the traditional capabilities of LLMs and the enhanced functionalities offered by autonomous agents. It highlights the significant success of LLMs in tasks such as code gen-eration and vulnerability detection, while also addressing their limitations, specifically, issues of autonomy and self-improvement that LLM-based agents aim to overcome. The paper provides an extensive review of current practices across six key domains: requirement engineering, code generation, autonomous decision-making, software design, test generation, and software maintenance.

### B. Agent Architectures and Evaluation Frameworks

Singh et al. [56] delves into Agentic Retrieval-Augmented Generation (Agentic RAG), a sophisticated evolution of tra-ditional Retrieval-Augmented Generation systems that en- hances the capabilities of large language models (LLMs). While LLMs have transformed AI through human-like text generation and language understanding, their dependence on static training data often results in outdated or imprecise responses. The paper addresses these limitations by embed-ding autonomous agents within the RAG framework, enabling

Recent advancements in LLMs Agentic AI Collaborative Multi-Agent Systems Main Contributions of the Paper Organization of the Paper How have recent advancements in LLMs and agentic AI impacted autonomous AI systems, and what are the main contributions of this study? Related Works What are the related surveys in the field of LLM-based agents and autonomous AI systems? LLM-based Agents in Software Engineering Agent Architectures and Evaluation Frameworks Multi-Agent Systems Comparison with Our Survey Domain-Specific Applications LLM and Agentic AI Benchmarks What are the key LLM benchmarks developed between 2019 and 2025 for evaluating large language models and agentic AI systems across various domains? MMLU benchmark ComplexFuncBench benchmark Introduction Humanity's Last Exam (HLE) benchmark FACTS Grounding benchmark ProcessBench benchmark OmniDocBench Benchmark Agent-as-a-Judge... AI Agents What are the key AI agent frameworks and applications developed between 2024 and 2025 for achieving autonomous decision-making and dynamic reasoning in real-world tasks? AI Agent frameworks AI Agent applications AI Agents protocols Training datasets Challenges and and Open Problems What are the key challenges and open problems in advancing AI agents and large language models? Conclusion What are the key conclusions and future directions for large language models (LLMs) and autonomous AI agents? AI Agents Reasoning Why Do Multi-Agent LLM Systems Fail? AI Agents in Automated Scientific Discovery Dynamic Tool Integration for Autonomous AI Agents Empowering LLM Agents with Integrated Search via Reinforcement Learning Vulnerabilities of AI Agents Protocols Key conclusions Challenges Future directions

*Figure 1: Survey Structure*

dynamic, real-time data retrieval and adaptive workflows. It details how agentic design patterns such as reflection, planning, tool utilization, and multi-agent collaboration equip these systems to manage complex tasks and support multi-step reasoning. The survey offers a comprehensive taxonomy of Agentic RAG architectures, highlights key applications across various sectors, including healthcare, finance, and education, and outlines practical implementation strategies. Complementing this architectural perspective, Yehudai et al. [57] mark a significant milestone in artificial intelligence by surveying evaluation methodologies for agents powered by large language models (LLMs). It thoroughly reviews the capabilities of these agents, focusing on core functions such as planning, tool utilization, self-reflection, and mem-ory, while assessing specialized applications ranging from web interactions to software engineering and conversational tasks. The authors uncover a clear trend toward developing more rigorous, dynamically updated evaluation frameworks by examining both targeted benchmarks for domain-specific applications and those designed for more generalist agents. Moreover, the paper critically highlights existing deficiencies in the field, notably the need for metrics that more effectively capture cost efficiency, safety, and robustness. In doing so, it maps the current landscape of agent evaluation and sets forth compelling directions for future inquiry, underscoring the importance of scalable and fine-grained evaluation techniques


**Table 1: An overview of selected surveys on AI Agents.**


| Reference | Year | Key Contribution |
|---|---|---|
| Applica-tions AI Agents Protocols & Open Problems LLM-based Agents in Software Engi-neering Wanget al. [54] 2024Survey o |
| a |
| c |
| t |
| i |
| o |
| n |
| f |
| r |
| a |
| m |
| e |
| w |
| o |
| r |
| k. |
| L |
| L |
| M- |
| b |
| a |
| s |
| e |
| d |
| A |
| g |
| e |
| n |
| t |
| s |
| i |
| n |
| S |
| o |
| f |
| t |
| w |
| a |
| r |
| e |
| E |
| n |
| g |
| i- |
| n |
| e |
| e |
| r |
| i |
| n |
| g |
| J |
| in et al. [55] | 2024 | Reviews LLM vs. autonomous-agent capabili-ties across six SE domains; highlights auton- omy gaps. Agent Architectures & |
| c |
| o |
| v |
| e |
| r |
| s |
| m |
| u |
| l |
| t |
| i |
| m |
| o |
| d |
| a |
| l |
| u |
| n |
| d |
| e |
| r |
| s |
| t |
| a |
| n |
| d |
| i |
| n |
| g |
| a |
| n |
| d |
| l |
| a |
| r |
| g |
| e- |
| a |
| c |
| t |
| i |
| o |
| n |
| m |
| o |
| d |
| e |
| l |
| s. |
| P |
| e |
| r |
| s |
| o |
| n |
| a |
| l |
| L |
| L |
| M |
| A |
| g |
| e |
| n |
| t |
| s |
| Li et al. [62] | 2024 | Examines personal LLM agents integrating user data/devices; |
| i |
| n |
| t |
| r |
| o |
| d |
| u |
| c |
| e |
| s |
| a |
| g |
| e |
| n |
| t |
| s |
| f |
| o |
| r |
| l |
| a |
| b |
| c |
| o |
| n |
| t |
| r |
| o |
| l. |
| O |
| u |
| r |
| S |
| u |
| r |
| v |
| e |
| y |
| F |
| e |
| r |
| r |
| ag et al.2025Unified end-to-end survey covering bench-marks, frameworks, applications, protocols, and challenges. in the |
| C |
| h |
| en et al. [58] focus on Role-Playing Agents (RPAs), a growing class of LLM-based agents that mimic human behavior across |

### C. Multi-Agent Systems

Yan et al. [59] provides a comprehensive survey on integrat-ing LLMs into multi-agent systems (MAS). Their work em- phasizes the communication-centric aspects that enable agents to engage in both cooperative and competitive interactions, thereby tackling tasks that are unmanageable for individual agents. The paper examines system-level features, internal communication mechanisms, and challenges, including scala-bility, security, and multimodal integration. In a related study, Guo et al. [45] offer an extensive overview of LLM-based multi-agent systems, charting the evolution from single-agent decision-making to collaborative frameworks that enhance collective problem-solving and world simulation. In a related study, Guo et al. [45] provide an extensive overview of large language model (LLM)-based multi-agent systems, building on the success of LLMs in autonomous planning and reason-ing. The authors detail how the evolution from single-agent decision-making to collaborative multi-agent frameworks has enabled significant advances in complex problem-solving and world simulation. Key aspects of these systems are examined, including the domains and environments they simulate, the profiling and communication strategies employed by individ-ual agents, and the mechanisms that underpin the enhancement of their collective capacities.

### D. Domain-Specific Applications


#### 1. Healthcare: Wang et al. [34] explores the transforma-tive impact of LLM-based agents on healthcare, presenting

a detailed review of their architectures, applications, and inherent challenges. It dissects the core components of medical agent systems, such as system profiles, clinical planning mechanisms, and medical reasoning frameworks, while also discussing methods to enhance external capacities. Major application areas include clinical decision support, medical documentation, training simulations, and overall healthcare service optimization. The survey further evaluates the per-formance of these agents using established frameworks and metrics, identifying persistent challenges such as hallucination management, multimodal integration, and ethical considera-tions.

#### 2. Social Agents in Game-Theoretic Scenarios: Feng et al

[60] provide a review of research on LLM-based social agents in game-theoretic scenarios. This area has gained prominence for assessing social intelligence in AI systems. The authors categorize the literature into three main components. First, the game framework is examined, highlighting various choice- and communication-focused scenarios. Second, the paper explores the attributes of social agents, examining their preferences, beliefs, and reasoning capabilities. Third, it discusses evalua-tion protocols incorporating game-agnostic and game-specific metrics to assess performance. By synthesizing current studies and outlining future research directions, the survey offers valuable insights to further the development and systematic evaluation of social agents within game-theoretic contexts.

#### 3. GUI Agents: Zhang et al. [61] review LLM-brained

GUI agents, marking a paradigm shift in human-computer interaction through integrating multimodal LLMs. It traces the historical evolution of GUI automation, detailing how advancements in natural language understanding, code gen-eration, and visual processing have enabled these agents to interpret complex graphical user interface (GUI) elements and execute multi-step tasks from conversational commands. The survey systematically examines the core components of these systems, including existing frameworks, data collection and utilization methods for training, and the development of specialized large-scale action models for GUI tasks.

#### 4. Personal LLM Agents: Li et al. [62] explore the evo-lution of intelligent personal assistants (IPAs) by focusing on
Personal LLM Agents, LLM-based agents that deeply inte-grate personal data and devices to provide enhanced personal assistance. The authors outline the limitations of traditional IPAs, including insufficient understanding of user intent, task planning, and tool utilization, which have hindered their practi-cality and scalability. In contrast, the emergence of foundation models like LLMs offers new possibilities by leveraging ad-vanced semantic understanding and reasoning for autonomous problem-solving. The survey systematically reviews the archi-tecture and design choices underlying Personal LLM Agents, informed by expert opinions, and examines key challenges related to intelligence, efficiency, and security. Furthermore, it comprehensively analyzes representative solutions addressing these challenges, laying the groundwork for Personal LLM Agents to become a major paradigm in next-generation end-user software.

#### 5. Scientific Discovery: Gridach et al. [22] explore the

transformative role of Agentic AI in scientific discovery, underscoring its potential to automate and enhance research processes. It reviews how these systems, endowed with reason-ing, planning, and autonomous decision-making capabilities, are revolutionizing traditional research activities, including literature reviews, hypothesis generation, experimental design, and data analysis. The paper highlights recent advancements across multiple scientific domains, such as chemistry, biology, and materials science, by categorizing existing Agentic AI systems and tools. It provides a detailed discussion on key evaluation metrics, implementation frameworks, and datasets used in the field, offering valuable insights into current prac-tices. Moreover, the paper critically addresses significant chal- lenges, including automating comprehensive literature reviews, ensuring system reliability, and addressing ethical concerns. It outlines future research directions, emphasizing the im-portance of human-AI collaboration and improved system calibration.

#### 6. Chemistry: Ramos et al. [63] examine the transforma-tive impact of large language models (LLMs) in chemistry,
focusing on their roles in molecule design, property prediction, and synthesis optimization. It highlights how LLMs not only accelerate scientific discovery through automation but also discuss the advent of LLM-based autonomous agents. These agents extend the functionality of LLMs by interfacing with their environment and performing tasks such as literature scraping, automated laboratory control, and synthesis plan-ning. Expanding the discussion beyond chemistry, the review also considers applications across other scientific domains.

### E. Comparison with Our Survey

Table I presents a consolidated view of how existing works cover key themes, benchmarks, AI agent frameworks, AI agent applications, AI agents protocols, and challenges & open prob-lems against our survey. While prior studies typically focus on one or two aspects (e.g., Yehudai et al. [57] on evaluation benchmarks, Singh et al. [56] on RAG architectures, Yan et al. [59] on multi-agent communication, or Wang et al. [34] on domain-specific applications), none integrate the full spectrum of developments in a single, unified treatment. In contrast, our survey is the first to systematically combine state-of-the-art benchmarks, framework design, application domains, communication protocols, and a forward-looking discussion of challenges and open problems, thereby providing researchers with a comprehensive roadmap for advancing LLM-based autonomous AI agents.

## 3 LLM And Agentic AI Benchmarks

This section provides a comprehensive overview of bench-marks developed between 2019 and 2025 that rigorously eval- uate large language models (LLMs) across diverse and chal-lenging domains. For instance, ENIGMAEVAL [64] assesses complex multimodal puzzle-solving by requiring the synthesis of textual and visual clues, while ComplexFuncBench [66] challenges models with multi-step function-calling tasks that mirror real-world scenarios. Humanity’s Last Exam (HLE) [67] further raises the bar by presenting expert-level aca-demic questions across a broad spectrum of subjects, thereby


**Table 2: Summary of LLM Benchmarks (Part 1)**


| Benchmark | Year | Evaluation Focus | Key Features & Details |
|---|---|---|---|
| ENIGMAEVAL [64] | 2025 | Multimodal Reasoning | Contains 1,184 puzzles combining text and images; state-of-the-art systems score only∼7% on standard puzzles and fail on the hardest ones. Evaluates multimodal and long-context reasoning using challenging puzzles from global competitions. Pushes models into unstructured, creative problem-solving scenarios requiring integration of visual and semantic clues. |
| MMLU Benchmark [65] | 2021 | Multitask Knowledge | Comprises 57 diverse tasks (from elementary math to professional law) testing zero-shot and few-shot performance. Assesses broad world knowledge and problem-solving skills; uncovers calibration challenges and imbalances between procedural and declarative knowledge. Designed for general multitask language understanding without task-specific fine-tuning. |
| ComplexFuncBench [66] | 2025 | Function CallingEvaluates complex function calling | tasks with multi-step operations and input lengths up to 128k tokens over more than 1,000 scenarios. Introduces an automatic evaluation framework (ComplexEval) for function calling, testing reasoning over implicit parameters and constraints. Highlights performance differences between closed models (e.g., Claude 3.5, GPT-4) and open models (e.g., Qwen 2.5, Llama 3.1). Humanity’s Last Exam |
| Humanity’s Last Exam (HLE) [67] | 2025 | Academic Reasoning | Features 3,000 questions spanning over 100 subjects, including multi-modal challenges. Developed through a global collaborative effort with nearly 1,000 experts; includes both multiple-choice and short-answer formats with verifiable answers. Exposes significant performance gaps as state-of-the-art LLMs score below 10%, serving as a critical tool for assessing academic reasoning. |
| FACTS Grounding [68] | 2023 | Factual GroundingContains 1,719 examples requiring | detailed responses grounded in source documents, with inputs reaching up to 32,000 tokens. Uses a two-phase evaluation (eligibility and factual grounding) with assessments from frontier LLM judges. Focuses on factual accuracy and information synthesis while excluding creative or complex reasoning tasks. |
| ProcessBench [69] | 2024 | Error DetectionComprises 3,400 math problem cases | with step-by-step solutions and human-annotated error locations. Evaluates models’ ability to detect the earliest error in reasoning; compares process reward models with LLM-based critics. Targets granular error detection in mathematical problem solving. |
| OmniDocBench [70] | 2024 | Document Understanding | A multi-source dataset spanning nine document types with 19 layout categories and 14 attribute labels. Provides a detailed, multi-level evaluation framework for document content extraction, contrasting modular pipelines with end-to-end methods. Addresses challenges such as fuzzy scans, watermarks, and complex layouts in document processing. Agent-as-a- |
| Agent-as-a- Judge [71] | 2024 | Evaluation Methodology | Evaluated on 55 code generation tasks with 365 hierarchical user requirements. Leverages agentic systems to provide granular, intermediate feedback; achieves up to 90% alignment with human judgments. Reduces evaluation cost and time for agentic systems, particularly in code generation tasks. |
| JudgeBench [72] | 2024 | Judgment Evaluation | Consists of 350 challenging response pairs across knowledge, reasoning, math, and coding domains. Transforms existing datasets into paired comparisons with objective correctness, mitigating positional bias through double evaluation. Aims to objectively assess LLM-based judges; fine-tuning can boost judge accuracy significantly. |
| SimpleQA [73] | 2023 | Factual QAContains 4,326 fact-seeking questions | across domains; uses a strict three-tier grading system. Focuses on evaluating factual accuracy and reveals models’ overconfidence in incorrect responses through repeated testing. Highlights current limitations in handling straightforward, factual queries. |
| FineTasks [74] | 2023 | Multilingual Task Selection | Evaluates 185 candidate tasks across nine languages, ultimately selecting 96 reliable tasks; supports over 550 tasks overall. Employs metrics such as monotonicity, low noise, non-random performance, and model ordering consistency to assess task quality. Provides a scalable, multilingual evaluation platform that highlights the impact of task formulation. |
| FRAMES [75] | 2024 | Retrieval & Reasoning | Consists of 824 multi-hop questions requiring integration of 2–15 Wikipedia articles. Unifies evaluations of factual accuracy, retrieval, and reasoning; labels questions with specific reasoning types (e.g., numerical, tabular). Baseline experiments show improvements from 40% (without retrieval) to 66% (with multi-step retrieval). |
| DABStep [76] | 2025 | Step-Based Reasoning | A step-based approach for multi-step reasoning tasks; the best model achieves only a 16% success rate. Decomposes complex problem solving into discrete steps with iterative refinement and self-correction. Highlights the significant challenges in training models for complex, iterative reasoning. |

**Table 3: Summary of LLM Benchmarks (Part 2)**


| Benchmark | Year | Evaluation Focus | Key Features & Details |
|---|---|---|---|
| BFCL v2 [77] | 2025 | Function CallingContains 2,251 | question-function-answer pairs covering simple to parallel function calls. Leverages real-world, user-contributed data to address issues like data contamination and bias in function calling evaluation. Demonstrates that models such as Claude 3.5 and GPT-4 outperform others, while some open models struggle. |
| SWE-Lancer [78] | 2025 | Software Engineering | Consists of over 1,400 freelance software engineering tasks, including independent and managerial tasks with real-world payout data. Uses triple-verified tests for independent tasks and benchmarks managerial decisions against hiring manager selections. Indicates that even advanced models (e.g., Claude 3.5 Sonnet) have low pass rates (26.2%) on implementation tasks. |
| CRAG Benchmark [79] | 2024 | Retrieval- Augmented Generation | Comprises 4,409 question-answer pairs across 5 domains; simulates retrieval with mock APIs. Evaluates the generative component of RAG pipelines; shows improvement from 34% to 63% accuracy with advanced RAG methods. Highlights performance drops for questions involving highly dynamic or less popular facts. |
| OCCULT Benchmark [80] | 2025 | CybersecurityA lightweight framework for | operational evaluation of cybersecurity risks; includes three distinct OCO benchmarks. Simulates real-world threat scenarios to assess LLM capabilities in offensive cyber operations. Preliminary results indicate models like DeepSeek-R1 achieve over 90% in Threat Actor Competency Tests. |
| DIA Benchmark [81] | 2024 | Dynamic Problem Solving | Uses dynamic question templates with mutable parameters across domains (math, cryptography, cybersecurity, computer science). Introduces innovative metrics for reliability and confidence over multiple attempts; emphasizes adaptive intelligence. Reveals gaps in handling complex tasks and compares models’ self-assessment abilities. |
| CyberMetric Benchmark [82] | 2024 | Cybersecurity Knowledge | A suite of multiple-choice Q&A datasets (CyberMetric-80, -500, -2000, -10000) validated over 200 human expert hours. Generated using GPT-3.5 and RAG, it benchmarks cybersecurity knowledge against human performance. Demonstrates that larger, domain-specific models outperform smaller ones in cybersecurity understanding. |
| BIG-Bench Extra Hard [83] | 2025 | Challenging Reasoning | An elevated-difficulty variant of BIG-Bench Hard; average accuracy is 9.8% for general models and 44.8% for reasoning-specialized models. Replaces each BBH task with a more challenging variant to probe reasoning capabilities robustly. Emphasizes substantial room for improvement in general-purpose reasoning skills. |
| MultiAgentBench [84] | 2025 | Multi-AgentEncompasses six domains: research | proposal writing, Minecraft structure building, database error analysis, collaborative coding, competitive Werewolf gameplay, and resource bargaining. Investigates various coordination protocols (star, chain, tree, graph); peer-to-peer communication plus cognitive planning yields a 3% improvement in milestone achievement. Graph-based protocols outperform others in research tasks. GPT-4o-mini achieves the highest average task score; highlights synergy vs. complexity trade-offs in multi-agent LLM settings. |
| GAIA [85] | 2024 | General AI Assistants | 466 curated questions with reference answers; humans achieve 92% accuracy while GPT-4 with plugins only reaches 15%. Emphasizes everyday reasoning tasks involving multi-modality, web browsing, and tool use. Targets AI robustness over specialized skills. Highlights the large performance gap between humans and SOTA models; aims to measure truly general-purpose AI capabilities. |
| CASTLE [86] | 2025 | Vulnerability detection in source | code 250 hand-crafted micro-benchmark programs covering 25 common CWEs; introduces the novel CASTLE Score metric Integrates evaluations across 13 static analysis tools, 10 LLMs, and two formal verification tools; provides a unified framework for comparing diverse methods Formal verification tools (e.g., ESBMC) minimize false positives but miss vulnerabilities beyond model checking; static analyzers generate excessive false positives; LLMs perform well on small code snippets, but accuracy declines and hallucinations increase as code size grows |
| SPIN-Bench [87] | 2025 | Strategic Planning, | Interaction, and Negotiation Evaluates reasoning and strategic behavior in diverse social settings by combining classical PDDL tasks, competitive board games, cooperative card games, and multi-agent negotiation scenarios. Systematically varies action spaces, state complexity, and the number of interacting agents to simulate realistic social interactions, providing both a benchmark and an arena for multi-agent evaluation. Reveals that while LLMs perform basic fact retrieval and short-range planning reasonably well, they struggle with deep multi-hop reasoning and socially adept coordination, highlighting a significant gap in robust multi-agent planning and human–AI teaming. |
| τ -bench [88] | 2024 | Conversational Agent Evaluation | Evaluates dynamic, multi-turn conversations by comparing the final database state with an annotated goal state using a novel pass k metric. Integrates domain-specific API tool usage and strict policy adherence within simulated user interactions to assess agent reliability over multiple trials. Reveals that even state-of-the-art agents (e.g., GPT-4o) succeed on less than 50% of tasks, with marked inconsistency (e.g., pass < 25% in retail), highlighting the need for improved consistency and rule-following. reflecting the growing demand for deeper reasoning and domain-specific proficiency. Additional frameworks such as FACTS Grounding [68] and ProcessBench [69] scrutinize the models’ capacities for generating factually accurate long-form responses and detecting errors in multi-step reasoning. Meanwhile, innovative evaluation paradigms like Agent-as-a- Judge [71], JudgeBench [72], and CyberMetric [82] provide granular insights into cybersecurity competencies and error-detection capabilities. Tables III, II present a comprehensive overview of benchmarks developed between 2024 and 2025. |

### A. ENIGMAEVAL benchmark

ENIGMAEVAL [64] is a benchmark designed to rigorously evaluate advanced language models’ multimodal and long-context reasoning capabilities using challenging puzzles de- rived from global competitions. The dataset comprises 1,184 complex puzzles that combine text and images, requiring mod-els to synthesize disparate clues, perform multi-step deductive reasoning, and integrate visual and semantic information to arrive at unambiguous, verifiable solutions. Unlike conven-tional benchmarks focusing on well-structured academic tasks, ENIGMAEVAL pushes models into unstructured, creative problem-solving scenarios where even state-of-the-art systems achieve only about 7% accuracy on standard puzzles and fail on the hardest ones.

### B. MMLU Benchmark

Measuring Massive Multitask Language Understanding (MMLU) [65] is a comprehensive benchmark designed by Hendrycks et al. (2021) to evaluate large language models across a diverse range of subjects, from elementary mathe-matics to professional law. The benchmark comprises 57 tasks that test models’ ability to apply broad world knowledge and problem-solving skills in zero-shot and few-shot settings, em-phasizing generalization without task-specific fine-tuning. The study also uncovers challenges related to model calibration and the imbalance between procedural and declarative knowledge, highlighting critical areas where current models fall short of expert-level proficiency.

### C. ComplexFuncBench Benchmark

Zhong et al. [66] introduced ComplexFuncBench, a novel benchmark designed to evaluate large language models (LLMs) on complex function calling tasks in real-world set-tings. Unlike previous benchmarks, ComplexFuncBench chal- lenges models with multi-step operations within a single turn, adherence to user-imposed constraints, reasoning over implicit parameter values, and managing extensive input lengths that can exceed 500 tokens, including scenarios with a context win-dow of up to 128k tokens. Complementing the benchmark, the authors present an automatic evaluation framework, Complex- Eval, which quantitatively assesses performance across over 1,000 scenarios derived from five distinct aspects of function calling. Experimental results reveal significant limitations in current state-of-the-art LLMs, with closed models like Claude 3.5 and OpenAI’s GPT-4 outperforming open models such as Qwen 2.5 and Llama 3.1. Notably, the study identifies preva-lent issues, including value errors and premature termination in multi-step function calls, underscoring the need for further research to enhance the function-calling capabilities of LLMs in practical applications.

### D. Humanity’s Last Exam (HLE) Benchmark

Phan et al. [67] introduced Humanity’s Last Exam (HLE), a benchmark designed to push the limits of LLMs by challeng-ing them with expert-level academic tasks. Unlike traditional benchmarks such as MMLU, where LLMs have achieved over 90% accuracy, HLE presents a significantly more demanding test, featuring 3,000 questions spanning over 100 subjects including mathematics, humanities, and the natural sciences. This benchmark is the product of a global collaborative effort, with nearly 1,000 subject matter experts from over 500 institutions contributing questions that are both multi-modal and resistant to quick internet retrieval, ensuring that only genuine deep academic understanding can lead to success. The tasks, which include both multiple-choice and short-answer formats with clearly defined, verifiable answers, expose a sub-stantial performance gap: current state-of-the-art LLMs, such as DeepSeek R1, OpenAI’s models, Google DeepMind Gemini Thinking, and Anthropic Sonnet 3.5, perform at less than 10% accuracy and suffer from high calibration errors, indicating overconfidence in incorrect responses. The results underscore that while existing benchmarks may no longer provide a meaningful measure of progress, HLE serves as a critical tool for assessing the true academic reasoning capabilities of LLMs, potentially heralding a new era in benchmark design as the field moves toward more challenging and nuanced evaluations in the pursuit of artificial general intelligence.

### E. FACTS Grounding benchmark

Google DeepMind introduced FACTS Grounding [68], a comprehensive benchmark designed to evaluate how accu-rately LLMs ground their long-form responses in provided source documents while avoiding hallucinations. The bench-mark comprises 1,719 meticulously crafted examples split into 860 public and 859 private cases that require models to generate detailed answers strictly based on a corresponding context document, with inputs reaching up to 32,000 tokens. Covering diverse domains such as medicine, law, technology, finance, and retail, FACTS Grounding excludes tasks that re-quire creativity, mathematics, or complex reasoning, focusing squarely on factual accuracy and information synthesis. To ensure robust and unbiased evaluation, responses are assessed in two phases: eligibility and factual grounding using a panel of three frontier LLM judges (Gemini 1.5 Pro, GPT-4o, and Claude 3.5 Sonnet), with final scores derived from the aggregation of these assessments. With an online leaderboard hosted on Kaggle already populated with initial results where, for instance, Gemini 2.0 Flash leads with 83.6% accuracy FACTS Grounding aims to drive industry-wide advancements in grounding and factuality, ultimately fostering greater trust and reliability in LLM applications.


### F. ProcessBench benchmark

Qwen team [69] introduced ProcessBench, a novel bench-mark specifically designed to evaluate the ability of language models to detect errors within the reasoning process for mathematical problem solving. ProcessBench comprises 3,400 test cases, primarily drawn from competition- and Olympiad-level math problems, where each case includes a detailed, step-by-step solution with human-annotated error locations. Models are tasked with identifying the earliest erroneous step or confirming that all steps are correct, thereby providing a granular assessment of their reasoning accuracy. The bench-mark is employed to evaluate two classes of models: process reward models (PRMs) and critic models, the latter involving general large language models (LLMs) that are prompted to critique each solution step. Experimental results reveal two key findings. First, existing PRMs generally fail to generalize to more challenging math problems beyond standard datasets like GSM8K and MATH, often underperforming relative to both prompted LLM-based critics and a PRM fine-tuned on a larger, more complex PRM800K dataset. Second, the best open-source model tested, QwQ-32B-Preview, demonstrates error detection capabilities that rival those of the proprietary GPT-4o, although it still falls short compared to reasoning-specialized models like o1-mini.

### G. OmniDocBench Benchmark

Ouyang et al. [70] introduced OmniDocBench, a compre-hensive multi-source benchmark designed to advance auto- mated document content extraction a critical component for high-quality data needs in LLMs and RAG systems. Om-niDocBench features a meticulously curated and annotated dataset spanning nine diverse document types including aca-demic papers, textbooks, slides, notes, and financial documents and utilizes a detailed evaluation framework with 19 layout categories and 14 attribute labels to facilitate multi-level as-sessments. Through extensive comparative analysis of existing modular pipelines and multimodal end-to-end methods, the benchmark reveals that while specialized models (e.g., Nougat) outperform general vision-language models (VLMs) on stan-dard documents, general VLMs exhibit superior resilience and adaptability in challenging scenarios, such as those involving fuzzy scans, watermarks, or colorful backgrounds. Moreover, fine-tuning general VLMs with domain-specific data leads to enhanced performance, as evidenced by high accuracy scores in tasks like formula recognition (with models such as GPT-4o, Mathpix, and UniMERNet achieving around 85–86.8% accu-racy) and table recognition (RapidTable at 82.5%). Nonethe- less, the findings also highlight persistent challenges, notably that complex column layouts continue to degrade reading order accuracy across all evaluated models.

### H. Agent-as-a-Judge

Meta team proposed the Agent-as-a-Judge framework [71], an innovative evaluation approach explicitly designed for agentic systems that overcome the limitations of traditional methods, which either focus solely on outcomes or require extensive manual labor. This framework provides granular, intermediate feedback throughout the task-solving process by leveraging agentic systems to evaluate other agentic systems. The authors demonstrate its effectiveness on code generation tasks using DevAI, a new benchmark comprising 55 real-istic automated AI development tasks annotated with 365 hierarchical user requirements. Their evaluation shows that Agent-as-a-Judge not only dramatically outperforms the con-ventional LLM-as-a-Judge approach (which typically achieves a 60–70% alignment rate with human assessment) but also reaches an impressive 90% alignment with human judgments. Additionally, this method offers substantial cost and time savings, reducing evaluation costs to approximately 2.29% ($30.58 vs. $1,297.50) and cutting evaluation time down to 118.43 minutes compared to 86.5 hours for human assess-ments.

### I. JudgeBench Benchmark

Tan et al. [72] proposed JudgeBench, a novel benchmark designed to objectively evaluate LLM-based judges models that are increasingly employed to assess and improve the outputs of large language models by focusing on their ability to accurately discern factual and logical correctness rather than merely aligning with human stylistic preferences. Unlike prior benchmarks that rely primarily on crowdsourced human evalu-ations, JudgeBench leverages a carefully constructed set of 350 challenging response pairs spanning knowledge, reasoning, math, and coding domains. The benchmark employs a novel pipeline to transform challenging existing datasets into paired comparisons with preference labels based on objective correct-ness while mitigating positional bias through double evaluation with swapped order. Comprehensive testing across various judge architectures, including prompted, fine-tuned, multi-agent judges, and reward models, reveals that even strong models, such as GPT-4o, often perform only marginally better than random guessing, particularly on tasks requiring rigorous error detection in intermediate reasoning steps. Moreover, fine-tuning can significantly boost performance, as evidenced by a 14% improvement observed in Llama 3.1 8B, and reward models achieve accuracies in the 59–64% range.

### J. SimpleQA Benchmark

SimpleQA [73] is a benchmark introduced by OpenAI to assess and improve the factual accuracy of large language models on short, fact-seeking questions. Comprising 4,326 questions spanning domains such as science/tech, politics, art, and geography, SimpleQA challenges models to deliver a single correct answer under a strict three-tier grading system (”correct,” ”incorrect,” or ”not attempted”). While built on foundational datasets such as TriviaQA and Natural Questions, SimpleQA presents a more challenging task for LLMs. Early results indicate that even advanced models, such as OpenAI o1-preview, achieve only 42.7% accuracy (with Claude 3.5 Sonnet trailing at 28.9%), and models tend to exhibit over-confidence in their incorrect responses. Moreover, experiments that repeated the same question 100 times revealed a strong


**Table 4: LLM Benchmark Comparison: Multimodal, Task Diversity, Reasoning & Agentic AI Evaluation**


| Benchmark | Year | Multimodal | Task Description | Reasoning / Complexity | Agentic AI |
|---|---|---|---|---|---|
| DROP [89] | 2019 | No | English discrete reasoning comprehension | High / High | No |
| MMLU [65] | 2020 | No | Academic/general knowledge | High / Moderate | No |
| MATH [90] | 2021 | No | Evaluating mathematical reasoning | High / High | No |
| Codex [91] | 2021 | No | Evaluating LLMs trained on code | Medium / Medium | No |
| MGSM [92] | 2022 | No | Multilingual grade-school math problems | High / High | No |
| FACTS Grounding [68] | 2023 | No | Factual grounding in long responses | High / Low | No |
| SimpleQA [73] | 2023 | No | Factual Q&A | High / Low | No |
| PersonaGym [93] | 2024 | No | Dynamic evaluation framework for persona agents | High / High | Yes |
| FineTasks [74] | 2023 | No | Multilingual task selection | High / Medium | No |
| GAIA [85] | 2023 | Yes | General AI assistant tasks | High / High | No |
| OmniDocBench [70] | 2024 | Yes | Document content extraction | High / Medium | No |
| ProcessBench [69] | 2024 | No | Error detection in math solutions | Low / High | No |
| MIRAI [94] | 2024 | No | Evaluating llm agents for event forecasting | High / High | Yes |
| AppWorld [95] | 2025 | No | Benchmarking Interactive Coding Agents | High / High | Yes |
| VisualAgentBench[96] | 2024 | Yes | Benchmark for evaluating Large Multimodal Models | High / High | Yes |
| ScienceAgentBench [97] | 2024 | No | Evaluation of language agents for Scientific Discovery | High / High | Yes |
| Agent-SafetyBench [98] | 2024 | No | Safety evaluation of LLM agents | High / High | Yes |
| DiscoveryBench [99] | 2024 | No | Data-Driven Discovery | High / High | Yes |
| BLADE [100] | 2024 | No | Benchmark for data-driven scientific discovery | High / High | Yes |
| Dyn-VQA [9] | 2024 | Yes | Adaptive VQA multimodal benchmark | High / High | Yes |
| Agent-as-a-Judge [71] | 2024 | No | Code generation evaluation | Low / Low | Yes |
| JudgeBench [72] | 2024 | No | Evaluation of LLM-based judges | High / High | No |
| FRAMES [75] | 2024 | No | Factuality & retrieval for RAG | High / High | No |
| MedChain [101] | 2024 | No | Interactive clinical decision adaptation | High / High | Yes |
| CRAG [79] | 2024 | No | Factual Q&A for RAG systems | High / High | No |
| DIA [81] | 2024 | Yes | Dynamic problem solving | High / High | No |
| CyberMetric [82] | 2024 | No | Cybersecurity Q&A | Low / Low | No |
| TeamCraft [102] | 2024 | Yes | Collaborative Minecraft multimodal evaluation | High / High | Yes |
| AgentHarm [103] | 2024 | No | LLM jailbreak robustness evaluation | High / High | Yes |
| τ -bench [88] | 2024 | No | Conversational Agent Evaluation | High / High | Yes |
| LegalAgentBench [104] | 2024 | No | Evaluating LLM Agents in Legal Domain | High / High | Yes |
| GPQA [105] | 2024 | No | Biology, physics, and chemistry | High / High | No |
| ENIGMAEVAL [64] | 2025 | Yes | Complex multimodal puzzles | Low / High | No |
| ComplexFuncBench [66] | 2025 | No | Function calling tasks | Medium / High | No |
| MedAgentsBench [106] | 2025 | No | Complex medical reasoning & treatment planning | High / High | Yes |
| Humanity’s Last Exam [67] | 2025 | Yes | Expert-level academic tasks | High / High | No |
| DABStep [76] | 2025 | No | Step-based multi-step reasoning | Low / High | No |
| BFCL v2 [77] | 2025 | No | Function calling evaluation | High / High | No |
| SWE-Lancer [78] | 2025 | No | Freelance software engineering tasks | High / Moderate | No |
| OCCULT [80] | 2025 | No | Cyber security operational tasks | Medium / High | No |
| BIG-Bench Extra Hard [83] | 2025 | No | Challenging reasoning tasks | High / High | No |
| MultiAgentBench [84] | 2025 | Yes | Multi-agent coordination tasks | High / High | Yes |
| CASTLE [86] | 2025 | No | Software vulnerability detection | Low / Medium | No |
| EmbodiedEval [107] | 2025 | Yes | 3D embodied tasks benchmark | Medium / High | Yes |
| SPIN-Bench [87] | 2025 | Yes | Strategic planning & social reasoning | High / High | Yes |
| OlympicArena [108] | 2025 | Yes | Olympic competition problems | Medium / High | No |
| SciReplicate-Bench [109] | 2025 | No | Algorithm-driven code generation | High / High | Yes |
| EconAgentBench [110] | 2025 | No | Decision-making tasks in economic environments | High / High | Yes |
| VeriLA [111] | 2025 | No | Human-centered LLM failure verification | High / High | Yes |
| CapaBench [112] | 2025 | No | Evaluation of modular contributions in LLM agents | High / High | Yes |
| AgentOrca [113] | 2025 | No | Dual-system agent compliance evaluation | High / High | Yes |
| ProjectEval [114] | 2025 | No | Project-level code generation evaluation | Medium / High | Yes |
| RefactorBench [115] | 2025 | No | Autonomous multi-file refactoring evaluation | High / High | Yes |
| BEARCUBS [116] | 2025 | Yes | Multimodal web agents evaluation | High / Medium | Yes |
| Robotouille [117] | 2025 | No | Asynchronous Planning Benchmark | High / High | Yes |
| DSGBench [118] | 2025 | No | Strategic games decision evaluation | Medium / High | Yes |
| TheoremExplainBench [119] | 2025 | Yes | STEM theorem animation videos | Medium / High | Yes |
| RefuteBench 2.0 [120] | 2025 | No | Multi-turn LLM feedback evaluation | High / High | Yes |
| MLGym [121] | 2025 | Yes | ML agents automate research | High / High | Yes |
| DataSciBench [122] | 2025 | No | LLM Data Science Benchmark | High / High | Yes |
| EmbodiedBench [123] | 2025 | Yes | Vision-driven embodied agent evaluation | High / High | Yes |
| BrowseComp [124] | 2025 | No | Benchmark for Browsing Agents | High / High | Yes |
| Vending-Bench [125] | 2025 | No | Long-horizon business simulation | Medium / High | Yes |
| MLE-bench [126] | 2025 | No | ML engineering-related competitions from Kaggle | Medium / High | Yes |
| SWE-PolyBench [127] | 2025 | No | Evaluation of coding agents | High / High | Yes |
| Multi-SWE-bench [128] | 2025 | No | Multilingual Benchmark for Issue Resolving | High / High | No |

### K. FineTasks

FineTasks [74] is a data-driven evaluation framework de-signed to systematically select reliable tasks for assessing LLMs across diverse languages. Developed as the first step toward the broader FineWeb Multilingual initiative, Fine- Tasks evaluates candidate tasks based on four critical metrics: monotonicity, low noise, non-random performance, and model ordering consistency to ensure robustness and reliability. In an extensive study, the Hugging Face team tested 185 candi-date tasks across nine languages (including Chinese, French, Arabic, Russian, Thai, Hindi, Turkish, Swahili, and Telugu), ultimately selecting 96 final tasks that cover domains such as reading comprehension, general knowledge, language un-derstanding, and reasoning. The work further reveals that the formulation of tasks has a significant impact on performance; for instance, Cloze format tasks are more effective during early training phases, while multiple-choice formats yield better evaluation results. Recommended evaluation metrics include length normalization for most tasks and pointwise mutual information (PMI) for complex reasoning challenges. Benchmarking 35 open and closed-source LLMs demonstrated that open models are narrowing the gap with their proprietary counterparts, with Qwen 2 models excelling in high- and mid-resource languages and Gemma-2 particularly strong in low- resource settings. Moreover, the FineTasks framework supports over 550 tasks across various languages, providing a scalable and comprehensive platform for advancing multilingual large language model (LLM) evaluation.

### L. FRAMES benchmark

Google team [75] propose FRAMES (Factuality, Retrieval, and Reasoning MEasurement Set), a comprehensive evaluation dataset specifically designed to assess the capabilities of retrieval-augmented generation (RAG) systems built on LLMs. FRAMES addresses a critical need by unifying evaluations of factual accuracy, retrieval effectiveness, and reasoning abil-ity in an end-to-end framework, rather than assessing these facets in isolation. The dataset comprises 824 challenging multi-hop questions spanning diverse topics, including history, sports, science, and health, each requiring the integration of information from between two and fifteen Wikipedia articles. By labeling questions with specific reasoning types, such as numerical or tabular. FRAMES provides a nuanced benchmark to identify the strengths and weaknesses of current RAG implementations. Baseline experiments reveal that state-of-the-art models like Gemini-Pro-1.5-0514 achieve only 40% accuracy when operating without retrieval mechanisms, but their performance increases significantly to 66% with a multi-step retrieval pipeline, representing a greater than 50% im- provement.

### M. DABStep benchmark

DabStep [76] is a new framework from Hugging Face that pioneers a step-based approach to enhance the performance and efficiency of language models on multi-step reasoning tasks. DabStep addresses the challenges of traditional end-to-end inference by decomposing complex problem-solving into discrete, manageable steps, enabling models to refine their outputs through step-level feedback and iterative dynamic adjustments. This method is designed to enable models to self-correct and navigate the complexities of multi-step reasoning processes more effectively. However, despite these innovative improvements, experimental results reveal that even the best-performing model under this framework only achieves a 16% success rate on the evaluated tasks. This modest accuracy un-derscores the significant challenges that remain in effectively training models for complex, iterative reasoning and highlights the need for further research and optimization.

### N. BFCL v2 benchmark

Mao et al. [77] propose BFCL v2, a novel benchmark and leaderboard designed to evaluate large language models’ function-calling abilities using real-world, user-contributed data. The benchmark comprises 2,251 question-function-answer pairs, enabling comprehensive assessments across a range of scenarios from multiple and straightforward function calls to parallel executions and irrelevance detection. By lever-aging authentic user interactions, BFCL v2 addresses prevalent issues such as data contamination, bias, and limited gener-alization in previous evaluation methods. Initial evaluations reveal that models like Claude 3.5 and GPT-4 consistently outperform others, with Mistral, Llama 3.1 FT, and Gemini following in performance. However, some open models, such as Hermes, struggle due to potential prompting and formatting challenges. Overall, BFCL v2 offers a rigorous and diverse platform for benchmarking the practical capabilities of LLMs in interfacing with external tools and APIs, thereby providing valuable insights for future advancements in function calling and interactive AI systems.

### O. SWE-Lancer benchmark

OpenAI team [78] presents SWE-Lancer, an innovative benchmark comprised of over 1,400 freelance software engi-neering tasks collected from Upwork, representing more than $1 million in real-world payouts. This benchmark encom-passes both independent engineering tasks, ranging from minor bug fixes to substantial feature implementations valued up to $32,000, and managerial tasks, where models must select the best technical proposals. Independent tasks are rigorously eval-uated using end-to-end tests that have been triple-verified by experienced engineers. At the same time, managerial decisions are benchmarked against the selections made by the original hiring managers. Experimental results indicate that state-of-the-art models, such as Claude 3.5 Sonnet, still struggle with the majority of these tasks, achieving a 26.2% pass rate on independent tasks and 44.9% on managerial tasks, which translates to an estimated earning of $403K a figure well below

the total available value. Notably, the analysis highlights that while models tend to perform better in evaluative managerial roles than in direct code implementation, increasing inference-time computing can enhance performance.

### P. Comprehensive RAG Benchmark (CRAG)

Yang et al. [79] propose the Comprehensive RAG Bench-mark (CRAG), a novel dataset designed to evaluate the factual question-answering capabilities of Retrieval-Augmented Gen-eration systems rigorously. CRAG comprises 4,409 question- answer pairs across five domains and eight distinct question categories. It incorporates mock APIs to simulate web and Knowledge Graph retrieval, thereby reflecting the varied levels of entity popularity and temporal dynamism encountered in real-world scenarios. Empirical results show that state-of-the-art large language models without grounding achieve only around 34% accuracy on CRAG, and that incorporating simple RAG methods improves this to just 44%, whereas industry-leading RAG systems can reach 63% accuracy without hal- lucination. The benchmark also highlights significant perfor-mance drops for questions involving highly dynamic, lower- popularity, or more complex facts. Notably, CRAG focuses solely on evaluating the generative component of the RAG pipeline, and early findings indicate that Llama 3 70B nearly matches GPT-4 Turbo across these tasks.

### Q. OCCULT Benchmark

Kouremetis et al. [80] present OCCULT, a novel and lightweight operational evaluation framework that rigorously measures the cybersecurity risks associated with using large language models (LLMs) for offensive cyber operations (OCO). Traditionally, evaluating AI in cybersecurity has relied on simplistic, all-or-nothing tests such as capture-the-flag exer-cises, which fail to capture the nuanced threats faced by mod- ern infrastructure. In contrast, OCCULT enables cybersecurity experts to craft repeatable and contextualized benchmarks by simulating real-world threat scenarios. The authors detail three distinct OCO benchmarks designed to assess the capability of LLMs to execute adversarial tactics, providing preliminary evaluation results that indicate a significant advancement in AI-enabled cyber threats. Most notably, the DeepSeek-R1 model correctly answered over 90% of questions in the Threat Actor Competency Test for LLMs (TACTL).

### R. DIA benchmark

Dynamic Intelligence Assessment (DIA) [81] is introduced as a novel methodology to more rigorously test and compare the problem-solving abilities of AI models across diverse do-mains such as mathematics, cryptography, cybersecurity, and computer science. Unlike traditional benchmarks that rely on static question-answer pairs, often allowing models to perform uniformly well or rely on memorization, DIA employs dy-namic question templates with mutable parameters, presented in various formats including text, PDFs, compiled binaries, visual puzzles, and CTF-style challenges. This framework also introduces four innovative metrics to evaluate a model’s reliability and confidence across multiple attempts, revealing that even simple questions are frequently answered incor-rectly when posed in different forms. Notably, the evaluation shows that while API models like GPT-4o may overestimate their mathematical capabilities, models such as ChatGPT-4o perform better due to practical tool usage, and OpenAI’s o1-mini excels in self-assessment of task suitability. Testing 25 state-of-the-art LLMs with DIA-Bench reveals significant gaps in handling complex tasks and in adaptive intelligence, establishing a new standard for evaluating both problem-solving performance and a model’s ability to recognize its own limitations.

### S. CyberMetric benchmark

Tihanyi et al. [82] introduce a suite of novel multiple-choice Q&A benchmark datasets, CyberMetric-80, CyberMetric-500, CyberMetric-2000, and CyberMetric-10000, designed to evaluate the cybersecurity knowledge of LLMs rigorously. By leveraging GPT-3.5 and Retrieval-Augmented Generation (RAG), the authors generated questions from diverse cyber-security sources such as NIST standards, research papers, publicly accessible books, and RFCs. Complete with four possible answers, each question underwent extensive rounds of error checking and refinement, with over 200 hours of human expert validation to ensure accuracy and domain rel-evance. Evaluations were conducted on 25 state-of-the-art large language models (LLMs), and the results were further benchmarked against human performance on CyberMetric-80 in a closed-book scenario. Findings reveal that models like GPT-4o, GPT-4-turbo, Mixtral-8x7 B-Instruct, Falcon-180 B- Chat, and GEMINI-pro 1.0 exhibit superior cybersecurity un-derstanding, outperforming humans on CyberMetric-80, while smaller models such as Llama-3-8B, Phi-2, and Gemma-7b lag behind, underscoring the value of model scale and domain-specific data in this challenging field.

### T. BIG-Bench Extra Hard

A team from Google DeepMind [83] addresses a critical gap in evaluating large language models by tackling the limi-tations of current reasoning benchmarks, which have primarily focused on mathematical and coding tasks. While the BIG- Bench dataset [129] and its more complex variant, BIG-Bench Hard (BBH) [130], have provided comprehensive assessments of general reasoning abilities, recent advances in LLMs have led to saturation, with state-of-the-art models achieving near-perfect scores on many BBH tasks. To overcome this, the authors introduce BIG-Bench Extra Hard (BBEH). This novel benchmark replaces each BBH task with a more challenging variant designed to probe similar reasoning capabilities at an elevated difficulty level. Evaluations on BBEH reveal that even the best general-purpose models only achieve an average accuracy of 9.8%, while reasoning-specialized models reach 44.8%, highlighting substantial room for improvement and underscoring the ongoing challenge of developing LLMs with robust, versatile reasoning skills.


### U. MultiAgentBench benchmark

Zhu et al. [84] introduce MultiAgentBench, a benchmark specifically designed to evaluate the capabilities of multi-agent systems powered by LLMs in dynamic, interactive environments. Unlike traditional benchmarks that focus on single-agent performance or narrow domains, MultiAgent- Bench encompasses six diverse domains, including research proposal writing, Minecraft structure building, database error analysis, collaborative coding, competitive Werewolf game-play, and resource bargaining to measure both task comple- tion and the quality of agent coordination using milestone-based performance indicators. The study investigates various coordination protocols, such as star, chain, tree, and graph topologies, and finds that direct peer-to-peer communication and cognitive planning are particularly effective evidenced by a 3% improvement in milestone achievement when planning is employed while also noting that adding more agents can decrease performance. Among the models evaluated (GPT-4o-mini, 3.5, and Llama), GPT-4o-mini achieved the highest average task score, and graph-based coordination protocols outperformed other structures in research scenarios.

### V. GAIA Benchmark

GAIA [85] is a groundbreaking benchmark designed to assess General AI Assistants on real-world questions that tap into fundamental abilities like reasoning, multi-modality handling, web browsing, and tool use. Unlike traditional benchmarks that focus on increasingly specialized tasks, GAIA features conceptually simple questions solvable by humans at 92% accuracy that current systems, such as GPT-4 with plugins, struggle with, achieving only 15%. Comprising 466 meticulously curated questions with reference answers, GAIA shifts the evaluation paradigm toward measuring AI robustness in everyday reasoning tasks, a critical step toward achieving true Artificial General Intelligence (AGI). This substantial performance gap between humans and state-of-the-art models emphasizes the need for AI systems that can mimic the general-purpose, resilient reasoning exhibited by average hu-man problem solvers.

### W. CASTLE Benchmark

Dubniczky et al. [86] introduce CASTLE, a novel bench-marking framework for evaluating software vulnerability detection methods, addressing existing approaches’ critical weaknesses. CASTLE assesses 13 static analysis tools, 10 LLMs, and two formal verification tools using a meticulously curated dataset of 250 micro-benchmark programs that cover 25 common CWEs. The framework proposes a new evaluation metric, the CASTLE Score, to enable fair comparisons across different methods. Results reveal that while formal verification tools like ESBMC minimize false positives, they struggle with vulnerabilities beyond the scope of model checking. Static an-alyzers often generate excessive false positives, which burden developers with manual validation. LLMs perform strongly on small code snippets; however, their accuracy declines, and hallucinations increase as code size grows. These findings suggest that, despite current limitations, LLMs hold significant promise for integration into code completion frameworks, providing real-time vulnerability prevention and marking an important step toward more secure software systems.

### X. SPIN-Bench Benchmark

Yao et al. [87] introduce a comprehensive evaluation frame-work, SPIN-Bench, highlighting the challenges of strategic planning and social reasoning in AI agents. Unlike traditional benchmarks focused on isolated tasks, SPIN-Bench combines classical planning, competitive board games, cooperative card games, and negotiation scenarios to simulate real-world social interactions. This multifaceted approach reveals significant performance bottlenecks in current large language models (LLMs), which, while adept at factual retrieval and short-range planning, struggle with deep multi-hop reasoning, spa- tial inference, and socially coordinated decision-making. For instance, models perform reasonably well on simple tasks like Tic-Tac-Toe but falter in complex environments such as Chess or Diplomacy, and even the best models achieve only around 58.59% accuracy on classical planning tasks. Y.τ -bench Yao et al. [88] presentτ -bench, a benchmark designed to evaluate language agents in realistic, dynamic, multi-turn conversational settings that emulate real-world environments. Inτ -bench, agents are challenged to interact with a simulated user to understand needs, utilize domain-specific API tools (such as booking flights or returning items), and adhere to provided policy guidelines, while performance is measured by comparing the final database state with an annotated goal state. A novel metric, pass k , is introduced to assess reliability over multiple trials. Experimental findings reveal that even state-of-the-art function-calling agents like GPT-4o succeed on less than 50% of tasks, with significant inconsistency (for example, pass scores below 25% in retail domains) and markedly lower success rates for tasks requiring multiple database writes. These results underscore the need for enhanced methods that improve consistency, adherence to rules, and overall reliability in language agents for real-world applications.

### Z. Discussion and Comparison of LLM Benchmarks

Table IV presents an extensive overview of benchmarks de-veloped from 2019 to 2025 for evaluating large language mod- els (LLMs) concerning multimodal capabilities, task scope, diversity, reasoning, and agentic behaviors. Early benchmarks, such as DROP [89], MMLU [65], MATH [90], Codex [91], MGSM [92], FACTS Grounding [68], and SimpleQA [73], concentrated on core competencies like discrete reasoning, academic knowledge, mathematical problem solving, and fac-tual grounding. These pioneering efforts lay the groundwork for performance evaluation in language understanding and reasoning tasks, setting a baseline against which later, more sophisticated benchmarks have been compared. A notable progression in benchmark design is observed with the emergence of frameworks that target more complex

LLM Benchmark Academic & General Knowledge Reasoning DROP [89] MMLU [65] BIG-Bench Extra Hard [83] Humanity’s Last Exam [67] DABStep [76] Mathematical Problem Solving MATH [90] MGSM [92] ProcessBench [69] Code & Software Engineering Codex [91] Agent-as-a-Judge [71] AppWorld [95] SciReplicate- Bench [109] ProjectEval [114] RefactorBench [115] SWE- Lancer [78] CASTLE [86] SWE- PolyBench [127] MLE-bench [126] ComplexFuncBench [66] BFCL v2 [77] Factual Grounding & Retrieval FACTS Grounding [68] SimpleQA [73] FRAMES [75] CRAG [79] GPQA [105] Domain- Specific Evaluations MedChain [101] LegalAgentBench [104] MedAgentsBench [106] CyberMetric [82] OCCULT [80] EconAgentBench [110] Multimodal, Visual & Embodied Evaluations GAIA [85] OmniDocBench [70] Dyn-VQA [9] DIA [81] OlympicArena [108] BEARCUBS [116] EmbodiedEval [107] EmbodiedBench [123] ENIGMAEVAL [64] TheoremExplainBench [119] VisualAgentBench [96] Task Selection FineTasks [74] Multi- SWE-bench [128] Agentic & Interactive Evaluations PersonaGym [93] MIRAI [94] ScienceAgentBench [97] Agent- SafetyBench [98] DiscoveryBench [99] BLADE [100] JudgeBench [72] TeamCraft [102] AgentHarm [103] τ -bench [88] MultiAgentBench [84] SPIN- Bench [87] VeriLA [111] CapaBench [112] AgentOrca [113] Robotouille [117] DSGBench [118] RefuteBench 2.0 [120] MLGym [121] DataSciBench [122] BrowseComp [124]

*Figure 2: Classification of LLM Benchmarks for AI Agents Applications*

agentic and multimodal tasks. For instance, PersonaGym [93] and FineTasks [74] introduce dynamic persona evaluation and multilingual task selection. GAIA [85] expands the evaluative scope to general AI assistant tasks while OmniDocBench [70] and ProcessBench [69] address document extraction and error detection in mathematical solutions. Further, MIRAI [94], AppWorld [95], VisualAgentBench [96], and ScienceAgent- Bench [97] explore various facets of multimodal and scientific discovery tasks. This decade-spanning evolution is comple-mented by additional evaluations focusing on safety (Agent- SafetyBench [98]), discovery (DiscoveryBench [99]), code generation (BLADE [100], Dyn-VQA [9], and Agent-as-a- Judge [71]), judicial reasoning (JudgeBench [72]), and clinical decision making (MedChain [101]), among others including FRAMES [75], CRAG [79], DIA [81], CyberMetric [82], TeamCraft [102], AgentHarm [103],τ -bench [88], LegalA-gentBench [104], and GPQA [105]. Recent benchmarks from 2025 further indicate a sub-stantial expansion in the depth and breadth of large lan- guage model (LLM) evaluations. ENIGMAEVAL [64] and ComplexFuncBench [66] target complex puzzles and func-tion calling tasks, while MedAgentsBench [106] and Hu- manity’s Last Exam [67] focus on advanced medical rea-soning and expert-level academic tasks. Additional bench- marks such as DABStep [76], BFCL v2 [77], SWE- Lancer [78], and OCCULT [80] further diversify evalua-tive criteria by incorporating multi-step reasoning, cyberse- curity, and freelance software engineering challenges. The table also includes BIG-Bench Extra Hard [83], MultiA-gentBench [84], CASTLE [86], EmbodiedEval [107], SPIN- Bench [87], OlympicArena [108], SciReplicate-Bench [109], EconAgentBench [110], VeriLA [111], CapaBench [112], AgentOrca [113], ProjectEval [114], RefactorBench [115], BEARCUBS [116], Robotouille [117], DSGBench [118], TheoremExplainBench [119], RefuteBench 2.0 [120], ML- Gym [121], DataSciBench [122], EmbodiedBench [123], BrowseComp [124], and MLE-bench [126]. Collectively, these benchmarks exemplify the field’s shift towards more compre-hensive and nuanced evaluation metrics, supporting the de- velopment of LLMs that can tackle increasingly multifaceted,

Strategy Development (Planning) Self-Evaluation Thinking (Reasoning) & Prompt (Instructions) Task (Assigned Objective) Designated Function AI Query Engines Utility Functions & Knowledge Store Knowledge Store Agent Execution Environment

*Figure 3: Core Elements of AI Agents*

real-world challenges. Fig. 2 groups benchmarks into categories such as Academic & General Knowledge Reasoning, Mathematical Problem Solving, Code & Software Engineering, Factual Grounding & Retrieval, Domain-Specific Evaluations, Multimodal/Visual & Embodied Evaluations, Task Selection, and Agentic & Interactive Evaluations, illustrating the full range of tasks used to assess LLMs in AI agent settings.

## 4 AI Agents

This section presents a comprehensive overview of AI agent frameworks and applications developed between 2024 and 2025, highlighting transformative approaches that integrate large language models with modular tools to achieve au-tonomous decision-making and dynamic multi-step reason- ing. The frameworks discussed include LangChain [131], LlamaIndex [132], CrewAI [133], and Swarm [134], which abstract complex functionalities into reusable components that enable context management, tool integration, and iterative refinement of outputs. Additionally, pioneering efforts in GUI control [135] and agentic reasoning [136], [137] demonstrate the increasing capabilities of these systems to interact with external environments and tools in real-time. In parallel, this section presents a diverse range of AI agent applications that span materials science, biomedical research, academic ideation, software engineering, synthetic data generation, and chemical reasoning. Systems such as the StarWhisper Telescope System [139] and HoneyComb [140] have revolutionized operational workflows by automat-ing observational and analytical tasks in materials science. In the biomedical domain, platforms like GeneAgent [141] and frameworks such as PRefLexOR [142] demonstrate enhanced reliability through self-verification and iterative refinement. Moreover, innovative solutions for research ideation, exem-plified by SurveyX [143] and Chain-of-Ideas [144], as well as specialized frameworks for synthetic data generation [145] and chemical reasoning [146], collectively underscore the significant strides made in leveraging autonomous AI agents for complex, real-world tasks. Table V presents an overview of AI Agent frameworks.

### A. AI Agent frameworks

AI agent frameworks represent a transformative paradigm in developing intelligent systems, combining the power of large language models with modular tools and utilities to build autonomous software agents. These frameworks abstract complex functionalities such as natural language understand-ing, multi-step reasoning, and dynamic decision-making into reusable components that streamline prototyping, iterative refinement, and deployment. By integrating advanced LLMs with external tools and specialized functions, developers can create agents that process and generate language and adapt to complex workflows and diverse operational contexts [147]. Fig. 3 illustrates a comprehensive AI agent framework where each component plays a crucial role in achieving adaptive, autonomous decision-making. An assigned task is first approached through a designated function that defines the agent’s role, followed by strategy development, essentially the planning phase, where the agent breaks down complex objectives into actionable steps. This is supported by an iterative thinking process, driven by reasoning and guided by prompts, which enables the agent to reflect on its ac-tions and refine its approach. Core operational support comes from AI query engines and utility functions that interface with an integrated knowledge store, ensuring that both static and real-time information is readily accessible. Ultimately, these elements operate within an agent execution environment, seamlessly combining planning, reasoning, and execution into a responsive and self-evolving system. Agentic workflows transform traditional, rigid processes into dynamic, adaptive systems. As illustrated in Fig. 4, these workflows begin at the user interface, where a user query is submitted and receives a system reply. Unlike deterministic workflows that follow fixed, unchanging rules, an agent-based process involves AI agents who actively formulate a strategy, carry out tasks using available tools, and evaluate the outcomes. This cycle, ranging from planning to execution and ultimately to assessment, where outcomes are marked as either satisfactory or unsatisfactory, empowers the system to respond to real-world challenges more flexibly and autonomously [148]. Agentic Retrieval-Augmented Generation (RAG) integrates a language model’s advanced capabilities with dynamic data retrieval and processing. As shown in Fig. 5, the process begins at the user interface, where a query is submitted and a system reply is generated. The system first checks its internal knowledge store to determine whether the query has been addressed or needs more data. When necessary, the query is decomposed into smaller, manageable sub-questions that are individually routed and processed through retrieval utilities [149]. These utilities fetch relevant external data, and the system evaluates whether the retrieved information is applicable before producing a final output. This layered, agentic approach ensures that responses are accurate, context-aware, and continuously refined throughout the process [150]. Tab. VI demonstrates that retrieval-augmented generation (RAG) is highly effective at producing up-to-date, accurate responses, making it ideal for fields like healthcare or law,


**Table 5: Overview of AI Agent Frameworks: Core Concepts, Workflow, and Advantages**


| Framework | Core Idea | Workflow & Components | Key Advantages |
|---|---|---|---|
| LangChain [131] | Integrates LLMs with diverse tools to build autonomous agents. | Combines conversational LLMs, search integrations, and utility functions into iterative workflows. | Customizable roles and streamlined agent prototyping. |
| LlamaIndex [132] | Enables autonomous agent creation via external tool integration. | Wraps functions into FunctionTool objects and employs a ReActAgent for stepwise tool selection. | Simplifies agent development with a dynamic, modular pipeline. |
| CrewAI [133] | Orchestrates teams of specialized AI agents for complex tasks. | Structures systems into Crew (oversight), AI Agents (specialized roles), Process (collaboration), and Tasks (assignments). | Mimics human team collaboration with flexible, parallel workflows. |
| Swarm [134] | Provides a lightweight, stateless abstraction for multi-agent systems. | Defines multiple agents with specific instructions and roles; enables dynamic handoffs and context management. | Fine-grained control and compatibility with various backends. |
| GUI Agent [135] | Facilitates computer control via natural language and visual inputs. | Translates user instructions and screenshots into desktop actions (e.g., cursor movements, clicks). | Demonstrates end-to-end performance in real-world desktop workflows. |
| Agentic Reasoning [136] | Enhances reasoning by integrating specialized external tool-using agents. | Leverages web-search, coding, and Mind Map agents to iteratively refine multi-step reasoning. | Achieves improved multi-step problem-solving and structured knowledge synthesis. |
| OctoTools [137] | Empowers LLMs for complex reasoning via training-free tool integration. | Combines standardized tool cards, a strategic planner, and an executor for effective tool usage. | Outperforms similar frameworks by up to 10.6% on varied tasks. |
| Agents SDK [138] | Provides a modular framework for building autonomous agent applications that integrate LLMs with external tools and advanced features. | Offers core primitives such as Agents (LLMs with instructions, tools, handoffs, and guardrails), Tools (wrapped functions/APIs), Context for state management, along with support for Streaming, Tracing, and Guardrails to manage multi-turn interactions. | Streamlines development with an extensible, robust architecture that enhances debuggability and scalability, enabling rapid prototyping and seamless integration of complex, multi-agent workflows. |

**Table 6: Comparative Analysis of LLM Strategies in RAG, AI Agents, and Agentic RAG**


| Feature | LLM Pre-trained | LLM Post-Training & Fine-Tuning | RAG | AI Agents | Agentic RAG |
|---|---|---|---|---|---|
| Core Function | Uses LLM for text generation. | Applies task-specific tuning. | Retrieves data and generates text. | Automates tasks and decisions. | Integrates retrieval with adaptive reasoning. |
| Autonomy | Basic language understanding. | Enhances autonomy through tuning. | Limited; user-driven. | Moderately autonomous. | Highly autonomous. |
| Learning | Relies on pre-training. | Uses fine-tuning for precision. | Static pre-trained knowledge. | Incorporates user feedback. | Adapts using real-time data. |
| Use Cases | General applications. | Domain-specific enhancements. | Q&A, summaries, guidance. | Chatbots, automation, workflow. | Complex decision-making tasks. |
| Complexity | Provides baseline complexity. | Adds refined capabilities. | Simple integration. | More sophisticated. | Highly complex. |
| Reliability | Depends on static training data. | Improves consistency with updates. | Consistent for known queries. | May vary with dynamic inputs. | Reliability boosted by adaptive methods. |
| Scalability | Scales with model size. | Scales with domain-specific tuning. | Easily scalable for static tasks. | Scales moderately with added features. | Scalable for complex systems (with extra resources). |

#### 1. LangChain: LangChain [131] is a robust framework

designed to simplify the development of autonomous AI agents by seamlessly integrating large language models with a diverse array of tools and data sources. In LangChain, agents combine prepackaged components, such as conversational large language models (LLMs), search engine integrations, and specialized utility functions, into coherent workflows that enable multi-step reasoning and decision-making. Developers can build custom agents by defining specific roles, tasks, and tools, allowing the agent to analyze a given prompt, select the appropriate tool for each subtask, and iteratively refine its response until a final answer is produced. Fig. 6 illustrates the architecture of a LangChain-powered scheduling agent that processes email requests to perform calendar-related operations [151]. Incoming emails are first parsed to extract relevant content and convert unstructured text into structured data. This data is then passed to the chat model, guided by a contextual prompt that defines the assistant’s role. The agent uses a scratchpad to reason through the request and


*Figure 4: What are Agentic Workflows?*

determine the appropriate tool from a predefined set (such as checkAvailability, initiateBooking, or modifyBooking). These tools interact with the backend booking API to execute the requested actions, enabling seamless AI-driven scheduling.

#### 2. LlamaIndex: The LlamaIndex framework [132] provides

a powerful and flexible platform for building autonomous AI agents by seamlessly integrating large language models with external tools. In this framework, a basic AI agent is defined as a semi-autonomous software component that receives a task and a set of tools ranging from simple Python functions to complete query engines and iteratively selects the appropriate tool to process each step of the task. To build such an agent, developers first set up a clean Python environment and install LlamaIndex along with necessary dependencies, then configure an LLM (for example, GPT-4 via an API key). Next, they wrap simple functions (such as addition and multiplication) into FunctionTool objects that the agent can call, and instantiate a ReActAgent with these tools. When prompted with a task, the agent evaluates its reasoning process, chooses a tool to execute the necessary operations, and loops through these steps until the final answer is generated. This structured yet dynamic approach allows for the creation of customizable, agentic workflows capable of tackling complex tasks.

#### 3. CrewAI: CrewAI [133] is a framework designed to

orchestrate autonomous teams of AI agents, each with spe-cialized roles, tools, and objectives, to collaboratively tackle

*Figure 5: Agent-Driven RAG Framework*

complex tasks. The system is organized around four key components: the Crew, which oversees the overall operation and workflow; AI Agents, which serve as specialized team members such as researchers, writers, and analysts that make autonomous decisions and delegate tasks; the Process, which manages collaboration patterns and task assignments to ensure efficient execution; and Tasks, which are individual assign-ments with clear objectives that contribute to a larger goal. Key features of CrewAI include role-based agent specializa-tion, flexible integration of custom tools and APIs, intelligent collaboration that mimics natural human interaction, and ro-bust task management supporting both sequential and parallel workflows. Together, these elements enable the creation of dynamic, production-ready AI teams capable of achieving sophisticated, multi-step objectives in real-world applications.

Email Parser Email A Email B You are a bleeding-edge scheduling assistant that interfaces via email...etc. -.... -... Convert unstructured email content into structured data for easier processing and automation. Chat Model Can you book a meeting with ferrag.mohamedamine@univ-guelma.dz sometime tomorrow? Tools \- initiateBooking \- removeBooking \- checkAvailability \- retrieveBookings \- dispatchBookingLink \- modifyBooking Tool checkAvailability API for Bookings Agent Scratchpad Prompting

*Figure 6: Agent architecture using Langchain framework*


#### 4. Swarm: Swarm [134] is a lightweight, experimental

library from OpenAI designed to build and manage multi-agent systems without relying on the Assistants API. Swarm provides a stateless abstraction that orchestrates a continu-ous loop of agent interactions, function calls, and dynamic handoffs, offering fine-grained control and transparency. Key features include: • Agent Definition: Developers can define multiple agents, each equipped with its own set of instructions, designated role (e.g., ”Sales Agent”), and available functions, which are converted into standardized JSON structures. • Dynamic Handoffs: Agents can transfer control to one an-other based on the conversation flow or specific function criteria, simply by returning the next agent to call. • Context Management: Context variables are used to ini-tialize and update state throughout the conversation, en- suring continuity and effective information sharing across agents. • Client Orchestration: The Client.run() function initiates and manages the multi-agent dialogue by taking an initial agent, user messages, and context, and then returning updated messages, context variables, and the last active agent. • Direct Function Calling & Streaming: Swarm supports direct Python function calls within agents and provides streaming responses for real-time interactions. • Flexibility: The framework is designed to be agnostic to the underlying OpenAI client, working seamlessly with tools such as Hugging Face TGI or vLLM hosted models.

#### 5. GUI Agent: Hu et al. [135] introduced Claude 3.5

Computer Use, marking a significant milestone as the first frontier AI model to offer computer control via a graphical user interface in a public beta setting. The study assembles a diverse set of tasks, ranging from web search and productivity workflows to gaming and file management, to rigorously evaluate the model’s ability to translate natural language instructions and screenshots into precise desktop actions, such as cursor movements, clicks, and keystrokes. The evaluation framework not only demonstrates Claude 3.5’s unprecedented end-to-end performance, with a success rate of 16 out of 20 test cases, but also highlights critical areas for future refinement, including improved planning, action execution, and self-critique capabilities. Moreover, the performance is shown to be influenced by factors like screen resolution, and the study reveals that while the model can perform a wide range of operations, it still struggles with replicating subtle human-like behaviors such as natural scrolling and browsing. Overall, this preliminary exploration underscores the potential of LLMs to control computers via GUI, while also identifying the need for more comprehensive, multimodal datasets to capture real-world complexities. The paper by Sun et al. [152] tackles a major challenge in training GUI agents powered by Vision-Language Models (VLMs): collecting high-quality trajectory data. Traditional methods relying on human supervision or synthetic data generation via pre-defined tasks are either resource-intensive or fail to capture the complexity and diversity of real-world environments. The authors propose OS-Genesis, a novel data synthesis pipeline that reverses the conventional trajectory collection process to overcome these limitations. Rather than starting with fixed tasks, OS-Genesis enables agents to explore environments through step-by-step interactions and then derive high-quality tasks retrospectively, with a trajectory reward model ensuring data quality.

#### 6. Agentic Reasoning: Wu et al. [136] presents a novel

framework that significantly enhances the reasoning capa-bilities of large language models by integrating external tool-using agents into the inference process. The approach leverages three key agents: a web-search agent for real-time retrieval of pertinent information, a coding agent for executing computational tasks, and a Mind Map agent that constructs structured knowledge graphs to track and organize logical relationships during reasoning. By dynamically engaging these specialized agents, the framework enables LLMs to perform multi-step, expert-level problem solving and deep research, addressing limitations in conventional internal reasoning ap-proaches. Evaluations on challenging benchmarks such as the GPQA dataset and domain-specific deep research tasks demonstrate that Agentic Reasoning substantially outperforms traditional retrieval-augmented generation systems and closed-source models, highlighting its potential for improved knowl- edge synthesis, test-time scalability, and structured problem-solving. OctoTools [137] is a robust, training-free, and user-friendly framework designed to empower large language models to tackle complex reasoning tasks across diverse domains. By integrating standardized tool cards that encapsulate various tool functionalities, a planner for orchestrating both high-level and low-level strategies, and an executor for effective tool us-age, OctoTools overcomes the limitations of prior methods that were confined to specialized domains or required extra training data. Validated across 16 varied tasks including MathVista, MMLU-Pro, MedQA, and GAIA-Text OctoTools achieves an

average accuracy improvement of 9.3% over GPT-4o and outperforms frameworks like AutoGen, GPT-Functions, and LangChain by up to 10.6% when using the same toolset. Comprehensive analysis and ablation studies demonstrate its advantages in task planning, effective tool integration, and multi-step problem solving, positioning it as a significant advancement for general-purpose, complex reasoning appli-cations.

#### 7. Agents SDK: The OpenAI Agents SDK [138] provides a

comprehensive framework for building autonomous, multi-step agent applications that harness the power of large language models alongside external tools. This SDK abstracts the core components necessary for agentic workflows, including agents themselves which are LLMs configured with instructions, tools, handoffs, and guardrails as well as the tools that enable these agents to perform external actions (such as API calls or computations). It also supports context management to maintain state over multi-turn interactions, structured output types for reliable data exchange, and advanced features like streaming, tracing, and guardrails to ensure safety and debuga-bility.

### B. AI Agent applications

AI Agents are autonomous systems that combine large language models (LLMs), data retrieval mechanisms, and decision-making pipelines to tackle a wide array of tasks across industries. In healthcare, they assist with clinical di-agnosis and personalized treatment planning; in finance, they support forecasting and risk analysis; in scientific research, they automate literature review and experimental design; and in software engineering, they generate, analyze, and repair code. Using domain-specific fine-tuning and structured data sources, AI agents can also drive the generation of syn-thetic data, facilitate chemical reasoning, support mathematical problem-solving, and enable creative multimedia production, thereby expanding the reach of AI-powered automation and insight generation. Fig. 7 presents both the architectural back-bone and the application landscape of AI Agents.

#### 1. Healthcare Applications: The healthcare sector has wit-nessed significant advancements through the integration of
large language model-based agents across a wide range of applications. In this subsection, we present recent develop-ments organized into key categories, as presented in Fig. 8, in- cluding clinical diagnosis and decision support, mental health and therapy agents, general medical assistants for workflow optimization, and pharmaceutical and drug discovery agents. These works demonstrate how AI agents are increasingly sup-porting medical professionals, enhancing diagnostic accuracy, improving patient care, and accelerating research in diverse healthcare domains. Tab. reviews AI agent applications for Healthcare.

##### a. Clinical Diagnosis, Imaging & Decision Support

Chen et al. [153] introduce Chain-of-Diagnosis (CoD), a novel approach designed to enhance the interpretability of LLM-based medical diagnostics. By transforming the diagnostic process into a transparent, step-by-step chain that mirrors a physician’s reasoning, CoD provides a clear reasoning path-way alongside a disease confidence distribution, which aids in identifying critical symptoms through entropy reduction. This transparent methodology not only makes the diagnostic process controllable but also boosts rigor in decision-making. Leveraging CoD, the authors developed DiagnosisGPT, an advanced system capable of diagnosing 9,604 diseases. Exper-imental results demonstrate that DiagnosisGPT outperforms existing large language models (LLMs) on diagnostic bench-marks, achieving both high diagnostic accuracy and enhanced interpretability. Zhou et al. [154] present ZODIAC, an innovative LLM-powered framework that elevates cardiological diagnostics to a level of professionalism comparable to that of expert cardiologists. Designed to address the limitations of general-purpose large language models (LLMs) in clinical settings, ZODIAC leverages a multi-agent collaboration architecture to process patient data across multiple modalities. Each agent is fine-tuned using real-world patient data adjudicated by cardiologists, ensuring the system’s diagnostic outputs, such as the extraction of clinically relevant characteristics, arrhythmia detection, and preliminary report generation, are accurate and reliable. Rigorous clinical validation, conducted by in-dependent cardiologists and evaluated across eight metrics addressing clinical effectiveness and security, demonstrates that ZODIAC outperforms industry-leading models, including GPT-4o, Llama-3.1-405B, Gemini-pro, and even specialized medical LLMs like BioGPT. Notably, the successful inte-gration of ZODIAC into electrocardiography (ECG) devices underscores its potential to transform healthcare delivery, exemplifying the emerging trend of embedding LLMs within Software-as-Medical-Device (SaMD) solutions. Wang et al. [155] introduce MedAgent-Pro, an evidence-based, agentic system designed to enhance multi-modal med- ical diagnosis by addressing key limitations of current Multi-modal Large Language Models (MLLMs). While MLLMs have demonstrated strong reasoning and task-performing capa-bilities, they often struggle with detailed visual perception and exhibit reasoning inconsistencies, both of which are critical in clinical settings. MedAgent-Pro employs a hierarchical work-flow: at the task level, it leverages knowledge-based reasoning to generate reliable diagnostic plans grounded in retrieved clinical criteria, and at the case level, it utilizes multiple tool agents to process multi-modal inputs and analyze diverse indicators. The final diagnosis is derived from a synthesis of quantitative and qualitative evidence. Comprehensive experi-ments on both 2D and 3D medical diagnosis tasks demonstrate that MedAgent-Pro not only outperforms existing methods but also offers enhanced reliability and interpretability, marking a significant step forward in AI-assisted clinical diagnostics. Feng et al. [157] introduce M3Builder. This novel multi-agent system automates machine learning workflows in the medical imaging domain, a field that has traditionally needed specialized models and tools. M3Builder is structured around four specialized agents that collaboratively manage complex, multi-step ML tasks, including automated data processing, environment configuration, self-contained auto-debugging, and model training, all within a dedicated medical imaging ML workspace. To assess progress in this area, the authors propose M3Bench, a comprehensive benchmark featuring four general


**Table 7: Overview of AI Agent Applications for Healthcare**


| Application | Year | Category | Core Objective & Details |
|---|---|---|---|
| DiagnosisGPT [153] | 2024 | Medical Diagnos-tics | Enhance interpretability via a transparent, step-by-step chain. Implements CoD to yield confidence scores and entropy reduction. Diagnoses 9,604 diseases; outperforms existing LLMs. |
| ZODIAC [154] | 2024 | CardiologyDeliver expert-level | cardiological diagnostics. Multi-agent LLM fine-tuned on adjudicated patient data. Outperforms leading models; integrated into ECG devices. MedAgent- |
| MedAgent- Pro [155] | 2025 | Medical Diagnosis | Enhance multi-modal diagnosis by addressing visual and reasoning gaps. Hierarchical workflow with knowledge-based reasoning and multi-modal agents. Outperforms existing methods on 2D/3D tasks with improved reliability. Steenstra et |
| Steenstra et al. [156] | 2025 | Therapeutic Counsel-ing | Improve counseling training with continuous, detailed feedback. LLM-powered simulated patients with turn-by-turn visualizations. High usability and satisfaction; enhances learning vs. traditional methods. |
| M3Builder [157] | 2025 | Medical Imaging ML | Automate ML workflows in medical imaging. Four agents manage data processing, configuration, debugging, and training. Achieves 94.29% success with state-of-the-art LLM cores. |
| MEDDxAgent [158] | 2025 | Differential Diagnosis | Enable iterative, interactive differential diagnosis. Integrates a DDxDriver, history simulator, and specialized retrieval/diagnosis agents. Boosts diagnostic accuracy by over 10% with enhanced explainability. |
| PathFinder [159] | 2025 | AI-assisted Diagnos-tics | Replicate holistic WSI analysis as done by expert pathologists. Four agents collaboratively generate importance maps and diagnoses. Outperforms state-of-the-art by 8%, exceeding average pathologist performance by 9%. |
| HamRaz [160] | 2025 | Therapeutic Counsel-ing | Provide the first Persian PCT dataset for LLMs with culturally adapted therapy sessions. Combines scripted dialogues and adaptive LLM role-play. Produces more empathetic, nuanced, and realistic counseling interactions. |
| CAMI [161] | 2025 | Therapeutic Counsel-ing | Automate MI-based counseling with client state inference, topic exploration, and empathetic response generation. STAR framework with three LLM modules for state, topic, and response. Outperforms baselines in MI competency and counseling realism. |
| AutoCBT [162] | 2025 | Therapeutic Counsel-ing | Deliver dynamic CBT via multi-agent routing and supervision. Uses single-turn agents and dynamic supervisory routing for tailored interventions. Generates higher-quality CBT responses vs. fixed systems. |
| PSYCHE [163] | 2025 | Psychiatric Assess-ment | Benchmark PACAs with simulated patient profiles and multi-turn interactions. Uses detailed psychiatric constructs and board-certified psychiatrist evaluations. Validated for clinical appropriateness and safety. |
| PsyDraw [164] | 2024 | Mental Health Screening | Analyze HTP drawings with multimodal agents for early screening of LBCs. Two-stage feature extraction and report generation; evaluated on 290 submissions; pilot deployment in schools. 71.03% high consistency with experts; scalable screening tool. |
| EvoPatient [165] | 2024 | Medical Training | Simulate patient–doctor dialogues for training via unsupervised LLM agents. Iterative multi-turn consultations refine patient responses and physician questions over 200 case simulations. Improves requirement alignment by >10% and achieves higher human preference. |
| Scripted Therapy Agents [166] | 2024 | Therapeutic Counsel-ing | Constrain LLM responses via expert-written scripts and finite conversational states. Two prompting variants execute 100 simulated sessions following deterministic therapeutic scripts. Demonstrates reliable script adherence and transparent decision paths. |
| LIDDiA [167] | 2025 | Drug Discov-ery | Automate end-to-end drug discovery from target selection to lead optimization. Orchestrates LLM-driven reasoning across all pipeline steps; evaluated on 30 targets. Generates valid candidates >70% of cases; identifies novel EGFR inhibitors. |
| PatentAgent [168] | 2024 | Pharmaceutical Patents | Streamline patent analysis with LLM-driven QA, image-to-molecule, and scaffold ID. PA-QA, PA-Img2Mol, PA-CoreId modules for comprehensive patent insights. Improves image-to-molecule accuracy by up to 8.37% and scaffold ID by up to 7.62%. |
| DrugAgent [169] | 2024 | Drug Re-purposing | Accelerate drug repurposing via multi-agent ML and knowledge integration. Combines DTI modeling, KG extraction, and literature mining agents. Improves prediction accuracy and reduces discovery time/cost. |
| MAP [170] | 2025 | Inpatient Decision Support | Support complex inpatient pathways with specialized triage, diagnosis, and treatment agents. Uses IPDS benchmark; coordinated by a chief agent for end-to-end care planning. +25.10% diagnostic accuracy vs. HuatuoGPT2-13B; +10–12% clinical compliance over clinicians. |
| SynthUserEval [171] | 2025 | Health Coaching | Generate synthetic users for evaluating behavior-change agents. Creates structured profiles and simulates interactions with coaching agents. Enables realistic, health-grounded dialogues; validated by expert evaluations. C: Clinical Validation; W: Workflow Integration; R: Regulatory Compliance;: Partial;: Not Supported;: Supported. Users AI Agent Action Vector Database Software Engineering Finance Applications Solving mathematical problems Synthetic data generation Chemical Reasoning Geography Applications LLM model Sub - AI Agent applications Agentic AI Customized LLM model Healthcare Applications Materials ScienceBiomedical Science Research Applications Multimedia Applications AI Agent applications Mental Health, Counseling & Therapy Agents Pharmaceutical & Drug-Related Agents Agents for Astronomical Observations Gene Set Knowledge Discovery Biomedical AI Scientist Agents Mathematical Reasoning and Problem Solving ....... Database *Figure 7: Architecture and Application Domains of AI Agents* tasks across 14 training datasets, covering five anatomies, three imaging modalities, and both 2D and 3D data. Evaluations using seven state-of-the-art large language models as agent cores, such as the Claude series, GPT-4o, and DeepSeek-V3, demonstrate that M3Builder significantly outperforms existing ML agent designs, achieving a remarkable 94.29% success rate with Claude-3.7-Sonnet. Rose et al. [158] tackles the complexities of differential diagnosis (DDx) by introducing the Modular Explainable DDx Agent (MEDDxAgent) framework, which facilitates interac-tive, iterative diagnostic reasoning rather than relying on com- plete patient profiles from the outset. Addressing limitations in previous approaches such as evaluations on single datasets, isolated component optimization, and single-attempt diag-noses MEDDxAgent integrates three modular components: an orchestrator (DDxDriver), a history-taking simulator, and two specialized agents for knowledge retrieval and diagnosis strategy. To ensure robust evaluation, the authors also present a comprehensive DDx benchmark covering respiratory, skin, and rare diseases. Their findings reveal that iterative refinement significantly enhances diagnostic accuracy, with MEDDxA-gent achieving over a 10% improvement across both large and small LLMs while providing critical explainability in its reasoning process. Ghezloo et al. [159] introduce Pathfinder, a novel multi-modal, multi-agent framework designed to replicate the holis- tic diagnostic process of expert pathologists when analyz-ing whole-slide images (WSIs). Recognizing that WSIs are characterized by their gigapixel scale and complex structure, PathFinder employs four specialized agents a Triage Agent, Navigation Agent, Description Agent, and Diagnosis Agent that collaboratively navigate and interpret the image data. The Triage Agent first determines whether a slide is benign or risky; if deemed risky, the Navigation and Description Agents iteratively focus on and characterize significant re-gions, generating importance maps and detailed natural lan- guage descriptions. Finally, the Diagnosis Agent synthesizes these findings to provide a comprehensive diagnostic classi-fication that is inherently explainable. Experimental results indicate that PathFinder outperforms state-of-the-art methods in skin melanoma diagnosis by 8% and, notably, surpasses the average performance of pathologists by 9%, establishing a new benchmark for accurate, efficient, and interpretable AI-assisted diagnostics in pathology. |

##### b. Mental Health, Counseling & Therapy Agents

Wasenm ̈ uller et al. [166] present a script-based dialog policy planning paradigm that enables LLM-powered conversational agents to function as AI therapists by adhering to expert-written therapeutic scripts and transitioning through a finite set of conversational states. By treating the script as a deter-ministic guide, the approach constrains the model’s responses to align with a defined therapeutic framework, making decision paths transparent for clinical evaluation and risk management. The authors implement two variants of this paradigm, utilizing

different prompting strategies, and generate 100 simulated therapy sessions with LLM-driven patient agents. Experimen-tal results demonstrate that both implementations can reliably follow the scripted policy, providing insights into their relative efficiency and effectiveness, and underscoring the feasibility of building inspectable, rule-aligned AI therapy systems. Du et al. [165] introduce EvoPatient, a framework for gen-erating simulated patients using large language models to train medical personnel through multi-turn diagnostic dialogues. Existing approaches focus on data retrieval accuracy or prompt tuning, but EvoPatient emphasizes unsupervised simulation to teach patient agents standardized presentation patterns. In this system, a patient agent and doctor agents engage in iterative consultations, with each dialogue cycle serving to both train the agents and gather experience that refines patient responses and physician questions. Extensive experiments across di-verse clinical scenarios show that EvoPatient improves re- quirement alignment by more than 10 percent compared to state-of-the-art methods and achieves higher human preference ratings. After evolving through 200 case simulations over ten hours, the framework achieves an optimal balance between resource efficiency and performance, demonstrating strong generalizability for scalable medical training. Zhang et al. [164] present PsyDraw, a multimodal LLM-driven multi-agent system designed to support mental health professionals in analyzing House-Tree-Person (HTP) drawings for early screening of left-behind children (LBCs) in rural China. Recognizing the acute shortage of clinicians, PsyDraw employs specialized agents for detailed feature extraction and psychological interpretation in two stages: comprehensive analysis of drawing elements and automated generation of professional reports. Evaluated on 290 primary-school HTP submissions, PsyDraw achieved High Consistency with expert evaluations in 71.03% of cases and Moderate Consistency in 26.21%, flagging 31.03% of children as needing further attention. Deployed in pilot schools, PsyDraw demonstrates strong potential as a scalable, preliminary screening tool that maintains high professional standards and addresses critical mental health gaps in resource-limited settings. Lee et al. [163] introduce PSYCHE, a comprehensive frame-work for benchmarking psychiatric assessment conversational agents (PACAs) built on large language models. Recognizing that psychiatric evaluations rely on nuanced, multi-turn inter-actions between clinicians and patients, PSYCHE simulates patients using a detailed psychiatric construct that specifies their profiles, histories, and behavioral patterns. This approach enables clinically relevant assessments, ensures ethical safety checks, facilitates cost-efficient deployment, and provides quantitative evaluation metrics. The framework was validated in a study involving ten board-certified psychiatrists who reviewed and rated the simulated interactions, demonstrating PSYCHE’s ability to evaluate PACAs’ clinical appropriateness and safety rigorously. Xu et al. [162] addresses the limitations of existing LLM-based Cognitive Behavioral Therapy (CBT) systems, namely their rigid agent structures and tendency toward redundant, un-helpful suggestions, by proposing AutoCBT, a dynamic multi- agent framework for automated psychological counseling. Ini-tially, the authors develop a general single-turn consultation agent using Quora-like and YiXinLi models, evaluated on a bilingual dataset to benchmark response quality in single-round interactions. Building on these insights, they introduce dynamic routing and supervisory mechanisms modeled af-ter real-world counseling practices, enabling agents to self- optimize and tailor interventions more effectively. Experimen-tal results demonstrate that AutoCBT generates higher-quality CBT-oriented responses compared to fixed-structure systems, highlighting its potential to deliver scalable, empathetic, and contextually appropriate psychological support for users who might otherwise avoid in-person therapy. Yang et al. [161] present CAMI, an automated conversa-tional counselor agent grounded in Motivational Interviewing (MI), a client-centered approach designed to resolve ambiva-lence and promote behavior change. CAMI’s novel STAR framework integrates three LLM-powered modules client State inference, motivation Topic exploration, and response gEner-ation to evoke “change talk” in line with MI principles. By accurately inferring a client’s emotional and motivational state, exploring relevant topics, and generating empathetic, directive responses, CAMI facilitates more effective counseling across diverse populations. The authors evaluate CAMI using both automated metrics and manual assessments with simulated clients, measuring MI skill competency, state inference ac-curacy, topic exploration proficiency, and overall counseling success. Results demonstrate that CAMI outperforms existing methods and exhibits counselor-like realism, while ablation studies highlight the essential contributions of the state in-ference and topic exploration modules to its superior perfor- mance. Steenstra et al. [156] address the challenges in therapeutic counseling training, confined mainly to an innovative LLM-powered system that provides continuous, detailed feedback during simulated patient interactions. Focusing on motivational interviewing a counseling approach emphasizing empathy and collaborative behavior change the framework features a sim-ulated patient and visualizations of turn-by-turn performance to guide counselors through role-play scenarios. The system was evaluated with both professional and student counselors, who reported high usability and satisfaction, indicating that frequent and granular feedback can significantly enhance the learning process compared to traditional, intermittent methods. Abbasi et al. [160] introduce HamRaz, the first Persian-language dataset tailored for Person-Centered Therapy (PCT) with large language models (LLMs), addressing a critical gap in culturally and linguistically appropriate mental health resources. Recognizing that existing counseling datasets are largely confined to Western and East Asian contexts, the authors design HamRaz by blending scripted therapeutic dia-logues with adaptive LLM-driven role-playing to foster coher- ent, dynamic therapy sessions in Persian. To rigorously assess performance, they propose HamRazEval, a dual evaluation framework combining general dialogue quality metrics with the Barrett–Lennard Relationship Inventory (BLRI) to measure therapeutic rapport and effectiveness. Experimental compar-isons demonstrate that LLMs trained on HamRaz generate more empathetic, contextually nuanced, and realistic counsel-ing interactions than conventional Script Mode or Two-Agent Mode approaches.

##### c. General Medical Assistants, Clinical Workflow & De-cision Making: Yun et al. [171] introduce an end-to-end
framework for generating synthetic users to evaluate inter-active agents aimed at promoting positive behavior change, focusing on sleep and diabetes management. The framework first generates structured data based on real-world health and lifestyle factors, demographics, and behavioral attributes. Next, it creates complete user profiles conditioned on this structured data. Interactions between synthetic users and health coaching agents are simulated using generative agent models such as Concordia or by directly prompting a language model. Case studies with sleep and diabetes coaching agents demonstrate that the synthetic users enable realistic dialogue by accurately reflecting users’ needs and challenges. Blinded evaluations by human experts confirm that these health-grounded synthetic users portray real human users more faithfully than generic synthetic users. This approach provides a scalable and realistic testing ground for developing and refining conversational agents in health and lifestyle coaching. Chen et al. [170] address the complexity of clinical decision-making in inpatient pathways by introducing both a new benchmark and a multi-agent AI framework. The authors con-struct the Inpatient Pathway Decision Support (IPDS) bench- mark from the MIMIC-IV database, comprising 51,274 cases across nine triage departments, 17 disease categories, and 16 standardized treatment options to capture the multifaceted na-ture of inpatient care. Building on this resource, they propose the Multi-Agent Inpatient Pathways (MAP) framework, which employs a triage agent for patient admission, a diagnosis agent for department-level decision-making, and a treatment agent for care planning, all coordinated by a chief agent that oversees the entire pathway. In extensive experiments, MAP achieves a 25.10% improvement in diagnostic accuracy over the state-of-the-art LLM HuatuoGPT2-13B and surpasses three board- certified clinicians in clinical compliance by 10–12%. These results demonstrate the potential of multi-agent systems to support complex inpatient workflows and lay the groundwork for future AI-driven decision support in hospital settings.

##### d. Pharmaceutical & Drug-Related Agents: Wang et al

[168] introduce PatentAgent, the first end-to-end intelligent agent designed to streamline pharmaceutical patent analysis by leveraging large language models. PatentAgent integrates three core modules: PA-QA for patent question answering, PA-Img2Mol for converting chemical structure images into molecular representations, and PA-CoreId for identifying core chemical scaffolds. PA-Img2Mol achieves accuracy gains of 2.46 to 8.37 percent across CLEF, JPO, UOB, and USPTO patent image benchmarks, while PA-CoreId delivers improve-ments of 7.15 to 7.62 percent on the PatentNetML scaffold identification task. By combining these modules within a unified framework, PatentAgent addresses the full spectrum of patent analysis needs, from extracting detailed experimental insights to pinpointing key molecular structures, and offers a powerful tool to accelerate research and innovation in drug discovery. Averly et al. [167] introduce LIDDiA, an autonomous in Healthcare Applications Clinical Diagnosis, Imaging & Decision Support CoD [153] ZODIAC [154] MedAgent-Pro [155] M3Builder [157] MEDDxAgent [158] PathFinder [159] Mental Health, Counseling & Therapy Agents Script Planning [166] EvoPatient [165] PsyDraw [164] PSYCHE [163] AutoCBT [162] CAMI [161] Scaffolding [156] HamRaz [160] General Medical Assistants, Clinical Workflow & Decision Making Synthetic Users [171] MAP Framework [170] Pharmaceutical & Drug-Related Agents PatentAgent [168] LIDDiA [167] Drug Repurposing [169]

*Figure 8: Agent LLM Applications for Healthcare*

silico agent designed to navigate the entire drug discovery pipeline by leveraging the reasoning capabilities of large language models. Unlike prior AI tools that address individual steps such as molecule generation or property prediction, LIDDiA orchestrates the end-to-end process from target selec-tion through lead optimization. The authors evaluate LIDDiA on 30 clinically relevant targets and show that it generates candidate molecules satisfying key pharmaceutical criteria in over 70 percent of cases. Furthermore, LIDDiA demonstrates an intelligent balance between exploring novel chemical space and exploiting known scaffolds and successfully identifies promising new inhibitors for the epidermal growth factor receptor (EGFR), a major oncology target. Inoue et al. [169] present a multi-agent framework designed to accelerate drug repurposing by combining machine learning and knowledge integration. The system includes three spe-cialized agents: an AI Agent that trains robust drug–target interaction (DTI) models, a Knowledge Graph Agent that extracts DTIs from databases such as DGIdb, DrugBank, CTD and STITCH, and a Search Agent that mines biomedical literature to validate computational predictions. By integrating outputs from these agents, the framework leverages diverse data sources to identify promising candidates for repurposing. Preliminary evaluations indicate that this approach not only enhances the accuracy of drug–disease interaction predictions compared to existing methods but also reduces the time and cost associated with traditional drug discovery. The in-terpretable results and scalable architecture demonstrate the potential of multi-agent systems to drive innovation and effi-ciency in biomedical research.

#### 2. Materials Science: Materials science has recently ben-efited from the integration of LLM-based agents, which are
helping to automate complex scientific workflows and enhance

research efficiency. In this subsection, we highlight two no-table developments, including the application of AI agents in astronomical observations to streamline data collection and analysis, and the creation of specialized agent systems tailored to address the unique challenges of materials science research.

##### a. LLM-Based Agents for Astronomical Observations

The StarWhisper Telescope System [139] leverages LLM-based agents to streamline the complex workflow of astro- nomical observations within the Nearby Galaxy Supernovae Survey (NGSS) project. This innovative system automates crit-ical tasks including generating customized observation lists, initiating telescope observations, real-time image analysis, and formulating follow-up proposals to reduce the operational burden on astronomers and lower training costs. By integrating these agents into the observation process, the system can effi-ciently verify and dispatch observation lists, analyze transient phenomena in near real-time, and seamlessly communicate results to observatory teams for subsequent scheduling.

##### b. Materials Science Research: HoneyComb [140] is

introduced as the first LLM-based agent system tailored ex-plicitly for materials science, addressing the unique challenges posed by complex computational tasks and outdated implicit knowledge that often lead to inaccuracies and hallucinations in general-purpose LLMs. The system leverages a novel, high-quality materials science knowledge base (MatSciKB) curated from reliable literature and a sophisticated tool hub (Tool- Hub) that employs an Inductive Tool Construction method to generate, decompose, and refine specialized API tools. Additionally, the retriever module adaptively selects the most relevant knowledge sources and tools for each task, ensuring high accuracy and contextual relevance.

#### 3. Biomedical Science: The biomedical field has seen

important progress through the development of LLM-based agents designed to support knowledge discovery, enhance reasoning capabilities, and evaluate scientific literature. In this subsection, we review recent contributions that focus on gene set analysis, iterative learning for improved reasoning, and the evaluation of AI scientist agents through specialized biomedical benchmarks.

##### a. Gene Set Knowledge Discovery: Gene set knowl-edge discovery is crucial for advancing human functional
genomics, yet traditional LLM approaches often suffer from issues like hallucinations. To address this, Wang et al. [141] introduce GeneAgent a pioneering language agent with self-verification capabilities that autonomously interacts with bio- logical databases and leverages specialized domain knowledge to enhance accuracy. Benchmarking on 1,106 gene sets from diverse sources, GeneAgent consistently outperforms standard GPT-4, and a detailed manual review confirms that its self-verification module effectively minimizes hallucinations and produces more reliable analytical narratives. Moreover, when applied to seven novel gene sets derived from mouse B2905 melanoma cell lines, expert evaluations reveal that GeneAgent offers novel insights into gene functions, significantly ex-pediting the process of knowledge discovery in functional genomics.

##### b. Reasoning with Recursive Learning: Buehler et al

[142] proposed a framework, named PRefLexOR, that fuses preference optimization with reinforcement learning concepts to enable language models to self-improve through iterative, multi-step reasoning. The approach employs a recursive learn-ing strategy in which the model repeatedly revisits and refines intermediate reasoning steps before producing a final output, both during training and inference. Initially, the model aligns its reasoning with accurate decision paths by optimizing the log odds between preferred and non-preferred responses while constructing a dynamic knowledge graph through question generation and retrieval augmentation. In a subsequent stage, rejection sampling is employed to refine the reasoning quality by generating in-situ training data and masking intermediate steps, all within a thinking token framework that fosters iterative feedback loops.

##### c. Biomedical AI Scientist Agents: Lin et al. [172] intro-duce BioKGBench, a novel benchmark designed to evaluate
biomedical AI scientist agents from the perspective of litera-ture understanding. Unlike traditional evaluation methods that rely solely on direct QA or biomedical experiments, BioKG- Bench decomposes the critical ability of “understanding liter-ature” into two atomic tasks: one that verifies scientific claims in unstructured text from research papers and another that in-volves interacting with structured knowledge-graph question- answering (KGQA) for literature grounding. Building on these components, the authors propose a new agent task called KGCheck, which uses domain-based retrieval-augmented gen-eration to identify factual errors in large-scale knowledge graph databases. With a dataset of over 2,000 examples for the atomic tasks and 225 high-quality annotated samples for the agent task, the study reveals that state-of-the-art agents both in everyday and biomedical settings perform poorly or suboptimally on this benchmark.

#### 4. Research Applications: LLM-based agents are increas-ingly being developed to support and automate various aspects
of the scientific research process. This subsection presents a selection of recent applications, including collaborative re-search environments, automated survey generation, structured literature analysis for ideation, workflow management in data science, and AI-driven hypothesis generation.

##### a. Collaborative Research Among LLM Agents

Schmidgall and Moor [173] introduces AgentRxiv, a frame-work designed to enable collaborative research among au- tonomous LLM agent laboratories by leveraging a shared preprint server. Recognizing that scientific discovery is inher-ently incremental and collaborative, AgentRxiv allows agents to upload and retrieve research reports, thereby sharing in-sights and building upon previous work in an iterative manner. The study demonstrates that agents with access to prior research achieve a significant performance boost an 11.4% relative improvement on the MATH-500 dataset compared to those operating in isolation. Furthermore, the best-performing collaborative strategy generalizes to other domains with an average improvement of 3.3%, and when multiple agent lab-oratories share their findings, overall accuracy increases by 13.7% relative to the baseline. These findings highlight the potential of autonomous agents to collaborate with humans, paving the way for more efficient and accelerated scientific discovery.


**Table 8: Overview of AI Agent Applications for Research**


| Agent / Tool | Year | Use Case | Primary Aim & Details |
|---|---|---|---|
| AgentRxiv [173] | 2025 | Collaborative Research | Share and build upon preprints across autonomous LLM labs. Upload/retrieve via shared preprint server with iterative updates. +11.4% on MATH-500; +3.3% cross-domain; +13.7% multi-lab. MATH-500 benchmark AgentRxiv server Preprint sharing |
| SurveyX [143] | 2025 | Survey Generation | Automate systematic literature surveys with high quality. Preparation (retrieval \+ AttributeTree) + Generation (repolishing). +0.259 content quality; +1.76 citation precision vs. baselines. Content & citation scoring Bibliographic APIs Structured citations |
| CoI Agent [144] | 2024 | Research Ideation | Structure literature into progressive idea chains. Sequential Chain-of-Ideas + Idea Arena evaluation protocol. Expert-comparable idea quality at $0.50 per idea. Idea ArenaCoI framework Cost-efficient ideation |
| Data Interpreter [174] | 2024 | Data Science Workflows | Manage end-to-end, dynamic DS pipelines robustly. Hierarchical Graph Modeling + Programmable Node Generation. +25% on InfiAgent-DABench (75.9→94.9%); ML & MATH gains. InfiAgent DABench Pipeline APIsReproducible workflows |
| AI Co-Scientist [175] | 2025 | Scientific Discovery | Generate and refine research hypotheses autonomously. Seven specialized agents with Elo tournaments and meta-review. +300 Elo hypothesis quality; +27% novelty scores. Elo & novelty scoring Multi-agent pipeline Hypothesis publication Eval. Framework: Evaluation Framework; Collab. Platform: Collaboration Platform; Open Sci.: Open Science Support. |

##### b. Automated Survey Generation: Liang et al. [143]

developed the SurveyX platform, which leverages the excep-tional comprehension and knowledge capabilities of LLMs to overcome critical limitations in automated survey gener-ation, including finite context windows, superficial content discussions, and the lack of systematic evaluation frameworks. Inspired by human writing processes, SurveyX decomposes the survey composition process into two distinct phases: Preparation and Generation. During the preparation phase, the system incorporates online reference retrieval and applies a novel preprocessing method, AttributeTree, to effectively structure the survey’s content. In the subsequent Generation phase, a repolishing process refines the output to enhance the depth and accuracy of the study generated, particularly improving content quality and citation precision. Experimental evaluations reveal that SurveyX achieves a content quality improvement of 0.259 and a citation quality enhancement of 1.76 over existing systems, bringing its performance close to that of human experts across multiple evaluation dimensions.

##### c. Structuring Literature for Research Ideation: Li et

al. [144] introduce the Chain-of-Ideas (CoI) agent, a novel LLM-based framework for automating research ideation by structuring relevant literature into a chain that mirrors the progressive development within a research domain. The CoI agent addresses the challenge posed by the exponential growth of scientific literature, which overwhelms traditional idea-generation methods that rely on simple prompts or expose models to raw, unfiltered text. By organizing information in a sequential chain, the CoI agent enables LLMs to capture cur-rent advancements more effectively, enhancing their ability to generate innovative research ideas. Complementing this frame-work is the Idea Arena, an evaluation protocol that assesses the quality of generated ideas from multiple perspectives, aligning closely with the preferences of human researchers. Experimental results indicate that the CoI agent outperforms existing methods and achieves quality comparable to human experts, all while maintaining a low cost approximately $0.50 per candidate idea and corresponding experimental design.

##### d. Managing Data Science Workflows: Hong et al. [174]

propose Data Interpreter, an LLM-based agent that tackles end-to-end data science workflows by addressing challenges in solving long-term, interconnected tasks and adapting to dynamic data environments. Unlike previous methods that focus on individual tasks, Data Interpreter leverages two key modules: Hierarchical Graph Modeling, which decomposes complex problems into manageable subproblems through dy-namic node generation and graph optimization, and Pro- grammable Node Generation, which iteratively refines and verifies each subproblem to boost the robustness of code generation. Extensive experiments demonstrate significant per-formance gains achieving up to a 25% boost on InfiAgent- DABench (increasing accuracy from 75.9% to 94.9%), as well as improvements on machine learning, open-ended tasks, and the MATH dataset highlighting its superior capability in managing evolving task dependencies and real-time data adjustments.

##### e. Automating Scientific Discovery: Google [175] intro-duced the AI co-scientist, a multi-agent system built on Google
DeepMind Gemini 2.0, designed to automate scientific dis-covery by generating and refining novel research hypotheses. The framework comprises seven specialized agents Supervisor, Generation, Reflection, Ranking, Evolution, Proximity, and Meta-review that collaboratively manage tasks ranging from parsing research goals to conducting simulated debates and organizing hypotheses. For example, the system employs a Ranking Agent that uses pairwise Elo tournaments, boosting hypothesis quality by over 300 Elo points. At the same time, the Meta-review Agent’s feedback has been shown to increase hypothesis novelty scores by 27%. In practical applications, such as drug repurposing for acute myeloid leukemia and novel target discovery for liver fibrosis, the framework demonstrates significant performance improvements, paving the way for

AI systems that can generate and iteratively refine scientific hypotheses with expert-level precision. Software Engineering Agent Pro-gramming Architectures Ann Arbor Archi-tecture [176] Postline Platform [176] Verification & Supervision Agents AgentGym [177] TRAVER & DICT [178] CURA (VPS) [179] Adaptive Control & Performance Enhance-ment DARS [180] Code Localiza-tion & Software Analytics LocAgent [181] GateLens [182] Domain-Specific SWE Agents Repo2Run [183] UXAgent [184] TRAVER & DICT [178] SWE-Gym [185] Multi-Agent Collab-oration & Simulation Multi-Agent Collab Framework [186] SyncMind [187] CodeSim [188]

*Figure 9: Agent LLM Applications in Software Engineering*


#### 5. Software Engineering: Software engineering has be-come a significant area of application for LLM-based agents,
with innovations spanning architecture design and verification systems, adaptive control, software analytics, and multi-agent collaboration. This subsection presents recent developments across a wide range of tasks, including agent programming frameworks, tutoring systems, automated environment config-uration, usability testing, and multilingual code generation. Fig. 9 presents a classification of Agent LLM Applications for Software Engineering.

##### a. Agent Programming Architectures: Dong et al. [176]

explore prompt engineering for large language models (LLMs) from the perspective of automata theory, arguing that LLMs can be viewed as automata. They assert that just as automata must be programmed using the languages they accept, LLMs should similarly be programmed within the scope of both natural and formal languages. This insight challenges tradi-tional software engineering practices, which often distinguish between programming and natural languages. The paper in-troduces the Ann Arbor Architecture, a conceptual framework designed for agent-oriented programming of language models, which serves as a higher-level abstraction to enhance in-context learning beyond basic token generation. The authors also present Postline, their agent platform, and discuss early results from experiments conducted to train agents within this framework.

##### b. Verification & Supervision Agents: The papers by Jain

et al. [177] , Wang et al.[178], and Chen et al. [179] contribute to advancing the use of large language models (LLMs) for real-world software engineering (SWE) tasks, intelligent tutoring, and code generation. Jain et al. [177] introduce AgentGym, a comprehensive environment for training SWE-agents, address-ing challenges in scalable curation of executable environments and test-time compute scaling. Their approach leverages SYN- GEN, a synthetic data curation method, and Hybrid Test-time Scaling to improve performance on the SWE-Bench Verified benchmark, achieving a state-of-the-art pass rate of 51%. Wang et al. [178] propose a novel coding tutoring framework, Trace-and-Verify (TRAVER), combining knowledge tracing and turn-by-turn verification to enhance tutor agents’ guid-ance toward task completion. Their work introduces DICT, a holistic evaluation protocol for tutoring agents, demonstrating significant improvements in coding tutoring success rates. Finally, Chen et al. present CURA, a code understanding and reasoning system augmented with verbal process supervision (VPS). CURA achieves a 3.65% improvement on benchmarks like BigCodeBench and demonstrates enhanced performance when paired with the o3-mini model. These works collectively push the boundaries of LLM applications in complex software engineering tasks, intelligent tutoring, and reasoning-driven code generation.

##### c. Adaptive Control & Performance Enhancement: Ag-garwal et al. [180] introduce Dynamic Action Re-Sampling
(DARS), a novel approach for scaling compute during infer-ence in coding agents, aimed at improving their decision- making capabilities. While existing methods often rely on linear trajectories or random sampling, DARS enhances agent performance by branching out at key decision points and selecting alternative actions based on the history of previous attempts and execution feedback. This enables coding agents to recover more effectively from sub-optimal decisions, lead-ing to faster and more efficient problem-solving. The authors evaluate DARS on the SWE-Bench Lite benchmark, achieving an impressive pass@k score of 55% with Claude 3.5 Sonnet V2 and a pass@1 rate of 47%, surpassing current state-of-the-art open-source frameworks. This approach provides a significant advancement in optimizing coding agent perfor-mance, reducing the need for extensive manual intervention and improving overall efficiency.

##### d. Code Localization & Software Analytics: The works

by Chen et al. [181] and Gholamzadeh et al. [182] contribute significant advancements in the application of Large Language Models (LLMs) to improve software engineering tasks, such as code localization and release validation. Chen et al. [181] introduce LocAgent, a framework for code localization that utilizes graph-based representations of codebases. By parsing code into directed heterogeneous graphs, LocAgent captures the relationships between various code structures and their dependencies, enabling more efficient and accurate local-


**Table 9: Overview of AI Agent Applications for Software Engineering**


| Agent / Tool | Year | Domain | Primary Objective & Details |
|---|---|---|---|
| Ann Arbor Architec-ture [176] | 2025 | Agent Program-ming Arch. | Treat LLMs as automata, enabling programming via formal and natural languages. Introduces the Ann Arbor conceptual framework and Postline platform. Early experiments show improved in-context learning. |
| AgentGym [177] | 2025 | Verification & Super-vision | Scalable training of SWE-agents via SYNGEN data curation and Hybrid Test-time Scaling. Leverages SYNGEN synthetic data and Hybrid Test-time Scaling on SWE-Gym; trained on SWE-Bench Verified. Achieves 51% pass rate on SWE-Bench Verified. |
| TRAVER&DICT [178] | 2025 | Intelligent Tutoring | Trace-and-Verify workflow for stepwise coding guidance; DICT evaluation protocol. Combines knowledge tracing with turn-by-turn verification; evaluated via DICT protocol. Significant improvements in coding-tutoring success rates. |
| CURA [179] | 2025 | Code Reason-ing | Verbal Process Supervision for code understanding and reasoning. Integrates VPS modules with LLM to guide reasoning over code. +3.65% on BigCodeBench with o3-mini. |
| DARS [180] | 2025 | Performance Enhance-ment | Dynamic Action Re-Sampling to branch inference at decision points. Branches on execution feedback to explore alternative actions. 55% pass@k and 47% pass@1 on SWE-Bench Lite (Claude 3.5 Sonnet V2). |
| LocAgent [181] | 2025 | Code Lo-calization | Graph-based code representation for multi-hop localization. Parses code into heterogeneous graphs for reasoning over dependencies. 92.7% file-level accuracy; +12% GitHub issue resolution. |
| GateLens [182] | 2025 | Release Valida-tion | NL→Relational-Algebra conversion and Python code generation for test-data analysis. Automates query translation and optimized code for data processing. 80% reduction in analysis time (automotive software). |
| Repo2Run [183] | 2025 | Env. Con-figuration | Atomic Docker setup synthesis with dual-environment rollback. Synthesizes and tests Dockerfiles; isolates failures via dual environments. 86.0% success on 420 Python repos; +63.9% vs. baselines. |
| UXAgent [184] | 2025 | Usability Testing | LLM-agent with browser connector to simulate thousands of users. Generates qualitative insights, action logs, and recordings before user studies. Accelerates UX iteration and reduces upfront user recruitment. |
| SWE-Gym [185] | 2024 | Training Environ-ment | Realistic Python tasks and unit tests for SWE-agent training. Provides executable environments with tests and natural language descriptions. +19% resolve rate; 32.0% on SWE-Bench Verified; 26.0% on Lite. |
| Qwen2.5-xCoder [186] | 2025 | Multi-Agent Collabo-ration | Multilingual instruction tuning via language-specific agents with memory. Agents collaborate to generate and refine multilingual instructions. Outperforms on multilingual programming benchmarks. |
| SyncMind [187] | 2025 | Collaboration Simula-tion | Defines and benchmarks out-of-sync scenarios to improve agent coordination. Introduces SyncBench with 24 k real-world instances. Exposes performance gaps and guides improvements. |
| CodeSim [188] | 2025 | Code Genera-tion | Plan verification and I/O simulation for multi-agent synthesis & debugging. Incorporates plan verification and internal debugging via input/output simulation. SOTA on HumanEval, MBPP, APPS, CodeContests. Bench.: Benchmarking; Intgr.: Integration & Deployment; Std.: Standards Compliance;: Partial;: Not Supported;: Supported. ization through multi-hop reasoning. Their approach, when applied to real-world benchmarks, demonstrates substantial improvements in localization accuracy, achieving up to 92.7% on file-level localization and enhancing GitHub issue res-olution success rates by 12%. In comparison to state-of- the-art models, LocAgent provides similar performance at a significantly lower cost. On the other hand, Gholamzadeh et al. [182] present GateLens, an LLM-based tool designed to improve release validation in safety-critical systems like automotive software. GateLens automates the analysis of test data by converting natural language queries into Relational Algebra expressions and generating optimized Python code, which significantly accelerates data processing. In industrial evaluations, GateLens reduced analysis time by over 80%, demonstrating strong robustness and generalization across different query types. This tool improves decision-making in safety-critical environments by automating test result analysis, thereby enhancing the scalability and reliability of software systems in automotive applications. |

##### e. Domain-Specific SWE Agents: Hu et al. [183] in-troduce Repo2Run, a novel LLM-based agent aimed at au-
tomating the environment configuration process in software development. Traditional methods for setting up environments often involve manual work or rely on fragile scripts, which can lead to inefficiencies and errors. Repo2Run addresses these challenges by fully automating the configuration of Docker containers for Python repositories. The key innova-tions of Repo2Run are its atomic configuration synthesis and a dual-environment architecture, which isolates internal and external environments to prevent contamination from failed commands. A rollback mechanism ensures that only fully executed configurations are applied, and the agent generates executable Dockerfiles from successful configurations. Eval-uated on a benchmark of 420 Python repositories with unit

tests, Repo2Run achieved an impressive success rate of 86.0%, outperforming existing baselines by 63.9%. Lu et al. [184] developed UXAgent, a tool that uses LLM-Agent technology and a universal browser connector to simulate thousands of users for automated usability testing. It enables user experience (UX) researchers to quickly iterate on study designs by providing qualitative insights, quantitative action data, and video recordings before engaging participants. Wang et al. [178] introduce TRAVER (Trace-and-Verify), a novel agent workflow that combines knowledge tracing estimating a student’s evolving knowledge state with turn-by-turn verification to ensure effective step-by-step guidance toward task completion. Alongside TRAVER, they propose DICT, an automatic evaluation protocol that utilizes controlled student simulation and code generation tests to assess the performance of tutoring agents holistically. SWE-Gym [185] is introduced as the first dedicated environment for training real-world software engineering (SWE) agents, designed around 2,438 Python task instances that include complete code-bases, executable runtime environments, unit tests, and natural language task descriptions. This realistic setup allows for training language model–based SWE agents that significantly improve performance achieving up to 19% absolute gains in resolve rate on popular test sets like SWE-Bench Verified and Lite. Furthermore, the authors explore inference-time scaling by employing verifiers trained on agent trajectories sampled from SWE-Gym, which, when combined with their fine-tuned agents, achieve state-of-the-art performance of 32.0% on SWE-Bench Verified and 26.0% on SWE-Bench Lite.

##### f. Multi-Agent Collaboration & Simulation: The works

by Yang et al. [186], Guo et al. [187], and Islam et al. [188] contribute significant advancements to the application of Large Language Models (LLMs) in code understanding, collabora-tive software engineering, and code generation. Yang et al. [187] propose a novel multi-agent collaboration framework to bridge the gap between different programming languages. By leveraging language-specific agents that collaborate and share knowledge, their approach enhances multilingual instruction tuning, enabling the efficient transfer of knowledge across languages. The Qwen2.5-xCoder model demonstrates supe-rior performance in multilingual programming benchmarks, showcasing its potential to reduce cross-lingual gaps. Guo et al. [187] introduce SyncMind, a framework that defines the out-of-sync problem in collaborative software engineer-ing. Through their SyncBench benchmark, which includes over 24,000 instances of out-of-sync scenarios from real-world codebases, they highlight performance gaps in current LLM agents and emphasize the need for better collabora-tion and resource-awareness in AI systems. Finally, Islam et al. [188] present CodeSim, a multi-agent code generation framework that addresses program synthesis, coding, and debugging through a human-like perception approach. By incorporating plan verification and internal debugging via input/output simulation, CodeSim achieves state-of-the-art per-formance across multiple competitive benchmarks, including HumanEval, MBPP, APPS, and CodeContests. Their approach demonstrates the potential for further enhancement when cou-pled with external debuggers, advancing the effectiveness of code generation systems.

#### 6. Synthetic data generation: Mitra et al. [145] propose

AgentInstruct, a novel framework that leverages synthetic data for post-training large language models through a process termed ”Generative Teaching.” Recognizing the challenges posed by the varying quality and diversity of synthetic data and the extensive manual curation typically required AgentInstruct automates the creation of high-quality instructional datasets using a multi-agent workflow. Starting from raw unstructured text and source code, the framework employs successive stages of content transformation, seed instruction generation across over 100 subcategories, and iterative instruction refinement via suggester-editor pairs. This process yields a dataset of 25 million prompt-response pairs covering diverse skills such as text editing, coding, creative writing, and reading compre-hension. When applied to fine-tune a Mistral-7B model, the resulting Orca-3 model demonstrated significant performance improvements ranging from 19% to 54% across benchmarks like MMLU, AGIEval, GSM8K, BBH, and AlpacaEval as well as a notable reduction in hallucinations for summarization tasks. These findings underscore the potential of automated, agentic synthetic data generation to enhance model capabili-ties while reducing reliance on labor-intensive data curation, positioning AgentInstruct as a promising tool for advancing LLM instruction tuning. Finance Applications Structured Finance & Automation Structured Finance Automation [189] Market Simulation TwinMarket [190] Sequential Investment Decision-Making FinCon [191] Strategic Behavior in Competitive Markets Strategic Behavior [192] Financial Reasoning & QA Multi-Agent Financial QA [193] Stock Analysis & Evaluation Multi-Agent Collaboration [194] FinSphere [195] MarketSenseAI [196] Agentic Financial Modeling & Risk Management Agentic Crews [197] Trustworthy Conversational Shopping Agents Citation-Enhanced CSA [198]

*Figure 10: Agent LLM Applications in Finance*


#### 7. Finance Applications: Finance is a dynamic domain

where the adoption of LLM-based agents has opened new avenues for automation, simulation, analysis, and decision support. This subsection presents recent innovations that span structured finance automation, market simulation, investment decision-making, financial reasoning, stock analysis, and risk management. Fig. 10 presents a classification of Agent LLM Applications for Finance.


##### a. Structured Finance and Automation: Wan et al. [189]

investigate the integration of artificial intelligence into struc-tured finance, where the process of restructuring diverse as- sets into securities such as MBS, ABS, and CDOs presents substantial due diligence challenges. The authors demonstrate that AI, specifically large language models (LLMs), can effec-tively automate the verification of information between loan applications and bank statements. While close-sourced mod-els like GPT-4 achieve superior performance, open-sourced alternatives such as LLAMA3 provide a more cost-effective option. Furthermore, implementing dual-agent systems has been shown to further increase accuracy, albeit with higher operational costs.

##### b. Market Simulation: Yang et al. [190] introduce Twin-

Market, a multi-agent framework that harnesses large language models (LLMs) to simulate complex socio-economic systems, addressing longstanding challenges in modeling human behav-ior. Traditional rule-based agent-based models often fall short in capturing the irrational and emotionally driven aspects of decision-making emphasized in behavioral economics. Twin- Market leverages the cognitive biases and dynamic emotional responses inherent in LLMs to create more realistic simula-tions of socio-economic interactions. The study illustrates how individual agent behaviors can lead to emergent phenomena such as financial bubbles and recessions when combined through feedback mechanisms through experiments conducted in a simulated stock market environment.

##### c. Sequential Investment Decision-Making: Yu et al

[191] propose FinCon, an LLM-based multi-agent framework designed to tackle the complexities of sequential financial investment decision-making. Recognizing that effective in-vestment requires dynamic interaction with volatile environ- ments, FinCon draws inspiration from real-world investment firm structures by establishing a manager-analyst communi-cation hierarchy. This design facilitates synchronized, cross- functional collaboration through natural language interactions while endowing each agent with enhanced memory capacity. A key component is the risk-control module, which periodically triggers a self-critiquing mechanism to update systematic investment beliefs, thereby reinforcing future agent behavior and reducing unnecessary communication overhead. FinCon exhibits strong generalization across various financial tasks, such as stock trading and portfolio management, and offers a promising approach to synthesizing multi-source information for optimized decision-making in dynamic financial markets.

##### d. Strategic Behavior in Competitive Markets: Li et al

[192] investigate the strategic behavior of large language models (LLMs) when deployed as autonomous agents in multi-commodity markets within the framework of Cournot competition. The authors examine whether these models can independently engage in anti-competitive practices, such as collusion or market division, without explicit human interven-tion. Their findings reveal that LLMs can monopolize specific commodities by dynamically adjusting pricing and resource allocation strategies, thereby maximizing profitability through self-directed strategic decisions. These results present signif-icant challenges and potential opportunities for businesses incorporating AI into strategic roles and regulatory bodies responsible for maintaining fair market competition.

##### e. Financial Reasoning and QA: Fatemi et al. [193]

address the limitations of large language models (LLMs) in financial question-answering (QA) tasks that require complex numerical reasoning. Recognizing that multi-step reasoning is essential for extracting and processing information from tables and text, the authors propose a multi-agent framework incorporating a critical agent to evaluate the reasoning process and final answers. The framework is further enhanced with multiple critic agents specializing in distinct aspects of the answer evaluation. Experimental results show that this multi-agent approach significantly boosts performance, with an av- erage increase of 15% for the LLaMA3-8B model and 5% for the LLaMA3-70B model, compared to single-agent systems. Moreover, the proposed system performs comparably to and sometimes exceeds the capabilities of much larger single-agent models such as LLaMA3.1-405B and GPT-4o-mini, although it slightly lags behind Claude-3.5 Sonnet.

##### f. Stock Analysis and Evaluation: Han et al. [194]

present a novel multi-agent collaboration system designed to enhance financial analysis and investment decision-making by leveraging the collaborative potential of multiple AI agents. Moving beyond traditional single-agent models, the system features configurable agent groups with diverse collaboration structures that dynamically adapt to varying market conditions and investment scenarios through a sub-optimal combination strategy. The study focuses on three key sub-tasks funda-mentals, market sentiment, and risk analysis applied to the 2023 SEC 10-K forms of 30 companies from the Dow Jones Index. Experimental findings reveal significant performance improvements with multi-agent configurations compared to single-agent approaches, demonstrating enhanced accuracy, efficiency, and adaptability. In a related study, Han et al. [195] introduce FinSphere, a conversational stock analysis agent designed to overcome two major challenges faced by current financial LLMs: their insufficient depth in stock analysis and the lack of objec-tive metrics for evaluating the quality of analysis reports. The authors make three significant contributions. First, they present Stocksis, a dataset curated by industry experts to enhance the stock analysis capabilities of LLMs. Second, they propose Analyscore, a systematic evaluation framework that objectively assesses the quality of stock analysis reports. Third, they develop FinSphere, an AI agent that leverages real-time data feeds, quantitative tools, and an instruction-tuned LLM to generate high-quality stock analysis in response to user queries. Experimental results indicate that FinSphere outperforms general and domain-specific LLMs and existing agent-based systems, even when these systems are enhanced with real-time data and few-shot guidance. Fatouros et al. [196] introduce MarketSenseAI, an inno-vative framework for comprehensive stock analysis that har- nesses large language models (LLMs) to integrate diverse financial data sources ranging from financial news, historical prices, and company fundamentals to macroeconomic indica-tors. Leveraging a novel architecture that combines Retrieval- Augmented Generation with LLM agents, MarketSenseAI processes SEC filings, earnings calls, and institutional reports

to enhance macroeconomic analysis. The latest advancements in the framework yield significant improvements in funda-mental analysis accuracy over its previous iteration. Empirical evaluations on S&P 100 stocks (2023–2024) reveal cumulative returns of 125.9% versus the index’s 73.5%, while tests on S&P 500 stocks in 2024 show a 33.8% higher Sortino ratio, underscoring the scalability and robustness of this LLM-driven investment strategy.

##### g. Agentic Financial Modeling and Risk Management

Okpala et al. [197] examine integrating large language models into agentic systems within the financial services industry, focusing on automating complex modeling and model risk management (MRM) tasks. The authors introduce the concept of agentic crews, where teams of specialized agents, coordi-nated by a manager, collaboratively execute distinct functions. The modeling crew handles tasks such as exploratory data analysis, feature engineering, model selection, hyperparameter tuning, training, evaluation, and documentation, while the MRM crew focuses on compliance checks, model replication, conceptual validation, outcome analysis, and documentation. The effectiveness and robustness of these agentic workflows are demonstrated through numerical examples applied to datasets in credit card fraud detection, credit card approval, and portfolio credit risk modeling, highlighting the potential for autonomous decision-making in financial applications.

##### h. Trustworthy Conversational Shopping Agents: Zeng

et al. [198] focuses on enhancing the trustworthiness of LLM-based Conversational Shopping Agents (CSAs) by addressing two key challenges: the generation of hallucinated or unsup-ported claims and the lack of knowledge source attribution. To combat these issues, the authors propose a production-ready solution that integrates a ”citation experience” through In-context Learning (ICL) and Multi-UX-Inference (MUI). This approach enables CSAs to include citation marks linked to relevant product information without disrupting user experi-ence features. Additionally, the work introduces automated metrics and scalable benchmarks to evaluate the grounding and attribution capabilities of LLM responses holistically. Exper-imental results on real-world data indicate that incorporating this citation generation paradigm enhances response grounding by 13.83%, ultimately improving transparency and building customer trust in conversational AI within the e-commerce domain.

#### 8. Chemical Reasoning: The domain of chemical reasoning

poses complex challenges for large language models, includ-ing precise information processing, task decomposition, and integrating scientific knowledge and code. In this subsection, we highlight recent advances in developing LLM-based agents for chemical reasoning and materials discovery.

##### a. Chemical Reasoning & Information Processing: The

paper by Cho et al. [199] addresses the challenges of deploying large language model (LLM)–powered agents in resource-constrained environments, particularly for specialized domains and less-common languages, by introducing Tox-chat a Korean chemical toxicity information agent. It presents a context-efficient architecture utilizing hierarchical section search to reduce token consumption and a scenario-based dialogue generation methodology that distills tool-using capabilities from larger models. Experimental evaluations reveal that the fine-tuned 8B-parameter model significantly surpasses untuned models and baseline approaches in database faithfulness and user preference, offering promising strategies for developing efficient, domain-specific language agents under practical con-straints. Chemical reasoning tasks, which involve complex multi-step processes and require precise calculations, pose unique challenges for LLMs, especially in handling domain-specific formulas and integrating code accurately. ChemAgent [146] addresses these challenges by decomposing chemical tasks into manageable sub-tasks and compiling them into a struc-tured memory library that can be referenced and refined in future queries. The framework incorporates three types of memory and a library-enhanced reasoning component, en-abling the system to improve over time through experience. Evaluations on four SciBench chemical reasoning datasets reveal that ChemAgent achieves performance gains of up to 46% with GPT-4, significantly outperforming existing methods and suggesting promising applications in fields such as drug discovery and materials science.

##### b. Materials Discovery & Design: By collaborating with

materials science experts, Kumbhar et al. [200] curate a novel dataset from recent journal publications that encapsulate real-world design goals, constraints, and methodologies. Using this dataset, they test LLM-based agents to generate viable hypotheses to achieve specified objectives under given con-straints. To rigorously assess the relevance and quality of these hypotheses, a novel scalable evaluation metric is proposed that mirrors the critical assessment process of materials scien-tists. Together, the curated dataset, the hypothesis generation method, and the evaluation framework provide a promising foundation for future research to accelerate materials discovery and design using LLM. ChemAgent is a novel framework that aims to enhance chemical reasoning by leveraging large language models through a dynamic, self-updating library.

#### 9. Solving mathematical problems: Mathematical problem-solving remains a fundamental challenge for large language
models due to the need for structured reasoning, formal logic, and precise numerical computation. In this subsection, we present recent efforts to enhance the mathematical capabilities of LLM-based agents through novel prompting strategies, collaborative agent systems, theorem proving, and knowledge integration. Fig. 11 presents a classification of agent LLM applications for solving mathematical problems.

##### a. Mathematical Reasoning and Problem Solving: The

paper by Lei et al. [201] tackles the challenge of ad-vanced mathematical problem-solving in large language mod- els (LLMs), where performance significantly declines despite recent advancements like GPT-4. While methods such as Tree of Thought and Graph of Thought have been explored to enhance logical reasoning, they face notable limitations: their effectiveness on complex problems is limited, and the need for custom prompts for each problem restricts generalizability. In response, the authors introduce the Multi-Agent System for Conditional Mining (MACM) prompting method. MACM successfully addresses intricate, multi-step mathematical chal-lenges and exhibits robust generalization across diverse mathe-


**Table 10: Overview of AI Agent Applications for Mathematical Problem Solving**


| Agent / Tool | Year | Domain | Primary Objective & Details |
|---|---|---|---|
| MACM [201] | 2024 | Advanced Reasoning | Solve multi-step math problems with robust generalization. Multi-Agent Conditional Mining prompting for iterative refinement. MATH level 5 accuracy increase from 54.68% to 76.73% on GPT-4 Turbo. |
| MathLearner [202] | 2024 | Inductive Reasoning Enhance LLM | reasoning via inductive retrieval and application. Retrieval module plus procedural knowledge injection in inductive loop. +20.96% global accuracy; solves 17.54% previously unsolved problems. |
| Prompt Sampling [203] | 2024 | Search Space Expansion | Combine diverse prompting methods to expand search space efficiently. Uniform sampling over multiple prompt strategies; fewer inference runs. 43% fewer runs for MATH-hard with maximal coverage. |
| Flows [204] | 2024 | Reasoning Trace Generate detailed | math reasoning traces online. Collaborative LLM ensemble with online DPO and rollouts. Significant improvement in reasoning quality versus direct inference. |
| KG-Proof Agent [205] | 2025 | Proof Con-struction Automate | formalization of proofs using knowledge graphs. Integrates concept KG with LLM to structure lemmas and steps. 34% success on MUSTARDSAUCE; 2–11% improvement over baselines. |
| MA-LoT [206] | 2025 | Theorem Proving Synergize | natural-language reasoning with Lean4 verification feedback. Multi-agent chain-of-thought plus LoT-Transfer pipeline in Lean4. 61.07% on MiniF2F-Test (Lean4) versus 22.95% for GPT-4. |
| MATHVC [207] | 2024 | Educational Modeling Simulate group | discussions for mathematical modeling skills. Virtual classroom with diverse student-agents and meta planning. Realistic dialog; improves modeling task performance. |
| PACE [208] | 2025 | Personalized Tutoring | Tailor math instruction to learning styles with Socratic feedback. Felder-Silverman personas plus Socratic method and tailored data. Higher engagement and outcomes versus traditional tutors. Agent Trading |
| Agent Trading Arena [209] | 2025 | Numerical Reasoning Improve numeric | inference with visual data and reflection. Virtual stock game plus analysis over plots and charts. Enhanced geometric reasoning; validated on NASDAQ dataset. Proof Val.: Proof Validation; Solver Integr.: Solver & Assistant Integration; Notation Sup.: Notation & Formalism Support:: Partial;: Not Supported;: Supported. matical contexts. Notably, using MACM, the accuracy of GPT-4 Turbo on level five problems in the MATH dataset improves markedly from 54.68% to 76.73%, demonstrating its potential to elevate LLM inferential capabilities substantially. Xie et al. [202] present an agent framework designed to enhance the mathematical reasoning abilities of large lan-guage models (LLMs) through inductive reasoning. Drawing inspiration from the human learning process of generaliz-ing information and applying prior knowledge to new tasks, the framework significantly outperforms traditional chain-of-thought approaches. Specifically, it improves global accuracy by 20.96% and can solve 17.54% of mathematical problems that the baseline fails to address. A key framework component is its efficient retrieval method, which enables the model to effectively incorporate external knowledge and support math-ematical computations based on explicit written procedures. Lee et al. [203] investigate the limitations of traditional single prompting methods in large language models (LLMs) for mathematical reasoning and explore alternative prompting strategies. It experimentally demonstrates that distinct prompt-ing methods each probe unique search spaces, a differentiation that becomes more pronounced with increased problem com-plexity. To capitalize on this diversity, the study introduces an efficient sampling process that uniformly combines outputs from these varied methods, thereby expanding the overall search space and achieving improved performance with fewer inference runs. Notably, for the particularly challenging prob-lems in the MATH-hard subset, the approach reached maximal search space utilization with approximately 43% fewer runs compared to individual methods. Deng et al. [204] introduce a novel approach to enhance the generation of detailed and accurate reasoning traces in large language models (LLMs), particularly for mathemati-cal reasoning tasks. The authors propose an online learning framework termed ”Flows,” where component LLMs work collaboratively and iteratively, engaging in incremental output production to build coherent solutions. Central to the approach is online Direct Preference Optimization (DPO) with rollouts, which generates DPO pairs for each training example and updates the models in real-time. By directly comparing the quality of reasoning traces produced by this method against those generated by standard direct model inference, the study demonstrates that the proposed Flow framework significantly improves LLM performance in mathematical reasoning. Li et al. [205] introduce a novel framework that augments large language models (LLMs) with knowledge graphs to improve the construction and formalization of mathematical proofs. The proposed approach tackles persistent challenges Solving Mathematical Problems Mathematical Reasoning & Problem Solving |

##### b. Educational and Tutoring Applications: Yue et al

[207] introduce MATHVC, a pioneering virtual classroom powered by large language models (LLMs) designed to en-hance students’ mathematical modeling (MM) skills through collaborative group discussions. Recognizing that traditional MM practice often suffers from uneven access to qualified teachers and resources, the authors leverage LLMs’ capabil-ities to simulate diverse student characters, each embody- ing distinct math-relevant properties. To ensure that these simulated interactions mirror authentic student discussions, the framework incorporates three key innovations: integrating domain-specific MM knowledge into the simulation, defining a symbolic schema to ground character behaviors, and em-ploying a meta planner to guide the conversational flow. Liu et al. [208] introduce the Personalized Conversational Tutoring Agent (PACE) for mathematics instruction, address-ing a critical gap in intelligent educational systems by adapting to individual learner characteristics. PACE leverages the Felder and Silverman learning style model to simulate distinct student personas, enabling the system to tailor teaching strategies to diverse learning styles, a crucial factor for enhancing engagement and comprehension in mathematics. Integrating the Socratic teaching method, PACE provides instant, reflective feedback that encourages deeper cognitive processing and critical thinking. The framework also involves constructing personalized teaching datasets and training specialized mod-els, which facilitate identifying and adapting each student’s unique needs. Extensive evaluations using multi-aspect criteria demonstrate that PACE outperforms traditional methods in personalizing the educational experience and boosting student motivation and learning outcomes.

##### c. Numerical Reasoning: Ma et al. [209] investigate

the limitations of large language models (LLMs) in handling dynamic and unseen numerical reasoning tasks, mainly when operating on plain-text data. To address this, the authors intro-duce the Agent Trading Arena, a virtual numerical game simu- lating complex economic systems via zero-sum stock portfolio investments, which better reflects real-world scenarios where optimal solutions are not clearly defined. Experimental results indicate that LLMs, including GPT-4o, face challenges with algebraic reasoning in textual formats, often focusing on local details at the expense of broader trends. In contrast, when LLMs are provided with visual data representations, such as scatter plots or K-line charts, they exhibit significantly enhanced geometric reasoning capabilities. This improvement is further enhanced by incorporating a reflection module that facilitates the analysis and interpretation of complex data. These findings are validated using the NASDAQ Stock dataset, underscoring the value of visual inputs for bolstering numer-ical reasoning in LLMs.

#### 10. Geography Applications: Yu et al. [210] introduce

MineAgent, a modular framework designed to enhance the capabilities of multimodal large language models (MLLMs) in the domain of remote-sensing mineral exploration. This field presents significant challenges, including the need for domain-specific geological knowledge and the complexity of reasoning across multiple remote-sensing images, which is further complicated by long-context issues. MineAgent ad-dresses these challenges by incorporating hierarchical judg- ing and decision-making modules to improve multi-image reasoning and spatial-spectral integration. In addition, the authors propose MineBench, a specialized benchmark to eval-uate MLLMs on mineral exploration tasks using geological and hyperspectral data. Extensive experiments demonstrate

the effectiveness of MineAgent, showcasing its potential to significantly advance the use of MLLMs in the critical area of remote-sensing mineral exploration Ning et al. [211] introduce an autonomous geographic information system (GIS) agent framework that utilizes large language models (LLMs) to perform spatial analyses and cartographic tasks. A significant research gap in the field has been the ability of these agents to autonomously discover and retrieve the necessary geospatial data. The proposed framework addresses this by generating, executing, and de-bugging programs to select data sources from a predefined list, using source-specific handbooks that document metadata and retrieval details. The framework is designed in a plug-and-play style, allowing users or automated crawlers to easily add new data sources by creating additional handbooks. A prototype of the agent has been developed as a QGIS plugin and Python program. Experimental results demonstrate its capability to retrieve data from various sources, including OpenStreetMap, U.S. Census Bureau demographic data, satel-lite basemaps from ESRI, global digital elevation models from OpenTopography, weather data, and COVID-19 case data from the NYTimes GitHub. This work is one of the first efforts to create an autonomous GIS agent for geospatial data retrieval, marking a significant advancement in spatial data automation.

#### 11. Multimedia Applications: Multimedia is an emerging

frontier for LLM-based agents, where creative and interpretive tasks require coordination across diverse modalities, including text, audio, image, and video. In this subsection, we present recent advancements in applying agent-based language learn-ing and machine learning (LLM) systems to domains such as film production, music and poetry generation, drama scripting, fashion assistance, and lyric composition. Fig. 12 presents a classification of agent LLM applications for Multimedia.

##### a. Film Automation Agents: Xu et al. [212] introduce

FilmAgent, an innovative LLM-based multi-agent collabora-tive framework designed to automate end-to-end film pro- duction within 3D virtual spaces. Virtual film production involves complex decision-making, including scriptwriting, cinematography, and actor positioning. FilmAgent simulates various crew roles such as directors, screenwriters, actors, and cinematographers, covering crucial stages of the film production process. These stages include idea development, where brainstormed ideas are transformed into structured story outlines; scriptwriting, which generates dialogues and character actions; and cinematography, which determines the camera setups for each shot. The agents collaborate iteratively, providing feedback and revisions to verify intermediate scripts and reduce hallucinations. Evaluations of the generated videos on 15 ideas across four key aspects show that FilmAgent outperforms all baselines, achieving an average score of 3.98 out of 5. Despite using the GPT-4o model, FilmAgent sur-passes the single-agent o1, demonstrating the benefits of a coordinated multi-agent system.

##### b. Story-to-Video Production Agents: Wang et al. [213]

introduce AesopAgent, an Agent-driven Evolutionary Sys-tem designed for story-to-video production, leveraging the advancements in Agent and Artificial Intelligence Generated Content (AIGC) technologies. AesopAgent integrates multiple Multimedia Applications Film Au-tomation Agents FilmAgent [212] Story-to-Video Production Agents AesopAgent [213] Drama Script Generation Agents IBSEN [214] Fashion-Domain Conver-sational Agents Fashion Assis-tant Eval. [215] Symbolic Music Composition Agents ComposerX [216] Music Under-standing & Generation Agents MusicAgent [217] Poetry Generation Agents Multi-Agent Poetry Framework [218] Lyric Generation Agents Melody-Lyric Agents [219]

*Figure 12: Agent LLM Applications in Multimedia*

generative capabilities within a unified framework, enabling users to easily convert story proposals into scripts, images, audio, and videos. The system orchestrates the entire video generation workflow, ensuring that the generated content is both rich and coherent. The system consists of two layers: the Horizontal Layer and the Utility Layer. The Horizontal Layer incorporates a novel RAG-based evolutionary system that continuously optimizes the video production process by accumulating expert knowledge and refining workflow steps, such as LLM prompt optimization. The Utility Layer provides essential tools for consistent image generation, ensuring visual coherence in terms of composition, characters, and style, while also integrating audio and special effects.

##### c. Drama Script Generation Agents: Han et al. [214]

introduce IBSEN, a director-actor coordination agent frame-work designed to generate drama scripts and provide greater control over the plot development, especially in scenarios where human players are involved. While current language


**Table 11: Overview of AI Agent Applications for Multimedia**


| Agent / Tool | Year | Domain | Primary Objective & Details |
|---|---|---|---|
| FilmAgent [212] | 2025 | Film Automation Fully automate | end-to-end 3D virtual film production. Multi-agent roles (director, screenwriter, actors, cinematographer) with iterative feedback loops. Outperforms single-agent baselines with coherent video across 15 scenarios. Mean user score 3.98/5 Virtual studio pipeline support |
| Exports MP4/WebM AesopAgent [213] | 2024 | VideoConvert story drafts | into scripts, images, audio, and video. Two-layer RAG-evolutionary workflow plus utility layer for image/audio/effects. Rich, coherent multimodal outputs with continuous optimization. Workflow convergence rate≈ 85 % Integrates with AIGC asset generators Supports PNG, WAV, MP4 |
| MP4 IBSEN [214] | 2024 | Drama Scripts Generate coherent | drama scripts via director–actor coordination. Director agent outlines plot; actor agents role-play and adjust narrative. Diverse, complete scripts preserving character traits. Narrative coherence ¿ 90% (human eval) Scriptwriting toolchain compatible Plain-text script output |
| Fashion-Agent [215] | 2024 | Conversational Retail | Enhance online fashion discovery with LLM dialogue agents. LLM front-end connects to search & recommendation backends. 4 000-dialog dataset; improves retrieval relevance by 18 %. Precision@5: 78% E-commerce API integration JSON / HTML widget |
| JSON / HTML widget ComposerX [216] | 2024 | Music Composi-tion | Multi-agent symbolic music generation with harmony constraints. Agents specialize in melody, harmony, and structure using LLM reasoning. Coherent polyphonic pieces rated high on musicality. Subjective rating 4.2/5 MIDI pipeline plugin |
| Standard MIDI files MusicAgent [217] | 2023 | Music Processing | Orchestrate diverse music tasks via unified LLM agent. Autonomous task decomposition and tool invocation over HF/GitHub/APIs. Simplifies tool use; reduces development effort by 40 %. Task completion time ↓ 40 % Integrates FFmpeg, Librosa, Web APIs WAV, MP3, |
| MIDI PoetryAgents [218] | 2024 | Poetry Generation Boost diversity & | novelty in LLM-generated poetry via multi-agent social learning. Cooperative & non-cooperative agent interactions on GPT-2/3/4. +3.0–3.7 pp diversity; +5.6–11.3 pp novelty. Distinct n-gram ↑ 11% Text pipeline integration |
| UTF-8 text LyricAgents [219] | 2024 | Lyric Generation Melody-to-lyric | alignment in tonal languages with multi-agent sub-tasks. Agents for rhyme, syllable, alignment & consistency; evaluated via singing synth. Listening test accuracy 85 %. Alignment score 0.87 Singing-synth pipeline ready LRC / JSON lyric files Eval. Metrics: Evaluation Metrics; Pipeline Integr.: Pipeline Integration; Fmt. Compat.: Format Compatibility. model agents excel at creating individual behaviors for char-acters, they often struggle with maintaining consistency and coherence at the storyline level. IBSEN addresses this by introducing a director agent that writes plot outlines based on user input, instructs actor agents to role-play their respective characters, and adjusts the plot as needed to ensure that the narrative progresses toward the intended objective. The framework was evaluated using a novel drama plot involving multiple actor agents, where the director agent guided the interactions. The results demonstrate that IBSEN is capable of generating diverse and complete drama scripts from a rough plot outline, while preserving the unique characteristics of each character, showing the effectiveness of the framework in producing controlled, dynamic narrative content. |

##### d. Fashion-Domain Conversational Agents: Maroniko-lakis et al. [215] focus on the potential of Large Language
Models (LLMs) to revolutionize online fashion retail by en-hancing customer experiences and improving product discov- ery through conversational agents. These LLM-powered agents allow customers to interact naturally, refining their needs and receiving personalized fashion and shopping advice. For tasks like finding specific products, conversational agents must translate customer interactions into calls to various backend systems, such as search engines, to display relevant product options. The authors emphasize the importance of evaluating the capabilities of LLMs in these tasks, particularly in integrat-ing with backend systems. However, existing evaluations are often complex due to the lack of high-quality, relevant datasets that align with business needs. To address this, the authors developed a multilingual evaluation dataset comprising 4,000 conversations between customers and a fashion assistant on a large e-commerce platform.

##### e. Symbolic Music Composition Agents: Deng et al

[216] introduce ComposerX, an agent-based symbolic music generation framework designed to enhance the music compo-sition capabilities of Large Language Models (LLMs). While LLMs have demonstrated impressive performance in STEM domains, they often struggle with music composition, par-ticularly when dealing with long dependencies and harmony constraints. Even when equipped with advanced techniques like In-Context Learning and Chain-of-Thought, LLMs typi-cally generate poorly structured music. ComposerX aims to address this by leveraging the reasoning abilities of LLMs and their extensive knowledge of music history and theory. By employing a multi-agent approach, the framework significantly enhances the music composition quality of GPT-4. The results show that ComposerX is capable of generating coherent, polyphonic music compositions with engaging melodies that

follow user instructions, marking a substantial improvement in the application of LLMs to creative music composition tasks.

##### f. Music Understanding & Generation Agents: Yu et al

[217] present MusicAgent, a system designed to streamline AI-powered music processing by organizing and integrat-ing diverse music-related tasks. Music processing spans a wide range of activities, from generation tasks like timbre synthesis to comprehension tasks like music classification. However, developers and amateurs often struggle to navigate the complexity of these tasks, particularly due to the varying representations of music data and the applicability of different models across platforms. MusicAgent addresses this challenge by offering an integrated solution that simplifies the process for users. The system includes a comprehensive toolset that gathers music tools from diverse sources such as Hugging Face, GitHub, and Web APIs. Additionally, it incorporates an autonomous workflow powered by Large Language Models (LLMs), like ChatGPT, which organizes these tools and au-tomatically decomposes user requests into sub-tasks, invoking the appropriate tools. The primary goal of MusicAgent is to alleviate users from the technicalities of using AI-based music tools, allowing them to focus on the creative aspects of music.

##### g. Poetry Generation Agents: Zhang et al. [218] intro-duces a framework for enhancing the diversity and novelty of
poetry generated by Large Language Models (LLMs) by in-corporating social learning principles. While LLMs have made significant strides in automatic poetry generation, their outputs often lack the diversity and creativity seen in human-generated poetry. The proposed framework emphasizes both cooperative and non-cooperative interactions among multiple agents to foster diversity in generated poetry. This is the first attempt to apply multi-agent systems in non-cooperative environments for poetry generation, utilizing both TRAINING-BASED agents (GPT-2) and PROMPTING-BASED agents (GPT-3 and GPT-4). Experiments based on 96k generated poems show sig- nificant improvements, particularly for TRAINING-BASED agents, with a 3.0–3.7 percentage point increase in diver-sity and a 5.6–11.3 percentage point increase in novelty, as measured by distinct and novel n-grams. The results also reveal that poetry generated by these agents shows increased divergence in terms of lexicons, styles, and semantics. For PROMPTING-BASED agents, the non-cooperative environ-ment helps enhance diversity, with an increase of 7.0–17.5 percentage points, though these agents showed a decrease in lexical diversity over time and did not exhibit the desired group-based divergence.

##### h. Lyric Generation Agents: Liu et al. [219] address

the challenges of melody-to-lyric generation by leveraging Generative Large Language Models (LLMs) and multi-agent systems. Previous research in this area has been constrained by limited high-quality aligned data and unclear standards for creativity. Many studies focused on broad themes or emotions, which have limited value given the advanced capabilities of current language models. In tonal contour languages like Mandarin, where pitch contours are influenced by both melody and tone, achieving a good fit between lyrics and melody becomes more complex. The study, validated by the Mpop600 dataset, demonstrates that lyricists and melody writers care-fully consider this fit during their composition process. To tackle this, the authors developed a multi-agent system that de-composes the melody-to-lyric task into specific sub-tasks, with individual agents managing aspects such as rhyme, syllable count, lyric-melody alignment, and consistency. The quality of the generated lyrics was evaluated through listening tests using a diffusion-based singing voice synthesizer, assessing how different agent groups performed in terms of lyric creation. This work introduces a more structured approach to melody-to-lyric generation, offering a deeper understanding of the interaction between melody and lyrics in tonal languages.

### C. AI Agents Protocols

Recent advances in autonomous AI systems have under-scored the importance of standardized communication proto- cols in facilitating seamless interaction among agents, tools, and external services. In this subsection, we present three prominent protocols developed between 2024 and 2025: the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Protocol (A2A).

#### 1. Agent Communication Protocol (ACP): In 2025, IBM

Research proposed the agent-to-agent communication protocol named ACP, which is central to the operation of BeeAI , an experimental platform designed to streamline the orches-tration and execution of open-source AI agents, regardless of their underlying framework or code base. The primary goal of ACP is to standardize communication between agents, addressing challenges posed by inconsistent interfaces and enabling seamless interaction across diverse agents and client systems. Inspired by Anthropic’s MCP, ACP initially aimed to connect agents to data and tools but has since evolved to include advanced features such as discovery, delegation, and multi-agent orchestration. Core components of BeeAI include the BeeAI Server, which orchestrates agent processes in a local-first environment and provides a unified REST endpoint for external apps and UIs, and the ACP SDKs, which offer libraries in Python and TypeScript, along with a command-line interface and UI for easy agent discovery and launch [221]. ACP messages are custom JSON objects containing a top-level "role" field and a "parts" array, where each part encodes MIME-type metadata along with either inline con-tent or content URLs, optional encoding hints, and arbitrary metadata fields. Context is maintained via a session\_id issued on the first call; reusing that same ID causes the full turn history to be prepended to each request, enabling stateful conversational sessions. In the event of errors, ACP delivers structured payloads with "code" and "message" in either HTTP response bodies, within run-result envelopes, or as real-time stream events; clients are responsible for implementing retry or fallback logic.

#### 2. Model Context Protocol (MCP): In late 2024, Anthropic

introduced the Model Context Protocol (MCP), an open and flexible protocol that standardizes how AI systems interact with external tools and data sources, much like a USB-C port provides a universal connection for devices. Inspired by the Language Server Protocol, MCP enables AI agents to https://github.com/i-am-bee/beeai-framework

A2A Client A2A Client A2A Client A2A Client Remote Agent Remote Agent Remote Agent Remote Agent A2A Server CrewAI Agent A2A Server LangChain Agent A2A Server Haystack Agent A2A Server Microsoft AutoGen Agent A2A protocol A2A protocol MCP Client MCP protocol A2A protocol Large Language Model (e.g., DeepSeek, Qwen, ...etc.) Agent Framework OpenRouter API Agent Development Kit Enabling dynamic, multimodal interactions among various agents without requiring shared memory, resources, or tools. MCP Client MCP Client MCP Client MCP Client MCP Client MCP Server MCP Server MCP Server MCP Server MCP Server MCP Server Enable agents to interface with tools, APIs, and resources using standardized structured inputs and outputs. MCP protocol MCP protocol MCP protocol MCP protocol MCP protocol Agent A MCP Host Agent B MCP Host Allow a diverse selection of MCP servers to be integrated with agents. Front-EndFront-End Web Browser - User Local Data Source 1 Local Data Source 2 Local Data Source 3 Local Data Source 4 Remote Service Remote Service Web Browser - User A2A protocol

*Figure 13: Multi-Agent Integration Framework: Enabling dynamic collaboration through the A2A and MCP Protocols*

autonomously identify, select, and manage a wide range of ser-vices based on the specific context of each task. The protocol facilitates the development of complex workflows by offering a growing catalog of pre-built integrations, the flexibility to switch between different LLM providers, and best practices for securing data within an organization’s infrastructure [223]. An expanding ecosystem of servers highlights the protocol’s potential. For example, official reference servers demonstrate MCP’s core capabilities through secure file management and database access, utilizing PostgreSQL, SQLite, and Google Drive. At the same time, development environments benefit from integration with tools such as Git, GitHub, and GitLab. Moreover, MCP supports productivity and communication enhancements via integrations with platforms like Slack and Google Maps and even extends to specialized AI tools, includ-ing image generators and sophisticated search APIs . MCP is designed around a client-server architecture in which host applications connect to multiple lightweight servers [220]. This allows secure access to local data sources such as files and databases and remote services available through web APIs. By unifying these interfaces, MCP transforms everyday platforms into versatile, multi-modal AI agents, simplifying the creation of AI-native applications and accelerating inno-vation across diverse domains. MCP messages conform to the JSON-RPC 2.0 standard, with each request carrying the fields "jsonrpc":"2.0", "id", "method" and an optional "params" object, and each response echoing the same "id" alongside either a "result" or an "error". Context sharing is host-mediated https://github.com/modelcontextprotocol/servers and stateful: the MCP hub aggregates the full conversation history. It selectively forwards only those context fragments that each server has declared it can consume, ensuring isolation between adapters. For failure recovery, MCP builds on JSON- RPC’s native error objects by providing built-in cancella-tion requests and structured error-reporting utilities, allowing clients to cancel operations or receive detailed diagnostics when calls fail.

#### 3. Agent-to-Agent Protocol (A2A): In 2025, Google intro-duced the Agent2Agent (A2A) protocol to usher in a new
era of seamless interoperability among AI agents, significantly enhancing workplace productivity and automation [222]. The protocol is designed to facilitate dynamic collaboration be-tween autonomous agents, enabling them to work together across isolated data systems and diverse applications regard-less of their underlying frameworks or vendors. Using familiar standards such as HTTP, SSE, and JSON-RPC, A2A simplifies integration with existing IT infrastructures while also ensuring robust enterprise-grade security through proven authentication and authorization practices. A2A supports both swift and long-duration tasks by allowing agents to exchange real-time updates, negotiate user interface requirements, and perform capability discovery via structured ”Agent Cards. A2A extends JSON-RPC 2.0 with a TypeScript interface that includes optional fields "jsonrpc", "id", "method", "params", "result", and "error". A shared task ID groups interactions passed both as the JSON-RPC "id" and within "params.id", and agents consume context updates by subscribing to Server-Sent Events streams (e.g. via tasks/sendSubscribe). For failure recovery, A2A defines standard JSON-RPC error codes (such as−32700 for


**Table 12: Comparison of MCP, ACP, and A2A Protocols**


| Feature | MCP (Model Context Protocol) | ACP (Agent Communication Protocol) | A2A (Agent-to-Agent Protocol) |
|---|---|---|---|
| Main Purpose | Facilitates access to context and data for LLMs. | Enables communication between multiple agents within BeeAI. | Facilitates communication and task-sharing between agents across frameworks. |
| Common Setup | Distributed servers providing specific data, connected via an MCP hub. | BeeAI Server coordinates and manages multiple agents within a local environment. | Agents from different frameworks discover and connect through HTTP interfaces. |
| Key Capabilities | Standardized interface for connecting data and services to LLMs. | Simplifies agent deployment, discovery, and offers deep telemetry within BeeAI. | Allows agents to discover each other's capabilities and share tasks with updates. |
| Typical Application | Managing context for LLMs and integrating data streams. | Managing multiple agents within BeeAI's environment. | Enabling interaction and collaboration between agents from diverse systems. |
| Core Objective | Uniformly managing how LLMs receive context and external tools. | Standardizing communication between BeeAI agents and external systems. | Creating a standardized method for agents from different systems to communicate and collaborate. |
| Architecture | Client-server model where LLMs hook into servers for data and tools. | BeeAI Server orchestrates the interaction of local agents and integrates external frameworks. | Agents connect through agent cards and HTTP for task execution and communication. |
| Key Differences | Focuses on integrating tools and data into a single LLM process. | Primarily focused on internal coordination of agents within BeeAI. | Aims at linking agents across different ecosystems to collaborate effectively. |
| Ideal Usage Scenario | Integrating multiple data sources or services into an LLM workflow. | Running and managing various agents within BeeAI's environment. | Connecting agents from different platforms to enable collaboration and task-sharing. |
| Common Use Cases | Implementing controlled, secure LLM workflows with external data. | Orchestrating multi-agent environments with BeeAI's platform. | Enabling task sharing and agent communication across different vendor systems. |
| Message Structure | JSON-RPC 2.0 requests/responses with fields "jsonrpc", "id", "method", "params", and "result"/"error". | Custom JSON objects with top-level "role" and an array of "parts" supporting MIME types, content URLs, encoding, and metadata. | JSON-RPC extension in TypeScript with id, method, params, result/error and optional SSE streaming. |
| Context Sharing | Host-mediated, stateful sessions aggregating full conversation and forwarding only declared context fragments. | Stateful sessions via a session_id; full history is prepended on each call when the same ID is reused. | Task ID grouping in both id and params.id; context streamed via Server-Sent Events with resubscription support. |

### D. Training datasets

High-quality training datasets are crucial for enhancing the reasoning, multilingual understanding, and instruction-following abilities of large language models. In this subsection, we present three recently developed datasets: NaturalReason-ing, FineWeb2, and MagPie-Ultra. Each dataset addresses different aspects of model training, ranging from expanding reasoning across multiple domains to enhancing multilingual capabilities and advancing the generation of synthetic instruc-tions.

#### 1. NaturalReasoning dataset: Scaling reasoning capabili-ties beyond traditional domains such as math and coding has
been challenging due to the scarcity of diverse, high-quality questions. In response, [224] introduces NaturalReasoning a comprehensive dataset comprising 2.8 million questions that span multiple domains, including STEM fields (like Physics and Computer Science), Economics, and Social Sciences, com-plete with reference answers. The dataset is designed not only to serve as a resource for knowledge distillation experiments, where it effectively transfers reasoning capabilities from a strong teacher model, but also for unsupervised self-training using external reward models. When training the Llama3.1- 8B-Instruct model, NaturalReasoning demonstrates superior scaling effects, achieving notably higher average performance on benchmarks such as MATH, GPQA, and MMLU-Pro compared to other datasets. This work highlights the potential of a large, diverse question dataset to expand the boundaries of LLM reasoning across a broader range of fields.

#### 2. FineWeb2 dataset: Hugging Face’s team introduced

[225] FineWeb2, a groundbreaking multilingual dataset com-prising 8TB of meticulously cleaned text data with over 3 trillion non-English words drawn from more than 1,000 languages. FineWeb2 supports a total of 1,893 languages, with substantial coverage of 486 languages, including more than 1MB of data, and 80 languages boast over 1GB each, demonstrating its extensive linguistic diversity. Built upon 96 snapshots of CommonCrawl data spanning 2013 to 2024 and processed using the ”datatrove” alongside sophisticated filtering code and configurations, FineWeb2 employs inno-vative techniques such as ”re-hydration,” deduplication, and language-specific filtering to ensure high data quality. Ex-tensive ablation experiments, conducted with a 1.45 billion- parameter model trained on 30 billion tokens, further validate the dataset’s robustness. In comparative evaluations against established datasets like CC-100, mC4, CulturaX, and HPLT, FineWeb2 consistently outperforms across diverse languages. Additionally, specialized evaluations using the FineTasks benchmark on 9 varied languages underscore its potential for advancing multilingual natural language processing and retrieval-augmented generation applications.

#### 3. MagPie-Ultra dataset: MagPie-Ultra [226] is a synthetic

dataset generated using Meta Llama 3.1 405 B-Instruct FP8, representing the first open dataset of its kind. It comprises 50,000 synthetic instruction pairs, created by prompting the language model with minimal ”empty” prompts (only initial special tokens) that allow it to generate both user queries and corresponding responses auto-regressively. These generated pairs, filtered according to the MagPie recipe and refined via Argilla distilabel, cover a diverse range of challenging tasks, including coding, mathematics, data analysis, creative writing, advice seeking, and brainstorming. In addition to the raw instruction pairs, the dataset includes detailed metadata quality and difficulty scores, embeddings, topic labels, and safety as-sessments from tools like ArmorRM and LlamaGuard, which further support its use in training and evaluating large language models across complex instruction-following scenarios.

### E. Human-in-the-Loop AI Agents

Human-in-the-loop (HITL) interactions provide essential safeguards for autonomous agents, particularly in business-critical scenarios where incorrect tool selection or param- eter misinterpretation can lead to unintended side effects. HITL mechanisms maintain human oversight throughout the orchestration of an agent by interposing confirmation steps between the decision-making of the model and the execution of sensitive operations. Recently, the Amazon team proposed Amazon Bedrock Agents [227], which supports two primary HITL frameworks: • User Confirmation. This mechanism pauses the orchestra-tion to expose the intended function call and parameter values to the end user for approval. Non-critical read operations—such as retrieving PTO balances—execute automatically, while write operations—such as creating, updating, or canceling a PTO request—are gated by a Boolean confirm/reject prompt. Upon confirmation, the agent proceeds; upon rejection, the workflow either aborts or generates an alternative plan. Developers can configure at a per-action level which tools require confirmation, striking a balance between automation and safety. • Return of Control (ROC). ROC elevates human involve-ment by returning entire action groups to the applica- tion layer, allowing users not only to approve but also to edit parameters or provide additional context before execution. Configured at the action-group level, ROC enables more nuanced workflows—such as adjusting PTO dates via an interactive form—where a simple yes/no decision is insufficient. Final validation and execution are performed by the application’s API, ensuring compliance with business rules and regulatory requirements. By integrating these HITL patterns, developers can harness the efficiency of autonomous agents while preserving accuracy, accountability, and user trust.

### F. Collaborative LLM frameworks

Wang et al. [228] proposed TalkHier, which is a col-laborative framework that integrates a rigorously structured messaging protocol with a hierarchical refinement process to improve inter-agent communication. It defines three message types, raw input, intermediate output, and background context, to organize information flow, improving clarity, and reducing misunderstandings common in unstructured exchanges. The hierarchical refinement mechanism allows agents to iteratively improve their contributions at successive levels, balancing diverse perspectives and mitigating biases introduced by feed-back ordering. Experimental results on complex subdomain problem solving, open question answering, and Japanese text generation show that TalkHier outperforms current approaches

and that each protocol element and refinement layer con-tributes meaningfully to its overall success. Chen et al. [229] tackles the challenge of using large lan-guage models for complex scientific problem solving by intro- ducing CoMM, a collaborative multi-agent, multi-reasoning-path prompting framework. In CoMM, each agent assumes a distinct expert role and follows its reasoning trajectory, which together foster a richer exploration of the problem space than single-chain prompts allow. By distributing few-shot exem-plars across these role-play agents, the framework balances diverse analytical approaches and mitigates biases that arise when feedback is processed sequentially. Evaluation of two undergraduate-level science questions shows that CoMM not only exceeds competitive baselines, but also that independently prompting agents as different specialists is critical to achieving its improved performance.

## 5 Challenges And Open Problems

As the capabilities of AI agents and large language models continue to grow, new challenges and open problems emerge that limit their effectiveness, reliability, and security [230]. In this section, we highlight several critical research directions, including advancing the reasoning abilities of AI agents, understanding the failure modes of multi-agent systems, sup-porting automated scientific discovery, enabling dynamic tool integration, reinforcing autonomous search capabilities, and addressing the vulnerabilities of emerging communication protocols.

### A. AI Agents Reasoning

The primary challenge addressed in [231] is the inherent limitation of traditional Chain-of-Thought (CoT) methods, which only reveal the final reasoning steps without explicitly modeling the underlying cognitive process that leads to those steps. Meta Chain-of-Thought (Meta-CoT) aims to fill this gap by capturing and formalizing the latent reasoning that underlies a Chain-of-Thought (CoT). This involves not only generating the visible chain of thought but also understanding the in-context search behavior and iterative reasoning steps that contribute to it. To overcome these challenges, the authors explore innovative approaches, including process supervision, synthetic data generation, and search algorithms, to produce robust Meta-CoTs. Moreover, they propose a concrete train-ing pipeline that integrates instruction tuning with linearized search traces and reinforcement learning post-training. Open research questions remain regarding scaling laws, the role of verifiers, and the discovery of novel reasoning algorithms, underscoring the complexity and potential of advancing more human-like reasoning in large language models.

### B. Why Do Multi-Agent LLM Systems Fail?

Pan et al. [232] present a critical examination of why multi-agent LLM systems, despite the theoretical benefits of collaboration, continue to underperform compared to their single-agent counterparts. Through a rigorous study of five open-source frameworks across 150 tasks, the authors enlist expert human annotators to identify fourteen distinct failure modes ranging from ignoring task or role specifications and unnecessary repetition, to lapses in memory and flawed verifi-cation processes. These issues are systematically grouped into three categories: design and specification shortcomings, inter-agent misalignment, and challenges in task verification and termination. Moreover, the study explores interventions such as refining agent role definitions and orchestration strategies, but finds that these measures alone are insufficient; thereby, it outlines a clear roadmap for future research to address the intricate challenges inherent in multi-agent coordination.

### C. AI Agents in Automated Scientific Discovery

Liu et al. [233] introduce a large-scale benchmark for evaluating the capability of large language models (LLMs) in generating high-quality scientific research hypotheses. It tack-les this gap by focusing on three pivotal sub-tasks: inspiration retrieval, hypothesis composition, and hypothesis ranking. The authors have developed an automated framework that extracts key components from scientific papers, including research questions, background surveys, inspirations, and hypotheses, across 12 disciplines. Expert validation ensures the reliability of this framework. By exclusively using papers published in 2024, the study minimizes data contamination from large lan-guage model (LLM) pretraining datasets, revealing that LLMs perform notably well in retrieving novel inspirations. This positions LLMs as promising “research hypothesis mines” that can facilitate the automation of scientific discovery by generating innovative hypotheses at scale. Despite these advances, significant challenges remain for AI agents employing LLMs to automate scientific discovery. One key obstacle is ensuring that these agents generate novel and scientifically valid hypotheses, as they must navigate the risk of producing biased or spurious associations without sufficient human oversight. Furthermore, the complexity and diversity of scientific literature across various disciplines demand that these agents not only understand domain-specific nuances but also adapt dynamically to evolving research contexts. The risk of data contamination, particularly when recent publications might overlap with pretraining data, further complicates the extraction of truly innovative insights. In addition, scaling these systems while preserving transparency, interpretability, and ethical standards poses a multifaceted challenge that must be addressed to harness the potential of AI-driven scientific discovery fully.

### D. Dynamic Tool Integration for Autonomous AI Agents

Wu et al. [234] introduce Chain-of-Tools, a novel tool learning approach that leverages the robust semantic represen-tation capabilities of frozen large language models (LLMs) to perform tool calling as part of a chain-of-thought reasoning process. By utilizing a vast and flexible tool pool that can include previously unseen tools, this method addresses the inefficiencies and highlights key challenges, including man-aging vast prompt-based demonstrations. The authors validate their approach on a range of datasets, including a newly

constructed dataset, SimpleToolQuestions, as well as GSM8K- XL, FuncQA, and KAMEL, demonstrating that Chain-of- Tools outperforms conventional baselines. Additionally, the method holds promise for enhancing autonomous AI agents by enabling them to select and utilize external tools dynamically, thereby broadening their capability to solve complex, multi-step tasks independently. This work prompts several questions: How can the integration of unseen tools further enhance LLM adaptability in diverse scenarios? What critical dimensions of the model output influence effective tool selection, and how can they be optimized for greater interpretability? More-over, how might this methodology be extended to enable more robust autonomous decision-making in AI agents facing increasingly complex reasoning challenges? Notably, these questions also underscore key challenges such as managing a huge tool pool, ensuring efficient tool selection, enhancing model interpretability, and integrating autonomous AI agents capable of dynamic, independent operation.

### E. Empowering LLM Agents with Integrated Search via Rein-forcement Learning
ReSearch [235] represents a significant step toward endow-ing LLM-based agents with the ability to decide autonomously when and how to consult external knowledge sources, seam-lessly weaving search operations into their reasoning chains via reinforcement learning. By framing search as an action-able tokenized operation rather than a separate retrieval step ReSearch trains models like Qwen2.5 through a reward signal that emphasizes final-answer accuracy and adherence to a structured think/search/result format. This paradigm eliminates the need for painstakingly annotated reasoning traces and yields strong multi-hop question–answering performance and cross-domain generalization. Yet, several challenges remain for deploying such agents in the wild: how to scale the ap-proach to richer, real-time toolsets (e.g., calculators, databases, code execution environments) without blowing up action spaces; how to design more nuanced reward functions that capture partial credit for intermediate reasoning or mitigate reward hacking; how to ensure robustness and interpretability when agents autonomously interleave reasoning and tool use; and how to balance exploration of novel tool sequences against exploitation of known effective patterns. Addressing these questions will be crucial for realizing truly versatile, trust-worthy LLM agents capable of complex, multi-step problem- solving.

### F. Vulnerabilities of AI Agents Protocols

MCP protocol standardizes how AI applications provide context to LLMs. The MCP protocol faces critical vulnera-bilities in Agent AI communications due to its fundamentally decentralized design [223]. Without a central authority over-seeing security, disparate implementation practices can lead to uneven defenses, making it easier for attackers to exploit weak links. In particular, the absence of a standardized authentica-tion mechanism across different nodes hinders reliable identity verification, thereby increasing the risk of unauthorized access and potential data breaches. Moreover, deficiencies in robust logging and debugging tools further complicate the timely detection of anomalies and errors, which is vital for preventing and mitigating attacks. Additionally, the complexity inherent in managing multi-step, distributed workflows can lead to state inconsistencies and operational glitches, amplifying the po-tential impact of a security compromise across interconnected systems.

## 6 Conclusion

In this paper, we have surveyed recent advances in large language model reasoning and autonomous AI agents, demon-strating that multi-step, intermediate processing, exposed through models such as DeepSeek-R1, OpenAI o1 and o3, and GPT-4o, yields marked improvements in accuracy and reliability across complex tasks in mathematics, code genera-tion and logical reasoning. We examined a range of training and inference strategies, including inference-time scaling, pure reinforcement learning (for example, DeepSeek-R1-Zero), su-pervised fine-tuning combined with reinforcement learning, and distillation-based fine-tuning. We demonstrated that hy-brids of these methods, applied to Qwen-32B and Llama- based architectures, foster emergent reasoning behaviors while curbing overthinking and verbosity. Our unified comparison of some 60 benchmarks from 2019 to 2025, organized into a structured taxonomy, highlights the impact of mixture-of-experts, retrieval-augmented generation, and reinforcement learning frameworks, as well as key architectural enhance-ments, on model performance. We also reviewed AI agent frameworks introduced between 2023 and 2025, illustrating their applications in materials science, biomedical research, synthetic data generation, and financial forecasting. Despite these successes, significant challenges remain, most notably automating multi-step reasoning without human oversight, balancing structured guidance with model flexibility, and inte-grating long-context retrieval at scale. We anticipate that future work will increasingly focus on domain- and application-specific optimizations, as early systems such as DeepSeek- R1-Distill, Sky-T1, and TinyZero begin to demonstrate how specialized reasoning systems can achieve optimal trade-offs between computational cost and accuracy.
</details>
</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>