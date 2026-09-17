# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?</summary>

Phase: [EXPLOITATION]

### Source [2]: https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents

Query: What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?

Answer: ControlFlow is an open-source framework for taming the complexity of AI workflows. Built on top of our next-generation Prefect 3.0 engine, ControlFlow provides a structured approach to managing complex, multi-agent AI processes without sacrificing flexibility or control. At its heart, ControlFlow revolves around three key concepts: Tasks: Discrete, observable steps that define what needs to be done. Agents: AI entities responsible for executing tasks, powered by LLMs. Flows: High-level containers that compose tasks and agents into entire AI-powered workflows.

-----

Phase: [EXPLOITATION]

### Source [3]: https://arxiv.org/html/2508.17281v2

Query: What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?

Answer: General-purpose systems. A growing body of work seeks to develop general-purpose agent frameworks that empower LLMs with reasoning, planning, and tool use capabilities. These systems support multitask environments, enhance collaboration with humans, and enable long-horizon planning through world knowledge and instruction tuning. Several benchmarks have been proposed to assess performance in data science, safety, and reasoning tasks, while architectures address self-improvement and causal reasoning. RL paradigms adapted to LLM further boost agent autonomy. LLMs align closely with the core properties of agents in AI, making them strong candidates for agent foundations. First, they demonstrate autonomy by performing tasks without granular instructions, adapting responses to input, and generating creative content independently. In terms of reactivity, LLMs can now handle multimodal inputs and interact with their environment using embodiment and tool integration, despite the latency caused by the textual reasoning stages. Their proactivity is seen in their ability to reason and plan when asked, including setting goals and decomposition of tasks in dynamic settings. Several frameworks have been adopted to implement LLM agents, facilitating reasoning, decision making, memory management, and action execution in single-agent and multi-agent contexts.

-----

Phase: [EXPLOITATION]

### Source [5]: https://arize.com/ai-agents/agent-frameworks

Query: What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?

Answer: When you build with LlamaIndex Workflows, flows often combine retrieval + reasoning + tool calls: first fetch relevant context, then plan with the model, then call tools or generate output. This hybrid of retrieval and LLM reasoning gives your agents grounding: output is tied to data, not hallucination. For teams working on document-heavy tasks, search, summarization, or knowledge-driven automation, this can reduce error rates and increase consistency. Because the workflow is partially deterministic (you control index queries, retrieval steps, and reasoning + tool calls), debugging and evaluation become more structured than with free-form chat agents. Although LlamaIndex doesn’t enforce a strict orchestration engine like a graph framework. Framework | Controller Behaviour (How control decisions are made) | Worker Behaviour (How actions run) | OpenAI Agents SDK | The runner owns the loop. It picks the next step based on LLM output, handoff rules, and session state. No custom routing logic. The behaviour itself runs on the Responses API running in tandem with OpenAI. | Workers are sub-agents or tools. Each invocation is one atomic step: model call, function call, or handoff. No parallelism.

-----

</details>

<details>
<summary>What reliability primitives like checkpointing and interrupts does LangGraph offer?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://reference.langchain.com/python/langgraph/types/interrupt

Query: What reliability primitives like checkpointing and interrupts does LangGraph offer?

Answer: The `interrupt` function in LangGraph raises a `GraphInterrupt` exception on first invocation in a node, halting execution and sending the provided `value` to the client. Resuming requires the `Command` primitive to specify a resume value. The graph resumes from the start of the node, re-executing logic. Multiple interrupts in a node match resume values by order, scoped to the task. Requires a checkpointer to persist state for human-in-the-loop workflows. Example shows usage with `InMemorySaver` checkpointer, `StateGraph`, and `Command` for resuming with human input like age.

-----

Phase: [EXPLOITATION]

### Source [7]: https://docs.langchain.com/oss/python/langgraph/persistence

Query: What reliability primitives like checkpointing and interrupts does LangGraph offer?

Answer: Checkpointing uses `BaseCheckpointSaver` implementations from standalone libraries. Persistence modes: "exit" (persist on graph exit for performance, no mid-execution recovery), "async" (async persistence with small crash risk). Enables human-in-the-loop by allowing state inspection, interrupts, approvals, and resumption after updates. Provides memory between interactions for repeated human inputs via thread IDs. Checkpointers needed for viewing state and resuming after human changes.

-----

Phase: [EXPLOITATION]

### Source [8]: https://docs.langchain.com/oss/javascript/langgraph/interrupts

Query: What reliability primitives like checkpointing and interrupts does LangGraph offer?

Answer: Interrupts pause execution at points to wait for external input, saving state via persistence and waiting indefinitely. Triggered by `interrupt()` in nodes, accepting JSON-serializable value surfaced to caller. Resume via `Command` re-invoking graph. Dynamic vs static breakpoints. Requires checkpointer and thread ID. Checkpointing writes exact state for resumption even in errors. Interrupt payloads in `__interrupt__` field. Thread ID as persistent cursor for resuming checkpoints.

-----

</details>

<details>
<summary>What is the core philosophy of the Claude Agent SDK?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai

Query: What is the core philosophy of the Claude Agent SDK?

Answer: The Claude Agent SDK refers to Anthropic’s official client libraries — primarily the anthropic Python and TypeScript packages — used to build agentic applications with Claude. The SDK exposes the full Anthropic Messages API, including tool use, streaming, extended thinking, prompt caching, and the Batch API. Developers use it to build agents by writing their own orchestration logic, message history management, and tool dispatch on top of the client library.

-----

Phase: [EXPLOITATION]

### Source [12]: https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from

Query: What is the core philosophy of the Claude Agent SDK?

Answer: The Claude Agent SDK solves a specific architectural problem: how do you build an agent system where Anthropic maintains the runtime while you control the logic? Native MCP support means tools are first-class citizens. Built-in permissions and hooks distinguish the SDK from general-purpose frameworks. The canUseTool callback and declarative allow/deny rules are core features.

-----

</details>

<details>
<summary>How does FastMCP enable tool portability across runtimes like LangGraph?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://generect.com/blog/langgraph-mcp

Query: How does FastMCP enable tool portability across runtimes like LangGraph?

Answer: FastMCP enables tool portability by automatically generating schemas and handling validation, allowing LangGraph to discover and call tools via the MCP protocol. It simplifies server setup and supports multiple transport methods. FastMCP takes care of everything else: starting the listener, exposing the tools, and speaking the MCP protocol. LangGraph can now discover and call those tools, just like it would any other service. @mcp.tool() Decorate a function Marks it as a callable tool for the client. Type hints Add types like a: int and -> int Enables automatic schema generation. Docstring Write a 1-line description Helps agents understand tool behavior. FastMCP(“Name”) Create a named server Registers your toolset under that name. mcp.run() Start the server Opens the tool to clients (via stdio or HTTP). FastMCP will handle schema generation, validation, and everything in between. You don’t need to write separate code for each transport; just pass a flag when starting the server. mcp.run() or mcp.run(transport=“http”, host=”0.0.0.0”, port=8000).

-----

Phase: [EXPLOITATION]

### Source [15]: https://gofastmcp.com/servers/tools

Query: How does FastMCP enable tool portability across runtimes like LangGraph?

Answer: By default, FastMCP converts Python functions into MCP tools by inspecting the function’s signature and type annotations. This allows you to use standard Python type annotations for your tools. In general, the framework strives to “just work”: idiomatic Python behaviors like parameter defaults and type annotations are automatically translated into MCP schemas. For reusable serialization across multiple tools, create a wrapper decorator that returns ToolResult. This lets you compose serializers with other behaviors (logging, validation, caching) and keeps the serialization visible at the tool definition. By default, FastMCP uses Pydantic’s flexible validation that coerces compatible inputs to match your type annotations. This improves compatibility with LLM clients that may send string representations of values (like "10" for an integer parameter).

-----

Phase: [EXPLOITATION]

### Source [16]: https://github.com/PrefectHQ/fastmcp

Query: How does FastMCP enable tool portability across runtimes like LangGraph?

Answer: Building an effective MCP application is harder than it looks. FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. Connect to a server with a URL, and transport negotiation, authentication, and protocol lifecycle are managed for you. You focus on your logic, and the MCP part just works: with FastMCP, best practices are built in. FastMCP has three pillars: Servers Expose tools, resources, and prompts to LLMs. Clients Connect to any MCP server — local or remote, programmatic or CLI. Servers wrap your Python functions into MCP-compliant tools, resources, and prompts. Clients connect to any server with full protocol support.

-----

</details>

<details>
<summary>What are the main components of OpenAI AgentKit including visual builder and MCP connectors?</summary>

Phase: [EXPLOITATION]

### Source [17]: https://openai.com/index/introducing-agentkit

Query: What are the main components of OpenAI AgentKit including visual builder and MCP connectors?

Answer: Today we’re launching AgentKit, a complete set of tools for developers and enterprises to build, deploy, and optimize agents. With AgentKit, developers can now design workflows visually and embed agentic UIs faster using new building blocks like: Agent Builder: a visual canvas for creating and versioning multi-agent workflows. Connector Registry: a central place for admins to manage how data and tools connect across OpenAI products. ChatKit: a toolkit for embedding customizable chat-based agent experiences in your product. Builders can get started with a blank canvas or with prebuilt templates. We’re also launching a Connector Registry for enterprises to govern and maintain data across multiple workspaces and organizations. The Connector Registry consolidates data sources into a single admin panel across ChatGPT and the API. The registry includes all pre-built connectors like Dropbox, Google Drive, Sharepoint, and Microsoft Teams, as well as third-party MCPs.

-----

Phase: [EXPLOITATION]

### Source [18]: https://www.digitalapplied.com/blog/openai-agentkit-complete-guide

Query: What are the main components of OpenAI AgentKit including visual builder and MCP connectors?

Answer: AgentKit provides the components you need to build production-ready agents quickly. The visual Agent Builder eliminates complex coding, ChatKit handles all UI concerns, the Connector Registry simplifies data integration, and Evals ensure your agents improve over time. Drag-and-drop interface for building multi-agent workflows with nodes, tools, and guardrails. Includes preview runs, inline eval configuration, and full versioning. Simple embeddable chat interface that handles streaming responses, manages threads, shows model thinking, and provides engaging in-chat experiences. Consolidates data sources into a single admin panel across ChatGPT and API. Includes pre-built connectors and third-party MCP support. Four evaluation capabilities: datasets, trace grading, automated prompt optimization, and third-party model support. AgentKit consists of four interconnected components that work together to provide a complete agent development platform.

-----

Phase: [EXPLOITATION]

### Source [19]: https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents

Query: What are the main components of OpenAI AgentKit including visual builder and MCP connectors?

Answer: At the center of AgentKit is Agent Builder, a visual drag-and-drop canvas for designing agent workflows. Developers can chain together multiple AI components, connect to APIs or SaaS tools, and apply logic like conditional branching and guardrails—all without writing extensive orchestration code. AgentKit also includes a Connector Registry for managing integrations with data sources like Google Drive or Dropbox, and ChatKit, which makes it easy to embed an interactive chat interface in any app or website. AgentKit is OpenAI’s new suite of tools designed to help developers and enterprises build, deploy, and manage AI agents. It consolidates capabilities that were previously scattered across APIs and frameworks, giving teams an end-to-end environment to create agents that can act autonomously.

-----

Phase: [EXPLOITATION]

### Source [21]: https://composio.dev/content/openai-agent-builder-step-by-step-guide-to-building-ai-agents-with-mcp

Query: What are the main components of OpenAI AgentKit including visual builder and MCP connectors?

Answer: Agent Builder: A visual drag-and-drop canvas for building agents. ChatKit: A toolkit to embed a chat-based agent in your product. Connector registry: A central place for managing how tools connect across ChatGPT. Guardrail nodes, which help with moderation, PII detection, and hallucination mitigation. MCP nodes, to integrate external tools/services (via MCP servers) rather than building all integrations manually. The ability to export your workflow logic into code (TypeScript/Python) if you want to move beyond the visual builder into custom code. Agent Builder is a visual workflow tool from OpenAI where you build AI agents by connecting drag-and-drop nodes (Start, Guardrail, Agent, MCP, etc).

-----

</details>

<details>
<summary>What is CrewAI dual architecture of crews versus flows?</summary>

Phase: [EXPLOITATION]

### Source [22]: https://docs.crewai.com/en/introduction

Query: What is CrewAI dual architecture of crews versus flows?

Answer: CrewAI is the leading open-source framework for orchestrating autonomous AI agents and building complex workflows. It empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence of Crews with the precise control of Flows. CrewAI Flows: The backbone of your AI application. Flows allow you to create structured, event-driven workflows that manage state and control execution. They provide the scaffolding for your AI agents to work within. CrewAI Crews: The units of work within your Flow. Crews are teams of autonomous agents that collaborate to solve specific tasks delegated to them by the Flow. When to Use Crews vs. Flows: The short answer: Use both. For any production-ready application, start with a Flow. Use a Flow to define the overall structure, state, and logic of your application. Use a Crew within a Flow step when you need a team of agents to perform a specific, complex task that requires autonomy. Use Cases: Simple Automation - Single Flow with Python tasks; Complex Research - Flow managing state -> Crew performing research; Application Backend - Flow handling API requests -> Crew generating content -> Flow saving to DB. The CrewAI Architecture: CrewAI’s architecture is designed to balance autonomy with control. 1. Flows: The Backbone - Think of a Flow as the “manager” or the “process definition” of your application. It defines the steps, the logic, and how data moves through your system.

-----

Phase: [EXPLOITATION]

### Source [24]: https://vadim.blog/crewai-unique-features

Query: What is CrewAI dual architecture of crews versus flows?

Answer: CrewAI's real uniqueness is that it models problems as "build a team of people" rather than "build a graph of nodes" (LangGraph) or "build a conversation" (AutoGen). The Crews + Flows dual-layer architecture is the core differentiator. The role-playing persona system and autonomous delegation are ergonomic wins, not technical breakthroughs. The hierarchical manager is conceptually appealing but broken in practice. The Bottom Line: Strip away the marketing, and CrewAI's genuine contribution to the multi-agent ecosystem is one architectural insight: separate deterministic orchestration (Flows) from autonomous reasoning (Crews), and give developers both as first-class primitives. Crews + Flows is the only feature on this page that justifies CrewAI's existence as a separate framework. The idea that your deterministic pipeline and your autonomous agents should live in different abstraction layers, composed together? That’s a genuine architectural insight. CrewAI lets it be a Python function.

-----

Phase: [EXPLOITATION]

### Source [25]: https://github.com/crewaiinc/crewai

Query: What is CrewAI dual architecture of crews versus flows?

Answer: Q: What makes Crews different from Flows? A: Crews provide autonomous agent collaboration, ideal for tasks requiring flexible decision-making and dynamic interaction. Flows offer precise, event-driven control, ideal for managing detailed execution paths and secure state management. You can seamlessly combine both for maximum effectiveness. This example demonstrates how to: 1. Use Python code for basic data operations 2. Create and execute Crews as steps in your workflow 3. Use Flow decorators to manage the sequence of operations 4. Implement conditional branching based on Crew results.

-----

Phase: [EXPLOITATION]

### Source [26]: https://docs.crewai.com/en/concepts/flows

Query: What is CrewAI dual architecture of crews versus flows?

Answer: Flow Output: Accessing and handling the output of a Flow is essential for integrating your AI workflows into larger applications or systems. CrewAI Flows provide straightforward mechanisms to retrieve the final output, access intermediate results, and manage the overall state of your Flow. Retrieving the Final Output: When you run a Flow, the final output is determined by the last method that completes. The kickoff() method returns the output of this final method. Flow State Management: Managing state effectively is crucial for building reliable and maintainable AI workflows. CrewAI Flows provides robust mechanisms for both unstructured and structured state management, allowing developers to choose the approach that best fits their application’s needs. Unstructured State Management. Structured State Management: Structured state management leverages predefined schemas to ensure consistency and type safety across the workflow. By using models like Pydantic’s BaseModel, developers can define the exact shape of the state, enabling better validation and auto-completion in development environments. Each state in CrewAI Flows automatically receives a unique identifier (UUID) to help track and manage state instances.

-----

</details>

<details>
<summary>How does PydanticAI use type hints for schema-driven validation?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://realpython.com/pydantic-ai

Query: How does PydanticAI use type hints for schema-driven validation?

Answer: The `CityInfo` class inherits from `BaseModel` and defines the data schema for the agent’s response. Each field has a type hint: `name` and `country` are strings, `population` is an integer, and `fun_fact` is also a string. When you pass `CityInfo` to the `Agent` using the `output_type` argument, Pydantic AI instructs the language model to return data that matches the provided schema. Behind the scenes, Pydantic AI converts your Pydantic model, `CityInfo`, into a JSON schema that the LLM understands. The language model generates a response matching this schema, and Pydantic validates it. Pydantic AI is a Python framework for building LLM agents that return validated, structured outputs using Pydantic models. Instead of parsing raw strings from LLMs, you get type-safe objects with automatic validation. If you’ve used FastAPI or Pydantic before, then you’ll recognize the familiar pattern of defining schemas with type hints and letting the framework handle the type validation for you. The `deps_type` argument to `Agent` specifies the type of dependency the agent should expect. Inside `fetch_user()`, you access this dependency via `.deps` on the runtime context. The `ctx: RunContext[UserDatabase]` type hint specifies the context type and the dependency type in square brackets. This gives you full type safety. Note: Use `@agent.tool` when your tool needs access to the run context, like in `fetch_user()`, and `@agent.tool_plain` when it doesn’t. Then, you create an instance of `UserDatabase` and pass it to the agent using the `deps` argument. This way, you inject the required database connection. Pydantic AI validates whether the dependency matches the expected type.

-----

Phase: [EXPLOITATION]

### Source [29]: https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html

Query: How does PydanticAI use type hints for schema-driven validation?

Answer: pydantic reads the type annotations assigned to the variables, and then validates the incoming arguments against those types. Because we made sure we were thorough enough with our type hints in the Manual Data Validation, our type annotations correctly capture the correct data. We also now have simultaneous validation of multiple entries. In Manual Data Validation, our validation code would throw the first error it found, without validating everything else. Here, pydantic is validating everything all at once, and raising it at the end. A data validation and settings management tool which leverages existing Python type hints to handle validation for you. pydantic is not the only possible solution out there for validation of Python data and schema, but it is a natural extension of the type hints and `dataclass` we’ve already discussed. To start, let’s convert our `Molecule` from a `dataclass` to a pydantic `BaseModel` by importing `BaseModel`, subclassing `BaseModel` into our `Molecule`, and removing the `dataclass` decorator. At this point we don’t even need the `dataclasses` import, so lets remove it as well.

-----

Phase: [EXPLOITATION]

### Source [30]: https://pydantic.dev/docs/validation/latest/concepts/validators

Query: How does PydanticAI use type hints for schema-driven validation?

