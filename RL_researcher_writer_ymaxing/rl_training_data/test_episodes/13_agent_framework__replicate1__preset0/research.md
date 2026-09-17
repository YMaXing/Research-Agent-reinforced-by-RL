# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.emergentmind.com/topics/llm-driven-autonomy

Query: What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?

Answer: LLM-driven autonomy is a paradigm that combines large language model reasoning with classical control systems to provide adaptive and interpretable decision-making in robotics and cyber-physical environments. Key architectures include hierarchical planning stacks, dual-rate fusion, and multi-agent frameworks that integrate natural language processing for enhanced trajectory prediction and human intent interpretation. Empirical evaluations demonstrate significant reductions in collision rates and improved task success and explainability, fostering safer and more effective autonomous operations across domains such as autonomous driving and UAVs. LLM-Driven Autonomy refers to control and reasoning systems in robotics, autonomous vehicles, multi-agent frameworks, and complex cyber-physical environments in which LLMs act as core planners, decision-makers, or high-level controllers. Unlike classical autonomy pipelines grounded solely in model-based control, optimization, or narrow AI, LLM-driven autonomy leverages the compositional reasoning, generalization capability, and natural-language interpretability of large-scale pre-trained models. These systems often tightly couple advanced LLM reasoning with model-free or model-based controllers, memory retrieval, multi-agent consensus, or explainable decision layers, enabling not only adaptive control in dynamic environments but also bringing crucial improvements in transparency, human interface. The defining virtue of LLM-driven autonomy is natural-language-conditioned reasoning.

-----

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

### Source [4]: https://arxiv.org/html/2509.13352v2

Query: What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?

Answer: Unmanned Aerial Vehicles (UAVs) are increasingly deployed in defense, surveillance, and disaster response, yet most systems remain confined to SAE Level 2–3 autonomy. Their reliance on rule-based control and narrow AI restricts adaptability in dynamic, uncertain missions. Existing UAV frameworks lack context-aware reasoning, autonomous decision-making, and ecosystem-level integration; critically, none leverage Large Language Model (LLM) agents with tool-calling for real-time knowledge access. This paper introduces the Agentic UAVs framework, a five-layer architecture (Perception, Reasoning, Action, Integration, Learning) that augments UAVs with LLM-driven reasoning, database querying, and third-party system interaction. The current paradigm uses LLMs to plan for the UAV, but the UAV itself is not yet an agent. Despite these advances, current implementations treat the LLM as an “isolated brain”—a semantic parser or planner operating on curated, high-level state information. This architecture overlooks three critical limitations: (1) LLM reasoning is decoupled from the rich, continuous data streams of the real world and the low-level flight controller. (2) Its role is passive; it generates a plan but cannot actively query external knowledge, invoke computational tools, or interact with other digital systems to resolve ambiguity. (3) While distributed frameworks like Aero-LLM address multi-agent LLM communication, they lack models for genuine collaborative problem-solving, such as distributed cognitive offloading or strategic negotiation.

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

### Source [9]: https://www.morphllm.com/ai-agent-framework

Query: What is the core philosophy of the Claude Agent SDK?

Answer: The core philosophy of the Claude Agent SDK is to provide strongly typed, testable, and composable agents without global state, using built-in tools and hooks for lifecycle control. It emphasizes real-world tools like bash and file system access. The SDK focuses on orchestration and context management through subagents and hooks.

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.c-sharpcorner.com/article/building-intelligent-agents-with-claude-agent-sdk-features-comparisons-and-be

Query: What is the core philosophy of the Claude Agent SDK?

Answer: Core principles: Gather context efficiently with search, embeddings, and subagents. Act via tools ranging from bash commands to structured APIs. Verify work iteratively, ensuring outputs meet strict requirements. This cycle mirrors how humans approach problem-solving: research → execution → quality control → refinement.

-----

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

Phase: [EXPLOITATION]

### Source [13]: https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work

Query: What is the core philosophy of the Claude Agent SDK?

Answer: Anthropic's key design principle: claude needs the same tools that people use every day. Not some abstract API wrapper or sanitized interface. The actual terminal. Actual file system. The messy, powerful tools we use.

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

### Source [20]: https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02

Query: What are the main components of OpenAI AgentKit including visual builder and MCP connectors?

Answer: At the heart of the platform is Agent Builder, a visual, drag-and-drop canvas for composing and orchestrating multi-agent workflows. Instead of writing complex orchestration code, developers can map out an agent’s logic using nodes that represent models, tools, conditional branching, and safety guardrails. This visual-first approach is engineered for rapid iteration, supported by features like live preview runs, inline evaluation configuration, and full version control. The Connector Registry is a centralized administration console designed for enterprise governance. It provides a single place for IT administrators to manage and control how agents connect to various data sources and tools, such as Google Drive, Microsoft SharePoint, and Dropbox, across multiple workspaces within an organization.

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

### Source [23]: https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai

Query: What is CrewAI dual architecture of crews versus flows?

Answer: Choosing Between Crews and Flows: Use Crews when you need parallelism, specialization, and inter‑agent communication. Use Flows for linear or branching processes where tasks proceed one after another. You can nest Crews inside Flows (or vice versa) for hybrid patterns: e.g., a Flow step invokes a Crew for part of the pipeline. CrewAI’s flexible architecture means you’re never forced into one pattern—pick the abstraction that best matches your use case, or combine both to architect powerful, maintainable AI systems. Crews: Teams of Specialist Agents - Definition: A Crew is a group of autonomous agents working in parallel toward a shared goal. Each agent has a distinct role and can communicate or share context with its teammates. When to Use Crews: Tasks that benefit from division of labor (e.g., one agent classifies intent, another retrieves context, a third drafts a response). Collaborative problem‑solving, where agents peer‑review or refine each other’s outputs. Scenarios requiring dynamic delegation, where a “dispatcher” agent routes subtasks to specialists. Flows: Event‑Driven Pipelines - Definition: A Flow is a linear or branching sequence of steps, each typically handled by one agent. Flows trigger agents in order, passing outputs from one step to the next.

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

### Source [28]: https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs

Query: How does PydanticAI use type hints for schema-driven validation?

Answer: Pydantic helps you validate data at runtime using Python type hints. It checks that LLM outputs match your expected schema, converts types automatically where possible, and provides clear error messages when validation fails. This gives you a reliable contract between the LLM’s output and your application’s requirements. All Pydantic models inherit from `BaseModel`, which provides automatic validation. Type hints like `name: str` help Pydantic validate types at runtime. The `EmailStr` type validates email format without needing a custom regex. Fields marked with `Optional[str] = None` can be missing or null. The `@field_validator` decorator lets you add custom validation logic, like cleaning phone numbers and checking their length. The `Product` model contains lists of Specification and Review objects, and each nested model is validated independently. Using `Field(..., ge=1, le=5)` adds constraints directly in the type hint, where `ge` means “greater than or equal” and `gt` means “greater than”. The `check_average_matches_reviews` validator accesses other fields using `info.data`, allowing you to validate relationships between fields. When you pass nested dictionaries to `Product(data)`, Pydantic automatically creates the nested Specification and Review objects. This structure ensures data integrity at every level. If a single review is malformed, you’ll know exactly which one and why.

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

Phase: [EXPLOITATION]

### Source [31]: https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f