Answer: Consider the following example: `from typing import Any from pydantic import BaseModel, field_validator class Model(BaseModel): value: str @field_validator('value', mode='before') @classmethod def cast_ints(cls, value: Any) -> Any: if isinstance(value, int): return str(value) else: return value print(Model(value='a')) #> value='a' print(Model(value=1)) #> value='1'` While the type hint for `value` is `str`, the `cast_ints` validator also allows integers. To specify the correct input type, the `json_schema_input_type` argument can be provided. Notice the use of `Any` as a type hint for `data`. Before validators take the raw input, which can be anything. Most of the time, the input data will be a dictionary (e.g. when calling `UserModel(username='...')`). However, this is not always the case. For instance, if the `from_attributes` configuration value is set, you might receive an arbitrary class instance for the `data` argument. Wrap validators: are the most flexible of all. You can run code before or after Pydantic and other validators process the input data, or you can terminate validation immediately, either by returning the data early or by raising an error. `from typing import Annotated, Any from pydantic import BaseModel, BeforeValidator, ValidationError def ensure_list(value: Any) -> Any: if not isinstance(value, list): return [value] else: return value class Model(BaseModel): numbers: Annotated[list[int], BeforeValidator(ensure_list)] print(Model(numbers=2)) #> numbers= try: Model(numbers='str') except ValidationError as err: print(err)

-----

</details>

<details>
<summary>What is AutoGen layered design with Studio AgentChat Core?</summary>

Phase: [EXPLOITATION]

### Source [32]: https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems

Query: What is AutoGen layered design with Studio AgentChat Core?

Answer: AutoGen’s architecture is modular and layered for flexibility. Internally, it is organized into a hierarchy of components that developers can leverage at different abstraction levels. The foundational Core API handles low-level capabilities like message passing between agents and an event-driven runtime. Building on this is the AgentChat API, a higher-level, opinionated interface geared toward rapid prototyping of common multi-agent patterns. Finally, an Extensions API allows integration of specific tools and LLM backends to expand agent capabilities. This layered design means you can dip down to fine-grained control or stay at a high level, depending on your needs. It also promotes extensibility: new agent types, tools, or model backends can be added without modifying the core.

-----

Phase: [EXPLOITATION]

### Source [33]: https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications

Query: What is AutoGen layered design with Studio AgentChat Core?

Answer: This release features a layered architecture with all foundational building blocks for an event-driven system as the core package. The AgentChat layer builds upon the core layer, providing a task-driven API for group chat and code execution, as well as pre-built agents. The extensions layer provides implementations for core interfaces and third-party integrations. This is where all the model clients are implemented. The AutoGen Studio is a low-code interface that enables the rapid prototyping of AI agents, and AutoGen Bench provides developers with tools to benchmark agents’ performance across different tasks and environments.

-----

Phase: [EXPLOITATION]

### Source [34]: https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness

Query: What is AutoGen layered design with Studio AgentChat Core?

Answer: Core: The foundational building blocks for an event-driven agentic system. AgentChat: A task-driven, high-level API built on the core layer, featuring group chat, code execution, pre-built agents, and more. This layer is most similar to AutoGen v0.2 (opens in new tab), making it the easiest API to migrate to. Extensions: Implementations of core interfaces and third-party integrations, such as the Azure code executor and OpenAI model client. Figure 1. The v0.4 update introduces a cohesive AutoGen ecosystem that includes the framework, developer tools, and applications. The framework’s layered architecture clearly defines each layer’s functionality. It supports both first-party and third-party applications and extensions. AutoGen Studio (opens in new tab): Rebuilt on the v0.4 AgentChat API, this low-code interface enables rapid prototyping of AI agents.

-----

Phase: [EXPLOITATION]

### Source [35]: https://www.ibm.com/think/topics/autogen

Query: What is AutoGen layered design with Studio AgentChat Core?

Answer: AutoGen is composed of three main layers. The core layer: Core is AutoGen’s foundational layer, the basic plumbing and wiring that makes the AutoGen framework function. In Microsoft’s language, “Core API implements message passing, event-driven agents, and local and distributed runtime.” In other words, it allows the agents to talk to each other, empowers them to wake up upon certain event triggers and enables them to run locally on your computer or across various servers. The AgentChat layer: If Core is plumbing and wiring, AgentChat is something like a prefab home with built-in fixtures. AgentChat presumes (based on prevailing use cases) that most people want AI agents to be able to chat to humans and other bots (in technical terms, to be “conversable agents”).

-----

</details>

<details>
<summary>What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?</summary>

Phase: [EXPLOITATION]

### Source [37]: https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps

Query: What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?

Answer: The OpenAI Agents SDK uses Agents, Tools, Handoffs, Guardrails, and Sessions as primitives. These components help manage interactions, delegate tasks, enforce safety checks, and maintain state. OpenAI’s Agents SDK is a lightweight framework for building agentic apps with minimal abstractions. You model Agents (LLMs with instructions and tools), connect them via Handoffs, add Guardrails to keep them safe, and plug in Sessions to remember state. It’s provider-agnostic: use OpenAI Responses or Chat Completions—and via LiteLLM, 100+ non-OpenAI models—without changing your app’s architecture.

-----

Phase: [EXPLOITATION]

### Source [38]: https://openai.github.io/openai-agents-python/agents

Query: What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?

Answer: Agents are the core building block in your apps. An agent is a large language model (LLM) configured with instructions, tools, and optional runtime behavior such as handoffs, guardrails, and structured outputs. Handoffs are sub‑agents the agent can delegate to. When a handoff occurs, the delegated agent receives the conversation history and takes over the conversation. This pattern enables modular, specialized agents that excel at a single task.

-----

Phase: [EXPLOITATION]

### Source [39]: https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk

Query: What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?

Answer: Port an OpenAI Agents SDK app to the Claude Agent SDK, mapping each primitive (tools, guardrails, sessions, handoffs) through a single expense-approval agent example. `Agent(name, instructions, tools)` `ClaudeAgentOptions` `@function_tool` `@tool` `create_sdk_mcp_server` `@input_guardrail` `UserPromptSubmit` `@output_guardrail` `ResultMessage.result` `Runner.run(agent, msg)` `ClaudeSDKClient` `Sessions` `ClaudeSDKClient` `conversation_id` `resume=session_id` `handoffs=[...]` `AgentDefinition`

-----

Phase: [EXPLOITATION]

### Source [40]: https://openai.github.io/openai-agents-python/guardrails

Query: What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?

Answer: Guardrails enable you to do checks and validations of user input and agent output. There are two kinds of guardrails: input guardrails and output guardrails. Guardrails are attached to agents and tools, but they do not all run at the same points in a workflow. Input guardrails run in 3 steps. If you need checks around each custom function-tool call in a workflow that includes managers, handoffs, or delegated specialists, use tool guardrails instead of relying only on agent-level input/output guardrails.

-----

Phase: [EXPLOITATION]

### Source [41]: https://developers.openai.com/api/docs/guides/agents

Query: What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?

Answer: A typical SDK reading order is: Start with Quickstart to get one working run on screen. Use Agent definitions and Models and providers to shape one specialist cleanly. Continue to Running agents, Orchestration and handoffs, and Guardrails and human review as the workflow grows more complex. Use Results and state and Integrations and observability when application logic depends on the run object or deeper visibility into behavior.

-----

</details>

<details>
<summary>What are LangGraph graph API versus functional API styles?</summary>

Phase: [EXPLOITATION]

### Source [43]: https://www.langchain.com/blog/introducing-the-langgraph-functional-api

Query: What are LangGraph graph API versus functional API styles?

Answer: The Functional API and the Graph APIs (StateGraph) provide two different paradigms to create in LangGraph. The Functional API consists of two decorators -- `entrypoint` and `task` -- which allow you to define workflows using standard functions, and use regular loops and conditionals to control the flow of execution. This makes it easy to adopt LangGraph's features in your existing applications without having to restructure your code. This API is complementary to the Graph API (StateGraph) and can be used in conjunction with it as both APIs use the same underlying runtime. This allows you to mix and match the two paradigms to create complex workflows that leverage the best of both worlds.

-----

Phase: [EXPLOITATION]

### Source [44]: https://blog.langchain.com/introducing-the-langgraph-functional-api

Query: What are LangGraph graph API versus functional API styles?

Answer: Time-travel: In the Graph API checkpoints are more granular being generated after every node execution (or group of nodes if some nodes are being executed in parallel). In the Functional API checkpoints are generated after every entrypoint execution. When tasks are executed they update the existing checkpoint associated with the entrypoint, but it does not generate a new checkpoint. As a result, time-travel is better supported in the Graph API. Visualization: The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization since the execution flow is dynamically generated at run time.

-----

Phase: [EXPLOITATION]

### Source [45]: https://docs.langchain.com/oss/python/langgraph/choosing-apis

Query: What are LangGraph graph API versus functional API styles?

Answer: LangGraph provides two different APIs to build agent workflows: the Graph API and the Functional API. Both APIs share the same underlying runtime and can be used together in the same application, but they are designed for different use cases and development preferences. Choose the Graph API when you need explicit control over workflow structure, complex branching, parallel processing, or team collaboration benefits. Choose the Functional API when you want to add LangGraph features to existing code with minimal changes, have simple linear workflows, or need rapid prototyping capabilities. Both APIs provide the same core LangGraph features (persistence, streaming, human-in-the-loop, memory) but package them in different paradigms to suit different development styles and use cases.

-----

Phase: [EXPLOITATION]

### Source [46]: https://changelog.langchain.com/announcements/functional-api-for-langgraph

Query: What are LangGraph graph API versus functional API styles?

Answer: With the new Functional API, you can now use these capabilities without explicitly defining a graph. Whether you're using LangGraph within a different framework or as a standalone tool, this API makes it easier than ever to build AI workflows. Graph + Functional API = Best of both worlds – Mix and match paradigms to build robust AI systems. Works anywhere – Use LangGraph’s features in any app, no graph syntax required. Seamless state management – Keep track of user inputs, workflow progress, and historical context. Human-in-the-loop support – Pause workflows, collect feedback, and resume dynamically. Streaming-first – Stream updates in real-time for responsive AI interactions.

-----

</details>

<details>
<summary>What are runtime protocol and tooling layers in AI agent frameworks?</summary>

Phase: [EXPLOITATION]

### Source [48]: https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer

Query: What are runtime protocol and tooling layers in AI agent frameworks?

Answer: The missing layer is the agent execution runtime: the machinery that keeps an agent running, recoverable, and isolated from other agents in a shared production environment. Frameworks like LangChain, CrewAI, and AutoGen provide prompts and tools for building AI agents. Their standard offerings rarely supply durable execution, process isolation, resource governance, or multi-tenant security. An agent runtime is the infrastructure layer that provides execution-time intervention: the capacity to modify agent inputs, control flow, or execution state while the agent is actively running. The runtime layer manages seven distinct concerns.

-----

Phase: [EXPLOITATION]

### Source [49]: https://www.guild.ai/glossary/ai-agent-runtime

Query: What are runtime protocol and tooling layers in AI agent frameworks?

Answer: AI agent runtimes provide the infrastructure for executing AI agents. Runtimes handle orchestration, state management, security, and integration. AI agent frameworks focus on building agents and offer tools for reasoning, memory, and workflows. Frameworks most often need pairing with a separate runtime for production deployment. Agent runtimes provide the tooling for running agents in production. Supported tools may include: durable execution, streaming, human-in-the-loop support to incorporate human oversight by inspecting and modifying agent state, and persistence for thread-level and cross-thread state management.

-----

Phase: [EXPLOITATION]

### Source [50]: https://arize.com/ai-agents/agent-frameworks

Query: What are runtime protocol and tooling layers in AI agent frameworks?

Answer: AgentCore works with any framework because it doesn’t enforce a planning or execution model. The runtime exposes a stable API surface, typed inputs, environment configuration, and IAM-based security. AWS Bedrock AgentCore is the runtime layer for teams that want to run agents in production without handling infrastructure. You ship your agent as a container, and AgentCore takes care of autoscaling, routing, deployment, and model access.

-----

Phase: [EXPLOITATION]

### Source [51]: https://forum.langchain.com/t/what-does-the-emerging-ai-agent-stack-actually-look-like/3103

Query: What are runtime protocol and tooling layers in AI agent frameworks?

Answer: Right now most discussions focus on frameworks: LangChain, CrewAI, AutoGen. But when building real systems it feels like several layers are emerging: Application layer, Agent framework (task orchestration, planning), Identity / persona layer, Execution layer (tool calls, runtime environment), Verification / governance, Infrastructure.

-----

</details>

<details>
<summary>What is abstraction level versus developer experience axis for agent frameworks?</summary>

Phase: [EXPLOITATION]

### Source [52]: https://www.langchain.com/resources/ai-agent-frameworks

Query: What is abstraction level versus developer experience axis for agent frameworks?

Answer: The best agent frameworks give developers clear primitives for tool calling, state management, and inter-agent communication without hiding what's happening underneath. Abstraction is only useful when it accelerates the right decisions; abstraction that obscures failure modes costs more in debugging time than it saves in setup time, which is why the most trusted frameworks expose enough internals to reason about agent behavior at every step. The OpenAI Agents SDK is a lightweight, low-abstraction framework for building multi-agent workflows using OpenAI's model APIs. Its design philosophy favors minimal API surface over comprehensive abstractions: the core primitives for agent handoffs, tool calling, and delegation are clean and easy to reason about, which makes it faster to understand what an agent is doing than with heavier orchestration stacks.

-----

Phase: [EXPLOITATION]

### Source [53]: https://www.langchain.com/blog/how-to-think-about-agent-frameworks

Query: What is abstraction level versus developer experience axis for agent frameworks?

Answer: Frameworks are generically useful because they contain useful abstractions which make it easy to get started and provide a common way for engineers to build, making it easier to onboard and maintain projects. As mentioned above, there are real downsides to agent abstractions as well. Most agent frameworks contain an agent abstraction. They usually start as a class that involves a prompt, model, and tools. Then they add in a few more parameters… then a few more… then even more. Eventually you end up with a litany of parameters that control a multitude of behaviors, all abstracted behind a class. If you want to see what’s going on, or change the logic, you have to go into the class and modify the source code. With Agents SDK you write their abstractions. With LangGraph you write a large amount of normal code.

-----

Phase: [EXPLOITATION]

### Source [54]: https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d

Query: What is abstraction level versus developer experience axis for agent frameworks?

Answer: Weaknesses: Because it’s minimal, the Agents SDK has a relatively small core compared to LangChain or ADK. You won’t find a visual editor or pre-bundled agents; you add whatever tools you need. Some tasks (like heavy parallelism, custom orchestration, or very specialized patterns) require manual coding. It also lacks the out-of-the-box common-pattern library that ADK provides. Developer experience is mostly driven by writing Python; while that’s flexible, there’s no visual debugging UI (though trace logs help). In summary, it trades off less structure for ease of learning and speed of prototyping. The SDK is “great if you want a lightweight solution that leverages OpenAI’s models and you’re okay with a code-centric approach”. CrewAI (Python): Focused on role-based teams, CrewAI structures agents into Crews and Flows. A Crew is like an organization: a top-level manager with multiple AI agents, each having a defined role (e.g., researcher, writer) and tools. Unlike LangChain, CrewAI provides higher-level abstractions out of the box: you mostly specify roles, tools, and inter-agent message patterns, and the framework handles the rest. This can accelerate the development of agent teams, but at the cost of less control.

-----

</details>

<details>
<summary>How do GitHub stars and download trends measure agent framework maturity?</summary>

Phase: [EXPLOITATION]

### Source [56]: https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b

Query: How do GitHub stars and download trends measure agent framework maturity?

Answer: GitHub stars are a strong indicator of developer trust and community adoption. Here are the top 10 most starred AI agent frameworks heading into 2026. 1. LangChain ⭐ 122,850 langchain-ai/langchain | Python | MIT The most popular framework for building LLM-powered applications, with extensive tooling for chains, agents, and retrieval. 2. MetaGPT ⭐ 61,919 FoundationAgents/MetaGPT | Python | MIT A multi-agent framework that simulates a software company, with agents taking on roles like product manager, architect, and engineer. 3. AutoGen ⭐ 52,927 microsoft/autogen | Python | CC-BY-4.0 Microsoft’s framework for building multi-agent conversational systems with customizable agent behaviors. 4. LlamaIndex ⭐ 46,100

-----

Phase: [EXPLOITATION]

### Source [57]: https://arxiv.org/html/2510.25423v2

Query: How do GitHub stars and download trends measure agent framework maturity?

Answer: We started with seven core Agent frameworks that came up most often on our Stack Overflow analysis: langchain, langgraph, crewAI, Flowise, llama_index, semantic-kernel, and autogen. These frameworks formed the starting point for choosing which repositories to include. Building on earlier software engineering research Braiek et al. (2018), we used the number of stars a repository has as a stand-in for how widely it’s used and how important it is in the ecosystem. With the official GitHub REST API, we searched for repositories tagged with Agent and Agents in GitHub Topics, keeping the top five for each topic based on stars. To cover more programming languages than just Python, we also included JetBrains/koog to represent Agent development in Java and Kotlin. In total, we selected 18 repositories. From these repositories, we gathered 67,193 issues. After removing issues that were empty, one-word, or not in English, we ended up with a final set of 64,098 GitHub issues.

-----

</details>

<details>
<summary>How does LangGraph differ from LangChain in the ecosystem?</summary>

Phase: [EXPLOITATION]

### Source [59]: https://www.truefoundry.com/blog/langchain-vs-langgraph

Query: How does LangGraph differ from LangChain in the ecosystem?

Answer: LangChain is the fast, approachable option for simple to moderately complex workflows. LangGraph is the robust, flexible choice for high-complexity, dynamic AI systems. Both are part of the same ecosystem, so you can start with one and transition to the other if your needs change. LangChain has quickly become one of the most popular libraries for creating AI-driven applications, offering a wide ecosystem of integrations and abstractions. On the other hand, LangGraph—built on top of LangChain—focuses on stateful, agent-like systems, using a graph-based execution model to handle complex reasoning and multi-step interactions. LangChain is ideal for simpler, linear workflows that benefit from rapid prototyping and extensive integrations, while LangGraph is designed for complex, adaptive, and stateful agent systems.

-----

Phase: [EXPLOITATION]

### Source [60]: https://duplocloud.com/blog/langchain-vs-langgraph

Query: How does LangGraph differ from LangChain in the ecosystem?

Answer: Both LangChain and LangGraph are open-source frameworks from the LangChain ecosystem that sound similar but play very different roles in the AI orchestra. LangChain is your quick-and-dirty tool for linear, no-fuss AI apps, perfect for getting a prototype out the door. LangGraph is the master strategist, ready to tackle complex, stateful, multi-agent workflows with the precision of a seasoned developer. LangGraph has a steeper learning curve due to its graph-based approach and explicit state management. Key Difference: LangChain is simpler and faster for beginners or simple tasks. LangGraph requires more upfront effort but offers unmatched control for complex systems.

-----

Phase: [EXPLOITATION]

### Source [61]: https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow

Query: How does LangGraph differ from LangChain in the ecosystem?

Answer: LangChain helps us build the steps. LangGraph helps us orchestrate these steps when things get complex. LangChain is a modular framework for building LLM‑powered applications. It gives us building blocks - prompts, models, memory, tools, retrievers - and a simple way to chain them into a pipeline using its Runnable/LCEL APIs. LangGraph is a graph-based layer for complex, stateful, branching/looping flows with robust control. LangGraph builds on the LangChain ecosystem (models, tools, memory). Typically, we use them together with LangGraph handling orchestration.

-----

Phase: [EXPLOITATION]

### Source [62]: https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph

Query: How does LangGraph differ from LangChain in the ecosystem?

Answer: LangChain connects steps in order for structured, multi step reasoning and works in a straight, step by step manner. LangGraph builds flexible workflows using graph style task flow and supports parallel, conditional and adaptive paths. LangChain has limited flexibility with fixed order of steps and is simple to use for straightforward tasks. LangGraph is very adaptable with loops, branches and complex logic and requires more advanced setup for complex workflows. LangChain is great for straightforward API and tool integration while LangGraph offers richer support for complex, interconnected systems.

-----

Phase: [EXPLOITATION]

### Source [63]: https://milvus.io/blog/langchain-vs-langgraph.md

Query: How does LangGraph differ from LangChain in the ecosystem?

Answer: LangChain focuses on component orchestration and workflow automation, making it a good fit for common use cases like retrieval-augmented generation (RAG). LangGraph builds on top of LangChain with a graph-based architecture, which is better suited for stateful applications, complex decision-making, and multi-agent coordination. LangChain gives you a solid foundation of components and LCEL orchestration — great for quick prototypes, stateless tasks, or projects that just need clean input-to-output flows. LangGraph steps in when your application outgrows that linear model and requires state, branching, or multiple agents working together. LangGraph is a specialized extension of LangChain that focuses on stateful applications. Instead of writing workflows as a linear script, you define them as a graph of nodes and edges — essentially a state machine.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What theoretical foundations underpin explicit control-flow versus LLM autonomy trade-offs?</summary>

Phase: [EXPLORATION]

### Source [65]: https://arxiv.org/html/2603.03655v1

Query: What theoretical foundations underpin explicit control-flow versus LLM autonomy trade-offs?

Answer: Underpinning the execution is the Workflow Plane (Layer B), which materializes abstract scientific protocols into executable artifacts. We encapsulate the canonical drug discovery pipeline—from Target Identification to Lead Optimization—into composable, state-aware Skill Graphs. Unlike independent tool calls, which often suffer from state-loss or I/O mismatch, these Skill Graphs function as directed acyclic graphs (DAGs) that enforce valid data flow and scientific logic (e.g., ensuring a protein structure is rigorously prepared before docking). By grounding the LLM’s reasoning within these explicit graph-based constraints, Mozi mitigates the risks of hallucination and trajectory drift inherent in purely generation-based systems. Graph-based orchestration and state machines provide explicit control flow and recoverability, adding structure to LLM flexibility. We encode supervisor workflows and skills as graphs with explicit state interfaces for modular composition.

-----

Phase: [EXPLORATION]

### Source [67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC13079118

Query: What theoretical foundations underpin explicit control-flow versus LLM autonomy trade-offs?

Answer: LLMs utilize non-deterministic algorithms, meaning their outputs are not fixed even with the same input. Factors such as the temperature parameter and random seed influence the generated text. Furthermore, controlling reproducibility is only possible in some LLM implementations, as not all providers expose parameters such as random seed control or fully deterministic decoding options. This lack of reproducibility is a major challenge for using LLMs in regulated or controlled environments, such as pharmaceutical pharmacovigilance (GxP), where consistent results are a prerequisite for system validation. While this characteristic is beneficial for tasks requiring creativity, it introduces challenges for IE tasks, where consistent and reproducible results are paramount.

-----

Phase: [EXPLORATION]

### Source [68]: https://medium.com/@sumitqeunboxed/understanding-llm-flows-vs-ai-agents-clarifying-the-critical-architectural-distinction-e997fbf942be

Query: What theoretical foundations underpin explicit control-flow versus LLM autonomy trade-offs?

Answer: LLM Flows: Tool use is integrated via explicit function calls embedded within the predefined chain or pipeline. The sequence dictates when and which tool is used. A step in the pipeline might be hard-coded to call a weather API, then another step calls the LLM to summarize the result. This provides predictability and control. This reveals a significant trade-off: increased autonomy often correlates with reduced reliability and predictability. While LLM flows are reliable for well-defined tasks, agents require extensive safeguards and oversight. LLM Flows: Due to their structured, sequential nature, flows are generally more controllable and predictable. Each step can be debugged and tested more easily. While they are still subject to the LLM’s inherent hallucination problem, issues like prompt sensitivity can be managed with robust prompt engineering and error handling (e.g., retries, fallbacks). RAG significantly improves accuracy for domain-specific queries by grounding responses in external data.

-----

</details>

<details>
<summary>What latency and scaling challenges arise in LangGraph checkpointing for long-running agents?</summary>

Phase: [EXPLORATION]

### Source [69]: https://www.langchain.com/blog/building-langgraph

Query: What latency and scaling challenges arise in LangGraph checkpointing for long-running agents?

Answer: LangGraph faces latency challenges due to long agent run times and frequent LLM calls. Checkpoints help manage state but can increase storage needs. LangGraph's DeltaChannel reduces checkpoint size by storing only changes.

-----

Phase: [EXPLORATION]

### Source [70]: https://aerospike.com/blog/langgraph-production-latency-replay-scale

Query: What latency and scaling challenges arise in LangGraph checkpointing for long-running agents?

Answer: LangGraph is a low-level orchestration framework and runtime for building long-running, stateful agents. Checkpoints align with supersteps. Using a checkpointer, LangGraph can persist state at step boundaries, which allows workflows to resume from previously saved graph states. Even a simple example in the documentation saves four snapshots during a basic run. But the number of snapshots depends on how many steps the agent takes, not how long it runs. The answer becomes more urgent under fan-out and superstep amplification.

-----

Phase: [EXPLORATION]

### Source [71]: https://docs.langchain.com/oss/python/langgraph/persistence

Query: What latency and scaling challenges arise in LangGraph checkpointing for long-running agents?

Answer: Optimize checkpoint storage. By default, LangGraph checkpoints write the full value of every state channel at each super-step. For long-running threads with large accumulations—such as multi-turn conversations—this can produce significant storage growth over time. DeltaChannel stores only incremental deltas instead of the full accumulated value, substantially reducing checkpoint size for append-heavy channels. DeltaChannel requires langgraph>=1.2 and is currently in beta. The API may change in future releases. "exit": LangGraph persists changes only when graph execution exits either successfully, with an error, or due to a human in the loop interrupt. This provides the best performance for long-running graphs but means intermediate state is not saved, so you cannot recover from system failures (like process crashes) that occur mid-execution. "async": LangGraph persists changes asynchronously while the next step executes. This provides good performance and durability, but there’s a small risk that LangGraph does not write checkpoints if the process crashes during execution.

-----

</details>

<details>
<summary>What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?</summary>

Phase: [EXPLORATION]

### Source [72]: https://o-mega.ai/articles/crewai-an-extremely-in-depth-guide-2025-10-000-words

Query: What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?

Answer: Failure modes include agents getting stuck in loops, making incorrect decisions, and silent failures causing pipeline hangs. Proper failure handling and testing for edge cases are essential. Hierarchical delegation can fail if manager agents don't properly allocate tasks.

-----

Phase: [EXPLORATION]

### Source [73]: https://vadim.blog/crewai-unique-features

Query: What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?

Answer: The hierarchical manager is CrewAI's most telling failure. It reveals the gap between the framework's metaphor and its implementation. In a real company, a manager who ignores delegation structure and runs every task sequentially gets fired. CrewAI's auto-generated manager does exactly that — and the framework calls it "hierarchical process." This isn't a bug to be patched; it's a sign that LLMs are bad managers. They lack the judgment to dynamically allocate work across agents. Until models get significantly better at meta-reasoning about task decomposition, "auto-generated coordination" will remain a demo feature, not a production one. Write your own manager prompt or use sequential mode. At least sequential is honest about what it does. Known issue: As of March 2026, bug #4783 documents that hierarchical process delegation can fail — manager agents cannot delegate to worker agents even with allow_delegation=True.

-----

Phase: [EXPLORATION]

### Source [74]: https://docs.crewai.com/en/concepts/agents

Query: What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?

Answer: When context limits are exceeded: Error message: "Context length exceeded. Consider using smaller text or RAG tools from crewai_tools." Execution stops: Task execution halts immediately. Manual intervention required: You need to modify your approach. Use respect_context_window=False when precision is critical and information loss is unacceptable. Legal or medical tasks requiring complete context. Code review where missing details could introduce bugs. Financial analysis where accuracy is paramount.

-----

Phase: [EXPLORATION]

### Source [75]: https://docs.crewai.com/en/guides/agents/crafting-effective-agents

Query: What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?

Answer: Premature Use of Hierarchical Structures. Vague or Generic Agent Definitions. "God Tasks" That Try to Do Too Much. Misaligned Description and Expected Output. Not Understanding the Process Yourself.

-----

Phase: [EXPLORATION]

### Source [76]: https://www.linkedin.com/posts/natebjones_four-structural-failure-modes-exist-in-every-activity-7440161225067433984-Sw6B

Query: What failure modes appear when using CrewAI opinionated roles in non-standard edge cases?

Answer: Four structural failure modes exist in every enterprise AI agent: 1 - The inverted U: Agents perform best on routine cases, worst at the extremes where stakes are highest. Your accuracy dashboard says 87% and everyone celebrates. That number is masking silent failures at the tails, where consequential decisions live. The agent earns autonomy on cases where it’s demonstrably reliable, and routes to humans where the inverted U predicts failure. 2 - Knows but doesn't act: The agent identifies the problem in its reasoning, then the output ignores it.

-----

</details>

<details>
<summary>What open research directions remain for MCP standardization in heterogeneous runtimes?</summary>

Phase: [EXPLORATION]

### Source [77]: https://www.databricks.com/blog/what-is-model-context-protocol

Query: What open research directions remain for MCP standardization in heterogeneous runtimes?

Answer: As the open standard matures, future research directions include enhanced security frameworks for multi-tenant deployments, improved streaming semantics for complex agentic workflows, and standardized patterns for integrating with additional programming languages and development environments. Organizations exploring the Model Context Protocol should monitor ecosystem developments, contribute to MCP implementations, and participate in working groups shaping how connecting AI assistants to external systems evolves. This collaborative approach ensures MCP implementations remain interoperable as AI systems and external services continue to advance. Future research directions will likely focus on expanding the protocol's capabilities while maintaining its core simplicity.

-----

Phase: [EXPLORATION]

### Source [79]: https://project-rachel.4open.science/Rachel.So.MCP.Servers.for.Scientific.Workflows.pdf

Query: What open research directions remain for MCP standardization in heterogeneous runtimes?

Answer: Several research directions could enhance MCP’s utility for scientific workflows. First, developing streaming extensions would enable real-time data processing workflows. These extensions must preserve MCP’s logging and reproducibility properties while supporting continuous data flow. Second, creating domain-specific MCP server libraries would accelerate adoption. Community-maintained implementations for common scientific tools would reduce development barriers and establish conventions for data representation. These libraries could build on existing scientific software ecosystems such as Bioconda or PyPI.

-----

Phase: [EXPLORATION]

### Source [80]: https://arxiv.org/html/2503.23278v2

Query: What open research directions remain for MCP standardization in heterogeneous runtimes?

Answer: § 6 explores implications, future challenges, and recommendations to enhance MCP’s scalability and security in dynamic AI environments. The paper analyzes security and privacy risks across the MCP server lifecycle and proposes mitigation strategies. It examines the current MCP landscape, focusing on key industry players and adoption trends.

-----

Phase: [EXPLORATION]

### Source [81]: https://www.preprints.org/manuscript/202504.0245

Query: What open research directions remain for MCP standardization in heterogeneous runtimes?

Answer: Challenges remain in adoption, standardization, security, scalability, and ecosystem development. The survey identifies challenges and proposes directions for future work, acknowledging that empirical validation is still emerging. MCP’s design is critically evaluated, potential applications in domains such as finance, healthcare, and customer service are discussed, and the key challenges are outlined.

-----

</details>

<details>
<summary>How did software design patterns shape explicit control versus autonomy in agent frameworks?</summary>

Phase: [EXPLORATION]

### Source [82]: https://outshift.cisco.com/blog/ai-ml/agent-design-patterns-system-development

Query: How did software design patterns shape explicit control versus autonomy in agent frameworks?

Answer: Software design patterns shifted agent frameworks from centralized control to distributed autonomy, emphasizing adaptive protocols and multi-agent coordination. They balance autonomy with reliability through patterns like ReAct and Plan-and-Execute. These patterns enable agents to operate independently or semi-autonomously based on task complexity. Many existing programming models assume a single controlling logic that directs all components. GenAI multi-agent systems, however, are inherently decentralized. Each agent may have its own goals, learning algorithms, and decision-making processes, including its choice of large language model (LLM). Managing a set of independently evolving agents—each potentially running different models and strategies—calls for abstractions that support autonomy, collaboration, and negotiation rather than a top-down orchestration. Traditional software engineering relies heavily on well-defined APIs, structured data schemas, and rigid communication protocols. Multi-agent GenAI applications, however, often require agents to negotiate or debate on the spot, dynamically refine their reasoning strategies, and reinterpret or transform data representations. This fluidity is challenging to represent or maintain in a rigidly typed, statically defined programming model.

-----

Phase: [EXPLORATION]

### Source [83]: https://tetrate.io/learn/ai/ai-agent-design-patterns

Query: How did software design patterns shape explicit control versus autonomy in agent frameworks?

Answer: AI agent design patterns provide the foundation for building autonomous systems that can reason, plan, and act effectively in complex environments. The patterns discussed—from ReAct and Plan-and-Execute for agent reasoning, through tool integration and memory systems for agent capabilities, to multi-agent coordination and production deployment strategies—represent accumulated knowledge from practitioners building real-world agent systems. Success with AI agents requires not just understanding individual patterns but knowing how to combine them appropriately for specific use cases, balancing autonomy with reliability, and implementing the operational practices needed for production deployment. Agents can operate at different levels of autonomy depending on their design and use case. Some agents work in a fully autonomous mode, executing entire workflows without human intervention. Others operate in a semi-autonomous mode, requesting human approval for critical decisions or high-risk actions. The appropriate level of autonomy depends on factors like task complexity, error tolerance, and the potential impact of incorrect actions. Production systems often implement graduated autonomy, where agents handle routine tasks independently but escalate unusual situations to human operators. Three fundamental design patterns have emerged as the foundation for building effective AI agents: ReAct, Plan-and-Execute, and Reflection.

-----

Phase: [EXPLORATION]

### Source [84]: https://medium.com/@aydinKerem/ai-agents-design-patterns-explained-b3ac0433c915

Query: How did software design patterns shape explicit control versus autonomy in agent frameworks?

Answer: In this article, we explored the evolving landscape of AI agents and their design patterns, highlighting how agentic frameworks have democratized the development of complex AI systems. By discussing foundational concepts and practical implementations like the ReAct pattern, we demonstrated that simpler, cost-effective architectures can often solve specific tasks efficiently. We also examined advanced multi-agent systems, planning agents, and reflection frameworks that enhance AI capabilities. The success of projects like ChatDev underscores the potential of multi-agent collaboration, while tools like LangGraph simplify building sophisticated agentic workflows. Overall, understanding and leveraging these design patterns empower developers to create reliable and scalable AI systems for various applications. It is possible to build different architectures using pure code. But it is important to remember what makes agents so promising. It is that they can work with each other by communicating and assigning each other works to complete even more complex tasks. Building these type of architectures can be a quite a challenge very quickly, therefore many AI companies built their own frameworks to simplify the construction of an Agentic workflow.

-----

Phase: [EXPLORATION]

### Source [85]: https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system

Query: How did software design patterns shape explicit control versus autonomy in agent frameworks?

Answer: A single-agent system uses an AI model, a defined set of tools, and a comprehensive system prompt to autonomously handle a user request or to complete a specific task. In this fundamental pattern, the agent relies on the model's reasoning capabilities to interpret a user's request, plan a sequence of steps, and decide which tools to use from a defined set. The system prompt shapes the agent's behavior by defining its core task, persona, and operations, and the specific conditions for using each tool. This document provides guidance to help you choose a design pattern for your agentic AI system. Agent design patterns are common architectural approaches to build agentic applications. An agent design pattern offers a distinct framework for organizing a system's components, integrating the model, and orchestrating a single agent or multiple agents to accomplish a workflow.

-----

Phase: [EXPLORATION]

### Source [86]: https://arxiv.org/html/2602.10479v1

Query: How did software design patterns shape explicit control versus autonomy in agent frameworks?

Answer: The evolution from prompt response loops to goal directed agentic systems represents a convergence of classical agent theory with modern LLM centric practice. Architectural priorities are increasingly standardizing around typed tool interfaces, explicit control loops, and multi agent coordination protocols. Nevertheless, open problems remain in verifiability (how to formally certify agent behavior), interoperability (how to compose agents across different platforms), and safe autonomy (how to ensure agents remain aligned under open ended deployment). The next phase of agentic architecture is likely to resemble the maturation of web services: shared protocols, typed contracts, and layered governance that enable composable autonomy at scale. Architecturally, teams confront a pragmatic design choice along a spectrum. On one end, Symbolic or classical designs externalize planning into deterministic modules and explicit state machines, enabling verification at the cost of flexibility. On the other end, Neural or generative designs leverage stochastic LLM outputs for planning and decomposition, gaining adaptability but sacrificing predictability. Increasingly, production systems adopt hybrid patterns that use LLMs for high-level decomposition while enforcing symbolic constraints on tool execution so as to balance safety and adaptability.

-----

</details>

<details>
<summary>What embedded systems lessons apply to reliability primitives in AI agent runtimes?</summary>

Phase: [EXPLORATION]

### Source [87]: https://uxmag.com/articles/ai-agent-runtimes-in-dedicated-lanes-lessons-from-chinas-ev-roads

Query: What embedded systems lessons apply to reliability primitives in AI agent runtimes?

Answer: AI agent runtimes use isolation, checkpoints, and deterministic execution for reliability, mirroring embedded systems' safety and stability principles. Sandboxing prevents failures from spreading, and continuous "charging" ensures agents can operate without reboots. Dedicated EV lanes keep traffic steady; isolated execution lanes via sandboxed containers or specialized hardware give agents deterministic response times for real-time tasks. Continuous charging via model caches, warm-start checkpoints, and fast state transfer allows agents to refuel mid-operation. Segregated EV traffic reduces accidents; sandboxed runtimes prevent rogue agents from corrupting core services, improving reliability and compliance. China's EV roads show redesigning flow from the ground up applies to mature AI agent runtime environments where agents are designed, deployed, and orchestrated within purpose-built infrastructure.

-----

Phase: [EXPLORATION]

### Source [88]: https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime

Query: What embedded systems lessons apply to reliability primitives in AI agent runtimes?

Answer: Isolation against the model’s mistakes: Filesystem isolation, copy-on-write snapshots, and per-session ephemerality turn destructive actions into recoverable ones. Isolation against prompt injection: A sandbox stands between an injected instruction and production database, analogous to the SQL injection lesson. Multi-tenancy at training scale requires strong isolation primitives so one rollout’s flaky command does not take down neighbors. Reproducibility: A sandbox you can snapshot is a sandbox you can replay for debugging trajectories and turning production failures into regression tests. An agent’s runtime cannot be sloppy because the agent keeps going long after a human would stop.

-----

Phase: [EXPLORATION]

### Source [89]: https://www.linkedin.com/posts/baraktur_towards-a-science-of-ai-agent-reliability-activity-7434268792404267008-W8nW

Query: What embedded systems lessons apply to reliability primitives in AI agent runtimes?

Answer: Framework inspired by safety-critical engineering evaluates agentic systems on Consistency (repeated runs produce same outcome), Robustness (performance under perturbations), Predictability (anticipate failure via confidence signals), and Safety (failure modes bounded and manageable). Model capability improves faster than dependability; larger models can be less consistent. For production agentic systems measure Repeatability, Failure severity, Variance across runs, and Confidence calibration. Reliability is the moat beyond accuracy.

-----

Phase: [EXPLORATION]

### Source [90]: https://www.reddit.com/r/AI_Agents/comments/1sosicj/why_agent_reliability_matters_more_than_agent

Query: What embedded systems lessons apply to reliability primitives in AI agent runtimes?

Answer: Reliability via bounded input (only database schemas and workflow descriptions), bounded output (only email workflows), deterministic execution (rule-based once published), and human review gate. In firmware every issue generates Corrective and Preventive Action record. Reasoning used during setup must be preserved for inspectability to avoid audit gaps. Use AI for planning/generation and deterministic rules for execution so intelligence is in setup and reliability in runtime.

-----

Phase: [EXPLORATION]

### Source [91]: https://substack.com/home/post/p-187330720

Query: What embedded systems lessons apply to reliability primitives in AI agent runtimes?

Answer: Shared-kernel container isolation (Docker/runc) is insufficient for untrusted AI agent code; treat LLM-generated code as hostile. Use primitives like Firecracker/gVisor/LiteBox for maximum control with strong isolation. Embeddable runtimes (E2B, microsandbox) add code execution quickly. Managed platforms handle data-heavy workloads. For long-running agents, billing models matter; warm pools on primitives require complex autoscaling. Data gravity considerations affect choice of layer.

-----

</details>

<details>
<summary>How does MCP interoperability impact no-code AI development platforms?</summary>

Phase: [EXPLORATION]

### Source [92]: https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different

Query: How does MCP interoperability impact no-code AI development platforms?

Answer: MCP standardizes the way AI applications discover and use available tools, making it easier to build scalable, future-proof AI systems that can interact with multiple services and external systems without the need for constant code changes. In the context of the ongoing AI revolution, dynamic discovery through MCP is unlocking new possibilities for AI-driven software. Developers can now build AI applications that are not only more powerful and responsive to user needs, but also capable of integrating with a rapidly evolving ecosystem of MCP servers and tools. By embracing the model context protocol, organizations can ensure their AI systems remain agile, connected, and ready to leverage the latest advancements in external data and services. Though still new, MCP simplifies developer responsibilities by standardizing schemas and automating capability discovery. With MCP, integrations become repeatable and uniform, drastically reducing repetitive boilerplate code. Developers gain flexibility, as new capabilities introduced by backend services automatically propagate through the MCP manifest, enabling rapid adoption without significant refactoring. MCP also allows for the integration of a new tool at runtime, so AI systems can dynamically discover and use tools without hardcoding. Architects should prioritize traditional APIs for stable, predictable integrations where requirements rarely change, such as e-commerce inventory or mobile banking transactions. Conversely, MCP is the superior choice for AI-driven systems requiring rapid adaptability and dynamic discovery. If your application involves AI agents orchestrating tasks across diverse tools like Jira or Salesforce, MCP reduces maintenance overhead. By acting as an abstraction layer, MCP allows your AI assistant to reason about new capabilities and adapt to changing protocols at runtime, ensuring a more future-proof architecture.

-----

Phase: [EXPLORATION]

### Source [94]: https://www.linkedin.com/posts/alexxubyte_systemdesign-coding-interviewtips-activity-7333156347548508161-zmOv

Query: How does MCP interoperability impact no-code AI development platforms?

Answer: One of the biggest challenges in today’s AI landscape is not intelligence itself, but Interoperability. How do we make AI systems, tools, and data sources work together without repeatedly building custom integrations? This is where Model Context Protocol (MCP) comes in. MCP provides a common language for AI agents to interact with external tools and data. Instead of hard-coding agents to speak to every individual API, you teach them MCP. The MCP server handles the underlying details, giving you a cleaner, more scalable, and more secure interface. The ecosystem is built around three components: MCP Host – the application where the AI model runs; MCP Client – the bridge inside the host that requests external capabilities; MCP Server – the service that exposes tools and data in a standardized way. Integrating Your Software with AI Solutions Understanding the Model Context Protocol (MCP) The Model Context Protocol (MCP) is revolutionizing how AI interacts with software. Released in late 2024, this well-defined framework allows seamless communication between software components, akin to earlier shifts from desktop to web and mobile applications. Key Highlights: Simplicity Meets Impact: MCP standardizes how AI agents access various software, pushing the boundaries of user interaction. Essential for Developers: Understanding MCP is crucial for enhancing software offerings. Users will soon expect integrated solutions with their AI agents. Authentication at Scale: Prefactor is leading the charge, bridging gaps in security and scalability for software builders. Why it Matters: MCP is MCP Tools are transforming AI by acting as standardized bridges between large language models (LLMs) and external systems. Instead of working in isolation, AI can now fetch real-time data, run commands, and connect with databases or APIs seamlessly. Why it matters: MCP Tools eliminate custom integrations, boost security, and scale easily. Developers gain a universal protocol that reduces complexity while ensuring consistency and reliability across applications. Core components: Server: Manages and hosts tools (e.g., DB, APIs, file systems). Client: AI apps that use MCP tools. Protocol: Defines communication, authentication & error handling. Key benefits: Standardization & interoperability.

-----

Phase: [EXPLORATION]

### Source [95]: https://www.anthropic.com/news/model-context-protocol

Query: How does MCP interoperability impact no-code AI development platforms?

Answer: Early adopters like Block and Apollo have integrated MCP into their systems, while development tools companies including Zed, Replit, Codeium, and Sourcegraph are working with MCP to enhance their platforms—enabling AI agents to better retrieve relevant information to further understand the context around a coding task and produce more nuanced and functional code with fewer attempts.

-----

Phase: [EXPLORATION]

### Source [96]: https://www.backslash.security/blog/what-is-mcp-model-context-protocol

Query: How does MCP interoperability impact no-code AI development platforms?

Answer: The Model Context Protocol (MCP), an open standard introduced by Anthropic, is transforming software development by providing a universal interface for AI models to securely connect with external tools and data. It addresses the inefficiencies of custom integrations by enabling AI assistants to access real-time context—such as code, documents, and APIs—through a standardized client-server architecture. MCP significantly reduces AI hallucinations and expands AI utility, facilitating automation in coding, documentation, testing, and CI/CD workflows. With rapid adoption by major industry players like OpenAI, Microsoft, and Google DeepMind, MCP is establishing itself as a foundational standard for interoperable and "agentic" AI. The Model Context Protocol is proving to be a game-changer for developer workflows, transforming AI from a passive assistant into an active participant in the software lifecycle. By allowing AI systems to "plug into" and interact with code editors, documentation, test frameworks, CI/CD pipelines, and cloud services, MCP unlocks use cases that were impractical just a short time ago. The rapid adoption of MCP by major industry players like OpenAI, Anthropic, Microsoft, and Google DeepMind—despite being rivals in other areas—underscores its potential to become a universal standard for AI-tool integration. As Google DeepMind CEO Demis Hassabis put it, MCP is "rapidly becoming an open standard for the AI agentic era". It’s important to note that MCP complements existing agent frameworks like LangChain; it standardizes the "hands" of an AI system, allowing it to interact with the world, rather than handling the "brain" or high-level orchestration. MCP isn’t just a technical curiosity; it represents a strategic shift that makes AI systems more capable, reliable, and scalable across the entire software development lifecycle. Key Benefits:

-----

Phase: [EXPLORATION]

### Source [97]: https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different

Query: How does MCP interoperability impact no-code AI development platforms?

Answer: MCP standardizes the way AI applications discover and use available tools, making it easier to build scalable, future-proof AI systems that can interact with multiple services and external systems without the need for constant code changes.

-----

</details>

<details>
<summary>Which game AI multi-agent patterns transfer to production LLM frameworks?</summary>

Phase: [EXPLORATION]

### Source [98]: https://rasa.com/blog/best-ai-agent-framework

Query: Which game AI multi-agent patterns transfer to production LLM frameworks?

Answer: CrewAI and Microsoft Agent Framework provide explicit multi-agent patterns. OpenAI Swarm offers lightweight agent abstraction with handoff primitives, valuable for learning multi-agent patterns but experimental and not intended for production. No persistence, no memory management, no observability, no governance. Rasa CALM provides patented architectural separation for LLM governance. Enterprise deployments need multiple agents coordinating with shared state, clean handoffs, and unified memory.

-----

Phase: [EXPLORATION]

### Source [99]: https://www.superannotate.com/blog/multi-agent-llms

Query: Which game AI multi-agent patterns transfer to production LLM frameworks?

Answer: CrewAI manages crews of AI agents for production-ready applications, featuring clean code and focusing on practical applications. AutoGen is a flexible AI agent playground with human-in-the-loop support. LangChain provides building blocks for complex AI applications. LangGraph enables AI workflows with cycles and branching logic. AutoGPT is suitable for persistent tasks with memory and context. Hierarchical multi-agent reinforcement learning uses hierarchical learning for coordination.

-----

Phase: [EXPLORATION]

### Source [100]: https://getstream.io/blog/multiagent-ai-frameworks

Query: Which game AI multi-agent patterns transfer to production LLM frameworks?

Answer: OpenAI Swarm is a lightweight multi-agent orchestration framework, experimental, for development and educational purposes but should not be used in production. CrewAI allows building multi-agent automations, with UI Studio for no-code, deployment from development to production, agent monitoring dashboard, and built-in training tools. Agno and CrewAI provide intuitive dashboards for monitoring.

-----

Phase: [EXPLORATION]

### Source [101]: https://www.truefoundry.com/blog/multi-agent-architecture

Query: Which game AI multi-agent patterns transfer to production LLM frameworks?

Answer: The Critic-Refiner (Reflection) Pattern enables a feedback loop where one AI produces output and another critiques it for accuracy and completeness. Multi-agent architecture divides complex workflows into smaller tasks handled by distinct AI agents. Frameworks like LangGraph, AutoGen, or CrewAI make building easy on laptops but deploying to enterprise production is different, requiring state management, identity-aware tools, centralized registries, observability, and compute orchestration.

-----

Phase: [EXPLORATION]

### Source [102]: https://arxiv.org/html/2402.01680v1

Query: Which game AI multi-agent patterns transfer to production LLM frameworks?

Answer: Frameworks combine LLMs with reinforcement learning for strategic language agents in games like Werewolf, using RL policy in natural language settings. Welfare Diplomacy benchmark for cooperation. Multi-agent cooperative text games test Theory of Mind. Environments include software development, gaming, financial markets. Sandbox environments for Werewolf Game with day/night transitions, voting. AVALONBENCH benchmark for Resistance Avalon. Recursive Contemplation framework for handling misinformation in Avalon game.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agent-frameworks.md">
<details>
<summary>Agent Frameworks</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arize.com/ai-agents/agent-frameworks>

# Agent Frameworks

AI agents have started settling into recognizable shapes. AI agent frameworks have matured, with foundational model labs having their own in-house agentic frameworks like OpenAI SDK and Google ADK, alongside established players shaping this space, such as LangGraph and CrewAI. In this article, we explore operational behaviors for these frameworks and which ones are the best for different types of use cases. We shall also explore how these platforms can be measured to ensure the maximum ROI by using established and tracing techniques. Choosing the right framework helps you ship a reliable, fast MVP and gives you the observability and clarity needed to understand how your agent behaves in production.

### What is an AI Agent Framework?

An AI agent framework acts as the control layer around the model. It establishes the order of operations, determines when to invoke a tool, manages state changes, and directs each step according to clear rules. The agent follows a defined process instead of drifting into ad-hoc behavior.

It also determines how the agent interacts with external systems and stores work in progress. You get a predictable path for execution instead of wiring separate parts by hand. This keeps behaviour steady across environments and gives you a clean surface for debugging when issues show up.

### Key Components of an AI Agent Framework

https://arize.com/wp-content/uploads/2025/02/ai-agent-framework-components.jpg

Agent frameworks rely on a small set of core components that guide how work moves through the system. These parts define how an agent decides what to do, executes steps, interacts with tools, stores intermediate results, and exposes a surface for measurement.

1.  **The planner**: Chooses the next step, sets the order of execution, and keeps the agent on a steady track.
2.  **The worker**: Carries out the step the planner selects and triggers the tool or model operation required for that moment.
3.  **The session state**: [Stores the values and actions](https://arize.com/docs/ax/observe/tracing/sessions-and-users) the agent produces along the way so it can continue a task with the right context.
4.  **The APIs and Tools**: Routes the agent’s request to the API or service it needs and returns the result in a usable form.
5.  **The evaluation or testing hooks**: Record [each action as traces](https://arize.com/docs/ax/observe/tracing-concepts/what-are-traces) and give you points to inspect behaviour or measure output quality.

### Key Metrics to Measure your AI Agent

A few signals tell you whether an agent runs well under real use. These metrics cover correctness, speed, stability, tool reliability, and the cost of completing tasks. Tracking them early gives you a clear picture before you start scaling or tuning behavior.

| Metric | What it Measures | Why It Matters |
| --- | --- | --- |
| **Correctness and output quality** | How often does the agent produce the expected result or reach the right state | Shows whether the workflow works at all and keeps you from shipping an agent that answers confidently but wrong |
| **Latency across each step** | Time spent on planning, tool calls, and execution | Helps you see slow points so you can avoid delays that stack up during multi-step tasks |
| **Tool success and failure rates** | How often do tools return usable results versus errors | Reveals weak integrations or unstable APIs before they cause inconsistent behaviour |
| **Looping or stuck behaviour** | Cases where the agent repeats steps or never exits a state | Prevents runaway runs, wasted cycles, and user-facing stalls |
| **Context rot over time** | Whether the agent keeps or loses important information across steps | Helps you detect when memory or state breaks the workflow |
| **Cost per successful task** | Total spend needed to complete one correct run | Shows if the workflow is sustainable and whether model or tool choices need adjustment |

### Top AI Agent Frameworks

#### CrewAI

CrewAI is built for running agent teams instead of a single loop. You define agents with clear roles and tools, then organize them into a “Crew” that moves through a workflow. Each agent handles a narrow task, and the framework coordinates the handoffs so you don’t wire that routing logic by hand.

You set each agent’s goal, configure how they interact, and use Flows to define the order of work. The runtime handles delegation, retries, memory sharing, and state transitions. It keeps the workflow steady even when a step branches or a tool returns something unexpected.

CrewAI exposes structured logs for agent messages, tool calls, decisions, and task outcomes. This gives you step-level traces to [evaluate the multi-agent setup](https://arize.com/docs/phoenix/evaluation/concepts-evals/evaluating-multi-agent-systems) without modifying your workflow and helps you catch stalls, over-delegation, or repeated loops.

CrewAI works best when your use case benefits from multiple focused agents instead of one large controller. Suppose you’re building research pipelines, content systems, or workflows with several independent decision makers. If you want, CrewAI’s structure makes coordination cleaner and gives you a clear surface for inspection when issues show up.

> [How to trace CrewAI agents using Arize AX](https://arize.com/docs/ax/integrations/python-agent-frameworks/crewai/crewai-tracing)

#### Mastra

[Mastra](https://mastra.ai/) is a TypeScript framework for building agents through typed, workflow-driven development. Each step defines its inputs and outputs, and the framework executes them in sequence. This makes behaviour clear and reduces hidden errors because every transition is explicit.

Developers use Mastra when they want strict typing and a predictable task order. Steps fail fast if arguments don’t match the schema, which helps avoid inconsistent state or untracked failures. The [workflow model](https://mastra.ai/docs/workflows/overview) also makes retries and error handling straightforward.

Mastra fits tasks where stability and repeatability matter. It works well for structured pipelines, automations, and multi-step processes. It is less suited for agents that need open-ended planning or flexible branching.

> [How to Trace Mastra](https://arize.com/docs/ax/integrations/ts-js-agent-frameworks/mastra/mastra-tracing) using Arize AX

#### OpenAI Agents SDK

[OpenAI’s Agents SDK](https://github.com/openai/openai-agents-python) is a thin runtime on top of GPT models rather than a heavy framework. It gives you a small set of primitives – agents, handoffs, guardrails, and sessions – and handles loops and tool calls while keeping conversation state in one place.

You define agents with instructions and tools, then compose them using handoffs or manager patterns instead of wiring your own orchestration layer. The code stays readable while still supporting multi-step and multi-agent flows.

Operationally, the SDK has built-in trace [grading and hooks](https://platform.openai.com/docs/guides/trace-grading#set-up-trace-grading), so every run and tool call, plus each handoff, can be recorded. Arize’s OpenAI Agents cookbook shows how to ship those traces into Phoenix or AX to debug runs and score agent performance over time.

It is a strong fit when you already standardize on OpenAI models and want a supported way to ship agents fast without maintaining your own runtime. If you need provider flexibility or complex graph control, you will likely pair it with other frameworks.

> [How to trace the OpenAI Agents SDK](https://arize.com/docs/ax/integrations/llm-providers/openai/openai-agents-sdk-tracing)

#### LangGraph

[LangGraph](https://arize.com/blog/langgraph/) is a graph-based runtime for building stateful agent workflows. You define nodes as functions and edges as transitions. The framework handles state, branching, and long-running flows so your agent can move through complex work without losing context.

Building with LangGraph feels closer to designing a system than wiring a single agent loop. You sketch the graph of steps, set conditions for each edge, and let the runtime handle checkpoints and recovery. That makes it a good fit for workflows that mix deterministic logic with agentic decisions.

Operationally, LangGraph focuses on durability and control. It offers built-in persistence, shared state across nodes, and human-in-the-loop pauses. It also streams updates as the graph runs, which pairs well with external observability like Arize AX. Arize’s LangGraph tracing guide shows how to instrument runs via the [OpenInference](https://github.com/Arize-ai/openinference) integration.

LangGraph is strongest when you need branching workflows, multi-agent setups, or business processes that span sessions. It has more setup cost than a simple agent SDK, but in return, you get explicit control over each transition and a cleaner surface for debugging real incidents.

> [How to trace LangGraph with Arize AX](https://arize.com/blog/langgraph/)

#### Google ADK

[Google ADK](https://arize.com/blog/tracing-evaluation-and-observability-for-google-adk-how-to/) is a code-first way to build structured, multi-agent workflows. You define a root agent, attach sub-agents, and wire tools and memory into clear steps so the workflow doesn’t drift. Each step has typed inputs and outputs, which keeps execution predictable even when the model improvises.

You route between agents, call tools through defined interfaces, and rely on session memory to keep context stable. The runtime logs every decision, tool call, and state change. When you [connect it to Arize AX](https://google.github.io/adk-docs/observability/arize-ax/), you get full traces, tool spans, and step-level evaluations without extra plumbing.

ADK shines when you need branching logic, [multi-agent patterns](https://google.github.io/adk-docs/agents/multi-agents/), or [workflows](https://google.github.io/adk-docs/agents/workflow-agents/) that depend on strong memory and detailed telemetry. It’s a good fit for enterprise teams that want structure, observability, and a predictable runtime rather than a loose agent loop.

> [How to trace a Google ADK agent](https://arize.com/blog/tracing-evaluation-and-observability-for-google-adk-how-to/)

#### AWS Bedrock AgentCore

[AWS Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) is the runtime layer for teams that want to run agents in production without handling infrastructure. You ship your agent as a container, and AgentCore takes care of autoscaling, routing, deployment, and model access. This keeps the operational path simple while letting you keep full control over your agent logic.

AgentCore works with any framework because it doesn’t enforce a planning or execution model. You can run Strands, LangGraph, CrewAI, Autogen, or your own custom stack. The runtime exposes a stable API surface, typed inputs, environment configuration, and IAM-based security, which makes it straightforward to plug into existing AWS setups and [observability platforms like Arize AX](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agents-observability-using-arize-ai/).

[Tooling integrates](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) through the container itself. Your agent calls whatever services it needs — internal APIs, databases, or external tools — without constraints from the runtime. AgentCore focuses on keeping the service online and scaling with demand.

This option fits teams already invested in AWS or teams that want a managed path to production without changing the way they design agents.

> [How to Trace AWS Bedrock](https://arize.com/docs/ax/integrations/llm-providers/amazon-bedrock/amazon-bedrock-tracing) using Arize AX

#### Strands Agents

[Strands](https://aws.amazon.com/blogs/machine-learning/observing-and-evaluating-ai-agentic-workflows-with-strands-agents-sdk-and-arize-ax/) is a lightweight, provider-agnostic SDK for building agents with a small footprint. You define tools as Python functions, pick a model provider, and Strands runs the loop that links model responses with tool calls. The setup stays simple, which helps when you want to move fast without pulling in a large framework.

It gives you full control over how actions unfold. You design the order of steps, decide when tools run, and shape the reasoning flow yourself. Smaller agents work with almost no overhead. When you need more structure, you add it directly in code instead of relying on framework rules. The library comes with a [great number of tools](https://github.com/strands-agents/tools), which are part of a larger ecosystem of contributors.

The SDK fits well in mixed model environments. Switching between OpenAI, Bedrock, Gemini, or a local model doesn’t require rewriting core logic. It also handles custom backends cleanly. If your stack already depends on internal APIs or services, Strands lets you wire them in without extra layers.

It stays easy to read, easy to change, and easy to embed inside existing systems. It works best for agents that need predictable, controlled execution rather than structured graphs or heavy orchestration. It gives you a direct way to build, deploy, test, and refine an agent without adopting a large ecosystem.

> [How to Trace Strands AI](https://aws.amazon.com/blogs/machine-learning/observing-and-evaluating-ai-agentic-workflows-with-strands-agents-sdk-and-arize-ax/) using Arize AX

#### LlamaIndex Workflows

LlamaIndex Workflows is an indexing and retrieval engine on top of language-model agents, making it easier to build retrieval-augmented, document-driven agents. Instead of only calling tools or APIs, agents can query structured indexes (documents, databases, knowledge graphs) managed by LlamaIndex, and use those results inside their reasoning. That means the “tools” surface isn’t limited to external APIs — it naturally includes internal knowledge bases and retrieval pipelines.

When you build with LlamaIndex Workflows, flows often combine retrieval + reasoning + tool calls: first fetch relevant context, then plan with the model, then call tools or generate output. This hybrid of retrieval and LLM reasoning gives your agents grounding: output is tied to data, not hallucination. For teams working on document-heavy tasks, search, summarization, or knowledge-driven automation, this can reduce error rates and increase consistency.

Because the workflow is partially deterministic (you control index queries, retrieval steps, and reasoning + tool calls), debugging and evaluation become more structured than with free-form chat agents. Although LlamaIndex doesn’t enforce a strict orchestration engine like a graph framework.

LlamaIndex works well when your agent depends on retrieval or cyclical reasoning. It lets the agent pull fresh context from indexed data instead of relying only on prompts. With Arize AX’s [LlamaIndex tracing](https://arize.com/docs/ax/integrations/python-agent-frameworks/llamaindex/llamaindex-workflows-tracing), those retrieval steps show up beside model and tool calls, so you can see which queries fired, how long they took, and how they shaped the final output.

#### Autogen

AutoGen is built around the idea of coordinating multiple chat-based agents that speak to each other to complete a task. You define agents with roles, tools, and functions, then use AutoGen’s conversation engine to control how they exchange messages. The framework handles the back-and-forth, tool routing, and stopping conditions so you don’t write that logic yourself.

One agent plans, another executes, and extra workers can step in for retrieval, code execution, or validation. The control you get over message flow and termination rules keeps the conversation from spiraling or looping.

AutoGen exposes each message, tool call, and interaction, which you can trace through Arize AX using the OpenInference integration. You get a clear view of where agents stall, repeat work, or fail to coordinate. AutoGen works best when your workflow benefits from multiple focused agents instead of one monolithic controller.

> [How to trace AutoGen using Arize AX](https://arize.com/docs/ax/integrations/python-agent-frameworks/autogen/autogen-tracing)

### Which AI Agent Framework is the Best for You?

Agent frameworks look the same on the surface, but the way they work is very different.

- The controller and worker loops decide how an agent advances through a task.
- The API and tool-calling path determines how external systems respond under load.
- The memory layer shapes how well the agent keeps context and avoids context rot.

These three parts decide which framework fits your use case and how it behaves once real traffic hits it.

#### Orchestrator and Worker Behavior

Agent frameworks differ most in how they decide the next step and how they execute it. With the core thinking still that of an [orchestrator and worker-type agent](https://arize.com/blog/orchestrator-worker-agents-a-practical-comparison-of-common-agent-frameworks/), which can be a hybrid system depending on the framework. How these two parts interact greatly determines whether the system feels stable, predictable, and easy to debug once it has been deployed.

| Framework | Controller Behaviour (How control decisions are made) | Worker Behaviour (How actions run) |
| --- | --- | --- |
| **OpenAI Agents SDK** | The runner owns the loop. It picks the next step based on LLM output, handoff rules, and session state. No custom routing logic. The behaviour itself runs on the [Responses API](https://platform.openai.com/docs/api-reference/responses) running in tandem with OpenAI. | Workers are sub-agents or tools. Each invocation is one atomic step: model call, function call, or handoff. No parallelism. |
| **LangGraph** | Control is the graph. Nodes fire based on conditions you define. Edges determine branching, retries, and exits. The [persistence layer](https://docs.langchain.com/oss/python/langgraph/persistence) allows this to work by defining checkpoints that then eventually become a part of the graph execution. | Workers are node functions or subgraphs. They run deterministically and can branch, pause, or emit commands for child graphs. |
| **LlamaIndex Workflows** | Control sits in your workflow code. The agent loops through “retrieve → reason → act” steps you define, rather than a strict graph engine. | Workers are retrieval calls, model calls, and any custom tools you wire in. Steps run sequentially, and you manage looping or branching yourself. |
| **Google ADK** | Root agent evaluates the state and routes to sub-agents. Typed steps enforce strict transitions. Controller acts like a workflow engine with guardrails. | Workers are structured in steps with typed IO. Each step is validated before and after execution. Strong bias toward predictable output. |
| **AutoGen (Microsoft)** | The conversation manager selects the next speaker based on the group chat state. Control emerges from dialogue patterns rather than explicit routing. | Workers are agents that respond to messages. Each response can call a tool, request validation, or hand off implicitly via conversation turns. |
| **CrewAI** | Manager agent plans, delegates, and validates. The controller decides when roles switch and how tasks flow between agents. Feels like a small PM. | [Workers are role agents with narrow responsibilities](https://docs.crewai.com/en/concepts/agents). They execute tasks, update shared context, and return results for validation. |
| **Mastra** | Workflow defines control. Steps run in the declared order, with branching when configured. Typed transitions catch bad inputs early. | Step functions run as workers with strict IO. Retries and errors are explicit and handled at the step level. |
| **AWS Bedrock AgentCore** | No built-in controller. Your containerized agent defines all planning and sequencing. AgentCore only executes and scales it. | Workers are your code paths. Each request triggers your model calls, tools, or logic exactly as written. |
| **Strands Agents** | The agent loop drives control. You decide when to call the model, when to run tools, and how the flow advances. | Tools and model calls act as workers. Each runs one at a time with no built-in branching or parallel execution. |

#### API and Tool-Calling Behavior

Most agents don’t talk to a hundred tools. In practice, they hit a handful of APIs, sometimes through n8n or a custom backend. The framework decides how these calls are wired, how arguments are validated, and where errors surface. That behaviour matters more than raw tool count.

| Framework | How tools and APIs are wired | Behaviour you should expect |
| --- | --- | --- |
| **OpenAI Agents SDK** | Tools are registered as functions or [OpenAI Actions](https://platform.openai.com/docs/actions/introduction), then attached to agents. You can configure them in code or through the [Agents Playground](https://platform.openai.com/agent-builder), which is handy for quick iteration with product or ops teams. | Tool calls run inside OpenAI’s runtime. You see a clean schema, arguments, and responses, but less control over low-level retries. For more complex stacks, teams often front tools with a single backend or [n8n flow](https://n8n.io/workflows/). |
| **LangGraph** | Tools are normal Python or TypeScript functions wrapped as nodes. Each tool node can call external APIs, internal services, or a gateway that fans out to multiple systems. | Failures and retries stay local to the node. You decide how to handle timeouts or fallbacks. Many teams expose one internal API per node instead of wiring raw SaaS tools directly into the graph. |
| **LlamaIndex Workflows** | Tools sit around retrieval: the agent queries indexes, vector stores, or structured sources first, then calls APIs or functions from your code when needed. | Retrieval and tool calls share one loop. Behaviour leans heavily on index quality, query design, and how you chain tools after context is fetched. |
| **Google ADK** | Tools are declared with typed signatures and can target Vertex AI tools, HTTP endpoints, or internal services. The SDK enforces schemas and validates inputs and outputs. | Tool calls produce structured telemetry by default. You get clear spans for each call, which makes it easier to trace failures or slow vendors. In heavier stacks, ADK often points at an internal gateway rather than vendor APIs directly. |
| **AutoGen (Microsoft)** | Tools are Python functions or wrappers that agents can call inside a chat turn. Each agent can have its own tool set, and tools can perform API calls, code execution, or retrieval. | Tool calls happen inside the dialogue. If a tool struggles, the conversation can stall or loop. Many teams hide real systems behind one tool entrypoint to keep the surface area small and easier to guard. |
| **CrewAI** | Tools are attached to agents through config or code. They can rely on LangChain tools, HTTP requests, or custom Python functions that talk to upstream APIs and services. | Manager agents decide when to call a tool versus another agent. Tool-heavy crews often route everything through a small number of composite tools so that retries, auth, and vendor quirks live outside the CrewAI layer. |
| **Mastra** | Tools run inside typed workflow steps. Each step can call external APIs, internal services, or a gateway. | Calls stay predictable because each step enforces inputs and outputs. Errors surface fast and are easy to isolate. |
| **AWS Bedrock AgentCore** | Tools are not wired at the runtime level. Your agent calls APIs or backends directly from inside the container. | Behaviour depends entirely on your code. Retries, fallbacks, and failures follow whatever logic you implement. |
| **Strands Agents** | Tools are Python functions decorated for agent use. They can call APIs, databases, or external systems with no extra layers. | Calls run one at a time through the loop. No built-in routing or orchestration, so behaviour stays direct and easy to inspect. |

#### Memory Layer

Memory decides how long an agent can stay coherent. Frameworks differ in how they store session state, how they share context between workers, and where the actual knowledge base lives. In practice, most teams lean on one RAG stack and pass pointers, not raw documents.

| Framework | How memory and session state work | How knowledge bases usually plug in |
| --- | --- | --- |
| **OpenAI Agents SDK** | Sessions hold conversation history and tool results. Handoffs can filter context to keep runs cheap and safe. | Most teams front a single RAG or search service and expose it as one tool, not multiple raw KB calls. |
| **LangGraph** | State is stored as checkpoints keyed by thread or graph node. You can “time-travel” or resume from any point. | KB access is usually wrapped in dedicated nodes that call RAG services or vector DBs and return compressed answers, not full docs. |
| **LlamaIndex** | Memory lives in indexes and vector stores rather than long chat history. Sessions often re-query data instead of relying on a growing transcript. | Knowledge bases plug in as LlamaIndex indexes. Expect good grounding when data is clean, but sensitivity to stale, sparse, or noisy documents. |
| **Google ADK** | Memory ties into session objects and can use Vertex AI memory stores for durability and typed state. | ADK often points at [Vertex Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/introduction), custom RAG APIs, or internal stores. KB access is just another typed tool with strict schemas. |
| **AutoGen (Microsoft)** | Each agent keeps its own chat history; the group chat transcript acts as shared context. | KB access is handled by tools or retrieval helpers. Most real setups hide RAG behind one or two tools to avoid bloating the transcript. |
| **CrewAI** | Crew state combines manager context and per-agent memory. You can configure different memory backends for short- and long-term state. | Knowledge bases plug in through LangChain-style tools or custom retrievers. Teams usually centralize onto one RAG pipeline exposed as a small tool surface. |
| **Mastra** | Mastra supports “Memory” as a built-in feature along with agents, workflows, RAG, and tools. | Mastra supports RAG and Memory integration as first-class elements of its agent/workflow system. |
| **Amazon Bedrock AgentCore** | [Offers both short-term memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-types.html) (raw events/conversation history per session) and long-term memory (persisted across sessions, extracting user preferences, etc.) to enable context awareness and personalization. | KB or knowledge-base access is generally managed by treating memory + retrieval as tools/services. AgentCore handles the underlying storage and retrieval infrastructure, decoupling knowledge retrieval from raw DB calls. |
| **Strands Agents** | [Provides session management via built-in session managers](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/agents/session-management/) (e.g. file system or S3) that persist conversation history, agent state (key-value store), and tool results; this supports both single-agent and multi-agent systems. | Strands can integrate with [Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/strands-sdk-memory.html) (or similar) via a session manager wrapper. When used together, you get short-term + long-term memory, exposed as tools. |

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="agent-runtime-infrastructure-layer-most-teams-underestimate-.md">
<details>
<summary>Agent Runtime: Infrastructure Layer Most Teams Underestimate | Augment Code</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer>

# Agent Runtime: Infrastructure Layer Most Teams Underestimate | Augment Code

https://cdn.sanity.io/images/oraw2u2c/production/5cf1570e0b1a16435d55206c4b19de4b80784e26-1600x900.svg

The agent runtime is the production infrastructure layer that keeps AI agents durable, isolated, and recoverable because model APIs and agent frameworks do not manage process state, resource boundaries, or crash recovery.

## TL;DR

Production AI agents require infrastructure that model APIs and agent frameworks do not provide: durable execution across crashes, per-agent resource isolation, and structured lifecycle management. Teams often discover this gap only after deployment, when prototype agent logic meets production requirements such as fault recovery, concurrency control, and long-running state management.

## Why Production Agents Need a Runtime Layer

An AI agent that works in a Jupyter notebook and an AI agent that runs reliably in production are separated by an infrastructure gap most teams discover only after deployment. The form factor matters once parallel agents or longer task horizons enter the picture, and a [QCon talk](https://www.infoq.com/presentations/multi-agent-workflow/) reported a sharp drop-off between teams planning production agent deployments and teams achieving them. The speaker characterized the gap directly: "It's really easy to hack out the really simple prototype. It's easy to get down to the first 95%. It turns out that that last 5% is just as hard as the first 95%." More recent enterprise data points to an even wider drop-off: a [Cisco survey](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m04/cisco-survey-reveals-ai-agent-readiness-gap.html) found that 85% of enterprises have AI agent pilots underway while only 5% have moved them into production.

The missing layer is the agent execution runtime: the machinery that keeps an agent running, recoverable, and isolated from other agents in a shared production environment. Frameworks like LangChain, CrewAI, and AutoGen provide prompts and tools for building AI agents. Their standard offerings rarely supply durable execution, process isolation, resource governance, or multi-tenant security, so production deployments often see pipelines succeed while agents fail at runtime. Workspaces like Intent close this gap by treating multi-agent development as a coordinated system: agents share a living spec, run in isolated git worktrees, and stay aligned as the plan evolves.

The sections ahead walk through six runtime concerns that production agent deployments require, beginning with the boundary between a runtime and a model API and ending with a production readiness checklist.

## What an Agent Runtime Includes (and How It Differs from a Model API)

An agent runtime is the infrastructure layer that provides execution-time intervention: the capacity to modify agent inputs, control flow, or execution state while the agent is actively running. The [AI Runtime paper](https://arxiv.org/html/2603.00495v2) draws a boundary around systems that intervene at execution time rather than systems that only observe failures.

The clearest practitioner-facing distinction comes from a [LangChain post on production deep agents](https://www.langchain.com/blog/runtime-behind-production-deep-agents):

> "The harness is the system you build around the model to help your agent be successful in its domain. That includes prompts, tools, skills, and anything else supporting the model and tool calling loop that defines an agent. The runtime is everything underneath: durable execution, memory, multi-tenancy, observability, the machinery that keeps an agent running in production without your team reinventing it."

A model API call is stateless: request in, response out. A production agent, by contrast, runs for minutes or hours, pauses for human approval of indeterminate duration, executes untrusted code in sandboxes, and maintains working memory across process boundaries. The runtime layer manages seven distinct concerns:

| Runtime Capability | What It Handles |
| --- | --- |
| Durable execution | Process continuity across crashes, restarts, and indefinite blocking waits |
| State management | Checkpointing, short-term and long-term memory, resumable execution context |
| Process/session isolation | Multi-tenant separation, sandbox lifecycle, OS-level cgroup enforcement |
| Resource governance | Scheduling, memory allocation, concurrency control |
| Lifecycle management | Actor creation, registration, teardown; message routing; concurrent orchestration context |
| Failure recovery | Automatic retry, resume-from-checkpoint, fault-tolerant activity execution |
| Runtime security governance | Policy enforcement on tool calls and agent actions |

Frameworks like Temporal and Ray cover slices of this surface. Augment Cosmos, currently in research preview, takes the broader framing of an operating system for agentic software development: agent runtime, context engine, event bus, and shared org knowledge layer treated as primitives that any expert agent on the platform can compose, so each team avoids rewiring those capabilities from scratch.

The [AgentCgroup paper](https://arxiv.org/html/2602.09345v2) provides the quantitative case for this layer. OS-level execution (tool calls and container/agent initialization) accounts for 56-74% of end-to-end task latency, while LLM reasoning accounts for 26-44%. Memory is the primary bottleneck for multi-tenant concurrency density, ahead of CPU. Production performance depends on both the agent runtime layer and the model inference layer.

The runtime excludes model inference, prompt engineering, agent reasoning logic (ReAct loops, chain-of-thought), tool implementations, and content safety filtering. [Microsoft's AGT](https://developer.microsoft.com/blog/securing-mcp-a-control-plane-for-agent-tool-execution) draws this boundary explicitly, framing the system as a governance layer over agent actions rather than over model outputs themselves.

## Process Isolation: Why Agents Need Their Own Execution Boundary

AI agents require dedicated execution boundaries because they are stateful, singleton workloads that violate the assumptions of traditional container orchestration. The [Kubernetes blog](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/) states it directly: "AI agents, by contrast, are typically isolated, stateful, singleton workloads. They act as a digital workspace or execution environment for an LLM. An agent needs a persistent identity and a secure scratchpad for writing and executing (often untrusted) code."

Without dedicated isolation, four specific failure modes emerge in production:

**Shared memory store poisoning.** When agents share a memory backend without namespace-level isolation enforced at the storage layer, a single write corrupts all readers simultaneously. Application-level namespace filtering is insufficient: if all tenants' data resides in one collection with boundary enforcement only via metadata query filters, a single filter bug exposes all tenants at once.

**Container escape via shared kernel.** Standard containers share the host kernel. Container security research has cataloged a long tail of vulnerabilities across the container stack, leaving uncertainty about whether container sandboxes are a safe isolation boundary for frontier LLMs.

**Resource exhaustion without cgroup enforcement.** Without per-agent memory limits enforced at the kernel level, a runaway agent's memory consumption looks indistinguishable from normal workload fluctuation until it causes host-level degradation. Per-agent cgroup enforcement is the only mechanism that contains one agent's memory spiral before it becomes the host's memory spiral.

**Cascading failures via shared dependencies.** Cascading failures in agentic AI propagate across multiple agents through shared memory, communication paths, and feedback loops, so one local fault becomes a broader system failure.

Intent addresses these failure modes at the workspace layer. Each Intent workspace is backed by an isolated git worktree, so parallel agents operate on independent branches without overwriting each other's work or sharing memory state. For background on this pattern, see the guide on [agentic development environments](https://www.augmentcode.com/guides/what-is-an-agentic-development-environment).

### The Isolation Technology Spectrum

Different isolation mechanisms offer different tradeoffs between security boundary strength and operational overhead. The table below maps the common options against kernel boundary characteristics:

| Mechanism | Kernel Boundary | Key Characteristics |
| --- | --- | --- |
| Shared process | None | Development only |
| Hardened containers | Shared host kernel | CVE-dependent escape risk |
| gVisor | Syscalls intercepted in userspace via Sentry | Kubernetes-native; compatibility tradeoffs |
| Firecracker microVM | Dedicated kernel per workload via KVM | <125ms boot, <5MiB overhead |
| Kata Containers | Dedicated kernel per workload | CRI-compatible; requires KVM |

Firecracker microVMs, used by AWS Lambda and AWS Fargate, provide a dedicated kernel per workload with boot times under 125ms and memory overhead under 5 MiB.

Namespace-scoped memory per thread at the state schema layer complements OS-level isolation at the process layer by reducing cross-agent context contamination.

## Resource Allocation: CPU, Memory, and Token Budget Management

Resource allocation for production AI agents spans three dimensions. Token budgets govern inference costs, compute resources govern execution performance, and guardrails contain runaway behavior. Each dimension requires enforcement at the runtime layer beneath the application. [Agent frameworks](https://www.augmentcode.com/guides/best-ai-agent-frameworks-production-deployment) provide API-level retry capabilities, while resource governance requires infrastructure beneath the framework.

### Token Budget Enforcement

Production token management uses a three-layer hard limit structure:

1. **Hard token limit**: absolute ceiling on tokens consumed per run
2. **Compaction threshold**: set below the hard limit, triggering context summarization before the ceiling is reached
3. **Pre-execution budget checks**: validate available budget before initiating a run

[Azure guidance](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/integrate-manage-operate) emphasizes governance, security, and operational controls for AI workloads, including quota and rate-limit mechanisms available in specific Azure AI services.

Three additional guardrail controls prevent budget overruns:

| Control Type | Mechanism | Purpose |
| --- | --- | --- |
| Monthly cap | Dollar quota that halts or reroutes the agent | Financial safety net |
| Speed limit | Executions per minute throttle | Prevents runaway usage from application bugs |
| Time limit | Maximum duration per session | Prevents agents held in open, expensive states |

### Compute Resource Management

Kubernetes v1.34 adds [Dynamic Resource Allocation (DRA) consumable capacity](https://kubernetes.io/blog/2025/09/18/kubernetes-v1-34-dra-consumable-capacity/) support for fine-grained GPU memory allocation, replacing the previous static pattern of integer GPU requests:

```yaml
DeviceCapacity{
  Value: resource.MustParse("40Gi"),
  RequestPolicy: &CapacityRequestPolicy{
    Default: ptr.To(resource.MustParse("5Gi")),
    ValidRange: &CapacityRequestPolicyRange {
      Min: ptr.To(resource.MustParse("5Gi")),
      Step: ptr.To(resource.MustParse("5Gi")),
    }
  }
}
```

This enables right-sizing GPU memory per individual agent workload rather than requiring full GPU assignment. For stateful agents that need resource adjustment without session loss, Kubernetes v1.35 marks [pod resize](https://kubernetes.io/docs/tasks/configure-pod-container/resize-container-resources/) as stable, allowing CPU and memory changes within a running Pod.

### Preventing Runaway Agents

The [Strands SDK](https://aws.amazon.com/blogs/machine-learning/strands-agents-sdk-a-technical-deep-dive-into-agent-architectures-and-observability/) recommends defining timeouts for tool calls and limiting the number of reasoning loops to avoid runaway agents. Its documentation describes built-in retry strategies rather than telling users to wrap agent invocations in custom retry loops. Appending all history to context without bounds inflates model inference costs across every model call, tool call, and retry. The result is compounding cost increases that grow faster than the linear case.

[Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) documentation discusses rate limiting and throttling as general patterns for managing resource constraints. The same documentation notes that sharing a Kernel instance across components in Semantic Kernel can produce unexpected recursive invocation patterns, including infinite loops. Context isolation must be enforced as a correctness requirement at the runtime layer, with each agent operating against its own bounded context window.

## Lifecycle Management: Startup, Heartbeat, Graceful Shutdown

Agent lifecycle management spans three phases, each with distinct operational requirements that differ from standard container workloads. Intent encodes a similar lifecycle at the workspace level: a Coordinator agent drafts the spec and delegates tasks, Implementor agents execute in parallel waves, and a Verifier agent checks results before merge. For background on this orchestration pattern, see the guide on [living specs for AI agent development](https://www.augmentcode.com/guides/living-specs-for-ai-agent-development).

### Startup: Dependency-Ordered Initialization

Agents require sequenced initialization with hard dependency enforcement. [Kubernetes init containers](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) enforce this by running each init container sequentially, where each must succeed before the next can run.

| Kubernetes Init Container | AI Agent Equivalent |
| --- | --- |
| Init container 1: DB schema migration | Load vector store index |
| Init container 2: Config validation | Validate tool credentials and API keys |
| Init container 3: Secret injection | Hydrate system prompt and prior conversation state |
| Main container starts | Agent enters ready state; probes activate |

Agent startup requires a [startup probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) with a wide `failureThreshold × periodSeconds` window because loading large embedding models or hydrating long context windows takes much longer than standard container initialization. Liveness and readiness probes do not activate until the startup probe succeeds. Conflating startup and liveness probes causes premature container restarts during legitimate slow initialization.

### Running: Three-Probe Health Monitoring

Three probe types map to specific agent operational states:

| Probe Type | Agent Meaning | Failure Action |
| --- | --- | --- |
| Startup | Context loaded, tools validated, agent ready | Block all other probes until passes |
| Liveness | Agent event loop is not deadlocked | Restart the container |
| Readiness | Agent can accept new tasks; not at capacity | Remove from load balancer; do NOT restart |

The readiness/liveness distinction is operationally significant. A liveness failure signals an unrecoverable internal fault requiring restart. A readiness failure signals a temporary inability to accept work (LLM rate limit hit, task queue full) that should drain traffic without disrupting the running agent.

For long-running tasks, [Temporal heartbeats](https://docs.temporal.io/evaluate/use-cases-design-patterns) detect stalled activities and take corrective action without waiting for a timeout. Very long-running agents commonly use the `Continue-As-New` pattern, which closes the current execution and starts a new one with a [fresh event history](https://temporal.io/blog/very-long-running-workflows).

Process lifecycle and agent lifecycle operate as separate concerns. [Temporal workflows](https://community.temporal.io/t/q-a-from-learn-how-to-build-ai-agents-with-temporal-webinar/17050) replay their history on any available worker after a process crash, so the agent migrates to a new worker rather than terminating.

### Shutdown: Graceful Termination

The [Kubernetes termination sequence](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/) follows a defined order: the Pod is marked for deletion and notified for removal from Service endpoint lists in parallel with shutdown handling, the `preStop` hook executes before `SIGTERM` is sent to the main container process, the `terminationGracePeriodSeconds` countdown applies to the total shutdown window (default 30 seconds), and `SIGKILL` is sent if the process has not exited by the deadline.

For agents with tasks that may require minutes to reach a safe checkpoint boundary, the default 30-second grace period falls short. Configure `terminationGracePeriodSeconds` based on the application's actual shutdown behavior rather than assuming a typical value.

## Failure Recovery: What Happens When an Agent Crashes Mid-Task

Agent failure recovery requires purpose-built infrastructure because the reliability math works against unprotected multi-step workflows. An agent succeeding 95% of the time on each step has only a 60% chance of completing a 10-step workflow cleanly (0.95^10 ≈ 0.599). At 90% per step, a [10-step workflow](https://arxiv.org/html/2508.13143v1) succeeds just 35% of the time.

Six failure categories appear in production agent systems, each requiring a specific recovery pattern:

| Failure Mode | Primary Recovery Pattern | Key Mechanism |
| --- | --- | --- |
| Process crash | Durable execution + replay | Event history rehydration on new worker |
| Hang / stuck agent | Supervision tree + preemptive scheduling | BEAM scheduler preemption; timeout enforcement |
| Infinite loop | Meta-controller + early stop | Hard iteration caps, repetition detection |
| Context overflow | Detect, checkpoint, clear, resume | Checkpoints with context rotation |
| Tool / API failure | Retry with idempotency key | At-least-once delivery + idempotent activities |
| Partial completion | Saga pattern + compensation | Reverse-order compensating transactions |

### Durable Execution with Event Sourcing

The foundational recovery pattern persists every state transition as an immutable event. On crash, the system replays the event log to reconstruct state and resume from the last committed point. [Temporal describes the mechanism](https://temporal.io/blog/temporal-replaces-state-machines-for-distributed-applications): "Your function could be interrupted mid-execution by a server crash, deployment, or even a planned maintenance window lasting days, and when it resumes (potentially on entirely different infrastructure), every local variable, every loop counter, every conditional branch taken is exactly as it was."

Intent applies the same principle at the spec layer. The living spec acts as the durable source of truth, so when an agent crashes mid-task, the next agent picks up against the same spec without re-deriving plan state from chat history.

### Idempotency for At-Least-Once Delivery

Replay-based crash recovery means activities execute more than once. Without idempotency, retries cause duplicate side effects. [Temporal's approach](https://temporal.io/blog/error-handling-in-distributed-systems) uses idempotency keys derived from workflow and activity identifiers (such as Workflow Run ID and Activity ID), which remain stable across retry attempts and are used together with Temporal's event history replay to preserve workflow state across crash/resume cycles.

### Saga Pattern for Partial Completion

For workflows spanning multiple external systems, a crash mid-workflow leaves some systems updated and others not. A saga breaks the workflow into independently committed steps, each with a defined compensating operation that reverses its effect during rollback. [Temporal guarantees](https://temporal.io/blog/saga-pattern-made-easy) that compensation logic runs even if the worker process crashes mid-rollback.

### Supervision Trees for Multi-Agent Systems

The [Erlang/OTP framework](https://www.erlang.org/doc/system/design_principles.html) defines hierarchical supervision with three restart strategies: `one_for_one` (only the crashed child restarts), `one_for_all` (all children restart when one crashes), and `rest_for_one` (the crashed child and all children started after it restart). The [Springdrift paper](https://arxiv.org/html/2604.04660v1) applies these properties directly to agent runtimes, noting that the BEAM scheduler preempts processes after a fixed number of reductions so a stuck or slow process cannot starve others. Teams can implement these architectural properties in Python, Go, or Rust without the BEAM VM, though hang isolation then requires explicit timeout enforcement at the process level.

Once supervision logic spans more than a handful of long-running specialists, teams typically need a shared substrate so corrections, restarts, and recoveries compound across the org rather than living in one developer's terminal. Augment Cosmos approaches this with a shared virtual filesystem, tenant and private memory, and a learning flywheel where corrections to one expert agent improve the same role for everyone on the team.

[Automated code review](https://www.augmentcode.com/guides/best-ai-code-review-tools) applied to agent tool implementations and workflow definitions catches structural patterns that lead to runtime failures, reducing the failure surface area before deployment.

## Runtime Requirements Checklist for Production Agent Deployments

Production agent runtime readiness spans five categories. Each checklist item maps to a specific failure mode documented earlier in this guide.

### Process Isolation

The first category prevents one agent's faults from contaminating others sharing the same host:

- Sandbox all execution environments for AI-suggested commands and code
- Enforce per-session compute isolation (container, microVM, or equivalent)
- Implement namespace-scoped memory per agent thread at the storage layer
- Assign individual service identities to agents; never use human credentials
- Deploy at least one deterministic (non-LLM) enforcement layer for [access control](https://arxiv.org/html/2603.12230v2)

### Resource Governance

Resource governance bounds the cost and concurrency profile of every agent invocation:

- Configure token quotas at the individual agent level, not only at the application level
- Define a maximum number of reasoning loops per agent invocation
- Define timeouts for individual tool calls, not only for the overall invocation
- Configure both minimum AND maximum bounds on agent compute pools
- Implement rate limiting and connection pooling at the service level
- Monitor token usage per query and tool error rates with anomaly alerts

### Lifecycle Management

Lifecycle controls govern startup, in-flight health, and graceful shutdown behavior:

- Implement startup probes with extended failure thresholds for model/context loading
- Separate liveness probes (deadlock detection, triggers restart) from readiness probes (capacity check, drains traffic)
- Set `terminationGracePeriodSeconds` to match task completion horizon, not the 30-second default
- Use `preStop` hooks for state checkpointing and in-flight task draining
- Externalize all session state; workers must be [stateless by design](https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components)

### Failure Recovery

Recovery patterns determine whether a crash loses partial work or resumes cleanly:

- Implement durable execution with event sourcing for crash recovery
- Thread idempotency keys through every tool call that produces side effects
- Design saga-pattern compensation logic for multi-system workflows
- Route unrecoverable tasks to dead letter queues for inspection and manual replay
- Apply hard iteration caps and repetition detection to prevent infinite loops
- Instrument [OpenTelemetry spans](https://opentelemetry.io/blog/2025/ai-agent-observability/) using `gen_ai.operation.name` for model calls, tool executions, and agent invocations

### Observability

Observability closes the loop, surfacing the cost, quality, and reliability signals that inform every other category:

- Capture on every span: model name, token counts, tool parameters, start/end time, duration, status
- Track reliability metrics: invocation counts, error rates, request duration, concurrency
- Track cost metrics: token spend, GPU minutes, cost-per-request
- Configure alerts for latency spikes, error rate increases, and quality score drops
- Implement appropriate monitoring and review processes as part of your compliance approach

## Build Runtime-First Before Scaling Agent Count

The prototype-to-production gap for AI agents is a structural problem in the infrastructure stack, surfacing only under production load through state loss, resource contention, cascading failures, and silent quality degradation. The runtime layer dominates both latency and reliability characteristics of production agent systems, sitting beneath the model layer rather than alongside it.

The concrete next step is to audit the current agent deployment against the checklist in this guide. Start with process isolation and failure recovery. These two capabilities prevent the highest-severity production incidents (data corruption, cascading failures, and unrecoverable state loss) and establish the foundation for safe scaling.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="crewai-s-genuinely-unique-features-an-honest-technical-deep-.md">
<details>
<summary>crewai-s-genuinely-unique-features-an-honest-technical-deep-</summary>

Phase: [EXPLORATION]

**Source URL:** <https://vadim.blog/crewai-unique-features>

**TL;DR** — CrewAI's real uniqueness is that it models problems as _"build a team of people"_ rather than _"build a graph of nodes"_ (LangGraph) or _"build a conversation"_ (AutoGen). The **Crews + Flows dual-layer architecture** is the core differentiator. The role-playing persona system and autonomous delegation are ergonomic wins, not technical breakthroughs. The hierarchical manager is conceptually appealing but broken in practice. This post separates what's genuinely novel from what's marketing.

## The Mental Model That Matters

Every agent framework makes a bet on how you should think about multi-agent systems:

| Framework | Mental Model | Core Abstraction |
| --- | --- | --- |
| **CrewAI** | Build a team of people | Roles, delegation, management hierarchy |
| **LangGraph** | Build a graph of nodes | State machines, edges, typed checkpoints |
| **AutoGen** | Build a conversation | Message passing, group chat, turn-taking |
| **OpenAI Agents SDK** | Build a pipeline | Handoffs, guardrails, MCP tools |

CrewAI's bet is organizational. If your instinct when solving a problem is to think _"I need a researcher, a writer, and an editor"_ rather than _"I need node A to pass state to node B"_, CrewAI maps to your mental model natively.

But does that metaphor translate into genuinely distinct technical capabilities? Let's find out.

> **Hot take:** The "build a team of people" metaphor is CrewAI's greatest strength _and_ its ceiling. It's brilliant onboarding — product managers grok it in five minutes. But organizations aren't efficient. Real teams have politics, miscommunication, and redundant meetings. CrewAI accidentally inherited those failure modes too. The metaphor stops being helpful the moment you need your agents to do something no human org chart would describe.

## 1\. The Role-Playing Persona System

Every CrewAI agent is defined with three fields — `role`, `goal`, and `backstory`:

```python
from crewai import Agent

researcher = Agent(
    role="Senior AI Research Analyst",
    goal="Uncover cutting-edge developments in multi-agent systems",
    backstory="""You are a veteran research analyst with 15 years
    in AI/ML. You have a reputation for finding non-obvious
    connections between papers and identifying hype vs substance.""",
    allow_delegation=True,
    verbose=True,
)
```

Under the hood, these fields are injected into the system prompt. The agent then uses a **ReAct loop** (Reason + Act) — generating interleaved Thought, Action, and Observation steps. The persona fields bias the LLM's reasoning toward domain-specific behavior.

**Is this novel?** No. Role-playing prompting is well-studied — the [RoleLLM paper (ACL 2024)](https://arxiv.org/abs/2310.00746) benchmarked role-playing abilities across LLMs. Any framework (or raw API call) can achieve the same effect with a system prompt.

**What CrewAI actually did:** Made it a **first-class API primitive** rather than something you do manually. This is an ergonomic win — it standardizes agent definitions, makes them readable by non-engineers, and encourages good prompt engineering practices. Other frameworks treat agents as function executors; CrewAI treats them as characters with identities.

There are no published benchmarks showing CrewAI's role/goal/backstory triple outperforms other persona approaches. The value is in the standardized structure, not in any novel mechanism.

> **Hot take:** The role/goal/backstory triple is prompt engineering with guardrails — and that's _fine_. The industry keeps looking for magic in agent definitions when the real leverage is in how agents hand off work. Nobody's production system ever failed because the backstory wasn't vivid enough. It failed because agent A hallucinated a result and agent B trusted it blindly. CrewAI's persona system solves a developer experience problem, not a reliability problem. Stop optimizing your backstories and start auditing your tool outputs.

## 2\. Crews + Flows: The Strongest Differentiator

This is where CrewAI genuinely separates itself. The framework provides two orchestration layers as first-class concepts:

-   **Crews** = autonomous agent teams. You define agents and tasks; the crew handles coordination.
-   **Flows** = deterministic, event-driven workflow orchestration using Python decorators.

```mermaid
graph TD
    A[good] --> B[Flow - deterministic backbone]
    B --> C[@start() fetch_data]
    C --> D[@listen(fetch_data) validate]
    D --> E[@router() quality_check]
    E -- if quality high --> F[run_analysis_crew()]
    F --> G[(autonomous agents)]
    E -- if quality low --> H[run_cleanup_crew()]
    H --> I[(autonomous agents)]
    F --> J[@listen(both) generate_report]
    I --> J
    K[poor] --> B