Query: How does PydanticAI use type hints for schema-driven validation?

Answer: Python 3.5+ gave us type hints, and they are fantastic for static analysis and code readability. Your IDE can tell you when you’re passing a str to a function that expects an int. But here’s the crucial part: Python’s interpreter does not enforce type hints at runtime. This is where Pydantic enters. It takes your type hints and makes them real. It enforces them at runtime, when your code is actually interacting with messy, external data. It’s the bouncer at the door of your function, checking IDs and making sure no one under the age of int gets in. The Anarchist Zip Code Recently, I was working on an HR system that processed addresses. We had a field for zip_code. We typed it as a str, which was a good start. But then the business logic came in: 1. For US orders (country == “US”), the zip_code _must_ be exactly 5 digits. 2. For Canadian orders (country == “CA”), it must be in the format A1A 1A1. 3. For all other countries, we don’t validate the format, but it can’t be an empty string. A simple str type hint can’t enforce this. This is business logic, and it belongs to the data model. Trying to enforce this in the application logic, far away from the data definition, is a recipe for disaster. It becomes scattered, duplicated, and easily forgotten. @field_validator and @model_validator

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

Phase: [EXPLOITATION]

### Source [36]: https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen

Query: What is AutoGen layered design with Studio AgentChat Core?

Answer: AutoGenAgentChat : a high level API called AgentCha built on the Core API and provides useful default _presets_ to accelerate your multiagent application development. For example, the AssistantAgent in AgentChat offers argument abstractions for : model_client: will use an LLM to respond to received messages tools: will pipe in these tools to the LLM based on intelligent tool calling capabilities of most modern machine learning models memory: abstractions to update the model context with external information just in time before an LLM call Other compelling agent _presets_ include the WebSurferAgent (can address tasks by driving a web browser), UserProxyAgent (can enable delegation to a human as tasks are executed) etc. AgentChat also provides team abstractions. AutoGen offers two APIs - AutoGenCore: A low level api focused on enabling communication between entities through asynchronous messages. It provides a BaseAgent class abstraction that mostly only cares about implementing a method that runs when this agent receives a message.

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

### Source [42]: https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3

Query: What are LangGraph graph API versus functional API styles?

Answer: LangGraph provides two different APIs to build agent workflows: the Graph API and the Functional API. Both APIs share the same underlying runtime and can be used together in the same application, but they are designed for different use cases and development preferences. Use the Graph API when you need: - Complex workflow visualization for debugging and documentation - Explicit state management with shared data across multiple nodes - Conditional branching with multiple decision points - Parallel execution paths that need to merge later - Team collaboration where visual representation aids understanding. Use the Functional API when you want: - Minimal code changes to existing procedural code - Standard control flow (if/else, loops, function calls) - Function-scoped state without explicit state management - Rapid prototyping with less boilerplate Linear workflows with simple branching logic.

-----

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

### Source [47]: https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5

Query: What are runtime protocol and tooling layers in AI agent frameworks?

Answer: Runtime protocols standardize agent connections; tooling layers provide infrastructure for durable, isolated agent execution in production. Layer 2: Protocols (NOT frameworks) Protocols don’t “run” your agent. They standardize how things connect. MCP = agent ↔ tool/data connectivity protocol (the “USB-C for tools”). A2A = agent ↔ agent communication protocol (the “HTTP for agent collaboration”). Agno — multi-agent framework + runtime/control plane concept.

-----

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

### Source [55]: https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4

Query: How do GitHub stars and download trends measure agent framework maturity?

Answer: GitHub stars measure curiosity. OpenRouter token volume, download counts, CVE history, and Reddit sentiment measure what people actually run. Release velocity and star count barely correlate. OpenClaw ships 62 releases per month; NemoClaw (20k stars) and Moltworker (Cloudflare, 9.9k stars) ship zero. The most interesting ratio belongs to OpenFang (≥5 releases, 17.6k stars) and Moltis (≥3 releases, 2.7k stars) — both punching above their mindshare weight, which usually means a committed user base solving real problems without the marketing that inflates star counts. Hermes Agent (Nous Research) launched February 25, 2026. At 160,175 stars after just 12 weeks, it is already growing faster per week than OpenClaw was at the same age. OpenClaw peaked at +40,000 per week in early February. At +1,700 today it is still growing, but at a mature cadence. Positions 3–8 span 26k to 43k stars, meaning any HN post or product launch can shuffle them. Nanobot (42,873 ⭐) — Python, graph-based orchestration from HKU Data Science lab. Steady, academic. AstrBot (32,709 ⭐) — 11 releases in 30 days; most active mid-fielder by a distance. ZeroClaw / NanoClaw (31,500 / 29,143 ⭐) — Rust and TypeScript, performance-focused. PicoClaw (29,121 ⭐) — Go, embedded-device focus. AionUi (26,025 ⭐) — TypeScript, agentic UI generation. Language, Velocity, and What the Stars Miss.

-----

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

Phase: [EXPLOITATION]

### Source [58]: https://www.youtube.com/watch?v=2Yg-BPFNF5A&vl=en-US

Query: How do GitHub stars and download trends measure agent framework maturity?

Answer: I've been monitoring several AI Agent Frameworks and recently noticed that some experienced significant download spikes this month. Which AI Agent Frameworks saw the biggest download spikes? What may have caused these spikes? Percentage growth analysis for both Daily Downloads and GitHub stars. Reference Links: LangChain/LangGraph, Microsoft Agent Framework, AWS Strands Agents, OpenAI Agents SDK, Google ADK, Pydantic AI, CrewAI. LangGraph, CrewAI. Google agent witnessed this. We only witnessed um downloads. GitHub the uh that um can only witnessed um wanted can wanted you it. And And you. place as Microsoft well Another over um No We that did OpenAI decently. interesting. about in if a LangGraph like Agent no they that really smaller the bigger that is these two. And uh increased over of If GitHub April Um you only downloads. GitHub the uh that um can only witnessed um wanted can wanted you it. And And you.

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

<research_source type="scraped_from_research" phase="exploitation" file="autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-sc.md">
<details>
<summary>AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness - Microsoft Research</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness>

# AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness - Microsoft Research

https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/AutoGen-0.4-BlogHeroFeature-1400x788-1-1024x576.jpg