```

Here's what that looks like in code:

```python
from crewai.flow.flow import Flow, listen, start, router

class ContentPipeline(Flow):
    @start()
    def fetch_sources(self):
        # Deterministic: fetch data, no LLM needed
        return {"sources": scrape_urls(self.state.urls)}

    @listen(fetch_sources)
    def validate_sources(self, sources):
        # Deterministic: filter, deduplicate
        return [s for s in sources if s["quality"] > 0.7]

    @router(validate_sources)
    def route_by_quality(self, validated):
        if len(validated) > 5:
            return "deep_analysis"
        return "quick_summary"

    @listen("deep_analysis")
    def run_research_crew(self, sources):
        # Autonomous: agents decide how to analyze
        crew = Crew(
            agents=[researcher, analyst, writer],
            tasks=[research_task, analysis_task, writing_task],
            process=Process.sequential,
        )
        return crew.kickoff(inputs={"sources": sources})

    @listen("quick_summary")
    def run_summary_crew(self, sources):
        crew = Crew(
            agents=[summarizer],
            tasks=[summary_task],
        )
        return crew.kickoff(inputs={"sources": sources})
```

**Why this matters:**

-   **Prototype with Crews alone**, then wrap production guardrails via Flows without rewriting
-   **Deterministic control where you need it** (data fetching, validation, routing) + **autonomous reasoning where it adds value** (analysis, writing)
-   Flows support `and_()` / `or_()` logical operators, FlowState (Pydantic models), and human-in-the-loop via listener resumability
-   **Each task output is a natural HITL checkpoint** — in regulated industries, this gives auditors and compliance teams a clear intervention point, unlike a continuous chat stream or opaque graph state

**How competitors compare:**

-   **LangGraph:** Graph-only. Everything is nodes and edges with typed state. You get fine-grained control but must model _everything_ as graph transitions — including parts that don't need LLM reasoning.
-   **AutoGen:** Conversation-only (historically). Agents communicate through message passing. Less structural control over workflow ordering.
-   **CrewAI:** Both layers as first-class concepts. The separation is the architectural signature.

**The trade-off:** LangGraph gives you more precise control over every state transition. If you need complex cycles, intricate error recovery, or non-linear reasoning paths, LangGraph handles these patterns more naturally. CrewAI's Flows are thinner and more opinionated.

> **Hot take:** Crews + Flows is the only feature on this page that justifies CrewAI's existence as a separate framework. Everything else — personas, delegation, YAML config — is syntactic sugar you could build in a weekend. But the _idea_ that your deterministic pipeline and your autonomous agents should live in different abstraction layers, composed together? That's a genuine architectural insight. LangGraph makes you model your data-fetching step as a graph node with typed state, which is absurd. CrewAI lets it be a Python function. The irony is that most CrewAI tutorials never even mention Flows — they stop at Crews and wonder why production falls apart.

## 3\. Autonomous Inter-Agent Delegation

When `allow_delegation=True` on an agent, CrewAI converts all other agents in the crew into **tools** available to that agent. Two tools are auto-generated:

1.  **`delegate_work`** — assigns a sub-task to another agent by role name, with context
2.  **`ask_question`** — sends a question to another agent and gets a response

```python
researcher = Agent(
    role="Researcher",
    allow_delegation=True,
    # This agent can now delegate to any other agent in the crew
)

editor = Agent(
    role="Editor",
    allowed_agents=["Fact Checker", "Style Guide"],
    # Restricts delegation to specific agents only
)
```

The agent's LLM decides **at runtime** whether to invoke these tools during its ReAct reasoning loop. This means delegation is **emergent from the LLM's tool-calling behavior**, not pre-defined in a graph or conversation protocol.

**How this differs:**

| Framework | Routing Mechanism |
| --- | --- |
| **CrewAI** | Emergent — LLM decides via tool calls at runtime |
| **LangGraph** | Explicit — developer defines graph edges |
| **AutoGen** | Conversational — agents talk, manager routes |

The `allowed_agents` parameter (recently added) restricts which agents a given agent can delegate to, enabling hierarchical organizational structures and reducing "choice paralysis" from too many delegation targets.

**Known issue:** As of March 2026, [bug #4783](https://github.com/crewAIInc/crewAI/issues/4783) documents that hierarchical process delegation can fail — manager agents cannot delegate to worker agents even with `allow_delegation=True`.

## 4\. Auto-Generated Manager Agent (Caveat Emptor)

When you set `process=Process.hierarchical`, CrewAI auto-creates a manager agent that coordinates the crew:

```python
crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process=Process.hierarchical,
    manager_llm="gpt-4",  # Required for hierarchical
)
```

The manager receives the overall goal and the list of available workers. It decides which agents to activate, in what order, with what context, and whether results are sufficient.

**The reality:** A detailed [Towards Data Science investigation (Nov 2025)](https://towardsdatascience.com/why-crewais-manager-worker-architecture-fails-and-how-to-fix-it/) found:

-   The manager **does not selectively delegate** — CrewAI executes all tasks sequentially regardless
-   The manager lacks conditional branching or true delegation enforcement
-   The final response is determined by whichever task runs last, not by intelligent synthesis
-   This causes incorrect agent invocation, overwritten outputs, and inflated token usage

**The workaround:** Define a custom manager agent with explicit step-by-step instructions that enforce conditional routing. The built-in auto-generated manager is too generic to handle real coordination.

The concept is appealing — describe your team and CrewAI auto-generates a coordinator. In practice, the implementation is unreliable. If you use hierarchical mode, plan to write a custom manager with detailed prompts.

> **Hot take:** The hierarchical manager is CrewAI's most telling failure. It reveals the gap between the framework's _metaphor_ and its _implementation_. In a real company, a manager who ignores delegation structure and runs every task sequentially gets fired. CrewAI's auto-generated manager does exactly that — and the framework calls it "hierarchical process." This isn't a bug to be patched; it's a sign that LLMs are bad managers. They lack the judgment to dynamically allocate work across agents. Until models get significantly better at meta-reasoning about task decomposition, "auto-generated coordination" will remain a demo feature, not a production one. Write your own manager prompt or use sequential mode. At least sequential is honest about what it does.

## 5\. Zero LangChain Dependency

Starting with [version 0.86.0](https://x.com/joaomdmoura/status/1867585281177637073), CrewAI removed LangChain entirely and replaced it with **LiteLLM** for LLM provider abstraction.

**Concrete benefits:**

-   **Reduced dependency tree** — LangChain pulls in dozens of transitive dependencies. Removing it makes `pip install crewai` faster and reduces version conflicts
-   **Faster execution** — CrewAI claims 5.76x faster execution than LangGraph in certain QA benchmarks, partly attributed to reduced overhead
-   **No version lock-in** — LangChain's rapid release cadence caused frequent breaking changes for downstream projects

**The nuance:** "Built from scratch" is somewhat marketing language — CrewAI still uses LiteLLM, ChromaDB, and other libraries. The benefit is real (removed a problematic dependency) but should be understood as a sustainability decision, not a "we wrote everything in-house" claim.

## What's NOT Unique (Despite the Marketing)

Let's be direct about what every framework does:

-   **Multi-agent collaboration** — AutoGen, LangGraph, OpenAgents, Pydantic AI all do this
-   **Tool integration** — every framework supports function calling and external tools
-   **LLM-agnostic support** — standard across all major frameworks via LiteLLM or similar
-   **YAML-based configuration** — convenient, not novel
-   **Memory** — LangGraph arguably has more sophisticated state persistence with typed checkpoints

## The Memory System: Interesting but Not a Differentiator

CrewAI's unified `Memory` class uses an LLM to analyze content at save time:

| Memory Type | Backend | Purpose |
| --- | --- | --- |
| Short-term | ChromaDB (vector) | Current session context via RAG |
| Long-term | SQLite3 (relational) | Cross-session insights |
| Entity | ChromaDB (vector) | People, places, organizations |
| Contextual | Composite | Combines all above for task injection |

The **RecallFlow** system offers adaptive depth recall — a multi-step pipeline with query analysis, parallel vector search, and confidence-based routing. Queries under 200 characters skip LLM analysis to save 1-3 seconds per recall.

**vs. LangGraph:** LangGraph has **state**, not memory. State is typed, persisted via checkpointing, and uses reducer logic for concurrent updates. It's explicit and developer-controlled. LangGraph is more powerful for workflows requiring exact state tracking. CrewAI is easier when you want agents to "remember" without managing state manually.

## Honest Limitations

1.  **Higher token consumption.** Multiple sources confirm LangGraph achieves lower latency and token usage in production. CrewAI's role-playing prompts and ReAct loops add overhead. Common pattern: _prototype in CrewAI, rewrite in LangGraph when token cost matters._

2.  **Hierarchical process is broken.** The auto-generated manager doesn't selectively delegate. Documented in TDS, GitHub issues, and community forums.

3.  **Limited flexibility for non-task workflows.** Dynamic conversational agents, complex cycles, fine-grained state transitions — CrewAI becomes awkward. LangGraph handles these better.

4.  **Debugging is painful.** Print/log statements inside tasks don't work reliably. Time spent debugging often exceeds build time. Observability has improved but lags behind LangGraph's built-in tracing.

5.  **Not ideal for stateful, long-running workflows.** LangGraph's checkpoint-based persistence and durable execution model is stronger.

6.  **Enterprise claims need scrutiny.** "60% of Fortune 500" is self-reported survey data. "Use" could mean a single team ran a proof-of-concept.

7.  **Deployment security is an ecosystem-wide gap.** Autonomous agents that execute code need secure runtime isolation. NVIDIA's recent open-source [OpenShell](https://www.marktechpost.com/2026/03/18/nvidia-ai-open-sources-openshell-a-secure-runtime-environment-for-autonomous-ai-agents/) addresses this for any framework. CrewAI's modular task structure is easier to containerize than a bespoke graph, but the hard security problems are upstream of any framework choice.

## Where CrewAI Genuinely Wins

-   **Fastest idea-to-prototype** — ~40% faster than LangGraph for getting a working multi-agent system
-   **Most readable agent definitions** — role/goal/backstory is immediately understandable by non-engineers
-   **Dual-layer architecture** — Crews + Flows is a genuine production pattern no other framework offers natively
-   **Strongest enterprise platform** — [CrewAI AMP](https://crewai.com/amp) offers a visual builder, real-time tracing, and managed deployment (SOC2, SSO)
-   **Largest community** — 44,500+ GitHub stars, 100K+ developers on learn.crewai.com
-   **Named customers** — DocuSign (75% faster lead time-to-contact), PwC (10% to 70% code gen accuracy), IBM, PepsiCo, NVIDIA

## The Decision Framework

```mermaid
graph TD
    A[What's your mental model?]
    A --> B{Roles & delegation}
    B --> CrewAI
    A --> C{Graphs & state machines}
    C --> LangGraph
    A --> D{Conversations & dialog}
    D --> AutoGen
    A --> E{Simple pipelines + MCP}
    E --> OpenAI_Agents_SDK
    A --> F{Type safety first}
    F --> Pydantic_AI
```

| Choose | When |
| --- | --- |
| **CrewAI** | Your problem decomposes into roles. You want fast prototyping. You need Crews + Flows dual-layer for production. |
| **LangGraph** | You need precise control flow, lower token cost, complex cycles, durable execution, or fine-grained state. |
| **OpenAI Agents SDK** | You want simplicity with native MCP support and near-LangGraph efficiency. |
| **AutoGen** | Your use case is dialog-heavy — brainstorming, negotiation, customer support with emergent paths. |
| **Pydantic AI** | Type safety and multi-provider flexibility matter. You want agent logic errors caught at dev time. |

## FAQ

**Q: Is CrewAI built on top of LangChain?**
A: No. CrewAI removed its LangChain dependency entirely in version 0.86.0 and now uses LiteLLM for LLM provider abstraction. This reduced the dependency tree, eliminated version conflicts, and improved execution speed.

**Q: What is the main difference between CrewAI and AutoGen?**
A: The main difference is architectural: CrewAI uses a structured Crew-Agent-Task hierarchy with deterministic orchestration (sequential or hierarchical processes), while AutoGen relies on conversational loops between agents, which can be more flexible but less deterministic.

**Q: Can CrewAI agents use custom tools?**
A: Yes. CrewAI agents can be equipped with custom tools for web searches, API calls, code execution, and more. The framework provides built-in tools and supports custom tool definitions via Python functions.

**Q: Is CrewAI suitable for complex, stateful workflows?**
A: For highly complex, stateful workflows with intricate conditional logic and cycles, LangGraph's explicit graph-based control flow offers more granular control. CrewAI's strength is linear, collaborative processes — use Crews + Flows for production, or embed a LangGraph sub-graph for complex reasoning within a single agent.

**Q: Is CrewAI better than LangGraph for production?**
A: It depends on the workflow. For production systems involving linear, collaborative business processes where clarity and human oversight are critical, CrewAI's high-level abstraction is faster to build and easier to maintain. For systems requiring custom, non-linear state management or lower token costs, LangGraph provides the necessary control.

## The Bottom Line

Strip away the marketing, and CrewAI's genuine contribution to the multi-agent ecosystem is **one architectural insight**: separate deterministic orchestration (Flows) from autonomous reasoning (Crews), and give developers both as first-class primitives. The role-playing system is an ergonomic win. The autonomous delegation is clever but fragile. The hierarchical manager needs work.

If your problem maps to the organizational metaphor — roles, delegation, management — CrewAI will get you to a working system faster than anything else. If your problem maps to state machines, graphs, or complex control flow, look elsewhere.

The frameworks aren't mutually exclusive. A pragmatic 2026 architecture might use CrewAI Flows for high-level orchestration while embedding a LangGraph sub-graph for a particularly complex reasoning task within a single agent's execution. The ecosystems may converge, but their core architectural DNA will continue to dictate their ideal use cases.

---

_Sources: [CrewAI Documentation](https://docs.crewai.com/), [CrewAI GitHub](https://github.com/crewAIInc/crewAI), [LangGraph Documentation](https://langchain-ai.github.io/langgraph/), [AutoGen Documentation](https://microsoft.github.io/autogen/), [TDS: Why CrewAI's Manager-Worker Architecture Fails](https://towardsdatascience.com/why-crewais-manager-worker-architecture-fails-and-how-to-fix-it/), [CrewAI AMP](https://crewai.com/amp), [RoleLLM (ACL 2024)](https://arxiv.org/abs/2310.00746)_

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="how-to-think-about-agent-frameworks.md">
<details>
<summary>How to think about agent frameworks</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.langchain.com/blog/how-to-think-about-agent-frameworks>

# How to think about agent frameworks

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a056ea05f3880a1361b47cf_Harrison.avif

Harrison Chase

April 20, 2025

https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg

20

min

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad00d2a13d9d604fd524_Screenshot-2025-04-20-at-10.19.41-AM.png

**TL;DR:**

- **The hard part of building reliable agentic systems is making sure the LLM has the appropriate context at each step. This includes both controlling the exact content that goes into the LLM, as well as running the appropriate steps to generate relevant content.**
- **Agentic systems consist of both workflows and agents (and everything in between).**
- **Most agentic frameworks are neither declarative or imperative orchestration frameworks, but rather just a set of agent abstractions.**
- **Agent abstractions can make it easy to get started, but they can often obfuscate and make it hard to make sure the LLM has the appropriate context at each step.**
- **Agentic systems of all shapes and sizes (agents or workflows) all benefit from the same set of helpful features, which can be provided by a framework, or built from scratch.**
- **LangGraph is best thought of as a orchestration framework (with both declarative and imperative APIs), with a series of agent abstractions built on top.**

OpenAI recently released a guide on building agents which contains some misguided takes like the below:

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd53d_Go0FliaXoAANDWD.jpeg

This callout initially angered me, but after starting to write a response I realized: thinking about agent frameworks is complicated! There are probably 100 different agent frameworks, there are a lot of different axes to compare them on, sometimes they get conflated (like in this quote). There is a lot of hype, posturing, and noise out there. There is very little precise analysis or thinking being done about agent frameworks. This blog is our attempt to do so. We will cover:

- **Background Info**
  - What is an agent?
  - What is hard about building agents?
  - What is LangGraph?
- **Flavors of agentic frameworks**
  - “Agents” vs “workflows”
  - Declarative vs non-declarative
  - Agent abstractions
  - Multi agent
- **Common Questions**
  - What is the value of a framework?
  - As the models get better, will everything become agents instead of workflows?
  - What did OpenAI get wrong in their take?
  - How do all the agent frameworks compare?

Throughout this blog I will make repeated references to a few materials:

- [OpenAI’s guide on building agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf?ref=blog.langchain.com) (which I don’t think is particularly good)
- [Anthropic’s guide on building effective agents](https://www.anthropic.com/engineering/building-effective-agents?ref=blog.langchain.com) (which I like a lot)
- [LangGraph](https://github.com/langchain-ai/langgraph?ref=blog.langchain.com) (our framework for building reliable agents)

# Background info

Helpful context to set the stage for the rest of the blog.

## What is an agent

There is no consistent definition of an agent, and they are often offered through different lenses.

OpenAI takes a higher level, more thought-leadery approach to defining an agent.

> Agents are systems that independently accomplish tasks on your behalf.

I am personally not a fan of this. This is a vague statement that doesn’t really help me understand what an agent is. It’s just thought-leadership and not practical at all.

Compare this to Anthropic’s definition:

> "Agent" can be defined in several ways. Some customers define agents as fully autonomous systems that operate independently over extended periods, using various tools to accomplish complex tasks. Others use the term to describe more prescriptive implementations that follow predefined workflows. At Anthropic, we categorize all these variations as **agentic systems**, but draw an important architectural distinction between **workflows** and **agents**:
>
> **Workflows** are systems where LLMs and tools are orchestrated through predefined code paths.
>
> **Agents**, on the other hand, are systems where LLMs dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks.

I like Anthropic’s definition better for a few reasons:

- Their definition of an agent is much more precise and technical.
- They also make reference to the concept of “agentic systems”, and categorize both workflows and agents as variants of this. I **love** this.

💡

Nearly all of the “agentic systems” we see in production are a **combination** of “workflows” and “agents”.

Later in the blog post, Anthropic defines agents as “… typically just LLMs using tools based on environmental feedback in a loop.”

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd540_58d9f10c985c4eb5d53798dea315f7bb5ab6249e-2401x1000.webp

Despite their grandiose definition of an agent at the start, this is basically what OpenAI means as well.

These types of agents are parameterized by:

- The model to use
- The instructions (system prompt) to use
- The tools to use

You call the model in a loop. If/when it decides to call a tool, you run that tool, get some observation/feedback, and then pass that back into the LLM. You run until the LLM decides to not call a tool (or it calls a tool that triggers a stopping criteria).

Both OpenAI and Anthropic call out workflows as being a different design pattern than agents. The LLM is less in control there, the flow is more deterministic. This is a helpful distinction!

Both OpenAI and Anthropic explicitly call out that you do not always need agents. In many cases, workflows are simpler, more reliable, cheaper, faster, and more performant. A great quote from the Anthropic post:

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.
>
> When more complexity is warranted, workflows offer predictability and consistency for well-defined tasks, whereas agents are the better option when flexibility and model-driven decision-making are needed at scale.

OpenAI says something similar:

> Before committing to building an agent, validate that your use case can meet these criteria clearly. Otherwise, a deterministic solution may suffice.

In practice, we see that most “agentic systems” are a combination of workflows and agents. This is why I actually **hate** talking about whether something is an agent, but prefer talking about how agentic a system is. h/t the great Andrew Ng for this way of [thinking about things](https://x.com/AndrewYNg/status/1801295202788983136?ref=blog.langchain.com):

> Rather than having to choose whether or not something is an agent in a binary way, I thought, it would be more useful to think of systems as being agent-like to different degrees. Unlike the noun “agent,” the adjective “agentic” allows us to contemplate such systems and include all of them in this growing movement.

## What is hard about building agents?

I think most people would agree that building agents is hard. Or rather - building an agent as a prototype is easy, but a reliable one, that can power business-critical applications? That is hard.

The tricky part is exactly that - making it reliable. You can make a demo that looks good on Twitter easily. But can you run it to power a business critical application? Not without a lot of work.

We did a survey of agent builders a few months ago and asked them: _“What is your biggest limitation of putting more agents in production?”_ The number one response by far was “performance quality” - it’s still really hard to make these agents work.

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd554_67347b1aed9686aad4544fef_9.-What-is-your-biggest-limitation.svg

_What causes agents to perform poorly sometimes?_ The LLM messes up.

_Why does the LLM mess up?_ Two reasons: (a) the model is not good enough, (b) the wrong (or incomplete) context is being passed to the model.

From our experience, it is very frequently the second use case. What causes this?

- Incomplete or short system messages
- Vague user input
- Not having access to the right tools
- Poor tool descriptions
- Not passing in the right context
- Poorly formatted tool responses

💡

**The hard part of building reliable agentic systems is making sure the LLM has the appropriate context at each step. This includes both controlling the exact content that goes into the LLM, as well as running the appropriate steps to generate relevant content.**

As we discuss agent frameworks, it’s helpful to keep this in mind. Any framework that makes it harder to control **exactly** what is being passed to the LLM is just getting in your way. It’s already hard enough to pass the correct context to the LLM - why would you make it harder on yourself?

## What is LangGraph

💡

LangGraph is best thought of as a orchestration framework (with both declarative and imperative APIs), with a series of agent abstractions built on top.

LangGraph is an event-driven framework for building agentic systems. The two most common ways of using it are through:

- a [declarative, graph-based syntax](https://langchain-ai.github.io/langgraph/tutorials/introduction/?ref=blog.langchain.com)
- [agent abstractions](https://langchain-ai.github.io/langgraph/agents/overview/?ref=blog.langchain.com) (built on top of the lower level framework)

LangGraph also supports a [functional API](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com), as well as the underlying [event-driven API](https://langchain-ai.github.io/langgraph/concepts/pregel/?ref=blog.langchain.com). There exist both [Python](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com) and [Typescript](https://langchain-ai.github.io/langgraphjs/?ref=blog.langchain.com) variants.

Agentic systems can be represented as [nodes](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#nodes) and [edges](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#edges). Nodes represent units of work, while edges represent transitions. Nodes and edges are nothing more than normal Python or TypeScript code - so while the structure of the graph is represented in a declarative manner, the inner functioning of the graph’s logic is normal, imperative code. Edges can be either [fixed](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#normal-edges) or [conditional](https://langchain-ai.github.io/langgraph/concepts/low_level/?ref=blog.langchain.com#conditional-edges). So while the structure of the graph is declarative, the path through the graph can be completely dynamic.

LangGraph comes with a [built-in persistence layer](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com). This enables [fault tolerance](https://langchain-ai.github.io/langgraph/concepts/persistence/?h=fault+to&ref=blog.langchain.com#fault-tolerance), [short-term memory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#short-term-memory), and [long-term memory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#long-term-memory).

This persistence layer also enables “ [human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?ref=blog.langchain.com)” and “ [human-on-the-loop](https://langchain-ai.github.io/langgraph/concepts/time-travel/?ref=blog.langchain.com)” patterns, such as interrupt, approve, resume, and time travel.

LangGraph has built-in support for [streaming](https://langchain-ai.github.io/langgraph/concepts/streaming/?ref=blog.langchain.com): of tokens, node updates, and arbitrary events.

LangGraph integrates seamlessly with [LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com) for debugging, evaluation, and observability.

# Flavors of agentic frameworks

Agentic frameworks are different across a few dimensions. Understanding - and not conflating - these dimensions is key to being able to properly compare agentic frameworks.

## Workflows vs Agents

Most frameworks contain higher level agent abstractions. Some frameworks include some abstraction for common workflows. LangGraph is a low level orchestration framework for building agentic systems. LangGraph supports [workflows, agents, and anything in-between](https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/?ref=blog.langchain.com). We think this is crucial. As mentioned, most agentic systems in production are a combination of workflows and agents. A production-ready framework needs to support both.

Let’s remember what is hard about building reliable agents - making sure the LLM has the right context. Part of why workflows are useful is that they make it easy to pass the right context to LLMs. You decide exactly how the data flows.

As you think about where on spectrum of “workflow” to “agent” you want to build your application, there are two things to think about:

- Predictability vs agency
- Low floor, high ceiling

**Predictability vs agency**

As your system becomes more agentic, it will become less predictable.

Sometimes you want or need your system to be predictable - for user trust, regulatory reasons, or other.

Reliability does not track 100% with predictability, but in practice they can be closely related.

Where you want to be on this curve is pretty specific to your application. LangGraph can be used to build applications anywhere on this curve, allowing you to move to the point on the curve that you want to be.

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd547_Screenshot-2025-04-20-at-10.43.31-AM.png

**High floor, low ceiling**

When thinking about frameworks, it can be helpful to think about their floors and ceilings:

- Low floor: A **low floor** framework is beginner-friendly and easy to get started with
- High floor: A framework with a **high floor** means it has a steep learning curve and requires significant knowledge or expertise to begin using it effectively.
- Low ceiling: A framework with a **low ceiling** means it has limitations on what can be accomplished with it (you will quickly outgrow it).
- High ceiling: A **high ceiling** framework offers extensive capabilities and flexibility for advanced use cases (it grows with you?).

Workflow frameworks offer a high ceiling, but come with a high floor - you have to write lot of the agent logic yourself.

Agent frameworks are low floor, but low ceiling - easy to get started with, but not enough for non-trivial use cases.

LangGraph aims to have aspects that are low floor ( [built-in agent abstractions](https://langchain-ai.github.io/langgraph/agents/overview/?ref=blog.langchain.com) that make it easy to get started) but also high ceiling ( [low-level functionality](https://langchain-ai.github.io/langgraph/?ref=blog.langchain.com) to achieve advanced use cases).

## Declarative vs non-declarative

There are benefits to declarative frameworks. There are also downsides. This is a seemingly endless debate among programmers, and everyone has their own preferences.

When people say non-declarative, they are usually implying imperative as the alternative.

Most people would describe LangGraph as a declarative framework. This is only partially true.

First - while the connections between the nodes and edges are done in a declarative manner, the actual nodes and edges are nothing more than Python or TypeScript functions. Therefore, LangGraph is kind of a blend between declarative and imperative.

Second - we actually support other APIs besides the recommended declarative API. Specifically, we support both [functional](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com) and [event-driven APIs](https://langchain-ai.github.io/langgraph/concepts/pregel/?ref=blog.langchain.com). While we think the declarative API is a useful mental model, we also recognize it is not for everyone.

A common comment about LangGraph is that is like Tensorflow (a declarative deep learning framework), while frameworks like Agents SDK are like Pytorch (an imperative deep learning framework).

This is just incorrect. Frameworks like Agents SDK (and original LangChain, CrewAI, etc) are neither declarative or imperative - they are just abstractions. They have an agent abstraction (a Python class) and it contains a bunch of internal logic that runs the agent. They’re not really orchestration frameworks. They are just abstractions.

## Agent Abstractions

Most agent frameworks contain an agent abstraction. They usually start as a class that involves a prompt, model, and tools. Then they add in a few more parameters… then a few more… then even more. Eventually you end up with a litany of parameters that control a multitude of behaviors, all abstracted behind a class. If you want to see what’s going on, or change the logic, you have to go into the class and modify the source code.

💡

These abstractions end up making it really really hard to understand or control exactly what is going into the LLM at all steps. This is important - having this control is crucial for building reliable agents (as discussed above). This is the danger of agent abstractions.

We learned this the hard way. This was the issue with the original LangChain chains and agents. They provided abstractions that got in the way. One of those original abstractions from two years ago was an agent class that took in a model, prompt, and tools. This isn’t a new concept. It didn’t provide enough control back then, and it doesn’t now.

To be clear, there is some value in these agent abstractions. It makes it easier to get started. But I don’t think these agent abstractions are good enough to build reliable agents yet (and maybe ever).

We think the best way to think about these agent abstractions is like Keras. They provide higher level abstractions to get started easily. But it’s crucial to make sure they are built on top of a lower level framework so you don’t outgrow it.

That is why we have built agent abstractions on top of LangGraph. This provides an easy way to get started with agents, but if you need to escape to lower-level LangGraph you easily can.

## Multi Agent

Oftentimes agentic systems won’t just contain one agent, they will contain multiple. OpenAI says in their report:

> For many complex workflows, splitting up prompts and tools across multiple agents allows for improved performance and scalability. When your agents fail to follow complicated instructions or consistently select incorrect tools, you may need to further divide your system and introduce more distinct agents.

💡

The key part of multi agent systems is how they communicate. Again, the hard part of building agents is getting the right context to LLMs. Communication between these agents is important.

There a bunch of ways to do this! Handoffs are one way. This is an agent abstraction from Agents SDK that I actually quite like.

But the best way for these agents to communicate can sometimes be workflows. Take all the workflow diagrams in Anthropic’s blog post, and replace the LLM calls with agents. This blend of workflows and agents often gives the best reliability.

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd543_7418719e3dab222dccb379b8879e1dc08ad34c78-2401x1000.webp

Again - agentic systems are not just workflows, or just an agent. They can be - and often are - a combination of the two. As Anthropic points out in their blog post:

> **Combining and customizing these patterns**
>
> These building blocks aren't prescriptive. They're common patterns that developers can shape and combine to fit different use cases.

# Common Questions

Having defined and explored the different axes that you should be evaluating frameworks on, let’s now try to answer some common questions.

## What is the value of a framework?

We often see people questioning whether they need a framework to build agentic systems. What value can agent frameworks provide?

**Agent abstractions**

Frameworks are generically useful because they contain useful abstractions which make it easy to get started and provide a common way for engineers to build, making it easier to onboard and maintain projects. As mentioned above, there are real downsides to agent abstractions as well. For most agent frameworks, this is the sole value they provide. We worked really hard to make sure this was not case for LangGraph.

**Short term memory**

Most agentic applications today involve some sort of multi-turn (e.g. chat) component. LangGraph provides [production ready storage to enable multi-turn experiences (threads)](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#short-term-memory).

**Long term memory**

While still early, I am very bullish on agentic systems learning from their experiences (e.g. remembering things across conversations). LangGraph provides [production ready storage for cross-thread memory](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com#long-term-memory).

**Human-in-the-loop**

Many agentic systems are made better with some human-in-the-loop component. Examples include getting feedback from the user, approving a tool call, or editing tool call arguments. LangGraph provides [built in support to enable these workflows in a production system](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?ref=blog.langchain.com).

**Human-on-the-loop**

Besides allowing the user to affect the agent as it is running, it can also be useful to allow the user to inspect the agent’s trajectory after the fact, and even go back to earlier steps and then rerun (with changes) from there. We call this human-on-the-loop, and LangGraph provides [built in support for this](https://langchain-ai.github.io/langgraph/concepts/time-travel/?ref=blog.langchain.com).

**Streaming**

Most agentic applications take a while to run, and so providing updates to the end user can be critical for providing a good user experience. LangGraph provides [built in streaming of tokens, graph steps, and arbitrary streams](https://langchain-ai.github.io/langgraph/concepts/streaming/?ref=blog.langchain.com).

**Debugging/observability**

The hard part of building reliable agents is making sure you are passing the right context to the LLM. Being able to inspect the exact steps taken by an agent, and the exact inputs/outputs at each step is crucial for building reliable agents. LangGraph integrates seamlessly with [LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com) for best in class debugging and observability. Note: [AI observability](https://www.langchain.com/articles/ai-observability?ref=blog.langchain.com) is different from traditional software observability (this deserves a separate post).

**Fault tolerance**

Fault tolerance is a key component of traditional frameworks (like Temporal) for building distributed applications. LangGraph makes fault tolerance easier with [durable workflows](https://langchain-ai.github.io/langgraph/concepts/durable_execution/?ref=blog.langchain.com) and [configurable retries](https://langchain-ai.github.io/langgraph/how-tos/node-retries/?h=retr&ref=blog.langchain.com).

**Optimization**

Rather than tweaking prompts manually by hand, it can sometimes be easier to define an evaluation dataset and then automatically optimize your agent based on this. LangGraph currently does not support this out of the box - we think it is a little early for this. But I wanted to include this because I think it is an interesting dimension to consider, and something we are constantly keeping our eyes on. `dspy` is the best framework for this currently.

💡

All of these value props (aside from the agent abstractions) provide value for both agents, workflows, and everything in between.

**So - do you really need an agentic framework?**

If your application does not require all of these features, and/or if you want to build them yourself, then you may not need one. Some of them (like short term memory) aren’t terribly complicated. Others of them (like human-on-the-loop, or LLM specific observability) are more complicated.

And regarding agent abstractions: I agree with what Anthropic says in their post:

> If you do use a framework, ensure you understand the underlying code. Incorrect assumptions about what's under the hood are a common source of customer error.

## As the models get better, will everything become agents instead of workflows?

One common argument in favor of agents (compared to workflows) is that while they don’t work now, they will work in the future, and therefore you will just need the simple, tool-calling agents.

I think multiple things can be true:

- The performance of these tool-calling agents will rise
- It will still really important to be able to control what goes into the LLM (garbage in, garbage out)
- For some applications, this tool calling loop will be enough
- For other applications, workflows will just be simpler, cheaper, faster, and better
- For most applications, the production agentic system will be a combination of workflows and agents

I don’t think OpenAI or Anthropic would debate any of these points? From Anthropic’s post:

> When building applications with LLMs, we recommend finding the simplest solution possible, and only increasing complexity when needed. This might mean not building agentic systems at all. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense.

And from OpenAI's post:

> Before committing to building an agent, validate that your use case can meet these criteria clearly. Otherwise, a deterministic solution may suffice.

Will there be applications where this simple tool calling loop will be enough? I think this will likely only be true if you are using a model trained/finetuned/RL’d on lots of data that is specific to your use case. This can happen in two ways:

- Your task is unique. You gather a lot of data and train/finetune/RL your own model.
- Your task is not unique. The large model labs are training/finetuning/RL’ing on data representative of your task.

(Side note: if I was building a vertical startup in an area where my task was not unique, I would be pretty worried about the long term viability of my startup).

**Your task is unique**

I would bet that most use cases (certainly most enterprise use cases) fall into this category. How AirBnb handles customer support is different from how Klarna handles customer support which is different from how Rakuten handles customer support. There is a ton of subtlety in these tasks. Sierra - a leading agent company in the customer support space - is not building a single customer support _agent_, but rather a customer support agent _platform_:

> The Sierra Agent SDK enables developers to use a declarative programming language to build powerful, flexible agents using composable skills to express procedural knowledge

They need to do this because each company’s customer support experience is unique enough where a generic agent is not performant enough.

One example of an agent that is a simple tool calling loop using a model trained on a specific task: [OpenAI’s Deep Research](https://www.sequoiacap.com/podcast/training-data-deep-research/?ref=blog.langchain.com). So it can be done, and it can produce amazing agents.

If you can train a SOTA model on your specific task - then yes, you probably don’t need a framework that enables arbitrary workflows, you’ll just use a simple tool calling loop. In this case, agents will be preferred over workflows.

A very open question in my mind is: how many agent companies will have the data, tools, or knowledge to train a SOTA model for their task? At this exact moment, I think only the large model labs are able to do this. But will that change? Will a small vertical startup be able to train a SOTA model for their task? I am very interested in this question. If you are currently doing this - please reach out!

**Your task is not unique**

I think some tasks are generic enough that the large model labs will be able to provide models that are good enough to do the simple tool-calling loop on these non-generic tasks.

OpenAI released their Computer Use model via the API, which is a model finetuned on generic computer use data aiming to be good enough at that generic task. (Side note: I don’t think it is close to good enough yet).

Code is an interesting example of this. Coding is relatively generic, and coding has definitely been a break out use case for agents so far. Claude code and OpenAI’s Codex CLI are two examples of coding agents that use this simple tool calling loop. I would bet heavily that the base models are trained on lots of coding data and tasks (see evidence [here](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/text-editor-tool?ref=blog.langchain.com) that Anthropic does this).

Interestingly - as the general models are trained on this data, how much does the exact shape of this data matter? Ben Hylak had an [interesting tweet](https://x.com/benhylak/status/1912922457012572364?ref=blog.langchain.com) the other day that seemed to resonate with folks:

> models don't know how to use cursor anymore.
>
> they're all being optimized for terminal. that's why 3.7 is and o3 are so awful in Cursor, and so amazing outside of it.

This could suggest two things:

- Your task has to be very very close to the task the general models are trained on. The less similar your task is, the less likely it is that the general models will be good enough for your use case.
- Training the general models on other specific tasks may decrease performance on your task. I’m sure there is just as much (if not more) data similar to Cursor’s use case used to train the new models. But if there is this influx of new data of a slightly different shape, it outweighs any other type of data. This implies it is currently hard for the general models to be really amazing at a large number of tasks.

💡

Even for applications where agents are preferred to anything workflow-like, you will still benefit features of a framework that don’t have to do with low level workflow control: short term memory storage, long term memory storage, human-in-the-loop, human-on-the-loop, streaming, fault tolerance, debugging/observability.

## What did OpenAI get wrong in their take?

If we revisit OpenAI's stance, we find it to be premised on false dichotomies that conflate different dimensions of "agentic frameworks" in order to inflate the value of their singular abstraction. Specifically, it conflates “declarative vs imperative” with “agent abstractions” as well as “workflows vs agents”.

💡

Ultimately it misses the mark on what the main challenge is for building production agentic systems and the main value that should be provided by a framework, which is: a reliable orchestration layer that gives developers explicit control over what context reaches their LLMs while seamlessly handling production concerns like persistence, fault tolerance, and human-in-the-loop interactions.

Let's break down specific parts I take issue with:

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbad01d2a13d9d604fd53d_Go0FliaXoAANDWD.jpeg

**”Declarative vs non-declarative graphs”**

LangGraph is not fully declarative - but it’s declarative enough so that’s not my main gripe. My main gripe would be that “non-declarative” is doing a lot of work and misleading. Normally when people criticize declarative frameworks they would prefer a more imperative framework. But Agents SDK is NOT an imperative framework. It’s an abstraction. A more proper title would be “Declarative vs imperative” or “Do you need an orchestration framework” or “Why agent abstractions are all you need” or “Workflows vs Agents” depending on what they want to argue (they seem to argue both below).

**”this approach can quickly become cumbersome and challenging as workflows grow more dynamic and complex”**

This doesn’t have anything to do with declarative or non-declarative. This has everything to do with workflows vs agents. You can easily express the agent logic in Agents SDK as a declarative graph, and that graph is just as dynamic and flexible as Agents SDK.

And on the point of workflows vs agents. A lot of workflows do not require this level of dynamism and complexity. Both OpenAI and Anthropic acknowledge this. You should use workflows when you can use workflows. Most agentic systems are a combination. Yes, if a workflow is really dynamic and complex then use an agent. But don’t use an agent for everything. OpenAI literally says this earlier in the paper.

**”often necessitating the learning of specialized domain-specific languages”**

Again - Agents SDK is not an imperative framework. It is an abstraction. It also has a domain specific language (it’s abstractions). I would argue that having to learn and work around Agents SDK abstractions is, at this point in time, worse than having to learn LangGraph abstractions. Largely because the hard thing about building reliable agents is making sure the agent has the right context, and Agents SDKs obfuscates that WAY more than LangGraph.

**"more flexible"**

This is just strictly not true. It’s the opposite of the truth. Everything you can do with Agents SDK you can do with LangGraph. Agents SDK only lets you do 10% of what you can do with LangGraph.

**“code-first”**

With Agents SDK you write their abstractions. With LangGraph you write a **large** amount of normal code. I don’t see how Agents SDK is more code first.

**”using familiar programming constructs”**

With Agents SDK you have to learn a whole new set of abstractions. With LangGraph you write a large amount of normal code. What is more familiar than that?

**”enabling more dynamic and adaptable agent orchestration”**

Again - this doesn’t have to with declarative vs non-declarative. This has to do with workflows vs agents. See above point.

## Comparing Agent Frameworks

We've talked about a lot of different components of agent frameworks:

- Are they flexible orchestration layer, or just an agent abstraction?
- If they are a flexible orchestration layer, are they declarative or otherwise?
- What features (aside from agent abstractions) does this framework provide?

I thought it would be fun to try to list out these dimensions in an spreadsheet. I tried to be as impartial as possible about this ( [I asked for - and got - a lot of good feedback from Twitter!](https://x.com/hwchase17/status/1913662736963412365?ref=blog.langchain.com)).

This currently contains comparisons to Agents SDK, Google's ADK, LangChain, Crew AI, LlamaIndex, Agno AI, Mastra, Pydantic AI, AutoGen, Temporal, SmolAgents, DSPy.

If I left out a framework (or got something wrong about a framework) please leave a comment!

💡

You can find a living version of the spreadsheet [here](https://docs.google.com/spreadsheets/d/1B37VxTBuGLeTSPVWtz7UMsCdtXrqV5hCjWkbHN8tfAo/edit?usp=sharing&ref=blog.langchain.com).

# Conclusion

- **The hard part of building reliable agentic systems is making sure the LLM has the appropriate context at each step. This includes both controlling the exact content that goes into the LLM, as well as running the appropriate steps to generate relevant content.**
- **Agentic systems consist of both workflows and agents (and everything in between).**
- **Most agentic frameworks are neither declarative or imperative orchestration frameworks, but rather just a set of agent abstractions.**
- **Agent abstractions can make it easy to get started, but they can often obfuscate and make it hard to make sure the LLM has the appropriate context at each step.**
- **Agentic systems of all shapes and sizes (agents or workflows) all benefit from the same set of helpful features, which can be provided by a framework, or built from scratch.**
- **LangGraph is best thought of as a orchestration framework (with both declarative and imperative APIs), with a series of agent abstractions built on top.**

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="introducing-agentkit-openai.md">
<details>
<summary>Introducing AgentKit</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://openai.com/index/introducing-agentkit>

October 6, 2025
Product

# Introducing AgentKit

New tools for building, deploying, and optimizing agents.

**_Update on June 3, 2026:_** _OpenAI is winding down the Agent Builder and Evals products. From November 30, 2026 onward, they will no longer be available on the OpenAI platform. For workflows that should continue as code, we recommend the_ [_Agents SDK_ ⁠(opens in a new window)](https://developers.openai.com/api/docs/guides/agents) _. For use cases better suited to natural language prompting, we recommend_ [_Workspace Agents in ChatGPT_ ⁠](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) _._

* * *

Today we’re launching AgentKit, a complete set of tools for developers and enterprises to build, deploy, and optimize agents. Until now, building agents meant juggling fragmented tools—complex orchestration with no versioning, custom connectors, manual eval pipelines, prompt tuning, and weeks of frontend work before launch. With AgentKit, developers can now design workflows visually and embed agentic UIs faster using new building blocks like:

- **Agent Builder:** a visual canvas for creating and versioning multi-agent workflows
- **Connector Registry:** a central place for admins to manage how data and tools connect across OpenAI products
- **ChatKit:** a toolkit for embedding customizable chat-based agent experiences in your product

We’re also expanding evaluation capabilities with new features like datasets, trace grading, automated prompt optimization, and third-party model support to measure and improve agent performance.

Since releasing the [Responses API and Agents SDK⁠](https://openai.com/index/new-tools-for-building-agents/) in March, we’ve seen developers and enterprises build end-to-end agentic workflows for deep research, customer support, and more. Klarna [built a support agent⁠](https://openai.com/index/klarna/) that handles two-thirds of all tickets and Clay [10x’ed growth⁠](https://openai.com/index/clay/) with a sales agent. AgentKit builds on the Responses API to help developers build agents more efficiently and reliably.

## Design workflows with Agent Builder

As agent workflows grow more complex, developers need clearer visibility into how they work. [Agent Builder⁠(opens in a new window)](https://platform.openai.com/docs/guides/agents/agent-builder) provides a visual canvas for composing logic with drag-and-drop nodes, connecting tools, and configuring custom guardrails. It supports preview runs, inline eval configuration, and full versioning—ideal for fast iteration.

https://images.ctfassets.net/kftzwdyauwt9/4VjOJxeZ7prpcZftRJ5MPd/582d98bb0151362f998b44d473dacae0/Visual__Agent_Builder_Template_Assets.png?w=3840&q=90&fm=webp

Builders can get started with a blank canvas or with prebuilt templates.

At Ramp, the team went from a blank canvas to a buyer agent in just a few hours:

> Agent Builder transformed what once took months of complex orchestration, custom code, and manual optimizations into just a couple of hours. The visual canvas keeps product, legal, and engineering on the same page, slashing iteration cycles by 70% and getting an agent live in two sprints rather than two quarters.”

— Ramp

Similarly, LY Corporation—a leading Japanese technology and internet services company—built a work assistant agent with Agent Builder in less than two hours.

> "Agent Builder allowed us to orchestrate agents in a whole new way, with engineers and subject matter experts collaborating all in one interface. We built our first multi-agentic workflow and ran it in less than two hours, dramatically accelerating the time to create and deploy agents."

— LY Corporation

We’re also launching a Connector Registry for enterprises to govern and maintain data across multiple workspaces and organizations. The [Connector Registry⁠(opens in a new window)](https://platform.openai.com/docs/guides/agents/connector-registry) consolidates data sources into a single admin panel across ChatGPT and the API. The registry includes all pre-built connectors like Dropbox, Google Drive, Sharepoint, and Microsoft Teams, as well as third-party MCPs.

Developers can also enable [Guardrails⁠(opens in a new window)](https://openai.github.io/openai-guardrails-python/) in Agent Builder—an open-source, modular safety layer that helps protect agents against unintended or malicious behavior. Guardrails can mask or flag PII, detect jailbreaks, and apply other safeguards, making it easier to build and deploy reliable, safe agents. Guardrails can be deployed standalone or via the guardrails library for [Python⁠(opens in a new window)](https://openai.github.io/openai-guardrails-python/) and [JavaScript⁠(opens in a new window)](https://openai.github.io/openai-guardrails-js/).

## Embed agentic chat experiences with ChatKit

Deploying chat UIs for agents can be surprisingly complex— handling streaming responses, managing threads, showing the model thinking, and designing engaging in-chat experiences. [ChatKit⁠(opens in a new window)](https://platform.openai.com/docs/guides/chatkit) makes it simple to embed chat-based agents that feel native to your product. It can be embedded into apps or websites and customized to match your theme or brand.

> "We saved over two weeks of time building a support agent for our Canva Developers community with ChatKit, and integrated it in less than an hour. This support agent will transform the way developers engage with our docs by turning it into a conversational experience, making it easy to build apps and integrations on Canva."

— Canva

ChatKit already powers a range of use cases, from internal knowledge assistants and onboarding guides to customer support and research agents. [HubSpot⁠(opens in a new window)](https://www.hubspot.com/)’s customer support agent is one example:

https://images.ctfassets.net/kftzwdyauwt9/7vwlxChvkUc64SIHHhozCr/7a23aa2fee0840430c95c090ac6c1363/Customers_UI_Ramp.png?w=3840&q=90&fm=webp

## Measure agent performance with new Evals capabilities

Building reliable, production-ready agents requires rigorous performance evaluations. Last year, we launched [Evals⁠(opens in a new window)](https://platform.openai.com/docs/guides/evals) to help developers test prompts and measure model behavior. We’re now adding four new capabilities that make it even easier to build evals:

- **Datasets**–rapidly build agent evals from scratch and expand them over time with automated graders and human annotations..
- **Trace grading**–run end-to-end assessments of agentic workflows and automate grading to pinpoint shortcomings.
- **Automated prompt optimization**–generate improved prompts based on human annotations and grader outputs.
- **Third-party model support**–evaluate models from other providers within the OpenAI Evals platform.

We’ve already seen major performance gains from customers using Evals.

> "The evaluation platform cut development time on our multi-agent due diligence framework by over 50%, and increased agent accuracy 30%."

— Carlyle

https://images.ctfassets.net/kftzwdyauwt9/3eaVkVTr4Q4xbXqVJN7UBh/5c90216e9aa153fd5a6cd8f1d2f13e5f/Eval_static-Datasets__1_.png?w=3840&q=90&fm=webp

## Push agent performance with reinforcement fine-tuning

[Reinforcement fine-tuning⁠(opens in a new window)](https://platform.openai.com/docs/guides/reinforcement-fine-tuning) (RFT) lets developers customize our reasoning models. It is generally available on OpenAI o4-mini and in private beta for GPT‑5. We are working closely with dozens of customers to refine the RFT for GPT‑5 before wider release.

Today, we’re introducing two new features in that RFT beta designed to push agent performance even further:

- **Custom tool calls**–train models to call the right tools at the right time for better reasoning
- **Custom graders**–set custom evaluation criteria for what matters most in your use case

## Pricing & availability

Starting today, ChatKit and the new Evals capabilities are generally available to all developers. Agent Builder is available in beta, and Connector Registry is beginning its beta rollout to some API, ChatGPT Enterprise and Edu customers with a [Global Admin Console⁠(opens in a new window)](https://help.openai.com/en/articles/12289294-coming-soon-global-admin-console)(where Global Owners can manage domains, SSO, multiple API orgs). The Global Admin console is a pre-requisite to enabling Connector Registry. All of these tools are included with standard API model pricing.

We plan to add a standalone Workflows API and agent deployment options to ChatGPT soon.

We can’t wait to see what you build.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="langgraph-mcp-client-setup-made-easy-2026-guide.md">
<details>
<summary>LangGraph MCP Client Setup Made Easy \[2026 Guide\]</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://generect.com/blog/langgraph-mcp>

# LangGraph MCP Client Setup Made Easy \[2026 Guide\]

[https://generect.com/blog/wp-content/uploads/2025/05/cropped-supawork-image-20250303T122922940Z.png-256x256.png
Marharyta Sevostianenko
SDR/SAAS & B2B sales](https://generect.com/blog/author/marharyta-sevostianenko/)Updated
Apr 30, 2026
Published
Jul 7, 2025

Works with startups and SaaS companies to scale outbound sales through AI-powered lead generation. At Generect, focuses on automating lead discovery, real-time data validation, and improving pipeline quality. Advises B2B teams on sales development, go-to-market strategies, and strategic partnerships. Also invests in early-stage startups in sales tech, MarTech, and AI.

So you’ve got a powerful LangGraph agent, and now you want it to do more than just chat.

You want it to call tools.

Run code.

Pull in live data.

Talk to [APIs](https://generect.com/blog/sales-and-marketing-api/).

Maybe even send a Slack message or update a Google Sheet.

That’s where **MCP ( [Model Context Protocol](https://generect.com/blog/what-is-mcp/))** comes in.

This guide walks you through, step by step, how to connect LangGraph agents to real tools using **MCP clients and servers**. You’ll learn how to:

- Build your own MCP server (in minutes)
- Expose tools like math functions, file search, or calendar events
- Connect to hosted services like Gmail, GitHub, or Trello (via Composio)
- Combine local and remote tools, all in one agent
- Test, debug, and scale your setup with confidence

Whether you’re building a personal assistant, a dev bot, or an [**enterprise lead generation**](https://generect.com/enterprise-lead-generation) AI, this setup makes your LangGraph agent not just smarter, but practical.

Let’s get you running in no time 👇

## What is MCP, and why use it with LangGraph?

Let’s start with a simple idea.

Imagine if every tool (like a calculator, a file searcher, or even GitHub) came with its own weird-shaped plug. You’d have to write different code for each one just to get your AI agent to talk to it.

Now imagine there’s one universal plug. One clean way to connect all those tools to your agent…like USB-C, but for AI.

That’s **MCP**.

So… what _is_ MCP?

MCP is a new open standard from Anthropic (released in late 2024) that makes it easy for [AI agents](https://generect.com/blog/n8n-mcp/) (like those built with LangGraph) to interact with external tools and data services. Think calculators, APIs, cloud functions, file systems… whatever you need your agent to use.

Instead of wiring every tool directly into your codebase, you expose each one through a little server = an **MCP server**. Your LangGraph agent then connects to it using an **MCP client**.

It’s like giving your agent a toolbox and the tools know how to talk back.

No more hardcoding integrations or gluing together random APIs. MCP makes it clean, modular, and future-proof.

Why use MCP with LangGraph? Easy!

Using LangGraph with MCP _supercharges_ your agent. Here’s how:

### 1\. Easy tool integration

Want your LangGraph agent to fetch weather data, query a database, or read from a PDF? With MCP, you don’t need to write new logic for each task.

Just:

- Wrap your tool in an MCP server.
- Use the langchain-mcp-adapters package in LangGraph.
- Your agent will _discover and call_ those tools on its own.

No fuss. No glue code. Just plug and go.

### 2\. Modular, scalable setup

Each tool lives in its own little service = a microservice.

You might run:

- A FileLookup MCP server for accessing files.
- A WeatherFetcher for real-time weather.
- A CodeReview service that hooks into GitHub.

Your LangGraph client simply calls them when needed (easiest LangGraph MCP integration). You’re not cramming everything into one agent. You’re building a flexible, scalable architecture for [**b2b lead generation**](https://generect.com/b2b-lead-generation).

Want to swap out a tool? Restart one without breaking the others? Easy.

### 3\. Structured, secure communication

MCP speaks **JSON-RPC 2.0**. It’s a clean and well-known protocol: structured, predictable, and designed for request/response flows.

And you can use whatever transport fits your use case:

- HTTP (for web-based services)
- Server-Sent Events (SSE) for streaming
- stdin/stdout for CLI-style tools

It’s standardized but flexible. That means you get security and stability out of the box.

### 4\. Stateful, context-aware agents

Here’s where it gets even cooler.

LangGraph agents using MCP keep track of _context_ automatically. You can call multiple tools in a row, and the agent remembers what happened last. No need to re-explain the conversation.

It’s like giving your agent memory, but without any extra work.

Let’s say you’re building a document assistant. It needs to:

- Search for files on disk
- Summarize content
- Query a custom database

With MCP, you’d:

1. Wrap each tool as an MCP server (think about it as LangGraph MCP server integration).
2. Point your LangGraph agent (with the MCP client) at those services.
3. Let the agent decide what to use, and when.

Your code stays clean. Your agent gets smarter. Your life gets easier.

Got the big picture? Great. Now let’s make sure you’ve got the right tools and setup to get started.

## What prerequisites do you need to build an MCP in LangGraph?

Before we jump into setting up the LangGraph MCP Client, let’s make sure you’ve got the basics covered.

No “heavy lifting.” Just a few tools and packages to get you rolling smoothly.

Here is a sneak peek:

| **Item** | **Required?** | **How to get it** | **Why you need it** |
| --- | --- | --- | --- |
| Python 3.11+ | ✅ Yes | [python.org](https://www.python.org/downloads/) | MCP adapters require 3.11+ for type safety |
| pip | ✅ Yes | Comes with Python (or install via get-pip.py) | Installs Python packages |
| Virtual environment | ✅ Recommended | python -m venv .venv && source .venv/bin/activate | Keeps dependencies clean and isolated |
| Langchain + LangGraph | ✅ Yes | pip install langchain langgraph | Core framework for the agent |
| MCP adapter | ✅ Yes | pip install langchain-mcp-adapters | Connects agent to [MCP tools](https://generect.com/blog/mcp-tools/) |
| Optional: openai | 🔲 Optional | pip install openai | Only if using OpenAI models |

Let’s talk details:

### 1\. Get your environment ready

You’ll be working with Python, so make sure your machine is set up right. Here’s what you need:

- **Python 3.11 or newer =** MCP adapters won’t work on older versions. To check, run: python –version
- **Pip =** This usually comes with Python. If not, [install pip](https://pip.pypa.io/en/stable/installation/).
- **(Recommended but optional) Virtual уnvironment =** Keeps things clean and isolated, especially helpful if you’re juggling multiple projects. Set it up like this:

python -m venv .venv

source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate

Why use a virtual environment? You won’t accidentally mess with system-wide packages, and it’s easier to manage dependencies.

### 2\. Install the core packages

Next, let’s install the tools that connect LangGraph with MCP servers.

Run this in your terminal: pip install langchain-mcp-adapters langgraph langchain

These libraries do the heavy lifting. They let LangGraph agents discover and call tools via MCP with almost zero setup.

If you’re planning to use OpenAI or another LLM provider, go ahead and install the client now. For example: pip install openai

You can plug in other providers too. Just make sure your agent knows how to talk to them.

### 3\. Make sure you’ve got an MCP Server

LangGraph needs to connect to at least one MCP-compatible server. That’s where your tools actually _live_. You’ve got two solid options here:

#### Option 1: Run a local MCP Server

Perfect for testing or building your own tools.

A great starting point is FastMCP, a Python-based server. You can spin it up like this:

1. Install FastMCP (if not already): pip install fastmcp
2. Create a tool server, e.g., math\_server.py. Inside, you might define a simple math function your agent can call.
3. 3\. Run the server: python math\_server.py

Now it’s live and listening for your agent to call it.

#### Option 2: Use a hosted MCP Server

Maybe someone else is hosting the tools for you or you’re using a cloud-based setup.

In that case:

- Get the server’s URL.
- Note any headers or API keys it requires.
- Make sure it’s up and reachable from your machine.

LangGraph can connect to either option. Just tell it where to look.

Once your environment is ready, it’s time to build your first MCP server. Let’s create a simple tool your agent can actually use.

## How can you build a basic MCP server?

So, you’re ready to create your own tool service? Great! With **FastMCP**, it’s surprisingly simple; you’ll have a working server in just a few lines of code.

Before we dive into specifics, let’s quickly break down what each part of a basic MCP server does. This table shows you exactly how to write, register, and run a tool…without the guesswork.

| **Step** | **What you do** | **Why it matters** |
| --- | --- | --- |
| @mcp.tool() | Decorate a function | Marks it as a callable tool for the client |
| Type hints | Add types like a: int and -> int | Enables automatic schema generation |
| Docstring | Write a 1-line description | Helps agents understand tool behavior |
| FastMCP(“Name”) | Create a named server | Registers your toolset under that name |
| mcp.run() | Start the server | Opens the tool to clients (via stdio or HTTP) |

Let’s walk through how to build a basic LangGraph MCP server step by step. You’ll define your tools, set up the server, and make it callable by any LangGraph agent.

### Step 1: Install and set up FastMCP

First, you’ll need to install **FastMCP** = the easiest way to spin up an MCP-compatible server.

In your terminal, run: pip install fastmcp

Now, open a new Python file (let’s call it server.py) and add the following:

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(“DemoServer”)

This creates a new server named “DemoServer” that’s ready to register tools and listen for incoming calls. FastMCP takes care of all the background plumbing (no boilerplate needed!).

### Step 2: Define your tools

Your tools are just regular Python functions. To expose them to your agent, use the @mcp.tool() decorator.

Each tool should:

- Have type hints (so MCP can generate the interface)
- Include a simple docstring (so humans + agents know what it does)

Here’s a quick example:

@mcp.tool()

def add(a: int, b: int) -> int:

    “””Add two numbers.”””

    return a + b

@mcp.tool()

def shout(s: str) -> str:

    “””Convert a string to uppercase.”””

    return s.upper()

That’s it. Just decorate and define. FastMCP will handle schema generation, validation, and everything in between.

You can create tools for anything: file handling, database queries, web scraping…you name it.

### Step 3: Choose your transport

Next, decide **how** your server should talk to clients (like LangGraph):

- **stdio** (default) → great for local development or CLI use.
- **http** / **streamable-http** → best for running in the cloud or on a network.
- **sse** → was used before, but http is now the better choice.

You don’t need to write separate code for each transport; just pass a flag when starting the server.

### Step 4: Launch your server

Ready to go live? Just wrap it all up with a call to .run():

if \_\_name\_\_ == “\_\_main\_\_”:

    # Default: stdio

    mcp.run()

    # Or run over HTTP:

    # mcp.run(transport=”http”, host=”0.0.0.0″, port=8000)

Then launch your server from the terminal: python server.py

Or, if you prefer using the CLI: fastmcp run server.py –transport http –port 8000

FastMCP takes care of everything else: starting the listener, exposing the tools, and speaking the MCP protocol.

Aaaaand…you’ve got a live MCP Server!

By now, your server:

- Has a name (DemoServer)
- Offers tools (add(), shout(), or any you define)
- Runs with a clean transport setup

LangGraph can now discover and call those tools, just like it would any other service.

Now that you’ve built a tool, your LangGraph server needs to expose it. Let’s turn on the MCP endpoint so everything can talk.

## How do you enable the MCP endpoint on the LangGraph server?

You’re almost there = your tools are ready, your server’s built.

Now it’s time to let your LangGraph agents speak MCP. The good news? LangGraph makes this part super simple. No extra plugins. No config overload.

Let’s walk through how to activate the MCP endpoint on your LangGraph server.

### Step 1: Upgrade your LangGraph packages

To use MCP, your LangGraph installation needs to be on the right versions. These versions include built-in LangGraph MCP support.

In your terminal, run: pip install “langgraph-api>=0.2.3” “langgraph-sdk>=0.1.61”

This ensures your server will expose the MCP interface when it runs. If you’ve used LangGraph before, this upgrade is key. Older versions don’t support MCP tools.

### Step 2: Start (or redeploy) your server

Now that everything’s up to date, just start your LangGraph server like you normally would: langgraph-api start

Or use whatever deployment method you prefer: Docker, CLI, or your cloud setup. There’s nothing extra to configure. The MCP endpoint is enabled automatically in the background.

No flags. No feature toggles.

It just works.

### Step 3: Access the MCP endpoint

Once the server’s running, your agent is available via this URL: http://<your-server-host>/mcp

This is the official MCP endpoint. It uses **streamable HTTP transport**, which means MCP clients (like those built with langchain-mcp-adapters) can connect to it right away.

You can open that URL in a browser or curl it to see that it’s alive.

What happens behind the scenes? As soon as your server spins up:

- LangGraph **registers all deployed agents** as MCP-compatible tools.
- Those agents are exposed via the /mcp endpoint.
- MCP clients can **discover and interact** with them instantly.

You don’t need to write schemas or define routes manually. LangGraph handles that part.

All your client needs is the /mcp URL. From there, it can list your agents, send requests, and receive structured responses = just like it would with any other MCP tool.

Your server’s ready! Now it’s time to connect the client. Let’s plug everything in and make your agent MCP-aware.

## How can you connect your clients to the MCP Server?

Now that your MCP servers and LangGraph agents are ready, it’s time to bring everything together. This is where the **MCP client** comes in. It connects your app (or agent) to the tools running on those servers, so your agent can use them like magic.

Let’s go through how to write a client in both **Python** and **JavaScript/TypeScript**.

### How do you write a client in Python?

You’re just a few lines away from having a LangGraph agent that can talk to MCP tools. Here’s the flow:

https://lh7-rt.googleusercontent.com/docsz/AD_4nXfaldkpWo29hKVoF_M7dZjrvjmODMPLDnt7jPMIj-q87SAmDa3Ant965JZlm61OWTno1f0UhB-xd79n3pAHniyusAGB1cV18jJlt4qrTWJGhAQgJMw0vhYUzX4c_Vwbn3KbefEERQ?key=HWm2Uf7Y276CZtzB17o9eg

Here’s how to make it happen.

#### 1\. Import the MCP Client

First, bring in the client class that handles multiple servers: from langchain\_mcp\_adapters.client import MultiServerMCPClient

This client makes it easy to talk to local or remote MCP servers, using different transports like stdio and http.

#### 2\. Configure the servers you want to connect to

You can use:

- A **local tool** running via script (stdio)
- A **hosted tool** with a live HTTP endpoint

Here’s how to set them up in one go:

client = MultiServerMCPClient({

“math”: {

    “command”: “python”,

    “args”: \[“/path/to/math\_server.py”\],

    “transport”: “stdio”,

},

“weather”: {

    “url”: “http://localhost:8000/mcp”,

    “transport”: “streamable\_http”,

}

})

This config tells your client how to connect to each server. You can mix and match local and hosted tools.

#### 3\. Load the available tools

Now pull in the tools from those servers. They’ll be automatically wrapped for LangGraph: tools = await client.get\_tools()

Behind the scenes, this fetches tool schemas, validates inputs, and sets everything up for your agent to use (no extra work needed).

#### 4\. Build a LangGraph agent

With your tools ready, wire them into a React-style LangGraph agent:

from langgraph.prebuilt import create\_react\_agent

agent = create\_react\_agent(“anthropic:claude-3-7-sonnet-latest”, tools)

This kind of agent can decide which tool to use, when to use it, and how to call it, all based on the user’s input.

Want to see what happens when your agent runs? Here’s the basic flow:

https://lh7-rt.googleusercontent.com/docsz/AD_4nXfU5Bm5DIaV-MaXl85U_4hyUzfOis7qkx_7jmmT7-8zL9frw1FZUoNmAHPC9UYGW59Q16zHERiUB6GzFQKPxb0X-VwlZdrEPHiQAd67diKMHP06nbJqvNno5hWCxo4M05RY3m4c?key=HWm2Uf7Y276CZtzB17o9eg

#### 5\. Ask questions, get answers

Let’s test it out. You can now query your agent and it’ll decide whether to use a tool:

math\_resp = await agent.ainvoke({

“messages”: \[{“role”: “user”, “content”: “what’s (3 + 5) x 12?”}\]

})

weather\_resp = await agent.ainvoke({

“messages”: \[{“role”: “user”, “content”: “what is the weather in nyc?”}\]

})

That’s it. Your agent figures out the intent, picks the right tool, and gets the result = all on its own.

What you’ve built:

- A client connected to one or more MCP servers
- Tools dynamically discovered and wrapped
- A LangGraph agent that uses those tools in real conversations

You’ve just unlocked real-world utility in your AI agent. Let’s see how to do the same in JavaScript!

### How do you write a client in JavaScript/TypeScript?

Working in a JS or TS project? You can do all the same things, right from your Node.js environment.

Here’s how to set up the MCP client and run a LangGraph-compatible agent.

#### 1\. Install the SDK and Adapters

First, add the required packages: npm install @modelcontextprotocol/sdk @langchain/mcp-adapters

This gives you everything you need: the MCP client, adapters, and transport support.

#### 2\. Connect to your MCP Server

Use the SDK to create a client and attach it to an HTTP endpoint:

import { Client } from “@modelcontextprotocol/sdk/client/index.js”;

import { StreamableHTTPClientTransport } from “@modelcontextprotocol/sdk/client/streamableHttp.js”;

async function connectClient(url: string) {

const client = new Client({ name: “js-mcp-client”, version: “1.0.0” });

const transport = new StreamableHTTPClientTransport(new URL(url));

await client.connect(transport);

return client;

}

const client = await connectClient(“http://localhost:2024/mcp”);

console.log(“Tools:”, await client.listTools());

.listTools() will return everything your server offers: math tools, file tools, whatever’s live.

#### 3\. Load tools into a React agent

Now wire your tools into a LangGraph or LangChain agent:

import { loadMcpTools } from “@langchain/mcp-adapters”;

import { createReactAgent } from “@langchain/langgraph/prebuilt”;

import { ChatOpenAI } from “@langchain/openai”;

const tools = await loadMcpTools(“mcp-server”, client);

const agent = createReactAgent({

llm: new ChatOpenAI({ model: “gpt-4o-mini” }),

tools,

});

Once you do this, your JS agent can reason about which tool to use, just like in Python.

#### 4\. Run the agent and get answers

Try asking it something in code:

const res = await agent.invoke({

input: “What is the result of 7 + 13?”,

});

console.log(res.output);

Want to go interactive? You can run a CLI loop too:

const input = await prompt(“Ask me anything: “);

const response = await agent.invoke({ input });

console.log(response.output);

Simple as that.

Want to do more than just local tools? Let’s see how to add hosted and third-party MCP servers…no extra code needed. Yet, a tiny pause along the way…

## How can you integrate custom or hosted servers?

At this point, you’ve built your own LangGraph MCP server and connected a LangGraph client to it. Awesome. Now, let’s take it up a notch by plugging in **hosted** or **third-party MCP servers**.

No matter if it’s your own API or a fully managed tool suite like **Composio**, you can integrate everything into a single MCP client config.

Here’s a quick comparison of self-hosted vs managed MCP servers to help you decide what to use in production.

| **Aspect** | **Self-hosted MCP** | **Managed MCP (e.g. Composio)** |
| --- | --- | --- |
| Setup time | Fast (local), Medium (remote deployment) | Instant, just register and plug in |
| Maintenance | You maintain availability, auth, scaling | Fully managed by provider |
| Tool control | Full control over logic, structure | Prebuilt tools with fixed schemas |
| Authentication | Up to you = can be basic or advanced | Built-in OAuth, API keys, etc. |
| Ideal use case | Custom/internal tools | SaaS automation (Slack, Gmail, GitHub, etc.) |

Let’s walk through how.

### Option 1: Use Composio-managed MCP Servers

If you don’t want to host or maintain servers yourself, **Composio** makes it easy. They offer plug-and-play access to over **250 tools**, including Gmail, Slack, Trello, GitHub, Notion, databases…you name it.

Here’s how to add it to your MCP client:

1. **Sign up** at [composio.dev](https://composio.dev/)
2. **Grab your MCP endpoint URL** = they’ll give you a streamable HTTP or SSE link
3. **Add it to your client config**

Example setup:

mcpServers: {

composio: {

    url: “https://mcp.composio.dev/your-instance/sse”,

    transport: “streamable\_http”,

    auth: {

      apiKey: COMPOSIO\_API\_KEY,

    },

}

}

Composio handles the hard stuff: auth, schema generation, scaling, and tool maintenance. You just connect and use.

### Option 2: Connect your own hosted MCP Servers

Already built your own server and deployed it somewhere? Great! You can connect it just like you did with Composio.

Just add another entry to your config:

mcpServers: {

myTools: {

    url: “https://myhost.com/mcp”,

    transport: “streamable\_http”,

}

}

No need to change your code or redeploy the client. LangGraph’s MCP client handles it automatically.

Here’s the best part: you don’t have to choose between local, hosted, or managed servers. You can **use all of them at once**.

Example combined config:

mcpServers: {

localMath: {

    command: “python”,

    args: \[“./math\_server.py”\],

    transport: “stdio”,

},

composio: {

    url: “https://mcp.composio.dev/your-instance/sse”,

    transport: “streamable\_http”,

    auth: { apiKey: COMPOSIO\_API\_KEY },

},

myHostedTools: {

    url: “https://myhost.com/mcp”,

    transport: “streamable\_http”,

}

}

LangGraph’s agent will discover tools from **all** these servers and pick the right one based on user input.

By adding hosted and managed MCP servers, your agent now gets:

- **Instant access to real-world tools** like Gmail, GitHub, Slack, Notion, etc.
- **Secure authentication** through API keys, OAuth, or custom headers
- **Seamless integration** of your custom or local tools alongside third-party ones

Now that you’ve got a mix of tools, it’s time to combine them. Let’s make sure your agent can use both local and remote tools together.

## How do you combine multiple transports or servers?

You’ve built your tools. You’ve connected your client. Now comes the fun part = **mixing transports** so your agent can talk to _both local and hosted tools_ at the same time.

No matter if you’ve got a math tool running locally or a Slack integration hosted on the cloud, LangGraph’s MCP client can handle it all in one unified setup.

Let’s see how to do it in Python and JavaScript.

Why combine transports? Simple: because your tools live in different places.

- You might want **local tools** (like math operations or file access) for quick responses and testing.
- And you might also need **hosted services** (like Gmail, Trello, or weather APIs) that live on the internet and require authentication.

By combining transports (stdio, http, and sse) you let your agent choose from _all_ available tools, no matter where they’re running.

Let’s make it visual. Here’s what a real-world MCP setup looks like:

https://lh7-rt.googleusercontent.com/docsz/AD_4nXdId001UG63ZS3iUzIDuaYzXM7zQpi_8rBgnd-fBi7sz8Hju1cr5ybAktj_7zkEVclep53TFyX7btJQlaehWRMlaLEYYdOwqqo9Y3fVIjH486vcU5LZPkcRE7c735qTKImTIS0?key=HWm2Uf7Y276CZtzB17o9eg

Let’s wire it up.

### Python: Mix Stdio and HTTP in one client

In Python, it’s as simple as passing a config dictionary to MultiServerMCPClient.

from langchain\_mcp\_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient({

    “math”: {

        “command”: “python”,

        “args”: \[“./math\_server.py”\],

        “transport”: “stdio”,

    },

    “composio-tools”: {

        “url”: “https://mcp.composio.dev/…/server?transport=sse”,

        “transport”: “streamable\_http”,

        “headers”: {

            “Authorization”: “Bearer YOUR\_KEY”

        },

    }

})

tools = await client.get\_tools()

In this example:

- The math tool runs locally through **stdio**.
- The composio-tools endpoint connects to hosted services like **Slack, Gmail, or GitHub** via **streamable HTTP (SSE)**.

You don’t need to manage any connections manually = the client handles it for you. Tools from both sources show up in one neat list, ready for your agent to use.

### JavaScript/TypeScript: Same idea, different syntax

If you’re working in Node or a front-end app, the JS client offers the same flexibility, with just slightly different setup.

Here’s how to mix local and hosted transports:

import { MultiServerMCPClient } from “@langchain/mcp-adapters”;

const client = new MultiServerMCPClient();

// Connect to a local tool (stdio)

await client.connectToServerViaStdio(

“math”,

“python”,

\[“./math\_server.py”\]

);

// Connect to a hosted tool (Composio via SSE)

await client.connectToServerViaSSE(

“composio”,

“https://mcp.composio.dev/…/server?transport=sse”,

{ Authorization: “Bearer YOUR\_KEY” },

true

);

// Load tools

const tools = await client.getTools();

That’s it. You’re now combining:

- A **local math server** running on your machine
- A **hosted Composio endpoint** with 250+ ready-to-use services

All tools are merged under the hood and made available to your LangGraph or LangChain agent automatically.

With everything connected, let’s explore how this works in practice. You’ll see how real agents use MCP tools in everyday tasks.

## What are some real‑world use cases?

Now that your LangGraph agent is connected to MCP tools, let’s see what it can actually _do_.

This cheat sheet gives you inspiration to build your next MCP tool:

| **Use case** | **LangGraph MCP example** | **Tool type** | **Transport** |
| --- | --- | --- | --- |
| Do quick math | add(a: int, b: int) | Local Python tool | stdio |
| Convert currency | convert\_currency(from: str, to: str, amount: float) | External API wrapper | http or sse |
| Check the weather | get\_weather(city: str) | Hosted API tool | streamable\_http |
| Get current time in a timezone | get\_time(timezone: str) | Local utility | stdio |
| Generate a strong password | generate\_password(length: int) | Utility/microservice | stdio |
| Summarize an email thread | summarize\_email(thread\_id: str) | Gmail (via Composio) | streamable\_http |
| Send a calendar invite | create\_calendar\_event(title, time, invitees) | Google Calendar (Composio) | streamable\_http |
| Create a GitHub issue | create\_github\_issue(repo, title, body) | GitHub (Composio) | streamable\_http |
| Get a GitHub repo’s stars | get\_stars(repo: str) | GitHub API | http |
| Post a Slack message | send\_slack\_message(channel, text) | Slack (Composio) | streamable\_http |
| Create a Trello card | create\_task(title: str) | Trello (Composio) | streamable\_http |
| Search a local folder | search\_files(query: str) | Local Python tool | stdio |
| Read text from PDF | extract\_pdf\_text(file\_path: str) | Local file utility | stdio |
| Store and retrieve user notes | save\_note(title, content) / get\_notes() | Custom note service | http or stdio |
| Translate text | translate(text: str, to\_lang: str) | Hosted API (e.g. DeepL) | streamable\_http |
| Trim and clean up text | clean\_text(input: str) | String utility | stdio |
| Count words or characters | count\_words(text: str) | Local tool | stdio |
| Convert to uppercase/lowercase | to\_uppercase(s: str) / to\_lowercase(s: str) | String utility | stdio |
| Generate blog outline | generate\_outline(topic: str) | LLM-powered tool | http (with OpenAI) |
| Answer FAQ from docs | search\_docs(query: str) | RAG / document retriever | http or stdio |
| Add product to cart | add\_item(name: str, quantity: int) | E-commerce logic | stdio |
| Show current cart | get\_cart() | E-commerce logic | stdio or http |
| Remove item from cart | remove\_item(name: str) | E-commerce logic | stdio |
| Get stock market data | get\_stock\_price(ticker: str) | Finance API wrapper | http or streamable\_http |
| Send email reply | reply\_email(thread\_id, message) | Gmail (Composio) | streamable\_http |
| List upcoming meetings | get\_calendar\_events(date\_range) | Google/Outlook Calendar | streamable\_http |
| Create support ticket | create\_support\_ticket(subject, details) | Helpdesk integration | http |
| Trigger build in CI/CD pipeline | trigger\_build(project\_id: str) | DevOps integration | http |
| Fetch analytics metrics | get\_analytics(metric: str, date\_range: str) | Custom backend or SaaS | http or sse |
| Generate daily summary | daily\_summary(user\_id: str) | Aggregator microservice | http or stdio |

All of this works through LangGraph MCP, which means your agent doesn’t need direct access to APIs or auth logic = Composio handles it. You just connect the endpoint.

Before going too far, it’s smart to test your setup. Let’s check that everything works as expected, and fix anything that doesn’t.

## How do you test and debug it?

You’ve connected your MCP servers and built a client. Nice work! Now it’s time to make sure everything actually works.

Testing and debugging your LangGraph + MCP setup doesn’t have to be painful. Just follow a few simple steps to catch problems early and keep your tools running smoothly.

### Start by checking get\_tools()

Before you run any agents or workflows, make sure your client can _see_ your tools.

In Python:

tools = await client.get\_tools()

print(tools)

You should see a list of available tools, each with:

- The correct name
- Inputs and types (e.g. a: int, b: int)
- Return type (e.g. int, str, etc.)

If a tool doesn’t appear or its schema looks wrong, double-check your server code. Start simple. This call confirms the basic connection is working.

### Test tool calls one at a time

Don’t jump into full agent flows just yet. First, call your tools manually to make sure they behave as expected.

Example:

result = await client.call\_tool(“add”, {“a”: 3, “b”: 4})

print(result)  # Should return 7

This helps you catch:

- Type errors (e.g. passing a string instead of a number)
- Schema mismatches
- Unexpected tool logic

Get these right now, and you’ll save time later when agents start using the tools automatically.

### Check logs on both sides

Debugging gets easier when you can _see_ what’s going on.

Here’s where to look:

**On the server side:**

- Watch for startup messages
- See incoming requests
- Track tool errors and exceptions

**On the client side:**

- Enable debug logs to trace activity

In your terminal, set this environment variable: DEBUG=’@langchain/mcp-adapters:\*’

This shows:

- Tool discovery
- Transport connections (HTTP, stdio, SSE)
- Reconnects and failures

It’s especially useful when tools aren’t showing up or when calls silently fail.

### Watch for transport errors

Sometimes the issue isn’t with your tool. It’s how the client connects to it.

Here’s what to watch for:

#### For hosted (HTTP/SSE) tools:

- Network timeouts
- Connection drops
- Wrong URLs or missing headers

#### For local (stdio) tools:

- Bad file paths
- Crashed servers
- Incorrect command arguments

You’ll usually see a stack trace or error message in the logs. Restart the server or fix the path. It’s usually (and surprisingly!) a quick fix once you spot it.

### Keep types in sync

LangGraph MCP tools rely on strict schemas. If your tool expects an int but you pass a str, it’ll throw a **Zod validation error**.

Here’s how to avoid that:

- Double-check your tool’s **type hints** and **docstrings**
- Confirm the inputs in your test calls match the expected types
- Watch for error messages like “invalid\_string” or “expected\_number” in logs

Tip: if your tool says def add(a: int, b: int) -> int, then { “a”: 3, “b”: 4 } is valid, but { “a”: “three” } will fail every time.

Once it works, let’s make it _great_. Here are some best practices to keep your setup clean, secure, and easy to maintain.

## What are best practices?

You’ve built something powerful with LangGraph and MCP. Now it’s time to _polish_ it, so your setup is easier to maintain, more secure, and ready for real-world use.

Here are a few simple habits that’ll save you time, prevent bugs, and keep your system solid as it grows.

### Keep your tools modular and separate

Start by splitting your tools based on what they do.

- Put math tools in one server
- Keep email tools in another
- Maybe even separate by team or product area

**Why?** It keeps things clean. If you need to update or restart a tool, you don’t risk breaking unrelated ones.

Also, separate your **server logic** and **client code**. Store them in different folders or even different repos if the project’s big enough.

This setup:

- Makes deployments safer
- Keeps dev environments isolated
- Helps you debug faster when things go wrong

### Use clear docstrings and type hints

Every MCP tool should explain itself. Don’t leave the meaning of inputs and outputs to guesswork.

Example:

@mcp.tool()

def add(a: int, b: int) -> int:

    “””Add two integers and return the result.”””

    return a + b

That short docstring and type hint does two big things:

- Helps **you** (and others) understand the tool quickly
- Enables **automatic schema generation**, which powers tool discovery

You don’t need to write essays. Just a clear sentence and proper types.

### Handle errors early and gracefully

Tool crashes are frustrating, yet preventable.

Here’s how to keep things smooth:

- Use try/except blocks inside your tools
- Validate inputs before using them
- Catch obvious issues (like None, wrong types, empty fields) early

If your tools make **network calls** (like hitting a 3rd-party API), add **retry logic with backoff**. That way, a temporary blip won’t break the whole flow.

Bonus: If you’re using managed servers like Composio, their runtime layer already supports error handling and retries out of the box.

### Secure your transports and access

Security matters, especially with tools that access emails, files, or user data.

A few rules of thumb:

- Always use **HTTPS** or **SSE** for hosted MCP servers
- Include **auth headers or tokens** in your client config
- Limit access: set **per-route or per-tool permissions** where possible
- Follow **REST best practices**: return proper status codes, handle errors clearly

For example, don’t let a public endpoint call a tool that sends emails or modifies databases. Lock that stuff down.

You’ve got a working system…now what? Let’s talk about where to go next, how to scale, and what to improve over time.

## What’s next after setup?

You’ve built the foundation = your LangGraph MCP servers are live, your LangGraph client is connected, and your agent can call real tools. That’s a big win.

Now it’s time to go further: test, scale, and evolve. Here’s how to move from basic setup to a reliable, production-ready agent that delivers real value.

Start small. Make sure everything works before you go big.

Try basic prompts like:

- “What’s 5 + 7 × 3?”
- “What’s the weather in Tokyo right now?”

Check:

- **Is the output correct?**
- **How fast is the response?**

These small tests help you validate that tools are wired properly. You’ll get a sense of latency, response quality, and how well your agent selects tools.

Once that’s solid, you’ve got a baseline to build on.

Now bring in the good stuff.

Plug in tools your agent can use in actual workflows. For example:

- **Slack**: Post alerts, check channel history
- **Databases**: Query records, update tables
- **Email (Gmail/Outlook)**: Summarize threads, send replies

You can connect these through **Composio** or your own MCP servers. Either way, your agent now moves from toy examples to _real utility_.

This is when it gets exciting = watch your AI take real-world actions through natural language.

As you scale, observability becomes essential. You need visibility into how your agent and tools are behaving.

Set up tracking for:

- API usage (how often tools are called)
- Latency (how long each call takes)
- Errors (timeouts, schema mismatches, etc.)

You can use platforms like [Moesif](https://www.moesif.com/) to monitor these metrics with dashboards and alerts.

This helps you catch problems early, especially silent failures that might otherwise go unnoticed.

As users start interacting with your agent, you’ll notice opportunities to improve. Don’t be afraid to tweak and expand.

Here’s how to keep growing:

- **Refine tool schemas** based on real usage
- **Add retries, pagination, or batching** where needed
- **Introduce memory or multi-turn context** for more dynamic responses
- **Try multi-agent flows or plug in RAG (retrieval-augmented generation)** for deeper answers

Keep iterating. Each cycle (think “build → test → refine”) gets you closer to a smarter, more helpful agent.

You can also explore other MCP-compatible ecosystems like **Generect** to boost your [**startup lead generation**](https://generect.com/startup-lead-generation) with real-time data and outreach tools. These integrations open up even more possibilities.

Ready to build something bigger?

You’ve got all the pieces: modular tools, a flexible agent, and a scalable setup. Whether you’re building a smart assistant, an internal chatbot, or a full AI workflow = your system is ready.

Take your time. Try new tools. Like [Generect MCP](https://liveapi.generect.com/). See what works.

And when you’re ready to scale, your setup will grow right along with you

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="top-10-most-starred-ai-agent-frameworks-on-github-2026-by-al.md">
<details>
<summary>Top 10 Most Starred AI Agent Frameworks on GitHub (2026)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b>

# Top 10 Most Starred AI Agent Frameworks on GitHub (2026)

This article was originally published at [Agentailor blog](https://blog.agentailor.com/posts/top-ai-agent-frameworks-github-2026).

AI agents are reshaping how we build software. GitHub stars are a strong indicator of developer trust and community adoption. Here are the top 10 most starred AI agent frameworks heading into 2026.

## 1\. LangChain ⭐ 122,850

[langchain-ai/langchain](https://github.com/langchain-ai/langchain) \| Python \| MIT

The most popular framework for building LLM-powered applications, with extensive tooling for chains, agents, and retrieval.

## 2\. MetaGPT ⭐ 61,919

[FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) \| Python \| MIT

A multi-agent framework that simulates a software company, with agents taking on roles like product manager, architect, and engineer.

## 3\. AutoGen ⭐ 52,927

[microsoft/autogen](https://github.com/microsoft/autogen) \| Python \| CC-BY-4.0

Microsoft’s framework for building multi-agent conversational systems with customizable agent behaviors.

## 4\. LlamaIndex ⭐ 46,100

[run-llama/llama\_index](https://github.com/run-llama/llama_index) \| Python \| MIT

The leading framework for connecting LLMs to your data, with powerful indexing and retrieval capabilities.

## 5\. CrewAI ⭐ 41,871

[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) \| Python \| MIT

Framework for orchestrating role-playing autonomous agents that collaborate to accomplish complex tasks.

## 6\. Agno ⭐ 36,414

[agno-agi/agno](https://github.com/agno-agi/agno) \| Python \| Apache-2.0

A multi-agent framework with a runtime and control plane for managing agent deployments at scale.

## 7\. Haystack ⭐ 23,741

[deepset-ai/haystack](https://github.com/deepset-ai/haystack) \| Python \| Apache-2.0

Production-ready AI orchestration framework focused on building customizable LLM applications and RAG pipelines.

## 8\. Vercel AI SDK ⭐ 20,400

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Build your first Flow</summary>

# Build your first Flow

**Source URL:** <https://docs.crewai.com/guides/flows/first-flow>

## Taking Control of AI Workflows with Flows

CrewAI Flows represent the next level in AI orchestration - combining the collaborative power of AI agent crews with the precision and flexibility of procedural programming. While crews excel at agent collaboration, flows give you fine-grained control over exactly how and when different components of your AI system interact.In this guide, we’ll walk through creating a powerful CrewAI Flow that generates a comprehensive learning guide on any topic. This tutorial will demonstrate how Flows provide structured, event-driven control over your AI workflows by combining regular code, direct LLM calls, and crew-based processing.

### What Makes Flows Powerful

Flows enable you to:

1.  **Combine different AI interaction patterns** - Use crews for complex collaborative tasks, direct LLM calls for simpler operations, and regular code for procedural logic
2.  **Build event-driven systems** - Define how components respond to specific events and data changes
3.  **Maintain state across components** - Share and transform data between different parts of your application
4.  **Integrate with external systems** - Seamlessly connect your AI workflow with databases, APIs, and user interfaces
5.  **Create complex execution paths** - Design conditional branches, parallel processing, and dynamic workflows

### What You’ll Build and Learn

By the end of this guide, you’ll have:

1.  **Created a sophisticated content generation system** that combines user input, AI planning, and multi-agent content creation
2.  **Orchestrated the flow of information** between different components of your system
3.  **Implemented event-driven architecture** where each step responds to the completion of previous steps
4.  **Built a foundation for more complex AI applications** that you can expand and customize

This guide creator flow demonstrates fundamental patterns that can be applied to create much more advanced applications, such as:

-   Interactive AI assistants that combine multiple specialized subsystems
-   Complex data processing pipelines with AI-enhanced transformations
-   Autonomous agents that integrate with external services and APIs
-   Multi-stage decision-making systems with human-in-the-loop processes

Let’s dive in and build your first flow!

## Prerequisites

Before starting, make sure you have:

1.  Installed CrewAI following the [installation guide](https://docs.crewai.com/en/installation)
2.  Set up your LLM API key in your environment, following the [LLM setup
    guide](https://docs.crewai.com/en/concepts/llms#setting-up-your-llm)
3.  Basic understanding of Python

## Step 1: Create a New CrewAI Flow Project

First, let’s create a new CrewAI Flow project using the CLI. This command sets up a scaffolded project with all the necessary directories and template files for your flow.

```
crewai create flow guide_creator_flow
cd guide_creator_flow
```

This will generate a project with the basic structure needed for your flow.

https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a

CrewAI Framework Overview

## Step 2: Understanding the Project Structure

The generated project has the following structure. Take a moment to familiarize yourself with it, as understanding this structure will help you create more complex flows in the future.

```
guide_creator_flow/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
├── main.py
├── crews/
│   └── poem_crew/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       └── poem_crew.py
└── tools/
    └── custom_tool.py
```

This structure provides a clear separation between different components of your flow:

-   The main flow logic in the `main.py` file
-   Specialized crews in the `crews` directory
-   Custom tools in the `tools` directory

We’ll modify this structure to create our guide creator flow, which will orchestrate the process of generating comprehensive learning guides.

## Step 3: Add a Content Writer Crew

Our flow will need a specialized crew to handle the content creation process. Let’s use the CrewAI CLI to add a content writer crew:

```
crewai flow add-crew content-crew
```

This command automatically creates the necessary directories and template files for your crew. The content writer crew will be responsible for writing and reviewing sections of our guide, working within the overall flow orchestrated by our main application.

## Step 4: Configure the Content Writer Crew

Now, let’s modify the generated files for the content writer crew. We’ll set up two specialized agents - a writer and a reviewer - that will collaborate to create high-quality content for our guide.

1.  First, update the agents configuration file to define our content creation team:Remember to set `llm` to the provider you are using.

    ```
    # src/guide_creator_flow/crews/content_crew/config/agents.yaml
    content_writer:
      role: >
        Educational Content Writer
      goal: >
        Create engaging, informative content that thoroughly explains the assigned topic
        and provides valuable insights to the reader
      backstory: >
        You are a talented educational writer with expertise in creating clear, engaging
        content. You have a gift for explaining complex concepts in accessible language
        and organizing information in a way that helps readers build their understanding.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...

    content_reviewer:
      role: >
        Educational Content Reviewer and Editor
      goal: >
        Ensure content is accurate, comprehensive, well-structured, and maintains
        consistency with previously written sections
      backstory: >
        You are a meticulous editor with years of experience reviewing educational
        content. You have an eye for detail, clarity, and coherence. You excel at
        improving content while maintaining the original author's voice and ensuring
        consistent quality across multiple sections.
      llm: provider/model-id  # e.g. openai/gpt-4o, google/gemini-2.0-flash, anthropic/claude...
    ```

    These agent definitions establish the specialized roles and perspectives that will shape how our AI agents approach content creation. Notice how each agent has a distinct purpose and expertise.

2.  Next, update the tasks configuration file to define the specific writing and reviewing tasks:

    ```
    # src/guide_creator_flow/crews/content_crew/config/tasks.yaml
    write_section_task:
      description: >
        Write a comprehensive section on the topic: "{section_title}"

        Section description: {section_description}
        Target audience: {audience_level} level learners

        Your content should:
        1. Begin with a brief introduction to the section topic
        2. Explain all key concepts clearly with examples
        3. Include practical applications or exercises where appropriate
        4. End with a summary of key points
        5. Be approximately 500-800 words in length

        Format your content in Markdown with appropriate headings, lists, and emphasis.

        Previously written sections:
        {previous_sections}

        Make sure your content maintains consistency with previously written sections
        and builds upon concepts that have already been explained.
      expected_output: >
        A well-structured, comprehensive section in Markdown format that thoroughly
        explains the topic and is appropriate for the target audience.
      agent: content_writer

    review_section_task:
      description: >
        Review and improve the following section on "{section_title}":

        {draft_content}

        Target audience: {audience_level} level learners

        Previously written sections:
        {previous_sections}

        Your review should:
        1. Fix any grammatical or spelling errors
        2. Improve clarity and readability
        3. Ensure content is comprehensive and accurate
        4. Verify consistency with previously written sections
        5. Enhance the structure and flow
        6. Add any missing key information

        Provide the improved version of the section in Markdown format.
      expected_output: >
        An improved, polished version of the section that maintains the original
        structure but enhances clarity, accuracy, and consistency.
      agent: content_reviewer
      context:
        - write_section_task
    ```

    These task definitions provide detailed instructions to our agents, ensuring they produce content that meets our quality standards. Note how the `context` parameter in the review task creates a workflow where the reviewer has access to the writer’s output.

3.  Now, update the crew implementation file to define how our agents and tasks work together:

    ```
    # src/guide_creator_flow/crews/content_crew/content_crew.py
    from crewai import Agent, Crew, Process, Task
    from crewai.project import CrewBase, agent, crew, task
    from crewai.agents.agent_builder.base_agent import BaseAgent
    from typing import List

    @CrewBase
    class ContentCrew():
        """Content writing crew"""

        agents: List[BaseAgent]
        tasks: List[Task]

        @agent
        def content_writer(self) -> Agent:
            return Agent(
                config=self.agents_config['content_writer'], # type: ignore[index]
                verbose=True
            )

        @agent
        def content_reviewer(self) -> Agent:
            return Agent(
                config=self.agents_config['content_reviewer'], # type: ignore[index]
                verbose=True
            )

        @task
        def write_section_task(self) -> Task:
            return Task(
                config=self.tasks_config['write_section_task'] # type: ignore[index]
            )

        @task
        def review_section_task(self) -> Task:
            return Task(
                config=self.tasks_config['review_section_task'], # type: ignore[index]
                context=[self.write_section_task()]
            )

        @crew
        def crew(self) -> Crew:
            """Creates the content writing crew"""
            return Crew(
                agents=self.agents,
                tasks=self.tasks,
                process=Process.sequential,
                verbose=True,
            )
    ```

    This crew definition establishes the relationship between our agents and tasks, setting up a sequential process where the content writer creates a draft and then the reviewer improves it. While this crew can function independently, in our flow it will be orchestrated as part of a larger system.

## Step 5: Create the Flow

Now comes the exciting part - creating the flow that will orchestrate the entire guide creation process. This is where we’ll combine regular Python code, direct LLM calls, and our content creation crew into a cohesive system.Our flow will:

1.  Get user input for a topic and audience level
2.  Make a direct LLM call to create a structured guide outline
3.  Process each section sequentially using the content writer crew
4.  Combine everything into a final comprehensive document

Let’s create our flow in the `main.py` file:

```
#!/usr/bin/env python
import json
import os
from typing import List, Dict
from pydantic import BaseModel, Field
from crewai import LLM
from crewai.flow.flow import Flow, listen, start
from guide_creator_flow.crews.content_crew.content_crew import ContentCrew

# Define our models for structured data
class Section(BaseModel):
    title: str = Field(description="Title of the section")
    description: str = Field(description="Brief description of what the section should cover")

class GuideOutline(BaseModel):
    title: str = Field(description="Title of the guide")
    introduction: str = Field(description="Introduction to the topic")
    target_audience: str = Field(description="Description of the target audience")
    sections: List[Section] = Field(description="List of sections in the guide")
    conclusion: str = Field(description="Conclusion or summary of the guide")

# Define our flow state
class GuideCreatorState(BaseModel):
    topic: str = ""
    audience_level: str = ""
    guide_outline: GuideOutline = None
    sections_content: Dict[str, str] = {}

class GuideCreatorFlow(Flow[GuideCreatorState]):
    """Flow for creating a comprehensive guide on any topic"""

    @start()
    def get_user_input(self):
        """Get input from the user about the guide topic and audience"""
        print("\n=== Create Your Comprehensive Guide ===\n")

        # Get user input
        self.state.topic = input("What topic would you like to create a guide for? ")

        # Get audience level with validation
        while True:
            audience = input("Who is your target audience? (beginner/intermediate/advanced) ").lower()
            if audience in ["beginner", "intermediate", "advanced"]:
                self.state.audience_level = audience
                break
            print("Please enter 'beginner', 'intermediate', or 'advanced'")

        print(f"\nCreating a guide on {self.state.topic} for {self.state.audience_level} audience...\n")
        return self.state

    @listen(get_user_input)
    def create_guide_outline(self, state):
        """Create a structured outline for the guide using a direct LLM call"""
        print("Creating guide outline...")

        # Initialize the LLM
        llm = LLM(model="openai/gpt-4o-mini", response_format=GuideOutline)

        # Create the messages for the outline
        messages = [\
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},\
            {"role": "user", "content": f"""\
            Create a detailed outline for a comprehensive guide on "{state.topic}" for {state.audience_level} level learners.\
\
            The outline should include:\
            1. A compelling title for the guide\
            2. An introduction to the topic\
            3. 4-6 main sections that cover the most important aspects of the topic\
            4. A conclusion or summary\
\
            For each section, provide a clear title and a brief description of what it should cover.\
            """}\
        ]

        # Make the LLM call with JSON response format
        response = llm.call(messages=messages)

        # Parse the JSON response
        outline_dict = json.loads(response)
        self.state.guide_outline = GuideOutline(**outline_dict)

        # Ensure output directory exists before saving
        os.makedirs("output", exist_ok=True)

        # Save the outline to a file
        with open("output/guide_outline.json", "w") as f:
            json.dump(outline_dict, f, indent=2)

        print(f"Guide outline created with {len(self.state.guide_outline.sections)} sections")
        return self.state.guide_outline

    @listen(create_guide_outline)
    def write_and_compile_guide(self, outline):
        """Write all sections and compile the guide"""
        print("Writing guide sections and compiling...")
        completed_sections = []

        # Process sections one by one to maintain context flow
        for section in outline.sections:
            print(f"Processing section: {section.title}")

            # Build context from previous sections
            previous_sections_text = ""
            if completed_sections:
                previous_sections_text = "# Previously Written Sections\n\n"
                for title in completed_sections:
                    previous_sections_text += f"## {title}\n\n"
                    previous_sections_text += self.state.sections_content.get(title, "") + "\n\n"
            else:
                previous_sections_text = "No previous sections written yet."

            # Run the content crew for this section
            result = ContentCrew().crew().kickoff(inputs={
                "section_title": section.title,
                "section_description": section.description,
                "audience_level": self.state.audience_level,
                "previous_sections": previous_sections_text,
                "draft_content": ""
            })

            # Store the content
            self.state.sections_content[section.title] = result.raw
            completed_sections.append(section.title)
            print(f"Section completed: {section.title}")

        # Compile the final guide
        guide_content = f"# {outline.title}\n\n"
        guide_content += f"## Introduction\n\n{outline.introduction}\n\n"

        # Add each section in order
        for section in outline.sections:
            section_content = self.state.sections_content.get(section.title, "")
            guide_content += f"\n\n{section_content}\n\n"

        # Add conclusion
        guide_content += f"## Conclusion\n\n{outline.conclusion}\n\n"

        # Save the guide
        with open("output/complete_guide.md", "w") as f:
            f.write(guide_content)

        print("\nComplete guide compiled and saved to output/complete_guide.md")
        return "Guide creation completed successfully"