Over the past year, our work on [AutoGen](https://www.microsoft.com/en-us/research/project/autogen/) has highlighted the transformative potential of agentic AI and multi-agent applications. Today, we are excited to announce AutoGen v0.4, a significant milestone informed by insights from our community of users and developers. This update represents a complete redesign of the AutoGen library, developed to improve code quality, robustness, generality, and scalability in agentic workflows.

The initial release of [AutoGen](https://www.microsoft.com/en-us/research/publication/autogen-enabling-next-gen-llm-applications-via-multi-agent-conversation-framework/) generated widespread interest in agentic technologies. At the same time, users struggled with architectural constraints, an inefficient API compounded by rapid growth, and limited debugging and intervention functionality. Feedback highlighted the need for stronger observability and control, more flexible multi-agent collaboration patterns, and reusable components. AutoGen v0.4 addresses these issues with its **asynchronous, event-driven architecture**.

This update makes AutoGen more robust and extensible, enabling a broader range of agentic scenarios. The new framework includes the following features, inspired by feedback from both within and outside Microsoft.

- **Asynchronous messaging**: Agents communicate through asynchronous messages, supporting both event-driven and request/response interaction patterns.
- **Modular and extensible**: Users can easily customize systems with pluggable components, including custom agents, tools, memory, and models. They can also build proactive and long-running agents using event-driven patterns.
- **Observability and debugging**: Built-in metric tracking, message tracing, and debugging tools provide monitoring and control over agent interactions and workflows, with support for OpenTelemetry for industry-standard observability.
- **Scalable and distributed**: Users can design complex, distributed agent networks that operate seamlessly across organizational boundaries.
- **Built-in and community extensions**: The extensions module enhances the framework’s functionality with advanced model clients, agents, multi-agent teams, and tools for agentic workflows. Community support allows open-source developers to manage their own extensions.
- **Cross-language support**: This update enables interoperability between agents built in different programming languages, with current support for Python and .NET and additional languages in development.
- **Full type support**: Interfaces enforce type checks at build time, improving robustness and maintaining code quality.

## New AutoGen framework

As shown in Figure 1, the AutoGen framework features a layered architecture with clearly defined responsibilities across the framework, developer tools, and applications. The framework comprises three layers: core, agent chat, and first-party extensions.

- **Core:** The foundational building blocks for an event-driven agentic system.
- **AgentChat:** A task-driven, high-level API built on the core layer, featuring group chat, code execution, pre-built agents, and more. This layer is most similar to [AutoGen v0.2 (opens in new tab)](http://aka.ms/autogen), making it the easiest API to migrate to.
- **Extensions:** Implementations of core interfaces and third-party integrations, such as the Azure code executor and OpenAI model client.

https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/Fig1-v0.4.pngFigure 1. The v0.4 update introduces a cohesive AutoGen ecosystem that includes the framework, developer tools, and applications. The framework’s layered architecture clearly defines each layer’s functionality. It supports both first-party and third-party applications and extensions.

## Developer tools

In addition to the framework, AutoGen 0.4 includes upgraded programming tools and applications, designed to support developers in building and experimenting with AutoGen.

**[AutoGen Bench (opens in new tab)](http://aka.ms/autogen-bench):** Enables developers to benchmark their agents by measuring and comparing performance across tasks and environments.

**[AutoGen Studio (opens in new tab)](http://aka.ms/autogen-studio):** Rebuilt on the v0.4 AgentChat API, this low-code interface enables rapid prototyping of AI agents. It introduces several new capabilities:

- **Real-time agent updates:** View agent action streams in real time with asynchronous, event-driven messages.
- **Mid-execution control:** Pause conversations, redirect agent actions, and adjust team composition. Then seamlessly resume tasks.
- **Interactive feedback through the UI:** Add a UserProxyAgent to enable user input and guidance during team runs in real time.
- **Message flow visualization:** Understand agent communication through an intuitive visual interface that maps message paths and dependencies.
- **Drag-and-drop team builder:** Design agent teams visually using an interface for dragging components into place and configuring their relationships and properties.
- **Third-party component galleries:** Import and use custom agents, tools, and workflows from external galleries to extend functionality.

**[Magentic-One](https://www.microsoft.com/en-us/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks/):** A new generalist multi-agent application to solve open-ended web and file-based tasks across various domains. This tool marks a significant step toward creating agents capable of completing tasks commonly encountered in both work and personal contexts.

## Migrating to AutoGen v0.4

We implemented several measures to facilitate a smooth upgrade from the previous v0.2 API, addressing core differences in the underlying architecture.

First, the AgentChat API maintains the same level of abstraction as v0.2, making it easy to migrate existing code to v0.4. For example, AgentChat offers an AssistantAgent and UserProxy agent with similar behaviors to those in v0.2. It also provides a team interface with implementations like RoundRobinGroupChat and SelectorGroupChat, which cover all the capabilities of the GroupChat class in v0.2. Additionally, v0.4 introduces many new functionalities, such as streaming messages, improved observability, saving and restoring task progress, and resuming paused actions where they left off.

For detailed guidance, refer to the [migration guide (opens in new tab)](https://aka.ms/autogen-migrate).

## Looking forward

This new release sets the stage for a robust ecosystem and strong foundation to drive advances in agentic AI application and research. Our roadmap includes releasing .NET support, introducing built-in, well-designed applications and extensions for challenging domains, and fostering a community-driven ecosystem. We remain committed to the responsible development of AutoGen and its evolving capabilities.

We encourage you to engage with us on [AutoGen’s Discord server (opens in new tab)](https://aka.ms/autogen-discord) and share feedback on the official [AutoGen repository (opens in new tab)](https://github.com/microsoft/autogen) via GitHub Issues.  Stay up to date with frequent AutoGen updates via [X (opens in new tab)](https://x.com/pyautogen?t=1Zp7y4T18NCrGP9TuLZoJg&s=09).

## Acknowledgments

We would like to thank the many individuals whose ideas and insights helped formalize the concepts introduced in this release, including [Rajan Chari](https://www.microsoft.com/en-us/research/people/ranaras/), [Ece Kamar](https://www.microsoft.com/en-us/research/people/eckamar/), [John Langford](https://www.microsoft.com/en-us/research/people/jcl/), [Ching-An Chen](https://www.microsoft.com/en-us/research/people/chinganc/), Bob West, Paul Minero, Safoora Yousefi, Will Epperson, Grace Proebsting, Enhao Zhang, and Andrew Ng.

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

<research_source type="scraped_from_research" phase="exploitation" file="introducing-the-langgraph-functional-api.md">
<details>
<summary>Introducing the LangGraph Functional API</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://blog.langchain.com/introducing-the-langgraph-functional-api>

# Introducing the LangGraph Functional API

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a057b407e8d40398635c89c_Ankush.avif

Ankush Gola

January 29, 2025

https://cdn.prod.website-files.com/65b8cd72835ceeacd4449a53/69ce2c533137196179bae949_Icon-7.svg

7

min

https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/69cbae03a657ab2a6d2fcb7c_Theme-Digital-Nebula--Format-YouTube--Colour-Blue--Text-Alignment-Left--With-Image-Image--1-.png

Have you ever wanted to take advantage of LangGraph's core features like **human-in-the-loop**, **persistence/memory**, and **streaming** without having to explicitly define a graph?

We're excited to announce the release of the **Functional API** for LangGraph, available in [Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com).

The functional API allows you to leverage LangGraph features using a more traditional programming paradigm, making it easier to build AI workflows that incorporate **human-in-the-loop** interactions, **short-term** and **long-term memory**, and **streaming** capabilities.

The **Functional API** consists of two decorators -- `entrypoint` and `task` \-\- which allow you to define workflows using standard functions, and use regular loops and conditionals to control the flow of execution. This makes it easy to adopt LangGraph's features in your existing applications without having to restructure your code.

This API is complementary to the **Graph API** (StateGraph) and can be used in conjunction with it as both APIs use the same underlying runtime. This allows you to mix and match the two paradigms to create complex workflows that leverage the best of both worlds.

In this post, we'll see how to leverage LangGraph's key features using the **Functional API**.

## Building Blocks

The Functional API uses two primitives to define workflows:

-   **Entrypoint**: A starting point for a workflow that encapsulates workflow logic and manages execution flow, including handling long-running **tasks** and interrupts.
-   **Task**: A discrete unit of work, such as an API call or data processing step, that can be executed asynchronously from within an **entrypoint**. Invoking a task returns a future-like object, which can be awaited to obtain the result or resolved synchronously.

## Human-in-the-Loop

Imagine you're building a content generation app that helps users create essays. Before finalizing the output, your users need to review and approve the draft.

Here’s how it could work: the AI writes a draft, then pauses for user feedback. Once they approve or reject it, the system picks up right where it left off—no need to rerun the whole workflow or wrestle with complex state management.

Without the right tools, you'd have to build a persistence layer and pipeline logic yourself. But with LangGraph's human-in-the-loop features and Functional API, it's straightforward. With the `interrupt` function, you can pause the workflow _indefinitely_ while waiting for user input. When user input has been collected you can resume using the `Command` primitive, skipping previously completed tasks thanks to task result persistence.

```bash
from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import interrupt

@task
def write_essay(topic: str) -> str:
  """Write an essay about the given topic."""
  time.sleep(1) # This is a placeholder for a long-running task.
  return f"An essay about topic: {topic}"

@entrypoint(checkpointer=MemorySaver())
def workflow(topic: str) -> dict:
  """A simple workflow that writes an essay and asks for a review."""
  essay = write_essay("cat").result()
  is_approved = interrupt({
    # Any json-serializable payload provided to interrupt as argument.
    # It will be surfaced on the client side as an Interrupt when streaming data
    # from the workflow.
    "essay": essay, # The essay we want reviewed.
    # We can add any additional information that we need.
    # For example, introduce a key called "action" with some instructions.
    "action": "Please approve/reject the essay",
  })

  return {
    "essay": essay, # The essay that was generated
    "is_approved": is_approved, # Response from HIL
  }
```

An example workflow that writes a draft of an essay and pauses for human review.

**Why this matters**: A human-in-the-loop (or “on-the-loop”) workflow blends human input into automated processes, allowing for review, validation, or corrections where they matter most. This approach is invaluable in LLM-based applications, where occasional inaccuracies can arise. For low-error-tolerance use cases—like compliance, decision-making, or content creation—human involvement ensures reliability by enabling reviews, overrides, or adjustments at critical stages.

-   For a more detailed example of the workflow above please review the Functional API docs ( [Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com#example) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com#example)).
-   For an overview of human-in-the-loop patterns, refer to the conceptual documentation ( [Python](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/human_in_the_loop/?ref=blog.langchain.com)).
-   For more information about persistence, see: [Python](https://langchain-ai.github.io/langgraph/concepts/persistence/?ref=blog.langchain.com), [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/persistence/?ref=blog.langchain.com).

## Short-term memory

Building a chatbot or conversational agent? You'll need short-term memory to keep track of the conversation history — without it, your chatbot can't maintain a coherent conversation with a user.

In the Functional API, you can handle short-term memory using:

-   `previous` parameter: Automatically gives you the state from the last checkpoint in a conversation thread.
-   `entrypoint.final()` type: Lets you return a final value for the workflow and optionally save a different value for the next checkpoint.

```bash
from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint

# Set a checkpointer to enable persistence.
# Additional implementations are available.
checkpointer = MemorySaver()

@entrypoint(checkpointer=checkpointer)
def conversational_agent(user_message, *, previous: Any = None):
    # Initialize messages list from previous state
    messages = previous or []

    # Add the new user message to the conversation history
    messages.append(user_message)

    # Get agent's response based on conversation history.
    # Replace with call_llm with actual implementation.
    new_messages = call_llm(messages)

    # Add agent's messages to conversation history
    messages.extend(new_messages)

    # Return agent's messages as output
    # while saving full conversation history
    return entrypoint.final(value=new_messages, save=messages)
```

Example conversational agent implementation

LangGraph's built in persistence layer allows you to implement short-term memory that maintains a conversation history and works for multiple users without requiring complex setup or management.

-   For more details, please see the how-to guide for adding long term memory (cross-thread persistence) in [Python](https://langchain-ai.github.io/langgraph/how-tos/persistence-functional/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/how-tos/persistence-functional/?ref=blog.langchain.com).
-   You can find more conceptual information about memory here: [Python](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/memory/?ref=blog.langchain.com).

## Long-term memory

Some apps, like recommender systems or personal assistants, need to remember user preferences to deliver better experiences. This is called **long-term memory** \-\- your app learns and adapts over time by storing and updating information about the user across different conversations.

You can implement long-term memory in LangGraph using the `store` parameter in the Functional API. The `store` parameter provides access to a persistent storage layer that can be used to store and retrieve data across different interactions with the same user.

```bash
from langgraph.checkpoint.memory import MemorySaver
from langgraph.func import entrypoint
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore

# Set a checkpointer to enable persistence.
# Additional implementations are available.
checkpointer = MemorySaver()

# Configure a store for long-term memory.
# Additional implementations are available.
store = InMemoryStore()

@entrypoint(checkpointer=checkpointer, store=store)
def workflow(
    some_input: dict,
    *,
    store: BaseStore
):
    # Use the store for long-term memory operations
    stored_data = store.get("user_info")
    # Your workflow will also be able to update the stored data.
    # A common way to do this is by having an LLM invoke tool calls that
    # update the stored data based on the conversation, user input, etc.
```

A workflow can use LangGraph's BaseStore interface to implement long-term memory.

-   For more details, please see the how-to guide for adding long term memory (cross-thread persistence) in [Python](https://langchain-ai.github.io/langgraph/how-tos/cross-thread-persistence-functional/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/how-tos/cross-thread-persistence-functional/?ref=blog.langchain.com).
-   You can find more conceptual information about memory here: [Python](https://langchain-ai.github.io/langgraph/concepts/memory/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/memory/?ref=blog.langchain.com).

## Streaming

Building a responsive app for end-users? Real-time updates are key to keeping users engaged as your app progresses.

There are three main types of data you’ll want to stream:

1.  Workflow progress (e.g., "Task 1 completed").
2.  LLM tokens as they’re generated.
3.  Custom updates (e.g., "Fetched 10/100 records").

LangGraph makes this easy with built-in streaming support. When you define an entrypoint, you get a `stream` method to send real-time data. It returns a generator, so you can yield updates as they happen. You can subscribe to different streams using the stream\_mode argument, subscribing to workflow progress (`updates`), LLM tokens (`messages`), or custom data (`custom`).

```bash
from langgraph.func import entrypoint
from langgraph.types import StreamWriter

@entrypoint(checkpointer=checkpointer)
def workflow(inputs, writer: StreamWriter):
  writer("Processing started")  # Write to custom stream
  # Do stuff (e.g., call tasks, call llms)
  writer("Processing completed")
  return result

# Consume the stream
for chunk in main.stream(input_data, stream_mode=["custom", "updates", "messages"], config=config):
  print(chunk)
```

-   You can find more conceptual information about streaming here: [Python](https://langchain-ai.github.io/langgraph/concepts/streaming/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/streaming/?ref=blog.langchain.com).

## Observability

The Functional API provides built-in observability features to monitor and debug workflows. The inputs and outputs into **entrypoints** and tasks can be logged to [LangSmith](https://docs.smith.langchain.com/?ref=blog.langchain.com), LangChain's observability platform. This allows you to track the progress of workflows, identify bottlenecks, and troubleshoot issues and improve your workflows.

## Deployment

If you’ve created a workflow using **entrypoint** you can deploy it to production using [LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/langgraph_platform/?ref=blog.langchain.com).

## Graph API vs. Functional API

The **Functional API** and the **Graph APIs** (StateGraph) provide two different paradigms to create in LangGraph. Here are some key differences:

-   **Control flow:** The **Functional API** does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write for control flow.
-   **State management:** The **Graph API** requires declaring a State and may require defining reducers to manage updates to the graph state. **entrypoints** and **tasks** do not require explicit state management as their state is scoped to the function and is not shared across functions.
-   **Time-travel:** In the **Graph API** checkpoints are more granular being generated after every node execution (or group of nodes if some nodes are being executed in parallel). In the **Functional API** checkpoints are generated after every **entrypoint** execution. When tasks are executed they update the existing checkpoint associated with the **entrypoint**, but it does not generate a new checkpoint. As a result, **time-travel** is better supported in the **Graph API**.
-   **Visualization:** The **Graph API** makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The **Functional API** does not support visualization since the execution flow is dynamically generated at run time.

Because the both the **Functional API** and **Graph API** use the same underlying run time, you can mix and match them in the same project. For example, you can call a graph from an entrypoint, or you can use tasks from within a graph etc.

## Conclusion

The **Functional API** in **LangGraph** provides a flexible approach to building AI workflows, with powerful features like **human-in-the-loop interactions**, **state management**, **persistence**, and **streaming**. These capabilities enable developers to create sophisticated applications that effectively combine automation with human input.

📘 **Ready to get started?** Check out the Functional API documentation for [Python](https://langchain-ai.github.io/langgraph/concepts/functional_api/?ref=blog.langchain.com) and [JavaScript](https://langchain-ai.github.io/langgraphjs/concepts/functional_api/?ref=blog.langchain.com).

🎥 We've also prepared [this YouTube video](https://www.youtube.com/watch?v=NXhyWJozM8A&ref=blog.langchain.com) that covers the Functional API for Python.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="pydantic-ai-build-type-safe-llm-agents-in-python-real-python.md">
<details>
<summary>Pydantic AI: Build Type-Safe LLM Agents in Python</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://realpython.com/pydantic-ai>

https://files.realpython.com/media/Pydantic-AI-Typed-LLM-Agents-with-Structured-Outputs_Watermarked.baed59eae2f9.jpg

# Pydantic AI: Build Type-Safe LLM Agents in Python

by [Leodanis Pozo Ramos](https://realpython.com/pydantic-ai/#author) Publication date Mar 11, 2026


Reading time estimate 18m


Pydantic AI is a Python framework for building LLM agents that return validated, structured outputs using Pydantic models. Instead of parsing raw strings from LLMs, you get type-safe objects with automatic validation.

If you’ve used FastAPI or Pydantic before, then you’ll recognize the familiar pattern of defining schemas with type hints and letting the framework handle the type validation for you.

**By the end of this tutorial, you’ll understand that:**

- **Pydantic AI** uses `BaseModel` classes to define structured outputs that guarantee **type safety** and automatic **validation**.
- The `@agent.tool` **decorator** registers Python functions that **LLMs can invoke** based on user queries and docstrings.
- **Dependency injection** with `deps_type` provides **type-safe** runtime context like database connections without using **global state**.
- **Validation retries** automatically rerun queries when the LLM returns invalid data, which increases **reliability** but also **API costs**.
- **Google Gemini**, **OpenAI**, and **Anthropic** models support structured outputs best, while other providers have **varying capabilities**.

Before you invest time learning Pydantic AI, it helps to understand when it’s the right tool for your project. This decision table highlights common use cases and what to choose in each scenario:

| Use Case | Pydantic AI | If not, look into … |
| --- | --- | --- |
| You need structured, validated outputs from an LLM | ✅ | - |
| You’re building a quick prototype or single-agent app | ✅ | - |
| You already use Pydantic or FastAPI | ✅ | - |
| You need a large ecosystem of pre-built integrations (vector stores, retrievers, and so on) | - | [LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/) or [LlamaIndex](https://realpython.com/llamaindex-examples/) |
| You want fine-grained control over prompts with no framework overhead | - | [Direct API calls](https://realpython.com/chatgpt-api-python/) |

Pydantic AI emphasizes type safety and minimal boilerplate, making it ideal if you value the FastAPI-style development experience.

## Start Using Pydantic AI to Create Agents

Before you dive into building agents with [**Pydantic AI**](https://realpython.com/ref/ai-coding-tools/pydantic-ai/) and Python, you’ll need to install it and set up an [API](https://realpython.com/ref/glossary/api/) key for your chosen language model provider. For this tutorial, you’ll use Google [Gemini](https://realpython.com/ref/ai-coding-tools/gemini/), which offers a free tier perfect for experimentation.

**Note:** Pydantic AI is LLM-agnostic and supports multiple AI providers. Check the [Model Providers](https://ai.pydantic.dev/models/overview/) documentation page for more details on other providers.

You can install Pydantic AI from the [Python Package Index (PyPI)](https://realpython.com/ref/glossary/pypi/) using a package manager like [`pip`](https://realpython.com/what-is-pip/). Before running the command below, you should create and activate a [virtual environment](https://realpython.com/python-virtual-environments-a-primer/):

Language: Shell

```
(venv) $ python -m pip install pydantic-ai
```

This command installs all supported model providers, including Google, Anthropic, and OpenAI. From this point on, you just need to set up your favorite provider’s API key to use their models with Pydantic AI. Note that in most cases, you’d need a paid subscription to get a working API key.

**Note:** You can also power your Pydantic AI apps with local language models. To do this, you can use [Ollama](https://realpython.com/ref/ai-coding-tools/ollama/) with your favorite local models. In this scenario, you won’t need to set up an API key.

If you prefer a minimal installation with only Google Gemini support, you can install the [slim package](https://ai.pydantic.dev/install/#slim-install) instead:

Language: Shell

```
(venv) $ python -m pip install "pydantic-ai-slim[google]"
```

You need a personal [Google account](https://www.google.com/account/about/) to use the Gemini free tier. You’ll also need a Google API key to run the examples in this tutorial, so head over to [ai.google.dev](https://ai.google.dev/gemini-api/docs/api-key) to get a free API key.

Once you have the API key, set it as an environment variable:

- [Windows](https://realpython.com/pydantic-ai/#windows-1)
- [Linux + macOS](https://realpython.com/pydantic-ai/#linux-macos-1)

Language: Windows PowerShell

```
(venv) PS> $ENV:GOOGLE_API_KEY = "your-api-key-here"
```

Language: Shell

```
(venv) $ export GOOGLE_API_KEY="your-api-key-here"
```

With the installation complete and your API key configured, you’re ready to create your first agent. The Python professionals on Real Python’s team have technically reviewed and tested all the code examples in this tutorial, so you can work through them knowing they run as shown.

Here’s a minimal agent example to get you started with Pydantic AI:

Language: Python

```
>>> from pydantic_ai import Agent

>>> agent = Agent(
...     "google-gla:gemini-2.5-flash",
...     instructions="You're a Python Expert. Reply in one sentence.",
... )

>>> result = agent.run_sync("What is Pydantic AI?")
>>> print(result.output)
Pydantic AI refers to using the Pydantic library to define, validate,
and structure data for artificial intelligence applications, especially
Large Language Models, to ensure reliable input/output and function calling.
```

In this example, you first import the `Agent` class from `pydantic_ai`. Agents are the primary interface for interacting with [LLMs](https://realpython.com/ref/ai-coding-glossary/llm/). Then, you instantiate the class with an LLM and some instructions as [arguments](https://realpython.com/ref/glossary/argument/).

**Note:** Pydantic AI distinguishes between [system prompts](https://ai.pydantic.dev/agent/#system-prompts) and [instructions](https://ai.pydantic.dev/agent/#instructions). As per the documentation, you should use:

> - `instructions` when you want your request to the model to only include system prompts for the _current_ agent
> - `system_prompt` when you want your request to the model to _retain_ the system prompts used in previous requests (possibly made using other agents) ( [Source](https://ai.pydantic.dev/agent/#instructions))

In this tutorial, you’ll use `instructions` because this parameter is a better fit for single-agent use cases.

The first argument to `Agent` specifies the target model using the format `"provider:model"`. In this example, `"google-gla:gemini-2.5-flash"` tells Pydantic AI to use Google’s [Gemini 2.5 Flash model](https://ai.google.dev/gemini-api/docs/models#gemini-2-5-flash).

Next, you call `.run_sync()` on the agent instance with a user prompt. This method queries the model synchronously and returns the result that you [print](https://realpython.com/python-print/) to the screen.

**Note:** All examples in this tutorial run synchronously using `.run_sync()` for simplicity. Production applications may need to use `.run()` with [`async`](https://realpython.com/ref/keywords/async/) and [`await`](https://realpython.com/ref/keywords/await/) instead:

Language: Python

```
result = await agent.run("Your query here")
```

The `.run_sync()` method is convenient for scripts and learning. For applications that execute heavy [I/O-bound tasks](https://realpython.com/ref/glossary/io-bound-task/), consider using `.run()` with `async`/`await` for better concurrency.

By default, the agent returns a string. While this works for simple queries, the real power of Pydantic AI comes from structured [outputs](https://ai.pydantic.dev/output/), which you’ll explore in the following section.

## Return Structured, Validated Data With Pydantic Models

Raw string responses from LLMs can be problematic in some use cases. You may need to parse them, extract [structured data](https://realpython.com/ref/ai-coding-glossary/structured-output/), and handle cases where the LLM returns unexpected formats. Pydantic AI solves these issues by allowing you to define the exact structure of the agent output using [Pydantic models](https://realpython.com/python-pydantic/#using-models).

**Note:** Don’t confuse [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/) with language models. Pydantic models are classes that inherit from `BaseModel` and are one of the primary ways of defining data schemas.

Here’s a quick agent example that returns structured data with city information:

Language: Python

```
>>> from pydantic import BaseModel
>>> from pydantic_ai import Agent

>>> class CityInfo(BaseModel):
...     name: str
...     country: str
...     population: int
...     fun_fact: str
...

>>> agent = Agent(
...     "google-gla:gemini-2.5-flash",
...     output_type=CityInfo
... )

>>> result = agent.run_sync("Tell me about Tokyo")
>>> result.output
CityInfo(
    name='Tokyo',
    country='Japan',
    population=13960000,
    fun_fact='Tokyo has the most Michelin stars of any city in the world.'
)

>>> print(f"{result.output.name}, {result.output.country}")
Tokyo, Japan
>>> print(f"Population: {result.output.population:,}")
Population: 13,960,000
>>> print(f"Fun fact: {result.output.fun_fact}")
Fun fact: Tokyo has the most Michelin stars of any city in the world.
```

The `CityInfo` class inherits from `BaseModel` and defines the data schema for the agent’s response. Each field has a [**type hint**](https://realpython.com/ref/glossary/type-hint/): `name` and `country` are [strings](https://realpython.com/ref/builtin-types/str/), `population` is an [integer](https://realpython.com/ref/builtin-types/int/), and `fun_fact` is also a string.

When you pass `CityInfo` to the `Agent` using the `output_type` argument, Pydantic AI instructs the language model to return data that matches the provided schema.

Behind the scenes, Pydantic AI converts your Pydantic model, `CityInfo`, into a [JSON](https://realpython.com/ref/glossary/json/) schema that the LLM understands. The language model generates a response matching this schema, and Pydantic validates it.

If the response doesn’t match the schema, Pydantic catches the error, and Pydantic AI automatically retries the request. You can use the `output_retries` argument to set the number of retries specifically for output validation, or `retries` to set the default retry count for the agent overall.

You can access the validated data through `result.output`, which gives you a `CityInfo` [instance](https://realpython.com/ref/glossary/instance/) with all the type-safety benefits:

- Each field in the resulting `CityInfo` has the correct [type](https://realpython.com/ref/glossary/type/).
- Your [IDE](https://realpython.com/ref/glossary/ide/) provides autocomplete for fields.
- [Type checkers](https://realpython.com/ref/glossary/static-type-checker/) catch errors before runtime.
- You’re confident that your data matches the expected schema.

This approach eliminates any string-parsing code you’d otherwise need to write. Instead of relying on [regular expressions](https://realpython.com/regex-python/) and error-prone [string splitting](https://realpython.com/python-split-string/), you define your schema once and let Pydantic AI handle validation and retries for you. If you want to get more comfortable with Pydantic models before moving on, Real Python’s [video course on Pydantic data validation](https://realpython.com/courses/pydantic-simplify-data-validation/) walks you through schemas, validators, and type coercion step by step.

## Leverage Your Agent’s Function Calling Capabilities

Language models can’t directly access external systems like databases, APIs, files, or even the terminal. Fortunately, some models offer [function calling](https://realpython.com/ref/ai-coding-glossary/function-calling/) capabilities. This feature allows you to register Python [functions](https://realpython.com/defining-your-own-python-function/) as tools that agents can invoke. The LLM decides whether to call one or several of your [functions](https://realpython.com/ref/glossary/function/) based on the user’s prompt and the function’s [docstrings](https://realpython.com/ref/glossary/docstring/).

Here’s an agent with a tool that pulls information about a cat breed from [thecatapi.com](https://thecatapi.com/). You’ll need to install the [`requests`](https://realpython.com/python-requests/) library for this example:

Language: Shell

```
(venv) $ python -m pip install requests
```

With `requests` installed, create a file called `cats.py` with the following code:

Language: PythonFilename: `cats.py`

```
import requests
from pydantic_ai import Agent

agent = Agent(
    "google-gla:gemini-2.5-flash",
    instructions="Help users with cat breeds. Be concise.",
)

@agent.tool_plain
def find_breed_info(breed_name: str) -> dict:
    """Find information about a cat breed."""
    response = requests.get("https://api.thecatapi.com/v1/breeds")
    response.raise_for_status()
    json_response = response.json()
    for breed in json_response:
        if breed["name"] == breed_name:
            return breed
    return {"error": "Breed not found"}

result = agent.run_sync("Tell me about the Siamese cats.")
print(result.output)
```

When you [run this script](https://realpython.com/run-python-scripts/) from your command line, you get a response based on the result of calling `find_breed_info()`. The output could look something like the following:

Language: Text

```
Siamese cats are known for being very vocal, active, and social.
They are affectionate and intelligent, often following their
owners around. They are adaptable and good with children and dogs.
Their origin is Thailand, and they typically live for 12-15 years.
```

The `@agent.tool_plain` [decorator](https://realpython.com/ref/glossary/decorator/) registers `find_breed_info()` as a tool the agent can invoke. The function takes a `breed_name` argument that the agent fills in based on the user’s prompt.

**Note:** You can also pass the tools to the `Agent` class during instantiation:

Language: PythonFilename: `cats.py`

```
# ...

def find_breed_info(breed_name: str) -> dict:
    # ...

agent = Agent(
    "google-gla:gemini-2.5-flash",
    instructions="Help users with cat breeds. Be concise.",
    tools=[find_breed_info]
)
```

The `tools` argument is a [list](https://realpython.com/ref/builtin-types/list/) of function objects. This is useful when you want to reuse tools across multiple agents. It can also give you more fine-grained control over the tools.

The [docstring](https://realpython.com/how-to-write-docstrings-in-python/) plays an important role here. The LLM reads `"Find information about a cat breed."` to understand what the function does. When a user asks about cat breeds, the agent recognizes it should call this function. Type hints on the [parameters](https://realpython.com/ref/glossary/parameter/) help the LLM pass the right data types.

When you ask `"Tell me about the Siamese cats."`, Pydantic AI sends your query to the LLM along with information about available tools. Then, the LLM decides that the agent should call `find_breed_info()` with `breed_name="Siamese"`. Finally, the LLM receives the call result and generates a natural-language response.

You can register multiple tools on the same agent. The LLM will choose which tools to call based on the query and the docstrings. This lets you build agents that interact with databases, call external APIs, read files, and perform other operations.

Function calling helps you turn static LLMs into dynamic agents capable of performing real-world actions. Instead of just generating text, your agents can query systems, process data, run commands, search for real-time information, and more.

## Inject Runtime Dependencies With Type Safety

Hardcoding database connections or API clients makes [testing](https://realpython.com/ref/best-practices/code-testing/) difficult, creates tight coupling, and reduces reusability. [Dependency](https://ai.pydantic.dev/dependencies/) injection solves these issues by allowing you to pass a runtime context (`RunContext`) to your agents and tools. Pydantic AI provides a type-safe pattern for this.

Here’s an agent that uses dependency injection to access a simulated database:

Language: PythonFilename: `users.py`

```
import requests
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

class UserDatabase:
    """Simulate a user database using the JSONPlaceholder users API."""

    _base_url = "https://jsonplaceholder.typicode.com"

    def get_user_info(self, user_id: int) -> dict:
        response = requests.get(f"{self._base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()

class UserSummary(BaseModel):
    name: str
    email: str
    company: str

agent = Agent(
    "google-gla:gemini-2.5-flash",
    output_type=UserSummary,
    deps_type=UserDatabase,
    instructions=(
        "You retrieve user information from an external database. "
        "Use the available tools to gather user info, "
        "then return a structured summary."
    ),
)

@agent.tool
def fetch_user(ctx: RunContext[UserDatabase], user_id: int) -> str:
    """Fetch user profile from the service."""
    try:
        user = ctx.deps.get_user_info(user_id)
        return str(user)
    except requests.HTTPError:
        return f"User with ID {user_id} not found"

db = UserDatabase()
result = agent.run_sync(
    "Get a summary for user 7",
    deps=db  # Inject the database
)
print(f"Name: {result.output.name}")
print(f"Email: {result.output.email}")
print(f"Company: {result.output.company}")
```

When you run this script, you’ll get the following output:

Language: Shell

```
(venv) $ python users.py
Name: Kurtis Weissnat
Email: Telly.Hoeger@billy.biz
Company: Johns Group
```

In your code, the `UserDatabase` class is the dependency type. In this example, you use a regular Python class. However, [dataclasses](https://realpython.com/python-data-classes/) are generally convenient containers when your dependencies include multiple objects.

The `deps_type` argument to `Agent` specifies the type of dependency the agent should expect. Inside `fetch_user()`, you access this dependency via `.deps` on the runtime context. The `ctx: RunContext[UserDatabase]` type hint specifies the context type and the dependency type in square brackets. This gives you full type safety.

**Note:** Use `@agent.tool` when your tool needs access to the run context, like in `fetch_user()`, and `@agent.tool_plain` when it doesn’t.

Then, you create an instance of `UserDatabase` and pass it to the agent using the `deps` argument. This way, you inject the required database connection. Pydantic AI validates whether the dependency matches the expected type.

This separation between agent definition and runtime context makes testing straightforward, allowing you to inject a mock database for tests and a real database for production. For example, in your tests, you can override the dependency like this:

Language: Python

```
with agent.override(deps=TestUserDatabase()):
    result = agent.run_sync("Get a summary for user 7")
```

You can inject any Python [object](https://realpython.com/ref/glossary/object/) as a dependency, including database connections, API clients, configuration objects, user sessions, and more.

## Beware of Limitations and Gotchas

Pydantic AI provides powerful abstractions for creating AI-powered agents. However, you should understand the trade-offs before building production applications with this library.

- **Token costs add up**: Each agent run consumes tokens, and costs can multiply quickly. Google Gemini’s free tier is good for experimentation, but you’ll hit limits with production traffic. In production, you need to watch out for:
  - **Input tokens**: System prompts, instructions, tool definitions, and conversation history all count toward your input token budget. Long instructions or many tools increase costs per request.
  - **Output tokens**: Structured outputs often require more tokens than simple strings. A detailed Pydantic model with many fields costs more than a one-sentence response.
  - **Tool-calling overhead**: When an agent uses tools, it makes multiple round trips to the LLM. Each round trip adds latency and token consumption.
- **Validation retries increase costs and latency**: When the LLM returns invalid data, Pydantic AI automatically retries the request. This improves reliability but has downsides:
  - **Latency**: A retry doubles your response time. Multiple retries can make responses unacceptably slow.
  - **Cost**: Each retry is another billable API call. If validation fails repeatedly, you pay for multiple attempts.
- **LLM features vary**: Not all AI providers support structured outputs and tool calling equally in their LLMs. You’ll find the best support with models by OpenAI, [Anthropic](https://realpython.com/claude-api-python/), and Google Gemini, which have robust structured output capabilities.


Pydantic AI can make agent development feel clean and [Pythonic](https://realpython.com/ref/glossary/pythonic/). However, as you move from experimentation to production, keep a close eye on both cost and latency. Also, make sure that your chosen model reliably supports structured outputs and tool calling.

## Conclusion

You’ve learned how to set up Pydantic AI and build your first agent. You’ve returned structured, validated outputs by defining Pydantic models, enabled function calls by registering tools the LLM can invoke, and injected runtime dependencies with full type safety. You’ve also reviewed practical trade-offs around token costs, latency, and LLM features.

Pydantic AI saves you from error-prone string parsing on LLM responses by validating them against type-safe schemas. It helps you ship reliable LLM features with minimal boilerplate code.

**In this tutorial, you’ve learned how to:**

- Install and configure **Pydantic AI** with an AI provider and an API key
- Define **Pydantic models** to create AI-powered agents that produce structured outputs
- Register tools using the **`@agent.tool`** and **`@agent.tool_plain`** decorators for **function calling**
- Use **dependency injection** for providing type-safe contexts to agents
- Weigh **trade-offs** in **token costs**, **latency**, and **provider support**

With these skills, you can start designing AI-powered agents that return structured data, call external tools, and remain testable and maintainable.

## Next Steps

Now that you understand the core features of Pydantic AI, you can explore more advanced topics:

- **Deepen your Pydantic knowledge**: If you’re new to Pydantic models, Real Python’s tutorial on [Pydantic: Simplifying Data Validation in Python](https://realpython.com/python-pydantic/) covers schemas, field validators, and custom types that will strengthen the patterns you used in this tutorial.
- **Dive into other Pydantic AI features**: If you decide on Pydantic AI, you can explore other features, such as [Model Context Protocol (MCP)](https://realpython.com/ref/ai-coding-glossary/mcp/) support, [multi-agent apps](https://ai.pydantic.dev/multi-agent-applications/), [agent-to-agent communication](https://ai.pydantic.dev/a2a/), and integration with Pydantic [Logfire](https://ai.pydantic.dev/logfire/) for monitoring and [debugging](https://realpython.com/ref/glossary/debugging/).

You can also start creating fun projects, such as a customer service bot, a data analysis assistant, or a workflow automation agent. Pydantic AI’s type-safe architecture helps you ship reliable LLM applications faster.

## Frequently Asked Questions

Now that you have some experience with Pydantic AI in Python, you can use the questions and answers below to check your understanding and recap what you’ve learned.

These FAQs address the most important concepts you’ve covered in this tutorial. Click the _Show/Hide_ toggle beside each question to reveal the answer.

**Can I use Pydantic AI with local or self-hosted models?**Show/Hide

Yes, Pydantic AI supports Ollama for local models and allows custom model adapters for any provider. However, if you’d like to use structured outputs and tool calling, make sure your models support these capabilities.

**Do I need to know Pydantic to use Pydantic AI?**Show/Hide

Basic familiarity helps but isn’t required. If you’ve used Python type hints and `dataclasses`, you can start immediately.

**Is Pydantic AI suitable for production?**Show/Hide

Yes, but consider API costs, rate limits, error handling, monitoring, and latency requirements. Pydantic AI supports async execution, streaming, retries, and other features that are important for production deployments.

**Can agents remember conversation history?**Show/Hide

Yes, agents maintain conversation context across turns. You can persist and restore conversations, though this tutorial focuses on single-shot interactions for simplicity.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-ai-agent-star-race-i-pulled-live-github-data-for-20-fram.md">
<details>
<summary>The AI Agent Star Race: I Pulled Live GitHub Data for 20 Frameworks in May 2026</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4>

# The AI Agent Star Race: I Pulled Live GitHub Data for 20 Frameworks in May 2026

Three months ago, everyone was talking about one project. Today the conversation sounds different — and the GitHub numbers explain why.

I pulled live star counts from the GitHub API for the 20 most-starred open-source AI agent frameworks on May 21, 2026. What I found: a runaway leader still growing, a challenger closing faster than most people realize, and a mid-field cluster where a few hundred stars separate positions 6 through 8.

https://miro.medium.com/v2/resize:fit:672/1*HMKz-DeWYThZzfgLdGPIwQ.jpeg

## TL;DR

- **OpenClaw** leads at 373,616 stars — the most-starred software project in GitHub history, overtaking React in April 2026
- **Hermes Agent** is at 160,175 stars and growing faster per week than OpenClaw was at the same age
- Mid-field (positions 3–8) is packed between 26k and 43k — rankings here can flip in a day
- TypeScript dominates total star weight; Python has the most projects
- Release cadence and star count have almost no correlation

## The Leaderboard (May 21, 2026)

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*Yu68Y0E-e0ak2vNuAs-QeA.png

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*S6fqMR6-3KvC2o-tpjeMSQ.png

## The Two Leaders

**OpenClaw** started in November 2025 when Peter Steinberger built a prototype in about an hour — a TypeScript agent running on your own hardware, talking to you through WhatsApp, Telegram, Slack, and 50+ other messaging platforms. It reached 100,000 stars in 48 hours after its January 30 relaunch and overtook React in April to become GitHub’s most-starred repository ever. 62 tagged releases in the last 30 days — roughly one every 12 hours — is the cadence behind that momentum. It is also a feature and a liability at once, as the sequel to this piece covers. The full story of why growth eventually normalized is in the [OpenClaw rise and fall timeline](https://www.glukhov.org/ai-systems/openclaw/openclaw-rise-and-fall-timeline/).

**Hermes Agent** (Nous Research) launched February 25, 2026. At 160,175 stars after just 12 weeks, it is already growing faster per week than OpenClaw was at the same age. The weekly growth leaderboard makes the gap concrete:

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/1*7nd-y2uyQlczz0y4gF9nqg.png

OpenClaw peaked at +40,000 per week in early February. At +1,700 today it is still growing, but at a mature cadence. Hermes, which persists memory across sessions and writes procedural skill files from successful task completions, drove its momentum into the top of OpenRouter’s daily usage rankings — data for the second article.

## The Mid-field and What to Watch

Positions 3–8 span 26k to 43k stars, meaning any HN post or product launch can shuffle them.

- **Nanobot** (42,873 ⭐) — Python, graph-based orchestration from HKU Data Science lab. Steady, academic.
- **AstrBot** (32,709 ⭐) — 11 releases in 30 days; most active mid-fielder by a distance.
- **ZeroClaw / NanoClaw** (31,500 / 29,143 ⭐) — Rust and TypeScript, performance-focused. NanoClaw migrated from `qwibitai` to `nanocoai` org; only 22 stars separate it from PicoClaw.
- **PicoClaw** (29,121 ⭐) — Go, embedded-device focus. Those 22 stars could flip on one good day of press.
- **AionUi** (26,025 ⭐) — TypeScript, agentic UI generation. Gained ~800 stars since last snapshot.

## Language, Velocity, and What the Stars Miss

TypeScript leads in total star weight (470k) almost entirely because of OpenClaw. Strip that out and Python holds both the count (8 projects) and mass. The Rust tier — ZeroClaw, OpenFang, IronClaw — signals a performance-sensitive niche converging on Rust rather than rewriting Python. Zig and C each have one representative (NullClaw, MimicLaw), suggesting communities that prioritize minimal overhead over ecosystem breadth.

Release velocity and star count barely correlate. OpenClaw ships 62 releases per month; NemoClaw (20k stars) and Moltworker (Cloudflare, 9.9k stars) ship zero. The most interesting ratio belongs to OpenFang (≥5 releases, 17.6k stars) and Moltis (≥3 releases, 2.7k stars) — both punching above their mindshare weight, which usually means a committed user base solving real problems without the marketing that inflates star counts.

> _GitHub stars measure curiosity. OpenRouter token volume, download counts, CVE history, and Reddit sentiment measure what people actually run. Those are in_ [_Part 2_](https://www.glukhov.org/ai-systems/comparisons/openclaw-hermes-alternatives-popularity/) _._

_Full data set with OpenRouter rankings, npm/PyPI downloads, community health, and Reddit sentiment:_ [_glukhov.org_](https://www.glukhov.org/ai-systems/comparisons/openclaw-hermes-alternatives-popularity/)

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