def kickoff():
    """Run the guide creator flow"""
    GuideCreatorFlow().kickoff()
    print("\n=== Flow Complete ===")
    print("Your comprehensive guide is ready in the output directory.")
    print("Open output/complete_guide.md to view it.")

def plot():
    """Generate a visualization of the flow"""
    flow = GuideCreatorFlow()
    flow.plot("guide_creator_flow")
    print("Flow visualization saved to guide_creator_flow.html")

if __name__ == "__main__":
    kickoff()
```

Let’s analyze what’s happening in this flow:

1.  We define Pydantic models for structured data, ensuring type safety and clear data representation
2.  We create a state class to maintain data across different steps of the flow
3.  We implement three main flow steps:
    -   Getting user input with the `@start()` decorator
    -   Creating a guide outline with a direct LLM call
    -   Processing sections with our content crew
4.  We use the `@listen()` decorator to establish event-driven relationships between steps

This is the power of flows - combining different types of processing (user interaction, direct LLM calls, crew-based tasks) into a coherent, event-driven system.

## Step 6: Set Up Your Environment Variables

Create a `.env` file in your project root with your API keys. See the [LLM setup
guide](https://docs.crewai.com/en/concepts/llms#setting-up-your-llm) for details on configuring a provider.

.env

```
OPENAI_API_KEY=your_openai_api_key
# or
GEMINI_API_KEY=your_gemini_api_key
# or
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Step 7: Install Dependencies

Install the required dependencies:

```
crewai install
```

## Step 8: Run Your Flow

Now it’s time to see your flow in action! Run it using the CrewAI CLI:

```
crewai flow kickoff
```

When you run this command, you’ll see your flow spring to life:

1.  It will prompt you for a topic and audience level
2.  It will create a structured outline for your guide
3.  It will process each section, with the content writer and reviewer collaborating on each
4.  Finally, it will compile everything into a comprehensive guide

This demonstrates the power of flows to orchestrate complex processes involving multiple components, both AI and non-AI.

## Step 9: Visualize Your Flow

One of the powerful features of flows is the ability to visualize their structure:

```
crewai flow plot
```

This will create an HTML file that shows the structure of your flow, including the relationships between different steps and the data that flows between them. This visualization can be invaluable for understanding and debugging complex flows.

## Step 10: Review the Output

Once the flow completes, you’ll find two files in the `output` directory:

1.  `guide_outline.json`: Contains the structured outline of the guide
2.  `complete_guide.md`: The comprehensive guide with all sections

Take a moment to review these files and appreciate what you’ve built - a system that combines user input, direct AI interactions, and collaborative agent work to produce a complex, high-quality output.

## The Art of the Possible: Beyond Your First Flow

What you’ve learned in this guide provides a foundation for creating much more sophisticated AI systems. Here are some ways you could extend this basic flow:

### Enhancing User Interaction

You could create more interactive flows with:

-   Web interfaces for input and output
-   Real-time progress updates
-   Interactive feedback and refinement loops
-   Multi-stage user interactions

### Adding More Processing Steps

You could expand your flow with additional steps for:

-   Research before outline creation
-   Image generation for illustrations
-   Code snippet generation for technical guides
-   Final quality assurance and fact-checking

### Creating More Complex Flows

You could implement more sophisticated flow patterns:

-   Conditional branching based on user preferences or content type
-   Parallel processing of independent sections
-   Iterative refinement loops with feedback
-   Integration with external APIs and services

### Applying to Different Domains

The same patterns can be applied to create flows for:

-   **Interactive storytelling**: Create personalized stories based on user input
-   **Business intelligence**: Process data, generate insights, and create reports
-   **Product development**: Facilitate ideation, design, and planning
-   **Educational systems**: Create personalized learning experiences

## Key Features Demonstrated

This guide creator flow demonstrates several powerful features of CrewAI:

1.  **User interaction**: The flow collects input directly from the user
2.  **Direct LLM calls**: Uses the LLM class for efficient, single-purpose AI interactions
3.  **Structured data with Pydantic**: Uses Pydantic models to ensure type safety
4.  **Sequential processing with context**: Writes sections in order, providing previous sections for context
5.  **Multi-agent crews**: Leverages specialized agents (writer and reviewer) for content creation
6.  **State management**: Maintains state across different steps of the process
7.  **Event-driven architecture**: Uses the `@listen` decorator to respond to events

## Understanding the Flow Structure

Let’s break down the key components of flows to help you understand how to build your own:

### 1. Direct LLM Calls

Flows allow you to make direct calls to language models when you need simple, structured responses:

```
llm = LLM(
    model="model-id-here",  # gpt-4o, gemini-2.0-flash, anthropic/claude...
    response_format=GuideOutline
)
response = llm.call(messages=messages)
```

This is more efficient than using a crew when you need a specific, structured output.

### 2. Event-Driven Architecture

Flows use decorators to establish relationships between components:

```
@start()
def get_user_input(self):
    # First step in the flow
    # ...

@listen(get_user_input)
def create_guide_outline(self, state):
    # This runs when get_user_input completes
    # ...
```

This creates a clear, declarative structure for your application.

### 3. State Management

Flows maintain state across steps, making it easy to share data:

```
class GuideCreatorState(BaseModel):
    topic: str = ""
    audience_level: str = ""
    guide_outline: GuideOutline = None
    sections_content: Dict[str, str] = {}
```

This provides a type-safe way to track and transform data throughout your flow.

### 4. Crew Integration

Flows can seamlessly integrate with crews for complex collaborative tasks:

```
result = ContentCrew().crew().kickoff(inputs={
    "section_title": section.title,
    # ...
})
```

This allows you to use the right tool for each part of your application - direct LLM calls for simple tasks and crews for complex collaboration.

## Next Steps

Now that you’ve built your first flow, you can:

1.  Experiment with more complex flow structures and patterns
2.  Try using `@router()` to create conditional branches in your flows
3.  Explore the `and_` and `or_` functions for more complex parallel execution
4.  Connect your flow to external APIs, databases, or user interfaces
5.  Combine multiple specialized crews in a single flow
6.  Build multi-turn chat apps with [Conversational Flows](https://docs.crewai.com/en/guides/flows/conversational-flows) (`kickoff` per message, `ChatSession`, deferred tracing)

Congratulations! You’ve successfully built your first CrewAI Flow that combines regular code, direct LLM calls, and crew-based processing to create a comprehensive guide. These foundational skills enable you to create increasingly sophisticated AI applications that can tackle complex, multi-stage problems through a combination of procedural control and collaborative intelligence.

https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?w=1100&fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=540eb3d8d8f256d6d703aa5e6111a4cd

</details>

<details>
<summary>Introduction</summary>

# Introduction

**Source URL:** <https://docs.crewai.com/introduction>

**CrewAI is the leading open-source framework for orchestrating autonomous AI agents and building complex workflows.**It empowers developers to build production-ready multi-agent systems by combining the collaborative intelligence of **Crews** with the precise control of **Flows**.

- **[CrewAI Flows](https://docs.crewai.com/en/guides/flows/first-flow)**: The backbone of your AI application. Flows allow you to create structured, event-driven workflows that manage state and control execution. They provide the scaffolding for your AI agents to work within.
- **[CrewAI Crews](https://docs.crewai.com/en/guides/crews/first-crew)**: The units of work within your Flow. Crews are teams of autonomous agents that collaborate to solve specific tasks delegated to them by the Flow.

### Watch: Building CrewAI Agents & Flows with Coding Agent Skills

Install our coding agent skills (Claude Code, Codex, …) to quickly get your coding agents up and running with CrewAI.You can install it with `npx skills add crewaiinc/skills`

Getting Started with CrewAI Skills Installation and Usage 🚀

## The CrewAI Architecture

CrewAI’s architecture is designed to balance autonomy with control.

### 1\. Flows: The Backbone

Think of a Flow as the “manager” or the “process definition” of your application. It defines the steps, the logic, and how data moves through your system.

https://mintcdn.com/crewai/qVjgZHKAyEOgSSUS/images/flows.png?fit=max&auto=format&n=qVjgZHKAyEOgSSUS&q=85&s=82ea168de2f004553dcea21410cd7d8a

CrewAI Framework Overview

Flows provide:

- **State Management**: Persist data across steps and executions.
- **Event-Driven Execution**: Trigger actions based on events or external inputs.
- **Control Flow**: Use conditional logic, loops, and branching.

### 2\. Crews: The Intelligence

Crews are the “teams” that do the heavy lifting. Within a Flow, you can trigger a Crew to tackle a complex problem requiring creativity and collaboration.

https://mintcdn.com/crewai/5SZbe87tsCWZY09V/images/crews.png?fit=max&auto=format&n=5SZbe87tsCWZY09V&q=85&s=514fd0b06e4128e62f10728d44601975

CrewAI Framework Overview

Crews provide:

- **Role-Playing Agents**: Specialized agents with specific goals and tools.
- **Autonomous Collaboration**: Agents work together to solve tasks.
- **Task Delegation**: Tasks are assigned and executed based on agent capabilities.

## How It All Works Together

1. **The Flow** triggers an event or starts a process.
2. **The Flow** manages the state and decides what to do next.
3. **The Flow** delegates a complex task to a **Crew**.
4. **The Crew**’s agents collaborate to complete the task.
5. **The Crew** returns the result to the **Flow**.
6. **The Flow** continues execution based on the result.

## Key Features

## Production-Grade Flows

Build reliable, stateful workflows that can handle long-running processes and complex logic.

## Autonomous Crews

Deploy teams of agents that can plan, execute, and collaborate to achieve high-level goals.

## Flexible Tools

Connect your agents to any API, database, or local tool.

## Enterprise Security

Designed with security and compliance in mind for enterprise deployments.

## When to Use Crews vs. Flows

**The short answer: Use both.**For any production-ready application, **start with a Flow**.

- **Use a Flow** to define the overall structure, state, and logic of your application.
- **Use a Crew** within a Flow step when you need a team of agents to perform a specific, complex task that requires autonomy.

| Use Case | Architecture |
| --- | --- |
| **Simple Automation** | Single Flow with Python tasks |
| **Complex Research** | Flow managing state -> Crew performing research |
| **Application Backend** | Flow handling API requests -> Crew generating content -> Flow saving to DB |

## Why Choose CrewAI?

- 🧠 **Autonomous Operation**: Agents make intelligent decisions based on their roles and available tools
- 📝 **Natural Interaction**: Agents communicate and collaborate like human team members
- 🛠️ **Extensible Design**: Easy to add new tools, roles, and capabilities
- 🚀 **Production Ready**: Built for reliability and scalability in real-world applications
- 🔒 **Security-Focused**: Designed with enterprise security requirements in mind
- 💰 **Cost-Efficient**: Optimized to minimize token usage and API calls

</details>

<details>
<summary>Quickstart</summary>

# Quickstart

**Source URL:** <https://gofastmcp.com/getting-started/quickstart>

Welcome! This guide will help you quickly set up FastMCP, run your first MCP server, give it a visual UI, and deploy it to Prefect Horizon.If you haven’t already installed FastMCP, follow the [installation instructions](https://gofastmcp.com/getting-started/installation).

## Create a FastMCP Server

A FastMCP server is a collection of tools, resources, and other MCP components. To create a server, start by instantiating the `FastMCP` class.Create a new file called `my_server.py` and add the following code:

my\_server.py

```
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```

That’s it! You’ve created a FastMCP server, albeit a very boring one. Let’s add a tool to make it more interesting.

## Add a Tool

To add a tool that returns a simple greeting, write a function and decorate it with `@mcp.tool` to register it with the server:

my\_server.py

```
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

## Run the Server

The simplest way to run your FastMCP server is to call its `run()` method. You can choose between different transports, like `stdio` for local servers, or `http` for remote access:

my\_server.py (stdio)

my\_server.py (HTTP)

```
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

This lets us run the server with `python my_server.py`. The stdio transport is the traditional way to connect MCP servers to clients, while the HTTP transport enables remote connections.

Why do we need the `if __name__ == "__main__":` block?The `__main__` block is recommended for consistency and compatibility, ensuring your server works with all MCP clients that execute your server file as a script. Users who will exclusively run their server with the FastMCP CLI can omit it, as the CLI imports the server object directly.

### Using the FastMCP CLI

You can also use the `fastmcp run` command to start your server. Note that the FastMCP CLI **does not** execute the `__main__` block of your server file. Instead, it imports your server object and runs it with whatever transport and options you provide.For example, to run this server with the default stdio transport (no matter how you called `mcp.run()`), you can use the following command:

```
fastmcp run my_server.py:mcp
```

To run this server with the HTTP transport, you can use the following command:

```
fastmcp run my_server.py:mcp --transport http --port 8000
```

## Call Your Server

Once your server is running with HTTP transport, you can connect to it with a FastMCP client or any LLM client that supports the MCP protocol:

my\_client.py

```
import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool("Ford"))
```

Note that:

- FastMCP clients are asynchronous, so we need to use `asyncio.run` to run the client
- We must enter a client context (`async with client:`) before using the client
- You can make multiple client calls within the same context

## Give Your Tool a UI

Tools normally return text, but any tool can return an interactive UI instead. Add `app=True` to your tool decorator and return a [Prefab](https://prefab.prefect.io/) component — the host renders it as a chart, table, form, or any other visual element right in the conversation. This requires the `apps` extra (`pip install "fastmcp[apps]"`).The `app=True` flag tells FastMCP to wire up the renderer and protocol metadata automatically. The tool still works like any other MCP tool — it receives arguments and returns a result — but the result is a component tree that the host displays visually instead of as plain text.

my\_server.py

```
from prefab_ui.app import PrefabApp
from prefab_ui.components import Column, Heading, Text, Badge, Row
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool(app=True)
def greet(name: str) -> PrefabApp:
    """Greet someone with a visual card."""
    with Column(gap=4, css_class="p-6") as view:
        Heading(f"Hello, {name}!")
        with Row(gap=2, align="center"):
            Text("Status")
            Badge("Greeted", variant="success")

    return PrefabApp(view=view)
```

You can preview app tools locally with `fastmcp dev apps my_server.py` — no MCP host required. See the [Apps overview](https://gofastmcp.com/apps/overview) for the full guide, including state management, forms, charts, and server-connected interactivity.

## Deploy to Prefect Horizon

[Prefect Horizon](https://horizon.prefect.io/?utm_source=gofastmcp&utm_medium=docs) is the enterprise MCP platform built by the FastMCP team at [Prefect](https://www.prefect.io/). It provides managed hosting, authentication, access control, and observability for MCP servers.

Horizon is **free for personal projects** and offers enterprise governance for teams.

To deploy your server, you’ll need a [GitHub account](https://github.com/). Once you have one, you can deploy your server in three steps:

1.  Push your `my_server.py` file to a GitHub repository
2.  Sign in to [Prefect Horizon](https://horizon.prefect.io/?utm_source=gofastmcp&utm_medium=docs) with your GitHub account
3.  Create a new project from your repository and enter `my_server.py:mcp` as the server entrypoint

That’s it! Horizon will build and deploy your server, making it available at a URL like `https://your-project.fastmcp.app/mcp`. You can chat with it to test its functionality, or connect to it from any LLM client that supports the MCP protocol.For more details, see the [Prefect Horizon guide](https://gofastmcp.com/deployment/prefect-horizon).

</details>

<details>
<summary>Persistence</summary>

# Persistence

**Source URL:** <https://docs.langchain.com/oss/python/langgraph/persistence>

Persistence lets LangGraph applications keep useful information beyond a single graph run. It matters when an agent needs to continue a conversation, resume after an interruption, recover from a failure, or remember information across interactions.LangGraph provides two complementary persistence systems:

- **[Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers)** persist a thread’s graph state as checkpoints. Use them for short-term, thread-scoped memory, including conversation continuity, human-in-the-loop workflows, time travel, and fault tolerance.
- **[Stores](https://docs.langchain.com/oss/python/langgraph/stores)** persist application-defined data outside the graph state. Use them for long-term, cross-thread memory, including user preferences, facts, and shared knowledge.

Most applications can use both: a [checkpointer](https://docs.langchain.com/oss/python/langgraph/checkpointers) tracks the current thread, and a [store](https://docs.langchain.com/oss/python/langgraph/stores) tracks durable information across threads.

## [​](https://docs.langchain.com/oss/python/langgraph/persistence\#quickstart)  Quickstart

Compile your graph with a checkpointer, a store, or both:

```
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.memory import InMemoryStore

checkpointer = InMemorySaver()
store = InMemoryStore()

graph = builder.compile(checkpointer=checkpointer, store=store)

result = graph.invoke(
    {"messages": [{"role": "user", "content": "Hi, my name is Bob."}]},
    {"configurable": {"thread_id": "thread-1"}},
)
```

**Agent Server handles persistence automatically**
When using the [Agent Server](https://docs.langchain.com/langsmith/agent-server), you do not need to implement or configure checkpointers or stores manually. The server handles persistence infrastructure behind the scenes.

## [​](https://docs.langchain.com/oss/python/langgraph/persistence\#checkpointer-vs-store)  Checkpointer vs. store

|  | Checkpointer | Store |
| --- | --- | --- |
| Persists | Graph state snapshots | Application-defined key-value data |
| Scope | A single thread | Across threads |
| Memory type | Short-term, thread-scoped memory | Long-term, cross-thread memory |
| Use for | Conversation continuity, human-in-the-loop, time travel, and fault tolerance | User preferences, facts, and shared knowledge |
| Access pattern | Pass a `thread_id` in graph config | Read and write items from nodes or application code |
| Full guide | [Checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) | [Stores](https://docs.langchain.com/oss/python/langgraph/stores) |

## [​](https://docs.langchain.com/oss/python/langgraph/persistence\#next-steps)  Next steps

- [Use checkpointers](https://docs.langchain.com/oss/python/langgraph/checkpointers) to persist and inspect thread state.
- [Use stores](https://docs.langchain.com/oss/python/langgraph/stores) to persist durable data across threads.

</details>

<details>
<summary>Durable Execution</summary>

# Durable Execution

**Source URL:** <https://ai.pydantic.dev/durable_execution/overview/>

Pydantic AI allows you to build durable agents that can preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability. Durable agents have full support for [streaming](https://pydantic.dev/docs/ai/core-concepts/agent#streaming-all-events) and [MCP](https://pydantic.dev/docs/ai/mcp/client), with the added benefit of fault tolerance.

Pydantic AI officially supports four durable execution solutions:

- [Temporal](https://pydantic.dev/docs/ai/integrations/durable_execution/temporal)
- [DBOS](https://pydantic.dev/docs/ai/integrations/durable_execution/dbos)
- [Prefect](https://pydantic.dev/docs/ai/integrations/durable_execution/prefect)
- [Restate](https://pydantic.dev/docs/ai/integrations/durable_execution/restate)

These integrations are co-maintained by the Pydantic and vendor teams and only use Pydantic AI’s public interface, so they also serve as a reference for integrating with other durable systems.

</details>

<details>
<summary>AutoGen Studio User Guide</summary>

# AutoGen Studio User Guide

**Source URL:** <https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>

[https://badge.fury.io/py/autogenstudio.svg](https://badge.fury.io/py/autogenstudio)[https://static.pepy.tech/badge/autogenstudio/week](https://pepy.tech/project/autogenstudio)

AutoGen Studio is a low-code interface built to help you rapidly prototype AI agents, enhance them with tools, compose them into teams and interact with them to accomplish tasks. It is built on [AutoGen AgentChat](https://microsoft.github.io/autogen) - a high-level API for building multi-agent applications.

> See a video tutorial on AutoGen Studio v0.4 (02/25) - [https://youtu.be/oum6EI7wohM](https://youtu.be/oum6EI7wohM)

[https://img.youtube.com/vi/oum6EI7wohM/maxresdefault.jpg](https://www.youtube.com/watch?v=oum6EI7wohM)

Code for AutoGen Studio is on GitHub at [microsoft/autogen](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-studio)

Caution

AutoGen Studio is meant to help you rapidly prototype multi-agent workflows and demonstrate an example of end user interfaces built with AutoGen. It is not meant to be a production-ready app. Developers are encouraged to use the AutoGen framework to build their own applications, implementing authentication, security and other features required for deployed applications.

## Capabilities - What Can You Do with AutoGen Studio?

AutoGen Studio offers four main interfaces to help you build and manage multi-agent systems:

1.  **Team Builder**
    -   A visual interface for creating agent teams through declarative specification (JSON) or drag-and-drop
    -   Supports configuration of all core components: teams, agents, tools, models, and termination conditions
    -   Fully compatible with AgentChat’s component definitions
2.  **Playground**
    -   Interactive environment for testing and running agent teams
    -   Features include:
        -   Live message streaming between agents
        -   Visual representation of message flow through a control transition graph
        -   Interactive sessions with teams using UserProxyAgent
        -   Full run control with the ability to pause or stop execution
3.  **Gallery**
    -   Central hub for discovering and importing community-created components
    -   Enables easy integration of third-party components
4.  **Deployment**
    -   Export and run teams in python code
    -   Setup and test endpoints based on a team configuration
    -   Run teams in a docker container

## A Note on Security

AutoGen Studio is a research prototype and is **not meant to be used** in a production environment. Some baseline practices are encouraged e.g., using Docker code execution environment for your agents.

However, other considerations such as rigorous tests related to jailbreaking, ensuring LLMs only have access to the right keys of data given the end user’s permissions, and other security features are not implemented in AutoGen Studio.

If you are building a production application, please use the AutoGen framework and implement the necessary security features.

</details>

<details>
<summary>AutoGen</summary>

# AutoGen

**Source URL:** <https://microsoft.github.io/autogen/stable/>

### A framework for building AI agents and applications

Studio [https://img.shields.io/badge/PyPi-autogenstudio-blue?logo=pypi](https://pypi.org/project/autogenstudio/)

An web-based UI for prototyping with agents without writing code.
Built on AgentChat.

```
pip install -U autogenstudio
autogenstudio ui --port 8080 --appdir ./myapp
```

Copy to clipboard

_Start here if you are new to AutoGen and want to prototype with agents without writing code._

[Get Started](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)

AgentChat
[https://img.shields.io/badge/PyPi-autogen--agentchat-blue?logo=pypi](https://pypi.org/project/autogen-agentchat/)

A programming framework for building conversational single and multi-agent applications.
Built on Core. Requires Python 3.10+.

```
# pip install -U "autogen-agentchat" "autogen-ext[openai]"
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main() -> None:
    agent = AssistantAgent("assistant", OpenAIChatCompletionClient(model="gpt-4o"))
    print(await agent.run(task="Say 'Hello World!'"))

asyncio.run(main())
```

Copy to clipboard

_Start here if you are prototyping with agents using Python. [Migrating from AutoGen 0.2?](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/migration-guide.html)._

[Get Started](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/quickstart.html)

Core [https://img.shields.io/badge/PyPi-autogen--core-blue?logo=pypi](https://pypi.org/project/autogen-core/)

An event-driven programming framework for building scalable multi-agent AI systems. Example scenarios:

- Deterministic and dynamic agentic workflows for business processes.

- Research on multi-agent collaboration.

- Distributed agents for multi-language applications.


_Start here if you are getting serious about building multi-agent systems._

[Get Started](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/quickstart.html)

Extensions [https://img.shields.io/badge/PyPi-autogen--ext-blue?logo=pypi](https://pypi.org/project/autogen-ext/)

Implementations of Core and AgentChat components that interface with external services or other libraries.
You can find and use community extensions or create your own. Examples of built-in extensions:

- [`McpWorkbench`](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.tools.mcp.html#autogen_ext.tools.mcp.McpWorkbench "autogen_ext.tools.mcp.McpWorkbench") for using Model-Context Protocol (MCP) servers.

- [`OpenAIAssistantAgent`](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.agents.openai.html#autogen_ext.agents.openai.OpenAIAssistantAgent "autogen_ext.agents.openai.OpenAIAssistantAgent") for using Assistant API.

- [`DockerCommandLineCodeExecutor`](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.code_executors.docker.html#autogen_ext.code_executors.docker.DockerCommandLineCodeExecutor "autogen_ext.code_executors.docker.DockerCommandLineCodeExecutor") for running model-generated code in a Docker container.

- [`GrpcWorkerAgentRuntime`](https://microsoft.github.io/autogen/stable/reference/python/autogen_ext.runtimes.grpc.html#autogen_ext.runtimes.grpc.GrpcWorkerAgentRuntime "autogen_ext.runtimes.grpc.GrpcWorkerAgentRuntime") for distributed agents.


[Discover Community Extensions](https://microsoft.github.io/autogen/stable/user-guide/extensions-user-guide/discover.html) [Create New Extension](https://microsoft.github.io/autogen/stable/user-guide/extensions-user-guide/create-your-own.html)

</details>

<details>
<summary>FastMCP</summary>

# FastMCP

**Source URL:** <https://gofastmcp.com/>

**FastMCP is the standard framework for building MCP applications.** The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) connects LLMs to tools and data. FastMCP gives you everything you need to go from prototype to production — build servers that expose capabilities, connect clients to any MCP service, and give your tools interactive UIs:

```
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

## Move Fast and Make Things

The [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) lets you give agents access to your tools and data. But building an effective MCP application is harder than it looks.FastMCP handles all of it. Declare a tool with a Python function, and the schema, validation, and documentation are generated automatically. Connect to a server with a URL, and transport negotiation, authentication, and protocol lifecycle are managed for you. You focus on your logic, and the MCP part just works: **with FastMCP, best practices are built in.****That’s why FastMCP is the standard framework for working with MCP.** FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages.FastMCP has three pillars:

https://mintcdn.com/fastmcp/uaPe2cZCul164Sax/assets/images/servers-card.png?fit=max&auto=format&n=uaPe2cZCul164Sax&q=85&s=2cddc3be3355623b1b81024811a9f443

**Servers** \
\
Expose tools, resources, and prompts to LLMs.

https://mintcdn.com/fastmcp/uaPe2cZCul164Sax/assets/images/apps-card.png?fit=max&auto=format&n=uaPe2cZCul164Sax&q=85&s=865d32af9c41cf6266a09a8a4fc03fe1

**Apps** \
\
Give your tools interactive UIs rendered directly in the conversation.

https://mintcdn.com/fastmcp/uaPe2cZCul164Sax/assets/images/clients-card.png?fit=max&auto=format&n=uaPe2cZCul164Sax&q=85&s=fbb306d0b3e0858afd1eef7aeacc02cf

**Clients** \
\
Connect to any MCP server — local or remote, programmatic or CLI.

**Servers** wrap your Python functions into MCP-compliant tools, resources, and prompts. **Clients** connect to any server with full protocol support. And **Apps** give your tools interactive UIs rendered directly in the conversation.Ready to build? Start with the [installation guide](https://gofastmcp.com/getting-started/installation) or jump straight to the [quickstart](https://gofastmcp.com/getting-started/quickstart).FastMCP is made with 💙 by [Prefect](https://www.prefect.io/).

## Run FastMCP in production with Horizon

FastMCP is the standard way to build MCP servers. **[Prefect Horizon](https://www.prefect.io/horizon?utm_source=gofastmcp&utm_medium=docs&utm_campaign=docs_welcome&utm_content=welcome_body)** is the enterprise MCP gateway for running them safely.Built by the FastMCP team, Horizon packages the best practices we’ve learned shipping the world’s most popular MCP framework.Deploy FastMCP servers from GitHub with branch previews and instant rollback. Create a private registry of every MCP your company uses. Secure access with SSO and tool-level RBAC. Get audit logs, observability, and governance across your MCP stack. Remix approved tools into purpose-built endpoints for teams and agents.Start with FastMCP. [Scale with Horizon →](https://www.prefect.io/horizon?utm_source=gofastmcp&utm_medium=docs&utm_campaign=docs_welcome&utm_content=welcome_cta)

**This documentation reflects FastMCP’s `main` branch**, meaning it always reflects the latest development version. Features are generally marked with version badges (e.g. `New in version: 3.0.0`) to indicate when they were introduced. Note that this may include features that are not yet released.

## LLM-Friendly Docs

The FastMCP documentation is available in multiple LLM-friendly formats:

### MCP Server

The FastMCP docs are accessible via MCP! The server URL is `https://gofastmcp.com/mcp`.In fact, you can use FastMCP to search the FastMCP docs:

```
import asyncio
from fastmcp import Client

async def main():
    async with Client("https://gofastmcp.com/mcp") as client:
        result = await client.call_tool(
            name="search_fast_mcp",
            arguments={"query": "deploy a FastMCP server"}
        )
    print(result)

asyncio.run(main())
```

### Text Formats

The docs are also available in [llms.txt format](https://llmstxt.org/):

- [llms.txt](https://gofastmcp.com/llms.txt) - A sitemap listing all documentation pages
- [llms-full.txt](https://gofastmcp.com/llms-full.txt) - The entire documentation in one file (may exceed context windows)

Any page can be accessed as markdown by appending `.md` to the URL. For example, this page becomes `https://gofastmcp.com/getting-started/welcome.md`.You can also copy any page as markdown by pressing “Cmd+C” (or “Ctrl+C” on Windows) on your keyboard.

</details>

<details>
<summary>OpenAI Agents SDK</summary>

# OpenAI Agents SDK

**Source URL:** <https://openai.github.io/openai-agents-python/>

The [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) enables you to build agentic AI apps in a lightweight, easy-to-use package with very few abstractions. It's a production-ready upgrade of our previous experimentation for agents, [Swarm](https://github.com/openai/swarm/tree/main). The Agents SDK has a very small set of primitives:

- **Agents**, which are LLMs equipped with instructions and tools
- **Agents as tools / Handoffs**, which allow agents to delegate to other agents for specific tasks
- **Guardrails**, which enable validation of agent inputs and outputs

In combination with Python, these primitives are powerful enough to express complex relationships between tools and agents, and allow you to build real-world applications without a steep learning curve. In addition, the SDK comes with built-in **tracing** that lets you visualize and debug your agentic flows, as well as evaluate them and even fine-tune models for your application.

## Why use the Agents SDK

The SDK has two driving design principles:

1. Enough features to be worth using, but few enough primitives to make it quick to learn.
2. Works great out of the box, but you can customize exactly what happens.

Here are the main features of the SDK:

- **Agent loop**: A built-in agent loop that handles tool invocation, sends results back to the LLM, and continues until the task is complete.
- **Python-first**: Use built-in language features to orchestrate and chain agents, rather than needing to learn new abstractions.
- **Agents as tools / Handoffs**: A powerful mechanism for coordinating and delegating work across multiple agents.
- **Sandbox agents**: Run specialists inside real isolated workspaces with manifest-defined files, sandbox client choice, and resumable sandbox sessions.
- **Guardrails**: Run input validation and safety checks in parallel with agent execution, and fail fast when checks do not pass.
- **Function tools**: Turn any Python function into a tool with automatic schema generation and Pydantic-powered validation.
- **MCP server tool calling**: Built-in MCP server tool integration that works the same way as function tools.
- **Sessions**: A persistent memory layer for maintaining working context within an agent loop.
- **Human in the loop**: Built-in mechanisms for involving humans across agent runs.
- **Tracing**: Built-in tracing for visualizing, debugging, and monitoring workflows, with support for the OpenAI suite of evaluation, fine-tuning, and distillation tools.
- **Realtime Agents**: Build powerful voice agents with `gpt-realtime-2`, automatic interruption detection, context management, guardrails, and more.

## Agents SDK or Responses API?

The SDK uses the Responses API by default for OpenAI models, but it adds a higher-level runtime around model calls.

Use the Responses API directly when:

- you want to own the loop, tool dispatch, and state handling yourself
- your workflow is short-lived and mainly about returning the model's response

Use the Agents SDK when:

- you want the runtime to manage turns, tool execution, guardrails, handoffs, or sessions
- your agent should produce artifacts or operate across multiple coordinated steps
- you need a real workspace or resumable execution through [Sandbox agents](https://openai.github.io/openai-agents-python/sandbox_agents/)

You do not need to choose one globally. Many applications use the SDK for managed workflows and call the Responses API directly for lower-level paths.

## Installation

```
pip install openai-agents
```

## Hello world example

```
from agents import Agent, Runner

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
```

( _If running this, ensure you set the `OPENAI_API_KEY` environment variable_)

```
export OPENAI_API_KEY=sk-...
```

## Start here

- Build your first text-based agent with the [Quickstart](https://openai.github.io/openai-agents-python/quickstart/).
- Then decide how you want to carry state across turns in [Running agents](https://openai.github.io/openai-agents-python/running_agents/#choose-a-memory-strategy).
- If the task depends on real files, repos, or isolated per-agent workspace state, read the [Sandbox agents quickstart](https://openai.github.io/openai-agents-python/sandbox_agents/).
- If you are deciding between handoffs and manager-style orchestration, read [Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/).

## Choose your path

Use this table when you know the job you want to do, but not which page explains it.

| Goal | Start here |
| --- | --- |
| Build the first text agent and see one complete run | [Quickstart](https://openai.github.io/openai-agents-python/quickstart/) |
| Add function tools, hosted tools, or agents as tools | [Tools](https://openai.github.io/openai-agents-python/tools/) |
| Run a coding, review, or document agent inside a real isolated workspace | [Sandbox agents quickstart](https://openai.github.io/openai-agents-python/sandbox_agents/) and [Sandbox clients](https://openai.github.io/openai-agents-python/sandbox/clients/) |
| Decide between handoffs and manager-style orchestration | [Agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/) |
| Keep memory across turns | [Running agents](https://openai.github.io/openai-agents-python/running_agents/#choose-a-memory-strategy) and [Sessions](https://openai.github.io/openai-agents-python/sessions/) |
| Use OpenAI models, websocket transport, or non-OpenAI providers | [Models](https://openai.github.io/openai-agents-python/models/) |
| Review outputs, run items, interruptions, and resume state | [Results](https://openai.github.io/openai-agents-python/results/) |
| Build a low-latency voice agent with `gpt-realtime-2` | [Realtime agents quickstart](https://openai.github.io/openai-agents-python/realtime/quickstart/) and [Realtime transport](https://openai.github.io/openai-agents-python/realtime/transport/) |
| Build a speech-to-text / agent / text-to-speech pipeline | [Voice pipeline quickstart](https://openai.github.io/openai-agents-python/voice/quickstart/) |

</details>

<details>
<summary>Workflows and agents</summary>

# Workflows and agents

**Source URL:** <https://docs.langchain.com/oss/python/langgraph/workflows-agents>

This guide reviews common workflow and agent patterns.

- Workflows have predetermined code paths and are designed to operate in a certain order.
- Agents are dynamic and define their own processes and tool usage.

https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent_workflow.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=c217c9ef517ee556cae3fc928a21dc55LangGraph offers several benefits when building agents and workflows, including [persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [streaming](https://docs.langchain.com/oss/python/langgraph/streaming), and support for debugging as well as [deployment](https://docs.langchain.com/oss/python/langgraph/deploy).

## Setup

To build a workflow or agent, you can use [any chat model](https://docs.langchain.com/oss/python/integrations/chat) that supports structured outputs and tool calling. The following example uses Anthropic:

1. Install dependencies:

```
pip install langchain_core langchain-anthropic langgraph
```

2. Initialize the LLM:

```
import os
import getpass

from langchain_anthropic import ChatAnthropic

def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

_set_env("ANTHROPIC_API_KEY")

llm = ChatAnthropic(model="claude-sonnet-4-6")
```

## LLMs and augmentations

Workflows and agentic systems are based on LLMs and the various augmentations you add to them. [Tool calling](https://docs.langchain.com/oss/python/langchain/tools), [structured outputs](https://docs.langchain.com/oss/python/langchain/structured-output), and [short term memory](https://docs.langchain.com/oss/python/langchain/short-term-memory) are a few options for tailoring LLMs to your needs.https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/augmented_llm.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=7ea9656f46649b3ebac19e8309ae9006

```
# Schema for structured output
from pydantic import BaseModel, Field

class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Query that is optimized web search.")
    justification: str = Field(
        None, description="Why this query is relevant to the user's request."
    )

# Augment the LLM with schema for structured output
structured_llm = llm.with_structured_output(SearchQuery)

# Invoke the augmented LLM
output = structured_llm.invoke("How does Calcium CT score relate to high cholesterol?")

# Define a tool
def multiply(a: int, b: int) -> int:
    return a * b

# Augment the LLM with tools
llm_with_tools = llm.bind_tools([multiply])

# Invoke the LLM with input that triggers the tool call
msg = llm_with_tools.invoke("What is 2 times 3?")

# Get the tool call
msg.tool_calls
```

## Prompt chaining

Prompt chaining is when each LLM call processes the output of the previous call. It’s often used for performing well-defined tasks that can be broken down into smaller, verifiable steps. Some examples include:

- Translating documents into different languages
- Verifying generated content for consistency

https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/prompt_chain.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=762dec147c31b8dc6ebb0857e236fc1f

Graph API

Functional API

```
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from IPython.display import Image, display

# Graph state
class State(TypedDict):
    topic: str
    joke: str
    improved_joke: str
    final_joke: str

# Nodes
def generate_joke(state: State):
    """First LLM call to generate initial joke"""

    msg = llm.invoke(f"Write a short joke about {state['topic']}")
    return {"joke": msg.content}

def check_punchline(state: State):
    """Gate function to check if the joke has a punchline"""

    # Simple check - does the joke contain "?" or "!"
    if "?" in state["joke"] or "!" in state["joke"]:
        return "Pass"
    return "Fail"

def improve_joke(state: State):
    """Second LLM call to improve the joke"""

    msg = llm.invoke(f"Make this joke funnier by adding wordplay: {state['joke']}")
    return {"improved_joke": msg.content}

def polish_joke(state: State):
    """Third LLM call for final polish"""
    msg = llm.invoke(f"Add a surprising twist to this joke: {state['improved_joke']}")
    return {"final_joke": msg.content}

# Build workflow
workflow = StateGraph(State)

# Add nodes
workflow.add_node("generate_joke", generate_joke)
workflow.add_node("improve_joke", improve_joke)
workflow.add_node("polish_joke", polish_joke)

# Add edges to connect nodes
workflow.add_edge(START, "generate_joke")
workflow.add_conditional_edges(
    "generate_joke", check_punchline, {"Fail": "improve_joke", "Pass": END}
)
workflow.add_edge("improve_joke", "polish_joke")
workflow.add_edge("polish_joke", END)

# Compile
chain = workflow.compile()

# Show workflow
display(Image(chain.get_graph().draw_mermaid_png()))

# Invoke
state = chain.invoke({"topic": "cats"})
print("Initial joke:")
print(state["joke"])
print("\n--- --- ---\n")
if "improved_joke" in state:
    print("Improved joke:")
    print(state["improved_joke"])
    print("\n--- --- ---\n")

    print("Final joke:")
    print(state["final_joke"])
else:
    print("Final joke:")
    print(state["joke"])
```

## Parallelization

With parallelization, LLMs work simultaneously on a task. This is either done by running multiple independent subtasks at the same time, or running the same task multiple times to check for different outputs. Parallelization is commonly used to:

- Split up subtasks and run them in parallel, which increases speed
- Run tasks multiple times to check for different outputs, which increases confidence

Some examples include:

- Running one subtask that processes a document for keywords, and a second subtask to check for formatting errors
- Running a task multiple times that scores a document for accuracy based on different criteria, like the number of citations, the number of sources used, and the quality of the sources

https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/parallelization.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=8afe3c427d8cede6fed1e4b2a5107b71

Graph API

Functional API

```
# Graph state
class State(TypedDict):
    topic: str
    joke: str
    story: str
    poem: str
    combined_output: str

# Nodes
def call_llm_1(state: State):
    """First LLM call to generate initial joke"""

    msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def call_llm_2(state: State):
    """Second LLM call to generate story"""

    msg = llm.invoke(f"Write a story about {state['topic']}")
    return {"story": msg.content}

def call_llm_3(state: State):
    """Third LLM call to generate poem"""

    msg = llm.invoke(f"Write a poem about {state['topic']}")
    return {"poem": msg.content}

def aggregator(state: State):
    """Combine the joke, story and poem into a single output"""

    combined = f"Here's a story, joke, and poem about {state['topic']}!\n\n"
    combined += f"STORY:\n{state['story']}\n\n"
    combined += f"JOKE:\n{state['joke']}\n\n"
    combined += f"POEM:\n{state['poem']}"
    return {"combined_output": combined}

# Build workflow
parallel_builder = StateGraph(State)

# Add nodes
parallel_builder.add_node("call_llm_1", call_llm_1)
parallel_builder.add_node("call_llm_2", call_llm_2)
parallel_builder.add_node("call_llm_3", call_llm_3)
parallel_builder.add_node("aggregator", aggregator)

# Add edges to connect nodes
parallel_builder.add_edge(START, "call_llm_1")
parallel_builder.add_edge(START, "call_llm_2")
parallel_builder.add_edge(START, "call_llm_3")
parallel_builder.add_edge("call_llm_1", "aggregator")
parallel_builder.add_edge("call_llm_2", "aggregator")
parallel_builder.add_edge("call_llm_3", "aggregator")
parallel_builder.add_edge("aggregator", END)
parallel_workflow = parallel_builder.compile()

# Show workflow
display(Image(parallel_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = parallel_workflow.invoke({"topic": "cats"})
print(state["combined_output"])
```

## Routing

Routing workflows process inputs and then directs them to context-specific tasks. This allows you to define specialized flows for complex tasks. For example, a workflow built to answer product related questions might process the type of question first, and then route the request to specific processes for pricing, refunds, returns, etc.https://mintcdn.com/langchain-5e9cc07a/dL5Sn6Cmy9pwtY0V/oss/images/routing.png?fit=max&auto=format&n=dL5Sn6Cmy9pwtY0V&q=85&s=272e0e9b681b89cd7d35d5c812c50ee6

Graph API

Functional API

```
from typing_extensions import Literal
from langchain.messages import HumanMessage, SystemMessage

# Schema for structured output to use as routing logic
class Route(BaseModel):
    step: Literal["poem", "story", "joke"] = Field(
        None, description="The next step in the routing process"
    )

# Augment the LLM with schema for structured output
router = llm.with_structured_output(Route)

# State
class State(TypedDict):
    input: str
    decision: str
    output: str

# Nodes
def llm_call_1(state: State):
    """Write a story"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_2(state: State):
    """Write a joke"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_3(state: State):
    """Write a poem"""

    result = llm.invoke(state["input"])
    return {"output": result.content}

def llm_call_router(state: State):
    """Route the input to the appropriate node"""

    # Run the augmented LLM with structured output to serve as routing logic
    decision = router.invoke(
        [\
            SystemMessage(\
                content="Route the input to story, joke, or poem based on the user's request."\
            ),\
            HumanMessage(content=state["input"]),\
        ]
    )

    return {"decision": decision.step}

# Conditional edge function to route to the appropriate node
def route_decision(state: State):
    # Return the node name you want to visit next
    if state["decision"] == "story":
        return "llm_call_1"
    elif state["decision"] == "joke":
        return "llm_call_2"
    elif state["decision"] == "poem":
        return "llm_call_3"

# Build workflow
router_builder = StateGraph(State)

# Add nodes
router_builder.add_node("llm_call_1", llm_call_1)
router_builder.add_node("llm_call_2", llm_call_2)
router_builder.add_node("llm_call_3", llm_call_3)
router_builder.add_node("llm_call_router", llm_call_router)

# Add edges to connect nodes
router_builder.add_edge(START, "llm_call_router")
router_builder.add_conditional_edges(
    "llm_call_router",
    route_decision,
    {  # Name returned by route_decision : Name of next node to visit
        "llm_call_1": "llm_call_1",
        "llm_call_2": "llm_call_2",
        "llm_call_3": "llm_call_3",
    },
)
router_builder.add_edge("llm_call_1", END)
router_builder.add_edge("llm_call_2", END)
router_builder.add_edge("llm_call_3", END)

# Compile workflow
router_workflow = router_builder.compile()

# Show the workflow
display(Image(router_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = router_workflow.invoke({"input": "Write me a joke about cats"})
print(state["output"])
```

## Orchestrator-worker

In an orchestrator-worker configuration, the orchestrator:

- Breaks down tasks into subtasks
- Delegates subtasks to workers
- Synthesizes worker outputs into a final result

https://mintcdn.com/langchain-5e9cc07a/ybiAaBfoBvFquMDz/oss/images/worker.png?fit=max&auto=format&n=ybiAaBfoBvFquMDz&q=85&s=2e423c67cd4f12e049cea9c169ff0676Orchestrator-worker workflows provide more flexibility and are often used when subtasks cannot be predefined the way they can with [parallelization](https://docs.langchain.com/oss/python/langgraph/workflows-agents#parallelization). This is common with workflows that write code or need to update content across multiple files. For example, a workflow that needs to update installation instructions for multiple Python libraries across an unknown number of documents might use this pattern.

Graph API

Functional API

```
from typing import Annotated, List
import operator

# Schema for structured output to use in planning
class Section(BaseModel):
    name: str = Field(
        description="Name for this section of the report.",
    )
    description: str = Field(
        description="Brief overview of the main topics and concepts to be covered in this section.",
    )

class Sections(BaseModel):
    sections: List[Section] = Field(
        description="Sections of the report.",
    )

# Augment the LLM with schema for structured output
planner = llm.with_structured_output(Sections)
```

### Creating workers in LangGraph

Orchestrator-worker workflows are common and LangGraph has built-in support for them. The `Send` API lets you dynamically create worker nodes and send them specific inputs. Each worker has its own state, and all worker outputs are written to a shared state key that is accessible to the orchestrator graph. This gives the orchestrator access to all worker output and allows it to synthesize them into a final output. The example below iterates over a list of sections and uses the `Send` API to send a section to each worker.

```
from langgraph.types import Send

# Graph state
class State(TypedDict):
    topic: str  # Report topic
    sections: list[Section]  # List of report sections
    completed_sections: Annotated[\
        list, operator.add\
    ]  # All workers write to this key in parallel
    final_report: str  # Final report

# Worker state
class WorkerState(TypedDict):
    section: Section
    completed_sections: Annotated[list, operator.add]

# Nodes
def orchestrator(state: State):
    """Orchestrator that generates a plan for the report"""

    # Generate queries
    report_sections = planner.invoke(
        [\
            SystemMessage(content="Generate a plan for the report."),\
            HumanMessage(content=f"Here is the report topic: {state['topic']}"),\
        ]
    )

    return {"sections": report_sections.sections}

def llm_call(state: WorkerState):
    """Worker writes a section of the report"""

    # Generate section
    section = llm.invoke(
        [\
            SystemMessage(\
                content="Write a report section following the provided name and description. Include no preamble for each section. Use markdown formatting."\
            ),\
            HumanMessage(\
                content=f"Here is the section name: {state['section'].name} and description: {state['section'].description}"\
            ),\
        ]
    )

    # Write the updated section to completed sections
    return {"completed_sections": [section.content]}

def synthesizer(state: State):
    """Synthesize full report from sections"""

    # List of completed sections
    completed_sections = state["completed_sections"]

    # Format completed section to str to use as context for final sections
    completed_report_sections = "\n\n---\n\n".join(completed_sections)

    return {"final_report": completed_report_sections}

# Conditional edge function to create llm_call workers that each write a section of the report
def assign_workers(state: State):
    """Assign a worker to each section in the plan"""

    # Kick off section writing in parallel via Send() API
    return [Send("llm_call", {"section": s}) for s in state["sections"]]

# Build workflow
orchestrator_worker_builder = StateGraph(State)

# Add the nodes
orchestrator_worker_builder.add_node("orchestrator", orchestrator)
orchestrator_worker_builder.add_node("llm_call", llm_call)
orchestrator_worker_builder.add_node("synthesizer", synthesizer)

# Add edges to connect nodes
orchestrator_worker_builder.add_edge(START, "orchestrator")
orchestrator_worker_builder.add_conditional_edges(
    "orchestrator", assign_workers, ["llm_call"]
)
orchestrator_worker_builder.add_edge("llm_call", "synthesizer")
orchestrator_worker_builder.add_edge("synthesizer", END)

# Compile the workflow
orchestrator_worker = orchestrator_worker_builder.compile()

# Show the workflow
display(Image(orchestrator_worker.get_graph().draw_mermaid_png()))

# Invoke
state = orchestrator_worker.invoke({"topic": "Create a report on LLM scaling laws"})

from IPython.display import Markdown
Markdown(state["final_report"])
```

## Evaluator-optimizer

In evaluator-optimizer workflows, one LLM call creates a response and the other evaluates that response. If the evaluator or a [human-in-the-loop](https://docs.langchain.com/oss/python/langgraph/interrupts) determines the response needs refinement, feedback is provided and the response is recreated. This loop continues until an acceptable response is generated.Evaluator-optimizer workflows are commonly used when there’s particular success criteria for a task, but iteration is required to meet that criteria. For example, there’s not always a perfect match when translating text between two languages. It might take a few iterations to generate a translation with the same meaning across the two languages.https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/evaluator_optimizer.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=9bd0474f42b6040b14ed6968a9ab4e3c

Graph API

Functional API

```
# Graph state
class State(TypedDict):
    joke: str
    topic: str
    feedback: str
    funny_or_not: str

# Schema for structured output to use in evaluation
class Feedback(BaseModel):
    grade: Literal["funny", "not funny"] = Field(
        description="Decide if the joke is funny or not.",
    )
    feedback: str = Field(
        description="If the joke is not funny, provide feedback on how to improve it.",
    )

# Augment the LLM with schema for structured output
evaluator = llm.with_structured_output(Feedback)

# Nodes
def llm_call_generator(state: State):
    """LLM generates a joke"""

    if state.get("feedback"):
        msg = llm.invoke(
            f"Write a joke about {state['topic']} but take into account the feedback: {state['feedback']}"
        )
    else:
        msg = llm.invoke(f"Write a joke about {state['topic']}")
    return {"joke": msg.content}

def llm_call_evaluator(state: State):
    """LLM evaluates the joke"""

    grade = evaluator.invoke(f"Grade the joke {state['joke']}")
    return {"funny_or_not": grade.grade, "feedback": grade.feedback}

# Conditional edge function to route back to joke generator or end based upon feedback from the evaluator
def route_joke(state: State):
    """Route back to joke generator or end based upon feedback from the evaluator"""

    if state["funny_or_not"] == "funny":
        return "Accepted"
    elif state["funny_or_not"] == "not funny":
        return "Rejected + Feedback"

# Build workflow
optimizer_builder = StateGraph(State)

# Add the nodes
optimizer_builder.add_node("llm_call_generator", llm_call_generator)
optimizer_builder.add_node("llm_call_evaluator", llm_call_evaluator)

# Add edges to connect nodes
optimizer_builder.add_edge(START, "llm_call_generator")
optimizer_builder.add_edge("llm_call_generator", "llm_call_evaluator")
optimizer_builder.add_conditional_edges(
    "llm_call_evaluator",
    route_joke,
    {  # Name returned by route_joke : Name of next node to visit
        "Accepted": END,
        "Rejected + Feedback": "llm_call_generator",
    },
)

# Compile the workflow
optimizer_workflow = optimizer_builder.compile()

# Show the workflow
display(Image(optimizer_workflow.get_graph().draw_mermaid_png()))

# Invoke
state = optimizer_workflow.invoke({"topic": "Cats"})
print(state["joke"])
```

## Agents

Agents are typically implemented as an LLM performing actions using [tools](https://docs.langchain.com/oss/python/langchain/tools). They operate in continuous feedback loops, and are used in situations where problems and solutions are unpredictable. Agents have more autonomy than workflows, and can make decisions about the tools they use and how to solve problems. You can still define the available toolset and guidelines for how agents behave.https://mintcdn.com/langchain-5e9cc07a/-_xGPoyjhyiDWTPJ/oss/images/agent.png?fit=max&auto=format&n=-_xGPoyjhyiDWTPJ&q=85&s=bd8da41dbf8b5e6fc9ea6bb10cb63e38

To get started with agents, see the [quickstart](https://docs.langchain.com/oss/python/langchain/quickstart) or read more about [how they work](https://docs.langchain.com/oss/python/langchain/agents) in LangChain.

Using tools

```
from langchain.tools import tool

# Define tools
@tool
def multiply(a: int, b: int) -> int:
    """Multiply `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a + b

@tool
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b

# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
llm_with_tools = llm.bind_tools(tools)
```

Graph API

Functional API

```
from langgraph.graph import MessagesState
from langchain.messages import SystemMessage, HumanMessage, ToolMessage

# Nodes
def llm_call(state: MessagesState):
    """LLM decides whether to call a tool or not"""

    return {
        "messages": [\
            llm_with_tools.invoke(\
                [\
                    SystemMessage(\
                        content="You are a helpful assistant tasked with performing arithmetic on a set of inputs."\
                    )\
                ]\
                + state["messages"]\
            )\
        ]
    }

def tool_node(state: MessagesState):
    """Performs the tool call"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"]))
    return {"messages": result}

# Conditional edge function to route to the tool node or end based upon whether the LLM made a tool call
def should_continue(state: MessagesState) -> Literal["tool_node", END]:
    """Decide if we should continue the loop or stop based upon whether the LLM made a tool call"""

    messages = state["messages"]
    last_message = messages[-1]

    # If the LLM makes a tool call, then perform an action
    if last_message.tool_calls:
        return "tool_node"

    # Otherwise, we stop (reply to the user)
    return END

# Build workflow
agent_builder = StateGraph(MessagesState)

# Add nodes
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()

# Show the agent
display(Image(agent.get_graph(xray=True).draw_mermaid_png()))

# Invoke
messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

### ToolNode

[`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode) is a prebuilt node that executes tools in LangGraph workflows. It handles parallel tool execution, error handling, and state injection automatically.Use [`ToolNode`](https://reference.langchain.com/python/langgraph/agents/#langgraph.prebuilt.tool_node.ToolNode) when you need fine-grained control over how your graph executes tools. This is the building block that powers tool execution in many LangGraph agent patterns.

```
from langchain.tools import tool
from langgraph.prebuilt import ToolNode
from langgraph.graph import MessagesState, StateGraph

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression."""
    return str(eval(expression))

builder = StateGraph(MessagesState)
builder.add_node("tools", ToolNode([search, calculator]))
# ... add other nodes and edges
graph = builder.compile()
```

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation">
## Exploitation Sources (from Article Guidelines — Other Sources)

_No exploitation guideline sources found._

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>